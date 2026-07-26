::: {#351315815 .myid}
[]{#_Toc404787428}[]{#struct_0_21182_x6397_x1434458080}[]{#_Toc382816936}

**WAAS \-- WAAS配置命令 \-- class**

------------------------------------------------------------------------

[**[class]{lang="EN-US"}**]{#struct_0_21182_x6397_1596456259}[命令用来配置]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略引用的指定类，并进入]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略类动作视图。]{style="font-family:宋体"}

[**[undo class]{lang="EN-US"}**]{#struct_0_21182_x6397_872694107}[命令用来取消]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略对指定类的引用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_2054669105}

[**[class ]{lang="EN-US"}***[class-name ]{lang="EN-US"}*[\[ **insert-before** *existing-class* \]]{lang="EN-US"}]{#struct_0_21182_x6397_682117391}

[**[undo class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_21182_x6397_467694538}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1685095293}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_276830024}[策略未引用任何类。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1014479197}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_972098944}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_868838471}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x2111151160}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1867061923}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x786469783}

[*[class-name]{lang="EN-US"}*]{#struct_0_21182_x6397_x576842572}[：[]{#OLE_LINK4}[指定引用的类名称，为]{#OLE_LINK3}]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，该类必须存在。]{style="font-family:宋体"}

[**[insert-before]{lang="EN-US"}**[ *existing-class*]{lang="EN-US"}]{#struct_0_21182_x6397_199289911}[：表示插入到指定类之前，]{style="font-family:宋体"}*[existing-class]{lang="EN-US"}*[表示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略已引用的类名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1156956623}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1895622179}[策略支持引用预定义类。（预定义类参见]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-7]{lang="EN-US"}](?-326408526#_Ref401328623)[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文流量匹配类时，按照引用的类的排序进行匹配，匹配上任一个类，则按照相应动作处理报文流量。]{style="font-family:宋体"}]{#struct_0_21182_x6397_x776131200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令，可对]{style="font-family:宋体"}]{#struct_0_21182_x6397_2014612832}[WAAS]{lang="EN-US"}[策略已引用的多个类进行排序。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1399976017}[WAAS]{lang="EN-US"}[策略未为引用的类配置任何动作，则该类不参与所属策略对报文流量的匹配。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议用户通过执行此命令进入预定义类动作视图，通过修改预定义类的方式完成配置。]{style="font-family:宋体"}]{#struct_0_21182_x6397_1998677831}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_667864323}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x1058174217}[配置]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略引用预定义类]{style="font-family:宋体"}[AFS]{lang="EN-US"}[，并进入其动作视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_1292867948}

[\[Sysname\] waas policy waas_global]{lang="EN-US"}

[\[Sysname-waaspolicy-waas_global\] class AFS]{lang="EN-US"}

[\[Sysname-waaspolicy-waas_global-AFS\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x1617769404}[配置]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略引用预定义类]{style="font-family:宋体"}[AOL]{lang="EN-US"}[，将其插入到]{style="font-family:宋体"}[AFS]{lang="EN-US"}[之前，并进入]{style="font-family:宋体"}[AOL]{lang="EN-US"}[动作视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_193824578}

[\[Sysname\] waas policy waas_global]{lang="EN-US"}

[\[Sysname-waaspolicy-waas_global\] class AOL insert-before AFS]{lang="EN-US"}

[\[Sysname-waaspolicy-waas_global-AOL\]]{lang="EN-US"}

[[\# WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x1705062834}[策略已依次引用预定义类]{style="font-family:宋体"}[AFS]{lang="EN-US"}[、]{style="font-family:宋体"}[AOL]{lang="EN-US"}[，调整]{style="font-family:宋体"}[class]{lang="EN-US"}[顺序，将]{style="font-family:宋体"}[AOL]{lang="EN-US"}[插入到]{style="font-family:宋体"}[AFS]{lang="EN-US"}[之前，并进入]{style="font-family:宋体"}[AOL]{lang="EN-US"}[类动作视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x754151513}

[\[Sysname\] waas policy waas_global]{lang="EN-US"}

[\[Sysname-waaspolicy-waas_global\] class AOL insert-before AFS]{lang="EN-US"}

[\[Sysname-waaspolicy-waas_global-AOL\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_452754793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_1952752155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_1918319487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x689359491}
:::

::: {#1395263565 .myid}
[]{#struct_0_21182_x6397_1085674594}[]{#_Toc404787429}

**WAAS \-- WAAS配置命令 \-- display waas class**

------------------------------------------------------------------------

[**[display waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_x230274653}[命令]{style="font-family:宋体"}[用来显示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1149636480}

[**[display waas class ]{lang="EN-US"}**[\[ *class-name* \]]{lang="EN-US"}]{#struct_0_21182_x6397_905414650}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_332564312}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1697810803}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1704155044}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_98462421}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_481577933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1763106623}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x1386628053}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1815785087}

[*[class-name]{lang="EN-US"}*]{#struct_0_21182_x6397_283082611}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_386668214}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x866700090}[显示类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display waas class class1]{lang="EN-US"}]{#struct_0_21182_x6397_x93642384}

[WAAS class: ]{lang="EN-US"}[class1]{lang="EN-US"}

[  match 1 tcp source 1.1.1.1/24 port 50000 60000]{lang="EN-US"}

[  match 6 tcp destination 2.2.2.2 port 1 1024]{lang="EN-US"}

[  match 11 tcp source 1001::1111/96 port 50000 60000]{lang="EN-US"}

[  match 16 tcp destination 2002::2222 port 1 1024]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display waas class]{lang="EN-US"}]{#struct_0_21182_x6397_1361981035}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x653129435}[[字段]{style="font-family:黑体"}]{#struct_0_21182_x6397_1750976319}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1994037178}

[[WAAS class]{lang="EN-US"}]{#struct_0_21182_x6397_x911195572}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x1658966042}[类的名称]{style="font-family:宋体"}

[[match]{lang="EN-US"}]{#struct_0_21182_x6397_x1179415727}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1869018087}[类包含的匹配规则]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_938520300}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[match tcp]{lang="EN-US"}**]{#struct_0_21182_x6397_243802273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_x355864109}

::: {#1404163808 .myid}
[]{#_Toc404787430}[]{#struct_0_21182_x6397_795484321}

**WAAS \-- WAAS配置命令 \-- display waas policy**

------------------------------------------------------------------------

[**[display waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_1030532801}[命令用来显示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_103349678}

[**[display waas policy]{lang="EN-US"}**[ \[ *policy-name* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x1609421975}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_548901906}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1985426991}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_913203243}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_931339226}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x109954536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_637322290}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x2101870474}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1549467628}

[*[policy-name]{lang="EN-US"}*]{#struct_0_21182_x6397_x549323700}[：指定]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x570516367}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_559463943}[显示指定]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略]{style="font-family:宋体"}[po1]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display waas policy po1]{lang="EN-US"}]{#struct_0_21182_x6397_1031614202}

[WAAS ]{lang="EN-US"}[policy: po1]{lang="EN-US"}

[  class cl1]{lang="EN-US"}

[    optimize TFO DRE LZ]{lang="EN-US"}

[  class cl2]{lang="EN-US"}

[    optimize TFO DRE]{lang="EN-US"}

[  class cl3]{lang="EN-US"}

[    passthrough]{lang="EN-US"}

[  class cl4]{lang="EN-US"}

[    optimize TFO LZ]{lang="EN-US"}

[  class cl5]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display waas policy]{lang="EN-US"}]{#struct_0_21182_x6397_1690811271}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x651469045}[[字段]{style="font-family:黑体"}]{#struct_0_21182_x6397_x16616313}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21182_x6397_1129021073}

[[WAAS policy]{lang="EN-US"}]{#struct_0_21182_x6397_x413685632}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1480143021}[策略的名称]{style="font-family:宋体"}

[[class]{lang="EN-US"}]{#struct_0_21182_x6397_x996998474}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_534806957}[策略引用的]{style="font-family:宋体"}[class]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[optimize]{lang="EN-US"}]{#struct_0_21182_x6397_304106562}

[[class]{lang="EN-US"}]{#struct_0_21182_x6397_x321266303}[配置的优化方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TFO]{lang="FR"}]{#struct_0_21182_x6397_783816576}[：表示流传输优化方式，仅支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[流传输优化。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRE]{lang="FR"}]{#struct_0_21182_x6397_x1499614099}[：表示]{style="font-family:宋体"}[消除冗余数据优化方式。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LZ]{lang="FR"}]{#struct_0_21182_x6397_x1412711710}[：表示]{style="font-family:宋体"}[数据压缩优化方式。]{style="font-family:宋体"}

[[passthrough]{lang="EN-US"}]{#struct_0_21182_x6397_x1582700254}

[[class]{lang="EN-US"}]{#struct_0_21182_x6397_x436627870}[直接旁路动作，不做任何优化处理]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x136346363}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[class]{lang="EN-US"}**]{#struct_0_21182_x6397_x1675757310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[optimize]{lang="EN-US"}**]{#struct_0_21182_x6397_x1638991241}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[passthrough]{lang="EN-US"}**]{#struct_0_21182_x6397_170274489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x131205637}

::: {#2086123682 .myid}
[]{#_Toc404787431}[]{#struct_0_21182_x6397_x91251993}

**WAAS \-- WAAS配置命令 \-- display waas session**

------------------------------------------------------------------------

[**[display waas session]{lang="EN-US"}**]{#struct_0_21182_x6397_x250412358}[命令用来显示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_842074454}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1859355914}

[**[display waas session ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **client-ip** *client-ip* \] \[ **client-port** *client-port* \] \[ **server-ip**]{lang="EN-US"}]{#struct_0_21182_x6397_x1745038729}

[*[server-ip]{lang="EN-US"}***[ ]{lang="EN-US"}**[\] \[ **server-port** *server-port* \] \[ **peer-id** *peer-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_21182_x6397_x1292113796}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21182_x6397_x241789187}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display waas session ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **client-ip** *client-ip* \] \[ **client-port** *client-port* \] \[ **server-ip**]{lang="EN-US"}]{#struct_0_21182_x6397_260647660}

[*[server-ip]{lang="EN-US"}***[ ]{lang="EN-US"}**[\] \[ **server-port** *server-port* \] \[ **peer-id** *peer-id* \] \[ **verbose** \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_21182_x6397_1146183101}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21182_x6397_x924004580}[模式：]{style="font-family:宋体"}

[**[display waas session ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **client-ip** *client-ip* \] \[ **client-port** *client-port* \] \[ **server-ip**]{lang="EN-US"}]{#struct_0_21182_x6397_771173888}

[*[server-ip]{lang="EN-US"}***[ ]{lang="EN-US"}**[\] \[ **server-port** *server-port* \] \[ **peer-id** *peer-id* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x278229079}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1911166877}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1350905314}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x96535544}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1729325038}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_1119147566}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1944290909}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x1089280121}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x937465290}

[**[ipv4]{lang="EN-US"}**]{#struct_0_21182_x6397_1203018643}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_21182_x6397_1100073158}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[**[client-ip ]{lang="EN-US"}***[client-ip]{lang="EN-US"}*]{#struct_0_21182_x6397_x1155616942}[：显示指定客户端地址的会话信息，]{style="font-family:宋体"}*[client-ip]{lang="EN-US"}*[表示客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[client-port ]{lang="EN-US"}***[client-port]{lang="EN-US"}*]{#struct_0_21182_x6397_x249147070}[：显示指定客户端端口号的会话信息，]{style="font-family:宋体"}*[client-port]{lang="EN-US"}*[表示客户端端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[server-ip ]{lang="EN-US"}***[server-ip]{lang="EN-US"}*]{#struct_0_21182_x6397_x1132361560}[：显示指定服务器端地址的会话信息，]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[表示服务器端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[server-port ]{lang="EN-US"}***[server-port]{lang="EN-US"}*]{#struct_0_21182_x6397_x101009795}[：显示指定服务器端端口号的会话信息，]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[表示服务器端端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[peer-id ]{lang="EN-US"}***[peer-id]{lang="EN-US"}*]{#struct_0_21182_x6397_393218536}[：显示指定对端设备的]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[会话信息，]{style="font-family:宋体"}*[peer-id]{lang="EN-US"}*[表示对端设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_21182_x6397_x1283406471}[：显示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[会话的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[会话的简要信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_254949457}[：显示指定单板的会话信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的会话信息。（分布设备]{style="font-family:宋体"}[-]{lang="EN-US"}[独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_x576494227}[：显示指定成员设备的会话信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示所有成员设备上的会话信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_x1389177620}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的会话信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的会话信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21182_x6397_1912128786}[：显示指定成员设备上指定单板的会话信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的会话信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21182_x6397_x666261034}[：显示指定单板的会话信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟槽位号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示所有单板上的会话信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1724814651}

[[显示所有满足指定条件的会话的信息。如果除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_21182_x6397_1415078000}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[外没有指定任何参数，将显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的会话信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2143835651}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_118636807}[显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display waas session ipv4]{lang="EN-US"}]{#struct_0_21182_x6397_1596521795}

[Peer ID: 0021-90ad-0012]{lang="EN-US"}

[Start Time: Fri Mar 21 10:43:05 2014]{lang="EN-US"}

[Source IP/Port: 1.1.1.1/34572]{lang="EN-US"}

[Destination IP/Port: 2.2.2.2/80]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer ID: 0011-10ad-0012]{lang="EN-US"}

[Start Time: Fri Mar 21 10:45:05 2014]{lang="EN-US"}

[Source IP/Port: 2.2.1.1/34572]{lang="EN-US"}

[Destination IP/Port: 3.2.2.3/80]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 2 sessions found.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_87286645}[显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display waas session ipv4 verbose]{lang="EN-US"}]{#struct_0_21182_x6397_1952817691}

[Peer ID: 0021-90ad0-01221]{lang="EN-US"}

[Start Time: Fri Mar 21 11:43:05 2014]{lang="EN-US"}

[Source IP/Port: 1.1.1.1/34572]{lang="EN-US"}

[Destination IP/Port: 2.2.2.2/80]{lang="EN-US"}

[LAN interface: Serial1/0/1]{lang="EN-US"}

[WAN interface: Serial1/0/2]{lang="EN-US"}

[Configured Policy: TFO DRE LZ]{lang="EN-US"}

[Negotiated Policy: TFO DRE LZ]{lang="EN-US"}

[LAN-\>WAN bytes: Original   104884      Optimized  88594]{lang="EN-US"}

[WAN-\>LAN bytes: Original   744588      Optimized  3355445]{lang="EN-US"}

[LZ section]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Encode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 0]{lang="EN-US"}

[    Bytes out: 0]{lang="EN-US"}

[    Bypass bytes: 400]{lang="EN-US"}

[    Space saved: 0%]{lang="EN-US"}

[    Average Latency: 0 usec]{lang="EN-US"}

[  Decode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 329]{lang="EN-US"}

[    Bytes out: 393]{lang="EN-US"}

[    Bypass bytes: 63]{lang="EN-US"}

[    Space saved: 16%]{lang="EN-US"}

[    Average Latency: 2 usec]{lang="EN-US"}

[DRE section]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Encode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 0]{lang="EN-US"}

[    Bytes out: 0]{lang="EN-US"}

[    Bypass bytes: 314]{lang="EN-US"}

[    Space saved: 0%]{lang="EN-US"}

[    Average latency: 0 usec]{lang="EN-US"}

[  Decode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 399]{lang="EN-US"}

[    Bytes out: 332]{lang="EN-US"}

[    Bypass bytes: 0]{lang="EN-US"}

[    Space saved: 0%]{lang="EN-US"}

[    Chunk miss]{lang="EN-US"}[: 0]{lang="EN-US"}

[    ]{lang="EN-US"}[Collision: 0]{lang="EN-US"}

[    Average latency: 23 usec]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer ID: 0011-10ad-0012]{lang="EN-US"}

[Start Time: Fri Mar 21 11:43:05 2014]{lang="EN-US"}

[Source IP/Port: 2.2.1.1/34572]{lang="EN-US"}

[Destination IP/Port: 3.2.2.3/80]{lang="EN-US"}

[LAN interface: Serial1/0/1]{lang="EN-US"}

[WAN interface: Serial1/0/2]{lang="EN-US"}

[Configured Policy: TFO DRE LZ]{lang="EN-US"}

[Negotiated Policy: TFO DRE LZ]{lang="EN-US"}

[LAN-\>WAN bytes: Original   104884      Optimized  88594]{lang="EN-US"}

[WAN-\>LAN bytes: Original   744588      Optimized  3355445]{lang="EN-US"}

[LZ section]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Encode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 0]{lang="EN-US"}

[    Bytes out: 0]{lang="EN-US"}

[    Bypass bytes: 400]{lang="EN-US"}

[    Space saved: 0%]{lang="EN-US"}

[    Average Latency: 0 usec]{lang="EN-US"}

[  Decode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 329]{lang="EN-US"}

[    Bytes out: 393]{lang="EN-US"}

[    Bypass bytes: 63]{lang="EN-US"}

[    Space saved: 16%]{lang="EN-US"}

[    Average Latency: 2 usec]{lang="EN-US"}

[DRE section]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Encode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 0]{lang="EN-US"}

[    Bytes out: 0]{lang="EN-US"}

[    Bypass bytes: 314]{lang="EN-US"}

[    Space saved: 0%]{lang="EN-US"}

[    Average latency: 0 usec]{lang="EN-US"}

[  Decode status]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Bytes in: 399]{lang="EN-US"}

[    Bytes out: 332]{lang="EN-US"}

[    Bypass bytes: 0]{lang="EN-US"}

[    Space saved: 0%]{lang="EN-US"}

[    Chunk miss]{lang="EN-US"}[: 0]{lang="EN-US"}

[    ]{lang="EN-US"}[Collision: 0]{lang="EN-US"}

[    Average latency 23 usec]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 2 sessions found.]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display waas session]{lang="EN-US"}]{#struct_0_21182_x6397_x1555369005}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x627751391}[[字段]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1433091539}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21182_x6397_1888071753}

[[Peer ID]{lang="EN-US"}]{#struct_0_21182_x6397_x768349168}

[[对端设备]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_21182_x6397_x220794689}[，即设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，用来唯一标识一台对端设备]{style="font-family:宋体"}

[[Start time]{lang="EN-US"}]{#struct_0_21182_x6397_x166908137}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1183743184}[会话建立时间]{style="font-family:宋体"}

[[Source IP/Port]{lang="EN-US"}]{#struct_0_21182_x6397_386733750}

[[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21182_x6397_x489653466}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Destination IP/Port]{lang="EN-US"}]{#struct_0_21182_x6397_421646483}

[[服务器端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21182_x6397_x2087075055}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[LAN interface]{lang="EN-US"}]{#struct_0_21182_x6397_x2018892690}

[[LAN]{lang="EN-US"}]{#struct_0_21182_x6397_1083248040}[侧接口]{style="font-family:宋体"}

[[WAN interface]{lang="EN-US"}]{#struct_0_21182_x6397_x1599286560}

[[WAN]{lang="EN-US"}]{#struct_0_21182_x6397_768655092}[侧接口]{style="font-family:宋体"}

[[Configured Policy]{lang="EN-US"}]{#struct_0_21182_x6397_x1094099610}

[[本端设备配置的优化方式，取值包括：]{style="font-family:宋体"}]{#struct_0_21182_x6397_x634057428}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1179350191}[：表示流传输优化方式，仅支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[流传输优化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x165490821}[：表示]{style="font-family:宋体"}[消除冗余数据优化方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LZ]{lang="EN-US"}]{#struct_0_21182_x6397_x1835720378}[：表示数据压缩优化方式]{style="font-family:宋体"}

[[Negotiated Policy]{lang="EN-US"}]{#struct_0_21182_x6397_x1747031987}

[[与对端设备协商后的优化动作，取值包括：]{style="font-family:宋体"}]{#struct_0_21182_x6397_990880870}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1602295982}[：表示流传输优化方式，仅支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[流传输优化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1450073565}[：表示]{style="font-family:宋体"}[消除冗余数据优化方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LZ]{lang="EN-US"}]{#struct_0_21182_x6397_x142219389}[：表示数据压缩优化方式]{style="font-family:宋体"}

[[协商后的优化方式取两端]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1549533164}[设备配置优化方式的交集]{style="font-family:宋体"}

[[LAN-\>WAN bytes]{lang="EN-US"}]{#struct_0_21182_x6397_x194785643}

[[LAN]{lang="EN-US"}]{#struct_0_21182_x6397_x694778859}[侧接口到]{style="font-family:宋体"}[WAN]{lang="EN-US"}[侧接口的数据统计：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Original]{lang="EN-US"}]{#struct_0_21182_x6397_1544978802}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[原始字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Optimized]{lang="EN-US"}]{#struct_0_21182_x6397_2058545030}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[优化后的字节数]{lang="EN-US" style="font-family:宋体"}

[[WAN-\>LAN bytes]{lang="EN-US"}]{#struct_0_21182_x6397_827117993}

[[WAN]{lang="EN-US"}]{#struct_0_21182_x6397_x16550777}[侧接口到]{style="font-family:宋体"}[LAN]{lang="EN-US"}[侧接口的数据统计：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Original]{lang="EN-US"}]{#struct_0_21182_x6397_444879205}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[原始字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Optimized]{lang="EN-US"}]{#struct_0_21182_x6397_x1175239163}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[优化后的字节数]{lang="EN-US" style="font-family:宋体"}

[[LZ section]{lang="EN-US"}]{#struct_0_21182_x6397_913868875}

[[LZ]{lang="EN-US"}]{#struct_0_21182_x6397_x1099704492}[统计信息]{style="font-family:宋体"}

[[DRE section]{lang="EN-US"}]{#struct_0_21182_x6397_411863082}

[[DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x816451350}[统计信息]{style="font-family:宋体"}

[[Encode status]{lang="EN-US"}]{#struct_0_21182_x6397_x1582634718}

[[压缩统计信息]{style="font-family:宋体"}]{#struct_0_21182_x6397_1409644440}

[[Decode status]{lang="EN-US"}]{#struct_0_21182_x6397_x1370884592}

[[解压缩统计信息]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1217786684}

[[Bytes in]{lang="EN-US"}]{#struct_0_21182_x6397_92347094}

[[输入字节数]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1003014526}

[[Bytes out]{lang="EN-US"}]{#struct_0_21182_x6397_1146248637}

[[输出字节数]{style="font-family:宋体"}]{#struct_0_21182_x6397_977725677}

[[Bypass bytes]{lang="EN-US"}]{#struct_0_21182_x6397_849677941}

[[未匹配上字典的字节数]{style="font-family:宋体"}]{#struct_0_21182_x6397_1513511103}

[[Space saved]{lang="EN-US"}]{#struct_0_21182_x6397_536186854}

[[压缩率，计算公式：]{style="font-family:宋体"}]{#struct_0_21182_x6397_x124347260}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[压缩]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1132296024}[：]{lang="EN-US" style="font-family:宋体"}[(1 - (Bytes out / Bytes in)) \* 100]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[解压：]{style="font-family:宋体"}[(1 - (Bytes ]{lang="EN-US"}]{#struct_0_21182_x6397_x677891395}[in]{lang="EN-US"}[/ Bytes ]{lang="EN-US"}[out]{lang="EN-US"}[)) \* 100]{lang="EN-US"}

[[Average Latency]{lang="EN-US"}]{#struct_0_21182_x6397_x101675408}

[[最后一次压缩或者解压的平均延迟时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_21182_x6397_13449387}

[[Chunk miss]{lang="EN-US"}]{#struct_0_21182_x6397_2089343210}

[[无法根据字典索引找到字典表项累计次数]{style="font-family:宋体"}]{#struct_0_21182_x6397_1839003058}

[[Collision]{lang="EN-US"}]{#struct_0_21182_x6397_1596587331}

[[解码后数据校验失败累计次数]{style="font-family:宋体"}]{#struct_0_21182_x6397_457231525}

[[Total sessions]{lang="EN-US"}]{#struct_0_21182_x6397_x342196814}

[[当前建立的会话总数]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1939450582}

[ ]{lang="EN-US"}

::: {#663869603 .myid}
[]{#_Toc404787432}[]{#struct_0_21182_x6397_x829526721}

**WAAS \-- WAAS配置命令 \-- display waas statistics dre**

------------------------------------------------------------------------

[**[display waas statistics dre]{lang="EN-US"}**]{#struct_0_21182_x6397_x2035083263}[命令用来显示]{style="font-family:
宋体"}[DRE]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_2036945637}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21182_x6397_1657913415}

[**[display waas statistics dre ]{lang="EN-US"}**[\[ **peer** *peer-id* \]]{lang="EN-US"}]{#struct_0_21182_x6397_989382167}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21182_x6397_x776000128}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display waas statistics dre ]{lang="EN-US"}**[\[ **peer** *peer-id* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x1878916708}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21182_x6397_x1007038790}[模式：]{style="font-family:宋体"}

[**[display waas statistics dre ]{lang="EN-US"}**[\[ **peer** *peer-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x614285958}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1247752136}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1116953154}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x216226254}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1326138580}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x1301945116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1246909376}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_1106309606}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x14598784}

[**[peer ]{lang="EN-US"}***[peer-id]{lang="EN-US"}*]{#struct_0_21182_x6397_1985333928}[：显示指定对端]{style="font-family:宋体"}[设备的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[peer-id]{lang="EN-US"}*[表示设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。如果未指定本参数，则显示设备上所有]{style="font-family:宋体"}[DRE]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_1318978300}[：显示指定单板上的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。（分布设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_x177035050}[：显示指定成员设备的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示所有成员设备上的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_883777383}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21182_x6397_1952883227}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21182_x6397_1550435898}[：显示指定单板的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟槽位号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示所有单板上的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1703206286}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_648678745}[显示设备上所有]{style="font-family:宋体"}[DRE]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display waas statistics dre]{lang="EN-US"}]{#struct_0_21182_x6397_386799286}

[Peer-ID: 0016-9d38-ca1d]{lang="EN-US"}

[Peer version: 1.0]{lang="EN-US"}

[Cache in storage: 614017 bytes]{lang="EN-US"}

[Index number: 11513600]{lang="EN-US"}

[Age: 3 weeks, 5 days, 21 hours, 22 minutes, 40 seconds]{lang="EN-US"}

[Total connections: 24]{lang="EN-US"}

[Active connections: 1]{lang="EN-US"}

[Encode Statistics]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Dre msgs: 64]{lang="EN-US"}

[  Bytes in: 67344 bytes]{lang="EN-US"}

[  Bytes out: 8840 bytes]{lang="EN-US"}

[  Bypass bytes: 35714 bytes]{lang="EN-US"}

[  Bytes Matched: 59355 bytes]{lang="EN-US"}

[  Space saved: 13%]{lang="EN-US"}

[  Average latency: 2191 usec]{lang="EN-US"}

[Decode Statistics]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Dre msgs: 318]{lang="EN-US"}

[  Bytes in: 8494760 bytes]{lang="EN-US"}

[  Bytes out: 13780812 bytes]{lang="EN-US"}

[  Bypass bytes: 35556 bytes]{lang="EN-US"}

[  Space saved: 38%]{lang="EN-US"}

[  Average latency: 1471 usec]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer-ID: 0d38-9d38-ca1d]{lang="EN-US"}

[Peer version: 1.0]{lang="EN-US"}

[Cache in storage: 614017 bytes ]{lang="EN-US"}

[Index number: 11513600]{lang="EN-US"}

[Age: 3 weeks, 5 days, 21 hours, 22 minutes, 40 seconds]{lang="EN-US"}

[Total connections: 24]{lang="EN-US"}

[Active connections: 1]{lang="EN-US"}

[Encode Statistics]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Dre msgs: 64]{lang="EN-US"}

[  Bytes in: 67344 bytes]{lang="EN-US"}

[  Bytes out: 8840 bytes]{lang="EN-US"}

[  Bypass bytes: 35714 bytes]{lang="EN-US"}

[  Bytes Matched: 59355 bytes]{lang="EN-US"}

[  Space saved: 13%]{lang="EN-US"}

[  Average latency: 2191 usec]{lang="EN-US"}

[Decode Statistics]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Dre msgs: 318]{lang="EN-US"}

[  Bytes in: 8494760 bytes]{lang="EN-US"}

[  Bytes out: 13780812 bytes]{lang="EN-US"}

[  Bypass bytes: 35556 bytes]{lang="EN-US"}

[  Space saved: 38%]{lang="EN-US"}

[  Average latency: 1471 usec]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x889834657}[显示指定对端设备的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display waas statistics dre peer 0016-9d38-ca1d]{lang="EN-US"}]{#struct_0_21182_x6397_x1179284655}

[Peer-ID: 0016-9d38-ca1d]{lang="EN-US"}

[Peer version: 1.0]{lang="EN-US"}

[Cache in storage: 614017 bytes ]{lang="EN-US"}

[Index number: 11513600]{lang="EN-US"}

[Age: 3 weeks, 5 days, 21 hours, 22 minutes, 40 seconds]{lang="EN-US"}

[Total connections: 24]{lang="EN-US"}

[Active connections: 1]{lang="EN-US"}

[Encode Statistics]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Dre msgs: 64]{lang="EN-US"}

[  Bytes in: 67344 bytes]{lang="EN-US"}

[  Bytes out: 8840 bytes]{lang="EN-US"}

[  Bypass bytes: 35714 bytes]{lang="EN-US"}

[  Bytes Matched: 59355 bytes]{lang="EN-US"}

[  Space saved: 13%]{lang="EN-US"}

[  Average latency: 2191 usec]{lang="EN-US"}

[Decode Statistics]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Dre msgs: 318]{lang="EN-US"}

[  Bytes in: 8494760 bytes]{lang="EN-US"}

[  Bytes out: 13780812 bytes]{lang="EN-US"}

[  Bypass bytes: 35556 bytes]{lang="EN-US"}

[  Space saved: 38%]{lang="EN-US"}

[  Average latency: 1471 usec]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display waas statistics dre]{lang="EN-US"}]{#struct_0_21182_x6397_1922700537}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x607051545}[[字段]{style="font-family:黑体"}]{#struct_0_21182_x6397_1299854210}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21182_x6397_x537253360}

[[Peer-ID]{lang="EN-US"}]{#struct_0_21182_x6397_1578456709}

[[对端设备]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_21182_x6397_1204482084}[，即设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，用来唯一标识一台对端设备]{style="font-family:宋体"}

[[Peer version]{lang="EN-US"}]{#struct_0_21182_x6397_x1332463048}

[[对端设备的]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_353847844}[版本号]{style="font-family:宋体"}

[[Cache in storage]{lang="EN-US"}]{#struct_0_21182_x6397_981578232}

[[元数据占用的空间大小，单位为字节]{style="font-family:宋体"}]{#struct_0_21182_x6397_1549598700}

[[Index number]{lang="EN-US"}]{#struct_0_21182_x6397_x1806243830}

[[元数据块索引的个数]{style="font-family:宋体"}]{#struct_0_21182_x6397_432581137}

[[Age]{lang="EN-US"}]{#struct_0_21182_x6397_906531339}

[[peer]{lang="EN-US"}]{#struct_0_21182_x6397_1861537745}[节点存在时间]{style="font-family:宋体"}

[[Total connections]{lang="EN-US"}]{#struct_0_21182_x6397_x909278366}

[[DER]{lang="EN-US"}]{#struct_0_21182_x6397_324965778}[连接总数]{style="font-family:宋体"}

[[Active connections]{lang="EN-US"}]{#struct_0_21182_x6397_1737421959}

[[DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x2116378632}[活动连接数]{style="font-family:宋体"}

[[Encode Statistics]{lang="EN-US"}]{#struct_0_21182_x6397_x1805914889}

[[压缩统计信息]{style="font-family:宋体"}]{#struct_0_21182_x6397_x16485241}

[[Decode Statistics]{lang="EN-US"}]{#struct_0_21182_x6397_846859005}

[[解压缩统计信息]{style="font-family:宋体"}]{#struct_0_21182_x6397_x294753013}

[[Dre msgs]{lang="EN-US"}]{#struct_0_21182_x6397_x196884360}

[[数据块个数]{style="font-family:宋体"}]{#struct_0_21182_x6397_345635091}

[[Bytes in]{lang="EN-US"}]{#struct_0_21182_x6397_1528699951}

[[输入字节数]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1580053235}

[[Bytes out]{lang="EN-US"}]{#struct_0_21182_x6397_178748298}

[[输出字节数]{style="font-family:宋体"}]{#struct_0_21182_x6397_1000181183}

[[Bypass bytes]{lang="EN-US"}]{#struct_0_21182_x6397_x1582569182}

[[未匹配上字典的字节数]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1960936117}

[[Bytes Matched]{lang="EN-US"}]{#struct_0_21182_x6397_x148183488}

[[匹配上字典的字节数]{style="font-family:宋体"}]{#struct_0_21182_x6397_866163752}

[[Space saved]{lang="EN-US"}]{#struct_0_21182_x6397_2080677229}

[[压缩率，计算公式：]{style="font-family:宋体"}]{#struct_0_21182_x6397_1208731906}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[压缩]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1277650908}[：]{lang="EN-US" style="font-family:宋体"}[(1 - (Bytes out / Bytes in)) \* 100]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[解压：]{style="font-family:宋体"}[(1 - (Bytes ]{lang="EN-US"}]{#struct_0_21182_x6397_1794233783}[in]{lang="EN-US"}[/ Bytes ]{lang="EN-US"}[out]{lang="EN-US"}[)) \* 100]{lang="EN-US"}

[[Average latency]{lang="EN-US"}]{#struct_0_21182_x6397_1146314173}

[[最后一次压缩或者解压的平均延迟时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_21182_x6397_x509775476}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1146304652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset waas statistics dre]{lang="EN-US"}**]{#struct_0_21182_x6397_x1695256182}

::: {#-1388979584 .myid}
[]{#_Toc404787433}[]{#struct_0_21182_x6397_x1303154924}[]{#_Toc382827017}

**WAAS \-- WAAS配置命令 \-- display waas status**

------------------------------------------------------------------------

[**[display waas status]{lang="EN-US"}**]{#struct_0_21182_x6397_1088915153}[命令用来显示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[全局状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2083406505}

[**[display waas status]{lang="EN-US"}**]{#struct_0_21182_x6397_x1276487888}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1695170306}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1863418104}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1498914885}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x308008454}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_95262033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1875804894}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x1132230488}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x612279761}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_192741937}[显示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[全局状态。]{style="font-family:宋体"}

[[\<Sysname\> display waas status]{lang="EN-US"}]{#struct_0_21182_x6397_1410354380}

[WAAS Version: 1.0]{lang="EN-US"}

[Local ID: 02e0-011a-0000]{lang="EN-US"}

[DRE Status: Disabled]{lang="EN-US"}

[LZ Status: Disabled]{lang="EN-US"}

[BlackList Status: Disabled]{lang="EN-US"}

[Total Active connections: 7889]{lang="EN-US"}

[Total data storage size: 1468006400 bytes]{lang="EN-US"}

[Total index number: 11513600]{lang="EN-US"}

[Blacklist Hold-time]{lang="EN-US"}[：]{style="font-family:宋体"}[5 minutes]{lang="EN-US"}

[Interfaces             Applied policy]{lang="EN-US"}

[Serial1/0/1            waas_global]{lang="EN-US"}

[Serial1/0/2            waas_default]{lang="EN-US"}

[Serial2/0/5            waas_global[]{#_GoBack}]{lang="EN-US"}

[  ]{lang="EN-US"}

[Total policy interfaces: 3]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display waas status]{lang="EN-US"}]{#struct_0_21182_x6397_466605996}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x608219949}[[字段]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2122641783}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21182_x6397_877679062}

[[WAAS Version]{lang="EN-US"}]{#struct_0_21182_x6397_1235897994}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1596652867}[版本号]{style="font-family:宋体"}

[[Local ID]{lang="EN-US"}]{#struct_0_21182_x6397_931295022}

[[本端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_21182_x6397_1059464212}[，即]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，用来唯一标识一台]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[[DRE Status]{lang="EN-US"}]{#struct_0_21182_x6397_423186976}

[[是否开启]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_311308007}[数据冗余消除功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_21182_x6397_1580072092}[：]{lang="EN-US" style="font-family:宋体"}[表示已开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_21182_x6397_357207604}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[未]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}

[[LZ Status]{lang="EN-US"}]{#struct_0_21182_x6397_x1114839006}

[[是否开启]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1131388723}[数据压缩功能功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_21182_x6397_x1331709416}[：]{lang="EN-US" style="font-family:宋体"}[表示已开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_21182_x6397_x289771265}[：]{lang="EN-US" style="font-family:宋体"}[表示未开启]{style="font-family:宋体"}

[[BlackList Status]{lang="EN-US"}]{#struct_0_21182_x6397_x775934592}

[[是否开启自动发现黑名单功能：]{style="font-family:宋体"}]{#struct_0_21182_x6397_1334170966}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_21182_x6397_1466897662}[：]{lang="EN-US" style="font-family:宋体"}[表示已开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_21182_x6397_x2119400697}[：]{lang="EN-US" style="font-family:宋体"}[表示未开启]{style="font-family:宋体"}

[[Total Active connections]{lang="EN-US"}]{#struct_0_21182_x6397_x898146170}

[[当前的]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_114560723}[活动连接数]{style="font-family:宋体"}

[[Total data storage size]{lang="EN-US"}]{#struct_0_21182_x6397_x380633974}

[[所有元数据所占空间的大小，单位为字节。元数据即为字典索引对应的原始数据]{style="font-family:宋体"}]{#struct_0_21182_x6397_x274280302}

[[Total index number]{lang="EN-US"}]{#struct_0_21182_x6397_1952948763}

[[元数据对应的所有字典索引的个数]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1241724732}

[[Blacklist Hold-time]{lang="EN-US"}]{#struct_0_21182_x6397_x280123923}

[[黑名单表项的老化时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_21182_x6397_x49426486}

[[Interfaces]{lang="EN-US"}]{#struct_0_21182_x6397_65271785}

[[已应用]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1890306069}[策略的接口列表]{style="font-family:宋体"}

[[Applied policy]{lang="EN-US"}]{#struct_0_21182_x6397_676479492}

[[接口应用策略列表]{style="font-family:宋体"}]{#struct_0_21182_x6397_1652033453}

[[Total policy interfaces]{lang="EN-US"}]{#struct_0_21182_x6397_386864822}

[[应用]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x239622474}[策略的接口总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1450937977 .myid}
[]{#_Toc404787434}[]{#struct_0_21182_x6397_x1373385716}

**WAAS \-- WAAS配置命令 \-- display waas tfo auto-discovery blacklist**

------------------------------------------------------------------------

[**[display waas tfo auto-discovery blacklist]{lang="EN-US"}**]{#struct_0_21182_x6397_1256316863}[命令用来显示黑名单信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_129591696}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21182_x6397_1783382206}

[**[display waas tfo auto-discovery blacklist ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** }]{lang="EN-US"}]{#struct_0_21182_x6397_894602846}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21182_x6397_1107296825}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display waas tfo auto-discovery blacklist ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x794161824}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21182_x6397_x1067470584}[模式：]{style="font-family:宋体"}

[**[display waas tfo auto-discovery blacklist]{lang="EN-US"}**[ { **ipv4** \| **ipv6** } \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x757783445}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_798921950}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x544789139}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1179219119}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x174828441}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_650141223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1042473913}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x2033960342}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1428896523}

[**[ipv4]{lang="EN-US"}**]{#struct_0_21182_x6397_383132438}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_21182_x6397_1767520724}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[黑名单信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_362173226}[：显示指定单板的黑名单信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的黑名单信息。（分布设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_1076499644}[：显示指定成员设备的黑名单信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示所有成员设备上的黑名单信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_21182_x6397_x1242817780}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的黑名单信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的黑名单信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21182_x6397_1676073819}[：显示指定成员设备上指定单板的黑名单信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示所有单板上的黑名单信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21182_x6397_1496689058}[：显示指定单板的黑名单信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟槽位号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示所有单板上的黑名单信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_721370867}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x1891987539}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[黑名单信息。]{style="font-family:宋体"}

[[\<Sysname\> display waas tfo auto-discovery blacklist ipv4]{lang="EN-US"}]{#struct_0_21182_x6397_1549664236}

[Server IP address/Port           Insert Time]{lang="EN-US"}

[1.1.1.1/8080                     Fri Mar 21 10:43:05 2014]{lang="EN-US"}

[1.1.1.2/8080                     Fri Mar 21 10:43:06 2014]{lang="EN-US"}

[2.2.2.2/443                      Fri Mar 21 10:20:37 2014]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total 3 entries found.]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display waas auto-discovery blacklist]{lang="EN-US"}]{#struct_0_21182_x6397_x1350340314}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x591303477}[[字段]{style="font-family:黑体"}]{#struct_0_21182_x6397_535181124}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1726505466}

[[Server IP address/Port]{lang="EN-US"}]{#struct_0_21182_x6397_1285220960}

[[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21182_x6397_x678070346}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Insert Time]{lang="EN-US"}]{#struct_0_21182_x6397_x1443102314}

[[黑名单表项的生成时间]{style="font-family:宋体"}]{#struct_0_21182_x6397_1246006797}

[[Total 3 entries found]{lang="EN-US"}]{#struct_0_21182_x6397_x451901397}

[[黑名单表项的总数]{style="font-family:宋体"}]{#struct_0_21182_x6397_301694556}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x44869293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset waas tfo auto-discovery blacklist]{lang="EN-US"}**]{#struct_0_21182_x6397_x16419705}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas tfo auto-discovery blacklist enable]{lang="EN-US"}**]{#struct_0_21182_x6397_833048827}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas tfo auto-discovery blacklist hold-time]{lang="EN-US"}**]{#struct_0_21182_x6397_77124371}

::: {#-794153034 .myid}
[]{#_Toc404787435}[]{#struct_0_21182_x6397_1376872761}

**WAAS \-- WAAS配置命令 \-- match tcp**

------------------------------------------------------------------------

[**[match tcp]{lang="EN-US"}**]{#struct_0_21182_x6397_713760059}[命令用来创建匹配流分类的规则。]{style="font-family:宋体"}

[**[undo match]{lang="EN-US"}**]{#struct_0_21182_x6397_x1252722074}[命令用来删除创建的匹配流分类规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x313457756}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **tcp** { **any** \| **destination** \| **source** } \[ **ip-address** *ip-address* \[ *mask-length* \| *mask* \] \| **ipv6-address** *ipv6-address* \[ *prefix-length* \] \] \[ **port** *port-list* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x2062203077}

[**[undo match]{lang="EN-US"}**[ *match-id*]{lang="EN-US"}]{#struct_0_21182_x6397_1998572421}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1222873390}

[[未创建匹配流分类的规则。]{style="font-family:宋体"}]{#struct_0_21182_x6397_1711655785}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_2061984443}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_935008362}[类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x922819382}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1238965079}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_971492592}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1582503646}

[*[match-id]{lang="EN-US"}*]{#struct_0_21182_x6397_x1469797080}[：指定匹配流分类规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，是]{style="font-family:宋体"}[match]{lang="EN-US"}[规则的唯一标识。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_21182_x6397_841813042}[：匹配]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文流量。]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_21182_x6397_1104486095}[：指定匹配规则的源或目的地址、端口号。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_21182_x6397_926157987}[：指定匹配规则的源地址、源端口号。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_21182_x6397_86851855}[：指定匹配规则的目的地址、目的端口号。]{style="font-family:宋体"}

[**[ip-address]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_21182_x6397_2097917828}[：指定匹配规则的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_21182_x6397_565821308}[：指定]{style="font-family:宋体"}[子网掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_21182_x6397_1569371781}[：指定子网掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv6-address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_21182_x6397_312199297}[：指定匹配规则的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_21182_x6397_1313608564}[：指定前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-list*]{lang="EN-US"}]{#struct_0_21182_x6397_240298421}[：指定匹配规则的端口号列表。表示方式为]{style="font-family:宋体"}*[port-list]{lang="EN-US"}*[ = { *port-number* \[ **to** *port-number* \] } &\<1-10\>]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[表示端口号，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[关键字指定端口号范围时，起始端口号必须小于或等于结束端口号。如果未指定本参数，则匹配所有端口号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_2124343435}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21182_x6397_x149453682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定匹配类型为源或目的时，需要至少指定]{style="font-family:宋体"}]{#struct_0_21182_x6397_2034408635}[IP]{lang="EN-US"}[地址、端口号两者中的一个。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定匹配类型为]{style="font-family:宋体"}]{#struct_0_21182_x6397_1146379709}[any]{lang="EN-US"}[时，如果指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号，则表示匹配源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号，或匹配目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许配置编号不同，但是内容完全相同的]{style="font-family:宋体"}]{#struct_0_21182_x6397_1749048684}[match]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_402843813}[类最多可创建]{style="font-family:宋体"}[65535]{lang="EN-US"}[条]{style="font-family:宋体"}[match]{lang="EN-US"}[规则，按照]{style="font-family:宋体"}[match]{lang="EN-US"}[规则的创建顺序进行匹配，匹配上其中任意一条，则认为匹配上了该类。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1031748552}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_1626515247}[创建类]{style="font-family:宋体"}[http_class]{lang="EN-US"}[的匹配规则：匹配源地址为]{style="font-family:宋体"}[192.168.0.1/16]{lang="EN-US"}[，源端口号为]{style="font-family:宋体"}[80]{lang="EN-US"}[和]{style="font-family:宋体"}[8000]{lang="EN-US"}[～]{style="font-family:宋体"}[8080]{lang="EN-US"}[的]{style="font-family:宋体"}[tcp]{lang="EN-US"}[流量。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_330618215}

[\[Sysname\] waas class http_class]{lang="EN-US"}

[\[Sysname-waasclass-http_class\] match tcp source ip-address 192.168.0.1 16 port 80 8000 to 8080]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_1060778520}[创建类]{style="font-family:宋体"}[http_class]{lang="EN-US"}[的匹配规则：匹配所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[流量。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x189682027}

[\[Sysname\] waas class http_class]{lang="EN-US"}

[\[Sysname-waasclass-http_class\] match tcp any]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1490461708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_x1401409522}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_256681135}
:::

::: {#-937897838 .myid}
[]{#_Toc404787436}[]{#struct_0_21182_x6397_65256056}

**WAAS \-- WAAS配置命令 \-- optimize**

------------------------------------------------------------------------

[**[optimize]{lang="EN-US"}**]{#struct_0_21182_x6397_1624622439}[命令用来配置]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类的优化方式。]{style="font-family:宋体"}

[**[undo optimize]{lang="EN-US"}**]{#struct_0_21182_x6397_1211833554}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1132164952}

[**[optimize tfo ]{lang="EN-US"}**[\[ **dre** \| **lz** \] \*]{lang="EN-US"}]{#struct_0_21182_x6397_388079535}

[**[undo optimize]{lang="EN-US"}**]{#struct_0_21182_x6397_947697183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_469491548}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x514482135}[类未配置任何优化方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1950869865}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_868504652}[策略类动作视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1800504782}

[[network-admin]{lang="FR"}]{#struct_0_21182_x6397_x327350902}

[[mdc-admin ]{lang="FR"}]{#struct_0_21182_x6397_x400097033}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1253355952}

[**[tfo]{lang="FR"}**]{#struct_0_21182_x6397_1954814353}**[：]{style="font-family:宋体"}**[流传输优化方式，仅支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[流传输优化。]{style="font-family:宋体"}

[**[dre]{lang="FR"}**]{#struct_0_21182_x6397_647909792}[：]{style="font-family:宋体"}[消除冗余数据优化方式。]{style="font-family:宋体"}

[**[lz]{lang="FR"}**]{#struct_0_21182_x6397_1743412875}[：]{style="font-family:宋体"}[数据压缩优化方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_900356634}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21182_x6397_x305761112}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令与]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1067963743}**[passthrough]{lang="EN-US"}**[命令二者只能选其一，如果同时配置了这两条命令，则后配置的生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令受优化控制功能状态的影响，如果用户配置了优化动作，而对应的优化控制功能处于关闭状态，则不能对匹配的报文流量进行相应的优化处理。]{style="font-family:宋体"}]{#struct_0_21182_x6397_1596718403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于匹配了黑名单的流量，通过]{style="font-family:宋体"}]{#struct_0_21182_x6397_x271993997}**[optimize]{lang="EN-US"}**[命令配置优化动作后，不会对指定流量进行优化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x605456504}

[[\# ]{lang="FR"}]{#struct_0_21182_x6397_x58402153}[配置]{style="font-family:宋体"}[WAAS]{lang="FR"}[类]{style="font-family:宋体"}[AFS]{lang="FR"}[的优化方式为]{style="font-family:
宋体"}[TFO]{lang="FR"}[、]{style="font-family:宋体"}[DRE]{lang="PT-BR"}[和]{style="font-family:宋体"}[LZ]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_21182_x6397_x707479389}

[\[Sysname\] waas policy waas_global]{lang="FR"}

[\[Sysname-waaspolicy-waas_global\] class AFS]{lang="FR"}

[\[Sysname-waaspolicy-waas_global-AFS\] optimize tfo dre lz]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_750193372}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[c]{lang="FR"}**]{#struct_0_21182_x6397_x1412589905}**[lass]{lang="FR"}**

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[display waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x2094918883}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[passthrough]{lang="EN-US"}**]{#struct_0_21182_x6397_1975605435}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[waas policy]{lang="FR"}**]{#struct_0_21182_x6397_1878495891}**[ ]{lang="FR"}**

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[waas tfo optimize dre]{lang="FR"}**]{#struct_0_21182_x6397_x1336765861}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[waas tfo optimize lz]{lang="FR"}**]{#struct_0_21182_x6397_1920998099}
:::

::: {#-334263399 .myid}
[]{#_Toc404787437}[]{#struct_0_21182_x6397_x167127142}

**WAAS \-- WAAS配置命令 \-- passthrough**

------------------------------------------------------------------------

[**[passthrough]{lang="EN-US"}**]{#struct_0_21182_x6397_x426749702}[命令用来配置]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类的直接旁路动作。]{style="font-family:宋体"}

[**[undo passthrough]{lang="EN-US"}**]{#struct_0_21182_x6397_1974409966}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x910152320}

[**[passthrough]{lang="EN-US"}**]{#struct_0_21182_x6397_1833167074}

[**[undo passthrough]{lang="EN-US"}**]{#struct_0_21182_x6397_x1879394514}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2093326033}

[[未配置直接旁路动作。]{style="font-family:宋体"}]{#struct_0_21182_x6397_x253349781}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1060184685}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x230939119}[策略类动作视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_301273910}

[[network-admin]{lang="FR"}]{#struct_0_21182_x6397_986983683}

[[mdc-admin ]{lang="FR"}]{#struct_0_21182_x6397_2012229119}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_987375776}

[[直接旁路动作就是对匹配]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_258644411}[类的报文流量不进行任何优化处理，直接转发。本命令与]{style="font-family:宋体"}**[optimize]{lang="EN-US"}**[命令二者只能选其一，如果同时配置了这两条命令，则后配置的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1603322401}

[[\# ]{lang="FR"}]{#struct_0_21182_x6397_x1011849805}[配置]{style="font-family:宋体"}[WAAS]{lang="PT-BR"}[类]{style="font-family:宋体"}[AFS]{lang="PT-BR"}[的优化方式为直接旁路]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_21182_x6397_1818731035}

[\[Sysname\] waas policy waas_global]{lang="FR"}

[\[Sysname-waaspolicy-waas_global\] class AFS]{lang="FR"}

[\[Sysname-waaspolicy-waas_global-AFS\] passthrough]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x71135188}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[class]{lang="FR"}**]{#struct_0_21182_x6397_927292856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_1255517986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[optimize]{lang="FR"}**]{#struct_0_21182_x6397_x126553031}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[waas policy]{lang="FR"}**]{#struct_0_21182_x6397_x652583159}**[ ]{lang="FR"}**
:::

::: {#81058526 .myid}
[]{#_Toc404787438}[]{#struct_0_21182_x6397_x1543793509}

**WAAS \-- WAAS配置命令 \-- reset waas cache dre**

------------------------------------------------------------------------

[**[reset waas cache dre]{lang="EN-US"}**]{#struct_0_21182_x6397_1222426552}[命令用来清除]{style="font-family:宋体"}[DRE]{lang="EN-US"}[的数据字典。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x287356383}

[**[reset waas cache dre ]{lang="EN-US"}**[\[ **peer** *peer-id* \]]{lang="EN-US"}]{#struct_0_21182_x6397_1884433863}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1216478639}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1838212549}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_821821079}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1087103239}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_671207157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x784895227}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x2000450442}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_252647094}

[**[peer ]{lang="EN-US"}***[peer-id]{lang="EN-US"}*]{#struct_0_21182_x6397_297281510}[：]{style="font-family:宋体"}[清除指定对端]{style="font-family:宋体"}[设备的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[数据字典，]{style="font-family:宋体"}*[peer-id]{lang="EN-US"}*[表示设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。如果未指定本参数，则清除设备上所有]{style="font-family:宋体"}[DRE]{lang="EN-US"}[的数据字典。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1893628593}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_998158104}[清除对端设备为]{style="font-family:宋体"}[0789-445d-effa]{lang="EN-US"}[的]{style="font-family:宋体"}[DER]{lang="EN-US"}[数据字典。]{style="font-family:宋体"}

[[\<Sysname\> reset waas cache dre peer 0789-445d-effa]{lang="EN-US"}]{#struct_0_21182_x6397_1532823950}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x503740238}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas statistics dre]{lang="EN-US"}**]{#struct_0_21182_x6397_x363138687}
:::

::: {#-1638107706 .myid}
[]{#_Toc404787439}[]{#struct_0_21182_x6397_x677938207}

**WAAS \-- WAAS配置命令 \-- reset waas statistics dre**

------------------------------------------------------------------------

[**[reset waas statistics dre]{lang="EN-US"}**]{#struct_0_21182_x6397_334847499}[命令用来清除]{style="font-family:
宋体"}[DRE]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1480223075}

[**[reset waas statistics dre ]{lang="EN-US"}**[\[ **peer** *peer-id* \]]{lang="EN-US"}]{#struct_0_21182_x6397_x1010236646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1821496124}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1268599336}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x118938901}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1877309402}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x1313436847}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1492178099}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x1462119511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1749620205}

[**[peer ]{lang="EN-US"}***[peer-id]{lang="EN-US"}*]{#struct_0_21182_x6397_x1870035496}[：]{style="font-family:宋体"}[清除指定对端]{style="font-family:宋体"}[设备的]{style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[peer-id]{lang="EN-US"}*[表示对端设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。如果未指定本参数，则清除设备上所有]{style="font-family:宋体"}[DRE]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1641973507}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x1924009155}[清除设备上所有]{style="font-family:宋体"}[DRE]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset waas statistics dre]{lang="EN-US"}]{#struct_0_21182_x6397_x342505468}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1556761760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas statistics dre]{lang="EN-US"}**]{#struct_0_21182_x6397_x1753740906}
:::

::: {#-86808993 .myid}
[]{#_Toc404787440}[]{#struct_0_21182_x6397_x557458111}

**WAAS \-- WAAS配置命令 \-- reset waas tfo auto-discovery blacklist**

------------------------------------------------------------------------

[**[reset waas tfo auto-discovery blacklist]{lang="EN-US"}**]{#struct_0_21182_x6397_x694249631}[命令用来清除所有的黑名单表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_725879822}

[**[reset waas tfo auto-discovery blacklist]{lang="EN-US"}**]{#struct_0_21182_x6397_1408151452}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1753507733}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1405830100}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1415446508}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1389555159}

[[network-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x2030715437}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1576633695}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21182_x6397_x201807512}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_884297654}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_2026021608}[清除所有的黑名单表项。]{style="font-family:宋体"}

[[\<Sysname\> reset waas tfo auto-discovery blacklist]{lang="EN-US"}]{#struct_0_21182_x6397_x448357382}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1209387502}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas tfo auto-discovery blacklist]{lang="EN-US"}**]{#struct_0_21182_x6397_x2026536482}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas tfo auto-discovery blacklist enable]{lang="EN-US"}**]{#struct_0_21182_x6397_49325780}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas tfo auto-discovery blacklist hold-time]{lang="EN-US"}**]{#struct_0_21182_x6397_706390422}
:::

::: {#241390138 .myid}
[]{#_Toc404787441}[]{#struct_0_21182_x6397_1599475101}[]{#_Toc185927308}[]{#_Toc123026768}

**WAAS \-- WAAS配置命令 \-- waas apply policy**

------------------------------------------------------------------------

[**[waas apply policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x2027440647}[命令用来在接口上应用]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo waas apply policy]{lang="EN-US"}**]{#struct_0_21182_x6397_118818215}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x150637433}

[**[waas apply policy ]{lang="EN-US"}**[\[ *policy-name* \]]{lang="EN-US"}]{#struct_0_21182_x6397_1589822091}

[**[undo waas apply policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x1754428100}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1624791008}

[[接口上未应用任何]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1990699033}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_532692725}

[[接口视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1563995447}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_666540463}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1326577717}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1279432923}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1257636658}

[*[policy-name]{lang="EN-US"}*]{#struct_0_21182_x6397_1299802408}[：指定]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，且该策略必须存在。如果不指定本参数，则在接口上应用预定义策略]{style="font-family:宋体"}[waas_default]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x867537297}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x2062397077}[设备应用策略的接口连接广域网，未应用策略的接口连接局域网。对从广域网侧发送或接收的报文流量会与广域网接口所引用的策略进行匹配。但如果指定流量经过设备的入接口和出接口都连接广域网或者局域网，则不对报文进行优化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1877430498}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x1716721374}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上应用]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略]{style="font-family:宋体"}[global_policy]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x568061671}

[\[Sysname\] interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-]{lang="EN-US"}[GigabitEthernet1/0/1]{lang="PT-BR"}[\] waas apply policy global_policy]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1108645113}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x559322450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas status]{lang="EN-US"}**]{#struct_0_21182_x6397_x39122676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x2116415821}
:::

::: {#-769685232 .myid}
[]{#_Toc404787442}[]{#struct_0_21182_x6397_792613282}

**WAAS \-- WAAS配置命令 \-- waas class**

------------------------------------------------------------------------

[**[waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_x100007053}[命令用来创建]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类，并进入]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类视图。]{style="font-family:宋体"}

[**[undo waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_x1158590902}[命令用来删除指定的]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x586051141}

[**[waas class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_21182_x6397_x1203324772}

[**[undo waas class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_21182_x6397_306292251}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1604662106}

[[只存在预定义类。]{style="font-family:宋体"}]{#struct_0_21182_x6397_750860913}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1486365363}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1012161981}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x906325917}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_2116630537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_158464229}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_509447682}

[*[class-name]{lang="EN-US"}*]{#struct_0_21182_x6397_x827182747}[：指定]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1050482169}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21182_x6397_x384491036}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的类不存在，创建该类并进入其视图，否则直接进入其视图。如果创建的]{style="font-family:宋体"}]{#struct_0_21182_x6397_603765126}[class]{lang="EN-US"}[未配置任何]{style="font-family:宋体"}[match]{lang="EN-US"}[规则，则该类不参与所属策略对报文流量的匹配。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议用户通过本命令进入]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1057324593}[WAAS]{lang="EN-US"}[预定义类视图，修改预定义类配置。（预定义类参见]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-7]{lang="EN-US"}](?-326408526#_Ref401328623)[）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2010160855}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x1255053674}[创建]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[类]{style="font-family:宋体"}[waas_global]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x1263772118}

[\[Sysname\] waas class waas_global]{lang="EN-US"}

[\[Sysname-waasclass-waas_global\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1135273249}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[class]{lang="EN-US"}**]{#struct_0_21182_x6397_392006140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas class]{lang="EN-US"}**]{#struct_0_21182_x6397_x1266382680}
:::

::: {#-1928861873 .myid}
[]{#_Toc404787443}[]{#struct_0_21182_x6397_941693984}

**WAAS \-- WAAS配置命令 \-- waas config remove-all**

------------------------------------------------------------------------

[**[waas config remove-all]{lang="EN-US"}**]{#struct_0_21182_x6397_1664046167}[命令用来删除]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_255987571}

[**[waas config]{lang="EN-US"}**[ **remove-all**]{lang="EN-US"}]{#struct_0_21182_x6397_x1588801505}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2142893024}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x86428995}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1453985696}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1078793069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x271865529}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1337286870}

[[通过本命令删除]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_2060266536}[特性的所有配置数据和运行数据，并使]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[进程退出。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x638123350}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_1843943077}[删除]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[所有配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_1462500675}

[\[Sysname\] waas config remove-all]{lang="EN-US"}

[The command will clear all the WAAS configuration. Continue? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#1957174718 .myid}
[]{#_Toc404787444}[]{#struct_0_21182_x6397_x1792781532}

**WAAS \-- WAAS配置命令 \-- waas config restore-default**

------------------------------------------------------------------------

[**[waas config restore-default]{lang="EN-US"}**]{#struct_0_21182_x6397_x960463865}[命令用来还原]{style="font-family:
宋体"}[WAAS]{lang="EN-US"}[的预定义配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1251573531}

[**[waas config restore-default]{lang="EN-US"}**]{#struct_0_21182_x6397_x1871198564}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_591093831}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x932931597}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x118854042}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x34101879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1246278969}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_709224690}

[[还原]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1245849627}[的预定义配置是把]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[预定义策略和预定义类的配置还原到]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[进程第一次启动时的配置，不修改用户自定义的配置。]{style="font-family:宋体"}

[[需要注意的是，配置本命令时，需保证所有接口未应用任何策略，否则恢复失败。]{style="font-family:宋体"}]{#struct_0_21182_x6397_x4957117}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_300733136}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_1044483996}[还原]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[预定义配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x910086784}

[\[Sysname\] waas config restore-default]{lang="EN-US"}

[The command will restore all the WAAS configuration to default. Continue? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#-326408526 .myid}
[]{#_Toc404787445}[]{#struct_0_21182_x6397_x878789913}[]{#_Toc382816935}

**WAAS \-- WAAS配置命令 \-- waas policy**

------------------------------------------------------------------------

[**[waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_x1686574800}[命令用来创建]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略，并进入]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[**[undo waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_1693226556}[命令用来删除指定的]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x765902295}

[**[waas policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_21182_x6397_834079461}

[**[undo waas policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_21182_x6397_x662861073}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1188796001}

[[只存在预定义策略]{style="font-family:宋体"}[waas_default]{lang="EN-US"}]{#struct_0_21182_x6397_44523591}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_16860399}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1283864440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1708804314}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_204666190}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x1079661518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1613136210}

[*[policy-name]{lang="EN-US"}*]{#struct_0_21182_x6397_1818796571}[：指定]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1120923137}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21182_x6397_902074505}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的策略不存在，创建该策略并进入其视图，否则直接进入其视图。]{style="font-family:宋体"}]{#struct_0_21182_x6397_x436276293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除指定策略时，如果该策略应用于接口，则应先取消策略在接口上的应用再删除，否则删除失败。]{style="font-family:宋体"}]{#struct_0_21182_x6397_215808178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议用户通过此命令进入预定义策略的视图，采用修改预定义策略的方式完成策略配置。预定义策略是]{style="font-family:宋体"}]{#struct_0_21182_x6397_x172186643}[WAAS]{lang="EN-US"}[进程在第一次启动时系统创建的策略，策略名称为]{style="font-family:宋体"}[waas_default]{lang="EN-US"}[，默认引用所有的预定义类。]{style="font-family:宋体"}

[]{#struct_0_21182_x6397_x1236746854}[[表1-7 ]{lang="EN-US"}[预定义策略]{style="font-family:
黑体"}]{#_Ref401328623}

[]{#table_struct_0_x587429837}[[预定义类]{style="font-family:黑体"}]{#struct_0_21182_x6397_1852923923}
:::

[[优化方式]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2129541609}

[[源端口号]{style="font-family:黑体"}]{#struct_0_21182_x6397_1677367100}

[[目的端口号]{style="font-family:黑体"}]{#struct_0_21182_x6397_x495485904}

[[Kerberos]{lang="EN-US"}]{#struct_0_21182_x6397_51676150}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_545557144}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_252712630}

[[88]{lang="EN-US"}]{#struct_0_21182_x6397_676675015}[、]{style="font-family:宋体"}[464]{lang="EN-US"}[、]{style="font-family:宋体"}[543]{lang="EN-US"}[、]{style="font-family:宋体"}[544]{lang="EN-US"}[、]{style="font-family:宋体"}[749]{lang="EN-US"}[、]{style="font-family:宋体"}[754]{lang="EN-US"}[、]{style="font-family:宋体"}[888]{lang="EN-US"}[、]{style="font-family:宋体"}[2053]{lang="EN-US"}

[[SASL]{lang="EN-US"}]{#struct_0_21182_x6397_1097610556}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1794594918}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2060659316}

[[3659]{lang="EN-US"}]{#struct_0_21182_x6397_x1368713391}

[[TACACS]{lang="EN-US"}]{#struct_0_21182_x6397_x839336348}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_40499456}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_693556636}

[[49]{lang="EN-US"}]{#struct_0_21182_x6397_x1313371311}

[[Amanda]{lang="EN-US"}]{#struct_0_21182_x6397_x248033350}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x621700150}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1484325245}

[[10080]{lang="EN-US"}]{#struct_0_21182_x6397_x1663582568}

[[BackupExpress]{lang="EN-US"}]{#struct_0_21182_x6397_2110563316}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1390568715}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1972389686}

[[6123]{lang="EN-US"}]{#struct_0_21182_x6397_1415512044}

[[CommVault]{lang="EN-US"}]{#struct_0_21182_x6397_628038472}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_1067854776}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x975428299}

[[8400-8403]{lang="EN-US"}]{#struct_0_21182_x6397_1547787694}

[[Connected-DataProtector]{lang="EN-US"}]{#struct_0_21182_x6397_x1948386188}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x221344935}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2094125426}

[[16384]{lang="EN-US"}]{#struct_0_21182_x6397_x150571897}

[[IBM-TSM]{lang="EN-US"}]{#struct_0_21182_x6397_9666008}

[[TFO+LZ+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1946902497}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1951473899}

[[1500-1502]{lang="EN-US"}]{#struct_0_21182_x6397_x77987532}

[[Legato-NetWorker]{lang="EN-US"}]{#struct_0_21182_x6397_x918921003}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1716655838}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_357592435}

[[7937]{lang="EN-US"}]{#struct_0_21182_x6397_1106312676}[、]{style="font-family:宋体"}[7938]{lang="EN-US"}[、]{style="font-family:宋体"}[, 7939]{lang="EN-US"}

[[Legato-RepliStor]{lang="EN-US"}]{#struct_0_21182_x6397_26360534}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_63011224}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2102187503}

[[7144]{lang="EN-US"}]{#struct_0_21182_x6397_1012227517}[、]{style="font-family:宋体"}[7145]{lang="EN-US"}

[[Veritas-BackupExec]{lang="EN-US"}]{#struct_0_21182_x6397_1030191617}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_875864162}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1364576730}

[[1125]{lang="EN-US"}]{#struct_0_21182_x6397_703008458}[、]{style="font-family:宋体"}[3527]{lang="EN-US"}[、]{style="font-family:宋体"}[6101]{lang="EN-US"}[、]{style="font-family:宋体"}[6102]{lang="EN-US"}[、]{style="font-family:宋体"}[6106]{lang="EN-US"}

[[Veritas-NetBackup]{lang="EN-US"}]{#struct_0_21182_x6397_x295884495}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1266317144}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2133122228}

[[13720]{lang="EN-US"}]{#struct_0_21182_x6397_1020541873}[、]{style="font-family:宋体"}[13721]{lang="EN-US"}[、]{style="font-family:宋体"}[13782]{lang="EN-US"}[、]{style="font-family:宋体"}[13785]{lang="EN-US"}

[[PDMWorks]{lang="EN-US"}]{#struct_0_21182_x6397_362915795}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1693890206}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x758622300}

[[30000]{lang="EN-US"}]{#struct_0_21182_x6397_1462566211}[、]{style="font-family:宋体"}[40000]{lang="EN-US"}

[[Cisco-CallManager]{lang="EN-US"}]{#struct_0_21182_x6397_x1830089012}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1835189685}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1083065649}

[[2443]{lang="EN-US"}]{#struct_0_21182_x6397_x910021248}[、]{style="font-family:宋体"}[2748]{lang="EN-US"}

[[SIP-secure]{lang="EN-US"}]{#struct_0_21182_x6397_x2062197478}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x855516093}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1472973103}

[[5061]{lang="EN-US"}]{#struct_0_21182_x6397_x190209173}

[[VoIP-Control]{lang="EN-US"}]{#struct_0_21182_x6397_1818862107}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x474801433}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1802793367}

[[1300]{lang="EN-US"}]{#struct_0_21182_x6397_x214665486}[、]{style="font-family:宋体"}[1718-1720, 2000-2002,2428, 5060,11000-11999]{lang="EN-US"}

[[CU-SeeMe]{lang="EN-US"}]{#struct_0_21182_x6397_1507995832}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_252778166}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1825741792}

[[7640]{lang="EN-US"}]{#struct_0_21182_x6397_x1777162221}[、]{style="font-family:宋体"}[7642]{lang="EN-US"}[、]{style="font-family:宋体"}[7648]{lang="EN-US"}[、]{style="font-family:宋体"}[7649]{lang="EN-US"}

[[ezMeeting]{lang="EN-US"}]{#struct_0_21182_x6397_2051915127}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x2122395586}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1313305775}

[[10101-10103]{lang="EN-US"}]{#struct_0_21182_x6397_502725777}[、]{style="font-family:宋体"}[26260-26261]{lang="EN-US"}

[[GnomeMeeting]{lang="EN-US"}]{#struct_0_21182_x6397_x1169641860}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1828045790}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1415577580}

[[30000-30010]{lang="EN-US"}]{#struct_0_21182_x6397_x1345160923}

[[Intel-Proshare]{lang="EN-US"}]{#struct_0_21182_x6397_1309094205}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x150506361}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1547946294}

[[5713-5717]{lang="EN-US"}]{#struct_0_21182_x6397_983159399}

[[MS-NetMeeting]{lang="EN-US"}]{#struct_0_21182_x6397_639149876}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1716590302}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_564644166}

[[522]{lang="EN-US"}]{#struct_0_21182_x6397_x1148540938}[、]{style="font-family:宋体"}[1503]{lang="EN-US"}[、]{style="font-family:宋体"}[1731]{lang="EN-US"}

[[VocalTec]{lang="EN-US"}]{#struct_0_21182_x6397_1012293053}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1410443161}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1071405362}

[[1490]{lang="EN-US"}]{#struct_0_21182_x6397_x1606604428}[、]{style="font-family:宋体"}[6670]{lang="EN-US"}[、]{style="font-family:宋体"}[22555]{lang="EN-US"}[、]{style="font-family:宋体"}[25793]{lang="EN-US"}

[[SSL-Shell]{lang="EN-US"}]{#struct_0_21182_x6397_x1266251608}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1566561743}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_848414655}

[[614]{lang="EN-US"}]{#struct_0_21182_x6397_x2059437485}

[[Telnet]{lang="EN-US"}]{#struct_0_21182_x6397_1462631747}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1026570207}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x95482431}

[[23]{lang="EN-US"}]{#struct_0_21182_x6397_653271200}[、]{style="font-family:宋体"}[107]{lang="EN-US"}[、]{style="font-family:宋体"}[513]{lang="EN-US"}

[[Telnets]{lang="EN-US"}]{#struct_0_21182_x6397_x909955712}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x40224561}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x180471866}

[[992]{lang="EN-US"}]{#struct_0_21182_x6397_1818927643}

[[Unix-Remote-Execution]{lang="EN-US"}]{#struct_0_21182_x6397_x61966179}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1370644044}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1893009197}

[[512]{lang="EN-US"}]{#struct_0_21182_x6397_252843702}[、]{style="font-family:宋体"}[514]{lang="EN-US"}

[[Documentum]{lang="EN-US"}]{#struct_0_21182_x6397_1643492165}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_289561113}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_65525714}

[[1489]{lang="EN-US"}]{#struct_0_21182_x6397_x1313240239}

[[Filenet]{lang="EN-US"}]{#struct_0_21182_x6397_x1564954868}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_773905646}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1415643116}

[[32768-32774]{lang="EN-US"}]{#struct_0_21182_x6397_x133978351}

[[ProjectWise-FileTransfer]{lang="EN-US"}]{#struct_0_21182_x6397_x1057323059}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1880693966}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x150440825}

[[5800]{lang="EN-US"}]{#struct_0_21182_x6397_x1554124149}

[[LDAP]{lang="EN-US"}]{#struct_0_21182_x6397_x1773006901}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1716524766}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1333188633}

[[389]{lang="EN-US"}]{#struct_0_21182_x6397_x1165423278}[、]{style="font-family:宋体"}[8404]{lang="EN-US"}

[[LDAP-Global-Catalog]{lang="EN-US"}]{#struct_0_21182_x6397_1012358589}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1349604840}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1072712111}

[[3268]{lang="EN-US"}]{#struct_0_21182_x6397_x1266186072}

[[LDAP-Global-Catalog-Secure]{lang="EN-US"}]{#struct_0_21182_x6397_1565459796}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_615588627}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1462697283}

[[3269]{lang="EN-US"}]{#struct_0_21182_x6397_875398095}

[[LDAP-secure]{lang="EN-US"}]{#struct_0_21182_x6397_1048788933}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x909890176}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x393285149}

[[636]{lang="EN-US"}]{#struct_0_21182_x6397_1253344080}

[[HP-OpenMail]{lang="EN-US"}]{#struct_0_21182_x6397_1818993179}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1125557808}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_304266914}

[[5729]{lang="EN-US"}]{#struct_0_21182_x6397_252909238}[、]{style="font-family:宋体"}[5755]{lang="EN-US"}[、]{style="font-family:宋体"}[5757]{lang="EN-US"}[、]{style="font-family:宋体"}[5766, 5767]{lang="EN-US"}[、]{style="font-family:宋体"}[5768]{lang="EN-US"}

[[Internet-Mail]{lang="EN-US"}]{#struct_0_21182_x6397_46272668}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_711080524}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1313174703}

[[25]{lang="EN-US"}]{#struct_0_21182_x6397_1312176372}[、]{style="font-family:宋体"}[110]{lang="EN-US"}[、]{style="font-family:宋体"}[143]{lang="EN-US"}[、]{style="font-family:宋体"}[220]{lang="EN-US"}

[[Internet-Mail-secure]{lang="EN-US"}]{#struct_0_21182_x6397_260697663}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_1415708652}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x999249503}

[[465]{lang="EN-US"}]{#struct_0_21182_x6397_x411235312}[、]{style="font-family:宋体"}[993]{lang="EN-US"}[、]{style="font-family:宋体"}[995]{lang="EN-US"}

[[Lotus-Notes]{lang="EN-US"}]{#struct_0_21182_x6397_x150375289}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1168004311}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1716459230}

[[1352]{lang="EN-US"}]{#struct_0_21182_x6397_1244795457}

[[MDaemon]{lang="EN-US"}]{#struct_0_21182_x6397_431547817}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1012424125}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1391449871}

[[3000]{lang="EN-US"}]{#struct_0_21182_x6397_x861520205}[、]{style="font-family:宋体"}[3001]{lang="EN-US"}

[[NNTP]{lang="EN-US"}]{#struct_0_21182_x6397_x1266120536}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1059251371}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1462762819}

[[119]{lang="EN-US"}]{#struct_0_21182_x6397_x1772929886}

[[NNTP-secure]{lang="EN-US"}]{#struct_0_21182_x6397_655334293}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x909824640}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x421739442}

[[563]{lang="EN-US"}]{#struct_0_21182_x6397_1984699114}

[[Novell-Groupwise]{lang="EN-US"}]{#struct_0_21182_x6397_1819058715}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1072671228}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_252974774}

[[1099]{lang="EN-US"}]{#struct_0_21182_x6397_x287001944}[、]{style="font-family:宋体"}[1677]{lang="EN-US"}[、]{style="font-family:宋体"}[2800]{lang="EN-US"}[、]{style="font-family:宋体"}[3800, 7100]{lang="EN-US"}[、]{style="font-family:宋体"}[7101]{lang="EN-US"}[、]{style="font-family:宋体"}[7180]{lang="EN-US"}[、]{style="font-family:宋体"}[7181]{lang="EN-US"}[、]{style="font-family:宋体"}[7205]{lang="EN-US"}[、]{style="font-family:宋体"}[9850]{lang="EN-US"}

[[PCMail-Server]{lang="EN-US"}]{#struct_0_21182_x6397_1078245533}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1313109167}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2097879615}

[[158]{lang="EN-US"}]{#struct_0_21182_x6397_1415774188}

[[QMTP]{lang="EN-US"}]{#struct_0_21182_x6397_1781323560}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_613221115}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x150309753}

[[209]{lang="EN-US"}]{#struct_0_21182_x6397_x1197006230}

[[X400]{lang="EN-US"}]{#struct_0_21182_x6397_x1716393694}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x363428627}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1012489661}

[[102]{lang="EN-US"}]{#struct_0_21182_x6397_x1746062116}

[[SAP]{lang="EN-US"}]{#struct_0_21182_x6397_x1423202615}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1266055000}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_670445813}

[[3200-3219]{lang="EN-US"}]{#struct_0_21182_x6397_1462828355}[、]{style="font-family:宋体"}[3221-3224]{lang="EN-US"}[、]{style="font-family:宋体"}[3226-3267]{lang="EN-US"}[、]{style="font-family:宋体"}[3270-3282]{lang="EN-US"}[、]{style="font-family:宋体"}[3284-3305]{lang="EN-US"}[、]{style="font-family:宋体"}[3307-3388]{lang="EN-US"}[、]{style="font-family:宋体"}[3390-3399]{lang="EN-US"}[、]{style="font-family:宋体"}[3600-3659]{lang="EN-US"}[、]{style="font-family:宋体"}[3662-3699]{lang="EN-US"}

[[Siebel]{lang="EN-US"}]{#struct_0_21182_x6397_949988847}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x223620502}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1579602560}

[[2320]{lang="EN-US"}]{#struct_0_21182_x6397_2082093463}[、]{style="font-family:宋体"}[2321]{lang="EN-US"}[、]{style="font-family:宋体"}[8448]{lang="EN-US"}

[[AFS]{lang="EN-US"}]{#struct_0_21182_x6397_1149280795}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1872411633}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x902032232}

[[7000-7009]{lang="EN-US"}]{#struct_0_21182_x6397_x416803146}

[[Apple-AFP]{lang="EN-US"}]{#struct_0_21182_x6397_x277056180}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1982887087}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1905418667}

[[548]{lang="EN-US"}]{#struct_0_21182_x6397_745996268}

[[CIFS-non-wafs]{lang="EN-US"}]{#struct_0_21182_x6397_549856054}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x820087673}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_103844822}

[[139]{lang="EN-US"}]{#struct_0_21182_x6397_1839708529}[、]{style="font-family:宋体"}[445]{lang="EN-US"}

[[NFS]{lang="EN-US"}]{#struct_0_21182_x6397_1908795682}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_773614216}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_342711741}

[[2049]{lang="EN-US"}]{#struct_0_21182_x6397_1274525349}

[[Novell-NetWare]{lang="EN-US"}]{#struct_0_21182_x6397_x1935832920}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_538044175}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1287314320}

[[524]{lang="EN-US"}]{#struct_0_21182_x6397_793050435}

[[Sun-RPC]{lang="EN-US"}]{#struct_0_21182_x6397_x1579537024}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x250406187}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1149346331}

[[111]{lang="EN-US"}]{#struct_0_21182_x6397_x292779942}

[[BFTP]{lang="EN-US"}]{#struct_0_21182_x6397_x416737610}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_850937692}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1982821551}

[[152]{lang="EN-US"}]{#struct_0_21182_x6397_x67532332}

[[FTP]{lang="EN-US"}]{#struct_0_21182_x6397_746061804}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x2035116988}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x820022137}

[[21]{lang="EN-US"}]{#struct_0_21182_x6397_x1129846357}

[[FTP-Data]{lang="EN-US"}]{#struct_0_21182_x6397_1908861218}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x810576004}

[[20]{lang="EN-US"}]{#struct_0_21182_x6397_342777277}

[ ]{lang="EN-US" style="font-size:10.5pt"}

[[FTPS]{lang="EN-US"}]{#struct_0_21182_x6397_x1845422918}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1935767384}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1106611016}

[[990]{lang="EN-US"}]{#struct_0_21182_x6397_793115971}

[[FTPS-Data]{lang="EN-US"}]{#struct_0_21182_x6397_739519412}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1579471488}

[[989]{lang="EN-US"}]{#struct_0_21182_x6397_1843252561}

[ ]{lang="EN-US" style="font-size:10.5pt"}

[[Simple-FTP]{lang="EN-US"}]{#struct_0_21182_x6397_1149411867}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_822786027}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x416672074}

[[115]{lang="EN-US"}]{#struct_0_21182_x6397_116124074}

[[TFTP]{lang="EN-US"}]{#struct_0_21182_x6397_x1982756015}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1353113814}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_746127340}

[[69]{lang="EN-US"}]{#struct_0_21182_x6397_x2058512427}

[[TFTPS]{lang="EN-US"}]{#struct_0_21182_x6397_x819956601}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x77349832}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1908926754}

[[3713]{lang="EN-US"}]{#struct_0_21182_x6397_x794817538}

[[AOL]{lang="EN-US"}]{#struct_0_21182_x6397_342842813}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1319382857}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1935701848}

[[5190-5193]{lang="EN-US"}]{#struct_0_21182_x6397_793181507}

[[Apple-iChat]{lang="EN-US"}]{#struct_0_21182_x6397_787330455}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1579405952}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1316049005}

[[5297]{lang="EN-US"}]{#struct_0_21182_x6397_1149477403}[、]{style="font-family:宋体"}[5298]{lang="EN-US"}

[[IRC]{lang="EN-US"}]{#struct_0_21182_x6397_x669516725}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x416606538}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1248050194}

[[531]{lang="EN-US"}]{#struct_0_21182_x6397_x1982690479}[、]{style="font-family:宋体"}[6660-6669]{lang="EN-US"}

[[Jabber]{lang="EN-US"}]{#struct_0_21182_x6397_746192876}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_316380757}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x819891065}

[[5222]{lang="EN-US"}]{#struct_0_21182_x6397_733961860}[、]{style="font-family:宋体"}[5269]{lang="EN-US"}

[[Lotus-Sametime-Connect]{lang="EN-US"}]{#struct_0_21182_x6397_1908992290}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x384157290}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_342908349}

[[1533]{lang="EN-US"}]{#struct_0_21182_x6397_x1935636312}

[[MS-Chat]{lang="EN-US"}]{#struct_0_21182_x6397_x1147142705}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_793247043}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_261618350}

[[6665]{lang="EN-US"}]{#struct_0_21182_x6397_x1579340416}[、]{style="font-family:宋体"}[6667]{lang="EN-US"}

[[MSN-Messenger]{lang="EN-US"}]{#struct_0_21182_x6397_x1107599864}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1149542939}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1114613252}

[[1863]{lang="EN-US"}]{#struct_0_21182_x6397_x416541002}[、]{style="font-family:宋体"}[6891-6900]{lang="EN-US"}

[[Yahoo-Messenger]{lang="EN-US"}]{#struct_0_21182_x6397_x1443996189}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1982624943}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_746258412}

[[5000]{lang="EN-US"}]{#struct_0_21182_x6397_x1061286895}[、]{style="font-family:宋体"}[5001]{lang="EN-US"}[、]{style="font-family:宋体"}[5050]{lang="EN-US"}[、]{style="font-family:宋体"}[5100]{lang="EN-US"}

[[DNS]{lang="EN-US"}]{#struct_0_21182_x6397_x819825529}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x71094028}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1909057826}

[[53]{lang="EN-US"}]{#struct_0_21182_x6397_x1247903299}

[[iSNS]{lang="EN-US"}]{#struct_0_21182_x6397_342973885}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1935570776}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_514411347}

[[3205]{lang="EN-US"}]{#struct_0_21182_x6397_793312579}

[[Service-Location]{lang="EN-US"}]{#struct_0_21182_x6397_x894716808}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1579274880}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1149608475}

[[427]{lang="EN-US"}]{#struct_0_21182_x6397_457435237}

[[WINS]{lang="EN-US"}]{#struct_0_21182_x6397_x416475466}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1640181876}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1982559407}

[[42]{lang="EN-US"}]{#struct_0_21182_x6397_746323948}[、]{style="font-family:宋体"}[137]{lang="EN-US"}[、]{style="font-family:宋体"}[1512]{lang="EN-US"}

[[Cisco-NetFlow]{lang="EN-US"}]{#struct_0_21182_x6397_x1789064753}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x819759993}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_255329030}

[[7544]{lang="EN-US"}]{#struct_0_21182_x6397_1909123362}[、]{style="font-family:宋体"}[7545]{lang="EN-US"}

[[Basic-TCP-services]{lang="EN-US"}]{#struct_0_21182_x6397_343039421}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1759459789}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1935505240}

[[1-19]{lang="EN-US"}]{#struct_0_21182_x6397_x1997855307}

[[BGP]{lang="EN-US"}]{#struct_0_21182_x6397_793378115}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1713492608}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1822250682}

[[179]{lang="EN-US"}]{#struct_0_21182_x6397_1015390747}

[[MS-Message-Queuing]{lang="EN-US"}]{#struct_0_21182_x6397_x550693194}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1876257534}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2116777135}

[[1801]{lang="EN-US"}]{#struct_0_21182_x6397_x2080731357}[、]{style="font-family:宋体"}[2101]{lang="EN-US"}[、]{style="font-family:宋体"}[2103]{lang="EN-US"}[、]{style="font-family:宋体"}[2105]{lang="EN-US"}

[[NTP]{lang="EN-US"}]{#struct_0_21182_x6397_612106220}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x953977721}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1947386543}

[[123]{lang="EN-US"}]{#struct_0_21182_x6397_1774905634}

[[Other-Secure]{lang="EN-US"}]{#struct_0_21182_x6397_208821693}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x149924892}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2069722968}

[[261]{lang="EN-US"}]{#struct_0_21182_x6397_659160387}[、]{style="font-family:宋体"}[44,]{lang="EN-US"}[、]{style="font-family:宋体"}[684]{lang="EN-US"}[、]{style="font-family:宋体"}[695]{lang="EN-US"}[、]{style="font-family:宋体"}[994]{lang="EN-US"}[、]{style="font-family:宋体"}[2252]{lang="EN-US"}[、]{style="font-family:宋体"}[2478]{lang="EN-US"}[、]{style="font-family:宋体"}[2479]{lang="EN-US"}[、]{style="font-family:宋体"}[2482]{lang="EN-US"}[、]{style="font-family:宋体"}[2484]{lang="EN-US"}[、]{style="font-family:宋体"}[2679]{lang="EN-US"}[、]{style="font-family:宋体"}[2762]{lang="EN-US"}[、]{style="font-family:宋体"}[2998]{lang="EN-US"}[、]{style="font-family:宋体"}[3077]{lang="EN-US"}[、]{style="font-family:宋体"}[3078]{lang="EN-US"}[、]{style="font-family:宋体"}[3183]{lang="EN-US"}[、]{style="font-family:宋体"}[3191]{lang="EN-US"}[、]{style="font-family:宋体"}[3220]{lang="EN-US"}[、]{style="font-family:宋体"}[3410]{lang="EN-US"}[、]{style="font-family:宋体"}[3424]{lang="EN-US"}[、]{style="font-family:宋体"}[3471]{lang="EN-US"}[、]{style="font-family:宋体"}[3496,3509]{lang="EN-US"}[、]{style="font-family:宋体"}[3529]{lang="EN-US"}[、]{style="font-family:宋体"}[3539]{lang="EN-US"}[、]{style="font-family:宋体"}[3660]{lang="EN-US"}[、]{style="font-family:宋体"}[3661]{lang="EN-US"}[、]{style="font-family:宋体"}[3747]{lang="EN-US"}[、]{style="font-family:宋体"}[3864]{lang="EN-US"}[、]{style="font-family:宋体"}[3885]{lang="EN-US"}[、]{style="font-family:宋体"}[3896]{lang="EN-US"}[、]{style="font-family:宋体"}[3897]{lang="EN-US"}[、]{style="font-family:宋体"}[3995]{lang="EN-US"}[、]{style="font-family:宋体"}[4031]{lang="EN-US"}[、]{style="font-family:宋体"}[5007]{lang="EN-US"}[、]{style="font-family:宋体"}[5989]{lang="EN-US"}[、]{style="font-family:宋体"}[5990]{lang="EN-US"}[、]{style="font-family:宋体"}[7674]{lang="EN-US"}[、]{style="font-family:宋体"}[9802]{lang="EN-US"}[、]{style="font-family:宋体"}[12109]{lang="EN-US"}

[[SOAP]{lang="EN-US"}]{#struct_0_21182_x6397_x1822696403}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1713427072}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1015456283}

[[7627]{lang="EN-US"}]{#struct_0_21182_x6397_x682234401}

[[Symantec-AntiVirus]{lang="EN-US"}]{#struct_0_21182_x6397_x550627658}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x2116711599}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_614987381}

[[2847]{lang="EN-US"}]{#struct_0_21182_x6397_612171756}[、]{style="font-family:宋体"}[2848]{lang="EN-US"}[、]{style="font-family:宋体"}[2967]{lang="EN-US"}[、]{style="font-family:宋体"}[2968, 38037, 38292]{lang="EN-US"}

[[BitTorrent]{lang="EN-US"}]{#struct_0_21182_x6397_x953912185}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1967912512}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1774971170}

[[6881]{lang="EN-US"}]{#struct_0_21182_x6397_x598360247}[--]{style="font-family:宋体"}[6889, 6969]{lang="EN-US"}

[[eDonkey]{lang="EN-US"}]{#struct_0_21182_x6397_208887229}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x2069657432}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_659225923}

[[4661]{lang="EN-US"}]{#struct_0_21182_x6397_385818995}[、]{style="font-family:宋体"}[4662]{lang="EN-US"}

[[Gnutella]{lang="EN-US"}]{#struct_0_21182_x6397_x1713361536}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1015521819}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2109902824}

[[6346]{lang="EN-US"}]{#struct_0_21182_x6397_x550562122}[--]{style="font-family:宋体"}[6349]{lang="EN-US"}[、]{style="font-family:宋体"}[6355]{lang="EN-US"}[、]{style="font-family:宋体"}[5634]{lang="EN-US"}

[[Grouper]{lang="EN-US"}]{#struct_0_21182_x6397_x2116646063}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1134056129}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_612237292}

[[8038]{lang="EN-US"}]{#struct_0_21182_x6397_x953846649}

[[HotLine]{lang="EN-US"}]{#struct_0_21182_x6397_1775036706}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1415384920}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_208952765}

[[5500]{lang="EN-US"}]{#struct_0_21182_x6397_x2069591896}[--]{style="font-family:宋体"}[5503]{lang="EN-US"}

[[Kazaa]{lang="EN-US"}]{#struct_0_21182_x6397_659291459}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1610412493}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1713296000}

[[1214]{lang="EN-US"}]{#struct_0_21182_x6397_1015587355}

[[Laplink-ShareDirect]{lang="EN-US"}]{#struct_0_21182_x6397_x1461421798}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x550496586}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2116580527}

[[2705]{lang="EN-US"}]{#struct_0_21182_x6397_612302828}

[[Napster]{lang="EN-US"}]{#struct_0_21182_x6397_x10699973}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x953781113}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1775102242}

[[6666]{lang="EN-US"}]{#struct_0_21182_x6397_2138381857}[、]{style="font-family:宋体"}[6677]{lang="EN-US"}[、]{style="font-family:宋体"}[6700]{lang="EN-US"}[、]{style="font-family:宋体"}[6688, 7777]{lang="EN-US"}[、]{style="font-family:宋体"}[8875]{lang="EN-US"}

[[Qnext]{lang="EN-US"}]{#struct_0_21182_x6397_209018301}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x2069526360}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_659356995}

[[44]{lang="EN-US"}]{#struct_0_21182_x6397_1220944108}[、]{style="font-family:宋体"}[5555]{lang="EN-US"}

[[SoulSeek]{lang="EN-US"}]{#struct_0_21182_x6397_x1713230464}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1015652891}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x550431050}

[[2234]{lang="EN-US"}]{#struct_0_21182_x6397_1262648818}[、]{style="font-family:宋体"}[5534]{lang="EN-US"}

[[WASTE]{lang="EN-US"}]{#struct_0_21182_x6397_x2116514991}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_612368364}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x27167998}

[[1337]{lang="EN-US"}]{#struct_0_21182_x6397_x953715577}

[[WinMX]{lang="EN-US"}]{#struct_0_21182_x6397_1775167778}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_209083837}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_612542035}

[[6699]{lang="EN-US"}]{#struct_0_21182_x6397_x2069460824}

[[AppSocket]{lang="EN-US"}]{#struct_0_21182_x6397_659422531}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1713164928}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1935499730}

[[9100]{lang="EN-US"}]{#struct_0_21182_x6397_1015718427}

[[IPP]{lang="EN-US"}]{#struct_0_21182_x6397_x550365514}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x2116449455}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1260457575}

[[631]{lang="EN-US"}]{#struct_0_21182_x6397_612433900}

[[SUN-Xprint]{lang="EN-US"}]{#struct_0_21182_x6397_x953650041}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1775233314}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_209149373}

[[8100]{lang="EN-US"}]{#struct_0_21182_x6397_1760751330}

[[Unix-Printing]{lang="EN-US"}]{#struct_0_21182_x6397_x2069395288}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_659488067}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1311822464}

[[170, 515]{lang="EN-US"}]{#struct_0_21182_x6397_1417060891}

[[Altiris-CarbonCopy]{lang="EN-US"}]{#struct_0_21182_x6397_x700971748}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x149023050}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1715106991}

[[1680]{lang="EN-US"}]{#struct_0_21182_x6397_1013776364}

[[Apple-NetAssistant]{lang="EN-US"}]{#struct_0_21182_x6397_x552307577}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x2118391518}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1511285106}

[[3283]{lang="EN-US"}]{#struct_0_21182_x6397_610491837}

[[Citrix-ICA]{lang="EN-US"}]{#struct_0_21182_x6397_x1668052824}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1311756928}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1417126427}

[[1494]{lang="EN-US"}]{#struct_0_21182_x6397_x148957514}[、]{style="font-family:宋体"}[2598]{lang="EN-US"}

[[ControlIT]{lang="EN-US"}]{#struct_0_21182_x6397_880724653}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1715041455}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1013841900}

[[799]{lang="EN-US"}]{#struct_0_21182_x6397_x552242041}

[[Danware-NetOp]{lang="EN-US"}]{#struct_0_21182_x6397_x2118325982}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_610557373}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1667987288}

[[6502]{lang="EN-US"}]{#struct_0_21182_x6397_1060896067}

[[Laplink-Host]{lang="EN-US"}]{#struct_0_21182_x6397_x1311691392}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_1417191963}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1496936339}

[[1547]{lang="EN-US"}]{#struct_0_21182_x6397_x148891978}

[[Laplink-PCSync]{lang="EN-US"}]{#struct_0_21182_x6397_x1714975919}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_1013907436}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x552176505}

[[8444]{lang="EN-US"}]{#struct_0_21182_x6397_x2118260446}

[[Laplink-PCSync-secure]{lang="EN-US"}]{#struct_0_21182_x6397_610622909}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1667921752}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1060961603}

[[8443]{lang="EN-US"}]{#struct_0_21182_x6397_176539456}

[[MS-Terminal-Services]{lang="EN-US"}]{#struct_0_21182_x6397_x1311625856}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_1417257499}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1714910383}

[[3389]{lang="EN-US"}]{#struct_0_21182_x6397_1013972972}

[[Netopia-Timbuktu]{lang="EN-US"}]{#struct_0_21182_x6397_x552110969}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x2118194910}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_610688445}

[[407]{lang="EN-US"}]{#struct_0_21182_x6397_x1667856216}[、]{style="font-family:宋体"}[1417]{lang="EN-US"}[--]{style="font-family:宋体"}[1420]{lang="EN-US"}

[[PCAnywhere]{lang="EN-US"}]{#struct_0_21182_x6397_1061027139}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1029667830}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1311560320}

[[73]{lang="EN-US"}]{#struct_0_21182_x6397_1417323035}[、]{style="font-family:宋体"}[5631]{lang="EN-US"}[、]{style="font-family:宋体"}[5632]{lang="EN-US"}[、]{style="font-family:宋体"}[65301]{lang="EN-US"}

[[RAdmin]{lang="EN-US"}]{#struct_0_21182_x6397_x148760906}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1714844847}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1014038508}

[[4899]{lang="EN-US"}]{#struct_0_21182_x6397_x552045433}

[[Remote-Anything]{lang="EN-US"}]{#struct_0_21182_x6397_x2118129374}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x970537647}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_610753981}

[[3999]{lang="EN-US"}]{#struct_0_21182_x6397_x1667790680}[、]{style="font-family:宋体"}[4000]{lang="EN-US"}

[[Vmware-VMConsole]{lang="EN-US"}]{#struct_0_21182_x6397_1061092675}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1311494784}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1417388571}

[[902]{lang="EN-US"}]{#struct_0_21182_x6397_x710366689}

[[VNC]{lang="EN-US"}]{#struct_0_21182_x6397_x148695370}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1714779311}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1014104044}

[[5801]{lang="EN-US"}]{#struct_0_21182_x6397_x551979897}[--]{style="font-family:宋体"}[5809]{lang="EN-US"}[、]{style="font-family:宋体"}[6900]{lang="EN-US"}[--]{style="font-family:宋体"}[6909]{lang="EN-US"}

[[XWindows]{lang="EN-US"}]{#struct_0_21182_x6397_x2118063838}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_610819517}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1667725144}

[[6000]{lang="EN-US"}]{#struct_0_21182_x6397_1914600702}[--]{style="font-family:宋体"}[6063]{lang="EN-US"}

[[Double-Take]{lang="EN-US"}]{#struct_0_21182_x6397_1061158211}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1445712512}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1283170843}

[[1100]{lang="EN-US"}]{#struct_0_21182_x6397_x282913098}[、]{style="font-family:宋体"}[1105]{lang="EN-US"}

[[EMC-Celerra-Replicator]{lang="EN-US"}]{#struct_0_21182_x6397_x1848997039}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_879886316}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x686197625}

[[8888]{lang="EN-US"}]{#struct_0_21182_x6397_2042685730}

[[MS-Content-Replication-Service]{lang="EN-US"}]{#struct_0_21182_x6397_476601789}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1801942872}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1701417586}

[[560]{lang="EN-US"}]{#struct_0_21182_x6397_926940483}[、]{style="font-family:宋体"}[507]{lang="EN-US"}

[[Netapp-SnapMirror]{lang="EN-US"}]{#struct_0_21182_x6397_x1445646976}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1283236379}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x282847562}

[[10565]{lang="EN-US"}]{#struct_0_21182_x6397_x1848931503}[--]{style="font-family:宋体"}[10569]{lang="EN-US"}

[[Remote-Replication-Agent]{lang="EN-US"}]{#struct_0_21182_x6397_879951852}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x686132089}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2042751266}

[[5678]{lang="EN-US"}]{#struct_0_21182_x6397_476667325}

[[Rsync]{lang="EN-US"}]{#struct_0_21182_x6397_x1801877336}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_927006019}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1445581440}

[[873]{lang="EN-US"}]{#struct_0_21182_x6397_1283301915}

[[Borland-Interbase]{lang="EN-US"}]{#struct_0_21182_x6397_1778904113}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x282782026}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1848865967}

[[3050]{lang="EN-US"}]{#struct_0_21182_x6397_880017388}

[[IBM-DB2]{lang="EN-US"}]{#struct_0_21182_x6397_x686066553}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_2042816802}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_476732861}

[[523]{lang="EN-US"}]{#struct_0_21182_x6397_x1801811800}

[[InterSystems-Cache]{lang="EN-US"}]{#struct_0_21182_x6397_927071555}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1445515904}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1283367451}

[[1972]{lang="EN-US"}]{#struct_0_21182_x6397_x282716490}

[[MS-SQL]{lang="EN-US"}]{#struct_0_21182_x6397_x1848800431}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_880082924}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x686001017}

[[1433]{lang="EN-US"}]{#struct_0_21182_x6397_2042882338}

[[MySQL]{lang="EN-US"}]{#struct_0_21182_x6397_476798397}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1801746264}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x882934866}

[[3306]{lang="EN-US"}]{#struct_0_21182_x6397_927137091}

[[Oracle]{lang="EN-US"}]{#struct_0_21182_x6397_x1445450368}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1283432987}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x282650954}

[[66]{lang="EN-US"}]{#struct_0_21182_x6397_x1848734895}[、]{style="font-family:宋体"}[1521]{lang="EN-US"}[、]{style="font-family:宋体"}[1525]{lang="EN-US"}

[[Pervasive-SQL]{lang="EN-US"}]{#struct_0_21182_x6397_880148460}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x685935481}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2042947874}

[[1583]{lang="EN-US"}]{#struct_0_21182_x6397_476863933}

[[PostgreSQL]{lang="EN-US"}]{#struct_0_21182_x6397_x1801680728}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_927202627}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1445384832}

[[5432]{lang="EN-US"}]{#struct_0_21182_x6397_1283498523}

[[Scalable-SQL]{lang="EN-US"}]{#struct_0_21182_x6397_x282585418}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1848669359}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_880213996}

[[3352]{lang="EN-US"}]{#struct_0_21182_x6397_x685869945}

[[SQL-Service]{lang="EN-US"}]{#struct_0_21182_x6397_2043013410}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_476929469}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1801615192}

[[156]{lang="EN-US"}]{#struct_0_21182_x6397_927268163}

[[Sybase-SQL]{lang="EN-US"}]{#struct_0_21182_x6397_x2115162752}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_613720603}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x952363338}

[[1498]{lang="EN-US"}]{#struct_0_21182_x6397_1776520017}[、]{style="font-family:宋体"}[2439]{lang="EN-US"}[、]{style="font-family:宋体"}[2638]{lang="EN-US"}[、]{style="font-family:宋体"}[3968]{lang="EN-US"}

[[UniSQL]{lang="EN-US"}]{#struct_0_21182_x6397_210436076}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1355647865}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1373235490}

[[1978]{lang="EN-US"}]{#struct_0_21182_x6397_x192848451}[、]{style="font-family:宋体"}[1979]{lang="EN-US"}

[[HTTPS]{lang="EN-US"}]{#struct_0_21182_x6397_1823574184}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_257490243}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2115097216}

[[443]{lang="EN-US"}]{#struct_0_21182_x6397_613786139}

[[SSH]{lang="EN-US"}]{#struct_0_21182_x6397_x952297802}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_1776585553}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_210501612}

[[22]{lang="EN-US"}]{#struct_0_21182_x6397_x1355582329}

[[EMC-SRDFA-IP]{lang="EN-US"}]{#struct_0_21182_x6397_1373301026}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1823639720}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_257555779}

[[1748]{lang="EN-US"}]{#struct_0_21182_x6397_x2115031680}

[[FCIP]{lang="EN-US"}]{#struct_0_21182_x6397_613851675}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x952232266}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1776651089}

[[3225]{lang="EN-US"}]{#struct_0_21182_x6397_210567148}

[[iFCP]{lang="EN-US"}]{#struct_0_21182_x6397_x1355516793}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1373366562}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x192717379}

[[3420]{lang="EN-US"}]{#struct_0_21182_x6397_1823705256}

[[iSCSI]{lang="EN-US"}]{#struct_0_21182_x6397_257621315}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x2114966144}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_613917211}

[[3260]{lang="EN-US"}]{#struct_0_21182_x6397_x952166730}

[[Liquid-Audio]{lang="EN-US"}]{#struct_0_21182_x6397_1776716625}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1355451257}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1373432098}

[[18888]{lang="EN-US"}]{#struct_0_21182_x6397_x192651843}

[[MS-NetShow]{lang="EN-US"}]{#struct_0_21182_x6397_1823770792}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_257686851}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x2114900608}

[[1755]{lang="EN-US"}]{#struct_0_21182_x6397_613982747}

[[RTSP]{lang="EN-US"}]{#struct_0_21182_x6397_x952101194}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_1776782161}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_210698220}

[[554]{lang="EN-US"}]{#struct_0_21182_x6397_x1355385721}[、]{style="font-family:宋体"}[8554]{lang="EN-US"}

[[VDOLive]{lang="EN-US"}]{#struct_0_21182_x6397_1373497634}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x192586307}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1823836328}

[[7000]{lang="EN-US"}]{#struct_0_21182_x6397_257752387}

[[BMC-Patrol]{lang="EN-US"}]{#struct_0_21182_x6397_614048283}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x952035658}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1776847697}

[[6161]{lang="EN-US"}]{#struct_0_21182_x6397_210763756}[、]{style="font-family:宋体"}[6162]{lang="EN-US"}[、]{style="font-family:宋体"}[6767]{lang="EN-US"}[、]{style="font-family:宋体"}[6768, 8160]{lang="EN-US"}[、]{style="font-family:宋体"}[8161]{lang="EN-US"}[、]{style="font-family:宋体"}[10128]{lang="EN-US"}

[[HP-OpenView]{lang="EN-US"}]{#struct_0_21182_x6397_x1355320185}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_1373563170}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x192520771}

[[7426]{lang="EN-US"}]{#struct_0_21182_x6397_1823901864}[--]{style="font-family:宋体"}[7431]{lang="EN-US"}[、]{style="font-family:宋体"}[7501]{lang="EN-US"}[、]{style="font-family:宋体"}[7510]{lang="EN-US"}

[[HP-Radia]{lang="EN-US"}]{#struct_0_21182_x6397_257817923}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_479830555}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1086253386}

[[3460]{lang="EN-US"}]{#struct_0_21182_x6397_1642629969}[、]{style="font-family:宋体"}[3461]{lang="EN-US"}[、]{style="font-family:宋体"}[3464]{lang="EN-US"}[、]{style="font-family:宋体"}[3466]{lang="EN-US"}

[[IBM-NetView]{lang="EN-US"}]{#struct_0_21182_x6397_76546028}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_x1489537913}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1239345442}

[[729]{lang="EN-US"}]{#struct_0_21182_x6397_1689684136}[--]{style="font-family:宋体"}[731]{lang="EN-US"}

[[IBM-Tivoli]{lang="EN-US"}]{#struct_0_21182_x6397_123600195}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_2045980032}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_479896091}

[[94]{lang="EN-US"}]{#struct_0_21182_x6397_x1086187850}[、]{style="font-family:宋体"}[627]{lang="EN-US"}[、]{style="font-family:宋体"}[1580]{lang="EN-US"}[、]{style="font-family:宋体"}[1581]{lang="EN-US"}[、]{style="font-family:宋体"}[1965]{lang="EN-US"}

[[LANDesk]{lang="EN-US"}]{#struct_0_21182_x6397_76611564}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_x1489472377}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1239410978}

[[9535]{lang="EN-US"}]{#struct_0_21182_x6397_x326672963}[、]{style="font-family:宋体"}[9593]{lang="EN-US"}[--]{style="font-family:宋体"}[9595]{lang="EN-US"}

[[NetIQ]{lang="EN-US"}]{#struct_0_21182_x6397_1689749672}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_2046045568}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_479961627}

[[2220]{lang="EN-US"}]{#struct_0_21182_x6397_x1086122314}[、]{style="font-family:宋体"}[2735]{lang="EN-US"}[、]{style="font-family:宋体"}[10113]{lang="EN-US"}[--]{style="font-family:宋体"}[10116]{lang="EN-US"}

[[Netopia-netOctopus]{lang="EN-US"}]{#struct_0_21182_x6397_1642761041}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_76677100}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1489406841}

[[1917]{lang="EN-US"}]{#struct_0_21182_x6397_x326607427}[、]{style="font-family:宋体"}[1921]{lang="EN-US"}

[[Novell-ZenWorks]{lang="EN-US"}]{#struct_0_21182_x6397_1689815208}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_123731267}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2046111104}

[[517]{lang="EN-US"}]{#struct_0_21182_x6397_480027163}[、]{style="font-family:宋体"}[1761]{lang="EN-US"}[--]{style="font-family:宋体"}[1763]{lang="EN-US"}[、]{style="font-family:宋体"}[2037, 2544]{lang="EN-US"}[、]{style="font-family:宋体"}[8039]{lang="EN-US"}

[[WAAS-FlowMonitor]{lang="EN-US"}]{#struct_0_21182_x6397_1642826577}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_76742636}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1489341305}

[[7878]{lang="EN-US"}]{#struct_0_21182_x6397_x326541891}

[[WBEM]{lang="EN-US"}]{#struct_0_21182_x6397_1689880744}

[[Pass-through]{lang="EN-US"}]{#struct_0_21182_x6397_123796803}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2046176640}

[[5987]{lang="EN-US"}]{#struct_0_21182_x6397_x1085991242}[、]{style="font-family:宋体"}[5988]{lang="EN-US"}

[[Clearcase]{lang="EN-US"}]{#struct_0_21182_x6397_1642892113}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_76808172}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x1489275769}

[[371]{lang="EN-US"}]{#struct_0_21182_x6397_x326476355}

[[CVS]{lang="EN-US"}]{#struct_0_21182_x6397_1689946280}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_123862339}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2046242176}

[[2401]{lang="EN-US"}]{#struct_0_21182_x6397_x1085925706}

[[CIFS]{lang="EN-US"}]{#struct_0_21182_x6397_1642957649}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_76873708}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1239673122}

[[139]{lang="EN-US"}]{#struct_0_21182_x6397_x326410819}[、]{style="font-family:宋体"}[445]{lang="EN-US"}

[[HTTP]{lang="EN-US"}]{#struct_0_21182_x6397_1690011816}

[[LZ+TFO+DRE]{lang="EN-US"}]{#struct_0_21182_x6397_123927875}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_542244549}

[[80]{lang="EN-US"}]{#struct_0_21182_x6397_x620554865}[、]{style="font-family:宋体"}[3128]{lang="EN-US"}[、]{style="font-family:宋体"}[8000]{lang="EN-US"}[、]{style="font-family:宋体"}[8001]{lang="EN-US"}[、]{style="font-family:宋体"}[8080]{lang="EN-US"}

[[HTTPS]{lang="EN-US"}]{#struct_0_21182_x6397_945529076}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x217270338}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1348813603}

[[443]{lang="EN-US"}]{#struct_0_21182_x6397_x1380069752}

[[L2TP]{lang="EN-US"}]{#struct_0_21182_x6397_898474909}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_542310085}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_2108394026}

[[1701]{lang="EN-US"}]{#struct_0_21182_x6397_945594612}

[[OpenVPN]{lang="EN-US"}]{#struct_0_21182_x6397_x1783288743}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x217204802}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_1348879139}

[[1194]{lang="EN-US"}]{#struct_0_21182_x6397_898540445}

[[PPTP]{lang="EN-US"}]{#struct_0_21182_x6397_x1830342910}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_542375621}

[[-]{lang="EN-US" style="font-size:10.5pt"}]{#struct_0_21182_x6397_x620423793}

[[1723]{lang="EN-US"}]{#struct_0_21182_x6397_945660148}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1255617068}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x398742616}[进入]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[预定义策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_2060336403}

[\[Sysname\] waas policy waas_default]{lang="EN-US"}

[\[Sysname-waaspolicy-waas_default\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1324876362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas policy]{lang="EN-US"}**]{#struct_0_21182_x6397_146885032}

::: {#282580802 .myid}
[]{#_Toc404787446}[]{#struct_0_21182_x6397_1687507654}[]{#_Toc382831082}

**WAAS \-- WAAS配置命令 \-- waas tfo auto-discovery blacklist enable**

------------------------------------------------------------------------

[**[waas tfo auto-discovery blacklist enable]{lang="EN-US"}**]{#struct_0_21182_x6397_x1783223207}[命令用来开启自动发现黑名单功能。]{style="font-family:宋体"}

[**[undo waas tfo auto-discovery blacklist enable]{lang="EN-US"}**]{#struct_0_21182_x6397_x86664224}[命令用来关闭自动发现黑名单功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1445989056}

[**[waas tfo auto-discovery blacklist enable]{lang="EN-US"}**]{#struct_0_21182_x6397_x1309844441}

[**[undo waas tfo auto-discovery blacklist enable]{lang="EN-US"}**]{#struct_0_21182_x6397_x1509618956}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1498062703}

[[自动发现黑名单功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21182_x6397_166948727}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1645968509}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_34858202}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x995530901}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1056253446}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x2140092538}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_2034065418}

[[当本端设备配置了]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1004454292}[策略并应用于接口时，如果本端设备不能通过此接口与对端设备建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，那么系统自动将请求的服务器接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号加入黑名单，对匹配黑名单的流量不做任何优化。]{style="font-family:宋体"}

[[在建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_21182_x6397_1922823641}[连接的三次握手过程中，本端发送携带特定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[选项的请求报文后，如果发生下列情况，则认为连接建立失败：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在指定时间内未作出有效应答。]{style="font-family:宋体"}]{#struct_0_21182_x6397_x217139266}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对端设备关闭了]{style="font-family:宋体"}]{#struct_0_21182_x6397_x549715375}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x979651680}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x733114834}[开启]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[自动发现黑名单功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_1323896740}

[\[Sysname\] waas tfo auto-discovery blacklist enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1025788326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas tfo auto-discovery blacklist]{lang="EN-US"}**]{#struct_0_21182_x6397_x1125459879}
:::

::: {#-1486098715 .myid}
[]{#_Toc404787447}[]{#struct_0_21182_x6397_216386645}

**WAAS \-- WAAS配置命令 \-- waas tfo auto-discovery blacklist hold-time**

------------------------------------------------------------------------

[**[waas tfo auto-discovery blacklist hold-time]{lang="EN-US"}**]{#struct_0_21182_x6397_x599784982}[命令用来配置黑名单表项的老化时间。]{style="font-family:宋体"}

[**[undo waas tfo auto-discovery blacklist hold-time]{lang="EN-US"}**]{#struct_0_21182_x6397_x2094466885}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1991415926}

[**[waas tfo auto-discovery blacklist hold-time ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_21182_x6397_x1741288101}

[**[undo waas tfo auto-discovery blacklist hold-time]{lang="EN-US"}**]{#struct_0_21182_x6397_x1348008047}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1834359131}

[[黑名单表项的老化时间为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_21182_x6397_1348944675}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_769617990}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1424041364}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x178542463}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1492577176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x224932704}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x844109069}

[*[minutes]{lang="EN-US"}*]{#struct_0_21182_x6397_x1288492488}[：指定黑名单表项的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10080]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1335153196}

[[黑名单表项具有一定的生存时间，超出老化时间，黑名单表项被系统自动删除，当有新连接接入时，设备通过发现黑名单功能构建新的黑名单表项。]{style="font-family:宋体"}]{#struct_0_21182_x6397_140746197}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1617782786}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x444763083}[配置]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[黑名单表项的老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_710450398}

[\[Sysname\] waas tfo auto-discovery blacklist hold-time 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2142399186}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas tfo auto-discovery blacklist]{lang="EN-US"}**]{#struct_0_21182_x6397_x1379938680}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[waas tfo auto-discovery blacklist enable]{lang="EN-US"}**]{#struct_0_21182_x6397_x135505511}
:::

::: {#-1708448751 .myid}
[]{#_Toc404787448}[]{#struct_0_21182_x6397_x747463826}

**WAAS \-- WAAS配置命令 \-- waas tfo base-congestion-window**

------------------------------------------------------------------------

[**[waas tfo base-congestion-window]{lang="EN-US"}**]{#struct_0_21182_x6397_x1379951436}[命令用来配置超时重传时慢启动的初始拥塞窗口大小。]{style="font-family:宋体"}

[**[undo waas tfo base-congestion-window]{lang="EN-US"}**]{#struct_0_21182_x6397_753221763}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_264347012}

[**[waas tfo base-congestion-window ]{lang="EN-US"}***[segments]{lang="EN-US"}*]{#struct_0_21182_x6397_1481783254}

[**[undo waas tfo base-congestion-window]{lang="EN-US"}**]{#struct_0_21182_x6397_136905339}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1915768428}

[[初始拥塞窗口为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_21182_x6397_x2118432983}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1024698185}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x1380208812}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1928356306}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1667514318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x630184557}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_898605981}

[*[segments]{lang="EN-US"}*]{#struct_0_21182_x6397_x361537345}*[：]{style="font-family:宋体"}*[超时重传时慢启动的初始拥塞窗口大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为最大报文段个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1005956762}

[[拥塞窗口的大小取决于网络的拥塞程度和发送速度，并且动态的在变化。设置合理的慢启动初始拥塞窗口，当拥塞发生后，能够较快的恢复到网络最大传输能力。]{style="font-family:宋体"}]{#struct_0_21182_x6397_1380320232}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1269462936}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_999046271}[配置超时重传时慢启动的初始拥塞窗口为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x668889958}

[\[Sysname\] waas tfo base-congestion-window 3]{lang="EN-US"}
:::

::: {#-1711981500 .myid}
[]{#_Toc404787449}[]{#struct_0_21182_x6397_1502343559}

**WAAS \-- WAAS配置命令 \-- waas tfo keepalive**

------------------------------------------------------------------------

[**[waas tfo keepalive]{lang="EN-US"}**]{#struct_0_21182_x6397_x1919635596}[命令用来开启]{style="font-family:宋体"}[TFO]{lang="EN-US"}[的保活功能。]{style="font-family:宋体"}

[**[undo waas tfo keepalive]{lang="EN-US"}**]{#struct_0_21182_x6397_1868353725}[命令用来关闭]{style="font-family:宋体"}[TFO]{lang="EN-US"}[的保活功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1290842562}

[**[waas tfo keepalive]{lang="EN-US"}**]{#struct_0_21182_x6397_x722309515}

[**[undo waas tfo keepalive]{lang="EN-US"}**]{#struct_0_21182_x6397_x834069880}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1889276388}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_x1830277374}[的保活功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_130698389}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x78336463}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_819402513}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_1280102406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x61043171}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1203610110}

[[开启]{style="font-family:宋体"}[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_1596644260}[的保活功能后，系统启动保活定时器。当定时器超时后，如果通信双方仍没有数据传输，则向对端设备发送保活报文，使连接不断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_2042440400}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_x1615644711}[开启]{style="font-family:宋体"}[TFO]{lang="EN-US"}[的保活功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x926190102}

[\[Sysname\] waas tfo keepalive]{lang="EN-US"}
:::

::: {#-746350279 .myid}
[]{#_Toc404787450}[]{#struct_0_21182_x6397_x1675624235}

**WAAS \-- WAAS配置命令 \-- waas tfo optimize dre**

------------------------------------------------------------------------

[**[waas tfo optimize dre]{lang="EN-US"}**]{#struct_0_21182_x6397_1662775636}[命令用来开启]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[消除数据冗余功能。]{style="font-family:宋体"}

[**[undo waas tfo optimize dre]{lang="EN-US"}**]{#struct_0_21182_x6397_x1164862866}[命令用来关闭]{style="font-family:
宋体"}[WAAS]{lang="EN-US"}[消除数据冗余功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1795549033}

[**[waas tfo optimize dre]{lang="EN-US"}**]{#struct_0_21182_x6397_542441157}

[**[undo waas tfo optimize dre]{lang="EN-US"}**]{#struct_0_21182_x6397_958568448}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1607952187}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_1414019476}[消除数据冗余功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x601016985}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_1397873067}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_654178778}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x27337158}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_807374219}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x224315462}

[[只有]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_730833708}[消除数据冗余功能处于开启状态时，]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略下所配置的消除数据冗余优化方式才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_90531804}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_1607341629}[关闭]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[消除数据冗余功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x2091345755}

[\[Sysname\] undo waas tfo optimize dre]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_2108525098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas status]{lang="EN-US"}**]{#struct_0_21182_x6397_1409506954}
:::

::: {#-195704495 .myid}
[]{#_Toc404787451}[]{#struct_0_21182_x6397_1707740282}

**WAAS \-- WAAS配置命令 \-- waas tfo optimize lz**

------------------------------------------------------------------------

[**[waas tfo optimize lz]{lang="EN-US"}**]{#struct_0_21182_x6397_13050768}[命令用来开启]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[数据压缩功能。]{style="font-family:宋体"}

[**[undo waas tfo optimize lz]{lang="EN-US"}**]{#struct_0_21182_x6397_x5505693}[命令用来关闭]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[数据压缩功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x639548406}

[**[waas tfo optimize lz]{lang="EN-US"}**]{#struct_0_21182_x6397_1833994059}

[**[undo waas tfo optimize lz]{lang="EN-US"}**]{#struct_0_21182_x6397_x278969971}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1948707180}

[[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x2138833818}[数据压缩功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x164734111}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x699468844}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1961328976}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x247812330}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_743647389}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x620358257}

[[只有]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_21182_x6397_x1275288087}[数据压缩功能处于开启状态时，]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略下所配置的数据压缩优化方式才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x2125509638}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_1296649193}[关闭]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[数据压缩功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_x1076674817}

[\[Sysname\] undo waas tfo optimize lz]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1682007760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display waas status]{lang="EN-US"}**]{#struct_0_21182_x6397_1405471244}
:::

::: {#1183690084 .myid}
[]{#_Toc404787452}[]{#struct_0_21182_x6397_x692545539}

**WAAS \-- WAAS配置命令 \-- waas tfo receive-buffer**

------------------------------------------------------------------------

[**[waas tfo receive-buffer]{lang="EN-US"}**]{#struct_0_21182_x6397_36078551}[命令用来配置]{style="font-family:宋体"}[TFO]{lang="EN-US"}[的接收缓冲区大小。]{style="font-family:宋体"}

[**[undo waas tfo receive-buffer]{lang="EN-US"}**]{#struct_0_21182_x6397_x952345878}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1548637400}

[**[waas tfo receive-buffer ]{lang="EN-US"}***[buffer-size]{lang="EN-US"}*]{#struct_0_21182_x6397_1607455721}

[**[undo waas tfo receive-buffer]{lang="EN-US"}**]{#struct_0_21182_x6397_x2105775506}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x617276883}

[[TFO]{lang="EN-US"}]{#struct_0_21182_x6397_325958440}[的接收缓冲区为]{style="font-family:宋体"}[64KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21182_x6397_945725684}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21182_x6397_x455637187}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1255260822}

[[network-admin]{lang="EN-US"}]{#struct_0_21182_x6397_x163109551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21182_x6397_248311937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1869202868}

[*[buffer-size]{lang="EN-US"}*]{#struct_0_21182_x6397_838266219}*[：]{style="font-family:宋体"}*[TFO]{lang="EN-US"}[的接收缓冲区大小，取值范围为]{style="font-family:宋体"}[32]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21182_x6397_x1193891956}

[[用户可以通过调整接收缓冲区的大小来影响线路的吞吐量。]{style="font-family:宋体"}]{#struct_0_21182_x6397_x379380675}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21182_x6397_1345126949}

[[\# ]{lang="EN-US"}]{#struct_0_21182_x6397_1086752793}[调整]{style="font-family:宋体"}[TFO]{lang="EN-US"}[的接收缓冲区为]{style="font-family:宋体"}[1024KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21182_x6397_829525460}

[\[Sysname\] waas tfo receive-buffer 1024]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
