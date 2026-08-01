#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
apply_config.py – 通过连接池服务对 H3C 设备执行配置命令（最多 5 条）

作为 server/connection_pool_server.py 的 HTTP 客户端。会话与视图状态由服务端保持，
每次调用返回 start_view / end_view，供调用方（AI）判断当前视图并导航。

用法：
  无认证：python3 apply_config.py <端口号> "<命令1>" "<命令2>" ...
  有认证：python3 apply_config.py <端口号> "<命令1>" ... --user <用户名>
           （密码交互输入，或用 --password-env <环境变量名>）
"""

import sys
import json
import argparse

import pool_client


def main() -> None:
    parser = argparse.ArgumentParser(
        description="通过连接池服务对 H3C 设备执行配置命令（最多 5 条）"
    )
    parser.add_argument("port", type=int, help="Telnet 端口号")
    parser.add_argument("commands", nargs="+", help="要执行的配置命令（最多 5 条），用空格分隔并加引号")
    pool_client.add_auth_args(parser)
    args = parser.parse_args()

    # 命令数量限制
    if len(args.commands) > 5:
        print(json.dumps({
            "status": "error",
            "error": f"单次最多执行 5 条命令，当前提供了 {len(args.commands)} 条。"
        }))
        sys.exit(1)

    username, password = pool_client.resolve_password(args)
    try:
        result = pool_client.exec_cmds(args.port, args.commands, username=username, password=password)
    except pool_client.PoolError as e:
        print(json.dumps({"status": "error", "error": str(e)}))
        sys.exit(1)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
