::: {#-1312030200 .myid}
[]{#_Toc404796188}[]{#struct_0_20797_15055_x2133004601}[]{#_Toc143664282}

**Track \-- Track配置命令 \-- display track**

------------------------------------------------------------------------

[**[display track]{lang="EN-US"}**]{#struct_0_20797_15055_x1985275026}[命令用来显示]{style="font-family:宋体"}[Track]{lang="EN-US"}[项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_x411219120}

[**[display track]{lang="EN-US" style="color:windowtext"}**]{#struct_0_20797_15055_838664758}[ { *track-entry-number*]{lang="EN-US" style="color:windowtext"}**[ ]{lang="EN-US" style="color:windowtext"}**[\| ]{lang="EN-US" style="color:windowtext"}**[all ]{lang="EN-US" style="color:windowtext"}**[}]{lang="EN-US" style="color:windowtext"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20797_15055_870182546}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20797_15055_x412056185}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20797_15055_x46286105}

[[network-admin]{lang="EN-US"}]{#struct_0_20797_15055_1319933534}

[[network-operator]{lang="EN-US"}]{#struct_0_20797_15055_1368801959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20797_15055_1957939042}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20797_15055_x299543509}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1647785931}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_x52685202}[：显示指]{style="font-family:宋体"}[定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_20797_15055_646441747}[：显示所有]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项的信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20797_15055_1543661063}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_x2106476504}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_944899010}[显示所有]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display track all]{lang="EN-US"}]{#struct_0_20797_15055_1369260711}

[Track ID: 1]{lang="EN-US"}

[  State: Positive]{lang="EN-US"}

[  Duration: 0 days 0 hours 0 minutes 7 seconds]{lang="EN-US"}

[  Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}

[  Tracked object]{lang="EN-US"}[：]{style="font-family:宋体"}

[    NQA entry: admin test ]{lang="EN-US"}

[    Reaction: 10]{lang="EN-US"}

[Track ID: 2]{lang="EN-US"}

[  State: NotReady]{lang="EN-US"}

[  Duration: 0 days 0 hours 0 minutes 32 seconds]{lang="EN-US"}

[  Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}

[  Tracked object:]{lang="EN-US"}

[    BFD session mode: Echo]{lang="EN-US"}

[    Outgoing interface: GigabitEthernet1/0/1]{lang="EN-US"}

[    VPN instance name: -]{lang="EN-US"}

[    Remote IP: 192.168.40.1]{lang="EN-US"}

[    Local IP: 192.168.40.2]{lang="EN-US"}

[Track ID: 3]{lang="EN-US"}

[  State: Negative]{lang="EN-US"}

[  Duration: 0 days 0 hours 0 minutes 32 seconds]{lang="EN-US"}

[  Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}

[  Tracked object:]{lang="EN-US"}

[    Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Protocol: IPv4]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_2018857997}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_1369195175}[显示所有]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display track all]{lang="EN-US"}]{#struct_0_20797_15055_1369129639}

[Track ID: 1]{lang="EN-US"}

[  State: Positive]{lang="EN-US"}

[  Duration: 0 days 0 hours 0 minutes 7 seconds]{lang="EN-US"}

[  Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}

[  Tracked object]{lang="EN-US"}[：]{style="font-family:宋体"}

[    NQA entry: admin test ]{lang="EN-US"}

[    Reaction: 10]{lang="EN-US"}

[Track ID: 2]{lang="EN-US"}

[  State: NotReady]{lang="EN-US"}

[  Duration: 0 days 0 hours 0 minutes 32 seconds]{lang="EN-US"}

[  Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}

[  Tracked object:]{lang="EN-US"}

[    BFD session mode: Echo]{lang="EN-US"}

[    Outgoing interface: Vlan-interface2]{lang="EN-US"}

[    VPN instance name: -]{lang="EN-US"}

[    Remote IP: 192.168.40.1]{lang="EN-US"}

[    Local IP: 192.168.40.2]{lang="EN-US"}

[Track ID: 3]{lang="EN-US"}

[  State: Negative]{lang="EN-US"}

[  Duration: 0 days 0 hours 0 minutes 32 seconds]{lang="EN-US"}

[  Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}

[  Tracked object:]{lang="EN-US"}

[    Interface:  Vlan-interface3]{lang="EN-US"}

[    Protocol: IPv4]{lang="EN-US"}

[Track ID: 4]{lang="EN-US"}

[  State: Negative]{lang="EN-US"}

[  Duration: 0 days 0 hours 0 minutes 32 seconds]{lang="EN-US"}

[  Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}

[  Tracked object:]{lang="EN-US"}

[    CFD service instance: 1, MEP ID: 2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display track]{lang="EN-US"}]{#struct_0_20797_15055_x1867898001}[命令输出信息描述]{style="font-family:黑体"}

[]{#table_struct_0_1497504083}[[字段]{style="font-family:黑体"}]{#struct_0_20797_15055_x2078687551}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20797_15055_1494992928}

[[Track ID]{lang="EN-US"}]{#struct_0_20797_15055_x1104449970}

[[Track]{lang="EN-US"}]{#struct_0_20797_15055_63686433}[项序号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_20797_15055_1149149429}

[[Track]{lang="EN-US"}]{#struct_0_20797_15055_1369064103}[项的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Positive]{lang="EN-US"}]{#struct_0_20797_15055_431695416}[：表示状态正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NotReady]{lang="EN-US"}]{#struct_0_20797_15055_1581957443}[：表示无效值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Negative]{lang="EN-US"}]{#struct_0_20797_15055_1131926559}[：表示状态异常]{lang="EN-US" style="font-family:宋体"}

[[Duration]{lang="EN-US"}]{#struct_0_20797_15055_1369522855}

[[Track]{lang="EN-US"}]{#struct_0_20797_15055_x1166853028}[项处于当前状态的持续时间]{style="font-family:宋体"}

[[Notification delay: Positive 20, Negative 30 (in seconds)]{lang="EN-US"}]{#struct_0_20797_15055_525448676}

[[通知延迟：]{style="font-family:宋体"}]{#struct_0_20797_15055_x201172747}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_501090213}[项状态变为]{lang="EN-US" style="font-family:宋体"}[Positive]{lang="EN-US"}[后，延迟]{lang="EN-US" style="font-family:宋体"}[20]{lang="EN-US"}[秒通知应用模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_1931217379}[项状态变为]{lang="EN-US" style="font-family:宋体"}[Negative]{lang="EN-US"}[后，延迟]{lang="EN-US" style="font-family:宋体"}[30]{lang="EN-US"}[秒通知应用模块]{lang="EN-US" style="font-family:宋体"}

[[Tracked object]{lang="EN-US"}]{#struct_0_20797_15055_1369457319}

[[Track]{lang="EN-US"}]{#struct_0_20797_15055_408191876}[项关联的对象]{style="font-family:宋体"}

[[NQA entry]{lang="EN-US"}]{#struct_0_20797_15055_x285426612}

[[Track]{lang="EN-US"}]{#struct_0_20797_15055_1204629023}[项关联的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组]{style="font-family:宋体"}

[[Reaction]{lang="EN-US"}]{#struct_0_20797_15055_x1358349031}

[[Track]{lang="EN-US"}]{#struct_0_20797_15055_1336776316}[项关联的联动项]{style="font-family:宋体"}

[[BFD session mode]{lang="EN-US"}]{#struct_0_20797_15055_1368998568}

[[BFD]{lang="EN-US"}]{#struct_0_20797_15055_852143567}[会话的模式，当前只支持]{style="font-family:宋体"}[Echo]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[Outgoing interface]{lang="EN-US"}]{#struct_0_20797_15055_x519049424}

[[BFD]{lang="EN-US"}]{#struct_0_20797_15055_x679738889}[会话报文的出接口]{style="font-family:宋体"}

[[VPN instance name]{lang="EN-US"}]{#struct_0_20797_15055_1368933032}

[[BFD]{lang="EN-US"}]{#struct_0_20797_15055_x757354379}[会话报文所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称。如果属于公网，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Remote IP]{lang="EN-US"}]{#struct_0_20797_15055_378085332}

[[BFD]{lang="EN-US"}]{#struct_0_20797_15055_584251626}[会话报文的远端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Local IP]{lang="EN-US"}]{#struct_0_20797_15055_847345559}

[[BFD]{lang="EN-US"}]{#struct_0_20797_15055_1368867496}[会话报文的本地]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_20797_15055_818578184}

[[Track]{lang="EN-US"}]{#struct_0_20797_15055_2688399}[项关联的接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_20797_15055_x1986709740}

[[监视接口的链路状态或网络层协议状态，取值包括：]{style="font-family:宋体"}]{#struct_0_20797_15055_1368801960}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_20797_15055_1958397797}[：监视接口的链路状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4]{lang="EN-US"}]{#struct_0_20797_15055_1169945840}[：监视三层接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_20797_15055_x1431529040}[：监视三层接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议状态]{style="font-family:宋体"}

[[CFD service instance]{lang="EN-US"}]{#struct_0_20797_15055_1369260712}

[[CFD]{lang="EN-US"}]{#struct_0_20797_15055_2018661389}[服务实例的编号]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_20797_15055_1374848067}

[[CFD MEP]{lang="EN-US"}]{#struct_0_20797_15055_x253063379}[的编号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1218669615}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[track bfd]{lang="EN-US"}**]{#struct_0_20797_15055_1369195176}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[track cfd]{lang="EN-US"}**]{#struct_0_20797_15055_x1160602953}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[track interface]{lang="EN-US"}**]{#struct_0_20797_15055_x994067189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[track interface protocol]{lang="EN-US"}**]{#struct_0_20797_15055_607820244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[track nqa]{lang="EN-US"}**]{#struct_0_20797_15055_1707933818}

::::: {#529609930 .myid}
[]{#_Toc404796189}[]{#struct_0_20797_15055_x805786074}[]{#_Toc291059019}[]{#_Toc164831185}

**Track \-- Track配置命令 \-- track bfd**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Track命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_20797_15055_x1845044550}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_20797_15055_252553645}
:::

[ ]{lang="EN-US"}

[**[track bfd]{lang="EN-US"}**]{#struct_0_20797_15055_x402571696}[命令用来创建和]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo track]{lang="EN-US"}**]{#struct_0_20797_15055_1369129640}[命令用来删除指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1868487820}

[**[track ]{lang="EN-US"}***[track-entry-number ]{lang="EN-US"}***[bfd echo interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}***[ remote ip ]{lang="EN-US"}***[remote-ip ]{lang="EN-US"}***[local ip ]{lang="EN-US"}***[local-ip ]{lang="EN-US"}*[\[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* \]]{lang="EN-US"}]{#struct_0_20797_15055_1641370250}

[**[undo track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_x361020421}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1729879966}

[[设备上不存在任何]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x1400878425}[项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1116906465}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20797_15055_450316707}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20797_15055_x382374827}

[[network-admin]{lang="EN-US"}]{#struct_0_20797_15055_1369064104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20797_15055_432023096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20797_15055_x380625115}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_454921266}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_20797_15055_x970373672}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话报文的]{style="font-family:宋体"}[出接口。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[**[remote ip]{lang="EN-US"}***[ remote-ip]{lang="EN-US"}*]{#struct_0_20797_15055_1778742976}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话探测的远端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[local ip]{lang="EN-US"}***[ local-ip]{lang="EN-US"}*]{#struct_0_20797_15055_1402543572}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话探测的本地]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}**]{#struct_0_20797_15055_x1709527385}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态发生变化时，延迟通知应用模块。如果不指定该参数，则]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变化后立即通知应用模块。]{style="font-family:宋体"}

[**[negative]{lang="EN-US"}**[ *negative-time*]{lang="EN-US"}]{#struct_0_20797_15055_x1704360487}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，延迟通知应用模块的时间。]{style="font-family:宋体"}*[negative-time]{lang="EN-US"}*[为延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[positive]{lang="EN-US"}**[ *positive-time*]{lang="EN-US"}]{#struct_0_20797_15055_1369522856}[：指定]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}[项状态变为]{lang="EN-US" style="font-family:
宋体"}[Positive]{lang="EN-US"}[时，延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}*[positive-time]{lang="EN-US"}*[为延迟时间，取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1167049636}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_409740556}[项创建后，不能通过重复执行]{style="font-family:宋体"}**[track]{lang="EN-US"}**[命令的方式修改]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联的内容。]{style="font-family:宋体"}[只能删除]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项后，再重新创建]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_1390322177}[项创建后，可以通过再次执行]{lang="EN-US" style="font-family:宋体"}**[track bfd delay]{lang="EN-US"}**[命令的方式修改延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_20797_15055_x163549287}[Track]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动时，]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能作为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话探测的本地地址和远端地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20797_15055_1430909168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_157238323}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_x1520129599}[创建与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}[BFD]{lang="EN-US"}[会话使用]{style="font-family:宋体"}[Echo]{lang="EN-US"}[报文进行探测，出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，远端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.40.1]{lang="EN-US"}[，本地]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.40.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_2078573438}

[\[Sysname\] track 1 bfd echo interface gigabitethernet 1/0/1 remote ip 192.168.40.1 local ip 192.168.40.2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_x1032282815}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_1369457320}[创建与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}[BFD]{lang="EN-US"}[会话使用]{style="font-family:宋体"}[Echo]{lang="EN-US"}[报文进行探测，出接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[ 2]{lang="EN-US"}[，远端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，本地]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_408781703}

[\[Sysname\] track 1 bfd echo interface vlan-interface 2 remote ip 1.1.1.1 local ip 1.1.1.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1103118633}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display track]{lang="EN-US"}**]{#struct_0_20797_15055_x2105132493}
:::::

::::: {#2095693871 .myid}
[]{#_Toc404796190}[]{#struct_0_20797_15055_x585934831}

**Track \-- Track配置命令 \-- track cfd**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Track命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_20797_15055_x667740229}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_20797_15055_x607575708}
:::

[ ]{lang="EN-US"}

[**[track cfd]{lang="EN-US"}**]{#struct_0_20797_15055_x2102052791}[命令用来创建和]{style="font-family:宋体"}[CFD]{lang="EN-US"}[连续性检测功能]{style="font-family:宋体"}[关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo track]{lang="EN-US"}**]{#struct_0_20797_15055_x268210021}[命令用来删除指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1359884784}

[**[track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}***[ cfd cc service-instance ]{lang="EN-US"}***[instance-id ]{lang="EN-US"}***[mep ]{lang="EN-US"}***[mep-id ]{lang="EN-US"}*[\[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* \]]{lang="EN-US"}]{#struct_0_20797_15055_x1372981437}

[**[undo track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_x2029622568}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20797_15055_298922967}

[[设备上不存在任何]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x2112275859}[项。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20797_15055_879560060}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20797_15055_843215379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20797_15055_856400741}

[[network-admin]{lang="EN-US"}]{#struct_0_20797_15055_1331731856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20797_15055_x1359950320}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20797_15055_1535388092}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_1633008140}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_20797_15055_x882656778}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_20797_15055_1594371683}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}**]{#struct_0_20797_15055_1012917292}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态发生变化时，延迟通知应用模块。如果不指定该参数，则]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变化后立即通知应用模块。]{style="font-family:宋体"}

[**[negative]{lang="EN-US"}**[ *negative-time*]{lang="EN-US"}]{#struct_0_20797_15055_x159352670}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，延迟通知应用模块的时间。]{style="font-family:宋体"}*[negative-time]{lang="EN-US"}*[为延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[positive]{lang="EN-US"}**[ *positive-time*]{lang="EN-US"}]{#struct_0_20797_15055_609356025}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[时，延迟通知应用模块的时间。]{style="font-family:宋体"}*[positive-time]{lang="EN-US"}*[为延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20797_15055_x328910242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x167706183}[项创建后，不能通过重复执行]{style="font-family:宋体"}**[track]{lang="EN-US"}**[命令的方式修改]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联的内容。]{style="font-family:宋体"}[只能删除]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项后，再重新创建]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x1360015856}[项创建后，可以通过再次执行]{lang="EN-US" style="font-family:宋体"}**[track ]{lang="EN-US"}[cfd]{lang="EN-US"}[ delay]{lang="EN-US"}**[命令的方式修改延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20797_15055_x337050630}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_566288816}[创建与]{style="font-family:宋体"}[CFD]{lang="EN-US"}[连续性检测功能关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。指定]{style="font-family:
宋体"}[CFD]{lang="EN-US"}[服务实例]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:宋体"}[MEP]{lang="EN-US"}[编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_409115781}

[\[Sysname\] track 1 cfd cc service-instance 2 mep 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_991672291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[d]{lang="EN-US"}[isplay track]{lang="EN-US"}**]{#struct_0_20797_15055_1501510039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd mep]{lang="EN-US"}**]{#struct_0_20797_15055_x262593721}[（]{style="font-family:
宋体"}[可靠性]{lang="EN-US" style="font-family:宋体"}[命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[CFD]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd service-instance]{lang="EN-US"}**]{#struct_0_20797_15055_266370804}[（]{style="font-family:宋体"}[可靠性]{lang="EN-US" style="font-family:宋体"}[命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[CFD]{lang="EN-US"}[）]{style="font-family:宋体"}
:::::

::: {#-1690495116 .myid}
[]{#_Toc404796191}[]{#struct_0_20797_15055_x1409777516}[]{#_Toc291059021}[]{#_Toc376781244}[]{#_Toc376781245}[]{#_Toc376781246}[]{#_Toc376781247}[]{#_Toc376781248}[]{#_Toc376781249}[]{#_Toc376781250}[]{#_Toc376781251}[]{#_Toc376781252}[]{#_Toc376781253}[]{#_Toc376781254}[]{#_Toc376781255}[]{#_Toc376781256}[]{#_Toc376781257}[]{#_Toc376781258}[]{#_Toc376781259}[]{#_Toc376781260}[]{#_Toc376781261}[]{#_Toc376781262}[]{#_Toc376781263}[]{#_Toc376781264}[]{#_Toc376781265}[]{#_Toc376781266}[]{#_Toc376781267}[]{#_Toc376781268}[]{#_Toc376781269}[]{#_Toc376781270}[]{#_Toc376781271}[]{#_Toc376781272}[]{#_Toc376781273}[]{#_Toc376781274}[]{#_Toc376781275}

**Track \-- Track配置命令 \-- track interface**

------------------------------------------------------------------------

[**[track interface]{lang="EN-US"}**]{#struct_0_20797_15055_1216991748}[命令用来创建与指定接口链路状态关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo track]{lang="EN-US"}**]{#struct_0_20797_15055_x2137878681}[命令用来删除指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_1150509423}

[**[track ]{lang="EN-US"}***[track-entry-number ]{lang="EN-US"}***[interface ]{lang="EN-US"}***[interface-type interface-number ]{lang="EN-US"}*[\[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* \]]{lang="EN-US"}]{#struct_0_20797_15055_1141658793}

[**[undo track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_1379395699}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20797_15055_936678132}

[[设备上不存在任何]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x1359819248}[项。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20797_15055_1826006223}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20797_15055_x309638484}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20797_15055_868062852}

[[network-admin]{lang="EN-US"}]{#struct_0_20797_15055_x1495471106}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20797_15055_x211758716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20797_15055_x976062567}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_967830223}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_20797_15055_1662073956}[：监视的接口类型和接口编号。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}**]{#struct_0_20797_15055_x1359360496}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态发生变化时，延迟通知应用模块。如果不指定该参数，则]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变化后立即通知应用模块。]{style="font-family:宋体"}

[**[negative]{lang="EN-US"}**[ *negative-time*]{lang="EN-US"}]{#struct_0_20797_15055_x910467256}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，延迟通知应用模块的时间。]{style="font-family:宋体"}*[negative-time]{lang="EN-US"}*[为延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[positive]{lang="EN-US"}**[ *positive-time*]{lang="EN-US"}]{#struct_0_20797_15055_x908179653}[：指定]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}[项状态变为]{lang="EN-US" style="font-family:
宋体"}[Positive]{lang="EN-US"}[时，延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}*[positive-time]{lang="EN-US"}*[为延迟时间，取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1215624625}

[[创建与接口链路状态关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x1159587085}[项后，接口的链路状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[；接口的链路状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[时，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[。通过]{style="font-family:宋体"}**[display ip interface brief]{lang="EN-US"}**[命令可以查看接口的链路状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_20797_15055_452269311}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_857505138}[项创建后，不能通过重复执行]{style="font-family:宋体"}**[track]{lang="EN-US"}**[命令的方式修改]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联的内容。]{style="font-family:宋体"}[只能删除]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项后，再重新创建]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_348969468}[项创建后，可以通过再次执行]{lang="EN-US" style="font-family:宋体"}**[track interface delay]{lang="EN-US"}**[命令的方式修改延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20797_15055_1538736534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_x1359426032}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_41046436}[创建与接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的链路状态关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_1529454325}

[\[Sysname\] track 1 interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_877945073}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_x1275965908}[创建与]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的链路状态关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_x546654544}

[\[Sysname\] track 1 interface vlan-interface 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_x21741785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display track]{lang="EN-US"}**]{#struct_0_20797_15055_x2129574085}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip interface brief]{lang="EN-US"}**]{#struct_0_20797_15055_x1806463161}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[地址）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#227704649 .myid}
[]{#_Toc404796192}[]{#struct_0_20797_15055_x1359884783}[]{#_Toc291059022}

**Track \-- Track配置命令 \-- track interface protocol**

------------------------------------------------------------------------

[**[track interface protocol]{lang="EN-US"}**]{#struct_0_20797_15055_x969696910}[命令用来创建与指定接口网络层协议状态关联的]{style="font-family:
宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo track]{lang="EN-US"}**]{#struct_0_20797_15055_x517874393}[命令用来删除指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_1461626261}

[**[track ]{lang="EN-US"}***[track-entry-number ]{lang="EN-US"}***[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}***[ protocol ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* \]]{lang="EN-US"}]{#struct_0_20797_15055_x1322512602}

[**[undo track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_765520587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1206795192}

[[设备上不存在任何]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_600928755}[项。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1887083527}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20797_15055_x1359950319}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20797_15055_325337903}

[[network-admin]{lang="EN-US"}]{#struct_0_20797_15055_x1275048854}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20797_15055_x367775883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20797_15055_2129291382}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_1896913856}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_20797_15055_x803276358}[：监视的接口类型和接口编号。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_20797_15055_x561456655}[：监视接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议状态。接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[；接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[时，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[。通过]{style="font-family:宋体"}**[display ip interface brief]{lang="EN-US"}**[命令可以查看接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议状态。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_20797_15055_2004868330}[：监视接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议状态。接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[；接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[时，]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[。通过]{style="font-family:宋体"}**[display ipv6 interface brief]{lang="EN-US"}**[命令可以查看接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议状态。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}**]{#struct_0_20797_15055_x2005288132}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态发生变化时，延迟通知应用模块。如果不指定该参数，则]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变化后立即通知应用模块。]{style="font-family:宋体"}

[**[negative]{lang="EN-US"}**[ *negative-time*]{lang="EN-US"}]{#struct_0_20797_15055_x1360015855}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，延迟通知应用模块的时间。]{style="font-family:宋体"}*[negative-time]{lang="EN-US"}*[为延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[positive]{lang="EN-US"}**[ *positive-time*]{lang="EN-US"}]{#struct_0_20797_15055_1229033311}[：指定]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}[项状态变为]{lang="EN-US" style="font-family:
宋体"}[Positive]{lang="EN-US"}[时，延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}*[positive-time]{lang="EN-US"}*[为延迟时间，取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1142320720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_473863823}[项创建后，不能通过重复执行]{style="font-family:宋体"}**[track]{lang="EN-US"}**[命令的方式修改]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联的内容。]{style="font-family:宋体"}[只能删除]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项后，再重新创建]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_1203873202}[项创建后，可以通过再次执行]{lang="EN-US" style="font-family:宋体"}**[track interface protocol delay]{lang="EN-US"}**[命令的方式修改延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20797_15055_1541123655}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_367054622}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_x1700075383}[创建与接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议状态关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_1368851023}

[\[Sysname\] track 1 interface gigabitethernet 1/0/1 protocol ipv4]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20797_15055_x1360081391}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_x1570132231}[创建与]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议状态关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_x507987011}

[\[Sysname\] track 1 interface vlan-interface 2 protocol ipv4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_119820182}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip interface brief]{lang="EN-US"}**]{#struct_0_20797_15055_x993270702}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[地址）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 interface brief]{lang="EN-US"}**]{#struct_0_20797_15055_x1601428093}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/IPv6]{lang="EN-US"}[基础）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display track]{lang="EN-US"}**]{#struct_0_20797_15055_948260547}
:::

::::: {#1726721035 .myid}
[]{#_Toc404796193}[]{#struct_0_20797_15055_1602557130}

**Track \-- Track配置命令 \-- track nqa**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Track命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_20797_15055_1236107544}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_20797_15055_348698415}
:::

[ ]{lang="EN-US"}

[**[track nqa]{lang="EN-US"}**]{#struct_0_20797_15055_x1419493318}[命令用来创建与]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组中指定联动项关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo track]{lang="EN-US"}**]{#struct_0_20797_15055_x1363919762}[命令用来删除指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1079561696}

[**[track ]{lang="EN-US"}***[track-entry-number ]{lang="EN-US"}***[nqa entry ]{lang="EN-US"}***[admin-name]{lang="EN-US"}*[ *operation-tag* **reaction** *item-number* \[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* \]]{lang="EN-US"}]{#struct_0_20797_15055_x2073764059}

[**[undo track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_1602622666}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20797_15055_2047883883}

[[设备上不存在任何]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x739786310}[项。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20797_15055_x1078199938}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20797_15055_x824582796}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20797_15055_x190518664}

[[network-admin]{lang="EN-US"}]{#struct_0_20797_15055_1593606448}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20797_15055_1502298524}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20797_15055_1135462657}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_20797_15055_x403046968}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[entry ]{lang="EN-US"}***[admin-name operation-tag]{lang="EN-US"}*]{#struct_0_20797_15055_1818745266}[：指定与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组。其中，]{style="font-family:宋体"}*[admin-name]{lang="EN-US"}*[为创建]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组的管理员的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写；]{style="font-family:宋体"}*[operation-tag]{lang="EN-US"}*[为]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试操作的标签，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[reaction ]{lang="EN-US"}***[item-number]{lang="EN-US"}*]{#struct_0_20797_15055_1862820507}[：指定与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联的联动项。其中，]{style="font-family:宋体"}*[item-number]{lang="EN-US"}*[为联动项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[delay]{lang="EN-US"}**]{#struct_0_20797_15055_940790468}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态发生变化时，延迟通知应用模块。如果不指定该参数，则]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变化后立即通知应用模块。]{style="font-family:宋体"}

[**[negative]{lang="EN-US"}**[ *negative-time*]{lang="EN-US"}]{#struct_0_20797_15055_1931875647}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态变为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，延迟通知应用模块的时间。]{style="font-family:宋体"}*[negative-time]{lang="EN-US"}*[为延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[positive]{lang="EN-US"}**[ *positive-time*]{lang="EN-US"}]{#struct_0_20797_15055_403361040}[：指定]{lang="EN-US" style="font-family:
宋体"}[Track]{lang="EN-US"}[项状态变为]{lang="EN-US" style="font-family:
宋体"}[Positive]{lang="EN-US"}[时，延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}*[positive-time]{lang="EN-US"}*[为延迟时间，取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20797_15055_x2003304226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_1603474634}[项创建后，不能通过重复执行]{style="font-family:宋体"}**[track]{lang="EN-US"}**[命令的方式修改]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联的内容。]{style="font-family:宋体"}[只能删除]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项后，再重新创建]{lang="EN-US" style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Track]{lang="EN-US"}]{#struct_0_20797_15055_x1498221100}[项创建后，可以通过再次执行]{lang="EN-US" style="font-family:宋体"}**[track nqa delay]{lang="EN-US"}**[命令的方式修改延迟通知应用模块的时间。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20797_15055_1985653900}

[[\# ]{lang="EN-US"}]{#struct_0_20797_15055_1307574933}[创建与]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组（]{style="font-family:宋体"}[admin--test]{lang="EN-US"}[）中联动项]{style="font-family:宋体"}[3]{lang="EN-US"}[关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20797_15055_x2091256398}

[\[Sysname\] track 1 nqa entry admin test reaction 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20797_15055_850085854}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display track]{lang="EN-US"}**]{#struct_0_20797_15055_892855126}
:::::
