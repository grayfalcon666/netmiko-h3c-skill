#!/usr/bin/env python3
"""
H3C 命令语法探索器（修复版 v2）
- 支持在设备上对不完整命令逐级使用 ? 查询，返回选项链。
- 自动处理可选参数后的子命令（使用虚拟值探测）。
- 仅执行只读查询，不修改配置。
- 设备类型根据认证状态自动选择 Telnet 类型。
- 修复：只提取缩进行作为帮助选项，彻底排除命令回显和提示符干扰。
"""

import sys
import json
import argparse
import re
from netmiko import ConnectHandler
from getpass import getpass


def parse_help_output(output: str) -> list:
    """
    解析 ? 命令的输出，提取有效选项关键字。
    只处理以至少两个空格缩进的行（Comware 帮助选项的铁律）。
    忽略空行、分隔线、错误信息、错误定位符。
    返回去重后的选项列表。
    """
    ignore_pattern = re.compile(
        r'^\s*(%|Error|----|<cr>|\^|$)'  # 错误、分隔线、回车、定位符、空行
    )
    options = []
    for line in output.splitlines():
        line_stripped = line.strip()
        # 只处理以至少两个空格开头的行（Comware 帮助选项的固定格式）
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
    # 去重保序
    seen = set()
    unique = []
    for o in options:
        if o not in seen:
            seen.add(o)
            unique.append(o)
    return unique


def is_parameter_type(opt: str) -> bool:
    """判断选项是否为参数类型（以 < 开头）"""
    return opt.startswith('<')


def extract_help_lines(raw_output: str) -> str:
    """
    从设备原始输出中提取帮助信息行。
    只保留以至少两个空格缩进、且不以 '[' 开头的行。
    """
    lines = []
    for line in raw_output.splitlines():
        if line.startswith('  ') and not line.strip().startswith('['):
            lines.append(line)
    return "\n".join(lines)


def explore_syntax(conn, base_cmd: str):
    """
    逐级探索命令语法，返回 (成功标志, chain列表, 信息字符串)。
    chain: [{"prefix": str, "options": list, "type": "keyword"|"parameter"}, ...]
    """
    chain = []
    current_prefix = base_cmd.strip()
    max_depth = 10  # 安全限制，防止意外循环

    for _ in range(max_depth):
        raw_output = conn.send_command_timing(
            f"{current_prefix} ?", strip_prompt=False, strip_command=False
        )

        # ---- 提取帮助信息（只保留缩进行） ----
        output = extract_help_lines(raw_output)

        # ---- 检查致命错误（在原始输出中检查） ----
        if re.search(
            r'% Unknown command|% Unrecognized command|Error', raw_output, re.IGNORECASE
        ):
            return True, chain, f"探索停止于 '{current_prefix}'，设备返回错误"

        options = parse_help_output(output)
        if not options:
            return True, chain, f"'{current_prefix}' 没有更多可用选项。"

        # 如果只有唯一选项
        if len(options) == 1:
            opt = options[0]
            # 如果是参数类型，需要探测后面是否还能继续
            if is_parameter_type(opt):
                # 用虚拟值 1 代替参数，发 ? 探测
                probe_raw = conn.send_command_timing(
                    f"{current_prefix} 1 ?", strip_prompt=False, strip_command=False
                )
                probe_output = extract_help_lines(probe_raw)
                if re.search(
                    r'% Unknown command|% Unrecognized command|Error',
                    probe_raw, re.IGNORECASE
                ):
                    # 参数后无更多命令，停止，且不记录该参数层级（它是终点）
                    return True, chain, f"'{current_prefix}' 后参数为终点，停止探索。"
                elif not parse_help_output(probe_output):
                    # 参数后无有效选项，停止
                    return True, chain, f"'{current_prefix}' 后参数为终点，停止探索。"
                else:
                    chain.append({
                        "prefix": current_prefix,
                        "options": [opt],
                        "type": "parameter"
                    })
                    current_prefix = f"{current_prefix} 1"
                    continue
            else:
                # 唯一选项是非参数关键字，直接追加继续
                chain.append({
                    "prefix": current_prefix,
                    "options": [opt],
                    "type": "keyword"
                })
                current_prefix = f"{current_prefix} {opt}"
                continue
        else:
            # 多个选项，停止自动探索
            chain.append({
                "prefix": current_prefix,
                "options": options,
                "type": "multiple"
            })
            break

    return True, chain, ""


def main():
    parser = argparse.ArgumentParser(description="H3C命令语法探索器（修复版 v2）")
    parser.add_argument("port", type=int, help="设备 Telnet 端口")
    parser.add_argument("commands", nargs='+',
                        help="前置视图命令（可选），最后一条为待探索的不完整命令")
    parser.add_argument("--user", help="登录用户名")
    parser.add_argument("--password-env", help="密码所在环境变量名")
    args = parser.parse_args()

    if len(args.commands) < 1:
        print(json.dumps({"status": "error", "error": "至少需要一条待探索的命令前缀"}))
        sys.exit(1)

    *pre_cmds, base_cmd = args.commands

    # 处理密码
    password = None
    if args.user:
        if args.password_env:
            import os
            password = os.environ.get(args.password_env)
            if not password:
                print(json.dumps({"status": "error", "error": f"环境变量 {args.password_env} 未设置"}))
                sys.exit(1)
        else:
            password = getpass(f"请输入 {args.user} 的密码: ")

    # ---- 动态选择设备类型（与 apply_config.py 保持一致） ----
    if args.user and password is not None:
        device_type = "hp_comware_telnet"
    else:
        device_type = "generic_telnet"
        if not args.user:
            args.user = ""
            password = ""

    device = {
        'device_type': device_type,
        'host': '192.168.56.1',
        'port': args.port,
        'username': args.user if args.user else '',
        'password': password if password else '',
        'fast_cli': False,
        'global_delay_factor': 1,
    }

    try:
        conn = ConnectHandler(**device)
        conn.send_command_timing("return", strip_prompt=False, strip_command=False)
        conn.send_command_timing("screen-length disable", strip_prompt=False, strip_command=False)
        conn.send_command_timing("system-view", strip_prompt=False, strip_command=False)

        # 执行前置命令（进入子视图）
        for cmd in pre_cmds:
            out = conn.send_command_timing(cmd, strip_prompt=False, strip_command=False)
            if re.search(r'Error|Unknown command|Unrecognized command', out, re.IGNORECASE):
                conn.disconnect()
                print(json.dumps({
                    "status": "error",
                    "error": f"前置命令 '{cmd}' 执行失败: {out.strip()}"
                }))
                sys.exit(1)

        success, chain, info = explore_syntax(conn, base_cmd)

        conn.send_command_timing("return", strip_prompt=False, strip_command=False)
        conn.disconnect()

        if not success:
            print(json.dumps({"status": "error", "error": info, "chain": chain}))
        else:
            print(json.dumps({
                "status": "success",
                "chain": chain,
                "info": info if info else "探索完成"
            }))
    except Exception as e:
        print(json.dumps({"status": "error", "error": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()