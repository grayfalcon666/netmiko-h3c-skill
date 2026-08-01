<!-- CMD-INDEX
  debugging ipv6 netstream event      | 用户视图             | L6
  debugging ipv6 netstream packet     | 用户视图             | L458
-->

**IPv6 NetStream \-- IPv6 NetStream调试命令 \-- debugging ipv6 netstream event**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 netstream event**]

**[undo debugging ipv6 netstream event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ipv6 netstream event**]命令用来打开IPv6 NetStream的事件调试信息开关。

**[undo debugging ipv6 netstream event**]命令用来关闭IPv6 NetStream的事件调试信息开关。

缺省情况下，IPv6 NetStream的事件调试信息开关处于关闭状态。

表1-1 debugging ipv6 netstream event命令输出信息描述表

字段

描述

IPv6 Flow Add to aged list (Statistic Flag *m*, *n* aged flows currently)

添加IP流到老化链表（统计标记位为*m*的当前老化流有*n*条）

IPv6 Flow Add a flow (*n* active flows currently)

增加一个IP流表项（目前总共有*n*个活跃表项）

IPv6 Flow Update a flow

更新一个IP流表项

IPv6 Flow Age a flow  

老化一个IP流表项

IPv6 Flow Age *n* flows (time out)

老化*n*个IP流表项（定时器超时）

IPv6 Flow Age *n* flows (cache overflow)

老化*n*个IP流表项（表项溢出）

IPv6 Flow Age all flows (reset)

老化所有IP流表项（重置）

IPv6 Flow Export a flow

输出一个IP流表项

as Aggre Add a flow (*n* active flows currently)

增加一个AS聚合流表项（目前总共有*n*个活跃表项）

as  Aggre Update a flow

更新一个AS聚合流表项

as Aggre Export *n* flows because aggre cache is full

输出*n*个AS聚合流表项（聚合缓冲区满）

as Aggre Export *n* flows  for timeout

输出*n*个AS聚合流表项（定时器超时）

Add to transmit queue (Current queue length is *n*)

添加一个报文到报文输出队列（目前报文输出队列长度为*n*）

Successfully send  (Current queue length is *n*)

成功发送报文（目前报文输出队列长度为*n*）

Fail to send (Current queue length is *n*)

发送报文失败（目前报文输出队列长度为*n*）

Activate Template (*n* active templates currently)

激活一个模板（目前共有*n*个激活模板):

Deactivate Template (*n* active templates currently)

去激活一个模板（目前共有*n*个激活模板)

Select Template for flow (Version 9 Type)

为普通流表项选择一个v9格式模板

Select Template for aggregate flow (Version 9 Type )

为聚合流表项选择一个v9格式模板

CPU 0 IPv6 Flow       Add a flow (1 active flows currently):

Direction: O Flow Type: IPv6 IP version: 6

InIf: 0 OutIf: 51314696 OutVrf: 0

SrcIP: 1:2::3:4 DstIP: 1:2::3:5 Prot: 58

SrcPort: 0 DstPort: 32768 Tos: 0x0 FlowLabel: 0x0 TcpFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 0 DstMask: 0

NextHop: 1:2::3:5 BGP-NextHop: ::

Label 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: UNKNOWN,  IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVLAN: 0 DstVLAN: 0

First: 0 Last: Pkts: 0  Bytes: 104

Sampling Mode: N/A Sampling Interval: 0

以IP流表项为例，各字段的意义如下：:

·Direction：方向

·Flow Type：流的类型

·IP version：IP版本

·InIf：入接口号

·OutIf：出接口号

·InVrf：入方向报文所属VPN

·OutVrf：出方向报文所属VPN

·SrcIP：源IP地址

·DstIP：目的IP地址

·Prot：协议

·SrcPort：源端口号

·DstPort：目的端口号

·Tos：服务类型

·FlowLabel：流标签

·TcpFlag：TCP标记

·SrcAS：源自治系统号

·DstAS：目的自治系统号

·SrcMask：源掩码

·DstMask：目的掩码

·NextHop：路由下一跳

·BGP-NextHop：BGP下一跳

·Label 1：MPLS一层标签

·Label 2：MPLS二层标签

·Label 3：MPLS三层标签

·TopLabel Type：栈顶标签的类型

·IPv4/IPv6 address：栈顶标签地址

·SrcMAC：源MAC地址

·DstMAC：目的MAC地址

·SrcVLAN：源VLAN ID

·DstVLAN：目的VLAN ID

·First：流的初始活跃时间

·Last：流的最后活跃时间

·Pkts：流的报文数目

·Bytes：流的字节数目

·Sampling Mode：采样模式

·Sampling Interval：采样间隔

CPU 0 as Aggre   Add a flow (*n* active flows currently):

InIf: 0 OutIf: 51314696 SrcAS: 0 DstAS: 0

Direction: O Aggre Type: as  IP version : 6

