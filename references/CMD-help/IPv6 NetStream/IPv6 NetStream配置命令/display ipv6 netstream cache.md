
**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- display ipv6 netstream cache**

------------------------------------------------------------------------

**[display ipv6 netstream cache**]命令用来查看IPv6 NetStream流缓存区的配置和状态信息。

【命令】

集中式设备：

**[display ipv6 netstream cache ** **verbose** ]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 netstream cache ** **slot** *slot-number*  **cpu** *cpu-number*  ]  **verbose**

分布式设备－IRF模式：

**[display ipv6 netstream cache ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息。 *slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的信息。 *slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示IPv6 NetStream流缓冲区的详细信息。

【举例】

\# 查看IPv6 NetStream流缓冲区信息。（集中式设备）

\<Sysname\> display ipv6 netstream cache verbose

IPv6 NetStream cache information:

  Active flow timeout             : 60 min

  Inactive flow timeout           : 10 sec

  Max number of entries           : 1000

  IPv6 active flow entries        : 1

  MPLS active flow entries        : 2

  IPL2 active flow entries        : 1

  IPv6 flow entries counted       : 10

  MPLS flow entries counted       : 20

  IPL2 flow entries counted       : 20

  Last statistics resetting time  : 01/01/2000 at 00:01:02

IPv6 packet size distribution (1103746 packets in total):

1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480

.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000

512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608

.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000

Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)

                  Flows /sec       /sec   /flow   /flow       /flow

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

TCP-Telnet      2656855     372        4       86        49        27

TCP-FTP         5900082      86        9        9        11        33

TCP-FTPD        3200453    1006        5      193        45        33

TCP-WWW       546778274   11170      887       12         8        32

TCP-other      49148540    3752       79       47        30        32

UDP-DNS       117240379     570      190        3         7        34

UDP-other      45502422    2272       73       30         8        37

ICMP           14837957     125       24        5        12        34

IP-other          77406       5        0       47        52        27

Type DstIP(Port)         SrcIP(Port)      Pro TC  FlowLbl If(Direct)   Pkts

     DstMAC(VLAN)        SrcMAC(VLAN)

     TopLblType(IP/MASK) Lbl-Exp-S-List

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IP   2001::1(1024)      2002::1(21)        6   0   0x6000  GE1/0/1(I)  42996

MPLS LDP(3.3.3.3/24)    1:18-6-0                           GE1/0/2(O)  291

2:24-6-0

                        3:30-6-1

IP&  2003::1(2048)      2008::1(0)         1   0   0x0     GE1/0/2(O)  10

IP&  2010::1(1024)      2020::1(67)        17  0   0x12345 GE1/0/3(I)  1848

MPLS LDP(4.4.4.4/24)    1:55-6-0

                        2:16-6-1

                        2:0-0-0

\# 查看IPv6 NetStream流缓冲区信息。（分布式设备－独立运行模式）

\<Sysname\> display ipv6 netstream cache slot 1 verbose

IPv6 NetStream cache information:

Active flow timeout             : 60 min

  Inactive flow timeout           : 10 sec

  Max number of entries           : 1000

  IPv6 active flow entries        : 1

  MPLS active flow entries        : 2

  IPL2 active flow entries        : 1

  IPv6 flow entries counted       : 10

  MPLS flow entries counted       : 20

  IPL2 flow entries counted       : 20

  Last statistics resetting time  : 01/01/2000 at 00:01:02

IPv6 packet size distribution (1103746 packets in total):

1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480

.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000

512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608

.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000

Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)

                  Flows /sec       /sec   /flow   /flow       /flow

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

TCP-Telnet      2656855     372        4       86        49         27

TCP-FTP         5900082      86        9        9        11         33

TCP-FTPD        3200453    1006        5      193        45         33

TCP-WWW       546778274   11170      887       12         8         32

TCP-other      49148540    3752       79       47        30         32

UDP-DNS       117240379     570      190        3         7         34

UDP-other      45502422    2272       73       30         8         37

ICMP           14837957     125       24        5        12         34

IP-other          77406       5        0       47        52         27

 Type DstIP(Port)        SrcIP(Port)      Pro TC  FlowLbl If(Direct)   Pkts

      DstMAC(VLAN)       SrcMAC(VLAN)

      TopLblType(IP/MASK)Lbl-Exp-S-List

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IP   2001::1(1024)      2002::1(21)        6   0   0x0     ET1/1(I)    42996

     TcpFlag:    0x1b

