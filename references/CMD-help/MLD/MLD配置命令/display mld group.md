::: {#1950746422 .myid}
[]{#_Toc404790274}[]{#struct_0_42457_14668_x969523842}[]{#_Toc136854345}[]{#_Toc157315256}[]{#_Toc157315257}[]{#_Toc157315258}[]{#_Toc157315259}[]{#_Toc157315260}[]{#_Toc157315261}[]{#_Toc157315262}[]{#_Toc157315263}[]{#_Toc157315264}[]{#_Toc157315265}[]{#_Toc157315266}[]{#_Toc157315267}[]{#_Toc157315268}[]{#_Toc157315269}[]{#_Toc157315270}[]{#_Toc157315271}[]{#_Toc157315274}[]{#_Toc157315275}[]{#_Toc157315278}[]{#_Toc157315279}[]{#_Toc157315280}[]{#_Toc157315286}[]{#_Toc157315287}[]{#_Toc157315290}[]{#_Toc157315291}[]{#_Toc157315316}[]{#_display_mld_group}

**MLD \-- MLD配置命令 \-- display mld group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mld** **group**]{lang="EN-US"}]{#struct_0_42457_14668_x2085781766}[命令用来显示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组（即通过]{style="font-family:宋体"}[MLD]{lang="EN-US"}[加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组）的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_551351577}

[**[display]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \] **group** \[ *ipv6-group-address* \| **interface** *interface-type interface-number* \] \[ **static** \| **verbose** \]]{lang="EN-US"}]{#struct_0_42457_14668_x1049865637}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1271522522}

[[任意视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x1383522920}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2053847678}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1403686375}