First: 12381680 Last: 12381680 Flows: 1 Pkts: 1 Bytes: 104

Sampling Mode: N/A Sampling Interval: 0

以AS聚合为例，各字段的意义如下：:

·InIf：入接口号

·OutIf：出接口号

·SrcAS：源自治系统号

·DstAS：目的自治系统号

·Direction：方向

·Aggre Type：聚合类型

·IP version：IP版本

·First：流的初始活跃时间

·Last：流的最后活跃时间

·Flows：聚合统计的流数目

·Pkts：流的报文数目

·Bytes：流的字节数目

·Sampling Mode：采样模式

·Sampling Interval：采样间隔

Received a packet from the driver for statistics, and the packet type is *packet*-*type*.

从驱动接收到一个待统计的报文，报文类型为*packet*-*type*

*[packet-type*]包括：

·IPv6_IPL2：二层转发中的IPv6报文

·IPv6_IPL3：三层转发中的IPv6报文

·IPv6_MPLS：载荷为IPv6的MPLS报文

·IPv6_L2VPN：载荷为IPv6的L2VPN报文

【举例】

\# 在一台设备上端口GigabitEthernet1/0/1使能了IPv6 Netstream入方向统计，配置目的输出主机，使能AS聚合，将表项不活跃老化时间设为10秒，打开IPv6 Netstream事件处理的调试信息开关，当有报文进入端口GigabitEthernet1/0/1并进行Netstream统计时，会有如下调试信息。

\<Sysname\> debugging ipv6 netstream event

\*Mar 21 12:53:28:46 2008 H3C NS6/7/NS6_EVENT: -MDC=1;

CPU 0 IPv6 Flow        Add a flow (Current 1 active flows):

Direction: I Flow Type: IPv6 IP version: 6

InIf: 0 OutIf: 51314696 InVrf: 0

SrcIP: 1:2::3:4 DstIP: 1:2::3:5 Prot: 58

SrcPort: 0 DstPort: 32768 Tos: 0x0 FlowLabel: 0x0 TcpFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 0 DstMask: 0

NextHop: 1:2::3:5 BGP-NextHop: 1:2::4:5

Label 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: UNKNOWN IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVLAN: 0 DstVLAN: 0

First: 0 Last: 0 Pkts: 0 Bytes: 104

Sampling Mode: N/A Sampling Interval: 0

*// 添加一条源地址为1:2::3:4、目的地址为1:2::3:5、端口号为58的IPv6流到使用链表中*

CPU 0 IPv6 Flow        Add a flow (Current 1 active flows):

Direction: I Flow Type: IPv6 IP version: 6

InIf: 0 OutIf: 51314696 InVrf: 0

SrcIP: 1:2::3:4 DstIP: 1:2::3:5 Prot: 58

SrcPort: 0 DstPort: 32768 Tos: 0x0 FlowLabel: 0x0 TcpFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 0 DstMask: 0

NextHop: 1:2::3:5 BGP-NextHop: 1:2::4:5

Label 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: UNKNOWN IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVLAN: 0 DstVLAN: 0

First: 0 Last: 0 Pkts: 0 Bytes: 104

Sampling Mode: N/A Sampling Interval: 0

*// 新增加一条源地址为1:2::6:4、目的地址为1:2::3:5、端口号为68的IPv6流到使用链表中*

\# 10秒后表项老化输出，会有如下调试信息：

\*Mar 21 12:53:37:718 2008 H3C NS6/7/NS6_EVENT:

CPU 0 IPv6 Flow        Age 1 flows (time out)

*// 老化一个IP流表项（不活跃时间超时）*

\*Mar 21 12:53:37:718 2008 H3C NS6/7/NS6_EVENT:

Select Template for flow(Version 9 Type IPv6 outbound Id 305 )

*// 为IP流表项选择一个模板*

\*Mar 21 12:53:37:718 2008 H3C NS6/7/NS6_EVENT:

CPU 0 IPv6 Flow        Export a flow:

Direction: O Flow Type: IPv6 IP version: 6

InIf: 0 OutIf: 51314696 OutVrf: 0

SrcIP: 1:2::3:4 DstIP: 1:2::3:5 Prot: 58

SrcPort: 0 DstPort: 32768 Tos: 0x0 FlowLabel: 0x0 TcpFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 128 DstMask: 64

NextHop: 1:2::3:5 BGP-NextHop: ::

Label 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: UNKNOWN IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVlan: 0 DstVlan: 0

First: 12381680 Last: 12381680 Pkts: 1 Bytes: 104

Sampling Mode: N/A Sampling Interval: 0

*// 输出一条源地址为1:2::3:4、目的地址为1:2::3:5、端口号为58的IPv6流表项*

\*Mar 21 12:53:37:718 2008 H3C NS6/7/NS6_EVENT:

CPU 0 as Aggre   Add a flow (1 active flows currently):

InIf: 0 OutIf: 51314696 SrcAS: 0 DstAS: 0

