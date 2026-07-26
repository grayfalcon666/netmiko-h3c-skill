
**sFlow \-- sFlow调试命令 \-- debugging sflow agent**

------------------------------------------------------------------------

【命令】

**[debugging sflow agent**]

**[undo debugging sflow agent**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging sflow agent**]命令用于打开sFlow Agent的调试信息开关。**undo debugging sflow agent**命令用于关闭sFlow Agent的调试信息开关。

缺省情况下，sFlow Agent的调试信息开关处于关闭状态。

表1-1 debugging sflow agent命令输出信息描述表

字段

描述

Created a timer for finding agent address, interval *n* seconds

创建寻找Agent地址的定时器，间隔时间为*n*秒

Destroyed the agent address timer.

删除寻找Agent地址的定时器

Created a timer for VPN reconnection, interval *n* seconds.

创建VPN重连定时器，间隔时间为*n*秒

Destroyed the VPN reconnection timer.

删除VPN重连定时器

Received IF\_*event_name(event_id)* event on interface *interface_name(ifIndex).*

收到*interface_name*接口的IF\_*event_name*事件，该事件的事件ID为*event_id*，该接口索引为*ifIndex*

Succeeded in processing IF\_*event_name(event_id)* event on interface *interface-name(ifIndex).*

处理*interface_name*接口的IF\_*event_name*事件成功，该事件的事件ID为*event_id*，该接口的接口索引为*ifIndex*

Failed to process IF*\_event_name(event_id)* event on interface *interface-name(ifIndex).*

处理*interface_name*接口的IF\_*event_name*事件失败，该事件的事件ID为*event_id*，该接口的接口索引为*ifIndex*

Received SLOT\_*event_name(event_id)* event for slot *slot_id.*（分布式设备－独立运行模式、集中式IRF设备）

Received SLOT\_*event_name(event_id)* event for chassis *chassis_id* slot *slot_id.*（分布式设备－IRF模式）

收到一个板*slot_id*的SLOT\_*event_name*事件，该事件的事件ID为*event_id*（分布式设备－独立运行模式、集中式IRF设备）

收到一个成员设备*chassis_id*上一个板*slot_id*的SLOT\_*event_name*事件，该事件ID为*event_id*（分布式设备－IRF模式）

Received *event_name(event_id)* event for vpn-instance *vpn_name*(vrfindex *vrfIndex*).

收到一个名为*vpn_name*的VPN实例的*event_name*事件，该事件的事件ID为*event_id*，*vpn_name*的VPN索引为*vrfIndex*

Succeeded in finding agent address *address,* and broadcast it to all slots*.

成功找到Agent地址*address*，并同步到所有板

【举例】

\# 在一台设备上启动sFlow功能，打开sFlow Agent的调试信息开关，不配置Agent地址，进行如下操作：拔去某一接口板，然后插入；配置一VPN实例，然后删除该VPN实例。

\<Sysname\> debugging sflow agent{.TerminalDisplayChar}

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ CREATE_AGNETIPTIMER:

Created a timer for finding agent address, interval 60 seconds.

*// 在未配置Agent地址的情况下，创建Agent地址自动查找定时器，间隔时间为60秒*

%Jun 13 10:03:53 673 2011 Sysname SFLOW/7/ DESTROY_AGENTIPTIMER:

Destroyed the agent address timer.

*// 自动查找到Agent地址后，删除Agent地址自动查找定时器*

%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ RCV_IFEVENT:

Received IF_DEACTIVE(0x01) event on interface GigabitEthernet1/0/1(1).

*// 拔去某一接口板，收到接口去激活事件* *，接口为GigabitEthernet1/0/1，接口索引为1*

%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ PROC_IFEVENT:

Succeeded in processing IF\_ DEACTIVE(0x01) event on interface GigabitEthernet1/0/1(1).

*// 处理接口去激活事件* *，接口为GigabitEthernet1/0/1，接口索引为1*

