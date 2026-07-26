::::: {#1725110147 .myid}
[]{#_Toc296086815}[]{#_Toc295480285}[]{#_Toc295465879}[]{#_Toc404783736}[]{#struct_0_x4619_57162_x338097139}[]{#_Toc366241761}[]{#_Toc345232201}

**POS接口 \-- POS接口配置命令 \-- alarm-detect**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_x50101281}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_1340802888}
:::

**[ ]{lang="EN-US"}**

[**[alarm-detect]{lang="EN-US"}**]{#struct_0_x4619_57162_139680160}[命令用来设置当前接口的告警联动动作。]{style="font-family:宋体"}

[**[undo alarm-detect]{lang="EN-US"}**]{#struct_0_x4619_57162_x338162675}[命令用来取消告警联动动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1545521985}

[**[alarm-detect]{lang="EN-US"}**[ { **rdi** \| **sd** \| **sf** } **action** **link-down**]{lang="EN-US"}]{#struct_0_x4619_57162_x1420249131}

[**[undo alarm-detect]{lang="EN-US"}**[ { **rdi** \| **sd** \| **sf** }]{lang="EN-US"}]{#struct_0_x4619_57162_1484727955}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1634741017}

[[接口不执行任何告警联动动作。]{style="font-family:宋体"}]{#struct_0_x4619_57162_x280970652}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_712787276}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x337966067}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_552729020}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x140631267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1024689709}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1202081041}

[**[rdi]{lang="EN-US"}**]{#struct_0_x4619_57162_x2003855223}[：表示]{style="font-family:宋体"}[RDI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Defect Indication]{lang="EN-US"}[，远端失效指示）告警。]{style="font-family:宋体"}

[**[sd]{lang="EN-US"}**]{#struct_0_x4619_57162_x514295744}[：表示]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_x4619_57162_x338031603}[：表示]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_x4619_57162_1933536532}[：设置当接口检测到告警时的联动动作。]{style="font-family:宋体"}

[**[link-down]{lang="EN-US"}**]{#struct_0_x4619_57162_x916903103}[：表示自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_294417713}

[[当设备收到对端发送的]{style="font-family:宋体"}[MS-RDI]{lang="EN-US"}]{#struct_0_x4619_57162_1286926314}[信号时，则认为发生了]{style="font-family:宋体"}[RDI]{lang="EN-US"}[告警。当设备收到的报文的误码率达到或超过设置的门限时，则生成]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警或]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警的门限可通过]{style="font-family:宋体"}**[threshold]{lang="EN-US"}**[命令设置。]{style="font-family:宋体"}

[[配置本命令后，当设备检测到告警时，会自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x4619_57162_x2032181374}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x337834995}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x1434906446}[配置当]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[检测到]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警时，自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1711896485}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] alarm-detect sd action link-down]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1313795418}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[threshold]{lang="EN-US"}**]{#struct_0_x4619_57162_1797087894}
:::::

::: {#1742433432 .myid}
[]{#_Toc263323266}[]{#_Toc252280725}[]{#_Toc404783737}[]{#struct_0_x4619_57162_x949945437}[]{#_Toc284169067}

**POS接口 \-- POS接口配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x4619_57162_992719841}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x4619_57162_655095458}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1049676354}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x4619_57162_297840660}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x4619_57162_x351804244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1317658467}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x4619_57162_2132486519}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_928653289}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x19420230}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x950010973}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1290924450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_440281591}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1004688519}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x4619_57162_x862140289}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x254009159}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x4619_57162_552083933}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x577553687}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x1706854654}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x950076509}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] bandwidth 50]{lang="EN-US"}
:::

::: {#424787513 .myid}
[]{#_Toc404783738}[]{#struct_0_x4619_57162_x1435683325}

**POS接口 \-- POS接口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_x4619_57162_1654330280}[命令用来设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x4619_57162_x78830293}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1179278191}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x4619_57162_x818442136}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x4619_57162_x470685336}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1155096719}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_895379822}[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x950142045}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x690026292}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x625799569}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1557011183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_507097197}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x2022003108}

[**[master]{lang="EN-US"}**]{#struct_0_x4619_57162_x112573752}[：设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的时钟模式为主时钟模式。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x4619_57162_x1129679694}[：设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的时钟模式为从时钟模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1262420956}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x453618877}[接口支持两种时钟模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[master]{lang="EN-US"}**]{#struct_0_x4619_57162_x950207581}[：主时钟模式，使用内部时钟信号；]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[slave]{lang="EN-US"}**]{#struct_0_x4619_57162_131252642}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:
宋体"}

[[与同步串口有]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_x4619_57162_1064431030}[和]{style="font-family:宋体"}[DCE]{lang="EN-US"}[两种工作方式相仿，]{style="font-family:宋体"}[POS]{lang="EN-US"}[也需要选择时钟模式。当两台路由器的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口直接相连时，应配置一端使用主时钟模式，另一端使用从时钟模式；当与]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[设备相连时，由于]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[网络的时钟精度高于]{style="font-family:宋体"}[POS]{lang="EN-US"}[本身内部时钟源的精度，应配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口使用从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1865664484}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x793238018}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x934838101}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] clock master]{lang="EN-US"}
:::

