#!/usr/bin/env python3
"""
search_cmd.py – H3C 命令文档查询脚本（纯标准库，无第三方依赖）

把 `references/CMD-help` 的 CMD-INDEX 语义索引缓存到 `references/.cmd_cache.jsonl`，
Agent 只需传关键词即可拿到精确文档定位（command/view/file/line），无需碰文件系统搜索。

- 缓存增量更新由 .env 开关 `NETMIKO_CMD_DOC_AUTO_REFRESH` 控制（默认 true）：
    - true ：用 `git status --porcelain -- references/CMD-help` 检测变更，有变更才重建；
             非 Git 仓库时回退到「路径+修改时间」哈希与缓存头比对，不一致才重建。
    - false：不做任何变更检查，直接用已有缓存；仅缓存缺失时构建一次。
- 查询：`command` 字段包含关键词（子串匹配，大小写不敏感），返回全部匹配。

CLI：
  python3 scripts/search_cmd.py [--full] [--exact|--prefix|--suffix|--word|--regex] <关键词>
    --full  直接输出匹配命令的完整文档块（默认输出 JSON 定位）
    --exact  命令名与关键词完全相等
    --prefix 命令名以关键词开头
    --suffix 命令名以关键词结尾
    --word   关键词作为完整单词出现（按空格分词，非子串）
    --regex  关键词为正则表达式（忽略大小写）
    匹配模式互斥，默认子串匹配；是否用哪种模式由调用方按需决定
"""

from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

# --------------------------------------------------------------------------
# 路径与环境
# --------------------------------------------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS_DIR = os.path.join(ROOT, "references", "CMD-help")
CACHE_FILE = os.path.join(ROOT, "references", ".cmd_cache.jsonl")

# 开关：是否开启动态检查 references/CMD-help 更新并动态更新索引缓存
_AUTO_REFRESH_RAW = os.environ.get("NETMIKO_CMD_DOC_AUTO_REFRESH", "true").strip().lower()
AUTO_REFRESH = _AUTO_REFRESH_RAW in ("1", "true", "yes", "on")

_INDEX_ROW = re.compile(r"L(\d+)")


def _load_dotenv() -> None:
    """加载仓库根目录 .env（若存在），不覆盖已存在的环境变量。纯标准库实现。"""
    path = os.path.join(ROOT, ".env")
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


_load_dotenv()
# .env 加载完成后重新读取开关（.env 中的值优先于默认值）
_AUTO_REFRESH_RAW = os.environ.get("NETMIKO_CMD_DOC_AUTO_REFRESH", "true").strip().lower()
AUTO_REFRESH = _AUTO_REFRESH_RAW in ("1", "true", "yes", "on")


# --------------------------------------------------------------------------
# 全量构建
# --------------------------------------------------------------------------
def _md_files() -> list[str]:
    """glob 扫描 CMD-help 下所有 .md，返回相对仓库根的路径（不读内容）。"""
    pattern = os.path.join(REFS_DIR, "**", "*.md")
    return sorted(
        os.path.relpath(p, ROOT) for p in glob.glob(pattern, recursive=True)
    )


def _fs_hash() -> str:
    """全部 .md 的「路径 + 修改时间」组合 sha256，用于缓存失效比对。"""
    h = hashlib.sha256()
    for rel in _md_files():
        try:
            st = os.stat(os.path.join(ROOT, rel))
        except OSError:
            continue
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(str(st.st_mtime_ns).encode("utf-8"))
    return h.hexdigest()


def _parse_cmd_index(content: str, rel: str) -> list[dict]:
    """解析一个文件的 CMD-INDEX 块（`命令名 | 视图 | L行号`）。格式不符自动跳过。"""
    entries: list[dict] = []
    in_block = False
    for line in content.splitlines():
        if not in_block:
            if "CMD-INDEX" in line:
                in_block = True
            continue
        if "-->" in line:
            break
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            continue
        m = _INDEX_ROW.search(parts[-1])
        if not m:
            continue
        entries.append({
            "command": parts[0],
            "view": parts[1],
            "file": rel,
            "line": int(m.group(1)),
        })
    return entries


def _build_cache() -> list[dict]:
    """全量扫描 CMD-help 重建缓存，返回全部条目。无索引/解析失败的文件自动跳过。"""
    entries: list[dict] = []
    for rel in _md_files():
        try:
            with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError:
            continue
        entries.extend(_parse_cmd_index(content, rel))

    tmp_fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(CACHE_FILE), suffix=".tmp")
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
            f.write(f"# hash: {_fs_hash()}\n")
            for e in entries:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
        os.replace(tmp_path, CACHE_FILE)
    except OSError:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
    return entries


