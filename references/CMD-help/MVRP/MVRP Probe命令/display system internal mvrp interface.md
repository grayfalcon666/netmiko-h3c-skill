
**MVRP \-- MVRP Probe命令 \-- display system internal mvrp interface**

------------------------------------------------------------------------

**[display system internal mvrp interface**]命令用来显示端口在指定VLAN下的MVRP运行信息。

【命令】

**[display system internal mvrp interface ***interface-type interface-number*** vlan ***vlan-id*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：显示指定端口的MVRP运行信息，*interface-type interface-number*表示端口类型和端口编号。

**[vlan*** vlan-id*]：显示端口在指定VLAN内的MVRP运行信息。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。

**MVRP \-- MVRP Probe命令 \-- display system internal mvrp map-count**

------------------------------------------------------------------------

**[display system internal mvrp map-count**]命令用来显示指定VLAN的传播计数信息。

【命令】

**[display system internal mvrp map-count vlan ***vlan-id*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan-id*]：显示指定VLAN的传播计数信息。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。

【使用指导】

该命令显示设备通过MVRP在指定VLAN注册的允许传播的接口个数，表明当前有多少STP状态为Forwarding的接口注册了该VLAN。