::: {#538040344 .myid}
[]{#_Toc404783739}[]{#struct_0_x4619_57162_x296384529}[]{#_Toc263323267}[]{#_Toc252280726}

**POS接口 \-- POS接口配置命令 \-- crc**

------------------------------------------------------------------------

[**[crc]{lang="EN-US"}**]{#struct_0_x4619_57162_795473970}[命令用来设定接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度。]{style="font-family:宋体"}

[**[undo crc]{lang="EN-US"}**]{#struct_0_x4619_57162_x950273117}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1074162667}

[**[crc]{lang="EN-US"}**[ { **16** \| **32** }]{lang="EN-US"}]{#struct_0_x4619_57162_797594471}

[**[undo]{lang="EN-US"}**[ **crc**]{lang="EN-US"}]{#struct_0_x4619_57162_x1649742121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x809339284}

[[CRC]{lang="EN-US"}]{#struct_0_x4619_57162_1310198396}[校验字长度为]{style="font-family:宋体"}[32]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1598379561}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_1816149857}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1851706040}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_499421523}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x950338653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x305096955}

[**[16]{lang="EN-US"}**]{#struct_0_x4619_57162_1989466543}[：]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_x4619_57162_x1759748064}[：]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度为]{style="font-family:宋体"}[32]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x649530168}

[[设置接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_x4619_57162_x1689775820}[校验字长度时，注意两端设备应保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1563530847}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1927238436}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验字长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_643291383}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] crc 16]{lang="EN-US"}
:::

::: {#1245918683 .myid}
[]{#_Toc353527897}[]{#_Toc404783740}[]{#struct_0_x4619_57162_x337966068}[]{#_Toc359918310}[]{#_Toc355619426}

**POS接口 \-- POS接口配置命令 \-- dampening**

------------------------------------------------------------------------

[**[dampening]{lang="EN-US"}**]{#struct_0_x4619_57162_x338031604}[命令用来开启接口的]{style="font-family:宋体"}[dampening]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo dampening]{lang="EN-US"}**]{#struct_0_x4619_57162_1933208852}[命令用来关闭接口的]{style="font-family:宋体"}[dampening]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_640399928}

[**[dampening]{lang="EN-US"}**[ \[ *half-life* *reuse suppress max-suppress-time* \]]{lang="EN-US"}]{#struct_0_x4619_57162_x1389617033}

[**[undo dampening]{lang="EN-US"}**]{#struct_0_x4619_57162_x337834996}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1434709838}

[[接口的]{style="font-family:宋体"}[dampening]{lang="EN-US"}]{#struct_0_x4619_57162_x647424209}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1640840929}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x720944433}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x337900532}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1392188681}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1420614705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1883295526}

[*[half-life]{lang="EN-US"}*]{#struct_0_x4619_57162_x337703924}[：]{style="font-family:宋体"}[半衰期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，]{style="font-family:宋体"}[单位为秒，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[54]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[*[reuse]{lang="EN-US"}*]{#struct_0_x4619_57162_x664119469}[：]{style="font-family:宋体"}[启用门限，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[750]{lang="EN-US"}[，]{style="font-family:宋体"}*[reuse]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[suppress]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[*[suppress]{lang="EN-US"}*]{#struct_0_x4619_57162_1850798209}[：抑制门限，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[max-suppress-time]{lang="EN-US"}*]{#struct_0_x4619_57162_686410120}[：]{style="font-family:宋体"}[最大抑制时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒，缺省值为半衰期的]{style="font-family:宋体"}[3]{lang="EN-US"}[倍，即]{style="font-family:宋体"}[162]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1988274817}

[[接口有两种物理连接状态：]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x4619_57162_x337769460}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[。由于线缆故障、接口连接或链路层配置错误等问题，可能会导致设备接口的状态频繁的在]{style="font-family:宋体"}[down]{lang="EN-US"}[和]{style="font-family:宋体"}[up]{lang="EN-US"}[之间切换，这种现象称为接口震荡。随着接口状态的频繁改变，设备会不停的刷新相关表项（比如路由表），消耗大量的系统资源。通过在接口上配置]{style="font-family:宋体"}[dampening]{lang="EN-US"}[功能，可以在一定条件下，屏蔽该接口的震荡对路由等上层业务的影响。此时若出现接口震荡，将不上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}[处理，仅产生对应的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息，从而节省系统资源的消耗。]{style="font-family:宋体"}

[[dampening]{lang="EN-US"}]{#struct_0_x4619_57162_x1421995279}[功能的工作原理如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启]{style="font-family:宋体"}]{#struct_0_x4619_57162_2030153760}[dampening]{lang="EN-US"}[功能后，接口将关联一个惩罚值，初始值是]{style="font-family:宋体"}[0]{lang="EN-US"}[。接口状态每次从]{style="font-family:宋体"}[up]{lang="EN-US"}[变到]{style="font-family:宋体"}[down]{lang="EN-US"}[时，惩罚值会增加]{style="font-family:宋体"}[1000]{lang="EN-US"}[（接口状态从]{style="font-family:宋体"}[down]{lang="EN-US"}[变到]{style="font-family:宋体"}[up]{lang="EN-US"}[时，惩罚值不变）。同时，惩罚值随着时间的推移自动减少，满足半衰期衰减规律]{style="font-family:宋体"}[：完全衰减时（即假如在此期间没有再发生接口震荡），经过一个半衰期，]{style="font-family:宋体"}[惩罚值将]{style="font-family:宋体"}[减少为原来值的一半]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x4619_57162_91061454}[惩罚值大于或等于抑制门限时，开始抑制接口：不上送]{style="font-family:
宋体"}[CPU]{lang="DA"}[处理接口状态变化，仅产生对应的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息]{style="font-family:宋体"}[。当]{style="font-family:宋体"}[惩罚值小于或等于启用门限时，不抑制接口：上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}[处理接口状态变化，同时发送对应的]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当惩罚值达到最大惩罚值后，惩罚值将不再增加。最大惩罚值不可配，其值与最大抑制时间、半衰期、启用门限之间的关系遵循如下公式：最大惩罚值＝]{style="font-family:宋体"}]{#struct_0_x4619_57162_1373002781}[2^(^]{lang="EN-US"}^[最大抑制时间]{style="font-family:宋体"}[/]{lang="EN-US"}[半衰期]{style="font-family:宋体"}[)]{lang="EN-US"}^[×启用值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每次接口进入抑制状态后，当接口持续抑制的时间超过最大抑制时间时，且此时惩罚值大于启用门限时，惩罚值将不再增加，此时惩罚值进入完全半衰期（此阶段接口状态变化不会增加惩罚值），直到惩罚值小于启用门限，不再抑制接口（完全半衰期中，接口仍然处于抑制状态，但完全半衰阶段时间不算入持续抑制时间）。]{style="font-family:宋体"}]{#struct_0_x4619_57162_x338228213}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口抑制时间不到最大抑制时间，惩罚值就小于启用门限，那么不存在完全半衰过程（持续抑制时间超过最大抑制时间才会进入）]{style="font-family:宋体"}]{#struct_0_x4619_57162_1494582984}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1109496100}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1938487759}[命令和]{lang="EN-US" style="font-family:宋体"}**[link-delay]{lang="EN-US"}**[命令不能同时使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令对使用]{style="font-family:宋体"}]{#struct_0_x4619_57162_x338293749}**[shutdown]{lang="EN-US"}**[命令手工关闭的接口无效。接口被关闭时，惩罚值恢复为初始值]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[处于抑制期时产生的接口]{style="font-family:宋体"}]{#struct_0_x4619_57162_1128486536}[up]{lang="EN-US"}[事件，通过]{style="font-family:宋体"}**[display interface pos]{lang="EN-US"}**[命令、]{style="font-family:宋体"}[MIB]{lang="EN-US"}[网管或]{style="font-family:宋体"}[Web]{lang="EN-US"}[网管等方式查看到时，接口状态仍然为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_757877287}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x777452562}[开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的]{style="font-family:宋体"}[dampening]{lang="EN-US"}[功能，配置半衰期为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，启用门限为]{style="font-family:宋体"}[800]{lang="EN-US"}[，抑制门限为]{style="font-family:宋体"}[3000]{lang="EN-US"}[，最大抑制时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x338097141}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] dampening 2 800 3000 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x49576998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_1689849053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[link-delay]{lang="EN-US"}**]{#struct_0_x4619_57162_1852393009}
:::

::: {#1948332219 .myid}
[]{#_Toc263067817}[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc139515317}[]{#_Toc137103150}[]{#_Toc272413471}[]{#_Toc261965075}[]{#_Toc205607679}[]{#_Toc404783741}[]{#struct_0_x4619_57162_x949355613}[]{#_Toc329007815}[]{#_Toc309912009}

**POS接口 \-- POS接口配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x4619_57162_1377481501}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x408109080}

[**[default]{lang="EN-US"}**]{#struct_0_x4619_57162_x639366582}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x2019886829}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_119653733}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_765250724}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1509696826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1324135450}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x949421149}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x4619_57162_1756136941}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x4619_57162_1964337491}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_2122089509}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x422362926}[将]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1131342383}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404783742}[]{#struct_0_x4619_57162_248184428}

**POS接口 \-- POS接口配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x4619_57162_925776989}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x4619_57162_787706622}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x949879904}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x4619_57162_x658625723}

[**[undo description]{lang="EN-US"}**]{#struct_0_x4619_57162_1603316673}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1621167427}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x4619_57162_342474535}["，比如：]{style="font-family:宋体"}[Pos2/2/0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1787415989}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x1392525828}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1905975208}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x604413416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1890221255}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x949945440}

[*[text]{lang="EN-US"}*]{#struct_0_x4619_57162_993047518}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1957303504}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x1066743771}[配置接口]{style="font-family:宋体"}[POS2/2/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[pos-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_544778232}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] description pos-interface]{lang="EN-US"}
:::

::: {#-1641266207 .myid}
[]{#_Toc404783743}[]{#struct_0_x4619_57162_582502981}[]{#_Toc263323268}[]{#_Toc252280727}[]{#_Toc274832279}[]{#_Toc275183040}

**POS接口 \-- POS接口配置命令 \-- display interface pos**

------------------------------------------------------------------------

[**[display interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_x1753138098}[命令用来显示]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x33697427}

[**[display interface]{lang="EN-US"}**[ \[ **pos** \[ *interface-number* \| *interface-number.subnumber* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x4619_57162_x950010976}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1291252130}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4619_57162_441872310}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_313954998}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x741917389}

[[network-operator]{lang="EN-US"}]{#struct_0_x4619_57162_609143475}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x598930155}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4619_57162_x2034751868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1951025258}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x4619_57162_891215373}[：显示指定]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_x4619_57162_x337769461}[：显示指定]{style="font-family:
宋体"}[POS]{lang="EN-US"}[子接口的信息。]{style="font-family:宋体"}*[interface-number.subnumber]{lang="EN-US"}*[表示]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口编号，其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x4619_57162_x950076512}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x4619_57162_235067779}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x4619_57162_1837565326}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x890312562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x4619_57162_x69124972}**[pos]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_x4619_57162_x2132079603}**[pos]{lang="EN-US"}**[参数，不指定接口编号，将显示所有已创建的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_138377072}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_750745363}[显示]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface pos 2/2/0]{lang="EN-US"}]{#struct_0_x4619_57162_x2134213117}

[Pos2/2/0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Pos5/1 Interface]{lang="EN-US"}

[Bandwidth: 50kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Dampening enabled:]{lang="EN-US"}

[ Penalty: 0 (not suppressed)]{lang="EN-US"}

[ Ceiling: 4525]{lang="EN-US"}

[ Reuse: 800]{lang="EN-US"}

[ Suppress: 3000]{lang="EN-US"}

[ Half-life: 2 seconds]{lang="EN-US"}

[ Max-suppress-time: 5 seconds]{lang="EN-US"}

[ Flap count: 0]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Internet Address: 5.5.5.2/24 Primary]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: opened, IPCP: opened]{lang="EN-US"}

[Physical layer: Packet Over SONET, Baudrate: 155520000 bps]{lang="EN-US"}

[Scramble: enabled, crc: 32, clock: slave, loopback: not set]{lang="EN-US"}

[SONET alarm:]{lang="EN-US"}

[  section layer: OOF LOF LOS]{lang="EN-US"}

[  line    layer: AIS]{lang="EN-US"}

[  path    layer: AIS RDI]{lang="EN-US"}

[  C2(Rx): 0xff, C2(Tx): 0x16]{lang="EN-US"}

[  J0(Rx): unknown]{lang="EN-US"}

[  J0(Tx): \"\"]{lang="EN-US"}

[  J1(Rx): unknown]{lang="EN-US"}

[  J1(Tx): \"\"]{lang="EN-US"}

[SONET error:]{lang="EN-US"}

[  section layer: B1 65535]{lang="EN-US"}

[  line    layer: B2 0 M1 0]{lang="EN-US"}

[  path    layer: B3 0 G1 0]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Input: ]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 runts, 0 giants, 0 CRC]{lang="EN-US"}

[  0 overruns, 0 aborts, 0 no buffers]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 underruns, 0 aborts]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_131449250}[显示]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface pos 2/2/0 brief]{lang="EN-US"}]{#struct_0_x4619_57162_x1435493525}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Pos2/2/0             UP   UP(s)    \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x178463201}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface pos brief down]{lang="EN-US"}]{#struct_0_x4619_57162_x950273120}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Pos2/2/0             ADM  Administratively]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface pos]{lang="EN-US"}]{#struct_0_x4619_57162_x1073703916}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_573282550}[[字段]{style="font-family:黑体"}]{#struct_0_x4619_57162_93280052}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4619_57162_181454650}

[[Pos2/2/0]{lang="EN-US"}]{#struct_0_x4619_57162_1755180472}

[[Current state]{lang="EN-US"}]{#struct_0_x4619_57162_1657545974}

[[该接口当前的物理状态和管理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x4619_57162_x206906013}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4619_57162_1278008062}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4619_57162_x950338656}[：表示该接口的物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x4619_57162_x304769275}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x4619_57162_x1949955337}

[[该接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1773352174}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x4619_57162_389334344}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4619_57162_1727459829}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x4619_57162_x949355616}

[[该接口的描述信息]{style="font-family:宋体"}]{#struct_0_x4619_57162_1377284893}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x4619_57162_689244076}

[[该接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x4619_57162_1731803818}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x4619_57162_1822263470}

[[该接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1243377164}

[[Dampening enabled:]{lang="EN-US"}]{#struct_0_x4619_57162_2045696979}

[[ Penalty: 0 (not suppressed)]{lang="EN-US"}]{#struct_0_x4619_57162_2045107154}

[[ Ceiling: 4525]{lang="EN-US"}]{#struct_0_x4619_57162_2045172690}

[[ Reuse: 800]{lang="EN-US"}]{#struct_0_x4619_57162_2045238226}

[[ Suppress: 3000]{lang="EN-US"}]{#struct_0_x4619_57162_2045303762}

[[ Half-life: 2 seconds]{lang="EN-US"}]{#struct_0_x4619_57162_2044845010}

[[ Max-suppress-time: 5 seconds]{lang="EN-US"}]{#struct_0_x4619_57162_2044910546}

[[ Flap count: 0]{lang="EN-US"}]{#struct_0_x4619_57162_2044976082}

[[该接口的]{style="font-family:宋体"}[dampening]{lang="EN-US"}]{#struct_0_x4619_57162_2045041618}[抑制信息，该显示信息的支持情况与用户的配置以及设备型号有关，请以设备的实际情况为准（若未使能]{style="font-family:宋体"}[dampening]{lang="EN-US"}[功能，则不会显示该段信息）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dampening enabled]{lang="EN-US"}]{#struct_0_x4619_57162_2045631442}[：已使能]{lang="EN-US" style="font-family:
  宋体"}[dampening]{lang="EN-US"}[功能]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Penalty]{lang="EN-US"}]{#struct_0_x4619_57162_2045696978}[：惩罚值]{lang="EN-US" style="font-family:宋体"}[（若接口处于抑制期，则在惩罚值后标识]{style="font-family:宋体"}[suppressed]{lang="EN-US"}[；反之，在惩罚值后标识]{style="font-family:宋体"}[not suppressed]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ceiling]{lang="EN-US"}]{#struct_0_x4619_57162_2045107153}[：最大惩罚值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reuse]{lang="EN-US"}]{#struct_0_x4619_57162_1406070760}[：启用门限]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Suppress]{lang="EN-US"}]{#struct_0_x4619_57162_2045172689}[：抑制门限]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Half-life]{lang="EN-US"}]{#struct_0_x4619_57162_2045238225}[：半衰期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max-suppress-time]{lang="EN-US"}]{#struct_0_x4619_57162_2045303761}[：最大抑制时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Flap count]{lang="EN-US"}]{#struct_0_x4619_57162_2044845009}[：]{lang="EN-US" style="font-family:宋体"}[接口震荡]{style="font-family:宋体"}[发生的次数]{lang="EN-US" style="font-family:宋体"}

 

[[Hold timer]{lang="EN-US"}]{#struct_0_x4619_57162_x949421152}

[[该接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x4619_57162_x942572036}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_x4619_57162_x942572038}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x4619_57162_x942572033}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet Address]{lang="EN-US"}]{#struct_0_x4619_57162_x1124742738}

[[该接口网络地址]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1252646329}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_x4619_57162_x949879903}

[[该接口的链路层封装的协议]{style="font-family:宋体"}]{#struct_0_x4619_57162_x658560187}

[[LCP: opened, IPCP: opened]{lang="EN-US"}]{#struct_0_x4619_57162_x776211855}

[[表示]{style="font-family:宋体"}[LCP]{lang="EN-US"}]{#struct_0_x4619_57162_x949945439}[和]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[都协商成功]{style="font-family:宋体"}

[[Physical layer]{lang="EN-US"}]{#struct_0_x4619_57162_992588769}

[[物理接口]{style="font-family:宋体"}]{#struct_0_x4619_57162_x783950388}

[[Baudrate]{lang="EN-US"}]{#struct_0_x4619_57162_x311868074}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_x4619_57162_x950010975}

[[Scramble]{lang="EN-US"}]{#struct_0_x4619_57162_1291055522}

[[该接口是否开启对载荷数据的加扰功能]{style="font-family:宋体"}]{#struct_0_x4619_57162_436582016}

[[crc]{lang="EN-US"}]{#struct_0_x4619_57162_1523465563}

[[该接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}]{#struct_0_x4619_57162_x1428761208}[校验字长度]{style="font-family:宋体"}

[[clock]{lang="EN-US"}]{#struct_0_x4619_57162_x950076511}

[[该接口的时钟模式]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1435159038}

[[loopback]{lang="EN-US"}]{#struct_0_x4619_57162_x952012921}

[[该接口是否开启环回功能]{style="font-family:宋体"}]{#struct_0_x4619_57162_395774065}

[[SONET alarm]{lang="EN-US"}]{#struct_0_x4619_57162_x950142047}

[[SONET]{lang="EN-US"}]{#struct_0_x4619_57162_x690157364}[告警信息]{style="font-family:宋体"}

[[SONET error]{lang="EN-US"}]{#struct_0_x4619_57162_x1013343686}

[[SONET]{lang="EN-US"}]{#struct_0_x4619_57162_x1786218042}[错误信息]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_x4619_57162_x1716721417}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x4619_57162_998415493}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x4619_57162_1012161938}

[[最近一次清除计数的时间]{style="font-family:宋体"}]{#struct_0_x4619_57162_131121570}

[[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x4619_57162_x1939578056}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x4619_57162_1585400788}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x4619_57162_x950273119}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x4619_57162_x1074293739}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input: ]{lang="EN-US"}]{#struct_0_x4619_57162_2091214931}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_x4619_57162_x950338655}

[[  0 errors, 0 runts, 0 giants, 0 CRC]{lang="EN-US"}]{#struct_0_x4619_57162_x304703739}

[[  0 overruns, 0 aborts, 0 no buffers]{lang="EN-US"}]{#struct_0_x4619_57162_x370770707}

[[接口收到的总报文数和总字节数：]{style="font-family:宋体"}]{#struct_0_x4619_57162_748946082}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_x4619_57162_x949355615}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[runts]{lang="EN-US"}]{#struct_0_x4619_57162_1377088285}[：接口接收到小于规定的最小报文长度报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_x4619_57162_390828071}[：接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CRC]{lang="EN-US"}]{#struct_0_x4619_57162_x949421151}[：接收长度正常但]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_x4619_57162_1755612652}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_x4619_57162_853162901}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffers]{lang="EN-US"}]{#struct_0_x4619_57162_x1606525251}[：在接收报文时由于内部缓存满，导致帧丢弃]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_x4619_57162_616204041}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_x4619_57162_x2110900664}

[[  0 errors, 0 underruns, 0 aborts]{lang="EN-US"}]{#struct_0_x4619_57162_1819726812}

[[接口发送的报文数和总字节数]{style="font-family:宋体"}]{#struct_0_x4619_57162_616138505}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_x4619_57162_x79135570}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_x4619_57162_320504756}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_x4619_57162_616072969}[：发送报文的异常错误]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_x4619_57162_x375388934}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_x4619_57162_932273481}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x4619_57162_616007433}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1624897354}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x4619_57162_615941897}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x4619_57162_1711123431}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x4619_57162_538879797}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4619_57162_615876361}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x4619_57162_634300595}

[[Link]{lang="EN-US"}]{#struct_0_x4619_57162_416270461}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x4619_57162_615810825}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x4619_57162_1356246022}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4619_57162_923275276}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x4619_57162_1460038063}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x4619_57162_923734028}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x4619_57162_615745289}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x4619_57162_1924013531}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x4619_57162_2045107150}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4619_57162_2045172686}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x4619_57162_2045238222}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x4619_57162_616728329}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4619_57162_x820931617}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x4619_57162_1251767897}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x4619_57162_616662793}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x4619_57162_1933927773}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x4619_57162_265139750}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x199301201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x4619_57162_616204042}

::: {#-19641155 .myid}
[]{#_Toc404783744}[]{#struct_0_x4619_57162_2044845006}[]{#_Toc356657152}

**POS接口 \-- POS接口配置命令 \-- flag c2**

------------------------------------------------------------------------

[**[flag]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4619_57162_x180299652}**[c2]{lang="DA"}**[命令用来配置信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo flag]{lang="EN-US"}**]{#struct_0_x4619_57162_2044910542}**[ ]{lang="EN-US"}[c2]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1768081912}

[**[flag]{lang="DA"}**]{#struct_0_x4619_57162_2044976078}[ **c2** *flag-value*]{lang="DA"}

[**[undo flag c2]{lang="DA"}**]{#struct_0_x4619_57162_217545315}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_2045041614}

[[信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}]{#struct_0_x4619_57162_x218518543}[的值为]{style="font-family:宋体"}[0x16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x349669542}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_2045631438}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x598823887}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_2045696974}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1423408120}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683776200}

[*[flag-value]{lang="EN-US"}*]{#struct_0_x4619_57162_x871223742}[：信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683710664}

[[信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}]{#struct_0_x4619_57162_x1282587378}[属于高阶通道开销字节，用于指示虚拟容器]{style="font-family:宋体"}[VC]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Container]{lang="EN-US"}[）帧的复接结构和信息净负荷的性质。]{style="font-family:宋体"}

[[C2]{lang="EN-US"}]{#struct_0_x4619_57162_1358186404}[字节的设置一定要使收]{style="font-family:宋体"}[/]{lang="EN-US"}[发两端相匹配，否则会产生告警。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683645128}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1061325872}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的信号标记字节]{style="font-family:宋体"}[C2]{lang="EN-US"}[为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x683579592}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] flag c2 01]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x852880236}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_x684038344}
:::

::: {#1143617011 .myid}
[]{#_Toc404783745}[]{#struct_0_x4619_57162_x683972808}[]{#_Toc356657155}

**POS接口 \-- POS接口配置命令 \-- flag j0**

------------------------------------------------------------------------

[**[flag]{lang="EN-US"}**]{#struct_0_x4619_57162_x49390568}[ ]{lang="EN-US"}**[j0]{lang="DA"}**[命令用来配置]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[帧的再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo flag]{lang="EN-US"}**]{#struct_0_x4619_57162_x683907272}[ ]{lang="EN-US"}**[j0]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1846846236}

[**[flag]{lang="DA"}**]{#struct_0_x4619_57162_x683841736}[ **j0** { **sdh** \| **sonet** } *flag-value*]{lang="DA"}

[**[undo flag j0]{lang="DA"}**]{#struct_0_x4619_57162_x881018357}[ { **sdh** \| **sonet** }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683251912}

[[系统使用]{style="font-family:宋体"}[SDH]{lang="EN-US"}]{#struct_0_x4619_57162_1499707619}[帧格式的缺省值，]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[的缺省值为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1030239000}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x683186376}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1050422681}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x683776201}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x871158206}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683710665}

[*[flag-value]{lang="EN-US"}*]{#struct_0_x4619_57162_x1282521842}[：再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[。]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_x4619_57162_x683645129}[：帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Digital Hierarchy]{lang="EN-US"}[，同步数字系列）。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x4619_57162_1061260336}[：帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Optical Network]{lang="EN-US"}[，同步光网络）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683579593}

[[再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}]{#struct_0_x4619_57162_x852814700}[属于段开销字节（]{style="font-family:宋体"}[Section Overhead]{lang="EN-US"}[），用于检测两个接口之间的连接在段层次上的连续性。]{style="font-family:宋体"}

[[在同一个运营者的网络内]{style="font-family:宋体"}[J0]{lang="EN-US"}]{#struct_0_x4619_57162_x684038345}[字节可为任意字符，而在两个不同运营者的网络边界处要使设备收、发两端的]{style="font-family:宋体"}[J0]{lang="EN-US"}[字节相匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x576151767}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x683972809}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧的再生段踪迹字节]{style="font-family:宋体"}[J0]{lang="EN-US"}[为]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x49325032}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] flag j0 sdh ff]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683907273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_1846780700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[frame-format]{lang="EN-US"}**]{#struct_0_x4619_57162_x683841737}
:::

::: {#-1585266344 .myid}
[]{#_Toc404783746}[]{#struct_0_x4619_57162_x881083893}[]{#_Toc356657156}

**POS接口 \-- POS接口配置命令 \-- flag j1**

------------------------------------------------------------------------

[**[flag]{lang="EN-US"}**]{#struct_0_x4619_57162_x683251913}[ ]{lang="EN-US"}**[j1]{lang="DA"}**[命令用来配置]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[帧的通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo flag]{lang="EN-US"}**]{#struct_0_x4619_57162_1499773155}[ ]{lang="EN-US"}**[j1]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683186377}

[**[flag]{lang="DA"}**]{#struct_0_x4619_57162_1050357145}[ **j1** { **sdh** \| **sonet** } *flag-value*]{lang="DA"}

[**[undo flag]{lang="DA"}**]{#struct_0_x4619_57162_x683776202}[ **j1** { **sdh** \| **sonet** }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x871092670}

[[系统使用]{style="font-family:宋体"}[SDH]{lang="EN-US"}]{#struct_0_x4619_57162_x683710666}[帧格式的缺省值，]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[的缺省值为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1282718450}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x683645130}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1061850161}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x683579594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x853273452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x684038346}

[*[flag-value]{lang="EN-US"}*]{#struct_0_x4619_57162_x576086231}[：通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[。]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_x4619_57162_x683972810}[：帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x4619_57162_x48866281}[：帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x683907274}

[[通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}]{#struct_0_x4619_57162_1846453020}[属于高阶通道开销字节，用于检测两个接口之间的连接在通道层次上的连续性。]{style="font-family:宋体"}

[[J1]{lang="EN-US"}]{#struct_0_x4619_57162_x683841738}[字节的设置一定要使收]{style="font-family:宋体"}[/]{lang="EN-US"}[发两端相匹配，否则会产生告警。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x881935861}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x683251914}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧的通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[为]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x683186378}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] flag j1 sdh aabbcc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1050029465}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_x683776203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag j1 ignore]{lang="EN-US"}**]{#struct_0_x4619_57162_x871027134}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[frame-format]{lang="EN-US"}**]{#struct_0_x4619_57162_x392214365}
:::

::::: {#1537804201 .myid}
[]{#_Toc404783747}[]{#struct_0_x4619_57162_x1955107869}[]{#_Toc366242904}[]{#_Toc366519271}[]{#_Toc366680916}[]{#_Toc252280729}[]{#_Toc252280730}[]{#_Toc252280731}[]{#_Toc252280732}[]{#_Toc252280733}[]{#_Toc252280734}[]{#_Toc252280735}[]{#_Toc252280736}[]{#_Toc252280737}[]{#_Toc252280738}[]{#_Toc252280739}[]{#_Toc252280740}[]{#_Toc252280768}[]{#_Toc252193498}[]{#_Toc252280770}[]{#_Toc252193499}[]{#_Toc252280771}[]{#_Toc252193500}[]{#_Toc252280772}[]{#_Toc252193501}[]{#_Toc252280773}[]{#_Toc252193502}[]{#_Toc252280774}[]{#_Toc252193503}[]{#_Toc252280775}[]{#_Toc252193504}[]{#_Toc252280776}[]{#_Toc252193505}[]{#_Toc252280777}[]{#_Toc252193506}[]{#_Toc252280778}[]{#_Toc252193507}[]{#_Toc252280779}[]{#_Toc252193508}[]{#_Toc252280780}[]{#_Toc252193509}[]{#_Toc252280781}[]{#_Toc252193525}[]{#_Toc252280797}[]{#_Toc366242905}[]{#_Toc366519272}[]{#_Toc366680917}[]{#_Toc366242906}[]{#_Toc366519273}[]{#_Toc366680918}[]{#_Toc366242907}[]{#_Toc366519274}[]{#_Toc366680919}[]{#_Toc366242908}[]{#_Toc366519275}[]{#_Toc366680920}[]{#_Toc366242909}[]{#_Toc366519276}[]{#_Toc366680921}[]{#_Toc366242910}[]{#_Toc366519277}[]{#_Toc366680922}[]{#_Toc366242911}[]{#_Toc366519278}[]{#_Toc366680923}[]{#_Toc366242912}[]{#_Toc366519279}[]{#_Toc366680924}[]{#_Toc366242913}[]{#_Toc366519280}[]{#_Toc366680925}[]{#_Toc366242914}[]{#_Toc366519281}[]{#_Toc366680926}[]{#_Toc366242915}[]{#_Toc366519282}[]{#_Toc366680927}[]{#_Toc366242916}[]{#_Toc366519283}[]{#_Toc366680928}[]{#_Toc366242917}[]{#_Toc366519284}[]{#_Toc366680929}[]{#_Toc366242918}[]{#_Toc366519285}[]{#_Toc366680930}[]{#_Toc366242919}[]{#_Toc366519286}[]{#_Toc366680931}[]{#_Toc366242920}[]{#_Toc366519287}[]{#_Toc366680932}[]{#_Toc366242921}[]{#_Toc366519288}[]{#_Toc366680933}[]{#_Toc366242922}[]{#_Toc366519289}[]{#_Toc366680934}[]{#_Toc366242923}[]{#_Toc366519290}[]{#_Toc366680935}[]{#_Hlt12766582}[]{#_Toc366242924}[]{#_Toc366519291}[]{#_Toc366680936}[]{#_Toc366242925}[]{#_Toc366519292}[]{#_Toc366680937}[]{#_Toc366242926}[]{#_Toc366519293}[]{#_Toc366680938}[]{#_Toc366242927}[]{#_Toc366519294}[]{#_Toc366680939}[]{#_Toc366242928}[]{#_Toc366519295}[]{#_Toc366680940}[]{#_Toc366242929}[]{#_Toc366519296}[]{#_Toc366680941}[]{#_Toc366242930}[]{#_Toc366519297}[]{#_Toc366680942}[]{#_Toc366242931}[]{#_Toc366519298}[]{#_Toc366680943}[]{#_Toc366242932}[]{#_Toc366519299}[]{#_Toc366680944}[]{#_Toc366242933}[]{#_Toc366519300}[]{#_Toc366680945}[]{#_Toc366242934}[]{#_Toc366519301}[]{#_Toc366680946}[]{#_Toc366242935}[]{#_Toc366519302}[]{#_Toc366680947}[]{#_Toc366242936}[]{#_Toc366519303}[]{#_Toc366680948}[]{#_Toc366242937}[]{#_Toc366519304}[]{#_Toc366680949}[]{#_Toc366242938}[]{#_Toc366519305}[]{#_Toc366680950}

**POS接口 \-- POS接口配置命令 \-- flag j1 ignore**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_x2017138330}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_x446448258}
:::

[ ]{lang="EN-US"}

[**[flag j1 ignore]{lang="EN-US"}**]{#struct_0_x4619_57162_1929216231}[命令用来配置忽略对通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[的检查。]{style="font-family:宋体"}

[**[undo flag j1 ignore]{lang="EN-US"}**]{#struct_0_x4619_57162_864832233}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_615941898}

[**[flag j1 ignore]{lang="EN-US"}**]{#struct_0_x4619_57162_1711123432}

[**[undo flag j1 ignore]{lang="EN-US"}**]{#struct_0_x4619_57162_538683189}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x645473896}

[[需要对通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}]{#struct_0_x4619_57162_x171205445}[进行检查。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x681877590}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x1131109561}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x317711549}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_450190881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_615876362}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_634300598}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_416270472}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[忽略对通道踪迹字节]{style="font-family:宋体"}[J1]{lang="EN-US"}[的检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x1350626920}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] flag j1 ignore]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1208367496}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**]{#struct_0_x4619_57162_x459439657}**[ j1]{lang="EN-US"}**
:::::

::::::: {#596268407 .myid}
[]{#_Toc263323270}[]{#_Toc252280799}[]{#_Toc404783748}[]{#struct_0_x4619_57162_x667868471}[]{#_Toc309912022}[]{#_Toc263067851}[]{#_Toc207010338}[]{#_Toc207010071}[]{#_Toc173120894}

**POS接口 \-- POS接口配置命令 \-- flow-interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4619_57162_x1341293330}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_615810826}
:::

[ ]{lang="EN-US"}

[**[flow-interval]{lang="EN-US"}**]{#struct_0_x4619_57162_1356246021}[命令用来配置接口统计报文信息的时间间隔。]{style="font-family:宋体"}

[**[undo flow-interval]{lang="EN-US"}**]{#struct_0_x4619_57162_1459972527}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_2125150898}

[**[flow-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x4619_57162_x1261820155}

[**[undo flow-interval]{lang="EN-US"}**]{#struct_0_x4619_57162_x1473218465}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1319322423}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4619_57162_89543072}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1968839199}

[[系统视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}]{#struct_0_x4619_57162_615745290}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4619_57162_x414638638}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_1741322164}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x174630204}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x146799935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x940561689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_753698258}

[*[interval]{lang="EN-US"}*]{#struct_0_x4619_57162_734979499}[：接口统计信息的时间间隔值，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[（即取值必须为]{style="font-family:宋体"}[5]{lang="EN-US"}[的整数倍）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x891186954}

[[用户可以配置接口统计报文信息的时间间隔：]{style="font-family:宋体"}]{#struct_0_x4619_57162_1904545493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统视图下的配置对所有接口生效；]{style="font-family:宋体"}]{#struct_0_x4619_57162_x891907850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口视图下的配置只对当前接口生效。]{style="font-family:宋体"}]{#struct_0_x4619_57162_1496750882}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1860261656}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_616728330}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的统计信息时间间隔为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1135383510}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] flow-interval 180]{lang="EN-US"}
:::::::

::: {#1701559760 .myid}
[]{#_Toc404783749}[]{#struct_0_x4619_57162_x1571386918}

**POS接口 \-- POS接口配置命令 \-- frame-format**

------------------------------------------------------------------------

[**[frame-format]{lang="SV"}**]{#struct_0_x4619_57162_1826215803}[命令用来设定]{style="font-family:宋体"}[POS]{lang="SV"}[接口的帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo frame-format]{lang="SV"}**]{#struct_0_x4619_57162_x648489391}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_585902793}

[**[frame-format]{lang="SV"}**]{#struct_0_x4619_57162_141943761}[ { **sdh** \| **sonet** }]{lang="SV"}

[**[undo]{lang="SV"}**]{#struct_0_x4619_57162_704739643}[ **frame-format**]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_616662794}

[[帧格式为]{style="font-family:宋体"}]{#struct_0_x4619_57162_1933927770}[SDH]{lang="SV"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_264943142}

[[POS]{lang="SV"}]{#struct_0_x4619_57162_x1680298895}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x385066277}

[[network-admin]{lang="SV"}]{#struct_0_x4619_57162_230501689}

[[mdc-admin]{lang="SV"}]{#struct_0_x4619_57162_49741976}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1195797421}

[**[sdh]{lang="SV"}**]{#struct_0_x4619_57162_x697578263}[：]{style="font-family:宋体"}[帧格式为]{style="font-family:宋体"}[SDH]{lang="SV"}[。]{style="font-family:宋体"}

[**[sonet]{lang="SV"}**]{#struct_0_x4619_57162_616204039}[：]{style="font-family:宋体"}[帧格式为]{style="font-family:宋体"}[SONET]{lang="SV"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1374762576}

[[通过]{style="font-family:宋体"}]{#struct_0_x4619_57162_70196707}**[flag ]{lang="SV"}[j0]{lang="DA"}**[和]{style="font-family:宋体"}**[flag]{lang="SV"}**[ ]{lang="SV"}**[j1]{lang="DA"}**[命令设置开销字节时，需要与帧格式匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x179833700}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1893037982}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[SONET]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x572207808}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] frame-format sonet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1085257501}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**]{#struct_0_x4619_57162_x126983749}**[ ]{lang="EN-US"}[j0]{lang="DA"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flag]{lang="EN-US"}**]{#struct_0_x4619_57162_x683251916}[ ]{lang="EN-US"}**[j1]{lang="DA"}**
:::

::: {#909387163 .myid}
[]{#_Toc263323271}[]{#_Toc252280800}[]{#_Toc404783750}[]{#struct_0_x4619_57162_616138503}

**POS接口 \-- POS接口配置命令 \-- interface pos**

------------------------------------------------------------------------

[**[interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_x79135572}[命令用来进入]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口视图。在进入]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口视图之前，如果指定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口不存在，则先创建]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口，再进入该]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口的视图。]{style="font-family:宋体"}

[**[undo interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_320504754}[命令用来删除]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1357678283}

[**[interface pos]{lang="EN-US"}**[ { *interface-number* \| *interface-number.subnumber* \[ **p2mp** \| **p2p** \] }]{lang="EN-US"}]{#struct_0_x4619_57162_x386022184}

[**[undo interface pos]{lang="EN-US"}**[ *interface-number.subnumber*]{lang="EN-US"}]{#struct_0_x4619_57162_x664118584}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1459715040}

[[不存在]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x4619_57162_1332272557}[子接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1168441706}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4619_57162_x669964948}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_616072967}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x375388928}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_932535624}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x637835055}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x4619_57162_878418956}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_x4619_57162_x1193451294}[：]{style="font-family:
宋体"}[POS]{lang="EN-US"}[子接口编号，其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[p2mp]{lang="EN-US"}**]{#struct_0_x4619_57162_x612386836}[：点到多点子接口。子接口缺省为]{style="font-family:宋体"}**[p2mp]{lang="EN-US"}**[类型。]{style="font-family:宋体"}

[**[p2p]{lang="EN-US"}**]{#struct_0_x4619_57162_207797134}[：点到点子接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_330019486}

[[只有]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x4619_57162_616007431}[主接口上封装的链路层协议为]{style="font-family:宋体"}[FR]{lang="EN-US"}[时，才能创建子接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1624897356}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_477548643}[创建]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口]{style="font-family:宋体"}[POS2/2/0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_565369898}

[\[Sysname\] interface pos 2/2/0.1]{lang="EN-US"}

[\[Sysname-Pos2/2/0.1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1582348706}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[link-protocol]{lang="EN-US"}**]{#struct_0_x4619_57162_x904801604}
:::

::::::: {#1002176090 .myid}
[]{#_Toc404783751}[]{#struct_0_x4619_57162_x907712895}

**POS接口 \-- POS接口配置命令 \-- link-delay**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image003.jpg){width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_1696335960}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_615941895}
:::

[ ]{lang="EN-US"}

[**[link-delay]{lang="EN-US"}**]{#struct_0_x4619_57162_1711123429}[命令用来设置接口物理连接状态抑制时间，即在接口发生]{style="font-family:宋体"}[up]{lang="EN-US"}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[的时候，需要经过连接状态抑制时间后，接口状态才能变为]{style="font-family:宋体"}[up]{lang="EN-US"}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo link-delay]{lang="EN-US"}**]{#struct_0_x4619_57162_539404086}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1971931047}

[**[link-delay msec ]{lang="EN-US"}***[milliseconds]{lang="EN-US"}*]{#struct_0_x4619_57162_x1741242551}

[**[undo link-delay]{lang="EN-US"}**]{#struct_0_x4619_57162_429269361}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x854530400}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4619_57162_1991570026}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_86857736}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_615876359}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x939677525}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_246711554}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1859620333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_914171084}

[**[msec ]{lang="EN-US"}***[milliseconds]{lang="EN-US"}*]{#struct_0_x4619_57162_x2070519423}[：接口物理连接状态抑制时间，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1126753072}

[[使用该命令可以防止短时间内的接口物理连接状态变化对正常业务的影响。]{style="font-family:宋体"}]{#struct_0_x4619_57162_x652373673}

[[需要注意的是，本命令和]{style="font-family:宋体"}**[dampening]{lang="EN-US"}**]{#struct_0_x4619_57162_x2017203867}[命令不能同时使用。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image003.jpg){#图片 3 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_65508463}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令对]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_615810823}[up]{lang="EN-US"}[或]{style="font-family:KaiTi_GB2312"}[down]{lang="EN-US"}[抑制的支持情况与设备的型号有关，请以设备的实际情况为准。即有些设备对]{style="font-family:KaiTi_GB2312"}[up]{lang="EN-US"}[进行抑制，有些设备对]{style="font-family:KaiTi_GB2312"}[down]{lang="EN-US"}[进行抑制，有些设备同时对]{style="font-family:KaiTi_GB2312"}[up/down]{lang="EN-US"}[进行抑制。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1356246016}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1459775920}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口物理连接状态抑制时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，即在]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口发生]{style="font-family:宋体"}[up]{lang="EN-US"}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[的时候，需要经过]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒后，接口状态才能变为]{style="font-family:宋体"}[up]{lang="EN-US"}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_527293867}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] link-delay msec 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x2017138331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dampening]{lang="EN-US"}**]{#struct_0_x4619_57162_x2012532199}
:::::::

::: {#232606835 .myid}
[]{#_Toc404783752}[]{#struct_0_x4619_57162_x698647009}[]{#_Toc263323272}[]{#_Toc252280801}

**POS接口 \-- POS接口配置命令 \-- link-protocol**

------------------------------------------------------------------------

[**[link-protocol]{lang="EN-US"}**]{#struct_0_x4619_57162_x1567057151}[命令用来配置接口的链路协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1526485811}

[**[link-protocol]{lang="EN-US"}**[ { **fr** \| **hdlc** \| **ppp** }]{lang="EN-US"}]{#struct_0_x4619_57162_465777527}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_223136110}

[[接口的链路协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x4619_57162_615745287}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1924013529}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x1598975565}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1432097229}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1225373516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1634168363}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_714746195}

[**[fr]{lang="EN-US"}**]{#struct_0_x4619_57162_x2115396094}[：使用帧中继作为接口的链路层协议。]{style="font-family:宋体"}

[**[hdlc]{lang="EN-US"}**]{#struct_0_x4619_57162_x324717760}[：使用]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[作为接口的链路层协议。]{style="font-family:宋体"}

[**[ppp]{lang="EN-US"}**]{#struct_0_x4619_57162_616728327}[：使用]{style="font-family:宋体"}[PPP]{lang="EN-US"}[作为接口的链路层协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x820931623}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1251505750}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的链路层协议为]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1649597796}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] link-protocol hdlc]{lang="EN-US"}
:::

::: {#405613428 .myid}
[]{#_Toc404783753}[]{#struct_0_x4619_57162_1443953714}[]{#_Toc263323273}[]{#_Toc252280802}

**POS接口 \-- POS接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_x4619_57162_x727658987}[命令用来开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的环回功能。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x4619_57162_x344873351}[命令用来关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的环回功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1701733070}

[**[loopback]{lang="EN-US"}**[ { **local** \| **remote** }]{lang="EN-US"}]{#struct_0_x4619_57162_616662791}

[**[undo]{lang="EN-US"}**[ **loopback**]{lang="EN-US"}]{#struct_0_x4619_57162_1933927775}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_264746534}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_2036128267}[接口的环回功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_2014096651}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x1475026465}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x712480880}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1123757404}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_527087598}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_616204040}

[**[local]{lang="EN-US"}**]{#struct_0_x4619_57162_x2110900665}[：开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口对内环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x4619_57162_253642871}[：开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_332377588}

[[只有在进行某些特殊功能测试的时候，才对接口设置环回功能。]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1255551576}

[[如果对]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x4619_57162_151406435}[接口封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协议，设置环回后，物理层的状态会上报为]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}

[[环回功能和]{style="font-family:宋体"}**[clock slave]{lang="EN-US"}**]{#struct_0_x4619_57162_795596693}[不能同时设置，否则]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口会无法对接成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1263513387}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1118607176}[开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[对内环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_616138504}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] loopback local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x79135569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock]{lang="EN-US"}**]{#struct_0_x4619_57162_x1635810389}
:::

::: {#988247972 .myid}
[]{#_Toc404783754}[]{#struct_0_x4619_57162_x1442526957}[]{#_Toc263323274}[]{#_Toc252280803}

**POS接口 \-- POS接口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x4619_57162_1030912801}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x4619_57162_107674922}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1999693003}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x4619_57162_x1814156221}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x4619_57162_396033951}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_616072968}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4619_57162_x375388933}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_932207945}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_1406954206}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1608125137}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x2045018787}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1095530965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_2102878065}

[*[size]{lang="EN-US"}*]{#struct_0_x4619_57162_x142230721}[：]{style="font-family:宋体"}[MTU]{lang="EN-US"}[的大小，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_616007432}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x4619_57162_x1624897355}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_x4619_57162_2043632584}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1493782105}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_553676566}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1181597112}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] mtu 1430]{lang="EN-US"}
:::

::::: {#-742084413 .myid}
[]{#_Toc404783755}[]{#struct_0_x4619_57162_x182463327}[]{#_Toc263323275}[]{#_Toc252280804}

**POS接口 \-- POS接口配置命令 \-- port-type switch**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image003.jpg){#图片 5 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_2055000145}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_615941896}
:::

[ ]{lang="EN-US"}

[**[port-type switch]{lang="EN-US"}**]{#struct_0_x4619_57162_1711123430}[命令用来在]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口和三层]{style="font-family:宋体"}[GE]{lang="EN-US"}[接口间进行类型切换。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_538814261}

[[在]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x1778105087}[接口视图下：]{style="font-family:宋体"}

[**[port-type switch gigabitethernet]{lang="EN-US"}**]{#struct_0_x4619_57162_x2137658722}

[[在三层]{style="font-family:宋体"}[GE]{lang="EN-US"}]{#struct_0_x4619_57162_477220663}[接口视图下：]{style="font-family:宋体"}

[**[port-type switch pos]{lang="EN-US"}**]{#struct_0_x4619_57162_753368346}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_210857735}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x2105379488}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[GE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x523928922}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_516400790}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1661825797}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_615876360}

[**[gigabitethernet]{lang="EN-US"}**]{#struct_0_x4619_57162_634300596}[：将当前]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口切换为三层]{style="font-family:宋体"}[GE]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[pos]{lang="EN-US"}**]{#struct_0_x4619_57162_x1778498303}[：]{style="font-family:宋体"}[将当前三层]{style="font-family:宋体"}[GE]{lang="EN-US"}[接口切换为]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_416270462}

[[接口类型切换后，原接口删除并创建新的接口，切换后的接口编号与切换前保持一致。]{style="font-family:宋体"}]{#struct_0_x4619_57162_605688216}

[[命令执行成功后会切换到新接口的接口视图下。]{style="font-family:宋体"}]{#struct_0_x4619_57162_1729938877}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1277468592}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x2107863118}[将]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[切换为]{style="font-family:宋体"}[GigabitEthernet2/2/0]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1729938875}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] port-type switch gigabitethernet]{lang="EN-US"}

[Changing port type can result in loss of port configuration. Are you sure to continue? \[Y/N\]:y]{lang="EN-US"}

[\[Sysname-GigabitEthernet2/2/0\]]{lang="EN-US"}
:::::

::: {#2052875588 .myid}
[]{#_Toc404783756}[]{#struct_0_x4619_57162_615810824}[]{#_Toc263323276}[]{#_Toc252280805}[]{#_Toc213490054}[]{#_Toc207010309}[]{#_Toc207010042}[]{#_Toc139515326}

**POS接口 \-- POS接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x4619_57162_1356246023}[命令用来清除]{style="font-family:
宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1460103599}

[**[reset counters interface]{lang="EN-US"}**[ \[ **pos** \[ *interface-number* ]{lang="EN-US"}[\| *interface-number.subnumber* \] \]]{lang="EN-US"}]{#struct_0_x4619_57162_x506744457}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1433222157}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4619_57162_1441561452}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1357101003}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1299992489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_945594960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_615745288}

[**[pos]{lang="EN-US"}**]{#struct_0_x4619_57162_1924013530}[：清除]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x4619_57162_x1599434318}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_x4619_57162_882832028}[：]{style="font-family:
宋体"}[POS]{lang="EN-US"}[子接口编号，其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1507752101}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x4619_57162_1342388818}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x4619_57162_1910237394}**[pos]{lang="EN-US"}**[参数，则清除所有接口的统计信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_x4619_57162_1441036793}**[pos]{lang="EN-US"}**[参数而不指定接口编号，则清除所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的统计信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{style="font-family:宋体"}]{#struct_0_x4619_57162_1762560043}**[pos]{lang="EN-US"}**[和接口编号，则清除指定]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1781968092}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_616728328}[清除]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface pos 2/2/0]{lang="EN-US"}]{#struct_0_x4619_57162_x820931618}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1252095577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}**]{#struct_0_x4619_57162_1114234383}**[pos]{lang="EN-US"}**
:::

::: {#679047146 .myid}
[]{#_Toc404783757}[]{#struct_0_x4619_57162_1069012939}[]{#_Toc263323277}[]{#_Toc252280806}[]{#_Toc214762441}

**POS接口 \-- POS接口配置命令 \-- scramble**

------------------------------------------------------------------------

[**[scramble]{lang="EN-US"}**]{#struct_0_x4619_57162_1144012035}[命令用来打开接口对载荷的加扰功能。]{style="font-family:宋体"}

[**[undo scramble]{lang="EN-US"}**]{#struct_0_x4619_57162_x1953277279}[命令用来关闭加扰功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x601226912}

[**[scramble]{lang="EN-US"}**]{#struct_0_x4619_57162_616662792}

[**[undo]{lang="EN-US"}**[ **scramble**]{lang="EN-US"}]{#struct_0_x4619_57162_1933927772}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_265074214}

[[接口对载荷的加扰功能处于打开状态。]{style="font-family:宋体"}]{#struct_0_x4619_57162_947007294}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1601518537}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_1355859999}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x783068083}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_2046992165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_849562832}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_616204037}

[[开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x4619_57162_1374762566}[或]{style="font-family:宋体"}[0]{lang="EN-US"}[，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端接口都打开或关闭对载荷的加扰功能，才能对接成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_70196706}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x2136148836}[打开]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[对载荷的加扰功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_616138501}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] scramble]{lang="EN-US"}
:::

::: {#1170655049 .myid}
[]{#_Toc404783758}[]{#struct_0_x4619_57162_x79135574}[]{#_Toc263323279}[]{#_Toc252280808}[]{#_Toc182036367}[]{#_Toc136937634}

**POS接口 \-- POS接口配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x4619_57162_320504752}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x4619_57162_x1357678281}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_776777230}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x4619_57162_x2019548490}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x4619_57162_284868320}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1990968060}

[[接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_x4619_57162_x1057115472}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x212838190}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_616072965}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x375388930}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_932011337}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_367439773}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x813862101}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x1206654485}[关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x1195417971}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] shutdown]{lang="EN-US"}
:::

::::: {#1279049909 .myid}
[]{#_Toc404783759}[]{#struct_0_x4619_57162_1874544443}[]{#_Toc366853702}

**POS接口 \-- POS接口配置命令 \-- snmp-agent trap enable { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image001.png){width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_x268892468}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_245566204}
:::

**[ ]{lang="EN-US"}**

[**[snmp-agent trap enable]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_1873954618}[命令用来开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_x130021811}[命令用来关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_307522835}

[**[snmp-agent trap enable]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_x1088911514}

[**[undo snmp-agent trap enable]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_x1153238175}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x812921753}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_744906340}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1592440245}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x818391004}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x50111071}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1874020154}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1017826038}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_610415512}

[[B1/B2/B3]{lang="EN-US"}]{#struct_0_x4619_57162_x1430434551}[告警都是用于指示]{style="font-family:宋体"}[SDH]{lang="EN-US"}[体制线路的当前信号传输性能的，只是三者关注的信号层次不一样：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B1]{lang="EN-US"}]{#struct_0_x4619_57162_x604811658}[检验的是当前传输信号]{style="font-family:宋体"}[STM-N]{lang="EN-US"}[帧的整体误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B2]{lang="EN-US"}]{#struct_0_x4619_57162_x1623366019}[检验的是传输信号基本组成单元]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧的误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B3]{lang="EN-US"}]{#struct_0_x4619_57162_x993729389}[检验的是]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧封装的复用信号（]{style="font-family:宋体"}[VC3]{lang="EN-US"}[或]{style="font-family:宋体"}[VC4]{lang="EN-US"}[帧）的误码情况。]{style="font-family:宋体"}

[[当开启了]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x1151005475}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能后，设备将在]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的误码超过]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警门限时生成告警信息。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1864029243}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1624646547}[关闭]{style="font-family:宋体"}[POS2/2/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[B1]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1873823546}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] undo snmp-agent trap enable b1-tca]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1685215074}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[threshold]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_1524901605}
:::::

::: {#-738165832 .myid}
[]{#_Toc404783760}[]{#struct_0_x4619_57162_x540389054}[]{#_Toc263323278}[]{#_Toc252280807}

**POS接口 \-- POS接口配置命令 \-- speed**

------------------------------------------------------------------------

[**[speed]{lang="EN-US"}**]{#struct_0_x4619_57162_616007429}[命令用来设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的速率。]{style="font-family:宋体"}

[**[undo speed]{lang="EN-US"}**]{#struct_0_x4619_57162_331417788}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_2140107031}

[**[speed ]{lang="EN-US"}***[speed-value]{lang="EN-US"}*]{#struct_0_x4619_57162_x2079330326}

[**[undo speed]{lang="EN-US"}**]{#struct_0_x4619_57162_793463073}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x271254928}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x999762873}[接口的速率为]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1851276561}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x827889229}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_615941893}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1711123427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_539010870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x502488398}

[*[speed-value]{lang="EN-US"}*]{#struct_0_x4619_57162_x2014800318}[：设置的速率值，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_127353708}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_1583446899}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的速率为]{style="font-family:宋体"}[2.5G]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x2088017876}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] speed 2500]{lang="EN-US"}
:::

::::: {#-1726874890 .myid}
[]{#_Toc404783761}[]{#struct_0_x4619_57162_x1421602248}[]{#_Toc263323280}[]{#_Toc252280809}

**POS接口 \-- POS接口配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image003.jpg){#图片 8 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_615876357}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_x939677519}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[开启本功能后可能需要耗费大量系统资源，请谨慎使用。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_246449411}
:::

**[ ]{lang="EN-US"}**

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x4619_57162_x791340484}[命令用来开启子接口的速率统计功能。]{style="font-family:
宋体"}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x4619_57162_x1609292325}[命令用来关闭子接口的速率统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1952144427}

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x4619_57162_1945129604}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_x4619_57162_436362538}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1632863886}

[[子接口的速率统计功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x4619_57162_615810821}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1356246018}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_1459382704}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1813824514}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1217453909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1787012816}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x976515524}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x592093137}[开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的子接口速率统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_615745285}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] sub-interface rate-statistic]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1924013527}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x4619_57162_x1599106637}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface pos]{lang="EN-US"}**]{#struct_0_x4619_57162_1504387786}
:::::

::::: {#-1291593385 .myid}
[]{#_Toc404783762}[]{#struct_0_x4619_57162_1788576213}[]{#_Toc263323281}[]{#_Toc252280810}[]{#_Toc130049687}[]{#_Toc129668368}[]{#_Toc129527974}[]{#_Toc82589828}[]{#_Toc74652476}[]{#_Toc182037637}[]{#_Toc182039372}[]{#_Toc182043417}

**POS接口 \-- POS接口配置命令 \-- threshold**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image003.jpg){#图片 9 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_x759472125}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_x1777727148}
:::

[ ]{lang="EN-US"}

[**[threshold]{lang="EN-US"}**]{#struct_0_x4619_57162_1379185453}[命令用来设置接口的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限和]{style="font-family:宋体"}[（]{style="font-family:宋体"}[或]{style="font-family:宋体"}[）]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限。]{style="font-family:宋体"}

[**[undo threshold]{lang="EN-US"}**]{#struct_0_x4619_57162_559387326}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_616728325}

[**[threshold]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4619_57162_x820931621}[{ **sd** *sdvalue* \| **sf** *sfvalue* } \*]{lang="FR"}

[**[undo threshold]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4619_57162_1251636822}[\[ **sd** \| **sf** \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_114780459}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4619_57162_x869633943}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_77823835}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_700379731}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1658742641}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x1134150795}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_616662789}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x404724393}

[**[sd]{lang="EN-US"}**]{#struct_0_x4619_57162_x312687622}[：表示配置]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警门限。]{style="font-family:宋体"}

[*[sd]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_x4619_57162_x1291827336}[：以]{style="font-family:宋体"}[10e-sd*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sd]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SD]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_x4619_57162_1587312733}[：表示配置]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警门限。]{style="font-family:宋体"}

[*[sf]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_x4619_57162_x1553887653}[：以]{style="font-family:宋体"}[10e-sf*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sf]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SF]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_138794241}

[[SD]{lang="EN-US"}]{#struct_0_x4619_57162_1321635094}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警都是用于指示当前线路性能的，相比较而言，]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警比]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警更为严重，]{style="font-family:宋体"}[SF]{lang="EN-US"}[的误码率门限一般会比]{style="font-family:宋体"}[SD]{lang="EN-US"}[的误码率门限高，也就是说，当出现少量误码时，设备产生]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警，当误码率增大到一定程度时，说明线路质量严重下降，此时设备才产生]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。因此，应使]{style="font-family:宋体"}[SD]{lang="EN-US"}[的告警门限小于]{style="font-family:宋体"}[SF]{lang="EN-US"}[的告警门限，]{style="font-family:宋体"}*[sdvalue]{lang="EN-US"}*[的值应大于]{style="font-family:宋体"}*[sfvalue]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x3942956}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_616204038}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限为]{style="font-family:宋体"}[10e-4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1374762575}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] threshold sd 4]{lang="EN-US"}
:::::

::::: {#146005858 .myid}
[]{#_Toc404783763}[]{#struct_0_x4619_57162_1873626938}[]{#_Toc366853701}

**POS接口 \-- POS接口配置命令 \-- threshold { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS接口命令.files/image001.png){#图片 15 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4619_57162_1075376228}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4619_57162_792391886}
:::

**[ ]{lang="EN-US"}**

[**[threshold]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_x662454247}[命令用来设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警门限。]{style="font-family:宋体"}

[**[undo threshold]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_1161884595}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1612896969}

[**[threshold]{lang="EN-US"}**[ { **b1-tca** *b1value* \| **b2-tca** *b2value* \| **b3-tca** *b3value* }]{lang="EN-US"}]{#struct_0_x4619_57162_419811936}

[**[undo threshold]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_1874478906}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1390710699}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4619_57162_1807308869}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x871577373}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x10401430}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x238042390}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_550357724}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x766873313}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1073446809}

[*[b1value]{lang="EN-US"}*]{#struct_0_x4619_57162_x1380782043}[：以]{style="font-family:宋体"}[10e-*b1value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[B1]{lang="EN-US"}[告警门限值，]{style="font-family:宋体"}*[b1value]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，值越大表示]{style="font-family:
宋体"}[B1]{lang="EN-US"}[告警门限越小。]{style="font-family:宋体"}

[*[b2value]{lang="EN-US"}*]{#struct_0_x4619_57162_974589129}[：以]{style="font-family:宋体"}[10e-*b2value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[B2]{lang="EN-US"}[告警门限值，]{style="font-family:宋体"}*[b2value]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，值越大表示]{style="font-family:
宋体"}[B2]{lang="EN-US"}[告警门限越小。]{style="font-family:宋体"}

[*[b3value]{lang="EN-US"}*]{#struct_0_x4619_57162_1874544442}[：以]{style="font-family:宋体"}[10e-*b3value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[B3]{lang="EN-US"}[告警门限值，]{style="font-family:宋体"}*[b3value]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，值越大表示]{style="font-family:
宋体"}[B3]{lang="EN-US"}[告警门限越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x268826932}

[[B1/B2/B3]{lang="EN-US"}]{#struct_0_x4619_57162_x1363092117}[告警都是用于指示]{style="font-family:宋体"}[SDH]{lang="EN-US"}[体制线路的当前信号传输性能的，只是三者关注的信号层次不一样：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B1]{lang="EN-US"}]{#struct_0_x4619_57162_239019417}[检验的是当前传输信号]{style="font-family:宋体"}[\--STM-N]{lang="EN-US"}[帧的整体误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B2]{lang="EN-US"}]{#struct_0_x4619_57162_x988078544}[检验的是传输信号基本组成单元]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧的误码情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B3]{lang="EN-US"}]{#struct_0_x4619_57162_618176298}[检验的是]{style="font-family:宋体"}[STM-1]{lang="EN-US"}[帧封装的复用信号（]{style="font-family:宋体"}[VC3]{lang="EN-US"}[或]{style="font-family:宋体"}[VC4]{lang="EN-US"}[帧）的误码情况。]{style="font-family:宋体"}

[[当开启了]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x4619_57162_1839689640}[接口的]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警功能后，设备将在]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的误码超过]{style="font-family:宋体"}[B1/B2/B3]{lang="EN-US"}[告警门限时生成告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_419382546}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_222339085}[配置]{style="font-family:宋体"}[POS2/2/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[B1]{lang="EN-US"}[告警门限为]{style="font-family:宋体"}[10e-4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_1873954621}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] threshold b1-tca 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x130480566}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent trap enable]{lang="EN-US"}**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]{lang="EN-US"}]{#struct_0_x4619_57162_1823203993}
:::::

::: {#1474946988 .myid}
[]{#_Toc404783764}[]{#struct_0_x4619_57162_70393315}[]{#_Toc323827378}[]{#_Toc317856915}[]{#_Toc309228573}[]{#_Toc205607563}

**POS接口 \-- POS接口配置命令 \-- timer-hold**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**]{#struct_0_x4619_57162_2127414717}[命令用来配置]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期。]{style="font-family:宋体"}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x4619_57162_1270320431}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x991611603}

[**[timer-hold]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x4619_57162_1273278924}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x4619_57162_885231727}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x577564993}

[[Keepalive]{lang="EN-US"}]{#struct_0_x4619_57162_x593574464}[报文的发送周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x79135571}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_320504755}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1357678284}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_17262343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x51031623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1038400398}

[*[seconds]{lang="EN-US"}*]{#struct_0_x4619_57162_x461564770}[：]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1284967532}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x4619_57162_x593574470}[、]{style="font-family:宋体"}[FR]{lang="EN-US"}[或]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[时，链路层会定期（可通过本命令修改）向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，从而上报链路层]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在速率非常低的链路上，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}]{#struct_0_x4619_57162_x593574469}[报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的收发。而接口在若干个（可通过]{style="font-family:宋体"}**[timer-hold ]{lang="EN-US"}[retry]{lang="EN-US"}**[命令修改）]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期后仍未收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，就认为链路发生故障，从而拆除链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_2117751183}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x593574471}[在]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_299624458}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] timer-hold 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1745077696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_x4619_57162_1745077694}
:::

::: {#518520923 .myid}
[]{#_Toc404783765}[]{#struct_0_x4619_57162_x58524473}

**POS接口 \-- POS接口配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_x4619_57162_1745077695}[命令用来配置在多少个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x4619_57162_1745077692}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x58131257}

[**[timer-hold]{lang="EN-US"}**[ **retry** *retry*]{lang="EN-US"}]{#struct_0_x4619_57162_1745077693}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x4619_57162_x58196793}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x1963941088}

[[在]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x4619_57162_1745077690}[个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1745077691}

[[POS]{lang="EN-US"}]{#struct_0_x4619_57162_x58327865}[接口视图]{style="font-family:宋体"}[/POS]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4619_57162_1745077688}

[[network-admin]{lang="EN-US"}]{#struct_0_x4619_57162_x58786618}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4619_57162_1745077689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x975911488}

[*[retry]{lang="EN-US"}*]{#struct_0_x4619_57162_x444887471}[：在多少个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x975911487}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x4619_57162_x975911490}[、]{style="font-family:宋体"}[FR]{lang="EN-US"}[或]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[时，链路层会定期（可通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改）向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在速率非常低的链路上，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}]{#struct_0_x4619_57162_x975911489}[报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的收发。而接口在若干个（可通过本命令修改）]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期后仍未收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，就认为链路发生故障，从而拆除链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x444953007}

[[\# ]{lang="EN-US"}]{#struct_0_x4619_57162_x975911492}[在]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[上，配置在]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4619_57162_x975911494}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] timer-hold retry 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4619_57162_x445149614}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_x4619_57162_x975911493}

[ ]{lang="EN-US"}
:::
