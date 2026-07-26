
**DDR \-- DDR调试命令 \-- debugging dialer**

------------------------------------------------------------------------

【命令】

**[debugging dialer**[ { **all** \| **event** \| **packet** }]]

**[undo debugging dialer**[ { **all** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DDR所有调试信息开关。

**[event**]：表示DDR事件调试信息开关。

**[packet**]：表示DDR报文调试信息开关。

【描述】

**[debugging dialer**]命令用来打开DDR调试信息开关。**undo** **debugging dialer**命令用来关闭DDR调试信息开关。

缺省情况下，DDR调试信息开关处于关闭状态。

表1-1 debugging dialer event命令输出信息描述表

字段

描述

Call up on interface *interface-name*

接口上的呼叫up，即呼叫建立

Config interface

配置接口，使用此接口配置进行协商

Call direction

呼叫方向，入呼叫call in；出呼叫call out

Calling number

主叫号码，入呼叫时有效

Call down on interface *interface-name*

接口上的呼叫down，即呼叫拆除

Link up on interface *interface-name*

接口上的链接up，即链接建立

Peer address

对端地址

Link down on interface *interface-name*

接口上的链接down，即链接拆除

Map info:

  Interface: *interface-name*

  Map type: *type*

  NextHop: *nexthop*

  Mask: *mask*

  VPN instance: *vpnindex*

  Broadcast: *broadcast*

map表项信息：

·Interface：map所属接口

·Map type：map类型，包括pppoec、dialer number、static（静态map）、dynamic（动态map）

·NextHop：目的地址

·Mask：目的地址掩码

·VPN instance：VPN索引

·Broadcast：广播属性，1广播；0单播

Diagnose timer timed out on interface *interface-name*, and link disconnected.

接口上诊断定时器超时，拆除呼叫

Enable timer timed out on interface *interface-name*.

接口上使能定时器超时

Wait-carrier timer timed out on interface *interface-name*, and call disconnected.

接口上等待载波定时器超时，拆除呼叫

Wait-nego timer timed out on interface *interface-name*, and link disconnected.

接口上等待协商定时器超时，拆除链接

Routing-disable timer timed out on interface *interface-name*, and standby link disconnected.

接口上的备份链路延迟断开定时器超时，拆除备份链接

Disconnecting link-call on interface *interface-name*.

拆除接口上的链接呼叫

Link negotiation up on interface *interface-name*.

接口上链路层链路协商up

Link negotiation down on interface *interface-name*.

接口上链路层链路协商down

Link network up on interface *interface-name*.

接口上链路层网络协商up

Link network down on interface *interface-name*.

接口上链路层网络协商down

Received a disconnect indication on interface *interface-name*, with user ID *userid* and call ID *callid.*

接口上收到呼叫拆除指示，user ID信息，call ID信息

Dialing *called-number* on interface *interface-name*, with user ID *userid*.

接口上发起呼叫，user ID信息

Disconnecting call on interface *interface-name*, with user ID *userid* and call ID *callid*.

接口上拆除呼叫，user ID信息，call ID信息

Received a connect indication on interface *interface-name*, with user ID *userid* and call ID *callid.*

接口上收到出呼叫应答，user ID信息，call ID信息

Callout failed on interface *interface-name*, and call disconnected.

接口上查找出呼叫失败，拆除呼叫

Received a caller *calling-number* on interface *interface-name*, with call ID *callid*.

接口上收到一个入呼叫，call ID信息

The caller *calling-number* should be rejected.

此入呼叫被拒绝

The caller *calling-number* should be allowed.

此入呼叫允许接入

The caller *calling-number* should be called back.

此入呼叫进行回呼

Found a route matching *calling-number*, and started the enable timer to call back.

找到匹配主叫号码的route，启动使能定时器准备回呼

Found no route matching *calling-number*, and callback failed.

没有找到匹配主叫号码的route，回呼失败

The interface *interface-name* is in shutdown state, and dial failed.

接口处于shutdown状态，拨号失败

Standby routing is effective on interface *interface-name*, and dial failed.

接口上路由备份功能生效，拨号失败

No available channel on interface *interface-name*, and competition started.

接口上没有空闲通道，竞争启动

No available channel on interface *interface-name*, and dial failed.

接口上没有空闲通道，拨号失败

Enable timer of interface *interface-name* is effective, and dial failed.

接口上的使能定时器生效，拨号失败

The route has no dialer number, and dial failed.

Route没有配置拨号串，拨号失败

The interface *interface-name* isn\'t a son of interface *interface-name*, and dial failed.

接口之间没有父子关系，拨号失败

Found a matching map on interface *interface-name*, and trying to dial with it.

在接口上找到匹配的map，开始拨号

Enable timer timed out, and performing callback on interface *interface-name*.

使能定时器超时，在接口上回呼

Idle timer timed out on interface *interface-name*, and link disconnected.

接口上的空闲定时器超时，拆除链接

Auto dial timer timed out, and trying to dial on interface *interface-name*.

自动拨号定时器超时，在接口上拨号

Found free channel on interface *interface-name*, and trying to dial with it.

接口上找到空闲通道，发起呼叫

The interface *interface-name* is in shutdown state, and call-in failed.

接口处于shutdown状态，入呼叫失败

Standby routing is effective on interface *interface-name*, and call-in failed.

接口上动态路由备份生效，入呼叫失败

User authentication failed, and link disconnected.

对端用户验证失败，拆除链接

Peer address authentication failed, and disconnect the link.

对端地址验证失败，拆除链接

Creating dynamic map failed.

创建动态map失败

Link has already been disconnected.

链接已经拆除

Link already up.

链接已经up

Peer address conflict, disconnect the link.

对端地址冲突，拆除链接

ACL created, match dialer-group *group-number* rule, and updated ACL number to a valid value.

ACL创建，匹配dialer-group rule，更新ACL number为有效值

ACL deleted, match dialer-group *group-number* rule, and updated ACL number to an invalid value.

ACL删除，匹配dialer-group rule，更新ACL number为无效值

Warmup timer timed out. Standby routing started.

动态路由备份功能启动定时器超时，启动路由备份

The route of standby routing-group *group-number* is up.

动态路由备份监控组的路由up

The route of standby routing-group *group-number* is down.

动态路由备份监控组的路由down

Refresh wadj: interface = *interface-name*, nexthop = *nexthop*, result = *result*

  Peer Address: *peer*

  Phy interface: *interface-name*

  VA interface: *interface-name*

  MTU: *mtu*

  Slot: *slot*

添加邻接表

·interface：路由接口

·nexthop：下一跳

·result：0成功，非0失败

·Peer Address：对端地址

·Phy interface：物理接口

·VA interface：虚拟接口

·MTU：mtu

·Slot：槽号

Delete wadj: interface = *interface-name*, nexthop = *nexthop*, result = *result*

删除邻接表

·interface：路由接口

·nexthop：下一跳

·result：0成功，非0失败

表1-2 debugging dialer packet命令输出信息描述表

字段

描述

Sending interesting unicast packet out of interface *interface-name*, nexthop is *nexthop*

在接口上发送感兴趣单播报文

Sending uninteresting unicast packet out of interface *interface-name*, nexthop is *nexthop*

在接口上发送非感兴趣单播报文

Sending interesting broadcast packet out of interface *interface-name.*

在接口上发送感兴趣广播报文

Sending uninteresting broadcast packet out of interface *interface-name.*

在接口上发送非感兴趣广播报文

There is no matching map on interface *interface-name*, and discard packet.

在接口上没有匹配的map表项，报文丢弃

Find an up link on interface *interface-name*, and send the packet.

在接口上找到一条处于up状态的链路，发送报文

Find a connecting link. Please wait.

链接正在建立，请等待

There is not a matching up link the address. Discard the uninteresting packet.

没有找到up的链接，丢弃非感兴趣报文

Enqueue the packet.

报文入缓存队列

Queue is not set. Discard this packet.

没有设置缓冲区! 丢弃报文

Queue is full. Discard this packet.

缓冲区已满! 丢弃报文

Receive interesting packet on interface *interface-name*, whose father interface is *interface-name*.

在接口上收到感兴趣报文，父接口信息

Receive uninteresting packet on interface *interface-name*, whose father interface is *interface-name*.

在接口上收到非感兴趣报文，父接口信息

Find a matching map on interface *interface-name.*

在接口上匹配到map表项

Try to dial on the interface *interface-name.*

在接口上尝试拨号

Link up on interface *interface-name*. Dequeue and send packets.

接口上链接up，报文出队发送

Map down on interface *interface-name*. Dequeue and drop packets.

接口上map down，报文出队丢弃

Map info:

  Interface: *interface-name*

  Map type: *type*

  NextHop: *nexthop*

  Mask: *mask*

  VPN instance: *vpnindex*

  Broadcast: *broadcast*

map表项信息

·Interface：Map所属接口

·Map type：Map类型，包括pppoec、dialer number、static（静态map）、dynamic（动态map）

·NextHop：目的地址

·Mask：目的地址掩码

·VPN instance：VPN索引

·Broadcast：广播属性，1广播；0单播

【举例】

两台设备通过CE1/PRI背靠背相连：

Router A配置：

\#

 dialer-group 1 rule ip permit

\#

controller E1 2/3/0

 pri-set

\#

interface Dialer1

 dialer circular enable

 dialer-group 1

 dialer number 12345678

 ip address 1.2.3.1 255.255.255.0

\#

interface Serial2/3/0:15

 dialer circular-group 1

\#

Router B配置：

\#

 dialer-group 1 rule ip permit

\#

controller E1 2/3/0

 pri-set

\#

interface Dialer1

 dialer circular enable

 dialer-group 1

 ip address 1.2.3.4 255.255.255.0

\#

interface Serial2/3/0:15

 dialer circular-group 1

 isdn protocol-mode network

\#

\# 打开Router A的DDR事件调试信息开关。从Router A ping Router B，调试信息分析如下：

\<RouteA\> debugging dialer event

\<RouteA\> ping 1.2.3.4

Ping 1.2.3.4 (1.2.3.4): 56 data bytes, press CTRL_C to break

\*Dec 14 14:06:34:716 2011 RouteA DDR/7/EVENT:

Found a matching map on interface Dialer1, and trying to dial with it.

*// 在Dialer1接口上找到匹配的map，尝试拨号*

\*Dec 14 14:06:34:716 2011 RouteA DDR/7/EVENT:

Found free channel on interface Serial2/3/0:15, and trying to dial with it.

*// 在Serial2/3/0:15接口上找到空闲通道，尝试拨号*

\*Dec 14 14:06:34:717 2011 RouteA DDR/7/EVENT:

Dialing 12345678 on interface Serial2/3/0:15, with user ID 0.

*// 在Serial2/3/0:15接口上呼叫号码12345678，用户id为0*

\*Dec 14 14:06:34:732 2011 RouteA DDR/7/EVENT:

Received a connect indication on interface Serial2/3/0:15, with user ID 0 and call ID 65535.

*// 在Serial2/3/0:15接口上收到呼叫确认，用户id为0，呼叫id为65535*

\*Dec 14 14:06:34:734 2011 RouteA DDR/7/EVENT:

Call up on interface Serial2/3/0:0

  Config interface: Dialer1

  Call direction: call out

  Calling number:

*// 接口Serial2/3/0:0呼叫up，配置接口为Dialer1，出呼叫，主叫号码为空*

\*Dec 14 14:06:34:748 2011 RouteA DDR/7/EVENT:

Link negotiation up on interface Serial2/3/0:0.

*// 接口Serial2/3/0:0链路协议链路层协商up*

\*Dec 14 14:06:34:763 2011 RouteA DDR/7/EVENT:

Link network up on interface Serial2/3/0:0.

*// 接口Serial2/3/0:0链路协议网络层协商up*

\*Dec 14 14:06:34:764 2011 RouteA DDR/7/EVENT:

Link up on interface Serial2/3/0:0

  Peer address: 1.2.3.4

  Map info:

    Interface: Dialer1

    Map type: dialer number

    NextHop: 0.0.0.0

    Mask: 0.0.0.0

    VPN instance: 0

    Broadcast: 1

*// 接口Serial2/3/0:0链接建立，对端地址为1.2.3.4，对应的map信息：接口为Dialer1接口，类型为dialer number，下一跳为0.0.0.0，掩码为0.0.0.0，VPN索引为0，广播类型为广播*

\*Dec 14 14:06:34:764 2011 RouteA DDR/7/EVENT:

Refresh wadj: interface = Dialer1, nexthop = 1.2.3.4, result = 0x0

  Peer Address: 1.2.3.4

  Phy interface: Serial2/3/0:0

  VA interface: N/A

  MTU: 1500

  Slot: 0

*// 添加邻接表成功，接口为Dialer1，下一跳为1.2.3.4，对端地址为1.2.3.4，物理接口为Serial2/3/0:0，VA接口为无效，MTU为1500，所在板号为0*

Request time out

56 bytes from 1.2.3.4: icmp_seq=1 ttl=255 time=25.637 ms

56 bytes from 1.2.3.4: icmp_seq=2 ttl=255 time=25.310 ms

56 bytes from 1.2.3.4: icmp_seq=3 ttl=255 time=25.350 ms

56 bytes from 1.2.3.4: icmp_seq=4 ttl=255 time=25.243 ms

\-\-- Ping statistics for 1.2.3.4 \-\--

5 packet(s) transmitted, 4 packet(s) received, 20.0% packet loss

round-trip min/avg/max/stddev = 25.243/25.385/25.637/0.150 ms

\# 打开Router A的DDR报文调试开关。从Router A ping Router B，调试信息分析如下：

\<RouteA\> debugging dialer packet

\<RouteA\> ping 1.2.3.4

Ping 1.2.3.4 (1.2.3.4): 56 data bytes, press CTRL_C to break

\*Dec 14 14:06:59:080 2011 RouteA DDR/7/PACKET:

Sending interesting unicast packet out of interface Dialer1, nexthop is 1.2.3.4

*[// Dialer1*]*接口上发送感兴趣单播报文，下一跳为1.2.3.4*

\*Dec 14 14:06:59:081 2011 RouteA DDR/7/PACKET:

Find a matching map on interface Dialer1.

  Map info:

    Interface: Dialer1

    Map type: dialer number

    NextHop: 0.0.0.0

    Mask: 0.0.0.0

    VPN instance: 0

    Broadcast: 1

*[// Dialer1*]*接口上找到匹配的map，对应的map信息：接口为Dialer1接口，类型为dialer number，下一跳为0.0.0.0，掩码为0.0.0.0，VPN索引为0，广播类型为广播*

\*Dec 14 14:06:59:081 2011 RouteA DDR/7/PACKET:

Try to dial on the interface Dialer1.

  Map info:

    Interface: Dialer1

    Map type: dialer number

    NextHop: 0.0.0.0

    Mask: 0.0.0.0

    VPN instance: 0

    Broadcast: 1

*[// Dialer1*]*接口上尝试拨号，对应的map信息：接口为Dialer1接口，类型为dialer number，下一跳为0.0.0.0，掩码为0.0.0.0，VPN索引为0，广播类型为广播*

\*Dec 14 14:06:59:081 2011 RouteA DDR/7/PACKET:

Queue is not set. Discard this packet.

*// 队列没有设置，报文丢弃*

\*Dec 14 14:06:59:123 2011 RouteA DDR/7/PACKET:

Link up on interface Dialer1. Dequeue and send packets.

  Map info:

    Interface: Dialer1

    Map type: dialer number

    NextHop: 0.0.0.0

    Mask: 0.0.0.0

    VPN instance: 0

    Broadcast: 1

*[// Dialer1*]*接口上链接up，报文出队发送，对应的map信息：接口为Dialer1接口，类型为dialer number，下一跳为0.0.0.0，掩码为0.0.0.0，VPN索引为0，广播类型为广播*

Request time out

56 bytes from 1.2.3.4: icmp_seq=1 ttl=255 time=25.577 ms

56 bytes from 1.2.3.4: icmp_seq=2 ttl=255 time=25.225 ms

56 bytes from 1.2.3.4: icmp_seq=3 ttl=255 time=25.174 ms

56 bytes from 1.2.3.4: icmp_seq=4 ttl=255 time=25.391 ms

\-\-- Ping statistics for 1.2.3.4 \-\--

5 packet(s) transmitted, 4 packet(s) received, 20.0% packet loss

round-trip min/avg/max/stddev = 25.174/25.342/25.577/0.158 ms

\<RouteA\>

\*Dec 14 14:07:01:532 2011 RouteA DDR/7/PACKET:

Receive interesting packet on interface Serial2/3/0:0, whose father interface is Dialer1.

*[// Serial2/3/0:0*]*接口上收到感兴趣报文，父接口为Dialer1接口*

\*Dec 14 14:07:01:758 2011 RouteA DDR/7/PACKET:

Receive interesting packet on interface Serial2/3/0:0, whose father interface is Dialer1.

*[// Serial2/3/0:0*]*接口上收到感兴趣报文，父接口为Dialer1接口*

\*Dec 14 14:07:01:983 2011 RouteA DDR/7/PACKET:

Receive interesting packet on interface Serial2/3/0:0, whose father interface is Dialer1.

*[// Serial2/3/0:0*]*接口上收到感兴趣报文，父接口为Dialer1接口*

