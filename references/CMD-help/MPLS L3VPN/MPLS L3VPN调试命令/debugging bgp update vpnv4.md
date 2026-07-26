::: {#-634711537 .myid}
[]{#_Toc404791059}[]{#struct_0_x1046_x2047_1735391933}[]{#_Toc304293040}[]{#_Toc87257691}[]{#_Toc207168985}[]{#_Toc207168986}[]{#_Toc207168987}[]{#_Toc207168988}[]{#_Toc207168989}[]{#_Toc207168990}[]{#_Toc207168991}[]{#_Toc207168992}[]{#_Toc207168993}[]{#_Toc207168994}[]{#_Toc207168995}[]{#_Toc207168996}[]{#_Toc207168997}[]{#_Toc207168998}[]{#_Toc207168999}[]{#_Toc207169165}[]{#_Toc207169166}[]{#_Toc207169485}[]{#_Toc207169486}[]{#_Toc207169526}[]{#_Toc207169527}[]{#_Toc207169528}[]{#_Toc207169529}[]{#_Toc207169531}[]{#_Toc207169532}[]{#_Toc207169533}[]{#_Toc207169534}[]{#_Toc207169537}[]{#_Toc207169539}[]{#_Toc207169540}[]{#_Toc207169565}[]{#_Toc207169572}[]{#_Toc207169573}[]{#_Toc207169574}[]{#_Toc207169576}[]{#_Toc207169577}[]{#_Toc207169579}[]{#_Toc207169580}[]{#_Toc207169582}[]{#_Toc207169583}[]{#_Toc293565315}[]{#_Toc293565316}[]{#_Toc293565317}[]{#_Toc293565318}[]{#_Toc293565319}[]{#_Toc293565320}[]{#_Toc293565321}[]{#_Toc293565322}[]{#_Toc293565323}[]{#_Toc293565324}[]{#_Toc293565325}[]{#_Toc293565327}[]{#_Toc293565328}[]{#_Toc293565329}[]{#_Toc293565477}[]{#_Toc293565478}[]{#_Toc293565479}[]{#_Toc293565480}[]{#_Toc293565483}[]{#_Toc293565486}[]{#_Toc293565490}[]{#_Toc293565493}[]{#_Toc293565501}[]{#_Toc293565504}[]{#_Toc293565507}[]{#_Toc293565510}[]{#_Toc293565514}[]{#_Toc293565515}[]{#_Toc293565517}[]{#_Toc293565518}[]{#_Toc293565521}[]{#_Toc293565522}[]{#_Toc293565524}[]{#_Toc293565525}[]{#_Toc293565529}[]{#_Toc293565530}[]{#_Toc293565532}[]{#_Toc293565533}[]{#_Toc293565536}[]{#_Toc293565537}[]{#_Toc293565539}[]{#_Toc293565540}[]{#_Toc293565542}[]{#_Toc293565544}[]{#_Toc293565545}[]{#_Toc293565547}[]{#_Toc293565548}[]{#_Toc293565552}[]{#_Toc293565553}[]{#_Toc293565555}[]{#_Toc293565556}[]{#_Toc293565560}[]{#_Toc293565562}[]{#_Toc293565563}[]{#_Toc293565564}

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp update vpnv4**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1133404001}

[**[debugging bgp update]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **vpnv4** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_x2060969112}

[**[undo debugging bgp update]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **vpnv4** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_658836341}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1980469186}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1935105321}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_511668697}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x991240674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x301718148}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1227135280}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_1960176671}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1668326451}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1046_x2047_1234374482}[：表示接收的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1046_x2047_x698137910}[：表示发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1999791557}

