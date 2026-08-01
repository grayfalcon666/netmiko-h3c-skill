<!-- CMD-INDEX
  display ip netstream cache          | 任意视图             | L25
  display ip netstream export         | 任意视图             | L467
  display ip netstream template       | 任意视图             | L705
  enable                              | NetStream聚合视图    | L1157
  ip netstream                        | 系统视图/接口视图        | L1199
  ip netstream { inbound \| outbound } filter | 接口视图             | L1271
  ip netstream { inbound \| outbound } mirror-to |                  | L1325
  ip netstream { inbound \| outbound } sampler | 接口视图             | L1401
  ip netstream aggregation            | 系统视图             | L1449
  ip netstream aggregation advanced   | 系统视图             | L1523
  ip netstream export host            | 系统视图/NetStream聚合视图 | L1577
  ip netstream export rate            | 系统视图             | L1649
  ip netstream export source          | 系统视图/NetStream聚合视图 | L1689
  ip netstream export v9-template refresh-rate packet | 系统视图             | L1749
  ip netstream export v9-template refresh-rate time | 系统视图             | L1799
  ip netstream export version         | 系统视图             | L1849
  ip netstream max-entry              | 系统视图             | L1909
  ip netstream mpls                   | 系统视图             | L1977
  ip netstream timeout active         | 系统视图             | L2033
  ip netstream timeout inactive       | 系统视图             | L2081
  reset ip netstream statistics       | 用户视图             | L2129
-->

**NetStream \-- NetStream配置命令 \-- display ip netstream cache**

------------------------------------------------------------------------

**[display ip netstream cache**]命令用来查看NetStream流缓存区的配置和状态信息。

【命令】

集中式设备：

**[display ip netstream cache ** **verbose** ]

分布式设备－独立运行模式/集中式IRF设备：

**[display ip netstream** **cache** [ **slot** *slot-number* [ *cpu cpu-number*  ]  **verbose** ]]

分布式设备－IRF模式：

**[display ip netstream** **cache** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息。*slot-number*表示成员设备在IRF中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的信息。*slot-number*表示成员设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number slot* *slot-number*]：显示指定成员设备上指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number slot* *slot-number*]：显示指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示NetStream流缓冲区的详细信息。

【举例】

\# 查看NetStream流缓冲区详细信息。（集中式设备）

\<Sysname\> display ip netstream cache verbose

IP NetStream cache information:

  Active flow timeout             : 60 min

  Inactive flow timeout           : 10 sec

  Max number of entries           : 1000

  IP active flow entries          : 1

  MPLS active flow entries        : 2

  L2 active flow entries          : 1

  IPL2 active flow entries        : 1

  IP flow entries counted         : 10

  MPLS flow entries counted       : 20

  L2 flow entries counted         : 10

  IPL2 flow entries counted       : 20

  Last statistics resetting time  : 01/01/2000 at 00:01:02

IP packet size distribution (1103746 packets in total):

1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480

.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000

 512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608

.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000

Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)

                  Flows /sec       /sec   /flow   /flow       /flow

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

TCP-Telnet      2656855     372        4       86          49        27

TCP-FTP         5900082      86        9        9          11        33

TCP-FTPD        3200453    1006        5      193          45        33

TCP-WWW       546778274   11170      887       12           8        32

TCP-other      49148540    3752       79       47          30        32

UDP-DNS       117240379     570      190        3           7        34

UDP-other      45502422    2272       73       30           8        37

ICMP           14837957     125       24        5          12        34

IP-other          77406       5        0       47          52        27

Type DstIP(Port)            SrcIP(Port)            Pro ToS If(Direct)  Pkts

     DstMAC(VLAN)           SrcMAC(VLAN)

     TopLblType(IP/Mask)    Lbl-Exp-S-List

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IP   11.1.1.1(1024)         11.1.1.2(21)           6   128 ET1/1(I)    42996

   TCPFlag:      27

     DstMask:      24       SrcMask:      24       NextHop:      0.0.0.0

     DstAS:         0       SrcAS:         0       BGPNextHop:   0.0.0.0

InVRF:        10

     SamplerMode:   2       SamplerInt:  256

     Active:  120.600       Bytes/Pkt:   152

L2   0012-3f86-e94c(10)     0012-3f86-e86a(0)              GE1/4/1(I)  1253

     SamplerMode:   1       SamplerInt:   64

     Active:    5.510       Bytes/Pkt:   210

MPLS LDP(3.3.3.3/24)        1:18-6-0                       GE1/0/2(O)  291

2:24-6-0

                            3:30-6-1

     SamplerMode:   0       SamplerInt:    0

     Active:  660.084       Bytes/Pkt:   100

IP&  192.168.123.1(2048)    192.168.1.1(0)         1   0   GE1/0/2(O)  10

L2   0012-3f86-e95d(0)      0012-3f86-e116(1008)

TCPFlag:      27

     DstMask:      24       SrcMask:      24       NextHop:    192.168.1.2

     DstAS:         0       SrcAS:         0       BGPNextHop: 0.0.0.0

     OutVRF:        0       TCPFlag:    0

     SamplerMode:   0       SamplerInt:    0

     Active:   12.030       Bytes/Pkt:    86

IP&  172.16.1.1(68)         172.16.2.1(67)         17  64  GE1/0/3(I)  1848

MPLS LDP(4.4.4.4/24)        1:55-6-0

                            2:16-6-1

     TCPFlag:       0

     DstMask:      24       SrcMask:      24       NextHop:    172.16.2.10

     DstAS:         0       SrcAS:         0       BGPNextHop: 0.0.0.0

InVRF:         0

     SamplerMode:   0       SamplerInt:    0

     Active:  382.542       Bytes/Pkt:  1426

\# 查看NetStream流缓冲区详细信息。（分布式设备－独立运行模式）

\<Sysname\> display ip netstream cache slot 1 verbose

