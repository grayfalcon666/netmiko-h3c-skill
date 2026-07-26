::: {#1742433432 .myid}
[]{#_Toc43285265}[]{#_Toc41205417}[]{#_Toc32638004}[]{#_Toc31422539}[]{#_Toc215479534}[]{#_Toc207017822}[]{#_Toc207011361}[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc139515317}[]{#_Toc137103150}[]{#_Toc317601815}[]{#_Toc309912009}[]{#_Toc404783906}[]{#struct_0_15224_x2020_251429913}[]{#_Toc345166888}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_15224_x2020_742205599}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_15224_x2020_374783120}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x2118799738}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_15224_x2020_x1721081484}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_15224_x2020_730775685}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x910101806}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_x943522909}[接口的期望带宽为]{style="font-family:宋体"}[0kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x503568391}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_1954321953}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x899960682}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1305552530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1982085648}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1338786179}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_15224_x2020_979225042}[：]{style="font-family:宋体"}[表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x2131069324}

[[接口的期望带宽会对下列内容有影响：]{style="font-size:10.0pt;font-family:宋体;color:black"}]{#struct_0_15224_x2020_x943457373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBQ]{lang="EN-US"}]{#struct_0_15224_x2020_1037355596}[队列带宽。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导]{style="font-family:宋体"}["中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[链路开销值。具体介绍请参见"三层技术]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;
color:black"}]{#struct_0_15224_x2020_x1809592784}[-IP]{lang="EN-US" style="font-size:
10.0pt;color:black"}[路由配置指导"中的"]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:black"}[OSPF]{lang="EN-US" style="font-size:
10.0pt;color:black"}["、]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:black"}["]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["]{lang="EN-US" style="font-family:宋体"}[和"]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:black"}[IS-IS]{lang="EN-US" style="font-size:10.0pt;color:black"}["]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:black"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1650266990}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x903075739}[配置]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[1000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15224_x2020_x405588090}

[\[Sysname\] interface loopback 1]{lang="EN-US"}

