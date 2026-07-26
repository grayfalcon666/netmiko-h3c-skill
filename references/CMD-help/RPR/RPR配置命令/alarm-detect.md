::::: {#1725110147 .myid}
[]{#_Toc296086815}[]{#_Toc295480285}[]{#_Toc295465879}[]{#_Toc404795716}[]{#struct_0_56601_x1470_618126410}[]{#_Toc382999905}[]{#_Toc366241761}[]{#_Toc345232201}

**RPR \-- RPR配置命令 \-- alarm-detect**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1732498409}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_679076308}
:::

**[ ]{lang="EN-US"}**

[**[alarm-detect]{lang="EN-US"}**]{#struct_0_56601_x1470_x1233068985}[命令用来配置当前接口的告警联动动作。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **alarm-detect**]{lang="EN-US"}]{#struct_0_56601_x1470_x163606498}[命令用来取消告警联动动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x592847569}

[**[alarm-detect]{lang="EN-US"}**[ { **rdi** \| **sd** \| **sf** } **action** **link-down**]{lang="EN-US"}]{#struct_0_56601_x1470_x1193632959}

[**[undo]{lang="EN-US"}**[ **alarm-detect** { **rdi** \| **sd** \| **sf** }]{lang="EN-US"}]{#struct_0_56601_x1470_x566303262}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1105428787}

[[接口不执行任何告警联动动作。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1683479935}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_718462113}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x1186672286}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1814422905}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1988782877}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x215052830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x767498108}

[**[rdi]{lang="EN-US"}**]{#struct_0_56601_x1470_1167424619}[：表示]{style="font-family:宋体"}[RDI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Defect Indication]{lang="EN-US"}[，远端失效指示）告警。]{style="font-family:宋体"}

[**[sd]{lang="EN-US"}**]{#struct_0_56601_x1470_1167599027}[：表示]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_56601_x1470_x1729690439}[：表示]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_56601_x1470_x489954597}[：配置当接口检测到告警时的联动动作。]{style="font-family:宋体"}

[**[link-down]{lang="EN-US"}**]{#struct_0_56601_x1470_x1157425212}[：表示自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x235080402}

[[当设备收到对端发送的]{style="font-family:宋体"}[MS-RDI]{lang="EN-US"}]{#struct_0_56601_x1470_x1894456913}[信号时，则认为发生了]{style="font-family:宋体"}[RDI]{lang="EN-US"}[告警。当设备收到的报文的误码率超过配置的门限时，则生成]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警或]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警的门限可通过]{style="font-family:宋体"}**[threshold]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[配置本命令后，当设备检测到告警时，会自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_56601_x1470_x1766844818}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_207603481}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1505819379}[配置当接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[检测到]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警时，自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1401764955}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] alarm-detect sd action link-down]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1584794118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[threshold]{lang="EN-US"}**]{#struct_0_56601_x1470_x1433389906}
:::::

::::: {#1742433432 .myid}
[]{#_Toc263323266}[]{#_Toc252280725}[]{#_Toc404795717}[]{#struct_0_56601_x1470_2056548673}[]{#_Toc382999906}[]{#_Toc284169067}

**RPR \-- RPR配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_56601_x1470_x1326405912}[命令用来配置当前接口的期望带宽。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bandwidth**]{lang="EN-US"}]{#struct_0_56601_x1470_775987043}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_958336145}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_56601_x1470_1773734458}

[**[undo]{lang="EN-US"}**[ **bandwidth**]{lang="EN-US"}]{#struct_0_56601_x1470_x889518324}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1911775247}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_56601_x1470_x1787570609}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x851591435}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1996784178}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/RPRGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRXGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 2 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x815494377}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1328569074}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1901145082}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1402477443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1728872141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x233104769}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_56601_x1470_1397690270}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x151299996}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_56601_x1470_x1200872933}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x595241338}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x540036890}[配置二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[10000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1449531610}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] bandwidth 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1164920881}[配置三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[10000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_699701056}

[\[Sysname\] interface rpr--router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] bandwidth 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_2083404582}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRGE2/2/0]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[10000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x482918951}

[\[Sysname\] interface rprge 2/2/0]{lang="EN-US"}

[\[Sysname-RPRGE2/2/0\] bandwidth 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1852792716}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE2/3/0]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[10000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x19958034}

[\[Sysname\] interface rprxge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRXGE2/3/0\] bandwidth 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x983357942}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[10000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x116552331}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] bandwidth 10000]{lang="EN-US"}
:::::

::::: {#424787513 .myid}
[]{#_Toc404795718}[]{#struct_0_56601_x1470_x1399789241}[]{#_Toc382999907}

**RPR \-- RPR配置命令 \-- clock**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1290787622}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_390660869}
:::

[ ]{lang="EN-US"}

[**[clock]{lang="EN-US"}**]{#struct_0_56601_x1470_2049949817}[命令用来配置当前接口的时钟模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **clock**]{lang="EN-US"}]{#struct_0_56601_x1470_1385713534}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1333656967}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_56601_x1470_1040394496}

[**[undo]{lang="EN-US"}**[ **clock**]{lang="EN-US"}]{#struct_0_56601_x1470_75133318}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1429635078}

[[接口的时钟模式为从时钟模式。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1805827506}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x711622477}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x1027085909}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_348046628}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1790027614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1286795276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1927890014}

[**[master]{lang="EN-US"}**]{#struct_0_56601_x1470_1064841943}[：表示主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_56601_x1470_x1622489245}[：表示从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x660215798}

[[与同步串口有]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_56601_x1470_239743565}[和]{style="font-family:宋体"}[DCE]{lang="EN-US"}[两种工作方式相仿，]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[也需要选择时钟模式。当两台设备的]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口直接相连时，应配置一端使用主时钟模式，另一端使用从时钟模式；当与]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[设备相连时，由于]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[网络的时钟精度高于]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[本身内部时钟源的精度，应配置]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口使用从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1307334018}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1859207146}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1386089190}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] clock master]{lang="EN-US"}
:::::

::::: {#538040344 .myid}
[]{#_Toc404795719}[]{#struct_0_56601_x1470_x84430819}[]{#_Toc382999908}

**RPR \-- RPR配置命令 \-- crc**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1676036658}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x410789523}
:::

**[ ]{lang="EN-US"}**

[**[crc]{lang="EN-US"}**]{#struct_0_56601_x1470_x349437185}[命令用来配置当前接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **crc**]{lang="EN-US"}]{#struct_0_56601_x1470_1908591183}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_643028092}

[**[crc]{lang="EN-US"}**[ { **16** \| **32** }]{lang="EN-US"}]{#struct_0_56601_x1470_979564370}

[**[undo]{lang="EN-US"}**[ **crc**]{lang="EN-US"}]{#struct_0_56601_x1470_x1100801983}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1115500966}

[[接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_56601_x1470_x1999567748}[校验字长度为]{style="font-family:宋体"}[32]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_504907684}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x897681620}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1536930250}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1164579830}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x234020117}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x923055849}

[**[16]{lang="EN-US"}**]{#struct_0_56601_x1470_x621501793}[：表示]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_56601_x1470_x464030246}[：表示]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度为]{style="font-family:宋体"}[32]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1531436964}

[[需要注意的是，两端设备接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_56601_x1470_x733347725}[校验字长度应保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x671382402}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_641985395}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x2034857260}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] crc 16]{lang="EN-US"}
:::::

::::: {#1245918683 .myid}
[]{#_Toc353527897}[]{#_Toc404795720}[]{#struct_0_56601_x1470_2028531004}[]{#_Toc382999909}[]{#_Toc359918310}[]{#_Toc355619426}

**RPR \-- RPR配置命令 \-- dampening**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x163540962}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x132243161}
:::

[ ]{lang="EN-US"}

[**[dampening]{lang="EN-US"}**]{#struct_0_56601_x1470_1298159238}[命令用来开启当前接口的]{style="font-family:宋体"}[Dampening]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dampening**]{lang="EN-US"}]{#struct_0_56601_x1470_1093811994}[命令用来关闭当前接口的]{style="font-family:宋体"}[Dampening]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_2060313361}

[**[dampening]{lang="EN-US"}**[ \[ *half-life* *reuse* *suppress* *max-suppress-time* \]]{lang="EN-US"}]{#struct_0_56601_x1470_158639223}

[**[undo]{lang="EN-US"}**[ **dampening**]{lang="EN-US"}]{#struct_0_56601_x1470_1513786971}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1413681678}

[[接口的]{style="font-family:宋体"}[Dampening]{lang="EN-US"}]{#struct_0_56601_x1470_1899584116}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1729624903}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x418484455}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x883514100}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x745662665}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x463787941}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1699500448}

[*[half-life]{lang="EN-US"}*]{#struct_0_56601_x1470_10835973}[：表示]{style="font-family:宋体"}[半衰期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，]{style="font-family:宋体"}[单位为秒，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[54]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[*[reuse]{lang="EN-US"}*]{#struct_0_56601_x1470_x466631293}[：表示]{style="font-family:宋体"}[启用门限，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[750]{lang="EN-US"}[，]{style="font-family:宋体"}*[reuse]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[suppress]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[*[suppress]{lang="EN-US"}*]{#struct_0_56601_x1470_x2064738776}[：表示抑制门限，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[max-suppress-time]{lang="EN-US"}*]{#struct_0_56601_x1470_x1326340376}[：表示]{style="font-family:宋体"}[最大抑制时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒，缺省值为半衰期的]{style="font-family:宋体"}[3]{lang="EN-US"}[倍，即]{style="font-family:宋体"}[162]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1380012799}

[[接口有两种物理连接状态：]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_56601_x1470_x1138752513}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[。由于线缆故障、接口连接或链路层配置错误等问题，可能会导致设备接口的状态频繁的在]{style="font-family:宋体"}[down]{lang="EN-US"}[和]{style="font-family:宋体"}[up]{lang="EN-US"}[之间切换，这种现象称为接口震荡。随着接口状态的频繁改变，设备会不停的刷新相关表项（比如路由表），消耗大量的系统资源。通过在接口上配置]{style="font-family:宋体"}[Dampening]{lang="EN-US"}[功能，可以在一定条件下，屏蔽该接口的震荡对路由等上层业务的影响。此时若出现接口震荡，将不上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}[处理，仅产生对应的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息，从而节省系统资源的消耗。]{style="font-family:宋体"}

[[Dampening]{lang="EN-US"}]{#struct_0_56601_x1470_1166629625}[功能的工作原理如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1570036917}[Dampening]{lang="EN-US"}[功能后，接口将关联一个惩罚值，初始值是]{style="font-family:宋体"}[0]{lang="EN-US"}[。接口状态每次从]{style="font-family:宋体"}[up]{lang="EN-US"}[变到]{style="font-family:宋体"}[down]{lang="EN-US"}[时，惩罚值会增加]{style="font-family:宋体"}[1000]{lang="EN-US"}[（接口状态从]{style="font-family:宋体"}[down]{lang="EN-US"}[变到]{style="font-family:宋体"}[up]{lang="EN-US"}[时，惩罚值不变）。同时，惩罚值随着时间的推移自动减少，满足半衰期衰减规律]{style="font-family:宋体"}[：完全衰减时（即假如在此期间没有再发生接口震荡），经过一个半衰期，]{style="font-family:宋体"}[惩罚值将]{style="font-family:宋体"}[减少为原来值的一半]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_56601_x1470_x772638892}[惩罚值大于或等于抑制门限时，开始抑制接口：不上送]{style="font-family:
宋体"}[CPU]{lang="DA"}[处理接口状态变化，仅产生对应的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息]{style="font-family:宋体"}[。当]{style="font-family:宋体"}[惩罚值小于或等于启用门限时，不抑制接口：上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}[处理接口状态变化，同时发送对应的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当惩罚值达到最大惩罚值后，惩罚值将不再增加。最大惩罚值不可配，其值与最大抑制时间、半衰期、启用门限之间的关系遵循如下公式：最大惩罚值＝]{style="font-family:宋体"}]{#struct_0_56601_x1470_1940151793}[2^(^]{lang="EN-US"}^[最大抑制时间]{style="font-family:宋体"}[/]{lang="EN-US"}[半衰期]{style="font-family:宋体"}[)]{lang="EN-US"}^[×启用值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每次接口进入抑制状态后，当接口持续抑制的时间超过最大抑制时间时，且此时惩罚值大于启用门限时，惩罚值将不再增加，此时惩罚值进入完全半衰期（此阶段接口状态变化不会增加惩罚值），直到惩罚值小于启用门限，不再抑制接口（完全半衰期中，接口仍然处于抑制状态，但完全半衰阶段时间不算入持续抑制时间）。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1203324853}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口抑制时间不到最大抑制时间，惩罚值就小于启用门限，那么不存在完全半衰过程（持续抑制时间超过最大抑制时间才会进入）。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1402542979}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x908576244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_56601_x1470_1921636989}[命令和]{lang="EN-US" style="font-family:宋体"}**[link-delay]{lang="EN-US"}**[命令不能同时使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令对使用]{style="font-family:宋体"}]{#struct_0_56601_x1470_x487110032}**[shutdown]{lang="EN-US"}**[命令手工关闭的接口无效。接口被关闭时，惩罚值恢复为初始值]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[处于抑制期时产生的接口]{style="font-family:宋体"}]{#struct_0_56601_x1470_x986233754}[up]{lang="EN-US"}[事件，通过]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}[命令、]{style="font-family:宋体"}[MIB]{lang="EN-US"}[网管或]{style="font-family:宋体"}[Web]{lang="EN-US"}[网管等方式查看到时，接口状态仍然为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x433795160}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1875010643}[开启]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[Dampening]{lang="EN-US"}[功能，配置半衰期为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，启用门限为]{style="font-family:宋体"}[800]{lang="EN-US"}[，抑制门限为]{style="font-family:宋体"}[3000]{lang="EN-US"}[，最大抑制时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1026943709}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] dampening 2 800 3000 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_85697871}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_56601_x1470_x41323246}[ **interface**]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[link-delay]{lang="EN-US"}**]{#struct_0_56601_x1470_1121380543}
:::::

::::: {#1948332219 .myid}
[]{#_Toc404795721}[]{#struct_0_56601_x1470_1449597146}[]{#_Toc382999910}

**RPR \-- RPR配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_56601_x1470_1967717416}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1640661929}

[**[default]{lang="EN-US"}**]{#struct_0_56601_x1470_2012264492}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1720595753}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1618521211}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/RPRGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRXGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1056348522}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x2009511383}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x478193385}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x116486795}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1688583130}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1726807500}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2116889707}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_56601_x1470_x831545278}[命令后通过]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **this**]{lang="EN-US"}[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1371380592}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1517499683}[将二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1690553115}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] default]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x2126984162}[将三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1805630898}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] default]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x257219665}[将]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRGE2/2/0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1882906082}

[\[Sysname\] interface rprge 2/2/0]{lang="EN-US"}

[\[Sysname-RPRGE2/2/0\] default]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1065941553}[将]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE2/3/0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x362561947}

[\[Sysname\] interface rprxge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRXGE2/3/0\] default]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_2065536452}[将]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x121240813}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] default]{lang="EN-US"}
:::::

::::: {#-1461383778 .myid}
[]{#_Toc404795722}[]{#struct_0_56601_x1470_x1791622987}[]{#_Toc382999911}

**RPR \-- RPR配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_56601_x1470_x395076683}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_56601_x1470_x2002317713}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_239546957}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_56601_x1470_x378129604}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_56601_x1470_1018685577}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x981572947}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_56601_x1470_x1953014887}["，比如二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[的缺省描述信息为"]{style="font-family:宋体"}[RPR-Bridge1 Interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1685464150}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1394914986}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/RPRGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRXGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1906960114}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1335528167}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_642831484}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x509066416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1555683764}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_205965047}

[*[text]{lang="EN-US"}*]{#struct_0_56601_x1470_1604982997}[：表示接口的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x815384173}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1717394257}[配置二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[RPR-Bridge-1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_710092541}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] description RPR-Bridge-1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x759213483}[配置三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[RPR-Router-1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x923252457}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] description RPR-Router-1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1862538777}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRGE2/2/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[RPRGE-1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_208602273}

[\[Sysname\] interface rprge 2/2/0]{lang="EN-US"}

[\[Sysname-RPRGE2/2/0\] description RPRGE-1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_832537022}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE2/3/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[RPRXGE-1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_520637896}

[\[Sysname\] interface rprxge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRXGE2/3/0\] description RPRXGE-1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1275377639}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[RPRPOS-1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1306887116}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] description RPRPOS-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1964403647}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x163737570}
:::::

::: {#186680629 .myid}
[]{#_Toc133657440}[]{#_Toc404795723}[]{#struct_0_56601_x1470_x204123741}

**RPR \-- RPR配置命令 \-- display interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x156271552}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1151040839}

[**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}[ \[ { **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_56601_x1470_x769317614}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1688883518}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_1802961359}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1361221475}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_998754474}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x1578735777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1729821511}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_61954115}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x79441044}

[**[rpr-bridge]{lang="EN-US"}**]{#struct_0_56601_x1470_x325310936}[：显示二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rpr-router]{lang="EN-US"}**]{#struct_0_56601_x1470_559481082}[：显示三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprge]{lang="EN-US"}**]{#struct_0_56601_x1470_1818379842}[：显示]{style="font-family:宋体"}[RPRGE]{lang="EN-US"}[接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprpos]{lang="EN-US"}**]{#struct_0_56601_x1470_1807431041}[：显示]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprxge]{lang="EN-US"}**]{#struct_0_56601_x1470_x26634243}[：显示]{style="font-family:宋体"}[RPRXGE]{lang="EN-US"}[接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_56601_x1470_1183844892}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_56601_x1470_x656717603}[：显示概要信息。如果未指定本参数，将显示详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_56601_x1470_x208420242}[：当用户配置的接口描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不会显示。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_56601_x1470_x1326536984}[：显示当前状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果未指定本参数，将不会根据接口接口状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_212711252}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1396043726}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定接口类型，将显示设备支持的所有接口的信息。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1640803589}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了接口类型而未指定接口编号，将显示所有已创建的指定类型接口的信息。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1602211386}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_446601406}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1450053935}[显示二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface rpr-bridge 1]{lang="EN-US"}]{#struct_0_56601_x1470_1127401281}

[RPR-Bridge1]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Description: RPR-Bridge1 Interface]{lang="EN-US"}

[Bandwidth: 0kbps]{lang="EN-US"}

[IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 34b9-854b-0102]{lang="EN-US"}

[Unknown-speed mode, full-duplex mode]{lang="EN-US"}

[Link speed type is autonegotiation, link duplex type is force link]{lang="EN-US"}

[PVID: 1]{lang="EN-US"}

[Port link-type: access]{lang="EN-US"}

[ Tagged Vlan:   none]{lang="EN-US"}

[ UnTagged Vlan: 1]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1402346371}[显示三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface rpr-router 1]{lang="EN-US"}]{#struct_0_56601_x1470_x965735102}

[RPR-Router1]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: RPR-Router1 Interface]{lang="EN-US"}

[Bandwidth: 0kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing : disabled]{lang="EN-US"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 34b9-854b-0102]{lang="EN-US"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 34b9-854b-0102]{lang="EN-US"}

[Last clearing of counters:  Never]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1360107410}[显示二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface rpr-bridge 1 brief]{lang="EN-US"}]{#struct_0_56601_x1470_1498950039}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Speed or Duplex: (a)/A - auto; H - half; F - full]{lang="EN-US"}

[Type: A - access; T - trunk; H - hybrid]{lang="EN-US"}

[Interface            Link Speed   Duplex Type PVID Description]{lang="EN-US"}

[RPR-B1               DOWN auto    A      A    1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_139876229}[显示三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface rpr-router 1 brief]{lang="EN-US"}]{#struct_0_56601_x1470_1449400538}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[RPR-R1               DOWN DOWN     \--]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface]{lang="EN-US"}]{#struct_0_56601_x1470_1982022483}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1473932874}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_639274548}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_2065537002}

[[Current state]{lang="EN-US"}]{#struct_0_56601_x1470_1842968491}

[[接口当前的物理状态和管理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x766253168}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_56601_x1470_694845036}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_56601_x1470_x1769331245}[：表示该接口的物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_56601_x1470_x116683403}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_56601_x1470_x1792314098}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x207860581}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_56601_x1470_2086400494}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_56601_x1470_x717919378}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_56601_x1470_903349051}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_56601_x1470_x64277954}

