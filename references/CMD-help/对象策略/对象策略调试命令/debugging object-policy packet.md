
**对象策略 \-- 对象策略调试命令 \-- debugging object-policy packet**

------------------------------------------------------------------------

【命令】

**[debugging**[ **object-policy** **packet** { **ip** \| **ipv6** } [ **acl** *acl-number* ]]]

**[undo**[ **debugging** **object-policy** **packet** { **ip** \| **ipv6** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip**]：表示IPv4报文的调试信息开关。

**[ipv6**]：表示IPv6报文的调试信息开关。

*[acl-number*]：表示输出指定编号ACL匹配报文的调试信息。若未指定，则输出指定类型所有报文的调试信息。*acl-number*表示ACL的编号，取值范围如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：若指定**ip**关键字，则表示IPv4基本ACL，若指定**ipv6**关键字，则表示IPv6基本ACL。

·3000～3999：若指定**ip**关键字，则表示IPv4高级ACL，若指定**ipv6**关键字，则表示IPv6高级ACL。

【描述】

**[debugging** **object-policy packet**]命令用来打开对象策略报文调试信息开关。**undo** **debugging** **object-policy packet**命令用来关闭对象策略报文调试信息开关。

缺省情况下，对象策略报文调试信息开关处于关闭状态。

表1-1 debugging object-policy packet命令输出信息描述表

字段

描述

The packet is permitted

允许报文通过

The packet is denied

丢弃报文

Src-Zone=*source-zone-name*(matched=Any)

报文的源安全域名称

当报文匹配上可匹配任意源安全域的域间实例时，此处会附加显示(matched=Any)信息

Dst-Zone=*destination-zone-name*(matched=Any)

报文的目的安全域名称

当报文匹配上可匹配任意目的安全域的域间实例时，此处会附加显示(matched=Any)信息

If-In=*inbound-interface-name*(*ifIndexIn*)

入接口名称（入接口索引号）

If-Out=*outbound-interface-name*(*ifIndexOut*)

出接口名称（出接口索引号）

VLAN-In

入VLAN ID，该字段仅在报文转发相关接口工作在二层模式时可见

VLAN-Out

出VLAN ID，该字段仅在报文转发相关接口工作在二层模式时可见

Packet Info

报文信息（该信息来自报文本身）

Match Info

匹配信息（该信息由设备提取自相关的会话表项，用于匹配包过滤策略）

Src-IP=*source-ip-address*

报文源IP地址

Dst-IP=*destination-ip-address*

报文目的IP地址

VPN-Instance=*VPN-instance-name*

报文所属的MPLS L3VPN索引名称

Src-Port=*source-port-number*

报文源端口

Dst-Port=*destination-port-number*

报文目的端口

Protocol=*protocol*(*number*)

报文的协议类型（协议号）

ObjectPolicy=*policy-name*

对象策略名称

【举例】

·根据报文信息输出debug信息

\# 打开OBJP报文调试信息开关，使用基本ACL 2000进行过滤

\<Sysname\> debugging object-policy packet ip acl 2000

\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Src-Zone=DMZ, Dst-Zone=TRUST; If-In=Ten-GigabitEthernet7/0/17(472), If-Out=Ten-GigabitEthernet7/0/18(473); Packet Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.

*// 允许通过的ipv4报文信息*

\# 打开OBJP报文调试信息开关，使用IPv6基本ACL 2000进行过滤

\<Sysname\> debugging object-policy packet ipv6 acl 2000

\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Src-Zone=DMZ, Dst-Zone=TRUST; If-In=Ten-GigabitEthernet7/0/17(472), If-Out=Ten-GigabitEthernet7/0/18(473); Packet Info: SrcIP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.

*// 被丢弃的ipv6报文*

·根据数据包匹配信息输出debug信息

\# 打开OBJP报文调试信息开关，使用基本ACL 2000进行过滤

\<Sysname\> debugging object-policy packet ip acl 2000

\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Src-Zone= DMZ, Dst-Zone=TRUST; Match Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.

*// 允许通过的ipv4报文信息*

\# 打开OBJP报文调试信息开关，使用IPv6基本ACL 2000进行过滤

\<Sysname\> debugging object-policy packet ipv6 acl 2000

\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Src-Zone= DMZ, Dst-Zone= TRUST; Match Info: Src-IP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ObjectPolicy=policy1.

*// 被丢弃的ipv6报文*