[\[Sysname-LoopBack1\] bandwidth 1000]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404783907}[]{#struct_0_15224_x2020_821270052}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_15224_x2020_x1840570711}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_792915648}

[**[default]{lang="EN-US"}**]{#struct_0_15224_x2020_x943391837}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1446544779}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_575893698}[接口视图]{style="font-family:宋体"}[/NULL]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1327257435}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1210957700}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_230652057}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1293740147}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_15224_x2020_1279525272}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_15224_x2020_1937478192}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x943326301}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x1682680501}[将]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15224_x2020_x868018789}

[\[Sysname\] interface loopback 1]{lang="EN-US"}

[\[Sysname-LoopBack1\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404783908}[]{#struct_0_15224_x2020_1346796416}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_15224_x2020_890013652}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_15224_x2020_x1812650294}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x273589046}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_15224_x2020_2013522161}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_15224_x2020_x1695543405}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x943260765}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_15224_x2020_x1732964186}["，比如：]{style="font-family:宋体"}[LoopBack1 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1900848613}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_x1057175623}[接口视图]{style="font-family:宋体"}[/NULL]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x898644325}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_894695633}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x796155163}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1105363824}

[*[text]{lang="EN-US"}*]{#struct_0_15224_x2020_597012340}[：接口的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x2126079873}

[[当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。]{style="font-family:宋体"}]{#struct_0_15224_x2020_x943195229}

[[配置的描述信息可通过命令行]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_15224_x2020_267039480}[查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_261290574}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x2147003097}[设置]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[for RouterID]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15224_x2020_x365469622}

[\[Sysname\] interface loopback 1]{lang="EN-US"}

[\[Sysname-LoopBack1\] description for RouterID]{lang="EN-US"}
:::

::::: {#-1840765529 .myid}
[]{#_Toc119753038}[]{#_Toc43285274}[]{#_Toc41205424}[]{#_Toc32638016}[]{#_Toc31422551}[]{#_Toc215479535}[]{#_Toc207017823}[]{#_Toc119753037}[]{#_Toc43285282}[]{#_Toc41205432}[]{#_Toc32638025}[]{#_Toc31422560}[]{#_Toc404783909}[]{#struct_0_15224_x2020_x1196494583}[]{#_Toc333483531}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- display interface inloopback**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LoopBack接口、NULL接口和InLoopBack接口命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_15224_x2020_x372147541}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_15224_x2020_x2125969153}
:::

**[ ]{lang="EN-US"}**

[**[display interface inloopback]{lang="EN-US"}**]{#struct_0_15224_x2020_x943129693}[命令用来显示]{style="font-family:
宋体"}[InLoopBack]{lang="EN-US"}[接口的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x595645897}

[**[display interface ]{lang="EN-US"}**[\[ **inloopback** \[ **0** \] \] \[ **brief** \[ **description** \] \]]{lang="EN-US"}]{#struct_0_15224_x2020_x2081717184}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x266012064}

[[任意视图]{style="font-family:宋体"}]{#struct_0_15224_x2020_429197716}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_43955962}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1468739974}

[[network-operator]{lang="EN-US"}]{#struct_0_15224_x2020_1662591797}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x1180186678}

[[mdc-operator]{lang="EN-US"}]{#struct_0_15224_x2020_x943064157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x145801735}

[**[0]{lang="EN-US"}**]{#struct_0_15224_x2020_1537246830}[：]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_15224_x2020_1943481381}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_15224_x2020_252622837}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。对于]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}[接口，因为其描述信息只能为]{style="font-family:宋体"}[InLoopBack0 Interface]{lang="EN-US"}[，不能配置，所以，该参数对]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}[接口无意义。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1736258575}

[[查看]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_611175231}[接口的相关信息时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_15224_x2020_x1800340126}**[inloopback]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[因为设备只支持一个]{style="font-family:宋体"}]{#struct_0_15224_x2020_x514562940}[InLoopBack]{lang="EN-US"}[接口]{style="font-family:宋体"}[InLoopBack0]{lang="EN-US"}[，所以，只要指定]{style="font-family:宋体"}**[inloopback]{lang="EN-US"}**[参数，不管是否指定]{style="font-family:宋体"}**[0]{lang="EN-US"}**[参数，显示的都是]{style="font-family:宋体"}[InLoopBack0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_458287435}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x944047197}[显示指定接口]{style="font-family:宋体"}[InLoopBack0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface inloopback]{lang="EN-US"}]{#struct_0_15224_x2020_1283377498}

[InLoopBack0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP(spoofing)]{lang="EN-US"}

[Description: InLoopBack0 Interface]{lang="EN-US"}

[Maximum Transmit Unit: 1536]{lang="EN-US"}

[Physical: InLoopBack]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface inloopback]{lang="EN-US"}]{#struct_0_15224_x2020_x1022634657}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2019238878}[[字段]{style="font-family:黑体"}]{#struct_0_15224_x2020_659507221}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_15224_x2020_x943981661}

[[Current state]{lang="EN-US"}]{#struct_0_15224_x2020_x939030968}

[[接口当前的物理层状态。始终为]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_15224_x2020_2144854445}[，表示接口能收发报文]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_15224_x2020_1934386149}

[[链路层协议状态。始终为]{style="font-family:宋体"}[UP(spoofing)]{lang="EN-US"}]{#struct_0_15224_x2020_x1804850172}[，表示接口的链路层协议状态为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在，而是按需建立的]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_15224_x2020_418226635}

[[接口的描述字符串。只能为]{style="font-family:宋体"}[InLoopBack0 Interface]{lang="EN-US"}]{#struct_0_15224_x2020_1648118764}[，不可配置]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_15224_x2020_1434668618}

[[接口的最大传输单元。只能为]{style="font-family:宋体"}[1536]{lang="EN-US"}]{#struct_0_15224_x2020_1468643760}[，不可配置]{style="font-family:宋体"}

[[Physical: InLoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_x943457376}

[[接口的物理类型是]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_1037158988}

[[Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_1599257036}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_15224_x2020_x855454328}[秒钟的平均输入速率（只有接口支持统计功能时才显示该信息）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_15224_x2020_2020155423}[表示平均每秒输入的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x943391840}[表示平均每秒输入的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_1446217100}[表示平均每秒输入的包数]{lang="EN-US" style="font-family:宋体"}

[[Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_984874257}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_15224_x2020_1192458318}[秒钟的平均输出速率（只有接口支持统计功能时才显示该信息）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_15224_x2020_1426043728}[表示平均每秒输出的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x943326304}[表示平均每秒输出的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x1683008181}[表示平均每秒输出的包数]{lang="EN-US" style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_15224_x2020_1230329274}

[[接口输入的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）]{style="font-family:宋体"}]{#struct_0_15224_x2020_1878017402}

[[Onput: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_15224_x2020_1809742862}

[[接口输出的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）]{style="font-family:宋体"}]{#struct_0_15224_x2020_x943260768}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x1732767578}[显示]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface inloopback 0 brief]{lang="EN-US"}]{#struct_0_15224_x2020_1507942787}

[Brief information on interface(s) under route mode: ]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[InLoop0              UP   UP(s)    \--]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[[display interface inloopback brie]{lang="EN-US"}]{.FigureDescriptionChar}[f]{lang="EN-US"}]{#struct_0_15224_x2020_267760377}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2023705969}[[字段]{style="font-family:黑体"}]{#struct_0_15224_x2020_310746471}

[[描述]{style="font-family:黑体"}]{#struct_0_15224_x2020_x335417769}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_15224_x2020_648971464}

[[InLoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_1556032334}[接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_15224_x2020_2057845725}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_15224_x2020_x943129696}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_15224_x2020_x1002971186}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_15224_x2020_x595973577}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_15224_x2020_x1321940811}[属性值中带有]{style="font-family:宋体"}[(s)]{lang="EN-US"}[，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[、]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_15224_x2020_x1805055480}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_15224_x2020_1999276775}

[[Link]{lang="EN-US"}]{#struct_0_15224_x2020_x69844442}

[[接口物理连接状态。取值为]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_15224_x2020_x943064160}[，表示本链路物理上是连通的]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_15224_x2020_x146260484}

[[接口数据链路层协议状态，取值为]{style="font-family:宋体"}[UP(s)]{lang="EN-US"}]{#struct_0_15224_x2020_244060324}

[[Main IP]{lang="EN-US"}]{#struct_0_15224_x2020_x214973696}

[[接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_15224_x2020_1930982714}[地址]{style="font-family:宋体"}

[[因为]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_1754791417}[接口下不能配置命令行，所以该项对]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}[接口无意义]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_15224_x2020_x944047200}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_15224_x2020_x1437283997}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[因为]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_x1469776598}[接口下不能配置命令行，所以该项对]{style="font-family:宋体"}[InLoopBack]{lang="EN-US"}[接口无意义]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2004230743 .myid}
[]{#_Toc404783910}[]{#struct_0_15224_x2020_438097069}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- display interface loopback**

------------------------------------------------------------------------

[**[display interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_508256541}[命令用来显示]{style="font-family:
宋体"}[LoopBack]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x2039697957}

[**[display interface ]{lang="EN-US"}**[\[ **loopback** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_15224_x2020_x943981664}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x938834360}

[[任意视图]{style="font-family:宋体"}]{#struct_0_15224_x2020_1800343721}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1593856140}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1157612307}

[[network-operator]{lang="EN-US"}]{#struct_0_15224_x2020_1976581017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x1710833718}

[[mdc-operator]{lang="EN-US"}]{#struct_0_15224_x2020_x176530356}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1070792091}

[*[interface-number]{lang="EN-US"}*]{#struct_0_15224_x2020_x943522911}[：]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的编号，取值范围为已创建的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的编号。如果不指定接口编号，将显示所有已创建的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_15224_x2020_x504092678}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_15224_x2020_259825465}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_15224_x2020_679156824}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1105862224}

[**[display interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_x220186194}[命令用来显示]{style="font-family:
宋体"}[Loopback]{lang="EN-US"}[接口的相关信息。只有创建]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口后，才支持该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_15224_x2020_188290968}**[loopback]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_470500886}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1040141380}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x943457375}[显示]{style="font-family:宋体"}[LoopBack0]{lang="EN-US"}[接口的相关信息。（支持统计功能的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的显示信息）]{style="font-family:宋体"}

[[\<Sysname\> display interface loopback 0]{lang="EN-US"}]{#struct_0_15224_x2020_1036962380}

[LoopBack0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP(spoofing)]{lang="EN-US"}

[Description: LoopBack0 Interface]{lang="EN-US"}

[Bandwidth: 1000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1536]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Physical: Loopback]{lang="EN-US"}

[Last clearing of counters:  Never]{lang="EN-US"}

[Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_855375154}[显示]{style="font-family:宋体"}[LoopBack0]{lang="EN-US"}[接口的相关信息。（不支持统计功能的]{style="font-family:宋体"}[LoopBack0]{lang="EN-US"}[接口的显示信息）]{style="font-family:宋体"}

[[\<Sysname\> display interface loopback 0]{lang="EN-US"}]{#struct_0_15224_x2020_x943391839}

[LoopBack0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP(spoofing)]{lang="EN-US"}

[Description: LoopBack0 Interface]{lang="EN-US"}

[Maximum Transmit Unit: 1536]{lang="EN-US"}

[Internet protocol processing : disabled]{lang="EN-US"}

[Physical: Loopback]{lang="EN-US"}

[Last clearing of counters:  Never]{lang="EN-US"}

[]{#struct_0_15224_x2020_1445627275}[[表1-3 ]{lang="EN-US"}[display interface loopback]{lang="EN-US"}]{#_Ref137377196}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2029132002}[[字段]{style="font-family:黑体"}]{#struct_0_15224_x2020_x457835386}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1991529458}

[[Current state]{lang="EN-US"}]{#struct_0_15224_x2020_443052161}

[[接口当前的物理层状态]{style="font-family:宋体"}]{#struct_0_15224_x2020_602311583}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_15224_x2020_x903038938}[：表示接口能收发报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_15224_x2020_x943326303}[：表示接口被手工关闭了，即在接口下配置了]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_15224_x2020_x1682549429}

[[链路层协议状态：]{style="font-family:宋体"}[UP(spoofing)]{lang="EN-US"}]{#struct_0_15224_x2020_161206408}[，表示接口的链路层协议状态为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在，而是按需建立的]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_15224_x2020_x1361455224}

[[接口的描述字符串]{style="font-family:宋体"}]{#struct_0_15224_x2020_x1300539801}

[[Bandwidth]{lang="EN-US"}]{#struct_0_15224_x2020_x943260767}

[[接口的期望带宽，只有当取值不为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_15224_x2020_x1732833114}[时，才显示该字段]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_15224_x2020_x1363529988}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_15224_x2020_x1568172731}

[[Internet protocol processing: disabled]{lang="EN-US"}]{#struct_0_15224_x2020_x581329612}

[[表示不能处理三层报文（接口没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_15224_x2020_x2681750}[地址时，显示该信息）]{style="font-family:宋体"}

[[Internet Address is 1.1.1.1/32 Primary]{lang="EN-US"}]{#struct_0_15224_x2020_x943195231}

[[接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_15224_x2020_267563769}[地址（接口配置了主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时显示该信息）]{style="font-family:宋体"}

[[Physical: Loopback]{lang="EN-US"}]{#struct_0_15224_x2020_x1582207035}

[[接口的物理类型是]{style="font-family:宋体"}[Loopback]{lang="EN-US"}]{#struct_0_15224_x2020_x1317729537}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_15224_x2020_x415751221}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_15224_x2020_x943129695}[命令清除接口下的统计信息的时间（如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x596039113}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_15224_x2020_x1422849074}[秒钟的平均输入速率（只有接口支持统计功能时才显示该信息）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_15224_x2020_1866385669}[表示平均每秒输入的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_15224_x2020_1829608180}[表示平均每秒输入的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x943064159}[表示平均每秒输入的包数]{lang="EN-US" style="font-family:宋体"}

[[Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x145670663}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_15224_x2020_1135808914}[秒钟的平均输出速率（只有接口支持统计功能时才显示该信息）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x1925531414}[表示平均每秒输出的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x1933067914}[表示平均每秒输出的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_15224_x2020_x944047199}[表示平均每秒输出的包数]{lang="EN-US" style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_15224_x2020_1283246426}

[[接口输入的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）]{style="font-family:宋体"}]{#struct_0_15224_x2020_541548776}

[[Onput: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_15224_x2020_x985568954}

[[接口输出的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）]{style="font-family:宋体"}]{#struct_0_15224_x2020_x943981663}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x939162040}[显示]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface loopback brief]{lang="EN-US"}]{#struct_0_15224_x2020_x189215934}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[[Loop1                UP   UP(s)    \--              forLAN1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_15224_x2020_x366441652}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_1081672175}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface loopback brief down]{lang="EN-US"}]{#struct_0_15224_x2020_x723874317}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Loop1                ADM  Administratively]{lang="EN-US"}

[]{#struct_0_15224_x2020_x1183043728}[[表1-4 ]{lang="EN-US"}[display interface loopback brief]{lang="EN-US"}]{#_Ref328495828}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1729430131}[[字段]{style="font-family:黑体"}]{#struct_0_15224_x2020_x2084757016}

[[描述]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1636641168}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_15224_x2020_622626569}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_1375647825}[接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_15224_x2020_117210058}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_15224_x2020_x16861045}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_15224_x2020_563374904}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_15224_x2020_x970776183}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_15224_x2020_622692105}[属性值中带有]{style="font-family:宋体"}[(s)]{lang="EN-US"}[，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_15224_x2020_x1732080736}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_15224_x2020_2130356633}

[[Link]{lang="EN-US"}]{#struct_0_15224_x2020_x2058346814}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_15224_x2020_x324008430}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_15224_x2020_476161357}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_15224_x2020_622757641}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_15224_x2020_x1315951521}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_15224_x2020_12861448}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_15224_x2020_x1093649886}

[[接口数据链路层协议状态，取值为]{style="font-family:宋体"}[UP(s)]{lang="EN-US"}]{#struct_0_15224_x2020_705395144}

[[Main IP]{lang="EN-US"}]{#struct_0_15224_x2020_622823177}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_15224_x2020_59804343}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_15224_x2020_1602173345}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_15224_x2020_x703025357}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_15224_x2020_x2097268863}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_15224_x2020_622888713}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时，表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_20226763}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_595409550}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_x917779194}

::: {#2078424724 .myid}
[]{#_Toc404783911}[]{#struct_0_15224_x2020_x2080242938}[]{#_Toc215479536}[]{#_Toc207017824}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- display interface null**

------------------------------------------------------------------------

[**[display interface null]{lang="EN-US"}**]{#struct_0_15224_x2020_x1960634182}[命令用来显示]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x264813551}

[**[display interface ]{lang="EN-US"}**[\[ **null** \[ **0** \] \] \[ **brief** \[ **description** \] \]]{lang="EN-US"}]{#struct_0_15224_x2020_1698463636}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x739640742}

[[任意视图]{style="font-family:宋体"}]{#struct_0_15224_x2020_622954249}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1601240771}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1392911406}

[[network-operator]{lang="EN-US"}]{#struct_0_15224_x2020_x272309525}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x1474369363}

[[mdc-operator]{lang="EN-US"}]{#struct_0_15224_x2020_1241734794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1218416382}

[**[0]{lang="EN-US"}**]{#struct_0_15224_x2020_x1169177153}[：]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_15224_x2020_623019785}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_15224_x2020_x810903193}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x299272902}

[[查看]{style="font-family:宋体"}[Null]{lang="EN-US"}]{#struct_0_15224_x2020_x917881779}[接口的相关信息时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_15224_x2020_728784515}**[null]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[因为设备只支持一个]{style="font-family:宋体"}]{#struct_0_15224_x2020_1862444542}[Null]{lang="EN-US"}[接口]{style="font-family:宋体"}[Null0]{lang="EN-US"}[，所以，只要指定]{style="font-family:宋体"}**[null]{lang="EN-US"}**[参数，不管是否指定]{style="font-family:宋体"}**[0]{lang="EN-US"}**[参数，显示的都是]{style="font-family:宋体"}[Null0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1031264848}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x489336106}[显示指定接口]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[的相关信息。（支持统计功能的]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的显示信息）]{style="font-family:宋体"}

[[\<Sysname\> display interface null 0]{lang="EN-US"}]{#struct_0_15224_x2020_622036745}

[NULL0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP(spoofing)]{lang="EN-US"}

[Description: NULL0 Interface]{lang="EN-US"}

[Bandwidth: 1000000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Physical: NULL DEV]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x176578272}[显示指定接口]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[的相关信息。（不支持统计功能的]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的显示信息）]{style="font-family:宋体"}

[[\<Sysname\> display interface null 0]{lang="EN-US"}]{#struct_0_15224_x2020_520379787}

[NULL0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP(spoofing)]{lang="EN-US"}

[Description:  NULL0 Interface]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Physical: NULL DEV]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x1587318435}[显示]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface null 0 brief]{lang="EN-US"}]{#struct_0_15224_x2020_622102281}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[[NULL0                UP   UP(s)    \--              ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_15224_x2020_x551878766}

[**[display interface null]{lang="EN-US"}**]{#struct_0_15224_x2020_952656371}[命令显示信息描述请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-3]{lang="EN-US"}](?-2004230743#_Ref137377196)[和]{style="font-family:
宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?-2004230743#_Ref328495828)[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1722437836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface null]{lang="EN-US"}**]{#struct_0_15224_x2020_x562423765}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface null]{lang="EN-US"}**]{#struct_0_15224_x2020_622561034}
:::

::: {#-1011556988 .myid}
[]{#_Toc32638018}[]{#_Toc31422553}[]{#_Toc32638014}[]{#_Toc31422549}[]{#_Toc404783912}[]{#struct_0_15224_x2020_x1608248015}[]{#_Toc215479539}[]{#_Toc207017825}[]{#_Toc43285284}[]{#_Toc41205434}[]{#_Toc32638023}[]{#_Toc31422558}[]{#_Toc317670450}[]{#_Toc220037885}[]{#_Toc220037886}[]{#_Toc220037887}[]{#_Toc220037888}[]{#_Toc220037889}[]{#_Toc220037890}[]{#_Toc220037891}[]{#_Hlt20219940}[]{#_Toc220037892}[]{#_Toc220037893}[]{#_Toc220037894}[]{#_Toc220037895}[]{#_Toc220037896}[]{#_Toc220037897}[]{#_Toc220037902}[]{#_Toc220037909}[]{#_Toc220037912}[]{#_Toc220037918}[]{#_Toc220037919}[]{#_Toc220037989}[]{#_Toc156191449}[]{#_Toc156191450}[]{#_Toc156191451}[]{#_Toc156191452}[]{#_Toc156191453}[]{#_Toc156191454}[]{#_Toc156191455}[]{#_Toc156191456}[]{#_Toc156191457}[]{#_Toc156191458}[]{#_Toc156191459}[]{#_Toc156191460}[]{#_Toc156191461}[]{#_Toc156191468}[]{#_Toc156191477}[]{#_Toc156191479}[]{#_Toc156191480}[]{#_Toc156191538}[]{#_Toc156191540}[]{#_Toc156191541}[]{#_Toc156191542}[]{#_Toc156191543}[]{#_Toc156191544}[]{#_Toc156191545}[]{#_Toc156191546}[]{#_Toc156191547}[]{#_Toc156191548}[]{#_Toc156191549}[]{#_Toc156191550}[]{#_Toc156191551}[]{#_Toc156191552}[]{#_Toc156191553}[]{#_Toc156191556}[]{#_Toc156191561}[]{#_Toc156191565}[]{#_Toc156191566}[]{#_Toc156191570}[]{#_Toc156191571}[]{#_Toc156191614}[]{#_Toc156191618}[]{#_Toc156191622}[]{#_Toc156191635}[]{#_Toc220037991}[]{#_Toc220037992}[]{#_Toc220037993}[]{#_Toc220037994}[]{#_Toc220037995}[]{#_Toc220037996}[]{#_Toc220037997}[]{#_Toc220037998}[]{#_Toc220037999}[]{#_Toc220038000}[]{#_Toc220038001}[]{#_Toc220038002}[]{#_Toc220038003}[]{#_Toc220038004}[]{#_Toc220038005}[]{#_Toc220038006}[]{#_Toc220038007}[]{#_Toc220038048}[]{#_Toc220038049}[]{#_Toc220038158}[]{#_Toc220038159}[]{#_Toc220038164}[]{#_Toc220038165}[]{#_Toc220038187}[]{#_Toc220038190}[]{#_Toc220038193}[]{#_Toc220038194}[]{#_Toc220038195}[]{#_Toc220038196}[]{#_Toc220038197}[]{#_Toc220038198}[]{#_Toc220038199}[]{#_Toc220038200}[]{#_Toc220038201}[]{#_Toc220038202}[]{#_Toc220038203}[]{#_Toc220038204}[]{#_Toc220038205}[]{#_Toc220038206}[]{#_Toc220038207}[]{#_Toc220038208}[]{#_Toc220038209}[]{#_Toc220038211}[]{#_Toc220038212}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- interface loopback**

------------------------------------------------------------------------

[**[interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_1484956702}[命令用来创建]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口，并进入]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[**[undo interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_1854431105}[命令用来删除指定的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_837005298}

[**[interface loopback]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_15224_x2020_1534474190}[]{#_Hlt24945530}*[interface-number]{lang="EN-US"}*

[**[undo interface loopback]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_15224_x2020_536166963}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1030558542}

[[设备上没有]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_x1899120308}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_622626570}

[[系统视图]{style="font-family:宋体"}]{#struct_0_15224_x2020_x580667320}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1215454470}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x1500398595}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x651498305}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1067870368}

[*[interface-number]{lang="EN-US"}*]{#struct_0_15224_x2020_846310701}[：]{style="font-family:宋体"}[]{#_Hlt24945619}[LoopBack]{lang="EN-US"}[接口的编号。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1293065648}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_x97929598}[接口创建后，物理层和链路层永远处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，除非手工关闭该接口。因此，使用]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口建立连接，能够避免连接受接口物理状态的影响，从而提高连接的可靠性。比如，将]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口作为建立]{style="font-family:宋体"}[FTP]{lang="EN-US"}[连接时的源接口，将]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的地址作为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议中的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_622692106}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x1732080737}[创建接口]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15224_x2020_564272692}

[\[Sysname\] interface loopback 1]{lang="EN-US"}

[\[Sysname-LoopBack1\]]{lang="EN-US"}[]{#_Toc215479541}[]{#_Toc207017827}[]{#_Toc43285285}[]{#_Toc41205435}[]{#_Toc32638024}[]{#_Toc31422559}
:::

::: {#917119076 .myid}
[]{#_Toc404783913}[]{#struct_0_15224_x2020_346519508}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- interface null**

------------------------------------------------------------------------

[**[interface null]{lang="EN-US"}**]{#struct_0_15224_x2020_382898730}[命令用来进入]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_316978588}

[**[interface null 0]{lang="EN-US"}**]{#struct_0_15224_x2020_x1443327380}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1462850645}

[[设备只支持一个]{style="font-family:宋体"}[NULL]{lang="EN-US"}]{#struct_0_15224_x2020_x163448902}[接口------]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[，用户不能创建也不能删除。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_622757642}

[[系统视图]{style="font-family:宋体"}]{#struct_0_15224_x2020_x1315951522}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1578945389}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x1916038728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_755647120}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1836935669}

[**[0]{lang="EN-US"}**]{#struct_0_15224_x2020_1872019079}[：]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1891572633}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x1252495661}[进入接口]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15224_x2020_622823178}

[\[Sysname\] interface null 0]{lang="EN-US"}

[\[Sysname-NULL0\]]{lang="EN-US"}[]{#_Toc215479543}[]{#_Toc213490054}[]{#_Toc207010309}[]{#_Toc207010042}[]{#_Toc139515326}[]{#_Toc257900561}[]{#_Toc139169437}[]{#_Toc139098114}[]{#_Toc139169436}[]{#_Toc217375476}[]{#_Toc218395059}[]{#_Toc220038215}[]{#_Toc220038216}[]{#_Toc220038218}[]{#_Toc220038219}[]{#_Toc220038220}[]{#_Toc220038221}[]{#_Toc220038222}[]{#_Toc220038223}[]{#_Toc220038224}[]{#_Toc220038225}[]{#_Toc220038226}[]{#_Toc220038227}[]{#_Toc220038228}[]{#_Toc220038230}
:::

::::: {#425213212 .myid}
[]{#_Toc404783914}[]{#struct_0_15224_x2020_59804348}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- reset counters interface loopback**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LoopBack接口、NULL接口和InLoopBack接口命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_15224_x2020_x1883489887}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_15224_x2020_1605467961}
:::

[ ]{lang="EN-US"}

[**[reset counters interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_382501172}[命令用来清除]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1765171209}

[**[reset counters interface]{lang="EN-US"}**[ \[ **loopback** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_15224_x2020_358030468}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1606008574}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15224_x2020_835558758}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_622888714}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_20226756}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x941832717}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_377170075}

[*[interface-number]{lang="EN-US"}*]{#struct_0_15224_x2020_1628384426}[：逻辑接口编号。如果不指定该参数，则清除所有]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1326408084}

[[如果要统计一定时间内接口的流量来判断接口和链路工作是否正常，可以使用该命令先清除接口原有的统计信息，然后让接口自动重新统计。]{style="font-family:宋体"}]{#struct_0_15224_x2020_x20457412}

[[只有创建]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_211338157}[接口后，才支持该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_1572176739}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_622954250}[清除接口]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface loopback 1]{lang="EN-US"}]{#struct_0_15224_x2020_x737411380}[]{#_Toc215479544}[]{#_Toc207017828}[]{#_Toc207011379}[]{#_Toc207010311}[]{#_Toc207010044}[]{#_Toc139515327}[]{#_Toc137103160}[]{#_Toc217375479}[]{#_Toc218395062}[]{#_Toc217375480}[]{#_Toc218395063}[]{#_Hlt13991793}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_264269311}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface loopback]{lang="EN-US"}**]{#struct_0_15224_x2020_x1679047942}
:::::

::::: {#-940204975 .myid}
[]{#_Toc404783915}[]{#struct_0_15224_x2020_x1769143552}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- reset counters interface null**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LoopBack接口、NULL接口和InLoopBack接口命令.files/image001.png){#图片 2 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_15224_x2020_1159138191}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_15224_x2020_184994243}
:::

[ ]{lang="EN-US"}

[**[reset counters interface null]{lang="EN-US"}**]{#struct_0_15224_x2020_x362194568}[命令用来清除]{style="font-family:
宋体"}[NULL]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1894649049}

[**[reset counters interface]{lang="EN-US"}**[ \[ **null** \[ **0** \] \]]{lang="EN-US"}]{#struct_0_15224_x2020_623019786}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x810903194}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15224_x2020_x298814150}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_643692816}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x613507817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_x1713551593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15224_x2020_571126740}

[**[0]{lang="EN-US"}**]{#struct_0_15224_x2020_x1442354947}[：]{style="font-family:宋体"}[NULL]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_635536156}

[[如果要统计一定时间内接口的流量来判断接口工作是否正常，可以使用该命令先清除接口原有的统计信息，然后让接口自动重新统计。]{style="font-family:宋体"}]{#struct_0_15224_x2020_622036746}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x176578269}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_520969610}[清除接口]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface null 0]{lang="EN-US"}]{#struct_0_15224_x2020_303103202}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1877281331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface null]{lang="EN-US"}**]{#struct_0_15224_x2020_1262143167}
:::::

::: {#1170655049 .myid}
[]{#_Toc404783916}[]{#struct_0_15224_x2020_659140992}

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_15224_x2020_940187854}[命令用来关闭]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_15224_x2020_1504307030}[命令用来开启]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15224_x2020_622102282}

[**[shutdown]{lang="EN-US"}**]{#struct_0_15224_x2020_x551878765}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_15224_x2020_x1875339294}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x118648690}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_1150711742}[接口处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1559384039}

[[LoopBack]{lang="EN-US"}]{#struct_0_15224_x2020_1806459855}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x1987822380}

[[network-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1900418566}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15224_x2020_1672857660}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15224_x2020_622561031}

[[执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_15224_x2020_x1608248010}[命令会导致使用该接口建立的链路中断，不能通信，请谨慎使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15224_x2020_x2050495707}

[[\# ]{lang="EN-US"}]{#struct_0_15224_x2020_x2037231459}[关闭接口]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15224_x2020_1954862826}

[\[Sysname\] interface loopback 1]{lang="EN-US"}

[\[Sysname-LoopBack1\] shutdown]{lang="EN-US"}
:::