%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ RCV_SLOTEVENT:

Received SLOT_INSERTED(0x01) event for slot 2.

*// 接口板插入，收到板插入事件，槽号为2（分布式设备－独立运行模式/集中式-IRF设备）*

\<Sysname\> system-view

Sysname ip vpn-instance vpn

%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ RCV_VPNEVENT:

Received VPN_CREATE(0x01) event for vpn-instance vpn(vrfindex 1).

*// 创建VPN实例vpn，收到VPN创建事件，VPN名字为vpn，索引为1*

Sysname undo ip vpn-instance vpn

%Jun 13 10:03:53 673 2011 Sysname SFLOW/7/ CREATE_VPNTIMER:

Created a timer for VPN reconnection, interval 1 seconds.

*// 删除VPN实例后，创建VPN重连定时器，间隔时间为1秒*

%Jun 13 10:03:53 673 2011 Sysname SFLOW/7/ DESTROY_VPNTIMER:

Destroyed the VPN reconnection timer.

*// 删除VPN重连定时器*

Sysname quit

\<Sysname\> debugging sflow synchronization

%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ LOOKUP_AGENTADDR:

Succeeded in finding agent address 192.168.20.104, and broadcast it to all slots.

*// 自动寻找到Agent地址，IP地址为192.168.20.104，并同步到所有接口板*

**sFlow \-- sFlow调试命令 \-- debugging sflow all**

------------------------------------------------------------------------

【命令】

**[debugging sflow all**]

**[undo debugging sflow all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging sflow all**]命令用于打开所有sFlow的调试信息开关。**undo debugging sflow all**命令用于关闭所有sFlow的调试信息开关。

缺省情况下，所有sFlow的调试信息开关处于关闭状态。

**sFlow \-- sFlow调试命令 \-- debugging sflow collector**

------------------------------------------------------------------------

【命令】

**[debugging sflow collector**]

**[undo debugging sflow collector**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging sflow collector**]命令用于打开sFlow Collector的调试信息开关。**undo debugging sflow collector**命令用于关闭sFlow Collector的调试信息开关。

缺省情况下，sFlow Collector的调试信息开关处于关闭状态。

表1-2 debugging sflow collector命令输出信息描述表

字段

描述

Created an aging timer for collector *collector-id*, interval *n* seconds.

创建Collector *collector-id*的老化定时器，间隔时间为*n*秒

Destroyed the aging timer for collector *collector-id*.

删除Collector *collector-id*的老化定时器

Time to age out collector *collector-id*, and broadcast the event to all slots.

Collector *collector-id*老化到期，并同步到所有板

Broadcast new vrfindex *vrfindex* of vpn-instace *vpn_name* on collector *collector-id* to all slots.

广播绑定到Collector *collector-id*的VPN *vpn_name*的新VPN索引*vrfindex*

sFlow datagram version = *version*

sFlow版本号

Agent IP version = *address_type*

Agent地址类型：

·1：IPv4类型

·2：IPv6类型

Agent IP address = *address*

Agent地址

Sub agent ID = *id*

子代理号

Sequence number = *number*

报文序列号

UpTime = *UpTime*

系统启动时间

Sample number = *number*

样本个数

sFlow counter sample header information:

Counter采样样本头信息

Data format = *format*

样本类型

Sample length = *length*

样本长度

Data source type = *type*

数据源类型

Data source index = *index*

数据源索引

Record number = *number*

记录个数

sFlow flow sample header information:

Flow采样样本头信息

Source id type = type

数据源ID类型

Source id index = index

数据源ID索引

Sampling rate = *rate*

采样率

Sample pool = *pool*

采样池

Drops = *number*

丢弃样本个数

Input interface format = *format*

入接口格式

Input interface index = *ifIndex*

入接口索引

Output interface format = *format*

出接口格式

Output interface index= *ifIndex*

出接口索引

【举例】

