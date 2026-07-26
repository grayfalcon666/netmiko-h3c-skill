::: {#1742433432 .myid}
[]{#_Toc263067817}[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc274913945}[]{#_Toc274832278}[]{#_Toc274658211}[]{#_Toc284169067}[]{#_Toc404785066}[]{#struct_0_21171_18224_1608526455}[]{#_Toc327792615}

**WAN接口 \-- WAN接口公共命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_21171_18224_829885559}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_21171_18224_1437520136}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x565046153}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_21171_18224_206365914}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_21171_18224_x316270764}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_398250485}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_21171_18224_x933346882}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x885196540}

[[串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x858706535}[串口子接口视图]{style="font-family:宋体"}[/AM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FCM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ISDN BRI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/E1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/T1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_176502541}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_805870291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_2381152}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_206169306}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_21171_18224_x1029986976}[：]{style="font-family:宋体"}[表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_2113140131}

[[接口的期望带宽会影响链路开销值，]{style="font-family:宋体"}]{#struct_0_21171_18224_x746719168}[具体介绍请参见"三层技术]{style="font-size:10.0pt;
font-family:宋体;color:black"}[-IP]{lang="EN-US" style="font-size:10.0pt;color:black"}[路由配置指导"中的"]{style="font-size:10.0pt;
font-family:宋体;color:black"}[OSPF]{lang="EN-US" style="font-size:
10.0pt;color:black"}["、]{style="font-size:10.0pt;font-family:宋体;
color:black"}["]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["]{style="font-family:宋体"}[和"]{style="font-size:10.0pt;font-family:宋体;
color:black"}[IS-IS]{lang="EN-US" style="font-size:10.0pt;color:black"}["]{style="font-size:10.0pt;font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_178203365}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1482292517}[设置串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1486025820}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] bandwidth 50]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404785067}[]{#struct_0_21171_18224_1752481403}[]{#_Toc329007815}[]{#_Toc309912009}

**WAN接口 \-- WAN接口公共命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_21171_18224_206234842}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_2037621202}

[**[default]{lang="EN-US"}**]{#struct_0_21171_18224_x1051880383}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x931013145}

[[串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_1938314822}[串口子接口视图]{style="font-family:宋体"}[/AM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FCM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ISDN BRI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/E1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/T1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/CE3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/CT3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1369195220}[接口视图]{style="font-family:宋体"}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1560779442}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x273210583}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x755498539}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_206562522}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1061523090}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1016024829}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_21171_18224_x1833451740}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_2072349352}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x193589653}[将串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1434586264}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785068}[]{#struct_0_21171_18224_x842716356}

**WAN接口 \-- WAN接口公共命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_21171_18224_206628058}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_21171_18224_x1801173231}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_441970466}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_21171_18224_303612661}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_21171_18224_1256268613}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1941779926}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_21171_18224_1600408293}["，比如：]{style="font-family:宋体"}[Serial2/1/0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x999700410}

[[串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_724182601}[串口子接口视图]{style="font-family:宋体"}[/AM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FCM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ISDN BRI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/E1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/T1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/CE3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/CT3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_206431450}[接口视图]{style="font-family:宋体"}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_276109588}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2004251047}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1297500939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x347514871}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x677953850}

[*[text]{lang="EN-US"}*]{#struct_0_21171_18224_1040545657}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1862933153}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1053153043}[配置串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[router-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_206496986}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] description router-interface]{lang="EN-US"}
:::

::: {#1170655049 .myid}
[]{#_Toc404785069}[]{#struct_0_21171_18224_x29682241}

**WAN接口 \-- WAN接口公共命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_21171_18224_x718586510}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_21171_18224_x18957390}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_436588592}

[**[shutdown]{lang="EN-US"}**]{#struct_0_21171_18224_740656230}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_21171_18224_1531781259}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1605656551}

[[接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_206824666}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1956379995}

[[串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1059246180}[串口子接口视图]{style="font-family:宋体"}[/AM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FCM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ISDN BRI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/E1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/T1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/CE3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/CT3]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1579758464}[接口视图]{style="font-family:宋体"}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_483364807}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1920817739}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1229315265}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1998837296}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1237070777}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_206890202}[关闭串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1168650038}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] shutdown]{lang="EN-US"}
:::

::: {#1474946988 .myid}
[]{#_Toc404785070}[]{#struct_0_21171_18224_x215264377}

**WAN接口 \-- WAN接口公共命令 \-- timer-hold**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**]{#struct_0_21171_18224_344088286}[命令用来配置]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_21171_18224_2031860091}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1247152027}

[**[timer-hold]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_21171_18224_x839296385}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_21171_18224_61405363}

[[【缺省情况】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_206300379}

[[Keepalive]{lang="EN-US"}]{#struct_0_21171_18224_x1612226858}[报文的]{style="font-family:宋体"}[发送周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1608591991}

[[串口视图]{style="font-family:宋体"}[/AM]{lang="EN-US"}]{#struct_0_21171_18224_x1582458904}[接口视图]{style="font-family:宋体"}[/FCM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ISDN BRI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/E1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/T1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1694036060}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_290210280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1613966802}

[[【参数】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1028386099}

[*[seconds]{lang="EN-US"}*]{#struct_0_21171_18224_x605992250}[：]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_206365915}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_21171_18224_x1612226859}[、]{style="font-family:宋体"}[FR]{lang="EN-US"}[或]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[时，链路层会定期（可通过本命令修改）向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，从而上报链路层]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在速率非常低的链路上，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}]{#struct_0_21171_18224_x1259487090}[报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的收发。而接口在若干个（可通过]{style="font-family:宋体"}**[timer-hold ]{lang="EN-US"}[retry]{lang="EN-US"}**[命令修改）]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期后仍未收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，就认为链路发生故障，从而拆除链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1309946614}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1612226853}[在串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x110036402}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] timer-hold 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1612226856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_21171_18224_662827211}
:::

::: {#518520923 .myid}
[]{#_Toc404785071}[]{#struct_0_21171_18224_x636092595}

**WAN接口 \-- WAN接口公共命令 \-- timer-hold retry**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_21171_18224_x1612226855}[命令用来配置在多少个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_21171_18224_1066111738}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1327941703}

[**[timer-hold]{lang="EN-US"}**[ **retry** *retry*]{lang="EN-US"}]{#struct_0_21171_18224_x1612226850}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_21171_18224_1825626625}

[[【缺省情况】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_967330406}

[[在]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_21171_18224_x1612226849}[个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1259552626}

[[串口视图]{style="font-family:宋体"}[/AM]{lang="EN-US"}]{#struct_0_21171_18224_x249935908}[接口视图]{style="font-family:宋体"}[/FCM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/ISDN BRI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/E1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/T1-F]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_528331746}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1110925014}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_149512656}

[[【参数】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x366788154}

[*[retry]{lang="EN-US"}*]{#struct_0_21171_18224_1110925015}[：在多少个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_149578192}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_21171_18224_2024465331}[、]{style="font-family:宋体"}[FR]{lang="EN-US"}[或]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[时，链路层会定期（可通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改）向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在速率非常低的链路上，]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}]{#struct_0_21171_18224_1110925012}[报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的收发。而接口在若干个（可通过本命令修改）]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期后仍未收到对端发来的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，就认为链路发生故障，从而拆除链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_149905872}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1110925013}[在串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上，配置在]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期内未收到应答就拆除链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1110925018}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] timer-hold retry 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_149250512}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_21171_18224_1110925019}
:::

::: {#-1780261722 .myid}
[]{#_Toc261964936}[]{#_Toc205607543}[]{#_Toc13287735}[]{#_Toc404785073}[]{#struct_0_21171_18224_206169307}[]{#_Toc324864445}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- async-mode**

------------------------------------------------------------------------

[**[async-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x1029986975}[命令用来设置异步串口的工作模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **async-mode**]{lang="EN-US"}]{#struct_0_21171_18224_x1778542638}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1115670353}

[**[async-mode]{lang="EN-US"}**[ { **flow** \| **protocol** }]{lang="EN-US"}]{#struct_0_21171_18224_x98892578}

[**[undo async-mode]{lang="EN-US"}**]{#struct_0_21171_18224_1359514718}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1269322243}

[[异步串口工作在协议模式（]{style="font-family:宋体"}**[protocol]{lang="EN-US"}**]{#struct_0_21171_18224_x2095432415}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1908563820}

[[异步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_206234843}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_2037621201}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1052076991}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1837620377}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x165997358}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x339783197}

[**[flow]{lang="EN-US"}**]{#struct_0_21171_18224_x1612490918}[：流模式，也称交互模式。指物理连接建立之后，链路的两端进行交互，主叫端向被叫端发送配置命令（与用户从远端手工键入配置命令效果相同），设置被叫端的链路层协议工作参数，然后建立链路。一般用于拨号等人机交互的情况。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**]{#struct_0_21171_18224_1726700997}[：协议模式。指物理连接建立之后，接口直接采用已有的链路层协议配置参数建立链路。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_146813829}

[[同[/]{lang="EN-US"}异步串口只有通过命令]{style="font-family:宋体"}**[physical-mode async]{lang="EN-US"}**]{#struct_0_21171_18224_206562523}[切换到异步模式后才能配置]{style="font-family:宋体"}**[async-mode]{lang="EN-US"}**[命令。]{style="font-family:宋体"}[当异步串口工作在流模式时，不允许进行]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的配置；当异步串口工作在协议模式时，允许进行]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1061523091}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1016090365}[设置异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[的工作模式为流模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1704243092}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\] async-mode flow]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_909684617}[设置]{style="font-family:宋体"}[同[/]{lang="EN-US"}异步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的工作模式为流模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x984194952}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] async-mode flow]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1689392848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[physical-mode]{lang="EN-US"}**]{#struct_0_21171_18224_206628059}
:::

::::: {#-2091441387 .myid}
[]{#_Toc404785074}[]{#struct_0_21171_18224_x1801173230}[]{#_Toc261964938}[]{#_Toc205607545}[]{#_Toc13287737}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- baudrate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](WAN接口命令.files/image001.jpg){width="62" height="24"}]{lang="EN-US"}]{#struct_0_21171_18224_2008054407}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21171_18224_x1888294443}
:::

**[ ]{lang="EN-US"}**

[**[baudrate]{lang="EN-US"}**]{#struct_0_21171_18224_1530022531}[命令用来设置同步串口的波特率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **baudrate**]{lang="EN-US"}]{#struct_0_21171_18224_x1572864429}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_810694890}

[**[baudrate]{lang="EN-US"}**[ *baudrate*]{lang="EN-US"}]{#struct_0_21171_18224_1201857394}

[**[undo baudrate]{lang="EN-US"}**]{#struct_0_21171_18224_2020245690}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_206431451}

[[同步串口的波特率为]{style="font-family:宋体"}[64000bps]{lang="EN-US"}]{#struct_0_21171_18224_276109587}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2004251062}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_537854980}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x589821195}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x201147887}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1845670232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x762223583}

[*[baudrate]{lang="EN-US"}*]{#struct_0_21171_18224_x596345238}[：同步串口的波特率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_206496987}

[[同步串口支持的波特率有：]{style="font-family:宋体"}]{#struct_0_21171_18224_x29682242}

[[1200bps]{lang="EN-US"}]{#struct_0_21171_18224_x718586507}[、]{style="font-family:宋体"}[2400bps]{lang="EN-US"}[、]{style="font-family:宋体"}[4800bps]{lang="EN-US"}[、]{style="font-family:宋体"}[9600bps]{lang="EN-US"}[、]{style="font-family:宋体"}[19200bps]{lang="EN-US"}[、]{style="font-family:宋体"}[38400bps]{lang="EN-US"}[、]{style="font-family:宋体"}[56000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[57600bps]{lang="EN-US"}[、]{style="font-family:宋体"}[64000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[72000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[115200bps]{lang="EN-US"}[、]{style="font-family:宋体"}[128000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[192000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[256000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[384000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[512000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[1024000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[2048000bps]{lang="EN-US"}[、]{style="font-family:宋体"}[4096000bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[另外同步串口对于不同的物理电气规程，所支持的波特率范围有所不同。]{style="font-family:宋体"}]{#struct_0_21171_18224_x19022925}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V.24 DTE/DCE]{lang="EN-US"}]{#struct_0_21171_18224_x363328501}[：]{lang="EN-US" style="font-family:宋体"}[1200bps]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[64000bps]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V.35 DCE/DCE]{lang="EN-US"}]{#struct_0_21171_18224_1667333131}[、]{lang="EN-US" style="font-family:宋体"}[X.21 DTE/DCE]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[EIA/TIA-449 DTE/DCE]{lang="EN-US"}[以及]{lang="EN-US" style="font-family:宋体"}[EIA-530 DTE/DCE]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[1200bps]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[8192000bps]{lang="EN-US"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21171_18224_1322103228}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在设置同步串口波特率时，要注意同步串口的外接电缆的电气规程等因素；]{style="font-family:宋体"}]{#struct_0_21171_18224_x933981808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DCE]{lang="EN-US"}]{#struct_0_21171_18224_1867148893}[设备和]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备之间线路传输的波特率，由]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_206824667}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1956379994}[设置]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备的同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的波特率为]{style="font-family:宋体"}[115200bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_506837761}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] baudrate 115200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_770339625}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[virtualbaudrate]{lang="EN-US"}**]{#struct_0_21171_18224_660796219}
:::::

::::: {#424787513 .myid}
[]{#_Toc404785075}[]{#struct_0_21171_18224_1417027022}[]{#_Toc261964939}[]{#_Toc205607546}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_490109378}[命令用来设置同步串口的时钟选择方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **clock**]{lang="EN-US"}]{#struct_0_21171_18224_x612394412}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_206890203}

[**[clock ]{lang="EN-US"}**[{ **dteclk1** \| **dteclk2** \| **dteclk3** \| **dteclk4** \| **dteclk5** \| **dteclkauto** }]{lang="EN-US"}]{#struct_0_21171_18224_1168650037}

[**[clock]{lang="EN-US"}**[ { **dceclk1** \| **dceclk2** \| **dceclk3** }]{lang="EN-US"}]{#struct_0_21171_18224_x215985273}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_1897148622}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x409357388}

[[同步串口]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_x999010598}[侧的时钟为]{style="font-family:宋体"}**[dteclk1]{lang="EN-US"}**[，同步串口]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧的时钟为]{style="font-family:宋体"}**[dceclk1]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1611913928}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x263891954}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1641572770}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_206300376}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1591584034}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1608264310}

[**[dteclk1]{lang="EN-US"}**]{#struct_0_21171_18224_427685528}[：设置接口时钟方式为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dteclk2]{lang="EN-US"}**]{#struct_0_21171_18224_541555813}[：设置接口时钟方式为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dteclk3]{lang="EN-US"}**]{#struct_0_21171_18224_x182150819}[：设置接口时钟方式为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dteclk4]{lang="EN-US"}**]{#struct_0_21171_18224_522863720}[：设置接口时钟方式为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dteclk5]{lang="EN-US"}**]{#struct_0_21171_18224_1617997575}[：设置接口时钟方式为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dteclkauto]{lang="EN-US"}**]{#struct_0_21171_18224_1525774493}[：设置接口时钟方式为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[自动协商。]{style="font-family:宋体"}

[**[dceclk1]{lang="EN-US"}**]{#struct_0_21171_18224_206365912}[：设置接口时钟方式为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dceclk2]{lang="EN-US"}**]{#struct_0_21171_18224_x316270770}[：设置接口时钟方式为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dceclk3]{lang="EN-US"}**]{#struct_0_21171_18224_397988340}[：设置接口时钟方式为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[时钟选择方式]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](WAN接口命令.files/image001.jpg){#图片 3 width="62" height="24"}]{lang="EN-US"}]{#struct_0_21171_18224_72327096}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当接口工作在]{lang="EN-US" style="font-family:KaiTi_GB2312"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_1877161168}[方式时，支持命令]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[clock]{lang="EN-US"}**[ { **dteclk1** \| **dteclk2** \| **dteclk3** \| **dteclk4** \| ]{lang="EN-US"}**[dteclk5]{lang="EN-US"}**[ \| **dteclkauto** }]{lang="EN-US"}[；]{lang="EN-US" style="font-family:
KaiTi_GB2312"}[当接口工作在]{lang="EN-US" style="font-family:KaiTi_GB2312"}[DCE]{lang="EN-US"}[方式时，支持命令]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[clock]{lang="EN-US"}**[ { **dceclk1** \| **dceclk2** \| **dceclk3** }]{lang="EN-US"}[。]{lang="EN-US" style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[命令]{style="font-family:KaiTi_GB2312"}]{#struct_0_21171_18224_1210368079}**[clock]{lang="EN-US"}**[ { **dceclk1** \| **dceclk2** \| **dceclk3** }]{lang="EN-US"}[的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_968141343}

[[同步串口有两种工作方式：]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_x1129963523}[和]{style="font-family:宋体"}[DCE]{lang="EN-US"}[，不同的工作方式有不同的工作时钟选择。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同步串口作为]{style="font-family:宋体"}]{#struct_0_21171_18224_206169304}[DCE]{lang="EN-US"}[侧，则需要向对端]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧提供时钟]{style="font-family:宋体"}[DCEclk]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同步串口作为]{style="font-family:宋体"}]{#struct_0_21171_18224_x1029986974}[DTE]{lang="EN-US"}[侧，则需要接受对端]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧提供的时钟，由于同步设备的接收和发送时钟是独立的，则]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧的接收时钟可以选择]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧的发送或接收时钟，]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧的发送时钟也可以选择]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧的发送或接收时钟，由此产生五种组合，即在]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧可以有五种时钟选择。]{style="font-family:宋体"}

[]{#struct_0_21171_18224_950340717}[]{#_Toc95307558}[]{#_Toc85599404}[]{#_Toc81465847}[]{#_Toc81372454}[]{#_Toc74660344}[]{#_Toc74660334}[]{#_Toc72586850}[]{#_Toc65753492}[]{#_Toc60051636}[]{#_Toc42510476}[]{#_Toc35240053}[]{#_Toc34558283}[[图1-1 ]{lang="EN-US"}[同步串口时钟选择示意图]{style="font-family:黑体"}]{#_Toc18140828}

[[![](WAN接口命令.files/image002.png){#图片 4 width="351" height="80"}]{lang="EN-US"}]{#struct_0_21171_18224_1560977117}

[ ]{lang="EN-US"}

[[其中，]{style="font-family:宋体"}[TxClk]{lang="EN-US"}]{#struct_0_21171_18224_x1914993952}[为发送时钟，]{style="font-family:宋体"}[RxClk]{lang="EN-US"}[为接收时钟。]{style="font-family:宋体"}

[[时钟选择方法规定如下表所示。]{style="font-family:宋体"}]{#struct_0_21171_18224_1893310592}

[]{#struct_0_21171_18224_x1002481463}[]{#_Toc95307564}[]{#_Toc85599407}[]{#_Toc81465850}[]{#_Toc81465255}[]{#_Toc81372457}[]{#_Toc74660337}[]{#_Toc72586843}[]{#_Toc65753485}[]{#_Toc60051629}[]{#_Toc35240065}[]{#_Toc34558301}[]{#_Toc28138659}[[表1-1 ]{lang="EN-US"}[同步串口]{style="font-family:黑体"}[DTE]{lang="EN-US"}]{#_Toc18140830}[侧时钟的选择方法]{style="font-family:黑体"}

[]{#table_struct_0_1832177982}[[选择方法]{style="font-family:黑体"}]{#struct_0_21171_18224_1075663456}
:::::

[[意义]{style="font-family:黑体"}]{#struct_0_21171_18224_206234840}

[[DTEclk1]{lang="EN-US"}]{#struct_0_21171_18224_2037621200}

[[TxClk = TxClk, RxClk = RxClk]{lang="EN-US"}]{#struct_0_21171_18224_x1052011455}

[[DTEclk2]{lang="EN-US"}]{#struct_0_21171_18224_732363324}

[[TxClk = TxClk, RxClk = TxClk]{lang="EN-US"}]{#struct_0_21171_18224_x923764991}

[[DTEclk3]{lang="EN-US"}]{#struct_0_21171_18224_x1393217768}

[[TxClk = RxClk, RxClk = TxClk]{lang="EN-US"}]{#struct_0_21171_18224_1831106855}

[[DTEclk4]{lang="EN-US"}]{#struct_0_21171_18224_206562520}

[[TxClk = RxClk, RxClk = RxClk]{lang="EN-US"}]{#struct_0_21171_18224_1061523092}

[[DTEclk5]{lang="EN-US"}]{#struct_0_21171_18224_x1015893757}

[[TxClk = Local, RxClk = Local]{lang="EN-US"}]{#struct_0_21171_18224_390448643}

[ ]{lang="EN-US"}

[[其中，']{style="font-family:宋体"}[=]{lang="EN-US"}]{#struct_0_21171_18224_x2071263969}['前为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧时钟，']{style="font-family:宋体"}[=]{lang="EN-US"}['后为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧时钟。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[同步串口]{style="font-family:黑体"}[DCE]{lang="EN-US"}]{#struct_0_21171_18224_1459286621}[侧时钟的选择方法]{style="font-family:黑体"}

[]{#table_struct_0_1859856382}[[选择方法]{style="font-family:黑体"}]{#struct_0_21171_18224_206628056}

[[意义]{style="font-family:黑体"}]{#struct_0_21171_18224_x1801173245}

[[DCEclk1]{lang="EN-US"}]{#struct_0_21171_18224_x1527201394}

[[TxClk = Local, RxClk = Local]{lang="EN-US"}]{#struct_0_21171_18224_688887596}

[[DCEclk2]{lang="EN-US"}]{#struct_0_21171_18224_x64445958}

[[TxClk = Local, RxClk = Line]{lang="EN-US"}]{#struct_0_21171_18224_898378440}

[[DCEclk3]{lang="EN-US"}]{#struct_0_21171_18224_x2132974748}

[[TxClk = Line, RxClk = Line]{lang="EN-US"}]{#struct_0_21171_18224_206431448}

[ ]{lang="EN-US"}

[[其中，']{style="font-family:宋体"}[=]{lang="EN-US"}]{#struct_0_21171_18224_x2062542564}['前为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧时钟，']{style="font-family:宋体"}[=]{lang="EN-US"}['后为时钟信号来源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_342492383}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1777174539}[设置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧的时钟选择方式为]{style="font-family:宋体"}[DTEclk2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_65341268}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] clock dteclk2]{lang="EN-US"}

::: {#1985170611 .myid}
[]{#_Toc261964950}[]{#_Toc205607557}[]{#_Toc13287744}[]{#_Toc404785076}[]{#struct_0_21171_18224_x2097734846}[]{#_Toc261964940}[]{#_Toc205607547}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- code**

------------------------------------------------------------------------

[**[code]{lang="EN-US"}**]{#struct_0_21171_18224_1148441677}[命令用来配置同步串口的数字信号编码格式。]{style="font-family:宋体"}

[**[undo code]{lang="EN-US"}**]{#struct_0_21171_18224_206496984}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x29682239}

[**[code]{lang="EN-US"}**[ { **nrz** \| **nrzi** }]{lang="EN-US"}]{#struct_0_21171_18224_1237728634}

[**[undo code]{lang="EN-US"}**]{#struct_0_21171_18224_1134606741}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1934742625}

[[同步串口的数字信号编码格式为]{style="font-family:宋体"}[NRZ]{lang="EN-US"}]{#struct_0_21171_18224_1740962159}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x591963781}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1296812224}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_206824664}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1956379993}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_2072921702}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x597445982}

[**[nrz]{lang="EN-US"}**]{#struct_0_21171_18224_x1094220803}[：采用]{style="font-family:宋体"}[NRZ]{lang="EN-US"}[（]{style="font-family:宋体"}[Non-Return to Zero]{lang="EN-US"}[，不归零）的数字信号编码格式。]{style="font-family:宋体"}

[**[nrzi]{lang="EN-US"}**]{#struct_0_21171_18224_x586338092}**[：]{style="font-family:宋体"}**[采用]{style="font-family:宋体"}[NRZI]{lang="EN-US"}[（]{style="font-family:宋体"}[Non-Return to Zero Inverted]{lang="EN-US"}[，反向不归零）的数字信号编码格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1958453191}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_323339971}[配置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的数字信号编码格式为]{style="font-family:宋体"}[NRZI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_206890200}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] code nrzi]{lang="EN-US"}
:::

::: {#538040344 .myid}
[]{#_Toc404785077}[]{#struct_0_21171_18224_1168650040}[]{#_Toc261964942}[]{#_Toc205607549}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- crc**

------------------------------------------------------------------------

[**[crc]{lang="EN-US"}**]{#struct_0_21171_18224_x215788666}[命令用来配置同步串口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验模式。]{style="font-family:宋体"}

[**[undo crc]{lang="EN-US"}**]{#struct_0_21171_18224_x873302122}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_282782550}

[**[crc ]{lang="EN-US"}**[{ **16** \| **32** \| **none** }]{lang="EN-US"}]{#struct_0_21171_18224_x1446197114}

[**[undo crc]{lang="EN-US"}**]{#struct_0_21171_18224_731015647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_807457973}

[[使用]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_21171_18224_69022937}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_206300377}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1591584035}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1608329846}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_751189379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1293054258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2132582255}

[**[16]{lang="EN-US"}**]{#struct_0_21171_18224_x352745327}[：同步串口使用]{style="font-family:宋体"}[16]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_21171_18224_2079173543}[：同步串口使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_21171_18224_1707449532}[：同步串口不进行]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_206365913}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x316270769}[配置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_397398517}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] crc 32]{lang="EN-US"}
:::

::: {#-1209445327 .myid}
[]{#_Toc261964946}[]{#_Toc205607553}[]{#_Toc404785078}[]{#struct_0_21171_18224_x1472493258}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- detect dcd**

------------------------------------------------------------------------

[**[detect]{lang="PT-BR"}**]{#struct_0_21171_18224_x1654280191}[ **dcd**]{lang="PT-BR"}[命令用来打开数据载波检测功能。即检测]{style="font-family:宋体"}[DSU/CSU]{lang="EN-US"}[的]{style="font-family:宋体"}[DCD]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Carrier Detect]{lang="EN-US"}[，数据载波检测）信号。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_21171_18224_330658834}**[detect]{lang="PT-BR"}**[ **dcd**]{lang="PT-BR"}[命令用来关闭数据载波检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1332821855}

[**[detect]{lang="PT-BR"}**]{#struct_0_21171_18224_x83358665}[ **dcd**]{lang="PT-BR"}

[**[undo detect]{lang="PT-BR"}**]{#struct_0_21171_18224_206169305}[ **dcd**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1029986973}

[[数据载波检测功能处于打开状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_1709855604}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1365993960}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x423251848}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1144157517}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1544289457}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1538892401}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_849091516}

[[系统在判断同步串口的状态（]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_21171_18224_206234841}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[）时，缺省情况下将同时检测]{style="font-family:宋体"}[DSR]{lang="EN-US"}[信号、]{style="font-family:宋体"}[DCD]{lang="EN-US"}[信号以及接口是否外接电缆。只有当三个信号全部有效时，系统才认为同步串口处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，否则为]{style="font-family:宋体"}[down]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_2037621199}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1286050874}[打开同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的数据载波检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1129084791}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] detect dcd]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_379019627}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[detect dsr-dtr]{lang="EN-US"}**]{#struct_0_21171_18224_x827770566}
:::

::: {#837565686 .myid}
[]{#_Toc261964944}[]{#_Toc205607551}[]{#_Toc404785079}[]{#struct_0_21171_18224_x1853226631}[]{#_Toc324864446}[]{#_Toc319999868}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- detect dsr-dtr**

------------------------------------------------------------------------

[**[detect dsr-dtr]{lang="EN-US"}**]{#struct_0_21171_18224_x768870880}[命令用来打开电平检测功能，即检测]{style="font-family:宋体"}[DSU/CSU]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Service Unit/Channel Service Unit]{lang="EN-US"}[，数据服务单元]{style="font-family:宋体"}[/]{lang="EN-US"}[信道服务单元，表示数字]{style="font-family:宋体"}[MODEM]{lang="EN-US"}[）的]{style="font-family:宋体"}[DSR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Set Ready]{lang="EN-US"}[，数据置位就绪）和]{style="font-family:宋体"}[DTR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Terminal Ready]{lang="EN-US"}[，数据终端就绪）信号。]{style="font-family:宋体"}

[**[undo detect dsr-dtr]{lang="EN-US"}**]{#struct_0_21171_18224_206562521}[命令用来关闭电平检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1061523093}

[**[detect dsr-dtr]{lang="EN-US"}**]{#struct_0_21171_18224_x1015959293}

[**[undo detect dsr-dtr]{lang="PT-BR"}**]{#struct_0_21171_18224_318404734}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x419181379}

[[电平检测功能处于打开状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_x2050925190}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1422065069}

[[同步串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_1583332280}[异步串口视图]{style="font-family:宋体"}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_1018138198}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_206628057}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1801173244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_38882547}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2049951267}

[[如果设置禁止异步串口进行电平检测，系统将不检测异步串口是否外接电缆，自动向用户报告异步串口的状态为]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_21171_18224_1767328622}[，且]{style="font-family:宋体"}[DTR = up]{lang="EN-US"}[、]{style="font-family:宋体"}[DSR = up]{lang="EN-US"}[；如果设置允许异步串口进行电平检测，则系统将不仅检测异步串口是否外接电缆，同时还要检测]{style="font-family:宋体"}[DSR]{lang="EN-US"}[信号，只有当该信号有效时，系统才认为异步串口处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，否则，为]{style="font-family:宋体"}[down]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[系统在判断同步串口的状态（]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_21171_18224_x1950765292}[或]{style="font-family:宋体"}[down]{lang="EN-US"}[）时，缺省情况下将同时检测]{style="font-family:宋体"}[DSR]{lang="EN-US"}[信号、]{style="font-family:宋体"}[DCD]{lang="EN-US"}[信号以及接口是否外接电缆。只有当三个信号全部有效时，系统才认为同步串口处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，否则为]{style="font-family:宋体"}[down]{lang="EN-US"}[状态。如果禁止同步串口进行电平检测，系统检测到外接电缆后，接口状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[，且]{style="font-family:宋体"}[DTR = up]{lang="EN-US"}[、]{style="font-family:宋体"}[DSR = up]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_438435675}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1783974785}[打开同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的电平检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_206431449}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] detect dsr-dtr]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x2062542565}[打开异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[的电平检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1223591558}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\] detect dsr-dtr]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x499503880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[detect dcd]{lang="EN-US"}**]{#struct_0_21171_18224_x1444624323}
:::

::: {#-320030929 .myid}
[]{#_Toc261964937}[]{#_Toc205607544}[]{#_Toc13287736}[]{#_Toc404785080}[]{#struct_0_21171_18224_x1195094471}[]{#_Toc326766650}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- display interface async**

------------------------------------------------------------------------

[**[display interface async]{lang="EN-US"}**]{#struct_0_21171_18224_x1526623979}[命令用来显示异步串口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_742753456}

[**[display interface]{lang="EN-US"}**[ \[ **async** \[ *interface-number* ]{lang="EN-US"}]{#struct_0_21171_18224_x29682240}[\] \]]{lang="EN-US" style="font-size:10.0pt;color:black"}[ \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x718586509}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x19416141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1666822408}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_915028985}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_356610843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x679041457}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_206824665}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1956379992}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x655961653}[：显示指定异步串口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_21171_18224_x483885491}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_21171_18224_1450708891}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_21171_18224_1052622470}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1264793215}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_21171_18224_1700289258}**[async]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[async]{lang="EN-US"}**]{#struct_0_21171_18224_1536114083}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的异步串口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_206890201}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1168650039}[显示异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface async 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_339762902}

[Async2/4/0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Async2/4/0 Interface]{lang="EN-US"}

[Bandwidth: 9kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Physical layer: asynchronous, Baudrate: 9600 bps]{lang="EN-US"}

[Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Input:]{lang="EN-US"}

[  1 packets, 0 bytes]{lang="EN-US"}

[  0 broadcasts, 0 multicasts]{lang="EN-US"}

[  1 errors, 0 runts, 0 giants]{lang="EN-US"}

[  0 crc, 0 align errors, 0 overruns]{lang="EN-US"}

[  0 aborts, 0 no buffers]{lang="EN-US"}

[  1 frame errors]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}

[  0 deferred]{lang="EN-US"}

[DCD: DOWN, DTR: UP, DSR: DOWN, RTS: UP, CTS: DOWN]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1591584032}[显示异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface async 2/4/0 brief]{lang="EN-US"}]{#struct_0_21171_18224_1608395382}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Asy2/4/0             DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1168741621}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的异步串口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface async brief down]{lang="EN-US"}]{#struct_0_21171_18224_206365910}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Asy2/4/0             ADM  Administratively]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display interface async]{lang="EN-US"}]{#struct_0_21171_18224_x316270768}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1861581658}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_397464053}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x464376632}

[[Async2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x1564418936}

[[Current state]{lang="EN-US"}]{#struct_0_21171_18224_x1657913033}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_1748689609}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_206169302}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x1029986980}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x1018831143}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_21171_18224_x1868948564}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1453002419}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x699662336}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_206234838}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_1228317144}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_21171_18224_38911844}

[[Bandwidth]{lang="EN-US"}]{#struct_0_21171_18224_975969051}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_21171_18224_x1350024585}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_21171_18224_206562518}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_21171_18224_x1659466100}

[[Hold timer]{lang="EN-US"}]{#struct_0_21171_18224_x915592776}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_29026635}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_21171_18224_x1616552236}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_x1616552230}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_21171_18224_x1826316493}

[[网络层协议处理状况]{style="font-family:宋体"}]{#struct_0_21171_18224_206628054}

[[Link layer protocol: PPP]{lang="EN-US"}]{#struct_0_21171_18224_x1801173243}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_21171_18224_1604966488}

[[LCP: initial]{lang="EN-US"}]{#struct_0_21171_18224_1501826048}

[[LCP]{lang="EN-US"}]{#struct_0_21171_18224_909904923}[（链路控制协议）初始化完成]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_1517396581}

[[输出队列（紧急队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x111546763}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - Protocol queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_1518248549}

[[输出队列（协议队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x691885502}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - FIFO queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_1518314085}

[[输出队列（先进先出队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x311371861}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_x646415857}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_919668084}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_x1938459121}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x2062542574}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Physical layer]{lang="EN-US"}]{#struct_0_21171_18224_342557919}

[[物理层链路信息]{style="font-family:宋体"}]{#struct_0_21171_18224_956122415}

[[Baudrate]{lang="EN-US"}]{#struct_0_21171_18224_206496982}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_21171_18224_x29682237}

[[Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_x1987200363}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_x1357598367}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_1418339871}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_206300375}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input:]{lang="EN-US"}]{#struct_0_21171_18224_1591584033}

[[  1 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_1608460918}

[[  0 broadcasts, 0 multicasts]{lang="EN-US"}]{#struct_0_21171_18224_206365911}

[[  1 errors, 0 runts, 0 giants]{lang="EN-US"}]{#struct_0_21171_18224_x316270767}

[[  0 crc, 0 align errors, 0 overruns]{lang="EN-US"}]{#struct_0_21171_18224_398316021}

[[  0 aborts, 0 no buffers]{lang="EN-US"}]{#struct_0_21171_18224_x1332252974}

[[  1 frame errors]{lang="EN-US"}]{#struct_0_21171_18224_206169303}

[[接口收到的总报文数和总字节数：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1029986979}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcasts]{lang="EN-US"}]{#struct_0_21171_18224_190825830}[：接收的广播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_21171_18224_206234839}[：接收的组播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_1228317143}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[runts]{lang="EN-US"}]{#struct_0_21171_18224_38584164}[：接口接收到小于规定的最小报文长度报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_21171_18224_206562519}[：接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[crc]{lang="EN-US"}]{#struct_0_21171_18224_x1659466099}[：接收长度正常但]{style="font-family:宋体"}[CRC ]{lang="EN-US"}[校验错误的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[align errors]{lang="EN-US"}]{#struct_0_21171_18224_x2124856534}[：排列错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_21171_18224_721467470}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_21171_18224_206628055}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffers]{lang="EN-US"}]{#struct_0_21171_18224_x1801173242}[：在接收报文时由于内部缓存满，导致帧丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[frame errors]{lang="EN-US"}]{#struct_0_21171_18224_x1123916867}[：帧错误]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_21171_18224_206431447}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_x2062542575}

[[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}]{#struct_0_21171_18224_x1223526022}

[[  0 deferred]{lang="EN-US"}]{#struct_0_21171_18224_206496983}

[[接口发送的报文数和总字节数]{style="font-family:宋体"}]{#struct_0_21171_18224_x29682238}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_1237728635}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_21171_18224_206824663}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[collisions]{lang="EN-US"}]{#struct_0_21171_18224_x1956379990}[：发送报文时，检测到冲突的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deferred]{lang="EN-US"}]{#struct_0_21171_18224_206890199}[：因为延时或超时无法发送报文的数目]{style="font-family:宋体"}

[[DCD: DOWN, DTR: UP, DSR: DOWN, RTS: UP, CTS: DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x1987200364}

[[DCD]{lang="EN-US"}]{#struct_0_21171_18224_x954313840}[（]{style="font-family:宋体"}[Data Carrier Detect]{lang="EN-US"}[）信号处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，]{style="font-family:宋体"}[DTR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Terminal Ready]{lang="EN-US"}[）信号处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，]{style="font-family:宋体"}[DSR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Set Ready]{lang="EN-US"}[）信号处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，关于]{style="font-family:宋体"}[DCD]{lang="EN-US"}[、]{style="font-family:宋体"}[DTR]{lang="EN-US"}[和]{style="font-family:宋体"}[DSR]{lang="EN-US"}[请参考]{style="font-family:宋体"}**[detect]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[RTS]{lang="EN-US"}]{#struct_0_21171_18224_1772384319}[（]{style="font-family:宋体"}[Request to Send]{lang="EN-US"}[）处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，]{style="font-family:宋体"}[CTS]{lang="EN-US"}[（]{style="font-family:宋体"}[Clear to Send]{lang="EN-US"}[）处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_21171_18224_309790612}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x573884356}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_21171_18224_1772449855}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_21171_18224_x786490612}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_21171_18224_x963033878}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_21171_18224_1772253247}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_x1655789081}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_21171_18224_1772318783}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_21171_18224_1134858313}

[[Link]{lang="EN-US"}]{#struct_0_21171_18224_x1195394838}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_1772646463}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x2038370208}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_170838278}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_21171_18224_1772711999}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_21171_18224_170903814}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_1910816785}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_x894112421}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_1852609083}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_1375661728}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_21171_18224_1256833064}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_21171_18224_1772580927}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21171_18224_367866981}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_x661187756}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_21171_18224_1772908607}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_21171_18224_x1197306105}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_21171_18224_1772974143}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x106559921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x367523148}

::: {#1875141752 .myid}
[]{#_Toc404785081}[]{#struct_0_21171_18224_1391623930}[]{#_Toc261964945}[]{#_Toc205607552}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- display interface serial**

------------------------------------------------------------------------

[**[display interface serial]{lang="EN-US"}**]{#struct_0_21171_18224_275184279}[命令用来显示]{style="font-family:
宋体"}[Serial]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_739257832}

[**[display interface]{lang="EN-US"}**[ \[ **serial** \[ *interface-number* ]{lang="EN-US"}]{#struct_0_21171_18224_310249363}[\] \] ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_673687374}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1752142532}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1148521094}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1480476713}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_1114838978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x2047694598}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_863397998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1772449856}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x786425076}[：显示指定]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_21171_18224_x1365537801}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_21171_18224_x924428944}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_21171_18224_x964717665}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1163044404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_21171_18224_x1764022728}**[serial]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_82555662}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1772253248}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1655854617}[显示同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface serial 2/1/0]{lang="EN-US"}]{#struct_0_21171_18224_x1232052520}

[Serial2/1/0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Serial2/1/0 Interface]{lang="EN-US"}

[Bandwidth: 64kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer]{lang="EN-US"}[：]{style="font-family:宋体"}[10 seconds, retry times: 5]{lang="EN-US"}

[Internet Address: 9.9.9.6/24 Primary]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: opened]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Physical layer: synchronous, Baudrate: 64000 bps]{lang="EN-US"}

[Interface: DCE]{lang="EN-US"}

[Cable type: V35]{lang="EN-US"}

[Clock mode: DCECLK]{lang="EN-US"}

[Last 300 seconds input rate: 2.40 bytes/sec, 19 bits/sec, 0.20 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 2.40 bytes/sec, 19 bits/sec, 0.20 packets/sec]{lang="EN-US"}

[Input: ]{lang="EN-US"}

[  6668 packets, 80414 bytes]{lang="EN-US"}

[  0 broadcasts, 0 multicasts]{lang="EN-US"}

[  0 errors, 0 runts, 0 giants]{lang="EN-US"}

[  0 crc, 0 align errors, 0 overruns]{lang="EN-US"}

[  0 aborts, 0 no buffers]{lang="EN-US"}

[  0 frame errors]{lang="EN-US"}

[Output: ]{lang="EN-US"}

[  6670 packets, 80446 bytes]{lang="EN-US"}

[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}

[  0 deferred]{lang="EN-US"}

[DCD: UP, DTR: UP, DSR: UP, RTS: UP, CTS: UP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1135317065}[显示同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface serial 2/1/0 brief]{lang="EN-US"}]{#struct_0_21171_18224_1983100779}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Ser2/1/0             UP   UP(s)    \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1390507862}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface serial brief down]{lang="EN-US"}]{#struct_0_21171_18224_1772646464}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Ser2/1/0             ADM  Administratively]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display interface serial]{lang="EN-US"}]{#struct_0_21171_18224_x2038304672}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1853855186}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_664766539}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_2036123472}

[[Serial2/1/0]{lang="EN-US"}]{#struct_0_21171_18224_473922765}

[[Current state]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_21171_18224_2037097091}

[[串口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_1772712000}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_697769435}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该串口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_1407445189}[：表示该串口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x814650763}[：该串口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_21171_18224_213439201}

[[该接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_1942155564}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_1772515392}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_1852543547}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_x1367619943}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_21171_18224_1668523841}

[[Bandwidth]{lang="EN-US"}]{#struct_0_21171_18224_711110901}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_21171_18224_1772580928}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_21171_18224_367408229}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_21171_18224_778900931}

[[Hold timer]{lang="EN-US"}]{#struct_0_21171_18224_x325571153}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_527529433}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_21171_18224_341925599}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_x1219076386}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet Address]{lang="EN-US"}]{#struct_0_21171_18224_1772908608}

[[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21171_18224_x1196716281}[地址]{style="font-family:宋体"}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_21171_18224_x675458664}

[[串口的数据链路层协议]{style="font-family:宋体"}]{#struct_0_21171_18224_1600544172}

[[LCP: opened]{lang="EN-US"}]{#struct_0_21171_18224_x595593809}

[[表示]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_21171_18224_1772974144}[连接建立成功]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_819929683}

[[输出队列（紧急队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_1772449853}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - Protocol queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_1750972878}

[[输出队列（协议队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_1140931256}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - FIFO queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_x1655658009}

[[输出队列（先进先出队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_176827061}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_x290054425}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_1276029516}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_594811795}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_439154417}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Physical layer]{lang="EN-US"}]{#struct_0_21171_18224_795988069}

[[物理层链路信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x1991897974}

[[Baudrate]{lang="EN-US"}]{#struct_0_21171_18224_796053605}

[[串口的波特率]{style="font-family:宋体"}]{#struct_0_21171_18224_x1908017846}

[[Interface: DCE]{lang="EN-US"}]{#struct_0_21171_18224_x1794288626}

[[Cable type: V35]{lang="EN-US"}]{#struct_0_21171_18224_1772318781}

[[Clock mode: DCECLK]{lang="EN-US"}]{#struct_0_21171_18224_1134989385}

[[同步串口]{style="font-family:宋体"}[DCE]{lang="EN-US"}]{#struct_0_21171_18224_368657465}[侧的时钟选择方式]{style="font-family:宋体"}

[[Last 300 seconds input rate 2.40 bytes/sec, 19 bits/sec, 0.20 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_1573536195}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_1772646461}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate 2.40 bytes/sec, 19 bits/sec, 0.20 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_x2038501280}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_159031065}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input:]{lang="EN-US"}]{#struct_0_21171_18224_1772711997}

[[  6668 packets, 80414 bytes]{lang="EN-US"}]{#struct_0_21171_18224_1910423569}

[[  0 broadcasts, 0 multicasts]{lang="EN-US"}]{#struct_0_21171_18224_x1268603186}

[[  0 errors, 0 runts, 0 giants]{lang="EN-US"}]{#struct_0_21171_18224_1148444169}

[[  0 crc, 0 align errors, 0 overruns]{lang="EN-US"}]{#struct_0_21171_18224_1772515389}

[[  0 aborts, 0 no buffers]{lang="EN-US"}]{#struct_0_21171_18224_1853133372}

[[  0 frame errors]{lang="EN-US"}]{#struct_0_21171_18224_x574699740}

[[接口收到的总报文数和总字节数：]{style="font-family:宋体"}]{#struct_0_21171_18224_1772580925}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcasts]{lang="EN-US"}]{#struct_0_21171_18224_367735909}[：接收的广播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_21171_18224_x2006773065}[：接收的组播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_1772908605}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[runts]{lang="EN-US"}]{#struct_0_21171_18224_x1197437177}[：接口接收到小于规定的最小报文长度报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_21171_18224_904735420}[：接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[crc]{lang="EN-US"}]{#struct_0_21171_18224_1772974141}[：接收长度正常但]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[align errors]{lang="EN-US"}]{#struct_0_21171_18224_x106690993}[：排列错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_21171_18224_833810859}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_21171_18224_1772384318}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffers]{lang="EN-US"}]{#struct_0_21171_18224_309725076}[：在接收报文时由于内部缓存满，导致帧丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[frame errors]{lang="EN-US"}]{#struct_0_21171_18224_1404784615}[：帧错误]{lang="EN-US" style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_21171_18224_1772449854}

[[  6670 packets, 80446 bytes]{lang="EN-US"}]{#struct_0_21171_18224_x786556148}

[[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}]{#struct_0_21171_18224_1367158276}

[[  0 deferred]{lang="EN-US"}]{#struct_0_21171_18224_1772253246}

[[接口发送的报文数和总字节数]{style="font-family:宋体"}]{#struct_0_21171_18224_x1655723545}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_739701083}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_21171_18224_1772318782}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[collisions]{lang="EN-US"}]{#struct_0_21171_18224_1134923849}[：发送报文时，检测到冲突的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deferred]{lang="EN-US"}]{#struct_0_21171_18224_2005371027}[：因为延时或超时无法发送报文的数目]{style="font-family:宋体"}

[[DCD: UP, DTR: UP, DSR: UP, RTS: UP, CTS: UP]{lang="EN-US"}]{#struct_0_21171_18224_1772646462}

[[DCD]{lang="EN-US"}]{#struct_0_21171_18224_x2038435744}[（]{style="font-family:宋体"}[Data Carrier Detect]{lang="EN-US"}[）、]{style="font-family:宋体"}[DTR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Terminal Ready]{lang="EN-US"}[）和]{style="font-family:宋体"}[DSR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Set Ready]{lang="EN-US"}[）信号处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，关于]{style="font-family:宋体"}[DCD]{lang="EN-US"}[、]{style="font-family:宋体"}[DTR]{lang="EN-US"}[和]{style="font-family:宋体"}[DSR]{lang="EN-US"}[请参考]{style="font-family:宋体"}**[detect]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[RTS]{lang="EN-US"}]{#struct_0_21171_18224_290122605}[（]{style="font-family:宋体"}[Request to Send]{lang="EN-US"}[）和]{style="font-family:宋体"}[CTS]{lang="EN-US"}[（]{style="font-family:宋体"}[Clear to Send]{lang="EN-US"}[）处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_21171_18224_1772711998}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_21171_18224_1910882321}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_21171_18224_1772515390}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_21171_18224_1852674619}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_21171_18224_1772580926}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_21171_18224_367801445}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_x1850278163}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_21171_18224_1772908606}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_21171_18224_x1197371641}

[[Link]{lang="EN-US"}]{#struct_0_21171_18224_1772974142}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_x106494385}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_776258518}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_1736201326}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_21171_18224_1772384315}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_21171_18224_1736266862}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_310052756}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_1772449851}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_188701657}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_1375858337}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_21171_18224_x1431597272}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_21171_18224_1772253243}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21171_18224_x1655526937}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_1772318779}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_21171_18224_1135513682}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_21171_18224_1772646459}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_21171_18224_x2037976989}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](WAN接口命令.files/image003.jpg){#图片 5 width="62" height="24"}]{lang="EN-US"}]{#struct_0_21171_18224_252751155}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[**[display interface serial]{lang="EN-US"}**]{#struct_0_21171_18224_x115434463}[命令的显示信息请以产品的实际情况和具体使用的板卡为准。]{lang="EN-US" style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_661366031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_1772711995}

::: {#-123085679 .myid}
[]{#_Toc404785082}[]{#struct_0_21171_18224_1910554641}[]{#_Toc324864447}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- eliminate-pulse**

------------------------------------------------------------------------

[**[eliminate-pulse]{lang="EN-US"}**]{#struct_0_21171_18224_x2076780822}[命令用来消除脉冲宽度小于]{style="font-family:宋体"}[3.472μs]{lang="EN-US"}[的脉冲。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **eliminate-pulse**]{lang="EN-US"}]{#struct_0_21171_18224_959474202}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2099212997}

[**[eliminate-pulse]{lang="EN-US"}**]{#struct_0_21171_18224_475891381}

[**[undo eliminate-pulse]{lang="EN-US"}**]{#struct_0_21171_18224_x1410354956}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1413476801}

[[消除脉冲宽度小于]{style="font-family:宋体"}[1.472μs]{lang="EN-US"}]{#struct_0_21171_18224_1772515387}[的脉冲。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1852740156}

[[异步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1006164811}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_1431910968}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1399133174}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1095632192}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1689999760}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x949372424}

[[同[/]{lang="EN-US"}异步串口只有通过命令]{style="font-family:宋体"}**[physical-mode async]{lang="EN-US"}**]{#struct_0_21171_18224_1772580923}[切换到异步模式后才能配置]{style="font-family:宋体"}**[eliminate-pulse]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[波特率等于]{style="font-family:宋体"}[115200bps]{lang="EN-US"}]{#struct_0_21171_18224_368129125}[时不能配置该命令；配置该命令后，波特率不能等于]{style="font-family:宋体"}[115200bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[本命令仅用于]{style="font-family:宋体"}[8ASE/16ASE]{lang="EN-US"}]{#struct_0_21171_18224_1162535749}[接口卡]{style="font-family:宋体"}[/]{lang="EN-US"}[模块。]{style="font-family:宋体"}

[[在线路干扰较大时可以配置本命令，增加信号的可靠性。]{style="font-family:宋体"}]{#struct_0_21171_18224_1378785836}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_2069598842}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1946919578}[配置异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[消除脉冲宽度小于]{style="font-family:宋体"}[3.472μs]{lang="EN-US"}[的脉冲。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1874943013}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\] eliminate-pulse]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x630282116}[配置]{style="font-family:宋体"}[同[/]{lang="EN-US"}异步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[消除脉冲宽度小于]{style="font-family:宋体"}[3.472μs]{lang="EN-US"}[的脉冲。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1772908603}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] eliminate-pulse]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1197043961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[physical-mode]{lang="EN-US"}**]{#struct_0_21171_18224_835271649}
:::

::: {#-2059163527 .myid}
[]{#_Toc261964947}[]{#_Toc205607554}[]{#_Toc404785083}[]{#struct_0_21171_18224_145720044}[]{#_Toc325038115}[]{#_Toc261964984}[]{#_Toc205607588}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- idle-code**

------------------------------------------------------------------------

[**[idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_727917911}[命令用来设置同步串口的线路空闲码类型]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_820118000}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_75382162}

[**[idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x85058720}[ { **7e** \| **ff** }]{lang="PT-BR"}

[**[undo idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_1772974139}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x107215284}

[[同步串口的线路空闲码类型为]{style="font-family:宋体"}]{#struct_0_21171_18224_1203189695}[0x7e]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x481018569}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x954753236}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1031378142}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x737363438}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x925018391}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x820665021}

[**[7e]{lang="PT-BR"}**]{#struct_0_21171_18224_1772384316}[：]{style="font-family:宋体"}[线路空闲码为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[类型。]{style="font-family:宋体"}

[**[ff]{lang="PT-BR"}**]{#struct_0_21171_18224_310118292}[：]{style="font-family:宋体"}[线路空闲码为]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x727502315}

[[通常情况下，同步串口使用]{style="font-family:宋体"}]{#struct_0_21171_18224_x1436816787}[0x7e]{lang="PT-BR"}[来表示线路的空闲状态，而有的设备在空闲时间采用]{style="font-family:宋体"}[0xff]{lang="EN-US"}[（即全"]{style="font-family:宋体"}[1]{lang="EN-US"}["的高电平）来表示线路的空闲状态。为了更好的兼容这种设备，需要设置同步串口的线路空闲码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_535513294}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_415443636}[设置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的线路空闲码为"]{style="font-family:宋体"}[0xFF]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1013426958}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] idle-code ff]{lang="EN-US"}
:::

::: {#665295680 .myid}
[]{#_Toc404785084}[]{#struct_0_21171_18224_1772449852}[]{#_Toc326766651}[]{#_Toc325028519}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- interface async**

------------------------------------------------------------------------

[**[interface ]{lang="EN-US"}[async]{lang="EN-US"}**]{#struct_0_21171_18224_x786687220}[命令用来进入]{style="font-family:宋体"}[异步串口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2124504326}

[**[interface ]{lang="EN-US"}[async ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_1345252237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x921150753}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1811415250}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2023383661}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_185697419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1498042759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1772253244}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1655592473}[：异步串口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1542479181}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_778321471}[进入异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1508429802}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\]]{lang="EN-US"}
:::

::: {#983854911 .myid}
[]{#_Toc404785085}[]{#struct_0_21171_18224_620207718}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- interface serial**

------------------------------------------------------------------------

[**[interface serial]{lang="EN-US"}**]{#struct_0_21171_18224_1509647422}[命令用来进入串口或串口子接口视图。在进入子接口视图之前，如果指定的子接口不存在，则先创建子接口，再进入该子接口的视图。]{style="font-family:宋体"}

[**[undo interface serial]{lang="EN-US"}**]{#struct_0_21171_18224_x14712458}[命令用来删除串口子接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1772318780}

[**[interface serial]{lang="EN-US"}**[ { *interface-number* \| *interface-number.subnumber* \[ **p2mp** \| **p2p** \] }]{lang="EN-US"}]{#struct_0_21171_18224_1135054921}

[**[undo interface serial]{lang="EN-US"}**[ *interface-number.subnumber*]{lang="EN-US"}]{#struct_0_21171_18224_x327728463}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x5790127}

[[不存在串口子接口。]{style="font-family:宋体"}]{#struct_0_21171_18224_121244916}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_837760220}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1923692420}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1838474030}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1685420944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1772646460}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2038566816}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_281146227}[：串口编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_21171_18224_1247678449}[：串口子接口编号，其中]{style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[p2mp]{lang="EN-US"}**]{#struct_0_21171_18224_x80746392}[：点到多点子接口。子接口缺省为]{style="font-family:宋体"}**[p2mp]{lang="EN-US"}**[类型。]{style="font-family:宋体"}

[**[p2p]{lang="EN-US"}**]{#struct_0_21171_18224_x2010678071}[：点到点子接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1715097851}

[[只有串口主接口上封装的链路层协议为]{style="font-family:宋体"}[FR]{lang="EN-US"}]{#struct_0_21171_18224_x1644463676}[时，才能创建子接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_678391903}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1772711996}[创建串口子接口]{style="font-family:宋体"}[Serial2/1/0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1910489105}

[\[Sysname\] interface serial 2/1/0.1]{lang="EN-US"}

[\[Sysname-Serial2/1/0.1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1027814622}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[link-protocol]{lang="EN-US"}**]{#struct_0_21171_18224_1580032110}
:::

::: {#-1456394328 .myid}
[]{#_Toc404785086}[]{#struct_0_21171_18224_x1607627204}[]{#_Toc261964948}[]{#_Toc205607555}[]{#_Toc275246602}[]{#_Toc275250570}[]{#_Toc275246604}[]{#_Toc275250572}[]{#_Toc275246605}[]{#_Toc275250573}[]{#_Toc275246606}[]{#_Toc275250574}[]{#_Toc275246607}[]{#_Toc275250575}[]{#_Toc275246608}[]{#_Toc275250576}[]{#_Toc275246609}[]{#_Toc275250577}[]{#_Toc275246610}[]{#_Toc275250578}[]{#_Toc275246611}[]{#_Toc275250579}[]{#_Toc275246612}[]{#_Toc275250580}[]{#_Toc275246613}[]{#_Toc275250581}[]{#_Toc275246614}[]{#_Toc275250582}[]{#_Toc275246615}[]{#_Toc275250583}[]{#_Toc275246616}[]{#_Toc275250584}[]{#_Toc275246617}[]{#_Toc275250585}[]{#_Toc275246619}[]{#_Toc275250587}[]{#_Toc275246620}[]{#_Toc275250588}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- invert receive-clock**

------------------------------------------------------------------------

[**[invert receive-clock]{lang="EN-US"}**]{#struct_0_21171_18224_x209188764}[命令用来允许翻转]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧同步串口的接收时钟信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**]{#struct_0_21171_18224_x884566607}[[ invert receive-clock]{lang="EN-US"}]{.commandkeywords}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_278867457}

[**[invert receive-clock]{lang="EN-US"}**]{#struct_0_21171_18224_1772515388}

[**[undo invert receive-clock]{lang="EN-US"}**]{#struct_0_21171_18224_1853198908}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1747531318}

[[同步串口作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_216816985}[侧时，禁止翻转接收时钟信号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x601221464}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1778607444}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_669547463}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x901247828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1772580924}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_367670373}

[[在某些特殊情况下，为了消除线路上半个时钟周期的时延，可以将]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_x2091867837}[侧同步串口的接收时钟信号翻转。只有某些特殊的]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备需要配置该命令，对于通常的应用，时钟不应作翻转。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1265532353}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1006617508}[将]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的接收时钟翻转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x945917333}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] invert receive-clock]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_2076363435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[invert transmit-clock]{lang="EN-US"}**]{#struct_0_21171_18224_1772908604}
:::

::: {#1316484371 .myid}
[]{#_Toc404785087}[]{#struct_0_21171_18224_88027829}[]{#_Toc261964949}[]{#_Toc205607556}[]{#_Toc371081774}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- invert transmit-clock**

------------------------------------------------------------------------

[**[invert transmit-clock]{lang="EN-US"}**]{#struct_0_21171_18224_x1017893955}[命令用来允许翻转]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧同步串口的发送时钟信号。]{style="font-family:宋体"}

[**[undo invert transmit-clock]{lang="EN-US"}**]{#struct_0_21171_18224_1553248129}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1223833048}

[**[invert transmit-clock]{lang="EN-US"}**]{#struct_0_21171_18224_790447809}

[**[undo invert transmit-clock]{lang="EN-US"}**]{#struct_0_21171_18224_628665935}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x836556665}

[[同步串口作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_1772974140}[侧时，禁止翻转发送时钟信号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x106625457}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1576548526}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1319465075}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_421808258}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1887041804}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1488157790}

[[在某些特殊情况下，为了消除线路上半个时钟周期的时延，可以将]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_x375270115}[侧同步串口的发送时钟信号翻转。只有某些特殊的]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备需要配置该命令，对于通常的应用，时钟不应作翻转。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956499036}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1070062905}[将]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的发送时钟翻转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x359241410}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] invert transmit-clock]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1458143925}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[invert receive-clock]{lang="EN-US"}]{.commandkeywords}]{#struct_0_21171_18224_x594763968}
:::

::: {#134624755 .myid}
[]{#_Toc404785088}[]{#struct_0_21171_18224_194870585}[]{#_Toc371081776}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- itf**

------------------------------------------------------------------------

[**[itf]{lang="PT-BR"}**]{#struct_0_21171_18224_x956433500}[命令用来设置帧间填充字节]{style="font-family:宋体"}[的个数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo itf]{lang="PT-BR"}**]{#struct_0_21171_18224_500864184}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_807438411}

[**[itf]{lang="PT-BR"}**]{#struct_0_21171_18224_795943260}[ **number** *number*]{lang="PT-BR"}

[**[undo itf number]{lang="PT-BR"}**]{#struct_0_21171_18224_1125130609}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1426404289}

[[帧间填充字节个数为]{style="font-family:宋体"}]{#struct_0_21171_18224_2042257656}[4]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1994461175}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_646703474}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x956630108}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x666570037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1006427867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1004338302}

[**[number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_21171_18224_546940559}[：设置帧间填充字节的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[14]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1839429046}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_979236576}[设置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧间填充字节个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x956564572}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] itf number 5]{lang="EN-US"}
:::

::: {#232606835 .myid}
[]{#_Toc404785089}[]{#struct_0_21171_18224_2056396801}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- link-protocol**

------------------------------------------------------------------------

[**[link-protocol]{lang="EN-US"}**]{#struct_0_21171_18224_255155275}[命令用来设置接口的链路层协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_897134465}

[**[link-protocol]{lang="EN-US"}**[ { **fr** \| **hdlc** \| **ppp** }]{lang="EN-US"}]{#struct_0_21171_18224_x1375985312}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1090908787}

[[同步串口使用]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_21171_18224_x1967243301}[作为链路层协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_718320264}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_2067166328}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x956236892}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_566310460}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1935938836}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_914798795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1321788475}

[**[fr]{lang="EN-US"}**]{#struct_0_21171_18224_x109906340}[：使用帧中继作为接口的链路层协议。]{style="font-family:宋体"}

[**[hdlc]{lang="EN-US"}**]{#struct_0_21171_18224_636672761}[：使用]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[作为接口的链路层协议。]{style="font-family:宋体"}

[**[ppp]{lang="EN-US"}**]{#struct_0_21171_18224_2120246652}[：使用]{style="font-family:宋体"}[PPP]{lang="EN-US"}[作为接口的链路层协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_938819044}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x956171356}[设置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的链路层协议为]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1274379624}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol hdlc]{lang="EN-US"}
:::

::: {#405613428 .myid}
[]{#_Toc404785090}[]{#struct_0_21171_18224_1890458553}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_728871756}[命令用来使能对内自环功能。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_142195442}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_883122251}

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x186050531}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_1395606535}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956367964}

[[对内自环功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_165790193}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_2106634063}

[[同步串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1923487207}[异步串口视图]{style="font-family:宋体"}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1188323688}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x527745902}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x133192791}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_500943679}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956302428}

[[只有在进行某些特殊功能测试时，才将接口设为对内自环。]{style="font-family:宋体"}]{#struct_0_21171_18224_885262580}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1332938927}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x456643845}[配置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x405498626}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] loopback]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1972934204}[配置异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1115421108}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\] loopback]{lang="EN-US"}
:::

::: {#988247972 .myid}
[]{#_Toc404785091}[]{#struct_0_21171_18224_566311922}[]{#_Toc261964951}[]{#_Toc205607558}[]{#_Toc13287745}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x955974748}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x1718869890}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2056733218}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_21171_18224_1923077899}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_545636156}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1087348635}

[[串口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_21171_18224_2083902144}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x440631186}

[[同步串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x955909212}[异步串口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[串口子接口视图]{style="font-family:宋体"}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x191356116}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1599009029}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1213492030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1127380965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x781022879}

[*[size]{lang="EN-US"}*]{#struct_0_21171_18224_x541107506}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x389625405}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_21171_18224_x462975949}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x956499035}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1070259513}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_510264091}[配置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_310055851}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] mtu 1430]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1161019558}[配置异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1555749998}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\] mtu 1430]{lang="EN-US"}
:::

::: {#1372817797 .myid}
[]{#_Toc261964953}[]{#_Toc205607560}[]{#_Toc404785092}[]{#struct_0_21171_18224_x607863285}[]{#_Toc324864449}[]{#_Toc275246638}[]{#_Toc275250606}[]{#_Toc275246640}[]{#_Toc275250608}[]{#_Toc275246641}[]{#_Toc275250609}[]{#_Toc275246642}[]{#_Toc275250610}[]{#_Toc275246643}[]{#_Toc275250611}[]{#_Toc275246644}[]{#_Toc275250612}[]{#_Toc275246645}[]{#_Toc275250613}[]{#_Toc275246646}[]{#_Toc275250614}[]{#_Toc275246647}[]{#_Toc275250615}[]{#_Toc275246648}[]{#_Toc275250616}[]{#_Toc275246649}[]{#_Toc275250617}[]{#_Toc275246650}[]{#_Toc275250618}[]{#_Toc275246651}[]{#_Toc275250619}[]{#_Toc275246652}[]{#_Toc275250620}[]{#_Toc275246654}[]{#_Toc275250622}[]{#_Toc275246655}[]{#_Toc275250623}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- phy-mru**

------------------------------------------------------------------------

[**[phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_x956433499}[命令用来配置异步串口在流模式下接收包的最大长度。]{style="font-family:宋体"}

[**[undo phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_x1837329217}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1742831099}

[**[phy-mru]{lang="EN-US"}**[ *mrusize*]{lang="EN-US"}]{#struct_0_21171_18224_1781262326}

[**[undo phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_x983986565}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1342296449}

[[异步串口在流模式下接收包的最大长度为]{style="font-family:宋体"}[1700]{lang="EN-US"}]{#struct_0_21171_18224_x2020214168}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x757173951}

[[异步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x956630107}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x667028789}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_224557951}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1572557034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_446135147}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1077982014}

[*[mrusize]{lang="EN-US"}*]{#struct_0_21171_18224_x1650320105}[：异步串口在流模式下接收包的最大长度，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[1700]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_882503824}

[**[phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_1726804549}[命令只有在异步流模式下能够成功配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956564571}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_2056331265}[设置异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[在流模式下接收包的最大长度为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1355373744}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\] async-mode flow]{lang="EN-US"}

[\[Sysname-Async2/4/0\] phy-mru 1500]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1184667962}[设置]{style="font-family:宋体"}[同[/]{lang="EN-US"}异步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[在流模式下接收包的最大长度为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_248356961}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] physical-mode async]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] async-mode flow]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] phy-mru 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1236286166}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[async-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x956236891}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[physical-mode]{lang="EN-US"}**]{#struct_0_21171_18224_566375996}
:::

::: {#1386823145 .myid}
[]{#_Toc404785093}[]{#struct_0_21171_18224_2038436659}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- physical-mode**

------------------------------------------------------------------------

[**[physical-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x439017499}[命令用来设置同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口的工作方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **physical-mode**]{lang="EN-US"}]{#struct_0_21171_18224_2012251093}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1713077296}

[**[physical-mode]{lang="EN-US"}**[ { **async** \| **sync** }]{lang="EN-US"}]{#struct_0_21171_18224_x2064102950}

[**[undo physical-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x1409084619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x526129517}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x956171355}[异步串口工作在同步（]{style="font-family:宋体"}[sync]{lang="EN-US"}[）方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1274445160}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x2063887790}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1071993516}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_301639804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1899798806}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1399671948}

[**[async]{lang="EN-US"}**]{#struct_0_21171_18224_1837394425}**[：]{style="font-family:宋体"}**[设置同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口工作在异步方式。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_21171_18224_x956367963}[：设置同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口工作在同步方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_165724657}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x938251853}[设置同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在异步方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_959278417}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] physical-mode async]{lang="EN-US"}[]{#_Toc102358846}
:::

::: {#2052875588 .myid}
[]{#_Toc404785094}[]{#struct_0_21171_18224_x860862248}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x127923462}[命令用来清除指定]{style="font-family:
宋体"}[Serial]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x613720184}

[**[reset counters interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[serial ]{lang="EN-US"}**[\[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_21171_18224_x952511801}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956302427}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_884934900}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_355432243}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x162778376}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1019247758}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1351255547}

[**[serial]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1567574985}[：指定]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1112066675}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_21171_18224_1592979040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_x955974747}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_x1718804354}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_110100841}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x382809919}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_810554672}[清除同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface serial 2/1/0]{lang="EN-US"}]{#struct_0_21171_18224_523708006}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1900348437}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}[serial]{lang="EN-US"}**]{#struct_0_21171_18224_x675100440}
:::

::: {#1261621385 .myid}
[]{#_Toc404785095}[]{#struct_0_21171_18224_x955909211}[]{#_Toc326766653}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x191159508}[命令用来清除指定异步串口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1978993711}

[**[reset counters interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[async ]{lang="EN-US"}**[\[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_21171_18224_1243457660}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x588907447}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1746641691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1372407753}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1907334769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_174323319}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956499038}

[**[async]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1070980409}[：指定异步串口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_115483105}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_21171_18224_2084745073}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[async]{lang="EN-US"}**]{#struct_0_21171_18224_x999968290}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[async]{lang="EN-US"}**]{#struct_0_21171_18224_1510638011}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有异步串口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[async]{lang="EN-US"}**]{#struct_0_21171_18224_617392571}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定异步串口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1604880903}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x956433502}[清除异步串口]{style="font-family:宋体"}[Async2/4/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface async 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_500733112}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1426818982}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}[async]{lang="EN-US"}**]{#struct_0_21171_18224_853727160}
:::

::: {#-887665568 .myid}
[]{#_Toc404785096}[]{#struct_0_21171_18224_1995029066}[]{#_Toc261964954}[]{#_Toc205607561}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- reverse-rts**

------------------------------------------------------------------------

[**[reverse-rts]{lang="EN-US"}**]{#struct_0_21171_18224_1837055808}[命令用来配置翻转]{style="font-family:宋体"}[RTS]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[**[undo reverse-rts]{lang="EN-US"}**]{#struct_0_21171_18224_x967913964}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x729710732}

[**[reverse-rts]{lang="EN-US"}**]{#struct_0_21171_18224_x2007826057}

[**[undo reverse-rts]{lang="EN-US"}**]{#struct_0_21171_18224_x956630110}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x667094326}

[[不翻转]{style="font-family:宋体"}[RTS]{lang="EN-US"}]{#struct_0_21171_18224_x646319411}[信号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1182127490}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x352807278}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1431387443}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x41604597}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1687891847}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956564574}

[[配置]{style="font-family:宋体"}**[reverse-rts]{lang="EN-US"}**]{#struct_0_21171_18224_2056527873}[命令后，本端发送数据时不允许对端发送数据。]{style="font-family:宋体"}

[[只在特定的调试需要时，才需要翻转]{style="font-family:宋体"}[RTS]{lang="EN-US"}]{#struct_0_21171_18224_602021632}[信号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1836247159}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_214808463}[设置同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[翻转]{style="font-family:宋体"}[RTS]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x956236894}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] reverse-rts]{lang="EN-US"}
:::

::::: {#-1726874890 .myid}
[]{#_Toc404785097}[]{#struct_0_21171_18224_566703676}[]{#_Toc261964956}[]{#_Toc212536117}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](WAN接口命令.files/image003.jpg){width="62" height="24"}]{lang="EN-US"}]{#struct_0_21171_18224_x227213721}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21171_18224_1020878469}
:::

**[ ]{lang="EN-US"}**

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_21171_18224_x1250633802}[命令用来开启串口子接口的速率统计功能。]{style="font-family:
宋体"}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_21171_18224_x952469901}[命令用来关闭串口子接口的速率统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x820305210}

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_21171_18224_x956171358}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_21171_18224_1274248552}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1252028300}

[[串口子接口的速率统计功能处于关闭状态]{style="font-family:宋体"}]{#struct_0_21171_18224_x1289014987}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1234432849}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_4373445}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1089109380}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1704369911}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x956367966}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_165921265}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_404962337}

[[开启本功能后可能需要耗费大量系统资源，请谨慎使用。]{style="font-family:宋体"}]{#struct_0_21171_18224_677624573}

[[支持该功能的串口子接口包括同步串口、同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1147505391}[异步串口、子通道串口，但不包括纯异步串口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2056381457}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1258163269}[开启]{style="font-family:宋体"}[同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[子接口速率统计功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1469630243}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] sub-interface rate-statistic]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956302430}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_884738293}[]{#_Toc261964957}[]{#_Toc205607563}
:::::

::::::: {#-1418618900 .myid}
[]{#_Toc404785098}[]{#struct_0_21171_18224_x978946937}[]{#_Toc261964958}[]{#_Toc205607564}

**WAN接口 \-- 同步串口、异步串口、同/异步串口配置命令 \-- virtualbaudrate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](WAN接口命令.files/image003.jpg){#图片 7 width="62" height="24"}]{lang="EN-US"}]{#struct_0_21171_18224_358203013}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_21171_18224_x176001298}
:::

**[ ]{lang="EN-US"}**

[**[virtualbaudrate]{lang="EN-US"}**]{#struct_0_21171_18224_x1841984265}[命令用来配置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[接口的虚拟波特率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **virtualbaudrate**]{lang="EN-US"}]{#struct_0_21171_18224_x1706650153}[命令用来取消虚拟波特率的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_345355377}

[**[virtualbaudrate ]{lang="EN-US"}***[virtualbaudrate]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_21171_18224_x585187550}

[**[undo virtualbaudrate]{lang="EN-US"}**]{#struct_0_21171_18224_x955974750}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1718345601}

[[同步串口的虚拟波特率为]{style="font-family:宋体"}[64000bps]{lang="EN-US"}]{#struct_0_21171_18224_433595001}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1446575822}

[[同步串口视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1716132512}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1219423110}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_870164175}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x403328538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x955909214}

[*[virtualbaudrate]{lang="EN-US"}*]{#struct_0_21171_18224_x190962900}[：指定的波特率，需要与]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧的配置保持一致。其取值范围为]{style="font-family:宋体"}[1200]{lang="EN-US"}[、]{style="font-family:宋体"}[2400]{lang="EN-US"}[、]{style="font-family:宋体"}[4800]{lang="EN-US"}[、]{style="font-family:宋体"}[9600]{lang="EN-US"}[、]{style="font-family:宋体"}[19200]{lang="EN-US"}[、]{style="font-family:宋体"}[38400]{lang="EN-US"}[、]{style="font-family:宋体"}[56000]{lang="EN-US"}[、]{style="font-family:宋体"}[57600]{lang="EN-US"}[、]{style="font-family:宋体"}[64000]{lang="EN-US"}[、]{style="font-family:宋体"}[72000]{lang="EN-US"}[、]{style="font-family:宋体"}[115200]{lang="EN-US"}[、]{style="font-family:宋体"}[128000]{lang="EN-US"}[、]{style="font-family:宋体"}[192000]{lang="EN-US"}[、]{style="font-family:宋体"}[256000]{lang="EN-US"}[、]{style="font-family:宋体"}[384000]{lang="EN-US"}[、]{style="font-family:宋体"}[512000]{lang="EN-US"}[、]{style="font-family:宋体"}[1024000]{lang="EN-US"}[、]{style="font-family:宋体"}[2048000]{lang="EN-US"}[、]{style="font-family:宋体"}[4096000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1549845164}

[[当串口工作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_21171_18224_587518632}[模式时，接口波特率通过协商从对端（]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧）获得。]{style="font-family:宋体"}**[virtualbaudrate]{lang="EN-US"}**[命令给用户提供一种手工配置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧波特率的方式。]{style="font-family:宋体"}

[[需要注意的是，如果接口时钟方式为]{style="font-family:宋体"}**[dteclk5]{lang="EN-US"}**]{#struct_0_21171_18224_x1015881852}[时钟模式，配置的虚拟波特率就是线路速率。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](WAN接口命令.files/image003.jpg){#图片 8 width="62" height="24"}]{lang="EN-US"}]{#struct_0_21171_18224_x128137334}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[baudrate]{lang="EN-US"}**]{#struct_0_21171_18224_x410481607}[和]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[virtualbaudrate]{lang="EN-US"}**[不能在链路的同一端配置，]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[baudrate]{lang="EN-US"}**[用于]{lang="EN-US" style="font-family:KaiTi_GB2312"}[DCE]{lang="EN-US"}[端，]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[virtualburdrate]{lang="EN-US"}**[用于]{lang="EN-US" style="font-family:KaiTi_GB2312"}[DTE]{lang="EN-US"}[端（仅同步模式）。]{lang="EN-US" style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[在]{lang="EN-US" style="font-family:KaiTi_GB2312"}[DCE]{lang="EN-US"}]{#struct_0_21171_18224_868048386}[端，通过]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[display interface]{lang="EN-US"}**[命令看到的是接口的]{lang="EN-US" style="font-family:
KaiTi_GB2312"}*[baudrate]{lang="EN-US"}*[；而在]{lang="EN-US" style="font-family:KaiTi_GB2312"}[DTE]{lang="EN-US"}[端，通过]{lang="EN-US" style="font-family:KaiTi_GB2312"}**[display interface]{lang="EN-US"}**[命令看到的是接口的]{lang="EN-US" style="font-family:KaiTi_GB2312"}*[virtualbaudrate]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956499037}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1070128441}[设置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备的同步串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的虚拟波特率为]{style="font-family:宋体"}[19200bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_829781739}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] virtualbaudrate 19200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_469297106}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[baudrate]{lang="EN-US"}**]{#struct_0_21171_18224_435408323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_377401916}
:::::::

::: {#-1342450891 .myid}
[]{#_Toc404785100}[]{#struct_0_21171_18224_x2076688600}[]{#_Toc326766300}

**WAN接口 \-- AM接口配置命令 \-- async-mode**

------------------------------------------------------------------------

[**[async-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x956433501}[命令用来设置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口的工作模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **async-mode**]{lang="EN-US"}]{#struct_0_21171_18224_500798648}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1419574029}

[**[async-mode]{lang="EN-US"}**[ { **flow** \| **protocol** }]{lang="EN-US"}]{#struct_0_21171_18224_690935532}

[**[undo async-mode]{lang="EN-US"}**]{#struct_0_21171_18224_721177803}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1750699953}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_x1996729080}[接口工作在流模式（]{style="font-family:宋体"}**[flow]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_804460066}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_x956630109}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x666635573}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1446942577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x128565625}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x383868058}

[**[flow]{lang="EN-US"}**]{#struct_0_21171_18224_x1939365743}[：流模式，也称交互模式。指物理连接建立之后，链路的两端进行交互，主叫端向接收端发送配置命令（与用户从远端手工键入配置命令效果相同），设置接收端的链路层协议工作参数，然后建立链路。一般用于拨号等人机交互的情况。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**]{#struct_0_21171_18224_200081565}[：协议模式。指物理连接建立之后，接口直接采用已有的链路层协议配置参数建立链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x933929619}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x171764938}[设置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[的工作模式为协议模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x956564573}

[\[Sysname\] interface analogmodem 2/4/0]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\] async-mode protocol]{lang="EN-US"}
:::

::: {#1270396608 .myid}
[]{#_Toc404785101}[]{#struct_0_21171_18224_2056462337}[]{#_Toc326766303}

**WAN接口 \-- AM接口配置命令 \-- display interface analogmodem**

------------------------------------------------------------------------

[**[display interface analogmodem]{lang="EN-US"}**]{#struct_0_21171_18224_x1752748063}[命令用来显示]{style="font-family:
宋体"}[AM]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x246245904}

[**[display interface]{lang="EN-US"}**[ \[ **analogmodem** \[ *interface-number* ]{lang="EN-US"}]{#struct_0_21171_18224_1900137297}[\] \] ]{lang="EN-US" style="font-size:10.0pt;
color:black"}[\[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1038974571}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_269636190}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x956236893}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_566244924}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_1207636754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1421669159}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_2114763736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x90334539}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1174980591}[：显示指定]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_21171_18224_x609556727}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_21171_18224_x956171357}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_21171_18224_x1309479225}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1274314088}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_21171_18224_x1667561586}**[analogmodem]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[analogmodem]{lang="EN-US"}**]{#struct_0_21171_18224_1055199912}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[AM]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x451455696}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x442979447}[显示]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface analogmodem 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_1108762427}

[Analogmodem2/4/0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Analogmodem2/4/0 Interface]{lang="EN-US"}

[Bandwidth: 57kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Physical layer: asynchronous, Baudrate: 57600 bps]{lang="EN-US"}

[Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Input:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 broadcasts, 0 multicasts]{lang="EN-US"}

[  0 errors, 0 runts, 0 giants]{lang="EN-US"}

[  0 crc, 0 align errors, 0 overruns]{lang="EN-US"}

[  0 aborts, 0 no buffers]{lang="EN-US"}

[  0 frame errors]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}

[  0 deferred]{lang="EN-US"}

[DCD: DOWN, DTR: UP, DSR: UP, RTS: UP, CTS: UP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_165855729}[显示]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface analogmodem 2/4/0 brief]{lang="EN-US"}]{#struct_0_21171_18224_x956302429}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[AM2/4/0              DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_885328116}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface analogmodem brief down]{lang="EN-US"}]{#struct_0_21171_18224_988990015}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[AM2/4/0              ADM  Administratively]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display interface analogmodem]{lang="EN-US"}]{#struct_0_21171_18224_x1940810136}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1872404070}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_x1030419200}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x421671828}

[[Analogmodem2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x955974749}

[[Current state]{lang="EN-US"}]{#struct_0_21171_18224_x1718935426}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_x186050219}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x1324858363}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x61974803}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x955909213}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_21171_18224_x191290580}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_759965051}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_1902919169}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_1139293240}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_1244432892}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x956499040}

[[Bandwidth]{lang="EN-US"}]{#struct_0_21171_18224_x1070456118}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_21171_18224_1478343704}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_21171_18224_661957061}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_21171_18224_2145380059}

[[Hold timer]{lang="EN-US"}]{#struct_0_21171_18224_x956433504}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_501126328}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_21171_18224_x847552712}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_x847552706}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_21171_18224_x1982949734}

[[网络层协议处理状况]{style="font-family:宋体"}]{#struct_0_21171_18224_474514469}

[[Link layer protocol: PPP]{lang="EN-US"}]{#struct_0_21171_18224_x956630112}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_21171_18224_x667225398}

[[LCP: initial]{lang="EN-US"}]{#struct_0_21171_18224_2105042849}

[[LCP]{lang="EN-US"}]{#struct_0_21171_18224_x2135871945}[（链路控制协议）初始化完成]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_392703544}

[[输出队列（紧急队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_392769080}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - Protocol queuing: Size/Length/Discards)]{lang="EN-US"}]{#struct_0_21171_18224_x1702089824}

[[输出队列（协议队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_393621048}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - FIFO queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_393686584}

[[输出队列（先进先出队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x724843482}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_x1586874959}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_x20791018}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_x1440484913}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x956564576}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Physical layer]{lang="EN-US"}]{#struct_0_21171_18224_2056658945}

[[物理层链路信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x2142585426}

[[Baudrate]{lang="EN-US"}]{#struct_0_21171_18224_x742249794}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_21171_18224_x956236896}

[[Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_54127243}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_x956171360}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_1274772837}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_x68084257}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input:]{lang="EN-US"}]{#struct_0_21171_18224_1997233206}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_x956367968}

[[  0 broadcasts, 0 multicasts]{lang="EN-US"}]{#struct_0_21171_18224_166052337}

[[  0 errors, 0 runts, 0 giants]{lang="EN-US"}]{#struct_0_21171_18224_x266424074}

[[  0 crc, 0 align errors, 0 overruns]{lang="EN-US"}]{#struct_0_21171_18224_x956302432}

[[  0 aborts, 0 no buffers]{lang="EN-US"}]{#struct_0_21171_18224_884607221}

[[  0 frame errors]{lang="EN-US"}]{#struct_0_21171_18224_x599428054}

[[接口收到的总报文数和总字节数：]{style="font-family:宋体"}]{#struct_0_21171_18224_356286801}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcasts]{lang="EN-US"}]{#struct_0_21171_18224_x955974752}[：接收的广播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_21171_18224_x1718476673}[：接收的组播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_1328939956}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[runts]{lang="EN-US"}]{#struct_0_21171_18224_x955909216}[：接口接收到小于规定的最小报文长度报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_21171_18224_x191093972}[：接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[crc]{lang="EN-US"}]{#struct_0_21171_18224_398706541}[：接收长度正常但]{style="font-family:宋体"}[CRC ]{lang="EN-US"}[校验错误的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[align errors]{lang="EN-US"}]{#struct_0_21171_18224_x956499039}[：排列错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_21171_18224_x1071045945}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_21171_18224_x239634025}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffers]{lang="EN-US"}]{#struct_0_21171_18224_x956433503}[：在接收报文时由于内部缓存满，导致帧丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[frame errors]{lang="EN-US"}]{#struct_0_21171_18224_500667576}[：帧错误]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_21171_18224_194140853}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_x956630111}

[[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}]{#struct_0_21171_18224_x667159862}

[[  0 deferred]{lang="EN-US"}]{#struct_0_21171_18224_x619777919}

[[接口发送的报文数和总字节数]{style="font-family:宋体"}]{#struct_0_21171_18224_150816601}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_x956564575}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_21171_18224_2056593409}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[collisions]{lang="EN-US"}]{#struct_0_21171_18224_2146417378}[：发送报文时，检测到冲突的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deferred]{lang="EN-US"}]{#struct_0_21171_18224_x956236895}[：因为延时或超时无法发送报文的数目]{style="font-family:宋体"}

[[DCD: DOWN, DTR: UP, DSR: UP, RTS: UP, CTS: UP]{lang="EN-US"}]{#struct_0_21171_18224_566638140}

[[DCD]{lang="EN-US"}]{#struct_0_21171_18224_x1839155323}[（]{style="font-family:宋体"}[Data Carrier Detect]{lang="EN-US"}[）信号处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，]{style="font-family:宋体"}[DTR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Terminal Ready]{lang="EN-US"}[）和]{style="font-family:宋体"}[DSR]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Set Ready]{lang="EN-US"}[）信号处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，]{style="font-family:宋体"}[RTS]{lang="EN-US"}[（]{style="font-family:宋体"}[Request to Send]{lang="EN-US"}[）和]{style="font-family:宋体"}[CTS]{lang="EN-US"}[（]{style="font-family:宋体"}[Clear to Send]{lang="EN-US"}[）处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_21171_18224_x956171359}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_21171_18224_1274183016}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_21171_18224_x956367967}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_21171_18224_165986801}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_21171_18224_x1977825055}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_21171_18224_x956302431}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_884803829}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_21171_18224_761659968}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_21171_18224_x955974751}

[[Link]{lang="EN-US"}]{#struct_0_21171_18224_x1718411137}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_x827758797}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x955909215}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x636058456}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_21171_18224_x190897364}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_21171_18224_x636517208}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_609584905}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_609650441}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x1353221629}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x930864985}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_21171_18224_x1353025021}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_21171_18224_x1386738482}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21171_18224_609453833}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_1148097928}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_21171_18224_x1128071983}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_21171_18224_609519369}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_21171_18224_1869339901}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1441061966}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_535065801}

::: {#783131296 .myid}
[]{#_Toc404785102}[]{#struct_0_21171_18224_609847049}[]{#_Toc326766304}

**WAN接口 \-- AM接口配置命令 \-- eliminate-pulse**

------------------------------------------------------------------------

[**[eliminate-pulse]{lang="EN-US"}**]{#struct_0_21171_18224_x359449939}[命令用来消除脉冲宽度小于]{style="font-family:宋体"}[3.472μs]{lang="EN-US"}[的脉冲，增加信号的可靠性。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **eliminate-pulse**]{lang="EN-US"}]{#struct_0_21171_18224_x1147002169}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x748240699}

[**[eliminate-pulse]{lang="EN-US"}**]{#struct_0_21171_18224_x1501753180}

[**[undo eliminate-pulse]{lang="EN-US"}**]{#struct_0_21171_18224_1925890801}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x732613928}

[[消除脉冲宽度小于]{style="font-family:宋体"}[1.472μs]{lang="EN-US"}]{#struct_0_21171_18224_609912585}[的脉冲。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1973184357}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_1377970686}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2280472}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1350348284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x176371196}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_103779724}

[[波特率等于]{style="font-family:宋体"}[115200bps]{lang="EN-US"}]{#struct_0_21171_18224_2066200301}[时不能配置该命令，同时配置该命令后，波特率不能等于]{style="font-family:宋体"}[115200bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[本命令仅用于]{style="font-family:宋体"}[8ASE/16ASE]{lang="EN-US"}]{#struct_0_21171_18224_2131838729}[接口卡]{style="font-family:宋体"}[/]{lang="EN-US"}[模块。]{style="font-family:宋体"}

[[在线路干扰较大时可以配置本命令。]{style="font-family:宋体"}]{#struct_0_21171_18224_609715977}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1680334507}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1358708362}[配置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[消除脉冲宽度小于]{style="font-family:宋体"}[3.472μs]{lang="EN-US"}[的脉冲。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_226104378}

[\[Sysname\] interface analogmodem 2/4/0]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\] eliminate-pulse]{lang="EN-US"}
:::

::: {#-219841602 .myid}
[]{#_Toc404785103}[]{#struct_0_21171_18224_407741716}[]{#_Toc326766305}[]{#_Toc309998809}[]{#_Toc309919901}

**WAN接口 \-- AM接口配置命令 \-- interface analogmodem**

------------------------------------------------------------------------

[**[interface analogmodem]{lang="EN-US"}**]{#struct_0_21171_18224_x81238127}[命令用来进入]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x804364888}

[**[interface analogmodem]{lang="EN-US"}**[ { *interface-number* \| *interface-number:***15** }]{lang="EN-US"}]{#struct_0_21171_18224_1270399861}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_609781513}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x2137810428}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x848532758}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_818161662}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x936805903}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1614912528}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1490085175}[：]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[*[interface-number:]{lang="EN-US"}***[15]{lang="EN-US"}**]{#struct_0_21171_18224_1142073932}[：由]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口生成的]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_681972451}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_610109193}[进入]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[的接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1132954877}

[\[Sysname\] interface analogmodem 2/4/0]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1312476988}[进入]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0:15]{lang="EN-US"}[的接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1651642913}

[\[Sysname\] interface analogmodem 2/4/0:15]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0:15\]]{lang="EN-US"}
:::

::: {#-951370423 .myid}
[]{#_Toc404785104}[]{#struct_0_21171_18224_x1618662340}[]{#_Toc326766306}

**WAN接口 \-- AM接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_697021756}[命令用来使能对内自环功能。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1763287479}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1187301389}

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_1651032263}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x228312096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_610174729}

[[对内自环功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_x3972314}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_993186507}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_785181865}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1452519790}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x242199372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_506604089}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2130230577}

[[只有在进行某些特殊功能测试时，才将接口设为对内自环。]{style="font-family:宋体"}]{#struct_0_21171_18224_1828006319}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_609584906}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1535386299}[配置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_495987710}

[\[Sysname\] interface analogmodem 2/4/0]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\] loopback]{lang="EN-US"}
:::

::: {#-1496619941 .myid}
[]{#_Toc404785105}[]{#struct_0_21171_18224_x1599349143}[]{#_Toc326766307}

**WAN接口 \-- AM接口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x1457049479}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_2050370112}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1777592340}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_21171_18224_609650442}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x1386738483}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1963107968}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_239727937}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1259523470}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_1785737787}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1085068521}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1385091740}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_196537361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_609453834}

[*[size]{lang="EN-US"}*]{#struct_0_21171_18224_1148097927}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1128268591}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_21171_18224_x826528706}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_14001681}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1738455302}[设置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1871590001}

[\[Sysname\] interface analogmodem 2/4/0]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\] mtu 1430]{lang="EN-US"}
:::

::: {#-1759151347 .myid}
[]{#_Toc404785106}[]{#struct_0_21171_18224_1249885723}[]{#_Toc326766308}

**WAN接口 \-- AM接口配置命令 \-- phy-mru**

------------------------------------------------------------------------

[**[phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_609519370}[命令用来配置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口在流模式下接收包的最大长度。]{style="font-family:宋体"}

[**[undo phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_x469312266}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_2051017247}

[**[phy-mru]{lang="EN-US"}**[ *mrusize*]{lang="EN-US"}]{#struct_0_21171_18224_x564205481}

[**[undo phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_172124064}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1075891163}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_995173330}[接口在流模式下接收包的最大长度为]{style="font-family:宋体"}[1700]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x284171033}

[[AM]{lang="EN-US"}]{#struct_0_21171_18224_609847050}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1979202212}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x367321474}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1802016133}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x569176799}

[*[mrusize]{lang="EN-US"}*]{#struct_0_21171_18224_1071176793}[：]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口在流模式下接收包的最大长度，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[1700]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1447882883}

[**[phy-mru]{lang="EN-US"}**]{#struct_0_21171_18224_534534560}[命令只有在异步流模式下能够成功配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1412748580}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_609912586}[设置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[在流模式下接收包的最大长度为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1973184358}

[\[Sysname\] interface analogmodem 2/4/0]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\] async-mode flow]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\] phy-mru 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x638451949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[async-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x1700303365}
:::

::: {#25937965 .myid}
[]{#_Toc404785107}[]{#struct_0_21171_18224_x1945013092}[]{#_Toc326766309}

**WAN接口 \-- AM接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_1445978162}[命令用来清除指定]{style="font-family:
宋体"}[AM]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2056263799}

[**[reset counters interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[analogmodem ]{lang="EN-US"}**[\[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_21171_18224_609715978}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1680334500}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x599193475}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_324650957}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1440830763}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x210353452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_243561584}

[**[analogmodem]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x779566631}[：指定]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_250854914}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_21171_18224_609781514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[analogmodem]{lang="EN-US"}**]{#struct_0_21171_18224_x2137810435}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[analogmodem]{lang="EN-US"}**]{#struct_0_21171_18224_x1964343541}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[AM]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[analogmodem]{lang="EN-US"}**]{#struct_0_21171_18224_712225381}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[AM]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1578596328}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1945366535}[清除]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口]{style="font-family:宋体"}[Analogmodem2/4/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface analogmodem 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x276264870}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1364055106}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}[analogmodem]{lang="EN-US"}**]{#struct_0_21171_18224_610109194}
:::

::: {#-1955601555 .myid}
[]{#_Toc404785109}[]{#struct_0_21171_18224_x52381791}[]{#_Toc326826699}[]{#_Toc323804934}

**WAN接口 \-- FCM接口配置命令 \-- display interface fcm**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[fcm]{lang="EN-US"}**]{#struct_0_21171_18224_1716489537}[命令用来显示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口]{style="font-family:宋体"}[的相关信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1671771360}

[**[display interface]{lang="EN-US"}**[ \[ **fcm** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_21171_18224_1354980961}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1168974828}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x650959601}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_610174730}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1952342831}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_x1951319039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x2033435914}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_290318996}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_29569141}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_616579710}[：显示指定]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_21171_18224_x721590915}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_21171_18224_609584903}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_21171_18224_256539179}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1535386304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_21171_18224_x1842467833}**[fcm]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_21171_18224_x1807036746}**[fcm]{lang="EN-US"}**[参数，不指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x784136852}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1529228695}[显示接口]{style="font-family:宋体"}[FCM2/4/0:15]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface fcm 2/4/0:15]{lang="EN-US"}]{#struct_0_21171_18224_x1232052422}

[Fcm2/4/0:15]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Fcm2/4/0:15 Interface]{lang="EN-US"}

[Bandwidth: 9kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Input:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 broadcasts, 0 multicasts]{lang="EN-US"}

[  0 errors, 0 runts, 0 giants]{lang="EN-US"}

[  0 CRC, 0 align errors, 0 overruns]{lang="EN-US"}

[  0 frame errors, 0 aborts, 0 no buffers]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}

[  0 deferred]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_569576646}[显示接口]{style="font-family:宋体"}[FCM2/4/0:15]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface fcm 2/4/0:15 brief]{lang="EN-US"}]{#struct_0_21171_18224_1846423943}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface           Link    Protocol   Main IP         Description]{lang="EN-US"}

[Fcm2/4/0:15         DOWN    DOWN       \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1735143757}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface fcm brief down]{lang="EN-US"}]{#struct_0_21171_18224_609453831}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface          Link    Cause]{lang="EN-US"}

[Fcm2/4/0:15        ADM     Administratively]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display interface fcm]{lang="EN-US"}]{#struct_0_21171_18224_1148097930}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1862584574}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_x1128596272}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x1070993529}

[[Fcm2/4/0:15 ]{lang="EN-US"}]{#struct_0_21171_18224_2063165285}

[[Current state]{lang="EN-US"}]{#struct_0_21171_18224_23236089}

[[接口当前的物理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_609519367}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_1869339895}[：该接口的物理状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_897852331}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，需要通过]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_21171_18224_1996341989}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1819810771}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_2106946417}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_609847047}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_x359449941}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x1146477878}

[[Bandwidth]{lang="EN-US"}]{#struct_0_21171_18224_x1447003381}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_21171_18224_358500234}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_21171_18224_609912583}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_21171_18224_x1973184363}

[[Hold timer]{lang="EN-US"}]{#struct_0_21171_18224_x591201174}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_x1466322718}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_21171_18224_341925690}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_341925694}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_21171_18224_1290959887}

[[网络层协议处理状况]{style="font-family:宋体"}]{#struct_0_21171_18224_609715975}

[[Link layer protocol: PPP]{lang="EN-US"}]{#struct_0_21171_18224_x1680334505}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_21171_18224_x195908948}

[[LCP: initial]{lang="EN-US"}]{#struct_0_21171_18224_197755310}

[[LCP]{lang="EN-US"}]{#struct_0_21171_18224_x2127845121}[（链路控制协议）初始化完成]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_x20659946}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_x348321096}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_1901654355}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_1798018370}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_609781511}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_x2137810430}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_x1204828654}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_21171_18224_1989644209}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input:]{lang="EN-US"}]{#struct_0_21171_18224_1885479711}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_x1353483772}

[[  0 broadcasts, 0 multicasts]{lang="EN-US"}]{#struct_0_21171_18224_x2126312109}

[[  0 errors, 0 runts, 0 giants]{lang="EN-US"}]{#struct_0_21171_18224_366802545}

[[  0 CRC, 0 align errors, 0 overruns]{lang="EN-US"}]{#struct_0_21171_18224_x1353287164}

[[  0 frame errors, 0 aborts, 0 no buffers]{lang="EN-US"}]{#struct_0_21171_18224_x1485900157}

[[接口收到的总报文数和总字节数：]{style="font-family:宋体"}]{#struct_0_21171_18224_610174727}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcasts]{lang="EN-US"}]{#struct_0_21171_18224_x1353352700}[：接收的广播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_21171_18224_x1352631804}[：接收的组播报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_x1127863556}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[runts]{lang="EN-US"}]{#struct_0_21171_18224_x1560644890}[：接口接收到小于规定的最小报文长度报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_21171_18224_x1352697340}[：接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CRC]{lang="EN-US"}]{#struct_0_21171_18224_2061497623}[：接收长度正常但]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[align errors]{lang="EN-US"}]{#struct_0_21171_18224_912422926}[：排列错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_21171_18224_x1353156091}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[frame errors]{lang="EN-US"}]{#struct_0_21171_18224_x817455726}[：帧错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_21171_18224_x1353221627}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffers]{lang="EN-US"}]{#struct_0_21171_18224_588164789}[：在接收报文时由于内部缓存满，导致帧丢弃]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_21171_18224_x3972308}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_x1353025019}

[[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}]{#struct_0_21171_18224_x1353090555}

[[  0 deferred]{lang="EN-US"}]{#struct_0_21171_18224_x800113561}

[[接口发送的报文数和总字节数]{style="font-family:宋体"}]{#struct_0_21171_18224_1721124710}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_x1353418235}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_21171_18224_x1478782996}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[collisions]{lang="EN-US"}]{#struct_0_21171_18224_x1353483771}[：发送报文时，检测到冲突的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deferred]{lang="EN-US"}]{#struct_0_21171_18224_x1723027582}[：因为延时或超时无法发送报文的数目]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_21171_18224_x1437703853}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_21171_18224_609584904}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_21171_18224_1535386297}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_21171_18224_496118782}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21171_18224_90664615}[Link]{lang="EN-US"}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_21171_18224_609650440}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_x1386738481}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_21171_18224_1169059914}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_21171_18224_609453832}

[[Link]{lang="EN-US"}]{#struct_0_21171_18224_1148097929}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1128137519}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_975038137}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_929959951}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_21171_18224_609519368}[：表示]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开]{style="font-family:宋体"}[接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_1869339902}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_x359449940}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x1353418234}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_87300945}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_21171_18224_x1353483770}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_21171_18224_x1146543414}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21171_18224_2073467340}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_609912584}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_21171_18224_x1973184356}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_21171_18224_x188113255}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_21171_18224_609715976}[的原因，]{style="font-family:宋体"}[取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1680334506}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_207375579}[]{#_Toc317856914}[]{#_Toc309228572}

::: {#2124399931 .myid}
[]{#_Toc404785110}[]{#struct_0_21171_18224_x1405909457}[]{#_Toc326826700}[]{#_Toc325029185}

**WAN接口 \-- FCM接口配置命令 \-- interface fcm**

------------------------------------------------------------------------

[**[interface fcm]{lang="EN-US"}**]{#struct_0_21171_18224_x161283349}[命令用来进入]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1100447343}

[**[interface fcm]{lang="EN-US"}**[ { *interface-number* \| *interface-number:***15** }]{lang="EN-US"}]{#struct_0_21171_18224_789086515}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_609781512}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x2137810429}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_717551183}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1052747334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1251406966}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_785909108}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_168466168}[：物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[*[interface-number:]{lang="EN-US"}***[15]{lang="EN-US"}**]{#struct_0_21171_18224_942205906}[：由]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口生成的]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1560559709}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1678320363}[进入]{style="font-family:宋体"}[FCM2/4/0]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1449773781}

[\[Sysname\] interface fcm 2/4/0]{lang="EN-US"}

[\[Sysname-Fcm2/4/0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_772354003}[进入]{style="font-family:宋体"}[FCM2/4/0:15]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x425780781}

[\[Sysname\] interface fcm 2/4/0:15]{lang="EN-US"}

[\[Sysname-Fcm2/4/0:15\]]{lang="EN-US"}
:::

::: {#1766416286 .myid}
[]{#_Toc404785111}[]{#struct_0_21171_18224_610174728}[]{#_Toc326826701}

**WAN接口 \-- FCM接口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x3972313}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x963128629}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x23954457}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_21171_18224_1373114379}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_209520471}

[[【缺省情况】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1468145239}

[[FCM]{lang="EN-US"}]{#struct_0_21171_18224_108763827}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1442721199}

[[FCM]{lang="EN-US"}]{#struct_0_21171_18224_609584901}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1535386302}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1842336761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1767087502}

[[【参数】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1951075991}

[*[size]{lang="EN-US"}*]{#struct_0_21171_18224_x694395811}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1470268339}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_21171_18224_1229885550}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x1502423798}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_609650437}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_569576648}[设置接口]{style="font-family:宋体"}[FCM2/4/0:15]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1846423933}

[\[Sysname\] interface fcm 2/4/0:15]{lang="EN-US"}

[\[Sysname-Fcm2/4/0:15\] mtu 1430]{lang="EN-US"}
:::

::: {#1343495305 .myid}
[]{#_Toc404785112}[]{#struct_0_21171_18224_x1735143752}[]{#_Toc326826706}

**WAN接口 \-- FCM接口配置命令 \-- pcm**

------------------------------------------------------------------------

[**[pcm]{lang="EN-US"}**]{#struct_0_21171_18224_x1157589386}[命令用来设置]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[对数压扩律。]{style="font-family:宋体"}

[**[undo pcm]{lang="EN-US"}**]{#struct_0_21171_18224_x402153435}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_244677699}

[**[pcm]{lang="EN-US"}**[ { **a-law** \| **u-law** }]{lang="EN-US"}]{#struct_0_21171_18224_609453829}

[**[undo pcm]{lang="EN-US"}**]{#struct_0_21171_18224_x1190554238}

[[【缺省情况】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1395540005}

[[FCM]{lang="EN-US"}]{#struct_0_21171_18224_x6727670}[接口的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[为]{style="font-family:宋体"}**[a-law]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_523791052}

[[FCM]{lang="EN-US"}]{#struct_0_21171_18224_x1183513842}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1320177968}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1317377890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1546861346}

[[【参数】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_609519365}

[**[a-law]{lang="EN-US"}**]{#struct_0_21171_18224_1869339897}[：对数压扩律]{style="font-family:宋体"}[A]{lang="EN-US"}[律，中国、欧洲、非洲和南美等国家使用。]{style="font-family:宋体"}

[**[µ-law]{lang="EN-US"}**]{#struct_0_21171_18224_897721259}[：对数压扩律]{style="font-family:宋体"}[µ]{lang="EN-US"}[律，美国使用。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x154978287}

[[为了减少噪声，提高信噪比，保证语音质量，实际应用中一般使用对数压扩律对信号进行非均匀量化。]{style="font-family:宋体"}]{#struct_0_21171_18224_482383822}

[[根据]{style="font-family:宋体"}[CCITT]{lang="EN-US"}]{#struct_0_21171_18224_694338123}[规定，使用]{style="font-family:宋体"}[µ]{lang="EN-US"}[律压扩的国家负责将信号转换为]{style="font-family:宋体"}[A]{lang="EN-US"}[律。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1700619702}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_280823800}[设置接口]{style="font-family:宋体"}[FCM2/4/0:15]{lang="EN-US"}[脉冲编码调制的对数压扩率为μ律。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_609847045}

[\[Sysname\] interface fcm2/4/0:15]{lang="EN-US"}

[\[Sysname-Fcm2/4/0:15\] pcm u-law]{lang="EN-US"}
:::

::: {#-759680570 .myid}
[]{#_Toc404785113}[]{#struct_0_21171_18224_x359449943}[]{#_Toc326826702}[]{#_Toc323804933}

**WAN接口 \-- FCM接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x1146346806}[命令用来清除]{style="font-family:
宋体"}[FCM]{lang="EN-US"}[接口]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_522039450}

[**[reset counters interface]{lang="EN-US"}**[ \[ **fcm** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_21171_18224_x1740418925}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1663389433}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1950014546}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1042632917}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_609912581}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1973184361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_571598240}

[**[fcm]{lang="EN-US"}**]{#struct_0_21171_18224_1056115171}[：清除]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1720590866}[：]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口]{style="font-family:宋体"}[的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1260479865}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_21171_18224_1226242230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[fcm]{lang="EN-US"}**]{#struct_0_21171_18224_1369316693}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[fcm]{lang="EN-US"}**]{#struct_0_21171_18224_x754970742}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[FCM]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[fcm]{lang="EN-US"}**]{#struct_0_21171_18224_609715973}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[FCM]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1680334511}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_2129624344}[清除]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[FCM2/4/0:15]{lang="EN-US"}[的统]{style="font-family:宋体"}[计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface fcm 2/4/0:15]{lang="EN-US"}]{#struct_0_21171_18224_1164989753}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x285334931}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}[fcm]{lang="EN-US"}**]{#struct_0_21171_18224_1645549304}
:::

::: {#1797341627 .myid}
[]{#_Toc404785115}[]{#struct_0_21171_18224_426367958}[]{#_Toc330384039}

**WAN接口 \-- ISDN BRI接口配置命令 \-- activate**

------------------------------------------------------------------------

[**[activate]{lang="EN-US"}**]{#struct_0_21171_18224_609781509}[命令用来激活]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_200841722}

[**[activate]{lang="EN-US"}**]{#struct_0_21171_18224_69367232}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x297699059}

[[BRI]{lang="EN-US"}]{#struct_0_21171_18224_1653476599}[接口处于未激活状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_60516595}

[[ISDN BRI]{lang="SV"}]{#struct_0_21171_18224_x605797210}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_307711828}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_610109189}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1205697289}

[[【使用指导】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_591692161}

[[BRI]{lang="EN-US"}]{#struct_0_21171_18224_273120896}[接口不存在呼叫时，]{style="font-family:宋体"}[ISDN BRI]{lang="EN-US"}[接口处于未激活状态，本命令用来手工激活]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1402252589}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x145802514}[手工激活]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1558128795}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] activate]{lang="EN-US"}
:::

::: {#-706277115 .myid}
[]{#_Toc404785116}[]{#struct_0_21171_18224_610174725}[]{#_Toc330384042}

**WAN接口 \-- ISDN BRI接口配置命令 \-- display interface bri**

------------------------------------------------------------------------

[**[display interface bri]{lang="EN-US"}**]{#struct_0_21171_18224_x3972310}[命令用来显示]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[的相关信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1757860555}

[**[display interface]{lang="EN-US"}**[ \[ **bri** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_21171_18224_x732620561}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1675682518}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_367599099}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1211575156}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1348115888}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_609584902}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1535386303}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_x1842271225}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1290813073}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_151337201}[：显示指定]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_21171_18224_159915024}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_21171_18224_2058478544}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_21171_18224_1822426511}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_609650438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_21171_18224_569576647}**[bri]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}**[bri]{lang="EN-US"}**]{#struct_0_21171_18224_1846423942}[参数，不指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1735078221}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1225136603}[显示]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface bri 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_350576447}

[Bri2/4/0]{lang="EN-US"}

[Current state: DOWN ( Administratively )]{lang="EN-US"}

[Line protocol state: UP (spoofing)]{lang="EN-US"}

[Description: Bri2/4/0 Interface]{lang="EN-US"}

[Bandwidth: 128kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Baudrate: 128000 bps ]{lang="EN-US"}

[Timeslot(s) Used: 1, 2]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 5 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Last 5 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}

[Input:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 runts, 0 giants,]{lang="EN-US"}

[  0 crc, 0 align errors, 0 overruns,]{lang="EN-US"}

[  0 aborts, 0 no buffers]{lang="EN-US"}

[  0 frame errors]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}

[  0 deferred]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1148097931}[显示]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface bri 2/4/0 brief]{lang="EN-US"}]{#struct_0_21171_18224_609519366}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Bri2/4/0             ADM  UP(s)    \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1869339896}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface bri brief down]{lang="EN-US"}]{#struct_0_21171_18224_897655723}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface              Link Cause]{lang="EN-US"}

[Bri2/4/0               ADM  Administratively]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display interface bri]{lang="EN-US"}]{#struct_0_21171_18224_2134742355}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1620699714}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_x382733900}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x6238094}

[[Bri2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_609847046}

[[Current state]{lang="EN-US"}]{#struct_0_21171_18224_x359449942}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1146412342}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_311406440}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x127873265}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x246849621}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_21171_18224_609912582}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1973184362}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_2137682181}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_660664842}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_956082712}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_21171_18224_609715974}

[[Bandwidth]{lang="EN-US"}]{#struct_0_21171_18224_x1680334504}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_21171_18224_1370174993}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_21171_18224_x1603008691}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_21171_18224_75388351}

[[Hold timer]{lang="EN-US"}]{#struct_0_21171_18224_609781510}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_x2137810431}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_21171_18224_1126063926}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_21171_18224_361389878}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Baudrate]{lang="EN-US"}]{#struct_0_21171_18224_361255287}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_21171_18224_x2086399022}

[[Timeslot(s) Used]{lang="EN-US"}]{#struct_0_21171_18224_610109190}

[[使用的时隙]{style="font-family:宋体"}]{#struct_0_21171_18224_x1132954880}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_21171_18224_1916986677}

[[网络层协议处理状况]{style="font-family:宋体"}]{#struct_0_21171_18224_x120132297}

[[Link layer protocol: PPP]{lang="EN-US"}]{#struct_0_21171_18224_610174726}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_21171_18224_x3972307}

[[LCP: initial]{lang="EN-US"}]{#struct_0_21171_18224_1001080678}

[[LCP]{lang="EN-US"}]{#struct_0_21171_18224_x160554001}[（链路控制协议）初始化完成]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_x1763068090}

[[输出队列（紧急队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_1192505740}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - Protocol queuing: Size/Length/Discards)]{lang="EN-US"}]{#struct_0_21171_18224_628798935}

[[输出队列（协议队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1210373542}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Output queue - FIFO queuing: Size/Length/Discards]{lang="EN-US"}]{#struct_0_21171_18224_x1763002554}

[[输出队列（先进先出队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1604029149}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数）]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_x20528874}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_1901785427}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_536570514}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_1959246238}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 5 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_x696336073}

[[最近]{style="font-family:宋体"}]{#struct_0_21171_18224_558173970}[5]{lang="EN-US"}[秒钟]{style="font-family:宋体"}[的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 5 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec]{lang="EN-US"}]{#struct_0_21171_18224_x1763199162}

[[最近]{style="font-family:宋体"}]{#struct_0_21171_18224_x1386541138}[5]{lang="EN-US"}[秒钟]{style="font-family:宋体"}[的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input:]{lang="EN-US"}]{#struct_0_21171_18224_x1252377839}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_x2131136452}

[[  0 errors, 0 runts, 0 giants,]{lang="EN-US"}]{#struct_0_21171_18224_x1763133626}

[[  0 crc, 0 align errors, 0 overruns,]{lang="EN-US"}]{#struct_0_21171_18224_x198591831}

[[  0 aborts, 0 no buffers]{lang="EN-US"}]{#struct_0_21171_18224_x1013862038}

[[  0 frame errors]{lang="EN-US"}]{#struct_0_21171_18224_x1762805946}

[[接口收到的总报文数和总字节数：]{style="font-family:宋体"}]{#struct_0_21171_18224_x860266998}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_x905651141}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[runts]{lang="EN-US"}]{#struct_0_21171_18224_1445422659}[：接口接收到小于规定的最小报文长度报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[giants]{lang="EN-US"}]{#struct_0_21171_18224_x1762740410}[：接收到长度大于规定长度的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[crc]{lang="EN-US"}]{#struct_0_21171_18224_393421137}[：接收长度正常但]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[align errors]{lang="EN-US"}]{#struct_0_21171_18224_525834169}[：排列错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overruns]{lang="EN-US"}]{#struct_0_21171_18224_x1762937018}[：接收的报文速度大于转发处理能力导致无法处理的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aborts]{lang="EN-US"}]{#struct_0_21171_18224_x1914449620}[：接收报文的异常错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no buffers]{lang="EN-US"}]{#struct_0_21171_18224_1673900648}[：在接收报文时由于内部缓存满，导致帧丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[frame errors]{lang="EN-US"}]{#struct_0_21171_18224_917976035}[：帧错误]{style="font-family:宋体"}

[[Output:]{lang="EN-US"}]{#struct_0_21171_18224_x1762871482}

[[  0 packets, 0 bytes]{lang="EN-US"}]{#struct_0_21171_18224_394664278}

[[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}]{#struct_0_21171_18224_x1998695848}

[[  0 deferred]{lang="EN-US"}]{#struct_0_21171_18224_x1762543802}

[[接口发送的报文数和总字节数]{style="font-family:宋体"}]{#struct_0_21171_18224_1150290563}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_21171_18224_1534469461}[：在物理层检测时发现的错误报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[underruns]{lang="EN-US"}]{#struct_0_21171_18224_x1762478266}[：因为接口读取内存的速度小于转发的速度而无法发送报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[collisions]{lang="EN-US"}]{#struct_0_21171_18224_x361960508}[：发送报文时，检测到冲突的报文数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deferred]{lang="EN-US"}]{#struct_0_21171_18224_234496425}[：因为延时或超时无法发送报文的数目]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_21171_18224_x1763068089}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x1180212791}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_21171_18224_x763867023}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_21171_18224_x1763002553}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21171_18224_x844514262}[Link]{lang="EN-US"}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_21171_18224_1514421957}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_x1763199161}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_21171_18224_179542803}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_21171_18224_x664358061}

[[Link]{lang="EN-US"}]{#struct_0_21171_18224_x1763133625}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_x601876358}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x1762805945}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_930353164}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_21171_18224_x456982471}[：表示]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开]{style="font-family:宋体"}[接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_21171_18224_930418700}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_21171_18224_289933747}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1762937017}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_21171_18224_x1353418232}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_21171_18224_x1075498469}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_21171_18224_x1353483768}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_21171_18224_1977233149}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21171_18224_x2113361432}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_x1762871481}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_21171_18224_x8620249}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_21171_18224_x1762543801}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_21171_18224_1553575090}[的原因，]{style="font-family:宋体"}[取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2499219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x1706711247}

::: {#518845131 .myid}
[]{#_Toc324413657}[]{#_Toc263323273}[]{#_Toc252280802}[]{#_Toc404785117}[]{#struct_0_21171_18224_x1200199952}[]{#_Toc330384043}

**WAN接口 \-- ISDN BRI接口配置命令 \-- interface bri**

------------------------------------------------------------------------

[**[interface bri]{lang="EN-US"}**]{#struct_0_21171_18224_x1762478265}[命令用来进入]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x765245035}

[**[interface bri ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_40331175}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x45111575}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1505864444}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x913115823}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_165425129}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1492627632}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1342426371}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1763068092}[：]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_29706326}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x466219487}[进入]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x2033782691}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\]]{lang="EN-US"}
:::

::: {#498463274 .myid}
[]{#_Toc404785118}[]{#struct_0_21171_18224_733047157}[]{#_Toc330384044}

**WAN接口 \-- ISDN BRI接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1032223217}[命令用来配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的对外自环。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x909442412}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1763002556}

[**[loopback]{lang="EN-US"}**[ { **b1** \| **b2** \| **both** }]{lang="EN-US"}]{#struct_0_21171_18224_x441229735}

[**[undo loopback]{lang="SV"}**]{#struct_0_21171_18224_x252106212}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1507931749}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_21171_18224_x211708063}[接口不对外自环。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1756067734}

[[ISDN BRI]{lang="SV"}]{#struct_0_21171_18224_1903031510}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1953273988}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1934112902}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1763199164}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x579972084}

[**[b1]{lang="SV"}**]{#struct_0_21171_18224_x1523586015}[：]{style="font-family:宋体"}[B1]{lang="SV"}[通道对外自环。]{style="font-family:
宋体"}

[**[b2]{lang="SV"}**]{#struct_0_21171_18224_x1643969224}[：]{style="font-family:宋体"}[B2]{lang="SV"}[通道对外自环。]{style="font-family:
宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_21171_18224_304383684}[：]{style="font-family:宋体"}[B1]{lang="EN-US"}[和]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道同时对外自环。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x786399674}

[[所谓自环，是指将从线路来的数据返回线路。]{style="font-family:宋体"}[ISDN BRI]{lang="EN-US"}]{#struct_0_21171_18224_1410012260}[接口支持]{style="font-family:宋体"}[B1]{lang="EN-US"}[、]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道对外自环以及]{style="font-family:宋体"}[B1]{lang="EN-US"}[和]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道同时对外自环。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1074127883}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1763133628}[配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的]{style="font-family:宋体"}[B1]{lang="EN-US"}[和]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道同时对外自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1361391245}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] loopback both]{lang="EN-US"}
:::

::: {#-1657532687 .myid}
[]{#_Toc404785119}[]{#struct_0_21171_18224_x791724994}[]{#_Toc330384045}

**WAN接口 \-- ISDN BRI接口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_1912273082}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_1714923406}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1819846188}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_21171_18224_x2038502053}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x1273883726}

[[【缺省情况】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x1762805948}

[[BRI]{lang="EN-US"}]{#struct_0_21171_18224_x53697944}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x816049360}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_21171_18224_x1895890444}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1479076887}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1758203743}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x851264249}

[[【参数】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_x481419401}

[*[size]{lang="EN-US"}*]{#struct_0_21171_18224_x1762740412}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_1556220551}

[[配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x685300393}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#943634"}]{#struct_0_21171_18224_943867039}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x743165320}[配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1261679355}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] mtu 1430]{lang="EN-US"}
:::

::: {#-1344736563 .myid}
[]{#_Toc404785120}[]{#struct_0_21171_18224_x340843704}[]{#_Toc330384046}

**WAN接口 \-- ISDN BRI接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_x1762937020}[命令用来清除]{style="font-family:
宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1558022652}

[**[reset counters interface]{lang="EN-US"}**[ \[ **bri** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_21171_18224_x1545858313}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1783576558}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1993629695}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1951547135}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1290794032}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1181166267}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x170696565}

[**[bri]{lang="EN-US"}**]{#struct_0_21171_18224_x1762871484}[：清除]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x411904776}[：]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_861250921}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1395372378}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[bri]{lang="EN-US"}**]{#struct_0_21171_18224_1437821291}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[bri]{lang="EN-US"}**]{#struct_0_21171_18224_x1337548929}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[bri]{lang="EN-US"}**]{#struct_0_21171_18224_x266424425}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1932004430}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1762543804}[清除]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface bri 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x1981877319}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_238152986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}[bri]{lang="EN-US"}**]{#struct_0_21171_18224_x1018873127}
:::

::: {#1725110147 .myid}
[]{#_Toc107907782}[]{#_Toc80503858}[]{#_Toc42331116}[]{#_Toc42327222}[]{#_Toc42055177}[]{#_Toc32637994}[]{#_Toc31422529}[]{#_Toc25403665}[]{#_Toc404785122}[]{#struct_0_21171_18224_x1205635436}[]{#_Toc325038103}[]{#_Toc261964968}[]{#_Toc205607573}[]{#_Toc35776871}[]{#_Toc35782345}[]{#_Toc35782468}[]{#_Toc35776872}[]{#_Toc35782346}[]{#_Toc35782469}[]{#_Toc35776873}[]{#_Toc35782347}[]{#_Toc35782470}[]{#_Toc35776874}[]{#_Toc35782348}[]{#_Toc35782471}[]{#_Toc35776875}[]{#_Toc35782349}[]{#_Toc35782472}[]{#_Toc35776876}[]{#_Toc35782350}[]{#_Toc35782473}[]{#_Toc35776877}[]{#_Toc35782351}[]{#_Toc35782474}[]{#_Toc35776878}[]{#_Toc35782352}[]{#_Toc35782475}[]{#_Toc35776879}[]{#_Toc35782353}[]{#_Toc35782476}[]{#_Toc35776880}[]{#_Toc35782354}[]{#_Toc35782477}[]{#_Toc35776881}[]{#_Toc35782355}[]{#_Toc35782478}[]{#_Toc35776882}[]{#_Toc35782356}[]{#_Toc35782479}[]{#_Toc35776883}[]{#_Toc35782357}[]{#_Toc35782480}[]{#_Toc35776884}[]{#_Toc35782358}[]{#_Toc35782481}[]{#_Toc35776885}[]{#_Toc35782359}[]{#_Toc35782482}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- alarm-detect**

------------------------------------------------------------------------

[**[alarm-detect]{lang="PT-BR"}**]{#struct_0_21171_18224_x1416047339}[命令用来配置检测远端告警信号。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_21171_18224_1156435087}**[alarm-detect]{lang="PT-BR"}**[命令用来取消检测远端告警信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1762478268}

[**[alarm-detect rai]{lang="PT-BR"}**]{#struct_0_21171_18224_x1168529562}

[**[undo alarm-detect rai]{lang="PT-BR"}**]{#struct_0_21171_18224_1241642376}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_698243671}

[[检测远端告警信号。]{style="font-family:宋体"}]{#struct_0_21171_18224_1391674016}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1773218518}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x1610706831}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x635939538}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x1763068091}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x1536377615}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1894453650}

[**[rai]{lang="PT-BR"}**]{#struct_0_21171_18224_832109139}[：]{style="font-family:宋体"}[Remote Alarm Indication]{lang="PT-BR"}[，]{style="font-family:宋体"}[即远端告警指示信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_353681933}

[[在]{style="font-family:宋体"}]{#struct_0_21171_18224_1127299948}[CE1]{lang="PT-BR"}[方式的情况下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以使用该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1492496999}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_769437690}[配置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[检测远端告警信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1763002555}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] alarm-detect rai]{lang="PT-BR"}
:::

::: {#1865358413 .myid}
[]{#_Toc404785123}[]{#struct_0_21171_18224_x37945208}[]{#_Toc325038104}[]{#_Toc261964969}[]{#_Toc205607574}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- cable (CE1/PRI interface)**

------------------------------------------------------------------------

[**[cable]{lang="FR"}**]{#struct_0_21171_18224_x1384387651}[命令用来配置]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[接口匹配的传输线路类型。]{style="font-family:宋体"}

[**[undo cable]{lang="FR"}**]{#struct_0_21171_18224_222569597}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1161021907}

[**[cable ]{lang="FR"}**]{#struct_0_21171_18224_x1953052569}[{ **long** \| **short** }]{lang="FR"}

[**[undo cable]{lang="FR"}**]{#struct_0_21171_18224_x486010535}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1333281799}

[[CE1/PRI]{lang="FR"}]{#struct_0_21171_18224_768516281}[接口匹配的传输线路类型为]{style="font-family:宋体"}**[long]{lang="FR"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1763199163}

[[CE1/PRI]{lang="FR"}]{#struct_0_21171_18224_1342342217}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1966712124}

[[network-admin]{lang="FR"}]{#struct_0_21171_18224_521247115}

[[mdc-admin]{lang="FR"}]{#struct_0_21171_18224_488013837}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x189678285}

[**[long]{lang="FR"}**]{#struct_0_21171_18224_x295460772}[：]{style="font-family:宋体"}[表示接收器的衰减为]{style="font-family:宋体"}[-43db]{lang="FR"}[。]{style="font-family:宋体"}

[**[short]{lang="FR"}**]{#struct_0_21171_18224_x1001511382}[：]{style="font-family:宋体"}[表示接收器的衰减为]{style="font-family:宋体"}[-10db]{lang="FR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1763133627}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1764675772}[配置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[匹配的传输线路类型为]{style="font-family:宋体"}**[short]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x127985151}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] cable short]{lang="EN-US"}
:::

::: {#32192858 .myid}
[]{#_Toc404785124}[]{#struct_0_21171_18224_944093597}[]{#_Toc374365279}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- cem-set (CE1/PRI interface)**

------------------------------------------------------------------------

[**[cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_x188283655}[命令用来将]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[接口的时隙捆绑为电路仿真组（]{style="font-family:宋体"}[cem set]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[undo cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_x692465752}[命令用来删除已有的]{style="font-family:宋体"}[电路仿真组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_21171_18224_423199738}

[**[cem-set]{lang="EN-US"}**[ *set-number* **timeslot-list** *list*]{lang="EN-US"}]{#struct_0_21171_18224_x453861130}

[**[undo cem-set]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_21171_18224_191921779}[\[]{lang="IT"}*[ set-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\]]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1056474631}

[[不捆绑任何]{style="font-family:宋体"}[cem set]{lang="EN-US"}]{#struct_0_21171_18224_944159133}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_142726645}

[[CE1/PRI]{lang="FR"}]{#struct_0_21171_18224_x1452193041}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1224042864}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1761632209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_288505023}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_944224669}

[*[set-number]{lang="EN-US"}*]{#struct_0_21171_18224_x698046971}[：]{style="font-family:宋体"}[该接口上时隙捆绑形成的电路仿真组编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_735383157}*[ list]{lang="FR"}*[：被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="EN-US"}*[为时隙编号，其取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。在指定捆绑的时隙时，可以用]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的形式指定单个时隙，也可以用]{style="font-family:宋体"}*[number1-number2]{lang="EN-US"}*[的形式指定一个范围内的时隙，还可以使用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[,*number2*-*number3*]{lang="EN-US"}[的形式，同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_875599865}

[[CE1/PRI]{lang="FR"}]{#struct_0_21171_18224_x1904286563}[接口使用]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[工作方式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[它在物理上分为]{style="font-family:宋体"}[32]{lang="FR"}[个时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[对应编号为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[。]{style="font-family:
宋体"}

[[使用时，可以将除]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_21171_18224_1572761958}[时隙外的全部时隙分成若干电路仿真组（]{style="font-family:宋体"}[cem set]{lang="EN-US"}[），每组时隙捆绑以后，将自动创建一个电路仿真接口。]{style="font-family:宋体"}

[[电路仿真接口]{style="font-family:宋体"}]{#struct_0_21171_18224_2071904261}[的名称是]{style="font-family:宋体"}**[circuit-emulation]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-number]{lang="FR"}***[:]{lang="FR"}***[set-number]{lang="FR"}*[。其中]{style="font-family:宋体"}*[interface-number]{lang="FR"}*[是]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[接口的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[set-number]{lang="FR"}*[是]{style="font-family:宋体"}[电路仿真组的]{style="font-family:宋体"}[编号。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}]{#struct_0_21171_18224_944814493}[CE1/PRI]{lang="FR"}[接口上，]{style="font-family:宋体"}[cem set]{lang="DA"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[可以同时使用（]{style="font-family:宋体"}[但]{style="font-family:宋体"}[cem set]{lang="FR"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[绑定的组号和时隙不能重复]{style="font-family:宋体"}[），]{style="font-family:宋体"}[pri set]{lang="DA"}[不能和其它]{style="font-family:宋体"}[方式同时使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1553764178}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_393564732}[将]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:
宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[10-15]{lang="EN-US"}[和]{style="font-family:宋体"}[18]{lang="EN-US"}[时隙捆绑为]{style="font-family:宋体"}[0]{lang="EN-US"}[号电路仿真组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_522891020}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] cem-set 0 timeslot-list 1,2,5,10-15,18]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_47587797}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_x7977741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pri-set]{lang="EN-US"}**]{#struct_0_21171_18224_944880029}
:::

::: {#-1316279111 .myid}
[]{#_Toc404785125}[]{#struct_0_21171_18224_x1402821655}[]{#_Toc325038105}[]{#_Toc261964970}[]{#_Toc205607575}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- channel-set (CE1/PRI interface)**

------------------------------------------------------------------------

[**[channel-set]{lang="FR"}**]{#struct_0_21171_18224_1832346714}[命令用来将]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[接口的时隙捆绑为通道组]{style="font-family:宋体"}[（]{style="font-family:宋体"}[channel set]{lang="FR"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo channel-set]{lang="FR"}**]{#struct_0_21171_18224_2026122249}[命令用来取消已有的通道组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1515786288}

[**[channel-set]{lang="FR"}**]{#struct_0_21171_18224_x1191121407}[ *set-number* **timeslot-list** *list*]{lang="FR"}

[**[undo]{lang="FR"}**]{#struct_0_21171_18224_x1762805947}[ **channel-set** \[ *set-number* \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_705816943}

[[不捆绑任何]{style="font-family:宋体"}]{#struct_0_21171_18224_x1558168660}[channel set]{lang="FR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x811398699}

[[CE1/PRI]{lang="FR"}]{#struct_0_21171_18224_2035054365}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1798452788}

[[network-admin]{lang="FR"}]{#struct_0_21171_18224_x203395334}

[[mdc-admin]{lang="FR"}]{#struct_0_21171_18224_x1616955381}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1762740411}

[*[set-number]{lang="FR"}*]{#struct_0_21171_18224_1959505078}[：]{style="font-family:宋体"}[该接口上时隙捆绑形成的]{style="font-family:宋体"}[channel set]{lang="FR"}[编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[30]{lang="FR"}[。]{style="font-family:宋体"}

[**[timeslot-list]{lang="FR"}**]{#struct_0_21171_18224_1905974626}*[ list]{lang="FR"}*[：]{style="font-family:宋体"}[被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="FR"}*[为时隙编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[。在指定捆绑的时隙时]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[可以用]{style="font-family:宋体"}*[number]{lang="FR"}*[的形式指定单个时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以用]{style="font-family:宋体"}*[number1-number2]{lang="FR"}*[的形式指定一个范围内的时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[还可以使用]{style="font-family:宋体"}*[number1]{lang="FR"}*[,*number2-number3*]{lang="FR"}[的形式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_236844333}

[[CE1/PRI]{lang="FR"}]{#struct_0_21171_18224_1215014307}[接口使用]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[工作方式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[它在物理上分为]{style="font-family:宋体"}[32]{lang="FR"}[个时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[对应编号为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[。]{style="font-family:
宋体"}

[[使用时，可以将除]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_21171_18224_x1992173679}[时隙外的全部时隙分成若干通道组（]{style="font-family:宋体"}[channel set]{lang="EN-US"}[），每组时隙捆绑以后，将自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，其逻辑特性与同步串口相同。]{style="font-family:宋体"}

[[Serial]{lang="EN-US"}]{#struct_0_21171_18224_x451547914}[接口的]{style="font-family:宋体"}[名称]{style="font-family:宋体"}[是]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *interface-number***:***set-number*]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[是]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的编号，]{style="font-family:宋体"}*[set-number]{lang="EN-US"}*[是]{style="font-family:宋体"}[channel set]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}]{#struct_0_21171_18224_x794050002}[CE1/PRI]{lang="FR"}[接口上，]{style="font-family:宋体"}[cem set]{lang="DA"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[可以同时使用（]{style="font-family:宋体"}[但]{style="font-family:宋体"}[cem set]{lang="EN-US"}[和]{style="font-family:宋体"}[channel set]{lang="EN-US"}[绑定的组号和时隙不能重复）]{style="font-family:宋体"}[，]{style="font-family:宋体"}[pri set]{lang="DA"}[不能和其它]{style="font-family:宋体"}[方式同时使用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1762937019}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_814433735}[将]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:
宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[10-15]{lang="EN-US"}[和]{style="font-family:宋体"}[18]{lang="EN-US"}[时隙捆绑为]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[channel-set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_411506364}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] channel-set 0 timeslot-list 1,2,5,10-15,18]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x883846579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_944355742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pri-set]{lang="EN-US"}**]{#struct_0_21171_18224_x1157288287}
:::

::: {#-1311170573 .myid}
[]{#_Toc404785126}[]{#struct_0_21171_18224_1048325001}[]{#_Toc325038106}[]{#_Toc261964971}[]{#_Toc205607576}[]{#_Toc11588577}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- clock (CE1/PRI interface)**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_690218536}[命令用来配置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_x786019059}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1762871483}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_21171_18224_x1171419663}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_x1707293334}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x190937905}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1950639323}[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x234047314}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1075280931}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_499894155}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1762543803}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1578592792}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1345461181}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_251574261}[：主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_1572540239}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_74593380}

[[当]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1970620059}[接口作为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧使用时，应使用主时钟模式；作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧使用时，应使用从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1165201372}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1876963955}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1762478267}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] clock master]{lang="EN-US"}
:::

::: {#1726432707 .myid}
[]{#_Toc404785127}[]{#struct_0_21171_18224_x1928044449}[]{#_Toc325038107}[]{#_Toc261964972}[]{#_Toc257636844}[]{#_Toc246215007}[]{#_Toc246210097}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- clock-change auto**

------------------------------------------------------------------------

[**[clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_x51983275}[命令用来开启接口的时钟自动切换功能。即接口在]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[模式下收到]{style="font-family:宋体"}[AIS/LOS/LOF]{lang="EN-US"}[告警后，自动切换成]{style="font-family:宋体"}**[master]{lang="EN-US"}**[模式。当告警消除后，接口自动切换成用户配置的时钟模式。]{style="font-family:宋体"}

[**[undo clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_x1436096025}[命令用来关闭接口的时钟自动切换功能，接口恢复成当前用户配置的时钟模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x839262597}

[**[clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_1205455646}

[**[undo clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_x1768134039}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1763068094}

[[时钟自动切换功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_x776862728}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_410577978}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1846794057}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x390432807}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_257178863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x558726255}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1528903436}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1089957750}[开启]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的时钟自动切换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1763002558}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] clock-change auto]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_365339319}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_x1136214429}
:::

::: {#773449183 .myid}
[]{#_Toc404785128}[]{#struct_0_21171_18224_136574582}[]{#_Toc325038108}[]{#_Toc261964973}[]{#_Toc205607577}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- code (CE1/PRI interface)**

------------------------------------------------------------------------

[**[code]{lang="EN-US"}**]{#struct_0_21171_18224_x1189701004}[命令用来配置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的线路编解码格式。]{style="font-family:宋体"}

[**[undo code]{lang="EN-US"}**]{#struct_0_21171_18224_527160615}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1699405934}

[**[code]{lang="EN-US"}**[ { **ami** \| **hdb3** }]{lang="EN-US"}]{#struct_0_21171_18224_x437864964}

[**[undo code]{lang="EN-US"}**]{#struct_0_21171_18224_x1763199166}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_582827330}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1680506641}[接口的线路编解码格式为]{style="font-family:宋体"}**[hdb3]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1204923084}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1046253483}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2013515637}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1787254421}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_211110429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1763133630}

[**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_x1005226421}[：采用]{style="font-family:宋体"}[AMI]{lang="EN-US"}[（]{style="font-family:宋体"}[Alternate Mark Inversion]{lang="EN-US"}[，信号交替反转码）线路编码格式。]{style="font-family:宋体"}

[**[hdb3]{lang="EN-US"}**]{#struct_0_21171_18224_x2019747353}[：采用]{style="font-family:宋体"}[HDB3]{lang="EN-US"}[（]{style="font-family:宋体"}[High Density Bipolar 3]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[阶高密度双极性码）线路编码格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1946602626}

[[配置接口的线路编解码格式时，请注意与对端设备保持一致。]{style="font-family:宋体"}]{#struct_0_21171_18224_x366384520}

[[线路编码采用]{style="font-family:宋体"}**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_175043409}[方式时，在该接口上需要同时配置]{style="font-family:宋体"}**[data-coding]{lang="EN-US"}**[ **inverted**]{lang="EN-US"}[，才能保证接口正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1515606569}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1172237842}[配置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的线路编解码格式为]{style="font-family:宋体"}**[ami]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1762805950}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] code ami]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_302597952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[data-coding]{lang="IT"}**]{#struct_0_21171_18224_1988969388}
:::

::: {#-781000338 .myid}
[]{#_Toc404785129}[]{#struct_0_21171_18224_x568900074}[]{#_Toc325038109}[]{#_Toc261964974}[]{#_Toc205607578}[]{#_Toc11588578}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- controller e1**

------------------------------------------------------------------------

[**[controller e1]{lang="EN-US"}**]{#struct_0_21171_18224_x486530651}[命令用来进入]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x627620656}

[**[controller]{lang="EN-US"}**[ **e1** *interface-number*]{lang="EN-US"}]{#struct_0_21171_18224_x811728482}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1625323424}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1762740414}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1575947331}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_567649422}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1318652172}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1196936202}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_1154302140}[：]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1695497210}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1291858748}[进入]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1762937022}

[\[Sysname\] controller e1 2/3/0]{lang="PT-BR"}

[\[Sysname-E1 2/3/0\]]{lang="PT-BR"}
:::

::: {#-2071102341 .myid}
[]{#_Toc404785130}[]{#struct_0_21171_18224_1574145230}[]{#_Toc325038110}[]{#_Toc261964976}[]{#_Toc205607580}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- data-coding (CE1/PRI interface)**

------------------------------------------------------------------------

[**[data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_x825126215}[命令用来设置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口是否对用户数据进行翻转。]{style="font-family:宋体"}

[**[undo data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_202643360}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_713983412}

[**[data-coding]{lang="IT"}**]{#struct_0_21171_18224_2081565231}[ { **inverted** \| **normal** }]{lang="IT"}

[**[undo data-coding]{lang="IT"}**]{#struct_0_21171_18224_x373378536}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1321050807}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_1209673933}[接口不对用户数据进行翻转。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1762871486}

[[CE1/PRI]{lang="IT"}]{#struct_0_21171_18224_x1574704190}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1951385292}

[[network-admin]{lang="IT"}]{#struct_0_21171_18224_956985566}

[[mdc-admin]{lang="IT"}]{#struct_0_21171_18224_678279528}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1502568476}

[**[inverted]{lang="IT"}**]{#struct_0_21171_18224_x1013404964}[：]{style="font-family:宋体"}[对用户数据进行翻转。]{style="font-family:宋体"}

[**[normal]{lang="PT-BR"}**]{#struct_0_21171_18224_x2077635633}[：]{style="font-family:宋体"}[不对用户数据进行翻转。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1762543806}

[[HDLC]{lang="EN-US"}]{#struct_0_21171_18224_x819077905}[协议为了防止有效数据中的]{style="font-family:宋体"}[7e]{lang="EN-US"}[被当作填充符，会在连续]{style="font-family:宋体"}[5]{lang="EN-US"}[个]{style="font-family:宋体"}[1]{lang="EN-US"}[后插入一个]{style="font-family:
宋体"}[0]{lang="EN-US"}[。然后可以进行数据翻转，数据翻转后，]{style="font-family:宋体"}[0]{lang="EN-US"}[变成]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[变成]{style="font-family:
宋体"}[0]{lang="EN-US"}[。数据翻转的作用是：当]{style="font-family:宋体"}[E1]{lang="EN-US"}[接口配置为]{style="font-family:宋体"}[AMI]{lang="EN-US"}[编码时，能保证每]{style="font-family:宋体"}[8]{lang="EN-US"}[个连续比特中至少有一个]{style="font-family:宋体"}[1]{lang="EN-US"}[，从而弥补]{style="font-family:宋体"}[AMI]{lang="EN-US"}[码中易出现过多连]{style="font-family:宋体"}[0]{lang="EN-US"}[的缺陷。]{style="font-family:宋体"}

[[需注意的是，只有通信的]{style="font-family:宋体"}[E1]{lang="EN-US"}]{#struct_0_21171_18224_1059276372}[线路两端的]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口保持一致（都进行翻转或都不进行数据翻转），才能正常通信。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1214409138}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1116812511}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[对用户数据进行翻转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1008788762}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] data-coding inverted]{lang="IT"}
:::

::: {#740203330 .myid}
[]{#_Toc404785131}[]{#struct_0_21171_18224_712558626}[]{#_Toc325038112}[]{#_Toc261964978}[]{#_Toc205607582}[]{#_Toc146362359}[]{#_Toc275246679}[]{#_Toc275250647}[]{#_Toc275246680}[]{#_Toc275250648}[]{#_Toc275246681}[]{#_Toc275250649}[]{#_Toc275246682}[]{#_Toc275250650}[]{#_Toc275246683}[]{#_Toc275250651}[]{#_Toc275246684}[]{#_Toc275250652}[]{#_Toc275246685}[]{#_Toc275250653}[]{#_Toc275246686}[]{#_Toc275250654}[]{#_Toc275246687}[]{#_Toc275250655}[]{#_Toc275246688}[]{#_Toc275250656}[]{#_Toc275246689}[]{#_Toc275250657}[]{#_Toc275246690}[]{#_Toc275250658}[]{#_Toc275246691}[]{#_Toc275250659}[]{#_Toc275246692}[]{#_Toc275250660}[]{#_Toc275246695}[]{#_Toc275250663}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- detect-ais**

------------------------------------------------------------------------

[**[detect-ais]{lang="EN-US"}**]{#struct_0_21171_18224_x518901625}[命令用来配置当前接口进行]{style="font-family:宋体"}[AIS]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[**[undo detect-ais]{lang="EN-US"}**]{#struct_0_21171_18224_x1762478270}[命令用来取消]{style="font-family:宋体"}[AIS]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1524694386}

[**[detect-ais]{lang="PT-BR"}**]{#struct_0_21171_18224_x1345762438}

[**[undo detect-ais]{lang="PT-BR"}**]{#struct_0_21171_18224_362367659}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1365983842}

[[进行]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_21171_18224_1919791226}[检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_902795307}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_346665125}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1763068093}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1595790267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_202659909}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1252572948}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_986375382}[接口工作在]{style="font-family:宋体"}[E1]{lang="PT-BR"}[方式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以使用该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1781149882}

[[\# ]{lang="PT-BR"}]{#struct_0_21171_18224_183014919}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="PT-BR"}[进行]{style="font-family:宋体"}[AIS]{lang="PT-BR"}[检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_932136242}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] detect-ais]{lang="PT-BR"}
:::

::: {#1346685889 .myid}
[]{#_Toc404785132}[]{#struct_0_21171_18224_x1763002557}[]{#_Toc325038113}[]{#_Toc261964979}[]{#_Toc205607583}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- display controller e1**

------------------------------------------------------------------------

[**[display controller e1]{lang="EN-US"}**]{#struct_0_21171_18224_1124854206}[命令用来显示]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1069899884}

[**[display controller]{lang="EN-US"}**[ **e1** \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_21171_18224_380445327}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1665967954}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1861452516}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2055390083}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_700457937}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_x1763199165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x2146056025}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_2016166898}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1182851456}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x279123192}[：]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的编号。不指定本参数，将显示所有]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1946323312}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_140377941}[显示]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller e1 2/3/0]{lang="EN-US"}]{#struct_0_21171_18224_x1763133629}

[E1 2/3/0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Description: E1 2/3/0 Interface]{lang="EN-US"}

[Basic Configuration:]{lang="EN-US"}

[  Work mode: E1 framed, Cable type: 75 Ohm unbalanced]{lang="EN-US"}

[  Line code: hdb3, Source clock: slave]{lang="EN-US"}

[  Idle code: 7e, Itf type: 7e, Itf number: 4, Loop back: not set]{lang="EN-US"}

[Alarm State:]{lang="EN-US"}

[  Receiver alarm state is None]{lang="EN-US"}

[Historical Statistics:]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Data in current interval (150 seconds elapsed):]{lang="EN-US"}

[  Loss Frame Alignment: 0 seconds, Framing Error: 0 seconds]{lang="EN-US"}

[  CRC Error: 0 seconds, Alarm Indication: 0 seconds]{lang="EN-US"}

[  Loss-of-signals: 0 seconds, Code Violations: 0 seconds]{lang="EN-US"}

[  ]{lang="FR"}[Slip: 0 seconds, E-Bit error: 0 seconds]{lang="EN-US"}

[]{#struct_0_21171_18224_1367492110}[]{#_Toc131988742}[[表1-8 ]{lang="EN-US"}[display controller e1]{lang="EN-US"}]{#_Toc121668337}[命令显示信息]{style="font-family:黑体"}[描述表]{style="font-family:黑体"}

[]{#table_struct_0_1610737590}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_x1355006851}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x1762805949}

[[E1 2/3/0]{lang="EN-US"}]{#struct_0_21171_18224_1512385997}

[[Current state]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_21171_18224_913138447}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_x2060295975}[接口当前的状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_x984794675}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_1262491512}[接口的描述信息]{style="font-family:宋体"}

[[Work mode]{lang="EN-US"}]{#struct_0_21171_18224_x1762740413}

[[E1]{lang="FR"}]{#struct_0_21171_18224_x1172662804}[接口的工作模式]{style="font-family:宋体"}[（]{style="font-family:宋体"}[E1/CE1]{lang="FR"}[）]{style="font-family:宋体"}

[[Cable type]{lang="EN-US"}]{#struct_0_21171_18224_1283587457}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_x1032727395}[接口的线缆类型]{style="font-family:宋体"}

[[Source Clock]{lang="EN-US"}]{#struct_0_21171_18224_1170860703}

[[接口的源时钟（]{style="font-family:宋体"}[master/slave]{lang="EN-US"}]{#struct_0_21171_18224_889271295}[）]{style="font-family:宋体"}

[[Line Code]{lang="EN-US"}]{#struct_0_21171_18224_x567179016}

[[线路码（]{style="font-family:宋体"}[Ami/hdb3]{lang="EN-US"}]{#struct_0_21171_18224_2079060098}[）]{style="font-family:宋体"}

[[Idle Code]{lang="EN-US"}]{#struct_0_21171_18224_x1762871485}

[[空闲码（]{style="font-family:宋体"}[7e/ff]{lang="EN-US"}]{#struct_0_21171_18224_x1977988717}[）]{style="font-family:宋体"}

[[Itf type]{lang="EN-US"}]{#struct_0_21171_18224_x246273410}

[[帧间填充码（]{style="font-family:宋体"}[7e/ff]{lang="EN-US"}]{#struct_0_21171_18224_1874893840}[）]{style="font-family:宋体"}

[[Itf number ]{lang="EN-US"}]{#struct_0_21171_18224_x2129221474}

[[帧间填充码的个数]{style="font-family:宋体"}]{#struct_0_21171_18224_x1762543805}

[[Loopback]{lang="EN-US"}]{#struct_0_21171_18224_x415793378}

[[接口是否设置了环回]{style="font-family:宋体"}]{#struct_0_21171_18224_220755182}

[[Alarm State]{lang="EN-US"}]{#struct_0_21171_18224_852790309}

[[告警状态]{style="font-family:宋体"}]{#struct_0_21171_18224_x1762478269}

[[Historical Statistics]{lang="EN-US"}]{#struct_0_21171_18224_1560353793}

[[历史统计数据]{style="font-family:宋体"}]{#struct_0_21171_18224_x1096961610}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_1635423106}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_1761708337}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_x1449690609}

[[清零记录]{style="font-family:宋体"}]{#struct_0_21171_18224_x196984149}

[[Data in current interval (150 seconds elapsed):]{lang="EN-US"}]{#struct_0_21171_18224_x36112142}

[[  Loss Frame Alignment: 0 seconds, Framing Error: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_995792218}

[[  CRC Error: 0 seconds, Alarm Indication: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x1427088700}

[[  Loss-of-signals: 0 seconds, Code Violations: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x196918613}

[[  Slip: 0 seconds, E-Bit error: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_395805107}

[[当前时间间隔内的各种错误发生持续的时间统计，错误包括：帧没对齐，帧错误，警告，丢信号，违规码时间，滑帧]{style="font-family:宋体"}]{#struct_0_21171_18224_x855595027}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1272949601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters controller e1]{lang="EN-US"}**]{#struct_0_21171_18224_855382637}

::: {#739210203 .myid}
[]{#_Toc404785133}[]{#struct_0_21171_18224_x1162836988}[]{#_Toc325038114}[]{#_Toc261964983}[]{#_Toc205607587}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- frame-format (CE1/PRI interface)**

------------------------------------------------------------------------

[**[frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_x197115221}[命令用来设置]{style="font-family:宋体"}[CE1]{lang="PT-BR"}[接口的帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_x396721295}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1412477366}

[**[frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_1898150202}[ { **crc4** \| **no-crc4** }]{lang="PT-BR"}

[**[undo frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_530143374}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1278501165}

[[CE1]{lang="PT-BR"}]{#struct_0_21171_18224_x952735378}[接口的帧格式为]{style="font-family:宋体"}**[no-crc4]{lang="PT-BR"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1579308124}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x197049685}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_449317830}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_1005166193}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x414642950}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_663742892}

[**[crc4]{lang="PT-BR"}**]{#struct_0_21171_18224_1183423367}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[CE1]{lang="PT-BR"}[接口的帧格式为]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[帧格式。]{style="font-family:宋体"}

[**[no-crc4]{lang="PT-BR"}**]{#struct_0_21171_18224_1700135505}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[CE1]{lang="PT-BR"}[接口的帧格式为非]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[帧格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1139567313}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_894678696}[CE1/PRI]{lang="PT-BR"}[接口工作在]{style="font-family:宋体"}[CE1]{lang="PT-BR"}[方式下时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[支持]{style="font-family:宋体"}**[crc4]{lang="PT-BR"}**[和]{style="font-family:宋体"}**[no-crc4]{lang="PT-BR"}**[两种帧格式。其中]{style="font-family:宋体"}**[crc4]{lang="EN-US"}**[帧格式支持对物理帧进行]{style="font-family:宋体"}[4]{lang="EN-US"}[比特的循环冗余校验，而]{style="font-family:宋体"}**[no-crc4]{lang="EN-US"}**[帧格式则不支持对物理帧进行]{style="font-family:宋体"}[4]{lang="EN-US"}[比特的循环冗余校验。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x196722005}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1547354862}[设置接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}**[crc4]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1373852460}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] frame-format crc4]{lang="EN-US"}
:::

::: {#-476883846 .myid}
[]{#_Toc11588581}[]{#_Toc404785134}[]{#struct_0_21171_18224_2056333563}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- idle-code (CE1/PRI interface)**

------------------------------------------------------------------------

[**[idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_202422810}[命令用来设置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口的线路空闲码类型]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x1899770891}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x591138796}

[**[idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x196656469}[ { **7e** \| **ff** }]{lang="PT-BR"}

[**[undo idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_1524240287}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1160956903}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_2039866610}[接口的线路空闲码类型为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1103502941}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x439207411}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2014675999}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_1685673648}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x196853077}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_21171_18224_x603947}

[**[7e]{lang="PT-BR"}**]{#struct_0_21171_18224_x1548390277}[：]{style="font-family:宋体"}[线路空闲码为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[类型。]{style="font-family:宋体"}

[**[ff]{lang="PT-BR"}**]{#struct_0_21171_18224_x65546396}[：]{style="font-family:宋体"}[线路空闲码为]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1925289149}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_1540771225}[接口的线路空闲码类型是指在没有被绑定到逻辑通道的时隙上发送的码型。]{style="font-family:宋体"}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_748009485}[接口的线路空闲码类型有两种]{style="font-family:宋体"}[：]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[和]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1793707941}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x255965293}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的线路空闲码类型为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x196787541}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] idle-code 7e]{lang="EN-US"}
:::

::: {#577437954 .myid}
[]{#_Toc404785135}[]{#struct_0_21171_18224_1131322079}[]{#_Toc325038116}[]{#_Toc261964985}[]{#_Toc205607589}[]{#_Toc107907662}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- itf (CE1/PRI interface)**

------------------------------------------------------------------------

[**[itf]{lang="PT-BR"}**]{#struct_0_21171_18224_x2077884813}[命令用来设置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口的帧间填充符类型和个数。]{style="font-family:宋体"}

[**[undo itf]{lang="PT-BR"}**]{#struct_0_21171_18224_x82190698}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x281012081}

[**[itf ]{lang="PT-BR"}**]{#struct_0_21171_18224_1485265608}[{ **number** *number* \| **type** { **7e** \| **ff** } }]{lang="PT-BR"}

[**[undo itf ]{lang="PT-BR"}**]{#struct_0_21171_18224_658226875}[{ **number** \| **type** }]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x196459861}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x723252040}[接口的帧间填充符类型为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[，帧间填充字节个数为]{style="font-family:宋体"}[4]{lang="PT-BR"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_735898087}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1543304077}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2094277130}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_310886532}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x940416763}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1175868850}

[**[number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_21171_18224_x196394325}[：设置帧间填充字节的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[14]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**]{#struct_0_21171_18224_339474482}[：设置帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型。]{style="font-family:宋体"}

[**[7e]{lang="EN-US"}**]{#struct_0_21171_18224_x2069321797}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[**[ff]{lang="EN-US"}**]{#struct_0_21171_18224_x2069256261}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_21171_18224_2564792}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x698274587}[接口的帧间填充符是指已经被绑定到逻辑通道的时隙在没有发送业务数据时发送的码型。]{style="font-family:宋体"}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x393545754}[接口的帧间填充符类型有两种：]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[和]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x1613853804}[CE1/PRI]{lang="PT-BR"}[接口工作在]{style="font-family:宋体"}[E1]{lang="PT-BR"}[方式，且帧间填充符配置为]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[格式时，在没有业务数据时，线路上会发送全"]{style="font-family:宋体"}[1]{lang="PT-BR"}["的数据，容易产生]{style="font-family:宋体"}[AIS]{lang="PT-BR"}[告警。在此情况下，建议用户通过]{style="font-family:宋体"}**[undo detect-ais]{lang="PT-BR"}**[命令取消]{style="font-family:宋体"}[AIS]{lang="PT-BR"}[检测，以免系统产生]{style="font-family:宋体"}[AIS]{lang="PT-BR"}[告警。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1660781532}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1836201982}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x196984148}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] itf type ff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x36177678}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的帧间填充字节个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x194519791}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] itf number 5]{lang="EN-US"}
:::

::: {#-1661911887 .myid}
[]{#_Toc404785136}[]{#struct_0_21171_18224_x1027011428}[]{#_Toc325038117}[]{#_Toc261964986}[]{#_Toc205607590}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- loopback (CE1/PRI interface)**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1498254779}[命令用来开启]{style="font-family:宋体"}[CE1/PR]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x126556990}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x602728436}

[**[loopback]{lang="EN-US"}**[ { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_21171_18224_x1110403495}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x196918612}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_395870643}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_1925996815}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1895151228}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1186738105}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_287953465}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_241695512}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1075555030}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1694327222}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_x197115220}[：设置接口对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_x396655759}[：设置接口对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_x1742306245}[：设置接口对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1852934949}

[[自环、环回功能主要用于检测接口或电缆本身的状况，正常工作时应关闭这些功能。]{style="font-family:宋体"}]{#struct_0_21171_18224_x744077059}

[[对于将]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1989883553}[接口时隙经捆绑而形成的串口，如果串口的链路层协议配置为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[，在设置自环后，其链路层协议状态将上报为]{style="font-family:宋体"}[down]{lang="EN-US"}[，这属于正常情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x115576379}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1064549303}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x197049684}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] loopback local]{lang="EN-US"}
:::

::: {#584894822 .myid}
[]{#_Toc404785137}[]{#struct_0_21171_18224_449252294}[]{#_Toc325038118}[]{#_Toc261964987}[]{#_Toc205607591}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- pri-set (CE1/PRI interface)**

------------------------------------------------------------------------

[**[pri-set]{lang="FR"}**]{#struct_0_21171_18224_x1360897381}[命令用来将]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[接口的时隙捆绑为]{style="font-family:宋体"}[pri set]{lang="FR"}[。]{style="font-family:宋体"}

[**[undo pri-set]{lang="FR"}**]{#struct_0_21171_18224_359295348}[命令用来取消已有的捆绑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1567755958}

[**[pri-set ]{lang="DA"}**]{#struct_0_21171_18224_652270866}[\[ **timeslot-list** *list* \]]{lang="DA"}

[**[undo pri-set]{lang="DA"}**]{#struct_0_21171_18224_x1084507607}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x196722004}

[[不创建任何]{style="font-family:宋体"}]{#struct_0_21171_18224_x1547420398}[pri set]{lang="DA"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1341845518}

[[CE1/PRI]{lang="DA"}]{#struct_0_21171_18224_x298894774}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x520357614}

[[network-admin]{lang="DA"}]{#struct_0_21171_18224_x901411718}

[[mdc-admin]{lang="DA"}]{#struct_0_21171_18224_534668796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x629937005}

[**[timeslot-list]{lang="DA"}**]{#struct_0_21171_18224_x196656468}*[ list]{lang="DA"}*[：]{style="font-family:宋体"}[被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="DA"}*[为时隙]{style="font-family:宋体"}[编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[31]{lang="DA"}[。在指定捆绑的时隙时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以用]{style="font-family:宋体"}*[number]{lang="DA"}*[的形式指定单个时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以用]{style="font-family:宋体"}*[number1-number2]{lang="DA"}*[的形式指定一个范围内的时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[还可以使用]{style="font-family:宋体"}*[number1]{lang="DA"}*[,*number2-number3*]{lang="DA"}[的形式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1524305823}

[[在进行]{style="font-family:宋体"}[pri set]{lang="EN-US"}]{#struct_0_21171_18224_x1913596369}[捆绑时，]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[16]{lang="EN-US"}[时隙将被作为]{style="font-family:宋体"}[D]{lang="EN-US"}[信道使用，因此，这个时隙不能被单独捆绑。如果捆绑的时隙只有一个]{style="font-family:宋体"}[16]{lang="EN-US"}[时隙，捆绑将会失败。]{style="font-family:宋体"}

[[将]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1232148702}[接口时隙捆绑为]{style="font-family:宋体"}[pri set]{lang="EN-US"}[时，]{style="font-family:宋体"}[0]{lang="EN-US"}[时隙被用作传输同步信息，]{style="font-family:宋体"}[16]{lang="EN-US"}[时隙被用作]{style="font-family:宋体"}[D]{lang="EN-US"}[通道传输信令，其余时隙被用作]{style="font-family:宋体"}[B]{lang="EN-US"}[通道传输数据。捆绑时可以将除]{style="font-family:宋体"}[0]{lang="EN-US"}[时隙之外的时隙捆绑为一个]{style="font-family:宋体"}[pri set]{lang="EN-US"}[（]{style="font-family:宋体"}[16]{lang="EN-US"}[时隙作为]{style="font-family:宋体"}[D]{lang="EN-US"}[信道会被自动捆绑）。在捆绑为]{style="font-family:宋体"}[pri set]{lang="EN-US"}[时，如果不指定捆绑的时隙，则为捆绑除]{style="font-family:宋体"}[0]{lang="EN-US"}[时隙外的其它所有时隙。]{style="font-family:宋体"}

[[接口在时隙捆绑以后将自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}]{#struct_0_21171_18224_x291921026}[接口，其逻辑特性与]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[接口相同。]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的名称是]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number***:15**]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*[是]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}]{#struct_0_21171_18224_1229566445}[CE1/PRI]{lang="FR"}[接口上，]{style="font-family:宋体"}[cem set]{lang="DA"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[可以同时使用（]{style="font-family:宋体"}[但]{style="font-family:宋体"}[cem set]{lang="EN-US"}[和]{style="font-family:宋体"}[channel set]{lang="EN-US"}[绑定的组号和时隙不能重复）]{style="font-family:宋体"}[，]{style="font-family:宋体"}[pri set]{lang="DA"}[不能和其它]{style="font-family:宋体"}[方式同时使用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x717207037}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_141706900}[将]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:
宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[时隙捆绑为]{style="font-family:宋体"}[pri set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x196853076}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] pri-set timeslot-list 1,2,8-12]{lang="DA"}[]{#_Toc11588583}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_21171_18224_x538411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_944093596}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_x32534725}
:::

::: {#-1366932403 .myid}
[]{#_Toc404785138}[]{#struct_0_21171_18224_2093190241}[]{#_Toc325038119}[]{#_Toc261964988}[]{#_Toc205607592}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- reset counters controller e1**

------------------------------------------------------------------------

[**[reset counters controller e1]{lang="EN-US"}**]{#struct_0_21171_18224_x332051513}[命令用来清除]{style="font-family:
宋体"}[CE1/PRI]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x761369325}

[**[reset counters controller e1]{lang="EN-US"}**[ \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_21171_18224_x849547069}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_804112938}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x196787540}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1131256543}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1064315947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_709860082}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1945386499}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_2083227728}[：]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的编号。不指定本参数，将清除所有]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_696109182}

[[单独清除]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_895068900}[接口的统计信息只能使用]{style="font-family:宋体"}**[reset counters controller e1]{lang="EN-US"}**[命令，不能使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令，该命令会清除所有接口的统计信息。]{style="font-family:宋体"}

[[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x503631072}[接口的统计信息可以用]{style="font-family:宋体"}**[display controller e1]{lang="EN-US"}**[命令来查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1872662891}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x196459860}[清除]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters controller e1 2/3/0]{lang="EN-US"}]{#struct_0_21171_18224_x723186504}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1161238430}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller e1]{lang="EN-US"}**]{#struct_0_21171_18224_x1941131469}
:::

::: {#-484439771 .myid}
[]{#_Toc404785139}[]{#struct_0_21171_18224_1502072107}[]{#_Toc325038123}[]{#_Toc261964990}[]{#_Toc205607594}[]{#_Toc275246708}[]{#_Toc275250676}[]{#_Toc275246710}[]{#_Toc275250678}[]{#_Toc275246711}[]{#_Toc275250679}[]{#_Toc275246712}[]{#_Toc275250680}[]{#_Toc275246713}[]{#_Toc275250681}[]{#_Toc275246714}[]{#_Toc275250682}[]{#_Toc275246715}[]{#_Toc275250683}[]{#_Toc275246716}[]{#_Toc275250684}[]{#_Toc275246717}[]{#_Toc275250685}[]{#_Toc275246718}[]{#_Toc275250686}[]{#_Toc275246719}[]{#_Toc275250687}[]{#_Toc275246720}[]{#_Toc275250688}[]{#_Toc275246721}[]{#_Toc275250689}[]{#_Toc275246724}[]{#_Toc275250692}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- using (CE1/PRI interface)**

------------------------------------------------------------------------

[**[using]{lang="PT-BR"}**]{#struct_0_21171_18224_409615027}[命令用来设置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口的工作方式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo using]{lang="PT-BR"}**]{#struct_0_21171_18224_193807174}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_622698628}

[**[using ]{lang="PT-BR"}**]{#struct_0_21171_18224_x196394324}[{ **ce1** \| **cem** \| **e1** }]{lang="PT-BR"}

[**[undo using]{lang="PT-BR"}**]{#struct_0_21171_18224_339540018}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1937985703}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x1878733587}[接口的工作方式为]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[工作方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x353368631}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_1636079363}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1210795357}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x2145295718}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x196984151}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x36636429}

[**[ce1]{lang="FR"}**]{#struct_0_21171_18224_1767502680}[：]{style="font-family:宋体"}[接口工作在]{style="font-family:宋体"}[CE1/PRI]{lang="FR"}[工作方式。]{style="font-family:宋体"}

[**[cem]{lang="FR"}**]{#struct_0_21171_18224_944814492}[：]{style="font-family:宋体"}[接口工作在]{style="font-family:宋体"}[CEM]{lang="FR"}[工作方式。]{style="font-family:宋体"}

[**[e1]{lang="PT-BR"}**]{#struct_0_21171_18224_x427279258}[：]{style="font-family:宋体"}[接口工作在]{style="font-family:宋体"}[E1]{lang="PT-BR"}[工作方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1116333532}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_1776930060}[接口有两种工作方式]{style="font-family:宋体"}[：非通道化]{style="font-family:宋体"}[工作方式和]{style="font-family:宋体"}[通道化]{style="font-family:宋体"}[工作方式。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}[非通道化工作方式又分为]{style="font-family:宋体"}[CEM]{lang="PT-BR"}[工作方式和]{style="font-family:宋体"}[E1]{lang="PT-BR"}[工作方式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[通道化工作方式也称为]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[工作方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_21171_18224_944880028}[CE1/PRI]{lang="PT-BR"}[接口使用]{style="font-family:宋体"}[CEM]{lang="PT-BR"}[工作方式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[它将生成一个不分时隙、数据带宽为]{style="font-family:宋体"}[2.048Mbps]{lang="PT-BR"}[的电路仿真接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[接口名是]{lang="EN-US" style="font-family:宋体"}**[circuit-emulation ]{lang="PT-BR"}***[interface-number]{lang="PT-BR"}***[:0]{lang="PT-BR"}**[。其中]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[是]{lang="EN-US" style="font-family:宋体"}[C]{lang="PT-BR"}[E]{lang="PT-BR"}[1/PRI]{lang="PT-BR"}[接口的编号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_21171_18224_66204645}[CE1/PRI]{lang="PT-BR"}[接口使用]{style="font-family:宋体"}[E1]{lang="PT-BR"}[工作方式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[它相当于一个不分时隙、数据带宽为]{style="font-family:宋体"}[2.048Mbps]{lang="PT-BR"}[的接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[其逻辑特性与同步串口相同]{style="font-family:宋体"}[，]{style="font-family:宋体"}[接口名是]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="PT-BR"}**[ *interface-number***:0**]{lang="PT-BR"}[。其中]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[是]{lang="EN-US" style="font-family:宋体"}[C]{lang="PT-BR"}[E]{lang="PT-BR"}[1/PRI]{lang="PT-BR"}[接口的编号]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x1994436402}[CE1/PRI]{lang="EN-US"}[接口使用]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[工作方式时，它在物理上分为]{style="font-family:宋体"}[32]{lang="EN-US"}[个时隙，对应编号为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，其中]{style="font-family:宋体"}[0]{lang="EN-US"}[时隙用于传输同步信息。对该接口有两种使用方法：]{style="font-family:宋体"}[CE1]{lang="EN-US"}[方式和]{style="font-family:宋体"}[PRI]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_395936179}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1508878236}[设置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[的工作在]{style="font-family:宋体"}[E1]{lang="EN-US"}[工作方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_341362620}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] using e1]{lang="EN-US"}
:::

::: {#304204497 .myid}
[]{#_Toc404785140}[]{#struct_0_21171_18224_2038838705}

**WAN接口 \-- CE1/PRI接口基本配置命令 \-- work-mode**

------------------------------------------------------------------------

[**[work-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x875516822}[命令用来配置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口的工作模式]{style="font-family:宋体"}

[**[undo work-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x602882560}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x318306131}

[**[work-mode]{lang="EN-US"}**[ { **async** \| **sync** }]{lang="EN-US"}]{#struct_0_21171_18224_x690044650}

[**[undo ]{lang="EN-US"}[work-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x223217751}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x310932458}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x1531647543}[接口]{style="font-family:宋体"}[工作在同步模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_588525453}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_277100825}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_80511912}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1771593343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_899908645}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1907448689}

[**[async]{lang="EN-US"}**]{#struct_0_21171_18224_1232269651}[：]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[工作在异步模式。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_21171_18224_2136819101}[：]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[工作在同步模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1029322703}

[[CE1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x204792519}[接口支持同步和异步两种工作模式，同步和异步是根据]{style="font-family:宋体"}[POS]{lang="EN-US"}[机的拨号方式来区分的（]{style="font-family:宋体"}[POS]{lang="EN-US"}[机通过设置拨号方式来进行刷卡和升级业务）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_21171_18224_1769146448}[POS]{lang="EN-US"}[机工作在同步拨号方式时，]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口应配置为工作在同步模式，这样，]{style="font-family:宋体"}[POS]{lang="EN-US"}[机会选择]{style="font-family:宋体"}[DHMIM-1E1POS1DM]{lang="EN-US"}[单板上的]{style="font-family:宋体"}[E1POS]{lang="EN-US"}[扣卡（即通过]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口生成的]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口和]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口）进行刷卡交易业务。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x1424355502}[POS]{lang="EN-US"}[机工作在异步拨号方式时，]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口应配置为工作在异步模式，这样，]{style="font-family:宋体"}[POS]{lang="EN-US"}[机会选择]{style="font-family:宋体"}[DHMIM-1E1POS1DM]{lang="EN-US"}[单板上的]{style="font-family:宋体"}[DM]{lang="EN-US"}[扣卡（即通过]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口生成的]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口和]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口）进行]{style="font-family:宋体"}[POS]{lang="EN-US"}[机升级业务。]{style="font-family:宋体"}

[[需要注意的是，只有]{style="font-family:宋体"}[DHMIM-1E1POS1DM]{lang="EN-US"}]{#struct_0_21171_18224_922411419}[单板上的]{style="font-family:宋体"}[CE1/PRI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[（该]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口的]{style="font-family:宋体"}[物理类型为]{style="font-family:宋体"}[PHY_E1POSDM]{lang="EN-US"}[）]{style="font-family:宋体"}[支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x422871194}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x70355330}[配置]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[E1 2/3/0]{lang="EN-US"}[工作在异步模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1496613704}

[\[Sysname\] controller e1 2/3/0]{lang="EN-US"}

[\[Sysname-E1 2/3/0\] ]{lang="PT-BR"}[work-mode async]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2128757399}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pri-set]{lang="EN-US"}**]{#struct_0_21171_18224_x517747471}
:::

::: {#1803826116 .myid}
[]{#_Toc404785142}[]{#struct_0_21171_18224_x506791837}[]{#_Toc325119316}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- alarm-detect**

------------------------------------------------------------------------

[**[alarm-detect]{lang="PT-BR"}**]{#struct_0_21171_18224_940402204}[命令用来配置检测远端告警信号。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_21171_18224_x1465624512}**[alarm-detect]{lang="PT-BR"}**[命令用来取消检测远端告警信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x197115223}

[**[alarm-detect rai]{lang="PT-BR"}**]{#struct_0_21171_18224_x396590223}

[**[undo alarm-detect rai]{lang="PT-BR"}**]{#struct_0_21171_18224_x170842620}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x291115973}

[[检测远端告警信号。]{style="font-family:宋体"}]{#struct_0_21171_18224_x319388818}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_165246741}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_1651242064}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x604226530}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x197049687}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_449186758}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x856967467}

[**[rai]{lang="PT-BR"}**]{#struct_0_21171_18224_323928747}[：]{style="font-family:宋体"}[Remote Alarm Indication]{lang="PT-BR"}[，]{style="font-family:宋体"}[即远端告警指示信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_2137042563}

[[在接口帧格式采用]{style="font-family:宋体"}**[esf]{lang="EN-US"}**]{#struct_0_21171_18224_x95489578}[的情况下，可以使用该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1300124658}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1135861732}[配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[检测远端告警信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x196722007}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] alarm-detect rai]{lang="PT-BR"}
:::

::: {#-848994222 .myid}
[]{#_Toc404785143}[]{#struct_0_21171_18224_x1547223790}[]{#_Toc325119317}[]{#_Toc319999921}[]{#_Toc261964993}[]{#_Toc205607597}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- alarm-threshold**

------------------------------------------------------------------------

[**[alarm-threshold]{lang="EN-US"}**]{#struct_0_21171_18224_x839797562}[命令用来配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的告警门限值。]{style="font-family:宋体"}

[**[undo alarm-threshold]{lang="EN-US"}**]{#struct_0_21171_18224_480806115}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_2114159487}

[**[alarm-threshold ]{lang="EN-US"}**[{ **ais** { **level-1 \| level-2** } **\| lfa** { **level-1 \| level-2 \| level-3 \| level-4** } **\| los** { **pulse-detection \| pulse-recovery** } *value* }]{lang="EN-US"}]{#struct_0_21171_18224_x538892152}

[**[undo alarm-threshold ]{lang="EN-US"}**[{ **ais \| lfa \| los** { **pulse-detection \| pulse-recovery** } }]{lang="EN-US"}]{#struct_0_21171_18224_567397449}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x657590946}

[[对于]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_21171_18224_x196656471}[告警，缺省值为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_21171_18224_1523715998}[告警，缺省值为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_21171_18224_553178548}[告警，]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[参数的值为]{style="font-family:宋体"}[176]{lang="EN-US"}[，]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[的值为]{style="font-family:宋体"}[22]{lang="EN-US"}[，即如果在]{style="font-family:宋体"}[176]{lang="EN-US"}[个脉冲周期内检测到的脉冲数小于]{style="font-family:宋体"}[22]{lang="EN-US"}[个则认为载波丢失，]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警产生。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x779698770}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1607311893}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x392472724}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x275235599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x887070811}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x196853079}

[**[ais]{lang="EN-US"}**]{#struct_0_21171_18224_51413}[：]{style="font-family:宋体"}[AIS]{lang="EN-US"}[（]{style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，告警指示信号）告警的门限值。]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警有两个门限值，分别为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[和]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[。]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[的门限为在一个]{style="font-family:宋体"}[SF/ESF]{lang="EN-US"}[帧内，比特流中的]{style="font-family:宋体"}[0]{lang="EN-US"}[的个数小等于]{style="font-family:宋体"}[2]{lang="EN-US"}[，则]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警产生；]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[的门限在]{style="font-family:宋体"}[SF]{lang="EN-US"}[格式时为，一个]{style="font-family:宋体"}[SF]{lang="EN-US"}[帧内码流的]{style="font-family:宋体"}[0]{lang="EN-US"}[个数小等于]{style="font-family:宋体"}[3]{lang="EN-US"}[；在]{style="font-family:宋体"}[ESF]{lang="EN-US"}[格式时为一个]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧内码流的]{style="font-family:宋体"}[0]{lang="EN-US"}[个数小等于]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lfa]{lang="EN-US"}**]{#struct_0_21171_18224_x1291723782}[：]{style="font-family:宋体"}[LFA]{lang="EN-US"}[（]{style="font-family:宋体"}[Loss of Frame Alignment]{lang="EN-US"}[，帧失步）告警的门限值。]{style="font-family:宋体"}[LFA]{lang="EN-US"}[告警有四个门限值可以配置，分别为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[、]{style="font-family:宋体"}**[level-3]{lang="EN-US"}**[和]{style="font-family:宋体"}**[level-4]{lang="EN-US"}**[。]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[为]{style="font-family:宋体"}[4]{lang="EN-US"}[个帧同步比特中丢失了]{style="font-family:宋体"}[2]{lang="EN-US"}[个；]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[为]{style="font-family:宋体"}[5]{lang="EN-US"}[个帧同步比特中丢失了]{style="font-family:
宋体"}[2]{lang="EN-US"}[个；]{style="font-family:宋体"}**[leve-3]{lang="EN-US"}**[为]{style="font-family:宋体"}[6]{lang="EN-US"}[个帧同步比特中丢失了]{style="font-family:宋体"}[2]{lang="EN-US"}[个；]{style="font-family:宋体"}**[level-4]{lang="EN-US"}**[仅仅对]{style="font-family:宋体"}[ESF]{lang="EN-US"}[格式有效，在连续]{style="font-family:宋体"}[4]{lang="EN-US"}[个]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧中出现错误时产生]{style="font-family:宋体"}[LFA]{lang="EN-US"}[告警。]{style="font-family:宋体"}

[**[los]{lang="EN-US"}**]{#struct_0_21171_18224_x1266637331}[：]{style="font-family:宋体"}[LOS]{lang="EN-US"}[（]{style="font-family:宋体"}[Loss Of Signal]{lang="EN-US"}[，信号丢失）告警的门限值。]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警有两个门限值，分别为]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[和]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[，]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[配置]{style="font-family:宋体"}[LOS]{lang="EN-US"}[的检测时长门限，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[，这个时长门限的单位为"脉冲周期"；]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[配置]{style="font-family:宋体"}[LOS]{lang="EN-US"}[的脉冲门限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[，就是在检测时长内（即]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[配置的若干个脉冲周期内），检测到的脉冲个数如果小于]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[所配置的值，则]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警产生。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1117645881}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1041407300}[将]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警的检测时长配置为]{style="font-family:宋体"}[300]{lang="EN-US"}[个脉冲周期。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x297689585}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] alarm-threshold los pulse-detection 300]{lang="EN-US"}
:::

::: {#-1129875734 .myid}
[]{#_Toc404785144}[]{#struct_0_21171_18224_x1448211204}[]{#_Toc325119318}[]{#_Toc319999922}[]{#_Toc261964994}[]{#_Toc205607598}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- bert (CT1/PRI interface)**

------------------------------------------------------------------------

[**[bert]{lang="EN-US"}**]{#struct_0_21171_18224_x196787543}[命令用来进行线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[**[undo bert]{lang="EN-US"}**]{#struct_0_21171_18224_1131191007}[命令用来取消进行线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1701797791}

[**[bert pattern]{lang="EN-US"}**[ { **2\^20** \| **2\^15** } **time** *minutes* \[ **unframed** \]]{lang="EN-US"}]{#struct_0_21171_18224_x429638374}

[**[undo bert]{lang="EN-US"}**]{#struct_0_21171_18224_x534534541}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1292111883}

[[不进行线路位错误率的测试。]{style="font-family:宋体"}]{#struct_0_21171_18224_x822549525}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_292690602}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x196459863}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x723120968}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_9175250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x414308812}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x164661483}

[**[pattern]{lang="EN-US"}**]{#struct_0_21171_18224_x1872194007}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，包括]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[（测试码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[15]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[）和]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[（测试码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[time ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_21171_18224_x1694301606}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[**[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_2132980721}[：设置测试数据流覆盖帧的开销位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x196394327}

[[ITU O.151]{lang="PT-BR"}]{#struct_0_21171_18224_339605554}[、]{style="font-family:宋体"}[ITU O.153]{lang="PT-BR"}[及]{style="font-family:宋体"}[ANSI T1.403-1999]{lang="PT-BR"}[定义了各种]{style="font-family:宋体"}[BERT]{lang="PT-BR"}[测试模式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[目前]{style="font-family:宋体"}[CT1/PRI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[2\^20]{lang="PT-BR"}[和]{style="font-family:宋体"}[2\^15]{lang="PT-BR"}[两]{style="font-family:宋体"}[种测试模式。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_x2122994184}[测试方式为，本端发出测试数据流，经过线路某处环回来，检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对方设置远端环回等。利用]{style="font-family:宋体"}**[bert]{lang="EN-US"}**[命令配置好测试模式，指定测试时间，开始测试后，可以查看接口状态中的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_66794172}[测试状态和测试结果详见]{style="font-family:宋体"}[CT1]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1471517848}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_716618226}[执行]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_725820251}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] bert pattern 2\^20 time 10]{lang="EN-US"}
:::

::: {#-1843978127 .myid}
[]{#_Toc404785145}[]{#struct_0_21171_18224_1860575762}[]{#_Toc325119319}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- cable (CT1/PRI interface)**

------------------------------------------------------------------------

[**[cable]{lang="EN-US"}**]{#struct_0_21171_18224_x196984150}[命令用来配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口匹配的传输线路类型。]{style="font-family:宋体"}

[**[undo cable]{lang="EN-US"}**]{#struct_0_21171_18224_x36701965}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1062727710}

[**[cable]{lang="EN-US"}**[ { **long** { **0db** \| **-7.5db** \| **-15db** \| **-22.5db** } \| **short** { **133ft** \| **266ft** \| **399ft** \| **533ft** \| **655ft** } }]{lang="EN-US"}]{#struct_0_21171_18224_x1545305175}

[**[undo cable]{lang="EN-US"}**]{#struct_0_21171_18224_x1171780733}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1760035512}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1865518215}[接口匹配的传输线路类型为]{style="font-family:宋体"}**[long]{lang="EN-US"}**[ **0db**]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_454864466}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x196918614}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_396001715}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1139770494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_422183902}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1393019162}

[**[long]{lang="EN-US"}**]{#struct_0_21171_18224_x1030886637}[：匹配]{style="font-family:宋体"}[655]{lang="EN-US"}[英尺以上的传输线路，可选参数有]{style="font-family:宋体"}**[0db]{lang="EN-US"}**[、]{style="font-family:宋体"}**[-7.5db]{lang="EN-US"}**[、]{style="font-family:宋体"}**[-15db]{lang="EN-US"}**[、]{style="font-family:宋体"}**[-22.5db]{lang="EN-US"}**[，可根据接收端信号质量选择不同的衰减参数，当线路质量越差时，信号衰减越大，需要用户对这种衰减进行相应补偿，此时，不需要外接]{style="font-family:宋体"}[CSU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[short]{lang="EN-US"}**]{#struct_0_21171_18224_x1042907212}[：匹配]{style="font-family:宋体"}[655]{lang="EN-US"}[英尺以下的传输线路，可选参数有]{style="font-family:宋体"}**[133ft]{lang="EN-US"}**[、]{style="font-family:宋体"}**[266ft]{lang="EN-US"}**[、]{style="font-family:宋体"}**[399ft]{lang="EN-US"}**[、]{style="font-family:宋体"}**[533ft]{lang="EN-US"}**[、]{style="font-family:宋体"}**[655ft]{lang="EN-US"}**[，可根据传输线路的长度，选择相应的长度参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_850036517}

[[本命令主要作用是配置发送时的信号波形，以适应不同传输需要。实际使用中，可根据接收端收到的信号质量的好坏，来决定是否使用此命令。如果信号质量较好，可以使用缺省设置。使用缺省配置时，]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x197115222}[接口不需外接]{style="font-family:宋体"}[CSU]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x396524687}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1358432134}[配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[匹配的传输线路类型为]{style="font-family:宋体"}[133]{lang="EN-US"}[英尺。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1533924311}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] cable short 133ft]{lang="EN-US"}
:::

::: {#-64286601 .myid}
[]{#_Toc404785146}[]{#struct_0_21171_18224_944224673}[]{#_Toc374365282}[]{#_Toc374191372}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- cem-set (CT1/PRI interface)**

------------------------------------------------------------------------

[**[cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_1640605179}[命令用来将]{style="font-family:宋体"}[CT1/PRI]{lang="FR"}[接口的时隙捆绑为电路仿真组（]{style="font-family:宋体"}[cem set]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[undo cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_1204086205}[命令用来删除已有的电路仿真组]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_610733344}

[**[cem-set ]{lang="EN-US"}***[set-number]{lang="EN-US"}***[ timeslot-list]{lang="EN-US"}***[ list]{lang="EN-US"}*]{#struct_0_21171_18224_1632538923}

[**[undo cem-set]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_21171_18224_944814497}[\[]{lang="IT"}*[ set-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\]]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1553764182}

[[不捆绑任何]{style="font-family:宋体"}[cem set]{lang="EN-US"}]{#struct_0_21171_18224_394220107}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2119585878}

[[CT1/PRI]{lang="FR"}]{#struct_0_21171_18224_944880033}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1959027303}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1209142060}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x281309758}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_944290210}

[*[set-number]{lang="EN-US"}*]{#struct_0_21171_18224_44923281}[：]{style="font-family:宋体"}[该接口上时隙捆绑形成的电路仿真组编号，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_856728438}*[ list]{lang="FR"}*[：被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="EN-US"}*[为时隙编号，其取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。在指定捆绑的时隙时，可以用]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的形式指定单个时隙，也可以用]{style="font-family:宋体"}*[number1-number2]{lang="EN-US"}*[的形式指定一个范围内的时隙，还可以使用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[,*number2*-*number3*]{lang="EN-US"}[的形式，同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x716161014}

[[CT1/PRI]{lang="FR"}]{#struct_0_21171_18224_944355746}[接口使用]{style="font-family:宋体"}[CT1/PRI]{lang="FR"}[工作方式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[它在物理上分为]{style="font-family:宋体"}[24]{lang="FR"}[个时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[对应编号为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[24]{lang="FR"}[。]{style="font-family:
宋体"}

[[使用时，可以将全部时隙分成若干电路仿真组（]{style="font-family:宋体"}[cem set]{lang="EN-US"}]{#struct_0_21171_18224_x330950066}[），每组时隙捆绑后，系统将自动创建一个电路仿真接口。]{style="font-family:宋体"}

[[电路仿真接口]{style="font-family:宋体"}]{#struct_0_21171_18224_126083826}[的名称是]{style="font-family:宋体"}**[circuit-emulation]{lang="FR"}**[ *interface-number***:***set-number*]{lang="FR"}[。其中]{style="font-family:宋体"}*[interface-number]{lang="FR"}*[是]{style="font-family:宋体"}[CT1/PRI]{lang="FR"}[接口的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[set-number]{lang="FR"}*[是]{style="font-family:宋体"}[电路仿真组的]{style="font-family:宋体"}[编号。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}]{#struct_0_21171_18224_2024582642}[CT1]{lang="DA"}[/PRI]{lang="FR"}[接口上，]{style="font-family:宋体"}[cem set]{lang="DA"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[可以同时使用（]{style="font-family:宋体"}[但]{style="font-family:宋体"}[cem set]{lang="FR"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[绑定的组号和时隙不能重复]{style="font-family:宋体"}[），]{style="font-family:宋体"}[pri set]{lang="DA"}[不能和其它]{style="font-family:宋体"}[方式同时使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_944421282}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_741832808}[将]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:
宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[10-15]{lang="EN-US"}[和]{style="font-family:宋体"}[18]{lang="EN-US"}[时隙捆绑为]{style="font-family:宋体"}[0]{lang="EN-US"}[号电路仿真组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x2071752674}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] cem-set 0 timeslot-list 1,2,5,10-15,18]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x600624200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_944486818}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pri-set]{lang="EN-US"}**]{#struct_0_21171_18224_1836058422}
:::

::: {#-565009800 .myid}
[]{#_Toc404785147}[]{#struct_0_21171_18224_1047668961}[]{#_Toc325119320}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- channel-set (CT1/PRI interface)**

------------------------------------------------------------------------

[**[channel-set]{lang="FR"}**]{#struct_0_21171_18224_11135078}[命令用来将]{style="font-family:宋体"}[CT1/PRI]{lang="FR"}[接口的时隙捆绑为通道组]{style="font-family:宋体"}[（]{style="font-family:宋体"}[channel set]{lang="FR"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo channel-set]{lang="FR"}**]{#struct_0_21171_18224_x1693947392}[命令用来取消已有的通道组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x197049686}

[**[channel-set]{lang="IT"}**]{#struct_0_21171_18224_449121222}[ *set-number*]{lang="IT"}[ ]{lang="IT"}**[timeslot-list]{lang="IT"}**[ *list* \[ **speed** { **56k** \| **64k** } \]]{lang="IT"}

[**[undo]{lang="FR"}**]{#struct_0_21171_18224_x1265149256}[ **channel-set** \[ *set-number* \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1600513887}

[[不捆绑任何]{style="font-family:宋体"}]{#struct_0_21171_18224_1832813545}[channel set]{lang="FR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1253476530}

[[CT1/PRI]{lang="FR"}]{#struct_0_21171_18224_329148652}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1993030115}

[[network-admin]{lang="FR"}]{#struct_0_21171_18224_x1976870740}

[[mdc-admin]{lang="FR"}]{#struct_0_21171_18224_x196722006}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1547289326}

[*[set-number]{lang="FR"}*]{#struct_0_21171_18224_x304896018}[：]{style="font-family:宋体"}[该接口上时隙捆绑形成的]{style="font-family:宋体"}[channel set]{lang="FR"}[编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[23]{lang="FR"}[。]{style="font-family:宋体"}

[**[timeslot-list ]{lang="FR"}**]{#struct_0_21171_18224_778296091}*[list]{lang="FR"}*[：]{style="font-family:宋体"}[被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="FR"}*[为时隙编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[24]{lang="FR"}[。在指定捆绑的时隙时]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[可以用]{style="font-family:宋体"}*[number]{lang="FR"}*[的形式指定单个时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以用]{style="font-family:宋体"}*[number1]{lang="FR"}*[-*number2*]{lang="FR"}[的形式指定一个范围内的时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[还可以使用]{style="font-family:宋体"}*[number1]{lang="FR"}*[,*number2*-*number3*]{lang="FR"}[的形式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[同时指定多个时隙。]{style="font-family:宋体"}

[**[speed]{lang="EN-US"}**[ { **56k** \| **64k** }]{lang="EN-US"}]{#struct_0_21171_18224_x1863229741}[：时隙捆绑速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。选用参数]{style="font-family:宋体"}**[56k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[56kbps]{lang="EN-US"}[；选用参数]{style="font-family:宋体"}**[64k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。系统默认为]{style="font-family:宋体"}**[64K]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1115616801}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1495330329}[接口在物理上分为]{style="font-family:宋体"}[24]{lang="EN-US"}[个时隙，对应编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。使用时，可以将全部时隙分成若干通道组（]{style="font-family:宋体"}[channel set]{lang="EN-US"}[），每组时隙捆绑以后，系统将自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，其逻辑特性与同步串口相同。]{style="font-family:宋体"}

[[Serial]{lang="EN-US"}]{#struct_0_21171_18224_x1910220590}[接口的名称是]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *interface-number***:***set-number*]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[是]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的编号，]{style="font-family:宋体"}*[set-number]{lang="EN-US"}*[是]{style="font-family:宋体"}[channel set]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}]{#struct_0_21171_18224_x196656470}[CT1]{lang="DA"}[/PRI]{lang="FR"}[接口上，]{style="font-family:宋体"}[cem set]{lang="DA"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[可以同时使用（]{style="font-family:宋体"}[但]{style="font-family:宋体"}[cem set]{lang="FR"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[绑定的组号和时隙不能重复]{style="font-family:宋体"}[），]{style="font-family:宋体"}[pri set]{lang="DA"}[不能和其它]{style="font-family:宋体"}[方式同时使用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1523781534}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_859809814}[将]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:
宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[10-15]{lang="EN-US"}[和]{style="font-family:宋体"}[18]{lang="EN-US"}[时隙捆绑为]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[channel-set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1883753825}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] channel-set 0 timeslot-list 1,2,5,10-15,18]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x704183688}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_944224674}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pri-set]{lang="EN-US"}**]{#struct_0_21171_18224_1317305403}
:::

::: {#-1202611508 .myid}
[]{#_Toc404785148}[]{#struct_0_21171_18224_825582361}[]{#_Toc325119321}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- clock (CT1/PRI interface)**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_x196853078}[命令用来配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_116949}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1398785453}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_21171_18224_x1118390750}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_1662387788}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1993309149}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1391790791}[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1495572318}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1229483733}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x196787542}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1131125471}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x469381640}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1464494718}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_1601286314}[：主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_x1007022750}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_169447103}

[[当]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_703194000}[接口作为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧使用时，应使用主时钟模式；作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧使用时，应使用从时钟模式。]{style="font-family:宋体"}

[[当两台路由器的]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x196459862}[接口直接相连时，必须使两端分别工作在从时钟模式和主时钟模式。当路由器的]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口与交换机连接时，交换机是]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧，负责提供时钟；而路由器的接口需工作在从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x723055432}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_740926117}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1745911490}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] clock master]{lang="EN-US"}
:::

::: {#552598556 .myid}
[]{#_Toc404785149}[]{#struct_0_21171_18224_x1236289712}[]{#_Toc325119322}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- code (CT1/PRI interface)**

------------------------------------------------------------------------

[**[code]{lang="EN-US"}**]{#struct_0_21171_18224_x1841232850}[命令用来配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的线路编解码格式。]{style="font-family:宋体"}

[**[undo code]{lang="EN-US"}**]{#struct_0_21171_18224_340585973}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1905183888}

[**[code]{lang="EN-US"}**[ { **ami** \| **b8zs** }]{lang="EN-US"}]{#struct_0_21171_18224_x196394326}

[**[undo code]{lang="EN-US"}**]{#struct_0_21171_18224_339671090}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_272584782}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x121261735}[接口的线路编解码格式为]{style="font-family:宋体"}**[b8zs]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x249662130}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1721772119}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1875436365}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1113383948}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x196984153}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x36767501}

[**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_600926348}[：采用]{style="font-family:宋体"}[AMI]{lang="EN-US"}[（]{style="font-family:宋体"}[Alternate Mark Inversion]{lang="EN-US"}[，信号交替反转码）线路编码格式。]{style="font-family:宋体"}

[**[b8zs]{lang="EN-US"}**]{#struct_0_21171_18224_x1869704816}[：采用]{style="font-family:宋体"}[B8ZS]{lang="EN-US"}[（]{style="font-family:宋体"}[Bipolar 8-zero substitution]{lang="EN-US"}[，双极性]{style="font-family:宋体"}[8zero]{lang="EN-US"}[替换码）线路编码格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1718343329}

[[配置接口的线路编解码格式时，请注意与对端设备保持一致。]{style="font-family:宋体"}]{#struct_0_21171_18224_x421484684}

[[线路编码采用]{style="font-family:宋体"}**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_1233923828}[方式时，在该接口上需要同时配置]{style="font-family:宋体"}**[data-coding]{lang="EN-US"}**[ **inverted**]{lang="EN-US"}[，才能保证接口正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1706391411}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x196918617}[配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的线路编解码格式为]{style="font-family:宋体"}**[ami]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_396067251}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] code ami]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1626682561}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[data-coding]{lang="IT"}**]{#struct_0_21171_18224_x505144115}
:::

::: {#-1883381394 .myid}
[]{#_Toc404785150}[]{#struct_0_21171_18224_274776905}[]{#_Toc325119323}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- controller t1**

------------------------------------------------------------------------

[**[controller t1]{lang="EN-US"}**]{#struct_0_21171_18224_x1386721107}[命令用来进入]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1440359404}

[**[controller]{lang="EN-US"}**[ **t1** *interface-number*]{lang="EN-US"}]{#struct_0_21171_18224_931224940}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x197115225}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x396459151}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1275654987}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1918643508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_695687097}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_2088831123}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x118628730}[：]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x792627276}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x197049689}[进入]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_450104262}

[\[Sysname\] controller t1 2/4/0]{lang="PT-BR"}

[\[Sysname-T1 2/4/0\]]{lang="PT-BR"}
:::

::: {#1784736614 .myid}
[]{#_Toc404785151}[]{#struct_0_21171_18224_x1796332110}[]{#_Toc325119324}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- data-coding (CT1/PRI interface)**

------------------------------------------------------------------------

[**[data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_x936770996}[命令用来设置]{style="font-family:宋体"}[CT1/PRI]{lang="PT-BR"}[接口是否对用户数据进行翻转。]{style="font-family:宋体"}

[**[undo data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_x1921064257}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x932392412}

[**[data-coding]{lang="IT"}**]{#struct_0_21171_18224_1447218025}[ { **inverted** \| **normal** }]{lang="IT"}

[**[undo data-coding]{lang="IT"}**]{#struct_0_21171_18224_546302190}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x196722009}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x1547617006}[接口不对用户数据进行翻转。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_518561572}

[[CT1/PRI]{lang="IT"}]{#struct_0_21171_18224_x1613844935}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1030071106}

[[network-admin]{lang="IT"}]{#struct_0_21171_18224_70557824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_712321875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1591165197}

[**[inverted]{lang="IT"}**]{#struct_0_21171_18224_x196656473}[：]{style="font-family:宋体"}[对用户数据进行翻转。]{style="font-family:宋体"}

[**[normal]{lang="PT-BR"}**]{#struct_0_21171_18224_1523847070}[：]{style="font-family:宋体"}[不对用户数据进行翻转。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1303494211}

[[HDLC]{lang="EN-US"}]{#struct_0_21171_18224_2075456977}[协议为了防止有效数据中的]{style="font-family:宋体"}[7e]{lang="EN-US"}[被当作填充符，会在连续]{style="font-family:宋体"}[5]{lang="EN-US"}[个]{style="font-family:宋体"}[1]{lang="EN-US"}[后插入一个]{style="font-family:
宋体"}[0]{lang="EN-US"}[。然后可以进行数据翻转，数据翻转后，]{style="font-family:宋体"}[0]{lang="EN-US"}[变成]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[变成]{style="font-family:
宋体"}[0]{lang="EN-US"}[。数据翻转的作用是：当]{style="font-family:宋体"}[T1]{lang="EN-US"}[接口配置为]{style="font-family:宋体"}[AMI]{lang="EN-US"}[编码时，能保证每]{style="font-family:宋体"}[8]{lang="EN-US"}[个连续比特中至少有一个]{style="font-family:宋体"}[1]{lang="EN-US"}[，从而弥补]{style="font-family:宋体"}[AMI]{lang="EN-US"}[码中易出现过多连]{style="font-family:宋体"}[0]{lang="EN-US"}[的缺陷。]{style="font-family:宋体"}

[[需注意的是，只有通信的]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_21171_18224_841278635}[线路两端的]{style="font-family:宋体"}[CT1/PRI]{lang="PT-BR"}[接口保持一致（都进行翻转或都不进行数据翻转），才能正常通信。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_309200860}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1456166061}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[对用户数据进行翻转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x196853081}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] data-coding inverted]{lang="IT"}
:::

::: {#-1845900351 .myid}
[]{#_Toc404785152}[]{#struct_0_21171_18224_x472864}[]{#_Toc325119326}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- display controller t1**

------------------------------------------------------------------------

[**[display controller t1]{lang="EN-US"}**]{#struct_0_21171_18224_1507784242}[命令用来显示]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1828784656}

[**[display controller]{lang="EN-US"}**[ **t1** \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_21171_18224_x1273367377}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1372927351}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_447595829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_979401178}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1097858655}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_x196787545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1131584223}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_x910212598}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1457907900}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1235881043}[：]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的编号。不指定本参数，将显示所有]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1367699663}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x885566546}[显示]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller t1 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x196984152}

[T1 2/4/0]{lang="EN-US"}

[Current state: DOWN]{lang="EN-US"}

[Description: T1 2/4/0 Interface]{lang="EN-US"}

[Basic Configuration:]{lang="EN-US"}

[  Work mode: T1 framed, Cable type: 100 Ohm balanced]{lang="EN-US"}

[  Frame-format: esf, fdl: none, Line code: b8zs]{lang="EN-US"}

[  Source clock: slave, Data-coding: normal]{lang="EN-US"}

[  Idle code: ff, Itf type: ff, Itf number: 2]{lang="EN-US"}

[  Loop back: not set]{lang="EN-US"}

[Alarm State:]{lang="EN-US"}

[  Receiver alarm state is Loss-of-Signal]{lang="EN-US"}

[  Transmitter is sending remote alarm]{lang="EN-US"}

[  Pulse density violation detected]{lang="EN-US"}

[SendLoopCode History:]{lang="EN-US"}

[  Inband-llb-up: 0 times, Inband-llb-down: 0 times]{lang="EN-US"}

[  Fdl-ansi-llb-up: 0 times, Fdl-ansi-llb-down: 0 times]{lang="EN-US"}

[  Fdl-ansi-plb-up: 0 times, Fdl-ansi-plb-down: 0 times]{lang="EN-US"}

[  Fdl-att-plb-up: 0 times, Fdl-att-plb-down: 0 times]{lang="EN-US"}

[BERT state:(stopped, not completed)]{lang="EN-US"}

[  Test pattern: 2\^15, Status: Not Sync, Sync Detected: 0]{lang="EN-US"}

[    Time: 0 minutes, Time past: 0 minutes]{lang="EN-US"}

[    Bit Errors (since test started): 0 bits]{lang="EN-US"}

[    Bits Received (since test started): 0 Kbits]{lang="EN-US"}

[    Bit Errors (since latest sync): 0 bits]{lang="EN-US"}

[    Bits Received (since latest sync): 0 Kbits]{lang="EN-US"}

[Historical Statistics:]{lang="EN-US"}

[Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[  Data in current interval (285 seconds elapsed):]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm: 286 seconds]{lang="EN-US"}

[    Slip: 7 seconds, Fr Loss: 286 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 286 seconds]{lang="EN-US"}

[  Data in Interval 1:]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm Secs: 901 seconds]{lang="EN-US"}

[    Slip: 22 seconds, Fr Loss: 901 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 901 seconds]{lang="EN-US"}

[  Data in Interval 2:]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0 ]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm: 900 seconds]{lang="EN-US"}

[    Slip: 23 seconds, Fr Loss: 900 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 900 seconds]{lang="EN-US"}

[  Total Data (last 2 15 minute intervals):]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0 ]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm: 2087 seconds]{lang="EN-US"}

[    Slip: 52 seconds, Fr Loss: 2087 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 2087 seconds]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display controller e1]{lang="EN-US"}]{#struct_0_21171_18224_x36833037}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1643478386}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_1603150058}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_84222925}

[[T1 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_1765215780}

[[Current state]{lang="EN-US"}]{#struct_0_21171_18224_x1149330676}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_332898194}[接口当前的状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_x196918616}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_396132787}[接口的描述信息]{style="font-family:宋体"}

[[Basic Configuration]{lang="EN-US"}]{#struct_0_21171_18224_77691681}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_1970904690}[接口基本配置]{style="font-family:宋体"}

[[Work mode]{lang="EN-US"}]{#struct_0_21171_18224_1375798869}

[[T1]{lang="FR"}]{#struct_0_21171_18224_x197115224}[接口的工作模式]{style="font-family:宋体"}[（]{style="font-family:宋体"}[T1/CT1]{lang="FR"}[）]{style="font-family:宋体"}

[[Cable type]{lang="EN-US"}]{#struct_0_21171_18224_x396393615}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_996984820}[接口的线缆类型]{style="font-family:宋体"}

[[Frame-format]{lang="EN-US"}]{#struct_0_21171_18224_1099287940}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_x1189491314}[接口的帧格式（]{style="font-family:宋体"}[esf/sf]{lang="EN-US"}[）]{style="font-family:宋体"}

[[fdl]{lang="EN-US"}]{#struct_0_21171_18224_x197049688}

[[FDL]{lang="SV"}]{#struct_0_21171_18224_450038726}[格式（]{style="font-family:宋体"}[ansi/att/none]{lang="SV"}[）]{style="font-family:宋体"}

[[Line code]{lang="EN-US"}]{#struct_0_21171_18224_x1846776686}

[[线路编码格式（]{style="font-family:宋体"}[b8zs/ami]{lang="EN-US"}]{#struct_0_21171_18224_1289565938}[）]{style="font-family:宋体"}

[[Source clock]{lang="EN-US"}]{#struct_0_21171_18224_x196722008}

[[接口的时钟源模式（]{style="font-family:宋体"}[master/slave]{lang="EN-US"}]{#struct_0_21171_18224_x1547682542}[）]{style="font-family:宋体"}

[[Data-coding]{lang="EN-US"}]{#struct_0_21171_18224_986502524}

[[包括正常和数据翻转两种模式（]{style="font-family:宋体"}[normal/inverted]{lang="EN-US"}]{#struct_0_21171_18224_1563277407}[）]{style="font-family:宋体"}

[[Idle code]{lang="EN-US"}]{#struct_0_21171_18224_x196656472}

[[空闲码（]{style="font-family:宋体"}[7e/ff]{lang="EN-US"}]{#struct_0_21171_18224_1523912606}[）]{style="font-family:宋体"}

[[Itf type]{lang="EN-US"}]{#struct_0_21171_18224_1267407854}

[[帧间填充码（]{style="font-family:宋体"}[7e/ff]{lang="EN-US"}]{#struct_0_21171_18224_x790854784}[）]{style="font-family:宋体"}

[[Itf number ]{lang="EN-US"}]{#struct_0_21171_18224_1883830556}

[[帧间填充码的个数]{style="font-family:宋体"}]{#struct_0_21171_18224_x196853080}

[[Loop back]{lang="EN-US"}]{#struct_0_21171_18224_x407328}

[[接口是否设置了环回（]{style="font-family:宋体"}[local/payload/remote/no set]{lang="EN-US"}]{#struct_0_21171_18224_x249383044}[）]{style="font-family:宋体"}

[[Alarm State]{lang="EN-US"}]{#struct_0_21171_18224_x1813341098}

[[告警状态]{style="font-family:宋体"}]{#struct_0_21171_18224_x196787544}

[[Receiver alarm state is Loss-of-Signal]{lang="EN-US"}]{#struct_0_21171_18224_1131518687}

[[收到的告警类型：]{style="font-family:宋体"}[none]{lang="EN-US"}]{#struct_0_21171_18224_1018280280}[、]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}

[[Transmitter is sending remote alarm]{lang="EN-US"}]{#struct_0_21171_18224_x196459864}

[[发出的告警类型：]{style="font-family:宋体"}[RAI]{lang="EN-US"}]{#struct_0_21171_18224_x723448648}[、]{style="font-family:宋体"}[none]{lang="EN-US"}

[[Pulse density violation detected]{lang="EN-US"}]{#struct_0_21171_18224_316450355}

[[脉冲密度不符合规范要求]{style="font-family:宋体"}]{#struct_0_21171_18224_1630251389}

[[SendLoopCode History:]{lang="EN-US"}]{#struct_0_21171_18224_x196394328}

[[  Inband-llb-up: 0 times, Inband-llb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_339802162}

[[  Fdl-ansi-llb-up: 0 times, Fdl-ansi-llb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_478272398}

[[  Fdl-ansi-plb-up: 0 times, Fdl-ansi-plb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_1369099792}

[[  Fdl-att-plb-up: 0 times, Fdl-att-plb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_70460294}

[[向对端发送环回码的历史记录，包括每种码的发送次数和最近发送的是哪种码]{style="font-family:宋体"}]{#struct_0_21171_18224_x1154528058}

[[BERT state]{lang="EN-US"}]{#struct_0_21171_18224_424390827}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_1369165328}[测试状态：]{style="font-family:宋体"}[completed]{lang="EN-US"}[（自然完成）还是]{style="font-family:宋体"}[stopped]{lang="EN-US"}[（人为中止）还是]{style="font-family:宋体"}[running]{lang="EN-US"}[（正在测试）]{style="font-family:宋体"}

[[Test pattern]{lang="EN-US"}]{#struct_0_21171_18224_x752510286}

[[测试模式（]{style="font-family:宋体"}]{#struct_0_21171_18224_199750257}[2\^20/2\^15]{lang="DE"}[）]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_21171_18224_1368968720}

[[是否处于同步状态]{style="font-family:宋体"}]{#struct_0_21171_18224_496217547}

[[Sync Detected]{lang="EN-US"}]{#struct_0_21171_18224_x847477396}

[[测试以来检测到的同步次数]{style="font-family:宋体"}]{#struct_0_21171_18224_1369034256}

[[Time]{lang="EN-US"}]{#struct_0_21171_18224_x1157355973}

[[预设的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_x1976113653}

[[Time past]{lang="EN-US"}]{#struct_0_21171_18224_1369361936}

[[已经过去的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_x1930442611}

[[Bit Errors (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_x582408681}

[[测试以来收到的错误的比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_1369427472}

[[Bits Received (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_1593672578}

[[测试以来收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_1138585391}

[[Bit Errors (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_1369230864}

[[最近的同步以来收到的错误的比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_1958892560}

[[Bits Received (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_x1983497511}

[[最近的同步以来收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_1369296400}

[[Historical Statistics]{lang="EN-US"}]{#struct_0_21171_18224_x1152315472}

[[历史信息]{style="font-family:宋体"}]{#struct_0_21171_18224_154620082}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_338668108}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_1904752049}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_x892126633}

[[清零记录]{style="font-family:宋体"}]{#struct_0_21171_18224_x1533204994}

[[  Data in current interval (285 seconds elapsed):]{lang="EN-US"}]{#struct_0_21171_18224_1369689616}

[[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}]{#struct_0_21171_18224_x1881070772}

[[    Ais Alarm: 0 seconds, Los Alarm: 286 seconds]{lang="EN-US"}]{#struct_0_21171_18224_2045731770}

[[    Slip: 7 seconds, Fr Loss: 286 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1369099793}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_70394758}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x1266303603}

[[    Severely Err: 0 seconds, Unavail: 286 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1369165329}

[[当前时间间隔内的统计信息（]{style="font-family:宋体"}[15]{lang="EN-US"}]{#struct_0_21171_18224_x752444750}[分钟为一个时间间隔）。这些数据是按照]{style="font-family:宋体"}[T1]{lang="EN-US"}[规范对物理层所作的各种信息统计，如]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警、]{style="font-family:宋体"}[LOS]{lang="EN-US"}[信号、]{style="font-family:宋体"}[LFA]{lang="EN-US"}[等。详细解释参见]{style="font-family:宋体"}[T1]{lang="EN-US"}[规范]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[和]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}

[[  Data in Interval 1:]{lang="EN-US"}]{#struct_0_21171_18224_1368968721}

[[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}]{#struct_0_21171_18224_496283083}

[[    Ais Alarm: 0 seconds, Los Alarm Secs: 901 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1931951456}

[[    Slip: 22 seconds, Fr Loss: 901 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1369034257}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_x1157421509}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1369361937}

[[    Severely Err: 0 seconds, Unavail: 901 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x1930377075}

[[第]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_21171_18224_x1172324570}[间隔内的统计信息]{style="font-family:宋体"}

[[统计内容同上]{style="font-family:宋体"}]{#struct_0_21171_18224_1369427473}

[[  Data in Interval 2:]{lang="EN-US"}]{#struct_0_21171_18224_1593738114}

[[    Line Code Violations: 0, Path Code Violations: 0 ]{lang="EN-US"}]{#struct_0_21171_18224_1369230865}

[[    Ais Alarm: 0 seconds, Los Alarm: 900 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1958827024}

[[    Slip: 23 seconds, Fr Loss: 900 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1369296401}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_x1152381008}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1671345703}

[[    Severely Err: 0 seconds, Unavail: 900 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1369624081}

[[第]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_21171_18224_x1533139458}[间隔内的统计信息]{style="font-family:宋体"}

[[统计内容同上]{style="font-family:宋体"}]{#struct_0_21171_18224_1369689617}

[[  Total Data (last 2 15 minute intervals):]{lang="EN-US"}]{#struct_0_21171_18224_x1881005236}

[[    Line Code Violations: 0, Path Code Violations: 0 ]{lang="EN-US"}]{#struct_0_21171_18224_1369099790}

[[    Ais Alarm: 0 seconds, Los Alarm: 2087 seconds]{lang="EN-US"}]{#struct_0_21171_18224_70591366}

[[    Slip: 52 seconds, Fr Loss: 2087 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1369165326}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_x751854926}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x1572069214}

[[    Severely Err: 0 seconds, Unavail: 2087 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1368968718}

[[所有间隔内的统计信息]{style="font-family:宋体"}]{#struct_0_21171_18224_495693262}

[[统计内容同上]{style="font-family:宋体"}]{#struct_0_21171_18224_1369034254}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1157487045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters controller ]{lang="EN-US"}**]{#struct_0_21171_18224_457839805}**[t]{lang="EN-US"}[1]{lang="EN-US"}**

::: {#-1385453608 .myid}
[]{#_Toc404785153}[]{#struct_0_21171_18224_438860553}[]{#_Toc325119327}[]{#_Toc319999934}[]{#_Toc261965007}[]{#_Toc205607611}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- fdl**

------------------------------------------------------------------------

[**[fdl]{lang="EN-US"}**]{#struct_0_21171_18224_1093052991}[命令用来配置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口在]{style="font-family:宋体"}[ESF]{lang="EN-US"}[格式时]{style="font-family:宋体"}[FDL]{lang="EN-US"}[比特位的使用模式。]{style="font-family:宋体"}

[**[undo fdl]{lang="EN-US"}**]{#struct_0_21171_18224_x676892818}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1369361934}

[**[fdl]{lang="EN-US"}**[ { **ansi** \| **att** \| **both** \| **none** }]{lang="EN-US"}]{#struct_0_21171_18224_x1930311539}

[**[undo fdl]{lang="EN-US"}**]{#struct_0_21171_18224_1346886847}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1398896848}

[[禁止]{style="font-family:宋体"}[FDL]{lang="EN-US"}]{#struct_0_21171_18224_x165777355}[（]{style="font-family:宋体"}**[none]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x327659103}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1155603213}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2089207549}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_686999676}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1369427470}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1593803650}

[**[ansi]{lang="EN-US"}**]{#struct_0_21171_18224_359922136}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，遵循]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[att]{lang="EN-US"}**]{#struct_0_21171_18224_318888779}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，遵循]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_21171_18224_x326644912}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，同时遵循]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_21171_18224_x1884475603}[：禁止]{style="font-family:宋体"}[FDL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_872470755}

[[FDL]{lang="EN-US"}]{#struct_0_21171_18224_1369230862}[（]{style="font-family:宋体"}[Facility Data Link]{lang="EN-US"}[，设备数据链路）是]{style="font-family:宋体"}[T1]{lang="EN-US"}[的]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧格式中]{style="font-family:宋体"}[4kbps]{lang="EN-US"}[的一个带宽，]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口在配置为]{style="font-family:宋体"}[ESF]{lang="EN-US"}[（]{style="font-family:宋体"}[Extended Super Frame]{lang="EN-US"}[，扩展超帧）格式时，其中的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[位可用来传递报警信息、性能信息及环回码等，相关的规范包括]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[和]{style="font-family:宋体"}[ATT TR 54016]{lang="EN-US"}[。在实际应用中，经常需要对]{style="font-family:宋体"}[FDL]{lang="EN-US"}[的使用及规范进行各种配置，包括：禁止]{style="font-family:宋体"}[FDL]{lang="EN-US"}[、使能并遵循]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范、使能并遵循]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范或者使能并遵循这两种规范。]{style="font-family:宋体"}

[[实际应用中，可以根据对方]{style="font-family:宋体"}[FDL]{lang="EN-US"}]{#struct_0_21171_18224_1959285776}[的模式调整本端]{style="font-family:宋体"}[FDL]{lang="EN-US"}[的模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x798106035}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_943787736}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0 FDL]{lang="EN-US"}[使能并遵循]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x536291872}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] fdl att]{lang="EN-US"}
:::

::: {#-2112243338 .myid}
[]{#_Toc404785154}[]{#struct_0_21171_18224_799567184}[]{#_Toc325119328}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- frame-format (CT1/PRI interface)**

------------------------------------------------------------------------

[**[frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_656394594}[命令用来设置]{style="font-family:宋体"}[CT1/PRI]{lang="PT-BR"}[接口的帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_356089336}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1369296398}

[**[frame-format ]{lang="IT"}**]{#struct_0_21171_18224_1950486439}[{ **esf** \| **sf** }]{lang="IT"}

[**[undo frame-format]{lang="IT"}**]{#struct_0_21171_18224_538274028}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1983092979}

[[CT1/PRI]{lang="SV"}]{#struct_0_21171_18224_1978001192}[接口的帧格式为]{style="font-family:宋体"}**[esf]{lang="SV"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1208270947}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_280372272}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2118504938}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_1369624078}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x1532680721}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_170930820}

[**[esf]{lang="IT"}**]{#struct_0_21171_18224_1737410788}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="IT"}[接口的帧格式为]{style="font-family:宋体"}[ESF]{lang="IT"}[（]{style="font-family:宋体"}[Extended Super Frame]{lang="IT"}[，]{style="font-family:宋体"}[扩展超帧]{style="font-family:宋体"}[）]{style="font-family:宋体"}[格式。]{style="font-family:宋体"}

[**[sf]{lang="IT"}**]{#struct_0_21171_18224_x2065951586}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="IT"}[接口的帧格式为]{style="font-family:宋体"}[SF]{lang="IT"}[（]{style="font-family:宋体"}[Super Frame]{lang="IT"}[，]{style="font-family:宋体"}[超帧]{style="font-family:宋体"}[）]{style="font-family:宋体"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_2014530289}

[[CT1/PRI]{lang="SV"}]{#struct_0_21171_18224_904919231}[接口支持超帧和扩展超帧两种帧格式。在超帧格式中，多个帧可以共享相同的帧同步信息和信令信息，从而有更多的有效位来传送用户数据。实际应用中，经常需要对系统进行测试，扩展超帧技术可以用来满足在测试时不影响正常业务运行的要求。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2062059382}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1369689614}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的帧格式为超帧格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1881201844}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] ]{lang="EN-US"}[frame-format sf]{lang="FR"}
:::

::: {#-493725245 .myid}
[]{#_Toc404785155}[]{#struct_0_21171_18224_x1169405372}[]{#_Toc325119329}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- idle-code (CT1/PRI interface)**

------------------------------------------------------------------------

[**[idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_1328165623}[命令用来设置]{style="font-family:宋体"}[CT1/PRI]{lang="PT-BR"}[接口的线路空闲码类型]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x518334994}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x733961026}

[**[idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x1858572706}[ { **7e** \| **ff** }]{lang="PT-BR"}

[**[undo idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_1369099791}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_70525830}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_461944506}[接口的线路空闲码类型为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_2117947004}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_561081334}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1606052637}

[[network-admin]{lang="PT-BR"}]{#struct_0_21171_18224_347780733}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_21171_18224_x751209951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1605754336}

[**[7e]{lang="PT-BR"}**]{#struct_0_21171_18224_1369165327}[：]{style="font-family:宋体"}[线路空闲码为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[类型。]{style="font-family:宋体"}

[**[ff]{lang="PT-BR"}**]{#struct_0_21171_18224_x751789390}[：]{style="font-family:宋体"}[线路空闲码为]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_323166959}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x71025393}[接口的线路空闲码类型是指在没有被绑定到逻辑通道的时隙上发送的码型。]{style="font-family:宋体"}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_1319138344}[接口的线路空闲码类型有两种]{style="font-family:宋体"}[：]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[和]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_980396514}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x587167258}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的线路空闲码类型为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1368968719}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] idle-code 7e]{lang="EN-US"}
:::

::: {#-1048962882 .myid}
[]{#_Toc404785156}[]{#struct_0_21171_18224_495758798}[]{#_Toc325119330}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- itf (CT1/PRI interface)**

------------------------------------------------------------------------

[**[itf]{lang="PT-BR"}**]{#struct_0_21171_18224_x644292628}[命令用来设置]{style="font-family:宋体"}[CT1/PRI]{lang="PT-BR"}[接口的帧间填充符类型和个数。]{style="font-family:宋体"}

[**[undo itf]{lang="PT-BR"}**]{#struct_0_21171_18224_x1800984717}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_33193643}

[**[itf ]{lang="PT-BR"}**]{#struct_0_21171_18224_x1394751599}[{ **number** *number* \| **type** { **7e** \| **ff** } }]{lang="PT-BR"}

[**[undo itf ]{lang="PT-BR"}**]{#struct_0_21171_18224_x615324419}[{ **number** \| **type** }]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_449946822}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_1369034255}[接口的帧间填充符类型为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[，帧间填充字节个数为]{style="font-family:宋体"}[4]{lang="PT-BR"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1157552581}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x691941579}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2139337195}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_514632237}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1042827718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_349633478}

[**[number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_21171_18224_1046618686}[：设置帧间填充字节的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[14]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**]{#struct_0_21171_18224_1369361935}[：设置帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型。]{style="font-family:宋体"}

[**[7e]{lang="EN-US"}**]{#struct_0_21171_18224_x1315901756}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[**[ff]{lang="EN-US"}**]{#struct_0_21171_18224_x1315967292}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1930246003}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_2027109603}[接口的帧间填充符是指已经被绑定到逻辑通道的时隙在没有发送业务数据时发送的码型。]{style="font-family:宋体"}

[[CT1/PRI]{lang="PT-BR"}]{#struct_0_21171_18224_x1597489039}[接口的帧间填充符类型有两种：]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[和]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1659119576}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x786528969}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1671520264}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] itf type ff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1612678059}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的帧间填充字节个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1369427471}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] itf number 5]{lang="EN-US"}
:::

::: {#414645470 .myid}
[]{#_Toc404785157}[]{#struct_0_21171_18224_1593869186}[]{#_Toc325119331}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- loopback (CT1/PRI interfacei)**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1541652935}[命令用来开启]{style="font-family:宋体"}[CT1/PR]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_1799912418}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1368101298}

[**[loopback]{lang="EN-US"}**[ { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_21171_18224_1945536045}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_1308264333}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_494663317}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_1369230863}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1959220240}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1243339433}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_18315010}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1855942464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1358688435}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_817351076}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_x1208070583}[：设置接口对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_1369296399}[：设置接口对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_1950420903}[：设置接口对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1293362317}

[[自环环回功能主要用于检测接口或电缆本身的状况，正常工作时应关闭这些功能。]{style="font-family:宋体"}]{#struct_0_21171_18224_333213595}

[[对于将]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_431605112}[接口时隙经捆绑而形成的串口，如果串口的链路层协议配置为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[，在设置自环后，其链路层协议状态将上报为]{style="font-family:宋体"}[down]{lang="EN-US"}[，这属于正常情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_822442885}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1606880806}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1369624079}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] loopback local]{lang="EN-US"}
:::

::: {#-192704281 .myid}
[]{#_Toc404785158}[]{#struct_0_21171_18224_x1532615185}[]{#_Toc325119332}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- pri-set (CT1/PRI interface)**

------------------------------------------------------------------------

[**[pri-set]{lang="FR"}**]{#struct_0_21171_18224_776945805}[命令用来将]{style="font-family:宋体"}[CT1/PRI]{lang="FR"}[接口的时隙捆绑为]{style="font-family:宋体"}[pri set]{lang="FR"}[。]{style="font-family:宋体"}

[**[undo pri-set]{lang="FR"}**]{#struct_0_21171_18224_x215182202}[命令用来取消已有的捆绑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1137699044}

[**[pri-set ]{lang="DA"}**]{#struct_0_21171_18224_x542292718}[\[ **timeslot-list** *list* \]]{lang="DA"}

[**[undo pri-set]{lang="DA"}**]{#struct_0_21171_18224_x566155402}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_442263495}

[[不创建任何]{style="font-family:宋体"}]{#struct_0_21171_18224_1369689615}[pri set]{lang="DA"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1881136308}

[[CT1/PRI]{lang="DA"}]{#struct_0_21171_18224_x981907164}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_336765722}

[[network-admin]{lang="DA"}]{#struct_0_21171_18224_1385724875}

[[mdc-admin]{lang="DA"}]{#struct_0_21171_18224_x527414908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1418538731}

[**[timeslot-list]{lang="DA"}**]{#struct_0_21171_18224_x878925479}*[ list]{lang="DA"}*[：]{style="font-family:宋体"}[被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="DA"}*[为时隙]{style="font-family:宋体"}[编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[24]{lang="DA"}[。在指定捆绑的时隙时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以用]{style="font-family:宋体"}[number]{lang="DA"}[的形式指定单个时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以用]{style="font-family:宋体"}[number1-number2]{lang="DA"}[的形式指定一个范围内的时隙]{style="font-family:宋体"}[，]{style="font-family:宋体"}[还可以使用]{style="font-family:宋体"}[number1,number2-number3]{lang="DA"}[的形式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_636575920}

[[在进行]{style="font-family:宋体"}[pri set]{lang="EN-US"}]{#struct_0_21171_18224_1369099788}[捆绑时，]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[24]{lang="EN-US"}[时隙将被作为]{style="font-family:宋体"}[D]{lang="EN-US"}[信道使用，因此，这个时隙不能被单独捆绑。如果捆绑的时隙只有一个]{style="font-family:宋体"}[24]{lang="EN-US"}[时隙，捆绑将会失败。]{style="font-family:宋体"}

[[将]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_70067079}[接口时隙捆绑为]{style="font-family:宋体"}[pri set]{lang="EN-US"}[时，]{style="font-family:宋体"}[24]{lang="EN-US"}[时隙被用作]{style="font-family:宋体"}[D]{lang="EN-US"}[通道传输信令，其余时隙被用作]{style="font-family:宋体"}[B]{lang="EN-US"}[通道传输数据。捆绑时可以将任意时隙捆绑为一个]{style="font-family:宋体"}[pri set]{lang="EN-US"}[（]{style="font-family:宋体"}[24]{lang="EN-US"}[时隙作为]{style="font-family:宋体"}[D]{lang="EN-US"}[信道会被自动捆绑），其逻辑特性与]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[接口相同。在捆绑为]{style="font-family:宋体"}[pri set]{lang="EN-US"}[时，如果不指定捆绑的时隙，则会将所有时隙捆绑起来，形成一个类似]{style="font-family:宋体"}[23B+D]{lang="EN-US"}[的]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[接口在时隙捆绑以后将自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}]{#struct_0_21171_18224_261452083}[接口，其逻辑特性与]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[接口相同。]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的名称是]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number***:23**]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*[是]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}]{#struct_0_21171_18224_x662308667}[CT1]{lang="DA"}[/PRI]{lang="FR"}[接口上，]{style="font-family:宋体"}[cem set]{lang="DA"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[可以同时使用（]{style="font-family:宋体"}[但]{style="font-family:宋体"}[cem set]{lang="FR"}[和]{style="font-family:宋体"}[channel set]{lang="FR"}[绑定的组号和时隙不能重复]{style="font-family:宋体"}[），]{style="font-family:宋体"}[pri set]{lang="DA"}[不能和其它]{style="font-family:宋体"}[方式同时使用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_2003336228}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1279918078}[将]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:
宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[时隙捆绑为]{style="font-family:宋体"}[pri set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1595445003}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] pri-set timeslot-list 1,2,8-12]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1369165324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cem-set]{lang="EN-US"}**]{#struct_0_21171_18224_x971142818}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_x751723854}
:::

::: {#911612258 .myid}
[]{#_Toc404785159}[]{#struct_0_21171_18224_x790260515}[]{#_Toc325119333}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- reset counters controller t1**

------------------------------------------------------------------------

[**[reset counters controller t1]{lang="EN-US"}**]{#struct_0_21171_18224_x65723005}[命令用来清除]{style="font-family:
宋体"}[CT1/PRI]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}[controller]{lang="EN-US"}[计数器值可以用]{style="font-family:宋体"}**[display controller t1]{lang="EN-US"}**[命令来查看。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1356329443}

[**[reset counters controller t1]{lang="EN-US"}**[ \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_21171_18224_x967682707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1824781636}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1942686669}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1368968716}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_496348622}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1223427347}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x258800664}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_305787659}[：]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的编号。不指定本参数，将清除所有]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x529506436}

[[单独清除]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1065478141}[接口的统计信息只能使用]{style="font-family:宋体"}**[reset counters controller t1]{lang="EN-US"}**[命令，不能使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令，该命令会清除所有接口的统计信息。]{style="font-family:宋体"}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_250051111}[接口的统计信息可以用]{style="font-family:宋体"}**[display controller t1]{lang="EN-US"}**[命令来查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x446964442}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1369034252}[清除]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[T1 2/4/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters controller t1 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x1157093829}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1464579500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller t1]{lang="EN-US"}**]{#struct_0_21171_18224_1817653110}
:::

::: {#1477538093 .myid}
[]{#_Toc404785160}[]{#struct_0_21171_18224_903653137}[]{#_Toc325119334}[]{#_Toc319999941}[]{#_Toc261965014}[]{#_Toc205607618}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- sendloopcode**

------------------------------------------------------------------------

[**[sendloopcode]{lang="EN-US"}**]{#struct_0_21171_18224_1266335232}[命令用来配置发送远程环回控制码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_412457721}

[**[sendloopcode]{lang="EN-US"}**[ { **fdl-ansi-llb-down** \| **fdl-ansi-llb-up** \| **fdl-ansi-plb-down** \| **fdl-ansi-plb-up** \| **fdl-att-plb-down** \| **fdl-att-plb-up** \| **inband-llb-down** \| **inband-llb-up** }]{lang="EN-US"}]{#struct_0_21171_18224_672115300}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1369361932}

[[不发送远程环回控制码。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1930704755}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1724201186}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_768600601}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x751417566}

[[network-admin]{lang="DA"}]{#struct_0_21171_18224_x397032879}

[[mdc-admin]{lang="DA"}]{#struct_0_21171_18224_608910344}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_697492725}

[**[fdl-ansi-llb-down]{lang="EN-US"}**]{#struct_0_21171_18224_1369427468}[：]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的线路环回去激活码，解除]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[环回。]{style="font-family:宋体"}

[**[fdl-ansi-llb-up]{lang="EN-US"}**]{#struct_0_21171_18224_1594327939}[：]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的线路环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[fdl-ansi-plb-down]{lang="EN-US"}**]{#struct_0_21171_18224_x1694839449}[：]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的净荷环回去激活码，解除]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[环回。]{style="font-family:宋体"}

[**[fdl-ansi-plb-up]{lang="EN-US"}**]{#struct_0_21171_18224_388094253}[：]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的净荷环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[fdl-att-plb-down]{lang="EN-US"}**]{#struct_0_21171_18224_x1385069418}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的净荷环回去激活码，解除]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[环回。]{style="font-family:宋体"}

[**[fdl-att-plb-up]{lang="EN-US"}**]{#struct_0_21171_18224_1704151723}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的净荷环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[inband-llb-down]{lang="EN-US"}**]{#struct_0_21171_18224_493918311}[：]{style="font-family:宋体"}[发送符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的带内线路环回去激活码，解除]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[环回。]{style="font-family:宋体"}

[**[inband-llb-up]{lang="EN-US"}**]{#struct_0_21171_18224_x937003951}[：]{style="font-family:宋体"}[发送符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的带内线路环回激活码，启动远端环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x26126779}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1369230860}[接口下可以通过发送环回控制码对远端的]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口进行环回的自动配置。]{style="font-family:宋体"}[LLB]{lang="EN-US"}[（]{style="font-family:宋体"}[Line loopback]{lang="EN-US"}[，线路环回）这种方式下，一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[帧的全部]{style="font-family:宋体"}[193]{lang="EN-US"}[位（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[位同步位及]{style="font-family:宋体"}[192]{lang="EN-US"}[位有效净荷）都被环回；]{style="font-family:宋体"}[PLB]{lang="EN-US"}[（]{style="font-family:宋体"}[Payload loopback]{lang="EN-US"}[，净荷环回）这种方式下，仅]{style="font-family:宋体"}[192]{lang="EN-US"}[位有效净荷被环回。环回码的格式规范包括]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[和]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}[。]{style="font-family:宋体"}[SF]{lang="EN-US"}[格式下的]{style="font-family:宋体"}[LLB]{lang="EN-US"}[环回码占用有效带宽；]{style="font-family:宋体"}[ESF]{lang="EN-US"}[格式下对]{style="font-family:宋体"}[LLB]{lang="EN-US"}[和]{style="font-family:宋体"}[PLB]{lang="EN-US"}[的环回码均使用]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[比特位收发。]{style="font-family:宋体"}

[[这条命令需要和远端]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_21171_18224_1959154704}[设备配合使用，当对方能检测符合上述格式的各种环回码时，对方能够根据检测到的环回码类型设置相应的环回模式。持续发送]{style="font-family:宋体"}[5]{lang="EN-US"}[秒钟，不影响其它接口的正常工作。]{style="font-family:宋体"}

[[配置该命令时要求远端的]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_1908560518}[接口能自动检测到来自网上的环回控制码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1583144120}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1657232306}[发送带内线路环回激活码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x561921403}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] sendloopcode inband-llb-up]{lang="DE"}
:::

::: {#-488042157 .myid}
[]{#_Toc404785161}[]{#struct_0_21171_18224_x971929249}[]{#_Toc374365283}[]{#_Toc374191373}

**WAN接口 \-- CT1/PRI接口基本配置命令 \-- using cem**

------------------------------------------------------------------------

[**[using cem]{lang="EN-US"}**]{#struct_0_21171_18224_x971994785}[命令用来设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[为]{style="font-family:宋体"}[CEM]{lang="EN-US"}[工作方式。]{style="font-family:宋体"}

[**[undo using]{lang="EN-US"}**]{#struct_0_21171_18224_605345112}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x971798177}

[**[using cem]{lang="EN-US"}**]{#struct_0_21171_18224_x971863713}

[**[undo using]{lang="EN-US"}**]{#struct_0_21171_18224_984971165}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x971142817}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_607775539}[接口的工作方式为]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[工作方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x971208353}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x1331405568}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x971667100}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x971732636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1768156123}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x971536028}

[[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_181517824}[接口有两种工作方式：非通道化工作方式和通道化工作方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非通道化工作方式又称为]{style="font-family:宋体"}]{#struct_0_21171_18224_x971601564}[CEM]{lang="EN-US"}[工作方式，当在这种工作方式时，它将生成一个不分时隙、数据带宽为]{style="font-family:宋体"}[1.544Mbps]{lang="EN-US"}[的电路仿真接口，]{style="font-family:宋体"}[接口名是]{lang="EN-US" style="font-family:宋体"}**[circuit-emulation ]{lang="PT-BR"}***[interface-number]{lang="PT-BR"}***[:0]{lang="PT-BR"}**[。其中]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[是]{lang="EN-US" style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的编号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通道化工作方式又称为]{style="font-family:宋体"}]{#struct_0_21171_18224_x555774424}[CT1/PRI]{lang="EN-US"}[工作方式，当在这种工作方式时，它在物理上分为]{style="font-family:宋体"}[24]{lang="EN-US"}[个时隙，对应编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。对该接口有两种使用方法：]{style="font-family:宋体"}[CT1]{lang="EN-US"}[接口和]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x971929244}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1717507731}[设置]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的工作在]{style="font-family:宋体"}[CEM]{lang="EN-US"}[工作方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x971994780}

[\[Sysname\] controller t1 2/4/0]{lang="EN-US"}

[\[Sysname-T1 2/4/0\] using cem]{lang="EN-US"}
:::

::: {#-319284079 .myid}
[]{#_Toc404785163}[]{#struct_0_21171_18224_1369296396}[]{#_Toc325381659}[]{#_Toc325378575}[]{#_Toc309659956}[]{#_Toc309135105}

**WAN接口 \-- E1-F接口配置命令 \-- clock-change auto**

------------------------------------------------------------------------

[**[clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_1950617511}[命令用来开启接口的时钟自动切换功能。即接口在]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[模式下收到]{style="font-family:宋体"}[AIS/LOS/LOF]{lang="EN-US"}[告警后，自动切换成]{style="font-family:宋体"}**[master]{lang="EN-US"}**[模式。当告警消除后，接口自动切换成用户配置的时钟模式。]{style="font-family:宋体"}

[**[undo clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_133166225}[命令用来关闭接口的时钟自动切换功能，接口恢复成当前用户配置的时钟模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1840972278}

[**[clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_x1320214782}

[**[undo clock-change auto]{lang="EN-US"}**]{#struct_0_21171_18224_1587669644}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_44254958}

[[时钟自动切换功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1045838413}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1369624076}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1533598225}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x314512055}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x227940019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_608633278}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_834695196}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1412705497}[打开]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[时钟自动切换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x313392544}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] clock-change auto]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1369689612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_x1881332916}
:::

::: {#-1840450981 .myid}
[]{#_Toc404785164}[]{#struct_0_21171_18224_1975190720}[]{#_Toc325381660}[]{#_Toc325378576}[]{#_Toc309659957}[]{#_Toc309135106}

**WAN接口 \-- E1-F接口配置命令 \-- crc**

------------------------------------------------------------------------

[**[crc]{lang="EN-US"}**]{#struct_0_21171_18224_344470758}[命令用来配置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验模式。]{style="font-family:宋体"}

[**[undo crc]{lang="EN-US"}**]{#struct_0_21171_18224_1480651880}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1365513261}

[**[crc ]{lang="EN-US"}**[{ **16** \| **32** \| **none** }]{lang="EN-US"}]{#struct_0_21171_18224_x844251714}

[**[undo crc]{lang="EN-US"}**]{#struct_0_21171_18224_1073775942}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1369099789}

[[使用]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_21171_18224_70001543}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x961157676}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_1212567801}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2078701853}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_113226703}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_930002825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x931535283}

[**[16]{lang="EN-US"}**]{#struct_0_21171_18224_1369165325}[：]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口使用]{style="font-family:宋体"}[16]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_21171_18224_x751658318}[：]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_21171_18224_x1273653341}[：]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口不进行]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x888947782}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_392340264}[配置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2057966876}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] crc 32]{lang="EN-US"}
:::

::: {#510800916 .myid}
[]{#_Toc404785165}[]{#struct_0_21171_18224_x190948450}[]{#_Toc325381662}[]{#_Toc325378578}[]{#_Toc309659958}[]{#_Toc309135107}

**WAN接口 \-- E1-F接口配置命令 \-- display fe1**

------------------------------------------------------------------------

[**[display fe1]{lang="EN-US"}**]{#struct_0_21171_18224_1973387695}[命令用来显示]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1368968717}

[**[display]{lang="EN-US"}**[ **fe1** \[ **serial** *interface-number* \]]{lang="EN-US"}]{#struct_0_21171_18224_496414158}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_960541451}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1096553338}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1360790984}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_899860283}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_1074563265}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1514624775}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_1369034253}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1157159365}

[**[serial]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_21171_18224_x1179999833}[：显示指定]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为串口编号。如果不指定接口，则显示所有的]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1443825208}

[[若指定的接口不是]{style="font-family:宋体"}[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x326638339}[接口而是一个普通串口，则系统会提示该串口不是]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1604934033}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1943049419}[显示]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display fe1 serial 2/1/0]{lang="EN-US"}]{#struct_0_21171_18224_1369361933}

[Serial2/1/0]{lang="EN-US"}

[  Basic Configuration:]{lang="EN-US"}

[    Work mode: E1 framed, Cable type: 75 Ohm unbalanced]{lang="EN-US"}

[    Frame format: no-crc4]{lang="EN-US"}

[    Line code: hdb3, Source clock: slave]{lang="EN-US"}

[    Idle code: 7e, Itf type: 7e, Itf number: 4]{lang="EN-US"}

[    Loopback: not set]{lang="EN-US"}

[  Alarm State:]{lang="EN-US"}

[    Receiver alarm state is None.]{lang="EN-US"}

[    Transmitter is sending remote alarm.]{lang="EN-US"}

[  Historical Statistics:]{lang="EN-US"}

[    Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[    Last clearing of counters: Never]{lang="EN-US"}

[    Data in current interval (19349 seconds elapsed):]{lang="EN-US"}

[      Loss Frame Alignment: 129 seconds, Framing Error: 0 seconds]{lang="EN-US"}

[      CRC Error: 0 seconds, Alarm Indication: 0 seconds]{lang="EN-US"}

[      Loss-of-signals: 129 seconds, Code Violations: 0 seconds]{lang="EN-US"}

[      Slip: 0 seconds, E-Bit Error: 0 seconds]{lang="EN-US"}

[]{#struct_0_21171_18224_x1930639219}[]{#_Toc43284203}[]{#_Toc95307565}[]{#_Toc85599408}[]{#_Toc81465851}[]{#_Toc81465256}[]{#_Toc81372458}[]{#_Toc68582072}[]{#_Toc58501615}[]{#_Toc43284219}[表1-10 ]{lang="EN-US"}[display fe1]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1788186659}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_x1596666672}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_1369427469}

[[Basic Configuration]{lang="EN-US"}]{#struct_0_21171_18224_1594393475}

[[接口基本配置]{style="font-family:宋体"}]{#struct_0_21171_18224_204143359}

[[Work mode]{lang="FR"}]{#struct_0_21171_18224_x1868643529}

[[接口的工作模式]{style="font-family:宋体"}]{#struct_0_21171_18224_x2147207084}

[[Cable ]{lang="FR"}[type]{lang="EN-US"}]{#struct_0_21171_18224_1832244453}

[[接口的线缆类型（]{style="font-family:宋体"}[75]{lang="EN-US"}]{#struct_0_21171_18224_1369230861}[欧非平衡]{style="font-family:宋体"}[/120]{lang="EN-US"}[欧平衡）]{style="font-family:宋体"}

[[Frame format]{lang="EN-US"}]{#struct_0_21171_18224_1959089168}

[[帧格式]{style="font-family:宋体"}[(crc4/no-crc4)]{lang="EN-US"}]{#struct_0_21171_18224_x2029562540}

[[Line Code]{lang="EN-US"}]{#struct_0_21171_18224_x628183317}

[[线路编码格式]{style="font-family:宋体"}[(ami/hdb3)]{lang="EN-US"}]{#struct_0_21171_18224_1674665636}

[[Source Clock]{lang="EN-US"}]{#struct_0_21171_18224_1369296397}

[[接口的源时钟]{style="font-family:宋体"}[(master/slave)]{lang="EN-US"}]{#struct_0_21171_18224_1950551975}

[[Idle code]{lang="FR"}]{#struct_0_21171_18224_x1444892722}

[[空闲码（]{style="font-family:宋体"}[7e/ff]{lang="EN-US"}]{#struct_0_21171_18224_x2098942463}[）]{style="font-family:宋体"}

[[Itf type]{lang="FR"}]{#struct_0_21171_18224_668021658}

[[帧间填充码（]{style="font-family:宋体"}[7e/ff]{lang="EN-US"}]{#struct_0_21171_18224_1369624077}[）]{style="font-family:宋体"}

[[Itf number]{lang="FR"}]{#struct_0_21171_18224_x1533532689}

[[帧间填充码的个数]{style="font-family:宋体"}]{#struct_0_21171_18224_x250281141}

[[Loopback]{lang="EN-US"}]{#struct_0_21171_18224_x356483768}

[[接口是否设置了环回]{style="font-family:宋体"}]{#struct_0_21171_18224_1369689613}

[[Alarm State]{lang="EN-US"}]{#struct_0_21171_18224_x1881267380}

[[告警状态]{style="font-family:宋体"}]{#struct_0_21171_18224_1676946605}

[[Historical Statistics]{lang="EN-US"}]{#struct_0_21171_18224_635957121}

[[历史统计信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x320761301}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_1904948657}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_x823934698}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_x1221251238}

[[最后一次清除接口统计信息的时间]{style="font-family:宋体"}]{#struct_0_21171_18224_x562325132}

[[    Data in current interval (19349 seconds elapsed):]{lang="EN-US"}]{#struct_0_21171_18224_1482713094}

[[      Loss Frame Alignment: 129 seconds, Framing Error: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x1359718027}

[[      CRC Error: 0 seconds, Alarm Indication: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x318080538}

[[      Loss-of-signals: 129 seconds, Code Violations: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x930360902}

[[      Slip: 0 seconds, E-Bit Error: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1566958130}

[[当前时间间隔内的各种错误发生持续的时间统计，错误包括：帧没对齐，帧错误，警告，丢信号，违规码时间，滑帧]{style="font-family:宋体"}]{#struct_0_21171_18224_x1359914635}

[ ]{lang="EN-US"}

::: {#381973131 .myid}
[]{#_Toc404785166}[]{#struct_0_21171_18224_1194627242}[]{#_Toc325381663}[]{#_Toc325378579}[]{#_Toc309659959}[]{#_Toc309135108}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 alarm-detect**

------------------------------------------------------------------------

[**[fe1 alarm-detect]{lang="EN-US"}**]{#struct_0_21171_18224_1694551298}[命令用来配置检测远端告警信号。]{style="font-family:宋体"}

[**[undo fe1 alarm-detect]{lang="EN-US"}**]{#struct_0_21171_18224_314958709}[命令用来取消检测远端告警信号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_85587115}

[**[fe1 alarm-detect rai]{lang="EN-US"}**]{#struct_0_21171_18224_22847871}

[**[undo fe1 alarm-detect rai]{lang="EN-US"}**]{#struct_0_21171_18224_x222575322}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359849099}

[[检测远端告警信号。]{style="font-family:宋体"}]{#struct_0_21171_18224_1678523189}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1662101766}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1162753971}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x678113686}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1830783346}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1304759478}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x483698279}

[**[rai]{lang="EN-US"}**]{#struct_0_21171_18224_2017763413}[：]{style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，即远端告警指示信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359521419}

[[在成帧方式的情况下，可以使用该命令。]{style="font-family:宋体"}]{#struct_0_21171_18224_x950394525}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x252567618}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1989557714}[配置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[检测远端告警信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x351185293}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ]{lang="EN-US"}[fe1 alarm-detect rai]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_231058168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_804619300}
:::

::: {#120207434 .myid}
[]{#_Toc261965019}[]{#_Toc404785167}[]{#struct_0_21171_18224_x1359455883}[]{#_Toc325381664}[]{#_Toc325378580}[]{#_Toc309659960}[]{#_Toc309135109}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 cable**

------------------------------------------------------------------------

[**[fe1 cable]{lang="EN-US"}**]{#struct_0_21171_18224_745834390}[命令用来设置接口支持的电缆类型。]{style="font-family:宋体"}

[**[undo fe1 cable]{lang="EN-US"}**]{#struct_0_21171_18224_1291627865}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_863096064}

[**[fe1 cable]{lang="EN-US"}**[ { **long** \| **short** }]{lang="EN-US"}]{#struct_0_21171_18224_x1089196082}

[**[undo fe1 cable]{lang="EN-US"}**]{#struct_0_21171_18224_x165665707}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x718641011}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1215537596}[接口支持长电缆类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359652491}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x279732652}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1557861419}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_162412975}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_791891254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1437203634}

[**[long]{lang="EN-US"}**]{#struct_0_21171_18224_1246465676}[：表示设置支持长电缆类型。]{style="font-family:宋体"}

[**[short]{lang="EN-US"}**]{#struct_0_21171_18224_1096082814}[：表示设置支持短电缆类型]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359586955}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x73235786}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[支持的电缆类型为]{style="font-family:宋体"}**[short]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1034058630}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 cable short]{lang="EN-US"}
:::

::: {#22035193 .myid}
[]{#_Toc404785168}[]{#struct_0_21171_18224_x1111626432}[]{#_Toc325381665}[]{#_Toc325378581}[]{#_Toc309659961}[]{#_Toc309135110}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 clock**

------------------------------------------------------------------------

[**[fe1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_1511292903}[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ fe1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_289938480}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1279073781}

[**[fe1 clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_21171_18224_1955834266}

[**[undo fe1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_x1359259275}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1123496982}

[[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_x1063915863}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1212605375}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1093508435}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1173116719}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x2016284533}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1927762763}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359193739}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_1384976271}[：主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_x1324785788}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1181657927}

[[当]{style="font-family:宋体"}[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1741476772}[接口作为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧使用时，应使用主时钟模式；作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧使用时，应使用从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x381520059}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1858452272}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1359783562}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 clock master]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2128409073}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock-change]{lang="EN-US"}**]{#struct_0_21171_18224_x1786563817}**[ auto]{lang="EN-US"}**
:::

::: {#-292274820 .myid}
[]{#_Toc205607627}[]{#_Toc404785169}[]{#struct_0_21171_18224_x334685331}[]{#_Toc325381666}[]{#_Toc325378582}[]{#_Toc309659962}[]{#_Toc309135111}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 code**

------------------------------------------------------------------------

[**[fe1 code]{lang="EN-US"}**]{#struct_0_21171_18224_1838783435}[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的线路编解码格式。]{style="font-family:宋体"}

[**[undo fe1 code]{lang="EN-US"}**]{#struct_0_21171_18224_59803992}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x689031433}

[**[fe1 code]{lang="EN-US"}**[ { **ami** \| **hdb3** }]{lang="EN-US"}]{#struct_0_21171_18224_1437710499}

[**[undo fe1 code]{lang="EN-US"}**]{#struct_0_21171_18224_x1359718026}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1248003403}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_950062907}[接口的线路编解码格式为]{style="font-family:宋体"}**[hdb3]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_2045598397}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1410016185}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2003316956}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_2093940727}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1895871775}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1861468663}

[**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_x1359914634}[：采用]{style="font-family:宋体"}[AMI]{lang="EN-US"}[（]{style="font-family:宋体"}[Alternate Mark Inversion]{lang="EN-US"}[，信号交替反转码）线路编码格式。]{style="font-family:宋体"}

[**[hdb3]{lang="EN-US"}**]{#struct_0_21171_18224_x1534256113}[：采用]{style="font-family:宋体"}[HDB3]{lang="EN-US"}[（]{style="font-family:宋体"}[High Density Bipolar 3]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[阶高密度双极性码）线路编码格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_321927181}

[[配置接口的线路编解码格式时，请注意与对端设备保持一致。]{style="font-family:宋体"}]{#struct_0_21171_18224_1596360645}

[[线路编码采用]{style="font-family:宋体"}**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_485644499}[方式时，在该接口上需要同时配置]{style="font-family:宋体"}**[fe1]{lang="EN-US"}**[ **data-coding inverted**]{lang="EN-US"}[，才能保证接口正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x29147617}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1522135200}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的线路编解码格式为]{style="font-family:宋体"}**[ami]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1359849098}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 code ami]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_112439248}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 data-coding]{lang="EN-US"}**]{#struct_0_21171_18224_1402871089}
:::

::: {#1285638224 .myid}
[]{#_Toc404785170}[]{#struct_0_21171_18224_x2127390843}[]{#_Toc325381667}[]{#_Toc325378583}[]{#_Toc309659963}[]{#_Toc309135112}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 data-coding**

------------------------------------------------------------------------

[**[fe1 data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_311589521}[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="PT-BR"}[接口是否对用户数据进行翻转。]{style="font-family:宋体"}

[**[undo fe1 data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_1824741643}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x987256802}

[**[fe1 data-coding]{lang="EN-US"}**[ { **inverted** \| **normal** }]{lang="EN-US"}]{#struct_0_21171_18224_x2020397698}

[**[undo fe1 data-coding]{lang="EN-US"}**]{#struct_0_21171_18224_x1359521418}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778488830}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_1865387949}[接口不对用户数据进行翻转。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1506376664}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_916555309}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x699871461}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1587393035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_350094070}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359455882}

[**[inverted]{lang="PT-BR"}**]{#struct_0_21171_18224_x1983048965}[：对用户数据进行翻转。]{style="font-family:宋体"}

[**[normal]{lang="PT-BR"}**]{#struct_0_21171_18224_x933955311}[：不对用户数据进行翻转。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1671455758}

[[HDLC]{lang="EN-US"}]{#struct_0_21171_18224_x1548640537}[协议为了防止有效数据中的]{style="font-family:宋体"}[7e]{lang="EN-US"}[被当作填充符，会在连续]{style="font-family:宋体"}[5]{lang="EN-US"}[个]{style="font-family:宋体"}[1]{lang="EN-US"}[后插入一个]{style="font-family:
宋体"}[0]{lang="EN-US"}[。然后可以进行数据翻转，数据翻转后，]{style="font-family:宋体"}[0]{lang="EN-US"}[变成]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[变成]{style="font-family:
宋体"}[0]{lang="EN-US"}[。数据翻转的作用是：当]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口配置为]{style="font-family:宋体"}[AMI]{lang="EN-US"}[编码时，能保证每]{style="font-family:宋体"}[8]{lang="EN-US"}[个连续比特中至少有一个]{style="font-family:宋体"}[1]{lang="EN-US"}[，从而弥补]{style="font-family:宋体"}[AMI]{lang="EN-US"}[码中易出现的过多连]{style="font-family:宋体"}[0]{lang="EN-US"}[的缺陷。]{style="font-family:宋体"}

[[需注意的是，只有通信的]{style="font-family:宋体"}[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1458872794}[线路两端的]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口保持一致（都进行翻转或都不进行数据翻转），才能正常通信。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1859035768}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_2142224035}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[对用户数据进行翻转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1359652490}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 data-coding inverted]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1286351289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 code]{lang="EN-US"}**]{#struct_0_21171_18224_1475537960}
:::

::: {#-941579216 .myid}
[]{#_Toc205607629}[]{#_Toc404785171}[]{#struct_0_21171_18224_2125757285}[]{#_Toc325381668}[]{#_Toc325378584}[]{#_Toc309659964}[]{#_Toc309135113}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 detect-ais**

------------------------------------------------------------------------

[**[fe1 detect-ais]{lang="EN-US"}**]{#struct_0_21171_18224_x2079870307}[命令用来配置当前接口进行]{style="font-family:宋体"}[AIS]{lang="EN-US"}[（]{style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，告警指示信号）检测。]{style="font-family:宋体"}

[**[undo fe1 detect-ais]{lang="EN-US"}**]{#struct_0_21171_18224_2131401034}[命令用来取消]{style="font-family:宋体"}[AIS]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1678207866}

[**[fe1 detect-ais]{lang="EN-US"}**]{#struct_0_21171_18224_789010086}

[**[undo fe1 detect-ais]{lang="EN-US"}**]{#struct_0_21171_18224_x1359586954}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1639319727}

[[进行]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_21171_18224_x1029470923}[检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1880112003}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_1347980829}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1637368493}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1239661068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x213802952}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359259274}

[[在非成帧方式的情况下，可以使用该命令。]{style="font-family:宋体"}]{#struct_0_21171_18224_442586959}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1718630113}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x444988189}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[进行]{style="font-family:宋体"}[AIS]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1810675347}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 detect-ais]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1492819280}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_x975181290}
:::

::: {#-16025335 .myid}
[]{#_Toc205607630}[]{#_Toc404785172}[]{#struct_0_21171_18224_x812479142}[]{#_Toc325381669}[]{#_Toc325378585}[]{#_Toc309659965}[]{#_Toc309135114}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 frame-format**

------------------------------------------------------------------------

[**[fe1 frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_x1359193738}[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="PT-BR"}[接口的帧格式。]{style="font-family:宋体"}

[**[undo fe1 frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_x1343907084}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1367705583}

[**[fe1 frame-format ]{lang="PT-BR"}**]{#struct_0_21171_18224_1793759850}[{ **crc4** \| **no-crc4** }]{lang="PT-BR"}

[**[undo fe1 frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_x900841773}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x640850306}

[[E1-F]{lang="PT-BR"}]{#struct_0_21171_18224_424743377}[接口的帧格式为]{style="font-family:宋体"}**[no-crc4]{lang="PT-BR"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1581729089}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1359783565}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_600474282}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1581128746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x774974850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_588109130}

[**[crc4]{lang="PT-BR"}**]{#struct_0_21171_18224_x211559671}[：设置]{style="font-family:宋体"}[E1-F]{lang="PT-BR"}[接口的帧格式为]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[帧格式。]{style="font-family:宋体"}

[**[no-crc4]{lang="PT-BR"}**]{#struct_0_21171_18224_x1365835074}[：设置]{style="font-family:宋体"}[E1-F]{lang="PT-BR"}[接口的帧格式为非]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[帧格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1799607417}

[[E1-F]{lang="PT-BR"}]{#struct_0_21171_18224_x1359718029}[接口工作在成帧方式下时，支持]{style="font-family:宋体"}**[crc4]{lang="PT-BR"}**[和]{style="font-family:宋体"}**[no-crc4]{lang="PT-BR"}**[两种帧格式。其中]{style="font-family:宋体"}**[crc4]{lang="EN-US"}**[帧格式支持对物理帧进行]{style="font-family:宋体"}[4]{lang="EN-US"}[比特的循环冗余校验，而]{style="font-family:宋体"}**[no-crc4]{lang="EN-US"}**[帧格式则不支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_132258156}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x925063214}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}**[crc4]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_752442948}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 frame-format crc4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1231473952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_1462493774}
:::

::: {#2120479095 .myid}
[]{#_Toc404785173}[]{#struct_0_21171_18224_123842838}[]{#_Toc325381670}[]{#_Toc325378586}[]{#_Toc309659966}[]{#_Toc309135115}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 idle-code**

------------------------------------------------------------------------

[**[fe1 idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x1359914637}[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="PT-BR"}[接口的线路空闲码类型。]{style="font-family:宋体"}

[**[undo fe1 idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x1937540640}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_709210755}

[**[fe1 idle-code]{lang="EN-US"}**[ { **7e** \| **ff** }]{lang="EN-US"}]{#struct_0_21171_18224_x709708896}

[**[undo fe1 idle-code]{lang="EN-US"}**]{#struct_0_21171_18224_x1407543709}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_771279986}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_793254676}[接口的线路空闲码类型为]{style="font-family:宋体"}[0x]{lang="EN-US"}[7e]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1817645506}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1359849101}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1321703006}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x799174320}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_917239823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x26956195}

[**[7e]{lang="PT-BR"}**]{#struct_0_21171_18224_x1732602427}[：线路空闲码为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[ff]{lang="PT-BR"}**]{#struct_0_21171_18224_x301375985}[：线路空闲码为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1070675984}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1359521421}[接口的线路空闲码类型是指在没有被绑定到逻辑通道的时隙上发送的码型。]{style="font-family:宋体"}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x593967557}[接口的线路空闲码类型有两种：]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[和]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_742103839}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1934639303}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的线路空闲码类型为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1891666261}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ]{lang="EN-US"}[fe1 idle-code 7e]{lang="ES-AR"}
:::

::: {#-1857334192 .myid}
[]{#_Toc404785174}[]{#struct_0_21171_18224_1831420315}[]{#_Toc325381671}[]{#_Toc325378587}[]{#_Toc309659967}[]{#_Toc309135116}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 itf**

------------------------------------------------------------------------

[**[fe1 ]{lang="EN-US"}**]{#struct_0_21171_18224_x204794730}**[itf]{lang="PT-BR"}**[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的帧间填充符类型和个数。]{style="font-family:宋体"}

[**[undo ]{lang="PT-BR"}[fe1 ]{lang="EN-US"}**]{#struct_0_21171_18224_579650548}**[itf]{lang="PT-BR"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359455885}

[**[fe1 ]{lang="EN-US"}[itf ]{lang="EN-US"}**[{ **number** *number* \| **type** { **7e** \| **ff** } }]{lang="EN-US"}]{#struct_0_21171_18224_1552403444}

[**[undo fe1 itf ]{lang="EN-US"}**[{ **number** \| **type** }]{lang="EN-US"}]{#struct_0_21171_18224_x395262281}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x791266235}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_689442487}[接口的帧间填充符类型为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[，帧间填充字节个数为]{style="font-family:宋体"}[4]{lang="PT-BR"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_843844887}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x811740397}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_74633929}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1359652493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_883066762}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_218091667}

[**[number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_21171_18224_1809470167}[：设置帧间填充字节的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[14]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**]{#struct_0_21171_18224_x208067740}[：设置帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型。]{style="font-family:宋体"}

[**[7e]{lang="EN-US"}**]{#struct_0_21171_18224_x2075351105}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[**[ff]{lang="EN-US"}**]{#struct_0_21171_18224_x2075416641}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1497255499}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x842156361}[接口的帧间填充符是指在已经被绑定到逻辑通道的时隙在没有发送业务数据时发送的码型。]{style="font-family:宋体"}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1116515037}[接口的帧间填充符类型有两种：]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[和]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x443651996}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1359586957}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1089563628}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-serial2/1/0\] fe1 itf type ff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1070531122}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧间填充字节个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x485179449}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 itf number 5]{lang="EN-US"}
:::

::: {#-570146202 .myid}
[]{#_Toc404785175}[]{#struct_0_21171_18224_1887048742}[]{#_Toc325381672}[]{#_Toc325378588}[]{#_Toc309659968}[]{#_Toc309135117}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 loopback**

------------------------------------------------------------------------

[**[fe1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_242995870}[命令用来开启]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo fe1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1359259277}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_39302432}

[**[fe1 loopback]{lang="EN-US"}**[ { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_21171_18224_x1866106443}

[**[undo fe1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x2080236159}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1277351398}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_191086728}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x905414464}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x142621740}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x657553873}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1359193741}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1028942519}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x992732176}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_753548561}[：设置接口对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_1667543978}[：设置接口对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_x1437749002}[：设置接口对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1436452204}

[[在接口上，本命令可以分别打开对内自环、对外净荷环回或者对外环回功能，但不能同时启用。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1749418547}

[[自环、环回功能主要用于检测接口或电缆本身的状况，正常工作时应关闭这些功能。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1359783564}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x965609659}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x561909428}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[进行对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_504820077}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 loopback local]{lang="EN-US"}
:::

::::: {#816880464 .myid}
[]{#_Toc27023197}[]{#_Toc404785176}[]{#struct_0_21171_18224_1479815949}[]{#_Toc325381673}[]{#_Toc325378589}[]{#_Toc309659969}[]{#_Toc309135118}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 timeslot-list**

------------------------------------------------------------------------

[**[fe1 timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_596414932}[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的时隙捆绑。]{style="font-family:宋体"}

[**[undo fe1 timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_x542698902}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359718028}

[**[fe1 timeslot-list]{lang="EN-US"}**[ *list*]{lang="EN-US"}]{#struct_0_21171_18224_1698342097}

[**[undo fe1 timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_x1162842224}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_350162301}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_1310566159}[接口捆绑所有的时隙，即]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的缺省速率为]{style="font-family:宋体"}[1984kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x383652427}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1982702604}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x701410622}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1359914636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x371456699}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x844186072}

[*[list]{lang="EN-US"}*]{#struct_0_21171_18224_744641828}[：被捆绑的时隙编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。在指定捆绑的时隙时，可以用]{style="font-family:宋体"}[number]{lang="EN-US"}[的形式指定单个时隙，也可以用]{style="font-family:宋体"}[number1-number2]{lang="EN-US"}[的形式指定一个范围内的时隙，还可以用]{style="font-family:宋体"}[number1]{lang="EN-US"}[，]{style="font-family:宋体"}[number2-number3]{lang="EN-US"}[的形式同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_145346108}

[[在对]{style="font-family:宋体"}[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1767526406}[接口进行时隙捆绑后，接口的速率会同时改变。例如，当用户将]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[这十个时隙捆绑之后，接口的速率就会变为]{style="font-family:宋体"}[10]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[与]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_694918238}[接口不同的是，在]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口上只能捆绑出一个通道组（]{style="font-family:宋体"}[channel set]{lang="EN-US"}[），捆绑出的通道组就对应当前的同步串口。而在]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口上可以捆绑出多个通道组，并且每捆绑一个通道组，系统都会自动生成一个与之相对应的同步串口。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](WAN接口命令.files/image003.jpg){#图片 18 width="62" height="24"}]{lang="EN-US"}]{#struct_0_21171_18224_x1737671486}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[因为]{style="font-family:KaiTi_GB2312"}]{#struct_0_21171_18224_x2089465256}[E1-F]{lang="EN-US"}[接口的]{style="font-family:KaiTi_GB2312"}[0]{lang="EN-US"}[时隙被用于传输同步信息，所以，当对]{style="font-family:KaiTi_GB2312"}[E1-F]{lang="EN-US"}[接口的时隙进行全部捆绑时，实际捆绑的时隙为]{style="font-family:KaiTi_GB2312"}[1]{lang="EN-US"}[～]{style="font-family:KaiTi_GB2312"}[31]{lang="EN-US"}[时隙。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[当]{style="font-family:宋体"}[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1359849100}[接口的工作方式为非成帧方式时，不能配置]{style="font-family:宋体"}**[fe1 timeslot-list]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x244380935}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_74911984}[将]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[18]{lang="EN-US"}[时隙捆绑起来。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1730698413}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 timeslot-list 1,2,5,10-15,18]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x835562620}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_295160744}
:::::

::: {#63273741 .myid}
[]{#_Toc404785177}[]{#struct_0_21171_18224_x1420302183}[]{#_Toc325381674}[]{#_Toc325378590}

**WAN接口 \-- E1-F接口配置命令 \-- fe1 unframed**

------------------------------------------------------------------------

[**[fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_x1359521420}[命令用来设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口的工作方式为非成帧方式。]{style="font-family:宋体"}

[**[undo fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_2134915798}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1538408383}

[**[fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_1224822916}

[**[undo fe1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_1541610509}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_364397459}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x79140905}[接口工作在成帧方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_370478262}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1359455884}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1176479911}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x826359960}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_68164208}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x354880385}

[[当]{style="font-family:宋体"}[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1978731755}[接口工作在非成帧的工作方式时，它相当于一个不分时隙、数据带宽为]{style="font-family:宋体"}[2048kbps]{lang="EN-US"}[的接口，其逻辑特性与同步串口相同。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_x258605456}[接口工作在成帧的工作方式时，它在物理上分为]{style="font-family:宋体"}[32]{lang="EN-US"}[个时隙，对应编号为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[，其中]{style="font-family:宋体"}[0]{lang="EN-US"}[时隙用于传输同步信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x71259193}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1359652492}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的工作方式为非成帧方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1845816593}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fe1 unframed]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1067944385}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fe1 timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_x209443559}
:::

::: {#985353701 .myid}
[]{#_Toc404785178}[]{#struct_0_21171_18224_x48202550}[]{#_Toc325381675}[]{#_Toc325378591}[]{#_Toc309659951}[]{#_Toc309135100}

**WAN接口 \-- E1-F接口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_22121229}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_266144720}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1273526283}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_21171_18224_x1359586956}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x476520313}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1148845471}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_1671380021}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_243676455}

[[E1-F]{lang="EN-US"}]{#struct_0_21171_18224_1772959250}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1120606831}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_565332581}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1359259276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1605386373}

[*[size]{lang="EN-US"}*]{#struct_0_21171_18224_x471134909}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1138109336}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_21171_18224_2054614033}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x1598011803}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1089972090}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1292230057}[设置]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1359193740}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] mtu 1430]{lang="EN-US"}
:::

::: {#330651965 .myid}
[]{#_Toc404785179}[]{#struct_0_21171_18224_x1699940836}[]{#_Toc325381676}[]{#_Toc325378592}[]{#_Toc309659954}[]{#_Toc309135103}

**WAN接口 \-- E1-F接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_1056649068}[命令用来清除指定接口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1383574266}

[**[reset counters interface]{lang="EN-US"}**[ \[ **serial** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_21171_18224_606526238}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x882499773}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1465117518}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1251427741}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1359783567}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1763273696}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1016942121}

[**[serial]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_431573541}[：指定]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_2077314647}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1619592629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_x113454230}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_x766204662}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_x1359718031}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_488422980}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x413060492}[清除]{style="font-family:宋体"}[E1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface serial 2/1/0]{lang="EN-US"}]{#struct_0_21171_18224_x2001022544}
:::

::: {#517537456 .myid}
[]{#_Toc404785181}[]{#struct_0_21171_18224_391258446}[]{#_Toc325386235}[]{#_Toc309660260}

**WAN接口 \-- T1-F接口配置命令 \-- crc**

------------------------------------------------------------------------

[**[crc]{lang="EN-US"}**]{#struct_0_21171_18224_x1401630862}[命令用来配置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验模式。]{style="font-family:宋体"}

[**[undo crc]{lang="EN-US"}**]{#struct_0_21171_18224_x1979661457}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359914639}

[**[crc ]{lang="EN-US"}**[{ **16** \| **32** \| **none** }]{lang="EN-US"}]{#struct_0_21171_18224_x1487201946}

[**[undo crc]{lang="EN-US"}**]{#struct_0_21171_18224_526284749}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x121540204}

[[使用]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_21171_18224_119865657}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1362738790}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_1917212817}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1294525392}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1359849103}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1810464876}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x857968477}

[**[16]{lang="EN-US"}**]{#struct_0_21171_18224_1857132481}[：]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口使用]{style="font-family:宋体"}[16]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_21171_18224_351288244}[：]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_21171_18224_x1416883712}[：]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口不进行]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1869963408}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x318262363}[配置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1359521423}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] crc 32]{lang="EN-US"}
:::

::: {#509686804 .myid}
[]{#_Toc404785182}[]{#struct_0_21171_18224_x1756766971}[]{#_Toc325386237}[]{#_Toc309660261}

**WAN接口 \-- T1-F接口配置命令 \-- display ft1**

------------------------------------------------------------------------

[**[display ft1]{lang="EN-US"}**]{#struct_0_21171_18224_729071003}[命令用来显示]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的]{style="font-family:宋体"}[相关]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359455887}

[**[display]{lang="EN-US"}**[ **ft1** \[ **serial** *interface-number* \]]{lang="EN-US"}]{#struct_0_21171_18224_x1579764438}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x748835188}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1909869560}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1577624270}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1343748309}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_x117854451}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x613046904}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_x1359652495}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1689635816}

[**[serial]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_21171_18224_1762573879}[：显示指定]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为串口编号。如果不指定接口，则显示所有的]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_581873910}

[[若指定的接口不是]{style="font-family:宋体"}[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1672600315}[接口而是一个普通串口，则系统会提示该串口不是]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1409409242}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_526859477}[显示]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接]{style="font-family:宋体"}[口]{style="font-family:宋体"}[2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display ft1 serial 2/1/0]{lang="EN-US"}]{#struct_0_21171_18224_x1359193743}

[Serial2/1/0]{lang="EN-US"}

[Input:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 broadcasts, 0 multicasts]{lang="EN-US"}

[  0 errors, 0 runts, 0 giants]{lang="EN-US"}

[  0 CRC, 0 align errors, 0 overruns]{lang="EN-US"}

[  0 aborts, 0 no buffers]{lang="EN-US"}

[  0 frame errors]{lang="EN-US"}

[Output:]{lang="EN-US"}

[  0 packets, 0 bytes]{lang="EN-US"}

[  0 errors, 0 underruns, 0 collisions]{lang="EN-US"}

[  0 deferred]{lang="EN-US"}

[Basic Configuration:]{lang="EN-US"}

[  Work mode: T1 framed, Cable type: 100 Ohm balanced]{lang="EN-US"}

[  Frame-format: esf, fdl: none, Line code: b8zs]{lang="EN-US"}

[  Source clock: slave, Data-coding: normal]{lang="EN-US"}

[  Idle code: ff, Itf type: ff, Itf number: 2]{lang="EN-US"}

[  Loopback: not set]{lang="EN-US"}

[Alarm State:]{lang="EN-US"}

[  Receiver alarm state is Loss-of-Signal.]{lang="EN-US"}

[  Transmitter is sending remote alarm.]{lang="EN-US"}

[  Pulse density violation detected.]{lang="EN-US"}

[SendLoopCode History:]{lang="EN-US"}

[  Inband-llb-up: 0 times, Inband-llb-down: 0 times]{lang="EN-US"}

[  Fdl-ansi-llb-up: 0 times, Fdl-ansi-llb-down: 0 times]{lang="EN-US"}

[  Fdl-ansi-plb-up: 0 times, Fdl-ansi-plb-down: 0 times]{lang="EN-US"}

[  Fdl-att-plb-up: 0 times, Fdl-att-plb-down: 0 times]{lang="EN-US"}

[BERT state: stopped  ]{lang="EN-US"}

[  Test pattern: 2\^15, Status: Not Sync, Sync Detected: 0]{lang="EN-US"}

[    Time: 0 minutes, Time past: 0 minutes]{lang="EN-US"}

[    Bit Errors (since test started): 0 bits]{lang="EN-US"}

[    Bits Received (since test started): 0 Kbits]{lang="EN-US"}

[    Bit Errors (since latest sync): 0 bits]{lang="EN-US"}

[    Bits Received (since latest sync): 0 Kbits]{lang="EN-US"}

[Historical Statistics:]{lang="EN-US"}

[  Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[  Last clearing of counters: Never]{lang="EN-US"}

[  Data in current interval (285 seconds elapsed):]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm: 286 seconds]{lang="EN-US"}

[    Slip: 7 seconds, Fr Loss: 286 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 286 seconds]{lang="EN-US"}

[  Data in Interval 1:]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm: 901 seconds]{lang="EN-US"}

[    Slip: 22 seconds, Fr Loss: 901 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 901 seconds]{lang="EN-US"}

[  Data in Interval 2:  ]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm: 900 seconds]{lang="EN-US"}

[    Slip: 23 seconds, Fr Loss: 900 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 900 seconds]{lang="EN-US"}

[  Total Data (last 2 15 minute intervals):]{lang="EN-US"}

[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}

[    Ais Alarm: 0 seconds, Los Alarm: 2087 seconds]{lang="EN-US"}

[    Slip: 52 seconds, Fr Loss: 2087 seconds]{lang="EN-US"}

[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}

[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}

[    Severely Err: 0 seconds, Unavail: 2087 seconds]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display ft1]{lang="EN-US"}]{#struct_0_21171_18224_x2103225363}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1657316986}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_52294827}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x607843111}

[[Input/Output]{lang="EN-US"}]{#struct_0_21171_18224_x150307509}

[[接口输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21171_18224_x1359783566}[输出统计信息]{style="font-family:宋体"}

[[Basic Configuration]{lang="EN-US"}]{#struct_0_21171_18224_197189755}

[[接口的基本配置]{style="font-family:宋体"}]{#struct_0_21171_18224_x1344308471}

[[Work mode]{lang="EN-US"}]{#struct_0_21171_18224_x1030018429}

[[T1-F]{lang="FR"}]{#struct_0_21171_18224_x1756895783}[接口的工作模式]{style="font-family:宋体"}[(T1/CT1)]{lang="FR"}

[[Cable type]{lang="EN-US"}]{#struct_0_21171_18224_x1359718030}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_2054506921}[接口的线缆类型（]{style="font-family:宋体"}[100 Ohm balanced]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Frame-format]{lang="EN-US"}]{#struct_0_21171_18224_x1949737713}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_422939060}[接口的帧格式]{style="font-family:宋体"}[(esf/sf)]{lang="EN-US"}

[[fdl]{lang="EN-US"}]{#struct_0_21171_18224_814292670}

[[FDL]{lang="SV"}]{#struct_0_21171_18224_1711973092}[格式（]{style="font-family:宋体"}[ansi/att/none]{lang="SV"}[）]{style="font-family:宋体"}

[[Line code]{lang="EN-US"}]{#struct_0_21171_18224_x1359914638}

[[线路编码格式（]{style="font-family:宋体"}[b8zs/ami]{lang="EN-US"}]{#struct_0_21171_18224_78881995}[）]{style="font-family:宋体"}

[[Source clock]{lang="EN-US"}]{#struct_0_21171_18224_x1619773773}

[[接口的时钟源模式（]{style="font-family:宋体"}[master/slave]{lang="EN-US"}]{#struct_0_21171_18224_x601087561}[）]{style="font-family:宋体"}

[[Data-coding]{lang="EN-US"}]{#struct_0_21171_18224_x1359849102}

[[包括正常和数据翻转两种模式（]{style="font-family:宋体"}[normal/inverted]{lang="EN-US"}]{#struct_0_21171_18224_918418479}[）]{style="font-family:宋体"}

[[Idle code]{lang="EN-US"}]{#struct_0_21171_18224_x1229232176}

[[空闲码]{style="font-family:宋体"}[(7e/ff)]{lang="EN-US"}]{#struct_0_21171_18224_x1830300266}

[[Itf type]{lang="EN-US"}]{#struct_0_21171_18224_1468281635}

[[帧间填充码的类型]{style="font-family:宋体"}[(7e/ff)]{lang="EN-US"}]{#struct_0_21171_18224_x1359521422}

[[Itf number]{lang="EN-US"}]{#struct_0_21171_18224_972116384}

[[帧间填充码的字节数为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_21171_18224_1664462749}[个]{style="font-family:宋体"}

[[Loopback]{lang="EN-US"}]{#struct_0_21171_18224_x1683866503}

[[接口是否设置了环回]{style="font-family:宋体"}[(local/payload/remote/not set)]{lang="EN-US"}]{#struct_0_21171_18224_x1359455886}

[[Alarm State]{lang="EN-US"}]{#struct_0_21171_18224_x13680497}

[[告警状态]{style="font-family:宋体"}]{#struct_0_21171_18224_x449703768}

[[Receiver alarm state is Loss-of-Signal]{lang="EN-US"}]{#struct_0_21171_18224_x364536620}

[[收到的告警类型：]{style="font-family:宋体"}[none]{lang="EN-US"}]{#struct_0_21171_18224_x1359652494}[、]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}

[[Transmitter is sending remote alarm]{lang="EN-US"}]{#struct_0_21171_18224_x1039247539}

[[发出的告警类型：]{style="font-family:宋体"}[RAI]{lang="EN-US"}]{#struct_0_21171_18224_484091246}[、]{style="font-family:宋体"}[none]{lang="EN-US"}

[[Pulse density violation detected]{lang="EN-US"}]{#struct_0_21171_18224_x1359586958}

[[脉冲密度不符合规范要求]{style="font-family:宋体"}]{#struct_0_21171_18224_686279101}

[[SendLoopCode History:]{lang="EN-US"}]{#struct_0_21171_18224_2122295770}

[[  Inband-llb-up: 0 times, Inband-llb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_1566165319}

[[  Fdl-ansi-llb-up: 0 times, Fdl-ansi-llb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_x1359259278}

[[  Fdl-ansi-plb-up: 0 times, Fdl-ansi-plb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_x1170551149}

[[  Fdl-att-plb-up: 0 times, Fdl-att-plb-down: 0 times]{lang="EN-US"}]{#struct_0_21171_18224_x400479912}

[[向对端发送环回码的历史记录，包括每种码的发送次数和最近发送的是哪种码]{style="font-family:宋体"}]{#struct_0_21171_18224_x1359193742}

[[BERT state]{lang="EN-US"}]{#struct_0_21171_18224_x537141422}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_x1916768906}[测试状态：]{style="font-family:宋体"}[completed]{lang="EN-US"}[（完成）还是]{style="font-family:宋体"}[stopped]{lang="EN-US"}[（人为中止）还是]{style="font-family:宋体"}[running]{lang="EN-US"}[（正在测试）]{style="font-family:宋体"}

[[Test pattern]{lang="EN-US"}]{#struct_0_21171_18224_562530738}

[[测试模式（]{style="font-family:宋体"}]{#struct_0_21171_18224_x329798037}[2\^20/2\^15]{lang="DE"}[）]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_21171_18224_1339336278}

[[是否处于同步状态，]{style="font-family:宋体"}[Not Sync]{lang="EN-US"}]{#struct_0_21171_18224_1518480391}[表示不处于同步状态]{style="font-family:宋体"}

[[Sync Detected]{lang="EN-US"}]{#struct_0_21171_18224_562596274}

[[测试以来检测到的同步次数]{style="font-family:宋体"}]{#struct_0_21171_18224_44567302}

[[Time]{lang="EN-US"}]{#struct_0_21171_18224_968365238}

[[预设的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_562399666}

[[Time past]{lang="EN-US"}]{#struct_0_21171_18224_x1002948452}

[[已经过去的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_1264822031}

[[Bit Errors (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_562465202}

[[测试以来收到的比特错误数]{style="font-family:宋体"}]{#struct_0_21171_18224_450038997}

[[Bits Received (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_x1461704651}

[[测试以来收到的比特总数]{style="font-family:宋体"}]{#struct_0_21171_18224_562792882}

[[Bit Errors (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_x2076850514}

[[最近的同步以来收到的比特错误数]{style="font-family:宋体"}]{#struct_0_21171_18224_x879872890}

[[Bits Received (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_562858418}

[[最近的同步以来收到的比特总数]{style="font-family:宋体"}]{#struct_0_21171_18224_138039500}

[[Historical Statistics]{lang="EN-US"}]{#struct_0_21171_18224_x1901805924}

[[历史信息]{style="font-family:宋体"}]{#struct_0_21171_18224_562661810}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_118822539}

[[接口最近一次物理状态改变到现在的时长。[Never]{lang="EN-US"}表示接口从设备启动后一直处于[down]{lang="EN-US"}状态（没有改变过）]{style="font-family:宋体"}]{#struct_0_21171_18224_1622458034}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_x1447261402}

[[清零记录]{style="font-family:宋体"}]{#struct_0_21171_18224_x905375405}

[[  Data in current interval (285 seconds elapsed):]{lang="EN-US"}]{#struct_0_21171_18224_562727346}

[[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}]{#struct_0_21171_18224_x824606488}

[[    Ais Alarm: 0 seconds, Los Alarm: 286 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x194373524}

[[    Slip: 7 seconds, Fr Loss: 286 seconds]{lang="EN-US"}]{#struct_0_21171_18224_563055026}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_x326695807}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_563120562}

[[    Severely Err: 0 seconds, Unavail: 286 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x313017009}

[[当前时间间隔内的统计信息（]{style="font-family:宋体"}[15]{lang="EN-US"}]{#struct_0_21171_18224_x114211244}[分钟为一个时间间隔）。]{style="font-family:宋体"} [这些数据是按照]{style="font-family:宋体"}[T1]{lang="EN-US"}[规范对物理层所作的各种信息统计，如]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警、]{style="font-family:宋体"}[LOS]{lang="EN-US"}[信号、]{style="font-family:宋体"}[LFA]{lang="EN-US"}[等。详细解释参见]{style="font-family:宋体"}[T1]{lang="EN-US"}[规范]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[和]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}

[[  Data in Interval 1:]{lang="EN-US"}]{#struct_0_21171_18224_562530739}

[[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}]{#struct_0_21171_18224_x329798038}

[[    Ais Alarm: 0 seconds, Los Alarm: 901 seconds]{lang="EN-US"}]{#struct_0_21171_18224_1339270742}

[[    Slip: 22 seconds, Fr Loss: 901 seconds]{lang="EN-US"}]{#struct_0_21171_18224_562596275}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_44567301}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_562399667}

[[    Severely Err: 0 seconds, Unavail: 901 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x1002948453}

[[第]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_21171_18224_x1464061324}[间隔内的统计信息]{style="font-family:宋体"}

[[统计内容同上]{style="font-family:宋体"}]{#struct_0_21171_18224_562465203}

[[  Data in Interval 2:  ]{lang="EN-US"}]{#struct_0_21171_18224_450038998}

[[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}]{#struct_0_21171_18224_562792883}

[[    Ais Alarm: 0 seconds, Los Alarm: 900 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x2076850515}

[[    Slip: 23 seconds, Fr Loss: 900 seconds]{lang="EN-US"}]{#struct_0_21171_18224_562858419}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_138039499}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_473582074}

[[    Severely Err: 0 seconds, Unavail: 900 seconds]{lang="EN-US"}]{#struct_0_21171_18224_562661811}

[[第]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_21171_18224_x2053715846}[间隔内的统计信息]{style="font-family:宋体"}

[[统计内容同上]{style="font-family:宋体"}]{#struct_0_21171_18224_562727347}

[[  Total Data (last 2 15 minute intervals):]{lang="EN-US"}]{#struct_0_21171_18224_x824606487}

[[    Line Code Violations: 0, Path Code Violations: 0]{lang="EN-US"}]{#struct_0_21171_18224_563055027}

[[    Ais Alarm: 0 seconds, Los Alarm: 2087 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x326695808}

[[    Slip: 52 seconds, Fr Loss: 2087 seconds]{lang="EN-US"}]{#struct_0_21171_18224_563120563}

[[    Line Err: 0 seconds, Degraded: 0 minutes]{lang="EN-US"}]{#struct_0_21171_18224_x313017008}

[[    Errored: 0 seconds, Bursty Err: 0 seconds]{lang="EN-US"}]{#struct_0_21171_18224_x114145708}

[[    Severely Err: 0 seconds, Unavail: 2087 seconds]{lang="EN-US"}]{#struct_0_21171_18224_562530736}

[[所有间隔内的统计信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x329798051}

[[统计内容同上]{style="font-family:宋体"}]{#struct_0_21171_18224_562596272}

[ ]{lang="EN-US"}

::: {#1202025005 .myid}
[]{#_Toc205607639}[]{#_Toc404785183}[]{#struct_0_21171_18224_44567308}[]{#_Toc325386238}[]{#_Toc309660262}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 alarm-detect**

------------------------------------------------------------------------

[**[ft1 alarm-detect]{lang="EN-US"}**]{#struct_0_21171_18224_x943319882}[命令用来配置检测远端告警信号。]{style="font-family:宋体"}

[**[undo ft1 alarm-detect]{lang="EN-US"}**]{#struct_0_21171_18224_1785277032}[命令用来取消检测]{style="font-family:宋体"}[远端告警信号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2025007741}

[**[ft1 alarm-detect rai]{lang="EN-US"}**]{#struct_0_21171_18224_562399664}

[**[undo ft1 alarm-detect rai]{lang="EN-US"}**]{#struct_0_21171_18224_x1002948454}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1867345851}

[[检测远端告警信号。]{style="font-family:宋体"}]{#struct_0_21171_18224_1526108968}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_646371486}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_169150378}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1347680832}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1636909969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_562465200}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_450038999}

[**[rai]{lang="EN-US"}**]{#struct_0_21171_18224_x1461704637}[：]{style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，即远端告警指示信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_685018594}

[[在接口帧格式采用]{style="font-family:宋体"}**[esf]{lang="EN-US"}**]{#struct_0_21171_18224_759545896}[的情况下，可以使用该命令]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x83846812}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_763135853}[配置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[检测远端告警信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_562792880}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ]{lang="EN-US"}[ft1 alarm-detect rai]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2076850516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_x2042672304}
:::

::: {#-1527289549 .myid}
[]{#_Toc404785184}[]{#struct_0_21171_18224_900116235}[]{#_Toc325386239}[]{#_Toc309660263}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 alarm-threshold**

------------------------------------------------------------------------

[**[ft1 alarm-threshold]{lang="EN-US"}**]{#struct_0_21171_18224_1398298786}[命令用来配置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口告警的门限值。]{style="font-family:宋体"}

[**[undo ft1 alarm-threshold]{lang="EN-US"}**]{#struct_0_21171_18224_880129039}[命令用来恢复缺省情况]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1199686210}

[**[ft1 alarm-threshold]{lang="EN-US"}**[ { **ais** { **level-1** \| **level-2** } \| **lfa** { **level-1** \| **level-2** \| **level-3** \| **level-4** } \| **los** { **pulse-detection** \| **pulse-recovery** } *value* }]{lang="EN-US"}]{#struct_0_21171_18224_x2060982423}

[**[undo ft1 alarm-threshold]{lang="EN-US"}**[ { **ais** \| **lfa** \| **los** { **pulse-detection** \| **pulse-recovery** } }]{lang="EN-US"}]{#struct_0_21171_18224_x990061181}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_562858416}

[[对于]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_21171_18224_138039514}[告警，缺省值为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_21171_18224_436846232}[告警，缺省值为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_21171_18224_x1518196607}[告警，]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[参数的值为]{style="font-family:宋体"}[176]{lang="EN-US"}[，]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[的值为]{style="font-family:宋体"}[22]{lang="EN-US"}[，即如果在]{style="font-family:宋体"}[176]{lang="EN-US"}[个脉冲周期内检测到的脉冲数小于]{style="font-family:宋体"}[22]{lang="EN-US"}[个则认为载波丢失，]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警产生。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x193341600}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_1799532841}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_921005775}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_231708491}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_562661808}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x97400719}

[**[ais]{lang="EN-US"}**]{#struct_0_21171_18224_x460896103}[：]{style="font-family:宋体"}[AIS]{lang="EN-US"}[（]{style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，告警指示信号）告警的门限值。]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警有两个门限值，分别为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[和]{style="font-family:宋体"}**[level-2]{lang="EN-US"}[。]{style="font-family:宋体"}[level-1]{lang="EN-US"}**[的门限为在一个]{style="font-family:宋体"}[SF/ESF]{lang="EN-US"}[帧内，比特流中的]{style="font-family:宋体"}[0]{lang="EN-US"}[的个数小等于]{style="font-family:宋体"}[2]{lang="EN-US"}[，则]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警产生；]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[的门限在]{style="font-family:宋体"}[SF]{lang="EN-US"}[格式时为，一个]{style="font-family:宋体"}[SF]{lang="EN-US"}[帧内码流的]{style="font-family:宋体"}[0]{lang="EN-US"}[个数小等于]{style="font-family:宋体"}[3]{lang="EN-US"}[；在]{style="font-family:宋体"}[ESF]{lang="EN-US"}[格式时为一个]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧内码流的]{style="font-family:宋体"}[0]{lang="EN-US"}[个数小等于]{style="font-family:宋体"}[5]{lang="EN-US"}[。缺省情况下，]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警门限值为]{style="font-family:宋体"}[level-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lfa]{lang="EN-US"}**]{#struct_0_21171_18224_x164962966}[：]{style="font-family:宋体"}[LFA]{lang="EN-US"}[（]{style="font-family:宋体"}[Loss of Frame Alignment]{lang="EN-US"}[，帧失步）]{style="font-family:宋体"}[告警的门限值。]{style="font-family:宋体"}[LFA]{lang="EN-US"}[告警有四个门限值可以配置，分别为]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[、]{style="font-family:宋体"}**[level-3]{lang="EN-US"}**[和]{style="font-family:宋体"}**[level-4]{lang="EN-US"}**[。]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[为]{style="font-family:宋体"}[4]{lang="EN-US"}[个帧同步比特中丢失了]{style="font-family:宋体"}[2]{lang="EN-US"}[个；]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[为]{style="font-family:宋体"}[5]{lang="EN-US"}[个帧同步比特中丢失了]{style="font-family:
宋体"}[2]{lang="EN-US"}[个；]{style="font-family:宋体"}**[leve-3]{lang="EN-US"}**[为]{style="font-family:宋体"}[6]{lang="EN-US"}[个帧同步比特中丢失了]{style="font-family:宋体"}[2]{lang="EN-US"}[个；]{style="font-family:宋体"}**[level-4]{lang="EN-US"}**[仅仅对]{style="font-family:宋体"}[ESF]{lang="EN-US"}[格式有效，在连续]{style="font-family:宋体"}[4]{lang="EN-US"}[个]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧中出现错误时产生]{style="font-family:宋体"}[LFA]{lang="EN-US"}[告警。缺省情况下，]{style="font-family:宋体"}[LFA]{lang="EN-US"}[告警门限值为]{style="font-family:宋体"}[level-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[los]{lang="EN-US"}**]{#struct_0_21171_18224_901515993}[：]{style="font-family:宋体"}[LOS]{lang="EN-US"}[（]{style="font-family:宋体"}[Loss Of Signal]{lang="EN-US"}[，信号丢失）]{style="font-family:宋体"}[告警的门限值。]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警有两个门限值，分别为]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[和]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[，]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[配置]{style="font-family:宋体"}[LOS]{lang="EN-US"}[的检测时长门限，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[，这个时长门限的单位为"脉冲周期"；]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[配置]{style="font-family:宋体"}[LOS]{lang="EN-US"}[的脉冲门限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[，就是在检测时长内（即]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[配置的若干个脉冲周期内），检测到的脉冲个数如果小于]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[所配置的值，则]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警产生。在缺省情况，]{style="font-family:宋体"}**[pulse-detection]{lang="EN-US"}**[参数的值为]{style="font-family:宋体"}[176]{lang="EN-US"}[，]{style="font-family:宋体"}**[pulse-recovery]{lang="EN-US"}**[的值为]{style="font-family:宋体"}[22]{lang="EN-US"}[，即如果在]{style="font-family:宋体"}[176]{lang="EN-US"}[个脉冲周期内检测到的脉冲数小于]{style="font-family:宋体"}[22]{lang="EN-US"}[个则认为载波丢失，]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警产生]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_122770250}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1326834507}[将]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[LOS]{lang="EN-US"}[告警的检测时长配置为]{style="font-family:宋体"}[300]{lang="EN-US"}[个脉冲周期。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_562727344}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 alarm-threshold los pulse-detection 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x824606486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_x194766740}
:::

::: {#-1271646165 .myid}
[]{#_Toc404785185}[]{#struct_0_21171_18224_x1071968390}[]{#_Toc325386240}[]{#_Toc309660264}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 bert**

------------------------------------------------------------------------

[**[ft1 ]{lang="DE"}[bert]{lang="EN-US"}**]{#struct_0_21171_18224_1814110880}[命令用来进行线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[**[undo ft1 bert]{lang="DE"}**]{#struct_0_21171_18224_266536190}[命令用来取消进行线路位]{style="font-family:宋体"}[（]{style="font-family:宋体"}[Bit]{lang="DE"}[）]{style="font-family:
宋体"}[错误率的测试。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1630356670}

[**[ft1 bert pattern]{lang="DE"}**]{#struct_0_21171_18224_x1762753258}[ { **2\^20** \| **2\^15** } **time** *minutes* \[ **unframed** \]]{lang="DE"}

[**[undo ft1 bert]{lang="DE"}**]{#struct_0_21171_18224_563055024}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x326695809}

[[不进行线路位错误率的测试。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1525177399}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_85582746}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_2000503731}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2082757906}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1636706875}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1400645840}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_563120560}

[**[pattern]{lang="DE"}**]{#struct_0_21171_18224_x313017007}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，包括]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[（测试码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[15]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[）和]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[（测试码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[time ]{lang="DE"}**]{#struct_0_21171_18224_x115128748}*[minutes]{lang="DE"}*[：]{style="font-family:
宋体"}[设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试的持续时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[分钟。]{style="font-family:宋体"}

[**[unframed]{lang="DE"}**]{#struct_0_21171_18224_1036678894}[：设置测试数据流覆盖帧的开销位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_91142584}

[[ITU O.151]{lang="EN-US"}]{#struct_0_21171_18224_2005834538}[、]{style="font-family:宋体"}[ITU O.153]{lang="EN-US"}[及]{style="font-family:宋体"}[ANSI T1.403-1999]{lang="EN-US"}[定义了各种]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，目前]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[和]{style="font-family:宋体"}[ 2\^15]{lang="EN-US"}[两种测试模式。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_1518856400}[测试方式为，本端发出测试数据流，经过线路某处环回来，检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对方设置远端环回等。利用]{style="font-family:宋体"}**[ft1 ]{lang="DE"}[bert]{lang="EN-US"}**[命令配置好测试模式，指定测试时间，开始测试后，可以查看接口状态中的]{style="font-family:
宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_2065100114}[测试状态和测试结果详见]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_562530737}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x329798052}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接]{style="font-family:宋体"}[口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[执行]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1339663952}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 bert pattern 2\^20 time 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x62092945}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ft1]{lang="EN-US"}**]{#struct_0_21171_18224_1065622314}
:::

::: {#1060976717 .myid}
[]{#_Toc404785186}[]{#struct_0_21171_18224_x870433601}[]{#_Toc325386241}[]{#_Toc309660265}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 cable**

------------------------------------------------------------------------

[**[ft1 cable]{lang="EN-US"}**]{#struct_0_21171_18224_1990948634}[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口匹配的传输线路的衰减或长度。]{style="font-family:宋体"}

[**[undo ft1 cable]{lang="EN-US"}**]{#struct_0_21171_18224_2088350381}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_562596273}

[**[ft1 cable]{lang="EN-US"}**[ { **long** *decibel* \| **short** *length* }]{lang="EN-US"}]{#struct_0_21171_18224_44567307}

[**[undo ft1 cable]{lang="EN-US"}**]{#struct_0_21171_18224_x223275850}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1051155744}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1584122951}[接口匹配的传输线路衰减为]{style="font-family:宋体"}**[long]{lang="EN-US"}**[ **0db**]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_521611590}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_1824149971}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x203928265}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_562399665}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1002948455}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x301261910}

[**[long]{lang="EN-US"}**[ *decibel*]{lang="EN-US"}]{#struct_0_21171_18224_x1248762534}[：匹配]{style="font-family:宋体"}[655]{lang="EN-US"}[英尺以上的传输线路，参数]{style="font-family:宋体"}*[decibel]{lang="EN-US"}*[的值可以为]{style="font-family:宋体"}**[0db]{lang="EN-US"}**[、]{style="font-family:宋体"}**[-7.5db]{lang="EN-US"}**[、]{style="font-family:宋体"}**[-15db]{lang="EN-US"}**[、]{style="font-family:宋体"}**[-22.5db]{lang="EN-US"}**[，可根据接收端信号质量选择不同的衰减参数，此时不需要外接]{style="font-family:宋体"}[CSU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[short ]{lang="EN-US"}***[length]{lang="EN-US"}*]{#struct_0_21171_18224_1894435686}[：匹配]{style="font-family:宋体"}[655]{lang="EN-US"}[英尺以下的传输线路，参数]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的值可以为]{style="font-family:宋体"}**[133ft]{lang="EN-US"}[、]{style="font-family:宋体"}[266ft]{lang="EN-US"}**[、]{style="font-family:宋体"}**[399ft]{lang="EN-US"}**[、]{style="font-family:宋体"}**[533ft]{lang="EN-US"}**[、]{style="font-family:宋体"}**[655ft]{lang="EN-US"}**[，]{style="font-family:宋体"}[可根据传输线路的长度选择相应的长度参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_29996546}

[[本命令主要作用是配置发送时的信号波形，以适应不同传输需要。实际使用中可根据接收端收到的信号质量的好坏来决定是否使用此命令。如果信号质量较好可以使用缺省设置。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1542448387}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x391750398}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_562465201}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接]{style="font-family:宋体"}[口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[匹配的传输线路设为]{style="font-family:宋体"}[133]{lang="EN-US"}[英尺。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_450039000}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 cable short 133ft]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1063317817}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_x1359605421}
:::

::: {#958479096 .myid}
[]{#_Toc404785187}[]{#struct_0_21171_18224_x836520379}[]{#_Toc325386242}[]{#_Toc309660266}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 clock**

------------------------------------------------------------------------

[**[ft1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_197124727}[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[的时钟]{style="font-family:宋体"}[模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ ft1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_2117565521}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_562792881}

[**[ft1 clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_21171_18224_x2076850517}

[**[undo ft1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_x476588363}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1524605558}

[[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_x1465245755}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1937355457}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_820301364}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1983919908}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_562858417}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_138039513}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_436846239}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_x1518196612}[：主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_209877391}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_381546043}

[[当]{style="font-family:宋体"}[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x966591196}[接口作为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[使用时，]{style="font-family:宋体"}[应使用主时钟模式；]{style="font-family:宋体"}[作为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[使用时，]{style="font-family:宋体"}[应使用从时钟模式。]{style="font-family:宋体"}

[[当两台路由器的]{style="font-family:宋体"}[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_488871369}[接口直接相连时，必须使两端分别工作在]{style="font-family:宋体"}[从时钟模式和主时钟模式。]{style="font-family:宋体"}[当路由器的]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口与交换机连接时，交换机是]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[，负责提供时钟；而路由器的接口需工作在]{style="font-family:宋体"}[从时钟模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_562661809}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x97400718}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接]{style="font-family:宋体"}[口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[使用主时钟模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x460896102}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 clock master]{lang="EN-US"}
:::

::: {#-264028804 .myid}
[]{#_Toc404785188}[]{#struct_0_21171_18224_x165028502}[]{#_Toc325386243}[]{#_Toc309660267}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 code**

------------------------------------------------------------------------

[**[ft1 code]{lang="EN-US"}**]{#struct_0_21171_18224_2086566792}[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的线路编解码格式。]{style="font-family:宋体"}

[**[undo ft1 code]{lang="EN-US"}**]{#struct_0_21171_18224_x1142205375}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x68204360}

[**[ft1 code ]{lang="EN-US"}**[{ **ami** \| **b8zs** }]{lang="EN-US"}]{#struct_0_21171_18224_562727345}

[**[undo ft1 code]{lang="EN-US"}**]{#struct_0_21171_18224_x824606485}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x194701204}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_527544749}[接口的线路]{style="font-family:宋体"}[编解码]{style="font-family:宋体"}[格式为]{style="font-family:宋体"}**[b8zs]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1694209147}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1660928177}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_913901402}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_120938553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_563055025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x326695810}

[**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_x1524587576}[：采用]{style="font-family:宋体"}[AMI]{lang="EN-US"}[（]{style="font-family:宋体"}[Alternate Mark Inversion]{lang="EN-US"}[，信号交替反转码）线路编码格式。]{style="font-family:宋体"}

[**[b8zs]{lang="EN-US"}**]{#struct_0_21171_18224_x1374705717}[：采用]{style="font-family:宋体"}[B8ZS]{lang="EN-US"}[（]{style="font-family:宋体"}[Bipolar 8-zero substitution]{lang="EN-US"}[，双极性]{style="font-family:宋体"}[8zero]{lang="EN-US"}[替换码）线路编码格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x331714165}

[[配置接口的线路编解码格式时，请注意与对端设备保持一致。]{style="font-family:宋体"}]{#struct_0_21171_18224_531697736}

[[线路编码采用]{style="font-family:宋体"}**[ami]{lang="EN-US"}**]{#struct_0_21171_18224_x1931712593}[方式时，在该接口上需要同时配置]{style="font-family:宋体"}**[ft1]{lang="EN-US"}**[ **data-coding inverted**]{lang="EN-US"}[，才能保证接口正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1303155920}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_563120561}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[线路编解码]{style="font-family:宋体"}[格式]{style="font-family:宋体"}[为]{style="font-family:宋体"}**[ami]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x313017006}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 code ami]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x115063212}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 data-coding]{lang="EN-US"}**]{#struct_0_21171_18224_x1645251609}
:::

::: {#-2029369242 .myid}
[]{#_Toc404785189}[]{#struct_0_21171_18224_1606917970}[]{#_Toc325386244}[]{#_Toc309660268}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 data-coding**

------------------------------------------------------------------------

[**[ft1 data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_233668760}[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="PT-BR"}[接口是否对用户数据进行翻转。]{style="font-family:宋体"}

[**[undo ft1 data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_x1838109941}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_562530734}

[**[ft1 data-coding]{lang="EN-US"}**[ { **inverted** \| **normal** }]{lang="EN-US"}]{#struct_0_21171_18224_x329798049}

[**[undo ft1 data-coding]{lang="EN-US"}**]{#struct_0_21171_18224_1339205199}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x789524915}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_773527349}[接口]{style="font-family:宋体"}[不对用户数据进行翻转]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_338063350}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_491715223}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1078724236}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_562596270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_44567306}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1733039286}

[**[inverted]{lang="PT-BR"}**]{#struct_0_21171_18224_x1875294897}[：对用户数据进行翻转。]{style="font-family:宋体"}

[**[normal]{lang="PT-BR"}**]{#struct_0_21171_18224_x1684077851}[：不对用户数据进行翻转。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_276368021}

[[HDLC]{lang="EN-US"}]{#struct_0_21171_18224_x1346812021}[协议为了防止有效数据中的]{style="font-family:宋体"}[7e]{lang="EN-US"}[被当作填充符，会在连续]{style="font-family:宋体"}[5]{lang="EN-US"}[个]{style="font-family:宋体"}[1]{lang="EN-US"}[后插入一个]{style="font-family:
宋体"}[0]{lang="EN-US"}[。然后可以进行数据翻转，数据翻转后，]{style="font-family:宋体"}[0]{lang="EN-US"}[变成]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[变成]{style="font-family:
宋体"}[0]{lang="EN-US"}[。数据翻转的作用是：当]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口配置为]{style="font-family:宋体"}[AMI]{lang="EN-US"}[编码时，能保证每]{style="font-family:宋体"}[8]{lang="EN-US"}[个连续比特中至少有一个]{style="font-family:宋体"}[1]{lang="EN-US"}[，从而弥补]{style="font-family:宋体"}[AMI]{lang="EN-US"}[码中易出现的过多连]{style="font-family:宋体"}[0]{lang="EN-US"}[的缺陷。]{style="font-family:宋体"}

[[需注意的是，只有通信的]{style="font-family:宋体"}[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x20619184}[线路两端的]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口保持一致（都进行翻转或都不进行数据翻转），才能正常通信]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_562399662}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1002948448}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[对用户数据进行翻转]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x254142207}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 data-coding inverted]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x967309104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 code]{lang="EN-US"}**]{#struct_0_21171_18224_514846886}
:::

::: {#-308878767 .myid}
[]{#_Toc404785190}[]{#struct_0_21171_18224_1959647284}[]{#_Toc325386245}[]{#_Toc309660269}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 fdl**

------------------------------------------------------------------------

[**[ft1 fdl]{lang="SV"}**]{#struct_0_21171_18224_1118172314}[命令用来配置]{style="font-family:宋体"}[T1-F]{lang="SV"}[接口在]{style="font-family:宋体"}[ESF]{lang="SV"}[格式时]{style="font-family:宋体"}[FDL]{lang="SV"}[比特位的使用模式。]{style="font-family:宋体"}

[**[undo ft1 fdl]{lang="SV"}**]{#struct_0_21171_18224_x1562240047}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_562465198}

[**[ft1 fdl ]{lang="EN-US"}**[{ **ansi** \| **att** \| **both** \| **none** }]{lang="EN-US"}]{#struct_0_21171_18224_x1469540300}

[**[undo ft1 fdl]{lang="SV"}**]{#struct_0_21171_18224_x2110582510}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1538136547}

[[禁止]{style="font-family:宋体"}[FDL]{lang="EN-US"}]{#struct_0_21171_18224_x327113813}[（]{style="font-family:宋体"}**[none]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1526554279}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_1833722061}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1113129482}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_562792878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1498072740}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_164851579}

[**[ansi]{lang="EN-US"}**]{#struct_0_21171_18224_1457055080}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，遵循]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[att]{lang="EN-US"}**]{#struct_0_21171_18224_742841858}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，遵循]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_21171_18224_x2077573562}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，同时遵循]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_21171_18224_x1352385739}[：禁止]{style="font-family:宋体"}[FDL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1627827189}

[[FDL]{lang="EN-US"}]{#struct_0_21171_18224_562858414}[（]{style="font-family:宋体"}[Facility Data Link]{lang="EN-US"}[，设备数据链路）]{style="font-family:宋体"}[是]{style="font-family:宋体"}[T1]{lang="SV"}[的]{style="font-family:宋体"}[ESF]{lang="SV"}[帧格式中]{style="font-family:宋体"}[4k]{lang="SV"}[bps]{lang="EN-US"}[的一个带宽，可以用来传递性能信息或者环回码之类。]{style="font-family:宋体"}

[[实际应用中，可以根据对方]{style="font-family:宋体"}[FDL]{lang="EN-US"}]{#struct_0_21171_18224_138039512}[的模式调整本端]{style="font-family:宋体"}[FDL]{lang="EN-US"}[的模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_436846238}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1518196613}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[支持]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1775961332}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 fdl ansi]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_183484229}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 ]{lang="EN-US"}[frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_x2012807856}
:::

::: {#-1449625293 .myid}
[]{#_Toc404785191}[]{#struct_0_21171_18224_562661806}[]{#_Toc325386246}[]{#_Toc309660270}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 frame-format**

------------------------------------------------------------------------

[**[ft1 frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_x97400709}[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="PT-BR"}[接口的帧格式。]{style="font-family:宋体"}

[**[undo ft1 frame-format]{lang="PT-BR"}**]{#struct_0_21171_18224_1495419033}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1259880119}

[**[ft1 frame-format ]{lang="EN-US"}**[{ **esf** \| **sf** }]{lang="EN-US"}]{#struct_0_21171_18224_x118938616}

[**[undo ft1 frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_1157461979}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1971539985}

[[T1-F]{lang="PT-BR"}]{#struct_0_21171_18224_x1333199515}[接口的帧格式为]{style="font-family:宋体"}**[esf]{lang="SV"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_562727342}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x824606484}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x194635668}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x679967686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_2059028978}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1921367407}

[**[esf]{lang="EN-US"}**]{#struct_0_21171_18224_1039449960}[：设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的帧格式为]{style="font-family:宋体"}[ESF]{lang="IT"}[（]{style="font-family:宋体"}[Extended Super Frame]{lang="IT"}[，]{style="font-family:宋体"}[扩展超帧]{style="font-family:宋体"}[）]{style="font-family:宋体"}[格式。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_21171_18224_563055022}[：设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的帧格式为]{style="font-family:宋体"}[SF]{lang="IT"}[（]{style="font-family:宋体"}[Super Frame]{lang="IT"}[，]{style="font-family:宋体"}[超帧]{style="font-family:宋体"}[）]{style="font-family:宋体"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x326695811}

[[T1-F]{lang="SV"}]{#struct_0_21171_18224_x1524653112}[接口支持超帧和扩展超帧两种帧格式。在超帧格式中，多个帧可以共享相同的帧同步信息和信令信息，从而有更多的有效位来传送用户数据。实际应用中，经常需要对系统进行测试，扩展超帧技术可以用来满足在测试时不影响正常业务运行的要求]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1489130328}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x203737520}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧格式为超帧格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1611378856}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 frame-format sf]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_209944221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 fdl]{lang="EN-US"}**]{#struct_0_21171_18224_410936187}
:::

::: {#-1600458471 .myid}
[]{#_Toc404785192}[]{#struct_0_21171_18224_563120558}[]{#_Toc325386247}[]{#_Toc309660271}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 idle-code**

------------------------------------------------------------------------

[**[ft1 idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_1260961113}[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="PT-BR"}[接口的线路空闲码类型。]{style="font-family:宋体"}

[**[undo ft1 idle-code]{lang="PT-BR"}**]{#struct_0_21171_18224_x767113407}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1617330543}

[**[ft1 idle-code]{lang="EN-US"}**[ { **7e** \| **ff** }]{lang="EN-US"}]{#struct_0_21171_18224_1531745515}

[**[undo ft1 idle-code]{lang="EN-US"}**]{#struct_0_21171_18224_1206046129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x686551774}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_15382890}[接口的线路空闲码类型为]{style="font-family:宋体"}[0x]{lang="EN-US"}[7e]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_562530735}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x329798050}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1339795024}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1527762357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1280959313}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x464185082}

[**[7e]{lang="PT-BR"}**]{#struct_0_21171_18224_x406558784}[：线路空闲码为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[ff]{lang="PT-BR"}**]{#struct_0_21171_18224_x474311133}[：线路空闲码为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_562596271}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_44567305}[接口的线路空闲码类型是指在没有被绑定到逻辑通道的时隙上发送的码型。]{style="font-family:宋体"}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x605612874}[接口的线路空闲码类型有两种：]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[和]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1946421360}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1138145259}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的线路空闲码]{style="font-family:宋体"}[类型]{style="font-family:宋体"}[为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_517918202}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ]{lang="EN-US"}[ft1 idle-code 7e]{lang="ES-AR"}
:::

::: {#-1826859952 .myid}
[]{#_Toc404785193}[]{#struct_0_21171_18224_x1265431272}[]{#_Toc325386248}[]{#_Toc309660272}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 itf**

------------------------------------------------------------------------

[**[ft1 ]{lang="EN-US"}**]{#struct_0_21171_18224_562399663}**[itf]{lang="PT-BR"}**[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型和个数。]{style="font-family:宋体"}

[**[undo ]{lang="PT-BR"}[ft1 ]{lang="EN-US"}**]{#struct_0_21171_18224_x1002948449}**[itf]{lang="PT-BR"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1311941734}

[**[ft1 itf ]{lang="EN-US"}**[{ **number** *number* \| **type** { **7e** \| **ff** } }]{lang="EN-US"}]{#struct_0_21171_18224_43487074}

[**[undo ft1 itf]{lang="EN-US"}**[ { **number** \| **type** }]{lang="EN-US"}]{#struct_0_21171_18224_x1646007180}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1825032950}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1715921639}[接口的帧间填充]{style="font-family:宋体"}[符]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[，]{style="font-family:宋体"}[帧间填充]{style="font-family:宋体"}[字节个数为]{style="font-family:宋体"}[4]{lang="PT-BR"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x177229076}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_562465199}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1469540299}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_974989956}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_431127518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1552921043}

[**[number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_21171_18224_398171448}[：设置帧间填充字节的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[14]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**]{#struct_0_21171_18224_345391479}[：设置帧间填充符类型。]{style="font-family:宋体"}

[**[7e]{lang="EN-US"}**]{#struct_0_21171_18224_x1305415997}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0x7e]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[**[ff]{lang="EN-US"}**]{#struct_0_21171_18224_x1305547069}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[帧间填充符为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_972245253}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_562792879}[接口的帧间填充符是指在已经被绑定到逻辑通道的时隙在没有发送业务数据时发送的码型。]{style="font-family:宋体"}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_1498072739}[接口的帧间填充符类型有两种：]{style="font-family:宋体"}[0x7e]{lang="PT-BR"}[和]{style="font-family:宋体"}[0xff]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[同时配置了]{style="font-family:宋体"}]{#struct_0_21171_18224_164392824}**[ft1 code ami]{lang="PT-BR"}**[命令和]{style="font-family:宋体"}**[ft1 data-coding inverted]{lang="PT-BR"}**[命令后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不能配置]{style="font-family:宋体"}**[ft1 itf type ff]{lang="PT-BR"}**[命令]{style="font-family:宋体"}[，]{style="font-family:宋体"}[否则]{style="font-family:宋体"}[T1-F]{lang="PT-BR"}[接口不能正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x511449206}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x934280487}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧间填充符类型为]{style="font-family:宋体"}[0xff]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2079580649}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 itf type ff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1697786029}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧间填充字节个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_562858415}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 itf number 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_138039511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 code]{lang="PT-BR"}**]{#struct_0_21171_18224_436846237}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 data-coding]{lang="PT-BR"}**]{#struct_0_21171_18224_x1518196602}
:::

::: {#361841255 .myid}
[]{#_Toc404785194}[]{#struct_0_21171_18224_209942927}[]{#_Toc325386249}[]{#_Toc309660273}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 loopback**

------------------------------------------------------------------------

[**[ft1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1507052740}[命令用来开启]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo ft1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_2070201237}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1095349160}

[**[ft1 ]{lang="EN-US"}[loopback]{lang="EN-US"}**[ { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_21171_18224_562661807}

[**[undo ft1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x97400708}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1495419034}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_1259945655}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1085725928}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_215006746}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1584588889}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_139448830}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_562727343}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x824606483}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_x195094420}[：设置接口对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_x1100810321}[：设置接口对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_x55226251}[：设置接口对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_387385521}

[[在接口上，本命令可以分别打开对内自环、对外净荷环回或者对外环回功能，但不能同时启用]{style="font-family:宋体"}]{#struct_0_21171_18224_669812973}[。]{style="font-family:宋体"}

[[自环、环回功能主要用于检测接口或电缆本身的状况，正常工作时应关闭这些功能]{style="font-family:宋体"}]{#struct_0_21171_18224_x1901321902}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_563055023}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x326695812}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[进行对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1524718648}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 loopback local]{lang="EN-US"}
:::

::: {#-1015842215 .myid}
[]{#_Toc404785195}[]{#struct_0_21171_18224_x2106704243}[]{#_Toc325386250}[]{#_Toc309660274}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 sendloopcode**

------------------------------------------------------------------------

[**[ft1 sendloopcode]{lang="EN-US"}**]{#struct_0_21171_18224_1862677203}[命令用来配置发送远程环回控制码]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1670874055}

[**[ft1 sendloopcode]{lang="EN-US"}**[ { **fdl-ansi-llb-down** \| **fdl-ansi-llb-up** \| **fdl-ansi-plb-down** \| **fdl-ansi-plb-up** \| **fdl-att-plb-down** \| **fdl-att-plb-up** \| **inband-llb-down** \| **inband-llb-up** }]{lang="EN-US"}]{#struct_0_21171_18224_1819674223}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1847777101}

[[不发送远程环回控制码。]{style="font-family:宋体"}]{#struct_0_21171_18224_563120559}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1260961114}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x767178943}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1625785372}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1957518969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_2114730917}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1891629188}

[**[fdl-ansi-llb-down]{lang="EN-US"}**]{#struct_0_21171_18224_x835371264}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的线路环回去激活码，解除远端环回。]{style="font-family:宋体"}

[**[fdl-ansi-llb-up]{lang="EN-US"}**]{#struct_0_21171_18224_2128614679}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的线路环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[fdl-ansi-plb-down]{lang="EN-US"}**]{#struct_0_21171_18224_1179276600}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的净荷环回去激活码，解除远端环回。]{style="font-family:宋体"}

[**[fdl-ansi-plb-up]{lang="EN-US"}**]{#struct_0_21171_18224_687599851}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的净荷环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[fdl-att-plb-down]{lang="EN-US"}**]{#struct_0_21171_18224_x181046448}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的净荷环回去激活码，解除远端环回。]{style="font-family:宋体"}

[**[fdl-att-plb-up]{lang="EN-US"}**]{#struct_0_21171_18224_x1321980616}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的净荷环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[inband-llb-down]{lang="EN-US"}**]{#struct_0_21171_18224_1535273717}[：发送符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的带内线路环回去激活码，解除远端环回。]{style="font-family:宋体"}

[**[inband-llb-up]{lang="EN-US"}**]{#struct_0_21171_18224_x1450538504}[：发送符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的带内线路环回激活码，启动远端环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x726851358}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_2128680215}[接口下可以通过发送环回控制码对远端的]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口进行环回的自动配置。]{style="font-family:宋体"}

[[LLB]{lang="EN-US"}]{#struct_0_21171_18224_x35444830}[（]{style="font-family:宋体"}[Line loopback]{lang="EN-US"}[，线路环回）这种方式下，一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[的]{style="font-family:宋体"}[PCM]{lang="EN-US"}[帧的全部]{style="font-family:宋体"}[193]{lang="EN-US"}[位（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[位同步位及]{style="font-family:宋体"}[192]{lang="EN-US"}[位有效净荷）都被环回；]{style="font-family:宋体"}[PLB]{lang="EN-US"}[（]{style="font-family:宋体"}[Payload loopback]{lang="EN-US"}[，净荷环回）这种方式下，仅]{style="font-family:宋体"}[192]{lang="EN-US"}[位有效净荷被环回。]{style="font-family:宋体"}

[[环回码的格式规范包括]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}]{#struct_0_21171_18224_x1600022687}[和]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}[。]{style="font-family:宋体"}

[[SF]{lang="EN-US"}]{#struct_0_21171_18224_2121825268}[格式下的]{style="font-family:宋体"}[LLB]{lang="EN-US"}[环回码占用有效带宽（]{style="font-family:宋体"}[1-24]{lang="EN-US"}[时隙）；]{style="font-family:宋体"}[ESF]{lang="EN-US"}[格式下对]{style="font-family:宋体"}[LLB]{lang="EN-US"}[和]{style="font-family:宋体"}[PLB]{lang="EN-US"}[的环回码均使用]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[比特位收发。]{style="font-family:宋体"}

[[这条命令需要和远端]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_21171_18224_535873676}[设备配合使用，当对方能检测符合上述格式的各种环回码时，对方能够根据检测到的环回码类型设置相应的环回模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1063626480}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1732508965}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[发送带内线路环回激活码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2128483607}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 sendloopcode inband-llb-up]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1203534412}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ft1 frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_676266599}
:::

::: {#1503891921 .myid}
[]{#_Toc404785196}[]{#struct_0_21171_18224_x209945570}[]{#_Toc325386251}[]{#_Toc309660275}

**WAN接口 \-- T1-F接口配置命令 \-- ft1 timeslot-list**

------------------------------------------------------------------------

[**[ft1 timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_x855230263}[命令用来设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的时隙捆绑。]{style="font-family:宋体"}

[**[undo ft1 timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_x1901792799}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1329666312}

[**[ft1 timeslot-list]{lang="EN-US"}**[ *list* \[ **speed** { **56k** \| **64k** } \]]{lang="EN-US"}]{#struct_0_21171_18224_x1396851428}

[**[undo ft1 timeslot-list]{lang="EN-US"}**]{#struct_0_21171_18224_2128549143}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1483948281}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_2045104507}[接口捆绑所有的时隙，]{style="font-family:宋体"}[时隙的缺省速率为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口的缺省速率为]{style="font-family:宋体"}[1536kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_604923016}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1268636143}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_88802119}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_864804123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x2079796742}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128876823}

[*[list]{lang="EN-US"}*]{#struct_0_21171_18224_719535395}[：被捆绑的时隙编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。在指定捆绑的时隙时，可以用]{style="font-family:宋体"}[number]{lang="EN-US"}[的形式指定单个时隙，也可以用]{style="font-family:宋体"}[number1-number2]{lang="EN-US"}[的形式指定一个范围内的时隙，还可以用]{style="font-family:宋体"}[number1,number2-number3]{lang="EN-US"}[的形式同时指定多个时隙。]{style="font-family:宋体"}

[**[speed]{lang="EN-US"}**[ { **56k** \| **64k** }]{lang="EN-US"}]{#struct_0_21171_18224_943841530}[：时隙捆绑速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。选用参数]{style="font-family:宋体"}**[56k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[56kbps]{lang="EN-US"}[；选用参数]{style="font-family:宋体"}**[64k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。时隙的缺省速率为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1507005640}

[[在对]{style="font-family:宋体"}[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1351564101}[接口进行时隙捆绑后，接口的速率会同时改变。例如，当用户将]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[这十个时隙捆绑之后，接口的速率就会变为]{style="font-family:宋体"}[10]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[（或]{style="font-family:宋体"}[10]{lang="EN-US"}[×]{style="font-family:宋体"}[56kbps]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[与]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}]{#struct_0_21171_18224_x698899092}[接口不同的是，在]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口上只能捆绑出一个通道组（]{style="font-family:宋体"}[channel set]{lang="EN-US"}[），捆绑出的通道组就对应当前的同步串口。而在]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上，可以捆绑出多个通道组，并且每捆绑一个通道组，系统都会自动生成一个同步串口，与之相对应。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1183452478}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1856795211}[将]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上的]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[18]{lang="EN-US"}[时隙捆绑起来。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2128942359}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ft1 timeslot-list 1,2,5,10-15,18]{lang="EN-US"}
:::

::: {#-180219302 .myid}
[]{#_Toc404785197}[]{#struct_0_21171_18224_x820048057}[]{#_Toc325386252}[]{#_Toc309660255}

**WAN接口 \-- T1-F接口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_16885063}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_1818906856}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1052699961}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_21171_18224_x1120971514}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_21171_18224_172360340}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x55733906}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_2128745751}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1950206322}

[[T1-F]{lang="EN-US"}]{#struct_0_21171_18224_x1052677713}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1164458543}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x365894174}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x460262351}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1445464531}

[*[size]{lang="EN-US"}*]{#struct_0_21171_18224_323645671}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128811287}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_21171_18224_x1590584582}[影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_21171_18224_x145042317}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1166550835}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1951421224}[设置]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1078939660}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] mtu 1430]{lang="EN-US"}
:::

::: {#-162777795 .myid}
[]{#_Toc404785198}[]{#struct_0_21171_18224_926298741}[]{#_Toc325386253}[]{#_Toc309660258}

**WAN接口 \-- T1-F接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_21171_18224_2129138967}[命令用来清除指定接口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_692833232}

[**[reset counters interface]{lang="EN-US"}**[ \[ **serial** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_21171_18224_x311230736}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1541811720}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1579803351}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1920620386}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1726294983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_2126995885}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_2129204503}

[**[serial]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_13849777}[：指定]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_153994623}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_21171_18224_1391405758}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_619427317}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_2075843864}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[serial]{lang="EN-US"}**]{#struct_0_21171_18224_x1873241057}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x694322222}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_2128614680}[清除]{style="font-family:宋体"}[T1-F]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface serial 2/1/0]{lang="EN-US"}]{#struct_0_21171_18224_1179866413}
:::

::: {#1211898318 .myid}
[]{#_Toc404785200}[]{#struct_0_21171_18224_1515715722}[]{#_Toc325447434}[]{#_Toc318120159}

**WAN接口 \-- CE3接口配置命令 \-- bert**

------------------------------------------------------------------------

[**[bert]{lang="EN-US"}**]{#struct_0_21171_18224_x18324846}[命令用来进行线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[**[undo bert]{lang="EN-US"}**]{#struct_0_21171_18224_x1047552150}[命令用来取消进行线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1785860770}

[**[bert pattern]{lang="EN-US"}**[ { **2\^7** \| **2\^11** \| **2\^15** \| **qrss** } **time** *number* \[ **unframed** \]]{lang="EN-US"}]{#struct_0_21171_18224_x67322570}

[**[undo bert]{lang="EN-US"}**]{#struct_0_21171_18224_2128680216}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x35641438}

[[不进行线路位错误率的测试。]{style="font-family:宋体"}]{#struct_0_21171_18224_1034756133}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2117850233}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_712596127}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x909209635}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_333777456}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_576076370}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128483608}

[**[pattern]{lang="EN-US"}**]{#struct_0_21171_18224_x1203206732}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，包括]{style="font-family:宋体"}[2\^7]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^7]{lang="EN-US"}**]{#struct_0_21171_18224_x1462713415}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[7]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^11]{lang="EN-US"}**]{#struct_0_21171_18224_x767247232}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[11]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^15]{lang="EN-US"}**]{#struct_0_21171_18224_1088377053}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[15]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[qrss]{lang="EN-US"}**]{#struct_0_21171_18224_x1303128733}[：发送码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[，且码流中不允许连续]{style="font-family:宋体"}[14]{lang="EN-US"}[个以上的]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_21171_18224_1321881829}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试的持续时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[**[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_786540405}[：设置测试数据流填充帧的开销位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1543631927}

[[ITU O.151]{lang="EN-US"}]{#struct_0_21171_18224_2128549144}[、]{style="font-family:宋体"}[ITU O.153]{lang="EN-US"}[及]{style="font-family:宋体"}[ANSI T1.403-1999]{lang="EN-US"}[定义了各种]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，目前]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口支持]{style="font-family:宋体"}[2\^7]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[这几种测试模式。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_1483751673}[测试方式为，本端发出测试数据流，经过线路某处环回回来，本端检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对端设置为远端环回等。]{style="font-family:宋体"}

[[利用]{style="font-family:宋体"}**[bert]{lang="EN-US"}**]{#struct_0_21171_18224_1598155699}[命令配置好测试模式，指定测试持续时间，开始测试后，可以查看接口状态中的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果。]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果的说明详见]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1624656299}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1752670065}[在]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[上执行]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x193911608}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] bert pattern qrss time 10]{lang="EN-US"}
:::

::: {#-1606168679 .myid}
[]{#_Toc404785201}[]{#struct_0_21171_18224_1801302511}[]{#_Toc325447435}[]{#_Toc318120160}

**WAN接口 \-- CE3接口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_762788568}[命令用来设置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_2128876824}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_719469859}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_21171_18224_2068027680}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_779974528}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_532454442}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_2094813395}[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1910697308}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_1453226366}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128942360}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x820637882}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x293696249}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_688525217}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_318992504}[：主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_450147540}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x254192015}

[[使用主时钟模式还是从时钟模式，主要根据所连接的对端设备而定，如果与传输设备相连，本端通常设置为从时钟模式。]{style="font-family:宋体"}]{#struct_0_21171_18224_x595130159}

[[如果是两台路由器的]{style="font-family:宋体"}[CE3]{lang="EN-US"}]{#struct_0_21171_18224_1796810140}[接口直接相连，则应该把一端路由器时钟设置为主时钟模式，另一端路由器时钟设置为从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128745752}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1950009714}[设置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x701213363}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] clock master]{lang="EN-US"}
:::

::: {#-781000336 .myid}
[]{#_Toc404785202}[]{#struct_0_21171_18224_x796230626}[]{#_Toc325447436}[]{#_Toc318120161}

**WAN接口 \-- CE3接口配置命令 \-- controller e3**

------------------------------------------------------------------------

[**[controller e3]{lang="EN-US"}**]{#struct_0_21171_18224_319825280}[命令用来进入]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_561997491}

[**[controller e3]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x250952316}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_833554873}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_2128811288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1591436550}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_883479267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1220012080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1579408160}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1093169240}[：]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1793044010}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1748511513}[进入]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2129138968}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\]]{lang="EN-US"}
:::

::: {#1346685891 .myid}
[]{#_Toc404785203}[]{#struct_0_21171_18224_692243408}[]{#_Toc325447438}[]{#_Toc318120162}

**WAN接口 \-- CE3接口配置命令 \-- display controller e3**

------------------------------------------------------------------------

[**[display controller e3]{lang="EN-US"}**]{#struct_0_21171_18224_1700348787}[命令用来显示]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_356239580}

[**[display controller e3]{lang="EN-US"}**]{#struct_0_21171_18224_1882624495}[ \[ ]{lang="EN-US"}*[interface-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_33835427}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x471433662}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1544849632}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_2129204504}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_14177457}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1953934536}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_1541435950}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_21171_18224_6874493}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x2091804420}[：]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口编号。不指定本参数，将显示所有]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x690840052}

[[本命令可以显示]{style="font-family:宋体"}[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x1401674075}[接口的状态信息，同时，还可以显示]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口工作在]{style="font-family:宋体"}[CE3]{lang="EN-US"}[模式时每个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1638900604}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_2128614677}[显示]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller e3 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_2128549141}

[E3 2/4/0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Description: E3 2/4/0 Interface]{lang="EN-US"}

[Frame-format: G751, line code: HDB3, clock: slave]{lang="EN-US"}

[national-bit: 1, Current mode: CE3, loopback: not set, Alarm: none]{lang="EN-US"}

[ERROR: 2 BPV, 0 EXZ, 0 FrmErr, 0 FEBE]{lang="EN-US"}

[BERT state: (stopped, not completed)]{lang="EN-US"}

[  Test pattern: 2\^7, Status: Not Sync, Sync Detected: 0]{lang="EN-US"}

[    Time: 2 minutes Time past: 2 minutes ]{lang="EN-US"}

[    Bit errors (since test started): 0 bits]{lang="EN-US"}

[    Bits received (since test started): 0 Mbits]{lang="EN-US"}

[    Bit errors (since latest sync): 0 bits]{lang="EN-US"}

[    Bits received (since latest sync): 0 Mbits]{lang="EN-US"}

[E3 2/4/0  CE1 1: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 2: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 3: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 4: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 5: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 6: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 7: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 8: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 9: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 10: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 11: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 12: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 13: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 14: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 15: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[E3 2/4/0  CE1 16: up]{lang="EN-US"}

[  Frame-format: NO-CRC4, clock: slave, loopback: not set]{lang="EN-US"}

[  Receiver alarm state: none]{lang="EN-US"}

[  BERT state: (stopped, not completed)]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display controller e3]{lang="EN-US"}]{#struct_0_21171_18224_1484079353}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1651315806}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_x1999878344}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x640273143}

[[E3 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x1917412340}

[[Current state]{lang="EN-US"}]{#struct_0_21171_18224_x518129855}

[[E3]{lang="EN-US"}]{#struct_0_21171_18224_2128876821}[接口当前的状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_719666467}

[[E3]{lang="EN-US"}]{#struct_0_21171_18224_x1218506646}[接口的描述信息]{style="font-family:宋体"}

[[Frame-format]{lang="EN-US"}]{#struct_0_21171_18224_53735977}

[[E3]{lang="EN-US"}]{#struct_0_21171_18224_x647205934}[接口的帧格式（]{style="font-family:宋体"}[crc4/no crc4]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Line Code]{lang="EN-US"}]{#struct_0_21171_18224_2128942357}

[[线路码（]{style="font-family:宋体"}[Ami/hdb3]{lang="EN-US"}]{#struct_0_21171_18224_x820965561}[）]{style="font-family:宋体"}

[[clock]{lang="EN-US"}]{#struct_0_21171_18224_1633985510}

[[接口的源时钟（]{style="font-family:宋体"}[master/slave]{lang="EN-US"}]{#struct_0_21171_18224_x1257321237}[）]{style="font-family:宋体"}

[[national-bit]{lang="EN-US"}]{#struct_0_21171_18224_1663209424}

[[国际通信位]{style="font-family:宋体"}]{#struct_0_21171_18224_2128745749}

[[Current mode]{lang="EN-US"}]{#struct_0_21171_18224_1950730611}

[[E3]{lang="FR"}]{#struct_0_21171_18224_x661183311}[接口的工作模式（]{style="font-family:宋体"}[E3/CE3]{lang="FR"}[）]{style="font-family:宋体"}

[[Loopback]{lang="EN-US"}]{#struct_0_21171_18224_875069072}

[[接口是否设置了环回]{style="font-family:宋体"}]{#struct_0_21171_18224_759512693}

[[Alarm]{lang="EN-US"}]{#struct_0_21171_18224_2128811285}

[[告警状态]{style="font-family:宋体"}]{#struct_0_21171_18224_x1590715654}

[[BERT state]{lang="EN-US"}]{#struct_0_21171_18224_x968706843}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_1017371909}[测试状态：]{style="font-family:宋体"}[completed]{lang="EN-US"}[（自然完成）还是]{style="font-family:宋体"}[stopped]{lang="EN-US"}[（人为中止）还是]{style="font-family:宋体"}[running]{lang="EN-US"}[（正在测试）]{style="font-family:宋体"}

[[Test pattern]{lang="EN-US"}]{#struct_0_21171_18224_2129138965}

[[测试模式（]{style="font-family:宋体"}]{#struct_0_21171_18224_692964304}[2\^20/2\^15]{lang="DE"}[）]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_21171_18224_1234531074}

[[是否处于同步状态]{style="font-family:宋体"}]{#struct_0_21171_18224_x1857839144}

[[Sync Detected]{lang="EN-US"}]{#struct_0_21171_18224_2129204501}

[[测试以来检测到的同步次数]{style="font-family:宋体"}]{#struct_0_21171_18224_13980849}

[[Time]{lang="EN-US"}]{#struct_0_21171_18224_1904155484}

[[预设的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_1795189450}

[[Time past]{lang="EN-US"}]{#struct_0_21171_18224_2128614678}

[[已经过去的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_1179342136}

[[Bit Errors (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_702291555}

[[测试以来收到的错误的比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_1416281455}

[[Bits Received (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_2128680214}

[[测试以来收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_x35510366}

[[Bit Errors (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_x1586916305}

[[最近的同步以来收到的错误的比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_616186223}

[[Bits Received (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_2128483606}

[[最近的同步以来收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_x1203599948}

[[E3 2/4/0  CE1 1]{lang="EN-US"}]{#struct_0_21171_18224_324873468}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_974285059}[接口下]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[up/down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Frame-format]{lang="EN-US"}]{#struct_0_21171_18224_2128549142}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_1483882745}[通道的帧格式，包括]{style="font-family:宋体"}[ESF]{lang="EN-US"}[和]{style="font-family:宋体"}[SF]{lang="EN-US"}

[[clock]{lang="EN-US"}]{#struct_0_21171_18224_x367948488}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_2128876822}[通道的时钟方式，包括]{style="font-family:宋体"}[slave]{lang="EN-US"}[和]{style="font-family:宋体"}[master]{lang="EN-US"}

[[loopback]{lang="EN-US"}]{#struct_0_21171_18224_719600931}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_x755948109}[通道的环回方式，包括]{style="font-family:宋体"}[local]{lang="EN-US"}[、]{style="font-family:宋体"}[remote]{lang="EN-US"}[和]{style="font-family:宋体"}[payload]{lang="EN-US"}

[[Receiver alarm state]{lang="EN-US"}]{#struct_0_21171_18224_2128942358}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_x820113593}[通道接收到的告警状态，包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[和]{style="font-family:宋体"}[RAI]{lang="EN-US"}

[[BERT state]{lang="EN-US"}]{#struct_0_21171_18224_844914335}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_2128745750}[测试状态，包括]{style="font-family:宋体"}[running]{lang="EN-US"}[、]{style="font-family:宋体"}[complete]{lang="EN-US"}[和]{style="font-family:宋体"}[stopped]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1950140786}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters controller e3]{lang="EN-US"}**]{#struct_0_21171_18224_1664230634}

::: {#-1916535094 .myid}
[]{#_Toc404785204}[]{#struct_0_21171_18224_x900180980}[]{#_Toc325447439}[]{#_Toc318120163}

**WAN接口 \-- CE3接口配置命令 \-- e1 bert**

------------------------------------------------------------------------

[**[e1 bert]{lang="EN-US"}**]{#struct_0_21171_18224_566816983}[命令用来进行]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口下某]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[**[undo e1]{lang="EN-US"}**[ **bert**]{lang="EN-US"}]{#struct_0_21171_18224_x802352532}[命令用来取消该测试。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_626788302}

[**[e1]{lang="EN-US"}**[ *line-number* **bert pattern** { **2\^11** \| **2\^15** \| **2\^20** \| **2\^23** \| **qrss** } **time** *number* \[ **unframed** \]]{lang="EN-US"}]{#struct_0_21171_18224_x371550942}

[**[undo e1]{lang="EN-US"}**[ *line-number* **bert**]{lang="EN-US"}]{#struct_0_21171_18224_2128811286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1590519046}

[[不进行线路位错误率的测试。]{style="font-family:宋体"}]{#struct_0_21171_18224_x1416847843}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1946030328}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x1588182056}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1818667084}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1078163846}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1263118727}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_2129138966}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_692898768}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pattern]{lang="EN-US"}**]{#struct_0_21171_18224_1298834015}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，包括]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^23]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^11]{lang="EN-US"}**]{#struct_0_21171_18224_x1690818032}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[11]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^15]{lang="EN-US"}**]{#struct_0_21171_18224_x673652286}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[15]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^20]{lang="EN-US"}**]{#struct_0_21171_18224_1322314750}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^23]{lang="EN-US"}**]{#struct_0_21171_18224_x1288150636}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[23]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[qrss]{lang="EN-US"}**]{#struct_0_21171_18224_x1256604}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[，且码流中不允许连续]{style="font-family:宋体"}[14]{lang="EN-US"}[个以上的]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time]{lang="EN-US"}**]{#struct_0_21171_18224_847520413}**[ ]{lang="EN-US"}***[numbe]{lang="EN-US"}[r]{lang="EN-US"}*[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试的持续时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[**[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_2129204502}[：设置测试数据流填充帧的开销位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_13784241}

[[ITU O.151]{lang="EN-US"}]{#struct_0_21171_18224_1268971442}[、]{style="font-family:宋体"}[ITU O.153]{lang="EN-US"}[及]{style="font-family:宋体"}[ANSI T1.403-1999]{lang="EN-US"}[定义了各种]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，目前]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道支持]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^23]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[这几种测试模式。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_1824245572}[测试方式如下：本端发出测试数据流，经过线路某处环回回来，检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对端设置为远端环回等。]{style="font-family:宋体"}

[[利用]{style="font-family:宋体"}]{#struct_0_21171_18224_x591800750}**[bert]{lang="EN-US"}**[命令配置好测试模式，指定测试持续时间，开始测试后，可以查看接口状态中的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果。]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果的说明详见]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_880486053}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x715899270}[在]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[上执行]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2128614675}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] e1 1 bert pattern qrss time 10]{lang="EN-US"}
:::

::: {#-1027784191 .myid}
[]{#_Toc404785205}[]{#struct_0_21171_18224_1180063032}[]{#_Toc325447440}[]{#_Toc318120164}

**WAN接口 \-- CE3接口配置命令 \-- e1 channel-set**

------------------------------------------------------------------------

[**[e1]{lang="EN-US"}***[ ]{lang="EN-US"}***[channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_x934083880}[命令用来对]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道进行时隙捆绑。]{style="font-family:宋体"}

[**[undo e1]{lang="EN-US"}**]{#struct_0_21171_18224_x1780722110}[ ]{lang="EN-US"}**[channel-set]{lang="EN-US"}**[命令用来取消时隙捆绑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_791667297}

[**[e1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_1490682176}*[ ]{lang="EN-US"}***[channel-set]{lang="EN-US"}**[ ]{lang="EN-US"}*[set-number]{lang="EN-US"}*[ **timeslot-list**]{lang="EN-US"}*[ list]{lang="EN-US"}*

[**[undo e1]{lang="EN-US"}**]{#struct_0_21171_18224_x115839186}[ ]{lang="EN-US"}*[line-number ]{lang="EN-US"}***[channel-set]{lang="EN-US"}**[ ]{lang="EN-US"}*[set-number]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128680211}

[[不捆绑任何]{style="font-family:宋体"}]{#struct_0_21171_18224_x35706974}[channel set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x133488162}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x681670799}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x345946828}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x857713137}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_347575518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1788638607}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_2128483603}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[set-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1203796556}[：指定]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道上时隙捆绑形成的]{style="font-family:宋体"}[channel set]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeslot-list]{lang="EN-US"}***[ list]{lang="EN-US"}*]{#struct_0_21171_18224_x967556158}[：被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="EN-US"}*[为时隙编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。在指定捆绑的时隙时，可以用]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的形式指定单个时隙，也可以用]{style="font-family:宋体"}*[number1-number2]{lang="EN-US"}*[的形式指定一个范围内的时隙，还可以使用]{style="font-family:宋体"}*[number1,number2-number3]{lang="EN-US"}*[的形式，同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1625283788}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x1555459606}[接口支持通道化到]{style="font-family:宋体"}[E1]{lang="EN-US"}[，每个]{style="font-family:宋体"}[E1]{lang="EN-US"}[最多可捆绑出]{style="font-family:宋体"}[31]{lang="EN-US"}[个通道。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x1459913649}[E1]{lang="EN-US"}[通道工作在成帧方式（]{style="font-family:宋体"}[CE1]{lang="EN-US"}[方式）时，可以对其进行时隙捆绑。系统会自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，编号为]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number*]{lang="EN-US"}**[/]{lang="EN-US"}***[line-number]{lang="EN-US"}***[:]{lang="EN-US"}***[set-number]{lang="EN-US"}*[，如]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[的第一个]{style="font-family:宋体"}[e1]{lang="EN-US"}[的]{style="font-family:宋体"}[channel-group 0]{lang="EN-US"}[生成的串口为]{style="font-family:宋体"}[2/4/0/1:0]{lang="EN-US"}[。此接口的速率为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，其逻辑特性与同步串口相同，可以视其为同步串口，进行进一步的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_956646977}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_488849585}[在接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[的第一个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道上捆绑出一个]{style="font-family:宋体"}[128kbps]{lang="EN-US"}[的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2128549139}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] e1 1 channel-set 1 timeslot-list 1,2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1484603634}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[e1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_x87948654}
:::

::: {#-739348982 .myid}
[]{#_Toc404785206}[]{#struct_0_21171_18224_x1297039835}[]{#_Toc325447441}[]{#_Toc318120165}

**WAN接口 \-- CE3接口配置命令 \-- e1 clock**

------------------------------------------------------------------------

[**[e1]{lang="EN-US"}**]{#struct_0_21171_18224_245510956}[ ]{lang="EN-US"}**[clock]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口下]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的时钟模式。]{style="font-family:宋体"}

[**[undo e1]{lang="EN-US"}**]{#struct_0_21171_18224_1573144678}[ ]{lang="EN-US"}**[clock]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1110833320}

[**[e1]{lang="EN-US"}**]{#struct_0_21171_18224_2128876819}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[clock]{lang="EN-US"}**[ { ]{lang="EN-US"}**[master]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[slave ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo e1]{lang="EN-US"}**]{#struct_0_21171_18224_720190754}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[clock]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_881027354}

[[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_x1071398629}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_611739589}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x1055439659}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_463495699}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_237704593}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_2128942355}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x820834489}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_874983288}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的顺序号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_794260776}[：主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_643293729}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1238800995}

[[当]{style="font-family:宋体"}[CE3]{lang="EN-US"}]{#struct_0_21171_18224_1308103706}[接口工作在通道化方式下，各个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道均能独立设置时钟。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1033392336}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_2128745747}[设置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[下第一个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道使用从时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1949813107}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] e1 1 clock slave]{lang="EN-US"}
:::

::: {#-1552622764 .myid}
[]{#_Toc404785207}[]{#struct_0_21171_18224_590794291}[]{#_Toc325447442}[]{#_Toc318120166}

**WAN接口 \-- CE3接口配置命令 \-- e1 frame-format**

------------------------------------------------------------------------

[**[e1]{lang="EN-US"}***[ ]{lang="EN-US"}***[frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_x650041174}[命令用来配置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的帧格式。]{style="font-family:宋体"}

[**[undo e1 frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_x615678712}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_825522103}

[**[e1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1357002172}*[ ]{lang="EN-US"}***[frame-format ]{lang="EN-US"}**[{]{lang="EN-US"}**[ crc4]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[no-crc4]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[undo e1 ]{lang="EN-US"}***[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1101524007}*[ ]{lang="EN-US"}***[frame-format]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128811283}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_x1590846726}[通道的帧格式为]{style="font-family:宋体"}**[no-crc4]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1027217371}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_1146569231}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1348313947}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_667722999}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1472396755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1024585929}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_2129138963}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[crc4]{lang="EN-US"}**]{#struct_0_21171_18224_692571088}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的帧格式为]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[no-crc4]{lang="EN-US"}**]{#struct_0_21171_18224_x750906036}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的帧格式为非]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_362297164}

[[只有当]{style="font-family:宋体"}]{#struct_0_21171_18224_1370332909}[E1]{lang="EN-US"}[通道工作在成帧方式时（使用命令]{style="font-family:宋体"}**[undo e1 unframed]{lang="EN-US"}**[），才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1520901728}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1696946347}[设置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的帧格式为]{style="font-family:宋体"}**[crc4]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1404257629}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] e1 1 frame-format crc4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_2129204499}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[e1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_x1942858566}
:::

::: {#295073978 .myid}
[]{#_Toc404785208}[]{#struct_0_21171_18224_x1592443230}[]{#_Toc325447443}[]{#_Toc318120167}

**WAN接口 \-- CE3接口配置命令 \-- e1 loopback**

------------------------------------------------------------------------

[**[e1]{lang="EN-US"}**]{#struct_0_21171_18224_2068227082}[ ]{lang="EN-US"}**[loopback]{lang="EN-US"}**[命令用来开启]{style="font-family:宋体"}[E3]{lang="EN-US"}[接口下]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo e1]{lang="EN-US"}**]{#struct_0_21171_18224_1927116622}**[ ]{lang="EN-US"}[loopback]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1262400887}

[**[e1]{lang="EN-US"}**]{#struct_0_21171_18224_x19246729}[ ]{lang="EN-US"}*[line-number ]{lang="EN-US"}***[loopback ]{lang="EN-US"}**[{]{lang="EN-US"}**[ local]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[payload]{lang="EN-US"}[ ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ remote]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[undo e1]{lang="EN-US"}**]{#struct_0_21171_18224_x2115462457}**[ ]{lang="EN-US"}***[line-number]{lang="EN-US"}[ ]{lang="EN-US"}***[loopback]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128614676}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_1180259640}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1285339269}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_1486601116}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x996152374}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1660173415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1317122428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_62069710}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_2128680212}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_x35903582}[：设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_x1508005216}[：设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_x188961194}[：设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x326059533}

[[如果]{style="font-family:宋体"}[E1]{lang="EN-US"}]{#struct_0_21171_18224_1518606824}[通道[]{#_Hlt536863893}的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[，在设置自环或环回后，其链路层协议状态将上报为]{style="font-family:宋体"}[down]{lang="EN-US"}[。这属于正常情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_61599254}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_446418287}[设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道进行对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_2128483604}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] e1 1 loopback local]{lang="EN-US"}
:::

::: {#-539090833 .myid}
[]{#_Toc404785209}[]{#struct_0_21171_18224_x1203468876}[]{#_Toc325447444}[]{#_Toc318120168}

**WAN接口 \-- CE3接口配置命令 \-- e1 shutdown**

------------------------------------------------------------------------

[**[e1 shutdown]{lang="EN-US"}**]{#struct_0_21171_18224_x926108732}[命令用来关闭]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的某个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[**[undo e1]{lang="EN-US"}**]{#struct_0_21171_18224_x191978068}*[ ]{lang="EN-US"}***[shutdown]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x774405716}

[**[e1 ]{lang="EN-US"}***[line-number ]{lang="EN-US"}***[shutdown]{lang="EN-US"}**]{#struct_0_21171_18224_2126667856}

[**[undo e1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x201411829}*[ ]{lang="EN-US"}***[shutdown]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128549140}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_1484013817}[通道处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2000944426}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x1169065671}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x511068285}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1798600328}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1738037352}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x706300082}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_2128876820}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_719732003}

[[该命令对于]{style="font-family:宋体"}]{#struct_0_21171_18224_396508869}[E1]{lang="EN-US"}[通道及其捆绑出的串口均有效。对指定]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道执行]{style="font-family:宋体"}**[e1 shutdown]{lang="EN-US"}**[操作后，该]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道捆绑形成的串口将]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[，停止收发数据。如果执行]{style="font-family:宋体"}**[undo e1 shutdown]{lang="EN-US"}**[操作，则所有该]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道捆绑形成的串口将被重新启用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1024042617}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1243815189}[关闭]{style="font-family:宋体"}[E3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x2138905339}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] e1 1 shutdown]{lang="EN-US"}
:::

::: {#-982229301 .myid}
[]{#_Toc404785210}[]{#struct_0_21171_18224_x1514553050}[]{#_Toc325447445}[]{#_Toc318120169}

**WAN接口 \-- CE3接口配置命令 \-- e1 unframed**

------------------------------------------------------------------------

[**[e1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_2128942356}[命令用来配置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道工作在非成帧方式（]{style="font-family:宋体"}[E1]{lang="EN-US"}[方式）。]{style="font-family:宋体"}

[**[undo e1]{lang="EN-US"}***[ ]{lang="EN-US"}***[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_x821031097}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1112181498}

[**[e1 ]{lang="EN-US"}***[line-number ]{lang="EN-US"}***[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_x1556070008}

[**[undo e1]{lang="EN-US"}***[ line-number]{lang="EN-US"}***[ unframed]{lang="EN-US"}**]{#struct_0_21171_18224_1470680370}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1558787262}

[[E1]{lang="EN-US"}]{#struct_0_21171_18224_x1228344212}[通道工作在成帧方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x925653843}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_2128745748}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1950665075}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x283976255}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x602722686}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_2047871062}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1103975698}[：]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1151501722}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_1981231627}[E1]{lang="EN-US"}[配置成非成帧方式后，它将不包含帧控制信息，也不分时隙，不能进行时隙捆绑。此时，系统会自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，编号为]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number***/***line-number***:0**]{lang="EN-US"}[。此接口的速率为]{style="font-family:宋体"}[2048kbps]{lang="EN-US"}[，其逻辑特性与同步串口相同，可以视其为同步串口进行进一步的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_2128811284}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1590650118}[设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道工作在非成帧方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1258841958}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] e1 1 unframed]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1711427727}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[e1 channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_1268161463}
:::

::: {#-1620789979 .myid}
[]{#_Toc404785211}[]{#struct_0_21171_18224_1825949770}[]{#_Toc325447446}[]{#_Toc318120170}

**WAN接口 \-- CE3接口配置命令 \-- fe3**

------------------------------------------------------------------------

[**[fe3]{lang="EN-US"}**]{#struct_0_21171_18224_x1420800977}[命令用于配置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口工作在]{style="font-family:宋体"}[FE3]{lang="EN-US"}[模式，并配置]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式或子速率。]{style="font-family:宋体"}

[**[undo fe3]{lang="EN-US"}**]{#struct_0_21171_18224_2129138964}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_693029840}

[**[fe3 ]{lang="EN-US"}**]{#struct_0_21171_18224_371694636}[{ ]{lang="EN-US"}**[dsu-mode]{lang="EN-US"}**[ {]{lang="EN-US"}**[ 0 ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ 1 ]{lang="EN-US"}**[} \| ]{lang="EN-US"}**[subrate]{lang="EN-US"}[ ]{lang="EN-US"}***[number ]{lang="EN-US"}*[}]{lang="EN-US"}

[**[undo fe3]{lang="EN-US"}**]{#struct_0_21171_18224_500884683}[ { ]{lang="EN-US"}**[dsu-mode]{lang="EN-US"}[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[subrate]{lang="EN-US"}**[ }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x758646091}

[[DSU]{lang="EN-US"}]{#struct_0_21171_18224_1755264817}[模式为]{style="font-family:宋体"}[1]{lang="EN-US"}[，即]{style="font-family:宋体"}[Kentrox]{lang="EN-US"}[模式；子速率为]{style="font-family:宋体"}[34010kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1295864551}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_941828628}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_2129204500}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_13915313}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1001794478}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1366583239}

[**[dsu-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x979259143}[：设置]{style="font-family:宋体"}[FE3]{lang="EN-US"}[的]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式，支持常用的几家厂商的]{style="font-family:宋体"}[FE3 DSU]{lang="EN-US"}[模式，如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[0]{lang="EN-US"}**]{#struct_0_21171_18224_1249372262}[：]{lang="EN-US" style="font-family:宋体"}[Digital Link]{lang="EN-US"}[，支持子速率范围为]{lang="EN-US" style="font-family:宋体"}[358]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[34010kbps]{lang="EN-US"}[，共]{lang="EN-US" style="font-family:宋体"}[95]{lang="EN-US"}[个速率等级，级差]{lang="EN-US" style="font-family:宋体"}[358kbps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[1]{lang="EN-US"}**]{#struct_0_21171_18224_145906369}[：]{style="font-family:
宋体"}[Kentrox]{lang="EN-US"}[，支持子速率范围为]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[24500]{lang="EN-US"}[，]{style="font-family:宋体"}[34010kbps]{lang="EN-US"}[，共]{style="font-family:宋体"}[50]{lang="EN-US"}[个速率等级，级差]{style="font-family:宋体"}[500kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[subrate]{lang="EN-US"}**]{#struct_0_21171_18224_2115946295}**[ ]{lang="EN-US"}***[number]{lang="EN-US"}*[：工作在]{style="font-family:宋体"}[FE3]{lang="EN-US"}[模式下的]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的子速率。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[34010]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_212919514}

[[FE3]{lang="EN-US"}]{#struct_0_21171_18224_x810104535}[（]{style="font-family:宋体"}[Fractional E3]{lang="EN-US"}[，或称]{style="font-family:宋体"}[Subrate E3]{lang="EN-US"}[）是]{style="font-family:宋体"}[E3]{lang="EN-US"}[的一种非标准应用模式。目前各厂商支持的速率等级均不一样，使用]{style="font-family:宋体"}**[fe3]{lang="EN-US"}**[命令可以使我们的设备和其它厂家设备的]{style="font-family:宋体"}[FE3 DSU]{lang="EN-US"}[模式兼容，实现互通。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21171_18224_858760325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令仅在支持]{style="font-family:宋体"}]{#struct_0_21171_18224_x13493192}[FE3]{lang="EN-US"}[特性的]{style="font-family:宋体"}[CE3]{lang="EN-US"}[单板上有效，如]{style="font-family:宋体"}[CE3]{lang="EN-US"}[单板不支持]{style="font-family:宋体"}[FE3]{lang="EN-US"}[特性，系统将提示该命令无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令仅能在]{style="font-family:宋体"}]{#struct_0_21171_18224_x1118605733}[E3]{lang="EN-US"}[模式下使用，在]{style="font-family:宋体"}[CE3]{lang="EN-US"}[模式下该命令不可见。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21171_18224_2033922836}**[fe3 subrate]{lang="EN-US"}**[设置的速率值是一个大概值。由于通过]{lang="EN-US" style="font-family:宋体"}**[fe3 dsu-mode]{lang="EN-US"}**[命令配置的各]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[的子速率值是离散的，因此，当再通过]{lang="EN-US" style="font-family:宋体"}**[fe3 subrate]{lang="EN-US"}**[命令指定子速率后，]{lang="EN-US" style="font-family:宋体"}[E3]{lang="EN-US"}[接口会根据当前配置的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式计算出与这个指定子速率最匹配的精确速率（精确到]{lang="EN-US" style="font-family:宋体"}[bps]{lang="EN-US"}[），并设置硬件电路支持该速率。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21171_18224_1157492868}**[display interface serial ]{lang="EN-US"}***[interface-number]{lang="EN-US"}***[:0]{lang="EN-US"}**[命令可以查看]{lang="EN-US" style="font-family:宋体"}[E3]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式、子速率设置值、接口实际速率和接口的波特率。接口实际速率为不含开销在内的纯数据带宽，接口波特率（]{lang="EN-US" style="font-family:宋体"}[34368kbps]{lang="EN-US"}[）为]{lang="EN-US" style="font-family:宋体"}[E3]{lang="EN-US"}[线路的实际速率（含开销位在内）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1914846037}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_212853978}[设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[FE3]{lang="EN-US"}[模式，]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式为]{style="font-family:宋体"}[1]{lang="EN-US"}[，子速率为]{style="font-family:宋体"}[3000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_344670445}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] using e3]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] fe3 dsu-mode 1]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] fe3 subrate 3000]{lang="EN-US"}
:::

::: {#98531835 .myid}
[]{#_Toc404785212}[]{#struct_0_21171_18224_2138663184}[]{#_Toc325447447}[]{#_Toc318120171}

**WAN接口 \-- CE3接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1858634385}[命令用来开启]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_1600068761}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_587122887}

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x695763098}[ {]{lang="EN-US"}**[ local]{lang="EN-US"}[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[payload]{lang="EN-US"}[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[remote ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_212788442}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1734038509}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_x471877134}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1166521845}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x1751923434}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1920760594}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1075219473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1074783229}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_212722906}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_x658882422}[：设置接口对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_x783873576}[：设置接口对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_x1897672495}[：设置接口对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1472119346}

[[只有在进行某些特殊功能测试时，才需要将]{style="font-family:宋体"}]{#struct_0_21171_18224_x471917703}[CE3]{lang="EN-US"}[接口设为自环。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}]{#struct_0_21171_18224_x1553249813}[CE3]{lang="EN-US"}[接口的链路层协议配置为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[，在设置环回[]{#_Hlt8649581}后，其链路层协议状态将上报为]{style="font-family:宋体"}[down]{lang="EN-US"}[，这属于正常情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x546194657}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_212657370}[设置接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1456437933}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] loopback local]{lang="EN-US"}
:::

::: {#1683336508 .myid}
[]{#_Toc404785213}[]{#struct_0_21171_18224_x2057845693}[]{#_Toc325447448}[]{#_Toc318120172}

**WAN接口 \-- CE3接口配置命令 \-- national-bit**

------------------------------------------------------------------------

[**[national-bit]{lang="EN-US"}**]{#struct_0_21171_18224_x701055328}[命令用来配置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[National bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo national-bit]{lang="EN-US"}**]{#struct_0_21171_18224_x1609681018}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1213976550}

[**[national-bit]{lang="EN-US"}**[ {]{lang="EN-US"}]{#struct_0_21171_18224_x2064987214}[ ]{lang="EN-US"}**[0]{lang="EN-US"}**[ \| **1** ]{lang="EN-US"}[}]{lang="EN-US"}

[**[undo national-bit]{lang="EN-US"}**]{#struct_0_21171_18224_212591834}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1323382038}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x1843178413}[接口的]{style="font-family:宋体"}[National bit]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1259480960}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_1058610250}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1210918090}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_969976031}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1171491214}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_212526298}

[**[0]{lang="EN-US"}**]{#struct_0_21171_18224_1864306779}[：配置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[National bit]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[。表明这个接口只能进行国内通信。]{style="font-family:
宋体"}

[**[1]{lang="EN-US"}**]{#struct_0_21171_18224_1553469328}[：配置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[National bit]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。表明这个接口只能进行国际通信。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1951199496}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1854057176}[设置接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[national-bit]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_212460762}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] national-bit 0]{lang="EN-US"}
:::

::: {#-1749269427 .myid}
[]{#_Toc404785214}[]{#struct_0_21171_18224_1443279620}[]{#_Toc325447449}[]{#_Toc318120173}

**WAN接口 \-- CE3接口配置命令 \-- reset counters controller e3**

------------------------------------------------------------------------

[**[reset counters controller e3]{lang="EN-US"}**]{#struct_0_21171_18224_x1169007223}[命令用来清除]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:宋体"}]{#struct_0_21171_18224_x1659650469}

[**[reset counters controller e3]{lang="EN-US"}**[ \[]{lang="EN-US"}*[ interface-number ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_21171_18224_x893899979}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2069951181}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1877152352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x26274163}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1067357701}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_213443802}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1157213688}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_820823930}[：]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口编号。不指定本参数，将清除所有]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1463047976}

[[单独清除]{style="font-family:宋体"}[CE3]{lang="EN-US"}]{#struct_0_21171_18224_1731953678}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[只能使用]{style="font-family:宋体"}**[reset counters controller e3]{lang="EN-US"}**[命令，不能使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令，该命令会清除所有接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_616832767}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[可以用]{style="font-family:宋体"}**[display controller e3]{lang="EN-US"}**[命令来查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1339651949}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_635364712}[清除]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters controller e3 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_213378266}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1452084809}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller e3]{lang="EN-US"}**]{#struct_0_21171_18224_x1404550309}
:::

::: {#59180213 .myid}
[]{#_Toc404785215}[]{#struct_0_21171_18224_213902402}[]{#_Toc325447451}[]{#_Toc318120174}

**WAN接口 \-- CE3接口配置命令 \-- using**

------------------------------------------------------------------------

[**[using]{lang="EN-US"}**]{#struct_0_21171_18224_127415856}[命令用来设置]{style="font-family:宋体"}[CE3]{lang="EN-US"}[接口的工作模式。]{style="font-family:宋体"}

[**[undo using]{lang="EN-US"}**]{#struct_0_21171_18224_x1253142510}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1787362916}

[**[using ]{lang="EN-US"}**[{ **ce3** \| **e3** }]{lang="EN-US"}]{#struct_0_21171_18224_1378264756}

[**[undo using]{lang="EN-US"}**]{#struct_0_21171_18224_187172792}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_212919515}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_x810104536}[接口工作在]{style="font-family:宋体"}[CE3]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_858694789}

[[CE3]{lang="EN-US"}]{#struct_0_21171_18224_389738475}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x39050701}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1390975650}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1407890780}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1546396394}

[**[ce3]{lang="EN-US"}**]{#struct_0_21171_18224_212853979}[：设置接口工作在通道化模式（]{style="font-family:宋体"}[CE3]{lang="EN-US"}[模式）。]{style="font-family:宋体"}

[**[e3]{lang="EN-US"}**]{#struct_0_21171_18224_344670444}[：设置接口工作在非通道化模式（]{style="font-family:宋体"}[E3]{lang="EN-US"}[模式）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_2138663183}

[[只有当]{style="font-family:宋体"}]{#struct_0_21171_18224_x1858699921}[CE3]{lang="EN-US"}[接口工作在通道化模式时，才能够对]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道进行配置。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x2076066007}[CE3]{lang="EN-US"}[接口工作在非通道化模式时，系统会自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，编号为]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number***/0:0**]{lang="EN-US"}[。此接口的速率为]{style="font-family:宋体"}[34.368Mbps]{lang="EN-US"}[，其逻辑特性与同步串口相同，可以视其为同步串口进行进一步的配置。]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#struct_0_21171_18224_1406161827}[【举例】]{style="font-family:黑体"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1176606820}[配置接口]{style="font-family:宋体"}[E3 2/4/0]{lang="EN-US"}[工作在非通道化模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_212788443}

[\[Sysname\] controller e3 2/4/0]{lang="EN-US"}

[\[Sysname-E3 2/4/0\] using e3]{lang="EN-US"}
:::

::: {#-1604999377 .myid}
[]{#_Toc404785217}[]{#struct_0_21171_18224_x472335885}[]{#_Toc325463696}[]{#_Toc318123779}

**WAN接口 \-- CT3接口配置命令 \-- alarm**

------------------------------------------------------------------------

[**[alarm]{lang="EN-US"}**]{#struct_0_21171_18224_x2045353993}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的告警信号检测与发送功能。]{style="font-family:宋体"}

[**[undo alarm]{lang="EN-US"}**]{#struct_0_21171_18224_x269453175}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2102558950}

[**[alarm]{lang="EN-US"}**[ { **detect** \| **generate** { **ais** \| **febe** \| **idle** \| **rai** } }]{lang="EN-US"}]{#struct_0_21171_18224_x1041242828}

[**[undo alarm]{lang="EN-US"}**[ { **detect** \| **generate** { **ais** \| **febe** \| **idle** \| **rai** } }]{lang="EN-US"}]{#struct_0_21171_18224_x536012516}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_212722907}

[[告警信号检测功能处于打开状态，发送功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_x658882421}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x784070184}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x67484675}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1938800289}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1781535771}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_182566354}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x999845525}

[**[detect]{lang="EN-US"}**]{#struct_0_21171_18224_212657371}[：]{style="font-family:宋体"}[ CT3]{lang="EN-US"}[接口的定时检测各种告警的功能。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_21171_18224_x1456437934}[：发送某种告警信号，如]{style="font-family:宋体"}[AIS]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[、]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[和]{style="font-family:宋体"}[FEBE]{lang="EN-US"}[。可用于线路状态测试。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ais]{lang="EN-US"}**]{#struct_0_21171_18224_1833837076}[：]{lang="EN-US" style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，即告警指示信号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[febe]{lang="EN-US"}**]{#struct_0_21171_18224_x1866090937}[：]{lang="EN-US" style="font-family:宋体"}[Far End Block Error]{lang="EN-US"}[，即远端块错误。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[idle]{lang="EN-US"}**]{#struct_0_21171_18224_1968964421}[：空闲信号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rai]{lang="EN-US"}**]{#struct_0_21171_18224_1851335951}[：]{lang="EN-US" style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，即远端告警指示信号。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1142873642}

[[上电后，]{style="font-family:宋体"}]{#struct_0_21171_18224_120835639}[CT3]{lang="EN-US"}[接口的告警信号定时检测功能是打开的，并能通过接口显示实时报告接口告警状态，如]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[等。当检测到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[后，会向对方发送]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警信号。]{style="font-family:宋体"}

[[主要的告警信号包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_21171_18224_212591835}[（]{style="font-family:宋体"}[Loss Of Signal]{lang="EN-US"}[，信号丢失）、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[（]{style="font-family:宋体"}[Loss Of Frame]{lang="EN-US"}[，帧同步丢失）、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[（]{style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，告警指示信号）、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，远端告警指示信号）、]{style="font-family:宋体"}[FEBE]{lang="EN-US"}[（]{style="font-family:宋体"}[Far End Block Error]{lang="EN-US"}[，远端块错误）、]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[为空闲信号。各信号具体格式遵循]{style="font-family:宋体"}[T3]{lang="EN-US"}[规范]{style="font-family:宋体"}[ANSI T1.107-1995]{lang="EN-US"}[。]{style="font-family:宋体"}

[[接口一次只能发送一种告警信号（包括在使用]{style="font-family:宋体"}]{#struct_0_21171_18224_x1323382039}**[detect]{lang="EN-US"}**[功能时检测到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[后而产生的]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警信号），发送另一种告警信号前必须使用]{style="font-family:宋体"}**[undo alarm]{lang="EN-US"}**[命令取消前一种告警信号。]{style="font-family:宋体"}**[detect]{lang="EN-US"}**[功能产生的告警信号（]{style="font-family:宋体"}[RAI]{lang="EN-US"}[）必须通过]{style="font-family:宋体"}**[undo alarm detect]{lang="EN-US"}**[命令取消。]{style="font-family:宋体"}

[[告警的收发状态详见]{style="font-family:宋体"}]{#struct_0_21171_18224_885704942}[CT3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x866160939}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_704192704}[打开]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的告警检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1093082066}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] alarm detect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_458945748}[在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[上发送]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_212526299}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[ \[Sysname-T3 2/4/0\] alarm generate ais]{lang="EN-US"}
:::

::: {#-219109132 .myid}
[]{#_Toc404785218}[]{#struct_0_21171_18224_1864306780}[]{#_Toc325463697}[]{#_Toc318123780}

**WAN接口 \-- CT3接口配置命令 \-- bert**

------------------------------------------------------------------------

[**[bert]{lang="EN-US"}**]{#struct_0_21171_18224_1553010569}[命令用来进行线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[**[undo bert]{lang="EN-US"}**]{#struct_0_21171_18224_x829479658}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_255859406}

[**[bert pattern]{lang="EN-US"}**[ { **2\^7** \| **2\^11** \| **2\^15** \| **qrss** } **time** *number* \[ **unframed** \]]{lang="EN-US"}]{#struct_0_21171_18224_x1248180664}

[**[undo bert]{lang="EN-US"}**]{#struct_0_21171_18224_219945783}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_212460763}

[[不进行线路位错误率的测试。]{style="font-family:宋体"}]{#struct_0_21171_18224_1443279621}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1168941687}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_881635538}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_76709096}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x441054438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_599211519}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1507566948}

[**[pattern]{lang="EN-US"}**]{#struct_0_21171_18224_213443803}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，包括]{style="font-family:宋体"}[2\^7]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^7]{lang="EN-US"}**]{#struct_0_21171_18224_1157213689}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[7]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^11]{lang="EN-US"}**]{#struct_0_21171_18224_820758394}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[11]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^15]{lang="EN-US"}**]{#struct_0_21171_18224_1635502223}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[15]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[qrss]{lang="EN-US"}**]{#struct_0_21171_18224_x1382220369}[：发送码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[，且码流中不允许连续]{style="font-family:宋体"}[14]{lang="EN-US"}[个以上的]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_21171_18224_70096120}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试的持续时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[**[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_74787371}[：设置测试数据流填充帧的开销位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x295015546}

[[ITU O.151]{lang="EN-US"}]{#struct_0_21171_18224_213378267}[、]{style="font-family:宋体"}[ITU O.153]{lang="EN-US"}[及]{style="font-family:宋体"}[ANSI T1.403-1999]{lang="EN-US"}[定义了各种]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，目前]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口支持]{style="font-family:宋体"}[2\^7]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[，]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[这几种测试模式。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_x1452084810}[测试方式为，本端发出测试数据流，经过线路某处环回回来，本端检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对端设置为远端环回等。]{style="font-family:宋体"}

[[利用]{style="font-family:宋体"}]{#struct_0_21171_18224_x194631192}**[bert]{lang="EN-US"}**[命令配置好测试模式，指定测试持续时间，开始测试后，可以查看接口状态中的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果。]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果的说明详见]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1048858157}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1387443314}[在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[上执行]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_634897330}

[\[Sysname\] interface t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] bert pattern qrss time 10]{lang="EN-US"}
:::

::: {#-798614504 .myid}
[]{#_Toc404785219}[]{#struct_0_21171_18224_x834751907}[]{#_Toc325463698}[]{#_Toc318123781}

**WAN接口 \-- CT3接口配置命令 \-- cable**

------------------------------------------------------------------------

[**[cable]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_21171_18224_212919512}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口所连接电缆的长度。]{style="font-family:宋体"}

[**[undo cable]{lang="EN-US"}**]{#struct_0_21171_18224_x810104533}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_858367109}

[**[cable]{lang="EN-US"}***[ feet]{lang="EN-US"}*]{#struct_0_21171_18224_1006896490}

[**[undo cable]{lang="EN-US"}**]{#struct_0_21171_18224_x2128933857}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1300507428}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x2066448106}[接口所连接电缆的长度为]{style="font-family:宋体"}[49]{lang="EN-US"}[英尺。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_521018513}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_212853976}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_344670455}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_182348048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1504588644}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_209569818}

[*[feet]{lang="EN-US"}*]{#struct_0_21171_18224_1919133582}[：电缆长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[450]{lang="EN-US"}[，单位为英尺（]{style="font-family:宋体"}[feet]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_535799597}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x162739206}[接口所连接电缆的长度是指从路由器到配线架之间电缆的长度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_212788440}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1734038507}[设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的电缆长度为]{style="font-family:宋体"}[50]{lang="EN-US"}[英尺。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x472008206}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] cable 50]{lang="EN-US"}
:::

::: {#-441129672 .myid}
[]{#_Toc404785220}[]{#struct_0_21171_18224_x80454461}[]{#_Toc325463699}[]{#_Toc318123782}

**WAN接口 \-- CT3接口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_x1106984016}[命令用来设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_x110810202}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_160158497}

[**[clock]{lang="EN-US"}**]{#struct_0_21171_18224_x1752500817}[ { ]{lang="EN-US"}**[master]{lang="EN-US"}**[ ]{lang="EN-US"}[\| ]{lang="EN-US"}**[slave ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_21171_18224_212722904}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x658882420}

[[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_x784004648}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_319821421}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_2147361364}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_271297355}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1947690618}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1631018044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_212657368}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_499877195}[：主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_1840631671}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_969324584}

[[使用主时钟模式还是从时钟模式，主要根据所连接的对端设备而定，如果与传输设备相连，本端通常设置为从时钟模式。]{style="font-family:宋体"}]{#struct_0_21171_18224_2009191499}

[[如果是两台路由器的]{style="font-family:宋体"}[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x709522518}[接口直接相连，则应该把一端路由器时钟设置为主时钟模式，另一端路由器时钟设置为从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1027016715}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_403851945}[设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_212591832}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] clock master]{lang="EN-US"}
:::

::: {#-1883381392 .myid}
[]{#_Toc404785221}[]{#struct_0_21171_18224_x1323382036}[]{#_Toc325463700}[]{#_Toc318123783}

**WAN接口 \-- CT3接口配置命令 \-- controller t3**

------------------------------------------------------------------------

[**[controller t3]{lang="EN-US"}**]{#struct_0_21171_18224_1288989469}[命令用来进入]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_563627536}

[**[controller t3]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1470186165}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_2144563380}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1561214251}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_212526296}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1864306765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1553207183}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_784332045}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_1200630260}[：]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1068227678}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1501058926}[进入]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_212460760}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\]]{lang="EN-US"}
:::

::: {#-1845900349 .myid}
[]{#_Toc404785222}[]{#struct_0_21171_18224_1443279622}[]{#_Toc325463702}[]{#_Toc318123784}

**WAN接口 \-- CT3接口配置命令 \-- display controller t3**

------------------------------------------------------------------------

[**[display controller t3]{lang="EN-US"}**]{#struct_0_21171_18224_x1169138295}[命令用来显示]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x679752406}

[**[display controller]{lang="EN-US"}**[ **t3**]{lang="EN-US"}]{#struct_0_21171_18224_2073619415}[ \[ ]{lang="EN-US"}*[interface-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1359343786}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21171_18224_1563632061}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_324811961}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_213443800}

[[network-operator]{lang="EN-US"}]{#struct_0_21171_18224_1157213686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_821741434}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21171_18224_1806758066}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1107675239}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_1199073964}[：]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口编号。不指定本参数，将显示所有]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_576453346}

[[本命令可以显示]{style="font-family:宋体"}[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x1143103229}[接口的状态信息，同时还可以显示]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口工作在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[模式时每个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_213378264}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1452084811}[显示]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller t3 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_212853977}

[T3 2/4/0]{lang="EN-US"}

[Current state: UP  ]{lang="EN-US"}

[Description: T3 2/4/0 Interface]{lang="FR"}

[Basic Configuration:]{lang="FR"}

[  ]{lang="FR"}[Work mode: CT3, cable length: 49 feet]{lang="EN-US"}

[  Frame-format: C-BIT Parity, line code: B3ZS]{lang="EN-US"}

[  Source clock: slave, loopback: not set]{lang="EN-US"}

[Alarm state:]{lang="EN-US"}

[  Receiver alarm state is none]{lang="EN-US"}

[MDL state:]{lang="EN-US"}

[  No message is sent now.]{lang="EN-US"}

[  Message data elements:]{lang="EN-US"}

[    EIC: line, LIC: line, FIC: line, UNIT: line]{lang="EN-US"}

[    FI: line, PORT_NO: line, GEN_NO: line]{lang="EN-US"}

[  Periodical detection: disabled]{lang="EN-US"}

[FEAC state:]{lang="EN-US"}

[  No code is sent now.]{lang="EN-US"}

[  Periodical detection is enabled, no code received now.]{lang="EN-US"}

[BERT state:(stopped, not completed)]{lang="EN-US"}

[    Test pattern: 2\^7, Status: Not Sync, Sync Detected: 0]{lang="EN-US"}

[      Time: 0 minutes, Time past: 0 minutes]{lang="EN-US"}

[      Bit errors (since test started): 0 bits]{lang="EN-US"}

[      Bits received (since test started): 0 Mbits]{lang="EN-US"}

[      Bit errors (since latest sync): 0 bits]{lang="EN-US"}

[      Bits received (since latest sync): 0 Mbits]{lang="EN-US"}

[Historical Statistics:]{lang="EN-US"}

[  Last link flapping: 6 hours 39 minutes 25 seconds]{lang="EN-US"}

[  Last clearing of counters: 14:39:02 UTC Sat 06/25/2005]{lang="EN-US"}

[  Data in current interval (22 seconds elapsed):]{lang="EN-US"}

[    Line Code Violations: 0 seconds Far End Block Error: 0 seconds]{lang="EN-US"}

[    C-Bit Coding Violation: 0 seconds]{lang="EN-US"}

[    P-bit Coding Violation: 0 seconds]{lang="EN-US"}

[    Framing Bit Err: 0 seconds, Severely Err Framing: 0 seconds]{lang="EN-US"}

[    C-bit Err: 0 seconds, C-bit Severely Err: 0 seconds]{lang="EN-US"}

[    P-bit Err: 0 seconds, P-bit Severely Err: 0 seconds]{lang="EN-US"}

[    Unavailable: 0 seconds, Line Err: 0 seconds]{lang="EN-US"}

[ T3 2/4/0  CT1 1: up]{lang="EN-US"}

[   Frame-format: ESF, clock: slave, loopback: not set]{lang="EN-US"}

[   FDL Performance Report: disabled]{lang="EN-US"}

[   Transmitter is sending none]{lang="EN-US"}

[   Receiver alarm state is none]{lang="EN-US"}

[   Line loop back deactivate code using inband signal last sent]{lang="EN-US"}

[   BERT state:(stopped, not completed)]{lang="EN-US"}

[     Test pattern: 2\^11, Status: Not Sync, Sync Detected: 0]{lang="EN-US"}

[       Time: 0 minutes, Time past: 0 minutes]{lang="EN-US"}

[       Bit errors (since test started): 0 bits]{lang="EN-US"}

[       Bits received (since test started): 0 Kbits]{lang="EN-US"}

[       Bit errors (since latest sync): 0 bits]{lang="EN-US"}

[       Bits received (since latest sync): 0 Kbits]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display controller t3]{lang="EN-US"}]{#struct_0_21171_18224_344670454}[命令显示信息解释]{style="font-family:黑体"}

[]{#table_struct_0_1676222062}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_182348047}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_1504588633}

[[T3 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_209766431}

[[Current state]{lang="EN-US"}]{#struct_0_21171_18224_212788441}

[[接口的物理]{style="font-family:宋体"}[up/down]{lang="EN-US"}]{#struct_0_21171_18224_1734038508}[状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_21171_18224_x471811598}

[[接口描述信息]{style="font-family:宋体"}]{#struct_0_21171_18224_x1129738641}

[[Basic Configuration]{lang="EN-US"}]{#struct_0_21171_18224_1551516097}

[[接口基本配置信息]{style="font-family:宋体"}]{#struct_0_21171_18224_212722905}

[[Work mode]{lang="EN-US"}]{#struct_0_21171_18224_x658882419}

[[工作模式，包括通道化（]{style="font-family:宋体"}[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x784594473}[）和非通道化（]{style="font-family:宋体"}[T3]{lang="EN-US"}[）]{style="font-family:宋体"}

[[cable length]{lang="EN-US"}]{#struct_0_21171_18224_712382267}

[[线缆长度]{style="font-family:宋体"}]{#struct_0_21171_18224_1560544409}

[[Frame-format]{lang="EN-US"}]{#struct_0_21171_18224_212657369}

[[帧格式，包括]{style="font-family:宋体"}[C-bit]{lang="EN-US"}]{#struct_0_21171_18224_499877194}[和]{style="font-family:宋体"}[M23]{lang="EN-US"}

[[line code]{lang="EN-US"}]{#struct_0_21171_18224_1840631672}

[[线路编码]{style="font-family:宋体"}]{#struct_0_21171_18224_969127976}

[[Source clock]{lang="EN-US"}]{#struct_0_21171_18224_212591833}

[[时钟模式，包括]{style="font-family:宋体"}[master]{lang="EN-US"}]{#struct_0_21171_18224_x1323382037}[和]{style="font-family:宋体"}[slave]{lang="EN-US"}

[[loopback]{lang="EN-US"}]{#struct_0_21171_18224_x277094472}

[[接口是否设置了环回]{style="font-family:宋体"}]{#struct_0_21171_18224_x1397369852}

[[Alarm state]{lang="EN-US"}]{#struct_0_21171_18224_553434339}

[[告警状态]{style="font-family:宋体"}]{#struct_0_21171_18224_212526297}

[[Receiver alarm state is none]{lang="EN-US"}]{#struct_0_21171_18224_1864306766}

[[显示接口收到的告警类别，包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_21171_18224_1553141647}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[当收到]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_21171_18224_x1587302310}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[之一时，向对方发送]{style="font-family:宋体"}[RAI]{lang="EN-US"}[，显示：]{style="font-family:宋体"}[Transmitter is sending RAI]{lang="EN-US"}

[[MDL state]{lang="EN-US"}]{#struct_0_21171_18224_212460761}

[[MDL]{lang="EN-US"}]{#struct_0_21171_18224_1443279623}[状态]{style="font-family:宋体"}

[[No message is sent now.]{lang="EN-US"}]{#struct_0_21171_18224_x1169072759}

[[当前没有发送]{style="font-family:宋体"}[MDL]{lang="EN-US"}]{#struct_0_21171_18224_x606659929}[消息]{style="font-family:宋体"}

[[发送]{style="font-family:宋体"}[MDL]{lang="EN-US"}]{#struct_0_21171_18224_213443801}[消息（如]{style="font-family:宋体"}[path]{lang="EN-US"}[和]{style="font-family:宋体"}[idle-signal]{lang="EN-US"}[）时，显示如下：]{style="font-family:宋体"}

[[Message sent now: path. idle signal]{lang="EN-US"}]{#struct_0_21171_18224_1157213687}

[[Message data elements:]{lang="EN-US"}]{#struct_0_21171_18224_821675898}

[[MDL]{lang="EN-US"}]{#struct_0_21171_18224_x1719942277}[数据元素]{style="font-family:宋体"}

[[EIC: line, LIC: line, FIC: line, UNIT: line]{lang="EN-US"}]{#struct_0_21171_18224_213378265}

[[EIC]{lang="EN-US"}]{#struct_0_21171_18224_x1452084812}[、]{style="font-family:宋体"}[LIC]{lang="EN-US"}[、]{style="font-family:宋体"}[FIC]{lang="EN-US"}[和]{style="font-family:宋体"}[UNIT]{lang="EN-US"}[为四种]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息的公共元素，用户可设置]{style="font-family:宋体"}

[[FI: line, PORT_NO: line, GEN_NO: line]{lang="EN-US"}]{#struct_0_21171_18224_x1357430606}

[[FI]{lang="EN-US"}]{#struct_0_21171_18224_212919510}[、]{style="font-family:宋体"}[PORT_NO]{lang="EN-US"}[和]{style="font-family:宋体"}[GEN_NO]{lang="EN-US"}[分别为消息]{style="font-family:宋体"}[path]{lang="EN-US"}[、]{style="font-family:宋体"}[idle-signal]{lang="EN-US"}[和]{style="font-family:宋体"}[test-signal]{lang="EN-US"}[的私有元素，用户可设置]{style="font-family:宋体"}

[[Periodical detection: disabled.]{lang="EN-US"}]{#struct_0_21171_18224_x810104531}

[[MDL]{lang="EN-US"}]{#struct_0_21171_18224_858498181}[周期性检测被禁止。上电后默认为禁止。]{style="font-family:宋体"}

[[当该检测功能被使能时，显示：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1066793283}

[[Periodical detection is enabled.]{lang="EN-US"}]{#struct_0_21171_18224_212853974}

[[No message was received. ]{lang="EN-US"}]{#struct_0_21171_18224_344670457}

[[当检测到]{style="font-family:宋体"}[MDL]{lang="EN-US"}]{#struct_0_21171_18224_182348046}[消息时显示如：]{style="font-family:宋体"}

[[Message received now: path.idle signal.]{lang="EN-US"}]{#struct_0_21171_18224_212788438}

[[    EIC: line, LIC: line, FIC: line, UNIT: line]{lang="EN-US"}]{#struct_0_21171_18224_x222276621}

[[    path/FI: line]{lang="EN-US"}]{#struct_0_21171_18224_2040797054}

[[    idle Signal/PORT_NO: line]{lang="EN-US"}]{#struct_0_21171_18224_212722902}

[[FEAC state:]{lang="EN-US"}]{#struct_0_21171_18224_x658882418}

[[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_x784528937}[状态]{style="font-family:宋体"}

[[No code is sent now. DS3 Line Loop Back Deactivate was last sent.]{lang="EN-US"}]{#struct_0_21171_18224_212657366}

[[当前没有]{style="font-family:宋体"}[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_499877205}[信号发出，上次发出的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[信号为]{style="font-family:宋体"}[DS3 Line Loop Back Deactivate]{lang="EN-US"}

[[Periodical detection is enabled, no code received now.]{lang="EN-US"}]{#struct_0_21171_18224_x461284644}

[[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_212591830}[周期性检测功能被使能。上电后默认使能。]{style="font-family:宋体"}

[[当前未收到]{style="font-family:宋体"}[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_x1323382034}[信号]{style="font-family:宋体"}

[[DS3 Line Loop Back Deactivate last received.]{lang="EN-US"}]{#struct_0_21171_18224_126190055}

[[上次收到的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_212526294}[信号为]{style="font-family:宋体"}[DS3 Line Loop Back Deactivate]{lang="EN-US"}

[[BERT state:(stopped, not completed)]{lang="EN-US"}]{#struct_0_21171_18224_1864306767}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_1553076111}[状态（停止）]{style="font-family:宋体"}

[[根据用户进行]{style="font-family:宋体"}[BERT]{lang="EN-US"}]{#struct_0_21171_18224_212460758}[操作的情况，有三种状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[running]{lang="EN-US"}]{#struct_0_21171_18224_x130698498}[－]{lang="EN-US" style="font-family:宋体"}[BERT]{lang="EN-US"}[测试正在进行；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[complete]{lang="EN-US"}]{#struct_0_21171_18224_x165181516}[－]{lang="EN-US" style="font-family:宋体"}[BERT]{lang="EN-US"}[测试自然完成（即达到测试时间）；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stopped]{lang="EN-US"}]{#struct_0_21171_18224_213443798}[－]{lang="EN-US" style="font-family:宋体"}[BERT]{lang="EN-US"}[测试被提前中止]{lang="EN-US" style="font-family:宋体"}

[[Test pattern: 2\^7, Status: Not Sync, Sync Detected: 0]{lang="EN-US"}]{#struct_0_21171_18224_2013571909}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_x506035156}[测试模式，包括]{style="font-family:宋体"}[2\^7]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[以及]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[等]{style="font-family:宋体"}

[[同步状态：是否同步]{style="font-family:宋体"}]{#struct_0_21171_18224_213378262}

[[子测试开始后检测到的同步次数]{style="font-family:宋体"}]{#struct_0_21171_18224_x1452084813}

[[Time]{lang="EN-US"}]{#struct_0_21171_18224_212919511}

[[总的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_x810104532}

[[Time past]{lang="EN-US"}]{#struct_0_21171_18224_858432645}

[[已经完成的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_212853975}

[[Bit errors (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_344670456}

[[自测试开始后收到的错误比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_182348045}

[[Bits received (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_212788439}

[[自测试开始后收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_x222276620}

[[Bit errors (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_212722903}

[[自上一次同步以来收到的错误比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_x658882417}

[[Bits received (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_x784201257}

[[自上一次同步以来收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_212657367}

[[Historical Statistics:]{lang="EN-US"}]{#struct_0_21171_18224_499877204}

[[历史统计数据]{style="font-family:宋体"}]{#struct_0_21171_18224_212591831}

[[Last link flapping]{lang="EN-US"}]{#struct_0_21171_18224_744643986}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_x1533900675}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_21171_18224_x668071098}

[[上次清零时间。从未清零显示]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_21171_18224_x1439893886}[，否则显示时间如：]{style="font-family:宋体"}

[[14:39:02 UTC Sat 06/25/2010]{lang="EN-US"}]{#struct_0_21171_18224_212526295}

[[Data in current interval (22 seconds elapsed):]{lang="EN-US"}]{#struct_0_21171_18224_1864306768}

[[当前]{style="font-family:宋体"}[interval]{lang="EN-US"}]{#struct_0_21171_18224_212460759}[（]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟为一个]{style="font-family:宋体"}[interval]{lang="EN-US"}[）内的各项错误计数（已过去的时间为]{style="font-family:宋体"}[22]{lang="EN-US"}[秒）]{style="font-family:宋体"}

[[Line Code Violations]{lang="EN-US"}]{#struct_0_21171_18224_x130698497}

[[线路信号错误数，包括：]{style="font-family:宋体"}[BPV]{lang="EN-US"}]{#struct_0_21171_18224_213443799}[错误、]{style="font-family:宋体"}[EXZ]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Far End Block Error]{lang="EN-US"}]{#struct_0_21171_18224_2013571910}

[[远端块错误数]{style="font-family:宋体"}]{#struct_0_21171_18224_x506624981}

[[C-Bit Coding violation]{lang="EN-US"}]{#struct_0_21171_18224_213378263}

[[C]{lang="EN-US"}]{#struct_0_21171_18224_x1452084814}[比特错误数]{style="font-family:宋体"}

[[P-bit Coding Violation]{lang="EN-US"}]{#struct_0_21171_18224_1779003455}

[[P]{lang="EN-US"}]{#struct_0_21171_18224_x871978586}[比特错误数]{style="font-family:宋体"}

[[Framing Bit Err]{lang="EN-US"}]{#struct_0_21171_18224_1778937919}

[[帧比特错误数]{style="font-family:宋体"}]{#struct_0_21171_18224_997292773}

[[Severely Err Framing Secs]{lang="EN-US"}]{#struct_0_21171_18224_1778872383}

[[帧比特严重错误的秒数]{style="font-family:宋体"}]{#struct_0_21171_18224_x518054596}

[[C-bit Err Secs]{lang="EN-US"}]{#struct_0_21171_18224_1778806847}

[[C]{lang="EN-US"}]{#struct_0_21171_18224_1397682084}[比特错误的秒数]{style="font-family:宋体"}

[[C-bit Severely Err Secs]{lang="EN-US"}]{#struct_0_21171_18224_1778741311}

[[C]{lang="EN-US"}]{#struct_0_21171_18224_x106184695}[比特严重错误的秒数，指]{style="font-family:宋体"}[1]{lang="EN-US"}[秒内]{style="font-family:宋体"}[C]{lang="EN-US"}[比特错误数超过]{style="font-family:宋体"}[44]{lang="EN-US"}[的秒]{style="font-family:宋体"}

[[P-bit Err Secs]{lang="EN-US"}]{#struct_0_21171_18224_x791231676}

[[P]{lang="EN-US"}]{#struct_0_21171_18224_1778675775}[比特错误的秒数]{style="font-family:宋体"}

[[P-bit Severely Err Secs]{lang="EN-US"}]{#struct_0_21171_18224_1445761680}

[[P]{lang="EN-US"}]{#struct_0_21171_18224_1778610239}[特严重错误的秒数，指]{style="font-family:宋体"}[1]{lang="EN-US"}[秒内]{style="font-family:宋体"}[P]{lang="EN-US"}[比特错误数超过]{style="font-family:宋体"}[44]{lang="EN-US"}[的秒]{style="font-family:宋体"}

[[Unavailable Secs]{lang="EN-US"}]{#struct_0_21171_18224_286733507}

[[服务无法获取的秒数]{style="font-family:宋体"}]{#struct_0_21171_18224_1778544703}

[[Line Err Secs]{lang="EN-US"}]{#struct_0_21171_18224_x111212849}

[[线路错误的秒数，包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_21171_18224_1779527743}[、]{style="font-family:宋体"}[BPV]{lang="EN-US"}[、]{style="font-family:宋体"}[EXZ]{lang="EN-US"}[、]{style="font-family:宋体"}[C]{lang="EN-US"}[比特错误、]{style="font-family:宋体"}[P]{lang="EN-US"}[比特错误等]{style="font-family:宋体"}

[[Data in Interval 1:]{lang="EN-US"}]{#struct_0_21171_18224_1779462207}

[[Interval 1]{lang="EN-US"}]{#struct_0_21171_18224_x1310450248}[内的数据]{style="font-family:宋体"}

[[Total Data (last 17 15 minute intervals):]{lang="EN-US"}]{#struct_0_21171_18224_1779003456}

[[总的数据（前]{style="font-family:宋体"}[17]{lang="EN-US"}]{#struct_0_21171_18224_x871913050}[个]{style="font-family:宋体"}[interval]{lang="EN-US"}[）]{style="font-family:宋体"}

[[T3 2/4/0  CT1 1: up]{lang="EN-US"}]{#struct_0_21171_18224_1778937920}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_996834024}[接口下]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[up/down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Frame-format: ESF, clock: slave, loopback: not set]{lang="EN-US"}]{#struct_0_21171_18224_1778872384}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_x518382276}[通道的帧格式，包括]{style="font-family:宋体"}[ESF]{lang="EN-US"}[和]{style="font-family:宋体"}[SF]{lang="EN-US"}

[[时钟方式包括]{style="font-family:宋体"}[slave]{lang="EN-US"}]{#struct_0_21171_18224_1778806848}[和]{style="font-family:宋体"}[master]{lang="EN-US"}[，环回包括]{style="font-family:宋体"}[local]{lang="EN-US"}[、]{style="font-family:宋体"}[remote]{lang="EN-US"}[和]{style="font-family:宋体"}[payload]{lang="EN-US"}

[[FDL Performance Report:  disabled]{lang="EN-US"}]{#struct_0_21171_18224_1398271908}

[[禁止用]{style="font-family:宋体"}[FDL]{lang="EN-US"}]{#struct_0_21171_18224_1778741312}[链路传输性能报告信息（]{style="font-family:宋体"}[PPR]{lang="EN-US"}[），可用]{style="font-family:宋体"}**[fdl ansi]{lang="DE"}**[命令使能]{style="font-family:宋体"}

[[Transmitter is sending RAI]{lang="EN-US"}]{#struct_0_21171_18224_x106119159}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_1778675776}[通道发送器在发送]{style="font-family:宋体"}[RAI]{lang="EN-US"}[。当收到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[时，发]{style="font-family:宋体"}[RAI]{lang="EN-US"}

[[Receiver alarm state is LOF]{lang="EN-US"}]{#struct_0_21171_18224_1445958288}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_1778610240}[通道接收到的告警状态，包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[和]{style="font-family:宋体"}[RAI]{lang="EN-US"}

[[Line loop back activate code using inband signal last sent]{lang="EN-US"}]{#struct_0_21171_18224_286274752}

[[上次发送的环回码：]{style="font-family:宋体"}[Line loop back activate code using inband signal]{lang="EN-US"}]{#struct_0_21171_18224_1778544704}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x111147313}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters controller t3]{lang="EN-US"}**]{#struct_0_21171_18224_2096580278}

::: {#-1524568353 .myid}
[]{#_Toc404785223}[]{#struct_0_21171_18224_186666064}[]{#_Toc325463703}[]{#_Toc318123785}

**WAN接口 \-- CT3接口配置命令 \-- feac**

------------------------------------------------------------------------

[**[feac]{lang="EN-US"}**]{#struct_0_21171_18224_1043551110}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[链路信号的检测和传输功能。]{style="font-family:宋体"}

[**[undo feac]{lang="EN-US"}**]{#struct_0_21171_18224_1779527744}[命令用来取消已有的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x506561690}

[**[feac]{lang="EN-US"}**[ { **detect** \| **generate** { **ds3-los** \| **ds3-ais** \| **ds3-oof** \| **ds3-idle** \| **ds3-eqptfail** \| **loopback** { **ds3-line** \| **ds3-payload** } } }]{lang="EN-US"}]{#struct_0_21171_18224_x643471900}

[**[undo feac]{lang="EN-US"}**[ { **detect** \| **generate** { **ds3-los** \| **ds3-ais** \| **ds3-oof** \| **ds3-idle** \| **ds3-eqptfail** \| **loopback** { **ds3-line** \| **ds3-payload** } } }]{lang="EN-US"}]{#struct_0_21171_18224_x1614707224}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_257531171}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_1104982856}[接口的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[定时检测功能处于打开状态，传输功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1365981586}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_712623944}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1779462208}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1310646856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1258640426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1614813506}

[**[detect]{lang="EN-US"}**]{#struct_0_21171_18224_75081291}[：]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口上的定时检测]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[链路信号功能。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_21171_18224_1567435995}[：发送]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[信号，包括]{style="font-family:宋体"}**[ds3-los]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-ais]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-oof]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-idle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-eqptfail]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x352478633}[：发送环回码，用于激活对端的线路环回（]{style="font-family:宋体"}**[ds3-line]{lang="EN-US"}**[）或者净荷环回（]{style="font-family:宋体"}**[ds3-payload]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_81041250}

[[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_1779003453}[（]{style="font-family:宋体"}[Far End Alarm and Control signal]{lang="EN-US"}[，远端告警与控制信号）是利用]{style="font-family:宋体"}[C-bit]{lang="EN-US"}[帧格式中第一个子帧中的第三个]{style="font-family:宋体"}[C]{lang="EN-US"}[比特组成的一条数据链路，可用于传输各种告警状态信号，也可用于传输环回控制码，用来激活或者取消对端的环回，进行环回测试。]{style="font-family:宋体"}[ANSI T1.107a]{lang="EN-US"}[中规定，]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[可用于传输多种告警信号（本命令中实现如上几种，多用于线路测试），并规定这条链路的数据帧为基于位的]{style="font-family:宋体"}[BOP]{lang="EN-US"}[（]{style="font-family:宋体"}[Bit Oriented Protocol]{lang="EN-US"}[）协议格式。]{style="font-family:宋体"}

[[上电后，]{style="font-family:宋体"}[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x871585370}[接口的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[定时检测功能是打开的，但不发送任何]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[当用]{style="font-family:宋体"}**[feac generate loopback]{lang="EN-US"}**[ { **ds3-line** \| **ds3-payload** }]{lang="EN-US"}]{#struct_0_21171_18224_x1151311820}[激活对端环回后，可用]{style="font-family:宋体"}**[undo feac generate loopback ]{lang="EN-US"}**[{ **ds3-line** \| **ds3-payload** }]{lang="EN-US"}[取消对端环回。]{style="font-family:宋体"}

[[需要注意的是，当利用该命令配置远端环回前，最好禁止本端的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_1852783107}[检测，以免发出的环回码在对方配好环回后被返回来，造成本端也配置为环回，引起线路上的环路死锁。]{style="font-family:宋体"}

[[FEAC]{lang="EN-US"}]{#struct_0_21171_18224_x578566433}[链路的收发状态的说明详见]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x740377086}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1769982461}[打开]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[链路数据检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1778937917}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] feac detect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_997161701}[在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[上发送]{style="font-family:宋体"}[ds3-los]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1741724019}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] feac generate ds3-los]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1001550087}[在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[上发送环回码给对端，设置对端为线路环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_228336463}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] feac generate loopback ds3-line ]{lang="EN-US"}
:::

::: {#1701559760 .myid}
[]{#_Toc404785224}[]{#struct_0_21171_18224_1323318459}[]{#_Toc325463704}[]{#_Toc318123786}

**WAN接口 \-- CT3接口配置命令 \-- frame-format**

------------------------------------------------------------------------

[**[frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_986503384}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="SV"}[接口所使用的帧格式。]{style="font-family:宋体"}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_1778872381}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x518185668}

[**[frame-format]{lang="SV"}**]{#struct_0_21171_18224_90255336}[ { **c-bit** \| **m23** }]{lang="SV"}

[**[undo frame-format]{lang="SV"}**]{#struct_0_21171_18224_832996057}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2097000811}

[[CT3]{lang="SV"}]{#struct_0_21171_18224_356788771}[接口的帧格式为]{style="font-family:宋体"}**[c-bit]{lang="SV"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1884128737}

[[CT3]{lang="SV"}]{#struct_0_21171_18224_x1075150363}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778806845}

[[network-admin]{lang="SV"}]{#struct_0_21171_18224_1397551012}

[[mdc-admin]{lang="SV"}]{#struct_0_21171_18224_1820844912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1855299477}

[**[c-bit]{lang="EN-US"}**]{#struct_0_21171_18224_x1261042975}[：设置帧格式为]{style="font-family:宋体"}[C-bit]{lang="SV"}[。]{style="font-family:宋体"}

[**[m23]{lang="EN-US"}**]{#struct_0_21171_18224_x1233083491}[：设置帧格式为]{style="font-family:宋体"}[m23]{lang="SV"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_79460393}

[[只有当]{style="font-family:宋体"}]{#struct_0_21171_18224_810831046}[CT3]{lang="SV"}[接口工作在通道化模式时，才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778741309}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x105660406}[设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}**[m23]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1325068708}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] frame-format m23]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x692332360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[using]{lang="EN-US"}**]{#struct_0_21171_18224_417807527}
:::

::: {#-1619675867 .myid}
[]{#_Toc404785225}[]{#struct_0_21171_18224_307920336}[]{#_Toc325463705}[]{#_Toc318123787}

**WAN接口 \-- CT3接口配置命令 \-- ft3**

------------------------------------------------------------------------

[**[ft3]{lang="EN-US"}**]{#struct_0_21171_18224_x1428578084}[命令用于配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口工作在]{style="font-family:宋体"}[FT3]{lang="EN-US"}[模式，并配置]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式或子速率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**]{#struct_0_21171_18224_1778675773}**[ ]{lang="EN-US"}[ft3]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1446154896}

[**[ft3]{lang="EN-US"}**[ { **dsu-mode** { **0** \| **1 \| 2 \| 3 \| 4** } \| **subrate** *number* }]{lang="EN-US"}]{#struct_0_21171_18224_x145723068}

[**[undo ft3]{lang="EN-US"}**[ { **dsu-mode** \| **subrate** }]{lang="EN-US"}]{#struct_0_21171_18224_1569561812}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_274122690}

[[DSU]{lang="EN-US"}]{#struct_0_21171_18224_261978992}[模式为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即]{style="font-family:宋体"}[Digital Link]{lang="EN-US"}[模式；子速率为]{style="font-family:宋体"}[44210kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x686675773}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x1949725643}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778610237}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_286340291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1747726598}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1833666521}

[**[dsu-mode]{lang="EN-US"}**]{#struct_0_21171_18224_x724292703}[：设置]{style="font-family:宋体"}[FT3]{lang="EN-US"}[的]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式，支持常用的几家厂商的]{style="font-family:宋体"}[FT3 DSU]{lang="EN-US"}[模式，如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[0]{lang="EN-US"}**]{#struct_0_21171_18224_x1330648597}[：]{lang="EN-US" style="font-family:宋体"}[Digital Link]{lang="EN-US"}[，支持子速率范围为]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{lang="EN-US" style="font-family:宋体"}[147]{lang="EN-US"}[个速率等级，级差]{lang="EN-US" style="font-family:宋体"}[300746bps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[1]{lang="EN-US"}**]{#struct_0_21171_18224_x1775361932}[：]{lang="EN-US" style="font-family:宋体"}[Kentrox]{lang="EN-US"}[，支持子速率范围为]{lang="EN-US" style="font-family:宋体"}[1500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[35000kbps]{lang="EN-US"}[及]{lang="EN-US" style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{lang="EN-US" style="font-family:宋体"}[69]{lang="EN-US"}[个速率等级，级差]{lang="EN-US" style="font-family:宋体"}[500000bps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[2]{lang="EN-US"}**]{#struct_0_21171_18224_x806860639}[：]{style="font-family:
宋体"}[Larscom]{lang="EN-US"}[，支持子速率范围为]{style="font-family:宋体"}[3100]{lang="EN-US"}[～]{style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{style="font-family:宋体"}[14]{lang="EN-US"}[个速率等级，级差]{style="font-family:宋体"}[3157835bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[3]{lang="EN-US"}**]{#struct_0_21171_18224_1778544701}[：]{style="font-family:
宋体"}[Adtran]{lang="EN-US"}[，支持子速率范围为]{style="font-family:宋体"}[75]{lang="EN-US"}[～]{style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{style="font-family:宋体"}[588]{lang="EN-US"}[个速率等级，级差]{style="font-family:宋体"}[75187bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[4]{lang="EN-US"}**]{#struct_0_21171_18224_x111343921}[：]{lang="EN-US" style="font-family:宋体"}[Verilink]{lang="EN-US"}[，支持子速率范围为]{lang="EN-US" style="font-family:宋体"}[1500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{lang="EN-US" style="font-family:宋体"}[20]{lang="EN-US"}[个速率等级，级差]{lang="EN-US" style="font-family:宋体"}[1578918bps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[subrate]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_21171_18224_x2140572563}[：工作在]{style="font-family:宋体"}[FT3]{lang="EN-US"}[模式下的]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的子速率。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[44210]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x665553105}

[[FT3]{lang="EN-US"}]{#struct_0_21171_18224_1058897653}[（]{style="font-family:宋体"}[Fractional T3]{lang="EN-US"}[，或称]{style="font-family:宋体"}[Subrate T3]{lang="EN-US"}[）是]{style="font-family:宋体"}[T3]{lang="EN-US"}[的一种非标准应用模式。目前各厂商支持的速率等级均不一样，使用]{style="font-family:宋体"}**[ft3]{lang="EN-US"}**[命令可以使我们的设备和其它厂家设备的]{style="font-family:宋体"}[FT3 DSU]{lang="EN-US"}[模式兼容，实现互通。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21171_18224_x1493175345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令仅在支持]{style="font-family:宋体"}]{#struct_0_21171_18224_1892441257}[FT3]{lang="EN-US"}[特性的]{style="font-family:宋体"}[CT3]{lang="EN-US"}[单板上有效，如]{style="font-family:宋体"}[CT3]{lang="EN-US"}[单板不支持]{style="font-family:宋体"}[FT3]{lang="EN-US"}[特性，系统将提示该命令无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令仅能在]{style="font-family:宋体"}]{#struct_0_21171_18224_1722409865}[T3]{lang="EN-US"}[模式下使用，在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[模式下该命令不可见。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21171_18224_1779527741}**[ft3 subrate]{lang="EN-US"}**[设置的速率值是一个大概值。由于通过]{lang="EN-US" style="font-family:宋体"}**[ft3 dsu-mode]{lang="EN-US"}**[命令配置的各]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[的子速率值是离散的，因此，当再通过]{lang="EN-US" style="font-family:宋体"}**[ft3 subrate]{lang="EN-US"}**[命令指定子速率后，]{lang="EN-US" style="font-family:宋体"}[T3]{lang="EN-US"}[接口会根据当前配置的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式计算出与这个指定子速率最匹配的精确速率（精确到]{lang="EN-US" style="font-family:宋体"}[bps]{lang="EN-US"}[），并设置硬件电路支持该速率。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21171_18224_x506758298}**[display interface serial interface-number:0]{lang="EN-US"}**[命令可以查看]{lang="EN-US" style="font-family:宋体"}[T3]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式、子速率设置值、接口实际速率和接口的波特率。接口实际速率为不含开销在内的纯数据带宽，接口波特率（]{lang="EN-US" style="font-family:宋体"}[44736kbps]{lang="EN-US"}[）为]{lang="EN-US" style="font-family:宋体"}[T3]{lang="EN-US"}[线路的实际速率（含开销位在内）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_502961763}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1754550524}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[FT3]{lang="EN-US"}[模式，]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式为]{style="font-family:宋体"}[1]{lang="EN-US"}[，子速率为]{style="font-family:宋体"}[3000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x138164821}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] using t3]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] ft3 dsu-mode 1]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] ft3 subrate 3000]{lang="EN-US"}
:::

::: {#-311773076 .myid}
[]{#_Toc404785226}[]{#struct_0_21171_18224_867307426}[]{#_Toc325463706}[]{#_Toc318123788}

**WAN接口 \-- CT3接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1804590847}[命令用来开启]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_1779462205}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1310319176}

[**[loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x218621918}[ {]{lang="EN-US"}**[ local]{lang="EN-US"}[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[payload]{lang="EN-US"}[ ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[remote ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1134862781}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1548080188}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_x2053676051}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1900469475}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_1779003454}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x872044122}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1037358089}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1886340594}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1619426424}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_x1377047080}[：设置接口对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_x248575306}[：设置接口对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_x1792756898}[：设置接口对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1047892865}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_1778937918}[接口两种对外环回的区别在于：对外载荷环回（]{style="font-family:宋体"}**[payload]{lang="EN-US"}**[）需要处理帧头开销，而对外远端环回（]{style="font-family:宋体"}**[remote]{lang="EN-US"}**[）则不对帧进行处理。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}]{#struct_0_21171_18224_997358309}[CT3]{lang="EN-US"}[接口的链路层协议配置为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[，在设置环回后，其链路层协议状态将上报为]{style="font-family:宋体"}[down]{lang="EN-US"}[，这属于正常情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x296630496}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_445195886}[设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[对内自环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x473058405}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] loopback local]{lang="EN-US"}
:::

::: {#-1385453599 .myid}
[]{#_Toc404785227}[]{#struct_0_21171_18224_1092705475}[]{#_Toc325463707}[]{#_Toc318123789}

**WAN接口 \-- CT3接口配置命令 \-- mdl**

------------------------------------------------------------------------

[**[mdl]{lang="EN-US"}**]{#struct_0_21171_18224_x1882212828}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[链路消息检测与传输功能。]{style="font-family:宋体"}

[**[undo mdl]{lang="EN-US"}**]{#struct_0_21171_18224_1778872382}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x517989060}

[**[mdl ]{lang="EN-US"}**[{ **data** { **eic** *string* \| **fic** *string* \| **gen-no** *string* \| **lic** *string* \| **pfi** *string* \| **port-no** *string* \| **unit** *string* } \| **detect** \| **generate** { **idle-signal** \| **path** \| **test-signal** } }]{lang="EN-US"}]{#struct_0_21171_18224_x545651908}

[**[undo mdl ]{lang="EN-US"}**[\[ **data** \[ **eic** \| **fic** \| **gen-no** \| **lic** \| **pfi** \| **port-no** \| **unit** \] \| **detect** \| **generate** \[ **idle-signal** \|  **path** \| **test-signal** \] \]]{lang="EN-US"}]{#struct_0_21171_18224_x1423145430}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x627729482}

[[上电后，]{style="font-family:宋体"}]{#struct_0_21171_18224_x1638982923}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[定时检测功能处于关闭状态，不发送任何消息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x435278441}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x1661434171}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778806846}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1397616548}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1693761123}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1471862542}

[**[data]{lang="EN-US"}**]{#struct_0_21171_18224_x297277080}[：设置]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息参数，其中]{style="font-family:宋体"}[eic]{lang="EN-US"}[、]{style="font-family:宋体"}[lic]{lang="EN-US"}[、]{style="font-family:宋体"}[fic]{lang="EN-US"}[和]{style="font-family:宋体"}[unit]{lang="EN-US"}[为三类]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息的公有参数，]{style="font-family:宋体"}[pfi]{lang="EN-US"}[、]{style="font-family:宋体"}[port-no]{lang="EN-US"}[和]{style="font-family:宋体"}[gen-no]{lang="EN-US"}[分别为消息]{style="font-family:宋体"}[path]{lang="EN-US"}[、]{style="font-family:宋体"}[idle signal]{lang="EN-US"}[和]{style="font-family:宋体"}[test signal]{lang="EN-US"}[的私有参数。这些参数为用户可定义的字符串，长度各有限制。]{style="font-family:宋体"}

[**[eic]{lang="EN-US"}**]{#struct_0_21171_18224_x1110074858}**[ ]{lang="EN-US"}***[string]{lang="EN-US"}*[：]{style="font-family:宋体"}[Equipment ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[fic ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_21171_18224_x891651627}[：]{style="font-family:宋体"}[Frame ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[gen-no ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_21171_18224_1479127498}[：]{style="font-family:宋体"}[Generator number in test signal message]{lang="EN-US"}[，]{style="font-family:宋体"}[test signal]{lang="EN-US"}[消息的私有参数，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[38]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lic ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_21171_18224_1778741310}[：]{style="font-family:宋体"}[Location ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[11]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pfi ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_21171_18224_x106250231}[：]{style="font-family:宋体"}[Facility ID in path message]{lang="EN-US"}[，]{style="font-family:宋体"}[path]{lang="EN-US"}[消息的私有参数，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[38]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[port-no ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_21171_18224_415363261}[：]{style="font-family:宋体"}[Port number in idle signal message]{lang="EN-US"}[，]{style="font-family:宋体"}[idle signal]{lang="EN-US"}[消息的私有参数，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[38]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[unit]{lang="EN-US"}**]{#struct_0_21171_18224_254420895}**[ ]{lang="EN-US"}***[string]{lang="EN-US"}*[：]{style="font-family:宋体"}[Unit]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:
宋体"}[line]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[detect]{lang="EN-US"}**]{#struct_0_21171_18224_92593125}[：]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口上的定时检测]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息功能。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_21171_18224_2001415433}[：按照]{style="font-family:宋体"}[data]{lang="EN-US"}[中配置的参数定时发送]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息，包括]{style="font-family:宋体"}[path]{lang="EN-US"}[、]{style="font-family:宋体"}[idle signal]{lang="EN-US"}[和]{style="font-family:宋体"}[test signal]{lang="EN-US"}[，可以同时发送。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_231562999}

[[MDL]{lang="EN-US"}]{#struct_0_21171_18224_x227596004}[（]{style="font-family:宋体"}[Maintenance Data Link]{lang="EN-US"}[，维护数据链路）是利用]{style="font-family:宋体"}[C-bit]{lang="EN-US"}[帧格式中第五个子帧中的]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[C]{lang="EN-US"}[比特组成的一条数据链路，可用于传输一些维护性的消息。]{style="font-family:
宋体"}[ANSI T1.107a]{lang="EN-US"}[中规定，]{style="font-family:宋体"}[MDL]{lang="EN-US"}[可用于传输三种消息：]{style="font-family:宋体"}[path]{lang="EN-US"}[、]{style="font-family:宋体"}[idle signal]{lang="EN-US"}[和]{style="font-family:宋体"}[test signal]{lang="EN-US"}[，并规定这条链路的数据帧为]{style="font-family:宋体"}[LAPD]{lang="EN-US"}[协议格式。]{style="font-family:宋体"}

[[MDL]{lang="EN-US"}]{#struct_0_21171_18224_1778675774}[链路的收发状态详见]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1445827216}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x457638970}[打开]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1036294052}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] mdl detect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1065270540}[配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[的]{style="font-family:宋体"}[lic]{lang="EN-US"}[参数为字符串"]{style="font-family:宋体"}[hello]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1223774661}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] mdl data lic hello]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1868275431}[设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[发送]{style="font-family:宋体"}[path]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1778610238}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] mdl generate path ]{lang="EN-US"}
:::

::: {#529275234 .myid}
[]{#_Toc404785228}[]{#struct_0_21171_18224_286799043}[]{#_Toc325463708}[]{#_Toc318123790}

**WAN接口 \-- CT3接口配置命令 \-- reset counters controller t3**

------------------------------------------------------------------------

[**[reset counters controller t3]{lang="EN-US"}**]{#struct_0_21171_18224_x51689985}[命令用来清除]{style="font-family:
宋体"}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1436943194}

[**[reset counters controller]{lang="EN-US"}**[ **t3** \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_21171_18224_1775536280}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_158199821}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21171_18224_x1993944719}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778544702}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x111278385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x278366517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1932836289}

[*[interface-number]{lang="EN-US"}*]{#struct_0_21171_18224_255994597}[：]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口编号。不指定本参数，将清除所有]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_320720954}

[[单独清除]{style="font-family:宋体"}[CT3]{lang="EN-US"}]{#struct_0_21171_18224_877802645}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[只能使用]{style="font-family:宋体"}**[reset counters controller t3]{lang="EN-US"}**[命令，不能使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令，该命令会清除所有接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_1060683400}[接口的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[可以用]{style="font-family:宋体"}**[display controller t3]{lang="EN-US"}**[命令来查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x903738828}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1779527742}[清除]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset counters controller t3 2/4/0]{lang="EN-US"}]{#struct_0_21171_18224_x506954906}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1394752462}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller t3]{lang="EN-US"}**]{#struct_0_21171_18224_192007051}
:::

::: {#-410499632 .myid}
[]{#_Toc404785229}[]{#struct_0_21171_18224_1028535263}[]{#_Toc325463710}[]{#_Toc318123791}

**WAN接口 \-- CT3接口配置命令 \-- t1 alarm**

------------------------------------------------------------------------

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_588174694}[ ]{lang="EN-US"}**[alarm]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口下某个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的告警信号检测与发送功能。]{style="font-family:宋体"}

[**[undo t1]{lang="EN-US"}***[ ]{lang="EN-US"}***[alarm]{lang="EN-US"}**]{#struct_0_21171_18224_577523783}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x186356918}

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_1779462206}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[alarm]{lang="EN-US"}**[ { ]{lang="EN-US"}**[detect ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[generate]{lang="EN-US"}**[ {]{lang="EN-US"}**[ ais]{lang="EN-US"}[ ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ rai]{lang="EN-US"}**[ } }]{lang="EN-US"}

[**[undo t1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1310515784}**[ ]{lang="EN-US"}[alarm ]{lang="EN-US"}**[{]{lang="EN-US"}**[ detect ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[generate]{lang="EN-US"}[ ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[ais]{lang="EN-US"}[ ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ rai ]{lang="EN-US"}**[} }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_396099926}

[[告警信号检测功能处于打开状态，发送功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_901847532}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x595951588}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x164056586}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1214962682}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_366418640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1779003451}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x871716442}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x373768640}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[detect]{lang="EN-US"}**]{#struct_0_21171_18224_641228230}[：]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口下某个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的告警信号检测功能。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_21171_18224_x2016412120}[：发送某种告警信号，如]{style="font-family:宋体"}[AIS]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[。可用于线路状态测试。]{style="font-family:宋体"}

[**[ais]{lang="EN-US"}**]{#struct_0_21171_18224_x2074096241}[：]{style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，即告警指示信号。]{style="font-family:宋体"}

[**[rai]{lang="EN-US"}**]{#struct_0_21171_18224_x1383068376}[：]{style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，即远端告警指示信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2006455826}

[[上电后，]{style="font-family:宋体"}]{#struct_0_21171_18224_1778937915}[CT3]{lang="EN-US"}[接口下各]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的告警信号定时检测功能是打开的，并能通过接口显示实时报告接口告警状态，如]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[等。当检测到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[后，会向对方发送]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警信号。]{style="font-family:宋体"}

[[主要的告警信号包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_21171_18224_997030629}[（]{style="font-family:宋体"}[Loss Of Signal]{lang="EN-US"}[，信号丢失）、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[（]{style="font-family:宋体"}[Loss Of Frame]{lang="EN-US"}[，帧同步丢失）、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[（]{style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，告警指示信号）、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，远端告警指示信号）。各信号具体格式遵循]{style="font-family:宋体"}[T1]{lang="EN-US"}[规范]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[。]{style="font-family:宋体"}

[[一次只能发送一种告警信号（包括在使用]{style="font-family:宋体"}]{#struct_0_21171_18224_x988541219}**[detect]{lang="EN-US"}**[功能时检测到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[后而产生的]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警信号），发送另一种告警信号前必须使用]{style="font-family:宋体"}**[undo t1 alarm generate]{lang="EN-US"}**[命令取消前一种告警信号。]{style="font-family:宋体"}**[detect]{lang="EN-US"}**[功能产生的告警信号（]{style="font-family:宋体"}[RAI]{lang="EN-US"}[）必须通过]{style="font-family:宋体"}**[undo t1 alarm detect]{lang="EN-US"}**[命令取消。]{style="font-family:宋体"}

[[告警的收发状态详见]{style="font-family:宋体"}]{#struct_0_21171_18224_1740421479}[CT3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_212383723}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1196995007}[打开]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的告警检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x815286953}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 alarm detect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x114574548}[在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1778872379}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 alarm generate ais]{lang="EN-US"}
:::

::: {#-1916534407 .myid}
[]{#_Toc404785230}[]{#struct_0_21171_18224_x518709957}[]{#_Toc325463711}[]{#_Toc318123792}

**WAN接口 \-- CT3接口配置命令 \-- t1 bert**

------------------------------------------------------------------------

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_x1135279361}[ ]{lang="EN-US"}**[bert]{lang="EN-US"}**[命令用来进行]{style="font-family:
宋体"}[CT3]{lang="EN-US"}[接口下某]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_1238327598}[ ]{lang="EN-US"}**[bert]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x579029146}

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_477620259}[ ]{lang="EN-US"}*[line-number ]{lang="EN-US"}***[bert]{lang="EN-US"}[ ]{lang="EN-US"}[pattern ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[2\^11]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[2\^15]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[2\^20]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[2\^23]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[qrss]{lang="EN-US"}**[ } ]{lang="EN-US"}**[time]{lang="EN-US"}**[ ]{lang="EN-US"}*[number ]{lang="EN-US"}*[\[]{lang="EN-US"}**[ unframed]{lang="EN-US"}[ ]{lang="EN-US"}**[\]]{lang="EN-US"}[ ]{lang="EN-US"}

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_44894594}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[bert]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778806843}

[[不进行线路位错误率的测试。]{style="font-family:宋体"}]{#struct_0_21171_18224_1397944228}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x2090980880}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_1937628543}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x393365075}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x681606244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x385536411}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_597569026}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_1778741307}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pattern]{lang="EN-US"}**]{#struct_0_21171_18224_x105791478}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，包括]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^23]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^11]{lang="EN-US"}**]{#struct_0_21171_18224_x260217313}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[11]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^15]{lang="EN-US"}**]{#struct_0_21171_18224_x1953607458}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[15]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^20]{lang="EN-US"}**]{#struct_0_21171_18224_365098300}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2\^23]{lang="EN-US"}**]{#struct_0_21171_18224_148487606}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[23]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[qrss]{lang="EN-US"}**]{#struct_0_21171_18224_x869965914}[：发送的码流长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[，且码流中不允许连续]{style="font-family:宋体"}[14]{lang="EN-US"}[个以上的]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_21171_18224_1227516081}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试的持续时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[**[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_1778675771}[：设置测试数据流填充帧的开销位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1446023824}

[[ITU O.151]{lang="EN-US"}]{#struct_0_21171_18224_x560083139}[、]{style="font-family:宋体"}[ITU O.153]{lang="EN-US"}[及]{style="font-family:宋体"}[ANSI T1.403-1999]{lang="EN-US"}[定义了各种]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[目前]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道支持]{style="font-family:宋体"}[2\^11]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^15]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^20]{lang="EN-US"}[、]{style="font-family:宋体"}[2\^23]{lang="EN-US"}[和]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[这几种测试模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_23625267}[测试方式如下：本端发出测试数据流，经过线路某处环回回来，检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对端设置为远端环回等。]{style="font-family:宋体"}

[[利用]{style="font-family:宋体"}**[bert]{lang="EN-US"}**]{#struct_0_21171_18224_x388169901}[命令配置好测试模式，指定测试持续时间，开始测试后，可以查看接口状态中的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果。]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果的说明详见]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_712774698}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1434111913}[在]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[上执行]{style="font-family:宋体"}[QRSS]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1778610235}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 bert pattern qrss time 10]{lang="EN-US"}
:::

::: {#-1029661762 .myid}
[]{#_Toc404785231}[]{#struct_0_21171_18224_286471363}[]{#_Toc325463712}[]{#_Toc318123793}

**WAN接口 \-- CT3接口配置命令 \-- t1 channel-set**

------------------------------------------------------------------------

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_x377051906}*[ ]{lang="EN-US"}***[channel-set]{lang="EN-US"}**[命令用来对]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道进行时隙捆绑。]{style="font-family:宋体"}

[**[undo t1 channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_1905560832}[命令用来取消时隙捆绑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x473750714}

[**[t1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1272118621}*[ ]{lang="EN-US"}***[channel-set ]{lang="EN-US"}***[set-number ]{lang="EN-US"}***[timeslot-list]{lang="EN-US"}**[ ]{lang="EN-US"}*[list]{lang="EN-US"}[ ]{lang="EN-US"}*[\[]{lang="EN-US"}**[ speed ]{lang="EN-US"}**[{]{lang="EN-US"}**[ 56k ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[64k]{lang="EN-US"}**[ } \]]{lang="EN-US"}[ ]{lang="EN-US"}

[**[undo t1 ]{lang="EN-US"}***[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_1366416220}[ ]{lang="EN-US"}**[channel-set]{lang="EN-US"}***[ set-number]{lang="EN-US"}*[ ]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1372188948}

[[不捆绑任何]{style="font-family:宋体"}[channel set]{lang="EN-US"}]{#struct_0_21171_18224_1778544699}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1845495510}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x442112640}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1619994513}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1720702568}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1271536814}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1781075961}

[*[line-numbe]{lang="EN-US"}*]{#struct_0_21171_18224_x791013006}*[r]{lang="EN-US"}*[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[set-number]{lang="EN-US"}*]{#struct_0_21171_18224_1779527739}[：指定]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道上时隙捆绑形成的]{style="font-family:宋体"}[channel set]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeslot-list]{lang="EN-US"}***[ list]{lang="EN-US"}*]{#struct_0_21171_18224_x506234005}[：被捆绑的时隙。]{style="font-family:宋体"}*[list]{lang="EN-US"}*[为时隙编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。在指定捆绑的时隙时，可以用]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的形式指定单个时隙，也可以用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[-*number2*]{lang="EN-US"}[的形式指定一个范围内的时隙，还可以使用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[,*number2*-*number3*]{lang="EN-US"}[的形式，同时指定多个时隙。]{style="font-family:宋体"}

[**[speed ]{lang="EN-US"}**]{#struct_0_21171_18224_2085864235}[{]{lang="EN-US"}**[ 56k ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[64k]{lang="EN-US"}**[ }]{lang="EN-US"}[：配置时隙捆绑的方式。选用参数]{style="font-family:宋体"}**[56k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[56kbps]{lang="EN-US"}[；选用参数]{style="font-family:宋体"}**[64k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。如果不指定速率，缺省采用]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1728003160}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_1871024566}[T1]{lang="EN-US"}[通道工作在成帧方式（]{style="font-family:宋体"}[CT1]{lang="EN-US"}[方式）时，可以对其进行时隙捆绑。系统会自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，编号为]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number***/***line-number***:***set-number*]{lang="EN-US"}[。此接口的速率为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[（或]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[56kbps]{lang="EN-US"}[），其逻辑特性与同步串口相同，可以视其为同步串口进行进一步的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_409339769}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1132480467}[在]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[接口的第一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道上捆绑出一个]{style="font-family:宋体"}[128kbps]{lang="EN-US"}[的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1779462203}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 channel-set 1 timeslot-list 1,2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1310188104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[t1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_1316585827}
:::

::: {#-739348293 .myid}
[]{#_Toc404785232}[]{#struct_0_21171_18224_x740138415}[]{#_Toc325463713}[]{#_Toc318123795}

**WAN接口 \-- CT3接口配置命令 \-- t1 clock**

------------------------------------------------------------------------

[**[t1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_2127934881}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口下]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式。]{style="font-family:宋体"}

[**[undo t1 clock]{lang="EN-US"}**]{#struct_0_21171_18224_x248556638}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x202025588}

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_1916876669}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}***[ clock ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[master]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[slave ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo t1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_1779003452}[ ]{lang="EN-US"}**[clock]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x871650906}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_1616052929}[接口下]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_786308080}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x1354089914}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_384431850}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x909189173}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1605629363}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778937916}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_997227237}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[master]{lang="EN-US"}**]{#struct_0_21171_18224_50478088}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式为主时钟模式，使用内部时钟信号。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_21171_18224_1960368229}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式为从时钟模式，使用线路提供的时钟信号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1849053415}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x1309748630}[CT3]{lang="EN-US"}[接口工作在通道化工作方式下，各个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道均能独立设置时钟。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_598185559}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_726969348}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[使用从时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1778872380}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 clock slave]{lang="EN-US"}
:::

::: {#-1134142576 .myid}
[]{#_Toc404785233}[]{#struct_0_21171_18224_x518120132}[]{#_Toc325463714}[]{#_Toc318123798}

**WAN接口 \-- CT3接口配置命令 \-- t1 fdl**

------------------------------------------------------------------------

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_x287190502}[ ]{lang="EN-US"}**[fdl]{lang="EN-US"}**[命令用来设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口下]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[链路格式。]{style="font-family:宋体"}

[**[undo t1 fdl]{lang="EN-US"}**]{#struct_0_21171_18224_330581095}[命令用来取消]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[链路传输。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_843258363}

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_x1510366469}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}***[ fdl ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[ansi]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[att ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[both]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[none ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_x1748062909}[ ]{lang="EN-US"}*[line-number ]{lang="EN-US"}***[fdl]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_499046224}

[[禁止]{style="font-family:宋体"}[FDL]{lang="EN-US"}]{#struct_0_21171_18224_1778806844}[（]{style="font-family:宋体"}**[none]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_1397485476}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x932268553}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1339259196}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_954900057}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1768579428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_961225453}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_210367833}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ansi]{lang="EN-US"}**]{#struct_0_21171_18224_1778741308}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，遵循]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[att]{lang="EN-US"}**]{#struct_0_21171_18224_x105725942}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，遵循]{style="font-family:宋体"}[AT&T TR 54016 ]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_21171_18224_1755265160}[：使能]{style="font-family:宋体"}[FDL]{lang="EN-US"}[，同时遵循]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T TR 54016]{lang="EN-US"}[规范。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_21171_18224_2052972109}[：禁止]{style="font-family:宋体"}[FDL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1623076369}

[[FDL]{lang="EN-US"}]{#struct_0_21171_18224_217467567}[（]{style="font-family:宋体"}[Facility Data Link]{lang="EN-US"}[，设备数据链路）是]{style="font-family:宋体"}[T1]{lang="EN-US"}[的]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧格式中的一条]{style="font-family:宋体"}[4kbps]{lang="EN-US"}[的数据链路，可用于传输]{style="font-family:宋体"}[PPR]{lang="EN-US"}[（]{style="font-family:宋体"}[Periodical Performance Report]{lang="EN-US"}[）数据，也可传输环回控制码，配置远端环回。]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}[规范定义，]{style="font-family:宋体"}[PPR]{lang="EN-US"}[数据格式为]{style="font-family:宋体"}[LAPD]{lang="EN-US"}[协议格式，环回控制码格式为]{style="font-family:宋体"}[BOP]{lang="EN-US"}[（]{style="font-family:宋体"}[Bit Oriented Protocol]{lang="EN-US"}[）协议格式。这里的]{style="font-family:宋体"}**[t1 fdl]{lang="EN-US"}**[命令仅用于启动]{style="font-family:宋体"}[PPR]{lang="EN-US"}[数据传输，对环回码的发送和检测没有影响，即收发环回码无需配置]{style="font-family:宋体"}[fdl]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：只有在]{style="font-family:宋体"}]{#struct_0_21171_18224_206735004}[CT3]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道工作在通道化模式下，且]{style="font-family:宋体"}[T1]{lang="EN-US"}[帧格式为]{style="font-family:宋体"}[ESF]{lang="EN-US"}[时候，该配置才有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_185288356}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1778675772}[设置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[格式为]{style="font-family:宋体"}[ansi]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1446220432}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 fdl ansi]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_168248341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[t1 ]{lang="EN-US"}[frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_x1665662381}
:::

::: {#-1539254743 .myid}
[]{#_Toc404785234}[]{#struct_0_21171_18224_x1797939763}[]{#_Toc325463715}[]{#_Toc318123796}

**WAN接口 \-- CT3接口配置命令 \-- t1 frame-format**

------------------------------------------------------------------------

[**[t1]{lang="EN-US"}***[ ]{lang="EN-US"}***[frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_1101493960}[命令用来配置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的帧格式。]{style="font-family:宋体"}

[**[undo t1 frame-format]{lang="EN-US"}**]{#struct_0_21171_18224_1998171849}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1778610236}

[**[t1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_286405827}[ ]{lang="EN-US"}**[frame-format]{lang="EN-US"}[ ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[esf ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ sf ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_x1103322502}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}***[ frame-format]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_1410957330}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_869890200}[通道的帧格式为]{style="font-family:宋体"}**[esf]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1174959578}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_86422949}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1520460408}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_1778544700}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x111409457}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1804401955}

[*[line-numbe]{lang="EN-US"}*]{#struct_0_21171_18224_1381488187}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[esf]{lang="EN-US"}**]{#struct_0_21171_18224_x271461858}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的帧格式为]{style="font-family:宋体"}[ESF]{lang="IT"}[（]{style="font-family:宋体"}[Extended Super Frame]{lang="IT"}[，]{style="font-family:宋体"}[扩展超帧]{style="font-family:宋体"}[）]{style="font-family:宋体"}[格式。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_21171_18224_585731559}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的帧格式为]{style="font-family:宋体"}[SF]{lang="IT"}[（]{style="font-family:宋体"}[Super Frame]{lang="IT"}[，]{style="font-family:宋体"}[超帧]{style="font-family:宋体"}[）]{style="font-family:宋体"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1580872414}

[[只有当]{style="font-family:宋体"}]{#struct_0_21171_18224_x632060671}[T1]{lang="EN-US"}[通道工作在成帧方式时（使用命令]{style="font-family:宋体"}**[undo t1 unframed]{lang="EN-US"}**[），才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1779527740}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x506823834}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的帧格式为]{style="font-family:宋体"}[超帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x196051635}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 frame-format sf]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1985892185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[t1 unframed]{lang="EN-US"}**]{#struct_0_21171_18224_x720801762}
:::

::: {#295096647 .myid}
[]{#_Toc404785235}[]{#struct_0_21171_18224_x1840089484}[]{#_Toc325463716}[]{#_Toc318123797}

**WAN接口 \-- CT3接口配置命令 \-- t1 loopback**

------------------------------------------------------------------------

[**[t1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1777202673}[命令用来开启]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口下]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的环回检测功能并设置检测方式。]{style="font-family:宋体"}

[**[undo t1 loopback]{lang="EN-US"}**]{#struct_0_21171_18224_1779462204}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1310384712}

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_x377513941}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}***[ loopback ]{lang="EN-US"}**[{]{lang="EN-US"}**[ local]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[payload]{lang="EN-US"}[ ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ remote]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[undo t1 ]{lang="EN-US"}***[line-number]{lang="EN-US"}***[ loopback]{lang="EN-US"}**]{#struct_0_21171_18224_x1235454209}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_760730986}

[[环回检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21171_18224_930030459}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1296493430}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x1991210814}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x949879900}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x658363579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1138256785}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_1808417841}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1811054285}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_21171_18224_x1299852924}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_21171_18224_x1340544486}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道对外净荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_21171_18224_x1681282086}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道对外环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x995396720}

[[如果]{style="font-family:宋体"}]{#struct_0_21171_18224_x949945436}[T1]{lang="EN-US"}[通道的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[，在设置自环或远端环回后，其链路层协议状态将上报为]{style="font-family:宋体"}[down]{lang="EN-US"}[，这属于正常情况。]{style="font-family:宋体"}

[[环回功能通常用于进行某些特殊测试，正常工作时不要启动环回。]{style="font-family:宋体"}]{#struct_0_21171_18224_992654305}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x147542221}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1286264841}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[进行对内自环]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_282536194}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 loopback local]{lang="EN-US"}
:::

::: {#-1846802740 .myid}
[]{#_Toc404785236}[]{#struct_0_21171_18224_x161703085}[]{#_Toc325463717}[]{#_Toc318123794}

**WAN接口 \-- CT3接口配置命令 \-- t1 sendloopcode**

------------------------------------------------------------------------

[**[t1 sendloopcode]{lang="EN-US"}**]{#struct_0_21171_18224_x1221165248}[命令用来设置对端]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的某个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的环回模式。]{style="font-family:宋体"}

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_x950010972}**[ ]{lang="EN-US"}[sendloopcode]{lang="EN-US"}**[命令用来取消对应的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1290989986}

[**[t1]{lang="EN-US"}**[ *line-number* **sendloopcode** { **fdl-ansi-line-up** \| **fdl-ansi-payload-up** \| **fdl-att-payload-up** \| **inband-line-up** }]{lang="EN-US"}]{#struct_0_21171_18224_877280795}

[**[undo t1 ]{lang="EN-US"}***[line-number]{lang="EN-US"}*[ **sendloopcode** { **fdl-ansi-line-up** \| **fdl-ansi-payload-up** \| **fdl-att-payload-up** \| **inband-line-up** }]{lang="EN-US"}]{#struct_0_21171_18224_1107007137}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1909620292}

[[不设置]{style="font-family:宋体"}**[sendloopcode]{lang="EN-US"}**]{#struct_0_21171_18224_x489816199}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1564594517}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_1198678598}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x950076508}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1435617789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x837698975}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_2129364910}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1991355313}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[fdl-ansi-line-up]{lang="EN-US"}**]{#struct_0_21171_18224_167507902}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的线路环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[fdl-ansi-payload-up]{lang="EN-US"}**]{#struct_0_21171_18224_2024741781}[：发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范的净荷环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[fdl-att-payload-up]{lang="EN-US"}**]{#struct_0_21171_18224_853973971}**[：]{style="font-family:宋体"}**[发送]{style="font-family:宋体"}[FDL]{lang="EN-US"}[承载的符合]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的净荷环回激活码，启动远端环回。]{style="font-family:宋体"}

[**[inband-line-up]{lang="EN-US"}**]{#struct_0_21171_18224_x950142044}[：发送符合]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[规范和]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[规范的带内线路环回激活码，启动远端环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x690091828}

[[环回测试是一种有效的问题诊断方法。除了在远端设备上通过命令行配置环回外，还可发送环回控制码，设置远端设备的环回。]{style="font-family:宋体"}[ANSI T1.403]{lang="EN-US"}]{#struct_0_21171_18224_x1391480665}[规范定义了]{style="font-family:宋体"}[T1]{lang="EN-US"}[接口下的环回控制码类型和格式。按照环回类型，可分为]{style="font-family:宋体"}[line]{lang="EN-US"}[环回（数据流不经过成帧器）和]{style="font-family:宋体"}[payload]{lang="EN-US"}[环回（数据流经过成帧器）两种；按照传输环回控制码的载体，可分为利用]{style="font-family:宋体"}[inband]{lang="EN-US"}[信号（即]{style="font-family:宋体"}[T1]{lang="EN-US"}[的]{style="font-family:宋体"}[192]{lang="EN-US"}[位有效数据带宽或]{style="font-family:宋体"}[193]{lang="EN-US"}[位全部带宽）和利用]{style="font-family:宋体"}[ESF]{lang="EN-US"}[帧格式中的]{style="font-family:宋体"}[FDL]{lang="EN-US"}[链路两种。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_1973941850}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_1279180618}[在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[发送]{style="font-family:宋体"}[inband]{lang="EN-US"}[信号，配置对端]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[为]{style="font-family:宋体"}[line]{lang="EN-US"}[环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1555117289}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 sendloopcode inband-line-up]{lang="EN-US"}
:::

::: {#1934265555 .myid}
[]{#_Toc404785237}[]{#struct_0_21171_18224_x527698772}[]{#_Toc325463718}[]{#_Toc318123799}

**WAN接口 \-- CT3接口配置命令 \-- t1 show**

------------------------------------------------------------------------

[**[t1 show]{lang="EN-US"}**]{#struct_0_21171_18224_1408411252}[命令用来快捷显示]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口下某个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道线路状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x950207580}

[**[t1 ]{lang="EN-US"}***[line-number ]{lang="EN-US"}***[show]{lang="EN-US"}**]{#struct_0_21171_18224_131187106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1539862648}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_49691119}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1976059898}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_656842084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_1044264286}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_999387556}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x950273116}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[show]{lang="EN-US"}**]{#struct_0_21171_18224_x1074097131}[：显示]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道物理线路状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1316549339}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x379408470}[显示]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的线路状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x950338652}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 show]{lang="EN-US"}

[T3 2/4/0  CT1 1: up]{lang="EN-US"}

[  Frame-format: ESF, clock: slave, loopback: not set]{lang="EN-US"}

[  FDL Performance Report: disabled]{lang="EN-US"}

[  Transmitter is sending RAI]{lang="EN-US"}

[  Receiver alarm state is LOF]{lang="EN-US"}

[  Line loop back activate code using inband signal last sent]{lang="EN-US"}

[  BERT state:(stopped, not completed)]{lang="EN-US"}

[    Test pattern: 2\^11, Status: Not Sync, Sync Detected: 0]{lang="EN-US"}

[    Time: 0 minutes, Time past: 0 minutes ]{lang="EN-US"}

[    Bit errors (since test started): 0 bits]{lang="EN-US"}

[    Bits received (since test started): 0 Kbits]{lang="EN-US"}

[    Bit errors (since latest sync): 0 bits]{lang="EN-US"}

[    Bits received (since latest sync): 0 Kbits]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[t1 show]{lang="EN-US"}]{#struct_0_21171_18224_x305031419}[命令显示信息解释]{style="font-family:黑体"}

[]{#table_struct_0_1692467726}[[字段]{style="font-family:黑体"}]{#struct_0_21171_18224_x390044392}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21171_18224_x1339033692}

[[T3 2/4/0  CT1 1: up]{lang="EN-US"}]{#struct_0_21171_18224_x699740620}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x949355612}[接口下]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[up/down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Frame-format]{lang="EN-US"}]{#struct_0_21171_18224_1377547037}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_1914469226}[通道的帧格式，包括]{style="font-family:宋体"}[ESF]{lang="EN-US"}[和]{style="font-family:宋体"}[SF]{lang="EN-US"}

[[clock]{lang="EN-US"}]{#struct_0_21171_18224_x1179175712}

[[时钟模式，包括]{style="font-family:宋体"}[slave]{lang="EN-US"}]{#struct_0_21171_18224_x783600614}[和]{style="font-family:宋体"}[master]{lang="EN-US"}

[[loopback]{lang="EN-US"}]{#struct_0_21171_18224_x949421148}

[[环回设置]{style="font-family:宋体"}]{#struct_0_21171_18224_1756071405}

[[FDL Performance Report: disabled]{lang="EN-US"}]{#struct_0_21171_18224_x1622560651}

[[禁止用]{style="font-family:宋体"}[FDL]{lang="EN-US"}]{#struct_0_21171_18224_x1630978188}[链路传输性能报告信息（]{style="font-family:宋体"}[PPR]{lang="EN-US"}[），可用]{style="font-family:宋体"}**[t1 ]{lang="EN-US"}[fdl ansi]{lang="DE"}**[命令使能]{style="font-family:宋体"}

[[Transmitter is sending RAI]{lang="EN-US"}]{#struct_0_21171_18224_x371115547}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_x949879899}[通道发送器在发送]{style="font-family:宋体"}[RAI]{lang="EN-US"}[。当收到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[时，发]{style="font-family:宋体"}[RAI]{lang="EN-US"}

[[Receiver alarm state is LOF]{lang="EN-US"}]{#struct_0_21171_18224_1679698764}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_x1425960986}[通道接收到的告警，包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[和]{style="font-family:宋体"}[RAI]{lang="EN-US"}

[[Line loop back activate code using inband signal last sent]{lang="EN-US"}]{#struct_0_21171_18224_398882109}

[[上次发送的环回码：]{style="font-family:宋体"}[Line loop back activate code using inband signal]{lang="EN-US"}]{#struct_0_21171_18224_x949945435}

[[BERT state]{lang="EN-US"}]{#struct_0_21171_18224_992850913}

[[BERT]{lang="EN-US"}]{#struct_0_21171_18224_1991273175}[测试状态。包括]{style="font-family:宋体"}[running]{lang="EN-US"}[、]{style="font-family:宋体"}[complete]{lang="EN-US"}[和]{style="font-family:宋体"}[stopped(not completed)]{lang="EN-US"}

[[Test pattern]{lang="EN-US"}]{#struct_0_21171_18224_x1848444129}

[[测试模式]{style="font-family:宋体"}]{#struct_0_21171_18224_x2129208697}

[[Status]{lang="EN-US"}]{#struct_0_21171_18224_x950010971}

[[同步状态]{style="font-family:宋体"}]{#struct_0_21171_18224_1290793378}

[[Sync Detected]{lang="EN-US"}]{#struct_0_21171_18224_1215822466}

[[检测到的同步次数]{style="font-family:宋体"}]{#struct_0_21171_18224_1541675757}

[[Time]{lang="EN-US"}]{#struct_0_21171_18224_x950076507}

[[总测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_x1435552253}

[[Time past]{lang="EN-US"}]{#struct_0_21171_18224_x688433646}

[[已经过去的测试时间]{style="font-family:宋体"}]{#struct_0_21171_18224_x891236270}

[[Bit errors (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_x950142043}

[[测试以来收到的错误比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_x689895220}

[[Bits received (since test started)]{lang="EN-US"}]{#struct_0_21171_18224_595627126}

[[测试以来收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_x950207579}

[[Bit errors (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_131776931}

[[上次同步以来收到的错误比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_1195848962}

[[Bits received (since latest sync)]{lang="EN-US"}]{#struct_0_21171_18224_189510355}

[[上次同步以来收到的总比特数]{style="font-family:宋体"}]{#struct_0_21171_18224_x950273115}

[ ]{lang="EN-US"}

::: {#-539068290 .myid}
[]{#_Toc404785238}[]{#struct_0_21171_18224_x1074031595}[]{#_Toc325463719}[]{#_Toc318123800}

**WAN接口 \-- CT3接口配置命令 \-- t1 shutdown**

------------------------------------------------------------------------

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_1260710639}[ ]{lang="EN-US"}**[shutdown]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的某个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_1610306414}**[ ]{lang="EN-US"}[shutdown]{lang="EN-US"}**[命令用来打开]{style="font-family:
宋体"}[T1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_728166012}

[**[t1]{lang="EN-US"}**]{#struct_0_21171_18224_303914184}**[ ]{lang="EN-US"}***[line-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[shutdown]{lang="EN-US"}**

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_x950338651}**[ ]{lang="EN-US"}***[line-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[shutdown]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x304965883}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_x1127991082}[通道处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1480593628}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_2092383012}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x328602185}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x572069160}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1049434075}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x949355611}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_1377350429}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_383399212}

[[该命令对于]{style="font-family:宋体"}]{#struct_0_21171_18224_870184106}[T1]{lang="EN-US"}[通道及其捆绑出的串口均有效。对指定]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道执]{style="font-family:宋体"}**[t1 shutdown]{lang="EN-US"}**[操作后，该]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道捆绑形成的串口将]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[，停止收发数据。如果执行]{style="font-family:宋体"}**[undo t1 shutdown]{lang="EN-US"}**[操作，则所有该]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道捆绑形成的串口将被重新启用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1977306341}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x285727236}[关闭]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1125866783}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 shutdown]{lang="EN-US"}
:::

::: {#-982206442 .myid}
[]{#_Toc404785239}[]{#struct_0_21171_18224_x949421147}[]{#_Toc325463720}[]{#_Toc318123801}

**WAN接口 \-- CT3接口配置命令 \-- t1 unframed**

------------------------------------------------------------------------

[**[t1]{lang="EN-US"}***[ ]{lang="EN-US"}***[unframed]{lang="EN-US"}**]{#struct_0_21171_18224_1755481581}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道工作在非成帧方式（]{style="font-family:宋体"}[T1]{lang="EN-US"}[方式）。]{style="font-family:宋体"}

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_884912121}[ ]{lang="EN-US"}**[unframed]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道工作在成帧方式（]{style="font-family:宋体"}[CT1]{lang="EN-US"}[方式）。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_385864216}

[**[t1]{lang="EN-US"}***[ line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1033882719}[ ]{lang="EN-US"}**[unframed]{lang="EN-US"}**

[**[undo t1]{lang="EN-US"}**]{#struct_0_21171_18224_299353246}[ ]{lang="EN-US"}*[line-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[unframed]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_x37592293}

[[T1]{lang="EN-US"}]{#struct_0_21171_18224_x1834095591}[通道工作在成帧方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_x949879902}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_x658494651}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_1972248609}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x280588175}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x463626250}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1819353813}

[*[line-number]{lang="EN-US"}*]{#struct_0_21171_18224_x1164306732}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[28]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_1201025688}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x949945438}[T1]{lang="EN-US"}[配置成非成帧方式后，它将不包含帧控制信息，也不分时隙，不能进行时隙捆绑。此时，系统会自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，编号为]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number***/***line-umber***:0**]{lang="EN-US"}[。此接口的速率为]{style="font-family:宋体"}[1544kbps]{lang="EN-US"}[，其逻辑特性与同步串口相同，可以视其为同步串口进行进一步的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_992523233}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x10732835}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口下第一个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道工作在非成帧方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_x1531472418}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] t1 1 unframed]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1245816882}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[t1 channel-set]{lang="EN-US"}**]{#struct_0_21171_18224_x1322203869}
:::

::: {#993886281 .myid}
[]{#_Toc404785240}[]{#struct_0_21171_18224_1195279613}[]{#_Toc325463721}[]{#_Toc318123802}

**WAN接口 \-- CT3接口配置命令 \-- using**

------------------------------------------------------------------------

[**[using]{lang="EN-US"}**]{#struct_0_21171_18224_x1821425797}[命令用来配置]{style="font-family:宋体"}[CT3]{lang="EN-US"}[接口的工作模式。]{style="font-family:宋体"}

[**[undo using]{lang="EN-US"}**]{#struct_0_21171_18224_x950010974}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21171_18224_1291121058}

[**[using]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_21171_18224_1228923896}[{]{lang="EN-US"}[ **ct3** ]{lang="EN-US"}[\|]{lang="EN-US"}[ **t3** ]{lang="EN-US"}[}]{lang="EN-US"}

[**[undo using]{lang="EN-US"}**]{#struct_0_21171_18224_1561432211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21171_18224_439368830}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_914333592}[接口工作在]{style="font-family:宋体"}[CT3]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21171_18224_561185842}

[[CT3]{lang="EN-US"}]{#struct_0_21171_18224_713529234}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21171_18224_x950076510}

[[network-admin]{lang="EN-US"}]{#struct_0_21171_18224_x1435093502}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21171_18224_x2091995678}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21171_18224_664233925}

[**[ct3]{lang="EN-US"}**]{#struct_0_21171_18224_x2094711003}[：设置接口工作在通道化模式（]{style="font-family:宋体"}[CT3]{lang="EN-US"}[模式）。]{style="font-family:宋体"}

[**[t3]{lang="EN-US"}**]{#struct_0_21171_18224_x1101899597}[：设置接口工作在非通道化模式（]{style="font-family:宋体"}[T3]{lang="EN-US"}[模式）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21171_18224_x1409374348}

[[只有当]{style="font-family:宋体"}]{#struct_0_21171_18224_x1683857388}[CT3]{lang="EN-US"}[接口工作在通道化模式时，才能够对]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道进行配置。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}]{#struct_0_21171_18224_x950142046}[CT3]{lang="EN-US"}[接口工作在非通道化模式时，系统会自动创建一个]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口，编号为]{style="font-family:宋体"}**[serial]{lang="EN-US"}**[ *number***/0:0**]{lang="EN-US"}[。此接口的速率为]{style="font-family:宋体"}[44.736Mbps]{lang="EN-US"}[，其逻辑特性与同步串口相同，可以视其为同步串口进行进一步的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21171_18224_x690222900}

[[\# ]{lang="EN-US"}]{#struct_0_21171_18224_x1759626164}[配置接口]{style="font-family:宋体"}[T3 2/4/0]{lang="EN-US"}[工作在非通道化模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21171_18224_1724417499}

[\[Sysname\] controller t3 2/4/0]{lang="EN-US"}

[\[Sysname-T3 2/4/0\] using t3]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
