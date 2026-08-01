#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["netmiko", "fastapi", "uvicorn"]
# ///
"""
纯函数单测（无需真实设备）：
  - parse_view        视图提示符解析
  - has_error         命令错误检测
  - sanitize          密码脱敏
  - ExecRequest       命令数量上限校验
  - update_nav_path   nav_path 跟踪分类
  - reconcile_nav_path  nav_path 对账（end_view 为 ground truth）
  - 历史消息           追加/读取/截断/不含密码
  - 描述符持久化       save/load 往返、损坏容错、不含密码

运行：
  uv run server/test_pool_utils.py
"""

import json
import os
import tempfile
import time
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
    def test_unrecognized_command(self):
        self.assertTrue(server.has_error("% Unrecognized command found at '^' position."))

    def test_incomplete_command(self):
        self.assertTrue(server.has_error("% Incomplete command found at '^' position."))

    def test_ambiguous_command(self):
        self.assertTrue(server.has_error("% Ambiguous command found at '^' position."))

    def test_wrong_parameter(self):
        self.assertTrue(server.has_error("% Wrong parameter found at '^' position."))

    def test_too_many_parameters(self):
        self.assertTrue(server.has_error("Too many parameters"))

    def test_invalid(self):
        self.assertTrue(server.has_error("Invalid input detected"))

    def test_caret_locator_line(self):
        self.assertTrue(server.has_error("  ^\n  % Wrong parameter found"))

    def test_unknown_command_not_matched(self):
        # Cisco 风格措辞不在表内（H3C 用 Unrecognized），按设计不判错
        self.assertFalse(server.has_error("% Unknown command at '^' position."))

    def test_plain_output_ok(self):
        self.assertFalse(server.has_error("<H3C>\nsysname test\n[H3C]"))

    def test_empty_ok(self):
        self.assertFalse(server.has_error(""))


class TestAuth(unittest.TestCase):
    SECRET = "s3cret-key"

    @staticmethod
    def _token(exp_delta=300, iat_delta=0, secret=None):
        claims = {"iss": "netmiko-h3c-client",
                  "iat": int(time.time()) + iat_delta,
                  "exp": int(time.time()) + exp_delta}
        return server.sign_jwt(claims, secret or TestAuth.SECRET)

    def test_no_secret_open_mode(self):
        old = server.POOL_SECRET
        server.POOL_SECRET = ""
        try:
            self.assertTrue(server.token_valid(""))
            self.assertTrue(server.token_valid("not-a-jwt"))
        finally:
            server.POOL_SECRET = old

    def test_valid_jwt_accepted(self):
        old = server.POOL_SECRET
        server.POOL_SECRET = self.SECRET
        try:
            self.assertTrue(server.token_valid(self._token()))
        finally:
            server.POOL_SECRET = old

    def test_expired_jwt_rejected(self):
        old = server.POOL_SECRET
        server.POOL_SECRET = self.SECRET
        try:
            self.assertFalse(server.token_valid(self._token(exp_delta=-600)))
        finally:
            server.POOL_SECRET = old

    def test_wrong_secret_rejected(self):
        old = server.POOL_SECRET
        server.POOL_SECRET = self.SECRET
        try:
            self.assertFalse(server.token_valid(self._token(secret="other-secret")))
        finally:
            server.POOL_SECRET = old

    def test_tampered_payload_rejected(self):
        old = server.POOL_SECRET
        server.POOL_SECRET = self.SECRET
        try:
            tok = self._token()
            seg1, _, sig = tok.split(".")
            bad_claims = {"iss": "netmiko-h3c-client",
                          "iat": int(time.time()) - 3600,
                          "exp": int(time.time()) - 3600}
            bad_seg2 = server._b64url_encode(json.dumps(bad_claims, separators=(",", ":")).encode("utf-8"))
            self.assertFalse(server.token_valid(f"{seg1}.{bad_seg2}.{sig}"))
        finally:
            server.POOL_SECRET = old

    def test_malformed_rejected(self):
        old = server.POOL_SECRET
        server.POOL_SECRET = self.SECRET
        try:
            self.assertFalse(server.token_valid("not-a-jwt"))
            self.assertFalse(server.token_valid("a.b"))
            self.assertFalse(server.token_valid(""))
        finally:
            server.POOL_SECRET = old


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
        # Pydantic v2 的 ValidationError 继承自 ValueError
        with self.assertRaises(ValueError):
            server.ExecRequest(port=30001, commands=["a"] * 6)


