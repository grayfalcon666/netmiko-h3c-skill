#!/usr/bin/env python3
"""
mock_h3c_device.py – 假 H3C 设备 Telnet 服务器（无真实设备时的端到端验证）

模拟 H3C Comware 提示符状态机：
  <H3C>                   用户视图
  [H3C]                   系统视图
  [H3C-<子视图>]           子视图（interface / vlan 等）

支持命令：
  system-view / quit / return / interface <X> / vlan <N> / sysname <N>
  dis version / dis <任意> / screen-length disable / terminal length 0
  <cmd> ?                 帮助查询（缩进的选项行，供 /explore 语法探索）
  空行（\\r\\n）            重发当前提示符（供 netmiko find_prompt 探测）
  其他                     % Unknown command at '^' position.

默认关闭认证（generic_telnet 流程）；--require-auth 时先提示
Username:/Password:（hp_comware_telnet 流程）。

用法：
  python3 server/mock_h3c_device.py --port 2323
  python3 server/mock_h3c_device.py --port 2324 --require-auth --hostname SW-1
"""

import re
import sys
import argparse
import socketserver

# 帮助选项表：命令前缀 -> 下一级选项（<x> 表示参数占位）
HELP_TABLE = {
    "dis": ["acl", "arp", "clock", "current-configuration", "interface"],
    "dis interface": ["GigabitEthernet"],
    "dis interface GigabitEthernet": [],
    "interface": ["<interface-name>"],
    "snmp-agent": ["<name>"],
    "system-view": [],
}


