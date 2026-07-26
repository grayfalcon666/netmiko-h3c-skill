::: {#1605279780 .myid}
[]{#_Toc404792077}[]{#struct_0_18947_x5086_x1666655093}[]{#_Toc304476814}

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer apply**

------------------------------------------------------------------------

[**[buffer apply]{lang="EN-US"}**]{#struct_0_18947_x5086_x613257356}[命令用来应用用户对数据缓冲区所做的配置。]{style="font-family:宋体"}

[**[undo buffer apply]{lang="EN-US"}**]{#struct_0_18947_x5086_1396721298}[命令用来取消数据缓冲区配置的应用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1413211050}

[**[buffer apply]{lang="EN-US"}**]{#struct_0_18947_x5086_x1206087473}

[**[undo buffer apply]{lang="EN-US"}**]{#struct_0_18947_x5086_x1164144746}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1069079312}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18947_x5086_x975160455}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x431722435}

[[network-admin]{lang="EN-US"}]{#struct_0_18947_x5086_1368181743}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18947_x5086_x735066036}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x24708997}

[[用户对数据缓冲区进行配置后，必须使用]{style="font-family:宋体"}**[buffer apply]{lang="EN-US"}**]{#struct_0_18947_x5086_x1705104934}[命令进行应用，这些配置才能生效。]{style="font-family:宋体"}

[[配置被应用后就不能被修改，需要先取消应用，再修改、应用，新的配置才能生效。]{style="font-family:宋体"}]{#struct_0_18947_x5086_18350286}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1383355850}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_1931064420}[应用用户对数据缓冲区所做的配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x1548729679}

[\[Sysname\] buffer apply]{lang="EN-US"}
:::

::::: {#-363753531 .myid}
[]{#_Toc404792078}[]{#struct_0_18947_x5086_x1973779223}[]{#_Toc304476815}

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer queue guaranteed**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](数据缓冲区命令.files/image001.png){#图片 3 width="62" height="27"}]{lang="EN-US"}]{#struct_0_18947_x5086_x431787971}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_18947_x5086_1781302500}
:::

**[ ]{lang="EN-US"}**

[**[buffer queue]{lang="EN-US"}**[ **guaranteed**]{lang="EN-US"}]{#struct_0_18947_x5086_x2111336866}[命令用来配置指定队列最多可使用的固定区域的大小。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **buffer** **queue** **guaranteed**]{lang="EN-US"}]{#struct_0_18947_x5086_280665768}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1493726580}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18947_x5086_x631422598}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **guaranteed** { **ratio** *ratio-value* \| *size-value* }]{lang="EN-US"}]{#struct_0_18947_x5086_x1103705135}

[**[undo buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **guaranteed**]{lang="EN-US"}]{#struct_0_18947_x5086_494160125}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18947_x5086_x1221024719}[模式：]{style="font-family:宋体"}

[**[buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **chassis** *chassis-number* **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **guaranteed** { **ratio** *ratio-value* \| *size-value* }]{lang="EN-US"}]{#struct_0_18947_x5086_x431853507}

[**[undo buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **chassis** *chassis-number* **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **guaranteed**]{lang="EN-US"}]{#struct_0_18947_x5086_606820274}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1934680257}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_18947_x5086_x1215127815}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1295705351}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18947_x5086_221460622}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1928651290}

[[network-admin]{lang="EN-US"}]{#struct_0_18947_x5086_x1093621696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18947_x5086_297957240}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1517547041}

[**[ingress]{lang="EN-US"}**]{#struct_0_18947_x5086_x431919043}[：表示对接收数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[egress]{lang="EN-US"}**]{#struct_0_18947_x5086_x1399778511}[：表示对发送数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_1835552890}[：取值只能为]{style="font-family:宋体"}[1]{lang="EN-US"}[，表示配置当前设备的数据缓冲区。（集中式设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_1922366903}[：表示接口板所在的槽位号。不指定该参数时，表示配置所有接口板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x631944499}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示配置所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_2044727442}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定接口板。不指定该参数时，表示配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的所有接口板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cell]{lang="EN-US"}**]{#struct_0_18947_x5086_x573575117}[：配置队列最多可使用的]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中固定区域的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_18947_x5086_2027773999}[：配置队列最多可使用的]{style="font-family:宋体"}[packet]{lang="EN-US"}[资源中固定区域的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_18947_x5086_x467434232}[：需要配置的队列编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[ratio-value]{lang="EN-US"}*]{#struct_0_18947_x5086_1846211505}[：队列最多可使用的缓存大小占整个接口板]{style="font-family:宋体"}[cell]{lang="EN-US"}[或]{style="font-family:宋体"}[packet]{lang="EN-US"}[固定区域的大小的百分比。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[size-value]{lang="EN-US"}*]{#struct_0_18947_x5086_x431984579}[：队列最多可使用的字节数。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x183431033}

[[缺省情况下，所有队列均分固定区域，但用户也可以使用该命令调整指定队列最多可使用的固定区域的大小，其它未配置的队列则均分剩余的固定区域。]{style="font-family:宋体"}]{#struct_0_18947_x5086_1282455942}

[[配置该命令后，系统就与给队列预留指定大小的空间，即便该队列没有报文存储需求，其他队列也不能抢占。所有队列所配置的固定区域大小之和，不应超过可配置的总固定区域大小，否则配置失败。]{style="font-family:宋体"}]{#struct_0_18947_x5086_x603144719}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18947_x5086_455459657}

[*[\# ]{lang="EN-US"}*]{#struct_0_18947_x5086_x173517675}[配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[最多可使用的]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定区域的大小为整个]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定缓冲区大小的]{style="font-family:宋体"}[20%]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[*[\<Sysname\>]{lang="EN-US"}*[ system-view]{lang="EN-US"}]{#struct_0_18947_x5086_1889225066}

[\[Sysname\] buffer egress cell queue 0 guaranteed ratio 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_1150271165}[配置]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板的队列]{style="font-family:宋体"}[0]{lang="EN-US"}[最多可使用的]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定区域的大小为该接口板]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定缓冲区大小的]{style="font-family:宋体"}[15%]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x417156934}

[\[Sysname\] buffer egress slot 2 cell queue 0 guaranteed ratio 15]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x1874740401}[配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的队列]{style="font-family:宋体"}[0]{lang="EN-US"}[最多可使用的]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定区域的大小为该成员设备]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定缓冲区大小的]{style="font-family:宋体"}[15%]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x432050115}

[\[Sysname\] buffer egress slot 2 cell queue 0 guaranteed ratio 15]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x1491410514}[配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板的队列]{style="font-family:宋体"}[0]{lang="EN-US"}[最多可使用的]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定区域的大小为该接口板]{style="font-family:宋体"}[cell]{lang="EN-US"}[固定缓冲区大小的]{style="font-family:宋体"}[15%]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x1999127392}

[\[Sysname\] buffer egress chassis 2 slot 2 cell queue 0 guaranteed ratio 15]{lang="EN-US"}
:::::

::: {#-1768896817 .myid}
[]{#_Toc404792079}[]{#struct_0_18947_x5086_x985596038}[]{#_Toc304476816}[]{#_Toc319071747}

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer queue shared**

------------------------------------------------------------------------

[**[buffer queue shared]{lang="EN-US"}**]{#struct_0_18947_x5086_500641280}[命令用来配置指定队列最多可使用的共享区域的大小。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **buffer queue shared**]{lang="EN-US"}]{#struct_0_18947_x5086_1859725876}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x654320208}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18947_x5086_x76287417}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **shared** { **ratio** *ratio-value* \| *size-value* }]{lang="EN-US"}]{#struct_0_18947_x5086_x1411648462}

[**[undo buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **shared**]{lang="EN-US"}]{#struct_0_18947_x5086_x432115651}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18947_x5086_x685335802}[模式：]{style="font-family:宋体"}

[**[buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **chassis** *chassis-number* **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **shared** { **ratio** *ratio-value* \| *size-value* }]{lang="EN-US"}]{#struct_0_18947_x5086_2132708271}

[**[undo buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **chassis** *chassis-number* **slot** *slot-number* \] { **cell** \| **packet** } **queue** *queue-id* **shared**]{lang="EN-US"}]{#struct_0_18947_x5086_1272819032}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1244273293}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_18947_x5086_460312436}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x316088081}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18947_x5086_1548318345}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18947_x5086_2101930196}

[[network-admin]{lang="EN-US"}]{#struct_0_18947_x5086_1983190551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18947_x5086_1791522648}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x432181187}

[**[ingress]{lang="EN-US"}**]{#struct_0_18947_x5086_44199277}**[：]{style="font-family:宋体"}**[表示对接收数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[egress]{lang="EN-US"}**]{#struct_0_18947_x5086_x1754371753}**[：]{style="font-family:宋体"}**[表示对发送数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x1033072996}[：取值只能为]{style="font-family:宋体"}[1]{lang="EN-US"}[，表示配置当前设备的数据缓冲区。（集中式设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_1855363214}[：表示接口板所在的槽位号。不指定该参数时，表示配置所有接口板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x1511602332}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示配置所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_1209195232}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定接口板。不指定该参数时，表示配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的所有接口板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cell]{lang="EN-US"}**]{#struct_0_18947_x5086_x1675334959}[：配置队列在]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中的最大共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_18947_x5086_885351544}[：配置队列在]{style="font-family:宋体"}[packet]{lang="EN-US"}[资源中的最大共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_18947_x5086_1751578442}[：需要配置的队列编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[ratio-value]{lang="EN-US"}*]{#struct_0_18947_x5086_x431198147}[：队列的最大共享缓存占用比，以百分数形式表示。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[size-value]{lang="EN-US"}*]{#struct_0_18947_x5086_x1026586908}[：队列的最大共享缓存占用字节数。参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1366935076}

[[缺省情况下，所有队列均分共享区域，但用户也可以调整指定队列最多可使用的共享区域的大小，其它未配置的队列最多可使用的共享区域的大小仍遵循缺省值。最终，各队列最多可使用的共享区域的大小将由芯片根据]{style="font-family:宋体"}**[buffer shared]{lang="EN-US"}**]{#struct_0_18947_x5086_1326334642}[配置，以及实际需要收发报文的数量决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1566088813}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_2040780198}[配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[在]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中的最大共享缓存占用比为]{style="font-family:宋体"}[10%]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_1211774765}

[\[Sysname\] buffer egress cell queue 0 shared ratio 10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_998364982}[配置]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板的队列]{style="font-family:宋体"}[0]{lang="EN-US"}[在该设备]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中的最大共享缓存占用比为]{style="font-family:宋体"}[5%]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x110926695}

[\[Sysname\] buffer egress slot 2 cell queue 0 shared ratio 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x431263683}[配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的队列]{style="font-family:宋体"}[0]{lang="EN-US"}[在该设备]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中的最大共享缓存占用比为]{style="font-family:宋体"}[5%]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x969320828}

[\[Sysname\] buffer egress slot 2 cell queue 0 shared ratio 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x1682104091}[配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板的队列]{style="font-family:宋体"}[0]{lang="EN-US"}[在该设备]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中的最大共享缓存占用比为]{style="font-family:宋体"}[5%]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x1464380040}

[\[Sysname\] buffer egress chassis 2 slot 2 cell queue 0 shared ratio 5]{lang="EN-US"}
:::

::: {#1268212040 .myid}
[]{#_Toc404792080}[]{#struct_0_18947_x5086_483469970}[]{#_Toc304476818}

**数据缓冲区 \-- 数据缓冲区配置命令 \-- buffer total-shared**

------------------------------------------------------------------------

[**[buffer total-shared]{lang="EN-US"}**]{#struct_0_18947_x5086_1878143259}[命令用来配置数据缓冲区中共享区域的大小。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **buffer total-shared**]{lang="EN-US"}]{#struct_0_18947_x5086_x147150456}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x512356152}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18947_x5086_x260064372}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **slot** *slot-number* \] { **cell** \| **packet** } **total-shared** { **ratio** *ratio-value* \| *size-value* }]{lang="EN-US"}]{#struct_0_18947_x5086_x1552682295}

[**[undo buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **slot** *slot-number* \] { **cell** \| **packet** } **total-shared**]{lang="EN-US"}]{#struct_0_18947_x5086_x431722434}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18947_x5086_1368247279}[模式：]{style="font-family:宋体"}

[**[buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **chassis** *chassis-number* **slot** *slot-number* \] { **cell** \| **packet** } **total-shared** { **ratio** *ratio-value* \| *size-value* }]{lang="EN-US"}]{#struct_0_18947_x5086_1204651084}

[**[undo buffer ]{lang="EN-US"}**[{ **ingress** \| **egress** } \[ **chassis** *chassis-number* **slot** *slot-number* \] { **cell** \| **packet** } **total-shared**]{lang="EN-US"}]{#struct_0_18947_x5086_x1729652661}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1487248837}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_18947_x5086_197513945}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x798352518}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18947_x5086_178928812}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18947_x5086_875483865}

[[network-admin]{lang="EN-US"}]{#struct_0_18947_x5086_x431787970}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18947_x5086_1781368036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1778897593}

[**[ingress]{lang="EN-US"}**]{#struct_0_18947_x5086_x1275757810}[：表示对接收数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[egress]{lang="EN-US"}**]{#struct_0_18947_x5086_x1926156132}[：表示对发送数据缓冲区进行配置。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x662344418}[：取值只能为]{style="font-family:宋体"}[1]{lang="EN-US"}[，表示配置当前设备的数据缓冲区。（集中式设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_16184173}[：表示接口板所在的槽位号。不指定该参数时，表示配置所有接口板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_2134796799}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示配置所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x1958011076}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定接口板。不指定该参数时，表示配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的所有接口板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cell]{lang="EN-US"}**]{#struct_0_18947_x5086_x373247848}[：配置]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中的共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_18947_x5086_x431853506}[：配置]{style="font-family:宋体"}[packet]{lang="EN-US"}[资源中的共享缓存区的大小。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}***[ratio-value]{lang="EN-US"}*]{#struct_0_18947_x5086_606754738}[：缓冲区中共享区域所占的比例，以百分数形式表示。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[size-value]{lang="EN-US"}*]{#struct_0_18947_x5086_x615553609}[：缓冲区中共享区域所占的字节数。该参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1088654164}

[[接口卡上整个数据缓冲区的大小是固定的，用户配置共享区域的大小后，其余部分将自动成为固定区域。]{style="font-family:宋体"}]{#struct_0_18947_x5086_x672415703}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1302028367}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x1852585784}[配置当前设备]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中的共享区域所占比例为]{style="font-family:宋体"}[50%]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x298746135}

[\[Sysname\] buffer egress cell total-shared ratio 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x526053503}[配置]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板的]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中共享区域所占比例为]{style="font-family:宋体"}[65%]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x2112266684}

[\[Sysname\] buffer egress slot 2 cell total-shared ratio 65]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x431919042}[配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中共享区域所占比例为]{style="font-family:宋体"}[65%]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_x1399844047}

[\[Sysname\] buffer egress slot 2 cell total-shared ratio 65]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_727261634}[配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板的]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源中共享区域所占比例为]{style="font-family:宋体"}[65%]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_1950012921}

[\[Sysname\] buffer egress chassis 2 slot 2 cell total-shared ratio 65]{lang="EN-US"}
:::

::: {#-1363566561 .myid}
[]{#_Toc404792081}[]{#struct_0_18947_x5086_128007133}[]{#_Toc307922392}[]{#_Toc291750142}[]{#_Toc263760090}[]{#_Toc226262757}[]{#_Toc205200257}[]{#_Toc153620361}[]{#_Toc319071751}

**数据缓冲区 \-- 数据缓冲区配置命令 \-- burst-mode enable**

------------------------------------------------------------------------

[**[burst-mode enable]{lang="EN-US"}**]{#struct_0_18947_x5086_x2044007410}[命令用来开启]{style="font-family:宋体"}[Burst]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo burst-mode enable]{lang="EN-US"}**]{#struct_0_18947_x5086_x222060905}[命令用来关闭]{style="font-family:宋体"}[Burst]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18947_x5086_101908596}

[**[burst-mode enable]{lang="EN-US"}**]{#struct_0_18947_x5086_1710908156}

[**[undo burst-mode enable]{lang="EN-US"}**]{#struct_0_18947_x5086_x1479694120}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x431984578}

[[Burst]{lang="EN-US"}]{#struct_0_18947_x5086_x183365497}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18947_x5086_76123033}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18947_x5086_x559835440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18947_x5086_357805057}

[[network-admin]{lang="EN-US"}]{#struct_0_18947_x5086_x1899942785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18947_x5086_x1295317000}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1105255397}

[[在下列情况下，]{style="font-family:宋体"}[Burst]{lang="EN-US"}]{#struct_0_18947_x5086_x647664854}[功能可以提供更好的报文缓存功能和流量转发性能：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[广播或者组播报文流量密集，瞬间突发大流量的网络环境中；]{style="font-family:宋体"}]{#struct_0_18947_x5086_x733987032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文从高速链路进入设备，由低速链路转发出去；或者报文从相同速率的多个接口同时进入设备，由一个相同速率的接口转发出去。]{style="font-family:宋体"}]{#struct_0_18947_x5086_x432050114}

[[用户可以通过开启]{style="font-family:宋体"}[Burst]{lang="EN-US"}]{#struct_0_18947_x5086_x1491476050}[功能，降低设备在上述特定环境中的报文丢包率，提高对报文的处理能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18947_x5086_1084734037}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_568805760}[开启]{style="font-family:宋体"}[Burst]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18947_x5086_1439351870}

[\[Sysname\] burst-mode enable]{lang="EN-US"}
:::

::: {#-2020356437 .myid}
[]{#_Toc404792082}[]{#struct_0_18947_x5086_1183228066}

**数据缓冲区 \-- 数据缓冲区配置命令 \-- display buffer**

------------------------------------------------------------------------

[**[display buffer]{lang="EN-US"}**]{#struct_0_18947_x5086_x1796222242}[命令显示数据缓冲区的大小。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x789448112}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18947_x5086_852795410}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display buffer ]{lang="EN-US"}**[\[ **slot** *slot-number* \] \[ **queue** \[ *queue-id* \] \]]{lang="EN-US"}]{#struct_0_18947_x5086_x432115650}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18947_x5086_x685401338}[模式：]{style="font-family:宋体"}

[**[display buffer ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \] \[ **queue** \[ *queue-id* \] \]]{lang="EN-US"}]{#struct_0_18947_x5086_x621758073}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x109205933}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18947_x5086_1380333508}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18947_x5086_491193082}

[[network-admin]{lang="EN-US"}]{#struct_0_18947_x5086_304148187}

[[network-operator]{lang="EN-US"}]{#struct_0_18947_x5086_852996212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18947_x5086_x303614009}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18947_x5086_x432181186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18947_x5086_44264813}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_718837791}[：取值只能为]{style="font-family:宋体"}[1]{lang="EN-US"}[，暂无意义。（集中式设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x1934443683}[：表示接口板所在的槽位号。不指定该参数时，表示所有接口板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x1610859059}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18947_x5086_x1761632629}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定接口板。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有接口板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[queue]{lang="EN-US"}**[ *queue-id*]{lang="EN-US"}]{#struct_0_18947_x5086_1503413728}[：表示队列的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。如果不指定]{style="font-family:
宋体"}*[queue-id]{lang="EN-US"}*[，表示所有队列。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x384979252}

[**[display buffer]{lang="EN-US"}**]{#struct_0_18947_x5086_x114748145}[命令不带]{style="font-family:宋体"}**[queue]{lang="EN-US"}**[关键字时，显示共享区域的大小。]{style="font-family:宋体"}

[**[display buffer]{lang="EN-US"}**]{#struct_0_18947_x5086_x431198146}[命令带]{style="font-family:宋体"}**[queue]{lang="EN-US"}**[关键字时，显示队列最多可使用的固定区域的大小以及队列最多可使用的共享区域的大小。其中，指定]{style="font-family:宋体"}*[queue-id]{lang="EN-US"}*[时，显示指定队列的相关信息，不指定]{style="font-family:宋体"}*[queue-id]{lang="EN-US"}*[时，显示所有队列的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1026652444}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x231358484}[显示数据缓冲区的大小。（不同型号的设备显示信息不同，请以设备的实际情况为准）（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display buffer]{lang="EN-US"}]{#struct_0_18947_x5086_698058514}

[Slot      Type          In(Total-shared)        Eg(Total-shared)]{lang="EN-US"}

[1         packet        24                      36]{lang="EN-US"}

[1         cell          50                      \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[          In: Size of the receiving buffer]{lang="EN-US"}

[          Eg: Size of the sending buffer]{lang="EN-US"}

[Total-shared: Size of the shared buffer for all ports]{lang="EN-US"}

[      Shared: Size of the maximum shared buffer per port]{lang="EN-US"}

[        Unit: Ratio]{lang="EN-US"}

[\<Sysname\> display buffer queue]{lang="EN-US"}

[Slot      Queue          Type       In(Guaranteed , Shared)     Eg(Guaranteed , Shared)]{lang="EN-US"}

[1         0-7            packet     256 , 128                   256 , 128]{lang="EN-US"}

[1         0-1,3-4,6-7    cell       256 , 128                   256 , 128]{lang="EN-US"}

[1         2,5            cell       512 , 128                   \-- , \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[        In: Size of the receiving buffer]{lang="EN-US"}

[        Eg: Size of the sending buffer]{lang="EN-US"}

[Guaranteed: Size of the minimum guaranteed buffer per queue]{lang="EN-US"}

[    Shared: Size of the maximum shared buffer per queue]{lang="EN-US"}

[[      Unit: Byte]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18947_x5086_1118085163}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_x431263682}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板数据缓冲区的大小。（不同型号的设备显示信息不同，请以设备的实际情况为准）（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display buffer chassis 1 slot 2]{lang="EN-US"}]{#struct_0_18947_x5086_x969255292}

[Slot      Type          In(Total-shared , Shared)        Eg(Total-shared , Shared)]{lang="EN-US"}

[1/2       packet        24 , 2                           36 , 2]{lang="EN-US"}

[1/2       cell          50 , 25                          \-- , \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[          In: Size of the receiving buffer]{lang="EN-US"}

[          Eg: Size of the sending buffer]{lang="EN-US"}

[Total-shared: Size of the shared buffer for all ports]{lang="EN-US"}

[      Shared: Size of the maximum shared buffer per port]{lang="EN-US"}

[        Unit: Ratio]{lang="EN-US"}

[\<Sysname\> display buffer chassis 1 slot 2 queue]{lang="EN-US"}

[Slot      Queue          Type       In(Guaranteed , Shared)     Eg(Guaranteed , Shared)]{lang="EN-US"}

[1/2       0-7            packet     256 , 128                   256 , 128]{lang="EN-US"}

[1/2       0-1,3-4,6-7    cell       256 , 128                   256 , 128]{lang="EN-US"}

[1/2       2,5            cell       512 , 128                   \-- , \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[        In: Size of the receiving buffer]{lang="EN-US"}

[        Eg: Size of the sending buffer]{lang="EN-US"}

[Guaranteed: Size of the minimum guaranteed buffer per queue]{lang="EN-US"}

[    Shared: Size of the maximum shared buffer per queue]{lang="EN-US"}

[      Unit: Byte]{lang="EN-US"}

[]{#struct_0_18947_x5086_x2078840928}[[表1-1 ]{lang="EN-US"}[display buffer]{lang="EN-US"}]{#_Ref318724271}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x514959688}[[字段]{style="font-family:黑体"}]{#struct_0_18947_x5086_x431722437}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18947_x5086_1368312815}

[[Slot]{lang="EN-US"}]{#struct_0_18947_x5086_x1953022682}

[[取值固定为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_18947_x5086_x1723370666}[（集中式设备）]{style="font-family:宋体"}

[[表示接口板所在的槽位号（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_18947_x5086_1972128222}

[[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18947_x5086_495554574}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[表示接口板所在的槽位号，其中第一维为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18947_x5086_x157562578}[中的成员编号，第二维为接口板在成员设备上的槽位号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_18947_x5086_x431787973}

[[缓冲区类型，包括]{style="font-family:宋体"}[packet]{lang="EN-US"}]{#struct_0_18947_x5086_1781171428}[资源和]{style="font-family:宋体"}[cell]{lang="EN-US"}[资源]{style="font-family:宋体"}

[[Queue]{lang="EN-US"}]{#struct_0_18947_x5086_x193729553}

[[队列]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18947_x5086_x499839790}[，范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}

[[In]{lang="EN-US"}]{#struct_0_18947_x5086_x599782083}

[[Ingress]{lang="EN-US"}]{#struct_0_18947_x5086_x478528231}[，入方向的数据缓冲区配置]{style="font-family:宋体"}

[[Eg]{lang="EN-US"}]{#struct_0_18947_x5086_x431853509}

[[Egress]{lang="EN-US"}]{#struct_0_18947_x5086_606427058}[，出方向的数据缓冲区配置]{style="font-family:宋体"}

[[(Total-shared)]{lang="EN-US"}]{#struct_0_18947_x5086_x2062469619}

[[共享区域的大小。如果显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_18947_x5086_1879241279}["字符串，则表示设备不支持该缓冲区]{style="font-family:宋体"}

[[(Guaranteed , Shared)]{lang="EN-US"}]{#struct_0_18947_x5086_238731439}

[[Guaranteed]{lang="EN-US"}]{#struct_0_18947_x5086_x1452065599}[表示最多可使用的固定区域的大小。如果显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["字符串，则表示设备不支持该数据缓冲区]{style="font-family:宋体"}

[[Shared]{lang="EN-US"}]{#struct_0_18947_x5086_x431919045}[对应表示最多可使用的共享区域的大小。如果显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["字符串，则表示设备不支持该数据缓冲区]{style="font-family:宋体"}

[[Unit]{lang="EN-US"}]{#struct_0_18947_x5086_x1399647439}

[[数据缓冲区的单位，为]{style="font-family:宋体"}[%]{lang="EN-US"}]{#struct_0_18947_x5086_2125311948}[或]{style="font-family:宋体"}[byte]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#592272944 .myid}
[]{#_Toc404792083}[]{#struct_0_18947_x5086_x863986861}

**数据缓冲区 \-- 数据缓冲区配置命令 \-- display buffer usage**

------------------------------------------------------------------------

[**[display buffer usage]{lang="EN-US"}**]{#struct_0_18947_x5086_2131090757}[命令用来显示数据缓冲区的使用率。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1693906785}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18947_x5086_679684140}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display buffer]{lang="EN-US"}**[ **usage** \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_18947_x5086_1502070676}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18947_x5086_x431984581}[模式：]{style="font-family:宋体"}

[**[display buffer]{lang="EN-US"}**[ **usage** \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_18947_x5086_x182906732}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18947_x5086_890777220}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18947_x5086_x220900294}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x1352597050}

[[network-admin]{lang="EN-US"}]{#struct_0_18947_x5086_2050225434}

[[network-operator]{lang="EN-US"}]{#struct_0_18947_x5086_x1334390458}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18947_x5086_826175405}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18947_x5086_1564819385}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18947_x5086_x432050117}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x1491279442}[：取值只能为]{style="font-family:宋体"}[1]{lang="EN-US"}[，表示显示当前设备的]{style="font-family:宋体"}[数据缓冲区的使用率]{style="font-family:宋体"}[。（集中式设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_1055433607}[：表示接口板所在的槽位号。不指定该参数时，表示所有接口板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18947_x5086_x1237399876}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18947_x5086_x207600567}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的指定接口板。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有接口板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18947_x5086_2091119014}

[[\# ]{lang="EN-US"}]{#struct_0_18947_x5086_1009332823}[显示数据缓冲区的使用率]{style="font-family:宋体"}[。（不同型号的设备显示信息不同，请以设备的实际情况为准）]{style="font-family:宋体"}

[[\<Sysname\> display buffer usage]{lang="EN-US"}]{#struct_0_18947_x5086_2000108249}

[Egress total-shared cell buffer usage for slot 1:]{lang="EN-US"}

[         4% in last 5 seconds]{lang="EN-US"}

[        16% in last 1 minute]{lang="EN-US"}

[        14% in last 5 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
