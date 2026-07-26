::: {#-275634315 .myid}
[]{#_Toc293559741}[]{#_Toc404797953}[]{#struct_0_x1068_x9952_x1988512502}[]{#_Toc339972636}

**TRILL \-- TRILL配置命令 \-- auto-cost enable**

------------------------------------------------------------------------

[**[auto-cost]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_73982160}[命令用来开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口链路开销值的自动计算功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **auto-cost** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_1168781662}[命令用来关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口链路开销值的自动计算功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1363658764}

[**[auto-cost]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x791413854}

[**[undo]{lang="EN-US"}**[ **auto-cost** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1968388008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x201195531}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_2027698149}[端口链路开销值的自动计算功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1241592707}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1715386417}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x910168452}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_631535343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1398109907}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x791086174}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1995043211}[端口的链路开销可以由系统自动计算或用户手工配置，其中手工配置优先，即：只要进行了手工配置，就取手工配置值；如果没有进行手工配置，若开启了自动计算功能则取自动计算值，若关闭了自动计算功能则取缺省值]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_2075010780}[端口链路开销值自动计算的公式如下：链路开销值＝]{style="font-family:宋体"}[20000000000000]{lang="EN-US"}[÷端口波特率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_37431422}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x2025502046}[关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口链路开销值的自动计算功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1508657858}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] undo auto-cost enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1471125289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**[ **cost**]{lang="EN-US"}]{#struct_0_x1068_x9952_759754722}
:::

::: {#1263346545 .myid}
[]{#_Toc404797954}[]{#struct_0_x1068_x9952_x1833061572}

**TRILL \-- TRILL配置命令 \-- display trill adjacent-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **adjacent-table**]{lang="EN-US"}]{#struct_0_x1068_x9952_x791020638}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻接表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1222367933}

[**[display]{lang="EN-US"}**[ **trill** **adjacent-table** \[ **count** \| **nickname** *nickname* **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x2013064893}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_444420191}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1619942479}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2104831601}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_160383336}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1073435060}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1747766894}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x791217246}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2026202599}

[**[count]{lang="EN-US"}**]{#struct_0_x1068_x9952_1591136021}[：显示表项的数量。]{style="font-family:宋体"}

[**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}[ **interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1068_x9952_467222981}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[指定端口上的信息。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数；]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为端口类型和端口编号。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RB]{lang="EN-US"}[所有端口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1865217578}

