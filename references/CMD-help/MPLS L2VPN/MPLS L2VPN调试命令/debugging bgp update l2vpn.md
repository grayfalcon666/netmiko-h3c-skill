::: {#1160184339 .myid}
[]{#_Toc131060009}[]{#_Toc404791331}[]{#struct_0_15149_x1311_x561944794}[]{#_Toc338865536}[]{#_Toc324777163}[]{#_Toc304293040}

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging bgp update l2vpn**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1993052096}

[**[debugging bgp update]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **l2vpn** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_15149_x1311_x8569112}

[**[undo debugging bgp update]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **l2vpn** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_15149_x1311_x1736532170}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15149_x1311_830210636}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1044502834}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15149_x1311_2034434026}

[[network-admin]{lang="EN-US"}]{#struct_0_15149_x1311_x1320077644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15149_x1311_301986145}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1159429097}

[*[ip-address]{lang="EN-US"}*]{#struct_0_15149_x1311_612609639}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_15149_x1311_x505854718}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_15149_x1311_x1992855488}[：表示接收的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_15149_x1311_2075142105}[：表示发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15149_x1311_46272859}

[**[debugging bgp update l2vpn]{lang="EN-US"}**]{#struct_0_15149_x1311_x62405199}[命令用来打开]{style="font-family:
宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:
宋体"}[Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging bgp l2vpn**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x1469549305}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging bgp update l2vpn]{lang="EN-US"}]{#struct_0_15149_x1311_x770067647}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1316991828}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1133557603}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_760699423}

[[BGP_L2VPN.: Recv UPDATE from peer *ip-address* with following destinations]{lang="EN-US"}]{#struct_0_15149_x1311_x1775641163}

[[从对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_15149_x1311_x1992921024}[接收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[BGP_L2VPN.: Send UPDATE to peer *ip-address* for following destinations]{lang="EN-US"}]{#struct_0_15149_x1311_x463387950}

[[向对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_15149_x1311_1699565861}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Update message length]{lang="EN-US"}]{#struct_0_15149_x1311_1913959896}

[[Update]{lang="EN-US"}]{#struct_0_15149_x1311_x1810680764}[消息的长度，单位为字节]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_15149_x1311_1185942032}

[[Origin]{lang="EN-US"}]{#struct_0_15149_x1311_x1993379779}[属性，即信息的来源，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IGP]{lang="EN-US"}]{#struct_0_15149_x1311_x1250824892}[：表示产生于本]{style="font-family:宋体"}[AS]{lang="EN-US"}[内]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EGP]{lang="EN-US"}]{#struct_0_15149_x1311_219760568}[：表示是通过]{style="font-family:宋体"}[EGP]{lang="EN-US"}[学到的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incomplete]{lang="EN-US"}]{#struct_0_15149_x1311_x1158108617}[：表示来源无法确定]{lang="EN-US" style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_15149_x1311_x2127565810}

[[AS Path]{lang="EN-US"}]{#struct_0_15149_x1311_122664783}[属性，即从本地到目的地所要经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Next hop]{lang="DA"}]{#struct_0_15149_x1311_x1993445315}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_15149_x1311_900331787}

[[Local pref]{lang="EN-US"}]{#struct_0_15149_x1311_x1427267611}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_15149_x1311_963581859}

[[MED]{lang="EN-US"}]{#struct_0_15149_x1311_148822139}

[[MED]{lang="EN-US"}]{#struct_0_15149_x1311_x1993248707}[（]{style="font-family:宋体"}[Multi-Exit Discriminator]{lang="EN-US"}[，多出口区分）值]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_15149_x1311_x1990127655}

[[扩展团体属性，包括：]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1744324823}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_15149_x1311_x1240633677}[：]{lang="EN-US" style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2VPN info]{lang="EN-US"}]{#struct_0_15149_x1311_1538935013}[：]{lang="EN-US" style="font-family:宋体"}[L2VPN]{lang="EN-US"}[相关信息，包括]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[值、封装类型（]{lang="EN-US" style="font-family:宋体"}[Encap type]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS ID]{lang="EN-US"}]{#struct_0_15149_x1311_x1993314243}[：用来标识该]{style="font-family:宋体"}[PE]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[AFI/SAFI]{lang="DA"}]{#struct_0_15149_x1311_2023517015}

[[地址族]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15149_x1311_1787867878}[子地址族]{style="font-family:宋体"}

[[RD]{lang="EN-US"}]{#struct_0_15149_x1311_x230566847}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_15149_x1311_1931475266}

[[Site ID]{lang="EN-US"}]{#struct_0_15149_x1311_x1993117635}

[[VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x1603293255}[内站点的编号]{style="font-family:宋体"}

[[Label offset]{lang="DA"}]{#struct_0_15149_x1311_1817926504}

[[标签块偏移量]{style="font-family:宋体"}]{#struct_0_15149_x1311_896724276}

[[Label base]{lang="DA"}]{#struct_0_15149_x1311_x1993183171}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_15149_x1311_892820025}

[[Label range]{lang="DA"}]{#struct_0_15149_x1311_480136616}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_15149_x1311_x451676168}

[[CSV]{lang="DA"}]{#struct_0_15149_x1311_x1992986563}

[[接入链路状态]{style="font-family:宋体"}]{#struct_0_15149_x1311_114454716}

[[PE address]{lang="EN-US"}]{#struct_0_15149_x1311_783023142}

[[PE]{lang="EN-US"}]{#struct_0_15149_x1311_1774028474}[的地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15149_x1311_213487669}

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_11869797}[打开对等体]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关。从对等体]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文时打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update 1.1.1.3 l2vpn receive]{lang="EN-US"}]{#struct_0_15149_x1311_x1993052099}

[\*Sep 24 06:44:31:368 2012 Sysname BGP/7/DEBUG: -MDC=1;                              ]{lang="DA"}

[         BGP_L2VPN.: Recv UPDATE from peer 1.1.1.3 with following destinations: ]{lang="DA"}

[         Update message length : 87                                             ]{lang="DA"}

[         Origin       : IGP                                                     ]{lang="DA"}

[         AS path      : 100                                                     ]{lang="DA"}

[         Next hop     : 1.1.1.3                                                 ]{lang="DA"}

[         Ext-Community: \<RT: 3:2\>, \<L2VPN info: MTU 1500, Encap type ATM AAL5 VCC transport\>]{lang="DA"}

[         AFI/SAFI     : 196/128 (L2VPN Draft)                                     ]{lang="DA"}

[         RD           : 9:8                                                     ]{lang="DA"}

[         Site ID      : 9                                                       ]{lang="DA"}

[         Label offset : 0                                                       ]{lang="DA"}

[         Label base   : 775000                                                  ]{lang="DA"}

[         Label range  : 10 ]{lang="DA"}

[         CSV          : 0x01000AFFFF]{lang="DA"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1574653053}*[从对等体]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，消息长度为]{style="font-family:宋体"}[87]{lang="EN-US"}[字节，标签块信息]{style="font-family:宋体"}[产生于本]{style="font-family:宋体"}[AS]{lang="EN-US"}[内]{style="font-family:宋体"}[，]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径为]{style="font-family:宋体"}[100]{lang="EN-US"}[，下一跳为]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[，]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性为]{style="font-family:宋体"}[3:2]{lang="EN-US"}[，]{style="font-family:宋体"}[MTU]{lang="EN-US"}[为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节，封装类型为]{style="font-family:宋体"}[ATM AAL5 VCC transport]{lang="DA"}[，地址族为]{style="font-family:宋体"}[196]{lang="EN-US"}[，子地址族为]{style="font-family:宋体"}[128]{lang="EN-US"}[，路由标识符为]{style="font-family:宋体"}[9:8]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内站点编号为]{style="font-family:宋体"}[9]{lang="EN-US"}[，标签块偏移量为]{style="font-family:宋体"}[0]{lang="EN-US"}[，标签块的初始标签值为]{style="font-family:宋体"}[775000]{lang="EN-US"}[，标签块大小为]{style="font-family:宋体"}[10]{lang="EN-US"}[，接入链路状态值为]{style="font-family:宋体"}[0x01000AFFFF]{lang="DA"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x1252277389}[打开对等体]{style="font-family:宋体"}[2.2.2.3]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关。从对等体]{style="font-family:宋体"}[2.2.2.3]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文时打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update 2.2.2.3 l2vpn receive]{lang="EN-US"}]{#struct_0_15149_x1311_x1992855491}

[[\*Sep 25 04:32:32:336 2012 Sysname BGP/7/DEBUG: -MDC=1;                              ]{lang="EN-US"}]{#_Toc333326093}

[         BGP_L2VPN.: Recv UPDATE from peer 2.2.2.3 with following destinations: ]{lang="EN-US"}

[         Update message length : 82                                             ]{lang="EN-US"}

[         Origin       : IGP                                                     ]{lang="EN-US"}

[         AS path      : 100                                                        ]{lang="EN-US"}

[         Next hop     : 2.2.2.3                                                 ]{lang="EN-US"}

[         Local pref   : 100                                                     ]{lang="EN-US"}

[         Ext-Community: \<RT: 3:2\>, \<VPLS ID: 5:67\>                              ]{lang="EN-US"}

[         AFI/SAFI     : 25/65 (L2VPN)                                     ]{lang="EN-US"}

[         RD           : 5:1                                                     ]{lang="EN-US"}

[         PE address   : 1.2.3.4 ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1009906074}*[从对等体]{style="font-family:宋体"}[2.2.2.3]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，消息长度为]{style="font-family:宋体"}[82]{lang="EN-US"}[字节，邻居自动发现信息]{style="font-family:宋体"}[产生于本]{style="font-family:宋体"}[AS]{lang="EN-US"}[内]{style="font-family:宋体"}[，]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径为]{style="font-family:宋体"}[100]{lang="EN-US"}[，下一跳为]{style="font-family:宋体"}[2.2.2.3]{lang="EN-US"}[，]{style="font-family:宋体"}[ Route Target]{lang="EN-US"}[属性为]{style="font-family:宋体"}[3:2]{lang="EN-US"}[，]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[为]{style="font-family:宋体"}[5:67]{lang="EN-US"}*[，*地址族为*]{style="font-family:宋体"}*[25]{lang="EN-US"}[，子地址族为]{style="font-family:宋体"}[65]{lang="EN-US"}[，]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[5:1]{lang="EN-US"}[，]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[1.2.3.4]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#933677320 .myid}
[]{#_Toc404791332}[]{#struct_0_15149_x1311_x1926574964}[]{#_Toc338865569}[]{#_Toc338865537}[]{#_Toc338865538}[]{#_Toc338865539}[]{#_Toc338865540}[]{#_Toc338865541}[]{#_Toc338865542}[]{#_Toc338865543}[]{#_Toc338865544}[]{#_Toc338865545}[]{#_Toc338865546}[]{#_Toc338865547}[]{#_Toc338865548}[]{#_Toc338865549}[]{#_Toc338865550}[]{#_Toc338865551}[]{#_Toc338865552}[]{#_Toc338865553}[]{#_Toc338865554}[]{#_Toc338865555}[]{#_Toc338865556}[]{#_Toc338865557}[]{#_Toc338865558}[]{#_Toc338865559}[]{#_Toc338865560}[]{#_Toc338865561}[]{#_Toc338865562}[]{#_Toc338865563}[]{#_Toc338865564}[]{#_Toc338865565}[]{#_Toc338865566}[]{#_Toc338865567}[]{#_Toc338865568}

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging bgp update-group l2vpn**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15149_x1311_2110403822}

[**[debugging bgp update-group l2vpn]{lang="EN-US"}**]{#struct_0_15149_x1311_x577463463}

[**[undo debugging bgp update-group l2vpn]{lang="EN-US"}**]{#struct_0_15149_x1311_x1313966305}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_15149_x1311_5457855}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1992921027}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15149_x1311_2034827242}

[[network-admin]{lang="EN-US"}]{#struct_0_15149_x1311_2034761706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15149_x1311_990745568}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1244289197}

[[无]{style="font-family:宋体"}]{#struct_0_15149_x1311_1570290915}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15149_x1311_203699529}

[**[debugging bgp update-group l2vpn]{lang="EN-US"}**]{#struct_0_15149_x1311_884064321}[命令用来打开]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族的打包组调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp update-group l2vpn]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族的打包组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_563603587}[地址族的打包组调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging bgp update-group l2vpn]{lang="EN-US"}]{#struct_0_15149_x1311_x1434206962}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1317635888}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1993379778}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_1478058463}

[[Send UPDATE to update-group *group-id* for following destinations]{lang="EN-US"}]{#struct_0_15149_x1311_x86601675}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_15149_x1311_x1704207363}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息更新]{style="font-family:宋体"}

[[Send UPDATE(Withdraw) to update-group *group-id* for following destinations]{lang="EN-US"}]{#struct_0_15149_x1311_2085040418}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_15149_x1311_x210081038}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息撤销]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_15149_x1311_x2129896161}

[[Origin]{lang="EN-US"}]{#struct_0_15149_x1311_x1993445314}[属性]{style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_15149_x1311_x1828551568}

[[AS Path]{lang="EN-US"}]{#struct_0_15149_x1311_2052141145}[属性]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_15149_x1311_62432144}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_15149_x1311_x2025955130}

[[Local Pref]{lang="EN-US"}]{#struct_0_15149_x1311_x1835799268}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1993248706}

[[MED]{lang="EN-US"}]{#struct_0_15149_x1311_x424043714}

[[MED]{lang="EN-US"}]{#struct_0_15149_x1311_1748917828}[（]{style="font-family:宋体"}[Multi-Exit Discriminator]{lang="EN-US"}[，多出口区分）值]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_15149_x1311_417332137}

[[扩展团体属性，包括：]{style="font-family:宋体"}]{#struct_0_15149_x1311_x400184509}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_15149_x1311_x1993314242}[：]{lang="EN-US" style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2VPN info]{lang="EN-US"}]{#struct_0_15149_x1311_457433074}[：]{lang="EN-US" style="font-family:宋体"}[L2VPN]{lang="EN-US"}[相关信息，包括]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[值、封装类型（]{lang="EN-US" style="font-family:宋体"}[Encap type]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS ID]{lang="EN-US"}]{#struct_0_15149_x1311_x1623121952}[：用来标识该]{style="font-family:宋体"}[PE]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例]{style="font-family:宋体"}

 

[[AFI/SAFI]{lang="DA"}]{#struct_0_15149_x1311_x1574124663}

[[地址族]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15149_x1311_1064082912}[子地址族]{style="font-family:宋体"}

[[RD]{lang="DA"}]{#struct_0_15149_x1311_1097809153}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1993117634}

[[Site ID]{lang="EN-US"}]{#struct_0_15149_x1311_1125590100}

[[VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x2080296131}[内站点的编号]{style="font-family:宋体"}

[[Label offset]{lang="DA"}]{#struct_0_15149_x1311_x490897188}

[[标签块的偏移量]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1993183170}

[[Label base]{lang="DA"}]{#struct_0_15149_x1311_x1836063330}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1542705808}

[[Label range]{lang="DA"}]{#struct_0_15149_x1311_1998724888}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_15149_x1311_269691568}

[[CSV]{lang="DA"}]{#struct_0_15149_x1311_x1992986562}

[[接入链路状态]{style="font-family:宋体"}]{#struct_0_15149_x1311_1680538657}

[[PE address]{lang="EN-US"}]{#struct_0_15149_x1311_80073201}

[[PE]{lang="EN-US"}]{#struct_0_15149_x1311_x1699343113}[的地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15149_x1311_540970294}

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x1993052098}[打开]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族的打包组调试信息开关，发布]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[标签块信息时，设备上将打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update-group l2vpn]{lang="EN-US"}]{#struct_0_15149_x1311_1154230302}

[\*Sep 24 06:44:31:370 2012 Sysname BGP/7/DEBUG: -MDC=1;                              ]{lang="EN-US"}

[         BGP_L2VPN.: Send UPDATE to update-group 0 for following destinations:  ]{lang="EN-US"}

[         Origin       : IGP                                                     ]{lang="EN-US"}

[         AS path      : 200                                                 ]{lang="EN-US"}

[         Next hop     : 1.1.1.3                                                 ]{lang="EN-US"}

[         Ext-Community: \<RT: 3:2\>, \<L2VPN info: MTU 1500, Encap type BGP VPLS\>  ]{lang="EN-US"}

[         AFI/SAFI     : 25/65 (L2VPN)                                     ]{lang="EN-US"}

[         RD           : 9:8                                                     ]{lang="EN-US"}

[         Site ID      : 9                                                       ]{lang="EN-US"}

[         Label offset : 0                                                       ]{lang="EN-US"}

[         Label base   : 775000                                                  ]{lang="EN-US"}

[         Label range  : 10   ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1821170349}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组]{style="font-family:宋体"}[0]{lang="EN-US"}[发送]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息更新，标签块信息]{style="font-family:宋体"}[产生于本]{style="font-family:宋体"}[AS]{lang="EN-US"}[内]{style="font-family:宋体"}[，]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径为]{style="font-family:宋体"}[200]{lang="EN-US"}[，下一跳为]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[，]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性为]{style="font-family:宋体"}[3:2]{lang="EN-US"}[，]{style="font-family:宋体"}[MTU]{lang="EN-US"}[为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节，封装类型为]{style="font-family:宋体"}[BGP VPLS]{lang="EN-US"}[，地址族为]{style="font-family:宋体"}[25]{lang="EN-US"}[，子地址族为]{style="font-family:宋体"}[65]{lang="EN-US"}[，路由标识符为]{style="font-family:宋体"}[9:8]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内站点编号为]{style="font-family:宋体"}[9]{lang="EN-US"}[，标签块偏移量为]{style="font-family:宋体"}[0]{lang="EN-US"}[，标签块的初始标签值为]{style="font-family:宋体"}[775000]{lang="EN-US"}[，标签块大小为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_911315963}[打开]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族的打包组调试信息开关，发布]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[邻居自动发现信息时，设备上将打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update-group l2vpn]{lang="EN-US"}]{#struct_0_15149_x1311_x1992855490}

[\*Sep 25 22:29:54:489 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[BGP_L2VPN.: Send UPDATE to update-group 0 for following destinations:  ]{lang="EN-US"}

[         Origin       : IGP                                                     ]{lang="EN-US"}

[         AS path      : 200                                                        ]{lang="EN-US"}

[         Next hop     : 0.0.0.0                                                 ]{lang="EN-US"}

[         Local pref   : 100                                                     ]{lang="EN-US"}

[         Ext-Community: \<RT: 3:2\>, \<VPLS ID: 5:67\>                              ]{lang="EN-US"}

[         AFI/SAFI     : 25/65(l2VPN)                                     ]{lang="EN-US"}

[         RD           : 5:1                                                     ]{lang="EN-US"}

[         PE address   : 1.2.3.4  ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_1718977281}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组]{style="font-family:宋体"}[0]{lang="EN-US"}[发送]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息更新，邻居自动发现信息]{style="font-family:宋体"}[产生于本]{style="font-family:宋体"}[AS]{lang="EN-US"}[内]{style="font-family:宋体"}[，]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径为]{style="font-family:宋体"}[200]{lang="EN-US"}[，下一跳地址为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，扩展团体属性]{style="font-family:宋体"}[RT]{lang="EN-US"}[为]{style="font-family:宋体"}[3:2]{lang="EN-US"}[，]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[为]{style="font-family:宋体"}[5:67]{lang="EN-US"}[，地址族为]{style="font-family:宋体"}[25]{lang="EN-US"}[，子地址族为]{style="font-family:宋体"}[65]{lang="EN-US"}[，路由标识符为]{style="font-family:宋体"}[5:1]{lang="EN-US"}[，]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[1.2.3.4]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#1398271569 .myid}
[]{#_Toc404791333}[]{#struct_0_15149_x1311_x443778912}

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging l2vpn management**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15149_x1311_441562698}

[**[debugging l2vpn management]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **hsb** \| **process** }]{lang="EN-US"}]{#struct_0_15149_x1311_x920069610}

[**[undo debugging l2vpn management]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **hsb** \| **process** }]{lang="EN-US"}]{#struct_0_15149_x1311_x1992921026}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15149_x1311_699411464}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1747055305}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15149_x1311_2034565099}

[[network-admin]{lang="EN-US"}]{#struct_0_15149_x1311_2034499563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15149_x1311_1723283801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1314456798}

[**[all]{lang="EN-US"}**]{#struct_0_15149_x1311_x1047635558}[：表示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_15149_x1311_x1508548016}[：表示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_15149_x1311_673769872}[：表示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[hsb]{lang="EN-US"}**]{#struct_0_15149_x1311_x1993379781}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[备份调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_15149_x1311_x895184356}[：表示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[创建]{style="font-family:宋体"}[PW]{lang="EN-US"}[过程调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15149_x1311_1219491851}

[**[debugging l2vpn management]{lang="EN-US"}**]{#struct_0_15149_x1311_1582403585}[命令用来打开]{style="font-family:
宋体"}[L2VPN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging l2vpn management]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[L2VPN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_626197082}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging l2vpn management error]{lang="EN-US"}]{#struct_0_15149_x1311_2009151212}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1323302801}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1993445317}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x262467627}

[[Failed to save vsi (*vsi-index*) to DBM.]{lang="EN-US"}]{#struct_0_15149_x1311_267800963}

[[保存]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_944443151}[到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败，此]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Failed to save peer to DBM.]{lang="EN-US"}]{#struct_0_15149_x1311_671929748}

[[保存]{style="font-family:宋体"}[peer]{lang="EN-US"}]{#struct_0_15149_x1311_x12821504}[到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to save the configuration of binding a VSI with an interface. Interface index: *if-index.*]{lang="EN-US"}]{#struct_0_15149_x1311_761832161}

[[保存接口绑定配置到]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_15149_x1311_x1993248709}[失败，接口索引为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*

[[Failed to free link ID (*link-id*) because it has been requested by another protocol. VSI index: *vsi-index*, new protocol: *new-protocol*, old protocol: *old-protocol*.]{lang="EN-US"}]{#struct_0_15149_x1311_1498270587}

[[释放链路的标识]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*]{#struct_0_15149_x1311_1710184679}[失败，因为此]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[已经被其他协议申请，对应的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，申请该]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[的新协议为]{style="font-family:宋体"}*[new-protocol]{lang="EN-US"}*[，旧协议为]{style="font-family:宋体"}*[old-protocol]{lang="EN-US"}*

[[Encapsulation mode not supported.]{lang="EN-US"}]{#struct_0_15149_x1311_1315952502}

[[不支持的链路封装类型]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1009050936}

[[Invalid VSI index (*vsi-index*).]{lang="EN-US"}]{#struct_0_15149_x1311_x1369188642}

[[非法的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_x1993314245}[索引]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Failed to send response message (*message type*).]{lang="EN-US"}]{#struct_0_15149_x1311_x1464881227}

[[向应用回应消息失败，消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_15149_x1311_x69367707}

[[Failed to send VSI notification.]{lang="EN-US"}]{#struct_0_15149_x1311_x1912759548}

[[向应用通告]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_x680712232}[信息失败]{style="font-family:宋体"}

[[Failed to start license reconnect timer for *feature-name.*]{lang="EN-US"}]{#struct_0_15149_x1311_419985310}

[[启动特性]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*]{#struct_0_15149_x1311_x955915151}[的]{style="font-family:宋体"}[license]{lang="EN-US"}[重连定时器失败]{style="font-family:宋体"}

[[The *feature-name* feature failed to receive messages from license daemon.]{lang="EN-US"}]{#struct_0_15149_x1311_x1297110044}

[[特性]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*]{#struct_0_15149_x1311_x1269846381}[接收来自]{style="font-family:宋体"}[License]{lang="EN-US"}[进程的消息失败]{style="font-family:宋体"}

[[The *feature-name* feature failed to get license data from license daemon.]{lang="EN-US"}]{#struct_0_15149_x1311_539981559}

[[特性]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*]{#struct_0_15149_x1311_1986069251}[向]{style="font-family:宋体"}[License]{lang="EN-US"}[进程获取]{style="font-family:宋体"}[License]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging l2vpn management event]{lang="EN-US"}]{#struct_0_15149_x1311_x1993117637}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1295313259}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x440493841}

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1378116425}

[[Received protocol (*protocol*) GR event (*event-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_x1497263925}

[[收到协议]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_15149_x1311_1879370266}[事件，协议号为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[，事件类型为]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Received interface event (*event-type*). Interface index: *if-index*.]{lang="EN-US"}]{#struct_0_15149_x1311_x1325124312}

[[收到接口事件，事件类型为]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_15149_x1311_x1993183173}[，接口索引为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*

[[Received VSI (*vsi-index*) deleted notification from L2VFIB.]{lang="EN-US"}]{#struct_0_15149_x1311_x269979389}

[[从]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_1059778932}[收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}[已删除的通告，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Received L2VPN-disabled notification from L2VFIB.]{lang="EN-US"}]{#struct_0_15149_x1311_1911081355}

[[从]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_1455591565}[收到]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[已去使能的通告]{style="font-family:宋体"}

[[Received L2VPN-disabled notification from application. Socket: *socket- id*.]{lang="EN-US"}]{#struct_0_15149_x1311_1201057741}

[[从应用收到]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_1255899583}[已去使能的通告，应用对应的套接字]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket- id]{lang="EN-US"}*

[[Received VSI (*vsi-index*) deleted notification from application. Socket: *socket- id*.]{lang="EN-US"}]{#struct_0_15149_x1311_x1992986565}

[[从应用收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_x1048344698}[已删除的通告，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，应用对应的套接字]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket- id]{lang="EN-US"}*

[[Received batch request for VSIs.]{lang="EN-US"}]{#struct_0_15149_x1311_x1346430423}

[[收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_600725888}[批量请求事件]{style="font-family:宋体"}

[[Received batch request for peers.]{lang="EN-US"}]{#struct_0_15149_x1311_x1377129725}

[[收到]{style="font-family:宋体"}[peer]{lang="EN-US"}]{#struct_0_15149_x1311_x1993052101}[批量请求事件]{style="font-family:宋体"}

[[Notified VSI event (*event-type*) successfully. VSI index: *vsi-index*]{lang="EN-US"}]{#struct_0_15149_x1311_x1930424660}

[[通告]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_x1843194630}[事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[成功，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Notified peer event (*event-type*) successfully.]{lang="EN-US"}]{#struct_0_15149_x1311_373800515}

[[通告]{style="font-family:宋体"}[peer]{lang="EN-US"}]{#struct_0_15149_x1311_x1479359090}[事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[[Notified AC state successfully. VSI index: *vsi-index*]{lang="EN-US"}]{#struct_0_15149_x1311_x1992855493}

[[通告]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_15149_x1311_152893340}[状态成功，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Notified PW class event (*event-type*) successfully. PW class name: *pw-class-name*]{lang="EN-US"}]{#struct_0_15149_x1311_x1090547575}

[[通告]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x1857741977}[模板事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[成功，]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名字为]{style="font-family:宋体"}*[pw-class-name]{lang="EN-US"}*

[[Notified L2VPN-disabled event successfully.]{lang="EN-US"}]{#struct_0_15149_x1311_x956400545}

[[通告]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x1992921029}[去使能事件成功]{style="font-family:宋体"}

[[Notified batch response event (*event-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_x60103423}

[[通告批量回应事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_15149_x1311_x1773354260}

[[Sent GR start to L2VFIB.]{lang="EN-US"}]{#struct_0_15149_x1311_x1668418851}

[[向]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_1950022140}[发送]{style="font-family:宋体"}[GR]{lang="EN-US"}[开始事件]{style="font-family:宋体"}

[[Sent GR end to L2VFIB.]{lang="EN-US"}]{#struct_0_15149_x1311_x1993379780}

[[向]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_1833698999}[发送]{style="font-family:宋体"}[GR]{lang="EN-US"}[结束事件]{style="font-family:宋体"}

[[Responded HA with an event (*event-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_x1465140808}

[[向]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15149_x1311_x1745701521}[回应一个事件]{style="font-family:宋体"}*[event type]{lang="EN-US"}*

[[Received an HA event (*event-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_x1993445316}

[[收到一个]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15149_x1311_1303616314}[事件]{style="font-family:宋体"}*[event type]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging l2vpn management hsb]{lang="EN-US"}]{#struct_0_15149_x1311_x1410986787}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1296606219}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1877476329}

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1993248708}

[[Sent an HA message (*message-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_x1230612768}

[[发送]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15149_x1311_1857762885}[消息，消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*

[[Received an HA message (*message-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_x1662960782}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15149_x1311_x1145159821}[消息，消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging l2vpn management process]{lang="EN-US"}]{#struct_0_15149_x1311_x1993314244}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1297462995}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_1264002128}

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1793639164}

[[Downloaded VSI binding to L2VFIB. Configuration type: *type*, VSI index: *vsi-index*, Interface index: *if-index*, service instance ID: *srv-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x1915542019}

[[向]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_x1993117636}[下发]{style="font-family:宋体"}[VSI]{lang="EN-US"}[绑定，配置类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，接口索引为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*[，服务实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[srv-id]{lang="EN-US"}*

[[Downloaded VSI to L2VFIB. Configuration type: *type*, VSI name: *vsi-name*]{lang="EN-US"}]{#struct_0_15149_x1311_x2006577782}

[[向]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_x360462659}[下发]{style="font-family:宋体"}[VSI]{lang="EN-US"}[信息，配置类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名字为]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*

[[Downloaded AC to L2VFIB. Operation type: *oper-type*, VSI index: *vsi-index*, link ID: *link-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x1725298051}

[[向]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_233192835}[下发]{style="font-family:宋体"}[AC]{lang="EN-US"}[表项，操作类型为]{style="font-family:宋体"}*[oper-type]{lang="EN-US"}*[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，链路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*

[[Downloaded PW to L2VFIB. Operation type: *oper-type*, VSI index: *vsi-index*, link ID: *link-id*, result: *result*]{lang="EN-US"}]{#struct_0_15149_x1311_x699880412}

[[向]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_x1993183172}[下发]{style="font-family:宋体"}[PW]{lang="EN-US"}[表项，操作类型为]{style="font-family:宋体"}*[oper-type]{lang="EN-US"}*[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，链路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[，处理结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Received MPLS PW addition notification. Protocol: *protocol*, VSI index: *vsi-index*, link ID: *link-id*, state: *state*]{lang="EN-US"}]{#struct_0_15149_x1311_1296104552}

[[收到添加]{style="font-family:宋体"}[MPLS PW]{lang="EN-US"}]{#struct_0_15149_x1311_812460799}[消息，信令协议号为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，链路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[[Received MPLS PW update notification. Protocol: *protocol*, VSI index: *vsi-index*, link ID: *link-id*, state: *state*]{lang="EN-US"}]{#struct_0_15149_x1311_1870256277}

[[收到更新]{style="font-family:宋体"}[MPLS PW]{lang="EN-US"}]{#struct_0_15149_x1311_x783748884}[消息，信令协议号为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，链路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[[Received PW deletion notification. VSI index: *vsi-index*, link ID: *link-id*, backup flag: *flag*]{lang="EN-US"}]{#struct_0_15149_x1311_x1992986564}

[[收到删除一条]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_517739243}[的通知，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，链路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[，备份标记为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[Processed PW switchover. Peer: *lsr-id*, PW ID: *pw-id*.]{lang="EN-US"}]{#struct_0_15149_x1311_1664617823}

[[处理]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x894204988}[切换，要切换的]{style="font-family:宋体"}[PW]{lang="EN-US"}[对端的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsr-id]{lang="EN-US"}[，]{style="font-family:宋体"}*[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*

[[Updated PW\'s VN info. Result: *result*, old VN ID: *old-vnid*, old FRR VN ID: *old-frr-vnid*, new VN ID: *new-vnid*, new FRR VN ID: *new-frr-vnid*]{lang="EN-US"}]{#struct_0_15149_x1311_x1110771737}

[[更新]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x1993052100}[的]{style="font-family:宋体"}[VN]{lang="EN-US"}[信息，处理结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*[，旧的]{style="font-family:宋体"}[VN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[old-vnid]{lang="EN-US"}*[，旧的]{style="font-family:宋体"}[FRR VN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[old-frr-vnid]{lang="EN-US"}*[，新的]{style="font-family:宋体"}[VN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[new-vnid]{lang="EN-US"}*[，新的]{style="font-family:宋体"}[FRR VN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[new-frr-vnid]{lang="EN-US"}*

[[Sent VN smooth start to FIB.]{lang="EN-US"}]{#struct_0_15149_x1311_798458695}

[[向]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_15149_x1311_527582852}[发送]{style="font-family:宋体"}[VN]{lang="EN-US"}[平滑开始]{style="font-family:宋体"}

[[Sent VN smooth end to FIB.]{lang="EN-US"}]{#struct_0_15149_x1311_x840663611}

[[向]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_15149_x1311_x206529292}[发送]{style="font-family:宋体"}[VN]{lang="EN-US"}[平滑结束]{style="font-family:宋体"}

[[Sent VN to FIB. VN ID: *vnid*, event: *event*-*type*, peer: *peer-lsrid*, nexthop number: *number*]{lang="EN-US"}]{#struct_0_15149_x1311_x1992855492}

[[向]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_15149_x1311_x1413190601}[下发]{style="font-family:宋体"}[VN]{lang="EN-US"}[，]{style="font-family:宋体"}[VN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vnid]{lang="EN-US"}*[，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[-*type*]{lang="EN-US"}[，对端]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[peer-lsrid]{lang="EN-US"}*[，等价下一跳个数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Sent dual VNs to FIB. VN ID: *vnid*, event: *event*-*type*, peer: *peer-lsrid*, NID: *nid*, backup peer: *backup-peer-lsrid*, backup NID: *backup-nid*]{lang="EN-US"}]{#struct_0_15149_x1311_1144851314}

[[向]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_15149_x1311_x409356440}[下发主备类型的]{style="font-family:宋体"}[VN]{lang="EN-US"}[，]{style="font-family:宋体"}[VN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vnid]{lang="EN-US"}*[，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[-*type*]{lang="EN-US"}[，主隧道的对端]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[peer-lsrid]{lang="EN-US"}*[，主隧道的]{style="font-family:宋体"}[NID]{lang="EN-US"}[为]{style="font-family:宋体"}*[nid]{lang="EN-US"}*[，备份隧道的对端]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[backup-peer-lsrid]{lang="EN-US"}*[ ]{lang="EN-US"}[，备隧道]{style="font-family:宋体"}[NID]{lang="EN-US"}[为]{style="font-family:宋体"}*[backup-nid]{lang="EN-US"}*

[[Notified the application to send MAC withdraw message. Peer: *lsr-id*, PW ID: *pw-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x1992921028}

[[通知应用发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_15149_x1311_1505980518}[地址回收消息，需要发送消息的对端为]{style="font-family:宋体"}*[lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*

[[VN switchover paused.]{lang="EN-US"}]{#struct_0_15149_x1311_x1319230783}

[[VN]{lang="EN-US"}]{#struct_0_15149_x1311_222124442}[切换处理暂停]{style="font-family:宋体"}

[[VN switchover completed.]{lang="EN-US"}]{#struct_0_15149_x1311_x427295836}

[[VN]{lang="EN-US"}]{#struct_0_15149_x1311_x1907186974}[切换处理完成]{style="font-family:宋体"}

[[Sent VSI deletion event to L2VFIB. VSI index: *vsi-index*.]{lang="EN-US"}]{#struct_0_15149_x1311_1965822910}

[[向]{style="font-family:宋体"}[L2VFIB]{lang="EN-US"}]{#struct_0_15149_x1311_1806908409}[发送]{style="font-family:宋体"}[VSI]{lang="EN-US"}[删除事件，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Processed GR event (*type*) for protocol (*protocol*). VSI index: *vsi-index*]{lang="EN-US"}]{#struct_0_15149_x1311_x427361372}

[[处理协议]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_15149_x1311_486438297}[事件，事件类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，协议号为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Received PW statistics disabling event. Total number is *number.*]{lang="EN-US"}]{#struct_0_15149_x1311_2128745245}

[[收到关闭]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_375966067}[统计功能事件，当前使能了统计功能的]{style="font-family:宋体"}[PW]{lang="EN-US"}[总数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Received PW statistics enabling event. Total number is *number.*]{lang="EN-US"}]{#struct_0_15149_x1311_2128155422}

[[收到关闭]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x12400341}[统计功能事件，当前使能了统计功能的]{style="font-family:宋体"}[PW]{lang="EN-US"}[总数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Timer (15 minutes) for PW MIB statistics timed out.]{lang="EN-US"}]{#struct_0_15149_x1311_x143761852}

[[PW MIB]{lang="EN-US"}]{#struct_0_15149_x1311_927237641}[统计定时器超时，定时器时长为十五分钟]{style="font-family:宋体"}

[[Started license reconnect timer for *feature-name*.]{lang="EN-US"}]{#struct_0_15149_x1311_x1905679054}

[[启动特性]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*]{#struct_0_15149_x1311_x2018560890}[的]{style="font-family:宋体"}[License ]{lang="EN-US"}[重连定时器]{style="font-family:宋体"}

[[Stopped license reconnect timer for *feature-name*.]{lang="EN-US"}]{#struct_0_15149_x1311_x339595113}

[[停止特性]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*]{#struct_0_15149_x1311_x810837138}[的]{style="font-family:宋体"}[License ]{lang="EN-US"}[重连定时器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15149_x1311_1631135705}

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_1649069556}[打开]{style="font-family:宋体"}[L2VPN]{lang="PT-BR"}[的错误调试信息开关。关闭]{style="font-family:宋体"}[LSM]{lang="EN-US"}[进程时，设备上会打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2vpn management error]{lang="EN-US"}]{#struct_0_15149_x1311_x427164764}

[\<Sysname\> process shutdown name lsmd]{lang="EN-US"}

[\*Aug 27 13:02:23:947 2011 Sysname L2VPN/7/ERROR: -MDC=1; Failed to connect to LSM.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1037619613}*[和]{style="font-family:宋体"}[LSM]{lang="EN-US"}[进程连接失败]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_1148803284}[打开]{style="font-family:宋体"}[L2VPN]{lang="PT-BR"}[的事件调试信息开关。创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，配置信令协议为]{style="font-family:宋体"}[LDP]{lang="EN-US"}[，并在]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令视图下配置一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[，设备上会打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2vpn management event]{lang="EN-US"}]{#struct_0_15149_x1311_1265552955}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\]]{lang="EN-US"}

[\*Sep  5 08:56:16:960 2011 Sysname L2VPN/7/EVENT: -MDC=1; Notified VSI event (0) successfully. VSI index: 0xa.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_1363295324}*[向应用通告]{style="font-family:宋体"}[VSI]{lang="EN-US"}[创建事件成功，事件类型为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0xa]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\[Sysname-vsi-vpn1\] pwsignaling ldp]{lang="EN-US"}]{#struct_0_15149_x1311_x427230300}

[\[Sysname-vsi-vpn1-ldp\]]{lang="EN-US"}

[\*Sep  5 08:56:41:652 2011 Sysname L2VPN/7/EVENT: -MDC=1; Notified VSI event (3) successfully. VSI index: 0xa.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_2041708726}*[向应用通告信令视图创建事件成功，事件类型为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0xa]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\[Sysname-vsi-vpn1-ldp\] peer 1.1.1.1 pw-id 1234]{lang="EN-US"}]{#struct_0_15149_x1311_1604246544}

[\[Sysname-vsi-vpn1-ldp-1.1.1.1-1234\]]{lang="EN-US"}

[\*Sep  5 08:57:07:365 2011 Sysname L2VPN/7/EVENT: -MDC=2; Notified peer event (8) successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x458027675}*[向应用通告]{style="font-family:宋体"}[peer]{lang="EN-US"}[创建事件成功，事件类型为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_x1764179611}[在三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上绑定]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[，打印如下调试信息。]{style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_15149_x1311_1072854995}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[\*Sep  5 08:58:32:680 2011 Sysname L2VPN/7/EVENT: -MDC=1; Notified AC state successfully. VSI index: 0xa.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x991099278}*[向应用通告]{style="font-family:宋体"}[AC]{lang="EN-US"}[状态成功，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0xa]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_1698433995}[打开]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[创建]{style="font-family:宋体"}[PW]{lang="EN-US"}[过程调试信息开关。在设备上创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2vpn management process]{lang="EN-US"}]{#struct_0_15149_x1311_x427033692}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\]]{lang="EN-US"}

[\*Sep  5 09:02:17:781 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Downloaded VSI to L2VFIB. Configuration type: 4, VSI name: vpn1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1082696132}*[创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，向内核下发]{style="font-family:宋体"}[VSI]{lang="EN-US"}[配置。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_x162913459}[设备两端创建]{style="font-family:宋体"}[PW ID]{lang="PT-BR"}[相同的]{style="font-family:宋体"}[PW]{lang="PT-BR"}[，然后再绑定此]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[，打印如下信息。]{style="font-family:宋体"}

[[\[]{lang="DA"}[Sysname]{lang="EN-US"}]{#struct_0_15149_x1311_1785626487}[\] vsi vpn1]{lang="DA"}

[\[]{lang="DA"}[Sysname]{lang="EN-US"}[-vsi-vpn1\] pwsignaling ldp]{lang="DA"}

[\[]{lang="DA"}[Sysname]{lang="EN-US"}[-vsi-vpn1-ldp\] peer 1.1.1.1 pw-id 222]{lang="DA"}

[\*Sep  5 09:08:27:343 2011 ]{lang="DA"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[L2VPN/7/PROCESS: -MDC=1; Received MPLS PW addition notification. Protocol: 3, VSI index: 0xa, link ID: 8, state: 3.]{lang="DA"}

[ ]{lang="DA"}

[\*Sep  5 09:08:27:343 2011 ]{lang="DA"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[L2VPN/7/PROCESS: -MDC=1; Updated PW\'s VN info. Result: 0, old VN ID: 0x0, old FRR VN ID: 0x0, new VN ID: 0x60000000, new FRR VN ID:]{lang="DA"}

[ 0x0.]{lang="DA"}

[*[// peer]{lang="EN-US"}*]{#struct_0_15149_x1311_318726253}*[创建时生成]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并关联]{style="font-family:宋体"}[VN]{lang="EN-US"}*

[ ]{lang="DA"}

[[\[]{lang="DA"}[Sysname]{lang="EN-US"}]{#struct_0_15149_x1311_x427099228}[-GigabitEthernet1/0/4\] xconnect vsi vpn1]{lang="DA"}

[\*Sep  5 09:09:24:648 2011 ]{lang="DA"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[L2VPN/7/PROCESS: -MDC=1; Downloaded xconnect to L2VFIB. Configuration type: 7, VSI index: 0xa, Interface index: 341, service instance ID: 0.]{lang="DA"}

[ ]{lang="DA"}

[\*Sep  5 09:09:24:650 2011 ]{lang="DA"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[L2VPN/7/PROCESS: -MDC=1; Downloaded AC to L2VFIB. Operation type: 3, VSI index: 0xa, link ID: 0.]{lang="DA"}

[ ]{lang="DA"}

[\*Sep  5 09:09:24:650 2011 ]{lang="DA"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[L2VPN/7/PROCESS: -MDC=1; Received MPLS PW update notification. Protocol: 3, VSI index: 0xa, link ID: 8, state: 3.]{lang="DA"}

[ ]{lang="DA"}

[\*Sep  5 09:10:32:568 2011 ]{lang="DA"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[L2VPN/7/PROCESS: -MDC=1; Downloaded PW to L2VFIB. Operation type: 1, VSI index: 0xa, link ID: 8, result: 0.]{lang="DA"}

[*[// ]{lang="DA"}*]{#struct_0_15149_x1311_x1136911895}*[绑定]{style="font-family:宋体"}[VSI]{lang="DA"}[后]{style="font-family:宋体"}[AC]{lang="DA"}[状态变为]{style="font-family:宋体"}[up]{lang="DA"}[，]{style="font-family:宋体"}[L2VPN]{lang="DA"}[收到]{style="font-family:宋体"}[PW]{lang="DA"}[更新]{style="font-family:宋体"}[，]{style="font-family:宋体"}[PW]{lang="DA"}[状态变为]{style="font-family:宋体"}[up]{lang="DA"}[，]{style="font-family:宋体"}[向内核下发绑定配置和]{style="font-family:宋体"}[AC]{lang="DA"}[表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并向内核下发]{style="font-family:宋体"}[up]{lang="DA"}[的]{style="font-family:宋体"}[PW]{lang="DA"}[。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_x1903460554}[创建备份]{style="font-family:宋体"}[LDP PW]{lang="DA"}[。]{style="font-family:宋体"}

[[\[Sysname-vsi-hvpls-ldp-1.1.1.1-222\] backup-peer 4.4.4.9 pw-id 444]{lang="DA"}]{#struct_0_15149_x1311_x1320651652}

[\*Sep  5 09:11:46:960 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Received MPLS PW addition notification. ]{lang="DA"}[Protocol: 3, VSI index: 0x3, link ID: 8, state: 3.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 09:11:46:961 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Sent dual VNs to FIB. VN ID: 0x860000002, event: 0, peer: 1.1.1.1, NID: 0x408, backup peer: 4.4.4.9, backup NID: 0xffffffff.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 09:11:46:961 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Sent dual VNs to FIB. VN ID: 0x960000003, event: 0, peer: 4.4.4.9, NID: 0xffffffff, backup peer: 1.1.1.1, backup NID: 0x408.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 09:11:46:962 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Updated PW\'s VN info. Result: 0, old VN ID: 0x60000000, old FRR VN ID: 0x0, new VN ID: 0x860000002, new FRR VN ID: 0x960000003.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep  5 09:11:46:962 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Downloaded PW to L2VFIB. Operation type: 1, VSI index: 0x3, link ID: 8, result: 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_1475070625}*[创建备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[收到]{style="font-family:宋体"}[PW]{lang="EN-US"}[更新，并更新]{style="font-family:宋体"}[PW]{lang="EN-US"}[关联的]{style="font-family:宋体"}[VN]{lang="EN-US"}[信息，将新的]{style="font-family:宋体"}[VN]{lang="EN-US"}[信息向内核下发。]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[向内核下发]{style="font-family:宋体"}[PW]{lang="EN-US"}[更新。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_x426902620}[打开]{style="font-family:宋体"}[L2VPN]{lang="PT-BR"}[的备份调试信息开关。创建]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[，并创建]{style="font-family:宋体"}[LDP PW]{lang="PT-BR"}[后，插入备板，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2vpn management hsb]{lang="EN-US"}]{#struct_0_15149_x1311_1999891185}

[\*Aug 27 12:43:43:143 2011 Sysname L2VPN/7/HSB: -MDC=1; Send an HA message, type(0).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_735830802}*[备板插入，进行批量备份。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_1595846656}[备板在位时，创建]{style="font-family:宋体"}[PW]{lang="PT-BR"}[，进行实时备份。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15149_x1311_x2134294305}

[\[Sysname\] vsi test]{lang="EN-US"}

[\[Sysname-vsi-test\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-test-ldp\] peer 23.2.2.2 pw-id 12345]{lang="EN-US"}

[\[Sysname-vsi-test-ldp-23.2.2.2-12345\]]{lang="EN-US"}

[\*Aug 27 12:45:26:332 2011 Sysname L2VPN/7/HSB: -MDC=1; Sent an HA message (1).]{lang="EN-US"}

[\*Aug 27 12:45:26:353 2011 Sysname L2VPN/7/HSB: -MDC=1; Sent an HA message (1).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x426968156}*[创建]{style="font-family:宋体"}[PW]{lang="EN-US"}[时会进行]{style="font-family:宋体"}[link ID]{lang="EN-US"}[申请和]{style="font-family:宋体"}[VN]{lang="EN-US"}[创建，对]{style="font-family:宋体"}[link ID]{lang="EN-US"}[和]{style="font-family:宋体"}[VN]{lang="EN-US"}[进行实时备份。]{style="font-family:宋体"}*

::: {#-754291817 .myid}
[]{#_Toc404791334}[]{#struct_0_15149_x1311_2034761704}[]{#_Toc339623831}

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging l2vpn packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15149_x1311_990614496}

[**[debugging l2vpn packet ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_15149_x1311_x621996991}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}*[ { ]{lang="IT"}**[connection ]{lang="EN-US"}***[connection-name ]{lang="EN-US"}*[\| **site** *site-id* **remote-site-id** *remote-site-id* } ]{lang="EN-US"}[\| **vsi** *vsi-name*]{lang="EN-US"}*[ ]{lang="EN-US" style="font-family:,\"serif\""}*[\]]{lang="EN-US"}

[**[undo debugging l2vpn packet ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_15149_x1311_2034958312}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}*[ { ]{lang="IT"}**[connection ]{lang="EN-US"}***[connection-name ]{lang="EN-US"}*[\| **site** *site-id* **remote-site-id** *remote-site-id* } ]{lang="EN-US"}[\| **vsi** *vsi-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x981226456}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15149_x1311_x814207623}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15149_x1311_605570708}

[[network-admin]{lang="EN-US"}]{#struct_0_15149_x1311_2034892776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15149_x1311_581103823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1517446918}

[**[xconnect-group ]{lang="IT"}**]{#struct_0_15149_x1311_x470988366}*[group-name]{lang="IT"}*[：表示指定交叉连接组的]{style="font-family:
宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:
宋体"}*[group-name]{lang="IT"}*[表示交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[connection ]{lang="EN-US"}***[connection-name]{lang="EN-US"}*]{#struct_0_15149_x1311_2034434025}[：表示指定交叉连接的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}*[connection-name]{lang="EN-US"}*[表示交叉连接的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[个字符的字符串，不能包含字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[**[site]{lang="EN-US"}**[ *site-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x1319881036}[：指定本地站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[remote-site-id]{lang="EN-US"}**[ *remote-site-id*]{lang="EN-US"}]{#struct_0_15149_x1311_1531145187}[：指定远端站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。同时指定]{style="font-family:宋体"}**[site-id]{lang="EN-US"}**[ *site-id*]{lang="EN-US"}[和]{style="font-family:宋体"}**[remote-site-id]{lang="EN-US"}**[ *remote-site-id*]{lang="EN-US"}[参数，则表示本端站点和指定远端站点之间交叉连接的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_15149_x1311_x488582494}[：表示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15149_x1311_2034368489}

[**[debugging l2vpn packet]{lang="EN-US"}**]{#struct_0_15149_x1311_2120133847}[命令用来打开]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo debugging l2vpn packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_1322812619}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果不指定任何参数，则表示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_357934549}[和交叉连接组的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging l2vpn packet]{lang="EN-US"}]{#struct_0_15149_x1311_x137946099}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1853148391}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_2034565097}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_239059373}

[[L2VPN input:]{lang="EN-US"}]{#struct_0_15149_x1311_2034499561}

[[收到]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_1723152729}[报文]{style="font-family:宋体"}

[[L2VPN output:]{lang="EN-US"}]{#struct_0_15149_x1311_x1220993800}

[[发送]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_2034696169}[报文]{style="font-family:宋体"}

[[L2VPN fsinput:]{lang="EN-US"}]{#struct_0_15149_x1311_x488648030}

[[收到]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x1517838255}[快转报文]{style="font-family:宋体"}

[[L2VPN fsoutput:]{lang="EN-US"}]{#struct_0_15149_x1311_x488451422}

[[发送]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_800700807}[快转报文]{style="font-family:宋体"}

[[Received a packet from interface *interface-name* Service Instance *Service-Instance-ID*]{lang="EN-US"}]{#struct_0_15149_x1311_x2126110808}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15149_x1311_2034630633}[收到数据包。如果是从二层以太网接口的服务实例（]{style="font-family:宋体"}[Service Instance]{lang="EN-US"}[）收到的报文，则]{style="font-family:宋体"}*[Service-Instance-ID]{lang="EN-US"}*[为接收报文的服务实例]{style="font-family:宋体"}[ID]{lang="EN-US"}*[。]{style="font-family:宋体"}*

[[Sent a packet to interface *interface-name*]{lang="EN-US"}]{#struct_0_15149_x1311_1387661531}

[[发送数据包到接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15149_x1311_x1421415480}

[[Sent a packet to chassis *chassis-number* slot ]{lang="EN-US"}]{#struct_0_15149_x1311_1883678656}*[slot-number]{lang="PT-BR"}*[ cpu *cpu-number*, PktLen = *length*, result *result*.]{lang="EN-US"}

[[发送数据包到成员设备]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*]{#struct_0_15149_x1311_1882826688}[单板]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[的编号为]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[CPU]{lang="PT-BR"}[，数据包长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，发送结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Received a packet from the PW ]{lang="EN-US"}]{#struct_0_15149_x1311_2034827241}

[[从]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_1028303301}[接收报文]{style="font-family:宋体"}

[[Connection-ID]{lang="EN-US"}]{#struct_0_15149_x1311_2034761705}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_990548960}[的]{style="font-family:宋体"}[Connection ID]{lang="EN-US"}

[[Link-ID]{lang="EN-US"}]{#struct_0_15149_x1311_2034958313}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x981160920}[的]{style="font-family:宋体"}[LINK ID]{lang="EN-US"}

[[Control-Word]{lang="EN-US"}]{#struct_0_15149_x1311_2034892777}

[[如果有控制字，则显示其内容]{style="font-family:宋体"}]{#struct_0_15149_x1311_581169359}

[[VC-Label]{lang="EN-US"}]{#struct_0_15149_x1311_x639461619}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_2034434022}[收发报文时，对应的]{style="font-family:宋体"}[VC]{lang="EN-US"}[标签]{style="font-family:宋体"}

[[PktLen]{lang="EN-US"}]{#struct_0_15149_x1311_x1320339788}

[[数据包的长度]{style="font-family:宋体"}]{#struct_0_15149_x1311_2034368486}

[[Label]{lang="EN-US"}]{#struct_0_15149_x1311_2119544023}

[[标签（包括私网内层标签和公网外层标签）]{style="font-family:宋体"}]{#struct_0_15149_x1311_2034565094}

[[EXP]{lang="EN-US"}]{#struct_0_15149_x1311_238993837}

[[MPLS]{lang="EN-US"}]{#struct_0_15149_x1311_2034499558}[报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_15149_x1311_1723611480}

[[MPLS]{lang="EN-US"}]{#struct_0_15149_x1311_2034696166}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Packet discarded because the PW isn't up.]{lang="EN-US"}]{#struct_0_15149_x1311_x2126831704}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_2034630630}[没有处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态，报文被丢弃。主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[中处于]{style="font-family:宋体"}[block]{lang="EN-US"}[状态]{style="font-family:宋体"}[(]{lang="EN-US"}[当前不被使用]{style="font-family:宋体"}[)]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[接收到的报文，无法被转发。]{style="font-family:宋体"}

[[Packet discarded because the AC isn't up.]{lang="EN-US"}]{#struct_0_15149_x1311_1387727067}

[[AC]{lang="EN-US"}]{#struct_0_15149_x1311_2034827238}[没有处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态，报文被丢弃。]{style="font-family:宋体"}

[[Packet discarded because the Tunnel isn't up.]{lang="EN-US"}]{#struct_0_15149_x1311_357934547}

[[Tunnel]{lang="EN-US"}]{#struct_0_15149_x1311_357934544}[没有处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded because the forwarding type isn\'t VPWS.]{lang="EN-US"}]{#struct_0_15149_x1311_1027844548}

[[报文不是]{style="font-family:宋体"}[VPWS]{lang="EN-US"}]{#struct_0_15149_x1311_2034761702}[转发，报文被丢弃。]{style="font-family:宋体"}

[[Packet discarded because interface *interface-name* Service Instance *Service-Instance-ID* isn't an AC.]{lang="EN-US"}]{#struct_0_15149_x1311_991007712}

[[根据接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15149_x1311_2034958310}[和服务实例（]{style="font-family:宋体"}[Service Instance]{lang="EN-US"}[）没有找到]{style="font-family:宋体"}[AC]{lang="EN-US"}[，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded because failed to find a PW with Connection-ID *connection-id* Link-ID *link-id*.]{lang="EN-US"}]{#struct_0_15149_x1311_x981357528}

[[根据]{style="font-family:宋体"}[Connection-ID]{lang="EN-US"}]{#struct_0_15149_x1311_2034892774}[和]{style="font-family:宋体"}[Link ID]{lang="EN-US"}[没有找到]{style="font-family:宋体"}[PW]{lang="EN-US"}[，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded because the packet should include the control word field.]{lang="EN-US"}]{#struct_0_15149_x1311_580972751}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_2034434023}[支持控制字，而报文不含控制字，丢弃报文]{style="font-family:宋体"}

[[Packet discarded because no corresponding AC or PW exists. ]{lang="EN-US"}]{#struct_0_15149_x1311_x1320274252}

[[找不到对应的表项，丢弃报文。]{style="font-family:宋体"}]{#struct_0_15149_x1311_2034368487}

[[Removed the control word field.]{lang="EN-US"}]{#struct_0_15149_x1311_2119478487}

[[砍掉控制字]{style="font-family:宋体"}]{#struct_0_15149_x1311_2034565095}

[[Removed the P-tag]{lang="EN-US"}]{#struct_0_15149_x1311_238928301}

[[砍掉]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}]{#struct_0_15149_x1311_2034499559}[字段，该]{style="font-family:宋体"}[Tag]{lang="EN-US"}[是一个服务提供商网络为了区分用户而要求用户压入的"服务定界符"]{style="font-family:宋体"}

[[Added the P-tag: priority *priority*, CFI *cfi-value*, VLAN ID *vlan-id.*]{lang="EN-US"}]{#struct_0_15149_x1311_1723677016}

[[添加]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}]{#struct_0_15149_x1311_2034696167}[字段，优先级为]{style="font-family:宋体"}*[priority]{lang="EN-US"}[，]{style="font-family:宋体"}*[CFI]{lang="EN-US"}[为]{style="font-family:宋体"}*[cfi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id ]{lang="EN-US"}*

[[Swapped the P-tag: priority *priority*, CFI *cfi-value*, VLAN ID *vlan-id.*]{lang="EN-US"}]{#struct_0_15149_x1311_x2126766168}

[[交换]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}]{#struct_0_15149_x1311_2034630631}[字段，交换后的优先级为]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[，]{style="font-family:宋体"}[CFI]{lang="EN-US"}[为]{style="font-family:宋体"}*[cfi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id ]{lang="EN-US"}*

[[Packet discarded because no forwarding information exists for the PW.]{lang="EN-US"}]{#struct_0_15149_x1311_1387792603}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_2034827239}[没有对应的转发信息，报文被丢弃]{style="font-family:宋体"}

[[Processed L2VPN service. *interface-name*, service phase: *phase*, service result: *result.*]{lang="EN-US"}]{#struct_0_15149_x1311_2034761703}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_990942176}[转发业务]{style="font-family:宋体"}

[*[phase]{lang="EN-US"}*]{#struct_0_15149_x1311_2034958311}[为业务处理阶段，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[input]{lang="EN-US"}]{#struct_0_15149_x1311_x981291992}[：入报文阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[o]{lang="EN-US"}[utput]{lang="EN-US"}]{#struct_0_15149_x1311_2034892775}[：出报文阶段]{style="font-family:
  宋体"}

[*[result]{lang="EN-US"}*]{#struct_0_15149_x1311_581038287}[为业务处理结果，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[continue]{lang="EN-US"}]{#struct_0_15149_x1311_x694449329}[：报文继续转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stop]{lang="EN-US"}]{#struct_0_15149_x1311_x1995633485}[：报文被业务截获，不用继续转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stop err]{lang="EN-US"}]{#struct_0_15149_x1311_x694514865}[：业务处理失败，不用继续转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[continue with new data]{lang="EN-US"}]{#struct_0_15149_x1311_x694318257}[：报文被业务修改，继续转发]{style="font-family:宋体"}

[[Sent a VCCV packet through the PW.]{lang="EN-US"}]{#struct_0_15149_x1311_x1615822586}

[[通过]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x694383793}[发送]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Packet discarded because the CC type of the PW isn't contrl word, or the CV type isn't Raw-BFD.]{lang="EN-US"}]{#struct_0_15149_x1311_x2069116919}

[[报文不是]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_15149_x1311_x694187185}[封装，但]{style="font-family:宋体"}[PW CC]{lang="EN-US"}[类型不是控制字方式或]{style="font-family:宋体"}[CV]{lang="EN-US"}[类型不是]{style="font-family:宋体"}[Raw-BFD]{lang="EN-US"}

[[Packet discarded because the PW doesn't support ping operation.]{lang="EN-US"}]{#struct_0_15149_x1311_x126248396}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x694252721}[不支持]{style="font-family:宋体"}[lsp ping]{lang="EN-US"}[，]{style="font-family:宋体"} [丢弃报文]{style="font-family:宋体"}

[[Packet discarded because the PW doesn't support BFD detection.]{lang="EN-US"}]{#struct_0_15149_x1311_x694056113}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x1661858185}[不支持]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测，丢弃报文]{style="font-family:宋体"}

[[Packet discarded because the UDP destination port is invalid.]{lang="EN-US"}]{#struct_0_15149_x1311_x694121649}

[[UDP]{lang="EN-US"}]{#struct_0_15149_x1311_1078309122}[封装的报文，目的端口无效，丢弃报文]{style="font-family:宋体"}

[[Packet discarded because adding the ACH failed.]{lang="EN-US"}]{#struct_0_15149_x1311_x693925041}

[[封装关联信道头失败，丢弃报文]{style="font-family:宋体"}]{#struct_0_15149_x1311_x757693354}

[[Received a VCCV packet. The CC type is *type*.]{lang="EN-US"}]{#struct_0_15149_x1311_x693990577}

[[收到]{style="font-family:宋体"}[VCCV]{lang="EN-US"}]{#struct_0_15149_x1311_x694449328}[报文，]{style="font-family:宋体"}[CC]{lang="EN-US"}[类型是]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[Packet discarded because CC type in the packet is different from the PW.]{lang="EN-US"}]{#struct_0_15149_x1311_x1995567949}

[[ ]{lang="EN-US"}]{#struct_0_15149_x1311_x694514864}[报文中]{style="font-family:宋体"}[CC]{lang="EN-US"}[类型与]{style="font-family:宋体"}[PW]{lang="EN-US"}[不一致（报文攻击时出现），丢弃报文]{style="font-family:宋体"}

[[Packet discarded because the packet contains ACH, but the PW doesn't support control word function.]{lang="EN-US"}]{#struct_0_15149_x1311_x694318256}

[[PW ]{lang="EN-US"}]{#struct_0_15149_x1311_x1615888122}[不支持控制字，但是报文携带关联信道头，丢弃报文]{style="font-family:宋体"}

[[A Raw-BFD VCCV packet discarded because the CV type of the PW isn't Raw-BFD.]{lang="EN-US"}]{#struct_0_15149_x1311_x694383792}

[[PW CV]{lang="EN-US"}]{#struct_0_15149_x1311_x2069051383}[类型不是]{style="font-family:宋体"}[Raw-BFD]{lang="EN-US"}[，而报文为]{style="font-family:宋体"}[Raw-BFD VCCV]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[Packet discarded because the IP field of the packet is invalid.]{lang="EN-US"}]{#struct_0_15149_x1311_x694187184}

[[IP ]{lang="EN-US"}]{#struct_0_15149_x1311_x694252720}[无效，丢弃报文]{style="font-family:宋体"}

[[KLSPV failed to process the echo request packet.]{lang="EN-US"}]{#struct_0_15149_x1311_689912906}

[[ KLSPV]{lang="EN-US"}]{#struct_0_15149_x1311_x694056112}[处理]{style="font-family:宋体"}[echo request]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Packet discarded because no suitable control channel for the PW.]{lang="EN-US"}]{#struct_0_15149_x1311_x694121648}

[[PW]{lang="EN-US"}]{#struct_0_15149_x1311_1078374658}[没有控制通道支持报文转发，丢弃报文]{style="font-family:宋体"}

[[A BFD UDP packet discarded because the CV type of PW isn\'t BFD.]{lang="EN-US"}]{#struct_0_15149_x1311_x693925040}

[[ PW CV]{lang="EN-US"}]{#struct_0_15149_x1311_x693990576}[类型不是]{style="font-family:宋体"}[BFD]{lang="EN-US"}[方式，而报文采用]{style="font-family:宋体"}[BFD UDP]{lang="EN-US"}[封装，丢弃报文]{style="font-family:宋体"}

[[L2L3: Received a packet from interface *interface-name*, PktLen=*packet-len*.]{lang="EN-US"}]{#struct_0_15149_x1311_x694449331}

[[从]{style="font-family:宋体"}[L2VE/L3VE]{lang="EN-US"}]{#struct_0_15149_x1311_x694514867}[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[收到报文，报文长度是]{style="font-family:宋体"}*[packet-len]{lang="EN-US"}*

[[L2L3: Sent a packet to interface *interface-name*, PktLen=*packet-len*.]{lang="EN-US"}]{#struct_0_15149_x1311_x694383795}

[[发送报文给]{style="font-family:宋体"}[L2VE/L3VE]{lang="EN-US"}]{#struct_0_15149_x1311_x694187187}[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，报文长度是]{style="font-family:宋体"}*[packet-len]{lang="EN-US"}*

[[Received a packet from interface *interface-name*, KeyType=*keytype*, KeyID=*keyid*, PktLen=*packet-len*.]{lang="EN-US"}]{#struct_0_15149_x1311_x339660649}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15149_x1311_1226423292}[收到数据包，该数据包为]{style="font-family:宋体"}*[keytype]{lang="EN-US"}*[报文，]{style="font-family:宋体"}[KeyID]{lang="EN-US"}[为]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[，]{style="font-family:宋体"}[数据包长度为]{style="font-family:宋体"}*[packet-len]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[*[Keytype]{lang="EN-US"}*]{#struct_0_15149_x1311_x183922380}[取值为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，表示数据包为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Sent a packet on interface *interface-name*, KeyType=*keytype*, KeyID=*keyid*, PktLen=*packet-len*.]{lang="EN-US"}]{#struct_0_15149_x1311_x1028695007}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15149_x1311_x1146229703}[发送数据包，该数据包为]{style="font-family:宋体"}*[keytype]{lang="EN-US"}*[报文，]{style="font-family:宋体"}[KeyID]{lang="EN-US"}[为]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[，]{style="font-family:宋体"}[数据包长度为]{style="font-family:宋体"}*[packet-len]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[*[Keytype]{lang="EN-US"}*]{#struct_0_15149_x1311_1014297932}[取值为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，表示数据包为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Packet discarded because the Tunnel doesn\'t exist.]{lang="EN-US"}]{#struct_0_15149_x1311_518093311}

[[找不到对应的隧道，报文被丢弃]{style="font-family:宋体"}]{#struct_0_15149_x1311_419854238}

[[Packet discarded because the Tunnel isn\'t up.]{lang="EN-US"}]{#struct_0_15149_x1311_991124111}

[[隧道没有处于]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_15149_x1311_1985938179}[状态，报文被丢弃]{style="font-family:宋体"}

[[Packet broadcast to VSI (*vsi-index*).]{lang="EN-US"}]{#struct_0_15149_x1311_925946230}

[[报文广播到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_x890021633}[中，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*

[[Packet delivered to the VSI gateway interface of VSI (*vsi-index*), Result=*result*.]{lang="EN-US"}]{#struct_0_15149_x1311_x742945176}

[[报文上送给]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_1253356510}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[网关接口，上送结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[*[result]{lang="EN-US"}*]{#struct_0_15149_x1311_324823443}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[0]{lang="EN-US"}]{.TableTextChar}]{#struct_0_15149_x1311_466908405}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[表示成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[588840961]{lang="EN-US"}]{.TableTextChar}]{#struct_0_15149_x1311_x1625026257}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[表示快转上送成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[1073807361]{lang="EN-US"}]{.TableTextChar}]{#struct_0_15149_x1311_2032992346}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[表示失败]{lang="EN-US" style="font-family:宋体"}

[[Packet discarded because VSI index (*vsi-index*) or LinkID (*link-id*) is invalid.]{lang="EN-US"}]{#struct_0_15149_x1311_357934541}

[[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_439257587}[索引]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[或链路]{style="font-family:宋体"}[ID *link-id*]{lang="EN-US"}[无效，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded because the VSI gateway interface isn\'t up, ifIndex=*ifIndex*.]{lang="EN-US"}]{#struct_0_15149_x1311_313323651}

[[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_823073229}[网关接口没有处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态，报文被丢弃，网关接口的接口索引为]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*

[[VSI gateway interface *interface-name* transmitted a packet, VSI=*vsi-index*, Link-ID=*link-id*, PktLen=*packet-len*.]{lang="EN-US"}]{#struct_0_15149_x1311_1117263822}

[[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_x1905810126}[网关接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[传输了一个数据包，该数据包从]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[Link-ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[的链路发送，数据包长度为]{style="font-family:宋体"}*[packet-len]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Failed to send a packet, VSI=*vsi-index*, Link-ID=*link-id*.]{lang="EN-US"}]{#struct_0_15149_x1311_x1524101689}

[[从]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_15149_x1311_725193827}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[Link-ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*[的链路发送数据包失败]{style="font-family:宋体"}

[[VTEP doesn\'t reply to the ARP request on behalf of the remote-site host because ARP flooding suppression is disabled.]{lang="EN-US"}]{#struct_0_15149_x1311_1294377379}

[[ARP]{lang="EN-US"}]{#struct_0_15149_x1311_x1980717612}[泛洪抑制功能未使能，不进行]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代答]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x694252723}

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_689847370}[打开]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关，从]{style="font-family:宋体"}[AC]{lang="EN-US"}[接口收到报文，并通过]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发该报文时，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2vpn packet]{lang="EN-US"}]{#struct_0_15149_x1311_x694056115}

[\*Oct 19 09:13:03:979 2010 Sysname L2VFW/7/PACKET:Slot=2;]{lang="EN-US"}

[L2VPN Input: Received a packet from interface GE1/0/1 Service Instance 0, PktLen=70.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1661464969}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的以太网服务实例]{style="font-family:宋体"}[0]{lang="EN-US"}[接收到报文，报文长度为]{style="font-family:宋体"}[70]{lang="EN-US"}[字节。]{style="font-family:宋体"}*

[[\*Dec 18 17:29:37:708 2012 Sysname L2VFW/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_15149_x1311_x1713683909}

[PUSH Label=1151, EXP=0, TTL=255.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x694121651}*[为报文添加]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签]{style="font-family:宋体"}[1151]{lang="EN-US"}[，标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Dec 18 17:29:37:708 2012 Sysname L2VFW/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_15149_x1311_1077784833}

[PUSH Label=1150, EXP=0, TTL=255.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x693925043}*[为报文添加公网隧道标签]{style="font-family:宋体"}[1150]{lang="EN-US"}[，标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x757824426}[打开]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[报文调试信息开关，将报文发送到]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2vpn packet]{lang="EN-US"}]{#struct_0_15149_x1311_x693990579}

[\*Jul  8 15:47:10:062 2013 Sysname L2VFW/7/PACKET: -Slot=2; ]{lang="EN-US"}

[L2L3: Sent a packet to interface L2VE130, PktLen=98.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1950341498}*[将报文发送到]{style="font-family:宋体"}[L2VE130]{lang="EN-US"}[接口，报文长度为]{style="font-family:宋体"}[98]{lang="EN-US"}[字节。]{style="font-family:宋体"}*

::: {#-420401342 .myid}
[]{#_Toc404791335}[]{#struct_0_15149_x1311_x1905285486}

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging mpls ldpvc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15149_x1311_411183681}

[**[debugging mpls ldpvc ]{lang="EN-US"}**[{ **advertisement** \| **all** \| **error** \| **event** \| **hsb** }]{lang="EN-US"}]{#struct_0_15149_x1311_965203953}

[**[undo debugging mpls ldpvc]{lang="EN-US"}**[ { **advertisement** \| **all** \| **error** \| **event** \| **hsb** }]{lang="EN-US"}]{#struct_0_15149_x1311_x761892136}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15149_x1311_1883769600}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15149_x1311_2005157588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x694449330}

[[network-admin]{lang="EN-US"}]{#struct_0_15149_x1311_x1995043660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15149_x1311_x694514866}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x426771548}

[**[advertisement]{lang="EN-US"}**]{#struct_0_15149_x1311_1229092370}[：表示用来通告]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[消息的调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_15149_x1311_402070811}[：表示]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_15149_x1311_1863959577}[：表示]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_15149_x1311_951657067}[：表示]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[hsb]{lang="EN-US"}**]{#struct_0_15149_x1311_x2073681242}[：表示]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[备份调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15149_x1311_1095002481}

[**[debugging mpls ldpvc]{lang="EN-US"}**]{#struct_0_15149_x1311_x60854417}[命令用来打开]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls ldpvc]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}]{#struct_0_15149_x1311_802538419}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging mpls ldpvc advertisement]{lang="EN-US"}]{#struct_0_15149_x1311_x426837084}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1308458246}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_1249545545}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1776425634}

[[Received a *message-type* message.]{lang="EN-US"}]{#struct_0_15149_x1311_x855734855}

[[Message content:]{lang="EN-US"}]{#struct_0_15149_x1311_x1843716035}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_x89022396}

[[LSR ID of peer PE:             *peer-lsrid*]{lang="EN-US"}]{#struct_0_15149_x1311_724617132}

[[VC ID:                                 *vc-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x427295835}

[[VC type:                             *vc-type*]{lang="EN-US"}]{#struct_0_15149_x1311_x1907252510}

[[Label:                                 *label*]{lang="EN-US"}]{#struct_0_15149_x1311_x2061270073}

[[LDP status code:     *         status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_x274938377}

[[PW status code:            *    pw-status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_1906662919}

[[C-bit:                               *   c-Bit*]{lang="EN-US"}]{#struct_0_15149_x1311_x427361371}

[[收到一个]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_15149_x1311_486241689}[消息，]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_1335163624}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_1028753813}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}*[peer-lsrid]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VC ID]{lang="EN-US"}]{#struct_0_15149_x1311_1689227601}[为]{lang="EN-US" style="font-family:宋体"}*[vc-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VC]{lang="EN-US"}]{#struct_0_15149_x1311_x1310337660}[类型为]{lang="EN-US" style="font-family:宋体"}*[vc-type]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[标签为]{lang="EN-US" style="font-family:宋体"}*[label]{lang="EN-US"}*]{#struct_0_15149_x1311_x427164763}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP]{lang="EN-US"}]{#struct_0_15149_x1311_x1037816221}[状态码为]{lang="EN-US" style="font-family:宋体"}*[status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_825639438}[状态码为]{lang="EN-US" style="font-family:宋体"}*[pw-status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[是否携带控制字比特为]{style="font-family:宋体"}]{#struct_0_15149_x1311_1231580311}*[c-Bit]{lang="EN-US"}*

[[Received a *message-type* message.]{lang="EN-US"}]{#struct_0_15149_x1311_x856222599}

[[Message content:]{lang="EN-US"}]{#struct_0_15149_x1311_x427230299}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_85983405}

[[LSR ID of peer PE:             *peer-lsrid*]{lang="EN-US"}]{#struct_0_15149_x1311_1575963066}

[[VPLS ID:                            *vpls-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x817387392}

[[SAII:                                   *saii*]{lang="EN-US"}]{#struct_0_15149_x1311_x1428601120}

[[TAII:                                   *taii*]{lang="EN-US"}]{#struct_0_15149_x1311_x427033691}

[[VC type:                             *vc-type*]{lang="EN-US"}]{#struct_0_15149_x1311_x1082499524}

[[Label:                                 *label*]{lang="EN-US"}]{#struct_0_15149_x1311_956250643}

[[LDP status code:   *            status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_1100688627}

[[PW status code:            *    pw-status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_x427099227}

[[C-bit:                               *   c-Bit*]{lang="EN-US"}]{#struct_0_15149_x1311_x1136977431}

[[收到一个]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_15149_x1311_x128360044}[消息，]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_359792891}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_x426902619}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}*[peer-lsrid]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS ID]{lang="EN-US"}]{#struct_0_15149_x1311_2000349940}[为]{lang="EN-US" style="font-family:宋体"}*[vpls-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SAII]{lang="EN-US"}]{#struct_0_15149_x1311_x954650571}[为]{lang="EN-US" style="font-family:宋体"}*[saii]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TAII]{lang="EN-US"}]{#struct_0_15149_x1311_x181144884}[为]{lang="EN-US" style="font-family:宋体"}*[taii]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VC]{lang="EN-US"}]{#struct_0_15149_x1311_x426968155}[类型为]{lang="EN-US" style="font-family:宋体"}*[vc-type]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[标签为]{lang="EN-US" style="font-family:宋体"}*[label]{lang="EN-US"}*]{#struct_0_15149_x1311_x1905482094}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP]{lang="EN-US"}]{#struct_0_15149_x1311_1428231027}[状态码为]{lang="EN-US" style="font-family:宋体"}*[status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_x1284593477}[状态码为]{lang="EN-US" style="font-family:宋体"}*[pw-status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[是否携带控制字比特为]{style="font-family:宋体"}]{#struct_0_15149_x1311_x426771547}*[c-Bit]{lang="EN-US"}*

[[Sent a *message-type* message.]{lang="EN-US"}]{#struct_0_15149_x1311_1229813266}

[[Message content:]{lang="EN-US"}]{#struct_0_15149_x1311_1192071343}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_x426837083}

[[LSR ID of peer PE:             *peer-lsrid*]{lang="EN-US"}]{#struct_0_15149_x1311_1249742153}

[[VC ID:                                 *vc-id*]{lang="EN-US"}]{#struct_0_15149_x1311_1717525060}

[[VC type:                             *vc-type*]{lang="EN-US"}]{#struct_0_15149_x1311_1300259408}

[[Label:                                 *label*]{lang="EN-US"}]{#struct_0_15149_x1311_x427295838}

[[LDP status code:             *          status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_x1907055902}

[[PW status code:            *    pw-status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_x768971511}

[[C-bit:                               *   c-Bit*]{lang="EN-US"}]{#struct_0_15149_x1311_x427361374}

[[发送一个]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_15149_x1311_486569369}[消息，]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_1188928857}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_82825592}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}*[peer-lsrid]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VC ID]{lang="EN-US"}]{#struct_0_15149_x1311_x427164766}[为]{lang="EN-US" style="font-family:宋体"}*[vc-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VC]{lang="EN-US"}]{#struct_0_15149_x1311_x1037488541}[类型为]{lang="EN-US" style="font-family:宋体"}*[vc-type]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[标签为]{lang="EN-US" style="font-family:宋体"}*[label]{lang="EN-US"}*]{#struct_0_15149_x1311_1467247088}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP]{lang="EN-US"}]{#struct_0_15149_x1311_x427230302}[状态码为]{lang="EN-US" style="font-family:宋体"}*[status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_2041577654}[状态码为]{lang="EN-US" style="font-family:宋体"}*[pw-status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[是否携带控制字比特为]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1483214732}*[c-Bit]{lang="EN-US"}*

[[Sent a *message-type*  message.]{lang="EN-US"}]{#struct_0_15149_x1311_x427033694}

[[Message content:]{lang="EN-US"}]{#struct_0_15149_x1311_x1082827204}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_1881366629}

[[LSR ID of peer PE:             *peer-lsrid*]{lang="EN-US"}]{#struct_0_15149_x1311_x427099230}

[[VPLS ID:                            *vpls-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x1137436184}

[[SAII:                                   *saii*]{lang="EN-US"}]{#struct_0_15149_x1311_1077381261}

[[TAII:                                   *taii*]{lang="EN-US"}]{#struct_0_15149_x1311_x426902622}

[[VC type:                             *vc-type*]{lang="EN-US"}]{#struct_0_15149_x1311_1999760113}

[[Label:                                 *label*]{lang="EN-US"}]{#struct_0_15149_x1311_x853911475}

[[LDP status code:          *     status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_x426968158}

[[PW status code:            *    pw-status-code*]{lang="EN-US"}]{#struct_0_15149_x1311_x1906202990}

[[C-bit:                               *   c-Bit*]{lang="EN-US"}]{#struct_0_15149_x1311_x426771550}

[[发送一个]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_15149_x1311_1229616659}[消息，]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_x332707229}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_x426837086}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}*[peer-lsrid]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS ID]{lang="EN-US"}]{#struct_0_15149_x1311_1249414473}[为]{lang="EN-US" style="font-family:宋体"}*[vpls-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SAII]{lang="EN-US"}]{#struct_0_15149_x1311_2135191779}[为]{lang="EN-US" style="font-family:宋体"}*[saii]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TAII]{lang="EN-US"}]{#struct_0_15149_x1311_x427295837}[为]{lang="EN-US" style="font-family:宋体"}*[taii]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VC]{lang="EN-US"}]{#struct_0_15149_x1311_x1907121438}[类型为]{lang="EN-US" style="font-family:宋体"}*[vc-type]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[标签为]{lang="EN-US" style="font-family:宋体"}*[label]{lang="EN-US"}*]{#struct_0_15149_x1311_x2144243417}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP]{lang="EN-US"}]{#struct_0_15149_x1311_x427361373}[状态码为]{lang="EN-US" style="font-family:宋体"}*[status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW]{lang="EN-US"}]{#struct_0_15149_x1311_486372761}[状态码为]{lang="EN-US" style="font-family:宋体"}*[pw-status-code]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[是否携带控制字比特为]{style="font-family:宋体"}]{#struct_0_15149_x1311_x427164765}*[c-Bit]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging mpls ldpvc error]{lang="EN-US"}]{#struct_0_15149_x1311_x1037685149}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1304467738}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x356924132}

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_653271169}

[[Received an invalid VSI event (*event-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_1427145196}

[[LDP]{lang="EN-US"}]{#struct_0_15149_x1311_x1452485143}[收到一个非法的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Failed to add a peer because VSI doesn't exist.]{lang="EN-US"}]{#struct_0_15149_x1311_1496364372}

[[LDP]{lang="EN-US"}]{#struct_0_15149_x1311_x427230301}[添加]{style="font-family:宋体"}[peer]{lang="EN-US"}[失败，因为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging mpls ldpvc event]{lang="EN-US"}]{#struct_0_15149_x1311_2041774262}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1278200139}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_2010473680}

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x222385}

[[Received an event (*event-type*) from L2VPN.]{lang="EN-US"}]{#struct_0_15149_x1311_x1150171959}

[[收到一个]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x355853990}[事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Received a session event (*event-type*) from LDP.]{lang="EN-US"}]{#struct_0_15149_x1311_1993446723}

[[收到一个]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_15149_x1311_x427033693}[会话事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Notified L2VPN to add a PW. VSI index: *vsi-index*, link ID: *link-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x1082630596}

[[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_444715899}[添加一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[link ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*

[[Notified L2VPN to delete a PW. VSI index: *vsi-index*, link ID: *link-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x253635759}

[[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x1611093049}[删除一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[，]{style="font-family:宋体"}[ PW]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[link ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15149_x1311_35574408}

[[\# ]{lang="PT-BR"}]{#struct_0_15149_x1311_x1401613034}[打开]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[的错误调试信息开关。将]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[去使能，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldpvc error]{lang="EN-US"}]{#struct_0_15149_x1311_x427099229}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] undo l2vpn enable]{lang="EN-US"}

[Info: This command will delete L2VPN globally. Continue? \[Y/N\]:y]{lang="EN-US"}

[Info: L2VPN is deleting, please wait \....Finished!]{lang="EN-US"}

[\*Sep  5 08:39:18:619 2011 Sysname LDPVC/7/ERROR: -MDC=1; Failed to connect to L2VPN.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1136846359}*[和]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[进程连接失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_1572575004}[打开]{style="font-family:宋体"}[MPLS LDP VC]{lang="EN-US"}[的事件调试信息开关。在设备上创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，配置信令协议为]{style="font-family:宋体"}[LDP]{lang="EN-US"}[，并在]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令视图下配置一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[，设备上会打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldpvc event]{lang="EN-US"}]{#struct_0_15149_x1311_x712338892}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp\] peer 1.1.1.1 pw-id 100]{lang="EN-US"}

[\*Sep  5 08:41:34:541 2011 Sysname LDPVC/7/EVENT: -MDC=1; Received an event (8) from L2VPN.]{lang="EN-US"}

[\*Sep  5 08:41:34:541 2011 Sysname LDPVC/7/EVENT: -MDC=1; Notified L2VPN to add a PW. VSI index: 0xa, link ID: 8.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x795379926}*[从]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[收到]{style="font-family:宋体"}[Peer]{lang="EN-US"}[添加事件，事件类型为]{style="font-family:宋体"}[8]{lang="EN-US"}[。向]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[添加一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[。该]{style="font-family:宋体"}[PW]{lang="EN-US"}[对应的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0x0a]{lang="EN-US"}[，]{style="font-family:宋体"}[link ID]{lang="EN-US"}[为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x426902621}[打开用来通告]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[消息调试信息开关。在一个三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下绑定已经创建的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldpvc advertisement]{lang="EN-US"}]{#struct_0_15149_x1311_1999825649}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[\*Sep  5 08:48:37:706 2011 Sysname LDPVC/7/ADVER: -MDC=1; Sent a mapping message.]{lang="EN-US"}

[Message content:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[LSR ID of peer PE:            1.1.1.1]{lang="EN-US"}

[VC ID:                        100]{lang="EN-US"}

[VC type:                      4]{lang="EN-US"}

[Label:                        775253]{lang="EN-US"}

[Status code:                  0xFFFFFFFF]{lang="EN-US"}

[PW status code:               0x0]{lang="EN-US"}

[C-bit:                        0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_708162938}*[发送]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式的]{style="font-family:宋体"}[mapping]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x1093325695}[在设备的对端]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[上也进行同样的配置，则本端设备上会打印如下调试信息。]{style="font-family:宋体"}

[[\*Sep  5 08:50:38:254 2011 Sysname LDPVC/7/ADVER: -MDC=1; Received a mapping message.]{lang="EN-US"}]{#struct_0_15149_x1311_x426968157}

[Message content:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[LSR ID of peer PE:            2.2.2.2]{lang="EN-US"}

[VC ID:                        100]{lang="EN-US"}

[VC type:                      4]{lang="EN-US"}

[Label:                        775121]{lang="EN-US"}

[Status code:                  0xFFFFFFFF]{lang="EN-US"}

[PW status code:               0x0]{lang="EN-US"}

[C-bit:                        0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1905351022}*[收到]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式的]{style="font-family:宋体"}[mapping]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x1306694466}[打开用来通告]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[消息调试信息开关。在三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下绑定已经创建的]{style="font-family:宋体"}[auto-discovery]{lang="EN-US"}[类型的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldpvc advertisement]{lang="EN-US"}]{#struct_0_15149_x1311_x426771549}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[\*Sep  5 08:48:37:706 2011 Sysname LDPVC/7/ADVER: -VD=1; Sent a mapping message.]{lang="EN-US"}

[Message content:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[LSR ID of peer PE:            2.2.2.9]{lang="EN-US"}

[VPLS ID:                      100:100]{lang="EN-US"}

[SAII:                         1010109]{lang="EN-US"}

[TAII:                         2020209]{lang="EN-US"}

[VC type:                      4]{lang="EN-US"}

[Label:                        775120]{lang="EN-US"}

[LDP status code:                  0xFFFFFFFF]{lang="EN-US"}

[PW status code:               0x0]{lang="EN-US"}

[C-bit:                        0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_1229157906}*[发送]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[mapping]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_1960623910}[在设备的对端]{style="font-family:宋体"}[2.2.2.9]{lang="EN-US"}[上也进行同样的配置，则本端设备上会打印如下调试信息。]{style="font-family:宋体"}

[[\*Sep  5 08:50:38:254 2011 Sysname LDPVC/7/ADVER: -VD=1; Received a mapping message.]{lang="EN-US"}]{#struct_0_15149_x1311_x696405670}

[Message content:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[LSR ID of peer PE:            2.2.2.9]{lang="EN-US"}

[VPLS ID:                      100:100]{lang="EN-US"}

[SAII:                         2020209]{lang="EN-US"}

[TAII:                         1010109]{lang="EN-US"}

[VC type:                      4]{lang="EN-US"}

[Label:                        775120]{lang="EN-US"}

[LDP status code:                  0xFFFFFFFF]{lang="EN-US"}

[PW status code:               0x0]{lang="EN-US"}

[C-bit:                        0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_136610812}*[收到]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[mapping]{lang="EN-US"}[消息]{style="font-family:宋体"}*

::: {#1376726853 .myid}
[]{#_Toc404791336}[]{#struct_0_15149_x1311_1037676243}[]{#_Toc342065330}

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging mpls bgpvc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x426837085}

[**[debugging mpls bgpvc ]{lang="EN-US"}**[{ **advertisement** \| **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_15149_x1311_1249611081}

[**[undo debugging mpls bgpvc]{lang="EN-US"}**[ { **advertisement** \| **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_15149_x1311_x635455433}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15149_x1311_1379244942}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1025439815}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x694252725}

[[network-admin]{lang="EN-US"}]{#struct_0_15149_x1311_x694056117}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15149_x1311_x1661596041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15149_x1311_661691201}

[**[advertisement]{lang="EN-US"}**]{#struct_0_15149_x1311_x30146799}[：表示]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的网络可达消息调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_15149_x1311_x427295840}[：表示]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_15149_x1311_x1907580191}[：表示]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_15149_x1311_1913477821}[：表示]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15149_x1311_x999720642}

[**[debugging mpls bgpvc]{lang="EN-US"}**]{#struct_0_15149_x1311_1110976068}[命令用来打开]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls bgpvc]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}]{#struct_0_15149_x1311_1701375286}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-11 ]{lang="EN-US"}[debugging mpls bgpvc advertisement]{lang="EN-US"}]{#struct_0_15149_x1311_725052171}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1278742693}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1484941746}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x427361376}

[[Received a label MP_REACH_NLRI:]{lang="EN-US"}]{#struct_0_15149_x1311_486700441}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_x2040524490}

[[Nexthop:                       *nexthop*]{lang="EN-US"}]{#struct_0_15149_x1311_x83653195}

[[RD:                               *rd*]{lang="EN-US"}]{#struct_0_15149_x1311_x143626786}

[[Site ID:                         *site-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x1413655050}

[[Label base:                  *label-base*]{lang="EN-US"}]{#struct_0_15149_x1311_x427164768}

[[Label range:               * range*]{lang="EN-US"}]{#struct_0_15149_x1311_x1038406045}

[[Label offset:                * offset*]{lang="EN-US"}]{#struct_0_15149_x1311_x1067952112}

[[Route Target:               *rt*]{lang="EN-US"}]{#struct_0_15149_x1311_x516917053}

[[MTU:                           * mtu*]{lang="EN-US"}]{#struct_0_15149_x1311_x505788521}

[[Control flag:                 *flag*]{lang="EN-US"}]{#struct_0_15149_x1311_x962423206}

[[Encaps type:               *EncapType*]{lang="EN-US"}]{#struct_0_15149_x1311_x427230304}

[[收到一个带有标签块的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}]{#struct_0_15149_x1311_2041446582}[消息]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_1663335471}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下一跳属性（即远端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_757701366}[的地址）为]{lang="EN-US" style="font-family:宋体"}*[nexthop]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RD]{lang="EN-US"}]{#struct_0_15149_x1311_x1714778083}[为]{lang="EN-US" style="font-family:宋体"}*[rd]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Site]{lang="EN-US"}]{#struct_0_15149_x1311_x427033696}[标识为]{lang="EN-US" style="font-family:宋体"}*[site-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为该]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1082958276}[Site]{lang="EN-US"}[分配的标签块的初始标签值为]{style="font-family:宋体"}*[label-base]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为该]{style="font-family:宋体"}]{#struct_0_15149_x1311_833672652}[Site]{lang="EN-US"}[分配的标签块大小为]{style="font-family:宋体"}*[range]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为该]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1434892951}[Site]{lang="EN-US"}[分配的标签块的偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_15149_x1311_1648823252}[属性为]{lang="EN-US" style="font-family:宋体"}*[rt]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTU]{lang="EN-US"}]{#struct_0_15149_x1311_x427099232}[为]{lang="EN-US" style="font-family:宋体"}*[mtu]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[是否携带控制字标记为为]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1137305112}*[flag]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[封装类型为]{lang="EN-US" style="font-family:宋体"}[EncapType]{lang="EN-US"}]{#struct_0_15149_x1311_x1517240804}

[[Received a neighbor MP_REACH_NLRI:]{lang="EN-US"}]{#struct_0_15149_x1311_887280237}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_266746065}

[[Nexthop:                       *nexthop*]{lang="EN-US"}]{#struct_0_15149_x1311_x426902624}

[[VPLS ID:                      *vpls-id*]{lang="EN-US"}]{#struct_0_15149_x1311_1999629041}

[[RD:                              * rd*]{lang="EN-US"}]{#struct_0_15149_x1311_x1591853324}

[[PE address:                 *pe-address*]{lang="EN-US"}]{#struct_0_15149_x1311_x1570049917}

[[Route Target:              * rt*]{lang="EN-US"}]{#struct_0_15149_x1311_x426968160}

[[收到一个带有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_x1905678705}[信息的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_x318914578}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下一跳属性（即远端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_1406182761}[的地址）为]{lang="EN-US" style="font-family:宋体"}*[nexthop]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS ID]{lang="EN-US"}]{#struct_0_15149_x1311_x426771552}[为]{lang="EN-US" style="font-family:宋体"}*[vpls-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RD]{lang="EN-US"}]{#struct_0_15149_x1311_1229485587}[为]{lang="EN-US" style="font-family:宋体"}*[rd]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端在]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_15149_x1311_x1502095981}[实例内的标识为]{lang="EN-US" style="font-family:宋体"}*[pe-address]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_15149_x1311_650517137}[为]{lang="EN-US" style="font-family:宋体"}*[rt]{lang="EN-US"}*

[[Sent a label MP_REACH_NLRI:]{lang="EN-US"}]{#struct_0_15149_x1311_x426837088}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_1250331977}

[[Nexthop:                       ]{lang="EN-US"}]{#struct_0_15149_x1311_x1866223464}

[[RD:                               *rd*]{lang="EN-US"}]{#struct_0_15149_x1311_x982667334}

[[Site ID:                         *site-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x427295839}

[[Label base:                  *label-base*]{lang="EN-US"}]{#struct_0_15149_x1311_x1906990366}

[[Label range:               * range*]{lang="EN-US"}]{#struct_0_15149_x1311_x400634292}

[[Label offset:                * offset*]{lang="EN-US"}]{#struct_0_15149_x1311_x427361375}

[[Route Target:              *ert*]{lang="EN-US"}]{#struct_0_15149_x1311_486503833}

[[MTU:                           * mtu*]{lang="EN-US"}]{#struct_0_15149_x1311_x1888970256}

[[Control flag:                 *flag*]{lang="EN-US"}]{#struct_0_15149_x1311_x427164767}

[[Encaps type:                *EncapType*]{lang="EN-US"}]{#struct_0_15149_x1311_x1037554077}

[[发送一个带有标签块的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}]{#struct_0_15149_x1311_1158236974}[消息]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_1763338674}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RD]{lang="EN-US"}]{#struct_0_15149_x1311_x427230303}[为]{lang="EN-US" style="font-family:宋体"}*[rd]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Site]{lang="EN-US"}]{#struct_0_15149_x1311_2041643190}[标识为]{lang="EN-US" style="font-family:宋体"}*[site-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为该]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1107311883}[Site]{lang="EN-US"}[分配的标签块的初始标签值为]{style="font-family:宋体"}*[label-base]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为该]{style="font-family:宋体"}]{#struct_0_15149_x1311_x427033695}[Site]{lang="EN-US"}[分配的标签块大小为]{style="font-family:宋体"}*[range]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为该]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1082761668}[Site]{lang="EN-US"}[分配的标签块的偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_15149_x1311_x1449766215}[属性为]{lang="EN-US" style="font-family:宋体"}*[rt]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTU]{lang="EN-US"}]{#struct_0_15149_x1311_x427099231}[为]{lang="EN-US" style="font-family:宋体"}*[mtu]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[是否携带控制字标记为为]{style="font-family:宋体"}]{#struct_0_15149_x1311_x1137370648}*[flag]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[封装类型为]{lang="EN-US" style="font-family:宋体"}[EncapType]{lang="EN-US"}]{#struct_0_15149_x1311_x1182500126}

[[Sent a neighbor MP_REACH_NLRI:]{lang="EN-US"}]{#struct_0_15149_x1311_x426902623}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_15149_x1311_1999694577}

[[Nexthop:                       ]{lang="EN-US"}]{#struct_0_15149_x1311_730802896}

[[VPLS ID:                      *vpls-id*]{lang="EN-US"}]{#struct_0_15149_x1311_x426968159}

[[RD:                              * rd*]{lang="EN-US"}]{#struct_0_15149_x1311_x1906268526}

[[PE address:                 *pe_address*]{lang="EN-US"}]{#struct_0_15149_x1311_926572115}

[[Route Target:             * ert*]{lang="EN-US"}]{#struct_0_15149_x1311_x426771551}

[[发送一个带有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_15149_x1311_1229682195}[信息的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[消息内容如下：]{style="font-family:宋体"}]{#struct_0_15149_x1311_21961947}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS ID]{lang="EN-US"}]{#struct_0_15149_x1311_x426837087}[为]{lang="EN-US" style="font-family:宋体"}*[vpls-id]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RD]{lang="EN-US"}]{#struct_0_15149_x1311_1249480009}[为]{lang="EN-US" style="font-family:宋体"}*[rd]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本端在]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_15149_x1311_1138788105}[实例内的标识为]{lang="EN-US" style="font-family:宋体"}*[pe-address]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_15149_x1311_50772370}[为]{lang="EN-US" style="font-family:宋体"}*[rt]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging mpls bgpvc error]{lang="EN-US"}]{#struct_0_15149_x1311_1855876047}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1276886201}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x1484363669}

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_68992096}

[[Received an invalid VSI event (*event-type*).]{lang="EN-US"}]{#struct_0_15149_x1311_1138722569}

[[BGP VC]{lang="EN-US"}]{#struct_0_15149_x1311_113507830}[收到一个非法的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Failed to send an event.]{lang="EN-US"}]{#struct_0_15149_x1311_x23741965}

[[向]{style="font-family:宋体"}[BGPVC]{lang="EN-US"}]{#struct_0_15149_x1311_x1599860013}[线程队列写事件失败]{style="font-family:宋体"}

[[The received PE-addr *pe-address* is the same as an existing remote PE-addr. The received RD is *rd*.]{lang="EN-US"}]{#struct_0_15149_x1311_2072638190}

[[收到的]{style="font-family:宋体"}[PE_Addr]{lang="EN-US"}]{#struct_0_15149_x1311_x2139585559}[地址]{style="font-family:宋体"}*[pe-address]{lang="EN-US"}*[和已经存在的某个远端]{style="font-family:宋体"}[PE_Addr]{lang="EN-US"}[相同，此次收到的]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}*[rd]{lang="EN-US"}*

[[The received PE-addr *pe-address* is the same as the local PE-addr. The received RD is *rd*.]{lang="EN-US"}]{#struct_0_15149_x1311_1138919177}

[[收到的]{style="font-family:宋体"}[PE_Addr]{lang="EN-US"}]{#struct_0_15149_x1311_1627800628}[地址]{style="font-family:宋体"}*[pe-address]{lang="EN-US"}*[和本地配置的]{style="font-family:宋体"}[PE_Addr]{lang="EN-US"}[相同，此次收到的]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}*[rd]{lang="EN-US"}*

[[The received site ID *site-id* is the same as the ID of an existing remote site. The received RD is *rd.*]{lang="EN-US"}]{#struct_0_15149_x1311_x815123751}

[[收到的]{style="font-family:宋体"}[site-id]{lang="EN-US"}]{#struct_0_15149_x1311_1780773958}[值]{style="font-family:宋体"}*[site-id]{lang="EN-US"}*[和已经存在的某个远端]{style="font-family:宋体"}[site-id]{lang="EN-US"}[相同，此次收到的]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}*[rd]{lang="EN-US"}*

[[The received site ID *site-id* is the same as the ID of the local site. The received RD is *rd*.]{lang="EN-US"}]{#struct_0_15149_x1311_x566558096}

[[收到的]{style="font-family:宋体"}[site-id]{lang="EN-US"}]{#struct_0_15149_x1311_1138853641}[值]{style="font-family:宋体"} *[site-id]{lang="EN-US"}*[和本地配置的]{style="font-family:宋体"}[site-id]{lang="EN-US"}[相同，此次收到的]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}*[rd]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging mpls bgpvc event]{lang="EN-US"}]{#struct_0_15149_x1311_x1060337486}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1283071303}[[字段]{style="font-family:黑体"}]{#struct_0_15149_x1311_x318224427}

[[描述]{style="font-family:黑体"}]{#struct_0_15149_x1311_x931290011}

[[Received an event (*event-type*) from L2VPN.]{lang="EN-US"}]{#struct_0_15149_x1311_1565123056}

[[收到一个]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x966676096}[事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Received an event (*event-type*) from BGP.]{lang="EN-US"}]{#struct_0_15149_x1311_x1110581969}

[[收到一个]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_15149_x1311_1139050249}[事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Sent an event (*event-type*) to BGP.]{lang="EN-US"}]{#struct_0_15149_x1311_x1475341025}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_15149_x1311_x1458130242}[发送事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Notified L2VPN to add a PW. VSI index: *vsi-index*, link ID: *link-id*]{lang="EN-US"}]{#struct_0_15149_x1311_1343109403}

[[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x855810774}[添加一条]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[link ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*

[[Notified L2VPN to delete a PW. VSI index: *vsi-index*, link ID: *link-id*]{lang="EN-US"}]{#struct_0_15149_x1311_823325450}

[[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_1138984713}[删除一条]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[link ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[link-id]{lang="EN-US"}*

[[Notified L2VPN to add an auto-discovered peer. VSI index: *vsi-index*, peer: *peer-address*]{lang="EN-US"}]{#struct_0_15149_x1311_516505993}

[[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x1791946100}[添加一个自动发现]{style="font-family:宋体"}[peer]{lang="EN-US"}[，该]{style="font-family:宋体"}[peer]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，地址为]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*

[[Notified L2VPN to delete an auto-discovered peer. VSI index: *vsi-index*, peer: *peer-address*]{lang="EN-US"}]{#struct_0_15149_x1311_578661594}

[[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_15149_x1311_x557339074}[删除一个自动发现]{style="font-family:宋体"}[peer]{lang="EN-US"}[，该]{style="font-family:宋体"}[peer]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，地址为]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15149_x1311_1139181321}

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_2044371039}[打开]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的错误调试信息开关。在设备上创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，配置]{style="font-family:宋体"}[auto-discovery]{lang="EN-US"}[，并配置信令协议为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[，本端]{style="font-family:宋体"}[Site]{lang="EN-US"}[标识为]{style="font-family:宋体"}[10]{lang="EN-US"}[。然后，在对端设备上配置两个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[：两个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[RD]{lang="EN-US"}[不同，]{style="font-family:宋体"}[RT]{lang="EN-US"}[相同，使用的信令协议为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[，]{style="font-family:宋体"}[Site]{lang="EN-US"}[标识均为]{style="font-family:宋体"}[20]{lang="EN-US"}[。两端均在接口上绑定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，本端设备会打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls bgpvc error]{lang="EN-US"}]{#struct_0_15149_x1311_2139925326}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] route-distinguisher 100:1]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] vpn-target 1:1]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] signaling-protocol bgp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto-bgp\] site 10 range 30]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto-bgp\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[\*Nov 24 09:15:15:046 2012 Sysname BGPVC/7/ERROR: -MDC=1; The received site ID 20 is the same as the ID of an existing remote site. The received RD is 100:2.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x259801016}[打开]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的事件调试信息开关。在设备上创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，配置]{style="font-family:宋体"}[auto-discovery]{lang="EN-US"}[，并配置信令协议为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[，本端]{style="font-family:宋体"}[Site]{lang="EN-US"}[标识为]{style="font-family:宋体"}[10]{lang="EN-US"}[。在对端设备上也进行相应配置。两端均在接口上绑定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，设备上会打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls bgpvc event]{lang="EN-US"}]{#struct_0_15149_x1311_1139115785}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] route-distinguisher 100:1]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] vpn-target 1:1]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] signaling-protocol bgp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto-bgp\] site 10 range 30]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto-bgp\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[\*Nov 24 09:27:54:334 2012 Sysname BGPVC/7/EVENT: -MDC=1; Notified L2VPN to add a PW. VSI index: 0x0, link ID: 27.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1034826259}*[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[添加一条]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[。该]{style="font-family:宋体"}[PW]{lang="EN-US"}[对应的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0x0]{lang="EN-US"}[，]{style="font-family:宋体"}[link ID]{lang="EN-US"}[为]{style="font-family:宋体"}[27]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_1888141020}[打开]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的事件调试信息开关。在设备上创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，配置]{style="font-family:宋体"}[auto-discovery]{lang="EN-US"}[，并配置信令协议为]{style="font-family:宋体"}[LDP]{lang="EN-US"}[，]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100:100]{lang="EN-US"}[。对端设备上也进行相应的配置。两端均在接口上绑定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，设备上会打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls bgpvc event]{lang="EN-US"}]{#struct_0_15149_x1311_x1961956372}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] route-distinguisher 100:1]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] vpn-target 1:1]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto\] signaling-protocol ldp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto-bgp\] vpls-id 100:100]{lang="EN-US"}

[\[Sysname-vsi-vpn1-auto-bgp\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[\*Nov 24 09:36:24:622 2012 Sysname BGPVC/7/EVENT: -MDC=1; Notified L2VPN to add a peer. VSI index: 0x1, peer: 2.2.2.9.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x853602680}*[通知]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[添加一个自动发现]{style="font-family:宋体"}[peer]{lang="EN-US"}[。该]{style="font-family:宋体"}[peer]{lang="EN-US"}[对应的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[，地址为]{style="font-family:宋体"}[2.2.2.9]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_1139312393}[打开]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的网络可达消息调试信息开关。在一个三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下绑定已经创建的]{style="font-family:宋体"}[auto-discovery]{lang="EN-US"}[类型]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldpvc advertisement]{lang="EN-US"}]{#struct_0_15149_x1311_1652031085}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[\*Nov 24 09:31:42:182 2012 PE1 BGPVC/7/ADVER: -MDC=1; Sent a label MP_REACH_NLRI:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Nexthop:]{lang="EN-US"}

[RD:                           100:1]{lang="EN-US"}

[Site ID:                      10]{lang="EN-US"}

[Label Base:                   775158]{lang="EN-US"}

[Label Range:                  30]{lang="EN-US"}

[Label Offset:                 0]{lang="EN-US"}

[ERT:                          3:3 1:1]{lang="EN-US"}

[MTU:                          1500]{lang="EN-US"}

[Control Flag:                 0]{lang="EN-US"}

[EncapType:                    19]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_1602138221}*[发送一个带有标签块的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*Nov 24 09:32:18:193 2012 PE1 BGPVC/7/ADVER: -MDC=1; Received a label MP_REACH_NLRI:]{lang="EN-US"}]{#struct_0_15149_x1311_1139246857}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Nexthop:                      2.2.2.9]{lang="EN-US"}

[RD:                           100:2]{lang="EN-US"}

[Site ID:                      20]{lang="EN-US"}

[Label Base:                   775128]{lang="EN-US"}

[Label Range:                  30]{lang="EN-US"}

[Label Offset:                 0]{lang="EN-US"}

[ERT:                          1:1 2:2]{lang="EN-US"}

[MTU:                          1500]{lang="EN-US"}

[Control Flag:                 0]{lang="EN-US"}

[EncapType:                    19]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_x1485558742}*[收到一个带有标签块的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15149_x1311_x1808146052}[打开]{style="font-family:宋体"}[MPLS BGP VC]{lang="EN-US"}[的网络可达消息调试信息开关。创建]{style="font-family:宋体"}[auto-discovery]{lang="EN-US"}[类型的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并配置信令协议为]{style="font-family:宋体"}[LDP]{lang="EN-US"}[，在接口上绑定该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldpvc advertisement]{lang="EN-US"}]{#struct_0_15149_x1311_x2040818815}

[\*Nov 24 09:38:26:744 2012 PE1 BGPVC/7/ADVER: -MDC=1; Sent a neighbor MP_REACH_NLRI:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Nexthop:]{lang="EN-US"}

[VPLS-ID:                      100:100]{lang="EN-US"}

[RD:                           101:1]{lang="EN-US"}

[PE_address:                   1.1.1.9]{lang="EN-US"}

[ERT:                          11:11]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_1138788106}*[发送一个带有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[信息的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*Nov 24 09:38:58:732 2012 PE1 BGPVC/7/ADVER: -MDC=1; Received a neighbor MP_REACH_NLRI:]{lang="EN-US"}]{#struct_0_15149_x1311_50575762}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Nexthop:                      2.2.2.9]{lang="EN-US"}

[VPLS-ID:                      100:100]{lang="EN-US"}

[RD:                           102:1]{lang="EN-US"}

[PE_address:                   2.2.2.9]{lang="EN-US"}

[ERT:                          11:11 22:22]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15149_x1311_1802656051}*[收到一个带有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[信息的]{style="font-family:宋体"}[BGP Update]{lang="EN-US"}[消息。]{style="font-family:宋体"}*
