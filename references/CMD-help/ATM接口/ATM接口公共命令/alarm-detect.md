::::: {#1725110147 .myid}
[]{#_Toc296086815}[]{#_Toc295480285}[]{#_Toc295465879}[]{#_Toc404783968}[]{#struct_0_x1622_x8463_478826605}[]{#_Toc366241761}[]{#_Toc345232201}

**ATM接口 \-- ATM接口公共命令 \-- alarm-detect**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image002.png){#图片 15 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x376091679}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x1241674499}
:::

[ ]{lang="EN-US"}

[**[alarm-detect]{lang="EN-US"}**]{#struct_0_x1622_x8463_626648314}[命令用来设置当前接口的告警联动动作。]{style="font-family:宋体"}

[**[undo alarm-detect]{lang="EN-US"}**]{#struct_0_x1622_x8463_1183093656}[命令用来取消告警联动动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_480969434}

[**[alarm-detect]{lang="EN-US"}**[ { **rdi** \| **sd** \| **sf** } **action link-down**]{lang="EN-US"}]{#struct_0_x1622_x8463_478892141}

[**[undo alarm-detect]{lang="EN-US"}**[ { **rdi** \| **sd** \| **sf** }]{lang="EN-US"}]{#struct_0_x1622_x8463_433968577}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1191855658}

[[接口不执行任何告警联动动作。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1527398526}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1790499032}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x399556936}[接口视图（包括]{style="font-family:宋体"}[13]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[E1]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[、]{style="font-family:宋体"}[E3]{lang="EN-US"}[、]{style="font-family:宋体"}[T3]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-3c/STM-1]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-12c/STM-4]{lang="EN-US"}[、]{style="font-family:宋体"}[25M]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL 2+]{lang="EN-US"}[、]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_478957677}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1979730894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x376359777}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_765257906}

[**[rdi]{lang="EN-US"}**]{#struct_0_x1622_x8463_1967733566}[：表示]{style="font-family:宋体"}[RDI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Defect Indication]{lang="EN-US"}[，远端失效指示）告警。]{style="font-family:宋体"}

[**[sd]{lang="EN-US"}**]{#struct_0_x1622_x8463_1275441474}[：表示]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_x1622_x8463_479547501}[：表示]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_x1622_x8463_x722230787}[：设置当接口检测到告警时的联动动作。]{style="font-family:宋体"}

[**[link-down]{lang="EN-US"}**]{#struct_0_x1622_x8463_747962541}[：表示自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_636057643}

[[当设备收到对端发送的]{style="font-family:宋体"}[MS-RDI]{lang="EN-US"}]{#struct_0_x1622_x8463_977793313}[信号时，则认为发生了]{style="font-family:宋体"}[RDI]{lang="EN-US"}[告警。当设备收到的报文的误码率达到或超过设置的门限时，则生成]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警或]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警的门限可通过]{style="font-family:宋体"}**[threshold]{lang="EN-US"}**[命令设置。]{style="font-family:宋体"}

[[配置本命令后，当设备检测到告警时，会自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1622_x8463_479613037}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1894466375}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1138278052}[配置当]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[接口检测到]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警时，自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1624511177}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] alarm-detect sd action link-down]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1811121364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[threshold]{lang="EN-US"}**]{#struct_0_x1622_x8463_479023212}
:::::

::: {#1742433432 .myid}
[]{#_Toc263067817}[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc139515317}[]{#_Toc137103150}[]{#_Toc274832278}[]{#_Toc274658211}[]{#_Toc284169067}[]{#_Toc404783969}[]{#struct_0_x1622_x8463_x1938233363}[]{#_Toc347149589}[]{#_Toc342919786}[]{#_Toc335656788}[]{#_Toc323804932}

**ATM接口 \-- ATM接口公共命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x1622_x8463_1096845785}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1400457858}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1839370566}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x1622_x8463_1421227792}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1488339074}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1277341108}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x1622_x8463_1375260173}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1455803062}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_176506693}[接口视图（包括]{style="font-family:宋体"}[13]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[E1]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[、]{style="font-family:宋体"}[E3]{lang="EN-US"}[、]{style="font-family:宋体"}[T3]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-3c/STM-1]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-12c/STM-4]{lang="EN-US"}[、]{style="font-family:宋体"}[25M]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL 2+]{lang="EN-US"}[、]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1106571408}[子接口视图]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1678869753}[接口视图（包括]{style="font-family:宋体"}[4]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_755086648}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x249671448}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1405057489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_897836070}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1376243213}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x1622_x8463_x812537373}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1616361700}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x1622_x8463_1100723450}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_50507507}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_982848727}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x2021663642}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] bandwidth 50]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404783970}[]{#struct_0_x1622_x8463_x1918516022}[]{#_Toc347149590}[]{#_Toc342919787}[]{#_Toc335656811}[]{#_Toc329007815}[]{#_Toc309912009}

**ATM接口 \-- ATM接口公共命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x1622_x8463_1376177677}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2027783182}

[**[default]{lang="EN-US"}**]{#struct_0_x1622_x8463_x442185787}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1207743218}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_2074783471}[接口视图（包括]{style="font-family:宋体"}[13]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[E1]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[、]{style="font-family:宋体"}[E3]{lang="EN-US"}[、]{style="font-family:宋体"}[T3]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-3c/STM-1]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-12c/STM-4]{lang="EN-US"}[、]{style="font-family:宋体"}[25M]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL 2+]{lang="EN-US"}[、]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x371679993}[子接口视图]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_1977870677}[接口视图（包括]{style="font-family:宋体"}[4]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_636892164}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1230875533}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353164427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_116451823}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1810518448}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_94787766}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1051532845}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_597420641}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_694018022}[将]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1186322962}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404783971}[]{#struct_0_x1622_x8463_x1353229963}[]{#_Toc347149591}[]{#_Toc342919788}[]{#_Toc335656812}

**ATM接口 \-- ATM接口公共命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1622_x8463_x666575796}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1056282574}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x774471457}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x1622_x8463_2122419688}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1622_x8463_1926119758}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1755361991}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_x1622_x8463_1674820924}["，比如：]{style="font-family:宋体"}[ATM2/4/0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_832254976}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353295499}[接口视图（包括]{style="font-family:宋体"}[13]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[E1]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[、]{style="font-family:宋体"}[E3]{lang="EN-US"}[、]{style="font-family:宋体"}[T3]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-3c/STM-1]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-12c/STM-4]{lang="EN-US"}[、]{style="font-family:宋体"}[25M]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL 2+]{lang="EN-US"}[、]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_1127354066}[子接口视图]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1790942827}[接口视图（包括]{style="font-family:宋体"}[4]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_1965546669}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_546246341}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1718067484}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x828343881}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2106433840}

[*[text]{lang="EN-US"}*]{#struct_0_x1622_x8463_x1129531833}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1353361035}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1952699169}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[atmswitch-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_732058886}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] description atmswitch-interface]{lang="EN-US"}
:::

::::: {#-1795371827 .myid}
[]{#_Toc404783972}[]{#struct_0_x1622_x8463_786967017}[]{#_Toc389663151}[]{#_Toc350859898}

**ATM接口 \-- ATM接口公共命令 \-- display counters**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x1057867491}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_409376734}
:::

[ ]{lang="EN-US"}

[**[display counters]{lang="EN-US"}**]{#struct_0_x1622_x8463_786901481}[命令用来显示接口的流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_853740721}

[**[display counters]{lang="EN-US"}**[ { **inbound** \| **outbound** } **interface** \[ **atm** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x1622_x8463_1586090093}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1999603862}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_168901901}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1842693941}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2052247285}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x1087313895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1864527784}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x17136786}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_786835945}

[**[inbound]{lang="EN-US"}**]{#struct_0_x1622_x8463_2109082029}[：显示输入报文的流量统计信息。]{style="font-family:宋体"}

[**[oubound]{lang="EN-US"}**]{#struct_0_x1622_x8463_250687029}[：显示输出报文的流量统计信息。]{style="font-family:宋体"}

[**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_152638967}[：显示]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的流量统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1622_x8463_x602976906}[：]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1277025020}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x1622_x8463_957190874}**[atm]{lang="EN-US"}**[，则显示所有可统计的接口的流量统计信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_1414901539}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则显示所有]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的流量统计信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_1383501666}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则显示指定]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的流量统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1524689764}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_786770409}[显示]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[接口的输入报文流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display counters inbound interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_x1275851802}

[Interface         Total (pkts)   Broadcast (pkts)   Multicast (pkts)  Err (pkts)]{lang="EN-US"}

[ATM2/4/0                   100                  0                100           0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Overflow: More than 14 digits (7 digits for column \"Err\").]{lang="EN-US"}

[       \--: Not supported.]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display counters]{lang="EN-US"}]{#struct_0_x1622_x8463_x1573250606}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1151879049}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1889827857}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1516753982}

[[Interface]{lang="EN-US"}]{#struct_0_x1622_x8463_x2013354246}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x1622_x8463_787753449}

[[Total (pkts)]{lang="EN-US"}]{#struct_0_x1622_x8463_x738726573}

[[接口接收或发送报文的总数（单位为包）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1646393728}

[[Broadcast (pkts)]{lang="EN-US"}]{#struct_0_x1622_x8463_4050779}

[[接口接收或发送广播报文的总数（单位为包）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1127236851}

[[Multicast (pkts)]{lang="EN-US"}]{#struct_0_x1622_x8463_787687913}

[[接口接收或发送组播报文的总数（单位为包）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_456196883}

[[Err (pkts)]{lang="EN-US"}]{#struct_0_x1622_x8463_1315543210}

[[接口接收或发送错误报文的总数（单位为包）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1775130958}

[[Overflow]{lang="EN-US"}]{#struct_0_x1622_x8463_787229162}[：]{style="font-family:宋体"}[More than 14 digits]{lang="EN-US"}[（]{style="font-family:宋体"}[7 digits for colum "Err"]{lang="EN-US"}[）]{style="font-family:宋体"}

[[当某个统计信息的值为]{style="font-family:宋体"}[Overflow]{lang="EN-US"}]{#struct_0_x1622_x8463_1881122470}[时，表示该项数据的长度超过了显示范围]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1356434976}[Err]{lang="EN-US"}[项，]{style="font-family:宋体"}[Overflow]{lang="EN-US"}[表示数据的长度超过了]{style="font-family:宋体"}[7]{lang="EN-US"}[位十进制数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于其它项，]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x882421218}[Overflow]{lang="EN-US"}[表示数据的长度超过了]{style="font-family:宋体"}[14]{lang="EN-US"}[位十进制数]{style="font-family:宋体"}

[[\--: Not supported.]{lang="EN-US"}]{#struct_0_x1622_x8463_787163626}

[[当某个统计信息的值为"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_x1622_x8463_767743483}["时，表示设备不支持该项数据的统计]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_633990407}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1622_x8463_x19651118}

::::: {#1444576144 .myid}
[]{#_Toc404783973}[]{#struct_0_x1622_x8463_x784223885}

**ATM接口 \-- ATM接口公共命令 \-- display counters rate**

------------------------------------------------------------------------

[**[display counters rate]{lang="EN-US"}**]{#struct_0_x1622_x8463_1939066788}[命令用来显示最近一个统计周期内处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的接口的报文速率统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x940299299}

[**[display counters rate]{lang="EN-US"}**[ { **inbound** \| **outbound** } **interface** \[ **atm** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x1622_x8463_1897081366}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x36903912}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_464842789}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_787098090}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1236737130}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x413944084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x435640970}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_1945887446}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_517733323}

[**[inbound]{lang="EN-US"}**]{#struct_0_x1622_x8463_x660301628}**[：]{style="font-family:宋体"}**[显示报文接收速率统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x1622_x8463_x238250597}**[：]{style="font-family:宋体"}**[显示报文发送速率统计信息。]{style="font-family:宋体"}

[**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x997137944}[：显示]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的报文速率统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1622_x8463_x1477993927}[：]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_703692948}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x1622_x8463_787032554}**[atm]{lang="EN-US"}**[，则显示所有可统计的接口类型中最近一个统计周期内处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的接口的报文速率统计信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_1576499445}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则显示最近一个统计周期内所有处于]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[状态的]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的报文速率统计信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2122704117}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则显示]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[最近一个统计周期内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:
宋体"}[报文速率统计信息。]{lang="EN-US" style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x216309884}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[统计周期与设备的型号有关，请以设备的实际情况为准：]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_1812333185}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[不支持]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[flow-interval]{lang="EN-US"}**]{#struct_0_x1622_x8463_x28924049}[命令的设备，统计周期]{lang="EN-US" style="font-family:
KaiTi_GB2312"}[固定]{style="font-family:KaiTi_GB2312"}[为]{lang="EN-US" style="font-family:KaiTi_GB2312"}[5]{lang="EN-US"}[分钟。]{lang="EN-US" style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[支持]{lang="EN-US" style="font-family:KaiTi_GB2312"}[flow-interval]{lang="EN-US"}]{#struct_0_x1622_x8463_x1019984833}[命令的设备，统计周期可以通过]{lang="EN-US" style="font-family:KaiTi_GB2312"}[flow-interval]{lang="EN-US"}[命令来]{lang="EN-US" style="font-family:KaiTi_GB2312"}[配置。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1832997747}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_786967018}[显示]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[接口的报文接收速率统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display counters rate inbound interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_x1057867496}

[Interface               Total (pps)       Broadcast (pps)       Multicast (pps)]{lang="EN-US"}

[ATM2/4/0                        100                     0                   100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Overflow: More than 14 digits.]{lang="EN-US"}

[       \--: Not supported.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display counters rate]{lang="EN-US"}]{#struct_0_x1622_x8463_1168891621}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1127149543}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1357367137}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1467217146}

[[Interface]{lang="EN-US"}]{#struct_0_x1622_x8463_786901482}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x1622_x8463_853740720}

[[Total (pps)]{lang="EN-US"}]{#struct_0_x1622_x8463_1586090094}

[[在最近一个统计周期内，接口接收或发送所有类型报文的平均速率（单位为包]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1622_x8463_x1999931542}[秒）]{style="font-family:宋体"}

[[Broadcast (pps)]{lang="EN-US"}]{#struct_0_x1622_x8463_x2009137583}

[[在最近一个统计周期内，接口接收或发送广播报文的平均速率（单位为包]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1622_x8463_786835946}[秒）]{style="font-family:宋体"}

[[Multicast (pps)]{lang="EN-US"}]{#struct_0_x1622_x8463_2109082026}

[[在最近一个统计周期内，接口接收或发送组播报文的平均速率（单位为包]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1622_x8463_250228277}[秒）]{style="font-family:宋体"}

[[Overflow: More than 14 digits.]{lang="EN-US"}]{#struct_0_x1622_x8463_142829}

[[当某个统计信息的值为]{style="font-family:宋体"}[Overflow]{lang="EN-US"}]{#struct_0_x1622_x8463_786770410}[时，表示该项数据的长度超过了]{style="font-family:宋体"}[14]{lang="EN-US"}[位十进制数]{style="font-family:宋体"}

[[\--: Not supported.]{lang="EN-US"}]{#struct_0_x1622_x8463_680463341}

[[当某个统计信息的值为"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_x1622_x8463_x1477668699}["时，则表示设备不支持该项数据的统计]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_298392140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1742676413}

::: {#875595164 .myid}
[]{#_Toc404783974}[]{#struct_0_x1622_x8463_1921105557}[]{#_Toc257220490}[]{#_Toc170286810}[]{#_Toc153612994}[]{#_Toc136937657}

**ATM接口 \-- ATM接口公共命令 \-- display interface atm**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_1837028853}[命令用来显示]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_145340918}

[**[display interface]{lang="EN-US"}**[ \[ **atm** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x1622_x8463_1902473132}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1353426571}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1525299842}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1034189046}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1378073283}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x804338375}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1494510112}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x1199046269}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_880711488}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1622_x8463_1102647302}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的信息，]{style="font-family:宋体"}[interface-number]{lang="EN-US"}[表示]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1353492107}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x1622_x8463_43999360}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x1622_x8463_1071562377}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1952657786}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x1622_x8463_776664218}**[atm]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2032393651}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_452362521}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x249118256}[显示接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353557643}

[ATM2/4/0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: ATM2/4/0 Interface]{lang="EN-US"}

[Bandwidth: 20000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[AAL enabled: AAL5]{lang="EN-US"}

[Current VCs: 0 (0 on main interface)]{lang="EN-US"}

[ATM over E1, Scramble: enabled, Frame-format: crc4-adm]{lang="EN-US"}

[Code: hdb3, Clock: slave, Cable length: long]{lang="EN-US"}

[Loopback: cell]{lang="EN-US"}

[Cable type: 75 ohm non-balanced]{lang="EN-US"}

[Line Alarm: LOS LOF]{lang="EN-US"}

[Line Error: 0 FERR, 0 LCV, 0 CERR, 0 FEBE]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}

[Input:]{lang="EN-US"}

[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}

[  0 errors, 0 crcs, 0 lens, 0 giants]{lang="EN-US"}

[  0 pads, 0 aborts, 0 timeouts]{lang="EN-US"}

[  0 overflows, 0 overruns, 0 no buffer]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}

[  0 errors, 0 overflows, 0 underruns]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353623179}[显示接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface atm 2/4/0 brief]{lang="EN-US"}]{#struct_0_x1622_x8463_x1206968158}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[ATM2/4/0             UP   UP(s)    \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_578437740}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface atm brief down]{lang="EN-US"}]{#struct_0_x1622_x8463_x2045524895}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[ATM2/4/0             DOWN Not connected]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display interface atm]{lang="EN-US"}]{#struct_0_x1622_x8463_x486937513}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x824796948}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_925279009}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1352640139}

[[ATM2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_486095405}

[[Current state]{lang="EN-US"}]{#struct_0_x1622_x8463_1425280999}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_609104921}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_1382162870}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_x763785696}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352705675}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x1622_x8463_1482131368}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1154814992}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_5984607}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_1161282824}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1622_x8463_x1201783486}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1353164426}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x1622_x8463_x1449632118}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1557345874}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x1622_x8463_2064703021}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1260215041}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353229962}

[[对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1622_x8463_2062307559}[报文的处理能力，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示尚未配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，不能处理]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文。当接口下配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之后，该字段将变为"]{style="font-family:宋体"}[Internet Address is]{lang="EN-US"}["]{style="font-family:宋体"}

[[AAL enabled]{lang="EN-US"}]{#struct_0_x1622_x8463_x1923909920}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x769645186}[接口使能的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[适配层类型，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[支持的适配层类型固定为]{style="font-family:宋体"}[AAL 5]{lang="EN-US"}[（]{style="font-family:宋体"}[ATM Adaptation Layer 5]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[适配层]{style="font-family:宋体"}[5]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Current VCs: 0 (0 on main interface)]{lang="EN-US"}]{#struct_0_x1622_x8463_x1432393580}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353295498}[接口下已经配置的虚电路数，括号中的内容表示主接口上已经配置的虚电路数]{style="font-family:宋体"}

[[ATM over E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1601529289}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x711081805}[接口的类型]{style="font-family:宋体"}

[[Scramble]{lang="EN-US"}]{#struct_0_x1622_x8463_958356765}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1740770622}[接口下加扰功能的使能情况]{style="font-family:宋体"}

[[Frame-format]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353361034}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_386615228}[接口的帧格式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sdh]{lang="EN-US"}]{#struct_0_x1622_x8463_1448162393}[：]{style="font-family:宋体"}[帧格式为]{lang="EN-US" style="font-family:宋体"}[SDH STM-1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sonet]{lang="EN-US"}]{#struct_0_x1622_x8463_803756666}[：]{style="font-family:宋体"}[帧格式为]{lang="EN-US" style="font-family:宋体"}[SONET OC-3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[crc4-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353426570}[：]{style="font-family:宋体"}[帧格式为]{lang="EN-US" style="font-family:宋体"}[CRC4 ADM]{lang="EN-US"}[格式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no-crc4-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_1203583513}[：]{style="font-family:宋体"}[帧格式为]{lang="EN-US" style="font-family:宋体"}[No-CRC4 ADM]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[esf-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_338472621}[：帧格式为]{lang="EN-US" style="font-family:宋体"}[ESF ADM]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sf-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_x1330161590}[：]{style="font-family:宋体"}[帧格式为]{lang="EN-US" style="font-family:宋体"}[SF ADM]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[g751-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353492106}[：帧格式为]{style="font-family:宋体"}[G.751]{lang="EN-US"}[直接成帧]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[g751-plcp]{lang="EN-US"}]{#struct_0_x1622_x8463_1652011262}[：帧格式为]{lang="EN-US" style="font-family:宋体"}[G.751 PLCP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[g832-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_1979691131}[：帧格式为]{style="font-family:宋体"}[G.823]{lang="EN-US"}[直接成帧]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[cbit-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_1629339687}[：帧格式为]{lang="EN-US" style="font-family:宋体"}[C-bit]{lang="EN-US"}[直接成帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[cbit-plcp]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353557642}[：帧格式为]{lang="EN-US" style="font-family:宋体"}[C-bit PLCP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m23-adm]{lang="EN-US"}]{#struct_0_x1622_x8463_2036994611}[：帧格式为]{style="font-family:宋体"}[M23]{lang="EN-US"}[直接成帧]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m23-plcp]{lang="EN-US"}]{#struct_0_x1622_x8463_81671396}[：帧格式为]{lang="EN-US" style="font-family:宋体"}[M23 PLCP]{lang="EN-US"}

[[Code]{lang="EN-US"}]{#struct_0_x1622_x8463_1011815578}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353623178}[接口的线路编码格式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ami]{lang="EN-US"}]{#struct_0_x1622_x8463_1521915197}[：线路编码为]{style="font-family:宋体"}[AMI]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hdb3]{lang="EN-US"}]{#struct_0_x1622_x8463_1814025454}[：线路编码为]{style="font-family:宋体"}[HDB3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[b8zs]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352640138}[：线路编码为]{style="font-family:宋体"}[B8ZS]{lang="EN-US"}

[[Clock]{lang="EN-US"}]{#struct_0_x1622_x8463_x1079988536}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_1773311942}[接口的时钟模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[master]{lang="EN-US"}]{#struct_0_x1622_x8463_x1983070062}[：]{style="font-family:宋体"}[主时钟模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[slave]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352705674}[：从时钟模式]{style="font-family:宋体"}

[[Cable length]{lang="EN-US"}]{#struct_0_x1622_x8463_x83952573}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x324625556}[接口的电缆模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[long]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353164429}[：长距模式，]{lang="EN-US" style="font-family:宋体"}[151]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[米]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[short]{lang="EN-US"}]{#struct_0_x1622_x8463_x333886871}[：短距模式，]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[150]{lang="EN-US"}[米]{lang="EN-US" style="font-family:宋体"}

[[Loopback]{lang="EN-US"}]{#struct_0_x1622_x8463_x1533937186}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1776347289}[接口的环回模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[cell]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353229965}[：对内进行信元自环]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_x1622_x8463_x1473144850}[：对内自环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[payload]{lang="EN-US"}]{#struct_0_x1622_x8463_x1463742379}[：对外载荷环回]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[remote]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353295501}[：对外线路环回]{lang="EN-US" style="font-family:宋体"}

[[Cable type]{lang="EN-US"}]{#struct_0_x1622_x8463_771582459}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x2110734581}[接口电缆类型]{style="font-family:宋体"}

[[Line Alarm]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353361037}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_789899755}[接口线路报警]{style="font-family:宋体"}

[[Line Error]{lang="EN-US"}]{#struct_0_x1622_x8463_945140904}

[[该]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353426573}[接口线路出错情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FERR]{lang="EN-US"}]{#struct_0_x1622_x8463_1606868040}[：]{style="font-family:宋体"}[Framing Bit Error]{lang="EN-US"}[（帧比特错误）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LCV]{lang="EN-US"}]{#struct_0_x1622_x8463_198887357}[：]{style="font-family:宋体"}[Line Code Violation]{lang="EN-US"}[（线路编码错误）]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CERR]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353492109}[：]{style="font-family:宋体"}[CRC Errors]{lang="EN-US"}[（循环冗余校验错误）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FEBE]{lang="EN-US"}]{#struct_0_x1622_x8463_1248726735}[：]{style="font-family:宋体"}[Far-End Block Error]{lang="EN-US"}[（远端模块错误）]{lang="EN-US" style="font-family:
  宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_x1622_x8463_610622866}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x1622_x8463_1552526077}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x1622_x8463_x1667921795}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1353557645}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_x1622_x8463_1277479724}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353623181}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_x1622_x8463_x851720838}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1622_x8463_x59837777}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"} [packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input:]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352640141}

[[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_129930581}

[[  0 errors, 0 crcs, 0 lens, 0 giants]{lang="EN-US"}]{#struct_0_x1622_x8463_x2111588702}

[[  0 pads, 0 aborts, 0 timeouts]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352705677}

[[  0 overflows, 0 overruns, 0 no buffer]{lang="EN-US"}]{#struct_0_x1622_x8463_x1650036514}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353164428}[：接口收到的总报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_x1622_x8463_x1899970812}[：接口收到的总字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_2124244143}[：]{style="font-family:宋体"} [接口接收报文所使用缓冲区个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353229964}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[crcs]{lang="EN-US"}]{#struct_0_x1622_x8463_1255738505}[：]{style="font-family:宋体"}[CRC]{lang="EN-US"}[错误数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[lens]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353295500}[：]{style="font-family:宋体"} [接口接收到长度错误的报文个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_x1622_x8463_x1957300896}[：接口接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pads]{lang="EN-US"}]{#struct_0_x1622_x8463_x2096242950}[：]{style="font-family:宋体"} [接口接收报文进行填充时发生的相关错误个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353361036}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[timeouts]{lang="EN-US"}]{#struct_0_x1622_x8463_x776184186}[：接口接收报文超时的个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overflows]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353426572}[：接口接收报文时芯片]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[溢出错误个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_x1622_x8463_40784099}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffer]{lang="EN-US"}]{#struct_0_x1622_x8463_1693387576}[：]{style="font-family:宋体"} [接口接收报文时因系统资源不足产生的相关错误]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353492108}

[[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_x1480156620}

[[  0 errors, 0 overflows, 0 underruns]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353557644}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_x1622_x8463_x1451403631}[：接口发送的总报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353623180}[：接口发送的总字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_1877162517}[：接口发送报文所使用的缓冲区个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_x1622_x8463_42737183}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overflows]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352640140}[：接口发送报文时芯片]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[溢出错误个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_x1622_x8463_x1436153360}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352705676}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_x1622_x8463_1078846841}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353164431}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x690182767}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353229967}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x1622_x8463_1659023032}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353295503}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1622_x8463_1934381873}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1351393442}