[[network-operator]{lang="EN-US"}]{#struct_0_42457_14668_x1361244969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_103234118}

[[mdc-operator]{lang="EN-US"}]{#struct_0_42457_14668_341942427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_1063964564}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_42457_14668_397747475}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_42457_14668_621150072}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_42457_14668_1270539482}[：显示指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:
宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_42457_14668_216406777}[：显示静态加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组信息。如果未指定本参数，将只显示动态加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_42457_14668_x725780593}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1702690431}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_323165270}[显示公网实例中动态加入的所有]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld group]{lang="EN-US"}]{#struct_0_42457_14668_x450365935}

[MLD groups in total: 1]{lang="EN-US"}

[ GigabitEthernet1/0/1(FE80::101):]{lang="EN-US"}

[  MLD groups reported in total: 1]{lang="EN-US"}

[   Group address: FF03::101]{lang="EN-US"}

[    Last reporter: FE80::10]{lang="EN-US"}

[    Uptime: 00:02:04]{lang="EN-US"}

[    Expires: 00:01:15]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mld group]{lang="EN-US"}]{#struct_0_42457_14668_x52947200}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1879542867}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_2032855693}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_x408371052}

[[MLD groups in total]{lang="EN-US"}]{#struct_0_42457_14668_x993434207}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1990068079}[组播组的总数]{style="font-family:宋体"}

[[MLD groups reported in total]{lang="EN-US"}]{#struct_0_42457_14668_x52881664}

[[当前接口上动态加入的]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_2058229921}[组播组总数]{style="font-family:宋体"}

[[Group address]{lang="EN-US"}]{#struct_0_42457_14668_x1208727415}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x1134683248}[组播组地址]{style="font-family:宋体"}

[[Last reporter]{lang="EN-US"}]{#struct_0_42457_14668_x1038597584}

[[最后发送报告报文的主机地址]{style="font-family:宋体"}]{#struct_0_42457_14668_x926336199}

[[Uptime]{lang="EN-US"}]{#struct_0_42457_14668_x52816128}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x1860209305}[组播组的运行时间]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_42457_14668_x1492045022}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x333085529}[组播组的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[ # ]{lang="EN-US"}]{#struct_0_42457_14668_x1092993796}[显示公网实例中动态加入的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF3E::101]{lang="EN-US"}[的详细信息（假设当前运行]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display mld group ff3e::101 verbose]{lang="EN-US"}]{#struct_0_42457_14668_1270605018}

[ GigabitEthernet1/0/1(FE80::101):]{lang="EN-US"}

[  MLD groups reported in total: 1]{lang="EN-US"}

[   Group: FF3E::101]{lang="EN-US"}

[     Uptime: 00:01:46]{lang="EN-US"}

[     Exclude expires: 00:04:16]{lang="EN-US"}

[     Mapping expires: 00:02:16]{lang="EN-US"}

[     Last reporter: FE80::10]{lang="EN-US"}

[     Last-listener-query-counter: 0]{lang="EN-US"}

[     Last-listener-query-timer-expiry: Off]{lang="EN-US"}

[     Mapping last-listener-query-counter: 0]{lang="EN-US"}

[     Mapping last-listener-query-timer-expiry: Off]{lang="EN-US"}

[     Group mode: Exclude]{lang="EN-US"}

[     Version1-host-present-timer-expiry: Off]{lang="EN-US"}

[     Source list (sources in total: 1):]{lang="EN-US"}

[       Source: 10::10]{lang="EN-US"}

[          Uptime: 00:00:09]{lang="EN-US"}

[          V2 expires: 00:04:11]{lang="EN-US"}

[          Mapping expires: 00:02:16]{lang="EN-US"}

[          Last-listener-query-counter: 0]{lang="EN-US"}

[          Last-listener-query-timer-expiry: Off]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display mld group verbose]{lang="EN-US"}]{#struct_0_42457_14668_x635006315}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1463568426}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_x1751910279}

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_1890006510}

[[MLD groups reported in total]{lang="EN-US"}]{#struct_0_42457_14668_x2044968478}

[[当前接口上动态加入的]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1305564005}[组播组总数]{style="font-family:宋体"}

[[Group]{lang="EN-US"}]{#struct_0_42457_14668_x1543113293}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1271063771}[组播组地址]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_42457_14668_188586415}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x494057255}[组播组的运行时间]{style="font-family:宋体"}

[[Exclude expires]{lang="EN-US"}]{#struct_0_42457_14668_1620810199}

[[EXCLUDE]{lang="EN-US"}]{#struct_0_42457_14668_1271129307}[模式下]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[[Mapping expires]{lang="EN-US"}]{#struct_0_42457_14668_x1908441575}

[[MLD SSM Mapping]{lang="EN-US"}]{#struct_0_42457_14668_1732371403}[规则所生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的超时时间。只有运行]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Last reporter]{lang="EN-US"}]{#struct_0_42457_14668_x189260939}

[[最后发送报告报文的主机地址]{style="font-family:宋体"}]{#struct_0_42457_14668_x1124645819}

[[Last-listener-query-counter]{lang="EN-US"}]{#struct_0_42457_14668_x2142660891}

[[最后组成员查询次数]{style="font-family:宋体"}]{#struct_0_42457_14668_x1591530731}

[[Last-listener-query-timer-expiry]{lang="EN-US"}]{#struct_0_42457_14668_x2119279034}

[[最后组成员查询定时器的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}]{#struct_0_42457_14668_1271194843}[表示该定时器关闭]{style="font-family:宋体"}

[[Mapping last-listener-query-counter]{lang="EN-US"}]{#struct_0_42457_14668_1732305867}

[[MLD SSM Mapping]{lang="EN-US"}]{#struct_0_42457_14668_2112015928}[规则所生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的最后组成员查询次数。只有运行]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Mapping last-listener-query-timer-expiry]{lang="EN-US"}]{#struct_0_42457_14668_1732240331}

[[MLD SSM Mapping]{lang="EN-US"}]{#struct_0_42457_14668_x1476586149}[规则所生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的最后组成员查询定时器的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Group mode]{lang="EN-US"}]{#struct_0_42457_14668_1329661784}

[[对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1017620545}[组播源的过滤模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Include]{lang="EN-US"}]{#struct_0_42457_14668_x761592609}[：表示]{lang="EN-US" style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exclude]{lang="EN-US"}]{#struct_0_42457_14668_x455603622}[：表示]{lang="EN-US" style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}[，对于未运行]{style="font-family:宋体"}[MLD]{lang="EN-US"}[ SSM Mapping]{lang="EN-US"}[的]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}[，也显示为本模式]{style="font-family:宋体"}

[[MLDv1]{lang="EN-US"}]{#struct_0_42457_14668_1889970112}[本身并不区分过滤模式，但当运行]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时，会根据具体配置以及加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组来显示相应的模式；而当未运行]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时，则固定显示为]{style="font-family:宋体"}[Exclude]{lang="EN-US"}

[[Version1-host-present-timer-expiry]{lang="EN-US"}]{#struct_0_42457_14668_1271260379}

[[MLDv1]{lang="EN-US"}]{#struct_0_42457_14668_x1407371958}[主机超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Source list (sources in total: 1)]{lang="EN-US"}]{#struct_0_42457_14668_1941594076}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1948676290}[组播源列表及总数。只有运行]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[或]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_42457_14668_x52095233}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x52685062}[组播源地址。只有运行]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[或]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_42457_14668_630653405}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x52619526}[组播源的运行时间。只有运行]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[或]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[V2 expires]{lang="EN-US"}]{#struct_0_42457_14668_243311361}

[[MLDv2]{lang="EN-US"}]{#struct_0_42457_14668_57769171}[组播源的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭，"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["表示该组播源由]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[规则生成。只有运行]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[或]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Mapping expires]{lang="EN-US"}]{#struct_0_42457_14668_x52553990}

[[MLD SSM Mapping]{lang="EN-US"}]{#struct_0_42457_14668_x787342677}[规则所生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的超时时间。只有运行]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Last-listener-query-counter]{lang="EN-US"}]{#struct_0_42457_14668_x52488454}

[[最后源组成员查询次数。只有运行]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}]{#struct_0_42457_14668_x30199957}[或]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Last-listener-query-timer-expiry]{lang="EN-US"}]{#struct_0_42457_14668_x52947206}

[[最后源组成员查询定时器的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}]{#struct_0_42457_14668_2032855699}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[或]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x409026412}[显示公网实例中静态加入的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld group static]{lang="EN-US"}]{#struct_0_42457_14668_x52881670}

[ Entries in total: 2]{lang="EN-US"}

[  (\*, FF03::101)]{lang="EN-US"}

[   Interface: GE1/0/1]{lang="EN-US"}

[   Expires: Never]{lang="EN-US"}

[ ]{lang="EN-US"}

[  (2001::101, FF3E::202)]{lang="EN-US"}

[   Interface: GE1/0/1]{lang="EN-US"}

[   Expires: Never]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display mld group static]{lang="EN-US"}]{#struct_0_42457_14668_101914789}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1932924665}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_x1399555686}

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_x52816134}

[[Entries in total]{lang="EN-US"}]{#struct_0_42457_14668_478442859}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x52750598}[组播组的总数]{style="font-family:宋体"}

[[(\*, FF03::101)]{lang="EN-US"}]{#struct_0_42457_14668_x144858257}

[[（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_42457_14668_x825641307}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[(2001::101, FF3E::202)]{lang="EN-US"}]{#struct_0_42457_14668_x52160774}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_42457_14668_x1697084158}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_42457_14668_x1435226151}

[[接口名称]{style="font-family:宋体"}]{#struct_0_42457_14668_x52095238}

[[Expires]{lang="EN-US"}]{#struct_0_42457_14668_1799416570}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x52685063}[组播组的超时时间，固定显示为]{style="font-family:宋体"}[Never]{lang="EN-US"}[，表示永不超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc136854346}[]{#struct_0_42457_14668_581014268}[]{#_display_mld_interface}[]{#_Toc296159307}[]{#_Toc299378839}[]{#_Toc296159308}[]{#_Toc299378840}[]{#_Toc296159309}[]{#_Toc299378841}[]{#_Toc296159310}[]{#_Toc299378842}[]{#_Toc296159311}[]{#_Toc299378843}[]{#_Toc296159312}[]{#_Toc299378844}[]{#_Toc296159313}[]{#_Toc299378845}[]{#_Toc296159314}[]{#_Toc299378846}[]{#_Toc296159315}[]{#_Toc299378847}[]{#_Toc296159316}[]{#_Toc299378848}[]{#_Toc296159317}[]{#_Toc299378849}[]{#_Toc296159318}[]{#_Toc299378850}[]{#_Toc296159319}[]{#_Toc299378851}[]{#_Toc296159320}[]{#_Toc299378852}[]{#_Toc296159321}[]{#_Toc299378853}[]{#_Toc296159322}[]{#_Toc299378854}[]{#_Toc296159323}[]{#_Toc299378855}[]{#_Toc296159324}[]{#_Toc299378856}[]{#_Toc296159325}[]{#_Toc299378857}[]{#_Toc296159326}[]{#_Toc299378858}[]{#_Toc296159327}[]{#_Toc299378859}[]{#_Toc296159328}[]{#_Toc299378860}[]{#_Toc296159329}[]{#_Toc299378861}[]{#_Toc296159330}[]{#_Toc299378862}[]{#_Toc296159331}[]{#_Toc299378863}[]{#_Toc296159332}[]{#_Toc299378864}[]{#_Toc296159333}[]{#_Toc299378865}[]{#_Toc296159334}[]{#_Toc299378866}[]{#_Toc296159335}[]{#_Toc299378867}[]{#_Toc296159336}[]{#_Toc299378868}[]{#_Toc296159340}[]{#_Toc299378872}[]{#_Toc296159347}[]{#_Toc299378879}[]{#_Toc296159348}[]{#_Toc299378880}[]{#_Toc296159350}[]{#_Toc299378882}[]{#_Toc296159358}[]{#_Toc299378890}[]{#_Toc296159359}[]{#_Toc299378891}[]{#_Toc296159405}[]{#_Toc299378937}[]{#_Toc296159407}[]{#_Toc299378939}[]{#_Toc296159408}[]{#_Toc299378940}[]{#_Toc296159409}[]{#_Toc299378941}[]{#_Toc296159410}[]{#_Toc299378942}[]{#_Toc296159411}[]{#_Toc299378943}[]{#_Toc296159412}[]{#_Toc299378944}[]{#_Toc296159413}[]{#_Toc299378945}[]{#_Toc296159414}[]{#_Toc299378946}[]{#_Toc296159415}[]{#_Toc299378947}[]{#_Toc296159416}[]{#_Toc299378948}[]{#_Toc296159417}[]{#_Toc299378949}[]{#_Toc296159418}[]{#_Toc299378950}[]{#_Toc296159419}[]{#_Toc299378951}[]{#_Toc296159420}[]{#_Toc299378952}[]{#_Toc296159421}[]{#_Toc299378953}[]{#_Toc296159422}[]{#_Toc299378954}[]{#_Toc296159423}[]{#_Toc299378955}[]{#_Toc296159424}[]{#_Toc299378956}[]{#_Toc296159425}[]{#_Toc299378957}[]{#_Toc296159426}[]{#_Toc299378958}[]{#_Toc296159427}[]{#_Toc299378959}[]{#_Toc296159432}[]{#_Toc299378964}[]{#_Toc296159451}[]{#_Toc299378983}[]{#_Toc296159453}[]{#_Toc299378985}[]{#_Toc296159454}[]{#_Toc299378986}[]{#_Toc296159455}[]{#_Toc299378987}[]{#_Toc296159456}[]{#_Toc299378988}[]{#_Toc296159457}[]{#_Toc299378989}[]{#_Toc296159458}[]{#_Toc299378990}[]{#_Toc296159459}[]{#_Toc299378991}[]{#_Toc296159460}[]{#_Toc299378992}[]{#_Toc296159461}[]{#_Toc299378993}[]{#_Toc296159462}[]{#_Toc299378994}[]{#_Toc296159463}[]{#_Toc299378995}[]{#_Toc296159464}[]{#_Toc299378996}[]{#_Toc296159465}[]{#_Toc299378997}[]{#_Toc296159466}[]{#_Toc299378998}[]{#_Toc296159467}[]{#_Toc299378999}[]{#_Toc296159468}[]{#_Toc299379000}[]{#_Toc296159469}[]{#_Toc299379001}[]{#_Toc296159470}[]{#_Toc299379002}[]{#_Toc296159471}[]{#_Toc299379003}[]{#_Toc296159472}[]{#_Toc299379004}[]{#_Toc296159473}[]{#_Toc299379005}[]{#_Toc296159474}[]{#_Toc299379006}[]{#_Toc296159475}[]{#_Toc299379007}[]{#_Toc296159476}[]{#_Toc299379008}[]{#_Toc296159477}[]{#_Toc299379009}[]{#_Toc296159478}[]{#_Toc299379010}[]{#_Toc296159479}[]{#_Toc299379011}[]{#_Toc296159480}[]{#_Toc299379012}[]{#_Toc296159481}[]{#_Toc299379013}[]{#_Toc296159482}[]{#_Toc299379014}[]{#_Toc296159483}[]{#_Toc299379015}[]{#_Toc296159485}[]{#_Toc299379017}[]{#_Toc296159492}[]{#_Toc299379024}[]{#_Toc296159493}[]{#_Toc299379025}[]{#_Toc296159515}[]{#_Toc299379047}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_42457_14668_x1061352748}**[mld]{lang="EN-US"}**[ **group**]{lang="EN-US"}

::: {#551905968 .myid}
[]{#_Toc404790275}[]{#struct_0_42457_14668_311606389}

**MLD \-- MLD配置命令 \-- display mld interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mld** **interface**]{lang="EN-US"}]{#struct_0_42457_14668_218537689}[命令用来显示接口上]{style="font-family:宋体"}[MLD]{lang="EN-US"}[配置和运行的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1552591989}

[**[display]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \] **interface** \[ *interface-type interface-number* \] \[ **proxy** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_42457_14668_917773626}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_99225174}

[[任意视图]{style="font-family:宋体"}]{#struct_0_42457_14668_1271391451}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1334952076}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1824455981}

[[network-operator]{lang="EN-US"}]{#struct_0_42457_14668_1413600659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1907623134}

[[mdc-operator]{lang="EN-US"}]{#struct_0_42457_14668_559066890}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1014586474}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_42457_14668_814091267}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_42457_14668_1271456987}[：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[**[proxy]{lang="EN-US"}**]{#struct_0_42457_14668_1732961227}[：显示代理接口的信息。如果未指定本参数，将显示所有接口的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_42457_14668_162197549}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x821373714}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1617583817}[显示公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（非代理接口）上]{style="font-family:宋体"}[MLD]{lang="EN-US"}[配置和运行的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}]{#struct_0_42457_14668_1271522523}

[ GigabitEthernet1/0/1(FE80::200:AFF:FE01:101):]{lang="EN-US"}

[   MLD is enabled.]{lang="EN-US"}

[   MLD version: 1]{lang="EN-US"}

[   Query interval for MLD: 125s]{lang="EN-US"}

[   Other querier present time for MLD: 255s]{lang="EN-US"}

[   Maximum query response time for MLD: 10s]{lang="EN-US"}

[   Last listener query interval: 1s]{lang="EN-US"}

[   Last listener query count: 2]{lang="EN-US"}

[   Startup query interval: 31s]{lang="EN-US"}

[   Startup query count: 2]{lang="EN-US"}

[   General query timer expiry (hh:mm:ss): 00:00:23]{lang="EN-US"}

[   Querier for MLD: FE80::200:AFF:FE01:101 (This router)]{lang="EN-US"}

[   MLD activity: 1 join(s), 0 done(s)]{lang="EN-US"}

[   IPv6 multicast routing on this interface: Enabled]{lang="EN-US"}

[   Robustness: 2]{lang="EN-US"}

[   Require-router-alert: Disabled]{lang="EN-US"}

[   Fast-leave: Disabled]{lang="EN-US"}

[   Startup-query: Off]{lang="EN-US"}

[   Other-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--]{lang="EN-US"}

[   Authorization: Disabled]{lang="EN-US"}

[   Join-by-session: Disabled]{lang="EN-US"}

[   User-VLAN-aggregation: Disabled]{lang="EN-US"}

[  MLD groups reported in total: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1732436938}[显示公网实例所有代理接口上]{style="font-family:宋体"}[MLD]{lang="EN-US"}[配置和运行的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld interface proxy verbose]{lang="EN-US"}]{#struct_0_42457_14668_x257676445}

[ GigabitEthernet1/0/2(FE80::100:CEF:FE01:101):]{lang="EN-US"}

[   MLD proxy is enabled.]{lang="EN-US"}

[   MLD version: 1]{lang="EN-US"}

[   IPv6 multicast routing on this interface: Enabled]{lang="EN-US"}

[   Require-router-alert: Disabled]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display mld interface]{lang="EN-US"}]{#struct_0_42457_14668_x1383588456}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1761233514}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_x771986655}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_x1114259840}

[[GigabitEthernet1/0/1(FE80::200:AFF:FE01:101)]{lang="EN-US"}]{#struct_0_42457_14668_x857020953}

[[接口的名称和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1463087520}[链路本地地址]{style="font-family:宋体"}

[[MLD is enabled]{lang="EN-US"}]{#struct_0_42457_14668_x301366261}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1270539483}[已使能]{style="font-family:宋体"}

[[MLD version]{lang="EN-US"}]{#struct_0_42457_14668_216472313}

[[此接口运行的]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_869901566}[版本]{style="font-family:宋体"}

[[Query interval for MLD]{lang="EN-US"}]{#struct_0_42457_14668_x11612148}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x610968201}[普遍组查询报文的发送间隔（秒）]{style="font-family:宋体"}

[[Other querier present time for MLD]{lang="EN-US"}]{#struct_0_42457_14668_317093849}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1270605019}[其它查询器的存在时间（秒）]{style="font-family:宋体"}

[[Maximum query response time for MLD]{lang="EN-US"}]{#struct_0_42457_14668_x635071851}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1415277840}[普遍组查询报文的最大响应时间（秒）]{style="font-family:宋体"}

[[Last listener query interval]{lang="EN-US"}]{#struct_0_42457_14668_x1300530682}

[[最后组成员查询间隔（秒）]{style="font-family:宋体"}]{#struct_0_42457_14668_x1464677137}

[[Last listener query count]{lang="EN-US"}]{#struct_0_42457_14668_392769084}

[[最后组成员查询次数]{style="font-family:宋体"}]{#struct_0_42457_14668_x1702089820}

[[Startup query interval]{lang="EN-US"}]{#struct_0_42457_14668_357355937}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1271063768}[查询器启动查询间隔（秒）]{style="font-family:宋体"}

[[Startup query count]{lang="EN-US"}]{#struct_0_42457_14668_556902824}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_325033451}[查询器启动查询次数]{style="font-family:宋体"}

[[General query timer expiry]{lang="EN-US"}]{#struct_0_42457_14668_x697153085}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_587122632}[普遍组查询的超时时间，]{style="font-family:宋体"}[off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[[Querier for MLD]{lang="EN-US"}]{#struct_0_42457_14668_1271129304}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x189064331}[查询器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址]{style="font-family:宋体"}

[[MLD activity: 1 join(s), 0 done(s)]{lang="EN-US"}]{#struct_0_42457_14668_54466163}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1485211655}[的活动统计：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[join(s)]{lang="EN-US"}]{#struct_0_42457_14668_506147236}[：表示加入过的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{lang="EN-US" style="font-family:宋体"}[总数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[done(s)]{lang="EN-US"}]{#struct_0_42457_14668_1271194840}[：表示离开过的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{lang="EN-US" style="font-family:宋体"}[总数]{style="font-family:宋体"}

[[IPv6 multicast routing on this interface]{lang="EN-US"}]{#struct_0_42457_14668_1329727320}

[[是否使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_610582246}[组播路由功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_42457_14668_167386677}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_42457_14668_2077028263}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Robustness]{lang="EN-US"}]{#struct_0_42457_14668_1271260376}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1408223926}[查询器的健壮系数]{style="font-family:宋体"}

[[Require-router-alert]{lang="EN-US"}]{#struct_0_42457_14668_x607325966}

[[是否使能丢弃未携带]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}]{#struct_0_42457_14668_567818273}[选项的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_42457_14668_1271325912}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_42457_14668_580686588}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Fast-leave]{lang="EN-US"}]{#struct_0_42457_14668_x26322819}

[[是否使能快速离开功能：]{style="font-family:宋体"}]{#struct_0_42457_14668_1117879233}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_42457_14668_1271391448}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_42457_14668_1335410827}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Startup-query]{lang="EN-US"}]{#struct_0_42457_14668_1780757402}

[[是否处于启动查询状态：]{style="font-family:宋体"}]{#struct_0_42457_14668_189781217}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_42457_14668_1271522520}[：表示处于启动查询状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_42457_14668_x1383391848}[：表示未处于启动查询状态]{style="font-family:宋体"}

[[Other-querier-present-timer-expiry]{lang="EN-US"}]{#struct_0_42457_14668_x654610608}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1270539480}[其它查询器的存在超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[[Authorization]{lang="EN-US"}]{#struct_0_42457_14668_1959180702}

[[是否使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x38853390}[可控组播功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_42457_14668_x107818960}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_42457_14668_1959246238}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_42457_14668_x52750599}

[[Join-by-session]{lang="EN-US"}]{#struct_0_42457_14668_x448173650}

[[是否使能按会话记录用户加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_427203629}[组播组：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_42457_14668_1959049630}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_42457_14668_x96578225}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_42457_14668_x52160775}

[[User-VLAN-aggregation]{lang="EN-US"}]{#struct_0_42457_14668_1778387610}

[[是否使能为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1959115166}[组播报文封装]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_42457_14668_x430776851}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_42457_14668_1958918558}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_42457_14668_x52095239}

[[MLD groups reported in total]{lang="EN-US"}]{#struct_0_42457_14668_851867887}

[[此接口上动态加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1270605016}[组播组数量。没有加入组时不显示本字段]{style="font-family:宋体"}

[[MLD proxy is enabled]{lang="EN-US"}]{#struct_0_42457_14668_1732961226}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1732895690}[代理功能已使能]{style="font-family:宋体"}

[[Version1-querier-present-timer-expiry]{lang="EN-US"}]{#struct_0_42457_14668_1732436937}

[[MLDv1]{lang="EN-US"}]{#struct_0_42457_14668_1732371401}[查询器的存在超时时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1887003520 .myid}
[]{#_Toc404790276}[]{#struct_0_42457_14668_1732305865}[]{#_Toc364955773}[]{#_Toc355963320}

**MLD \-- MLD配置命令 \-- display mld proxy group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mld** **proxy** **group**]{lang="EN-US"}]{#struct_0_42457_14668_2111884856}[命令用来显示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理记录的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_2111818253}

[**[display]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \] **proxy** **group** \[ *ipv6-group-address*]{lang="EN-US"}[ \| **interface** *interface-type* *interface-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_42457_14668_1732240329}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1476061862}

[[任意视图]{style="font-family:宋体"}]{#struct_0_42457_14668_1732699081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_2039170333}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1732633545}

[[network-operator]{lang="EN-US"}]{#struct_0_42457_14668_103385455}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1913733546}

[[mdc-operator]{lang="EN-US"}]{#struct_0_42457_14668_1732568009}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_442480975}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_42457_14668_1732502473}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[ipv6-]{lang="EN-US"}[group-address]{lang="EN-US"}*]{#struct_0_42457_14668_504298922}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_42457_14668_1732961225}[：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_42457_14668_2034933594}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1732895689}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1025520365}[显示公网实例中]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理记录的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld proxy group]{lang="EN-US"}]{#struct_0_42457_14668_166353001}

[MLD proxy group records in total: 2]{lang="EN-US"}

[ GigabitEthernet1/0/1(FE80::16:1):]{lang="EN-US"}

[  MLD proxy group records in total: 2]{lang="EN-US"}

[   Group address: FF1E::1]{lang="EN-US"}

[    Member state: Idle]{lang="EN-US"}

[    Expires: Off]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Group address: FF1E::2]{lang="EN-US"}

[    Member state: Idle]{lang="EN-US"}

[    Expires: Off]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x765504729}[显示公网实例中]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理记录的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld proxy group ff1e::1 verbose]{lang="EN-US"}]{#struct_0_42457_14668_166287465}

[ GigabitEthernet1/0/1(FE80::16:1):]{lang="EN-US"}

[  MLD proxy group records in total: 2]{lang="EN-US"}

[   Group: FF1E::1]{lang="EN-US"}

[     Group mode: Include]{lang="EN-US"}

[     Member state: Idle]{lang="EN-US"}

[     Expires: Off]{lang="EN-US"}

[     Source list (sources in total: 1):]{lang="EN-US"}

[       100::1]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display mld proxy group]{lang="EN-US"}]{#struct_0_42457_14668_402400564}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1567769352}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_166221929}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_166156393}

[[MLD proxy group records in total]{lang="ES-AR"}]{#struct_0_42457_14668_166615145}

[[MLD]{lang="ES-AR"}]{#struct_0_42457_14668_166549609}[代理记录的]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[组播组总数]{style="font-family:宋体"}

[[GigabitEthernet1/0/1(FE80::16:1)]{lang="EN-US"}]{#struct_0_42457_14668_166484073}

[[MLD]{lang="ES-AR"}]{#struct_0_42457_14668_1441419974}[代理接口的名称和]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[地址]{style="font-family:宋体"}

[[Pending proxy group]{lang="EN-US"}]{#struct_0_42457_14668_166418537}

[[等待生效的代理组]{style="font-family:宋体"}]{#struct_0_42457_14668_166877289}

[[Group address/Group]{lang="EN-US"}]{#struct_0_42457_14668_166811753}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_166353000}[组播组地址]{style="font-family:宋体"}

[[Member state]{lang="EN-US"}]{#struct_0_42457_14668_166287464}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_402400563}[组播组成员的状态，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delay]{lang="EN-US"}]{#struct_0_42457_14668_166221928}[：表示加入了一个组，并对该组启动了延迟发送报告报文的定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_42457_14668_166156392}[：表示加入了一个组，但对该组尚未启动延迟发送报告报文的定时器]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_42457_14668_166615144}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_166549608}[组播组延迟发送报告报文的时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[[Group mode]{lang="ES-AR"}]{#struct_0_42457_14668_166484072}

[[对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_166418536}[组播源的过滤模式，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Include]{lang="EN-US"}]{#struct_0_42457_14668_1410308793}[：表示]{lang="EN-US" style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exclude]{lang="EN-US"}]{#struct_0_42457_14668_166877288}[：表示]{lang="EN-US" style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Source list]{lang="EN-US"}]{#struct_0_42457_14668_166811752}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_166352999}[代理的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组所包含的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源列表]{style="font-family:宋体"}

[[sources in total]{lang="EN-US"}]{#struct_0_42457_14668_166287463}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_166221927}[组播源的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1845000922 .myid}
[]{#_Toc404790277}[]{#struct_0_42457_14668_1201152979}[]{#_Toc364955774}[]{#_Toc355963321}

**MLD \-- MLD配置命令 \-- display mld proxy routing-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mld** **proxy** **routing-table**]{lang="EN-US"}]{#struct_0_42457_14668_166156391}[命令用来显示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理路由表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1003114248}

[**[display]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \] **proxy** **routing-table** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \] \* \[ **verbose** \]]{lang="EN-US"}]{#struct_0_42457_14668_166615143}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1811036088}

[[任意视图]{style="font-family:宋体"}]{#struct_0_42457_14668_166549607}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1325920536}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_76984054}

[[network-operator]{lang="EN-US"}]{#struct_0_42457_14668_166484071}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1441419972}

[[mdc-operator]{lang="EN-US"}]{#struct_0_42457_14668_166418535}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_1410308790}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_42457_14668_166877287}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_42457_14668_x2010039143}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[*[ipv6-]{lang="EN-US"}[group-address]{lang="EN-US"}*]{#struct_0_42457_14668_166811751}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_42457_14668_x1218870296}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址的前缀长度。对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[；对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，其取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_42457_14668_x1519447822}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_166352998}

[[\# ]{lang="FR"}]{#struct_0_42457_14668_2031952627}[显示公网实例]{style="font-family:宋体"}[MLD]{lang="FR"}[代理路由表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld proxy routing-table]{lang="FR"}]{#struct_0_42457_14668_166287462}

[ Total 1 (\*, G) entries, 2 (S, G) entries.]{lang="FR"}

[ ]{lang="FR"}

[ (100::1, FF1E::1)]{lang="FR"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="FR"}

[     Downstream interfaces (1 in total):]{lang="FR"}

[         1: Vlan-interface2]{lang="FR"}

[             Protocol: MLD]{lang="FR"}

[ ]{lang="FR"}

[ (\*, FF1E::2)]{lang="FR"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="FR"}

[     Downstream interfaces (1 in total):]{lang="FR"}

[         1: Vlan-interface2]{lang="FR"}

[             Protocol: STATIC]{lang="FR"}

[ ]{lang="FR"}

[ (2::2, FF1E::2)]{lang="FR"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="FR"}

[     Downstream interfaces (2 in total):]{lang="FR"}

[         1: LoopBack1]{lang="FR"}

[             Protocol: STATIC]{lang="FR"}

[         2: Vlan-interface2]{lang="FR"}

[             Protocol: PROXY]{lang="FR"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_166221926}[显示公网实例]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理路由表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld proxy routing-table verbose]{lang="EN-US"}]{#struct_0_42457_14668_166156390}

[ Total 1 (\*, G) entries, 2 (S, G) entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (100::1, FF1E::1)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface2]{lang="EN-US"}

[             Protocol: MLD]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state]{lang="EN-US"}[：]{style="font-family:宋体"}[Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Non-downstream interfaces: None]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (\*, FF1E::2)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface2]{lang="EN-US"}

[             Protocol: STATIC]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state]{lang="EN-US"}[：]{style="font-family:宋体"}[Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Non-downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface3]{lang="EN-US"}

[             Protocol: MLD]{lang="EN-US"}

[             Querier state: Non-querier]{lang="EN-US"}

[             Join/Prune state]{lang="EN-US"}[：]{style="font-family:宋体"}[Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (2::2, FF1E::2)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (2 in total):]{lang="EN-US"}

[         1: LoopBack1]{lang="EN-US"}

[             Protocol: STATIC]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state: Join]{lang="EN-US"}

[         2: Vlan-interface2]{lang="EN-US"}

[             Protocol: PROXY]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state: Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Non-downstream interfaces: None]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display mld proxy routing-table]{lang="EN-US"}]{#struct_0_42457_14668_166615142}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1549655792}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_166549606}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_x1325920537}

[[Total 1 (\*, G) entries, 2 (S, G) entries]{lang="EN-US"}]{#struct_0_42457_14668_166484070}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_42457_14668_166418534}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项和（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的总数]{style="font-family:宋体"}

[[(100::1, FF1E::1)]{lang="FR"}]{#struct_0_42457_14668_166877286}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_42457_14668_166811750}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Upstream interface]{lang="EN-US"}]{#struct_0_42457_14668_166352997}

[[表项的入接口]{style="font-family:宋体"}]{#struct_0_42457_14668_2031952616}

[[Downstream interfaces (1 in total)]{lang="EN-US"}]{#struct_0_42457_14668_166287461}

[[下游的出接口信息及总数]{style="font-family:宋体"}]{#struct_0_42457_14668_166221925}

[[Non-downstream interfaces (1 in total)]{lang="EN-US"}]{#struct_0_42457_14668_166156389}

[[下游的非出接口信息及总数]{style="font-family:宋体"}]{#struct_0_42457_14668_166615141}

[[1: Vlan-interface2]{lang="EN-US"}]{#struct_0_42457_14668_166549605}

[[索引号为]{style="font-family:宋体"}]{#struct_0_42457_14668_x1325920538}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}

[[Protocol]{lang="EN-US"}]{#struct_0_42457_14668_166484069}

[[接口使用的协议类型：]{style="font-family:宋体"}]{#struct_0_42457_14668_166418533}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_166877285}[：表示动态]{style="font-family:宋体"}[MLD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROXY]{lang="EN-US"}]{#struct_0_42457_14668_166811749}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_42457_14668_166352996}[：表示静态]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}

[[Querier state]{lang="EN-US"}]{#struct_0_42457_14668_2031952617}

[[接口的查询器状态：]{style="font-family:宋体"}]{#struct_0_42457_14668_166287460}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Querier]{lang="EN-US"}]{#struct_0_42457_14668_166221924}[：表示接口为]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Non-querier]{lang="EN-US"}]{#struct_0_42457_14668_166156388}[：表示接口不是]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器]{lang="EN-US" style="font-family:宋体"}

[[Join/Prune state]{lang="EN-US"}]{#struct_0_42457_14668_166615140}

[[接口的加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_42457_14668_166549604}[剪枝状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NI]{lang="EN-US"}]{#struct_0_42457_14668_166484068}[：表示默认状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Join]{lang="EN-US"}]{#struct_0_42457_14668_166418532}[：表示处于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[加入的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Prune]{lang="EN-US"}]{#struct_0_42457_14668_1410308789}[：表示处于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[剪枝的状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1500068686 .myid}
[]{#_Toc404790278}[]{#struct_0_42457_14668_166877284}[]{#_Toc360707118}[]{#_Toc360705929}

**MLD \-- MLD配置命令 \-- display mld ssm-mapping**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mld** **ssm-mapping**]{lang="EN-US"}]{#struct_0_42457_14668_x2010039140}[命令用来显示]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_166811748}

[**[display]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \] **ssm-mapping** *ipv6-group-address*]{lang="EN-US"}]{#struct_0_42457_14668_737444833}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_569637528}

[[任意视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x616061532}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_569571992}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1544957658}

[[network-operator]{lang="EN-US"}]{#struct_0_42457_14668_x1445200982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_569506456}

[[mdc-operator]{lang="EN-US"}]{#struct_0_42457_14668_670571026}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_569440920}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_42457_14668_x50516295}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_42457_14668_569899672}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1967837223}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_569834136}[显示公网实例中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF3E::101]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[\<Sysname\> display mld ssm-mapping ff3e::101]{lang="EN-US"}]{#struct_0_42457_14668_x776088790}

[ Group: FF3E::101]{lang="EN-US"}

[ Source list:]{lang="EN-US"}

[        1::1]{lang="EN-US"}

[        1::2]{lang="EN-US"}

[        10::1]{lang="EN-US"}

[        100::10]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display mld ssm-mapping]{lang="EN-US"}]{#struct_0_42457_14668_569768600}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_782432425}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_1319252388}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_569703064}

[[Group]{lang="EN-US"}]{#struct_0_42457_14668_570161816}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_570096280}[组播组地址]{style="font-family:宋体"}

[[Source list]{lang="EN-US"}]{#struct_0_42457_14668_569637527}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_569571991}[组播源地址列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-685379462 .myid}
[]{#_Toc404790279}[]{#struct_0_42457_14668_1958918557}[]{#_Toc372127973}[]{#_Toc365467127}[]{#_Toc364430855}[]{#_Toc363576219}

**MLD \-- MLD配置命令 \-- display mld user-authorization**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_42457_14668_x455904050}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_42457_14668_x1097654145}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}**[mld]{lang="EN-US"}**[ ]{lang="EN-US"}**[user-authorization]{lang="EN-US"}**]{#struct_0_42457_14668_x481441593}[命令用来显示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[用户的授权信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_2141305228}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}**[mld]{lang="EN-US"}**[ ]{lang="EN-US"}**[user-authorization]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_42457_14668_249223395}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1958984093}

[[任意视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x427404921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1634086638}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x221041689}

[[network-operator]{lang="EN-US"}]{#struct_0_42457_14668_x2143128313}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1208939691}

[[mdc-operator]{lang="EN-US"}]{#struct_0_42457_14668_1958787485}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x788401045}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_42457_14668_1205909896}[：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2107425729}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x767250227}[显示所有]{style="font-family:宋体"}[MLD]{lang="EN-US"}[用户的授权信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld user-authorization]{lang="EN-US"}]{#struct_0_42457_14668_1958853021}

[ Authorized users in total: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[   User name: user1@isp1]{lang="EN-US"}

[   Access type: PPP]{lang="EN-US"}

[   Interface: Virtual-Access0]{lang="EN-US"}

[   Access interface: Virtual-Access0]{lang="EN-US"}

[   Maximum programs for order: 10]{lang="EN-US"}

[   User profile: profile1]{lang="EN-US"}

[   Authorized programs list:]{lang="EN-US"}

[     FF03::101]{lang="EN-US"}

[ ]{lang="EN-US"}

[   User name: user2]{lang="EN-US"}

[   Access type: IPoE]{lang="EN-US"}

[   Interface: Multicast-UA0]{lang="EN-US"}

[   Access interface: GigabitEthernet1/0/1.1]{lang="EN-US"}

[   VLAN ID: 100]{lang="EN-US"}

[   Second VLAN ID: 10]{lang="EN-US"}

[   Maximum programs for order: 10]{lang="EN-US"}

[   User profile: profile1]{lang="EN-US"}

[   Authorized programs list:]{lang="EN-US"}

[     FF03::101]{lang="EN-US"}

[     FF03::102]{lang="EN-US"}

[     FF03::103]{lang="EN-US"}

[ ]{lang="EN-US"}

[   User name: user3]{lang="EN-US"}

[   Access type: Portal]{lang="EN-US"}

[   Interface: Multicast-UA1]{lang="EN-US"}

[   Access interface: GigabitEthernet1/0/2]{lang="EN-US"}

[   Maximum programs for order: 10]{lang="EN-US"}

[   User profile: profile1]{lang="EN-US"}

[   Authorized programs list:]{lang="EN-US"}

[     FF03::101]{lang="EN-US"}

[     FF03::103]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display mld user-authorization]{lang="EN-US"}]{#struct_0_42457_14668_1959704989}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x74802170}[[字段]{style="font-family:黑体"}]{#struct_0_42457_14668_x469347780}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_42457_14668_x282504920}

[[Authorized users in total]{lang="EN-US"}]{#struct_0_42457_14668_973739829}

[[接入用户总数]{style="font-family:宋体"}]{#struct_0_42457_14668_1959770525}

[[User name]{lang="EN-US"}]{#struct_0_42457_14668_x438885198}

[[用户名]{style="font-family:宋体"}]{#struct_0_42457_14668_x1147823081}

[[Access type]{lang="EN-US"}]{#struct_0_42457_14668_1959180700}

[[用户接入的方式：]{style="font-family:宋体"}]{#struct_0_42457_14668_x38722318}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPoE]{lang="EN-US"}]{#struct_0_42457_14668_x1831415899}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Portal]{lang="EN-US"}]{#struct_0_42457_14668_1604898222}[：表示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_42457_14668_1959246236}[：表示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[方式]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_42457_14668_x448042578}

[[用户接口]{style="font-family:宋体"}]{#struct_0_42457_14668_425142065}

[[Access interface]{lang="EN-US"}]{#struct_0_42457_14668_1959049628}

[[用户接入的实际接口]{style="font-family:宋体"}]{#struct_0_42457_14668_x97102512}

[[VLAN ID]{lang="EN-US"}]{#struct_0_42457_14668_x1753260178}

[[用户带]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_42457_14668_1959115164}[接入时所携带的第一层（或唯一一层）]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Second VLAN ID]{lang="EN-US"}]{#struct_0_42457_14668_x430907923}

[[用户带]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_42457_14668_1403094309}[接入时所携带的第二层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Maximum programs for order]{lang="EN-US"}]{#struct_0_42457_14668_x193268138}

[[允许用户加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1958918556}[组播组的最大数量]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_42457_14668_x481376057}

[[用户授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_42457_14668_x622383676}[名称，用户可加入该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下通过]{style="font-family:宋体"}**[mld]{lang="EN-US"}**[ **access-policy**]{lang="EN-US"}[命令所配置接入策略中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}

[[Authorized programs list]{lang="EN-US"}]{#struct_0_42457_14668_1958984092}

[[用户授权加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x427470457}[组播组列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#911026809 .myid}
[]{#_Toc404790280}[]{#struct_0_42457_14668_x288095909}[]{#_Toc372212375}[]{#_Toc372205816}[]{#_Toc371343405}[]{#_Toc368325565}[]{#_Toc368294504}

**MLD \-- MLD配置命令 \-- last-listener-query-count (MLD view)**

------------------------------------------------------------------------

[**[last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x713716979}[命令用来全局配置]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[最后组成员查询次数。]{style="font-family:宋体"}

[**[undo last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_1958787484}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x788466581}

[**[last-listener-query-count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_42457_14668_1194798631}

[**[undo last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x654068873}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x859138437}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1826449699}[最后组成员查询次数等于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1958853020}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x2015246790}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x504643997}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1879080209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1303497465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_735890717}

[*[count]{lang="EN-US"}*]{#struct_0_42457_14668_1959704988}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x469413316}

[[本命令与]{style="font-family:宋体"}**[mld last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x1853718764}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1352114251}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1840557429}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1959770524}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] last-listener-query-count 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x438819662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld ]{lang="EN-US"}[last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x1929440430}
:::

::: {#2034835825 .myid}
[]{#_Toc404790281}[]{#struct_0_42457_14668_613331651}[]{#_Toc372212376}[]{#_Toc372205817}[]{#_Toc371343406}[]{#_Toc368325566}[]{#_Toc368294505}

**MLD \-- MLD配置命令 \-- last-listener-query-interval (MLD view)**

------------------------------------------------------------------------

[**[last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x1423897156}[命令用来全局配置]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[最后组成员查询间隔。]{style="font-family:宋体"}

[**[undo last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x153583608}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1959180699}

[**[last-listener-query-interval]{lang="EN-US"}***[ ]{lang="EN-US"}[interval]{lang="EN-US"}*]{#struct_0_42457_14668_x1995496213}

[**[undo last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x1416746051}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_655370170}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_357011945}[最后组成员查询间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x143846675}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1959246235}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x447845970}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x205605890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x138463054}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_97670961}

[*[interval]{lang="EN-US"}*]{#struct_0_42457_14668_923336857}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_1959049627}

[[本命令与]{style="font-family:宋体"}**[mld last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x96905904}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x851316705}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x434948474}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1856079819}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] last-listener-query-interval 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1959115163}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld ]{lang="EN-US"}[last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x431104531}
:::

::: {#769069036 .myid}
[]{#_Toc404790282}[]{#struct_0_42457_14668_x159314013}[]{#_Toc372212377}[]{#_Toc372205818}[]{#_Toc371343407}[]{#_Toc368325567}[]{#_Toc368294506}

**MLD \-- MLD配置命令 \-- max-response-time (MLD view)**

------------------------------------------------------------------------

[**[max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_x162390083}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的最大响应时间。]{style="font-family:宋体"}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_x1358028565}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1611097915}

[**[max-response-time]{lang="EN-US"}***[ time]{lang="EN-US"}*]{#struct_0_42457_14668_1958918555}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_x481572665}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_964778903}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1181254900}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1668605269}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x41575798}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1958984091}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x427273849}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1601986179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1389687811}

[*[time]{lang="EN-US"}*]{#struct_0_42457_14668_220144868}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3174]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_1958787483}

[[本命令与]{style="font-family:宋体"}**[mld max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_x788794261}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_431363962}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x542170841}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1434587334}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] max-response-time 25]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1232947546}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld]{lang="EN-US"}**]{#struct_0_42457_14668_1958853019}[ ]{lang="EN-US"}**[max-response-time]{lang="EN-US"}**
:::

::: {#-1028698951 .myid}
[]{#_Toc404790283}[]{#struct_0_42457_14668_1544957659}

**MLD \-- MLD配置命令 \-- mld**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**]{#struct_0_42457_14668_569506455}[命令用来进入]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld**]{lang="EN-US"}]{#struct_0_42457_14668_670571025}[命令用来清除]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_569440919}

[**[mld]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_42457_14668_x1624494414}

[**[undo]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_42457_14668_x275192016}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_569899671}

[[系统视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x1967837226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_569834135}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x776088789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_569768599}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1056135624}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_42457_14668_569703063}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1907800200}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_945234658}[进入公网实例的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_570096279}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1170724705}[进入]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_569637526}

[\[Sysname\] mld vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-mld-mvpn\]]{lang="EN-US"}
:::

::::: {#-1845926589 .myid}
[]{#_Toc404790284}[]{#struct_0_42457_14668_1959704987}[]{#_Toc372127975}[]{#_Toc365467129}[]{#_Toc364430856}[]{#_Toc363576229}

**MLD \-- MLD配置命令 \-- mld access-policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_42457_14668_x455772975}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_42457_14668_494733685}
:::

[ ]{lang="EN-US"}

[**[mld]{lang="EN-US"}**[ **access-policy**]{lang="EN-US"}]{#struct_0_42457_14668_x469740996}[命令用来配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[用户的接入策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[mld]{lang="EN-US"}**[ **access-policy**]{lang="EN-US"}]{#struct_0_42457_14668_x293002896}[命令用来删除]{style="font-family:宋体"}[MLD]{lang="EN-US"}[用户的接入策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1959770523}

[**[mld]{lang="EN-US"}**[ **access-policy** *acl6-number*]{lang="EN-US"}]{#struct_0_42457_14668_x438754126}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[mld]{lang="EN-US"}**[ **access-policy** *acl6-number*]{lang="EN-US"}]{#struct_0_42457_14668_1611665484}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x40410437}

[[没有配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x311573690}[用户的接入策略，即]{style="font-family:宋体"}[MLD]{lang="EN-US"}[用户未被授权加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1959180706}

[[User-Profile]{lang="EN-US"}]{#struct_0_42457_14668_x38591246}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1722590189}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x500309545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x676787569}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x169653846}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_42457_14668_1959246242}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}[MLD]{lang="EN-US"}[用户只能加入该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x447780427}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_42457_14668_x474248864}[IPv6]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1715053313}[IPv]{lang="DA"}[6]{lang="DA"}[高级]{lang="EN-US" style="font-family:
宋体"}[ACL]{lang="DA"}[，]{lang="EN-US" style="font-family:宋体"}[该]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{lang="EN-US" style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[MLDv1]{lang="DA"}[报文和未携带]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[MLDv2]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[视其]{lang="EN-US" style="font-family:
宋体"}[IPv6]{lang="DA"}[组播源地址为]{lang="EN-US" style="font-family:宋体"}[0::0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}**[destination]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:
宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过多次执行本命令可以配置多条]{style="font-family:宋体"}]{#struct_0_42457_14668_x596962957}[MLD]{lang="EN-US"}[用户接入策略，用户发送的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文只需匹配其中一条就允许通过。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1014743730}

[[\#]{lang="EN-US"}]{#struct_0_42457_14668_x987971964}[[ ]{lang="EN-US"}]{#_Toc80176819}[在名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下配置只允许]{style="font-family:宋体"}[MLD]{lang="EN-US"}[用户加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1959049634}

[\[Sysname\] acl ipv6 basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule permit source ff03::101 0]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] user-profile abc]{lang="EN-US"}

[\[Sysname-user-profile-abc\] mld access-policy 2000]{lang="EN-US"}
:::::

::::: {#546504029 .myid}
[]{#_Toc404790285}[]{#struct_0_42457_14668_x96840369}[]{#_Toc372127976}[]{#_Toc365467130}[]{#_Toc364430857}[]{#_Toc363576226}[]{#_Toc363465604}

**MLD \-- MLD配置命令 \-- mld authorization-enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_42457_14668_x456166191}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_42457_14668_x433768867}
:::

[ ]{lang="EN-US"}

[**[mld]{lang="EN-US"}**[ **authorization-enable**]{lang="EN-US"}]{#struct_0_42457_14668_x1252491492}[命令用来使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[可控组播功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **authorization-enable**]{lang="EN-US"}]{#struct_0_42457_14668_x634722905}[命令用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[可控组播功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1735341077}

[**[mld]{lang="EN-US"}**[ **authorization-enable**]{lang="EN-US"}]{#struct_0_42457_14668_1959115170}

[**[undo]{lang="EN-US"}**[ **mld** **authorization-enable**]{lang="EN-US"}]{#struct_0_42457_14668_x431170066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_977134090}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_472732465}[可控组播功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_936463438}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_42457_14668_1958918562}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VT]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x481638204}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1768185772}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1689325110}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_853138193}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1958984098}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[可控组播功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x427863673}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld authorization-enable]{lang="EN-US"}
:::::

::: {#-1622009386 .myid}
[]{#_Toc103401138}[]{#_Toc87351937}[]{#_Toc87265573}[]{#_Toc82920367}[]{#_Toc404790286}[]{#struct_0_42457_14668_x634088811}[]{#_Toc136854366}[]{#_Toc375301765}[]{#_Toc375301766}[]{#_Toc296159518}[]{#_Toc299379050}[]{#_Toc296159519}[]{#_Toc299379051}[]{#_Toc296159520}[]{#_Toc299379052}[]{#_Toc296159521}[]{#_Toc299379053}[]{#_Toc296159522}[]{#_Toc299379054}[]{#_Toc296159523}[]{#_Toc299379055}[]{#_Toc296159524}[]{#_Toc299379056}[]{#_Toc296159525}[]{#_Toc299379057}[]{#_Toc296159526}[]{#_Toc299379058}[]{#_Toc296159527}[]{#_Toc299379059}[]{#_Toc296159528}[]{#_Toc299379060}[]{#_Toc296159529}[]{#_Toc299379061}[]{#_Toc296159530}[]{#_Toc299379062}[]{#_Toc296159531}[]{#_Toc299379063}[]{#_Toc296159532}[]{#_Toc299379064}[]{#_Toc296159533}[]{#_Toc299379065}[]{#_Toc296159534}[]{#_Toc299379066}[]{#_Toc296159535}[]{#_Toc299379067}[]{#_Toc296159536}[]{#_Toc299379068}[]{#_Toc296159543}[]{#_Toc299379075}[]{#_Toc296159544}[]{#_Toc299379076}[]{#_Toc296159545}[]{#_Toc299379077}[]{#_Toc296159574}[]{#_Toc299379106}[]{#_Toc296159576}[]{#_Toc299379108}[]{#_Toc296159577}[]{#_Toc299379109}[]{#_Toc296159578}[]{#_Toc299379110}[]{#_Toc296159579}[]{#_Toc299379111}[]{#_Toc296159580}[]{#_Toc299379112}[]{#_Toc296159581}[]{#_Toc299379113}[]{#_Toc296159582}[]{#_Toc299379114}[]{#_Toc296159583}[]{#_Toc299379115}[]{#_Toc296159584}[]{#_Toc299379116}[]{#_Toc296159585}[]{#_Toc299379117}[]{#_Toc296159586}[]{#_Toc299379118}[]{#_Toc296159587}[]{#_Toc299379119}[]{#_Toc296159588}[]{#_Toc299379120}[]{#_Toc296159589}[]{#_Toc299379121}[]{#_Toc296159590}[]{#_Toc299379122}[]{#_Toc296159591}[]{#_Toc299379123}[]{#_Toc296159592}[]{#_Toc299379124}[]{#_Toc296159593}[]{#_Toc299379125}[]{#_Toc296159594}[]{#_Toc299379126}[]{#_Toc296159595}[]{#_Toc299379127}[]{#_Toc296159596}[]{#_Toc299379128}[]{#_Toc296159597}[]{#_Toc299379129}[]{#_Toc296159600}[]{#_Toc299379132}[]{#_Toc296159601}[]{#_Toc299379133}[]{#_Toc296159605}[]{#_Toc299379137}[]{#_Toc296159606}[]{#_Toc299379138}[]{#_Toc296159607}[]{#_Toc299379139}[]{#_Toc296159608}[]{#_Toc299379140}[]{#_Toc296159610}[]{#_Toc299379142}[]{#_Toc136854348}[]{#_Toc136854349}[]{#_Toc136854350}[]{#_Toc136854351}[]{#_Toc136854352}[]{#_Toc136854353}[]{#_Toc136854354}[]{#_Toc136854355}[]{#_Toc136854356}[]{#_Toc136854357}[]{#_Toc136854358}[]{#_Toc136854359}[]{#_Toc136854360}[]{#_Toc136854361}[]{#_Toc136854362}[]{#_Toc296159611}[]{#_Toc299379143}[]{#_Toc296159644}[]{#_Toc299379176}[]{#_Toc296159646}[]{#_Toc299379178}[]{#_Toc296159647}[]{#_Toc299379179}[]{#_Toc296159648}[]{#_Toc299379180}[]{#_Toc296159649}[]{#_Toc299379181}[]{#_Toc296159650}[]{#_Toc299379182}[]{#_Toc296159651}[]{#_Toc299379183}[]{#_Toc296159652}[]{#_Toc299379184}[]{#_Toc296159653}[]{#_Toc299379185}[]{#_Toc296159654}[]{#_Toc299379186}[]{#_Toc296159655}[]{#_Toc299379187}[]{#_Toc296159656}[]{#_Toc299379188}[]{#_Toc296159657}[]{#_Toc299379189}[]{#_Toc296159658}[]{#_Toc299379190}[]{#_Toc296159659}[]{#_Toc299379191}[]{#_Toc296159660}[]{#_Toc299379192}[]{#_Toc296159661}[]{#_Toc299379193}[]{#_Toc296159662}[]{#_Toc299379194}[]{#_Toc296159663}[]{#_Toc299379195}[]{#_Toc296159664}[]{#_Toc299379196}[]{#_Toc296159665}[]{#_Toc299379197}[]{#_Toc296159666}[]{#_Toc299379198}[]{#_Toc296159671}[]{#_Toc299379203}[]{#_Toc296159681}[]{#_Toc299379213}[]{#_Toc296159682}[]{#_Toc299379214}[]{#_Toc296159683}[]{#_Toc299379215}[]{#_Toc296159684}[]{#_Toc299379216}[]{#_Toc296159685}[]{#_Toc299379217}[]{#_Toc296159686}[]{#_Toc299379218}[]{#_Toc296159687}[]{#_Toc299379219}[]{#_Toc296159688}[]{#_Toc299379220}[]{#_Toc296159689}[]{#_Toc299379221}[]{#_Toc296159690}[]{#_Toc299379222}[]{#_Toc296159691}[]{#_Toc299379223}[]{#_Toc296159692}[]{#_Toc299379224}[]{#_Toc296159693}[]{#_Toc299379225}[]{#_Toc296159694}[]{#_Toc299379226}[]{#_Toc296159695}[]{#_Toc299379227}[]{#_Toc296159696}[]{#_Toc299379228}[]{#_Toc296159697}[]{#_Toc299379229}[]{#_Toc296159698}[]{#_Toc299379230}[]{#_Toc296159699}[]{#_Toc299379231}[]{#_Toc296159700}[]{#_Toc299379232}[]{#_Toc296159701}[]{#_Toc299379233}[]{#_Toc296159716}[]{#_Toc299379248}[]{#_Toc296159717}[]{#_Toc299379249}[]{#_Toc296159754}[]{#_Toc299379286}[]{#_Toc296159756}[]{#_Toc299379288}[]{#_Toc296159757}[]{#_Toc299379289}[]{#_Toc296159758}[]{#_Toc299379290}[]{#_Toc296159759}[]{#_Toc299379291}[]{#_Toc296159760}[]{#_Toc299379292}[]{#_Toc296159761}[]{#_Toc299379293}[]{#_Toc296159762}[]{#_Toc299379294}[]{#_Toc296159763}[]{#_Toc299379295}[]{#_Toc296159764}[]{#_Toc299379296}[]{#_Toc296159765}[]{#_Toc299379297}[]{#_Toc296159766}[]{#_Toc299379298}[]{#_Toc296159767}[]{#_Toc299379299}[]{#_Toc296159768}[]{#_Toc299379300}[]{#_Toc296159769}[]{#_Toc299379301}[]{#_Toc296159770}[]{#_Toc299379302}[]{#_Toc296159771}[]{#_Toc299379303}[]{#_Toc296159772}[]{#_Toc299379304}[]{#_Toc296159773}[]{#_Toc299379305}[]{#_Toc296159774}[]{#_Toc299379306}[]{#_Toc296159776}[]{#_Toc299379308}[]{#_Toc296159781}[]{#_Toc299379313}[]{#_Toc296159800}[]{#_Toc299379332}[]{#_Toc296159801}[]{#_Toc299379333}[]{#_Toc296159802}[]{#_Toc299379334}[]{#_Toc296159804}[]{#_Toc299379336}[]{#_Toc296159805}[]{#_Toc299379337}[]{#_Toc296159806}[]{#_Toc299379338}[]{#_Toc296159807}[]{#_Toc299379339}[]{#_Toc296159808}[]{#_Toc299379340}[]{#_Toc296159809}[]{#_Toc299379341}[]{#_Toc296159810}[]{#_Toc299379342}[]{#_Toc296159811}[]{#_Toc299379343}[]{#_Toc296159812}[]{#_Toc299379344}[]{#_Toc296159813}[]{#_Toc299379345}[]{#_Toc296159814}[]{#_Toc299379346}[]{#_Toc296159815}[]{#_Toc299379347}[]{#_Toc296159816}[]{#_Toc299379348}[]{#_Toc296159817}[]{#_Toc299379349}[]{#_Toc296159818}[]{#_Toc299379350}[]{#_Toc296159819}[]{#_Toc299379351}[]{#_Toc296159823}[]{#_Toc299379355}[]{#_Toc296159824}[]{#_Toc299379356}[]{#_Toc296159825}[]{#_Toc299379357}[]{#_Toc296159826}[]{#_Toc299379358}[]{#_Toc296159827}[]{#_Toc299379359}[]{#_Toc296159828}[]{#_Toc299379360}[]{#_Toc296159829}[]{#_Toc299379361}[]{#_Toc296159830}[]{#_Toc299379362}[]{#_Toc296159831}[]{#_Toc299379363}[]{#_Toc296159832}[]{#_Toc299379364}[]{#_Toc296159833}[]{#_Toc299379365}[]{#_Toc296159834}[]{#_Toc299379366}[]{#_Toc296159835}[]{#_Toc299379367}[]{#_Toc296159836}[]{#_Toc299379368}[]{#_Toc296159837}[]{#_Toc299379369}[]{#_Toc296159838}[]{#_Toc299379370}[]{#_Toc296159840}[]{#_Toc299379372}[]{#_Toc296159841}[]{#_Toc299379373}[]{#_Toc296159842}[]{#_Toc299379374}[]{#_Toc296159843}[]{#_Toc299379375}[]{#_Toc296159844}[]{#_Toc299379376}[]{#_Toc296159846}[]{#_Toc299379378}[]{#_Toc296159847}[]{#_Toc299379379}[]{#_Toc296159848}[]{#_Toc299379380}[]{#_Toc296159849}[]{#_Toc299379381}[]{#_Toc296159850}[]{#_Toc299379382}[]{#_Toc296159851}[]{#_Toc299379383}[]{#_Toc296159852}[]{#_Toc299379384}[]{#_Toc296159853}[]{#_Toc299379385}[]{#_Toc296159854}[]{#_Toc299379386}[]{#_Toc296159855}[]{#_Toc299379387}[]{#_Toc296159856}[]{#_Toc299379388}[]{#_Toc296159857}[]{#_Toc299379389}[]{#_Toc296159859}[]{#_Toc299379391}[]{#_max-response-time}[]{#_Toc296159861}[]{#_Toc299379393}[]{#_Toc296159862}[]{#_Toc299379394}[]{#_Toc296159863}[]{#_Toc299379395}[]{#_Toc296159865}[]{#_Toc299379397}[]{#_Toc296159866}[]{#_Toc299379398}[]{#_Toc296159867}[]{#_Toc299379399}[]{#_Toc296159868}[]{#_Toc299379400}[]{#_Toc296159869}[]{#_Toc299379401}[]{#_Toc296159870}[]{#_Toc299379402}[]{#_Toc296159871}[]{#_Toc299379403}[]{#_Toc296159872}[]{#_Toc299379404}[]{#_Toc296159873}[]{#_Toc299379405}[]{#_Toc296159874}[]{#_Toc299379406}[]{#_Toc296159875}[]{#_Toc299379407}[]{#_Toc296159876}[]{#_Toc299379408}[]{#_Toc296159881}[]{#_Toc299379413}[]{#_Toc296159882}[]{#_Toc299379414}[]{#_Toc296159883}[]{#_Toc299379415}[]{#_Toc296159884}[]{#_Toc299379416}[]{#_Toc296159885}[]{#_Toc299379417}[]{#_Toc296159886}[]{#_Toc299379418}[]{#_Toc296159887}[]{#_Toc299379419}[]{#_Toc296159888}[]{#_Toc299379420}[]{#_Toc296159889}[]{#_Toc299379421}[]{#_Toc296159890}[]{#_Toc299379422}[]{#_Toc296159891}[]{#_Toc299379423}[]{#_Toc296159892}[]{#_Toc299379424}[]{#_Toc296159893}[]{#_Toc299379425}[]{#_Toc296159894}[]{#_Toc299379426}[]{#_Toc296159895}[]{#_Toc299379427}

**MLD \-- MLD配置命令 \-- mld enable**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_42457_14668_x613251449}[命令用来在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **enable**]{lang="EN-US"}]{#struct_0_42457_14668_x575972005}[命令用来在接口上关闭]{style="font-family:宋体"}[MLD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1905454105}

[]{#struct_0_42457_14668_1041888722}[]{#_Hlt20797640}**[mld]{lang="EN-US"}**[ **enable**]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **mld** **enable**]{lang="EN-US"}]{#struct_0_42457_14668_1586685864}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_1523170864}

[[接口上的]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1271063769}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_556837288}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x2081412056}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1832578775}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x249839254}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_107096896}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_348491530}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在相应实例中先使能了]{style="font-family:宋体"}]{#struct_0_42457_14668_678737104}[IPv6]{lang="EN-US"}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在接口上使能了]{style="font-family:宋体"}]{#struct_0_42457_14668_1373752808}[MLD]{lang="EN-US"}[，在该接口上所做的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[配置才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1271129305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x189129867}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x699263964}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_382191531}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1096037273}

[[\# ]{lang="SV"}]{#struct_0_42457_14668_1713314665}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="SV"}[上使能]{style="font-family:宋体"}[MLD]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1271194841}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1329792856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 multicast]{lang="EN-US"}**[ **routing**]{lang="EN-US"}]{#struct_0_42457_14668_x619635526}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/IPv6]{lang="EN-US"}[组播路由与转发）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1738143011 .myid}
[]{#_Toc136854367}[]{#_Toc404790287}[]{#struct_0_42457_14668_x988204883}

**MLD \-- MLD配置命令 \-- mld fast-leave**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **fast-leave**]{lang="EN-US"}]{#struct_0_42457_14668_x1039198548}[命令用来在接口上使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组成员快速离开功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **fast-leave**]{lang="EN-US"}]{#struct_0_42457_14668_x2038536016}[命令用来在接口上关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组成员快速离开功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1585108134}

[**[mld]{lang="EN-US"}**[ **fast-leave** \[ ]{lang="EN-US"}**[group-policy]{lang="EN-US"}***[ acl6-number ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_42457_14668_137941627}

[**[undo]{lang="EN-US"}**[ **mld** **fast-leave**]{lang="EN-US"}]{#struct_0_42457_14668_1314910242}

[[【]{style="font-family:黑体"}]{#struct_0_42457_14668_552731650}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1271260377}[组播组成员快速离开功能处于关闭状态，即]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器在收到主机发送的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[离开组报文后将发送]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文或]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定源组查询报文，而不会直接向上游发送离开通告。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1408289462}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x879845459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1417306319}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_502656639}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1517632004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_685513644}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_42457_14668_x713864307}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果指定了本参数，快速离开功能将只为该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组服务；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则快速离开功能将为所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组服务。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x474969759}

[[ACL]{lang="EN-US"}]{#struct_0_42457_14668_x198776466}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_757310860}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_1271325913}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_580621052}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组成员快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x432991450}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld fast-leave]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_1240559194}

[[\# ]{lang="SV"}]{#struct_0_42457_14668_x134980433}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="SV"}[上使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组成员快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1549263607}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld fast-leave]{lang="EN-US"}
:::

::: {#-55976181 .myid}
[]{#_Toc404790288}[]{#struct_0_42457_14668_1776734076}[]{#_Toc307402355}[]{#_Toc307402356}[]{#_Toc307402357}[]{#_Toc296159902}[]{#_Toc299379434}[]{#_Toc296159903}[]{#_Toc299379435}[]{#_Toc296159904}[]{#_Toc299379436}[]{#_Toc296159906}[]{#_Toc299379438}[]{#_Toc296159907}[]{#_Toc299379439}[]{#_Toc296159908}[]{#_Toc299379440}[]{#_Toc296159909}[]{#_Toc299379441}[]{#_Toc296159910}[]{#_Toc299379442}[]{#_Toc296159911}[]{#_Toc299379443}[]{#_Toc296159912}[]{#_Toc299379444}[]{#_Toc296159913}[]{#_Toc299379445}[]{#_Toc296159914}[]{#_Toc299379446}[]{#_Toc296159915}[]{#_Toc299379447}[]{#_Toc296159916}[]{#_Toc299379448}[]{#_Toc296159917}[]{#_Toc299379449}[]{#_Toc296159918}[]{#_Toc299379450}[]{#_Toc296159919}[]{#_Toc299379451}[]{#_Toc296159920}[]{#_Toc299379452}[]{#_Toc296159921}[]{#_Toc299379453}[]{#_Toc296159922}[]{#_Toc299379454}[]{#_Toc296159923}[]{#_Toc299379455}[]{#_Toc296159924}[]{#_Toc299379456}[]{#_Toc296159925}[]{#_Toc299379457}[]{#_Toc296159926}[]{#_Toc299379458}[]{#_Toc296159927}[]{#_Toc299379459}[]{#_Toc296159928}[]{#_Toc299379460}[]{#_Toc296159930}[]{#_Toc299379462}

**MLD \-- MLD配置命令 \-- mld group-policy**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **group-policy**]{lang="EN-US"}]{#struct_0_42457_14668_1271391449}[命令用来在接口上配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器，以限定该接口下的主机所能加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **group-policy**]{lang="EN-US"}]{#struct_0_42457_14668_1335476363}[命令用来在接口上删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1677841569}

[**[mld]{lang="EN-US"}**[ **group-policy** *acl6-number* \[ *version-number* \]]{lang="EN-US"}]{#struct_0_42457_14668_x667602193}

[**[undo]{lang="EN-US"}**[ **mld** **group-policy**]{lang="EN-US"}]{#struct_0_42457_14668_x1409086780}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_2113713751}

[[接口上没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_41065143}[组播组过滤器，即该接口下的主机可以加入任意]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_600630777}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x957848680}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1269536749}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1271456985}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_162328621}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1769780500}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_42457_14668_2107639925}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。主机只能加入该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[*[version-number]{lang="EN-US"}*]{#struct_0_42457_14668_x1188876004}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。缺省情况下，系统同时支持对]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}[和]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[报告报文的过滤。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x128515071}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_42457_14668_x474838690}[IPv6]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_181362226}[IPv]{lang="DA"}[6]{lang="DA"}[高级]{lang="EN-US" style="font-family:
宋体"}[ACL]{lang="DA"}[，]{lang="EN-US" style="font-family:宋体"}[该]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{lang="EN-US" style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[MLDv1]{lang="DA"}[报文和未携带]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[MLDv2]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[视其]{lang="EN-US" style="font-family:
宋体"}[IPv6]{lang="DA"}[组播源地址为]{lang="EN-US" style="font-family:宋体"}[0::0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}**[destination]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:
宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于本命令只能过滤]{style="font-family:宋体"}]{#struct_0_42457_14668_760718187}[MLD]{lang="EN-US"}[报文，因此无法对接口静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组或组播源组进行限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_556498656}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_924188000}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1271522521}[限定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下的主机只能加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x1383457384}

[\[Sysname\] acl ipv6 basic 2005]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2005\] rule permit source ff03::101 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2005\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld group-policy 2005]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_223184587}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1183203182}[限定接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[下的主机只能加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1972223384}

[\[Sysname\] acl ipv6 basic 2005]{lang="EN-US"}

[\[Sysname\--acl-ipv6-basic-2005\] rule permit source ff03::101 128]{lang="EN-US"}

[\[Sysname\--acl-ipv6-basic-2005\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld group-policy 2005]{lang="EN-US"}
:::

::::: {#-1459380755 .myid}
[]{#_Toc404790289}[]{#struct_0_42457_14668_1959246241}[]{#_Toc372127980}[]{#_Toc372127323}[]{#_Toc370719719}[]{#_Toc363576227}

**MLD \-- MLD配置命令 \-- mld join-by-session**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_42457_14668_x455904048}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_42457_14668_x455838512}
:::

[ ]{lang="EN-US"}

[**[mld]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_42457_14668_x447583819}[命令用来配置按会话记录用户加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[mld]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_42457_14668_1959049633}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x96643761}

[**[mld]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_42457_14668_x1523756672}

[**[undo]{lang="EN-US"}**[ **mld** **join-by-session**]{lang="EN-US"}]{#struct_0_42457_14668_x826561458}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x341805607}

[[按接口记录用户加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_1959115169}[组播组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x430711315}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_42457_14668_x583569892}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x873261932}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x853897921}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1958918561}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x481834812}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当按接口记录用户加入的]{style="font-family:宋体"}]{#struct_0_42457_14668_x997910567}[IPv6]{lang="EN-US"}[组播组时，设备只会向物理接口发送一份]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播报文；当按会话记录用户加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组时，设备会向接口下的每位用户分别发送一份]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_42457_14668_2096804316}[命令]{style="font-family:宋体"}[与]{lang="EN-US" style="font-family:宋体"}**[mld]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令]{style="font-family:宋体"}[互斥，不]{lang="EN-US" style="font-family:宋体"}[允许]{style="font-family:宋体"}[同时配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_572857745}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1958984097}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置按会话记录用户加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x427142777}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld join-by-session]{lang="EN-US"}
:::::

::: {#2008618660 .myid}
[]{#_Toc33096884}[]{#_Toc404790290}[]{#struct_0_42457_14668_x1840059898}[]{#_Toc372212382}[]{#_Toc372205804}[]{#_Toc371343393}[]{#_Toc368325554}[]{#_Toc368294498}

**MLD \-- MLD配置命令 \-- mld last-listener-query-count**

------------------------------------------------------------------------

[**[mld last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x910217490}[命令用来在接口上配置]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[最后组成员查询次数。]{style="font-family:宋体"}

[**[undo mld last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_1958787489}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x789187477}

[**[mld last-listener-query-count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_42457_14668_x1889492428}

[**[undo mld last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_39543767}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x431793809}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1958853025}[最后组成员查询次数等于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2015574470}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x1555571415}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1636551212}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1488740389}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1959704993}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x470003139}

[*[count]{lang="EN-US"}*]{#struct_0_42457_14668_399078967}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x613271842}

[[本命令与]{style="font-family:宋体"}**[last-listener-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_1959770529}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x439147342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_831620155}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1580640850}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x7178452}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld last-listener-query-count 6]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_43223393}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_537804020}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_583607299}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld last-listener-query-count 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x555553452}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[last-listener-query-count]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}]{#struct_0_42457_14668_x2106420069}
:::

::: {#1852120580 .myid}
[]{#_Toc404790291}[]{#struct_0_42457_14668_43157857}[]{#_Toc372212383}[]{#_Toc372205805}[]{#_Toc371343394}[]{#_Toc368325555}[]{#_Toc368294499}

**MLD \-- MLD配置命令 \-- mld last-listener-query-interval**

------------------------------------------------------------------------

[**[mld last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_69489307}[命令用来在接口上配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询间隔。]{style="font-family:宋体"}

[**[undo mld last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1089418043}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x458829294}

[**[mld last-listener-query-interval]{lang="EN-US"}***[ ]{lang="EN-US"}[interval]{lang="EN-US"}*]{#struct_0_42457_14668_x1449778351}

[**[undo mld last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_43092321}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_2020158038}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x482751533}[最后组成员查询间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_2005776811}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_392626303}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_43026785}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1239464040}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_188957223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x393441896}

[*[interval]{lang="EN-US"}*]{#struct_0_42457_14668_x237719151}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_42961249}

[[本命令与]{style="font-family:宋体"}**[last-listener-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x1745610056}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2131829972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1545437212}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_440396306}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_42895713}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld last-listener-query-interval 6]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_264952752}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1080422510}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[最后组成员查询间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x1879339593}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld last-listener-query-interval 6]{lang="EN-US"}

[]{#_Toc371343395}[]{#_Toc368325556}[]{#_Toc368294500}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_640866328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[last-listener-query-interval]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}]{#struct_0_42457_14668_42830177}
:::

::: {#-83490669 .myid}
[]{#_Toc404790292}[]{#struct_0_42457_14668_294241507}[]{#_Toc372212384}[]{#_Toc372205806}

**MLD \-- MLD配置命令 \-- mld max-response-time**

------------------------------------------------------------------------

[**[mld max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_x152380921}[命令用来在接口上配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的最大响应时间。]{style="font-family:宋体"}

[**[undo mld max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_1043919402}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x505390046}

[**[mld max-response-time]{lang="EN-US"}***[ time]{lang="EN-US"}*]{#struct_0_42457_14668_42764641}

[**[undo mld max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_677246743}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x479961695}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1295217070}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_43747681}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_2016509908}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2021116}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1662158653}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_2010099415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_43682145}

[*[time]{lang="EN-US"}*]{#struct_0_42457_14668_x799599142}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3174]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x552792938}

[[本命令与]{style="font-family:宋体"}**[max-response-time]{lang="EN-US"}**]{#struct_0_42457_14668_x409204366}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1723384614}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_43223392}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1800848140}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1348249826}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld max-response-time 25]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_266821001}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x420198649}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_43157856}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld max-response-time 25]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1886825829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-response-time]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}]{#struct_0_42457_14668_x1132530660}
:::

::: {#-1236027165 .myid}
[]{#_Toc404790293}[]{#struct_0_42457_14668_1889576893}[]{#_Toc369785485}[]{#_Toc365363041}[]{#_Toc363907096}

**MLD \-- MLD配置命令 \-- mld other-querier-present-timeout**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **other-querier-present-timeout**]{lang="EN-US"}]{#struct_0_42457_14668_x1212719090}[命令用来在接口上配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[其它查询器的存在时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld other-querier-present-timeout**]{lang="EN-US"}]{#struct_0_42457_14668_1889642429}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1539928584}

[**[mld]{lang="EN-US"}**[ **other-querier-present-timeout** *time*]{lang="EN-US"}]{#struct_0_42457_14668_x2043312270}

[**[undo]{lang="EN-US"}**[ **mld** **other-querier-present-timeout**]{lang="EN-US"}]{#struct_0_42457_14668_x1136603921}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1119282158}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1889970109}[其它查询器的存在时间＝]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔×]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数＋]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间÷]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1948944821}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x1256314999}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1302542197}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_554252826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1890035645}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2034715006}

[*[time]{lang="EN-US"}*]{#struct_0_42457_14668_x1152446036}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[其它查询器的存在时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_42895712}

[[本命令与]{style="font-family:宋体"}**[other-querier-present-timeout]{lang="EN-US"}**]{#struct_0_42457_14668_x1691362384}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1483856823}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1501932070}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1889839037}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[其它查询器的存在时间为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x1525397970}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld other-querier-present-timeout 125]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x937979967}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x833416401}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[其它查询器的存在时间为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1889904573}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld other-querier-present-timeout 125]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_42764640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[other-querier-present-]{lang="EN-US"}**]{#struct_0_42457_14668_x1661405417}**[timeout]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}
:::

::: {#1538211218 .myid}
[]{#_Toc404790294}[]{#struct_0_42457_14668_570161814}[]{#_Toc364955779}[]{#_Toc355963325}

**MLD \-- MLD配置命令 \-- mld proxy enable**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_42457_14668_570096278}[命令用来在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **proxy** **enable**]{lang="EN-US"}]{#struct_0_42457_14668_x1170724704}[命令用来关闭接口上的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_569637525}

[**[mld]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_42457_14668_x616061545}

[**[undo]{lang="EN-US"}**[ **mld** **proxy** **enable**]{lang="EN-US"}]{#struct_0_42457_14668_569571989}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x411357485}

[[接口上的]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_569506453}[代理功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_670571031}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_569440917}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1624494400}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_569899669}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x11522098}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_569834133}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x776088787}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_569768597}

[]{#struct_0_42457_14668_x1056135614}[]{#_Hlt26244069}[]{#_Toc32805310}[]{#_Toc32805323}[]{#_Hlt16393071}[]{#_Hlt26244065}[]{#_Toc32812466}[]{#_Toc32812467}[]{#_Toc32812468}[]{#_Toc32812469}[]{#_Toc32812470}[]{#_Toc32812471}[]{#_Toc32812472}[]{#_Toc32812473}[]{#_Toc32812474}[]{#_Toc32812475}[]{#_Toc32812476}[]{#_Toc32812477}[]{#_Toc32812478}[]{#_Toc32812479}[]{#_Toc32812480}[]{#_Toc32812481}[]{#_Toc32812482}[]{#_Toc32812484}[]{#_Toc32812509}[]{#_Toc32812511}[]{#_Toc32812512}[]{#_Toc32812513}[]{#_Toc32812514}[]{#_Toc32812515}[]{#_Hlt20986286}[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}[：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="FR"}]{#struct_0_42457_14668_569703061}[使能公网实例中的]{style="font-family:宋体"}[Ipv6]{lang="FR"}[组播路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上使能]{style="font-family:宋体"}[MLD]{lang="FR"}[代理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x966768727}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld proxy enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_570161813}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1907800194}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_570096277}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld proxy enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1170724699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6]{lang="EN-US"}**]{#struct_0_42457_14668_569637524}[ ]{lang="EN-US"}**[multicast]{lang="EN-US"}**[ **routing**]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[IPv6]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#1082848765 .myid}
[]{#_Toc404790295}[]{#struct_0_42457_14668_x616061544}[]{#_Toc364955780}

**MLD \-- MLD配置命令 \-- mld proxy forwarding**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_42457_14668_569571988}[命令用来使能非查询器转发功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_42457_14668_x411357484}[命令用来关闭非查询器转发功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_569506452}

[**[mld]{lang="EN-US"}**[ **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_42457_14668_670571030}

[**[undo]{lang="EN-US"}**[ **mld** **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_42457_14668_569440916}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1624494401}

[[非查询器转发功能处于关闭状态]{style="font-family:宋体"}]{#struct_0_42457_14668_484257335}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_569899668}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x11522097}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_569834132}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x776088786}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_569768596}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1056135615}

[[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_569703060}[组播数据通常只被查询器转发，非查询器不具备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播转发能力，这样可避免]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据被重复转发。但如果]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理设备的路由器接口未能当选查询器，应在该接口上使能非查询器转发功能，否则下游主机将无法收到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x966768728}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_570161812}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1907800193}[在]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理设备的路由器接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能非查询器转发功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_570096276}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld proxy forwarding]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1170724698}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_569637523}[在]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理设备的路由器接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能非查询器转发功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x616061543}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld proxy forwarding]{lang="EN-US"}
:::

::: {#-70590567 .myid}
[]{#_Toc404790296}[]{#struct_0_42457_14668_1889576892}[]{#_Toc369785488}[]{#_Toc365363043}[]{#_Toc363907095}

**MLD \-- MLD配置命令 \-- mld query-interval**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **query-interval**]{lang="EN-US"}]{#struct_0_42457_14668_x1212784626}[命令用来在接口上配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **query-interval**]{lang="EN-US"}]{#struct_0_42457_14668_1889642428}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1539863048}

[**[mld]{lang="EN-US"}**[ **query-interval** *interval*]{lang="EN-US"}]{#struct_0_42457_14668_183581173}

[**[undo]{lang="EN-US"}**[ **mld** **query-interval**]{lang="EN-US"}]{#struct_0_42457_14668_x1624006791}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x481143265}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1889970108}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1949010357}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_553359790}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1840359082}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1890035644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x2034780542}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_62703524}

[*[interval]{lang="EN-US"}*]{#struct_0_42457_14668_x97317480}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_43092319}

[[本命令与]{style="font-family:宋体"}**[query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x1148745689}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1889839036}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1525463506}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_2062134120}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x761718444}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld query-interval 60]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_1889904572}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x383170374}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x14728094}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld query-interval 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_43026783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[query-interval]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}]{#struct_0_42457_14668_x1908492184}
:::

::: {#-1142304743 .myid}
[]{#_Toc404790297}[]{#struct_0_42457_14668_x1280514726}[]{#_Toc372212389}[]{#_Toc372205811}[]{#_Toc371343400}[]{#_Toc368325560}[]{#_Toc368294501}

**MLD \-- MLD配置命令 \-- mld robust-count**

------------------------------------------------------------------------

[**[mld robust-count]{lang="EN-US"}**]{#struct_0_42457_14668_42961247}[命令用来在接口上配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[**[undo mld robust-count]{lang="EN-US"}**]{#struct_0_42457_14668_930749112}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1057011115}

[**[mld robust-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_42457_14668_1006415989}

[**[undo mld robust-count]{lang="EN-US"}**]{#struct_0_42457_14668_42895711}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x117384272}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x233069393}[查询器的健壮系数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_582029795}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_42830175}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_676578531}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1893499833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_42764639}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x448816826}

[*[count]{lang="EN-US"}*]{#struct_0_42457_14668_x1954851278}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_1464507676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_43747679}[查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器就越"健壮"，但是组播组超时所需的时间也就越长。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{style="font-family:宋体"}]{#struct_0_42457_14668_1602907059}**[robust-count]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1108705130}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_43682143}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x417262118}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x1437275964}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld robust-count 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x652744552}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_43223390}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_2111782132}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld robust-count 5]{lang="EN-US"}

[]{#_Toc371343401}[]{#_Toc368325561}[]{#_Toc368294502}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_2108821328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[robust-count]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}]{#struct_0_42457_14668_43157854}
:::

::: {#-1350703195 .myid}
[]{#_Toc404790298}[]{#struct_0_42457_14668_2025804443}[]{#_Toc372212390}[]{#_Toc372205812}

**MLD \-- MLD配置命令 \-- mld startup-query-count**

------------------------------------------------------------------------

[**[mld startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x1069329425}[命令用来在接口上配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询次数。]{style="font-family:宋体"}

[**[undo mld startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_414033352}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_43092318}

[**[mld startup-query-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_42457_14668_1189906471}

[**[undo mld startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_87646084}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x870211586}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_43026782}[查询器的启动查询次数等于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_47822952}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x1297895909}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1888657947}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_42961246}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1407903048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2080303286}

[*[count]{lang="EN-US"}*]{#struct_0_42457_14668_1956164731}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_42895710}

[[本命令与]{style="font-family:宋体"}**[startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x2073699408}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x755573620}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1886481254}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_42830174}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x1279736605}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld startup-query-count 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_984727237}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_42764638}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1507498310}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld startup-query-count 5]{lang="EN-US"}

[]{#_Toc371343402}[]{#_Toc368325562}[]{#_Toc368294503}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1839675330}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[startup-query-count]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}]{#struct_0_42457_14668_1823898480}
:::

::: {#-1443671786 .myid}
[]{#_Toc404790299}[]{#struct_0_42457_14668_43747678}[]{#_Toc372212391}[]{#_Toc372205813}

**MLD \-- MLD配置命令 \-- mld startup-query-interval**

------------------------------------------------------------------------

[**[mld startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x735745101}[命令用来在接口上配置]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[查询器的启动查询间隔。]{style="font-family:宋体"}

[**[undo mld startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x1949000786}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x630494572}

[**[mld startup-query-interval]{lang="EN-US"}***[ ]{lang="EN-US"}[interval]{lang="EN-US"}*]{#struct_0_42457_14668_43682142}

[**[undo mld startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1539053018}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_602048950}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_43223397}[查询器的启动查询间隔为]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文发送间隔的]{style="font-family:宋体"}[1/4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x226870028}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x174063138}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1005024823}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_43157861}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_488562176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_1064884174}

[*[interval]{lang="EN-US"}*]{#struct_0_42457_14668_x504617675}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_43092325}

[[本命令与]{style="font-family:宋体"}**[startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1255483990}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2111322429}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1323323356}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_43026789}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_474789992}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld startup-query-interval 100]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_2127054559}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x598715144}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_42961253}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld startup-query-interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1732159005}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[startup-query-interval]{lang="EN-US"}**[ (MLD view)]{lang="EN-US"}]{#struct_0_42457_14668_2015053112}
:::

::: {#-1382827687 .myid}
[]{#_Toc87351946}[]{#_Toc87265582}[]{#_Toc82920376}[]{#_Toc404790300}[]{#struct_0_42457_14668_1623960028}[]{#_Toc136854390}[]{#_Toc307402359}[]{#_Toc307402360}[]{#_mld_lastlistener-queryinterval}[]{#_Toc296159932}[]{#_Toc299379464}[]{#_Toc296159933}[]{#_Toc299379465}[]{#_Toc296159934}[]{#_Toc299379466}[]{#_Toc296159935}[]{#_Toc299379467}[]{#_Toc296159936}[]{#_Toc299379468}[]{#_Toc296159937}[]{#_Toc299379469}[]{#_Toc296159938}[]{#_Toc299379470}[]{#_Toc296159939}[]{#_Toc299379471}[]{#_Toc296159940}[]{#_Toc299379472}[]{#_Toc296159941}[]{#_Toc299379473}[]{#_Toc296159942}[]{#_Toc299379474}[]{#_Toc296159943}[]{#_Toc299379475}[]{#_Toc296159944}[]{#_Toc299379476}[]{#_Toc296159945}[]{#_Toc299379477}[]{#_Toc296159946}[]{#_Toc299379478}[]{#_Toc296159947}[]{#_Toc299379479}[]{#_Toc296159948}[]{#_Toc299379480}[]{#_Toc296159950}[]{#_Toc299379482}[]{#_Toc296159951}[]{#_Toc299379483}[]{#_Toc296159952}[]{#_Toc299379484}[]{#_Toc296159953}[]{#_Toc299379485}[]{#_Toc296159956}[]{#_Toc299379488}[]{#_Toc296159958}[]{#_Toc299379490}[]{#_Toc296159959}[]{#_Toc299379491}[]{#_Toc296159961}[]{#_Toc299379493}[]{#_Toc296159962}[]{#_Toc299379494}[]{#_Toc296159963}[]{#_Toc299379495}[]{#_Toc296159964}[]{#_Toc299379496}[]{#_Toc296159965}[]{#_Toc299379497}[]{#_Toc296159966}[]{#_Toc299379498}[]{#_Toc296159967}[]{#_Toc299379499}[]{#_Toc296159968}[]{#_Toc299379500}[]{#_Toc296159969}[]{#_Toc299379501}[]{#_Toc296159970}[]{#_Toc299379502}[]{#_Toc296159971}[]{#_Toc299379503}[]{#_Toc296159972}[]{#_Toc299379504}[]{#_Toc296159973}[]{#_Toc299379505}[]{#_Toc296159975}[]{#_Toc299379507}[]{#_Toc296159976}[]{#_Toc299379508}[]{#_Toc296159977}[]{#_Toc299379509}[]{#_Toc296159978}[]{#_Toc299379510}[]{#_Toc296159980}[]{#_Toc299379512}[]{#_Toc99945446}[]{#_Toc99945641}[]{#_Toc99945448}[]{#_Toc99945643}[]{#_mld_max-response-time}[]{#_Toc296159983}[]{#_Toc299379515}[]{#_Toc296159984}[]{#_Toc299379516}[]{#_Toc296159986}[]{#_Toc299379518}[]{#_Toc296159987}[]{#_Toc299379519}[]{#_Toc296159988}[]{#_Toc299379520}[]{#_Toc296159989}[]{#_Toc299379521}[]{#_Toc296159990}[]{#_Toc299379522}[]{#_Toc296159991}[]{#_Toc299379523}[]{#_Toc296159992}[]{#_Toc299379524}[]{#_Toc296159993}[]{#_Toc299379525}[]{#_Toc296159994}[]{#_Toc299379526}[]{#_Toc296159995}[]{#_Toc299379527}[]{#_Toc296159996}[]{#_Toc299379528}[]{#_Toc296159997}[]{#_Toc299379529}[]{#_Toc296159998}[]{#_Toc299379530}[]{#_Toc296159999}[]{#_Toc299379531}[]{#_Toc296160001}[]{#_Toc299379533}[]{#_mld_prompt-leave}[]{#_Toc296160003}[]{#_Toc299379535}[]{#_Toc296160004}[]{#_Toc299379536}[]{#_Toc296160006}[]{#_Toc299379538}[]{#_mld_require-router-alert}[]{#_Toc296160009}[]{#_Toc299379541}[]{#_Toc296160010}[]{#_Toc299379542}[]{#_Toc296160011}[]{#_Toc299379543}[]{#_Toc296160012}[]{#_Toc299379544}[]{#_Toc296160013}[]{#_Toc299379545}[]{#_Toc296160014}[]{#_Toc299379546}[]{#_Toc296160015}[]{#_Toc299379547}[]{#_Toc296160016}[]{#_Toc299379548}[]{#_Toc296160017}[]{#_Toc299379549}[]{#_Toc296160018}[]{#_Toc299379550}[]{#_Toc296160019}[]{#_Toc299379551}[]{#_Toc296160020}[]{#_Toc299379552}[]{#_Toc296160021}[]{#_Toc299379553}[]{#_Toc296160022}[]{#_Toc299379554}[]{#_Toc296160023}[]{#_Toc299379555}[]{#_Toc296160024}[]{#_Toc299379556}[]{#_Toc296160025}[]{#_Toc299379557}[]{#_Toc296160026}[]{#_Toc299379558}[]{#_Toc296160027}[]{#_Toc299379559}[]{#_Toc296160030}[]{#_Toc299379562}[]{#_Toc296160032}[]{#_Toc299379564}[]{#_Toc296160033}[]{#_Toc299379565}[]{#_Toc296160038}[]{#_Toc299379570}[]{#_Toc296160039}[]{#_Toc299379571}[]{#_Toc296160040}[]{#_Toc299379572}[]{#_Toc296160041}[]{#_Toc299379573}[]{#_Toc296160042}[]{#_Toc299379574}[]{#_Toc296160043}[]{#_Toc299379575}[]{#_Toc296160044}[]{#_Toc299379576}[]{#_Toc296160045}[]{#_Toc299379577}[]{#_Toc296160046}[]{#_Toc299379578}[]{#_Toc296160047}[]{#_Toc299379579}[]{#_Toc296160048}[]{#_Toc299379580}[]{#_Toc296160049}[]{#_Toc299379581}[]{#_Toc296160050}[]{#_Toc299379582}[]{#_Toc296160051}[]{#_Toc299379583}[]{#_Toc296160052}[]{#_Toc299379584}[]{#_Toc296160053}[]{#_Toc299379585}[]{#_Toc296160055}[]{#_Toc299379587}[]{#_Toc296160056}[]{#_Toc299379588}[]{#_Toc296160057}[]{#_Toc299379589}[]{#_Toc296160058}[]{#_Toc299379590}[]{#_Toc296160061}[]{#_Toc299379593}[]{#_Toc296160063}[]{#_Toc299379595}[]{#_Toc296160064}[]{#_Toc299379596}[]{#_Toc296160066}[]{#_Toc299379598}[]{#_Toc296160067}[]{#_Toc299379599}[]{#_Toc296160068}[]{#_Toc299379600}[]{#_Toc296160069}[]{#_Toc299379601}[]{#_Toc296160070}[]{#_Toc299379602}[]{#_Toc296160071}[]{#_Toc299379603}[]{#_Toc296160072}[]{#_Toc299379604}[]{#_Toc296160073}[]{#_Toc299379605}[]{#_Toc296160074}[]{#_Toc299379606}[]{#_Toc296160075}[]{#_Toc299379607}[]{#_Toc296160076}[]{#_Toc299379608}[]{#_Toc296160077}[]{#_Toc299379609}[]{#_Toc296160078}[]{#_Toc299379610}[]{#_Toc296160080}[]{#_Toc299379612}[]{#_mld_robust-count}[]{#_Toc296160082}[]{#_Toc299379614}[]{#_Toc296160083}[]{#_Toc299379615}[]{#_Toc296160088}[]{#_Toc299379620}[]{#_Toc296160091}[]{#_Toc299379623}[]{#_Toc296160092}[]{#_Toc299379624}[]{#_Toc296160093}[]{#_Toc299379625}[]{#_Toc296160094}[]{#_Toc299379626}[]{#_Toc296160095}[]{#_Toc299379627}[]{#_Toc296160096}[]{#_Toc299379628}[]{#_Toc296160097}[]{#_Toc299379629}[]{#_Toc296160098}[]{#_Toc299379630}[]{#_Toc296160099}[]{#_Toc299379631}[]{#_Toc296160100}[]{#_Toc299379632}[]{#_Toc296160101}[]{#_Toc299379633}[]{#_Toc296160102}[]{#_Toc299379634}[]{#_Toc296160103}[]{#_Toc299379635}[]{#_Toc296160104}[]{#_Toc299379636}[]{#_Toc296160105}[]{#_Toc299379637}[]{#_Toc296160106}[]{#_Toc299379638}[]{#_Toc296160107}[]{#_Toc299379639}[]{#_Toc296160109}[]{#_Toc299379641}[]{#_mld_send-router-alert}[]{#_Toc296160111}[]{#_Toc299379643}[]{#_Toc296160112}[]{#_Toc299379644}[]{#_Toc296160114}[]{#_Toc299379646}[]{#_Toc296160117}[]{#_Toc299379649}[]{#_Toc296160120}[]{#_Toc299379652}[]{#_Toc296160121}[]{#_Toc299379653}[]{#_Toc296160122}[]{#_Toc299379654}[]{#_Toc296160123}[]{#_Toc299379655}[]{#_Toc296160124}[]{#_Toc299379656}[]{#_Toc296160125}[]{#_Toc299379657}[]{#_Toc296160126}[]{#_Toc299379658}[]{#_Toc296160127}[]{#_Toc299379659}[]{#_Toc296160128}[]{#_Toc299379660}[]{#_Toc296160129}[]{#_Toc299379661}[]{#_Toc296160130}[]{#_Toc299379662}[]{#_Toc296160131}[]{#_Toc299379663}[]{#_Toc296160132}[]{#_Toc299379664}[]{#_Toc296160134}[]{#_Toc299379666}[]{#_Toc136854374}[]{#_Toc136854375}[]{#_Toc136854378}[]{#_Toc136854379}[]{#_Toc136854380}[]{#_Toc136854381}[]{#_Toc136854382}[]{#_Toc136854383}[]{#_Toc136854384}[]{#_Toc136854385}[]{#_Toc136854386}[]{#_Toc136854387}[]{#_Toc136854388}[]{#_Toc136854389}[]{#_Toc296160136}[]{#_Toc299379668}[]{#_Toc296160137}[]{#_Toc299379669}[]{#_Toc296160142}[]{#_Toc299379674}[]{#_Toc296160144}[]{#_Toc299379676}[]{#_Toc296160145}[]{#_Toc299379677}[]{#_Toc296160146}[]{#_Toc299379678}[]{#_Toc296160147}[]{#_Toc299379679}[]{#_Toc296160148}[]{#_Toc299379680}[]{#_Toc296160149}[]{#_Toc299379681}[]{#_Toc296160150}[]{#_Toc299379682}[]{#_Toc296160151}[]{#_Toc299379683}[]{#_Toc296160152}[]{#_Toc299379684}[]{#_Toc296160153}[]{#_Toc299379685}[]{#_Toc296160154}[]{#_Toc299379686}[]{#_Toc296160155}[]{#_Toc299379687}[]{#_Toc296160156}[]{#_Toc299379688}[]{#_Toc296160158}[]{#_Toc299379690}[]{#_Toc296160160}[]{#_Toc299379692}[]{#_Toc296160161}[]{#_Toc299379693}[]{#_Toc296160164}[]{#_Toc299379696}[]{#_Toc296160165}[]{#_Toc299379697}[]{#_Toc296160166}[]{#_Toc299379698}[]{#_Toc296160167}[]{#_Toc299379699}[]{#_Toc296160168}[]{#_Toc299379700}[]{#_Toc296160169}[]{#_Toc299379701}[]{#_Toc296160170}[]{#_Toc299379702}[]{#_Toc296160171}[]{#_Toc299379703}[]{#_Toc296160172}[]{#_Toc299379704}[]{#_Toc296160173}[]{#_Toc299379705}[]{#_Toc296160174}[]{#_Toc299379706}[]{#_Toc296160175}[]{#_Toc299379707}[]{#_Toc296160176}[]{#_Toc299379708}[]{#_Toc296160177}[]{#_Toc299379709}[]{#_Toc296160178}[]{#_Toc299379710}[]{#_Toc296160179}[]{#_Toc299379711}[]{#_Toc296160180}[]{#_Toc299379712}[]{#_Toc296160181}[]{#_Toc299379713}[]{#_Toc296160183}[]{#_Toc299379715}[]{#_Toc296160184}[]{#_Toc299379716}[]{#_Toc296160185}[]{#_Toc299379717}[]{#_Toc296160186}[]{#_Toc299379718}[]{#_Toc296160189}[]{#_Toc299379721}[]{#_Toc296160190}[]{#_Toc299379722}[]{#_Toc296160191}[]{#_Toc299379723}[]{#_Toc296160192}[]{#_Toc299379724}[]{#_Toc296160194}[]{#_Toc299379726}[]{#_Toc296160195}[]{#_Toc299379727}[]{#_Toc296160196}[]{#_Toc299379728}[]{#_Toc296160197}[]{#_Toc299379729}[]{#_Toc296160198}[]{#_Toc299379730}[]{#_Toc296160199}[]{#_Toc299379731}[]{#_Toc296160200}[]{#_Toc299379732}[]{#_Toc296160201}[]{#_Toc299379733}[]{#_Toc296160202}[]{#_Toc299379734}[]{#_Toc296160203}[]{#_Toc299379735}[]{#_Toc296160204}[]{#_Toc299379736}[]{#_Toc296160205}[]{#_Toc299379737}[]{#_Toc296160206}[]{#_Toc299379738}[]{#_Toc296160208}[]{#_Toc299379740}[]{#_Toc296160209}[]{#_Toc299379741}[]{#_Toc296160210}[]{#_Toc299379742}[]{#_Toc296160211}[]{#_Toc299379743}[]{#_Toc296160214}[]{#_Toc299379746}

**MLD \-- MLD配置命令 \-- mld static-group**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **static-group**]{lang="EN-US"}]{#struct_0_42457_14668_1270539481}[命令用来配置接口静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组或组播源组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **static-group**]{lang="EN-US"}]{#struct_0_42457_14668_216341241}[命令用来]{style="font-family:宋体"}[恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1371746566}

[**[mld]{lang="EN-US"}**[ **static-group** *ipv6-group-address* \[ **source** *ipv6-source-address* \] \[ **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* \]]{lang="EN-US"}]{#struct_0_42457_14668_736620622}

[**[undo]{lang="EN-US"}**[ **mld** **static-group** { **all** \| *ipv6-group-address* \[ **source** *ipv6-source-address* \] \[ **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* \] }]{lang="EN-US"}]{#struct_0_42457_14668_x1368984152}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_1896877616}

[[接口没有以静态方式加入任何]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x107426753}[组播组或组播源组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1486234981}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_x868003928}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1270605017}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x634154347}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_221056927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x2146686715}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_42457_14668_x737441416}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。]{style="font-family:
宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_42457_14668_x2076283400}[：指定组播源的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。如果未指定本参数，表示针对所有组播源。]{style="font-family:宋体"}

[**[dot1q]{lang="EN-US"}**[ **vid** *vlan-list*]{lang="EN-US"}]{#struct_0_42457_14668_42830181}[：指定封装的第一层]{style="font-family:
宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:
宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[dot1q]{lang="EN-US"}**[ **vid** *vlan-id* **second-dot1q** *vlan-list*]{lang="EN-US"}]{#struct_0_42457_14668_x41041350}[：指定封装的第一层和第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[；]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_42457_14668_x1760472244}[：删除此接口加入的所有静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x537930564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_42457_14668_x1537350923}[IPv6]{lang="EN-US"}[组播组地址在]{style="font-family:宋体"}[SSM]{lang="EN-US"}[组地址范围内，则必须同时指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的地址，否则将不会生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由表项用于指导组播转发；如果指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址不在]{style="font-family:宋体"}[SSM]{lang="EN-US"}[组地址范围内，则无此限制。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于同一个]{style="font-family:宋体"}]{#struct_0_42457_14668_42764645}[IPv6]{lang="EN-US"}[组播组或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组，不带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[封装、带一层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[封装和带两层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[封装的静态加入配置两两互斥，不允许同时配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置不带]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_42457_14668_1441920791}[封装的静态加入]{lang="EN-US" style="font-family:宋体"}[时]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[如果子]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[上没有]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}**[mld]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}[命令]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}**[mld]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令，]{lang="EN-US" style="font-family:宋体"}[才]{style="font-family:宋体"}[生成]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态]{lang="EN-US" style="font-family:宋体"}[组播]{style="font-family:宋体"}[表项。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置带]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_42457_14668_43747685}[封装的静态加入时，]{lang="EN-US" style="font-family:宋体"}[如果子]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[配置了]{lang="EN-US" style="font-family:宋体"}**[mld]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}[命令，]{lang="EN-US" style="font-family:宋体"}[那么当相应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[用户上线时]{lang="EN-US" style="font-family:宋体"}[才]{style="font-family:宋体"}[生成]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态]{lang="EN-US" style="font-family:宋体"}[组播]{style="font-family:宋体"}[表项；]{lang="EN-US" style="font-family:宋体"}[如果子接口上]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}**[mld]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令，]{lang="EN-US" style="font-family:宋体"}[那么只有二者的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[封装相同，]{lang="EN-US" style="font-family:宋体"}[才]{style="font-family:宋体"}[生成]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态]{lang="EN-US" style="font-family:宋体"}[组播]{style="font-family:宋体"}[表项。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_583153722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_1271063766}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_555985320}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x1621969709}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld static-group ff03::101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x345840532}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组（]{style="font-family:宋体"}[2001::101]{lang="EN-US"}[，]{style="font-family:宋体"}[FF3E::202]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x1708256813}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld static-group ff3e::202 source 2001::101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_43682149}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[按会话记录用户加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组，并静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[：当第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[、第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[的用户上线时才生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态组播表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1494423002}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] mld join-by-session]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] mld static-group ff03::101 dot1q vid 10 second-dot1q 10 to 20]{lang="EN-US"}

[]{#_Toc136854391}[]{#struct_0_42457_14668_1157084348}[]{#_mld_timer_other-querier-present}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_803033769}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1271129302}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld static-group ff03::101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x189457547}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组（]{style="font-family:宋体"}[2001::101]{lang="EN-US"}[，]{style="font-family:宋体"}[FF3E::202]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_462594751}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld static-group ff3e::202 source 2001::101]{lang="EN-US"}
:::

::::: {#89509420 .myid}
[]{#_Toc404790301}[]{#struct_0_42457_14668_43223396}[]{#_Toc372127984}[]{#_Toc372127327}[]{#_Toc370719720}[]{#_Toc363576228}

**MLD \-- MLD配置命令 \-- mld user-vlan-aggregation dot1q**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_42457_14668_1110114356}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_42457_14668_529717111}
:::

[ ]{lang="EN-US"}

[**[mld]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}]{#struct_0_42457_14668_1729445108}[命令用来配置为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播报文封装的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **user-vlan-aggregation** **dot1q**]{lang="EN-US"}]{#struct_0_42457_14668_43157860}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1467752960}

[**[mld]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q** **vid** *vlan-id* \[ **second-dot1q** *vlan-id* \]]{lang="EN-US"}]{#struct_0_42457_14668_334249877}

[**[undo]{lang="EN-US"}**[ **mld** **user-vlan-aggregation** **dot1q**]{lang="EN-US"}]{#struct_0_42457_14668_43092324}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x700831146}

[[不为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x421173636}[组播报文封装]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_43026788}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_42457_14668_x1863862168}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x177884444}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_42961252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x606493155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x577995573}

[**[vid]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_42457_14668_42895716}[：指定封装的第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[second-dot1q]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_42457_14668_1838930864}[：指定封装的第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x390261770}

[**[mld]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_42457_14668_42830180}[命令与]{style="font-family:宋体"}**[mld]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令互斥，不允许同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1997356486}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_524894056}[在子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[上配置为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播报文封装的第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[，第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_42764644}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] mld user-vlan-aggregation dot1q vid 10 second-dot1q 20]{lang="EN-US"}
:::::

::: {#1734238503 .myid}
[]{#_Toc87351923}[]{#_Toc87265559}[]{#_Toc82920352}[]{#_Toc404790302}[]{#struct_0_42457_14668_61188345}[]{#_Toc136854393}[]{#_Toc307402362}[]{#_Toc307402363}[]{#_Toc296160217}[]{#_Toc299379749}[]{#_Toc296160218}[]{#_Toc299379750}[]{#_Toc296160220}[]{#_Toc299379752}[]{#_Toc296160221}[]{#_Toc299379753}[]{#_Toc296160222}[]{#_Toc299379754}[]{#_Toc296160223}[]{#_Toc299379755}[]{#_Toc296160224}[]{#_Toc299379756}[]{#_Toc296160225}[]{#_Toc299379757}[]{#_Toc296160226}[]{#_Toc299379758}[]{#_Toc296160227}[]{#_Toc299379759}[]{#_Toc296160228}[]{#_Toc299379760}[]{#_Toc296160229}[]{#_Toc299379761}[]{#_Toc296160230}[]{#_Toc299379762}[]{#_Toc296160231}[]{#_Toc299379763}[]{#_Toc296160232}[]{#_Toc299379764}[]{#_Toc296160234}[]{#_Toc299379766}[]{#_mld_timer_query}[]{#_Toc296160236}[]{#_Toc299379768}[]{#_Toc296160237}[]{#_Toc299379769}[]{#_Toc296160239}[]{#_Toc299379771}[]{#_Toc296160242}[]{#_Toc299379774}[]{#_Toc296160243}[]{#_Toc299379775}[]{#_Toc296160245}[]{#_Toc299379777}[]{#_Toc296160246}[]{#_Toc299379778}[]{#_Toc296160247}[]{#_Toc299379779}[]{#_Toc296160248}[]{#_Toc299379780}[]{#_Toc296160249}[]{#_Toc299379781}[]{#_Toc296160250}[]{#_Toc299379782}[]{#_Toc296160251}[]{#_Toc299379783}[]{#_Toc296160252}[]{#_Toc299379784}[]{#_Toc296160253}[]{#_Toc299379785}[]{#_Toc296160254}[]{#_Toc299379786}[]{#_Toc296160255}[]{#_Toc299379787}[]{#_Toc296160256}[]{#_Toc299379788}[]{#_Toc296160257}[]{#_Toc299379789}[]{#_Toc296160259}[]{#_Toc299379791}[]{#_mld_version}[]{#_Toc296160261}[]{#_Toc299379793}[]{#_Toc296160262}[]{#_Toc299379794}[]{#_Toc296160264}[]{#_Toc299379796}

**MLD \-- MLD配置命令 \-- mld version**

------------------------------------------------------------------------

[**[mld]{lang="EN-US"}**[ **version**]{lang="EN-US"}]{#struct_0_42457_14668_1355794167}[命令用来在接口上配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[的版本。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld** **version**]{lang="EN-US"}]{#struct_0_42457_14668_769610314}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_2131681594}

[**[mld]{lang="EN-US"}**[ **version** *version-number*]{lang="EN-US"}]{#struct_0_42457_14668_x503868358}

[**[undo]{lang="EN-US"}**[ **mld** **version**]{lang="EN-US"}]{#struct_0_42457_14668_1271194838}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_1330251603}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_544841922}[的版本为]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1587327797}

[[接口视图]{style="font-family:宋体"}]{#struct_0_42457_14668_120251651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1979577218}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1495954041}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x510443702}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_1866691787}

[*[version-number]{lang="EN-US"}*]{#struct_0_42457_14668_1849542701}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1271260374}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x1408092854}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_913599018}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使用]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x775277564}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld version 2]{lang="EN-US"}

[]{#_Toc136854394}[]{#_Toc103401227}[]{#struct_0_42457_14668_x238860067}[]{#_multicast_ipv6_routing-enable_1}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1730077461}[指定接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[使用]{style="font-family:宋体"}[MLDv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x540494001}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] mld version 2]{lang="EN-US"}
:::

::: {#-2009010439 .myid}
[]{#_Toc404790303}[]{#struct_0_42457_14668_43747684}[]{#_Toc372212394}[]{#_Toc372205819}[]{#_Toc371343408}[]{#_Toc368325568}[]{#_Toc368294507}

**MLD \-- MLD配置命令 \-- other-querier-present-timeout (MLD view)**

------------------------------------------------------------------------

[**[other-querier-present-timeout]{lang="EN-US"}**]{#struct_0_42457_14668_43682148}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[其它查询器的存在时间。]{style="font-family:宋体"}

[**[undo other-querier-present-timeout]{lang="EN-US"}**]{#struct_0_42457_14668_x844229158}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1045899802}

[**[other-querier-present-timeout]{lang="EN-US"}***[ ]{lang="EN-US"}[time]{lang="EN-US"}*]{#struct_0_42457_14668_1609307334}

[**[undo other-querier-present-timeout]{lang="EN-US"}**]{#struct_0_42457_14668_x1148091942}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1210388596}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1609241798}[其它查询器的存在时间＝]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔×]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数＋]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间÷]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1227790527}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1789342593}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609176262}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1526985466}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1114986482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609110726}

[*[time]{lang="EN-US"}*]{#struct_0_42457_14668_x1511644212}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[其它查询器的存在时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1717912845}

[[本命令与]{style="font-family:宋体"}**[mld other-querier-present-timeout]{lang="EN-US"}**]{#struct_0_42457_14668_1609045190}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x358716695}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_895629075}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[其它查询器的存在时间为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1608979654}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] other-querier-present-timeout 125]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1918419912}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld ]{lang="EN-US"}[other-querier-present-timeout]{lang="EN-US"}**]{#struct_0_42457_14668_2117787868}
:::

::: {#-977543516 .myid}
[]{#_Toc404790304}[]{#struct_0_42457_14668_569768595}[]{#_Toc364955783}

**MLD \-- MLD配置命令 \-- proxy multipath (MLD view)**

------------------------------------------------------------------------

[**[proxy]{lang="EN-US"}**[ **multipath**]{lang="EN-US"}]{#struct_0_42457_14668_x1056135612}[命令用来使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理的负载分担功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **proxy** **multipath**]{lang="EN-US"}]{#struct_0_42457_14668_569703059}[命令用来关闭]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理的负载分担功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1371883441}

[**[proxy]{lang="EN-US"}**[ **multipath**]{lang="EN-US"}]{#struct_0_42457_14668_570161811}

[**[undo]{lang="EN-US"}**[ **proxy** **multipath**]{lang="EN-US"}]{#struct_0_42457_14668_1907800196}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_570096275}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1170724701}[代理的负载分担功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x996446413}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_2027622234}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x996511949}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1810321041}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_71735238}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x996577485}

[[当在]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x695166295}[代理设备的多个接口上使能了]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理功能时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果关闭了]{style="font-family:宋体"}]{#struct_0_42457_14668_x996643021}[MLD]{lang="EN-US"}[代理的负载分担功能，则只有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址最大的接口会转发]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播流量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使能了]{style="font-family:宋体"}]{#struct_0_42457_14668_503564436}[MLD]{lang="EN-US"}[代理的负载分担功能，则可通过这些接口对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播流量按组进行负载分担。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x996184269}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1463420920}[在公网实例中使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理的负载分担功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x996249805}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] proxy multipath]{lang="EN-US"}
:::

::: {#16446600 .myid}
[]{#_Toc404790305}[]{#struct_0_42457_14668_1608848582}[]{#_Toc372212396}[]{#_Toc372205821}[]{#_Toc371343410}[]{#_Toc368325569}[]{#_Toc368294508}

**MLD \-- MLD配置命令 \-- query-interval (MLD view)**

------------------------------------------------------------------------

[**[query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1609831622}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x734226562}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1985152844}

[**[query-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_42457_14668_x743877124}

[**[undo query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1609766086}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1907290938}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1146182727}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609307333}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1147764262}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_527540351}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1609241797}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1228642495}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_820059355}

[*[interval]{lang="EN-US"}*]{#struct_0_42457_14668_1609176261}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1527051002}

[[本命令与]{style="font-family:宋体"}**[mld query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x1217090356}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609110725}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1511447604}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1275974073}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] query-interval 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609045189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld ]{lang="EN-US"}[query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x359306520}
:::

::: {#-878812909 .myid}
[]{#_Toc404790306}[]{#struct_0_42457_14668_342376161}[]{#_Toc136854398}[]{#_prompt-leave}[]{#_require-router-alert}[]{#_Toc299379799}[]{#_Toc299379800}[]{#_Toc299379801}[]{#_Toc299379803}[]{#_Toc299379804}[]{#_Toc299379805}[]{#_Toc299379806}[]{#_Toc299379807}[]{#_Toc299379808}[]{#_Toc299379809}[]{#_Toc299379810}[]{#_Toc299379811}[]{#_Toc299379812}[]{#_Toc299379813}[]{#_Toc299379814}[]{#_Toc157315339}[]{#_Toc157315340}[]{#_Toc157315341}[]{#_Toc157315342}[]{#_Toc157315343}[]{#_Toc157315344}[]{#_Toc157315345}[]{#_Toc157315346}[]{#_Toc157315347}[]{#_Toc157315348}[]{#_Toc157315349}[]{#_Toc157315350}[]{#_Toc157315351}[]{#_Toc157315352}[]{#_Toc157315353}[]{#_Toc157315355}[]{#_Toc157315356}[]{#_Toc157315357}[]{#_Toc157315358}[]{#_Toc157315360}[]{#_Toc157315361}

**MLD \-- MLD配置命令 \-- reset mld group**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **mld** **group**]{lang="EN-US"}]{#struct_0_42457_14668_1271325910}[命令用来清除]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_580817660}

[**[reset]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \] **group** ]{lang="EN-US"}[{ **all** \| **interface** *interface-type interface-number* { **all** \| *ipv6-group-address* \[ *prefix-length* \] \[ *ipv6-source-address* \[ *prefix-length* \] \] } }]{lang="EN-US"}]{#struct_0_42457_14668_1359543293}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1473722714}

[[用户视图]{style="font-family:宋体"}]{#struct_0_42457_14668_307163830}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1622308881}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_320099696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1265632125}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1389347650}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_42457_14668_1271391446}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的记录，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的记录。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_42457_14668_1335017611}[：前一个]{style="font-family:宋体"}**[all]{lang="EN-US"}**[表示清除所有接口上的记录，后一个]{style="font-family:宋体"}**[all]{lang="EN-US"}**[表示清除所有组播组的记录。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_42457_14668_x1307855031}[：清除指定接口上的记录。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_42457_14668_184369221}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的记录，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。]{style="font-family:
宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_42457_14668_x1085384099}[：清除指定组播源的记录。如果未指定本参数，将清除所有组播源的记录。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_42457_14668_x765213479}[：指定组播源或组播组地址的前缀长度。对于组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[；对于组播组地址，其取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x355369363}

[[执行本命令可能导致接收者中断]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_42457_14668_x1292495617}[组播信息的接收。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1271456982}

[]{#_Toc136854399}[]{#_Toc107805423}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_162394157}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_956213080}[清除公网实例所有接口上]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset mld group all]{lang="EN-US"}]{#struct_0_42457_14668_1144746420}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_778274773}[清除公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset mld group interface gigabitethernet 1/0/1 all]{lang="EN-US"}]{#struct_0_42457_14668_x1115178248}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x362513760}[清除公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101:10]{lang="EN-US"}[的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset mld group interface gigabitethernet 1/0/1 ff03::101:10]{lang="EN-US"}]{#struct_0_42457_14668_69500664}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_42457_14668_x157984563}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1271522518}[清除公网实例所有接口上]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset mld group all]{lang="EN-US"}]{#struct_0_42457_14668_x1383916133}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x2145356168}[清除公网实例接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上所有]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset mld group interface vlan-interface 100 all]{lang="EN-US"}]{#struct_0_42457_14668_2065252585}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x494391225}[清除公网实例接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[MLD]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101:10]{lang="EN-US"}[的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset mld group interface vlan-interface 100 ff03::101:10]{lang="EN-US"}]{#struct_0_42457_14668_432582955}[]{#_Toc296160270}[]{#_Toc296160272}[]{#_Toc296160273}[]{#_Toc296160274}[]{#_Toc296160275}[]{#_Toc296160276}[]{#_Toc296160277}[]{#_Toc296160278}[]{#_Toc296160279}[]{#_Toc296160280}[]{#_Toc296160281}[]{#_Toc296160282}[]{#_Toc296160283}[]{#_Toc296160284}[]{#_Toc296160285}[]{#_Toc296160286}[]{#_Toc296160287}[]{#_Toc296160288}[]{#_Toc296160289}[]{#_Toc296160290}[]{#_Toc296160292}[]{#_Toc296160294}[]{#_Toc168110757}[]{#_Toc168110758}[]{#_Toc296160296}[]{#_Toc296160297}[]{#_Toc296160299}[]{#_Toc296160300}[]{#_Toc296160301}[]{#_Toc296160302}[]{#_Toc296160303}[]{#_Toc296160304}[]{#_Toc296160305}[]{#_Toc296160306}[]{#_Toc296160307}[]{#_Toc296160308}[]{#_Toc296160309}[]{#_Toc296160310}[]{#_Toc296160311}[]{#_Toc296160312}[]{#_Toc296160313}[]{#_Toc296160315}[]{#_Toc296160316}[]{#_Toc296160317}[]{#_Toc296160319}[]{#_Toc296160320}[]{#_Toc296160321}[]{#_Toc296160322}[]{#_Toc296160323}[]{#_Toc296160324}[]{#_Toc296160325}[]{#_Toc296160326}[]{#_Toc296160327}[]{#_Toc296160328}[]{#_Toc296160329}[]{#_Toc296160330}[]{#_Toc296160331}[]{#_Toc296160332}[]{#_Toc296160333}[]{#_Toc296160334}[]{#_Toc296160338}[]{#_Toc296160339}[]{#_Toc296160342}[]{#_Toc296160343}[]{#_Toc296160344}[]{#_Toc296160345}[]{#_Toc296160346}[]{#_Toc296160347}[]{#_Toc296160348}[]{#_Toc296160349}[]{#_Toc296160350}[]{#_Toc296160351}[]{#_Toc296160352}[]{#_Toc296160353}[]{#_timer_other-querier-present}[]{#_Toc296160357}[]{#_Toc296160358}[]{#_Toc296160359}[]{#_Toc296160361}[]{#_Toc296160362}[]{#_Toc296160363}[]{#_Toc296160364}[]{#_Toc296160365}[]{#_Toc296160366}[]{#_Toc296160367}[]{#_Toc296160368}[]{#_Toc296160369}[]{#_Toc296160370}[]{#_Toc296160371}[]{#_Toc296160372}[]{#_Toc296160373}[]{#_Toc296160374}[]{#_Toc296160375}[]{#_Toc296160379}[]{#_Toc296160380}[]{#_Toc296160381}[]{#_Toc296160382}[]{#_Toc296160383}[]{#_Toc296160384}[]{#_Toc296160385}[]{#_Toc296160386}[]{#_Toc296160387}[]{#_Toc296160388}[]{#_Toc296160389}[]{#_Toc296160390}[]{#_Toc296160391}[]{#_Toc296160392}[]{#_Toc296160393}[]{#_Toc296160394}[]{#_Toc296160396}[]{#_Toc296160397}[]{#_Toc296160398}[]{#_Toc296160399}[]{#_Toc296160400}[]{#_Toc296160402}[]{#_Toc296160403}[]{#_Toc296160404}[]{#_Toc296160405}[]{#_Toc296160406}[]{#_Toc296160407}[]{#_Toc296160408}[]{#_Toc296160409}[]{#_Toc296160410}[]{#_Toc296160411}[]{#_Toc296160412}[]{#_Toc296160413}[]{#_Toc296160415}[]{#_Toc296160416}[]{#_Toc296160417}[]{#_Toc296160418}[]{#_Toc296160419}[]{#_Toc296160421}[]{#_Toc296160422}[]{#_Toc296160423}[]{#_Toc296160424}[]{#_Toc296160425}[]{#_Toc296160426}[]{#_Toc296160427}[]{#_Toc296160428}[]{#_Toc296160429}[]{#_Toc296160430}[]{#_Toc296160431}[]{#_Toc296160432}[]{#_timer_query}[]{#_Toc296160436}[]{#_Toc296160437}[]{#_Toc296160438}[]{#_Toc296160440}[]{#_Toc296160441}[]{#_Toc296160442}[]{#_Toc296160443}[]{#_Toc296160444}[]{#_Toc296160445}[]{#_Toc296160446}[]{#_Toc296160447}[]{#_Toc296160448}[]{#_Toc296160449}[]{#_Toc296160450}[]{#_Toc296160451}[]{#_version}[]{#_Toc296160455}[]{#_Toc296160456}[]{#_Toc296160457}[]{#_Toc296160459}[]{#_Toc296160460}[]{#_Toc296160461}[]{#_Toc296160462}[]{#_Toc296160463}[]{#_Toc296160464}[]{#_Toc296160465}[]{#_Toc296160466}[]{#_Toc296160467}[]{#_Toc296160468}[]{#_Toc296160469}[]{#_Toc296160470}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1642936037}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **mld** **group**]{lang="EN-US"}]{#struct_0_42457_14668_x461207795}
:::

::: {#1906058762 .myid}
[]{#_Toc404790307}[]{#struct_0_42457_14668_1608848581}[]{#_Toc372212398}[]{#_Toc372205823}[]{#_Toc371343412}[]{#_Toc368325571}[]{#_Toc368294509}

**MLD \-- MLD配置命令 \-- robust-count (MLD view)**

------------------------------------------------------------------------

[**[robust-count]{lang="EN-US"}**]{#struct_0_42457_14668_x1928411199}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[**[undo robust-count]{lang="EN-US"}**]{#struct_0_42457_14668_1609831621}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x734292098}

[**[robust-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_42457_14668_1546963743}

[**[undo robust-count]{lang="EN-US"}**]{#struct_0_42457_14668_1609766085}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1907225402}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x79036619}[查询器的健壮系数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609307332}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1147698726}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1959533751}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1609241796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_1228708031}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_787077210}

[*[count]{lang="EN-US"}*]{#struct_0_42457_14668_1609176260}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1527116538}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1389575847}[查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器就越"健壮"，但是组播组超时所需的时间也就越长。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{style="font-family:宋体"}]{#struct_0_42457_14668_1609110724}**[mld robust-count]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1511513140}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_1190781661}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1609045188}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] robust-count 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x359240984}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld ]{lang="EN-US"}[robust-count]{lang="EN-US"}**]{#struct_0_42457_14668_1225847263}
:::

::: {#544180404 .myid}
[]{#_Toc404790308}[]{#struct_0_42457_14668_x995987661}[]{#_Toc360707126}[]{#_Toc360705937}[]{#_Toc306713291}[]{#_Toc293993316}

**MLD \-- MLD配置命令 \-- ssm-mapping (MLD view)**

------------------------------------------------------------------------

[**[ssm-mapping]{lang="EN-US"}**]{#struct_0_42457_14668_221289247}[命令用来配置]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ssm-mapping**]{lang="EN-US"}]{#struct_0_42457_14668_x996446414}[命令用来删除]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_2027425626}

[**[ssm-mapping]{lang="EN-US"}**[ *ipv6-source-address* *acl6-number*]{lang="EN-US"}]{#struct_0_42457_14668_x996511950}

[**[undo ssm-mapping]{lang="EN-US"}**[ { *ipv6-source-address* \| **all** }]{lang="EN-US"}]{#struct_0_42457_14668_x1810779792}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_x996577486}

[[未配置]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}]{#struct_0_42457_14668_x695231831}[规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x51793690}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x996643022}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_503367828}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x996184270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1462962167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_x996249806}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_42457_14668_x219673584}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_42457_14668_x996315342}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。通过该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[语句指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的范围。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则表示未指定任何]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_42457_14668_x1868332135}[：删除所有的]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_1091114181}

[[ACL]{lang="EN-US"}]{#struct_0_42457_14668_x213243150}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x996380878}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1405803061}[在公网实例中添加如下一条]{style="font-family:宋体"}[MLD SSM Mapping]{lang="EN-US"}[规则：组地址范围为]{style="font-family:宋体"}[FF3E::/64]{lang="EN-US"}[，对应的源地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x995922126}

[\[Sysname\] acl ipv6 basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2001\] rule permit source ff3e:: 64]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] ssm-mapping 1::1 2001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x995987662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mld ssm-mapping]{lang="EN-US"}**]{#struct_0_42457_14668_221092639}
:::

::: {#799059673 .myid}
[]{#_Toc404790309}[]{#struct_0_42457_14668_1608914116}[]{#_Toc372212400}[]{#_Toc372205825}[]{#_Toc371343414}[]{#_Toc368325572}[]{#_Toc368294510}

**MLD \-- MLD配置命令 \-- startup-query-count (MLD view)**

------------------------------------------------------------------------

[**[startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_1608848580}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询次数。]{style="font-family:宋体"}

[**[undo startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x1928345663}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1707065783}

[**[startup-query-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_42457_14668_1609831620}

[**[undo startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_x734357634}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_1146193021}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_1609766084}[查询器的启动查询次数等于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1907159866}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_2086223732}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609307331}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_x1147895334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x957009019}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609241795}

[*[count]{lang="EN-US"}*]{#struct_0_42457_14668_1228511423}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1901942826}

[[本命令与]{style="font-family:宋体"}**[mld startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_1609176259}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1527575293}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1173269039}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_1609110723}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] startup-query-count 5]{lang="EN-US"}

[]{#_Toc371343415}[]{#_Toc368325573}[]{#_Toc368294511}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1511316532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld ]{lang="EN-US"}[startup-query-count]{lang="EN-US"}**]{#struct_0_42457_14668_1609045187}
:::

::: {#-60396300 .myid}
[]{#_Toc404790310}[]{#struct_0_42457_14668_x358389016}[]{#_Toc372212401}[]{#_Toc372205826}

**MLD \-- MLD配置命令 \-- startup-query-interval (MLD view)**

------------------------------------------------------------------------

[**[startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_x1146805658}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询间隔。]{style="font-family:宋体"}

[**[undo startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1608979651}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1918092232}

[**[startup-query-interval]{lang="EN-US"}***[ ]{lang="EN-US"}[interval]{lang="EN-US"}*]{#struct_0_42457_14668_1782817023}

[**[undo startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1608914115}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_42457_14668_794817837}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1408774392}[查询器的启动查询间隔为]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文发送间隔的]{style="font-family:宋体"}[1/4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_42457_14668_1608848579}

[[MLD]{lang="EN-US"}]{#struct_0_42457_14668_x1928935488}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_42457_14668_207569613}

[[network-admin]{lang="EN-US"}]{#struct_0_42457_14668_1609831619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_42457_14668_x734816387}

[[【参数】]{style="font-family:黑体"}]{#struct_0_42457_14668_1160968680}

[*[interval]{lang="EN-US"}*]{#struct_0_42457_14668_1609766083}[：指定]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_42457_14668_x1907618618}

[[本命令与]{style="font-family:宋体"}**[mld startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_366760548}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609307338}

[[\# ]{lang="EN-US"}]{#struct_0_42457_14668_x1147305510}[在公网实例中全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询器的启动查询间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_42457_14668_x477845682}

[\[Sysname\] mld]{lang="EN-US"}

[\[Sysname-mld\] startup-query-interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_42457_14668_1609241802}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld ]{lang="EN-US"}[startup-query-interval]{lang="EN-US"}**]{#struct_0_42457_14668_1183815878}

[ ]{lang="EN-US"}
:::
