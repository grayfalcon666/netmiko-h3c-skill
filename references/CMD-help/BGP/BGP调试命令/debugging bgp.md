::: {#-741763347 .myid}
[]{#_Toc404788301}[]{#struct_0_16239_89686_x786505234}

**BGP \-- BGP调试命令 \-- debugging bgp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x979268654}

[**[debugging bgp]{lang="EN-US"}**[ { **keepalive** \| **open** \| **packet** \| **raw-packet** \| **route-refresh** } \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \] \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_16239_89686_1665435399}

[**[undo debugging bgp]{lang="EN-US"}**[ { **keepalive** \| **open** \| **packet** \| **raw-packet** \| **route-refresh** }  \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \] \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_16239_89686_x1696032169}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_1074714986}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x715127030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x963993063}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x963927527}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_297619940}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_1582992664}

[**[keepalive]{lang="EN-US"}**]{#struct_0_16239_89686_214338842}[：]{style="font-family:宋体"}[BGP Keepalive]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[open]{lang="EN-US"}**]{#struct_0_16239_89686_832363404}[：]{style="font-family:宋体"}[BGP Open]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_16239_89686_1831238335}[：所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文的调试信息开关，包括]{style="font-family:宋体"}[Open]{lang="EN-US"}[报文，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文和]{style="font-family:宋体"}[Route-Refresh]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[raw-packet]{lang="EN-US"}**]{#struct_0_16239_89686_157923890}[：]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文具体信息调试开关。]{style="font-family:宋体"}

[**[route-refresh]{lang="EN-US"}**]{#struct_0_16239_89686_1665500935}[：]{style="font-family:宋体"}[BGP Route-Refresh]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_16239_89686_x74427607}[：对等体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_16239_89686_x967800476}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_16239_89686_x424258300}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_16239_89686_x283958843}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_1741464974}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_16239_89686_1412722916}[：接收的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_16239_89686_382868367}[：发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x460748426}

[**[debugging bgp]{lang="EN-US"}**]{#struct_0_16239_89686_1504935057}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[指定类型报文的调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[指定类型报文的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，该调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16239_89686_251881932}

[[表1-1 ]{lang="EN-US"}[debugging bgp keepalive]{lang="EN-US"}]{#struct_0_16239_89686_1243031414}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_919910043}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_1665566471}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x530051385}

[[BGP.*vpn-instance*]{lang="EN-US"}]{#struct_0_16239_89686_x789156597}

[[VPN]{lang="EN-US"}]{#struct_0_16239_89686_1602301331}[实例]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[如果不携带]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*]{#struct_0_16239_89686_448960676}[参数，则表示公网的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[X.X.X.X]{lang="EN-US"}*]{#struct_0_16239_89686_x1947579287}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1132144903}[邻居的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[X:X::X:X]{lang="EN-US"}*]{#struct_0_16239_89686_1665632007}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_664485055}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Recv]{lang="EN-US"}]{#struct_0_16239_89686_2108237659}

[[收到报文]{style="font-family:宋体"}]{#struct_0_16239_89686_x906726155}

[[Send]{lang="EN-US"}]{#struct_0_16239_89686_x245835080}

[[发送报文]{style="font-family:宋体"}]{#struct_0_16239_89686_472298505}

[[Length: *LengthNumber*]{lang="EN-US"}]{#struct_0_16239_89686_1666221831}

[[报文长度]{style="font-family:宋体"}]{#struct_0_16239_89686_186501287}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging bgp open]{lang="EN-US"}]{#struct_0_16239_89686_61357319}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_919506030}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x914911273}

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x1529389470}

[[BGP.*vpn-instance*]{lang="EN-US"}]{#struct_0_16239_89686_x1720926477}

[[VPN]{lang="EN-US"}]{#struct_0_16239_89686_1264098135}[实例]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[如果不携带]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*]{#struct_0_16239_89686_1666287367}[参数，则表示公网的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[X.X.X.X]{lang="EN-US"}*]{#struct_0_16239_89686_x692747188}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x361981206}[邻居的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[X:X::X:X]{lang="EN-US"}*]{#struct_0_16239_89686_2133366340}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1725046461}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Recv]{lang="EN-US"}]{#struct_0_16239_89686_x552908113}

[[收到报文]{style="font-family:宋体"}]{#struct_0_16239_89686_x1633773628}

[[Send]{lang="EN-US"}]{#struct_0_16239_89686_1665697544}

[[发送报文]{style="font-family:宋体"}]{#struct_0_16239_89686_x170228798}

[[Version]{lang="EN-US"}]{#struct_0_16239_89686_540957948}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x616682314}[协议版本号]{style="font-family:宋体"}

[[Local AS]{lang="EN-US"}]{#struct_0_16239_89686_x1627002455}

[[本地自治域号]{style="font-family:宋体"}]{#struct_0_16239_89686_1309681829}

[[HoldTime]{lang="EN-US"}]{#struct_0_16239_89686_1665763080}

[[HoldTime]{lang="EN-US"}]{#struct_0_16239_89686_x891375293}[值，单位：秒]{style="font-family:宋体"}

[[Router ID]{lang="FR"}]{#struct_0_16239_89686_271680414}

[[路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16239_89686_1289996707}[号]{style="font-family:宋体"}

[[BGP ID]{lang="EN-US"}]{#struct_0_16239_89686_x1820827775}

[[BGP ID]{lang="EN-US"}]{#struct_0_16239_89686_x1768592849}[号]{style="font-family:宋体"}

[[OPT Type:   2 (Capability)]{lang="EN-US"}]{#struct_0_16239_89686_1665828616}

[[能力协商内容]{style="font-family:宋体"}]{#struct_0_16239_89686_293645804}

[[CAP Type:   1 (Multiprotocol)  CAP Len: 4]{lang="PT-BR"}]{#struct_0_16239_89686_1913761266}

[[具有多协议能力]{style="font-family:宋体"}]{#struct_0_16239_89686_x1019178961}

[[IPv4-UNC (1/1)]{lang="EN-US"}]{#struct_0_16239_89686_1665894152}

[[CAP Type:   2 (RouteRefresh)   CAP Len: 0]{lang="EN-US"}]{#struct_0_16239_89686_x531487436}

[[具有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_16239_89686_379552964}[单播路由更新能力]{style="font-family:宋体"}

[[IPv4-MLC (1/2)]{lang="EN-US"}]{#struct_0_16239_89686_x963993062}

[[CAP Type:   2 (RouteRefresh)   CAP Len: 0]{lang="EN-US"}]{#struct_0_16239_89686_x438796428}

[[具有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_16239_89686_x963927526}[组播路由更新能力]{style="font-family:宋体"}

[[CAP Type:   65 (AS4)   CAP Len: 4 AS4]{lang="EN-US"}]{#struct_0_16239_89686_2048735008}[：]{style="font-family:宋体"}[100]{lang="EN-US"}

[[支持]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_16239_89686_687724901}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Total CAPB Len]{lang="EN-US"}]{#struct_0_16239_89686_1665435400}

[[能力协商总长度值]{style="font-family:宋体"}]{#struct_0_16239_89686_1025415758}

[[Total OPT Len]{lang="EN-US"}]{#struct_0_16239_89686_x299117178}

[[可选参数总长度值]{style="font-family:宋体"}]{#struct_0_16239_89686_1448122936}

[[Total Message Len]{lang="EN-US"}]{#struct_0_16239_89686_1665500936}

[[整个报文长度]{style="font-family:宋体"}]{#struct_0_16239_89686_x74230999}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging bgp route-refresh]{lang="EN-US"}]{#struct_0_16239_89686_x1884018058}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_914561112}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_1162959262}

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_1405690474}

[[BGP.*vpn-instance*]{lang="EN-US"}]{#struct_0_16239_89686_1234248609}

[[VPN]{lang="EN-US"}]{#struct_0_16239_89686_1599388213}[实例]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[如果不携带]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*]{#struct_0_16239_89686_1665566472}[参数，则表示公网的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[X.X.X.X]{lang="EN-US"}*]{#struct_0_16239_89686_x530116921}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x378996517}[邻居的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[X:X::X:X]{lang="EN-US"}*]{#struct_0_16239_89686_1705819783}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_2023046236}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Recv]{lang="EN-US"}]{#struct_0_16239_89686_x1330168276}

[[收到报文]{style="font-family:宋体"}]{#struct_0_16239_89686_1476520298}

[[Send]{lang="EN-US"}]{#struct_0_16239_89686_1665632008}

[[发送报文]{style="font-family:宋体"}]{#struct_0_16239_89686_663502015}

[[Length]{lang="EN-US"}]{#struct_0_16239_89686_x969934952}

[[报文长度]{style="font-family:宋体"}]{#struct_0_16239_89686_x1693780974}

[[AFI: 1; ]{lang="EN-US"}]{#struct_0_16239_89686_x12886799}[SAFI]{lang="EN-US"}[: 1]{lang="EN-US"}

[[地址族：]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_16239_89686_1666221832}[；子地址族：]{style="font-family:宋体"}[1]{lang="EN-US"}

[[AFI/ ]{lang="EN-US"}]{#struct_0_16239_89686_186435751}[SAFI]{lang="EN-US"}

[[地址族]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16239_89686_365921325}[子地址族]{style="font-family:宋体"}

[[WTR]{lang="EN-US"}]{#struct_0_16239_89686_x1559249288}

[[发送刷新信息的延时（]{style="font-family:宋体"}[When to Refresh]{lang="EN-US"}]{#struct_0_16239_89686_x593838460}[）]{style="font-family:宋体"}

[[peer x.x.x.x]{lang="EN-US"}]{#struct_0_16239_89686_x19299890}

[[对端邻居地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_16239_89686_1666287368}[地址]{style="font-family:宋体"}

[[peer x:x::x:x]{lang="EN-US"}]{#struct_0_16239_89686_x693074868}

[[对端邻居地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_16239_89686_448001962}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[Update]{lang="EN-US"}]{#struct_0_16239_89686_x1347014096}[报文调试信息详见后面小节介绍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1566500566}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_x1431493968}[在本地设备上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文的调试信息开关，收发]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文时打印调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp packet]{lang="EN-US"}]{#struct_0_16239_89686_1665697541}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 192.168.109.29 as-number 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer 192.168.109.29 enable]{lang="EN-US"}

[\*Apr 16 17:13:01:742 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: 192.168.109.29 Send OPEN, Version: 4]{lang="EN-US"}

[         Local AS: 100, HoldTime: 180, Router ID: 192.168.109.88]{lang="EN-US"}

[ ]{lang="EN-US"}

[         OPT Type:   2 (Capability)]{lang="EN-US"}

[         CAP Type:   1 (Multiprotocol)   CAP Len: 4]{lang="EN-US"}

[                                         IPv4-UNC (1/1)]{lang="EN-US"}

[         CAP Type:   2 (RouteRefresh)    CAP Len: 0]{lang="EN-US"}

[         CAP Type:  65 (AS4)             CAP Len: 4 AS4: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[         Total CAPB Len    : 14]{lang="EN-US"}

[         Total OPT Len     : 16]{lang="EN-US"}

[         Total Message Len : 45]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x169901118}*[向]{style="font-family:宋体"}[192.168.109.29]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP open]{lang="EN-US"}[报文，协商]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话参数。]{style="font-family:宋体"}*

[[\*Apr 16 17:13:01:761 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_972920389}

[         BGP.: 192.168.109.29 Recv OPEN Length: 37]{lang="EN-US"}

[         Version: 4, Local AS: 100, HoldTime : 180,]{lang="EN-US"}

[         BGP ID: 192.168.109.29, TotOptLen: 10]{lang="EN-US"}

[ ]{lang="EN-US"}

[         OPT Type:   2 (Capability)     OPT Len: 8]{lang="EN-US"}

[         ]{lang="EN-US"}[CAP Type:   1 (Multiprotocol)  CAP Len: 4]{lang="PT-BR"}

[                                        ]{lang="PT-BR"}[IPv4-UNC (1/1)]{lang="EN-US"}

[         CAP Type:   2 (RouteRefresh)   CAP Len: 0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1842589571}*[从]{style="font-family:宋体"}[192.168.109.29]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP open]{lang="EN-US"}[报文，建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*

[[\*Apr 16 17:13:01:771 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1665763077}

[         BGP.: 192.168.109.29 Send KEEPALIVE]{lang="EN-US"}

[         Length: 19]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x891309772}*[向]{style="font-family:宋体"}[192.168.109.29]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP keepalive]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[19]{lang="EN-US"}[字节。]{style="font-family:宋体"}*

[[\*Apr 16 17:13:01:802 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1214051240}

[         BGP.: 192.168.109.29 Recv KEEPALIVE]{lang="EN-US"}

[         Length: 19]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x1892828134}*[从]{style="font-family:宋体"}[192.168.109.29]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP keepalive]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[19]{lang="EN-US"}[字节。]{style="font-family:宋体"}*

[[\[Sysname-bgp-ipv4\] import-route static]{lang="EN-US"}]{#struct_0_16239_89686_x1387077874}

[\*Apr 16 17:54:09:96 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: Send UPDATE to peer 192.168.109.29 for following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      :]{lang="EN-US"}

[         Next hop     : 192.168.109.88]{lang="EN-US"}

[         Local pref   : 100]{lang="EN-US"}

[         111.1.1.1/32,]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x407047566}*[引入静态路由后，向]{style="font-family:宋体"}[192.168.109.29]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP update]{lang="EN-US"}[报文，发布引入的静态路由信息。]{style="font-family:宋体"}*

[[\*Apr 16 17:56:41:933 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1665828613}

[         BGP.: Recv UPDATE from peer 192.168.109.29 with following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      :]{lang="EN-US"}

[         Next hop     : 192.168.109.29]{lang="EN-US"}

[         Local pref   : 100]{lang="EN-US"}

[         MED          : 0]{lang="EN-US"}

[         111.1.1.1/32,]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_293842412}*[从]{style="font-family:宋体"}[192.168.109.29]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP update]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_x2111162700}[在两台设备]{style="font-family:宋体"}[A]{lang="EN-US"}[、]{style="font-family:宋体"}[B]{lang="EN-US"}[之间建立]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}[A]{lang="EN-US"}[上打开接收]{style="font-family:宋体"}[BGP Route-Refresh]{lang="EN-US"}[报文的调试信息开关，]{style="font-family:宋体"}[B]{lang="EN-US"}[上打开发送]{style="font-family:宋体"}[BGP Route-Refresh]{lang="EN-US"}[报文的调试信息开关。在]{style="font-family:宋体"}[B]{lang="EN-US"}[上执行]{style="font-family:宋体"}**[refresh bgp ipv4 all import]{lang="EN-US"}**[命令后，]{style="font-family:宋体"}[A]{lang="EN-US"}[和]{style="font-family:宋体"}[B]{lang="EN-US"}[上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp route-refresh send]{lang="EN-US"}]{#struct_0_16239_89686_x682576228}

[\<Sysname\> refresh bgp ipv4 all import]{lang="EN-US"}

[\*Apr 16 18:01:11:53 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: Send ROUTEREFRESH MSG to peer 9.9.9.9(IPv4-UNC).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x891081214}*[设备]{style="font-family:宋体"}[B]{lang="EN-US"}[发送]{style="font-family:宋体"}[Route-Refresh]{lang="EN-US"}[报文]{style="font-family:宋体"}*[，*长度为*]{style="font-family:宋体"}*[23]{lang="EN-US"}[字节]{style="font-family:宋体"}*[，*地址族是*]{style="font-family:宋体"}*[1]{lang="EN-US"}*[，*子地址族是*]{style="font-family:宋体"}*[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\<Sysname\> debugging bgp route-refresh receive]{lang="EN-US"}]{#struct_0_16239_89686_x2031767387}

[\*Apr 16 18:01:11:53 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.1 Recv ROUTEREFRESH MSG:]{lang="EN-US"}

[ Length: 23, AFI: 1, SAFI: 1, WTR: 4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1984855496}*[设备]{style="font-family:宋体"}[A]{lang="EN-US"}[收到]{style="font-family:宋体"}[Route-Refresh]{lang="EN-US"}[报文]{style="font-family:宋体"}*[，*长度为*]{style="font-family:宋体"}*[23]{lang="EN-US"}[字节]{style="font-family:宋体"}*[，*地址族是*]{style="font-family:宋体"}*[1]{lang="EN-US"}*[，*子地址族是*]{style="font-family:宋体"}*[1]{lang="EN-US"}*[，]{style="font-family:宋体"}*[发送刷新信息的延时时间是]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-153845544 .myid}
[]{#_Toc404788302}[]{#struct_0_16239_89686_1665894149}[]{#_Toc312411690}

**BGP \-- BGP调试命令 \-- debugging bgp acl**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x531815117}

[**[debugging bgp acl]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_16239_89686_1955175440}

[**[undo debugging bgp acl]{lang="EN-US"}**]{#struct_0_16239_89686_1804066287}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_1254952216}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x969524555}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x964255208}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x199071831}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x216878937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_1945722481}

[*[acl-number]{lang="EN-US"}*]{#struct_0_16239_89686_1665435397}[：用于匹配路由信息目的网络地址的访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1695114665}

[**[debugging bgp acl]{lang="EN-US"}**]{#struct_0_16239_89686_184916866}[命令用来打开通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp acl]{lang="EN-US"}**[命令]{style="font-family:宋体"}[用来关闭通过]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[过滤的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1534847121}[路由的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16239_89686_x1027819965}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时配置了本命令和]{style="font-family:宋体"}]{#struct_0_16239_89686_x397119575}**[debugging bgp prefix-list]{lang="EN-US"}**[命令，则只有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由同时通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤，才会打开该路由的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过基本]{style="font-family:宋体"}]{#struct_0_16239_89686_x1647571926}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[）对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由进行过滤时，如果配置了]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **source** *source-address* *source-wildcard*]{lang="EN-US"}[命令，则只要路由的目的网络地址与]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}*[source-address source-wildcard]{lang="EN-US"}*[匹配，则该路由与]{style="font-family:
宋体"}**[rule]{lang="EN-US"}**[命令配置的规则匹配，不会再比较路由的目的网络地址掩码。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_16239_89686_x616923308}[（]{lang="EN-US" style="font-family:宋体"}[3000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[）对]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由进行过滤时，]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[命令配置的规则用]{lang="EN-US" style="font-family:宋体"}[来过滤指定目的网络地址的路由；]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[命令配置的规则用]{lang="EN-US" style="font-family:宋体"}[来过滤指定目的网络地址和掩码的路由，其中]{lang="EN-US" style="font-family:宋体"}**[source ]{lang="EN-US"}***[sour-addr sour-wildcard]{lang="EN-US"}*[用来过滤路由目的网络地址，]{lang="EN-US" style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[用来过滤路由掩码。]{lang="EN-US" style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[指定的掩码应该是连续的。如果指定的掩码不连续，则该过滤掩码的条件不生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x32213712}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_x1312388040}[通过配置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤条件，打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[的路由更新调试信息开关。设备接收到对端发布的]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[和]{style="font-family:宋体"}[11.1.1.2/32]{lang="EN-US"}[两条路由后，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16239_89686_1665500933}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 11.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] quit]{lang="EN-US"}

[\<Sysname\> debugging bgp update]{lang="EN-US"}

[\<Sysname\> debugging bgp acl 2000]{lang="EN-US"}

[\*Dec 20 16:02:33:923 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: Recv UPDATE from peer 13.1.1.1 with following destinations:]{lang="EN-US"}

[         Update message length : 60]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 100]{lang="EN-US"}

[         Next hop     : 13.1.1.1]{lang="EN-US"}

[         MED          : 0]{lang="EN-US"}

[         11.1.1.1/32,]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x74034391}*[对端发布两条路由]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[和]{style="font-family:宋体"}[11.1.1.2/32]{lang="EN-US"}[，只有]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤，因此，只打印]{style="font-family:宋体"}[11.1.1.1/32 ]{lang="EN-US"}[的调试信息。]{style="font-family:宋体"}*
:::

::::: {#655458520 .myid}
[]{#_Toc404788303}[]{#struct_0_16239_89686_615488624}[]{#_Toc205722844}

**BGP \-- BGP调试命令 \-- debugging bgp all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_923421934}

[**[debugging bgp]{lang="EN-US"}**[ **all** \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_451699494}

[**[undo debugging bgp]{lang="EN-US"}**[ **all** \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_x116080320}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_1665566469}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x530575672}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x963927528}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_298209764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x964124136}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_x2030387618}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_16239_89686_x1581762387}[：表示与指定对等体之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}*[ipv4-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_16239_89686_598611141}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_16239_89686_x80535655}[：表示与指定对等体之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_16239_89686_x1997612309}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_855038524}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1463683081}

[]{#struct_0_16239_89686_x1487364404}[]{#_Hlt7001923}[]{#_Hlt9148270}**[debugging bgp all]{lang="EN-US"}**[命令打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}**[undo debugging ]{lang="EN-US"}[bgp all]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1665632005}[所有调试开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16239_89686_664353983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令会打开所有和]{style="font-family:宋体"}]{#struct_0_16239_89686_1072578301}[BGP]{lang="EN-US"}[相关的调试信息开关，信息量会比较大，可能影响系统应用，请慎重使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[调试完毕后，请及时关闭调试信息开关。]{style="font-family:宋体"}]{#struct_0_16239_89686_x1765830772}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1777169068}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_x362686744}[在设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[所有调试信息开关。当设备]{style="font-family:宋体"}[A]{lang="EN-US"}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.109.88]{lang="EN-US"}[）和设备]{style="font-family:宋体"}[B]{lang="EN-US"}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.109.29]{lang="EN-US"}[）建立]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[会话时，设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上打印如下调试信息。]{style="font-family:宋体"}

[[\<DeviceA\> debugging bgp all]{lang="EN-US"}]{#struct_0_16239_89686_x344466132}

[\*Apr 16 16:19:10:54 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 CR Timer Expired.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 Receive FsmConnectRetryTimer_Expires event in IDLE state.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 Receive ManualStart event in IDLE state.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 State is changed from IDLE to CONNECT.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x2072619603}*[激活]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体后，等待]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}*[，*主动发起连接。*]{style="font-family:宋体"}

[[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1666287365}

[ BGP.: 192.168.109.29 CR Timer Expired.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 Receive FsmConnectRetryTimer_Expires event in CONNECT state.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 State is changed from CONNECT to CONNECT.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 CR Timer Expired.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 Receive FsmConnectRetryTimer_Expires event in CONNECT state.]{lang="EN-US"}

[\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 State is changed from CONNECT to CONNECT.]{lang="EN-US"}

[\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 Receive Tcp_CR_Acked event in CONNECT state.]{lang="EN-US"}

[\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: Connected to 192.168.109.29.]{lang="EN-US"}

[\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 CR Timer Deleted.]{lang="EN-US"}

[\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 HD Timer Created.]{lang="EN-US"}

[\*Apr 16 16:19:10:75 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: 192.168.109.29 Send OPEN, Version: 4]{lang="EN-US"}

[         Local AS: 100, HoldTime: 180, Router ID: 192.168.109.88]{lang="EN-US"}

[         OPT Type:   2 (Capability)]{lang="EN-US"}

[         CAP Type:   1 (Multiprotocol)   CAP Len: 4]{lang="EN-US"}

[                                         IPv4-UNC (1/1)]{lang="EN-US"}

[         CAP Type:   2 (RouteRefresh)    CAP Len: 0]{lang="EN-US"}

[         CAP Type:  65 (AS4)             CAP Len: 4 AS4: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[         Total CAPB Len    : 14]{lang="EN-US"}

[         Total OPT Len     : 16]{lang="EN-US"}

[         Total Message Len : 45]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:75 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP: Sent to 192.168.109.29 (AS Number: 100)]{lang="EN-US"}

[         (Displaying bytes from 1 to 45)]{lang="EN-US"}

[         Message Type: Open, Total number of bytes: 45]{lang="EN-US"}

[         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF]{lang="EN-US"}

[         ]{lang="EN-US"}[00 2D 01 04 00 64 00 B4 C0 A8 6D 58 10 02 0E 01]{lang="PT-BR"}

[         04 00 01 00 01 02 00 41 04 00 00 00 64]{lang="PT-BR"}

[\*Apr 16 16:19:10:75 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="PT-BR"}

[ ]{lang="PT-BR"}[BGP.: 192.168.109.29 State is changed from CONNECT to OPENSENT.]{lang="EN-US"}

[\*Apr 16 16:19:10:76 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SESSION be sent SIGNAL: SIG_MAIN  .]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_16239_89686_x692878260}*[连接成功]{style="font-family:宋体"}*[，*主动发送*]{style="font-family:宋体"}*[OPEN]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1665697542}

[         BGP: Received from 192.168.109.29 (AS Number: 100)]{lang="EN-US"}

[         (Displaying bytes from 1 to 45)]{lang="EN-US"}

[         Message Type: Open, Total number of bytes: 45]{lang="EN-US"}

[         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF]{lang="EN-US"}

[         ]{lang="EN-US"}[00 2D 01 04 00 64 00 B4 83 01 01 01 10 02 0E 01]{lang="PT-BR"}

[         04 00 01 00 01 02 00 41 04 00 00 00 64]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="PT-BR"}

[         ]{lang="PT-BR"}[BGP.: 192.168.109.29 Recv OPEN Length: 45]{lang="EN-US"}

[         Version: 4, Local AS: 100, HoldTime : 180,]{lang="EN-US"}

[         BGP ID: 131.1.1.1, TotOptLen: 16]{lang="EN-US"}

[ ]{lang="EN-US"}

[         OPT Type:   2 (Capability)      OPT Len: 14]{lang="EN-US"}

[                                         IPv4-UNC (1/1)]{lang="EN-US"}

[         CAP Type:   1 (Multiprotocol)   CAP Len: 4]{lang="EN-US"}

[         CAP Type:   2 (RouteRefresh)    CAP Len: 0]{lang="EN-US"}

[         CAP Type:  65 (AS4)             CAP Len: 4 AS4: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 Receive ReceiveOpenMessage event in OPENSENT state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x170097726}*[收到对端发送的]{style="font-family:宋体"}[OPEN]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1665763078}

[ BGP.: 192.168.109.29 KA Timer Created.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: 192.168.109.29 Send KEEPALIVE]{lang="EN-US"}

[         Length: 19]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP: Sent to 192.168.109.29 (AS Number: 100)]{lang="EN-US"}

[         (Displaying bytes from 1 to 19)]{lang="EN-US"}

[         Message Type: KeepAlive, Total number of bytes: 19]{lang="EN-US"}

[         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF]{lang="EN-US"}

[         00 13 04]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 State is changed from OPENSENT to OPENCONFIRM.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:92 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SESSION be sent SIGNAL: SIG_MAIN  .]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:99 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SESSION be sent SIGNAL: SIG_MAIN  .]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:105 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP: Received from 192.168.109.29 (AS Number: 100)]{lang="EN-US"}

[         (Displaying bytes from 1 to 19)]{lang="EN-US"}

[         Message Type: KeepAlive, Total number of bytes: 19]{lang="EN-US"}

[         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF]{lang="EN-US"}

[         00 13 04]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:105 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: 192.168.109.29 Recv KEEPALIVE]{lang="EN-US"}

[         Length: 19]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:105 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 Receive ReceiveKeepAliveMsg event in OPENCONFIRM state.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Apr 16 16:19:10:106 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 State is changed from OPENCONFIRM to ESTABLISHED.]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_x891899596}*[会话建立成功。]{style="font-family:宋体"}*

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BGP%20Debug.files/image001.png){#图片 1 width="63" height="25"}]{lang="EN-US"}]{#struct_0_16239_89686_x1572729539}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[以上是执行]{style="font-family:KaiTi_GB2312"}]{#struct_0_16239_89686_x1932652763}**[debugging bgp all]{lang="EN-US"}**[命令后在设备]{style="font-family:KaiTi_GB2312"}[A]{lang="EN-US"}[上得到的]{style="font-family:KaiTi_GB2312"}[BGP]{lang="EN-US"}[会话建立过程的全部调试信息，当设备无法建立]{style="font-family:KaiTi_GB2312"}[BGP]{lang="EN-US"}[会话时，可以初步对比此流程，观察是否缺少某个步骤的报文，进而定位问题。后续命令将逐一介绍这些调试信息，此处不再重复。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}
:::::

::: {#-1700882526 .myid}
[]{#_Toc404788304}[]{#struct_0_16239_89686_1008531353}[]{#_Toc205722845}

**BGP \-- BGP调试命令 \-- debugging bgp calc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_1239783391}

[**[debugging bgp]{lang="EN-US"}**[ **calc** \[ **ipv4** \[ **mdt** \| **multicast** \] \| **ipv6** \[ **multicast** \] \| **l2vpn** \| **vpn-instance** *vpn-instance-name* { **ipv4** \| **ipv6** \| **vpnv4** } \| **vpnv4** \| **vpnv6** \]]{lang="EN-US"}]{#struct_0_16239_89686_x1020884658}

[**[undo debugging bgp calc ]{lang="EN-US"}**[\[ **ipv4** \[ **mdt** \| **multicast** \] \| **ipv6** \[ **multicast** \] \| **l2vpn** \| **vpn-instance** *vpn-instance-name* { **ipv4** \| **ipv6** \| **vpnv4** } \| **vpnv4** \| **vpnv6** \]]{lang="EN-US"}]{#struct_0_16239_89686_x1101121363}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_1665828614}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_293776876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x963730923}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x963665387}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x2020317035}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1534333966}

[**[ipv4]{lang="EN-US"}**]{#struct_0_16239_89686_x1219553330}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_16239_89686_2119154812}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[**[mdt]{lang="EN-US"}**]{#struct_0_16239_89686_x964255210}[：表示]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_16239_89686_x964189674}[：表示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[**[l2vpn]{lang="EN-US"}**]{#struct_0_16239_89686_x2015704402}[：表示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[地址族的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息选择调试信息开关。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_1480492974}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_16239_89686_1350733237}[：表示]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_16239_89686_1665894150}[：表示]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x531356364}

[**[debugging bgp calc]{lang="EN-US"}**]{#struct_0_16239_89686_1943337237}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp calc]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x908067595}[路由选择调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**]{#struct_0_16239_89686_x964386282}[和]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**[参数，则表示单播地址族。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1986638266}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_x971517797}[打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择调试信息开关。设备通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体学习到路由]{style="font-family:宋体"}[129.1.1.0/24]{lang="EN-US"}[，在该设备上手工配置一条到达]{style="font-family:宋体"}[129.1.1.0/24]{lang="EN-US"}[的静态路由，并将其引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由，触发]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由优选。此时，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp calc]{lang="EN-US"}]{#struct_0_16239_89686_1665435398}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] ip route-static 129.1.1.0 24 null 0]{lang="EN-US"}

[\[Sysname\] display ip routing-table 129.1.1.0 24]{lang="EN-US"}

[Routing Table : Public]{lang="EN-US"}

[Summary Count : 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination/Mask    Proto  Pre  Cost         NextHop         Interface]{lang="EN-US"}

[ ]{lang="EN-US"}

[129.1.1.0/24         Static 60   0            0.0.0.0         NULL0]{lang="EN-US"}

[\[Sysname\] display bgp ipv4 routing-table 129.1.1.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID: 80.1.1.200]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ Paths:   1 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table entry information of 129.1.1.0/24:]{lang="EN-US"}

[ From            : 192.168.136.1 (192.168.136.1)]{lang="EN-US"}

[ Rely Nexthop    : 0.0.0.0]{lang="EN-US"}

[ Original nexthop: 192.168.136.1]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : 200]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : pref-val 0, pre 255]{lang="EN-US"}

[ State           : valid, external, best,]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] import-route static]{lang="EN-US"}

[\*May 31 21:50:59:773 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ CALC process result, Dest/Mask: 129.1.1.0/24 :]{lang="EN-US"}

[         InstKey         : IPv4-UNC/0]{lang="EN-US"}

[         First Rt        : 0xb320ef88]{lang="EN-US"}

[         Last Active Rt  : 0xb320ef88]{lang="EN-US"}

[         Table           : 0]{lang="EN-US"}

[         Flag            : 0x201]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x1696097705}*[到达目的网络]{style="font-family:宋体"}[129.1.1.0/24]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由选择结束，打印优选结果。]{style="font-family:宋体"}*
:::

::: {#-808132243 .myid}
[]{#_Toc404788305}[]{#struct_0_16239_89686_1186290698}[]{#_Toc205722846}

**BGP \-- BGP调试命令 \-- debugging bgp event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x568756309}

[**[debugging bgp]{lang="EN-US"}**[ **event** \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_665181448}

[**[undo debugging bgp]{lang="EN-US"}**[ **event** \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_1665500934}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_x74362071}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_1634865552}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x964124138}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x964058602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x549487736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_1649340807}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_16239_89686_x2109520904}[：表示与指定对等体之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的事件调试信息开关。]{style="font-family:宋体"}*[ipv4-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_16239_89686_598480070}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_16239_89686_2008139066}[：表示与指定对等体之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的事件调试信息开关。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_16239_89686_1259169030}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_x360107915}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_1665566470}

[**[debugging bgp event]{lang="EN-US"}**]{#struct_0_16239_89686_x529985849}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1523997721}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[打开此调试信息开关，会打印所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_606542562}[状态机转变过程和触发状态机转变的事件，如果]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居无法建立，从中可以定位是在哪个状态出现问题，是什么事件触发等。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging bgp event]{lang="EN-US"}]{#struct_0_16239_89686_1826192588}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_911403204}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_465313007}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_820776875}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_2057232963}

[[数据包属于]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x197316846}[协议]{style="font-family:宋体"}

[*[X.X.X.X]{lang="EN-US"}*]{#struct_0_16239_89686_1665632006}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_664419519}[邻居的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[X:X::X:X]{lang="EN-US"}*]{#struct_0_16239_89686_1720895527}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_522507528}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Receive *Eventname* event in state,]{lang="EN-US"}]{#struct_0_16239_89686_1129366803}

[[在某状态收到事件]{style="font-family:宋体"}]{#struct_0_16239_89686_1510296269}

[[State is changed from *old-state* to *new-state*.]{lang="EN-US"}]{#struct_0_16239_89686_1021570718}

[[状态转换报文，原始状态：]{style="font-family:宋体"}*[old-state ;]{lang="EN-US"}*]{#struct_0_16239_89686_1666221830}

[[新状态：]{style="font-family:宋体"}*[new-state]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_16239_89686_186566823}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_438873775}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_x458571608}[打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[事件调试信息开关。与]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体建立会话时，将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp event]{lang="EN-US"}]{#struct_0_16239_89686_1730641359}

[\*Apr 16 16:44:13:52 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 192.168.109.29 State is changed from IDLE to CONNECT.]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_x942432198}*[会话从]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[状态转换为]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Apr 16 16:44:13:60 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_626075679}

[ BGP.: 192.168.109.29 Receive Tcp_CR_Acked event in CONNECT state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x1159728935}*[在]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[状态收到]{style="font-family:宋体"}[Tcp_CR_Acked]{lang="EN-US"}[事件。]{style="font-family:宋体"}*

[[\*Apr 16 16:44:13:66 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1666287366}

[ BGP.: Connected to 192.168.109.29.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x692681652}*[建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}*

[[\*Apr 16 16:44:13:71 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_17609168}

[ BGP.: 192.168.109.29 State is changed from CONNECT to OPENSENT.]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_144768938}*[会话从]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[状态转换为]{style="font-family:宋体"}[OPENSENT]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Apr 16 16:44:13:79 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_535452943}

[ BGP.: 192.168.109.29 Receive ReceiveOpenMessage event in OPENSENT state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x1238547282}*[在]{style="font-family:宋体"}[OPENSENT]{lang="EN-US"}[状态收到]{style="font-family:宋体"}[Open]{lang="EN-US"}[报文事件。]{style="font-family:宋体"}*

[[\*Apr 16 16:44:13:80 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1505057619}

[ BGP.: 192.168.109.29 State is changed from OPENSENT to OPENCONFIRM.]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_99021715}*[会话从]{style="font-family:宋体"}[OPENSENT]{lang="EN-US"}[状态转换为]{style="font-family:宋体"}[OPENCONFIRM]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Apr 16 16:44:13:87 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x706955450}

[ BGP.: 192.168.109.29 Receive ReceiveKeepAliveMsg event in OPENCONFIRM state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1131165896}*[在]{style="font-family:宋体"}[OPENCONFIRM]{lang="EN-US"}[状态收到]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文事件。]{style="font-family:宋体"}*

[[\*Apr 16 16:44:13:87 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1242378770}

[ BGP.: 192.168.109.29 State is changed from OPENCONFIRM to ESTABLISHED.]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_x848966811}*[会话从]{style="font-family:宋体"}[OPENCONFIRM]{lang="EN-US"}[状态转换为]{style="font-family:宋体"}[ESTABLISHED]{lang="EN-US"}[状态，成功建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*

::: {#1300164082 .myid}
[]{#_Toc404788306}[]{#struct_0_16239_89686_x1183230446}

**BGP \-- BGP调试命令 \-- debugging bgp graceful-restart**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1152409898}

[**[debugging bgp]{lang="EN-US"}**[ **graceful-restart** \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_283230199}

[**[undo debugging bgp graceful-restart ]{lang="EN-US"}**[\[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_x677014685}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_x2047945730}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x706889914}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_958124631}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_957928023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_1963610831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_1749879355}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_16239_89686_1548573765}[：表示与指定对等体之间的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[ipv4-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_16239_89686_598742211}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_16239_89686_x1734357355}[：表示与指定对等体之间的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_16239_89686_387808699}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_x599930117}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1633212792}

[**[debugging bgp]{lang="EN-US"}**[ **graceful-restart**]{lang="EN-US"}]{#struct_0_16239_89686_1931010636}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp]{lang="EN-US"}**[ **graceful-restart**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x706824378}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[打开此调试信息开关，会打印]{style="font-family:宋体"}[BGP GR]{lang="EN-US"}]{#struct_0_16239_89686_367707216}[过程的调试信息，包括]{style="font-family:宋体"}[GR]{lang="EN-US"}[开始、]{style="font-family:宋体"}[GR]{lang="EN-US"}[结束等信息。如果]{style="font-family:宋体"}[BGP]{lang="EN-US"}[在]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程中发生问题，可以打开该调试信息开关定位问题。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging bgp graceful-restart]{lang="EN-US"}]{#struct_0_16239_89686_x93186636}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_911027931}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x1574438433}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x686512679}

[[PrevNegGrSessCnt]{lang="EN-US"}]{#struct_0_16239_89686_x1928307815}

[[重启前协商]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16239_89686_x1148270447}[的邻居个数]{style="font-family:宋体"}

[[Restarter GR Starts]{lang="EN-US"}]{#struct_0_16239_89686_984131116}

[[GR Restarter]{lang="EN-US"}]{#struct_0_16239_89686_x706758842}[开始]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程]{style="font-family:宋体"}

[[Restarter GR Ends]{lang="EN-US"}]{#struct_0_16239_89686_x1566271904}

[[GR Restarter]{lang="EN-US"}]{#struct_0_16239_89686_x1196337675}[结束]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程]{style="font-family:宋体"}

[[Get GR State Over. Start FSM]{lang="EN-US"}]{#struct_0_16239_89686_2074547218}

[[获取]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_16239_89686_816148399}[状态结束，启动状态机]{style="font-family:宋体"}

[[Received EOR from Peer *peer-address* (*address-family*)]{lang="EN-US"}]{#struct_0_16239_89686_x814953797}

[[从对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*]{#struct_0_16239_89686_616985914}[接收到]{style="font-family:宋体"}[EOR]{lang="EN-US"}[（]{style="font-family:宋体"}[End of Routing-Information-Base]{lang="EN-US"}[，路由信息库结束）标识，该]{style="font-family:宋体"}[EOR]{lang="EN-US"}[的地址族为]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*

[[Recv ALL_PEERS_UP EVT, Get EOR wait Count]{lang="EN-US"}]{#struct_0_16239_89686_x707217594}

[[所有需要等待的邻居都]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_16239_89686_1186156169}[了，还需要等待的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6 EOR]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Trigger Calc NULL Node]{lang="EN-US"}]{#struct_0_16239_89686_1794269323}

[[触发最后一条表项优选]{style="font-family:宋体"}]{#struct_0_16239_89686_2062172025}

[[Trigger Calc Result NULL Node]{lang="EN-US"}]{#struct_0_16239_89686_22949918}

[[触发处理优选后的最后一条表项]{style="font-family:宋体"}]{#struct_0_16239_89686_x817179669}

[[Global GR Send Protect Timer Created]{lang="EN-US"}]{#struct_0_16239_89686_x707152058}

[[创建触发发送的超时保护定时器]{style="font-family:宋体"}]{#struct_0_16239_89686_x772339805}

[[Recv SMOOTH_END Event]{lang="EN-US"}]{#struct_0_16239_89686_x788666166}

[[接收到]{style="font-family:宋体"}[RM]{lang="EN-US"}]{#struct_0_16239_89686_1959013987}[平滑结束消息，老化引入的路由]{style="font-family:宋体"}

[[Trigger All Prefix Received Node]{lang="EN-US"}]{#struct_0_16239_89686_x2033662152}

[[通知发送模块触发发送]{style="font-family:宋体"}]{#struct_0_16239_89686_x707086522}

[[Sent EOR to Peer *peer-address* (*address-family*)]{lang="EN-US"}]{#struct_0_16239_89686_x1519199819}

[[向对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*]{#struct_0_16239_89686_1906622593}[发送]{style="font-family:宋体"}[EOR]{lang="EN-US"}[标识，该]{style="font-family:宋体"}[EOR]{lang="EN-US"}[的地址族为]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1806353799}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_519546040}[在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[调试信息]{style="font-family:宋体"}[开关。在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[之间建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，并且会话处于]{style="font-family:宋体"}[Established]{lang="EN-US"}[状态。]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上重启]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp graceful-restart]{lang="EN-US"}]{#struct_0_16239_89686_884754477}

[\*Aug  9 17:34:51:255 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP_GR: PrevNegGrSessCnt 3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x549090645}*[重启前协商]{style="font-family:宋体"}[GR]{lang="EN-US"}[的邻居个数为]{style="font-family:宋体"}[3]{lang="EN-US"}[个。]{style="font-family:宋体"}*

[[\*Aug  9 17:34:51:255 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x707020986}

[ BGP_GR: (IPv4) Restarter GR Starts.]{lang="EN-US"}

[*[// IPv4]{lang="EN-US"}*]{#struct_0_16239_89686_x409603979}*[地址族开始]{style="font-family:宋体"}[GR]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug  9 17:34:52:209 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_2111733002}

[ BGP_GR: Get GR State Over. Start FSM.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1733860020}*[启动状态机。]{style="font-family:宋体"}*

[[\*Aug  9 17:35:23:421 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_870716436}

[ BGP_GR.: Received EOR from Peer 12.1.3.2 (IPv4-VPN).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x7598077}*[收到]{style="font-family:宋体"}[EOR]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug  9 17:35:48:704 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1609163667}

[ BGP_GR.: Received EOR from Peer 12.1.4.2 (IPv4-VPN).]{lang="EN-US"}

[\*Aug  9 17:36:16:383 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP_GR: Recv ALL_PEERS_UP EVT, Get EOR wait Count:]{lang="EN-US"}

[          IPv4 Count: 1, IPv6 Count: 0, L2VPN Count: 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x706431162}*[所有需要等待的邻居都]{style="font-family:宋体"}[UP]{lang="EN-US"}[了，还需要等待一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的]{style="font-family:宋体"}[EOR]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug  9 17:36:16:383 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_381904386}

[ BGP_GR.: Received EOR from Peer 12.1.2.2 (IPv4-VPN)]{lang="EN-US"}

[\*Aug  9 17:36:19:205 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP_GR: (IPv4) Restarter GR Ends.]{lang="EN-US"}

[*[// IPv4]{lang="EN-US"}*]{#struct_0_16239_89686_1071554252}*[地址族]{style="font-family:宋体"}[GR]{lang="EN-US"}[结束。]{style="font-family:宋体"}*

[[\*Aug  9 17:36:19:205 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x902035763}

[ BGP_GR: Trigger Calc NULL Node(VerID=0x2). IPv4.]{lang="EN-US"}

[\*Aug  9 17:36:19:205 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP_GR: Trigger Calc Result NULL Node(VerID=0x2). IPv4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x1564985469}*[所有路由迭代结束后触发优选。]{style="font-family:宋体"}*

[[\*Jan  1 00:44:00:786 2000 Sysname BGP/7/DEBUG:]{lang="EN-US"}]{#struct_0_16239_89686_1795908462}

[ BGP_TIMER: Global GR Send Protect Timer Created. IPv4.]{lang="EN-US"}

[\*Jan  1 00:44:00:847 2000 Sysname BGP/7/DEBUG:]{lang="EN-US"}

[ BGP_GR: Recv SMOOTH_END Event. usFamily 2.]{lang="EN-US"}

[\*Jan  1 00:44:00:848 2000 Sysname BGP/7/DEBUG:]{lang="EN-US"}

[ BGP_GR: Delete All IPv4 Redist Routes With Stale Flag.]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_x706365626}*[接收到]{style="font-family:宋体"}[RM]{lang="EN-US"}[平滑结束消息，老化引入的路由。]{style="font-family:宋体"}*

[[\*Jan  1 00:44:00:849 2000 Sysname BGP/7/DEBUG:]{lang="EN-US"}]{#struct_0_16239_89686_1506752549}

[ BGP_GR: Trigger Calc NULL Node(VerID=0x2). IPv4.]{lang="EN-US"}

[\*Jan  1 00:44:00:850 2000 Sysname BGP/7/DEBUG:]{lang="EN-US"}

[ BGP_GR: Trigger Calc Result NULL Node(VerID=0x2). IPv4.]{lang="EN-US"}

[*[// RM]{lang="EN-US"}*]{#struct_0_16239_89686_1704868430}*[平滑结束后再次触发迭代优选。]{style="font-family:宋体"}*

[[\*Jan  1 00:44:02:783 2000 Sysname BGP/7/DEBUG:]{lang="EN-US"}]{#struct_0_16239_89686_453756860}

[ BGP_GR: Check All Prefix Received Success. IPv4.]{lang="EN-US"}

[\*Jan  1 00:44:02:783 2000 Sysname BGP/7/DEBUG:]{lang="EN-US"}

[ BGP_GR: Trigger All Prefix Received Node. IPv4.]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_787326226}*[路由已经稳定，触发发送。]{style="font-family:宋体"}*

[[\*Aug  9 17:36:22:206 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x2065562501}

[ BGP_GR.: Sent EOR to Peer 12.1.3.2 (IPv4-VPN).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1028495269}*[发送]{style="font-family:宋体"}[EOR]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug  9 17:36:22:206 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x706955449}

[ BGP_GR.: Sent EOR to Peer 12.1.4.2 (IPv4-VPN).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1130576073}*[发送]{style="font-family:宋体"}[EOR]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug  9 17:36:22:206 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x907269315}

[ BGP_GR.: Sent EOR to Peer 12.1.2.2 (IPv4-VPN).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1687685682}*[发送]{style="font-family:宋体"}[EOR]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-1381568800 .myid}
[]{#_Toc404788307}[]{#struct_0_16239_89686_x1538015682}

**BGP \-- BGP调试命令 \-- debugging bgp ha**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1947611881}

[**[debugging bgp]{lang="EN-US"}**[ **ha**]{lang="EN-US"}]{#struct_0_16239_89686_1577091755}

[**[undo debugging bgp]{lang="EN-US"}**[ **ha**]{lang="EN-US"}]{#struct_0_16239_89686_x937836432}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_427948514}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x706889913}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_957993556}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_958321236}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1323783161}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_x415423534}

[[无]{style="font-family:宋体"}]{#struct_0_16239_89686_617313485}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_1548806544}

[**[debugging bgp ha]{lang="EN-US"}**]{#struct_0_16239_89686_x2118613201}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp ha]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，该调试开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16239_89686_x6532642}

[[打开此调试信息开关，会打印]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1877327522}[主备线程间的调试信息。如果]{style="font-family:宋体"}[BGP]{lang="EN-US"}[在主备过程中发生问题，可以打开该调试信息开关定位。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging bgp ha]{lang="EN-US"}]{#struct_0_16239_89686_x706824377}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1956362669}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_958255700}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_958583380}

[[BGP-HA]{lang="EN-US"}]{#struct_0_16239_89686_958648916}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_958059093}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息]{style="font-family:宋体"}

[[The main process received an HA message. Type: *type*.]{lang="EN-US"}]{#struct_0_16239_89686_958124629}

[[接收到类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_16239_89686_957928021}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[The standby process received realtime backup data from the main process. Data type: *type*.]{lang="EN-US"}]{#struct_0_16239_89686_958321237}

[[备进程从主进程接收实备数据，数据类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_16239_89686_958386773}

[[The standby process finished processing the realtime backup data. Result: *result*.]{lang="EN-US"}]{#struct_0_16239_89686_958190165}

[[备进程处理完实备数据]{style="font-family:宋体"}]{#struct_0_16239_89686_958255701}

[[Begin to backup data in batches.]{lang="EN-US"}]{#struct_0_16239_89686_958583381}

[[批备数据开始]{style="font-family:宋体"}]{#struct_0_16239_89686_958648917}

[[Finished backing up data in batches.]{lang="EN-US"}]{#struct_0_16239_89686_958059090}

[[批备数据完成]{style="font-family:宋体"}]{#struct_0_16239_89686_958124626}

[[Started to process the received HA message. Message type: *type*.]{lang="EN-US"}]{#struct_0_16239_89686_957993554}

[[开始处理接收到的]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_16239_89686_958321234}[消息，消息类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[The main process backed up the configuration data to the standby process through HA channel. Result: *result*.]{lang="EN-US"}]{#struct_0_16239_89686_958386770}

[[主进程通过]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_16239_89686_958190162}[通道将配置数据备份到备进程，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Received an unknown HA message. Message type: *type*,]{lang="EN-US"}]{#struct_0_16239_89686_958255698}

[[收到未知类型的]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_16239_89686_958583378}[消息，消息类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[The main process sent data to the backup process in batches through the HA channel. Result: *result*.]{lang="EN-US"}]{#struct_0_16239_89686_958059091}

[[主进程通过批备通道给备进程发送数据，返回值为]{style="font-family:宋体"}*[ result]{lang="EN-US"}*]{#struct_0_16239_89686_958124627}

[[BGP notified HA that the operation *type* completed.]{lang="EN-US"}]{#struct_0_16239_89686_957928019}

[[通知]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_16239_89686_957993555}[操作完成，操作类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[The main process backed up the VRF data to the standby process through HA channel. Result: *result*.]{lang="EN-US"}]{#struct_0_16239_89686_958321235}

[[主进程通过]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_16239_89686_958386771}[通道将]{style="font-family:宋体"}[VRF]{lang="EN-US"}[数据备份到备进程，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[The main process backed up the session reset event to the standby process through HA channel. Result: *result*.]{lang="EN-US"}]{#struct_0_16239_89686_958255699}

[[主进程通过]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_16239_89686_958583379}[通道将会话]{style="font-family:宋体"}[reset]{lang="EN-US"}[事件备份到备进程，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[The session thread received a Stop messge from the main process.]{lang="EN-US"}]{#struct_0_16239_89686_958648915}

[[SESSION]{lang="EN-US"}]{#struct_0_16239_89686_x1770824261}[线程收到主进程发送的]{style="font-family:宋体"}[Stop]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[The session thread received a Upgrade messge from the main process.]{lang="EN-US"}]{#struct_0_16239_89686_x1770758725}

[[SESSION]{lang="EN-US"}]{#struct_0_16239_89686_x1770889797}[线程收到主进程发送的升级消息]{style="font-family:宋体"}

[[The main process backed up the data of update-group *group-id* to the standby process through HA channel. Result: *result*.]{lang="EN-US"}]{#struct_0_16239_89686_x1770562117}

[[主进程通过]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_16239_89686_x1770496581}[通道将打包组]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[的打包组数据备份到备进程，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[The send thread received a Stop messge from the main process.]{lang="EN-US"}]{#struct_0_16239_89686_x1770693189}

[[SEND]{lang="EN-US"}]{#struct_0_16239_89686_x1770299973}[线程收到主进程发送的]{style="font-family:宋体"}[Stop]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[The send thread received a Upgrade messge from the main process.]{lang="EN-US"}]{#struct_0_16239_89686_x1770234437}

[[SEND]{lang="EN-US"}]{#struct_0_16239_89686_x1770824260}[线程收到主进程发送的升级消息]{style="font-family:宋体"}

[[Triggered the main process to backup data to the standby processes in batches. Trigger type: *type*, result: *result*.]{lang="EN-US"}]{#struct_0_16239_89686_x1770758724}

[[触发主进程向备进程通知批备数据，触发类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_16239_89686_x1770955332}[，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Notified the main thread to decrease the HA_UPGRADE_Cnt to *number*.]{lang="EN-US"}]{#struct_0_16239_89686_x1770562116}

[[通知主线程将]{style="font-family:宋体"}[HA_UPGRADE_Cnt]{lang="EN-US"}]{#struct_0_16239_89686_x1770496580}[减少为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Notified the main thread to decrease the HA_STOP_Cnt to *number*.]{lang="EN-US"}]{#struct_0_16239_89686_x1770693188}

[[通知主线程将]{style="font-family:宋体"}[HA_UPGRADE_Cnt]{lang="EN-US"}]{#struct_0_16239_89686_x1770299972}[减少为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Notified the main thread to decrease the HA_BATCH_Cnt to *number*.]{lang="EN-US"}]{#struct_0_16239_89686_x1770234436}

[[通知主线程将]{style="font-family:宋体"}[HA_BATCH_Cnt]{lang="EN-US"}]{#struct_0_16239_89686_x1770824263}[减少为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[The BRIB thread received a Upgrade messge from the main process.]{lang="EN-US"}]{#struct_0_16239_89686_x1770758727}

[[BRIB]{lang="EN-US"}]{#struct_0_16239_89686_x1770889799}[线程收到主进程发送的升级消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x707217593}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_x1770693190}[在]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息]{style="font-family:宋体"}[开关。在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[之间建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，并且会话处于]{style="font-family:宋体"}[Established]{lang="EN-US"}[状态。]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上配置]{style="font-family:宋体"}[NSR]{lang="EN-US"}[时，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp ha]{lang="EN-US"}]{#struct_0_16239_89686_1313678835}

[\*May 19 20:33:54:844 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP-HA: The main process received an HA message. Type: 0x00000001.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770627654}*[接收到类型为]{style="font-family:宋体"}[0x00000001]{lang="EN-US"}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x583236465}

[ BGP-HA: The standby process received realtime backup data from the main process. Data type: 0x0001.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770299974}*[备进程从主进程接收实备数据，数据类型为]{style="font-family:宋体"}[0x0001]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[ BGP-HA: The standby process finished processing the realtime backup data. Result: 0x01.]{lang="EN-US"}]{#struct_0_16239_89686_x1770234438}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x310980378}*[备进程从主进程接收实备数据，数据类型为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770824265}

[ BGP-HA: The standby process finished processing the realtime backup data. Result: 0x01.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770758729}*[实备数据完成，返回值为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x198898744}

[ BGP-HA: Begin backing up data in batches.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770955337}*[批备数据开始。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770889801}

[ BGP-HA: Finished backing up data in batches.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1462660468}*[批备数据完成。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770562121}

[ BGP-HA: Started to process the received HA message. Message type: 0x01.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_2043264109}*[开始处理接收到的]{style="font-family:宋体"}[HA]{lang="EN-US"}[消息，消息类型为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770496585}

[ BGP-HA: The main process backed up the configuration data to the standby process through HA channel. Result: 0x01.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770693193}*[主进程通过]{style="font-family:宋体"}[HA]{lang="EN-US"}[通道将配置数据备份到备进程，返回值为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_910394308}

[ BGP-HA: Received an unknown HA message. Message type: 0x01.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770627657}*[收到未知类型的]{style="font-family:宋体"}[HA]{lang="EN-US"}[消息，消息类型为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770299977}

[ BGP-HA: The main process sent data to the backup process in batches through the HA channel. Result: 0x01.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_1549906256}*[主进程通过批备通道给备进程发送数据，返回值为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770234441}

[ BGP-HA: BGP notified HA that the operation 0x01 completed.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770824264}*[通知]{style="font-family:宋体"}[HA]{lang="EN-US"}[操作完成，操作类型为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x998079341}

[ BGP-HA: The main process backed up the VRF data to the standby process through HA channel. Result: 0x01.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770758728}*[主进程通过]{style="font-family:宋体"}[HA]{lang="EN-US"}[通道将]{style="font-family:宋体"}[VRF]{lang="EN-US"}[数据备份到备进程，返回值为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770955336}

[ BGP-HA: The main process backed up the session reset event to the standby process through HA channel. Result: 0x01.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_1932176891}*[主进程通过]{style="font-family:宋体"}[HA]{lang="EN-US"}[通道将会话]{style="font-family:宋体"}[reset]{lang="EN-US"}[事件备份到备进程，返回值为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770889800}

[ BGP-HA: The session thread received a Stop messge from the main process.]{lang="EN-US"}

[*[// BGP-HA SESSION]{lang="EN-US"}*]{#struct_0_16239_89686_1266222887}*[线程收到主进程发送的]{style="font-family:宋体"}[Stop]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770562120}

[ BGP-HA: The session thread received a Upgrade messge from the main process.]{lang="EN-US"}

[*[// BGP-HA SESSION]{lang="EN-US"}*]{#struct_0_16239_89686_x1770496584}*[线程收到主进程发送的升级消息。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x613592189}

[ BGP-HA: Triggered the main process to backup data to the standby processes in batches. Trigger type: 0x01. result: 0x02.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1770693192}*[触发主进程向备进程通知批备数据，触发类型为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[，返回值为]{style="font-family:宋体"}[0x02]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770627656}

[ BGP-HA: Notified the main thread to decrease the HA_UPGRADE_Cnt to 1.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1746035879}*[通知主线程将]{style="font-family:宋体"}[HA_UPGRADE_Cnt]{lang="EN-US"}[减少为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770299976}

[ BGP-HA: Notified the main thread to decrease the HA_STOP_Cnt to 2.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x1178977099}*[通知主线程将]{style="font-family:宋体"}[HA_UPGRADE_Cnt]{lang="EN-US"}[减少为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1770234440}

[BGP-HA: Notified the main thread to decrease the HA_BATCH_Cnt to 3.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x204740320}*[通知主线程将]{style="font-family:宋体"}[HA_BATCH_Cnt]{lang="EN-US"}[减少为]{style="font-family:宋体"}[ 3]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1795027335}

[BGP-HA: The BRIB thread received a Upgrade messge from the main process.]{lang="EN-US"}

[*[// BGP-HA]{lang="EN-US"}*]{#struct_0_16239_89686_x204674784}*[的]{style="font-family:宋体"}[BRIB]{lang="EN-US"}[线程收到主进程发送的升级消息。]{style="font-family:宋体"}*

::: {#-1994793985 .myid}
[]{#_Toc404788308}[]{#struct_0_16239_89686_272774987}[]{#_Toc205722847}

**BGP \-- BGP调试命令 \-- debugging bgp ipc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_429277369}

[**[debugging bgp]{lang="EN-US"}**[ **ipc**]{lang="EN-US"}]{#struct_0_16239_89686_x841554379}

[**[undo debugging bgp]{lang="EN-US"}**[ **ipc**]{lang="EN-US"}]{#struct_0_16239_89686_180698822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_1512359833}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_926365057}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x204478176}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x204412640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x204609248}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_x775229279}

[[无]{style="font-family:宋体"}]{#struct_0_16239_89686_x707020985}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x409407371}

[**[debugging bgp ipc]{lang="EN-US"}**]{#struct_0_16239_89686_x1005170888}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的线程间通信调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp ipc]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的线程间通信调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1682258005}[线程间通信调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[打开此调试信息开关，会打印]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1499058907}[各线程间的调试信息，信息中给出了当前触发的信号量。如果]{style="font-family:宋体"}[BGP]{lang="EN-US"}[在线程通信过程中发生问题，可以打开该调试信息开关定位。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging bgp ipc]{lang="EN-US"}]{#struct_0_16239_89686_x241257515}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_909416381}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x47593052}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x633666846}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1579288158}

[[数据包属于]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x706431161}[协议]{style="font-family:宋体"}

[[MAIN/SEND/BRIB/]{lang="EN-US"}[SESSION/CALC/RELY]{lang="EN-US"}]{#struct_0_16239_89686_381707778}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_2076864838}[各线程]{style="font-family:宋体"}

[[receive]{lang="EN-US"}]{#struct_0_16239_89686_1498675693}

[[接收事件]{style="font-family:宋体"}]{#struct_0_16239_89686_x1414351293}

[[process]{lang="EN-US"}]{#struct_0_16239_89686_x1056418251}

[[处理事件]{style="font-family:宋体"}]{#struct_0_16239_89686_x308949618}

[[sent]{lang="EN-US"}]{#struct_0_16239_89686_x706365625}

[[发送事件]{style="font-family:宋体"}]{#struct_0_16239_89686_1506949157}

[[Notify done]{lang="EN-US"}]{#struct_0_16239_89686_900283448}

[[通知事件处理完成]{style="font-family:宋体"}]{#struct_0_16239_89686_1277957342}

[[0x00072005]{lang="EN-US"}]{#struct_0_16239_89686_x616138005}

[[信号量]{style="font-family:宋体"}]{#struct_0_16239_89686_1492481777}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x706955452}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_1131034824}[在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[IPC]{lang="EN-US"}[调试信息]{style="font-family:宋体"}[开关。在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[之间建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，并且会话处于]{style="font-family:宋体"}[Established]{lang="EN-US"}[状态。]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上配置一条命令时，设备上将打印如下调试信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp ipc]{lang="EN-US"}]{#struct_0_16239_89686_1488667313}

[ \*May 19 20:33:54:844 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND    receive EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:845 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ Send SIGNAL: SIG_SEND   to SEND.]{lang="EN-US"}

[*[// Send]{lang="EN-US"}*]{#struct_0_16239_89686_387175680}*[线程收到给自己的发送信号。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1148262326}

[ SEND    process EVENT : 0x00072005.]{lang="EN-US"}

[*[// Send]{lang="EN-US"}*]{#struct_0_16239_89686_x622955701}*[线程处理事件。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1378067435}

[ SEND    notify  EVENT : 0x00072005 done.]{lang="EN-US"}

[*[// Send]{lang="EN-US"}*]{#struct_0_16239_89686_x706889916}*[线程通知事件完成。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x763491495}

[ Send SIGNAL: SIG_MAIN   to MAIN.]{lang="EN-US"}

[*[// Send]{lang="EN-US"}*]{#struct_0_16239_89686_x1768909337}*[线程发送信号给]{style="font-family:宋体"}[MAIN]{lang="EN-US"}[线程。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1989023073}

[ BRIB    receive EVENT : 0x00072005.]{lang="EN-US"}

[*[// BRIB]{lang="EN-US"}*]{#struct_0_16239_89686_1380217878}*[线程接收到事件。]{style="font-family:宋体"}*

[[\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x706824380}

[ Send SIGNAL: SIG_BRIB   to BRIB.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BRIB    process EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BRIB    notify  EVENT : 0x00072005 done.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SESSION receive EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ MAIN    process EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ MAIN    process EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SESSION process EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SESSION notify  EVENT : 0x00072005 done.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:849 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ Send SIGNAL: SIG_MAIN   to MAIN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:849 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ MAIN    process EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:849 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND    receive EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ Send SIGNAL: SIG_SEND   to SEND.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND    process EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND    notify  EVENT : 0x00072005 done.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ Send SIGNAL: SIG_MAIN   to MAIN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:851 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BRIB    receive EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:852 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ Send SIGNAL: SIG_BRIB   to BRIB.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:852 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BRIB    process EVENT : 0x00072005.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 19 20:33:54:852 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BRIB    notify  EVENT : 0x00072005 done.]{lang="EN-US"}

::: {#-659974581 .myid}
[]{#_Toc404788309}[]{#struct_0_16239_89686_x204674786}[]{#_Toc353628999}[]{#_Toc346636105}

**BGP \-- BGP调试命令 \-- debugging bgp non-stop-routing**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x204871394}

[**[debugging bgp non-stop-routing]{lang="EN-US"}**]{#struct_0_16239_89686_231499400}

[**[undo debugging non-stop-routing]{lang="EN-US"}**]{#struct_0_16239_89686_x204805858}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_x204478178}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x204412642}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x935262160}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x204609250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x204543714}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_x204216034}

[[无]{style="font-family:宋体"}]{#struct_0_16239_89686_1008392691}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x204150498}

[**[debugging bgp]{lang="EN-US"}**[ **non-stop-routing**]{lang="EN-US"}]{#struct_0_16239_89686_x204740321}[命令用来打开]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp]{lang="EN-US"}**[ **non-stop-routing**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}]{#struct_0_16239_89686_x204674785}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[打开此调试信息开关，会打印出]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}]{#struct_0_16239_89686_592954392}[过程的调试信息，包括]{style="font-family:宋体"}[NSR]{lang="EN-US"}[开始、]{style="font-family:宋体"}[NSR]{lang="EN-US"}[结束等信息。如果]{style="font-family:宋体"}[BGP]{lang="EN-US"}[在]{style="font-family:宋体"}[NSR]{lang="EN-US"}[过程中发生问题，可以打开该调试信息开关定位问题。打开调试信息开关会影响系统的性能，因此，请不要轻易打开调试信息开关，调试完毕后，请及时关闭调试信息开关。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging bgp non-stop-routing]{lang="EN-US"}]{#struct_0_16239_89686_x204871393}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1879451448}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x204478177}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x204412641}

[[BGP_NSR]{lang="EN-US"}]{#struct_0_16239_89686_x204543713}

[[BGP NSR]{lang="EN-US"}]{#struct_0_16239_89686_x204216033}[相关信息]{style="font-family:宋体"}

[[Received NSR batch backup start event, and notified *number* threads]{lang="EN-US"}]{#struct_0_16239_89686_x204740324}

[[收到]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_16239_89686_x204674788}[批备消息，已经通知]{style="font-family:宋体"}*[number]{lang="EN-US"}*[个线程开始批备]{style="font-family:宋体"}[NSR]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[Notified the standby process to start batch backup. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_x204871396}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x204478180}[通知备板开始批备，结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Notified the BGP standby process that the memory of the BGP primary process had reached the critical state. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_x204412644}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x204543716}[主进程达到三级内存门限，通知备进程，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Received ACK message from HA. Type: *type*, length: *length*]{lang="EN-US"}]{#struct_0_16239_89686_x204216036}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x204740323}[接收到]{style="font-family:宋体"}[HA]{lang="EN-US"}[回复的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[消息，类型值为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Received a BGP message from BGP peer *peer-address*, and backed up the information of the message to the standby process through HA. Information length: *length*, result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_x204674787}

[[收到]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x204805859}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[,]{lang="EN-US"}[发送的报文后通过]{style="font-family:宋体"}[HA]{lang="EN-US"}[将报文信息备份到备板，备份的信息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[字节，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Backed up the *event-type* event to the standby process for BGP peer *peer-address* (*address-family*)]{lang="EN-US"}]{#struct_0_16239_89686_x204478179}

[[为地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_16239_89686_x204609251}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[将]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[消息备份到备进程]{style="font-family:宋体"}

[*[address-family]{lang="EN-US"}*]{#struct_0_16239_89686_x204543715}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IPv4-UNC]{lang="EN-US"}]{#struct_0_16239_89686_x204150499}[：]{style="font-family:
  宋体"}[IPv4]{lang="EN-US"}[单播地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4-VPN]{lang="EN-US"}]{#struct_0_16239_89686_1361343621}[：]{lang="EN-US" style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6-UNC]{lang="EN-US"}]{#struct_0_16239_89686_1361212549}[：]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6-VPN]{lang="EN-US"}]{#struct_0_16239_89686_1361278085}[：]{lang="EN-US" style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族]{lang="EN-US" style="font-family:宋体"}

[*[event-type]{lang="EN-US"}*]{#struct_0_16239_89686_1361671301}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[refresh-in]{lang="EN-US"}]{#struct_0_16239_89686_1361474693}[：入方向的软重启事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[undo-keep-all-routes]{lang="EN-US"}]{#struct_0_16239_89686_1361867909}[：取消保存所有路由事件]{style="font-family:宋体"}

[[The batch backup of BRIB started. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361343622}

[[BRIB]{lang="EN-US"}]{#struct_0_16239_89686_1361409158}[开始批备，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Backed up the send status *status*. Time stamp: *time-stamp*, result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361278086}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361605766}[主进程备份]{style="font-family:宋体"}[send]{lang="EN-US"}[的状态]{style="font-family:宋体"}*[status]{lang="EN-US"}*[，时间戳为]{style="font-family:宋体"}*[time-stamp]{lang="EN-US"}*[，返回值是]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[BGP.*vpn-instance-name*]{lang="EN-US"}]{#struct_0_16239_89686_1361474694}

[[VPN]{lang="EN-US"}]{#struct_0_16239_89686_1361867910}[实例]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[内的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[相关信息]{style="font-family:宋体"}

[[Enabled the TCP NSR option of socket *socket-id* for BGP peer *peer-address*. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361343619}

[[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361409155}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[使能]{style="font-family:宋体"}[socket]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP NSR]{lang="EN-US"}[选项，]{style="font-family:宋体"}[Socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Disabled the TCP NSR option of socket *socket-id* for BGP peer *peer-address*. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361278083}

[[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361671299}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[关闭]{style="font-family:宋体"}[socket]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP NSR]{lang="EN-US"}[选项，]{style="font-family:宋体"}[Socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Set the preferred standby process of socket *socket-id* to the process located on slot *slot-number* for BGP peer *peer-address*. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361474691}

[[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361867907}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}[优选的备板号是]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Failed to delete the packet from the receive cache for BGP peer *peer-address* due to incorrect time-stamp]{lang="EN-US"}]{#struct_0_16239_89686_1361933443}

[[由于时间戳错误，为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361409156}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[删除接收缓冲区中的报文失败]{style="font-family:宋体"}

[[Deleted the packet from the cache of socket *socket-id* for BGP peer *peer-address*. Delete length: *delete-length*, remaining length: *remaining-length*]{lang="EN-US"}]{#struct_0_16239_89686_1361212548}

[[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361605764}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[删除]{style="font-family:宋体"}[socket]{lang="EN-US"}[缓冲区中的报文，]{style="font-family:宋体"}[Socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[，本次删除的报文长度为]{style="font-family:宋体"}*[delete-length]{lang="EN-US"}*[字节，剩余报文的长度为]{style="font-family:宋体"}*[remaining-length]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[After processing the null message for BGP peer *peer-address*, BGP notified the standby process that backup finished. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361671300}

[[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361540228}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[处理完空报文后通知备进程备份完成，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[After sending an Update message to BGP peer *peer-address*, BGP notified the standby process to delete the update message backed up previously. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361933444}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361343617}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息后，通知备进程删除之前备份的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[When processing the refresh event for ]{lang="EN-US"}]{#struct_0_16239_89686_1361212545}[BGP peer *peer-address*, BGP backed up the refresh state to the standby process. Result: *result*]{lang="EN-US"}

[[处理]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1361278081}[对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[的]{style="font-family:宋体"}[Refresh]{lang="EN-US"}[事件时，将]{style="font-family:宋体"}[Refresh]{lang="EN-US"}[状态备份到备进程，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[The batch backup of BGP session started. Result: *result*]{lang="EN-US"}]{#struct_0_16239_89686_1361671297}

[[BGP session]{lang="EN-US"}]{#struct_0_16239_89686_1361540225}[进程开始批备]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x570141913}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_1361867905}[配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议后，打开]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp non-stop-routing]{lang="EN-US"}]{#struct_0_16239_89686_1361933441}

[ \*May 19 20:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP_NSR: Received NSR batch backup start event, and notified 3 threads]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_1361343618}*[收到]{style="font-family:宋体"}[NSR]{lang="EN-US"}[批备消息，通知了]{style="font-family:宋体"}[3]{lang="EN-US"}[个线程开始批备。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1361409154}

[ BGP_NSR: Notified the standby process to start batch backup. Result: 0]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_x926670074}*[备份]{style="font-family:宋体"}[NSR]{lang="EN-US"}[批备开始消息。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1361212546}

[ BGP_NSR: Notified the BGP standby process that the memory of the BGP primary process had reached the critical state. Result: 0]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_1361278082}*[主进程内存门限时通知备进程删除数据消息。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1361605762}

[ BGP_NSR: Received ACK message from HA. Type: 1, length: 20]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_1372691083}*[接收到]{style="font-family:宋体"}[HA]{lang="EN-US"}[回复的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[消息，类型值]{style="font-family:宋体"}[1]{lang="EN-US"}[，消息长度]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1361671298}

[ BGP_NSR: Received a BGP message from BGP peer 1.1.1.1, and backed up the information of the message to the standby process through HA. Information length: 19, result: 0]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_1361474690}*[会话]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[接收到报文处理后向]{style="font-family:宋体"}[HA]{lang="EN-US"}[写入消息长度为]{style="font-family:宋体"}[19]{lang="EN-US"}[，返回值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1361540226}

[ BGP_NSR: Backed up the refresh-in event to the standby process for BGP peer 1.1.1.1 (IPv4-UNC)]{lang="EN-US"}

[*[// BGP IPv4]{lang="EN-US"}*]{#struct_0_16239_89686_1361867906}*[单播邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[备份]{style="font-family:宋体"}[refresh-in]{lang="EN-US"}[状态到备进程。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_1361933442}

[ BGP_NSR: Backed up the undo-keep-all-routes event to the standby process for BGP peer 1.1.1.1 (IPv4-UNC)]{lang="EN-US"}

[*[// BGP IPv4]{lang="EN-US"}*]{#struct_0_16239_89686_x2139443078}*[单播邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[备份]{style="font-family:宋体"}[undo-keep-all-routes]{lang="EN-US"}[状态到备进程。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1011309374}

[ BGP_NSR: The batch backup of BRIB started. Result: 0]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_x1011243838}*[备份]{style="font-family:宋体"}[BRIB]{lang="EN-US"}[备份开始消息。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1011440446}

[ BGP_NSR: Backed up the send status 1. Time stamp: 1, result: 0]{lang="EN-US"}

[*[// BGP SEND]{lang="EN-US"}*]{#struct_0_16239_89686_x1658685030}*[备份状态消息，时间戳为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1011374910}

[ BGP.vpn1: Enabled the TCP NSR option of socket 1 for BGP peer 1.1.1.1. Result: 0]{lang="EN-US"}

[*[// BGP ]{lang="EN-US"}*]{#struct_0_16239_89686_x1011047230}*[使能]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[tcp nsr]{lang="EN-US"}[选项。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1010981694}

[ BGP.vpn1: Set the preferred standby process of socket 2 to the process located on slot 2 for BGP peer 1.1.1.1. Result: 0]{lang="EN-US"}

[*[// BGP ]{lang="EN-US"}*]{#struct_0_16239_89686_672205593}*[设置]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的优选备选项。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1011178302}

[ BGP.vpn1: Failed to delete the packet from the receive cache for BGP peer 1.1.1.1 due to incorrect time-stamp]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x1011112766}*[时间戳错误，丢弃]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的报文。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1010785086}

[ BGP.vpn1: Deleted the packet from the cache of socket 2 for BGP peer peer-address. Deletelength: 20, remaining length: 30]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_16239_89686_x1911360431}*[通知]{style="font-family:宋体"}[TCP  drop]{lang="EN-US"}[掉]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[缓冲区。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1010719550}

[ BGP.vpn1: After processing the null message for BGP peer 1.1.1.1, BGP notified the standby process that backup finished. Result: 0.]{lang="EN-US"}

[*[// BGP  vpn1]{lang="EN-US"}*]{#struct_0_16239_89686_x1011309373}*[邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[处理完空报文向备进程备份消息。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1011243837}

[ BGP.vpn1: After sending an Update message to BGP peer 1.1.1.1, BGP notified the standby process to delete the update message backed up previously. Result: 0]{lang="EN-US"}

[*[// BGP  vpn1]{lang="EN-US"}*]{#struct_0_16239_89686_x1011440445}*[邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[发送完]{style="font-family:宋体"}[UPDATE]{lang="EN-US"}[报文后向备进程确认消息。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1255400503}

[ BGP.vpn1: When processing the refresh event for BGP peer 1.1.1.1, BGP backed up the refresh state to the standby process. Result: 0]{lang="EN-US"}

[*[// BGP  vpn1]{lang="EN-US"}*]{#struct_0_16239_89686_x1011374909}*[邻居]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[发送完除]{style="font-family:宋体"}[UPDATE]{lang="EN-US"}[外的其他报文后向备进程确认消息。]{style="font-family:宋体"}*

[[\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x1011047229}

[ BGP_NSR: The batch backup of BGP session started. Result: 0]{lang="EN-US"}

[*[// BGP SESSION]{lang="EN-US"}*]{#struct_0_16239_89686_x1010981693}*[备份开始消息。]{style="font-family:宋体"}*

::: {#1301953054 .myid}
[]{#_Toc404788310}[]{#struct_0_16239_89686_367182937}[]{#_Toc312411691}[]{#_Toc290478104}[]{#_Toc290478105}

**BGP \-- BGP调试命令 \-- debugging bgp prefix-list**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x706758844}

[**[debugging ]{lang="EN-US"}[bgp]{lang="EN-US"}**[ **prefix-list** *prefix-list-name*]{lang="EN-US"}]{#struct_0_16239_89686_x1566402976}

[**[undo debugging bgp prefix-list]{lang="EN-US"}**]{#struct_0_16239_89686_x1693113676}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_x2050682913}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x1119363714}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1011178301}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1011112765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1010785085}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_1292312869}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_16239_89686_743141272}[：用于匹配路由信息目的网络地址的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16239_89686_x584457243}

[**[debugging bgp prefix-list]{lang="EN-US"}**]{#struct_0_16239_89686_x707217596}[命令用来打开通过]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的调试信息开关。]{style="font-family:宋体"}**[undo debugging bgpprefix-list]{lang="EN-US"}**[命令]{style="font-family:
宋体"}[用来关闭通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1186025097}[路由的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果同时配置了本命令和]{style="font-family:宋体"}**[debugging bgp acl]{lang="EN-US"}**]{#struct_0_16239_89686_x928858512}[命令，则只有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由同时通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤，才会打开该路由的调试信息开关。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1509841229}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_1744944772}[通过配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤条件，打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[的调试信息开关。设备接收到对端发布的]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[和]{style="font-family:宋体"}[11.1.1.2/32]{lang="EN-US"}[两条路由后，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16239_89686_x825659321}

[\[Sysname\] ip prefix-list p1 permit 11.1.1.1 32]{lang="EN-US"}

[\[Sysname\] quit]{lang="EN-US"}

[\<Sysname\> debugging bgp update]{lang="EN-US"}

[\<Sysname\> debugging bgp prefix-list p1]{lang="EN-US"}

[\*Dec 20 16:02:33:923 2011 H3C BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: Recv UPDATE from peer 13.1.1.1 with following destinations:]{lang="EN-US"}

[         Update message length : 60]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 100]{lang="EN-US"}

[         Next hop     : 13.1.1.1]{lang="EN-US"}

[         MED          : 0]{lang="EN-US"}

[         11.1.1.1/32,]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_2113805067}*[对端发布两条路由]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[和]{style="font-family:宋体"}[11.1.1.2/32]{lang="EN-US"}[，只有]{style="font-family:宋体"}[11.1.1.1/32]{lang="EN-US"}[通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤，因此，只打印]{style="font-family:宋体"}[11.1.1.1/32 ]{lang="EN-US"}[的调试信息。]{style="font-family:宋体"}*
:::

::: {#1341680823 .myid}
[]{#_Toc404788311}[]{#struct_0_16239_89686_x707152060}[]{#_Toc205281028}

**BGP \-- BGP调试命令 \-- debugging bgp rely**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x771815514}

[**[debugging bgp rely]{lang="EN-US"}[ ]{lang="EN-US"}**[\[ **common** \| **tunnel** \]]{lang="EN-US"}]{#struct_0_16239_89686_839803092}

[**[undo debugging bgp rely ]{lang="EN-US"}**[\[ **common** \| **tunnel** \]]{lang="EN-US"}]{#struct_0_16239_89686_x369921484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1894869428}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x204765091}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1010981696}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1011178304}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1011112768}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1077392404}

[**[common]{lang="EN-US"}**]{#struct_0_16239_89686_x707086524}[：迭代到普通路由。]{style="font-family:宋体"}

[**[tunnel]{lang="EN-US"}**]{#struct_0_16239_89686_x1519593035}[：迭代到隧道。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1766396403}

[**[debugging bgp]{lang="SV"}[ ]{lang="SV"}[rely]{lang="EN-US"}**]{#struct_0_16239_89686_x394296081}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="SV"}[路由迭代]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp]{lang="SV"}[ ]{lang="SV"}[rely]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="SV"}[路由迭代]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_16239_89686_341970609}[BGP rely]{lang="SV"}[调试开关处于关闭状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x476846603}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_657136731}[打开]{style="font-family:宋体"}[BGP]{lang="SV"}[路由迭代]{style="font-family:
宋体"}[调试信息开关。设备上进行路由迭代时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp rely]{lang="SV"}]{#struct_0_16239_89686_x707020988}

[\*May 31 21:48:48:511 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="SV"}

[ RELY add rely node, Dest/Mask: 129.1.1.0/24 :]{lang="SV"}

[          InstKey         : IPv4-UNC/0]{lang="SV"}

[         Original NextHop: 192.168.136.1]{lang="SV"}

[         ]{lang="SV"}[Rely     NextHop: NULL]{lang="EN-US"}

[         NbrType         : 4097]{lang="EN-US"}

[         VrfIndexNexthop: 0]{lang="EN-US"}

[         TnlPolicy       :]{lang="EN-US"}

[         IfIndexOrig     : 0]{lang="EN-US"}

[         TunnelID        : 0]{lang="EN-US"}

[         Action          : 1]{lang="EN-US"}

[\*May 31 21:48:48:526 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ RELY process result, Dest/Mask: 129.1.1.0/24 :]{lang="EN-US"}

[InstKey         : IPv4-UNC/0]{lang="EN-US"}

[         Original NextHop: 192.168.136.1]{lang="EN-US"}

[         Old Rely NextHop: NULL]{lang="EN-US"}

[         New Rely NextHop: 0.0.0.0]{lang="EN-US"}

[         Table           : 0]{lang="EN-US"}

[         Type            : SUCCEDED]{lang="EN-US"}
:::

::: {#-740108864 .myid}
[]{#_Toc404788312}[]{#struct_0_16239_89686_x409210763}

**BGP \-- BGP调试命令 \-- debugging bgp timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1368330054}

[**[debugging bgp]{lang="EN-US"}**[ **timer** \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_x1114887126}

[**[undo debugging bgp]{lang="EN-US"}**[ **timer** \[ *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] *\| ipv6-address* \[ *prefix-length* \] } \]]{lang="EN-US"}]{#struct_0_16239_89686_x135976093}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_412285387}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_1578597185}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1011243839}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1011440447}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x92601089}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_x706431164}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_16239_89686_382035458}[：对等体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_16239_89686_195457686}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_16239_89686_x1087285095}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_16239_89686_288975046}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_1432983431}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[定时器超时调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1895921522}

[**[debugging bgp timer]{lang="EN-US"}**]{#struct_0_16239_89686_618341365}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp timer]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_498918611}[定时器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging bgp timer]{lang="EN-US"}]{#struct_0_16239_89686_x970503357}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_936446769}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x706365628}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_1506621477}

[[Peer X.X.X.X]{lang="EN-US"}]{#struct_0_16239_89686_x1033988035}

[[对端邻居的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_16239_89686_x873031933}[地址]{style="font-family:宋体"}

[[Peer *X:X::X:X*]{lang="EN-US"}]{#struct_0_16239_89686_x841183999}

[[对端邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_16239_89686_x2115855319}[地址]{style="font-family:宋体"}

[[CR Timer]{lang="EN-US"}]{#struct_0_16239_89686_x137114548}

[[重新尝试连接（]{style="font-family:宋体"}[Connect Retry]{lang="EN-US"}]{#struct_0_16239_89686_x706955451}[）定时器]{style="font-family:宋体"}

[[KA Timer]{lang="EN-US"}]{#struct_0_16239_89686_1131100360}

[[KeepAlive]{lang="EN-US"}]{#struct_0_16239_89686_x905898754}[超时定时器]{style="font-family:宋体"}

[[HD Timer]{lang="EN-US"}]{#struct_0_16239_89686_243963577}

[[连接超时定时器]{style="font-family:宋体"}]{#struct_0_16239_89686_x1109671464}

[[BGP Timers debugging is on]{lang="EN-US"}]{#struct_0_16239_89686_x54656034}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x706889915}[定时器调试信息开关处于打开状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x763557031}

[**[\# ]{lang="EN-US"}**]{#struct_0_16239_89686_930697570}[在设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[定时器调试信息开关。在设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上创建对等体]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[（设备]{style="font-family:宋体"}[B]{lang="EN-US"}[的地址），在设备]{style="font-family:宋体"}[B]{lang="EN-US"}[上不指定设备]{style="font-family:宋体"}[A]{lang="EN-US"}[为其对等体。此时，设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp timer]{lang="EN-US"}]{#struct_0_16239_89686_x145389086}

[\*Apr 16 18:12:50:861 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: 2.2.2.2 CR Timer Created.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x1227347352}*[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[创建重新尝试连接定时器。]{style="font-family:宋体"}*

::: {#586993084 .myid}
[]{#_Toc404788313}[]{#struct_0_16239_89686_x1327061939}[]{#_Toc205722851}

**BGP \-- BGP调试命令 \-- debugging bgp update**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1841381491}

[**[debugging bgp update ]{lang="EN-US"}**[\[ *ipv4-address* \[ *mask-length* \] \[ **ipv4** \[ **mdt** \| **multicast** \] \| **ipv6** \| **vpnv4** \| **vpnv6** \] \| *ipv6-address* \[ *prefix-length* \] \[ **ipv6** \[ **multicast** \] \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] { **ipv4** \| **vpnv4** } \| *ipv6-address* \[ *prefix-length* \] **ipv6** } \] \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_16239_89686_1041262657}

[**[undo]{lang="EN-US"}**[ **debugging bgp update** \[ *ipv4-address* \[ *mask-length* \] \[ **ipv4** \[ **mdt** \| **multicast** \] \| **ipv6** \| **vpnv4** \| **vpnv6** \] \| *ipv6-address* \[ *prefix-length* \] \[ **ipv6** \[ **multicast** \] \] \| **vpn-instance** *vpn-instance-name* { *ipv4-address* \[ *mask-length* \] { **ipv4** \| **vpnv4** } *\| ipv6-address* \[ *prefix-length* \] **ipv6** } \] \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_16239_89686_x1884398875}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_x706824379}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_367772752}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1010981698}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1011178306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_x1011112770}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_1251081365}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_16239_89686_427798652}[：对等体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_16239_89686_194998934}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_16239_89686_1720769119}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_16239_89686_x1784718298}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_16239_89686_x356692752}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族。]{style="font-family:宋体"}

[**[mdt]{lang="EN-US"}**]{#struct_0_16239_89686_x1010719554}[：表示]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_16239_89686_1298528761}[：表示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播地址族。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_16239_89686_x1349121640}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_16239_89686_x706758843}[：]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_16239_89686_x1566337440}[：]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_x244823990}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新报文调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_16239_89686_1662426430}[：接收的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_16239_89686_1175195372}[：发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1361800516}

[**[debugging bgp update]{lang="EN-US"}**]{#struct_0_16239_89686_1618797979}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新报文的调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp update]{lang="EN-US"}**[命令]{style="font-family:宋体"}[用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新报文的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x279021225}[更新报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**]{#struct_0_16239_89686_x1011374913}[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则表示单播地址族。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging bgp update ipv4]{lang="EN-US"}]{#struct_0_16239_89686_x387805950}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_935928679}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x1101165456}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x707217595}

[[BGP.xxx]{lang="EN-US"}]{#struct_0_16239_89686_1186090633}

[[当前实例名]{style="font-family:宋体"}]{#struct_0_16239_89686_x569215117}

[[Recv UPDATE from x.x.x.x]{lang="EN-US"}]{#struct_0_16239_89686_x1287952471}

[[从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x153800494}[邻居]{style="font-family:宋体"}[x.x.x.x]{lang="EN-US"}[收到更新路由]{style="font-family:宋体"}

[[Recv UPDATE from x:x::x:x]{lang="EN-US"}]{#struct_0_16239_89686_1800794900}

[[从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1186400779}[邻居]{style="font-family:宋体"}[x:x::x:x]{lang="EN-US"}[收到更新路由]{style="font-family:宋体"}

[[Recv UPDATE(Withdraw) from x.x.x.x ]{lang="EN-US"}]{#struct_0_16239_89686_x707152059}

[[从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x772405341}[邻居]{style="font-family:宋体"}[x.x.x.x]{lang="EN-US"}[收到撤销路由]{style="font-family:宋体"}

[[Recv UPDATE(Withdraw) from x:x::x:x]{lang="EN-US"}]{#struct_0_16239_89686_1859084371}

[[从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1389931862}[邻居]{style="font-family:宋体"}[x:x::x:x]{lang="EN-US"}[收到撤销路由]{style="font-family:宋体"}

[[Send UPDATE to x.x.x.x]{lang="EN-US"}]{#struct_0_16239_89686_1689898562}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_289067415}[邻居]{style="font-family:宋体"}[x.x.x.x]{lang="EN-US"}[发送更新路由]{style="font-family:宋体"}

[[Send UPDATE to x:x::x:x]{lang="EN-US"}]{#struct_0_16239_89686_x707086523}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1519134283}[邻居]{style="font-family:宋体"}[x:x::x:x]{lang="EN-US"}[发送更新路由]{style="font-family:宋体"}

[[Send UPDATE(Withdraw) to peer x.x.x.x]{lang="EN-US"}]{#struct_0_16239_89686_x1740737029}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1519380404}[邻居]{style="font-family:宋体"}[x.x.x.x]{lang="EN-US"}[发送撤销路由]{style="font-family:宋体"}

[[Send UPDATE(Withdraw) to peer x:x::x:x]{lang="EN-US"}]{#struct_0_16239_89686_1660159303}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1780079761}[邻居]{style="font-family:宋体"}[x:x::x:x]{lang="EN-US"}[发送撤销路由]{style="font-family:宋体"}

[[x.x.x.x/xx]{lang="EN-US"}]{#struct_0_16239_89686_x707020987}

[[目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16239_89686_x409538443}[掩码]{style="font-family:宋体"}

[[Update message length]{lang="EN-US"}]{#struct_0_16239_89686_939628063}

[[Update]{lang="EN-US"}]{#struct_0_16239_89686_595162740}[报文长度]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_16239_89686_x706431163}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_381838850}[的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_16239_89686_311075098}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1344076990}[的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_16239_89686_686786603}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x706365627}[的]{style="font-family:宋体"}[Next Hop]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Local pref]{lang="EN-US"}]{#struct_0_16239_89686_1506818085}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_112183233}[的]{style="font-family:宋体"}[Local Pref]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_16239_89686_x1048044529}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_222143883}[的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Community]{lang="EN-US"}]{#struct_0_16239_89686_x706955454}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1130903752}[的团体属性]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_16239_89686_x108164972}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1754348730}[的扩展团体属性]{style="font-family:宋体"}

[[Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*]{lang="EN-US"}]{#struct_0_16239_89686_x706889918}

[[向地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_16239_89686_x763884711}[的对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，下一跳地址为]{style="font-family:宋体"}*[next-hop]{lang="EN-US"}*

 

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x591989708}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_2066222358}[在两台设备]{style="font-family:宋体"}[A]{lang="EN-US"}[和]{style="font-family:宋体"}[B]{lang="EN-US"}[之间建立]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[会话。在设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新报文调试信息开关。]{style="font-family:宋体"}[A]{lang="EN-US"}[和]{style="font-family:宋体"}[B]{lang="EN-US"}[之间交互]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[单播路由时，将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update]{lang="EN-US"}]{#struct_0_16239_89686_x1005113284}

[\*Apr 16 21:06:16:48 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: Send UPDATE to peer 192.168.109.1 for following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 100]{lang="EN-US"}

[         Next hop     : 192.168.109.88]{lang="EN-US"}

[         111.1.1.1/32,]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_129104577}*[向]{style="font-family:宋体"}[192.168.109.1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文，发布路由]{style="font-family:宋体"}[111.1.1.1/32]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Apr 16 ]{lang="EN-US"}]{#struct_0_16239_89686_x706824382}[21:09:59:37]{lang="EN-US"}[ 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: Recv UPDATE from peer 192.168.109.1 with following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 500 501]{lang="EN-US"}

[         Next hop     : 192.168.109.1]{lang="EN-US"}

[         MED          : 150]{lang="EN-US"}

[ADD route, Dest/Mask: 12.12.12.0/24.]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 500 501]{lang="EN-US"}

[         Next hop     : 192.168.109.1]{lang="EN-US"}

[         MED          : 150]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_367051865}*[从]{style="font-family:宋体"}[192.168.109.1]{lang="EN-US"}[接收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文，该报文携带路由]{style="font-family:宋体"}[12.12.12.0/24]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Apr 16 21:09:59:58 2010 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x2020898796}

[ BGP.: Send UPDATE MSG to peer 192.168.109.87(IPv4-UNC) NextHop: 192.168.109.88.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x921874275}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[192.168.109.87]{lang="EN-US"}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文，下一跳地址为]{style="font-family:宋体"}[192.168.109.88]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#123873821 .myid}
[]{#_Toc404788314}[]{#struct_0_16239_89686_x1701892243}[]{#_Toc333321195}

**BGP \-- BGP调试命令 \-- debugging bgp update-group**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x2000923673}

[**[debugging bgp update-group ]{lang="EN-US"}**[\[ \[ **vpn-instance** *vpn-instance-name* \] { **ipv4** \| **ipv6** } \| **ipv4 mdt** \| { **ipv4** \| **ipv6** } **multicast** \]]{lang="EN-US"}]{#struct_0_16239_89686_486420454}

[**[undo debugging bgp update-group ]{lang="EN-US"}**[\[ \[ **vpn-instance** *vpn-instance-name* \] { **ipv4** \| **ipv6** } \| **ipv4 mdt** \| { **ipv4** \| **ipv6** } **multicast** \]]{lang="EN-US"}]{#struct_0_16239_89686_x706758846}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_x1566534048}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x212884626}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_555298855}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_555364391}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_554774568}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_16239_89686_7202047}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_554643496}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[打包组调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网打包组的调试信息开关。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_16239_89686_x1674153672}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_16239_89686_x1007033389}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族。]{style="font-family:宋体"}

[**[ipv4 mdt]{lang="EN-US"}**]{#struct_0_16239_89686_554709032}[：表示]{style="font-family:宋体"}[IPv4 MDT]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_16239_89686_1533531889}[：表示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播地址族。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_1067884516}

[**[debugging bgp update-group]{lang="EN-US"}**]{#struct_0_16239_89686_x707217598}[命令用来打开]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[打包组调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp update-group]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[打包组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1186418313}[打包组调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16239_89686_554905640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定任何参数，则表示打开或关闭所有打包组的调试信息开关。]{style="font-family:宋体"}]{#struct_0_16239_89686_665834005}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定]{style="font-family:宋体"}]{#struct_0_16239_89686_554709029}**[multicast]{lang="EN-US"}**[和]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**[参数，则表示单播地址族。]{style="font-family:宋体"}

[[表1-11 ]{lang="EN-US"}[debugging bgp update-group]{lang="EN-US"}]{#struct_0_16239_89686_1172571885}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_931436588}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x4735023}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x1005974279}

[[BGP.*vpn-instance-name*]{lang="EN-US"}]{#struct_0_16239_89686_635284710}

[[VPN]{lang="EN-US"}]{#struct_0_16239_89686_530962519}[实例]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[内的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组信息]{style="font-family:宋体"}

[[Send UPDATE to update-group *group-id*]{lang="EN-US"}]{#struct_0_16239_89686_x707152062}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x771946586}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送路由更新]{style="font-family:宋体"}

[[Send UPDATE(Withdraw) to update-group *group-id*]{lang="EN-US"}]{#struct_0_16239_89686_434355853}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1625238577}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送路由撤销]{style="font-family:宋体"}

[*[destination-address]{lang="EN-US"}*[/*mask-length*]{lang="EN-US"}]{#struct_0_16239_89686_427672133}

[[发布的路由前缀的目的地址和掩码]{style="font-family:宋体"}]{#struct_0_16239_89686_565423051}

[[Update message length]{lang="EN-US"}]{#struct_0_16239_89686_x707086526}

[[Update]{lang="EN-US"}]{#struct_0_16239_89686_x1519461963}[消息长度]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_16239_89686_x1082526985}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x710808637}[的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_16239_89686_x670337029}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_244664642}[的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_16239_89686_x707020990}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x409735050}[的]{style="font-family:宋体"}[Next Hop]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Local pref]{lang="EN-US"}]{#struct_0_16239_89686_2107652233}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x727961996}[的]{style="font-family:宋体"}[Local Pref]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_16239_89686_2021488222}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x706431166}[的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Community]{lang="EN-US"}]{#struct_0_16239_89686_382166530}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1111175729}[的团体属性]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_16239_89686_801768862}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1534640966}[的扩展团体属性]{style="font-family:宋体"}

[[update-group *group-id* *address-family* created]{lang="EN-US"}]{#struct_0_16239_89686_1334580434}

[[创建地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_16239_89686_x706365630}[的打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*

[[update-group *group-id* *address-family* deleted]{lang="EN-US"}]{#struct_0_16239_89686_1507145764}

[[删除地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_16239_89686_2124376791}[的打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_1045446029}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_1007847346}[打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组调试信息开关，发布]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由时，设备上将打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update-group]{lang="EN-US"}]{#struct_0_16239_89686_x706955453}

[\*Apr 16 21:06:16:48 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.: Send UPDATE to update-group 0 for following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 100]{lang="EN-US"}

[         Next hop     : 192.168.109.88]{lang="EN-US"}

[         111.1.1.1/32,]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1130969288}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组]{style="font-family:宋体"}[0]{lang="EN-US"}[发送路由更新，路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性为]{style="font-family:宋体"}[Incomplete]{lang="EN-US"}[，]{style="font-family:宋体"}[AS path]{lang="EN-US"}[属性为]{style="font-family:宋体"}[100]{lang="EN-US"}[，下一跳地址为]{style="font-family:宋体"}[192.168.109.88]{lang="EN-US"}[，发布的路由前缀为]{style="font-family:宋体"}[111.1.1.1/32]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_1801536569}[打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组调试信息开关，创建和删除打包组时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update-group]{lang="EN-US"}]{#struct_0_16239_89686_x1203893129}

[\*Aug 16 10:24:34:132 2012 PE2 BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ BGP.: update-group 0 IPv6-UNC created.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x2046713457}*[创建]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族的打包组]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 16 10:24:02:896 2012 PE2 BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_x2038266227}

[ BGP.: update-group 0 IPv6-UNC deleted.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_1862041298}*[删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族的打包组]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#1425602596 .myid}
[]{#_Toc404788315}[]{#struct_0_16239_89686_x1820014498}[]{#_Toc235419783}[]{#_Toc205722852}

**BGP \-- BGP调试命令 \-- debugging bgp urt**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16239_89686_x706889917}

[**[debugging bgp]{lang="EN-US"}**[ **urt** \[ **ipv4** \[ **mdt** \| **multicast** \] \| **ipv6** \[ **multicast** \] \| **l2vpn** \| **vpn-instance** *vpn-instance-name* \[ **ipv4** \| **ipv6** \| **vpnv4** \] \| **vpnv4** \| **vpnv6** \]]{lang="EN-US"}]{#struct_0_16239_89686_x763425959}

[**[undo debugging bgp]{lang="EN-US"}**[ **urt** \[ **ipv4** \[ **mdt** \| **multicast** \] \| **ipv6** \[ **multicast** \] \| **l2vpn** \| **vpn-instance** *vpn-instance-name* \[ **ipv4** \| **ipv6** \| **vpnv4** \] \| **vpnv4** \| **vpnv6** \]]{lang="EN-US"}]{#struct_0_16239_89686_204105807}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16239_89686_20503604}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16239_89686_x973662992}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16239_89686_555036707}

[[network-admin]{lang="EN-US"}]{#struct_0_16239_89686_555102243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16239_89686_554905635}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16239_89686_323779556}

[**[ipv4]{lang="EN-US"}**]{#struct_0_16239_89686_x1960327753}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族。]{style="font-family:宋体"}

[**[mdt]{lang="EN-US"}**]{#struct_0_16239_89686_555298851}[：表示]{style="font-family:宋体"}[IPv4 MDT]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_16239_89686_555364387}[：表示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播地址族。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_16239_89686_x706824381}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族。]{style="font-family:宋体"}

[**[l2vpn]{lang="EN-US"}**]{#struct_0_16239_89686_367248473}[：]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16239_89686_x282394765}[：表示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新、添加、删除路由的调试信息开关。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新、添加、删除路由的调试信息开关。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_16239_89686_2101745403}[：]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_16239_89686_14900817}[：]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16239_89686_1363858517}

[**[debugging bgp urt]{lang="EN-US"}**]{#struct_0_16239_89686_1673965035}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新、添加、删除路由的调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp urt]{lang="EN-US"}**[命令]{style="font-family:宋体"}[用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新、添加、删除路由的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，该调试开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16239_89686_145002929}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**]{#struct_0_16239_89686_554709028}[和]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**[参数，则表示单播地址族。]{style="font-family:宋体"}

[[表1-12 ]{lang="EN-US"}[debugging bgp urt]{lang="EN-US"}]{#struct_0_16239_89686_1440896325}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_928107323}[[字段]{style="font-family:黑体"}]{#struct_0_16239_89686_x706758845}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16239_89686_x1566468512}

[[BGP.*vpn-instance*]{lang="EN-US"}]{#struct_0_16239_89686_493155022}

[[VPN]{lang="EN-US"}]{#struct_0_16239_89686_1920532541}[实例]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*[的调试信息]{style="font-family:宋体"}

[[如果不携带]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*]{#struct_0_16239_89686_x2093998993}[参数，则表示公网的调试信息]{style="font-family:宋体"}

[[MODIFY]{lang="EN-US"}]{#struct_0_16239_89686_846370867}

[[修改路由信息]{style="font-family:宋体"}]{#struct_0_16239_89686_x603142029}

[[Dest/Mask]{lang="EN-US"}]{#struct_0_16239_89686_x707217597}

[[目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16239_89686_1185959561}[掩码]{style="font-family:宋体"}

[[Old attribute]{lang="EN-US"}]{#struct_0_16239_89686_x392804848}

[[原属性]{style="font-family:宋体"}]{#struct_0_16239_89686_x271255279}

[[New attribute]{lang="EN-US"}]{#struct_0_16239_89686_521756583}

[[修改后的属性]{style="font-family:宋体"}]{#struct_0_16239_89686_x707152061}

[[Old real nexthop]{lang="EN-US"}]{#struct_0_16239_89686_x771881050}

[[修改前的真实下一跳]{style="font-family:宋体"}]{#struct_0_16239_89686_1640926820}

[[New real nexthop]{lang="EN-US"}]{#struct_0_16239_89686_2038204174}

[[修改后的真实下一跳]{style="font-family:宋体"}]{#struct_0_16239_89686_1890924007}

[[ADD]{lang="EN-US"}]{#struct_0_16239_89686_1834822130}

[[添加一条路由信息]{style="font-family:宋体"}]{#struct_0_16239_89686_x707086525}

[[DELETE]{lang="EN-US"}]{#struct_0_16239_89686_x1519527499}

[[删除一条路由信息]{style="font-family:宋体"}]{#struct_0_16239_89686_1391035592}

[[Origin]{lang="EN-US"}]{#struct_0_16239_89686_227063413}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_141425459}[的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_16239_89686_x707020989}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x409145227}[的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_16239_89686_x1789904924}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x996605614}[的]{style="font-family:宋体"}[Next Hop]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Local pref]{lang="EN-US"}]{#struct_0_16239_89686_850756663}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_572270182}[的]{style="font-family:宋体"}[Local Pref]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_16239_89686_x706431165}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_381969922}[的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Community]{lang="EN-US"}]{#struct_0_16239_89686_1471687972}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1572830149}[的团体属性]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_16239_89686_x706365629}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_1506687013}[的扩展团体属性]{style="font-family:宋体"}

[[NbrId]{lang="EN-US"}]{#struct_0_16239_89686_x664305287}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x908105727}[的邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Outif]{lang="EN-US"}]{#struct_0_16239_89686_859128491}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_2038645986}[路由的物理出接口]{style="font-family:宋体"}

[[Logicif]{lang="EN-US"}]{#struct_0_16239_89686_682082765}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_85566149}[路由的逻辑出接口]{style="font-family:宋体"}

[[Metric ]{lang="EN-US"}]{#struct_0_16239_89686_x936623185}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_859194027}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Pref]{lang="EN-US"}]{#struct_0_16239_89686_x305630365}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_x1545735770}[路由的路由优选值]{style="font-family:宋体"}

[[ProtoID]{lang="EN-US"}]{#struct_0_16239_89686_1332859725}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_859259563}[路由的协议]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[SubProto]{lang="EN-US"}]{#struct_0_16239_89686_x2017931324}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_568322834}[路由的子协议]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Route common]{lang="EN-US"}]{#struct_0_16239_89686_85420855}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_716953361}[路由的通用信息]{style="font-family:宋体"}

[[Tag]{lang="EN-US"}]{#struct_0_16239_89686_x203384971}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_85486391}[路由信息的外部标记]{style="font-family:宋体"}

[[Outlabel]{lang="EN-US"}]{#struct_0_16239_89686_1002720851}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_85551927}[路由的出标签值]{style="font-family:宋体"}

[[Weight]{lang="EN-US"}]{#struct_0_16239_89686_x1259066138}

[[BGP]{lang="EN-US"}]{#struct_0_16239_89686_85617463}[路由信息的权重值]{style="font-family:宋体"}

[[ProcessID]{lang="EN-US"}]{#struct_0_16239_89686_506462327}

[[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16239_89686_85682999}

[[IpPrec]{lang="EN-US"}]{#struct_0_16239_89686_1536627869}

[[IP]{lang="EN-US"}]{#struct_0_16239_89686_85748535}[优先级]{style="font-family:宋体"}

[[QosLocID]{lang="EN-US"}]{#struct_0_16239_89686_1567070902}

[[Qos-Local-ID]{lang="EN-US"}]{#struct_0_16239_89686_x1103146037}[属性]{style="font-family:宋体"}

[[OriRD]{lang="EN-US"}]{#struct_0_16239_89686_85814071}

[[原始]{style="font-family:宋体"}[RD]{lang="EN-US"}]{#struct_0_16239_89686_x366623157}

[[VNID]{lang="EN-US"}]{#struct_0_16239_89686_84831031}

[[引入路由的]{style="font-family:宋体"}[VNID]{lang="EN-US"}]{#struct_0_16239_89686_1876882402}

[[ProtoID]{lang="EN-US"}]{#struct_0_16239_89686_84896567}

[[路由协议类型]{style="font-family:宋体"}]{#struct_0_16239_89686_x2069737038}

[[SubProID]{lang="EN-US"}]{#struct_0_16239_89686_85355318}

[[路由协议子类型]{style="font-family:宋体"}]{#struct_0_16239_89686_1415090567}

[[OrigProtoID]{lang="EN-US"}]{#struct_0_16239_89686_85420854}

[[源路由协议类型]{style="font-family:宋体"}]{#struct_0_16239_89686_x1621698799}

[[InstKey]{lang="EN-US"}]{#struct_0_16239_89686_85486390}

[[路由所属实例的]{style="font-family:宋体"}[Key]{lang="EN-US"}]{#struct_0_16239_89686_x1335931309}[值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16239_89686_x443694637}

[[\# ]{lang="EN-US"}]{#struct_0_16239_89686_859325099}[在设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新、添加、删除路由的调试信息开关。在两台设备]{style="font-family:宋体"}[A]{lang="EN-US"}[和]{style="font-family:宋体"}[B]{lang="EN-US"}[之间建立]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[会话，并在二者之间发布]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由。设备]{style="font-family:宋体"}[A]{lang="EN-US"}[上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp urt]{lang="EN-US"}]{#struct_0_16239_89686_858866347}

[\*Apr 16 22:24:11:24 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ ADD route, Dest/Mask: 14.14.14.14/32.]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 500 501]{lang="EN-US"}

[         Next hop     : 192.168.109.1]{lang="EN-US"}

[         MED           : 100]{lang="EN-US"}

[\*Apr 16 22:24:11:84 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ ADD route common, Dest/Mask: 14.14.14.14/32, InstKey: IPv4-UNC/0.]{lang="EN-US"}

[       Tag      : 0         , Outlabel   : 4294967295]{lang="EN-US"}

[       Weight   : 0        , ProtoID     : 6]{lang="EN-US"}

[       SubProID : 1        , ProcessID  : 0]{lang="EN-US"}

[       IpPrec   : 65535    , QosLocID   : 65535]{lang="EN-US"}

[                                OrigProtoID: 6]{lang="EN-US"}

[       OriRD    : 0x0,]{lang="EN-US"}

[       VNID     : 0x0]{lang="EN-US"}

[*[// IPv4]{lang="EN-US"}*]{#struct_0_16239_89686_85617462}*[地址族下收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文，添加一条路由信息。]{style="font-family:宋体"}*

[[\*Apr 16 22:24:11:104 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_85682998}

[ MODIFY route common, Dest/Mask: 14.14.14.14/32, InstKey: IPv4-UNC/0.]{lang="EN-US"}

[ Old : Tag      : 0         , Outlabel   : 4294967295]{lang="EN-US"}

[       Weight   : 0         ,  ProtoID    : 6]{lang="EN-US"}

[       SubProID : 1         , ProcessID  : 0]{lang="EN-US"}

[       IpPrec   : 5         ,  QosLocID   : 5]{lang="EN-US"}

[                                 OrigProtoID: 6]{lang="EN-US"}

[       OriRD    : 0x0,]{lang="EN-US"}

[       VNID     : 0x0]{lang="EN-US"}

[ New : Tag      : 0         , Outlabel   : 4294967295]{lang="EN-US"}

[       Weight   : 0         ,  ProtoID    : 6]{lang="EN-US"}

[       SubProID : 1         , ProcessID  : 0]{lang="EN-US"}

[       IpPrec   : 65535     , QosLocID   : 65535]{lang="EN-US"}

[                                 OrigProtoID: 6]{lang="EN-US"}

[       OriRD    : 0x0]{lang="EN-US"}

[       VNID     : 0x0]{lang="EN-US"}

[\*Apr 16 22:24:11:123 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND Process Prefix. 14.14.14.14/32,  AttrId: 6, Op: ADD.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_16239_89686_x568779722}*[修改路由的属性值。]{style="font-family:宋体"}*

[[\*Apr 16 22:30:32:108 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_16239_89686_858931883}

[ DELETE Route, Dest/Mask: 14.14.14.14/32.]{lang="EN-US"}

[\*Apr 16 22:30:32:110 2010 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND Process Prefix. 14.14.14.14/32,  AttrId: 0, Op: DELETE.]{lang="EN-US"}

[*[// IPv4]{lang="EN-US"}*]{#struct_0_16239_89686_571796610}*[地址族下收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文，删除一条路由信息。]{style="font-family:宋体"}*