[**[debugging bgp update vpnv4]{lang="EN-US"}**]{#struct_0_x1046_x2047_416307668}[命令用来打开]{style="font-family:
宋体"}[BGP VPNv4]{lang="EN-US"}[的]{style="font-family:
宋体"}[Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging bgp vpnv4**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980534722}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging bgp update vpnv4]{lang="EN-US"}]{#struct_0_x1046_x2047_x1701380856}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2052063008}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1779345847}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1718119682}

[[BGP_L3VPN.: Recv UPDATE from peer *ip-address* with following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_648481121}

[[从对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_309448593}[接收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[BGP_L3VPN.: Send UPDATE to peer *ip-address* for following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_x61100419}

[[向对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_1098097693}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Update message length]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980600258}

[[Update]{lang="EN-US"}]{#struct_0_x1046_x2047_1006862364}[消息的长度，单位为字节]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_1802844594}

[[路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_x184421035}[属性，即路由信息的来源，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[IGP]{lang="IT"}]{#struct_0_x1046_x2047_772585862}[：网络层可达信息来源于]{style="font-family:宋体"}[AS]{lang="IT"}[内部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[EGP]{lang="IT"}]{#struct_0_x1046_x2047_1343078455}[：网络层可达信息通过]{style="font-family:宋体"}[EGP]{lang="IT"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incomplete]{lang="IT"}]{#struct_0_x1046_x2047_x1980665794}[：网络层可达信息通过其他方式学习]{lang="EN-US" style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_x1046_x2047_x1912638479}

[[路由的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}]{#struct_0_x1046_x2047_x1976972020}[属性，即路由从本地到目的地址所要经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_x1046_x2047_1764878478}

[[路由的下一跳属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1104171534}

[[Local pref]{lang="EN-US"}]{#struct_0_x1046_x2047_x57015424}

[[路由的本地优先级]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1980731330}

[[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_x1204033982}

[[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_289145547}[（]{style="font-family:宋体"}[Multi-Exit Discriminator]{lang="EN-US"}[，多出口区分）值]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_x1046_x2047_x874075520}

[[路由的扩展团体属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x656908434}

[*[prefix/mask ]{lang="EN-US"}*[(RD *route-distinguisher*, Label *label*)]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980796866}

[[路由前缀为]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*]{#struct_0_x1046_x2047_x582824671}[、路由前缀的掩码长度为]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[、]{style="font-family:宋体"}[RD]{lang="EN-US"}[值为]{style="font-family:宋体"}*[route-distinguisher]{lang="EN-US"}*[、标签值为]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[[Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*]{lang="EN-US"}]{#struct_0_x1046_x2047_x566028328}

[[向地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_1284209545}[的对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，下一跳地址为]{style="font-family:宋体"}*[next-hop]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x712161413}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_1170365821}[打开对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关。从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[接收、向对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文时打印相关调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update 1.1.1.1 vpnv4]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980862402}

[\*Mar 25 16:49:43:054 2011 Sysname BGP/7/DEBUG: -MDC=1;]{lang="DA"}

[         ]{lang="DA"}[BGP_L3VPN.: Recv UPDATE from peer 3.3.3.3 with following destinations:]{lang="EN-US"}

[         Update message length : 98]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 20]{lang="EN-US"}

[         Next hop     : 3.3.3.3]{lang="EN-US"}

[         Local pref   : 100]{lang="EN-US"}

[         MED          : 0]{lang="EN-US"}

[         Ext-Community: \<RT: 1:2\>]{lang="EN-US"}

[         8.8.8.8/32 (RD 1]{lang="EN-US"}[：]{style="font-family:宋体"}[2, Label 1000120)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_1073121978}*[从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，消息长度为]{style="font-family:宋体"}[98]{lang="EN-US"}[字节，路由信息通过]{style="font-family:宋体"}[IGP]{lang="EN-US"}[、]{style="font-family:宋体"}[EGP]{lang="EN-US"}[之外的其他方式学习，]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径为]{style="font-family:宋体"}[20]{lang="EN-US"}[，下一跳为]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[，本地优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[MED]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，路由前缀为]{style="font-family:宋体"}[8.8.8.8/32]{lang="EN-US"}[，]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，标签值为]{style="font-family:宋体"}[1000120]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Mar 25 16:49:43:065 2011 ]{lang="DA"}[Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_x1046_x2047_x1343438768}

[         BGP_L3VPN.: Send UPDATE to peer 3.3.3.3 for following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 20]{lang="EN-US"}

[         Next hop     : 3.3.3.1]{lang="EN-US"}

[         Local pref   : 100]{lang="EN-US"}

[         MED          : 0]{lang="EN-US"}

[         Ext-Community: \<RT: 1:2\>]{lang="EN-US"}

[         8.8.8.8/32 (RD 1]{lang="EN-US"}[：]{style="font-family:宋体"}[2, Label 1000120)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1413529747}*[向对等体]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，路由信息通过]{style="font-family:宋体"}[IGP]{lang="EN-US"}[、]{style="font-family:宋体"}[EGP]{lang="EN-US"}[之外的其他方式学习，]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径为]{style="font-family:宋体"}[20]{lang="EN-US"}[，下一跳为]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[，本地优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[MED]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，路由前缀为]{style="font-family:宋体"}[8.8.8.8/32]{lang="EN-US"}[，]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，标签值为]{style="font-family:宋体"}[1000120]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Mar 25 16:49:44:012 2011]{lang="DA"}[ ]{lang="DA"}[Sysname BGP/7/DEBUG: -MDC=1; ]{lang="EN-US"}]{#struct_0_x1046_x2047_2112584562}

[ BGP.: Send UPDATE MSG to peer 3.3.3.3(IPv4-VPN) NextHop: 3.3.3.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1979879362}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[发送路由更新，下一跳地址为]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-808137150 .myid}
[]{#_Toc404791060}[]{#struct_0_x1046_x2047_1729024486}[]{#_Toc304293042}[]{#_Toc320024914}[]{#_Toc320026549}[]{#_Toc320024915}[]{#_Toc320026550}[]{#_Toc320024916}[]{#_Toc320026551}[]{#_Toc320024917}[]{#_Toc320026552}[]{#_Toc320024918}[]{#_Toc320026553}[]{#_Toc320024919}[]{#_Toc320026554}[]{#_Toc320024920}[]{#_Toc320026555}[]{#_Toc320024921}[]{#_Toc320026556}[]{#_Toc320024922}[]{#_Toc320026557}[]{#_Toc320024923}[]{#_Toc320026558}[]{#_Toc320024924}[]{#_Toc320026559}[]{#_Toc320024925}[]{#_Toc320026560}[]{#_Toc320024926}[]{#_Toc320026561}[]{#_Toc320024927}[]{#_Toc320026562}[]{#_Toc320024928}[]{#_Toc320026563}[]{#_Toc320024929}[]{#_Toc320026564}[]{#_Toc320024930}[]{#_Toc320026565}[]{#_Toc320024967}[]{#_Toc320026602}[]{#_Toc320024968}[]{#_Toc320026603}[]{#_Toc320024969}[]{#_Toc320026604}[]{#_Toc320024970}[]{#_Toc320026605}[]{#_Toc320024971}[]{#_Toc320026606}[]{#_Toc320024972}[]{#_Toc320026607}[]{#_Toc320024973}[]{#_Toc320026608}[]{#_Toc320024974}[]{#_Toc320026609}[]{#_Toc320024975}[]{#_Toc320026610}[]{#_Toc320024976}[]{#_Toc320026611}[]{#_Toc320024977}[]{#_Toc320026612}[]{#_Toc320024978}[]{#_Toc320026613}[]{#_Toc320024979}[]{#_Toc320026614}[]{#_Toc320024980}[]{#_Toc320026615}[]{#_Toc320024981}[]{#_Toc320026616}[]{#_Toc320024982}[]{#_Toc320026617}[]{#_Toc320024983}[]{#_Toc320026618}[]{#_Toc320024984}[]{#_Toc320026619}[]{#_Toc320024985}[]{#_Toc320026620}[]{#_Toc320024986}[]{#_Toc320026621}[]{#_Toc320024987}[]{#_Toc320026622}[]{#_Toc320024988}[]{#_Toc320026623}[]{#_Toc320024989}[]{#_Toc320026624}[]{#_Toc320024990}[]{#_Toc320026625}[]{#_Toc320024991}[]{#_Toc320026626}[]{#_Toc283627065}

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp update vpn-instance ipv4**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1920164203}

[**[debugging bgp update]{lang="EN-US"}**[ **vpn-instance** *vpn-instance-name* *ip-address* \[ *mask-length* \] **ipv4** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_1040802133}

[**[undo debugging bgp update]{lang="EN-US"}***[ ]{lang="EN-US"}***[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}***[ ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \[ *mask-length* \] **ipv4** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_65558937}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_307017382}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1097113859}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_511472089}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x443878207}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x367413590}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1979944898}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_520604738}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1668523062}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1873907521}[：]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1046_x2047_908133909}[：表示接收的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1046_x2047_865166697}[：表示发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1793032910}