[[Link]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353361039}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1353426575}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_800298986}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_x1399964255}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353492111}[：表示接口被手工关闭了，需要执行]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x1622_x8463_x1399898719}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1622_x8463_892561911}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1353623183}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_478761065}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_478826601}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x1622_x8463_478892137}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x1622_x8463_x2014520252}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352640143}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1622_x8463_1292729995}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1352705679}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x1622_x8463_x1199697820}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353164430}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#497897632 .myid}
[]{#_Toc404783975}[]{#struct_0_x1622_x8463_2038700588}[]{#_Toc257220491}[]{#_Toc170286811}[]{#_Toc153612995}[]{#_Toc136937658}

**ATM接口 \-- ATM接口公共命令 \-- interface atm**

------------------------------------------------------------------------

[**[interface atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x843904909}[命令用来进入]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口或子接口视图。在进入子接口视图之前，如果指定的子接口不存在，则先创建子接口，再进入该子接口的视图。]{style="font-family:宋体"}

[**[undo interface atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1461043385}[命令用来删除]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2094484903}

[**[interface atm]{lang="EN-US"}**[ { *interface-number* \| *interface-number.subnumber* \[ **p2mp** \| **p2p** \] }]{lang="EN-US"}]{#struct_0_x1622_x8463_917263117}

[**[undo interface atm]{lang="EN-US"}**[ *interface-number.subnumber*]{lang="EN-US"}]{#struct_0_x1622_x8463_x421667381}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x715223801}

[[不存在]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353229966}[子接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_92939091}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1466027922}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2142505507}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_925358503}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_322960270}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x346417962}

[]{#_Hlt17514754}[]{#struct_0_x1622_x8463_x615986611}[]{#_Hlt25382970}*[interface-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_x1622_x8463_x358958026}[：]{style="font-family:
宋体"}[ATM]{lang="EN-US"}[子接口编号，其中]{style="font-family:宋体"}[interface-number]{lang="EN-US"}[为主接口编号；]{style="font-family:宋体"}[subnumber]{lang="EN-US"}[为子接口编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[p2mp]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1353295502}[：点到多点子接口。子接口缺省为]{style="font-family:宋体"}**[p2mp]{lang="EN-US"}**[类型。]{style="font-family:宋体"}

[**[p2p]{lang="EN-US"}**]{#struct_0_x1622_x8463_x794501482}[：点到点子接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1246212466}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x849519900}[进入]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x442029406}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1188178397}[创建]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口]{style="font-family:宋体"}[ATM2/4/0.1]{lang="EN-US"}[并进入子接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_494391924}

[\[Sysname\] interface atm2/4/0.1]{lang="EN-US"}

[\[Sysname-ATM2/4/0.1\]]{lang="EN-US"}
:::

::: {#988247972 .myid}
[]{#_Toc404783976}[]{#struct_0_x1622_x8463_x1363851527}[]{#_Toc347149598}[]{#_Toc342919794}[]{#_Toc335656818}[]{#_Toc317856914}[]{#_Toc309228572}[]{#_Toc13287745}

**ATM接口 \-- ATM接口公共命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1353361038}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1226522880}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1425556087}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x1622_x8463_1179354024}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1622_x8463_x97450088}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x793443736}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x1622_x8463_x2129737642}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2042704602}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_800556833}[接口视图（包括]{style="font-family:宋体"}[13]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[E1]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[、]{style="font-family:宋体"}[E3]{lang="EN-US"}[、]{style="font-family:宋体"}[T3]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-3c/STM-1]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-12c/STM-4]{lang="EN-US"}[、]{style="font-family:宋体"}[25M]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL 2+]{lang="EN-US"}[、]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353426574}[子接口视图]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_x765784955}[接口视图（包括]{style="font-family:宋体"}[4]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_2058810325}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x745597046}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1176974805}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1338011179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_74974569}

[*[size]{lang="EN-US"}*]{#struct_0_x1622_x8463_547828060}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1353492110}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x1622_x8463_x1836321444}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_518623270}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_629243258}[配置接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[200]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x442674826}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] mtu 200]{lang="EN-US"}
:::

::: {#2052875588 .myid}
[]{#_Toc404783977}[]{#struct_0_x1622_x8463_x685359326}[]{#_Toc257220493}[]{#_Toc214762440}[]{#_Toc213490054}[]{#_Toc207010309}[]{#_Toc207010042}[]{#_Toc139515326}

**ATM接口 \-- ATM接口公共命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1622_x8463_x971762583}[命令用来清除指定接口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x963449888}

[**[reset counters interface]{lang="EN-US"}**[ \[ **atm** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x1622_x8463_x1353557646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x288604217}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_916068247}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1224517023}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1563441621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x2010920988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_408236680}

[**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_1893878662}[：清除]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1622_x8463_x1353623182}[：]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_714363103}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1835164218}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1452443704}**[atm]{lang="EN-US"}**[参数，则清除所有接口的统计信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1750284612}[参数而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[atm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1689391005}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_546266156}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1401046997}[清除]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_x63750728}
:::

::: {#1170655049 .myid}
[]{#_Toc404783978}[]{#struct_0_x1622_x8463_x1352640142}[]{#_Toc347149612}[]{#_Toc342919798}[]{#_Toc335656822}

**ATM接口 \-- ATM接口公共命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1622_x8463_x273353946}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1622_x8463_x329615683}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1019519953}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1622_x8463_x239848260}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1046181907}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x753631005}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x2131722705}[接口处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1063401695}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1352705678}[接口视图（包括]{style="font-family:宋体"}[13]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[E1]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[、]{style="font-family:宋体"}[E3]{lang="EN-US"}[、]{style="font-family:宋体"}[T3]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-3c/STM-1]{lang="EN-US"}[、]{style="font-family:宋体"}[OC-12c/STM-4]{lang="EN-US"}[、]{style="font-family:宋体"}[25M]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL 2+]{lang="EN-US"}[、]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_1529185535}[子接口视图]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1861429776}[接口视图（包括]{style="font-family:宋体"}[4]{lang="EN-US"}[种物理类型：]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[SHDSL_8WIRE_BIS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_1505859618}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_217791573}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1689814283}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x2118104867}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x356294477}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x938270860}[关闭]{style="font-family:宋体"}[ATM]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_569149874}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\]]{lang="SV"}[ ]{lang="SV"}[shutdown]{lang="EN-US"}
:::

::: {#424787513 .myid}
[]{#_Toc404783980}[]{#struct_0_x1622_x8463_x1318452140}[]{#_Toc345946845}

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1940277952}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1692918546}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1289686931}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1622_x8463_92627043}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_x779806878}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_569084338}

[[时钟模式为从时钟模式（]{style="font-family:宋体"}]{#struct_0_x1622_x8463_954656871}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1245247951}

[[ATM 25M]{lang="EN-US"}]{#struct_0_x1622_x8463_1119033516}[接口视图]{style="font-family:宋体"}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_x1622_x8463_32221011}[接口视图]{style="font-family:宋体"}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_x1622_x8463_x194209667}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_935922698}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2016577345}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1593414298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_569018802}

[**[master]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1787125069}[：配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式为主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1622_x8463_x991972564}[：配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式为从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_115817806}

[[当作为]{style="font-family:宋体"}[DCE]{lang="EN-US"}]{#struct_0_x1622_x8463_1732102604}[设备使用时，应配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口使用主时钟模式；作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备使用时，应配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口使用从时钟模式。]{style="font-family:宋体"}

[[当两台路由器的]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_886177329}[接口通过光纤直连时，应该将一端的时钟配置为主时钟模式，另一端为从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x141571302}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_225871306}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[上的时钟为主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_568953266}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] clock master]{lang="SV"}
:::

::: {#2006314719 .myid}
[]{#_Toc404783981}[]{#struct_0_x1622_x8463_x2070774366}[]{#_Toc345946846}

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- flag**

------------------------------------------------------------------------

[**[flag]{lang="EN-US"}**]{#struct_0_x1622_x8463_1112214686}[命令用来配置]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[帧的开销字节。]{style="font-family:宋体"}

[**[undo flag]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1541154869}[命令用来恢复]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[帧开销字节的缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x618400987}

[**[flag]{lang="DA"}**[ ]{lang="DA"}]{#struct_0_x1622_x8463_1304548004}**[c2]{lang="DA"}**[ ]{lang="DA"}*[flag-value]{lang="DA"}*

[**[undo flag c2]{lang="DA"}**]{#struct_0_x1622_x8463_2213919}

[**[flag]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[{ ]{lang="EN-US"}]{#struct_0_x1622_x8463_2089624891}**[j0]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[\| ]{lang="EN-US"}**[j1]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[} { ]{lang="EN-US"}**[sdh]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[\| ]{lang="EN-US"}**[sonet]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[} ]{lang="EN-US"}*[flag-value]{lang="NO-BOK"}*

[**[undo flag]{lang="NO-BOK"}**]{#struct_0_x1622_x8463_x545178216}[ ]{lang="NO-BOK"}[{ ]{lang="EN-US"}**[j0]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[\| ]{lang="EN-US"}**[j1]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[} {]{lang="EN-US"}[ ]{lang="EN-US"}**[sdh]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[\| ]{lang="EN-US"}**[sonet]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[}]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568887730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[c2]{lang="EN-US"}**]{#struct_0_x1622_x8463_252035798}[的缺省值为]{lang="EN-US" style="font-family:宋体"}[0x13]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统使用]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1055699496}[SDH]{lang="EN-US"}[帧格式的缺省值，]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}**[j0]{lang="EN-US"}**[和]{style="font-family:宋体"}**[j1]{lang="EN-US"}**[的缺省值都为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x114010861}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_x1622_x8463_x451489353}[接口视图]{style="font-family:宋体"}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_x1622_x8463_634593993}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x935575448}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2085854065}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_568822194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_990108486}

[**[c2 ]{lang="EN-US"}***[flag-value]{lang="EN-US"}*]{#struct_0_x1622_x8463_1340937188}[：信号标记字节，属于高阶通道开销（]{style="font-family:宋体"}[Higher-Order Path Overhead]{lang="EN-US"}[）字节，用于指示虚拟容器]{style="font-family:宋体"}[VC]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Container]{lang="EN-US"}[）帧的复接结构和信息净负荷的性质。取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j0]{lang="EN-US"}**]{#struct_0_x1622_x8463_106363824}*[ flag-value]{lang="EN-US"}*[：再生段踪迹字节，属于段开销字节（]{style="font-family:宋体"}[Section Overhead]{lang="EN-US"}[），用于检测两个端口之间的连接在段层次上的连续性。]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1084510546}*[ flag-value]{lang="EN-US"}*[：通道踪迹字节，属于高阶通道开销字节，用于检测两个端口之间的连接在通道层次上的连续性。]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_x1622_x8463_2121273775}[：帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Digital Hierarchy]{lang="EN-US"}[，同步数字系列）。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x1622_x8463_906134761}[：帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Optical Network]{lang="EN-US"}[，同步光网络）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_919773749}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C2]{lang="EN-US"}]{#struct_0_x1622_x8463_x1936397576}[字节和]{style="font-family:宋体"}[J1]{lang="EN-US"}[字节的设置一定要使收]{style="font-family:宋体"}[/]{lang="EN-US"}[发两端相匹配，否则会产生告警。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个运营者的网络内]{style="font-family:宋体"}]{#struct_0_x1622_x8463_568756658}[J0]{lang="EN-US"}[字节可为任意字符，而在两个不同运营者的网络边界处要使设备收、发两端的]{style="font-family:宋体"}[J0]{lang="EN-US"}[字节相匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1237209088}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x452377198}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[开销字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[为]{style="font-family:宋体"}[ff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_594264564}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] flag j0 sdh f[f]{#_Toc345946847}]{lang="EN-US"}
:::

::: {#1701559760 .myid}
[]{#_Toc404783982}[]{#struct_0_x1622_x8463_x541207093}

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- frame-format**

------------------------------------------------------------------------

[**[frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1580938851}[命令用来设定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的帧格式。]{style="font-family:宋体"}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_993615330}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1582520417}

[**[frame-format]{lang="EN-US"}**[ { **sdh** \| **sonet** }]{lang="EN-US"}]{#struct_0_x1622_x8463_568691122}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_1199168003}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_633058230}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1072635897}[接口的帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1340222600}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_x1622_x8463_x543308556}[接口视图]{style="font-family:宋体"}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_x1622_x8463_x1771719201}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1568463558}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_696889621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_569674162}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2111493042}

[**[sdh]{lang="EN-US"}**]{#struct_0_x1622_x8463_1712495443}[：帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x1622_x8463_x768908691}[：帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2132181801}

[[通过]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1847810807}**[flag]{lang="EN-US"}**[命令设置开销字节时，需要与帧格式匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1786625330}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_932176773}[设置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_569608626}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] frame-format sdh]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_917582044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**]{#struct_0_x1622_x8463_1787188123}
:::

::: {#1002176090 .myid}
[]{#_Toc404783983}[]{#struct_0_x1622_x8463_787163621}[]{#_Toc389663161}

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- link-delay**

------------------------------------------------------------------------

[**[link-delay]{lang="EN-US"}**]{#struct_0_x1622_x8463_767743484}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口物理连接状态抑制功能。]{style="font-family:宋体"}

[**[undo link-delay]{lang="EN-US"}**]{#struct_0_x1622_x8463_633990404}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x19651115}

[**[link-delay]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1622_x8463_x784223888}

[**[undo link-delay]{lang="EN-US"}**]{#struct_0_x1622_x8463_1939263396}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x579040785}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1110310510}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1503542006}

[[ATM 25M]{lang="EN-US"}]{#struct_0_x1622_x8463_787098085}[接口视图]{style="font-family:宋体"}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1101915033}[接口视图]{style="font-family:宋体"}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_x1622_x8463_1503083019}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1553117007}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1178471244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x158851722}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x166625676}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1622_x8463_1111845006}[：物理连接状态的抑制时间，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_920412654}

[[通常情况下，当接口的物理连接状态（]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1622_x8463_x180278515}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[）改变时，系统会立即通知上层协议模块并生成]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息。为了避免接口物理连接状态在短时间内的频繁改变带来额外的系统开销，可通过本命令配置接口的物理连接状态抑制时间，接口在此时间内产生的物理连接状态变化将被系统忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1289248913}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2090676218}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的物理连接状态抑制时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_787032549}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] link-delay 20]{lang="EN-US"}
:::

::: {#405613428 .myid}
[]{#_Toc404783984}[]{#struct_0_x1622_x8463_280744572}[]{#_Toc345946848}

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1194303754}[命令用来开启]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_638440647}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x178830682}

[**[loopback]{lang="EN-US"}**[ { **cell** \| **local** \| **remote** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x46005493}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_1464660685}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_569149875}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_573023065}[接口的环回检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1318452139}

[[ATM 25M]{lang="EN-US"}]{#struct_0_x1622_x8463_x17767043}[接口视图]{style="font-family:宋体"}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_x1622_x8463_514785982}[接口视图]{style="font-family:宋体"}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_x1622_x8463_573000415}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x151899737}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x53927093}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1364713967}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_569084339}

[**[cell]{lang="EN-US"}**]{#struct_0_x1622_x8463_954656872}[：设置接口对内信元环回。此方式可以用来检测本端物理芯片是否正常。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1245247948}[：设置接口对内自环。此方式可以用来检测本端业务芯片是否正常。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1622_x8463_x90885601}[：设置接口对外线路环回。此方式可以用来检测对端是否正常。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1998202085}

[[只有在进行某些特殊功能测试的时候，才将接口设置为对内自环或对外环回。正常工作时，不要启用环回检测功能。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1608829065}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x778093478}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1645382092}[开启]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_569018803}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] loopback local]{lang="EN-US"}
:::

::: {#679047146 .myid}
[]{#_Toc404783985}[]{#struct_0_x1622_x8463_x1787125070}[]{#_Toc345946849}

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- scramble**

------------------------------------------------------------------------

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_930276201}[命令用来开启]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口对载荷的加扰功能。]{style="font-family:宋体"}

[**[undo scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1791797156}[命令用来关闭加扰功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1996776719}

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x54596127}

[**[undo scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1459714486}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_521160940}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1740692188}[接口对载荷的加扰功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568953267}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_x1622_x8463_x2070774367}[接口视图]{style="font-family:宋体"}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_x1622_x8463_x1616668669}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x336599752}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2018316982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1401102017}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x813694333}

[[开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1622_x8463_1934206280}[或]{style="font-family:宋体"}[0]{lang="EN-US"}[，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口都打开或关闭对载荷的加扰功能，才能对接成功。]{style="font-family:宋体"}

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x247714785}[命令只对载荷进行加扰和解扰，不影响信元头。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568887731}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_252035799}[开启]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[对载荷的加扰功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1055699497}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] scrambl[e]{#_Toc345946850}]{lang="EN-US"}
:::

::::: {#-1291593385 .myid}
[]{#_Toc404783986}[]{#struct_0_x1622_x8463_x1893629784}[]{#_Toc324519303}

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- threshold**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image004.jpg){#图片 9 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x1240670377}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x1893564248}
:::

[ ]{lang="EN-US"}

[**[threshold]{lang="EN-US"}**]{#struct_0_x1622_x8463_1270188026}[命令用来设置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限和]{style="font-family:宋体"}[（]{style="font-family:宋体"}[或]{style="font-family:宋体"}[）]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限。]{style="font-family:宋体"}

[**[undo threshold]{lang="EN-US"}**]{#struct_0_x1622_x8463_x604336114}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1893498712}

[**[threshold]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_1579209998}[{ **sd** *sdvalue* \| **sf** *sfvalue* } \*]{lang="FR"}

[**[undo threshold]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1893433176}[\[ **sd** \| **sf** \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1669072106}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x800244479}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1893891928}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_x1622_x8463_x564450}[接口视图]{style="font-family:宋体"}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_x1622_x8463_x1860287865}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1893826392}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_759047089}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1295793723}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1893760856}

[**[sd]{lang="EN-US"}**]{#struct_0_x1622_x8463_1901687094}[：表示配置]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警门限。]{style="font-family:宋体"}

[*[sd]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_x1622_x8463_138510720}[：以]{style="font-family:宋体"}[10e-sd*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sd]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SD]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1893695320}[：表示配置]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警门限。]{style="font-family:宋体"}

[*[sf]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_x1622_x8463_192003648}[：以]{style="font-family:宋体"}[10e-sf*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sf]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SF]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1830701730}

[[SD]{lang="EN-US"}]{#struct_0_x1622_x8463_x1893105496}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警都是用于指示当前线路性能的，相比较而言，]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警比]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警更为严重，]{style="font-family:宋体"}[SF]{lang="EN-US"}[的误码率门限一般会比]{style="font-family:宋体"}[SD]{lang="EN-US"}[的误码率门限高，也就是说，当出现少量误码时，设备产生]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警，当误码率增大到一定程度时，说明线路质量严重下降，此时设备才产生]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。因此，应使]{style="font-family:宋体"}[SD]{lang="EN-US"}[的告警门限小于]{style="font-family:宋体"}[SF]{lang="EN-US"}[的告警门限，]{style="font-family:宋体"}*[sdvalue]{lang="EN-US"}*[的值应大于]{style="font-family:宋体"}*[sfvalue]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_888157096}

[[\#]{lang="EN-US"}]{#struct_0_x1622_x8463_x587427660}[[ ]{lang="EN-US"}]{#_Toc74621539}[设置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10e-4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1893039960}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] threshold sd 4]{lang="EN-US"}
:::::

::: {#-798614504 .myid}
[]{#_Toc404783988}[]{#struct_0_x1622_x8463_x1532612399}[]{#_Toc345946851}

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- cable**

------------------------------------------------------------------------

[**[cable]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1235367609}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的电缆模式。]{style="font-family:宋体"}

[**[undo cable]{lang="EN-US"}**]{#struct_0_x1622_x8463_1310182771}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_417602515}

[**[cable]{lang="EN-US"}**[ { **long** \| **short** }]{lang="EN-US"}]{#struct_0_x1622_x8463_568822195}

[**[undo cable]{lang="EN-US"}**]{#struct_0_x1622_x8463_990108487}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1340937187}

[[接口链路使用长距模式，在该模式下系统可自动对长距]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1622_x8463_105642928}[短距模式进行调整，即缺省模式下先是使用长距模式，如果电缆属于短距离的，那么系统会自动切换成短距模式而无需手工输入命令。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1000581934}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_310250258}[接口视图]{style="font-family:宋体"}[/ATM T1]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x79416689}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1467347250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1260327123}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568756659}

[**[long]{lang="EN-US"}**]{#struct_0_x1622_x8463_1237209087}[：长距模式，电缆长度为]{style="font-family:宋体"}[151]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[米。在该模式下，如果电缆属于短距离的（电缆长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[150]{lang="EN-US"}[米），那么系统会自动切换成短距模式。]{style="font-family:宋体"}

[**[short]{lang="EN-US"}**]{#struct_0_x1622_x8463_x451525230}[：短距模式，电缆长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[150]{lang="EN-US"}[米。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_310881122}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1307537767}[设置]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[使用短距模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1199166520}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] cable short]{lang="EN-US"}
:::

::: {#-1606168679 .myid}
[]{#_Toc404783989}[]{#struct_0_x1622_x8463_x1215973498}[]{#_Toc345946852}[]{#_Toc349121865}[]{#_Toc349122022}[]{#_Toc349121866}[]{#_Toc349122023}[]{#_Toc349121867}[]{#_Toc349122024}[]{#_Toc349121868}[]{#_Toc349122025}[]{#_Toc349121869}[]{#_Toc349122026}

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2110164789}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_568691123}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1199168002}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1622_x8463_632992694}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_x974443056}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x840272099}

[[时钟模式为从时钟模式（]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1782438035}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1686288994}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1481846060}[接口视图]{style="font-family:宋体"}[/ATM T1]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1481466992}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_569674163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2111493041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1712298835}

[**[master]{lang="EN-US"}**]{#struct_0_x1622_x8463_x773674435}[：配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式为主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1622_x8463_x896936661}[：配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式为从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1666510918}

[[当作为]{style="font-family:宋体"}[DCE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1049638532}[设备使用时，应配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口使用主时钟模式；作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备使用时，应配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口使用从时钟模式。]{style="font-family:宋体"}

[[当两台路由器的]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_1038460656}[接口通过光纤直连时，应该将一端的时钟配置为主时钟模式，另一端为从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_717493394}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_569608627}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[上的时钟为主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_917582045}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] clock master]{lang="SV"}
:::

::: {#1726432707 .myid}
[]{#_Toc404783990}[]{#struct_0_x1622_x8463_1787188122}[]{#_Toc345946853}

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- clock-change auto**

------------------------------------------------------------------------

[**[clock-change auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_280679036}[命令用来开启接口的时钟自动切换功能。]{style="font-family:宋体"}

[**[undo clock-change auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_x798025904}[命令用来关闭时钟自动切换功能，接口恢复成当前用户配置的时钟模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1053129967}

[**[clock-change auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_1696435781}

[**[undo clock-change auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1817332223}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_569149872}

[[时钟自动切换功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_573023062}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1318452138}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1583850984}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1537937233}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2114876861}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_706994392}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x431384318}

[[时钟自动切换功能指的是]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_963645383}[接口在]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[模式下收到]{style="font-family:宋体"}[AIS/LOS]{lang="EN-US"}[告警后，接口自动切换成]{style="font-family:宋体"}**[master]{lang="EN-US"}**[模式。当告警消除后，接口自动切换成用户配置的时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_569084336}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_954656877}[开启]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[接口时钟自动切换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1245247953}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] clock-change auto]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x43765898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_1332643765}
:::

