# Netmiko H3C Automation Configuration Skill

This repository is an automation configuration toolkit for H3C switches, routers and other network devices, built with Netmiko and Python scripts. It was originally designed for AI assistants, but can also be used directly by network operation engineers. It enables secure and efficient configuration delivery via Telnet, device initialization and firmware version verification.

## Language Navigation

- [中文](./README.md)
- [English](./README_en.md)

## Features

- **Persistent Connection Pool Service**: A FastAPI-based local HTTP backend pools Telnet connections and preserves device view state across calls, avoiding repeated reconnection and authentication overhead.
- **View State Reporting**: Each command batch returns `start_view`/`end_view`, letting the caller (AI) determine the current view and issue navigation commands.
- **Device Initialization & Version Inspection**: One-click connect and retrieve device version, returning structured JSON results.
- **Secure Configuration Deployment**: All configurations are executed via the unified `apply_config.py` script, with built-in error detection, command-count limit and timeout protection.
- **Secondary Confirmation for High-Risk Operations**: Manual approval is mandatory before executing destructive commands such as `reboot`, `undo`, `reset`. The server never auto-answers `[Y/N]` prompts.
- **Command Syntax Exploration**: For unknown commands, `explore_syntax.py` performs step-by-step `?` queries to discover the syntax instead of guessing.
- **Structured Command Reference Library**: `references/CMD-help` organizes configuration, debugging and probe commands by functional modules (VLAN, OSPF, BGP, DHCP, etc.), with a whitelist of frequently used commands to reduce lookup overhead.
- **Password Protection**: Passwords live only in server memory and travel over the loopback interface. Support interactive input or environment variable for password transmission. Plaintext passwords are forbidden in command lines or files.
- **Multi-Device Support**: Differentiate devices using distinct Telnet port numbers. The underlying proxy transparently forwards TCP traffic to corresponding Console serial ports.

## Directory Structure

```
netmiko-h3c/
├── SKILL.md                      # Skill specification & execution rules (for AI or operators)
├── CMD_HELP_STANDARD.md          # CMD-help documentation authoring spec (read before contributing)
├── README.md                     # Chinese documentation
├── README_en.md                  # English documentation (this file)
├── scripts/
│   ├── pool_client.py            # Connection-pool HTTP client (pure stdlib) + lifecycle CLI
│   ├── apply_config.py           # General configuration deployment script (service client)
│   ├── device_init.py            # Device initialization & version query script (service client)
│   ├── explore_syntax.py         # Command syntax exploration script (service client)
│   └── search_cmd.py             # Command doc query script (pure stdlib, incremental index cache)
├── server/
│   ├── connection_pool_server.py # Connection-pool backend service (FastAPI + uvicorn)
│   ├── test_pool_utils.py        # Pure-function unit tests (no device required)
│   ├── mock_h3c_device.py        # Fake H3C device Telnet server (local e2e verification)
│   └── data/                     # Runtime-generated: session descriptors & history (not committed)
└── references/
    ├── CMD-help/                 # H3C command reference documents grouped by modules
    │   ├── VLAN/
    │   │   ├── Configuration Commands/
    │   │   ├── Debug Commands/
    │   │   └── Probe Commands/
    │   ├── OSPF/
    │   ├── DHCP/
    │   ├── BGP/
    │   └── ...                   # Other functional modules
    └── high-frequency-commands.md # Whitelist of frequently used operational commands
```

## Requirements