[]{#_Ref189458167}[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1472843295}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻接表所有表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill adjacent-table]{lang="EN-US"}]{#struct_0_x1068_x9952_x791151710}

[NextHop     MAC address       Interface]{lang="EN-US"}

[0x899b      00e0-fc58-123a    GE1/0/1]{lang="EN-US"}

[[\# ]{lang="FR"}]{#struct_0_x1068_x9952_x2004045563}[显示]{style="font-family:宋体"}[TRILL]{lang="FR"}[邻接表的表项数量。]{style="font-family:宋体"}

[[\<Sysname\> display trill adjacent-table count]{lang="FR"}]{#struct_0_x1068_x9952_x2042612963}

[Total number of TRILL ADJ entries: 1]{lang="FR"}

[]{#struct_0_x1068_x9952_422533128}[[表1-1 ]{lang="EN-US"}[display trill adjacent-table]{lang="EN-US"}]{#_Toc94583057}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1005930752}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x831351967}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x548115043}

[[NextHop]{lang="EN-US"}]{#struct_0_x1068_x9952_193049333}

[[报文转发的下一跳]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_1170377011}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_x790824030}

[[报文转发的下一跳]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_701036823}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_716279829}

[[报文的出端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1330932574}

[[Total number of TRILL ADJ entries]{lang="EN-US"}]{#struct_0_x1068_x9952_306296354}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_29927416}[邻接表的表项数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1183541893 .myid}
[]{#_Toc404797955}[]{#struct_0_x1068_x9952_x790758494}

**TRILL \-- TRILL配置命令 \-- display trill brief**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **brief**]{lang="EN-US"}]{#struct_0_x1068_x9952_1540653430}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x801648905}

[**[display]{lang="EN-US"}**[ **trill** **brief**]{lang="EN-US"}]{#struct_0_x1068_x9952_1510315644}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1293655268}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2002952047}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1675512425}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1566827109}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x2041507827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x791348317}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_1138000138}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x289008356}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1739300649}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill brief]{lang="EN-US"}]{#struct_0_x1068_x9952_x791282781}

[Network entity: 00.00a0.fc00.5806.00]{lang="EN-US"}

[Nickname: 0xfa1b]{lang="EN-US"}

[Nickname priority: 64]{lang="EN-US"}

[Tree-root priority: 32768]{lang="EN-US"}

[Cost style: Wide]{lang="EN-US"}

[Maximum allowed LSP received: 1492]{lang="EN-US"}

[Maximum allowed LSP originated: 1458]{lang="EN-US"}

[Maximum unicast load-balancing: 8]{lang="EN-US"}

[Overload status: None]{lang="EN-US"}

[Overload remaining time: N/A]{lang="EN-US"}

[Device role: Normal]{lang="EN-US"}

[Timers:]{lang="EN-US"}

[  LSP-max-age: 1200s]{lang="EN-US"}

[  LSP-refresh: 900s]{lang="EN-US"}

[  Interval between SPFs: 10s  10ms  20ms]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display trill brief]{lang="EN-US"}]{#struct_0_x1068_x9952_x407684028}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1003899424}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1237072882}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1336926979}

[[Network entity]{lang="EN-US"}]{#struct_0_x1068_x9952_569780929}

[[网络实体的名称]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1001270470}

[[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_x541121491}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x791479389}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[Nickname priority]{lang="EN-US"}]{#struct_0_x1068_x9952_x1600516935}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_1339005618}[拥有]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[的优先级]{style="font-family:宋体"}

[[Tree-root priority]{lang="EN-US"}]{#struct_0_x1068_x9952_1166724627}

[[设备作为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1616960039}[分发树根桥的优先级]{style="font-family:宋体"}

[[Cost style]{lang="EN-US"}]{#struct_0_x1068_x9952_x1427380938}

[[开销类型，仅支持]{style="font-family:宋体"}[Wide]{lang="EN-US"}]{#struct_0_x1068_x9952_x791413853}[类型]{style="font-family:宋体"}

[[Maximum allowed LSP received]{lang="EN-US"}]{#struct_0_x1068_x9952_x1968846760}

[[可接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1270929538}[最大长度]{style="font-family:宋体"}

[[Maximum allowed LSP originated]{lang="EN-US"}]{#struct_0_x1068_x9952_864586777}

[[可生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_2134906724}[最大长度]{style="font-family:宋体"}

[[Maximum unicast load-balancing]{lang="EN-US"}]{#struct_0_x1068_x9952_x791086173}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1994584459}[单播等价多路径的最大路径数]{style="font-family:宋体"}

[[Overload status]{lang="EN-US"}]{#struct_0_x1068_x9952_1909194613}

[[过载标志位的置位原因：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x406653384}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Config]{lang="EN-US"}]{#struct_0_x1068_x9952_x29131503}[：表示配置过载标志位置位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GR]{lang="EN-US"}]{#struct_0_x1068_x9952_x791020637}[：表示在平滑重启中过载标志位置位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GR/Config]{lang="EN-US"}]{#struct_0_x1068_x9952_x1222695613}[：表示在]{style="font-family:宋体"}[Start]{lang="EN-US"}[类型的平滑重启中配置过载标志位置位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x1068_x9952_x712383067}[：表示未配置过载标志位置位]{style="font-family:宋体"}

[[Device role]{lang="EN-US"}]{#struct_0_x1068_x9952_173724319}

[[设备角色：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1803979248}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x1068_x9952_x595444678}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[普通]{lang="EN-US" style="font-family:宋体"}[RB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Access]{lang="EN-US"}]{#struct_0_x1068_x9952_173658783}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[二层接入设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Gateway]{lang="EN-US"}]{#struct_0_x1068_x9952_x470370649}[：表示网关设备]{lang="EN-US" style="font-family:宋体"}

[[Overload remaining time]{lang="EN-US"}]{#struct_0_x1068_x9952_808809604}

[[过载标志位保持置位状态的时间，单位为秒。]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x1068_x9952_259750453}[表示未配置此时间或此时间已超时]{style="font-family:宋体"}

[[Timers]{lang="EN-US"}]{#struct_0_x1068_x9952_x791217245}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x2026137063}[定时器]{style="font-family:宋体"}

[[LSP-max-age]{lang="EN-US"}]{#struct_0_x1068_x9952_x1642390677}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x960609195}[的最大生存时间，单位为秒]{style="font-family:宋体"}

[[LSP-refresh]{lang="EN-US"}]{#struct_0_x1068_x9952_x791151709}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x2004635386}[的刷新周期，单位为秒]{style="font-family:宋体"}

[[Interval between SPFs]{lang="EN-US"}]{#struct_0_x1068_x9952_1912132643}

[[依次为使用]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x1068_x9952_x227009580}[（]{style="font-family:宋体"}[Shortest Path First]{lang="EN-US"}[，最短路径优先）算法进行路由计算的最大时间间隔（单位为秒）、最小时间间隔（单位为毫秒）和时间间隔惩罚增量（单位为毫秒）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1309111719 .myid}
[]{#_Toc65310809}[]{#_Toc36367100}[]{#_Toc34185794}[]{#_Toc404797956}[]{#struct_0_x1068_x9952_598612447}[]{#_Toc293559740}

**TRILL \-- TRILL配置命令 \-- display trill fib**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **fib**]{lang="EN-US"}]{#struct_0_x1068_x9952_x790824029}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[单播转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_701626646}

[**[display]{lang="EN-US"}**[ **trill** **fib** \[ **count** \| **nickname** *nickname* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x821767015}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2006551777}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2127721432}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1319010445}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1820067113}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x733364412}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x790758493}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_1540718966}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x446306234}

[**[count]{lang="EN-US"}**]{#struct_0_x1068_x9952_596399438}[：显示表项的数量。]{style="font-family:宋体"}

[**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}]{#struct_0_x1068_x9952_x432073691}[：显示指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数]{style="font-family:宋体"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RB]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1487579583}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x899409719}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[单播转发表所有表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill fib]{lang="EN-US"}]{#struct_0_x1068_x9952_x791348320}

[Flags: T-Transit, E-Egress]{lang="EN-US"}

[Destination   HopCount   NextHop   Interface                Flags]{lang="EN-US"}

[0xfa1b        63         ]{lang="DE"}[N/A   ]{lang="EN-US"}[    ]{lang="DE"}[N/A                      ]{lang="EN-US"}[E]{lang="DE"}

[0x899b        63         0x2a5c    GE1/0/1                  T]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x1068_x9952_1137541385}[显示]{style="font-family:宋体"}[TRILL]{lang="DE"}[单播转发表的表项数量。]{style="font-family:宋体"}

[[\<Sysname\> display trill fib count]{lang="DE"}]{#struct_0_x1068_x9952_690003941}

[Total number of TRILL FIB destinations: 1]{lang="DE"}

[Total number of TRILL FIB entries: 2]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display trill fib]{lang="EN-US"}]{#struct_0_x1068_x9952_2065965017}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x980201600}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_673484040}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1126627485}

[[Destination]{lang="EN-US"}]{#struct_0_x1068_x9952_2100674315}

[[目的]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x779294184}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[HopCount]{lang="EN-US"}]{#struct_0_x1068_x9952_x791282784}

[[到达目的]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x408011708}[的跳数]{style="font-family:宋体"}

[[NextHop]{lang="EN-US"}]{#struct_0_x1068_x9952_193488153}

[[下一跳]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_1692311417}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_x343612365}

[[报文的出端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x6346660}

[[Flags]{lang="DE"}]{#struct_0_x1068_x9952_x791479392}

[[标志：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1599796038}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1068_x9952_x1598868204}[：表示转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x1068_x9952_x920861998}[：表示出隧道]{style="font-family:宋体"}

[[Total number of TRILL FIB destinations]{lang="EN-US"}]{#struct_0_x1068_x9952_x1302694274}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x791413856}[单播转发表中目的]{style="font-family:宋体"}[RB]{lang="EN-US"}[的数量]{style="font-family:宋体"}

[[Total number of TRILL FIB entries]{lang="EN-US"}]{#struct_0_x1068_x9952_x1968519080}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x246780870}[单播转发表的表项数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1978935495 .myid}
[]{#_Toc404797957}[]{#struct_0_x1068_x9952_x1996156560}[]{#_Toc326062189}

**TRILL \-- TRILL配置命令 \-- display trill graceful-restart status**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**]{#struct_0_x1068_x9952_1328055276}[ **tril**l **graceful-restart** **status**]{lang="EN-US"}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[（]{style="font-family:宋体"}[Graceful Restart]{lang="EN-US"}[，平滑重启）状态信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_244504084}

[**[display]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1599850663}[ **trill** **graceful-restart** **status**]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x791086176}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1994912139}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x320676441}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1185093736}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x825228584}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x234576506}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1491404482}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1039620946}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1409316929}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill graceful-restart status]{lang="EN-US"}]{#struct_0_x1068_x9952_x791020640}

[Restart status: RESTARTING]{lang="EN-US"}

[Restart phase: LSDB synchronization]{lang="EN-US"}

[Restart interval: 300s]{lang="EN-US"}

[T3 remaining time: 140s]{lang="EN-US"}

[Total number of interfaces: 1]{lang="EN-US"}

[Number of waiting LSPs: 3]{lang="EN-US"}

[T2 remaining time: 55s]{lang="EN-US"}

[  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    T1 remaining time: 2s]{lang="EN-US"}

[    RA received: Y]{lang="EN-US"}

[    CSNP received: N]{lang="EN-US"}

[    T1 expiration number: 1]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display trill graceful-restart status]{lang="EN-US"}]{#struct_0_x1068_x9952_x1222892228}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x977380800}[[字段]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x635491152}
:::

[[描述]{style="font-family:宋体"}]{#struct_0_x1068_x9952_577596924}

[[Restart status]{lang="EN-US"}]{#struct_0_x1068_x9952_x791217248}

[[重启状态：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2025809383}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_x1068_x9952_x712764658}[：表示]{lang="EN-US" style="font-family:宋体"}[平滑]{style="font-family:宋体"}[重启已完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESTARTING]{lang="EN-US"}]{#struct_0_x1068_x9952_x1983208146}[：表示正进行]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[estart]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[平滑]{style="font-family:宋体"}[重启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STARTING]{lang="EN-US"}]{#struct_0_x1068_x9952_1106602452}[：表示正进行]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[tart]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[平滑]{style="font-family:宋体"}[重启]{lang="EN-US" style="font-family:宋体"}

[[Restart phase]{lang="EN-US"}]{#struct_0_x1068_x9952_x350143891}

[[重启阶段：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x791151712}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_x1068_x9952_x2004176635}[：表示平滑重启已完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSDB synchronization]{lang="EN-US"}]{#struct_0_x1068_x9952_x621796271}[：表示]{lang="EN-US" style="font-family:
  宋体"}[T2]{lang="EN-US"}[同步阶段]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_x1068_x9952_x1269622715}[：表示]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[生成阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MCS synchronization]{lang="EN-US"}]{#struct_0_x1068_x9952_x1728284351}[：表示二层组播数据同步阶段]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPF]{lang="EN-US"}]{#struct_0_x1068_x9952_x2130573160}[：表示路由计算阶段]{style="font-family:宋体"}

[[Restart interval]{lang="EN-US"}]{#struct_0_x1068_x9952_x790824032}

[[重启间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_x1068_x9952_700905751}

[[T3 remaining time]{lang="EN-US"}]{#struct_0_x1068_x9952_x1876269004}

[[T3]{lang="EN-US"}]{#struct_0_x1068_x9952_1245962522}[定时器的超时剩余时间，单位为秒。初始值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒，后续会根据]{style="font-family:宋体"}[RA]{lang="EN-US"}[报文中的剩余时间来更新]{style="font-family:宋体"}

[[Total number of interfaces]{lang="EN-US"}]{#struct_0_x1068_x9952_1620466039}

[[进程下的所有端口数]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x790758496}

[[Number of waiting LSPs]{lang="EN-US"}]{#struct_0_x1068_x9952_1540522358}

[[等待的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x808035849}[数量]{style="font-family:宋体"}

[[T2 remaining time]{lang="EN-US"}]{#struct_0_x1068_x9952_x652068991}

[[T2]{lang="EN-US"}]{#struct_0_x1068_x9952_1211864693}[定时器的超时剩余时间，单位为秒。对于]{style="font-family:宋体"}[Restart]{lang="EN-US"}[类型的]{style="font-family:宋体"}[GR]{lang="EN-US"}[，初始值固定为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒；对于]{style="font-family:宋体"}[Start]{lang="EN-US"}[类型的]{style="font-family:宋体"}[GR]{lang="EN-US"}[，初始值为]{style="font-family:宋体"}**[graceful-restart interval]{lang="EN-US"}**[命令的配置值（缺省为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒）]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_x791348319}

[[端口名称]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1138131210}

[[T1 remaining time]{lang="EN-US"}]{#struct_0_x1068_x9952_x1445420958}

[[T1]{lang="EN-US"}]{#struct_0_x1068_x9952_x711241525}[定时器的超时剩余时间，单位为秒。初始值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[RA received]{lang="EN-US"}]{#struct_0_x1068_x9952_x791282783}

[[RA]{lang="EN-US"}]{#struct_0_x1068_x9952_x407552956}[接收标记位：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_x1068_x9952_x1209202670}[：表示置位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x1068_x9952_x835736152}[：表示未置位]{lang="EN-US" style="font-family:宋体"}

[[CSNP received]{lang="EN-US"}]{#struct_0_x1068_x9952_x1208354435}

[[CSNP]{lang="EN-US"}]{#struct_0_x1068_x9952_x791479391}[接收标记位：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_x1068_x9952_x1599992646}[：表示置位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x1068_x9952_985222104}[：表示未置位]{lang="EN-US" style="font-family:宋体"}

[[T1 expiration number]{lang="EN-US"}]{#struct_0_x1068_x9952_x1772958140}

[[T1]{lang="EN-US"}]{#struct_0_x1068_x9952_x791413855}[定时器的超时次数。最大值为]{style="font-family:宋体"}[10]{lang="EN-US"}[次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-184934579 .myid}
[]{#_Toc404797958}[]{#struct_0_x1068_x9952_1523803190}[]{#_Toc386113371}[]{#_Toc385854369}[]{#_Toc379615177}

**TRILL \-- TRILL配置命令 \-- display trill ingress-route**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **ingress-route**]{lang="EN-US"}]{#struct_0_x1068_x9952_x42280751}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[入流量的转发信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2003530432}

[**[display]{lang="EN-US"}**[ **trill** **ingress-route** \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x465852879}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x718730501}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1209806145}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1080990040}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_177278018}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_1894134957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1109054721}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x67014236}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1964595052}

[**[vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}]{#struct_0_x1068_x9952_x1887812952}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}[v*lan-list*]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1677989228}

[[通过本命令可以显示流量进入]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1874074222}[网络的本地入端口，以及流量转发所使用的树根和出端口信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1413806219}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x271736275}[显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[入流量的转发信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill ingress-route]{lang="EN-US"}]{#struct_0_x1068_x9952_130661955}

[Total number of VLANs: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[VLAN ID:]{lang="EN-US"}

[  1]{lang="EN-US"}

[List of local ports:]{lang="EN-US"}

[  GE1/0/1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[VLAN ID:]{lang="EN-US"}

[  1]{lang="EN-US"}

[Tree root:]{lang="EN-US"}

[  0x1111]{lang="EN-US"}

[List of remote ports:]{lang="EN-US"}

[  GE1/0/2]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display trill ingress-route]{lang="EN-US"}]{#struct_0_x1068_x9952_1793539350}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1003000003}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_764288303}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_275101371}

[[Total number of VLANs]{lang="EN-US"}]{#struct_0_x1068_x9952_x1983137091}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_1169322537}[总数]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1068_x9952_x1353040600}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x1742582420}[的编号]{style="font-family:宋体"}

[[List of local ports]{lang="EN-US"}]{#struct_0_x1068_x9952_x604466478}

[[流量进入]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1501813406}[网络的本地入端口]{style="font-family:宋体"}

[[Tree root]{lang="EN-US"}]{#struct_0_x1068_x9952_538226246}

[[本]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x2261644}[转发组播流量所使用的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树树根的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[List of remote ports]{lang="EN-US"}]{#struct_0_x1068_x9952_986300935}

[[报文经]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x190365414}[封装后的转发出端口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2064055765 .myid}
[]{#_Toc404797959}[]{#struct_0_x1068_x9952_x1968453544}

**TRILL \-- TRILL配置命令 \-- display trill interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **interface**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1244083411}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x43419510}

[**[display]{lang="EN-US"}**[ **trill** **interface** \[ *interface-type* *interface-number* \| **verbose** \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x2007852279}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_158580002}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1465026965}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x791086175}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1994977675}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1902657520}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1668185344}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x963891823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1163957861}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x1068_x9952_x172522780}[：显示指定端口的信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为端口类型和端口编号。如果未指定本参数，将显示所有端口的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1690287205}[：显示详细信息。如果未指定本参数，将显示摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1202000994}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1970333644}[显示所有]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill interface]{lang="EN-US"}]{#struct_0_x1068_x9952_1785702849}

[Interface                   Protocol state   DRB  Cost      Link type]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[GigabitEthernet1/0/1        UP               Yes  2000      Access]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_861133362}[显示所有]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill interface verbose]{lang="EN-US"}]{#struct_0_x1068_x9952_x791020639}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Protocol state: UP]{lang="EN-US"}

[Nickname: 0xfa1b]{lang="EN-US"}

[MTU: 1470]{lang="EN-US"}

[DRB: Yes]{lang="EN-US"}

[Designated VLAN: 1]{lang="EN-US"}

[Link type: Access]{lang="EN-US"}

[CSNP timer: 10s]{lang="NO-BOK"}

[Hello timer: 10s]{lang="NO-BOK"}

[Hello multiplier: 3]{lang="NO-BOK"}

[LSP timer: 10ms]{lang="NO-BOK"}

[LSP transmit-throttle count: 5]{lang="EN-US"}

[Cost: 2000]{lang="EN-US"}

[AVF inhibited timer: 30s]{lang="EN-US"}

[Priority: 64]{lang="EN-US"}

[Track index: None]{lang="EN-US"}

[Track state: NotReady]{lang="EN-US"}

[Active AVF:]{lang="EN-US"}

[  1-3, 5, 58]{lang="EN-US"}

[Inhibited AVF: None]{lang="EN-US"}

[]{#struct_0_x1068_x9952_x1222302397}[[表1-6 ]{lang="EN-US"}[display trill interface]{lang="EN-US"}]{#_Toc283318652}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x981706752}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1241283687}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x791217247}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_x2026268135}

[[端口名称]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x33724477}

[[Protocol state]{lang="EN-US"}]{#struct_0_x1068_x9952_200216446}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1267132782}[协议的状态，包括]{style="font-family:宋体"}[UP]{lang="EN-US"}[和]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_2026716379}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x791151711}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[MTU]{lang="EN-US"}]{#struct_0_x1068_x9952_x2004111099}

[[链路的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x1068_x9952_1048504001}[值，单位为字节]{style="font-family:宋体"}

[[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x2034339641}

[[是否被选举为]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1627704839}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x1068_x9952_x580013715}[：表示已被选举为]{style="font-family:宋体"}[DRB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x1068_x9952_x790824031}[：表示未被选举为]{style="font-family:宋体"}[DRB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1068_x9952_34047586}[：表示端口状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[，不参与]{style="font-family:宋体"}[DRB]{lang="EN-US"}[的选举]{style="font-family:宋体"}

[[Designated VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_701102359}

[[当前生效的指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x1164997163}[。如果显示为]{style="font-family:宋体"}[65535]{lang="EN-US"}[，表示端口]{style="font-family:宋体"}[down]{lang="EN-US"}[或端口下没有使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Link type]{lang="EN-US"}]{#struct_0_x1068_x9952_1341720010}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x682933386}[端口的类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Access]{lang="EN-US"}]{#struct_0_x1068_x9952_x790758495}[：表示]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hybrid]{lang="EN-US"}]{#struct_0_x1068_x9952_1540587894}[：表示]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Trunk]{lang="EN-US"}]{#struct_0_x1068_x9952_376896562}[：表示]{lang="EN-US" style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_173724321}[：表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[CSNP timer]{lang="EN-US"}]{#struct_0_x1068_x9952_x1032613561}

[[CSNP]{lang="EN-US"}]{#struct_0_x1068_x9952_774735625}[报文的发送间隔，单位为秒]{style="font-family:宋体"}

[[Hello timer]{lang="NO-BOK"}]{#struct_0_x1068_x9952_249523791}

[[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_x1092566906}[报文发送间隔，单位为秒]{style="font-family:宋体"}

[[Hello multiplier]{lang="NO-BOK"}]{#struct_0_x1068_x9952_x499256772}

[[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_x633729358}[报文的失效数目]{style="font-family:宋体"}

[[LSP timer]{lang="NO-BOK"}]{#struct_0_x1068_x9952_774801161}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_1229889259}[的最小发送间隔，单位为毫秒]{style="font-family:宋体"}

[[LSP transmit-throttle count]{lang="EN-US"}]{#struct_0_x1068_x9952_370560078}

[[一次发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1058661471}[的最大数目]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x1068_x9952_774604553}

[[端口的链路开销值]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1744909187}

[[AVF inhibited timer]{lang="EN-US"}]{#struct_0_x1068_x9952_493510324}

[[环路避免的抑制时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x1068_x9952_900822094}

[[Priority]{lang="EN-US"}]{#struct_0_x1068_x9952_774670089}

[[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_1817717121}[优先级]{style="font-family:宋体"}

[[Track index]{lang="EN-US"}]{#struct_0_x1068_x9952_1389585462}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x475611696}[监测的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项，]{style="font-family:宋体"}[None]{lang="EN-US"}[表示没有]{style="font-family:宋体"}

[[Track state]{lang="EN-US"}]{#struct_0_x1068_x9952_x637891027}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1111134595}[监测的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NotReady]{lang="EN-US"}]{#struct_0_x1068_x9952_x176498479}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[没有监测任何]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项]{lang="EN-US" style="font-family:宋体"}[或未连接]{style="font-family:宋体"}[Track]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Positive]{lang="EN-US"}]{#struct_0_x1068_x9952_890330540}[：]{lang="EN-US" style="font-family:宋体"}[表示状态正常]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Negative]{lang="EN-US"}]{#struct_0_x1068_x9952_x1975614245}[：]{lang="EN-US" style="font-family:宋体"}[表示状态异常]{style="font-family:宋体"}

[[Active AVF]{lang="EN-US"}]{#struct_0_x1068_x9952_x1056999071}

[[当前端口上被]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1318843032}[分配为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[None]{lang="EN-US"}[表示没有]{style="font-family:宋体"}

[[Inhibited AVF]{lang="EN-US"}]{#struct_0_x1068_x9952_774997769}

[[当前端口上暂时被抑制的]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_x1068_x9952_x722803672}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[None]{lang="EN-US"}[表示没有]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1695344543 .myid}
[]{#_Toc404797960}[]{#struct_0_x1068_x9952_x1983488085}

**TRILL \-- TRILL配置命令 \-- display trill lsdb**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **lsdb**]{lang="EN-US"}]{#struct_0_x1068_x9952_1820428236}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[链路状态数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x362358731}

[**[display]{lang="EN-US"}**[ **trill** **lsdb** \[ **local** \| **lsp-id** *lsp-id* \| **verbose** \] \*]{lang="EN-US"}]{#struct_0_x1068_x9952_125139982}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_775063305}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x50484080}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2028998171}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_998146628}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_327450052}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x890426132}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1284501668}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1898294745}

[**[local]{lang="EN-US"}**]{#struct_0_x1068_x9952_469655886}[：显示本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[lsp-id]{lang="EN-US"}**[ *lsp-id*]{lang="EN-US"}]{#struct_0_x1068_x9952_774866697}[：显示指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[LSP]{lang="EN-US"}[标识，形式为]{style="font-family:宋体"}[SYSID*.*Pseudonode ID-fragment num]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[SYSID]{lang="EN-US"}[是]{style="font-family:宋体"}[产生该]{style="font-family:宋体"}[LSP]{lang="EN-GB"}[的结点或伪结点的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[，]{style="font-family:宋体"}[fragment num]{lang="EN-US"}[是该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片号。如果未指定本参数，将显示所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1068_x9952_16805254}[：显示详细信息。如果未指定本参数，将显示摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1588309689}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x153794737}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[链路状态数据库的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill lsdb]{lang="EN-US"}]{#struct_0_x1068_x9952_1025581123}

[Flags: \* - Self LSP]{lang="EN-US"}

[LSP ID                 Seq num     Checksum  Holdtime  Length    Overload]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[00a0.fc00.5806.00-00\*  0x00000005  0xd315    361       78        0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_864528342}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[链路状态数据库的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill lsdb verbose]{lang="EN-US"}]{#struct_0_x1068_x9952_774932233}

[LSP ID: 00a0.fc00.5806.00-00\*]{lang="EN-US"}

[Sequence number: 0x00000005]{lang="EN-US"}

[Checksum: 0xd315]{lang="EN-US"}

[Holdtime: 1145s]{lang="EN-US"}

[Length: 78]{lang="EN-US"}

[Overload: 0]{lang="EN-US"}

[Source: 00a0.fc00.5806.00]{lang="EN-US"}

[TRILL version: 0x00]{lang="EN-US"}

[Nickname:]{lang="EN-US"}

[  Nickname: 0xfa1b]{lang="EN-US"}

[  Priority: 64]{lang="EN-US"}

[  Tree-root priority: 32768]{lang="EN-US"}

[Trees:]{lang="EN-US"}

[  Compute trees number: 1]{lang="EN-US"}

[  Max compute trees number: 15]{lang="EN-US"}

[  Used trees number: 1]{lang="EN-US"}

[Tree identifiers:]{lang="EN-US"}

[  0x899b]{lang="EN-US"}

[Trees used identifiers:]{lang="EN-US"}

[  0x899b]{lang="EN-US"}

[Interested VLANs:]{lang="EN-US"}

[  Start: 4, End: 4, M4: 0, M6: 0]{lang="EN-US"}

[  Start: 5, End: 6, M4: 1, M6: 0]{lang="EN-US"}

[Neighbor:]{lang="EN-US"}

[  ID: 00e0.fc58.123a.01, Cost: 2000]{lang="EN-US"}

[Group address:]{lang="EN-US"}

[  VLAN ID: 2]{lang="EN-US"}

[  Group MAC address: 0100-5e01-0101]{lang="EN-US"}

[Gateway information:]{lang="EN-US"}

[  MAC address: 0100-5e01-0001]{lang="EN-US"}

[   VR type: IPv4, VR ID: 2, VR priority: 64]{lang="EN-US"}

[Gateway router capability:]{lang="EN-US"}

[  VR type: IPv4, VR ID: 2]{lang="EN-US"}

[   VLAN ID: 2]{lang="EN-US"}

[    Virtual address:]{lang="EN-US"}

[     192.168.1.1]{lang="EN-US"}

[     192.168.1.2]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display trill lsdb]{lang="EN-US"}]{#struct_0_x1068_x9952_775259913}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x959139872}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x198362303}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_998784142}

[[LSP ID]{lang="EN-US"}]{#struct_0_x1068_x9952_1545538207}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_450291722}[标识，]{style="font-family:宋体"}[\*]{lang="EN-US"}[表示是本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[Seq num/Sequence number]{lang="EN-US"}]{#struct_0_x1068_x9952_x799184016}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1387005940}[的序列号]{style="font-family:宋体"}

[[Checksum]{lang="EN-US"}]{#struct_0_x1068_x9952_775325449}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x967231259}[的校验和]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_x1068_x9952_x1461021384}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x186715508}[的生存剩余时间，单位为秒]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_x1068_x9952_x2131653612}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x192164212}[的长度]{style="font-family:宋体"}

[[Overload]{lang="EN-US"}]{#struct_0_x1068_x9952_774735626}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_249523794}[中]{style="font-family:宋体"}[Overload]{lang="EN-US"}[位的置位情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x1068_x9952_x1092566911}[：表示]{lang="EN-US" style="font-family:宋体"}[未]{style="font-family:宋体"}[置位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1068_x9952_260192579}[：表示]{lang="EN-US" style="font-family:宋体"}[已]{style="font-family:宋体"}[置位]{lang="EN-US" style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_x1068_x9952_2145017119}

[[生成此]{style="font-family:宋体"}]{#struct_0_x1068_x9952_774801162}[LSP]{lang="SV"}[的]{style="font-family:宋体"}[RB]{lang="SV"}[的编号]{style="font-family:
  宋体"}

[[TRILL version]{lang="EN-US"}]{#struct_0_x1068_x9952_1229889256}

[[生成此]{style="font-family:宋体"}]{#struct_0_x1068_x9952_370494542}[LSP]{lang="SV"}[的]{style="font-family:宋体"}[RB]{lang="SV"}[支持的最高版本]{style="font-family:
  宋体"}

[[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_864510309}

[[生成此]{style="font-family:宋体"}]{#struct_0_x1068_x9952_774604554}[LSP]{lang="SV"}[的]{style="font-family:宋体"}[RB]{lang="SV"}[的]{style="font-family:
  宋体"}[Nickname]{lang="EN-US"}[信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_x1744909182}[：]{lang="EN-US" style="font-family:宋体"}[RB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Priority]{lang="EN-US"}]{#struct_0_x1068_x9952_90225797}[：占有]{lang="EN-US" style="font-family:宋体"}[Nickname]{lang="EN-US"}[的优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tree-root priority]{lang="EN-US"}]{#struct_0_x1068_x9952_x216318341}[：作为]{lang="EN-US" style="font-family:
  宋体"}[TRILL]{lang="EN-US"}[分发树根桥的优先级]{lang="EN-US" style="font-family:
  宋体"}

[[Trees]{lang="EN-US"}]{#struct_0_x1068_x9952_199391000}

[[生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_774670090}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树计算信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Compute trees number]{lang="EN-US"}]{#struct_0_x1068_x9952_x138598006}[：希望整网计算的]{lang="EN-US" style="font-family:
  宋体"}[TRILL]{lang="EN-US"}[分发树数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max compute trees number]{lang="EN-US"}]{#struct_0_x1068_x9952_2000783180}[：最多可计算的]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Used trees number]{lang="EN-US"}]{#struct_0_x1068_x9952_x952982873}[：作为]{lang="EN-US" style="font-family:
  宋体"}[Ingress ]{lang="EN-US"}[RB]{lang="EN-US"}[时使用的]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树数量]{lang="EN-US" style="font-family:宋体"}

[[Tree identifiers]{lang="EN-US"}]{#struct_0_x1068_x9952_774997770}

[[生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_1233511473}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[作为根桥优先级最高的]{style="font-family:宋体"}[RB]{lang="EN-US"}[时，要求其它]{style="font-family:宋体"}[RB]{lang="EN-US"}[计算的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树]{style="font-family:宋体"}

[[Trees used identifiers]{lang="EN-US"}]{#struct_0_x1068_x9952_x581066792}

[[生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_752430388}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[作为]{style="font-family:宋体"}[Ingress RB]{lang="EN-US"}[时使用的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树]{style="font-family:宋体"}

[[Interested VLANs]{lang="EN-US"}]{#struct_0_x1068_x9952_775063306}

[[以生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x50484079}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Start]{lang="EN-US"}]{#struct_0_x1068_x9952_x2073628178}[：起始]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[End]{lang="EN-US"}]{#struct_0_x1068_x9952_x1474517072}[：结束]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M4]{lang="EN-US"}]{#struct_0_x1068_x9952_774866698}[：在此]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围内是否存在]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播路由器。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示存在，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示不存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M6]{lang="EN-US"}]{#struct_0_x1068_x9952_16805247}[：在此]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围内是否存在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由器。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示存在，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示不存在]{style="font-family:宋体"}

[[Neighbor]{lang="EN-US"}]{#struct_0_x1068_x9952_815741470}

[[生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_49834954}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[的邻居信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ID]{lang="EN-US"}]{#struct_0_x1068_x9952_774932234}[：邻居的编号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Cost]{lang="EN-US"}]{#struct_0_x1068_x9952_1605714108}[：到达此邻居的开销值]{style="font-family:宋体"}

[[Group address]{lang="EN-US"}]{#struct_0_x1068_x9952_331347444}

[[生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_775259914}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[的组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1068_x9952_x198362304}[：组播]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所]{lang="EN-US" style="font-family:宋体"}[属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_998849678}[：关注的组播]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Gateway information]{lang="EN-US"}]{#struct_0_x1068_x9952_173789858}

[[生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1309558542}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[的网关信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_173986466}[：封装的三层协议报文的实际]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VR type]{lang="EN-US"}]{#struct_0_x1068_x9952_x700431956}[：网络类型]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VR ID]{lang="EN-US"}]{#struct_0_x1068_x9952_173920930}[：]{style="font-family:宋体"}[VR]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VR ]{lang="EN-US"}]{#struct_0_x1068_x9952_1986479513}[p]{lang="EN-US"}[riority]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[竞选主成员]{style="font-family:宋体"}[RB]{lang="EN-US"}[的优先级]{style="font-family:宋体"}

[[Gateway router capability]{lang="EN-US"}]{#struct_0_x1068_x9952_x16562512}

[[生成此]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_173462171}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[的网关路由能力：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VR type]{lang="EN-US"}]{#struct_0_x1068_x9952_358391870}[：网络类型]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VR ID]{lang="EN-US"}]{#struct_0_x1068_x9952_173396635}[：]{style="font-family:宋体"}[VR]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1068_x9952_1285040832}[：虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Virtual ]{lang="EN-US"}]{#struct_0_x1068_x9952_1647736691}[a]{lang="EN-US"}[ddress]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[列表]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1645838662 .myid}
[]{#_Toc404797961}[]{#struct_0_x1068_x9952_1773632964}[]{#_Toc296348982}[]{#_Toc287873945}

**TRILL \-- TRILL配置命令 \-- display trill mfib ingress**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](TRILL命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1068_x9952_1904680436}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1068_x9952_775325450}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **trill** **mfib** **ingress**]{lang="EN-US"}]{#struct_0_x1068_x9952_989083868}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播转发表的入表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1989029283}

[**[display]{lang="EN-US"}**[ **trill** **mfib** **ingress** \[ **vlan** *vlan-id* \[ **local-entry** \| **remote-entry** \] \]]{lang="EN-US"}]{#struct_0_x1068_x9952_40596500}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1976636599}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x990842770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x674284176}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_364434499}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_1781426317}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1357144100}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_774735623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_249523789}

[**[vlan]{lang="EN-US"}**[ ]{lang="EN-US"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x1068_x9952_1246085262}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[local-entry]{lang="EN-US"}**]{#struct_0_x1068_x9952_318957067}[：显示本地的入表项信息。本地入表项是指从该表项中的端口发出的报文无需进行]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[封装。]{style="font-family:宋体"}

[**[remote-entry]{lang="EN-US"}**]{#struct_0_x1068_x9952_x702517420}[：显示远端的入表项信息。远端入表项是指从该表项中的端口发出的报文需要进行]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[封装。]{style="font-family:宋体"}

[[【使用指南】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2089988331}

[[如果未指定]{style="font-family:宋体"}**[local-entry]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1965397452}[和]{style="font-family:宋体"}**[remote-entry]{lang="EN-US"}**[参数，将同时显示本地和远端的入表项信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2142092659}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x694686800}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播转发表所有入表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill mfib ingress]{lang="EN-US"}]{#struct_0_x1068_x9952_x771799805}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Ingress type: Local entry]{lang="EN-US"}

[  VLAN ID: 1]{lang="EN-US"}

[  Ports:]{lang="EN-US"}

[    GE1/0/1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Ingress type: Remote entry]{lang="EN-US"}

[  VLAN ID: 1]{lang="EN-US"}

[  RootNickName: 0x5092]{lang="EN-US"}

[  Ports:]{lang="EN-US"}

[    GE1/0/2]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display trill mfib ingress]{lang="EN-US"}]{#struct_0_x1068_x9952_299140065}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x962676352}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x291746643}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_430903162}

[[Ingress type]{lang="EN-US"}]{#struct_0_x1068_x9952_x670596224}

[[入表项的类型：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_774670087}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local entry]{lang="EN-US"}]{#struct_0_x1068_x9952_1817717127}[：表示本地入]{lang="EN-US" style="font-family:宋体"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote entry]{lang="EN-US"}]{#struct_0_x1068_x9952_x1057130143}[：表示远端入表]{lang="EN-US" style="font-family:宋体"}[项]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1068_x9952_67806898}

[[表项对应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x1864157555}[的编号]{style="font-family:宋体"}

[[RootNickName]{lang="EN-US"}]{#struct_0_x1068_x9952_x574202511}

[[表项对应]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x76944621}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[Ports]{lang="EN-US"}]{#struct_0_x1068_x9952_774997767}

[[表项对应的端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x722803662}

[ ]{lang="EN-US"}

::::: {#-1717650448 .myid}
[]{#_Toc404797962}[]{#struct_0_x1068_x9952_x1983488086}

**TRILL \-- TRILL配置命令 \-- display trill mfib transit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](TRILL命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1068_x9952_x2071254533}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1068_x9952_2049835902}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **trill** **mfib** **transit**]{lang="EN-US"}]{#struct_0_x1068_x9952_662820988}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播转发表的出表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_461778835}

[**[display]{lang="EN-US"}**[ **trill** **mfib** **transit** \[ **nickname** *nickname* \[ **prune-entry** \| **rpf-entry** \| **vlan** *vlan-id* \[ **mac** *mac-address* \] \] \]]{lang="EN-US"}]{#struct_0_x1068_x9952_775063303}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x50484074}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2073628191}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_899053427}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1252017242}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1223232296}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1830693679}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x40773845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_342660698}

[**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}]{#struct_0_x1068_x9952_774866695}[：显示指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数]{style="font-family:宋体"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[prune-entry]{lang="EN-US"}**]{#struct_0_x1068_x9952_16805252}[：显示被剪枝掉的表项的信息。如果未指定本参数，将显示所有表项的信息。]{style="font-family:宋体"}

[**[rpf-entry]{lang="EN-US"}**]{#struct_0_x1068_x9952_1970646713}[：显示]{style="font-family:宋体"}[RPF]{lang="EN-US"}[表项的信息。如果未指定本参数，将显示所有表项的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1068_x9952_575664230}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_x1068_x9952_1905601436}**[：]{style="font-family:宋体"}**[显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的信息，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_258512960}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_2058959442}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播转发表所有出表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill mfib transit]{lang="EN-US"}]{#struct_0_x1068_x9952_774932231}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Transit type: RPF entry]{lang="EN-US"}

[  RootNickName: 0x5092]{lang="EN-US"}

[  InNickName: 0x5092]{lang="EN-US"}

[  Port:]{lang="EN-US"}[ ]{lang="EN-US"}[GE1/0/1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Transit type: RB entry]{lang="EN-US"}

[  RootNickName: 0x5092]{lang="EN-US"}

[  Flag: Egress/Transit]{lang="SV"}

[  Ports:]{lang="SV"}

[    GE1/0/1]{lang="SV"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Transit type: VLAN RB entry]{lang="EN-US"}

[  RootNickName: 0x5092]{lang="EN-US"}

[  VLAN ID: 1]{lang="SV"}

[  Flag: Egress/Transit]{lang="SV"}

[  Ports:]{lang="SV"}

[    GE1/0/1]{lang="SV"}

[[表1-9 ]{lang="EN-US"}[display trill mfib transit]{lang="EN-US"}]{#struct_0_x1068_x9952_1605714103}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x960645024}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_330757620}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1468859651}

[[Transit type]{lang="EN-US"}]{#struct_0_x1068_x9952_775259911}

[[出表项的类型：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x198362301}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RB entry]{lang="EN-US"}]{#struct_0_x1068_x9952_998653070}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RPF entry]{lang="EN-US"}]{#struct_0_x1068_x9952_x2001169161}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[RPF]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN RB entry]{lang="EN-US"}]{#struct_0_x1068_x9952_1905146220}[：]{lang="EN-US" style="font-family:宋体"}[表示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC VLAN RB entry]{lang="EN-US"}]{#struct_0_x1068_x9952_x1696592641}[：]{lang="EN-US" style="font-family:
  宋体"}[表示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[RootNickName]{lang="EN-US"}]{#struct_0_x1068_x9952_775325447}

[[表项对应]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x967231261}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[InNickName]{lang="EN-US"}]{#struct_0_x1068_x9952_x1461545673}

[[表项入口]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1214145654}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1068_x9952_x1746772017}

[[表项对应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x251013664}[的编号]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_774735624}

[[表项对应的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1068_x9952_249523792}[地址]{style="font-family:宋体"}

[[Flag]{lang="SV"}]{#struct_0_x1068_x9952_x1092566909}

[[表项的类型：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_616488475}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Egress]{lang="EN-US"}]{#struct_0_x1068_x9952_x335476296}[：表示]{lang="EN-US" style="font-family:宋体"}[Egress]{lang="EN-US"}[表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_x1068_x9952_774801160}[：表示]{lang="EN-US" style="font-family:宋体"}[Transit]{lang="EN-US"}[表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Egress/Transit]{lang="EN-US"}]{#struct_0_x1068_x9952_1229889258}[：表示既是]{lang="EN-US" style="font-family:宋体"}[Egress]{lang="EN-US"}[表项又是]{lang="EN-US" style="font-family:宋体"}[Transit]{lang="EN-US"}[表项]{lang="EN-US" style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x1068_x9952_370625614}[/Ports]{lang="SV"}

[[表项对应的端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1187576745}

[ ]{lang="EN-US"}

::: {#295424289 .myid}
[]{#_Toc404797963}[]{#struct_0_x1068_x9952_1439600388}

**TRILL \-- TRILL配置命令 \-- display trill multicast-route**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **multicast-route**]{lang="EN-US"}]{#struct_0_x1068_x9952_774604552}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由表信息，即基于组播分发树的组播报文的下一跳出端口列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1744909188}

[**[display]{lang="EN-US"}**[ **trill** **multicast-route** \[ **tree-root** *nickname* \[ **vlan** *vlan-list* \[ **mac-address** *mac-address* \] \] \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x1428803977}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1247018095}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x370269394}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1565202335}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1049269990}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x956801662}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x299139472}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_774670088}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1817717122}

[**[tree-root]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}]{#struct_0_x1068_x9952_x1056933535}[：显示以指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由表信息。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数]{style="font-family:宋体"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由表信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}]{#struct_0_x1068_x9952_722987825}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}[v*lan-list*]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_x1068_x9952_1948172349}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的信息，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1369725573}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1907713415}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由表所有表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill multicast-route]{lang="EN-US"}]{#struct_0_x1068_x9952_774997768}

[Root                          Flag]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0x899b                        Valid]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x722803671}[显示以指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[（]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[为]{style="font-family:宋体"}[0x899B]{lang="EN-US"}[）为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由表信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill multicast-route tree-root 899b]{lang="EN-US"}]{#struct_0_x1068_x9952_x1983553621}

[Root: 0x899b]{lang="EN-US"}

[LocalRcvFlag: True]{lang="EN-US"}

[List of VLANs:]{lang="EN-US"}

[  1 to 10, 13, 40, 60 to 85, 200, 1001]{lang="EN-US"}

[List of outgoing ports (4 in total):]{lang="EN-US"}

[  GE1/0/1]{lang="EN-US"}

[  GE1/0/2]{lang="EN-US"}

[  GE1/0/3]{lang="EN-US"}

[  GE1/0/4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1646063951}[显示]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[内以指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[（]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[为]{style="font-family:宋体"}[0x899B]{lang="EN-US"}[）为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由表信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill multicast-route tree-root 899b vlan 1]{lang="EN-US"}]{#struct_0_x1068_x9952_775063304}

[Root: 0x899b]{lang="EN-US"}

[VLAN: 1]{lang="EN-US"}

[LocalRcvFlag: False]{lang="EN-US"}

[List of outgoing ports (3 in total):]{lang="EN-US"}

[  GE1/0/1]{lang="EN-US"}

[  GE1/0/2]{lang="EN-US"}

[  GE1/0/3]{lang="EN-US"}

[List of IPv4 multicast-router ports (2 in total):]{lang="EN-US"}

[  GE1/0/1]{lang="EN-US"}

[  GE1/0/2]{lang="EN-US"}

[List of IPv6 multicast-router ports (2 in total):]{lang="EN-US"}

[  GE1/0/2]{lang="EN-US"}

[  GE1/0/3]{lang="EN-US"}

[List of MAC addresses (4 in total):]{lang="EN-US"}

[  0000-1111-00ee]{lang="EN-US"}

[  00ff-1111-00ff]{lang="EN-US"}

[  00ef-1111-00ef]{lang="EN-US"}

[  0000-111f-00ff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x50484081}[显示]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[内以指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[（]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[为]{style="font-family:宋体"}[0x899B]{lang="EN-US"}[）为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的、指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址（]{style="font-family:宋体"}[0011-11FF-0022]{lang="EN-US"}[）上的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由表信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill multicast-route tree-root 899b vlan 1 mac-address 0011-11ff-0022]{lang="EN-US"}]{#struct_0_x1068_x9952_774866696}

[Root: ]{lang="NL"}[0x899b]{lang="EN-US"}

[VLAN: 1]{lang="EN-US"}

[MAC address: 0011-11ff-0022]{lang="EN-US"}

[LocalRcvFlag: True]{lang="EN-US"}

[List of outgoing ports (2 in total):]{lang="EN-US"}

[  GE1/0/3]{lang="EN-US"}

[  GE1/0/4]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display trill multicast-route]{lang="EN-US"}]{#struct_0_x1068_x9952_16805253}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x968338656}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_14331577}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x435837042}

[[Root]{lang="NL"}]{#struct_0_x1068_x9952_1907066178}

[[作为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_147918117}[分发树根桥的]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname ]{lang="NL"}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_1018478672}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_774932232}[的编号]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_1605714106}

[[MAC]{lang="EN-US"}]{#struct_0_x1068_x9952_330429940}[地址]{style="font-family:宋体"}

[[Flag]{lang="NL"}]{#struct_0_x1068_x9952_x830196583}

[[根桥是否有效：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1406662866}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_x1068_x9952_1579956844}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}[alid]{lang="EN-US"}]{#struct_0_x1068_x9952_775259912}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[有效]{lang="EN-US" style="font-family:宋体"}

[[LocalRcvFlag]{lang="EN-US"}]{#struct_0_x1068_x9952_x198362302}

[[本地接收标识，即是否需要进行本地转发：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_998718606}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_x1068_x9952_770080403}[：表示不需要进行本地转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[True]{lang="EN-US"}]{#struct_0_x1068_x9952_1139006934}[：表示需要进行本地转发]{style="font-family:宋体"}

[[List of outgoing ports (4 in total)]{lang="EN-US"}]{#struct_0_x1068_x9952_775325448}

[[出端口列表及其总数，]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_x1068_x9952_x967231260}[表示没有]{style="font-family:宋体"}

[[List of VLANs (2 in total)]{lang="EN-US"}]{#struct_0_x1068_x9952_x1461480137}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_73238497}[列表及其总数，]{style="font-family:宋体"}[None]{lang="EN-US"}[表示没有]{style="font-family:宋体"}

[[List of IPv4 multicast-router ports (2 in total)]{lang="EN-US"}]{#struct_0_x1068_x9952_939932888}

[[IPv4]{lang="EN-US"}]{#struct_0_x1068_x9952_774735621}[组播路由器的端口列表及其总数]{style="font-family:宋体"}

[[List of IPv6 multicast-router ports (2 in total)]{lang="EN-US"}]{#struct_0_x1068_x9952_249523787}

[[IPv6]{lang="EN-US"}]{#struct_0_x1068_x9952_1246085248}[组播路由器的端口列表及其总数]{style="font-family:宋体"}

[[List of MAC addresses (4 in total)]{lang="EN-US"}]{#struct_0_x1068_x9952_319350281}

[[MAC]{lang="EN-US"}]{#struct_0_x1068_x9952_1459447643}[地址列表及其总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1521198473 .myid}
[]{#_Toc404797964}[]{#struct_0_x1068_x9952_774801157}

**TRILL \-- TRILL配置命令 \-- display trill neighbor-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **neighbor-table**]{lang="EN-US"}]{#struct_0_x1068_x9952_x344088851}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻居表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2117421763}

[**[display]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[neighbor-table]{lang="EN-US"}**]{#struct_0_x1068_x9952_x126290645}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_889323698}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2139202634}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1937320671}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1428327068}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_774604549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_211405959}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_1801005274}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1876126454}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1164374159}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻居表信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill neighbor-table]{lang="EN-US"}]{#struct_0_x1068_x9952_x707582376}

[Total number of nexthops: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[NextHop   MAC address       Interface]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0x899b    00e0-fc58-123a    GE1/0/1]{lang="EN-US"}

[[表1-11 ]{lang="DE"}[display trill neighbor-table]{lang="DE"}]{#struct_0_x1068_x9952_832243729}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x971184288}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1026283619}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_774670085}

[[Total number of nexthops]{lang="EN-US"}]{#struct_0_x1068_x9952_231896024}

[[下一跳的总数]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1426257751}

[[NextHop]{lang="EN-US"}]{#struct_0_x1068_x9952_1817717125}

[[下一跳的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_x1057261215}

[[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_x735548848}

[[下一跳的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1068_x9952_x23492785}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_x255883996}

[[出端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_774997765}

[ ]{lang="EN-US"}

::: {#-631074906 .myid}
[]{#_Toc404797965}[]{#struct_0_x1068_x9952_x722803660}

**TRILL \-- TRILL配置命令 \-- display trill peer**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **peer**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1983619158}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻居统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1388138979}

[**[display]{lang="EN-US"}**[ **trill** **peer** \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x2030710146}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x750513977}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_762156189}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_737381992}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x2052652268}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_775063301}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x50484076}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x2073628189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1255349323}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1068_x9952_1328108915}[：显示指定端口上的信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为端口类型和端口编号。如果未指定本参数，将显示所有端口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_150722714}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_2100855296}[显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻居统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill peer interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1068_x9952_774866693}

[System ID: 00e0.fc58.123a]{lang="EN-US"}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Circuit ID: 00e0.fc58.123a.01]{lang="EN-US"}

[State: Up]{lang="EN-US"}

[Holdtime: 8s]{lang="EN-US"}

[DRB priority: 64]{lang="EN-US"}

[Nickname: 0x899b]{lang="EN-US"}

[Uptime: 00:38:15]{lang="EN-US"}

[]{#struct_0_x1068_x9952_16805258}[[表1-12 ]{lang="EN-US"}[display trill peer]{lang="EN-US"}]{#_Toc283318653}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x969465472}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_823635641}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_729040334}

[[System ID]{lang="EN-US"}]{#struct_0_x1068_x9952_1231478894}

[[邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_x1068_x9952_x61752970}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_774932229}

[[与邻居直连的本地]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x350601025}[端口]{style="font-family:宋体"}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x1068_x9952_1407745582}

[[伪节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1578866040}[编号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1068_x9952_x843445801}

[[邻居状态，包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x1068_x9952_x695553155}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Holdtime]{lang="EN-US"}]{#struct_0_x1068_x9952_775259909}

[[邻接关系保持时间，单位为秒。如果在该时间内未收到邻居发来的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_1757952827}[报文，则认为与该邻居的邻接关系已失效；如果收到了，则重置此时间]{style="font-family:宋体"}

[[DRB priority]{lang="EN-US"}]{#struct_0_x1068_x9952_1496398517}

[[邻居端口的]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x2031111175}[优先级]{style="font-family:宋体"}

[[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_x1015648517}

[[邻居的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_775325445}

[[Uptime]{lang="EN-US"}]{#struct_0_x1068_x9952_x967231263}

[[与该邻居的邻接关系已保持的时间]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1461676745}

[ ]{lang="EN-US"}

::: {#-382489365 .myid}
[]{#_Toc404797966}[]{#struct_0_x1068_x9952_x671488028}

**TRILL \-- TRILL配置命令 \-- display trill rpf-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **rpf-table**]{lang="EN-US"}]{#struct_0_x1068_x9952_x113025624}[命令用来显示]{style="font-family:宋体"}[TRILL RPF]{lang="EN-US"}[检查表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1583624076}

[**[display]{lang="EN-US"}**[ **trill** **rpf-table** **tree-root** *nickname*]{lang="EN-US"}]{#struct_0_x1068_x9952_600656278}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_774735622}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_249523790}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1092566907}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1066827169}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x627997945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1070697757}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_1843297223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x680854257}

[**[tree-root]{lang="EN-US"}**[ ]{lang="EN-US"}*[nickname]{lang="EN-US"}*]{#struct_0_x1068_x9952_774801158}[：显示以指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的信息。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x344088846}

[[TRILL RPF]{lang="EN-US"}]{#struct_0_x1068_x9952_x2117094082}[（]{style="font-family:宋体"}[Reverse Path Forwarding]{lang="EN-US"}[，逆向路径转发）检查表用来检查组播报文的入端口是否合法。即根据报文中]{style="font-family:宋体"}[Egress RB]{lang="EN-US"}[（即该报文所属]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的根桥）和]{style="font-family:宋体"}[Ingress RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，检查报文的实际入端口与]{style="font-family:宋体"}[RPF]{lang="EN-US"}[表项中的入端口是否一致，如不一致则认为该报文非法并将其丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x865865948}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1597663435}[显示以指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[（]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[为]{style="font-family:宋体"}[0x899B]{lang="EN-US"}[）为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的]{style="font-family:宋体"}[TRILL RPF]{lang="EN-US"}[检查表信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill rpf-table tree-root 899b]{lang="EN-US"}]{#struct_0_x1068_x9952_x238749032}

[Ingress-nickname           Expected-rcv-ports]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0x1fff                     GE1/0/1]{lang="EN-US"}

[0x1ff0                     GE1/0/2]{lang="EN-US"}

[0x0ffe                     GE1/0/3]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display trill rpf-table]{lang="EN-US"}]{#struct_0_x1068_x9952_x646311178}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x943123616}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_774604550}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1744909186}

[[Ingress-nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_2059594265}

[[Ingress RB]{lang="EN-US"}]{#struct_0_x1068_x9952_416499273}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[Expected-rcv-ports]{lang="EN-US"}]{#struct_0_x1068_x9952_x1500436809}

[[期望的入端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x58129734}

[ ]{lang="EN-US"}

::: {#-1862794404 .myid}
[]{#_Toc404797967}[]{#struct_0_x1068_x9952_986497543}[]{#_Toc386113380}[]{#_Toc385854378}[]{#_Toc379615176}

**TRILL \-- TRILL配置命令 \-- display trill topology**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **topology**]{lang="EN-US"}]{#struct_0_x1068_x9952_1155119555}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络的拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x579586398}

[**[display]{lang="EN-US"}**[ **trill** **topology** \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x1185300984}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_669177004}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x614450660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1254806178}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x563582868}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1226569120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_343711124}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1334143005}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_685783079}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1068_x9952_x2145670339}[：显示详细信息。如果未指定本参数，将显示摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_592250374}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1281851670}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络拓扑的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill topology]{lang="EN-US"}]{#struct_0_x1068_x9952_690940682}

[                         TRILL topology information]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Flags: O-Node is overloaded          R-Node is directly reachable]{lang="EN-US"}

[           D-Node or link is to be deleted]{lang="EN-US"}

[ ]{lang="EN-US"}

[SPF node          Node flag    SPF link               Link cost  Link flag]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0011.2200.0201.00 -/-/-]{lang="EN-US"}

[                               \--\>0011.2200.0301.01   20000      -]{lang="EN-US"}

[0011.2200.0301.01 -/R/-]{lang="EN-US"}

[                               \--\>0011.2200.0201.00   0          -]{lang="EN-US"}

[                               \--\>0011.2200.0301.00   0          -]{lang="EN-US"}

[0011.2200.0301.00 -/-/-]{lang="EN-US"}

[                               \--\>0011.2200.0301.01   20000      -]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_325971737}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络拓扑的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill topology verbose]{lang="EN-US"}]{#struct_0_x1068_x9952_x1339101285}

[                         TRILL topology information]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Flags: O-Node is overloaded          R-Node is directly reachable]{lang="EN-US"}

[           D-Node or link is to be deleted]{lang="EN-US"}

[ ]{lang="EN-US"}

[SPF node: 0011.2200.0201.00]{lang="EN-US"}

[  Node flag: -/-/-]{lang="EN-US"}

[  SPF links count: 1]{lang="EN-US"}

[  \--\>0011.2200.0301.01]{lang="EN-US"}

[    Link cost: 20000]{lang="EN-US"}

[    Link flag: -]{lang="EN-US"}

[    Link sources: 1]{lang="EN-US"}

[     Link source 1]{lang="EN-US"}

[       Type: Adjacent       Interface: N/A]{lang="EN-US"}

[       Cost: 20000          NextHop: N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[SPF node: 0011.2200.0301.01]{lang="EN-US"}

[  Node flag: -/R/-]{lang="EN-US"}

[  SPF links: 2]{lang="EN-US"}

[  \--\>0011.2200.0201.00]{lang="EN-US"}

[    Link cost: 0]{lang="EN-US"}

[    Link flag: -]{lang="EN-US"}

[    Link sources count: 1]{lang="EN-US"}

[     Link source 1]{lang="EN-US"}

[       Type: Remote         Interface: N/A]{lang="EN-US"}

[       Cost: 0              NextHop: N/A]{lang="EN-US"}

[  \--\>0011.2200.0301.00]{lang="EN-US"}

[    Link cost: 0]{lang="EN-US"}

[    Link flag: -]{lang="EN-US"}

[    Link sources: 1]{lang="EN-US"}

[     Link source 1]{lang="EN-US"}

[       Type: Remote         Interface: GE1/0/1]{lang="EN-US"}

[       Cost: 0              NextHop: 0x0002]{lang="EN-US"}

[ ]{lang="EN-US"}

[SPF node: 0011.2200.0301.00]{lang="EN-US"}

[  Node flag: -/-/-]{lang="EN-US"}

[  SPF links: 1]{lang="EN-US"}

[  \--\>0011.2200.0301.01]{lang="EN-US"}

[    Link cost: 20000]{lang="EN-US"}

[    Link flag: -]{lang="EN-US"}

[    Link sources: 1]{lang="EN-US"}

[     Link source 1]{lang="EN-US"}

[       Type: Remote         Interface: N/A]{lang="EN-US"}

[       Cost: 20000          NextHop: N/A]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display trill topology]{lang="EN-US"}]{#struct_0_x1068_x9952_209059150}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1028566813}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2139543476}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_112033113}

[[SPF node]{lang="EN-US"}]{#struct_0_x1068_x9952_1389782070}

[[拓扑节点的编号]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1633382942}

[[Node flag]{lang="EN-US"}]{#struct_0_x1068_x9952_x1979604657}

[[节点的状态标记：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x176301871}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x1068_x9952_541887882}[：]{style="font-family:宋体"}[OverLoad]{lang="EN-US"}[状态，表示节点当前不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1068_x9952_x531589229}[：表示节点是直连节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1068_x9952_x2098616172}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[节点待删除]{lang="EN-US" style="font-family:宋体"}

[[SPF link]{lang="EN-US"}]{#struct_0_x1068_x9952_599647387}

[[拓扑链路]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1022629279}

[[SPF links]{lang="EN-US"}]{#struct_0_x1068_x9952_630267183}

[[拓扑链路的个数]{style="font-family:宋体"}]{#struct_0_x1068_x9952_568359385}

[[Link cost]{lang="EN-US"}]{#struct_0_x1068_x9952_x1742320276}

[[拓扑链路的开销]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1464391936}

[[Link flag]{lang="EN-US"}]{#struct_0_x1068_x9952_x1479084790}

[[链路状态标记，]{style="font-family:宋体"}[D]{lang="EN-US"}]{#struct_0_x1068_x9952_986563079}[表示链路待删除]{style="font-family:宋体"}

[[Link sources]{lang="EN-US"}]{#struct_0_x1068_x9952_x768052951}

[[链路发布源的个数]{style="font-family:宋体"}]{#struct_0_x1068_x9952_93850002}

[[Link source 1]{lang="EN-US"}]{#struct_0_x1068_x9952_x579520862}

[[ ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1159462299}[链路发布源的相关信息]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1068_x9952_x2145604803}

[[链路发布源的类型：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1286943356}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adjacent]{lang="EN-US"}]{#struct_0_x1068_x9952_x1642266187}[：表示由本地邻居维护产生]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote]{lang="EN-US"}]{#struct_0_x1068_x9952_227048192}[：]{lang="EN-US" style="font-family:宋体"}[表示由]{style="font-family:宋体"}[其它节点]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[产生]{lang="EN-US" style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x1068_x9952_2123740273}

[[链路发布源的开销]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x376821947}

[ ]{lang="EN-US"}

::: {#-650599762 .myid}
[]{#_Toc404797968}[]{#struct_0_x1068_x9952_774670086}

**TRILL \-- TRILL配置命令 \-- display trill unicast-route**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **unicast-route**]{lang="EN-US"}]{#struct_0_x1068_x9952_1817717128}[命令用来显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[单播路由表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1056540319}

[**[display]{lang="EN-US"}**[ **trill** **unicast-route** \[ **nickname** *nickname* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1068_x9952_441910044}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1890643901}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_719190682}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x777705144}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1881317258}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1393600231}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_774997766}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x722803661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1983553622}

[**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}]{#struct_0_x1068_x9952_x2049348478}[：显示指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数]{style="font-family:宋体"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1068_x9952_332143112}[：显示详细信息。如果未指定本参数，将显示摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x15687557}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1173378045}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[单播路由表所有表项的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill unicast-route]{lang="EN-US"}]{#struct_0_x1068_x9952_775063302}

[Destinations: 2        Unicast routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination    Interface                NextHop]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0xfa1b         N/A                      N/A]{lang="EN-US"}

[0x899b         GE1/0/1                  Direct]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x50484075}[显示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[单播路由表所有表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill unicast-route verbose]{lang="EN-US"}]{#struct_0_x1068_x9952_x2073628190}

[Destinations: 2        Unicast routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination: 0xfa1b]{lang="EN-US"}

[NextHop count: 0             Neighbor ID: 0x0000]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination: 0x899b]{lang="EN-US"}

[NextHop count: 1             Neighbor ID: 0x0101]{lang="EN-US"}

[Interface: GE1/0/1           NextHop: Direct]{lang="EN-US"}

[]{#struct_0_x1068_x9952_x1829829928}[]{#_Toc266110051}[[表1-15 ]{lang="EN-US"}[display trill unicast-route]{lang="EN-US"}]{#_Toc265237222}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x939784608}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x918525733}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1056493490}

[[Destinations]{lang="EN-US"}]{#struct_0_x1068_x9952_x1287199286}

[[目的]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_325469251}[的数量]{style="font-family:宋体"}

[[Unicast routes]{lang="EN-US"}]{#struct_0_x1068_x9952_1797914429}

[[单播路由的条数]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1522149875}

[[Destination]{lang="EN-US"}]{#struct_0_x1068_x9952_86409735}

[[目的]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_774866694}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_16805251}

[[出端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_396668601}

[[NextHop]{lang="EN-US"}]{#struct_0_x1068_x9952_x1089534163}

[[下一跳的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_1729436559}

[[NextHop count]{lang="EN-US"}]{#struct_0_x1068_x9952_738282018}

[[下一跳的数量]{style="font-family:宋体"}]{#struct_0_x1068_x9952_774932230}

[[Neighbor ID]{lang="EN-US"}]{#struct_0_x1068_x9952_1605714104}

[[下一跳关联的邻居编号]{style="font-family:宋体"}]{#struct_0_x1068_x9952_330561012}

[ ]{lang="EN-US"}

::: {#1961216506 .myid}
[]{#_Toc404797969}[]{#struct_0_x1068_x9952_x1754684829}[]{#_Toc350777172}[]{#_Toc350774928}

**TRILL \-- TRILL配置命令 \-- display trill vr**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **vr**]{lang="EN-US"}]{#struct_0_x1068_x9952_x938461096}[命令用来显示]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Router]{lang="EN-US"}[，虚拟路由器）的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x569545217}

[**[display]{lang="EN-US"}**[ **trill** **vr** \[ **ipv6** \] \[ **verbose** \[ **vrid** *vr-id* \[ **interface** *interface-type interface-number* \] \] \| **vrid** *vr-id* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_1448437802}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1754619293}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_337626243}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2003954310}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1948586788}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x233272489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755209116}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_891248279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2125935885}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x1068_x9952_x845887427}[：显示]{style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[的信息。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1068_x9952_727435981}[：显示详细信息。如果未指定本参数，将显示摘要信息。]{style="font-family:宋体"}

[**[vrid]{lang="EN-US"}**[ *vr-id*]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755143580}[：显示指定]{style="font-family:宋体"}[VR]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vr-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VR]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1068_x9952_119022045}[：]{style="font-family:宋体"}[显示指定端口上的信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为端口类型和端口编号。如果未指定本参数，将显示所有端口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1955505934}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1347434513}[显示所有]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill vr]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755078044}

[VRID    Partner RB         State       Local]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[1       0606.0606.0606     Backup      Y]{lang="EN-US"}

[        0808.0808.0808     Master      N]{lang="EN-US"}

[2       0606.0606.0606     Backup      Y]{lang="EN-US"}

[        0808.0808.0808     Master      N]{lang="EN-US"}

[3       0606.0606.0606     Backup      Y]{lang="EN-US"}

[        0808.0808.0808     Master      N]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_665769343}[显示所有]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill vr verbose]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755012508}

[IPv4 virtual router information:]{lang="EN-US"}

[  VRID: 1     Virtual MAC: 0cda-41ed-be01]{lang="EN-US"}

[    Partner RB information:]{lang="EN-US"}

[      System ID: 0606.0606.0606]{lang="EN-US"}

[        State: Backup]{lang="EN-US"}

[        Local: Y]{lang="EN-US"}

[      System ID: 0808.0808.0808]{lang="EN-US"}

[        State: Master]{lang="EN-US"}

[        Local: N]{lang="EN-US"}

[    Interface information:]{lang="EN-US"}

[      Interface: Vlan-interface10]{lang="EN-US"}

[        Virtual IP: 193.1.1.1]{lang="EN-US"}

[        Track index: 11     State: Positive]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display trill vr]{lang="EN-US"}]{#struct_0_x1068_x9952_x1083326018}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1694016569}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1754946972}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1754881436}

[[VRID]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754815900}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754750364}[的编号]{style="font-family:宋体"}

[[Partner RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754684828}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754619292}[中成员]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755209115}

[[该成员]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755143579}[在]{style="font-family:宋体"}[VR]{lang="EN-US"}[中的状态，包括]{style="font-family:宋体"}[Master]{lang="EN-US"}[、]{style="font-family:宋体"}[Backup]{lang="EN-US"}[和]{style="font-family:宋体"}[Inactive]{lang="EN-US"}[三种]{style="font-family:宋体"}

[[Local]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755078043}

[[该成员]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755012507}[是否为当前设备：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754946971}[：表示是当前设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754881435}[：表示不是当前设备]{style="font-family:宋体"}

[[IPv4 virtual router information]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754815899}

[[IPv4 TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_1494955643}[的信息]{style="font-family:宋体"}

[[IPv6 virtual router information]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754750363}

[[IPv6 TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754684827}[的信息]{style="font-family:宋体"}

[[Virtual MAC]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754619291}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755209122}[的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Partner RB information]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755143586}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755078050}[中成员]{style="font-family:宋体"}[RB]{lang="EN-US"}[的信息]{style="font-family:宋体"}

[[System ID]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755012514}

[[该成员]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754946978}[的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[Interface information]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754881442}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754815906}[所在接口的信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754750370}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1754684834}

[[Virtual IP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754619298}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755209121}[的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Track index]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755143585}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755078049}[监测的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项（配置了]{style="font-family:宋体"}**[trill]{lang="EN-US"}**[ **vr** **vrid** **track**]{lang="EN-US"}[命令后，才会显示此项）]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1068_x9952_x1755012513}

[[Track]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754946977}[项的状态（配置了]{style="font-family:宋体"}**[trill]{lang="EN-US"}**[ **vr** **vrid** **track**]{lang="EN-US"}[命令后，才会显示此项）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Negative]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754881441}[：表示无效状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Positive]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754815905}[：表示有效状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NotReady]{lang="EN-US"}]{#struct_0_x1068_x9952_x1754750369}[：表示尚未就绪状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#140771917 .myid}
[]{#_Toc404797970}[]{#struct_0_x1068_x9952_x1754684833}[]{#_Toc374084876}

**TRILL \-- TRILL配置命令 \-- display trill vr-adjacent-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1068_x9952_x131826506}**[trill]{lang="EN-US"}**[ **vr-**]{lang="EN-US"}**[adjacent-table]{lang="EN-US"}**[命令用来显示]{style="font-family:宋体"}[TRILL VR]{lang="PT-BR"}[邻接表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1083439585}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1068_x9952_x441760071}**[trill]{lang="EN-US"}**[ **vr-**]{lang="EN-US"}**[adjacent-table]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[count]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x607317648}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1754619297}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1987972585}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x2138783702}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1780416943}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_710710103}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x189125177}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1885435031}

[**[count]{lang="EN-US"}**]{#struct_0_x1068_x9952_1699177212}[：显示表项的数量。]{style="font-family:宋体"}

[**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}[ **interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1068_x9952_x397685465}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[RB]{lang="EN-US"}[指定端口上的信息。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数]{style="font-family:宋体"}[；]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[RB]{lang="EN-US"}[所有端口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x932346822}

[]{#_Toc341712884}[]{#_Toc138044435}[]{#_Toc89146412}[]{#_Toc85625889}[]{#_Toc81455776}[]{#_Toc74708566}[]{#_Toc72635551}[]{#_Toc66068431}[]{#_Toc60132630}[]{#_Toc54665893}[]{#_Toc38708889}[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1669203714}[显示]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[邻接表所有表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill vr-adjacent-table]{lang="EN-US"}]{#struct_0_x1068_x9952_x189059641}

[NextHop     MAC address       Interface]{lang="EN-US"}

[0x899b      00e0-fc58-123a    GE1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1664684997}[显示]{style="font-family:宋体"}[TRILL VR]{lang="FR"}[邻接表的表项数量。]{style="font-family:宋体"}

[[\<Sysname\> display trill vr-adjacent-table count]{lang="EN-US"}]{#struct_0_x1068_x9952_1826039294}

[Total number of TRILL VR ADJ entries: 3]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display trill ]{lang="EN-US"}]{#struct_0_x1068_x9952_x354202294}[vr-]{lang="EN-US"}[adjacent-table]{lang="FR"}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1704822109}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x188994105}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x188928569}

[[NextHop]{lang="EN-US"}]{#struct_0_x1068_x9952_x188863033}

[[报文转发下一跳]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x188797497}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_x188731961}

[[报文转发下一跳]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x188666425}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_x188600889}

[[报文的出端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x188535353}

[[Total number of TRILL VR ADJ entries]{lang="EN-US"}]{#struct_0_x1068_x9952_x189125176}

[[TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x189059640}[邻接表的表项数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1773648410 .myid}
[]{#_Toc404797971}[]{#struct_0_x1068_x9952_x188994104}[]{#_Toc374084877}

**TRILL \-- TRILL配置命令 \-- display trill vr-fib**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1068_x9952_x748677189}**[trill]{lang="EN-US"}**[ **vr-fib**]{lang="EN-US"}[命令用来显示]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[单播转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1214630544}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1068_x9952_x38271777}**[trill]{lang="EN-US"}**[ **vr-fib** ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[count]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[mac]{lang="EN-US"}**[ *mac-address* **vlan** *vlan-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x823221539}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x188928568}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_126984305}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_235188376}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1712801347}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x694919664}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_715001108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x188863032}

[**[count]{lang="EN-US"}**]{#struct_0_x1068_x9952_467325140}[：显示表项的数量。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1421431894}[ *mac-address* **vlan** *vlan-id*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x708072283}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1344338113}[显示]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[单播转发表所有表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill vr-fib]{lang="EN-US"}]{#struct_0_x1068_x9952_x188797496}

[MAC ]{lang="EN-US"}[address]{lang="EN-US"}[    VLAN NextHop   Interface]{lang="EN-US"}

[0cad-41ed-be01 1    0x2a5c    GE1/0/1]{lang="EN-US"}

[0cad-41ed-bf01 2    0x2a5c    GE1/0/2]{lang="EN-US"}

[[\# ]{lang="DE"}]{#struct_0_x1068_x9952_2009178855}[显示]{style="font-family:宋体"}[TRILL VR]{lang="DE"}[单播转发表的表项数量。]{style="font-family:宋体"}

[[\<Sysname\> display trill vr-fib count]{lang="EN-US"}]{#struct_0_x1068_x9952_x784614437}

[Total number of TRILL VR FIB destinations: 2]{lang="EN-US"}

[Total number of TRILL VR FIB entries: 2]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display trill vr-fib]{lang="EN-US"}]{#struct_0_x1068_x9952_695342998}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1725239347}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x188731960}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x188666424}

[[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_x188600888}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1068_x9952_x188535352}[地址]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x189125175}

[[转发的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x189059639}[编号]{style="font-family:宋体"}

[[NextHop]{lang="EN-US"}]{#struct_0_x1068_x9952_x188994103}

[[下一跳]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x188928567}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x1068_x9952_x188863031}

[[报文的出端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x188797495}

[[Total number of TRILL VR FIB destinations]{lang="EN-US"}]{#struct_0_x1068_x9952_x188731959}

[[TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x188666423}[单播转发表中目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数量]{style="font-family:宋体"}

[[Total number of TRILL VR FIB entries]{lang="EN-US"}]{#struct_0_x1068_x9952_x188600887}

[[TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x188535351}[单播转发表的表项数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#89449881 .myid}
[]{#_Toc404797972}[]{#struct_0_x1068_x9952_1619168215}

**TRILL \-- TRILL配置命令 \-- display trill vr-route**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **trill** **vr-route**]{lang="EN-US"}]{#struct_0_x1068_x9952_x189125174}[命令用来显示]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1885631639}

[**[display]{lang="EN-US"}**[ **trill** **vr-route** \[ **vrid** *vrid* \] \[ **vlan** *vlan-id* \] \[ **mac-address** *mac-address* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_811974182}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1522838030}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x701048910}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_375100758}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x189059638}

[[network-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_1665274826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_305997431}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1068_x9952_x1916581635}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x176191375}

[**[vrid]{lang="EN-US"}**[ *vr-id*]{lang="EN-US"}]{#struct_0_x1068_x9952_x188994102}[：显示指定]{style="font-family:宋体"}[VR]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vr-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[的编号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VR]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ ]{lang="EN-US"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x1068_x9952_x748808261}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_x1068_x9952_x372722009}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的信息，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_985852888}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x319821978}[显示]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表所有表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display trill vr-route]{lang="EN-US"}]{#struct_0_x1068_x9952_x188928566}

[VRID    MAC address     VLAN    Port]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[1       0cda-41ed-be01  1       GE1/0/1]{lang="EN-US"}

[                        2       GE1/0/3]{lang="EN-US"}

[                        3       GE1/0/4]{lang="EN-US"}

[2       0cda-41ed-be02  1       GE1/0/2]{lang="EN-US"}

[                        3       GE1/0/5]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display trill vr-route]{lang="EN-US"}]{#struct_0_x1068_x9952_127377521}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1712453237}[[字段]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x188863030}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x188797494}

[[VRID]{lang="EN-US"}]{#struct_0_x1068_x9952_x188731958}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x188666422}[的编号]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1068_x9952_x188600886}

[[VR]{lang="EN-US"}]{#struct_0_x1068_x9952_x188535350}[的虚拟]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x189125181}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x189059645}[的编号]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x1068_x9952_x188994109}

[[出端口]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x188928573}

[ ]{lang="EN-US"}

::: {#1202717567 .myid}
[]{#_Toc404797973}[]{#struct_0_x1068_x9952_630398255}[]{#_Toc386113382}[]{#_Toc385854380}[]{#_Toc379615170}[]{#_Toc379555238}[]{#_Toc378607610}

**TRILL \-- TRILL配置命令 \-- flash-flood**

------------------------------------------------------------------------

[**[flash-flood]{lang="EN-US"}**]{#struct_0_x1068_x9952_1691557337}[命令用来开启]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **flash-flood**]{lang="EN-US"}]{#struct_0_x1068_x9952_152947877}[命令用来关闭]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1494689742}

[**[flash-flood]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **flood-count** *flooding-count* \| **max-timer-interval** *flooding-interval* \] \*]{lang="EN-US"}]{#struct_0_x1068_x9952_637116210}

[**[undo]{lang="EN-US"}**[ **flash-flood**]{lang="EN-US"}]{#struct_0_x1068_x9952_x831651753}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_598634045}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x438016362}[快速扩散功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1911228297}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1340912276}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x786032603}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x2147263793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x287238889}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_333356904}

[**[flood-count]{lang="EN-US"}**[ *flooding-count*]{lang="EN-US"}]{#struct_0_x1068_x9952_x1196016329}[：表示]{style="font-family:宋体"}[扩散次]{style="font-family:宋体"}[数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[max-timer-interval]{lang="EN-US"}**[ *flooding-interval*]{lang="EN-US"}]{#struct_0_x1068_x9952_x309201297}[：]{style="font-family:宋体"}[表示开始进行]{style="font-family:宋体"}[扩散的延迟时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[毫秒（表示立即扩散）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_104162642}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x291665936}[的变化会导致重新计算]{style="font-family:宋体"}[SPF]{lang="EN-US"}[。开启本功能后，设备会将导致]{style="font-family:宋体"}[SPF]{lang="EN-US"}[重新计算的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散出去，从而有效缩短拓扑变化时全网设备上]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[不一致的时间，提高全网的快速收敛性能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x322010059}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x918421393}[开启]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能，并配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散的个数为]{style="font-family:宋体"}[10]{lang="EN-US"}[个、延迟时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1387971079}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] flash-flood flood-count 10 max-timer-interval 10]{lang="EN-US"}
:::

::: {#285548656 .myid}
[]{#_Toc404797974}[]{#struct_0_x1068_x9952_1674898153}[]{#_Toc386113383}[]{#_Toc385854381}[]{#_Toc379615173}

**TRILL \-- TRILL配置命令 \-- flush-policy difference**

------------------------------------------------------------------------

[**[flush-policy]{lang="EN-US"}**[ **difference**]{lang="EN-US"}]{#struct_0_x1068_x9952_1984007979}[命令用来配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由采用差异化下刷策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **flush-policy** **difference**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1058351800}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_924869217}

[**[flush-policy]{lang="EN-US"}**[ **difference**]{lang="EN-US"}]{#struct_0_x1068_x9952_1306163199}

[**[undo]{lang="EN-US"}**[ **flush-policy** **difference**]{lang="EN-US"}]{#struct_0_x1068_x9952_x480989399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1733104923}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1008450927}[组播路由未采用差异化下刷策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1350978454}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x178112862}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x505877716}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1309323337}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1580653553}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x631752923}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1866675223}[组播路由表项分为]{style="font-family:宋体"}[RB]{lang="EN-US"}[表项、]{style="font-family:宋体"}[RB]{lang="EN-US"}[＋]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[表项和]{style="font-family:宋体"}[RB]{lang="EN-US"}[＋]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[＋]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项三级。在特定的组网和配置下，如果]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由相关的下级表项与上一级表项完全相同，此时只需下刷上一级表项便可正确指导转发，这便是差异化下刷策略，即仅当下级表项与上一级表项不同时才下刷。]{style="font-family:宋体"}

[[例如：若一棵]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1184930686}[分发树的]{style="font-family:宋体"}[RB]{lang="EN-US"}[表项、]{style="font-family:宋体"}[RB]{lang="EN-US"}[＋]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[表项和]{style="font-family:宋体"}[RB]{lang="EN-US"}[＋]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[＋]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项均相同，则只需下刷]{style="font-family:宋体"}[RB]{lang="EN-US"}[表项即可，]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[数据报文可以直接查找]{style="font-family:宋体"}[RB]{lang="EN-US"}[表项进行转发。]{style="font-family:宋体"}

[[需要注意的是，本命令只能应用在]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1179607239}[表项、]{style="font-family:宋体"}[RB]{lang="EN-US"}[＋]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[表项和]{style="font-family:宋体"}[RB]{lang="EN-US"}[＋]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[＋]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项的出端口和本地标识都相同的特殊组网中，否则将导致大量表项同一时间集中下刷而使性能下降。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1832275049}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_474926682}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播路由采用差异化下刷策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1744196803}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] flush-policy difference]{lang="EN-US"}
:::

::: {#63544256 .myid}
[]{#_Toc404797975}[]{#struct_0_x1068_x9952_x1922360404}[]{#_Toc326062199}

**TRILL \-- TRILL配置命令 \-- graceful-restart**

------------------------------------------------------------------------

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1067027406}[命令用来使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_x1068_x9952_1270618657}[命令用来关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_775259910}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1068_x9952_x198362300}

[**[undo ]{lang="EN-US"}[graceful-restart]{lang="EN-US"}**]{#struct_0_x1068_x9952_998587534}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1881088755}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_585012692}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1990961078}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_229066336}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1227157151}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x166346965}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_775325446}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x967231262}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1461611209}[使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1120093533}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] graceful-restart]{lang="EN-US"}
:::

::: {#16863910 .myid}
[]{#_Toc404797976}[]{#struct_0_x1068_x9952_109547954}[]{#_Toc326062200}

**TRILL \-- TRILL配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

[**[graceful-restart interval]{lang="EN-US"}**]{#struct_0_x1068_x9952_x40747342}[命令用来配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔。]{style="font-family:宋体"}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_x1068_x9952_1561165001}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597917370}

[**[graceful-restart interval ]{lang="EN-US"}**]{#struct_0_x1068_x9952_720561029}*[interval]{lang="EN-US"}*

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_x1068_x9952_1012730165}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x936049462}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x49475094}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_84813380}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_2025374631}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x701737903}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x386379947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597851834}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1302204110}

[*[interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_x486755007}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1002271724}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x53432569}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_140483393}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] graceful-restart interval 120]{lang="EN-US"}
:::

::: {#1056335496 .myid}
[]{#_Toc379615164}[]{#_Toc379555232}[]{#_Toc404797977}[]{#struct_0_x1068_x9952_x937627749}[]{#_Toc386113386}[]{#_Toc385854384}[]{#_Toc379615168}[]{#_Toc379555236}

**TRILL \-- TRILL配置命令 \-- graceful-restart suppress-sa**

------------------------------------------------------------------------

[**[graceful-restart]{lang="EN-US"}**[ **suppress-sa**]{lang="EN-US"}]{#struct_0_x1068_x9952_x728267512}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[TRILL GR]{lang="EN-US"}[重启时抑制]{style="font-family:宋体"}[SA]{lang="EN-US"}[（]{style="font-family:宋体"}[Suppress-Advertisement]{lang="EN-US"}[）位置位。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **graceful-restart** **suppress-sa**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1238660069}[命令用来]{style="font-family:宋体"}[恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1442172436}

[**[graceful-restart]{lang="EN-US"}**[ **suppress-sa**]{lang="EN-US"}]{#struct_0_x1068_x9952_1791255606}

[**[undo]{lang="EN-US"}**[ **graceful-restart** **suppress-sa**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1635141953}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2049215674}

[[TRILL GR]{lang="EN-US"}]{#struct_0_x1068_x9952_1093982525}[重启时]{style="font-family:宋体"}[SA]{lang="EN-US"}[位将被置位。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1610640974}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1148519645}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2013486242}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1721638310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1542062471}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1042963110}

[[SA]{lang="EN-US"}]{#struct_0_x1068_x9952_225171665}[表示抑制邻接标志位，将其置位的主要目的是避免出现路由黑洞，例如在启动或重启时没有保留本地转发表，此时如果]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[将报文送到设备来进行转发将造成严重的丢包现象。在这种情况下，]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文中必须将]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位，而]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[收到这种]{style="font-family:宋体"}[SA]{lang="EN-US"}[位被置位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文后，将不会把发送该]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[放入]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中扩散出去。而对于启动速度要求较高的场景，则可以不配置]{style="font-family:宋体"}[TRILL GR]{lang="EN-US"}[重启时抑制]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1258380498}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_671098157}[配置]{style="font-family:宋体"}[TRILL GR]{lang="EN-US"}[重启时抑制]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1020234834}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] graceful-restart suppress-sa]{lang="EN-US"}
:::

::: {#486671225 .myid}
[]{#_Toc404797978}[]{#struct_0_x1068_x9952_1071311360}[]{#_Toc386113388}[]{#_Toc385854386}[]{#_Toc379615165}[]{#_Toc379555233}

**TRILL \-- TRILL配置命令 \-- ingress assign-delay**

------------------------------------------------------------------------

[**[ingress]{lang="EN-US"}**[ **assign-delay**]{lang="EN-US"}]{#struct_0_x1068_x9952_303284365}[命令用来配置入流量分配给新]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的延时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ingress** **assign-delay**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1216249913}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1171992533}

[**[ingress]{lang="EN-US"}**[ **assign-delay** ]{lang="EN-US"}*[delay]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1478353643}

[**[undo]{lang="EN-US"}**[ **ingress** **assign-delay**]{lang="EN-US"}]{#struct_0_x1068_x9952_1518723610}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_925279985}

[[入流量分配给新]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1697142636}[分发树的延时时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_806170400}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1714044862}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1443813270}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_837930552}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1765299008}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2112146321}

[*[delay]{lang="EN-US"}*]{#struct_0_x1068_x9952_396747127}[：入流量分配给新]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的延时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1471168406}

[[当入流量选择]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_343873275}[分发树的策略为负载均衡优先时，当新增一棵]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树时，为了让所有]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树来进行流量分担，]{style="font-family:宋体"}[Ingress RB]{lang="EN-US"}[需要将部分已分配给其它树的]{style="font-family:宋体"}[AVF VLAN]{lang="EN-US"}[重新分配给新树，以使新树分担本地流量的转发。但在其他]{style="font-family:宋体"}[RB]{lang="EN-US"}[尚未声明使用新树前，本地流量是无法使用新树进行转发的。因此，可以通过本命令来设置新树生效后，入流量分配给该树的延时时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x353700361}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1031740719}[配置入流量分配给新]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的延时时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1468984133}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] ingress assign-delay 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1062956952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ingress]{lang="EN-US"}**[ **assign-rule** **load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1132458420}
:::

::: {#380640639 .myid}
[]{#_Toc404797979}[]{#struct_0_x1068_x9952_1492170362}[]{#_Toc386113387}[]{#_Toc385854385}

**TRILL \-- TRILL配置命令 \-- ingress assign-rule load-balancing**

------------------------------------------------------------------------

[**[ingress]{lang="EN-US"}**[ **assign-rule** **load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_1723226256}[命令用来配置入流量选择]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的策略为负载均衡优先。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ingress** **assign-rule**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1963308304}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_282642343}

[**[ingress]{lang="EN-US"}**[ **assign-rule** **load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_831227319}

[**[undo]{lang="EN-US"}**[ **ingress** **assign-rule**]{lang="EN-US"}]{#struct_0_x1068_x9952_x880230104}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_550192200}

[[入流量选择]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1418319704}[分发树的策略为稳定优先。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1340846740}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x253258479}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2081253704}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x998785250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x63470570}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1753113682}

[[当新增或删除]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_562712459}[分发树时，入流量选择]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的策略缺省为稳定优先，即尽量保持原分发树不变；如果想让全部分发树都对入流量进行负载分担，则可将策略配置为负载均衡优先。]{style="font-family:宋体"}

[[需要注意的是，本命令只影响减少]{style="font-family:宋体"}[AVF VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x801419177}[时对剩余]{style="font-family:宋体"}[AVF VLAN]{lang="EN-US"}[选择]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1486752474}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_2134871522}[配置入表项选择]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的策略为负载均衡优先。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1388036615}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] ingress assign-rule load-balancing]{lang="EN-US"}
:::

::: {#-1553303123 .myid}
[]{#_Toc404797980}[]{#struct_0_x1068_x9952_2074717768}

**TRILL \-- TRILL配置命令 \-- log-peer-change enable**

------------------------------------------------------------------------

[**[log-peer-change]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x369922188}[命令用来开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻接状态输出开关。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **log-peer-change** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1598048442}[命令用来关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻接状态输出开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x22823944}

[**[log-peer-change]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1540285915}

[**[undo]{lang="EN-US"}**[ **log-peer-change** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_1980040364}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x51021960}

[[邻接状态输出开关处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1033241143}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_746561734}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x393320103}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597982906}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1368041460}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1629341805}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_901556381}

[[开启邻接状态输出开关后，]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_935904474}[邻接状态的变化会输出到配置终端上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1280667697}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_310957320}[关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻接状态输出开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x925980878}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] undo log-peer-change enable]{lang="EN-US"}
:::

::: {#-446381553 .myid}
[]{#_Toc404797981}[]{#struct_0_x1068_x9952_x1597655226}[]{#_Toc339972653}

**TRILL \-- TRILL配置命令 \-- lsp-length originate**

------------------------------------------------------------------------

[**[lsp-length]{lang="EN-US"}**[ **originate**]{lang="EN-US"}]{#struct_0_x1068_x9952_409328226}[命令用来配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[可生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **lsp-length** **originate**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1496032580}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x7152887}

[**[lsp-length]{lang="EN-US"}**[ **originate** *size*]{lang="EN-US"}]{#struct_0_x1068_x9952_821401782}

[**[undo]{lang="EN-US"}**[ **lsp-length** **originate**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1945070777}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2054695240}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x110853693}[可生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度为]{style="font-family:宋体"}[1458]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x209947305}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597589690}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x455098701}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_373266045}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x674820897}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1506606325}

[*[size]{lang="EN-US"}*]{#struct_0_x1068_x9952_x194835488}[：表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[可生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度，取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x297630590}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_178630810}[的实际最大长度将由本配置值、端口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值和所有其它]{style="font-family:宋体"}[RB]{lang="EN-US"}[在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中携带的自身能生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度这三者中的最小值来决定。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x67543401}[可生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度不得大于]{style="font-family:宋体"}[RB]{lang="EN-US"}[可接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度，否则系统将提示出错。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597786298}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1110467471}[配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[可生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1786283719}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] lsp-length originate 1024]{lang="EN-US"}

[]{#_Toc339972654}[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_874687790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lsp-length]{lang="EN-US"}**[ **receive**]{lang="EN-US"}]{#struct_0_x1068_x9952_x913238177}
:::

::: {#-1321064373 .myid}
[]{#_Toc404797982}[]{#struct_0_x1068_x9952_119961292}

**TRILL \-- TRILL配置命令 \-- lsp-length receive**

------------------------------------------------------------------------

[**[lsp-length]{lang="EN-US"}**[ **receive**]{lang="EN-US"}]{#struct_0_x1068_x9952_x983994573}[命令用来配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[可接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **lsp-length** **receive**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597720762}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1214734852}

[**[lsp-length]{lang="EN-US"}**[ **receive** *size*]{lang="EN-US"}]{#struct_0_x1068_x9952_782762700}

[**[undo]{lang="EN-US"}**[ **lsp-length** **receive**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1475042151}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1003849003}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x712360875}[可接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度为]{style="font-family:宋体"}[1492]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1160523180}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1259402514}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x28576590}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597393082}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1185646288}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1420025311}

[*[size]{lang="EN-US"}*]{#struct_0_x1068_x9952_662386315}[：表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[可接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度，取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1358656822}

[[需要注意的是，]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x714118869}[可接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度不得小于]{style="font-family:宋体"}[RB]{lang="EN-US"}[可生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度，否则系统将提示出错。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x522946833}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_556144775}[配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[可接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[最大长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597327546}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] lsp-length receive 1024]{lang="EN-US"}

[]{#_Toc339972655}[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1521840230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lsp-length originate]{lang="EN-US"}**]{#struct_0_x1068_x9952_x148032806}
:::

::: {#196595129 .myid}
[]{#_Toc404797983}[]{#struct_0_x1068_x9952_446179124}

**TRILL \-- TRILL配置命令 \-- max-unicast-load-balancing**

------------------------------------------------------------------------

[**[max-unicast-load-balancing]{lang="EN-US"}**]{#struct_0_x1068_x9952_x2095926323}[命令用来配置]{style="font-family:
宋体"}[TRILL]{lang="EN-US"}[单播等价多路径的最大路径数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **max-unicast-load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_x275304276}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x498281327}

[**[max-unicast-load-balancing]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x1068_x9952_x662916890}

[**[undo]{lang="EN-US"}**[ **max-unicast-load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597917369}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1930480146}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1177021293}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2121498771}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1652935866}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2042223848}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x810433932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1826523955}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1992584031}

[*[number]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1597851833}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[单播等价多路径的最大路径数，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示不进行负载分担。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x542689223}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_2106206976}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[单播等价多路径的最大路径数为]{style="font-family:宋体"}[3]{lang="EN-US"}[条。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_2020343896}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] max-unicast-load-balancing 3]{lang="EN-US"}
:::

::: {#1854666751 .myid}
[]{#_Toc404797984}[]{#struct_0_x1068_x9952_225237201}[]{#_Toc386113393}[]{#_Toc385854391}[]{#_Toc379615167}[]{#_Toc379555235}

**TRILL \-- TRILL配置命令 \-- multicast multi-thread enable**

------------------------------------------------------------------------

[**[multicast]{lang="EN-US"}**[ **multi-thread** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x849203530}[命令用来开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树计算]{style="font-family:宋体"}[支持多线程功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **multicast** **multi-thread** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_33528846}[命令用来关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树计算]{style="font-family:宋体"}[支持多线程功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1635009182}

[**[multicast]{lang="EN-US"}**[ **multi-thread** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_951338319}

[**[undo]{lang="EN-US"}**[ **multicast** **multi-thread** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x640760443}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2004750708}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1595074742}[分发树计算]{style="font-family:宋体"}[支持多线程功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_562219563}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1697077100}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1676776982}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_300478543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1493852817}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1393454702}

[[在多核]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1068_x9952_88484501}[设备上]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树计算]{style="font-family:宋体"}[支]{style="font-family:宋体"}[持多线程功能，以提升]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树]{style="font-family:宋体"}[的计算效率。开启本功能后]{style="font-family:宋体"}[，每棵]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树将分别]{style="font-family:宋体"}[使用一个线程进行计算。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2052442914}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在单核]{style="font-family:宋体"}]{#struct_0_x1068_x9952_200475867}[CPU]{lang="EN-US"}[设备上]{style="font-family:宋体"}[开启本功能后，]{style="font-family:宋体"}[并不一定会带来效率的提升。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启或关闭]{style="font-family:宋体"}]{#struct_0_x1068_x9952_719043623}[本功能，]{style="font-family:宋体"}[将会清除]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进程当前的动态运行数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x412539018}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1637678404}[开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树计算]{style="font-family:宋体"}[支持多线程功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1031806255}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] multicast multi-thread enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_479931104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**]{#struct_0_x1068_x9952_2125975275}[ **trill**]{lang="EN-US"}
:::

::: {#766037401 .myid}
[]{#_Toc404797985}[]{#struct_0_x1068_x9952_x2016026674}

**TRILL \-- TRILL配置命令 \-- multicast-ecmp enable**

------------------------------------------------------------------------

[**[multicast-ecmp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x2015961138}[命令用来开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播等价多路径功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **multicast-ecmp** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x23112893}[命令用来关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播等价多路径功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1901823719}

[**[multicast-ecmp]{lang="EN-US"}**[ **enable** [\[ **p2p-ignore** \]]{style="color:black"}]{lang="EN-US"}]{#struct_0_x1068_x9952_x625758650}

[**[undo]{lang="EN-US"}**[ **multicast-ecmp** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_1573430869}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1062849408}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1207595620}[组播等价多路径功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x566523747}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x2015895602}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_857220051}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1254903504}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x201406951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1340781204}

[**[p2p-ignore]{lang="EN-US" style="color:black"}**]{#struct_0_x1068_x9952_498434406}[：表示在伪节点被旁路的等价路径上，只使用一条路径转发组播报文。如果未指定本参数，表示在伪节点被旁路的等价路径上，使用全部等价路径转发组播报文，这样可在最大程度上实现组播流量的负载分担。但当与第三方厂商的设备互通时，可能需要指定本参数以保证互通成功。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1685510811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1368815309}[TRILL]{lang="EN-US"}[组播等价多路径功能关闭时，由于根桥不同而使各分发树拓扑不同，从而可在一定程度上实现组播流量的负载分担，但并未利用开销相同的等价路径来分担流量；当开启该功能后，]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[可将这些等价路径分给不同的分发树，从而实现更好的负载分担效果。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本功能的配置在]{style="font-family:宋体"}]{#struct_0_x1068_x9952_855127222}[TRILL]{lang="EN-US"}[网络中所有]{style="font-family:宋体"}[RB]{lang="EN-US"}[上应完全一致，否则可能导致组播流量不通。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1928554037}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x806499534}[开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[组播等价多路径功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x2015830066}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] multicast-ecmp enable]{lang="EN-US"}
:::

::: {#1142895620 .myid}
[]{#_Toc404797986}[]{#struct_0_x1068_x9952_1525515412}[]{#_Toc339972656}[]{#_Toc347394258}[]{#_Toc347394259}

**TRILL \-- TRILL配置命令 \-- nickname**

------------------------------------------------------------------------

[**[nickname]{lang="EN-US"}**]{#struct_0_x1068_x9952_1158272362}[命令用来配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **nickname**]{lang="EN-US"}]{#struct_0_x1068_x9952_x2126758881}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_775647630}

[**[nickname]{lang="EN-US"}**[ *nickname* \[ **priority** *priority* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x1598048441}

[**[undo]{lang="EN-US"}**[ **nickname** *nickname*]{lang="EN-US"}]{#struct_0_x1068_x9952_x426108471}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_810919336}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_1017366781}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[由系统自动分配，其持有]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_x1068_x9952_9956982}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1144836849}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_809559618}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x856794337}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1911627843}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597982905}

[*[nickname]{lang="EN-US"}*]{#struct_0_x1068_x9952_964756933}[：表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFBF]{lang="EN-US"}[的十六进制数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x1068_x9952_423000782}[：表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[持有]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[129]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[192]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x795762107}

[[Nickname]{lang="EN-US"}]{#struct_0_x1068_x9952_473251089}[是]{style="font-family:宋体"}[RB]{lang="EN-US"}[在]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络中的地址。如果]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络中不同]{style="font-family:宋体"}[RB]{lang="EN-US"}[拥有相同的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，则优先级较高者保留此]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[；如果优先级也相同，则]{style="font-family:宋体"}[System ID]{lang="EN-US"}[较大者保留此]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，其余]{style="font-family:宋体"}[RB]{lang="EN-US"}[再由系统为其自动分配一个新的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1428684749}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x283449675}[配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[为]{style="font-family:宋体"}[0x0001]{lang="EN-US"}[，其持有]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[198]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1368855730}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] nickname 0001 priority 198]{lang="EN-US"}
:::

::: {#-1264590328 .myid}
[]{#_Toc404797987}[]{#struct_0_x1068_x9952_x1597655225}

**TRILL \-- TRILL配置命令 \-- reset trill**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **trill**]{lang="EN-US"}]{#struct_0_x1068_x9952_812612753}[命令用来清除]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进程当前的动态运行数据。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_141416686}

[**[reset]{lang="EN-US"}**[ **trill**]{lang="EN-US"}]{#struct_0_x1068_x9952_643231294}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1865359315}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1304321358}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_24025253}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1503372586}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x782459817}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597589689}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1664886746}[清除]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进程当前的动态运行数据。]{style="font-family:宋体"}

[[\<Sysname\> reset trill]{lang="EN-US"}]{#struct_0_x1068_x9952_54072903}
:::

::: {#916303518 .myid}
[]{#_Toc404797988}[]{#struct_0_x1068_x9952_x1744065731}[]{#_Toc386113397}[]{#_Toc385854395}[]{#_Toc379615166}[]{#_Toc379555234}

**TRILL \-- TRILL配置命令 \-- set ingress-load-balancing**

------------------------------------------------------------------------

[**[set]{lang="EN-US"}**[ **ingress-load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_x794480142}[命令用来对]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树转发的流量进行手工均衡。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_628587264}

[**[set]{lang="EN-US"}**[ **ingress-load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1130466885}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_250608959}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1635660002}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1380390104}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x321882219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1132129041}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1834072771}

[[当入流量选择]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_931590060}[分发树的策略为稳定优先时，当]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[在各]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树上分布不均衡时，可使用本命令对]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树转发的流量进行手工均衡。]{style="font-family:宋体"}

[[需要注意的是，执行本命令可能影响当前某些报文的转发。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1425529834}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1586223494}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_357237521}[对]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树转发的流量进行手工均衡。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x937496677}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] set ingress-load-balancing]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x457425061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ingress]{lang="EN-US"}**[ **assign-rule** **load-balancing**]{lang="EN-US"}]{#struct_0_x1068_x9952_731818888}
:::

::: {#1011346875 .myid}
[]{#_Toc404797989}[]{#struct_0_x1068_x9952_x2090658901}[]{#_Toc339972658}

**TRILL \-- TRILL配置命令 \-- set overload**

------------------------------------------------------------------------

[**[set]{lang="EN-US"}**[ **overload**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1706729240}[命令用来将]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的过载标志位置位并配置保持置位状态的时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **set** **overload**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1836326010}[命令用来清除过载标志位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1649537657}

[**[set]{lang="EN-US"}**[ **overload** \[ *timeout* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x817904962}

[**[undo]{lang="EN-US"}**[ **set** **overload**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597786297}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_350952584}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x860200233}[的过载标志位未置位。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1279516513}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_99861916}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1999887673}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x442315707}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1230222108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x456261997}

[*[timeout]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1597720761}[：表示过载标志位保持置位状态的时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。缺省值为无穷大，即一直保持置位状态直至被清除。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_351349089}

[[需要注意的是，请不要在作为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x236913377}[分发树根桥的]{style="font-family:宋体"}[RB]{lang="EN-US"}[上配置本命令，否则将导致使用该根桥的流量转发不通。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2005117042}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1899619321}[将]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的过载标志位置位，并配置保持置位状态的时间为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_958611190}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] set overload 1200]{lang="EN-US"}
:::

::: {#870763228 .myid}
[]{#_Toc339972659}[]{#_Toc404797990}[]{#struct_0_x1068_x9952_1554778613}[]{#_Toc344302280}

**TRILL \-- TRILL配置命令 \-- snmp context-name**

------------------------------------------------------------------------

[**[snmp]{lang="EN-US"}**]{#struct_0_x1068_x9952_979159430}[ **context-name**]{lang="EN-US"}[命令用来配置管理]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp** ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597393081}**[context-name]{lang="EN-US"}**[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x782361761}

[**[snmp]{lang="EN-US"}**]{#struct_0_x1068_x9952_2009577789}[ **context-name**]{lang="EN-US"}[ *context-name*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **snmp** ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1498712747}**[context-name]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x703182580}

[[没有配置]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1443825568}[管理]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1518279421}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_667500386}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597327545}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1207043125}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x812651694}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1591517621}

[*[context-name]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1999868357}[：上下文的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_596497165}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1758284199}[使用]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Management Information Base]{lang="EN-US"}[，管理信息库）对]{style="font-family:宋体"}[NMS]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Management System]{lang="EN-US"}[，网络管理系统）提供]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[对象的管理，但标准]{style="font-family:宋体"}[IS-IS MIB]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[为单实例管理对象，无法同时对]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[和]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进行管理]{style="font-family:宋体"}[。因此，参考]{style="font-family:宋体"}[RFC 4750]{lang="EN-US"}[中对]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[多实例的管理方法，为管理]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[定义一个上下文名称，以区分来自]{style="font-family:宋体"}[NMS]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求是要对]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[还是]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进行管理。需要注意的是，由于上下文名称只是]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[独有的概念，因此对于]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[，会将团体名映射为上下文名称以对不同协议进行区分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x930400045}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_762176151}[配置管理]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称为]{style="font-family:宋体"}[trill]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597917372}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] snmp context-name trill]{lang="EN-US"}
:::

::: {#-1450992871 .myid}
[]{#_Toc404797991}[]{#struct_0_x1068_x9952_1883360443}[]{#_Toc344302281}

**TRILL \-- TRILL配置命令 \-- snmp-agent trap enable trill**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**]{#struct_0_x1068_x9952_14907281}[ **trap** **enable** **trill**]{lang="EN-US"}[命令用来开启]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[告警]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**]{#struct_0_x1068_x9952_588948503}[ **snmp-agent** **trap** **enable** **trill**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[告警]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1174646266}

[**[snmp-agent]{lang="EN-US"}**]{#struct_0_x1068_x9952_x960630687}[ **trap** **enable** **trill**]{lang="EN-US"}[ ]{lang="EN-US"}[\[ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]{lang="EN-US"}**[maxarea-mismatch]{lang="NO-BOK"}**[ \| **new-drb** \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** \] \*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**]{#struct_0_x1068_x9952_2047615374}[ ]{lang="EN-US"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **trill**]{lang="EN-US"}[ ]{lang="EN-US"}[\[ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]{lang="EN-US"}**[maxarea-mismatch]{lang="NO-BOK"}**[ \| **new-drb** \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** \] \*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1842751031}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597851836}[的]{style="font-family:宋体"}[告警]{style="font-family:宋体"}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x139404696}

[[系统]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x255979474}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x243391706}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_552306056}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1835392295}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1439719596}

[**[adjacency-state-change]{lang="EN-US"}**]{#struct_0_x1068_x9952_1193493744}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻接状态变化的告警信息。]{style="font-family:宋体"}

[**[area-mismatch]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1598048444}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文区域地址不匹配的告警信息。]{style="font-family:宋体"}

[**[buffsize-mismatch]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1185623358}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[长度与产生缓冲区大小不匹配的告警信息。]{style="font-family:宋体"}

[**[id-length-mismatch]{lang="EN-US"}**]{#struct_0_x1068_x9952_x529187856}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[报文中]{style="font-family:宋体"}[System ID]{lang="EN-US"}[长度不匹配的告警信息。]{style="font-family:宋体"}

[**[lsdboverload-state-change]{lang="EN-US"}**]{#struct_0_x1068_x9952_x361133004}[：表示]{style="font-family:
宋体"}[LSDB]{lang="EN-US"}[过载状态变化的告警信息。]{style="font-family:宋体"}

[**[lsp-parse-error]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1375175022}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[解析错误的告警信息。]{style="font-family:宋体"}

[**[lsp-size-exceeded]{lang="EN-US"}**]{#struct_0_x1068_x9952_1023823865}[：表示超大]{style="font-family:宋体"}[LSP]{lang="EN-US"}[导致泛洪失败的告警信息。]{style="font-family:宋体"}

[**[max-seq-exceeded]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1712746321}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号超过最大序列号的告警信息。]{style="font-family:宋体"}

[**[maxarea-mismatch]{lang="NO-BOK"}**]{#struct_0_x1068_x9952_23142738}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文最大区域地址不匹配的告警信息。]{style="font-family:宋体"}

[**[new-drb]{lang="EN-US"}**]{#struct_0_x1068_x9952_x245065932}[：表示成为新]{style="font-family:宋体"}[DRB]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}

[**[own-lsp-purge]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1597982908}[：表示尝试清除本地]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}

[**[protocol-support]{lang="EN-US"}**]{#struct_0_x1068_x9952_561472406}[：表示报文协议支持类型不匹配的告警信息。]{style="font-family:宋体"}

[**[rejected-adjacency]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1102330059}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文邻接不匹配丢弃的告警信息。]{style="font-family:宋体"}

[**[skip-sequence-number]{lang="EN-US"}**]{#struct_0_x1068_x9952_598926744}[：表示跳过已产生过的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号的告警信息。]{style="font-family:宋体"}

[**[topology-change]{lang="EN-US"}**]{#struct_0_x1068_x9952_x984234883}[：表示]{style="font-family:宋体"}[AVF]{lang="EN-US"}[状态变化的告警信息。]{style="font-family:宋体"}

[**[version-skew]{lang="EN-US"}**]{#struct_0_x1068_x9952_x662563156}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文版本号不匹配的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_395607800}

[[如果未指定任何可选参数，表示开启或关闭]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x490953535}[TRILL]{lang="EN-US"}[的全部告警功能。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1635762535}[的告警功能之后，]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_969539052}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597655228}[关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的全部]{style="font-family:宋体"}[告警]{style="font-family:宋体"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1928358000}

[\[Sysname\] undo snmp-agent trap enable trill]{lang="EN-US"}
:::

::: {#928103452 .myid}
[]{#_Toc404797992}[]{#struct_0_x1068_x9952_1211029723}

**TRILL \-- TRILL配置命令 \-- system-id**

------------------------------------------------------------------------

[**[system-id]{lang="EN-US"}**]{#struct_0_x1068_x9952_605238628}[命令用来配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **system-id**]{lang="EN-US"}]{#struct_0_x1068_x9952_1630096207}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1514722332}

[**[system-id]{lang="EN-US"}**[ *system-id*]{lang="EN-US"}]{#struct_0_x1068_x9952_x484598309}

[**[undo]{lang="EN-US"}**[ **system-id**]{lang="EN-US"}]{#struct_0_x1068_x9952_x454778893}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597589692}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1617898115}[启动后会根据自己的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址自动生成一个]{style="font-family:宋体"}[System ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1458742293}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x951870311}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x693046516}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x760803721}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1242005606}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x477040385}

[*[system-id]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1498742381}[：表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xxxx.xxxx.xxxx]{lang="EN-US"}[，]{style="font-family:宋体"}[x]{lang="EN-US"}[代表十六进制数。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597786300}

[[需要注意的是，如果用户为]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_753778360}[新配置的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[与原有的不同，系统将重置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1165267094}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x15663604}[配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1010.1020.1030]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1592997677}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] system-id 1010.1020.1030]{lang="EN-US"}
:::

::: {#408390348 .myid}
[]{#_Toc404797993}[]{#struct_0_x1068_x9952_x177916254}[]{#_Toc386113402}[]{#_Toc385854400}[]{#_Toc379615172}[]{#_Toc379555240}[]{#_Toc378607612}[]{#_Toc350776425}[]{#_Toc333225599}[]{#_Toc33866123}

**TRILL \-- TRILL配置命令 \-- timer lsp-generation**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **lsp-generation**]{lang="EN-US"}]{#struct_0_x1068_x9952_94092931}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成的时间间隔]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **lsp-generation**]{lang="EN-US"}]{#struct_0_x1068_x9952_455843964}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1744000195}

[**[timer]{lang="EN-US"}**[ **lsp-generation** ]{lang="EN-US"}*[maximum-interval]{lang="EN-US"}*[ \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x1583843970}

[**[undo]{lang="EN-US"}**[ **timer** **lsp-generation**]{lang="EN-US"}]{#struct_0_x1068_x9952_x2069781418}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1529654927}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_2025087279}[重新生成的最大时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1871596853}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_890098909}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1449175036}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_376164871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x40458572}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1130284984}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_628652800}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新]{style="font-family:宋体"}[生成的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1980648368}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新]{style="font-family:宋体"}[生成的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒，必须为]{style="font-family:宋体"}[10]{lang="EN-US"}[的整数倍。最小时间间隔必须小于最大时间间隔。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1341303209}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新]{style="font-family:宋体"}[生成的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒，必须为]{style="font-family:宋体"}[10]{lang="EN-US"}[的整数倍。时间间隔惩罚增量必须小于最大时间间隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1971422498}

[[网络拓扑的变化会导致重新生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_1384193472}[，通过调节]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成的时间间隔，可以抑制网络频繁变化可能导致的对带宽资源和设备资源的过多占用。在网络变化不频繁的情况下，将]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成的时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*[，而在网络变化频繁的情况下可进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_205914811}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_385072390}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成的最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1900723937}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] timer lsp-generation 10 100 200]{lang="EN-US"}
:::

::: {#490996559 .myid}
[]{#_Toc404797994}[]{#struct_0_x1068_x9952_1115081765}

**TRILL \-- TRILL配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **lsp-max-age**]{lang="EN-US"}]{#struct_0_x1068_x9952_x2069196656}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **lsp-max-age**]{lang="EN-US"}]{#struct_0_x1068_x9952_441304702}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597720764}

[**[timer]{lang="EN-US"}**[ **lsp-max-age** *time*]{lang="EN-US"}]{#struct_0_x1068_x9952_x51935438}

[**[undo]{lang="EN-US"}**[ **timer** **lsp-max-age**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1473665857}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_520719300}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1848009172}[的最大生存时间为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_582616820}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1199753109}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x956499333}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1650598599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597393084}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x22846874}

[*[time]{lang="EN-US"}*]{#struct_0_x1068_x9952_1971299892}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_681188301}

[[当]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1833268520}[生成一个]{style="font-family:宋体"}[LSP]{lang="EN-US"}[时，会将该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间作为]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中的剩余生存时间告知其他]{style="font-family:宋体"}[RB]{lang="EN-US"}[。当]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中一个]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的剩余生存时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，说明该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[已失效，]{style="font-family:宋体"}[RB]{lang="EN-US"}[将从]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中删除该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的内容，只保留其摘要，并将该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的剩余生存时间置]{style="font-family:宋体"}[0]{lang="EN-US"}[后泛洪给其他]{style="font-family:宋体"}[RB]{lang="EN-US"}[以清除此]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，由于]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x868733739}[的实际刷新时间会受]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送间隔和一次发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大数目的影响，因此请合理配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间和刷新周期，以免]{style="font-family:宋体"}[LSP]{lang="EN-US"}[被意外老化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1295417147}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_582995136}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间为]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597327548}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] timer lsp-max-age 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1972178924}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="FR"}**]{#struct_0_x1068_x9952_917606414}[ **lsp-refresh**]{lang="FR"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**[ **timer** **lsp**]{lang="EN-US"}]{#struct_0_x1068_x9952_866919679}
:::

::: {#-1091829735 .myid}
[]{#_Toc404797995}[]{#struct_0_x1068_x9952_1113925918}

**TRILL \-- TRILL配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **lsp-refresh**]{lang="EN-US"}]{#struct_0_x1068_x9952_1628004816}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的刷新周期。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **lsp-refresh**]{lang="EN-US"}]{#struct_0_x1068_x9952_x650944140}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x212656003}

[**[timer]{lang="FR"}**]{#struct_0_x1068_x9952_x1597917371}[ **lsp-refresh** ]{lang="FR"}*[time]{lang="FR"}*

[**[undo]{lang="FR"}**]{#struct_0_x1068_x9952_x2008322326}[ **timer** **lsp-refresh**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1401387096}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x474185257}[的刷新周期为]{style="font-family:宋体"}[900]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x648060982}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x551022495}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1440216985}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1863266516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_2058227631}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597851835}

[*[time]{lang="EN-US"}*]{#struct_0_x1068_x9952_263879831}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的刷新周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x551309997}

[[对于一个本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_x1463410053}[，当其剩余生存时间]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[（最大生存时间－刷新周期）时，即使该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中的内容没有任何改变，也要重新更新此]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，这样可避免网络中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[老化太频繁，保证网络稳定性。]{style="font-family:宋体"}

[[需要注意的是，由于]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_442892579}[的实际刷新时间会受]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送间隔和一次发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大数目的影响，因此请合理配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间和刷新周期，以免]{style="font-family:宋体"}[LSP]{lang="EN-US"}[被意外老化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1875623866}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1372804774}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的刷新周期为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1598048443}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] timer lsp-refresh 1000]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1588907885}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="EN-US"}**[ **lsp-max-age**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1345385427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**[ **timer** **lsp**]{lang="EN-US"}]{#struct_0_x1068_x9952_x431890434}
:::

::: {#1171776781 .myid}
[]{#_Toc404797996}[]{#struct_0_x1068_x9952_190964504}[]{#_Toc339972662}

**TRILL \-- TRILL配置命令 \-- timer spf**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **spf**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1615304021}[命令用来配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[使用]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法进行路由计算的时间间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **spf**]{lang="EN-US"}]{#struct_0_x1068_x9952_x359442949}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_62851415}

[**[timer]{lang="EN-US"}**[ **spf** *maximum-interval* \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x218768534}

[**[undo]{lang="EN-US"}**[ **timer** **spf**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597982907}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x198042481}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1726661629}[使用]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法进行路由计算的最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x153626871}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_317470506}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x169112965}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_930548209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x761636913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1636639448}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1597655227}[：表示最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_1975412167}[：表示最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒，必须为]{style="font-family:宋体"}[10]{lang="EN-US"}[的整数倍。最小时间间隔必须小于最大时间间隔。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_343285175}[：表示时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒，必须为]{style="font-family:宋体"}[10]{lang="EN-US"}[的整数倍。时间间隔惩罚增量必须小于最大时间间隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x306407791}

