::: {#320779778 .myid}
[]{#_Toc243714555}[]{#_Toc135644047}[]{#_Toc86723807}[]{#_Toc77992827}[]{#_Toc65740896}[]{#_Toc61239702}[]{#_Toc60036174}[]{#_Toc53707118}[]{#_Toc52484714}[]{#_Toc33866008}[]{#_Toc404788833}[]{#struct_0_12376_x3448_1933845132}[]{#_Toc313019151}[]{#_Toc286221458}[]{#_Toc286221461}[]{#_Toc286221462}[]{#_Toc286221463}[]{#_Toc286221464}[]{#_Toc286221465}[]{#_Toc286221466}[]{#_Toc286221467}[]{#_Toc286221468}[]{#_Toc286221469}[]{#_Toc286221470}[]{#_Toc286221471}[]{#_Toc286221472}[]{#_Toc286221473}[]{#_Toc286221474}[]{#_Toc286221475}[]{#_Toc135620205}[]{#_Toc135620208}[]{#_Toc135620209}[]{#_Toc135620210}[]{#_Toc135620211}[]{#_Toc135620212}[]{#_Toc135620213}[]{#_Toc135620214}[]{#_Toc135620215}[]{#_Toc135620216}[]{#_Toc135620217}[]{#_Toc135620218}[]{#_Toc135620219}[]{#_Toc135620220}[]{#_Toc135620221}[]{#_Toc135620222}[]{#_Toc135620223}[]{#_Toc135620224}[]{#_Toc135620225}[]{#_Toc135620226}[]{#_Toc135620227}[]{#_Toc135620234}[]{#_Toc135620248}[]{#_Toc135620249}[]{#_Toc135620256}[]{#_Toc135620257}[]{#_Toc135620261}[]{#_Toc135620263}[]{#_Toc135620264}[]{#_Toc135620277}[]{#_Toc286221476}[]{#_Toc286221477}[]{#_Toc286221478}[]{#_Toc286221479}[]{#_Toc286221480}[]{#_Toc286221481}[]{#_Toc286221482}[]{#_Toc286221483}[]{#_Toc286221484}[]{#_Toc286221485}[]{#_Toc286221486}[]{#_Toc286221487}[]{#_Toc286221488}[]{#_Toc286221489}[]{#_Toc286221490}[]{#_Toc286221491}[]{#_Toc286221492}[]{#_Toc286221493}[]{#_Toc286221494}

**RIPng \-- RIPng配置命令 \-- checkzero**

------------------------------------------------------------------------

[**[checkzero]{lang="EN-US"}**]{#struct_0_12376_x3448_x1291203315}[命令用来使能]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的零域检查功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**]{#struct_0_12376_x3448_1402889662}[ **checkzero**]{lang="EN-US"}[命令用来关闭零域检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2115910747}

[**[checkzero]{lang="EN-US"}**]{#struct_0_12376_x3448_670627671}

[**[undo checkzero]{lang="EN-US"}**]{#struct_0_12376_x3448_1659143941}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1553647396}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_410842266}[报文的零域检查功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1662441929}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1029426652}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x755718714}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_33920898}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1447612613}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1097632192}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1689999694}[报文头部中的一些字段必须配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[，也称为零域。使能]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的零域检查后，如果报文头部零域中的值不为零，这些报文将被丢弃，不做处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1659602693}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_406010785}[关闭进程号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程对]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的零域检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x1002606944}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] undo checkzero]{lang="EN-US"}
:::

::: {#-1740075607 .myid}
[]{#_Toc404788834}[]{#struct_0_12376_x3448_x1907307652}[]{#_Toc313019152}

**RIPng \-- RIPng配置命令 \-- default cost**

------------------------------------------------------------------------

[**[default cost]{lang="EN-US"}**]{#struct_0_12376_x3448_1869626561}[命令用来配置引入路由的缺省度量值。]{style="font-family:宋体"}

[**[undo default cost]{lang="EN-US"}**]{#struct_0_12376_x3448_1669140262}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_755913650}

[**[default cost ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_12376_x3448_x413708343}

[**[undo default cost]{lang="EN-US"}**]{#struct_0_12376_x3448_x840140908}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1659537157}

[[引入路由的缺省度量值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_12376_x3448_1987834923}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1109280984}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_603857956}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1064969992}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1982717327}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x279668571}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1509728790}

[*[value]{lang="EN-US"}*]{#struct_0_12376_x3448_x410274556}[：引入路由的缺省度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1659471621}

[[当使用]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_12376_x3448_x1149128717}[命令从其它协议引入路由时，如果不指定具体的度量值，则引入路由的度量值为]{style="font-family:宋体"}**[default cost]{lang="EN-US"}**[所指定的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1188158723}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1514710277}[配置引入路由的缺省度量值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_2088315496}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] default cost 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x892096164}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_12376_x3448_x989131147}
:::

::: {#-737721681 .myid}
[]{#_Toc404788835}[]{#struct_0_12376_x3448_581548286}

**RIPng \-- RIPng配置命令 \-- display ripng**

------------------------------------------------------------------------

[**[display ripng]{lang="EN-US"}**]{#struct_0_12376_x3448_x98169995}[命令用来显示指定]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的当前运行状态及配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1659406085}

[**[display ripng]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_12376_x3448_x1537644302}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1752677278}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1734085492}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x241075022}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x71781733}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_1710442430}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1815602323}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_548114870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1659864837}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_1167872415}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，则显示所有已配置的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_372259833}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1891225751}[显示所有已配置的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的当前运行状态及配置信息。]{style="font-family:宋体"}

