#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["netmiko", "fastapi", "uvicorn"]
# ///
"""
connection_pool_server.py – H3C 设备 Telnet 连接池后端服务

为三个客户端脚本（apply_config.py / device_init.py / explore_syntax.py）提供常驻连接池，
池化保持 Telnet 连接并跨请求保持视图状态。每次 /exec 前用 find_prompt() + 正则探测当前视图，
返回 start_view / end_view，由调用方（AI）用命令导航视图。

启动：
  uv run server/connection_pool_server.py            # 默认 127.0.0.1:8765
  NETMIKO_POOL_HOST=127.0.0.1 NETMIKO_POOL_PORT=9000 uv run server/connection_pool_server.py

安全：密码仅存内存，日志只记 端口+操作名+status+耗时，绝不记录命令正文、设备输出或密码。
"""

import os
import re
import sys
import time
import json
import threading
import logging
from contextlib import asynccontextmanager
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator
from fastapi import FastAPI
import uvicorn
import netmiko
from netmiko import ConnectHandler


def load_dotenv() -> None:
    """从仓库根目录加载 .env（若存在），不覆盖已存在的环境变量。纯标准库实现。"""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(root, ".env")
    if not os.path.isfile(path):
        return
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                if line.startswith("export "):
                    line = line[7:].strip()
                key, _, val = line.partition("=")
                key = key.strip()
                if key and key not in os.environ:
                    os.environ[key] = val.strip().strip("\"'")
    except OSError:
        pass


load_dotenv()

# --------------------------------------------------------------------------
# 日志：只记端口+操作名+status+耗时，杜绝敏感信息
# --------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("pool-server")

# 设备固定 IP（可用环境变量覆盖，便于用 mock 设备做本地端到端验证）
DEVICE_IP = os.environ.get("NETMIKO_POOL_DEVICE_IP", "192.168.56.1")
MAX_COMMANDS = 5

# 数据持久化：会话描述符 + 每端口历史记录
HISTORY_MAX = 1000                                # 每端口历史保留的最大行数，超出截断
DEFAULT_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DATA_DIR = os.environ.get("NETMIKO_POOL_DATA_DIR", DEFAULT_DATA_DIR)
SESSION_FILE = os.path.join(DATA_DIR, "pool_sessions.json")
_io_lock = threading.Lock()                       # 描述符/历史文件写盘互斥


# --------------------------------------------------------------------------
# 视图探测（纯函数，可单测）
# --------------------------------------------------------------------------
PROMPT_USER = re.compile(r"^<([^<>]+)>$")       # <H3C>          -> 用户视图
PROMPT_SUB = re.compile(r"^\[([^\]]+)\]$")      # [H3C] 或 [H3C-GigabitEthernet1/0/1]


def _is_subview_path(path: str) -> bool:
    """启发式判断 [host-path] 中的 path 是否为子视图名。

    主机名常含 '-'（如 [SW-1]、[SW-Core-01]），故不能简单按第一个 '-' 切分即判子视图。
    子视图路径几乎总是：
      - 含 '/'（接口视图，如 GigabitEthernet1/0/1）
      - 或 字母后紧跟数字（如 vlan100、Vlan-interface100、AR1）
    """
    if not path:
        return False
    if "/" in path:
        return True
    return bool(re.search(r"[A-Za-z]+[0-9]", path))


def parse_view(prompt: str) -> dict:
    """
    解析 H3C 提示符，返回结构化视图信息：
    {"prompt":..., "view": "user"|"system"|"subview", "hostname":..., "path":...}
    无法识别时抛 ValueError。
    """
    prompt = (prompt or "").strip()
    m = PROMPT_USER.match(prompt)
    if m:
        return {"prompt": prompt, "view": "user", "hostname": m.group(1).strip(), "path": ""}
    m = PROMPT_SUB.match(prompt)
    if m:
        inner = m.group(1).strip()               # 如 'H3C-GigabitEthernet1/0/1' 或 'SW-1'
        hostname, _, sub = inner.partition("-")
        view = "subview" if _is_subview_path(sub) else "system"
        return {
            "prompt": prompt,
            "view": view,
            "hostname": hostname.strip(),
            "path": sub if view == "subview" else "",
        }
    raise ValueError(f"无法识别的提示符: {prompt!r}")