[[根据本地维护的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1307160774}[，]{style="font-family:宋体"}[RB]{lang="EN-US"}[通过]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法算出以自己为根的最短路径树，并根据此树决定到达目的网络的下一跳。通过调节]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法的时间间隔，可抑制由于网络频繁变化而导致的带宽资源和设备资源的过多占用。]{style="font-family:宋体"}

[[系统在网络变化不频繁时将连续路由计算的时间间隔缩小至]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_1218958244}[，而在网络变化频繁时进行相应的惩罚，即]{style="font-family:宋体"}[增加]{style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[×]{style="font-family:宋体"}[2^n-2^]{lang="EN-US"}[（]{style="font-family:宋体"}[n]{lang="EN-US"}[为连续触发路由计算的次数），但]{style="font-family:宋体"}[最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1980147930}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1601055453}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[使用]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法进行路由计算的最大时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597589691}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] timer spf 15 100 200]{lang="EN-US"}
:::

::: {#489164287 .myid}
[]{#_Toc404797997}[]{#struct_0_x1068_x9952_x2021182642}

**TRILL \-- TRILL配置命令 \-- tree-root priority**

------------------------------------------------------------------------

[**[tree-root]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_x1068_x9952_x303184104}[命令用来配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[作为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **tree-root** **priority**]{lang="EN-US"}]{#struct_0_x1068_x9952_123716427}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x794606957}

[**[tree-root]{lang="EN-US"}**[ **priority** *priority*]{lang="EN-US"}]{#struct_0_x1068_x9952_887361441}

[**[undo]{lang="EN-US"}**[ **tree-root** **priority**]{lang="EN-US"}]{#struct_0_x1068_x9952_259399867}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x422205947}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597786299}[作为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树的根桥优先级为]{style="font-family:宋体"}[32768]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x455616470}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1497811158}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x260487674}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x776908410}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_485318154}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1753651982}

[*[priority]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1707298757}[：表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[作为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，数值越大优先级越高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1149183738}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597720763}[配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[作为]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树根桥的优先级为]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1514148503}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] tree-root priority 65535]{lang="EN-US"}
:::

::: {#481906170 .myid}
[]{#_Toc404797998}[]{#struct_0_x1068_x9952_x28005923}

**TRILL \-- TRILL配置命令 \-- trees calculate**

------------------------------------------------------------------------

[**[trees]{lang="EN-US"}**[ **calculate**]{lang="EN-US"}]{#struct_0_x1068_x9952_x448261174}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[希望整网计算的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树数量。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trees** **calculate**]{lang="EN-US"}]{#struct_0_x1068_x9952_782992704}[命令]{style="font-family:宋体"}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x876960092}

[**[trees]{lang="EN-US"}**[ **calculate** *count*]{lang="EN-US"}]{#struct_0_x1068_x9952_1199571693}

[**[undo]{lang="EN-US"}**[ **trees** ]{lang="EN-US"}**[calculate]{lang="EN-US"}**]{#struct_0_x1068_x9952_x2128682120}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597393083}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_380437653}[希望整网计算的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[棵。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_449053756}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1265125266}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1728374033}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1747846070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_637175602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x460205537}

[*[count]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1597327547}[：表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[希望整网计算的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x44243711}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_446024262}[配置]{style="font-family:宋体"}[RB]{lang="EN-US"}[希望整网计算的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[分发树数量为]{style="font-family:宋体"}[2]{lang="EN-US"}[棵。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1656608701}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] trees calculate 2]{lang="EN-US"}
:::

::: {#443679883 .myid}
[]{#_Toc404797999}[]{#struct_0_x1068_x9952_264287278}

**TRILL \-- TRILL配置命令 \-- trill**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**]{#struct_0_x1068_x9952_x465023826}[命令用来全局使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议，并进入]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill**]{lang="EN-US"}]{#struct_0_x1068_x9952_1999535667}[命令用来全局关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_709670357}

[**[trill]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1597917374}

[**[undo]{lang="EN-US"}**[ **trill**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1248807439}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_889118214}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1111197987}[协议处于全局关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_170293657}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1811483645}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2076419788}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1112870799}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1532361692}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597851838}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1379625078}[全局使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议，并进入]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1337365135}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\]]{lang="EN-US"}
:::

