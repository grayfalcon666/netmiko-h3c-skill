# Netmiko H3C Automation Configuration Skill

This repository is an automation configuration toolkit for H3C switches, routers and other network devices, built with Netmiko and Python scripts. It was originally designed for AI assistants, but can also be used directly by network operation engineers. It enables secure and efficient configuration delivery via Telnet, device initialization and firmware version verification.

## Language Navigation

- [中文](./README.md)
- [English](./README_en.md)

## Features

- **Environment Self-Check**: Automatically verify whether the Netmiko library is installed with clear guidance.
- **Device Initialization & Version Inspection**: One-click disable pagination, retrieve device version and return structured JSON results.
- **Secure Configuration Deployment**: All configurations are executed via the unified `apply_config.py` script, built-in view switching, error detection and timeout protection to prevent human misoperation.
- **Secondary Confirmation for High-Risk Operations**: Manual approval is mandatory before executing destructive commands such as `reboot`, `undo`, `reset`.
- **Structured Command Reference Library**: `references/CMD-help` organizes configuration, debugging and probe commands by functional modules (VLAN, OSPF, BGP, DHCP, etc.), with a whitelist of frequently used commands to reduce lookup overhead.
- **Password Protection**: Support interactive input or environment variable for password transmission. Plaintext passwords are forbidden in command lines or files.
- **Multi-Device Support**: Differentiate devices using distinct Telnet port numbers. The underlying proxy transparently forwards TCP traffic to corresponding Console serial ports.

## Directory Structure

```
netmiko-h3c/
├── SKILL.md                      # Skill specification & execution rules (for AI or operators)
├── README.md                     # Chinese documentation
├── README_en.md                  # English documentation (this file)
├── scripts/
│   ├── device_init.py            # Device initialization & version query script
│   └── apply_config.py           # General configuration deployment script
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

- Python 3.6+
- Netmiko library: `pip install netmiko`
- Telnet service enabled on target devices. Accessible via `192.168.56.1` with specific ports (the underlying proxy forwards TCP traffic to real Console ports).

## Quick Start

### 1. Verify Netmiko Environment

```
python3 -c "import netmiko; print(netmiko.__version__)"
```

If the version number is printed, the environment is ready. Otherwise run `pip install netmiko`.

### 2. Device Initialization & Version Check

Use `scripts/device_init.py` to connect devices, automatically disable pagination and fetch version information.

- Unauthenticated device:

```
python3 scripts/device_init.py <port_number>
```

- Authenticated device:

```
python3 scripts/device_init.py <port_number> <username> <password>
```

> 
> Note: Password will not be recorded in command history. Interactive input or environment variable passing is recommended.

Sample script output:

```
{"status": "success", "output": "H3C Comware Software, Version 7.1.064, Release 9660P39 ..."}
```

If `status` equals `error`, troubleshoot according to the error message inside `output`.

### 3. Deploy Configurations

All configuration tasks (VLAN creation, interface setup, routing protocols, etc.) must be executed through `scripts/apply_config.py`. The script automatically handles view switching, disables pagination and detects command errors.

- Unauthenticated device:

```
python3 scripts/apply_config.py <port_number> "vlan 100" "name test_vlan"
```

- Authenticated device (interactive password prompt):

```
python3 scripts/apply_config.py <port_number> "vlan 100" --user admin
```

- Authenticated device (password via environment variable):

```
export MY_SECRET='your_password'
python3 scripts/apply_config.py <port_number> "vlan 100" --user admin --password-env MY_SECRET
```

> 
> **Important Limitation**: A single call accepts up to 5 commands. Split multiple commands into batches, and proceed only after the previous batch succeeds.

Output format (JSON):

```
{"status": "success", "output": "..."}
```

If `status` is `error`, command execution failed (e.g. `% Unknown command`). Stop subsequent operations and verify commands or consult relevant personnel.

## Command Reference Documents

Check corresponding module files under `references/CMD-help` before deploying any configuration.
Example for adding VLAN:

```
grep -rl "vlan" references/CMD-help/ | grep -i config
```

Read matched `.md` files to obtain accurate command syntax.

**Exception**: Commands listed in `references/high-frequency-commands.md` are confirmed standard H3C syntax and can be used directly without document lookup.

If no matching document is found but you confirm the syntax is standard H3C command: clearly inform the user with the message: *"No matching document found, command will be executed following general syntax"*, display exact commands and obtain confirmation before running.

## Connection & Port Explanation

All devices are reachable via unified address `192.168.56.1`. Different port numbers represent different network devices. A black-box underlying proxy forwards Telnet TCP connections on specified ports to device Console serial ports. Confirm port mapping for each device before usage.

## Security & High-Risk Operations

- **Password Protection**: Never store plaintext passwords in command lines, scripts or persistent files. Using `--password-env` or interactive prompt is strongly recommended.
- **Secondary Confirmation for Risky Commands**: Commands including `reboot`, bulk configuration removal via `undo`, `reset`, `erase` and other operations that may cause service interruption or trigger `[Y/N]` interactive prompts **must acquire explicit user authorization before execution**. The script will not automatically answer confirmation prompts. Do not proceed without permission.

## Script Detailed Description

### `device_init.py`

- Function: Establish connection, execute `screen-length disable`, collect device version with `display version`, then close the session.
- Scenario: Initial device inspection. The session terminates after each run. Separate connections are required for configuration tasks.

### `apply_config.py`

- Function: Establish Telnet session and run fixed workflow: `return` → `screen-length disable` → `system-view` → user-defined commands → `return`.
- Features:
  - Use `send_command_timing` independent of prompt patterns, compatible with arbitrary nested sub-views.
  - Automatically detect error keywords in each command output (e.g. `% Unknown command`, `^ Error`). Terminate immediately and return `error` once detected.
  - All timeout values ≤10 seconds.
  - Single call supports maximum 5 commands. Multiple commands requiring continuous execution under the same sub-view should be placed within one call (view state persists during a single invocation).
- Notice: The Telnet connection closes after each call. A new connection and system-view entry will be created on next invocation. Do NOT rely on persistent view state across separate calls.

## Typical Workflow

1. Environment check: Confirm Netmiko availability.
2. Collect device port and authentication information.
3. Run `device_init.py` for each device to retrieve version and identify connectivity/authentication issues early.
4. Look up proper command syntax in `references/CMD-help` based on requirements.
5. Invoke `apply_config.py` in batches (≤5 commands per run) and validate return results.
6. Verify key configurations using inspection commands such as `display current-configuration | include ...`.
7. For high-risk commands, obtain manual approval before submitting to the script.

## Contribution & Extension

- To add command references for new functional modules: create folders under `references/CMD-help` and write standardized `.md` documents.
- If script defects are found or new enhancements are needed (new authentication methods, custom error matching logic, etc.), modify Python files inside `scripts/`. Keep consistent JSON output structure and error detection logic.
- Issues and Pull Requests are welcome to improve this repository.

## License

This tool is released under the [MIT License](LICENSE)

---

This standardized workflow makes routine configuration on H3C devices secure, traceable and easy to automate. For further details, refer to rules defined in [SKILL.md](./SKILL.md).