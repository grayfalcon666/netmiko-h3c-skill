::: {#1826316826 .myid}
[]{#_Toc404785045}[]{#struct_0_12275_x1692_x879053844}[]{#_Toc257905496}[]{#_Toc96758234}[]{#_Toc31795107}[]{#_Toc505401544}

**HDLC \-- HDLC配置命令 \-- link-protocol hdlc**

------------------------------------------------------------------------

[**[link-protocol]{lang="EN-US"}**[ **hdlc**]{lang="EN-US"}]{#struct_0_12275_x1692_x1741326798}[命令用来配置接口封装]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1399340518}

[**[link-protocol hdlc]{lang="EN-US"}**]{#struct_0_12275_x1692_2050447569}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x162666283}

[[接口封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_12275_x1692_x1762796240}[协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1358774954}

[[POS]{lang="EN-US"}]{#struct_0_12275_x1692_x1511566775}[接口视图]{style="font-family:宋体"}[/Serial]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x148228513}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_2016261507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1923122119}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x661250824}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1735860383}[为链路层协议，可承载]{style="font-family:宋体"}[IP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[等网络层协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x817884134}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x1449155186}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[封装]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_1358316199}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol hdlc]{lang="EN-US"}
:::

::: {#1474946988 .myid}
[]{#_Toc404785046}[]{#struct_0_12275_x1692_87124363}[]{#_Toc257905498}[]{#_Toc96758235}

**HDLC \-- HDLC配置命令 \-- timer-hold**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**]{#struct_0_12275_x1692_193126243}[命令用来配置接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期。]{style="font-family:宋体"}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_12275_x1692_1942814352}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x159092635}

[**[timer-hold]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_12275_x1692_600901744}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_12275_x1692_471032882}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1060072232}

[[接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_12275_x1692_2114665011}[报文的周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_676746936}

[[POS]{lang="EN-US"}]{#struct_0_12275_x1692_1358250663}[接口视图]{style="font-family:宋体"}[/Serial]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_97854805}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1333094553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1549091506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_183941232}

[*[seconds]{lang="EN-US"}*]{#struct_0_12275_x1692_x1926103601}[：接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_637508277}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_829292727}[协议使用轮询机制来确认链路状态是否正常。]{style="font-family:宋体"}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x2039748611}[时，链路层会周期性地向对端发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文（可以通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送周期），]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文中携带了本端发送序号和前一次收到的对端发送序号。当接口收到对端发来的、携带有本端前一次发送序号的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文后，接口下次发送的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文中的发送序号将加一，否则发送序号不变。如果接口在]{style="font-family:宋体"}*[retry]{lang="EN-US"}*[个（可以通过]{style="font-family:宋体"}**[timer-hold retry]{lang="EN-US"}**[命令修改该个数）]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内无法收到对端发来的、携带有本端前一次发送序号的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12275_x1692_2101561923}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果将]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_12275_x1692_1358185127}[报文的发送周期]{lang="EN-US" style="font-family:宋体"}[配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，则不发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1489904151}[keepalive]{lang="EN-US"}[报文的发送周期时，建议链路两端的设置保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果网络的延迟比较大，或拥塞程度较高，可以适当加大]{style="font-family:宋体"}]{#struct_0_12275_x1692_x754104374}[keepalive]{lang="EN-US"}[报文的发送间隔，以避免链路被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x278126698}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x779567721}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_x521713304}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-serial2/1/0\] timer-hold 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1632012540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_12275_x1692_1632012547}
:::

::: {#518520923 .myid}
[]{#_Toc404785047}[]{#struct_0_12275_x1692_x1244791212}[]{#_Toc394763468}

**HDLC \-- HDLC配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_12275_x1692_1632012546}[命令用来配置允许接口重传的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文个数。]{style="font-family:宋体"}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_12275_x1692_x1244856748}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x324302597}

[**[timer-hold]{lang="EN-US"}**[ **retry** *retry*]{lang="EN-US"}]{#struct_0_12275_x1692_x673125834}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_12275_x1692_x324302598}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x674108874}

[[允许接口重传的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_12275_x1692_x324302599}[报文个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x674043338}

[[POS]{lang="EN-US"}]{#struct_0_12275_x1692_x324302600}[接口视图]{style="font-family:宋体"}[/Serial]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_900393517}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x324302593}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x673387978}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x324302594}

[*[retry]{lang="EN-US"}*]{#struct_0_12275_x1692_x673322442}[：允许接口重传的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x324302595}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x673256906}[协议使用轮询机制来确认链路状态是否正常。]{style="font-family:宋体"}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x324302596}[时，链路层会周期性地向对端发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文（可以通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送周期），]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文中携带了本端发送序号和前一次收到的对端发送序号。当接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文后，如果在]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内收到对端发来的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[应答报文（该报文携带有本端前一次发送序号），接口下次发送的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文中的发送序号将加一，否则，每经过一个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期，接口将重发一次]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，该报文的发送序号不变。如果接口重发第]{style="font-family:宋体"}*[retry]{lang="EN-US"}*[个（可以通过]{style="font-family:宋体"}**[timer-hold retry]{lang="EN-US"}**[命令修改该个数）]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文后，在]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内仍然没有收到对端发来的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[应答报文，链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，如果网络的延迟比较大，或拥塞程度较高，可以适当加大]{style="font-family:宋体"}*[retry]{lang="EN-US"}*]{#struct_0_12275_x1692_x673191370}[值，以避免链路被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x324302589}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x674043339}[配置允许接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[重传的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文个数为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_x324302590}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] timer-hold retry 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1904768773}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_12275_x1692_1314259010}
:::

::: {#1742433432 .myid}
[]{#_Toc404785049}[]{#struct_0_12275_x1692_x1376058916}[]{#_Toc361745445}[]{#_Toc353540946}[]{#_Toc348875570}[]{#_Toc348875494}[]{#_Toc317782947}[]{#_Toc307818511}[]{#_Toc284169067}

**HDLC \-- HDLC链路捆绑配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_12275_x1692_x428130197}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_12275_x1692_x576355842}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1710596086}

[**[bandwidth]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12275_x1692_x1136420209}*[bandwidth-value]{lang="EN-US"}*

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_12275_x1692_x886853397}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x997142310}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_12275_x1692_x576421378}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_215518698}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x1778230123}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1075708558}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x575962626}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1236472805}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1400082809}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_12275_x1692_x793975480}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbi]{lang="EN-US"}[t/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x224295838}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_12275_x1692_x576028162}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x2088477504}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x193875921}[设置]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[1000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_x127302532}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] bandwidth 1000]{lang="EN-US"}
:::