IP NetStream information:

  Active flow timeout                : 60 min

  Inactive flow timeout              : 10 sec

  Max number of entries              : 1000

  IP active flow entries             : 1

  MPLS active flow entries           : 2

  L2 active flow entries             : 1

  IPL2 active flow entries           : 1

  IP flow entries counted            : 10

  MPLS flow entries counted          : 20

  L2 flow entries counted            : 10

  IPL2 flow entries counted          : 20

  Last statistics resetting time     : 01/01/2012 at 00:01:02

IP packet size distribution (1103746 packets in total):

1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480

.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000

 512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608

.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000

Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)

                  Flows /sec       /sec   /flow   /flow       /flow

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

TCP-Telnet      2656855     372        4       86          49        27

TCP-FTP         5900082      86        9        9          11        33

TCP-FTPD        3200453    1006        5      193          45        33

TCP-WWW       546778274   11170      887       12           8        32

TCP-other      49148540    3752       79       47          30        32

UDP-DNS       117240379     570      190        3           7        34

UDP-other      45502422    2272       73       30           8        37

ICMP           14837957     125       24        5          12        34

IP-other          77406       5        0       47          52        27

Type DstIP(Port)            SrcIP(Port)            Pro ToS If(Direct)  Pkts

     DstMAC(VLAN)           SrcMAC(VLAN)

     TopLblType(IP/Mask)    Lbl-Exp-S-List

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

IP   11.1.1.1(1024)         11.1.1.2(21)           6   128 ET1/1(I)    42996

     TCPFlag:      27

     DstMask:      24       SrcMask:      24       NextHop:      0.0.0.0

     DstAS:         0       SrcAS:         0       BGPNexthop:   0.0.0.0

InVRF:        10

     SamplerMode:   2       SamplerInt:  256

     Active:  120.600       Bytes/Pkt:   152

L2   0012-3f86-e94c(10)     0012-3f86-e86a(0)              GE1/4/1(I)  1253

     SamplerMode:   1       SamplerInt:   64

     Active:    5.510       Bytes/Pkt:   210

MPLS LDP(3.3.3.3/24)        1:18-6-0                       GE1/0/2(O)  291

                            2:24-6-0

                            3:30-6-1

     SamplerMode:   0       SamplerInt:    0

     Active:  660.084       Bytes/Pkt:   100

IP&  192.168.123.1(2048)    192.168.1.1(0)         1   0   GE1/0/2(O)  10

L2   0012-3f86-e95d(0)      0012-3f86-e116(1008)

     DstMask:      24       SrcMask:      24       NextHop:    192.168.1.2

     DstAS:         0       SrcAS:         0       BGPNexthop: 0.0.0.0

     OutVRF:        0       TCPFlag:    0

     SamplerMode:   0       SamplerInt:    0

     Active:   12.030       Bytes/Pkt:    86

IP&  172.16.1.1(68)         172.16.2.1(67)         17  64  GE1/0/3(I)  1848

MPLS LDP(4.4.4.4/24)        1:55-6-0

                            2:16-6-1

     DstMask:      24       SrcMask:      24       NextHop:    172.16.2.10

     DstAS:         0       SrcAS:         0       BGPNextHop: 0.0.0.0

InVRF:         0

     SamplerMode:   0       SamplerInt:    0

     Active:  382.542       Bytes/Pkt:  1426

表1-1 display ip netstream cache命令显示信息描述表

字段

描述

IP NetStream information

NetStream流缓存区信息

Active flow timeout

活跃流的老化时间，单位为分钟

Inactive flow timeout

不活跃流的老化时间，单位为秒

Max number of entries

NetStream流缓存区中允许的最大流数

IP active flow entries

NetStream流缓存区中活跃的IP流数

MPLS active flow entries

NetStream流缓存区中活跃的MPLS流数

L2 active flow entries

NetStream流缓存区中活跃的二层流数

IPL2 active flow entries

NetStream流缓存区中活跃的二层和三层流数

IP flow entries counted

已经被统计的IP流数

MPLS flow entries counted

已经被统计的MPLS流数

L2 flow entries counted

已经被统计的二层流数

IPL2 flow entries counted

已经被统计的二层和三层流数

Last statistics resetting time

上次清除统计的时间

该字段只在执行了**reset ip netstream statistics**命令后才会显示为时间，否则显示为Never

IP packet size distribution (1103746 packets in total)

IP报文按大小分布情况，括号中为IP报文总数。

分布值按占IP报文总数的比率显示，只显示3位小数，如".027"表示占IP报文总数的0.027

1-32   64   96  128  160  192  224  256  288

320  352  384  416  448  480 512  544  576

1024 1536 2048 2560 3072 3584 4096 4608

IP报文尺寸区间（报文长度不包括二层链路层的头）。长度不超过576字节时，以32字节为单位递增，例如："1-32"是长度为1～32个字节的报文数目，"64"是长度为33～64字节的报文数。长度超过1024字节时，以512字节为单位递增，例如"1536"是长度为1025～1536字节的报文数。长度在577～1024间的报文记录在1024项中

Protocol     Total Flows     Packets /sec

Flows/sec   Packets/flow

Active(sec)/flow     Idle(sec)/flow

按协议分类的报文统计信息：协议类型、总流数、每秒的报文数、每秒的流数、平均每条流的报文数、平均每条流的活跃时间、平均每条流的非活跃时间

Type DstIP(Port)            SrcIP(Port)            Pro ToS If(Direct)  Pkts

当前流缓存区中活跃流的IP层信息：流的类型、目的IP地址（目的端口号）、源IP地址（源端口号）、协议号、服务类型、接口名（方向）、包数

其中流的类型有五种：IP流（IP）、二层流（L2）、二三层混合流（IP&L2）、不带IP选项的MPLS流（MPLS)、带IP选项的MPLS流（IP&MPLS）

