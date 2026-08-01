#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
设备初始化脚本：通过连接池服务连接设备并获取版本信息。

用法：
  无认证：python3 device_init.py <端口号>
  有认证：python3 device_init.py <端口号> --user <用户名>
           （密码交互输入，或用 --password-env <环境变量名>）

注意：会话保持池化，版本查验后不会断开，可继续下发配置。
"""

import argparse
import json
import sys

import pool_client


def main() -> None:
    parser = argparse.ArgumentParser(description="连接设备并获取版本信息")
    parser.add_argument("port", type=int, help="Telnet 端口号")
    pool_client.add_auth_args(parser)
    args = parser.parse_args()

    username, password = pool_client.resolve_password(args)
    try:
        result = pool_client.exec_cmds(args.port, ["dis version"], username=username, password=password)
    except pool_client.PoolError as e:
        print(json.dumps({"status": "error", "error": str(e)}))
        sys.exit(1)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