::: {#1903571002 .myid}
[]{#_Toc404798000}[]{#struct_0_x1068_x9952_x1382494662}[]{#_Toc339972666}

**TRILL \-- TRILL配置命令 \-- trill announcing-vlan**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **announcing-vlan**]{lang="EN-US"}]{#struct_0_x1068_x9952_x799003997}[命令用来配置通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **announcing-vlan**]{lang="EN-US"}]{#struct_0_x1068_x9952_159106920}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_908541753}

[**[trill]{lang="EN-US"}**[ **announcing-vlan** { *vlan-list* \| **null** }]{lang="EN-US"}]{#struct_0_x1068_x9952_1350103656}

[**[undo]{lang="EN-US"}**[ **trill** **announcing-vlan** { *vlan-list* \| **null** }]{lang="EN-US"}]{#struct_0_x1068_x9952_x1598048446}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1946544524}

[[没有配置通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_749826245}[，此时通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的范围相同。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1792584270}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x1725918508}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1448758563}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1942874195}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x544116631}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_112678185}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1597982910}[：通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的列表，表示多个通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[null]{lang="EN-US"}**]{#struct_0_x1068_x9952_205176510}[：表示通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为空集，即不包含任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x2136419990}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x836542725}[之间的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，是通过一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合来交互的，具体来说：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x836542726}[在]{style="font-family:宋体"}[以下]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合中发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文：使能]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∩（]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∪]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非]{lang="EN-US" style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_2121517992}[在]{style="font-family:宋体"}[以下]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合中发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文：使能]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∩（指定]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∪（通告]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∩]{lang="EN-US" style="font-family:宋体"}[ AVF VLAN]{lang="EN-US"}[））。]{lang="EN-US" style="font-family:宋体"}

[[由于]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x836542723}[端口会在上述]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合的每个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内都发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，这样当]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合较大时，设备会因发送大量]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文而占用过多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[资源，从而无法及时处理其它协议的报文。为了避免这种情况，可以通过减少通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的范围来缩小]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合的范围。]{style="font-family:宋体"}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x795555358}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1621263321}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1476301296}[配置通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597655230}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill announcing-vlan 10 to 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1572193176}[配置通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为空集。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_434940295}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill announcing-vlan null]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1252440538}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**[ **designated-vlan**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1165646295}
:::