def detect_view(conn) -> dict:
    """基于 netmiko find_prompt() 探测当前视图。"""
    return parse_view(conn.find_prompt())


def safe_detect(session) -> Optional[dict]:
    """尽力探测视图；失败（断连/无响应）返回 None。"""
    try:
        if session.conn is None:
            return None
        return detect_view(session.conn)
    except Exception:
        return None


_PROMPT_RE = re.compile(r'[\[<][^\]>]*[\]>]')


def probe_alive(session, timeout: float = 3.0) -> bool:
    """有界往返存活探测：发空行，要求超时内设备回显提示符。

    netmiko 的 is_alive() 只发 IAC NOP 再读 1 字节，把"活但静默"和"死但静默"
    都判为存活，无法发现设备重启/半开连接（尤其中间有透明代理时）。此探测要求
    真实提示符回显，失败即视为死连接；调用方据此断开并重建。
    """
    conn = session.conn
    if conn is None:
        return False
    try:
        out = conn.send_command_timing("", read_timeout=timeout)
    except Exception:
        return False
    return bool(out) and bool(_PROMPT_RE.search(out))


# --------------------------------------------------------------------------
# 导航路径（nav_path）：从用户视图重放到当前视图的命令序列，用于重启/重连后恢复
# --------------------------------------------------------------------------
def update_nav_path(nav_path, cmd):
    """根据已发送命令更新导航路径。纯函数，返回新列表。"""
    cmd = (cmd or "").strip()
    low = cmd.lower()
    out = list(nav_path or [])
    if low == "return":
        return []
    if low == "quit":
        return out[:-1]
    if low == "system-view":
        return out if out else ["system-view"]
    if low.startswith("interface ") or low.startswith("vlan "):
        out.append(cmd)
    return out


_VLAN_RE = re.compile(r"^[Vv]lan(\d+)$")
_VLAN_IF_RE = re.compile(r"^[Vv]lan-[Ii]nterface(\d+)$")
_INTERFACE_RE = re.compile(r"[A-Za-z]+[0-9]+(?:/[0-9]+)*")


def reconcile_nav_path(nav_path, end_view):
    """用探测到的 end_view 对账导航路径（end_view 是 ground truth）。纯函数。

    - user 视图 → []；system 视图 → ["system-view"]。
    - 子视图：trace 尾项与 path 相关则保留 trace；否则按 path 生成最小导航
      （interface X / vlan N / Vlan-interface N）。嵌套子视图无法从单段 path 重建时
      靠命令跟踪兜底（保留 trace）。
    - end_view 为 None 时原样返回。
    """
    if not end_view or not end_view.get("view"):
        return list(nav_path or [])
    view = end_view["view"]
    path = (end_view.get("path") or "").strip()
    if view == "user":
        return []
    if view == "system":
        return ["system-view"]
    nav = list(nav_path or [])
    if nav:
        tail = nav[-1].strip().lower()
        if path and (path.lower() in tail or tail.endswith(path.lower())):
            return nav
    if path:
        m = _VLAN_RE.match(path)
        if m:
            return ["system-view", f"vlan {int(m.group(1))}"]
        if _VLAN_IF_RE.match(path) or _INTERFACE_RE.search(path):
            return ["system-view", f"interface {path}"]
    return nav


def restore_view(conn, nav_path):
    """尽力重放导航命令恢复视图；命令报错或连接异常即停。返回实际视图 dict（探测失败为 None）。"""
    for cmd in (nav_path or []):
        if not cmd or not isinstance(cmd, str):
            continue
        try:
            out = conn.send_command_timing(cmd, read_timeout=8)
        except Exception:
            break
        if has_error(out):
            break
    try:
        return detect_view(conn)
    except Exception:
        return None