class TestNavPath(unittest.TestCase):
    def test_return_clears(self):
        self.assertEqual(
            server.update_nav_path(["system-view", "interface GigabitEthernet1/0/1"], "return"),
            [])

    def test_quit_pops(self):
        self.assertEqual(
            server.update_nav_path(["system-view", "interface GigabitEthernet1/0/1"], "quit"),
            ["system-view"])

    def test_system_view_seeds(self):
        self.assertEqual(server.update_nav_path([], "system-view"), ["system-view"])

    def test_system_view_noop_in_subview(self):
        self.assertEqual(
            server.update_nav_path(["system-view", "vlan 100"], "system-view"),
            ["system-view", "vlan 100"])

    def test_interface_appends(self):
        self.assertEqual(
            server.update_nav_path(["system-view"], "interface GigabitEthernet1/0/1"),
            ["system-view", "interface GigabitEthernet1/0/1"])

    def test_vlan_appends(self):
        self.assertEqual(
            server.update_nav_path(["system-view"], "vlan 100"),
            ["system-view", "vlan 100"])

    def test_data_command_ignored(self):
        self.assertEqual(server.update_nav_path(["system-view"], "display version"),
                         ["system-view"])
        self.assertEqual(server.update_nav_path(["system-view"], "sysname foo"),
                         ["system-view"])


class TestReconcileNavPath(unittest.TestCase):
    def test_user_view_clears(self):
        self.assertEqual(
            server.reconcile_nav_path(["system-view"], {"view": "user", "path": ""}), [])

    def test_system_view(self):
        self.assertEqual(
            server.reconcile_nav_path([], {"view": "system", "path": ""}), ["system-view"])

    def test_subview_trace_kept(self):
        nav = ["system-view", "interface GigabitEthernet1/0/1"]
        v = {"view": "subview", "path": "GigabitEthernet1/0/1"}
        self.assertEqual(server.reconcile_nav_path(nav, v), nav)

    def test_subview_vlan_rebuilt(self):
        v = {"view": "subview", "path": "vlan100"}
        self.assertEqual(server.reconcile_nav_path([], v), ["system-view", "vlan 100"])

    def test_subview_interface_rebuilt(self):
        v = {"view": "subview", "path": "GigabitEthernet1/0/1"}
        self.assertEqual(server.reconcile_nav_path([], v),
                         ["system-view", "interface GigabitEthernet1/0/1"])

    def test_subview_vlan_interface_rebuilt(self):
        v = {"view": "subview", "path": "Vlan-interface100"}
        self.assertEqual(server.reconcile_nav_path([], v),
                         ["system-view", "interface Vlan-interface100"])

    def test_none_view_unchanged(self):
        self.assertEqual(server.reconcile_nav_path(["system-view"], None), ["system-view"])


class _FakeConn:
    """替代 netmiko 连接的假对象：可返回提示符/乱码/抛异常。"""

    def __init__(self, output="", raises=False):
        self.output = output
        self.raises = raises

    def send_command_timing(self, cmd, read_timeout=None):
        if self.raises:
            raise OSError("connection dead")
        return self.output


class TestProbeAlive(unittest.TestCase):
    def _probe(self, fake_conn):
        s = server.Session(30010)
        s.conn = fake_conn
        return server.probe_alive(s, timeout=1.0)

    def test_alive_system_prompt(self):
        self.assertTrue(self._probe(_FakeConn(output="\r\n[H3C]\r\n")))

    def test_alive_user_prompt(self):
        self.assertTrue(self._probe(_FakeConn(output="<H3C>")))

    def test_alive_subview_prompt(self):
        self.assertTrue(self._probe(_FakeConn(output="[H3C-vlan100]")))

    def test_garbage_no_prompt(self):
        self.assertFalse(self._probe(_FakeConn(output="some noise")))

    def test_empty_output(self):
        self.assertFalse(self._probe(_FakeConn(output="")))

    def test_raises_is_dead(self):
        self.assertFalse(self._probe(_FakeConn(output="", raises=True)))

    def test_no_conn_is_dead(self):
        self.assertFalse(server.probe_alive(server.Session(30011), timeout=1.0))


