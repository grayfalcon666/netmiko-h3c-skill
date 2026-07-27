<!-- CMD-INDEX
  debugging tunnel                    | 用户视图             | L7
  debugging tunnel4                   | 用户视图             | L381
  debugging tunnel6                   | 用户视图             | L603
-->

**隧道 \-- 隧道调试命令 \-- debugging tunnel**

------------------------------------------------------------------------

【命令】

**[debugging tunnel**[ { **all** \| **error** \| **event** \| **packet** } [ **interface tunnel** *interface-number* ]]]

**[undo debugging tunne**[l { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示Tunnel模块所有调试信息开关。

**[error**]：表示Tunnel模块错误调试信息开关。

**[event**]：表示Tunnel模块事件调试信息开关。

**[packet**]：表示Tunnel模块报文调试信息开关。

**[interface tunnel** *interface-number*]：表示指定Tunnel接口进行调试。

【描述】

**[debugging tunnel**]命令用来打开Tunnel模块的调试信息开关。**undo debugging tunnel**命令用来关闭Tunnel模块的调试信息开关。

缺省情况下，Tunnel模块的调试信息开关处于关闭状态。

表1-1 debugging tunnel error命令输出信息描述表

字段

描述

Failed to send data to slot *num*.

发送数据到槽位号为*num*的接口板失败

Tunnel ICMP error: Can't get the corresponding tunnel interface in up state.

收到ICMP差错报文后，找不到对应的处于up状态的隧道接口

Tunnel ICMP error: Failed to update the ICMP soft state.

更新ICMP软状态失败

Failed to create Tunnel*num*.

创建接口Tunnel*num*失败

Failed to delete Tunnel*num*.

删除接口Tunnel*num*失败

The EVI-Link interface already exists.

此EVI-Link接口已经存在

The number of the EVI-Link interfaces has reached the maximum.

EVI-Link接口数量已经达到最大值

The EVI-Link interface doesn\'t exist.

此EVI-Link接口不存在

Failed to find the tunnel interface with the EVI-Link interface.

根据EVI-Link接口查找Tunnel接口失败

Failed to create the EVI-link interface.

创建EVI-Link接口失败

Failed to delete the EVI-Link interface.

删除EVI-Link接口失败

Failed to find the EVI-Link interface.

查找EVI-Link接口失败

Failed to find the output interface.

查找出接口失败

Failed to get the tunnel mode.

获取隧道模式失败

表1-2 debugging tunnel event命令输出信息描述表

字段

描述

Tunnel*num* can\'t come up because *reason*.

隧道Tunnel*num*不能up的原因为*reason*，*reason*的取值包括：

·the source address has been changed：隧道源接口地址已经改变

·the tunnel interface is shutdown：接口处于shutdown状态

·mode check failed：隧道模式检查失败

·there is not enough hardware resource：硬件资源不足

·the tunnel source and destination belong to different VRFs：隧道源地址和目的地址属于不同的VPN

Tunnel*num*: No keepalive packet received from the peer.

隧道Tunnel*num*发送keepalive报文后，没有收到对端返回的keepalive报文

Tunnel ICMP event: The ICMP error message has been sent to ICMP module.

ICMP差错信息已经发送到ICMP模块

Tunnel ICMP event: The ICMPv6 error message has been sent to ICMP6 module.

ICMP6差错信息已经发送到ICMPv6模块

Received an ADJ change message (flag = *flag*).

收到一个ADJ变化的消息，标记为*flag*

Received a VN change message.

收到一个VN变化的消息

Event registered: SocketFd = *fd,* tunnelMode = *mode*, event = *event*.

Tunnel事件注册：套接字为*fd*，隧道模式为*mode*，事件类型为*event*

Recovered interface (ifType = *type*) configuration during ISSU.

ISSU期间添加节点，接口类型*type*

Configuration of Tunnel*num* has already been synchronized.

接口Tunnel*num*的配置已经同步

Synchronization count is *number*.

同步次数为*number*

Received EVI-Link creating message.

收到创建EVI-Link接口消息

Received EVI-Link deleting message.

收到删除EVI-Link接口消息

Tunnel*num* adjusted link MTU to *mtusize*.

接口Tunnel*num*调整MTU为*mtusize*

EVI-Link*num*: No keepalive packet received from the peer.

EVI-Link*num*发送keepalive报文后，没有收到对端返回的keepalive报文

RIB updated message: IfIndex = *index*, ifType = *type*, nextHop = *addr*, count = *cnt*, VNID = *vnid*, outIfIndex = *indexout*, rtFlag = *flag*.

路由刷新消息：接口索引为*index*，接口类型为*type*，下一跳地址为*addr*，路由个数为*cnt*，VN ID为*vnid*，出接口索引为*index*，路由标记*flag*

RIB deleted message: IfIndex = *index*, ifType = *type*, nextHop = *addr*,

路由删除消息：接口索引为*index*，接口类型为*type*，下一跳地址为*addr*

Registered RIB: IfIndex = *index*, ifType = *type*, dstAddr = *addr*, vrfIndex = *vrfindex*

向路由表中注册：接口索引为*index*，接口类型为*type*，目的地址我*addr，*VPN实例索引为*vrfindex*

Deregistered RIB: IfIndex = *index*, ifType = *type*, dstAddr = *addr*, vrfIndex = *vrfindex*

从路由表中解除注册：接口索引为*index*，接口类型为*type*，目的地址为*addr，*VPN实例索引为*vrfindex*

Synchronized tunnel configurations on Tunnel*num* (ifIndex = *ifindex*).

接口Tunnel*num*同步隧道的相关配置，接口索引为*index*

Number of synchronization messages sent: *cnt*.

同步发送个数为*cnt*

Number of synchronization message received: *cnt*.

同步接收个数为*cnt*

Synchronization started.

同步开始

Synchronized DS-Lite switch on interface (ifIndex = *ifindex*)*.

接口同步DS-Lite开关的配置，接口索引为if*index*

*[IfName* failed to get information about operation *id*.]

Tunnel接口或EVI-Link接口*IfName*获取操作*id*的信息失败

Processing result of operation *id* for *IfName*: *result*.

Tunnel接口或EVI-Link接口*IfName*下发的操作*id，*处理结果为*result*，*result*的取值包括：

·succeeded：处理该操作成功

·not supported：不能处理该操作

·resources not enough：没有足够的资源处理该操作

·resources not ready：未准备好处理该操作

·failed：处理该操作失败

·processed already：相同的操作已经处理

*[IfName* notifies driver: Operation = *id*]

TunnelIfIndex = *tunnelifindex*, EvilinkIfIndex = *evilinkifindex*

VRFIndex = *vrfindex*, DstVRFIndex = *dstvrfindex*

TunnelMode = *mode*, TransPro = *pro*

TunnelSrc = *srcaddr*

TunnelDst = *dstaddr*

TTL = *ttl*, ToS = *tos*, DFBit = *dfbit*

MTU = *mtu*, IPv6MTU = *ipv6mtu*

DrvContext0 = *context0*, DrvContext1 = *context1*

VNHandle = *vnhandle*, ADJIndex = *adjindex*

Tunnel接口或EVI-Link接口*IfName*通知驱动进行操作*id*

Tunnel接口索引为*ifindex*，EVI-Link接口索引为*evilinkifindex*

Tunnel接口所属VPN为*vrfindex*，隧道目的端地址所属VPN为*dstvrfindex*

隧道模式为*mode*，隧道传输协议为*pro*

隧道源端地址为*srcaddr*

隧道目的端地址为*dstaddr*

TTL为*ttl*，TOS为*tos*，DF标志为*dfbit*

MTU为*mtu*，IPv6MTU为*ipv6mtu*

隧道驱动上下文信息为*context0*、*context1*

VN句柄为*vnhandle*，ADJ索引为*adjindex*

表1-3 debugging tunnel packet命令输出信息描述表

字段

描述

IPv6 tunnel packet: The length of extension header is *length*.

隧道通过IPv6快转转发出隧道报文时，解析出IPv6报文扩展头长度是*length*

The protocol number *number* of the packet from driver is unknown. Dropped the packet

驱动发送给隧道接口的报文，协议号为未知的数值*number*，丢弃该报文

Sent an ICMPv6 parameter problem message to the source, when the encapsulation limit is reached.

IPv6 over IPv6隧道报文超过允许的最大嵌套封装次数后，不允许该报文再进入隧道进行封装。此时，隧道向源节点发送ICMP6参数错误报文

Tunnel packet: Received an inner ICMP message (type = *type*, code = *code*).

接收到ICMP差错报文，差错类型为*type*和差错码为*code*

Received a packet to be de-encapsulated.

收到一个需要解封装的报文

Received a GRE over IPv4 packet with upper layer protocol *id*.

收到一个GRE over IPv4报文，上层协议为*id*

Received an IPv4 over IPv4 packet.

收到一个IPv4 over IPv4报文

Received an IPv6 over IPv4 packet.

收到一个IPv6 over IPv4报文

Received a de-encapsulated packet.

收到一个已经解封装的报文

Received a GRE over IPv6 packet with upper layer protocol *id*.

收到一个GRE over IPv6报文，上层协议为*id*

Received an IPv4 over IPv6 packet.

收到一个IPv4 over IPv6报文

Received an IPv6 over IPv6 packet.

收到一个IPv6 over IPv6报文

Received a too big packet.

收到一个过大报文

Received a packet (family = *family*, length = *length*).

收到一个报文，协议族为*family*，长度为*length*

Received a message to trigger ARP.

收到一个触发ARP的消息

Received a message to trigger ND.

收到一个触发ND的消息

Received a message to resend interface information for Tunnel*num* (ifindex = *ifindex*).

收到一个重发接口Tunnel*num*（接口索引为*ifindex*）信息的消息

【举例】

\# 打开Tunnel错误调试信息开关。在分布式环境下配置隧道相关命令时插拔接口板，设备上将出现如下调试信息。

\<Sysname\> debugging tunnel error

\*Nov 17 09:16:07:928 2010 Sysname TUNNEL/7/error: -MDC=1;

Failed to send data to slot1.

*// 发送数据到1号接口板失败*

\# 打开Tunnel事件调试信息开关。创建隧道接口，配置隧道接口参数使隧道接口up后，shutdown隧道接口，设备上将出现如下调试信息。

\<Sysname\> debugging tunnel event

\*Sep  6 11:59:59:183 2011 Sysname TUNNEL/7/event: -MDC=1;

 Tunnel0 can\'t come up because the tunnel interface is shutdown. 

*// 由于接口处于shutdown状态，隧道Tunnel0不能up*

\# 打开Tunnel报文调试信息开关。设备接收到不支持的协议报文时，打印如下调试信息。

\<Sysname\> debugging tunnel packet

\*Nov 17 09:16:07:928 2010 Sysname TUNNEL/7/debug: -MDC=1;

 The protocol number 4 of the packet is unknown. Dropped the packet

*// 隧道接收到不支持的协议报文（协议号为4），丢弃该报文*

**隧道 \-- 隧道调试命令 \-- debugging tunnel4**

------------------------------------------------------------------------

【命令】

**[debugging tunnel4**[ { **all** \| **error** \| **packet** } [ **interface tunnel** *interface-number* ]]]

**[undo debugging tunnel4**[ { **all** \| **error** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IPv4 Tunnel所有调试信息开关。

**[error**]：表示IPv4 Tunnel错误调试信息开关。

**[packet**]：表示IPv4 Tunnel报文调试信息开关。

**[interface tunnel** *interface-number*]：表示指定Tunnel接口进行调试。

【描述】

**[debugging tunnel4**]命令用来打开IPv4 Tunnel的调试信息开关。**undo debugging tunnel4**命令用来关闭IPv4 Tunnel的调试信息开关。

缺省情况下，IPv4 Tunnel的调试信息开关处于关闭状态。

IPv4 Tunnel指的是外层传输协议为IPv4协议的隧道。

表1-4 debugging tunnel4 error命令输出信息描述表

字段

描述

Tunnel*num* status check: Source address is not set.

隧道Tunnel*num*状态检查：源地址没有配置

Tunnel*num* status check: Destination address is not set.

隧道Tunnel*num*状态检查：目的地址没有配置

Tunnel*num* status check: Source address is not the address of a local interface.

隧道Tunnel*num*状态检查：源地址不是本设备接口的地址

Tunnel*num* status check: Failed to get FIB information of the source address.

隧道Tunnel*num*状态检查：获取源地址FIB信息失败

Tunnel*num* status check: Destination address should not be the address of a local interface.

隧道Tunnel*num*状态检查：目的地址不能是本设备接口的地址

Tunnel*num* status check: Failed to get FIB information of the destination address.

隧道Tunnel*num*状态检查：获取目的地址FIB信息失败

The protocol state of Tunnel*num* is not up. Dropped the packet.

待解封装报文出隧道时发现相应隧道接口协议状态不是up的，报文被丢弃

Tunnel*num*: The information obtained from the adjacency table is invalid.

隧道Tunnel*num*：获取的邻接表信息非法

Tunnel*num*: The passenger protocol number *number* is not supported.

隧道Tunnel*num*：不支持乘客协议*protocol-number*

The IPv4 address embedded in the source IPv6 address is invalid.

自动隧道中的IPv6源地址里内嵌的IPv4地址非法，丢弃报文

The IPv4 address embedded in the destination IPv6 address is invalid.

自动隧道中的IPv6目的地址里内嵌的IPv4地址非法，丢弃报文

IPv6 destination address is not a 6to4 address.

6to4隧道加封装时获取的IPv6目的地址前缀不是2002::

IPv6 destination address is not an IPv4-compatible IPv6 address

IPv4兼容IPv6自动隧道加封装时获取到的目的地址不是兼容地址

Failed to forward the IPv4 packet.

加封装后的IPv4报文发送失败

No tunnel in the physical state of up was found for the packet. Dropped the packet.

出隧道报文解封装时找不到对应的、物理状态up的隧道接口

表1-5 debugging tunnel4 packet命令输出信息描述表

字段

描述

Tunnel*num* packet: Before encapsulation according to adjacency table,

*[source*-\>*destination* (length = *length*)]

隧道Tunnel*num*：根据邻接表加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before encapsulation according to fast-forwarding table,

*[source*-\>*destination* (length = *length*)]

隧道Tunnel*num*：根据快转表加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: After encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：加封装后，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Fast forwarded the encapsulated packet.

快速转发加封装后的报文

Failed to fast forward the encapsulated packet.

快转加封装后的报文失败

Before de-encapsulation, *source*-\>*destination* (length = *length*)

解封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before de-encapsulation according to fast-forwarding table, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：根据快转表解封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: After de-encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：解封装后，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Discarded compatible address packet.

丢弃含有IPv4兼容IPv6地址的IPv6报文

【举例】

\# 打开本端的IPv4 Tunnel错误调试信息开关。创建隧道接口，但没有配置源地址时，打印如下调试信息。

\<Sysname\> debugging tunnel4 error

\*Mar 29 09:16:07:928 2011 Sysname TUNNEL4/7/error: -MDC=1;

 Tunnel1 status check: Source address is not set.

*// 隧道Tunnel1状态检查：没有配置源地址*

\# 打开本端的IPv4 Tunnel报文调试信息开关。在两台设备之间建立IPv4 over IPv4隧道，并分别配置参数使隧道接口up。在本端设备上ping对端设备，本端设备上将打印如下调试信息。

\<Sysname\> debugging tunnel4 packet

\<Sysname\> ping -c 1 -a 10.1.1.1 10.1.3.1

PING 10.1.3.1 (10.1.3.1) from 10.1.1.1: 56 data bytes

56 bytes from 10.1.3.1: icmp_seq=0 ttl=255 time=1.000 ms

\-\-- 10.1.3.1 ping statistics \-\--

1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss

round-trip min/avg/max/stddev = 1.000/1.000/1.000/0.000 ms

Sysname

\*Sep  6 11:56:35:242 2011 Sysname TUNNEL4/7/packet: -MDC=1;

 Tunnel0 packet: Before encapsulation according to adjacency table,

   10.1.1.1-\>10.1.3.1 (length = 84)

*// 根据邻接表加封装前，报文的源IP地址为10.1.1.1，目的IP地址为10.1.3.1，报文长度为84字节*

\*Sep  6 11:56:35:242 2011 Sysname TUNNEL4/7/packet: -MDC=1;

 Tunnel0 packet: After encapsulation,

   1.1.1.1-\>1.1.1.2 (length = 104)

*// 加封装后，报文的源IP地址为1.1.1.1，目的IP地址为1.1.1.2，报文长度为104字节*

\*Sep  6 11:56:35:242 2011 Sysname TUNNEL4/7/packet: -MDC=1;

 Tunnel0 packet: Fast forwarded the encapsulated packet.

*// 根据快转表项快速转发封装后的报文*

\*Sep  6 11:56:35:243 2011 Sysname TUNNEL4/7/packet: -MDC=1;

 Tunnel0 packet: Before de-encapsulation according to fast-forwarding table,

   1.1.1.2-\>1.1.1.1 (length = 104)

*// 接收到的报文根据快转表项解封装前，源IP地址为1.1.1.2，目的IP地址为1.1.1.1，报文长度为104字节*

\*Sep  6 11:56:35:243 2011 Sysname TUNNEL4/7/packet: -MDC=1;

 Tunnel0 packet: After de-encapsulation,

   10.1.3.1-\>10.1.1.1 (length = 84)

*// 接收到的报文解封装后，源IP地址为10.1.3.1，目的IP地址为10.1.1.1，报文长度为84字节*

**隧道 \-- 隧道调试命令 \-- debugging tunnel6**

------------------------------------------------------------------------

【命令】

**[debugging tunnel6**[ { **all** \| **error** \| **packet** } [ **interface tunnel** *interface-number* ]]]

**[undo debugging tunnel6**[ { **all** \| **error** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IPv6 Tunnel所有调试信息开关。

**[error**]：表示IPv6 Tunnel错误调试信息开关。

**[packet**]：表示IPv6 Tunnel报文调试信息开关。

**[interface tunnel** *interface-number*]：表示指定Tunnel接口进行调试。

【描述】

**[debugging tunnel6**]命令用来打开IPv6 Tunnel的调试信息开关。**undo debugging tunnel6**命令用来关闭IPv6 Tunnel的调试信息开关。

缺省情况下，IPv6 Tunnel的调试信息开关处于关闭状态。

IPv6 Tunnel指的是外层传输协议为IPv6协议的隧道。

表1-6 debugging tunnel6 error命令输出信息描述表

字段

描述

Tunnel*num* status check: Source address is not set.

隧道Tunnel*num*状态检查：源地址没有配置

Tunnel*num* status check: Destination address is not set.

隧道Tunnel*num*状态检查：目的地址没有配置

Tunnel*num* status check: Source address is not the address of a local interface.

隧道Tunnel*num*状态检查：源地址不是本设备接口的地址

Tunnel*num* status check: Failed to get FIB information of the source address.

隧道Tunnel*num*状态检查：获取源地址FIB信息失败

Tunnel*num* status check: Destination address should not be the address of a local interface.

隧道Tunnel*num*状态检查：目的地址不能是本设备接口的地址

Tunnel*num* status check: Failed to get FIB information of the destination address.

隧道Tunnel*num*状态检查：获取目的地址FIB信息失败

The protocol state of Tunnel*num* is not up. Dropped the packet.

待解封装报文出隧道时发现相应隧道接口协议状态不是up的，报文被丢弃

Tunnel*num*: The information obtained from the adjacency table is invalid.

隧道Tunnel*num*：邻接表信息非法

Tunnel*num*: The passenger protocol number *number* is not supported.

隧道Tunnel*num*：不支持乘客协议*protocol-number*

Failed to forward the IPv6 packet.

加封装后的IPv6报文发送失败

No tunnel in the physical state of up was found for the packet. Dropped the packet.

出隧道报文解封装时找不到对应的、物理状态up的隧道接口

表1-7 debugging tunnel6 packet命令输出信息描述表

字段

描述

Tunnel*num* packet: Before encapsulation according to adjacency table,

*[source*-\>*destination* (length = *length*)]

隧道Tunnel*num*：根据邻接表加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before encapsulation according to fast-forwarding table,

*[source*-\>*destination* (length = *length*)]

隧道Tunnel*num*：根据快转表加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: After encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：加封装后，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Fast forwarded the encapsulated packet.

快速转发加封装后的报文

Failed to fast forward the encapsulated packet.

快转加封装后的报文失败

Before de-encapsulation, *source*-\>*destination* (length = *length*)

解封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before de-encapsulation according to fast-forwarding table, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：根据快转表解封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: After de-encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*：解封装后，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Discarded compatible address packet.

丢弃含有IPv4兼容IPv6地址的IPv6报文

【举例】

\# 打开本端的IPv6 Tunnel错误调试信息开关。创建隧道接口，但没有配置源地址时，打印如下调试信息。

\<Sysname\> debugging tunnel6 error

\*Mar 29 09:17:07:928 2011 Sysname TUNNEL6/7/error: -MDC=1;

 Tunnel1 status check: Source address is not set.

*// 隧道Tunnel1状态检查：没有配置源地址*

\# 打开本端的IPv6 Tunnel报文调试信息开关。在两台设备之间建立IPv6 over IPv6隧道，并分别配置参数使隧道接口up。在本端设备上ping对端设备，本端设备上将打印如下调试信息。

\<Sysname\> debugging tunnel6 packet

\<Sysname\> ping ipv6 -c 1 -a 3::1 5::1

PING6(56 data bytes) 3::1 \--\> 5::1

56 bytes from 5::1, icmp_seq=0 hlim=64 time=2.000 ms

\-\-- 5::1 ping6 statistics \-\--

1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 2.000/2.000/2.000/0.000 ms

\<Sysname\>

\*Sep  6 12:05:12:296 2011 Sysname TUNNEL6/7/packet: -MDC=1;

 Tunnel1 packet: Before encapsulation,

   3::1-\>5::1 (length = 104)

*// 报文加封装前，源IPv6地址为3::1，目的IPv6地址为5::1，报文长度为104字节*

\*Sep  6 12:05:12:296 2011 Sysname TUNNEL6/7/packet: -MDC=1;

 Tunnel1 packet: After encapsulation,

   1::1-\>1::2 (length = 144)

*// 报文加封装后，源IPv6地址为1::1，目的IPv6地址为1::2，报文长度为144字节*

\*Sep  6 12:05:12:296 2011 Sysname TUNNEL6/7/packet: -MDC=1;

 Tunnel1 packet: Failed to fast forward the encapsulated packet.

*// 没有找到封装后报文对应的快转表项，快转失败*

\*Sep  6 12:05:12:297 2011 Sysname TUNNEL6/7/packet: -MDC=1;

 Tunnel1 packet: Before de-encapsulation according to fast-forwarding table,

   1::2-\>1::1 (length = 144)

*// 根据快转表项解封装前，报文的源IPv6地址为1::2，目的IPv6地址为1::1，报文长度为144字节*

\*Sep  6 12:05:12:297 2011 Sysname TUNNEL6/7/packet: -MDC=1;

 Tunnel1 packet: After de-encapsulation,

   5::1-\>3::1 (length = 104)

*// 报文解封装后，源IPv6地址为5::1，目的IPv6地址为3::1，报文长度为104字节*
