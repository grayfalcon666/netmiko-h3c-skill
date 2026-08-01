#!/usr/bin/env python3
"""
pool_client.py – 连接池服务 HTTP 客户端（纯 stdlib，无第三方依赖）

被 apply_config.py / device_init.py / explore_syntax.py 复用：
  - exec_cmds()   发配置命令（等价原 apply_config）
  - connect()     建立/复用会话并探测当前视图
  - explore()     语法探索（? 探测由服务端完成）
  - disconnect()/status()/health()   会话生命周期管理

也可作为 CLI 使用：
  python3 pool_client.py health
  python3 pool_client.py status [端口]
  python3 pool_client.py disconnect <端口>
  python3 pool_client.py history <端口> [--limit N]
"""

import os
import sys
import json
import argparse
import getpass
import urllib.request
import urllib.error


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

POOL_URL = os.environ.get("NETMIKO_POOL_URL", "http://127.0.0.1:8765")


class PoolError(Exception):
    """连接池服务不可达或响应异常。"""


# --------------------------------------------------------------------------
# 底层请求
# --------------------------------------------------------------------------
def _request(method: str, path: str, payload: dict = None, timeout: int = 15) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(POOL_URL + path, data=data, method=method)
    if payload is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise PoolError(
            f"连接池服务未启动或不可达（{POOL_URL}）。请先运行："
            f"uv run <SKILL目录>/server/connection_pool_server.py"
        ) from e
    except Exception as e:  # JSON 解析等
        raise PoolError(f"连接池服务响应异常: {e}") from e


# --------------------------------------------------------------------------
# API 封装
# --------------------------------------------------------------------------
def health() -> dict:
    return _request("GET", "/health")


def connect(port: int, username: str = None, password: str = None) -> dict:
    payload = {"port": port}
    if username is not None:
        payload["username"] = username
    if password is not None:
        payload["password"] = password
    return _request("POST", "/connect", payload)


def exec_cmds(port: int, commands: list, username: str = None,
              password: str = None, timeout: int = 5) -> dict:
    payload = {"port": port, "commands": list(commands), "timeout": timeout}
    if username is not None:
        payload["username"] = username
    if password is not None:
        payload["password"] = password
    return _request("POST", "/exec", payload)


def explore(port: int, commands: list, base: str, username: str = None,
            password: str = None, timeout: int = 5) -> dict:
    payload = {"port": port, "commands": list(commands), "base": base, "timeout": timeout}
    if username is not None:
        payload["username"] = username
    if password is not None:
        payload["password"] = password
    return _request("POST", "/explore", payload)


def disconnect(port: int) -> dict:
    return _request("POST", "/disconnect", {"port": port})


def status(port: int = None) -> dict:
    path = "/status" if port is None else f"/status?port={port}"
    return _request("GET", path)


def history(port: int, limit: int = None) -> dict:
    path = f"/history?port={port}"
    if limit is not None:
        path += f"&limit={limit}"
    return _request("GET", path)


# --------------------------------------------------------------------------
# 认证参数解析（集中安全规则，供三个客户端脚本复用）
# --------------------------------------------------------------------------
def add_auth_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--user", help="登录用户名（提供则启用认证模式）")
    parser.add_argument("--password", help="登录密码（不安全，建议用 --password-env 或交互输入）")
    parser.add_argument("--password-env", help="从环境变量读取密码，指定变量名")


def resolve_password(args) -> tuple:
    """
    解析认证参数，返回 (username, password)。
    无认证时返回 (None, None)；password 为 None 表示无认证。
    优先级：--password-env > 交互 getpass > --password（带警告）。
    """
    if not args.user:
        return None, None
    if args.password_env:
        password = os.environ.get(args.password_env)
        if password is None:
            print(json.dumps({"status": "error", "error": f"环境变量 {args.password_env} 未设置。"}))
            sys.exit(1)
        return args.user, password
    if args.password:
        sys.stderr.write("警告：密码通过命令行传递不安全，建议使用 --password-env 或交互式输入。\n")
        return args.user, args.password
    return args.user, getpass.getpass("请输入设备密码: ")


# --------------------------------------------------------------------------
# CLI 入口（生命周期管理）
# --------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="H3C 连接池服务客户端")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("health", help="检查服务是否存活")
    p_status = sub.add_parser("status", help="列出会话")
    p_status.add_argument("port", nargs="?", type=int, help="可选：指定端口")
    p_dis = sub.add_parser("disconnect", help="断开指定端口会话")
    p_dis.add_argument("port", type=int)
    p_hist = sub.add_parser("history", help="读取指定端口会话历史")
    p_hist.add_argument("port", type=int)
    p_hist.add_argument("--limit", type=int, default=None, help="返回最近 N 条（默认 100）")
    args = parser.parse_args()

    try:
        if args.cmd == "health":
            result = health()
        elif args.cmd == "status":
            result = status(args.port if "port" in args else None)
        elif args.cmd == "history":
            result = history(args.port, args.limit)
        else:  # disconnect
            result = disconnect(args.port)
    except PoolError as e:
        print(json.dumps({"status": "error", "error": str(e)}))
        sys.exit(1)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
