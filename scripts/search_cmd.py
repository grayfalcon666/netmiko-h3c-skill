#!/usr/bin/env python3
"""
search_cmd.py – H3C 命令文档查询脚本（纯标准库，无第三方依赖）

把 `references/CMD-help` 的 CMD-INDEX 语义索引缓存到 `references/.cmd_cache.jsonl`，
Agent 只需传关键词即可拿到精确文档定位（command/view/file/line），无需碰文件系统搜索。

- 缓存增量更新由 .env 开关 `NETMIKO_CMD_DOC_AUTO_REFRESH` 控制（默认 true）：
    - true ：用 `git status --porcelain -- references/CMD-help` 检测变更，有变更才重建；
             非 Git 仓库时回退到「路径+修改时间」哈希与缓存头比对，不一致才重建。
    - false：不做任何变更检查，直接用已有缓存；仅缓存缺失时构建一次。
- 查询：默认子串匹配（多词为 AND，跨 command+view 全包含）；支持 `--view`/`--file` 过滤；
        无匹配时返回前 3 个相似命令建议（`{"suggestions": [...]}`）。

CLI：
  python3 scripts/search_cmd.py [--full] [--exact|--prefix|--suffix|--word|--regex] [--view <视图>] [--file <模块>] <关键词...>
    --full  直接输出匹配命令的完整文档块（默认输出 JSON 定位）
    --exact  命令名与关键词完全相等（自动剥离索引命令名的括号注记与花括号备选，
             如 ipsec { ipv6-policy \\| policy } 可被 --exact "ipsec policy" 命中）
    --prefix 命令名以关键词开头
    --suffix 命令名以关键词结尾
    --word   关键词作为完整单词出现（按空格分词，非子串）
    --regex  关键词为正则表达式（忽略大小写）
    --view   仅看指定视图下的命令（视图名子串匹配，大小写不敏感）
    --file   仅看指定文件/模块路径下的命令（如 --file IPsec）
    五个匹配模式互斥，默认子串匹配；--view/--file 是过滤条件，可与任一匹配模式叠加
    多词默认 AND（空格分隔的词须全部出现在「命令名+视图名」拼接串中）
    无匹配时返回 {"suggestions": [前3个相似命令]}（regex 模式除外）；
    --full 模式下无匹配时直接输出前 3 个相似命令的紧凑摘要
    （{command, view, syntax, file, line}，syntax 为【命令】段落前 5 行），无需再 Read
"""

from __future__ import annotations

import difflib
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


def _body_view(lines: list[str], ref: int) -> str:
    """从命令文档块正文提取【视图】小节视图名（索引里 view 为空时以正文为准）。

    自索引行向后找本块的【视图】小节，收集其后若干非空行（正文可能列多个视图，
    用 / 连接）；越过本块标题（**…\\--…**）视为跨块，立即返回空。找不到返回空串。
    """
    for i in range(ref, len(lines)):
        line = lines[i].strip()
        if line.startswith("【视图】"):
            vals: list[str] = []
            for j in range(i + 1, len(lines)):
                nxt = lines[j].strip()
                if not nxt:
                    continue
                if nxt.startswith("【"):
                    break
                vals.append(nxt)
            return "/".join(vals)
        if i > ref and line.startswith("**") and line.endswith("**") and "\\--" in line:
            return ""
    return ""