DstMask:      24   SrcMask:      24

     DstAS:         0   SrcAS:         0

     NextHop:           2001::2

     BGPNextHop:        0:0:0:0:0:0:0:0

     InVRF:        10

SamplerMode:   0   SamplerInt:    0

     Active:      120   Bytes/Pkt:   152

MPLS LDP(3.3.3.3/24)    1:18-6-0                           GE1/0/2(O)  291

                        2:24-6-0

                        3:30-6-1

     SamplerMode:   0   SamplerInt:    0

     Active:      660   Bytes/Pkt:   100

IP&  2003::1(2048)      2008::1(0)         1   0   0x0     GE1/0/2(O)  10

IP&  2010::1(1024)      2020::1(67)        17  255 0x12345 GE1/0/3(I)  1848

MPLS LDP(4.4.4.4/24)    1:55-6-0

                        2:16-6-1

                        3:0-0-0

     TcpFlag:       0

     DstMask:      24   SrcMask:      24

     DstAS:         0   SrcAS:         0

NextHop:           2020::2

     BGPNextHop:        0:0:0:0:0:0:0:0

     InVRF:         0

SamplerMode:   0   SamplerInt:    0

     Active:      382   Bytes/Pkt:  1426

表1-1 display ipv6 netstream cache命令显示信息描述表

字段

描述

IPv6 NetStream cache information

IPv6 NetStream流缓存区信息

Active flow  timeout

活跃流的老化时间，单位为分钟

Inactive flow timeout

不活跃流的老化时间，单位为秒

Max number of entries

IPv6 NetStream流缓存区中允许的最大流数

IPv6 active flow entries

IPv6 NetStream流缓存区中活跃的IPv6流数

MPLS active flow entries

IPv6 NetStream流缓存区中活跃的MPLS流数

IPL2 active flow entries

IPv6 NetStream流缓存区中活跃的二层和三层流数

IPv6 flow entries counted

已经被统计的IPv6流数

MPLS flow entries counted

已经被统计的MPLS流数

IPL2 flow entries counted

已经被统计的二层和三层流数

Last statistics resetting time

上次清除统计的时间

该字段只在执行了**reset ipv6 netstream statistics**命令后才会显示为时间，否则显示为Never

IPv6 packet size distribution (1103746packets in total):

IPv6报文按大小分布情况，括号中为IPv6报文总数。分布值按各项占报文总数的比率显示，只显示3位小数，如".027"表示占IPv6报文总数的0.027

1-32   64   96  128  160  192  224  256  288 

320  352  384  416  448  480 512  544  576

1024 1536 2048 2560 3072 3584 4096 4608 \>4608

IPv6报文尺寸区间（报文长度不包括二层链路层的头）。长度不超过576字节时，以32字节为单位递增，例如："1-32"是长度为1～32个字节的报文数目，"64"是长度为33～64字节的报文数。长度超过1024字节时，以512字节为单位递增，例如"1536"是长度为1025～1536字节的报文数。长度为577～1024间的报文记录存放在1024项中。

Protocol     Total Flows     Packets/Sec

Flow/Sec   Packets/flow

Active(sec)/ flow   Idle(sec)/flow

按协议分类的报文统计信息：协议类型、总流数、每秒的报文数、每秒的流数、平均每条流的报文数、平均每条流的活跃时间、平均每条流的非活跃时间

Type DstIP(Port)        SrcIP(Port)        Pro TC  FlowLbl    If(Direct)   Pkts

当前流缓存区中活跃流的IP层信息： 流的类型、目的IPv6地址（目的端口号）、源IPv6地址（源端口号）、协议号、流量分类、流标签、接口名（方向）、包数

其中流的类型有四种：IP流（IP）、二三层混合流（IPL2）、不带IP选项的MPLS流（MPLS）、带IP选项的MPLS流（IP&MPLS）

需要注意的是，对于ICMPv6报文只有Type和Code字段，因此用目的端口号的高8位为Type字段、低8位为Code字段，源端口号为0

DstMAC(VLAN)          SrcMAC(VLAN)

当前流缓存区中活跃流的二层信息：目的MAC地址、目的VLAN ID、源MAC地址、源VLAN ID

TopLblType(IP/MASK)      Lbl-Exp-S-List

当前流缓存区中活跃流的MPLS信息：栈顶标签的类型（栈顶标签对应的IP地址及掩码长度）、标签列表

标签主要的三部分：

·20比特的Label字段表示标签值

·3比特的EXP字段用来实现QoS

·1比特S字段置1表示已达栈底

TcpFlag:

DstMask:   SrcMask:

