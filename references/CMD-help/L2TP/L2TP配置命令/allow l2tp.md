::: {#1179903853 .myid}
[]{#_Toc404785001}[]{#struct_0_x5615_53139_266699108}[]{#_Toc303863680}

**L2TP \-- L2TP配置命令 \-- allow l2tp**

------------------------------------------------------------------------

[**[allow l2tp]{lang="EN-US"}**]{#struct_0_x5615_53139_1693301396}[命令用来配置]{style="font-family:宋体"}[LNS]{lang="EN-US"}[接受来自指定]{style="font-family:宋体"}[LAC]{lang="EN-US"}[的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求，并指定[]{#_Toc60322392}[]{#_Toc99783685}建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道时使用的虚拟模板]{style="font-family:宋体"}[接口。]{style="font-family:宋体"}

[**[undo allow]{lang="EN-US"}**]{#struct_0_x5615_53139_x1513692117}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x726804866}

[]{#struct_0_x5615_53139_x2138667257}[**[allow l2tp virtual-template ]{lang="EN-US"}***[virtual-template-number]{lang="EN-US"}*[ \[ **remote** *remote-name*]{lang="EN-US"}]{#_Hlt25484868}*[ ]{lang="EN-US"}*[\]]{lang="EN-US"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x5615_53139_1617815527}[]{#_Hlt20218653}**[allow]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1591320081}

[[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_359868604}[不接受任何]{style="font-family:宋体"}[LAC]{lang="EN-US"}[的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1066285478}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_918330134}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1439430092}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1634548641}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x154831348}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x255492498}

[**[virtual-template]{lang="EN-US"}***[ virtual-template-number]{lang="EN-US"}*]{#struct_0_x5615_53139_953747802}[：指定虚拟模板接口。其中，]{style="font-family:宋体"}*[virtual-template-number]{lang="EN-US"}*[为虚拟模板接口序号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[LNS]{lang="EN-US"}[根据虚拟模板接口下配置的参数，动态地创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Access]{lang="EN-US"}[，虚拟访问）接口。不同的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口用来处理不同]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话上的数据。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}***[ remote-name]{lang="EN-US"}*]{#struct_0_x5615_53139_x2138208505}[：指定发起]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求的对端（即]{style="font-family:宋体"}[LAC]{lang="EN-US"}[）。其中，]{style="font-family:宋体"}*[remote-name]{lang="EN-US"}*[表示隧道对端的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1595099612}

[[本命令需要在]{style="font-family:宋体"}[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_x2117451974}[设备上执行，用来指定]{style="font-family:宋体"}[LNS]{lang="EN-US"}[可以接受来自哪些]{style="font-family:宋体"}[LAC]{lang="EN-US"}[的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_451590263}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[下，可以不指定隧道对端名称。即在]{style="font-family:
宋体"}[L2TP]{lang="EN-US"}[组]{style="font-family:
宋体"}[1]{lang="EN-US"}[下，本命令的格式为：]{style="font-family:宋体"}**[allow l2tp virtual-template]{lang="EN-US"}**[ *virtual-template-number* \[ **remote** *remote-name* \]]{lang="EN-US"}[。如果指定了隧道对端名称，则]{style="font-family:宋体"}[LNS]{lang="EN-US"}[只接受来自指定隧道对端的建立请求。如果不指定隧道对端名称，则]{style="font-family:宋体"}[LNS]{lang="EN-US"}[可以接受任何名称的隧道对端的建立请求，此时]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[称为缺省]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[在其他]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1563887013}[组（非]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[）下，必须指定隧道对端的名称。即在其他]{style="font-family:
宋体"}[L2TP]{lang="EN-US"}[组下，本命令的格式为：]{style="font-family:宋体"}**[allow l2tp virtual-template ]{lang="EN-US"}***[virtual-template-number]{lang="EN-US"}*[ **remote** *remote-name*]{lang="EN-US"}*[。]{style="font-family:
宋体"}*

[[如果发起建立请求的隧道对端与某个]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1062765313}[组下配置的对端名称匹配，则]{style="font-family:宋体"}[LNS]{lang="EN-US"}[与该对端建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道时采用该]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下配置的隧道参数（如隧道验证功能、流控功能等）。如果隧道对端不与任何]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下配置的对端名称匹配，则存在缺省]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组时，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[与该对端建立的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道采用缺省]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下配置的隧道参数，不存在缺省]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组时，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[无法与该对端建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[如下情况下，建议用户在]{style="font-family:宋体"}[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_x1952015757}[上配置缺省]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[某些]{style="font-family:宋体"}]{#struct_0_x5615_53139_1820206086}[LAC]{lang="EN-US"}[（如采用]{style="font-family:宋体"}[Windows 2000 beta 2]{lang="EN-US"}[版本的主机）发送的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求中本端名称为空。为了接受这种不知名的对端发起的隧道建立请求，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[上需要配置缺省]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_x1494988060}[与多个]{style="font-family:宋体"}[LAC]{lang="EN-US"}[建立的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道参数相同时，可以通过缺省]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组简化配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x678775305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能在]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2138274041}[LNS]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下执行本命令。]{style="font-family:宋体"}[LAC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时要确保指定的隧道对端名称和]{style="font-family:宋体"}]{#struct_0_x5615_53139_x434806318}[LAC]{lang="EN-US"}[侧配置的隧道本端名称一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在同一个]{style="font-family:宋体"}]{#struct_0_x5615_53139_1520302560}[L2TP]{lang="EN-US"}[组下重复执行本命令，则新的配置覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1413750074}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1531184331}[配置]{style="font-family:宋体"}[LNS]{lang="EN-US"}[接受名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的对端（]{style="font-family:宋体"}[LAC]{lang="EN-US"}[）发起的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求，并指定建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道时使用的虚拟模板接口为]{style="font-family:宋体"}[Virtual-Template2]{lang="EN-US"}[。对于其他名称的对端，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[接受]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求，]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立时使用的虚拟模板接口为]{style="font-family:宋体"}[Virtual-Template1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_754467472}

[\[Sysname\] l2tp-group 1 mode lns]{lang="EN-US"}

[\[Sysname-l2tp1\] allow l2tp virtual-template 1]{lang="EN-US"}

[\[Sysname-l2tp1\] quit]{lang="EN-US"}

[\[Sysname\] l2tp-group 2 mode lns]{lang="EN-US"}

[\[Sysname-l2tp2\] allow l2tp virtual-template 2 remote aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x666741057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel name]{lang="EN-US"}**]{#struct_0_x5615_53139_1720555012}
:::

::: {#1742433432 .myid}
[]{#_Toc404785002}[]{#struct_0_x5615_53139_x2138732792}[]{#_Toc345061223}

**L2TP \-- L2TP配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x5615_53139_x1807102648}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x5615_53139_x2105771900}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1959406125}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x5615_53139_x176860208}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x5615_53139_882574083}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x547599005}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x5615_53139_x1249760607}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_60768225}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_283446691}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2138798328}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1608228488}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x2124990893}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_290814574}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x5615_53139_x1207673333}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x715892839}

[[接口的期望带宽会影响链路的开销值。具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x5615_53139_x1241716243}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1412512080}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x424010924}[设置虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[100kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_229834870}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] bandwidth 100]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404785003}[]{#struct_0_x5615_53139_x2138863864}

**L2TP \-- L2TP配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x5615_53139_x1750562276}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_857283137}

[**[default]{lang="EN-US"}**]{#struct_0_x5615_53139_x324805887}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1770347501}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x1287082893}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1730776955}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x532862082}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1424608340}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1734858866}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2138929400}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x5615_53139_1584371640}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_871951411}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x2007371563}[将虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_1577401141}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785004}[]{#struct_0_x5615_53139_231129059}[]{#_Toc335656812}

**L2TP \-- L2TP配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x5615_53139_x1935935381}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x5615_53139_1428976234}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1254405758}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x5615_53139_1450409233}

[**[undo description]{lang="EN-US"}**]{#struct_0_x5615_53139_x2138470648}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1122600125}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x5615_53139_345983162}["，比如：]{style="font-family:宋体"}[Virtual-PPP254 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1022712182}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_1133765493}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1319226796}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1028517524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x583549280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_269292693}

[*[text]{lang="EN-US"}*]{#struct_0_x5615_53139_830616599}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2138536184}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1142393068}[配置虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[virtual-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_490852188}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] description virtual-interface]{lang="EN-US"}
:::

::: {#-1101078304 .myid}
[]{#_Toc404785005}[]{#struct_0_x5615_53139_1112376221}[]{#_Toc335656813}[]{#_Toc323804934}

**L2TP \-- L2TP配置命令 \-- display interface virtual-ppp**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[virtual-ppp]{lang="EN-US"}**]{#struct_0_x5615_53139_x1944064384}[命令用来显示虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1354271527}

[**[display interface ]{lang="EN-US"}**[\[]{lang="EN-US"}]{#struct_0_x5615_53139_x146995377}**[ virtual-ppp]{lang="EN-US"}**[ \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1710574627}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2138601720}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_245802927}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1452652332}

[[network-operator]{lang="EN-US"}]{#struct_0_x5615_53139_x965978738}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1335788336}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5615_53139_x1573295266}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x203494071}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x5615_53139_x1625046061}[：显示指定虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x5615_53139_x1045203481}[：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x5615_53139_x310383138}[：显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x5615_53139_280895234}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2138667256}

[[执行本命令时，如果不指定]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1111067828}**[virtual-ppp]{lang="EN-US"}**[参数，则显示设备支持的所有接口的相关信息；如果指定]{style="font-family:宋体"}**[virtual-ppp]{lang="EN-US"}**[参数，不指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，则显示所有已创建的虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x434499135}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_673256145}[显示虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-ppp 10]{lang="EN-US"}]{#struct_0_x5615_53139_x2138208504}

[Virtual-PPP10]{lang="EN-US"}

[Current state: Administratively DOWN]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Virtual-PPP10 Interface]{lang="EN-US"}

[Bandwidth: 100000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Internet Address is 10.0.0.1/24 Primary]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Physical: L2TP, baudrate: 100000000 bps]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 154 packets, 1880 bytes, 0 drops]{lang="EN-US"}

[Output: 155 packets, 1875 bytes, 0 drops]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface virtual-ppp]{lang="EN-US"}]{#struct_0_x5615_53139_x1133783743}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_527205475}[[字段]{style="font-family:黑体"}]{#struct_0_x5615_53139_876835345}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1810904181}

[[Current state]{lang="EN-US"}]{#struct_0_x5615_53139_169715643}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x5615_53139_582697412}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_x5615_53139_476401511}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x5615_53139_1597998542}[：表示该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x5615_53139_x2138274040}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x5615_53139_x2000890259}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x673981433}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x5615_53139_x1452634551}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x5615_53139_1212930589}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_x5615_53139_x1835596794}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x5615_53139_x1836651498}

[[接口描述信息]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2138732795}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x5615_53139_x1047587761}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x5615_53139_132606450}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x5615_53139_401957236}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x5615_53139_x189135083}