# --------------------------------------------------------------------------
# 命令输出错误检测（从原 apply_config.py 原样迁移）
# --------------------------------------------------------------------------
def has_error(output: str) -> bool:
    """检查命令输出是否包含错误关键字。忽略 % Unrecognized command（由 return 在用户视图引起）。"""
    cleaned = re.sub(r'^\s*% Unrecognized command.*\n?', '', output or '', flags=re.MULTILINE).strip()
    if not cleaned:
        return False
    error_patterns = [
        r'% Unknown command',
        r'%\s*\^',                 # 错误定位符
        r'Incomplete command',
        r'Invalid',
        r'Error',
        r'Too many parameters',
        r'Wrong parameter',
    ]
    for pat in error_patterns:
        if re.search(pat, cleaned, re.IGNORECASE):
            return True
    return False


# --------------------------------------------------------------------------
# 密码脱敏（防御性：即使异常文本含密码也替换掉）
# --------------------------------------------------------------------------
def sanitize(text: str, secrets: List[str]) -> str:
    """把文本中出现过的所有敏感串替换为 ***。"""
    out = text or ""
    for s in secrets:
        if s:
            out = out.replace(s, "***")
    return out


# --------------------------------------------------------------------------
# 连接池
# --------------------------------------------------------------------------
class Session:
    """单个设备（端口）的池化 Telnet 会话。"""

    def __init__(self, port: int, username: str = "", password: Optional[str] = None):
        self.port = port
        self.username = username
        self.password = password              # 仅内存，绝不落盘/落日志
        self.conn = None                      # netmiko ConnectHandler
        self.lock = threading.Lock()          # 每设备一把锁，串行化该端口全部操作
        self.last_used = time.time()
        self.has_auth = bool(username and password is not None)
        self.device_type = "hp_comware_telnet" if self.has_auth else "generic_telnet"
        self.nav_path: List[str] = []         # 从用户视图重放到当前视图的导航命令序列（持久化恢复用）

    @property
    def connected(self) -> bool:
        return self.conn is not None and self.conn.is_alive()


