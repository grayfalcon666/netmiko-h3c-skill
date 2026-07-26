#!/usr/bin/env python3
"""
apply_config.py – 通过 Telnet 对 H3C 设备执行配置命令（最多 5 条）
符合 Skill 安全规范：固定初始化框架、错误检测、密码保护、单设备操作。
已修正：统一使用 send_command_timing，兼容任意嵌套深度的子视图提示符。
"""

import sys
import json
import argparse
import getpass
import os
import re

try:
    from netmiko import ConnectHandler
except ImportError:
    sys.stderr.write("错误：未安装 netmiko，请执行 pip install netmiko\n")
    sys.exit(1)

# 设备固定 IP
DEVICE_IP = "192.168.56.1"

def has_error(output: str) -> bool:
    """
    检查命令输出是否包含错误关键字。
    忽略特定上下文中允许的 '% Unrecognized command'（通常由 return 在用户视图引起）。
    """
    # 移除 '% Unrecognized command' 行后再检查
    cleaned = re.sub(r'^\s*% Unrecognized command.*\n?', '', output, flags=re.MULTILINE).strip()
    if not cleaned:
        return False
    # 常见错误关键字
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

def apply_config(port: int, commands: list, username: str = None, password: str = None):
    """
    核心执行函数。
    port: Telnet 端口
    commands: 配置命令列表（不含 return、screen-length disable、system-view）
    username, password: 认证信息，None 则使用无认证模式
    """
    # 连接参数
    if username and password is not None:
        device_type = "hp_comware_telnet"
    else:
        device_type = "generic_telnet"
        username = ""
        password = ""

    device = {
        "device_type": device_type,
        "ip": DEVICE_IP,
        "port": port,
        "username": username,
        "password": password,
        "global_delay_factor": 1,
        "conn_timeout": 10,
    }

    conn = None
    all_output = []
    try:
        # 建立连接
        conn = ConnectHandler(**device)

        # ---- 固定框架（全部使用 send_command_timing，兼容任意提示符） ----
        # 1. 返回用户视图（忽略 Unrecognized command）
        out = conn.send_command_timing("return", read_timeout=5)
        all_output.append(out)

        # 2. 关闭分屏
        out = conn.send_command_timing("screen-length disable", read_timeout=5)
        all_output.append(out)
        if has_error(out):
            raise RuntimeError("关闭分屏失败: " + out)

        # 3. 进入系统视图
        out = conn.send_command_timing("system-view", read_timeout=5)
        all_output.append(out)
        if has_error(out):
            raise RuntimeError("进入系统视图失败: " + out)

        # ---- 执行用户配置命令（统一 send_command_timing） ----
        for cmd in commands:
            cmd = cmd.strip()
            if not cmd:
                continue
            out = conn.send_command_timing(cmd, read_timeout=5)
            all_output.append(out)
            if has_error(out):
                raise RuntimeError(f"命令 '{cmd}' 执行失败: {out}")

        # ---- 固定框架结束 ----
        # 返回用户视图
        out = conn.send_command_timing("return", read_timeout=5)
        all_output.append(out)
        # 此处的 Unrecognized command 忽略，不视为错误

        return {
            "status": "success",
            "output": "\n".join(all_output)
        }

    except Exception as e:
        return {
            "status": "error",
            "output": "\n".join(all_output) if all_output else "",
            "error": str(e)
        }
    finally:
        if conn:
            conn.disconnect()

def main():
    parser = argparse.ArgumentParser(
        description="通过 Telnet 对 H3C 设备执行配置命令（最多 5 条）"
    )
    parser.add_argument("port", type=int, help="Telnet 端口号")
    parser.add_argument("commands", nargs="+", help="要执行的配置命令（最多 5 条），用空格分隔并加引号")
    parser.add_argument("--user", help="登录用户名（若提供则启用认证模式）")
    parser.add_argument("--password", help="登录密码（不安全，建议用 --password-env 或交互输入）")
    parser.add_argument("--password-env", help="从环境变量读取密码，指定变量名")

    args = parser.parse_args()

    # 命令数量限制
    if len(args.commands) > 5:
        print(json.dumps({
            "status": "error",
            "error": f"单次最多执行 5 条命令，当前提供了 {len(args.commands)} 条。"
        }))
        sys.exit(1)

    # 密码处理
    password = None
    if args.user:
        # 认证模式
        if args.password_env:
            password = os.environ.get(args.password_env)
            if password is None:
                print(json.dumps({
                    "status": "error",
                    "error": f"环境变量 {args.password_env} 未设置。"
                }))
                sys.exit(1)
        elif args.password:
            password = args.password
            # 警告：密码出现在命令行中
            sys.stderr.write("警告：密码通过命令行传递不安全，建议使用 --password-env 或交互式输入。\n")
        else:
            password = getpass.getpass("请输入设备密码: ")
    else:
        # 无认证模式，用户名密码留空
        pass

    result = apply_config(args.port, args.commands, args.user, password)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
