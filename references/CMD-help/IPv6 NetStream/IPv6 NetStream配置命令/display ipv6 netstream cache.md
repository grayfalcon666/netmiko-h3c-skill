::: {#693902187 .myid}
[]{#_Toc404797315}[]{#struct_0_x7706_12603_405786566}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- display ipv6 netstream cache**

------------------------------------------------------------------------

[**[display ipv6 netstream cache]{lang="EN-US"}**]{#struct_0_x7706_12603_x2132988557}[命令用来查看]{style="font-family:
宋体"}[IPv6 NetStream]{lang="EN-US"}[流缓存区的配置和状态信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x720330920}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7706_12603_x667156204}

[**[display ipv6 netstream cache ]{lang="EN-US"}**[\[ **verbose** \]]{lang="EN-US"}]{#struct_0_x7706_12603_x1415324574}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7706_12603_1053153667}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 netstream cache ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x7706_12603_2021050147}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7706_12603_1902323555}[模式：]{style="font-family:宋体"}

[**[display ipv6 netstream cache ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x7706_12603_x1142771857}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_835167490}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1274254356}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_819218302}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x541387642}

[[network-operator]{lang="EN-US"}]{#struct_0_x7706_12603_x1986934271}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x2133054093}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x7706_12603_440490521}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_78664868}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x7706_12603_983236327}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_45852640}[：显示指定成员设备上的信息。]{style="font-family:宋体"} *[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_x1207112404}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"} *[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_941898112}[：显示指定成员设备上指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_x107041137}[：显示指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x7706_12603_1463791481}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x7706_12603_x1446787074}[：显示]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流缓冲区的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x577664859}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_576116017}[查看]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流缓冲区信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 netstream cache verbose]{lang="EN-US"}]{#struct_0_x7706_12603_x2132660877}

[IPv6 NetStream cache information:]{lang="EN-US"}

[  Active flow timeout             : 60 min]{lang="EN-US"}

[  Inactive flow timeout           : 10 sec]{lang="EN-US"}

[  Max number of entries           : 1000]{lang="EN-US"}

[  IPv6 active flow entries        : 1]{lang="EN-US"}

[  MPLS active flow entries        : 2]{lang="EN-US"}

[  IPL2 active flow entries        : 1]{lang="EN-US"}

[  IPv6 flow entries counted       : 10]{lang="EN-US"}

[  MPLS flow entries counted       : 20]{lang="EN-US"}

[  IPL2 flow entries counted       : 20]{lang="EN-US"}

[  Last statistics resetting time  : 01/01/2000 at 00:01:02]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 packet size distribution (1103746 packets in total):]{lang="EN-US"}

[1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480]{lang="EN-US"}

[.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608]{lang="EN-US"}

[.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)]{lang="EN-US"}

[                  Flows /sec       /sec   /flow   /flow       /flow]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[TCP-Telnet      2656855     372        4       86        49        27]{lang="EN-US"}

[TCP-FTP         5900082      86        9        9        11        33]{lang="EN-US"}

[TCP-FTPD        3200453    1006        5      193        45        33]{lang="EN-US"}

[TCP-WWW       546778274   11170      887       12         8        32]{lang="EN-US"}

[TCP-other      49148540    3752       79       47        30        32]{lang="EN-US"}

[UDP-DNS       117240379     570      190        3         7        34]{lang="EN-US"}

[UDP-other      45502422    2272       73       30         8        37]{lang="EN-US"}

[ICMP           14837957     125       24        5        12        34]{lang="EN-US"}

[IP-other          77406       5        0       47        52        27]{lang="EN-US"}

[ ]{lang="EN-US"}

[Type DstIP(Port)         SrcIP(Port)      Pro TC  FlowLbl If(Direct)   Pkts]{lang="EN-US"}

[     DstMAC(VLAN)        SrcMAC(VLAN)]{lang="EN-US"}

[     TopLblType(IP/MASK) Lbl-Exp-S-List]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="DA"}

[IP   2001::1(1024)      2002::1(21)        6   0   0x6000  GE1/0/1(I)  42996]{lang="DA"}

[MPLS LDP(3.3.3.3/24)    1:18-6-0                           GE1/0/2(O)  291]{lang="DA"}

[                        ]{lang="DA"}[2:24-6-0]{lang="PT-BR"}

[                        3:30-6-1]{lang="PT-BR"}

[IP&  2003::1(2048)      2008::1(0)         1   0   0x0     GE1/0/2(O)  10]{lang="PT-BR"}

[IP&  2010::1(1024)      2020::1(67)        17  0   0x12345 GE1/0/3(I)  1848]{lang="DA"}

[MPLS LDP(4.4.4.4/24)    1:55-6-0]{lang="DA"}

[                        2:16-6-1]{lang="DA"}

[                        2:0-0-0]{lang="DA"}

[[\# ]{lang="DA"}]{#struct_0_x7706_12603_1751574199}[查看]{style="font-family:宋体"}[IPv6 NetStream]{lang="DA"}[流缓冲区信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 netstream cache slot 1 verbose]{lang="DA"}]{#struct_0_x7706_12603_x2132791949}

[IPv6 NetStream cache information:]{lang="DA"}

[  ]{lang="DA"}[Active flow timeout             : 60 min]{lang="EN-US"}

[  Inactive flow timeout           : 10 sec]{lang="EN-US"}

[  Max number of entries           : 1000]{lang="EN-US"}

[  IPv6 active flow entries        : 1]{lang="EN-US"}

[  MPLS active flow entries        : 2]{lang="EN-US"}

[  IPL2 active flow entries        : 1]{lang="EN-US"}

[  IPv6 flow entries counted       : 10]{lang="EN-US"}

[  MPLS flow entries counted       : 20]{lang="EN-US"}

[  IPL2 flow entries counted       : 20]{lang="EN-US"}

[  Last statistics resetting time  : 01/01/2000 at 00:01:02]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 packet size distribution (1103746 packets in total):]{lang="EN-US"}

[1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480]{lang="EN-US"}

[.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608]{lang="EN-US"}

[.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)]{lang="EN-US"}

[                  Flows /sec       /sec   /flow   /flow       /flow]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[TCP-Telnet      2656855     372        4       86        49         27]{lang="EN-US"}

[TCP-FTP         5900082      86        9        9        11         33]{lang="EN-US"}

[TCP-FTPD        3200453    1006        5      193        45         33]{lang="EN-US"}

[TCP-WWW       546778274   11170      887       12         8         32]{lang="EN-US"}

[TCP-other      49148540    3752       79       47        30         32]{lang="EN-US"}

[UDP-DNS       117240379     570      190        3         7         34]{lang="EN-US"}

[UDP-other      45502422    2272       73       30         8         37]{lang="EN-US"}

[ICMP           14837957     125       24        5        12         34]{lang="EN-US"}

[IP-other          77406       5        0       47        52         27]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Type DstIP(Port)        SrcIP(Port)      Pro TC  FlowLbl If(Direct)   Pkts]{lang="EN-US"}

[      DstMAC(VLAN)       SrcMAC(VLAN)]{lang="EN-US"}

[      TopLblType(IP/MASK)Lbl-Exp-S-List]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="DA"}

[IP   2001::1(1024)      2002::1(21)        6   0   0x0     ET1/1(I)    42996]{lang="DA"}

[     TcpFlag:    0x1b]{lang="DA"}

[     ]{lang="DA"}[DstMask:      24   SrcMask:      24]{lang="EN-US"}

[     DstAS:         0   SrcAS:         0]{lang="EN-US"}

[     NextHop:           2001::2]{lang="EN-US"}

[     BGPNextHop:        0:0:0:0:0:0:0:0]{lang="EN-US"}

[     InVRF:        10]{lang="EN-US"}

[     ]{lang="PT-BR"}[SamplerMode:   0   SamplerInt:    0]{lang="EN-US"}

[     Active:      120   Bytes/Pkt:   152]{lang="EN-US"}

[MPLS LDP(3.3.3.3/24)    1:18-6-0                           GE1/0/2(O)  291]{lang="PT-BR"}

[                        2:24-6-0]{lang="PT-BR"}

[                        3:30-6-1]{lang="PT-BR"}

[     SamplerMode]{lang="PT-BR"}[:   0   SamplerInt:    0]{lang="EN-US"}

[     Active:      660   Bytes/Pkt:   100]{lang="PT-BR"}

[IP&  2003::1(2048)      2008::1(0)         1   0   0x0     GE1/0/2(O)  10]{lang="PT-BR"}