::: {#414282972 .myid}
[]{#_Toc404785050}[]{#struct_0_12275_x1692_x576093698}[]{#_Toc361745446}[]{#_Toc353540940}[]{#_Toc348875564}[]{#_Toc348875488}

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle id**

------------------------------------------------------------------------

[**[bundle id]{lang="EN-US"}**]{#struct_0_12275_x1692_x221546962}[命令用来将当前接口加入指定的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[**[undo bundle id]{lang="EN-US"}**]{#struct_0_12275_x1692_x930867195}[命令用来将接口从]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑中退出。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x795179699}

[**[bundle id]{lang="EN-US"}**[ *bundle-id*]{lang="EN-US"}]{#struct_0_12275_x1692_x576159234}

[**[undo bundle id]{lang="EN-US"}**]{#struct_0_12275_x1692_1814358153}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_187345437}

[[接口不属于任何]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1060046572}[捆绑。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x633794701}

[[POS]{lang="EN-US"}]{#struct_0_12275_x1692_x575700482}[接口视图]{style="font-family:宋体"}[/Serial]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1500381865}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_135043241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x2095760554}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x575766018}

[*[bundle-id]{lang="NO-BOK"}*]{#struct_0_12275_x1692_x58278334}[：]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1752944757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口只能加入一个]{style="font-family:宋体"}]{#struct_0_12275_x1692_x553823872}[HDLC]{lang="EN-US"}[捆绑，如果需要加入其他]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑，必须先退出原来的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加入]{style="font-family:宋体"}]{#struct_0_12275_x1692_x371223238}[HDLC]{lang="EN-US"}[捆绑的接口封装的链路层协议必须为]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[。接口加入]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑之后不允许修改链路层协议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x576224771}[捆绑接口没有创建的情况下，也允许将接口加入]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1740297283}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_1415773448}[将]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[加入]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_x1332631817}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] bundle id 1]{lang="EN-US"}
:::

::: {#-1752419274 .myid}
[]{#_Toc404785051}[]{#struct_0_12275_x1692_x576290307}[]{#_Toc361745447}[]{#_Toc353540942}[]{#_Toc348875566}[]{#_Toc348875490}

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle load-balance**

------------------------------------------------------------------------

[**[bundle load-balance]{lang="EN-US"}**]{#struct_0_12275_x1692_x1376124452}[命令用来配置负载分担方式。]{style="font-family:宋体"}

[**[undo bundle load-balance]{lang="EN-US"}**]{#struct_0_12275_x1692_1629311365}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1699784863}

[**[bundle load-balance]{lang="EN-US"}**[ { **per-flow** \| **per-packet** }]{lang="EN-US"}]{#struct_0_12275_x1692_x576355843}

[**[undo bundle load-balance]{lang="EN-US"}**]{#struct_0_12275_x1692_x1710661622}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_16831286}

[[采用逐包负载分担。]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1623604514}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_542350533}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x576421379}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_215584234}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1827262890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1984310620}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x575962627}

[**[per-flow]{lang="EN-US"}**]{#struct_0_12275_x1692_x1236407269}[：逐流负载分担。]{style="font-family:宋体"}

[**[per-packet]{lang="EN-US"}**]{#struct_0_12275_x1692_1020845510}[：逐包负载分担。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1140839686}

[[负载分担方式分为逐流负载分担和逐包负载分担两种，原理如下：]{style="font-family:宋体"}]{#struct_0_12275_x1692_616324169}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[逐流负载分担：通过源]{style="font-family:宋体"}]{#struct_0_12275_x1692_x576028163}[IP]{lang="EN-US"}[地址和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址等将报文分成不同的流，同一条流的报文将在同一个选中成员接口上发送。目前支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文根据源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行分流，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文根据标签进行分流。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[逐包负载分担：以报文为单位，轮流从所有选中成员接口中选择接口发送报文。]{style="font-family:宋体"}]{#struct_0_12275_x1692_x2088411968}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1610576561}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x1216877131}[配置]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[采用逐流负载分担方式发送报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_x576093699}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] bundle load-balance per-flow]{lang="EN-US"}
:::

::: {#-1508956398 .myid}
[]{#_Toc404785052}[]{#struct_0_12275_x1692_x221612498}[]{#_Toc361745448}[]{#_Toc353540938}

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle max-active links**

------------------------------------------------------------------------

[**[bundle max-active links]{lang="EN-US"}**]{#struct_0_12275_x1692_209054423}[命令用来配置最多选中成员接口数目。]{style="font-family:宋体"}

[**[undo bundle max-active links]{lang="EN-US"}**]{#struct_0_12275_x1692_949231288}[命令用来取消限制。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x576159235}

[**[bundle max-active links ]{lang="NO-BOK"}**]{#struct_0_12275_x1692_1814292617}*[number]{lang="NO-BOK"}*

[**[undo bundle max-active links]{lang="NO-BOK"}**]{#struct_0_12275_x1692_1032657968}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1945351938}

[[以设备支持的最多选中成员接口数目为准。不同设备支持的最多选中成员接口数目不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_12275_x1692_x649021289}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x575700483}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1500447401}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_2095022390}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1508860655}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x575766019}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x58212798}

[*[number]{lang="NO-BOK"}*]{#struct_0_12275_x1692_x2106482129}[：最多选中成员接口数目，取值范围为]{style="font-family:宋体"}[1]{lang="DE"}[～]{style="font-family:宋体"}[16]{lang="DE"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1269741322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置的值不能小于]{lang="EN-US" style="font-family:宋体"}**[bundle min-active links]{lang="EN-US"}**]{#struct_0_12275_x1692_1414318088}[命令配置的值。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令一般需要和]{style="font-family:宋体"}]{#struct_0_12275_x1692_1346089535}**[bundle member-priority]{lang="EN-US"}**[命令配合使用，以保证两台设备相互连接的接口能够同时处于选中状态（只有两端接口同时处于选中状态，报文才能发送成功），避免出现一端接口处于选中状态，而另一端接口没有处于选中状态的情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1217224010}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_238082002}[配置最多选中成员接口数目为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_1648781803}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] bundle max-active links 8]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1346023999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bundle member-priority]{lang="EN-US"}**]{#struct_0_12275_x1692_1712377650}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bundle min-active links]{lang="EN-US"}**]{#struct_0_12275_x1692_x1577354779}
:::

::: {#620266864 .myid}
[]{#_Toc404785053}[]{#struct_0_12275_x1692_402674083}[]{#_Toc361745449}[]{#_Toc353540941}[]{#_Toc348875565}[]{#_Toc348875489}

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle member-priority**

------------------------------------------------------------------------

[**[bundle member-priority]{lang="EN-US"}**]{#struct_0_12275_x1692_x1565581505}[命令用来配置接口的捆绑优先级。]{style="font-family:宋体"}

[**[undo bundle member-priority]{lang="EN-US"}**]{#struct_0_12275_x1692_1345958463}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_979953545}

[**[bundle member-priority ]{lang="NO-BOK"}**]{#struct_0_12275_x1692_x612379651}*[priority]{lang="NO-BOK"}*

[**[undo bundle member-priority]{lang="NO-BOK"}**]{#struct_0_12275_x1692_x2145910125}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1345892927}

[[接口的捆绑优先级为]{style="font-family:宋体"}[32768]{lang="EN-US"}]{#struct_0_12275_x1692_x900900454}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1024200252}

[[POS]{lang="EN-US"}]{#struct_0_12275_x1692_1032751051}[接口视图]{style="font-family:宋体"}[/Serial]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1995530204}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1346351679}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1076643693}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_294108867}

[*[priority]{lang="EN-US"}*]{#struct_0_12275_x1692_x46080972}[：接口的捆绑优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[值越大，接口的捆绑优先级越低。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1346286143}

[]{#_Toc353540939}[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x1826125702}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/2/0]{lang="EN-US"}[的捆绑优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_2045387858}

[\[Sysname\] interface pos 2/2/0]{lang="EN-US"}

[\[Sysname-Pos2/2/0\] bundle member-priority 1]{lang="EN-US"}
:::

::: {#1028231939 .myid}
[]{#_Toc404785054}[]{#struct_0_12275_x1692_x2096173146}[]{#_Toc361745450}

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle min-active bandwidth**

------------------------------------------------------------------------

[**[bundle min-active bandwidth]{lang="NO-BOK"}**]{#struct_0_12275_x1692_1346220607}[命令]{style="font-family:
宋体"}[用来配置]{style="font-family:宋体"}[最小激活带宽。]{style="font-family:
宋体"}

[**[undo bundle min-active bandwidth]{lang="NO-BOK"}**]{#struct_0_12275_x1692_483083288}[命令]{style="font-family:宋体"}[用来]{style="font-family:宋体"}[取消限制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_606070750}

[**[bundle min-active bandwidth ]{lang="NO-BOK"}**]{#struct_0_12275_x1692_2100716925}*[bandwidth]{lang="NO-BOK"}*

[**[undo bundle min-active bandwidth]{lang="NO-BOK"}**]{#struct_0_12275_x1692_1210712194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1346155071}

[[不进行限制。]{style="font-family:宋体"}]{#struct_0_12275_x1692_x253762071}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x64288395}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1084398899}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_640012982}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1346613823}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x629092617}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1692330410}

[*[bandwidth]{lang="EN-US"}*]{#struct_0_12275_x1692_x1905043250}[：最小激活带宽，取值范围为]{style="font-family:宋体"}[64]{lang="EN-US"}[～]{style="font-family:宋体"}[1342177280]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1346548287}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_87877651}[配置最小激活带宽为]{style="font-family:宋体"}[1000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_1594797954}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] bundle min-active bandwidth 1000]{lang="EN-US"}
:::

::: {#484018876 .myid}
[]{#_Toc404785055}[]{#struct_0_12275_x1692_x1720529695}[]{#_Toc361745451}[]{#_Toc353540937}

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle min-active links**

------------------------------------------------------------------------

[**[bundle min-active links]{lang="NO-BOK"}**]{#struct_0_12275_x1692_1346089534}[命令用来配置]{style="font-family:
宋体"}[最少选中成员接口数目]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo bundle min-active links]{lang="DE"}**]{#struct_0_12275_x1692_1217158474}[命令用来取消限制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1783736801}

[**[bundle min-active links ]{lang="NO-BOK"}**]{#struct_0_12275_x1692_2045272134}*[number]{lang="NO-BOK"}*

[**[undo bundle min-active links]{lang="NO-BOK"}**]{#struct_0_12275_x1692_1346023998}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1712312114}

[[不进行限制。]{style="font-family:宋体"}]{#struct_0_12275_x1692_1558060048}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1112483092}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1202366167}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1345958462}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_980019081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1556725292}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1690299723}

[*[number]{lang="NO-BOK"}*]{#struct_0_12275_x1692_x954722686}[：最少选中成员接口数目，取值范围为]{style="font-family:宋体"}[1]{lang="DE"}[～]{style="font-family:宋体"}[16]{lang="DE"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1345892926}

[[本命令配置的值不能大于]{style="font-family:宋体"}**[bundle max-active links]{lang="EN-US"}**]{#struct_0_12275_x1692_x900834918}[命令配置的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1412971439}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_723964837}[配置最少选中成员接口数目为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_1346351678}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] bundle min-active links 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1076578157}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bundle max-active links]{lang="EN-US"}**]{#struct_0_12275_x1692_995203367}
:::

::: {#1948332219 .myid}
[]{#_Toc404785056}[]{#struct_0_12275_x1692_773579981}[]{#_Toc361745452}[]{#_Toc353540947}[]{#_Toc348875571}[]{#_Toc348875495}

**HDLC \-- HDLC链路捆绑配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_12275_x1692_1346286142}[命令用来恢复默认配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1826191238}

[**[default]{lang="EN-US"}**]{#struct_0_12275_x1692_884892598}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_761921709}

[[HDLC]{lang="NO-BOK"}]{#struct_0_12275_x1692_948658176}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1346220606}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_483017752}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1353735704}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1669780660}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_12275_x1692_1346155070}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_12275_x1692_x253696535}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_316487462}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_1631657036}[将]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="NO-BOK"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_12275_x1692_1346613822}

[\[Sysname\] interface hdlc-bundle 1]{lang="DE"}

[\[Sysname-HDLC-bundle1\] default]{lang="DE"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785057}[]{#struct_0_12275_x1692_x629027081}[]{#_Toc361745453}[]{#_Toc353540948}[]{#_Toc348875572}[]{#_Toc348875496}[]{#_Toc317782948}[]{#_Toc307818512}

**HDLC \-- HDLC链路捆绑配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_12275_x1692_x1795191856}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_12275_x1692_2035260252}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x2129721259}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_12275_x1692_1346548286}

[**[undo description]{lang="EN-US"}**]{#struct_0_12275_x1692_87812115}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1996479771}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_12275_x1692_507068083}["，比如：]{style="font-family:宋体"}[HDLC-bundle1 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1638259514}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1346089533}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1217092938}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_212212720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1179824739}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1346023997}

[*[text]{lang="EN-US"}*]{#struct_0_12275_x1692_1711460146}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1453783908}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_552521490}[配置]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[HDLC-bundle interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_1345958461}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] description HDLC-bundle interface]{lang="EN-US"}
:::

::: {#-1084498885 .myid}
[]{#_Toc404785058}[]{#struct_0_12275_x1692_980084617}[]{#_Toc361745454}[]{#_Toc353540943}[]{#_Toc348875567}[]{#_Toc348875491}

**HDLC \-- HDLC链路捆绑配置命令 \-- display bundle hdlc-bundle**

------------------------------------------------------------------------

[**[display bundle hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_x849007691}[命令用来显示]{style="font-family:
宋体"}[HDLC]{lang="EN-US"}[捆绑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_428853594}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12275_x1692_x691623523}

[**[display bundle hdlc-bundle]{lang="EN-US"}**[ \[ *bundle-id* \]]{lang="EN-US"}]{#struct_0_12275_x1692_1345892925}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12275_x1692_x900769382}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display bundle hdlc-bundle]{lang="EN-US"}**[ \[ *bundle-id* \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_12275_x1692_482478848}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12275_x1692_1344586770}[模式：]{style="font-family:宋体"}

[**[display bundle hdlc-bundle]{lang="EN-US"}**[ \[ *bundle-id* \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_12275_x1692_1346351677}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1075988333}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1762140597}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1156737111}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1201665140}

[[network-operator]{lang="EN-US"}]{#struct_0_12275_x1692_1346286141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1826256774}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12275_x1692_147611057}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x763218709}

[*[bundle-id]{lang="DE"}*]{#struct_0_12275_x1692_1346220605}[：显示指定]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口的捆绑信息。如果不指定本参数，将显示所有]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口的捆绑信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_483214360}[：显示指定单板的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_x714509230}[：显示指定成员设备的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_2145754840}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_x2098920773}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_x583128515}[：显示指定单板的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_12275_x1692_254507564}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x542756531}

[[主用主控板显示信息中包括了所有成员接口的信息；备用主控板、接口板显示信息中只包括选中成员接口的信息，不包括非选中成员接口的信息。]{style="font-family:宋体"}]{#struct_0_12275_x1692_1346155069}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x254286360}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x962709953}[显示主用主控板]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的捆绑信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display bundle hdlc-bundle 1]{lang="NO-BOK"}]{#struct_0_12275_x1692_1346613821}

[Bundle: HDLC-bundle1]{lang="NO-BOK"}

[  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps]{lang="NO-BOK"}

[  Selected members: 2, Total bandwidth: 1244160 kbps]{lang="NO-BOK"}

[  Member              State               Bandwidth(kbps)     Priority]{lang="NO-BOK"}

[  Pos2/2/1            Selected            622080              1]{lang="NO-BOK"}

[  Pos2/2/2            Selected            622080              2]{lang="NO-BOK"}

[  Pos2/2/4            Ready               622080              32768]{lang="NO-BOK"}

[  Pos2/2/3            Ready               622080              65535]{lang="NO-BOK"}

[  Pos2/2/5            Ready               155520              32768]{lang="NO-BOK"}

[  Pos2/2/6            Ready               155520              32768]{lang="NO-BOK"}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x628961545}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[CPU 0]{lang="EN-US"}[的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的捆绑信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display bundle hdlc-bundle 1 slot 1 cpu 0]{lang="NO-BOK"}]{#struct_0_12275_x1692_166491731}

[Bundle: HDLC-bundle1, slot 1 cpu 0]{lang="NO-BOK"}

[  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps]{lang="NO-BOK"}

[  Selected members: 2, Total bandwidth: 1244160 kbps]{lang="NO-BOK"}

[  Member              State               Bandwidth(kbps)     Priority]{lang="NO-BOK"}

[  Pos2/2/1            Selected            622080              1]{lang="NO-BOK"}

[  Pos2/2/2            Selected            622080              2]{lang="NO-BOK"}

[[\# ]{lang="NO-BOK"}]{#struct_0_12275_x1692_1346548285}[显示成员设备]{style="font-family:宋体"}[1]{lang="NO-BOK"}[上]{style="font-family:宋体"}[CPU 0]{lang="NO-BOK"}[的]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="NO-BOK"}[的捆绑信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="NO-BOK"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display bundle hdlc-bundle 1 slot 1 cpu 0]{lang="NO-BOK"}]{#struct_0_12275_x1692_87746579}

[Bundle: HDLC-bundle1, slot 1 cpu 0]{lang="NO-BOK"}

[  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps]{lang="NO-BOK"}

[  Selected members: 2, Total bandwidth: 1244160 kbps]{lang="NO-BOK"}

[  Member              State               Bandwidth(kbps)     Priority]{lang="NO-BOK"}

[  Pos2/2/1            Selected            622080              1]{lang="NO-BOK"}

[  Pos2/2/2            Selected            622080              2]{lang="NO-BOK"}

[[\# ]{lang="NO-BOK"}]{#struct_0_12275_x1692_1593797912}[显示成员设备]{style="font-family:宋体"}[1]{lang="NO-BOK"}[上]{style="font-family:宋体"}[1]{lang="NO-BOK"}[号单板上]{style="font-family:宋体"}[CPU 0]{lang="NO-BOK"}[的]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="NO-BOK"}[的捆绑信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="NO-BOK"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display bundle hdlc-bundle 1 chassis 1 slot 1 cpu 0]{lang="NO-BOK"}]{#struct_0_12275_x1692_1346089532}

[Bundle: HDLC-bundle1, chassis 1, slot 1 cpu 0]{lang="NO-BOK"}

[  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps]{lang="NO-BOK"}

[  Selected members: 2, Total bandwidth: 1244160 kbps]{lang="NO-BOK"}

[  Member              State               Bandwidth(kbps)     Priority]{lang="NO-BOK"}

[  Pos2/2/1            Selected            622080              1]{lang="NO-BOK"}

[  Pos2/2/2            Selected            622080              2]{lang="NO-BOK"}

[[表1-1 ]{lang="EN-US"}[display bundle hdlc-bundle]{lang="EN-US"}]{#struct_0_12275_x1692_1217027402}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x63442249}[[字段]{style="font-family:黑体"}]{#struct_0_12275_x1692_x123438656}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12275_x1692_1346023996}

[[Bundle]{lang="NO-BOK"}]{#struct_0_12275_x1692_1711394610}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x1436231758}[捆绑接口的名称]{style="font-family:宋体"}

[[chassis]{lang="EN-US"}]{#struct_0_12275_x1692_1345958460}

[[显示信息接口板所在成员设备编号]{style="font-family:宋体"}]{#struct_0_12275_x1692_980150153}

[[slot]{lang="EN-US"}]{#struct_0_12275_x1692_362722825}

[[显示信息所在接口板槽位号]{style="font-family:宋体"}]{#struct_0_12275_x1692_1345892924}

[[cpu]{lang="NO-BOK"}]{#struct_0_12275_x1692_254442027}

[[显示信息所在]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12275_x1692_254114347}[的编号]{style="font-family:宋体"}

[[max-active links]{lang="EN-US"}]{#struct_0_12275_x1692_x900703846}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1346351676}[捆绑接口上配置的最多选中成员接口数目（如果没有配置则不显示此配置项）]{style="font-family:宋体"}

[[min-active links]{lang="EN-US"}]{#struct_0_12275_x1692_x1075922797}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_988778113}[捆绑接口上配置的最少选中成员接口数目（如果没有配置则不显示此配置项）]{style="font-family:宋体"}

[[min-active bandwidth]{lang="EN-US"}]{#struct_0_12275_x1692_1346286140}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x1826322310}[捆绑接口上配置的最小激活带宽（如果没有配置则不显示此配置项）]{style="font-family:宋体"}

[[Selected members]{lang="EN-US"}]{#struct_0_12275_x1692_x1751970428}

[[当前选中的成员接口数目]{style="font-family:宋体"}]{#struct_0_12275_x1692_1346220604}

[[Total bandwidth]{lang="EN-US"}]{#struct_0_12275_x1692_483148824}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1346155068}[捆绑接口下所有选中成员接口带宽之和]{style="font-family:宋体"}

[[Member]{lang="EN-US"}]{#struct_0_12275_x1692_x254220824}

[[成员接口名称]{style="font-family:宋体"}]{#struct_0_12275_x1692_x938085915}

[[State]{lang="EN-US"}]{#struct_0_12275_x1692_1346613820}

[[成员接口状态，各含义如下：]{style="font-family:宋体"}]{#struct_0_12275_x1692_x628896009}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Selected]{lang="EN-US"}]{#struct_0_12275_x1692_1346548284}[：选中状态（接口板只显示该状态的成员接口信息）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_12275_x1692_87681043}[：就绪状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Negotiated]{lang="EN-US"}]{#struct_0_12275_x1692_x425846973}[：协商状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initial]{lang="EN-US"}]{#struct_0_12275_x1692_1346089531}[：初始状态]{lang="EN-US" style="font-family:宋体"}

[[Bandwidth(kbps)]{lang="EN-US"}]{#struct_0_12275_x1692_1216961866}

[[成员接口的带宽，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_12275_x1692_1346023995}

[[Priority]{lang="EN-US"}]{#struct_0_12275_x1692_1711591218}

[[成员接口的捆绑优先级]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1431597083}

[ ]{lang="EN-US"}

::: {#-1080871426 .myid}
[]{#_Toc404785059}[]{#struct_0_12275_x1692_1345958459}[]{#_Toc361745455}[]{#_Toc353540945}[]{#_Toc348875569}[]{#_Toc348875493}

**HDLC \-- HDLC链路捆绑配置命令 \-- display interface hdlc-bundle**

------------------------------------------------------------------------

[**[display interface hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_979560332}[命令用来显示]{style="font-family:
宋体"}[HDLC]{lang="EN-US"}[捆绑接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1856825281}

[**[display interface]{lang="EN-US"}**[ \[ **hdlc-bundle** \[ *bundle-id* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_12275_x1692_1345892923}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x900638310}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12275_x1692_2059114107}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_2007909827}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_1361457041}

[[network-operator]{lang="EN-US"}]{#struct_0_12275_x1692_1346351675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1075857261}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12275_x1692_x769004263}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1431833911}

[*[bundle-id]{lang="DE"}*]{#struct_0_12275_x1692_1346286139}[：显示指定]{style="font-family:宋体"}[HDLC]{lang="DE"}[捆绑接口的相关信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_12275_x1692_x1825732493}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_12275_x1692_1699816141}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_12275_x1692_253852203}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x402833186}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_12275_x1692_1346220603}**[hdlc-bundle]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_483345432}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[bundle-id]{lang="EN-US"}*[参数，]{lang="EN-US" style="font-family:宋体"}[将显示所有]{style="font-family:宋体"}[HDLC]{lang="DE"}[捆绑接口的相关信息]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1268461102}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_634374115}[显示]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface hdlc-bundle 1]{lang="EN-US"}]{#struct_0_12275_x1692_1346155067}

[HDLC-bundle1]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: HDLC-bundle1 Interface]{lang="EN-US"}

[Bandwidth: 128kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Internet Address is 1.1.1.2/24 Primary]{lang="EN-US"}

[Link layer protocol: HDLC]{lang="EN-US"}

[Physical: HDLC-BUNDLE, baudrate: 128000 bps]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 32 packets, 1842 bytes, 0 drops]{lang="EN-US"}

[Output: 27 packets, 1512 bytes, 0 drops]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x253631000}[显示]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="DE"}[的概要信息。]{style="font-family:
宋体"}

[[\<Sysname\> display interface hdlc-bundle 1 brief]{lang="EN-US"}]{#struct_0_12275_x1692_1346613819}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[HBDL1                UP   UP(s)    1.1.1.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x628437256}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface hdlc-bundle brief down]{lang="EN-US"}]{#struct_0_12275_x1692_1331858625}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[HBDL2                ADM  Administratively]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display interface hdlc-bundle]{lang="EN-US"}]{#struct_0_12275_x1692_1346548283}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x29343159}[[字段]{style="font-family:黑体"}]{#struct_0_12275_x1692_88139795}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12275_x1692_1771054709}

[[Current state]{lang="EN-US"}]{#struct_0_12275_x1692_1346089530}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1216896330}[捆绑接口的物理状态和管理状态，状态可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN ( Administratively )]{lang="EN-US"}]{#struct_0_12275_x1692_988605780}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_12275_x1692_1346023994}[：表示该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12275_x1692_1711525682}[：表示该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_12275_x1692_114451034}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1345958458}[捆绑接口的链路层协议状态，状态可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_12275_x1692_979625868}[：表示数据链路层协议状态为关闭，一般是没有选中成员接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12275_x1692_x40054362}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_12275_x1692_1345892922}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x900572774}[捆绑接口的描述信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_12275_x1692_1346351674}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x1075791725}[捆绑接口的期望带宽]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_12275_x1692_x161269090}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1346286138}[捆绑接口的最大传输单元]{style="font-family:宋体"}

[[Hold timer]{lang="EN-US"}]{#struct_0_12275_x1692_x1825798029}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_12275_x1692_519297010}[报文的时间间隔]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1346220602}[捆绑接口不发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，此字段无意义）]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_12275_x1692_64522493}

[[允许接口重传的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_12275_x1692_64522499}[报文个数]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x315651842}[捆绑接口不发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，此字段无意义）]{style="font-family:宋体"}

[[Internet Address is 1.1.1.2/24 Primary]{lang="EN-US"}]{#struct_0_12275_x1692_483279896}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1346155066}[捆绑接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果接口尚未配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，本字段将变为"]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}["]{style="font-family:宋体"}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_12275_x1692_x253565464}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1103473509}[捆绑接口封装的链路层协议]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_12275_x1692_1346613818}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x628371720}[捆绑接口的物理类型]{style="font-family:宋体"}

[[baudrate]{lang="EN-US"}]{#struct_0_12275_x1692_x218073681}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1346548282}[捆绑接口的波特率]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}]{#struct_0_12275_x1692_88074259}

[[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}]{#struct_0_12275_x1692_x1382793820}

[[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}]{#struct_0_12275_x1692_x39644201}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x1688716050}[捆绑接口输出队列的类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[紧急发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1382859356}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_12275_x1692_1472044366}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[先入先出发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1382924892}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_12275_x1692_1337777146}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_12275_x1692_x1382990428}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_12275_x1692_x542478589}

[[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_12275_x1692_598652461}

[[当前接口最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_12275_x1692_x1382531676}[秒内输入（]{style="font-family:宋体"}[input]{lang="EN-US"}[）和输出（]{style="font-family:宋体"}[output]{lang="EN-US"}[）报文的平均速率]{style="font-family:宋体"}

[[Input: 32 packets, 1842 bytes, 0 drops]{lang="EN-US"}]{#struct_0_12275_x1692_x271409255}

[[接口输入的报文总数（分别以包和字节为单位进行了统计），输入报文中丢弃的报文数]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1382597212}

[[Output: 27 packets, 1512 bytes, 0 drops]{lang="EN-US"}]{#struct_0_12275_x1692_x671143257}

[[接口输出的报文总数（分别以包和字节为单位进行了统计），输出报文中丢弃的报文数]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1382662748}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_12275_x1692_x1122153955}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_12275_x1692_1562133253}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_12275_x1692_x1382728284}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1062430814}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_12275_x1692_x1382269532}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_12275_x1692_189578257}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_12275_x1692_x1382335068}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_12275_x1692_727793445}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1382793821}

[[Link]{lang="EN-US"}]{#struct_0_12275_x1692_1526439740}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1382859357}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12275_x1692_x1256838989}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_12275_x1692_x1682225301}[：表示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_12275_x1692_x1382924893}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_12275_x1692_x228306795}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12275_x1692_1023605352}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_12275_x1692_2137404837}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_12275_x1692_1057699509}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_12275_x1692_x1382531677}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12275_x1692_1294674686}[地址（]{style="font-family:宋体"}[\--]{lang="EN-US"}[表示没有为该接口配置主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_12275_x1692_x1382597213}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_12275_x1692_894940684}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_12275_x1692_x1382662749}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_12275_x1692_1606729400}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x611173125}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_12275_x1692_x1382728285}

::: {#-498282059 .myid}
[]{#_Toc404785060}[]{#struct_0_12275_x1692_1666452541}[]{#_Toc361745456}[]{#_Toc353540944}[]{#_Toc348875568}[]{#_Toc348875492}

**HDLC \-- HDLC链路捆绑配置命令 \-- interface hdlc-bundle**

------------------------------------------------------------------------

[**[interface hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_x1039451015}[命令用来创建]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口并进入]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口视图。如果该]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口已经存在，则直接进入该]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口视图。]{style="font-family:宋体"}

[**[undo interface hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_x1297861466}[命令用来删除]{style="font-family:
宋体"}[HDLC]{lang="EN-US"}[捆绑接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1528149052}

[**[interface hdlc-bundle ]{lang="EN-US"}***[bundle-id]{lang="EN-US"}*]{#struct_0_12275_x1692_x1382269533}

[**[undo interface hdlc-bundle ]{lang="EN-US"}***[bundle-id]{lang="EN-US"}*]{#struct_0_12275_x1692_x1376505684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1230634287}

[[不存在]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1922712181}[捆绑接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1065870163}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12275_x1692_x363542948}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382335069}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x2001089910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x506077727}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1443279280}

[*[bundle-id]{lang="DE"}*]{#struct_0_12275_x1692_x1139230087}[：]{style="font-family:宋体"}[HDLC]{lang="DE"}[捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382793822}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x1202443615}[创建]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[并进入]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_12275_x1692_x821106042}

[\[Sysname\] interface hdlc-bundle 1]{lang="DE"}

[\[Sysname-HDLC-bundle1\]]{lang="DE"}
:::

::: {#988247972 .myid}
[]{#_Toc404785061}[]{#struct_0_12275_x1692_x711256165}[]{#_Toc361745457}[]{#_Toc353540952}

**HDLC \-- HDLC链路捆绑配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_12275_x1692_x1382859358}[命令用来配置]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_12275_x1692_665475312}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1244157771}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_12275_x1692_685387960}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_12275_x1692_x256886575}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382924894}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_531208092}[捆绑接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1462629411}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_193471308}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x267679411}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1382990430}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x186313765}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x942026764}

[*[size]{lang="EN-US"}*]{#struct_0_12275_x1692_x2084678458}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x317310864}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_12275_x1692_x778907070}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_12275_x1692_x1382531678}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_178929439}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x357479912}[配置]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="NO-BOK"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_x1755176251}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] mtu 1430]{lang="EN-US"}
:::

::: {#2052875588 .myid}
[]{#_Toc404785062}[]{#struct_0_12275_x1692_x811829332}[]{#_Toc361745458}[]{#_Toc353540949}[]{#_Toc348875573}[]{#_Toc348875497}[]{#_Toc317782953}[]{#_Toc307818519}

**HDLC \-- HDLC链路捆绑配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_12275_x1692_x1382597214}[命令用来清除]{style="font-family:
宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1833942671}

[**[reset counters interface ]{lang="EN-US"}**[\[ **hdlc-bundle** \[ *bundle-id* \] \]]{lang="EN-US"}]{#struct_0_12275_x1692_x1841023791}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_464230434}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12275_x1692_x878289853}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382662750}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1478318779}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_287655523}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1186039415}

[*[bundle-id]{lang="EN-US"}*]{#struct_0_12275_x1692_1442858804}[：]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382728286}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_12275_x1692_2069737068}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_x1586530449}[和]{lang="EN-US" style="font-family:宋体"}*[bundle-id]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_x1865808916}[而不指定]{lang="EN-US" style="font-family:宋体"}*[bundle-id]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_x976431586}[和]{lang="EN-US" style="font-family:宋体"}*[bundle-id]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382269534}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x973221157}[清除]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[HDLC-bundle1]{lang="EN-US"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface hdlc-bundle1]{lang="EN-US"}]{#struct_0_12275_x1692_480677181}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1945207782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface hdlc-bundle]{lang="EN-US"}**]{#struct_0_12275_x1692_x1456145143}
:::

::: {#-780779607 .myid}
[]{#_Toc404785063}[]{#struct_0_12275_x1692_x1382335070}[]{#_Toc361745459}[]{#_Toc353540953}

**HDLC \-- HDLC链路捆绑配置命令 \-- service**

------------------------------------------------------------------------

[**[service]{lang="EN-US"}**]{#struct_0_12275_x1692_1083958269}[命令用来指定处理当前接口流量的业务板。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_12275_x1692_x1984114315}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1571966955}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12275_x1692_x1609383486}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[service slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12275_x1692_x1382793823}

[**[undo service slot]{lang="EN-US"}**]{#struct_0_12275_x1692_363640326}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12275_x1692_x335576647}[模式：]{style="font-family:宋体"}

[**[service ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12275_x1692_1425733954}

[**[undo service ]{lang="EN-US"}[chassis]{lang="EN-US"}**]{#struct_0_12275_x1692_223383893}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x2123191187}

[[没有指定处理当前接口流量的业务板。]{style="font-family:宋体"}]{#struct_0_12275_x1692_x1382859359}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x2063408043}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_1488690738}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_12275_x1692_2586413}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x920456515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1382924895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1034875849}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_53587215}[：指定单板所在的槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_27107388}[：指定设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12275_x1692_x836593184}[：指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382990431}

[[没有通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**]{#struct_0_12275_x1692_1379770176}[命令指定处理流量的业务板时，由收到数据流量的接口所在单板作为处理]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口流量的业务板。为了避免同一个单板处理过多的流量，可以指定处理]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口流量的业务板。]{style="font-family:宋体"}

[[需要注意的是，如果拔出了本命令所指定的业务板，即使]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x595839827}[捆绑接口]{style="font-family:宋体"}[UP]{lang="EN-US"}[，流量也无法正常处理；如果重新插入指定的业务板，则流量可以恢复在该板的正常处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x479916745}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x1717780862}[指定]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板为处理]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="NO-BOK"}[流量的业务板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x1382531679}[指定]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备为处理]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="NO-BOK"}[流量的业务处理设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_1745013380}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] service slot 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x825110734}[指定]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板为处理]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="NO-BOK"}[流量的业务板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_x198311724}

[\[Sysname\] interface hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] service chassis 1 slot 1]{lang="EN-US"}
:::

::: {#1170655049 .myid}
[]{#_Toc404785064}[]{#struct_0_12275_x1692_x1333939925}[]{#_Toc361745460}[]{#_Toc353540950}[]{#_Toc348875574}[]{#_Toc348875498}[]{#_Toc317782954}

**HDLC \-- HDLC链路捆绑配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_12275_x1692_x1382597215}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_12275_x1692_x267858730}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12275_x1692_494566641}

[**[shutdown]{lang="EN-US"}**]{#struct_0_12275_x1692_2065200120}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_12275_x1692_1883457287}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1382662751}

[[接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_12275_x1692_1250564576}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x705211907}

[[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x1009293990}[捆绑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12275_x1692_1336151444}

[[network-admin]{lang="EN-US"}]{#struct_0_12275_x1692_x1382728287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12275_x1692_503653127}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12275_x1692_x1072328732}

[[当打开]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_12275_x1692_x732435515}[捆绑接口时，会触发重新确定成员接口的状态；当关闭]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口时，所有选中成员口都会变成协商状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12275_x1692_909941644}

[[\# ]{lang="EN-US"}]{#struct_0_12275_x1692_x1382269535}[关闭]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口]{style="font-family:宋体"}[HDLC-bundle1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12275_x1692_1755662198}

[\[Sysname\] hdlc-bundle 1]{lang="EN-US"}

[\[Sysname-HDLC-bundle1\] shutdown]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
