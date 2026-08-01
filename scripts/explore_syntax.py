#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
H3C 命令语法探索器（连接池客户端版）

作为 server/connection_pool_server.py 的 HTTP 客户端。对不完整命令逐级使用 ? 查询、
返回选项链的逻辑已迁移到服务端 /explore 端点，本脚本只负责传参并打印结果。

用法：
  无认证：python3 explore_syntax.py <端口> "<前置子视图命令1>" ... "<待探索的不完整命令>"
  有认证：python3 explore_syntax.py <端口> ... --user <用户名> [--password-env <环境变量名>]
"""

import sys
import json
import argparse

import pool_client


def main() -> None:
    parser = argparse.ArgumentParser(description="H3C 命令语法探索器（连接池客户端）")
    parser.add_argument("port", type=int, help="设备 Telnet 端口")
    parser.add_argument("commands", nargs="+",
                        help="前置视图命令（可选），最后一条为待探索的不完整命令")
    pool_client.add_auth_args(parser)
    args = parser.parse_args()

    if len(args.commands) < 1:
        print(json.dumps({"status": "error", "error": "至少需要一条待探索的命令前缀"}))
        sys.exit(1)

    *pre_cmds, base_cmd = args.commands
    username, password = pool_client.resolve_password(args)
    try:
        result = pool_client.explore(args.port, pre_cmds, base_cmd, username=username, password=password)
    except pool_client.PoolError as e:
        print(json.dumps({"status": "error", "error": str(e)}))
        sys.exit(1)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
