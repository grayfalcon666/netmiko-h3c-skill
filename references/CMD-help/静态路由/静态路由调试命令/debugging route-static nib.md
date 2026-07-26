::: {#1520867867 .myid}
[]{#_Toc340320660}[]{#_Toc343536561}[]{#_Toc340320655}[]{#_Ref335832846}[]{#_Ref335832845}[]{#_Ref335832841}[]{#_Toc404787493}[]{#struct_0_19345_x2375_x1951444283}[]{#_Toc343536562}[]{#_Toc340320656}

**静态路由 \-- 静态路由调试命令 \-- debugging route-static nib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_19345_x2375_x735197017}

[**[debugging route-static nib]{lang="EN-US"}**[ \[ *nib-id* \]]{lang="EN-US"}]{#struct_0_19345_x2375_1572045885}

[**[undo debugging route-static nib]{lang="EN-US"}**]{#struct_0_19345_x2375_2055377615}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19345_x2375_722921391}

[[用户视图]{style="font-family:宋体"}]{#struct_0_19345_x2375_1341416}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19345_x2375_x1126755052}

[[network-admin]{lang="EN-US"}]{#struct_0_19345_x2375_x368259241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19345_x2375_1649012833}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19345_x2375_1011571362}

[*[nib-id]{lang="EN-US"}*]{#struct_0_19345_x2375_1137151969}[：下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}[，十六进制，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_19345_x2375_x1698979741}

[**[debugging route-static nib]{lang="EN-US"}**]{#struct_0_19345_x2375_x1251603698}[命令用来打开]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[单播静态路由下一跳信息的调试信息开关。]{style="font-family:宋体"}**[undo debugging route-static nib]{lang="EN-US"}**[用来关闭]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[单播静态路由下一跳信息的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_19345_x2375_1722252419}[单播静态路由下一跳信息的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging route-static nib]{lang="EN-US"}]{#struct_0_19345_x2375_x813359784}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x235698997}[[字段]{style="font-family:黑体"}]{#struct_0_19345_x2375_x2025258367}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_19345_x2375_x1126820588}

[[Add/Delete/Modify NIB]{lang="EN-US"}]{#struct_0_19345_x2375_568671317}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19345_x2375_1992684154}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[修改下一跳信息]{style="font-family:宋体"}

[[Seq]{lang="EN-US"}]{#struct_0_19345_x2375_x41932078}

[[序号]{style="font-family:宋体"}]{#struct_0_19345_x2375_x70004156}

[[Errno]{lang="EN-US"}]{#struct_0_19345_x2375_x1187355370}

[[错误码]{style="font-family:宋体"}]{#struct_0_19345_x2375_1528423941}

[[PrefixIndex]{lang="EN-US"}]{#struct_0_19345_x2375_1251730650}

[[前缀编号]{style="font-family:宋体"}]{#struct_0_19345_x2375_455091381}

[[Vrf]{lang="EN-US"}]{#struct_0_19345_x2375_x1432768268}

[[实例名]{style="font-family:宋体"}]{#struct_0_19345_x2375_777924689}

[[OrigNexthop]{lang="EN-US"}]{#struct_0_19345_x2375_x2125015319}

[[原始下一跳]{style="font-family:宋体"}]{#struct_0_19345_x2375_1033893392}

[[RealNexthop]{lang="EN-US"}]{#struct_0_19345_x2375_1251796186}

[[真实下一跳]{style="font-family:宋体"}]{#struct_0_19345_x2375_x716150522}

[[Interface]{lang="EN-US"}]{#struct_0_19345_x2375_x280833509}

[[出接口名]{style="font-family:宋体"}]{#struct_0_19345_x2375_712954067}

[[Localaddr]{lang="EN-US"}]{#struct_0_19345_x2375_753736126}

[[本地接口地址]{style="font-family:宋体"}]{#struct_0_19345_x2375_1251861722}

[[RelyDepth]{lang="EN-US"}]{#struct_0_19345_x2375_x324227216}

[[迭代深度]{style="font-family:宋体"}]{#struct_0_19345_x2375_534285338}

[[Msgtype]{lang="EN-US"}]{#struct_0_19345_x2375_x1199391545}

[[消息类型]{style="font-family:宋体"}]{#struct_0_19345_x2375_39108390}

[[TunnelCnt]{lang="EN-US"}]{#struct_0_19345_x2375_1251927258}

[[隧道个数]{style="font-family:宋体"}]{#struct_0_19345_x2375_x701041742}

[[TunnelID]{lang="EN-US"}]{#struct_0_19345_x2375_x400071404}

[[隧道号]{style="font-family:宋体"}]{#struct_0_19345_x2375_1135830297}

[[Topology]{lang="EN-US"}]{#struct_0_19345_x2375_x1469698616}

[[拓扑名称，]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_19345_x2375_x276105886}[base]{lang="EN-US" style="font-size:10.0pt"}[为公网拓扑（目前]{style="font-size:10.0pt;font-family:
  宋体"}[IPv6]{lang="EN-US" style="font-size:10.0pt"}[不支持子拓扑，显示为空）]{style="font-size:10.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_19345_x2375_1966347290}[]{#表NBR_3}[【举例】]{style="font-family:黑体"}

[[\# ]{lang="EN-US"}]{#struct_0_19345_x2375_1994687525}[打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播静态路由下一跳信息的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging route-static nib]{lang="EN-US"}]{#struct_0_19345_x2375_1251992794}

[\*Aug 23 15:44:45:833 2012 Sysname NIB/7/DEBUG: -MDC=1; USR delete NIB 11000000 w]{lang="EN-US"}

[ith seq 2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_1227242173}*[删除]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 19 09:16:18:606 2012 Sysname NIB/7/DEBUG: -MDC=1; USR add NIB 0001/0/2]{lang="EN-US"}]{#struct_0_19345_x2375_x567599783}

[/0/2/1.2.3.4, id 11000004 seq 4, errno 0]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 1.2.3.4]{lang="EN-US"}

[  RelyDepth: 0              RealNexthop: 1.2.3.4]{lang="EN-US"}

[  Interface: GE1/0/2           LocalAddr: 11.1.1.2]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_x1434849041}*[添加基础]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 19 09:16:18:657 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_19345_x2375_1833379704}

[ USR sync NIB 11000004 to RIB, msgtype ADD, bytes 200]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 1.2.3.4]{lang="EN-US"}

[  RelyDepth: 0              RealNexthop: 1.2.3.4]{lang="EN-US"}

[  Interface: GE1/0/2           LocalAddr: 11.1.1.2]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_1252058330}*[同步基础]{style="font-family:宋体"}[NIB]{lang="EN-US"}[给]{style="font-family:宋体"}[RIB]{lang="EN-US"}*

[[\*Sep 19 09:16:18:708 2012 Sysname NIB/7/DEBUG: -MDC=1; USR add NIB 1000\[11000004]{lang="EN-US"}]{#struct_0_19345_x2375_x909522454}

[/4/2/1/0\]\[11000001/1/2/1/0\], id 11000005 seq 5, errno 0]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[       PrefixIndex: 0]{lang="EN-US"}

[               Vrf: default-vrf]{lang="EN-US"}

[  Orig/RealNexthop: 1.2.3.4/1.2.3.4]{lang="EN-US"}

[         Interface: GE1/0/2]{lang="EN-US"}

[         LocalAddr: 11.1.1.2]{lang="EN-US"}

[         RelyDepth: 0]{lang="EN-US"}

[Backup Nexthop Value:]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 1.2.3.4]{lang="EN-US"}

[  RelyDepth: 0              RealNexthop: 0.0.0.0]{lang="EN-US"}

[  Interface: NULL0            LocalAddr: 0.0.0.0]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_2230290}*[添加]{style="font-family:宋体"}[FRR]{lang="EN-US"}[的]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 19 09:16:18:761 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_19345_x2375_1252123866}

[ USR sync NIB 11000005 to RIB, msgtype ADD, bytes 320]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 1.2.3.4]{lang="EN-US"}

[  RelyDepth: 0              RealNexthop: 1.2.3.4]{lang="EN-US"}

[  Interface: GE1/0/2           LocalAddr: 11.1.1.2]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[Backup Nexthop Value:]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 1.2.3.4]{lang="EN-US"}

[  RelyDepth: 0              RealNexthop: 0.0.0.0]{lang="EN-US"}

[  Interface: NULL0            LocalAddr: 0.0.0.0]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_x802699485}*[同步]{style="font-family:宋体"}[FRR]{lang="EN-US"}[的]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 19 09:15:23:313 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_19345_x2375_x1733293281}

[ USR modify NIB 11000000 with nexthop 2.2.2.2:]{lang="EN-US"}

[ Old value:]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2.2.2.2]{lang="EN-US"}

[  RelyDepth: 1              RealNexthop: 0.0.0.0]{lang="EN-US"}

[  Interface: NULL0            LocalAddr: 0.0.0.0]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[ New value:]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2.2.2.2]{lang="EN-US"}

[  RelyDepth: 1              RealNexthop: 1.2.3.4]{lang="EN-US"}

[  Interface: GE1/0/2           LocalAddr: 11.1.1.2]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_1252189402}*[修改]{style="font-family:宋体"}[NIB]{lang="EN-US"}*

[[\*Sep 19 09:15:23:370 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_19345_x2375_1459377455}

[ USR sync NIB 11000000 to RIB, msgtype MOD, bytes 192]{lang="EN-US"}

[ 1 Nexthop Value(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2.2.2.2]{lang="EN-US"}

[  RelyDepth: 1              RealNexthop: 0.0.0.0]{lang="EN-US"}

[  Interface: NULL0            LocalAddr: 0.0.0.0]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_x590547724}*[修改]{style="font-family:宋体"}[NIB]{lang="EN-US"}[同步给]{style="font-family:宋体"}[RIB]{lang="EN-US"}*

[[\*Sep 19 09:15:23:421 2012 Sysname NIB/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_19345_x2375_x1843029342}

[ USR re-rely route under NIB 11000000]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_x1460591695}*[处理一个]{style="font-family:宋体"}[NIB]{lang="EN-US"}[的重新迭代]{style="font-family:宋体"}*

::: {#-1000075257 .myid}
[]{#_Toc404787494}[]{#struct_0_19345_x2375_1237477560}

**静态路由 \-- 静态路由调试命令 \-- debugging route-static process**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_19345_x2375_x785598780}

[**[debugging route-static process]{lang="EN-US"}**]{#struct_0_19345_x2375_1251206362}

[**[undo debugging route-static process]{lang="EN-US"}**]{#struct_0_19345_x2375_x314480205}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19345_x2375_542233245}

[[用户视图]{style="font-family:宋体"}]{#struct_0_19345_x2375_x452654022}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19345_x2375_x2142691235}

[[network-admin]{lang="EN-US"}]{#struct_0_19345_x2375_1224523296}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19345_x2375_x1216114409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19345_x2375_310225933}

[[无]{style="font-family:宋体"}]{#struct_0_19345_x2375_1009726618}

[[【描述】]{style="font-family:黑体"}]{#struct_0_19345_x2375_x1879372608}

[**[debugging route-static process]{lang="EN-US"}**]{#struct_0_19345_x2375_1251271898}[命令用来打开]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[单播静态路由的调试信息开关。]{style="font-family:宋体"}**[undo debugging route-static process]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播静态路由的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_19345_x2375_864989359}[单播静态路由的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_19345_x2375_x908400190}[[表1-2 ]{lang="EN-US"}[debugging route-static process]{lang="EN-US"}]{#_Ref291766152}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x240023797}[[字段]{style="font-family:黑体"}]{#struct_0_19345_x2375_x814681751}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_19345_x2375_1798856263}

[[Add/Delete/Modify route]{lang="EN-US"}]{#struct_0_19345_x2375_548552928}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19345_x2375_1495414414}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[修改路由]{style="font-family:宋体"}

[[NibID]{lang="EN-US"}]{#struct_0_19345_x2375_x1154602348}

[[下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19345_x2375_1251730651}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19345_x2375_455156917}

[[\# ]{lang="EN-US"}]{#struct_0_19345_x2375_76103796}[打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播静态路由的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging route-static process]{lang="EN-US"}]{#struct_0_19345_x2375_1118840030}

[%May  9 10:41:38:990 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ Add static route 101.1.1.0/24]{lang="EN-US"}

[%May  9 10:41:38:991 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ USR: Add route 101.1.1.0/24 with NibID 0x11000003 to RIB]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_1941505054}*[添加目的地址为]{style="font-family:宋体"}[101.1.1.0/24]{lang="EN-US"}[的静态路由]{style="font-family:宋体"}*

[[%May  9 10:42:13:279 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_19345_x2375_363128159}

[ Add static route 101.1.1.0/24]{lang="EN-US"}

[%May  9 10:42:13:279 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}

[ USR: Modify route 101.1.1.0/24 with NibID 0x11000003]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_x725706812}*[修改目的地址为]{style="font-family:宋体"}[101.1.1.0/24]{lang="EN-US"}[的静态路由]{style="font-family:宋体"}*

[[%May  9 10:40:58:530 2012 Sysname STATICRT/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_19345_x2375_1251796187}

[ USR: Delete route 101.1.1.0/24 with NibID 0x11000003]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19345_x2375_x716084986}*[删除目的地址为]{style="font-family:宋体"}[101.1.1.0/24]{lang="EN-US"}[的静态路由]{style="font-family:宋体"}*