[]{#_Toc60036175}[]{#_Toc53707119}[]{#_Toc52484715}[[\<Sysname\> display ripng]{lang="EN-US"}]{#struct_0_12376_x3448_1463531203}

[  Public VPN-instance name:]{lang="EN-US"}

[ ]{lang="EN-US"}

[    RIPng process: 1]{lang="EN-US"}

[       Preference: 100]{lang="EN-US"}

[           Routing policy: abc]{lang="EN-US"}

[       Checkzero: Enabled]{lang="EN-US"}

[       Default cost: 0]{lang="EN-US"}

[       Maximum number of load balanced routes: 6]{lang="EN-US"}

[       Update time   :   30 secs  Timeout time         :  180 secs]{lang="EN-US"}

[       Suppress time :  120 secs  Garbage-collect time :  120 secs]{lang="EN-US"}

[       Number of periodic updates sent: 256]{lang="EN-US"}

[       Number of trigger updates sent: 1]{lang="EN-US"}

[]{#struct_0_12376_x3448_1714014148}[]{#_Toc86653071}[[表1-1 ]{lang="EN-US"}[display ripng]{lang="EN-US"}]{#_Toc68339148}[命令显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x349162085}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_1659799301}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12376_x3448_1899910380}

[[Public VPN-instance name/Private VPN-instance name]{lang="EN-US"}]{#struct_0_12376_x3448_x251308146}

[[RIPng]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_12376_x3448_x1146906876}[进程运行在公网实例下]{style="font-size:9.0pt;font-family:宋体"}[/RIPng]{lang="EN-US" style="font-size:9.0pt"}[进程应用于指定]{style="font-size:9.0pt;
  font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例]{style="font-size:9.0pt;font-family:宋体"}

[[RIPng Process]{lang="EN-US"}]{#struct_0_12376_x3448_709159894}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x145778256}[进程号]{style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_12376_x3448_727168582}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1659340550}[路由优先级]{style="font-family:宋体"}

[[Routing policy]{lang="EN-US"}]{#struct_0_12376_x3448_x1143593674}

[[路由策略]{style="font-family:宋体"}]{#struct_0_12376_x3448_x151506172}

[[Checkzero]{lang="EN-US"}]{#struct_0_12376_x3448_x764135733}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1975019464}[报文头部的零域检查功能：]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[表示使能，]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[表示未使能]{style="font-family:宋体"}

[[Default cost]{lang="EN-US"}]{#struct_0_12376_x3448_x801367142}

[[引入路由的缺省度量值]{style="font-family:宋体"}]{#struct_0_12376_x3448_1659275014}

[[Maximum number of load balanced routes]{lang="EN-US"}]{#struct_0_12376_x3448_1202249292}

[[等价路由的最大数目]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1256440426}

[[Update time]{lang="EN-US"}]{#struct_0_12376_x3448_1610225928}

[[Update]{lang="EN-US"}]{#struct_0_12376_x3448_741172021}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Timeout time]{lang="EN-US"}]{#struct_0_12376_x3448_1631906523}

[[Timeout]{lang="EN-US"}]{#struct_0_12376_x3448_1659209478}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Suppress time]{lang="EN-US"}]{#struct_0_12376_x3448_x1185720942}

[[Suppress]{lang="EN-US"}]{#struct_0_12376_x3448_136544344}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Garbage-collect time]{lang="EN-US"}]{#struct_0_12376_x3448_x58478315}

[[Garbage-Collect]{lang="EN-US"}]{#struct_0_12376_x3448_1638387828}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Number of periodic updates sent]{lang="EN-US"}]{#struct_0_12376_x3448_1659143942}

[[定时发送的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1553844004}[更新报文的统计数量]{style="font-family:宋体"}

[[Number of trigger updates sent]{lang="EN-US"}]{#struct_0_12376_x3448_x1566289508}

[[触发发送的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1864095818}[更新报文的统计数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1639489666 .myid}
[]{#_Toc404788836}[]{#struct_0_12376_x3448_x1108108590}[]{#_Toc243714556}[]{#_Toc135644048}[]{#_Toc86723808}[]{#_Toc77992828}[]{#_Toc65740897}[]{#_Toc61239703}

**RIPng \-- RIPng配置命令 \-- display ripng database**

------------------------------------------------------------------------

[**[display ripng database]{lang="EN-US"}**]{#struct_0_12376_x3448_1659602694}[命令用来显示指定]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程发布数据库的所有激活路由。这些路由以常规]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[更新报文的形式发送。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_405683105}

[**[display ripng]{lang="EN-US"}**[ *process-id* **database** \[ *ipv6-address prefix-length* \]]{lang="EN-US"}]{#struct_0_12376_x3448_x1736992248}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1705093291}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x955433599}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_635212991}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1461700761}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_57582765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x741385936}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_1659537158}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1986851883}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_x2102515}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}***[ ]{lang="EN-US"}***[prefix-length]{lang="EN-US"}*]{#struct_0_12376_x3448_x803373245}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的激活路由信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2114159510}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x796006942}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程发布数据库中的激活路由。]{style="font-family:宋体"}

[]{#_Toc60036176}[]{#_Toc53707120}[]{#_Toc52484716}[[\<Sysname\> display ripng 1 database]{lang="EN-US"}]{#struct_0_12376_x3448_1155337842}

[   1::/64,]{lang="EN-US"}

[        cost 0, RIPng-interface]{lang="EN-US"}

[   10::/32,]{lang="EN-US"}

[        cost 0, imported]{lang="EN-US"}

[   2::2/128,]{lang="EN-US"}

[       via FE80::20C:29FF:FE7A:E3E4, cost 1]{lang="EN-US"}

[]{#struct_0_12376_x3448_1659471622}[]{#_Toc86653072}[[表1-2 ]{lang="EN-US"}[display ripng database]{lang="EN-US"}]{#_Toc68339149}[命令显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x319483746}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1149063181}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1521341403}

[[cost]{lang="EN-US"}]{#struct_0_12376_x3448_488124300}

[[度量值]{style="font-family:宋体"}]{#struct_0_12376_x3448_553840150}

[[RIPng-interface]{lang="EN-US"}]{#struct_0_12376_x3448_224301055}

[[从使能]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1776011430}[协议的接口学来的路由]{style="font-family:宋体"}

[[imported]{lang="EN-US"}]{#struct_0_12376_x3448_1659406086}

[[表示该条路由是从其它路由协议引入的]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1537447694}

[[via]{lang="EN-US"}]{#struct_0_12376_x3448_987812451}

[[下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12376_x3448_1411851613}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1040867339 .myid}
[]{#struct_0_12376_x3448_30134376}[]{#_Toc404788837}

**RIPng \-- RIPng配置命令 \-- display ripng graceful-restart**

------------------------------------------------------------------------

[**[display ripng]{lang="EN-US"}**[ **graceful-restart**]{lang="EN-US"}]{#struct_0_12376_x3448_224029125}[命令用来显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1075424171}

[**[display ripng ]{lang="EN-US"}**[\[ *process-id* \] **graceful-restart**]{lang="EN-US"}]{#struct_0_12376_x3448_29675624}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_199306471}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_723331864}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2122817552}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1930907199}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_634647732}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_29741160}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_x753147766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1015726534}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_1662840317}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1177113284}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x665409157}[显示]{style="font-family:宋体"}[RIPng 1]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ripng 1 graceful-restart]{lang="EN-US"}]{#struct_0_12376_x3448_29806696}

[RIPng process: 1]{lang="EN-US"}

[ Graceful Restart capability    : Enabled]{lang="EN-US"}

[ Current GR state               : Normal]{lang="EN-US"}

[ Graceful Restart period        : 60  seconds]{lang="EN-US"}

[ Graceful Restart remaining time: 0   seconds]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ripng graceful-restart]{lang="EN-US"}]{#struct_0_12376_x3448_x1454295271}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1550777147}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1481468108}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12376_x3448_1586114675}

[[Graceful Restart capability]{lang="EN-US"}]{#struct_0_12376_x3448_1487817155}

[[GR]{lang="EN-US"}]{#struct_0_12376_x3448_29872232}[使能状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_12376_x3448_91419319}[：使能了]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_12376_x3448_x1873958491}[：关闭了]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力]{lang="EN-US" style="font-family:宋体"}

[[Current GR state]{lang="EN-US"}]{#struct_0_12376_x3448_1346669221}

[[当前]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_12376_x3448_x1482400507}[所处状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Under GR]{lang="EN-US"}]{#struct_0_12376_x3448_30462056}[：进程正在]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_12376_x3448_841078276}[：普通状态]{lang="EN-US" style="font-family:宋体"}

[[Graceful Restart period]{lang="EN-US"}]{#struct_0_12376_x3448_481441135}

[[GR]{lang="EN-US"}]{#struct_0_12376_x3448_1022262288}[间隔]{style="font-family:宋体"}

[[Graceful Restart remaining time]{lang="EN-US"}]{#struct_0_12376_x3448_30527592}

[[GR]{lang="EN-US"}]{#struct_0_12376_x3448_x1931328174}[结束剩余时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1755082716 .myid}
[]{#_Toc86723809}[]{#_Toc77992829}[]{#_Toc65740898}[]{#_Toc61239704}[]{#_Toc404788838}[]{#struct_0_12376_x3448_x1847357567}[]{#_Toc243714557}[]{#_Toc135644049}

**RIPng \-- RIPng配置命令 \-- display ripng interface**

------------------------------------------------------------------------

[**[display ripng interface]{lang="EN-US"}**]{#struct_0_12376_x3448_1284892915}[命令用来显示指定]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2029096243}

[**[display ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}*[ **interface** \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_12376_x3448_558054957}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1659864838}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_1167282591}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1972617925}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_269225274}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_x341482833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_907094041}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_x864922631}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1179323102}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_x2013091387}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12376_x3448_1659799302}[：接口类型和编号。如果未指定本参数，则显示指定]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的所有接口信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1899713772}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x612566398}[显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[\<Sysname\> display ripng 1 interface]{lang="EN-US"}]{#struct_0_12376_x3448_199343034}

[ ]{lang="EN-US"}

[ Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[         Link-local address: FE80::20C:29FF:FEC8:B4DD]{lang="EN-US"}

[         Split-horizon: On                Poison-reverse: Off]{lang="EN-US"}

[         MetricIn: 0                      MetricOut: 1]{lang="EN-US"}

[         Default route: Off]{lang="EN-US"}

[         Summary address:]{lang="EN-US"}

[                1::/16]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ripng interface]{lang="EN-US"}]{#struct_0_12376_x3448_1934514213}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x325979118}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1408417267}
:::

[[意义]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713312442}

[[Interface]{lang="EN-US"}]{#struct_0_12376_x3448_767682849}

[[运行]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_696285097}[协议的接口的名称]{style="font-family:宋体"}

[[Link-local address]{lang="EN-US"}]{#struct_0_12376_x3448_x37341362}

[[运行]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x578259172}[协议的接口的链路本地地址]{style="font-family:宋体"}

[[Split-horizon]{lang="EN-US"}]{#struct_0_12376_x3448_73656420}

[[是否使能了水平分割（]{style="font-family:宋体"}[On]{lang="EN-US"}]{#struct_0_12376_x3448_677063801}[表示使能，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示关闭）]{style="font-family:宋体"}

[[Poison-reverse]{lang="EN-US"}]{#struct_0_12376_x3448_x713377978}

[[是否使能了毒性逆转（]{style="font-family:宋体"}[On]{lang="EN-US"}]{#struct_0_12376_x3448_15419119}[表示使能，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示关闭）]{style="font-family:宋体"}

[[MetricIn/MetricOut]{lang="EN-US"}]{#struct_0_12376_x3448_x1882740563}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12376_x3448_2014256571}[发送路由时添加的附加度量值]{style="font-family:宋体"}

[[Default route]{lang="EN-US"}]{#struct_0_12376_x3448_1254613395}

[[是否配置了发布缺省路由以及发布缺省路由的模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12376_x3448_x1350383867}[取消发布缺省路由]{style="font-family:宋体"}[/]{lang="EN-US"}[缺省路由处于]{style="font-family:宋体"}[garbage-collect]{lang="EN-US"}[时间：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置了发布缺省路由：此时从接口发布缺省路由的模式有两种]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_x713443514}[O]{lang="EN-US"}[nly/]{lang="EN-US"}[O]{lang="EN-US"}[riginate]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[O]{lang="EN-US"}[nly]{lang="EN-US"}[表示从接口只发布缺省路由，]{lang="EN-US" style="font-family:宋体"}[O]{lang="EN-US"}[riginate]{lang="EN-US"}[表示同时发布缺省路由和其他]{lang="EN-US" style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由。处于这种状态时，路由器相应的显示：]{lang="EN-US" style="font-family:宋体"}[Default route: ]{lang="EN-US"}[O]{lang="EN-US"}[nly]{lang="EN-US"}[，或者]{lang="EN-US" style="font-family:宋体"}[Default route:]{lang="EN-US"}[ O]{lang="EN-US"}[riginate]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[取消发布缺省路由：表示当前没有配置发布缺省路由或者是取消发布默认路由后]{lang="EN-US" style="font-family:宋体"}[garbage-collect]{lang="EN-US"}]{#struct_0_12376_x3448_x6785844}[已经超时，此时接口不发送]{lang="EN-US" style="font-family:
  宋体"}[RIPng]{lang="EN-US"}[的缺省路由。处于这种状态时，路由器显示：]{lang="EN-US" style="font-family:宋体"}[Default route: ]{lang="EN-US"}[O]{lang="EN-US"}[ff]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省路由正处于]{lang="EN-US" style="font-family:宋体"}[garbage-collect]{lang="EN-US"}]{#struct_0_12376_x3448_x1837042129}[时间]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}[取消发布缺省路由配置后，缺省路由会进入]{lang="EN-US" style="font-family:宋体"}[garbage-collect]{lang="EN-US"}[状态，此时从接口发送]{lang="EN-US" style="font-family:宋体"}[metric]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[16]{lang="EN-US"}[的缺省路由。处于这种状态时，路由器显示：]{lang="EN-US" style="font-family:宋体"}[Default route: In garbage-collection status (]{lang="EN-US"}*[x]{lang="EN-US"}*[s)]{lang="EN-US"}

[[Default route cost]{lang="EN-US"}]{#struct_0_12376_x3448_x1461593560}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1372392263}[接口下配置发布缺省路由的]{style="font-family:宋体"}[cost]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Summary address]{lang="EN-US"}]{#struct_0_12376_x3448_x713509050}

[[在接口配置的聚合的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12376_x3448_x1200356675}[地址以及被聚合的路由的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1290722923 .myid}
[]{#_Toc404788839}[]{#struct_0_12376_x3448_30134373}

**RIPng \-- RIPng配置命令 \-- display ripng neighbor**

------------------------------------------------------------------------

[**[display ripng neighbor]{lang="EN-US"}**]{#struct_0_12376_x3448_1415670213}[命令用来显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2117794590}

[**[display ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ neighbor]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_12376_x3448_x2034956821}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_29675621}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1374671641}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_87141871}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1645374155}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_x577277553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1333770016}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_29741157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1923841351}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_x1094900065}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12376_x3448_x2059053172}[：接口类型和编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[的所有邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x436307707}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_587564129}[显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display ripng 1 neighbor]{lang="EN-US"}]{#struct_0_12376_x3448_29806693}

[Neighbor Address: FE80::230:FF:FE00:0]{lang="EN-US"}

[     Interface  : Vlan-interface1]{lang="EN-US"}

[     Version    : RIPng version 1     Last update: 00h00m27s]{lang="EN-US"}

[     Bad packets: 0                   Bad routes : 0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ripng neighbor]{lang="EN-US"}]{#struct_0_12376_x3448_1649030937}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1572355121}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_x159431720}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12376_x3448_1012563440}

[[Version]{lang="EN-US"}]{#struct_0_12376_x3448_29872229}

[[收到邻居]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1230536220}[报文的版本]{style="font-family:宋体"}

[[Last update]{lang="EN-US"}]{#struct_0_12376_x3448_x1209390272}

[[上次收到邻居更新报文距离现在时间]{style="font-family:宋体"}]{#struct_0_12376_x3448_30462053}

[]{#_Toc375236033}[[ ]{lang="EN-US"}]{#_Toc369852595}

::: {#1692442076 .myid}
[]{#_Toc404788840}[]{#struct_0_12376_x3448_x1879910908}

**RIPng \-- RIPng配置命令 \-- display ripng non-stop-routing**

------------------------------------------------------------------------

[**[display ripng]{lang="EN-US"}**[ **non-stop-routing**]{lang="EN-US"}]{#struct_0_12376_x3448_x1810379097}[命令用来显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_812624485}

[**[display ripng]{lang="EN-US"}**[ \[ *process-id* \] **non-stop-routing**]{lang="EN-US"}]{#struct_0_12376_x3448_194018108}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1924905034}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_30527589}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1224522221}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_349772913}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_x816630054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_2059588322}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_761773449}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_29937766}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_1220882886}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1353966570}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1753881133}[显示]{style="font-family:宋体"}[RIPng 1]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ripng 1 non-stop-routing]{lang="EN-US"}]{#struct_0_12376_x3448_30003302}

[RIPng process: 1]{lang="EN-US"}

[ Nonstop Routing capability: Enabled]{lang="EN-US"}

[ Current NSR state         : Finish]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ripng non-stop-routing]{lang="EN-US"}]{#struct_0_12376_x3448_x1330310166}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1567604889}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1176758238}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12376_x3448_x35015198}

[[Nonstop Routing capability]{lang="EN-US"}]{#struct_0_12376_x3448_x2074903197}

[[NSR]{lang="EN-US"}]{#struct_0_12376_x3448_30068838}[使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_12376_x3448_x108355768}[：使能]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_12376_x3448_x1712113650}[：不使能]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}

[[Current NSR state]{lang="EN-US"}]{#struct_0_12376_x3448_30134374}

[[当前]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_12376_x3448_606366149}[所处状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initialization]{lang="EN-US"}]{#struct_0_12376_x3448_x1158174283}[：]{style="font-family:宋体"}[初始准备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Smooth]{lang="EN-US"}]{#struct_0_12376_x3448_493005019}[：]{style="font-family:宋体"}[数据平滑]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advertising]{lang="EN-US"}]{#struct_0_12376_x3448_29675622}[：]{style="font-family:宋体"}[发布路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redistribution]{lang="EN-US"}]{#struct_0_12376_x3448_581643495}[：]{style="font-family:宋体"}[路由引入处理]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_12376_x3448_898221844}[：]{style="font-family:宋体"}[完成]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1018723638 .myid}
[]{#_Toc404788841}[]{#struct_0_12376_x3448_x924754591}[]{#_Toc243714558}[]{#_Toc135644050}

**RIPng \-- RIPng配置命令 \-- display ripng route**

------------------------------------------------------------------------

[**[display ripng route]{lang="EN-US"}**]{#struct_0_12376_x3448_766586648}[命令用来显示指定]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x533137689}

[**[display ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ route ]{lang="EN-US"}**[\[ *ipv6-address* *prefix-length* \[ **verbose** \] \| **peer** *ipv6-address* \| **statistics** \]]{lang="EN-US"}]{#struct_0_12376_x3448_1816757302}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1084917409}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_765912773}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1603918635}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x713050298}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_776524209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_440148802}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_288863297}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1978105344}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_x20658038}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-address prefix-length]{lang="EN-US"}*]{#struct_0_12376_x3448_x1479282357}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的路由信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_12376_x3448_456296647}[：显示当前]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由表中的指定前缀路由的所有路由信息。如果未指定本参数，则只显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的地址和前缀的最优]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_12376_x3448_1113651488}[：显示从指定邻居]{style="font-family:宋体"}[学到的所有路由信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_12376_x3448_x713115834}[：显示路由的统计信息。路由的统计信息包括路由总数目，各个邻居的路由数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x766431253}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1873516003}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display ripng 1 route]{lang="EN-US"}]{#struct_0_12376_x3448_658763782}

[   Route Flags: A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct]{lang="EN-US"}

[                O - Optimal, F - Flush to RIB]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Peer FE80::20C:29FF:FED4:7171 on GigabitEthernet1/0/2]{lang="EN-US"}

[ Destination 4::4/128,]{lang="EN-US"}

[     via FE80::20C:29FF:FED4:7171, cost 1, tag 0, AOF, 5 secs]{lang="EN-US"}

[ Local route]{lang="EN-US"}

[ Destination 3::3/128,]{lang="EN-US"}

[     via ::, cost 0, tag 0, DOF]{lang="EN-US"}

[ Destination 6::/64,]{lang="EN-US"}

[     via ::, cost 0, tag 0, DOF]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x713181370}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程中指定地址]{style="font-family:宋体"}[3::3/128]{lang="EN-US"}[的所有路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display ripng 1 route 3::3 128 verbose]{lang="EN-US"}]{#struct_0_12376_x3448_x713246906}

[   Route Flags: A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct]{lang="EN-US"}

[                O - Optimal, F - Flush to RIB]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Local route]{lang="EN-US"}

[ Destination 3::3/128,]{lang="EN-US"}

[     via ::, cost 0, tag 0, DOF]{lang="EN-US"}

[]{#struct_0_12376_x3448_x1541162192}[]{#_Toc86653073}[[表1-7 ]{lang="EN-US"}[display ripng route]{lang="EN-US"}]{#_Toc68339150}[命令显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x323016993}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_1010728300}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1228232292}

[[A - Aging]{lang="EN-US"}]{#struct_0_12376_x3448_138675018}

[[此路由项处于老化状态]{style="font-family:宋体"}]{#struct_0_12376_x3448_506623753}

[[S - Suppressed]{lang="EN-US"}]{#struct_0_12376_x3448_136278852}

[[此路由项处于抑制状态]{style="font-family:宋体"}]{#struct_0_12376_x3448_x712788154}

[[G - Garbage-collect]{lang="EN-US"}]{#struct_0_12376_x3448_x1194756198}

[[此路由项处于]{style="font-family:宋体"}[Garbage-collect]{lang="EN-US"}]{#struct_0_12376_x3448_1132478726}[状态]{style="font-family:宋体"}

[[D - Direct]{lang="EN-US"}]{#struct_0_12376_x3448_x1459308175}

[[此路由项是]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x712853690}[生成的直连路由]{style="font-family:宋体"}

[[Local route]{lang="PT-BR"}]{#struct_0_12376_x3448_396326232}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1614334912}[本地生成的直连路由]{style="font-family:宋体"}

[[O - Optimal]{lang="EN-US"}]{#struct_0_12376_x3448_x713312441}

[[此路由项处于最优路由状态]{style="font-family:宋体"}]{#struct_0_12376_x3448_767748385}

[[F - Flush to RIB]{lang="EN-US"}]{#struct_0_12376_x3448_1013485364}

[[此路由项已经被下刷到]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_12376_x3448_x1331010960}

[[Peer]{lang="EN-US"}]{#struct_0_12376_x3448_x1981295585}

[[与接口相连的邻居]{style="font-family:宋体"}]{#struct_0_12376_x3448_x566333514}

[[Destination]{lang="EN-US"}]{#struct_0_12376_x3448_x713377977}

[[目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12376_x3448_15746799}[地址]{style="font-family:宋体"}

[[via]{lang="EN-US"}]{#struct_0_12376_x3448_2049117141}

[[下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12376_x3448_x2024804375}[地址]{style="font-family:宋体"}

[[cost]{lang="EN-US"}]{#struct_0_12376_x3448_x308062323}

[[度量值]{style="font-family:宋体"}]{#struct_0_12376_x3448_x713443513}

[[tag]{lang="EN-US"}]{#struct_0_12376_x3448_x6851380}

[[路由标签]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1738096302}

[[secs]{lang="EN-US"}]{#struct_0_12376_x3448_558680460}

[[此路由项处于某种状态的时间]{style="font-family:宋体"}]{#struct_0_12376_x3448_1491351409}

[]{#_Toc60036177}[]{#_Toc53707121}[[ ]{lang="EN-US"}]{#_Toc52484717}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x713509049}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程路由信息的统计计数。]{style="font-family:宋体"}

[[\<Sysname\> display ripng 1 route statistics]{lang="EN-US"}]{#struct_0_12376_x3448_x713050297}

[ Peer                                            Optimal/Aging    Garbage]{lang="EN-US"}

[ FE80::20C:29FF:FED4:7171                        1/2              0]{lang="EN-US"}

[ Local                                           2/0              0]{lang="EN-US"}

[ total                                           3/2              0]{lang="EN-US"}

[]{#struct_0_12376_x3448_776589745}[]{#_Toc79394769}[[表1-8 ]{lang="EN-US"}[display ripng route statistics]{lang="EN-US"}]{#_Toc75056666}[命令显示信息]{style="font-family:
黑体"}[描述表]{style="font-family:黑体"}

[]{#table_struct_0_x334722639}[[字段]{style="font-family:黑体"}]{#struct_0_12376_x3448_1988127631}

[[描述]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2145004253}

[[Peer]{lang="EN-US"}]{#struct_0_12376_x3448_1291465330}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1590081019}[邻居]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Optimal]{lang="EN-US"}]{#struct_0_12376_x3448_64545810}

[[路由信息中处于最优路由状态的路由条数]{style="font-family:宋体"}]{#struct_0_12376_x3448_1883873231}

[[Aging]{lang="EN-US"}]{#struct_0_12376_x3448_x713115833}

[[路由信息中处于老化状态的路由条数]{style="font-family:宋体"}]{#struct_0_12376_x3448_x766890005}

[[Garbage]{lang="EN-US"}]{#struct_0_12376_x3448_x1215946297}

[[路由信息中处于]{style="font-family:宋体"}[Garbage-collection]{lang="EN-US"}]{#struct_0_12376_x3448_x1762197033}[状态的路由条数]{style="font-family:宋体"}

[[Local]{lang="EN-US"}]{#struct_0_12376_x3448_x713181369}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_34233724}[本地生成的直连路由条数的总和]{style="font-family:宋体"}

[[total]{lang="EN-US"}]{#struct_0_12376_x3448_x713246905}

[[从所有]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1541227728}[邻居学习到的路由条数的总和]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1009486692 .myid}
[]{#_Toc404788842}[]{#struct_0_12376_x3448_x1730998460}

**RIPng \-- RIPng配置命令 \-- enable ipsec-profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIPng命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12376_x3448_x1257852587}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_12376_x3448_1314247426}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[enable ipsec-profile]{lang="EN-US"}**]{#struct_0_12376_x3448_148666880}[命令用来在]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo enable ipsec-profile]{lang="EN-US"}**]{#struct_0_12376_x3448_642241112}[命令用来取消在]{style="font-family:
宋体"}[RIPng]{lang="EN-US"}[进程应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x712788153}

[**[enable ipsec-profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_12376_x3448_x1194297446}

[**[undo enable ipsec-profile]{lang="EN-US"}**]{#struct_0_12376_x3448_x90563431}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1434371087}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x2000117605}[没有应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x829526377}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1270015994}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x422698466}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x712853689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_395736407}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x259896899}

[*[profile-name]{lang="EN-US"}*]{#struct_0_12376_x3448_258750322}[：安全框架名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x13502858}

[[本命令应结合]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_12376_x3448_369395327}[安全框架使用，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的具体情况请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPsec]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x330043061}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1433708984}[配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架为]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x713312444}

[\[Sysname\] ripng 1]{lang="EN-US"}

[\[Sysname-ripng-1\] enable ipsec-profile profile001]{lang="EN-US"}
:::::

::: {#1247311243 .myid}
[]{#_Toc243714567}[]{#_Toc135644056}[]{#_Toc86723815}[]{#_Toc77992834}[]{#_Toc65740903}[]{#_Toc61239708}[]{#_Toc60036180}[]{#_Toc53707124}[]{#_Toc52484720}[]{#_Toc404788843}[]{#struct_0_12376_x3448_768076065}[]{#_Toc306780263}[]{#_Toc304993411}[]{#_Toc286221500}[]{#_Toc286221501}[]{#_Toc286221502}[]{#_Toc286221503}[]{#_Toc286221504}[]{#_Toc286221505}[]{#_Toc286221506}[]{#_Toc286221507}[]{#_Toc286221508}[]{#_Toc286221509}[]{#_Toc286221510}[]{#_Toc286221511}[]{#_Toc286221512}[]{#_Toc286221513}[]{#_Toc286221514}[]{#_Toc286221515}[]{#_Toc286221519}[]{#_Toc286221520}[]{#_Toc286221523}[]{#_Toc286221524}[]{#_Toc286221525}[]{#_Toc286221526}[]{#_Toc286221527}[]{#_Toc286221528}[]{#_Toc286221529}[]{#_Toc286221530}[]{#_Toc286221531}[]{#_Toc286221532}[]{#_Toc286221533}[]{#_Toc286221534}[]{#_Toc286221535}[]{#_Toc286221536}[]{#_Toc286221537}[]{#_Toc286221538}[]{#_Toc286221539}[]{#_Toc286221540}[]{#_Toc286221541}[]{#_Toc286221542}[]{#_Toc286221543}[]{#_Toc286221544}[]{#_Toc286221546}[]{#_Toc286221547}[]{#_Toc286221549}[]{#_Toc286221550}[]{#_Toc286221551}[]{#_Toc286221552}[]{#_Toc286221553}[]{#_Toc286221554}[]{#_Toc286221555}[]{#_Toc286221556}[]{#_Toc286221557}[]{#_Toc286221558}[]{#_Toc286221559}[]{#_Toc286221560}[]{#_Toc286221561}[]{#_Toc286221562}[]{#_Toc286221563}[]{#_Toc286221564}[]{#_Toc286221565}[]{#_Toc286221566}[]{#_Toc286221567}[]{#_Toc286221568}[]{#_Toc286221569}[]{#_Toc286221570}[]{#_Toc286221571}[]{#_Toc286221572}[]{#_Toc286221574}[]{#_Toc286221575}[]{#_Toc286221577}[]{#_Toc286221578}[]{#_Toc286221580}[]{#_Toc286221581}[]{#_Toc286221583}[]{#_Toc286221584}[]{#_Toc286221585}[]{#_Toc286221586}[]{#_Toc286221587}[]{#_Toc286221588}[]{#_Toc286221589}[]{#_Toc286221590}[]{#_Toc286221591}[]{#_Toc286221592}[]{#_Toc286221593}[]{#_Toc286221594}[]{#_Toc286221595}[]{#_Toc286221596}[]{#_Toc286221597}[]{#_Toc286221598}[]{#_Toc286221599}[]{#_Toc286221600}[]{#_Toc286221601}[]{#_Toc286221602}[]{#_Toc286221603}[]{#_Toc286221604}[]{#_Toc264986238}[]{#_Toc264986239}[]{#_Toc264986240}[]{#_Toc264986241}[]{#_Toc264986242}[]{#_Toc264986243}[]{#_Toc264986244}[]{#_Toc264986245}[]{#_Toc264986246}[]{#_Toc264986247}[]{#_Toc264986248}[]{#_Toc264986249}[]{#_Toc264986250}[]{#_Toc264986251}[]{#_Toc264986252}[]{#_Toc264986253}[]{#_Toc264986255}[]{#_Toc286221605}[]{#_Toc286221606}[]{#_Toc286221607}[]{#_Toc286221608}[]{#_Toc286221609}[]{#_Toc286221610}[]{#_Toc286221611}[]{#_Toc286221612}[]{#_Toc286221613}[]{#_Toc286221614}[]{#_Toc286221615}[]{#_Toc286221616}[]{#_Toc286221617}[]{#_Toc286221618}[]{#_Toc286221619}[]{#_Toc286221620}[]{#_Toc286221621}[]{#_Toc286221622}[]{#_Toc286221623}[]{#_Toc286221624}[]{#_Toc286221627}[]{#_Toc286221628}[]{#_Toc286221629}[]{#_Toc286221630}[]{#_Toc286221631}[]{#_Toc286221632}[]{#_Toc286221633}[]{#_Toc286221634}[]{#_Toc286221635}[]{#_Toc286221636}[]{#_Toc286221637}[]{#_Toc286221638}[]{#_Toc286221639}[]{#_Toc286221640}[]{#_Toc286221641}[]{#_Toc286221642}[]{#_Toc286221643}[]{#_Toc286221644}[]{#_Toc286221645}[]{#_Toc286221646}[]{#_Toc286221648}[]{#_Toc286221649}[]{#_Toc286221650}[]{#_Toc286221651}[]{#_Toc286221652}[]{#_Toc286221653}[]{#_Toc286221654}[]{#_Toc286221655}[]{#_Toc286221656}[]{#_Toc286221657}[]{#_Toc286221658}[]{#_Toc286221659}[]{#_Toc286221660}[]{#_Toc286221661}[]{#_Toc286221662}[]{#_Toc286221663}[]{#_Toc286221664}[]{#_Toc286221665}[]{#_Toc286221667}[]{#_Toc286221668}[]{#_Toc286221669}[]{#_Toc286221670}[]{#_Toc286221671}[]{#_Toc286221672}[]{#_Toc286221673}[]{#_Toc286221674}[]{#_Toc286221675}[]{#_Toc286221676}[]{#_Toc286221677}[]{#_Toc286221678}[]{#_Toc286221679}

**RIPng \-- RIPng配置命令 \-- filter-policy export**

------------------------------------------------------------------------

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_12376_x3448_443374881}[命令用来配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[输出路由过滤策略，只有通过过滤的路由才能通过更新报文发布出去。]{style="font-family:宋体"}

[**[undo filter-policy]{lang="EN-US"}**[ **export**]{lang="EN-US"}]{#struct_0_12376_x3448_74884436}[命令用来取消输出路由过滤策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x876547504}

[**[filter-policy ]{lang="EN-US"}**[{ *acl6-number* \| **prefix-list** *prefix-list-name* } **export** \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_12376_x3448_771377511}

[**[undo filter-policy]{lang="EN-US"}**[ **export** \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_12376_x3448_x1587918679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_355191309}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_880590253}[不对发布的路由信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713377980}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_15943406}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x481539853}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x950791021}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_2064875027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x112685748}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_12376_x3448_x1942212428}[：]{style="font-family:宋体"}[指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本或高级访问控制列表，]{style="font-family:宋体"}[用于对发布的路由信息进行过滤，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_12376_x3448_65753501}[：]{style="font-family:宋体"}[指定用于过滤发布路由信息的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_12376_x3448_x1524816798}[：]{style="font-family:宋体"}[被过滤路由信息的路由协议。目前可选择]{style="font-family:宋体"}[bgp4+]{lang="EN-US"}[、]{style="font-family:宋体"}[direct]{lang="EN-US"}[、]{style="font-family:宋体"}[isisv6]{lang="EN-US"}[、]{style="font-family:宋体"}[ospfv3]{lang="EN-US"}[、]{style="font-family:宋体"}[ripng]{lang="EN-US"}[、]{style="font-family:宋体"}[static]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_x713443516}[：]{style="font-family:宋体"}[被过滤路由信息的路由协议的进程号，取]{style="font-family:宋体"}[值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。仅当路由]{style="font-family:宋体"}[协议为]{style="font-family:宋体"}[ripng]{lang="EN-US"}[、]{style="font-family:宋体"}[ospfv3]{lang="EN-US"}[、]{style="font-family:宋体"}[isisv6]{lang="EN-US"}[时需要指定进程号]{style="font-family:宋体"}[，若未指定，缺省进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x6654772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_12376_x3448_1816818372}*[protocol]{lang="EN-US"}*[参数，则只对从指定路由协议引入的路由信息进行过滤；否则将对所有要发布的路由信息进行过滤。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当配置的是高级]{style="font-family:宋体"}]{#struct_0_12376_x3448_846047482}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]{lang="EN-US"}[来过滤指定目的地址和前缀的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x878297253}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x2085533473}[用地址前缀列表过滤发布的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[更新报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_1398938382}

[\[Sysname\] ipv6 prefix-list abc index 10 permit 100:1:: 32]{lang="EN-US"}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] filter-policy prefix-list abc export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1656206006}[用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对发布的路由进行过滤，只允许]{style="font-family:宋体"}[2001::1/128]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x713509052}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 100 deny ipv6]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] filter-policy 3000 export]{lang="EN-US"}
:::

::: {#632247711 .myid}
[]{#_Toc404788844}[]{#struct_0_12376_x3448_x1200225603}[]{#_Toc306780264}[]{#_Toc304993412}

**RIPng \-- RIPng配置命令 \-- filter-policy import**

------------------------------------------------------------------------

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_12376_x3448_1744777460}[命令用来对接收的路由信息进行过滤，符合过滤条件的路由才能被接收。]{style="font-family:宋体"}**[undo filter-policy]{lang="EN-US"}**[ **import**]{lang="EN-US"}[命令用来取消对接收的路由信息进行过滤。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1224606617}

[**[filter-policy]{lang="EN-US"}**[ { *acl6-number* \| **prefix-list** *prefix-list-name* } **import**]{lang="EN-US"}]{#struct_0_12376_x3448_1775205650}

[**[undo filter-policy]{lang="EN-US"}**[ **import**]{lang="EN-US"}]{#struct_0_12376_x3448_1336840990}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1744966682}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x43022572}[不对接收的路由信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713050300}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1561603656}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1822023198}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_2054514634}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1216133564}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x688210261}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_12376_x3448_x1697299391}[：用于过滤接收的路由信息的访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_12376_x3448_x2118111655}[：]{style="font-family:宋体"}[指定用于过滤接收路由信息的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{lang="EN-US" style="font-family:
黑体;color:#0096d6"}]{#struct_0_12376_x3448_x2061729938}

[[当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_12376_x3448_x713115836}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]{lang="EN-US"}[来过滤指定目的地址和前缀的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x766562325}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1657730468}[用地址前缀列表过滤收到的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[更新报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x1472341688}

[\[Sysname\] ipv6 prefix-list abc index 10 permit 100:1:: 32]{lang="EN-US"}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] filter-policy prefix-list abc import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1505577762}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由进行过滤，只允许]{style="font-family:宋体"}[2001::1/128]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x713181372}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 100 deny ipv6]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] filter-policy 3000 import]{lang="EN-US"}
:::

::::: {#63544256 .myid}
[]{#_Toc306780265}[]{#_Toc304993413}[]{#_Toc404788845}[]{#struct_0_12376_x3448_34823547}[]{#_Toc322355686}[]{#_Toc321837765}[]{#_Toc303839441}

**RIPng \-- RIPng配置命令 \-- graceful-restart**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIPng命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12376_x3448_1852717534}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_12376_x3448_614855798}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_12376_x3448_x1118904707}[命令用来使能]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_12376_x3448_x445095768}[命令用来关闭]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x883182953}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_12376_x3448_x1457693906}

[**[undo ]{lang="FR"}[graceful-restart]{lang="EN-US"}**]{#struct_0_12376_x3448_x1625557713}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713246908}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1541031120}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1879429863}

[[RIPng]{lang="FR"}]{#struct_0_12376_x3448_1032395534}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1538838074}

[[network-admin]{lang="FR"}]{#struct_0_12376_x3448_1736292593}

[[mdc-admin]{lang="FR"}]{#struct_0_12376_x3448_623443595}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_29937772}

[[RIPng GR]{lang="FR"}]{#struct_0_12376_x3448_30003308}[特性与]{style="font-family:宋体"}[RIPng NSR]{lang="FR"}[特性互斥]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}**[graceful-restart]{lang="FR"}**[和]{style="font-family:宋体"}**[non-stop-routing]{lang="FR"}**[命令互斥]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_922136592}

[[\# ]{lang="FR"}]{#struct_0_12376_x3448_636286012}[使能]{style="font-family:宋体"}[RIPng]{lang="FR"}[进程]{style="font-family:宋体"}[1]{lang="FR"}[的]{style="font-family:
宋体"}[GR]{lang="FR"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> syste]{lang="FR"}]{#struct_0_12376_x3448_x712788156}[m-view]{lang="FR"}

[\[Sysname\] ripng 1]{lang="FR"}

[\[Sysname-ripng-1\] graceful-restart]{lang="FR"}
:::::

::: {#16863910 .myid}
[]{#_Toc404788846}[]{#struct_0_12376_x3448_30068844}[]{#_Toc375236039}[]{#_Toc328746913}[]{#_Toc322686170}[]{#_Toc320863813}

**RIPng \-- RIPng配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

[**[graceful-restart interval]{lang="EN-US"}**]{#struct_0_12376_x3448_x1349786033}[命令用来配置]{style="font-family:
宋体"}[RIPng]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间。]{style="font-family:宋体"}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_12376_x3448_1930432018}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1931541964}

[**[graceful-restart interval ]{lang="EN-US"}***[interval-value[ ]{style="color:blue"}]{lang="EN-US"}*]{#struct_0_12376_x3448_x762863657}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_12376_x3448_30134380}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1764006402}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1536618643}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1087723582}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_29675628}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1801638681}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x924753262}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x796565686}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x92830754}

[*[interval-value]{lang="EN-US"}*]{#struct_0_12376_x3448_29741164}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[路由器平滑重启的时长，取值范围是]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[360]{lang="EN-US"}[，单位是秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_11526282}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_791525930}[配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[平滑重启间隔。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x1972888678}

[\[Sysname\] ripng 1]{lang="EN-US"}

[\[Sysname-ripng-1\] graceful-restart interval 200]{lang="EN-US"}
:::

::: {#29262825 .myid}
[]{#_Toc404788847}[]{#struct_0_12376_x3448_x1194625126}

**RIPng \-- RIPng配置命令 \-- import-route**

------------------------------------------------------------------------

[**[import-route]{lang="EN-US"}**]{#struct_0_12376_x3448_x1410421247}[命令用来从其它路由协议引入路由。]{style="font-family:宋体"}

[**[undo import-route]{lang="EN-US"}**]{#struct_0_12376_x3448_1047821034}[命令用来取消引入外部路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1092896918}

[**[import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \] \[ **allow-ibgp** \] \[ **allow-direct** \| **cost** *cost* \| **route-policy** *route-policy-name* \] \*]{lang="EN-US"}]{#struct_0_12376_x3448_197420963}

[**[undo import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \]]{lang="EN-US"}]{#struct_0_12376_x3448_x1966859309}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x712853692}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_396195160}[不引入其它路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2016132798}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x417132780}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1700522204}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1562327568}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1880196141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1734434957}

[*[protocol]{lang="EN-US"}*]{#struct_0_12376_x3448_x1152892377}[：]{style="font-family:宋体"}[指定要引入的路由协议，可以是]{style="font-family:宋体"}[bgp4+]{lang="EN-US"}[、]{style="font-family:宋体"}[direct]{lang="EN-US"}[、]{style="font-family:宋体"}[isisv6]{lang="EN-US"}[、]{style="font-family:宋体"}[ospfv3]{lang="EN-US"}[、]{style="font-family:宋体"}[ripng]{lang="EN-US"}[或]{style="font-family:宋体"}[static]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_x713312443}[：]{style="font-family:宋体"}[路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。只有当]{style="font-family:宋体"}[protocol]{lang="EN-US"}[是]{style="font-family:宋体"}[isisv6]{lang="EN-US"}[、]{style="font-family:宋体"}[ospfv3]{lang="EN-US"}[或]{style="font-family:宋体"}[ripng]{lang="EN-US"}[时该参数可选。]{style="font-family:宋体"}

[**[allow-ibgp]{lang="EN-US"}**]{#struct_0_12376_x3448_767617313}[：当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[为]{style="font-family:宋体"}[bgp4+]{lang="EN-US"}[时，]{style="font-family:宋体"}**[allow-ibgp]{lang="EN-US"}**[为可选关键字]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[allow-direct]{lang="EN-US"}**]{#struct_0_12376_x3448_1071222777}[：在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入协议路由时不会包含使能了该协议的接口网段路由。当]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[与]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}[参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[配置失效。例如，当配置]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数引入]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[直连时，在路由策略中不要配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[ **route-type**]{lang="EN-US"}[匹配条件，否则，]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数失效。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}***[ cost]{lang="EN-US"}*]{#struct_0_12376_x3448_x866640256}[：]{style="font-family:宋体"}[所要引入路由的度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。如果没有指定度量值，则使用缺省度量值]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**]{#struct_0_12376_x3448_281747849}*[ route-policy-name]{lang="EN-US"}*[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1869767175}

[**[import-route bgp4+]{lang="EN-US"}**]{#struct_0_12376_x3448_x438020647}[表示只引入]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由，]{style="font-family:宋体"}**[import-route bgp4+ allow-ibgp]{lang="EN-US"}**[表示也将]{style="font-family:
宋体"}[IBGP]{lang="EN-US"}[路由引入，容易引起路由环路，请慎用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_440590763}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x713377979}[引入]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[协议（进程号]{style="font-family:宋体"}[7]{lang="EN-US"}[）的路由信息，并将其度量值设置为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_15353583}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] import-route isisv6 7 cost 7]{lang="EN-US"}
:::

::: {#1012649285 .myid}
[]{#_Toc306780266}[]{#_Toc304993414}[]{#_Toc264986258}[]{#_Toc243714564}[]{#_Toc135644055}[]{#_Toc86723814}[]{#_Toc77992833}[]{#_Toc65740902}[]{#_Toc404788848}[]{#struct_0_12376_x3448_x221599175}[]{#_Toc313019160}

**RIPng \-- RIPng配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

[**[maximum load]{lang="EN-US"}**]{#struct_0_12376_x3448_540940975}**[-balancing]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[最大等价路由条数。]{style="font-family:宋体"}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_12376_x3448_1715481824}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1493864455}

[**[maximum load-balancing]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_12376_x3448_x1416091116}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_12376_x3448_x280919895}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713443515}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x6720308}[支持的等价路由的最大条数与]{style="font-family:宋体"}[系统支持最大等价路由的条数相同。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1765268546}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1935140087}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_314314772}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1299248176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1643203560}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1929655719}

[*[number]{lang="EN-US"}*]{#struct_0_12376_x3448_233092164}[：等价路由的最大条数]{style="font-family:宋体"}[，当]{style="font-family:宋体"}*[maximum]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，相当于不进行负载分担]{style="font-family:宋体"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713509051}

[[如果通过]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_12376_x3448_x1200291139}[命令配置系统支持最大等价路由的条数为]{style="font-family:宋体"}[m]{lang="EN-US"}[，则本命令的缺省值为]{style="font-family:宋体"}[m]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[m]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_12376_x3448_654890388}[命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2002428170}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1882080060}[配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[最大等价路由条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x1879515967}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] maximum load-balancing 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1596474178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_12376_x3448_x298767725}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{style="font-family:宋体"}
:::

::: {#-1554088180 .myid}
[]{#_Toc404788849}[]{#struct_0_12376_x3448_x373346760}[]{#_Toc375236042}[]{#_Toc328746914}[]{#_Toc322686171}[]{#_Toc320863814}

**RIPng \-- RIPng配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_12376_x3448_x373281224}[命令用来使能]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[协议]{style="font-family:宋体"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_12376_x3448_1777503552}[命令用来关闭]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[协]{style="font-family:宋体"}[议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_486582521}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_12376_x3448_1563264105}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_12376_x3448_x373215688}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_584015782}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1388112810}[协]{style="font-family:宋体"}[议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能处于]{style="font-family:宋体"}[关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x877097442}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x373150152}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1725693447}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x84990275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1985095802}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x373608904}

[[RIPng NSR]{lang="EN-US"}]{#struct_0_12376_x3448_681795049}[特性与]{style="font-family:宋体"}[RIPng GR]{lang="EN-US"}[特性互斥，即]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[和]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2073290814}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x585619387}[配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[使能]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x373543368}

[\[Sysname\] ripng 1]{lang="EN-US"}

[\[Sysname-ripng-1\] non-stop-routing]{lang="EN-US"}
:::

::: {#-1957377733 .myid}
[]{#_Toc404788850}[]{#struct_0_12376_x3448_626816765}[]{#_Toc375236043}[]{#_Toc328746915}[]{#_Toc322686172}[]{#_Toc216497586}

**RIPng \-- RIPng配置命令 \-- output-delay**

------------------------------------------------------------------------

[**[output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_634086950}[用来配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的发送速率。]{style="font-family:宋体"}

[**[undo output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_x1097318196}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1165234640}

[**[output-delay]{lang="EN-US"}***[ time ]{lang="EN-US"}***[count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_12376_x3448_x373477832}

[**[undo output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_x160937593}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1891848687}

[[发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x448351531}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x373412296}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1384508348}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x503590413}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_754250049}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x2105398845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x372822472}

[*[time]{lang="EN-US"}*]{#struct_0_12376_x3448_220458038}[：发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_12376_x3448_1783240580}[：一次发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的最大个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_839940011}

[[如果全局和接口都进行了配置，以接口的配置为准。]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1491111469}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x372756936}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x168051129}[配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_557225213}

[\[Sysname\] ripng 1]{lang="EN-US"}

[\[Sysname-ripng-1\] output-delay 60 count 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1106113159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ripng output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_x373346759}
:::

::: {#830408614 .myid}
[]{#_Toc404788851}[]{#struct_0_12376_x3448_x102655259}

**RIPng \-- RIPng配置命令 \-- preference**

------------------------------------------------------------------------

[**[preference]{lang="EN-US"}**]{#struct_0_12376_x3448_x713050299}[命令用来配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由的优先级。]{style="font-family:宋体"}

[**[undo preference]{lang="EN-US"}**]{#struct_0_12376_x3448_776458673}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_433714529}

[**[preference]{lang="EN-US"}**[ ]{lang="EN-US"}[{ *preference* \| **route-policy** *route-policy-name* } \*]{lang="EN-US"}]{#struct_0_12376_x3448_574666935}

[**[undo preference]{lang="EN-US"}**]{#struct_0_12376_x3448_550259983}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_760229054}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_849807909}[路由优先级的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1346918604}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_837347207}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713115835}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x766496789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1462361325}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x250689396}

[*[preference]{lang="EN-US"}*]{#struct_0_12376_x3448_1136840385}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由优先级的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}[取值越小，优先级越高。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy]{lang="EN-US"}*[-*name*]{lang="EN-US"}]{#struct_0_12376_x3448_x382131441}[：路由策略名称，]{style="font-family:宋体"}*[route-policy]{lang="EN-US"}*[-*name*]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。对满足特定条件的路由设置优先级。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_108783982}

[[通过指定]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1097120209}**[route-policy]{lang="EN-US"}**[参数，可应用路由策略对特定的路由设置优先级：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果在路由策略中已经设置了匹配路由的优先级，则匹配路由取路由策略设置的优先级，其它路由取]{style="font-family:宋体"}]{#struct_0_12376_x3448_922009343}**[preference]{lang="EN-US"}**[命令所设优先级。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果在路由策略中没有设置匹配路由的优先级，则所有路由都取]{style="font-family:宋体"}]{#struct_0_12376_x3448_x713181371}**[preference]{lang="EN-US"}**[命令所设优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_34758011}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_47427685}[配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由的优先级为]{style="font-family:宋体"}[120]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_665704531}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] preference 120]{lang="EN-US"}
:::

::: {#658009669 .myid}
[]{#_Toc404788852}[]{#struct_0_12376_x3448_x2122006397}[]{#_Toc313019162}

**RIPng \-- RIPng配置命令 \-- reset ripng process**

------------------------------------------------------------------------

[**[reset ripng process]{lang="EN-US"}**]{#struct_0_12376_x3448_x478388350}[命令用来重启指定]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1691001525}

[**[reset ripng ]{lang="EN-US"}**]{#struct_0_12376_x3448_568797184}*[process-id]{lang="EN-US"}*[ ]{lang="EN-US"}**[process]{lang="EN-US"}**

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1151804931}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x713246907}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1541096656}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1897116944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_628501558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1924816644}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_2123048117}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1977168840}

[[执行该命令后，系统提示用户确认是否重启]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1142876366}[RIPng]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x870966878}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x712788155}[重启进程号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[\<Sysname\> reset ripng 100 process]{lang="EN-US"}]{#struct_0_12376_x3448_x1194690662}

[Reset RIPng process? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#-1827024737 .myid}
[]{#_Toc404788853}[]{#struct_0_12376_x3448_1825369863}[]{#_Toc313019163}

**RIPng \-- RIPng配置命令 \-- reset ripng statistics**

------------------------------------------------------------------------

[**[reset ripng statistics]{lang="EN-US"}**]{#struct_0_12376_x3448_x1762767500}[命令用来清除]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x826068666}

[**[reset ripng]{lang="EN-US"}**]{#struct_0_12376_x3448_1963238730}[ *process-id* **statistics**]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1933815603}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_1438567692}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_852866736}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x712853691}

[[network-operator]{lang="EN-US"}]{#struct_0_12376_x3448_396260696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x833091788}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12376_x3448_1656319244}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1423616652}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_221905193}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x746617844}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1055246988}[清除进程号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ripng 100 statistics]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_12376_x3448_x1556125271}
:::

::: {#1256057567 .myid}
[]{#_Toc404788854}[]{#struct_0_12376_x3448_x713312446}

**RIPng \-- RIPng配置命令 \-- ripng**

------------------------------------------------------------------------

[**[ripng]{lang="EN-US"}**]{#struct_0_12376_x3448_767944993}[命令用来创建]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程，并进入]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo ripng]{lang="EN-US"}**]{#struct_0_12376_x3448_2074804520}[命令用来关闭]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1581054444}

[**[ripng]{lang="EN-US"}**[ \[ *process-id* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12376_x3448_x433960479}

[**[undo]{lang="EN-US"}**[ **ripng** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_12376_x3448_2010899187}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_705112033}

[[没有]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x985920657}[进程在运行。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_470304076}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x713377982}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_16074478}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1752789498}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_998069491}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1152673603}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_261932798}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_12376_x3448_141520035}*[ vpn-instance-name]{lang="EN-US"}*[：指定]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x166853270}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先创建]{style="font-family:宋体"}]{#struct_0_12376_x3448_x834830442}[RIPng]{lang="EN-US"}[进程，才能配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[的各种全局性参数，而配置与接口相关的参数时，可以不受这个限制。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[停止运行]{style="font-family:宋体"}]{#struct_0_12376_x3448_x713443518}[RIPng]{lang="EN-US"}[进程后，原来配置的接口参数也同时失效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x6523700}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_46666699}[创建]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x2117135563}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\]]{lang="EN-US"}
:::

::: {#383118309 .myid}
[]{#_Toc243714569}[]{#_Toc135644058}[]{#_Toc86723817}[]{#_Toc77992836}[]{#_Toc65740905}[]{#_Toc61239710}[]{#_Toc60036182}[]{#_Toc53707126}[]{#_Toc52484722}[]{#_Toc404788855}[]{#struct_0_12376_x3448_x81242036}[]{#_Toc313019167}[]{#_Toc286221681}[]{#_Toc286221682}[]{#_Toc286221683}[]{#_Toc286221685}[]{#_Toc286221688}[]{#_Toc286221689}[]{#_Toc286221690}[]{#_Toc286221691}[]{#_Toc286221692}[]{#_Toc286221693}[]{#_Toc286221694}[]{#_Toc286221695}[]{#_Toc286221696}[]{#_Toc286221697}[]{#_Toc286221698}[]{#_Toc286221699}[]{#_Toc286221700}[]{#_Toc286221701}[]{#_Toc286221702}[]{#_Toc286221703}[]{#_Toc286221704}[]{#_Toc286221705}[]{#_Toc286221706}[]{#_Toc286221707}[]{#_Toc286221708}[]{#_Toc286221709}[]{#_Toc286221710}[]{#_Toc286221711}[]{#_Toc286221712}[]{#_Toc286221714}[]{#_Toc286221715}[]{#_Toc286221716}[]{#_Toc286221718}[]{#_Toc326738822}[]{#_Toc326738823}[]{#_Toc326738824}[]{#_Toc326738825}[]{#_Toc326738826}[]{#_Toc326738827}[]{#_Toc326738828}[]{#_Toc326738829}[]{#_Toc326738830}[]{#_Toc326738831}[]{#_Toc326738832}[]{#_Toc326738833}[]{#_Toc326738834}[]{#_Toc326738835}[]{#_Toc326738836}[]{#_Toc326738837}[]{#_Toc326738838}[]{#_Toc326738839}[]{#_Toc326738840}[]{#_Toc292815538}[]{#_Toc326738841}[]{#_Toc326738842}[]{#_Toc326738843}[]{#_Toc326738844}[]{#_Toc326738845}[]{#_Toc326738846}[]{#_Toc326738847}[]{#_Toc326738848}[]{#_Toc326738849}[]{#_Toc326738850}

**RIPng \-- RIPng配置命令 \-- ripng default-route**

------------------------------------------------------------------------

[**[ripng default-route]{lang="EN-US"}**]{#struct_0_12376_x3448_x53423453}[命令用来以指定度量值向]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[邻居发布一条缺省路由。]{style="font-family:宋体"}

[**[undo ripng default-route]{lang="EN-US"}**]{#struct_0_12376_x3448_1293225859}[命令用来禁止发布]{style="font-family:
宋体"}[RIPng]{lang="EN-US"}[缺省路由和转发]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[缺省路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2002078013}

[**[ripng default-route]{lang="EN-US"}**]{#struct_0_12376_x3448_x713509054}[ { **only** \| **originate** } \[ **cost** *cost \|* ]{lang="EN-US"}**[route-policy ]{lang="EN-US"}***[route-policy-name ]{lang="EN-US"}*[\] \*]{lang="EN-US"}

[**[undo ripng default-route]{lang="EN-US"}**]{#struct_0_12376_x3448_x1200618819}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_745450203}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x722001483}[进程不发布缺省路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_766407942}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_1864239622}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1899486257}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1114996747}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1983076353}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713050302}

[**[only]{lang="EN-US"}**]{#struct_0_12376_x3448_x1561734728}[：只发布]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[缺省路由（]{style="font-family:宋体"}[::/0]{lang="EN-US"}[），抑制其它路由的发布。]{style="font-family:宋体"}

[**[originate]{lang="EN-US"}**]{#struct_0_12376_x3448_x208428380}[：发布]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[缺省路由（]{style="font-family:宋体"}[::/0]{lang="EN-US"}[），但不影响其它路由的发布。]{style="font-family:宋体"}

[*[cost]{lang="EN-US"}*]{#struct_0_12376_x3448_x1264871870}[：发布缺省路由的度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_12376_x3448_x373346762}[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，]{style="font-family:宋体"}[区分大小写。只有当前路由器的路由表中有路由匹配]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[指定的路由策略时，才发送缺省路由。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_906576049}

[[通过该命令的设置，生成的]{style="font-family:宋体"}]{#struct_0_12376_x3448_675705212}[RIPng]{lang="EN-US"}[缺省路由将强制通过指定接口的路由更新报文发布出去。该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[缺省路由的发布不考虑其是否已经存在于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[配置发布缺省路由的]{style="font-family:宋体;border:none windowtext 1.0pt;padding:0cm"}]{#struct_0_12376_x3448_1922768467}[RIPng]{lang="EN-US" style="border:none windowtext 1.0pt;padding:0cm"}[接口不接收来自]{style="font-family:宋体;border:none windowtext 1.0pt;padding:0cm"}[RIPng]{lang="EN-US" style="border:none windowtext 1.0pt;padding:0cm"}[邻居的缺省路由。]{style="font-family:宋体;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x686630819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_856376620}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x713115838}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[只将缺省路由以更新报文的形式从接口发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x766169109}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng default-route only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x830476157}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[将缺省路由同其它路由一起以更新报文的形式从接口发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_2142632288}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng default-route originate]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1835119015}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1243848838}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[只将缺省路由以更新报文的形式从接口发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x1382291545}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng default-route only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x713181374}[在接口]{style="font-family:宋体"}[Vlan-interface101]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[将缺省路由同其它路由一起以更新报文的形式从接口发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_34430331}

[\[Sysname\] interface vlan-interface 101]{lang="EN-US"}

[\[Sysname-Vlan-interface101\] ripng default-route originate]{lang="EN-US"}
:::

::: {#1594112757 .myid}
[]{#_Toc404788856}[]{#struct_0_12376_x3448_x1242054852}

**RIPng \-- RIPng配置命令 \-- ripng enable**

------------------------------------------------------------------------

[**[ripng]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_12376_x3448_x1008229212}[命令用来在接口上使能]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由协议。]{style="font-family:宋体"}

[**[undo ripng enable]{lang="EN-US"}**]{#struct_0_12376_x3448_x319838739}[命令用来在接口上关闭]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_216430586}

[**[ripng]{lang="EN-US"}**[ *process-id* **enable**]{lang="EN-US"}]{#struct_0_12376_x3448_x1839624787}

[**[undo ripng]{lang="EN-US"}**[ ]{lang="EN-US"}**[enable]{lang="EN-US"}**]{#struct_0_12376_x3448_808813120}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1456473525}

[[接口禁用]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x713246910}[路由协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1541555407}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_2014602523}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1060565074}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_151975084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x313588545}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_223049562}

[*[process-id]{lang="EN-US"}*]{#struct_0_12376_x3448_x1591360999}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1280683425}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_x712788158}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1195018342}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[RIPng 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_1887743753}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng 100 enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_x2129722757}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1588536061}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[RIPng 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x219324414}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng 100 enable]{lang="EN-US"}
:::

::::: {#470990893 .myid}
[]{#_Toc332815975}[]{#_Toc404788857}[]{#struct_0_12376_x3448_71738537}

**RIPng \-- RIPng配置命令 \-- ripng ipsec-profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIPng命令.files/image001.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_12376_x3448_1326749991}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_12376_x3448_x712853694}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[ripng ipsec-profile]{lang="EN-US"}**]{#struct_0_12376_x3448_396064088}[命令用来在]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[接口上应用安全框架。]{style="font-family:宋体"}

[**[undo ripng ipsec-profile]{lang="EN-US"}**]{#struct_0_12376_x3448_1653361540}[命令用来取消]{style="font-family:
宋体"}[RIPng]{lang="EN-US"}[接口上应用的安全框架。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_822522012}

[**[ripng ipsec-profile]{lang="EN-US"}[ ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_12376_x3448_x1988407891}

[**[undo ripng ipsec-profile]{lang="EN-US"}**]{#struct_0_12376_x3448_462396157}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_960533037}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x1607056875}[接口]{style="font-family:宋体"}[没有应用安全框架。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713312445}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_768010529}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1954587866}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1875833899}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1366251359}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_363676426}

[*[profile-name]{lang="EN-US"}*]{#struct_0_12376_x3448_x1082115499}[：安全框架名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_514844187}

[[本命令应结合]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_12376_x3448_33007606}[安全框架使用，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的具体情况请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPsec]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2105469970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_x713377981}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_15877870}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[应用]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架为]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x1520122491}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng ipsec-profile profile001]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_1229793367}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1163816618}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[应用]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架为]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_1401085707}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng ipsec-profile profile001]{lang="EN-US"}
:::::

::: {#-2030525276 .myid}
[]{#_Toc243714573}[]{#_Toc135644060}[]{#_Toc86723819}[]{#_Toc77992838}[]{#_Toc65740907}[]{#_Toc61239712}[]{#_Toc60036184}[]{#_Toc53707128}[]{#_Toc52484724}[]{#_Toc404788858}[]{#struct_0_12376_x3448_x2032440591}[]{#_Toc313019168}[]{#_Toc286221720}[]{#_Toc286221721}[]{#_Toc286221722}[]{#_Toc286221723}[]{#_Toc286221724}[]{#_Toc286221725}[]{#_Toc286221726}[]{#_Toc286221727}[]{#_Toc286221728}[]{#_Toc286221729}[]{#_Toc286221730}[]{#_Toc286221731}[]{#_Toc286221732}[]{#_Toc286221733}[]{#_Toc286221734}[]{#_Toc286221735}[]{#_Toc286221736}[]{#_Toc286221740}[]{#_Toc286221741}[]{#_Toc286221742}[]{#_Toc286221746}[]{#_Toc286221747}[]{#_Toc286221748}[]{#_Toc286221749}[]{#_Toc286221750}[]{#_Toc286221751}[]{#_Toc286221752}[]{#_Toc286221753}[]{#_Toc286221754}[]{#_Toc286221755}[]{#_Toc286221756}[]{#_Toc286221757}[]{#_Toc286221758}[]{#_Toc286221759}[]{#_Toc286221760}[]{#_Toc286221761}[]{#_Toc286221762}[]{#_Toc286221763}[]{#_Toc286221765}[]{#_Toc286221766}[]{#_Toc286221767}[]{#_Toc286221769}[]{#_Toc286221771}[]{#_Toc286221772}[]{#_Toc286221773}[]{#_Toc286221774}[]{#_Toc286221775}[]{#_Toc286221776}[]{#_Toc286221777}[]{#_Toc286221778}[]{#_Toc286221779}[]{#_Toc286221780}[]{#_Toc286221781}[]{#_Toc286221782}[]{#_Toc286221783}[]{#_Toc286221784}[]{#_Toc286221785}[]{#_Toc286221786}[]{#_Toc286221787}[]{#_Toc286221788}[]{#_Toc286221790}[]{#_Toc286221791}[]{#_Toc286221792}[]{#_Toc286221794}

**RIPng \-- RIPng配置命令 \-- ripng metricin**

------------------------------------------------------------------------

[**[ripng metricin]{lang="EN-US"}**]{#struct_0_12376_x3448_x713443517}[命令用来配置接口接收]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由时的附加度量值。]{style="font-family:宋体"}

[**[undo ripng metricin]{lang="EN-US"}**]{#struct_0_12376_x3448_x6589236}[命令用来恢复缺省情况]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_436254208}

[**[ripng]{lang="EN-US"}**]{#struct_0_12376_x3448_x308860902}[ **metricin** *value*]{lang="EN-US"}

[**[undo ripng]{lang="EN-US"}**]{#struct_0_12376_x3448_80671206}[ **metricin**]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1354677033}

[[接口接收]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x2125871949}[路由时的附加度量值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_199034384}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1828128005}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x713509053}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1200160067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x428130658}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x864681774}

[*[value]{lang="EN-US"}*]{#struct_0_12376_x3448_811046434}[：接收附加度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc157826816}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_528216242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_198868247}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1788841459}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在接收]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由时的附加度量值为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x713050301}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng metricin 12]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1561669192}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_363065863}[指定接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[在接收]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由时添加的附加度量值为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x735137355}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng metricin 12]{lang="EN-US"}
:::

::: {#1945513437 .myid}
[]{#_Toc404788859}[]{#struct_0_12376_x3448_x405765063}[]{#_Toc313019169}

**RIPng \-- RIPng配置命令 \-- ripng metricout**

------------------------------------------------------------------------

[**[ripng metricout]{lang="EN-US"}**]{#struct_0_12376_x3448_1252538506}[命令用来配置接口发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由时的附加度量值。]{style="font-family:宋体"}

[**[undo ripng metricout]{lang="EN-US"}**]{#struct_0_12376_x3448_x2043688634}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2086341540}

[**[ripng metricout]{lang="EN-US"}**]{#struct_0_12376_x3448_45735653}[ *value*]{lang="EN-US"}

[**[undo ]{lang="EN-US"}**]{#struct_0_12376_x3448_x713115837}**[ripng metricout]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x766627861}

[[接口发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x838381116}[路由时的附加度量值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2000252312}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_237514226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1865739947}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_78972212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1401475981}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1141926517}

[*[value]{lang="EN-US"}*]{#struct_0_12376_x3448_x713181373}[：发送附加度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_34889083}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_304202388}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x813054271}[设置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由时添加的附加度量值为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x48192478}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng metricout 12]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_2104432579}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1718234806}[设置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由时添加的附加度量值为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x713246909}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng metricout 12]{lang="EN-US"}
:::

::: {#1185832256 .myid}
[]{#_Toc404788860}[]{#struct_0_12376_x3448_1192606113}[]{#_Toc375236053}[]{#_Toc328746918}

**RIPng \-- RIPng配置命令 \-- ripng output-delay**

------------------------------------------------------------------------

[**[ripng output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_1192671649}[命令用来配置接口下]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的发送速率。]{style="font-family:宋体"}

[**[undo ripng output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_249291724}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_2110308218}

[**[ripng output-delay]{lang="EN-US"}***[ time]{lang="EN-US"}***[ count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_12376_x3448_1193261473}

[**[undo ripng output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_x2108562347}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1663952870}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_1193327009}[报文的发包速率由进程全局的配置决定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1702441621}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x478928561}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2054136314}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1192737186}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x153563937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1862243480}

[*[time]{lang="EN-US"}*]{#struct_0_12376_x3448_x1803701801}[：接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_12376_x3448_1192802722}[：接口一次发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的最大个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x130847119}

[[如果全局和接口都进行了配置，以接口的配置为准。]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1294695099}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1901175279}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_1192868258}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x902974768}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[6]{lang="EN-US"}[个]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_1192933794}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng output-delay 30 count 6]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_12376_x3448_1433598398}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1141065383}[在]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[配置发送]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[6]{lang="EN-US"}[个]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_1192475042}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng output-delay 30 count 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1338329610}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[output-delay]{lang="EN-US"}**]{#struct_0_12376_x3448_243123804}
:::

::: {#-1619005863 .myid}
[]{#_Toc404788861}[]{#struct_0_12376_x3448_x1540965584}

**RIPng \-- RIPng配置命令 \-- ripng poison-reverse**

------------------------------------------------------------------------

[**[ripng poison-reverse]{lang="EN-US"}**]{#struct_0_12376_x3448_863879523}[命令用来使能毒性逆转功能。]{style="font-family:宋体"}

[**[undo ripng poison-reverse]{lang="EN-US"}**]{#struct_0_12376_x3448_289269656}[命令用来关闭毒性逆转功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1754581594}

[**[ripng poison-reverse]{lang="EN-US"}**]{#struct_0_12376_x3448_x232311382}

[**[undo ripng poison-reverse]{lang="EN-US"}**]{#struct_0_12376_x3448_591162783}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1259771521}

[[毒性逆转功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1692611472}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_544858624}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x712788157}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1194559590}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_279373282}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1024746200}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1845999031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_263205658}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_734601067}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置对]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[更新报文进行毒性逆转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_482421329}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng poison-reverse]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_x712853693}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_396129624}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置对]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[更新报文进行毒性逆转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x728693082}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng poison-reverse]{lang="EN-US"}
:::

::: {#913976058 .myid}
[]{#_Toc404788862}[]{#struct_0_12376_x3448_x456827022}[]{#_Toc243714574}[]{#_Toc135644061}[]{#_Toc86723820}[]{#_Toc77992839}[]{#_Toc65740908}[]{#_Toc61239713}[]{#_Toc60036185}[]{#_Toc53707129}[]{#_Toc52484725}[]{#_Toc138824575}[]{#_Toc138824576}[]{#_Toc138824577}[]{#_Toc138824578}[]{#_Toc138824579}

**RIPng \-- RIPng配置命令 \-- ripng split-horizon**

------------------------------------------------------------------------

[**[ripng]{lang="EN-US"}**[ **split-horizon**]{lang="EN-US"}]{#struct_0_12376_x3448_x1214790958}[命令用来使能水平分割功能。]{style="font-family:宋体"}

[**[undo ripng split-horizon]{lang="EN-US"}**]{#struct_0_12376_x3448_x505664165}[命令用来关闭水平分割。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_278578193}

[**[ripng split-horizon]{lang="EN-US"}**]{#struct_0_12376_x3448_1565384559}

[**[undo ripng split-horizon]{lang="EN-US"}**]{#struct_0_12376_x3448_159458909}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_852771499}

[[水平分割功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_12376_x3448_1419082482}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_707271655}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_945739355}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1222580888}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1933985695}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1454099702}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_773084494}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下，为了防止路由环路的出现，水平分割都是必要的，因此，建议不要关闭水平分割。]{style="font-family:宋体"}]{#struct_0_12376_x3448_x1689900492}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只是在某些特殊情况下，为保证协议的正确执行，需要关闭水平分割。在关闭水平分割时一定要确认是否必要。]{style="font-family:宋体"}]{#struct_0_12376_x3448_852705963}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时使能了水平分割和毒性逆转，则只有毒性逆转功能生效。]{style="font-family:宋体"}]{#struct_0_12376_x3448_x2089195812}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在帧中继和]{style="font-family:宋体"}]{#struct_0_12376_x3448_x495377315}[X.25]{lang="EN-US"}[等]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[（]{style="font-family:宋体"}[Non-Broadcast Multi-Access]{lang="EN-US"}[，非广播多路访问）网络中，当主接口和点到多点子接口配置了多条虚电路时，为了保证路由信息的正确传播，需要关闭水平分割功能。关于帧中继和]{style="font-family:宋体"}[X.25]{lang="EN-US"}[的详细信息，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入配置指导"中的"帧中继"和"]{style="font-family:宋体"}[LAPB]{lang="EN-US"}[和]{style="font-family:宋体"}[X.25]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_827038304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_x1817721968}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x1859884903}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置水平分割。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x838738479}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng split-horizon]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_1967228813}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_852640427}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置水平分割。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_1828878997}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng split-horizon]{lang="EN-US"}
:::

::: {#627641752 .myid}
[]{#_Toc404788863}[]{#struct_0_12376_x3448_993515447}[]{#_Toc243714575}[]{#_Toc135644062}[]{#_Toc86723821}[]{#_Toc77992840}[]{#_Toc65740909}[]{#_Toc61239714}[]{#_Toc60036186}[]{#_Toc53707130}[]{#_Toc52484726}[]{#_Toc138824581}[]{#_Toc138824582}[]{#_Toc138824583}[]{#_Toc138824584}[]{#_Toc138824585}

**RIPng \-- RIPng配置命令 \-- ripng summary-address**

------------------------------------------------------------------------

[**[ripng summary-address]{lang="EN-US"}**]{#struct_0_12376_x3448_512843931}[命令用来配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[在接口发布聚合的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，并指定被聚合的路由的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}

[**[undo ripng summary]{lang="EN-US"}[-address]{lang="EN-US"}**]{#struct_0_12376_x3448_1109343442}[命令用来禁止]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由器发布聚合的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2072137874}

[**[ripng summary-address ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[ ]{lang="EN-US"}*[prefix-length]{lang="EN-US"}*]{#struct_0_12376_x3448_563633885}

[**[undo ripng summary-address]{lang="EN-US"}**[ *ipv6-address prefix-length*]{lang="EN-US"}]{#struct_0_12376_x3448_x318461684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2063901174}

[[没有配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_852574891}[在接口发布聚合的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_785248830}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12376_x3448_x240210049}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1255337816}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_839797172}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1667957052}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1829168112}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12376_x3448_x140060518}[：]{style="font-family:宋体"}[聚合路由的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_12376_x3448_249237609}[：]{style="font-family:宋体"}[聚合路由的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。它指定地址中有多少连续的位组成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网络前缀，即]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址中的网络地址部分。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_853033643}

[[如果一条路由的前缀和前缀长度与定义的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12376_x3448_x1947515443}[前缀匹配，则这个自定义的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀将取代原来的路由被发布出去。这样，多条路由将由一条路由所代替，而且，这条路由的度量值是原多条路由中最低的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x2101056555}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_x1701231830}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_99025280}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[2001:200::3EFF:FE11:6770]{lang="EN-US"}[，前缀长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[位。通过]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[聚合为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀]{style="font-family:宋体"}[2001:200::/35]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x314918422}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2001:200::3EFF:FE11:6770/64]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ripng summary-address 2001:200:: 35]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12376_x3448_2055960536}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x73656508}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[2001:200::3EFF:FE11:6770]{lang="EN-US"}[，其前缀长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[位。通过]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[聚合为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀]{style="font-family:宋体"}[2001:200::/35]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_852968107}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2001:200::3EFF:FE11:6770/64]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ripng summary-address 2001:200:: 35]{lang="EN-US"}
:::

::: {#-1147623796 .myid}
[]{#_Toc404788864}[]{#struct_0_12376_x3448_x723089056}[]{#_Toc375236057}[]{#_Toc328746919}[]{#_Toc322686176}

**RIPng \-- RIPng配置命令 \-- timer triggered**

------------------------------------------------------------------------

[**[timer triggered]{lang="EN-US"}**]{#struct_0_12376_x3448_x1606673949}[命令用来配置]{style="font-family:宋体"}[触发更新]{style="font-family:宋体"}[的时间间隔。]{style="font-family:宋体"}

[**[undo timer triggered]{lang="EN-US"}**]{#struct_0_12376_x3448_x723154592}[命令]{style="font-family:宋体"}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x31642017}

[**[timer triggered ]{lang="EN-US"}***[maximum-interval]{lang="EN-US"}*[ \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_12376_x3448_x754462046}

[**[undo timer triggered]{lang="EN-US"}**]{#struct_0_12376_x3448_x723482272}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_383904404}

[[发送触发更新的]{style="font-family:宋体"}]{#struct_0_12376_x3448_825965097}[最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，增量惩罚间隔为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1417625183}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x723547808}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x385381219}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_1775352101}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x723351200}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1919645105}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_12376_x3448_480928436}[[：触发更新的最大间隔时间。取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}]{.varname}[[～]{style="font-family:宋体"}[5]{lang="EN-US"}]{.varname}[[，单位是秒。]{style="font-family:宋体"}]{.varname}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_12376_x3448_x1769807461}[[：触发更新的最小间隔时间。取值范围是]{style="font-family:宋体"}[10]{lang="EN-US"}]{.varname}[[～]{style="font-family:宋体"}[5000]{lang="EN-US"}]{.varname}[[，单位是毫秒。]{style="font-family:宋体"}]{.varname}

[[*[incremental-interval]{lang="EN-US"}*]{.varname}]{#struct_0_12376_x3448_x723416736}[[：触发更新间隔的增加时间。取值范围是]{style="font-family:宋体"}[100]{lang="EN-US"}]{.varname}[[～]{style="font-family:宋体"}[1000]{lang="EN-US"}]{.varname}[[，单位是毫秒。]{style="font-family:宋体"}]{.varname}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_755636260}

[[本命令在网络变化不频繁的情况下将触发更新的时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_12376_x3448_495985139}[，而在网络变化频繁的情况下可以进行相应惩罚，将时间间隔按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_12376_x3448_x722695840}[和]{style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1981850572}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_x29264273}[配置发送触发更新的最大时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x722761376}

[\[Sysname\] ripng 100]{lang="EN-US"}

[\[Sysname-ripng-100\] timer triggered 2 100 100]{lang="EN-US"}
:::

::: {#-1110649075 .myid}
[]{#_Toc404788865}[]{#struct_0_12376_x3448_x724123174}[]{#_Toc243714576}[]{#_Toc135644063}[]{#_Toc86723822}[]{#_Toc77992841}[]{#_Toc65740910}[]{#_Toc61239715}[]{#_Toc60036187}[]{#_Toc53707131}[]{#_Toc52484727}

**RIPng \-- RIPng配置命令 \-- timers**

------------------------------------------------------------------------

[**[timers]{lang="EN-US"}**]{#struct_0_12376_x3448_1001086626}[命令用来配置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[定时器的值。]{style="font-family:宋体"}

[**[undo timers]{lang="EN-US"}**]{#struct_0_12376_x3448_1001852194}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1021655475}

[**[timers ]{lang="EN-US"}**[{ **garbage-collect** *garbage-collect-value* \| **suppress** *suppress-value* \| **timeout** *timeout-value* \| **update** *update-value* } \*]{lang="EN-US"}]{#struct_0_12376_x3448_x415509050}

[**[undo timers ]{lang="EN-US"}**[{ **garbage-collect** \| **suppress** \| **timeout** \| **update** } \*]{lang="EN-US"}]{#struct_0_12376_x3448_x580058432}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12376_x3448_395026224}

[[Garbage-collect]{lang="EN-US"}]{#struct_0_12376_x3448_852902571}[定时器的值为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Update]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1454116970}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x905289892}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x1662252502}

[[network-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1768561882}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12376_x3448_x1189328573}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12376_x3448_1803285867}

[*[garbage-collect-value]{lang="EN-US"}*]{#struct_0_12376_x3448_249326389}[：]{style="font-family:宋体"}[Garbage-collect]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[suppress-value]{lang="EN-US"}*]{#struct_0_12376_x3448_x1340805598}[：]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[timeout-value]{lang="EN-US"}*]{#struct_0_12376_x3448_852837035}[：]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[update-value]{lang="EN-US"}*]{#struct_0_12376_x3448_2042383822}[：]{style="font-family:宋体"}[Update]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x823016935}

[[RIPng]{lang="EN-US"}]{#struct_0_12376_x3448_x10217665}[受四个定时器的控制，分别是]{style="font-family:宋体"}[Update]{lang="EN-US"}[、]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[、]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[和]{style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Update]{lang="EN-US"}]{#struct_0_12376_x3448_283367954}[定时器，定义了发送更新报文的时间间隔。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Timeout]{lang="EN-US"}]{#struct_0_12376_x3448_x1930872547}[定时器，定义了路由老化时间。如果在老化时间内没有收到关于某条路由的更新报文，则该条路由在路由表中的度量值将会被设置为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Suppress]{lang="EN-US"}]{#struct_0_12376_x3448_x1948527125}[定时器，定义了]{style="font-family:
宋体"}[RIPng]{lang="EN-US"}[路由处于抑制状态的时间段长度。当一条路由的度量值变为]{style="font-family:宋体"}[16]{lang="EN-US"}[时，该路由将进入被抑制状态。在被抑制状态，只有来自同一邻居，且度量值小于]{style="font-family:宋体"}[16]{lang="EN-US"}[的路由更新才会被路由器接收，取代不可达路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Garbage-Collect]{lang="EN-US"}]{#struct_0_12376_x3448_x1167476590}[定时器，定义了一条路由从度量值变为]{style="font-family:宋体"}[16]{lang="EN-US"}[开始，直到它从路由表里被删除所经过的时间。]{style="font-family:宋体"}[在]{lang="EN-US" style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[时间内，]{lang="EN-US" style="font-family:宋体"}[RIPng]{lang="EN-US"}[以]{lang="EN-US" style="font-family:宋体"}[16]{lang="EN-US"}[作为度量值向外发送这条路由的更新，如果]{lang="EN-US" style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[超时，该路由仍没有得到更新，则该路由将从路由表中被彻底删除。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12376_x3448_771705508}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下，无需改变各定时器的缺省值，该命令须谨慎使用。]{style="font-family:宋体"}]{#struct_0_12376_x3448_1290619255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[各个定时器的值在网络中所有的路由器上必须保持一致。]{style="font-family:宋体"}]{#struct_0_12376_x3448_853295787}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12376_x3448_x873999872}

[[\# ]{lang="EN-US"}]{#struct_0_12376_x3448_1163061612}[分别设置]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[各定时器的值：其中，]{style="font-family:宋体"}[Update]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒、]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒、]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒、]{style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12376_x3448_x1738356634}

[\[Sysname\] ripng 1]{lang="EN-US"}

[\[Sysname-ripng-1\] timers update 5 timeout 15 suppress 15 garbage-collect 30]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