需要注意的是，对于ICMP报文只有Type和Code字段，因此用目的端口号的高8位为Type字段、低8位为Code字段，源端口号为0

DstMAC(VLAN)          SrcMAC(VLAN)

当前流缓存区中活跃流的二层信息：目的MAC地址、目的VLAN ID、源MAC地址、源VLAN ID

TopLblType(IP/Mask)      Lbl-Exp-S-List

当前流缓存区中活跃流的MPLS信息：栈顶标签的类型（栈顶标签对应的IP地址及掩码长度）、标签列表

标签列表中至多列出三层标签

TCPFlag:

DstMask:      SrcMask:             NextHop:

DstAS:           SrcAS:            BGPNextHop:

OutVRF:       InVRF:

SamplerMode:                     SamplerInt:

Active:       Bytes/Pkt:

当前流缓存区中活跃流的其他信息：TCP标记、目的掩码、源掩码、路由下一跳、目的自治系统、源自治系统、BGP下一跳、出方向报文所属VPN、入方向报文所属VPN、采样模式、采样间隔、流活跃时间、平均每个包的字节数

NetStream采样模式，目前支持三种：

·0：表示不采样，统计所有报文

·1：表示固定采样

·2：表示随机采样

**NetStream \-- NetStream配置命令 \-- display ip netstream export**

------------------------------------------------------------------------

**[display ip netstream export**]命令用来查看NetStream统计输出报文的各种信息。

【命令】

