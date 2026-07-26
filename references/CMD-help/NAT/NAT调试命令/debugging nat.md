
**NAT \-- NAT调试命令 \-- debugging nat**

------------------------------------------------------------------------

【命令】

**[debugging nat **[{ **event** \| **packet** [ **acl** *acl-number* ] }]]

**[undo debugging nat **[{ **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：表示事件调试信息开关。

**[packet**]： 表示报文调试信息开关。

**[acl** *acl-number*]：指定仅对与ACL匹配的报文输出报文调试信息。*acl-number*表示ACL编号，取值范围为2000～3999。

【描述】

**[debugging nat**]命令用来打开NAT通用调试信息开关。**undo debugging nat**命令用来关闭NAT通用调试信息开关。

缺省情况下，NAT通用调试信息开关处于关闭状态。

表1-1 debugging nat event命令输出信息描述表

字段

描述

Deleted NAT session entry for configuration sequence changed!

NAT配置序号变化，删除NAT会话表项

Deleted NAT session entry for out interface changed!

会话接口检查发现出接口变化，删除NAT会话表项

表1-2 debugging nat packet命令输出信息描述表

字段

描述

PACKET: (*interface-type interface-number-direction*)

报文信息：（接口名-报文方向）

Protocol: *protocol*

报文的协议类型

*[OrgSrcIP*: *OrgSrcPort* - *OrgDstIP*: *OrgDstPort* (VPN:    *OrgVpnIndex*) \-\-\-\-\--\>]

*[NewSrcIP*: *NewSrcPort* - *NewDstIP*: *NewDstPort* (VPN:    *NewVpnIndex*) ]

NAT转换前的报文原始五元组：

·*OrgSrcIP*：原始源IP地址

·*OrgSrcPort*：原始源端口号

·*OrgDstIP*：原始目的IP地址

·*OrgDstPort*：原始目的端口号

·*OrgVpnIndex*：原始报文所属的MPLS L3VPN索引

NAT转换后的报文新五元组：

·*NewSrcIP*：新源IP地址

·*NewSrcPort*：新源端口号

·*NewDstIP*：新目的IP地址

·*NewDstPort*：新目的端口号

·*New*V*pnIndex*：转换后报文所属的MPLS L3VPN索引

【举例】

\# 在启用了NAT功能的设备上打开NAT通用事件调试信息开关，有TCP报文通过该设备，此时会创建NAT会话。修改NAT配置，使得报文转换方式发生变化，如果上述TCP报文通过设备，则输出如下调试信息。

\<Sysname\> debugging nat event

\*Apr 20 15:13:01:182 2012 Sysname NAT/7/COMMON: -MDC=1;

 EVENT: Deleted NAT session entry for configuration sequence changed!

*// 因为NAT配置序号发生了变化，所以删除NAT会话表项*

\# 在启用了NAT功能的设备上打开NAT通用事件调试信息开关，有TCP报文通过该设备，此时会创建NAT会话。关闭原来的报文出接口，使报文从另一个接口发送出去，如果上述TCP报文通过设备，则输出如下调试信息。

\<Sysname\> debugging nat event{.TerminalDisplayChar}

\*Apr 20 15:13:01:184 2012 Sysname NAT/7/COMMON: -MDC=1;

 EVENT: Deleted NAT session entry for out interface changed!

*[// NAT*]*会话在做接口检查时发现出接口变化，删除NAT会话表项*

\# 在启用了NAT功能的设备上打开NAT通用报文调试信息开关，有ping报文通过该设备时输出如下调试信息。

\<Sysname\> debugging nat packet

\*Apr 20 15:13:01:178 2012 Sysname NAT/7/COMMON: -MDC=1;

 PACKET: (GigabitEthernet1/0/2-out) Protocol: ICMP

   192.168.1.100:    0 -       2.2.2.100:    0(VPN:    0) \-\-\-\-\--\>

       2.2.2.250:    0 -       2.2.2.100:    0(VPN:    0)

*// 在GigabitEthernet1/0/2出方向对一个ICMP报文进行了NAT转换（转换了源IP地址）*

\# 在启用了NAT功能的设备上打开NAT通用报文调试信息开关，有TCP报文通过该设备时输出如下调试信息。

\<Sysname\> debugging nat packet

\*Apr 20 15:13:01:180 2012 Sysname NAT/7/COMMON: -MDC=1;

PACKET: (GigabitEthernet1/0/2-out) Protocol: TCP

   192.168.1.100: 2776 -       2.2.2.100:   21(VPN:    0) \-\-\-\-\--\>

       2.2.2.254: 1024 -       2.2.2.100:   21(VPN:    0)

*// 在GigabitEthernet1/0/2出方向对一个TCP报文进行了NAT转换（转换了源IP地址+源端口号）*

**NAT \-- NAT调试命令 \-- debugging nat alg**

------------------------------------------------------------------------

【命令】

**[debugging nat alg **[{ **all** \| **event** \| **packet** [ **acl** *acl-number* ] }]]

**[undo debugging nat alg **[{ **all** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[acl** *acl-number*]：指定仅对与ACL匹配的报文输出报文调试信息。其中，*acl-number*表示ACL编号，取值范围为2000～3999。

【描述】

**[debugging nat alg**]命令用来打开NAT ALG调试信息开关。**undo debugging nat alg**命令用来关闭NAT ALG调试信息开关。

缺省情况下，NAT ALG调试信息开关处于关闭状态。

表1-3 debugging nat alg event命令输出信息描述表

字段

描述

EVENT: (*interface-type interface-num*) The payload of DNS packet with domain *domain-name* will be translated.

接口*interface-type interface-num*收到DNS报文，NAT要处理的DNS报文的域名为*domain-name*

表1-4 debugging nat alg packet命令输出信息描述表

字段

描述

PACKET: (*interface-type interface-num*) ALG payload was translated according to *trans-type*:

*[OrgIP/OrgPort*(VPN: *OrgVpnIndex*)\-\--\> *NewIP/NewPort*(VPN: *NewVpnIndex*)]

在接口*interface-type interface-num*上对报文载荷中的地址进行了NAT转换，转换类型为*trans-type*，包括以下取值：

·session table：根据会话表转换

·relation table(Local)：根据local类型的关联表的转换

·relation table(Global)：根据global类型的关联表的转换

·configuration：根据配置信息转换

NAT转换前的报文载荷信息：

·*OrgIP*：原始IP地址

·*OrgPort*：原始端口号

·*OrgVpnIndex*：原始报文所属的MPLS L3VPN索引

NAT转换后的报文载荷信息：

·*NewIP*：新IP地址

·*NewPort*：新端口号

·*NewVpnInde**x*：转换后报文所属的MPLS L3VPN索引

PACKET: (*interface-type interface-num*-*direction*) DNS *packet-type* packet was translated:

*[OrgIP*\-\--\> *NewIP*]

在接口*interface-type interface-num*的*direction*方向上对DNS报文进行了NAT转换，DNS报文类型为*packet-type*，包括以下取值：

·DNS Query

·DNS RRs

NAT转换前的报文载荷信息：

·*OrgIP*：原始IP地址

NAT转换后的报文载荷信息：

·*NewIP*：新IP地址

PACKET: (*interface-type interface-num*-*direction*) ICMP error payload was translated:

Pro: *protocol* *OrgIP*/*OrgPort*\-\--\> *NewIP*/*NewPort*

在接口*interface-type interface-num*的*direction*方向上对ICMP差错控制报文中的载荷进行了NAT转换

引发该ICMP报文的报文的协议类型：*protocol*

NAT转换前的报文载荷信息：

·*OrgIP*：原始IP地址

·*OrgPort*：原始端口号

NAT转换后的报文载荷信息：

·*NewIP*：新IP地址

·*NewPort*：新端口号

【举例】

\# 在配置了NAT和ALG功能的设备上打开NAT ALG事件调试信息开关，有FTP PORT报文通过设备时输出如下调试信息。

\<Sysname\> debugging nat alg event

\*Apr 20 15:33:02:122 2012 Sysname NAT/7/ALG: -MDC=1;

 EVENT: (GigabitEthernet1/0/2) The payload of DNS packet with domain www.xxxxx.com will be translated.

*// 接口GigabitEthernet1/0/2上收到DNS报文，其中的DNS域名www.xxxxx.com需要进行NAT转换*

\# 在配置了NAT和ALG功能的设备上打开NAT ALG报文调试信息开关，有FTP PORT报文通过设备时输出如下调试信息。

\<Sysname\> debugging nat alg packet

\*Apr 20 15:33:02:122 2012 Sysname NAT/7/ALG: -MDC=1;

 PACKET: (GigabitEthernet1/0/2) ALG payload was translated according to configuration:

    192.168.1.100/2787(VPN: 0) \-\--\> 2.2.2.254/10626(VPN: 0)

*// 在接口GigabitEthernet1/0/2对一个h225协议报文进行了NAT转换*

**NAT \-- NAT调试命令 \-- debugging nat config**

------------------------------------------------------------------------

【命令】

**[debugging nat config **[{ **all** \| **error** \| **event** }]]

**[undo debugging nat config **[{ **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging nat config**]命令用来打开NAT配置调试信息开关。**undo debugging nat config**命令用来关闭NAT配置调试信息开关。

缺省情况下，NAT配置调试信息开关处于关闭状态。

表1-5 debugging nat config命令输出信息描述表

字段

描述

EVENT: Received lipc message, message type: *type*.

收到lipc消息，消息类型为*type*

EVENT: Received ioctl message, message type: *type*.

收到ioctl消息，消息类型为*type*，包括以下取值：

·log enable：使能日志开关

·log disable：关闭日志开关

·log flow active：使能活跃流日志

·log flow deactive：关闭活跃流日志

·log flow begin：使能流创建日志

·log flow begin disable：关闭流创建日志

·log flow end：使能流结束日志

·log flow end disable：关闭流结束日志

·set all log configration：使能所有日志功能

·set alg：使能ALG

·set all alg configration：使能所有ALG

·set eim：使能EIM

·add dns-map：添加DNS mapping配置

·delete dns-map：删除DNS mapping配置

·add static inbound：添加入方向静态地址转换配置

·delete static inbound：删除入方向静态地址转换配置

·add static outbound：添加出方向静态地址转换配置

·delete static outbound：删除出方向静态地址转换配置

·add address group：添加地址组

·delete address group：删除地址组

·add address group member：添加地址组成员

·delete address group member：删除地址组成员

·add server group：添加服务器组

·delete server group：删除服务器组

·add server group member：添加服务器组成员

·delete server group member：删除服务器组成员

·set interface static：设置接口下的静态使能开关

·set interface hairpin：设置接口下的hairpin使能开关

·add dynamic：添加动态转换配置

·delete dynamic：删除动态转换配置

·add server：添加内部服务器

·delete server：删除内部服务器

·acl rule change：ACL规则变化

·get statistics：获取统计信息

·smoothing begin：平滑开始

·smoothing end：平滑结束

·get server group statistics：获取服务器组统计信息

·add portblockgroup：添加端口块组

·delete port block group：删除端口块组

·add portblockgroup member：添加端口块组的地址成员

·delete port blockgroup member：删除端口块组的地址成员

·set portblockgroup parameters：设置端口块组的参数

EVENT: Received ioctl message, message type: *type*

·add outbound portblockgroup：添加NAT444端口块静态映射配置

·delete outbound portblockgroup：删除NAT444端口块静态映射配置

·log NAT444 enable：使能NAT444用户日志或告警信息日志

·log NAT444 disable：关闭NAT444用户日志或告警信息日志

·set service slot：设置接口与业务板号绑定关系

·add NAT address：添加NAT地址

·delete NAT address：删除NAT地址

·delete all NAT configurations on interface：删除接口上的所有NAT配置

EVENT: Received ACL event message, ACL number: *number*.

收到ACL事件消息，ACL编号为*number*

EVENT: Received L3VPN message, event: *event*.

收到L3VPN事件消息，事件类型为*event*，包括以下取值：

·Create：VPN创建

·Delete：VPN删除

EVENT: Received interface event message, interface: *interface-type interface-num*, event: *event*.

收到接口事件消息，接口名为*interface-type interface-num*，事件类型为*event*，*event*包括以下取值：

·Active：接口激活

·Deactive：去激活接口

·Delete：删除接口

·Push finish：事件补报结束

EVENT: Received slot event message, slot number: *slot-num*, event: *event*.

收到接口板事件消息，接口板所在槽位号为*slot-num*，事件类型为*event*，*event*包括以下取值：

·Inserted：板插入

·Remove：板拔出

EVENT: Received link event message, interface: *interface*, event: *event*..

收到接口链路事件消息，接口名为*interface-type interface-num*，事件类型为*event*，包括以下取值：

·Link up：链路up

·Push finish：补充报告事件结束

EVENT: Received IPADDR event message, interface: *interface*, event: *event*.

收到地址事件消息，接口名为*interface-type interface-num*，事件类型为*event*，包括以下取值：

·Add：地址添加

·Delete：地址删除

EVENT: Added configuration in kernel: *configuration-type*.

内核新增一条配置，配置类型为*configuration-type*，包括以下取值：

·dns-map：dns-map配置

·static inbound：static inbound配置

·static outbound：static outbound配置

·address group：地址组

·address group member：地址组成员

·server group：内部服务器组

·server group member：内部服务器组成员

·dynamic：动态地址转换配置

·server：内部服务器配置

·portblockgroup：端口块组配置

·portblockgroup member：端口块组的地址成员配置

·NAT address：NAT地址

EVENT: Deleted configuration in kernel: *configuration-type*.

内核删除一条配置，配置类型为*configuration-type*，包括以下取值：

·dns-map：dns-map配置

·static inbound：static inbound配置

·static outbound：static outbound配置

·address group：地址组

·address group member：地址组成员

·server group：内部服务器组

·server group member：内部服务器组成员

·dynamic：动态地址转换配置

·server：内部服务器配置

·portblockgroup：端口块组配置

·portblockgroup member：端口块组的地址成员配置

·NAT address：NAT地址

·all NAT configurations on interface：接口上的所有NAT配置

EVENT: Set configuration in kernel: *configuration-type*.

内核中的NAT配置被修改，配置类型为*configuration-type*，包括以下取值：

·log enable：日志开关

·log flow active：活跃流日志开关

·log flow begin：流创建日志开关

·log flow end：流删除日志开关

·all log configration：所有日志配置

·alg：ALG开关

·all alg configration：所有ALG配置

·eim：EIM开关

·interface static：接口下静态使能开关

·interface hairpin：接口下hairpin使能开关

·acl rule change：ACL变化

·smooth begin：平滑开始

·smooth end：平滑结束

·port block group parameters：端口块组参数

·service slot：业务板号

FLOWMGR *flowmgr-event*, Dest: *dest*, Priority: *priority*, MatchWildCard: *wildcard*, SrcKey: *sip*, DstKey: *dip*, *protocol*,  VPN: *vpn*.

收到引流信息，事件类型为*flowmgr-event*，包括以下取值：

·ADD：删除引流

·DEL：增加引流

目的引擎为*dest*

优先级为*priority*，包括以下取值：

·NAT_FLOW_ADDRGRP_ADDR

·NAT_FLOW_ADDRGRP_PORT

·NAT_FLOW_PORTBLOCK_LOCAL

·NAT_FLOW_PORTBLOCK_GLOBAL

·NAT_FLOW_SRVGRP

·NAT_FLOW_SERVER_LOCAL

·NAT_FLOW_SERVER_GLOBAL

·NAT_FLOW_STATIC_INBOUND_ORIGINAL

·NAT_FLOW_STATIC_INBOUND_NAT

·NAT_FLOW_STATIC_OUTBOUND_ORIGINAL

·NAT_FLOW_STATIC_OUTBOUND_NAT

源地址信息为*sip*，表示源IP地址范围

目的地址信息为*dip, protocol*，*protocol*表示协议号，*dip*表示目的IP地址范围

所属VPN名称为*vpn*

【举例】

\# 在启用了NAT功能的设备上打开所有NAT配置调试功能，并配置**nat service**命令和**nat outbound**命令。**nat service**命令及相关Debug信息的支持情况与设备的具体型号有关，请以设备的实际情况为准。

\<Sysname\> debugging nat config all

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 nat service slot 1

\*Nov 5 08:55:11:361 2013 H3C NAT/7/CONFIG: -MDC=1; 

 EVENT: Received ioctl message, message type: set service slot.

\*Nov 5 08:55:11:361 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Set configuration in kernel: service slot.

*// 内核收到添加接口绑定业务板的IOCTL消息，并且成功添加。*

Sysname-GigabitEthernet1/0/1 nat outbound 2001 address-group 1 no-pat reversible

\*Nov 5 08:55:22:732 2013 H3C NAT/7/CONFIG: -MDC=1; 

 EVENT: Received ioctl message, message type: add address group.

\*Nov 5 08:55:22:732 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Added configuration in kernel: address group.

\*Nov 5 08:55:22:733 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Received ioctl message, message type: set address group parameters.

\*Nov 5 08:55:22:733 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Received ioctl message, message type: add NAT address.

\*Nov 5 08:55:22:733 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Added configuration in kernel: NAT address.

\*Nov 5 08:55:22:739 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Received ioctl message, message type: add NAT address.

\*Nov 5 08:55:22:739 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Added configuration in kernel: NAT address.

\*Nov 5 08:55:22:742 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Received ioctl message, message type: add dynamic.

\*Nov 5 08:55:22:742 2013 H3C NAT/7/CONFIG: -MDC=1;

 EVENT: Added configuration in kernel: dynamic.

\*Nov 5 08:55:22:745 2013 Sysname NAT/7/CONFIG: -MDC=1;

[ FLOWMGR ADD, Dest: 0x11, Priority: AddrGrp-Addr, MatchWildCard: IF_IN \| L3_DEST]

 , SrcKey: 0.0.0.0 255.255.255.255, DstKey: 1.2.3.9-1.2.3.9, All protocols, VPN: vpn1.

\*Nov 5 08:55:22:745 2013 Sysname NAT/7/CONFIG: -MDC=1;

[ FLOWMGR ADD, Dest: 0x19, Priority: AddrGrp-Addr, MatchWildCard: IF_IN \| L3_DEST]

 , SrcKey: 0.0.0.0 255.255.255.255, DstKey: 1.2.3.10-1.2.3.10, All protocols, VPN: vpn1.

*// 收到LIPC消息和IOCTL消息，并且在内核成功添加动态地址转换配置。*