::: {#-1404112778 .myid}
[]{#_Toc404798001}[]{#struct_0_x1068_x9952_1791517750}[]{#_Toc386113410}[]{#_Toc385854408}[]{#_Toc379615169}[]{#_Toc379555237}[]{#_Toc378607609}

**TRILL \-- TRILL配置命令 \-- trill bypass-pseudonode enable**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **bypass-pseudonode** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x834679649}[命令用来开启旁路伪节点功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **bypass-pseudonode** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x488107242}[命令用来]{style="font-family:宋体"}[关闭旁路伪节点功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1956011468}

[**[trill]{lang="EN-US"}**[ **bypass-pseudonode** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1536112860}

[**[undo]{lang="EN-US"}**[ **trill** **bypass-pseudonode** **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_1848566697}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_225433809}

[[旁路伪节点功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_946257100}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1322116588}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x507164029}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1410219188}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1829127421}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1644839132}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_115679279}

[[开启本功能后，如果当前端口为]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1207288973}[且只有一个邻居，则不再生成伪节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，以减少网络中]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的数量。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x758411396}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_178486774}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启旁路伪节点功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1696880492}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="NO-BOK"}[trill bypass-pseudonode enable]{lang="EN-US"}
:::

::: {#1902513059 .myid}
[]{#_Toc404798002}[]{#struct_0_x1068_x9952_1393334629}[]{#_Toc339972667}

**TRILL \-- TRILL配置命令 \-- trill cost**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **cost**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1880216770}[命令用来配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口的链路开销值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **cost**]{lang="EN-US"}]{#struct_0_x1068_x9952_x897385073}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597589694}

[**[trill]{lang="EN-US"}**[ **cost** *value*]{lang="EN-US"}]{#struct_0_x1068_x9952_1870500127}

[**[undo]{lang="EN-US"}**[ **trill** **cost**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1549257630}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1898628050}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_554087310}[端口的链路开销值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1987920690}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_1626215937}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_757585487}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1535438583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597786302}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x409021054}