class _TempDataMixin:
    """把 DATA_DIR / SESSION_FILE 指向临时目录，测完恢复。"""

    def setUp(self):
        self._orig_data_dir = server.DATA_DIR
        self._orig_session_file = server.SESSION_FILE
        self._tmp = tempfile.TemporaryDirectory()
        server.DATA_DIR = self._tmp.name
        server.SESSION_FILE = os.path.join(self._tmp.name, "pool_sessions.json")

    def tearDown(self):
        server.DATA_DIR = self._orig_data_dir
        server.SESSION_FILE = self._orig_session_file
        self._tmp.cleanup()


class TestHistory(_TempDataMixin, unittest.TestCase):
    def test_append_and_read(self):
        session = server.Session(30001)
        entry = server._history_entry(
            session, "exec", ["system-view"], ["[H3C]"], "success",
            {"view": "user", "path": ""}, {"view": "system", "path": ""})
        server.append_history(30001, entry)
        got = server.read_history(30001)
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["op"], "exec")
        self.assertEqual(got[0]["commands"], ["system-view"])
        self.assertEqual(got[0]["end_view"]["view"], "system")

    def test_read_missing_returns_empty(self):
        self.assertEqual(server.read_history(39999), [])

    def test_trim_history(self):
        session = server.Session(30002)
        old = server.HISTORY_MAX
        server.HISTORY_MAX = 3
        try:
            for i in range(5):
                entry = server._history_entry(
                    session, "exec", [f"cmd{i}"], [str(i)], "success", None, None)
                server.append_history(30002, entry)
            got = server.read_history(30002, limit=100)
            self.assertEqual(len(got), 3)
            self.assertEqual(got[0]["commands"], ["cmd2"])
        finally:
            server.HISTORY_MAX = old

    def test_entry_never_contains_password(self):
        session = server.Session(30003, username="admin", password="S3cretPw!")
        entry = server._history_entry(
            session, "exec", ["display version"], ["<H3C>"], "success", None, None)
        blob = json.dumps(entry, ensure_ascii=False)
        self.assertNotIn("S3cretPw!", blob)
        self.assertNotIn("password", blob.lower())


class TestDescriptorPersistence(_TempDataMixin, unittest.TestCase):
    def test_save_load_roundtrip(self):
        pool = server.ConnectionPool()
        pool._descriptors = {30001: {"username": "", "nav_path": ["system-view", "interface Gi1/0/1"]}}
        pool.save_state()
        pool2 = server.ConnectionPool()
        pool2.load_state()
        self.assertEqual(pool2._descriptors[30001]["nav_path"],
                         ["system-view", "interface Gi1/0/1"])
        self.assertEqual(pool2._descriptors[30001]["username"], "")

    def test_corrupt_file_rebuilds_empty(self):
        os.makedirs(server.DATA_DIR, exist_ok=True)
        with open(server.SESSION_FILE, "w", encoding="utf-8") as f:
            f.write("{ not valid json")
        pool = server.ConnectionPool()
        pool.load_state()
        self.assertEqual(pool._descriptors, {})

    def test_missing_file_rebuilds_empty(self):
        pool = server.ConnectionPool()
        pool.load_state()
        self.assertEqual(pool._descriptors, {})

    def test_save_state_never_writes_password(self):
        pool = server.ConnectionPool()
        pool._descriptors = {30001: {"username": "admin", "nav_path": ["system-view"]}}
        pool.save_state()
        with open(server.SESSION_FILE, encoding="utf-8") as f:
            blob = f.read()
        self.assertNotIn("password", blob.lower())
        self.assertNotIn("secret", blob.lower())

    def test_remove_descriptor(self):
        pool = server.ConnectionPool()
        pool._descriptors = {30001: {"username": "", "nav_path": ["system-view"]}}
        pool.remove_descriptor(30001)
        self.assertEqual(pool._descriptors, {})
        pool2 = server.ConnectionPool()
        pool2.load_state()
        self.assertEqual(pool2._descriptors, {})

    def test_seed_from_descriptor(self):
        pool = server.ConnectionPool()
        pool._descriptors = {30001: {"username": "", "nav_path": ["system-view"]}}
        session = pool._seed_from_descriptor(server.Session(30001))
        self.assertEqual(session.nav_path, ["system-view"])
        s2 = pool._seed_from_descriptor(server.Session(30002))
        self.assertEqual(s2.nav_path, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
