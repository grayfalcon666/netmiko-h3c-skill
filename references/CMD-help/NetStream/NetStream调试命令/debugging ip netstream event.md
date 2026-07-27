<!-- CMD-INDEX
  debugging ip netstream event        | 用户视图             | L6
  debugging ip netstream packet       | 用户视图             | L472
-->

**NetStream \-- NetStream调试命令 \-- debugging ip netstream event**

------------------------------------------------------------------------

【命令】

**[debugging ip netstream event**]

**[undo debugging ip netstream event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging ip netstream event**]命令用来打开IPv4 Netstream的事件调试信息开关。

**[undo debugging ip netstream event**]命令用来关闭IPv4 Netstream的事件调试信息开关。

缺省情况下，IPv4 Netstream的事件调试信息开关处于关闭状态。

表1-1 debugging ip netstream event命令输出信息描述表

字段

描述

IP Flow Add to age list (Statistic Flag *m* Current *n* age flows)

添加IP流到老化链表（统计标记位为*m*的当前老化流有*n*条）

IP Flow Add a Flow (Current *n* active flows)

增加一个IP流表项（目前总共有*n*个活跃表项）

IP Flow Update a flow

更新一个IP流表项

IP Flow Age a flow

老化一个IP流表项

IP Flow Age *n* flows (time out)

老化*n*条IP流表项（定时器超时）

IP Flow Age *n* flows (cache full)

老化*n*个IP流表项（表项溢出）

IP Flow Age all flows (reset)

老化所有IP流表项（重置）

IP Flow Export a flow

输出一个IP流表项

as Aggre Create cache

创建AS聚合流缓冲区

as Aggre Destory cache when *n* entries left

清除AS聚合流缓冲区，剩余*n*个表项

as Aggre Add a flow (*n* active flows currently)

增加一个AS聚合流表项（目前总共有*n*个活跃表项）

as Aggre Update a flow

更新一个AS聚合流表项

as Aggre Export a flow

输出一个AS聚合流表项

as Aggre Export *n* flow

输出*n*个AS聚合流表项数据报文

Add to transmit queue (Current queue length is *n*)

添加一个报文到报文输出队列（目前报文输出队列长度为*n*）

Successfully send (Current queue length is *n*)

成功发送报文（目前报文输出队列长度为*n*）

Fail to send (Current queue length is *n*)

发送报文失败（目前报文输出队列长度为*n*）

Activate Template (*n* active templates currently)

激活一个模板（目前共有*n*个激活模板）

Deactivate Template (*n* active templates currently)

去激活一个模板（目前共有*n*个激活模板）

Select Template for flow (Version 9 Type)

为普通流表项选择一个V9格式模板

Select Template for aggregated flow (Version 9 Type)

为聚合流表项选择一个V9格式模板

CPU 0   IP Flow        Add a flow(Current 1 active flows):

Direction: O Flow Type:   IP IP version: 4

InIf: 0 OutIf: 1048577 OutVrf: 0

SrcIP: 5.4.3.2 DstIP: 5.4.3.1 Prot: 1

SrcPort: 0 DstPort: 2048 Tos: 0x0 TCPFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 0 DstMask: 0

NextHop: 5.4.3.1 BGP-NextHop: 0.0.0.0

Lable 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: Unknown ,IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVLAN: 0 DstVLAN: 0

First: 0 Last: 0 Pkts: 0 0 Bytes: 0 84

Sampling Mode: Fixed Sampling Interval: 0

以IP流表项为例，各字段的意义如下：

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

·TCPFlag：TCP标记

·SrcAS：源自治系统号

·DstAS：目的自治系统号

·SrcMask：源掩码

·DstMask：目的掩码

·NextHop：路由下一跳

·BGP-NextHop：BGP下一跳

·Lable 1：MPLS一层标签

·Lable 2：MPLS二层标签

·Lable 3：MPLS三层标签

·TopLabel Type：栈顶标签的类型

·IP：IP地址

·Mask：掩码

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

CPU 0 AS Aggre   Add a flow (*n* active flows currently):