[*[value]{lang="EN-US"}*]{#struct_0_x1068_x9952_x216177388}[：表示链路开销值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1727838547}

[[对于]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_1932567642}[端口的链路开销值来说：如果进行了手工配置，则取配置值；如果没有手工配置且自动计算功能处于开启状态，则取自动计算值；如果没有手工配置且自动计算功能处于关闭状态，则取缺省值]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1046394531}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_451703184}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_650083202}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的链路开销值为]{style="font-family:宋体"}[20000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597720766}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill cost 20000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1110863976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-cost]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_1757390417}
:::

::: {#-776834799 .myid}
[]{#_Toc404798003}[]{#struct_0_x1068_x9952_389555506}[]{#_Toc339972668}

**TRILL \-- TRILL配置命令 \-- trill designated-vlan**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **designated-vlan**]{lang="EN-US"}]{#struct_0_x1068_x9952_426159711}[命令用来配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **designated-vlan**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1185779928}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_551451307}

[**[trill]{lang="EN-US"}**[ **designated-vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_x1068_x9952_1196791481}

[**[undo]{lang="EN-US"}**[ **trill** **designated-vlan**]{lang="EN-US"}]{#struct_0_x1068_x9952_1918362537}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597393086}

[[没有配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_1139952540}[，此时指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[由系统从使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中自动选出。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_496303406}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x2019028689}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1231241415}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x458888537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1079011354}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x586911775}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1597327550}[：表示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1966623548}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1218879750}[之间的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，是通过一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合来交互的，具体来说：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1121268593}[在]{style="font-family:宋体"}[以下]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合中发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文：使能]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∩（]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∪]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[通告]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非]{lang="EN-US" style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x1218879747}[在]{style="font-family:宋体"}[以下]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[集合中发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文：使能]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∩（指定]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∪（通告]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}[∩]{lang="EN-US" style="font-family:宋体"}[ AVF VLAN]{lang="EN-US"}[））。]{lang="EN-US" style="font-family:宋体"}