Direction: O Aggre Type: as IP version : 6

First: 12381680 Last: 12381680 Streams: 1 Pkts: 0 1 Bytes: 0 104

Sample Mode: FULL Sample Interval: 0

*// 增加一个AS聚合流表项（目前总共有一个活跃表项）*

\*Mar 21 12:53:37:734 2008 H3C NS6/7/NS6_EVENT:

CPU 0 Add to transmit queue (Current queue length is 1):

Packet Type: Normal IPv6  Version No: 0  Records: 1

*// 添加一个普通IPv6流数据报文到报文输出队列*

\*Mar 21 12:53:37:734 2008 H3C NS6/7/NS6_EVENT:

CPU 0 Successfully send (Current queue length is 0):

Packet Type: Normal IPv6  Version No: 0  Records: 1

*// 该包已成功发送*

\*Mar 21 12:53:37:734 2008 H3C NS6/7/NS6_EVENT:

CPU 0 IPv6 Flow        Export a flow:

*// 输出一个IPv6流表项数据报文*

\*Mar 21 12:53:37:734 2008 H3C NS6/7/NS6_EVENT:

Select Template for aggregated flow(Version 9 Type as outbound Id 293 )

*// 为AS聚合流表项选择一个模板*

\*Mar 21 12:53:37:734 2008 H3C NS6/7/NS6_EVENT:

CPU 0 as Aggre   Export a flow:

InIf: 0 OutIf: 51314696 SrcAS: 0 DstAS: 0

Direction: O Aggre Type: as IP version : 6

First: 12381680 Last: 12381680 Streams: 1 Pkts: 0 1 Bytes: 0 104

Sample Mode: N/A Sample Interval: 0

\*Mar 21 12:53:37:750 2008 H3C NS6/7/NS6_EVENT:

CPU 0 as Aggre   Export 1 flows

*// 输出一个AS聚合流表项*

\*Mar 21 12:53:37:750 2008 H3C NS6/7/NS6_EVENT:

CPU 0 Add to transmit queue (Current queue length is 1):

Packet Type: Aggre as  Version No: 0  Records: 1

*// 添加一个AS聚合流数据报文到报文输出队列*

\*Mar 21 12:53:37:765 2008 H3C NS6/7/NS6_EVENT:

CPU 0 Add to transmit queue (Current queue length is 1):

Packet Type: Aggre as  Version No: 0  Records: 1

*// 成功发送报文*

\*Mar 21 12:53:37:765 2008 H3C NS6/7/NS6_EVENT:

CPU 0 as Aggre   Export a flow:

*// 输出1个AS聚合流表项数据报文*

\*Mar 21 12:53:37:765 2008 H3C NS6/7/NS6_EVENT: -MDC=1-Slot=2;

Received a packet from the driver for statistics, and the packet type is IPv6_IPL2.

*[//*]*从驱动收到一个待统计的报文，报文类型为二层转发中的IPv6报文*

**IPv6 NetStream \-- IPv6 NetStream调试命令 \-- debugging ipv6 netstream packet**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 netstream packet**]

**[undo debugging ipv6 netstream packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging ipv6 netstream packet**]命令用来打开IPv6 Netstream的报文调试信息开关。

**[undo debugging ipv6 netstream packet**]命令用来关闭IPv6 Netstream的报文调试信息开关。

缺省情况下，IPv6 Netstream的报文调试信息开关处于关闭状态。

表1-2 debugging ipv6 netstream packet命令输出信息描述表

字段

描述

Successfully send

发送报文成功

Fail to send

发送报文失败

Packet Type

发送的报文的类型：

·Normal：普通流统计信息，包括IPv6，MPLS，IPL2

·Aggregation：聚合信息,，包括支持的六种聚合类型

·Template：模板信息

Version No.

版本号，默认为9

Records

数据包中包含的记录条数，比如表项数或模板个数

SrcIP(Port): 192.168.20.173(40000) DstIP(Port): 192.168.20.180(138) VrfID: 0

·SrcIP(Port)：源IP地址（源端口号）

·DstIP(Port)：目的IP地址（目的端口号）

·VrfID：私网路由索引

【举例】

\# 在一台设备上端口GigabitEthernet1/0/1使能了IPv6 Netstream，配置了输出目的主机，并打开IPv6 Netstream报文处理的调试信息开关，当有报文通过端口GigabitEthernet1/0/1并进行Netstream统计，当表项老化输出时，会有如下调试信息：

\<Sysname\> debugging ipv6 netstream packet

\*Mar 21 13:17:33:562 2008 H3C NS6/7/NS6_PACKET:  -MDC=1;

Successfully send.

Packet Type: Normal IPv6  Version No: 9  Records: 1

SrcIP(Port): 192.168.20.173(40000) DstIP(Port): 192.168.20.180(138) VrfID: 0

*// 成功发送一个普通IPv6流数据报文*