InIf: 0 OutIf: 1048576 SrcAS: 0 DstAS: 0

Direction O Aggre Type: AS IP version : 4

First: 551894110 Last: 551894110 Flows: 1 Pkts: 0 1 Bytes: 0 84

Sampling Mode: N/A Sampling Interval: 0

以AS聚合为例，各字段的意义如下：

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

Received a packet from the driver for statistics, and the packet type is *packet*-*type*

从驱动接收到一个待统计的报文，报文类型为*packet*-*type*

*[packet-type*]包括：

·IPv4_IPL2：二层转发中的IPv4报文

·IPv4_IPL3：三层转发中的IPv4报文

·IPv4_MPLS：载荷为IPv4的MPLS报文

·IPv4_L2VPN：载荷为IPv4的L2VPN报文

【举例】

\# 在一台设备上端口GigabitEthernet1/0/1使能了Netstream入方向统计，配置目的输出主机，使能AS聚合，配置版本号为9，将表项不活跃老化时间设为10秒，打开IPv4 Netstream的事件调试信息开关，当有一个IP报文进入端口GigabitEthernet1/0/1并进行Netstream统计时，会有如下调试信息。

\<Sysname\> debugging ip netstream event

\*Sep 14 14:20:35:749 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0   IP Flow        Add a flow (Current 1 active flows):

Direction: I Flow Type:   IP IP version: 4

InIf: 51314696 OutIf: 0 InVrf: 0

SrcIP: 192.168.20.180 DstIP: 192.168.20.173 Prot: 1

SrcPort: 0 DstPort: 2048 Tos: 0x0 TCPFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 0 DstMask: 0

NextHop: 0.0.0.0 BGP-NextHop: 0.0.0.0

Lable 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: Unknown IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVLAN: 0 DstVLAN: 0

First: 0 Last: 0 Pkts: 0 0 Bytes: 0 60

Sampling Mode: N/A Sampling Interval: 0

*// 添加一条源IP地址为192.168.20.180，目的地址为192.168.20.173，端口为1的IPv4流到使用链表中*

\*Sep 14 14:20:35:749 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0   IP Flow        Add a flow (Current 1 active flows):

Direction: I Flow Type:   IP IP version: 4

InIf: 51314696 OutIf: 118816768 InVrf: 0

SrcIP: 192.168.20.181 DstIP: 192.168.20.173 Prot: 2

SrcPort: 0 DstPort: 2048 Tos: 0x0 TCPFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 24 DstMask: 32

NextHop: 127.0.0.1 BGP NextHop: 0.0.0.0

Lable 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: Unknown IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVLAN: 0 DstVLAN: 0

First: 10981810 Last: 10981810 Pkts: 0 1 Bytes: 0 60

Sampling Mode: N/A Sampling Interval: 0

*// 新增加一条源地址为192.168. 20.181，目的地址为192.168.20.173，端口为2的IPv4流表项*

\# 10秒后表项老化输出，会有如下调试信息：

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0   IP Flow        Age 1 flows (time out[).]

*// 老化一个IP流表项*（*不活跃时间超时*）*

\*Sep 14 14:20:42:199 2012 H3C NS4/7/NS_EVENT: -MDC=1;

Select Template for flow(Version 9 Type   IP inbound ID 281 )

*// 为IP流表项选择一个模板*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0   IP Flow        Export a flow:

Direction: I Flow Type:   IP IP version: 4

InIf: 51314696 OutIf: 118816768 InVrf: 0

SrcIP: 192.168.20.180 DstIP: 192.168.20.173 Prot: 1

SrcPort: 0 DstPort: 2048 Tos: 0x0 TCPFlag: 0x0

SrcAS: 0 DstAS: 0 SrcMask: 24 DstMask: 32

NextHop: 127.0.0.1 BGP-NextHop: 0.0.0.0

Lable 1:0-0-0 2:0-0-0 3:0-0-0

TopLabel Type: Unknown IPv4/IPv6 address: 0.0.0.0/0

