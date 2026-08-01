#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["netmiko", "fastapi", "uvicorn"]
# ///
"""
纯函数单测（无需真实设备）：
  - parse_view  视图提示符解析
  - has_error   命令错误检测
  - sanitize    密码脱敏
  - ExecRequest 命令数量上限校验

运行：
  uv run server/test_pool_utils.py
"""

import unittest

import connection_pool_server as server


class TestParseView(unittest.TestCase):
    def test_user_view(self):
        v = server.parse_view("<H3C>")
        self.assertEqual(v["view"], "user")
        self.assertEqual(v["hostname"], "H3C")
        self.assertEqual(v["path"], "")

    def test_system_view(self):
        v = server.parse_view("[H3C]")
        self.assertEqual(v["view"], "system")
        self.assertEqual(v["hostname"], "H3C")
        self.assertEqual(v["path"], "")

    def test_interface_subview(self):
        v = server.parse_view("[H3C-GigabitEthernet1/0/1]")
        self.assertEqual(v["view"], "subview")
        self.assertEqual(v["hostname"], "H3C")
        self.assertEqual(v["path"], "GigabitEthernet1/0/1")

    def test_vlan_subview(self):
        v = server.parse_view("[H3C-vlan100]")
        self.assertEqual(v["view"], "subview")
        self.assertEqual(v["path"], "vlan100")

    def test_hostname_with_dash_is_system_view(self):
        # 主机名含 '-' 时不能误判为子视图（SW-1 / SW-Core-01 均为系统视图）
        v = server.parse_view("[SW-1]")
        self.assertEqual(v["view"], "system")
        self.assertEqual(v["hostname"], "SW")
        v = server.parse_view("[SW-Core-01]")
        self.assertEqual(v["view"], "system")

    def test_vlan_interface_subview_with_dash(self):
        # 子视图名本身可含 '-'（如 Vlan-interface100），仍应判为子视图
        v = server.parse_view("[H3C-Vlan-interface100]")
        self.assertEqual(v["view"], "subview")
        self.assertEqual(v["path"], "Vlan-interface100")

    def test_garbage(self):
        with self.assertRaises(ValueError):
            server.parse_view("foo")
        with self.assertRaises(ValueError):
            server.parse_view("")


class TestHasError(unittest.TestCase):
    def test_unknown_command(self):
        self.assertTrue(server.has_error("% Unknown command at '^' position."))

    def test_error_caret(self):
        self.assertTrue(server.has_error("  ^\n  % Wrong parameter found"))

    def test_incomplete(self):
        self.assertTrue(server.has_error("Incomplete command found at '^' position."))

    def test_invalid(self):
        self.assertTrue(server.has_error("Invalid input detected"))

    def test_unrecognized_ignored(self):
        self.assertFalse(server.has_error("% Unrecognized command found at '^' position."))

    def test_plain_output_ok(self):
        self.assertFalse(server.has_error("<H3C>\nsysname test\n[H3C]"))


class TestSanitize(unittest.TestCase):
    def test_password_removed(self):
        text = "auth failed for admin password=MySecretToken"
        out = server.sanitize(text, ["MySecretToken"])
        self.assertNotIn("MySecretToken", out)
        self.assertIn("***", out)

    def test_no_secret_unchanged(self):
        text = "hello world"
        self.assertEqual(server.sanitize(text, ["s3cr3t"]), text)


class TestExecRequestLimit(unittest.TestCase):
    def test_max_five_ok(self):
        req = server.ExecRequest(port=30001, commands=["a", "b", "c", "d", "e"])
        self.assertEqual(len(req.commands), 5)

    def test_six_rejected(self):
        with self.assertRaises(Exception):
            server.ExecRequest(port=30001, commands=["a"] * 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
