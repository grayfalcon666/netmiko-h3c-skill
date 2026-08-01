<!-- CMD-INDEX
  debugging ipv6 address event        | 用户视图             | L12
  debugging ipv6 error                | 用户视图             | L92
  debugging ipv6 icmp                 | 用户视图             | L162
  debugging ipv6 nd                   | 用户视图             | L260
  debugging ipv6 nd snooping          | 用户视图             | L552
  debugging ipv6 packet               | 用户视图             | L792
  debugging ipv6 pathmtu              | 用户视图             | L1132
  debugging tcp-proxy                 | 用户视图             | L1296
-->

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 address event**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 address event**]

**[undo debugging ipv6 address event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ipv6 address event**]命令用来打开IPv6地址事件的调试信息开关。**undo debugging ipv6 address event**命令用来关闭IPv6地址时间的调试信息开关。

缺省情况下，IPv6地址事件调试信息开关处于关闭状态。

表1-1 debugging ipv6 address event命令输出信息描述表

字段

描述

Event type

事件类型

module

被通知的模块ID

Prefix Len

前缀长度

VPN Index

Vpn索引

Interface

接口名

****

【举例】

\# 在设备上配置IPv6地址事件的调试信息开关，配置接口GigabitEthernet1/0/1的IPv6地址为2012::6664。

\<Sysname\> debugging ipv6 address event

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 ip address 2012::6664

Sysname-GigabitEthernet1/0/1

\*Dec 3 15:13:01:182 2012 Sysname IP6ADDR/7/EVENT: -MDC=1;

IPv6 prefix event type 0x20001 notified to module 0x04040000,

Prefix: 2012::, Prefix Length: 64, VPN Index: 0, Interface: GigabitEthernet1/0/1

\*Dec 3 15:13:01:381 2012 Sysname IP6ADDR/7/EVENT: -MDC=1;

IPv6 address event type 0x10001 notified to module 0x04040000,

Prefix 2012::66, Prefix Length: 64, VPN Index: 0, Interface: GigabitEthernet1/0/1

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 error**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 error**]

**[undo debugging ipv6 error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ipv6 error**]命令用来打开IPv6报文的错误调试信息开关。**undo debugging ipv6 error**命令用来关闭IPv6报文的错误调试信息开关。

缺省情况下，IPv6报文的错误调试信息开关处于关闭状态。

表1-2 debugging ipv6 error命令输出信息描述表{.TableHeadingChar}

字段

描述

Number of IPv6 fragments exceeded the threshold.

分片报文的数量超过了限制

Number of IPv6 reassembly queues exceeded the threshold.

重组队列的数量超过了限制

Invalid IPv6 packet.

IPv6报文非法

Failed to process the hop-by-hop extension header.

处理报文中逐跳扩展头失败

Failed to process the hop-by-hop option.

处理报文中逐跳选项失败

The packet was discarded by services.

业务禁止报文

The packet was administratively discarded.

IPv6报文被管理禁止

【举例】

\# 在一台支持IPv6功能并在接口下配置IPv6地址的设备上打开IPv6报文的错误调试信息开关，设备收到很多分片报文。

\<Sysname\> debugging ipv6 error

\*Aug  4 01:42:06:375 2010 Sysname IP6FW/3/debug_error:

Number of IPv6 fragments exceeded the threshold. Interface is GigabitEthernet1/0/1

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 icmp**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging ipv6 icmp**]

**[undo debugging ipv6 icmp**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging ipv6 icmp** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging ipv6 icmp** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging ipv6 icmp** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging ipv6 icmp** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的ICMPv6调试信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的ICMPv6调试信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ICMPv6调试信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的ICMPv6调试信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ICMPv6调试信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的ICMPv6调试信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ICMPv6调试信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的ICMPv6调试信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ICMPv6调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的ICMPv6调试信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的ICMPv6调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【描述】

**[debugging ipv6 icmp**]命令用来打开ICMPv6调试信息开关。**undo debugging ipv6 icmp**命令用来关闭ICMPv6调试信息开关。

表1-3 debugging ipv6 icmp命令输出信息描述表

字段

描述

ICMP6 Output

发送报文的操作

ICMP6 Input

接收报文的操作

src

报文源地址

dst

报文目的地址

type

ICMPv6消息的类型

code

ICMPv6消息的代码，可将某一类型的ICMPv6消息细分为更具体的用途

【举例】

\# 打开ICMPv6调试信息开关，收到ICMPv6报文时输入下列调试信息。

\<Sysname\> debugging ipv6 icmp

\*Dec 24 18:07:49:132 2010 Sysname SOCKET/7/ICMPv6:

ICMP6 Input:

 ICMPv6 Packet: src = 2222::1234, dst = 2222::2222

                type = 128, code = 0 (echo-request)

*// 接收ICMPv6报文*

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 nd**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 nd **[{ **entry** \| **error** \| **packet** }]]

