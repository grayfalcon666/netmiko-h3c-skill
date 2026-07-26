::: {#1153695161 .myid}
[]{#_Toc404797263}[]{#struct_0_84792_x5137_206243796}[]{#_Toc250995600}[]{#_Toc55050581}[]{#_Toc28576987}

**NetStream \-- NetStream配置命令 \-- display ip netstream cache**

------------------------------------------------------------------------

[**[display ip netstream cache]{lang="EN-US"}**]{#struct_0_84792_x5137_1601665034}[命令用来查看]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[流缓存区的配置和状态信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1941925947}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_84792_x5137_794092770}

[**[display ip netstream cache ]{lang="EN-US"}**[\[ **verbose** \]]{lang="EN-US"}]{#struct_0_84792_x5137_x384834510}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_84792_x5137_x979888167}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip netstream]{lang="EN-US"}**[ **cache** \[ **slot** *slot-number* \[ *cpu cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_84792_x5137_x294756823}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_84792_x5137_x966717568}[模式：]{style="font-family:宋体"}

[**[display ip netstream]{lang="EN-US"}**[ **cache** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_84792_x5137_429805986}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1288951247}

[[任意视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1718335485}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_238205828}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1941991483}

[[network-operator]{lang="EN-US"}]{#struct_0_84792_x5137_1943189330}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_608787753}

[[mdc-operator]{lang="EN-US"}]{#struct_0_84792_x5137_75544777}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1110959181}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_84792_x5137_499659843}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_533503734}[：显示指定成员设备上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示成员设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_1114226585}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示成员设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number slot* *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_x119429566}[：显示指定成员设备上指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number slot* *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_1114423193}[：显示指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_84792_x5137_220695365}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_84792_x5137_1557332704}[：显示]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流缓冲区的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1942057019}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1321272114}[查看]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流缓冲区详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ip netstream cache verbose]{lang="EN-US"}]{#struct_0_84792_x5137_1941663803}

[IP NetStream cache information:]{lang="EN-US"}

[  Active flow timeout             : 60 min]{lang="EN-US"}

[  Inactive flow timeout           : 10 sec]{lang="EN-US"}

[  Max number of entries           : 1000]{lang="EN-US"}

[  IP active flow entries          : 1]{lang="EN-US"}

[  MPLS active flow entries        : 2]{lang="EN-US"}

[  L2 active flow entries          : 1]{lang="EN-US"}

[  IPL2 active flow entries        : 1]{lang="EN-US"}

[  IP flow entries counted         : 10]{lang="EN-US"}

[  MPLS flow entries counted       : 20]{lang="EN-US"}

[  L2 flow entries counted         : 10]{lang="EN-US"}

[  IPL2 flow entries counted       : 20]{lang="EN-US"}

[  Last statistics resetting time  : 01/01/2000 at 00:01:02]{lang="EN-US"}

[ ]{lang="EN-US"}

[IP packet size distribution (1103746 packets in total):]{lang="EN-US"}

[1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480]{lang="EN-US"}

[.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[ 512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608]{lang="EN-US"}

[.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)]{lang="EN-US"}

[                  Flows /sec       /sec   /flow   /flow       /flow]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[TCP-Telnet      2656855     372        4       86          49        27]{lang="EN-US"}

[TCP-FTP         5900082      86        9        9          11        33]{lang="EN-US"}

[TCP-FTPD        3200453    1006        5      193          45        33]{lang="EN-US"}

[TCP-WWW       546778274   11170      887       12           8        32]{lang="EN-US"}

[TCP-other      49148540    3752       79       47          30        32]{lang="EN-US"}

[UDP-DNS       117240379     570      190        3           7        34]{lang="EN-US"}

[UDP-other      45502422    2272       73       30           8        37]{lang="EN-US"}

[ICMP           14837957     125       24        5          12        34]{lang="EN-US"}

[IP-other          77406       5        0       47          52        27]{lang="EN-US"}

[ ]{lang="EN-US"}

[Type DstIP(Port)            SrcIP(Port)            Pro ToS If(Direct)  Pkts]{lang="EN-US"}

[     DstMAC(VLAN)           SrcMAC(VLAN)]{lang="EN-US"}

[     TopLblType(IP/Mask)    Lbl-Exp-S-List]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[IP   11.1.1.1(1024)         11.1.1.2(21)           6   128 ET1/1(I)    42996]{lang="DA"}

[  ]{lang="DA"}[   TCPFlag:      27]{lang="EN-US"}

[     DstMask:      24       SrcMask:      24       NextHop:      0.0.0.0]{lang="EN-US"}

[     DstAS:         0       SrcAS:         0       BGPNextHop:   0.0.0.0]{lang="EN-US"}

[     ]{lang="EN-US"}[InVRF:        10]{lang="NO-BOK"}

[     SamplerMode:   2       SamplerInt:  256]{lang="NO-BOK"}

[     Active:  120.600       Bytes/Pkt:   152]{lang="NO-BOK"}

[L2   0012-3f86-e94c(10)     0012-3f86-e86a(0)              GE1/4/1(I)  1253]{lang="DA"}

[     SamplerMode:   1       SamplerInt:   64 ]{lang="NO-BOK"}

[     Active:    5.510       Bytes/Pkt:   210]{lang="NO-BOK"}

[MPLS LDP(3.3.3.3/24)        1:18-6-0                       GE1/0/2(O)  291]{lang="DA"}

[                            ]{lang="DA"}[2:24-6-0]{lang="EN-US"}

[                            3:30-6-1]{lang="EN-US"}

[     SamplerMode:   0       SamplerInt:    0]{lang="NO-BOK"}

[     Active:  660.084       Bytes/Pkt:   100]{lang="NO-BOK"}

[IP&  192.168.123.1(2048)    192.168.1.1(0)         1   0   GE1/0/2(O)  10]{lang="EN-US"}

[L2   0012-3f86-e95d(0)      0012-3f86-e116(1008)]{lang="EN-US"}

[     ]{lang="NO-BOK"}[TCPFlag:      27]{lang="EN-US"}

[     DstMask:      24       SrcMask:      24       NextHop:    192.168.1.2]{lang="NO-BOK"}

[     DstAS:         0       SrcAS:         0       BGPNextHop: 0.0.0.0]{lang="NO-BOK"}

[     OutVRF:        0       TCPFlag:    0]{lang="NO-BOK"}

[     SamplerMode:   0       SamplerInt:    0]{lang="NO-BOK"}

[     Active:   12.030       Bytes/Pkt:    86]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}

[IP&  172.16.1.1(68)         172.16.2.1(67)         17  64  GE1/0/3(I)  1848]{lang="EN-US"}

[MPLS LDP(4.4.4.4/24)        1:55-6-0]{lang="EN-US"}

[                            2:16-6-1]{lang="EN-US"}

[     TCPFlag:       0]{lang="NO-BOK"}

[     DstMask:      24       SrcMask:      24       NextHop:    172.16.2.10]{lang="NO-BOK"}

[     DstAS:         0       SrcAS:         0       BGPNextHop: 0.0.0.0]{lang="NO-BOK"}

[     ]{lang="NO-BOK"}[InVRF:         0]{lang="EN-US"}

[     SamplerMode:   0       SamplerInt:    0]{lang="EN-US"}

[     Active:  382.542       Bytes/Pkt:  1426]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x7811335}[查看]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流缓冲区详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display ip netstream cache slot 1 verbose]{lang="EN-US"}]{#struct_0_84792_x5137_1942384699}

[IP NetStream information:]{lang="EN-US"}

[  Active flow timeout                : 60 min]{lang="EN-US"}

[  Inactive flow timeout              : 10 sec]{lang="EN-US"}

[  Max number of entries              : 1000]{lang="EN-US"}

[  IP active flow entries             : 1]{lang="EN-US"}

[  MPLS active flow entries           : 2]{lang="EN-US"}

[  L2 active flow entries             : 1]{lang="EN-US"}

[  IPL2 active flow entries           : 1]{lang="EN-US"}

[  IP flow entries counted            : 10]{lang="EN-US"}

[  MPLS flow entries counted          : 20]{lang="EN-US"}

[  L2 flow entries counted            : 10]{lang="EN-US"}

[  IPL2 flow entries counted          : 20]{lang="EN-US"}

[  Last statistics resetting time     : 01/01/2012 at 00:01:02]{lang="EN-US"}

[ ]{lang="EN-US"}

[IP packet size distribution (1103746 packets in total):]{lang="EN-US"}

[1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480]{lang="EN-US"}

[.249 .694 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[ 512  544  576 1024 1536 2048 2560 3072 3584 4096 4608 \>4608]{lang="EN-US"}

[.000 .000 .027 .000 .027 .000 .000 .000 .000 .000 .000 .000]{lang="EN-US"}

[ ]{lang="EN-US"}

[Protocol          Total Packets    Flows  Packets Active(sec) Idle(sec)]{lang="EN-US"}

[                  Flows /sec       /sec   /flow   /flow       /flow]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[TCP-Telnet      2656855     372        4       86          49        27]{lang="EN-US"}

[TCP-FTP         5900082      86        9        9          11        33]{lang="EN-US"}

[TCP-FTPD        3200453    1006        5      193          45        33]{lang="EN-US"}

[TCP-WWW       546778274   11170      887       12           8        32]{lang="EN-US"}

[TCP-other      49148540    3752       79       47          30        32]{lang="EN-US"}

[UDP-DNS       117240379     570      190        3           7        34]{lang="EN-US"}

[UDP-other      45502422    2272       73       30           8        37]{lang="EN-US"}

[ICMP           14837957     125       24        5          12        34]{lang="EN-US"}

[IP-other          77406       5        0       47          52        27]{lang="EN-US"}

[ ]{lang="EN-US"}

[Type DstIP(Port)            SrcIP(Port)            Pro ToS If(Direct)  Pkts]{lang="EN-US"}

[     DstMAC(VLAN)           SrcMAC(VLAN)]{lang="EN-US"}

[     TopLblType(IP/Mask)    Lbl-Exp-S-List]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[IP   11.1.1.1(1024)         11.1.1.2(21)           6   128 ET1/1(I)    42996]{lang="EN-US"}

[     TCPFlag:      27]{lang="EN-US"}

[     DstMask:      24       SrcMask:      24       NextHop:      0.0.0.0]{lang="EN-US"}

[     DstAS:         0       SrcAS:         0       BGPNexthop:   0.0.0.0]{lang="EN-US"}

[     ]{lang="EN-US"}[InVRF:        10]{lang="NO-BOK"}

[     SamplerMode:   2       SamplerInt:  256]{lang="NO-BOK"}

[     Active:  120.600       Bytes/Pkt:   152]{lang="NO-BOK"}

[L2   0012-3f86-e94c(10)     0012-3f86-e86a(0)              GE1/4/1(I)  1253]{lang="NO-BOK"}

[     SamplerMode:   1       SamplerInt:   64]{lang="NO-BOK"}

[     Active:    5.510       Bytes/Pkt:   210]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}

[MPLS LDP(3.3.3.3/24)        1:18-6-0                       GE1/0/2(O)  291]{lang="NO-BOK"}

[                            2:24-6-0]{lang="NO-BOK"}

[                            3:30-6-1]{lang="NO-BOK"}

[     SamplerMode:   0       SamplerInt:    0]{lang="NO-BOK"}

[     Active:  660.084       Bytes/Pkt:   100]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}

[IP&  192.168.123.1(2048)    192.168.1.1(0)         1   0   GE1/0/2(O)  10]{lang="NO-BOK"}

[L2   0012-3f86-e95d(0)      0012-3f86-e116(1008)]{lang="NO-BOK"}

[     DstMask:      24       SrcMask:      24       NextHop:    192.168.1.2]{lang="NO-BOK"}

[     DstAS:         0       SrcAS:         0       BGPNexthop: 0.0.0.0]{lang="NO-BOK"}

[     OutVRF:        0       TCPFlag:    0]{lang="NO-BOK"}

[     SamplerMode:   0       SamplerInt:    0]{lang="NO-BOK"}

[     Active:   12.030       Bytes/Pkt:    86]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}