DstAS:       SrcAS:

NextHop:

BGPNextHop:

OutVRF:     InVRF:

SamplerMode:                  SamplerInt:

Active:       Bytes/Pkt:

当前流缓存区中活跃流的其它信息：TCP标记、目的掩码、源掩码、目的自治系统、源自治系统、路由下一跳、BGP下一跳、出方向报文所属VPN 、入方向报文所属VPN、采样模式、采样间隔、流活跃时间、平均每个包的字节数

NetStream采样模式，目前支持三种：

·0：表示不采样，统计所有报文

·1：表示固定采样

·2：表示随机采样

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- display ipv6 netstream export**

------------------------------------------------------------------------

**[display ipv6 netstream export**]命令用来查看IPv6 NetStream统计输出报文的各种信息。

【命令】

**[display ipv6 netstream export **]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看IPv6 NetStream统计输出信息。

\<Sysname\> display ipv6 netstream export

as aggregation export information:

  Flow source interface                            : GigabitEthernet1/0/1

  Flow destination VPN instance                    : VPN1

  Flow destination IP address (UDP)                : 10.10.0.10 (30000)

  Version 9 exported flows number                  : 16

  Version 9 exported UDP datagrams number (failed) : 2 (0)

IPv6 export information:

  Flow source interface                           : GigabitEthernet1/0/1

  Flow destination VPN instance                   : VPN1

  Flow destination IP address (UDP)               : 10.10.0.10 (30000)

  Version 9 exported flows number                 : 16

  Version 9 exported UDP datagrams number (failed): 16 (0)

MPLS export information:

  Flow source interface                            : GigabitEthernet1/0/1

  Flow destination VPN instance                    : VPN1

  Flow destination IP address (UDP)                : 10.10.0.10 (30000)

  Version 9 exported flows number                  : 20

  Version 9 exported UDP datagrams number (failed) : 2 (0)

表1-2 display ipv6 netstream export命令显示信息描述表

字段

描述

IPv6 export information

IPv6 NetStream统计输出信息

Flow source interface

输出信息的源接口

Flow destination VPN instance

输出信息的目的地址所在的VPN

Flow destination IP address (UDP)

输出信息的目的IP地址（UDP端口号）

Version 9 exported flows number

使用版本9格式发送的流信息数

Version 9 exported UDP datagrams number (failed)

使用版本9格式发送的UDP报文数（发送失败的报文数）

MPLS export information

版本9的MPLS流统计输出信息

as aggregation export information

启用自治系统聚合的版本9统计输出信息

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- display ipv6 netstream template**

------------------------------------------------------------------------

**[display ipv6 netstream template**]命令用来查看IPv6 NetStream模板的配置和状态信息。

【命令】

集中式设备：

