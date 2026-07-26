::: {#1535431539 .myid}
[]{#_Toc404795235}[]{#struct_0_x1399_86837_x1118911634}[]{#_Toc402451925}[]{#_Toc399849670}

**射频资源测量 \-- 射频资源测量配置命令 \-- display wlan measure-report**

------------------------------------------------------------------------

[**[display wlan measure-report]{lang="EN-US"}**]{#struct_0_x1399_86837_578221065}[命令用于显示客户端的测量报告信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1250911916}

[**[display wlan measure-report ap ]{lang="EN-US"}***[ap-name]{lang="EN-US"}***[ radio ]{lang="EN-US"}***[radio-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **client mac-address** *mac-address* \]]{lang="EN-US"}]{#struct_0_x1399_86837_274161667}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x545162247}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1399_86837_x1053350000}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1399_86837_790978932}

[[network-admin]{lang="EN-US"}]{#struct_0_x1399_86837_x1220074736}

[[network-operator]{lang="EN-US"}]{#struct_0_x1399_86837_x822866043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1399_86837_x1238165342}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1399_86837_278824718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1399_86837_400803975}

[**[ap]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_x1399_86837_832448599}[：指定客户端关联的]{style="font-family:宋体"}[AP]{lang="EN-US"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}***[ radio-number]{lang="EN-US"}*]{#struct_0_x1399_86837_547417901}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的射频号。取值范围与]{style="font-family:宋体"}[AP]{lang="EN-US"}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[client]{lang="EN-US"}**]{#struct_0_x1399_86837_1374816882}**[：]{style="font-family:宋体"}**[指定客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_x1399_86837_2047143849}[：客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x730480043}

[[如果不指定]{style="font-family:宋体"}**[client mac-address]{lang="EN-US"}**]{#struct_0_x1399_86837_x144317802}[参数，将显示所有客户端的测量信息。]{style="font-family:宋体"}
:::

::: {#187527762 .myid}
[]{#_Toc396742904}[]{#_Toc404795236}[]{#struct_0_x1399_86837_1215547878}[]{#_Toc402451927}[]{#_Toc400723199}

**射频资源测量 \-- 射频资源测量配置命令 \-- measure**

------------------------------------------------------------------------

[**[measure]{lang="EN-US"}**]{#struct_0_x1399_86837_x1291922274}[命令用于开启测量功能。]{style="font-family:宋体"}

[**[undo measure]{lang="EN-US"}**]{#struct_0_x1399_86837_x250900698}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x1096420617}

[**[measure ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[all ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[link]{lang="EN-US"}**[ \| **neighbor** \| **radio** \| **spectrum** \| **tpc** } { **enable** \| **disable** }]{lang="EN-US"}]{#struct_0_x1399_86837_1726350204}

[**[undo measure]{lang="EN-US"}**]{#struct_0_x1399_86837_x293260286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x460249733}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_1894838370}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_1650897618}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，测量功能处于关闭状态。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_973534156}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，测量功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1138081452}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x1843158909}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_1946657821}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1980431499}

[[network-admin]{lang="EN-US"}]{#struct_0_x1399_86837_x29496432}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1399_86837_x609945356}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1399_86837_24000712}

[**[all]{lang="EN-US"}**]{#struct_0_x1399_86837_1436961081}[：所有测量。]{style="font-family:宋体"}

[**[link]{lang="EN-US"}**]{#struct_0_x1399_86837_x1730568351}[：链路测量，测量针对链路测量请求帧的]{style="font-family:宋体"}[RCPI]{lang="EN-US"}[、]{style="font-family:宋体"}[RSNI]{lang="EN-US"}[和链路冗余等信息。]{style="font-family:宋体"}

[**[neighbor]{lang="EN-US"}**]{#struct_0_x1399_86837_786444554}[：邻居测量，测量邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}[的信道号、]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[等信息。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**]{#struct_0_x1399_86837_x799047579}[：射频测量，包括信道负载测量、噪声分布测量、]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[测量、]{style="font-family:宋体"}[Frame]{lang="EN-US"}[测量、]{style="font-family:宋体"}[STA]{lang="EN-US"}[统计测量、位置信息测量和传输流测量。]{style="font-family:宋体"}

[**[spectrum]{lang="EN-US"}**]{#struct_0_x1399_86837_182688218}[：频谱测量，包括]{style="font-family:宋体"}[Basic]{lang="EN-US"}[测量、]{style="font-family:宋体"}[CCA]{lang="EN-US"}[测量和]{style="font-family:宋体"}[RPI]{lang="EN-US"}[测量。]{style="font-family:宋体"}

[**[tpc]{lang="EN-US"}**]{#struct_0_x1399_86837_x302048234}[：传输功率控制测量，测量客户端的链路冗余和传输功率。]{style="font-family:宋体"}

[**[enable]{lang="EN-US"}**]{#struct_0_x1399_86837_116757847}[：开启测量。]{style="font-family:宋体"}

[**[disable]{lang="EN-US"}**]{#struct_0_x1399_86837_x1145393588}[：关闭测量。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1830510809}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有开启射频资源测量功能，]{lang="EN-US" style="font-family:宋体"}[link]{lang="EN-US"}]{#struct_0_x1399_86837_x550759304}[、]{lang="EN-US" style="font-family:宋体"}[neighbor]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[radio]{lang="EN-US"}[测量功能才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有开启频谱管理功能，]{lang="EN-US" style="font-family:宋体"}[spectrum]{lang="EN-US"}]{#struct_0_x1399_86837_x715185432}[、]{lang="EN-US" style="font-family:宋体"}[tpc]{lang="EN-US"}[测量功能才会生效。]{lang="EN-US" style="font-family:宋体"}[有关频谱管理功能相关配置的详细介绍请参见"]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[WLAN RRM]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1818898411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x2024298252}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1399_86837_1425089522}[开启频谱测量。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1399_86837_x841583580}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] measure spectrum enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_x1350591332}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1399_86837_x278209009}[开启频谱测量。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1399_86837_x1915492246}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] measure spectrum enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x551629332}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[measure-duration]{lang="EN-US"}**]{#struct_0_x1399_86837_453059334}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[measure-interval]{lang="EN-US"}**]{#struct_0_x1399_86837_348550361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[resource-measure]{lang="EN-US"}**]{#struct_0_x1399_86837_1457846971}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spectrum-management]{lang="EN-US"}**]{#struct_0_x1399_86837_1501587564}
:::

::: {#1961699920 .myid}
[]{#_Toc404795237}[]{#struct_0_x1399_86837_507805973}[]{#_Toc402451928}[]{#_Toc400723200}

**射频资源测量 \-- 射频资源测量配置命令 \-- measure-duration**

------------------------------------------------------------------------

[**[measure-duration]{lang="EN-US"}**]{#struct_0_x1399_86837_x590148975}[命令用于配置测量持续时间。]{style="font-family:宋体"}

[**[undo measure-duration]{lang="EN-US"}**]{#struct_0_x1399_86837_x1015447354}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1875218635}

[**[measure-duration ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_x1399_86837_x1771466642}

[**[undo]{lang="EN-US"}[ measure-duration]{lang="EN-US"}**]{#struct_0_x1399_86837_x144095186}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1887299775}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x1292941448}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x971689585}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，测量持续时间为]{style="font-family:宋体"}[500TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_x894637738}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，测量持续时间为]{style="font-family:宋体"}[500TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1206229759}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x1900266078}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_1821394528}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x659136103}

[[network-admin]{lang="EN-US"}]{#struct_0_x1399_86837_421475939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1399_86837_725360827}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1073655610}

[*[time]{lang="EN-US"}*]{#struct_0_x1399_86837_931697301}[：测量持续时间，取值范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[TU]{lang="EN-US"}[（]{style="font-family:宋体"}[Time Unit]{lang="EN-US"}[，]{style="font-family:宋体"}[1TU=1024]{lang="EN-US"}[微秒）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1611646534}

[[开启测量功能后，在]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1399_86837_x817304041}[向客户端发送的测量请求报文中携带配置的测量持续时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1399_86837_871867564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x46629800}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1399_86837_x485287684}[配置测量持续时间为]{style="font-family:宋体"}[512TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1399_86837_x532241903}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] measure-duration 512]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_x1662292651}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1399_86837_1753397488}[配置测量持续时间为]{style="font-family:宋体"}[512TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1399_86837_x539560722}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] measure-duration 512]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x541531531}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[measure]{lang="EN-US"}**]{#struct_0_x1399_86837_x1197898294}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[measure-interval]{lang="EN-US"}**]{#struct_0_x1399_86837_1548039044}
:::

::: {#1940760751 .myid}
[]{#_Toc404795238}[]{#struct_0_x1399_86837_x1416078004}[]{#_Toc402451929}[]{#_Toc400723201}

**射频资源测量 \-- 射频资源测量配置命令 \-- measure-interval**

------------------------------------------------------------------------

[**[measure-interval]{lang="EN-US"}**]{#struct_0_x1399_86837_569043118}[命令用于配置发送测量请求的时间间隔。]{style="font-family:宋体"}

[**[undo measure-interval]{lang="EN-US"}**]{#struct_0_x1399_86837_x1797336183}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x1967753526}

[**[measure-interval ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1399_86837_1886183832}

[**[undo measure-interval]{lang="EN-US"}**]{#struct_0_x1399_86837_x2051371625}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1399_86837_875409191}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x1816147459}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x1580541366}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，发送测量请求间隔时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_x1529026519}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，发送测量请求间隔时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1416135881}

[[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x662543665}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_1965326075}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x589623408}

[[network-admin]{lang="EN-US"}]{#struct_0_x1399_86837_209178768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1399_86837_2127872160}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x636743789}

[*[value]{lang="EN-US"}*]{#struct_0_x1399_86837_x1516021928}[：发送测量请求的时间间隔，取值范围]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x1591209963}

[[开启测量功能后，]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x1399_86837_x2015735947}[以配置的时间间隔定时向客户端发送的测量请求报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1399_86837_677511730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x1399_86837_x609001945}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1399_86837_x1163959020}[配置发送测量请求间隔时间为]{style="font-family:宋体"}[35]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1399_86837_x2080482791}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] measure-interval 35]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x1399_86837_x615290647}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1399_86837_x1515662858}[配置发送测量请求间隔时间为]{style="font-family:宋体"}[35]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1399_86837_x719636103}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] measure-interval 35]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1119468564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[measure]{lang="EN-US"}**]{#struct_0_x1399_86837_x16995977}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[measure-duration]{lang="EN-US"}**]{#struct_0_x1399_86837_220918119}
:::

::: {#1079210731 .myid}
[]{#_Toc404795239}[]{#struct_0_x1399_86837_1867025322}

**射频资源测量 \-- 射频资源测量配置命令 \-- resource-measure**

------------------------------------------------------------------------

[**[resource-measure]{lang="EN-US" style="color:black"}**]{#struct_0_x1399_86837_x1275290923}**[ enable]{lang="IT"}**[命令用于开启射频资源测量功能。]{style="font-family:宋体"}

[**[resource-measure]{lang="EN-US" style="color:black"}**]{#struct_0_x1399_86837_1056797084}**[ disable]{lang="IT"}**[命令用于关闭射频资源测量功能。]{style="font-family:宋体"}

[**[undo ]{lang="IT"}**]{#struct_0_x1399_86837_x944704405}**[resource-measure]{lang="EN-US" style="color:black"}**[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x888572211}

[**[resource measure]{lang="EN-US" style="color:black"}**]{#struct_0_x1399_86837_x1938924650}**[ ]{lang="EN-US"}**[{ **enable** \| **disable** }]{lang="IT"}

[**[undo ]{lang="IT"}**]{#struct_0_x1399_86837_x1857612190}**[resource measure]{lang="EN-US" style="color:black"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x1949863115}

[[射频资源测量功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1399_86837_2027350489}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x16243004}

[[Radio]{lang="EN-US"}]{#struct_0_x1399_86837_x1335418552}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x2081952935}

[[network-admin]{lang="EN-US"}]{#struct_0_x1399_86837_1840264119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1399_86837_x613060181}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x943664720}

[[\# ]{lang="IT"}]{#struct_0_x1399_86837_236076834}[开启射频资源测量功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x1399_86837_x143678888}

[[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}]{#struct_0_x1399_86837_x1451379088}

[[\[Sysname-wlan-ap-ap1\] radio 2]{lang="IT"}]{#struct_0_x1399_86837_x1985227832}

[[\[Sysname-wlan-ap-ap1-radio-2\] ]{lang="IT"}[resource-measure]{lang="EN-US"}]{#struct_0_x1399_86837_x808780033}[ enable]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1840311144}

[[开启射频资源测量功能后：]{style="font-family:宋体"}]{#struct_0_x1399_86837_164018320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_x1399_86837_x375009509}[发送的]{lang="EN-US" style="font-family:
宋体"}[Beacon]{lang="EN-US"}[、]{lang="EN-US" style="font-family:
宋体"}[Probe Response]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Association Response]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Reassociation Response]{lang="EN-US"}[帧中，能力集字段中的]{lang="EN-US" style="font-family:宋体"}[Radio Measurement]{lang="EN-US"}[位会被置位，并携带]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[支持的射频]{lang="EN-US" style="font-family:宋体"}[资源]{style="font-family:宋体"}[测量能力信息，用于告知客户端，]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[支持射频资源测量，以及支持的测量类型。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_x1399_86837_513992744}[通过]{lang="EN-US" style="font-family:
宋体"}[定期]{style="font-family:宋体"}[发送]{lang="EN-US" style="font-family:宋体"}[Measurement Pilot]{lang="EN-US"}[帧协助]{style="font-family:宋体"}[客户端更快地扫描到]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[Measurement Pilot]{lang="EN-US"}[报文可视为轻量级的]{lang="EN-US" style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧，其发送的频率比]{lang="EN-US" style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧]{style="font-family:宋体"}[高，但携带的信息比]{lang="EN-US" style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧]{style="font-family:宋体"}[少。]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1297558139 .myid}
[]{#_Toc404795240}[]{#struct_0_x1399_86837_2091623739}[]{#_Toc396742905}

**射频资源测量 \-- 射频资源测量配置命令 \-- rm-capability mode**

------------------------------------------------------------------------

[**[rm-capability mode]{lang="IT"}**]{#struct_0_x1399_86837_1774120604}[命令用于配置对客户端射频测量能力集的检查模式。]{style="font-family:宋体"}

[**[undo rm-capability mode]{lang="IT"}**]{#struct_0_x1399_86837_187380967}[命令用于恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x1240851823}

[**[rm-capability mode ]{lang="IT"}**]{#struct_0_x1399_86837_2104563965}[{ **all** \| ]{lang="IT"}**[none ]{lang="EN-US"}**[\| ]{lang="IT"}**[partial]{lang="EN-US"}[ ]{lang="EN-US"}**[}]{lang="IT"}

[**[undo rm-capability mode]{lang="IT"}**]{#struct_0_x1399_86837_x2143247629}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1671272066}

[[不检查客户端射频测量能力集。]{style="font-family:宋体"}]{#struct_0_x1399_86837_1440947840}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1399_86837_619183020}

[[Radio]{lang="EN-US"}]{#struct_0_x1399_86837_x26657744}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1949847910}

[[network-admin]{lang="EN-US"}]{#struct_0_x1399_86837_x214369338}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1399_86837_274227203}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1399_86837_1633570269}

[**[all]{lang="EN-US"}**]{#struct_0_x1399_86837_727913589}[：完全匹配模式。只有客户端的射频测量能力集与]{style="font-family:宋体"}[AP]{lang="EN-US"}[的能力集全部匹配，才允许客户端上线，否则，不允许客户端上线。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x1399_86837_x1211336388}[：不检查模式，即不检查客户端射频测量能力集。]{style="font-family:宋体"}

[**[partial]{lang="EN-US"}**]{#struct_0_x1399_86837_1330005662}[：部分匹配模式。配置部分匹配模式时，客户端的射频测量能力集与设备的能力集只要有一个匹配，则允许客户端上线，否则，不允许客户端上线。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x1782723046}

[[只有开启射频资源测量功能，射频测量能力集检查功能才会生效。]{style="font-family:宋体"}]{#struct_0_x1399_86837_1464149762}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x335142030}

[[\# ]{lang="IT"}]{#struct_0_x1399_86837_x1680291003}[配置对客户端射频测量能力集的检查模式为部分匹配模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x1399_86837_x253946235}

[[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}]{#struct_0_x1399_86837_1518155595}

[[\[Sysname-wlan-ap-ap1\] radio 2]{lang="IT"}]{#struct_0_x1399_86837_x1457102131}

[[\[Sysname-wlan-ap-ap1-radio-2\] ]{lang="IT"}[resource-measure]{lang="EN-US"}]{#struct_0_x1399_86837_x349788839}[ enable]{lang="EN-US"}

[[\[Sysname-wlan-ap-ap1-radio-2\] rm-capability mode partial]{lang="IT"}]{#struct_0_x1399_86837_x1703299508}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1399_86837_x1357162823}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[resource-measure]{lang="IT"}**]{#struct_0_x1399_86837_x1585136413}

[]{#_Toc396290138}[]{#_Toc396290139}[]{#_Toc396290140}[]{#_Toc396290141}[]{#_Toc396290142}[ ]{lang="IT"}
:::