class H3CDeviceHandler(socketserver.StreamRequestHandler):
    """每个客户端连接一个线程；实现简单 prompt 状态机。"""

    def setup(self):
        super().setup()
        self.hostname = self.server.hostname
        self.mode = "user"            # user / system / subview
        self.subview = ""             # 子视图路径
        self._buffer = ""             # 字节缓冲（跨 recv 累积）
        self._auth_stage = "username" if self.server.require_auth else "ready"

    # ------------------------------------------------------------------ I/O
    def handle(self):
        try:
            if self.server.require_auth:
                self.send("Username:")
            while True:
                data = self.connection.recv(4096)
                if not data:
                    break
                for line in self._iter_lines(data):
                    self._handle_line(line)
        except (ConnectionResetError, BrokenPipeError, OSError):
            pass
        finally:
            try:
                self.connection.close()
            except OSError:
                pass

    def send(self, text: str) -> None:
        """发送一行文本（telnet 用 \\r\\n 结尾）。"""
        self.connection.sendall(text.encode("utf-8") + b"\r\n")

    def _strip_iac(self, data: bytes) -> str:
        """剥掉 telnet IAC 序列（netmiko is_alive() 会发 IAC NOP）。"""
        out = bytearray()
        i, n = 0, len(data)
        while i < n:
            b = data[i]
            if b == 0xFF:                     # IAC
                if i + 1 >= n:
                    break                     # 截断，丢弃即可
                cmd = data[i + 1]
                if cmd in (0xFB, 0xFC, 0xFD, 0xFE):  # WILL/WONT/DO/DONT + option
                    i += 3
                else:                          # NOP/SE/SB 等，仅 1 字节参数
                    i += 2
                continue
            out.append(b)
            i += 1
        return bytes(out).decode("utf-8", errors="replace")

    def _iter_lines(self, data: bytes):
        """把新数据拼进缓冲，按 \\r\\n|\\r|\\n 切出完整行，返回行列表。"""
        self._buffer += self._strip_iac(data)
        lines = []
        buf = self._buffer
        while buf:
            m = re.search(r"\r\n|\r|\n", buf)
            if not m:
                break
            line = buf[: m.start()]
            rest = buf[m.end():]
            if m.group(0) == "\r" and rest.startswith("\n"):  # 处理 \r\n 拆包
                rest = rest[1:]
            lines.append(line)
            buf = rest
        self._buffer = buf
        return lines

    # ------------------------------------------------------------- 状态机
    def _handle_line(self, line: str):
        line = line.strip()
        if self._auth_stage == "username":
            self.username = line
            self._auth_stage = "password"
            self.send("Password:")
            return
        if self._auth_stage == "password":
            self.password = line
            self._auth_stage = "ready"
            self._send_banner()
            self.send(self._prompt())
            return
        if not line:                          # 空行 -> 重发提示符（find_prompt）
            self.send(self._prompt())
            return
        self._dispatch(line)

    def _prompt(self) -> str:
        if self.mode == "user":
            return f"<{self.hostname}>"
        if self.mode == "system":
            return f"[{self.hostname}]"
        return f"[{self.hostname}-{self.subview}]"

    def _send_banner(self):
        self.send("* Copyright (c) 2004-2024 New H3C Technologies Co., Ltd. All rights reserved.*")
        self.send("* Without the owner's prior written consent, no decompiling or reverse-engineering shall be allowed.*")

    # ------------------------------------------------------------- 命令分发
    def _dispatch(self, cmd: str):
        # H3C 命令回显
        self.send(cmd)
        # display 是 dis 的全称
        if cmd.startswith("display "):
            cmd = "dis" + cmd[len("display"):]

        # 帮助查询
        if cmd.rstrip().endswith("?"):
            self._handle_help(cmd.rstrip())
            return

        # 视图切换
        if cmd == "system-view":
            if self.mode == "user":
                self.mode = "system"
        elif cmd == "quit":
            if self.mode == "subview":
                self.mode = "system"
            elif self.mode == "system":
                self.mode = "user"
        elif cmd == "return":
            self.mode, self.subview = "user", ""
        elif cmd.startswith("interface ") and self.mode == "system":
            self.mode, self.subview = "subview", cmd.split(None, 1)[1]
        elif cmd.startswith("vlan ") and self.mode == "system":
            parts = cmd.split()
            if len(parts) >= 2 and parts[1].isdigit():
                self.mode, self.subview = "subview", f"vlan{parts[1]}"
        elif cmd.startswith("sysname ") and self.mode == "system":
            newname = cmd.split(None, 1)[1].strip()
            if newname:
                self.hostname = newname
        elif cmd == "dis version":
            self._send_version()
        elif cmd in ("screen-length disable", "terminal length 0"):
            pass                              # 关闭分屏：无输出
        elif cmd.startswith("dis "):
            pass                              # 通用 display：模拟空结果
        else:
            self.send("% Unknown command at '^' position.")
        self.send(self._prompt())

    def _send_version(self):
        self.send("H3C Comware Software, Version 7.1.070, Release 1234")
        self.send("Copyright (c) 2004-2024 New H3C Technologies Co., Ltd. All rights reserved.")
        self.send("H3C S6520X-30QC-EI uptime is 1 week, 2 days, 3 hours, 4 minutes")

    def _handle_help(self, query: str):
        base = query[:-1].strip()             # 去掉末尾 '?'
        options = HELP_TABLE.get(base)
        if options is None:
            self.send("% Unrecognized command found at '^' position.")
        elif options:
            for opt in options:
                self.send(f"  {opt}")
        else:
            self.send("  <cr>")
        self.send(self._prompt())


class MockH3CServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, server_address, require_auth: bool = False, hostname: str = "H3C"):
        self.require_auth = require_auth
        self.hostname = hostname
        super().__init__(server_address, H3CDeviceHandler)


def main() -> None:
    parser = argparse.ArgumentParser(description="假 H3C 设备 Telnet 服务器")
    parser.add_argument("--port", type=int, default=2323, help="监听端口（默认 2323）")
    parser.add_argument("--hostname", default="H3C", help="设备主机名（默认 H3C）")
    parser.add_argument("--require-auth", action="store_true", help="启用 Username/Password 认证流程")
    args = parser.parse_args()

    with MockH3CServer(("127.0.0.1", args.port),
                       require_auth=args.require_auth,
                       hostname=args.hostname) as server:
        print(f"mock H3C device listening on 127.0.0.1:{args.port}"
              f" (auth={'on' if args.require_auth else 'off'})", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nstopped", flush=True)


if __name__ == "__main__":
    main()