class ConnectionPool:
    def __init__(self, device_ip: str = DEVICE_IP, idle_timeout: int = 300, reaper_interval: int = 60):
        self.device_ip = device_ip
        self.idle_timeout = idle_timeout
        self.reaper_interval = reaper_interval
        self._sessions: dict = {}
        self._pool_lock = threading.Lock()
        self._stop_event = threading.Event()
        self._reaper_thread = None
        self._descriptors: dict = {}          # port -> {username, nav_path}，持久化恢复计划（不含密码）

    # ---- 会话获取 ----
    def _seed_from_descriptor(self, session: Session) -> Session:
        """新建会话时从持久化描述符播种导航路径（认证设备懒恢复的关键）。"""
        desc = self._descriptors.get(session.port)
        if desc:
            session.nav_path = list(desc.get("nav_path") or [])
        return session

    def get_or_create(self, port: int, username: str = "", password: Optional[str] = None) -> Session:
        with self._pool_lock:
            session = self._sessions.get(port)
            if session is None:
                session = self._seed_from_descriptor(Session(port, username, password))
                self._sessions[port] = session
                return session
            # 认证签名变化（有/无认证）时断开旧连接并重建
            new_auth = bool(username and password is not None)
            if new_auth != session.has_auth or (session.username or "") != (username or ""):
                conn = session.conn
                session.conn = None
                session.password = None
                if conn:
                    try:
                        conn.disconnect()
                    except Exception:
                        pass
                session = self._seed_from_descriptor(Session(port, username, password))
                self._sessions[port] = session
            return session

    def _create_conn(self, session: Session):
        device = {
            "device_type": session.device_type,
            "ip": self.device_ip,
            "port": session.port,
            "username": session.username,
            "password": session.password or "",
            "global_delay_factor": 1,
            "conn_timeout": 10,
        }
        return ConnectHandler(**device)

    def ensure_connected(self, session: Session) -> None:
        """懒建连：连接为空或已断时重建。分屏在建连时一次性关闭。

        存活判定用有界往返探测（probe_alive）而非 is_alive()：设备重启后旧连接
        半开，is_alive 无法发现，这里要求真实提示符回显，失败即断开重建。
        """
        if session.conn is not None:
            if probe_alive(session):
                return
            try:
                session.conn.disconnect()
            except Exception:
                pass
            session.conn = None
        session.conn = self._create_conn(session)
        # 无认证用 generic_telnet，netmiko 不会自动关分屏，补一次
        if session.device_type == "generic_telnet":
            session.conn.send_command_timing("screen-length disable", read_timeout=10)
        # 新连接默认回到用户视图：若有保存的导航路径则重放恢复，并据此对账后落盘
        if session.nav_path:
            actual = restore_view(session.conn, session.nav_path)
            session.nav_path = reconcile_nav_path(session.nav_path, actual)
            self._save_descriptor(session)

    # ---- 断连与清理 ----
    def drop_session(self, session: Session) -> None:
        with self._pool_lock:
            if self._sessions.get(session.port) is session:
                del self._sessions[session.port]
        conn = session.conn
        session.conn = None
        session.password = None
        if conn:
            try:
                conn.disconnect()
            except Exception:
                pass

    def list_sessions(self, port: Optional[int] = None) -> List[dict]:
        with self._pool_lock:
            sessions = [self._sessions[port]] if port is not None and port in self._sessions else list(self._sessions.values())
        now = time.time()
        out = []
        for s in sessions:
            # 有界往返探测（非阻塞加锁，避开正在执行的命令）：死连接不挂起、不显示假视图
            if s.lock.acquire(blocking=False):
                try:
                    alive = probe_alive(s, timeout=3.0)
                    view = safe_detect(s) if alive else None
                except Exception:
                    alive, view = False, None
                finally:
                    s.lock.release()
            else:
                alive = s.connected
                view = safe_detect(s) if alive else None
            out.append({
                "port": s.port,
                "connected": alive,
                "auth": "user" if s.has_auth else "none",
                "view": view,
                "idle_seconds": round(now - s.last_used, 1),
            })
        return out

    # ---- 后台回收线程 ----
    def start_reaper(self) -> None:
        self._stop_event.clear()
        self._reaper_thread = threading.Thread(target=self._reaper_loop, daemon=True, name="pool-reaper")
        self._reaper_thread.start()

    def _reaper_loop(self) -> None:
        while not self._stop_event.wait(self.reaper_interval):
            self._reap_idle()

    def _reap_idle(self) -> None:
        now = time.time()
        with self._pool_lock:
            sessions = list(self._sessions.values())
        for s in sessions:
            if now - s.last_used > self.idle_timeout:
                if s.lock.acquire(blocking=False):     # 忙碌中则跳过，避免打断进行中的命令
                    try:
                        self.drop_session(s)
                    finally:
                        s.lock.release()

    def shutdown_all(self) -> None:
        self._stop_event.set()
        with self._pool_lock:
            sessions = list(self._sessions.values())
            self._sessions.clear()
        for s in sessions:
            conn = s.conn
            s.conn = None
            s.password = None
            if conn:
                try:
                    conn.disconnect()
                except Exception:
                    pass

    # ---- 持久化（会话描述符，绝不包含密码）----
    def save_state(self) -> None:
        """把会话描述符写入磁盘（原子写：临时文件 + rename）。"""
        with self._pool_lock:
            descriptors = [
                {"port": p, "username": d.get("username", "") or "",
                 "nav_path": list(d.get("nav_path") or [])}
                for p, d in self._descriptors.items()
            ]
        try:
            os.makedirs(DATA_DIR, exist_ok=True)
            tmp = SESSION_FILE + ".tmp"
            with _io_lock:
                with open(tmp, "w", encoding="utf-8") as f:
                    json.dump(descriptors, f, ensure_ascii=False, indent=2)
                os.replace(tmp, SESSION_FILE)
        except OSError:
            logger.warning("写入会话状态失败: %s", SESSION_FILE)

    def load_state(self) -> None:
        """从磁盘加载会话描述符到 self._descriptors；缺失/损坏则置空重建。"""
        try:
            with open(SESSION_FILE, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):
            self._descriptors = {}
            return
        out = {}
        for d in data if isinstance(data, list) else []:
            try:
                port = int(d.get("port"))
                out[port] = {
                    "username": (d.get("username") or "") or "",
                    "nav_path": [c for c in (d.get("nav_path") or []) if isinstance(c, str)],
                }
            except (TypeError, ValueError):
                continue
        self._descriptors = out

    def _save_descriptor(self, session: Session) -> None:
        """更新单个会话描述符并落盘。"""
        with self._pool_lock:
            self._descriptors[session.port] = {
                "username": session.username or "",
                "nav_path": list(session.nav_path),
            }
        self.save_state()

    def remove_descriptor(self, port: int) -> None:
        """/disconnect 时移除该端口的恢复计划。"""
        with self._pool_lock:
            self._descriptors.pop(port, None)
        self.save_state()

    def sync_session(self, session: Session, end_view) -> None:
        """批末副作用：用探测到的 end_view 对账导航路径 + 写描述符。"""
        session.nav_path = reconcile_nav_path(session.nav_path, end_view)
        self._save_descriptor(session)


