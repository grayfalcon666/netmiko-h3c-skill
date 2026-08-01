# Netmiko H3C 自动化配置 Skill

>
> 语言版本：[中文](./README.md) | [English](./README_en.md)

本仓库是一个面向新华三（H3C）交换机、路由器等设备的自动化配置技能包，基于 Netmiko 和 Python 脚本实现。它最初为 AI 助手设计，但同样适合网络运维人员直接使用，能安全、高效地通过 Telnet 下发配置、初始化设备并验证版本信息。

## 功能特性

- **常驻连接池服务**：一个基于 FastAPI 的本机 HTTP 后端服务池化保持 Telnet 连接，跨调用保持设备视图状态，避免反复重连与认证开销。
- **视图状态上报**：每次命令批次返回 `start_view`/`end_view`，调用方（AI）据此判断当前视图并决定导航命令。
- **设备初始化与版本查验**：一键连接并获取设备版本，返回结构化 JSON 结果。
- **安全的配置下发**：所有配置通过统一的 `apply_config.py` 脚本执行，内置错误检测、命令数量上限和超时保护。
- **高危操作二次确认**：对 `reboot`、`undo`、`reset` 等危险命令在执行前强制人工授权，服务端不自动回复 `[Y/N]`。
- **命令语法探索**：对未知命令用 `explore_syntax.py` 逐级 `?` 查询语法，避免盲猜试错。
- **结构化命令参考库**：`references/CMD-help` 按功能模块（VLAN、OSPF、BGP、DHCP 等）整理了配置、调试、Probe 命令，并配有高频命令白名单，减少查阅成本。
- **密码保护**：密码仅存于服务端内存、经本机回环传输，支持交互式输入或环境变量传递，禁止明文写入命令行或文件。
- **多设备支持**：通过不同 Telnet 端口号区分设备，底层透明转发至对应 Console 串口。

## 目录结构

```
netmiko-h3c/
├── SKILL.md                      # 技能描述与执行规范（供 AI 或使用者参考）
├── README.md                     # 本文件
├── scripts/
│   ├── pool_client.py            # 连接池服务 HTTP 客户端（纯标准库）+ 生命周期 CLI
│   ├── apply_config.py           # 配置下发通用脚本（服务客户端）
│   ├── device_init.py            # 设备初始化与版本查询脚本（服务客户端）
│   └── explore_syntax.py         # 命令语法探索脚本（服务客户端）
├── server/
│   ├── connection_pool_server.py # 连接池后端服务（FastAPI + uvicorn）
│   ├── test_pool_utils.py        # 纯函数单元测试（无需真实设备）
│   ├── mock_h3c_device.py        # 假 H3C 设备 Telnet 服务器（本地端到端验证用）
│   └── data/                     # 运行时生成：会话描述符与历史记录（不入库 git）
└── references/
    ├── CMD-help/                 # 按模块整理的 H3C 命令参考文档
    │   ├── VLAN/
    │   │   ├── 配置命令/
    │   │   ├── 调试命令/
    │   │   └── Probe命令/
    │   ├── OSPF/
    │   ├── DHCP/
    │   ├── BGP/
    │   └── ...                   # 其他功能模块
    └── high-frequency-commands.md # 高频操作白名单命令清单
```

## 环境要求