**[undo debugging ipv6 nd **[{ **entry** \| **error** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[entry**]：表示邻居发现的表项信息开关。

**[error**]：表示邻居发现的错误信息开关。

**[packet**]：表示邻居发现的报文信息开关。

【描述】

**[debugging ipv6 nd**]命令用来打开邻居发现的调试信息开关。**undo debugging ipv6 nd**命令用来关闭邻居发现的调试信息开关。

缺省情况下，邻居发现的调试信息开关处于关闭状态。

表1-4 debugging ipv6 nd packet命令输出信息描述表

字段

描述

Sent *packet-type* to *ipv6-address* from interface *interface-type interface-number*

从接口*interface-type interface-number*发送到*ipv6-address*的*packet-type*的报文

Received *packet-type* from *ipv6-address* on interface *interface-type interface-number*

从接口*interface-type interface-number*接收到来自*ipv6-address*的*packet-type *的消息

表1-5 debugging ipv6 nd entry命令显示信息描述表

字段

描述

Added neighbor-state NB entry: ipv6-address on interface-type interface-number

·{.TableTextChar}[添加邻居地址为ipv6-address]{.TableTextChar}的邻居表项，邻居状态为neighbor-state{.TableTextChar}，与该邻居相邻的接口为interface-type interface-number{.TableTextChar}

邻居状态：

·INCMP：正在解析地址，邻居的链路层地址尚未确定；

·正在解析地：邻居可达；

·STALE：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居；

·DELAY：未确定邻居是否可达，延迟一段时间发送邻居请求报文；

·PROBE：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性；

neighbor-state1-\>neighbor-state2: ipv6-address on interface-type interface-number

邻居表项的状态从neighbor-state1转换为neighbor-state2

Deleted neighbor-state NB entry: ipv6-address on interface-type interface-number

·{.TableTextChar}[删除邻居地址为ipv6-address]{.TableTextChar}的邻居表项，邻居状态为neighbor-state{.TableTextChar}，与该邻居相邻的接口为interface-type interface-number{.TableTextChar}

邻居状态：

·INCMP：正在解析地址，邻居的链路层地址尚未确定；

·正在解析地：邻居可达；

·STALE：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居；

·DELAY：未确定邻居是否可达，延迟一段时间发送邻居请求报文；

·PROBE：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性；

表1-6 debugging ipv6 nd error命令显示信息描述表

字段

描述

Packet discarded for hop limit is invalid: packet-type on ipv6-address

·{.TableTextChar}[报文类型为packet-type]{.TableTextChar}，源地址为ipv6-address{.TableTextChar}的报文被丢弃，因为报文的跳段数限制不合法{.TableTextChar}

报文类型：

·RS：路由器请求消息报文

·RA：路由器宣告消息报文

·FINAL RA：路由器宣告消息的最终报文

·NS：邻居请求消息报文

·NA：邻居宣告消息报文

Packet discarded for source address is unspecified and destination address is not solicited multicast: packet-type on ipv6-address

报文类型为packet-type,源地址为ipv6-address的报文被丢弃，因为报文的源地址不合法，目的地址非组播地址

Packet discarded for source address is unspecified and SLLA is included: packet-type on ipv6-address

报文类型为packet-type,源地址为ipv6-address的报文被丢弃，因为报文未指定源地址而且报文包含了SLLA

Packet discarded for target address is tentative: packet-type on ipv6-address

报文类型为packet-type, 目标地址为ipv6-address的报文被丢弃，因为目标地址未生效

Packet discarded for source addres is error: packet-type on ipv6-address

报文类型为packet-type,源地址为ipv6-address的报文被丢弃，因为源地址错误

Packet discarded for source addres is error: packet-type on ipv6-address

报文类型为packet-type,目的地址为ipv6-address的报文被丢弃，因为目的地址错误

Packet discarded for option is error: packet-type on ipv6-address

报文类型为packet-type,源地址为ipv6-address的报文被丢弃，因为报文中携带的选项错误

Packet discarded for target address is a multicast address: packet-type on ipv6-address

报文类型为packet-type,目标地址为ipv6-address的报文被丢弃，因为目标地址是组播

Packet discarded for destination address is a multicast address but S flag is set: packet-type on ipv6-address

报文类型为packet-type,目的地址为ipv6-address的报文被丢弃，因为目的地址是组播但是S标记设置为1

Packet discarded for target address is error: packet-type on ipv6-address

报文类型为packet-type,目标地址为ipv6-address的报文被丢弃，因为目标地址错误

Packet discarded for no TLLA is included: packet-type on ipv6-address

报文类型为packet-type,目标地址为ipv6-address的报文被丢弃，因为目标中没有携带TLLA选项

Packet discarded for including invalid TLLA:packet-type on ipv6-address

报文类型为packet-type,目标地址为ipv6-address的报文被丢弃，因为携带无效的TLLA选项

Packet discarded for including invalid SLLA: packet-type on ipv6-address

报文类型为packet-type,源地址为ipv6-address的报文被丢弃，因为报文内的SLLA不合法

Packet discarded for getting extend header failed: packet-type on ipv6-address

报文类型为packet-type,源地址为ipv6-address的报文被丢弃，因为获取报文的扩展头失败

Packet discarded for target address is not this router: packet-type on ipv6-address

报文类型为packet-type,目标地址为ipv6-address的报文被丢弃，因为目标地址不是本路由器的

Packet could not send for target address is error: packet-type on ipv6-address

报文类型为packet-type,目标地址为ipv6-address的报文无法发送，因为目标地址错误

Packet discarded for interface index is invalid

报文丢弃：接口索引无效

Packet discarded for VLAN ID is invalid

报文丢弃：VLAN id无效

Packet discarded for VLAN is not allowed on the port

报文丢弃：VLAN不允许通过

Packet discarded for port is down

报文丢弃：端口down

Packet discarded for STP state of the port is not forwarding

报文丢弃：端口STP状态不是forwarding

Packet discarded for port is a link aggregatioin member

报文丢弃：端口是聚合成员口

Packet discarded for interface is a link aggregation member

报文丢弃：接口是聚合成员口

Updating entry failed for port is not a local interface

报文丢弃：非本板接口

Updating entry failed for conflicting with static configuration

与静态配置冲突，更新表项失败

Sending syn message failed

发送同步消息失败

Syn entry failed for interface is down

同步表项失败：接口down

Syn entry failed for port is down

同步表项失败：端口down

Syn entry failed for VLAN is not allowed on the port

同步表项失败：VLAN不允许通过

Syn entry failed for maximum number of entires is reached.

同步表项失败：表项个数达到上限

Syn entry failed for interface is a link aggregaton member

同步表项失败：接口是聚合成员口

Syn entry failed for port is a link aggregation member

同步表项失败：端口是聚合成员口

Syn entry failed for conflicting with static configuration

同步表项失败：与静态配置冲突

【举例】

\# 在一台支持IPv6功能并在接口下配置IPv6地址的设备上打开IPv6的邻居状态和邻居消息的调试信息开关，并执行ping操作。

\<Sysname\> debugging ipv6 nd packet

\<Sysname\> debugging ipv6 nd entry

\<Sysname\> ping ipv6 --c 1 1::2

   PING 1::2 : 56  data bytes, press CTRL_C to break

\*Aug  4 01:13:02:703 2006 Sysname ND/7/ND_ENTRY:

 Added INCOMPLETE NB entry: 1::2 on interface GigabitEthernet1/0/1

*// 添加状态为INCOMPLETE的邻居表项。*

\*Aug  4 01:13:02:704 2006 Sysname ND/7/ND_PACKET:

 Sent NS to FF02::1:FF00:2, from interface GigabitEthernet1/0/1

*// 向地址FF02::1:FF00:2发送邻居请求消息。*

\*Aug  4 01:13:02:707 2006 Sysname ND/7/ND_PACKET:

 Received NA from 1::2, on interface GigabitEthernet1/0/1

*// 接收到来自1::2的邻居应答消息。*

\*Aug  4 01:13:02:708 2006 Sysname ND/7/ND_ENTRY:

 INCOMPLETE-\>REACHABLE : 1::2 on interface GigabitEthernet1/0/1

*// 表项的状态从INCOMPLETE转换为REACHABLE。*

    Reply from 1::2

    Bytes=56 Sequence=1 Hop limit=64  Time = 8 ms

  \-\-- 1::2 ping6 statistics \-\--

\# 设备上接收到错误的报文。

\<Sysname\> debugging ipv6 nd error

\<Sysname\>\*Nov 16 23:32:45:642 2012 Sysname ND/7/ND_ERROR:

 Packet discarded for hop limit is invalid:  RS on 1::3

*// 接收RS报文的跳数错误，报文被丢弃。*

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 nd snooping**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 nd snooping**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging ipv6 nd snooping**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示ND Snooping的所有调试信息开关。

**[error**]：表示ND Snooping的错误调试信息开关。

**[event**]：表示ND Snooping的事件调试信息开关。

**[packet**]：表示ND Snooping的报文调试信息开关。

【描述】

**[debugging ipv6 nd snooping**]命令用来打开ND Snooping的调试信息开关。**undo debugging ipv6 nd snooping**命令用来关闭ND Snooping的调试信息开关。

缺省情况下，ND Snooping的调试信息开关处于关闭状态。

表1-7 debugging ipv6 nd snooping error命令输出信息描述表

字段

描述

Failed to send packet in vlan *vlan-id*.

在vlan *vlan-id*内发送报文失败

****

表1-8 debugging ipv6 nd snooping event命令输出信息描述表

字段

描述

The number of ND snooping entries on the device has reached the maximum.

ND Snooping表项总数已达到最大规格

The number of ND snooping entries on the interface *interface-type interface-number* has reached the maximum.

端口*interface-type interface-number*下的ND Snooping表项总数已达到最大规格{.TableTextChar}

ND snooping successfully notified the user mode.

ND Snooping通知用户状态成功

ND snooping failed to notify the user mode.

ND Snooping通知用户状态失败

ND snooping synchronization channel between the kernel mode and the user mode disconnected.

ND Snooping内核与用户状态的同步通道断开

ND snooping packet synchronization channel between the LPU kernel mode and the MPU kernel mode disconnected.

ND Snooping接口板内核与主控板内核的报文同步通道断开

IPv6 address

IPv6地址

First VLAN ID

外层VLAN编号

Second VLAN ID

内层VLAN编号

Valid port

生效的入端口

Tentative port

待验证的接入端口

MAC address

MAC地址

Tentative MAC address

待验证的MAC地址

Status changed from *old-status* to *new-status*.

状态由*old-status*迁至*new-status*。

其中*old-status*、* new-status*可选的状态包括：

NO_BIND、TENTATIVE、TESTING_TPLT、VALID、

TESTING_VP

表1-9 debugging ipv6 nd snooping packet命令输出信息描述表

字段

描述

Packet not processed by ND snooping.

ND Snooping无需处理此报文

Received *packet-type* packet.

接收到*packet-type*报文。*packet-type*可以是：

·DAD NS：重复地址检测的Neighbor Solicitation报文

·NS：Neighbor Solicitation报文

·NA：Neighbor Advertisement报文

·DATA：数据报文

Sent packet from *source*.

将报文从*source*发送出去。其中*source*可以是TP(信任

端口)、VP(非信任端口)和VLAN这三者间的组合

Interface

生效的接入端口

First VLAN ID

外层VLAN 编号

Second VLAN ID

内层VLAN编号

IPv6 address

IPv6地址

MAC address

MAC地址

【举例】

\# 打开ND Snooping报文调试信息开关，用户从接口GigabitEthernet1/0/2侧上线。

\<Sysname\> debugging ipv6 nd snooping all

*// 设备收到DAD NS报文。*

\*Jan  7 20:07:33:140 2013 H3C ND/7/ND SNOOPING PACKET:

 Received DAD NS packet.

\*Jan  7 20:07:33:140 2013 H3C ND/7/ND SNOOPING EVENT:

 Information about ND snooping entry:

   IPv6 address: fe80::2e0:7fff:fe68:5e78

   First VLAN ID: 1   Second VLAN ID: 0

   Valid port: GE1/0/2

   Tentative port: N/A

   MAC address: 00e0-7f68-5e78

   Tentative MAC address: 0000-0000-0000

   Status changed from NO_BIND to TENTATIVE.

*// 设备从信任口发送2个DAD NS报文。*

\*Jan  7 20:07:33:141 2013 H3C ND/7/ND SNOOPING PACKET:

 Sent DAD NS packet from TP.

 Information about ND snooping entry:

   Interface:GE1/0/2           First VLAN ID: 1   Second VLAN ID: 0

   IPv6 address: fe80::2e0:7fff:fe68:5e78    MAC address: 00e0-7f68-5e78

\*Jan  7 20:07:33:392 2013 H3C ND/7/ND SNOOPING PACKET:

 Sent DAD NS packet from TP.

 Information about ND snooping entry:

   Interface:GE1/0/2           First VLAN ID: 1   Second VLAN ID: 0

   IPv6 address: fe80::2e0:7fff:fe68:5e78    MAC address: 00e0-7f68-5e78

\*Jan  7 20:07:33:640 2013 H3C ND/7/ND SNOOPING EVENT:

 Information about ND snooping entry:

   IPv6 address: fe80::2e0:7fff:fe68:5e78

   First VLAN ID: 1   Second VLAN ID: 0

   Valid port: GE1/0/2

   Tentative port: N/A

   MAC address: 00e0-7f68-5e78

   Tentative MAC address: 0000-0000-0000

   Status changed from TENTATIVE to VALID.

*[// ND Snooping*]*通知用户状态成功。*

\*Jan  7 20:07:33:640 2013 H3C ND/7/ND SNOOPING EVENT:

 ND snooping successfully notified the user mode.

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 packet**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 packet** [ **acl6** *acl6-number* ]]

**[undo debugging ipv6 packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl6 ***acl6-number*]：输出通过指定访问控制列表过滤的IPv6报文调试信息。*acl6-number*表示ACL的序号，取值范围为2000～3999。

【描述】

**[debugging ipv6 packet**]命令用来打开IPv6报文的调试信息开关。**undo debugging ipv6 packet**命令用来关闭IPv6报文的调试信息开关。

缺省情况下，IPv6报文的调试信息开关处于关闭状态。

表1-10 debugging ipv6 packet命令输出信息描述表{.TableHeadingChar}

字段

描述

Discarding

丢弃报文的操作

Sending

发送报文的操作

Receiving

接收报文的操作

Delivering

IP层将报文送到上层

Transferring

透传报文的操作或把报文提交给其它模块的操作

LocalSending

本机发送报文的操作

interface

接收/发送报文的接口

version

IP协议版本号

traffic class

通信流类别

flow label

流标签

payload length

有效载荷长度

protocol

下一个报头

hop limit

跳数限制

Src

报文源地址

Dst

报文目的地址

Ingress interface did not join the group address.

入接口没有加入该组播组

Sending the packet from local interface *interface-type interface-number*

从本地接口*interface-type interface-number*发送报文

Sending the packet from *interface-type interface-number1* through *interface-type interface-number2*

从*interface-type interface-number1*接受报文后从接口*interface-type interface-number2*发送

Received an IPv6 packet.

接收到IPv6报文

Delivering the IPv6 packet to the upper layer.

将IPv6报文送到上层处理

Invalid next header.

IPv6的下一个扩展头无效

Invalid next header sequence.

IPv6头扩展头顺序错误

Unknown options in the extension header.

扩展头信息里面的选项无法识别

Invalid hop-by-hop header.

逐跳选项头错误

Incorrect format: the hop-by-hop option is after the hop-by-hop extension header.

逐跳选项在逐跳选项扩展头的后面，格式错误

Length of the fragment packet is invalid.

分片报文的报文长度错误

Failed to reassemble fragments.

分片重组失败

No IPv6 address configured for the interface.

接口上没有IPv6地址

Unknown FIB error

未知的FIB错误

Destination is unreachable!

目的不可达

Exceeded hop limits.

报文超过跳数限制

No source IP address specified for forwarding the IPv6 packet.

转发报文时发现源地址没有指定

Invalid source IPv4-compatible address

无效的IPv4兼容源地址

Invalid destination IPv4-compatible address.

无效的IPv4兼容目的地址

Unknown destination

未知的目的

Source address is link local address but destination address is not.

转发报文时发现报文的源地址是链路本地地址而目的地址不是链路本地地址，丢弃报文

Invalid version.

报文版本号错误

Source IPv6 address was a multicast address.

源地址为多播地址

No destination IPv6 address specified

目的地址未指定

The packet was bigger than the MTU.

报文长度大于MTU

Sending the ND packet to a module for managing IPv6 neighbors.

将ND报文送到ND模块处理

Sending the IPv6 packet to the control CPU.

将IPv6报文送到控制核处理

Receiving an IPv6 fragment transported from another slot.

收到从其它板透传过来的IPv6分片报文

Receiving an IPv6 packet transported from another slot.

收到从其它板透传过来的IPv6报文

Jumbo payload option is not supported.

不支持Jumbo选项

Failed to obtain the hop-by-hop extension header.

获取逐跳扩展头失败

Failed to obtain the destination extension header.

获取目的扩展头失败

Failed to obtain the route extension header.

获取路由扩展头失败

Fragments contain overlapped data.

分片报文中数据与其它分片重叠

Failed to obtain fragment extension header.

获取分片扩展头失败

Sending the IPv6 packet to slot *slot-id*.

将IPv6报文送到*slot-id*板处理

Starting multicast forwarding.

开始进行组播转发处理

The packet size is smaller than 40 bytes.

报文长度小于40字节

The destination IPv6 address is a loopback address.

目的地址是环回地址

The source IPv6 address is a loopback address.

源地址是环回地址

The packet payload length cannot be zero.

报文的有效载荷长度不能为0

The packet size is smaller than declared in the packet header.

报文实际长度小于报文头中标识的长度

Sending the IPv6 packet to the MPLS module.

将IPv6报文送到MPLS模块处理

Multicast forwarding the IPv6 packet.

将IPv6报文送到组播转发处理

No source address specified.

本机发送时没有选到源地址

No outbound interface specified for sending the link local packet.

本机发送的链路本地报文没有指定出接口

【举例】

\# 在一台支持IPv6功能并在接口下配置IPv6地址的设备上打开IPv6的报文调试信息开关，并执行ping操作。

\<Sysname\> debugging ipv6 packet

\<Sysname\> ping ipv6 -c 1 1::2

  PING 1::2 : 56  data bytes, press CTRL_C to break

\*Aug  4 01:42:06:375 2010 Sysname IP6FW/7/debug_case:

Sending, interface = GigabitEthernet1/0/1, version = 6, traffic class = 0,

flow label = 0, payload length = 64, protocol = 58, hop limit = 255,

Src = 1::1, Dst = 1::2,

prompt: Sending the packet from local interface GigabitEthernet1/0/1

*// 从接口GigabitEthernet1/0/1发送报文*

\*Aug  4 01:42:06:377 2010 Sysname IP6FW/7/debug_case:

Receiving, interface = GigabitEthernet1/0/1, version = 6, traffic class = 0,

flow label = 0, payload length = 64, protocol = 58, hop limit = 64,

Src = 1::2, Dst = 1::1,

prompt: Received an IPv6 packet.

*// 接收到IPv6报文*

\*Aug  4 01:42:06:378 2010 Sysname IP6FW/7/debug_case:

Delivering, interface = GigabitEthernet1/0/1, version = 6, traffic class = 0,

flow label = 0, payload length = 64, protocol = 58, hop limit = 64,

Src = 1::2, Dst = 1::1,

prompt: Delivering the IPv6 packet to the upper layer.

*// 将接收报文送到上层*

    Reply from 1::2

    bytes=56 Sequence=1 hop limit=64  time = 5 ms

  \-\-- 1::2 ping statistics \-\--

    1 packet(s) transmitted

    1 packet(s) received

    0.00% packet loss

    round-trip min/avg/max = 5/5/5 ms

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 pathmtu**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 pathmtu**]

**[undo debugging ipv6 pathmtu**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ipv6 pathmtu**]命令用来打开IPv6 PMTU的调试信息开关。**undo debugging ipv6 pathmtu**命令用来关闭IPv6 PMTU的调试信息开关。

缺省情况下，IPv6 PMTU的调试信息开关处于关闭状态。

表1-11 {.TableHeadingChar}debugging ipv6 pathmtu命令输出信息描述表{.TableHeadingChar}

字段

描述

VPNIndex

VPN实例索引

IPv6Addr

IPv6地址

EntryType

PMTU表项类型，可能的取值及其含义如下：

·STATIC：表示静态表项

·TOOBIG：表示toobig报文触发添加的动态表项

·SOCKET：表示本机发包触发添加的动态表项

MTU

MTU值

Agetime

老化时间

Adding PMTU entry

添加PMTU表项

The type of the added PMTU entry is wrong

添加的PMTU表项类型错误

Delete PMTU entry

删除PMTU表项

The type of the deleted PMTU entry is wrong

删除的PMTU表项类型错误

Age out PMTU entry

老化PMTU表项

Update agetime

更新老化时间

Delete all static PMTU entries

删除所有静态PMTU表项

Delete all dynamic PMTU entries

删除所有动态PMTU表项

Delete all PMTU entries

删除所有PMTU表项

PMTU entry smoothing started

平滑PMTU表项开始

PMTU entry smoothing finished

平滑PMTU表项结束

Age timer timed out

老化定时器超时

Update epoch value for dynamic PMTU entries

更新动态PMTU表项epoch值

Error message received

收到错误消息

Kernel adding PMTU entry

内核发起添加PMTU表项

Kernel delete PMTU entry

内核发起删除PMTU表项

Adding PMTU entry failed; the maximum number of static PMTU entries has been reached

添加PMTU表项失败，static类型表项达到上限

Adding PMTU entry failed; the maximum number of toobig PMTU entries has been reached

添加PMTU表项失败，toobig类型表项达到上限

Add *number* PMTU entries

添加*number*个PMTU表项

Get *number* PMTU entries

获取*number*个PMTU表项

Binding socket to PMTU succeeded

socket绑定PMTU表项成功

Unbinding PMTU from socket succeeded

socket解除绑定PMTU表项成功

【举例】

\# 打开IPv6的PMTU调试信息开关。

\<Sysname\> debugging ipv6 pathmtu

\# 增加PMTU表项，可以看到如下调试信息。

\<Sysname\> system-view

Sysname ipv6 pathmtu 1::2 1500

\*Sep  9 10:01:02:688 2011 Sysname IP6PMTU/7/IP6PMTU_DBG: -MDC=1; Adding PMTU entry.

 VPNIndex: 0, IPv6Addr: 1::2, EntryType: STATIC, MTU: 1500

*// 添加PMTU表项：VPN实例索引为0，IPv6地址为1::2，静态表项，MTU值为1500*

**IPv6基础 \-- IPv6基础调试命令 \-- debugging tcp-proxy**

------------------------------------------------------------------------

【命令】

**[debugging**[ **tcp-proxy** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

**[undo**[ **debugging** **tcp-proxy** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示TCP代理的所有调试信息开关。

**[error**]：表示TCP代理的错误调试信息开关。

**[event**]：表示TCP代理的事件调试信息开关。

**[fsm**]：表示TCP代理的状态机调试信息开关。

**[packet**]：表示TCP代理的报文调试信息开关。

【描述】

**[debugging** **tcp-proxy**]命令用来打开TCP代理的调试信息开关。**undo** **debugging** **tcp-proxy**命令用来关闭TCP代理的调试信息开关。

缺省情况下，TCP代理的调试信息开关处于关闭状态。

本命令用来打开IPv4 TCP和IPv6 TCP代理的调试信息开关。

表1-12 debugging tcp-proxy error命令输出信息描述表

字段

描述

*addressport*

地址端口信息：

·*sip*/*sport* \--\> *dip*/*dport*：发起方IPv4/IPv6地址/端口号*sip*/*sport*，响应方IPv4/IPv6地址/端口号*dip*/*dport*

·*sip*/*sport -*-\> None：发起方IPv4/IPv6地址/端口号*sip*/*sport*，无响应方

·initial：未指定地址和端口号

 

Failed to connect to IPv4/IPv6* sip*/*sport* on handle \*[addressport*.]

应用程序用句柄（地址端口信息为*addressport*）向IPv4/IPv6的源IP*sip*/源端口*sport*发起连接失败

 

Failed to create new packet for data of *datalen* bytes due to insufficient memory.

由于内存不足，导致创建*datalen*字节的报文失败

 

Failed to erase *overlaplen* bytes of overlapping data from packet *packet*

从报文*packet*中擦除*overlaplen*字节的重叠数据失败

 

Failed to create TCP proxy data block due to insufficient memory.

由于内存不足，导致创建TCP代理数据信息失败

 

Failed to send SYN ACK packet.

发送SYN ACK报文失败

 

Invalid ACK packet. Dropped it.

丢弃无效的ACK报文

 

Can\'t find listening TCP proxy data block for server/client *addressport*.

无法找到服务器/客户端（地址端口信息为*addressport*）的TCP代理监听数据信息

 

Server/Client *addressport* is unable to process *event* event in *state* state.

服务器/客户端（地址端口信息为*addressport*）的不能在状态*state*下处理*event*事件

 

Failed to create data packet on server/client*addressport*.

服务器/客户端（地址端口信息为*addressport*）创建报文失败

 

Failed to send packet.

发送报文失败

 

 TCP packet: src=*sip*/*sport*, dst=*dip*/*dport*

             seq=*seqnum*, ack=*acknum*, flag=*flag*

             win=*winsize*, checksum=*checksum*, datalen=*datalen*, headlen=*headlen*

TCP报文的信息：源IPv4/IPv6地址/端口号*sip*/*sport*，目的IPv4/IPv6地址/端口号*dip*/*dport*，序号*seqnum*，确认序号*acknum*，标志*flag*，窗口大小*winsize*，检验和*checksum*，数据长度*datalen*，首部长度*headlen*

 

表1-13 debugging tcp-proxy event命令输出信息描述表

字段

描述

*addressport*

地址端口信息：

·*sip*/*sport* \--\> *dip*/*dport*：发起方IPv4/IPv6地址/端口号*sip*/*sport*，响应方IPv4/IPv6地址/端口号*dip*/*dport*

·*sip*/*sport -*-\> None：发起方IPv4/IPv6地址/端口号*sip*/*sport*，无响应方

·initial：未指定地址和端口号

 

Application has created a new handle.

应用程序已创建一个新句柄

 

Application is closing handle *addressport*.

应用程序正在关闭一个句柄（地址端口信息为*addressport*）

 

Application is binding handle *addressport* to IPv4/IPv6* sip*/*sport*.

应用程序正在绑定句柄（地址端口信息为*addressport*）到IPv4/IPv6*sip*/*sport*

 

Application is connecting to IPv4/IPv6* sip*/*sport* on handle \*[addressport*.]

应用程序正在用句柄（地址端口信息为*addressport*）向IPv4/IPv6 *sip*/*sport*发起连接

 

Application set handle *addressport* to listening state.

应用程序设置句柄（地址端口信息为*addressport*）进入监听状态

 

Application accepted a new connection on handle *addressport*.

应用程序在句柄（地址端口信息为*addressport*）上获取了一个新连接

 

Application registered readable/writable/error event on handle *addressport*.

应用程序在句柄（地址端口信息为*addressport*）上注册了可读/可写/错误事件

 

Application wanted *datalen* bytes of data, actually received *receivelen* bytes on handle *addressport*.

应用程序期望通过句柄（地址端口信息为*addressport*）接收*datalen*字节数据，实际接收*receivelen*字节

 

Foreign window on handle *addressport* is not enough, declined to send 0 byte.

句柄（地址端口信息为*addressport*）的外部窗口大小不够，拒绝发送0字节数据

 

Application is sending *count* packets on handle *addressport*.

应用程序正在通过句柄（地址端口信息为*addressport*）发送*count*个报文

 

Application received *count* packets on handle *addressport*.

应用程序通过句柄（地址端口信息为*addressport*）接收*count*个报文

 

Server/Client *addressport* received a retransmitted packet and ignored it.

服务器/客户端（地址端口信息为*addressport*）收到重传报文，忽略此报文

 

*[Datalen *bytes of overlapping data has been erased from packet, *packet*]

应用程序已经从报文中擦除*datalen*字节重叠数据，报文信息为*packet*

 

Server/Client *addressport* submitted a pipe writable event to application.

服务器/客户端（地址端口信息为*addressport*）提交一个管道可写事件给应用程序

 

Application ignored a pipe writeable event on server/client *addressport*.

应用程序忽略了句柄服务器/客户端（地址端口信息为*addressport*）上的一个管道可写事件

 

Server/Client *addressport* submitted *datalen* bytes of data to application.

服务器/客户端（地址端口信息为*addressport*）提交*datalen*字节数据给应用程序

 

Application ignored *datalen* bytes of data on server/client *addressport*.

应用程序忽略了句柄服务器/客户端（地址端口信息为*addressport*）上的*datalen*字节数据

 

Server/Client *addressport* state migrated: *state1* -\> *state2*.

服务器/客户端（地址端口信息为*addressport*）状态迁移：*state1*-\> *state2*

 

Server/Client *addressport* submitted a new connection to application.

服务器/客户端（地址端口信息为*addressport*）向应用程序提交一个新连接

 

Application ignored a new connection on server/client *addressport*.

应用程序忽略了句柄服务器/客户端（地址端口信息为*addressport*）上的一个新连接

 

Received an expired ACK packet. Ignored it.

收到一个过期的ACK报文，忽略此报文

 

Server/Client *addressport* submitted a disconnection event to application.

服务器/客户端（地址端口信息为*addressport*）向应用程序提交一个连接关闭事件

 

Application ignored a disconnection event on server/client *addressport*.

应用程序忽略一个来自服务器/客户端（地址端口信息为*addressport*）的连接关闭事件

 

Server/Client *addressport* window size is not enough. Stopped sending packet.

服务器/客户端（地址端口信息为*addressport*）的窗口尺寸不足，停止发送报文

 

表1-14 debugging tcp-proxy fsm命令输出信息描述表

字段

描述

*addressport*

地址和端口的信息：

·*sip*/*sport* \--\> *dip*/*dport*：发起方IPv4/IPv6地址/端口号*sip*/*sport*，响应方IPv4/IPv6地址/端口号*dip*/*dport*

·*sip*/*sport -*-\> None：发起方IPv4/IPv6地址/端口号*sip*/*sport*，无响应方

·initial：未指定地址和端口号

 

Server/Client *addressport* before/after FSM processed *event*

 Info: seq=*expectsendseq*, ack=*expectsendack*, sent ack=*alreadysendack*, received ack=*foreignack*, lwin=*localwin*, fwin=*foreignwin*

 State: *state*.

服务器/客户端（地址端口信息为*addressport*）在状态机处理*event*事件前/后的信息：

本端下次发送的起始序号*expectsendseq*，本端期待发送的确认号*expectsendack*，本端已发出的确认号*alreadysendack*，对端已确认的数据*foreignack*，本端当前窗口大小*localwin*，对端最后一次有效报文通告的窗口大小*foreignwin*，状态*state*。其中：

*[event*]包括：

·SYN

·SYNACK

·FIN

·ACK

·RST

·NONE

·TIMEOUT

*[state*]包括：

·CLSD

·LSTN

·SYNSND

·SYNRCV

·EST

·CLSWT

·FINWT1

·CLSNG

·LSTACK

·FINWT2

·TMWT

 

表1-15 debugging tcp-proxy packet命令输出信息描述表

字段

描述

Received a disordered packet: expected seq=*expectseq*, packet seq=*packetseq*.

收到一个乱序报文，期待的序号*expectseq*，报文实际的序号*packetseq*

Input packet: Time=*time*, total length=*len*

接收报文的时间*time*，报文总长度*len*

Output packet: Time=*time*, total length=*len*

发送报文的时间*time*，报文总长度*len*

Processing disordered packet *packet*

处理乱序报文，报文信息为*packet*

 TCP packet: src=*sip*/*sport*, dst=*dip*/*dport*

             seq=*seqnum*, ack=*acknum*, flag=*flag*

             win=*winsize*, checksum=*checksum*, datalen=*datalen*, headlen=*headlen*

TCP报文的信息：源IPv4/IPv6地址/端口号*sip*/*sport*，目的IPv4/IPv6地址/端口号*dip*/*dport*，序号*seqnum*，确认序号*acknum*，标志*flag*，窗口大小*winsize*，检验和*checksum*，数据长度*datalen*，首部长度*headlen*

【举例】

\# 打开TCP代理错误调试信息开关。

\<Sysname\> debugging tcp-proxy error

\*Jan 16 09:29:23:045 2014 Sysname TCPP/7/FSM: Failed to send packet.

*// 发送报文失败*

\# 打开TCP代理事件调试信息开关。

\<Sysname\> debugging tcp-proxy event

\*Jan 16 09:29:23:075 2014 Sysname TCPP/7/EVENT: -MDC=1; Application is closing a client [5005::5/80\--\>5005::141/45457.]

*// 应用程序正在关闭一个客户端（源IPv6地址/端口号5005::5/80\--\>目的IPv6地址/端口号5005::141/4547）*

\# 打开TCP代理状态机调试信息开关。

\<Sysname\> debugging tcp-proxy fsm

\*Jan 16 09:29:23:076 2014 Sysname TCPP/7/FSM: -MDC=1; Server [5005::5:80\--\>5005::141:45457 before FSM processed ACK]

 Info: seq=0x00b4cc08, ack=0x0e4cbe56, sent ack=0x0e4cbe56, received ack=0x00b4cc07, lwin=65535, fwin=64800

 State: FINWAIT1.

*// 服务器（本端IPv6地址/端口号5005::5/80\--\>对端IPv6地址/端口号5005::141/4547）在状态机处理ACK事件前的信息：本端下次发送的起始序号0x00b4cc08，本端期待发送的确认号0x0e4cbe56，本端已发出的确认号0x0e4cbe56，对端已确认的数据0x00b4cc07，本端当前窗口大小65535，对端最后一次有效报文通告的窗口大小64800，状态FINWAIT1*

\# 打开TCP代理报文调试信息开关。

\<Sysname\> debugging tcp-proxy packet

\*Jan 16 09:29:25:089 2014 Sysname TCPP/7/PACKET: -MDC=1; Input packet: Time=4350167781, total length=572

 TCP packet: src=5005::141/45457, dst=5005::5/80

             seq=0x0e4cbe56, ack=0x00b4cc08, flag=0x18

             win=64800, checksum=0x9cc8, datalen=512, headlen=20

*// 接收报文的时间为4350167781，报文总长度为572。TCP报文的信息：源IPv6地址/端口号5005::141/45457，目的IPv6地址/端口号5005::5/80，序号0x0e4cbe56，确认序号0x00b4cc08，标志0x18，窗口大小64800，检验和0x9cc8，数据长度512，首部长度20*