# --------------------------------------------------------------------------
# 历史记录（每端口一个 jsonl，命令与输出，绝不包含密码）
# --------------------------------------------------------------------------
def history_path(port: int) -> str:
    return os.path.join(DATA_DIR, f"history_{port}.jsonl")


def append_history(port: int, entry: dict) -> None:
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        path = history_path(port)
        with _io_lock:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            _trim_history(path)
    except OSError:
        logger.warning("写入历史失败: %s", history_path(port))


def _trim_history(path: str) -> None:
    """保留最近 HISTORY_MAX 行，防止无限膨胀。"""
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) > HISTORY_MAX:
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines[-HISTORY_MAX:])
    except OSError:
        pass


def read_history(port: int, limit: Optional[int] = None) -> List[dict]:
    limit = limit or 100
    try:
        with open(history_path(port), encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return []
    out = []
    for line in lines[-limit:]:
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except ValueError:
            continue
    return out


def _history_entry(session: Session, op: str, commands, outputs, status,
                   start_view, end_view, failed_index=None, error=None) -> dict:
    """构造历史条目。命令/输出原样记录；绝不写入密码（凭据独立传参，命令正文不含）。"""
    return {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "port": session.port,
        "op": op,
        "commands": list(commands),
        "output": "\n".join(outputs) if outputs else "",
        "status": status,
        "start_view": start_view,
        "end_view": end_view,
        "failed_index": failed_index,
        "error": error,
    }


pool = ConnectionPool()


# --------------------------------------------------------------------------
# FastAPI 应用与生命周期
# --------------------------------------------------------------------------
def _restore_noauth_in_background() -> None:
    """无认证设备启动即自动重连+恢复视图；失败静默保留描述符，下次懒恢复兜底。"""
    for port, desc in pool._descriptors.items():
        if desc.get("username"):
            continue  # 认证设备懒恢复（等 AI 带凭据调用）
        def _restore(p=port):
            try:
                s = pool.get_or_create(p)
                with s.lock:
                    pool.ensure_connected(s)
            except Exception:
                pass
        threading.Thread(target=_restore, daemon=True, name=f"restore-{port}").start()


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.load_state()
    pool.start_reaper()
    _restore_noauth_in_background()
    yield
    pool.save_state()
    pool.shutdown_all()


app = FastAPI(title="H3C Netmiko 连接池服务", version="1.0", lifespan=lifespan)


# --------------------------------------------------------------------------
# 请求模型
# --------------------------------------------------------------------------
class ConnectRequest(BaseModel):
    port: int
    username: Optional[str] = None
    password: Optional[str] = None


class ExecRequest(BaseModel):
    port: int
    commands: List[str] = Field(default_factory=list)
    timeout: int = 5
    username: Optional[str] = None
    password: Optional[str] = None

    @field_validator("commands")
    @classmethod
    def _limit_commands(cls, v: List[str]) -> List[str]:
        if len(v) > MAX_COMMANDS:
            raise ValueError(f"单次最多执行 {MAX_COMMANDS} 条命令")
        return v


class ExploreRequest(BaseModel):
    port: int
    commands: List[str] = Field(default_factory=list)   # 前置子视图命令
    base: str                                           # 待探索的不完整命令
    timeout: int = 5
    username: Optional[str] = None
    password: Optional[str] = None


class DisconnectRequest(BaseModel):
    port: int


# --------------------------------------------------------------------------
# 端点
# --------------------------------------------------------------------------
@app.get("/health")
def health() -> dict:
    with pool._pool_lock:
        n = len(pool._sessions)
    return {"status": "ok", "sessions": n}


@app.get("/status")
def status(port: Optional[int] = None) -> dict:
    return {"status": "success", "sessions": pool.list_sessions(port)}


@app.get("/history")
def history_endpoint(port: Optional[int] = None, limit: Optional[int] = None) -> dict:
    """返回指定端口的历史消息（命令+输出，最近 limit 条，默认 100）。"""
    if port is None:
        return {"status": "error", "error": "缺少 port 参数", "history": []}
    return {"status": "success", "port": port, "history": read_history(port, limit)}


@app.post("/connect")
def connect(req: ConnectRequest) -> dict:
    t0 = time.time()
    username = req.username or ""
    secrets = [req.password] if req.password else []
    session = pool.get_or_create(req.port, username, req.password)
    try:
        with session.lock:
            pool.ensure_connected(session)
            view = detect_view(session.conn)
            session.last_used = time.time()
        pool.sync_session(session, view)
        append_history(session.port, _history_entry(session, "connect", [], [], "success", view, view))
        logger.info("op=connect port=%s status=success dur_ms=%s", req.port, int((time.time() - t0) * 1000))
        return {"status": "success", "port": req.port, "view": view}
    except Exception as e:
        pool.drop_session(session)
        append_history(session.port, _history_entry(
            session, "connect", [], [], "error", None, None,
            error="连接失败: " + sanitize(str(e), secrets)))
        logger.info("op=connect port=%s status=error dur_ms=%s", req.port, int((time.time() - t0) * 1000))
        return {"status": "error", "port": req.port, "view": None, "error": sanitize(str(e), secrets)}


@app.post("/exec")
def exec_endpoint(req: ExecRequest) -> dict:
    t0 = time.time()
    username = req.username or ""
    secrets = [req.password] if req.password else []
    session = pool.get_or_create(req.port, username, req.password)
    start_view = None
    end_view = None
    outputs = []
    status = "error"
    failed_index = None
    error = None
    try:
        with session.lock:
            try:
                pool.ensure_connected(session)
            except Exception as e:
                pool.drop_session(session)
                error = "连接设备失败: " + sanitize(str(e), secrets)
                _finish_exec(session, start_view, None, [], status, None, error, req, t0)
                return _exec_result(req.port, start_view, None, [], status, None, error)

            start_view = safe_detect(session)
            for i, cmd in enumerate(req.commands):
                cmd = (cmd or "").strip()
                if not cmd:
                    continue
                try:
                    out = session.conn.send_command_timing(cmd, read_timeout=req.timeout)
                except Exception as e:
                    end_view = safe_detect(session)
                    failed_index = i
                    if end_view is None:
                        pool.drop_session(session)
                        error = "连接中断，下个请求将自动重建: " + sanitize(str(e), secrets)
                    else:
                        error = "命令执行异常: " + sanitize(str(e), secrets)
                    _finish_exec(session, start_view, end_view, outputs, status, failed_index, error, req, t0)
                    return _exec_result(req.port, start_view, end_view, outputs, status, failed_index, error)
                outputs.append(out)
                if has_error(out):
                    end_view = safe_detect(session)
                    failed_index = i
                    error = f"命令 '{cmd}' 执行失败"
                    _finish_exec(session, start_view, end_view, outputs, status, failed_index, error, req, t0)
                    return _exec_result(req.port, start_view, end_view, outputs, status, failed_index, error)

            end_view = safe_detect(session)
            session.last_used = time.time()
            status = "success"
    except Exception as e:
        pool.drop_session(session)
        error = "未知错误: " + sanitize(str(e), secrets)
    _finish_exec(session, start_view, end_view, outputs, status, failed_index, error, req, t0)
    return _exec_result(req.port, start_view, end_view, outputs, status, failed_index, error)


def _exec_result(port, start_view, end_view, outputs, status, failed_index, error):
    return {
        "status": status,
        "start_view": start_view,
        "end_view": end_view,
        "output": "\n".join(outputs) if outputs else "",
        "error": error,
        "failed_index": failed_index,
    }


def _finish_exec(session, start_view, end_view, outputs, status, failed_index, error, req, t0):
    """exec 批末副作用：对账导航路径、写描述符、记历史、记日志。"""
    pool.sync_session(session, end_view)
    append_history(session.port, _history_entry(
        session, "exec", req.commands, outputs, status,
        start_view, end_view, failed_index, error))
    logger.info("op=exec port=%s status=%s dur_ms=%s",
                session.port, status, int((time.time() - t0) * 1000))


@app.post("/disconnect")
def disconnect(req: DisconnectRequest) -> dict:
    with pool._pool_lock:
        session = pool._sessions.pop(req.port, None)
    if session:
        conn = session.conn
        session.conn = None
        session.password = None
        if conn:
            try:
                conn.disconnect()
            except Exception:
                pass
    pool.remove_descriptor(req.port)
    append_history(req.port, {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "port": req.port, "op": "disconnect",
        "commands": [], "output": "", "status": "success",
        "start_view": None, "end_view": None,
        "failed_index": None, "error": None,
    })
    return {"status": "success", "port": req.port}


# --------------------------------------------------------------------------
# 语法探索（原 explore_syntax.py 逻辑迁入）
# --------------------------------------------------------------------------
def extract_help_lines(raw_output: str) -> str:
    """只保留以至少两个空格缩进、且不以 '[' 开头的行（Comware 帮助选项铁律）。"""
    lines = []
    for line in (raw_output or "").splitlines():
        if line.startswith("  ") and not line.strip().startswith("["):
            lines.append(line)
    return "\n".join(lines)


def parse_help_output(output: str) -> List[str]:
    ignore_pattern = re.compile(r'^\s*(%|Error|----|<cr>|\^|$)')
    options = []
    for line in output.splitlines():
        line_stripped = line.strip()
        if not line.startswith('  ') or line_stripped.startswith('['):
            continue
        if ignore_pattern.match(line_stripped):
            continue
        words = line_stripped.split()
        if not words:
            continue
        opt = words[0].rstrip('.,;')
        if opt and not opt.isdigit():
            options.append(opt)
    seen = set()
    unique = []
    for o in options:
        if o not in seen:
            seen.add(o)
            unique.append(o)
    return unique


def is_parameter_type(opt: str) -> bool:
    return opt.startswith('<')


def explore_syntax(conn, base_cmd: str):
    """逐级探索命令语法，返回 (成功标志, chain, info)。"""
    chain = []
    current_prefix = base_cmd.strip()
    max_depth = 10
    for _ in range(max_depth):
        raw_output = conn.send_command_timing(
            f"{current_prefix} ?", strip_prompt=False, strip_command=False
        )
        output = extract_help_lines(raw_output)
        if re.search(r'% Unknown command|% Unrecognized command|Error', raw_output, re.IGNORECASE):
            return True, chain, f"探索停止于 '{current_prefix}'，设备返回错误"
        options = parse_help_output(output)
        if not options:
            return True, chain, f"'{current_prefix}' 没有更多可用选项。"
        if len(options) == 1:
            opt = options[0]
            if is_parameter_type(opt):
                probe_raw = conn.send_command_timing(
                    f"{current_prefix} 1 ?", strip_prompt=False, strip_command=False
                )
                probe_output = extract_help_lines(probe_raw)
                if re.search(r'% Unknown command|% Unrecognized command|Error', probe_raw, re.IGNORECASE):
                    return True, chain, f"'{current_prefix}' 后参数为终点，停止探索。"
                elif not parse_help_output(probe_output):
                    return True, chain, f"'{current_prefix}' 后参数为终点，停止探索。"
                else:
                    chain.append({"prefix": current_prefix, "options": [opt], "type": "parameter"})
                    current_prefix = f"{current_prefix} 1"
                    continue
            else:
                chain.append({"prefix": current_prefix, "options": [opt], "type": "keyword"})
                current_prefix = f"{current_prefix} {opt}"
                continue
        else:
            chain.append({"prefix": current_prefix, "options": options, "type": "multiple"})
            break
    return True, chain, ""


def _finish_explore(session, req, start_view, end_view, status, chain, info, error, t0):
    """explore 批末副作用：对账导航路径、写描述符、记历史、记日志。"""
    pool.sync_session(session, end_view)
    append_history(session.port, _history_entry(
        session, "explore", list(req.commands) + [req.base], [info] if info else [],
        status, start_view, end_view, None, error))
    logger.info("op=explore port=%s status=%s dur_ms=%s",
                session.port, status, int((time.time() - t0) * 1000))


@app.post("/explore")
def explore_endpoint(req: ExploreRequest) -> dict:
    t0 = time.time()
    username = req.username or ""
    secrets = [req.password] if req.password else []
    session = pool.get_or_create(req.port, username, req.password)
    start_view = None
    end_view = None
    try:
        with session.lock:
            try:
                pool.ensure_connected(session)
            except Exception as e:
                pool.drop_session(session)
                return {"status": "error", "error": "连接设备失败: " + sanitize(str(e), secrets),
                        "chain": [], "info": "", "start_view": None, "end_view": None}
            start_view = safe_detect(session)
            for cmd in req.commands:
                out = session.conn.send_command_timing(cmd, strip_prompt=False, strip_command=False)
                if re.search(r'Error|Unknown command|Unrecognized command', out, re.IGNORECASE):
                    end_view = safe_detect(session)
                    status = "error"
                    error = f"前置命令 '{cmd}' 执行失败"
                    session.last_used = time.time()
                    _finish_explore(session, req, start_view, end_view, status, [], "", error, t0)
                    return {"status": status, "error": error,
                            "chain": [], "info": "", "start_view": start_view, "end_view": end_view}
            success, chain, info = explore_syntax(session.conn, req.base)
            end_view = safe_detect(session)
            session.last_used = time.time()
            status = "success" if success else "error"
            error = None if success else "语法探索失败"
        _finish_explore(session, req, start_view, end_view, status, chain, info, error, t0)
        return {"status": status, "chain": chain, "info": info,
                "start_view": start_view, "end_view": end_view}
    except Exception as e:
        pool.drop_session(session)
        return {"status": "error", "error": sanitize(str(e), secrets), "chain": [], "info": "",
                "start_view": start_view, "end_view": None}


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------
def main() -> None:
    host = os.environ.get("NETMIKO_POOL_HOST", "127.0.0.1")
    port = int(os.environ.get("NETMIKO_POOL_PORT", "8765"))
    print(f"连接池服务启动: http://{host}:{port}  (设备地址 {DEVICE_IP})", flush=True)
    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