SrcMAC: 0000-0000-0000 DstMAC: 0000-0000-0000 SrcVlan: 0 DstVlan: 0

First: 10981810 Last: 10981810 Pkts: 0 1 Bytes: 0 60

Sampling Mode: N/A Sampling Interval: 0

*// 输出一条源地址为192.168.20.180，目的地址为192.168.20.173，端口为1的IP流表项*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0 as Aggre   Add a flow (1 active flows currently):

InIf: 51314696 OutIf: 118816768 SrcAS: 0 DstAS: 0

Direction: I Aggre Type: as IP version : 4

First: 10981810 Last: 10981810 Flows: 1 Pkts: 0 1 Bytes: 0 60

Sampling Mode: N/A Sampling Interval: 0

*// 增加一个AS聚合流表项*（*目前总共有一个活跃表项*）*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0 Add to transmit queue (Current queue length is 1):

Packet Type: Normal   IP  Version No: 9  Records: 1

*// 添加一个普通IP流数据报文到报文输出队列*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0 Successfully send (Current [queue length is 0):]

Packet Type: Normal   IP  Version No: 9  Records: 1

*// 成功发送一个包*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0   IP Flow        Export a flow:

*// 输出1个IP流表项数据报文*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

Select Template for aggregated flow (Version 9 Type as inbound ID 257 )

*// 为AS聚合流表项选择一个模板*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0 as Aggre   Export a flow:

InIf: 51314696 OutIf: 118816768 SrcAS: 0 DstAS: 0

Direction: I Aggre Type: as IP version : 4

First: 10981810 Last: 10981810 Flows: 1 Pkts: 0 1 Bytes: 0 60

Sampling Mode: N/A Sample Interval: 0

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1:

CPU 0 as Aggre   Export 1 flows

*// 输出一个AS聚合流表项*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0 Add to transmit queue (Current queue length is 1):

Packet Type: Aggre as  Version No: 9  Records: 1

*// 添加一个AS聚合流数据报文到报文输出队列*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0 Successfully send (Current [queue length is 0):]

Packet Type: Aggre as  Version No: 9  Records: 1

*// 成功发送报文*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

CPU 0 as Aggre   Export a flow:

*// 输出1个AS聚合流表项数据报文*

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1-Slot=2;

Received a packet from the driver for statistics, and the packet type is IPv4_IPL2.

*[//*]*从驱动收到一个待统计的报文，报文类型为二层转发中的IPv4报文*

**NetStream \-- NetStream调试命令 \-- debugging ip netstream packet**

------------------------------------------------------------------------

【命令】

**[debugging ip netstream packet**]

**[undo debugging ip netstream packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging ip netstream packet**]命令用来打开IPv4 Netstream的报文调试信息开关。

**[undo debugging ip netstream packet**]命令用来关闭IPv4 Netstream的报文调试信息开关。

缺省情况下，IPv4 Netstream的报文调试信息开关处于关闭状态。

表1-2 debugging ip netstream packet命令输出信息描述表

字段

描述

Successfully send

发送报文成功

Fail to send

发送报文失败

SrcIP(Port): 192.168.20.173(40000) DstIP(Port): 192.168.20.180(138) VrfID: 0

·SrcIP(Port)：源IP地址（源端口号）

·DstIP(Port)：目的IP地址（目的端口号）

·VrfID：私网路由索引

【举例】

\# 在一台设备上端口GigabitEthernet1/0/1使能了Netstream，配置了输出目的主机，并打开IPv4 Netstream的报文调试信息开关，当有报文通过端口GigabitEthernet1/0/2时进行Netstream统计。表项老化输出时，会有如下调试信息。

\<Sysname\> debugging ip netstream packet

\*Sep 14 14:20:42:166 2012 H3C NS4/7/NS_EVENT: -MDC=1;

Successfully send.

Packet Type: Normal   IP  Version No: 5  Records: 2

SrcIP(Port): 192.168.20.173(40000) DstIP(Port): 192.168.20.180(138) VrfID: 0

*// 成功发送一个普通IP流数据报文*