- Python 3.9+
- [uv](https://docs.astral.sh/uv/)：服务端依赖（netmiko/fastapi/uvicorn）由 `uv run` 依据脚本头部的 PEP 723 内联元数据自动创建临时环境并安装，无需手动 `pip install`；客户端脚本为纯 Python 标准库，可用 `python3` 直接运行。
- 设备侧需开启 Telnet 服务，并可通过 `192.168.56.1` 的特定端口访问（底层代理负责将 TCP 流量转发至真实 Console 口）。

## 快速开始

### 1. 启动连接池服务

所有脚本都通过本机连接池服务执行命令，**使用前必须先启动该服务**：

```bash
uv run server/connection_pool_server.py
```

默认监听 `127.0.0.1:8765`。可用环境变量覆盖，也可写入仓库根目录的 `.env` 文件（模板见 `.env.example`），服务端与客户端脚本启动时会自动加载（已存在的环境变量优先）：

- `NETMIKO_POOL_HOST` / `NETMIKO_POOL_PORT`：服务监听地址
- `NETMIKO_POOL_DEVICE_IP`：设备地址，默认 `192.168.56.1`
- `NETMIKO_POOL_URL`：客户端连接的服务地址（默认 `http://127.0.0.1:8765`）
- `NETMIKO_POOL_DATA_DIR`：持久化数据目录（默认 `server/data/`）

启动后可用 `scripts/pool_client.py` 检查与管理系统：

```bash
python3 scripts/pool_client.py health          # 检查服务是否存活
python3 scripts/pool_client.py status          # 列出所有会话与当前视图
python3 scripts/pool_client.py status <端口>   # 查看指定端口会话
python3 scripts/pool_client.py disconnect <端口>  # 断开指定端口会话
python3 scripts/pool_client.py history <端口>  # 读取该端口会话历史（默认最近 100 条）
```

### 2. 设备初始化与版本查验

使用 `scripts/device_init.py` 连接设备并获取版本。

- 无认证设备：
  ```bash
  python3 scripts/device_init.py <端口号>
  ```
- 有认证设备（交互输入密码）：
  ```bash
  python3 scripts/device_init.py <端口号> --user admin
  ```
- 有认证设备（通过环境变量）：
  ```bash
  export MY_SECRET='your_password'
  python3 scripts/device_init.py <端口号> --user admin --password-env MY_SECRET
  ```

脚本输出示例：
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

若 `status` 为 `error`，根据 `output` 中的错误信息排查。会话由连接池保持，版本查验后不会断开，可继续配置。

> **兼容性说明**：旧版的 `device_init.py <端口> <用户名> <密码>` 位置参数密码形式已移除（明文密码违反安全规则），请改用 `--user` + `--password-env` 或交互输入。

### 3. 下发配置

所有配置任务（VLAN 创建、接口设置、路由协议等）均通过 `scripts/apply_config.py` 执行。会话与视图由服务端保持，命令错误由服务端自动检测。

- 无认证设备：
  ```bash
  python3 scripts/apply_config.py <端口号> "system-view" "vlan 100" "name test_vlan"
  ```
- 有认证设备（交互输入密码）：
  ```bash
  python3 scripts/apply_config.py <端口号> "system-view" "vlan 100" --user admin
  ```
- 有认证设备（通过环境变量）：
  ```bash
  export MY_SECRET='your_password'
  python3 scripts/apply_config.py <端口号> "system-view" "vlan 100" --user admin --password-env MY_SECRET
  ```

> **重要限制**：单次调用最多支持 5 条命令，若需执行更多命令请分批次调用，且保证上一批次成功后再继续。

输出为 JSON，其中 `start_view`/`end_view` 描述本批命令执行前后的设备视图，供调用方判断是否需要导航（如 `system-view`、`interface X`、`quit`、`return`）：
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
若 `status` 为 `error`，说明命令执行过程中出现错误（如 `% Unknown command`），请停止后续操作，检查命令或联系用户。

### 4. 命令语法探索（可选）

当不确定某命令的后续语法时，使用 `scripts/explore_syntax.py`，由服务端在一次连接中逐级 `?` 查询：

```bash
python3 scripts/explore_syntax.py <端口号> "前置子视图命令..." "待探索的不完整命令"
```

返回 JSON 中的 `chain` 数组按探索顺序给出每级可用选项（`type` 为 `keyword`/`parameter`/`multiple`）。

## 命令参考文档

执行任何配置前，请先查阅 `references/CMD-help` 目录下对应的功能模块。例如需要添加 VLAN：
```bash
grep -rl "vlan" references/CMD-help/ | grep -i config
```
然后读取匹配的 `.md` 文件获取精确的命令格式。

**例外**：`references/high-frequency-commands.md` 中列出的命令已确认为通用 H3C 语法，可直接使用，无需查阅文档。

若在文档中未找到对应命令，但可确定是 H3C 标准语法，请在执行前明确告知用户“未找到对应文档，将按通用语法执行”并展示具体命令，获得确认后继续。

## 连接与端口说明

所有设备统一通过地址 `192.168.56.1` 访问，不同设备使用不同端口号区分。连接池服务向指定端口的 TCP Telnet 建立并保持连接，底层黑盒代理会将连接透明转发到对应网络设备的 Console 串口。实际使用时请先确认每台设备映射的端口号。

## 安全与高危操作

- **密码保护**：严禁在命令行、脚本或任何持久化文件中明文写入密码。密码仅保存在连接池服务内存中，经本机回环传输，服务端不落日志、不回显。强烈建议使用 `--password-env` 或脚本交互提示输入。
- **高危命令二次确认**：对于 `reboot`、`undo` 清空大段配置、`reset`、`erase` 等可能破坏业务或触发 `[Y/N]` 交互的命令，**必须**在执行前获得用户明确的授权。服务端不会替您回答任何确认提示，未经允许请勿继续执行。

## 会话持久化与历史

服务把每个会话的恢复计划与调用历史落在数据目录（默认 `server/data/`，可用 `NETMIKO_POOL_DATA_DIR` 覆盖）：

- `pool_sessions.json`：会话描述符（端口、用户名、**导航路径**）。导航路径是从用户视图重放到当前视图的命令序列（如 `system-view → interface GigabitEthernet1/0/1`）。
- `history_<端口>.jsonl`：该端口每次调用的命令与输出（JSON Lines，保留最近 1000 行）。

**重启恢复**：服务重启后自动加载描述符并重连恢复视图——无认证设备在启动时自动恢复；认证设备**懒恢复**（下次调用方携带凭据时重建连接并重放导航）。恢复是尽力而为：若设备状态变化导致重放失败，按实际探测到的视图对账，调用方拿到的 `start_view` 始终是真实视图。

**读取历史**：`GET /history?port=<端口>&limit=N`，或命令行 `python3 scripts/pool_client.py history <端口> [--limit N]`。

**安全红线**：描述符与历史中**绝不包含密码**（密码仅存服务端内存）。显式 `/disconnect` 会移除该端口的恢复计划。

## 脚本详细说明

### `server/connection_pool_server.py`
- 功能：FastAPI 连接池后端服务，池化保持各端口的 Telnet 连接，跨请求保持视图状态。
- 端点：`GET /health`、`GET /status`、`POST /connect`、`POST /exec`、`POST /explore`、`POST /disconnect`、`GET /history`。
- 机制：懒建连（连接中断自动重建，存活判定用有界往返探测，能发现设备重启/半开导致的死连接）、每端口一把锁（同端口串行、不同端口并行）、空闲超时自动回收（默认 300s）、优雅关闭。
- 持久化：会话描述符（端口/用户名/导航路径，**不含密码**）与历史消息落在 `server/data/`（可用 `NETMIKO_POOL_DATA_DIR` 覆盖），重启后自动恢复视图。
- 启动：`uv run server/connection_pool_server.py`（依赖经 PEP 723 自动安装）。

### `scripts/pool_client.py`
- 功能：连接池服务的纯标准库 HTTP 客户端，封装 `health`/`status`/`disconnect`/`history`/`exec_cmds`/`connect`/`explore`，并提供统一的认证参数解析（`--user`/`--password`/`--password-env`）。
- 用法：`python3 scripts/pool_client.py health | status [端口] | disconnect <端口> | history <端口> [--limit N]`。

### `scripts/device_init.py`
- 功能：连接设备并获取版本信息（`dis version`）。
- 注意：会话保持池化，版本查验后不会断开，可继续下发配置。位置参数密码已移除。

### `scripts/apply_config.py`
- 功能：向连接池服务下发配置命令（≤5 条），返回 `start_view`/`end_view`。
- 特点：
  - 使用 `send_command_timing` 不依赖提示符，可适应任意嵌套子视图。
  - 服务端自动检测每一条命令的输出是否包含错误关键字（如 `% Unknown command`），一旦发现立即终止并返回 `error`。
  - 单次调用支持 ≤5 条命令，服务端强制校验。
- 视图不自动切换：调用方需依据 `start_view`/`end_view` 显式下发导航命令。

### `server/mock_h3c_device.py`（测试用）
- 功能：假 H3C 设备 Telnet 服务器，模拟提示符状态机，用于无真实设备时的端到端验证。
- 用法：`python3 server/mock_h3c_device.py --port 2323 [--require-auth]`，配合 `NETMIKO_POOL_DEVICE_IP=127.0.0.1` 启动连接池服务。

### `server/test_pool_utils.py`（测试用）
- 功能：纯函数单元测试（视图解析、错误检测、密码脱敏、命令数上限、nav_path 跟踪与对账、历史读写/截断、描述符持久化与损坏容错）。
- 用法：`uv run server/test_pool_utils.py`。

## 典型工作流

1. 启动连接池服务：`uv run server/connection_pool_server.py`，并用 `python3 scripts/pool_client.py health` 确认。
2. 获取设备端口和认证信息。
3. 对每台设备执行 `device_init.py`，确认版本信息，及时发现连接或认证问题。
4. 根据配置需求，查阅 `references/CMD-help` 找到正确命令格式。
5. 分批次调用 `apply_config.py` 下发配置，每次不超过 5 条命令，依据返回的 `start_view`/`end_view` 判断并下发视图导航命令，校验返回结果。
6. 对关键配置执行验证命令，如 `display current-configuration | include ...`。
7. 遇到高危命令时，先取得人工授权，再放入脚本执行。
8. 任务结束用 `return` 导航回用户视图或 `pool_client.py disconnect` 断开，避免遗留视图状态。

## 贡献与扩展

- 如需增加新功能模块的命令参考，请在 `references/CMD-help` 下创建对应目录，并编写规范的 `.md` 文件。
- 若发现脚本缺陷或需要增强（如适配其他认证方式、自定义错误模式），可修改 `scripts/` 下的 Python 文件或 `server/connection_pool_server.py`，请保持 JSON 输出结构与检测逻辑一致。
- 欢迎提交 Issue 或 Pull Request 完善本仓库。

## 许可

本工具遵循 [MIT License](LICENSE)

---

通过这个标准化流程，您可以让 H3C 设备的日常配置变得安全、可追溯且易于自动化。如有疑问请参考 `SKILL.md` 中的详细规则。
