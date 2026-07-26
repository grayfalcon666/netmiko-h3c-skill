::: {#2083024061 .myid}
[]{#_Toc404793547}[]{#struct_0_86917_x8972_x712298265}

**会话管理 \-- 会话管理配置命令 \-- display session aging-time application**

------------------------------------------------------------------------

[**[display session aging-time application]{lang="EN-US"}**]{#struct_0_86917_x8972_1137997516}[命令用来显示应用层协议的会话老化时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x869550556}

[**[display session aging-time application]{lang="EN-US"}**]{#struct_0_86917_x8972_x1816780502}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_372623070}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_321369924}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1105711834}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_220722032}

[[network-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x1820649691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1255459770}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x1903415145}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x710627404}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_2080655225}[显示当前各应用层协议的会话老化时间。]{style="font-family:宋体"}

[[\<Sysname\> display session aging-time application]{lang="EN-US"}]{#struct_0_86917_x8972_321697604}

[Application         Aging Time(s)]{lang="EN-US"}

[DNS                 60]{lang="EN-US"}

[FTP                 3600]{lang="EN-US"}

[GTP                 60]{lang="EN-US"}

[H225                3600]{lang="EN-US"}

[H245                3600]{lang="EN-US"}

[RAS                 300]{lang="EN-US"}

[RTSP                3600]{lang="EN-US"}

[SIP                 300]{lang="EN-US"}

[TFTP                60]{lang="EN-US"}

[ILS                 3600]{lang="EN-US"}

[MGCP                60]{lang="EN-US"}

[NBT                 3600]{lang="EN-US"}

[PPTP                3600]{lang="EN-US"}

[RSH                 60]{lang="EN-US"}

[SCCP                3600]{lang="EN-US"}

[SQLNET              600]{lang="EN-US"}

[XDMCP               3600]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display session aging-time application]{lang="EN-US"}]{#struct_0_86917_x8972_x1718360906}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x93600967}[[字段]{style="font-family:黑体"}]{#struct_0_86917_x8972_x2084264173}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86917_x8972_x650751817}

[[Application]{lang="EN-US"}]{#struct_0_86917_x8972_x190808561}

[[应用层协议类型]{style="font-family:宋体"}]{#struct_0_86917_x8972_25788879}

[[Aging Time(s)]{lang="EN-US"}]{#struct_0_86917_x8972_321763140}

[[会话老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1287092150}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1682929504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[application aging-time]{lang="EN-US"}**]{#struct_0_86917_x8972_1194264472}

::: {#190248486 .myid}
[]{#_Toc404793548}[]{#struct_0_86917_x8972_x1865340068}

**会话管理 \-- 会话管理配置命令 \-- display session aging-time state**

------------------------------------------------------------------------

[**[display session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_x177159397}[命令用来显示各协议状态的会话老化时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x237246334}

[**[display session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_x1971914568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x911030696}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_321173317}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x532242696}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1037945631}

[[network-operator]{lang="EN-US"}]{#struct_0_86917_x8972_148294892}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1845309071}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86917_x8972_983738497}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x555458343}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x579561628}[显示当前各协议状态的会话老化时间。]{style="font-family:宋体"}

[[\<Sysname\> display session aging-time state]{lang="EN-US"}]{#struct_0_86917_x8972_321238853}

[State                     Aging Time(s)]{lang="EN-US"}

[SYN                       10]{lang="DA"}

[TCP-EST                   3600]{lang="DA"}

[FIN                       10]{lang="DA"}

[UDP-OPEN                  10]{lang="DA"}

[UDP-READY                 30]{lang="EN-US"}

[ICMP-REQUEST              30]{lang="EN-US"}

[ICMP-REPLY                10]{lang="EN-US"}

[RAWIP-OPEN                30]{lang="EN-US"}

[RAWIP-READY               60]{lang="EN-US"}

[UDPLITE-OPEN              30]{lang="EN-US"}

[UDPLITE-READY             60]{lang="EN-US"}

[DCCP-REQUEST              30]{lang="EN-US"}

[DCCP-EST                  3600]{lang="EN-US"}

[DCCP-CLOSEREQ             30]{lang="EN-US"}

[SCTP-INIT                 30]{lang="EN-US"}

[SCTP-EST                  3600]{lang="EN-US"}

[SCTP-SHUTDOWN             30]{lang="EN-US"}

[ICMPV6-REQUEST            60]{lang="EN-US"}

[ICMPV6-REPLY              30]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display session aging-time state]{lang="EN-US"}]{#struct_0_86917_x8972_x1501650663}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x100573735}[[字段]{style="font-family:黑体"}]{#struct_0_86917_x8972_232142725}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86917_x8972_1544663877}

[[State]{lang="EN-US"}]{#struct_0_86917_x8972_321042245}

[[各协议的状态类型]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1310518284}

[[Aging Time(s)]{lang="EN-US"}]{#struct_0_86917_x8972_797770075}

[[会话老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1697965383}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x948622984}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_x1008719774}

::: {#-1424836227 .myid}
[]{#_Toc404793549}[]{#struct_0_86917_x8972_928185187}

**会话管理 \-- 会话管理配置命令 \-- display session relation-table**

------------------------------------------------------------------------

[**[display session relation-table]{lang="EN-US"}**]{#struct_0_86917_x8972_x455013726}[命令用来显示关联表项信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_321107781}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1700957891}

[**[display session relation-table ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } ]{lang="EN-US"}]{#struct_0_86917_x8972_x2136564614}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_1613466068}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display session relation-table ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_86917_x8972_x1737626156}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_x1878579256}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display session relation-table ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ ]{lang="EN-US"}]{#struct_0_86917_x8972_x601904177}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x202914769}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x435960787}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_323281664}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_321435461}

[[network-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x445329745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1812802148}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x1596843285}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1831516387}

[**[ipv4]{lang="EN-US"}**]{#struct_0_86917_x8972_x1399802133}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[关联表项。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86917_x8972_1684542491}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[关联表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1726582175}[：显示指定单板上的关联表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，显示所有单板上的关联表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1438835601}[：显示指定成员设备上的关联表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有成员设备上的关联表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_1115953475}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的关联表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的关联表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_321500997}[：显示指定成员设备的指定单板上的关联表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的关联表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1274042832}[：]{style="font-family:宋体"}[显示指定单板上的关联表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的关联表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x847992901}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的关联表项信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1197195871}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1398959781}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[关联表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display session relation-table ipv4]{lang="EN-US"}]{#struct_0_86917_x8972_321304389}

[Source IP/port:      192.168.1.100/-]{lang="EN-US"}

[Destination IP/port: 192.168.2.100/99]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: 1/-/-]{lang="FR"}

[Protocol: TCP(6)    TTL: 1234s    App: FTP-DATA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Source IP]{lang="FR"}[/port]{lang="EN-US"}[:      -/-]{lang="FR"}

[Destination IP/port: 192.168.2.200/1212]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[Protocol: TCP(6)    TTL: 3100s    App: H225]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found:  2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_529702617}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[关联表项。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display session relation-table ipv4]{lang="EN-US"}]{#struct_0_86917_x8972_x712298276}

[Slot 1]{lang="EN-US"}[：]{style="font-family:
宋体"}

[Source IP/port:      192.168.1.100]{lang="EN-US"}[/-]{lang="FR"}

[Destination IP/port: 192.168.2.100/99]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: 1/-/-]{lang="FR"}

[Protocol: TCP(6)    TTL: 1234s    App: FTP-DATA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Source IP]{lang="FR"}[/port]{lang="EN-US"}[:      -/-]{lang="FR"}

[Destination IP/port: 192.168.2.200/1212]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[Protocol: TCP(6)    TTL: 3100s    App: H225]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found:  2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_1137931981}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[关联表项。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display session relation-table ipv6]{lang="EN-US"}]{#struct_0_86917_x8972_321369925}

[Source IP:             2011::0002]{lang="FR"}

[Destination IP/port: 2011::0008/1212]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[Protocol: TCP(6)    TTL: 567s    App: FTP-DATA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found:]{lang="EN-US"}[  1]{lang="FR"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1105711835}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[关联表项。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display session relation-table ipv6]{lang="EN-US"}]{#struct_0_86917_x8972_1786805973}

[Slot 1]{lang="EN-US"}[：]{style="font-family:
宋体"}

[Source IP:             2011::0002]{lang="FR"}

[Destination IP/port: 2011::0008/1212]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[Protocol: TCP(6)    TTL: 567s    App: FTP-DATA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found:]{lang="EN-US"}[  1]{lang="FR"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x848255045}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[关联表项。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display session relation-table ipv4]{lang="EN-US"}]{#struct_0_86917_x8972_1188082391}

[CPU 0 on slot 1]{lang="EN-US"}[：]{style="font-family:宋体"}

[Source IP/port:      192.168.1.100]{lang="EN-US"}[/-]{lang="FR"}

[Destination IP/port: 192.168.2.100/99]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: 1/-/-]{lang="FR"}

[Protocol: TCP(6)    TTL: 1234s    App: FTP-DATA]{lang="EN-US"}

[Source IP]{lang="FR"}[/port]{lang="EN-US"}[:      -/-]{lang="FR"}

[Destination IP/port: 192.168.2.200/1212]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[Protocol: TCP(6)    TTL: 3100s    App: H225]{lang="EN-US"}

[Total entries found:  2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x318271949}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[关联表项。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display session relation-table ipv6]{lang="EN-US"}]{#struct_0_86917_x8972_x848451653}

[CPU 0 on slot 1]{lang="EN-US"}[：]{style="font-family:宋体"}

[Source IP:             2011::0002]{lang="FR"}

[Destination IP/port: 2011::0008/1212]{lang="FR"}

[DS-Lite tunnel peer: -]{lang="EN-US"}

[VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[Protocol: TCP(6)    TTL: 567s    App: FTP-DATA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries found:]{lang="EN-US"}[  1]{lang="FR"}

[[表1-3 ]{lang="EN-US"}[display session relation-table]{lang="EN-US"}]{#struct_0_86917_x8972_x551830153}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x97236263}[[字段]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1858276599}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86917_x8972_2033262691}

[[Source IP]{lang="EN-US"}]{#struct_0_86917_x8972_321697605}[/port]{lang="FR"}

[[会话的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86917_x8972_x1718360905}[地址和端口号。如果未指定则显示"]{style="font-family:宋体"}[-/-]{lang="EN-US"}["]{style="font-family:宋体"}

[[IPv6]{lang="EN-US"}]{#struct_0_86917_x8972_1807418596}[会话无源端口号字段]{style="font-family:宋体"}

[[Destination IP/port]{lang="FR"}]{#struct_0_86917_x8972_x1203517371}

[[会话的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86917_x8972_689066049}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_86917_x8972_x1261291013}

[[会话所属的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}]{#struct_0_86917_x8972_820408623}[隧道对端地址。未指定的参数则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[VPN instance/VLAN ID/VLL ID]{lang="FR"}]{#struct_0_86917_x8972_321763141}

[[关联表项所属的]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1287092151}[MPLS L3VPN/]{lang="EN-US"}[二层转发时会话所属的]{style="font-family:宋体"}[VLAN ID/]{lang="EN-US"}[二层转发时会话所属的]{style="font-family:宋体"}[INLINE]{lang="EN-US"}[。未指定的参数则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_86917_x8972_1045953851}

[[传输层协议类型]{style="font-family:宋体"}]{#struct_0_86917_x8972_235589145}

[[TTL]{lang="EN-US"}]{#struct_0_86917_x8972_x825908494}

[[关联表的剩余存活时间，单位为秒]{style="font-family:宋体"}]{#struct_0_86917_x8972_2108401310}

[[App]{lang="EN-US"}]{#struct_0_86917_x8972_321173314}

[[应用层协议类型]{style="font-family:宋体"}]{#struct_0_86917_x8972_x532242695}

[[Total entries found]{lang="EN-US"}]{#struct_0_86917_x8972_1038142239}

[[当前查找到的关联表总数]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1645085135}

[ ]{lang="EN-US"}

::: {#-895637405 .myid}
[]{#_Toc404793550}[]{#struct_0_86917_x8972_x2011240304}

**会话管理 \-- 会话管理配置命令 \-- display session statistics**

------------------------------------------------------------------------

[**[display session statistics]{lang="EN-US"}**]{#struct_0_86917_x8972_1553764455}[命令用来显示会话统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x797748674}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_321238850}

[**[display session statistics ]{lang="EN-US"}**[\[ **summary** \]]{lang="EN-US"}]{#struct_0_86917_x8972_x1501650662}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_x1333941216}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display session statistics ]{lang="EN-US"}**[\[ **summary** \]]{lang="EN-US"}[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}]{#struct_0_86917_x8972_x1165448093}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_x223879739}[模式：]{style="font-family:宋体"}

[**[display session statistics ]{lang="EN-US"}**[\[ **summary** \]]{lang="EN-US"}**[ ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_86917_x8972_1203247952}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_378765824}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x2089366947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1584037562}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_321042242}

[[network-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x1310518289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_750715908}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x659872833}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1966208551}

[**[summary]{lang="EN-US"}**]{#struct_0_86917_x8972_x1825959920}[：显示会话统计信息的概要信息。不指定该参数时，显示会话统计信息的详细信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x114481637}[：显示指定单板上的会话统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，显示所有单板上的会话统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1279369725}[：显示指定成员设备上的会话统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有成员设备上的会话统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_x853480529}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的会话统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的会话统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x2084785027}[：显示指定成员设备的指定单板上的会话统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的会话统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_183825035}[：]{style="font-family:宋体"}[显示指定单板上的会话统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的会话统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_717894437}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的会话统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1401250118}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_1915495467}[显示所有会话统计信息的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display session statistics]{lang="EN-US"}]{#struct_0_86917_x8972_321500994}

[Current sessions: 3]{lang="EN-US"}

[     TCP sessions: 0]{lang="EN-US"}

[            TCP_SYN_SENT: 0                    TCP_SYN_RECV: 0]{lang="EN-US"}

[         TCP_ESTABLISHED: 0                    TCP_FIN_WAIT: 0]{lang="EN-US"}

[          TCP_CLOSE_WAIT: 0                    TCP_LAST_ACK: 0]{lang="EN-US"}

[           TCP_TIME_WAIT: 0                       TCP_CLOSE: 0]{lang="EN-US"}

[           TCP_SYN_SENT2: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     UDP sessions: 0]{lang="EN-US"}

[                UDP_OPEN: 0                       UDP_READY: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     ICMP sessions: 3]{lang="EN-US"}

[            ICMP_REQUEST: 0                      ICMP_REPLY: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[     ICMPv6 sessions: 0]{lang="EN-US"}

[            ICMP_REQUEST: 0                      ICMP_REPLY: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     UDP-Lite sessions: 0]{lang="EN-US"}

[            UDPLITE_OPEN: 0                   UDPLITE_READY: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     SCTP sessions: 0]{lang="EN-US"}

[             SCTP_CLOSED: 0                SCTP_COOKIE_WAIT: 0]{lang="EN-US"}

[      SCTP_COOKIE_ECHOED: 0                SCTP_ESTABLISHED: 0]{lang="EN-US"}

[      SCTP_SHUTDOWN_SENT: 0              SCTP_SHUTDOWN_RECD: 0]{lang="EN-US"}

[  SCTP_SHUTDOWN_ACK_SENT: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     DCCP sessions: 0]{lang="EN-US"}

[            DCCP_REQUEST: 0                    DCCP_RESPOND: 0]{lang="EN-US"}

[           DCCP_PARTOPEN: 0                       DCCP_OPEN: 0]{lang="EN-US"}

[           DCCP_CLOSEREQ: 0                    DCCP_CLOSING: 0]{lang="EN-US"}

[           DCCP_TIMEWAIT: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[     RAWIP sessions: 0]{lang="EN-US"}

[              RAWIP_OPEN: 0                     RAWIP_READY: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Current relation-table entries: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Session establishment rate: 0/s]{lang="EN-US"}

[          TCP:                   0/s]{lang="EN-US"}

[          UDP:                   0/s]{lang="EN-US"}

[         ICMP:                   0/s]{lang="EN-US"}

[       ICMPv6:                   0/s]{lang="EN-US"}

[     UDP-Lite:                   0/s]{lang="EN-US"}

[         SCTP:                   0/s]{lang="EN-US"}

[         DCCP:                   0/s]{lang="EN-US"}

[        RAWIP:                   0/s]{lang="EN-US"}

[ ]{lang="EN-US"}

[Received TCP      :                   0 packets                    0 bytes]{lang="EN-US"}

[Received UDP      :                 118 packets                13568 bytes]{lang="EN-US"}

[Received ICMP     :                 105 packets                 8652 bytes]{lang="EN-US"}

[Received ICMPv6   :                   0 packets                    0 bytes]{lang="EN-US"}

[Received UDP-Lite :                   0 packets                    0 bytes]{lang="EN-US"}

[Received SCTP     :                   0 packets                    0 bytes]{lang="EN-US"}

[Received DCCP     :                   0 packets                    0 bytes]{lang="EN-US"}

[Received RAWIP    :                   0 packets                    0 bytes]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display session statistics]{lang="EN-US"}]{#struct_0_86917_x8972_x13488932}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x71034023}[[字段]{style="font-family:黑体"}]{#struct_0_86917_x8972_365171542}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86917_x8972_x975514196}

[[Current sessions]{lang="EN-US"}]{#struct_0_86917_x8972_1506137301}

[[系统当前的总会话数]{style="font-family:宋体"}]{#struct_0_86917_x8972_2078245275}

[[TCP sessions]{lang="EN-US"}]{#struct_0_86917_x8972_321304386}

[[系统当前的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_529702604}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[UDP sessions]{lang="EN-US"}]{#struct_0_86917_x8972_1626353883}

[[系统当前的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_86917_x8972_1916244427}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[ICMP sessions]{lang="EN-US"}]{#struct_0_86917_x8972_635951057}

[[系统当前的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_86917_x8972_x1081866560}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[ICMPv6 sessions]{lang="EN-US"}]{#struct_0_86917_x8972_321369922}

[[系统当前的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_86917_x8972_x1105711836}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[UDP-Lite sessions]{lang="EN-US"}]{#struct_0_86917_x8972_1383521446}

[[系统当前的]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}]{#struct_0_86917_x8972_1901914982}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[SCTP sessions]{lang="EN-US"}]{#struct_0_86917_x8972_x1016007369}

[[系统当前的]{style="font-family:宋体"}[SCTP]{lang="EN-US"}]{#struct_0_86917_x8972_2045562639}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[DCCP sessions]{lang="EN-US"}]{#struct_0_86917_x8972_321697602}

[[系统当前的]{style="font-family:宋体"}[DCCP]{lang="EN-US"}]{#struct_0_86917_x8972_x1718360908}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[RAWIP sessions]{lang="EN-US"}]{#struct_0_86917_x8972_1404134069}

[[系统当前的]{style="font-family:宋体"}[Raw IP]{lang="EN-US"}]{#struct_0_86917_x8972_2024470073}[会话数，以及各协议状态下的会话数]{style="font-family:宋体"}

[[Current ]{lang="EN-US"}[relation-table entries]{lang="EN-US"}]{#struct_0_86917_x8972_x307288094}

[[总关联表项个数]{style="font-family:宋体"}]{#struct_0_86917_x8972_321763138}

[[Session establishment rate]{lang="EN-US"}]{#struct_0_86917_x8972_1051560002}

[[系统创建会话的速率，以及创建各协议会话的速率]{style="font-family:宋体"}]{#struct_0_86917_x8972_965026926}

[[Received TCP]{lang="EN-US"}]{#struct_0_86917_x8972_1315468057}

[[系统当前收到的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_2086316404}[报文数、报文字节数]{style="font-family:宋体"}

[[Received UDP]{lang="EN-US"}]{#struct_0_86917_x8972_321173315}

[[系统当前收到的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_86917_x8972_x532242694}[报文数、报文字节数]{style="font-family:宋体"}

[[Received ICMP]{lang="EN-US"}]{#struct_0_86917_x8972_1038076703}

[[系统当前收到的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_86917_x8972_1891380197}[报文数、报文字节数]{style="font-family:宋体"}

[[Received ICMPv6]{lang="EN-US"}]{#struct_0_86917_x8972_x2024056631}

[[系统当前收到的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_86917_x8972_321238851}[报文数、报文字节数]{style="font-family:宋体"}

[[Received UDP-Lite]{lang="EN-US"}]{#struct_0_86917_x8972_x1501650661}

[[系统当前收到的]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}]{#struct_0_86917_x8972_x930656689}[报文数、报文字节数]{style="font-family:宋体"}

[[Received SCTP]{lang="EN-US"}]{#struct_0_86917_x8972_x1553073753}

[[系统当前收到的]{style="font-family:宋体"}[SCTP]{lang="EN-US"}]{#struct_0_86917_x8972_321042243}[报文数、报文字节数]{style="font-family:宋体"}

[[Received DCCP]{lang="EN-US"}]{#struct_0_86917_x8972_x1310518290}

[[系统当前收到的]{style="font-family:宋体"}[DCCP]{lang="EN-US"}]{#struct_0_86917_x8972_x1171663929}[报文数、报文字节数]{style="font-family:宋体"}

[[Received RAWIP]{lang="EN-US"}]{#struct_0_86917_x8972_301863362}

[[系统当前收到的]{style="font-family:宋体"}[Raw IP]{lang="EN-US"}]{#struct_0_86917_x8972_321107779}[报文数、报文字节数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1826680817}[显示所有会话统计信息的概要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display session statistics summary]{lang="EN-US"}]{#struct_0_86917_x8972_x236093476}

[Sessions  TCP       UDP       Rate      TCP rate  UDP rate]{lang="EN-US"}

[3         0         0         0/s       0/s       0/s]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_316167751}[显示会话统计信息的概要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display session statistics summary]{lang="EN-US"}]{#struct_0_86917_x8972_x2008843320}

[Slot CPU Sessions  TCP       UDP       Rate      TCP rate  UDP rate]{lang="EN-US"}

[2    1   3         0         0         0/s       0/s       0/s]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x761872636}[显示会话统计信息的概要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display session statistics summary]{lang="EN-US"}]{#struct_0_86917_x8972_x1826615281}

[Chassis Slot CPU Sessions  TCP       UDP       Rate      TCP rate  UDP rate]{lang="EN-US"}

[1       2    1   3         0         0         0/s       0/s       0/s]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display session statistics summary]{lang="EN-US"}]{#struct_0_86917_x8972_x1629719727}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_623643715}[[字段]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1408334539}

[[描述]{style="font-family:黑体"}]{#struct_0_86917_x8972_x232543482}

[[Chassis]{lang="EN-US"}]{#struct_0_86917_x8972_x1738057961}

[[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_x1826549745}[成员编号]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_86917_x8972_1059653595}

[[单板所在的槽位号（]{style="font-family:宋体"}]{#struct_0_86917_x8972_x331102459}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_x1825959921}[中的成员编号（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_86917_x8972_1192558471}

[[CPU]{lang="EN-US"}]{#struct_0_86917_x8972_x2060209363}[编号]{style="font-family:宋体"}

[[Sessions]{lang="EN-US"}]{#struct_0_86917_x8972_1368169904}

[[系统当前的总会话数]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1825894385}

[[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_1590911149}

[[系统当前的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_x1873616146}[会话数]{style="font-family:宋体"}

[[UDP]{lang="EN-US"}]{#struct_0_86917_x8972_175355663}

[[系统当前的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_86917_x8972_x1826484210}[会话数]{style="font-family:宋体"}

[[Rate]{lang="EN-US"}]{#struct_0_86917_x8972_x108143197}

[[系统创建会话的速率]{style="font-family:宋体"}]{#struct_0_86917_x8972_246971453}

[[TCP rate]{lang="EN-US"}]{#struct_0_86917_x8972_x1826418674}

[[系统创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_x1723913138}[会话的速率]{style="font-family:宋体"}

[[UDP rate]{lang="EN-US"}]{#struct_0_86917_x8972_x23966499}

[[系统创建]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_86917_x8972_x1826353138}[会话的速率]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#2070092156 .myid}
[]{#_Toc404793551}[]{#struct_0_86917_x8972_1402368325}

**会话管理 \-- 会话管理配置命令 \-- display session table ipv4**

------------------------------------------------------------------------

[**[display session table ipv4]{lang="EN-US"}**]{#struct_0_86917_x8972_x1776367385}[命令用来显示]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[会话表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_755666941}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1096205662}

[**[display session table]{lang="EN-US"}**[ **ipv4** \[ **source-ip** *start*-*source-ip* \[ *end-source-ip* \] \] \[ **destination-ip** *start*-*destination-ip* \[ *end-destination-ip* \] \] \[ **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_86917_x8972_560171021}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_191697803}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display session table]{lang="EN-US"}**[ **ipv4** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *start*-*source-ip* \[ *end-source-ip* \] \] \[ **destination-ip** *start*-*destination-ip* \[ *end-destination-ip* \] \] \[ **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_86917_x8972_x2094552875}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_1415525449}[模式：]{style="font-family:宋体"}

[**[display session table]{lang="EN-US"}**[ **ipv4** \[ ]{lang="EN-US"}]{#struct_0_86917_x8972_x2144837041}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *start*-*source-ip* \[ *end-source-ip* \] \] \[ **destination-ip** *start*-*destination-ip* \[ *end-destination-ip* \] \] \[ **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_321435459}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x2019307849}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_2114506557}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1055646208}

[[network-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x1600755411}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1277557167}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x233997467}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1760918239}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1821697703}[：显示指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_321500995}[：显示指定成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_x1660115119}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x13488933}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x144354381}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_717959972}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**[ *start*-*source-ip* \[ *end-source-ip* \]]{lang="EN-US"}]{#struct_0_86917_x8972_365171541}[：显示指定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的会话表项。其中，]{style="font-family:宋体"}*[start]{lang="EN-US"}*[-*source-ip*]{lang="EN-US"}[表示发起方到响应方会话的起始源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[end-source-ip]{lang="EN-US"}*[表示发起方到响应方会话的结束源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}**[ *start*-*destination-ip* \[ *end-destination-ip* \]]{lang="EN-US"}]{#struct_0_86917_x8972_x975514199}[：显示指定目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的会话表项。其中，]{style="font-family:宋体"}*[start]{lang="EN-US"}*[-*destination-ip*]{lang="EN-US"}[表示发起方到响应方会话的起始目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[end-destination-ip]{lang="EN-US"}*[表示发起方到响应方会话的结束目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**[ { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]{lang="EN-US"}]{#struct_0_86917_x8972_x1826615282}[：显示指定协议类型的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[传输层协议类型可包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[、]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**[ *source-port*]{lang="EN-US"}]{#struct_0_86917_x8972_x1226435200}[：显示指定源端口号的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[source-port]{lang="EN-US"}*[表示发起方到响应方会话的源端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**[ *destination-port*]{lang="EN-US"}]{#struct_0_86917_x8972_1958407226}[：显示指定目的端口号的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[destination-port]{lang="EN-US"}*[表示发起方到响应方会话的目的端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_86917_x8972_1506202837}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项的详细信息。不指定该参数时，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项的概要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1365129972}

[[如果不指定任何参数，则显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_86917_x8972_321304387}[会话表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_529702603}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_1626353888}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项的概要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv4]{lang="EN-US"}]{#struct_0_86917_x8972_1915785675}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1877]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/22]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: TCP(6)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1792]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/2048]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: ICMP(1)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Total sessions found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1169857892}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项的概要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv4]{lang="EN-US"}]{#struct_0_86917_x8972_321369923}

[Slot 1:]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1877]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/22]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: TCP(6)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1792]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/2048]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: ICMP(1)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Total sessions found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1105711837}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项的详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv4 verbose]{lang="EN-US"}]{#struct_0_86917_x8972_321763139}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: ICMP_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         60 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_86917_x8972_1051560001}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="FR"}[会话表项的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="FR"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv4 verbose]{lang="EN-US"}]{#struct_0_86917_x8972_1887322795}

[Slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/- ]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: ICMP_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         60 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_86917_x8972_x1424978184}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="FR"}[会话表项的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="FR"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv4 verbose]{lang="EN-US"}]{#struct_0_86917_x8972_717632290}

[CPU 0 on slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/- ]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: ICMP_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         60 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[表1-6 ]{lang="EN-US"}[display session table]{lang="EN-US"}]{#struct_0_86917_x8972_1411139218}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x71372519}[[字段]{style="font-family:黑体"}]{#struct_0_86917_x8972_x739101372}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887584939}

[[Initiator]{lang="EN-US"}]{#struct_0_86917_x8972_1329613114}

[[发起方到响应方的连接对应的会话信息]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1743416978}

[[Responder]{lang="FR"}]{#struct_0_86917_x8972_371346661}

[[响应方到发起方的连接对应的会话信息]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1593645475}

[[Source IP/port]{lang="EN-US"}]{#struct_0_86917_x8972_x1015265664}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86917_x8972_1887388331}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Destination IP/port]{lang="FR"}]{#struct_0_86917_x8972_1031590592}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86917_x8972_x1862331263}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_86917_x8972_1342494482}

[[DS-Lite]{lang="FR"}]{#struct_0_86917_x8972_1887453867}[隧道对端地址。会话不属于任何]{style="font-family:宋体"}[DS-Lite]{lang="FR"}[隧道时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[本字段显示为]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="FR"}["]{style="font-family:宋体"}

[[VPN instance/VLAN ID/VLL ID]{lang="FR"}]{#struct_0_86917_x8972_x1404763567}

[[会话所属的]{style="font-family:宋体"}[MPLS L3VPN/]{lang="EN-US"}]{#struct_0_86917_x8972_1864106171}[二层转发时会话所属的]{style="font-family:宋体"}[VLAN ID/]{lang="EN-US"}[二层转发时会话所属的]{style="font-family:宋体"}[INLINE]{lang="EN-US"}[。未指定的参数则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_86917_x8972_1170607954}

[[传输层协议类型，取值包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}]{#struct_0_86917_x8972_1887781547}[、]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[Raw IP]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}

[[括号中的数字表示协议号]{style="font-family:宋体"}]{#struct_0_86917_x8972_x560469072}

[[Inbound interface]{lang="FR"}]{#struct_0_86917_x8972_837031114}

[[报文的入接口]{style="font-family:宋体"}]{#struct_0_86917_x8972_837096650}

[[Source security zone]{lang="FR"}]{#struct_0_86917_x8972_327617369}

[[源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_86917_x8972_433222294}["]{style="font-family:宋体"}

[[该参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_86917_x8972_433287830}

[[State]{lang="EN-US"}]{#struct_0_86917_x8972_498069773}

[[会话状态]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_86917_x8972_x1193885431}

[[Application]{lang="EN-US"}]{#struct_0_86917_x8972_1056463684}

[[应用层协议类型，取值包括：]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_86917_x8972_1887847083}[、]{style="font-family:宋体"}[DNS]{lang="EN-US"}[等，]{style="font-family:宋体"}[OTHER]{lang="FR"}[表示未知协议类型，其对应的端口为非知名端口]{style="font-family:宋体"}

[[Start time]{lang="FR"}]{#struct_0_86917_x8972_x613428157}

[[会话创建时间]{style="font-family:宋体"}]{#struct_0_86917_x8972_x596478087}

[[TTL]{lang="EN-US"}]{#struct_0_86917_x8972_x1023704748}

[[会话剩余存活时间，单位为秒]{style="font-family:宋体"}]{#struct_0_86917_x8972_746668817}

[[Initiator-\>Responder]{lang="FR"}]{#struct_0_86917_x8972_2094361917}

[[发起方到响应方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_86917_x8972_1887322796}

[[Responder-\>Initiator]{lang="FR"}]{#struct_0_86917_x8972_x560820648}

[[响应方到发起方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_86917_x8972_1264067011}

[[Total sessions found]{lang="EN-US"}]{#struct_0_86917_x8972_918324232}

[[当前查找到的会话表项总数]{style="font-family:宋体"}]{#struct_0_86917_x8972_1887126188}

[ ]{lang="EN-US"}

::: {#2070223228 .myid}
[]{#_Toc404793552}[]{#struct_0_86917_x8972_x1826484212}

**会话管理 \-- 会话管理配置命令 \-- display session table ipv6**

------------------------------------------------------------------------

[**[display session table ipv6]{lang="EN-US"}**]{#struct_0_86917_x8972_x1826418676}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[会话表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1408254744}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_x200870244}

[**[display session table]{lang="EN-US"}**[ **ipv6** \[ **source-ip** *start*-*source-ip* \[ *end-source-ip* \] \] \[ **destination-ip** *start*-*destination-ip* \[ *end-destination-ip* \] \] \[ **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_86917_x8972_x1076629022}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_x600511312}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display session table]{lang="EN-US"}**[ **ipv6** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *start*-*source-ip* \[ *end-source-ip* \] \] \[ **destination-ip** *start*-*destination-ip* \[ *end-destination-ip* \] \] \[ **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_86917_x8972_x585603620}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_1251201166}[模式：]{style="font-family:宋体"}

[**[display session table]{lang="EN-US"}**[ **ipv6** \[ ]{lang="EN-US"}]{#struct_0_86917_x8972_x1826353140}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *start*-*source-ip* \[ *end-source-ip* \] \] \[ **destination-ip** *start*-*destination-ip* \[ *end-destination-ip* \] \] \[ **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1441499971}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1413718846}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1095445609}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_29730031}

[[network-operator]{lang="EN-US"}]{#struct_0_86917_x8972_959945092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x98011694}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86917_x8972_x27447911}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x447420149}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1826287604}[：显示指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1472465723}[：显示指定成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_712472340}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1451266646}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x139430042}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1121348021}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**[ *start*-*source-ip* \[ *end-source-ip* \]]{lang="EN-US"}]{#struct_0_86917_x8972_94099677}[：显示指定源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的会话表项。其中，]{style="font-family:宋体"}*[start]{lang="EN-US"}*[-*source-ip*]{lang="EN-US"}[表示发起方到响应方会话的起始源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[end-source-ip]{lang="EN-US"}*[表示发起方到响应方会话的结束源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}**[ *destination-ip-start* \[*destination-ip-end* \]]{lang="EN-US"}]{#struct_0_86917_x8972_x1895271697}[：显示指定目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的会话表项。其中，]{style="font-family:宋体"}*[start]{lang="EN-US"}*[-*destination-ip*]{lang="EN-US"}[表示发起方到响应方会话的起始目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[end-destination-ip]{lang="EN-US"}*[表示发起方到响应方会话的结束目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**[ { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]{lang="EN-US"}]{#struct_0_86917_x8972_x1249727700}[：显示指定协议类型的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[传输层协议类型可包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**[ *source-port*]{lang="EN-US"}]{#struct_0_86917_x8972_x1308836449}[：显示指定源端口号的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[source-port]{lang="EN-US"}*[表示发起方到响应方]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话的源端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**[ *destination-port*]{lang="EN-US"}]{#struct_0_86917_x8972_x1826746356}[：显示指定目的端口号的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[destination-port]{lang="EN-US"}*[表示发起方到响应方]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话的目的端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_86917_x8972_x8821336}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项的详细信息。不指定该参数时，显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项的概要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1221987953}

[[如果不指定任何参数，则显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86917_x8972_x1476555066}[会话表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x2118548471}

[[\# ]{lang="FR"}]{#struct_0_86917_x8972_x1201062859}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="FR"}[会话表项的概要信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv6]{lang="EN-US"}]{#struct_0_86917_x8972_x1826680820}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 2011::2/58473]{lang="EN-US"}

[  Destination IP/port: 2011::8/32768]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: IPV6-ICMP(58)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total sessions found: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x639312467}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项的概要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv6]{lang="EN-US"}]{#struct_0_86917_x8972_x1665807487}

[Slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 2011::2/58473]{lang="FR"}

[  Destination IP/port: 2011::8/32768]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  ]{lang="FR"}[Protocol: IPV6-ICMP(58)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total sessions found: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_1520028314}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项的详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv6 verbose]{lang="EN-US"}]{#struct_0_86917_x8972_x1826615284}

[Initiator:]{lang="FR"}

[  Source      IP/port: 2011::2/58473]{lang="FR"}

[  Destination IP/port: 2011::8/32768]{lang="FR"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: IPV6-ICMP(58)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 2011::8/58473]{lang="FR"}

[  Destination IP/port: 2011::2/33024]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: IPV6-ICMP(58)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: ICMPV6_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:23:41  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         104 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 1]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_86917_x8972_1905732682}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="FR"}[会话表项的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="FR"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv6 verbose]{lang="EN-US"}]{#struct_0_86917_x8972_x1826549748}

[Slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 2011::2/58473]{lang="FR"}

[  Destination IP/port: 2011::8/32768]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: IPV6-ICMP(58)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 2011::8/58473]{lang="FR"}

[  Destination IP/port: 2011::2/33024]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: IPV6-ICMP(58)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: ICMPV6_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:23:41  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         104 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 1]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_86917_x8972_1819168482}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="FR"}[会话表项的概要信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="FR"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv6]{lang="EN-US"}]{#struct_0_86917_x8972_x1274762794}

[CPU 0 on slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 2011::2/58473]{lang="FR"}

[  Destination IP/port: 2011::8/32768]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  ]{lang="FR"}[Protocol: IPV6-ICMP(58)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total sessions found: 1]{lang="EN-US"}

[[\# ]{lang="FR"}]{#struct_0_86917_x8972_x1825959924}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="FR"}[会话表项的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="FR"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display session table ipv6 verbose]{lang="EN-US"}]{#struct_0_86917_x8972_789273944}

[CPU 0 on slot 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 2011::2/58473]{lang="FR"}

[  Destination IP/port: 2011::8/32768]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: IPV6-ICMP(58)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: Trust]{lang="EN-US"}

[Responder:]{lang="FR"}

[  Source      IP/port: 2011::8/58473]{lang="FR"}

[  Destination IP/port: 2011::2/33024]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: IPV6-ICMP(58)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Local]{lang="EN-US"}

[State: ICMPV6_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:23:41  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         104 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 1]{lang="FR"}

[[表1-7 ]{lang="EN-US"}[display session table]{lang="EN-US"}]{#struct_0_86917_x8972_227157227}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_659063243}[[字段]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1825894388}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1826484213}

[[Initiator]{lang="EN-US"}]{#struct_0_86917_x8972_x1674227138}

[[发起方到响应方的连接对应的会话信息]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1826418677}

[[Responder]{lang="FR"}]{#struct_0_86917_x8972_x1826353141}

[[响应方到发起方的连接对应的会话信息]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1826287605}

[[Source IP/port]{lang="EN-US"}]{#struct_0_86917_x8972_x1256417632}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86917_x8972_x1826746357}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Destination IP/port]{lang="FR"}]{#struct_0_86917_x8972_x1826680821}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86917_x8972_926771474}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_86917_x8972_x1826615285}

[[DS-Lite]{lang="FR"}]{#struct_0_86917_x8972_x1826549749}[隧道对端地址。会话不属于任何]{style="font-family:宋体"}[DS-Lite]{lang="FR"}[隧道时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[本字段显示为]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="FR"}["]{style="font-family:宋体"}

[[VPN instance/VLAN ID/VLL ID]{lang="FR"}]{#struct_0_86917_x8972_x909714873}

[[会话所属的]{style="font-family:宋体"}[MPLS L3VPN/]{lang="EN-US"}]{#struct_0_86917_x8972_x1825959925}[二层转发时会话所属的]{style="font-family:宋体"}[VLAN ID/]{lang="EN-US"}[二层转发时会话所属的]{style="font-family:宋体"}[INLINE]{lang="EN-US"}[。未指定的参数则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_86917_x8972_x1825894389}

[[传输层协议类型，取值包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}]{#struct_0_86917_x8972_x22226959}[、]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[Raw IP]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}

[[括号中的数字表示协议号]{style="font-family:宋体"}]{#struct_0_86917_x8972_535486419}

[[Inbound interface]{lang="FR"}]{#struct_0_86917_x8972_535420883}

[[报文的入接口]{style="font-family:宋体"}]{#struct_0_86917_x8972_x799360732}

[[Source security zone]{lang="FR"}]{#struct_0_86917_x8972_535617491}

[[源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_86917_x8972_535551955}["]{style="font-family:宋体"}

[[该参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_86917_x8972_535748563}

[[State]{lang="EN-US"}]{#struct_0_86917_x8972_x498283125}

[[会话状态]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_86917_x8972_535683027}

[[Application]{lang="EN-US"}]{#struct_0_86917_x8972_535879635}

[[应用层协议类型，取值包括：]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_86917_x8972_x311928561}[、]{style="font-family:宋体"}[DNS]{lang="EN-US"}[等，]{style="font-family:宋体"}[OTHER]{lang="FR"}[表示未知协议类型，其对应的端口为非知名端口]{style="font-family:宋体"}

[[Start time]{lang="FR"}]{#struct_0_86917_x8972_535814099}

[[会话创建时间]{style="font-family:宋体"}]{#struct_0_86917_x8972_536010707}

[[TTL]{lang="EN-US"}]{#struct_0_86917_x8972_174224097}

[[会话剩余存活时间，单位为秒]{style="font-family:宋体"}]{#struct_0_86917_x8972_535945171}

[[Initiator-\>Responder]{lang="FR"}]{#struct_0_86917_x8972_535486418}

[[发起方到响应方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_86917_x8972_391135281}

[[Responder-\>Initiator]{lang="FR"}]{#struct_0_86917_x8972_535420882}

[[响应方到发起方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_86917_x8972_535617490}

[[Total sessions found]{lang="EN-US"}]{#struct_0_86917_x8972_535551954}

[[当前查找到的会话表项总数]{style="font-family:宋体"}]{#struct_0_86917_x8972_1503937715}

[ ]{lang="EN-US"}

::: {#2038896869 .myid}
[]{#_Toc404793553}[]{#struct_0_86917_x8972_x1383047039}

**会话管理 \-- 会话管理配置命令 \-- reset session table ipv4**

------------------------------------------------------------------------

[**[reset session table ipv4]{lang="EN-US"}**]{#struct_0_86917_x8972_x2000244982}[命令用来删除]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_823568072}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_440938084}

[**[reset session]{lang="EN-US"}**[ **table ipv4** \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}]{#struct_0_86917_x8972_x1431564604}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_1136680448}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset session table]{lang="EN-US"}**[ **ipv4** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port**  *source-port* \] \[ **destination-port** *destination-port* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86917_x8972_1817646293}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_1887191724}[模式：]{style="font-family:宋体"}

[**[reset session table]{lang="EN-US"}**[ **ipv4** \[ ]{lang="EN-US"}]{#struct_0_86917_x8972_x936776724}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **protocol** { **dccp** \| **icmp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port**  *source-port* \] \[ **destination-port** *destination-port* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x407373438}

[[用户视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_1559592041}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_699611955}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_125968727}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_676131979}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1600060049}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1505958896}[：删除指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，删除所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1887519404}[：删除指定成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，删除所有成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_x227659082}[：删除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，删除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1410680466}[：删除指定成员设备的指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x603841771}[：]{style="font-family:宋体"}[删除指定单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，删除所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_717894432}[：删除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**[ *source-ip*]{lang="EN-US"}]{#struct_0_86917_x8972_x315620131}[：删除指定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[表示发起方到响应方会话的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}**[ *destination-ip*]{lang="EN-US"}]{#struct_0_86917_x8972_x617360676}[：删除指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[destination-ip]{lang="EN-US"}*[表示发起方到响应方会话的目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**[ { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]{lang="EN-US"}]{#struct_0_86917_x8972_783733332}[：删除指定协议类型的会话表项。其中，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[传输层协议类型可包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[、]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**[ *source-port*]{lang="EN-US"}]{#struct_0_86917_x8972_x1727107123}[：删除指定源端口号的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[source-port]{lang="EN-US"}*[表示发起方到响应方会话的源端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**[ *destination-port*]{lang="EN-US"}]{#struct_0_86917_x8972_1785868613}[：删除指定目的端口号的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[destination-port]{lang="EN-US"}*[表示发起方到响应方会话的目的端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86917_x8972_x833171054}[：删除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，删除公网中的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x710251150}

[[如果不指定任何参数，则删除所有公网中的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_86917_x8972_224521717}[会话表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1262546951}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1273360696}[删除所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[\<Sysname\> reset session table ipv4]{lang="EN-US"}]{#struct_0_86917_x8972_x744729103}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x88134941}[删除所有发起方源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.10.10.10]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[\<Sysname\> reset session table ipv4 source-ip 10.10.10.10]{lang="EN-US"}]{#struct_0_86917_x8972_595727437}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887388332}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session table ipv4]{lang="EN-US"}**]{#struct_0_86917_x8972_1031525056}
:::

::: {#-1873733403 .myid}
[]{#_Toc404793554}[]{#struct_0_86917_x8972_496749934}

**会话管理 \-- 会话管理配置命令 \-- reset session table ipv6**

------------------------------------------------------------------------

[**[reset session table ipv6]{lang="EN-US"}**]{#struct_0_86917_x8972_150540052}[命令用来删除]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1298259097}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_1902987265}

[**[reset session]{lang="EN-US"}**[ **table ipv6** \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}]{#struct_0_86917_x8972_4685974}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_x292275851}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset session table ipv6 ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port**  *source-port* \] \[ **destination-port** *destination-port* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86917_x8972_1498841935}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_1887453868}[模式：]{style="font-family:宋体"}

[**[reset session table]{lang="EN-US"}**[ **ipv6** \[ ]{lang="EN-US"}]{#struct_0_86917_x8972_x1404698031}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **source-ip** *source-ip* \] \[ **destination-ip** *destination-ip* \] \[ **protocol** { **dccp** \| **icmpv6**  \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_2115767245}

[[用户视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_680553764}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_2014274413}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_74304207}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1256588436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1958463813}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x485505349}[：删除指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，删除所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1846512598}[：删除指定成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，删除所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_x987173969}[：删除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，删除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1887781548}[：删除指定成员设备的指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_342806470}[：]{style="font-family:宋体"}[删除指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，删除所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x2010923382}[：删除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**[ *source-ip*]{lang="EN-US"}]{#struct_0_86917_x8972_x561058896}[：删除指定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[表示发起方到响应方会话的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}**[ *destination-ip*]{lang="EN-US"}]{#struct_0_86917_x8972_1308392320}[：删除指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[destination-ip]{lang="EN-US"}*[表示发起方到响应方会话的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**[ { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]{lang="EN-US"}]{#struct_0_86917_x8972_1275411161}[：删除指定协议类型的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[传输层协议类型可包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**[ *source-port*]{lang="EN-US"}]{#struct_0_86917_x8972_313835494}[：删除指定源端口号的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[source-port]{lang="EN-US"}*[表示发起方到响应方会话的源端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**[ *destination-port*]{lang="EN-US"}]{#struct_0_86917_x8972_x1098696248}[：删除指定目的端口号的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[destination-port]{lang="EN-US"}*[表示发起方到响应方会话的目的端口号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86917_x8972_210594004}[：删除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，删除公网中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_552539676}

[[如果不指定任何参数，则删除所有公网中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86917_x8972_x2144570156}[会话表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x529851834}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_828208761}[删除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[\<Sysname\> reset session table ipv6]{lang="EN-US"}]{#struct_0_86917_x8972_1327754957}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_1569480984}[删除所有发起方源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2011::0002]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[\<Sysname\> reset session table ipv6 source-ip 2011::0002]{lang="EN-US"}]{#struct_0_86917_x8972_x535407793}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_512066762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session table ipv6]{lang="EN-US"}**]{#struct_0_86917_x8972_1887257257}
:::

::: {#-700780411 .myid}
[]{#_Toc404793555}[]{#struct_0_86917_x8972_x990849656}[]{#_Toc311121249}[]{#_Toc313535381}[]{#_Toc311121250}[]{#_Toc313535382}[]{#_Toc311121251}[]{#_Toc313535383}[]{#_Toc311121252}[]{#_Toc313535384}[]{#_Toc311121253}[]{#_Toc313535385}[]{#_Toc311121254}[]{#_Toc313535386}[]{#_Toc311121255}[]{#_Toc313535387}[]{#_Toc311121256}[]{#_Toc313535388}[]{#_Toc311121257}[]{#_Toc313535389}[]{#_Toc311121258}[]{#_Toc313535390}[]{#_Toc311121259}[]{#_Toc313535391}[]{#_Toc311121260}[]{#_Toc313535392}[]{#_Toc311121261}[]{#_Toc313535393}[]{#_Toc311121262}[]{#_Toc313535394}[]{#_Toc311121263}[]{#_Toc313535395}[]{#_Toc311121264}[]{#_Toc313535396}[]{#_Toc311121265}[]{#_Toc313535397}[]{#_Toc311121266}[]{#_Toc313535398}[]{#_Toc311121267}[]{#_Toc313535399}[]{#_Toc311121268}[]{#_Toc313535400}[]{#_Toc311121269}[]{#_Toc313535401}[]{#_Toc311121270}[]{#_Toc313535402}[]{#_Toc311121271}[]{#_Toc313535403}[]{#_Toc311121272}[]{#_Toc313535404}[]{#_Toc311121273}[]{#_Toc313535405}[]{#_Toc311121274}[]{#_Toc313535406}[]{#_Toc311121275}[]{#_Toc313535407}[]{#_Toc311121276}[]{#_Toc313535408}[]{#_Toc311121277}[]{#_Toc313535409}[]{#_Toc311121278}[]{#_Toc313535410}[]{#_Toc311121279}[]{#_Toc313535411}[]{#_Toc311121280}[]{#_Toc313535412}[]{#_Toc311121281}[]{#_Toc313535413}

**会话管理 \-- 会话管理配置命令 \-- reset session table**

------------------------------------------------------------------------

[**[reset session table]{lang="EN-US"}**]{#struct_0_86917_x8972_x640676559}[命令用来删除所有会话表项，包括]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_852710898}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_x191892889}

[**[reset session table]{lang="EN-US"}**]{#struct_0_86917_x8972_1171602811}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_119283194}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset session table ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_86917_x8972_1450173198}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_1887322793}[模式：]{style="font-family:宋体"}

[**[reset session table ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_86917_x8972_x561148328}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_886864874}

[[用户视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_1334364223}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x2044443948}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x616228434}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x2036369711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1768539599}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1596897560}[：删除指定单板上的所有会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，删除所有单板上的所有会话表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x1827500004}[：删除指定成员设备上的所有会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，删除所有成员设备上的所有会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_x1746688856}[：删除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的所有会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，删除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的所有会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1887126185}[：删除指定成员设备的指定单板上的所有会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的所有会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x953046388}[：]{style="font-family:宋体"}[删除指定单板上的所有会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，删除所有单板上的所有会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x2011119991}[：删除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有会话表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x2016511648}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1318620566}[删除所有会话表项。]{style="font-family:宋体"}

[[\<Sysname\> reset session table]{lang="EN-US"}]{#struct_0_86917_x8972_1887191721}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x936449044}[]{#_Toc311106992}[]{#_Toc311107018}[]{#_Toc311119669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session table]{lang="EN-US"}**]{#struct_0_86917_x8972_x814279980}[]{#_Toc311106993}[]{#_Toc311107019}[]{#_Toc311119670}**[ ipv4]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session table]{lang="EN-US"}**]{#struct_0_86917_x8972_221643312}[]{#_Toc311106994}[]{#_Toc311107020}[]{#_Toc311119671}**[ ipv6]{lang="EN-US"}**
:::

::: {#794645278 .myid}
[]{#_Toc404793556}[]{#struct_0_86917_x8972_x130573479}

**会话管理 \-- 会话管理配置命令 \-- reset session statistics**

------------------------------------------------------------------------

[**[reset session statistics]{lang="EN-US"}**]{#struct_0_86917_x8972_x2074585326}[命令用来清除会话统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x701261979}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1558289067}

[**[reset session statistics]{lang="EN-US"}**]{#struct_0_86917_x8972_65054796}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_294137015}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset session statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_86917_x8972_1887519401}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_1411008146}[模式：]{style="font-family:宋体"}

[**[reset session statistics]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_86917_x8972_x725767679}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1747809056}

[[用户视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_2065754685}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x905569904}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_272829110}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_720214967}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x2024397897}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1887584937}[：清除指定单板的上会话统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，清除所有单板上的会话统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1330268474}[：清除指定成员设备上的会话统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，清除所有成员设备上的会话统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_x1390524032}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的会话统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的会话统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x280184266}[：清除指定成员设备的指定单板上的会话统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，清除所有成员设备的所有单板上的会话统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1448467392}[：]{style="font-family:宋体"}[清除指定单板上的会话统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，清除所有单板上的会话统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x2010923384}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的会话统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_194111636}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1189181417}[清除所有的会话统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset session statistics]{lang="EN-US"}]{#struct_0_86917_x8972_1887388329}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1031066303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session statistics]{lang="EN-US"}**]{#struct_0_86917_x8972_x1871827995}
:::

::: {#-1509936691 .myid}
[]{#_Toc404793557}[]{#struct_0_86917_x8972_x1128324219}

**会话管理 \-- 会话管理配置命令 \-- reset session relation-table**

------------------------------------------------------------------------

[**[reset session]{lang="EN-US"}**[ **relation-table**]{lang="EN-US"}]{#struct_0_86917_x8972_x447172303}[命令用来删除关联表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_605169557}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86917_x8972_1391705946}

[**[reset session]{lang="EN-US"}**[ **relation-table** \[ **ipv4** \| **ipv6** \] ]{lang="EN-US"}]{#struct_0_86917_x8972_x526666207}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86917_x8972_x1287251869}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset session]{lang="EN-US"}**[ **relation-table** \[ **ipv4** \| **ipv6** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_86917_x8972_1887453865}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_86917_x8972_x1404894639}[模式：]{style="font-family:宋体"}

[**[reset session]{lang="EN-US"}**[ **relation-table** \[ **ipv4** \| **ipv6** \] \[ ]{lang="EN-US"}]{#struct_0_86917_x8972_1923199147}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1275809080}

[[用户视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1996744044}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1964800752}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_359379264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1228773605}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887781545}

[**[ipv4]{lang="EN-US"}**]{#struct_0_86917_x8972_x560338000}[：删除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[关联表项。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86917_x8972_2049014826}[：删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[关联表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_276915435}[：删除指定单板上的关联表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，删除所有单板上的关联表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1887847081}[：删除指定成员设备上的关联表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，删除所有成员设备上的关联表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_86917_x8972_x227724618}[：删除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的关联表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，删除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的关联表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x613297085}[：删除指定成员设备上指定单板的关联表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的关联表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_86917_x8972_1442983696}[：]{style="font-family:宋体"}[删除指定单板上的关联表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，删除所有单板上的关联表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_86917_x8972_x2010792313}[：删除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的关联表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x201439603}

[[如果不指定]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**]{#struct_0_86917_x8972_x1493890347}[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[，则删除所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[关联表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1823361028}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x858019680}[删除所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[关联表项。]{style="font-family:宋体"}

[[\<Sysname\> reset session relation-table ipv4]{lang="EN-US"}]{#struct_0_86917_x8972_1887257258}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x990784120}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session relation-table]{lang="EN-US"}**]{#struct_0_86917_x8972_x309987146}
:::

::: {#1812424295 .myid}
[]{#_Toc404793558}[]{#struct_0_86917_x8972_x1471393900}

**会话管理 \-- 会话管理配置命令 \-- session aging-time application**

------------------------------------------------------------------------

[**[session aging-time application]{lang="EN-US"}**]{#struct_0_86917_x8972_x2003694781}[命令用来设置应用层协议的会话老化时间。]{style="font-family:
宋体"}

[**[undo session aging-time application]{lang="EN-US"}**]{#struct_0_86917_x8972_231113063}[命令用来恢复缺省情况。如果不指定应用层协议类型，则将所有应用层协议的会话老化时间都恢复为缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_798029888}

[**[session aging-time application ]{lang="EN-US"}**[{ **dns** \| **ftp** \| **gtp** ]{lang="EN-US"}]{#struct_0_86917_x8972_427145434}[\|]{lang="ES-AR"}[ ]{lang="ES-AR"}**[h225]{lang="EN-US"}**[ \| **h245** \| **ils** \| **mgcp** \| **nbt** \| **pptp** \| **ras** \| **rsh** \| **rtsp** ]{lang="EN-US"}[\|]{lang="ES-AR"}[ ]{lang="ES-AR"}**[sccp]{lang="EN-US"}**[ \| **sip** ]{lang="EN-US"}[\| **sqlnet** ]{lang="ES-AR"}[\|]{lang="EN-US"}[ ]{lang="EN-US"}**[tftp ]{lang="EN-US"}**[\| **xdmcp** } *time-value*]{lang="EN-US"}

[**[undo session aging-time application]{lang="EN-US"}**[ \[ **dns** \| **ftp** \| **gtp** ]{lang="EN-US"}]{#struct_0_86917_x8972_912454392}[\|]{lang="ES-AR"}[ ]{lang="ES-AR"}**[h225]{lang="EN-US"}**[ \| **h245** \| **ras** \| **rtsp** ]{lang="EN-US"}[\| ]{lang="ES-AR"}**[sip ]{lang="EN-US"}**[\| ]{lang="ES-AR"}**[tftp ]{lang="EN-US"}**[\]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887322794}

[[各应用层协议的会话老化时间为：]{style="font-family:宋体"}]{#struct_0_86917_x8972_x560951720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}**]{#struct_0_86917_x8972_2035127877}[：]{lang="EN-US" style="font-family:宋体"}[60]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ftp]{lang="EN-US"}**]{#struct_0_86917_x8972_665692769}[：]{lang="EN-US" style="font-family:宋体"}[3600]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gtp]{lang="EN-US"}**]{#struct_0_86917_x8972_x205137938}[：]{lang="EN-US" style="font-family:宋体"}[60]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[h225]{lang="EN-US"}**]{#struct_0_86917_x8972_656821935}[：]{lang="EN-US" style="font-family:宋体"}[3600]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[h245]{lang="EN-US"}**]{#struct_0_86917_x8972_x457570870}[：]{lang="EN-US" style="font-family:宋体"}[3600]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ils]{lang="EN-US"}**]{#struct_0_86917_x8972_x203605243}[：]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[00]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mgcp]{lang="EN-US"}**]{#struct_0_86917_x8972_1752709893}[：]{lang="EN-US" style="font-family:宋体"}[6]{lang="EN-US"}[0]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nbt]{lang="EN-US"}**]{#struct_0_86917_x8972_216814835}[：]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[00]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pptp]{lang="EN-US"}**]{#struct_0_86917_x8972_1387504141}[：]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[00]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ras]{lang="EN-US"}**]{#struct_0_86917_x8972_x1267600787}[：]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rsh]{lang="EN-US"}**]{#struct_0_86917_x8972_x1064351433}[：]{lang="EN-US" style="font-family:宋体"}[6]{lang="EN-US"}[0]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rtsp]{lang="EN-US"}**]{#struct_0_86917_x8972_1887126186}[：]{lang="EN-US" style="font-family:宋体"}[3]{lang="PT-BR"}[6]{lang="EN-US"}[0]{lang="EN-US"}[0]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sccp]{lang="EN-US"}**]{#struct_0_86917_x8972_1204552712}[：]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[00]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sip]{lang="EN-US"}**]{#struct_0_86917_x8972_x1383178111}[：]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sqlnet]{lang="ES-AR"}**]{#struct_0_86917_x8972_1394752018}[：]{lang="EN-US" style="font-family:宋体"}[6]{lang="EN-US"}[00]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tftp]{lang="EN-US"}**]{#struct_0_86917_x8972_1737445304}[：]{lang="EN-US" style="font-family:宋体"}[60]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[xdmcp]{lang="EN-US"}**]{#struct_0_86917_x8972_x1960218857}[：]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[00]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x2063348337}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1033924467}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1874328869}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1152495189}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1740355194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1736982192}

[**[dns]{lang="EN-US"}**]{#struct_0_86917_x8972_1887191722}[：表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[ftp]{lang="EN-US"}**]{#struct_0_86917_x8972_x936383508}[：表示]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[gtp]{lang="EN-US"}**]{#struct_0_86917_x8972_x1175759155}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[GTP]{lang="PT-BR"}[（]{style="font-family:宋体"}[GPRS Tunneling Protocol]{lang="PT-BR"}[，]{style="font-family:宋体"}[GPRS]{lang="PT-BR"}[隧道协议）]{style="font-family:宋体"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[h225]{lang="EN-US"}**]{#struct_0_86917_x8972_1214488931}[：表示]{style="font-family:宋体"}[H.225]{lang="EN-US"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[h245]{lang="EN-US"}**]{#struct_0_86917_x8972_x1995462278}[：表示]{style="font-family:宋体"}[H.245]{lang="EN-US"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[ils]{lang="ES-AR"}**]{#struct_0_86917_x8972_178731781}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ILS]{lang="EN-US"}[（]{style="font-family:宋体"}[Internet Locator Service]{lang="EN-US"}[，互联网定位服务）协议的会话老化时间。]{style="font-family:宋体"}

[**[mgcp]{lang="ES-AR"}**]{#struct_0_86917_x8972_x216083100}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MGCP]{lang="EN-US"}[（]{style="font-family:宋体"}[Media Gateway Control Protocol]{lang="EN-US"}[，媒体网关控制协议）协议的会话老化时间。]{style="font-family:宋体"}

[**[nbt]{lang="ES-AR"}**]{#struct_0_86917_x8972_x151227416}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[NBT]{lang="EN-US"}[（]{style="font-family:宋体"}[NetBIOS over TCP/IP]{lang="EN-US"}[，基于]{style="font-family:宋体"}[TCP/IP]{lang="EN-US"}[的网络基本输入输出系统）协议的会话老化时间。]{style="font-family:宋体"}

[**[pptp]{lang="ES-AR"}**]{#struct_0_86917_x8972_x1914715735}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[PPTP]{lang="EN-US"}[（]{style="font-family:宋体"}[Point-to-Point Tunneling Protocol]{lang="EN-US"}[，点到点隧道协议）协议的会话老化时间。]{style="font-family:宋体"}

[**[ras]{lang="EN-US"}**]{#struct_0_86917_x8972_x158251229}[：表示]{style="font-family:宋体"}[RAS]{lang="EN-US"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[rsh]{lang="ES-AR"}**]{#struct_0_86917_x8972_2135046917}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[RSH]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Shell]{lang="EN-US"}[，远程外壳）协议的会话老化时间。]{style="font-family:宋体"}

[**[rtsp]{lang="EN-US"}**]{#struct_0_86917_x8972_x1740276406}[：表示]{style="font-family:宋体"}[RTSP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Real Time Streaming Protocol]{lang="PT-BR"}[，实时流协议）协议]{style="font-family:宋体"}[的会话老化时间。]{style="font-family:宋体"}

[**[sccp]{lang="EN-US"}**]{#struct_0_86917_x8972_841162597}[：表示]{style="font-family:宋体"}[SCCP]{lang="EN-US"}[（]{style="font-family:宋体"}[Skinny Client Control Protocol]{lang="EN-US"}[，瘦小客户端控制协议）协议的会话老化时间。]{style="font-family:宋体"}

[**[sip]{lang="EN-US"}**]{#struct_0_86917_x8972_1957382481}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[sqlnet]{lang="ES-AR"}**]{#struct_0_86917_x8972_1273265220}[：表示]{style="font-family:宋体"}[SQLNET]{lang="EN-US"}[协议的会话老化时间。]{style="font-family:宋体"}

[**[tftp]{lang="EN-US"}**]{#struct_0_86917_x8972_156777462}[：表示]{style="font-family:宋体"}[TFTP]{lang="PT-BR"}[协议]{style="font-family:宋体"}[的会话老化时间。]{style="font-family:宋体"}

[**[xdmcp]{lang="EN-US"}**]{#struct_0_86917_x8972_30642968}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[XDMCP]{lang="EN-US"}[（]{style="font-family:宋体"}[X Display Manager Control Protocol]{lang="EN-US"}[，]{style="font-family:宋体"}[X]{lang="EN-US"}[显示监控）协议的会话老化时间。]{style="font-family:宋体"}

[*[time-value]{lang="EN-US"}*]{#struct_0_86917_x8972_2039021546}[：指定的老化时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1411073682}

[[应用层协议的会话老化时间仅在会话进入稳态时生效（]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_1280157516}[会话的稳态为]{style="font-family:宋体"}[TCP-EST]{lang="EN-US"}[，]{style="font-family:宋体"}[UDP]{lang="EN-US"}[会话的稳态为]{style="font-family:宋体"}[UDP-READY]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[会话进入稳态后，如果该会话属于本命令中指定的一种应用层协议，则此会话的老化时间为指定的应用层协议老化时间；否则为传输层协议状态的老化时间（由]{style="font-family:宋体"}**[session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_x1269312219}[命令配置）。]{style="font-family:
宋体"}

[[需要注意的是，对]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_1715222415}[会话来说，如果会话符合长连接会话的规则，那么该会话稳态的老化时间为长连接老化时间（由]{style="font-family:宋体"}**[session persistent acl]{lang="EN-US"}**[命令配置）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1037966385}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1833555258}[设置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的会话老化时间为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_1886596987}

[\[Sysname\] ]{lang="EN-US"}[session aging-time application ftp 1800]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1008295949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_86917_x8972_1887584938}**[session]{lang="EN-US"}[ aging-time application]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_1329678650}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session persist]{lang="EN-US"}**]{#struct_0_86917_x8972_977000561}**[ent]{lang="EN-US"}[ acl]{lang="EN-US"}**
:::

::: {#997283514 .myid}
[]{#_Toc404793559}[]{#struct_0_86917_x8972_2015080544}

**会话管理 \-- 会话管理配置命令 \-- session aging-time state**

------------------------------------------------------------------------

[**[session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_487061672}[命令用来设置各协议状态的会话老化时间。]{style="font-family:
宋体"}

[**[undo session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_797367406}[命令用来恢复缺省情况，如果不指定任何参数，则将所有协议状态的会话老化时间都恢复为缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x723718971}

[**[session aging-time state ]{lang="EN-US"}**[{ **fin** \| **icmp-reply** \| **icmp-request** \| **rawip-open** \| **rawip-ready** \| **syn** \| **tcp-est** \| **udp-open** \| **udp-ready** } *time-value*]{lang="EN-US"}]{#struct_0_86917_x8972_362784339}

[**[undo session aging-time state ]{lang="EN-US"}**[\[ **fin** \| **icmp-reply** \| **icmp-request** \| **rawip-open** \| **rawip-ready** \| **syn** \| **tcp-est** \| **udp-open** \| **udp-ready** \]]{lang="EN-US"}]{#struct_0_86917_x8972_1507559359}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887388330}

[[各协议状态的会话老化时间为：]{style="font-family:宋体"}]{#struct_0_86917_x8972_1031656128}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fin]{lang="EN-US"}**]{#struct_0_86917_x8972_2042506145}[：]{lang="EN-US" style="font-family:宋体"}[30]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-reply]{lang="EN-US"}**]{#struct_0_86917_x8972_x1991869478}[：]{lang="EN-US" style="font-family:宋体"}[30]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[icmp-request]{lang="EN-US"}**]{#struct_0_86917_x8972_x835828035}[：]{lang="EN-US" style="font-family:宋体"}[60]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rawip-open]{lang="EN-US"}**]{#struct_0_86917_x8972_x1651669008}[：]{lang="EN-US" style="font-family:宋体"}[30]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rawip-ready]{lang="EN-US"}**]{#struct_0_86917_x8972_1453313447}[：]{lang="EN-US" style="font-family:宋体"}[60]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[syn]{lang="EN-US"}**]{#struct_0_86917_x8972_2126563167}[：]{lang="EN-US" style="font-family:宋体"}[30]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tcp-est]{lang="EN-US"}**]{#struct_0_86917_x8972_1697285461}[：]{lang="EN-US" style="font-family:宋体"}[3600]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-open]{lang="EN-US"}**]{#struct_0_86917_x8972_x1014712639}[：]{lang="EN-US" style="font-family:宋体"}[30]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp-ready]{lang="EN-US"}**]{#struct_0_86917_x8972_1887453866}[：]{lang="EN-US" style="font-family:宋体"}[60]{lang="EN-US"}[秒]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1404829103}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x229028297}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1957864771}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_546328994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x2141908279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_102875164}

[**[fin]{lang="EN-US"}**]{#struct_0_86917_x8972_2145888286}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[协议]{style="font-family:宋体"}[FIN-WAIT]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[icmp-reply]{lang="EN-US"}**]{#struct_0_86917_x8972_721083181}[：表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[协议]{style="font-family:宋体"}[REPLY]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[icmp-request]{lang="EN-US"}**]{#struct_0_86917_x8972_1887781546}[：表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[协议]{style="font-family:宋体"}[REQUEST]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[rawip-open]{lang="EN-US"}**]{#struct_0_86917_x8972_x560403536}[：表示]{style="font-family:宋体"}[RAWIP-OPEN]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[rawip-ready]{lang="EN-US"}**]{#struct_0_86917_x8972_x717390057}[：表示]{style="font-family:宋体"}[RAWIP-READY]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[syn]{lang="EN-US"}**]{#struct_0_86917_x8972_1718866518}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[协议]{style="font-family:宋体"}[SYN-SENT]{lang="EN-US"}[和]{style="font-family:宋体"}[SYN-RCV]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[tcp-est]{lang="EN-US"}**]{#struct_0_86917_x8972_x56038061}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[协议]{style="font-family:宋体"}[ESTABLISHED]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[udp-open]{lang="EN-US"}**]{#struct_0_86917_x8972_1239818497}[：表示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议]{style="font-family:宋体"}[OPEN]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[**[udp-ready]{lang="EN-US"}**]{#struct_0_86917_x8972_1887847082}[：表示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议]{style="font-family:宋体"}[READY]{lang="EN-US"}[状态的会话老化时间。]{style="font-family:宋体"}

[*[time-value]{lang="EN-US"}*]{#struct_0_86917_x8972_x613362621}[：指定的老化时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_614525219}

[[会话进入稳态后，如果该会话属于]{style="font-family:宋体"}**[session aging-time application]{lang="EN-US"}**]{#struct_0_86917_x8972_779238626}[命令中指定的一种应用层协议，则此会话的老化时间为指定的应用层协议老化时间；否则为四层协议状态的老化时间（由]{style="font-family:宋体"}**[session aging-time state]{lang="EN-US"}**[命令配置）。]{style="font-family:宋体"}

[[需要注意的是，对]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_1887257255}[会话来说，如果会话符合长连接会话的规则，那么该会话稳态的老化时间为长连接老化时间（由]{style="font-family:宋体"}**[session persistent acl]{lang="EN-US"}**[命令配置）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x990980728}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_511846024}[设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[协议]{style="font-family:宋体"}[SYN-SENT]{lang="EN-US"}[和]{style="font-family:宋体"}[SYN-RCV]{lang="EN-US"}[状态的老化时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_1560343721}

[\[Sysname\] session aging-time state syn 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1090604611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_821111058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session aging-time application]{lang="EN-US"}**]{#struct_0_86917_x8972_x1704517931}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session persist]{lang="EN-US"}**]{#struct_0_86917_x8972_x1563656831}**[ent]{lang="EN-US"}[ acl]{lang="EN-US"}**
:::

::::: {#-1985534397 .myid}
[]{#_Toc404793560}[]{#struct_0_86917_x8972_1887322791}

**会话管理 \-- 会话管理配置命令 \-- session log bytes-active**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](会话管理命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86917_x8972_x561279400}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86917_x8972_510914660}
:::

[ ]{lang="EN-US"}

[**[session log bytes-active]{lang="EN-US"}**]{#struct_0_86917_x8972_x2096104451}[命令用来配置输出会话日志的字节数流量阈值。]{style="font-family:
宋体"}

[**[undo session log bytes-active]{lang="EN-US"}**]{#struct_0_86917_x8972_890710590}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1280935065}

[**[session log bytes-active]{lang="EN-US"}**[ *bytes-value*]{lang="EN-US"}]{#struct_0_86917_x8972_x1667318444}

[**[undo session log]{lang="EN-US"}**[ **bytes-active**]{lang="EN-US"}]{#struct_0_86917_x8972_x1934582850}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x199170554}

[[不依据字节数流量阈值发送会话日志。]{style="font-family:宋体"}]{#struct_0_86917_x8972_1887126183}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1383505791}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_1091578405}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1334332622}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x835334693}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1114574799}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1825691383}

[*[bytes-value]{lang="EN-US"}*]{#struct_0_86917_x8972_1783670849}[：表示发送会话日志的字节数阈值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为兆字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_875394859}

[[如果设置的字节数阈值为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_86917_x8972_1887191719}[，则一个会话每传输]{style="font-family:宋体"}*[n]{lang="EN-US"}*[兆个字节整数倍时，设备就输出一次相应的会话日志。]{style="font-family:宋体"}

[[同时配置了时间阈值和流量阈值的情况下，只要有一个阈值到达，就会输出相应的会话日志，并将所有的阈值统计信息清零。]{style="font-family:宋体"}]{#struct_0_86917_x8972_x936973329}

[[同时只能有一种流量阈值有效，以最后一次配置的阈值类型为准，例如，先配置报文数阈值再配置字节数阈值，则当前有效的阈值是字节数阈值，只会输出达到字节数阈值的会话日志。]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1575659631}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1428509556}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1472432096}[设置输出会话日志的字节数流量阈值为]{style="font-family:宋体"}[10]{lang="EN-US"}[兆字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_x113636769}

[\[Sysname\] session log bytes-active 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_804371479}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log enable]{lang="EN-US"}**]{#struct_0_86917_x8972_x46232857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log time-active]{lang="EN-US"}**]{#struct_0_86917_x8972_x199853038}
:::::

::::: {#1585794599 .myid}
[]{#_Toc404793561}[]{#struct_0_86917_x8972_1887519399}

**会话管理 \-- 会话管理配置命令 \-- session log enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](会话管理命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86917_x8972_x544782693}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86917_x8972_x1873926079}
:::

[ ]{lang="EN-US"}

[**[session log enable]{lang="EN-US"}**]{#struct_0_86917_x8972_700535106}[命令用来使能会话日志功能。]{style="font-family:宋体"}

[**[undo session log enable]{lang="EN-US"}**]{#struct_0_86917_x8972_x801603936}[命令]{style="font-family:宋体"}[用来关闭会话日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1567785722}

[**[session log enable ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **acl** *acl-number* \] { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_86917_x8972_x1276753383}

[**[undo session log enable ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **acl** *acl-number* \] { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_86917_x8972_267756941}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1525681974}

[[会话日志功能处于关闭状态]{style="font-family:宋体"}]{#struct_0_86917_x8972_1887584935}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1330399546}

[[接口视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x696957577}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_936942369}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x352596296}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1276065489}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_929665744}

[**[ipv4]{lang="EN-US"}**]{#struct_0_86917_x8972_x1132664150}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话日志。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86917_x8972_x772557183}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话日志。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_86917_x8972_1887388327}[：对与指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[相匹配的会话输出会话日志，其中]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_86917_x8972_1031721663}[：指定输出入方向的会话日志。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_86917_x8972_x1855283163}[：指定输出出方向的会话日志。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x415572667}

[[如果不指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_86917_x8972_1779296586}[，则表示允许输出经过接口的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话的日志。]{style="font-family:宋体"}

[[可配置仅输出单方向的会话日志，也可以配置输出双向的会话日志。每个方向上最多可以配置一个]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}]{#struct_0_86917_x8972_1855123682}[规则和一个]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[在未指定相关阈值（流量阈值、时间阈值）的情况下，若会话日志功能处于使能状态，则仅在会话表创建和删除的时候分别输出一次会话日志。]{style="font-family:宋体"}]{#struct_0_86917_x8972_x739981543}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_503869016}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x96992033}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口下开启会话日志功能，指定输出此接口入方向上的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话日志。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_1887453863}

[\[Sysname\] ]{lang="EN-US"}[interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] session log enable ipv4 inbound]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1405025711}[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[接口下开启会话日志功能，指定输出此接口出方向上匹配]{style="font-family:宋体"}[ACL 2050]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话日志。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_415577938}

[\[Sysname\] ]{lang="EN-US"}[interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] session log enable ipv4 acl 2050 outbound]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_1260011688}[在]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[接口下开启会话日志功能，指定输出此接口出方向上匹配]{style="font-family:宋体"}[ACL 2050]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话日志。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_44157023}

[\[Sysname\] ]{lang="EN-US"}[interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] session log enable ipv6 acl 2050 outbound]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1452143724}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log bytes-active]{lang="EN-US"}**]{#struct_0_86917_x8972_x410698343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log packets-active]{lang="EN-US"}**]{#struct_0_86917_x8972_1887781543}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log time-active]{lang="EN-US"}**]{#struct_0_86917_x8972_x560731216}
:::::

::::: {#51955204 .myid}
[]{#_Toc404793562}[]{#struct_0_86917_x8972_456431104}

**会话管理 \-- 会话管理配置命令 \-- session log packets-active**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](会话管理命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86917_x8972_1371452224}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86917_x8972_1890721211}
:::

[ ]{lang="EN-US"}

[**[session log packets-active]{lang="EN-US"}**]{#struct_0_86917_x8972_692577202}[命令用来配置输出会话日志的报文数流量阈值。]{style="font-family:
宋体"}

[**[undo session log packets-active]{lang="EN-US"}**]{#struct_0_86917_x8972_1936916108}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1551357250}

[**[session log packets-active ]{lang="EN-US"}***[packets-value]{lang="EN-US"}*]{#struct_0_86917_x8972_1887847079}

[**[undo session log]{lang="EN-US"}**[ **packets-active**]{lang="EN-US"}]{#struct_0_86917_x8972_x613821376}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_231104132}

[[不依据报文数流量阈值发送会话日志。]{style="font-family:宋体"}]{#struct_0_86917_x8972_805274635}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x317553936}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_1589736620}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_182411332}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1761579408}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_343810795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887257256}

[*[packets-value]{lang="EN-US"}*]{#struct_0_86917_x8972_x990915192}[：表示发送会话日志的报文数阈值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为兆包。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1240958052}

[[如果设置的报文数阈值为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_86917_x8972_x907417716}[，则一个会话每收发]{style="font-family:宋体"}*[n]{lang="EN-US"}*[兆个报文，设备就输出一次相应的会话日志。]{style="font-family:宋体"}

[[同时配置了时间阈值和流量阈值的情况下，只要有一个阈值到达，就会输出相应的会话日志，并将所有的阈值统计信息清零。]{style="font-family:宋体"}]{#struct_0_86917_x8972_1736003378}

[[同时只能有一种流量阈值有效，以最后一次配置的阈值类型为准，例如，先配置报文数阈值再配置字节数阈值，则当前有效的阈值是字节数阈值，只会输出达到字节数阈值的会话日志。]{style="font-family:宋体"}]{#struct_0_86917_x8972_1796966844}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1202962241}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_985016340}[设置输出会话日志的流量阈值为]{style="font-family:宋体"}[10]{lang="EN-US"}[兆报文数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_1887322792}

[\[Sysname\] session log packets-active 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x561082792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log enable]{lang="EN-US"}**]{#struct_0_86917_x8972_1609369998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log time-active]{lang="EN-US"}**]{#struct_0_86917_x8972_x794935946}
:::::

::::: {#1752809551 .myid}
[]{#_Toc404793563}[]{#struct_0_86917_x8972_x688946090}

**会话管理 \-- 会话管理配置命令 \-- session log time-active**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](会话管理命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86917_x8972_x141545845}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86917_x8972_x1670794398}
:::

[ ]{lang="EN-US"}

[**[session log time-active]{lang="EN-US"}**]{#struct_0_86917_x8972_1434964520}[命令用来配置输出会话日志的时间阈值。]{style="font-family:宋体"}

[**[undo session log time-active]{lang="EN-US"}**]{#struct_0_86917_x8972_1508327814}[用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1491370460}

[**[session log time-active ]{lang="EN-US"}***[time-value]{lang="EN-US"}*]{#struct_0_86917_x8972_1887126184}

[**[undo session log time-active]{lang="EN-US"}**]{#struct_0_86917_x8972_x1383309183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_659690325}

[[不依据时间阈值发送会话日志。]{style="font-family:宋体"}]{#struct_0_86917_x8972_108322306}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_324207387}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x953629006}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x837147896}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_189695032}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1260759164}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887191720}

[*[time-value]{lang="EN-US"}*]{#struct_0_86917_x8972_x936514580}[：表示发送会话日志的时间阈值，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为分钟，只能为]{style="font-family:宋体"}[10]{lang="EN-US"}[的整数倍。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1950019568}

[[如果设置的时间阈值为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_86917_x8972_x464992779}[，则每经过]{style="font-family:宋体"}*[n]{lang="EN-US"}*[分钟，设备就输出一次相应的会话日志。]{style="font-family:宋体"}

[[同时配置了时间阈值和流量阈值的情况下，只要有一个阈值到达，就会输出相应的会话日志，并将所有的阈值统计信息清零。]{style="font-family:宋体"}]{#struct_0_86917_x8972_x1572271398}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1855245387}

[]{#_Toc287971017}[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x713957820}[设置输出会话日志的时间阈值为]{style="font-family:宋体"}[50]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_86917_x8972_x1936046178}

[\[Sysname\] ]{lang="EN-US"}[session log time-active 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1887519400}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log enable]{lang="EN-US"}**]{#struct_0_86917_x8972_1410942610}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log bytes-active]{lang="EN-US"}**]{#struct_0_86917_x8972_x1828119863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session log packets-active]{lang="EN-US"}**]{#struct_0_86917_x8972_2036894311}
:::::

::: {#1957212743 .myid}
[]{#_Toc404793564}[]{#struct_0_86917_x8972_1869629242}

**会话管理 \-- 会话管理配置命令 \-- session statistic enable**

------------------------------------------------------------------------

[**[session statistics enable]{lang="EN-US"}**]{#struct_0_86917_x8972_x255712439}[命令用来开启会话统计功能。]{style="font-family:
宋体"}

[**[undo session statistics enable]{lang="EN-US"}**]{#struct_0_86917_x8972_970066297}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1553049580}

[**[session statistics enable]{lang="EN-US"}**]{#struct_0_86917_x8972_x954394387}

[**[undo session statistics enable]{lang="EN-US"}**]{#struct_0_86917_x8972_665460676}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x469349695}

[[会话统计功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_86917_x8972_1869694778}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_916202991}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_1848721686}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1930250232}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x816878597}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1217034240}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x146286699}

[[开启会话统计功能之后，设备将对收到和发送的基于会话的业务报文数目和报文字节数进行统计，基于会话的报文统计信息可以通过]{style="font-family:宋体"}**[display session table]{lang="EN-US"}**]{#struct_0_86917_x8972_1420317953}[命令查看，基于报文类型的报文统计信息可以通过]{style="font-family:宋体"}**[display session statistics]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1869760314}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x678997140}[开启会话统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_x329299482}

[\[Sysname\] session statistics enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x991094239}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session statistics]{lang="EN-US"}**]{#struct_0_86917_x8972_x1480853586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session table]{lang="EN-US"}**]{#struct_0_86917_x8972_1364725315}
:::

::: {#-1220228836 .myid}
[]{#_Toc404793565}[]{#struct_0_86917_x8972_1655649575}

**会话管理 \-- 会话管理配置命令 \-- session persistent acl**

------------------------------------------------------------------------

[**[session persistent acl]{lang="EN-US"}**]{#struct_0_86917_x8972_1442403590}[命令用来配置长连接会话规则。]{style="font-family:宋体"}

[**[undo session persistent acl]{lang="EN-US"}**]{#struct_0_86917_x8972_2012270270}[命令用来清除长连接会话规则。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1393621085}

[**[session persistent acl]{lang="EN-US"}**[ \[ **ipv6** \] *acl-number* \[ **aging-time** *time-value* \]]{lang="EN-US"}]{#struct_0_86917_x8972_1278600152}

[**[undo session persistent acl ]{lang="EN-US"}**[\[ **ipv6** \]]{lang="EN-US"}]{#struct_0_86917_x8972_1887584936}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1330334010}

[[无长连接会话规则。]{style="font-family:宋体"}]{#struct_0_86917_x8972_2082357971}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1623013348}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_x363506630}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1117397818}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1707565342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1576965559}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86917_x8972_938555861}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86917_x8972_1887388328}[：指定]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。如果没有指定本参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_86917_x8972_1031131839}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[aging-time]{lang="EN-US"}***[ time-value]{lang="EN-US"}*]{#struct_0_86917_x8972_1290117216}[：长连接会话的老化时间。其中，]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*[表示指定的老化时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[360]{lang="EN-US"}[，单位为小时，缺省值为]{style="font-family:宋体"}[24]{lang="EN-US"}[小时。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示永不老化。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_1219677482}

[[长连接老化时间仅在]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_86917_x8972_464222598}[会话进入稳态（]{style="font-family:宋体"}[TCP-EST]{lang="EN-US"}[状态）时生效。在]{style="font-family:宋体"}[TCP]{lang="EN-US"}[会话处于稳态时，长连接老化时间具有最高的优先级，其次为应用层协议老化时间，最后为协议状态老化时间。]{style="font-family:宋体"}

[[对于设置为永不老化的长连接会话，不会因为没有报文命中而被老化删除，只有当会话的发起方或响应方主动发起关闭连接请求或管理员使用]{style="font-family:宋体"}**[reset session table]{lang="EN-US"}**]{#struct_0_86917_x8972_x56766133}[命令手动删除该会话时，才会被删除。]{style="font-family:宋体"}

[[长连接会话的配置仅影响后续生成的会话，对于已经生效的会话不产生作用。]{style="font-family:宋体"}]{#struct_0_86917_x8972_1869367098}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x282618337}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_201760849}[配置符合]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[规则的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话为长连接，老化时间为]{style="font-family:宋体"}[72]{lang="EN-US"}[小时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_1934269879}

[\[Sysname\] session persistent acl 2000 aging-time 72]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_1887453864}[配置符合]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[规则的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话为长连接，老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[小时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_x1404960175}

[\[Sysname\] session persistent acl ipv6 3000 aging-time 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1414206995}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session aging-time application]{lang="EN-US"}**]{#struct_0_86917_x8972_x1863771689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session aging-time state]{lang="EN-US"}**]{#struct_0_86917_x8972_x1461903479}
:::

::: {#-6603498 .myid}
[]{#_Toc404793566}[]{#struct_0_86917_x8972_x587250432}[]{#_Toc380069740}[]{#_Toc373223063}[]{#_Toc364776367}

**会话管理 \-- 会话管理配置命令 \-- session synchronization enable**

------------------------------------------------------------------------

[**[session synchronization enable]{lang="EN-US" style="color:black"}**]{#struct_0_86917_x8972_x1956363194}[命令用来[开启会话业务热备份功能]{style="color:black"}。]{style="font-family:宋体"}

[**[undo [session synchronization enable]{style="color:black"}]{lang="EN-US"}**]{#struct_0_86917_x8972_1876617652}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1171620921}

[**[session synchronization enable]{lang="EN-US" style="color:black"}**]{#struct_0_86917_x8972_821073582}

[**[undo [session synchronization enable]{style="color:black"}]{lang="EN-US"}**]{#struct_0_86917_x8972_x587315968}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x1249735767}

[[会话业务热备份功能处于关闭状态。]{style="font-family:宋体;color:black"}]{#struct_0_86917_x8972_728386091}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x957653261}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86917_x8972_2083230972}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x587381504}

[[network-admin]{lang="EN-US"}]{#struct_0_86917_x8972_x1592411837}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86917_x8972_1226910140}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x2125516099}

[[会话[业务热备份]{style="color:black"}功能实现了多台设备之间会话以及基于会话的业务（]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_86917_x8972_889976337}[、]{style="font-family:宋体"}[ALG]{lang="EN-US"}[、]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[）的动态表项的热备份。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86917_x8972_x587447040}

[[\# ]{lang="EN-US"}]{#struct_0_86917_x8972_x1588747586}[开启会话[业务热备份]{style="color:black"}能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86917_x8972_x720705141}

[\[Sysname\] session synchronization enable]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
