::: {#499041820 .myid}
[]{#_Toc404787515}[]{#struct_0_x1720_20489_1242948824}[]{#_Toc206489347}[]{#_Toc135643971}[]{#_Toc65038553}[]{#_Toc58333111}[]{#_Toc58294772}

**静态路由 \-- 静态路由配置命令 \-- delete static-routes all**

------------------------------------------------------------------------

[**[delete static-routes all]{lang="EN-US"}**]{#struct_0_x1720_20489_2127882117}[命令用来删除所有静态路由。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x643166322}

[**[delete ]{lang="EN-US"}**[\[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **static-routes all**]{lang="EN-US"}]{#struct_0_x1720_20489_1906857258}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1720_20489_517570742}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1752601677}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1377954162}

[[network-admin]{lang="EN-US"}]{#struct_0_x1720_20489_1135478350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1720_20489_x24790678}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1243014360}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x1720_20489_x1863454055}[：删除指定拓扑的所有静态路由。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则表示删除公网的所有静态路由。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1720_20489_x954699408}[：删除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的所有静态路由。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示删除公网的所有静态路由。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x574086392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用本命令删除静态路由时，系统会提示确认，确认后才会删除所配置的所有静态路由。]{style="font-family:宋体"}]{#struct_0_x1720_20489_1077853493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo ip route-static]{lang="EN-US"}**]{#struct_0_x1720_20489_x842356575}[命令可以删除一条静态路由]{style="font-family:宋体"}[，而使用]{lang="EN-US" style="font-family:宋体"}**[delete static-routes all]{lang="EN-US"}**[命令可以删除包括缺省路由在内的所有静态路由。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1720_20489_2031703378}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_2032237851}[删除所有静态路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1720_20489_x388388220}

[\[Sysname\] delete static-routes all]{lang="EN-US"}

[This will erase all IPv4 static routes and their configurations, you must reconf]{lang="EN-US"}

[igure all static routes.]{lang="EN-US"}

[Are you sure?\[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1243604184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip route-static]{lang="EN-US"}**]{#struct_0_x1720_20489_x570068688}
:::

::: {#1234766828 .myid}
[]{#_Toc206489348}[]{#_Toc135643972}[]{#_Toc404787516}[]{#struct_0_x1720_20489_x2074518342}[]{#_Toc343694280}

**静态路由 \-- 静态路由配置命令 \-- display route-static nib**

------------------------------------------------------------------------

[**[display route-static nib]{lang="EN-US"}**]{#struct_0_x1720_20489_x573351756}[命令用来显示静态路由下一跳信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_80514461}

[**[display route-static nib ]{lang="EN-US"}**[\[ *nib-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1720_20489_x956933513}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1720_20489_500667678}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1720_20489_597425370}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1880004832}

[[network-admin]{lang="EN-US"}]{#struct_0_x1720_20489_1243669720}

[[network-operator]{lang="EN-US"}]{#struct_0_x1720_20489_923426053}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1720_20489_x330091806}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1720_20489_138439956}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x944748714}

[*[nib-id]{lang="EN-US"}*]{#struct_0_x1720_20489_x1513441718}[：路由邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[值，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1720_20489_x604878548}[：显示详细信息。如果未指定本参数，则显示概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1263102279}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_165409096}[显示]{style="font-family:宋体"}[静态路由下一跳信息。]{style="font-family:宋体"}

[[\<Sysname\> display route-static nib]{lang="EN-US"}]{#struct_0_x1720_20489_1243079897}

[Total number of nexthop(s): 44]{lang="EN-US"}

[ ]{lang="EN-US"}

[      NibID: 0x11000000        Sequence: 0]{lang="EN-US"}

[       Type: 0x21               Flushed: Yes]{lang="EN-US"}

[   UserKey0: 0x111              VrfNthp: 0]{lang="EN-US"}

[   UserKey1: 0x0                Nexthop: 0.0.0.0]{lang="EN-US"}

[    IFIndex: 0x111            LocalAddr: 0.0.0.0]{lang="EN-US"}

[   TopoNthp: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[      NibID: 0x11000001        Sequence: 1]{lang="EN-US"}

[       Type: 0x41               Flushed: Yes]{lang="EN-US"}

[   UserKey0: 0x0                VrfNthp: 5]{lang="EN-US"}

[   UserKey1: 0x0                Nexthop: 2.2.2.2]{lang="EN-US"}

[    IFIndex: 0x0              LocalAddr: 0.0.0.0]{lang="EN-US"}

[   TopoNthp: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\...\...]{lang="EN-US"}[（省略部分显示信息）]{style="font-family:
宋体"}

[]{#struct_0_x1720_20489_1348820288}[[表1-1 ]{lang="EN-US"}[display route-static nib]{lang="EN-US"}]{#_Ref343696159}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2077092801}[[字段]{style="font-family:黑体"}]{#struct_0_x1720_20489_x447331626}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1720_20489_1766884746}

[[Total number of nexthop(s)]{lang="EN-US"}]{#struct_0_x1720_20489_306390323}

[[总的下一跳个数]{style="font-family:宋体"}]{#struct_0_x1720_20489_1243145433}

[[NibID]{lang="EN-US"}]{#struct_0_x1720_20489_958326245}

[[NIB ID]{lang="EN-US"}]{#struct_0_x1720_20489_x2117948406}[号]{style="font-family:宋体"}

[[Sequence]{lang="EN-US"}]{#struct_0_x1720_20489_1519497327}

[[NIB]{lang="EN-US"}]{#struct_0_x1720_20489_x1095468739}[序列号]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1720_20489_x716120406}

[[NIB]{lang="EN-US"}]{#struct_0_x1720_20489_1243210969}[类型]{style="font-family:宋体"}

[[Flushed]{lang="EN-US"}]{#struct_0_x1720_20489_223429658}

[[是否下刷]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_x1720_20489_x1503715542}

[[UserKey0]{lang="EN-US"}]{#struct_0_x1720_20489_x1503933383}

[[NIB]{lang="EN-US"}]{#struct_0_x1720_20489_2033874234}[协议保留数据]{style="font-family:宋体"}[1]{lang="EN-US"}

[[UserKey1]{lang="EN-US"}]{#struct_0_x1720_20489_x1195231959}

[[NIB]{lang="EN-US"}]{#struct_0_x1720_20489_1243276505}[协议保留数据]{style="font-family:宋体"}[2]{lang="EN-US"}

[[VrfNthp]{lang="EN-US"}]{#struct_0_x1720_20489_x974485386}

[[下一跳所在]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1720_20489_x1991745448}

[[Nexthop]{lang="EN-US"}]{#struct_0_x1720_20489_494687923}

[[下一跳信息]{style="font-family:宋体"}]{#struct_0_x1720_20489_x851949859}

[[IFIndex]{lang="EN-US"}]{#struct_0_x1720_20489_1242817753}

[[接口索引]{style="font-family:宋体"}]{#struct_0_x1720_20489_209648586}

[[LocalAddr]{lang="EN-US"}]{#struct_0_x1720_20489_x2131973505}

[[本地接口地址]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1847095716}

[[TopoNthp]{lang="EN-US"}]{#struct_0_x1720_20489_x1934599215}

[[下一跳所在拓扑，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1720_20489_1565093950}[为公网拓扑（目前]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[不支持子拓扑，显示为]{style="font-family:宋体"}[Invalid]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_1052836638}[显示]{style="font-family:宋体"}[静态路由下一跳详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display route-static nib verbose]{lang="EN-US"}]{#struct_0_x1720_20489_1242948825}

[Total number of nexthop(s): 44]{lang="EN-US"}

[ ]{lang="EN-US"}

[      NibID: 0x11000000        Sequence: 0]{lang="EN-US"}

[       Type: 0x21               Flushed: Yes]{lang="EN-US"}

[   UserKey0: 0x111              VrfNthp: 0]{lang="EN-US"}

[   UserKey1: 0x0                Nexthop: 0.0.0.0]{lang="EN-US"}

[    IFIndex: 0x111            LocalAddr: 0.0.0.0]{lang="EN-US"}

[   TopoNthp: 0]{lang="EN-US"}

[     RefCnt: 2              FlushRefCnt: 0]{lang="EN-US"}

[       Flag: 0x2                Version: 1]{lang="EN-US"}

[ 1 nexthop(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 0.0.0.0]{lang="EN-US"}

[  RelyDepth: 0              RealNexthop: 0.0.0.0]{lang="EN-US"}

[  Interface: NULL0            LocalAddr: 0.0.0.0]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[ ]{lang="EN-US"}

[      NibID: 0x11000001        Sequence: 1]{lang="EN-US"}

[       Type: 0x41               Flushed: Yes]{lang="EN-US"}

[   UserKey0: 0x0                VrfNthp: 5]{lang="EN-US"}

[   UserKey1: 0x0                Nexthop: 2.2.2.2]{lang="EN-US"}

[    IFIndex: 0x0              LocalAddr: 0.0.0.0]{lang="EN-US"}

[   TopoNthp: 0]{lang="EN-US"}

[     RefCnt: 1              FlushRefCnt: 0]{lang="EN-US"}

[       Flag: 0x12               Version: 1]{lang="EN-US"}

[ 2 nexthop(s):]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2.2.2.2]{lang="EN-US"}

[  RelyDepth: 7              RealNexthop: 8.8.8.8]{lang="EN-US"}

[  Interface: Dia0             LocalAddr: 12.12.12.12]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[PrefixIndex: 0              OrigNexthop: 2.2.2.2]{lang="EN-US"}

[  RelyDepth: 9              RealNexthop: 0.0.0.0]{lang="EN-US"}

[  Interface: NULL0            LocalAddr: 0.0.0.0]{lang="EN-US"}

[  TunnelCnt: 0                      Vrf: default-vrf]{lang="EN-US"}

[   TunnelID: N/A               Topology: base]{lang="EN-US"}

[ ]{lang="EN-US"}

[\...\...]{lang="EN-US"}[（省略部分显示信息）]{style="font-family:
宋体"}

[]{#_Toc343694281}[]{#struct_0_x1720_20489_2127816581}[[表1-2 ]{lang="EN-US"}[display route-static nib verbose]{lang="EN-US"}]{#_Ref343696198}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2072592458}[[字段]{style="font-family:黑体"}]{#struct_0_x1720_20489_572210473}

[[描述]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1570418607}

[*[x]{lang="EN-US"}*[ nexthop (s)]{lang="EN-US"}]{#struct_0_x1720_20489_x968772379}

[[下一跳具体值（前面数值表示下一跳个数）]{style="font-family:宋体"}]{#struct_0_x1720_20489_x881980772}

[[PrefixIndex]{lang="EN-US"}]{#struct_0_x1720_20489_584402250}

[[等价时下一跳序号]{style="font-family:宋体"}]{#struct_0_x1720_20489_1860258204}

[[OrigNexthop]{lang="EN-US"}]{#struct_0_x1720_20489_x104753925}

[[原始下一跳]{style="font-family:宋体"}]{#struct_0_x1720_20489_2140372204}

[[RelyDepth]{lang="EN-US"}]{#struct_0_x1720_20489_1621378877}

[[迭代深度]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1634215717}

[[RealNexthop]{lang="EN-US"}]{#struct_0_x1720_20489_1419005308}

[[真实下一跳]{style="font-family:宋体"}]{#struct_0_x1720_20489_299393782}

[[Interface]{lang="EN-US"}]{#struct_0_x1720_20489_1243604185}

[[出接口]{style="font-family:宋体"}]{#struct_0_x1720_20489_x570134224}

[[localAddr]{lang="EN-US"}]{#struct_0_x1720_20489_1357239401}

[[本地接口地址]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1719380592}

[[TunnelCnt]{lang="EN-US"}]{#struct_0_x1720_20489_1243669721}

[[迭代到隧道的个数]{style="font-family:宋体"}]{#struct_0_x1720_20489_923360517}

[[Vrf]{lang="EN-US"}]{#struct_0_x1720_20489_1621575485}

[[实例名]{style="font-family:宋体"}]{#struct_0_x1720_20489_x822618765}

[[TunnelID]{lang="EN-US"}]{#struct_0_x1720_20489_x1716065421}

[[迭代到隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1720_20489_153170483}

[[Topology]{lang="EN-US"}]{#struct_0_x1720_20489_x1934730287}

[[拓扑名称，]{style="font-family:宋体"}[base]{lang="EN-US"}]{#struct_0_x1720_20489_x1934271535}[为公网拓扑（目前]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[不支持子拓扑，显示为空）]{style="font-family:宋体"}

[[RefCnt]{lang="EN-US"}]{#struct_0_x1720_20489_1201816138}

[[下一跳信息的引用计数]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1082586087}

[[FlushRefCnt]{lang="EN-US"}]{#struct_0_x1720_20489_1243079894}

[[下一跳信息的下刷引用计数]{style="font-family:宋体"}]{#struct_0_x1720_20489_1348623680}

[[Flag]{lang="EN-US"}]{#struct_0_x1720_20489_353554177}

[[下一跳信息的标志位]{style="font-family:宋体"}]{#struct_0_x1720_20489_1680447587}

[[Version]{lang="EN-US"}]{#struct_0_x1720_20489_1243145430}

[[下一跳信息的版本号]{style="font-family:宋体"}]{#struct_0_x1720_20489_958260709}

[ ]{lang="EN-US"}

::: {#-6284171 .myid}
[]{#_Toc404787517}[]{#struct_0_x1720_20489_1374876321}

**静态路由 \-- 静态路由配置命令 \-- display route-static routing-table**

------------------------------------------------------------------------

[**[display route-static routing-table]{lang="EN-US"}**]{#struct_0_x1720_20489_1242230691}[命令用来显示静态路由表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1365031921}

[**[display route-static routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] \[ *ip-address* { *mask-length* \| *mask* } \]]{lang="EN-US"}]{#struct_0_x1720_20489_x843788865}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x718490041}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1720_20489_1532809888}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1243210966}

[[network-admin]{lang="EN-US"}]{#struct_0_x1720_20489_224019482}

[[network-operator]{lang="EN-US"}]{#struct_0_x1720_20489_x831101818}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1720_20489_1792896374}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1720_20489_x1752416031}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1457511081}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x1720_20489_x1863454056}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1720_20489_x1235111973}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1720_20489_1674721727}[：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制。]{style="font-family:宋体"}

[*[mask-length/mask]{lang="EN-US"}*]{#struct_0_x1720_20489_14860296}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1625569144}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_1243276502}[显示静态路由表信息。]{style="font-family:宋体"}

[[\<Sysname\> display route-static routing-table]{lang="EN-US"}]{#struct_0_x1720_20489_1242817750}

[Total number of routes: 24]{lang="EN-US"}

[ ]{lang="EN-US"}

[Status: \* - valid]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Destination: 0.0.0.0/0]{lang="EN-US"}

[       NibID: 0x1100000a         NextHop: 2.2.2.10]{lang="EN-US"}

[   MainNibID: N/A              BkNextHop: N/A]{lang="EN-US"}

[     BkNibID: N/A              Interface: N/A]{lang="EN-US"}

[     TableID: 0x2            BkInterface: N/A]{lang="EN-US"}

[        Flag: 0x82d01           BfdSrcIp: N/A]{lang="EN-US"}

[     DbIndex: 0xd             BfdIfIndex: 0x0]{lang="EN-US"}

[        Type: Normal         BfdVrfIndex: 0]{lang="EN-US"}

[  TrackIndex: 0xffffffff           Label: NULL]{lang="EN-US"}

[  Preference: 60             vrfIndexDst: 0]{lang="EN-US"}

[     BfdMode: N/A             vrfIndexNH: 0]{lang="EN-US"}

[   Permanent: 0                      Tag: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination: 0.0.0.0/0]{lang="EN-US"}

[       NibID: 0x1100000b         NextHop: 2.2.2.11]{lang="EN-US"}

[   MainNibID: N/A              BkNextHop: N/A]{lang="EN-US"}

[     BkNibID: N/A              Interface: N/A]{lang="EN-US"}

[     TableID: 0x2            BkInterface: N/A]{lang="EN-US"}

[        Flag: 0x82d01           BfdSrcIp: N/A]{lang="EN-US"}

[     DbIndex: 0xd             BfdIfIndex: 0x0]{lang="EN-US"}

[        Type: Normal         BfdVrfIndex: 0]{lang="EN-US"}

[  TrackIndex: 0xffffffff           Label: NULL]{lang="EN-US"}

[  Preference: 60             vrfIndexDst: 0]{lang="EN-US"}

[     BfdMode: N/A             vrfIndexNH: 0]{lang="EN-US"}

[   Permanent: 0                      Tag: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\...\...]{lang="EN-US"}[（省略部分显示信息）]{style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_209714122}[显示目的地址为]{style="font-family:宋体"}[1.2.3.4/32]{lang="EN-US"}[的静态路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display route-static routing-table 1.2.3.4 32]{lang="EN-US"}]{#struct_0_x1720_20489_1777063726}

[ ]{lang="EN-US"}

[\*Destination: 1.2.3.4/32]{lang="EN-US"}

[       NibID: 0x11000017         NextHop: 4.4.4.4]{lang="EN-US"}

[   MainNibID: 0x11000015       BkNextHop: 5.5.5.5]{lang="EN-US"}

[     BkNibID: 0x11000016       Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     TableID: 0x2            BkInterface: GigabitEthernet1/0/2]{lang="EN-US"}

[        Flag: 0xa8d0b           BfdSrcIp: N/A]{lang="EN-US"}

[     DbIndex: 0x17            BfdIfIndex: 0x0]{lang="EN-US"}

[        Type: Normal         BfdVrfIndex: 0]{lang="EN-US"}

[  TrackIndex: 0xffffffff           Label: NULL]{lang="EN-US"}

[  Preference: 60             vrfIndexDst: 0]{lang="EN-US"}

[     BfdMode: N/A             vrfIndexNH: 0]{lang="EN-US"}

[   Permanent: 0                      Tag: 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display route-static routing-table]{lang="EN-US"}]{#struct_0_x1720_20489_84453795}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_2068581878}[[字段]{style="font-family:黑体"}]{#struct_0_x1720_20489_1242883286}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1720_20489_946458171}

[[Total number of routes]{lang="EN-US"}]{#struct_0_x1720_20489_x7870995}

[[总的路由条数]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1850853908}

[[Destination]{lang="EN-US"}]{#struct_0_x1720_20489_833135496}

[[目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1720_20489_x987603813}[掩码]{style="font-family:宋体"}

[[NibID]{lang="EN-US"}]{#struct_0_x1720_20489_x1612787568}

[[下一跳信息]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1720_20489_1242948822}

[[MainNibID]{lang="EN-US"}]{#struct_0_x1720_20489_2128275333}

[[FRR]{lang="EN-US"}]{#struct_0_x1720_20489_x1582380725}[静态路由主下一跳信息]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[BkNibID]{lang="EN-US"}]{#struct_0_x1720_20489_1151599856}

[[FRR]{lang="EN-US"}]{#struct_0_x1720_20489_1137792168}[静态路由备下一跳信息]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[NextHop]{lang="EN-US"}]{#struct_0_x1720_20489_654769654}

[[此路由的下一跳地址]{style="font-family:宋体"}]{#struct_0_x1720_20489_1243014358}

[[BkNextHop]{lang="EN-US"}]{#struct_0_x1720_20489_x955223699}

[[此路由的备份下一跳地址]{style="font-family:宋体"}]{#struct_0_x1720_20489_x940665843}

[[Interface]{lang="EN-US"}]{#struct_0_x1720_20489_x1954630717}

[[出接口，即到该目的网段的数据包将从此接口发出]{style="font-family:宋体"}]{#struct_0_x1720_20489_530245418}

[[BkInterface]{lang="EN-US"}]{#struct_0_x1720_20489_x257563186}

[[备份出接口]{style="font-family:宋体"}]{#struct_0_x1720_20489_1243604182}

[[TableID]{lang="EN-US"}]{#struct_0_x1720_20489_x570199760}

[[路由所在的表]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1720_20489_1796204678}

[[Flag]{lang="EN-US"}]{#struct_0_x1720_20489_x1638716579}

[[路由标志位]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1704670798}

[[DbIndex]{lang="EN-US"}]{#struct_0_x1720_20489_1243669718}

[[路由所在]{style="font-family:宋体"}[DB]{lang="EN-US"}]{#struct_0_x1720_20489_923950342}[的]{style="font-family:宋体"}[DB]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1720_20489_184985401}

[[路由类型：]{style="font-family:宋体"}]{#struct_0_x1720_20489_x758157215}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x1720_20489_1243079895}[：普通类型的静态路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x1720_20489_1348689216}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[类型的静态路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAT]{lang="EN-US"}]{#struct_0_x1720_20489_x1670292218}[：]{style="font-family:宋体"}[NAT]{lang="EN-US"}[类型的静态路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec]{lang="EN-US"}]{#struct_0_x1720_20489_x297697790}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[类型的静态路由]{style="font-family:宋体"}

[[BfdSrcIp]{lang="EN-US"}]{#struct_0_x1720_20489_1181798953}

[[BFD]{lang="EN-US"}]{#struct_0_x1720_20489_x1664822722}[非直连会话源地址]{style="font-family:宋体"}

[[BfdIfIndex]{lang="EN-US"}]{#struct_0_x1720_20489_1243145431}

[[BFD]{lang="EN-US"}]{#struct_0_x1720_20489_958195173}[使用的接口索引]{style="font-family:宋体"}

[[BfdVrfIndex]{lang="EN-US"}]{#struct_0_x1720_20489_x1986196738}

[[BFD]{lang="EN-US"}]{#struct_0_x1720_20489_940989534}[所在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例索引]{style="font-family:宋体"}

[[BfdMode]{lang="EN-US"}]{#struct_0_x1720_20489_1243210967}

[[BFD]{lang="EN-US"}]{#struct_0_x1720_20489_224085018}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x1720_20489_1076180565}[：未配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ctrl]{lang="EN-US"}]{#struct_0_x1720_20489_x493865750}[：控制报文方式的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Echo]{lang="EN-US"}]{#struct_0_x1720_20489_1243276503}[：]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文方式的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[TrackIndex]{lang="EN-US"}]{#struct_0_x1720_20489_x974616458}

[[NQA Track]{lang="EN-US"}]{#struct_0_x1720_20489_693419622}[索引]{style="font-family:宋体"}

[[Label]{lang="EN-US"}]{#struct_0_x1720_20489_x229437955}

[[标签]{style="font-family:宋体"}]{#struct_0_x1720_20489_1242817751}

[[Preference]{lang="EN-US"}]{#struct_0_x1720_20489_209779658}

[[路由优先级]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1353697989}

[[vrfIndexDst]{lang="EN-US"}]{#struct_0_x1720_20489_850857687}

[[目的所在]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1720_20489_1242883287}[索引]{style="font-family:宋体"}

[[vrfIndexNH]{lang="EN-US"}]{#struct_0_x1720_20489_946392635}

[[下一跳所在]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1720_20489_133836388}[索引]{style="font-family:宋体"}

[[Permanent]{lang="EN-US"}]{#struct_0_x1720_20489_1242948823}

[[永久静态路由标志（]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1720_20489_2128209797}[表示永久静态路由）]{style="font-family:宋体"}

[[Tag]{lang="EN-US"}]{#struct_0_x1720_20489_345850009}

[[路由标记]{style="font-family:宋体"}]{#struct_0_x1720_20489_1243014359}

[ ]{lang="EN-US"}

::: {#903810212 .myid}
[]{#_Toc404787518}[]{#struct_0_x1720_20489_x955158163}

**静态路由 \-- 静态路由配置命令 \-- ip route-static**

------------------------------------------------------------------------

[**[ip route-static]{lang="EN-US"}**]{#struct_0_x1720_20489_x187787560}[命令用来配置静态路由。]{style="font-family:宋体"}

[**[undo ip route-static]{lang="EN-US"}**]{#struct_0_x1720_20489_x137583908}[命令用来删除已配置的静态路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x538421489}

[**[ip]{lang="EN-US"}**[ **route-static** *dest-address* { *mask-length* \| *mask* } { *interface-type* *interface-number* \[ *next-hop-address* \] \[ **backup-interface** *interface-type* *interface-number* \[ **backup-nexthop** *backup-nexthop-address* \] \[ **permanent** \] \| **bfd** { **control-packet** \| **echo-packet** } \| **permanent** \] \| *next-hop-address* \[ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* \] \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* \[ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* \] } \[ **preference** *preference-value* \] \[ **tag** *tag-value* \] \[ **description** *description-text* \]]{lang="EN-US"}]{#struct_0_x1720_20489_x2107347457}

[**[undo]{lang="EN-US"}**[ **ip** **route-static**]{lang="EN-US"}[ *dest-address* { *mask-length* \| *mask* } \[ *interface-type* *interface-number* \[ *next-hop-address* \] \| *next-hop-address* \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* \] \[ **preference** *preference-value* \]]{lang="EN-US"}]{#struct_0_x1720_20489_x529259254}

[**[ip route-static]{lang="EN-US"}**[ **vpn-instance** *s-vpn-instance-name* *dest-address* { *mask-length* \| *mask* } { *interface-type* *interface-number* \[ *next-hop-address* \] \[ **backup-interface** *interface-type* *interface-number* \[ **backup-nexthop** *backup-nexthop-address* \] \[ **permanent** \] \| **bfd** { **control-packet** \| **echo-packet** } \| **permanent** \] \| *next-hop-address* \[ **public** \] \[ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* \] \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* \[ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* \] } \[ **preference** *preference-value* \] \[ **tag** *tag-value* \] \[ **description** *description-text* \]]{lang="EN-US"}]{#struct_0_x1720_20489_37427749}

[**[undo]{lang="EN-US"}**[ **ip** **route-static** **vpn-instance**]{lang="EN-US"}[ *s-vpn-instance-name* *dest-address* { *mask-length* \| *mask* } \[ *interface-type* *interface-number* \[ *next-hop-address* \] \| *next-hop-address* \[ **public** \] \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* \] \[ **preference** *preference-value* \]]{lang="EN-US"}]{#struct_0_x1720_20489_1514103150}

[**[ip route-static]{lang="EN-US"}**[ **topology** *topo-name* *dest-address* { *mask* \| *mask-length* } { *next-hop-address* \| *interface-type* *interface-number* \[ *next-hop-address* \[ **backup-interface** *interface-type* *interface-number* **backup-nexthop** *backup-nexthop-address* \] \] } \[ **preference** *preference-value* \] \[ **tag** *tag-value* \] \[ **description** *description-text* \]]{lang="EN-US"}]{#struct_0_x1720_20489_x298025470}

[**[undo]{lang="EN-US"}**[ **ip** **route-static** **topology**]{lang="EN-US"}[ *topo-name* *dest-address* { *mask* \| *mask-length* } \[ *next-hop-address* \| *interface-type* *interface-number* \[ *next-hop-address* \] \] \[ **preference** *preference-value* \]]{lang="EN-US"}]{#struct_0_x1720_20489_x887192817}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1243604183}

[[没有配置静态路由。]{style="font-family:宋体"}]{#struct_0_x1720_20489_x570265296}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1356505178}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1720_20489_1525122536}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x409920265}

[[network-admin]{lang="EN-US"}]{#struct_0_x1720_20489_1732178369}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1720_20489_x1129596455}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1301528357}

[**[vpn-instance]{lang="EN-US"}**[ *s-vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1720_20489_x1718695908}[：指定源]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[s-vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。每个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[都有自己的路由表，配置的静态路由将被加入指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的路由表。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x1720_20489_x297959934}[：指定拓扑。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。每个拓扑都有自己的路由表，配置的静态路由将被加入指定拓扑的路由表。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[dest-address]{lang="EN-US"}*]{#struct_0_x1720_20489_1243669719}[：静态路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length/mask]{lang="EN-US"}*]{#struct_0_x1720_20489_923884806}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="FR"}**]{#struct_0_x1720_20489_2079316105}*[ d-vpn-instance-name]{lang="FR"}*[：]{style="font-family:宋体"}[指定目的]{style="font-family:宋体"}[VPN]{lang="FR"}[。]{style="font-family:宋体"}*[d-vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果指定目的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，静态路由将根据配置的]{style="font-family:宋体"}*[next-hop-address]{lang="EN-US"}*[在目的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中查找出接口。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1720_20489_1570851261}[：指定静态路由的出接口类型和接口号。在指定静态路由的出接口类型和接口号时需要注意的事项，详见使用指导。]{style="font-family:宋体"}

[*[next-hop-address]{lang="EN-US"}*]{#struct_0_x1720_20489_x1050483835}[：指定路由的下一跳的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制格式。在指定路由的下一跳的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时需要注意的事项，详见使用指导。]{style="font-family:宋体"}

[**[backup-interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1720_20489_2075325513}[：备份出接口。对于备份出接口为非]{style="font-family:宋体"}[P2P]{lang="EN-US"}[类型的接口时（包括]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型接口或广播类型接口，如以太网接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口等），必须同时指定其对应的备份下一跳地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为指定的接口类型和编号。]{style="font-family:
宋体"}

[**[backup-nexthop]{lang="EN-US"}***[ ]{lang="EN-US"}[backup-nexthop-address]{lang="EN-US"}*]{#struct_0_x1720_20489_x750418509}[：备份下一跳地址。]{style="font-family:宋体"}

[**[bfd]{lang="EN-US"}**]{#struct_0_x1720_20489_1480169312}[：使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Bidirectional Forwarding Detection]{lang="EN-US"}[，双向转发检测）功能，对静态路由下一跳的可达性进行快速检测，当下一跳不可达时可以快速切换到备份路由。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[control-packet]{lang="EN-US"}**]{#struct_0_x1720_20489_1761756951}[：通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文方式实现]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[bfd-source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1720_20489_x1638985977}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。建议配置为]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[permanent]{lang="EN-US"}**]{#struct_0_x1720_20489_x1485803457}[：指定为永久静态路由。即使在出接口]{style="font-family:宋体"}[down]{lang="EN-US"}[时，配置的永久静态路由仍然保持]{style="font-family:宋体"}[active]{lang="EN-US"}[状态。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[track ]{lang="EN-US"}**]{#struct_0_x1720_20489_x1955855637}*[track-entry-number]{lang="EN-US"}*[：将静态路由与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项相关联，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。关于]{style="font-family:宋体"}[Track]{lang="EN-US"}[的详细介绍，请参见"可靠性配置指导"中的"]{style="font-family:宋体"}[Track]{lang="EN-US"}["。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[echo-packet]{lang="EN-US"}**]{#struct_0_x1720_20489_169170422}[：通过]{style="font-family:宋体"}[BFD echo]{lang="EN-US"}[报文方式实现]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[public]{lang="EN-US"}**]{#struct_0_x1720_20489_2078354101}[：指定静态路由下一跳处于公网实例。]{style="font-family:宋体"}

[]{#struct_0_x1720_20489_250385054}[]{#_Hlt6909217}**[preference]{lang="EN-US"}**[ *preference-value*]{lang="EN-US"}[：指定静态路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[60]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag-value]{lang="EN-US"}*]{#struct_0_x1720_20489_x1559554564}[：静态路由]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，用于标识该条静态路由，以便在路由策略中根据]{style="font-family:宋体"}[Tag]{lang="EN-US"}[对路由进行灵活的控制。]{style="font-family:宋体"}*[tag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。关于路由策略的详细信息，请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由配置指导"中的"路由策略"。]{style="font-family:宋体"}

[**[description ]{lang="EN-US"}***[description-text]{lang="EN-US"}*]{#struct_0_x1720_20489_2064750827}[：配置的静态路由描述信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[个字符。除"]{style="font-family:宋体"}[?]{lang="EN-US"}["外，可以包含空格等特殊字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1485737921}

[[如果目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1720_20489_x748728503}[地址和掩码都为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[（或掩码为]{style="font-family:宋体"}[0]{lang="EN-US"}[），则配置的路由为缺省路由。当没有匹配的路由表项时，将使用缺省路由进行报文转发。]{style="font-family:宋体"}

[[对不同的优先级配置，可采用不同的路由管理策略。例如，为同一目的地配置多条路由，如果指定相同的优先级，则实现路由负载分担；如果指定不同的优先级，则实现路由备份。]{style="font-family:宋体"}]{#struct_0_x1720_20489_1579136584}

[[配置静态路由时，可根据实际需要指定出接口或下一跳地址。需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1720_20489_1984491649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[Null0]{lang="EN-US"}]{#struct_0_x1720_20489_1665002373}[接口，配置了出接口就不需要配置下一跳地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于点到点接口（如封装]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1294516984}[PPP]{lang="EN-US"}[协议的串口），配置时可以只指定出接口，不指定下一跳地址。这样，即使对端地址发生了变化也无须改变配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1010454921}[NBMA]{lang="EN-US"}[、]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[等接口（如封装]{style="font-family:宋体"}[X.25]{lang="EN-US"}[或者帧中继的接口），需要进行]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址到链路层地址的映射，建议同时配置出接口和下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于广播类型接口（如以太网接口、]{style="font-family:宋体"}]{#struct_0_x1720_20489_826171624}[VLAN]{lang="EN-US"}[接口），因为可能有多个下一跳，配置时必须同时指定出接口和下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[配置静态路由时需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1176360720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由振荡时，使能]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1307628542}[BFD]{lang="EN-US"}[检测功能可能会加剧振荡，需谨慎使用。关于]{style="font-family:宋体"}[BFD]{lang="EN-US"}[的详细介绍，请参考"可靠性配置指导"中的"]{style="font-family:宋体"}[BFD]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1485672385}[Track]{lang="EN-US"}[模块通过]{style="font-family:宋体"}[NQA]{lang="EN-US"}[探测私网静态路由中下一跳的可达性，静态路由下一跳的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例号与]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组配置的实例号必须相同，才能进行正常的探测。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在静态路由进行迭代时，]{style="font-family:宋体"}]{#struct_0_x1720_20489_1389583591}[Track]{lang="EN-US"}[项监测的应该是静态路由真正的下一跳，而不是配置的下一跳。否则，可能导致错误地将有效路由判断为无效路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}**[permanent]{lang="EN-US"}**]{#struct_0_x1720_20489_x2007760323}[不能和]{lang="EN-US" style="font-family:宋体"}**[bfd]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[track]{lang="EN-US"}**[一起进行配置。]{lang="EN-US" style="font-family:宋体"}

[[【**举例】**]{style="font-family:黑体"}]{#struct_0_x1720_20489_x199208738}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_x2084339544}[配置静态路由，其目的地址为]{style="font-family:宋体"}[1.1.1.1/24]{lang="EN-US"}[，指定下一跳为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值为]{style="font-family:宋体"}[45]{lang="EN-US"}[，描述信息为"]{style="font-family:宋体"}[for internet]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1720_20489_x1849234705}

[\[Sysname\] ip route-static 1.1.1.1 24 2.2.2.2 tag 45 description for internet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x59272945}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip routing-table protocol]{lang="EN-US"}**]{#struct_0_x1720_20489_x763360041}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1369791922 .myid}
[]{#_Toc404787519}[]{#struct_0_x1720_20489_x1485606849}[]{#_Toc206489349}[]{#_Toc135643973}[]{#_Toc73872319}[]{#_Toc134071117}[]{#_Toc135455872}

**静态路由 \-- 静态路由配置命令 \-- ip route-static default-preference**

------------------------------------------------------------------------

[**[ip route-static default-preference]{lang="EN-US"}**]{#struct_0_x1720_20489_x823156107}[命令用来配置静态路由的缺省优先级。]{style="font-family:宋体"}

[**[undo ip route-static default-preference]{lang="EN-US"}**]{#struct_0_x1720_20489_1511135135}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1697029417}

[**[ip route-static default-preference ]{lang="EN-US"}***[default-preference-value]{lang="EN-US"}*]{#struct_0_x1720_20489_22117625}

[**[undo ip route-static default-preference]{lang="EN-US"}**]{#struct_0_x1720_20489_1164446674}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1499787545}

[[静态路由的缺省优先级为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_x1720_20489_403051562}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1431324362}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1720_20489_1391706703}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1486065601}

[[network-admin]{lang="EN-US"}]{#struct_0_x1720_20489_x17557562}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1720_20489_1755406383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x274110222}

[*[default-preference-value]{lang="EN-US"}*]{#struct_0_x1720_20489_x80150022}[：静态路由缺省优先级的值，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1119482177}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在配置静态路由时没有指定优先级，就会使用缺省优先级。]{style="font-family:宋体"}]{#struct_0_x1720_20489_x784393368}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新配置缺省优先级后，新设置的缺省优先级仅对新增的静态路由有效。]{style="font-family:宋体"}]{#struct_0_x1720_20489_1144180743}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1919304635}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_x1486000065}[配置静态路由的缺省优先级为]{style="font-family:宋体"}[120]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1720_20489_1059527186}

[\[Sysname\] ip route-static default-preference 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1885604807}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip routing-table protocol]{lang="EN-US"}**]{#struct_0_x1720_20489_x2074427565}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#2064101149 .myid}
[]{#_Toc404787520}[]{#struct_0_x1720_20489_576890218}[]{#_Toc357582607}[]{#_Toc354145697}[]{#_Toc333393884}[]{#_Toc333390460}

**静态路由 \-- 静态路由配置命令 \-- ip route-static fast-reroute auto**

------------------------------------------------------------------------

[**[ip route-static fast-reroute auto]{lang="EN-US"}**]{#struct_0_x1720_20489_x1425659154}[命令用来配置静态路由自动]{style="font-family:宋体"}[快速重路由功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ip route-static fast-reroute auto]{lang="EN-US"}**]{#struct_0_x1720_20489_293206084}[命令用来关闭静态路由自动]{style="font-family:宋体"}[快速重路由功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x1485934529}

[**[ip route-static fast-reroute auto]{lang="EN-US"}**]{#struct_0_x1720_20489_x1251562899}

[**[undo ip route-static fast-reroute auto]{lang="EN-US"}**]{#struct_0_x1720_20489_1007299286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x569754217}

[[静态路由自动快速重路由功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1286671407}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x12221107}

[[系统]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1485868993}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1625108022}

[[network-admin]{lang="EN-US"}]{#struct_0_x1720_20489_419944602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1720_20489_2144415074}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x387130873}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_467354722}[配置静态路由自动快速重路由功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1720_20489_x1485279169}

[[\[Sysname\] ip route-static fast-reroute auto]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1720_20489_x1687301075}
:::

::::: {#1303044923 .myid}
[]{#_Toc404787521}[]{#struct_0_x1720_20489_x298156543}[]{#_Toc363978890}

**静态路由 \-- 静态路由配置命令 \-- ip route-static primary-path-detect bfd echo**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](静态路由命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1720_20489_x298091007}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1720_20489_1823387814}
:::

**[ ]{lang="EN-US"}**

[**[ip route-static primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_x1720_20489_773767017}[命令用来使能静态路由中主用链路的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[**[undo ip route-static primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_x1720_20489_x298025471}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x887258353}

[**[ip route-static primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_x1720_20489_1012244331}

[**[undo ip route-static primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_x1720_20489_1769199568}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x297959935}

[[静态路由中主用链路的]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1720_20489_852036886}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1720_20489_1808659107}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1720_20489_x1816576741}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x297370111}

[[network-admin]{lang="EN-US"}]{#struct_0_x1720_20489_x1882577467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1720_20489_x835605853}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1720_20489_x297304575}

[[配置本功能后，静态路由的快速重路由特性中的主用链路将使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1720_20489_x315164617}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）进行检测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1720_20489_907715719}

[[\# ]{lang="EN-US"}]{#struct_0_x1720_20489_x89875968}[配置静态路由快速重路由特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1720_20489_x297894400}

[\[Sysname\] ip route-static 1.1.1.1 32 gigabitethernet 1/0/1 2.2.2.2 backup-interface gigabitethernet 1/0/2 backup-nexthop 3.3.3.3]{lang="EN-US"}

[\[Sysname\] ip route-static primary-path-detect bfd echo]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
