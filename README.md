# Netmiko H3C 自动化配置 Skill

本仓库是一个面向新华三（H3C）交换机、路由器等设备的自动化配置技能包，基于 Netmiko 和 Python 脚本实现。它最初为 AI 助手设计，但同样适合网络运维人员直接使用，能安全、高效地通过 Telnet 下发配置、初始化设备并验证版本信息。

## 功能特性

- **环境自检**：自动验证 Netmiko 库是否安装，给出明确指引。
- **设备初始化与版本查验**：一键关闭分屏、获取设备版本，返回结构化 JSON 结果。
- **安全的配置下发**：所有配置通过统一的 `apply_config.py` 脚本执行，内置视图切换、错误检测和超时保护，避免人工误操作。
- **高危操作二次确认**：对 `reboot`、`undo`、`reset` 等危险命令在执行前强制人工授权。
- **结构化命令参考库**：`references/CMD-help` 按功能模块（VLAN、OSPF、BGP、DHCP 等）整理了配置、调试、Probe 命令，并配有高频命令白名单，减少查阅成本。
- **密码保护**：支持交互式输入或环境变量传递密码，禁止明文写入命令行或文件。
- **多设备支持**：通过不同 Telnet 端口号区分设备，底层透明转发至对应 Console 串口。

## 目录结构

```
netmiko-h3c/
├── SKILL.md                      # 技能描述与执行规范（供 AI 或使用者参考）
├── README.md                     # 本文件
├── scripts/
│   ├── device_init.py            # 设备初始化与版本查询脚本
│   └── apply_config.py           # 配置下发通用脚本
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

- Python 3.6+
- Netmiko 库：`pip install netmiko`
- 设备侧需开启 Telnet 服务，并可通过 `192.168.56.1` 的特定端口访问（底层代理负责将 TCP 流量转发至真实 Console 口）

## 快速开始

### 1. 检查 Netmiko 环境
```bash
python3 -c "import netmiko; print(netmiko.__version__)"
```
若打印版本号则环境就绪，否则请执行 `pip install netmiko`。

### 2. 设备初始化与版本查验
使用 `scripts/device_init.py` 连接设备，自动关闭分屏并获取版本。

- 无认证设备：
  ```bash
  python3 scripts/device_init.py <端口号>
  ```
- 有认证设备：
  ```bash
  python3 scripts/device_init.py <端口号> <用户名> <密码>
  ```
  注意：密码不会记录在命令历史中，建议通过交互式输入或环境变量提供。

脚本输出示例：
```json
{"status": "success", "output": "H3C Comware Software, Version 7.1.064, Release 9660P39 ..."}
```
若 `status` 为 `error`，根据 `output` 中的错误信息排查。

### 3. 下发配置
所有配置任务（VLAN 创建、接口设置、路由协议等）均通过 `scripts/apply_config.py` 执行。脚本会自动处理视图切换、关闭分屏并检查命令错误。

- 无认证设备：
  ```bash
  python3 scripts/apply_config.py <端口号> "vlan 100" "name test_vlan"
  ```
- 有认证设备（交互输入密码）：
  ```bash
  python3 scripts/apply_config.py <端口号> "vlan 100" --user admin
  ```
- 有认证设备（通过环境变量）：
  ```bash
  export MY_SECRET='your_password'
  python3 scripts/apply_config.py <端口号> "vlan 100" --user admin --password-env MY_SECRET
  ```

> **重要限制**：单次调用最多支持 5 条命令，若需执行更多命令请分批次调用，且保证上一批次成功后再继续。

输出为 JSON：
```json
{"status": "success", "output": "..."}
```
若 `status` 为 `error`，说明命令执行过程中出现错误（如 `% Unknown command`），请停止后续操作，检查命令或联系用户。

## 命令参考文档

执行任何配置前，请先查阅 `references/CMD-help` 目录下对应的功能模块。例如需要添加 VLAN：
```bash
grep -rl "vlan" references/CMD-help/ | grep -i config
```
然后读取匹配的 `.md` 文件获取精确的命令格式。

**例外**：`references/high-frequency-commands.md` 中列出的命令已确认为通用 H3C 语法，可直接使用，无需查阅文档。

若在文档中未找到对应命令，但可确定是 H3C 标准语法，请在执行前明确告知用户“未找到对应文档，将按通用语法执行”并展示具体命令，获得确认后继续。

## 连接与端口说明

所有设备统一通过地址 `192.168.56.1` 访问，不同设备使用不同端口号区分。底层黑盒代理会将指定端口的 TCP Telnet 连接透明转发到对应网络设备的 Console 串口。实际使用时请先确认每台设备映射的端口号。

## 安全与高危操作

- **密码保护**：严禁在命令行、脚本或任何持久化文件中明文写入密码。强烈建议使用 `--password-env` 或脚本交互提示输入。
- **高危命令二次确认**：对于 `reboot`、`undo` 清空大段配置、`reset`、`erase` 等可能破坏业务或触发 `[Y/N]` 交互的命令，**必须**在执行前获得用户明确的授权。脚本不会替您回答任何确认提示，未经允许请勿继续执行。

## 脚本详细说明

### `device_init.py`
- 功能：连接设备，执行 `screen-length disable`，收集设备版本信息（`display version`），随后断开连接。
- 适用场景：设备初始检查，每次运行后会话终止，配置任务需另行连接。

### `apply_config.py`
- 功能：建立 Telnet 会话，自动执行固定框架：`return` → `screen-length disable` → `system-view` → 用户命令 → `return`。
- 特点：
  - 使用 `send_command_timing` 不依赖提示符，可适应任意嵌套子视图。
  - 自动检测每一条命令的输出是否包含错误关键字（如 `% Unknown command`、`^ Error`），一旦发现立即终止并返回 `error`。
  - 所有超时设置 ≤10 秒。
  - 单次调用支持 ≤5 条命令，需连续在子视图下执行的多条命令应放在同一调用中（视图状态会在调用内保持）。
- 注意：该脚本每次调用结束后 Telnet 连接即断开，下一次调用将重新连接并重新进入系统视图，因此不要依赖跨调用的视图保持。

## 典型工作流

1. 环境检查：确认 Netmiko 可用。
2. 获取设备端口和认证信息。
3. 对每台设备执行 `device_init.py`，确认版本信息，及时发现连接或认证问题。
4. 根据配置需求，查阅 `references/CMD-help` 找到正确命令格式。
5. 分批次调用 `apply_config.py` 下发配置，每次不超过 5 条命令，并校验返回结果。
6. 对关键配置执行验证命令，如 `display current-configuration | include ...`。
7. 遇到高危命令时，先取得人工授权，再放入脚本执行。

## 贡献与扩展

- 如需增加新功能模块的命令参考，请在 `references/CMD-help` 下创建对应目录，并编写规范的 `.md` 文件。
- 若发现脚本缺陷或需要增强（如适配其他认证方式、自定义错误模式），可修改 `scripts/` 下的 Python 文件，请保持 JSON 输出结构与检测逻辑一致。
- 欢迎提交 Issue 或 Pull Request 完善本仓库。

## 许可

本工具遵循 [MIT License](LICENSE)

---

通过这个标准化流程，您可以让 H3C 设备的日常配置变得安全、可追溯且易于自动化。如有疑问请参考 `SKILL.md` 中的详细规则。