[[而除]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_x1218879748}[报文外的其它]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议报文和本地数据报文，则全部通过指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[来交互。因此，请确保所配置的指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[处于使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的范围内，否则可能导致]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[邻居无法建立或]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[数据报文无法转发。]{style="font-family:宋体"}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_15058588}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x816269059}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x326827469}[配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1950059839}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill designated-vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_867390799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**[ **announcing-vlan**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597917373}
:::

::: {#-149570930 .myid}
[]{#_Toc404798004}[]{#struct_0_x1068_x9952_x845522912}

**TRILL \-- TRILL配置命令 \-- trill drb-priority**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **drb-priority**]{lang="EN-US"}]{#struct_0_x1068_x9952_x35117062}[命令用来配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口的]{style="font-family:宋体"}[DRB]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill**]{lang="EN-US"}[ **drb-priority**]{lang="EN-US"}]{#struct_0_x1068_x9952_242020868}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1907176451}

[**[trill]{lang="EN-US"}**[ **drb-priority** *priority*]{lang="EN-US"}]{#struct_0_x1068_x9952_1737069205}

[**[undo]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[drb-priority]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1348909737}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1992104286}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1490196080}[端口的]{style="font-family:宋体"}[DRB]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597851837}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_1426679245}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1134801651}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1399841841}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1488390912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1616414826}

[*[priority]{lang="EN-US"}*]{#struct_0_x1068_x9952_x386264956}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口的]{style="font-family:宋体"}[DRB]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[，数值越大优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1303975599}

[[当网络类型为广播网时，]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x663262765}[需要选举]{style="font-family:宋体"}[DRB]{lang="EN-US"}[：]{style="font-family:宋体"}[DRB]{lang="EN-US"}[优先级较高的]{style="font-family:宋体"}[RB]{lang="EN-US"}[优先被选中为]{style="font-family:宋体"}[DRB]{lang="EN-US"}[；若两个]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[DRB]{lang="EN-US"}[优先级相同，则]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址最大者会被选为]{style="font-family:宋体"}[DRB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1598048445}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1543259997}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1333830269}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[DRB]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1071068467}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill drb-priority 2]{lang="EN-US"}
:::

::: {#772239676 .myid}
[]{#_Toc404798005}[]{#struct_0_x1068_x9952_x535211302}

**TRILL \-- TRILL配置命令 \-- trill enable**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_904031573}[命令用来在端口上使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill**]{lang="EN-US"}[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_483853363}[命令用来在端口上关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x339053353}

[**[trill]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597982909}

[**[undo]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[enable]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1004611535}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1702006912}

[[端口上的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x514081829}[协议处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_811490591}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_1487175077}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x222314915}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_2074226316}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597655229}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x800525355}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x71868677}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在端口上使能]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1633273777}[TRILL]{lang="EN-US"}[协议之前，必须先全局使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1772686487}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x872437348}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x137148022}[全局使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议，并在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x2093775130}

[\[Sysname\] trill]{lang="EN-US"}

[\[Sysname-trill\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1880415460}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1597589693}
:::