[IP&  172.16.1.1(68)         172.16.2.1(67)         17  64  GE1/0/3(I)  1848]{lang="NO-BOK"}

[MPLS LDP(4.4.4.4/24)        1:55-6-0]{lang="NO-BOK"}

[                            2:16-6-1 ]{lang="NO-BOK"}

[     DstMask:      24       SrcMask:      24       NextHop:    172.16.2.10]{lang="NO-BOK"}

[     DstAS:         0       SrcAS:         0       BGPNextHop: 0.0.0.0]{lang="NO-BOK"}

[     ]{lang="NO-BOK"}[InVRF:         0]{lang="EN-US"}

[     SamplerMode:   0       SamplerInt:    0]{lang="EN-US"}

[     Active:  382.542       Bytes/Pkt:  1426]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip netstream cache]{lang="EN-US"}]{#struct_0_84792_x5137_1047228806}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x517174841}[[字段]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1936070416}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_84792_x5137_529681333}

[[IP NetStream information]{lang="EN-US"}]{#struct_0_84792_x5137_x1493309327}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_1385235112}[流缓存区信息]{style="font-family:宋体"}

[[Active flow timeout]{lang="EN-US"}]{#struct_0_84792_x5137_1942450235}

[[活跃流的老化时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_84792_x5137_x179158189}

[[Inactive flow timeout]{lang="EN-US"}]{#struct_0_84792_x5137_x822256356}

[[不活跃流的老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_84792_x5137_1491736443}

[[Max number of entries]{lang="EN-US"}]{#struct_0_84792_x5137_x91995770}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x1065138275}[流缓存区中允许的最大流数]{style="font-family:宋体"}

[[IP active flow entries]{lang="EN-US"}]{#struct_0_84792_x5137_1941860412}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x809286963}[流缓存区中活跃的]{style="font-family:宋体"}[IP]{lang="EN-US"}[流数]{style="font-family:宋体"}

[[MPLS active flow entries]{lang="EN-US"}]{#struct_0_84792_x5137_x1788945936}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x196384375}[流缓存区中活跃的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流数]{style="font-family:宋体"}

[[L2 active flow entries]{lang="EN-US"}]{#struct_0_84792_x5137_345962551}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x1776495159}[流缓存区中活跃的二层流数]{style="font-family:宋体"}

[[IPL2 active flow entries]{lang="EN-US"}]{#struct_0_84792_x5137_1941925948}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_794682594}[流缓存区中活跃的二层和三层流数]{style="font-family:宋体"}

[[IP flow entries counted]{lang="EN-US"}]{#struct_0_84792_x5137_1198968203}

[[已经被统计的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_84792_x5137_x533286226}[流数]{style="font-family:宋体"}

[[MPLS flow entries counted]{lang="EN-US"}]{#struct_0_84792_x5137_x536414024}

[[已经被统计的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_84792_x5137_1941991484}[流数]{style="font-family:宋体"}

[[L2 flow entries counted]{lang="EN-US"}]{#struct_0_84792_x5137_1943385938}

[[已经被统计的二层流数]{style="font-family:宋体"}]{#struct_0_84792_x5137_1074390571}

[[IPL2 flow entries counted]{lang="EN-US"}]{#struct_0_84792_x5137_x763808471}

[[已经被统计的二层和三层流数]{style="font-family:宋体"}]{#struct_0_84792_x5137_x570131218}

[[Last statistics resetting time]{lang="EN-US"}]{#struct_0_84792_x5137_1942057020}

[[上次清除统计的时间]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1320682287}

[[该字段只在执行了]{style="font-family:宋体"}**[reset ip netstream statistics]{lang="EN-US"}**]{#struct_0_84792_x5137_x279716041}[命令后才会显示为时间，否则显示为]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[IP packet size distribution (1103746 packets in total)]{lang="EN-US"}]{#struct_0_84792_x5137_1145683520}

[[IP]{lang="EN-US"}]{#struct_0_84792_x5137_x25506057}[报文按大小分布情况，括号中为]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文总数。]{style="font-family:宋体"}

[[分布值按占]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_84792_x5137_1941598268}[报文总数的比率显示，只显示]{style="font-family:宋体"}[3]{lang="EN-US"}[位小数，如"]{style="font-family:宋体"}[.027]{lang="EN-US"}["表示占]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文总数的]{style="font-family:宋体"}[0.027]{lang="EN-US"}

[[1-32   64   96  128  160  192  224  256  288]{lang="EN-US"}]{#struct_0_84792_x5137_716957701}

[[320  352  384  416  448  480 512  544  576]{lang="EN-US"}]{#struct_0_84792_x5137_x1799067167}

[[1024 1536 2048 2560 3072 3584 4096 4608]{lang="EN-US"}]{#struct_0_84792_x5137_50731913}

[[IP]{lang="EN-US"}]{#struct_0_84792_x5137_x594497492}[报文尺寸区间（报文长度不包括二层链路层的头）。长度不超过]{style="font-family:宋体"}[576]{lang="EN-US"}[字节时，以]{style="font-family:宋体"}[32]{lang="EN-US"}[字节为单位递增，例如："]{style="font-family:宋体"}[1-32]{lang="EN-US"}["是长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字节的报文数目，"]{style="font-family:宋体"}[64]{lang="EN-US"}["是长度为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[字节的报文数。长度超过]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节时，以]{style="font-family:宋体"}[512]{lang="EN-US"}[字节为单位递增，例如"]{style="font-family:宋体"}[1536]{lang="EN-US"}["是长度为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[1536]{lang="EN-US"}[字节的报文数。长度在]{style="font-family:宋体"}[577]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[间的报文记录在]{style="font-family:宋体"}[1024]{lang="EN-US"}[项中]{style="font-family:宋体"}

[[Protocol     Total Flows     Packets /sec]{lang="EN-US"}]{#struct_0_84792_x5137_1941663804}

[[Flows/sec   Packets/flow]{lang="EN-US"}]{#struct_0_84792_x5137_x7745799}

[[Active(sec)/flow     Idle(sec)/flow]{lang="EN-US"}]{#struct_0_84792_x5137_2044004944}

[[按协议分类的报文统计信息：协议类型、总流数、每秒的报文数、每秒的流数、平均每条流的报文数、平均每条流的活跃时间、平均每条流的非活跃时间]{style="font-family:宋体"}]{#struct_0_84792_x5137_x2090572563}

[[Type DstIP(Port)            SrcIP(Port)            Pro ToS If(Direct)  Pkts]{lang="EN-US"}]{#struct_0_84792_x5137_1941729340}

[[当前流缓存区中活跃流的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_84792_x5137_1092705516}[层信息：流的类型、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（目的端口号）、源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（源端口号）、协议号、服务类型、接口名（方向）、包数]{style="font-family:宋体"}

[[其中流的类型有五种：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_84792_x5137_456373790}[流（]{style="font-family:宋体"}[IP]{lang="EN-US"}[）、二层流（]{style="font-family:宋体"}[L2]{lang="EN-US"}[）、二三层混合流（]{style="font-family:宋体"}[IP&L2]{lang="EN-US"}[）、不带]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流（]{style="font-family:宋体"}[MPLS)]{lang="EN-US"}[、带]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流（]{style="font-family:宋体"}[IP&MPLS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[需要注意的是，对于]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_84792_x5137_1512402794}[报文只有]{style="font-family:宋体"}[Type]{lang="EN-US"}[和]{style="font-family:宋体"}[Code]{lang="EN-US"}[字段，因此用目的端口号的高]{style="font-family:宋体"}[8]{lang="EN-US"}[位为]{style="font-family:宋体"}[Type]{lang="EN-US"}[字段、低]{style="font-family:宋体"}[8]{lang="EN-US"}[位为]{style="font-family:宋体"}[Code]{lang="EN-US"}[字段，源端口号为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[DstMAC(VLAN)          SrcMAC(VLAN)]{lang="EN-US"}]{#struct_0_84792_x5137_1941794876}

[[当前流缓存区中活跃流的二层信息：目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_84792_x5137_419328272}[地址、目的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、源]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[TopLblType(IP/Mask)      Lbl-Exp-S-List]{lang="EN-US"}]{#struct_0_84792_x5137_1015175864}

[[当前流缓存区中活跃流的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_84792_x5137_1942384700}[信息：栈顶标签的类型（栈顶标签对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及掩码长度）、标签列表]{style="font-family:宋体"}

[[标签列表中至多列出三层标签]{style="font-family:宋体"}]{#struct_0_84792_x5137_x908627571}

[[TCPFlag:]{lang="EN-US"}]{#struct_0_84792_x5137_x1978249354}

[[DstMask:      SrcMask:             NextHop:]{lang="EN-US"}]{#struct_0_84792_x5137_1044511214}

[[DstAS:           SrcAS:            BGPNextHop:]{lang="EN-US"}]{#struct_0_84792_x5137_1942450236}

[[OutVRF:       InVRF:]{lang="EN-US"}]{#struct_0_84792_x5137_x178961581}

[[SamplerMode:                     SamplerInt:]{lang="EN-US"}]{#struct_0_84792_x5137_x55996847}

[[Active:       Bytes/Pkt:]{lang="EN-US"}]{#struct_0_84792_x5137_x787022940}

[[当前流缓存区中活跃流的其他信息：]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_84792_x5137_981686987}[标记、目的掩码、源掩码、路由下一跳、目的自治系统、源自治系统、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳、出方向报文所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[、入方向报文所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[、采样模式、采样间隔、流活跃时间、平均每个包的字节数]{style="font-family:宋体"}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x1854516233}[采样模式，目前支持三种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_84792_x5137_x2092296894}[：表示不采样，统计所有报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_84792_x5137_x786957404}[：表示固定采样]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_84792_x5137_x1772641505}[：表示随机采样]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1586400033 .myid}
[]{#_Toc404797264}[]{#struct_0_84792_x5137_232881953}[]{#_Toc250995601}

**NetStream \-- NetStream配置命令 \-- display ip netstream export**

------------------------------------------------------------------------

[**[display ip netstream export]{lang="EN-US"}**]{#struct_0_84792_x5137_579944397}[命令用来查看]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[统计输出报文的各种信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x786891868}

[**[display ip netstream export]{lang="EN-US"}**]{#struct_0_84792_x5137_x910902778}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1073539527}

[[任意视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_593042159}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x385576969}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_267988483}

[[network-operator]{lang="EN-US"}]{#struct_0_84792_x5137_1208285574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1265276108}

[[mdc-operator]{lang="EN-US"}]{#struct_0_84792_x5137_614786403}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x786826332}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_84792_x5137_1758473894}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1422539068}[查看]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip netstream export]{lang="EN-US"}]{#struct_0_84792_x5137_x787285084}

[IP export information:]{lang="EN-US"}

[  Flow source interface                            : GigabitEthernet1/0/1]{lang="EN-US"}

[  Flow destination VPN instance                    : VPN1]{lang="EN-US"}

[  Flow destination IP address (UDP)                : 10.10.0.10 (30000)]{lang="EN-US"}

[  Version 5 exported flows number                  : 16]{lang="EN-US"}

[  Version 5 exported UDP datagrams number (failed) : 16 (0)]{lang="EN-US"}

[  Version 9 exported flows number                  : 20]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed) : 2 (0)]{lang="EN-US"}

[ ]{lang="EN-US"}

[MPLS export information:]{lang="EN-US"}

[  Flow source interface                            : GigabitEthernet1/0/1]{lang="EN-US"}

[  Flow destination VPN instance                    : VPN1]{lang="EN-US"}

[  Flow destination IP address (UDP)                : 10.10.0.10 (30000)]{lang="EN-US"}

[  Version 9 exported flows number                  : 20]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed) : 2 (0)]{lang="EN-US"}

[ ]{lang="EN-US"}

[as aggregation export information:]{lang="EN-US"}

[  Flow source interface                            : GigabitEthernet1/0/1]{lang="EN-US"}

[  Flow destination VPN instance                    : VPN1]{lang="EN-US"}

[  Flow destination IP address (UDP)                : 10.10.0.10 (30000)]{lang="EN-US"}

[  Version 8 exported flows number                  : 16]{lang="EN-US"}

[  Version 8 exported UDP datagrams number (failed) : 2 (0)]{lang="EN-US"}

[  Version 9 exported flows number                  : 16]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed) : 2 (0)]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ip netstream export]{lang="EN-US"}]{#struct_0_84792_x5137_x560297146}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x487773721}[]{#struct_0_84792_x5137_x1943383846}[]{#_Toc157417828}[]{#_Toc157417866}[]{#_Toc158434518}[字段]{style="font-family:
   黑体"}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_84792_x5137_631450115}

[[IP export information]{lang="EN-US"}]{#struct_0_84792_x5137_548172347}

[[版本]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_84792_x5137_x993725831}[和版本]{style="font-family:宋体"}[9]{lang="EN-US"}[统计输出信息]{style="font-family:宋体"}

[[Flow source interface]{lang="EN-US"}]{#struct_0_84792_x5137_x787219548}

[[输出信息的源接口]{style="font-family:宋体"}]{#struct_0_84792_x5137_x2073357306}

[[Flow destination VPN instance]{lang="EN-US"}]{#struct_0_84792_x5137_x1085781331}

[[输出信息的目的地址所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_84792_x5137_x1086690896}

[[Flow destination IP address (UDP)]{lang="EN-US"}]{#struct_0_84792_x5137_1002459598}

[[输出信息的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_84792_x5137_75250912}[地址（]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号）]{style="font-family:宋体"}

[[Version 5 exported flows number]{lang="EN-US"}]{#struct_0_84792_x5137_x1110009864}

[[使用版本]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_84792_x5137_x787154012}[格式发送的流信息数]{style="font-family:宋体"}

[[Version 5 exported UDP datagrams number (failed)]{lang="EN-US"}]{#struct_0_84792_x5137_975705809}

[[使用版本]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_84792_x5137_1485498233}[格式发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数（发送失败的报文数）]{style="font-family:宋体"}

[[Version 9 exported flows number]{lang="EN-US"}]{#struct_0_84792_x5137_x1245130217}

[[使用版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_84792_x5137_1402489258}[格式发送的流信息数]{style="font-family:宋体"}

[[Version 9 exported UDP datagrams number (failed)]{lang="EN-US"}]{#struct_0_84792_x5137_x787088476}

[[使用版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_84792_x5137_1854381868}[格式发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数（发送失败的报文数）]{style="font-family:宋体"}

[[MPLS export information]{lang="EN-US"}]{#struct_0_84792_x5137_1278390423}

[[版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_84792_x5137_386151724}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流统计输出信息]{style="font-family:宋体"}

[[根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"自治系统"聚合方式为例]{style="font-family:宋体"}]{#struct_0_84792_x5137_x2097972248}

[[as aggregation export information]{lang="EN-US"}]{#struct_0_84792_x5137_x786498652}

[[启用自治系统聚合的版本]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_84792_x5137_x1319264234}[统计输出信息]{style="font-family:宋体"}

[[Version 8 exported flows number]{lang="EN-US"}]{#struct_0_84792_x5137_1867502565}

[[使用版本]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_84792_x5137_x1249952679}[格式发送的流信息数]{style="font-family:宋体"}

[[Version 8 exported UDP datagrams number (failed)]{lang="EN-US"}]{#struct_0_84792_x5137_1693767146}

[[使用版本]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_84792_x5137_x786433116}[格式发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数（发送失败的报文数）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_84792_x5137_1773588559}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1588031610}[查看]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip netstream export]{lang="EN-US"}]{#struct_0_84792_x5137_x787022939}

[IP export information:]{lang="EN-US"}

[  Flow source interface                           : Vlan-interface2]{lang="EN-US"}

[  Flow destination VPN instance                   : Not specified]{lang="EN-US"}

[  Flow destination IP address (UDP)               : 192.168.0.5 (5000)]{lang="EN-US"}

[  Version 5 exported flows number                 : 27]{lang="EN-US"}

[  Version 5 exported UDP datagrams number (failed): 21 (0)]{lang="EN-US"}

[  Version 9 exported flows number                 : 0]{lang="EN-US"}

[  Version 9 exported UDP datagram number (failed) : 0 (0)]{lang="EN-US"}

[ ]{lang="EN-US"}

[L2 export information:]{lang="EN-US"}

[  Flow source interface                           : Vlan-interface2]{lang="EN-US"}

[  Flow destination VPN instance                   : Not specified]{lang="EN-US"}

[  Flow destination IP address (UDP)               : 192.168.0.5 (5000)]{lang="EN-US"}

[  Version 9 exported flows number                 : 0]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed): 0 (0)]{lang="EN-US"}

[ ]{lang="EN-US"}

[protocol-port aggregation export information:]{lang="FR"}

[  ]{lang="FR"}[Flow source interface                           : Vlan-interface2]{lang="EN-US"}

[  Flow destination VPN instance                   : Not specified]{lang="EN-US"}

[  Flow destination IP address (UDP)               : 192.168.0.5 (5000)]{lang="EN-US"}

[  Version 8 exported flows number                 : 24]{lang="EN-US"}

[  Version 8 exported UDP datagrams number (failed): 21 (0)]{lang="EN-US"}

[  Version 9 exported flows number                 : 0]{lang="EN-US"}

[  Version 9 exported UDP datagrams number (failed): 0 (0)]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ip netstream export]{lang="EN-US"}]{#struct_0_84792_x5137_982276818}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x491273049}[[字段]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1674447257}

[[描述]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1018738277}

[[IP export information]{lang="EN-US"}]{#struct_0_84792_x5137_1043548483}

[[版本]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_84792_x5137_1053747219}[和版本]{style="font-family:宋体"}[9]{lang="EN-US"}[统计输出信息]{style="font-family:宋体"}

[[Flow source interface]{lang="EN-US"}]{#struct_0_84792_x5137_x786957403}

[[输出信息的源接口]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1772575969}

[[Flow destination VPN instance]{lang="EN-US"}]{#struct_0_84792_x5137_1255021562}

[[输出信息的目的地址所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_84792_x5137_1366995068}

[[Flow destination IP address (UDP)]{lang="EN-US"}]{#struct_0_84792_x5137_x204170834}

[[输出信息的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_84792_x5137_x1688080162}[地址（]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号）]{style="font-family:宋体"}

[[Version 5 exported flows number]{lang="EN-US"}]{#struct_0_84792_x5137_x786891867}

[[使用版本]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_84792_x5137_x910312954}[格式发送的流信息数]{style="font-family:宋体"}

[[Version 5 exported UDP datagram number (failed)]{lang="EN-US"}]{#struct_0_84792_x5137_692971787}

[[使用版本]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_84792_x5137_444768438}[格式发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数（发送失败的报文数）]{style="font-family:宋体"}

[[Version 9 exported flows number]{lang="EN-US"}]{#struct_0_84792_x5137_x580297435}

[[使用版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_84792_x5137_323658263}[格式发送的流信息数]{style="font-family:宋体"}

[[Version 9 exported UDP datagram number (failed)]{lang="EN-US"}]{#struct_0_84792_x5137_x786826331}

[[使用版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_84792_x5137_1758670502}[格式发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数（发送失败的报文数）]{style="font-family:宋体"}

[[L2 export information]{lang="EN-US"}]{#struct_0_84792_x5137_x1780800306}

[[二层流统计输出信息]{style="font-family:宋体"}]{#struct_0_84792_x5137_x363140809}

[[根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"协议－端口"聚合方式为例]{style="font-family:宋体"}]{#struct_0_84792_x5137_2080645313}

[[protocol-port aggregation export information]{lang="EN-US"}]{#struct_0_84792_x5137_x787285083}

[[启用协议－端口聚合的版本]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_84792_x5137_x559838394}[统计输出信息]{style="font-family:宋体"}

[[Version 8 exported flows number]{lang="EN-US"}]{#struct_0_84792_x5137_281647085}

[[使用版本]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_84792_x5137_520288549}[格式发送的流信息数]{style="font-family:宋体"}

[[Version 8 exported UDP datagram number (failed)]{lang="EN-US"}]{#struct_0_84792_x5137_x446015364}

[[使用版本]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_84792_x5137_x787219547}[格式发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文数（发送失败的报文数）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-730756559 .myid}
[]{#_Toc404797265}[]{#struct_0_84792_x5137_x2073816058}[]{#_Toc250995602}

**NetStream \-- NetStream配置命令 \-- display ip netstream template**

------------------------------------------------------------------------

[**[display ip netstream template]{lang="EN-US"}**]{#struct_0_84792_x5137_x1480989088}[命令用来查看]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[模板的配置和状态信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x558736917}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_84792_x5137_1477129992}

[**[display ip netstream template]{lang="EN-US"}**]{#struct_0_84792_x5137_1609767790}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_84792_x5137_x1899527840}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip netstream template]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ *cpu cpu-number* \] \]]{lang="EN-US"}]{#struct_0_84792_x5137_2057178546}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_84792_x5137_x981287677}[模式：]{style="font-family:宋体"}

[**[display ip netstream template]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ *cpu cpu-number* \] \]]{lang="EN-US"}]{#struct_0_84792_x5137_x787154011}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_975771345}

[[任意视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_776529153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_456044193}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1656009704}

[[network-operator]{lang="EN-US"}]{#struct_0_84792_x5137_1681741133}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1531450456}

[[mdc-operator]{lang="EN-US"}]{#struct_0_84792_x5137_979753398}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x448522152}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_84792_x5137_x787088475}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_1854316332}[：显示指定成员设备的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示成员设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主用设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_1114816402}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示成员设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示主用设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number slot* *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_x300717675}[：显示指定成员设备上指定单板的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number slot* *slot-number*]{lang="EN-US"}]{#struct_0_84792_x5137_1114750866}[：显示指定单板的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示主用设备主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_84792_x5137_267552925}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1840009045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_84792_x5137_x1824301747}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1496793233}[使能自治系统聚合。查看]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[模板信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip netstream template]{lang="EN-US"}]{#struct_0_84792_x5137_x786433115}

[ Flow template refresh frequency            : 20]{lang="EN-US"}

[ Flow template refresh interval             : 30 min]{lang="EN-US"}

[ Active flow templates                      : 2]{lang="EN-US"}

[ Created flow templates                     : 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[AS outbound template:]{lang="EN-US"}

[ Template ID                : 3258]{lang="EN-US"}

[ Packets                    : 0]{lang="EN-US"}

[ Last template export time  : Never]{lang="EN-US"}

[ Field count                : 14]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Flows                        4]{lang="EN-US"}

[ Out packets                  8]{lang="EN-US"}

[ Out bytes                    8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Source AS                    4]{lang="EN-US"}

[ Destination AS               4]{lang="EN-US"}

[ Input interface index        4]{lang="EN-US"}

[ Output interface index       4]{lang="EN-US"}

[ Direction                    1]{lang="EN-US"}

[ Sampling algorithm           1]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ Sampling interval            4]{lang="EN-US"}

[ ]{lang="EN-US"}

[AS inbound template:]{lang="EN-US"}

[ Template ID                : 3257]{lang="EN-US"}

[ Packets                    : 0]{lang="EN-US"}

[ Last template export time  : Never]{lang="EN-US"}

[ Field count                : 14]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Flows                        4]{lang="EN-US"}

[ In packets                   8]{lang="EN-US"}

[ In bytes                     8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Source AS                    4]{lang="EN-US"}

[ Destination AS               4]{lang="EN-US"}

[ Input interface index        4]{lang="EN-US"}

[ Output interface index       4]{lang="EN-US"}

[ Direction                    1]{lang="EN-US"}

[ Sampling algorithm           1]{lang="EN-US"}

[ PAD                          1]{lang="EN-US"}

[ Sampling interval            4]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ip netstream template]{lang="EN-US"}]{#struct_0_84792_x5137_1773391951}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x498765369}[[字段]{style="font-family:黑体"}]{#struct_0_84792_x5137_x787022942}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_84792_x5137_981555915}

[[Flow template refresh frequency]{lang="EN-US"}]{#struct_0_84792_x5137_x2141105436}

[[模板的包刷新率]{style="font-family:宋体"}]{#struct_0_84792_x5137_395766533}

[[Flow template refresh interval]{lang="EN-US"}]{#struct_0_84792_x5137_x1414801973}

[[模板的时间刷新率，单位为分钟]{style="font-family:宋体"}]{#struct_0_84792_x5137_1113534625}

[[Active flow templates]{lang="EN-US"}]{#struct_0_84792_x5137_x786957406}

[[当前激活的模板数]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1772772577}

[[Created flow templates]{lang="EN-US"}]{#struct_0_84792_x5137_1663918172}

[[创建的模板总数]{style="font-family:宋体"}]{#struct_0_84792_x5137_829074897}

[[根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"自治系统"聚合方式为例]{style="font-family:宋体"}]{#struct_0_84792_x5137_x683684524}

[[AS outbound template]{lang="EN-US"}]{#struct_0_84792_x5137_x934865003}

[[AS]{lang="EN-US"}]{#struct_0_84792_x5137_x786891870}[出方向模板信息]{style="font-family:宋体"}

[[AS inbound template]{lang="EN-US"}]{#struct_0_84792_x5137_x910378489}

[[AS]{lang="EN-US"}]{#struct_0_84792_x5137_634943260}[入方向模板信息]{style="font-family:宋体"}

[[Template ID]{lang="EN-US"}]{#struct_0_84792_x5137_x831964009}

[[模板]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_84792_x5137_x581431156}

[[Packets]{lang="EN-US"}]{#struct_0_84792_x5137_x786826334}

[[使用该模板的发送报文数]{style="font-family:宋体"}]{#struct_0_84792_x5137_1758867110}

[[Last template export time]{lang="EN-US"}]{#struct_0_84792_x5137_1354363852}

[[该模板最近的一次输出时间]{style="font-family:宋体"}]{#struct_0_84792_x5137_x744962208}

[[Field count]{lang="EN-US"}]{#struct_0_84792_x5137_1517496444}

[[模板的域总数]{style="font-family:宋体"}]{#struct_0_84792_x5137_x787285086}

[[Field type]{lang="EN-US"}]{#struct_0_84792_x5137_x560166074}

[[域类型]{style="font-family:宋体"}]{#struct_0_84792_x5137_1613421663}

[[Field length (bytes)]{lang="EN-US"}]{#struct_0_84792_x5137_x960327677}

[[域长度，单位为字节]{style="font-family:宋体"}]{#struct_0_84792_x5137_x327200473}

[[Flows]{lang="EN-US"}]{#struct_0_84792_x5137_x787219550}

[[聚合流数量]{style="font-family:宋体"}]{#struct_0_84792_x5137_x2073881593}

[[Out packets]{lang="EN-US"}]{#struct_0_84792_x5137_x483336689}

[[输出的数据包个数]{style="font-family:宋体"}]{#struct_0_84792_x5137_19475911}

[[In packets]{lang="EN-US"}]{#struct_0_84792_x5137_x787154014}

[[输入的数据包个数]{style="font-family:宋体"}]{#struct_0_84792_x5137_975574737}

[[Out bytes]{lang="EN-US"}]{#struct_0_84792_x5137_1279988371}

[[输出的数据个数，单位为字节]{style="font-family:宋体"}]{#struct_0_84792_x5137_x375681269}

[[In bytes]{lang="EN-US"}]{#struct_0_84792_x5137_x787088478}

[[输入的数据个数，单位为字节]{style="font-family:宋体"}]{#struct_0_84792_x5137_1853988652}

[[First forwarded]{lang="EN-US"}]{#struct_0_84792_x5137_x1798125369}

[[记录转发第一个报文时的系统时间，时间精确到毫秒]{style="font-family:宋体"}]{#struct_0_84792_x5137_x621759602}

[[Last forwarded]{lang="EN-US"}]{#struct_0_84792_x5137_x2057692435}

[[记录转发最后一个报文时的系统时间，时间精确到毫秒]{style="font-family:宋体"}]{#struct_0_84792_x5137_x786498654}

[[Source AS]{lang="EN-US"}]{#struct_0_84792_x5137_x1318871018}

[[源]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_84792_x5137_x1473025521}[号]{style="font-family:宋体"}

[[Destination AS]{lang="EN-US"}]{#struct_0_84792_x5137_x786433118}

[[目的]{style="font-family:宋体"}[AS ]{lang="EN-US"}]{#struct_0_84792_x5137_1773719631}

[[Input interface index]{lang="EN-US"}]{#struct_0_84792_x5137_1911102255}

[[输入接口的索引]{style="font-family:宋体"}]{#struct_0_84792_x5137_1048058837}

[[Output interface index]{lang="EN-US"}]{#struct_0_84792_x5137_x787022941}

[[输出接口的索引]{style="font-family:宋体"}]{#struct_0_84792_x5137_981752523}

[[Direction]{lang="EN-US"}]{#struct_0_84792_x5137_2054520954}

[[方向字段]{style="font-family:宋体"}]{#struct_0_84792_x5137_x786957405}

[[Sampling algorithm]{lang="EN-US"}]{#struct_0_84792_x5137_x1772707041}

[[采样算法]{style="font-family:宋体"}]{#struct_0_84792_x5137_x711142738}

[[PAD]{lang="EN-US"}]{#struct_0_84792_x5137_x786891869}

[[空白占位符]{style="font-family:宋体"}]{#struct_0_84792_x5137_x910968314}

[[Sampling interval]{lang="EN-US"}]{#struct_0_84792_x5137_x942311461}

[[采样率]{style="font-family:宋体"}]{#struct_0_84792_x5137_1409516942}

[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_84792_x5137_x786826333}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_1758539430}[使能协议－端口聚合。查看]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[模板信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip netstream template]{lang="EN-US"}]{#struct_0_84792_x5137_x787219549}

[ Flow template refresh frequency            : 20]{lang="EN-US"}

[ Flow template refresh interval             : 30 min]{lang="EN-US"}

[ Active flow templates                      : 8]{lang="EN-US"}

[ Created flow templates                     : 8]{lang="EN-US"}

[ ]{lang="EN-US"}

[Protocol port outbound template:]{lang="EN-US"}

[ Template ID                : 3272]{lang="EN-US"}

[ Field count                : 16]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Flows                        4]{lang="EN-US"}

[ Out packets                  8]{lang="EN-US"}

[ Out bytes                    8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Protocol                     1]{lang="EN-US"}

[ ]{lang="EN-US"}[Direction                    1]{lang="FR"}

[ PAD                          1]{lang="FR"}

[ PAD                          1]{lang="FR"}

[ L4 source port               2]{lang="FR"}

[ L4 destination port          2]{lang="FR"}

[ Sampling algorithm           1]{lang="FR"}

[ ]{lang="FR"}[PAD                          1]{lang="SV"}

[ Sampling interval            4]{lang="SV"}

[ ]{lang="SV"}

[Protocol-port inbound template:]{lang="EN-US"}

[ Template ID                : 3271]{lang="EN-US"}

[ Field count                : 16]{lang="EN-US"}

[ Field type                   Field length (bytes)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Flows                        4]{lang="EN-US"}

[ In packets                   8]{lang="EN-US"}

[ In bytes                     8]{lang="EN-US"}

[ First forwarded              4]{lang="EN-US"}

[ Last forwarded               4]{lang="EN-US"}

[ Protocol                     1]{lang="EN-US"}

[ ]{lang="EN-US"}[Direction                    1]{lang="FR"}

[ PAD                          1]{lang="FR"}

[ L4 source port               2]{lang="FR"}

[ L4 destination port          2]{lang="FR"}

[ Sampling algorithm           1]{lang="FR"}

[ ]{lang="FR"}[PAD                          1]{lang="EN-US"}

[ Sampling interval            4]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ip netstream template]{lang="EN-US"}]{#struct_0_84792_x5137_x2073422842}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x499612441}[[字段]{style="font-family:黑体"}]{#struct_0_84792_x5137_666823701}

[[描述]{style="font-family:黑体"}]{#struct_0_84792_x5137_1506436672}

[[Flow template refresh frequency]{lang="EN-US"}]{#struct_0_84792_x5137_2070285466}

[[模板的包刷新率]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1273592305}

[[Flow template refresh interval]{lang="EN-US"}]{#struct_0_84792_x5137_x1827054966}

[[模板的时间刷新率，单位为分钟]{style="font-family:宋体"}]{#struct_0_84792_x5137_x787154013}

[[Active flow templates]{lang="EN-US"}]{#struct_0_84792_x5137_975640273}

[[当前活跃的模板数]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1616029439}

[[Created flow templates]{lang="EN-US"}]{#struct_0_84792_x5137_x326450818}

[[创建的模板总数]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1904541353}

[[根据不同的聚合方式，下面的显示信息会有差异，请以实际配置的聚合方式为准，这里以"协议－端口聚合"聚合方式为例]{style="font-family:宋体"}]{#struct_0_84792_x5137_1792097736}

[[Protocol-port outbound template]{lang="EN-US"}]{#struct_0_84792_x5137_x787088477}

[[协议－端口聚合出方向模板信息]{style="font-family:宋体"}]{#struct_0_84792_x5137_1854447404}

[[Protocol-port inbound template]{lang="EN-US"}]{#struct_0_84792_x5137_60421200}

[[协议－端口聚合入方向模板信息]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1244908749}

[[Template ID]{lang="EN-US"}]{#struct_0_84792_x5137_x1939087989}

[[模板]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_84792_x5137_x1795883041}

[[Field count]{lang="EN-US"}]{#struct_0_84792_x5137_x786498653}

[[模板的域总数]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1319329770}

[[Field type]{lang="EN-US"}]{#struct_0_84792_x5137_x3553734}

[[域类型]{style="font-family:宋体"}]{#struct_0_84792_x5137_x2026654214}

[[Field length (bytes)]{lang="EN-US"}]{#struct_0_84792_x5137_638697446}

[[域长度，单位为字节]{style="font-family:宋体"}]{#struct_0_84792_x5137_x786433117}

[[Flows]{lang="EN-US"}]{#struct_0_84792_x5137_1773523023}

[[聚合流数量]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1245140736}

[[Out packets]{lang="EN-US"}]{#struct_0_84792_x5137_1106998903}

[[输出的数据包大小]{style="font-family:宋体"}]{#struct_0_84792_x5137_x787022944}

[[In packets]{lang="EN-US"}]{#struct_0_84792_x5137_981949131}

[[输入的数据包大小]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1223184979}

[[Out bytes]{lang="EN-US"}]{#struct_0_84792_x5137_x250883242}

[[输出的数据大小，单位为字节]{style="font-family:宋体"}]{#struct_0_84792_x5137_54891832}

[[In bytes]{lang="EN-US"}]{#struct_0_84792_x5137_x786957408}

[[输入的数据大小，单位为字节]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1772903649}

[[First forwarded]{lang="EN-US"}]{#struct_0_84792_x5137_x1615385136}

[[记录转发第一个报文时的系统时间，时间精确到毫秒]{style="font-family:宋体"}]{#struct_0_84792_x5137_500397045}

[[Last forwarded]{lang="EN-US"}]{#struct_0_84792_x5137_x786891872}

[[记录转发最后一个报文时的系统时间，时间精确到毫秒]{style="font-family:宋体"}]{#struct_0_84792_x5137_x910509561}

[[Protocol]{lang="EN-US"}]{#struct_0_84792_x5137_245564093}

[[协议]{style="font-family:宋体"}]{#struct_0_84792_x5137_x786826336}

[[Direction]{lang="EN-US"}]{#struct_0_84792_x5137_1758736038}

[[方向]{style="font-family:宋体"}]{#struct_0_84792_x5137_1753704714}

[[L4 source port]{lang="EN-US"}]{#struct_0_84792_x5137_620450370}

[[TCP/UDP]{lang="EN-US"}]{#struct_0_84792_x5137_x787285088}[的源端口号]{style="font-family:宋体"}

[[L4 destination port]{lang="EN-US"}]{#struct_0_84792_x5137_x560559290}

[[TCP/UDP]{lang="EN-US"}]{#struct_0_84792_x5137_104919278}[的目的端口号]{style="font-family:宋体"}

[[Sampling algorithm]{lang="EN-US"}]{#struct_0_84792_x5137_1468226169}

[[采样算法]{style="font-family:宋体"}]{#struct_0_84792_x5137_x787219552}

[[PAD]{lang="EN-US"}]{#struct_0_84792_x5137_x2074012665}

[[空白占位符]{style="font-family:宋体"}]{#struct_0_84792_x5137_1180170984}

[[Sampling interval]{lang="EN-US"}]{#struct_0_84792_x5137_x787154016}

[[采样率]{style="font-family:宋体"}]{#struct_0_84792_x5137_975443665}

[ ]{lang="EN-US"}

::: {#-366434638 .myid}
[]{#_Toc404797266}[]{#struct_0_84792_x5137_1270711951}[]{#_Toc250995603}[]{#_Toc157337215}[]{#_Toc157413423}[]{#_Toc157417829}[]{#_Toc157417867}[]{#_Toc158434519}

**NetStream \-- NetStream配置命令 \-- enable**

------------------------------------------------------------------------

[**[enable]{lang="EN-US"}**]{#struct_0_84792_x5137_2142224400}[命令用来开启当前聚合视图对应的聚合功能。]{style="font-family:宋体"}

[**[undo enable]{lang="EN-US"}**]{#struct_0_84792_x5137_156918951}[命令用来关闭当前聚合视图对应的聚合功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x453368978}[]{#_Toc157337216}[]{#_Toc157413424}[]{#_Toc157417830}[]{#_Toc157417868}[]{#_Toc158434520}

[**[enable]{lang="EN-US"}**]{#struct_0_84792_x5137_x787088480}[]{#_Toc157337217}[]{#_Toc157413425}[]{#_Toc157417831}[]{#_Toc157417869}[]{#_Toc158434521}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[enable]{lang="EN-US"}**]{#struct_0_84792_x5137_1854512933}[]{#_Toc157337218}[]{#_Toc157413426}[]{#_Toc157417832}[]{#_Toc157417870}[]{#_Toc158434522}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_877935415}

[[未开启任何]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_1431970145}[聚合功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x786498656}[]{#_Toc157337219}[]{#_Toc157413427}[]{#_Toc157417833}[]{#_Toc157417871}[]{#_Toc158434523}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x1319002090}[聚合视图]{style="font-family:宋体"}[]{#_Toc157337220}[]{#_Toc157413428}[]{#_Toc157417834}[]{#_Toc157417872}[]{#_Toc158434524}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1192511927}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1976866953}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x845378581}[]{#_Toc157337221}[]{#_Toc157413429}[]{#_Toc157417835}[]{#_Toc157417873}[]{#_Toc158434525}[]{#_Toc157337222}[]{#_Toc157413430}[]{#_Toc157417836}[]{#_Toc157417874}[]{#_Toc158434526}

[]{#struct_0_84792_x5137_x517294643}[]{#_Toc157337229}[]{#_Toc157413437}[]{#_Toc157417843}[]{#_Toc157417881}[]{#_Toc158434533}[【举例】]{style="font-family:
黑体"}[]{#_Toc157337230}[]{#_Toc157413438}[]{#_Toc157417844}[]{#_Toc157417882}[]{#_Toc158434534}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1287281566}[开启]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[的自治系统聚合功能。]{style="font-family:宋体"}[]{#_Toc157337231}[]{#_Toc157413439}[]{#_Toc157417845}[]{#_Toc157417883}[]{#_Toc158434535}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x786433120}[]{#_Toc157337232}[]{#_Toc157413440}[]{#_Toc157417846}[]{#_Toc157417884}[]{#_Toc158434536}

[\[Sysname\] ip netstream aggregation as[]{#_Toc157337233}[]{#_Toc157413441}[]{#_Toc157417847}[]{#_Toc157417885}[]{#_Toc158434537}]{lang="EN-US"}

[\[Sysname-ns-aggregation-as\] enable]{lang="EN-US"}[]{#_Toc157337234}[]{#_Toc157413442}[]{#_Toc157417848}[]{#_Toc157417886}[]{#_Toc158434538}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1773195344}

[]{#_Toc250995605}[]{#_Toc55050573}[]{#_Toc28576979}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream aggregation]{lang="EN-US"}**]{#struct_0_84792_x5137_1507234492}
:::

::::::: {#1941388863 .myid}
[]{#_Toc404797267}[]{#struct_0_84792_x5137_2105407120}

**NetStream \-- NetStream配置命令 \-- ip netstream**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_84792_x5137_2117367232}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的视图支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_84792_x5137_183463069}
:::

**[ ]{lang="EN-US"}**

[**[ip netstream]{lang="EN-US"}**]{#struct_0_84792_x5137_1890522336}[命令用来在全局或当前接口开启]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ip netstream]{lang="EN-US"}**]{#struct_0_84792_x5137_302804691}[命令用来在全局或当前接口关闭]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1027915225}

[[系统视图：]{style="font-family:宋体"}]{#struct_0_84792_x5137_x787022943}

[**[ip netstream]{lang="EN-US"}**]{#struct_0_84792_x5137_981621451}

[**[undo ip netstream]{lang="EN-US"}**]{#struct_0_84792_x5137_x1098386086}

[[接口视图：]{style="font-family:宋体"}]{#struct_0_84792_x5137_991819193}

[**[ip netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_84792_x5137_x691949966}

[**[undo ip netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_84792_x5137_1019415828}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x786957407}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_84792_x5137_x1772838113}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_84792_x5137_1716089069}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_84792_x5137_x1431947929}
:::

[ ]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x17104536}

[[全局和接口]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x1885642902}[功能处于关闭状态。]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_722703079}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1429477985}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1831583433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x558003950}

[**[inbound]{lang="EN-US"}**]{#struct_0_84792_x5137_1076335568}[：对入方向的流量进行]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_84792_x5137_x786891871}[：对出方向的流量进行]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x910444025}

[[全局开启]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x931945205}[功能后，将开启所有接口入方向及出方向的]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1161927665}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_1716154605}[全局开启]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_88266609}

[\[Sysname\] ip netstream]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_725910244}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的入方向上开启]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_305930802}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip netstream inbound]{lang="EN-US"}
:::::::

::::: {#-1190816823 .myid}
[]{#_Toc404797268}[]{#struct_0_84792_x5137_x1050454280}[]{#_Toc250995614}[]{#_Toc142468160}[]{#_Toc143941786}[]{#_Toc144007555}[]{#_Toc142468163}[]{#_Toc143941789}[]{#_Toc144007558}

**NetStream \-- NetStream配置命令 \-- ip netstream { inbound \| outbound } filter**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_84792_x5137_249323763}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_84792_x5137_x1404977020}
:::

**[ ]{lang="EN-US"}**

[**[ip netstream filter]{lang="EN-US"}**]{#struct_0_84792_x5137_x1927955752}[命令用来配置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[过滤功能，根据指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则对报文进行过滤。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip netstream filter**]{lang="EN-US"}]{#struct_0_84792_x5137_x545624833}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_158744354}

[**[ip netstream ]{lang="EN-US"}**[{ **inbound** \| **outbound** } **filter acl** *acl-number*]{lang="EN-US"}]{#struct_0_84792_x5137_1569129038}

[**[undo ip netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **filter**]{lang="EN-US"}]{#struct_0_84792_x5137_x1620761744}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_779650826}

[[未配置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x793929275}[过滤功能，此时统计所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_255069459}

[[接口视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1075624356}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1453123102}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1499723398}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_2059555141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x729493072}

[**[inbound]{lang="EN-US"}**]{#struct_0_84792_x5137_779060999}[：入方向过滤，即对从当前接口收到的报文进行过滤统计。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_84792_x5137_395781254}[：出方向过滤，即对从当前接口发出的报文进行过滤统计。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_84792_x5137_530570998}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号，基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[，高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_2096706029}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_983315781}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置根据]{style="font-family:宋体"}[ACL 2003]{lang="EN-US"}[规则进行出方向过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_894031156}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip netstream outbound]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip netstream outbound filter acl 2003]{lang="EN-US"}
:::::

::::: {#396119178 .myid}
[]{#_Toc404797269}

**NetStream \-- NetStream配置命令 \-- ip netstream { inbound \| outbound } mirror-to**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[![](NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

**[ip]{lang="EN-US"}**[ **netstream** { **inbound** \| **outbound** } **mirror**-**to**]{lang="EN-US"}[命令用来将端口流量镜像到业务板。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

**[ip]{lang="EN-US"}**[ **netstream** { **inbound** \| **outbound** } **mirror**-**to**]{lang="EN-US"}[命令用来将端口流量镜像到业务设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

**[undo ip netstream ]{lang="EN-US"}**[{ **inbound** \| **outbound** } **mirror-to**]{lang="EN-US"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[【命令】]{style="font-family:黑体"}

[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

**[ip netstream ]{lang="EN-US"}**[{ inbound \| outbound } **mirror-to service slot** *slot-number* \[ **backup slot** *slot-number* \]]{lang="EN-US"}

**[undo ip netstream ]{lang="EN-US"}**[{ inbound \| outbound } **mirror-to**]{lang="EN-US"}

[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

**[ip netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **mirror-to service chassis** *chassis-number* **slot** *slot-number* \[ **backup chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}

**[undo ip netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **mirror-to**]{lang="EN-US"}

[【缺省情况】]{style="font-family:黑体"}

[不对端口流量进行镜像。]{style="font-family:宋体"}

[【视图】]{style="font-family:黑体"}

[接口视图]{style="font-family:宋体"}

[【缺省用户角色】]{style="font-family:黑体"}

[network-admin]{lang="EN-US"}

[mdc-admin]{lang="EN-US"}

[【参数】]{style="font-family:黑体"}

**[inbound]{lang="EN-US"}**[：对接口的入方向流量进行镜像。]{style="font-family:宋体"}

**[outbound]{lang="EN-US"}**[：对接口的出方向流量进行镜像。]{style="font-family:宋体"}

**[service slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：指定主用业务板所在的槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示业务板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

**[service slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：指定主用业务设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

**[service chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：指定成员设备上的指定业务板作为主用业务板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示业务板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

**[backup slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：指定备用业务板所在的槽位号。若未指定该参数，表示未配置备用业务板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

**[backup slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}[：指定备用业务设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若未指定该参数，表示未配置备用业务设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

**[backup chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：指定成员设备上的指定业务板作为备用业务板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示业务板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[【使用指导】]{style="font-family:黑体"}

[只有当主用业务板出现故障时，流量才可以被镜像到备用业务板。主用业务板恢复，备用业务板恢复为备份身份，流量镜像到主用业务板。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[只有当主用业务设备出现故障时，流量才可以被镜像到备用业务设备。主用业务设备恢复，备用业务设备恢复为备份身份，流量镜像到主用业务设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[【举例】]{style="font-family:黑体"}

[\# ]{lang="EN-US"}[在接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[上配置入方向流量镜像，将流量镜像到]{style="font-family:宋体"}[3]{lang="EN-US"}[号槽的业务板。]{style="font-family:宋体"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip netstream inbound mirror-to service slot 3]{lang="EN-US"}
:::::

::: {#-121622093 .myid}
[]{#_Toc404797270}[]{#struct_0_84792_x5137_x180318750}[]{#_Toc250995618}

**NetStream \-- NetStream配置命令 \-- ip netstream { inbound \| outbound } sampler**

------------------------------------------------------------------------

[**[ip netstream sampler]{lang="EN-US"}**]{#struct_0_84792_x5137_x1666932810}[命令用来启用]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[采样功能。]{style="font-family:宋体"}

[**[undo ip netstream sampler]{lang="EN-US"}**]{#struct_0_84792_x5137_x1252164021}[命令用来禁用]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[采样功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_391611879}

[**[ip netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **sampler** *sampler-name*]{lang="EN-US"}]{#struct_0_84792_x5137_1395433813}

[**[undo ip netstream]{lang="EN-US"}**[ { **inbound** \| **outbound** } **sampler**]{lang="EN-US"}]{#struct_0_84792_x5137_x1151862185}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_779585287}

[[未启用]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_1288197883}[采样功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_79156508}

[[接口视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_154793116}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_371242831}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x836918785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1328056280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1321710942}

[**[inbound]{lang="EN-US"}**]{#struct_0_84792_x5137_779650823}[：对入方向的报文进行采样。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_84792_x5137_x793929272}[：对出方向的报文进行采样。]{style="font-family:宋体"}

[**[sampler ]{lang="EN-US"}***[sampler-name]{lang="EN-US"}*]{#struct_0_84792_x5137_886801358}[：采样器名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_254610707}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1564676121}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上启用]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[采样功能，使用名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的采样器对入方向的报文进行采样，]{style="font-family:宋体"}[Netstream]{lang="EN-US"}[根据采样结果进行报文统计。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x1114792782}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip netstream inbound]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip netstream inbound sampler abc]{lang="EN-US"}
:::

::::: {#-785124074 .myid}
[]{#_Toc404797271}[]{#struct_0_84792_x5137_x786826335}[]{#_Toc250995606}[]{#_Toc55050574}[]{#_Toc28576980}[]{#_Toc345334432}

**NetStream \-- NetStream配置命令 \-- ip netstream aggregation**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NetStream命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_84792_x5137_1758932646}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令中各参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_84792_x5137_x1362806089}
:::

**[ ]{lang="EN-US"}**

[**[ip netstream aggregation]{lang="EN-US"}**]{#struct_0_84792_x5137_x1462628246}[命令用来设置]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[流聚合方式，并进入相应的]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[聚合视图。]{style="font-family:
宋体"}

[**[undo ip netstream aggregation]{lang="EN-US"}**]{#struct_0_84792_x5137_x2117411934}[命令用来关闭]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[流聚合方式，并删除流聚合方式相应的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_660272051}

[**[ip netstream aggregation]{lang="EN-US"}**[ { **as** \| **destination-prefix** \| **prefix** \| **prefix-port** \| **protocol-port** \| **source-prefix** \| **tos-as** \| **tos-bgp-nexthop** \| **tos-destination-prefix** \| **tos-prefix** \| **tos-protocol-port** \| **tos-source-prefix** }]{lang="EN-US"}]{#struct_0_84792_x5137_869270878}

[**[undo ip netstream aggregation]{lang="EN-US"}**[ { **as** \| **destination-prefix** \| **prefix** \| **prefix-port** \| **protocol-port** \| **source-prefix** \| **tos-as** \| **tos-bgp-nexthop** \| **tos-destination-prefix** \| **tos-prefix** \| **tos-protocol-port** \| **tos-source-prefix** }]{lang="EN-US"}]{#struct_0_84792_x5137_454282578}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1023201169}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_x787285087}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x560100538}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x313188159}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x541362449}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1558652882}

[**[as]{lang="EN-US"}**]{#struct_0_84792_x5137_1469004704}[：自治系统聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的源自治系统号、目的自治系统号、输入接口索引和输出接口索引]{style="font-family:宋体"}[4]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-prefix]{lang="EN-US"}**]{#struct_0_84792_x5137_111879736}[：目的前缀聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的目的自治系统号、目的掩码长度、目的前缀和输出接口索引]{style="font-family:宋体"}[4]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**]{#struct_0_84792_x5137_x1977190043}[：源和目的前缀聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的源自治系统号、目的自治系统号、源掩码长度、目的掩码长度，源前缀、目的前缀、输入接口索引和输出接口索引]{style="font-family:宋体"}[8]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[prefix-port]{lang="EN-US"}**]{#struct_0_84792_x5137_1622194022}[：前缀端口聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的源前缀、目的前缀、源掩码长度、目的掩码长度、]{style="font-family:宋体"}[ToS]{lang="EN-US"}[、协议号、源端口、目的端口、输入接口索引、输出接口索引]{style="font-family:宋体"}[10]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[protocol-port]{lang="EN-US"}**]{#struct_0_84792_x5137_x787219551}[：协议－端口聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的协议号、源端口和目的端口]{style="font-family:宋体"}[3]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-prefix]{lang="EN-US"}**]{#struct_0_84792_x5137_x2073947129}[：源前缀聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的源自治系统号、源掩码长度、源前缀和输入接口索引]{style="font-family:宋体"}[4]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tos-as]{lang="EN-US"}**]{#struct_0_84792_x5137_1688601213}[：服务类型－自治系统聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[、源自治系统号、目的自治系统号、输入接口索引和输出接口索引]{style="font-family:宋体"}[5]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tos-bgp-nexthop]{lang="EN-US"}**]{#struct_0_84792_x5137_1033628619}[：服务类型]{style="font-family:宋体"}[-BGP]{lang="EN-US"}[下一跳聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的服务类型、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、输出接口索引]{style="font-family:宋体"}[3]{lang="EN-US"}[个关键项对流分类。服务类型]{style="font-family:宋体"}[-BGP]{lang="EN-US"}[下一跳聚合只在]{style="font-family:宋体"}[V9]{lang="EN-US"}[模板下生效，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tos-destination-prefix]{lang="EN-US"}**]{#struct_0_84792_x5137_x2033337936}[：服务类型－目的前缀聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[、目的自治系统号、目的掩码长度、目的前缀和输出接口索引]{style="font-family:宋体"}[5]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tos-prefix]{lang="EN-US"}**]{#struct_0_84792_x5137_1732105162}[：服务类型－前缀聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[、源自治系统号、源前缀、源掩码长度、目的自治系统号、目的掩码长度、目的前缀、输入接口索引和输出接口索引]{style="font-family:宋体"}[9]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tos-protocol-port]{lang="EN-US"}**]{#struct_0_84792_x5137_1685245434}[：服务类型－协议－端口聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[、协议号、源端口、目的端口、输入接口索引和输出接口索引]{style="font-family:宋体"}[6]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[tos-source-prefix]{lang="EN-US"}**]{#struct_0_84792_x5137_138264249}[：服务类型－源前缀聚合，根据]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[、源自治系统号、源前缀、源掩码长度和输入接口索引]{style="font-family:宋体"}[5]{lang="EN-US"}[个关键项对流分类，本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x787154015}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在聚合视图下，可以启用或关闭聚合功能，以及设置]{style="font-family:宋体"}]{#struct_0_84792_x5137_x787088479}[NetStream]{lang="EN-US"}[统计输出报文源接口、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址以及目的端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果一条流同时满足多个聚合方式，则该流会被统计到多个聚合流中。]{style="font-family:宋体"}]{#struct_0_84792_x5137_1854054188}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1236161181}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_742170713}[设置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流聚合方式为自治系统聚合，并进入]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[自治系统聚合视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x1104960263}

[\[Sysname\] ip netstream aggregation as]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1008790281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**]{#struct_0_84792_x5137_x377847225}
:::::

::::: {#-1961236626 .myid}
[]{#_Toc404797272}[]{#struct_0_84792_x5137_x786498655}

**NetStream \-- NetStream配置命令 \-- ip netstream aggregation advanced**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NetStream命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_84792_x5137_x1318936554}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_84792_x5137_59357066}
:::

**[ ]{lang="EN-US"}**

[**[ip netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_84792_x5137_1386355627}[命令用来使能硬件流聚合功能。]{style="font-family:宋体"}

[**[undo ip netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_84792_x5137_73514654}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x959328893}

[**[ip netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_84792_x5137_260085513}

[**[undo ip netstream aggregation advanced]{lang="EN-US"}**]{#struct_0_84792_x5137_2132172036}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x786433119}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_1773654095}[硬件流聚合功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1657272519}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1435682070}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1924052440}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1916411162}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1459458052}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1838167712}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能硬件流聚合功能时，系统根据]{style="font-family:宋体"}]{#struct_0_84792_x5137_1047544956}[NetStream]{lang="EN-US"}[统计功能是否配置了统计信息输出的目的地址以及配置的聚合类型来决定是否进行硬件聚合。如果在系统视图下配置了统计信息输出的目的地址或硬件聚合不支持配置的聚合类型，则硬件聚合配置不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能硬件流聚合功能以后，硬件聚合流表项添加到普通流表项记录中，并进行表项的输出。]{style="font-family:宋体"}]{#struct_0_84792_x5137_779061001}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1625539071}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x532251166}[使能硬件流聚合功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x138842801}

[\[Sysname\] ip netstream aggregation advanced]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_56413261}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream aggregation]{lang="EN-US"}**]{#struct_0_84792_x5137_2021488630}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream export host]{lang="EN-US"}**]{#struct_0_84792_x5137_x87176002}
:::::

::: {#1811555797 .myid}
[]{#_Toc404797273}[]{#struct_0_84792_x5137_1181156004}

**NetStream \-- NetStream配置命令 \-- ip netstream export host**

------------------------------------------------------------------------

[**[ip netstream export host]{lang="EN-US"}**]{#struct_0_84792_x5137_779126537}[命令用来配置]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[统计输出报文的目的地址和目的]{style="font-family:
宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:
宋体"}**[undo ip netstream export host]{lang="EN-US"}**[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1083022524}

[**[ip netstream export host]{lang="EN-US"}**[ *ip-address udp-port* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_84792_x5137_319721022}

[**[undo ip netstream export host ]{lang="EN-US"}**[\[ *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_84792_x5137_7688171}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1629561973}

[[系统视图和聚合视图下均没有配置目的地址和目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_84792_x5137_x601937472}[端口号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1355198572}

[[系统视图]{style="font-family:宋体"}[/NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_667934424}[聚合视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_87222606}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_779192073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_730284044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1389360272}

[*[ip-address]{lang="EN-US"}*]{#struct_0_84792_x5137_1388100891}[：]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[udp-port]{lang="EN-US"}*]{#struct_0_84792_x5137_292124492}[：]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vpn-instance vpn-instance-name]{lang="EN-US"}*]{#struct_0_84792_x5137_x1662233425}[：指定]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[统计输出报文的目的地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文的目的地址位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x2117388716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若某类聚合视图没有使能，则无法通过]{lang="EN-US" style="font-family:宋体"}**[display ip netstream export]{lang="EN-US"}**]{#struct_0_84792_x5137_620309382}[命令查看它的相关信息（包括目的地址的目的]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}[undo ip netstream export host]{lang="EN-US"}]{#struct_0_84792_x5137_x1127137259}[命令时未指定地址，表示取消指定本视图下配置的所有地址]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同聚合视图下可以配置相同的目的地址和目的]{style="font-family:宋体"}]{#struct_0_84792_x5137_975300191}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若聚合视图下没有配置目的地址和目的]{style="font-family:宋体"}]{#struct_0_84792_x5137_779257609}[UDP]{lang="EN-US"}[端口号，则使用系统视图下的配置；若聚合视图下配置了目的地址和目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，则使用聚合视图下的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个视图下最多可配置]{style="font-family:宋体"}]{#struct_0_84792_x5137_x207935536}[4]{lang="EN-US"}[组目的地址，包括不同]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。在同一视图下，若先后配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址相同、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号不同的目的地址，则后配置的目的地址生效。在用户配置了不同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称时，允许配置相同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[普通流统计输出报文会发给系统视图下配置的所有目的地址。聚合流统计输出报文会发给聚合类型对应的聚合视图下配置的所有目的地址。]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1442498355}[为了减少对网络带宽的占用，可以只在聚合视图下配置]{lang="EN-US" style="font-family:宋体"}**[ip netstream export host]{lang="EN-US"}**[命令，此时设备只会输出聚合流信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[undo ip netstream export host]{lang="EN-US"}**]{#struct_0_84792_x5137_635297172}[命令时，如果未指定]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则取消本视图下配置的所有]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x664431722}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x127756832}[配置全局]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[172.16.105.48]{lang="EN-US"}[，]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[5000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_901453896}

[\[Sysname\] ip netstream export host 172.16.105.48 5000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1012597674}[配置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[自治系统聚合统计输出报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[172.16.105.50]{lang="EN-US"}[，]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[6000]{lang="EN-US"}[。]{style="font-family:宋体"}[.]{lang="EN-US"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x638305774}

[\[Sysname\] ip netstream aggregation as]{lang="EN-US"}

[\[Sysname-ns-aggregation-as\] ip netstream export host 172.16.105.50 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1840658564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream aggregation]{lang="EN-US"}**]{#struct_0_84792_x5137_1189567621}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream export source]{lang="EN-US"}**]{#struct_0_84792_x5137_778798857}
:::

::: {#1113114618 .myid}
[]{#_Toc404797274}[]{#struct_0_84792_x5137_x487278083}

**NetStream \-- NetStream配置命令 \-- ip netstream export rate**

------------------------------------------------------------------------

[**[ip netstream export rate]{lang="EN-US"}**]{#struct_0_84792_x5137_x1338335384}[命令用来配置输出速率限制，即限制每秒钟输出的最多报文数。]{style="font-family:
宋体"}

[**[undo ip netstream export rate]{lang="EN-US"}**]{#struct_0_84792_x5137_x342378608}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1223510587}

[**[ip netstream export rate ]{lang="EN-US"}***[rate]{lang="EN-US"}*]{#struct_0_84792_x5137_x539423771}

[**[undo ip netstream export rate]{lang="EN-US"}**]{#struct_0_84792_x5137_x2116331724}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1309837484}

[[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_108560571}[统计输出报文的输出速率不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_778864393}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_x395450323}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1969412569}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_926301147}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1285757452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1305893581}

[*[rate]{lang="EN-US"}*]{#struct_0_84792_x5137_x1776771124}[：]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文的输出速率限制，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为每秒允许输出的最多报文个数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x35727905}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_778929929}[设置每秒最多允许]{style="font-family:宋体"}[10]{lang="EN-US"}[个报文被输出。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_2028219765}

[\[Sysname\] ip netstream export rate 10]{lang="EN-US"}
:::

::: {#-590963205 .myid}
[]{#_Toc404797275}[]{#struct_0_84792_x5137_553205898}[]{#_Toc250995610}[]{#_Toc55050577}[]{#_Toc28576983}

**NetStream \-- NetStream配置命令 \-- ip netstream export source**

------------------------------------------------------------------------

[**[ip netstream export source]{lang="EN-US"}**]{#struct_0_84792_x5137_1417586934}[命令用来配置]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[统计输出报文的源接口。]{style="font-family:
宋体"}

[**[undo ip netstream export source]{lang="EN-US"}**]{#struct_0_84792_x5137_x1904939593}[命令用来取消配置的输出报文的源接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1255770455}

[**[ip netstream export source interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_84792_x5137_2129339573}

[**[undo ip netstream export source]{lang="EN-US"}**]{#struct_0_84792_x5137_1127432236}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1328356499}

[[采用统计输出报文的出接口作为源接口。]{style="font-family:宋体"}]{#struct_0_84792_x5137_778995465}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1190539587}

[[系统视图]{style="font-family:宋体"}[/NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_1589853855}[聚合视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1793064493}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x2141566886}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1106087365}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x356349580}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_84792_x5137_1383998061}[：]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文的源接口，由接口类型和接口编号组成。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1964781195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令配置源接口后，会将]{style="font-family:宋体"}]{#struct_0_84792_x5137_779585289}[NetStream]{lang="EN-US"}[统计输出报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址设置为该接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同聚合视图下可以配置不同的源接口。]{style="font-family:宋体"}]{#struct_0_84792_x5137_1288197873}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合视图下若没有配置源接口，则使用系统视图下的配置。]{style="font-family:宋体"}]{#struct_0_84792_x5137_79156519}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x617775103}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x813158256}[将]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文源接口设置为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x2017233169}

[\[Sysname\] ip netstream export source interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1012335530}[将]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[自治系统聚合统计输出报文源接口设置为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x1012532138}

[\[Sysname\] ip netstream aggregation as]{lang="EN-US"}

[\[Sysname-ns-aggregation-as\] ip netstream export source interface gigabitethernet 1/0/2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1440208623}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream aggregation]{lang="EN-US"}**]{#struct_0_84792_x5137_2108418286}
:::

::: {#-1197763210 .myid}
[]{#_Toc404797276}[]{#struct_0_84792_x5137_779650825}

**NetStream \-- NetStream配置命令 \-- ip netstream export v9-template refresh-rate packet**

------------------------------------------------------------------------

[**[ip netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_84792_x5137_x793929274}[命令用来配置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率。]{style="font-family:宋体"}

[**[undo ip netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_84792_x5137_255003923}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1237600457}

[**[ip netstream export v9-template refresh-rate packet ]{lang="EN-US"}***[packets]{lang="EN-US"}*]{#struct_0_84792_x5137_1156453588}

[**[undo ip netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_84792_x5137_x15415612}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x644073886}

[[每隔]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_84792_x5137_x955212858}[个包设备发送一次版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x890500948}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_779061002}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1625539070}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1033832775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_728431950}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x713347762}

[*[packets]{lang="EN-US"}*]{#struct_0_84792_x5137_1936344816}[：]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为包数，即每隔多少个包更新一次模板，并通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的]{style="font-family:宋体"}[V9]{lang="EN-US"}[模板格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1998275283}

[[V9]{lang="EN-US"}]{#struct_0_84792_x5137_779126538}[版本是基于模板方式的、支持自定义格式，由于]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器不会永久保存模板，所以设备需要定期通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的]{style="font-family:宋体"}[V9]{lang="EN-US"}[模板格式。用户可以根据实际情况，配置版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率，及时更新模板。]{style="font-family:宋体"}

[[可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_1083022525}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_319655486}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_393618170}[将]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的包刷新率设为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x1952540705}

[\[Sysname\] ip netstream export v9-template refresh-rate packet 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1013087195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_84792_x5137_x1766156540}
:::

::: {#113470092 .myid}
[]{#_Toc404797277}[]{#struct_0_84792_x5137_1181021057}

**NetStream \-- NetStream配置命令 \-- ip netstream export v9-template refresh-rate time**

------------------------------------------------------------------------

[**[ip netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_84792_x5137_779192074}[命令用来配置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率。]{style="font-family:宋体"}

[**[undo ip netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_84792_x5137_730284051}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_949291883}

[**[ip netstream export v9-template refresh-rate time ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_84792_x5137_1408488133}

[**[undo ip netstream export v9-template refresh-rate time]{lang="EN-US"}**]{#struct_0_84792_x5137_x1053374401}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_2103827687}

[[每隔]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_84792_x5137_279868474}[分钟设备发送一次版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x982376739}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_779257610}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_2130716633}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x2049695930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1085083028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_582681305}

[*[minutes]{lang="EN-US"}*]{#struct_0_84792_x5137_73039680}[：]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为分钟，即每隔多少分钟更新一次模板，并通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的]{style="font-family:宋体"}[V9]{lang="EN-US"}[模板格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_449558600}

[[V9]{lang="EN-US"}]{#struct_0_84792_x5137_778798858}[版本是基于模板方式的、支持自定义格式，由于]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器不会永久保存模板，所以设备需要定期通知]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[服务器最新的]{style="font-family:宋体"}[V9]{lang="EN-US"}[模板格式。用户可以根据实际情况，配置版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率，及时更新模板。]{style="font-family:宋体"}

[[可以同时配置包刷新率和时间刷新率，只要满足任意一个刷新条件，设备就会将符合条件的模板发送给]{style="font-family:宋体"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_x487278092}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1338400921}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_2042637066}[将]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文版本]{style="font-family:宋体"}[9]{lang="EN-US"}[模板的时间刷新率设为]{style="font-family:宋体"}[60]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x1608060782}

[\[Sysname\] ip netstream export v9-template refresh-rate time 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_2028707438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream export v9-template refresh-rate packet]{lang="EN-US"}**]{#struct_0_84792_x5137_1374532262}
:::

::: {#-494163086 .myid}
[]{#_Toc404797278}[]{#struct_0_84792_x5137_864492948}

**NetStream \-- NetStream配置命令 \-- ip netstream export version**

------------------------------------------------------------------------

[**[ip netstream export version 5]{lang="EN-US"}**]{#struct_0_84792_x5137_778864394}[命令用来配置]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[版本]{style="font-family:
宋体"}[5]{lang="EN-US"}[的自治系统选项。]{style="font-family:宋体"}

[**[ip netstream export version 9]{lang="EN-US"}**]{#struct_0_84792_x5137_x395450330}[命令用来配置]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[版本]{style="font-family:
宋体"}[9]{lang="EN-US"}[的自治系统选项和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳选项。]{style="font-family:宋体"}

[**[undo ip netstream export version]{lang="EN-US"}**]{#struct_0_84792_x5137_x1969215962}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1297384174}

[**[ip netstream export version]{lang="EN-US"}**[ *5* \[ **origin-as** \| **peer-as** \]]{lang="EN-US"}]{#struct_0_84792_x5137_432286523}

[**[ip netstream export version]{lang="EN-US"}**[ 9 \[ **origin-as** \| **peer-as** \] \[ **bgp-nexthop** \]]{lang="EN-US"}]{#struct_0_84792_x5137_x125714525}

[**[undo ip netstream export version]{lang="EN-US"}**]{#struct_0_84792_x5137_671231761}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1565434984}

[[普通流信息通过版本]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_84792_x5137_x1818879398}[的]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文发送，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[流信息不输出。自治系统选项使用邻接自治系统号（]{style="font-family:宋体"}**[peer-as]{lang="EN-US"}**[），流信息中不记录]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_778929930}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_x310432404}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1532434073}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_1727821046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1448695946}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x697204493}

[**[origin-as]{lang="EN-US"}**]{#struct_0_84792_x5137_1737881575}[：流信息中记录的自治系统号为起始自治系统号。]{style="font-family:宋体"}

[**[peer-as]{lang="EN-US"}**]{#struct_0_84792_x5137_x94593154}[：流信息中记录的自治系统号为邻接自治系统号。]{style="font-family:宋体"}

[**[bgp-nexthop]{lang="EN-US"}**]{#struct_0_84792_x5137_1655342666}[：流信息中记录]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_778995466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_1190539586}[流信息中会记录流的源]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址及其对应的自治系统号；目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及其对应的自治系统号。设备会根据用户实际配置的自治系统参数来确定记录的自治系统号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在版本号为]{style="font-family:宋体"}]{#struct_0_84792_x5137_1589919391}[9]{lang="EN-US"}[时，才可以配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[下一跳。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备上同时只允许一种版本存在，]{style="font-family:宋体"}]{#struct_0_84792_x5137_x186104300}[V5]{lang="EN-US"}[和]{style="font-family:宋体"}[V9]{lang="EN-US"}[不能同时配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备上配置了聚合时，如果配置输出报文版本为]{style="font-family:宋体"}]{#struct_0_84792_x5137_x941025581}[V5]{lang="EN-US"}[，则流统计信息采用]{style="font-family:宋体"}[V8]{lang="EN-US"}[版本输出；如果配置输出版本为]{style="font-family:宋体"}[V9]{lang="EN-US"}[，则流统计信息采用]{style="font-family:宋体"}[V9]{lang="EN-US"}[版本输出。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令重复配置时，新配置会覆盖旧配置。]{style="font-family:宋体"}]{#struct_0_84792_x5137_1558885009}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_316464385}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_1283893600}[将]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[统计输出报文版本号设为]{style="font-family:宋体"}[5]{lang="EN-US"}[，并设置流信息中记录的自治系统号为起始自治系统号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_779585290}

[\[Sysname\] ip netstream export version 5 origin-as]{lang="EN-US"}
:::

::: {#-126248018 .myid}
[]{#_Toc404797279}[]{#struct_0_84792_x5137_x815541667}[]{#_Toc250995616}

**NetStream \-- NetStream配置命令 \-- ip netstream max-entry**

------------------------------------------------------------------------

[**[ip netstream max-entry]{lang="EN-US"}**]{#struct_0_84792_x5137_984636901}[命令用来配置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流缓存区中流表项的最大数目及达到最大数目时的处理方式。]{style="font-family:宋体"}

[**[undo ip netstream max-entry]{lang="EN-US"}**]{#struct_0_84792_x5137_1083022522}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_319589950}

[**[ip netstream max-entry]{lang="EN-US"}**[ { *max-entries* \| *aging* \| *disable-caching* }]{lang="EN-US"}]{#struct_0_84792_x5137_x127173270}

[**[undo ip netstream max-entry]{lang="EN-US"}**]{#struct_0_84792_x5137_x246522207}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1225578503}

[[本命令的缺省情况与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_84792_x5137_457267033}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1882251066}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_779192071}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_730284046}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1389360274}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_225301477}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1114981931}

[*[max-entries]{lang="EN-US"}*]{#struct_0_84792_x5137_x852521118}[：]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流缓存区中流表项的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[aging]{lang="EN-US"}**]{#struct_0_84792_x5137_563051984}[：达到流表项的最大数目时，强制老化部分流表项。]{style="font-family:宋体"}

[**[disable-caching]{lang="EN-US"}**]{#struct_0_84792_x5137_439956668}[：达到流表项的最大数目时，禁止新建流表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1632316667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-entries]{lang="EN-US"}*]{#struct_0_84792_x5137_779257607}[参数值在各单板上单独生效，而不是各单板的总和。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-entries]{lang="EN-US"}*]{#struct_0_84792_x5137_x207935534}[参数值在各成员设备的各单板上单独生效，而不是各单板的总和。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-entries]{lang="EN-US"}*]{#struct_0_84792_x5137_x1442629427}[参数值在各成员设备上单独生效，而不是各成员设备的总和。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream max-entry]{lang="EN-US"}**[ *max-entries*]{lang="EN-US"}]{#struct_0_84792_x5137_x2047902938}[命令可重复配置，以最后一次配置为准。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream max-entry]{lang="EN-US"}**]{#struct_0_84792_x5137_x1012335533}**[ ]{lang="EN-US"}**[{ **aging** \| **disable-caching** }]{lang="EN-US"}[命令可以重复配置，以最后一次配置为准。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_784286615}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1506447431}[设置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[流缓存区中流表项的最大数目为]{style="font-family:宋体"}[5000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x2094196337}

[\[Sysname\] ip netstream max-entry 5000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x123681248}[设置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[在达到流表项的最大数目时，禁止新建流表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_778798855}

[\[Sysname\] ip netstream max-entry disable-caching]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x487278081}[设置]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[在达到流表项的最大数目时，强制老化部分流表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x1338204312}

[\[Sysname\] ip netstream max-entry aging]{lang="EN-US"}
:::

::: {#-738592420 .myid}
[]{#_Toc404797280}[]{#struct_0_84792_x5137_x45834337}[]{#_Toc250995617}

**NetStream \-- NetStream配置命令 \-- ip netstream mpls**

------------------------------------------------------------------------

[**[ip netstream mpls]{lang="EN-US"}**]{#struct_0_84792_x5137_x620063650}[命令用来开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文统计功能，即统计和输出]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[格式的报文。]{style="font-family:宋体"}

[**[undo ip netstream mpls]{lang="EN-US"}**]{#struct_0_84792_x5137_1501650497}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1018747984}

[**[ip netstream mpls ]{lang="EN-US"}**[\[ **label-positions** *label-position1* \[ *label-position2* \[ *label-position3* \] \] \] \[ **no-ip-fields** \]]{lang="EN-US"}]{#struct_0_84792_x5137_1873908086}

[**[undo ip netstream mpls]{lang="EN-US"}**]{#struct_0_84792_x5137_1102679824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_778864391}

[[未开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_84792_x5137_x395450325}[报文统计功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1969019353}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_1334114175}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_665600659}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_180767728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_744063361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x981814130}

[**[label-positions]{lang="EN-US"}**]{#struct_0_84792_x5137_778929927}[：统计的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的标签位置。]{style="font-family:宋体"}

[*[label-position1]{lang="EN-US"}*]{#struct_0_84792_x5137_2028219763}[：指定统计的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的第一个标签位置，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[label-position2]{lang="EN-US"}*]{#struct_0_84792_x5137_553599114}[：指定统计的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的第二个标签位置，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[label-position3]{lang="EN-US"}*]{#struct_0_84792_x5137_505319024}[：指定统计的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的第三个标签位置，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-ip-fields]{lang="EN-US"}**]{#struct_0_84792_x5137_845026282}[：不统计]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1512396200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令不仅使能]{lang="EN-US" style="font-family:宋体"}[IPv4 NetStream]{lang="EN-US"}]{#struct_0_84792_x5137_2054614653}[对]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的统计功能，同时也使能了]{lang="EN-US" style="font-family:宋体"}[IPv6 NetStream]{lang="EN-US"}[对]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的统计功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若未指定任何参数，表示基于]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1215674773}[MPLS]{lang="EN-US"}[报文的首标签并且带有]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当需要统计]{style="font-family:宋体"}]{#struct_0_84792_x5137_x211527849}[MPLS]{lang="EN-US"}[报文的多个标签时，指定的标签位置不允许重复，最终统计的多个标签的位置依据从小到大的顺序取指定值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_778995463}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_1190539581}[开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文统计功能，基于]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的首标签并且不带]{style="font-family:宋体"}[IP]{lang="EN-US"}[选项进行统计。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_1589722783}

[\[Sysname\] ip netstream mpls no-ip-fields]{lang="EN-US"}
:::

::: {#1620236268 .myid}
[]{#_Toc404797281}[]{#struct_0_84792_x5137_x1745883386}[]{#_Toc250995619}[]{#_Toc55050579}[]{#_Toc28576985}

**NetStream \-- NetStream配置命令 \-- ip netstream timeout active**

------------------------------------------------------------------------

[**[ip netstream timeout active]{lang="EN-US"}**]{#struct_0_84792_x5137_779061000}[命令用来配置流的活跃老化时间。]{style="font-family:
宋体"}

[**[undo ip netstream timeout active]{lang="EN-US"}**]{#struct_0_84792_x5137_x1625539072}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x128966639}

[**[ip netstream timeout active]{lang="EN-US"}**[ *minutes*]{lang="EN-US"}]{#struct_0_84792_x5137_x1950738298}

[**[undo ip netstream timeout active]{lang="EN-US"}**]{#struct_0_84792_x5137_x326912506}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x412554509}

[[流的活跃老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_84792_x5137_351577322}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_779126536}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_1083022523}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_319524414}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_102703697}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1217836369}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x250692637}

[*[minutes]{lang="EN-US"}*]{#struct_0_84792_x5137_779192072}[：流的活跃老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_730284045}

[[从采集到的第一个报文]{style="font-family:宋体"}]{#struct_0_84792_x5137_x1389360273}[开始，该]{style="font-family:宋体"}[流在]{style="font-family:宋体"}[指定的时间内能被采集到，则该流属于活跃的流，指定的时间称为流的活跃老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x177983050}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_779257608}[将流的活跃老化时间设置为]{style="font-family:宋体"}[60]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_x207935535}

[\[Sysname\] ip netstream timeout active 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1442563891}

[]{#_Toc250995620}[]{#_Toc55050580}[]{#_Toc28576986}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip netstream timeout inactive]{lang="EN-US"}**]{#struct_0_84792_x5137_1191450328}
:::

::: {#-1093526609 .myid}
[]{#_Toc404797282}[]{#struct_0_84792_x5137_1916164139}

**NetStream \-- NetStream配置命令 \-- ip netstream timeout inactive**

------------------------------------------------------------------------

[**[ip netstream timeout inactive]{lang="EN-US"}**]{#struct_0_84792_x5137_x2081892495}[命令用来配置流的不活跃老化时间。]{style="font-family:
宋体"}

[**[undo ip netstream timeout inactive]{lang="EN-US"}**]{#struct_0_84792_x5137_778798856}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x487278082}

[**[ip netstream timeout inactive]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_84792_x5137_x1338400920}

[**[undo ip netstream timeout inactive]{lang="EN-US"}**]{#struct_0_84792_x5137_x686246289}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x357880459}

[[流的不活跃老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_84792_x5137_647295752}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x2059968722}

[[系统视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_778864392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x395450324}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x1968953817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_307189407}

[[【参数】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x1292108414}

[*[seconds]{lang="EN-US"}*]{#struct_0_84792_x5137_x1111238089}[：流的不活跃老化时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1778116023}

[[从采集到的最后一个报文]{style="font-family:宋体"}]{#struct_0_84792_x5137_778929928}[开始，该]{style="font-family:宋体"}[流在]{style="font-family:宋体"}[指定的时间内没有被采集到，则该流属于不活跃的流，指定的时间称为流的不活跃老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_2028219764}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_553140362}[将流的不活跃老化时间设置为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_84792_x5137_778995464}

[\[Sysname\] ip netstream timeout inactive 60]{lang="EN-US"}[]{#_Toc143514304}[]{#_Toc143517533}[]{#_Toc143514305}[]{#_Toc143517534}[]{#_Toc143514306}[]{#_Toc143517535}[]{#_Toc143514307}[]{#_Toc143517536}[]{#_Toc143514308}[]{#_Toc143517537}[]{#_Toc143514309}[]{#_Toc143517538}[]{#_Toc143514310}[]{#_Toc143517539}[]{#_Toc143514311}[]{#_Toc143517540}[]{#_Toc143514312}[]{#_Toc143517541}[]{#_Toc143514313}[]{#_Toc143517542}[]{#_Toc143514314}[]{#_Toc143517543}[]{#_Toc143514315}[]{#_Toc143517544}[]{#_Toc143514318}[]{#_Toc143517547}[]{#_Toc143514326}[]{#_Toc143517555}[]{#_Toc143514342}[]{#_Toc143517571}[]{#_Hlt11753812}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1190539588}

[]{#_Toc250995622}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ip netstream timeout active]{lang="EN-US"}**]{#struct_0_84792_x5137_1589264031}
:::

::: {#53358021 .myid}
[]{#_Toc404797283}[]{#struct_0_84792_x5137_1742621214}

**NetStream \-- NetStream配置命令 \-- reset ip netstream statistics**

------------------------------------------------------------------------

[**[reset ip netstream statistics]{lang="EN-US"}**]{#struct_0_84792_x5137_1626847279}[命令用来将流缓存区中所有流强制老化，输出报文信息，并清空]{style="font-family:
宋体"}[NetStream]{lang="EN-US"}[缓冲区的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1503837763}

[**[reset ip netstream statistics]{lang="EN-US"}**]{#struct_0_84792_x5137_1944223928}

[[【视图】]{style="font-family:黑体"}]{#struct_0_84792_x5137_2091372411}

[[用户视图]{style="font-family:宋体"}]{#struct_0_84792_x5137_779585288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_84792_x5137_1288197872}

[[network-admin]{lang="EN-US"}]{#struct_0_84792_x5137_79090983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_84792_x5137_x353257409}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_84792_x5137_x262815318}

[[在执行清空缓冲区中老化流的动作时，命令行会给出提示，告知用户这个动作可能要持续几分钟，在这段时间内不能统计。]{style="font-family:宋体"}]{#struct_0_84792_x5137_x2084411186}

[[【举例】]{style="font-family:黑体"}]{#struct_0_84792_x5137_2061570475}

[[\# ]{lang="EN-US"}]{#struct_0_84792_x5137_x1388296337}[将流缓存区中所有流老化，输出报文信息，并清空]{style="font-family:宋体"}[NetStream]{lang="EN-US"}[缓冲区的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ip netstream statistics]{lang="EN-US"}]{#struct_0_84792_x5137_x1277172535}

[This process may take a few minutes.]{lang="EN-US"}

[Netstream statistic function is disabled during this process.]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
