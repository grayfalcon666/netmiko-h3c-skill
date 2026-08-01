<!-- CMD-INDEX
  debugging acl                       | 用户视图             | L6
  debugging packet-filter packet      | 用户视图             | L426
-->

**ACL \-- ACL调试命令 \-- debugging acl**

------------------------------------------------------------------------

【命令】

**[debugging**[ **acl** { **all** \| **error** \| **event** \| **match** }]]

**[undo**[ **debugging** **acl** { **all** \| **error** \| **event** \| **match** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示ACL所有调试信息开关。

**[error**]：表示ACL错误调试信息开关。

**[event**]：表示ACL事件调试信息开关。

**[match**]：表示ACL匹配调试信息开关。

【描述】

**[debugging** **acl**]命令用来打开ACL调试信息开关。**undo** **debugging** **acl**命令用来关闭ACL调试信息开关。

缺省情况下，ACL调试信息开关处于关闭状态。

表1-1 debugging acl error命令输出信息描述表

字段

描述

Message error on daemon.

守护进程消息错误

Message head error on daemon.

守护进程消息头错误

Failed to send add-group message to other boards.

发送添加组消息到其它板失败

Failed to send set-match-order message to other boards.

发送设置匹配顺序消息到其它板失败

Failed to send delete-group message to other boards.

发送删除组消息到其它板失败

Failed to send copy-group message to other boards.

发送拷贝组消息到其它板失败

Failed to send set-step message to other boards.

发送设置步长消息到其它板失败

Failed to send add-description message to other boards.

发送添加描述信息消息到其它板失败

Failed to send delete-description message to other boards.

发送删除描述信息消息到其它板失败

Failed to send reset-group message to other boards.

发送重置组消息到其它板失败

Failed to send add-rule message to other boards.

发送添加规则消息到其它板失败

Failed to send modify-rule message to other boards.

发送修改规则消息到其它板失败

Failed to send delete-rule message to other boards.

发送删除规则消息到其它板失败

Failed to send add-comment message to other boards.

发送添加注释消息到其它板失败

Failed to send delete-comment message to other boards.

发送删除注释消息到其它板失败

Failed to send open-debugging-switch message to other boards.

发送打开调试信息开关消息到其它板失败

Failed to send close-debugging-switch message to other boards.

发送关闭调试信息开关消息到其它板失败

Failed to send set-logging message to other boards.

发送设置报文过滤日志的生成与发送周期消息到其它板失败

Failed to send time-range message to other boards.

发送时间段消息到其它板失败

Failed to send L3VPN message to other boards.

发送L3VPN事件消息到其它板失败

Failed to get rule match statistics from other boards.

从其它板获取规则匹配统计信息失败

Failed to send copy-rule message to other boards

发送拷贝规则消息到其他板失败

表1-2 debugging acl event命令输出信息描述表

字段

描述

Received add-group message.

收到添加组消息

Received delete-group message.

收到删除组消息

Received set-step message.

收到设置步长消息

Received copy-group message.

收到拷贝组消息

Received reset-group message.

收到重置组消息

Received add-description message.

收到添加描述消息

Received delete-description message.

收到删除描述消息

Received do-rule message.

收到配置规则消息

Received undo-rule message.

收到取消配置规则消息

Received add-rule message.

收到添加规则消息

Received modify-rule message.

收到修改规则消息

Received delete-rule message.

收到删除规则消息

Received add-comment message.

收到添加注释消息

Received delete-comment message.

收到删除注释消息

Received open-debugging-switch message.

收到打开调试信息开关消息

Received close-debugging-switch message.

收到关闭调试信息开关消息

Received set-logging message.

收到设置报文过滤日志的生成与发送周期消息

Received time-range message.

收到时间段变化消息

Received L3VPN message.

收到L3VPN事件消息

The main daemon begins to send batch info to backup board.

主进程开始向备板发送批量备份数据

The backup daemon is upgraded.

备进程已升级

The main daemon is stopped.

主进程已停止

The main daemon is degraded.

主进程已降级

Received a time-range *time-range* event.

收到名为*time-range*的时间段事件

Received an L3VPN event.

收到L3VPN事件

表1-3 debugging acl match命令输出信息描述表

字段

描述

ACL *num* *ruleID* does not exist when filtering packet info.

过滤报文信息时，ACL *num* *ruleID*不存在

ACL *num* *ruleID* does not exist when filtering packet buffer.

过滤报文时，ACL *num* *ruleID*不存在

No match for fragment in basic rule *ruleID*.

基本规则*ruleID*中的分片信息项不匹配

No match for VPN instance in basic rule *ruleID*.

基本规则*ruleID*中的L3VPN索引项不匹配

No match for source address in basic rule *ruleID*.

基本规则*ruleID*中的源地址项不匹配

No match for fragment in advanced rule *ruleID*.

高级规则*ruleID*中的分片信息项不匹配

No match for source address in advanced rule *ruleID*.

高级规则*ruleID*中的源地址项不匹配

No match for destination address in advanced rule *ruleID*.

高级规则*ruleID*中的目的地址项不匹配

No match for protocol in advanced rule *ruleID*.

高级规则*ruleID*中的协议类型项不匹配

No match for ToS in advanced rule *ruleID*.

高级规则*ruleID*中的服务类型项不匹配

No match for VPN instance in advanced rule *ruleID*.

高级规则*ruleID*中的L3VPN索引项不匹配

No match for ICMP type in advanced rule *ruleID*.

高级规则*ruleID*中的ICMP消息类型项不匹配

No match for ICMP code in advanced rule *ruleID*.

高级规则*ruleID*中的ICMP消息码项不匹配

No match for source port in advanced rule *ruleID*.

高级规则*ruleID*中的源端口项不匹配

No match for destination port in advanced rule *ruleID*.

高级规则*ruleID*中的目的端口项不匹配

No match for TCP flag in advanced rule *ruleID*.

高级规则*ruleID*中的TCP标志项不匹配

No match for source MAC address in MAC rule *ruleID*.

二层规则*ruleID*中的源MAC地址项不匹配

No match for desination MAC address in MAC rule *ruleID*.

二层规则*ruleID*中的目的MAC地址项不匹配

No match for CoS in MAC rule *ruleID*.

二层规则*ruleID*中的CoS项不匹配

No match for frame type in MAC rule *ruleID*.

二层规则*ruleID*中的帧类型项不匹配

No match for LSAP type in MAC rule *ruleID*.

二层规则*ruleID*中的LSAP类型项不匹配

No match for fragment in IPv6 basic rule *ruleID*.

IPv6基本规则*ruleID*中的分片信息项不匹配

No match for VPN instance in IPv6 basic rule *ruleID*.

IPv6基本规则*ruleID*中的L3VPN索引项不匹配

No match for routing type in IPv6 basic rule *ruleID*.

IPv6基本规则*ruleID*中的路由头类型项不匹配

No match for source address in IPv6 basic rule *ruleID*.

IPv6基本规则*ruleID*中的源地址项不匹配

No match for fragment in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的分片信息项不匹配

No match for VPN instance in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的L3VPN索引项不匹配

No match for routing type in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的路由头类型项不匹配

No match for source address in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的源地址项不匹配

No match for destination address in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的目的地址项不匹配

No match for protocol in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的协议类型项不匹配

No match for DSCP in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的DSCP项不匹配

No match for flow-label in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的流标签项不匹配

No match for ICMP type in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的ICMP消息类型项不匹配

No match for ICMP code in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的ICMP消息码项不匹配

No match for source port in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的源端口项不匹配

No match for destination port in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的目的端口项不匹配

No match for TCP flag in IPv6 advanced rule *ruleID*.

IPv6高级规则*ruleID*中的TCP标志项不匹配

【举例】

\# 配置IPv4基本ACL 2000，并打开ACL错误调试信息开关。

\<Sysname\> debugging acl error

\*Mar 22 10:12:25:381 2011 Sysname ACL/7/Error: -MDC=1; Failed to send add-group message to other boards.

*// 发送添加组消息到其它板失败*

\# 配置IPv4基本ACL 2000，并打开ACL事件调试信息开关。

\<Sysname\> debugging acl event

\*Mar 22 10:12:20:380 2011 Sysname ACL/7/Event: -MDC=1; Received add-group message.

*// 收到添加组消息*

\# 配置IPv4基本ACL 2000，并打开ACL匹配调试信息开关。

\<Sysname\> debugging acl match

\*Mar 22 10:12:23:382 2011 Sysname ACL/7/Match: -MDC=1; No match for fragment in basic rule 2000.

*[//* *ACL* *2000*]*中的分片信息项不匹配*

**ACL \-- ACL调试命令 \-- debugging packet-filter packet**

------------------------------------------------------------------------

【命令】

**[debugging**[ **packet-filter** **packet** { **ip** \| **ipv6** } [ **acl** *acl-number* ]]]

**[undo**[ **debugging** **packet-filter** **packet** { **ip** \| **ipv6** }]]

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

**[debugging** **packet-filter packet**]命令用来打开包过滤报文调试信息开关。**undo** **debugging** **packet-filter packet**命令用来关闭包过滤报文调试信息开关。

缺省情况下，包过滤报文调试信息开关处于关闭状态。

表1-4 debugging packet-filter packet命令输出信息描述表

字段

描述

The packet is permitted.

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

If-Out=*outbound-interface-name*(i*fIndexOut*)

出接口名称（出接口索引号）

VLAN-In

入VLAN ID，该字段仅在报文转发相关接口工作在二层模式时可见

VLAN-Out

出VLAN ID，该字段仅在报文转发相关接口工作在二层模式时可见

Interface=*interface-name*

接口名称

Direction=*direction*

报文匹配上了*direction*方向的包过滤策略，*direction*取值为INBOUND和OUTBOUND

Packet Info

报文信息（该信息来自报文本身）

Match Info

匹配信息（该信息由设备提取自相关的会话表项，用于匹配包过滤策略）

Src-IP=*source-ip-address*

报文源IP地址

Dst-IP=*destination-ip-address*

报文目的IP地址

VPN-Instance=*VPN-instance-name*

报文所属的MPLS L3VPN名称

Src-Port=*source-port-number*

报文源端口

Dst-Port=*destination-port-number*

报文目的端口

Protocol=*protocol*(*number*)

报文的协议类型（协议号）

ACL=*acl-number*

ACL编号

【举例】

·根据报文信息输出域间实例debug信息

\# 打开包过滤报文调试信息开关，使用基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ip acl 2000

\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Src-Zone=DMZ, Dst-Zone=TRUST; If-In=Ten-GigabitEthernet7/0/17(472), If-Out=Ten-GigabitEthernet7/0/18(473); Packet Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=3000.

*// 允许通过的ipv4报文信息*

\# 打开包过滤报文调试信息开关，使用IPv6基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ipv6 acl 2000

\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Src-Zone=DMZ, Dst-Zone=TRUST; If-In=Ten-GigabitEthernet7/0/17(472), If-Out=Ten-GigabitEthernet7/0/18(473); Packet Info: Src-IP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=3000.

*// 被丢弃的ipv6报文*

·根据数据包匹配信息输出域间debug信息

\# 打开包过滤报文调试信息开关，使用基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ip acl 2000

\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Src-Zone=DMZ, Dst-Zone=TRUST; Match Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=3000.

*// 允许通过的ipv4报文信息*

\# 打开包过滤报文调试信息开关，使用IPv6基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ipv6 acl 2000

\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Src-Zone=DMZ, Dst-Zone=TRUST; Match Info: Src-IP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=3000.

*// 被丢弃的ipv6报文*

·根据报文信息输出接口debug信息

\# 打开包过滤报文调试信息开关，使用基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ip acl 2000

\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Interface=Ten-GigabitEthernet7/0/18, Direction=OUTBOUND; Packet Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=2000.

*// 允许通过的ipv4报文信息*

\# 打开包过滤报文调试信息开关，使用IPv6基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ipv6 acl 2000

\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Interface=Ten-GigabitEthernet7/0/18, Direction=OUTBOUND; Packet Info: Src-IP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=3000.

*// 被丢弃的ipv6报文*

·根据数据包匹配信息输出接口debug信息

\# 打开包过滤报文调试信息开关，使用基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ip acl 2000

\*Mar 22 10:12:25:381 2011 Sysname pflt/7/Event: -MDC=1; The packet is permitted. Interface=Ten-GigabitEthernet7/0/18, Direction=OUTBOUND; Match Info: Src-IP=1.1.1.1, Dst-IP=2.2.2.2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=3000.

*// 允许通过的ipv4报文信息*

\# 打开包过滤报文调试信息开关，使用IPv6基本ACL 2000进行过滤

\<Sysname\> debugging packet-filter packet ipv6 acl 2000

\*Mar 22 10:12:20:380 2011 Sysname pflt/7/Event: -MDC=1; The packet is denied. Interface=Ten-GigabitEthernet7/0/18, Direction=OUTBOUND; Match Info: Src-IP=1::1, Dst-IP=2::2, VPN-Instance=vpn1, Src-Port=1024, Dst-Port=1025, Protocol=tcp(6), ACL=3000.

*// 被丢弃的ipv6报文*