::: {#-694627945 .myid}
[]{#_Toc404798006}[]{#struct_0_x1068_x9952_1110985240}

**TRILL \-- TRILL配置命令 \-- trill link-type**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **link-type**]{lang="EN-US"}]{#struct_0_x1068_x9952_x254189101}[命令用来配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口的类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill**]{lang="EN-US"}[ **link-type**]{lang="EN-US"}]{#struct_0_x1068_x9952_535306819}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1088112404}

[**[trill]{lang="EN-US"}**[ **link-type** { **access** \[ **alone** \] \| **hybrid** \| **trunk** \| **vr** }]{lang="EN-US"}]{#struct_0_x1068_x9952_x734200990}

[**[undo]{lang="EN-US"}**[ **trill** **link-type**]{lang="EN-US"}]{#struct_0_x1068_x9952_1183048169}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_147837600}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_224260300}[端口的类型为]{style="font-family:宋体"}[Access]{lang="EN-US"}[类型（非]{style="font-family:宋体"}[Alone]{lang="EN-US"}[属性）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1597786301}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x812305581}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1602605035}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1727866852}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_468732326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_57863598}

[**[access]{lang="EN-US"}**[ \[ **alone** \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x1061669129}[：表示]{style="font-family:宋体"}[Access]{lang="EN-US"}[类型。如果未指定]{style="font-family:宋体"}**[alone]{lang="EN-US"}**[参数，表示非]{style="font-family:宋体"}[Alone]{lang="EN-US"}[属性的]{style="font-family:宋体"}[Access]{lang="EN-US"}[端口，此类端口只能处理本地数据报文和]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文；如果指定了]{style="font-family:宋体"}**[alone]{lang="EN-US"}**[参数，表示]{style="font-family:宋体"}[Alone]{lang="EN-US"}[属性的]{style="font-family:宋体"}[Access]{lang="EN-US"}[端口，此类端口不会收、发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，不参与]{style="font-family:宋体"}[DRB]{lang="EN-US"}[选举和]{style="font-family:宋体"}[AVF]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[**[hybrid]{lang="EN-US"}**]{#struct_0_x1068_x9952_1816719973}[：表示]{style="font-family:宋体"}[Hybrid]{lang="EN-US"}[类型。该类型的端口同时具有]{style="font-family:宋体"}[Access]{lang="EN-US"}[和]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[的属性，能够处理本地数据报文和过路数据报文。]{style="font-family:宋体"}

[**[trunk]{lang="EN-US"}**]{#struct_0_x1068_x9952_x1597720765}[：表示]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型。该类型的端口能够处理过路数据报文和部分二层协议报文（如]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文），不能处理本地数据报文。]{style="font-family:宋体"}

[**[vr]{lang="EN-US"}**]{#struct_0_x1068_x9952_x592082027}[：表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[类型。该类型的端口是一种特殊的虚拟路由端口，除了可以和]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型端口一样转发]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[数据报文外，还可以转发非]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[封装的三层单播数据报文和非]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[封装的二、三层组播数据报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1618019379}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x467351112}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_306419071}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1845840684}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的类型为]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1845117654}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill link-type trunk]{lang="EN-US"}
:::

::: {#477865632 .myid}
[]{#_Toc404798007}[]{#struct_0_x1068_x9952_1098513589}

**TRILL \-- TRILL配置命令 \-- trill timer avf-inhibited**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **timer** **avf-inhibited**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1901004223}[命令用来配置环路避免的抑制时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[timer]{lang="EN-US"}**[ **avf-inhibited**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597393085}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1543237067}

[**[trill]{lang="EN-US"}**[ **timer** **avf-inhibited** *time*]{lang="EN-US"}]{#struct_0_x1068_x9952_x1315570414}

[**[undo]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[timer]{lang="EN-US"}**[ **avf-inhibited**]{lang="EN-US"}]{#struct_0_x1068_x9952_8385068}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1322828710}

[[环路避免的抑制时间]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1395709871}[为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x334610720}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x921115949}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1074635520}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1597327549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_406094983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x560919228}

[*[time]{lang="EN-US"}*]{#struct_0_x1068_x9952_96792941}[：表示环路避免的抑制时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1668020384}

[[AVF]{lang="EN-US"}]{#struct_0_x1068_x9952_1541166019}[的存在保证了在一条链路上与一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[相关的报文，只会有唯一的出口或入口，其他]{style="font-family:宋体"}[RB]{lang="EN-US"}[收到与该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[相关的报文时将不做任何处理。然而，当]{style="font-family:宋体"}[RB]{lang="EN-US"}[发现链路上的根桥发生了变化，或其他]{style="font-family:宋体"}[RB]{lang="EN-US"}[宣称的]{style="font-family:宋体"}[AVF]{lang="EN-US"}[与本]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[AVF]{lang="EN-US"}[发生冲突时，会将相关的]{style="font-family:宋体"}[AVF]{lang="EN-US"}[抑制一段时间以避免环路的产生。抑制时间超时后，如果本]{style="font-family:宋体"}[RB]{lang="EN-US"}[仍是该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[AVF]{lang="EN-US"}[，则重新履行]{style="font-family:宋体"}[AVF]{lang="EN-US"}[的职能。]{style="font-family:宋体"}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2258925}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x326628395}

[[\#]{lang="EN-US"}]{#struct_0_x1068_x9952_x1599232391}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置环路避免的抑制时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x31833429}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill timer avf-inhibited 20]{lang="EN-US"}
:::

::: {#1571179840 .myid}
[]{#_Toc404798008}[]{#struct_0_x1068_x9952_x553933647}

**TRILL \-- TRILL配置命令 \-- trill timer csnp**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **timer** **csnp**]{lang="EN-US"}]{#struct_0_x1068_x9952_1533515032}[命令用来配置]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的发送间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **timer** **csnp**]{lang="EN-US"}]{#struct_0_x1068_x9952_266980721}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1628670434}

[**[trill]{lang="EN-US"}**[ **timer** **csnp** *interval*]{lang="EN-US"}]{#struct_0_x1068_x9952_443705566}

[**[undo]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[timer]{lang="EN-US"}**[ **csnp**]{lang="EN-US"}]{#struct_0_x1068_x9952_x120801013}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1691252342}

[[CSNP]{lang="EN-US"}]{#struct_0_x1068_x9952_x31767893}[报文的发送间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1539274676}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x534822157}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x272249783}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x1100814238}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x729454103}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_337260267}

[*[interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_604116482}[：表示]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x31964501}

[[当网络类型为广播网时，]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_x1068_x9952_x2101333841}[定期发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文进行全网的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步。]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文记录了本地]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要，当一个]{style="font-family:宋体"}[RB]{lang="EN-US"}[收到一个]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文时，就会与本地的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[进行比较，检查其中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[是否有老化和缺失。如果]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文中有某个]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要而本地]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中没有，]{style="font-family:宋体"}[RB]{lang="EN-US"}[将发送]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文以请求获取该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_447496407}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1806569180}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1370804878}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的发送间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x1587706693}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill timer csnp 15]{lang="EN-US"}
:::

::: {#1603844840 .myid}
[]{#_Toc404798009}[]{#struct_0_x1068_x9952_x392015840}

**TRILL \-- TRILL配置命令 \-- trill timer hello**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **timer** **hello**]{lang="EN-US"}]{#struct_0_x1068_x9952_1288995598}[命令用来配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **timer** **hello**]{lang="EN-US"}]{#struct_0_x1068_x9952_x31898965}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1732705476}

[**[trill]{lang="EN-US"}**[ **timer** **hello** *interval*]{lang="EN-US"}]{#struct_0_x1068_x9952_588310900}

[**[undo]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[timer]{lang="EN-US"}**[ **hello**]{lang="EN-US"}]{#struct_0_x1068_x9952_1636840978}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1668748313}

[[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_1189588625}[报文的发送间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1066085899}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x633199853}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1475416647}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x31571285}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x971904633}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1370565297}

[*[interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_1559947626}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x411831378}

[[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_860970627}[定期发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文以维持邻接关系。]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送间隔越短，网络收敛越快，但也会占用更多的系统资源。]{style="font-family:宋体"}

[[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_x1541200224}[报文的发送间隔与失效数目的乘积为]{style="font-family:宋体"}[邻接关系保持时间，即]{style="font-family:宋体"}[RB]{lang="EN-US"}[监测到链路失效并进行路由重计算的时间。]{style="font-family:宋体"}[RB]{lang="EN-US"}[通过]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文将邻接关系保持时间通知给其邻居，若该邻居在邻接关系保持时间内未收到此报文，便宣告邻接关系失效。]{style="font-family:宋体"}

[[本命令用来配置]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_x1068_x9952_x2036165956}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，而]{style="font-family:宋体"}[DRB]{lang="EN-US"}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔则为]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[1/3]{lang="EN-US"}[，以保证]{style="font-family:宋体"}[DRB]{lang="EN-US"}[失效后可被快速检测到。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1113284347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_1188026327}[报文的发送间隔与失效数目的乘积不允许超过]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x31505749}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_927483467}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1279318520}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送间隔]{style="font-family:宋体"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x195604223}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill timer hello 20]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1459554095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**[ **timer** **holding-multiplier**]{lang="EN-US"}]{#struct_0_x1068_x9952_x840894265}
:::

::: {#-528109679 .myid}
[]{#_Toc404798010}[]{#struct_0_x1068_x9952_995835748}

**TRILL \-- TRILL配置命令 \-- trill timer holding-multiplier**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **timer** **holding-multiplier**]{lang="EN-US"}]{#struct_0_x1068_x9952_x813690105}[命令用来配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的失效数目。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **timer** **holding-multiplier**]{lang="EN-US"}]{#struct_0_x1068_x9952_x31702357}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x714181659}

[**[trill]{lang="EN-US"}**[ **timer** **holding-multiplier** *count*]{lang="EN-US"}]{#struct_0_x1068_x9952_x1673634439}

[**[undo]{lang="EN-US"}**[ **trill** **holding-multiplier**]{lang="EN-US"}]{#struct_0_x1068_x9952_883057713}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x589049713}

[[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_x935783479}[报文的失效数目为]{style="font-family:宋体"}[3]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1296848720}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x1495813425}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x31636821}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1949071125}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1750710387}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1505895607}

[*[count]{lang="EN-US"}*]{#struct_0_x1068_x9952_x2131334680}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的失效数目，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1439058572}

[[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_1696522746}[报文的发送间隔与失效数目的乘积为]{style="font-family:宋体"}[邻接关系保持时间，即]{style="font-family:宋体"}[RB]{lang="EN-US"}[监测到链路失效并进行路由重计算的时间。]{style="font-family:宋体"}[RB]{lang="EN-US"}[通过]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文将邻接关系保持时间通知给其邻居，若该邻居在邻接关系保持时间内未收到此报文，便宣告邻接关系失效。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1225367811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x1068_x9952_1719693007}[报文的发送间隔与失效数目的乘积不允许超过]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x1574721775}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x31309141}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x529048291}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的失效数目为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1609672004}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill timer holding-multiplier 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_59652721}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[trill]{lang="EN-US"}**[ **timer** **hello**]{lang="EN-US"}]{#struct_0_x1068_x9952_x1642517309}
:::

::: {#-765547089 .myid}
[]{#_Toc404798011}[]{#struct_0_x1068_x9952_x1698051954}

**TRILL \-- TRILL配置命令 \-- trill timer lsp**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **timer** **lsp**]{lang="EN-US"}]{#struct_0_x1068_x9952_x277718797}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送间隔和一次发送的最大数目。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **timer** **lsp**]{lang="EN-US"}]{#struct_0_x1068_x9952_1807375827}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x31243605}

[**[trill]{lang="EN-US"}**[ **timer** **lsp** *interval* \[ **count** *count* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_1826929622}

[**[undo]{lang="EN-US"}**[ **trill** ]{lang="EN-US"}**[timer]{lang="EN-US"}**[ **lsp**]{lang="EN-US"}]{#struct_0_x1068_x9952_403983402}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_330705986}

[[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_1012217045}[的最小发送间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，一次发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大数目为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x542017018}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x2102933149}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_782624151}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_2002751154}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x31833428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x553933648}

[*[interval]{lang="EN-US"}*]{#struct_0_x1068_x9952_1534498072}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_x1068_x9952_851294573}[：表示一次发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_2089581992}

[[为了避免网络中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1068_x9952_1801379750}[老化太频繁，]{style="font-family:宋体"}[RB]{lang="EN-US"}[需要定期发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，以使全网]{style="font-family:宋体"}[RB]{lang="EN-US"}[上的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[和路由计算保持稳定有效。]{style="font-family:宋体"}

[[需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1093614973}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1474680112}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x31767892}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒，一次发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大数目为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1539274677}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill timer lsp 500 count 10]{lang="NO-BOK"}
:::

::: {#923477696 .myid}
[]{#_Toc404798012}[]{#struct_0_x1068_x9952_x1071517797}[]{#_Toc386113421}[]{#_Toc385854419}[]{#_Toc379615171}[]{#_Toc379555239}[]{#_Toc378607611}

**TRILL \-- TRILL配置命令 \-- trill track**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **track**]{lang="EN-US"}]{#struct_0_x1068_x9952_604836132}[命令用来配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[监测的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **track**]{lang="EN-US"}]{#struct_0_x1068_x9952_665426507}[命令用来取消]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[监测的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x448479161}

[**[trill]{lang="EN-US"}**[ **track**]{lang="EN-US"}[ *track-entry-number*]{lang="EN-US"}]{#struct_0_x1068_x9952_1136995015}

[**[undo]{lang="EN-US"}**[ **trill** **track**]{lang="EN-US"}]{#struct_0_x1068_x9952_286772462}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1867782554}

[[TRILL]{lang="EN-US"}]{#struct_0_x1068_x9952_x1232585562}[未监测任何]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_827523908}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1068_x9952_x1993394841}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1657365558}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1797578287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x788876487}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1142083925}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_x1068_x9952_x398554998}[：表示]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1967061115}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_866830438}[在]{style="font-family:宋体"}[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[监测]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_x435404759}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] trill track 10]{lang="EN-US"}
:::

::: {#1784025601 .myid}
[]{#_Toc350777203}[]{#_Toc350774958}[]{#_Toc404798013}[]{#struct_0_x1068_x9952_973739774}[]{#_Toc350777204}[]{#_Toc350774959}

**TRILL \-- TRILL配置命令 \-- trill vr ipv6 vrid**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **vr** **ipv6** ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1644833416}**[vrid]{lang="EN-US"}**[命令用来创建]{style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[并为其配置]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **vr** **ipv6** ]{lang="EN-US"}]{#struct_0_x1068_x9952_973805310}**[vrid]{lang="EN-US"}**[命令用来删除指定的]{style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[，或为其删除一个]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1998235453}

[**[trill]{lang="EN-US"}**[ **vr** **ipv6** **vrid** *vr-id* **virtual-ip** *virtual-address* \[ **link-local** \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x456935741}

[**[undo]{lang="EN-US"}**[ **trill** **vr** **ipv6** **vrid** *vr-id* **virtual-ip** \[ *virtual-address* \[ **link-local** \] \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x863392797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x615118302}

[[不存在任何]{style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_973870846}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_828037043}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_1096061273}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1756619799}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1466324244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_1828791895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_973936382}

[*[vr-id]{lang="EN-US"}*]{#struct_0_x1068_x9952_1970776030}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[virtual-address]{lang="EN-US"}*]{#struct_0_x1068_x9952_x609554357}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，必须为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址。如果未指定本参数，表示删除该]{style="font-family:宋体"}[VR]{lang="EN-US"}[中的所有虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[link-local]{lang="EN-US"}**]{#struct_0_x1068_x9952_1587856305}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址。当虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址时，必须指定本参数；当虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址，则不得指定本参数，否则系统都将提示出错。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1545166751}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x78356742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[trill]{lang="EN-US"}**[ **vr** **ipv6** ]{lang="EN-US"}]{#struct_0_x1068_x9952_x657815529}**[vrid]{lang="EN-US"}**[命令时，]{lang="EN-US" style="font-family:宋体"}[如果指定编号的]{lang="EN-US" style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[不存在，则创建一个新的]{lang="EN-US" style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[；如果指定编号的]{lang="EN-US" style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[已存在，则为其]{lang="EN-US" style="font-family:宋体"}[更新或]{style="font-family:宋体"}[添加一个]{lang="EN-US" style="font-family:宋体"}[虚拟]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[（对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址]{lang="EN-US" style="font-family:宋体"}[是更新，对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址]{lang="EN-US" style="font-family:宋体"}[是添加）]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在一个]{style="font-family:宋体"}]{#struct_0_x1068_x9952_974001918}[VLAN]{lang="EN-US"}[接口上必须且只能]{style="font-family:宋体"}[为一个]{style="font-family:宋体"}[VR]{lang="EN-US"}[配置一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址；]{style="font-family:宋体"}[为]{style="font-family:宋体"}[VR]{lang="EN-US"}[配置的第一个虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址必须为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址，且]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址必须被最后一个删除。否则，系统都将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在一个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x624592168}[接口上最多可配置]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[个]{lang="EN-US" style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[，且所有]{lang="EN-US" style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[的虚拟]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址总数不得超过]{lang="EN-US" style="font-family:宋体"}[16]{lang="EN-US"}[个。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1531712908}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1487617533}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上]{style="font-family:宋体"}[先创建]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[TRILL VR]{lang="EN-US"}[ 2]{lang="EN-US"}[并为其配置]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[FE80::1]{lang="EN-US"}[，然后再为其]{style="font-family:宋体"}[添加一个虚拟]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_974067454}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] trill vr ipv6 vrid 2 virtual-ip fe80::1 link-local]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] trill vr ipv6 vrid 2 virtual-ip 1::1]{lang="EN-US"}
:::

::: {#1471538856 .myid}
[]{#_Toc404798014}[]{#struct_0_x1068_x9952_1776979659}

**TRILL \-- TRILL配置命令 \-- trill vr vrid**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **vr** ]{lang="EN-US"}]{#struct_0_x1068_x9952_x1879041425}**[vrid]{lang="EN-US"}**[命令用来创建]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[并为其配置]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **vr** **vrid**]{lang="EN-US"}]{#struct_0_x1068_x9952_464217546}[命令用来删除指定的]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[，或为其删除一个]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1619930978}

[**[trill]{lang="EN-US"}**[ **vr** **vrid** *vr-id* **virtual-ip** *virtual-address*]{lang="EN-US"}]{#struct_0_x1068_x9952_x412130052}

[**[undo]{lang="EN-US"}**[ **trill** **vr** **vrid** *vr-id* **virtual-ip** \[ *virtual-address* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_974132990}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1754432653}

[[不存在任何]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_547815953}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x475985296}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_900686014}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1714535810}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_974198526}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x164297477}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1597001944}

[*[vr-id]{lang="EN-US"}*]{#struct_0_x1068_x9952_866378773}[：表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[virtual-address]{lang="EN-US"}*]{#struct_0_x1068_x9952_x823288435}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，必须为合法的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址（]{style="font-family:宋体"}[A]{lang="EN-US"}[、]{style="font-family:宋体"}[B]{lang="EN-US"}[、]{style="font-family:
宋体"}[C]{lang="EN-US"}[类地址，不包括全零、广播和环回地址）。如果未指定本参数，表示删除该]{style="font-family:宋体"}[VR]{lang="EN-US"}[中的所有虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1857856907}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1068_x9952_1497784059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2022872985}**[trill]{lang="EN-US"}**[ **vr** ]{lang="EN-US"}**[vrid]{lang="EN-US"}**[命令时，]{style="font-family:宋体"}[如果指定编号的]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[不存在，则创建一个新的]{style="font-family:宋体"}[IPv4 TRILL]{lang="EN-US"}[ VR]{lang="EN-US"}[；如果指定编号的]{style="font-family:
宋体"}[IPv4 TRILL ]{lang="EN-US"}[VR]{lang="EN-US"}[已存在，则为其添加一个]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x1068_x9952_974264062}[VLAN]{lang="EN-US"}[接口上最多可配置]{style="font-family:宋体"}[4]{lang="EN-US"}[个]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[，且所有]{style="font-family:宋体"}[IPv4 TRILL]{lang="EN-US"}[ VR]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址总数不得超过]{style="font-family:宋体"}[16]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1874435783}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_x2052925509}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上]{style="font-family:宋体"}[先创建]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[TRILL]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[VR]{lang="EN-US"}[ 1]{lang="EN-US"}[并为其配置]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，然后再为其]{style="font-family:宋体"}[添加一个虚拟]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[10.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1662458884}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] trill vr vrid 1 virtual-ip 10.1.1.1]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] trill vr vrid 1 virtual-ip 10.1.1.2]{lang="EN-US"}
:::

::: {#2083220729 .myid}
[]{#_Toc404798015}[]{#struct_0_x1068_x9952_863415927}[]{#_Toc350777205}

**TRILL \-- TRILL配置命令 \-- trill vr vrid track**

------------------------------------------------------------------------

[**[trill]{lang="EN-US"}**[ **vr** **vrid** **track**]{lang="EN-US"}]{#struct_0_x1068_x9952_973674239}[命令用来配置]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[监测的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **trill** **vr** **vrid** **track**]{lang="EN-US"}]{#struct_0_x1068_x9952_218569742}[命令用来取消]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[监测的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x837629694}

[**[trill]{lang="EN-US"}**[ **vr** \[ **ipv6** \] **vrid**]{lang="EN-US"}[ *vr-id* **track** *track-entry-number*]{lang="EN-US"}]{#struct_0_x1068_x9952_x964750567}

[**[undo]{lang="EN-US"}**[ **trill** **vr** \[ **ipv6** \] **vrid**]{lang="EN-US"}[ *vr-id* **track** \[ *track-entry-number* \]]{lang="EN-US"}]{#struct_0_x1068_x9952_x1767562907}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1727027532}

[[TRILL VR]{lang="EN-US"}]{#struct_0_x1068_x9952_973739775}[未监测任何]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x1644833417}

[[VLAN]{lang="EN-US"}]{#struct_0_x1068_x9952_x284245405}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_x378172593}

[[network-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_x599725269}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1068_x9952_690848794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_973805311}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x1068_x9952_1998235454}[：表示]{style="font-family:宋体"}[IPv6 TRILL VR]{lang="EN-US"}[。如果未指定本参数，表示]{style="font-family:宋体"}[IPv4 TRILL VR]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vr-id]{lang="EN-US"}*]{#struct_0_x1068_x9952_x456476989}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VR]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_x1068_x9952_x1965541649}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。如果未指定本参数，表示取消监测所有]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_1322735389}

[[需要注意的是，如果]{style="font-family:宋体"}]{#struct_0_x1068_x9952_x2093427290}[当前接口下不存在指定的]{style="font-family:宋体"}[TRILL VR]{lang="EN-US"}[，或一个]{style="font-family:宋体"}[VR]{lang="EN-US"}[监测]{style="font-family:宋体"}[了超过]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[，均将导致配置失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1068_x9952_973870847}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_828037042}[在]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[IPv4 TRILL VR 1]{lang="EN-US"}[监测]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_1096061274}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] trill vr vrid 1 track 8]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1068_x9952_1756292119}[在]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[IPv6 TRILL VR 2]{lang="EN-US"}[监测]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1068_x9952_973936383}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] trill vr ipv6 vrid 2 track 9]{lang="EN-US"}
:::
