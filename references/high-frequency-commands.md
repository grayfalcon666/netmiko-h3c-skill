# H3C 高频操作白名单

以下命令可直接按通用 H3C 语法执行，无需查阅 CMD-help 文档。所有命令中的 `<参数>` 需根据实际环境替换。

## 系统与视图管理
- `sysname <名称>`
- `system-view`
- `quit`
- `return`
- `screen-length disable`
- `save force`

## 基本信息查看
- `display version`
- `display device`
- `display cpu-usage`
- `display memory`
- `display logbuffer`
- `display current-configuration`
- `display current-configuration interface <接口名>`
- `display current-configuration vlan <VLAN编号>`
- `display this`
- `display diagnostic-information`

## 接口基础配置与查看
- `interface <接口名>`
- `description <描述文本>`
- `ip address <IP地址> <掩码>`
- `undo shutdown`
- `display interface <接口名>`
- `display ip interface brief`
- `display interface brief`
- `display link-aggregation summary`
- `display link-aggregation verbose`

## VLAN 与端口类型
- `vlan <VLAN编号>`
- `display vlan`
- `display vlan brief`
- `port link-type access`
- `port link-type trunk`
- `port link-type hybrid`
- `port access vlan <VLAN编号>`
- `port trunk permit vlan <VLAN列表>`
- `port trunk pvid vlan <VLAN编号>`
- `port hybrid vlan <VLAN列表> tagged`
- `port hybrid vlan <VLAN列表> untagged`
- `port hybrid pvid vlan <VLAN编号>`

## 生成树协议 (STP)
- `display stp brief`
- `display stp interface <接口名>`
- `stp global enable`
- `stp mode {stp|rstp|mstp}`

## 链路聚合
- `interface Bridge-Aggregation <聚合组编号>`
- `port link-aggregation group <聚合组编号>`

## 路由协议（IPv4）
- `display ip routing-table`
- `display ospf brief`
- `display bgp summary`
- `ospf <进程号> router-id <路由器ID>`
- `bgp <AS号>`
- `rip <进程号>`

## ACL 与包过滤
- `acl advanced <ACL编号>`
- `acl basic <ACL编号>`
- `display acl all`

## 诊断与调试
- `ping <目标地址>`
- `tracert <目标地址>`
- `reset counters interface <接口名>` *(需注意该命令可能清空统计计数器，如用户未明确禁止可执行)*