[[Hold timer]{lang="EN-US"}]{#struct_0_x5615_53139_446729062}

[[当前接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x5615_53139_x2138798331}[报文的周期，单位为秒]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_x5615_53139_1011509315}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x5615_53139_x1709479861}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet Address]{lang="EN-US"}]{#struct_0_x5615_53139_314151349}

[[虚拟]{style="font-family:宋体"}]{#struct_0_x5615_53139_260228887}[PPP]{lang="NO-BOK"}[接口的]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址。如果没有为]{style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[PPP]{lang="NO-BOK"}[接口配置]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址，则该字段显示为]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}[，表示不能处理]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[报文]{style="font-family:宋体"}

[[Primary]{lang="EN-US"}]{#struct_0_x5615_53139_x1899447301}[表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_x5615_53139_1357985168}

[[链路层封装的协议，取值为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x2138863867}

[[LCP]{lang="EN-US"}]{#struct_0_x5615_53139_2141120493}

[[LCP]{lang="EN-US"}]{#struct_0_x5615_53139_x1296025861}[（]{style="font-family:宋体"}[Link Control Protocol]{lang="EN-US"}[，链路控制协议）状态]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x5615_53139_x49723154}

[[接口的物理类型，取值为]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x1222922012}

[[baudrate]{lang="EN-US"}]{#struct_0_x5615_53139_x1709479870}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_x5615_53139_629172298}

[[Last clearing of counters: Never]{lang="EN-US"}]{#struct_0_x5615_53139_x271997485}

[[最后一次清除接口统计信息的时间（]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x5615_53139_x2138929403}[表示未清除过接口的统计信息）]{style="font-family:宋体"}

[[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x5615_53139_1181087113}

[[当前接口最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x5615_53139_x176302782}[秒内输入报文的平均速率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_x5615_53139_858450780}[表示平均每秒输入的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_x5615_53139_x2138470651}[表示平均每秒输入的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_x5615_53139_87187920}[表示平均每秒输入的包数]{lang="EN-US" style="font-family:宋体"}

[[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_x5615_53139_575802616}

[[当前接口最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x5615_53139_x199927704}[秒内输出报文的平均速率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_x5615_53139_1005361957}[表示平均每秒输]{lang="EN-US" style="font-family:宋体"}[出]{style="font-family:宋体"}[的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_x5615_53139_x2138536187}[表示平均每秒输]{lang="EN-US" style="font-family:宋体"}[出]{style="font-family:宋体"}[的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_x5615_53139_1545677595}[表示平均每秒输]{lang="EN-US" style="font-family:宋体"}[出]{style="font-family:宋体"}[的包数]{lang="EN-US" style="font-family:宋体"}

[[Input: 154 packets, 1880 bytes, 0 drops]{lang="EN-US"}]{#struct_0_x5615_53139_1682504853}

[[总计输入的报文数，总计输入的字节，总计丢弃的输入报文数]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1650308811}

[[Output: 155 packets, 1875 bytes, 0 drops]{lang="EN-US"}]{#struct_0_x5615_53139_266515199}

[[总计输出的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_x5615_53139_x2138601723}[总计输出的字节，总计丢弃的输出报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1811886868}[显示虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-ppp 10 brief]{lang="EN-US"}]{#struct_0_x5615_53139_1688202585}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[VPPP10               ADM  DOWN     10.0.0.1        Virtual-PPP10 Interface]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x902132107}[显示所有当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-ppp brief down]{lang="EN-US"}]{#struct_0_x5615_53139_1190266793}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause ]{lang="EN-US"}

[VPPP9                ADM  Administratively]{lang="EN-US"}

[VPPP10               ADM  Administratively]{lang="EN-US"}

[VPPP12               ADM  Administratively]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x2138667259}[显示虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的概要信息，包括用户配置的全部描述信息。]{style="font-family:宋体"}

[[\<Sysname\> display inter Virtual-PPP 10 brief description]{lang="EN-US"}]{#struct_0_x5615_53139_2068154221}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[VPPP10               ADM  DOWN     10.0.0.1        Virtual-PPP10 Interface]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display interface virtual-ppp brief]{lang="EN-US"}]{#struct_0_x5615_53139_1941641556}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_522264393}[[字段]{style="font-family:黑体"}]{#struct_0_x5615_53139_x421808086}

[[描述]{style="font-family:黑体"}]{#struct_0_x5615_53139_26584764}

[[The brief information of interface(s) under route mode/Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_x5615_53139_1222203733}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_x5615_53139_850366960}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x5615_53139_x2138208507}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x5615_53139_432300198}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x5615_53139_x1270770816}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display ]{lang="EN-US"}[interface-backup]{lang="EN-US"}[ state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x5615_53139_1955824667}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x5615_53139_624775587}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x5615_53139_x2037463178}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2138274043}

[[Link]{lang="EN-US"}]{#struct_0_x5615_53139_x1597605732}

[[接口物理连接状态，取值为：]{style="font-family:宋体"}]{#struct_0_x5615_53139_1148705670}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x5615_53139_x662182485}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x5615_53139_2049956817}[：表示接口物理上不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x5615_53139_x1178662418}[[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}]{.TableTextChar}**[undo shutdown]{lang="EN-US"}**[[命令才能打开接口]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x5615_53139_x1398175897}[：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x5615_53139_x1877842066}

[[接口数据链路层协议状态，取值为：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2138732794}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x5615_53139_1681295594}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x5615_53139_3260083}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x5615_53139_1505796510}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会取该值]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x5615_53139_x153875267}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5615_53139_x2138798330}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x5615_53139_x1251932592}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x5615_53139_x1105234215}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x5615_53139_x1184885843}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x5615_53139_x476220813}[的原因，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_x5615_53139_x2138863866}[：]{style="font-family:宋体"}[表示本链路被手工关闭了（配置了]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_x5615_53139_x587762862}[：]{style="font-family:宋体"}[表示没有物理连接，一般是因为]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[协商失败，或者配置不充分未能触发]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[协商]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1936016661 .myid}
[]{#_Toc404785006}[]{#struct_0_x5615_53139_x814457896}

**L2TP \-- L2TP配置命令 \-- display l2tp session**

------------------------------------------------------------------------

[**[display l2tp session]{lang="EN-US"}**]{#struct_0_x5615_53139_x1307818177}[命令用来显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1096000656}

[**[display l2tp session]{lang="EN-US"}**[ \[ **statistics** \]]{lang="EN-US"}]{#struct_0_x5615_53139_968251568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2070422539}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1705501758}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2138929402}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1547796242}

[[network-operator]{lang="EN-US"}]{#struct_0_x5615_53139_60979506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x944551918}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5615_53139_x1050704437}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1637993279}

[**[statistics]{lang="EN-US"}**]{#struct_0_x5615_53139_x330790765}[：显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1293410996}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_351885360}[显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp session statistics]{lang="EN-US"}]{#struct_0_x5615_53139_x2138470650}

[Total number of sessions: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1478896021}[显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp session]{lang="EN-US"}]{#struct_0_x5615_53139_x51341386}

[LocalSID      RemoteSID      LocalTID      State]{lang="EN-US"}

[89            36245          10878         Established]{lang="EN-US"}[]{#_Toc42598111}[]{#_Toc137627620}[]{#_Toc85622795}[]{#_Toc81453338}[]{#_Toc74711151}[]{#_Toc72631497}[]{#_Toc66003570}[]{#_Toc60131642}

[[表1-3 ]{lang="EN-US"}[display l2tp session]{lang="EN-US"}]{#struct_0_x5615_53139_183661777}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_281022478}[[字段]{style="font-family:黑体"}]{#struct_0_x5615_53139_1374271233}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5615_53139_1276362923}

[[Total number of sessions]{lang="EN-US"}]{#struct_0_x5615_53139_x1755242910}

[[会话的数目]{style="font-family:宋体"}]{#struct_0_x5615_53139_x3595807}

[[LocalSID]{lang="EN-US"}]{#struct_0_x5615_53139_x755362867}

[[本端的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x5615_53139_x2138536186}

[[RemoteSID]{lang="EN-US"}]{#struct_0_x5615_53139_x20406346}

[[对端的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x5615_53139_x2124317727}

[[LocalTID]{lang="EN-US"}]{#struct_0_x5615_53139_x750426073}

[[本端的隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x5615_53139_358037229}

[[State]{lang="EN-US"}]{#struct_0_x5615_53139_x23952033}

[[会话的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x5615_53139_563733107}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x5615_53139_x2138601722}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-tunnel]{lang="EN-US"}]{#struct_0_x5615_53139_x916996487}[：等待建立]{lang="EN-US" style="font-family:宋体"}[隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-reply]{lang="EN-US"}]{#struct_0_x5615_53139_x500319168}[：等待]{lang="EN-US" style="font-family:宋体"}[ICRP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-]{lang="EN-US"}]{#struct_0_x5615_53139_82250381}[c]{lang="EN-US"}[onnect]{lang="EN-US"}[：等待]{lang="EN-US" style="font-family:宋体"}[ICCN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Established]{lang="EN-US"}]{#struct_0_x5615_53139_x1897215548}[：]{lang="EN-US" style="font-family:宋体"}[会话成功建立]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1641042205 .myid}
[]{#_Toc404785007}[]{#struct_0_x5615_53139_x1285269058}

**L2TP \-- L2TP配置命令 \-- display l2tp tunnel**

------------------------------------------------------------------------

[**[display l2tp tunnel]{lang="DE"}**]{#struct_0_x5615_53139_x2138667258}[命令用来显示]{style="font-family:宋体"}[L2TP]{lang="DE"}[隧道的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x660729134}

[**[display l2tp tunnel]{lang="EN-US"}**[ \[ **statistics** \]]{lang="EN-US"}]{#struct_0_x5615_53139_x1400245978}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x507756546}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1391207746}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1972138238}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_497979407}

[[network-operator]{lang="EN-US"}]{#struct_0_x5615_53139_431551190}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x581665878}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5615_53139_1540131893}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2138208506}

[**[statistics]{lang="EN-US"}**]{#struct_0_x5615_53139_1998384139}[：显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1090988863}

[]{#_Toc42598112}[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1409659568}[显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp tunnel statistics]{lang="EN-US"}]{#struct_0_x5615_53139_1342389525}

[Total number of tunnels: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x847684242}[显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp tunnel]{lang="EN-US"}]{#struct_0_x5615_53139_x1718075608}

[LocalTID RemoteTID State         Sessions RemoteAddress    RemotePort RemoteName]{lang="EN-US"}

[10878    21        Established   1        20.1.1.2         1701       lns]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display l2tp tunnel]{lang="EN-US"}]{#struct_0_x5615_53139_x633064463}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_284535471}[[字段]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2138274042}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5615_53139_1131277623}

[[Total number of tunnels]{lang="EN-US"}]{#struct_0_x5615_53139_1060485002}

[[隧道的数目]{style="font-family:宋体"}]{#struct_0_x5615_53139_x650339761}

[[LocalTID]{lang="EN-US"}]{#struct_0_x5615_53139_x1413012866}

[[本端的隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x5615_53139_1871696791}

[[RemoteTID]{lang="EN-US"}]{#struct_0_x5615_53139_1982132334}

[[对端的隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x5615_53139_x167932388}

[[State]{lang="EN-US"}]{#struct_0_x5615_53139_x216418490}

[[隧道的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1756989572}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[Idle]{lang="EN-US"}]{#struct_0_x5615_53139_23458190}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[Wait-reply]{lang="EN-US"}]{#struct_0_x5615_53139_x1413591773}[：等待]{lang="EN-US" style="font-family:宋体"}[SCCRP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[Wait-]{lang="EN-US"}]{#struct_0_x5615_53139_107094589}[c]{lang="EN-US"}[onnect]{lang="EN-US"}[：等待]{lang="EN-US" style="font-family:宋体"}[SCCCN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[Established]{lang="EN-US"}]{#struct_0_x5615_53139_x2032889414}[：隧道]{lang="EN-US" style="font-family:宋体"}[成功建立]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stopping]{lang="EN-US"}]{#struct_0_x5615_53139_x216484026}[：正在下线]{lang="EN-US" style="font-family:宋体"}

[[Sessions]{lang="EN-US"}]{#struct_0_x5615_53139_x567171829}

[[此隧道上的会话数目]{style="font-family:宋体"}]{#struct_0_x5615_53139_x331049635}

[[RemoteAddress]{lang="EN-US"}]{#struct_0_x5615_53139_x1838870035}

[[对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5615_53139_x1323122025}[地址]{style="font-family:宋体"}

[[RemotePort]{lang="EN-US"}]{#struct_0_x5615_53139_x576713600}

[[对端]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x216549562}[使用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[RemoteName]{lang="EN-US"}]{#struct_0_x5615_53139_2141258429}

[[隧道对端的名称]{style="font-family:宋体"}]{#struct_0_x5615_53139_x958866455}

[]{#_Toc16585284}[]{#_Hlt25567314}[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1918842726}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset l2tp tunnel]{lang="EN-US"}**]{#struct_0_x5615_53139_x1827464471}

::: {#2023868928 .myid}
[]{#_Toc404785008}[]{#struct_0_x5615_53139_1722839281}[]{#_Toc390949862}[]{#_Toc366514053}

**L2TP \-- L2TP配置命令 \-- display l2tp va-pool**

------------------------------------------------------------------------

[**[display l2tp va-pool]{lang="EN-US"}**]{#struct_0_x5615_53139_x2036249518}[命令用来显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_323688940}

[**[display l2tp va-pool]{lang="EN-US"}**]{#struct_0_x5615_53139_x491635858}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1872790587}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2022624098}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1103114963}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1252133319}

[[network-operator]{lang="EN-US"}]{#struct_0_x5615_53139_1418086013}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1281495462}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5615_53139_1722773745}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_337482059}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1104532716}[显示]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp va-pool]{lang="PT-BR"}]{#struct_0_x5615_53139_93953848}

[VT interface          Size      Unused      State]{lang="PT-BR"}

[Virtual-Template1     1000      900         Normal]{lang="PT-BR"}

[[表1-5 ]{lang="EN-US"}[display l2tp va-pool]{lang="EN-US"}]{#struct_0_x5615_53139_719920199}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1540087868}[[字段]{style="font-family:黑体"}]{#struct_0_x5615_53139_1747044945}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5615_53139_990998893}

[[VT interface]{lang="PT-BR"}]{#struct_0_x5615_53139_1493034930}

[[使用]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x5615_53139_1722708209}[池的虚拟模板接口]{style="font-family:宋体"}

[[Size]{lang="PT-BR"}]{#struct_0_x5615_53139_x458827690}

[[用户申请的]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x5615_53139_x1763851561}[池容量]{style="font-family:宋体"}

[[Unused]{lang="PT-BR"}]{#struct_0_x5615_53139_273311611}

[[VA]{lang="EN-US"}]{#struct_0_x5615_53139_1678188291}[池中可用的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口数量]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x5615_53139_122523654}

[[VA]{lang="EN-US"}]{#struct_0_x5615_53139_1722642673}[池当前的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Creating]{lang="EN-US"}]{#struct_0_x5615_53139_x425976626}[：]{style="font-family:
  宋体"}[表示正在创建]{lang="EN-US" style="font-family:宋体"}[VA]{lang="EN-US"}[池]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Destroying]{lang="EN-US"}]{#struct_0_x5615_53139_192944261}[：]{style="font-family:
  宋体"}[表示正在删除]{lang="EN-US" style="font-family:宋体"}[VA]{lang="EN-US"}[池]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x5615_53139_x1876681583}[：表示]{style="font-family:宋体"}[VA]{lang="EN-US"}[池已经创建完成]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1723101425}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[l2tp virtual-template va-pool]{lang="EN-US"}**]{#struct_0_x5615_53139_x1215584163}

::: {#-1268060838 .myid}
[]{#_Toc404785009}[]{#struct_0_x5615_53139_45922485}

**L2TP \-- L2TP配置命令 \-- interface virtual-ppp**

------------------------------------------------------------------------

[**[interface virtual-ppp]{lang="EN-US"}**]{#struct_0_x5615_53139_86090615}[命令用来创建虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口，并进入指定的虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口视图。如果指定的虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口已经创建，则该命令用来直接进入虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[**[undo interface virtual-ppp]{lang="EN-US"}**]{#struct_0_x5615_53139_850495889}[命令用来删除指定的虚拟]{style="font-family:
宋体"}[PPP]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216615098}

[**[interface virtual-ppp]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x5615_53139_1013264567}

[**[undo interface virtual-ppp]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x5615_53139_x1746217003}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1010275462}

[[设备上不存在任何虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x424582342}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1777276301}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_1052145651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x688923152}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1699032914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_671364968}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216156346}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x5615_53139_996850508}[：虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1057339472}

[[配置]{style="font-family:宋体"}[LAC-Auto-Initiated]{lang="EN-US"}]{#struct_0_x5615_53139_x1362602640}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道时，需要在]{style="font-family:宋体"}[LAC]{lang="EN-US"}[端创建虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2124207657}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x607166419}[创建虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[，并进入虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_1024186899}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\]]{lang="EN-US"}
:::

::: {#-843408420 .myid}
[]{#_Toc404785010}[]{#struct_0_x5615_53139_1293765252}

**L2TP \-- L2TP配置命令 \-- l2tp enable**

------------------------------------------------------------------------

[**[l2tp enable]{lang="EN-US"}**]{#struct_0_x5615_53139_x863259102}[命令用来开启]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo l2tp enable]{lang="EN-US"}**]{#struct_0_x5615_53139_x216221882}[命令用来关闭]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1460034904}

[**[l2tp enable]{lang="EN-US"}**]{#struct_0_x5615_53139_1450387000}

[**[undo l2tp enable]{lang="EN-US"}**]{#struct_0_x5615_53139_x2037517065}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1292669024}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x692794811}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x363595598}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1529714635}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1605714319}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_713750003}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x216287418}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_600917653}

[[只有开启该功能后其他]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x314511561}[相关配置才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1309564389}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1660614075}[开启]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_502736368}

[\[Sysname\] l2tp enable]{lang="EN-US"}
:::

::: {#-1213666689 .myid}
[]{#_Toc404785011}[]{#struct_0_x5615_53139_1866994890}

**L2TP \-- L2TP配置命令 \-- l2tp tsa-id**

------------------------------------------------------------------------

[**[l2tp tsa-id]{lang="EN-US"}**]{#struct_0_x5615_53139_1867191498}[命令用来配置]{style="font-family:宋体"}[LTS]{lang="EN-US"}[设备的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[，并开启]{style="font-family:宋体"}[LTS]{lang="EN-US"}[设备的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[环路检测功能。]{style="font-family:宋体"}

[**[undo l2tp tsa-id]{lang="EN-US"}**]{#struct_0_x5615_53139_x1617246143}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1946520820}

[**[l2tp tsa-id ]{lang="EN-US"}***[tsa-id]{lang="EN-US"}*]{#struct_0_x5615_53139_x1546108111}

[**[undo l2tp tsa-id]{lang="EN-US"}**]{#struct_0_x5615_53139_x1761265290}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x543739544}

[[未指定]{style="font-family:宋体"}[LTS]{lang="EN-US"}]{#struct_0_x5615_53139_955263719}[设备的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[，且]{style="font-family:宋体"}[LTS]{lang="EN-US"}[设备的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[环路检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1867125962}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_636394166}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1871402101}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_253560303}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x268731017}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1697606141}

[*[tsa-id]{lang="EN-US"}*]{#struct_0_x5615_53139_x1626843586}[：]{style="font-family:宋体"}[LTS]{lang="EN-US"}[设备的唯一标识，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1803890500}

[[在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1463382678}[隧道交换组网中，]{style="font-family:宋体"}[LTS]{lang="EN-US"}[通过]{style="font-family:宋体"}[ICRQ]{lang="EN-US"}[（]{style="font-family:宋体"}[Incoming Call Request]{lang="EN-US"}[，入呼叫请求）报文中的]{style="font-family:宋体"}[TSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Tunnel Switching Aggregator]{lang="EN-US"}[，隧道交换聚合）]{style="font-family:宋体"}[ ID AVP]{lang="EN-US"}[来避免环路。]{style="font-family:宋体"}

[[LTS]{lang="EN-US"}]{#struct_0_x5615_53139_894909732}[接收到]{style="font-family:宋体"}[ICRQ]{lang="EN-US"}[报文后，将报文中携带的所有]{style="font-family:宋体"}[TSA ID AVP]{lang="EN-US"}[中的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[逐一与本地配置的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[进行比较。如果]{style="font-family:宋体"}[TSA ID AVP]{lang="EN-US"}[中存在与本地相同的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[，则表示存在环路，]{style="font-family:宋体"}[LTS]{lang="EN-US"}[立即拆除会话。否则，]{style="font-family:宋体"}[LTS]{lang="EN-US"}[将自己的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[封装到新的]{style="font-family:宋体"}[TSA ID AVP]{lang="EN-US"}[中，]{style="font-family:宋体"}[LTS]{lang="EN-US"}[向它的下一跳]{style="font-family:宋体"}[LTS]{lang="EN-US"}[发送]{style="font-family:宋体"}[ICRQ]{lang="EN-US"}[报文时携带接收到的所有]{style="font-family:宋体"}[TSA ID AVP]{lang="EN-US"}[及本地封装的]{style="font-family:宋体"}[TSA ID AVP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[为不同]{style="font-family:宋体"}[LTS]{lang="EN-US"}]{#struct_0_x5615_53139_x1336535466}[设备配置的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[不能相同，否则会导致环路检测错误。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_807837831}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1395873256}[配置]{style="font-family:宋体"}[LTS]{lang="EN-US"}[设备的]{style="font-family:宋体"}[TSA ID]{lang="EN-US"}[为]{style="font-family:宋体"}[lts0]{lang="EN-US"}[，并开启]{style="font-family:宋体"}[LTS]{lang="EN-US"}[设备的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[环路检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_37673820}

[\[Sysname\] l2tp tsa-id lts0]{lang="EN-US"}
:::

::: {#1244361336 .myid}
[]{#_Toc404785012}[]{#struct_0_x5615_53139_1722446062}[]{#_Toc390949878}[]{#_Toc366514068}

**L2TP \-- L2TP配置命令 \-- l2tp virtual-template va-pool**

------------------------------------------------------------------------

[**[l2tp virtual-template va-pool]{lang="EN-US"}**]{#struct_0_x5615_53139_1925663267}[命令用来配置]{style="font-family:
宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[**[undo l2tp ]{lang="EN-US"}[virtual-template va-pool]{lang="EN-US"}**]{#struct_0_x5615_53139_752652649}[命令用来删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x916639593}

[**[l2tp virtual-template]{lang="EN-US"}**[ *template-number* **va-pool** *va-volume*]{lang="EN-US"}]{#struct_0_x5615_53139_x1710619869}

[**[undo ]{lang="EN-US"}[l2tp virtual-template]{lang="EN-US"}**[ *template-number* **va-pool**]{lang="EN-US"}]{#struct_0_x5615_53139_x1270884426}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1026021014}

[[设备上不存在任何]{style="font-family:宋体"}[VA]{lang="EN-US"}]{#struct_0_x5615_53139_x1594578822}[池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1059599793}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_1822106704}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_729238155}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x2032547280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1722380526}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_393163776}

[**[virtual-template ]{lang="EN-US"}***[template-number]{lang="EN-US"}*]{#struct_0_x5615_53139_x766529776}[：指定需要使用]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的虚拟模板接口。该接口必须已经存在。]{style="font-family:宋体"}

[**[va-pool ]{lang="EN-US"}***[va-volume]{lang="EN-US"}*]{#struct_0_x5615_53139_332067052}[：指定需要创建的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_392702882}

[[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_x1356672972}[设备在用户上线创建会话时需要创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，用于和]{style="font-family:宋体"}[LAC]{lang="EN-US"}[交换数据。在用户下线后需要删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口。由于创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口需要一定的时间，所以如果有大量用户上线]{style="font-family:宋体"}[/]{lang="EN-US"}[下线，]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[连接的建立和拆除性能会受到影响。]{style="font-family:宋体"}

[[VA]{lang="EN-US"}]{#struct_0_x5615_53139_x157855647}[池可以用来解决上述问题。]{style="font-family:宋体"}[VA]{lang="EN-US"}[池是在建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[连接前事先创建的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口的集合。创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[池后，当需要创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口时，直接从]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中获取一个]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，加快了]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[连接的建立速度。当用户下线后，直接把]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口放入]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中，不需要删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，加快了]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[连接的拆除速度。当]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口耗光后，仍需在建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[连接时再创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，在用户下线后删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x350311422}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个虚拟模板接口只能关联一个]{style="font-family:宋体"}]{#struct_0_x5615_53139_636255631}[VA]{lang="EN-US"}[池。如果想要修改使用的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的大小，只能先删除原来的配置，然后重新配置]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_x5615_53139_440594723}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[VA]{lang="EN-US"}[池需要花费一定的时间，请用户耐心等待。在]{style="font-family:宋体"}[VA]{lang="EN-US"}[池创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除过程中（还没创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除完成）允许用户上线]{style="font-family:宋体"}[/]{lang="EN-US"}[下线，但正在创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统可能由于资源不足不能创建用户指定容量的]{style="font-family:宋体"}]{#struct_0_x5615_53139_473197424}[VA]{lang="EN-US"}[池，用户可以通过]{style="font-family:宋体"}**[display l2tp va-pool]{lang="EN-US"}**[命令查看实际可用的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的容量以及]{style="font-family:宋体"}[VA]{lang="EN-US"}[池的状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VA]{lang="EN-US"}]{#struct_0_x5615_53139_x1339347874}[池会占用较多的系统内存，请用户根据实际情况创建大小合适的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_x5615_53139_1722839278}[VA]{lang="EN-US"}[池时，如果已有在线用户使用该]{style="font-family:宋体"}[VA]{lang="EN-US"}[池中的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口，不会导致这些用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2035659695}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x154979292}[为虚拟模板]{style="font-family:宋体"}[2]{lang="EN-US"}[创建容量为]{style="font-family:宋体"}[1000]{lang="EN-US"}[的]{style="font-family:宋体"}[VA]{lang="EN-US"}[池。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_2048795444}

[\[Sysname\] l2tp virtual-template 2 va-pool 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x89663127}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2tp va-pool]{lang="EN-US"}**]{#struct_0_x5615_53139_x2029014579}
:::

::: {#-1412536338 .myid}
[]{#_Toc404785013}[]{#struct_0_x5615_53139_x806846264}

**L2TP \-- L2TP配置命令 \-- l2tp-auto-client**

------------------------------------------------------------------------

[**[l2tp-auto-client]{lang="EN-US"}**]{#struct_0_x5615_53139_x2003313894}[命令用来触发]{style="font-family:宋体"}[LAC]{lang="EN-US"}[自动建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[**[undo l2tp-auto-client]{lang="EN-US"}**]{#struct_0_x5615_53139_204864137}[命令用来拆除]{style="font-family:宋体"}[LAC]{lang="EN-US"}[自动建立的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216352954}

[**[l2tp-auto-client ]{lang="EN-US"}[l2tp-group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_x5615_53139_1054664971}

[**[undo l2tp-auto-client]{lang="EN-US"}**]{#struct_0_x5615_53139_x799911332}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_168473071}

[[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_545486607}[不会自动建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1251694336}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_828985952}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x983801404}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1749894647}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_14952247}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1060051806}

[**[l2tp-group]{lang="EN-US"}***[ group-number]{lang="EN-US"}*]{#struct_0_x5615_53139_x215894202}[：指定]{style="font-family:宋体"}[LAC]{lang="EN-US"}[采用特定]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下配置的隧道参数建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_328836493}

[[配置本命令时指定的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_863650042}[组必须已经创建，并且]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组的模式必须是]{style="font-family:宋体"}[LAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[触发]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_1612852832}[建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道后，该隧道将始终存在，直到通过]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **l2tp-auto-client**]{lang="EN-US"}[或]{style="font-family:宋体"}**[undo l2tp-group]{lang="EN-US"}***[ group-number]{lang="EN-US"}*[命令拆除该隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2087576855}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1628298122}[触发]{style="font-family:宋体"}[LAC]{lang="EN-US"}[自动建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道，建立隧道时采用]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{style="font-family:宋体"}[10]{lang="EN-US"}[下配置的隧道参数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x533159087}

[\[Sysname\] interface virtual-ppp 1]{lang="EN-US"}

[\[Sysname-Virtual-PPP1\] l2tp-auto-client l2tp-group 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1337322940}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[l2tp-group]{lang="EN-US"}**]{#struct_0_x5615_53139_x693778938}
:::

::: {#870583763 .myid}
[]{#_Toc404785014}[]{#struct_0_x5615_53139_x215959738}

**L2TP \-- L2TP配置命令 \-- l2tp-group**

------------------------------------------------------------------------

[**[l2tp-group]{lang="EN-US"}**]{#struct_0_x5615_53139_x1639120066}[命令用来创建]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组，指定]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组的模式，并进入]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组视图。]{style="font-family:宋体"}

[**[undo l2tp-group]{lang="EN-US"}**]{#struct_0_x5615_53139_631763418}[命令用来删除]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1970649310}

[**[l2tp-group]{lang="EN-US"}**[ *group-number* \[ **mode** { **lac** \| **lns** } \]]{lang="EN-US"}]{#struct_0_x5615_53139_x938140847}

[**[undo l2tp-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_x5615_53139_x609230324}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x742002499}

[[设备上不存在任何]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_887760684}[组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1574696460}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1240529802}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216418489}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1757448323}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x243951944}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1351121334}

[*[group-number]{lang="SV"}*]{#struct_0_x5615_53139_174132317}[：]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**]{#struct_0_x5615_53139_x1744122018}[：指定]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组的模式。]{style="font-family:宋体"}

[**[lac]{lang="EN-US"}**]{#struct_0_x5615_53139_1931099758}[：]{style="font-family:宋体"}[LAC]{lang="EN-US"}[模式，表示设备可以作为]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[LAC]{lang="EN-US"}[端向]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发起隧道建立请求。]{style="font-family:宋体"}

[**[lns]{lang="EN-US"}**]{#struct_0_x5615_53139_766002523}[：]{style="font-family:宋体"}[LNS]{lang="EN-US"}[模式，表示设备可以作为]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[LNS]{lang="EN-US"}[端接受来自]{style="font-family:宋体"}[LAC]{lang="EN-US"}[的隧道建立请求。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1442283189}

[[通过本命令创建]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x430447215}[组时，必须携带]{style="font-family:宋体"}**[mode]{lang="EN-US"}**[关键字，指定]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组的模式。通过本命令进入已经创建的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组视图时，不需要携带]{style="font-family:宋体"}**[mode]{lang="EN-US"}**[关键字。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x216484025}[组视图下，可以配置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的参数，如隧道验证功能、流控功能等。]{style="font-family:宋体"}

[[一台设备上可以同时存在]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x567368437}[模式和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组，且最多能够创建]{style="font-family:宋体"}[1000]{lang="EN-US"}[个]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1408336857}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x414708851}[创建]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{style="font-family:宋体"}[2]{lang="EN-US"}[，指定]{style="font-family:
宋体"}[L2TP]{lang="EN-US"}[组模式为]{style="font-family:宋体"}[LAC]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x164595819}

[\[Sysname\] l2tp-group 2 mode lac]{lang="EN-US"}

[\[Sysname-l2tp2\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1859688403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[allow l2tp]{lang="EN-US"}**]{#struct_0_x5615_53139_780918212}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lns-ip]{lang="EN-US"}**]{#struct_0_x5615_53139_x1345576687}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user]{lang="EN-US"}**]{#struct_0_x5615_53139_x1433704763}
:::

::: {#-456898580 .myid}
[]{#_Toc404785015}[]{#struct_0_x5615_53139_x216549561}

**L2TP \-- L2TP配置命令 \-- lns-ip**

------------------------------------------------------------------------

[**[lns-ip]{lang="EN-US"}**]{#struct_0_x5615_53139_2141061821}[命令用来在]{style="font-family:宋体"}[LAC]{lang="EN-US"}[端配置]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **lns-ip**]{lang="EN-US"}]{#struct_0_x5615_53139_659401714}[命令用来在]{style="font-family:宋体"}[LAC]{lang="EN-US"}[端删除]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x174673978}

[**[lns-ip ]{lang="EN-US"}**[{ *ip-address* }&\<1-5\>]{lang="EN-US"}]{#struct_0_x5615_53139_x529631395}

[**[undo lns-ip]{lang="EN-US"}**]{#struct_0_x5615_53139_1632597565}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2019379548}

[[没有在]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x1229309746}[端]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_881062407}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x716574497}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216615097}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1013985463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x2140773935}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1957327371}

[[{ *ip-address* }*&*\<1-5\>]{lang="EN-US"}]{#struct_0_x5615_53139_x1723197946}[：]{style="font-family:
宋体"}[LNS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[&\<1-5\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1117545701}

[[在建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x1673774121}[隧道时，]{style="font-family:宋体"}[LAC]{lang="EN-US"}[将按照]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置的先后顺序依次向每个]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发送建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的请求。]{style="font-family:宋体"}[LAC]{lang="EN-US"}[接收到某个]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的接受应答后，该]{style="font-family:宋体"}[LNS]{lang="EN-US"}[就作为隧道的对端；否则，]{style="font-family:宋体"}[LAC]{lang="EN-US"}[向下一个]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发起隧道建立请求。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x756968046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能在]{style="font-family:宋体"}]{#struct_0_x5615_53139_695769025}[LAC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下执行本命令。]{style="font-family:宋体"}[LNS]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在同一个]{style="font-family:宋体"}]{#struct_0_x5615_53139_x216156345}[L2TP]{lang="EN-US"}[组下重复执行本命令，则新的配置覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_997047116}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x196354674}[在]{style="font-family:宋体"}[LAC]{lang="EN-US"}[端配置]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x1226311625}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] lns-ip 202.1.1.1]{lang="EN-US"}
:::

::: {#-1053061097 .myid}
[]{#_Toc404785016}[]{#struct_0_x5615_53139_x1823792305}

**L2TP \-- L2TP配置命令 \-- mandatory-chap**

------------------------------------------------------------------------

[**[mandatory-chap]{lang="EN-US"}**]{#struct_0_x5615_53139_793665647}[命令用来强制]{style="font-family:宋体"}[LNS]{lang="EN-US"}[重新对用户进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[验证。]{style="font-family:宋体"}

[**[undo mandatory-chap]{lang="EN-US"}**]{#struct_0_x5615_53139_1159401782}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1014476794}

[**[mandatory-chap]{lang="EN-US"}**]{#struct_0_x5615_53139_867626462}

[**[undo mandatory-chap]{lang="EN-US"}**]{#struct_0_x5615_53139_x525852357}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216221881}

[[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_1460100440}[不会重新对用户进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[验证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1852396465}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1022454160}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x557621010}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1438613968}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1264862829}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1370014724}

[[缺省情况下，]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x192865591}[代替]{style="font-family:宋体"}[LNS]{lang="EN-US"}[对用户进行验证，并将用户的所有验证信息及]{style="font-family:宋体"}[LAC]{lang="EN-US"}[端本身配置的验证方式发送给]{style="font-family:宋体"}[LNS]{lang="EN-US"}[。]{style="font-family:宋体"}[LNS]{lang="EN-US"}[根据接收到的信息及]{style="font-family:宋体"}[LNS]{lang="EN-US"}[端配置的验证方式，判断用户是否合法。]{style="font-family:宋体"}

[[为了增加安全性，可以执行]{style="font-family:宋体"}**[mandatory-chap]{lang="EN-US"}**]{#struct_0_x5615_53139_242189441}[命令，强制在]{style="font-family:宋体"}[LAC]{lang="EN-US"}[代理验证成功后，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[再次对用户进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[验证。]{style="font-family:宋体"}

[[执行]{style="font-family:宋体"}**[mandatory-chap]{lang="EN-US"}**]{#struct_0_x5615_53139_x216287417}[命令配置强制]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[验证后，对于]{style="font-family:宋体"}[NAS-Initiated]{lang="EN-US"}[模式]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的用户来说，会经过两次验证：一次是在]{style="font-family:宋体"}[NAS]{lang="EN-US"}[端的验证，另一次是在]{style="font-family:宋体"}[LNS]{lang="EN-US"}[端的验证。一些用户可能不支持进行第二次验证，这时，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[端的]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[重新验证会失败。在这种情况下，建议不要开启]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的强制]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[验证功能。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_600721045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能在]{style="font-family:宋体"}]{#struct_0_x5615_53139_276235816}[LNS]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下执行本命令。]{style="font-family:宋体"}[LAC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对]{style="font-family:宋体"}[NAS-In]{lang="EN-US"}]{#struct_0_x5615_53139_205824461}[i]{lang="EN-US"}[tiated]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道有效，对]{style="font-family:宋体"}[Client-Initiated]{lang="EN-US"}[模式和]{style="font-family:宋体"}[LAC-Auto-Initiated]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mandatory-lcp]{lang="EN-US"}**]{#struct_0_x5615_53139_x1889122845}[命令]{lang="EN-US" style="font-family:宋体"}[的优先级高于本命令，即如果在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下同时执行了]{style="font-family:宋体"}**[mandatory-chap]{lang="EN-US"}**[命令和]{style="font-family:宋体"}**[mandatory-lcp]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[，则]{style="font-family:宋体"}[LNS]{lang="EN-US"}[与用户重新进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1426746243}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1081914803}[强制]{style="font-family:宋体"}[LNS]{lang="EN-US"}[重新对用户进行]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[验证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x887007192}

[\[Sysname\] l2tp-group 1 mode lns]{lang="EN-US"}

[\[Sysname-l2tp1\] mandatory-chap]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1349493198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mandatory-lcp]{lang="EN-US"}**]{#struct_0_x5615_53139_x216352953}
:::

::: {#482311173 .myid}
[]{#_Toc404785017}[]{#struct_0_x5615_53139_1054861579}

**L2TP \-- L2TP配置命令 \-- mandatory-lcp**

------------------------------------------------------------------------

[**[mandatory-lcp]{lang="EN-US"}**]{#struct_0_x5615_53139_1091350387}[命令用来强制]{style="font-family:宋体"}[LNS]{lang="EN-US"}[与用户重新进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[（]{style="font-family:宋体"}[Link Control Protocol]{lang="EN-US"}[，链路控制协议）协商。]{style="font-family:宋体"}

[**[undo mandatory-lcp]{lang="EN-US"}**]{#struct_0_x5615_53139_2130204872}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_706295271}

[**[mandatory-lcp]{lang="EN-US"}**]{#struct_0_x5615_53139_1984832614}

[**[undo mandatory-lcp]{lang="EN-US"}**]{#struct_0_x5615_53139_2056162611}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_968371960}

[[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_1091396859}[不会与用户重新进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x583515645}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x215894201}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_329033101}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_444455728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1994201113}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1121078982}

[[缺省情况下，对于]{style="font-family:宋体"}[NAS-Initialized]{lang="EN-US"}]{#struct_0_x5615_53139_x1731597271}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道，用户先和]{style="font-family:宋体"}[LAC]{lang="EN-US"}[进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商。如果协商通过，则由]{style="font-family:宋体"}[LAC]{lang="EN-US"}[发起]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求，并把与用户协商时收集到的信息（包括验证信息）发送给]{style="font-family:宋体"}[LNS]{lang="EN-US"}[。]{style="font-family:宋体"}[LNS]{lang="EN-US"}[根据接收到的信息判断用户是否合法。]{style="font-family:宋体"}[LNS]{lang="EN-US"}[不会与用户重新进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x888718051}[与用户协商出来的]{style="font-family:宋体"}[LCP]{lang="EN-US"}[参数可能不是]{style="font-family:宋体"}[LNS]{lang="EN-US"}[期望的参数。此时，需要在]{style="font-family:宋体"}[LNS]{lang="EN-US"}[上执行]{style="font-family:宋体"}**[mandatory-lcp]{lang="EN-US"}**[命令，强制]{style="font-family:宋体"}[LNS]{lang="EN-US"}[与用户重新进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商，忽略]{style="font-family:宋体"}[LAC]{lang="EN-US"}[发送的信息。]{style="font-family:宋体"}

[[如果一些]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x739139534}[用户不支持]{style="font-family:宋体"}[LCP]{lang="EN-US"}[重新协商，则]{style="font-family:宋体"}[LCP]{lang="EN-US"}[重新协商过程会失败。在这种情况下，建议不要开启]{style="font-family:宋体"}[LNS]{lang="EN-US"}[的强制]{style="font-family:宋体"}[LCP]{lang="EN-US"}[重协商功能。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_832180813}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能在]{style="font-family:宋体"}]{#struct_0_x5615_53139_1913123656}[LNS]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下执行本命令。]{style="font-family:宋体"}[LAC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对]{style="font-family:宋体"}[NAS-In]{lang="EN-US"}]{#struct_0_x5615_53139_x215959737}[i]{lang="EN-US"}[tiated]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道有效，对]{style="font-family:宋体"}[Client-Initiated]{lang="EN-US"}[模式和]{style="font-family:宋体"}[LAC-Auto-Initiated]{lang="EN-US"}[模式的隧道无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1639972034}[命令]{lang="EN-US" style="font-family:宋体"}[的优先级高于]{style="font-family:宋体"}**[mandatory-chap]{lang="EN-US"}**[命令，即如果在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下同时执行了]{style="font-family:宋体"}**[mandatory-chap]{lang="EN-US"}**[命令和]{style="font-family:宋体"}**[mandatory-lcp]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[，则]{style="font-family:宋体"}[LNS]{lang="EN-US"}[与用户重新进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_794454211}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_881475704}[强制]{style="font-family:宋体"}[LNS]{lang="EN-US"}[与用户重新进行]{style="font-family:宋体"}[LCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_220107586}

[\[Sysname\] l2tp-group 1 mode lns]{lang="EN-US"}

[\[Sysname-l2tp1\] mandatory-lcp]{lang="EN-US"}[]{#_Toc16585282}[]{#_Toc16497322}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x679321994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mandatory-chap]{lang="EN-US"}**]{#struct_0_x5615_53139_x1865380455}
:::

::: {#988247972 .myid}
[]{#_Toc404785018}[]{#struct_0_x5615_53139_445007104}

**L2TP \-- L2TP配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x5615_53139_1477811055}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x5615_53139_x1517174937}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_445465856}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x5615_53139_x383797846}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x5615_53139_753443546}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_520663971}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x1900663522}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1950059193}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_441079109}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2020834275}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_445400320}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_461746749}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x403282633}

[*[size]{lang="EN-US"}*]{#struct_0_x5615_53139_x583399545}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x952888217}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x5615_53139_1503369188}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_x5615_53139_769998199}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1511312235}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_444941575}[配置虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1400]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x1528835701}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] mtu 1400]{lang="EN-US"}
:::

::: {#-82843708 .myid}
[]{#_Toc404785019}[]{#struct_0_x5615_53139_x1306135534}[]{#_Toc335656819}[]{#_Toc323804933}[]{#_Toc345658524}[]{#_Toc345658525}[]{#_Toc345658526}[]{#_Toc345658527}[]{#_Toc345658528}[]{#_Toc345658529}[]{#_Toc345658530}[]{#_Toc345658531}[]{#_Toc345658532}[]{#_Toc345658533}[]{#_Toc345658534}[]{#_Toc345658535}[]{#_Toc345658536}[]{#_Toc345658537}[]{#_Toc345658538}[]{#_Toc345658539}[]{#_Toc345658540}[]{#_Toc345658541}[]{#_Toc345658542}[]{#_Toc345658543}[]{#_Toc345658544}[]{#_Toc345658545}[]{#_Toc345658546}

**L2TP \-- L2TP配置命令 \-- reset counters interface virtual-ppp**

------------------------------------------------------------------------

[**[reset counters interface virtual-ppp]{lang="EN-US"}**]{#struct_0_x5615_53139_107984720}[命令用来清除虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216418492}

[**[reset counters interface]{lang="EN-US"}**[ \[ **virtual-ppp** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x5615_53139_x1757120644}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1769372266}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1693717301}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1923060307}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1468280245}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1248817695}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1759642674}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x5615_53139_x1981221694}[：虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x806206741}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x5615_53139_x216484028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5615_53139_x567040757}**[virtual-ppp]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5615_53139_517808220}**[virtual-ppp]{lang="EN-US"}**[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5615_53139_1863191865}**[virtual-ppp]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1377814602}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1976498581}[清除虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface virtual-ppp 10]{lang="EN-US"}]{#struct_0_x5615_53139_1711841470}
:::

::: {#954707549 .myid}
[]{#_Toc404785020}[]{#struct_0_x5615_53139_1697288072}

**L2TP \-- L2TP配置命令 \-- reset l2tp tunnel**

------------------------------------------------------------------------

[**[reset l2tp tunnel]{lang="EN-US"}**]{#struct_0_x5615_53139_x202787815}[命令用来断开指定的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道，同时断开该隧道内的所有会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1924812631}

[**[reset l2tp tunnel]{lang="EN-US"}**[ { **id** *tunnel-id* \| **name** *remote-name* }]{lang="EN-US"}]{#struct_0_x5615_53139_x216549564}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2140865213}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1303062403}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1089482998}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x2089644609}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x135223957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_451106439}

[**[id ]{lang="EN-US"}**]{#struct_0_x5615_53139_1426375316}*[tunnel-id]{lang="SV"}*[：断开隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[为指定值的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}*[tunnel-id]{lang="SV"}*[为隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="SV"}**]{#struct_0_x5615_53139_x1478175181}[ ]{lang="SV"}*[remote-name]{lang="SV"}*[：断开与指定隧道对端之间的]{style="font-family:
宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:
宋体"}*[remote-name]{lang="SV"}*[表示隧道对端的名称，为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216615100}

[[在用户数为零、网络发生故障等情况下，可以通过本命令强制断开指定的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x942526288}[隧道。]{style="font-family:宋体"}[LAC]{lang="EN-US"}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[任何一端都可主动发起断开]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的请求。隧道断开后，该隧道上的所有]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话也将被清除。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_637097365}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[强制断开一个]{style="font-family:宋体"}]{#struct_0_x5615_53139_1139903687}[L2TP]{lang="EN-US"}[隧道后，当对端用户再次呼入时，隧道可以重新建立。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过指定隧道的对端名称来确定需要断开的]{style="font-family:宋体"}]{#struct_0_x5615_53139_503613591}[L2TP]{lang="EN-US"}[隧道时，如果没有符合条件的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道存在，则对当前的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道没有影响；如果有多个符合条件的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道存在（同一个名称，不同]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址），则断开所有符合条件的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1324006642}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1425061202}[断开对端名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道，并断开该隧道内的所有会话。]{style="font-family:宋体"}

[[\<Sysname\> reset l2tp tunnel ]{lang="EN-US"}]{#struct_0_x5615_53139_x2037472570}[[name aaa]{lang="EN-US"}]{#_Toc16585292}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1574380188}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2tp tunnel]{lang="EN-US"}**]{#struct_0_x5615_53139_1022416900}[]{#_Hlt21862211}
:::

::::: {#-780779607 .myid}
[]{#_Toc404785021}[]{#struct_0_x5615_53139_x216156348}[]{#_Toc335656821}[]{#_Toc303865071}[]{#_Toc215545670}[]{#_Toc215479545}

**L2TP \-- L2TP配置命令 \-- service**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](L2TP命令.files/image001.png){#图片 7 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x5615_53139_997768012}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5615_53139_x533638549}
:::

[ ]{lang="EN-US"}

[**[service]{lang="EN-US"}**]{#struct_0_x5615_53139_x186611792}[命令用来指定虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口下流量的业务处理板。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_x5615_53139_220707278}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_540356139}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5615_53139_229935071}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[service slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5615_53139_x1670165624}

[**[undo service slot]{lang="EN-US"}**]{#struct_0_x5615_53139_x1162937640}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5615_53139_1187129840}[模式：]{style="font-family:宋体"}

[**[service ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5615_53139_x216221884}

[**[undo service ]{lang="EN-US"}[chassis]{lang="EN-US"}**]{#struct_0_x5615_53139_1460428120}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_300199538}

[[没有指定虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x976527024}[接口下流量的业务处理板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1764116837}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_457903951}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x292747633}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1480760038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1727100692}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216287420}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x5615_53139_600393364}[：指定单板所在的槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x5615_53139_x1845521803}[：指定设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x5615_53139_x980897955}[：指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1574984902}

[**[service]{lang="EN-US"}**]{#struct_0_x5615_53139_17844734}[命令仅对]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数据报文的处理产生影响，]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[控制报文始终在主用主控板上处理，不受本命令的控制。]{style="font-family:宋体"}

[[如果通过本命令指定了虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_157872918}[接口下流量的业务处理板，则通过该接口转发的报文均在指定的单板]{style="font-family:宋体"}[/]{lang="EN-US"}[成员设备上进行封装和解封装处理。否则，由系统自动选择处理]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数据报文的单板]{style="font-family:宋体"}[/]{lang="EN-US"}[成员设备。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_72424250}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[tunnel flow-control]{lang="EN-US"}**]{#struct_0_x5615_53139_x845687426}[命令为]{lang="EN-US" style="font-family:
宋体"}[L2TP]{lang="EN-US"}[数据报文开启了流控功能时，需要在虚拟]{lang="EN-US" style="font-family:
宋体"}[PPP]{lang="EN-US"}[接口下配置]{lang="EN-US" style="font-family:宋体"}**[service]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的业务处理板被拔出，则即使接口]{style="font-family:宋体"}]{#struct_0_x5615_53139_727501447}[UP]{lang="EN-US"}[，流量也转发不通。重新插入该业务处理板后，流量可以恢复在指定板上进行封装和解封装处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216352956}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1054533899}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板集中处理虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的流量。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x403454298}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x2124758059}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备集中处理虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的流量。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_420269164}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1907852356}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板集中处理虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的流量。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_1734097327}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\]]{lang="EN-US"}[ ]{lang="EN-US"}[service ]{lang="IT"}[chassis]{lang="EN-US"}[ ]{lang="EN-US"}[2 slot 2]{lang="IT"}
:::::

::: {#1170655049 .myid}
[]{#_Toc404785022}[]{#struct_0_x5615_53139_x1550600373}[]{#_Toc335656822}

**L2TP \-- L2TP配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x5615_53139_x215894204}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x5615_53139_329229709}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1853408395}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x5615_53139_x623457940}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x5615_53139_1795460288}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_61888560}

[[接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_x5615_53139_x131117042}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1447461947}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_2116007913}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_595225920}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x215959740}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1639644357}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x943670584}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1347087976}[关闭虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_1404332970}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] shutdown]{lang="EN-US"}
:::

::: {#1646906047 .myid}
[]{#_Toc404785023}[]{#struct_0_x5615_53139_445007111}[]{#_Toc374353031}

**L2TP \-- L2TP配置命令 \-- source-ip**

------------------------------------------------------------------------

[**[source-ip]{lang="EN-US"}**]{#struct_0_x5615_53139_x478504076}[命令用来设置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端地址，即封装后]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道报文的源地址。]{style="font-family:宋体"}

[**[undo source-ip]{lang="EN-US"}**]{#struct_0_x5615_53139_x942287665}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_445465863}

[**[source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x5615_53139_1190180271}

[**[undo source-ip]{lang="EN-US"}**]{#struct_0_x5615_53139_x1591584623}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1711519378}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1446726841}[隧道的源端地址为本端隧道出接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1319401513}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x1202252777}[组]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x291289388}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_445400327}

[[network-operator]{lang="EN-US"}]{#struct_0_x5615_53139_461746744}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x403282620}

[*[ip-address]{lang="SV"}*]{#struct_0_x5615_53139_x583202936}[：]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1829067536}

[[建议将]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_304856902}[隧道的源端地址配置为设备上某]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，以减小物理接口故障对]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[业务造成的影响。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_444941574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能在]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1528835702}[LAC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下执行本命令。]{style="font-family:宋体"}[LN]{lang="EN-US"}[S]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_988211892}[多机备份的情况下，如果]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[视图]{style="font-family:宋体"}[下同时配置了]{lang="EN-US" style="font-family:宋体"}**[tunnel vsrp source-ip]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[source-ip]{lang="EN-US"}**[命令，将使用]{lang="EN-US" style="font-family:宋体"}**[tunnel vsrp source-ip]{lang="EN-US"}**[命令指定的地址作为]{lang="EN-US" style="font-family:
宋体"}[L2TP]{lang="EN-US"}[隧道的源端地址；如果]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[视图]{style="font-family:宋体"}[下配置了]{lang="EN-US" style="font-family:宋体"}**[source-ip]{lang="EN-US"}**[命令，没有配置]{lang="EN-US" style="font-family:宋体"}**[tunnel vsrp source-ip]{lang="EN-US"}**[命令，将会导致]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[多机备份故障。]{lang="EN-US" style="font-family:宋体"}[关于]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[多机备份的详细介绍请参见"可靠性配置指导"中的"多机备份"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1064570751}

[[\# ]{lang="SV"}]{#struct_0_x5615_53139_444876038}[设置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端地址]{style="font-family:宋体"}[为]{style="font-family:宋体"}[2.2.2.2]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_x5615_53139_1963339568}

[\[Sysname\] l2tp-group 1 ]{lang="SV"}[mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] source-ip 2.2.2.2]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_444810502}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel vsrp source-ip]{lang="EN-US"}**]{#struct_0_x5615_53139_405983395}[（可靠性命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[多机备份）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-2024387197 .myid}
[]{#_Toc404785024}[]{#struct_0_x5615_53139_x655213866}

**L2TP \-- L2TP配置命令 \-- tunnel authentication**

------------------------------------------------------------------------

[**[tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_x43281393}[命令用来开启]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道验证功能。]{style="font-family:宋体"}

[**[undo tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_x299280461}[命令用来关闭]{style="font-family:
宋体"}[L2TP]{lang="EN-US"}[隧道验证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_278406525}

[**[tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_x216418491}

[**[undo tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_x1756924036}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_809737345}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_229774537}[隧道验证功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1621273059}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x864775689}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_775448694}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1721454336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x682008334}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x82141392}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x216484027}[隧道验证功能用来防止本端设备与非法的对端设备建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道，提高网络的安全性。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x567237365}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[两端都开启了隧道验证功能，则两端密钥（通过]{style="font-family:宋体"}**[tunnel password]{lang="EN-US"}**[命令配置）不为空并且完全一致的情况下，二者之间才能成功建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x86584030}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[中的一端开启了隧道验证功能，则另一端可不开启隧道验证功能，但需要两端密钥（通过]{style="font-family:宋体"}**[tunnel password]{lang="EN-US"}**[命令配置）不为空并且完全一致，二者之间才能成功建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x1539235384}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[两端都禁用隧道验证功能，则无论两端是否配置密钥、密钥是否相同，都不影响隧道建立。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x854392479}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了保证隧道安全，建议用户不要禁用隧道验证功能。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5615_53139_849938681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户需要修改隧道验证的密钥，请在隧道开始协商前进行，否则修改的密钥不生效。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5615_53139_x705537076}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1101377320}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1218914971}[开启]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道验证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_649482538}

[\[Sysname\] l2tp-group 1 mode lns]{lang="EN-US"}

[\[Sysname-l2tp1\] tunnel authentication]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_813406713}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel password]{lang="EN-US"}**]{#struct_0_x5615_53139_x758525742}
:::

::: {#-1842633323 .myid}
[]{#_Toc404785025}[]{#struct_0_x5615_53139_1384950630}

**L2TP \-- L2TP配置命令 \-- tunnel avp-hidden**

------------------------------------------------------------------------

[**[tunnel avp-hidden]{lang="EN-US"}**]{#struct_0_x5615_53139_x1718520246}[命令用来配置隧道采用隐藏方式（即密文方式）传输]{style="font-family:宋体"}[AVP]{lang="EN-US"}[数据。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **tunnel avp-hidden**]{lang="EN-US"}]{#struct_0_x5615_53139_x216549563}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2141192893}

[**[tunnel avp-hidden]{lang="EN-US"}**]{#struct_0_x5615_53139_1043353029}

[**[undo tunnel avp-hidden]{lang="EN-US"}**]{#struct_0_x5615_53139_1496633184}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2024015198}

[[隧道采用明文方式传输]{style="font-family:宋体"}[AVP]{lang="EN-US"}]{#struct_0_x5615_53139_x896110043}[数据。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_323102110}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_346068990}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1483610959}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1095403733}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x216615099}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1013330103}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x534772408}[协议通过]{style="font-family:宋体"}[AVP]{lang="EN-US"}[（]{style="font-family:宋体"}[Attribute Value Pair]{lang="EN-US"}[，属性值对）来传输隧道协商参数、会话协商参数和用户认证信息等。如果用户不希望这些信息（如用户密码）被窃取，则可以使用本配置将]{style="font-family:宋体"}[AVP]{lang="EN-US"}[数据的传输方式配置为隐藏传输，即利用隧道验证密钥（通过]{style="font-family:宋体"}**[tunnel password]{lang="EN-US"}**[命令配置）对]{style="font-family:宋体"}[AVP]{lang="EN-US"}[数据进行加密传输。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1844917269}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_1734069819}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下都可以执行本命令。但是，目前]{style="font-family:宋体"}[LNS]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下本命令不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有通过]{lang="EN-US" style="font-family:宋体"}**[tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_746997080}[命令开启隧道验证功能后，]{lang="EN-US" style="font-family:宋体"}[本命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2040216367}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1650686827}[配置]{style="font-family:宋体"}[AVP]{lang="EN-US"}[数据采用隐藏方式传输。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x980915926}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] tunnel avp-hidden]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216156347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_996916044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel password]{lang="EN-US"}**]{#struct_0_x5615_53139_312832441}
:::

::: {#-1023556656 .myid}
[]{#_Toc404785026}[]{#struct_0_x5615_53139_1569740946}

**L2TP \-- L2TP配置命令 \-- tunnel flow-control**

------------------------------------------------------------------------

[**[tunnel flow-control]{lang="EN-US"}**]{#struct_0_x5615_53139_x502770842}[命令用来开启]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的流控功能。]{style="font-family:宋体"}

[**[undo tunnel flow-control]{lang="EN-US"}**]{#struct_0_x5615_53139_1999171976}[命令用来关闭]{style="font-family:
宋体"}[L2TP]{lang="EN-US"}[会话的流控功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x2049907722}

[**[tunnel flow-control]{lang="EN-US"}**]{#struct_0_x5615_53139_921339945}

[**[undo tunnel flow-control]{lang="EN-US"}**]{#struct_0_x5615_53139_41309066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2052529020}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x216221883}[会话的流控功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1459969368}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_2063619113}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x308471983}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1491573243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_273356836}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1490899562}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x397628141}[会话的流控功能是指在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话上传递的报文中携带序列号，通过序列号检测是否存在丢包，并根据序列号对乱序报文进行排序。]{style="font-family:宋体"}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1848410515}[会话的流控功能应用在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数据报文的接收与发送过程中。]{style="font-family:宋体"}

[[只要]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x1928051887}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[中的一端开启了流控功能，二者之间建立的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话就支持流控功能。设备作为]{style="font-family:宋体"}[LAC]{lang="EN-US"}[时，]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话建立后如果]{style="font-family:宋体"}[LNS]{lang="EN-US"}[上改变了流控功能的状态，则]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的流控功能状态随之改变。设备作为]{style="font-family:宋体"}[LNS]{lang="EN-US"}[时，]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话建立后如果]{style="font-family:宋体"}[LAC]{lang="EN-US"}[上改变了流控功能的状态，则]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的流控功能状态不会随之改变。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216287419}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_600852117}[开启]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话的流控功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_1621064244}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] tunnel flow-control]{lang="EN-US"}
:::

::: {#-1004152632 .myid}
[]{#_Toc404785027}[]{#struct_0_x5615_53139_1892966775}

**L2TP \-- L2TP配置命令 \-- tunnel name**

------------------------------------------------------------------------

[**[tunnel name]{lang="EN-US"}**]{#struct_0_x5615_53139_x1406058305}[命令用来配置隧道本端的名称。]{style="font-family:宋体"}

[**[undo tunnel name]{lang="EN-US"}**]{#struct_0_x5615_53139_x1381798596}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x437495719}

[**[tunnel name]{lang="EN-US"}**[ *name*]{lang="EN-US"}]{#struct_0_x5615_53139_1809095563}

[**[undo tunnel name]{lang="EN-US"}**]{#struct_0_x5615_53139_x184521993}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216352955}

[[隧道本端的名称为设备的名称。设备名称的详细介绍，请参见"基础配置指导"中的"设备管理"。]{style="font-family:宋体"}]{#struct_0_x5615_53139_1054730507}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x468376400}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x1845437307}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1224440261}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x826002598}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_442689953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1565275879}

[*[name]{lang="EN-US"}*]{#struct_0_x5615_53139_x1331913961}[：隧道本端的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x36937852}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x215894203}[配置隧道本端的名称为]{style="font-family:宋体"}[itsme]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_328902029}

[\[Sysname\] l2tp-group 1 mode lns]{lang="EN-US"}

[\[Sysname-l2tp1\] tunnel name itsme]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_140013303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sysname]{lang="EN-US"}**]{#struct_0_x5615_53139_729853743}[（基础配置命令参考]{style="font-family:
宋体"}[/]{lang="EN-US"}[设备管理）]{style="font-family:宋体"}
:::

::: {#250721067 .myid}
[]{#_Toc404785028}[]{#struct_0_x5615_53139_x2050968798}

**L2TP \-- L2TP配置命令 \-- tunnel password**

------------------------------------------------------------------------

[**[tunnel password]{lang="EN-US"}**]{#struct_0_x5615_53139_x870154907}[命令用来配置隧道验证密钥。]{style="font-family:宋体"}

[**[undo tunnel password]{lang="EN-US"}**]{#struct_0_x5615_53139_x754920344}[命令用来删除隧道验证密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2043671273}

[**[tunnel password]{lang="EN-US"}**[ { **cipher** \| **simple** } *password*]{lang="EN-US"}]{#struct_0_x5615_53139_x2021807051}

[**[undo tunnel password]{lang="EN-US"}**]{#struct_0_x5615_53139_x215959739}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1639054530}

[[没有配置隧道验证密钥。]{style="font-family:宋体"}]{#struct_0_x5615_53139_x2028632482}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x479877362}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_616843784}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1045076476}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_1464834251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_794633523}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_769838109}

[**[cipher]{lang="EN-US"}**]{#struct_0_x5615_53139_1536608817}[：以密文方式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x5615_53139_x216418494}[：以明文方式设置密钥。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_x5615_53139_x1756727428}[：隧道验证密钥，区分大小写。如果是]{style="font-family:宋体"}**[cipher]{lang="EN-US"}**[方式，则]{style="font-family:宋体"}*[password]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的密文字符串；如果是]{style="font-family:宋体"}**[simple]{lang="EN-US"}**[方式，则]{style="font-family:宋体"}*[password]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[16]{lang="EN-US"}[个字符的明文字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x474172593}

[[只有通过]{style="font-family:宋体"}**[tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_134998827}[命令开启隧道验证功能后，本命令才会生效。]{style="font-family:宋体"}

[[以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x5615_53139_1440933770}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1355795991}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_806739362}[以明文方式配置隧道验证密钥为]{style="font-family:宋体"}[yougotit]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x1373647995}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] tunnel password simple yougotit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1012350156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel authentication]{lang="EN-US"}**]{#struct_0_x5615_53139_x216484030}
:::

::: {#1370339540 .myid}
[]{#_Toc404785029}[]{#struct_0_x5615_53139_x567565046}

**L2TP \-- L2TP配置命令 \-- tunnel timer hello**

------------------------------------------------------------------------

[**[tunnel timer hello]{lang="EN-US"}**]{#struct_0_x5615_53139_472016943}[命令用来配置隧道中]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[**[undo tunnel timer hello]{lang="EN-US"}**]{#struct_0_x5615_53139_838547441}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1770152708}

[**[tunnel timer hello]{lang="EN-US"}**[ *hello-interval*]{lang="EN-US"}]{#struct_0_x5615_53139_1614552605}

[**[undo tunnel timer hello]{lang="EN-US"}**]{#struct_0_x5615_53139_92347211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_214864298}

[[隧道中]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x5615_53139_x1520021927}[报文的发送时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_563930100}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_x216549566}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2140996285}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x919111070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_502750586}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1605909134}

[*[hello-interval]{lang="EN-US"}*]{#struct_0_x5615_53139_677879043}[：]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x77719939}

[[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x638261121}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[在没有]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[报文发送时，按照本命令配置的时间间隔周期性发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，以免]{style="font-family:宋体"}[LAC]{lang="EN-US"}[和]{style="font-family:宋体"}[LNS]{lang="EN-US"}[之间的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道和会话在超时后被删除。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[LNS]{lang="EN-US"}]{#struct_0_x5615_53139_1072065875}[和]{style="font-family:宋体"}[LAC]{lang="EN-US"}[上，可以配置不同的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送时间间隔。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1766616355}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x216615102}[配置隧道中]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔为]{style="font-family:宋体"}[90]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x942657360}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] tunnel timer hello 90]{lang="EN-US"}
:::

::: {#464137912 .myid}
[]{#_Toc404785030}[]{#struct_0_x5615_53139_1400294027}[]{#_Hlt13991793}

**L2TP \-- L2TP配置命令 \-- ip dscp**

------------------------------------------------------------------------

[**[ip dscp]{lang="EN-US"}**]{#struct_0_x5615_53139_1475802774}[命令用来配置隧道报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[（]{style="font-family:宋体"}[Differentiated Services Code Point]{lang="EN-US"}[，区分服务编码点）优先级。]{style="font-family:宋体"}

[**[undo ip dscp]{lang="EN-US"}**]{#struct_0_x5615_53139_916528442}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1507769344}

[**[ip dscp]{lang="EN-US"}**[ *dscp-value*]{lang="EN-US"}]{#struct_0_x5615_53139_1989132914}

[**[undo ip dscp]{lang="EN-US"}**]{#struct_0_x5615_53139_x1780576738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1614269816}

[[隧道报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}]{#struct_0_x5615_53139_x216156350}[优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_997243725}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1612159277}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1385417401}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1101504525}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_624052439}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1620946153}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_x5615_53139_2063371243}[：隧道报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1990835007}

[[DSCP]{lang="EN-US"}]{#struct_0_x5615_53139_x1093421706}[携带在]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定发送的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216221886}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1460297048}[配置隧道报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_225608783}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] ip dscp 50]{lang="EN-US"}
:::

::: {#1474946988 .myid}
[]{#_Toc404785031}[]{#struct_0_x5615_53139_1677322326}[]{#_Toc317856915}[]{#_Toc309228573}[]{#_Toc205607563}[]{#_Toc335656823}

**L2TP \-- L2TP配置命令 \-- timer-hold**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**]{#struct_0_x5615_53139_x483582371}[命令用来配置接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期。]{style="font-family:宋体"}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x5615_53139_x1132373096}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x331343451}

[**[timer-hold]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x5615_53139_x1414375726}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x5615_53139_1328009639}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216287422}

[[接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x5615_53139_600524436}[报文的周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1131600017}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_1050612952}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x161530988}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x393797331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x296707354}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_833526496}

[*[seconds]{lang="EN-US"}*]{#struct_0_x5615_53139_x454206344}[：接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1088407999}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x216352958}[接口定期向对端发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。可以通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[在速率非常低的链路上，参数]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*]{#struct_0_x5615_53139_1055451403}[不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送与接收。而接口如果在]{style="font-family:宋体"}[retry]{lang="EN-US"}[个（可以通过]{style="font-family:宋体"}**[timer-hold retry]{lang="EN-US"}**[命令修改该个数）]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期之后仍然无法收到对端的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，它就会认为链路发生故障。如果]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x461262862}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_x1255994926}[配置虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_1005959331}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] timer-hold 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1709479894}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_x5615_53139_x1709479895}
:::

::: {#518520923 .myid}
[]{#_Toc404785032}[]{#struct_0_x5615_53139_x1709479896}

**L2TP \-- L2TP配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_x5615_53139_x1638577498}[命令用来配置接口在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x5615_53139_x1344444308}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1344444307}

[**[timer-hold]{lang="EN-US"}**[ **retry** *retry*]{lang="EN-US"}]{#struct_0_x5615_53139_1053434206}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x5615_53139_x1344444306}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1344444305}

[[接口在]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x5615_53139_x109365208}[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1344444304}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x1344444303}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x915934262}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1344444302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_650149679}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1344444301}

[*[retry]{lang="EN-US"}*]{#struct_0_x5615_53139_x1344444300}[：接口在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x512649735}

[[虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x5615_53139_x1344444299}[接口定期向对端发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口的链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。可以通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[在速率非常低的链路上，参数]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*]{#struct_0_x5615_53139_994207852}[不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送与接收。而接口如果在]{style="font-family:宋体"}*[retry]{lang="EN-US"}*[个（可以通过]{style="font-family:宋体"}**[timer-hold retry]{lang="EN-US"}**[命令修改该个数）]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期之后仍然无法收到对端的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，它就会认为链路发生故障。如果]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1370228280}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_994207853}[配置虚拟]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[在]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_994207855}

[\[Sysname\] interface virtual-ppp 10]{lang="EN-US"}

[\[Sysname-Virtual-PPP10\] timer-hold retry 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1370228281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_x5615_53139_994207856}
:::

::: {#1904591196 .myid}
[]{#_Toc404785033}[]{#struct_0_x5615_53139_1892301877}[]{#_Toc395702175}

**L2TP \-- L2TP配置命令 \-- user**

------------------------------------------------------------------------

[**[user]{lang="EN-US"}**]{#struct_0_x5615_53139_x182197196}[命令用来配置本端作为]{style="font-family:宋体"}[LAC]{lang="EN-US"}[端时向]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发起隧道建立请求的触发条件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **user**]{lang="EN-US"}]{#struct_0_x5615_53139_x316104143}[命令用来删除配置的触发条件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1578804354}

[**[user]{lang="EN-US"}**[ { **domain** *domain-name* \| **fullusername** *user-name* }]{lang="EN-US"}]{#struct_0_x5615_53139_x215894206}

[**[undo user]{lang="EN-US"}**]{#struct_0_x5615_53139_329098637}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1973696577}

[[没有指定本端作为]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_x1111887776}[端时向]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发起隧道建立请求的触发条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x135648548}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_360089521}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x614768377}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1103530088}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x979805580}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x1123983140}

[**[domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_x5615_53139_x215959742}[：指定接入用户的域名与配置的域名匹配时，]{style="font-family:宋体"}[LAC]{lang="EN-US"}[向]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发起]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[表示用户域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[fullusername]{lang="EN-US"}**[ *user-name*]{lang="EN-US"}]{#struct_0_x5615_53139_x1639775429}[：指定接入用户的用户名与配置的完整用户名匹配时，]{style="font-family:宋体"}[LAC]{lang="EN-US"}[向]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发起]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求。]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[表示完整的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_897298374}

[[只有接入用户的域名或完整用户名符合本命令配置的触发条件时，]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_x5615_53139_875676758}[才会向对端]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发送建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的请求。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5615_53139_1524108881}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能在]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1960519536}[LAC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下执行本命令。]{style="font-family:宋体"}[LNS]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在同一个]{style="font-family:宋体"}]{#struct_0_x5615_53139_559329067}[L2TP]{lang="EN-US"}[组下重复执行本命令，则新的配置覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x65976347}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_1599509723}[配置接入用户的完整用户名为]{style="font-family:宋体"}[test@aabbcc.net]{lang="EN-US"}[时，触发]{style="font-family:宋体"}[LAC]{lang="EN-US"}[向]{style="font-family:宋体"}[LNS]{lang="EN-US"}[发送]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道建立请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x803258728}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] user fullusername test@aabbcc.net]{lang="EN-US"}
:::

::: {#1715388964 .myid}
[]{#_Toc404785034}[]{#struct_0_x5615_53139_x216418493}

**L2TP \-- L2TP配置命令 \-- vpn-instance**

------------------------------------------------------------------------

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_x5615_53139_x1757055108}[命令用来配置隧道对端所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x5615_53139_1800640568}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1516905378}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x5615_53139_x910138925}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x5615_53139_x2078705936}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5615_53139_432691223}

[[隧道对端属于公网。]{style="font-family:宋体"}]{#struct_0_x5615_53139_1162872523}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1391475708}

[[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_617395706}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5615_53139_x216484029}

[[network-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x567106293}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5615_53139_x1489314727}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x5615_53139_6506731}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x5615_53139_1983219676}[：]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5615_53139_1808680824}

[[通过本命令指定隧道对端所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x5615_53139_x1396628570}[后，设备将在指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内发送]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[控制消息和数据消息，即在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内查找到达控制消息和数据消息目的地址的路由，根据指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的路由转发控制消息和数据消息。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_x5615_53139_1015662111}[隧道的一个端点位于某个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中时，需要在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的另一个端点上通过本命令指定隧道对端属于该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，以便正确地在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道端点之间转发报文。]{style="font-family:宋体"}

[[执行本命令时需要注意：]{style="font-family:宋体"}]{#struct_0_x5615_53139_x1436410964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[隧道]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5615_53139_x755057297}[对端]{style="font-family:宋体"}[所属的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[应该与本端设备连接]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道对端的物理接口所属的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[（通过]{lang="EN-US" style="font-family:宋体"}**[ip binding vpn-instance]{lang="EN-US"}**[命令配置）相同。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令中指定的]{style="font-family:宋体"}]{#struct_0_x5615_53139_x216549565}[VPN]{lang="EN-US"}[实例必须已经创建。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5615_53139_2140799677}

[[\# ]{lang="EN-US"}]{#struct_0_x5615_53139_594890926}[配置隧道对端所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5615_53139_x1012053192}

[\[Sysname\] l2tp-group 1 mode lac]{lang="EN-US"}

[\[Sysname-l2tp1\] vpn-instance vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5615_53139_568329057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip vpn-instance]{lang="EN-US"}**]{#struct_0_x5615_53139_1040082602}[（]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{style="font-family:宋体"}[/MPLS L3VPN]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip binding vpn-instance]{lang="EN-US"}**]{#struct_0_x5615_53139_857627296}[（]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{style="font-family:宋体"}[/MPLS L3VPN]{lang="EN-US"}[）]{style="font-family:宋体"}
:::
