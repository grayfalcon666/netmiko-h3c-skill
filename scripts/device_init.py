#!/usr/bin/env python3
"""
设备初始化脚本：连接设备、关闭分屏、获取版本信息。
用法：
  python3 device_init.py <端口号> [用户名] [密码]
示例：
  # 无认证
  python3 device_init.py 30001
  # 有认证
  python3 device_init.py 30001 admin MyPassword
"""
import sys
import json
from netmiko import ConnectHandler


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "用法: device_init.py <端口号> [用户名] [密码]"}))
        sys.exit(1)

    port = int(sys.argv[1])
    username = sys.argv[2] if len(sys.argv) >= 3 else None
    password = sys.argv[3] if len(sys.argv) >= 4 else None

    device = {
        'host': '192.168.56.1',
        'port': port,
        'global_delay_factor': 2,
        'conn_timeout': 30,
    }

    if username and password:
        device['device_type'] = 'hp_comware_telnet'
        device['username'] = username
        device['password'] = password
    else:
        device['device_type'] = 'generic_telnet'

    try:
        conn = ConnectHandler(**device)
        # 强制回到用户视图，清除残留会话
        conn.send_command_timing('return', read_timeout=15)
        conn.send_command('screen-length disable', read_timeout=15)
        version_output = conn.send_command('dis version', read_timeout=30)
        # 确保退出前回到用户视图
        conn.send_command_timing('return', read_timeout=15)
        print(json.dumps({"status": "success", "output": version_output}))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)


if __name__ == '__main__':
    main()