[[Bandwidth]{lang="EN-US"}]{#struct_0_56601_x1470_x894424345}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_56601_x1470_1805696434}

[[Unknown-speed mode, unknown-duplex mode]{lang="EN-US"}]{#struct_0_56601_x1470_x1074524965}

[[接口速率未知，双工模式未知]{style="font-family:宋体"}]{#struct_0_56601_x1470_101819758}

[[Link speed type is autonegotiation]{lang="EN-US"}]{#struct_0_56601_x1470_x2145420903}

[[接口速率通过自协商确定]{style="font-family:宋体"}]{#struct_0_56601_x1470_131134707}

[[link duplex type is autonegotiation]{lang="EN-US"}]{#struct_0_56601_x1470_x370574878}

[[链路双工类型通过自协商确定]{style="font-family:宋体"}]{#struct_0_56601_x1470_352703695}

[[PVID]{lang="EN-US"}]{#struct_0_56601_x1470_239612493}

[[接口的缺省]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1698947532}[VLAN ID]{lang="SV"}

[[Port link-type]{lang="EN-US"}]{#struct_0_56601_x1470_x511049238}

[[接口链路类型（有]{style="font-family:宋体"}[access]{lang="EN-US"}]{#struct_0_56601_x1470_x934936072}[、]{style="font-family:宋体"}[trunk]{lang="EN-US"}[和]{style="font-family:宋体"}[hybrid]{lang="EN-US"}[三种类型）]{style="font-family:宋体"}

[[Tagged Vlan]{lang="EN-US"}]{#struct_0_56601_x1470_140835261}

[[标识在该端口有哪些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_56601_x1470_x1731642664}[的报文需要打]{style="font-family:宋体"}[Tag]{lang="EN-US"}[标记]{style="font-family:宋体"}

[[UnTagged Vlan]{lang="EN-US"}]{#struct_0_56601_x1470_642897020}

[[标识在该端口有哪些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_56601_x1470_x90827006}[的报文不需要打]{style="font-family:宋体"}[Tag]{lang="EN-US"}[标记]{style="font-family:宋体"}

[[VLAN Passing]{lang="EN-US"}]{#struct_0_56601_x1470_1138290874}

[[Trunk]{lang="EN-US"}]{#struct_0_56601_x1470_x1121184418}[口实际可以通过的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[已经创建，并且接口允许其通过）]{style="font-family:宋体"}

[[VLAN permitted]{lang="EN-US"}]{#struct_0_56601_x1470_x923186921}

[[Trunk]{lang="EN-US"}]{#struct_0_56601_x1470_x208791651}[口允许通过的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不一定存在，可能没有创建）]{style="font-family:宋体"}

[[Trunk port encapsulation]{lang="EN-US"}]{#struct_0_56601_x1470_x2019138019}

[[Trunk]{lang="EN-US"}]{#struct_0_56601_x1470_x1656170704}[口上封装的协议类型]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_56601_x1470_x775365316}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1786159091}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_56601_x1470_x163672034}

[[对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56601_x1470_601426617}[报文的处理能力，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，不能处理]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文。当接口下配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之后，该字段将变为"]{style="font-family:宋体"}[Internet Address is]{lang="EN-US"}["]{style="font-family:宋体"}

[[Internet Address is 192.168.2.1/24 Primary]{lang="EN-US"}]{#struct_0_56601_x1470_484429975}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_1454655629}[接口配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_56601_x1470_72932806}

[[IPv4]{lang="EN-US"}]{#struct_0_56601_x1470_44582952}[报文帧格式]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_56601_x1470_x1729755975}

[[IPv6]{lang="EN-US"}]{#struct_0_56601_x1470_x176108696}[报文帧格式]{style="font-family:宋体"}

[[Hardware Address]{lang="EN-US"}]{#struct_0_56601_x1470_1295998237}

[[接口的硬件地址]{style="font-family:宋体"}]{#struct_0_56601_x1470_201568941}

[[Last link flapping]{lang="EN-US"}]{#struct_0_56601_x1470_449653028}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_56601_x1470_x1326471448}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_56601_x1470_1402411907}

[[最后一次使用]{style="font-family:宋体"}**[reset]{lang="EN-US"}**[ **counts** **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x1321494527}[命令清除接口统计信息的时间，]{style="font-family:
  宋体"}[Never]{lang="EN-US"}[表示未清除过]{style="font-family:
  宋体"}

[[Brief information on interface(s) under bridge mode]{lang="EN-US"}]{#struct_0_56601_x1470_1449466074}

[[二层接口的概要信息]{style="font-family:宋体"}]{#struct_0_56601_x1470_1601013677}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_56601_x1470_x116617867}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1749399684}

[[Dampening enabled:]{lang="EN-US"}]{#struct_0_56601_x1470_1805499826}

[[ Penalty: 0 (not suppressed)]{lang="EN-US"}]{#struct_0_56601_x1470_x1446101797}

[[ Ceiling: 4525]{lang="EN-US"}]{#struct_0_56601_x1470_x722271415}

[[ Reuse: 800]{lang="EN-US"}]{#struct_0_56601_x1470_748647761}

[[ Suppress: 3000]{lang="EN-US"}]{#struct_0_56601_x1470_239415885}

[[ Half-life: 2 seconds]{lang="EN-US"}]{#struct_0_56601_x1470_1613539054}

[[ Max-suppress-time: 5 seconds]{lang="EN-US"}]{#struct_0_56601_x1470_x988007239}

[[ Flap count: 0]{lang="EN-US"}]{#struct_0_56601_x1470_x1384144424}

[[接口的]{style="font-family:宋体"}[dampening]{lang="EN-US"}]{#struct_0_56601_x1470_1038926736}[抑制信息，该显示信息的支持情况与用户的配置以及设备型号有关，请以设备的实际情况为准（若未使能]{style="font-family:宋体"}[dampening]{lang="EN-US"}[功能，则不会显示该段信息）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dampening enabled]{lang="EN-US"}]{#struct_0_56601_x1470_642700412}[：已使能]{lang="EN-US" style="font-family:
  宋体"}[dampening]{lang="EN-US"}[功能]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Penalty]{lang="EN-US"}]{#struct_0_56601_x1470_101663729}[：惩罚值]{lang="EN-US" style="font-family:宋体"}[（若接口处于抑制期，则在惩罚值后标识]{style="font-family:宋体"}[suppressed]{lang="EN-US"}[；反之，在惩罚值后标识]{style="font-family:宋体"}[not suppressed]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ceiling]{lang="EN-US"}]{#struct_0_56601_x1470_372799877}[：最大惩罚值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reuse]{lang="EN-US"}]{#struct_0_56601_x1470_1299107623}[：启用门限]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Suppress]{lang="EN-US"}]{#struct_0_56601_x1470_x887894745}[：抑制门限]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Half-life]{lang="EN-US"}]{#struct_0_56601_x1470_x1340008490}[：半衰期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max-suppress-time]{lang="EN-US"}]{#struct_0_56601_x1470_x923383529}[：最大抑制时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Flap count]{lang="EN-US"}]{#struct_0_56601_x1470_x1450746166}[：]{lang="EN-US" style="font-family:宋体"}[接口震荡]{style="font-family:宋体"}[发生的次数]{lang="EN-US" style="font-family:宋体"}

 

[[Hold timer]{lang="EN-US"}]{#struct_0_56601_x1470_2047169575}

[[Keepalive]{lang="EN-US"}]{#struct_0_56601_x1470_445730912}[报文的发送周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_56601_x1470_x163868642}

[[在多少个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}]{#struct_0_56601_x1470_x528515860}[报文发送周期内未收到应答就拆除链路]{style="font-family:宋体"}

[[Internet Address]{lang="EN-US"}]{#struct_0_56601_x1470_2004657005}

[[接口的网络地址]{style="font-family:宋体"}]{#struct_0_56601_x1470_x423529092}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_56601_x1470_x1275520331}

[[接口的链路层封装的协议]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1729952583}

[[LCP: opened, IPCP: opened]{lang="EN-US"}]{#struct_0_56601_x1470_305247378}

[[表示]{style="font-family:宋体"}[LCP]{lang="EN-US"}]{#struct_0_56601_x1470_x1487683782}[和]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[都协商成功]{style="font-family:宋体"}

[[Physical layer]{lang="EN-US"}]{#struct_0_56601_x1470_1605017423}

[[物理接口]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1326668056}

[[Baudrate]{lang="EN-US"}]{#struct_0_56601_x1470_1376119438}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1963910284}

[[Scramble]{lang="EN-US"}]{#struct_0_56601_x1470_776706283}

[[接口是否开启对载荷数据的加扰功能]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2062015622}

[[crc]{lang="EN-US"}]{#struct_0_56601_x1470_1402215299}

[[接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_56601_x1470_576219946}[校验字长度]{style="font-family:宋体"}

[[clock]{lang="EN-US"}]{#struct_0_56601_x1470_x142667159}

[[接口的时钟模式]{style="font-family:宋体"}]{#struct_0_56601_x1470_522242700}

[[loopback]{lang="EN-US"}]{#struct_0_56601_x1470_1449269466}

[[接口是否开启环回功能]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1179951731}

[[SONET alarm]{lang="EN-US"}]{#struct_0_56601_x1470_x52572299}

[[SONET]{lang="EN-US"}]{#struct_0_56601_x1470_1587473079}[告警信息]{style="font-family:宋体"}

[[SONET error]{lang="EN-US"}]{#struct_0_56601_x1470_x116814475}

[[SONET]{lang="EN-US"}]{#struct_0_56601_x1470_141206922}[错误信息]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_56601_x1470_x1248316060}

[[最近一次清除计数的时间]{style="font-family:宋体"}]{#struct_0_56601_x1470_1824840840}

[[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_56601_x1470_x1332661540}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_56601_x1470_1805565362}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_56601_x1470_62024264}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_56601_x1470_x286196614}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input: ]{lang="EN-US"}]{#struct_0_56601_x1470_239481421}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_56601_x1470_1138761105}

[[  0 errors, 0 runts, 0 giants, 0 CRC]{lang="EN-US"}]{#struct_0_56601_x1470_1273602079}

[[  0 overruns, 0 aborts, 0 no buffers]{lang="EN-US"}]{#struct_0_56601_x1470_1982799348}

[[接口收到的总报文数和总字节数：]{style="font-family:宋体"}]{#struct_0_56601_x1470_642765948}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_56601_x1470_x1492767072}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[runts]{lang="EN-US"}]{#struct_0_56601_x1470_1639817797}[：接口接收到小于规定的最小报文长度报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_56601_x1470_x86657462}[：接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CRC]{lang="EN-US"}]{#struct_0_56601_x1470_x923317993}[：接收长度正常但]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_56601_x1470_x1790145435}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_56601_x1470_1757213563}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffers]{lang="EN-US"}]{#struct_0_56601_x1470_x163803106}[：在接收报文时由于内部缓存满，导致帧丢弃]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_56601_x1470_1002733465}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_56601_x1470_517713652}

[[  0 errors, 0 underruns, 0 aborts]{lang="EN-US"}]{#struct_0_56601_x1470_x1729887047}

[[接口发送的报文数和总字节数]{style="font-family:宋体"}]{#struct_0_56601_x1470_578756418}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_56601_x1470_x1366017738}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_56601_x1470_x154884945}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_56601_x1470_x1326602520}[：发送报文的异常错误]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_56601_x1470_x1051871703}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_56601_x1470_x374159886}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_56601_x1470_1402280835}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2116410327}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_56601_x1470_x1039636383}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Speed or Duplex: (a)/A - auto; H - half; F - full]{lang="EN-US"}]{#struct_0_56601_x1470_x2011620467}

[[Speed]{lang="EN-US"}]{#struct_0_56601_x1470_1449335002}[属性值为]{style="font-family:宋体"}[(a)]{lang="EN-US"}[表示该接口的速率通过自动协商获取；]{style="font-family:宋体"}[Duplex]{lang="EN-US"}[属性值为]{style="font-family:宋体"}[(a)]{lang="EN-US"}[或]{style="font-family:宋体"}[A]{lang="EN-US"}[表示该接口的]{style="font-family:宋体"}[Duplex]{lang="EN-US"}[属性通过自动协商获取，为]{style="font-family:宋体"}[H]{lang="EN-US"}[表示半双工，为]{style="font-family:宋体"}[F]{lang="EN-US"}[则表示全双工]{style="font-family:宋体"}

[[Type: A - access; T - trunk; H - hybrid]{lang="EN-US"}]{#struct_0_56601_x1470_1186653736}

[[接口的链路类型：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x950992238}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_56601_x1470_x116748939}[：表示]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_56601_x1470_x1785432165}[：表示]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_56601_x1470_x1270105370}[：表示]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[链路类型]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_56601_x1470_x1167580927}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_56601_x1470_x1551974990}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_56601_x1470_555689870}

[[接口名称的缩写]{style="font-family:宋体"}]{#struct_0_56601_x1470_26261372}

[[Link]{lang="EN-US"}]{#struct_0_56601_x1470_1176908365}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1424781558}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_56601_x1470_1769036498}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_56601_x1470_1580192892}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_56601_x1470_x1200058861}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_56601_x1470_1670721479}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_56601_x1470_14108951}

[[接口的速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}]{#struct_0_56601_x1470_x2012654799}

[[Duplex]{lang="EN-US"}]{#struct_0_56601_x1470_541899860}

[[接口的双工模式：]{style="font-family:宋体"}]{#struct_0_56601_x1470_1065392114}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_56601_x1470_773623838}[：表示双工模式由自动协商结果决定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_56601_x1470_x585850830}[：表示全双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F(a)]{lang="EN-US"}]{#struct_0_56601_x1470_1306019184}[：表示自由协商的结果为全双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_56601_x1470_x792460103}[：表示半双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H(a)]{lang="EN-US"}]{#struct_0_56601_x1470_966862372}[：表示自由协商的结果为半双工]{lang="EN-US" style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_56601_x1470_370331392}

[[接口的链路类型：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x389175576}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_56601_x1470_1496222569}[：表示]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_56601_x1470_1472294843}[：表示]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_56601_x1470_x1955259517}[：表示]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[链路类型]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_56601_x1470_1797608953}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1198214257}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_56601_x1470_x1908205350}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_56601_x1470_x1524357541}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_56601_x1470_x547795237}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_56601_x1470_820678005}

[[接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56601_x1470_94715243}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_56601_x1470_653588635}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_56601_x1470_x1551909454}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_56601_x1470_783616794}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_56601_x1470_1176973901}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x262428549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **counters** **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x45908880}

::: {#-1312892087 .myid}
[]{#_Toc168996348}[]{#_Toc404795724}[]{#struct_0_56601_x1470_x336030083}

**RPR \-- RPR配置命令 \-- display rpr bind-info**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **bind-info**]{lang="EN-US"}]{#struct_0_56601_x1470_916382119}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口与]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口的绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x158996754}

[**[display]{lang="EN-US"}**[ **rpr** **bind-info** \[ { **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_x934660279}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_911336150}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_1585163957}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_544080570}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_196203417}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x464378307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1580258428}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_394384089}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1307493917}

[[{ **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_x962010000}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[接口的绑定信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的绑定信息。不同型号的设备支持的接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x836951968}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x146379177}[显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr bind-info]{lang="EN-US"}]{#struct_0_56601_x1470_601107047}

[Bind information on interface RPR-Bridge1:]{lang="EN-US"}

[ Smart connection: Enabled/Disconnected]{lang="EN-US"}

[ PHY interface    Ringlet ID    Role       Mate port]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ None             N/A           N/A        N/A]{lang="EN-US"}

[ None             N/A           N/A        N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Bind information on interface RPR-Router1:]{lang="EN-US"}

[ Smart connection: Enabled/Connected]{lang="EN-US"}

[ PHY interface    Ringlet ID    Role       Mate port]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ RPRPOS2/4/0      0             Primary    Up]{lang="EN-US"}

[ RPRPOS2/4/1      1             Secondary  Up]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display rpr bind-info]{lang="EN-US"}]{#struct_0_56601_x1470_763881375}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1454479394}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_14174487}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1194419652}

[[Bind information on interface]{lang="EN-US"}]{#struct_0_56601_x1470_2012524335}

[[[RPR]{lang="EN-US"}]{.ItemListinTableCharChar}]{#struct_0_56601_x1470_1773783856}[[逻辑接口的绑定信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Smart connection]{lang="EN-US"}]{#struct_0_56601_x1470_1542039867}

[[MATE]{lang="EN-US"}]{#struct_0_56601_x1470_215702862}[[口的智能连接功能是否使能以及]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}[MATE]{lang="EN-US"}[[口的连接情况：]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled/Connected]{lang="EN-US"}]{#struct_0_56601_x1470_781827434}[：表示智能连接功能处于使能状态，]{lang="EN-US" style="font-family:
  宋体"}[MATE]{lang="EN-US"}[口已在内部自动连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled/Disconnected]{lang="EN-US"}]{#struct_0_56601_x1470_x1660305971}[：表示智能连接功能处于使能状态，但]{lang="EN-US" style="font-family:
  宋体"}[MATE]{lang="EN-US"}[口在内部并未自动连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_56601_x1470_x1329548546}[：表示智能连接功能处于关闭状态]{lang="EN-US" style="font-family:宋体"}

[[PHY interface]{lang="EN-US"}]{#struct_0_56601_x1470_773689374}

[[绑定到]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1721863877}[逻辑接口的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}

[[Ringlet ID]{lang="EN-US"}]{#struct_0_56601_x1470_372251288}

[[[RPR]{lang="EN-US"}]{.ItemListinTableCharChar}]{#struct_0_56601_x1470_x1569843984}[[物理接口绑定到]{style="font-family:宋体"}]{.ItemListinTableCharChar}[RPR]{lang="EN-US"}[[逻辑接口上的绑定方向：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x463583413}[：表示]{style="font-family:宋体"}[[RPR]{lang="EN-US"}]{.ItemListinTableCharChar}[物理接口绑定为]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的西向接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x288522505}[：表示]{style="font-family:宋体"}[[RPR]{lang="EN-US"}]{.ItemListinTableCharChar}[物理接口绑定为]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的东向接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_56601_x1470_x611820651}[：表示没有绑定]{lang="EN-US" style="font-family:宋体"}

[[Role]{lang="EN-US"}]{#struct_0_56601_x1470_736219933}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x792394567}[物理接口的角色：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_56601_x1470_x1736837047}[：表示该]{lang="EN-US" style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口为主接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Secondary]{lang="EN-US"}]{#struct_0_56601_x1470_829990012}[：表示该]{lang="EN-US" style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口为从接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_56601_x1470_x1281330337}[：表示没有绑定]{lang="EN-US" style="font-family:宋体"}

[[Mate port]{lang="EN-US"}]{#struct_0_56601_x1470_x84653753}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1761490393}[[物理接口对应]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MATE]{lang="EN-US"}[[口的状态：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_56601_x1470_403014693}[：表示]{style="font-family:宋体"}[MATE]{lang="EN-US"}[口处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_56601_x1470_110892674}[：表示]{lang="EN-US" style="font-family:宋体"}[MATE]{lang="EN-US"}[口处于]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_56601_x1470_x389110040}[：表示没有绑定]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#630371087 .myid}
[]{#_Toc404795725}[]{#struct_0_56601_x1470_x459651997}[]{#_Toc168996350}[]{#_Toc168970015}[]{#_Toc168996349}

**RPR \-- RPR配置命令 \-- display rpr defect**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **defect**]{lang="EN-US"}]{#struct_0_56601_x1470_x1437827529}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[的缺陷信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_567991398}

[**[display]{lang="EN-US"}**[ **rpr** **defect** \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_x707618930}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x55536006}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_1027994177}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_370892880}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_2096086840}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x562743962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1955193981}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x1891458973}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1188828637}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_1701433747}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的缺陷信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的缺陷信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1564692794}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x89336093}[显示三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的缺陷信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr defect rpr-router 1]{lang="EN-US"}]{#struct_0_56601_x1470_x1908139814}

[RPR defects on interface RPR-Router1:]{lang="EN-US"}

[  Reserved rate exceeded                            : Ringlet0]{lang="EN-US"}[：]{style="font-family:宋体"}[0; Ringlet1: 0]{lang="EN-US"}

[  Jumbo configuration defect                        : 0]{lang="EN-US"}

[  Maximum number of stations exceeded               : 0]{lang="EN-US"}

[  Miscabling                                        : Ringlet0: 0; Ringlet1: 0]{lang="EN-US"}

[  Protection mode configuration defect              : 0]{lang="EN-US"}

[  Inconsistent topology                             : 0]{lang="EN-US"}

[  Unstable topology                                 : 0]{lang="EN-US"}

[  Invalid topology entry                            : 0]{lang="EN-US"}

[  Duplicate IP address                              : 0]{lang="EN-US"}

[  Duplicate secondary MAC address                   : 0]{lang="EN-US"}

[  Maximum number of secondary MAC addresses exceeded: 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display rpr defect]{lang="EN-US"}]{#struct_0_56601_x1470_x1100105187}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1452925104}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_x664641726}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_x121137634}

[[RPR defects on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_928418873}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_450949250}[[接口对应站点所在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[RPR]{lang="EN-US"}[[环的缺陷信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Reserved rate exceeded]{lang="EN-US"}]{#struct_0_56601_x1470_1150953012}

[[[超过预留带宽缺陷，分别对]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_372491802}[[环和]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[环说明：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Jumbo configuration defect]{lang="EN-US"}]{#struct_0_56601_x1470_x579285204}

[[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_1556897709}[[帧配置缺陷：]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}[[表示没有缺陷，]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Maximum number of stations exceeded]{lang="EN-US"}]{#struct_0_56601_x1470_820743541}

[[[超过最大站点数限制缺陷：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_897352727}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Miscabling]{lang="EN-US"}]{#struct_0_56601_x1470_1633654095}

[[[光纤错接缺陷，分别对]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x1218887051}[[环和]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[环说明：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Protection mode configuration defect]{lang="EN-US"}]{#struct_0_56601_x1470_x183863030}

[[[保护倒换模式配置缺陷：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_117559508}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Inconsistent topology]{lang="EN-US"}]{#struct_0_56601_x1470_595431997}

[[[拓扑不一致缺陷：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x547273612}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Unstable topology]{lang="EN-US"}]{#struct_0_56601_x1470_x1552106062}

[[[拓扑不稳定缺陷：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x400666787}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Invalid topology entry]{lang="EN-US"}]{#struct_0_56601_x1470_1528158946}

[[拓扑实体无效缺陷：]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_10344604}[表示没有缺陷，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示存在缺陷]{style="font-family:宋体"}

[[Duplicate IP address]{lang="EN-US"}]{#struct_0_56601_x1470_1373570394}

[[IP]{lang="EN-US"}]{#struct_0_56601_x1470_x2111949715}[地址重复缺陷：]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有缺陷，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示存在缺陷]{style="font-family:宋体"}

[[Duplicate secondary MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_1250168217}

[[[次级]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_20236747}[[地址重复缺陷：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[[0]{lang="EN-US"}]{.ItemListinTableCharChar}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[[1]{lang="EN-US"}]{.ItemListinTableCharChar}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Maximum number of secondary MAC addresses exceeded]{lang="EN-US"}]{#struct_0_56601_x1470_1176777293}

[[超过最大次级]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_1636072358}[地址数]{style="font-family:宋体"}[[缺陷：]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}[[表示没有缺陷，]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}[[表示存在缺陷]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[ ]{lang="EN-US"}

::::: {#1629099320 .myid}
[]{#_Toc404795726}[]{#struct_0_56601_x1470_450559573}[]{#_Toc168996351}

**RPR \-- RPR配置命令 \-- display rpr fairness**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **fairness**]{lang="EN-US"}]{#struct_0_56601_x1470_x175876589}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[的公平性参数信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1369456979}

[**[display]{lang="EN-US"}**[ **rpr** **fairness** \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_x318880967}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1580061820}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1568936946}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x939129807}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_2108232269}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x901566997}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_2110118530}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x1822384872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1061275119}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_2092997396}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的公平性参数信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的公平性参数信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_420986741}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_321809233}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[已绑定两个]{style="font-family:宋体"}[2.5GPOS]{lang="EN-US"}[物理接口，显示该接口的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[公平性参数信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr fairness rpr-router 1]{lang="EN-US"}]{#struct_0_56601_x1470_13977879}

[RPR fairness parameters on interface RPR-Router1:]{lang="EN-US"}

[  Fairness weight on Ringlet0: 1]{lang="EN-US"}

[  Fairness weight on Ringlet1: 1]{lang="EN-US"}

[  Local reserved bandwidth for class A0 service on Ringlet0: 0 Mbps]{lang="EN-US"}

[  Local reserved bandwidth for class A0 service on Ringlet1: 0 Mbps]{lang="EN-US"}

[  Local rate limit for subclass A1 service on Ringlet0: 5 Mbps]{lang="EN-US"}

[  Local rate limit for subclass A1 service on Ringlet1: 5 Mbps]{lang="EN-US"}

[  Local rate limit for class B CIR service on Ringlet0: 0 Mbps]{lang="EN-US"}

[  Local rate limit for class B CIR service on Ringlet1: 0 Mbps]{lang="EN-US"}

[  Local rate limit for class B EIR and class C service on Ringlet0: 2500 Mbps]{lang="EN-US"}

[  Local rate limit for class B EIR and class C service on Ringlet1: 2500 Mbps]{lang="EN-US"}

[  Total reserved bandwidth for class A0 service on Ringlet0: 0 Mbps]{lang="EN-US"}

[  Total reserved bandwidth for class A0 service on Ringlet1: 0 Mbps]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_2111028618}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router2]{lang="EN-US"}[没有绑定任何]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口，显示该接口的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[公平性参数信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr fairness rpr-router 2]{lang="EN-US"}]{#struct_0_56601_x1470_773492766}

[RPR fairness parameters on interface RPR-Router2:]{lang="EN-US"}

[  Fairness weight on Ringlet0: 1]{lang="EN-US"}

[  Fairness weight on Ringlet1: 1]{lang="EN-US"}

[  Local reserved bandwidth for class A0 service on Ringlet0: 0 in permillage]{lang="EN-US"}

[  Local reserved bandwidth for class A0 service on Ringlet1: 0 in permillage]{lang="EN-US"}

[  Local rate limit for subclass A1 service on Ringlet0: 2 in permillage]{lang="EN-US"}

[  Local rate limit for subclass A1 service on Ringlet1: 2 in permillage]{lang="EN-US"}

[  Local rate limit for class B CIR service on Ringlet0: 0 in permillage]{lang="EN-US"}

[  Local rate limit for class B CIR service on Ringlet1: 0 in permillage]{lang="EN-US"}

[  Local rate limit for class B EIR and class C service on Ringlet0: 1000 in permillage]{lang="EN-US"}

[  Local rate limit for class B EIR and class C service on Ringlet1: 1000 in permillage]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 12 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_1151901358}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[当]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_377335636}[RPR]{lang="EN-US"}[逻辑接口没有与]{style="font-family:KaiTi_GB2312"}[RPR]{lang="EN-US"}[物理接口进行绑定时，站点在]{style="font-family:KaiTi_GB2312"}[0]{lang="EN-US"}[环和]{style="font-family:KaiTi_GB2312"}[1]{lang="EN-US"}[环上为各类业务配置的预留带宽显示的是该类业务预留带宽占总带宽的千分比。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display rpr fairness]{lang="EN-US"}]{#struct_0_56601_x1470_1078781891}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1458799904}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_96059396}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_296038033}

[[RPR fairness parameters on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_870008489}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x373026843}[[接口对应站点公平性参数信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Fairness weight on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x792591175}

[[[本站点在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x1731546769}[[环上公平权重]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Fairness weight on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_86296135}

[[[本站点在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}]{#struct_0_56601_x1470_1730642619}[[环上公平权重]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Local reserved bandwidth for class A0 service on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x154075633}

[[[本站点在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_131574431}[[环上为]{style="font-family:宋体"}]{.ItemListinTableCharChar}[A0]{lang="EN-US"}[[类业务预留的带宽]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Local reserved bandwidth for class A0 service on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_2100352817}

[[[本站点在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x389306648}[[环上为]{style="font-family:宋体"}]{.ItemListinTableCharChar}[A0]{lang="EN-US"}[[类业务预留的带宽]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Local rate limit for subclass A1 service on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_326643139}

[[[本站点在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[0]{lang="EN-US"}]{#struct_0_56601_x1470_426426464}[[环上为]{style="font-family:宋体"}]{.ItemListinTableCharChar}[A1]{lang="EN-US"}[[类业务配置的预留带宽]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Local rate limit for subclass A1 service on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_1700860283}

[[[本站点在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x1585110295}[[环上为]{style="font-family:宋体"}]{.ItemListinTableCharChar}[A1]{lang="EN-US"}[[类业务配置的预留带宽]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Local rate limit for class B CIR service on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x170442481}

[[本站点在]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_91286461}[环上为]{style="font-family:宋体"}[B-CIR]{lang="EN-US"}[类业务配置的预留带宽]{style="font-family:宋体"}

[[Local rate limit for class B CIR service on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_1340423123}

[[本站点在]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x1955390589}[环上为]{style="font-family:宋体"}[B-CIR]{lang="EN-US"}[类业务配置的预留带宽]{style="font-family:宋体"}

[[Local rate limit for class B EIR and class C service on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x1397013193}

[[本站点在]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_1337947900}[环上为]{style="font-family:宋体"}[B-EIR]{lang="EN-US"}[和]{style="font-family:宋体"}[C]{lang="EN-US"}[类业务配置的预留带宽]{style="font-family:宋体"}

[[Local rate limit for class B EIR and class C service on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_1313650211}

[[本站点在]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_1077675234}[环上为]{style="font-family:宋体"}[B-EIR]{lang="EN-US"}[和]{style="font-family:宋体"}[C]{lang="EN-US"}[类业务配置的预留带宽]{style="font-family:宋体"}

[[Total reserved bandwidth for class A0 service on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_697995923}

[[本站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1908336422}[环上的所有站点在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上为]{style="font-family:宋体"}[A0]{lang="EN-US"}[类业务预留带宽之和]{style="font-family:宋体"}

[[Total reserved bandwidth for class A0 service on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_x423166353}

[[本站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_354097052}[环上的所有站点在]{style="font-family:宋体"}[1]{lang="EN-US"}[环上为]{style="font-family:宋体"}[A0]{lang="EN-US"}[类业务预留带宽之和]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::::: {#382868596 .myid}
[]{#_Toc404795727}[]{#struct_0_56601_x1470_x23709110}[]{#_Toc353460850}

**RPR \-- RPR配置命令 \-- display rpr mac-address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_1129934100}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_776560717}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **rpr** **mac-address**]{lang="EN-US"}]{#struct_0_56601_x1470_x1130337957}[命令用来显示]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}[地址表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_820546933}[]{#_Toc353460851}

[**[display]{lang="EN-US"}**[ **rpr** **mac-address** \[ **dynamic** \| **static** \] \[ **destination** *mac-address1* \] \[ **vlan** *vlan-id* \] \[ **ring** *mac-address2* \] \[ **rpr-bridge** *interface-number* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_56601_x1470_1752716929}[]{#_Toc353460852}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1433626891}[]{#_Toc353460853}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1454036054}[]{#_Toc353460854}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1708990923}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x198237500}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_215259678}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1302831863}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x35170160}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1805942289}[]{#_Toc353460857}

[**[dynamic]{lang="EN-US"}**]{#struct_0_56601_x1470_481966485}[：显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}[]{#_Toc353460859}

[**[static]{lang="EN-US"}**]{#struct_0_56601_x1470_x1552040526}[：显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}[]{#_Toc353460858}

[**[destination]{lang="EN-US"}**[ *mac-address1*]{lang="EN-US"}]{#struct_0_56601_x1470_x1352442624}[：显示指定目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的表项信息。]{style="font-family:宋体"}[]{#_Toc353460860}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_56601_x1470_260716415}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[]{#_Toc353460861}

[**[ring]{lang="EN-US"}**[ *mac-address2*]{lang="EN-US"}]{#struct_0_56601_x1470_610462064}[：显示指定下环站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的表项信息。]{style="font-family:宋体"}[]{#_Toc353460862}

[**[rpr-bridge]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_163841339}[：显示指定二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应站点的]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}[地址表信息。如果未指定本参数，将显示所有二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应站点的]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}[]{#_Toc353460863}

[**[count]{lang="EN-US"}**]{#struct_0_56601_x1470_1838647610}[：显示指定]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}[地址表的表项条数。]{style="font-family:宋体"}[]{#_Toc353460864}[]{#_Toc353460865}[]{#_Toc353460866}[]{#_Toc353460867}[]{#_Toc353460868}[]{#_Toc353460869}[]{#_Toc353460871}[]{#_Toc353460872}[]{#_Toc353460874}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1622783751}[]{#_Toc353460875}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_541167946}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr mac-address static]{lang="EN-US"}]{#struct_0_56601_x1470_1176842829}

[Static MAC address table on interface RPR-Bridge1:]{lang="EN-US"}

[ MAC address     VLAN ID   Next hop          Status    Ringlet ID   TTL]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 0001-0001-0001  1         00e0-fc01-6503    Valid     1            1]{lang="EN-US"}

[ 0001-0001-0001  2         00e0-fc01-6503    Valid     1            1]{lang="EN-US"}

[ 0002-0002-0002  2         00e0-fc01-6503    Invalid   N/A          N/A]{lang="EN-US"}

[ 0002-0002-0002  1000      00e0-fc01-6503    Valid     1            244]{lang="EN-US"}

[ \-\--   Total entrie(s): 4   \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_130489655}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr mac-address dynamic]{lang="EN-US"}]{#struct_0_56601_x1470_x413856741}

[Dynamic MAC address table on interface RPR-Bridge1:]{lang="EN-US"}

[ MAC address     VLAN ID   Next hop          Status    Ringlet ID   TTL]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 0001-0001-0001  2         00e0-fc01-6503    Valid     1            1]{lang="EN-US"}

[ \-\--   Total entrie(s): 1   \-\--]{lang="EN-US"}[]{#_Toc353460876}[]{#_Toc353460877}[]{#_Toc353460878}[]{#_Toc353460879}[]{#_Toc353460880}[]{#_Toc353460881}[]{#_Toc353460882}[]{#_Toc353460883}[]{#_Toc353460884}[]{#_Toc353460885}[]{#_Toc353460886}[]{#_Toc353460887}[]{#_Toc353460888}[]{#_Toc353460889}[]{#_Toc353460890}[]{#_Toc353460891}[]{#_Toc353460892}[]{#_Toc353460893}[]{#_Toc353460894}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 14 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_737983571}[]{#_Toc353460895}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1389462951}[动态]{style="font-family:KaiTi_GB2312"}[MAC]{lang="EN-US"}[地址表的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}[]{#_Toc353460896}
:::

[]{#_Toc353460897}[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display rpr mac-address]{lang="EN-US"}]{#struct_0_56601_x1470_1245715191}[命令显示信息描述表]{style="font-family:黑体"}[]{#_Toc353460898}

[]{#table_struct_0_x1428615302}[]{#struct_0_56601_x1470_x1870600803}[]{#_Toc353460931}[字段]{style="font-family:黑体"}
:::::::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_1580127356}

[[Static MAC address table on interface RPR-Bridge1]{lang="EN-US"}]{#struct_0_56601_x1470_x1223699162}

[[RPR-Bridge1]{lang="EN-US"}]{#struct_0_56601_x1470_1389588818}[接口对应站点的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息]{style="font-family:宋体"}

[[Dynamic MAC address table on interface RPR-Bridge1]{lang="EN-US"}]{#struct_0_56601_x1470_703058424}

[[RPR-Bridge1]{lang="EN-US"}]{#struct_0_56601_x1470_2042767498}[接口对应站点的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_1916006438}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x519442852}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_56601_x1470_14043415}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_1116506315}[地址所在的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_56601_x1470_941223353}

[[下一跳的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x1582185189}[地址]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_56601_x1470_x420817054}

[[是否有效：]{style="font-family:宋体"}]{#struct_0_56601_x1470_451054908}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_56601_x1470_x2103893895}[：表示有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_56601_x1470_986365547}[：表示无效]{lang="EN-US" style="font-family:宋体"}

[[Ringlet ID]{lang="EN-US"}]{#struct_0_56601_x1470_773558302}

[[子环号]{style="font-family:宋体"}]{#struct_0_56601_x1470_x394170454}

[[TTL]{lang="EN-US"}]{#struct_0_56601_x1470_x36297313}

[[生存时间]{style="font-family:宋体"}]{#struct_0_56601_x1470_457211769}

[[Total entrie(s)]{lang="EN-US"}]{#struct_0_56601_x1470_55928498}

[[指定]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x1451151631}[地址表表项条数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x792525639}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的表项条数。]{style="font-family:宋体"}[]{#_Toc353460932}

[[\<Sysname\> display rpr mac-address static count]{lang="EN-US"}]{#struct_0_56601_x1470_x2141813801}[]{#_Toc353460933}

[Static MAC address table on interface RPR-Bridge1[]{#_Toc353460934}:]{lang="EN-US"}

[  5 entries found[]{#_Toc353460935}.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Static MAC address table on interface RPR-Bridge2[]{#_Toc353460936}:]{lang="EN-US"}

[  No entry found[]{#_Toc353460937}.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_639455437}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的表项条数。]{style="font-family:宋体"}[]{#_Toc353460938}

[[\<Sysname\> display rpr mac-address dynamic count]{lang="EN-US"}]{#struct_0_56601_x1470_x808907576}[]{#_Toc353460939}

[Dynamic MAC address table on interface RPR-Bridge1:[]{#_Toc353460940}]{lang="EN-US"}

[  No entry found[]{#_Toc353460941}.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Dynamic MAC address table on interface RPR-Bridge2:[]{#_Toc353460942}]{lang="EN-US"}

[  No entry found[]{#_Toc353460943}.]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1772728429}[]{#_Toc353460944}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_937049544}[动态]{style="font-family:KaiTi_GB2312"}[MAC]{lang="EN-US"}[地址表表项条数的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}[]{#_Toc353460945}
:::

[]{#_Toc353460946}[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display rpr mac-address count]{lang="EN-US"}]{#struct_0_56601_x1470_x389241112}[命令显示信息描述表]{style="font-family:黑体"}[]{#_Toc353460947}

[]{#table_struct_0_x1426718309}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_x54282014}[]{#_Toc353460948}

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_1002246605}[]{#_Toc353460949}

[]{#_Toc353460950}

[[Static MAC address table on interface]{lang="EN-US"}]{#struct_0_56601_x1470_493817186}[]{#_Toc353460951}[ RPR-Bridge1]{lang="EN-US"}

[[RPR-Bridge1]{lang="EN-US"}]{#struct_0_56601_x1470_960400154}[接口对应站点的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息]{style="font-family:宋体"}[]{#_Toc353460952}

[]{#_Toc353460953}

[[Dynamic MAC address table on interface]{lang="EN-US"}]{#struct_0_56601_x1470_1096005136}[]{#_Toc353460954}[ RPR-Bridge1]{lang="EN-US"}

[[RPR-Bridge1]{lang="EN-US"}]{#struct_0_56601_x1470_1756608127}[接口对应站点的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息]{style="font-family:宋体"}[]{#_Toc353460955}

[]{#_Toc353460956}

[[5 entries found]{lang="EN-US"}]{#struct_0_56601_x1470_x1955325053}[]{#_Toc353460957}

[[指定]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x292487433}[地址表表项条数]{style="font-family:宋体"}[]{#_Toc353460958}

[]{#_Toc353460959}

[]{#_Toc353460960}[ ]{lang="EN-US"}

::::: {#301569792 .myid}
[]{#_Toc404795728}[]{#struct_0_56601_x1470_1089772225}[]{#_Toc353460961}

**RPR \-- RPR配置命令 \-- display rpr mac-address aging-time**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x896430627}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1465787943}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **rpr** **mac-address** **aging-time**]{lang="EN-US"}]{#struct_0_56601_x1470_1967162284}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项的老化时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1908270886}[]{#_Toc353460962}

[**[display]{lang="EN-US"}**[ **rpr** **mac-address** **aging-time**]{lang="EN-US"}]{#struct_0_56601_x1470_184175611}[]{#_Toc353460963}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1366063148}[]{#_Toc353460964}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1615216734}[]{#_Toc353460965}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1803540760}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_279030125}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x439626006}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1208875423}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_701917675}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1371788467}[]{#_Toc353460979}

[]{#_Toc168996352}[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_820612469}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项的老化时间。]{style="font-family:宋体"}[]{#_Toc353460980}

[[\<Sysname\> display rpr mac-address aging-time]{lang="EN-US"}]{#struct_0_56601_x1470_x706015227}[]{#_Toc353460981}

[  Dynamic MAC-Learning aging time : 100 s]{lang="EN-US"}[]{#_Toc353460982}

[[表1-7 ]{lang="EN-US"}[display rpr mac-address aging-time]{lang="EN-US"}]{#struct_0_56601_x1470_755447686}[命令显示信息描述表]{style="font-family:黑体"}[]{#_Toc353460983}

[]{#table_struct_0_x1427655751}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_x480948482}[]{#_Toc353460984}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_610902143}[]{#_Toc353460985}

[]{#_Toc353460986}

[[Dynamic MAC-Learning aging time]{lang="EN-US"}]{#struct_0_56601_x1470_x899384573}[]{#_Toc353460987}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_938014775}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项的老化时间]{style="font-family:宋体"}[]{#_Toc353460988}

[]{#_Toc353460989}

[]{#_Toc353460990}[ ]{lang="EN-US"}

::::: {#1318827234 .myid}
[]{#_Hlt17378915}[]{#_Toc404795729}[]{#struct_0_56601_x1470_x1844841679}[]{#_Toc133657444}

**RPR \-- RPR配置命令 \-- display rpr protection**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **protection**]{lang="EN-US"}]{#struct_0_56601_x1470_x1735861750}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[的保护信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1552237134}

[**[display]{lang="EN-US"}**[ **rpr** **protection** \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_x2084496947}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_302630438}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_367810713}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x315198615}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1088063757}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_845840077}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1796653519}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_122484947}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x891925424}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_x874806183}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的保护信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的保护信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1820541267}

[[需要注意的是，保护倒换模式分为配置的保护倒换模式和生效的保护倒换模式，前者由用户手工配置，但并不一定生效，协议自动检查环上所有站点的保护倒换模式，尽量保证生效的保护倒换模式的一致性。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1176646221}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_72282213}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_557225974}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[已绑定两个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口，显示该接口的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[保护信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr protection rpr-router 1]{lang="EN-US"}]{#struct_0_56601_x1470_x1441396019}

[Protection information on interface RPR-Router1:]{lang="EN-US"}

[  Configured protection mode: Steer]{lang="EN-US"}

[  Active protection mode: Steer]{lang="EN-US"}

[  Protection reversion mode: Revertible]{lang="EN-US"}

[  Context containment: Disabled]{lang="EN-US"}

[                                    West span              East span]{lang="EN-US"}

[  Protection state                  IDLE                   FS]{lang="EN-US"}

[  Edge state                        Unedged                Edged]{lang="EN-US"}

[  Last known neighbour              00e0-0100-0002         00e0-0300-0002]{lang="EN-US"}

[  The number of protection states   1                      4]{lang="EN-US"}

[  The number of local edges         0                      2]{lang="EN-US"}

[  Last local edge time              -                      2014.04.08 05:47:31]{lang="EN-US"}

[  Local edge start time             -                      2014.04.08 05:48:07]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1628745762}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router2]{lang="EN-US"}[没有绑定任何]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口，显示该接口的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[保护信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr protection rpr-router 2]{lang="EN-US"}]{#struct_0_56601_x1470_1749144999}

[Protection information on interface RPR-Router2:]{lang="EN-US"}

[  Configured protection mode: Steer]{lang="EN-US"}

[  Protection reversion mode: Revertible]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 17 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_1579930748}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[当]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1120783389}[RPR]{lang="EN-US"}[逻辑接口未与任何]{style="font-family:KaiTi_GB2312"}[RPR]{lang="EN-US"}[物理接口进行绑定时，将只显示该]{style="font-family:KaiTi_GB2312"}[RPR]{lang="EN-US"}[逻辑接口配置的保护倒换模式和保护倒换恢复模式。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[]{#_Toc118294325}[[表1-8 ]{lang="EN-US"}[display rpr protection]{lang="EN-US"}]{#struct_0_56601_x1470_778417638}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1427228403}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_712197898}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_520011795}

[[Protection information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x283152235}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_1361795888}[[接口对应站点的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[[RPR]{lang="EN-US"}]{.ItemListinTableCharChar}[[保护信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Configured protection mode]{lang="EN-US"}]{#struct_0_56601_x1470_x1752851862}

[[[配置的保护倒换模式]{style="font-family:宋体"}]{.ItemListinTableCharChar}]{#struct_0_56601_x1470_13846807}

[[Active protection mode]{lang="EN-US"}]{#struct_0_56601_x1470_556689331}

[[[生效的保护倒换模式]{style="font-family:宋体"}]{.ItemListinTableCharChar}]{#struct_0_56601_x1470_1210752817}

[[Protection reversion mode]{lang="EN-US"}]{#struct_0_56601_x1470_x2087380081}

[[[保护倒换恢复模式]{style="font-family:宋体"}]{.ItemListinTableCharChar}]{#struct_0_56601_x1470_x873109005}

[[Context containment]{lang="EN-US"}]{#struct_0_56601_x1470_x1626150775}

[[上下文抑制]{style="font-family:宋体"}]{#struct_0_56601_x1470_773361694}[[是否生效：]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_56601_x1470_148836660}[：表示生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_56601_x1470_x1153277749}[：表示无效]{lang="EN-US" style="font-family:宋体"}

[[Protection state]{lang="EN-US"}]{#struct_0_56601_x1470_x1148970515}

[[[东西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_2119143265}[[上的保护状态：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_x784033172}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SF]{lang="EN-US"}]{#struct_0_56601_x1470_1505546089}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SD]{lang="EN-US"}]{#struct_0_56601_x1470_x792722247}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS]{lang="EN-US"}]{#struct_0_56601_x1470_x2137047787}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_x985979635}[：等待恢复状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_56601_x1470_x1456794351}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[Edge state]{lang="EN-US"}]{#struct_0_56601_x1470_x1630627983}

[[[东西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_95702617}[[上的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Edge]{lang="EN-US"}[[状态：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Edged]{lang="EN-US"}]{#struct_0_56601_x1470_x389437720}[：表示发生]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[dge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unedged]{lang="EN-US"}]{#struct_0_56601_x1470_706716349}[：表示没有发[[生]{style="font-family:宋体"}]{.ItemListinTableCharChar}]{lang="EN-US" style="font-family:宋体"}[[E]{lang="EN-US"}]{.ItemListinTableCharChar}[dge]{lang="EN-US"}

[[Last known neighbour]{lang="EN-US"}]{#struct_0_56601_x1470_x1955521661}

[[[东西向邻站点]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x933030461}[[地址]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[The number of protection states]{lang="EN-US"}]{#struct_0_56601_x1470_x1908467494}

[[[本站点东西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x650414760}[[上保护状态变化次数]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[The number of local edges]{lang="EN-US"}]{#struct_0_56601_x1470_x1370349534}

[[[本站点东西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_820415861}[[上出现]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Edge]{lang="EN-US"}[[的次数]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Last local edge time]{lang="EN-US"}]{#struct_0_56601_x1470_576316009}

[[[本站点东西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x1552171598}[[上上一次出现]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Edge]{lang="EN-US"}[[的时间]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Local edge start time]{lang="EN-US"}]{#struct_0_56601_x1470_1597623369}

[[[本站点东西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_1176711757}[[上当前]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Edge]{lang="EN-US"}[[的开始时间]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[ ]{lang="EN-US"}

::: {#1817001370 .myid}
[]{#_Toc404795730}[]{#struct_0_56601_x1470_1255850000}[]{#_Toc133657445}

**RPR \-- RPR配置命令 \-- display rpr rs-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **rs-table**]{lang="EN-US"}]{#struct_0_56601_x1470_1360012297}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[选环表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x971293447}

[**[display]{lang="EN-US"}**[ **rpr** **rs-table** { **default** \| **dynamic** \| **overall** \| **static** } \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_x1329891724}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1395113355}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_169446786}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_334482625}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x510296507}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_1579996284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1155657609}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_513799314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2073593945}

[**[default]{lang="EN-US"}**]{#struct_0_56601_x1470_173423202}[：显示默认选环表信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_56601_x1470_1526922896}[：显示动态选环表信息。]{style="font-family:宋体"}

[**[overall]{lang="EN-US"}**]{#struct_0_56601_x1470_x881517579}[：显示综合选环表信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_56601_x1470_x211443041}[：显示静态选环表信息。]{style="font-family:宋体"}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_1794340048}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点选环表的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点选环表的信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1092790061}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1274052321}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态选环表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr rs-table dynamic]{lang="EN-US"}]{#struct_0_56601_x1470_13912343}

[Dynamic ringlet selection table on interface RPR-Router1:]{lang="EN-US"}

[ MAC address     Ringlet ID  TTL  IP address       Station name]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 00e0-fc00-1a01  0           1    -]{lang="EN-US"}

[ \-\--   Entries in total: 1    \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x242279586}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态选环表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr rs-table static]{lang="EN-US"}]{#struct_0_56601_x1470_x626906601}

[Static ringlet selection table on interface RPR-Router1:]{lang="EN-US"}

[ MAC address    Ringlet ID   Status]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 0003-0002-0002 0            Invalid]{lang="EN-US"}

[ \-\--   Entries in total: 1    \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x468510586}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[默认选环表的信息。]{style="font-family:宋体"}

[[\<Sysname\>display rpr rs-table default]{lang="EN-US"}]{#struct_0_56601_x1470_1295851821}

[Default ringlet selection table on interface RPR-Router1:]{lang="EN-US"}

[  Configured default ringlet: Ringlet0]{lang="EN-US"}

[  Active default ringlet: Ringlet0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_220717836}[显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[综合选环表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr rs-table overall]{lang="EN-US"}]{#struct_0_56601_x1470_773427230}

[Overall ringlet selection table on interface RPR-Router2:]{lang="EN-US"}

[ MAC address     Ringlet ID  TTL  Type      IP address       Station name]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 00e0-fe10-0001  0           1    Dynamic   -]{lang="EN-US"}

[ \-\--   Entries in total: 1    \-\--]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display rpr rs-table]{lang="EN-US"}]{#struct_0_56601_x1470_x820386680}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1430675198}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_1670125513}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_658150071}

[[Dynamic ringlet selection table on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x426616536}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_1628969057}[[接口对应站点动态选环表的信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Static ringlet selection table on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1051374546}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x792656711}[[接口对应站点静态选环表的信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Default ringlet selection table on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_1753681821}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_661762097}[[接口对应站点默认选环表的信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Overall ringlet selection table on interface RPR-Router2]{lang="EN-US"}]{#struct_0_56601_x1470_1109517942}

[[RPR-Router2]{lang="EN-US"}]{#struct_0_56601_x1470_211386644}[[接口对应站点综合选环表的信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_x774446890}

[[[目的站点]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_1759493673}[[地址]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Ringlet ID]{lang="EN-US"}]{#struct_0_56601_x1470_x389372184}

[[发送子环：]{style="font-family:宋体"}]{#struct_0_56601_x1470_338451291}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_1833010720}[：表示]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_73471261}[：表示]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[环]{lang="EN-US" style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_56601_x1470_x1468106830}

[[生存时间，到目的站点经过的跳数]{style="font-family:宋体"}]{#struct_0_56601_x1470_825110822}

[[Type]{lang="EN-US"}]{#struct_0_56601_x1470_1570562963}

[[生成综合选环表的选环表类型：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1955456125}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_56601_x1470_938884907}[：表示静态选环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_56601_x1470_1140876746}[：表示动态选环]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_56601_x1470_667256624}

[[[目的站点]{style="font-family:宋体"}]{.ItemListinTableCharChar}[IP]{lang="EN-US"}]{#struct_0_56601_x1470_x663301542}[[地址，目的站点未配置]{style="font-family:宋体"}]{.ItemListinTableCharChar}[IP]{lang="EN-US"}[[地址时显示为]{style="font-family:宋体"}]{.ItemListinTableCharChar}[-]{lang="EN-US"}

[[Station name]{lang="EN-US"}]{#struct_0_56601_x1470_386176409}

[[目的站点名称]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1908401958}

[[Status]{lang="EN-US"}]{#struct_0_56601_x1470_1865843081}

[[表项状态：]{style="font-family:宋体"}]{#struct_0_56601_x1470_12693661}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_56601_x1470_1535836084}[：表示有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_56601_x1470_135408356}[：表示无效]{lang="EN-US" style="font-family:宋体"}

[[Configured default ringlet]{lang="EN-US"}]{#struct_0_56601_x1470_820481397}

[[配置的默认选环：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2073179677}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_1209637003}[：表示]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_1096450425}[：表示]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[环]{lang="EN-US" style="font-family:宋体"}

[[Active default ringlet]{lang="EN-US"}]{#struct_0_56601_x1470_575428651}

[[实际生效的默认选环：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x279488339}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x375169624}[：表示]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_x1685865038}[：表示]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[环]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1343457061 .myid}
[]{#_Toc404795731}[]{#struct_0_56601_x1470_609245552}[]{#_Toc133657446}

**RPR \-- RPR配置命令 \-- display rpr statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **statistics**]{lang="EN-US"}]{#struct_0_56601_x1470_446601335}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环上流量统计的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1442159767}

[**[display]{lang="EN-US"}**[ **rpr** **statistics** { **dmac** \| **smac** } \[ *mac-address* \] \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_x374776532}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1905541561}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1339873565}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2074116594}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_146763648}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_1043018317}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1869801645}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x659765405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_440052644}

[**[dmac]{lang="EN-US"}**]{#struct_0_56601_x1470_x440272828}[：显示发送到指定目的站点的流量统计信息。]{style="font-family:宋体"}

[**[smac]{lang="EN-US"}**]{#struct_0_56601_x1470_209004404}[：显示从指定源站点收到的流量统计信息。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_56601_x1470_1331568284}[：显示发送到环上指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的目的站点或从环上指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的源站点收到的流量统计信息。如果未指定本参数，将显示发送到环上所有站点或从环上所有站点收到的流量统计信息。]{style="font-family:宋体"}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_1650833752}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的流量统计信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的流量统计信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1363002940}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_896613638}[显示从]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00E0-FC00-1A01]{lang="EN-US"}[的环上站点发送过来的流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr statistics smac 00e0-fc00-1a01]{lang="EN-US"}]{#struct_0_56601_x1470_1446302844}

[Statistics for traffic from the source station on interface RPR-Router1:]{lang="EN-US"}

[ MAC address      Packets              Bytes]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 00e0-fc00-1a01   1844                 1844]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display rpr statistics]{lang="EN-US"}]{#struct_0_56601_x1470_1010326207}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1438468196}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_1534979710}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_871449647}

[[Statistics for traffic from the source station on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1699412100}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1024394794}[[接口对应站点基于源]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}[[地址统计的流量信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Statistics for traffic to the destination station on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x347456833}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1832233555}[[接口对应站点基于目的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}[[地址统计的流量信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_x119781097}

[[[源或目的站点的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x11837906}[[地址]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Packets]{lang="EN-US"}]{#struct_0_56601_x1470_x432143745}

[[发送或接收的报文数]{style="font-family:宋体"}]{#struct_0_56601_x1470_857560743}

[[Bytes]{lang="EN-US"}]{#struct_0_56601_x1470_x2038065807}

[[发送或接收的字节数]{style="font-family:宋体"}]{#struct_0_56601_x1470_1723956952}

[ ]{lang="EN-US"}

::::: {#-1315995407 .myid}
[]{#_Toc404795732}[]{#struct_0_56601_x1470_x1162851963}[]{#_Toc133657447}

**RPR \-- RPR配置命令 \-- display rpr timers**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **timers**]{lang="EN-US"}]{#struct_0_56601_x1470_x1579162316}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[可配定时器的值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_639733790}

[**[display]{lang="EN-US"}**[ **rpr** **timers** \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_x2132431072}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1943024603}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2093059242}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1164967003}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_360095834}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_1346551604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x926350151}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x1699675908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1998505160}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_2123834969}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的定时器信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的定时器信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1887022095}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1432382265}[显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[可配定时器的值。]{style="font-family:宋体"}

[[\<Sysname\> display rpr timers]{lang="EN-US"}]{#struct_0_56601_x1470_x523065624}

[RPR timers on interface RPR-Bridge1:]{lang="EN-US"}

[  Fast TP timer: 10 ms]{lang="EN-US"}

[  Slow TP timer: 100 ms]{lang="EN-US"}

[  Fast TC timer: 10 ms]{lang="EN-US"}

[  Slow TC timer: 100 ms]{lang="EN-US"}

[  ATD timer: 1 s]{lang="EN-US"}

[  WTR timer: 10 s]{lang="EN-US"}

[  Holdoff timer: 0 ms]{lang="EN-US"}

[  Keepalive timer: 3 ms]{lang="EN-US"}

[  Topology stability timer: 40 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[RPR timers on interface RPR-Router1:]{lang="EN-US"}

[  Fast TP timer: 10 ms]{lang="EN-US"}

[  Slow TP timer: 100 ms]{lang="EN-US"}

[  Fast TC timer: 10 ms]{lang="EN-US"}

[  Slow TC timer: 100 ms]{lang="EN-US"}

[  ATD timer: 1 s]{lang="EN-US"}

[  WTR timer: 10 s]{lang="EN-US"}

[  Holdoff timer: 0 ms]{lang="EN-US"}

[  Keepalive timer: 3 ms]{lang="EN-US"}

[  Topology stability timer: 40 ms]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_527082148}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_571387384}
:::

[ ]{lang="EN-US"}

[]{#_Toc118294330}[[表1-11 ]{lang="EN-US"}[display rpr timers]{lang="EN-US"}]{#struct_0_56601_x1470_27956451}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1434860887}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_1468311138}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_493537421}

[[RPR timers on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x2089149565}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_808459442}[接口对应站点所有定时器的值]{style="font-family:宋体"}

[[Fast TP timer]{lang="EN-US"}]{#struct_0_56601_x1470_1321362212}

[[TP]{lang="EN-US"}]{#struct_0_56601_x1470_1153047866}[帧快发定时器的值]{style="font-family:宋体"}

[[Slow TP timer]{lang="EN-US"}]{#struct_0_56601_x1470_1870132442}

[[TP]{lang="EN-US"}]{#struct_0_56601_x1470_807018018}[帧慢发定时器的值]{style="font-family:宋体"}

[[Fast TC timer]{lang="EN-US"}]{#struct_0_56601_x1470_x2065215817}

[[TC]{lang="EN-US"}]{#struct_0_56601_x1470_x1018424939}[帧快发定时器的值]{style="font-family:宋体"}

[[Slow TC timer]{lang="EN-US"}]{#struct_0_56601_x1470_x1842036891}

[[TC]{lang="EN-US"}]{#struct_0_56601_x1470_x1765645711}[帧慢发定时器的值]{style="font-family:宋体"}

[[ATD timer]{lang="EN-US"}]{#struct_0_56601_x1470_x2042095398}

[[ATD]{lang="EN-US"}]{#struct_0_56601_x1470_732784553}[帧定时器的值]{style="font-family:宋体"}

[[WTR timer]{lang="EN-US"}]{#struct_0_56601_x1470_2007481742}

[[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_267684996}[定时器的值]{style="font-family:宋体"}

[[Holdoff timer]{lang="EN-US"}]{#struct_0_56601_x1470_x1983640156}

[[Hold Off]{lang="EN-US"}]{#struct_0_56601_x1470_536320824}[定时器的值]{style="font-family:宋体"}

[[Keepalive timer]{lang="EN-US"}]{#struct_0_56601_x1470_x1434870226}

[[Keepalive]{lang="EN-US"}]{#struct_0_56601_x1470_686787957}[定时器的值]{style="font-family:宋体"}

[[Topology stability timer]{lang="EN-US"}]{#struct_0_56601_x1470_x47970543}

[[拓扑稳定定时器的值]{style="font-family:宋体"}]{#struct_0_56601_x1470_640376950}

[ ]{lang="EN-US"}

::: {#1751831933 .myid}
[]{#_Toc404795733}[]{#struct_0_56601_x1470_1733172945}[]{#_Toc133657448}

**RPR \-- RPR配置命令 \-- display rpr topology**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rpr** **topology**]{lang="EN-US"}]{#struct_0_56601_x1470_x1832780235}[命令用来显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1303079496}

[**[display]{lang="EN-US"}**[ **rpr** **topology** { **all** \| **local** \| **ring** \| **stations** } \[ **brief** \] \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_2020596512}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x435798453}

[[任意视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1682929781}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1685799502}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_226009780}

[[network-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x1160480888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1675736541}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56601_x1470_x1575292861}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_960919798}

[**[all]{lang="EN-US"}**]{#struct_0_56601_x1470_x19095637}[：显示拓扑数据库所有信息。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_56601_x1470_1913130939}[：显示本站点拓扑信息。]{style="font-family:宋体"}

[**[ring]{lang="EN-US"}**]{#struct_0_56601_x1470_x1765210875}[：显示环路级的拓扑信息。]{style="font-family:宋体"}

[**[stations]{lang="EN-US"}**]{#struct_0_56601_x1470_92604616}[：显示环上所有站点拓扑信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_56601_x1470_x217466482}[：显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[拓扑摘要信息。]{style="font-family:宋体"}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_x1698186277}[：显示指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的相关拓扑信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的相关拓扑信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_663289854}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1043083853}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[已绑定两个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口，显示该接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的所有拓扑数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr topology all rpr-router 1]{lang="EN-US"}]{#struct_0_56601_x1470_1446368380}

[Ring-level topology information on interface RPR-Router1:]{lang="EN-US"}

[  Number of stations on Ringlet0: 1]{lang="EN-US"}

[  Number of stations on Ringlet1: 1]{lang="EN-US"}

[  Total number of stations on the ring: 2]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Ring topology type: Closed ring]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local station topology information on interface RPR-Router1:]{lang="EN-US"}

[  Station name:]{lang="EN-US"}

[  MAC address: 00e0-fc00-1001]{lang="EN-US"}

[  IP address: -]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Active protection mode: Steer]{lang="EN-US"}

[  Protection state on the west span: IDLE]{lang="EN-US"}

[  Protection state on the east span: IDLE]{lang="EN-US"}

[  Edge state on the west span: Unedged]{lang="EN-US"}

[  Edge state on the east span: Unedged]{lang="EN-US"}

[  Sequence number: 10]{lang="EN-US"}

[  Last known neighbour on the west span: 00e0-fc00-1a01]{lang="EN-US"}

[  Last known neighbour on the east span: 00e0-fc00-1a01]{lang="EN-US"}

[  Local topology state: Valid]{lang="EN-US"}

[ ]{lang="EN-US"}

[Station topology information on interface RPR-Router1:]{lang="EN-US"}

[ Station entry on Ringlet0:]{lang="EN-US"}

[  MAC address: 00e0-fc00-1a01]{lang="EN-US"}

[  Station name:]{lang="EN-US"}

[  IP address: -]{lang="EN-US"}

[  Hops: 1]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Protection mode: Steer]{lang="EN-US"}

[  Protection state on the west span: IDLE]{lang="EN-US"}

[  Protection state on the east span: IDLE]{lang="EN-US"}

[  Edge state on the west span: Unedged]{lang="EN-US"}

[  Edge state on the east span: Unedged]{lang="EN-US"}

[  Sequence number: 9]{lang="EN-US"}

[  Reachability: Reachable]{lang="EN-US"}

[  Valid: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Station entry on Ringlet1:]{lang="EN-US"}

[  MAC address: 00e0-fc00-1a01]{lang="EN-US"}

[  Station name:]{lang="EN-US"}

[  IP address:  -]{lang="EN-US"}

[  Hops: 1]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Protection mode: Steer]{lang="EN-US"}

[  Protection state on the west span: IDLE]{lang="EN-US"}

[  Protection state on the east span: IDLE]{lang="EN-US"}

[  Edge state on the west span: Unedged]{lang="EN-US"}

[  Edge state on the east span: Unedged]{lang="EN-US"}

[  Sequence number: 9]{lang="EN-US"}

[  Reachability: Reachable]{lang="EN-US"}

[  Valid: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1805653815}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router2]{lang="EN-US"}[没有绑定任何]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口，显示该接口对应]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的所有拓扑数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr topology all rpr-router 2]{lang="EN-US"}]{#struct_0_56601_x1470_x1807691278}

[Ring-level topology information on interface RPR-Router2:]{lang="EN-US"}

[  Number of stations on Ringlet0: 0]{lang="EN-US"}

[  Number of stations on Ringlet1: 0]{lang="EN-US"}

[  Total number of stations on the ring: 1]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Ring topology type: Open ring]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local station topology information on interface RPR-Router2:]{lang="EN-US"}

[  Station name:]{lang="EN-US"}

[  IP address: -]{lang="EN-US"}

[ ]{lang="EN-US"}

[Station topology information on interface RPR-Router2:]{lang="EN-US"}

[ Station entry on Ringlet0:]{lang="EN-US"}

[  No station entry.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Station entry on Ringlet1: ]{lang="EN-US"}

[  No station entry.]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display rpr topology all]{lang="EN-US"}]{#struct_0_56601_x1470_x119715561}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1441242705}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_x778882929}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_1427631162}

[[Ring-level topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_857843763}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_429233459}[[接口对应的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[RPR]{lang="EN-US"}[[站点所在]{style="font-family:宋体"}]{.ItemListinTableCharChar}[RPR]{lang="EN-US"}[[环的环路拓扑信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Number of stations on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x1249241602}

[[[站点在西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x1341873018}[[上的站点数]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Number of stations on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_x1081841400}

[[[站点在东向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x2094547464}[[上的站点数]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Total number of stations on the ring]{lang="EN-US"}]{#struct_0_56601_x1470_942313711}

[[站点所在环上总站点数]{style="font-family:宋体"}]{#struct_0_56601_x1470_639799326}

[[Jumbo preference]{lang="EN-US"}]{#struct_0_56601_x1470_250928640}

[[[是否支持]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_1522401372}[[帧：]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Regular]{lang="EN-US"}]{#struct_0_56601_x1470_99526645}[：表示不支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_x683719730}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[Ring topology type]{lang="EN-US"}]{#struct_0_56601_x1470_x1248324404}

[[环状态：]{style="font-family:宋体"}]{#struct_0_56601_x1470_891523115}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Open ring]{lang="EN-US"}]{#struct_0_56601_x1470_x926284615}[：表示开环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Closed ring]{lang="EN-US"}]{#struct_0_56601_x1470_x899731895}[：表示闭环]{lang="EN-US" style="font-family:宋体"}

[[Local station topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_501461430}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_1280034643}[[接口对应的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[RPR]{lang="EN-US"}[[站点的本地拓扑数据库信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Station name]{lang="EN-US"}]{#struct_0_56601_x1470_x1247852062}

[[站点名称]{style="font-family:宋体"}]{#struct_0_56601_x1470_x222386831}

[[MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_x523000088}

[[[站点]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x270729109}[[地址]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[IP address]{lang="EN-US"}]{#struct_0_56601_x1470_x973936337}

[[[站点]{style="font-family:宋体"}]{.ItemListinTableCharChar}[IP]{lang="EN-US"}]{#struct_0_56601_x1470_2022817413}[[地址，未配置]{style="font-family:宋体"}]{.ItemListinTableCharChar}[IP]{lang="EN-US"}[[地址时显示为]{style="font-family:宋体"}]{.ItemListinTableCharChar}[-]{lang="EN-US"}

[[Active protection mode]{lang="EN-US"}]{#struct_0_56601_x1470_239579581}

[[站点生效保护倒换模式：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1970427427}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wrap]{lang="EN-US"}]{#struct_0_56601_x1470_x1039324222}[：表示]{lang="EN-US" style="font-family:宋体"}[wrap]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Steer]{lang="EN-US"}]{#struct_0_56601_x1470_x2089084029}[：表示]{lang="EN-US" style="font-family:宋体"}[steer]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Protection state on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_x695417507}

[[[站点西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_1061657279}[[的保护状态：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_1685095360}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SF]{lang="EN-US"}]{#struct_0_56601_x1470_1686093438}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SD]{lang="EN-US"}]{#struct_0_56601_x1470_401933017}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS]{lang="EN-US"}]{#struct_0_56601_x1470_x2042029862}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_236823741}[：等待恢复状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_56601_x1470_804484935}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[Protection state on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_160135135}

[[[站点东向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_590583978}[[的保护状态：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_x1336399127}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SF]{lang="EN-US"}]{#struct_0_56601_x1470_464774277}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SD]{lang="EN-US"}]{#struct_0_56601_x1470_686853493}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS]{lang="EN-US"}]{#struct_0_56601_x1470_x1890908181}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_1860282299}[：等待恢复状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_56601_x1470_x99795653}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[Edge state on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_x1057419329}

[[[站点西向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x1685996110}[[是否出现]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Edge]{lang="EN-US"}[[状态：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Edged]{lang="EN-US"}]{#struct_0_56601_x1470_1058519418}[：表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unedged]{lang="EN-US"}]{#struct_0_56601_x1470_x1544596308}[：表示没有[[发生]{style="font-family:宋体"}]{.ItemListinTableCharChar}]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[Edge state on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_x749652816}

[[[站点东向]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_790571098}[[是否出现]{style="font-family:宋体"}]{.ItemListinTableCharChar}[Edge]{lang="EN-US"}[[状态：]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Edged]{lang="EN-US"}]{#struct_0_56601_x1470_1487735191}[表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unedged]{lang="EN-US"}]{#struct_0_56601_x1470_1042887245}[表示[[没有发生]{style="font-family:宋体"}]{.ItemListinTableCharChar}]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[Sequence number]{lang="EN-US"}]{#struct_0_56601_x1470_x1236599861}

[[TP]{lang="EN-US"}]{#struct_0_56601_x1470_x980288159}[[帧序列号]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Last known neighbour on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_x1269909}

[[[西向最后学习到的邻站点的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_375464608}[[地址]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Last known neighbour on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_886202662}

[[[东向最后学习到的邻站点的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_1446171772}[[地址]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Local topology state]{lang="EN-US"}]{#struct_0_56601_x1470_1329510485}

[[本站点拓扑状态：]{style="font-family:宋体"}]{#struct_0_56601_x1470_233780037}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Start]{lang="EN-US"}]{#struct_0_56601_x1470_x1013119079}[：表示拓扑初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stable]{lang="EN-US"}]{#struct_0_56601_x1470_x1875712416}[：表示拓扑稳定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unstable]{lang="EN-US"}]{#struct_0_56601_x1470_x366889132}[：表示拓扑不稳定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_56601_x1470_x119912169}[：表示拓扑有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_56601_x1470_x774247994}[：表示拓扑无[[效]{style="font-family:宋体"}]{.ItemListinTableCharChar}]{lang="EN-US" style="font-family:宋体"}

[[Station topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_1369524444}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_1996826001}[[接口对应的]{style="font-family:宋体"}]{.ItemListinTableCharChar}[RPR]{lang="EN-US"}[[站点的拓扑数据库信息]{style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Station entry on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_639602718}

[[站点西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_233680843}[上邻站点的拓扑信息]{style="font-family:宋体"}

[[Station entry on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_2044767341}

[[站点东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_609218611}[上邻站点的拓扑信息]{style="font-family:宋体"}

[[Hops]{lang="EN-US"}]{#struct_0_56601_x1470_x1528421380}

[[该站点到本地站点的跳数]{style="font-family:宋体"}]{#struct_0_56601_x1470_x926481223}

[[Protection mode]{lang="EN-US"}]{#struct_0_56601_x1470_x905284107}

[[站点的保护倒换模式：]{style="font-family:宋体"}]{#struct_0_56601_x1470_1064223532}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="EN-US"}[rap]{lang="EN-US"}]{#struct_0_56601_x1470_1838985692}[：表示]{lang="EN-US" style="font-family:宋体"}[Wrapping]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="NL"}]{#struct_0_56601_x1470_483708150}[teer]{lang="NL"}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[Steering]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Sequence number]{lang="EN-US"}]{#struct_0_56601_x1470_x523196696}

[[TP]{lang="EN-US"}]{#struct_0_56601_x1470_x1073408107}[帧序列号]{style="font-family:宋体"}

[[Reachability]{lang="EN-US"}]{#struct_0_56601_x1470_1351470023}

[[站点是否可达：]{style="font-family:宋体"}]{#struct_0_56601_x1470_623387791}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}[eachable]{lang="EN-US"}]{#struct_0_56601_x1470_x2084791602}[：表示可达]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nreachable]{lang="EN-US"}]{#struct_0_56601_x1470_x2089280637}[：表示不可达]{lang="EN-US" style="font-family:宋体"}

[[Valid]{lang="EN-US"}]{#struct_0_56601_x1470_x2033549063}

[[表项是否有效：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x901500231}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_906621250}[：表示有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x2042226470}[：表示无效]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_198610423}[显示拓扑数据库所有信息的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rpr topology all brief]{lang="EN-US"}]{#struct_0_56601_x1470_1513900478}

[Topology information items:]{lang="EN-US"}

[PSW: Protection State, West       PSE: Protection State, East]{lang="EN-US"}

[ESW: Edge State, West             ESE: Edge State, East]{lang="EN-US"}

[WC: Wrap protection Configured    JP: Jumbo frame Preferred]{lang="EN-US"}

[ ]{lang="EN-US"}

[Ring-level topology information on interface RPR-Router1:]{lang="EN-US"}

[ Ringlet0  Ringlet1  Ring  Jumbo prefer  Topology type]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 1         1         2     Regular       Closed ring]{lang="EN-US"}

[ ]{lang="EN-US"}

[Local station topology information on interface RPR-Router1:]{lang="EN-US"}

[ MAC address    PSW  PSE  ESW  ESE  WC  JP  IP address       Station name]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 00e0-fc00-1001 IDLE IDLE 0    0    0   0   -                StationA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Station topology information on interface RPR-Router1:]{lang="EN-US"}

[ Station entry on Ringlet0:]{lang="EN-US"}

[ MAC address    PSW  PSE  ESW  ESE  WC  JP  IP address       Station name]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 00e0-fc00-1a01 IDLE IDLE 0    0    0   0   -                StationB]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Station entry on Ringlet1:]{lang="EN-US"}

[ MAC address    PSW  PSE  ESW  ESE  WC  JP  IP address       Station name]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 00e0-fc00-1a01 IDLE IDLE 0    0    0   0   -                StationB]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display rpr topology all brief]{lang="EN-US"}]{#struct_0_56601_x1470_2080244738}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1412738983}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_1222917402}

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_686656885}

[[Topology information items]{lang="EN-US"}]{#struct_0_56601_x1470_x1989046107}

[[拓扑信息条目]{style="font-family:宋体"}]{#struct_0_56601_x1470_x222424935}

[[PSE]{lang="EN-US"}]{#struct_0_56601_x1470_2080452333}

[[站点东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x1503165886}[保护状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_56601_x1470_x1674532055}[S]{lang="EN-US"}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_56601_x1470_x1365297414}[F]{lang="EN-US"}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_56601_x1470_x22820851}[D]{lang="EN-US"}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}]{#struct_0_56601_x1470_x1685930574}[S]{lang="EN-US"}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_813315808}[：等待恢复状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_56601_x1470_1660474275}[DLE]{lang="EN-US"}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[PSW]{lang="EN-US"}]{#struct_0_56601_x1470_133375410}

[[站点西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_809517646}[保护状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_56601_x1470_x2044109935}[S]{lang="EN-US"}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_56601_x1470_355293075}[F]{lang="EN-US"}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_56601_x1470_1921719170}[D]{lang="EN-US"}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}]{#struct_0_56601_x1470_1042952781}[S]{lang="EN-US"}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_x59418239}[：等待恢复状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_56601_x1470_x168870814}[DLE]{lang="EN-US"}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[ESE]{lang="EN-US"}]{#struct_0_56601_x1470_1317609927}

[[站点东向]{style="font-family:宋体"}[Span Edge]{lang="EN-US"}]{#struct_0_56601_x1470_x1188154082}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x1474768999}[：表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_292952626}[：表示没有发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[ESW]{lang="EN-US"}]{#struct_0_56601_x1470_1446237308}

[[站点西向]{style="font-family:宋体"}[Span Edge]{lang="EN-US"}]{#struct_0_56601_x1470_1363410193}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_1256608591}[：表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_18991534}[：表示没有发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[WC]{lang="EN-US"}]{#struct_0_56601_x1470_454355744}

[[Wrap]{lang="EN-US"}]{#struct_0_56601_x1470_x545069070}[保护设置：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x119846633}[：表示]{lang="EN-US" style="font-family:宋体"}[Wrapping]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x789070760}[：表示]{lang="EN-US" style="font-family:宋体"}[Steering]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[JP:Jumbo frame preferred]{lang="EN-US"}]{#struct_0_56601_x1470_817972227}

[[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_x861456452}[帧设置：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x1686381335}[：表示支持]{lang="EN-US" style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_1325787373}[：表示不支持]{lang="EN-US" style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[Ring-level topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x268058901}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_639668254}[接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的拓扑信息]{style="font-family:宋体"}

[[Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_1388662984}

[[站点在西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_1472499202}[上的站点数]{style="font-family:宋体"}

[[Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_1466833680}

[[站点在东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x137187171}[上的站点数]{style="font-family:宋体"}

[[Ring]{lang="EN-US"}]{#struct_0_56601_x1470_x98859974}

[[站点所在环上总站点数]{style="font-family:宋体"}]{#struct_0_56601_x1470_x926415687}

[[Jumbo prefer]{lang="EN-US"}]{#struct_0_56601_x1470_1813881743}

[[是否支持]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_1932627846}[帧：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[Regular]{lang="PT-BR"}]{#struct_0_56601_x1470_x92227836}[：]{lang="EN-US" style="font-family:宋体"}[表示不支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_x1495423608}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[Topology type]{lang="EN-US"}]{#struct_0_56601_x1470_x523131160}

[[环状态：]{style="font-family:宋体"}]{#struct_0_56601_x1470_116946285}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[pen ring]{lang="EN-US"}]{#struct_0_56601_x1470_x1027064711}[：表示开环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}[losed ring]{lang="EN-US"}]{#struct_0_56601_x1470_1685207568}[：表示闭环]{lang="EN-US" style="font-family:宋体"}

[[Local station topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_923391366}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x2089215101}[接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的本地拓扑数据库摘要信息]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_236929615}

[[站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_1567621800}[地址]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_56601_x1470_x332740572}

[[站点]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56601_x1470_1974198965}[地址]{style="font-family:宋体"}

[[Station name]{lang="EN-US"}]{#struct_0_56601_x1470_x2042160934}

[[站点名称]{style="font-family:宋体"}]{#struct_0_56601_x1470_1864620914}

[[Station topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_443831177}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_53906263}[接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的其它站点的拓扑摘要信息]{style="font-family:宋体"}

[[Station entry on ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_1723609512}

[[该接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_686722421}[站点在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的西向]{style="font-family:宋体"}[Span]{lang="EN-US"}[上邻站点的拓扑摘要信息]{style="font-family:宋体"}

[[Station entry on ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_x1662515086}

[[该接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_1769899059}[站点在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的东向]{style="font-family:宋体"}[Span]{lang="EN-US"}[上邻站点的拓扑摘要信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1756945781}[显示本站点的拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\>display rpr topology local]{lang="EN-US"}]{#struct_0_56601_x1470_x1686127182}

[Local station topology information on interface RPR-Router1:]{lang="EN-US"}

[  Station name: StationA]{lang="EN-US"}

[  MAC address: 00e0-fc00-1001]{lang="EN-US"}

[  IP address: -]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Active protection mode: Steer]{lang="EN-US"}

[  Protection state on the west span: IDLE]{lang="EN-US"}

[  Protection state on the east span: IDLE]{lang="EN-US"}

[  Edge state on the west span: Unedged]{lang="EN-US"}

[  Edge state on the east span: Unedged]{lang="EN-US"}

[  Sequence number: 10]{lang="EN-US"}

[  Last known neighbour on the west span: 00e0-fc00-1a01]{lang="EN-US"}

[  Last known neighbour on the east span: 00e0-fc00-1a01]{lang="EN-US"}

[  Local topology state: Valid]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display rpr topology local]{lang="EN-US"}]{#struct_0_56601_x1470_x2016033758}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1417201994}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1292934541}

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_x630628370}

[[Local station topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1930131537}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1150788905}[接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的本地拓扑数据库信息]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_1042756173}

[[站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x2002548774}[地址]{style="font-family:宋体"}

[[Station name]{lang="EN-US"}]{#struct_0_56601_x1470_x1787850686}

[[站点名称]{style="font-family:宋体"}]{#struct_0_56601_x1470_x261859712}

[[IP address]{lang="EN-US"}]{#struct_0_56601_x1470_x1110314614}

[[站点]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56601_x1470_1001386657}[地址]{style="font-family:宋体"}

[[Jumbo preference]{lang="EN-US"}]{#struct_0_56601_x1470_1001786688}

[[是否支持]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_1002245303}[帧：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="PT-BR"}]{#struct_0_56601_x1470_x1100977357}[egular]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示不支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[J]{lang="EN-US"}[umbo]{lang="EN-US"}]{#struct_0_56601_x1470_1446040700}[：]{lang="EN-US" style="font-family:宋体"}[表示支持]{lang="EN-US" style="font-family:宋体"}

[[Active protection mode]{lang="EN-US"}]{#struct_0_56601_x1470_x1392884778}

[[站点的保护倒换模式]{style="font-family:宋体"}]{#struct_0_56601_x1470_2098156555}

[[Protection state on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_x1149356804}

[[站点东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_380876984}[保护状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_1661089026}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SF]{lang="EN-US"}]{#struct_0_56601_x1470_x120043241}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SD]{lang="EN-US"}]{#struct_0_56601_x1470_x1831772607}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS]{lang="EN-US"}]{#struct_0_56601_x1470_114141888}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_x1714296782}[：等待恢复状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_56601_x1470_851233036}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[Protection state on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_x1043914992}

[[站点西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_1099752384}[保护状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_639471646}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SF]{lang="EN-US"}]{#struct_0_56601_x1470_1122968405}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SD]{lang="EN-US"}]{#struct_0_56601_x1470_x1182214255}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS]{lang="EN-US"}]{#struct_0_56601_x1470_1473543752}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_1458940156}[：等待恢复状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_56601_x1470_x637721617}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[Edge state on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_x926612295}

[[站点西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_1808591575}[的]{style="font-family:宋体"}[Edge]{lang="EN-US"}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[dged]{lang="EN-US"}]{#struct_0_56601_x1470_1382782941}[：表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nedged]{lang="EN-US"}]{#struct_0_56601_x1470_1553305055}[：表示没有发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[Edge state on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_x9314769}

[[站点东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x523327768}[的]{style="font-family:宋体"}[Edge]{lang="EN-US"}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[dged]{lang="EN-US"}]{#struct_0_56601_x1470_x657683339}[：表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nedged]{lang="EN-US"}]{#struct_0_56601_x1470_x988900104}[：表示没有发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[Sequence number]{lang="EN-US"}]{#struct_0_56601_x1470_1739801935}

[[TP]{lang="EN-US"}]{#struct_0_56601_x1470_x1514758278}[帧序列号]{style="font-family:宋体"}

[[Last known neighbour on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_x2089411709}

[[西向最后学习到的邻站点]{style="font-family:宋体"}]{#struct_0_56601_x1470_44623649}

[[Last known neighbour on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_1599280601}

[[东向最后学习到的邻站点]{style="font-family:宋体"}]{#struct_0_56601_x1470_302078190}

[[Local topology state]{lang="EN-US"}]{#struct_0_56601_x1470_x1605001188}

[[本站点拓扑状态：]{style="font-family:宋体"}]{#struct_0_56601_x1470_1242965439}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[tart]{lang="EN-US"}]{#struct_0_56601_x1470_x2042357542}[：表示拓扑初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[table]{lang="EN-US"}]{#struct_0_56601_x1470_761267037}[：表示拓扑稳定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nstable]{lang="EN-US"}]{#struct_0_56601_x1470_x963909001}[：表示拓扑不稳定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}[alid]{lang="EN-US"}]{#struct_0_56601_x1470_x1977224852}[：表示拓扑有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[nvalid]{lang="EN-US"}]{#struct_0_56601_x1470_x668568612}[：表示拓扑无效]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1909621685}[显示环路级的拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\>display rpr topology ring]{lang="EN-US"}]{#struct_0_56601_x1470_686525813}

[Ring-level topology information on interface RPR-Router1:]{lang="EN-US"}

[  Number of stations on Ringlet0: 1]{lang="EN-US"}

[  Number of stations on Ringlet1: 1]{lang="EN-US"}

[  Total number of stations on the ring: 2]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Ring topology type: Closed ring]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display rpr topology ring]{lang="EN-US"}]{#struct_0_56601_x1470_2019332396}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1420327334}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_x181399854}

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_x892070831}

[[Ring-level topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1752816318}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_x1636122317}[接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的环路拓扑信息]{style="font-family:宋体"}

[[Number of stations on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x1686061646}

[[站点在西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x1071484771}[上的站点数]{style="font-family:宋体"}

[[Number of stations on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_1021953817}

[[站点在东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x1986621301}[上的站点数]{style="font-family:宋体"}

[[Total number of stations on the ring]{lang="EN-US"}]{#struct_0_56601_x1470_x54883654}

[[站点所在环上总站点数]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2119346645}

[[Jumbo preference]{lang="EN-US"}]{#struct_0_56601_x1470_334237312}

[[是否支持]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_1042821709}[帧：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="PT-BR"}]{#struct_0_56601_x1470_x457001111}[egular]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示不支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[J]{lang="EN-US"}[umbo]{lang="EN-US"}]{#struct_0_56601_x1470_723090697}[：]{lang="EN-US" style="font-family:宋体"}[表示支持]{lang="EN-US" style="font-family:宋体"}

[[Ring topology type]{lang="EN-US"}]{#struct_0_56601_x1470_x23194809}

[[环状态：]{style="font-family:宋体"}]{#struct_0_56601_x1470_1461880793}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[pen ring]{lang="EN-US"}]{#struct_0_56601_x1470_656298699}[：表示开环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}[losed ring]{lang="EN-US"}]{#struct_0_56601_x1470_x1637617016}[：表示闭环]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1446106236}[显示环上所有站点拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\>display rpr topology stations]{lang="EN-US"}]{#struct_0_56601_x1470_x119977705}

[Station topology information on interface RPR-Router1:]{lang="EN-US"}

[ Station entry on Ringlet0:]{lang="EN-US"}

[  MAC address: 00e0-fc00-1a01]{lang="EN-US"}

[  Station name: StationA]{lang="EN-US"}

[  IP address: -]{lang="EN-US"}

[Hops: 1]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Protection mode: Steer]{lang="EN-US"}

[  Protection state on the west span: IDLE]{lang="EN-US"}

[  Protection state on the east span: IDLE]{lang="EN-US"}

[  Edge state on the west span: Unedged]{lang="EN-US"}

[  Edge state on the east span: Unedged]{lang="EN-US"}

[  Sequence number: 9]{lang="EN-US"}

[  Reachability: Reachable]{lang="EN-US"}

[  Valid: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Station entry on Ringlet1:]{lang="EN-US"}

[  MAC address: 00e0-fc00-1a01]{lang="EN-US"}

[  Station name: StationB]{lang="EN-US"}

[  IP address: -]{lang="EN-US"}

[ Hops: 1]{lang="EN-US"}

[  Jumbo preference: Regular]{lang="EN-US"}

[  Protection mode: Steer]{lang="EN-US"}

[  Protection state on the west span: IDLE]{lang="EN-US"}

[  Protection state on the east span: IDLE]{lang="EN-US"}

[  Edge state on the west span: Unedged]{lang="EN-US"}

[  Edge state on the east span: Unedged]{lang="EN-US"}

[  Sequence number: 9]{lang="EN-US"}

[  Reachability: Reachable]{lang="EN-US"}

[  Valid: 1]{lang="EN-US"}

[]{#_Toc118294328}[[表1-16 ]{lang="EN-US"}[display rpr topology stations]{lang="EN-US"}]{#struct_0_56601_x1470_x1563932771}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1421209241}[[字段]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1163019195}

[[描述]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1089479587}

[[Station topology information on interface RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_1756827107}

[[RPR-Router1]{lang="EN-US"}]{#struct_0_56601_x1470_771421131}[接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点所在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环的其它站点的拓扑信息]{style="font-family:宋体"}

[[Station entry on Ringlet0]{lang="EN-US"}]{#struct_0_56601_x1470_x121801022}

[[西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x1819773319}[上邻站点的拓扑信息]{style="font-family:宋体"}

[[Station entry on Ringlet1]{lang="EN-US"}]{#struct_0_56601_x1470_639537182}

[[东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_20563436}[上邻站点的拓扑信息]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_56601_x1470_2144778015}

[[站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_x439100403}[地址]{style="font-family:宋体"}

[[Station name]{lang="EN-US"}]{#struct_0_56601_x1470_1611260432}

[[站点名称]{style="font-family:宋体"}]{#struct_0_56601_x1470_362480997}

[[IP address]{lang="EN-US"}]{#struct_0_56601_x1470_x926546759}

[[站点]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56601_x1470_x1717889016}[地址]{style="font-family:宋体"}

[[Hops]{lang="EN-US"}]{#struct_0_56601_x1470_x1223579035}

[[该站点到本地站点的跳数]{style="font-family:宋体"}]{#struct_0_56601_x1470_x839356964}

[[Jumbo preference]{lang="EN-US"}]{#struct_0_56601_x1470_1182923010}

[[是否支持]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}]{#struct_0_56601_x1470_x657784399}[帧：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="PT-BR"}]{#struct_0_56601_x1470_x523262232}[egular]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示不支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[J]{lang="EN-US"}[umbo]{lang="EN-US"}]{#struct_0_56601_x1470_522316266}[：]{lang="EN-US" style="font-family:宋体"}[表示支持]{lang="EN-US" style="font-family:宋体"}

[[Protection mode]{lang="EN-US"}]{#struct_0_56601_x1470_1618938861}

[[站点的保护倒换模式]{style="font-family:宋体"}]{#struct_0_56601_x1470_x675305253}

[[Protection state on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_782000137}

[[站点西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x2089346173}[的保护状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_1658139520}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SF]{lang="EN-US"}]{#struct_0_56601_x1470_x2042292006}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SD]{lang="EN-US"}]{#struct_0_56601_x1470_x1457237790}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS]{lang="EN-US"}]{#struct_0_56601_x1470_x479178879}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_686591349}[：等待恢复状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_56601_x1470_789288118}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[Protection state on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_x1819755086}

[[站点东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_x772311907}[的保护状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_1910410658}[：强制倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SF]{lang="EN-US"}]{#struct_0_56601_x1470_909128269}[：信号失效状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SD]{lang="EN-US"}]{#struct_0_56601_x1470_x1763799736}[：信号衰减状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MS]{lang="EN-US"}]{#struct_0_56601_x1470_577912136}[：手工倒换状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_56601_x1470_1061269318}[：等待恢复状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_56601_x1470_x204528688}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[Edge state on the west span]{lang="EN-US"}]{#struct_0_56601_x1470_589731363}

[[站点西向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_1312412796}[是否出现]{style="font-family:宋体"}[Edge]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[dged]{lang="EN-US"}]{#struct_0_56601_x1470_1460542322}[：表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nedged]{lang="EN-US"}]{#struct_0_56601_x1470_1449737309}[：表示没有发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[Edge state on the east span]{lang="EN-US"}]{#struct_0_56601_x1470_x1931740050}

[[站点东向]{style="font-family:宋体"}[Span]{lang="EN-US"}]{#struct_0_56601_x1470_713470431}[是否出现]{style="font-family:宋体"}[Edge]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[dged]{lang="EN-US"}]{#struct_0_56601_x1470_429533285}[：表示发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nedged]{lang="EN-US"}]{#struct_0_56601_x1470_x253671145}[：表示没有发生]{lang="EN-US" style="font-family:宋体"}[edge]{lang="EN-US"}

[[Sequence number]{lang="EN-US"}]{#struct_0_56601_x1470_324304436}

[[TP]{lang="EN-US"}]{#struct_0_56601_x1470_x964466462}[帧序列号]{style="font-family:宋体"}

[[Reachability]{lang="EN-US"}]{#struct_0_56601_x1470_x617292564}

[[站点是否可达：]{style="font-family:宋体"}]{#struct_0_56601_x1470_1928980670}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}[eachable]{lang="EN-US"}]{#struct_0_56601_x1470_x270388548}[：表示可达]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nreachable]{lang="EN-US"}]{#struct_0_56601_x1470_505843742}[：表示不可达]{lang="EN-US" style="font-family:宋体"}

[[Valid]{lang="EN-US"}]{#struct_0_56601_x1470_x1097014186}

[[表项是否有效：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1520954928}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x1377736866}[：表示有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_x1381154149}[：表示无效]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 19 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x311958408}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1060240199}[RPR]{lang="EN-US"}[逻辑接口没有与]{style="font-family:KaiTi_GB2312"}[RPR]{lang="EN-US"}[物理接口绑定时，显示本站点拓扑信息时只显示站点名和站点]{style="font-family:KaiTi_GB2312"}[IP]{lang="EN-US"}[。]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_605225464}[RPR]{lang="EN-US"}[逻辑接口没有与]{style="font-family:KaiTi_GB2312"}[RPR]{lang="EN-US"}[物理接口绑定时，站点拓扑信息将无信息显示。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

::::: {#-19641155 .myid}
[]{#_Toc404795734}[]{#struct_0_56601_x1470_2039035106}[]{#_Toc382999913}

**RPR \-- RPR配置命令 \-- flag c2**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x442777197}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_453823091}
:::

[ ]{lang="EN-US"}

[**[flag]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_56601_x1470_954400856}**[c2]{lang="DA"}**[命令用来配置信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **flag**]{lang="EN-US"}]{#struct_0_56601_x1470_x1908341189}[ ]{lang="EN-US"}**[c2]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x971060136}

[**[flag]{lang="DA"}**]{#struct_0_56601_x1470_x1361378916}[ **c2** *flag-value*]{lang="DA"}

[**[undo]{lang="DA"}**]{#struct_0_56601_x1470_x656955672}[ **flag** **c2**]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_962964451}

[[信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}]{#struct_0_56601_x1470_x199000358}[的值为]{style="font-family:宋体"}[0x16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x963435204}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_328820811}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_951765461}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1262422793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x925516650}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_763697160}

[*[flag-value]{lang="EN-US"}*]{#struct_0_56601_x1470_x718567454}[：表示信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x828356837}

[[信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}]{#struct_0_56601_x1470_2071927683}[属于高阶通道开销字节，用于指示虚拟容器]{style="font-family:宋体"}[VC]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Container]{lang="EN-US"}[）帧的复接结构和信息净负荷的性质。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[C2]{lang="EN-US"}]{#struct_0_56601_x1470_1068461628}[字节的配置一定要使收、发两端相匹配，否则会产生告警。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1578420197}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1133824885}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}[为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_182597902}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] flag c2 01]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x230274006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x1998123131}
:::::

::::: {#1143617011 .myid}
[]{#_Toc404795735}[]{#struct_0_56601_x1470_45583102}[]{#_Toc382999914}

**RPR \-- RPR配置命令 \-- flag j0**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_795415730}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_2118981850}
:::

[ ]{lang="EN-US"}

[**[flag]{lang="EN-US"}**]{#struct_0_56601_x1470_733315771}[ ]{lang="EN-US"}**[j0]{lang="DA"}**[命令用来配置]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[帧的再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **flag**]{lang="EN-US"}]{#struct_0_56601_x1470_x374235738}[ ]{lang="EN-US"}**[j0]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1892851797}

[**[flag]{lang="DA"}**]{#struct_0_56601_x1470_416737322}[ **j0** { **sdh** \| **sonet** } *flag-value*]{lang="DA"}

[**[undo]{lang="DA"}**]{#struct_0_56601_x1470_x810115975}[ **flag** **j0** { **sdh** \| **sonet** }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1666133990}

[[系统使用]{style="font-family:宋体"}[SDH]{lang="EN-US"}]{#struct_0_56601_x1470_x608980620}[帧格式的缺省值，]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[的缺省值为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x742854200}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_858472293}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_552897909}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1123796162}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1066864991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_687642632}

[*[flag-value]{lang="EN-US"}*]{#struct_0_56601_x1470_x1171402078}[：表示再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[。]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_56601_x1470_x408109026}[：表示帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Digital Hierarchy]{lang="EN-US"}[，同步数字系列）。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_56601_x1470_x639759792}[：表示帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Optical Network]{lang="EN-US"}[，同步光网络）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1441207033}

[[再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}]{#struct_0_56601_x1470_x1371276018}[属于段开销字节（]{style="font-family:宋体"}[Section Overhead]{lang="EN-US"}[），用于检测两个接口之间的连接在段层次上的连续性。]{style="font-family:宋体"}

[[需要注意的是，在同一个运营者的网络内]{style="font-family:宋体"}[J0]{lang="EN-US"}]{#struct_0_56601_x1470_x1819689550}[字节可为任意字符，而在两个不同运营者的网络边界处要使设备收、发两端的]{style="font-family:宋体"}[J0]{lang="EN-US"}[字节相匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_421518789}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1180539805}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧的再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[为]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_352391906}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] flag j0 sdh ff]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1486404669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x1095916848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[frame-format]{lang="EN-US"}**]{#struct_0_56601_x1470_2033021455}
:::::

::::: {#-1585266344 .myid}
[]{#_Toc404795736}[]{#struct_0_56601_x1470_x440364028}[]{#_Toc382999915}

**RPR \-- RPR配置命令 \-- flag j1**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_577584771}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_149186978}
:::

[ ]{lang="EN-US"}

[**[flag]{lang="EN-US"}**]{#struct_0_56601_x1470_909193805}[ ]{lang="EN-US"}**[j1]{lang="DA"}**[命令用来配置]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[帧的通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **flag**]{lang="EN-US"}]{#struct_0_56601_x1470_x559754549}[ ]{lang="EN-US"}**[j1]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_751771715}

[**[flag]{lang="DA"}**]{#struct_0_56601_x1470_x2059444369}[ **j1** { **sdh** \| **sonet** } *flag-value*]{lang="DA"}

[**[undo]{lang="DA"}**]{#struct_0_56601_x1470_x20315327}[ **flag** **j1** { **sdh** \| **sonet** }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1537702975}

[[系统使用]{style="font-family:宋体"}[SDH]{lang="EN-US"}]{#struct_0_56601_x1470_1921580520}[帧格式的缺省值，]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[的缺省值为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1450849083}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_1839158350}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1312478332}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x545871494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1080326539}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1627045361}

[*[flag-value]{lang="EN-US"}*]{#struct_0_56601_x1470_x1977756140}[：表示通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[。]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_56601_x1470_2030696550}[：表示帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_56601_x1470_868032427}[：表示帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x769956918}

[[通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}]{#struct_0_56601_x1470_x1474306743}[属于高阶通道开销字节，用于检测两个接口之间的连接在通道层次上的连续性。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[J1]{lang="EN-US"}]{#struct_0_56601_x1470_x190137340}[字节的配置一定要使收、发两端相匹配，否则会产生告警。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x803825095}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x253605609}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧的通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[为]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_725134276}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] flag j1 sdh aabbcc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1234510326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x1471540106}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**[ **j1** **ignore**]{lang="EN-US"}]{#struct_0_56601_x1470_x1201580918}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[frame-format]{lang="EN-US"}**]{#struct_0_56601_x1470_1686587327}
:::::

::::: {#1537804201 .myid}
[]{#_Toc404795737}[]{#struct_0_56601_x1470_382850209}[]{#_Toc382999916}[]{#_Hlt12766582}

**RPR \-- RPR配置命令 \-- flag j1 ignore**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x2059922190}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1288174690}
:::

[ ]{lang="EN-US"}

[**[flag]{lang="EN-US"}**[ **j1** **ignore**]{lang="EN-US"}]{#struct_0_56601_x1470_505909278}[命令用来配置忽略对通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[的检查。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **flag** **j1** **ignore**]{lang="EN-US"}]{#struct_0_56601_x1470_x1522783521}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x339791226}

[**[flag]{lang="EN-US"}**[ **j1** **ignore**]{lang="EN-US"}]{#struct_0_56601_x1470_x59412963}

[**[undo]{lang="EN-US"}**[ **flag** **j1** **ignore**]{lang="EN-US"}]{#struct_0_56601_x1470_651430959}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1526339394}

[[需要对通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}]{#struct_0_56601_x1470_989154668}[进行检查。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1072193376}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_1314761094}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1782738910}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1060174663}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x887896684}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x164221268}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1283691831}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[忽略对通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[的检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x196875320}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] flag j1 ignore]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1918338172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**]{#struct_0_56601_x1470_851749407}[ **j1**]{lang="EN-US"}
:::::

::::::: {#596268407 .myid}
[]{#_Toc263323270}[]{#_Toc252280799}[]{#_Toc404795738}[]{#struct_0_56601_x1470_x141365070}[]{#_Toc382999917}

**RPR \-- RPR配置命令 \-- flow-interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x136924381}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x656890136}
:::

[ ]{lang="EN-US"}

[**[flow-interval]{lang="EN-US"}**]{#struct_0_56601_x1470_x1404964081}[命令用来配置接口统计报文信息的时间间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **flow-interval**]{lang="EN-US"}]{#struct_0_56601_x1470_1090918274}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1723092303}

[**[flow-interval]{lang="EN-US"}**[ ]{lang="EN-US"}*[interval]{lang="EN-US"}*]{#struct_0_56601_x1470_2022331406}

[**[undo]{lang="EN-US"}**[ **flow-interval**]{lang="EN-US"}]{#struct_0_56601_x1470_1397988183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1835578038}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1652573873}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1454550034}

[[系统视图]{style="font-family:宋体"}[/RPRGE]{lang="EN-US"}]{#struct_0_56601_x1470_450307181}[接口视图]{style="font-family:宋体"}[/RPRXGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image003.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_1218282368}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_2071993219}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x506946601}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_2081151740}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1504977113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1161472597}

[*[interval]{lang="EN-US"}*]{#struct_0_56601_x1470_x1065387461}[：表示接口统计信息的时间间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x546191482}

[[需要注意的是，系统视图下的全局配置对所有接口都生效，接口视图下的配置只对当前接口生效，如果设备同时支持这两种配置，则全局配置优先生效。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1624865443}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x68212394}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x70070329}[全局配置接口统计报文信息的时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x2851600}

[\[Sysname\] flow-interval 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1373542870}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRGE2/2/0]{lang="EN-US"}[统计报文信息的时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_2119047386}

[\[Sysname\] interface rprge 2/2/0]{lang="EN-US"}

[\[Sysname-RPRGE2/2/0\] flow-interval 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x797283017}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE2/3/0]{lang="EN-US"}[统计报文信息的时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_387631026}

[\[Sysname\] interface rprxge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRXGE2/3/0\] flow-interval 100]{lang="EN-US"}

[[\# ]{lang="NO-BOK"}]{#struct_0_56601_x1470_1597975582}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS]{lang="NO-BOK"}[2/4/0]{lang="EN-US"}[统计报文信息的时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_904705374}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-]{lang="NO-BOK"}[RPRPOS2/4/0]{lang="EN-US"}[\] ]{lang="NO-BOK"}[flow-interval 100]{lang="EN-US"}
:::::::

::::: {#1701559760 .myid}
[]{#_Toc404795739}[]{#struct_0_56601_x1470_x1451955001}[]{#_Toc382999918}

**RPR \-- RPR配置命令 \-- frame-format**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_1609484875}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_552963445}
:::

[ ]{lang="EN-US"}

[**[frame-format]{lang="SV"}**]{#struct_0_56601_x1470_2066108730}[命令用来配置当前接口的帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="SV"}**]{#struct_0_56601_x1470_x1754619377}[ **frame-format**]{lang="SV"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1987055082}

[**[frame-format]{lang="SV"}**]{#struct_0_56601_x1470_x1767215872}[ { **sdh** \| **sonet** }]{lang="SV"}

[**[undo]{lang="SV"}**]{#struct_0_56601_x1470_182669329}[ **frame-format**]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_472682870}

[[接口的帧格式为]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1122975156}[SDH]{lang="SV"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x454616668}

[[RPRPOS]{lang="SV"}]{#struct_0_56601_x1470_1630287659}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x719931504}

[[network-admin]{lang="SV"}]{#struct_0_56601_x1470_x1819886158}

[[mdc-admin]{lang="SV"}]{#struct_0_56601_x1470_x172457311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x860010107}

[**[sdh]{lang="SV"}**]{#struct_0_56601_x1470_1447960672}[：表示]{style="font-family:宋体"}[帧格式为]{style="font-family:宋体"}[SDH]{lang="SV"}[。]{style="font-family:宋体"}

[**[sonet]{lang="SV"}**]{#struct_0_56601_x1470_x950779214}[：表示]{style="font-family:宋体"}[帧格式为]{style="font-family:宋体"}[SONET]{lang="SV"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_2019042026}

[[通过]{style="font-family:宋体"}]{#struct_0_56601_x1470_1772097392}**[flag]{lang="SV"}**[ ]{lang="SV"}**[j0]{lang="DA"}**[和]{style="font-family:宋体"}**[flag]{lang="SV"}**[ ]{lang="SV"}**[j1]{lang="DA"}**[命令配置开销字节时，需要与帧格式匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1262322682}

[[\# ]{lang="SV"}]{#struct_0_56601_x1470_646072316}[配置]{style="font-family:宋体"}[RPR]{lang="SV"}[物理]{style="font-family:
宋体"}[接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="SV"}[的帧格式为]{style="font-family:宋体"}[SONET]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56601_x1470_908997197}

[\[Sysname\] interface rprpos 2/4/0]{lang="SV"}

[\[Sysname-RPRPOS2/4/0\] frame-format sonet]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1804864257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**]{#struct_0_56601_x1470_x1877215919}[ ]{lang="EN-US"}**[j0]{lang="DA"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**]{#struct_0_56601_x1470_453204426}[ ]{lang="EN-US"}**[j1]{lang="DA"}**
:::::

::: {#775541518 .myid}
[]{#_Toc133657450}[]{#_Toc168996361}[]{#_Toc152759631}[]{#_Toc140909788}[]{#_Toc404795740}[]{#struct_0_56601_x1470_x1689047639}

**RPR \-- RPR配置命令 \-- interface**

------------------------------------------------------------------------

[**[interface]{lang="EN-US"}**[ { **rprge** \| **rprpos** \| **rprxge** }]{lang="EN-US"}]{#struct_0_56601_x1470_2050478477}[命令用来进入]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口视图。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ { **rpr-bridge** \| **rpr-router** }]{lang="EN-US"}]{#struct_0_56601_x1470_x229917205}[命令用来创建]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口，并进入]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **interface** { **rpr-bridge** \| **rpr-router** }]{lang="EN-US"}]{#struct_0_56601_x1470_x1133343454}[用来删除已创建的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2084857559}

[**[interface]{lang="EN-US"}**[ { **rprge** \| **rprpos** \| **rprxge** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_x437601024}

[**[interface]{lang="EN-US"}**[ { **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_1312281724}

[**[undo]{lang="EN-US"}**[ **interface** { **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_x115830582}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_292148009}

[[系统视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_262350812}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_2105199703}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1860751237}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x938380458}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1415373367}

[**[rprge]{lang="EN-US"}**]{#struct_0_56601_x1470_242067317}[：表示]{style="font-family:宋体"}[RPRGE]{lang="EN-US"}[接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprpos]{lang="EN-US"}**]{#struct_0_56601_x1470_x253802217}[：表示]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprxge]{lang="EN-US"}**]{#struct_0_56601_x1470_x441906730}[：表示]{style="font-family:宋体"}[RPRXGE]{lang="EN-US"}[接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rpr-bridge]{lang="EN-US"}**]{#struct_0_56601_x1470_1768969744}[：表示二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rpr-router]{lang="EN-US"}**]{#struct_0_56601_x1470_x1379196309}[：表示三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_56601_x1470_x1726017645}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_488394794}

[[如果指定的]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x720781581}[逻辑接口不存在，则]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[ { **rpr-bridge** \| **rpr-router** }]{lang="EN-US"}[命令先完成]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的创建，然后再进入该逻辑接口的视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1440516579}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x837568108}[创建二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_565151564}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[[RPR-Bridge1]{lang="SV"}]{.TerminalDisplayChar}[\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_505712670}[创建三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x905357236}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\]]{lang="EN-US"}

[]{#struct_0_56601_x1470_1034178261}[]{#_Toc274669808}[]{#_Toc274671085}[]{#_Toc274669811}[]{#_Toc274671088}[\# ]{lang="EN-US"}[进入]{style="font-family:
宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRGE2/3/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_970701270}

[\[Sysname\] interface rprge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRGE2/3/0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_45111355}[进入]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE2/3/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1913475733}

[\[Sysname\] interface rprxge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRXGE2/3/0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x264019341}[进入]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x967577569}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\]]{lang="EN-US"}
:::

::::::: {#1002176090 .myid}
[]{#_Toc404795741}[]{#struct_0_56601_x1470_x701214364}[]{#_Toc382999920}

**RPR \-- RPR配置命令 \-- link-delay**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1060371271}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1645028254}
:::

[ ]{lang="EN-US"}

[**[link-delay]{lang="EN-US"}**]{#struct_0_56601_x1470_690751518}[命令用来配置当前接口的物理连接状态抑制时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **link-delay**]{lang="EN-US"}]{#struct_0_56601_x1470_x250590049}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_32371310}

[**[link-delay]{lang="EN-US"}**[ **msec** *milliseconds*]{lang="EN-US"}]{#struct_0_56601_x1470_x1071935358}

[**[undo]{lang="EN-US"}**[ **link-delay**]{lang="EN-US"}]{#struct_0_56601_x1470_x1405954489}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_741336102}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1202882911}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x420448293}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x1130912201}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x657086744}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1349962242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1169179365}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1021079057}

[**[msec]{lang="EN-US"}**[ *milliseconds*]{lang="EN-US"}]{#struct_0_56601_x1470_857083134}[：表示接口物理连接状态的抑制时间，单位为毫秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1357260032}

[[物理连接状态的抑制时间是指在接口发生]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_56601_x1470_1422274934}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[的时候，需要经过连接状态抑制时间后，接口状态才能变为]{style="font-family:宋体"}[up]{lang="EN-US"}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[。使用本命令可以防止短时间内的接口物理连接状态变化对正常业务的影响。]{style="font-family:宋体"}

[[需要注意的是，本命令和]{style="font-family:宋体"}**[dampening]{lang="EN-US"}**]{#struct_0_56601_x1470_1935761843}[命令不能同时使用。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image004.jpg){#图片 3 width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_2114035747}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令对]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_2071796611}[up]{lang="EN-US"}[或]{style="font-family:KaiTi_GB2312"}[down]{lang="EN-US"}[抑制的支持情况与设备的型号有关，请以设备的实际情况为准。即有些设备对]{style="font-family:KaiTi_GB2312"}[up]{lang="EN-US"}[进行抑制，有些设备对]{style="font-family:KaiTi_GB2312"}[down]{lang="EN-US"}[进行抑制，有些设备同时对]{style="font-family:KaiTi_GB2312"}[up/down]{lang="EN-US"}[进行抑制。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x512629752}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_119145248}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的物理连接状态抑制时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1945530107}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] link-delay msec 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1837087949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dampening]{lang="EN-US"}**]{#struct_0_56601_x1470_1256000972}
:::::::

::::: {#988247972 .myid}
[]{#_Toc404795742}[]{#struct_0_56601_x1470_1663902998}[]{#_Toc382999923}

**RPR \-- RPR配置命令 \-- mtu**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 8 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_821443553}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x440239078}
:::

[ ]{lang="EN-US"}

[**[mtu]{lang="EN-US"}**]{#struct_0_56601_x1470_2118850778}[命令用来配置当前接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mtu**]{lang="EN-US"}]{#struct_0_56601_x1470_x1167657053}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1925637634}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_56601_x1470_x797786368}

[**[undo]{lang="EN-US"}**[ **mtu**]{lang="EN-US"}]{#struct_0_56601_x1470_x1574301825}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1546688270}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x87037850}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1617059142}

[[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_1507800421}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x217963805}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x163875535}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1375901488}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_552766837}

[*[size]{lang="EN-US"}*]{#struct_0_56601_x1470_x2090612612}[：表示]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值的大小，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_64480050}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_56601_x1470_283497827}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1473424418}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x530643218}[配置三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1492]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1959372944}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] mtu 1492]{lang="EN-US"}
:::::

::: {#2052875588 .myid}
[]{#_Toc404795743}[]{#struct_0_56601_x1470_x965100762}[]{#_Toc270436479}[]{#_Toc270436542}[]{#_Toc270438135}[]{#_Toc270436481}[]{#_Toc270436544}[]{#_Toc270438137}[]{#_Toc270436482}[]{#_Toc270436545}[]{#_Toc270438138}[]{#_Toc270436483}[]{#_Toc270436546}[]{#_Toc270438139}[]{#_Toc270436484}[]{#_Toc270436547}[]{#_Toc270438140}[]{#_Toc270436485}[]{#_Toc270436548}[]{#_Toc270438141}[]{#_Toc270436486}[]{#_Toc270436549}[]{#_Toc270438142}[]{#_Toc270436487}[]{#_Toc270436550}[]{#_Toc270438143}[]{#_Toc270436488}[]{#_Toc270436551}[]{#_Toc270438144}[]{#_Toc270436489}[]{#_Toc270436552}[]{#_Toc270438145}[]{#_Toc270436490}[]{#_Toc270436553}[]{#_Toc270438146}[]{#_Toc270436491}[]{#_Toc270436554}[]{#_Toc270438147}[]{#_Toc270436492}[]{#_Toc270436555}[]{#_Toc270438148}[]{#_Toc270436493}[]{#_Toc270436556}[]{#_Toc270438149}[]{#_Toc270436494}[]{#_Toc270436557}[]{#_Toc270438150}[]{#_Toc270436495}[]{#_Toc270436558}[]{#_Toc270438151}[]{#_Toc270436496}[]{#_Toc270436559}[]{#_Toc270438152}[]{#_Toc270436497}[]{#_Toc270436560}[]{#_Toc270438153}[]{#_Toc270436500}[]{#_Toc270436563}[]{#_Toc270438156}[]{#_Toc383692244}[]{#_Toc279653570}[]{#_Toc279653572}[]{#_Toc279653573}[]{#_Toc279653574}[]{#_Toc279653576}[]{#_Toc279653577}[]{#_Toc279653578}[]{#_Toc279653580}[]{#_Toc279653581}

**RPR \-- RPR配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **counters** **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x978968389}[命令用来清除]{style="font-family:宋体"}[RPR]{lang="EN-US"}[接口上的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1099997676}

[**[reset]{lang="EN-US"}**[ **counters** **interface** \[ { **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_56601_x1470_1488015843}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1819820622}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_1488266350}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1953194221}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1157344636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1209588468}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1537324886}

[**[rpr-bridge]{lang="EN-US"}**]{#struct_0_56601_x1470_1828352113}[：清除二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rpr-router]{lang="EN-US"}**]{#struct_0_56601_x1470_273489210}[：清除三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprge]{lang="EN-US"}**]{#struct_0_56601_x1470_x407768985}[：清除]{style="font-family:宋体"}[RPRGE]{lang="EN-US"}[接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprpos]{lang="EN-US"}**]{#struct_0_56601_x1470_307861093}[：清除]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[rprxge]{lang="EN-US"}**]{#struct_0_56601_x1470_909062733}[：清除]{style="font-family:宋体"}[RPRXGE]{lang="EN-US"}[接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_56601_x1470_x599463253}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1506723928}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。]{style="font-family:宋体"}]{#struct_0_56601_x1470_2141826795}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_56601_x1470_1848801972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定接口类型和接口编号，将清除所有接口上的统计信息。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1206405266}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了接口类型而未指定接口编号，将清除所有已创建的指定类型接口的统计信息。]{style="font-family:宋体"}]{#struct_0_56601_x1470_91419111}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x344741467}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1719892470}[清除二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface rpr-bridge 1]{lang="EN-US"}]{#struct_0_56601_x1470_1312347260}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x501319199}[清除三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface rpr-router 1]{lang="EN-US"}]{#struct_0_56601_x1470_483854986}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1524248702}[清除]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRGE2/2/0]{lang="EN-US"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface rprge 2/2/0]{lang="EN-US"}]{#struct_0_56601_x1470_x1996695303}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1010815971}[清除]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE2/3/0]{lang="EN-US"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface rprxge 2/3/0]{lang="EN-US"}]{#struct_0_56601_x1470_1516388604}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1748981217}[清除]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface rprpos 2/4/0]{lang="EN-US"}]{#struct_0_56601_x1470_551100259}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1072958195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_56601_x1470_x253736681}
:::

::: {#-1699313974 .myid}
[]{#_Toc404795744}[]{#struct_0_56601_x1470_x2000799982}

**RPR \-- RPR配置命令 \-- reset rpr protection statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **rpr** **protection** **statistics**]{lang="EN-US"}]{#struct_0_56601_x1470_1032987395}[命令用来清除]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的保护事件统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x443828692}

[**[reset]{lang="EN-US"}**[ **rpr** **protection** **statistics** \[ { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_56601_x1470_390575793}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1075804507}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_1982793323}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1721236872}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1910041270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x2073587569}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1132339821}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_925058429}[：清除指定]{style="font-family:
宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的保护事件统计信息。如果未指定本参数，将清除所有]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口对应的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的保护事件统计信息。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_505778206}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_597961596}[清除]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的保护事件统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset rpr protection statistics]{lang="EN-US"}]{#struct_0_56601_x1470_1171030684}
:::

::::: {#1568877003 .myid}
[]{#_Toc404795745}[]{#struct_0_56601_x1470_101659903}

**RPR \-- RPR配置命令 \-- rpr admin-request**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **admin-request**]{lang="EN-US"}]{#struct_0_56601_x1470_x829082434}[命令用来在指定子环上配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[保护请求。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2026182229}

[**[rpr]{lang="EN-US"}**[ **admin-request** { **fs** \| **idle** \| **ms** } { **ringlet0** \| **ringlet1** }]{lang="EN-US"}]{#struct_0_56601_x1470_x256522952}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_505153849}

[[子环上没有配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_564115779}[保护请求。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_67824562}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x895397886}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_2055838311}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1060305735}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1475038090}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x638365888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x2063295678}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x581510002}

[**[fs]{lang="EN-US"}**]{#struct_0_56601_x1470_x2003680054}[：配置]{style="font-family:宋体"}[FS]{lang="EN-US"}[保护请求。]{style="font-family:宋体"}

[**[ms]{lang="EN-US"}**]{#struct_0_56601_x1470_521472926}[：配置]{style="font-family:宋体"}[MS]{lang="EN-US"}[保护请求。]{style="font-family:宋体"}

[**[idle]{lang="EN-US"}**]{#struct_0_56601_x1470_x1602476797}[：配置]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[保护请求。]{style="font-family:宋体"}

[**[ringlet0]{lang="EN-US"}**]{#struct_0_56601_x1470_x1732578534}[：在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上配置保护请求。]{style="font-family:宋体"}

[**[ringlet1]{lang="EN-US"}**]{#struct_0_56601_x1470_1969840220}[：在]{style="font-family:宋体"}[1]{lang="EN-US"}[环上配置保护请求。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1454461638}

[[保护请求包括]{style="font-family:宋体"}[FS]{lang="EN-US"}]{#struct_0_56601_x1470_x657021208}[（]{style="font-family:宋体"}[Forced Switch]{lang="EN-US"}[，强制倒换）、]{style="font-family:宋体"}[MS]{lang="EN-US"}[（]{style="font-family:宋体"}[Manual Switch]{lang="EN-US"}[，手工倒换）和]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[（空闲），优先级从高到低，其中]{style="font-family:宋体"}[FS]{lang="EN-US"}[和]{style="font-family:宋体"}[MS]{lang="EN-US"}[是需要手工配置的。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rpr]{lang="EN-US"}**[ **admin-request** **fs**]{lang="EN-US"}]{#struct_0_56601_x1470_x1753383671}[命令用来产生]{lang="EN-US" style="font-family:宋体"}[FS]{lang="EN-US"}[保护请求。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rpr]{lang="EN-US"}**]{#struct_0_56601_x1470_x890793187}[ **admin-request** **ms**]{lang="EN-US"}[命令用来产生]{style="font-family:宋体"}[MS]{lang="EN-US"}[保护请求。当站点发出]{style="font-family:宋体"}[MS]{lang="EN-US"}[保护请求时，若环上存在优先级更高的保护请求，]{style="font-family:宋体"}[MS]{lang="EN-US"}[保护请求将不被处理。需要指出的是，本地站点物理端口上的]{style="font-family:宋体"}[FS]{lang="EN-US"}[保护请求可以被本地站点相同物理端口上发出的]{style="font-family:宋体"}[MS]{lang="EN-US"}[保护请求抢占。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rpr]{lang="EN-US"}**[ **admin-request** **idle**]{lang="EN-US"}]{#struct_0_56601_x1470_x2016229249}[命令用来清除]{lang="EN-US" style="font-family:宋体"}[FS]{lang="EN-US"}[或者]{lang="EN-US" style="font-family:宋体"}[MS]{lang="EN-US"}[保护请求。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1092239590}

[]{#_Toc133657455}[]{#_Toc168996364}[]{#struct_0_56601_x1470_781368497}[]{#_Toc133657451}[]{#_Toc133657452}[]{#_Toc133657453}[\# ]{lang="EN-US"}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[0]{lang="EN-US"}[环的]{style="font-family:宋体"}[FS]{lang="EN-US"}[保护请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_783793378}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr admin-request fs ringlet0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1803186449}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[0]{lang="EN-US"}[环的]{style="font-family:宋体"}[FS]{lang="EN-US"}[保护请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1348989691}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr admin-request fs ringlet0]{lang="EN-US"}
:::::

::::: {#1721784578 .myid}
[]{#_Toc404795746}[]{#struct_0_56601_x1470_1960322297}

**RPR \-- RPR配置命令 \-- rpr bind**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **bind**]{lang="EN-US"}]{#struct_0_56601_x1470_2071862147}[命令用来配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口与]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口的绑定关系。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **bind**]{lang="EN-US"}]{#struct_0_56601_x1470_x493481800}[命令用来取消]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口与]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x202788470}

[[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x846162340}[逻辑接口视图或三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图下：]{style="font-family:宋体"}

[**[rpr]{lang="EN-US"}**[ **bind** { { **rprge** \| **rprpos** \| **rprxge** } *interface-number* } { **ringlet0** \| **ringlet1** }]{lang="EN-US"}]{#struct_0_56601_x1470_1735993233}

[**[undo]{lang="EN-US"}**[ **rpr** **bind** { { **rprge** \| **rprpos** \| **rprxge** } *interface-number* }]{lang="EN-US"}]{#struct_0_56601_x1470_x15234929}

[[在]{style="font-family:宋体"}[RPRGE]{lang="EN-US"}]{#struct_0_56601_x1470_x1750261138}[接口视图、]{style="font-family:宋体"}[RPRXGE]{lang="EN-US"}[接口视图或]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口视图下：]{style="font-family:宋体"}

[**[rpr]{lang="EN-US"}**[ **bind** { { **rpr-bridge** \| **rpr-router** } *interface-number* } { **ringlet0** \| **ringlet1** }]{lang="EN-US"}]{#struct_0_56601_x1470_472110560}

[**[undo]{lang="EN-US"}**[ **rpr** **bind**]{lang="EN-US"}]{#struct_0_56601_x1470_x663961430}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1557293500}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_2118916314}[逻辑接口与]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口未绑定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_768204944}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x833147470}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/RPRGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRXGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 29 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1110145990}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x99629523}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_104104785}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1668218066}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x777867465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_836258311}

[[{ **rprge** \| **rprpos** \| **rprxge** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_552832373}[：指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口的接口类型和编号。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_56601_x1470_867926220}[：指定]{style="font-family:
宋体"}[RPR]{lang="EN-US"}[逻辑接口的接口类型和编号。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ringlet0]{lang="EN-US"}**]{#struct_0_56601_x1470_x1071237113}[：把在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上接收数据帧、在]{style="font-family:宋体"}[1]{lang="EN-US"}[环上发送数据帧的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口绑定为]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的西向接口。]{style="font-family:宋体"}

[**[ringlet1]{lang="EN-US"}**]{#struct_0_56601_x1470_1262331404}[：把在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上发送数据帧、在]{style="font-family:宋体"}[1]{lang="EN-US"}[环上接收数据帧的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口绑定为]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的东向接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_698861706}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1001408878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_56601_x1470_1037386464}[RPR]{lang="EN-US"}[逻辑接口可以绑定两个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口，一个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口只能绑定一个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_119024646}[站点要正常工作，]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口至少要与一个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口进行绑定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每一个]{style="font-family:宋体"}]{#struct_0_56601_x1470_x805682649}[RPR]{lang="EN-US"}[物理接口都有一]{style="font-family:宋体"}[MATE]{lang="EN-US"}[口，如果两个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口绑定到了同一]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口，那么它们的]{style="font-family:宋体"}[MATE]{lang="EN-US"}[口必须连接起来。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1270483058}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1820017230}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上，将]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[绑定为当前接口的西向接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x326632044}

[\[sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr bind rprpos 2/4/0 ringlet0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_774892244}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上，将]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[绑定为当前接口的西向接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_2013348358}

[\[sysname\] interface rpr-router 1]{lang="EN-US"}

[\[sysname-RPR-Router1\] rpr bind rprpos 2/4/0 ringlet0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x562586412}[在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[上，将当前接口绑定为二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[的东向接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1080089797}

[\[sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[sysname-RPRPOS2/4/0\] rpr bind rpr-bridge 1 ringlet1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1260865324}[在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[上，将当前接口绑定为三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[的东向接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_908866125}

[\[sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[sysname-RPRPOS2/4/0\] rpr bind rpr-router 1 ringlet1]{lang="EN-US"}
:::::

::::: {#-1750918657 .myid}
[]{#_Toc404795747}[]{#struct_0_56601_x1470_1445661038}

**RPR \-- RPR配置命令 \-- rpr default-rs ringlet1**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **default-rs** **ringlet1**]{lang="EN-US"}]{#struct_0_56601_x1470_x1638287316}[命令用来配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[的默认选环为]{style="font-family:宋体"}[1]{lang="EN-US"}[环。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **default-rs**]{lang="EN-US"}]{#struct_0_56601_x1470_x49515368}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1609811913}

[**[rpr]{lang="EN-US"}**[ **default-rs** **ringlet1**]{lang="EN-US"}]{#struct_0_56601_x1470_x1165715587}

[**[undo]{lang="EN-US"}**[ **rpr** **default-rs**]{lang="EN-US"}]{#struct_0_56601_x1470_426308461}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2090856138}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_829114237}[的默认选环为]{style="font-family:宋体"}[0]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_823101732}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x436547375}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x167803738}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1312150652}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_293602571}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_3850644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1189561000}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1880954006}

[[默认选环就是指数据帧的缺省发送子环。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2019855532}

[[需要注意的是，当配置的默认选环因故障而不具备数据转发能力时，未发送故障的另一子环将成为生效的默认选还；而当两个子环都发生故障时，系统仍会把配置的默认选环视为生效的默认选环。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1421935718}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1642190057}

[]{#_Toc133657456}[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1288092743}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[的默认选环为]{style="font-family:宋体"}[1]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x2086279474}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr default-rs ringlet1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x253933289}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[的默认选环为]{style="font-family:宋体"}[1]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1125684517}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr default-rs ringlet1]{lang="EN-US"}
:::::

::::: {#1045840258 .myid}
[]{#_Toc404795748}[]{#struct_0_56601_x1470_660300081}

**RPR \-- RPR配置命令 \-- rpr echo mac**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **echo** **mac**]{lang="EN-US"}]{#struct_0_56601_x1470_x1454373277}[命令用来检测当前站点与目的站点之间的连通性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1018483108}

[**[rpr]{lang="EN-US"}**[ **echo** **mac** *mac-address* \[ **-c** *c-value* \| **-r** { **reverse** \| **ringlet0** \| **ringlet1** } \| **-s** { **ringlet0** \| **ringlet1** } \| **-t** *t-value* \] \*]{lang="EN-US"}]{#struct_0_56601_x1470_590128848}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_136230920}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_1274684338}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_274532142}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1237406898}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x678145460}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_505581598}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1179896726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1663635549}

[*[mac-address]{lang="EN-US"}*]{#struct_0_56601_x1470_x424319950}[：检测到达该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的目的站点的连通性。]{style="font-family:宋体"}

[**[-c]{lang="EN-US"}**[ *c-value*]{lang="EN-US"}]{#struct_0_56601_x1470_x980280721}[：指定发送的]{style="font-family:宋体"}[Echo Request]{lang="EN-US"}[报文的数量，]{style="font-family:宋体"}*[c-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[**[-r]{lang="EN-US"}**]{#struct_0_56601_x1470_x791526330}[：指定目点站点发送]{style="font-family:宋体"}[Echo Response]{lang="EN-US"}[报文的发送子环，取值为]{style="font-family:宋体"}**[reverse]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ringlet0]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ringlet1]{lang="EN-US"}**[。]{style="font-family:宋体"}**[reverse]{lang="EN-US"}**[表示目的站点将从与接收]{style="font-family:宋体"}[Echo Request]{lang="EN-US"}[报文子环的反方向子环发送]{style="font-family:宋体"}[Echo Response]{lang="EN-US"}[报文，缺省的发送环为实际生效的默认子环。例如，当目的站点从]{style="font-family:宋体"}[0]{lang="EN-US"}[环接收]{style="font-family:宋体"}[Echo Request]{lang="EN-US"}[报文时，则会从]{style="font-family:宋体"}[1]{lang="EN-US"}[环发送]{style="font-family:宋体"}[Echo Response]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[-s]{lang="EN-US"}**]{#struct_0_56601_x1470_x1634070724}[：指定发送]{style="font-family:宋体"}[Echo Request]{lang="EN-US"}[报文的子环，取值为]{style="font-family:宋体"}**[ringlet0]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ringlet1]{lang="EN-US"}**[，缺省的发送环为实际生效的默认子环。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}**[ *t-value*]{lang="EN-US"}]{#struct_0_56601_x1470_550135907}[：指定站点等待目的站点应答的超时时间，]{style="font-family:宋体"}*[t-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1463210892}

[[如果当前站点在指定子环上发送的]{style="font-family:宋体"}[Echo Request]{lang="EN-US"}]{#struct_0_56601_x1470_x1060502343}[报文目的站点可以接收到，且目的站点在指定子环上发送的]{style="font-family:宋体"}[Echo Response]{lang="EN-US"}[报文当前站点也可以接收到，即只有当前站点和目的站点同时在指定发送子环和指定接收子环上连接正常时，则认为当前站点与目的站点之间连通，否则认为出现故障。]{style="font-family:宋体"}

[[需要注意的是，如果没有指定发送子环和接收子环，源站点将根据综合选环表选择相应的子环发送]{style="font-family:宋体"}[Echo Request]{lang="EN-US"}]{#struct_0_56601_x1470_76389808}[报文，目的站点也将根据综合选环表选择相应的子环发送]{style="font-family:宋体"}[Echo Response]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1303968607}

[]{#_Toc133657457}[]{#struct_0_56601_x1470_x456434036}[]{#_Hlt12095531}[\# ]{lang="EN-US"}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上检测到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0012-3F83-A1E3]{lang="EN-US"}[的目的站点的连通性，指定的发送子环为]{style="font-family:宋体"}[0]{lang="EN-US"}[环、接收子环为]{style="font-family:宋体"}[1]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1620631522}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr echo mac 0012-3F83-A1E3 -s ringlet0 -r ringlet1]{lang="EN-US"}

[Ping 0012-3F83-A1E3: press CTRL+C to break]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=2 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=3 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=4 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=5 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=6 time=1 ms ]{lang="EN-US"}

[\-\-- Ping statistics for 0012-3F83-A1E3 \-\--]{lang="EN-US"}

[    5 packet(s) transmitted]{lang="EN-US"}

[    5 packet(s) received]{lang="EN-US"}

[    0.0% packet loss]{lang="EN-US"}

[    Round-trip min/avg/max = 1/1/1 ms]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1189077177}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上检测到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0012-3F83-A1E3]{lang="EN-US"}[的目的站点的连通性，指定的发送子环为]{style="font-family:宋体"}[0]{lang="EN-US"}[环、接收子环为]{style="font-family:宋体"}[1]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x657217816}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr echo mac 0012-3F83-A1E3 -s ringlet0 -r ringlet1]{lang="EN-US"}

[Ping 0012-3F83-A1E3: press CTRL+C to break]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=2 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=3 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=4 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=5 time=1 ms]{lang="EN-US"}

[   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=6 time=1 ms ]{lang="EN-US"}

[\-\-- Ping statistics for 0012-3F83-A1E3 \-\--]{lang="EN-US"}

[    5 packet(s) transmitted]{lang="EN-US"}

[    5 packet(s) received]{lang="EN-US"}

[    0.0% packet loss]{lang="EN-US"}

[    Round-trip min/avg/max = 1/1/1 ms]{lang="EN-US"}
:::::

::::: {#849869593 .myid}
[]{#_Toc404795749}[]{#struct_0_56601_x1470_957596074}[]{#_Toc353461126}

**RPR \-- RPR配置命令 \-- rpr mac-address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x445950981}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_357634491}[]{#_Toc353461147}
:::

[ ]{lang="EN-US"}

[**[rpr]{lang="EN-US"}**[ **mac-address**]{lang="EN-US"}]{#struct_0_56601_x1470_x934936946}[命令用来向]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}[地址表中添加表项，使到达指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[目的站点的数据帧被单播到指定环上站点下环。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **mac-address**]{lang="EN-US"}]{#struct_0_56601_x1470_950401470}[命令用来删除指定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_241177565}[]{#_Toc353461127}

[**[rpr]{lang="EN-US"}**[ **mac-address** { **dynamic** \| **static** } **destination** *mac-address1* **vlan** *vlan-id* **ring** *mac-address2*]{lang="EN-US"}]{#struct_0_56601_x1470_2071665539}[]{#_Toc353461128}

[**[undo]{lang="EN-US"}**[ **rpr** **mac-address** \[ **dynamic** \| **static** \] \[ **destination** *mac-address1* \] \[ **vlan** *vlan-id* \] \[ **ring** *mac-address2* \]]{lang="EN-US"}]{#struct_0_56601_x1470_1471383192}[]{#_Toc353461129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_776579518}

[[没有配置]{style="font-family:宋体"}[RPR MAC]{lang="EN-US"}]{#struct_0_56601_x1470_2016968831}[地址表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_375692336}[]{#_Toc353461130}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x818954832}[逻辑接口视图]{style="font-family:宋体"}[]{#_Toc353461131}[]{#_Toc353461132}[]{#_Toc353461134}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2081774227}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x728625924}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x92101690}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x492955842}[]{#_Toc353461137}

[**[dynamic]{lang="EN-US"}**]{#struct_0_56601_x1470_2118719706}[：添加]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[]{#_Toc353461139}

[**[static]{lang="EN-US"}**]{#struct_0_56601_x1470_763177154}[：添加]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[]{#_Toc353461138}

[*[mac-address1]{lang="EN-US"}*]{#struct_0_56601_x1470_x693270992}[：目的以太网]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}[]{#_Toc353461140}

[*[mac-address2]{lang="EN-US"}*]{#struct_0_56601_x1470_79373691}[：下环站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}[]{#_Toc353461141}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_56601_x1470_1253455060}[：目的以太网]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[]{#_Toc353461142}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_332717444}[]{#_Toc353461143}

[[需要注意的是，下环站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_56601_x1470_1610766551}[地址必须为环上站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，才能新增一条有效的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[]{#_Toc353461145}

[]{#struct_0_56601_x1470_x1214976524}[]{#_Toc353461146}[]{#_Toc353461148}[【举例】]{style="font-family:
黑体"}[]{#_Toc353461150}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x95684187}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上添加如下]{style="font-family:宋体"}[RPR]{lang="EN-US"}[静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项：目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0011-43CA-7D45]{lang="EN-US"}[，属于]{style="font-family:宋体"}[VLAN 5]{lang="EN-US"}[，下环站点的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2256-38B8-D92C]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc353461151}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_552635765}[]{#_Toc353461152}

[\[Sysname\] interface rpr-bridge 1[]{#_Toc353461153}]{lang="EN-US"}

[\[Sysname-RPR-Bridge1\] rpr mac-address static destination 0011-43ca-7d45 vlan 5 ring 2256-38b8-d92c]{lang="EN-US"}[]{#_Toc353461154}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2098221474}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **rpr** **mac-address**]{lang="EN-US"}]{#struct_0_56601_x1470_1536975241}
:::::

::::: {#607747308 .myid}
[]{#_Toc404795750}[]{#struct_0_56601_x1470_413650160}[]{#_Toc353461155}[]{#_Toc367885345}[]{#_Toc367975090}[]{#_Toc367975510}[]{#_Toc367976422}[]{#_Toc369006482}[]{#_Toc369007654}[]{#_Toc369177337}[]{#_Toc353461156}[]{#_Toc367885346}[]{#_Toc367975091}[]{#_Toc367975511}[]{#_Toc367976423}[]{#_Toc369006483}[]{#_Toc369007655}[]{#_Toc369177338}[]{#_Toc353461157}[]{#_Toc367885347}[]{#_Toc367975092}[]{#_Toc367975512}[]{#_Toc367976424}[]{#_Toc369006484}[]{#_Toc369007656}[]{#_Toc369177339}[]{#_Toc353461158}[]{#_Toc367885348}[]{#_Toc367975093}[]{#_Toc367975513}[]{#_Toc367976425}[]{#_Toc369006485}[]{#_Toc369007657}[]{#_Toc369177340}[]{#_Toc353461159}

**RPR \-- RPR配置命令 \-- rpr mac-address timer**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x515273824}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_463631399}
:::

**[ ]{lang="EN-US"}**

[**[rpr]{lang="EN-US"}**[ **mac-address** **timer**]{lang="EN-US"}]{#struct_0_56601_x1470_93549724}[命令用来配置]{style="font-family:
宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项是否老化及老化时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **mac-address** **timer**]{lang="EN-US"}]{#struct_0_56601_x1470_x81777393}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1867352846}[]{#_Toc353461160}

[**[rpr]{lang="EN-US"}**[ **mac-address** **timer** { **aging** *seconds* \| **no-aging** }]{lang="EN-US"}]{#struct_0_56601_x1470_1665722622}[]{#_Toc353461161}

[**[undo]{lang="EN-US"}**[ **rpr** **mac-address** **timer** **aging**]{lang="EN-US"}]{#struct_0_56601_x1470_1812937886}[]{#_Toc353461162}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1571522399}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x731312312}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x177812602}[]{#_Toc353461163}

[[系统视图]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1819951694}[]{#_Toc353461164}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x158114355}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1010048919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1915857404}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1557559480}[]{#_Toc353461167}

[**[aging]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_56601_x1470_x1849076558}[：]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项的老化定时器的值，]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[85899]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[]{#_Toc353461168}

[**[no-aging]{lang="EN-US"}**]{#struct_0_56601_x1470_x1832116154}[：配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项不老化。]{style="font-family:宋体"}[]{#_Toc353461169}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1337404263}[]{#_Toc353461177}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x996720087}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表表项的老化时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}[]{#_Toc353461178}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_908931661}[]{#_Toc353461179}

[\[Sysname\] rpr mac-address timer aging 600]{lang="EN-US"}[]{#_Toc353461180}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_678723284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **rpr** **mac-address** **aging-time**]{lang="EN-US"}]{#struct_0_56601_x1470_x979931016}
:::::

::::::: {#-1345714565 .myid}
[]{#_Toc133657459}[]{#_Toc404795751}[]{#struct_0_56601_x1470_x339767734}

**RPR \-- RPR配置命令 \-- rpr mate smart-connect**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x4029208}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_2076709546}
:::

[ ]{lang="EN-US"}

[**[rpr]{lang="EN-US"}**[ **mate** **smart-connect**]{lang="EN-US"}]{#struct_0_56601_x1470_733220600}[命令用来使能]{style="font-family:宋体"}[RPR MATE]{lang="EN-US"}[口的智能连接功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **mate** **smart-connect**]{lang="EN-US"}]{#struct_0_56601_x1470_x774499811}[用来关闭]{style="font-family:宋体"}[RPR MATE]{lang="EN-US"}[口的智能连接功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x499521268}

[**[rpr]{lang="EN-US"}**[ **mate** **smart-connect**]{lang="EN-US"}]{#struct_0_56601_x1470_x1432637075}

[**[undo]{lang="EN-US"}**[ **rpr** **mate** **smart-connect**]{lang="EN-US"}]{#struct_0_56601_x1470_2127438121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1434727235}

[[RPR MATE]{lang="EN-US"}]{#struct_0_56601_x1470_1312216188}[口的智能连接功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x125571435}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x530418221}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x51607700}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x491829677}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_339283251}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x665426548}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1418190057}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1855587595}

[[通过使能]{style="font-family:宋体"}[RPR MATE]{lang="EN-US"}]{#struct_0_56601_x1470_x1469909958}[口的智能连接功能，当两个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口在同一个子卡上时，]{style="font-family:宋体"}[RPR]{lang="EN-US"}[会自动把两个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口的]{style="font-family:宋体"}[MATE]{lang="EN-US"}[口通过内部部件连接起来，不再需要将这两个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口的]{style="font-family:宋体"}[MATE]{lang="EN-US"}[口用光纤在外部连接起来。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x253867753}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1514717899}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[RPR MATE]{lang="EN-US"}[口的智能连接功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1992456549}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr mate smart-connect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1992081061}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[RPR MATE]{lang="EN-US"}[口的智能连接功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1166760439}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr mate smart-connect]{lang="EN-US"}
:::::::

::::::: {#-296684771 .myid}
[]{#_Toc404795752}[]{#struct_0_56601_x1470_x38972562}

**RPR \-- RPR配置命令 \-- rpr port-type**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 39 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x83588074}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1120002835}
:::

[ ]{lang="EN-US"}

[**[rpr]{lang="EN-US"}**[ **port-type**]{lang="EN-US"}]{#struct_0_56601_x1470_x1403773673}[命令用来改变]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口的类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_505647134}

[**[rpr]{lang="FR"}**]{#struct_0_56601_x1470_975347706}[ **port-type** { **10ge** \| **10gpos** }]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1332932107}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1260115197}[物理接口的类型与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_858363585}

[[RPRXGE]{lang="EN-US"}]{#struct_0_56601_x1470_1794496474}[接口视图]{style="font-family:宋体"}[/RPRPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 38 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_854016349}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x794105621}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1105558668}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1468776214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1060436807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1375654710}

[**[10ge]{lang="EN-US"}**]{#struct_0_56601_x1470_2014840624}[：表示]{style="font-family:宋体"}[10GE]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[10gpos]{lang="EN-US"}**]{#struct_0_56601_x1470_1667495838}[：表示]{style="font-family:宋体"}[10GPOS]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_2037815889}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1464090477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[改变]{style="font-family:宋体"}]{#struct_0_56601_x1470_223314028}[RPR]{lang="EN-US"}[物理接口的类型后接口板会自动重启并切换到新类型，该接口上的原有配置将丢失；如果该接口原先被分配给非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，在接口类型切换后该接口会被归还给缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，请重新进行配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令仅对]{style="font-family:宋体"}]{#struct_0_56601_x1470_991103041}[10GE]{lang="EN-US"}[和]{style="font-family:宋体"}[10GPOS]{lang="EN-US"}[的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口起作用，若对]{style="font-family:宋体"}[GE]{lang="EN-US"}[或]{style="font-family:宋体"}[2.5GPOS]{lang="EN-US"}[的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口执行本命令将返回错误提示信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1068835500}

[[\# ]{lang="FR"}]{#struct_0_56601_x1470_x1958831669}[改变]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE]{lang="FR"}[2/3/0]{lang="EN-US"}[的类型为]{style="font-family:宋体"}[10GPOS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x657152280}

[\[Sysname\] interface rprxge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRXGE]{lang="FR"}[2/3/0]{lang="EN-US"}[\] rpr port-type 10gpos]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_56601_x1470_x185530169}[改变]{style="font-family:宋体"}[RPR]{lang="FR"}[物理接口]{style="font-family:
宋体"}[RPRPOS2/4/0]{lang="FR"}[的类型为]{style="font-family:宋体"}[10GE]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_56601_x1470_777274573}

[\[Sysname\] interface rprpos 2/4/0]{lang="FR"}

[\[Sysname-RPRPOS2/4/0\] rpr port-type 10ge]{lang="FR"}
:::::::

::::: {#1645565123 .myid}
[]{#_Toc404795753}[]{#struct_0_56601_x1470_1082554509}[]{#_Toc133657460}

**RPR \-- RPR配置命令 \-- rpr protect-mode wrap**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **protect-mode** **wrap**]{lang="EN-US"}]{#struct_0_56601_x1470_1870022971}[命令用来配置站点的保护倒换模式为]{style="font-family:宋体"}[Wrapping]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **protect-mode**]{lang="EN-US"}]{#struct_0_56601_x1470_x1920262590}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_640459139}

[**[rpr]{lang="NL"}**]{#struct_0_56601_x1470_76577330}[ **protect-mode** **wrap**]{lang="NL"}

[**[undo]{lang="EN-US"}**[ **rpr** **protect-mode**]{lang="EN-US"}]{#struct_0_56601_x1470_2071731075}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2039368751}

[[站点的保护倒换模式为]{style="font-family:宋体"}[Steering]{lang="EN-US"}]{#struct_0_56601_x1470_x1902691762}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1810407376}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_1644329273}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_1704156524}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x689894142}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x559409195}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1467491022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1675835419}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1003840627}

[]{#_Toc133657461}[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_2118785242}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置本站点的保护倒换模式为]{style="font-family:宋体"}[Wrapping]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1147098714}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr protect-mode wrap]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1409607853}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上配置本站点的保护倒换模式为]{style="font-family:宋体"}[Wrapping]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1814593164}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysnamey-RPR-Router1\] rpr protect-mode wrap]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1950159823}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **rpr** **protection**]{lang="EN-US"}]{#struct_0_56601_x1470_x538606917}
:::::

::::: {#-1821441635 .myid}
[]{#_Toc404795754}[]{#struct_0_56601_x1470_x207750753}

**RPR \-- RPR配置命令 \-- rpr rate-limit**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **rate-limit**]{lang="EN-US"}]{#struct_0_56601_x1470_1697706370}[命令用来配置站点各类业务在指定子环上的预留带宽或速率限制。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **rate-limit**]{lang="EN-US"}]{#struct_0_56601_x1470_x1381285510}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_552701301}

[**[rpr]{lang="EN-US"}**[ **rate-limit** { **high** \| **low** \| **medium** \| **reserved** } { **ringlet0** \| **ringlet1** } *value*]{lang="EN-US"}]{#struct_0_56601_x1470_x144277331}

[**[undo]{lang="EN-US"}**[ **rpr** **rate-limit** { **high** \| **low** \| **medium** \| **reserved** } { **ringlet0** \| **ringlet1** }]{lang="EN-US"}]{#struct_0_56601_x1470_401721762}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x368220927}

[[A0]{lang="EN-US"}]{#struct_0_56601_x1470_x775151456}[类业务的预留带宽占总带宽的]{style="font-family:宋体"}[0]{lang="EN-US"}[‰，]{style="font-family:宋体"}[A1]{lang="EN-US"}[类业务的速率限制值为]{style="font-family:宋体"}[2]{lang="EN-US"}[‰，]{style="font-family:宋体"}[B-CIR]{lang="EN-US"}[类业务的速率限制值为]{style="font-family:宋体"}[0]{lang="EN-US"}[‰，]{style="font-family:宋体"}[B-EIR]{lang="EN-US"}[类业务和]{style="font-family:宋体"}[C]{lang="EN-US"}[类业务的速率限制值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[‰。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1384411813}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_1227388640}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x191244073}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1908865000}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1896835561}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1276267140}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x607382993}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1381955615}

[**[high]{lang="EN-US"}**]{#struct_0_56601_x1470_x1953645134}[：表示]{style="font-family:宋体"}[A1]{lang="EN-US"}[类业务。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_56601_x1470_1325005065}[：表示]{style="font-family:宋体"}[B-EIR]{lang="EN-US"}[和]{style="font-family:宋体"}[C]{lang="EN-US"}[类业务。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_56601_x1470_542889493}[：表示]{style="font-family:宋体"}[B-CIR]{lang="EN-US"}[类业务。]{style="font-family:宋体"}

[**[reserved]{lang="EN-US"}**]{#struct_0_56601_x1470_1812287241}[：表示]{style="font-family:宋体"}[A0]{lang="EN-US"}[类业务。]{style="font-family:宋体"}

[**[ringlet0]{lang="EN-US"}**]{#struct_0_56601_x1470_355236358}[：表示各类业务在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上的预留带宽或速率限制。]{style="font-family:宋体"}

[**[ringlet1]{lang="EN-US"}**]{#struct_0_56601_x1470_1953480292}[：表示各类业务在]{style="font-family:宋体"}[1]{lang="EN-US"}[环上的预留带宽或速率限制。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_56601_x1470_1166156948}[：]{style="font-family:宋体"}[A0]{lang="EN-US"}[类业务预留带宽占总带宽的千分比或]{style="font-family:宋体"}[B]{lang="EN-US"}[、]{style="font-family:宋体"}[C]{lang="EN-US"}[类业务的速率限制值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为千分之一。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x810610861}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_56601_x1470_x268971295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置了]{style="font-family:宋体"}]{#struct_0_56601_x1470_x2088200627}[A0]{lang="EN-US"}[类业务的站点，为]{style="font-family:宋体"}[A0]{lang="EN-US"}[类业务预留的带宽总和不能超过环路带宽（即]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑口的带宽）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[这里的]{style="font-family:宋体"}]{#struct_0_56601_x1470_x904183484}[0]{lang="EN-US"}[环、]{style="font-family:宋体"}[1]{lang="EN-US"}[环都是指发送子环。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1670874052}

[]{#_Toc133657463}[]{#struct_0_56601_x1470_802955379}[]{#_Toc133657462}[\# ]{lang="EN-US"}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置站点]{style="font-family:宋体"}[A0]{lang="EN-US"}[类业务在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上的预留带宽占总带宽的]{style="font-family:宋体"}[5]{lang="EN-US"}[‰。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_775238221}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr rate-limit reserved ringlet0 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x942661134}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上配置站点]{style="font-family:宋体"}[A0]{lang="EN-US"}[类业务在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上的预留带宽占总带宽的]{style="font-family:宋体"}[5]{lang="EN-US"}[‰。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_211846696}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr rate-limit reserved ringlet0 5]{lang="EN-US"}
:::::

::::: {#1149289146 .myid}
[]{#_Toc404795755}[]{#struct_0_56601_x1470_x1616453028}

**RPR \-- RPR配置命令 \-- rpr reversion-mode non-revertive**

------------------------------------------------------------------------

[**[rpr]{lang="FR"}**]{#struct_0_56601_x1470_x1526256874}[ **reversion-mode** **non-revertive**]{lang="FR"}[命令用来配置站点上保护倒换的恢复模式为不可恢复模式。]{style="font-family:宋体"}**[undo]{lang="FR"}**[ **rpr** **reversion-mode**]{lang="FR"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x4591279}

[**[rpr]{lang="FR"}**]{#struct_0_56601_x1470_x763567220}[ **reversion-mode** **non-revertive**]{lang="FR"}

[**[undo]{lang="FR"}**]{#struct_0_56601_x1470_542069091}[ **rpr** **reversion-mode**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x322231391}

[[站点上保护倒换的恢复模式为可恢复模式。]{style="font-family:宋体"}]{#struct_0_56601_x1470_231634248}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_816713427}

[[二层]{style="font-family:宋体"}]{#struct_0_56601_x1470_1927430117}[RPR]{lang="FR"}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="FR"}[三层]{style="font-family:宋体"}[RPR]{lang="FR"}[逻辑接口视图]{style="font-family:
宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_1178522748}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x833544810}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1838084087}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x665485290}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_617179219}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x712704088}

[]{#_Toc133657464}[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1580554957}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上，将站点上保护倒换的恢复模式配置为不可恢复模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1727947957}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr reversion-mode non-revertive]{lang="FR"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_870170144}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上，将站点上保护倒换的恢复模式配置为不可恢复模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1561637382}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr reversion-mode non-revertive]{lang="FR"}
:::::

::::: {#-964793382 .myid}
[]{#_Toc404795756}[]{#struct_0_56601_x1470_x1139833906}

**RPR \-- RPR配置命令 \-- rpr static-rs**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **static-rs**]{lang="EN-US"}]{#struct_0_56601_x1470_x387561193}[命令用来添加静态选环表项信息，使到达指定目的站点的数据帧通过指定子环发送。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rpr** **static-rs**]{lang="EN-US"}[命令用来删除到指定目的站点的静态选环表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x656885393}

[**[rpr]{lang="EN-US"}**[ **static-rs** *mac-address* { **ringlet0** \| **ringlet1** }]{lang="EN-US"}]{#struct_0_56601_x1470_x1788040178}

[**[undo]{lang="EN-US"}**[ **rpr** **static-rs** *mac-address*]{lang="EN-US"}]{#struct_0_56601_x1470_588534455}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_274938114}

[[不存在静态选环表项信息。]{style="font-family:宋体"}]{#struct_0_56601_x1470_841722696}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1888548828}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1433317589}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x835405279}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1914477457}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_371953694}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1645156799}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1461755731}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1446287989}

[**[ringlet0]{lang="EN-US"}**]{#struct_0_56601_x1470_x566625015}[：到指定目的站点的数据帧通过]{style="font-family:宋体"}[0]{lang="EN-US"}[环发送。]{style="font-family:宋体"}

[**[ringlet1]{lang="EN-US"}**]{#struct_0_56601_x1470_x320182131}[：到指定目的站点的数据帧通过]{style="font-family:宋体"}[1]{lang="EN-US"}[环发送。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_56601_x1470_x1991054838}[：目的站点]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1957963764}

[]{#_Toc133657465}[]{#_Toc114488721}[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1019558373}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0001-0002-0003]{lang="EN-US"}[的目的站点的数据帧走]{style="font-family:宋体"}[0]{lang="EN-US"}[环，到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0001-0002-0004]{lang="EN-US"}[的目的站点的数据帧走]{style="font-family:宋体"}[1]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_192510211}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-RPR-Bridge1\] rpr static-rs 0001-0002-0003 ringlet0]{lang="EN-US"}

[\[Sysname-RPR-Bridge1\] rpr static-rs 0001-0002-0004 ringlet1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1194130247}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上配置到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0001-0002-0003]{lang="EN-US"}[的目的站点的数据帧走]{style="font-family:宋体"}[0]{lang="EN-US"}[环，到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0001-0002-0004]{lang="EN-US"}[的目的站点的数据帧走]{style="font-family:宋体"}[1]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_505948826}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr static-rs 0001-0002-0003 ringlet0]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr static-rs 0001-0002-0004 ringlet1]{lang="EN-US"}
:::::

::::: {#2090528835 .myid}
[]{#_Toc404795757}[]{#struct_0_56601_x1470_x1197557393}

**RPR \-- RPR配置命令 \-- rpr station-name**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **station-name**]{lang="EN-US"}]{#struct_0_56601_x1470_52189856}[命令用来配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的名称。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **station-name**]{lang="EN-US"}]{#struct_0_56601_x1470_202330798}[命令用来删除已存在的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2081050071}

[**[rpr]{lang="EN-US"}**[ **station-name** *station-name*]{lang="EN-US"}]{#struct_0_56601_x1470_x733388462}

[**[undo]{lang="EN-US"}**[ **rpr** **station-name**]{lang="EN-US"}]{#struct_0_56601_x1470_2028308259}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_546950031}

[[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1451932882}[站点没有配置任何名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1058289674}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1941416559}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x790845720}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x840530821}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2141908691}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x252961984}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1605271973}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x688119487}

[*[station-name]{lang="EN-US"}*]{#struct_0_56601_x1470_292623393}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[站点的名称，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_672564461}

[]{#_Toc133657466}[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1336589625}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置本站点的名称为]{style="font-family:宋体"}[ABC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1938037635}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr station-name ABC]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1426110283}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上配置本站点的名称为]{style="font-family:宋体"}[ABC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_70595513}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr station-name ABC]{lang="EN-US"}
:::::

::::: {#1682696413 .myid}
[]{#_Toc404795758}[]{#struct_0_56601_x1470_1985091802}

**RPR \-- RPR配置命令 \-- rpr timer**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_56601_x1470_538045453}[命令用来配置各类]{style="font-family:宋体"}[RPR]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **timer**]{lang="EN-US"}]{#struct_0_56601_x1470_1264204127}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x629987720}

[**[rpr]{lang="EN-US"}**[ **timer** { **atd** *atd-value* \| **holdoff** *holdoff-value* \| **keepalive** *keepalive-value* \| **stability** *stability-value* \| **tc-fast** *tc-fast-value* \| **tc-slow** *tc-slow-value* \| **tp-fast** *tp-fast-value* \| **tp-slow** *tp-slow-value* \| **wtr** *wtr-value* }]{lang="EN-US"}]{#struct_0_56601_x1470_x249066205}

[**[undo]{lang="EN-US"}**[ **rpr** **timer** { **atd** \| **holdoff** \| **keepalive** \| **stability** \| **tc-fast** \| **tc-slow** \| **tp-fast** \| **tp-slow** \| **wtr** }]{lang="EN-US"}]{#struct_0_56601_x1470_2116834504}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1810707960}

[[ATD]{lang="EN-US"}]{#struct_0_56601_x1470_419007861}[帧定时器的值为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Hold Off]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[0]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[3]{lang="EN-US"}[毫秒，拓扑稳定定时器的值为]{style="font-family:宋体"}[40]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[TC]{lang="EN-US"}[帧快发定时器的值为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[TC]{lang="EN-US"}[帧慢发定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[TP]{lang="EN-US"}[帧快发定时器的值为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[TP]{lang="EN-US"}[帧慢发定时器的值为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[WTR]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1590075091}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1874217354}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_1480237222}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1953579598}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1474458424}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1605004545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1097201241}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1788798040}

[**[atd]{lang="EN-US"}**[ *atd-value*]{lang="EN-US"}]{#struct_0_56601_x1470_x1868049868}[：]{style="font-family:宋体"}[ATD]{lang="EN-US"}[帧定时器的值，]{style="font-family:宋体"}*[atd-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[holdoff]{lang="EN-US"}**[ *holdoff-value*]{lang="EN-US"}]{#struct_0_56601_x1470_762102726}[：]{style="font-family:宋体"}[Hold Off]{lang="EN-US"}[定时器的值，]{style="font-family:宋体"}*[holdoff-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[，单位为毫秒，步长为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[keepalive]{lang="EN-US"}**[ *keepalive-value*]{lang="EN-US"}]{#struct_0_56601_x1470_1477617088}[：]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[定时器的值，]{style="font-family:宋体"}*[keepalive-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[，单位为毫秒。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[stability]{lang="EN-US"}**[ *stability-value*]{lang="EN-US"}]{#struct_0_56601_x1470_775303757}[：拓扑稳定定时器的值，]{style="font-family:宋体"}*[stability-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[tc-fast]{lang="EN-US"}**[ *tc-fast-value*]{lang="EN-US"}]{#struct_0_56601_x1470_1396693840}[：]{style="font-family:宋体"}[TC]{lang="EN-US"}[帧快发定时器的值，]{style="font-family:宋体"}*[tc-fast-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[tc-slow]{lang="EN-US"}**[ *tc-slow-value*]{lang="EN-US"}]{#struct_0_56601_x1470_x1679033706}[：]{style="font-family:宋体"}[TC]{lang="EN-US"}[帧慢发定时器的值，]{style="font-family:宋体"}*[tc-slow-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒，步长为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[tp-fast]{lang="EN-US"}**[ *tp-fast-value*]{lang="EN-US"}]{#struct_0_56601_x1470_350012095}[：]{style="font-family:宋体"}[TP]{lang="EN-US"}[帧快发定时器的值，]{style="font-family:宋体"}*[tp-fast-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[tp-slow]{lang="EN-US"}**[ *tp-slow-value*]{lang="EN-US"}]{#struct_0_56601_x1470_x230220989}[：]{style="font-family:宋体"}[TP]{lang="EN-US"}[帧慢发定时器的值，]{style="font-family:宋体"}*[tp-slow-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒，步长为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[wtr]{lang="EN-US"}**[ *wtr-value*]{lang="EN-US"}]{#struct_0_56601_x1470_1146479081}[：]{style="font-family:宋体"}[WTR]{lang="EN-US"}[定时器的值，]{style="font-family:宋体"}*[wtr-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1737138995}

[]{#_Toc133657467}[]{#_Toc138163513}[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_882293552}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[ATD]{lang="EN-US"}[帧定时器的值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1913712833}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr timer atd 3]{lang="NO-BOK"}

[[\# ]{lang="NO-BOK"}]{#struct_0_56601_x1470_x594076783}[在三层]{style="font-family:宋体"}[RPR]{lang="NO-BOK"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="NO-BOK"}[上配置]{style="font-family:宋体"}[ATD]{lang="NO-BOK"}[帧定时器的值为]{style="font-family:宋体"}[3]{lang="NO-BOK"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_56601_x1470_x1346695570}

[\[Sysname\] interface rpr-router 1]{lang="NO-BOK"}

[\[Sysname-RPR-Router1\] rpr timer atd 3]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_655299782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **rpr** **timers**]{lang="EN-US"}]{#struct_0_56601_x1470_787077107}
:::::

::::: {#-654853492 .myid}
[]{#_Toc404795759}[]{#struct_0_56601_x1470_1178588284}[]{#_Toc353461189}[]{#_Toc367806690}[]{#_Toc367806884}[]{#_Toc367885358}[]{#_Toc367975103}[]{#_Toc367975523}[]{#_Toc367976435}[]{#_Toc369006495}[]{#_Toc369007667}[]{#_Toc369177350}[]{#_Toc353461190}[]{#_Toc367806691}[]{#_Toc367806885}[]{#_Toc367885359}[]{#_Toc367975104}[]{#_Toc367975524}[]{#_Toc367976436}[]{#_Toc369006496}[]{#_Toc369007668}[]{#_Toc369177351}[]{#_Toc353461191}[]{#_Toc367806692}[]{#_Toc367806886}[]{#_Toc367885360}[]{#_Toc367975105}[]{#_Toc367975525}[]{#_Toc367976437}[]{#_Toc369006497}[]{#_Toc369007669}[]{#_Toc369177352}[]{#_Toc353461192}[]{#_Toc367806693}[]{#_Toc367806887}[]{#_Toc367885361}[]{#_Toc367975106}[]{#_Toc367975526}[]{#_Toc367976438}[]{#_Toc369006498}[]{#_Toc369007670}[]{#_Toc369177353}[]{#_Toc353461193}[]{#_Toc367806694}[]{#_Toc367806888}[]{#_Toc367885362}[]{#_Toc367975107}[]{#_Toc367975527}[]{#_Toc367976439}[]{#_Toc369006499}[]{#_Toc369007671}[]{#_Toc369177354}[]{#_Toc353461194}[]{#_Toc367806695}[]{#_Toc367806889}[]{#_Toc367885363}[]{#_Toc367975108}[]{#_Toc367975528}[]{#_Toc367976440}[]{#_Toc369006500}[]{#_Toc369007672}[]{#_Toc369177355}[]{#_Toc353461195}[]{#_Toc367806696}[]{#_Toc367806890}[]{#_Toc367885364}[]{#_Toc367975109}[]{#_Toc367975529}[]{#_Toc367976441}[]{#_Toc369006501}[]{#_Toc369007673}[]{#_Toc369177356}[]{#_Toc353461196}[]{#_Toc367806697}[]{#_Toc367806891}[]{#_Toc367885365}[]{#_Toc367975110}[]{#_Toc367975530}[]{#_Toc367976442}[]{#_Toc369006502}[]{#_Toc369007674}[]{#_Toc369177357}[]{#_Toc353461197}[]{#_Toc367806698}[]{#_Toc367806892}[]{#_Toc367885366}[]{#_Toc367975111}[]{#_Toc367975531}[]{#_Toc367976443}[]{#_Toc369006503}[]{#_Toc369007675}[]{#_Toc369177358}[]{#_Toc353461198}[]{#_Toc367806699}[]{#_Toc367806893}[]{#_Toc367885367}[]{#_Toc367975112}[]{#_Toc367975532}[]{#_Toc367976444}[]{#_Toc369006504}[]{#_Toc369007676}[]{#_Toc369177359}[]{#_Toc353461199}[]{#_Toc367806700}[]{#_Toc367806894}[]{#_Toc367885368}[]{#_Toc367975113}[]{#_Toc367975533}[]{#_Toc367976445}[]{#_Toc369006505}[]{#_Toc369007677}[]{#_Toc369177360}[]{#_Toc353461200}[]{#_Toc367806701}[]{#_Toc367806895}[]{#_Toc367885369}[]{#_Toc367975114}[]{#_Toc367975534}[]{#_Toc367976446}[]{#_Toc369006506}[]{#_Toc369007678}[]{#_Toc369177361}[]{#_Toc353461201}[]{#_Toc367806702}[]{#_Toc367806896}[]{#_Toc367885370}[]{#_Toc367975115}[]{#_Toc367975535}[]{#_Toc367976447}[]{#_Toc369006507}[]{#_Toc369007679}[]{#_Toc369177362}[]{#_Toc353461202}[]{#_Toc367806703}[]{#_Toc367806897}[]{#_Toc367885371}[]{#_Toc367975116}[]{#_Toc367975536}[]{#_Toc367976448}[]{#_Toc369006508}[]{#_Toc369007680}[]{#_Toc369177363}[]{#_Toc353461203}[]{#_Toc367806704}[]{#_Toc367806898}[]{#_Toc367885372}[]{#_Toc367975117}[]{#_Toc367975537}[]{#_Toc367976449}[]{#_Toc369006509}[]{#_Toc369007681}[]{#_Toc369177364}[]{#_Toc353461204}[]{#_Toc367806705}[]{#_Toc367806899}[]{#_Toc367885373}[]{#_Toc367975118}[]{#_Toc367975538}[]{#_Toc367976450}[]{#_Toc369006510}[]{#_Toc369007682}[]{#_Toc369177365}[]{#_Toc353461205}[]{#_Toc367806706}[]{#_Toc367806900}[]{#_Toc367885374}[]{#_Toc367975119}[]{#_Toc367975539}[]{#_Toc367976451}[]{#_Toc369006511}[]{#_Toc369007683}[]{#_Toc369177366}[]{#_Toc353461206}[]{#_Toc367806707}[]{#_Toc367806901}[]{#_Toc367885375}[]{#_Toc367975120}[]{#_Toc367975540}[]{#_Toc367976452}[]{#_Toc369006512}[]{#_Toc369007684}[]{#_Toc369177367}[]{#_Toc353461207}[]{#_Toc367806708}[]{#_Toc367806902}[]{#_Toc367885376}[]{#_Toc367975121}[]{#_Toc367975541}[]{#_Toc367976453}[]{#_Toc369006513}[]{#_Toc369007685}[]{#_Toc369177368}[]{#_Toc353461208}[]{#_Toc367806709}[]{#_Toc367806903}[]{#_Toc367885377}[]{#_Toc367975122}[]{#_Toc367975542}[]{#_Toc367976454}[]{#_Toc369006514}[]{#_Toc369007686}[]{#_Toc369177369}[]{#_Toc353461209}[]{#_Toc367806710}[]{#_Toc367806904}[]{#_Toc367885378}[]{#_Toc367975123}[]{#_Toc367975543}[]{#_Toc367976455}[]{#_Toc369006515}[]{#_Toc369007687}[]{#_Toc369177370}[]{#_Toc353461210}[]{#_Toc367806711}[]{#_Toc367806905}[]{#_Toc367885379}[]{#_Toc367975124}[]{#_Toc367975544}[]{#_Toc367976456}[]{#_Toc369006516}[]{#_Toc369007688}[]{#_Toc369177371}[]{#_Toc353461211}[]{#_Toc367806712}[]{#_Toc367806906}[]{#_Toc367885380}[]{#_Toc367975125}[]{#_Toc367975545}[]{#_Toc367976457}[]{#_Toc369006517}[]{#_Toc369007689}[]{#_Toc369177372}[]{#_Toc353461212}[]{#_Toc367806713}[]{#_Toc367806907}[]{#_Toc367885381}[]{#_Toc367975126}[]{#_Toc367975546}[]{#_Toc367976458}[]{#_Toc369006518}[]{#_Toc369007690}[]{#_Toc369177373}[]{#_Toc132536888}[]{#_Toc132536889}[]{#_Toc132536896}[]{#_Toc132536899}[]{#_Toc132536902}[]{#_Toc353461213}[]{#_Toc367806714}[]{#_Toc367806908}[]{#_Toc367885382}[]{#_Toc367975127}[]{#_Toc367975547}[]{#_Toc367976459}[]{#_Toc369006519}[]{#_Toc369007691}[]{#_Toc369177374}[]{#_Toc353461214}[]{#_Toc367806715}[]{#_Toc367806909}[]{#_Toc367885383}[]{#_Toc367975128}[]{#_Toc367975548}[]{#_Toc367976460}[]{#_Toc369006520}[]{#_Toc369007692}[]{#_Toc369177375}[]{#_Toc353461215}[]{#_Toc367806716}[]{#_Toc367806910}[]{#_Toc367885384}[]{#_Toc367975129}[]{#_Toc367975549}[]{#_Toc367976461}[]{#_Toc369006521}[]{#_Toc369007693}[]{#_Toc369177376}[]{#_Toc353461216}[]{#_Toc367806717}[]{#_Toc367806911}[]{#_Toc367885385}[]{#_Toc367975130}[]{#_Toc367975550}[]{#_Toc367976462}[]{#_Toc369006522}[]{#_Toc369007694}[]{#_Toc369177377}[]{#_Toc353461217}[]{#_Toc367806718}[]{#_Toc367806912}[]{#_Toc367885386}[]{#_Toc367975131}[]{#_Toc367975551}[]{#_Toc367976463}[]{#_Toc369006523}[]{#_Toc369007695}[]{#_Toc369177378}[]{#_Toc353461218}[]{#_Toc367806719}[]{#_Toc367806913}[]{#_Toc367885387}[]{#_Toc367975132}[]{#_Toc367975552}[]{#_Toc367976464}[]{#_Toc369006524}[]{#_Toc369007696}[]{#_Toc369177379}[]{#_Toc353461219}[]{#_Toc367806720}[]{#_Toc367806914}[]{#_Toc367885388}[]{#_Toc367975133}[]{#_Toc367975553}[]{#_Toc367976465}[]{#_Toc369006525}[]{#_Toc369007697}[]{#_Toc369177380}[]{#_Toc353461220}[]{#_Toc367806721}[]{#_Toc367806915}[]{#_Toc367885389}[]{#_Toc367975134}[]{#_Toc367975554}[]{#_Toc367976466}[]{#_Toc369006526}[]{#_Toc369007698}[]{#_Toc369177381}

**RPR \-- RPR配置命令 \-- rpr weight**

------------------------------------------------------------------------

[**[rpr]{lang="EN-US"}**[ **weight**]{lang="EN-US"}]{#struct_0_56601_x1470_347574164}[命令用来配置站点的链路权重。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rpr** **weight**]{lang="EN-US"}]{#struct_0_56601_x1470_x630736879}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1652619648}

[**[rpr]{lang="EN-US"}**[ **weight** { **ringlet0** \| **ringlet1** } *value*]{lang="EN-US"}]{#struct_0_56601_x1470_1571902727}

[**[undo]{lang="EN-US"}**[ **rpr** **weight** { **ringlet0** \| **ringlet1** }]{lang="EN-US"}]{#struct_0_56601_x1470_x1358226153}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1619975463}

[[站点在]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_56601_x1470_1358914004}[环和]{style="font-family:宋体"}[1]{lang="EN-US"}[环上的链路权重均为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1089449602}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1994217452}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_329441365}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_195228385}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x387495657}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1460892684}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x464724653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1561326544}

[**[ringlet0]{lang="EN-US"}**]{#struct_0_56601_x1470_x714010732}[：配置站点在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上的链路权重。]{style="font-family:宋体"}

[**[ringlet1]{lang="EN-US"}**]{#struct_0_56601_x1470_x924397125}[：配置站点在]{style="font-family:宋体"}[1]{lang="EN-US"}[环上的链路权重。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_56601_x1470_x377254818}[：链路权重值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，必须是]{style="font-family:宋体"}[2]{lang="EN-US"}[的指数幂。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_708105288}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_90993854}[在二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[上配置站点在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上的链路权重为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_372019230}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] rpr weight ringlet0 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1665340532}[在三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上配置站点在]{style="font-family:宋体"}[0]{lang="EN-US"}[环上的链路权重为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x2066263061}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] rpr weight ringlet0 2]{lang="EN-US"}
:::::

::::: {#679047146 .myid}
[]{#_Toc404795760}[]{#struct_0_56601_x1470_909744129}[]{#_Toc382999926}[]{#_Toc263323277}[]{#_Toc252280806}

**RPR \-- RPR配置命令 \-- scramble**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_1777074477}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1890580615}
:::

[ ]{lang="EN-US"}

[**[scramble]{lang="EN-US"}**]{#struct_0_56601_x1470_1743164790}[命令用来开启当前接口对载荷的加扰功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **scramble**]{lang="EN-US"}]{#struct_0_56601_x1470_x702516927}[命令用来关闭该功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1050139258}

[**[scramble]{lang="EN-US"}**]{#struct_0_56601_x1470_1726960948}

[**[undo]{lang="EN-US"}**[ **scramble**]{lang="EN-US"}]{#struct_0_56601_x1470_x1194064711}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1786981316}

[[接口对载荷的加扰功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x948770076}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_576393584}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x1758099261}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_309042169}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x570631157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x976450006}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_995885695}

[[开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_56601_x1470_x790780184}[或]{style="font-family:宋体"}[0]{lang="EN-US"}[，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端接口都打开或关闭对载荷的加扰功能，才能对接成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_735454799}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x730604876}[开启]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[对载荷的加扰功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_278073451}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] scramble]{lang="EN-US"}
:::::

::::: {#-780779607 .myid}
[]{#_Toc404795761}[]{#struct_0_56601_x1470_965754174}[]{#_Toc215479545}[]{#_Toc383693402}[]{#_Toc303865071}[]{#_Toc215545670}

**RPR \-- RPR配置命令 \-- service**

------------------------------------------------------------------------

[**[service]{lang="EN-US"}**]{#struct_0_56601_x1470_x561066506}[命令用来指定转发当前接口流量的业务处理板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **service**]{lang="EN-US"}]{#struct_0_56601_x1470_x705766399}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x677127487}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_56601_x1470_1069369594}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[service]{lang="EN-US"}**[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56601_x1470_49095595}

[**[undo]{lang="EN-US"}**[ **service** **slot**]{lang="EN-US"}]{#struct_0_56601_x1470_1227828480}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_56601_x1470_1938103171}[模式：]{style="font-family:宋体"}

[**[service]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56601_x1470_x1359050342}

[**[undo]{lang="EN-US"}**[ **service** **chassis**]{lang="EN-US"}]{#struct_0_56601_x1470_x1572990222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1068702360}

[[流量会被接收该流量的]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x1166852953}[物理端口所在的单板直接进行处理。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1712855512}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x462084060}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_891876042}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1985157338}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1249367331}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x1787626251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x232105978}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_650484484}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_56601_x1470_296606172}[：将指定单板作为处理当前接口流量的业务处理板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_56601_x1470_1614986216}[：将指定该成员设备作为处理当前接口流量的业务处理板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_56601_x1470_1622601010}[：将指定该成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[作为处理当前接口流量的业务处理板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56601_x1470_419073397}[：将指定成员设备上的指定单板作为处理当前接口流量的业务处理板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56601_x1470_19588671}[：将指定单板作为处理当前接口流量的业务处理板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1617880335}

[[缺省情况下，流量会被接收该流量的]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_x827259873}[物理端口所在的单板直接进行处理。而某些业务（如]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[抗重放检测）要求同一个]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的流量必须在同一个单板]{style="font-family:宋体"}[/]{lang="EN-US"}[成员设备上进行处理，此时可以通过本命令指定转发当前接口流量的业务处理板。]{style="font-family:宋体"}

[[需要注意的是，如果把本配置所指定的业务处理板拔出，将导致流量转发不通；重新插入该板后，流量可以恢复在该板的正常转发。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1572411938}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_2053619690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式应用]{style="font-family:宋体"}]{#struct_0_56601_x1470_x746698488}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_186562159}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板作为处理二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[流量的业务处理板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1576323116}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1953776206}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板作为处理三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[流量的业务处理板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x346774641}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] service slot 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1839972607}[IRF]{lang="EN-US"}[设备应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_101165992}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备作为处理二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[流量的业务处理板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x412797666}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1226553511}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备作为处理三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[流量的业务处理板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_429535480}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] service slot 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_56601_x1470_981210615}[IRF]{lang="EN-US"}[模式应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_731384905}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板处理二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[流量的业务处理板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x909370137}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] service chassis 2 slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_775107149}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板处理三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[流量的业务处理板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1122998008}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] service chassis 2 slot 2]{lang="EN-US"}
:::::

::::: {#1170655049 .myid}
[]{#_Toc404795762}[]{#struct_0_56601_x1470_x436676719}[]{#_Toc382999927}

**RPR \-- RPR配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_56601_x1470_x976225890}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_56601_x1470_x927768667}[命令用来打开当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_250586705}

[**[shutdown]{lang="EN-US"}**]{#struct_0_56601_x1470_x114592820}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_56601_x1470_x1631524538}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_893793613}

[[接口处于开启状态。]{style="font-family:宋体"}]{#struct_0_56601_x1470_x1146927466}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1178391676}

[[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_56601_x1470_1498988686}[逻辑接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/RPRGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRXGE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/RPRPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image002.png){#图片 51 width="63" height="25"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1393511754}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_x1138032157}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_2024680219}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x691394654}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1299314762}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x387692265}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1676565496}[关闭二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Bridge1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_661164603}

[\[Sysname\] interface rpr-bridge 1]{lang="EN-US"}

[\[Sysname-[RPR-Bridge1]{.TerminalDisplayChar}\] shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x2012360784}[关闭三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_1477303156}

[\[Sysname\] interface rpr-router 1]{lang="EN-US"}

[\[Sysname-RPR-Router1\] shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1603250626}[关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRGE2/2/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_467215401}

[\[Sysname\] interface rprge 2/2/0]{lang="EN-US"}

[\[Sysname-RPRGE2/2/0\] shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_371822622}[关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRXGE2/3/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x2000034408}

[\[Sysname\] interface rprxge 2/3/0]{lang="EN-US"}

[\[Sysname-RPRXGE2/3/0\] shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x726113976}[关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x262644062}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] shutdown]{lang="EN-US"}
:::::

::::: {#1279049909 .myid}
[]{#_Toc404795763}[]{#struct_0_56601_x1470_1049687028}[]{#_Toc382999928}[]{#_Toc366853702}

**RPR \-- RPR配置命令 \-- snmp-agent trap enable { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1194261319}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1033406184}
:::

**[ ]{lang="EN-US"}**

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_x1973212311}[命令用来开启当前接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_1933959155}[命令用来关闭当前接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1392460854}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_1703237668}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_x162758146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_632847499}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x790976792}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_717098950}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x1829829897}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2127658419}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_421907595}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1583304176}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1743107583}

[[B1/B2/B3]{lang="EN-US"}]{#struct_0_56601_x1470_1496461509}[告警都是用于指示]{style="font-family:宋体"}[SDH]{lang="EN-US"}[体制线路的当前信号传输性能的，只是三者关注的信号层次不一样：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B1]{lang="EN-US"}]{#struct_0_56601_x1470_x86187122}[检验的是当前传输信号]{style="font-family:宋体"}[STM-N]{lang="EN-US"}[帧的整体误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B2]{lang="EN-US"}]{#struct_0_56601_x1470_x1304390043}[检验的是传输信号基本组成单元]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧的误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B3]{lang="EN-US"}]{#struct_0_56601_x1470_1937906563}[检验的是]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧封装的复用信号（]{style="font-family:宋体"}[VC3]{lang="EN-US"}[或]{style="font-family:宋体"}[VC4]{lang="EN-US"}[帧）的误码情况。]{style="font-family:宋体"}

[[当开启了]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x1916982592}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能后，设备将在]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口的误码超过]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警门限时生成告警信息。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_2142764301}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x660970294}[关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[B1]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_2102665647}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] undo snmp-agent trap enable b1-tca]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x114139466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[threshold]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_x525598127}
:::::

::::: {#-1291593385 .myid}
[]{#_Toc404795764}[]{#struct_0_56601_x1470_x2007652846}[]{#_Toc382999931}[]{#_Toc263323281}[]{#_Toc252280810}[]{#_Toc130049687}[]{#_Toc129668368}[]{#_Toc129527974}[]{#_Toc82589828}[]{#_Toc74652476}[]{#_Toc383692255}[]{#_Toc182037637}[]{#_Toc182039372}[]{#_Toc182043417}

**RPR \-- RPR配置命令 \-- threshold**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image004.jpg){#图片 9 width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x1038887269}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_1984960730}
:::

[ ]{lang="EN-US"}

[**[threshold]{lang="EN-US"}**]{#struct_0_56601_x1470_1251702346}[命令用来配置当前接口的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限和]{style="font-family:宋体"}[（]{style="font-family:宋体"}[或]{style="font-family:宋体"}[）]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **threshold**]{lang="EN-US"}]{#struct_0_56601_x1470_2011380606}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1143011329}

[**[threshold]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_56601_x1470_x267143053}[{ **sd** *sdvalue* \| **sf** *sfvalue* } \*]{lang="FR"}

[**[undo]{lang="EN-US"}**[ **threshold** ]{lang="EN-US"}]{#struct_0_56601_x1470_x359694705}[\[ **sd** \| **sf** \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1253253215}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_56601_x1470_1112983425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_438150699}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x268088385}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_418876789}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_24035484}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1216395431}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1761239836}

[**[sd]{lang="EN-US"}**]{#struct_0_56601_x1470_x413391921}[：表示配置]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警门限。]{style="font-family:宋体"}

[*[sd]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_56601_x1470_x796369501}[：以]{style="font-family:宋体"}[10e-sd*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sd]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SD]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_56601_x1470_x817886096}[：表示配置]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警门限。]{style="font-family:宋体"}

[*[sf]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_56601_x1470_x273433506}[：以]{style="font-family:宋体"}[10e-sf*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sf]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SF]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1977644826}

[[SD]{lang="EN-US"}]{#struct_0_56601_x1470_1337591599}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警都是用于指示当前线路性能的，相比较而言，]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警比]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警更为严重，]{style="font-family:宋体"}[SF]{lang="EN-US"}[的误码率门限一般会比]{style="font-family:宋体"}[SD]{lang="EN-US"}[的误码率门限高，也就是说，当出现少量误码时，设备产生]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警，当误码率增大到一定程度时，说明线路质量严重下降，此时设备才产生]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。因此，应使]{style="font-family:宋体"}[SD]{lang="EN-US"}[的告警门限小于]{style="font-family:宋体"}[SF]{lang="EN-US"}[的告警门限，]{style="font-family:宋体"}*[sdvalue]{lang="EN-US"}*[的值应大于]{style="font-family:宋体"}*[sfvalue]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_151625702}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_x1953710670}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限为]{style="font-family:宋体"}[10e-4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1325044901}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] threshold sd 4]{lang="EN-US"}
:::::

::::: {#146005858 .myid}
[]{#_Toc404795765}[]{#struct_0_56601_x1470_x1245771139}[]{#_Toc382999932}[]{#_Toc366853701}

**RPR \-- RPR配置命令 \-- threshold { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_1022223715}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_988910066}
:::

**[ ]{lang="EN-US"}**

[**[threshold]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_15504733}[命令用来配置当前接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警门限。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **threshold** { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_2136323967}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_317226128}

[**[threshold]{lang="EN-US"}**[ { **b1-tca** *b1value* \| **b2-tca** *b2value* \| **b3-tca** *b3value* }]{lang="EN-US"}]{#struct_0_56601_x1470_1910486960}

[**[undo]{lang="EN-US"}**[ **threshold** { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_775172685}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x390377698}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_56601_x1470_244554344}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2034711839}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_1661855433}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1035232819}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_2021578420}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x467219368}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x441454497}

[*[b1value]{lang="EN-US"}*]{#struct_0_56601_x1470_599670505}[：以]{style="font-family:宋体"}[10e-*b1value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[B1]{lang="EN-US"}[告警门限值，]{style="font-family:宋体"}*[b1value]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，值越大表示]{style="font-family:
宋体"}[B1]{lang="EN-US"}[告警门限越小。]{style="font-family:宋体"}

[*[b2value]{lang="EN-US"}*]{#struct_0_56601_x1470_x293362146}[：以]{style="font-family:宋体"}[10e-*b2value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[B2]{lang="EN-US"}[告警门限值，]{style="font-family:宋体"}*[b2value]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，值越大表示]{style="font-family:
宋体"}[B2]{lang="EN-US"}[告警门限越小。]{style="font-family:宋体"}

[*[b3value]{lang="EN-US"}*]{#struct_0_56601_x1470_715603090}[：以]{style="font-family:宋体"}[10e-*b3value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[B3]{lang="EN-US"}[告警门限值，]{style="font-family:宋体"}*[b3value]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，值越大表示]{style="font-family:
宋体"}[B3]{lang="EN-US"}[告警门限越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1178457212}

[[B1/B2/B3]{lang="EN-US"}]{#struct_0_56601_x1470_1465482121}[告警都是用于指示]{style="font-family:宋体"}[SDH]{lang="EN-US"}[体制线路的当前信号传输性能的，只是三者关注的信号层次不一样：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B1]{lang="EN-US"}]{#struct_0_56601_x1470_x1557840768}[检验的是当前传输信号]{style="font-family:宋体"}[\--STM-N]{lang="EN-US"}[帧的整体误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B2]{lang="EN-US"}]{#struct_0_56601_x1470_x1819820477}[检验的是传输信号基本组成单元]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧的误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B3]{lang="EN-US"}]{#struct_0_56601_x1470_1085309505}[检验的是]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧封装的复用信号（]{style="font-family:宋体"}[VC3]{lang="EN-US"}[或]{style="font-family:宋体"}[VC4]{lang="EN-US"}[帧）的误码情况。]{style="font-family:宋体"}

[[当开启了]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x167753896}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能后，设备将在]{style="font-family:宋体"}[RPRPOS]{lang="EN-US"}[接口的误码超过]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警门限时生成告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1096056641}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_2120303079}[配置]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[B1]{lang="EN-US"}[告警门限为]{style="font-family:宋体"}[10e-4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1441299318}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] threshold b1-tca 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_111360902}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_56601_x1470_x775277282}
:::::

::::: {#1474946988 .myid}
[]{#_Toc404795766}[]{#struct_0_56601_x1470_1717848283}[]{#_Toc382999933}[]{#_Toc323827378}[]{#_Toc317856915}[]{#_Toc309228573}[]{#_Toc205607563}

**RPR \-- RPR配置命令 \-- timer-hold**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_x387626729}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_916991584}
:::

[ ]{lang="EN-US"}

[**[timer-hold]{lang="EN-US"}**]{#struct_0_56601_x1470_x1428178488}[命令用来配置]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer-hold**]{lang="EN-US"}]{#struct_0_56601_x1470_x906600400}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1308225956}

[**[timer-hold]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_56601_x1470_831286070}

[**[undo]{lang="EN-US"}**[ **timer-hold**]{lang="EN-US"}]{#struct_0_56601_x1470_x1663688778}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x834231306}

[[Keepalive]{lang="EN-US"}]{#struct_0_56601_x1470_736783702}[报文的发送周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_371888158}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_381191831}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_443195477}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_230763616}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x496107293}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1648321994}

[*[seconds]{lang="EN-US"}*]{#struct_0_56601_x1470_x517207862}[：]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1813726863}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_56601_x1470_1934945792}[、]{style="font-family:宋体"}[FR]{lang="EN-US"}[或]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[时，链路层会定期（可通过本命令修改）向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，从而上报链路层]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在速率非常低的链路上，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}]{#struct_0_56601_x1470_x1042756362}[报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的收发。而接口在若干个（可通过]{style="font-family:宋体"}**[timer-hold ]{lang="EN-US"}[retry]{lang="EN-US"}**[命令修改）]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期后仍未收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，就认为链路发生故障，从而拆除链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_815006559}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_791082908}[在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x1321001764}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] timer-hold 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1411942344}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_56601_x1470_x1194195783}
:::::

::::: {#518520923 .myid}
[]{#_Toc404795767}[]{#struct_0_56601_x1470_x237012373}

**RPR \-- RPR配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RPR命令.files/image001.png){#图片 15 width="62" height="24"}]{lang="EN-US"}]{#struct_0_56601_x1470_360499938}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_56601_x1470_290075595}
:::

[ ]{lang="EN-US"}

[**[timer-hold ]{lang="EN-US"}[retry]{lang="EN-US"}**]{#struct_0_56601_x1470_1301372500}[命令用来配置在多少个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer-hold retry**]{lang="EN-US"}]{#struct_0_56601_x1470_x87147817}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1511563860}

[**[timer-hold retry]{lang="EN-US"}**[ *retry*]{lang="EN-US"}]{#struct_0_56601_x1470_x953117651}

[**[undo]{lang="EN-US"}**[ **timer-hold retry**]{lang="EN-US"}]{#struct_0_56601_x1470_x6700602}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x885840962}

[[在]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_56601_x1470_x50903700}[个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x790911256}

[[RPRPOS]{lang="EN-US"}]{#struct_0_56601_x1470_x442715671}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1108823137}

[[network-admin]{lang="EN-US"}]{#struct_0_56601_x1470_1665016608}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56601_x1470_x162132115}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x2129786376}

[*[retry]{lang="EN-US"}*]{#struct_0_56601_x1470_x46912568}[：在多少个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56601_x1470_877225920}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_56601_x1470_1119565150}[、]{style="font-family:宋体"}[FR]{lang="EN-US"}[或]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[时，链路层会定期（可通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改）向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在速率非常低的链路上，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}]{#struct_0_56601_x1470_x12098992}[报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的收发。而接口在若干个（可通过本命令修改）]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期后仍未收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，就认为链路发生故障，从而拆除链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56601_x1470_x1458562258}

[[\# ]{lang="EN-US"}]{#struct_0_56601_x1470_1937972099}[在]{style="font-family:宋体"}[RPR]{lang="EN-US"}[物理接口]{style="font-family:宋体"}[RPRPOS2/4/0]{lang="EN-US"}[上，配置在]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56601_x1470_x783745741}

[\[Sysname\] interface rprpos 2/4/0]{lang="EN-US"}

[\[Sysname-RPRPOS2/4/0\] timer-hold retry 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56601_x1470_1217170455}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_56601_x1470_1432421643}

[ ]{lang="EN-US"}
:::::
