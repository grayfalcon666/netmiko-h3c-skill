<!-- CMD-INDEX
  debugging dhcp client               | 用户视图             | L8
  debugging dhcp relay                | 用户视图             | L638
  debugging dhcp server               | 用户视图             | L1108
  debugging dhcp snooping             | 用户视图             | L1634
-->

**DHCP \-- DHCP调试命令 \-- debugging dhcp client**

------------------------------------------------------------------------

【命令】

**[debugging dhcp client**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging dhcp client**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCP/BOOTP客户端的所有调试信息开关。

**[error**]：表示DHCP/BOOTP客户端的报文不可识别或错误调试信息开关。

**[event**]：表示DHCP/BOOTP客户端事件调试信息开关。

**[packet**]：表示DHCP/BOOTP客户端的报文调试信息开关。

【描述】

**[debugging dhcp client**]命令用来打开DHCP/BOOTP客户端调试信息开关。**undo debugging dhcp client**命令用来关闭DHCP/BOOTP客户端调试信息开关。

缺省情况下，DHCP/BOOTP客户端调试信息开关处于关闭状态。

表1-1 debugging dhcp client packet命令输出信息描述表

字段

描述

From *ip-address* port *port*

接收报文的源地址和端口号

To *ip-address* port *port*

发送报文的目的地址和端口号

interface *interface-name*

接收或发送报文的接口

Message type: *message-type*

DHCP报文的操作类型，有两种：REQUEST和REPLY

Hardware type: *hardware-type*

DHCP客户端的硬件类型

Hardware address length: *length*

DHCP客户端的硬件地址长度

Hops: *hops*

DHCP报文经过DHCP中继到服务器的跳数

Transaction ID: *transaction-ID*

DHCP客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程

Seconds: *seconds*

DHCP客户端从开始申请到当前经过的时间

Broadcast flag: *flag*

DHCP广播标记：1为广播，0为单播

Client IP address: *client-ip*

DHCP客户端IP地址

Your IP address: *your-ip*

DHCP服务器分配给客户端的IP地址

Server IP address: *server-ip*

DHCP服务器的IP地址

Relay agent IP address: *gateway-ip*

DHCP中继的IP地址

Client hardware address: *client-hardware-address*

DHCP客户端的硬件地址

Server host name: *host-name*

DHCP服务器的主机名

Boot file name: *file-name*

启动文件名及路径

DHCP message type: *type*

DHCP报文的类型，有8种类型：

·BOOTP

·DHCPDISCOVER

·DHCPOFFER

·DHCPREQUEST

·DHCPDECLINE

·DHCPACK

·DHCPNAK

·DHCPRELEASE

·DHCPINFORM

表1-2 debugging dhcp client event命令输出信息描述表

字段

描述

*[InterfaceName*:]

配置为DHCP客户端的接口

DHCP/BOOTP FSM state transfered (*state1*\--\> *state2*) successfully.

DHCP/BOOTP客户端从*state1*状态转换为*state2*状态

Resending DHCP request packet timed out. Stopped sending.

DHCP请求报文重发超时，停止发送DHCP请求报文

Successfully sent ARP request for address (*ip-address*).

发送ARP成功

Received no ARP reply for *ip-address*, so the IP address is available.

没有收到ARP回应，分配的地址可用

Successfully sent *Message-Type* packet.

发送*Message-Type*报文成功

Successfully enabled/disabled DHCP.

启用/关闭DHCP功能成功

Successfully enabled/disabled protocol on cpu.

启用/关闭DHCP功能上送CPU成功

Failed to add IP address.

添加IP地址失败

Notified route module to add routes.

通知路由模块添加路由

Notified route module to delete routes.

通知路由模块删除路由

Received *Message-Type* packet in *state* state. Ignored the packet.

在*state*状态收到*Message-Type*报文，不合法，忽略该报文

Received DHCPACK, *ip-address* is not our requested address. Ignored the packet.

收到的DHCPACK报文中的IP地址不是请求地地址，忽略该报文

Received DHCPACK from non-selected server *ip-address*. Ignored the packet.

收到的DHCPACK报文不是来自选择的Server，忽略该报文

Lease is below min time. Ignored the packet.

租约小于最小时间，忽略该报文

Received duplicate lease. Ignored the packet.

收到重复的租约，忽略该报文

Beginning to detect IP address conflict via ARP.

开始通过ARP进行冲突检测

Interface hardware address changed. Transfered to INIT state.

接口硬件地址变化。DHCP客户端状态迁移到INIT状态

Allocated IP (*ip-address*) has been used by another host.

分配的IP地址已经被其它客户端使用

Allocated IP (*ip-address*) conflicts with some other interface.

分配的IP地址与本机其它接口冲突

T1 timer expired. Begin to renew.

T1时间到期，开始续约操作

Lease expired.

租约到期

Successfully notified the client\'s information change.

Client状态发生变化时，成功通知外部模块option信息变化

****

表1-3 debugging dhcp client error命令输出信息描述表

字段

描述

*[InterfaceName*:]

配置为DHCP客户端的接口

*[operation*]

DHCP客户端状态机变化和事件处理

Failed to allocate memory for new packet.

申请报文内存失败

Failed to send *Message-Type* packet.

发送*Message-Type*报文失败

The *field* field of the received *Message-Typ*e packet is invalid. Ignored the packet.

*[Message-Type*]报文中的*field*域无效，忽略该报文

The received *Message-Type* packet is for another client (*ip-address).* Ignored the packet.

接收到的*Message-Type*报文是发送给客户端*ip-address*的，忽略该报文

Failed to enable/disable DHCP.

启用/关闭DHCP功能失败

Failed to enable/disable BOOTP.

启用/关闭BOOTP功能失败

The length of *option-type* option is invalid (%d bytes). Ignored it.

*[option-type*]域长度非法，忽略此域。*option-type*取值包括：

·subnet mask：子网掩码

·server identifier：服务器标识

·router：默认网关

·tftp server address：TFTP服务器地址

·AC list：接入控制器

·domain name servers：域名服务器地址

·static router：静态路由

·classless static router：无类静态路由

·BIMS server：BIMS服务器地址

The length of *option-type* option is too long (%d bytes). Only save part of it.

*[option-type*]域长度太长，仅保存部分域。*option-type*取值包括：

·router：默认网关

·tftp server address：TFTP服务器地址

·boot file name：启动文件名称

·AC list：接入控制器

·tftp server name：TFTP服务器名称

·domain name servers：域名服务器地址

·domain name：域名

·static router：静态路由

The *option-type* option is invalid. Ignored it.

*[option-type*]域内容非法，忽略此域。*option-type*取值包括： router：默认网关

Discarding packet with bogus htype/hlen.

丢弃包含假htype/hlen域的报文

Decoding options field failed.

解析选项域错误

Received a duplicate DHCPACK packet. Ignored the packet.

接收到重复的DHCPACK报文，忽略该报文

Address conflicts.

地址冲突

Transfered to unknown FSM state.

迁移到未知状态

Skip parsing the current PXE server TLV in verdor specific information option due to invalid server type.

由于PXE服务器类型错误，跳过当前PXE引导服务器地址列表，继续解析Option 43的其他字段

Skip parsing the current PXE server TLV in verdor specific information option due to length error.

由于PXE地址列表长度错误，跳过当前PXE引导服务器地址列表，继续解析Option 43的其他字段

Skip parsing the current PXE server TLV in verdor specific information option due to invalid server number.

由于PXE服务器数目错误，跳过当前PXE引导服务器地址列表，继续解析Option 43的其他字段

Skip parsing the current PXE server TLV in verdor specific information option due to unknown error.

由于未知错误，跳过当前PXE引导服务器地址列表，继续解析Option 43的其他字段

Failed to parse verdor specific information option. Ignore it.

解析Option 43域失败，忽略此域

The destination IP address of classless static route option is wrong.

Option 121选项中的目的地址错误

The mask length of classless static route option is wrong.

Option 121选项中的掩码长度错误

Failed to parse classless static route option. Ignore it.

解析Option 121域失败，忽略该域

The destination IP address of static route option is wrong.

Option 33选项中的目的地址错误

Failed to parse static route option. Ignore it.

解析Option 33域失败，忽略该域

Failed to parse ACS parameters in verdor specific information option.

Option 43选项中ACS参数解析失败

Failed to parse ACS provision code in verdor specific information option.

Option 43选项中ACS provision code解析失败

Malformed packet dhcp:

option length does not equal its option buffer length.

非法的DHCP报文：服务器选项的实际长度和选项中"L"字段标识的长度不相等

The received BOOTP/DHCP packet is not a BOOTPREPLY.

接收到的BOOTP/DHCP报文不是应答报文

Received an invalid DHCP packet, the type is *type-id*

接收到的DHCP报文为非法报文，类型为*type-id*

Failed to add allocated IP *ip-address*.

添加分配的地址失败

Failed to get the index of receiving interface.

获取入接口的接口索引失败

Received an invalid DHCP/BOOTP packet, the length of the packet is too short.

收到非法DHCP/BOOTP报文，报文长度过短

【举例】

\# DHCP客户端从DHCP服务器获得IP地址。打开DHCP客户端的所有调试开关。

\<Sysname\> debugging dhcp client all

\<Sysname\> terminal monitor

\<Sysname\> terminal logging level 7

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 ip address dhcp-alloc

Sysname-Vlan-interface2

\*Jan 19 15:16:24:424 2012 Sysname DHCPC/7/Debug: -MDC=1;

Successfully enabled protocol on cpu.

*[// DHCP*]*协议上送成功。*

\*Jan 19 15:16:24:426 2012 Sysname DHCPC/7/Debug: -MDC=1;

Successfully notified the client\'s information change.

*[// Client*]*状态发生变化时，成功通知外部模块option信息变化。*

\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2: Successfully enabled DHCP.

*// 接口通过DHCP获取IP地址的配置成功。*

\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 DHCP FSM state transfered (HALT\--\>INIT) successfully.

*[// DHCP*]*客户端从HALT状态迁移为INIT状态。*

\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 DHCP FSM state transfered (INIT\--\>SELECTING) successfully.

\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/PACKET: -MDC=1;

To 255.255.255.255 port 67, interface Vlan-interface2

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 2883026512

    Seconds: 0, Broadcast flag: 1

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 000c-295c-e3a6

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPDISCOVER (1)

\*Jan 19 15:16:24:429 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Successfully sent DHCPDISCOVER packet.

*[// DHCP*]*客户端成功发送DHCP-DISCOVER报文，状态机从INIT状态迁移为SELECTING状态。*

\*Jan 19 15:16:24:622 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Received a packet.

\*Jan 19 15:16:24:622 2012 Sysname DHCPC/7/PACKET: -MDC=1;

From 192.168.38.254 port 67, interface Vlan-interface2

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 2883026512

    Seconds: 0, Broadcast flag: 1

    Client IP address: 0.0.0.0   Your IP address: 22.0.0.2

    Server IP address: 22.0.0.1   Relay agent IP address: 0.0.0.0

    Client hardware address: 000c-295c-e3a6

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPOFFER (2)

// DHCP客户端收到IP地址为22.0.0.1的DHCP服务器发送的DHCP-OFFER报文，分配到的IP地址为22.0.0.2，租约时间为86400秒（即一天）。

\*Jan 19 15:16:26:117 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 DHCP FSM state transfered (SELECTING\--\>REQUESTING) successfully.

\*Jan 19 15:16:26:117 2012 Sysname DHCPC/7/PACKET: -MDC=1;

To 255.255.255.255 port 67, interface Vlan-interface2

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 2883026512

    Seconds: 0, Broadcast flag: 1

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 000c-295c-e3a6

    Server host name: not configured

    Boot file name: not configured

DHCP message type: DHCPREQUEST (3)

\*Jan 19 15:16:26:118 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Successfully sent DHCPREQUEST packet.

*[// DHCP*]*客户端成功发送DHCP-REQUEST报文，状态机从SELECTING状态迁移为REQUESTING状态。*

\*Jan 19 15:16:26:118 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Received a packet.

\*Jan 19 15:16:26:118 2012 Sysname DHCPC/7/PACKET: -MDC=1;

From 192.168.38.254 port 67, interface Vlan-interface2

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 2883026512

    Seconds: 0, Broadcast flag: 1

    Client IP address: 0.0.0.0   Your IP address: 22.0.0.2

    Server IP address: 22.0.0.1   Relay agent IP address: 0.0.0.0

    Client hardware address: 000c-295c-e3a6

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPACK (5)

*[// DHCP*]*客户端接收DHCP-ACK报文。*

\*Jan 19 15:16:28:118 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2: Beginning to detect IP address conflict via ARP.

*[// DHCP*]*客户端开始通过ARP进行冲突检测。*

\*Jan 19 15:16:27:119 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Successfully sent ARP request for address 22.0.0.2.

\*Jan 19 15:16:27:119 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Transfer to BOUND state if no ARP reply is received in 2 seconds.

*// 发送ARP报文成功，如果在2秒内没有收到ARP响应报文，则转变为BOUND状态。*

\*Jan 19 15:16:28:118 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Successfully sent ARP request for address 22.0.0.2.

\*Jan 19 15:16:28:118 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Transfer to BOUND state if no ARP reply is received in 1 second

*// 发送ARP报文成功，如果在1秒内没有收到ARP响应报文，则转变为BOUND状态。*

\*Jan 19 15:16:29:117 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 Received no ARP reply for 22.0.0.2, so the IP address is available.

*// 没有收到ARP响应报文，开始使用该地址。*

\*Jan 19 15:16:29:127 2012 Sysname DHCPC/7/Debug: -MDC=1;

Notified route module to add 1 route.

*// 成功通知路由模块添加1条路由。*

\*Jan 19 15:16:29:129 2012 Sysname DHCPC/7/Debug: -MDC=1;

Successfully notified the client\'s information change.

*[// Client*]*状态发生变化时，成功通知外部模块option信息变化。*

\*Jan 19 15:16:29:129 2012 Sysname DHCPC/7/Debug: -MDC=1;

Vlan-interface2 DHCP FSM state transfered (REQUESTING\--\>BOUND) successfully.

*[// DHCP*]*状态迁移为BOUND状态。*

**DHCP \-- DHCP调试命令 \-- debugging dhcp relay**

------------------------------------------------------------------------

【命令】

**[debugging dhcp relay**[ { **all** \| **error** \| **event** \| **packet** [ **client** **mac** *mac-address* ] }]]

**[undo**[ **debugging dhcp relay** { **all** \| **error** \| **event** \| **packet** [ **client mac** *mac-address* ] }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCP中继的所有调试信息开关。

**[error**]：表示DHCP中继的错误调试信息开关。

**[event**]：表示DHCP中继的事件调试信息开关。

**[packet**]：表示DHCP中继的报文调试信息开关。

**[client** **mac** *mac-address*]：表示DHCP中继为指定DHCP客户端转发报文的调试信息开关，其中*mac-address*为DHCP客户端的MAC地址，形式为H-H-H。

【描述】

**[debugging dhcp relay**]命令用来打开DHCP中继调试信息开关。**undo debugging dhcp relay**命令用来关闭DHCP中继调试信息开关。

缺省情况下，DHCP中继调试信息功能开关处于关闭状态。

表1-4 debugging dhcp relay packet调试信息描述表

字段

描述

From *ip-address*

接收报文

To *ip-address*

发送报文

interface *interface-name*

接收或发送报文的接口

Message type: *message-type*

DHCP报文的操作类型，有两种：DHCP-REQUEST和DHCP-REPLY

Hardware type: *hardware-type*

DHCP客户端的硬件类型

Hardware address length: *length*

DHCP客户端的硬件地址长度

Hops: *hops*

DHCP报文经过DHCP中继转发的跳数

Transaction ID: *transaction-ID*

DHCP客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程

Seconds: *seconds*

DHCP客户端从开始申请到当前经过的时间，目前没有使用，固定为0

Broadcast flag: *flag*

DHCP广播标记：1为广播，0为单播

Client IP address: *client-ip*

DHCP客户端IP地址

Your IP address: *your-ip*

DHCP服务器分配给客户端的IP地址

Server IP address: *server-ip*

DHCP服务器的IP地址

Relay agent IP address: *gateway-ip*

DHCP中继的IP地址

Client hardware address: *client-hardware-address*

DHCP客户端的硬件地址

Server host name: *host-name*

DHCP服务器的主机名

Boot file name: *file-name*

启动文件名及路径

DHCP message type: *type*

DHCP报文的类型，有8种类型：

·BOOTP

·DHCPDISCOVER

·DHCPOFFER

·DHCPREQUEST

·DHCPDECLINE

·DHCPACK

·DHCPNAK

·DHCPRELEASE

·DHCPINFORM

表1-5 debugging dhcp relay event调试信息描述表

字段

描述

Add relay agent option (*byte-count* bytes) to the packet.

向报文中添加了*byte-count*个字节的relay agent option选项

Can't find an interface to process the packet.

找不到处理报文的接口，一般原因为对应的接口没有启用DHCP功能

Discard packet with invalid hlen.

丢弃hlen域不正确的报文

Discard packet with invalid options.

丢弃选项内容不正确的报文

Interface *interface-name* is activated.

接口*interface-name*被激活

Add an IP address *ip-address* to the interface *interface-name*.

接口*interface-name*添加IP地址*ip-address*

Interface *interface-name* is deactivated.

接口*interface-name*被去激活

Delete an IP address *ip-address* from the interface *interface-name*.

接口*interface-name*删除IP地址*ip-address*

Interface *interface-name* is deleted.

接口*interface-name*被删除

The MAC address of interface *interface-name* is changed..

接口*interface-name*的MAC地址改变

The packet is a response for refreshing client information.

收到的报文是用户地址表项刷新应答报文

The packet is neither BOOTPREPLY nor BOOTPREQUEST.

收到的报文即不是请求报文也不是应答报文

The received DHCP packet was dropped because it was sent by the receiving relay agent.

DHCP中继收到自己发送的报文后，丢弃该报文

Discard the packet containing option 82 according to the relay information strategy.

由于携带中继信息选项，根据DHCP中继信息处理策略，丢弃该报文

Source MAC check failed.

源MAC地址检测失败

Detect unknown interface event *event* on interface *interface-name*.

接口*interface-name*检测到不支持的接口事件*event*

Detect unknown IP address event *event* on interface *interface-name*.

接口*interface-name*检测到不支持的IP地址事件*event*

The received DHCP packet was dropped because it has traversed a maximum of 16 relay agents

DHCP中继收到的DHCP报文达到最大跳数16，丢弃该报文

表1-6 debugging dhcp relay error调试信息描述表

字段

描述

DHCP is not enabled.

DHCP功能未使能

Error occurs when calculation the value of option *option-code*.

计算选项编号为*option-code*的选项值出错

Failed to get IP address of interface *interface-name*.

获取接口*interface-name*的IP地址失败

Failed to process relay agent option.

处理选项relay agent option失败

Failed to send packet.

报文发送失败

Relay agent option (*option-length* bytes) wasn't added to the packet, because there's no enough space in the packet

报文没有足够的空间存储长度为*option-length*字节的relay agent option选项。忽略relay agent option选项，不将其添加到报文中

Malformed packet dhcp:

option length does not equal its option buffer length.

非法的DHCP报文：服务器选项的实际长度和选项中"L"字段标识的长度不相等

The number of dynamic client entries has reached the maximum.

动态用户地址表项达到最大值

The number of temporary client entries has reached the maximum.

临时用户地址表项达到最大值

【举例】

\# DHCP客户端通过DHCP中继从DHCP服务器获得IP地址。打开DHCP中继的所有调试信息开关。

\<Sysname\> terminal monitor

Current terminal monitor is on.

\<Sysname\> terminal logging level 7

\<Sysname\> debugging dhcp relay all

\<Sysname\>

\*Mar 25 11:36:20:913 2011 Sysname DHCPR/7/PACKET:

From 0.0.0.0 port 68, interface GigabitEthernet1/0/1

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554434

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPDISCOVER (1)

\*Mar 25 11:36:20:916 2011 Sysname DHCPR/7/PACKET:

To 2.0.0.2 port 67, interface is selected by routing table

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 1, Transaction ID: 33554434

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPDISCOVER (1)

*[// DHCP*]*中继接收到DHCP客户端发来的DHCP-DISCOVER请求报文，并向IP地址为2.0.0.2的DHCP服务器转发该报文。*

\*Mar 25 11:36:21:430 2011 Sysname DHCPR/7/PACKET:

From 2.0.0.2 port 67, interface GigabitEthernet1/0/1

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 1, Transaction ID: 33554434

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10

    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPOFFER (2)

\*Mar 25 11:36:21:432 2011 Sysname DHCPR/7/PACKET:

To 1.0.0.10 port 68, interface GigabitEthernet1/0/1

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554434

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10

    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPOFFER (2)

*[// DHCP*]*中继接收到DHCP服务器发来的DHCP-OFFER响应报文，并广播发送该报文。*

\*Mar 25 11:36:22:378 2011 Sysname DHCPR/7/PACKET:

From 0.0.0.0 port 68, interface GigabitEthernet1/0/1

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554435

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPREQUEST (3)

\*Mar 25 11:36:22:385 2011 Sysname DHCPR/7/PACKET:

To 2.0.0.2 port 67, interface is selected by routing table

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 1, Transaction ID: 33554435

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPREQUEST (3)

*[// DHCP*]*中继接收到DHCP客户端发来的DHCP-REQUESET请求报文，并向IP地址为2.0.0.2的DHCP服务器转发该报文。*

\*Mar 25 11:36:22:390 2011 Sysname DHCPR/7/PACKET:

From 2.0.0.2 port 67, interface GigabitEthernet1/0/1

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 1, Transaction ID: 33554435

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10

    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPACK (5)

\*Mar 25 11:36:22:393 2011 Sysname DHCPR/7/PACKET:

To 1.0.0.10 port 68, interface GigabitEthernet1/0/1

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554435

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10

    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPACK (5)

*[// DHCP*]*中继接收到DHCP服务器发来的DHCP-ACK响应报文，并广播发送该报文。*

**DHCP \-- DHCP调试命令 \-- debugging dhcp server**

------------------------------------------------------------------------

【命令】

**[debugging dhcp server**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging dhcp server**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCP服务器的所有调试信息开关。

**[error**]：表示DHCP服务器的错误调试信息开关。

**[event**]：表示DHCP服务器的事件调试信息开关。

**[packet**]：表示DHCP服务器的报文调试信息开关。

【描述】

**[debugging dhcp server**]命令用来打开DHCP服务器调试信息开关。**undo debugging dhcp server**命令用来关闭DHCP服务器调试信息开关。

缺省情况下，DHCP服务器的调试信息开关处于关闭状态。

表1-7 debugging dhcp server packet命令输出信息描述表

字段

描述

From *ip-address*:*port*

接收报文的源地址和端口号

To *ip-address*:*port*

发送报文的目的地址和端口号

interface *interface-name*

接收或发送报文的接口

Message type: *message-type*

DHCP报文的操作类型，有两种：DHCP-REQUEST和DHCP-REPLY

Hardware type: *hardware-type*

DHCP客户端的硬件类型

Hardware address length: *length*

DHCP客户端的硬件地址长度

Hops: *hops*

DHCP报文经过DHCP中继到服务器的跳数

Transaction ID: *transaction-ID*

DHCP客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程

Seconds: *seconds*

DHCP客户端从开始申请到当前经过的时间，目前没有使用，固定为0

Broadcast flag: *flag*

DHCP广播标记：1为广播，0为单播

Client IP address: *client-ip*

DHCP客户端IP地址

Your IP address: *your-ip*

DHCP服务器分配给客户端的IP地址

Server IP address: *server-ip*

DHCP服务器的IP地址

Relay agent IP address: *gateway-ip*

DHCP中继的IP地址

Client hardware address: *client-hardware-address*

DHCP客户端的硬件地址

Server host name: *host-name*

DHCP服务器的主机名

Boot file name: *file-name*

启动文件名及路径

DHCP message type: *type*

DHCP报文的类型，有8种类型：

·BOOTP

·DHCPDISCOVER

·DHCPOFFER

·DHCPREQUEST

·DHCPDECLINE

·DHCPACK

·DHCPNAK

·DHCPRELEASE

·DHCPINFORM

表1-8 debugging dhcp server event命令输出信息描述表

字段

描述

Add a conflict IP *ip-address*.

添加冲突地址*ip-address*

Can't find an interface to process the packet.

找不到处理报文的接口，一般原因为对应的接口没有启用DHCP功能

Client was rebooted.

客户端重启。收到客户端DISCOVER报文时，如果已经给该客户端分配过租约，且该租约有效，则判断为该客户端重启

Client is rebinding its lease.

客户端续约

Client is renewing its lease.

客户端续约

The client selected another server.

客户端选用了其他DHCP服务器分配的地址

The client selected the local server.

客户端选用了本服务器分配的地址

Sent DHCPACK to *ip-address*.

向地址*ip-address*回复DHCPACK应答

No requested address specified in the DHCPDECLINE.

DHCP-DECLINE报文中没有指定请求的地址

The server identifier in the DHCPDECLINE is different from that of the local server.

DHCP-DECLINE报文中的server identifier与本地服务器的server identifier不同

Add conflict IP *ip-address* failed, because the number of conflict IP addresses has reached the maximum.

添加冲突地址*ip-address*失败。原因为冲突地址数量达到系统上限

Add conflict IP *ip-address* failed, because there is no matching lease.

添加冲突地址*ip-address*失败。原因为没有找到对应的租约

Adding conflict IP *ip-address* is ignored, because the declined IP address is static.

添加冲突地址*ip-address*被忽略。原因为请求的地址为静态绑定的地址

Added conflict IP *ip-address* successfully.

添加的冲突地址*ip-address*成功

Ignored the DHCPINFORM, because the source address of the DHCPINFORM is invalid.

DHCP-INFORM被忽略。原因是报文的源地址无效

The DHCPRELEASE specified requested address option.

DHCP-RELEASE报文中携带了请求地址选项。（报文中不应该携带此选项）

The server identifier in the DHCPRELEASE is different from that of the local server.

DHCP-RELEASE报文中的server identifier与本地服务器的server identifier不同

Release IP *ip-address* failed, because the lease is not found.

释放地址*ip-address*失败。原因是没有找到对应的租约

Released IP *ip-address* successfully.

成功释放地址*ip-address*

Receive a DHCPREQUEST message for *request-ip-address*  from *dst-ip-address/interface-name*; server identifier is *server-identifier.*

从地址*dst-ip-address**、*接口*interface-name*收到请求地址*request-ip-address*的DHCP-REQUEST报文，报文中的server identifier选项为*server-identifier*

Discard packet with invalid hlen.

丢弃hlen字段取值不正确的报文

Discard packet with invalid options.

丢弃选项内容不正确的报文

Discard the *message-type* packet: Invalid chaddr.

丢弃类型为*message-type*的报文。原因是报文chaddr域无效

Discard the *message-type* packet: Ignore BOOTP request.

丢弃类型为*message-type*的报文。原因是不处理BOOTP报文

Discard the *message-type* packet: Invalid op field.

丢弃类型为*message-type*的报文。原因是报文op域无效

Discard the *message-type* packet: Invalid packet.

丢弃类型为*message-type*的报文。原因是报文无效

Failed to allocate a lease to client.

分配租约失败

Failed to find lease *ip-address*.

找不到为地址*ip-address*分配的租约

Interface *interface-name* is activated.

接口*interface-name*被激活

Add an IP address *ip-address* to the interface *interface-name*.

接口*interface-name*添加IP地址*ip-address*

Interface *interface-name* is deactivated.

接口*interface-name*被去激活

Delete an IP address *ip-address* from the interface *interface-name*.

接口*interface-name*删除IP地址*ip-address*

Interface *interface-name* is deleted.

接口*interface-name*被删除

The MAC address of interface *interface-name* is changed.

接口*interface-name*的MAC地址改变

The client identifier of the lease for *ip-address* does not match that in the packet.

地址*ip-address*对应的租约中记录的客户端ID为*client-identifier*，和报文中的不匹配

No matching network for the client.

没有找到匹配的网段

Received an ICMP echo reply from *ip-address*.

收到地址*ip-address*的ICMP应答

Received a DHCP packet without options.

收到一个没有选项的DHCP报文

Requested IP *ip-address* is unavailable; Reallocate another IP.

报文中请求的地址*ip-address*不能分配，尝试分配其他的地址

Send an ICMP echo request to *ip-address*.

向地址*ip-address*发送ICMP echo request请求

Discarded the DHCP packet because the op field did not match the DHCP message type option.

由于DHCP报文中的操作类型字段和DHCP报文类型选项不匹配，丢弃该DHCP报文

The packet *message-type* from *ip-address* is too short.

来自地址*ip-address*的消息类型为*message-type*报文，报文长度过短

Detect unknown interface event *event* on interface *interface-name*.

接口*interface-name*检测到不支持的接口事件*event*

Detect unknown IP address event *event* on interface *interface-name*.

接口*interface-name*检测到不支持的IP地址事件*event*

Receive a *message-type* message from *dst-ip-address/interface-name*.

从地址*dst-ip-address**、*接口*interface-name*收到类型为*message-type*的报文

Send a *message-type* message on *dst-ip-address/interface-name*.

通过地址*dst-ip-address**、*接口*interface-name*发送类型为*message-type*的报文

Receive an unknown message (type *message-type*) from *dst-ip-address/interface-name;* Discarded the message.

从地址*dst-ip-address**、*接口*interface-name*收到未知类型的报文，类型为*message-type*。丢弃此报文

Discarded the received DHCP packet because no gateway is configured

由于未配置网关，丢弃收到的DHCP报文

表1-9 debugging dhcp server error命令输出信息描述表

字段

描述

No lease contains the source address *ip-address* of the ICMP echo reply.

收到的ICMP应答地址*ip-address*没有绑定任何租约

DHCP is not enabled.

DHCP功能未使能

Error occurs when calculation the value of option *option-code*.

计算选项编号为*option-code*的选项值出错

Failed to receive ICMP echo reply.

接收ICMP应答报文失败

Failed to allocate a lease: Because the number of leases has reached the maximum.

分配租约失败，数量达到上限

Failed to create timer for ICMP echo request.

创建ICMP请求应答超时定时器失败

Failed to get IP address of interface *interface-name*.

获取接口*interface-name*的IP地址失败

Failed to send ICMP echo request to *ip-address*.

向地址*ip-address*发送ICMP echo请求失败

Failed to send packet.

报文发送失败

Malformed packet dhcp: option length does not equal its option buffer length.

非法的DHCP报文：服务器选项的实际长度和选项中"L"字段标识的长度不相等

No free IP in the address range of the pool or the class.

address range、class range中没有可分配的IP地址

No free IP in the network *network-address*.

网段*network-address*中没有可分配的IP地址

No enough space for option *option-code.*

报文中没有空间存储选项编号为*option-code*的选项内容

No enough space for more options.

报文中没有空间存储过多的选项

【举例】

\# 在设备上配置DHCP服务器功能，打开DHCP服务器的所有调试开关。DHCP客户端通过DHCP中继与DHCP服务器相连，并申请地址。

\<Sysname\> terminal monitor

Current terminal monitor is on.

\<Sysname\> terminal logging level 7

\<Sysname\> debugging dhcp server all

\<Sysname\>

\*Mar 25 11:27:42:714 2011 Sysname DHCPS/7/PACKET:

From 0.0.0.0 port 68, interface GigabitEthernet1/0/1

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554432

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPDISCOVER (1)

\*Mar 25 11:27:42:714 2011 Sysname DHCPS/7/EVENT: Receive a DHCPDISCOVER message from GigabitEthernet1/0/1.

*[// DHCP*]*服务器收到一个DHCPDISCOVER报文。*

\*Mar 25 11:27:42:717 2011 Sysname DHCPS/7/EVENT: Send an ICMP echo request to 1.0.0.10.

*[// DHCP*]*服务器发送ICMP报文检测地址1.0.0.10是否被占用。*

\*Mar 25 11:27:43:228 2011 Sysname DHCPS/7/EVENT: Send a DHCPOFFER message on GigabitEthernet1/0/1.

\*Mar 25 11:27:43:233 2011 Sysname DHCPS/7/PACKET:

To 1.0.0.10 port 68, interface GigabitEthernet1/0/1

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554432

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPOFFER (2)

*[// DHCP*]*服务器发送DHCP-OFFER应答报文。*

\*Mar 25 11:27:43:246 2011 Sysname DHCPS/7/PACKET:

From 0.0.0.0 port 68, interface GigabitEthernet1/0/1

    Message type: REQUEST (1)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554433

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPREQUEST (3)

\*Mar 25 11:27:43:247 2011 Sysname DHCPS/7/EVENT: Receive a DHCPREQUEST message for 1.0.0.10 from GigabitEthernet1/0/1; The server identifier is 1.0.0.1.

\*Mar 25 11:27:43:249 2011 Sysname DHCPS/7/EVENT: The client selected the local server.

*[// DHCP*]*服务器收到一个DHCP-REQUEST报文。*

%Mar 25 11:27:43:250 2011 Sysname DHCPS/5/ALLOCATE_IP: Server IP = 1.0.0.1, DHCP client IP = 1.0.0.10, DHCP client hardware address = 0014-2226-a962, DHCP client lease = 86400 seconds.

\*Mar 25 11:27:43:253 2011 Sysname DHCPS/7/EVENT: Send a DHCPACK message on GigabitEthernet1/0/1.

\*Mar 25 11:27:43:255 2011 Sysname DHCPS/7/PACKET:

To 1.0.0.10 port 68, interface GigabitEthernet1/0/1

    Message type: REPLY (2)

    Hardware type: 1, Hardware address length: 6

    Hops: 0, Transaction ID: 33554433

    Seconds: 0, Broadcast flag: 0

    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10

    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0

    Client hardware address: 0014-2226-a962

    Server host name: not configured

    Boot file name: not configured

    DHCP message type: DHCPACK (5)

*[// DHCP*]*服务器发送DHCP-ACK应答报文。*

**DHCP \-- DHCP调试命令 \-- debugging dhcp snooping**

------------------------------------------------------------------------

【命令】

**[debugging dhcp snooping**[ { **all** \| **error** \| **event** \| **information** \| **packet** }]]

**[undo debugging dhcp snooping**[ { **all** \| **error** \| **event** \| **information** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCP Snooping的所有调试信息开关。

**[error**]：表示DHCP Snooping的错误调试信息开关。

**[event**]：表示DHCP Snooping的事件调试信息开关。

**[information**]：表示DHCP Snooping的Option 82调试信息开关。

**[packet**]：表示DHCP Snooping的报文调试信息开关。

【描述】

**[debugging dhcp snooping**]命令用来打开DHCP Snooping调试信息开关。**undo debugging dhcp snooping**命令用来关闭DHCP Snooping调试信息开关。

缺省情况下，DHCP Snooping的调试信息开关处于关闭状态。

表1-10 debugging dhcp snooping error命令输出信息描述表

字段

描述

Failed to parse DHCP packet.

解析DHCP报文信息失败

Failed to parse IP information (Perhaps the packet is not a UDP packet).

解析IP信息失败，可能因为不是UDP报文

Failed to parse IP header.

解析IP报文头部信息失败

The packet is not a UDP packet.

此报文不是UDP报文

The packet is a bad UDP packet.

此报文是错误的UDP报文

Failed to parse UDP header.

解析UDP头部信息失败

L3Output: Failed to parse IP information (Perhaps the packet is not a UDP packet).

监听三层出方向报文：解析IP信息失败，可能因为不是UDP报文

L3Output: Failed to parse DHCP packet.

监听三层出方向报文：解析DHCP报文信息失败

Failed to send packets. The egress and ingress interfaces are the same *interface-index.*

发送报文失败，因为入接口和出接口相同*interface-index*

Failed to send packets. The interface *interface-index* is invalid.

发送报文失败，因为接口*interface-index*无效

Failed to send packets. The interface *interface-index* does not belong to the current VLAN.

发送报文失败，因为接口*interface-index*不属于当前vlan

The interface *interface-index* is an aggregation group member, which can't send the packets.

接口*interface-index*是聚合口成员，不能从该接口发送报文

Failed to send packets. The interface *interface-index* is down.

发送报文失败，因为接口*interface-index*是down状态

Failed to send packets in VLAN (interface is *interface-index*).

vlan内接口*interface-index*转发报文失败

Successfully sent packets in VLAN (interface is *interface-index*).

vlan内接口*interface-index*转发报文成功

The option field of DHCP packet is too short (The value is *value*).

DHCP报文option域太短，值为*value*

Packet statistics error: ERROR_NO_ENOUGH_RESOURCE OutBufsize is *size*

获取报文统计信息错误，因为长度不足，长度值为*size*

ISSU recovery error (error is *error*).

ISSU恢复失败*error*

ISSU file saving failed (error is *error*).

ISSU存储文件失败*error*

Opening *filename* failed.

打开文件*filename*失败

The length of file header is error (len is *length*).

文件头长度*length*错误

File header error.

文件头错误

Insufficient storage space.

存储空间不足

Failed to get file attribute: fstat *string*

获取文件属性失败

Failed to delete IPCIM entries by VLAN *vlan-id*.

通知IPCIM删除vlan(*vlan id*)下的表项

Failed to delete IPCIM entries on interface *interface-index.*

通知IPCIM删除接口*interface-index*下的表项

Failed to delete an IPCIM entry.

通知IPCIM删除一条表项

Failed to synchronize IPCIM results.

同步IPCIM结束失败

Failed to synchronize IPCIM.

同步IPCIM失败

Failed to set rule on the the port *interface-index*.

设置接口*interface-index*规则失败

Failed to set the request rule.

设置请求方向规则失败

Failed to set the reply rule.

设置应答方向规则失败

Failed to send synchronous message to chassis *chassis-number* slot *slot-number*.

发送到框号*chassis-number*，板号*slot-number*.的同步消息失败

Failed to send asynchronous message to chassis *chassis-number* slot *slot-number*.

发送到框号*chassis-number*，板号*slot-number*的异步消息失败

表1-11 debugging dhcp snooping event命令输出信息描述表

字段

描述

Started to delete the running database.

开始删除正在运行的数据库

Started to reset the running database.

开始重置正在运行的数据库

Set global configuration to database *result*.

设置全局配置数据库*result*

Deleted global configuration from database *result*.

删除全局配置数据库*result*

Set interface *interface-index* used configuration database *result.*

设置接口*interface-index*生效配置数据库*result.*

Deleted interface *interface-index* used configuration database *result.*.

删除接口*interface-index*生效配置数据库*result.*

Set interface *interface-index* unused configuration database *result.*.

设置接口*interface-index*未生效配置数据库*result.*

Try to add an IP-MAC entry to the running database.

尝试向运行数据库添加IP-MAC表项

Try to delete an IP-MAC entry from the running database.

尝试从运行数据库删除IP-MAC表项

Try to delete IP-MAC entries from the running database by interface *interface-index*.

尝试向运行数据根据接口*interface-index*删除IP-MAC表项

Try to move the data from the database *number* to the database *number*.

尝试移动数据库

Try to delete database.

尝试删除数据库

Start to send asynchronous message (DataType: *DataType* OpType: *OpType*) to all slots.

开始发送异步消息(*DataType**，OpType*)到所有单板

Start to send asynchronous message (DataType: *DataType* OpType: *OpType*) to slot *slot-number*.

开始发送异步消息(*DataType**，OpType*)到单板*slot-number*.

Start to send asynchronous message (DataType: *DataType* OpType: *OpType*) by if *interface-index*.

开始发送异步消息(*DataType**，OpType*)到接口*interface-index*所在板

Start to send synchronous message to slot *slot-number*.

开始发送同步消息到单板*slot-number*

Set the global rule *rule-id*.

设置全局规则*rule-id*

Set the port *interface-index* rule *rule-id*.

设置接口*interface-index*规则*rule-id*

Set the rate limit.

设置限速

Started to synchronize IPCIM.

开始同步IPCIM

Finished synchronizing IPCIM.

结束同步IPCIM

Deleted if *interface-index*.

删除接口*interface-index*处理

Inactivated if *interface-index*..

去激活接口*interface-index*处理

Activated if *interface-index*.

激活接口*interface-index*处理

Added port *interface-index* to aggregate interface.

接口*interface-index*加入聚合口处理

Removed port *interface-index* from aggregate interface.

接口*interface-index*离开聚合口处理

The slot *slot-number* is inserted.

单板*slot-number*插入完成

The number of MAC-PORT entries has reached the maximum.

MAC-PORT表项达到最大值

Successfully added a MAC-port entry (mac is *mac-address*, ifindex is *interface-index*,CVlan is *CVlan*, CSVlan is *CSVlan*, SVlan is *SVlan*, SSVlan is *SSVlan*, MsgType is *MsgType*)

Failed to add a MAC-port entry (mac is *mac-address*, ifindex is *interface-index*, CVlan is *CVlan*, CSVlan is *CSVlan*, SVlan is *SVlan*, SSVlan is *SSVlan*, MsgType is *MsgType*)

添加MAC-PORT表项(*mac**地址，interface-index*,*，server vlan，server second vlan，MsgType*)成功

添加MAC-PORT表项(*mac**地址，interface-index*,*，server vlan，server second vlan，MsgType*)失败

The number of packet nodes has reached the maximum.

packet结点个数超过最大值

Notify user to get *number* packet nodes, the result is *result.*

通知用户态获取packet结点*number*，结果是*result*

Assign the rate limit to driver: interface *interface-index*, LimitRate *LimitRate*, result *result.*

向驱动下发限速(*interface-index**，LimitRate，result.*)

Obtained kernel data: DataType is *DataType*, OperType is *OperType*, ProcResult is *ProcResult*

获取内核态数据(*DataType**，OperType，ProcResult*)

Set kernel data: DataType is *DataType*, OperType is *OperType*, ProcResult is *ProcResult*

向内核态下发数据(*DataType*，*OperType*，*ProcResult*)

Responded to bridge MAC change: DEV_EVT_BMAC_CHANGE

响应桥MAC变化

Child process *number* of parent process *number* exited: exitcode is *exitcode*

父进程*number*的子进程*number*退出*exitcode*

No MAC-port entry is found when adding a packet node.

添加packet结点时，没有找到MAC-PORT表项

Successfully added a MAC-port entry by packet type *type-id*.

报文*type-id*添加MAC-PORT表项成功

Delete an IP-MAC entry from database *number*.

从DBM删除一条IP-MAC表项

Add an IP-MAC entry to database *number*..

向DBM添加一条IP-MAC表项

表1-12 debugging dhcp snooping information命令输出信息描述表

字段

描述

Fill circuit-id in padding format *type*:Length is *length*.

以*type*填充方式填充circuit id，填充长度是*length*.

填充方式如下几种：

·normal

·verbose

·string

Fill remote-id in padding format *type*:Length is *length*..

以*type*填充方式填充remote id，填充长度是*length*.

填充方式如下几种：

·normal

·sysname

·string

Stripping Option 82 succeeded: offset is *offset*, stripped length is *length*.

剥离Option 82，偏移量*offset*，剥离长度*length*

Padded packet: padded length is *length*..

填充报文，填充长度*length*.

Recalculated IP and UDP checksum.

重新计算IP和UDP校验和

Received packet: Option 82 offset is *offset*, Option 82 handling strategy is *type*.

Option 82在报文中的偏移量是*offset*，处理策略是*type*，

处理策略：

·replace：替换成新的Option 82内容

·keep：保持现有的Option 82内容

·drop：删除现有的Option 82内容

表1-13 debugging dhcp snooping packet命令输出信息描述表

字段

描述

Started to parse DHCP option (len is *length*).

开始解析DHCP报文option域，域长度为*length*

Option *number* is found: the offset is *offset*

选项*number*找到，偏移量是*offset*

Before VLAN mapping: MBUFIfIndex is *MBUFIfIndex*, IfIndex is *interface-index*, InFstVLAN is *InFstVLAN*,InSecVLAN is *InSecVLAN*, OutFstVLAN is *OutFstVLAN*, OutSecVLAN is *OutSecVLAN*

VLAN mapping处理前，MBUF中的接口索引*MBUFIfIndex*，接收报文的接口索引*interface-index*,，入方向first vlan是*InFstVLAN*，入方向second vlan是*InSecVLAN*，出方向first vlan是*OutFstVLAN*，出方向second vlan是*OutSecVLAN*

After VLAN mapping: MBUFIfIndex is *MBUFIfIndex*, IfIndex is *interface-index* InFstVLAN is *InFstVLAN*, InSecVLAN is *InSecVLAN*, OutFstVLAN is *OutFstVLAN*, OutSecVLAN is *OutSecVLAN*

VLAN mapping处理后，MBUF中的接口索引*MBUFIfIndex*，接收报文的接口索引*interface-index*，入方向first vlan是*InFstVLAN*，入方向second vlan是*InSecVLAN*，出方向first vlan是*OutFstVLAN*，出方向second vlan是*OutSecVLAN*

Started to check MAC validity in DHCP packets.

开始检查MAC有效性

Started to check validity of the DHCP-request-packet.

开始请求方向报文有效性检查

The MAC in the DHCP packet doesn\'t match the source MAC in Ethernet header.

以太帧头的MAC与DHCP报文的MAC不匹配

Invalid packet by request-check.

通过请求方向报文有效检查，此报文无效

Successfully sent packets in VLAN (interface is *interface-index*).

vlan内接口*interface-index*转发报文成功

Delivered the request packet to CPU, continue

请求方向报文上送本机，继续处理

Sent the packet through the trusted port.

从信任端口转发报文

Sent the cast packet, through the trusted port.

广播报文从信任端口转发

Failed to send a DHCP packet.

发送DHCP报文失败

L3Output: Started to process DHCP packets.

三层出方向开始处理报文

L3Output: Ignored request packets.

三层出方向请求报文不处理

Started to process DHCP packets.

开始处理DHCP报文

The DHCP packet is sent to slot *slot-number.*

DHCP报文透传主用板*slot-number.*

Sent a DHCP reply packet to DHCP relay agent.

发送给DHCP relay的报文

Received packets from interface *interface-index*

            Transaction ID: *Transaction ID*

            Client IP address: *ip-address* Your IP address: *ip-address*

            Relay agent IP address: *ip-address*

            Client hardware address: *hardware address*

            Request IP address: *ip-address* Server ID: *server-id*

            Client First VLAN ID: *vlan-id* Client Second VLAN ID: *vlan-id*

            Server First VLAN ID: *vlan-id* Server Second VLAN ID: *vlan-id*

            DHCP message type: *message-type*\"

从接口*interface-index*接收到报文，报文中的*Transaction ID，*客户端IP地址*ip-address，*服务器分配客户端的*ip-address*，中继IP地址*ip-address*，客户端硬件地址*hardware address*，请求的IP地址*ip-address*，服务器ID*server-id*，客户端第一层VLAN ID *vlan-id*，客户端第2层VLAN ID *vlan-id*。服务器第一层VLAN ID*vlan-id*，服务器第2层VLAN ID *vlan-id*。DHCP报文类型*message-type*。

【举例】

\#打开DHCP Snooping上的所有调试信息开关，DHCP客户端从DHCP服务器获得IP地址，DHCP Snooping设备连接在客户端和服务器之间进行侦听。

\<Sysname\> debugging dhcp snooping all

\<Sysname\> terminal monitor

\<Sysname\> terminal logging level 7

\<Sysname\>

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.    

*[// DHCP Snooping*]*开始处理报文。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found：the offset is 4.

*// 解析报文，报文携带option53。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 12 is found：the offset is 7.

*// 解析报文，报文携带option12。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 50 is found: the offset is 25

*// 解析报文，报文携带option50。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 55 is found：the offset is 31

*// 解析报文，报文携带option55。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 57 is found：the offset is 40

*// 解析报文，报文携带option57。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 60 is found：the offset is 44

*// 解析报文，报文携带option60。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 61 is found：the offset is 71

*// 解析报文，报文携带option61。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0

, IfIndex is 4, InFstVLAN is 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0

*[// VLAN mapping*]*处理前，报文携带的VLAN等信息。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,

 IfIndex is 4, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is0

*[// VLAN mapping*]*处理后，报文携带的VLAN等信息。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len is 105)

*// 解析报文的option域。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET:

Receiveed packets from interface Ten-GigabitEthernet1/0/3

    Transaction ID: 9e604c7b

    Client IP address: 0.0.0.0            Your IP address: 0.0.0.0

    Relay agent IP address: 0.0.0.0

    Client hardware address: 000f-e25d-f27c

    Request IP address: 9.2.2.2           Server ID: N/A

    Client First VLAN ID: 1               Client Second VLAN ID: N/A

    Server First VLAN ID: 1               Server Second VLAN ID: N/A

    DHCP message type: DHCPDISCOVER

*// DHCP Snooping收到一个DHCP-DISCOVER报文。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/KENTRY: Successfully added a MAC-port entry(mac is 000f-e25d-f27c, ifindex is 4, CVlan is 1, CSVlan is 65535, SVlan is 1, SSVlan is 0, MsgType is 1)    

*// 添加MAC-PORT表项。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Successfully added a MAC-port entry

by packet type(1).

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Fill circuit-id in padding format

normal： Length is 8.

*// 填充option82的circuit id。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Fill remote-id in padding format

normal： Length is 10.

*// 填充option82的remote id。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.      

*// 计算IP头和UDP头校验和。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Received packet Option 82 offset is

0, option 82 strategy is Replace.

*// 接收的报文携带option 82，对此报文的处理策略replace。*

\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET:

*// 从VLAN下的e1/0/4接口转发报文。*

\*Jan  1 00:43:17:873 2011 Sysname DHCPSP4/6/PACKET: Successfully sent packet in vlan

(interface is 5)                                                 \
*// 转发报文成功。*

\*Jan  1 00:43:17:873 2011 Sysname DHCPSP4/6/PACKET: Failed to send packets. The interfa

ce(12) is down.

*// 从接口索引为12的接口转发报文失败，因为此接口状态down。*

\*Jan  1 00:43:17:873 2011 Sysname DHCPSP4/6/PACKET: BroadCast packet, Trans packet to t

rust port and continue

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found, the offset is 4.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 54 is found, the offset is 7.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 51 is found, the offset is 13

.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 58 is found, the offset is 19

.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 59 is found, the offset is 25

.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 1 is found, the offset is 31.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len=64).

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 82 is found, the offset is 37

.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0, IfIndex is 5, InFstVLAN is 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MacPort ifSendIndex

is 4, CVlan is 1, CSVlan is 65535, SSVlan is 0

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MarkFlag is 0, OutPort

Index is 4, OutFstVLAN is 1

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,

 IfIndex is 5, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is 0

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/PACKET:

Receive packets from interface Ten-GigabitEthernet1/0/4

    Transaction ID: 9e604c7b

    Client IP address: 0.0.0.0            Your IP address: 9.2.2.2

    Relay agent IP address: 0.0.0.0

    Client hardware address: 000f-e25d-f27c

    Request IP address: N/A               Server ID: 9.0.0.1

    Client First VLAN ID: 1               Client Second VLAN ID: N/A

    Server First VLAN ID: 1               Server Second VLAN ID: N/A

    DHCP message type: DHCPOFFER

*// DHCP Snooping收到一个DHCP-OFFER报文。*

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/INFO: Stripping Option 82 succeeded: offset is

319, stripped length is 20.

*// 剥离option82选项。*

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/INFO: Padded packet: padded length is 20.

\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found, the offset is 4.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 12 is found, the offset is 7.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len is 111)

.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 50 is found, the offset is 25

.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 54 is found, the offset is 31

.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 55 is found, the offset is 37

.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 57 is found, the offset is 46

.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 60 is found, the offset is 50

.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 61 is found, the offset is 77

.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0

, IfIndexis 4, InFstVLANis 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,

 IfIndex is 4, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is 0

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/KENTRY: Successfully added a MAC-port(mac is 000f

-e25d-f27c, ifindex is 4, CVlan is 1, CSVlan is 65535, SVlan is 1, SSVlan is 0, MsgType is 3)

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Successfully added a MAC-port entry

by packet type(3).

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/PACKET:

Receiveed packets from interface Ten-GigabitEthernet1/0/3

    Transaction ID: 9e604c7b

    Client IP address: 0.0.0.0            Your IP address: 0.0.0.0

    Relay agent IP address: 0.0.0.0

    Client hardware address: 000f-e25d-f27c

    Request IP address: 9.2.2.2           Server ID: 9.0.0.1

    Client First VLAN ID: 1               Client Second VLAN ID: N/A

    Server First VLAN ID: 1               Server Second VLAN ID: N/A

    DHCP message type: DHCPREQUEST

*// DHCP Snooping收到一个DHCP-REQUEST报文。*

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Fill circuit-id in padding format

 normal:Length is 8.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Fill remote-id in padding format

normal: Length is 10.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.

\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Receiveed packet Option 82 offset is

0, Option 82 strategy is Replace.

\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/KENTRY: Notify user to get 1 packet node

s, the result is 0.

\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/PACKET: Successfully Sent packets in vlan (interface is 5).

\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/PACKET: Failed to send packets. The interfa

ce(12) is down.

\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/PACKET: BroadCast packet, Trans packet to t

rust port and continue

\*Jan  1 00:43:17:886 2011 Sysname DHCPSP4/6/2KNL: Started to send synchronous message

to slot(1).

\*

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found, the offset is 4.

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 54 is found, the offset is 7.

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 51 is found, the offset is 13

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 58 is found, the offset is 19

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 59 is found, the offset is 25

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 1 is found, the offset is 31.

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 82 is found, the offset is 37

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len is 64).

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0

, IfIndex is 5, InFstVLAN is 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MacPort ifSendIndex

is 4, CVlan is 1, CSVlan is 65535, SSVlan is 0

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MarkFlag is 0, OutPort

Index is 4, OutFstVLAN is 1

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,

 IfIndex is 5, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is 0

\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/7/PACKET:

Received packets from interface Ten-GigabitEthernet1/0/4

    Transaction ID: 9e604c7b

    Client IP address: 0.0.0.0            Your IP address: 9.2.2.2

    Relay agent IP address: 0.0.0.0

    Client hardware address: 000f-e25d-f27c

    Request IP address: N/A               Server ID: 9.0.0.1

    Client First VLAN ID: 1               Client Second VLAN ID: N/A

    Server First VLAN ID: 1               Server Second VLAN ID: N/A

    DHCP message type: DHCPACK

*// *DHCP Snooping收到一个DHCP-ACK报文。*

\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/7/INFO: StrippingOption 82 succeeded: offset is

319, stripped length is 20.

\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/7/INFO: Padded packet: Paddedlength is 20.

\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.

\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/6/KENTRY: Notify user to get 1 packet node

s, the result is 0.

*// 通知用户态获取报文信息。*

\*Jan  1 00:43:17:896 2011 Sysname DHCPSP4/6/2KNL: Started to send synchronous message

to slot(1).

\*Jan  1 00:43:17:897 2011 Sysname DHCPSP4/6/DBM: Try to add an IP-MAC entry to the running database.

\*Jan  1 00:43:17:901 2011 Sysname DHCPSP4/6/DBM: Failed to add an IP-MAC entry to database (0)