- Python 3.9+
- [uv](https://docs.astral.sh/uv/): server dependencies (netmiko/fastapi/uvicorn) are installed automatically by `uv run` via PEP 723 inline metadata; the client scripts are pure Python stdlib and can be run with `python3`.
- Telnet service enabled on target devices. Accessible via `192.168.56.1` with specific ports (the underlying proxy forwards TCP traffic to real Console ports).

## Quick Start

### 1. Start the Connection Pool Service

All scripts execute commands through the local connection pool service, so **start it first**:

```
uv run server/connection_pool_server.py
```

It listens on `127.0.0.1:8765` by default. Overridable environment variables — these can also be placed in a `.env` file at the repository root (template: `.env.example`), which is auto-loaded by the server and the client scripts at startup (existing environment variables take precedence):

- `NETMIKO_POOL_HOST` / `NETMIKO_POOL_PORT`: server listen address
- `NETMIKO_POOL_DEVICE_IP`: device address (default `192.168.56.1`)
- `NETMIKO_POOL_URL`: client-side service URL (default `http://127.0.0.1:8765`)
- `NETMIKO_POOL_DATA_DIR`: persistence data directory (default `server/data/`)
- `NETMIKO_POOL_JWT_SECRET`: HS256 signing secret (optional but recommended). Client scripts use it to sign a short-lived JWT (default 5-minute TTL) sent in the `X-Auth-Token` header; every endpoint except `/health` validates it.

Use `scripts/pool_client.py` to check and manage the service:

```
python3 scripts/pool_client.py health             # check if the service is alive
python3 scripts/pool_client.py status             # list all sessions & current views
python3 scripts/pool_client.py status <port>      # show a specific session
python3 scripts/pool_client.py disconnect <port>  # disconnect a session
python3 scripts/pool_client.py history <port>     # read session history (default latest 100)
```

### 2. Device Initialization & Version Check

Use `scripts/device_init.py` to connect devices and fetch version information.

- Unauthenticated device:

```
python3 scripts/device_init.py <port_number>
```

- Authenticated device (interactive password prompt):

```
python3 scripts/device_init.py <port_number> --user admin
```

- Authenticated device (password via environment variable):

```
export MY_SECRET='your_password'
python3 scripts/device_init.py <port_number> --user admin --password-env MY_SECRET
```

Sample script output:

```json
{
  "status": "success",
  "start_view": {"prompt": "<H3C>", "view": "user", "hostname": "H3C", "path": ""},
  "end_view": {"prompt": "<H3C>", "view": "user", "hostname": "H3C", "path": ""},
  "output": "H3C Comware Software, Version 7.1.064, Release 9660P39 ...",
  "error": null,
  "failed_index": null
}
```

If `status` equals `error`, troubleshoot according to the error message inside `output`. The session stays pooled after version check and can be reused for configuration.

> **Compatibility note**: The old positional form `device_init.py <port> <username> <password>` was removed (plaintext passwords violate security rules). Use `--user` + `--password-env` or interactive input instead.

### 3. Deploy Configurations

All configuration tasks (VLAN creation, interface setup, routing protocols, etc.) must be executed through `scripts/apply_config.py`. Sessions and views are kept by the server, and command errors are detected server-side.

- Unauthenticated device:

```
python3 scripts/apply_config.py <port_number> "system-view" "vlan 100" "name test_vlan"
```

- Authenticated device (interactive password prompt):

```
python3 scripts/apply_config.py <port_number> "system-view" "vlan 100" --user admin
```

- Authenticated device (password via environment variable):

```
export MY_SECRET='your_password'
python3 scripts/apply_config.py <port_number> "system-view" "vlan 100" --user admin --password-env MY_SECRET
```

> **Important Limitation**: A single call accepts up to 5 commands. Split multiple commands into batches, and proceed only after the previous batch succeeds.

Output format (JSON). `start_view`/`end_view` describe the device view before/after the batch, letting the caller decide whether navigation commands are needed (e.g. `system-view`, `interface X`, `quit`, `return`):

```json
{
  "status": "success",
  "start_view": {"prompt": "<H3C>", "view": "user", "hostname": "H3C", "path": ""},
  "end_view": {"prompt": "[H3C-vlan100]", "view": "subview", "hostname": "H3C", "path": "vlan100"},
  "output": "[H3C]\n[H3C-vlan100]",
  "error": null,
  "failed_index": null
}
```

If `status` is `error`, command execution failed (e.g. `% Unrecognized command`). Stop subsequent operations and verify commands or consult relevant personnel.

### 4. Command Syntax Exploration (optional)

When unsure about the syntax of an incomplete command, use `scripts/explore_syntax.py`. The server performs step-by-step `?` queries within one connection:

```
python3 scripts/explore_syntax.py <port_number> "prefix subview commands..." "incomplete command"
```

The `chain` array in the JSON result lists the available options at each level (`type` is `keyword`/`parameter`/`multiple`).

## Command Reference Documents

The command docs under [`references/CMD-help`](./references/CMD-help/) follow the [CMD_HELP_STANDARD.md](./CMD_HELP_STANDARD.md) authoring spec; read it before adding or modifying any document.

Query the command format before deploying any configuration:

```bash
python3 scripts/search_cmd.py "<keyword>"                # JSON locator
python3 scripts/search_cmd.py --full "<keyword>"         # full help text
python3 scripts/search_cmd.py --exact --full "<keyword>" # exact command-name match + full help text
python3 scripts/search_cmd.py --view "IKE profile视图"     # commands under a specific view only
python3 scripts/search_cmd.py --file "IPsec" "ike"        # commands under a specific module/file only
```

Without `--full` the script returns a JSON array (each item contains `command`, `view`, `file`, `line`); use the Read tool on the reported line to obtain the exact command format, replacing manual grep/index lookup. With `--full` it prints the complete documentation block from the indexed line up to the next indexed line, so no file read is needed. The matching modes are mutually exclusive and default to substring: `--exact` exact command-name match (automatically strips parenthetical annotations and brace alternatives from the indexed name, e.g. `--exact "ipsec policy"` hits `ipsec { ipv6-policy \| policy }`), `--prefix` starts with the keyword, `--suffix` ends with the keyword, `--word` keyword as a full word (does not hit substrings like `ipsec`), `--regex` regex match; `--view <view>` / `--file <module>` are filters that can be combined with any matching mode. Multi-word keywords default to AND — space-separated words must all appear in the concatenation of command name plus view name (e.g. the search text for `rule (IPv4 advanced ACL view)` is `rule IPv4高级ACL视图`, so `"rule ipv4"` hits it). When nothing matches, the script returns `{"suggestions": [top 3 similar commands]}` to prompt the user; with `--full`, each suggested command additionally carries a `syntax` field (the first 5 lines of its 【命令】 section), so the syntax is visible at a glance without opening the file. The index cache (`references/.cmd_cache.jsonl`) is refreshed incrementally via git status; in non-Git environments it falls back to file-hash comparison. The `.env` switch `NETMIKO_CMD_DOC_AUTO_REFRESH` (default `true`) controls whether dynamic change detection and cache refresh are enabled. For index entries with an empty `view` column, the view is extracted from the body 【视图】 section (body takes precedence; only when the body has none does it fall back to the nearest preceding non-empty view in the same file). When a `--file <module>` filter returns nothing, the result carries a `suggested_modules` field listing the most similar module names (e.g. `--file "ike"` suggests `["IPsec"]`) so you can retry with the correct module name.

**Exception**: Commands listed in `references/high-frequency-commands.md` are confirmed standard H3C syntax and can be used directly without document lookup.

If `search_cmd.py` returns an empty array but you confirm the syntax is standard H3C command: clearly inform the user with the message: *"No matching document found, command will be executed following general syntax"*, display exact commands and obtain confirmation before running.

## Connection & Port Explanation

All devices are reachable via unified address `192.168.56.1`. Different port numbers represent different network devices. The connection pool opens and keeps a TCP Telnet connection on the specified port; a black-box underlying proxy forwards traffic to device Console serial ports. Confirm port mapping for each device before usage.

## Security & High-Risk Operations

- **Password Protection**: Never store plaintext passwords in command lines, scripts or persistent files. Passwords live only in the connection-pool server memory, travel over the loopback interface, and are never written to logs or echoed. Using `--password-env` or interactive prompt is strongly recommended.
- **Token Authentication**: Set `NETMIKO_POOL_JWT_SECRET` to enable (used as an HS256 signing secret). Client scripts auto-sign a short-lived JWT (default 5-minute TTL) into the `X-Auth-Token` header; the server validates the signature and expiry, returning 401 for invalid/expired tokens. If unset, the server runs in open mode (loopback only, with a startup warning).
- **Secondary Confirmation for Risky Commands**: Commands including `reboot`, bulk configuration removal via `undo`, `reset`, `erase` and other operations that may cause service interruption or trigger `[Y/N]` interactive prompts **must acquire explicit user authorization before execution**. The server will not automatically answer confirmation prompts. Do not proceed without permission.

## Script Detailed Description

### `server/connection_pool_server.py`

- Function: FastAPI connection-pool backend that keeps Telnet connections per port and preserves view state across requests.
- Endpoints: `GET /health`, `GET /status`, `POST /connect`, `POST /exec`, `POST /explore`, `POST /disconnect`, `GET /history`.
- Mechanism: lazy (re)connect with a bounded round-trip liveness probe that detects dead/half-open connections (device reboot), one lock per port (serialize same-port, parallelize different ports), idle timeout reaping (default 300s), graceful shutdown.
- Persistence: session descriptors (port/username/nav path, **never passwords**) and history land in `server/data/` (overridable via `NETMIKO_POOL_DATA_DIR`); views are restored automatically after a restart.
- Run: `uv run server/connection_pool_server.py` (dependencies installed automatically via PEP 723).

### `scripts/search_cmd.py`

- Function: command-document query script (pure stdlib, standalone, no pool service required). Locates the command format in `references/CMD-help` (`command`/`view`/`file`/`line`); `--full` mode prints the complete documentation block from the indexed line up to the next indexed line.
- Cache: `references/.cmd_cache.jsonl`, refreshed incrementally via git status (falls back to file-hash comparison in non-Git environments); the `.env` switch `NETMIKO_CMD_DOC_AUTO_REFRESH` (default `true`) controls whether dynamic change detection and cache refresh are enabled.
- Usage: `python3 scripts/search_cmd.py [--full] [--exact|--prefix|--suffix|--word|--regex] [--view <view>] [--file <module>] "<keyword>"` → with `--full` prints full help text, otherwise a JSON array; matching modes are mutually exclusive and default to substring, multi-word keywords default to AND, and no-match returns `{"suggestions": [top 3 similar commands]}` (see Command Reference above).

### `scripts/pool_client.py`

- Function: pure-stdlib HTTP client for the pool service, wrapping `health`/`status`/`disconnect`/`history`/`exec_cmds`/`connect`/`explore`, plus unified auth-arg parsing (`--user`/`--password`/`--password-env`).
- Usage: `python3 scripts/pool_client.py health | status [port] | disconnect <port> | history <port> [--limit N]`.

### `scripts/device_init.py`

- Function: connect and fetch device version (`dis version`).
- Notice: the session stays pooled after version check and can be reused for configuration. The positional password argument was removed.

### `scripts/apply_config.py`

- Function: send configuration commands (≤5) to the pool service, returning `start_view`/`end_view`.
- Features:
  - Uses `send_command_timing` independent of prompt patterns, compatible with arbitrary nested sub-views.
  - Server automatically detects error keywords in each command output (e.g. `% Unrecognized command`, `% Incomplete command`, `Wrong parameter`, `Too many parameters`). Terminate immediately and return `error` once detected.
  - Single call supports maximum 5 commands, enforced server-side.
- Views are not auto-switched: the caller must issue navigation commands explicitly based on `start_view`/`end_view`.

### `server/mock_h3c_device.py` (testing)

- Function: fake H3C device Telnet server that simulates a prompt state machine, for end-to-end verification without a real device.
- Usage: `python3 server/mock_h3c_device.py --port 2323 [--require-auth]`, paired with `NETMIKO_POOL_DEVICE_IP=127.0.0.1` for the pool server.

### `server/test_pool_utils.py` (testing)

- Function: pure-function unit tests (view parsing, error detection, password sanitization, command-count limit, nav-path tracking/reconciliation, history read/trim, descriptor persistence & corrupt-file tolerance).
- Usage: `uv run server/test_pool_utils.py`.

## Session Persistence & History

The server persists each session's recovery plan and call history in the data directory (default `server/data/`, overridable via `NETMIKO_POOL_DATA_DIR`):

- `pool_sessions.json`: session descriptors (port, username, **nav path**). The nav path is the command sequence that replays from the user view to the current view (e.g. `system-view → interface GigabitEthernet1/0/1`).
- `history_<port>.jsonl`: per-port commands and outputs (JSON Lines, keeping the latest 1000 lines).

**Restart recovery**: after restart the server loads the descriptors and reconnects to restore views — unauthenticated devices restore automatically at startup; authenticated devices restore **lazily** (the connection is rebuilt and nav commands replayed the next time the caller supplies credentials). Recovery is best-effort: if device state changed and replay fails, the nav path is reconciled against the actual detected view, so the `start_view` the caller sees is always the true view.

**Reading history**: `GET /history?port=<port>&limit=N`, or on the CLI `python3 scripts/pool_client.py history <port> [--limit N]`.

**Security red line**: descriptors and history **never contain passwords** (passwords live only in server memory). An explicit `/disconnect` removes that port's recovery plan.

## Typical Workflow

1. Start the pool service: `uv run server/connection_pool_server.py`, then confirm with `python3 scripts/pool_client.py health`.
2. Collect device port and authentication information.
3. Run `device_init.py` for each device to retrieve version and identify connectivity/authentication issues early.
4. Look up proper command syntax in `references/CMD-help` based on requirements.
5. Invoke `apply_config.py` in batches (≤5 commands per run). Decide navigation commands based on `start_view`/`end_view`, and validate return results.
6. Verify key configurations using inspection commands such as `display current-configuration | include ...`.
7. For high-risk commands, obtain manual approval before submitting to the script.
8. After finishing a task, navigate back to user view with `return` or disconnect via `pool_client.py disconnect <port>` to avoid leftover view state.

## Contribution & Extension

- **Contributing command references (CMD-help)**: before adding or modifying command docs, read the [CMD_HELP_STANDARD.md](./CMD_HELP_STANDARD.md) spec first to match the structure that [`scripts/search_cmd.py`](./scripts/search_cmd.py) depends on:
  - Name files under [`references/CMD-help/<module>/`](./references/CMD-help/) as `<module>配置命令.md` / `<module>调试命令.md` / `<module>Probe命令.md`;
  - Add a `<!-- CMD-INDEX ... -->` index block at the top of every file (`command | view | Lline`), where `Lline` must point to the command-block title line in the body;
  - Organize the body per the spec: block title, full-width separator, and `【命令】`/`【视图】` sections; when the index view column is empty, the body `【视图】` section must be filled accurately;
  - Verify with `python3 scripts/search_cmd.py --exact "<new command>"` (the cache is rebuilt automatically via git status).
- If script defects are found or new enhancements are needed (new authentication methods, custom error matching logic, etc.), modify Python files inside [`scripts/`](./scripts/) or [`server/connection_pool_server.py`](./server/connection_pool_server.py). Keep consistent JSON output structure and error detection logic.
- Issues and Pull Requests are welcome to improve this repository.

## License

This tool is released under the [MIT License](LICENSE)

---

This standardized workflow makes routine configuration on H3C devices secure, traceable and easy to automate. For further details, refer to rules defined in [SKILL.md](./SKILL.md).
