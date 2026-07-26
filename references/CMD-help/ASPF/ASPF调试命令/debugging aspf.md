
**ASPF \-- ASPF调试命令 \-- debugging aspf**

------------------------------------------------------------------------

【命令】

**[debugging aspf**[ { **all** \| **event** \| **packet** [ **acl** *acl-number* ] }]]

**[undo debugging aspf **[{ **all** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有ASPF调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[acl** *acl-number*]：表示仅输出匹配指定ACL规则的报文的ASPF会话的报文调试信息。其中，*acl-number*表示ACL的编号，取值范围为2000～3999。若不指定该参数，则表示输出所有会话的ASPF报文调试信息。

【描述】

**[debugging** **aspf**]命令用来打开ASPF调试信息开关。**undo** **debugging** **aspf**命令用来关闭ASPF调试信息开关。

缺省情况下，ASPF调试信息开关处于关闭状态。

表1-1 debugging aspf event命令输出信息描述表

字段

描述

Received an active event for interface *interface-type interface-num*.

ASPF收到一个接口激活事件通知

Received a deactive event for *interface-type interface-num*.

ASPF收到一个接口去激活事件通知

Received a deleting event for interface *interface-type interface-num*.

ASPF收到一个接口删除事件通知

表1-2 debugging aspf packet命令输出信息描述表

字段

描述

Interface

处理报文的接口名称

Direction

报文方向，取值为INBOUND和OUTBOUND

Src-Zone=*source-zone-name*

源安全域名称

当报文匹配上可匹配任意源安全域的域间实例时，源安全域名称后会附加显示(matched=Any)信息

Dst-Zone=*destination-zone-name*

目的安全域名称

当报文匹配上可匹配任意目的安全域的域间实例时，目的安全域名称后会附加显示(matched=Any)信息

If-In=*inbound-interface-name*(*ifIndexIn*)

入接口名称（入接口索引号）

If-Out=*outbound-interface-name*(i*fIndexOut*)

出接口名称（出接口索引号）

VLAN-In

入接口所属VLAN ID，该字段仅在入接口工作在二层模式时可见

VLAN-Out

出接口所属VLAN ID，该字段仅在出接口工作在二层模式时可见

Src-IP=*source-ip-address*

报文的源IP地址

Dst-IP=*destination-ip-address*

报文的目的IP地址

VPN-Instance=*vpn-instance-name*

报文所属的MPLS L3VPN实例

Src-Port=*source-port-number*

报文的源端口

Dst-Port=*destination-port-number*

报文的目的端口

Protocol=*protocol*(*number*)

报文的四层协议名（协议号）

The packet of no session was dropped by ASPF, because the ICMP error checking failed.

报文没有匹配任何会话，因为没有通过ASPF的ICMP差错报文检查，被ASPF丢弃

The packet of no session was dropped by ASPF, because the TCP SYN checking failed.

报文没有匹配任何会话，因为没有通过ASPF的TCP SYN检查，被ASPF丢弃

The first packet was dropped by ASPF, because the TCP SYN checking failed.

会话首报文没有通过ASPF的TCP SYN检查，被ASPF丢弃

The non-first packet of child session was dropped by ASPF for invalid status.

子会话后续报文由于状态机非法，被ASPF丢弃

The non-first packet was dropped by ASPF for invalid status.

会话后续报文由于状态机非法，被ASPF丢弃

The first packet of child session was set an ALG flag by ASPF.

子会话首报文被设置需要进行ALG处理标记

The gtp packet was dropped by ASPF.

GTP报文在ALG处理中没有通过检查被ASPF丢弃

The first packet was dropped by ASPF for nonexistent zone-pair.

首报文因域间实例不存在被ASPF丢弃

The first packet of child session was dropped by ASPF, because the TCP SYN checking failed.

子会话首报文没有通过ASPF的TCP SYN检查，被ASPF丢弃

The non-first packet of child session was dropped by ASPF for nonexistent zone pair.

子会话非首报文因域间实例不存在被ASPF丢弃

The first packet of child session was dropped by ASPF for nonexistent zone pair.

子会话首报文因域间实例不存在被ASPF丢弃

The non-first packet was dropped by ASPF for nonexistent zone pair.

非首报文因域间实例不存在被ASPF丢弃

The packet that matches no session was dropped by ASPF for nonexistent zone pair.

没有匹配任何会话的报文因域间实例不存在被ASPF丢弃

The non-first packet was dropped because of config changes.

非首报文由于配置变更被丢弃

The non-first packet of child session was dropped by packet filter or object-policy.

子会话非首报文被packet filter或object-policy丢弃

The first packet of child session was dropped by packet filter or object-policy.

子会话首报文被packet filter或object-policy丢弃

The non-first packet was dropped by packet filter or object-policy.

非首报文被packet filter或object-policy丢弃

The first packet was dropped by packet filter or object-policy.

首报文被packet filter或object-policy丢弃

The packet that matches no session was dropped by packet filter or object-policy.

报文因没有匹配任何会话被packet filter或 object-policy丢弃

【举例】

\# 在设备上配置ASPF策略，在接口上应用ASPF策略，并且打开ASPF报文调试信息开关，当有报文被ASPF丢弃时，打印如下调试信息。

\<Sysname\> debugging aspf packet

\*Aut 28 12:09:44:309 2011 Sysname ASPF/7/PACKET: -MDC=1; The packet of no session was dropped by ASPF, because the TCP SYN checking failed. Interface=GigabitEthernet1/0/2, Diretion=INBOUND; Packet Info: Src-IP=1.1.1.1, Dst-IP=1.1.1.2, VPN-Instance=none, Src-Port=12345, Dst-Port=21, Protocol=tcp（6）.

*// 报文没有匹配任何会话，通过PFILTER检查，但没有通过ASPF的TCP SYN检查，因此被丢弃。该报文来自接口GigabitEthernet1/0/2的入方向，源IP地址为1.1.1.1，目的IP地址为1.1.1.2，不属于属于公网，源端口号为12345，目的端口号为21，协议类型为TCP*

\# 在设备上配置ASPF策略，在域间应用ASPF策略，并且打开ASPF报文调试信息开关，当有报文被ASPF丢弃时，打印如下调试信息。

\<Sysname\> debugging aspf packet

\*Aut 28 12:09:44:309 2011 Sysname ASPF/7/PACKET: -MDC=1; The first packet was dropped by ASPF, because the TCP SYN checking failed. Src-Zone=Zone1, Dst-Zone=Zone2; If-In=Ten-GigabitEthernet7/0/17(471), If-Out=Ten-GigabitEthernet7/0/18(472); Packet Info: Src-IP=1.1.1.1, Dst-IP=1.1.1.2, VPN-Instance=none, Src-Port=12345, Dst-Port=21, Protocol=tcp（6）.

*[//*]*报文没有匹配任何会话，通过PFILTER检查，但没有通过ASPF的TCP SYN检查，因此被丢弃。该报文自安全域Zone1发往安全域Zone2，人接口为Ten-GigabitEthernet7/0/17，出接口为Ten-GigabitEthernet7/0/18，源IP地址为1.1.1.1，目的IP地址为1.1.1.2，属于公网，源端口号为12345，目的端口号为21，协议类型为TCP*

\# 在设备上配置ASPF策略，在接口上应用ASPF策略，并且打开ASPF事件调试开关时，当有接口事件上报时，打印如下调试信息。

\<Sysname\> debugging aspf event

\*Aut 28 12:13:44:290 2011 Sysname ASPF/7/EVENT: -MDC=1; Received an active event for interface GigabitEthernet1/0/2.

*[// ASPF*]*收到一个接口激活事件通知*