**[display ip netstream export**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

·路由应用

\# 查看NetStream统计输出信息。

\<Sysname\> display ip netstream export

IP export information:

  Flow source interface                            : GigabitEthernet1/0/1

  Flow destination VPN instance                    : VPN1

  Flow destination IP address (UDP)                : 10.10.0.10 (30000)

  Version 5 exported flows number                  : 16

  Version 5 exported UDP datagrams number (failed) : 16 (0)

  Version 9 exported flows number                  : 20

  Version 9 exported UDP datagrams number (failed) : 2 (0)

MPLS export information:

  Flow source interface                            : GigabitEthernet1/0/1

  Flow destination VPN instance                    : VPN1

  Flow destination IP address (UDP)                : 10.10.0.10 (30000)

  Version 9 exported flows number                  : 20

  Version 9 exported UDP datagrams number (failed) : 2 (0)

as aggregation export information:

  Flow source interface                            : GigabitEthernet1/0/1

  Flow destination VPN instance                    : VPN1

  Flow destination IP address (UDP)                : 10.10.0.10 (30000)

  Version 8 exported flows number                  : 16

  Version 8 exported UDP datagrams number (failed) : 2 (0)

  Version 9 exported flows number                  : 16

  Version 9 exported UDP datagrams number (failed) : 2 (0)

表1-2 display ip netstream export命令显示信息描述表

字段

描述

IP export information

版本5和版本9统计输出信息

Flow source interface

输出信息的源接口

Flow destination VPN instance

输出信息的目的地址所在的VPN

Flow destination IP address (UDP)

输出信息的目的IP地址（UDP端口号）

Version 5 exported flows number

使用版本5格式发送的流信息数

Version 5 exported UDP datagrams number (failed)

使用版本5格式发送的UDP报文数（发送失败的报文数）

Version 9 exported flows number

使用版本9格式发送的流信息数

Version 9 exported UDP datagrams number (failed)

使用版本9格式发送的UDP报文数（发送失败的报文数）

MPLS export information

版本9的MPLS流统计输出信息

根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"自治系统"聚合方式为例

as aggregation export information

启用自治系统聚合的版本8统计输出信息

Version 8 exported flows number

使用版本8格式发送的流信息数

Version 8 exported UDP datagrams number (failed)

使用版本8格式发送的UDP报文数（发送失败的报文数）

·交换应用

\# 查看NetStream统计输出信息。

\<Sysname\> display ip netstream export

IP export information:

  Flow source interface                           : Vlan-interface2

  Flow destination VPN instance                   : Not specified

  Flow destination IP address (UDP)               : 192.168.0.5 (5000)

  Version 5 exported flows number                 : 27

  Version 5 exported UDP datagrams number (failed): 21 (0)

  Version 9 exported flows number                 : 0

  Version 9 exported UDP datagram number (failed) : 0 (0)

L2 export information:

  Flow source interface                           : Vlan-interface2

  Flow destination VPN instance                   : Not specified

  Flow destination IP address (UDP)               : 192.168.0.5 (5000)

  Version 9 exported flows number                 : 0

  Version 9 exported UDP datagrams number (failed): 0 (0)

protocol-port aggregation export information:

Flow source interface                           : Vlan-interface2

  Flow destination VPN instance                   : Not specified

  Flow destination IP address (UDP)               : 192.168.0.5 (5000)

  Version 8 exported flows number                 : 24

  Version 8 exported UDP datagrams number (failed): 21 (0)

  Version 9 exported flows number                 : 0

  Version 9 exported UDP datagrams number (failed): 0 (0)

表1-3 display ip netstream export命令显示信息描述表

字段

描述

IP export information

版本5和版本9统计输出信息

Flow source interface

输出信息的源接口

Flow destination VPN instance

输出信息的目的地址所在的VPN

Flow destination IP address (UDP)

输出信息的目的IP地址（UDP端口号）

Version 5 exported flows number

使用版本5格式发送的流信息数

Version 5 exported UDP datagram number (failed)

使用版本5格式发送的UDP报文数（发送失败的报文数）

Version 9 exported flows number

使用版本9格式发送的流信息数

Version 9 exported UDP datagram number (failed)

使用版本9格式发送的UDP报文数（发送失败的报文数）

L2 export information

二层流统计输出信息

根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"协议－端口"聚合方式为例

protocol-port aggregation export information

启用协议－端口聚合的版本8统计输出信息

Version 8 exported flows number

使用版本8格式发送的流信息数

Version 8 exported UDP datagram number (failed)

使用版本8格式发送的UDP报文数（发送失败的报文数）

**NetStream \-- NetStream配置命令 \-- display ip netstream template**

------------------------------------------------------------------------

**[display ip netstream template**]命令用来查看NetStream模板的配置和状态信息。

【命令】

集中式设备：

**[display ip netstream template**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ip netstream template** [ **slot** *slot-number* [ *cpu cpu-number*  ]]]

分布式设备－IRF模式：

**[display ip netstream template** [ **chassis** *chassis-number* **slot** *slot-number* [ *cpu cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板上的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的信息。*slot-number*表示成员设备在IRF中的成员编号。如果未指定本参数，将显示主用设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的信息。*slot-number*表示成员设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主用设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number slot* *slot-number*]：显示指定成员设备上指定单板的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number slot* *slot-number*]：显示指定单板的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

·路由应用

\# 使能自治系统聚合。查看NetStream模板信息。

\<Sysname\> display ip netstream template

 Flow template refresh frequency            : 20

 Flow template refresh interval             : 30 min

 Active flow templates                      : 2

 Created flow templates                     : 2

AS outbound template:

 Template ID                : 3258

 Packets                    : 0

 Last template export time  : Never

 Field count                : 14

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Flows                        4

 Out packets                  8

 Out bytes                    8

 First forwarded              4

 Last forwarded               4

 Source AS                    4

 Destination AS               4

 Input interface index        4

 Output interface index       4

 Direction                    1

 Sampling algorithm           1

 PAD                          1

 Sampling interval            4

AS inbound template:

 Template ID                : 3257

 Packets                    : 0

 Last template export time  : Never

 Field count                : 14

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Flows                        4

 In packets                   8

 In bytes                     8

 First forwarded              4

 Last forwarded               4

 Source AS                    4

 Destination AS               4

 Input interface index        4

 Output interface index       4

 Direction                    1

 Sampling algorithm           1

 PAD                          1

 Sampling interval            4

表1-4 display ip netstream template命令显示信息描述表

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

聚合流数量

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

·交换应用

\# 使能协议－端口聚合。查看NetStream模板信息。

\<Sysname\> display ip netstream template

 Flow template refresh frequency            : 20

 Flow template refresh interval             : 30 min

 Active flow templates                      : 8

 Created flow templates                     : 8

Protocol port outbound template:

 Template ID                : 3272

 Field count                : 16

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Flows                        4

 Out packets                  8

 Out bytes                    8

 First forwarded              4

 Last forwarded               4

 Protocol                     1

Direction                    1

 PAD                          1

 PAD                          1

 L4 source port               2

 L4 destination port          2

 Sampling algorithm           1

PAD                          1

 Sampling interval            4

Protocol-port inbound template:

 Template ID                : 3271

 Field count                : 16

 Field type                   Field length (bytes)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Flows                        4

 In packets                   8

 In bytes                     8

 First forwarded              4

 Last forwarded               4

 Protocol                     1

Direction                    1

 PAD                          1

 L4 source port               2

 L4 destination port          2

 Sampling algorithm           1

PAD                          1

 Sampling interval            4

表1-5 display ip netstream template命令显示信息描述表

字段

描述

Flow template refresh frequency

模板的包刷新率

Flow template refresh interval

模板的时间刷新率，单位为分钟

Active flow templates

当前活跃的模板数

Created flow templates

创建的模板总数

根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"协议－端口聚合"聚合方式为例

Protocol-port outbound template

协议－端口聚合出方向模板信息

Protocol-port inbound template

协议－端口聚合入方向模板信息

Template ID

模板ID

Field count

模板的域总数

Field type

域类型

Field length (bytes)

域长度，单位为字节

Flows

聚合流数量

Out packets

输出的数据包大小

In packets

输入的数据包大小

Out bytes

输出的数据大小，单位为字节

In bytes

输入的数据大小，单位为字节

First forwarded

记录转发第一个报文时的系统时间，时间精确到毫秒

Last forwarded

记录转发最后一个报文时的系统时间，时间精确到毫秒

Protocol

协议

Direction

方向

L4 source port

TCP/UDP的源端口号

L4 destination port

TCP/UDP的目的端口号

Sampling algorithm

采样算法

PAD

空白占位符

Sampling interval

采样率

**NetStream \-- NetStream配置命令 \-- enable**

------------------------------------------------------------------------

**[enable**]命令用来开启当前聚合视图对应的聚合功能。

**[undo enable**]命令用来关闭当前聚合视图对应的聚合功能。

【命令】

**[enable**]

**[undo******enable**]

【缺省情况】

未开启任何NetStream聚合功能。

【视图】

NetStream聚合视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启NetStream的自治系统聚合功能。

\<Sysname\> system-view

Sysname ip netstream aggregation as

Sysname-ns-aggregation-as enable

【相关命令】

·**ip netstream aggregation**

**NetStream \-- NetStream配置命令 \-- ip netstream**

------------------------------------------------------------------------

![说明](NetStream命令.files/image001.png)

本命令的视图支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ip netstream**]命令用来在全局或当前接口开启NetStream功能。

**[undo ip netstream**]命令用来在全局或当前接口关闭NetStream功能。

【命令】

系统视图：

**[ip netstream**]

**[undo ip netstream**]

接口视图：

**[ip netstream**[ { **inbound** \| **outbound** }]]

**[undo ip netstream**[ { **inbound** \| **outbound** }]]

【视图】

系统视图/接口视图

!(NetStream命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省情况】

全局和接口NetStream功能处于关闭状态。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：对入方向的流量进行NetStream统计。

**[outbound**]：对出方向的流量进行NetStream统计。

【使用指导】

全局开启NetStream功能后，将开启所有接口入方向及出方向的NetStream功能。

【举例】

\# 全局开启NetStream功能。

\<Sysname\> system-view

Sysname ip netstream

\# 在GigabitEthernet1/0/1接口的入方向上开启NetStream功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip netstream inbound

**NetStream \-- NetStream配置命令 \-- ip netstream { inbound \| outbound } filter**

------------------------------------------------------------------------

![说明](NetStream命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ip netstream filter**]命令用来配置NetStream过滤功能，根据指定ACL规则对报文进行过滤。

**[undo** **ip netstream filter**]命令用来取消已有配置。

【命令】

**[ip netstream **[{ **inbound** \| **outbound** } **filter acl** *acl-number*]]

**[undo ip netstream**[ { **inbound** \| **outbound** } **filter**]]

【缺省情况】

未配置NetStream过滤功能，此时统计所有IPv4报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：入方向过滤，即对从当前接口收到的报文进行过滤统计。

**[outbound**]：出方向过滤，即对从当前接口发出的报文进行过滤统计。

**[acl*** acl-number*]：ACL规则号，基本ACL取值范围为2000～2999，高级ACL取值范围为3000～3999。

【举例】

\# 在接口GigabitEthernet1/0/1上配置根据ACL 2003规则进行出方向过滤。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip netstream outbound

Sysname-GigabitEthernet1/0/1 ip netstream outbound filter acl 2003

**NetStream \-- NetStream配置命令 \-- ip netstream { inbound \| outbound } mirror-to**

------------------------------------------------------------------------

!(NetStream命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**ip**[ **netstream** { **inbound** \| **outbound** } **mirror**-**to**]命令用来将端口流量镜像到业务板。（分布式设备－独立运行模式/分布式设备－IRF模式）

**ip**[ **netstream** { **inbound** \| **outbound** } **mirror**-**to**]命令用来将端口流量镜像到业务设备。（集中式IRF设备）

**undo ip netstream **[{ **inbound** \| **outbound** } **mirror-to**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**ip netstream **[{ inbound \| outbound } **mirror-to service slot** *slot-number* [ **backup slot** *slot-number* ]]

**undo ip netstream **[{ inbound \| outbound } **mirror-to**]

分布式设备－IRF模式：

**ip netstream**[ { **inbound** \| **outbound** } **mirror-to service chassis** *chassis-number* **slot** *slot-number* [ **backup chassis** *chassis-number* **slot** *slot-number* ]]

**undo ip netstream**[ { **inbound** \| **outbound** } **mirror-to**]

【缺省情况】

不对端口流量进行镜像。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**inbound**：对接口的入方向流量进行镜像。

**outbound**：对接口的出方向流量进行镜像。

**service slot** *slot-number*：指定主用业务板所在的槽位号。*slot-number*表示业务板所在的槽位号。（分布式设备－独立运行模式）

**service slot** *slot-number*：指定主用业务设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**service chassis** *chassis-number* **slot** *slot-number*：指定成员设备上的指定业务板作为主用业务板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示业务板所在的槽位号。（分布式设备－IRF模式）

**backup slot** *slot-number*：指定备用业务板所在的槽位号。若未指定该参数，表示未配置备用业务板。（分布式设备－独立运行模式）

**backup slot** *slot-number*：指定备用业务设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。若未指定该参数，表示未配置备用业务设备。（集中式IRF设备）

**backup chassis** *chassis-number* **slot** *slot-number*：指定成员设备上的指定业务板作为备用业务板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示业务板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

只有当主用业务板出现故障时，流量才可以被镜像到备用业务板。主用业务板恢复，备用业务板恢复为备份身份，流量镜像到主用业务板。（分布式设备－独立运行模式/分布式设备－IRF模式）

只有当主用业务设备出现故障时，流量才可以被镜像到备用业务设备。主用业务设备恢复，备用业务设备恢复为备份身份，流量镜像到主用业务设备。（集中式IRF设备）

【举例】

\# 在接口GigabitEthernet 1/0/1上配置入方向流量镜像，将流量镜像到3号槽的业务板。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip netstream inbound mirror-to service slot 3

**NetStream \-- NetStream配置命令 \-- ip netstream { inbound \| outbound } sampler**

------------------------------------------------------------------------

**[ip netstream sampler**]命令用来启用NetStream采样功能。

**[undo ip netstream sampler**]命令用来禁用NetStream采样功能。

【命令】

**[ip netstream**[ { **inbound** \| **outbound** } **sampler** *sampler-name*]]

**[undo ip netstream**[ { **inbound** \| **outbound** } **sampler**]]

【缺省情况】

未启用NetStream采样功能。

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

\# 在接口GigabitEthernet1/0/1上启用NetStream采样功能，使用名为abc的采样器对入方向的报文进行采样，Netstream根据采样结果进行报文统计。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip netstream inbound

Sysname-GigabitEthernet1/0/1 ip netstream inbound sampler abc

**NetStream \-- NetStream配置命令 \-- ip netstream aggregation**

------------------------------------------------------------------------

![说明](NetStream命令.files/image001.png)

本命令中各参数的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ip netstream aggregation**]命令用来设置NetStream流聚合方式，并进入相应的NetStream聚合视图。

**[undo ip netstream aggregation**]命令用来关闭NetStream流聚合方式，并删除流聚合方式相应的配置。

【命令】

**[ip netstream aggregation**[ { **as** \| **destination-prefix** \| **prefix** \| **prefix-port** \| **protocol-port** \| **source-prefix** \| **tos-as** \| **tos-bgp-nexthop** \| **tos-destination-prefix** \| **tos-prefix** \| **tos-protocol-port** \| **tos-source-prefix** }]]

**[undo ip netstream aggregation**[ { **as** \| **destination-prefix** \| **prefix** \| **prefix-port** \| **protocol-port** \| **source-prefix** \| **tos-as** \| **tos-bgp-nexthop** \| **tos-destination-prefix** \| **tos-prefix** \| **tos-protocol-port** \| **tos-source-prefix** }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[as**]：自治系统聚合，根据NetStream流的源自治系统号、目的自治系统号、输入接口索引和输出接口索引4个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[destination-prefix**]：目的前缀聚合，根据NetStream流的目的自治系统号、目的掩码长度、目的前缀和输出接口索引4个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[prefix**]：源和目的前缀聚合，根据NetStream流的源自治系统号、目的自治系统号、源掩码长度、目的掩码长度，源前缀、目的前缀、输入接口索引和输出接口索引8个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[prefix-port**]：前缀端口聚合，根据NetStream流的源前缀、目的前缀、源掩码长度、目的掩码长度、ToS、协议号、源端口、目的端口、输入接口索引、输出接口索引10个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[protocol-port**]：协议－端口聚合，根据NetStream流的协议号、源端口和目的端口3个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[source-prefix**]：源前缀聚合，根据NetStream流的源自治系统号、源掩码长度、源前缀和输入接口索引4个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[tos-as**]：服务类型－自治系统聚合，根据NetStream流的ToS、源自治系统号、目的自治系统号、输入接口索引和输出接口索引5个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[tos-bgp-nexthop**]：服务类型-BGP下一跳聚合，根据NetStream流的服务类型、BGP下一跳IP地址、输出接口索引3个关键项对流分类。服务类型-BGP下一跳聚合只在V9模板下生效，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[tos-destination-prefix**]：服务类型－目的前缀聚合，根据NetStream流的ToS、目的自治系统号、目的掩码长度、目的前缀和输出接口索引5个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[tos-prefix**]：服务类型－前缀聚合，根据NetStream流的ToS、源自治系统号、源前缀、源掩码长度、目的自治系统号、目的掩码长度、目的前缀、输入接口索引和输出接口索引9个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[tos-protocol-port**]：服务类型－协议－端口聚合，根据NetStream流的ToS、协议号、源端口、目的端口、输入接口索引和输出接口索引6个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[tos-source-prefix**]：服务类型－源前缀聚合，根据NetStream流的ToS、源自治系统号、源前缀、源掩码长度和输入接口索引5个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。

【使用指导】

·在聚合视图下，可以启用或关闭聚合功能，以及设置NetStream统计输出报文源接口、目的IP地址以及目的端口号。

·如果一条流同时满足多个聚合方式，则该流会被统计到多个聚合流中。

【举例】

\# 设置NetStream流聚合方式为自治系统聚合，并进入NetStream自治系统聚合视图。

\<Sysname\> system-view

Sysname ip netstream aggregation as

【相关命令】

·**enable**

**NetStream \-- NetStream配置命令 \-- ip netstream aggregation advanced**

------------------------------------------------------------------------

![说明](NetStream命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ip netstream aggregation advanced**]命令用来使能硬件流聚合功能。

**[undo ip netstream aggregation advanced**]命令用来恢复缺省情况。

【命令】

**[ip netstream aggregation advanced**]

**[undo ip netstream aggregation advanced**]

【缺省情况】

NetStream硬件流聚合功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·使能硬件流聚合功能时，系统根据NetStream统计功能是否配置了统计信息输出的目的地址以及配置的聚合类型来决定是否进行硬件聚合。如果在系统视图下配置了统计信息输出的目的地址或硬件聚合不支持配置的聚合类型，则硬件聚合配置不生效。

·使能硬件流聚合功能以后，硬件聚合流表项添加到普通流表项记录中，并进行表项的输出。

【举例】

\# 使能硬件流聚合功能。

\<Sysname\> system-view

Sysname ip netstream aggregation advanced

【相关命令】

·**ip netstream aggregation**

·**ip netstream export host**

**NetStream \-- NetStream配置命令 \-- ip netstream export host**

------------------------------------------------------------------------

**[ip netstream export host**]命令用来配置NetStream统计输出报文的目的地址和目的UDP端口号。**undo ip netstream export host**命令用来删除已有配置。

【命令】

**[ip netstream export host** *ip-address udp-port* [ **vpn-instance** *vpn-instance-name* ]]

**[undo ip netstream export host ** *ip-address*  **vpn-instance** *vpn-instance-name*  ]

【缺省情况】

系统视图和聚合视图下均没有配置目的地址和目的UDP端口号。

【视图】

系统视图/NetStream聚合视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：NetStream统计输出报文的目的IP地址。

*[udp-port*]：NetStream统计输出报文的目的UDP端口号，取值范围为0～65535。

*[vpn-instance vpn-instance-name*]：指定NetStream统计输出报文的目的地址所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示NetStream统计输出报文的目的地址位于公网中。

【使用指导】

·若某类聚合视图没有使能，则无法通过**display ip netstream export**命令查看它的相关信息（包括目的地址的目的UDP端口号）。

·执行undo ip netstream export host命令时未指定地址，表示取消指定本视图下配置的所有地址。

·不同聚合视图下可以配置相同的目的地址和目的UDP端口号。

·若聚合视图下没有配置目的地址和目的UDP端口号，则使用系统视图下的配置；若聚合视图下配置了目的地址和目的UDP端口号，则使用聚合视图下的配置。

·一个视图下最多可配置4组目的地址，包括不同VPN实例。在同一视图下，若先后配置了IP地址相同、UDP端口号不同的目的地址，则后配置的目的地址生效。在用户配置了不同的VPN实例名称时，允许配置相同的IP地址和UDP端口号。

·普通流统计输出报文会发给系统视图下配置的所有目的地址。聚合流统计输出报文会发给聚合类型对应的聚合视图下配置的所有目的地址。为了减少对网络带宽的占用，可以只在聚合视图下配置**ip netstream export host**命令，此时设备只会输出聚合流信息。

·在执行**undo ip netstream export host**命令时，如果未指定IP地址，则取消本视图下配置的所有IP地址。

【举例】

\# 配置全局NetStream统计输出报文的目的IP地址为172.16.105.48，UDP端口号为5000。

\<Sysname\> system-view

Sysname ip netstream export host 172.16.105.48 5000

\# 配置NetStream自治系统聚合统计输出报文的目的IP地址为172.16.105.50，UDP端口号为6000。.

\<Sysname\> system-view

Sysname ip netstream aggregation as

Sysname-ns-aggregation-as ip netstream export host 172.16.105.50 6000

【相关命令】

·**ip netstream aggregation**

·**ip netstream export source**

**NetStream \-- NetStream配置命令 \-- ip netstream export rate**

------------------------------------------------------------------------

**[ip netstream export rate**]命令用来配置输出速率限制，即限制每秒钟输出的最多报文数。

**[undo ip netstream export rate**]命令用来恢复缺省情况。

【命令】

**[ip netstream export rate ***rate*]

**[undo ip netstream export rate**]

【缺省情况】

NetStream统计输出报文的输出速率不受限制。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：NetStream统计输出报文的输出速率限制，取值范围为1～1000，单位为每秒允许输出的最多报文个数。

【举例】

\# 设置每秒最多允许10个报文被输出。

\<Sysname\> system-view

Sysname ip netstream export rate 10

**NetStream \-- NetStream配置命令 \-- ip netstream export source**

------------------------------------------------------------------------

**[ip netstream export source**]命令用来配置NetStream统计输出报文的源接口。

**[undo ip netstream export source**]命令用来取消配置的输出报文的源接口。

【命令】

**[ip netstream export source interface** *interface-type interface-number*]

**[undo ip netstream export source**]

【缺省情况】

采用统计输出报文的出接口作为源接口。

【视图】

系统视图/NetStream聚合视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：NetStream统计输出报文的源接口，由接口类型和接口编号组成。

【使用指导】

·通过本命令配置源接口后，会将NetStream统计输出报文的源IP地址设置为该接口的IP地址。

·不同聚合视图下可以配置不同的源接口。

·聚合视图下若没有配置源接口，则使用系统视图下的配置。

【举例】

\# 将NetStream统计输出报文源接口设置为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname ip netstream export source interface gigabitethernet 1/0/1

\# 将NetStream自治系统聚合统计输出报文源接口设置为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname ip netstream aggregation as

Sysname-ns-aggregation-as ip netstream export source interface gigabitethernet 1/0/2

【相关命令】

·**ip netstream aggregation**

**NetStream \-- NetStream配置命令 \-- ip netstream export v9-template refresh-rate packet**

------------------------------------------------------------------------

**[ip netstream export v9-template refresh-rate packet**]命令用来配置NetStream统计输出报文版本9模板的包刷新率。

**[undo ip netstream export v9-template refresh-rate packet**]命令用来恢复缺省情况。

【命令】

**[ip netstream export v9-template refresh-rate packet ***packets*]

**[undo ip netstream export v9-template refresh-rate packet**]

【缺省情况】

每隔20个包设备发送一次版本9模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[packets*]：NetStream统计输出报文版本9模板的包刷新率，取值范围为1～600，单位为包数，即每隔多少个包更新一次模板，并通知NetStream服务器最新的V9模板格式。

【使用指导】

V9版本是基于模板方式的、支持自定义格式，由于NetStream服务器不会永久保存模板，所以设备需要定期通知NetStream服务器最新的V9模板格式。用户可以根据实际情况，配置版本9模板的包刷新率，及时更新模板。

可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给NetStream服务器。

【举例】

\# 将NetStream统计输出报文版本9模板的包刷新率设为100。

\<Sysname\> system-view

Sysname ip netstream export v9-template refresh-rate packet 100

【相关命令】

·**ip netstream export v9-template refresh-rate time**

**NetStream \-- NetStream配置命令 \-- ip netstream export v9-template refresh-rate time**

------------------------------------------------------------------------

**[ip netstream export v9-template refresh-rate time**]命令用来配置NetStream统计输出报文版本9模板的时间刷新率。

**[undo ip netstream export v9-template refresh-rate time**]命令用来恢复缺省情况。

【命令】

**[ip netstream export v9-template refresh-rate time ***minutes*]

**[undo ip netstream export v9-template refresh-rate time**]

【缺省情况】

每隔30分钟设备发送一次版本9模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：NetStream统计输出报文版本9模板的时间刷新率，取值范围为1～3600，单位为分钟，即每隔多少分钟更新一次模板，并通知NetStream服务器最新的V9模板格式。

【使用指导】

V9版本是基于模板方式的、支持自定义格式，由于NetStream服务器不会永久保存模板，所以设备需要定期通知NetStream服务器最新的V9模板格式。用户可以根据实际情况，配置版本9模板的时间刷新率，及时更新模板。

可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给NetStream服务器。

【举例】

\# 将NetStream统计输出报文版本9模板的时间刷新率设为60分钟。

\<Sysname\> system-view

Sysname ip netstream export v9-template refresh-rate time 60

【相关命令】

·**ip netstream export v9-template refresh-rate packet**

**NetStream \-- NetStream配置命令 \-- ip netstream export version**

------------------------------------------------------------------------

**[ip netstream export version 5**]命令用来配置NetStream版本5的自治系统选项。

**[ip netstream export version 9**]命令用来配置NetStream版本9的自治系统选项和BGP下一跳选项。

**[undo ip netstream export version**]命令用来恢复缺省情况。

【命令】

**[ip netstream export version**[ *5* [ **origin-as** \| **peer-as** ]]]

**[ip netstream export version**[ 9 [ **origin-as** \| **peer-as** ]  **bgp-nexthop** ]]

**[undo ip netstream export version**]

【缺省情况】

普通流信息通过版本9的NetStream统计输出报文发送，MPLS流信息不输出。自治系统选项使用邻接自治系统号（**peer-as**），流信息中不记录BGP下一跳地址。

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

·NetStream流信息中会记录流的源IP地址及其对应的自治系统号；目的IP地址及其对应的自治系统号。设备会根据用户实际配置的自治系统参数来确定记录的自治系统号。

·只有在版本号为9时，才可以配置BGP下一跳。

·设备上同时只允许一种版本存在，V5和V9不能同时配置。

·当设备上配置了聚合时，如果配置输出报文版本为V5，则流统计信息采用V8版本输出；如果配置输出版本为V9，则流统计信息采用V9版本输出。

·本命令重复配置时，新配置会覆盖旧配置。

【举例】

\# 将NetStream统计输出报文版本号设为5，并设置流信息中记录的自治系统号为起始自治系统号。

\<Sysname\> system-view

Sysname ip netstream export version 5 origin-as

**NetStream \-- NetStream配置命令 \-- ip netstream max-entry**

------------------------------------------------------------------------

**[ip netstream max-entry**]命令用来配置NetStream流缓存区中流表项的最大数目及达到最大数目时的处理方式。

**[undo ip netstream max-entry**]命令用来恢复缺省情况。

【命令】

**[ip netstream max-entry**[ { *max-entries* \| *aging* \| *disable-caching* }]]

**[undo ip netstream max-entry**]

【缺省情况】

本命令的缺省情况与设备的型号相关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-entries*]：NetStream流缓存区中流表项的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[aging**]：达到流表项的最大数目时，强制老化部分流表项。

**[disable-caching**]：达到流表项的最大数目时，禁止新建流表项。

【使用指导】

·*max-entries*参数值在各单板上单独生效，而不是各单板的总和。（分布式设备－独立运行模式）

·*max-entries*参数值在各成员设备的各单板上单独生效，而不是各单板的总和。（分布式设备－IRF模式）

·*max-entries*参数值在各成员设备上单独生效，而不是各成员设备的总和。（集中式IRF设备）

·**ip netstream max-entry** *max-entries*命令可重复配置，以最后一次配置为准。

·**ip netstream max-entry******[{ **aging** \| **disable-caching** }]命令可以重复配置，以最后一次配置为准。

【举例】

\# 设置NetStream流缓存区中流表项的最大数目为5000。

\<Sysname\> system-view

Sysname ip netstream max-entry 5000

\# 设置NetStream在达到流表项的最大数目时，禁止新建流表项。

\<Sysname\> system-view

Sysname ip netstream max-entry disable-caching

\# 设置NetStream在达到流表项的最大数目时，强制老化部分流表项。

\<Sysname\> system-view

Sysname ip netstream max-entry aging

**NetStream \-- NetStream配置命令 \-- ip netstream mpls**

------------------------------------------------------------------------

**[ip netstream mpls**]命令用来开启MPLS报文统计功能，即统计和输出MPLS格式的报文。

**[undo ip netstream mpls**]用来恢复缺省情况。

【命令】

**[ip netstream mpls ** **label-positions** *label-position1*  *label-position2* [ *label-position3*  ] ]  **no-ip-fields**

**[undo ip netstream mpls**]

【缺省情况】

未开启MPLS报文统计功能。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[label-positions**]：统计的MPLS报文的标签位置。

*[label-position1*]：指定统计的MPLS报文的第一个标签位置，取值范围为1～6。

*[label-position2*]：指定统计的MPLS报文的第二个标签位置，取值范围为1～6。

*[label-position3*]：指定统计的MPLS报文的第三个标签位置，取值范围为1～6。

**[no-ip-fields**]：不统计IP选项。

【使用指导】

·该命令不仅使能IPv4 NetStream对MPLS报文的统计功能，同时也使能了IPv6 NetStream对MPLS报文的统计功能。

·若未指定任何参数，表示基于MPLS报文的首标签并且带有IP选项进行统计。

·当需要统计MPLS报文的多个标签时，指定的标签位置不允许重复，最终统计的多个标签的位置依据从小到大的顺序取指定值。

【举例】

\# 开启MPLS报文统计功能，基于MPLS报文的首标签并且不带IP选项进行统计。

\<Sysname\> system-view

Sysname ip netstream mpls no-ip-fields

**NetStream \-- NetStream配置命令 \-- ip netstream timeout active**

------------------------------------------------------------------------

**[ip netstream timeout active**]命令用来配置流的活跃老化时间。

**[undo ip netstream timeout active**]命令用来恢复缺省情况。

【命令】

**[ip netstream timeout active** *minutes*]

**[undo ip netstream timeout active**]

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

Sysname ip netstream timeout active 60

【相关命令】

·**ip netstream timeout inactive**

**NetStream \-- NetStream配置命令 \-- ip netstream timeout inactive**

------------------------------------------------------------------------

**[ip netstream timeout inactive**]命令用来配置流的不活跃老化时间。

**[undo ip netstream timeout inactive**]命令用来恢复缺省情况。

【命令】

**[ip netstream timeout inactive** *seconds*]

**[undo ip netstream timeout inactive**]

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

Sysname ip netstream timeout inactive 60

【相关命令】

·**ip netstream timeout active**

**NetStream \-- NetStream配置命令 \-- reset ip netstream statistics**

------------------------------------------------------------------------

**[reset ip netstream statistics**]命令用来将流缓存区中所有流强制老化，输出报文信息，并清空NetStream缓冲区的状态信息。

【命令】

**[reset ip netstream statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在执行清空缓冲区中老化流的动作时，命令行会给出提示，告知用户这个动作可能要持续几分钟，在这段时间内不能统计。

【举例】

\# 将流缓存区中所有流老化，输出报文信息，并清空NetStream缓冲区的状态信息。

\<Sysname\> reset ip netstream statistics

This process may take a few minutes.

Netstream statistic function is disabled during this process.

