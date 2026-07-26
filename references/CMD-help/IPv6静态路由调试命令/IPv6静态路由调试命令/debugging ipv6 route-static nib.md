::: {#1663666384 .myid}
[]{#_Toc340320660}[]{#_Toc404788710}[]{#struct_0_50192_x1172_250178044}[]{#_Toc340320661}

**IPv6静态路由调试命令 \-- IPv6静态路由调试命令 \-- debugging ipv6 route-static nib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_50192_x1172_x1041819827}

[**[debugging ipv6 route-static nib]{lang="EN-US"}**[ \[ *nib-id* \]]{lang="EN-US"}]{#struct_0_50192_x1172_x1313372740}

[**[undo debugging ipv6 route-static nib]{lang="EN-US"}**]{#struct_0_50192_x1172_2079507545}

[[【视图】]{style="font-family:黑体"}]{#struct_0_50192_x1172_x246648908}

[[用户视图]{style="font-family:宋体"}]{#struct_0_50192_x1172_93715365}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_50192_x1172_667279825}

[[network-admin]{lang="EN-US"}]{#struct_0_50192_x1172_x241077857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_50192_x1172_1531365726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_50192_x1172_1592249908}

[*[nib-id]{lang="EN-US"}*]{#struct_0_50192_x1172_817577851}[：下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}[，十六进制，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_50192_x1172_x918509132}

[**[debugging ipv6 route-static nib]{lang="EN-US"}**]{#struct_0_50192_x1172_x1883503942}[命令用来打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播静态路由下一跳信息的调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 route-static nib ]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[单播静态路由下一跳信息的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_50192_x1172_x1727527399}[单播静态路由下一跳信息的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ipv6 route-static nib]{lang="EN-US"}]{#struct_0_50192_x1172_x23809233}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1170779611}[[字段]{style="font-family:黑体"}]{#struct_0_50192_x1172_93256610}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_50192_x1172_x1487300188}

[[Add/Delete/Modify NIB]{lang="EN-US"}]{#struct_0_50192_x1172_1103894347}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_50192_x1172_x122161838}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[修改]{style="font-family:宋体"}[NIB]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}

[[Seq]{lang="EN-US"}]{#struct_0_50192_x1172_424899951}

[[序号]{style="font-family:宋体"}]{#struct_0_50192_x1172_494421756}

[[errno]{lang="EN-US"}]{#struct_0_50192_x1172_2055923732}

[[错误码]{style="font-family:宋体"}]{#struct_0_50192_x1172_93191074}

[[PrefixIndex]{lang="EN-US"}]{#struct_0_50192_x1172_200043244}

[[前缀编号]{style="font-family:宋体"}]{#struct_0_50192_x1172_1816735411}

[[Vrf]{lang="EN-US"}]{#struct_0_50192_x1172_x1874173290}

[[实例名]{style="font-family:宋体"}]{#struct_0_50192_x1172_1551953833}

[[OrigNexthop]{lang="EN-US"}]{#struct_0_50192_x1172_x641087975}

[[原始下一跳]{style="font-family:宋体"}]{#struct_0_50192_x1172_93125538}

[[RealNexthop]{lang="EN-US"}]{#struct_0_50192_x1172_x512714628}

[[真实下一跳]{style="font-family:宋体"}]{#struct_0_50192_x1172_x1826511575}

[[Interface]{lang="EN-US"}]{#struct_0_50192_x1172_x206266134}

[[出接口名]{style="font-family:宋体"}]{#struct_0_50192_x1172_x682960397}

[[Localaddr]{lang="EN-US"}]{#struct_0_50192_x1172_287393109}

[[本地接口地址]{style="font-family:宋体"}]{#struct_0_50192_x1172_93060002}

[[RelyDepth]{lang="EN-US"}]{#struct_0_50192_x1172_227087637}

[[迭代深度]{style="font-family:宋体"}]{#struct_0_50192_x1172_913236775}

[[Msgtype]{lang="EN-US"}]{#struct_0_50192_x1172_x1408641678}

[[消息类型]{style="font-family:宋体"}]{#struct_0_50192_x1172_x1051442835}

[[TunnelCnt]{lang="EN-US"}]{#struct_0_50192_x1172_93518754}

[[隧道个数]{style="font-family:宋体"}]{#struct_0_50192_x1172_x959393987}

[[TunnelID]{lang="EN-US"}]{#struct_0_50192_x1172_x2016373665}

[[隧道号]{style="font-family:宋体"}]{#struct_0_50192_x1172_x1452333937}

[[Topology]{lang="EN-US"}]{#struct_0_50192_x1172_x1293160090}

[[拓扑名称，目前]{style="font-size:10.0pt;
  font-family:宋体"}]{#struct_0_50192_x1172_x1727685390}[IPv6]{lang="EN-US" style="font-size:10.0pt"}[不支持子拓扑，显示为空]{style="font-size:10.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_50192_x1172_809801147}

[[\# ]{lang="EN-US"}]{#struct_0_50192_x1172_1219624350}[打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播静态路由邻居的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 route-static nib]{lang="EN-US"}]{#struct_0_50192_x1172_93453218}

[\*Sep 20 10:51:41:770 2012 Sysname NIB/7/DEBUG: -MDC=1; USR add NIB 0041/0/0/0/0]{lang="EN-US"}

[/3::3, id 21000002 seq 5, errno 0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_995731871}*[添加]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 20 10:51:41:822 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_x1061558251}

[ USR sync NIB 21000002 to RIB, msgtype ADD, bytes 104]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_x735712075}*[将]{style="font-family:宋体"}[NIB]{lang="EN-US"}[添加消息同步到]{style="font-family:宋体"}[RIB]{lang="EN-US"}*

[[\*Sep 20 10:51:41:924 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_x1980576788}

[ USR sync NIB 21000002 to RIB, msgtype MOD, bytes 192]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 3::3]{lang="EN-US"}

[  RelyDepth: 1              RealNexthop: 1:1::2]{lang="EN-US"}

[  Interface: GE1/0/2          LocalAddr: 1:1::3]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_x1191288494}*[将]{style="font-family:宋体"}[NIB]{lang="EN-US"}[修改消息同步到]{style="font-family:宋体"}[RIB]{lang="EN-US"}*

[[\*Sep 20 10:51:41:975 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_93387682}

[ USR re-rely route under NIB 21000002]{lang="EN-US"}

[*[// NIB]{lang="EN-US"}*]{#struct_0_50192_x1172_1438493469}*[进行重新迭代]{style="font-family:宋体"}*

[[\*Sep 20 10:51:42:127 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_x757364432}

[ USR modify NIB 21000001 with nexthop 2::2:]{lang="EN-US"}

[ Old value:]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2::2]{lang="EN-US"}

[  RelyDepth: 1              RealNexthop: ::]{lang="EN-US"}

[  Interface: NULLL0           LocalAddr: ::]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[ New value:]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2::2]{lang="EN-US"}

[  RelyDepth: 2              RealNexthop: 1:1::2]{lang="EN-US"}

[  Interface: GE1/0/2          LocalAddr: 1:1::3]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_x1966465064}*[修改]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 20 10:51:52:670 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_93780898}

[ USR modify NIB 21000001 with nexthop 2::2:]{lang="EN-US"}

[ Old value:]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2::2]{lang="EN-US"}

[  RelyDepth: 2              RealNexthop: 1:1::2]{lang="EN-US"}

[  Interface: GE1/0/2          LocalAddr: 1:1::3]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[ New value:]{lang="EN-US"}

[ 2 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2::2]{lang="EN-US"}

[  RelyDepth: 2              RealNexthop: 1:1::2]{lang="EN-US"}

[  Interface: GE1/0/2          LocalAddr: 1:1::3]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[ ]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2::2]{lang="EN-US"}

[  RelyDepth: 1              RealNexthop: ::]{lang="EN-US"}

[  Interface: NULLL0           LocalAddr: ::]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Sep 20 10:51:52:721 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ USR sync NIB 21000001 to RIB, msgtype MOD, bytes 400]{lang="EN-US"}

[ 2 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2::2]{lang="EN-US"}

[  RelyDepth: 2              RealNexthop: 1:1::2]{lang="EN-US"}

[  Interface: GE1/0/2          LocalAddr: 1:1::3]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[ ]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2::2]{lang="EN-US"}

[  RelyDepth: 1              RealNexthop: ::]{lang="EN-US"}

[  Interface: NULLL0           LocalAddr: ::]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_x656470849}*[修改]{style="font-family:宋体"}[NIB]{lang="EN-US"}[的内容]{style="font-family:宋体"}*

[[\*Sep 20 10:52:00:745 2012 Sysname NIB/7/DEBUG: -MDC=1; USR delete NIB 21000002]{lang="EN-US"}]{#struct_0_50192_x1172_x949882228}

[with seq 5]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_597305502}*[删除指定]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 20 10:52:00:796 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_838042070}

[ USR sync NIB 21000002 to RIB, msgtype DEL, bytes 36]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_x1454534505}*[同步删除消息到]{style="font-family:宋体"}[RIB]{lang="EN-US"}*

::: {#-2104462130 .myid}
[]{#_Toc404788711}[]{#struct_0_50192_x1172_x767447757}

**IPv6静态路由调试命令 \-- IPv6静态路由调试命令 \-- debugging ipv6 route-static process**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_50192_x1172_x2014621307}

[**[debugging ipv6 route-static process]{lang="EN-US"}**]{#struct_0_50192_x1172_x1365703879}

[**[undo debugging ipv6 route-static process]{lang="EN-US"}**]{#struct_0_50192_x1172_93715362}

[[【视图】]{style="font-family:黑体"}]{#struct_0_50192_x1172_x142024239}

[[用户视图]{style="font-family:宋体"}]{#struct_0_50192_x1172_1303461375}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_50192_x1172_166369278}

[[network-admin]{lang="EN-US"}]{#struct_0_50192_x1172_x1580647225}

[[mdc-admin]{lang="EN-US"}]{#struct_0_50192_x1172_x1118026245}

[[【参数】]{style="font-family:黑体"}]{#struct_0_50192_x1172_756169197}

[[无]{style="font-family:宋体"}]{#struct_0_50192_x1172_2029563321}

[[【描述】]{style="font-family:黑体"}]{#struct_0_50192_x1172_x1014987439}

[**[debugging ipv6 route-static process]{lang="EN-US"}**]{#struct_0_50192_x1172_180077820}[命令用来打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播静态路由的调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 route-static process]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播静态路由的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_50192_x1172_93256611}[单播静态路由的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging ipv6 route-static process]{lang="EN-US"}]{#struct_0_50192_x1172_469014948}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1141550069}[[字段]{style="font-family:黑体"}]{#struct_0_50192_x1172_x959764003}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_50192_x1172_335224896}

[[Add/Delete/Modify route]{lang="EN-US"}]{#struct_0_50192_x1172_1280164131}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_50192_x1172_x2064037442}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[修改路由]{style="font-family:宋体"}

[[NibID]{lang="EN-US"}]{#struct_0_50192_x1172_2077236013}

[[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_50192_x1172_93191075}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_50192_x1172_x2138608916}

[[\# ]{lang="EN-US"}]{#struct_0_50192_x1172_1989667863}[打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播静态路由的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 route-static process]{lang="EN-US"}]{#struct_0_50192_x1172_1306842363}

[%May  9 10:52:33:645 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ Add static route 1::/96]{lang="EN-US"}

[%May  9 11:13:24:652 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ USR: Add route 3::3/128 with NibID 0x21000000 to RIB]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_1472412082}*[添加目的地址为]{style="font-family:宋体"}[1::/96]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由]{style="font-family:宋体"}*

[[%May  9 10:52:50:764 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_1054744001}

[ Add static route 1::/96]{lang="EN-US"}

[%May  9 10:52:50:764 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ USR: Modify route 1::/96 with NibID 0x21000000]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_x1604890044}*[修改目的地址为]{style="font-family:宋体"}[1::/96]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由]{style="font-family:宋体"}*

[[%May  9 10:53:25:398 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_50192_x1172_93125539}

[ USR: Delete route 1::/96 with NibID 0x21000000]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_50192_x1172_1825937532}*[删除目的地址为]{style="font-family:宋体"}[1::/96]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由]{style="font-family:宋体"}*