::: {#1985170611 .myid}
[]{#_Toc404783991}[]{#struct_0_x1622_x8463_790137198}[]{#_Toc345946854}

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- code**

------------------------------------------------------------------------

[**[code]{lang="EN-US"}**]{#struct_0_x1622_x8463_x618234202}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的线路编码格式。]{style="font-family:宋体"}

[**[undo code]{lang="EN-US"}**]{#struct_0_x1622_x8463_x617569178}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_569018800}

[[在]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1787125071}[接口视图下：]{style="font-family:宋体"}

[**[code]{lang="EN-US"}**[ { **ami** \| **hdb3** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x635807740}

[**[undo code]{lang="EN-US"}**]{#struct_0_x1622_x8463_579175745}

[[在]{style="font-family:宋体"}[ATM T1]{lang="EN-US"}]{#struct_0_x1622_x8463_1114029293}[接口视图下：]{style="font-family:宋体"}

[**[code]{lang="EN-US"}**[ { **ami** \| **b8zs** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1666173607}

[**[undo code]{lang="EN-US"}**]{#struct_0_x1622_x8463_x629375124}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x995253437}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_1786234799}[接口的线路编码为]{style="font-family:宋体"}[HDB3]{lang="EN-US"}[格式；]{style="font-family:宋体"}[ATM T1]{lang="EN-US"}[接口的线路编码为]{style="font-family:宋体"}[B8ZS]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568953264}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x2070774368}[接口视图]{style="font-family:宋体"}[/ATM T1]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1562553380}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_700100865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_209301311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1866797476}

[**[ami]{lang="EN-US"}**]{#struct_0_x1622_x8463_x545425443}[：配置]{style="font-family:宋体"}[ATM E1/T1]{lang="EN-US"}[线路编码为]{style="font-family:宋体"}[AMI]{lang="EN-US"}[（]{style="font-family:宋体"}[Alternate Mark Inversion]{lang="EN-US"}[，信号交替反转码）格式。]{style="font-family:宋体"}

[**[hdb3]{lang="EN-US"}**]{#struct_0_x1622_x8463_886682496}[：配置]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[线路编码为]{style="font-family:宋体"}[HDB3]{lang="EN-US"}[（]{style="font-family:宋体"}[High Density Bipolar 3]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[阶高密度双极性码）格式。]{style="font-family:宋体"}

[**[b8zs]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1254866741}[：配置]{style="font-family:宋体"}[ATM T1]{lang="EN-US"}[线路编码为]{style="font-family:宋体"}[B8ZS]{lang="EN-US"}[（]{style="font-family:宋体"}[Bipolar 8-zero substitution]{lang="EN-US"}[，双极性]{style="font-family:宋体"}[8zero]{lang="EN-US"}[替换码）格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568887728}

[[线路编码采用]{style="font-family:宋体"}[AMI]{lang="EN-US"}]{#struct_0_x1622_x8463_x2086616370}[格式时，请确保该接口工作在加扰模式（即使用]{style="font-family:宋体"}**[scramble]{lang="EN-US"}**[命令开启加扰功能）。]{style="font-family:宋体"}

[[两端]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x2099393139}[接口配置的线路编码格式要保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1683563185}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x415165912}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的线路编码为]{style="font-family:宋体"}[AMI]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1820733420}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] code ami]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1498246830}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1892901729}
:::

::: {#-48218953 .myid}
[]{#_Toc404783992}[]{#struct_0_x1622_x8463_568822192}[]{#_Toc345946855}

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- frame-format**

------------------------------------------------------------------------

[**[frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_990108488}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的帧格式。]{style="font-family:宋体"}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_1340937190}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_105839537}

[[在]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1521164756}[接口视图下：]{style="font-family:宋体"}

[**[frame-format]{lang="PT-BR"}**]{#struct_0_x1622_x8463_x1293112582}[ ]{lang="PT-BR"}[{]{lang="EN-US"}[ ]{lang="EN-US"}**[crc4-adm]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| ]{lang="EN-US"}**[no-crc4-adm]{lang="PT-BR"}**[ ]{lang="PT-BR"}[}]{lang="EN-US"}

[**[undo frame-format]{lang="PT-BR"}**]{#struct_0_x1622_x8463_1593754846}

[[在]{style="font-family:宋体"}[ATM T1]{lang="EN-US"}]{#struct_0_x1622_x8463_373238451}[接口视图下：]{style="font-family:宋体"}

[**[frame-format]{lang="PT-BR"}**]{#struct_0_x1622_x8463_x631490102}[ ]{lang="PT-BR"}[{]{lang="EN-US"}[ ]{lang="EN-US"}**[esf-adm]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| ]{lang="EN-US"}**[sf-adm]{lang="PT-BR"}**[ ]{lang="PT-BR"}[}]{lang="EN-US"}

[**[undo frame-format]{lang="PT-BR"}**]{#struct_0_x1622_x8463_568756656}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1237209102}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_1504593306}[的帧格式为]{style="font-family:宋体"}[CRC4 ADM]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM T1]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[ESF ADM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1299403093}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1741729827}[接口视图]{style="font-family:宋体"}[/ATM T1]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2102092876}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_734141419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1053206793}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x584409543}

[**[crc4-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_568691120}[：配置]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[帧格式为]{style="font-family:宋体"}[CRC4 ADM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-crc4-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_1199168001}[：配置]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[帧格式为]{style="font-family:宋体"}[No-CRC4 ADM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[esf-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_632927158}[：配置]{style="font-family:宋体"}[ATM T1]{lang="EN-US"}[帧格式为]{style="font-family:宋体"}[ESF ADM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sf-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_629705404}[：配置]{style="font-family:宋体"}[ATM T1]{lang="EN-US"}[帧格式为]{style="font-family:宋体"}[SF ADM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1516630640}

[[ADM]{lang="EN-US"}]{#struct_0_x1622_x8463_1618203565}[（]{style="font-family:宋体"}[ATM Direct Mapping]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[直接映射）是指当在]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}[线路上传输]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元时，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元可以直接映射到]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}[帧中，]{style="font-family:宋体"}[ITU−T]{lang="EN-US"}[建议]{style="font-family:宋体"}[G.804]{lang="EN-US"}[和]{style="font-family:宋体"}[ATM]{lang="EN-US"}[论坛分别定义了]{style="font-family:宋体"}[ATM]{lang="EN-US"}[直接映射的过程和帧格式，系统根据用户配置的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的帧格式自动选择对应的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[直接映射方式。]{style="font-family:宋体"}

[[两端]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_x586307689}[接口配置的帧格式要保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1233804687}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1061780657}[配置]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[使用]{style="font-family:宋体"}[No-CRC4 ADM]{lang="EN-US"}[帧格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_569674160}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] frame-format no-crc4-adm]{lang="EN-US"}
:::

::: {#-951370423 .myid}
[]{#_Toc404783993}[]{#struct_0_x1622_x8463_2111493044}[]{#_Toc345946856}

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_1712626515}[命令用来开启]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1173885415}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2035225661}

[**[loopback]{lang="EN-US"}**[ { **cell** \| **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x2116107957}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_x489987984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1622695128}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_569608624}[接口的环回检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_917582042}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_1787188121}[接口视图]{style="font-family:宋体"}[/ATM T1]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_280613500}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1513840143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1015020512}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1158961843}

[**[cell]{lang="EN-US"}**]{#struct_0_x1622_x8463_1287102694}[：设置接口对内信元环回。此方式可以用来检测本端物理芯片是否正常。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1622_x8463_1143836182}[：设置接口对内自环。此方式可以用来检测本端业务芯片是否正常。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1802336460}[：设置接口对外载荷环回。此方式可以用来检测数据负荷成帧是否正常。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1622_x8463_569149873}[：设置接口对外线路环回。此方式可以用来检测对端是否正常。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_573023063}

[[只有在进行某些特殊功能测试的时候，才将接口配置为对内自环或对外环回。正常工作时，不要启用环回检测功能。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1318452137}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_788802011}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1948147179}[开启]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[对外载荷环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x2145846093}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] loopback payload]{lang="SV"}
:::

::: {#-837106270 .myid}
[]{#_Toc404783994}[]{#struct_0_x1622_x8463_977556064}[]{#_Toc345946857}

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- scramble**

------------------------------------------------------------------------

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_1724011143}[命令用来开启]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口对载荷的加扰功能。]{style="font-family:宋体"}

[**[undo scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_569084337}[命令用来关闭加扰功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_954656878}

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1245247958}

[**[undo scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x90820065}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2232133}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_987988074}[接口对载荷的加扰功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x108112997}

[[ATM E1]{lang="EN-US"}]{#struct_0_x1622_x8463_x949614686}[接口视图]{style="font-family:宋体"}[/ATM T1]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1344520404}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_569018801}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1787125072}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x232523213}

[[开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1622_x8463_x578398448}[或]{style="font-family:宋体"}[0]{lang="EN-US"}[，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口都打开或关闭对载荷的加扰功能，才能对接成功。]{style="font-family:宋体"}

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x325296799}[命令只对载荷进行加扰和解扰，不影响信元头。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2057639799}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_211044616}[开启]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}[接口对载荷的加扰功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x256581028}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] scrambl[e]{#_Toc345946858}]{lang="EN-US"}
:::

::: {#-620300078 .myid}
[]{#_Toc404783996}[]{#struct_0_x1622_x8463_568953265}[]{#_Toc345946859}

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- cable**

------------------------------------------------------------------------

[**[cable]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2070774369}[命令用来配置]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[接口的电缆模式。]{style="font-family:宋体"}

[**[undo cable]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1166329975}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x667499243}

[**[cable]{lang="EN-US"}**[ { **long** \| **short** }]{lang="EN-US"}]{#struct_0_x1622_x8463_1739714826}

[**[undo cable]{lang="EN-US"}**]{#struct_0_x1622_x8463_1221149259}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1022210759}

[[电缆模式为短距模式。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1368778264}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1083855207}

[[ATM T3]{lang="EN-US"}]{#struct_0_x1622_x8463_568887729}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2086616369}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_985786112}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1494273800}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1855915234}

[**[long]{lang="EN-US"}**]{#struct_0_x1622_x8463_x133193596}[：长距模式，电缆长度为]{style="font-family:宋体"}[151]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[米。]{style="font-family:宋体"}

[**[short]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1845143900}[：短距模式，电缆长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[150]{lang="EN-US"}[米。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_915319217}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1806784967}[配置]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[使用长距模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_568822193}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] cable long]{lang="EN-US"}
:::

::: {#-441129672 .myid}
[]{#_Toc404783997}[]{#struct_0_x1622_x8463_990108489}[]{#_Toc345946860}[]{#_Toc349121878}[]{#_Toc349122035}[]{#_Toc349121879}[]{#_Toc349122036}[]{#_Toc349121880}[]{#_Toc349122037}[]{#_Toc349121881}[]{#_Toc349122038}[]{#_Toc349121882}[]{#_Toc349122039}

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_1340937189}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_106298288}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1511638045}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1622_x8463_1929808863}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1622_x8463_x766126154}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_300932189}

[[时钟模式为从时钟模式（]{style="font-family:宋体"}]{#struct_0_x1622_x8463_568756657}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1237209101}

[[ATM E3]{lang="EN-US"}]{#struct_0_x1622_x8463_1504396698}[接口视图]{style="font-family:宋体"}[/ATM T3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1017908537}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x401168171}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x2025089614}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1710099426}

[**[master]{lang="EN-US"}**]{#struct_0_x1622_x8463_1289237859}[：设置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式为主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1622_x8463_884397448}[：设置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的时钟模式为从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568691121}

[[当作为]{style="font-family:宋体"}[DCE]{lang="EN-US"}]{#struct_0_x1622_x8463_1199168000}[设备使用时，应配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口使用主时钟模式；作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备使用时，应配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口使用从时钟模式。]{style="font-family:宋体"}

[[当两台路由器的]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_632861622}[接口通过光纤直连时，应该将一端的时钟配置为主时钟模式，另一端为从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1329320963}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_501961133}[设置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[上的时钟为主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1742241719}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] clock master]{lang="SV"}
:::

::: {#1622283305 .myid}
[]{#_Toc404783998}[]{#struct_0_x1622_x8463_384091686}[]{#_Toc345946861}

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- frame-format**

------------------------------------------------------------------------

[**[frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1332117871}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的帧格式。]{style="font-family:宋体"}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_569674161}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2111493043}

[[在]{style="font-family:宋体"}[ATM E3]{lang="EN-US"}]{#struct_0_x1622_x8463_1712429907}[接口视图下：]{style="font-family:宋体"}

[**[frame-format]{lang="EN-US"}**[ { **g751-adm** \| **g751-plcp** \| **g832-adm** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1179175715}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1186885141}

[[在]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}]{#struct_0_x1622_x8463_686578658}[接口视图下：]{style="font-family:宋体"}

[**[frame-format]{lang="EN-US"}**[ { **cbit-adm** \| **cbit-plcp** \| **m23-adm** \| **m23-plcp** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1937510182}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_x1622_x8463_1153687669}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x520817524}

[[ATM E3]{lang="EN-US"}]{#struct_0_x1622_x8463_569608625}[接口的帧格式为]{style="font-family:宋体"}[G.751 PLCP]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[接口的帧格式为]{style="font-family:宋体"}[C-bit PLCP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_917582043}

[[ATM E3]{lang="EN-US"}]{#struct_0_x1622_x8463_1787188120}[接口视图]{style="font-family:宋体"}[/ATM T3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_280547964}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1199059292}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1724235983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x685410643}

[**[g751-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x249936659}[：配置]{style="font-family:宋体"}[ATM E3]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[G.751]{lang="EN-US"}[直接成帧。]{style="font-family:宋体"}

[**[g751-plcp]{lang="EN-US"}**]{#struct_0_x1622_x8463_1358648846}[：配置]{style="font-family:宋体"}[ATM E3]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[G.751 PLCP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g832-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_569149870}[：配置]{style="font-family:宋体"}[ATM E3]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[G.823]{lang="EN-US"}[直接成帧。]{style="font-family:宋体"}

[**[cbit-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_573023060}[：配置]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[C-bit]{lang="EN-US"}[直接成帧。]{style="font-family:宋体"}

[**[cbit-plcp]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1318452136}[：配置]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[C-bit PLCP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[m23-adm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x777281930}[：配置]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[M23]{lang="EN-US"}[直接成帧。]{style="font-family:宋体"}

[**[m23-plcp]{lang="EN-US"}**]{#struct_0_x1622_x8463_1634962752}[：配置]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[M23 PLCP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_185204012}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1004722925}[配置]{style="font-family:宋体"}[ATM E3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[使用的帧格式为]{style="font-family:宋体"}[G.832]{lang="EN-US"}[直接成帧。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x244978571}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] frame-format g832-adm]{lang="DA"}
:::

::: {#498463274 .myid}
[]{#_Toc404783999}[]{#struct_0_x1622_x8463_569084334}[]{#_Toc345946862}

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_954656875}[命令用来开启接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1245247955}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x850334952}

[**[loopback]{lang="EN-US"}**[ { **cell** \| **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x825090111}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1327693709}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1885666096}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_680616045}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1508181511}

[[ATM E3]{lang="EN-US"}]{#struct_0_x1622_x8463_569018798}[接口视图]{style="font-family:宋体"}[/ATM T3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2107292716}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_455355890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1536931080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1946640544}

[**[cell]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1104575213}[：设置接口对内信元环回。此方式可以用来检测本端物理芯片是否正常。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1096320998}[：设置接口对内自环。此方式可以用来检测本端业务芯片是否正常。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_x1622_x8463_x640339010}[：设置接口对外载荷环回。此方式可以用来检测数据负荷成帧是否正常。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1622_x8463_1549085310}[：设置接口对外线路环回。此方式可以用来检测对端是否正常。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568953262}

[[只有在进行某些特殊功能测试的时候，才将接口配置为对内自环或对外环回。正常工作时，不要启用环回检测功能。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x2070774370}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1918849276}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x316328865}[开启]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[对外载荷环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_31684378}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] loopback payloa[d]{#_Toc345946863}]{lang="EN-US"}
:::

::: {#1013840085 .myid}
[]{#_Toc404784000}[]{#struct_0_x1622_x8463_x1243057138}

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- scramble**

------------------------------------------------------------------------

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1681301360}[命令用来开启]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口对载荷的加扰功能。]{style="font-family:宋体"}

[**[undo scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_600099377}[命令用来关闭加扰功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568887726}

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2086616364}

[**[undo scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x129959135}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1878989615}

[[ATM]{lang="EN-US"}]{#struct_0_x1622_x8463_1888754286}[接口对载荷的加扰功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1552042357}

[[ATM E3]{lang="EN-US"}]{#struct_0_x1622_x8463_1533426655}[接口视图]{style="font-family:宋体"}[/ATM T3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_256912221}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1844064288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_568822190}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_990108490}

[[开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1622_x8463_x997714978}[或]{style="font-family:宋体"}[0]{lang="EN-US"}[，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口都打开或关闭对载荷的加扰功能，才能对接成功。]{style="font-family:宋体"}

[**[scramble]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1885341517}[命令只对载荷进行加扰和解扰，不影响信元头。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x80023372}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1586267101}[开启]{style="font-family:宋体"}[ATM T3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[对载荷的加扰功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1498417556}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] scrambl[e]{#_Toc345946864}]{lang="EN-US"}
:::

::: {#1797341627 .myid}
[]{#_Toc404784002}[]{#struct_0_x1622_x8463_1504462234}

**ATM接口 \-- ADSL接口配置命令 \-- activate**

------------------------------------------------------------------------

[**[activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2037564878}[命令用来激活]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x437365876}[命令用来去激活]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1742365902}

[**[activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x393161871}

[**[undo activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x241848062}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568691118}

[[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1139484167}[接口处于激活状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1910874213}

[[ATM ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1307912568}[接口视图]{style="font-family:宋体"}[/ATM ADSL 2+]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1729922655}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1891206612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1077559844}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x67298579}

[[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_1283678395}[（]{style="font-family:宋体"}[Customer Premises Equipment]{lang="EN-US"}[，用户侧设备）设备上的]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口在进行业务传输前必须先激活。]{style="font-family:宋体"}

[[激活是指局端设备]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_569674158}[（]{style="font-family:宋体"}[Central Office]{lang="EN-US"}[，中心局）与用户]{style="font-family:宋体"}[CPE]{lang="EN-US"}[之间进行的一系列的握手训练和交换信息的操作。激活过程将根据]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备的线路配置模板中制定的]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[标准、通道方式、上下行线路速率、规定的噪声容限等设定，检测线路距离和线路状况，在]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备与]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备之间进行协商，确认能否在上述条件下正常工作。如果激活成功，则在]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备与]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备建立起了通信连接，此时，就可以传输业务了。]{style="font-family:宋体"}

[[线路激活协商连接参数时，]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x227159124}[设备处于主导地位，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备处于从属地位，也就是说，大多数连接参数都是由]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备提供并拥有最终的决定权。典型的激活时间是]{style="font-family:宋体"}[30]{lang="EN-US"}[秒（激活时间是指从线路开始协商到线路]{style="font-family:宋体"}[up]{lang="EN-US"}[的时间）。]{style="font-family:宋体"}

[[激活的相反操作是去激活。去激活后，]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_1352342086}[设备与]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备建立通信的连接不再存在。]{style="font-family:宋体"}

[[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1045152778}[不同于]{style="font-family:宋体"}[DDR]{lang="EN-US"}[，]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[是永远在线的。所以，路由器开机后]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口会自己启动激活任务，进入激活状态。只要线路良好，就应该始终处于激活状态。路由器会定时检测线路的状态，如果线路质量恶化，路由器会自动将线路去激活，重新训练，重新激活。]{style="font-family:宋体"}

[[本命令用于手工的激活]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1622_x8463_x2132785082}[去激活]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口，主要在测试和故障诊断时使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1710685486}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1030266181}[激活]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_988035337}

[\[Sysname\] interface atm2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] activate]{lang="EN-US"}
:::

::: {#-1693812261 .myid}
[]{#_Toc404784003}[]{#struct_0_x1622_x8463_569608622}[]{#_Toc345946866}[]{#_Toc349121889}[]{#_Toc349122046}[]{#_Toc349121890}[]{#_Toc349122047}[]{#_Toc349121891}[]{#_Toc349122048}[]{#_Toc349121892}[]{#_Toc349122049}[]{#_Toc349121893}[]{#_Toc349122050}

**ATM接口 \-- ADSL接口配置命令 \-- adsl standard**

------------------------------------------------------------------------

[**[adsl standard]{lang="EN-US"}**]{#struct_0_x1622_x8463_917582048}[命令用来配置]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口使用的工作标准。]{style="font-family:宋体"}

[**[undo adsl standard]{lang="EN-US"}**]{#struct_0_x1622_x8463_1787188111}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_280613497}

[[在]{style="font-family:宋体"}[ATM ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x405739155}[接口视图下：]{style="font-family:宋体"}

[**[adsl standard]{lang="EN-US"}**[ { **auto** \| **gdmt** \| **glite** \| **t1413** }]{lang="EN-US"}]{#struct_0_x1622_x8463_1228540661}

[**[undo adsl standard]{lang="EN-US"}**]{#struct_0_x1622_x8463_x724815049}

[[在]{style="font-family:宋体"}[ATM ADSL 2+]{lang="EN-US"}]{#struct_0_x1622_x8463_x532831226}[接口视图下：]{style="font-family:宋体"}

[**[adsl standard]{lang="EN-US"}**[ { **auto** \| **g9923** \| **g9925** \| **gdmt** \| **glite** \| **t1413** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x2100269443}

[**[undo adsl standard]{lang="EN-US"}**]{#struct_0_x1622_x8463_569149871}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_573023061}

[[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1318452135}[接口使用的工作标准是自适应方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1951601425}

[[ATM ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_2065281074}[接口视图]{style="font-family:宋体"}[/ATM ADSL 2+]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1655981153}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1600019755}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x994099871}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x461239349}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_569084335}[：自适应方式。由]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口芯片自动与对端协商使用的工作标准。]{style="font-family:宋体"}

[**[g9923]{lang="EN-US"}**]{#struct_0_x1622_x8463_954656876}[：使用]{style="font-family:宋体"}[ADSL2(G992.3)]{lang="EN-US"}[标准。]{style="font-family:宋体"}

[**[g9925]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1245247952}[：使用]{style="font-family:宋体"}[ADSL2+(G992.5)]{lang="EN-US"}[标准。]{style="font-family:宋体"}

[**[gdmt]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1609849839}[：使用]{style="font-family:宋体"}[G.DMT]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.1]{lang="EN-US"}[）标准。]{style="font-family:宋体"}

[**[glite]{lang="EN-US"}**]{#struct_0_x1622_x8463_x996290149}[：使用]{style="font-family:宋体"}[G.Lite]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.2]{lang="EN-US"}[）标准。]{style="font-family:宋体"}

[**[t1413]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1830804097}[：使用]{style="font-family:宋体"}[T1.413]{lang="EN-US"}[标准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1810973050}

[[ADSL-I]{lang="EN-US"}]{#struct_0_x1622_x8463_1825536552}[模块不支持]{style="font-family:宋体"}[G.Lite]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.2]{lang="EN-US"}[）和]{style="font-family:宋体"}[T1.413]{lang="EN-US"}[标准。]{style="font-family:宋体"}

[[两端]{style="font-family:宋体"}[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1747629564}[接口需要使用相同的工作标准。]{style="font-family:宋体"}

[[该项配置不会立即生效，只有下一次激活或开启接口后才能够起作用。如果用户要立即生效，可以执行]{style="font-family:宋体"}]{#struct_0_x1622_x8463_569018799}**[shutdown]{lang="EN-US"}**[/]{lang="EN-US"}**[undo shutdown]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[undo activate]{lang="EN-US"}**[/]{lang="EN-US"}**[activate]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2107292715}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_455159282}[配置]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[接口使用的工作标准为]{style="font-family:宋体"}[T1.413]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_2062821116}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] adsl standard t1413]{lang="EN-US"}
:::

::: {#-1538067523 .myid}
[]{#_Toc404784004}[]{#struct_0_x1622_x8463_x356009249}[]{#_Toc345946867}[]{#_Toc349121895}[]{#_Toc349122052}[]{#_Toc349121896}[]{#_Toc349122053}[]{#_Toc349121899}[]{#_Toc349122056}

**ATM接口 \-- ADSL接口配置命令 \-- adsl tx-attenuation**

------------------------------------------------------------------------

[**[adsl tx-attenuation]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1346100770}[命令用来配置]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口的发送功率衰减值。]{style="font-family:宋体"}

[**[undo adsl tx-attenuation]{lang="EN-US"}**]{#struct_0_x1622_x8463_x539118041}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1778809117}

[**[adsl tx-attenuation]{lang="EN-US"}**[ *attenuation*]{lang="EN-US"}]{#struct_0_x1622_x8463_568953263}

[**[undo adsl tx-attenuation]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2070774371}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x810034079}

[[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x712793054}[接口的发送功率衰减值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示不衰减。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_802780401}

[[ATM ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1569162234}[接口视图]{style="font-family:宋体"}[/ATM ADSL 2+]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x36882614}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1181080934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1302038669}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_568887727}

[*[attenuation]{lang="EN-US"}*]{#struct_0_x1622_x8463_x2086616363}[：发送功率的衰减值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x533243662}

[[本命令的配置会影响]{style="font-family:宋体"}[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x142518651}[接口发送信号功率的大小。配置的衰减值越大，表示发送功率越小；配置的衰减值越小，表示发送功率越大。如果发送功率太大，可能会影响其它]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口发送的信号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1084639732}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1565959827}[配置]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口的发送功率衰减值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_277815913}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] adsl tx-attenuation 10]{lang="EN-US"}
:::

::::: {#-520666389 .myid}
[]{#_Toc404784005}[]{#struct_0_x1622_x8463_x85455184}[]{#_Toc345946868}[]{#_Toc349121901}[]{#_Toc349122058}[]{#_Toc349121902}[]{#_Toc349122059}[]{#_Toc349121905}[]{#_Toc349122062}

**ATM接口 \-- ADSL接口配置命令 \-- display dsl configuration**

------------------------------------------------------------------------

[**[display dsl configuration]{lang="EN-US"}**]{#struct_0_x1622_x8463_568822191}[命令用来显示]{style="font-family:
宋体"}[ADSL]{lang="EN-US"}[接口的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_990108491}

[**[display dsl configuration interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x997714979}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1885407053}

[[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_380539319}[任意视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_519612021}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x5159029}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_924781231}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_744716591}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_568756655}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1237209099}

[**[interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x452442735}[：显示指定]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_978520404}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_717842347}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x1226404047}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2038332750}[显示]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl configuration interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_568691119}

[Line Params Set by User:]{lang="EN-US"}

[  Standard:               T1.413]{lang="EN-US"}

[  Annex:                  A]{lang="EN-US"}

[  Coding Gain(dB):        Auto]{lang="EN-US"}

[  Tx Pow Attn(dB):        0]{lang="EN-US"}

[  Bit-Swap:               disable]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Actual Config           Near End        Far End]{lang="EN-US"}

[ ]{lang="EN-US"}[Standard:               T1.413          T1.413]{lang="FR"}

[ ]{lang="EN-US"}[Trellis Coding:         Enable          Enable]{lang="FR"}

[ Vendor ID:              0x0039          0x0004]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         AS0 (DS)        LS0(US)]{lang="EN-US"}

[ Rate(Bytes):            238             26]{lang="EN-US"}

[ Rate(kbps):             7616            832]{lang="EN-US"}

[ Latency:                Intlv           Intlv]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display dsl configuration]{lang="EN-US"}]{#struct_0_x1622_x8463_x1139484168}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x830485288}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1980808556}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1085565259}

[[以下信息为配置信息：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_569674159}

[[Standard]{lang="EN-US"}]{#struct_0_x1622_x8463_x227159125}

[[接口链路配置的标准：（此参数可以通过]{style="font-family:宋体"}**[adsl standard]{lang="EN-US"}**]{#struct_0_x1622_x8463_1352407622}[命令进行配置）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1622_x8463_2099573842}[：自适应方式（缺省情况标准值）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.3]{lang="EN-US"}]{#struct_0_x1622_x8463_x1174278526}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.3]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.5]{lang="EN-US"}]{#struct_0_x1622_x8463_x187693527}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2+]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.5]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.1]{lang="EN-US"}]{#struct_0_x1622_x8463_1825755279}[：使用]{lang="EN-US" style="font-family:宋体"}[G.DMT]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.1]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.2]{lang="EN-US"}]{#struct_0_x1622_x8463_569608623}[：使用]{lang="EN-US" style="font-family:宋体"}[G.Lite]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.2]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T1.413]{lang="EN-US"}]{#struct_0_x1622_x8463_917582049}[：使用]{lang="EN-US" style="font-family:宋体"}[T1.413]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[Annex]{lang="EN-US"}]{#struct_0_x1622_x8463_1787188110}

[[接口链路所采用的附加标准：（此参数为预设值，用户不能修改）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_280547961}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_1199059297}[：]{lang="EN-US" style="font-family:宋体"}[Annex A]{lang="EN-US"}[标准（表示]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口类型为]{lang="EN-US" style="font-family:宋体"}[ADSL over POTS]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_x1622_x8463_x1724563663}[：]{lang="EN-US" style="font-family:宋体"}[Annex B]{lang="EN-US"}[标准（表示]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口类型为]{lang="EN-US" style="font-family:宋体"}[ADSL over ISDN]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[Coding Gain(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_2135233815}

[[接口线路所采用的编码增益，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}]{#struct_0_x1622_x8463_x1511293708}[（此参数为预设值，用户不能修改）]{style="font-family:宋体"}

[[Auto]{lang="EN-US"}]{#struct_0_x1622_x8463_x987614169}[表示自动协商编码增益]{style="font-family:宋体"}

[[Tx Pow Attn(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_x423749734}

[[接口链路的发送功率衰减，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}]{#struct_0_x1622_x8463_1076239089}[（此参数为预设值，用户不能修改）]{style="font-family:宋体"}

[[Bit-Swap]{lang="EN-US"}]{#struct_0_x1622_x8463_2135168279}

[[比特交换功能使能情况（此参数为预设值，用户不能修改）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1975210742}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e]{lang="EN-US"}[nable]{lang="EN-US"}]{#struct_0_x1622_x8463_2069135972}[：]{lang="EN-US" style="font-family:宋体"}[使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disable]{lang="EN-US"}]{#struct_0_x1622_x8463_736726506}[：]{lang="EN-US" style="font-family:宋体"}[未使能]{style="font-family:宋体"}

[[以下信息只有在线路激活以后才会显示：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2135102743}

[[Standard]{lang="EN-US"}]{#struct_0_x1622_x8463_1557066091}

[[接口实际生效的标准：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2105567591}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1622_x8463_x1417185964}[：自适应方式（缺省情况标准值）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.3]{lang="EN-US"}]{#struct_0_x1622_x8463_107448463}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.3]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.5]{lang="EN-US"}]{#struct_0_x1622_x8463_2135037207}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2+]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.5]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.1]{lang="EN-US"}]{#struct_0_x1622_x8463_x1925338423}[：使用]{lang="EN-US" style="font-family:宋体"}[G.DMT]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.1]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.2]{lang="EN-US"}]{#struct_0_x1622_x8463_1657506105}[：使用]{lang="EN-US" style="font-family:宋体"}[G.Lite]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.2]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T1.413]{lang="EN-US"}]{#struct_0_x1622_x8463_x179410741}[：使用]{lang="EN-US" style="font-family:宋体"}[T1.413]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[Trellis Coding]{lang="EN-US"}]{#struct_0_x1622_x8463_2134971671}

[[网格编码功能使能情况：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1555328337}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[nable]{lang="EN-US"}]{#struct_0_x1622_x8463_x612798426}[：]{lang="EN-US" style="font-family:宋体"}[使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[isable]{lang="EN-US"}]{#struct_0_x1622_x8463_171997077}[：]{lang="EN-US" style="font-family:宋体"}[未使能]{style="font-family:宋体"}

[[Vendor ID]{lang="EN-US"}]{#struct_0_x1622_x8463_2134906135}

[[厂商]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1622_x8463_1978146328}[，表示生产芯片的厂商编号]{style="font-family:宋体"}

[[Rate(Bytes)]{lang="EN-US"}]{#struct_0_x1622_x8463_x1553665912}

[[表示协商速率，]{style="font-family:宋体"}[AS0 (DS)]{lang="EN-US"}]{#struct_0_x1622_x8463_x1119686095}[下行，]{style="font-family:宋体"}[LS0 (US)]{lang="EN-US"}[上行，单位是]{style="font-family:宋体"}[Bytes]{lang="EN-US"}

[[Rate(kbps)]{lang="EN-US"}]{#struct_0_x1622_x8463_2134840599}

[[表示协商速率，]{style="font-family:宋体"}[AS0 (DS)]{lang="EN-US"}]{#struct_0_x1622_x8463_x397736037}[下行，]{style="font-family:宋体"}[LS0 (US)]{lang="EN-US"}[上行，单位是]{style="font-family:宋体"}[kbps]{lang="EN-US"}

[[Latency]{lang="EN-US"}]{#struct_0_x1622_x8463_1404505985}

[[表示使用的数据编码模式：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1273129558}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[Fast]{lang="EN-US"}]{#struct_0_x1622_x8463_2134775063}[：快速模式（该模式的特点：线路时延较小，线路质量较差）]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interleave]{lang="EN-US"}]{#struct_0_x1622_x8463_31572346}[：交织模式（该模式的特点：纠错能力强，线路时延较大）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-58748941 .myid}
[]{#_Toc404784006}[]{#struct_0_x1622_x8463_x2100149596}[]{#_Toc345946869}

**ATM接口 \-- ADSL接口配置命令 \-- display dsl status**

------------------------------------------------------------------------

[**[display dsl status]{lang="EN-US"}**]{#struct_0_x1622_x8463_1300016999}[命令用来显示]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1068240151}

[**[display dsl status interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x1956031471}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1831391393}

[[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_1389273244}[任意视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1493369629}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2135758103}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x411390637}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_855822911}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_1067216663}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1760489550}

[**[interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x1248262358}[：显示指定]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_296305328}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x848255724}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x1915309351}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2135692567}[显示]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl status interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_1151463956}

[Line Status:            Loss Of Signal]{lang="EN-US"}

[Training Status:        Idle]{lang="EN-US"}

[ ]{lang="EN-US"}

[Active Params           Near End        Far End]{lang="EN-US"}

[Standard:               G.dmt           G.dmt]{lang="EN-US"}

[SNR (dB):               0.0             0.0]{lang="EN-US"}

[Attn(dB):               0.0             0.0]{lang="EN-US"}

[Pwr(dBm):               0.0             0.0]{lang="EN-US"}

[Current Rate(kbps):     0               0]{lang="EN-US"}

[Latency:                Intl            Intl]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display dsl status]{lang="EN-US"}]{#struct_0_x1622_x8463_1594410679}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x834953108}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x565487577}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2135233816}

[[Line Status]{lang="EN-US"}]{#struct_0_x1622_x8463_x1511359244}

[[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_782233730}[链路当前所处的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No Defect]{lang="EN-US"}]{#struct_0_x1622_x8463_x71457442}[[：正常状态]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loss Of Frame]{lang="EN-US"}]{#struct_0_x1622_x8463_x566909717}[[：帧错误]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loss Of Signal]{lang="EN-US"}]{#struct_0_x1622_x8463_478671210}[[：信号错误]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loss Of Power]{lang="EN-US"}]{#struct_0_x1622_x8463_2135168280}[[：电源错误]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loss Of Signal Quality]{lang="EN-US"}]{#struct_0_x1622_x8463_x1974751975}[[：信号质量错误]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1622_x8463_2120564560}[[：未知]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[Training Status]{lang="EN-US"}]{#struct_0_x1622_x8463_x1793501928}

[[ADSL]{lang="EN-US"}]{#struct_0_x1622_x8463_682176032}[链路同]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[（]{style="font-family:宋体"}[Digital Subscriber Line Access Multiplexer]{lang="EN-US"}[，数字用户线路接入复用器）设备训练过程中所处的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x1622_x8463_x1514465962}[[：空闲]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G.994 Training]{lang="EN-US"}]{#struct_0_x1622_x8463_2135102744}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[G.994]{lang="EN-US"}[[训练]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G.992 Started]{lang="EN-US"}]{#struct_0_x1622_x8463_1557393771}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[G.992]{lang="EN-US"}[[开始]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G.922 Channel Analysis]{lang="EN-US"}]{#struct_0_x1622_x8463_x1818048669}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[G.922]{lang="EN-US"}[[通道分析]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G.992 Message Exchange]{lang="EN-US"}]{#struct_0_x1622_x8463_x904799610}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[G.992]{lang="EN-US"}[[消息交换]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Showtime]{lang="EN-US"}]{#struct_0_x1622_x8463_x532411655}[[：正常数据交换]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1622_x8463_2135037208}[[：未知]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[以下信息只有在线路激活以后才会显示：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1925928247}

[[Active Params]{lang="EN-US"}]{#struct_0_x1622_x8463_1212784932}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standard]{lang="EN-US"}]{#struct_0_x1622_x8463_x293677261}[：]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[链路同]{lang="EN-US" style="font-family:宋体"}[DSLAM]{lang="EN-US"}[设备当前的连接标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SNR]{lang="EN-US"}]{#struct_0_x1622_x8463_x2027906300}[：当前]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[链路的信噪比，信噪比越大，表示信号质量越好]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Attn]{lang="EN-US"}]{#struct_0_x1622_x8463_2134971672}[：当前]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[链路的衰减，衰减越大，说明线路状况越差]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pwr]{lang="EN-US"}]{#struct_0_x1622_x8463_x1555393873}[：当前]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[模块的发射能量，单位为]{style="font-family:宋体"}[dbm]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Current Rate]{lang="EN-US"}]{#struct_0_x1622_x8463_x856518720}[：]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[链路的速率，单位为]{lang="EN-US" style="font-family:宋体"}[kbps]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Latency]{lang="EN-US"}]{#struct_0_x1622_x8463_1045927744}[：]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[链路的数据编码模式，分为]{lang="EN-US" style="font-family:宋体"}[Intl]{lang="EN-US"}[（交织）和]{lang="EN-US" style="font-family:宋体"}[Fast]{lang="EN-US"}[（快速）两种]{lang="EN-US" style="font-family:宋体"}

[[Near End]{lang="EN-US"}]{#struct_0_x1622_x8463_2134906136}[表示下行方向（接口接收报文的方向），]{style="font-family:宋体"}[Far End]{lang="EN-US"}[表示上行方向（接口发送报文的方向）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-42155287 .myid}
[]{#_Toc404784007}[]{#struct_0_x1622_x8463_1977949720}[]{#_Toc345946870}

**ATM接口 \-- ADSL接口配置命令 \-- display dsl version**

------------------------------------------------------------------------

[**[display dsl version]{lang="EN-US"}**]{#struct_0_x1622_x8463_x497804693}[命令用来显示]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口的版本信息和支持的能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1498020124}

[**[display dsl version interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x1827186513}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1939844578}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_528045980}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1595263307}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x365289475}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_2134840600}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1175652242}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x1743381001}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1735591858}

[**[interface atm]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_1204920279}*[interface-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口的版本信息和支持的能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x531225914}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_436968170}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_427930666}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2134775064}[显示]{style="font-family:宋体"}[ADSL]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的版本信息和支持的能力。]{style="font-family:宋体"}

[[\<Sysname\> display dsl version interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_2135758104}

[ADSL board chipset and version info:]{lang="EN-US"}

[  DSL Line Type:          ADSL Over Pots]{lang="EN-US"}

[  Chipset Vendor:         BDCM]{lang="EN-US"}

[  FW Release:             A2pB017l.d15h]{lang="EN-US"}

[  DSP Version:            17.1200]{lang="EN-US"}

[  AFE Version:            1.0]{lang="EN-US"}

[  Bootrom Version:        1.1]{lang="EN-US"}

[  Hardware Version:       4.0]{lang="EN-US"}

[  Driver Version:         1.3]{lang="EN-US"}

[  CPLD Version:           1.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADSL Capability:]{lang="EN-US"}

[  ANNEX Supported:]{lang="EN-US"}

[    ANNEX A]{lang="EN-US"}

[  Standard Supported:]{lang="EN-US"}

[    ANSI T1.413 Issue 2]{lang="EN-US"}

[    ITU G992.1(G.dmt)]{lang="EN-US"}

[    ITU G992.2(G.lite)]{lang="EN-US"}

[    ITU G992.3(Adsl2)]{lang="EN-US"}

[    ITU G992.3(ReAdsl2)]{lang="EN-US"}

[    ITU G992.5(Adsl2p)]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display adsl version]{lang="EN-US"}]{#struct_0_x1622_x8463_x411718317}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x807926916}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x344623207}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_252026101}

[[ADSL board chipset and version info]{lang="EN-US"}]{#struct_0_x1622_x8463_1415682998}

[[接口板的版本信息和厂商信息]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1032657844}

[[DSL Line Type]{lang="EN-US"}]{#struct_0_x1622_x8463_x392513788}

[[用户接入线的类型，取值为]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2135692568}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADSL over ISDN]{lang="EN-US"}]{#struct_0_x1622_x8463_1151660564}[：]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[承载在]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[线路上，]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[信号的频段分布在比较高的频段，]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[信号的频段分布在比较低的频段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADSL Over Pots]{lang="EN-US"}]{#struct_0_x1622_x8463_1955669193}[：]{lang="EN-US" style="font-family:宋体"}[ADSL]{lang="EN-US"}[承载在电话线路上]{lang="EN-US" style="font-family:宋体"}

[[Chipset Vendor]{lang="EN-US"}]{#struct_0_x1622_x8463_1378637075}

[[ADSL Chipsets]{lang="EN-US"}]{#struct_0_x1622_x8463_1708948421}[的厂商标识]{style="font-family:宋体"}

[[FW Release]{lang="EN-US"}]{#struct_0_x1622_x8463_x199047268}

[[FirmWare]{lang="EN-US"}]{#struct_0_x1622_x8463_2135233813}[的标识和版本信息]{style="font-family:宋体"}

[[DSP Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x1511686924}

[[DSP]{lang="EN-US"}]{#struct_0_x1622_x8463_x211382156}[版本]{style="font-family:宋体"}

[[AFE Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x2118588149}

[[AFE]{lang="EN-US"}]{#struct_0_x1622_x8463_x2121877684}[版本]{style="font-family:宋体"}

[[Bootrom Version]{lang="EN-US"}]{#struct_0_x1622_x8463_514130676}

[[Bootrom]{lang="EN-US"}]{#struct_0_x1622_x8463_2135168277}[的版本号]{style="font-family:宋体"}

[[Hardware Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x1974293238}

[[接口板硬件的版本号]{style="font-family:宋体"}]{#struct_0_x1622_x8463_824627384}

[[Driver Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x418060030}

[[驱动软件的版本号]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2135102741}

[[CPLD Version]{lang="EN-US"}]{#struct_0_x1622_x8463_1557197163}

[[逻辑器件的版本号]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1298461882}

[[ADSL Capability]{lang="EN-US"}]{#struct_0_x1622_x8463_x927538282}

[[该接口支持的标准及其附加标准]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1025353241}

[ ]{lang="EN-US"}

::: {#378004530 .myid}
[]{#_Toc404784009}[]{#struct_0_x1622_x8463_1309745254}[]{#_Toc345946872}

**ATM接口 \-- G.SHDSL接口配置命令 \-- activate**

------------------------------------------------------------------------

[**[activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1857262955}[命令用来激活]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_2134971669}[命令用来去激活]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1554804048}

[**[activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_662606941}

[**[undo activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x888000564}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1184908292}

[[接口处于激活状态。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1595855228}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x177097353}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x695973731}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2134906133}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1977753112}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x2124568254}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1177515630}

[[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1672594769}[设备上的]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[类型的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口在进行业务传输前必须先激活。]{style="font-family:宋体"}

[[激活是指局端设备]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x1298833977}[（]{style="font-family:宋体"}[Central Office]{lang="EN-US"}[，中心局）与用户]{style="font-family:宋体"}[CPE]{lang="EN-US"}[之间进行的一系列的握手训练和交换信息的操作。激活过程将根据]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备的线路配置模板中制定的]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[标准、通道方式、上下行线路速率、规定的噪声容限等设定，检测线路距离和线路状况，在]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备与]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备之间进行协商，确认能否在上述条件下正常工作。如果激活成功，则在]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备与]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备建立起了通信连接，此时，就可以传输业务了。]{style="font-family:宋体"}

[[线路激活协商连接参数时，]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x130987434}[设备处于主导地位，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备处于从属地位，也就是说，大多数连接参数都是由]{style="font-family:宋体"}[CO]{lang="EN-US"}[设备提供并拥有最终的决定权。典型的激活时间是]{style="font-family:宋体"}[30]{lang="EN-US"}[秒（激活时间是指从线路开始协商到线路]{style="font-family:宋体"}[up]{lang="EN-US"}[的时间）。]{style="font-family:宋体"}

[[激活的相反操作是去激活。去激活后，]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x112032474}[设备与]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备建立通信的连接不再存在。]{style="font-family:宋体"}

[[SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1112741760}[类型的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口是永远在线的。所以，路由器开机后]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[类型的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口会自己启动激活任务，进入激活状态。只要线路良好，就应该始终处于激活状态。路由器会定时检测线路的状态，如果线路质量恶化，路由器会自动将线路去激活，重新训练，重新激活。]{style="font-family:宋体"}

[[本命令用于手工的激活]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1622_x8463_2134840597}[去激活]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[类型的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口，主要在测试和故障诊断时使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x398653541}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2046150810}[激活]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1846790413}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] activate]{lang="SV"}
:::

::::: {#-517007253 .myid}
[]{#_Toc404784010}[]{#struct_0_x1622_x8463_x1823978935}[]{#_Toc345946873}

**ATM接口 \-- G.SHDSL接口配置命令 \-- display dsl configuration**

------------------------------------------------------------------------

[**[display dsl configuration]{lang="EN-US"}**]{#struct_0_x1622_x8463_x360660549}[命令用来显示]{style="font-family:
宋体"}[ATM]{lang="EN-US"}[接口的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x167108214}

[**[display dsl configuration interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x753173526}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2134775061}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_31703418}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x460803988}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1271365727}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x1640904097}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_102383212}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x957146096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1428474275}

[**[interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_2135758101}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x411521709}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_98262499}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x812499328}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1893204700}[显示]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl configuration interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_2135692565}

[Line parameter and mode configuration:]{lang="EN-US"}

[  Mode:           CPE]{lang="FR"}

[  Standard:       G.991.2]{lang="FR"}

[  Annex:          B]{lang="FR"}

[  ]{lang="FR"}[Wire type:      2]{lang="EN-US"}

[  ]{lang="FR"}[Line rate:      Auto Adaptive]{lang="EN-US"}

[  ]{lang="FR"}[Current margin: 2]{lang="EN-US"}

[  ]{lang="FR"}[SNEXT margin:   0]{lang="EN-US"}

[  ]{lang="FR"}[PSD mode:       Sym PSD]{lang="EN-US"}

[ ]{lang="EN-US"}

[Actual handshake status:]{lang="EN-US"}

[  ]{lang="FR"}[00: 0002 0000 0000 0000 0000 0000 0000 0000 0000 0000]{lang="EN-US"}

[  ]{lang="FR"}[10: 0000 0008 0000 0000 0000 0000 0000 0000 0008 0000]{lang="EN-US"}

[  ]{lang="FR"}[20: 0000 0000 0002 0002 0004 0010]{lang="EN-US"}

[Local handshake status:]{lang="EN-US"}

[  ]{lang="FR"}[00: 0002 0001 0000 0000 0000 0000 0034 003f 003f 003f]{lang="EN-US"}

[  ]{lang="FR"}[10: 003f 003f 0003 0034 003f 003f 003f 003f 003f 0003]{lang="EN-US"}

[  ]{lang="FR"}[20: 0000 0000 0003 0003 000f 0010]{lang="EN-US"}

[Remote handshake status:]{lang="EN-US"}

[  ]{lang="FR"}[00: 0002 0000 0000 0000 0000 0000 0030 003f 003f 003f]{lang="EN-US"}

[  ]{lang="FR"}[10: 003f 000f 0000 0030 003f 003f 003f 003f 000f 0000]{lang="EN-US"}

[  ]{lang="FR"}[20: 0000 0000 0003 0003 0003 0004 0010]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display dsl configuration]{lang="EN-US"}]{#struct_0_x1622_x8463_1151332884}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x807200892}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1925825546}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2115775632}

[[Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_x1693755817}

[[工作模式：]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_2135233814}[为用户端，]{style="font-family:宋体"}[CO]{lang="EN-US"}[为中心局端]{style="font-family:宋体"}

[[Standard]{lang="EN-US"}]{#struct_0_x1622_x8463_x1511228172}

[[所支持的标准规范：（此参数为预设值，用户不能修改）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_869440856}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1622_x8463_1869073655}[：自适应方式（缺省情况标准值）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.3]{lang="EN-US"}]{#struct_0_x1622_x8463_498119072}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.3]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.5]{lang="EN-US"}]{#struct_0_x1622_x8463_375742992}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2+]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.5]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.1]{lang="EN-US"}]{#struct_0_x1622_x8463_2135168278}[：使用]{lang="EN-US" style="font-family:宋体"}[G.DMT]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.1]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.2]{lang="EN-US"}]{#struct_0_x1622_x8463_x1975276278}[：使用]{lang="EN-US" style="font-family:宋体"}[G.Lite]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.2]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T1.413]{lang="EN-US"}]{#struct_0_x1622_x8463_x1610511101}[：使用]{lang="EN-US" style="font-family:宋体"}[T1.413]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G.SHDSL.bis]{lang="EN-US"}]{#struct_0_x1622_x8463_x1197445850}[：协商采用物理层标准是]{style="font-family:宋体"}[G.BIS]{lang="EN-US"}[标准]{style="font-family:宋体"}

[[Annex]{lang="EN-US"}]{#struct_0_x1622_x8463_x1099249851}

[[接口链路所采用的附加标准：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2135102742}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_1557000555}[：]{style="font-family:宋体"}[Annex A]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_x1622_x8463_x1817565931}[：]{style="font-family:宋体"}[Annex B]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[Wire type]{lang="EN-US"}]{#struct_0_x1622_x8463_29472962}

[[连线类型，分为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1622_x8463_508327956}[线制和]{style="font-family:宋体"}[4]{lang="EN-US"}[线制]{style="font-family:宋体"}

[[Current margin]{lang="EN-US"}]{#struct_0_x1622_x8463_2135037206}

[[当前信噪比容限量]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1925272887}

[[SNEXT margin]{lang="EN-US"}]{#struct_0_x1622_x8463_1729287869}

[[最差的信噪比容限量]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x463028344}

[[Line rate]{lang="EN-US"}]{#struct_0_x1622_x8463_587037572}

[[线路速率]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2134971670}

[[PSD mode]{lang="EN-US"}]{#struct_0_x1622_x8463_x1555262801}

[[功率频谱密度方式，分为对称（]{style="font-family:宋体"}[Sym]{lang="EN-US"}]{#struct_0_x1622_x8463_x573926239}[）和非对称方式（]{style="font-family:宋体"}[Asym]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Actual handshake status]{lang="EN-US"}]{#struct_0_x1622_x8463_x716980602}

[[实际的握手状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2134906134}

[[Local handshake status]{lang="EN-US"}]{#struct_0_x1622_x8463_1978080792}

[[本端的握手状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1487522562}

[[Remote handshake status]{lang="EN-US"}]{#struct_0_x1622_x8463_834847475}

[[远端的握手状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1196127604}

[ ]{lang="EN-US"}

::::: {#393417901 .myid}
[]{#_Toc404784011}[]{#struct_0_x1622_x8463_2134840598}[]{#_Toc345946874}

**ATM接口 \-- G.SHDSL接口配置命令 \-- display dsl status**

------------------------------------------------------------------------

[**[display dsl status]{lang="EN-US"}**]{#struct_0_x1622_x8463_x397801573}[命令用来显示]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1284460021}

[**[display dsl status interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x265869128}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x185405043}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x416969739}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1901853890}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2078704412}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_2134775062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_31637882}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x1488544008}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1390853777}

[**[interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x83416975}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1845695050}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_1131865534}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_1478479117}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2135758102}[当接口状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时显示两线]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl status interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_2135692566}

[Operating Mode:]{lang="NO-BOK"}[        ]{lang="ES-AR"}[CPE]{lang="NO-BOK"}

[DSL Mode:]{lang="NO-BOK"}[              ]{lang="ES-AR"}[SHDSL Annex B]{lang="NO-BOK"}

[Configured Wire Type:]{lang="EN-US"}[  ]{lang="ES-AR"}[2]{lang="EN-US"}

[Line A Statistics since last activation:]{lang="EN-US"}

[CRC:            0]{lang="ES-AR"}

[LOSW Defect:    0]{lang="ES-AR"}

[ES:             0]{lang="ES-AR"}

[SES:            0]{lang="ES-AR"}

[UAS:            0]{lang="ES-AR"}

[TX EOC:         0]{lang="ES-AR"}

[RX EOC:         0]{lang="ES-AR"}

[ ]{lang="EN-US"}

[Line A status:]{lang="EN-US"}

[Xcvr Op State:          Data Mode]{lang="EN-US"}

[Last Fail Op State:     0x00]{lang="EN-US"}

[Line Rate(Kbps):        2312]{lang="EN-US"}

[Wire Type:              2]{lang="EN-US"}

[SNR Margin(dB):         16.30]{lang="EN-US"}

[Loop Attenuation(dB):   0.00]{lang="EN-US"}

[RecvGain(dB):           6.07]{lang="EN-US"}

[TxPower(dBm):           9.50]{lang="EN-US"}

[Power Backoff:          enable]{lang="EN-US"}

[Power Backoff Level:    5]{lang="EN-US"}

[Tip/Ring Reversal:      Reversed]{lang="EN-US"}

[FrmOH Stat:             0x00]{lang="EN-US"}

[Rmt Encoder A:          0x0000016e]{lang="EN-US"}

[Rmt Encoder B:          0x00000331]{lang="EN-US"}

[Rmt NSF Cusdata:        0x0000]{lang="EN-US"}

[Rmt NSF CusID:          0x0000]{lang="EN-US"}

[Rmt Country Code:       0x00b5]{lang="EN-US"}

[Rmt Provider Code:      GSPN]{lang="EN-US"}

[Rmt Vendor Data:        0x12 0x34 0x56 0x78]{lang="EN-US"}

[                        0x12 0x34 0x56 0x78]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1151529492}[当接口状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时显示四线]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl status interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_2135168275}

[Operating Mode:         CPE]{lang="NO-BOK"}

[DSL Mode:               SHDSLAnnex B]{lang="NO-BOK"}

[Configured Wire Type:   4]{lang="EN-US"}

[Line A Statistics since last activation:]{lang="EN-US"}

[CRC:             0]{lang="ES-AR"}

[LOSW Defect:     0]{lang="ES-AR"}

[ES:              0]{lang="ES-AR"}

[SES:             0]{lang="ES-AR"}

[UAS:             0]{lang="ES-AR"}

[TX EOC:          0]{lang="ES-AR"}

[RX EOC:          0]{lang="ES-AR"}

[ ]{lang="EN-US"}

[Line A status:]{lang="EN-US"}

[Xcvr Op State:          Data Mode]{lang="EN-US"}

[Last Fail Op State:     0x00]{lang="EN-US"}

[Line Rate(Kbps):        2312]{lang="EN-US"}

[Wire Type:              4]{lang="EN-US"}

[SNR Margin(dB):         13.30]{lang="EN-US"}

[Loop Attenuation(dB):   0.00]{lang="EN-US"}

[RecvGain(dB):           5.86]{lang="EN-US"}

[TxPower(dBm):           9.50]{lang="EN-US"}

[Power Backoff:          enable]{lang="EN-US"}

[Power Backoff Level:    5]{lang="EN-US"}

[Tip/Ring Reversal:      Reversed]{lang="EN-US"}

[FrmOH Stat:             0x00]{lang="EN-US"}

[Rmt Encoder A:          0x0000016e]{lang="EN-US"}

[Rmt Encoder B:          0x00000331]{lang="EN-US"}

[Rmt NSF Cusdata:        0x0000]{lang="EN-US"}

[Rmt NSF CusID:          0x0000]{lang="EN-US"}

[Rmt Country Code:       0x00b5]{lang="EN-US"}

[Rmt Provider Code:      GSPN]{lang="EN-US"}

[Rmt Vendor Data:        0x12 0x34 0x56 0x78]{lang="EN-US"}

[                        0x12 0x34 0x56 0x78]{lang="EN-US"}

[ ]{lang="EN-US"}

[Line B Statistics since last activation:]{lang="EN-US"}

[CRC:            1]{lang="ES-AR"}

[LOSW Defect:    1]{lang="ES-AR"}

[ES:             1]{lang="ES-AR"}

[SES:            1]{lang="ES-AR"}

[UAS:            0]{lang="ES-AR"}

[TX EOC:         0]{lang="ES-AR"}

[RX EOC:         0]{lang="ES-AR"}

[Line B status:]{lang="EN-US"}

[Xcvr Op State:          Data Mode]{lang="EN-US"}

[Last Fail Op State:     0x00]{lang="EN-US"}

[Line Rate(Kbps):        2312]{lang="EN-US"}

[Wire Type:              4]{lang="EN-US"}

[SNR Margin(dB):         12.30]{lang="EN-US"}

[Loop Attenuation(dB):   0.00]{lang="EN-US"}

[RecvGain(dB):           5.28]{lang="EN-US"}

[TxPower(dBm):           9.50]{lang="EN-US"}

[Power Backoff:          enable]{lang="EN-US"}

[Power Backoff Level:    5]{lang="EN-US"}

[Tip/Ring Reversal:      Reversed]{lang="EN-US"}

[FrmOH Stat:             0x00]{lang="EN-US"}

[Rmt Encoder A:          0x0000016e]{lang="EN-US"}

[Rmt Encoder B:          0x00000331]{lang="EN-US"}

[Rmt NSF Cusdata:        0x0000]{lang="EN-US"}

[Rmt NSF CusID:          0x0000]{lang="EN-US"}

[Rmt Country Code:       0x00b5]{lang="EN-US"}

[Rmt Provider Code:      GSPN]{lang="EN-US"}

[Rmt Vendor Data:        0x12 0x34 0x56 0x78]{lang="EN-US"}

[                        0x12 0x34 0x56 0x78]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display dsl status]{lang="EN-US"}]{#struct_0_x1622_x8463_x1974424310}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x810220312}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2135102739}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1556672876}

[[Operating Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_2111519635}

[[工作模式：]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1428412159}[为用户端，]{style="font-family:宋体"}[CO]{lang="EN-US"}[为中心局端]{style="font-family:宋体"}

[[DSL Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_x1078019328}

[[接口链路所采用的附加标准：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1023338310}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHDSL Annex ]{lang="NO-BOK"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_2135037203}[：]{style="font-family:宋体"}[Annex A]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHDSL Annex ]{lang="NO-BOK"}[B]{lang="EN-US"}]{#struct_0_x1622_x8463_x1925600567}[：]{style="font-family:宋体"}[Annex B]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[Configured Wire Type]{lang="EN-US"}]{#struct_0_x1622_x8463_1848172213}

[[配置连线类型，分为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1622_x8463_x762946942}[线制和]{style="font-family:宋体"}[4]{lang="EN-US"}[线制]{style="font-family:宋体"}

[[Line A Statistics since last activation]{lang="EN-US"}]{#struct_0_x1622_x8463_x1768432314}

[[从激活时开始到现在]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_2134971667}[线对的统计信息]{style="font-family:宋体"}

[[CRC]{lang="EN-US"}]{#struct_0_x1622_x8463_x1555721552}

[[CRC]{lang="EN-US"}]{#struct_0_x1622_x8463_x1155526053}[错误数]{style="font-family:宋体"}

[[LOSW Defect]{lang="EN-US"}]{#struct_0_x1622_x8463_922583119}

[[同步丢失错误数]{style="font-family:宋体"}]{#struct_0_x1622_x8463_742639362}

[[ES]{lang="EN-US"}]{#struct_0_x1622_x8463_2134906131}

[[每秒错误数]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1977884184}

[[SES]{lang="EN-US"}]{#struct_0_x1622_x8463_1789068915}

[[每秒严重错误数]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1923755366}

[[UAS]{lang="EN-US"}]{#struct_0_x1622_x8463_1792360171}

[[每秒不可用状态计数]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2134840595}

[[TX EOC]{lang="EN-US"}]{#struct_0_x1622_x8463_x398522469}

[[发送]{style="font-family:宋体"}[EOC]{lang="EN-US"}]{#struct_0_x1622_x8463_x1864549166}[信源计数]{style="font-family:宋体"}

[[RX EOC]{lang="EN-US"}]{#struct_0_x1622_x8463_1553401751}

[[接收]{style="font-family:宋体"}[EOC]{lang="EN-US"}]{#struct_0_x1622_x8463_360230894}[信源计数]{style="font-family:宋体"}

[[Line A status]{lang="EN-US"}]{#struct_0_x1622_x8463_2134775059}

[[A]{lang="EN-US"}]{#struct_0_x1622_x8463_32227703}[线对状态]{style="font-family:宋体"}

[[Xcvr Op State]{lang="EN-US"}]{#struct_0_x1622_x8463_1754145764}

[[收发器工作状态：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2044517872}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x1622_x8463_2135758099}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Data Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_1927654730}[：]{style="font-family:宋体"}[激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HandShaking]{lang="EN-US"}]{#struct_0_x1622_x8463_x475569873}[：]{style="font-family:宋体"}[激活握手阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Training]{lang="EN-US"}]{#struct_0_x1622_x8463_630515952}[：]{style="font-family:宋体"}[激活训练阶段]{lang="EN-US" style="font-family:宋体"}

[[Last Fail Op State]{lang="EN-US"}]{#struct_0_x1622_x8463_2135692563}

[[上次协商失败收发器工作状态，可能的取值同上]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1151201812}

[[Line Rate(Kbps)]{lang="EN-US"}]{#struct_0_x1622_x8463_804696247}

[[协商线对速率]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x720997035}

[[Wire Type]{lang="EN-US"}]{#struct_0_x1622_x8463_2135233812}

[[线数类型，可能的取值有]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1622_x8463_x1511621388}[（]{style="font-family:宋体"}[2]{lang="EN-US"}[线制）、]{style="font-family:宋体"}[4]{lang="EN-US"}[（]{style="font-family:宋体"}[4]{lang="EN-US"}[线制）]{style="font-family:宋体"}

[[SNR Margin(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_x1595928760}

[[信噪比容限量]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2135168276}

[[Loop Attenuation(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_x1974358774}

[[环路衰减]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1804154189}

[[RecvGain(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_916956276}

[[接收增益]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2135102740}

[[TxPower(dBm)]{lang="EN-US"}]{#struct_0_x1622_x8463_1557131627}

[[发送功率]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1702539352}

[[Power Backoff]{lang="EN-US"}]{#struct_0_x1622_x8463_2135037204}

[[功率补偿状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1925141815}

[[Power Backoff Level]{lang="EN-US"}]{#struct_0_x1622_x8463_1241250130}

[[功率补偿级别]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2134971668}

[[Tip/Ring Reversal]{lang="EN-US"}]{#struct_0_x1622_x8463_x1554738512}

[[Tip/Ring]{lang="EN-US"}]{#struct_0_x1622_x8463_x1521995459}[翻转状态]{style="font-family:宋体"}

[[FrmOH Stat]{lang="EN-US"}]{#struct_0_x1622_x8463_1230618509}

[[帧溢出状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2134906132}

[[Rmt Encoder A]{lang="EN-US"}]{#struct_0_x1622_x8463_1977687576}

[[远端译码器系数]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_x541819963}

[[Rmt Encoder B]{lang="EN-US"}]{#struct_0_x1622_x8463_2134840596}

[[远端译码器系数]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_x1622_x8463_x398719077}

[[Rmt NSF Cusdata]{lang="EN-US"}]{#struct_0_x1622_x8463_1269697748}

[[远端非标准格式用户数据]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2134775060}

[[Rmt NSF CusID]{lang="EN-US"}]{#struct_0_x1622_x8463_31768954}

[[远端非标准格式用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1622_x8463_666862289}

[[Rmt Country Code]{lang="EN-US"}]{#struct_0_x1622_x8463_2135758100}

[[远端国家代码]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x411456173}

[[Rmt Provider Code]{lang="EN-US"}]{#struct_0_x1622_x8463_87997400}

[[远端芯片供应商代码]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2135692564}

[[Rmt Vendor Data]{lang="EN-US"}]{#struct_0_x1622_x8463_1151398420}

[[远端制造商代码]{style="font-family:宋体"}]{#struct_0_x1622_x8463_335989262}

[ ]{lang="EN-US"}

::::: {#-688133518 .myid}
[]{#_Toc404784012}[]{#struct_0_x1622_x8463_219276506}[]{#_Toc345946875}

**ATM接口 \-- G.SHDSL接口配置命令 \-- display dsl version**

------------------------------------------------------------------------

[**[display dsl version]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1334990364}[命令用来显示]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的版本信息和支持的能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1164623338}

[**[display dsl version interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x892817236}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1396532411}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2069917770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x7702984}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1630699800}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x1468417876}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_219342042}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_625626290}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_493493780}

[**[interface atm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_176660734}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的版本信息和支持的能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x881884222}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_1718360028}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_1502152005}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1933231468}[显示]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[上的版本信息和支持的能力。]{style="font-family:宋体"}

[[\<Sysname\> display dsl version interface atm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_219407578}

[DSL Line Type:          G.SHDSL]{lang="EN-US"}

[ATM SAR Device:         0x823614f1]{lang="EN-US"}

[ATM SAR Revision:       0x02]{lang="EN-US"}

[Chipset Vendor:         GSPN]{lang="EN-US"}

[Firmware Rel-Rev:       R2.3.1-0]{lang="EN-US"}

[DSP Version:            1]{lang="EN-US"}

[PCB Version:            0.0]{lang="EN-US"}

[CPLD Version:           0.0]{lang="EN-US"}

[Driver Version:         2.0]{lang="EN-US"}

[Hardware Version:       1.0]{lang="EN-US"}

[ITU G991.2 ANNEX A:     Supported]{lang="EN-US"}

[ITU G991.2 ANNEX B:     Supported]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display dsl version]{lang="EN-US"}]{#struct_0_x1622_x8463_1651616245}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1059936976}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1736337704}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_225097580}

[[DSL Line Type]{lang="EN-US"}]{#struct_0_x1622_x8463_219473114}

[[用户接入线的类型]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1047668874}

[[ATM SAR Device]{lang="EN-US"}]{#struct_0_x1622_x8463_x1428038584}

[[SAR]{lang="EN-US"}]{#struct_0_x1622_x8463_504475055}[芯片的标识]{style="font-family:宋体"}

[[ATM SAR Revision]{lang="EN-US"}]{#struct_0_x1622_x8463_x1775815818}

[[SAR]{lang="EN-US"}]{#struct_0_x1622_x8463_83476929}[芯片的修改标识]{style="font-family:宋体"}

[[Chipset Vendor]{lang="EN-US"}]{#struct_0_x1622_x8463_219538650}

[[DSL Chipsets]{lang="EN-US"}]{#struct_0_x1622_x8463_x304073537}[的厂商标识]{style="font-family:宋体"}

[[Firmware Rel-Rev]{lang="EN-US"}]{#struct_0_x1622_x8463_10320868}

[[FirmWare]{lang="EN-US"}]{#struct_0_x1622_x8463_1943804968}[的标识和版本信息]{style="font-family:宋体"}

[[DSP Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x1670746008}

[[DSP]{lang="EN-US"}]{#struct_0_x1622_x8463_219604186}[版本]{style="font-family:宋体"}

[[PCB Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x363735145}

[[单板]{style="font-family:宋体"}[PCB]{lang="EN-US"}]{#struct_0_x1622_x8463_2011654250}[的版本号]{style="font-family:宋体"}

[[CPLD Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x55194793}

[[逻辑器件的版本号]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1007238479}

[[Driver Version]{lang="EN-US"}]{#struct_0_x1622_x8463_219669722}

[[驱动软件的版本号]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1595031289}

[[Hardware Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x1614740603}

[[硬件版本]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1663995094}

[[ITU G991.2 ANNEX A]{lang="EN-US"}]{#struct_0_x1622_x8463_x26830414}[，]{style="font-family:宋体"}[ITU G991.2 ANNEX B]{lang="EN-US"}

[[支持的标准及其附加标准]{style="font-family:宋体"}]{#struct_0_x1622_x8463_219735258}

[ ]{lang="EN-US"}

::: {#-880684077 .myid}
[]{#_Toc404784013}[]{#struct_0_x1622_x8463_410215003}[]{#_Toc345946876}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl annex**

------------------------------------------------------------------------

[**[shdsl annex]{lang="EN-US"}**]{#struct_0_x1622_x8463_x501412217}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口所支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}[标准。]{style="font-family:宋体"}

[**[undo shdsl annex]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1043724244}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2120916822}

[**[shdsl annex]{lang="EN-US"}**[ { **a** \| **b** }]{lang="EN-US"}]{#struct_0_x1622_x8463_121089597}

[**[undo shdsl annex]{lang="EN-US"}**]{#struct_0_x1622_x8463_1003512307}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_218752218}

[[支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}]{#struct_0_x1622_x8463_x113933866}[标准为]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_472544555}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1328692846}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1616533867}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_10331822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1905454741}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2105805362}

[**[a]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1010909736}[：支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}[标准为]{style="font-family:宋体"}[Annex a]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[b]{lang="EN-US"}**]{#struct_0_x1622_x8463_218817754}[：支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}[标准为]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_66504797}

[[如果]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x1402125144}[设备和]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备选用的]{style="font-family:宋体"}[Annex]{lang="EN-US"}[标准不一样，线路会难以激活，两设备之间将无法建立连接。]{style="font-family:宋体"}

[[Annex a/b]{lang="EN-US"}]{#struct_0_x1622_x8463_812701946}[均是]{style="font-family:宋体"}[G.991.2]{lang="EN-US"}[的标准，]{style="font-family:宋体"}[Annex a]{lang="EN-US"}[主要在北美应用，]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[主要在欧洲应用，其它地区网络要根据当地网络的不同，选择不同的标准，例如中国地区网络执行的标准类型为]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1430034722}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2132787987}[配置]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[所支持的标准为]{style="font-family:宋体"}[Annex ]{lang="EN-US"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1729669794}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl annex a]{lang="EN-US"}
:::

::: {#1394850264 .myid}
[]{#_Toc404784014}[]{#struct_0_x1622_x8463_219276507}[]{#_Toc345946877}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl capability**

------------------------------------------------------------------------

[**[shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1334990365}[命令用来配置接口的协商能力。]{style="font-family:宋体"}

[**[undo shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_401460603}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1841243615}

[**[shdsl capability]{lang="EN-US"}**[ { **auto** \| **g-shdsl** \| **g-shdsl-bis** }]{lang="EN-US"}]{#struct_0_x1622_x8463_522782479}

[**[undo shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_x898281729}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x605900570}

[[在]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1228082749}[模式下，采用]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[方式。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_219342043}[模式下，采用]{style="font-family:宋体"}**[g-shdsl-bis]{lang="EN-US"}**[方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_625626291}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_493493781}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_176660733}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x881884219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1717901273}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1403154585}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1924240223}[：自动选择与对端接口相同的协商能力（只在]{style="font-family:宋体"}[CPE]{lang="EN-US"}[模式下支持，在]{style="font-family:宋体"}[CO]{lang="EN-US"}[模式下不支持）。]{style="font-family:宋体"}

[**[g-shdsl]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2102379063}[：使用]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g-shdsl-bis]{lang="EN-US"}**]{#struct_0_x1622_x8463_219407579}[：使用]{style="font-family:宋体"}[G.SHDSL.bis]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1651616246}

[[在]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_1736141096}[模式下支持]{style="font-family:宋体"}[g-shdsl]{lang="EN-US"}[和]{style="font-family:宋体"}[g-shdsl-bis]{lang="EN-US"}[以及]{style="font-family:宋体"}[auto]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x2095603625}[模式下支持]{style="font-family:宋体"}[g-shdsl]{lang="EN-US"}[和]{style="font-family:宋体"}[g-shdsl-bis]{lang="EN-US"}[，不支持]{style="font-family:宋体"}[auto]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在配置]{style="font-family:宋体"}**[shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2107091089}[时，会自动恢复为各自模式下的缺省配置。]{style="font-family:宋体"}

[[两端接口需要使用相同的协商能力，才能协商成功。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1590694789}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_241024813}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1121542855}[配置接口的协商能力为]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_219473115}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl capability g-shdsl]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1047668875}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[shdsl mode]{lang="SV"}**]{#struct_0_x1622_x8463_138045357}
:::

::: {#1117133388 .myid}
[]{#_Toc404784015}[]{#struct_0_x1622_x8463_504693328}[]{#_Toc345946878}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl line-probing**

------------------------------------------------------------------------

[**[shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_1636351272}[命令用来开启]{style="font-family:
宋体"}[SHDSL]{lang="EN-US"}[线路的探询功能。]{style="font-family:宋体"}

[**[undo shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1488740189}[命令用来关闭]{style="font-family:
宋体"}[SHDSL]{lang="EN-US"}[线路的探询功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x355480365}

[**[shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_x812387697}

[**[undo shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_219538651}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x304073538}

[[SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_9468900}[线路的探询功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_834159872}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_1228997108}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_21872158}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1181134425}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x152876611}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_665335658}

[[开启探询功能后，在线路激活的过程中，系统将执行线路探询功能去协商最佳的线路速率；若关闭探询功能，系统会选择]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_219604187}[和]{style="font-family:宋体"}[CO]{lang="EN-US"}[都支持的速率交集中的最大速率。这种方式因为跳过了线路速率的适配过程，减短了激活]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路的时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x363735144}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_2011719786}[关闭]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路的探询功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_741681338}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] undo shdsl line-probing enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_104697550}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[activate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1109072674}
:::

::: {#577373275 .myid}
[]{#_Toc404784016}[]{#struct_0_x1622_x8463_351142876}[]{#_Toc345946879}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl mode**

------------------------------------------------------------------------

[**[shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_219669723}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的工作模式。]{style="font-family:宋体"}

[**[undo shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1595031288}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1114142752}

[**[shdsl mode ]{lang="EN-US"}**[{ **co** \| **cpe** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1661264939}

[**[undo shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1700117957}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x392075837}

[[工作模式为]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_1293648659}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x55266418}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x10739610}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219735259}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_410215002}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x501412216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1043658708}

[**[co]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1327740920}[：设置为]{style="font-family:宋体"}[CO]{lang="EN-US"}[（]{style="font-family:宋体"}[Central Office]{lang="EN-US"}[，中心局）模式。]{style="font-family:宋体"}

[**[cpe]{lang="EN-US"}**]{#struct_0_x1622_x8463_x226060764}[：设置为]{style="font-family:宋体"}[CPE]{lang="EN-US"}[（]{style="font-family:宋体"}[Customer Premises Equipment]{lang="EN-US"}[，用户侧设备）模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x981073806}

[[两台设备直连时，必须把一端配置为]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x1180381333}[模式，另一端配置成]{style="font-family:宋体"}[CPE]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x996970104}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_218752219}[配置]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[CO]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x113933867}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl mode co]{lang="SV"}
:::

::: {#1675429643 .myid}
[]{#_Toc404784017}[]{#struct_0_x1622_x8463_472479019}[]{#_Toc345946880}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl pam**

------------------------------------------------------------------------

[**[shdsl pam]{lang="EN-US"}**]{#struct_0_x1622_x8463_1420435258}[用来配置]{style="font-family:宋体"}[PAM]{lang="EN-US"}[（]{style="font-family:宋体"}[Pulse Amplitude Modulation]{lang="EN-US"}[，脉冲调制）]{style="font-family:宋体"} [Constellation]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo shdsl pam]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1098132090}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1440005596}

[**[shdsl pam]{lang="SV"}[ ]{lang="SV"}**[{ ]{lang="EN-US"}]{#struct_0_x1622_x8463_581297660}**[16]{lang="SV"}**[ ]{lang="SV"}[\| ]{lang="EN-US"}**[32]{lang="SV"}[ ]{lang="SV"}**[\| ]{lang="EN-US"}**[auto]{lang="SV"}**[ ]{lang="SV"}[}]{lang="EN-US"}

[**[undo shdsl pam]{lang="SV"}**]{#struct_0_x1622_x8463_x2000430000}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_218817755}

[[自动选择]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_x1622_x8463_66504796}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_554189992}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1626846498}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1310606863}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_39644691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x834268268}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1469679299}

[**[16]{lang="EN-US"}**]{#struct_0_x1622_x8463_219276504}[：使用]{style="font-family:宋体"}[16 PAM Constellation]{lang="EN-US"}[。在]{style="font-family:宋体"}[16 PAM]{lang="EN-US"}[下，速率范围为]{style="font-family:宋体"}[192]{lang="EN-US"}[～]{style="font-family:宋体"}[3840]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1334990366}[：使用]{style="font-family:宋体"}[32 PAM Constellation]{lang="EN-US"}[。在]{style="font-family:宋体"}[32 PAM]{lang="EN-US"}[下，速率范围为]{style="font-family:宋体"}[768]{lang="EN-US"}[～]{style="font-family:宋体"}[5696]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_1967544544}[：根据线路两端的参数自动选择两端都支持的最好的]{style="font-family:宋体"}[PAM]{lang="EN-US"}[（]{style="font-family:宋体"}[32 PAM]{lang="EN-US"}[比]{style="font-family:宋体"}[16 PAM]{lang="EN-US"}[好）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x303946351}

[[PAM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1395664134}[是数字线路的一种编码模式，叫脉冲调制模式，]{style="font-family:宋体"}[Constellation]{lang="EN-US"}[用来形容]{style="font-family:宋体"}[PAM]{lang="EN-US"}[编码模式像星座。本命令用于配置]{style="font-family:宋体"}[PHY]{lang="EN-US"}[芯片的数字信号调制模式。]{style="font-family:宋体"}

[[当接口的协商能力为]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_861131620}[时，不支持]{style="font-family:宋体"}[32 PAM Constellation]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1636497340}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1483061719}[配置]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[使用]{style="font-family:宋体"}[16 PAM Constellation]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_219342040}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl pam 16]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_625626288}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1845158372}
:::

::: {#-663222519 .myid}
[]{#_Toc404784018}[]{#struct_0_x1622_x8463_1994039724}[]{#_Toc345946881}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl pbo**

------------------------------------------------------------------------

[**[shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_x518504644}[命令用来调整发送功率。]{style="font-family:宋体"}

[**[undo shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_x1451973395}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x165550104}

[**[shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_1658396965}[ { *value* \| **auto**]{lang="SV"}[ ]{lang="SV"}[}]{lang="EN-US"}

[**[undo shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_1529244051}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219407576}

[[自动调整发送功率。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1651616259}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1737124137}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_1052131984}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1464029105}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x681154646}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_19601102}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2126529552}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_219473112}[：自动调整发送功率。]{style="font-family:宋体"}

[*[value]{lang="SV"}*]{#struct_0_x1622_x8463_x1047668876}[：发送功率调整值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1704129298}

[[正常情况下，接口会根据线路噪声情况，自动调整发送功率，以保证可以获得合适的信噪比。当线路的噪声已知的情况下，或者自动调整不准确的时候，可以通过此命令行手动调整发射功率。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2051095860}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1330327153}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_470569050}[设置]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[接口的发送功率调整值为]{style="font-family:宋体"}[20db]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1425862740}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl pbo 20]{lang="SV"}
:::

::: {#56821508 .myid}
[]{#_Toc404784019}[]{#struct_0_x1622_x8463_x1025602559}[]{#_Toc345946882}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl psd**

------------------------------------------------------------------------

[**[shdsl psd]{lang="EN-US"}**]{#struct_0_x1622_x8463_219538648}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的功率频谱密度模式。]{style="font-family:宋体"}

[**[undo shdsl psd]{lang="EN-US"}**]{#struct_0_x1622_x8463_2034578631}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1735372178}

[**[shdsl psd]{lang="EN-US"}**[ { **asymmetry** \| **symmetry** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x35848588}

[**[undo shdsl psd]{lang="EN-US"}**]{#struct_0_x1622_x8463_1992141706}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1208294413}

[[功率频谱密度模式为对称模式。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x816650547}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_863818467}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x2043650979}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219604184}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x363735147}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_2011785322}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x834513320}

[**[asymmetry]{lang="EN-US"}**]{#struct_0_x1622_x8463_1903777549}[：功率频谱密度模式为非对称模式。]{style="font-family:宋体"}

[**[symmetry]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1186037410}[：功率频谱密度模式为对称模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1649756605}

[[PSD]{lang="EN-US"}]{#struct_0_x1622_x8463_x867578526}[（]{style="font-family:宋体"}[Power Spectral Density]{lang="EN-US"}[，功率频谱密度）指发射功率在最高准位时，一脉冲或一序列脉冲，其单位带宽的总输出能量除以总脉冲持续时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219669720}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1595031287}[配置]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的功率频谱密度模式为非对称模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x1164401909}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl psd asymmetry]{lang="SV"}
:::

::: {#514530750 .myid}
[]{#_Toc404784020}[]{#struct_0_x1622_x8463_654199821}[]{#_Toc345946883}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl rate**

------------------------------------------------------------------------

[**[shdsl rate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x105395248}[命令用来配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口单线对的速率。]{style="font-family:宋体"}

[**[undo shdsl rate]{lang="EN-US"}**]{#struct_0_x1622_x8463_1683044364}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2049095197}

[**[shdsl rate]{lang="EN-US"}**[ { *rate* \| **auto** }]{lang="EN-US"}]{#struct_0_x1622_x8463_329500293}

[**[undo shdsl rate]{lang="EN-US"}**]{#struct_0_x1622_x8463_219735256}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_410214993}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x899799046}[、]{style="font-family:宋体"}[ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[ATM SHDSL 8WIRE_BIS]{lang="EN-US"}[接口的单线对速率为自动协商方式。]{style="font-family:宋体"}

[[ATM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1362948911}[接口，在两线模式下单线对速率为自动协商方式，在非两线模式下的单线对速率为]{style="font-family:宋体"}[2312kbit/s]{lang="EN-US"}[（即四线接口速率为]{style="font-family:宋体"}[4624kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1325765965}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_974181812}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1343162175}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_387340932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x49212524}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_218752216}

[*[rate]{lang="EN-US"}*]{#struct_0_x1622_x8463_x113933856}[：]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的单线对速率最大值。对于]{style="font-family:宋体"}[ATM G.SHDSL]{lang="EN-US"}[接口和]{style="font-family:宋体"}[ATM SHDSL_4WIRE]{lang="EN-US"}[接口，取值范围为]{style="font-family:宋体"}[192]{lang="EN-US"}[～]{style="font-family:宋体"}[2312]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[；]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[ATM SDHSL_4WIRE_BIS]{lang="EN-US"}[接口和]{style="font-family:宋体"}[ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口，取值范围为]{style="font-family:宋体"}[192]{lang="EN-US"}[～]{style="font-family:宋体"}[5696]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_472544558}[：为自动协商方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1328692857}

[[在实际使用中，最大下行速率还会受局端设备的限制和线路条件的限制，有可能达不到设置的值。如果将速率设置成自动协商方式，在激活过程中两端会根据当前的线路状况协商出一个合适的速率；如果]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1112283952}[端和]{style="font-family:宋体"}[CO]{lang="EN-US"}[端设置成固定速率，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[端和]{style="font-family:宋体"}[CO]{lang="EN-US"}[端将进行速率协商，若无法满足二者之中较低的速率要求的时候，线路无法被激活。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1675623717}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[四线（即双线对）的]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1950963360}[ATM]{lang="EN-US"}[接口的速率为单线对速率的两倍。例如设置单线对速率为]{style="font-family:宋体"}[2312kbit/s]{lang="EN-US"}[，则四线接口的速率为]{style="font-family:宋体"}[4624kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[四线的]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x469625308}[ATM]{lang="EN-US"}[接口的单线对速率无法配置成]{style="font-family:宋体"}[auto]{lang="EN-US"}[方式，因为四线的接口无法进行速率的协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x693081971}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_218817752}[配置]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的单线对速率为自动协商方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_66504799}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl rate auto]{lang="SV"}
:::

::: {#-391430866 .myid}
[]{#_Toc404784021}[]{#struct_0_x1622_x8463_x1784462168}[]{#_Toc345946884}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl snr-margin**

------------------------------------------------------------------------

[**[shdsl snr-margin]{lang="EN-US"}**]{#struct_0_x1622_x8463_564748841}[命令用来配置接口链路的信噪比容限量。]{style="font-family:宋体"}

[**[undo shdsl snr-margin]{lang="EN-US"}**]{#struct_0_x1622_x8463_x379856850}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1825456480}

[**[shdsl snr-margin]{lang="EN-US"}**[ \[ **current** *current-margin-value* \] \[ **snext** *snext-margin-value* \]]{lang="EN-US"}]{#struct_0_x1622_x8463_2104593127}

[**[undo shdsl snr-margin]{lang="EN-US"}**]{#struct_0_x1622_x8463_219276505}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1334990367}

[[线路协商时]{style="font-family:宋体"}[current-margin-value]{lang="EN-US"}]{#struct_0_x1622_x8463_x761338811}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:
宋体"}[snext-margin-value]{lang="EN-US"}[为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1152220201}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_638592339}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1716853264}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1866809301}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_704979591}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_651021243}

[**[current]{lang="EN-US"}***[ current-margin-value]{lang="EN-US"}*]{#struct_0_x1622_x8463_219342041}[：当前信噪比容限量。]{style="font-family:宋体"}*[current-margin-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路在训练的时候以线路信噪比门限加上]{style="font-family:宋体"}*[current-margin-value]{lang="EN-US"}*[进行训练。配置比较大的]{style="font-family:宋体"}*[current-margin-value]{lang="EN-US"}*[可以使得协商成功的链路更加稳定，抗噪能力更强。]{style="font-family:宋体"}

[**[snext ]{lang="EN-US"}***[snext-margin-value]{lang="EN-US"}*]{#struct_0_x1622_x8463_625626289}[：最差的信噪比容限量。]{style="font-family:宋体"}*[snext-margin-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路在训练的时候以最差信噪比门限加上]{style="font-family:宋体"}*[snext-margin-value]{lang="EN-US"}*[进行训练。设置比较大的]{style="font-family:宋体"}*[snext-margin-value]{lang="EN-US"}*[可以使得协商成功的链路更加稳定，抗噪能力更强。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1845158371}

[[配置信噪比容限量会影响线路支持的最大速率。因此在线路比较好的情况下，可以配置较小的信噪比容限量，以获得更高的速率。但是，在线路存在较多的噪声的情况下，配置过小的当前信噪比容限量会造成线路容易掉线。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1590755197}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_460502563}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x2041358866}[配置接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[的当前信噪比容限量为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_264820197}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl snr-margin current 5]{lang="EN-US"}
:::

::: {#-611532825 .myid}
[]{#_Toc404784022}[]{#struct_0_x1622_x8463_x2133087318}[]{#_Toc345946885}

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl wire**

------------------------------------------------------------------------

[**[shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_219407577}[命令用来配置四线和八线]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[接口的连线模式。]{style="font-family:宋体"}

[**[undo shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_1651616260}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1736534310}

[[在]{style="font-family:宋体"}[ATM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_1026245130}[、]{style="font-family:宋体"}[ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图下：]{style="font-family:宋体"}

[**[shdsl wire]{lang="EN-US"}**[ { **2** \| **4-auto-enhanced** \| **4-enhanced** \| **4-standard** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1586112946}

[**[undo shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_x305094838}

[[在]{style="font-family:宋体"}[ATM SHDSL_8WIRE_BIS]{lang="EN-US"}]{#struct_0_x1622_x8463_1195754219}[接口视图下：]{style="font-family:宋体"}

[**[shdsl wire]{lang="EN-US"}**[ { **2** \| **4-enhanced** \| **4-standard** \| **6** \| **8** \| **auto** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1474024775}

[**[undo shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_x980195408}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219473113}

[[ATM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1047668877}[接口的连线模式为]{style="font-family:宋体"}**[4-enhanced]{lang="EN-US"}**[（四线增强模式）。]{style="font-family:宋体"}

[[ATM SHDSL 4WIRE_BIS]{lang="EN-US"}]{#struct_0_x1622_x8463_x1024754057}[接口的连线模式为]{style="font-family:宋体"}**[4-standard]{lang="EN-US"}**[（四线标准模式）。]{style="font-family:宋体"}

[[ATM SHDSL_8WIRE_BIS]{lang="EN-US"}]{#struct_0_x1622_x8463_2131118859}[接口的连线模式为]{style="font-family:宋体"}**[8]{lang="EN-US"}**[（八线模式）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x129651444}

[[ATM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1198164423}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ATM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1351477899}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x610774474}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_219538649}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2034578630}

[**[2]{lang="EN-US"}**]{#struct_0_x1622_x8463_1735306642}[：两线模式。]{style="font-family:宋体"}

[**[4-auto-enhanced]{lang="EN-US"}**]{#struct_0_x1622_x8463_1142107147}[：四线自动模式，系统首先以]{style="font-family:宋体"}**[4-enhanced]{lang="EN-US"}**[模式进行协商，如果检测到对端是]{style="font-family:宋体"}**[4-standard]{lang="EN-US"}**[模式，则本端自动切换成]{style="font-family:宋体"}**[4-standard]{lang="EN-US"}**[模式进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[4-enhanced]{lang="EN-US"}**]{#struct_0_x1622_x8463_527236276}[：四线增强模式，四线中的一个线对先与对端协商，协商成功后，另一个线对再与对端进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[4-standard]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1146745502}[：四线标准模式，四线的两个线对必须同时开始进行协商，要求对端也为四线标准模式。]{style="font-family:宋体"}

[**[6]{lang="EN-US"}**]{#struct_0_x1622_x8463_2081087017}[：六线模式。]{style="font-family:宋体"}

[**[8]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1922709309}[：八线模式。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_1615852788}[：自动模式，本端根据对端接口连线模式进行协商，最终协商的连线模式与对端配置一致。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219604185}

[[配置]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x363735146}**[shdsl wire]{lang="EN-US"}**[命令时，需要根据对端接口的设置选择正确连线模式。在无法确定对端接口连线模式的情况下，本端接口可以配置为]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[自动模式与对端进行协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2011850858}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1963937}[设置]{style="font-family:宋体"}[SHDSL_4WIRE ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[工作在四线自动模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x48139195}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] shdsl wire 4-auto-enhanced]{lang="EN-US"}
:::

::::: {#-97892784 .myid}
[]{#_Toc404784024}[]{#struct_0_x1622_x8463_70471970}[]{#_Toc345946887}

**ATM接口 \-- EFM接口配置命令 \-- display dsl configuration**

------------------------------------------------------------------------

[**[display dsl configuration]{lang="EN-US"}**]{#struct_0_x1622_x8463_x685183923}[命令用来显示]{style="font-family:
宋体"}[EFM]{lang="EN-US"}[接口的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_574672845}

[**[display dsl configuration interface efm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_168679507}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219735257}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_410214992}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x899799045}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1363014447}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x1769309916}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_761356067}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_1774250772}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1777912501}

[**[interface efm]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_218752217}*[interface-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x113933857}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_472479022}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x1300553921}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x80920779}[显示]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl configuration interface efm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_218817753}

[Line parameter and mode configuration:]{lang="EN-US"}

[  Mode:           CPE]{lang="FR"}

[  Standard:       G.991.2]{lang="FR"}

[  Annex:          B]{lang="FR"}

[  ]{lang="FR"}[Wire type:      2]{lang="EN-US"}

[  ]{lang="FR"}[Line rate:      Auto Adaptive]{lang="EN-US"}

[  ]{lang="FR"}[Current margin: 2]{lang="EN-US"}

[  ]{lang="FR"}[SNEXT margin:   0]{lang="EN-US"}

[  ]{lang="FR"}[Psd mode:       Sym PSD]{lang="EN-US"}

[ ]{lang="EN-US"}

[Actual handshake status:]{lang="EN-US"}

[  00: 0002 0000 0000 0000 0000 0000 0000 0000 0000 0000]{lang="FR"}

[  10: 0000 0008 0000 0000 0000 0000 0000 0000 0008 0000]{lang="FR"}

[  20: 0000 0000 0002 0002 0004 0010]{lang="FR"}

[Local handshake status:]{lang="EN-US"}

[  00: 0002 0001 0000 0000 0000 0000 0034 003f 003f 003f]{lang="FR"}

[  10: 003f 003f 0003 0034 003f 003f 003f 003f 003f 0003]{lang="FR"}

[  20: 0000 0000 0003 0003 000f 0010]{lang="FR"}

[Remote handshake status:]{lang="EN-US"}

[  00: 0002 0000 0000 0000 0000 0000 0030 003f 003f 003f]{lang="FR"}

[  10: 003f 000f 0000 0030 003f 003f 003f 003f 000f 0000]{lang="FR"}

[  20: 0000 0000 0003 0003 0004 0010]{lang="FR"}

[[表1-10 ]{lang="EN-US"}[display dsl configuration]{lang="EN-US"}]{#struct_0_x1622_x8463_66504798}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1058138044}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_171852968}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2005191482}

[[Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_219276502}

[[工作模式：]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1334990368}[为用户端，]{style="font-family:宋体"}[CO]{lang="EN-US"}[为中心局端]{style="font-family:宋体"}

[[Standard]{lang="EN-US"}]{#struct_0_x1622_x8463_804745130}

[[所支持的标准规范：（此参数为预设值，用户不能修改）]{style="font-family:宋体"}]{#struct_0_x1622_x8463_475517334}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1622_x8463_x695881257}[：自适应方式（缺省情况标准值）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.3]{lang="EN-US"}]{#struct_0_x1622_x8463_1833742858}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.3]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.5]{lang="EN-US"}]{#struct_0_x1622_x8463_219342038}[：使用]{lang="EN-US" style="font-family:宋体"}[ADSL2+]{lang="EN-US"}[（]{style="font-family:宋体"}[G992.5]{lang="EN-US"}[）]{style="font-family:宋体"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.1]{lang="EN-US"}]{#struct_0_x1622_x8463_1434930344}[：使用]{lang="EN-US" style="font-family:宋体"}[G.DMT]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.1]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G992.2]{lang="EN-US"}]{#struct_0_x1622_x8463_x1618996232}[：使用]{lang="EN-US" style="font-family:宋体"}[G.Lite]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[G992.2]{lang="EN-US"}[）标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T1.413]{lang="EN-US"}]{#struct_0_x1622_x8463_x1508924588}[：使用]{lang="EN-US" style="font-family:宋体"}[T1.413]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G.SHDSL.bis]{lang="EN-US"}]{#struct_0_x1622_x8463_x1314975669}[：协商采用物理层标准是]{style="font-family:宋体"}[G.BIS]{lang="EN-US"}[标准]{style="font-family:宋体"}

[[Annex]{lang="EN-US"}]{#struct_0_x1622_x8463_622589174}

[[接口链路所采用的附加标准：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_219407574}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_1651616257}[：]{style="font-family:宋体"}[Annex A]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_x1622_x8463_1736206633}[：]{style="font-family:宋体"}[Annex B]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[Wire type]{lang="EN-US"}]{#struct_0_x1622_x8463_625945637}

[[连线类型，分为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1622_x8463_1077169005}[线制和]{style="font-family:宋体"}[4]{lang="EN-US"}[线制]{style="font-family:宋体"}

[[Current margin]{lang="EN-US"}]{#struct_0_x1622_x8463_219473110}

[[当前容限量]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1047668878}

[[SNEXT margin]{lang="EN-US"}]{#struct_0_x1622_x8463_1253790604}

[[最差情况的容限量]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1466180784}

[[Line rate]{lang="EN-US"}]{#struct_0_x1622_x8463_219538646}

[[线路速率]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2034578621}

[[PSD mode]{lang="EN-US"}]{#struct_0_x1622_x8463_1735372179}

[[功率频谱密度方式，分为对称（]{style="font-family:宋体"}[Sym]{lang="EN-US"}]{#struct_0_x1622_x8463_x35914124}[）和非对称方式（]{style="font-family:宋体"}[Asym]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Actual handshake status]{lang="EN-US"}]{#struct_0_x1622_x8463_x314278553}

[[实际的握手状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_219604182}

[[Local handshake status]{lang="EN-US"}]{#struct_0_x1622_x8463_x363735149}

[[本端的握手状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2012440682}

[[Remote handshake status]{lang="EN-US"}]{#struct_0_x1622_x8463_635173152}

[[远端的握手状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_219669718}

[ ]{lang="EN-US"}

::::: {#-1078575944 .myid}
[]{#_Toc404784025}[]{#struct_0_x1622_x8463_361283841}[]{#_Toc345946888}

**ATM接口 \-- EFM接口配置命令 \-- display dsl status**

------------------------------------------------------------------------

[**[display dsl status]{lang="EN-US"}**]{#struct_0_x1622_x8463_192978963}[命令用来显示]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_71585013}

[**[display dsl status interface efm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_413900784}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_86352451}

[[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1717584094}[任意视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1241825583}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1130226949}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_219735254}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_410214991}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x899799048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1363342127}

[**[interface efm]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1154372510}*[interface-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1168853639}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x1765625706}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_839490595}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_218752214}[当接口状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时显示两线]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl status interface efm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_218817750}

[Operating Mode:]{lang="NO-BOK"}[        ]{lang="ES-AR"}[CPE]{lang="NO-BOK"}

[DSL Mode:]{lang="NO-BOK"}[              ]{lang="ES-AR"}[SHDSL Annex B]{lang="NO-BOK"}

[Configured Wire Type:]{lang="EN-US"}[  ]{lang="ES-AR"}[2]{lang="EN-US"}

[Line A Statistics since last activation:]{lang="EN-US"}

[CRC:            0]{lang="ES-AR"}

[LOSW Defect:    0]{lang="ES-AR"}

[ES:             0]{lang="ES-AR"}

[SES:            0]{lang="ES-AR"}

[UAS:            0]{lang="ES-AR"}

[TX EOC:         0]{lang="ES-AR"}

[RX EOC:         0]{lang="ES-AR"}

[ ]{lang="EN-US"}

[Line A status:]{lang="EN-US"}

[Xcvr Op State:          Data Mode]{lang="EN-US"}

[Last Fail Op State:     0x00]{lang="EN-US"}

[Line Rate(Kbps):        2312]{lang="EN-US"}

[Wire Type:              2]{lang="EN-US"}

[SNR Margin(dB):         16.30]{lang="EN-US"}

[Loop Attenuation(dB):   0.00]{lang="EN-US"}

[RecvGain(dB):           6.07]{lang="EN-US"}

[TxPower(dBm):           9.50]{lang="EN-US"}

[Power Backoff:          enable]{lang="EN-US"}

[Power Backoff Level:    5]{lang="EN-US"}

[Tip/Ring Reversal:      Reversed]{lang="EN-US"}

[FrmOH Stat:             0x00]{lang="EN-US"}

[Rmt Encoder A:          0x0000016e]{lang="EN-US"}

[Rmt Encoder B:          0x00000331]{lang="EN-US"}

[Rmt NSF Cusdata:        0x0000]{lang="EN-US"}

[Rmt NSF CusID:          0x0000]{lang="EN-US"}

[Rmt Country Code:       0x00b5]{lang="EN-US"}

[Rmt Provider Code:      GSPN]{lang="EN-US"}

[Rmt Vendor Data:        0x12 0x34 0x56 0x78]{lang="EN-US"}

[                        0x12 0x34 0x56 0x78]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_66504801}[当接口状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时显示四线]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display dsl status interface efm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_219342039}

[Operating Mode:]{lang="NO-BOK"}[         ]{lang="ES-AR"}[CPE]{lang="NO-BOK"}

[DSL Mode:]{lang="NO-BOK"}[               ]{lang="ES-AR"}[SHDSLAnnex B]{lang="NO-BOK"}

[Configured Wire Type:   4]{lang="EN-US"}

[Line A Statistics since last activation:]{lang="EN-US"}

[CRC:             0]{lang="ES-AR"}

[LOS WDefect:     0]{lang="ES-AR"}

[ES:              0]{lang="ES-AR"}

[SES:             0]{lang="ES-AR"}

[UAS:             0]{lang="ES-AR"}

[TX EOC:          0]{lang="ES-AR"}

[RX EOC:          0]{lang="ES-AR"}

[ ]{lang="EN-US"}

[Line A status:]{lang="EN-US"}

[Xcvr Op State:          Data Mode]{lang="EN-US"}

[Last Fail Op State:     0x00]{lang="EN-US"}

[Line Rate(Kbps):        2312]{lang="EN-US"}

[Wire Type:              4]{lang="EN-US"}

[SNR Margin(dB):         13.30]{lang="EN-US"}

[Loop Attenuation(dB):   0.00]{lang="EN-US"}

[RecvGain(dB):           5.86]{lang="EN-US"}

[TxPower(dBm):           9.50]{lang="EN-US"}

[Power Backoff:          enable]{lang="EN-US"}

[Power Backoff Level:    5]{lang="EN-US"}

[Tip/Ring Reversal:      Reversed]{lang="EN-US"}

[FrmOH Stat:             0x00]{lang="EN-US"}

[Rmt Encoder A:          0x0000016e]{lang="EN-US"}

[Rmt Encoder B:          0x00000331]{lang="EN-US"}

[Rmt NSF Cusdata:        0x0000]{lang="EN-US"}

[Rmt NSF CusID:          0x0000]{lang="EN-US"}

[Rmt Country Code:       0x00b5]{lang="EN-US"}

[Rmt Provider Code:      GSPN]{lang="EN-US"}

[Rmt Vendor Data:        0x12 0x34 0x56 0x78]{lang="EN-US"}

[                        0x12 0x34 0x56 0x78]{lang="EN-US"}

[ ]{lang="EN-US"}

[Line B Statistics since last activation:]{lang="EN-US"}

[CRC:            1]{lang="ES-AR"}

[LOSW Defect:    1]{lang="ES-AR"}

[ES:             1]{lang="ES-AR"}

[SES:            1]{lang="ES-AR"}

[UAS:            0]{lang="ES-AR"}

[TX EOC:         0]{lang="ES-AR"}

[RX EOC:         0]{lang="ES-AR"}

[ ]{lang="EN-US"}

[Line B status:]{lang="EN-US"}

[Xcvr Op State:          Data Mode]{lang="EN-US"}

[Last Fail Op State:     0x00]{lang="EN-US"}

[Line Rate(Kbps):        2312]{lang="EN-US"}

[Wire Type:              4]{lang="EN-US"}

[SNR Margin(dB):         12.30]{lang="EN-US"}

[Loop Attenuation(dB):   0.00]{lang="EN-US"}

[RecvGain(dB):           5.28]{lang="EN-US"}

[TxPower(dBm):           9.50]{lang="EN-US"}

[Power Backoff:          enable]{lang="EN-US"}

[Power Backoff Level:    5]{lang="EN-US"}

[Tip/Ring Reversal:      Reversed]{lang="EN-US"}

[FrmOH Stat:             0x00]{lang="EN-US"}

[Rmt Encoder A:          0x0000016e]{lang="EN-US"}

[Rmt Encoder B:          0x00000331]{lang="EN-US"}

[Rmt NSF Cusdata:        0x0000]{lang="EN-US"}

[Rmt NSF CusID:          0x0000]{lang="EN-US"}

[Rmt Country Code:       0x00b5]{lang="EN-US"}

[Rmt Provider Code:      GSPN]{lang="EN-US"}

[Rmt Vendor Data:        0x12 0x34 0x56 0x78]{lang="EN-US"}

[                        0x12 0x34 0x56 0x78]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display dsl status]{lang="EN-US"}]{#struct_0_x1622_x8463_1434930345}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1062295776}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_219407575}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1651616258}

[[Operating Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_1737058601}

[[工作模式：]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_621787634}[为用户端，]{style="font-family:宋体"}[CO]{lang="EN-US"}[为中心局端]{style="font-family:宋体"}

[[DSL Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_639619546}

[[接口链路所采用的附加标准：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x192636774}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_219473111}[：]{style="font-family:宋体"}[Annex A]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_x1622_x8463_x1047668879}[：]{style="font-family:宋体"}[Annex B]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}

[[Configured Wire Type]{lang="EN-US"}]{#struct_0_x1622_x8463_x1475092751}

[[配置连线类型，分为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1622_x8463_x569141482}[线制和]{style="font-family:宋体"}[4]{lang="EN-US"}[线制]{style="font-family:宋体"}

[[Line A Statistics since last activation]{lang="EN-US"}]{#struct_0_x1622_x8463_x2024499885}

[[从激活时开始到现在]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_x1450332323}[线对的统计信息]{style="font-family:宋体"}

[[CRC]{lang="EN-US"}]{#struct_0_x1622_x8463_219538647}

[[CRC]{lang="EN-US"}]{#struct_0_x1622_x8463_2034578620}[错误数]{style="font-family:宋体"}

[[LOSW Defect]{lang="EN-US"}]{#struct_0_x1622_x8463_1735306643}

[[LOSW]{lang="EN-US"}]{#struct_0_x1622_x8463_1142172683}[（同步丢失）错误数]{style="font-family:宋体"}

[[ES]{lang="EN-US"}]{#struct_0_x1622_x8463_219604183}

[[每秒错误数]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x363735148}

[[SES]{lang="EN-US"}]{#struct_0_x1622_x8463_2012506218}

[[每秒严重错误数]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1724063236}

[[UAS]{lang="EN-US"}]{#struct_0_x1622_x8463_1955374730}

[[每秒不可用状态计数]{style="font-family:宋体"}]{#struct_0_x1622_x8463_219669719}

[[TX EOC]{lang="EN-US"}]{#struct_0_x1622_x8463_361283842}

[[发送]{style="font-family:宋体"}[ECO]{lang="EN-US"}]{#struct_0_x1622_x8463_192978960}[信源计数]{style="font-family:宋体"}

[[RX EOC]{lang="EN-US"}]{#struct_0_x1622_x8463_71585010}

[[接收]{style="font-family:宋体"}[ECO]{lang="EN-US"}]{#struct_0_x1622_x8463_x1542414352}[信源计数]{style="font-family:宋体"}

[[Line A status]{lang="EN-US"}]{#struct_0_x1622_x8463_219735255}

[[A]{lang="EN-US"}]{#struct_0_x1622_x8463_410214990}[线对状态]{style="font-family:宋体"}

[[Xcvr Op State]{lang="EN-US"}]{#struct_0_x1622_x8463_x899799047}

[[收发器工作状态：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1362883375}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x1622_x8463_218752215}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Data Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_x113933855}[：]{style="font-family:宋体"}[激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HandShaking]{lang="EN-US"}]{#struct_0_x1622_x8463_472610094}[：]{style="font-family:宋体"}[激活握手阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Training]{lang="EN-US"}]{#struct_0_x1622_x8463_143728247}[：]{style="font-family:宋体"}[激活训练阶段]{lang="EN-US" style="font-family:宋体"}

[[Last Fail Op State]{lang="EN-US"}]{#struct_0_x1622_x8463_218817751}

[[上次协商失败收发器工作状态，可能的取值同上]{style="font-family:宋体"}]{#struct_0_x1622_x8463_66504800}

[[Line Rate(Kbps)]{lang="EN-US"}]{#struct_0_x1622_x8463_x222096277}

[[协商线对速率]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1502341317}

[[Wire Type]{lang="EN-US"}]{#struct_0_x1622_x8463_1785360447}

[[线数类型，可能的取值有]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1622_x8463_x859539560}[（]{style="font-family:宋体"}[2]{lang="EN-US"}[线制）、]{style="font-family:宋体"}[4]{lang="EN-US"}[（]{style="font-family:宋体"}[4]{lang="EN-US"}[线制）]{style="font-family:宋体"}

[[SNR Margin(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_1695752873}

[[信噪比容限量]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1518497550}

[[Loop Attenuation(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_1785425983}

[[环路衰减]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x422527492}

[[RecvGain(dB)]{lang="EN-US"}]{#struct_0_x1622_x8463_x48264025}

[[接收增益]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785491519}

[[TxPower(dBm)]{lang="EN-US"}]{#struct_0_x1622_x8463_x439358583}

[[发送功率]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x364148974}

[[Power Backoff]{lang="EN-US"}]{#struct_0_x1622_x8463_x747930652}

[[功率补偿状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785557055}

[[Power Backoff Level]{lang="EN-US"}]{#struct_0_x1622_x8463_x2021141350}

[[功率补偿级别]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x767377925}

[[Tip/Ring Reversal]{lang="EN-US"}]{#struct_0_x1622_x8463_1785622591}

[[Tip/Ring]{lang="EN-US"}]{#struct_0_x1622_x8463_x50688510}[翻转状态]{style="font-family:宋体"}

[[FrmOH Stat]{lang="EN-US"}]{#struct_0_x1622_x8463_x1454622484}

[[帧溢出状态]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785688127}

[[Rmt Encoder A]{lang="EN-US"}]{#struct_0_x1622_x8463_12702293}

[[远端译码器系数]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_x1622_x8463_x1623913511}

[[Rmt Encoder B]{lang="EN-US"}]{#struct_0_x1622_x8463_x1597346385}

[[远端译码器系数]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_x1622_x8463_1785753663}

[[Rmt NSF Cusdata]{lang="EN-US"}]{#struct_0_x1622_x8463_1095369327}

[[远端非标准格式用户数据]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x422297761}

[[Rmt NSF CusID]{lang="EN-US"}]{#struct_0_x1622_x8463_1785819199}

[[远端非标准格式用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1622_x8463_x1576516043}

[[Rmt Country Code]{lang="EN-US"}]{#struct_0_x1622_x8463_x1426529375}

[[远端国家代码]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1784836159}

[[Rmt Provider Code]{lang="EN-US"}]{#struct_0_x1622_x8463_1102602148}

[[远端芯片供应商代码]{style="font-family:宋体"}]{#struct_0_x1622_x8463_687880814}

[[Rmt Vendor Data]{lang="EN-US"}]{#struct_0_x1622_x8463_1784901695}

[[远端制造商代码]{style="font-family:宋体"}]{#struct_0_x1622_x8463_722397932}

[ ]{lang="EN-US"}

::::: {#1828835274 .myid}
[]{#_Toc404784026}[]{#struct_0_x1622_x8463_440087736}[]{#_Toc345946889}

**ATM接口 \-- EFM接口配置命令 \-- display dsl version**

------------------------------------------------------------------------

[**[display dsl version]{lang="EN-US"}**]{#struct_0_x1622_x8463_725445450}[命令用来显示]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的版本信息和支持的能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1785360448}

[**[display dsl version interface efm]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1622_x8463_x859736168}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1345206024}

[[ ]{lang="EN-US"}]{#struct_0_x1622_x8463_663783540}[任意视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_114471318}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1179857198}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_1967502856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1122091940}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_1785425984}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x422199812}

[**[interface efm]{lang="EN-US"}**]{#struct_0_x1622_x8463_691083849}*[ interface-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的版本信息和支持的能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_641043833}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image003.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x1514697737}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与具体芯片相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x57223453}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x712321977}[显示]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[上的版本信息和支持的能力。]{style="font-family:宋体"}

[[\<Sysname\> display dsl version interface efm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_1785491520}

[DSL Line Type:          G.SHDSL]{lang="EN-US"}

[ATM SAR Device:         0x823614f1]{lang="EN-US"}

[ATM SAR Revision:       0x02]{lang="EN-US"}

[Chipset Vendor:         GSPN]{lang="EN-US"}

[Firmware Rel-Rev:       R2.3.1-0]{lang="EN-US"}

[DSP Version:            1]{lang="EN-US"}

[PCB Version:            0.0]{lang="EN-US"}

[CPLD Version:           0.0]{lang="EN-US"}

[Driver Version:         2.0]{lang="EN-US"}

[Hardware Version:       1.0]{lang="EN-US"}

[ITU G991.2 ANNEX A:     Supported]{lang="EN-US"}

[ITU G991.2 ANNEX B:     Supported]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display dsl version]{lang="EN-US"}]{#struct_0_x1622_x8463_x438768758}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1044054452}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1151170677}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x939951560}

[[DSL Line Type]{lang="EN-US"}]{#struct_0_x1622_x8463_1405513303}

[[用户接入线的类型]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785557056}

[[ATM SAR Device]{lang="EN-US"}]{#struct_0_x1622_x8463_x2021206886}

[[SAR]{lang="EN-US"}]{#struct_0_x1622_x8463_x958352174}[芯片的标识]{style="font-family:宋体"}

[[ATM SAR Revision]{lang="EN-US"}]{#struct_0_x1622_x8463_x1242953479}

[[SAR]{lang="EN-US"}]{#struct_0_x1622_x8463_1559876837}[芯片的修改标识]{style="font-family:宋体"}

[[Chipset Vendor]{lang="EN-US"}]{#struct_0_x1622_x8463_x68327319}

[[DSL Chipsets]{lang="EN-US"}]{#struct_0_x1622_x8463_1785622592}[的厂商标识]{style="font-family:宋体"}

[[Firmware Rel-Rev]{lang="EN-US"}]{#struct_0_x1622_x8463_x50885118}

[[FirmWare]{lang="EN-US"}]{#struct_0_x1622_x8463_1136617096}[的标识和版本信息]{style="font-family:宋体"}

[[DSP Version]{lang="EN-US"}]{#struct_0_x1622_x8463_1467070223}

[[DSP]{lang="EN-US"}]{#struct_0_x1622_x8463_x470658098}[版本]{style="font-family:宋体"}

[[PCB Version]{lang="EN-US"}]{#struct_0_x1622_x8463_1785688128}

[[单板]{style="font-family:宋体"}[PCB]{lang="EN-US"}]{#struct_0_x1622_x8463_12243541}[的版本号]{style="font-family:宋体"}

[[CPLD Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x686140998}

[[逻辑器件的版本号]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1093647267}

[[Driver Version]{lang="EN-US"}]{#struct_0_x1622_x8463_x683670233}

[[驱动软件的版本号]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785753664}

[[Hardware Version]{lang="EN-US"}]{#struct_0_x1622_x8463_1095303791}

[[硬件版本]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x451085576}

[[ITU G991.2 ANNEX A]{lang="EN-US"}]{#struct_0_x1622_x8463_1100524187}[，]{style="font-family:宋体"}[ITU G991.2 ANNEX B]{lang="EN-US"}

[[接口支持的标准及其附加标准]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785819200}

[ ]{lang="EN-US"}

::: {#-1947707384 .myid}
[]{#_Toc345946890}[]{#struct_0_x1622_x8463_1144014380}[]{#_Toc404784027}[]{#_Toc354243964}

**ATM接口 \-- EFM接口配置命令 \-- display interface efm**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[efm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1159958174}[命令用来显示]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_234827084}

[**[display interface]{lang="EN-US"}**[ \[ **efm** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x1622_x8463_749514451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_808980853}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_731508010}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1784836160}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1102143397}

[[network-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_x504320215}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x882839265}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1622_x8463_1234375983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_912641583}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1622_x8463_x1365576908}[：显示指定]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的信息，]{style="font-family:宋体"}[interface-number]{lang="EN-US"}[表示]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x1622_x8463_958848528}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x1622_x8463_722463468}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x1622_x8463_1841825169}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1920091840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x1622_x8463_676767871}**[efm]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1622_x8463_x8286137}**[efm]{lang="EN-US"}**[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有]{lang="EN-US" style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_974815342}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_440790309}[显示接口]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface efm 2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_1785360445}

[EFM2/4/0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: EFM2/4/0 Interface]{lang="EN-US"}

[Bandwidth: 20000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: b8af-67fa-10f0]{lang="EN-US"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: b8af-67fa-10f0]{lang="EN-US"}

[2Wire-Shdsl Line, Operation State: DOWN_NOT_READY, Operating Mode: CO]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}

[Input:]{lang="EN-US"}

[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}

[  0 errors, 0 crcs, 0 lens, 0 giants]{lang="EN-US"}

[  0 pads, 0 aborts, 0 timeouts]{lang="EN-US"}

[  0 overflows, 0 overruns, 0 no buffer]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}

[  0 errors, 0 overflows, 0 underruns]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x859408488}[显示接口]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface efm 2/4/0 brief]{lang="EN-US"}]{#struct_0_x1622_x8463_1785425981}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[EFM2/4/0             UP   UP(s)    \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x422396420}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface efm brief down]{lang="EN-US"}]{#struct_0_x1622_x8463_1502681027}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[EFM2/4/0             DOWN Not connected]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display interface efm]{lang="EN-US"}]{#struct_0_x1622_x8463_1932040256}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1048240856}[[字段]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1405031710}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2019530884}

[[EFM2/4/0]{lang="EN-US"}]{#struct_0_x1622_x8463_1785491517}

[[Current state]{lang="EN-US"}]{#struct_0_x1622_x8463_x438703223}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x356493485}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_1790743744}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_x33686922}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_x1062137002}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x1622_x8463_1785557053}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x2021010278}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_x1296862815}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_1529697942}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1622_x8463_1597751038}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785622589}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x1622_x8463_x50164223}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1031665556}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x1622_x8463_86831713}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1641489128}

[[Hold timer]{lang="EN-US"}]{#struct_0_x1622_x8463_1785688125}

[[轮询时间间隔]{style="font-family:宋体"}]{#struct_0_x1622_x8463_12571221}

[[Internet protocol processing ]{lang="EN-US"}]{#struct_0_x1622_x8463_x2126894049}

[[网络层协议处理状况：（]{style="font-family:宋体"}[enabled/disabled]{lang="EN-US"}]{#struct_0_x1622_x8463_x690951014}[）]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_x1622_x8463_162509293}

[[IP]{lang="EN-US"}]{#struct_0_x1622_x8463_1785753661}[报文帧类型]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_x1622_x8463_1095500399}

[[IPv6]{lang="EN-US"}]{#struct_0_x1622_x8463_x1619568621}[报文帧类型]{style="font-family:宋体"}

[[Hardware Address]{lang="EN-US"}]{#struct_0_x1622_x8463_x703774597}

[[接口的硬件地址]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785819197}

[[2Wire-Shdsl Line]{lang="EN-US"}]{#struct_0_x1622_x8463_x1576909259}

[[线对采用的连线模式：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2067406850}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2Wire-Shdsl]{lang="EN-US"}]{#struct_0_x1622_x8463_917701486}[：]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[线模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4Wire-Shdsl]{lang="EN-US"}]{#struct_0_x1622_x8463_1784836157}[：]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[线模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6Wire-Shdsl]{lang="EN-US"}]{#struct_0_x1622_x8463_1102471076}[：]{lang="EN-US" style="font-family:宋体"}[6]{lang="EN-US"}[线模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8Wire-Shdsl]{lang="EN-US"}]{#struct_0_x1622_x8463_x2064607234}[：]{lang="EN-US" style="font-family:宋体"}[8]{lang="EN-US"}[线模式]{lang="EN-US" style="font-family:宋体"}

[[Operation State]{lang="EN-US"}]{#struct_0_x1622_x8463_x111984444}

[[线对的状态：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1784901693}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN_NOT_READY]{lang="EN-US"}]{#struct_0_x1622_x8463_722791148}[：线路处于]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[，未就绪状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN\_ READY]{lang="EN-US"}]{#struct_0_x1622_x8463_x1714909226}[：线路处于]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[，就绪状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INITIALIZING]{lang="EN-US"}]{#struct_0_x1622_x8463_1785360446}[：线路处于正在协商的状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP_DATA_MODE]{lang="EN-US"}]{#struct_0_x1622_x8463_x859605096}[：线路协商成功，处于数据模式]{lang="EN-US" style="font-family:宋体"}

[[Operating Mode]{lang="EN-US"}]{#struct_0_x1622_x8463_2115349451}

[[线对的工作模式：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_251734073}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_1785425982}[：表示模式为局端模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_x422593028}[：表示模式为用户端模式]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_x1622_x8463_613917168}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x1622_x8463_x952166773}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x1622_x8463_x788908449}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1550291351}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_x1622_x8463_1785491518}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1622_x8463_x439293047}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_x1622_x8463_791172744}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1622_x8463_1785557054}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"} [packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input:]{lang="EN-US"}]{#struct_0_x1622_x8463_x2021075814}

[[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_791457573}

[[  0 errors, 0 crcs, 0 lens, 0 giants]{lang="EN-US"}]{#struct_0_x1622_x8463_1785622590}

[[  0 pads, 0 aborts, 0 timeouts]{lang="EN-US"}]{#struct_0_x1622_x8463_x50754046}

[[  0 overflows, 0 overruns, 0 no buffer]{lang="EN-US"}]{#struct_0_x1622_x8463_x212537016}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_x1622_x8463_x680376550}[：接口收到的总报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_x1622_x8463_1785688126}[：接口收到的总字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_12636757}[：]{style="font-family:宋体"} [接口接收报文所使用缓冲区个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_x1622_x8463_x1944286444}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[crcs]{lang="EN-US"}]{#struct_0_x1622_x8463_1785753662}[：]{style="font-family:宋体"}[CRC]{lang="EN-US"}[错误数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[lens]{lang="EN-US"}]{#struct_0_x1622_x8463_1095434863}[：]{style="font-family:宋体"} [接口接收到长度错误的报文个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_x1622_x8463_1127164563}[：接口接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pads]{lang="EN-US"}]{#struct_0_x1622_x8463_1785819198}[：]{style="font-family:宋体"} [接口接收报文进行填充时发生的相关错误个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_x1622_x8463_x1576450507}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[timeouts]{lang="EN-US"}]{#struct_0_x1622_x8463_310767948}[：接口接收报文超时的个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overflows]{lang="EN-US"}]{#struct_0_x1622_x8463_1784836158}[：接口接收报文时芯片]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[溢出错误个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_x1622_x8463_1102667684}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffer]{lang="EN-US"}]{#struct_0_x1622_x8463_x1277132415}[：]{style="font-family:宋体"} [接口接收报文时因系统资源不足产生的相关错误]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_x1622_x8463_1784901694}

[[  0 packets, 0 bytes, 0 buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_722332396}

[[  0 errors, 0 overflows, 0 underruns]{lang="EN-US"}]{#struct_0_x1622_x8463_1785360443}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_x1622_x8463_x859277416}[：接口发送的总报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_x1622_x8463_182829481}[：接口发送的总字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[buffers]{lang="EN-US"}]{#struct_0_x1622_x8463_1785425979}[：接口发送报文所使用的缓冲区个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_x1622_x8463_x421872141}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overflows]{lang="EN-US"}]{#struct_0_x1622_x8463_x1502745842}[：接口发送报文时芯片]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[溢出错误个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_x1622_x8463_1785491515}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_x1622_x8463_x438572151}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_x1622_x8463_1785557051}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x1622_x8463_x2020879206}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1822386172}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1622_x8463_1785622587}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x1622_x8463_x50557439}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x1622_x8463_1785688123}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1622_x8463_12964437}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x991958245}

[[Link]{lang="EN-US"}]{#struct_0_x1622_x8463_1785753659}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1094976112}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_1785819195}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_925700109}[：表示接口物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x1622_x8463_x1576778187}[：表示接口被手工关闭了，需要执行]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1622_x8463_1846064062}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1784901691}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1622_x8463_875819676}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1622_x8463_875754140}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x1622_x8463_876212892}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x1622_x8463_722660076}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1622_x8463_1785360444}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1622_x8463_x859474024}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x1622_x8463_1785425980}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x1622_x8463_x422461956}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1622_x8463_x1597540874}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#147137292 .myid}
[]{#_Toc404784028}[]{#struct_0_x1622_x8463_1785491516}

**ATM接口 \-- EFM接口配置命令 \-- interface efm**

------------------------------------------------------------------------

[**[interface efm]{lang="EN-US"}**]{#struct_0_x1622_x8463_x438637687}[命令用来进入]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口或子接口视图。在进入子接口视图之前，如果指定的子接口不存在，则先创建子接口，再进入该子接口的视图。]{style="font-family:宋体"}

[**[undo interface efm]{lang="EN-US"}**]{#struct_0_x1622_x8463_841712908}[命令用来删除]{style="font-family:宋体"}[EFM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x319729902}

[**[interface efm]{lang="EN-US"}**[ { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_x1622_x8463_x595000579}

[**[undo interface efm]{lang="EN-US"}**[ *interface-number.subnumber*]{lang="EN-US"}]{#struct_0_x1622_x8463_x1731320513}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x849383899}

[[不存在]{style="font-family:宋体"}[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_387947611}[子接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x560469846}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1785557052}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2020944742}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1047504590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x656707376}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1367523951}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1622_x8463_x1374441225}[：]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_x1622_x8463_x1819688050}[：]{style="font-family:
宋体"}[EFM]{lang="EN-US"}[子接口编号，其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，但单个]{style="font-family:宋体"}[EFM]{lang="EN-US"}[主接口上最大只能创建]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[EFM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_287628744}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1540001977}[进入]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1785622588}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\]]{lang="SV"}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x50229759}[创建]{style="font-family:宋体"}[EFM]{lang="EN-US"}[子接口]{style="font-family:宋体"}[EFM2/4/0.1]{lang="EN-US"}[并进入子接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_375148169}

[\[Sysname\] interface efm 2/4/0.1]{lang="EN-US"}

[\[Sysname-EFM2/4/0.1\]]{lang="SV"}
:::

::: {#552212377 .myid}
[]{#_Toc404784029}[]{#struct_0_x1622_x8463_1537779824}[]{#_Toc345946891}

**ATM接口 \-- EFM接口配置命令 \-- shdsl annex**

------------------------------------------------------------------------

[**[shdsl annex]{lang="EN-US"}**]{#struct_0_x1622_x8463_731858164}[命令是用来配置]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口所支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}[标准。当两端标准不同，线路会难以激活。]{style="font-family:宋体"}

[**[undo shdsl annex]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2088929691}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1785688124}

[**[shdsl annex]{lang="EN-US"}**[ { **a** \| **b** }]{lang="EN-US"}]{#struct_0_x1622_x8463_12505685}

[**[undo shdsl annex]{lang="EN-US"}**]{#struct_0_x1622_x8463_1717156393}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_136572466}

[[支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}]{#struct_0_x1622_x8463_x1255201315}[标准为]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1180014389}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x144247475}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x788018786}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x693592283}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1785753660}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1095565935}

[**[a]{lang="EN-US"}**]{#struct_0_x1622_x8463_347715034}[：支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}[标准为]{style="font-family:宋体"}[Annex a]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[b]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1499911062}[：支持的]{style="font-family:宋体"}[Annex]{lang="EN-US"}[标准为]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1073348119}

[[Annex a/b]{lang="EN-US"}]{#struct_0_x1622_x8463_x369425795}[均是]{style="font-family:宋体"}[G.991.2]{lang="EN-US"}[的标准，]{style="font-family:宋体"}[Annex a]{lang="EN-US"}[主要在北美应用，]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[主要在欧洲应用，其它地区网络要根据当地网络的不同，选择不同的标准，例如中国地区网络执行的标准类型为]{style="font-family:宋体"}[Annex b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1525520302}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x76571206}[配置]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[所支持的标准为]{style="font-family:宋体"}[Annex ]{lang="EN-US"}[a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1785819196}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\]]{lang="SV"}[ ]{lang="SV"}[shdsl annex a]{lang="EN-US"}
:::

::: {#-1178970197 .myid}
[]{#_Toc404784030}[]{#struct_0_x1622_x8463_x1576843723}[]{#_Toc345946892}

**ATM接口 \-- EFM接口配置命令 \-- shdsl capability**

------------------------------------------------------------------------

[**[shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1124549701}[命令用来配置接口的协商能力。]{style="font-family:宋体"}

[**[undo shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1261618246}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1035733948}

[**[shdsl capability]{lang="EN-US"}**[ { **auto** \| **g-shdsl** \| **g-shdsl-bis** }]{lang="EN-US"}]{#struct_0_x1622_x8463_649759065}

[**[undo shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_x845661602}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_275088939}

[[在]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_1784836156}[模式下，采用]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[方式。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_1102536612}[模式下，采用]{style="font-family:宋体"}**[g-shdsl-bis]{lang="EN-US"}**[方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_290851966}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1214238463}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x232556701}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1384118590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_637588084}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x671213434}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2065729930}[：自动选择与对端接口相同的协商能力（只在]{style="font-family:宋体"}[CPE]{lang="EN-US"}[模式下支持，在]{style="font-family:宋体"}[CO]{lang="EN-US"}[模式下不支持）。]{style="font-family:宋体"}

[**[g-shdsl]{lang="EN-US"}**]{#struct_0_x1622_x8463_1784901692}[：使用]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g-shdsl-bis]{lang="EN-US"}**]{#struct_0_x1622_x8463_722725612}[：使用]{style="font-family:宋体"}[G.SHDSL.bis]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1400713444}

[[在]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_x31281422}[模式下支持]{style="font-family:宋体"}[g-shdsl]{lang="EN-US"}[和]{style="font-family:宋体"}[g-shdsl-bis]{lang="EN-US"}[以及]{style="font-family:宋体"}[auto]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_x918575729}[模式下支持]{style="font-family:宋体"}[g-shdsl]{lang="EN-US"}[和]{style="font-family:宋体"}[g-shdsl-bis]{lang="EN-US"}[，不支持]{style="font-family:宋体"}[auto]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在配置]{style="font-family:宋体"}**[shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1061801907}[时，会自动恢复为各自模式下的缺省配置。]{style="font-family:宋体"}

[[两端接口需要使用相同的协商能力，才能协商成功。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x2117350499}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x787362677}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_628710251}[配置接口的协商能力为]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x943522908}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\] shdsl capability g-shdsl]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x503633927}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[shdsl mode]{lang="SV"}]{#struct_0_x1622_x8463_2001632518}
:::

::: {#-184178899 .myid}
[]{#_Toc404784031}[]{#struct_0_x1622_x8463_260517494}[]{#_Toc345946893}

**ATM接口 \-- EFM接口配置命令 \-- shdsl line-probing**

------------------------------------------------------------------------

[**[shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1184503441}[命令用来开启]{style="font-family:
宋体"}[SHDSL]{lang="EN-US"}[线路的探询功能。]{style="font-family:宋体"}

[**[undo shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_1549867981}[命令用来关闭]{style="font-family:
宋体"}[SHDSL]{lang="EN-US"}[线路的探询功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x975701042}

[**[shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_x943457372}

[**[undo shdsl line-probing enable]{lang="EN-US"}**]{#struct_0_x1622_x8463_1037421132}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1286774781}

[[线路的探询功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x115586699}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x133579843}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_1700270773}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x8969170}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x2132165624}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1755810024}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943391836}

[[开启探询功能后，在线路激活的过程中，系统将执行线路探询功能去协商最佳的线路速率；若关闭探询功能，系统会选择]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_1446610315}[和]{style="font-family:宋体"}[CO]{lang="EN-US"}[都支持的速率交集中的最大速率。这种方式因为跳过了线路速率的适配过程，减短了激活]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路的时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_2127053715}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_940475697}[关闭]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路的探询功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1684417230}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\] ]{lang="SV"}[undo shdsl line-probing enable]{lang="EN-US"}
:::

::: {#-477819422 .myid}
[]{#_Toc404784032}[]{#struct_0_x1622_x8463_1328469185}[]{#_Toc345946894}

**ATM接口 \-- EFM接口配置命令 \-- shdsl mode**

------------------------------------------------------------------------

[**[shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_1354583255}[命令用来配置]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的工作模式。]{style="font-family:宋体"}

[**[undo shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_380880538}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943326300}

[**[shdsl mode]{lang="EN-US"}**[ { **co** \| **cpe** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1682746037}

[**[undo shdsl mode]{lang="EN-US"}**]{#struct_0_x1622_x8463_x958613054}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2008443651}

[[工作模式为]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_812403302}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x906253512}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_913603620}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_288311661}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x943260764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1733029722}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1923676598}

[**[co]{lang="EN-US"}**]{#struct_0_x1622_x8463_2067155567}[：配置为]{style="font-family:宋体"}[CO]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[cpe]{lang="EN-US"}**]{#struct_0_x1622_x8463_2135854571}[：配置为]{style="font-family:宋体"}[CPE]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1966290221}

[[两台设备直连时，必须把一端配置为]{style="font-family:宋体"}[CO]{lang="EN-US"}]{#struct_0_x1622_x8463_98194444}[模式，另一端配置成]{style="font-family:宋体"}[CPE]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x177616712}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1285602914}[配置]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[CO]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x943195228}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\] shdsl mode co]{lang="SV"}
:::

::: {#-1131078901 .myid}
[]{#_Toc404784033}[]{#struct_0_x1622_x8463_267105016}[]{#_Toc345946895}

**ATM接口 \-- EFM接口配置命令 \-- shdsl pam**

------------------------------------------------------------------------

[**[shdsl pam]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2063652737}[用来配置]{style="font-family:宋体"}[PAM Constellation]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo shdsl pam]{lang="EN-US"}**]{#struct_0_x1622_x8463_x833956330}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1862665791}

[**[shdsl pam]{lang="SV"}**[ ]{lang="SV"}[{ ]{lang="EN-US"}]{#struct_0_x1622_x8463_1805484638}**[16]{lang="SV"}**[ ]{lang="SV"}[\| ]{lang="EN-US"}**[32]{lang="SV"}[ ]{lang="SV"}**[\| ]{lang="EN-US"}**[auto]{lang="SV"}**[ ]{lang="SV"}[}]{lang="EN-US"}

[**[undo shdsl pam]{lang="SV"}**]{#struct_0_x1622_x8463_463992275}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943129692}

[[自动选择]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_x1622_x8463_x595711433}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x2128432727}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_1444883225}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_299814453}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_303963700}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1235374326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1793650612}

[**[16]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2116278160}[：使用]{style="font-family:宋体"}[16 PAM Constellation]{lang="EN-US"}[。在]{style="font-family:宋体"}[16 PAM]{lang="EN-US"}[下，速率范围为]{style="font-family:宋体"}[192]{lang="EN-US"}[～]{style="font-family:宋体"}[3840]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_x1622_x8463_x943064156}[：使用]{style="font-family:宋体"}[32 PAM Constellation]{lang="EN-US"}[。在]{style="font-family:宋体"}[32 PAM]{lang="EN-US"}[下，速率范围为]{style="font-family:宋体"}[768]{lang="EN-US"}[～]{style="font-family:宋体"}[5696]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_x145867271}[：根据线路两端的参数自动选择两端都支持的最好的]{style="font-family:宋体"}[PAM]{lang="EN-US"}[（]{style="font-family:宋体"}[32 PAM]{lang="EN-US"}[比]{style="font-family:宋体"}[16 PAM]{lang="EN-US"}[好）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x381760824}

[[PAM]{lang="EN-US"}]{#struct_0_x1622_x8463_915490063}[是数字线路的一种编码模式，叫脉冲调制模式，]{style="font-family:宋体"}[Constellation]{lang="EN-US"}[用来形容]{style="font-family:宋体"}[PAM]{lang="EN-US"}[编码方式像星座。本命令用于配置]{style="font-family:宋体"}[PHY]{lang="EN-US"}[芯片的数字信号调制模式。]{style="font-family:宋体"}

[[当接口的协商能力为]{style="font-family:宋体"}[G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_898843649}[时，不支持]{style="font-family:宋体"}[32 PAM Constellation]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x195659322}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x633795342}[配置]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[使用]{style="font-family:宋体"}[16 PAM Constellation]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1896848306}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\] shdsl pam 16]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x944047196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[shdsl capability]{lang="EN-US"}**]{#struct_0_x1622_x8463_1283311962}
:::

::: {#-1175254568 .myid}
[]{#_Toc404784034}[]{#struct_0_x1622_x8463_1776544814}[]{#_Toc345946896}

**ATM接口 \-- EFM接口配置命令 \-- shdsl pbo**

------------------------------------------------------------------------

[**[shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_864749262}[命令用来调整发送功率。]{style="font-family:宋体"}

[**[undo shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_2015916998}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x629677944}

[**[shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_1696894210}[ { *value* \| **auto**]{lang="SV"}[ ]{lang="SV"}[}]{lang="EN-US"}

[**[undo shdsl pbo]{lang="SV"}**]{#struct_0_x1622_x8463_2083596817}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943981660}

[[自动调整发送功率。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x939096504}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1299253127}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1588049949}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x306200916}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_715059391}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1174056216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x966725464}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_1224829036}[：自动调整发送功率。]{style="font-family:宋体"}

[*[value]{lang="SV"}*]{#struct_0_x1622_x8463_x943522907}[：发送功率调整值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[dB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x504223751}

[[正常情况下，接口会根据线路噪声情况，自动调整发送功率，以保证可以获得合适的信噪比。当线路的噪声已知的情况下，或者自动调整不准确的时候，可以通过此命令行手动调整发射功率。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x508658655}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x427583872}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_1576427277}[配置]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[接口的发送功率调整值为]{style="font-family:宋体"}[20db]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1366260616}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\] shdsl pbo 20]{lang="SV"}
:::

::: {#332097330 .myid}
[]{#_Toc404784035}[]{#struct_0_x1622_x8463_209867789}[]{#_Toc345946897}

**ATM接口 \-- EFM接口配置命令 \-- shdsl psd**

------------------------------------------------------------------------

[**[shdsl psd]{lang="EN-US"}**]{#struct_0_x1622_x8463_x943457371}[命令用来配置]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的功率频谱密度模式。]{style="font-family:宋体"}

[**[undo shdsl psd]{lang="EN-US"}**]{#struct_0_x1622_x8463_1037224524}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_925516527}

[**[shdsl psd ]{lang="EN-US"}**[{ **asymmetry** \| **symmetry** }]{lang="EN-US"}]{#struct_0_x1622_x8463_986053622}

[**[undo shdsl psd]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2084885263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_672682760}

[[功率频谱密度模式为对称模式。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_2043192007}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1240511042}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1186806698}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943391835}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1446413707}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_162975415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_567828749}

[**[asymmetry]{lang="EN-US"}**]{#struct_0_x1622_x8463_859138900}[：功率频谱密度模式为非对称模式。]{style="font-family:宋体"}

[**[symmetry]{lang="EN-US"}**]{#struct_0_x1622_x8463_495933731}[：功率频谱密度模式为对称模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1208361039}

[[PSD]{lang="EN-US"}]{#struct_0_x1622_x8463_960744980}[（]{style="font-family:宋体"}[Power Spectral Density]{lang="EN-US"}[，功率频谱密度）指发射功率在最高准位时，一脉冲或一序列脉冲，其单位带宽的总输出能量除以总脉冲持续时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943326299}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_656495956}[配置]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[的功率频谱密度模式为非对称模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x167770446}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\] shdsl psd asymmetry]{lang="SV"}
:::

::: {#1958013934 .myid}
[]{#_Toc404784036}[]{#struct_0_x1622_x8463_x790617757}[]{#_Toc345946898}

**ATM接口 \-- EFM接口配置命令 \-- shdsl rate**

------------------------------------------------------------------------

[**[shdsl rate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2000971002}[命令用来配置]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口单线对的速率。]{style="font-family:宋体"}

[**[undo shdsl rate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1172978282}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1754084118}

[**[shdsl rate]{lang="EN-US"}**[ { *rate* \| **auto** }]{lang="EN-US"}]{#struct_0_x1622_x8463_121262757}

[**[undo shdsl rate]{lang="EN-US"}**]{#struct_0_x1622_x8463_x943260763}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1733095258}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_1944147638}[、]{style="font-family:宋体"}[EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[、]{style="font-family:宋体"}[EFM SHDSL 8WIRE_BIS]{lang="EN-US"}[接口的单线对速率为自动协商方式。]{style="font-family:宋体"}

[[EFM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_x673121105}[接口，在两线模式下单线对速率为自动协商方式，在非两线模式下的单线对速率为]{style="font-family:宋体"}[2312kbit/s]{lang="EN-US"}[（即四线接口速率为]{style="font-family:宋体"}[4624kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x233468576}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_162760560}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x415509044}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x580320577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1202699103}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943195227}

[*[rate]{lang="EN-US"}*]{#struct_0_x1622_x8463_267956984}[：]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的单线对速率最大值。对于]{style="font-family:宋体"}[EFM G.SHDSL]{lang="EN-US"}[接口和]{style="font-family:宋体"}[EFM SHDSL_4WIRE]{lang="EN-US"}[接口，取值范围为]{style="font-family:宋体"}[192]{lang="EN-US"}[～]{style="font-family:宋体"}[2312]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[；]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[EFM]{lang="EN-US"}[ SDHSL_4WIRE_BIS]{lang="EN-US"}[接口和]{style="font-family:宋体"}[EFM]{lang="EN-US"}[ SHDSL_8WIRE_BIS]{lang="EN-US"}[接口，取值范围为]{style="font-family:宋体"}[192]{lang="EN-US"}[～]{style="font-family:宋体"}[5696]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_122818361}[：为自动协商方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1139830381}

[[在实际使用中，最大下行速率还会受局端设备的限制和线路条件的限制，有可能达不到设置的值。如果将速率设置成自动协商方式，在激活过程中两端会根据当前的线路状况协商出一个合适的速率；如果]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_x1622_x8463_576995782}[端和]{style="font-family:宋体"}[CO]{lang="EN-US"}[端设置成固定速率，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[端和]{style="font-family:宋体"}[CO]{lang="EN-US"}[端将进行速率协商，若无法满足二者之中较低的速率要求的时候，线路无法被激活。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x702254593}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[四线（即双线对）的]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1324170460}[EFM]{lang="EN-US"}[接口的速率为单线对速率的两倍。例如设置单线对速率为]{style="font-family:宋体"}[2312kbit/s]{lang="EN-US"}[，则四线接口的速率为]{style="font-family:宋体"}[4624kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[四线的]{style="font-family:宋体"}]{#struct_0_x1622_x8463_x1807498057}[EFM]{lang="EN-US"}[接口的单线对速率无法配置成]{style="font-family:宋体"}[auto]{lang="EN-US"}[方式，因为四线的接口无法进行速率的协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943129691}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x595776969}[配置]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[的单线对速率为自动协商方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_1437863807}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\] shdsl rate auto]{lang="SV"}
:::

::: {#-2090916309 .myid}
[]{#_Toc404784037}[]{#struct_0_x1622_x8463_1745979566}[]{#_Toc345946899}

**ATM接口 \-- EFM接口配置命令 \-- shdsl snr-margin**

------------------------------------------------------------------------

[**[shdsl snr-margin]{lang="EN-US"}**]{#struct_0_x1622_x8463_1065245735}[命令用来配置]{style="font-family:宋体"}[SNR]{lang="EN-US"}[的目标容限量。]{style="font-family:宋体"}

[**[undo shdsl snr-margin]{lang="EN-US"}**]{#struct_0_x1622_x8463_x513959150}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_900989753}

[**[shdsl snr-margin ]{lang="EN-US"}**[\[ **current** *current-margin-value* \] \[ **snext** *snext-margin-value* \]]{lang="EN-US"}]{#struct_0_x1622_x8463_x1884905396}

[**[undo shdsl snr-margin]{lang="EN-US"}**]{#struct_0_x1622_x8463_501691398}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943064155}

[[线路协商时]{style="font-family:宋体"}[current-margin-value]{lang="EN-US"}]{#struct_0_x1622_x8463_x145932807}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:
宋体"}[snext-margin-value]{lang="EN-US"}[为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1600530557}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_603071297}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1847664702}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_792347677}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1682190393}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_257062729}

[**[current]{lang="EN-US"}***[ current-margin-value]{lang="EN-US"}*]{#struct_0_x1622_x8463_x205361211}[：当前信噪比容限量。]{style="font-family:宋体"}*[current-margin-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路在训练的时候以线路信噪比门限加上]{style="font-family:宋体"}*[current-margin-value]{lang="EN-US"}*[进行训练。配置比较大的]{style="font-family:宋体"}*[current-margin-value]{lang="EN-US"}*[可以使得协商成功的链路更加稳定，抗噪能力更强。]{style="font-family:宋体"}

[**[snext ]{lang="EN-US"}***[snext-margin-value]{lang="EN-US"}*]{#struct_0_x1622_x8463_x944047195}[：最差的信噪比容限量。]{style="font-family:宋体"}*[snext-margin-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}[SHDSL]{lang="EN-US"}[线路在训练的时候以最差信噪比门限加上]{style="font-family:宋体"}*[snext-margin-value]{lang="EN-US"}*[进行训练。设置比较大的]{style="font-family:宋体"}*[snext-margin-value]{lang="EN-US"}*[可以使得协商成功的链路更加稳定，抗噪能力更强。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1283508570}

[[配置信噪比容限量会影响线路支持的最大速率。因此在线路比较好的情况下，可以配置较小的信噪比容限量，以获得更高的速率。但是，在线路存在较多的噪声的情况下，配置过小的当前信噪比容限量会造成线路容易掉线。]{style="font-family:宋体"}]{#struct_0_x1622_x8463_987615730}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_392534519}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1163408075}[配置接口]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[的当前信噪比容限量为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x822946719}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\]]{lang="SV"}[ ]{lang="SV"}[shdsl snr-margin current 5]{lang="EN-US"}
:::

::: {#-1575229111 .myid}
[]{#_Toc404784038}[]{#struct_0_x1622_x8463_721819784}[]{#_Toc345946900}

**ATM接口 \-- EFM接口配置命令 \-- shdsl wire**

------------------------------------------------------------------------

[**[shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_x943981659}[命令用来配置]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的连线模式。]{style="font-family:宋体"}

[**[undo shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_x939555253}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1729324174}

[[在]{style="font-family:宋体"}[EFM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_x12840640}[、]{style="font-family:宋体"}[EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图下：]{style="font-family:宋体"}

[**[shdsl wire]{lang="EN-US"}**[ { **2** \| **4-auto-enhanced** \| **4-enhanced** \| **4-standard** }]{lang="EN-US"}]{#struct_0_x1622_x8463_x1566762974}

[**[undo shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_x41732304}

[[在]{style="font-family:宋体"}[EFM SHDSL_8WIRE_BIS]{lang="EN-US"}]{#struct_0_x1622_x8463_x1838779281}[接口视图下：]{style="font-family:宋体"}

[**[shdsl wire]{lang="EN-US"}**[ { **2** \| **4-enhanced** \| **4-standard** \| **6** \| **8** \| **auto** }]{lang="EN-US"}]{#struct_0_x1622_x8463_1858465837}

[**[undo shdsl wire]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1445470841}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943522910}

[[EFM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_x504158214}[接口的连线模式为]{style="font-family:宋体"}**[4-enhanced]{lang="EN-US"}**[（四线增强模式）。]{style="font-family:宋体"}

[[EFM SHDSL 4WIRE_BIS]{lang="EN-US"}]{#struct_0_x1622_x8463_x528706123}[接口的连线模式为]{style="font-family:宋体"}**[4-standard]{lang="EN-US"}**[（四线标准模式）。]{style="font-family:宋体"}

[[EFM SHDSL_8WIRE_BIS]{lang="EN-US"}]{#struct_0_x1622_x8463_1254168642}[接口的连线模式为]{style="font-family:宋体"}**[8]{lang="EN-US"}**[（八线模式）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1320798670}

[[EFM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_x1622_x8463_x1992632226}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x66007113}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x1036086019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_x943457374}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1037027916}

[**[2]{lang="EN-US"}**]{#struct_0_x1622_x8463_1653585737}[：两线模式。]{style="font-family:宋体"}

[**[4-auto-enhanced]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1922179737}[：四线自动模式，系统首先以]{style="font-family:宋体"}**[4-enhanced]{lang="EN-US"}**[模式进行协商，如果检测到对端是]{style="font-family:宋体"}**[4-standard]{lang="EN-US"}**[模式，则本端自动切换成]{style="font-family:宋体"}**[4-standard]{lang="EN-US"}**[模式进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[4-enhanced]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1370761685}[：四线增强模式，四线中的一个线对先与对端协商，协商成功后，另一个线对再与对端进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[4-standard]{lang="EN-US"}**]{#struct_0_x1622_x8463_x2103389540}[：四线标准模式，四线的两个线对必须同时开始进行协商，要求对端也为四线标准模式。]{style="font-family:宋体"}

[**[6]{lang="EN-US"}**]{#struct_0_x1622_x8463_x422910294}[：六线模式。]{style="font-family:宋体"}

[**[8]{lang="EN-US"}**]{#struct_0_x1622_x8463_x464911930}[：八线模式。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1901160893}[：自动模式，本端根据对端接口连线模式进行协商，最终协商的连线模式与对端配置一致。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943391838}

[[配置]{style="font-family:宋体"}]{#struct_0_x1622_x8463_1445692811}**[shdsl wire]{lang="EN-US"}**[命令时，需要根据对端接口的配置选择正确连线模式。在无法确定对端接口连线模式的情况下，本端接口可以配置为]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[自动模式与对端进行协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_1507547741}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_961380627}[配置四线]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[工作在四线自动模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x2135552783}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\]]{lang="SV"}[ ]{lang="SV"}[shdsl wire 4-auto-enhanced]{lang="EN-US"}
:::

::::: {#-1726874890 .myid}
[]{#_Toc404784039}[]{#struct_0_x1622_x8463_1234262622}[]{#_Toc345510478}[]{#_Toc263323280}[]{#_Toc252280809}

**ATM接口 \-- EFM接口配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM接口命令.files/image004.jpg){#图片 8 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1622_x8463_x1885274479}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x943326302}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[开启本功能后可能需要耗费大量系统资源，请谨慎使用。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1622_x8463_x1682614965}
:::

[ ]{lang="EN-US"}

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x1622_x8463_84515572}[命令用来开启]{style="font-family:宋体"}[EFM]{lang="EN-US"}[子接口的速率统计功能。]{style="font-family:宋体"}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x1622_x8463_x972888613}[命令用来关闭]{style="font-family:宋体"}[EFM]{lang="EN-US"}[子接口的速率统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x256352726}

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x1622_x8463_x1128724236}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x1622_x8463_x408899960}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1085666473}

[[EFM]{lang="EN-US"}]{#struct_0_x1622_x8463_x458272611}[子接口的速率统计功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x943260766}

[[EFM G.SHDSL]{lang="EN-US"}]{#struct_0_x1622_x8463_x1732898650}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_4WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM SHDSL_8WIRE_BIS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_x1251561067}

[[network-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_1858718308}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1622_x8463_115198344}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1622_x8463_386254365}

[[\# ]{lang="EN-US"}]{#struct_0_x1622_x8463_x1420318339}[开启接口]{style="font-family:宋体"}[EFM2/4/0]{lang="EN-US"}[的子接口速率统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1622_x8463_x943195230}

[\[Sysname\] interface efm 2/4/0]{lang="EN-US"}

[\[Sysname-EFM2/4/0\]]{lang="SV"}[ ]{lang="SV"}[sub-interface rate-statistic]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
