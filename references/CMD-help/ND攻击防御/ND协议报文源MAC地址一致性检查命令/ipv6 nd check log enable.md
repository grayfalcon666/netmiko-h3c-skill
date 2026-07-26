
**ND攻击防御 \-- ND协议报文源MAC地址一致性检查命令 \-- ipv6 nd check log enable**

------------------------------------------------------------------------

**[ipv6 nd check log enable**]命令开启ND日志信息功能。

**[undo ipv6 nd check log enable**]命令关闭ND日志信息功能。

【命令】

**[ipv6 nd check log enable**]

**[undo ipv6 nd check log enable**]

【缺省情况】

设备ND日志信息功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

设备生成的ND日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。

为了防止设备输出过多的ND日志信息，一般情况下建议不要打开此功能。

【举例】

\# 开启ND日志信息功能。

\<Sysname\> system-view

Sysname ipv6 nd check log enable

**ND攻击防御 \-- ND协议报文源MAC地址一致性检查命令 \-- ipv6 nd mac-check enable**

------------------------------------------------------------------------

**[ipv6 nd mac-check enable**]命令用来开启ND协议报文源MAC地址一致性检查功能。

**[undo ipv6 nd mac-check enable**]命令用来关闭ND协议报文源MAC地址一致性检查功能。

【命令】

**[ipv6 nd mac-check enable**]

**[undo ipv6 nd mac-check enable**]

【缺省情况】

ND协议报文源MAC地址一致性检查功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

网关设备开启该功能后，会对接收到的ND协议报文进行检查，如果ND报文中的源MAC地址和以太网数据帧首部的源MAC地址，则丢弃该报文。

【举例】

\# 开启ND协议报文源MAC地址一致性检查功能。

\<Sysname\> syatem-view

Sysname ipv6 nd mac-check enable

**ND攻击防御 \-- ND Detection配置命令 \-- display ipv6 nd detection statistics**

------------------------------------------------------------------------

**[display ipv6 nd detection statistics**]命令用来显示ND Detection进行用户合法性检查时丢弃ND报文的统计信息。

【命令】

**[display ipv6 nd detection statistics** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口ND Detection进行用户合法性检查时丢弃ND报文的统计信息。*interface-type interface-number*表示接口类型和接口编号。

【举例】

\# 显示ND Detection进行用户合法性检查时丢弃报文的统计信息。

\<Sysname\> display ipv6 nd detection statistics

ND packets dropped by ND detection:

Interface         Packets dropped

GE1/0/1           78

GE1/0/2           0

GE1/0/3           0

GE1/0/4           0

表1-1 display ipv6 nd detection statistics命令显示信息描述表

字段

描述

ND packets dropped by ND detection：

根据ND Detection丢弃的ND报文

Interface

ND报文入接口

Packets dropped

丢弃的报文数目

**ND攻击防御 \-- ND Detection配置命令 \-- ipv6 nd detection enable**

------------------------------------------------------------------------

**[ipv6 nd detection enable**]命令用来开启ND Detection功能，即对ND报文进行合法性检查。

**[undo ipv6 nd detection enable**]命令用来关闭ND Detection功能。

【命令】

**[ipv6 nd detection enable**]

**[undo ipv6 nd detection enable**]

【缺省情况】

ND Detection功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在VLAN 10内开启ND Detection功能。

\<Sysname\> system-view

Sysname vlan 10

Sysname-vlan10 ipv6 nd detection enable

**ND攻击防御 \-- ND Detection配置命令 \-- ipv6 nd detection trust**

------------------------------------------------------------------------

**[ipv6 nd detection trust**]命令用来配置端口为ND信任端口。

**[undo ipv6 nd detection trust**]命令用来配置端口为ND非信任端口。

【命令】

**[ipv6 nd detection trust**]

**[undo ipv6 nd detection trust**]

【缺省情况】

端口为ND非信任端口。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1为ND信任端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd detection trust

\# 配置二层聚合接口Bridge-Aggregation1为ND信任端口。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 ipv6 nd detection trust

**ND攻击防御 \-- ND Detection配置命令 \-- reset ipv6 nd detection statistics**

------------------------------------------------------------------------

**[reset ipv6 nd detection statistics**]命令用来清除ND Detection的统计信息。

【命令】

**[reset ipv6 nd detection statistics** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：表示清除指定接口的统计信息。*interface-type interface-number*表示接口类型和接口编号。

【举例】

\# 清除所有的ND Detection统计信息。

\<Sysname\> reset ipv6 nd detection statistics
