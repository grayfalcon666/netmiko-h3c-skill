::::: {#-1914678111 .myid}
[]{#struct_0_x7131_45285_x1174679304}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404800509}[]{#_Toc384916010}

**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog host**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心Probe命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7131_45285_x1225384719}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7131_45285_x246951022}
:::

[ ]{lang="EN-US"}

[**[display system internal customlog host]{lang="EN-US"}**]{#struct_0_x7131_45285_x2026404276}[命令用来显示指定日志主机当前运行状态下的内核数据信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x703220323}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7131_45285_1437921469}

[**[display system internal customlog host ]{lang="EN-US"}***[index]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW \|  cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** }]{lang="EN-US"}]{#struct_0_x7131_45285_x1719361701}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7131_45285_x1167153341}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal customlog host ]{lang="EN-US"}***[index]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW \|  cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_x673067205}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7131_45285_925452449}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal customlog host ]{lang="EN-US"}***[index]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW \|  cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_x973049821}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7131_45285_923002922}

[[Probe]{lang="EN-US"}]{#struct_0_x7131_45285_1874617058}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7131_45285_1708948423}

[[network-admin]{lang="EN-US"}]{#struct_0_x7131_45285_x198916196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7131_45285_x590082103}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x325305334}

[*[index]{lang="EN-US"}*]{#struct_0_x7131_45285_x1413504215}[：表示指定日志主机的索引号。]{style="font-family:宋体;color:black"}*[index]{lang="EN-US" style="color:black"}*[取值范围为]{style="font-family:宋体;
color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[3]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[**[cmccPortA]{lang="EN-US"}**]{#struct_0_x7131_45285_x1614931599}**[：]{style="font-family:宋体"}**[指定中国移动公司的端口创建日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[cmccPortF]{lang="EN-US"}**]{#struct_0_x7131_45285_x1844192980}**[：]{style="font-family:宋体"}**[指定中国移动公司的端口资源不足日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[cmccPortW]{lang="EN-US"}**]{#struct_0_x7131_45285_1176551077}**[：]{style="font-family:宋体"}**[指定中国移动公司的端口删除日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[cmccSessionA]{lang="EN-US"}**]{#struct_0_x7131_45285_2055978948}**[：]{style="font-family:宋体"}**[指定中国移动公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[创建日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[cmccSessionW]{lang="EN-US"}**]{#struct_0_x7131_45285_x2012824549}**[：]{style="font-family:宋体"}**[指定中国移动公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[删除日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[portA]{lang="EN-US"}**]{#struct_0_x7131_45285_x1783316941}**[：]{style="font-family:宋体"}**[指定中国联通公司的端口创建日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[portW]{lang="EN-US"}**]{#struct_0_x7131_45285_1880653090}**[：]{style="font-family:宋体"}**[指定中国联通公司的端口删除日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[sessionA]{lang="EN-US"}**]{#struct_0_x7131_45285_x226950500}**[：]{style="font-family:宋体"}**[指定中国联通公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[创建日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[sessionW]{lang="EN-US"}**]{#struct_0_x7131_45285_x1369505347}**[：]{style="font-family:宋体"}**[指定中国联通公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[删除日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[sessionbasedA]{lang="EN-US"}**]{#struct_0_x7131_45285_x1777569302}**[：]{style="font-family:宋体"}**[指定中国电信公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[创建日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[sessionbasedW ]{lang="EN-US"}**]{#struct_0_x7131_45285_x1890760483}**[：]{style="font-family:宋体"}**[指定中国电信公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[删除日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[userbasedA]{lang="EN-US"}**]{#struct_0_x7131_45285_x1167153342}**[：]{style="font-family:宋体"}**[指定中国电信公司的端口创建日志，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[userbasedF]{lang="EN-US"}**]{#struct_0_x7131_45285_x269782678}**[：]{style="font-family:宋体"}**[指定中国电信公司的端口资源不足日志类型，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[userbasedW]{lang="EN-US"}**]{#struct_0_x7131_45285_1413941916}**[：]{style="font-family:宋体"}**[指定中国电信公司的端口删除日志，并显示日志对应的内核数据信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_x768307356}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如未指定该参数，则显示当前日志主机主控板运行状态下的内核数据信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_x1045475014}[：显示指定成员设备上的内核数据信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如未指定该参数，则显示当前日志主机主控板运行状态下的内核数据信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_1603476456}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的内核数据信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如未指定该参数，则显示当前日志主机主控板运行状态下的内核数据信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_x108417135}[：显示指定成员设备和单板上的内核数据信息。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。]{style="font-family:宋体;
color:black"}[如未指定该参数，则显示当前日志主机全局主用主控板运行状态下的内核数据信息。[（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_2016414872}[：显示指定单板上的内核数据信息。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所[在的槽位号。如未指定该参数，则显示当前日志主机全局主用主控板运行状态下的内核数据信息。（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_x7131_45285_x1719578828}[：指定]{style="font-family:宋体;color:black"}[需要显示信息的成员设备所在[的]{style="color:black"}]{style="font-family:宋体"}[CPU]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="color:black"}。]{style="font-family:宋体"}
:::::

::::: {#1600225130 .myid}
[]{#_Toc404800510}[]{#struct_0_x7131_45285_x246271012}[]{#_Toc388598672}[]{#_Toc388598861}[]{#_Toc388598673}[]{#_Toc388598862}[]{#_Toc388598674}[]{#_Toc388598863}[]{#_Toc388598680}[]{#_Toc388598869}[]{#_Toc388598681}[]{#_Toc388598870}[]{#_Toc388598682}[]{#_Toc388598871}[]{#_Toc388598683}[]{#_Toc388598872}[]{#_Toc388598684}[]{#_Toc388598873}[]{#_Toc388598685}[]{#_Toc388598874}[]{#_Toc388598686}[]{#_Toc388598875}[]{#_Toc388598688}[]{#_Toc388598877}[]{#_Toc388598689}[]{#_Toc388598878}[]{#_Toc388598690}[]{#_Toc388598879}[]{#_Toc388598691}[]{#_Toc388598880}[]{#_Toc388598692}[]{#_Toc388598881}[]{#_Toc388598693}[]{#_Toc388598882}[]{#_Toc388598694}[]{#_Toc388598883}[]{#_Toc388598695}[]{#_Toc388598884}[]{#_Toc388598696}[]{#_Toc388598885}[]{#_Toc388598697}[]{#_Toc388598886}[]{#_Toc388598698}[]{#_Toc388598887}[]{#_Toc388598699}[]{#_Toc388598888}[]{#_Toc388598700}[]{#_Toc388598889}[]{#_Toc388598701}[]{#_Toc388598890}[]{#_Toc388598702}[]{#_Toc388598891}[]{#_Toc388598703}[]{#_Toc388598892}[]{#_Toc388598704}[]{#_Toc388598893}[]{#_Toc388598705}[]{#_Toc388598894}[]{#_Toc388598706}[]{#_Toc388598895}[]{#_Toc388598707}[]{#_Toc388598896}[]{#_Toc388598708}[]{#_Toc388598897}[]{#_Toc388598711}[]{#_Toc388598900}[]{#_Toc388598712}[]{#_Toc388598901}[]{#_Toc388598713}[]{#_Toc388598902}[]{#_Toc388598714}[]{#_Toc388598903}[]{#_Toc388598715}[]{#_Toc388598904}[]{#_Toc388598716}[]{#_Toc388598905}

**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog mbuf dump**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心Probe命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7131_45285_x2021817018}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7131_45285_x1180667485}
:::

[ ]{lang="EN-US" style="color:blue"}

[**[display system internal customlog mbuf dump]{lang="EN-US"}**]{#struct_0_x7131_45285_x155845309}[命令用来显示指定个数的]{style="font-family:宋体"}[CUSTOMLOG]{lang="EN-US"}[报文的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x1420252154}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_x7131_45285_x903678083}

[**[display system internal customlog mbuf dump count ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x7131_45285_1147836036}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7131_45285_1072138029}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal customlog mbuf dump count ]{lang="EN-US"}***[number]{lang="EN-US"}*[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_x183726066}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7131_45285_x277205439}[模式：]{style="font-family:宋体"}

[**[display system internal customlog mbuf dump count ]{lang="EN-US"}***[number]{lang="EN-US"}*[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_187588523}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7131_45285_1726058961}

[[Probe]{lang="EN-US"}]{#struct_0_x7131_45285_490133693}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7131_45285_2119301115}

[[network-admin]{lang="EN-US"}]{#struct_0_x7131_45285_1961919333}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7131_45285_x1167153343}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x1835866619}

[*[number]{lang="EN-US"}*]{#struct_0_x7131_45285_x1019472991}[：指定需要显示的日志个数。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_305877581}[：显示指定单板上]{style="font-family:宋体"}[CUSTOMLOG]{lang="EN-US"}[报文的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_x1943808596}[：显示指定成员设备上]{style="font-family:宋体"}[CUSTOMLOG]{lang="EN-US"}[报文的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_84446682}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[CUSTOMLOG]{lang="EN-US"}[报文的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_424438232}[：显示指定成员设备和单板的]{style="font-family:宋体"}[CUSTOMLOG]{lang="EN-US"}[报文的详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_x1011623496}[：显示指定单板的]{style="font-family:宋体"}[CUSTOMLOG]{lang="EN-US"}[报文的详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x7131_45285_55788924}[：指定需要显示信息的成员设备所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::::: {#-1390934657 .myid}
[]{#_Toc404800511}[]{#struct_0_x7131_45285_1293028852}[]{#_Toc384916011}[]{#_Toc388598718}[]{#_Toc388598907}[]{#_Toc388598719}[]{#_Toc388598908}[]{#_Toc388598763}[]{#_Toc388598952}[]{#_Toc388598764}[]{#_Toc388598953}[]{#_Toc388598766}[]{#_Toc388598955}[]{#_Toc388598767}[]{#_Toc388598956}[]{#_Toc388598768}[]{#_Toc388598957}[]{#_Toc388598769}[]{#_Toc388598958}[]{#_Toc388598771}[]{#_Toc388598960}[]{#_Toc388598772}[]{#_Toc388598961}[]{#_Toc388598773}[]{#_Toc388598962}[]{#_Toc388598774}[]{#_Toc388598963}[]{#_Toc388598775}[]{#_Toc388598964}[]{#_Toc388598776}[]{#_Toc388598965}[]{#_Toc388598777}[]{#_Toc388598966}[]{#_Toc388598778}[]{#_Toc388598967}[]{#_Toc388598779}[]{#_Toc388598968}[]{#_Toc388598780}[]{#_Toc388598969}[]{#_Toc388598781}[]{#_Toc388598970}[]{#_Toc388598782}[]{#_Toc388598971}[]{#_Toc388598783}[]{#_Toc388598972}[]{#_Toc388598784}[]{#_Toc388598973}[]{#_Toc388598785}[]{#_Toc388598974}

**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog mbuf usage**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心Probe命令.files/image002.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7131_45285_x1954565160}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7131_45285_x729278714}
:::

[ ]{lang="EN-US"}

[**[display system internal customlog mbuf usage]{lang="EN-US"}**]{#struct_0_x7131_45285_x1662605938}[命令用来显示指定日志主机上每个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池的使用情况信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x121857587}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_x7131_45285_x1806004919}

[**[display system internal customlog mbuf usage ]{lang="EN-US"}***[index]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** }]{lang="EN-US"}]{#struct_0_x7131_45285_x265747439}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7131_45285_x1831775833}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal customlog mbuf usage ]{lang="EN-US"}***[index]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_1413863506}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7131_45285_358852172}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal customlog mbuf usage ]{lang="EN-US"}***[index]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA \| cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA** \| **sessionbasedW  **\| **userbasedA \| userbasedF** \| **userbasedW** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_x1753291795}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7131_45285_1211025581}

[[Probe]{lang="EN-US"}]{#struct_0_x7131_45285_x2102566162}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7131_45285_1439866807}

[[network-admin]{lang="EN-US"}]{#struct_0_x7131_45285_x1547621667}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7131_45285_x1167153344}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x1076351732}

[*[index]{lang="EN-US"}*]{#struct_0_x7131_45285_8681698}[：指定需要查看数据的日志主机索引号。]{style="font-family:宋体;color:black"}*[index]{lang="EN-US" style="color:black"}*[取值范围为]{style="font-family:宋体;
color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[3]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[**[cmccPortA]{lang="EN-US"}**]{#struct_0_x7131_45285_784384932}**[：]{style="font-family:宋体"}**[指定中国移动公司的端口创建日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[cmccPortF]{lang="EN-US"}**]{#struct_0_x7131_45285_795755721}**[：]{style="font-family:宋体"}**[指定中国移动公司的端口资源不足日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[cmccPortW]{lang="EN-US"}**]{#struct_0_x7131_45285_x245441876}**[：]{style="font-family:宋体"}**[指定中国移动公司的端口删除日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[cmccSessionA]{lang="EN-US"}**]{#struct_0_x7131_45285_1257473518}**[：]{style="font-family:宋体"}**[指定中国移动公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[创建日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[cmccSessionW]{lang="EN-US"}**]{#struct_0_x7131_45285_x1068448069}**[：]{style="font-family:宋体"}**[指定中国移动公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[删除日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[portA]{lang="EN-US"}**]{#struct_0_x7131_45285_1663435617}**[：]{style="font-family:宋体"}**[指定中国联通公司的端口创建日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[portW]{lang="EN-US"}**]{#struct_0_x7131_45285_375757391}**[：]{style="font-family:宋体"}**[指定中国联通公司的端口删除日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[sessionA]{lang="EN-US"}**]{#struct_0_x7131_45285_718913313}**[：]{style="font-family:宋体"}**[指定中国联通公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[创建日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[sessionW]{lang="EN-US"}**]{#struct_0_x7131_45285_x1084102347}**[：]{style="font-family:宋体"}**[指定中国联通公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[删除日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[sessionbasedA]{lang="EN-US"}**]{#struct_0_x7131_45285_x713735997}**[：]{style="font-family:宋体"}**[指定中国电信公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[创建日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[sessionbasedW ]{lang="EN-US"}**]{#struct_0_x7131_45285_1185624215}**[：]{style="font-family:宋体"}**[指定中国电信公司的]{style="font-family:宋体"}[session]{lang="EN-US"}[删除日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[userbasedA]{lang="EN-US"}**]{#struct_0_x7131_45285_1535658395}**[：]{style="font-family:宋体"}**[指定中国电信公司的端口创建日志，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[userbasedF]{lang="EN-US"}**]{#struct_0_x7131_45285_x297092679}**[：]{style="font-family:宋体"}**[指定中国电信公司的端口资源不足日志类型，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[userbasedW]{lang="EN-US"}**]{#struct_0_x7131_45285_x1866187768}**[：]{style="font-family:宋体"}**[指定中国电信公司的端口删除日志，并显示日志对应的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池使用情况信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_2000418585}[：显示指定单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池的使用情况信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。]{style="font-family:宋体"}[如未指定该参数，则显示当前日志主机主控板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[使用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_1382530237}[：显示指定成员设备上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池的使用情况信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如未指定该参数，则显示当前日志主控板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[使用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7131_45285_843633889}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[池的使用情况信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如未指定该参数，则显示当前日志主控板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[使用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_x1999472946}[：显示指定成员设备和单板上的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[内]{style="font-family:宋体;color:black"}[MBUF]{lang="EN-US" style="color:black"}[池的使用情况信息]{style="font-family:宋体;
color:black"}[。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。]{style="font-family:宋体;
color:black"}[如未指定该参数，则显示当前日志主机主控板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[内]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[使用情况。[（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备]{style="font-family:宋体;color:black"}[）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_x184364060}[：显示指定单板上的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[内]{style="font-family:宋体;color:black"}[MBUF]{lang="EN-US" style="color:black"}[池的使用情况信息]{style="font-family:宋体;
color:black"}[。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如未指定该参数，则显示当前日志主机主控板上]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[内]{style="font-family:宋体;
color:black"}[MBUF]{lang="EN-US" style="color:black"}[使用情况。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备]{style="font-family:宋体;
color:black"}[）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_x7131_45285_x991605795}[：指定]{style="font-family:宋体;color:black"}[需要显示信息的成员设备所在[的]{style="color:black"}]{style="font-family:宋体"}[CPU]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为]{style="color:black"}准。]{style="font-family:宋体"}
:::::

::::: {#1369281453 .myid}
[]{#_Toc404800512}[]{#struct_0_x7131_45285_1258456127}[]{#_Toc384916013}[]{#_Toc388598787}[]{#_Toc388598976}[]{#_Toc388598788}[]{#_Toc388598977}[]{#_Toc388598789}[]{#_Toc388598978}[]{#_Toc388598794}[]{#_Toc388598983}[]{#_Toc388598797}[]{#_Toc388598986}[]{#_Toc388598800}[]{#_Toc388598989}[]{#_Toc388598803}[]{#_Toc388598992}[]{#_Toc388598806}[]{#_Toc388598995}[]{#_Toc388598809}[]{#_Toc388598998}[]{#_Toc388598812}[]{#_Toc388599001}[]{#_Toc388598815}[]{#_Toc388599004}[]{#_Toc388598816}[]{#_Toc388599005}[]{#_Toc388598817}[]{#_Toc388599006}[]{#_Toc388598818}[]{#_Toc388599007}[]{#_Toc388598819}[]{#_Toc388599008}[]{#_Toc388598820}[]{#_Toc388599009}[]{#_Toc388598821}[]{#_Toc388599010}[]{#_Toc388598823}[]{#_Toc388599012}[]{#_Toc388598824}[]{#_Toc388599013}[]{#_Toc388598825}[]{#_Toc388599014}[]{#_Toc388598826}[]{#_Toc388599015}[]{#_Toc388598827}[]{#_Toc388599016}[]{#_Toc388598828}[]{#_Toc388599017}[]{#_Toc388598829}[]{#_Toc388599018}[]{#_Toc388598830}[]{#_Toc388599019}[]{#_Toc388598831}[]{#_Toc388599020}[]{#_Toc388598832}[]{#_Toc388599021}[]{#_Toc388598833}[]{#_Toc388599022}[]{#_Toc388598834}[]{#_Toc388599023}[]{#_Toc388598835}[]{#_Toc388599024}[]{#_Toc388598836}[]{#_Toc388599025}[]{#_Toc388598837}[]{#_Toc388599026}[]{#_Toc388598838}[]{#_Toc388599027}[]{#_Toc388598839}[]{#_Toc388599028}[]{#_Toc388598840}[]{#_Toc388599029}[]{#_Toc388598841}[]{#_Toc388599030}[]{#_Toc388598842}[]{#_Toc388599031}[]{#_Toc388598843}[]{#_Toc388599032}[]{#_Toc388598844}[]{#_Toc388599033}[]{#_Toc388598846}[]{#_Toc388599035}[]{#_Toc388598847}[]{#_Toc388599036}[]{#_Toc388598848}[]{#_Toc388599037}[]{#_Toc388598849}[]{#_Toc388599038}[]{#_Toc388598850}[]{#_Toc388599039}[]{#_Toc388598851}[]{#_Toc388599040}[]{#_Toc388598852}[]{#_Toc388599041}[]{#_Toc388598853}[]{#_Toc388599042}

**信息中心 \-- 信息中心Probe命令 \-- display system internal customlog test**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信息中心Probe命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7131_45285_291793133}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7131_45285_1481933501}
:::

[ ]{lang="EN-US"}

[**[display system internal customlog test]{lang="EN-US"}**]{#struct_0_x7131_45285_963772848}[命令用来发送指定数目]{style="font-family:宋体"}[CUSTOMLOG]{lang="EN-US"}[测试的报文，并显示日志发送结果信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7131_45285_1228068785}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_x7131_45285_1974130864}

[**[display system internal customlog test count ]{lang="EN-US"}***[number ]{lang="EN-US"}*[{ **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** }]{lang="EN-US"}]{#struct_0_x7131_45285_x1167153345}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7131_45285_1652531623}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal customlog test count ]{lang="EN-US"}***[number]{lang="EN-US"}*[ { **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_1219669972}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7131_45285_x385207015}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal customlog test count ]{lang="EN-US"}***[number]{lang="EN-US"}*[ { **cmccPortA** \| **cmccPortF** \| **cmccPortW** \| **cmccSessionA** \| **cmccSessionW** \| **portA** \| **portW** \| **sessionA** \| **sessionW** \| **sessionbasedA \| sessionbasedW** \| **userbasedA** \| **userbasedF** \| **userbasedW** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7131_45285_x1722113512}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x813365192}

[[Probe]{lang="EN-US"}]{#struct_0_x7131_45285_x446943210}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7131_45285_1364827417}

[[network-admin]{lang="EN-US"}]{#struct_0_x7131_45285_1472955136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7131_45285_1835700656}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7131_45285_x856615745}

[*[number]{lang="EN-US"}*]{#struct_0_x7131_45285_x70014008}[：指定需要参与测试的]{style="font-family:宋体;color:black"}[CUSTOMLOG]{lang="EN-US" style="color:black"}[数目。]{style="font-family:宋体;
color:black"}*[number]{lang="EN-US" style="color:black"}*[取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[100]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}

[**[cmccPortA]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x746422262}**[：]{style="font-family:宋体;color:black"}**[指定中国移动公司的端口创建日志类型，并显示日志对应的]{style="font-family:宋体;
color:black"}[测试日志发送结果信息。]{style="font-family:宋体;
color:black"}

[**[cmccPortF]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x1729681379}**[：]{style="font-family:宋体;color:black"}**[指定中国移动公司的端口资源不足日志类型，并显示日志对应的]{style="font-family:宋体;
color:black"}[测试日志发送结果信息。]{style="font-family:宋体;
color:black"}

[**[cmccPortW]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_1843178831}**[：]{style="font-family:宋体;color:black"}**[指定中国移动公司的端口删除日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;
color:black"}

[**[cmccSessionA]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x740431730}**[：]{style="font-family:宋体;color:black"}**[指定中国移动公司的]{style="font-family:宋体;
color:black"}[session]{lang="EN-US" style="color:black"}[创建日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[cmccSessionW]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x2133228053}**[：]{style="font-family:宋体;color:black"}**[指定中国移动公司的]{style="font-family:宋体;
color:black"}[session]{lang="EN-US" style="color:black"}[删除日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[portA]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_1071051944}**[：]{style="font-family:
宋体;color:black"}**[指定中国联通公司的端口创建日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[portW]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x1616789392}**[：]{style="font-family:
宋体;color:black"}**[指定中国联通公司的端口删除日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[sessionA]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x746422261}**[：]{style="font-family:宋体;color:black"}**[指定中国联通公司的]{style="font-family:宋体;
color:black"}[session]{lang="EN-US" style="color:black"}[创建日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[sessionW]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x1729484771}**[：]{style="font-family:宋体;color:black"}**[指定中国联通公司的]{style="font-family:宋体;
color:black"}[session]{lang="EN-US" style="color:black"}[删除日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[sessionbasedA]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x2143680397}**[：]{style="font-family:宋体;color:black"}**[指定中国电信公司的]{style="font-family:宋体;
color:black"}[session]{lang="EN-US" style="color:black"}[创建日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[sessionbasedW ]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x1631936607}**[：]{style="font-family:宋体;color:black"}**[指定中国电信公司的]{style="font-family:宋体;
color:black"}[session]{lang="EN-US" style="color:black"}[删除日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;color:black"}

[**[userbasedA]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x836714026}**[：]{style="font-family:宋体;color:black"}**[指定中国电信公司的端口创建日志，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;
color:black"}

[**[userbasedF]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x544403380}**[：]{style="font-family:宋体;color:black"}**[指定中国电信公司的端口资源不足日志类型，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;
color:black"}

[**[userbasedW]{lang="EN-US" style="color:black"}**]{#struct_0_x7131_45285_x1842373446}**[：]{style="font-family:宋体;color:black"}**[指定中国电信公司的端口删除日志，并显示日志对应的测试日志发送结果信息。]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_x1195249450}[：显示指定单板上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在槽位号。]{style="font-family:宋体;color:black"}[如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。[（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:
宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_1602012927}[：显示指定成员设备上的日志发送结果信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。]{style="font-family:宋体;color:black"}[如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。[（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_37064835}[：显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US"}[上的日志发送结果信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号[。如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。（集中式]{style="color:
black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_x1061733707}[：显示指定成员设备和单板上的日志发送结果信息。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。]{style="font-family:宋体;
color:black"}[如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。[（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x7131_45285_211066708}[：显示指定单板上的日志发送结果信息。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如未指定该参数，则显示当前日志主机主控板上日志报文的发送结果信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_x7131_45285_1775293338}[：指定]{style="font-family:宋体;color:black"}[需要显示信息的成员设备所在[的]{style="color:black"}]{style="font-family:宋体"}[CPU]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::::
