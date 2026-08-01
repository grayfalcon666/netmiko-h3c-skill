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

    # ---- 会话获取 ----
    def get_or_create(self, port: int, username: str = "", password: Optional[str] = None) -> Session:
        with self._pool_lock:
            session = self._sessions.get(port)
            if session is None:
                session = Session(port, username, password)
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
                session = Session(port, username, password)
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
        """懒建连：连接为空或已断时重建。分屏在建连时一次性关闭。"""
        if session.conn is not None:
            try:
                if session.conn.is_alive():
                    return
            except Exception:
                pass
        if session.conn is not None:
            try:
                session.conn.disconnect()
            except Exception:
                pass
        session.conn = self._create_conn(session)
        # 无认证用 generic_telnet，netmiko 不会自动关分屏，补一次
        if session.device_type == "generic_telnet":
            session.conn.send_command_timing("screen-length disable", read_timeout=10)

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
            view = safe_detect(s)
            out.append({
                "port": s.port,
                "connected": s.connected,
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


pool = ConnectionPool()


# --------------------------------------------------------------------------
# FastAPI 应用与生命周期
# --------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.start_reaper()
    yield
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
        logger.info("op=connect port=%s status=success dur_ms=%s", req.port, int((time.time() - t0) * 1000))
        return {"status": "success", "port": req.port, "view": view}
    except Exception as e:
        pool.drop_session(session)
        logger.info("op=connect port=%s status=error dur_ms=%s", req.port, int((time.time() - t0) * 1000))
        return {"status": "error", "port": req.port, "view": None, "error": sanitize(str(e), secrets)}


@app.post("/exec")
def exec_endpoint(req: ExecRequest) -> dict:
    t0 = time.time()
    username = req.username or ""
    secrets = [req.password] if req.password else []
    session = pool.get_or_create(req.port, username, req.password)
    start_view = None
    try:
        with session.lock:
            try:
                pool.ensure_connected(session)
            except Exception as e:
                pool.drop_session(session)
                return _err(req.port, start_view, None, "连接设备失败", sanitize(str(e), secrets), None, t0)

            start_view = safe_detect(session)
            outputs = []
            for i, cmd in enumerate(req.commands):
                cmd = (cmd or "").strip()
                if not cmd:
                    continue
                try:
                    out = session.conn.send_command_timing(cmd, read_timeout=req.timeout)
                except Exception as e:
                    end_view = safe_detect(session)
                    if end_view is None:
                        pool.drop_session(session)
                        return _err(req.port, start_view, None, "连接中断，下个请求将自动重建", sanitize(str(e), secrets), i, t0)
                    return _err(req.port, start_view, end_view, "命令执行异常", sanitize(str(e), secrets), i, t0)
                outputs.append(out)
                if has_error(out):
                    end_view = safe_detect(session)
                    return _err(req.port, start_view, end_view, f"命令 '{cmd}' 执行失败", None, i, t0, outputs=outputs)

            end_view = safe_detect(session)
            session.last_used = time.time()
        logger.info("op=exec port=%s status=success dur_ms=%s", req.port, int((time.time() - t0) * 1000))
        return {
            "status": "success",
            "start_view": start_view,
            "end_view": end_view,
            "output": "\n".join(outputs),
            "error": None,
            "failed_index": None,
        }
    except Exception as e:
        pool.drop_session(session)
        logger.info("op=exec port=%s status=error dur_ms=%s", req.port, int((time.time() - t0) * 1000))
        return _err(req.port, start_view, None, "未知错误", sanitize(str(e), secrets), None, t0)


def _err(port, start_view, end_view, error, err_detail, failed_index, t0, outputs=None):
    logger.info("op=exec port=%s status=error dur_ms=%s", port, int((time.time() - t0) * 1000))
    if err_detail:
        error = f"{error}: {err_detail}"
    return {
        "status": "error",
        "start_view": start_view,
        "end_view": end_view,
        "output": "\n".join(outputs) if outputs else "",
        "error": error,
        "failed_index": failed_index,
    }


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


@app.post("/explore")
def explore_endpoint(req: ExploreRequest) -> dict:
    t0 = time.time()
    username = req.username or ""
    secrets = [req.password] if req.password else []
    session = pool.get_or_create(req.port, username, req.password)
    start_view = None
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
                    return {"status": "error", "error": f"前置命令 '{cmd}' 执行失败",
                            "chain": [], "info": "", "start_view": start_view,
                            "end_view": safe_detect(session)}
            success, chain, info = explore_syntax(session.conn, req.base)
            end_view = safe_detect(session)
            session.last_used = time.time()
        logger.info("op=explore port=%s status=%s dur_ms=%s", req.port,
                    "success" if success else "error", int((time.time() - t0) * 1000))
        return {"status": "success" if success else "error", "chain": chain, "info": info,
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
