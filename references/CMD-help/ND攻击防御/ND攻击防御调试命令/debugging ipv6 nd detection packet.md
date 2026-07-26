
**ND攻击防御 \-- ND攻击防御调试命令 \-- debugging ipv6 nd detection packet**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 nd detection packet**]

**[undo debugging ipv6 nd detection packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ipv6 nd detection packet**]命令用来打开ND Detection报文调试信息开关。**undo debugging ipv6 nd detection packet**命令用来关闭ND Detection报文调试信息开关。

缺省情况下，ND Detection报文调试信息开关处于关闭状态。

表1-1 debugging ipv6 nd detection packet命令输出信息描述表

字段

描述

Received *packet-type* packet on untrust port *port-name*, no matching entry, dropped it.

从非信任口*port-name*接收到*packet-type*报文，由于没有表项匹配，故丢弃。其中*port-name*可以是二层以太口或者二层聚合口。*Packet-type*是：

lRS：Router Solicitation报文

lNS：Neighbor Solicitation报文

·NA：Neighbor Advertisement报文

Received *packet-type* packet on untrust port *port-name*, dropped it.

从非信任口port-name接收到packet-type报文，丢弃。其中*port-name*可以是二层以太网端口或二层聚合口，*packet-type*是：

lRR：ICMPv6 redirect报文

·RA：Router Advertisement报文

【举例】

\# 打开ND Detection报文调试信息开关，并收到ND报文。

\<Sysname\> debugging ipv6 nd detection packet

*// 在聚合口BAGG1上收到NA报文，由于未找到匹配表项而丢弃*

\*Jul 25 14:10:50:414 2014 H3C ND/7/ND DETECTION PACKET: -MDC=1;

 Received NA packet on untrust port BAGG1, no matching entry, dropped it.