**[display ipv6 netstream template**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 netstream template** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 netstream template** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主用设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主用设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 查看IPv6 NetStream模板信息。

\<Sysname\> display ipv6 netstream template

 Flow template refresh frequency            : 20

 Flow template refresh interval             : 30 min

 Active flow templates                      : 4

 Created flow templates                     : 4

AS outbound template:

 Template ID                : 3293

 Field count                : 14

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Flows                        4

 Out packets                  8

 Out bytes                    8

 First forwarded              4

 Last forwarded               4

 Source AS                    4

 Destination AS               4

 Input Interface Index        4

 Output Interface Index       4

 IP protocol version          1

 Direction                    1

 Sampling algorithm           1

 PAD                          1

 Sampling interval            4

AS inbound template:

 Template ID                : 3292

 Field count                : 14

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Flows                        4

 In packets                   8

 In bytes                     8

 First forwarded              4

 Last forwarded               4

 Source AS                    4

 Destination AS               4

 Input Interface Index        4

 Output Interface Index       4

 IP protocol version          1

 Direction                    1

 Sampling algorithm           1

 PAD                          1

 Sampling interval            4

L3 outbound template:

 Template ID                : 3305

 Field count                : 27

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Out packets                  8

 Out bytes                    8

 First forwarded              4

 Last forwarded               4

 Input Interface Index        4

 Output Interface Index       4

 IPv6 source address          16

 IPv6 destination address     16

 IPv6 nexthop                 16

 PAD                          1

 IPv6 flow label              3

 Source AS                    4

Destination AS               4

 L4 source port               2

 L4 destination port          2

 IP protocol version          1

 TCP flags                    1

 Protocol                     1

 Source ToS                   1

 IPv6 source mask             1

 IPv6 destination mask        1

 Direction                    1

Forwarding offset            1

 Out VPN ID                   2

 Sampling algorithm           1

 PAD                          1

 Sampling interval            4

L3 inbound template:

 Template ID                : 3306

 Field count                : 27

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Out packets                  8

 Out bytes                    8

 First forwarded              4

 Last forwarded               4

 Input Interface Index        4

 Output Interface Index       4

 IPv6 source address          16

 IPv6 destination address     16

 IPv6 nexthop                 16

 PAD                          1

 IPv6 flow label              3

 Source AS                    4

Destination AS               4

 L4 source port               2

 L4 destination port          2

 IP protocol version          1

 TCP flags                    1

 Protocol                     1

 Source ToS                   1

 IPv6 source mask             1

 IPv6 destination mask        1

 Direction                    1

Forwarding offset            1

 Out VPN ID                   2

 Sampling algorithm           1

 PAD                          1

 Sampling interval            4

表1-3 display ipv6 netstream template命令显示信息描述表

字段

描述

Flow template refresh frequency

模板的包刷新率

Flow template refresh interval

模板的时间刷新率，单位为分钟

Active flow templates

当前激活的模板数

Created flow templates

创建的模板总数

根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"自治系统"聚合方式为例

AS outbound template

AS出方向模板信息

AS inbound template

AS入方向模板信息

Template ID

模板ID

Packets

使用该模板的发送报文数

Last template export time

该模板最近的一次输出时间

Field count

模板的域总数

Field type

域类型

Field length (bytes)

域长度，单位为字节

Flows

流数量

Out packets

输出的数据包个数

In packets

输入的数据包个数

Out bytes

输出的数据个数，单位为字节

In bytes

输入的数据个数，单位为字节

First forwarded

记录转发第一个报文时的系统时间，时间精确到毫秒

Last forwarded

记录转发最后一个报文时的系统时间，时间精确到毫秒

Source AS

源AS号

Destination AS

目的AS

Input interface index

输入接口的索引

Output interface index

输出接口的索引

Direction

方向字段

Sampling algorithm

采样算法

PAD

空白占位符

Sampling interval

采样率

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- enable**

------------------------------------------------------------------------

**[enable**]命令用来使能当前聚合视图对应的聚合功能。

**[undo enable**]命令用来关闭当前聚合视图对应的聚合功能。

【命令】

**[enable**]

**[undo enable**]

【缺省情况】

未使能当前聚合视图对应的聚合功能。

【视图】

IPv6 NetStream聚合视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能IPv6 NetStream的自治系统聚合功能。

\<Sysname\> system-view

Sysname ipv6 netstream aggregation as

Sysname-ns6-aggregation-as enable

【相关命令】

·**ipv6 netstream aggregation**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream**

------------------------------------------------------------------------

**[ipv6 netstream**]命令用来在全局或当前接口开启IPv6 NetStream功能。

**[undo ipv6 netstream**]命令用来在全局或当前接口关闭NetStream功能。

【命令】

系统视图：

**[ipv6 netstream**]

**[undo ipv6 netstream**]

接口视图：

**[ipv6 netstream**[ { **inbound** \| **outbound** }]]

**[undo ipv6 netstream**[ { **inbound** \| **outbound** }]]

【缺省情况】

IPv6 NetStream功能处于关闭状态。

【视图】

接口视图/系统视图

!(IPv6%20NetStream命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对入方向的流量进行IPv6 NetStream统计。

**[outbound**]：对出方向的流量进行IPv6 NetStream统计。

【使用指导】

全局开启IPv6 NetStream功能后，将开启所有接口入方向及出方向的IPv6 NetStream功能。

【举例】

\# 在GigabitEthernet1/0/1接口的入方向上开启IPv6 NetStream功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 netstream inbound

\# 全局开启IPv6 NetStream功能。

\<Sysname\> system-view

Sysname ipv6 netstream

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream { inbound \| outbound } filter**

------------------------------------------------------------------------

**[ipv6 netstream filter**]命令用来配置IPv6 NetStream过滤功能，根据指定ACL规则对报文进行过滤。

**[undo** **ipv6 netstream filter**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream**[ { **inbound** \| **outbound** } **filter acl** *acl-number*]]

**[undo ipv6 netstream**[ { **inbound** \| **outbound** } **filter**]]

【缺省情况】

未启用IPv6 NetStream过滤功能，此时统计所有IPv6报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：入方向过滤，即对从当前接口收到的报文进行过滤统计。

**[outbound**]：出方向过滤，即对从当前接口发出的报文进行过滤统计。

**[acl*** acl-number*]：ACL规则号，取值范围为2000～3999和4000～4999。

【举例】

\# 在接口GigabitEthernet1/0/1上配置根据规则号为2003的ACL规则进行出方向过滤。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 netstream outbound

Sysname-GigabitEthernet1/0/1 ipv6 netstream outbound filter acl 2003

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream { inbound \| outbound } sampler**

------------------------------------------------------------------------

!(IPv6%20NetStream命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 netstream sampler**]命令用来启用IPv6 NetStream采样功能。

**[undo ipv6 netstream sampler**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream**[ { **inbound** \| **outbound** } **sampler** *sampler-name*]]

**[undo ipv6 netstream**[ { **inbound** \| **outbound** } **sampler**]]

【缺省情况】

未启用IPv6 NetStream采样功能。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对入方向的报文进行采样。

**[outbound**]：对出方向的报文进行采样。

**[sampler ***sampler-name*]：采样器名称，为1～31个字符的字符串，不区分大小写。

【举例】

\# 在接口GigabitEthernet1/0/1上启用IPv6 NetStream采样功能，使用名为abc的采样器对入方向的报文进行采样，Netstream根据采样结果进行报文统计。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 netstream inbound

Sysname-GigabitEthernet1/0/1 ipv6 netstream inbound sampler abc

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream aggregation**

------------------------------------------------------------------------

!(IPv6%20NetStream命令.files/image001.png)

本命令中各参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 netstream aggregation**]命令用来设置IPv6 NetStream流聚合方式，并进入相应的IPv6 NetStream聚合视图。

**[undo ipv6 netstream aggregation**]命令用来关闭IPv6 NetStream流聚合方式，并删除流聚合方式相应的配置。

【命令】

**[ipv6 netstream aggregation**[ { **as** \| **bgp-nexthop** \| **destination-prefix** \| **prefix** \| **protocol-port** \| **source-prefix** }]]

**[undo ipv6 netstream aggregation**[ { **as** \| **bgp-nexthop** \| **destination-prefix** \| **prefix** \| **protocol-port** \| **source-prefix** }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[as**]：自治系统聚合，根据IPv6 NetStream流的源自治系统号、目的自治系统号、输入接口索引和输出接口索引4个关键项对流分类。

**[bgp-nexthop**]：边界网关-下一跳聚合，根据IPv6 NetStream流的BGP下一跳IPv6地址、输出接口索引2个关键项对流分类。

**[destination-prefix**]：目的前缀聚合，根据IPv6 NetStream流的目的自治系统号、目的掩码长度、目的前缀和输出接口索引4个关键项对流分类。

**[prefix**]：源和目的前缀聚合，根据IPv6 NetStream流的源自治系统号、目的自治系统号、源掩码长度、目的掩码长度，源前缀、目的前缀、输入接口索引和输出接口索引8个关键项对流分类。

**[protocol-port**]：协议-端口聚合，根据IPv6 NetStream流的协议号、源端口和目的端口3个关键项对流分类。

**[source-prefix**]：源前缀聚合，根据IPv6 NetStream流的源自治系统号、源掩码长度、源前缀和输入接口索引4个关键项对流分类。

【使用指导】

·在聚合视图下，可以启用或关闭聚合功能，以及设置IPv6 NetStream统计输出报文源接口、目的IPv6地址以及目的端口号。

·如果一条流同时满足多个聚合方式，则该流会被统计到多个聚合流中。

【举例】

\# 进入IPv6 NetStream自治系统聚合视图。

\<Sysname\> system-view

Sysname ipv6 netstream aggregation as

【相关命令】

·**enable**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream aggregation advanced**

------------------------------------------------------------------------

![说明](IPv6%20NetStream命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ipv6 netstream aggregation advanced**]命令用来配置硬件流聚合功能。

**[undo ipv6 netstream aggregation advanced**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream aggregation advanced**]

**[undo ipv6 netstream aggregation advanced**]

【缺省情况】

IPv6 NetStream硬件流聚合功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·使能硬件流聚合功能时，系统根据IPv6 NetStream统计功能是否配置了统计信息的目的地址以及配置的聚合类型来决定是否进行硬件聚合。如果在系统视图下配置了统计信息输出的目的地址或配置了硬件聚合不支持配置的聚合类型，则硬件聚合配置不生效。

·使能硬件流聚合以后，硬件聚合流表项添加到普通流表项记录中，并进行表项的输出。

【举例】

\# 使能硬件流聚合功能。

\<Sysname\> system-view

Sysname ipv6 netstream aggregation advanced

【相关命令】

·**ipv6 netstream export host**

·**ipv6 netstream aggregation**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export host**

------------------------------------------------------------------------

**[ipv6 netstream export host**]命令用来配置IPv6 NetStream统计输出报文的目的地址和目的UDP端口号。

**[undo ipv6 netstream export host**]命令用来删除已有配置。

【命令】

**[ipv6 netstream export host**[ { *ip-address \| ipv6-address* } *udp-port* [ **vpn-instance** *vpn-instance-name* ]]]

**[undo ipv6 netstream export host**[ [ *ip-address \| ipv6-address* [ **vpn-instance** *vpn-instance-name* ] ]]]

【缺省情况】

系统视图和聚合视图下均没有配置目的地址和目的UDP端口号。

【视图】

系统视图/IPv6 NetStream聚合视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：IPv6 NetStream统计输出报文的IPv4目的地址。

*[Ipv6-address*]：IPv6 NetStream统计输出报文的IPv6目的地址。

*[udp-port*]：IPv6 NetStream统计输出报文的目的UDP端口号，取值范围为0～65535。

**[vpn-instance ***vpn-instance-name*]：指定IPv6 NetStream统计输出报文的目的地址所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示IPv6 NetStream统计输出报文的目的地址位于公网中。

【使用指导】

·若某类聚合视图没有使能，则无法通过**display ipv6 netstream export**命令查看它的相关信息（包括目的地址的目的UDP端口号）。

·执行**undo ipv6 netstream export host**命令时未指定地址，表示取消指定本视图下配置的所有地址。

·不同聚合视图下可以配置相同的目的地址和目的UDP端口号。

·若聚合视图下没有配置目的地址和目的UDP端口号，则使用系统视图下的配置；若聚合视图下配置了目的地址和目的UDP端口号，则使用聚合视图下的配置。

·一个视图下最多可配置4组IPv4目的地址，包括不同VPN实例。在同一视图下，若先后配置了IPv4地址相同、UDP端口号不同的目的地址，则后配置的目的地址生效。在用户配置了不同的VPN实例名称时，允许配置相同的IP地址和UDP端口号。

·一个视图下最多可配置4组IPv6目的地址，包括不同VPN实例。在同一视图下，若先后配置了IPv6地址相同、UDP端口号不同的目的地址，则后配置的目的地址生效。在用户配置了不同的VPN实例名称时，允许配置相同的IPv6地址和UDP端口号。

·普通流统计输出报文会发给系统视图下配置的所有目的地址。聚合流统计输出报文会发给聚合类型对应的聚合视图下配置的所有目的地址。为了减少对网络带宽的占用，可以只在聚合视图下配置**ipv6 netstream export host**命令，此时设备只会输出聚合流信息。

·在执行**undo ipv6 netstream export host**命令时，如果未指定IP地址，则取消本视图下配置的所有IP地址。

【举例】

\# 配置全局IPv6 NetStream统计输出报文的目的IP地址为1.1.1.1，UDP端口号为5000。

\<Sysname\> system-view

Sysname ipv6 netstream export host 1.1.1.1 5000

\# 配置IPv6 NetStream自治系统聚合统计输出报文的目的地址为1.1.1.2，UDP端口号为6000。

\<Sysname\> system-view

Sysname ipv6 netstream aggregation as

Sysname-ns6-aggregation-as ipv6 netstream export host 1.1.1.2 6000

【相关命令】

·**ipv6 netstream aggregation**

·**ipv6 netstream export source**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export rate**

------------------------------------------------------------------------

**[ipv6 netstream export rate**]命令用来配置输出速率限制，即限制每秒钟输出的报文数。

**[undo ipv6 netstream export rate**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream export******rate*** rate*]

**[undo ipv6 netstream export******rate**]

【缺省情况】

NetStream统计输出报文的输出速率不受限制。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：IPv6 NetStream统计输出报文的输出速率限制，取值范围为1～1000，单位为每秒允许输出的最多报文个数。

【举例】

\# 设置每秒最多允许10个报文被输出。

\<Sysname\> system-view

Sysname ipv6 netstream export rate 10

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export source**

------------------------------------------------------------------------

**[ipv6 netstream export source**]命令用来配置IPv6 NetStream统计输出报文的源接口。

**[undo ipv6 netstream export source**]命令用来取消配置的输出报文的源接口。

【命令】

**[ipv6 netstream export source interface** *interface-type interface-number*]

**[undo ipv6 netstream export source**]

【缺省情况】

采用统计输出报文的出接口作为源接口。

【视图】

系统视图/IPv6 NetStream聚合视图

【参数】

*[interface-type interface-number*]：IPv6 NetStream统计输出报文的源接口，由接口类型和接口编号组成。

【使用指导】

·通过本命令配置源接口后，会将NetStream统计输出报文的源IPv6地址设置为该接口的IPv6地址。

·不同聚合视图下可以配置不同的源接口。

·聚合视图下若没有配置源接口，则使用系统视图下的配置。

·建议使用以太网管理接口作为源接口，与服务器相连，并向服务器输出统计信息。

【举例】

\# 将全局IPv6 NetStream统计输出报文源接口设置为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname ipv6 netstream export source interface gigabitethernet 1/0/1

\# 将IPv6 NetStream自治系统聚合统计输出报文源接口设置为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname ipv6 netstream aggregation as

Sysname-ns6-aggregation-as ipv6 netstream export source interface gigabitethernet 1/0/2

【相关命令】

·**ipv6 netstream aggregation**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export v9-template refresh-rate packet**

------------------------------------------------------------------------

**[ipv6 netstream export v9-template refresh-rate packet**]命令用来配置IPv6 NetStream统计输出报文版本9模板的包刷新率。

**[undo ipv6 netstream export v9-template refresh-rate packet**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream export v9-template refresh-rate packet ***packets*]

**[undo ipv6 netstream export v9-template refresh-rate packet**]

【缺省情况】

每隔20个包设备发送一次版本9模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[packets*]：IPv6 NetStream统计输出报文版本9模板的包刷新率，取值范围为1～600，单位为上报报文的个数，即每隔多少个包发送一次模板，通知NetStream服务器最新的版本9模版格式。

【使用指导】

版本9是基于模板方式的、可支持自定义格式，所以设备上需要定期刷新模板，并通知NetStream服务器最新的版本9模版格式。用户可以根据实际情况，配置版本9模板的包刷新率，及时更新模板。

可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给NetStream服务器。

【举例】

\# 将IPv6 NetStream统计输出报文版本9模板的包刷新率设为100。

\<Sysname\> system-view

Sysname ipv6 netstream export v9-template refresh-rate packet 100

【相关命令】

·**ipv6 netstream export v9-template refresh-rate time**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export v9-template refresh-rate time**

------------------------------------------------------------------------

**[ipv6 netstream export v9-template refresh-rate time**]命令用来配置IPv6 NetStream统计输出报文版本9模板的时间刷新率。

**[undo ipv6 netstream export v9-template refresh-rate time**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream export v9-template refresh-rate time ***minutes*]

**[undo ipv6 netstream export v9-template refresh-rate time**]

【缺省情况】

每隔30分钟设备发送一次版本9模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：IPv6 NetStream统计输出报文版本9模板的时间刷新率，取值范围为1～3600，单位为分钟，即每隔多少分钟更新一次模板，通知NetStream服务器最新的V9模版格式。

【使用指导】

V9版本是基于模板方式的、可支持自定义格式，所以设备上需要定期刷新模板，并通知NetStream服务器最新的V9模版格式。用户可以根据实际情况，配置版本9模板的时间刷新率，及时更新模板。

可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给NetStream服务器。

【举例】

\# 将IPv6 NetStream统计输出报文版本9模板的时间刷新率设为60分钟。

\<Sysname\> system-view

Sysname ipv6 netstream export v9-template refresh-rate time 60

【相关命令】

·**ipv6 netstream export v9-template refresh-rate packet**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export version 9**

------------------------------------------------------------------------

**[ipv6 netstream export version 9**]命令用来配置IPv6 NetStream版本9的自治系统选项和BGP下一跳选项。

**[undo ipv6 netstream export version**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream export version**[ **9** [ **origin-as** \| **peer-as** ]  **bgp-nexthop** ]]

**[undo ipv6 netstream export version**]

【缺省情况】

IPv6普通流信息、IPv6聚合统计流信息和带IPv6选项信息的MPLS流信息都通过版本9的NetStream统计输出报文发送。流统计信息中记录邻接自治系统号（peer-as），流信息中不记录BGP下一跳地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[origin-as**]：流信息中记录的自治系统号为起始自治系统号。

**[peer-as**]：流信息中记录的自治系统号为邻接自治系统号。

**[bgp-nexthop**]：流信息中记录BGP下一跳。

【使用指导】

·IPv6 NetStream流信息中会记录流的源IPv6地址及其对应的自治系统号；目的IPv6地址及其对应的自治系统号。设备会根据用户实际配置的自治系统参数来确定记录的自治系统号。

·在使用ipv6 netstream export version 9配置输出版本信息时，如果没有配置任何选项，则流统计信息中记录邻接自治系统号（peer-as），流信息中不记录BGP下一跳地址。

【举例】

\# 将IPv6 NetStream统计采用起始自治系统号作为给定IPv6地址的自治系统号。

\<Sysname\> system-view

Sysname ipv6 netstream export version 9 origin-as

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream max-entry**

------------------------------------------------------------------------

**[ipv6 netstream max-entry**]命令用来配置IPv6 NetStream流缓存区中流表项的最大数目，或者达到流表项的最大数目时的处理方式。

**[undo ipv6 netstream max-entry**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream max-entry**[ { *max-entries* \| **aging** \| **disable-caching** }]]

**[undo ipv6 netstream max-entry**]

【缺省情况】

本命令的缺省情况与设备的型号相关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-entries*]：IPv6 NetStream流缓存区中流表项的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[aging**]：达到流表项的最大数目时，强制老化部分流表项。

**[disable-caching**]：达到流表项的最大数目时，禁止新建流表项。

【使用指导】

·*max-entries*参数值在各单板上单独生效，而不是各单板的总和。（分布式设备－独立运行模式/分布式设备－IRF模式）

·*max-entries*参数值在各成员设备上单独生效，而不是各成员设备的总和。（集中式IRF设备）

·**ipv6 netstream max-entry** *max-entries*命令可重复配置，以最后一次配置为准。

[·**ipv6 netstream max-entry**[ { **aging** \| **disable-caching** }]]命令可重复配置，以最后一次配置为准。

【举例】

\# 设置IPv6 NetStream流缓存区中流表项的最大数目为5000。

\<Sysname\> system-view

Sysname ipv6 netstream max-entry 5000

\# 设置IPv6 NetStream在达到流表项的最大数目时，禁止新建流表项。

\<Sysname\> system-view

Sysname ipv6 netstream max-entry disable-caching

\# 设置IPv6 NetStream在达到流表项的最大数目时，强制老化部分流表项。

\<Sysname\> system-view

Sysname ipv6 netstream max-entry aging

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream timeout active**

------------------------------------------------------------------------

**[ipv6 netstream timeout active**]命令用来配置流的活跃老化时间。

**[undo ipv6 netstream timeout active**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream timeout active** *minutes*]

**[undo ipv6 netstream timeout active**]

【缺省情况】

流的活跃老化时间为30分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：流的活跃老化时间，取值范围为1～60，单位为分钟。

【使用指导】

从采集到的第一个报文开始，该流在指定的时间内能被采集到，则该流属于活跃的流，指定的时间称为流的活跃老化时间。

【举例】

\# 将流的活跃老化时间设置为60分钟。

\<Sysname\> system-view

Sysname ipv6 netstream timeout active 60

【相关命令】

·**ipv6 netstream timeout inactive**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream timeout inactive**

------------------------------------------------------------------------

**[ipv6 netstream timeout inactive**]命令用来配置流的不活跃老化时间。

**[undo ipv6 netstream timeout inactive**]命令用来恢复缺省情况。

【命令】

**[ipv6 netstream timeout inactive** *seconds*]

**[undo ipv6 netstream timeout inactive**]

【缺省情况】

流的不活跃老化时间为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：流的不活跃老化时间，取值范围为10～600，单位为秒。

【使用指导】

从采集到的最后一个报文开始，该流在指定的时间内没有被采集到，则该流属于不活跃的流，指定的时间称为流的不活跃老化时间。

【举例】

\# 将流的不活跃老化时间设置为60秒。

\<Sysname\> system-view

Sysname ipv6 netstream timeout inactive 60

【相关命令】

·**ipv6 netstream timeout active**

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- reset ipv6 netstream statistics**

------------------------------------------------------------------------

**[reset ipv6** **netstream statistics**]命令用来将流缓存区中所有流强制老化，输出报文信息，并清空IPv6 NetStream缓冲区的状态信息。

【命令】

**[reset ipv6** **netstream statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在执行清除缓冲区中老化流的动作时，命令行会给出提示，告知用户这个动作可能要持续几分钟，在这段时间内不能统计。

【举例】

\# 将流缓存区中所有流老化，并清空IPv6 NetStream缓冲区的状态信息和输出报文信息。

\<Sysname\> reset ipv6 netstream statistics

This process may take a few minutes.

NetStream statistic function is disabled during this process.