[**[debugging bgp update vpn-instance ipv4]{lang="EN-US"}**]{#struct_0_x1046_x2047_x1314951305}[命令用来打开指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP IPv4 Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging bgp update vpn-instance ipv4**]{lang="EN-US"}[命令用来关闭指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP IPv4 Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1046_x2047_x1956638065}[实例的]{style="font-family:宋体"}[BGP IPv4 Update]{lang="EN-US"}[报文调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging bgp update vpn-instance ipv4]{lang="EN-US"}]{#struct_0_x1046_x2047_438894129}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2057318048}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1980403653}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1236750251}

[[BGP.vpn1: Recv UPDATE from peer *ip-address* with following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_937701619}

[[从对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_x2004152776}[接收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[BGP.: Send UPDATE to peer *ip-address* for following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_x1036134795}

[[向对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1474928694}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Update message length]{lang="EN-US"}]{#struct_0_x1046_x2047_x1044188394}

[[Update]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980469189}[消息的长度]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_1531820794}

[[路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_x1951460325}[属性，即路由信息的来源，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[IGP]{lang="IT"}]{#struct_0_x1046_x2047_x724536236}[：网络层可达信息来源于]{style="font-family:宋体"}[AS]{lang="IT"}[内部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[EGP]{lang="IT"}]{#struct_0_x1046_x2047_1809324035}[：网络层可达信息通过]{style="font-family:宋体"}[EGP]{lang="IT"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incomplete]{lang="IT"}]{#struct_0_x1046_x2047_161937020}[：网络层可达信息通过其他方式学习]{lang="EN-US" style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_x1046_x2047_x1384905401}

[[路由的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980534725}[属性，即路由从本地到目的地址所要经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_x1046_x2047_x941865969}

[[路由的下一跳属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_786084863}

[[Local pref]{lang="EN-US"}]{#struct_0_x1046_x2047_1889244787}

[[路由的本地优先级]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x7714280}

[[MED ]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980600261}

[[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_x202925681}[属性]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_x1046_x2047_x38979370}

[[路由的扩展团体属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1630809998}

[*[prefix]{lang="EN-US"}*[/*mask*]{lang="EN-US"}]{#struct_0_x1046_x2047_x1380047632}

[[路由前缀为]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1980665797}[、路由前缀的掩码长度为]{style="font-family:宋体"}*[mask]{lang="EN-US"}*

[[Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*]{lang="EN-US"}]{#struct_0_x1046_x2047_1979044290}

[[向地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_789055338}[的对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，下一跳地址为]{style="font-family:宋体"}*[next-hop]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1869471931}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_x1091385372}[打开]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[中对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4 Update]{lang="EN-US"}[报文调试信息开关。在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内向对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文时打印相关调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update 1.1.1.1 vpn-instance vpn1 ipv4 send]{lang="DA"}]{#struct_0_x1046_x2047_x1980731333}

[\*Jul  9 18:10:27:900 2010 Sysname BGP/7/BGPDEBUG:]{lang="EN-US"}

[         BGP.vpn1: Send UPDATE to peer 1.1.1.1 for following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      :]{lang="EN-US"}

[         Next hop     : 1.1.1.2]{lang="EN-US"}

[         Local pref   : 100]{lang="EN-US"}

[         MED          : 0]{lang="EN-US"}

[         11.1.1.0/24]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_x800749455}*[在]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内向对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP IPv4 Update]{lang="EN-US"}[报文，路由信息通过]{style="font-family:宋体"}[IGP]{lang="EN-US"}[、]{style="font-family:宋体"}[EGP]{lang="EN-US"}[之外的其他方式学习，下一跳为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，本地优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[MED]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，路由前缀为]{style="font-family:宋体"}[11.1.1.0/24]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jul  9 18:10:27:950 2010 Sysname BGP/7/DEBUG: -MDC=1; ]{lang="EN-US"}]{#struct_0_x1046_x2047_x2031416587}

[ BGP.vpn1: Send UPDATE MSG to peer 1.1.1.1(IPv4-UNC) NextHop: 1.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_1708557761}*[向]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[发送路由更新，下一跳地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#1826730624 .myid}
[]{#_Toc304293043}[]{#_Toc404791061}[]{#struct_0_x1046_x2047_993362197}[]{#_Toc333326093}[]{#_Toc283627067}[]{#_Toc283627068}[]{#_Toc283627069}[]{#_Toc283627070}[]{#_Toc283627071}[]{#_Toc283627072}[]{#_Toc283627073}[]{#_Toc283627074}[]{#_Toc283627075}[]{#_Toc283627076}[]{#_Toc283627077}[]{#_Toc283627078}[]{#_Toc283627080}[]{#_Toc283627082}[]{#_Toc283627083}[]{#_Toc283627084}[]{#_Toc283627085}[]{#_Toc283627086}[]{#_Toc283627087}[]{#_Toc283627088}[]{#_Toc283627097}

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp update-group vpnv4**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x480789025}

[**[debugging bgp update-group vpnv4]{lang="EN-US"}**]{#struct_0_x1046_x2047_x222948142}

[**[undo debugging bgp update-group vpnv4]{lang="EN-US"}**]{#struct_0_x1046_x2047_1983620753}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1394439979}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1209745075}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_511668696}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_511734232}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x1759507696}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1726183209}

[[无]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x666529391}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x214372114}

[**[debugging bgp update-group vpnv4]{lang="EN-US"}**]{#struct_0_x1046_x2047_x1973884665}[命令用来打开]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族的打包组调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp update-group vpnv4]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族的打包组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}]{#struct_0_x1046_x2047_x1765207241}[地址族的打包组调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[打开调试信息开关会影响系统的性能，因此，请不要轻易打开调试信息开关，调试完毕后，请及时关闭调试信息开关。]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1621938991}

[[表1-3 ]{lang="EN-US"}[debugging bgp update-group vpnv4]{lang="EN-US"}]{#struct_0_x1046_x2047_313579415}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2056281632}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1980862405}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_669837451}

[[Send UPDATE to update-group *group-id*]{lang="EN-US"}]{#struct_0_x1046_x2047_x392426255}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_473632606}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送路由更新]{style="font-family:宋体"}

[[Send UPDATE(Withdraw) to update-group *group-id*]{lang="EN-US"}]{#struct_0_x1046_x2047_x528738628}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x713906608}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送路由撤销]{style="font-family:宋体"}

[*[destination-address]{lang="EN-US"}*[/*mask-length*]{lang="EN-US"}]{#struct_0_x1046_x2047_x1577010121}

[[发布的路由前缀的目的地址和掩码]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1979879365}

[[Update message length]{lang="EN-US"}]{#struct_0_x1046_x2047_1325739959}

[[Update]{lang="EN-US"}]{#struct_0_x1046_x2047_x653832969}[消息长度]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_83429844}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x51289475}[的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_x1046_x2047_495363465}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x1979944901}[的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_x1046_x2047_1729999568}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_711871537}[的]{style="font-family:宋体"}[Next Hop]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Local pref]{lang="EN-US"}]{#struct_0_x1046_x2047_x797095770}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_384074512}[的]{style="font-family:宋体"}[Local Pref]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_2121784740}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980403652}[的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Community]{lang="EN-US"}]{#struct_0_x1046_x2047_329333690}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_1519925504}[的团体属性]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_x1046_x2047_x1053335090}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_1235693970}[的扩展团体属性]{style="font-family:宋体"}

[[update-group *group-id* *address-family* created]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980469188}

[[创建地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1197062561}[的打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*

[[update-group *group-id* *address-family* deleted]{lang="EN-US"}]{#struct_0_x1046_x2047_983706591}

[[删除地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_980347803}[的打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1350362599}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_256392183}[打开]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[打包组调试信息开关，发布]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[路由时，设备上将打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update-group vpnv4]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980534724}

[\*Apr 16 21:06:16:48 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP.L3VPN: Send UPDATE to update-group 0 for following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 100]{lang="EN-US"}

[         Next hop     : 192.168.109.88]{lang="EN-US"}

[         Ext-Community: \<RT: 1:2\>]{lang="EN-US"}

[         8.8.8.8/32 (RD 1:2, Label 1000120)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_1787017386}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组]{style="font-family:宋体"}[0]{lang="EN-US"}[发送路由更新，路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性为]{style="font-family:宋体"}[Incomplete]{lang="EN-US"}[，]{style="font-family:宋体"}[AS path]{lang="EN-US"}[属性为]{style="font-family:宋体"}[100]{lang="EN-US"}[，下一跳地址为]{style="font-family:宋体"}[192.168.109.88]{lang="EN-US"}[，路由的扩展团体属性]{style="font-family:宋体"}[RT]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，发布的路由前缀为]{style="font-family:宋体"}[111.1.1.1/32]{lang="EN-US"}[，]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，通告的标签为]{style="font-family:宋体"}[1000120]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-2099944137 .myid}
[]{#_Toc404791062}[]{#struct_0_x1046_x2047_x172370630}

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp label**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x423493087}

[**[debugging bgp label ]{lang="EN-US"}**]{#struct_0_x1046_x2047_x483631311}

[**[undo debugging bgp label]{lang="EN-US"}**]{#struct_0_x1046_x2047_x1518290490}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1210412969}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1980600260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_511472088}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_512061912}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_85933331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x643346791}

[[无]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1627695775}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1970447383}

[**[debugging bgp label]{lang="EN-US"}**]{#struct_0_x1046_x2047_984401993}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[标签分配调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging bgp label**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[标签分配调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x474318126}[标签分配调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging bgp label]{lang="EN-US"}]{#struct_0_x1046_x2047_2142395720}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2060912416}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1980665796}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x749839065}

[[SEND LABEL In/Out/Op]{lang="EN-US"}]{#struct_0_x1046_x2047_x783013054}

[[标签相关调试信息，包括入标签（]{style="font-family:宋体"}[In]{lang="EN-US"}]{#struct_0_x1046_x2047_x312422553}[）、出标签（]{style="font-family:宋体"}[Out]{lang="EN-US"}[）和操作类型（]{style="font-family:宋体"}[Op]{lang="EN-US"}[）]{style="font-family:宋体"}

[[其中，]{style="font-family:宋体"}[Op]{lang="EN-US"}]{#struct_0_x1046_x2047_1080551786}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALLOC_NEW]{lang="EN-US"}]{#struct_0_x1046_x2047_1624042354}[：生成标签数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FREE]{lang="EN-US"}]{#struct_0_x1046_x2047_x1887363814}[：释放标签数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FREE_STALE]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980731332}[：释放]{style="font-family:宋体"}[STALE]{lang="EN-US"}[标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FREE_USED]{lang="EN-US"}]{#struct_0_x1046_x2047_1928133900}[：释放在用标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIND_EXIST_LABEL]{lang="EN-US"}]{#struct_0_x1046_x2047_35426706}[：查找到对应的标签数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIND_STALE_LABEL]{lang="EN-US"}]{#struct_0_x1046_x2047_x1641794599}[：查找到对应的、存在]{style="font-family:宋体"}[STALE]{lang="EN-US"}[标记的标签数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECV_NO_EXIST_FEC_LABEL]{lang="EN-US"}]{#struct_0_x1046_x2047_14602885}[：从]{style="font-family:宋体"}[LSM]{lang="EN-US"}[收到没有记录的标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECV_EXIST_FEC_LABEL]{lang="EN-US"}]{#struct_0_x1046_x2047_x586309831}[：从]{style="font-family:宋体"}[LSM]{lang="EN-US"}[收到记录在用的标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INCREASE_CNT]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980796868}[：标签引用计数增加]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DECREASE_CNT]{lang="EN-US"}]{#struct_0_x1046_x2047_936205103}[：标签引用计数减少]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TRIGGER_ILM]{lang="EN-US"}]{#struct_0_x1046_x2047_1255073264}[：触发]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项更新]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FLUSH_LSM]{lang="EN-US"}]{#struct_0_x1046_x2047_x2144745658}[：重新向]{style="font-family:宋体"}[LSM]{lang="EN-US"}[下刷在用标签]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1046_x2047_x1335614904}

[[类型，取值包括：]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x551943641}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NH]{lang="EN-US"}]{#struct_0_x1046_x2047_x1980862404}[：表示为下一跳分配或删除标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PF]{lang="EN-US"}]{#struct_0_x1046_x2047_x2059045904}[：表示为前缀分配或删除标签]{style="font-family:宋体"}

[[Fec]{lang="EN-US"}]{#struct_0_x1046_x2047_75302388}

[[标签对应的]{style="font-family:宋体"}[FEC]{lang="EN-US"}]{#struct_0_x1046_x2047_x1114330770}[信息]{style="font-family:宋体"}

[[Nid]{lang="EN-US"}]{#struct_0_x1046_x2047_x1221085694}

[[邻居信息]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1979879364}

[[取值为]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1403143396}[0]{lang="EN-US"}[时，表示无效的邻居信息；取值为非]{style="font-family:宋体"}[0]{lang="EN-US"}[值时，表示邻居的地址]{style="font-family:宋体"}

[[Vrf]{lang="EN-US"}]{#struct_0_x1046_x2047_1989194367}

[[VPN]{lang="EN-US"}]{#struct_0_x1046_x2047_573852097}[实例索引，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时表示公网]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_x1046_x2047_805176448}

[[标签数据状态标记，目前取值只能为]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1979944900}[0x01]{lang="EN-US"}[，表示标签数据处于]{style="font-family:宋体"}[STALE]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Ref]{lang="EN-US"}]{#struct_0_x1046_x2047_163915627}

[[引用标签的路由数]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1460612042}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x516997956}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_288114583}[打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的标签分配调试信息开关，收到标签分配信息时打印相关调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp label]{lang="EN-US"}]{#struct_0_x1046_x2047_x414319708}

[\*Feb  1 02:27:22:739 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND LABEL In/Out/Op         : 1279/4294967295/ALLOC_NEW]{lang="EN-US"}

[ Type/Fec/Nid/Vrf/Flag/Ref    : NH/106.1.1.2(0)/2a000000/1/0x0/1]{lang="EN-US"}

[*[// BGP]{lang="EN-US"}*]{#struct_0_x1046_x2047_1354367609}*[为下一跳]{style="font-family:宋体"}[106.1.1.2/0]{lang="EN-US"}[分配入标签]{style="font-family:宋体"}[1279]{lang="EN-US"}[，出标签值为]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，下一跳所在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，邻居]{style="font-family:宋体"}[Nid]{lang="EN-US"}[为]{style="font-family:宋体"}[2a000000]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Feb  1 02:27:22:739 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_x1046_x2047_x1159203593}

[ SEND LABEL In/Out/Op         : 1279/4294967295/TRIGGER_ILM]{lang="EN-US"}

[ Type/Fec/Nid/Vrf/Flag/Ref    : NH/106.1.1.2(0)/2a000000/1/0x0/1 ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_x996688294}*[删除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[为下一跳]{style="font-family:宋体"}[106.1.1.2/0]{lang="EN-US"}[分配的入标签]{style="font-family:宋体"}[1279]{lang="EN-US"}[，出标签值为]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，下一跳所在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，邻居]{style="font-family:宋体"}[Nid]{lang="EN-US"}[为]{style="font-family:宋体"}[2a000000]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-33319675 .myid}
[]{#_Toc404791063}[]{#struct_0_x1046_x2047_150438294}[]{#_Toc304293044}[]{#_Toc320024994}[]{#_Toc320026629}[]{#_Toc320024995}[]{#_Toc320026630}[]{#_Toc320024996}[]{#_Toc320026631}[]{#_Toc320024997}[]{#_Toc320026632}[]{#_Toc320024998}[]{#_Toc320026633}[]{#_Toc320024999}[]{#_Toc320026634}[]{#_Toc320025000}[]{#_Toc320026635}[]{#_Toc320025001}[]{#_Toc320026636}[]{#_Toc320025002}[]{#_Toc320026637}[]{#_Toc320025003}[]{#_Toc320026638}

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp lsp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x879084838}

[**[debugging bgp lsp]{lang="EN-US"}**]{#struct_0_x1046_x2047_x2125802488}

[**[undo debugging bgp lsp]{lang="EN-US"}**]{#struct_0_x1046_x2047_85609451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1288539110}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x414385244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_511734231}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x1759507697}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_563931769}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1402061776}

[[无]{style="font-family:宋体"}]{#struct_0_x1046_x2047_41514154}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x955200082}

[**[debugging bgp lsp]{lang="EN-US"}**]{#struct_0_x1046_x2047_1798959583}[命令用来打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging bgp lsp**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x1743045094}[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging bgp lsp]{lang="EN-US"}]{#struct_0_x1046_x2047_x915832985}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2033580128}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1634462195}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x414450780}

[[LSP Type]{lang="EN-US"}]{#struct_0_x1046_x2047_x558771547}

[[LSP]{lang="EN-US"}]{#struct_0_x1046_x2047_x48202220}[类型，取值包括]{style="font-family:宋体"}[ILM]{lang="EN-US"}[、]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[、]{style="font-family:宋体"}[LOCAL_NHLFE;]{lang="EN-US"}

[[Op]{lang="EN-US"}]{#struct_0_x1046_x2047_1203133136}

[[操作类型，取值包括]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x406802641}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADD]{lang="EN-US"}]{#struct_0_x1046_x2047_x43448148}[：创建表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DELETE]{lang="EN-US"}]{#struct_0_x1046_x2047_x414516316}[：删除表项]{lang="EN-US" style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1046_x2047_x168903755}

[[FEC]{lang="EN-US"}]{#struct_0_x1046_x2047_587890551}[类型，]{style="font-family:宋体"}[PREFIX]{lang="EN-US"}[表示前缀类型的表项，]{style="font-family:宋体"}[NEXTHOP]{lang="EN-US"}[表示下一跳类型的表项，]{style="font-family:宋体"}[LOCIFNET]{lang="EN-US"}[表示]{style="font-family:宋体"}[LocalIfnet]{lang="EN-US"}[类型的表项]{style="font-family:宋体"}

[[Fec]{lang="EN-US"}]{#struct_0_x1046_x2047_x1312718642}

[[Type]{lang="EN-US"}]{#struct_0_x1046_x2047_1964108491}[取值为]{style="font-family:宋体"}[PREFIX]{lang="EN-US"}[和]{style="font-family:宋体"}[LOCIFNET]{lang="EN-US"}[时，表示前缀信息；]{style="font-family:宋体"}[Type]{lang="EN-US"}[取值为]{style="font-family:宋体"}[NEXTHOP]{lang="EN-US"}[时，表示下一跳信息]{style="font-family:宋体"}

[[Vrf]{lang="EN-US"}]{#struct_0_x1046_x2047_x162681138}

[[下一跳所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1046_x2047_x578644450}[实例索引]{style="font-family:宋体"}

[[OutLabel]{lang="EN-US"}]{#struct_0_x1046_x2047_x414581852}

[[出标签]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1021599208}

[[InLabel]{lang="EN-US"}]{#struct_0_x1046_x2047_x890090320}

[[入标签值]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1493181763}

[[InLabel/Ref/Flag]{lang="EN-US"}]{#struct_0_x1046_x2047_x629939211}

[[入标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1046_x2047_x414647388}[引用计数]{style="font-family:宋体"}[/]{lang="EN-US"}[下刷标记]{style="font-family:宋体"}

[[OutFlushNum/OutSegNum]{lang="EN-US"}]{#struct_0_x1046_x2047_1406945154}

[[出方向下刷个数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1046_x2047_x1215469105}[出方向个数]{style="font-family:宋体"}

[[LSP Op]{lang="EN-US"}]{#struct_0_x1046_x2047_x286173650}

[[下刷]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1046_x2047_1081135049}[表项操作类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FLUSH_LSM]{lang="EN-US"}]{#struct_0_x1046_x2047_x749486498}[：下刷]{lang="EN-US" style="font-family:宋体"}[LSM]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EXIST_NHLFE_NOT_FLUSH]{lang="EN-US"}]{#struct_0_x1046_x2047_x414712924}[：存在]{lang="EN-US" style="font-family:
  宋体"}[NHLFE]{lang="EN-US"}[表项，不需要下刷]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO_LSP_TO_DELETE]{lang="EN-US"}]{#struct_0_x1046_x2047_653322636}[：不存在需要删除的]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BEFORE_RECV_TUNNEL_CHG]{lang="EN-US"}]{#struct_0_x1046_x2047_1445072419}[：隧道变化前结果]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AFTER_RECV_TUNNEL_CHG]{lang="EN-US"}]{#struct_0_x1046_x2047_x472294753}[：隧道变化后结果]{lang="EN-US" style="font-family:
  宋体"}

[[OutSeg Info No.]{lang="EN-US"}]{#struct_0_x1046_x2047_x414778460}

[[出方向信息]{style="font-family:宋体"}]{#struct_0_x1046_x2047_2131785622}

[[Nexthop/vrf/OutLabel]{lang="EN-US"}]{#struct_0_x1046_x2047_x108871306}

[[出方向相关信息：下一跳信息]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1046_x2047_1025336961}[下一跳所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例索引]{style="font-family:宋体"}[/]{lang="EN-US"}[出标签]{style="font-family:宋体"}

[[ifIndex/Nid]{lang="EN-US"}]{#struct_0_x1046_x2047_x250328373}

[[出接口索引]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1046_x2047_x413795420}[出方向隧道的]{style="font-family:宋体"}[NID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1866870931}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_711217861}[基本]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[组网环境下，在]{style="font-family:宋体"}[PE 1]{lang="EN-US"}[上打开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的调试信息开关。在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[上引入静态路由时，打印相关调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp lsp]{lang="EN-US"}]{#struct_0_x1046_x2047_780767321}

[\*Jan 31 10:11:29:123 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ SEND LSP Type/Op             : ILM/ADD]{lang="EN-US"}

[ Type/Fec/Vrf/OutLabel        : NEXTHOP/106.1.1.2(0)/1/4294967295]{lang="EN-US"}

[ InLabel                      : 1279]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1581542238}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[（]{style="font-family:宋体"}[106.1.1.2/0]{lang="EN-US"}[）分配标签]{style="font-family:宋体"}[1279]{lang="EN-US"}[，并创建]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 31 10:11:29:123 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_x1046_x2047_x1577498367}

[ SEND LSP Op                  : FLUSH_LSM]{lang="EN-US"}

[ Type/Fec/Vrf/OutLabel        : NEXTHOP/106.1.1.2(0)/1/4294967295]{lang="EN-US"}

[ InLabel/Ref/Flag             : 1279/0/0x1]{lang="EN-US"}

[ OutFlushNum/OutSegNum        : 0/0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_771580521}*[下刷]{style="font-family:宋体"}[LSM]{lang="EN-US"}*

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::: {#-634842609 .myid}
[]{#_Toc404791066}[]{#struct_0_x1046_x2047_1665082475}

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN调试命令 \-- debugging bgp update vpnv6**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1402486024}

[**[debugging bgp update]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **vpnv6** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_575802526}

[**[undo debugging bgp update]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **vpnv6** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_x192033533}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1050789745}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1004251919}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_512127447}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_941510827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x1054546313}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1985338064}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_193313138}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1668326453}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1046_x2047_664051801}[：表示接收的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1046_x2047_x1183069596}[：表示发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_702968426}

[**[debugging bgp update vpnv6]{lang="EN-US"}**]{#struct_0_x1046_x2047_x606058810}[命令用来打开]{style="font-family:
宋体"}[BGP VPNv6]{lang="EN-US"}[的]{style="font-family:
宋体"}[Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging bgp vpnv6**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}]{#struct_0_x1046_x2047_x1336830634}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表2-1 ]{lang="EN-US"}[debugging bgp update vpnv6]{lang="EN-US"}]{#struct_0_x1046_x2047_x414385243}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2038353664}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_199176209}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1076531441}

[[BGP_6VPE.: Recv UPDATE from peer *ip-address* with following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_x723468898}

[[从对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1606900168}[接收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[BGP_6VPE.: Send UPDATE to peer *ip-address* for following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_1354114590}

[[向对等体]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_1148277375}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Update message length]{lang="EN-US"}]{#struct_0_x1046_x2047_x414450779}

[[Update]{lang="EN-US"}]{#struct_0_x1046_x2047_x559230302}[消息的长度，单位为字节]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_x74452506}

[[路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_x816729245}[属性，即路由信息的来源，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[IGP]{lang="IT"}]{#struct_0_x1046_x2047_62849785}[：网络层可达信息来源于]{style="font-family:宋体"}[AS]{lang="IT"}[内部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[EGP]{lang="IT"}]{#struct_0_x1046_x2047_589611519}[：网络层可达信息通过]{style="font-family:宋体"}[EGP]{lang="IT"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incomplete]{lang="IT"}]{#struct_0_x1046_x2047_x2037734044}[：网络层可达信息通过其他方式学习]{lang="EN-US" style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_x1046_x2047_x414516315}

[[路由的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}]{#struct_0_x1046_x2047_x168969291}[属性，即路由从本地到目的地址所要经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_x1046_x2047_1785262453}

[[路由的下一跳属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x2022076798}

[[Local pref]{lang="EN-US"}]{#struct_0_x1046_x2047_x2024785981}

[[路由的本地优先级]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x414581851}

[[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_1021664744}

[[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_x808623826}[（]{style="font-family:宋体"}[Multi-Exit Discriminator]{lang="EN-US"}[，多出口区分）值]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_x1046_x2047_147946759}

[[路由的扩展团体属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x531137647}

[*[prefix/prefix-length ]{lang="EN-US"}*[(RD *route-distinguisher*, Label *label*)]{lang="EN-US"}]{#struct_0_x1046_x2047_x414647387}

[[路由前缀为]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*]{#struct_0_x1046_x2047_1407534978}[、路由前缀的前缀长度为]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[、]{style="font-family:宋体"}[RD]{lang="EN-US"}[值为]{style="font-family:宋体"}*[route-distinguisher]{lang="EN-US"}*[、标签值为]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[[Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*]{lang="EN-US"}]{#struct_0_x1046_x2047_x2028079698}

[[向地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1355335442}[的对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，下一跳地址为]{style="font-family:宋体"}*[next-hop]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x854298647}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_1987024571}[打开对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文调试信息开关。从对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[接收、向对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文时打印相关调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update 3.3.3.9 vpnv6]{lang="EN-US"}]{#struct_0_x1046_x2047_x414712923}

[\*May 14 14:00:49:845 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP_6VPE.: Recv UPDATE from peer 3.3.3.9 with following destinations:]{lang="EN-US"}

[         Update message length : 112]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      :]{lang="EN-US"}

[         Next hop     : ::FFFF:3.3.3.9]{lang="EN-US"}

[         Local pref   : 100]{lang="EN-US"}

[         MED          : 0]{lang="EN-US"}

[         Ext-Community: \<RT: 111:1\>]{lang="EN-US"}

[         2001:3::/96 (RD 200:1, Label 1279)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_653257100}*[从对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，消息长度为]{style="font-family:宋体"}[112]{lang="EN-US"}[字节，路由信息通过]{style="font-family:宋体"}[IGP]{lang="EN-US"}[、]{style="font-family:宋体"}[EGP]{lang="EN-US"}[之外的其他方式学习，下一跳为]{style="font-family:宋体"}[::FFFF:3.3.3.9]{lang="EN-US"}[，本地优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[MED]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[为]{style="font-family:宋体"}[111:1]{lang="EN-US"}[，路由前缀为]{style="font-family:宋体"}[2001:3::/96]{lang="EN-US"}[，]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[200:1]{lang="EN-US"}[，标签值为]{style="font-family:宋体"}[1279]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*May 14 14:00:49:860 2012 Sysname BGP/7/DEBUG: -MDC=1; ]{lang="EN-US"}]{#struct_0_x1046_x2047_1822458421}

[ BGP.: Send UPDATE MSG to peer 3.3.3.9(IPv6-VPN) NextHop: ::FFFF:3.3.3.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_x475211722}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[发送]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[路由更新，下一跳地址为]{style="font-family:宋体"}[::FFFF:3.3.3.1]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-808006078 .myid}
[]{#_Toc404791067}[]{#struct_0_x1046_x2047_1318161728}

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN调试命令 \-- debugging bgp update vpn-instance ipv6**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_273977449}

[**[debugging bgp update]{lang="EN-US"}**[ **vpn-instance** *vpn-instance-name* *ipv6-address* \[ *prefix-length* \] **ipv6** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_x1084934649}

[**[undo debugging bgp update]{lang="EN-US"}***[ ]{lang="EN-US"}***[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}***[ ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[ \[ *prefix-length* \] **ipv6** \[ **receive** \| **send** \]]{lang="EN-US"}]{#struct_0_x1046_x2047_914609873}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x414778459}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_2131326869}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1054742921}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_534620092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_146879250}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_372908079}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1987171482}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1668719664}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1046_x2047_1367481850}[：]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1046_x2047_x211630114}[：表示接收的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1046_x2047_x936848674}[：表示发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x413795419}

[**[debugging bgp update vpn-instance ipv6]{lang="EN-US"}**]{#struct_0_x1046_x2047_1867460754}[命令用来打开指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP IPv6 Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging bgp update vpn-instance ipv6**]{lang="EN-US"}[命令用来关闭指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP IPv6 Update]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1046_x2047_1488540483}[实例的]{style="font-family:宋体"}[BGP IPv6 Update]{lang="EN-US"}[报文调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表2-2 ]{lang="EN-US"}[debugging bgp update vpn-instance ipv6]{lang="EN-US"}]{#struct_0_x1046_x2047_x1926465833}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2041544320}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_894042247}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1550545856}

[[BGP.IPV6_vpn1: Recv UPDATE from peer *ipv6-address* with following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_1713495393}

[[从对等体]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1941216646}[接收到]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[BGP.: Send UPDATE to peer *ipv6-address* for following destinations]{lang="EN-US"}]{#struct_0_x1046_x2047_x413860955}

[[向对等体]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1046_x2047_1956303644}[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Update message length]{lang="EN-US"}]{#struct_0_x1046_x2047_x1461532833}

[[Update]{lang="EN-US"}]{#struct_0_x1046_x2047_x1518025873}[消息的长度]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_x1102376191}

[[路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_480600235}[属性，即路由信息的来源，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[IGP]{lang="IT"}]{#struct_0_x1046_x2047_x414319710}[：网络层可达信息来源于]{style="font-family:宋体"}[AS]{lang="IT"}[内部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[EGP]{lang="IT"}]{#struct_0_x1046_x2047_1354891898}[：网络层可达信息通过]{style="font-family:宋体"}[EGP]{lang="IT"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incomplete]{lang="IT"}]{#struct_0_x1046_x2047_391556981}[：网络层可达信息通过其他方式学习]{lang="EN-US" style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_x1046_x2047_x1539429050}

[[路由的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}]{#struct_0_x1046_x2047_74233097}[属性，即路由从本地到目的地址所要经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_x1046_x2047_941702351}

[[路由的下一跳属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x414385246}

[[Local pref]{lang="EN-US"}]{#struct_0_x1046_x2047_198979601}

[[路由的本地优先级]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1365991496}

[[MED ]{lang="EN-US"}]{#struct_0_x1046_x2047_x1248737463}

[[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_x1329432609}[属性]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_x1046_x2047_x1432761461}

[[路由的扩展团体属性]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x414450782}

[*[prefix]{lang="EN-US"}*[/]{lang="EN-US"}*[prefix-length]{lang="EN-US"}*]{#struct_0_x1046_x2047_x558640475}

[[路由前缀为]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*]{#struct_0_x1046_x2047_344322765}[、路由前缀的前缀长度为]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*

[[Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*]{lang="EN-US"}]{#struct_0_x1046_x2047_x728435706}

[[向地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_1520280454}[的对等体]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，下一跳地址为]{style="font-family:宋体"}*[next-hop]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x414516318}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_x169821259}[打开]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[中对等体]{style="font-family:宋体"}[19::1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6 Update]{lang="EN-US"}[报文调试信息开关。从]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内的对等体]{style="font-family:宋体"}[19::1]{lang="EN-US"}[接收、向其发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[报文时打印相关调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update vpn-instance vpn1 19::1 ipv6]{lang="EN-US"}]{#struct_0_x1046_x2047_x596666786}

[\*Sep 26 17:55:17:419 2011 H3C BGP/7/DEBUG: -MDC=1;                               ]{lang="EN-US"}

[         BGP_IPV6.vpn1: Recv UPDATE from peer 19::1 with following destinations:]{lang="EN-US"}

[         Update message length : 77                                             ]{lang="EN-US"}

[         Origin       : Incomplete                                              ]{lang="EN-US"}

[         AS path      : 200                                                     ]{lang="EN-US"}

[         Next hop     : 19::1                                                   ]{lang="EN-US"}

[         MED          : 0                                                       ]{lang="EN-US"}

[         19::/64,  ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_x307818588}*[在]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内收到对等体]{style="font-family:宋体"}[19::1]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP IPv6 Update]{lang="EN-US"}[报文，路由信息通过]{style="font-family:宋体"}[IGP]{lang="EN-US"}[、]{style="font-family:宋体"}[EGP]{lang="EN-US"}[之外的其他方式学习，]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径为]{style="font-family:宋体"}[200]{lang="EN-US"}[，下一跳为]{style="font-family:宋体"}[19::1]{lang="EN-US"}[，]{style="font-family:宋体"}[MED]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，路由前缀为]{style="font-family:宋体"}[19::/64]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Sep 26 17:55:17:520 2011 Sysname BGP/7/DEBUG: -MDC=1; ]{lang="EN-US"}]{#struct_0_x1046_x2047_x2063558970}

[ BGP.vpn1: Send UPDATE MSG to peer 19::1(IPv6-UNC) NextHop: 19::2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_2064540029}*[向]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内对等体]{style="font-family:宋体"}[19::1]{lang="EN-US"}[发送路由更新，下一跳地址为]{style="font-family:宋体"}[19::2]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#1444393600 .myid}
[]{#_Toc404791068}[]{#struct_0_x1046_x2047_x414581854}[]{#_Toc333326115}

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN调试命令 \-- debugging bgp update-group vpnv6**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1021468136}

[**[debugging bgp update-group vpnv6]{lang="EN-US"}**]{#struct_0_x1046_x2047_x2039293899}

[**[undo debugging bgp update-group vpnv6]{lang="EN-US"}**]{#struct_0_x1046_x2047_97770838}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1040882381}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x333948512}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1054546314}

[[network-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_x1054480778}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1046_x2047_1449438771}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_2062319801}

[[无]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x414647390}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_1407469441}

[**[debugging bgp update-group vpnv6]{lang="EN-US"}**]{#struct_0_x1046_x2047_x1213842219}[命令用来打开]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[地址族的打包组调试信息开关。]{style="font-family:宋体"}**[undo debugging bgp update-group vpnv6]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[地址族的打包组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}]{#struct_0_x1046_x2047_1196604731}[地址族的打包组调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[打开调试信息开关会影响系统的性能，因此，请不要轻易打开调试信息开关，调试完毕后，请及时关闭调试信息开关。]{style="font-family:宋体"}]{#struct_0_x1046_x2047_1127688916}

[[表2-3 ]{lang="EN-US"}[debugging bgp update-group vpnv6]{lang="EN-US"}]{#struct_0_x1046_x2047_79550581}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2040507904}[[字段]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x862930586}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1046_x2047_946938289}

[[Send UPDATE to update-group *group-id*]{lang="EN-US"}]{#struct_0_x1046_x2047_x414712926}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_653453708}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送路由更新]{style="font-family:宋体"}

[[Send UPDATE(Withdraw) to update-group *group-id*]{lang="EN-US"}]{#struct_0_x1046_x2047_918788343}

[[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x127655576}[打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送路由撤销]{style="font-family:宋体"}

[*[destination-address]{lang="EN-US"}*[/*mask-length*]{lang="EN-US"}]{#struct_0_x1046_x2047_2129568714}

[[发布的路由前缀的目的地址和掩码]{style="font-family:宋体"}]{#struct_0_x1046_x2047_x1220948903}

[[Update message length]{lang="EN-US"}]{#struct_0_x1046_x2047_1154428575}

[[Update]{lang="EN-US"}]{#struct_0_x1046_x2047_x414778462}[消息长度]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x1046_x2047_2131654550}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x98552203}[的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[AS path]{lang="EN-US"}]{#struct_0_x1046_x2047_x1836295276}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_1180435260}[的]{style="font-family:宋体"}[AS Path]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_x1046_x2047_x2120827405}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x413795422}[的]{style="font-family:宋体"}[Next Hop]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Local pref]{lang="EN-US"}]{#struct_0_x1046_x2047_1867002003}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_1852980482}[的]{style="font-family:宋体"}[Local Pref]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_x1046_x2047_209593330}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x1221006062}[的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Community]{lang="EN-US"}]{#struct_0_x1046_x2047_x413860958}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_1955582748}[的团体属性]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_x1046_x2047_x538559692}

[[BGP]{lang="EN-US"}]{#struct_0_x1046_x2047_x2134895945}[的扩展团体属性]{style="font-family:宋体"}

[[update-group *group-id* *address-family* created]{lang="EN-US"}]{#struct_0_x1046_x2047_799850187}

[[创建地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_x414319709}[的打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*

[[update-group *group-id* *address-family* deleted]{lang="EN-US"}]{#struct_0_x1046_x2047_1354433145}

[[删除地址族]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*]{#struct_0_x1046_x2047_x1187133768}[的打包组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1046_x2047_x1835115785}

[[\# ]{lang="EN-US"}]{#struct_0_x1046_x2047_x363290487}[打开]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[打包组调试信息开关，发布]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[路由时，设备上将打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bgp update-group vpnv6]{lang="EN-US"}]{#struct_0_x1046_x2047_x414385245}

[\*Apr 16 21:06:16:48 2012 Sysname BGP/7/DEBUG: -MDC=1;]{lang="EN-US"}

[         BGP_6VPE.: Send UPDATE to update-group 0 for following destinations:]{lang="EN-US"}

[         Origin       : Incomplete]{lang="EN-US"}

[         AS path      : 100]{lang="EN-US"}

[         Next hop     : 100::1]{lang="EN-US"}

[         Ext-Community: \<RT: 1:2\>]{lang="EN-US"}

[         2::/64 (RD 1:2, Label 1000120)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1046_x2047_199045137}*[向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组]{style="font-family:宋体"}[0]{lang="EN-US"}[发送路由更新，路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性为]{style="font-family:宋体"}[Incomplete]{lang="EN-US"}[，]{style="font-family:宋体"}[AS path]{lang="EN-US"}[属性为]{style="font-family:宋体"}[100]{lang="EN-US"}[，下一跳地址为]{style="font-family:宋体"}[100::1]{lang="EN-US"}[，路由的扩展团体属性]{style="font-family:宋体"}[RT]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，发布的路由前缀为]{style="font-family:宋体"}[2::/64]{lang="EN-US"}[，]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[1:2]{lang="EN-US"}[，通告的标签为]{style="font-family:宋体"}[1000120]{lang="EN-US"}[。]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[ ]{lang="EN-US"}