def _parse_cmd_index(content: str, rel: str) -> list[dict]:
    """解析一个文件的 CMD-INDEX 块（`命令名 | 视图 | L行号`）。格式不符自动跳过。

    view 为空的条目优先取正文【视图】小节（索引丢视图时以正文为准），
    正文也没有时回退到同文件里最近一条有视图的条目。
    """
    entries: list[dict] = []
    in_block = False
    last_view = ""
    lines = content.splitlines()
    for line in lines:
        if not in_block:
            if "CMD-INDEX" in line:
                in_block = True
            continue
        if "-->" in line:
            break
        # 行分隔符为未转义的 |；命令名里的花括号备选 { a \| b } 含反斜杠转义竖线，不拆
        parts = [p.strip() for p in re.split(r"(?<!\\)\|", line)]
        if len(parts) < 3:
            continue
        m = _INDEX_ROW.search(parts[-1])
        if not m:
            continue
        view = parts[1]
        if not view:
            view = _body_view(lines, int(m.group(1))) or last_view
        else:
            last_view = view
        entries.append({
            "command": parts[0],
            "view": view,
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


_SEP = re.compile(r"^-{10,}\s*$")


def _block_text(entry: dict, all_entries: list[dict]) -> str:
    """返回该命令的完整文档块：从本索引行到同文件下一个索引行之前。

    结束行取同文件所有索引行中大于本行号的最小者；无后续索引时，用「本块
    标题之后的第二条整行分隔线」兜底——第一条是本块的，第二条是下一块的，
    避免把文件末尾未索引的命令块/目录等无关内容一起截进来。
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
    if end > len(lines):
        # 命令块以整行分隔线（紧随 **标题**）隔开；第一条是本块的，第二条是下一块的
        seen = 0
        for i in range(line + 1, len(lines)):
            if _SEP.match(lines[i]):
                seen += 1
                if seen >= 2:
                    end = i
                    break
    return "\n".join(lines[line - 1 : end - 1])


_SECTION_MARK = re.compile(r"【[^】]+】")


def _clean_syntax(line: str) -> str:
    """去除 Markdown 粗/斜体标记与转义竖线，归一文档的方括号包裹注记。

    H3C 文档把整条语法写成 `**[cmd**[ { ... } ... ]]` 样式，去掉 **、* 与
    `\\|` 后形如 `[cmd[ { ... } ... ]]]`；这里把行首 `[` 与命令后的 `[`
    （包裹注记的开口）归一，并把尾部多余的成对 `]` 合并为一个。
    """
    s = line.replace("**", "").replace("\\|", "|").replace("*", "")
    s = re.sub(r"^\[([^\[\]]+?)\s*\[", r"\1 ", s)
    s = re.sub(r"\]{2,}$", "]", s)
    return re.sub(r"\s+", " ", s).strip()


def _syntax_summary(entry: dict, all_entries: list[dict], max_lines: int = 5) -> str:
    """从文档块提取【命令】段落的前 max_lines 行，作为紧凑语法摘要。

    【命令】段落取该小节标题到下一个【…】小节标题之间的行；空行剔除后
    最多保留 max_lines 行，换行拼接。取不到【命令】段落时回退到文档块
    首个非空行（通常是“模块 -- 模块 -- 命令”标题行）。
    """
    lines = _block_text(entry, all_entries).splitlines()
    start = next((i for i, l in enumerate(lines) if l.strip() == "【命令】"), None)
    if start is None:
        for l in lines:
            if l.strip():
                return _clean_syntax(l)
        return ""
    end = len(lines)
    for i in range(start + 1, len(lines)):
        # 文档里小节标题可能带尾随 ]（模板注记），用前缀匹配即可
        if _SECTION_MARK.match(lines[i].strip()):
            end = i
            break
    picked = [_clean_syntax(l) for l in lines[start + 1 : end] if l.strip()]
    return "\n".join(picked[:max_lines])


_MODES = ("--exact", "--prefix", "--suffix", "--word", "--regex")
_PARENS = re.compile(r"\([^()]*\)")
_BRACE_GROUP = re.compile(r"\{([^{}]*)\}")
_USAGE = (
    "用法: python3 scripts/search_cmd.py [--full] "
    "[--exact|--prefix|--suffix|--word|--regex] [--view <视图>] [--file <模块>] <关键词...>"
)


def _apply_filters(entries: list[dict], view_filter: str, file_filter: str) -> list[dict]:
    """按 --view / --file 过滤（子串匹配，大小写不敏感）。"""
    if view_filter:
        v = view_filter.lower()
        entries = [e for e in entries if v in str(e.get("view", "")).lower()]
    if file_filter:
        f = file_filter.lower()
        entries = [e for e in entries if f in str(e.get("file", "")).lower()]
    return entries


def _command_variants(cmd: str) -> set[str]:
    """生成命令名「实际设备写法」候选，供 --exact 比对。

    索引里的命令名可能带两种注记，设备实际命令并不包含：
    - 括号注记 (…)：rule (IPv4 advanced ACL view) → rule
    - 花括号备选 { a \\| b }：ipsec { ipv6-policy \\| policy } → ipsec ipv6-policy / ipsec policy
    """
    variants = {_PARENS.sub("", cmd).strip()}
    while True:
        nxt: set[str] = set()
        expanded = False
        for v in variants:
            m = _BRACE_GROUP.search(v)
            if not m:
                nxt.add(v)
                continue
            expanded = True
            prefix = v[: m.start()].rstrip()
            suffix = v[m.end() :].lstrip()
            for alt in (a.strip() for a in re.split(r"\\\|", m.group(1))):
                nxt.add(" ".join(x for x in (prefix, alt, suffix) if x))
        variants = nxt
        if not expanded:
            break
    return {re.sub(r"\s+", " ", v).strip() for v in variants if v.strip()}


def _match(entries: list[dict], mode: str, keyword: str) -> list[dict]:
    """按模式匹配命令名；默认子串，多词为 AND（跨 command+view 全包含）。"""
    if mode == "regex":
        pattern = re.compile(keyword, re.IGNORECASE)
        return [e for e in entries if pattern.search(str(e.get("command", "")))]

    k = keyword.lower()
    if mode == "exact":
        return [e for e in entries
                if k in {v.lower() for v in _command_variants(str(e.get("command", "")))}]
    if mode == "prefix":
        return [e for e in entries if str(e.get("command", "")).lower().startswith(k)]
    if mode == "suffix":
        return [e for e in entries if str(e.get("command", "")).lower().endswith(k)]
    if mode == "word":
        return [e for e in entries if k in str(e.get("command", "")).lower().split()]

    words = k.split()
    if len(words) > 1:
        # AND：词须全部出现在「去掉括号注记的命令名 + 视图」中
        return [e for e in entries if all(
            w in _PARENS.sub("", str(e.get("command", ""))).lower()
            + " " + str(e.get("view", "")).lower()
            for w in words)]
    return [e for e in entries if k in str(e.get("command", "")).lower()]


def _suggestions(entries: list[dict], keyword: str, limit: int = 3) -> list[dict]:
    """无匹配时的模糊建议：按 command/view 关键词命中数与相似度取前 limit 条。

    同一命令名（去掉括号注记）只保留得分最高的一条，避免同一命令的视图变体刷屏。
    """
    words = keyword.lower().split()
    q = " ".join(words)
    best: dict[str, tuple[int, dict]] = {}
    for e in entries:
        cmd = str(e.get("command", "")).lower()
        view = str(e.get("view", "")).lower()
        bare = _PARENS.sub("", cmd)
        cmd_hits = sum(1 for w in words if w in cmd)
        view_hits = sum(1 for w in words if w in view)
        if cmd_hits or view_hits:
            score = cmd_hits * 2000 + view_hits * 1000
        else:
            ratio = difflib.SequenceMatcher(None, q, cmd).ratio()
            if ratio < 0.7:
                continue
            score = int(ratio * 100)
        prev = best.get(bare)
        if prev is None or score > prev[0]:
            best[bare] = (score, e)
    ranked = sorted(((sc, bare, e) for bare, (sc, e) in best.items()),
                    key=lambda x: (-x[0], x[1]))
    return [e for _, _, e in ranked[:limit]]


def _module_of(file_path: str) -> str:
    """从缓存 file 路径提取顶层模块目录名（CMD-help 下第一级）；不含 CMD-help 时返回空串。"""
    parts = str(file_path).replace("\\", "/").split("/")
    try:
        idx = parts.index("CMD-help")
    except ValueError:
        return ""
    if idx + 1 < len(parts):
        return parts[idx + 1]
    return ""


def _top_modules(entries: list[dict]) -> list[str]:
    """从缓存所有文件路径提取顶层模块目录名，去重排序。"""
    return sorted({m for e in entries if (m := _module_of(str(e.get("file", ""))))})


def _suggest_modules(entries: list[dict], keyword: str, limit: int = 3) -> list[str]:
    """按 difflib 相似度找与 keyword 最相似的模块目录名，取前 limit 个。

    附加信号：该模块下 command 名含关键词的条数（如 `ike` 会命中 IPsec 模块下
    大量 ike 命令），避免纯字符相似度对短词误报（如 `ike` 与 IPoE 字符相似）。
    得分 = 相似度 + min(命令命中数, 5) * 0.15；无命令命中时要求相似度 ≥0.6。
    """
    q = keyword.lower()
    cmd_hits: dict[str, int] = {}
    for e in entries:
        mod = _module_of(str(e.get("file", "")))
        if mod and q in str(e.get("command", "")).lower():
            cmd_hits[mod] = cmd_hits.get(mod, 0) + 1
    scored: list[tuple[float, str]] = []
    for m in _top_modules(entries):
        ratio = difflib.SequenceMatcher(None, q, m.lower()).ratio()
        bonus = min(cmd_hits.get(m, 0), 5) * 0.15
        if bonus > 0 or ratio >= 0.6:
            scored.append((ratio + bonus, m))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [m for _, m in scored[:limit]]


def main() -> None:
    full = False
    mode = "substring"  # 默认子串匹配
    view_filter = ""
    file_filter = ""
    rest: list[str] = []
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--full":
            full = True
        elif a == "--view":
            i += 1
            if i >= len(args):
                print(json.dumps({"error": "--view 缺少视图参数"}, ensure_ascii=False))
                sys.exit(1)
            view_filter = args[i]
        elif a == "--file":
            i += 1
            if i >= len(args):
                print(json.dumps({"error": "--file 缺少文件参数"}, ensure_ascii=False))
                sys.exit(1)
            file_filter = args[i]
        elif a in _MODES:
            if mode != "substring":
                print(json.dumps(
                    {"error": "匹配模式互斥，只能指定一个: " + " | ".join(_MODES)},
                    ensure_ascii=False))
                sys.exit(1)
            mode = a[2:]
        else:
            rest.append(a)
        i += 1

    keyword = " ".join(rest).strip()
    if not keyword and not view_filter and not file_filter:
        print(json.dumps({"error": _USAGE}, ensure_ascii=False))
        sys.exit(1)

    entries = load_entries()
    filtered = _apply_filters(entries, view_filter, file_filter)

    if not keyword:
        matches = filtered
    else:
        try:
            matches = _match(filtered, mode, keyword)
        except re.error as exc:
            print(json.dumps({"error": f"无效正则: {exc}"}, ensure_ascii=False))
            sys.exit(1)

    if not matches:
        sugg = _suggestions(filtered, keyword) if keyword and mode != "regex" else []
        result: dict = {"suggestions": sugg}
        # --file 过滤结果为空时，从模块目录名中找最相似的模块名提示
        if file_filter and not filtered:
            mods = _suggest_modules(entries, file_filter)
            if mods:
                result["suggested_modules"] = mods
        if full and sugg:
            compact = [{
                "command": s.get("command", ""),
                "view": s.get("view", ""),
                "syntax": _syntax_summary(s, entries),
                "file": s.get("file", ""),
                "line": s.get("line", 0),
            } for s in sugg]
            result["suggestions"] = compact
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if not full:
        print(json.dumps(matches, ensure_ascii=False, indent=2))
        return

    _print_full(matches, entries)


def _print_full(matches: list[dict], entries: list[dict]) -> None:
    """按 --full 格式输出每个命令的文档块。"""
    for m in matches:
        print(f"## 命令: {m.get('command', '')}")
        print(f"视图: {m.get('view', '')}")
        print(f"来源: {m.get('file', '')}:{m.get('line', '')}")
        print("---")
        print(_block_text(m, entries))
        print("=" * 40)


if __name__ == "__main__":
    main()