\# 在一台设备上启动了sFlow功能，打开sFlow Collector的调试信息开关，进行如下配置：配置一个有老化时间的Collector；配置一个没有老化时间且能够正确收集报文的地址的Collector；在某接口下配置Flow采样实例，并能够正确采样；在某一接口下配置Counter采样实例，并能够正确采样；创建一VPN实例和配置一绑定到该VPN的Collector，然后删除该VPN。

\<Sysname{.TerminalDisplayChar}\> debugging sflow collector

\<[Sysname{.TerminalDisplayChar}\> system-view]

Sysname{.TerminalDisplayChar} sflow collector 1 ip 1.1.1.1 time-out 90

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ CREATE_COLLECTORTIMER:

Created an aging timer for collector 1, interval 90 seconds.

*// 创建Collector 1的老化定时器，间隔时间为90秒*

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ AGE_COLLECTOR:

Time to age out collector 1, and broadcast the event to all slots.

*[// Collector 1*]*老化时间超时，并同步到所有接口板*

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ DESTROY_COLLECTORTIMER:

Destroyed the aging timer for collector 1.

*// 删除Collector 1的老化定时器*

\<Sysname{.TerminalDisplayChar}\> system-view

Sysname{.TerminalDisplayChar} sflow collector 1 ip 11.1.1.1

Sysname sflow collector 2 ip 11.1.1.2

Sysname{.TerminalDisplayChar} interface gigabitethernet 1/0/1

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow counter interval 2

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow counter collector 2

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow sampling-rate 1000

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow flow collector 1

Sysname \*Mar 29 10:37:40:515 2013 Sysname SFLOW/7/COLLECTOR: -MDC=1; sFlow counter sampl

e header information:

Data format = 4

Sample length = 60

Sequence number = 10

Data source type = 0

Data source index = 1

Record number = 3

\*Mar 29 10:37:39:504 2013 Sysname SFLOW/7/COLLECTOR: -MDC=1; sFlow send a packet

:

Collector ID = 2

Collector address = 11.1.1.2

Vrfindex = 0

sFlow datagram version = 5

Agent IP version = 1

Agent IP address = 10.1.1.1

Sub agent id = 0

Sequence number = 30

Uptime = 326000

Sample number = 1

*// 采集到一个Counter样本，打印样本头信息。其中数据格式为4，样本长度为60，样本序列号为10，数据源类型为0，数据源索引为1，记录个数为3*

\*Mar 29 13:44:31:966 2013 MSR26.62 SFLOW/7/COLLECTOR: sFlow flow sample header i

nformation:

Data format = 3

Sample length = 80

Sequence number = 10

Source id type = 0

Source id index = 1

Sampling rate = 1000

Sample pool = 5000

Drops = 0

Input interface format = 0

Input interface = 1

Output interface format = 0

Output interface = 3

Record number = 5

\*Mar 29 13:44:32:635 2013 MSR26.62 SFLOW/7/COLLECTOR: sFlow send a packet:

Collector ID = 1

Collector address = 11.1.1.1

Vrfindex = 0

sFlow datagram version = 5

Agent IP version = 1

Agent IP address = 10.1.1.1

Sub agent id = 0

Sequence number = 2

Uptime = 18153000

Sample number = 1

*// 采集到一个Flow样本，打印样本头信息。其中数据格式为3，样本长度为80，样本序列号为10，数据源ID类型为0，数据源ID索引为1，采样率为1000，样本次个数5000，丢弃个数0，入接口格式为0，入接口索引为1，出接口格式为0，出接口索引为3，记录个数为5*

Sysname-GigabitEthernet1/0/1 quit

Sysname{.TerminalDisplayChar} sflow collector 3 vpn-instance vpn ip 1.1.1.1

Sysname{.TerminalDisplayChar} ip vpn-instance vpn

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ COLLECTOR:

Broadcast new vrfindex 2 of vpn-instace vpn on collector 3 to all slots.

*// 配置Collector 3关联的VPN实例名称，创建该VPN实例，打印VPN变化调试信息*

**sFlow \-- sFlow调试命令 \-- debugging sflow counter-polling**

------------------------------------------------------------------------

【命令】

**[debugging sflow counter-polling**]

**[undo debugging sflow counter-polling**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging sflow counter-polling**]命令用于打开Counter采样的调试信息开关。**undo debugging sflow counter-polling**命令用于关闭Counter采样的调试信息开关。

缺省情况下，Counter采样的调试信息开关处于关闭状态。

表1-3 debugging sflow counter-polling 命令输出信息描述表

字段

描述

sFlow poller sample data information

sFlow Poller数据项信息

Summary info:

概要信息

Ifindex = *Ifindex*

接口索引

Iftype = *Iftype*

接口类型

Direction = *direction*

报文方向

IfStatus = *If_status*

接口状态

IfSpeed = *if_speed*

接口速率

Bitmap = *bitmap*

数据项

IfTable info:

IfTable表信息

LastChange = *last_change_time*

接口最后一次修改时的系统启动时长为*last_change_time*

Mtu = *mtu*

接口MTU

Speed = *speed*

接口速率

InOctets = *InOctets*

入站包字节数

InUcastPkts = *InUcastPkts*

入站的单播包数

InNUcastPkts = *InNUcastPkts*

入站的非单播包数

InDiscards = *Discard number*

丢弃的入站包数

InErrors = *Errors number*

有错误的入站包数

InUnknownProtos = *InUnknownProtos*

不支持的协议的入站包数

OutOctets = *OutOctets*

出站包字节数

OutUcastPkts = *OutUcastPkts*

出站的单播包数

OutNUcastPkts = *OutNUcastPkts*

出站的非单播包数

OutDiscards = *Discard number*

丢弃的出站包数

OutErrors = *Errors number*

有错误的出站包数

OutQLen = *Queen length*

出包队列长度

usOperStatus = *Status*

接口的当前运行状态

PhysAddress = *mac Address*

接口在协议子层的物理地址

IfXTable info:

IfXTable表信息

HCInOctets = *HCInOctets*

入站包字节数

HCInUcastPkts = *HCInUcastPkts*

入站单播包数

HCInMulticastPkts = *HCInMulticastPkts*

入站多播包数

HCInBroadcastPkts = *HCInBroadcastPkts*

入站广播包数

HCOutOctets = *HCOutOctets*

出站包字节数

HCOutUcastPkts = *HCOutUcastPkts*

出站单播包数

HCOutMulticastPkts = *HCOutMulticastPkts*

出站多播包数

HCOutBroadcastPkts= *HCOutBroadcastPkts*

出站广播包数

InMulticastPkts = *InMulticastPkts*

入站的多播包数

InBroadcastPkts = *InBroadcastPkts*

入站的广播包数

OutMulticastPkts = *OutMulticastPkts*

出站的多播包数

OutBroadcastPkts = *OutBroadcastPkts*

出站的广播包数

HighSpeed = *HighSpeed*

接口的当前带宽

CounterDiscontinuityTime = *CounterDiscontinuityTime*

计数中断时间

PromiscuousMode = *PromiscuousMode*

混杂模式设置状态

ConnectorPresent = *ConnectorPresent*

是否有物理连接器

Ethernet statistics:

以太网链路统计信息

AlignmentErrors = *AlignmentErrors*

队列错误数

FCSErrors = *FCSErrors*

校验码错误帧数

SingleCollisionFrames = *SingleCollisionFrames*

单个冲突帧数

MultipleCollisionFrames = *MultipleCollisionFrames*

多个冲突帧数

SQETestErrors = *SQETestErrors*

SQE测试错误数

DeferredTransmissions = *DeferredTransmissions*

超时帧数

LateCollisions = *LateCollisions*

延迟冲突数

ExcessiveCollisions = *ExcessiveCollisions*

额外冲突数

InternalMacTransmitErrors = *InternalMacTransmitErrors*

内部传送错误数

CarrierSenseErrors = *CarrierSenseErrors*

载波侦听错误数

FrameTooLongs = *FrameTooLongs*

过长的帧数

InternalMacReceiveErrors = *InternalMacReceiveErrors*

内部接收错误数

SymbolErrors = *symbol_errors*

符号错误数

DuplexStatus = *DuplexStatus*

双工状态

Run info:

运行信息

Sequence = *Sequence number*

序列号

Next polling time = *Next polling time*

下一次采样时刻

【举例】

\# 在一台设备上启动了sFlow功能，打开Counter采样调试开关，并配置了Counter采样。

\<Sysname{.TerminalDisplayChar}\> debugging sflow counter-polling

\<[Sysname{.TerminalDisplayChar}\> system-view]

Sysname{.TerminalDisplayChar} sflow agent ip 1.1.1.1

Sysname{.TerminalDisplayChar} sflow collector 1 ip 192.168.20.104

Sysname{.TerminalDisplayChar} interface gigabitethernet 1/0/1

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow counter interval 2

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow counter collector 1

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/POLLER:

sFlow poller sample data information

Summary info:

Ifindex = 3

Iftype = 3

Direction = 1

IfStatus = 1

IfSpeed = 100

Bitmap = 3

IfTable info:

LastChange = 32900

Mtu = 1500

Speed = 100

InOctets = 30

InUcastPkts = 50

InNUcastPkts = 39

InDiscards = 24

InErrors = 3

InUnknownProtos = 99

OutOctets = 10

OutUcastPkts = 0

OutNUcastPkts = 0

OutDiscards = 23

OutErrors = 1

OutQLen = 100

OperStatus = 1

PhysAddress = 00-e4-67-90-23-f5

IfXTable info:

HCInOctets = 35

HCInUcastPkts = 12

HCInMulticastPkts = 10

HCInBroadcastPkts = 0

HCOutOctets = 19

HCOutUcastPkts = 0

HCOutMulticastPkts = 0

HCOutBroadcastPkts = 0

InMulticastPkts = 0

InBroadcastPkts = 0

OutMulticastPkts = 0

OutBroadcastPkts = 0

HighSpeed = 1000

CounterDiscontinuityTime = 29808

PromiscuousMode = 1

ConnectorPresent = 1

Ethernet statistics:

Index = 3

AlignmentErrors = 0

FCSErrors = 0

SingleCollisionFrames = 0

MultipleCollisionFrames = 0

SQETestErrors = 0

DeferredTransmissions = 0

LateCollisions = 0

ExcessiveCollisions = 0

InternalMacTransmitErrors = 0

CarrierSenseErrors = 0

FrameTooLongs = 0

InternalMacReceiveErrors = 0

SymbolErrors = 0

DuplexStatus = 0

Run info:

Sequence = 34

Next polling time = 35009

*// 封装了一个Counter采样的数据项*

**sFlow \-- sFlow调试命令 \-- debugging sflow driver**

------------------------------------------------------------------------

【命令】

**[debugging sflow driver**]

**[undo debugging sflow driver**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging sflow driver**]命令用来打开sFlow驱动的调试信息开关。**undo debugging sflow driver**命令用来关闭sFlow驱动的调试信息开关。

缺省情况下，sFlow驱动的调试信息开关处于关闭状态。

表1-4 debugging sflow driver命令输出信息描述表

字段

描述

*[commad_type direction* on interface *interface_name(ifIndex),* parameter = *parameter,* result *= result*]

*[interface_name*]接口Flow采样*commad_type*下驱动，方向为*direction*，下驱动参数为*parameter*，下驱动结果为*result*

【举例】

\# 在一台设备上启动了sFlow功能，打开sFlow驱动调试开关，配置Flow采样的采样频率。

\<Sysname{.TerminalDisplayChar}\> debugging sflow driver

\<[Sysname{.TerminalDisplayChar}\> system-view]

Sysname{.TerminalDisplayChar} interface gigabitethernet 1/0/1

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow sampling-rate 1000

%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:

Enable the sampling inbound on interface GigabitEthernet1/0/1(1), parameter = 0, result = 0.

*// 接口GigabitEthernet1/0/1，接口索引为1，入方向开启采样功能，参数为0，下驱动结果为0（成功）*

%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:

Enable the sampling outbound on interface GigabitEthernet1/0/1(1), parameter = 0, result = 0.

*// 接口GigabitEthernet1/0/1，接口索引为1，出方向开启采样功能，参数为0，下驱动结果为0（成功）*

%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:

Set the sampling rate inbound on interface GigabitEthernet1/0/1(1), parameter = 1000, ret = 0. 

*// 接口GigabitEthernet1/0/1，接口索引为1，入方向Flow采样频率下驱动，参数为1000，下驱动结果为0（成功）*

%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:

Set the sampling rate outbound on interface GigabitEthernet1/0/1(1), parameter = 1000, result = 0.

*// 接口GigabitEthernet1/0/1，接口索引为1，出方向Flow采样频率下驱动，参数为1000，下驱动结果为0（成功）*

**sFlow \-- sFlow调试命令 \-- debugging sflow flow-sampling**

------------------------------------------------------------------------

【命令】

**[debugging sflow flow-sampling**]

**[undo debugging sflow flow-sampling**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging sflow flow-sampling**]命令用于打开Flow采样的调试信息开关。**undo debugging flow-sampling**命令用于关闭Flow采样的调试信息开关。

缺省情况下，Flow采样的调试信息开关处于关闭状态。

表1-5 debugging sflow flow-sampling命令输出信息描述表

字段

描述

sFlow poller sample data information

Poller数据项信息

ifIndex = *ifIndex*

接口索引

HeaderLen = *length*

原始报文头长度

EthType = *type*

以太帧类型

EthTotalLen = *length*

以太帧总长度

DstMac = *mac_address*

目的MAC地址

SrcMac = *mac_address*

源MAC地址

L3Protocol = *protocol*

IP头协议字段表示的协议类型

TcpFlag = *flag*

TCP Flag标记字段

IPTos = *tos*

IP头tos字段

SrcPort = *port*

源端口号

DstPort = *port*

目的端口号

vrfIndex = *vrfIndex*

VPN索引

SrcIP = *address*

源IP地址

DstIP = *address*

目的IP地址

NextHop = *address*

下一跳地址

SrcMaskLen = *length*

源地址掩码长度

DstMaskLen = *length*

目的地址掩码长度

IPPacketLen = *length*

IP包长度

Bitmap = *bitmap*

数据项Bitmap

sFlow flow sample additional information:

sFlow Flow采样驱动上传的MBUF附加信息

Direction = *direction*

样本经过设备的方向

Input interface = *internet_name*

入接口

Output interface = *internet_name*

出接口

Input TCI = *TCI*

入接口TCI信息

Output TCI = *TCI*

出接口TCI信息

Sample pool = *number*

样本池个数

Forward type = *type*

转发类型

【举例】

\# 在一台设备上启动了sFlow功能，打开Flow采样调试开关，配置了Flow采样实例并能够正确采样。

\<Sysname{.TerminalDisplayChar}\> debugging sflow flow-sampling

\<[Sysname{.TerminalDisplayChar}\> system-view]

Sysname{.TerminalDisplayChar} sflow agent ip 1.1.1.1

Sysname{.TerminalDisplayChar} sflow collector 1 ip 192.168.20.104

Sysname{.TerminalDisplayChar} interface gigabitethernet 1/0/1

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow sampling-rate 1000

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow flow collector 1

%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/SAMPLER:

sFlow flow sample additional information:

Direction = inbound

Input interface = GigabitEthernet1/0/3

Output interface = GigabitEthernet1/0/5

Input TCI = 3

Output TCI = 3

Sample pool = 5000

Forward type = L3 forward

*// 驱动上传了一个MBUF，其中包方向为inbound，入接口为GigabitEthernet 1/0/3，出接口为GigabitEthernet 1/0/5，入接口TCI为3，出接口TCI为3，样本池为5000，转发类型为L3 forward*

%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/SAMPLER:

sFlow poller sample data information

ifIndex = 2

HeaderLen = 50

EthType = 2048

EthTotalLen = 1600

DstMac = 00-e0-fc-6f-84-a6

SrcMac = 00-46-a5-90-e3-43

L3Protocol = 6

TcpFlag = 0

IPTos = 0

SrcPort = 6343

DstPort = 6343

vrfIndex = 4

SrcIP = 10.55.98.114

DstIP = 10.55.99.55

NextHop = 10.55.98.1

SrcMaskLen = 24

DstMaskLen = 24

IPPacketLen = 1500

Bitmap = 48

*// 封装了一个Flow采样数据项，其中采样接口接口索引为2，原始头长度为50，以太帧类型为2048，以太帧总长度为1600，源MAC地址为00-46-a5-90-e3-43，目的MAC地址为00-e0-fc-6f-84-a6，三层协议字段类型为6，TCP Flag为0，IP TOS为0，源端口为6343，目的端口为6343，VPN索引为4，源地址为10.55.98.114，目的地址为10.55.98.117，下一跳为10.55.98.55.1，IP包长度为1500，bitmap为48*

**sFlow \-- sFlow调试命令 \-- debugging sflow synchronization**

------------------------------------------------------------------------

【命令】

**[debugging sflow synchronization**]

**[undo debugging sflow synchronization**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging sflow synchronization**]命令用于打开sFlow同步的调试信息开关。**undo debugging sflow synchronization**命令用于关闭sFlow同步的调试信息开关。

缺省情况下，sFlow同步的调试信息开关处于关闭状态。

表1-6 debugging sflow synchronization命令输出信息描述表

字段

描述

Start smoothing process on slot *slot_id*（集中式设备、分布式设备－独立运行模式、集中式IRF设备）

Start smoothing process on chassis *chassis_id* slot *slot_id*（分布式设备－IRF模式）

开始在板*slot_id*上进行平滑处理（集中式设备、分布式设备－独立运行模式、集中式IRF设备）

开始在在成员设备*chassis_id*的单板*slot_id*上进行平滑处理（分布式设备－IRF模式）

Stop smoothing process on slot *slot_id*（集中式设备、分布式设备－独立运行模式、集中式IRF设备）

Stop smoothing process on chassis *chassis_id* slot *slot_id*（分布式设备－IRF模式）

结束在板*slot_id*上的平滑处理（集中式设备、分布式设备－独立运行模式、集中式IRF设备）

结束在在成员设备*chassis_id*的单板*slot_id*上的平滑处理（分布式设备－IRF模式）

Succeeded in sending a smooth message to slot *slot_id*, length *length*, errcode *code*（集中式设备、分布式设备－独立运行模式、集中式IRF设备）

Succeeded in sending a smooth message to chassis *chassis_id* slot *slot_id,* length *length*, errcode *code*（分布式设备－IRF模式）

向*slot_id*发送一个平滑消息，消息长度为*length*，返回的错误码为*code*（集中式设备、分布式设备－独立运行模式、集中式IRF设备）

向成员设备*chassis_id*上的单板*slot_id*发送一个平滑消息，消息长度为*length*，返回的错误码为*code*（分布式设备－IRF模式）

Succeeded in synchronizing the configuration on interface *interface_name(ifIndex).*

向*interface_name*接口所在板同步该接口数据成功，该接口的接口索引为*ifIndex*

Failed to synchronize the configuration on interface *Interfacen_name(ifIndex).*

向*interface_name*接口所在板同步该接口数据失败，该接口的接口索引为*ifIndex*

Succeeded in synchronizing the message to slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*（分布式设备－独立运行模式、集中式IRF设备）

Succeeded in synchronizing the message to chassis *chassis_id* slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*（分布式设备－IRF模式）

同步数据到*slot_id*成功，socket 文件描述符为*fd*，数据长度为*length*，返回的错误码为*errcode*（分布式设备－独立运行模式、集中式IRF设备）

同步数据到成员设备*chassis_id*上的单板*slot_id*成功，socket 文件描述符为*fd*，数据长度为*length*，返回的错误码为*errcode*（分布式设备－IRF模式）

Failed to synchronize the message to slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*（分布式设备－独立运行模式、集中式IRF设备）

Failed to synchronize the message to chassis *chassis_id* slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*（分布式设备－IRF模式）

同步数据到*slot_id*失败，socket 文件描述符为*fd*，数据长度为*length*，返回的错误码为*errcode*（分布式设备－独立运行模式、集中式IRF设备）

同步数据到成员设备*chassis_id*上的单板*slot_id*失败，socket 文件描述符为*fd*，数据长度为*length*，返回的错误码为*errcode*（分布式设备－IRF模式）

Succeeded in synchronizing *message_type* message to kernel*,* length *length,* errcode *errcode*

用户态成功同步消息到内核，消息类型为*message_type*，消息长度为*length*，返回的错误码为*errcode*

Failed to synchronize *message_type* message to kernel*,* length *length,* errcode *errcode*

用户态未成功同步消息到内核，消息类型为*message_type*，消息长度为*length*，返回的错误码为*errcode*

Received smooth message, length *length*.

用户态收到平滑消息，消息长度为*length*

Received *message_type* configuration message*,* length *length*

用户态收到配置消息，消息类型为*message_type*，消息长度为*length*

【举例】

\# 在一台设备上启动sFlow功能，打开sFlow同步的调试信息开关，进行如下配置和操作：配置一全局配置；配置接口板上的接口的采样实例；拔出某一接口板然后再插入。

\<Sysname{.TerminalDisplayChar}\> debugging sflow synchronization

\<[Sysname{.TerminalDisplayChar}\> system-view]

Sysname{.TerminalDisplayChar} sflow agent ip 192.168.20.104 

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SYNC_UNICAST:

Succeeded in synchronizing the message to slot 2, length 40, errcode 0x00.

*// 成功同步配置数据到槽号为2的接口板，消息长度为40，错误码为0x00（成功）（分布式设备－独立运行模式、集中式-IRF设备）*

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SYNC_KERNEL:

Succeeded in synchronizing configuration message to kernel, length 40, errcode 0x%00.

*// 配置数据下内核成功，消息长度为40，错误码为0x00（成功）*

Sysname interface gigabitethernet 1/0/1

Sysname{.TerminalDisplayChar}-GigabitEthernet1/0/1 sflow counter interval 2   

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SYNC_IFCFG:

Succeeded in synchronizing the configuration on interface GigabitEthernet1/0/1(4).

*// 成功同步接口GigabitEthernet 1/0/1(4)的数据到接口板（分布式设备－独立运行模式/集中式-IRF设备）*

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ START_SMOOTH:

Start smoothing process with slot 2.

*// 接口板拔出再插入，开始与槽号为2接口板进行平滑处理*

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SEND_SMTHMSG:

Succeeded in sending a smooth message to slot 2, length 90, errcode 0x00000000.

*// 发送平滑数据到槽号为2的接口板，消息长度为90*

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ STOP_SMOOTH:

Stop smoothing process with slot 2.

*// 结束与槽号为2的接口板的平滑处理*

%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ RCV_MSG:

Received smooth message, length 90.

*// 收到平滑消息，消息长度为90（分布式设备－独立运行模式、集中式IRF设备）*

