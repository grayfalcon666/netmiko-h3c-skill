::: {#27196274 .myid}
[]{#_Toc404784378}[]{#struct_0_13089_x3611_1555611090}[]{#_Toc212028162}

**环路检测 \-- 环路检测配置命令 \-- display loopback-detection**

------------------------------------------------------------------------

[**[display loopback-detection]{lang="EN-US"}**]{#struct_0_13089_x3611_x1717063620}[命令用来显示[]{#_Hlt25985280}环路检测的配置和运行情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_915914099}

[**[display loopback-detection]{lang="EN-US"}**]{#struct_0_13089_x3611_x2142664953}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x965077942}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13089_x3611_x1733209959}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1450746555}

[[network-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x1997182701}

[[network-operator]{lang="EN-US"}]{#struct_0_13089_x3611_758602427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13089_x3611_731000922}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13089_x3611_1942821850}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13089_x3611_647214956}

[[\# ]{lang="EN-US"}]{#struct_0_13089_x3611_x1611792976}[显示环路检测的配置和运行情况。]{style="font-family:宋体"}

[]{#struct_0_13089_x3611_x2142730489}[[\<Sysname\> display loopback-detection]{lang="EN-US"}]{#_Hlt25988738}

[Loopback detection is enabled.]{lang="EN-US"}

[Loopback detection interval is 30 second(s).]{lang="EN-US"}

[Loopback is detected on following interfaces:]{lang="EN-US"}

[ Interface                Action mode]{lang="EN-US"}

[ GigabitEthernet1/0/1     Block]{lang="EN-US"}

[ GigabitEthernet1/0/2     Shutdown]{lang="EN-US"}

[ GigabitEthernet1/0/3     None]{lang="EN-US"}

[ GigabitEthernet1/0/4     No-learning]{lang="EN-US"}

[]{#struct_0_13089_x3611_1154540948}[[表1-1 ]{lang="EN-US"}[display loopback-detection]{lang="EN-US"}]{#_Toc79392005}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x367202986}[[字段]{style="font-family:黑体"}]{#struct_0_13089_x3611_1320821866}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13089_x3611_14526329}

[[Loopback detection is enabled]{lang="EN-US"}]{#struct_0_13089_x3611_x303027172}

[[环路检测功能已使能]{style="font-family:宋体"}]{#struct_0_13089_x3611_1702383180}

[[Loopback detection is disabled]{lang="EN-US"}]{#struct_0_13089_x3611_x2142533881}

[[环路检测功能已关闭]{style="font-family:宋体"}]{#struct_0_13089_x3611_928923832}

[[Loopback detection interval is 30 second(s)]{lang="EN-US"}]{#struct_0_13089_x3611_1742270562}

[[环路检测的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_13089_x3611_76563481}[秒]{style="font-family:宋体"}

[[Loopback is detected on following interfaces]{lang="EN-US"}]{#struct_0_13089_x3611_x1018054299}

[[下列端口被检测到存在环路]{style="font-family:宋体"}]{#struct_0_13089_x3611_478264707}

[[Interface]{lang="EN-US"}]{#struct_0_13089_x3611_1223475462}

[[端口名称]{style="font-family:宋体"}]{#struct_0_13089_x3611_x2142599417}

[[Action mode]{lang="EN-US"}]{#struct_0_13089_x3611_x842619052}

[[环路检测的处理模式：]{style="font-family:宋体"}]{#struct_0_13089_x3611_x1550243066}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Block]{lang="EN-US"}]{#struct_0_13089_x3611_x1482007357}[：当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址并将端口的入方向阻塞]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_13089_x3611_x1402994079}[：当系统检测到端口出现环路时，除了生成日志信息外不对该端口进行任何处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No-learning]{lang="EN-US"}]{#struct_0_13089_x3611_1917235203}[：当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Shutdown]{lang="EN-US"}]{#struct_0_13089_x3611_x2143058168}[：当系统检测到端口出现环路时，除了生成日志信息外，还会自动关闭该端口，使其不能收发任何报文。端口被关闭后能够自动恢复，恢复时间由]{style="font-family:宋体"}**[shutdown-interval]{lang="EN-US"}**[命令（请参考"基础配置命令参考"中的"设备管理"）决定]{style="font-family:宋体"}

[[No loopback is detected]{lang="EN-US"}]{#struct_0_13089_x3611_x892583769}

[[未检测到环路]{style="font-family:宋体"}]{#struct_0_13089_x3611_x2137667529}

[[ ]{lang="EN-US"}]{#_Toc212028166}

::: {#913060921 .myid}
[]{#_Toc404784379}[]{#struct_0_13089_x3611_2068350727}

**环路检测 \-- 环路检测配置命令 \-- loopback-detection action**

------------------------------------------------------------------------

[**[loopback-detection action]{lang="EN-US"}**]{#struct_0_13089_x3611_1190413994}[命令用来在端口上配置环路检测的处理模式。]{style="font-family:
宋体"}

[**[undo loopback-detection action]{lang="EN-US"}**]{#struct_0_13089_x3611_14482015}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x111892298}

[[在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13089_x3611_529132018}[S]{lang="PT-BR"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口视图]{style="font-family:宋体"}[下：]{style="font-family:宋体"}

[**[loopback-detection action]{lang="EN-US"}**[ { **block** \| **no-learning** \| **shutdown** }]{lang="EN-US"}]{#struct_0_13089_x3611_1616529348}

[**[undo loopback-detection action]{lang="EN-US"}**]{#struct_0_13089_x3611_x2143123704}

[[在二层聚合接口视图下：]{style="font-family:宋体"}]{#struct_0_13089_x3611_x1650670478}

[**[loopback-detection action]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_13089_x3611_1552723581}

[**[undo loopback-detection action]{lang="EN-US"}**]{#struct_0_13089_x3611_1948042982}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1019454824}

[[当系统检测到端口出现环路时不对该端口进行任何处理，仅生成日志信息。]{style="font-family:宋体"}]{#struct_0_13089_x3611_422887443}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1630292744}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13089_x3611_x1910047082}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[S]{lang="PT-BR"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x283981752}

[[network-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x621757977}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x2142927096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1040143008}

[**[block]{lang="SV"}**]{#struct_0_13089_x3611_x680716093}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Block]{lang="SV"}[模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址并将端口的入方向阻塞。二层聚合接口不支持本模式。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[no-learning]{lang="EN-US"}**]{#struct_0_13089_x3611_x1553715639}[：表示]{style="font-family:宋体"}[No-learning]{lang="EN-US"}[模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。二层聚合接口不支持本模式。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[shutdown]{lang="EN-US"}**]{#struct_0_13089_x3611_x2067388574}[：表示]{style="font-family:宋体"}[Shutdown]{lang="EN-US"}[模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会自动关闭该端口，使其不能收发任何报文。被关闭的端口将在]{style="font-family:宋体"}**[shutdown-interval]{lang="EN-US"}**[命令（请参考"基础配置命令参考"中的"设备管理"）所配置的时间之后自动恢复。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13089_x3611_773816506}

[[用户可以使用]{style="font-family:宋体"}**[loopback-detection global action]{lang="EN-US"}**]{#struct_0_13089_x3611_463975536}[命令在系统视图下全局配置环路检测的处理模式，也可以使用本命令在接口视图下配置当前端口的环路检测处理模式。系统视图下的配置对所有端口都有效，接口视图下的配置则只对当前端口有效，且接口视图下的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x474760841}

[[\# ]{lang="EN-US"}]{#struct_0_13089_x3611_x1363475810}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置环路检测的处理模式为]{style="font-family:宋体"}[Shutdown]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13089_x3611_742930677}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[System-GigabitEthernet1/0/1\] loopback-detection action shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x2142992632}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display loopback-detection]{lang="EN-US"}**]{#struct_0_13089_x3611_x761336231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loopback-detection global action]{lang="EN-US"}**]{#struct_0_13089_x3611_x1681400671}
:::

::: {#-530650172 .myid}
[]{#_Toc404784380}[]{#struct_0_13089_x3611_x2001971823}[]{#_Toc212028163}

**环路检测 \-- 环路检测配置命令 \-- loopback-detection enable**

------------------------------------------------------------------------

[**[loopback-detection enable]{lang="EN-US"}**]{#struct_0_13089_x3611_1555774090}[命令用来在端口上使能环路检测功能。]{style="font-family:
宋体"}

[**[undo loopback-detection enable]{lang="EN-US"}**]{#struct_0_13089_x3611_x1300802998}[用来在端口上关闭环路检测功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1131868129}

[**[loopback-detection enable vlan]{lang="EN-US"}**[ { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_13089_x3611_x1101625755}

[**[undo loopback-detection enable vlan]{lang="EN-US"}**[ { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_13089_x3611_783366367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13089_x3611_829845255}

[[端口上的环路检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13089_x3611_x2142796024}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x477154627}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13089_x3611_x1896426394}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[S]{lang="PT-BR"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x38871056}

[[network-admin]{lang="EN-US"}]{#struct_0_13089_x3611_331367691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x1248401894}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1213258601}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_13089_x3611_x1899451841}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_13089_x3611_x738263030}[：表示所有已创建的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x345745782}

[[用户可以使用]{style="font-family:宋体"}**[loopback-detection global enable]{lang="EN-US"}**]{#struct_0_13089_x3611_x2142861560}[命令在系统视图下全局使能环路检测功能，也可以使用本命令在接口视图下使能当前端口的环路检测功能。系统视图下的配置对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的所有端口都有效，而接口视图下的配置则只对当前端口有效（该端口必须属于所指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，否则配置无效），且接口视图下的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x172378499}

[]{#_Toc212028165}[[\# ]{lang="EN-US"}]{#struct_0_13089_x3611_x1161601713}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[内的环路检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13089_x3611_x860439184}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[System-GigabitEthernet1/0/1\] loopback-detection enable vlan 10 to 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x478351089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display loopback-detection]{lang="EN-US"}**]{#struct_0_13089_x3611_x1695249013}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loopback-detection global enable]{lang="EN-US"}**]{#struct_0_13089_x3611_x255882063}
:::

::: {#612978468 .myid}
[]{#_Toc404784381}[]{#struct_0_13089_x3611_190646741}

**环路检测 \-- 环路检测配置命令 \-- loopback-detection global action**

------------------------------------------------------------------------

[**[loopback-detection global action]{lang="EN-US"}**]{#struct_0_13089_x3611_903774518}[命令用来全局配置环路检测的处理模式。]{style="font-family:宋体"}

[**[undo loopback-detection global action]{lang="EN-US"}**]{#struct_0_13089_x3611_x1046418493}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x2142664952}

[**[loopback-detection global action]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_13089_x3611_601005999}

[**[undo loopback-detection global action]{lang="EN-US"}**]{#struct_0_13089_x3611_x814475290}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13089_x3611_999370869}

[[当系统检测到端口出现环路时不对该端口进行任何处理，仅生成日志信息。]{style="font-family:宋体"}]{#struct_0_13089_x3611_384487813}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1686839615}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13089_x3611_x1951683623}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1505690561}

[[network-admin]{lang="EN-US"}]{#struct_0_13089_x3611_245439266}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x354799947}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x2142730488}

[**[shutdown]{lang="EN-US"}**]{#struct_0_13089_x3611_x411542993}[：表示]{style="font-family:宋体"}[Shutdown]{lang="EN-US"}[模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会自动关闭该端口，使其不能收发任何报文。被关闭的端口将在]{style="font-family:宋体"}**[shutdown-interval]{lang="EN-US"}**[命令（请参考"基础配置命令参考"中的"设备管理"）所配置的时间之后自动恢复。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13089_x3611_529656145}

[[用户可以使用本命令在系统视图下全局配置环路检测的处理模式，也可以使用]{style="font-family:宋体"}**[loopback-detection action]{lang="EN-US"}**]{#struct_0_13089_x3611_2001654648}[命令在接口视图下配置当前端口的环路检测处理模式。系统视图下的配置对所有端口都有效，接口视图下的配置则只对当前端口有效，且接口视图下的配置优先级较高。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x2124355045}

[[\# ]{lang="EN-US"}]{#struct_0_13089_x3611_x1854258256}[全局配置环路检测的处理模式为]{style="font-family:宋体"}[Shutdown]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13089_x3611_x1428821803}

[\[Sysname\] loopback-detection global action shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1053339964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display loopback-detection]{lang="EN-US"}**]{#struct_0_13089_x3611_517496623}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loopback-detection action]{lang="EN-US"}**]{#struct_0_13089_x3611_x2142533880}
:::

::: {#92430208 .myid}
[]{#_Toc404784382}[]{#struct_0_13089_x3611_x637160109}

**环路检测 \-- 环路检测配置命令 \-- loopback-detection global enable**

------------------------------------------------------------------------

[**[loopback-detection global enable]{lang="EN-US"}**]{#struct_0_13089_x3611_x690953713}[命令用来全局使能环路检测功能。]{style="font-family:宋体"}

[**[undo loopback-detection global enable]{lang="EN-US"}**]{#struct_0_13089_x3611_191023287}[用来全局关闭环路检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1642652622}

[**[loopback-detection global enable vlan]{lang="EN-US"}**[ { *vlan-list* \| **all** }]{lang="EN-US"}]{#struct_0_13089_x3611_77753994}

[**[undo loopback-detection global enable vlan]{lang="EN-US"}**[ { *vlan-list* \| **all** }]{lang="EN-US"}]{#struct_0_13089_x3611_x1510667504}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1562624355}

[[环路检测功能处于全局关闭状态。]{style="font-family:宋体"}]{#struct_0_13089_x3611_x863623694}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13089_x3611_129793886}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13089_x3611_x2142599416}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1886264303}

[[network-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x246592992}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x822466558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13089_x3611_335222821}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_13089_x3611_840220964}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_13089_x3611_2136495908}[：表示所有已创建的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1096401431}

[[用户可以使用本命令在系统视图下全局使能环路检测功能，也可以使用]{style="font-family:宋体"}**[loopback-detection enable]{lang="EN-US"}**]{#struct_0_13089_x3611_x2143165553}[命令在接口视图下使能当前端口的环路检测功能。系统视图下的配置对指定]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[中的所有端口都有效，而接口视图下的配置则只对当前端口有效（该端口必须属于所指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，否则配置无效），且接口视图下的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1096018791}

[[\# ]{lang="EN-US"}]{#struct_0_13089_x3611_x1205255636}[全局使能]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[内的环路检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13089_x3611_x2143058171}

[\[Sysname\] loopback-detection global enable vlan 10 to 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1029664996}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display loopback-detection]{lang="EN-US"}**]{#struct_0_13089_x3611_x1790353095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loopback-detection enable]{lang="EN-US"}**]{#struct_0_13089_x3611_x1845245418}
:::

::: {#1256592562 .myid}
[]{#_Toc404784383}[]{#struct_0_13089_x3611_478957188}

**环路检测 \-- 环路检测配置命令 \-- loopback-detection interval-time**

------------------------------------------------------------------------

[**[loopback-detection interval-time]{lang="EN-US"}**]{#struct_0_13089_x3611_x793782492}[命令用来配置环路检测的时间间隔。]{style="font-family:宋体"}

[**[undo loopback-detection interval-time]{lang="EN-US"}**]{#struct_0_13089_x3611_x949142248}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_573450129}

[**[loopback-detection interval-time ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_13089_x3611_1554354135}

[**[undo loopback-detection interval-time]{lang="EN-US"}**]{#struct_0_13089_x3611_249713348}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x2143123707}

[[环路检测的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_13089_x3611_x2053955005}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13089_x3611_35766085}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13089_x3611_x1250459598}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x1546267486}

[[network-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x1973572664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13089_x3611_x196101539}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x14700282}

[*[interval]{lang="EN-US"}*]{#struct_0_13089_x3611_630859574}[：环路检测的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13089_x3611_x2142927099}

[[当使能了环路检测功能后，系统开始以一定的时间间隔发送环路检测报文，该间隔越长耗费的系统性能越少，该间隔越短环路检测的灵敏度越高。用户可以通过本命令调整发送环路检测报文的时间间隔，以在系统性能和环路检测的灵敏度之间进行平衡。]{style="font-family:宋体"}]{#struct_0_13089_x3611_x1087197175}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13089_x3611_1267380089}

[[\# ]{lang="EN-US"}]{#struct_0_13089_x3611_35345383}[配置环路检测的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13089_x3611_x1388074503}

[\[Sysname\] loopback-detection interval-time 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13089_x3611_218380749}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display loopback-detection]{lang="EN-US"}**]{#struct_0_13089_x3611_x1085945917}
:::