# --------------------------------------------------------------------------
# 缓存读取与失效判断
# --------------------------------------------------------------------------
def _read_cache_hash() -> str | None:
    try:
        with open(CACHE_FILE, encoding="utf-8") as f:
            first = f.readline().strip()
    except OSError:
        return None
    if first.startswith("# hash: "):
        return first[len("# hash: "):]
    return None


def _load_cache() -> list[dict] | None:
    """读取缓存全部条目；文件缺失或损坏返回 None。"""
    entries: list[dict] = []
    try:
        with open(CACHE_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    entries.append(json.loads(line))
                except (ValueError, TypeError):
                    return None
    except OSError:
        return None
    return entries


def _git_changed() -> bool:
    """git status 检测 references/CMD-help 是否有变更。git 缺失/非 Git 仓库时抛异常由调用方回退。"""
    git_bin = shutil.which("git")
    if not git_bin:
        raise OSError("git not found")
    proc = subprocess.run(  # noqa: S603 - git_bin 来自 shutil.which，参数均为常量
        [git_bin, "status", "--porcelain", "--", "references/CMD-help"],
        cwd=ROOT,
        capture_output=True,
        timeout=10,
        check=False,
        shell=False,
    )
    return bool(proc.stdout.strip())


def _cache_stale() -> bool:
    """缓存是否失效：git status 有变更，或（非 Git 仓库时）哈希不一致。"""
    try:
        return _git_changed()
    except Exception:  # noqa: BLE001 - 非 Git 仓库/工具缺失等一律回退
        return _fs_hash() != _read_cache_hash()


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------
def load_entries() -> list[dict]:
    """按开关逻辑返回最新缓存条目，必要时自动重建。"""
    if not AUTO_REFRESH:
        if not os.path.isfile(CACHE_FILE):
            return _build_cache()
        entries = _load_cache()
        return entries if entries is not None else _build_cache()

    if not os.path.isfile(CACHE_FILE):
        return _build_cache()
    if _cache_stale():
        return _build_cache()
    entries = _load_cache()
    return entries if entries is not None else _build_cache()


def _block_text(entry: dict, all_entries: list[dict]) -> str:
    """返回该命令的完整文档块：从本索引行到同文件下一个索引行之前。

    结束行取同文件所有索引行中大于本行号的最小者；无后续索引则到文件末尾。
    """
    rel = entry["file"]
    line = int(entry.get("line", 0))
    try:
        with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
    except OSError:
        return f"<无法读取文档: {rel}>"

    end = len(lines) + 1
    for e in all_entries:
        el = int(e.get("line", 0))
        if e.get("file") == rel and el > line and el < end:
            end = el
    return "\n".join(lines[line - 1 : end - 1])


_MODES = ("--exact", "--prefix", "--suffix", "--word", "--regex")


def main() -> None:
    full = False
    mode = "substring"  # 默认子串匹配
    rest: list[str] = []
    for a in sys.argv[1:]:
        if a == "--full":
            full = True
        elif a in _MODES:
            if mode != "substring":
                print(json.dumps(
                    {"error": "匹配模式互斥，只能指定一个: " + " | ".join(_MODES)},
                    ensure_ascii=False))
                sys.exit(1)
            mode = a[2:]
        else:
            rest.append(a)
    if not rest:
        print(json.dumps(
            {"error": "用法: python3 scripts/search_cmd.py [--full] [--exact|--prefix|--suffix|--word|--regex] <关键词>"},
            ensure_ascii=False))
        sys.exit(1)

    keyword = rest[0]
    entries = load_entries()

    if mode == "regex":
        try:
            pattern = re.compile(keyword, re.IGNORECASE)
        except re.error as exc:
            print(json.dumps({"error": f"无效正则: {exc}"}, ensure_ascii=False))
            sys.exit(1)
        matches = [e for e in entries if pattern.search(str(e.get("command", "")))]
    else:
        k = keyword.lower()
        if mode == "exact":
            matches = [e for e in entries if str(e.get("command", "")).lower() == k]
        elif mode == "prefix":
            matches = [e for e in entries if str(e.get("command", "")).lower().startswith(k)]
        elif mode == "suffix":
            matches = [e for e in entries if str(e.get("command", "")).lower().endswith(k)]
        elif mode == "word":
            matches = [e for e in entries if k in str(e.get("command", "")).lower().split()]
        else:  # substring
            matches = [e for e in entries if k in str(e.get("command", "")).lower()]

    if not full:
        print(json.dumps(matches, ensure_ascii=False, indent=2))
        return

    if not matches:
        print(json.dumps([], ensure_ascii=False))
        return
    for m in matches:
        print(f"## 命令: {m.get('command', '')}")
        print(f"视图: {m.get('view', '')}")
        print(f"来源: {m.get('file', '')}:{m.get('line', '')}")
        print("---")
        print(_block_text(m, entries))
        print("=" * 40)


if __name__ == "__main__":
    main()