[IP&  2010::1(1024)      2020::1(67)        17  255 0x12345 GE1/0/3(I)  1848]{lang="DA"}

[MPLS LDP(4.4.4.4/24)    1:55-6-0]{lang="DA"}

[                        2:16-6-1]{lang="DA"}

[                        3:0-0-0]{lang="DA"}

[     TcpFlag:       0]{lang="DA"}

[     DstMask:      24   SrcMask:      24]{lang="DA"}

[     DstAS:         0   SrcAS:         0]{lang="DA"}

[     ]{lang="DA"}[NextHop:           2020::2]{lang="EN-US"}

[     BGPNextHop:        0:0:0:0:0:0:0:0]{lang="EN-US"}

[     InVRF:         0]{lang="EN-US"}

[     ]{lang="PT-BR"}[SamplerMode:   0   SamplerInt:    0]{lang="EN-US"}

[     Active:      382   Bytes/Pkt:  1426]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ipv6 netstream cache]{lang="EN-US"}]{#struct_0_x7706_12603_x979244115}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1287307168}[[字段]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1932143544}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7706_12603_x2133381773}

[[IPv6 NetStream cache information]{lang="EN-US"}]{#struct_0_x7706_12603_689271313}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x1766728623}[流缓存区信息]{style="font-family:宋体"}

[[Active flow  timeout]{lang="EN-US"}]{#struct_0_x7706_12603_x2124678572}

[[活跃流的老化时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1668813642}

[[Inactive flow timeout ]{lang="EN-US"}]{#struct_0_x7706_12603_65755075}

[[不活跃流的老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x7706_12603_x824473}

[[Max number of entries]{lang="EN-US"}]{#struct_0_x7706_12603_x1669234580}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x2133447309}[流缓存区中允许的最大流数]{style="font-family:宋体"}

[[IPv6 active flow entries]{lang="EN-US"}]{#struct_0_x7706_12603_1781831295}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_960555789}[流缓存区中活跃的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[流数]{style="font-family:宋体"}

[[MPLS active flow entries]{lang="EN-US"}]{#struct_0_x7706_12603_x1579049162}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_282996857}[流缓存区中活跃的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流数]{style="font-family:宋体"}

[[IPL2 active flow entries]{lang="EN-US"}]{#struct_0_x7706_12603_x903820569}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x777063964}[流缓存区中活跃的二层和三层流数]{style="font-family:宋体"}

[[IPv6 flow entries counted]{lang="EN-US"}]{#struct_0_x7706_12603_596025875}

[[已经被统计的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7706_12603_x279011795}[流数]{style="font-family:宋体"}

[[MPLS flow entries counted]{lang="EN-US"}]{#struct_0_x7706_12603_797609207}

[[已经被统计的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x7706_12603_x2113338184}[流数]{style="font-family:宋体"}

[[IPL2 flow entries counted]{lang="EN-US"}]{#struct_0_x7706_12603_x2048554999}

[[已经被统计的二层和三层流数]{style="font-family:宋体"}]{#struct_0_x7706_12603_x144261752}

[[Last statistics resetting time]{lang="EN-US"}]{#struct_0_x7706_12603_366380354}

[[上次清除统计的时间]{style="font-family:宋体"}]{#struct_0_x7706_12603_595960339}

[[该字段只在执行了]{style="font-family:宋体"}**[reset ipv6 netstream statistics]{lang="EN-US"}**]{#struct_0_x7706_12603_1115076345}[命令后才会显示为时间，否则显示为]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[IPv6 packet size distribution (1103746packets in total): ]{lang="EN-US"}]{#struct_0_x7706_12603_1063775839}

[[IPv6]{lang="EN-US"}]{#struct_0_x7706_12603_x1124885899}[报文按大小分布情况，括号中为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文总数。分布值按各项占报文总数的比率显示，只显示]{style="font-family:宋体"}[3]{lang="EN-US"}[位小数，如"]{style="font-family:宋体"}[.027]{lang="EN-US"}["表示占]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文总数的]{style="font-family:宋体"}[0.027]{lang="EN-US"}

[[1-32   64   96  128  160  192  224  256  288  ]{lang="EN-US"}]{#struct_0_x7706_12603_1575204561}

[[320  352  384  416  448  480 512  544  576 ]{lang="EN-US"}]{#struct_0_x7706_12603_595894803}

[[1024 1536 2048 2560 3072 3584 4096 4608 \>4608]{lang="EN-US"}]{#struct_0_x7706_12603_x2063288355}

[[IPv6]{lang="EN-US"}]{#struct_0_x7706_12603_x789973801}[报文尺寸区间（报文长度不包括二层链路层的头）。长度不超过]{style="font-family:宋体"}[576]{lang="EN-US"}[字节时，以]{style="font-family:宋体"}[32]{lang="EN-US"}[字节为单位递增，例如："]{style="font-family:宋体"}[1-32]{lang="EN-US"}["是长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字节的报文数目，"]{style="font-family:宋体"}[64]{lang="EN-US"}["是长度为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[字节的报文数。长度超过]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节时，以]{style="font-family:宋体"}[512]{lang="EN-US"}[字节为单位递增，例如"]{style="font-family:宋体"}[1536]{lang="EN-US"}["是长度为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[1536]{lang="EN-US"}[字节的报文数。长度为]{style="font-family:宋体"}[577]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[间的报文记录存放在]{style="font-family:宋体"}[1024]{lang="EN-US"}[项中。]{style="font-family:宋体"}

[[Protocol     Total Flows     Packets/Sec ]{lang="EN-US"}]{#struct_0_x7706_12603_x1955606349}

[[Flow/Sec   Packets/flow]{lang="EN-US"}]{#struct_0_x7706_12603_1797226718}

[[Active(sec)/ flow   Idle(sec)/flow]{lang="EN-US"}]{#struct_0_x7706_12603_595829267}

[[按协议分类的报文统计信息：协议类型、总流数、每秒的报文数、每秒的流数、平均每条流的报文数、平均每条流的活跃时间、平均每条流的非活跃时间]{style="font-family:宋体"}]{#struct_0_x7706_12603_x410572014}

[[Type DstIP(Port)        SrcIP(Port)        Pro TC  FlowLbl    If(Direct)   Pkts]{lang="EN-US"}]{#struct_0_x7706_12603_x687216311}

[[当前流缓存区中活跃流的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7706_12603_1607740798}[层信息：]{style="font-family:宋体"} [流的类型、目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（目的端口号）、源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（源端口号）、协议号、流量分类、流标签、接口名（方向）、包数]{style="font-family:宋体"}

[[其中流的类型有四种：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7706_12603_1431118735}[流（]{style="font-family:宋体"}[IP]{lang="EN-US"}[）、二三层混合流（]{style="font-family:宋体"}[IPL2]{lang="EN-US"}[）、不带]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流（]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[）、带]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流（]{style="font-family:宋体"}[IP&MPLS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[需要注意的是，对于]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_x7706_12603_596288019}[报文只有]{style="font-family:宋体"}[Type]{lang="EN-US"}[和]{style="font-family:宋体"}[Code]{lang="EN-US"}[字段，因此用目的端口号的高]{style="font-family:宋体"}[8]{lang="EN-US"}[位为]{style="font-family:宋体"}[Type]{lang="EN-US"}[字段、低]{style="font-family:宋体"}[8]{lang="EN-US"}[位为]{style="font-family:宋体"}[Code]{lang="EN-US"}[字段，源端口号为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[DstMAC(VLAN)          SrcMAC(VLAN)]{lang="EN-US"}]{#struct_0_x7706_12603_1520124247}

[[当前流缓存区中活跃流的二层信息：目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x7706_12603_268788056}[地址、目的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、源]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[TopLblType(IP/MASK)      Lbl-Exp-S-List]{lang="EN-US"}]{#struct_0_x7706_12603_44132738}

[[当前流缓存区中活跃流的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x7706_12603_273323766}[信息：栈顶标签的类型（栈顶标签对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及掩码长度）、标签列表]{style="font-family:宋体"}

[[标签主要的三部分：]{style="font-family:宋体"}]{#struct_0_x7706_12603_596222483}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[20]{lang="EN-US"}]{#struct_0_x7706_12603_x35252877}[比特的]{style="font-family:宋体"}[Label]{lang="EN-US"}[字段表示标签值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x7706_12603_x1880778939}[比特的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[字段用来实现]{style="font-family:宋体"}[QoS]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x7706_12603_x1409117294}[比特]{style="font-family:宋体"}[S]{lang="EN-US"}[字段置]{style="font-family:宋体"}[1]{lang="EN-US"}[表示已达栈底]{style="font-family:宋体"}

[[TcpFlag:]{lang="EN-US"}]{#struct_0_x7706_12603_596156947}

[[DstMask:   SrcMask:]{lang="EN-US"}]{#struct_0_x7706_12603_1284051699}

[[DstAS:       SrcAS: ]{lang="EN-US"}]{#struct_0_x7706_12603_1207757828}

[[NextHop: ]{lang="EN-US"}]{#struct_0_x7706_12603_2015068508}

[[BGPNextHop: ]{lang="EN-US"}]{#struct_0_x7706_12603_596091411}

[[OutVRF:     InVRF:]{lang="EN-US"}]{#struct_0_x7706_12603_x736488402}

[[SamplerMode:                  SamplerInt:]{lang="EN-US"}]{#struct_0_x7706_12603_1779861354}

[[Active:       Bytes/Pkt:]{lang="EN-US"}]{#struct_0_x7706_12603_1049214824}

[[当前流缓存区中活跃流的其它信息：]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x7706_12603_595501587}[标记、目的掩码、源掩码、目的自治系统、源自治系统、路由下一跳、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳、出方向报文所属]{style="font-family:宋体"}[VPN ]{lang="EN-US"}[、入方向报文所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[、采样模式、采样间隔、流活跃时间、平均每个包的字节数]{style="font-family:宋体"}

[[NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x488780541}[采样模式，目前支持三种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x7706_12603_380060937}[：表示不采样，统计所有报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x7706_12603_699610402}[：表示固定采样]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x7706_12603_595436051}[：表示随机采样]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-962784512 .myid}
[]{#_Toc404797316}[]{#struct_0_x7706_12603_x177728463}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- display ipv6 netstream export**

------------------------------------------------------------------------

[**[display ipv6 netstream export]{lang="EN-US"}**]{#struct_0_x7706_12603_172711368}[命令用来查看]{style="font-family:
宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的各种信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1434021495}

[**[display ipv6 netstream export ]{lang="EN-US"}**]{#struct_0_x7706_12603_x1829083898}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x681016664}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1152242375}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1793562849}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1014656719}

[[network-operator]{lang="EN-US"}]{#struct_0_x7706_12603_871755288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_2060465450}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x7706_12603_596025874}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x279011794}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_797543671}[查看]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 netstream export]{lang="EN-US"}]{#struct_0_x7706_12603_x476129730}

[as aggregation export information:]{lang="EN-US"}

[  Flow source interface                            : GigabitEthernet1/0/1]{lang="EN-US"}

[  Flow destination VPN instance                    : VPN1]{lang="EN-US"}

[  Flow destination IP address (UDP)                : 10.10.0.10 (30000)]{lang="EN-US"}

[  Version 9 exported flows number                  : 16]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed) : 2 (0)]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 export information:]{lang="EN-US"}

[  Flow source interface                           : GigabitEthernet1/0/1]{lang="EN-US"}

[  Flow destination VPN instance                   : VPN1]{lang="EN-US"}

[  Flow destination IP address (UDP)               : 10.10.0.10 (30000)]{lang="EN-US"}

[  Version 9 exported flows number                 : 16]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed): 16 (0)]{lang="EN-US"}

[ ]{lang="EN-US"}

[MPLS export information:]{lang="EN-US"}

[  Flow source interface                            : GigabitEthernet1/0/1]{lang="EN-US"}

[  Flow destination VPN instance                    : VPN1]{lang="EN-US"}

[  Flow destination IP address (UDP)                : 10.10.0.10 (30000)]{lang="EN-US"}

[  Version 9 exported flows number                  : 20]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed) : 2 (0)]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 netstream export]{lang="EN-US"}]{#struct_0_x7706_12603_825616520}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1281803136}[[字段]{style="font-family:黑体"}]{#struct_0_x7706_12603_595960338}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7706_12603_1115076346}

[[IPv6 export information]{lang="EN-US"}]{#struct_0_x7706_12603_1063710303}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_1231508331}[统计输出信息]{style="font-family:宋体"}

[[Flow source interface]{lang="EN-US"}]{#struct_0_x7706_12603_x482690737}

[[输出信息的源接口]{style="font-family:宋体"}]{#struct_0_x7706_12603_x366459607}

[[Flow destination VPN instance]{lang="EN-US"}]{#struct_0_x7706_12603_x1714556665}

[[输出信息的目的地址所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x7706_12603_x458372352}

[[Flow destination IP address (UDP)]{lang="EN-US"}]{#struct_0_x7706_12603_595894802}

[[输出信息的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7706_12603_x2063288356}[地址（]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号）]{style="font-family:宋体"}

[[Version 9 exported flows number]{lang="EN-US"}]{#struct_0_x7706_12603_x386689274}

[[使用版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_x7706_12603_902567152}[格式发送的流信息数]{style="font-family:宋体"}

[[Version 9 exported UDP datagrams number (failed)]{lang="EN-US"}]{#struct_0_x7706_12603_1632749023}

[[使用版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_x7706_12603_x2048178956}[格式发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数（发送失败的报文数）]{style="font-family:宋体"}

[[MPLS export information]{lang="EN-US"}]{#struct_0_x7706_12603_x1426089615}

[[版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_x7706_12603_595829266}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流统计输出信息]{style="font-family:宋体"}

[[as aggregation export information]{lang="EN-US"}]{#struct_0_x7706_12603_x410572013}

[[启用自治系统聚合的版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_x7706_12603_x687543991}[统计输出信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-220011083 .myid}
[]{#_Toc404797317}[]{#struct_0_x7706_12603_x361705418}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- display ipv6 netstream template**

------------------------------------------------------------------------

[**[display ipv6 netstream template]{lang="EN-US"}**]{#struct_0_x7706_12603_x966629265}[命令用来查看]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[模板的配置和状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1839271605}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1167539598}

[**[display ipv6 netstream template]{lang="EN-US"}**]{#struct_0_x7706_12603_x868298864}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7706_12603_1700953028}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 netstream template]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7706_12603_596288018}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7706_12603_1520124248}[模式：]{style="font-family:宋体"}

[**[display ipv6 netstream template]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7706_12603_267805016}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1063901057}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x2123510842}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x138170672}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_509993483}

[[network-operator]{lang="EN-US"}]{#struct_0_x7706_12603_757864717}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x373595808}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x7706_12603_x1343922127}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x974445749}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x7706_12603_x1251516332}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_596222482}[：显示指定成员设备上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主用设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_x1207309011}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示主用设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_x35252876}[：显示指定成员设备上指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7706_12603_x1207374547}[：显示指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x7706_12603_x1880778940}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x199329249}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x1705505707}[查看]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[模板信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 netstream template]{lang="EN-US"}]{#struct_0_x7706_12603_595436050}

[ Flow template refresh frequency            : 20]{lang="EN-US"}

[ Flow template refresh interval             : 30 min]{lang="EN-US"}

[ Active flow templates                      : 4]{lang="EN-US"}

[ Created flow templates                     : 4]{lang="EN-US"}

[ ]{lang="EN-US"}

[AS outbound template:]{lang="EN-US"}

[ Template ID                : 3293]{lang="EN-US"}

[ Field count                : 14]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Flows                        4]{lang="EN-US"}

[ Out packets                  8]{lang="EN-US"}

[ Out bytes                    8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Source AS                    4]{lang="EN-US"}

[ Destination AS               4]{lang="EN-US"}

[ Input Interface Index        4]{lang="EN-US"}

[ Output Interface Index       4]{lang="EN-US"}

[ IP protocol version          1]{lang="EN-US"}

[ Direction                    1]{lang="EN-US"}

[ Sampling algorithm           1]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ Sampling interval            4]{lang="EN-US"}

[ ]{lang="EN-US"}

[AS inbound template:]{lang="EN-US"}

[ Template ID                : 3292]{lang="EN-US"}

[ Field count                : 14]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Flows                        4]{lang="EN-US"}

[ In packets                   8]{lang="EN-US"}

[ In bytes                     8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Source AS                    4]{lang="EN-US"}

[ Destination AS               4]{lang="EN-US"}

[ Input Interface Index        4]{lang="EN-US"}

[ Output Interface Index       4]{lang="EN-US"}

[ IP protocol version          1]{lang="EN-US"}

[ Direction                    1]{lang="EN-US"}

[ Sampling algorithm           1]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ Sampling interval            4]{lang="EN-US"}

[ ]{lang="EN-US"}

[L3 outbound template:]{lang="EN-US"}

[ Template ID                : 3305]{lang="EN-US"}

[ Field count                : 27]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Out packets                  8]{lang="EN-US"}

[ Out bytes                    8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Input Interface Index        4]{lang="EN-US"}

[ Output Interface Index       4]{lang="EN-US"}

[ IPv6 source address          16]{lang="EN-US"}

[ IPv6 destination address     16]{lang="EN-US"}

[ IPv6 nexthop                 16]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ IPv6 flow label              3]{lang="EN-US"}

[ Source AS                    4]{lang="EN-US"}

[ ]{lang="EN-US"}[Destination AS               4]{lang="FR"}

[ L4 source port               2]{lang="FR"}

[ L4 destination port          2]{lang="FR"}

[ IP protocol version          1]{lang="FR"}

[ TCP flags                    1]{lang="FR"}

[ Protocol                     1]{lang="FR"}

[ Source ToS                   1]{lang="FR"}

[ IPv6 source mask             1]{lang="FR"}

[ IPv6 destination mask        1]{lang="FR"}

[ Direction                    1]{lang="FR"}

[ ]{lang="FR"}[Forwarding offset            1]{lang="EN-US"}

[ Out VPN ID                   2]{lang="EN-US"}

[ Sampling algorithm           1]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ Sampling interval            4]{lang="EN-US"}

[L3 inbound template:]{lang="EN-US"}

[ Template ID                : 3306]{lang="EN-US"}

[ Field count                : 27]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Out packets                  8]{lang="EN-US"}

[ Out bytes                    8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Input Interface Index        4]{lang="EN-US"}

[ Output Interface Index       4]{lang="EN-US"}

[ IPv6 source address          16]{lang="EN-US"}

[ IPv6 destination address     16]{lang="EN-US"}

[ IPv6 nexthop                 16]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ IPv6 flow label              3]{lang="EN-US"}

[ Source AS                    4]{lang="EN-US"}

[ ]{lang="EN-US"}[Destination AS               4]{lang="FR"}

[ L4 source port               2]{lang="FR"}

[ L4 destination port          2]{lang="FR"}

[ IP protocol version          1]{lang="FR"}

[ TCP flags                    1]{lang="FR"}

[ Protocol                     1]{lang="FR"}

[ Source ToS                   1]{lang="FR"}

[ IPv6 source mask             1]{lang="FR"}

[ IPv6 destination mask        1]{lang="FR"}

[ Direction                    1]{lang="FR"}

[ ]{lang="FR"}[Forwarding offset            1]{lang="EN-US"}

[ Out VPN ID                   2]{lang="EN-US"}

[ Sampling algorithm           1]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ Sampling interval            4]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ipv6 netstream template]{lang="EN-US"}]{#struct_0_x7706_12603_x177728464}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1276005137}[[字段]{style="font-family:黑体"}]{#struct_0_x7706_12603_172252616}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7706_12603_x29603324}

[[Flow template refresh frequency]{lang="EN-US"}]{#struct_0_x7706_12603_467322732}

[[模板的包刷新率]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1425184950}

[[Flow template refresh interval]{lang="EN-US"}]{#struct_0_x7706_12603_2087106017}

[[模板的时间刷新率，单位为分钟]{style="font-family:宋体"}]{#struct_0_x7706_12603_464016325}

[[Active flow templates]{lang="EN-US"}]{#struct_0_x7706_12603_x344737325}

[[当前激活的模板数]{style="font-family:宋体"}]{#struct_0_x7706_12603_596025873}

[[Created flow templates]{lang="EN-US"}]{#struct_0_x7706_12603_x279011793}

[[创建的模板总数]{style="font-family:宋体"}]{#struct_0_x7706_12603_797215991}

[[根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"自治系统"聚合方式为例]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1818492432}

[[AS outbound template]{lang="EN-US"}]{#struct_0_x7706_12603_x914827800}

[[AS]{lang="EN-US"}]{#struct_0_x7706_12603_x1511372868}[出方向模板信息]{style="font-family:宋体"}

[[AS inbound template]{lang="EN-US"}]{#struct_0_x7706_12603_x2021500982}

[[AS]{lang="EN-US"}]{#struct_0_x7706_12603_595960337}[入方向模板信息]{style="font-family:宋体"}

[[Template ID]{lang="EN-US"}]{#struct_0_x7706_12603_1115076355}

[[模板]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7706_12603_1063775838}

[[Packets]{lang="EN-US"}]{#struct_0_x7706_12603_x1124951435}

[[使用该模板的发送报文数]{style="font-family:宋体"}]{#struct_0_x7706_12603_1812480948}

[[Last template export time]{lang="EN-US"}]{#struct_0_x7706_12603_x1947138915}

[[该模板最近的一次输出时间]{style="font-family:宋体"}]{#struct_0_x7706_12603_595894801}

[[Field count]{lang="EN-US"}]{#struct_0_x7706_12603_x2063288353}

[[模板的域总数]{style="font-family:宋体"}]{#struct_0_x7706_12603_372825613}

[[Field type]{lang="EN-US"}]{#struct_0_x7706_12603_1097548264}

[[域类型]{style="font-family:宋体"}]{#struct_0_x7706_12603_x142363860}

[[Field length (bytes)]{lang="EN-US"}]{#struct_0_x7706_12603_x1019700136}

[[域长度，单位为字节]{style="font-family:宋体"}]{#struct_0_x7706_12603_595829265}

[[Flows]{lang="EN-US"}]{#struct_0_x7706_12603_x410572012}

[[流数量]{style="font-family:宋体"}]{#struct_0_x7706_12603_x687609527}

[[Out packets]{lang="EN-US"}]{#struct_0_x7706_12603_x1857940244}

[[输出的数据包个数]{style="font-family:宋体"}]{#struct_0_x7706_12603_1626337523}

[[In packets]{lang="EN-US"}]{#struct_0_x7706_12603_596288017}

[[输入的数据包个数]{style="font-family:宋体"}]{#struct_0_x7706_12603_1520124253}

[[Out bytes]{lang="EN-US"}]{#struct_0_x7706_12603_268525911}

[[输出的数据个数，单位为字节]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1353172368}

[[In bytes]{lang="EN-US"}]{#struct_0_x7706_12603_1359076808}

[[输入的数据个数，单位为字节]{style="font-family:宋体"}]{#struct_0_x7706_12603_596222481}

[[First forwarded]{lang="EN-US"}]{#struct_0_x7706_12603_x35252875}

[[记录转发第一个报文时的系统时间，时间精确到毫秒]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1880778937}

[[Last forwarded]{lang="EN-US"}]{#struct_0_x7706_12603_1723050588}

[[记录转发最后一个报文时的系统时间，时间精确到毫秒]{style="font-family:宋体"}]{#struct_0_x7706_12603_x2001390633}

[[Source AS]{lang="EN-US"}]{#struct_0_x7706_12603_596156945}

[[源]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_x7706_12603_595436049}[号]{style="font-family:宋体"}

[[Destination AS]{lang="EN-US"}]{#struct_0_x7706_12603_1778586665}

[[目的]{style="font-family:宋体"}[AS ]{lang="EN-US"}]{#struct_0_x7706_12603_596025872}

[[Input interface index]{lang="EN-US"}]{#struct_0_x7706_12603_x279011792}

[[输入接口的索引]{style="font-family:宋体"}]{#struct_0_x7706_12603_797150455}

[[Output interface index]{lang="EN-US"}]{#struct_0_x7706_12603_206630223}

[[输出接口的索引]{style="font-family:宋体"}]{#struct_0_x7706_12603_595960336}

[[Direction]{lang="EN-US"}]{#struct_0_x7706_12603_1115076356}

[[方向字段]{style="font-family:宋体"}]{#struct_0_x7706_12603_1063710302}

[[Sampling algorithm]{lang="EN-US"}]{#struct_0_x7706_12603_1231442795}

[[采样算法]{style="font-family:宋体"}]{#struct_0_x7706_12603_595894800}

[[PAD]{lang="EN-US"}]{#struct_0_x7706_12603_x2063288354}

[[空白占位符]{style="font-family:宋体"}]{#struct_0_x7706_12603_776110140}

[[Sampling interval]{lang="EN-US"}]{#struct_0_x7706_12603_714649281}

[[采样率]{style="font-family:宋体"}]{#struct_0_x7706_12603_595829264}

[ ]{lang="EN-US"}

::: {#-366434638 .myid}
[]{#_Toc404797318}[]{#struct_0_x7706_12603_x410572011}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- enable**

------------------------------------------------------------------------

[**[enable]{lang="EN-US"}**]{#struct_0_x7706_12603_x687412919}[命令用来使能当前聚合视图对应的聚合功能。]{style="font-family:宋体"}

[**[undo enable]{lang="EN-US"}**]{#struct_0_x7706_12603_1194351540}[命令用来关闭当前聚合视图对应的聚合功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x297016271}

[**[enable]{lang="EN-US"}**]{#struct_0_x7706_12603_1240862324}

[**[undo enable]{lang="EN-US"}**]{#struct_0_x7706_12603_x463906406}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x668410549}

[[未使能当前聚合视图对应的聚合功能。]{style="font-family:宋体"}]{#struct_0_x7706_12603_1153311047}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_596288016}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_1520124254}[聚合视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_268591447}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1694448654}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x839863475}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_815093679}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1981318166}[使能]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[的自治系统聚合功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_385995451}

[\[Sysname\] ipv6 netstream aggregation as]{lang="EN-US"}

[\[Sysname-ns6-aggregation-as\] enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1737443581}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream aggregation]{lang="EN-US"}**]{#struct_0_x7706_12603_1042516281}
:::

::::: {#-1684552356 .myid}
[]{#_Toc404797319}[]{#struct_0_x7706_12603_344623001}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream**

------------------------------------------------------------------------

[**[ipv6 netstream]{lang="EN-US"}**]{#struct_0_x7706_12603_596222480}[命令用来在全局或当前接口开启]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ipv6 netstream]{lang="EN-US"}**]{#struct_0_x7706_12603_x35252874}[命令用来在全局或当前接口关闭]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1880778938}

[[系统视图：]{style="font-family:宋体"}]{#struct_0_x7706_12603_156966647}

[**[ipv6 netstream]{lang="EN-US"}**]{#struct_0_x7706_12603_x1263661274}

[**[undo ipv6 netstream]{lang="EN-US"}**]{#struct_0_x7706_12603_180502307}

[[接口视图：]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1460490412}

[**[ipv6 netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x7706_12603_617816495}

[**[undo ipv6 netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x7706_12603_x1300633200}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1811538877}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_867084629}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_596156944}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7706_12603_1284051700}[系统视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](IPv6%20NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7706_12603_x749147123}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7706_12603_1625672133}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1101128494}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x1279015867}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x1988192237}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_452483576}

[**[inbound]{lang="EN-US"}**]{#struct_0_x7706_12603_x1959149663}[：对入方向的流量进行]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x7706_12603_1007536523}[：对出方向的流量进行]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x905048965}

[[全局开启]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_596091408}[功能后，将开启所有接口入方向及出方向的]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1219826725}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1247538517}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的入方向上开启]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_1884612620}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 netstream inbound]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x2029285896}[全局开启]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_x1953827422}

[\[Sysname\] ipv6 netstream]{lang="EN-US"}
:::::

::: {#1657408528 .myid}
[]{#_Toc404797320}[]{#struct_0_x7706_12603_1284051694}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream { inbound \| outbound } filter**

------------------------------------------------------------------------

[**[ipv6 netstream filter]{lang="EN-US"}**]{#struct_0_x7706_12603_1206905860}[命令用来配置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[过滤功能，根据指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则对报文进行过滤。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 netstream filter**]{lang="EN-US"}]{#struct_0_x7706_12603_x654677556}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1493025426}

[**[ipv6 netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **filter acl** *acl-number*]{lang="EN-US"}]{#struct_0_x7706_12603_141014656}

[**[undo ipv6 netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **filter**]{lang="EN-US"}]{#struct_0_x7706_12603_x1079644610}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1137560711}

[[未启用]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x1814156319}[过滤功能，此时统计所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_596091406}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_1219826727}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1247407445}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x1189479353}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_600471676}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x422056302}

[**[inbound]{lang="EN-US"}**]{#struct_0_x7706_12603_x285161122}[：入方向过滤，即对从当前接口收到的报文进行过滤统计。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x7706_12603_x723601152}[：出方向过滤，即对从当前接口发出的报文进行过滤统计。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_x7706_12603_x632359488}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[和]{style="font-family:宋体"}[4000]{lang="EN-US"}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x23628231}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_705153830}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置根据规则号为]{style="font-family:宋体"}[2003]{lang="EN-US"}[的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则进行出方向过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_595501582}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 netstream outbound]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 netstream outbound filter acl 2003]{lang="EN-US"}

[ ]{lang="EN-US"}
:::

::::: {#914270821 .myid}
[]{#_Toc404797321}[]{#struct_0_x7706_12603_x1172844297}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream { inbound \| outbound } sampler**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](IPv6%20NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7706_12603_1659940780}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7706_12603_x761256975}
:::

[ ]{lang="EN-US"}

[**[ipv6 netstream sampler]{lang="EN-US"}**]{#struct_0_x7706_12603_x1639261122}[命令用来启用]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[采样功能。]{style="font-family:宋体"}

[**[undo ipv6 netstream sampler]{lang="EN-US"}**]{#struct_0_x7706_12603_x1778147757}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x2097780353}

[**[ipv6 netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **sampler** *sampler-name*]{lang="EN-US"}]{#struct_0_x7706_12603_384324396}

[**[undo ipv6 netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **sampler**]{lang="EN-US"}]{#struct_0_x7706_12603_x1870281099}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1617717901}

[[未启用]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x459703970}[采样功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_999179330}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1447290749}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1902686407}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_423627998}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x431869809}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1371411284}

[**[inbound]{lang="EN-US"}**]{#struct_0_x7706_12603_x87382619}[：对入方向的报文进行采样。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x7706_12603_x1687634260}[：对出方向的报文进行采样。]{style="font-family:宋体"}

[**[sampler ]{lang="EN-US"}***[sampler-name]{lang="EN-US"}*]{#struct_0_x7706_12603_x1391874375}[：采样器名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_999113794}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x1046353099}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上启用]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[采样功能，使用名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的采样器对入方向的报文进行采样，]{style="font-family:宋体"}[Netstream]{lang="EN-US"}[根据采样结果进行报文统计。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_465616191}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 netstream inbound]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 netstream inbound sampler abc]{lang="EN-US"}
:::::

::::: {#133216688 .myid}
[]{#_Toc404797322}[]{#struct_0_x7706_12603_x2141949100}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream aggregation**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](IPv6%20NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7706_12603_1110277416}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令中各参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7706_12603_x1793099263}
:::

[ ]{lang="EN-US"}

[**[ipv6 netstream aggregation]{lang="EN-US"}**]{#struct_0_x7706_12603_613992088}[命令用来设置]{style="font-family:
宋体"}[IPv6 NetStream]{lang="EN-US"}[流聚合方式，并进入相应的]{style="font-family:
宋体"}[IPv6 NetStream]{lang="EN-US"}[聚合视图。]{style="font-family:宋体"}

[**[undo ipv6 netstream aggregation]{lang="EN-US"}**]{#struct_0_x7706_12603_x312608715}[命令用来关闭]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流聚合方式，并删除流聚合方式相应的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1308330058}

[**[ipv6 netstream aggregation]{lang="EN-US"}**[ { **as** \| **bgp-nexthop** \| **destination-prefix** \| **prefix** \| **protocol-port** \| **source-prefix** }]{lang="EN-US"}]{#struct_0_x7706_12603_595501584}

[**[undo ipv6 netstream aggregation]{lang="EN-US"}**[ { **as** \| **bgp-nexthop** \| **destination-prefix** \| **prefix** \| **protocol-port** \| **source-prefix** }]{lang="EN-US"}]{#struct_0_x7706_12603_x488780542}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_379995401}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1418124914}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1048697384}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1468529813}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x673701139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x237007357}

[**[as]{lang="EN-US"}**]{#struct_0_x7706_12603_x396590119}[：自治系统聚合，根据]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流的源自治系统号、目的自治系统号、输入接口索引和输出接口索引]{style="font-family:宋体"}[4]{lang="EN-US"}[个关键项对流分类。]{style="font-family:宋体"}

[**[bgp-nexthop]{lang="EN-US"}**]{#struct_0_x7706_12603_1785079303}[：边界网关]{style="font-family:宋体"}[-]{lang="EN-US"}[下一跳聚合，根据]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、输出接口索引]{style="font-family:宋体"}[2]{lang="EN-US"}[个关键项对流分类。]{style="font-family:宋体"}

[**[destination-prefix]{lang="EN-US"}**]{#struct_0_x7706_12603_x1205450956}[：目的前缀聚合，根据]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流的目的自治系统号、目的掩码长度、目的前缀和输出接口索引]{style="font-family:宋体"}[4]{lang="EN-US"}[个关键项对流分类。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**]{#struct_0_x7706_12603_595436048}[：源和目的前缀聚合，根据]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流的源自治系统号、目的自治系统号、源掩码长度、目的掩码长度，源前缀、目的前缀、输入接口索引和输出接口索引]{style="font-family:宋体"}[8]{lang="EN-US"}[个关键项对流分类。]{style="font-family:宋体"}

[**[protocol-port]{lang="EN-US"}**]{#struct_0_x7706_12603_1778586664}[：协议]{style="font-family:宋体"}[-]{lang="EN-US"}[端口聚合，根据]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流的协议号、源端口和目的端口]{style="font-family:宋体"}[3]{lang="EN-US"}[个关键项对流分类。]{style="font-family:宋体"}

[**[source-prefix]{lang="EN-US"}**]{#struct_0_x7706_12603_x1261572093}[：源前缀聚合，根据]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流的源自治系统号、源掩码长度、源前缀和输入接口索引]{style="font-family:宋体"}[4]{lang="EN-US"}[个关键项对流分类。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1178526293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在聚合视图下，可以启用或关闭聚合功能，以及设置]{style="font-family:宋体"}]{#struct_0_x7706_12603_x81203185}[IPv6 NetStream]{lang="EN-US"}[统计输出报文源接口、目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址以及目的端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果一条流同时满足多个聚合方式，则该流会被统计到多个聚合流中。]{style="font-family:宋体"}]{#struct_0_x7706_12603_1559452953}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x85705901}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x99343903}[进入]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[自治系统聚合视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_1570376883}

[\[Sysname\] ipv6 netstream aggregation as]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1381757123}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**]{#struct_0_x7706_12603_596025871}
:::::

::::: {#1390197162 .myid}
[]{#_Toc404797323}[]{#struct_0_x7706_12603_x279011791}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream aggregation advanced**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6%20NetStream命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7706_12603_797347063}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7706_12603_1627986586}
:::

**[ ]{lang="EN-US"}**

[**[ipv6 netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_x7706_12603_336480650}[命令用来配置硬件流聚合功能。]{style="font-family:宋体"}

[**[undo ipv6 netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_x7706_12603_1084228996}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1301490989}

[**[ipv6 netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_x7706_12603_2036726404}

[**[undo ipv6 netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_x7706_12603_877338437}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x55893665}

[[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_758593350}[硬件流聚合功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_595960335}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_1115076357}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1063644766}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_19604976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x1010273208}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1662007178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能硬件流聚合功能时，系统根据]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1586330609}[IPv6 NetStream]{lang="EN-US"}[统计功能是否配置了统计信息的目的地址以及配置的聚合类型来决定是否进行硬件聚合。如果在系统视图下配置了统计信息输出的目的地址或配置了硬件聚合不支持配置的聚合类型，则硬件聚合配置不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能硬件流聚合以后，硬件聚合流表项添加到普通流表项记录中，并进行表项的输出。]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1852570646}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_88582817}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x328687228}[使能硬件流聚合功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_595894799}

[\[Sysname\] ipv6 netstream aggregation advanced]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x473832766}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream export host]{lang="EN-US"}**]{#struct_0_x7706_12603_x122426313}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream aggregation]{lang="EN-US"}**]{#struct_0_x7706_12603_792926241}
:::::

::: {#1308514480 .myid}
[]{#_Toc404797324}[]{#struct_0_x7706_12603_2040267597}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export host**

------------------------------------------------------------------------

[**[ipv6 netstream export host]{lang="EN-US"}**]{#struct_0_x7706_12603_x308809707}[命令用来配置]{style="font-family:
宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的目的地址和目的]{style="font-family:
宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:
宋体"}

[**[undo ipv6 netstream export host]{lang="EN-US"}**]{#struct_0_x7706_12603_485690201}[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_332998030}

[**[ipv6 netstream export host]{lang="EN-US"}**[ { *ip-address \| ipv6-address* } *udp-port* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x7706_12603_x971625929}

[**[undo ipv6 netstream export host]{lang="EN-US"}**[ \[ *ip-address \| ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_x7706_12603_1009803408}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1854099897}

[[系统视图和聚合视图下均没有配置目的地址和目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7706_12603_595829263}[端口号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x410572010}

[[系统视图]{style="font-family:宋体"}[/IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x687478455}[聚合视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_2057740310}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x948430736}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1775112527}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_175644191}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x7706_12603_x1572163598}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[目的地址。]{style="font-family:宋体"}

[*[Ipv6-address]{lang="EN-US"}*]{#struct_0_x7706_12603_x878793340}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的地址。]{style="font-family:宋体"}

[*[udp-port]{lang="EN-US"}*]{#struct_0_x7706_12603_x2072676551}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x7706_12603_x541008739}[：指定]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的目的地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的目的地址位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_596288015}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若某类聚合视图没有使能，则无法通过]{lang="EN-US" style="font-family:宋体"}**[display ipv6 netstream export]{lang="EN-US"}**]{#struct_0_x7706_12603_1520124251}[命令查看它的相关信息（包括目的地址的目的]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo ipv6 netstream export host]{lang="EN-US"}**]{#struct_0_x7706_12603_268394839}[命令时未指定地址，表示取消指定本视图下配置的所有地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同聚合视图下可以配置相同的目的地址和目的]{style="font-family:宋体"}]{#struct_0_x7706_12603_x439368504}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若聚合视图下没有配置目的地址和目的]{style="font-family:宋体"}]{#struct_0_x7706_12603_x366377206}[UDP]{lang="EN-US"}[端口号，则使用系统视图下的配置；若聚合视图下配置了目的地址和目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，则使用聚合视图下的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个视图下最多可配置]{style="font-family:宋体"}]{#struct_0_x7706_12603_1361400096}[4]{lang="EN-US"}[组]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[目的地址，包括不同]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。在同一视图下，若先后配置了]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址相同、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号不同的目的地址，则后配置的目的地址生效。在用户配置了不同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称时，允许配置相同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个视图下最多可配置]{style="font-family:宋体"}]{#struct_0_x7706_12603_x960539825}[4]{lang="EN-US"}[组]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的地址，包括不同]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。在同一视图下，若先后配置了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址相同、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号不同的目的地址，则后配置的目的地址生效。在用户配置了不同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称时，允许配置相同的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[普通流统计输出报文会发给系统视图下配置的所有目的地址。聚合流统计输出报文会发给聚合类型对应的聚合视图下配置的所有目的地址。]{style="font-family:宋体"}]{#struct_0_x7706_12603_x256904986}[为了减少对网络带宽的占用，可以只在聚合视图下配置]{lang="EN-US" style="font-family:宋体"}**[ipv6 netstream export host]{lang="EN-US"}**[命令，此时设备只会输出聚合流信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[undo ipv6 netstream export host]{lang="EN-US"}**]{#struct_0_x7706_12603_1605237006}[命令时，如果未指定]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则取消本视图下配置的所有]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x661446518}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x643441434}[配置全局]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[5000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_596222479}

[\[Sysname\] ipv6 netstream export host 1.1.1.1 5000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x602825084}[配置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[自治系统聚合统计输出报文的目的地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[6000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_57686260}

[\[Sysname\] ipv6 netstream aggregation as]{lang="EN-US"}

[\[Sysname-ns6-aggregation-as\] ipv6 netstream export host 1.1.1.2 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x844556931}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream aggregation]{lang="EN-US"}**]{#struct_0_x7706_12603_1534547340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream export source]{lang="EN-US"}**]{#struct_0_x7706_12603_x1410222430}
:::

::: {#916842177 .myid}
[]{#_Toc404797325}[]{#struct_0_x7706_12603_x1713067231}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export rate**

------------------------------------------------------------------------

[**[ipv6 netstream export rate]{lang="EN-US"}**]{#struct_0_x7706_12603_x114544242}[命令用来配置输出速率限制，即限制每秒钟输出的报文数。]{style="font-family:
宋体"}

[**[undo ipv6 netstream export rate]{lang="EN-US"}**]{#struct_0_x7706_12603_x1276205842}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_x7706_12603_5311332}

[**[ipv6 netstream export]{lang="EN-US"}***[ ]{lang="EN-US"}***[rate]{lang="EN-US"}***[ rate]{lang="EN-US"}*]{#struct_0_x7706_12603_x1269888079}

[**[undo ipv6 netstream export]{lang="EN-US"}***[ ]{lang="EN-US"}***[rate]{lang="EN-US"}**]{#struct_0_x7706_12603_1056191924}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x941969323}

[[NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_596156943}[统计输出报文的输出速率不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1284051695}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_1206971396}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1264097127}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x1052736501}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x1902920527}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x105275234}

[*[rate]{lang="EN-US"}*]{#struct_0_x7706_12603_1695233988}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的输出速率限制，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为每秒允许输出的最多报文个数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_741145365}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1285655781}[设置每秒最多允许]{style="font-family:宋体"}[10]{lang="EN-US"}[个报文被输出。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_596091407}

[\[Sysname\] ipv6 netstream export rate 10]{lang="EN-US"}
:::

::: {#-443447757 .myid}
[]{#_Toc404797326}[]{#struct_0_x7706_12603_1219826728}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export source**

------------------------------------------------------------------------

[**[ipv6 netstream export source]{lang="EN-US"}**]{#struct_0_x7706_12603_1246817621}[命令用来配置]{style="font-family:
宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的源接口。]{style="font-family:
宋体"}

[**[undo ipv6 netstream export source]{lang="EN-US"}**]{#struct_0_x7706_12603_x63964215}[命令用来取消配置的输出报文的源接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1063046159}

[**[ipv6 netstream export source interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x7706_12603_800919409}

[**[undo ipv6 netstream export source]{lang="EN-US"}**]{#struct_0_x7706_12603_x347664379}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x623034587}

[[采用统计输出报文的出接口作为源接口。]{style="font-family:宋体"}]{#struct_0_x7706_12603_193932799}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1746225306}

[[系统视图]{style="font-family:宋体"}[/IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_595501583}[聚合视图]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x488780537}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x7706_12603_379667728}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文的源接口，由接口类型和接口编号组成。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x2018917121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令配置源接口后，会将]{style="font-family:宋体"}]{#struct_0_x7706_12603_1313292908}[NetStream]{lang="EN-US"}[统计输出报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址设置为该接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同聚合视图下可以配置不同的源接口。]{style="font-family:宋体"}]{#struct_0_x7706_12603_699866161}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合视图下若没有配置源接口，则使用系统视图下的配置。]{style="font-family:宋体"}]{#struct_0_x7706_12603_1122747752}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议使用以太网管理接口作为源接口，与服务器相连，并向服务器输出统计信息。]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1551122711}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1149324260}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x61433957}[将全局]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文源接口设置为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_595436047}

[\[Sysname\] ipv6 netstream export source interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x603021691}[将]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[自治系统聚合统计输出报文源接口设置为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_x1101372143}

[\[Sysname\] ipv6 netstream aggregation as]{lang="EN-US"}

[\[Sysname-ns6-aggregation-as\] ipv6 netstream export source interface gigabitethernet 1/0/2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1778586679}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream aggregation]{lang="EN-US"}**]{#struct_0_x7706_12603_x1261768702}
:::

::: {#-619483088 .myid}
[]{#_Toc404797327}[]{#struct_0_x7706_12603_x1753470928}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export v9-template refresh-rate packet**

------------------------------------------------------------------------

[**[ipv6 netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_x7706_12603_1911203762}[命令用来配置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率。]{style="font-family:宋体"}

[**[undo ipv6 netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_x7706_12603_x489642088}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1540924418}

[**[ipv6 netstream export v9-template refresh-rate packet ]{lang="EN-US"}***[packets]{lang="EN-US"}*]{#struct_0_x7706_12603_x1893069084}

[**[undo ipv6 netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_x7706_12603_2137741924}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1693346846}

[[每隔]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_x7706_12603_596025870}[个包设备发送一次版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x279011790}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_797281527}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_445020763}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1130881046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1815322492}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x2123752437}

[*[packets]{lang="EN-US"}*]{#struct_0_x7706_12603_x1369101175}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为上报报文的个数，即每隔多少个包发送一次模板，通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模版格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1899399350}

[[版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_x7706_12603_975847258}[是基于模板方式的、可支持自定义格式，所以设备上需要定期刷新模板，并通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模版格式。用户可以根据实际情况，配置版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率，及时更新模板。]{style="font-family:宋体"}

[[可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_595960334}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1115076358}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1064627806}[将]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率设为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_x467827769}

[\[Sysname\] ipv6 netstream export v9-template refresh-rate packet 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1657777661}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_x7706_12603_2085918227}
:::

::: {#-1839703837 .myid}
[]{#_Toc404797328}[]{#struct_0_x7706_12603_x942619442}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export v9-template refresh-rate time**

------------------------------------------------------------------------

[**[ipv6 netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_x7706_12603_1765944071}[命令用来配置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率。]{style="font-family:宋体"}

[**[undo ipv6 netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_x7706_12603_1606165781}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x207197495}

[**[ipv6 netstream export v9-template refresh-rate time ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_x7706_12603_595894798}

[**[undo ipv6 netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_x7706_12603_x473832767}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x122360777}

[[每隔]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x7706_12603_1182662910}[分钟设备发送一次版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1708953081}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_1771089455}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_519838616}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x604557048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x835301609}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_709782935}

[*[minutes]{lang="EN-US"}*]{#struct_0_x7706_12603_x913496385}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为分钟，即每隔多少分钟更新一次模板，通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的]{style="font-family:宋体"}[V9]{lang="EN-US"}[模版格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_595829262}

[[V9]{lang="EN-US"}]{#struct_0_x7706_12603_x410572009}[版本是基于模板方式的、可支持自定义格式，所以设备上需要定期刷新模板，并通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的]{style="font-family:宋体"}[V9]{lang="EN-US"}[模版格式。用户可以根据实际情况，配置版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率，及时更新模板。]{style="font-family:宋体"}

[[可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_x687937208}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1910922465}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x1433159897}[将]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率设为]{style="font-family:宋体"}[60]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_x2068413586}

[\[Sysname\] ipv6 netstream export v9-template refresh-rate time 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1965852358}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_x7706_12603_x585745411}
:::

::: {#859709601 .myid}
[]{#_Toc404797329}[]{#struct_0_x7706_12603_71011346}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream export version 9**

------------------------------------------------------------------------

[**[ipv6 netstream export version 9]{lang="EN-US"}**]{#struct_0_x7706_12603_596288014}[命令用来配置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[版本]{style="font-family:宋体"}[9]{lang="EN-US"}[的自治系统选项和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳选项。]{style="font-family:宋体"}

[**[undo ipv6 netstream export version]{lang="EN-US"}**]{#struct_0_x7706_12603_1520124252}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_268460375}

[**[ipv6 netstream export version]{lang="EN-US"}**[ **9** \[ **origin-as** \| **peer-as** \] \[ **bgp-nexthop** \]]{lang="EN-US"}]{#struct_0_x7706_12603_2105079450}

[**[undo ipv6 netstream export version]{lang="EN-US"}**]{#struct_0_x7706_12603_108474593}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x193610213}

[[IPv6]{lang="EN-US"}]{#struct_0_x7706_12603_x528865690}[普通流信息、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[聚合统计流信息和带]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[选项信息的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流信息都通过版本]{style="font-family:宋体"}[9]{lang="EN-US"}[的]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文发送。流统计信息中记录邻接自治系统号（]{style="font-family:宋体"}[peer-as]{lang="EN-US"}[），流信息中不记录]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x652368877}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1126656232}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x495268011}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x300121942}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_596222478}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x844556930}

[**[origin-as]{lang="EN-US"}**]{#struct_0_x7706_12603_1534481804}[：流信息中记录的自治系统号为起始自治系统号。]{style="font-family:宋体"}

[**[peer-as]{lang="EN-US"}**]{#struct_0_x7706_12603_529375227}[：流信息中记录的自治系统号为邻接自治系统号。]{style="font-family:宋体"}

[**[bgp-nexthop]{lang="EN-US"}**]{#struct_0_x7706_12603_x1627955431}[：流信息中记录]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1511520950}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 NetStream]{lang="EN-US"}]{#struct_0_x7706_12603_1478558844}[流信息中会记录流的源]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址及其对应的自治系统号；目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及其对应的自治系统号。设备会根据用户实际配置的自治系统参数来确定记录的自治系统号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使用]{style="font-family:宋体"}]{#struct_0_x7706_12603_x2088005752}[ipv6 netstream export version 9]{lang="EN-US"}[配置输出版本信息时，如果没有配置任何选项，则流统计信息中记录邻接自治系统号（]{style="font-family:宋体"}[peer-as]{lang="EN-US"}[），流信息中不记录]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_253003850}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1910156657}[将]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[统计采用起始自治系统号作为给定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的自治系统号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_596156942}

[\[Sysname\] ipv6 netstream export version 9 origin-as]{lang="EN-US"}
:::

::: {#916006254 .myid}
[]{#_Toc404797330}[]{#struct_0_x7706_12603_x488780536}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream max-entry**

------------------------------------------------------------------------

[**[ipv6 netstream max-entry]{lang="EN-US"}**]{#struct_0_x7706_12603_379733264}[命令用来配置]{style="font-family:
宋体"}[IPv6 NetStream]{lang="EN-US"}[流缓存区中流表项的最大数目，或者达到流表项的最大数目时的处理方式。]{style="font-family:
宋体"}

[**[undo ipv6 netstream max-entry]{lang="EN-US"}**]{#struct_0_x7706_12603_1942644367}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x168136414}

[**[ipv6 netstream max-entry]{lang="EN-US"}**[ { *max-entries* \| **aging** \| **disable-caching** }]{lang="EN-US"}]{#struct_0_x7706_12603_x1773806492}

[**[undo ipv6 netstream max-entry]{lang="EN-US"}**]{#struct_0_x7706_12603_x1254084412}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1694958870}

[[本命令的缺省情况与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x7706_12603_1541124786}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_595436046}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_1778586678}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1261834238}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x416236744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1623243565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_2122355188}

[*[max-entries]{lang="EN-US"}*]{#struct_0_x7706_12603_1957677299}[：]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流缓存区中流表项的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[aging]{lang="EN-US"}**]{#struct_0_x7706_12603_x238553959}[：达到流表项的最大数目时，强制老化部分流表项。]{style="font-family:宋体"}

[**[disable-caching]{lang="EN-US"}**]{#struct_0_x7706_12603_x268282092}[：达到流表项的最大数目时，禁止新建流表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1011878351}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-entries]{lang="EN-US"}*]{#struct_0_x7706_12603_x72505096}[参数值在各单板上单独生效，而不是各单板的总和。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-entries]{lang="EN-US"}*]{#struct_0_x7706_12603_999310402}[参数值在各成员设备上单独生效，而不是各成员设备的总和。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream max-entry]{lang="EN-US"}**[ *max-entries*]{lang="EN-US"}]{#struct_0_x7706_12603_x1610987264}[命令可重复配置，以最后一次配置为准。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream max-entry]{lang="EN-US"}**[ { **aging** \| **disable-caching** }]{lang="EN-US"}]{#struct_0_x7706_12603_x602562939}[命令可重复配置，以最后一次配置为准。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1374379111}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x653976648}[设置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[流缓存区中流表项的最大数目为]{style="font-family:宋体"}[5000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_2016753479}

[\[Sysname\] ipv6 netstream max-entry 5000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_x1576297799}[设置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[在达到流表项的最大数目时，禁止新建流表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_1986272808}

[\[Sysname\] ipv6 netstream max-entry disable-caching]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_404917886}[设置]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[在达到流表项的最大数目时，强制老化部分流表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_999244866}

[\[Sysname\] ipv6 netstream max-entry aging]{lang="EN-US"}
:::

::: {#845167650 .myid}
[]{#_Toc404797331}[]{#struct_0_x7706_12603_x1340761326}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream timeout active**

------------------------------------------------------------------------

[**[ipv6 netstream timeout active]{lang="EN-US"}**]{#struct_0_x7706_12603_411101545}[命令用来配置流的活跃老化时间。]{style="font-family:
宋体"}

[**[undo ipv6 netstream timeout active]{lang="EN-US"}**]{#struct_0_x7706_12603_159469040}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x199862166}

[**[ipv6 netstream timeout active]{lang="EN-US"}**[ *minutes*]{lang="EN-US"}]{#struct_0_x7706_12603_1782988145}

[**[undo ipv6 netstream timeout active]{lang="EN-US"}**]{#struct_0_x7706_12603_x656879242}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_999572546}

[[流的活跃老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x7706_12603_991876139}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1671867962}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_1466661643}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1289238495}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_13120354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x555003079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_1422037970}

[*[minutes]{lang="EN-US"}*]{#struct_0_x7706_12603_1523564362}[：流的活跃老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1009753906}

[[从采集到的第一个报文]{style="font-family:宋体"}]{#struct_0_x7706_12603_999507010}[开始，该]{style="font-family:宋体"}[流在]{style="font-family:宋体"}[指定的时间内能被采集到，则该流属于活跃的流，指定的时间称为流的活跃老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1718979019}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1444855640}[将流的活跃老化时间设置为]{style="font-family:宋体"}[60]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_x67771135}

[\[Sysname\] ipv6 netstream timeout active 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x85225975}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream timeout inactive]{lang="EN-US"}**]{#struct_0_x7706_12603_537403935}
:::

::: {#1131147260 .myid}
[]{#_Toc404797332}[]{#struct_0_x7706_12603_x1043854709}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- ipv6 netstream timeout inactive**

------------------------------------------------------------------------

[**[ipv6 netstream timeout inactive]{lang="EN-US"}**]{#struct_0_x7706_12603_x218514269}[命令用来配置流的不活跃老化时间。]{style="font-family:宋体"}

[**[undo ipv6 netstream timeout inactive]{lang="EN-US"}**]{#struct_0_x7706_12603_x337009428}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1426845202}

[**[ipv6 netstream timeout inactive]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x7706_12603_999441474}

[**[undo ipv6 netstream timeout inactive]{lang="EN-US"}**]{#struct_0_x7706_12603_591611961}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7706_12603_622863424}

[[流的不活跃老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x7706_12603_2021278405}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x467416075}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x898835221}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_131105916}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_777008488}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_83946996}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7706_12603_731787332}

[*[seconds]{lang="EN-US"}*]{#struct_0_x7706_12603_999375938}[：流的不活跃老化时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1413620273}

[[从采集到的最后一个报文开始，该流在指定的时间内没有被采集到，则该流属于不活跃的流，指定的时间称为流的不活跃老化时间。]{style="font-family:宋体"}]{#struct_0_x7706_12603_x1050391079}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1163567895}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1532004663}[将流的不活跃老化时间设置为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7706_12603_1835680436}

[\[Sysname\] ipv6 netstream timeout inactive 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1221651242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 netstream timeout active]{lang="EN-US"}**]{#struct_0_x7706_12603_x857758519}
:::

::: {#56245110 .myid}
[]{#_Toc404797333}[]{#struct_0_x7706_12603_x472148091}

**IPv6 NetStream \-- IPv6 NetStream配置命令 \-- reset ipv6 netstream statistics**

------------------------------------------------------------------------

[**[reset ipv6]{lang="EN-US"}**[ **netstream statistics**]{lang="EN-US"}]{#struct_0_x7706_12603_x453812963}[命令用来将流缓存区中所有流强制老化，输出报文信息，并清空]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[缓冲区的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7706_12603_222497237}

[**[reset ipv6]{lang="EN-US"}**[ **netstream statistics**]{lang="EN-US"}]{#struct_0_x7706_12603_x1616113851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7706_12603_998786114}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x7706_12603_x24114527}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7706_12603_304984821}

[[network-admin]{lang="EN-US"}]{#struct_0_x7706_12603_1802100419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7706_12603_x546430004}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x804318899}

[[在执行清除缓冲区中老化流的动作时，命令行会给出提示，告知用户这个动作可能要持续几分钟，在这段时间内不能统计。]{style="font-family:宋体"}]{#struct_0_x7706_12603_x680618526}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7706_12603_x1499094959}

[[\# ]{lang="EN-US"}]{#struct_0_x7706_12603_1045606675}[将流缓存区中所有流老化，并清空]{style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[缓冲区的状态信息和输出报文信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 netstream statistics]{lang="EN-US"}]{#struct_0_x7706_12603_x2131720213}

[This process may take a few minutes.]{lang="EN-US"}

[NetStream statistic function is disabled during this process.]{lang="EN-US"}
:::
