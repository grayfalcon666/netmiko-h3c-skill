::: {#1310668221 .myid}
[]{#_Toc275248925}[]{#_Toc67195986}[]{#_Toc67145811}[]{#_Toc61012174}[]{#_Toc404790487}[]{#struct_0_24739_x6658_1023900908}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls forwarding ilm**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mpls forwarding ilm**]{lang="EN-US"}]{#struct_0_24739_x6658_650457785}[命令用来显示]{style="font-family:宋体"}[ILM]{lang="EN-US"}[（]{style="font-family:宋体"}[Incoming Label Map]{lang="EN-US"}[，入标签映射）表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1864852333}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1539359749}

[**[display mpls forwarding ilm ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ ]{lang="EN-US"}***[label ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_24739_x6658_981988368}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_24739_x6658_x814168612}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mpls forwarding ilm ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ ]{lang="EN-US"}***[label ]{lang="EN-US"}*[\]]{lang="EN-US"}[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_24739_x6658_x1777633549}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_24739_x6658_740353240}[模式：]{style="font-family:宋体"}

[**[display mpls forwarding ilm]{lang="EN-US"}**[ \[ *label* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_24739_x6658_x182574965}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_895686457}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_2059431225}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_26715259}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_303923901}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_283655315}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1750762149}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_1621057861}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_740287704}

[*[label]{lang="EN-US"}*]{#struct_0_24739_x6658_x963090111}[：显示指定入标签的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项，不同型号的设备支持的取值范围不同，请以设备的实际情况为准]{style="font-family:宋体"}[。如果不指定本参数，]{style="font-family:宋体"}[则显示所有]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_24739_x6658_1920606303}*[ slot-number]{lang="PT-BR"}***[：]{style="font-family:宋体"}**[显示指定单板上的]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。如果不指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_24739_x6658_x1630013796}[：显示指定成员设备上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_24739_x6658_1206220316}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_24739_x6658_251349608}*[chassis-number]{lang="PT-BR"}*[ **slot** *slot-number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备主用主控板上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_24739_x6658_x1454365653}*[chassis-number]{lang="PT-BR"}*[ **slot** *slot-number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备主用主控板上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_24739_x6658_328080475}[：显示指定]{style="font-family:宋体"}[CP]{lang="EN-US"}[U]{lang="EN-US"}[的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1839734187}

[[ILM]{lang="EN-US"}]{#struct_0_24739_x6658_944667211}[用于根据入标签查找对应的标签操作类型、出标签值等。]{style="font-family:宋体"}[LSR]{lang="EN-US"}[接收到带有标签的报文后，根据报文中的栈顶标签值查找对应的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项，执行相应的标签操作，并转发该报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_586971141}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1036994549}[显示指定入标签的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> display mpls forwarding ilm 30]{lang="EN-US"}]{#struct_0_24739_x6658_739828953}

[Flags: T - Forwarded through a tunnel]{lang="EN-US"}

[       N - Forwarded through the outgoing interface to the nexthop IP address]{lang="EN-US"}

[       B - Backup forwarding information]{lang="EN-US"}

[       A - Active forwarding information]{lang="EN-US"}

[ ]{lang="EN-US"}

[InLabel Oper    VRF   Flag SwapLabel Forwarding Info]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[30      SWAP    0     T    1300      1024]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1464916621}[显示所有]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> display mpls forwarding ilm]{lang="EN-US"}]{#struct_0_24739_x6658_787671744}

[Total ILM entries: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flags: T - Forwarded through a tunnel]{lang="EN-US"}

[       N - Forwarded through the outgoing interface to the nexthop IP address]{lang="EN-US"}

[       B - Backup forwarding information]{lang="EN-US"}

[       A - Active forwarding information]{lang="EN-US"}

[ ]{lang="EN-US"}

[InLabel Oper    VRF   Flag SwapLabel Forwarding Info]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[30      SWAP    0     T    1300      1024]{lang="EN-US"}

[1279    POP     0     -    -         -]{lang="EN-US"}

[1407    SWAP    0     NA   1271      GE1/0/3                   50.2.0.2]{lang="EN-US"}

[                      NB   1270      Tun0                     0.0.0.0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mpls forwarding ilm]{lang="EN-US"}]{#struct_0_24739_x6658_739763417}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x667035442}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_229904490}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1730011496}

[[Total ILM entries]{lang="EN-US"}]{#struct_0_24739_x6658_x2138776989}

[[ILM]{lang="EN-US"}]{#struct_0_24739_x6658_177735345}[表项总数]{style="font-family:宋体"}

[[InLabel]{lang="EN-US"}]{#struct_0_24739_x6658_x1483822649}

[[入标签]{style="font-family:宋体"}]{#struct_0_24739_x6658_x376906773}

[[Oper]{lang="EN-US"}]{#struct_0_24739_x6658_739697881}

[[操作类型，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_1876990777}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[POP]{lang="EN-US"}]{#struct_0_24739_x6658_424621027}[：弹出标签]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[POPGO]{lang="EN-US"}]{#struct_0_24739_x6658_x68145380}[：弹出标签，并将报文转发到另一条隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SWAP]{lang="EN-US"}]{#struct_0_24739_x6658_x1886007218}[：交换标签]{lang="EN-US" style="font-family:宋体"}

[[VRF]{lang="EN-US"}]{#struct_0_24739_x6658_1599305891}

[[VPN]{lang="EN-US"}]{#struct_0_24739_x6658_739632345}[实例的索引]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_24739_x6658_629072122}

[[转发标记，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_59950472}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_24739_x6658_x1240285945}[：隧道转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_24739_x6658_1126606125}[：出接口]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[下一跳转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_24739_x6658_941967974}[：备份转发信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_24739_x6658_740091097}[：在用转发信息]{style="font-family:宋体"}

[[SwapLabel]{lang="EN-US"}]{#struct_0_24739_x6658_x22607028}

[[交换的标签值，即出标签值]{style="font-family:宋体"}]{#struct_0_24739_x6658_209846380}

[[Forwarding Info]{lang="EN-US"}]{#struct_0_24739_x6658_x1959268641}

[[转发信息]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1966169397}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[转发标记为]{style="font-family:宋体"}]{#struct_0_24739_x6658_740025561}[N]{lang="EN-US"}[时，转发信息为出接口和下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[转发标记为]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1210756824}[T]{lang="EN-US"}[时，转发信息为]{style="font-family:宋体"}[NID]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#466178914 .myid}
[]{#_Toc404790488}[]{#struct_0_24739_x6658_199354560}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls forwarding nhlfe**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mpls forwarding nhlfe**]{lang="EN-US"}]{#struct_0_24739_x6658_328775131}[命令用来显示]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[（]{style="font-family:宋体"}[Next Hop Label Forwarding Entry]{lang="EN-US"}[，下一跳标签转发项）表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x843324497}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1127793014}

[**[display mpls forwarding nhlfe ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ ]{lang="EN-US"}***[nid]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_24739_x6658_x929418366}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_24739_x6658_739960025}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mpls forwarding nhlfe ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ ]{lang="EN-US"}***[nid]{lang="EN-US"}*[ \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_24739_x6658_1229864444}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_24739_x6658_x1879941008}[模式：]{style="font-family:宋体"}

[**[display mpls forwarding nhlfe]{lang="EN-US"}**[ \[ *nid* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_24739_x6658_37405599}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1932767921}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x703981988}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1254005143}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_1412464564}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_350017291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_739894489}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x367848843}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1024359660}

[*[nid]{lang="EN-US"}*]{#struct_0_24739_x6658_x1130410636}[：显示指定]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}*[nid]{lang="EN-US"}*[为]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定本参数，则显示所有]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_24739_x6658_1868815319}[：显示指定单板上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。如果不指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_24739_x6658_x1630341477}[：显示指定成员设备上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_24739_x6658_x1119378512}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_24739_x6658_x1067738678}[：显示指定成员设备上指定单板的]{style="font-family:
宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备主用主控板上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_24739_x6658_1609504843}[：显示指定单板的]{style="font-family:
宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备主用主控板上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_24739_x6658_327818331}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1094396180}

[[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_568331557}[表项描述了标签的转发信息（如出标签、出接口等），]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项主要用于为报文添加多层标签的情况。需要为报文添加多层标签时，]{style="font-family:宋体"}[LSR]{lang="EN-US"}[首先通过]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项或]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项获取最内层标签和对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，然后根据]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引查找]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项，从该表项中获取报文的外层标签。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1816898960}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_740353241}[显示索引号为]{style="font-family:宋体"}[2048]{lang="EN-US"}[的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> display mpls forwarding nhlfe 2048]{lang="EN-US"}]{#struct_0_24739_x6658_x182574964}

[Flags: T - Forwarded through a tunnel]{lang="EN-US"}

[       N - Forwarded through the outgoing interface to the nexthop IP address]{lang="EN-US"}

[       B - Backup forwarding information]{lang="EN-US"}

[       A - Active forwarding information]{lang="EN-US"}

[ ]{lang="EN-US"}

[NID        Tnl-Type Flag OutLabel Forwarding Info]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[2048       LSP      NA   2025     GE1/0/2                   10.11.112.26]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_895751993}[显示所有的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> display mpls forwarding nhlfe]{lang="EN-US"}]{#struct_0_24739_x6658_740287705}

[Total NHLFE entries: 5]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flags: T - Forwarded through a tunnel]{lang="EN-US"}

[       N - Forwarded through the outgoing interface to the nexthop IP address]{lang="EN-US"}

[       B - Backup forwarding information]{lang="EN-US"}

[       A - Active forwarding information]{lang="EN-US"}

[ ]{lang="EN-US"}

[NID        Tnl-Type Flag OutLabel Forwarding Info]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[10         -        TA   -        2049]{lang="EN-US"}

[20         ]{lang="FR"}[-      ]{lang="EN-US"}[  TA   -        2050]{lang="FR"}

[2048       ]{lang="FR"}[LSP    ]{lang="EN-US"}[  NA   2025     GE1/0/2                   10.11.112.26]{lang="FR"}

[2049       ]{lang="FR"}[LSP    ]{lang="EN-US"}[  NA   3024     GE1/0/2                   10.11.112.26]{lang="FR"}

[                    ]{lang="FR"}[TB   3026     20]{lang="IT"}

[2050       ]{lang="IT"}[LSP    ]{lang="EN-US"}[  NA   3025     GE1/0/1                   10.11.113.26]{lang="IT"}

[[表1-2 ]{lang="EN-US"}[display mpls forwarding nhlfe]{lang="EN-US"}]{#struct_0_24739_x6658_x963090112}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x641004613}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_1920802911}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_1430068237}

[[Total NHLFE entries]{lang="EN-US"}]{#struct_0_24739_x6658_169261556}

[[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_27047477}[表项总数]{style="font-family:宋体"}

[[NID]{lang="EN-US"}]{#struct_0_24739_x6658_1885761950}

[[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_739828950}[表项索引]{style="font-family:宋体"}

[[Tnl-Type]{lang="EN-US"}]{#struct_0_24739_x6658_x1464916622}

[[隧道类型，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1941211611}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LOCAL]{lang="EN-US"}]{#struct_0_24739_x6658_1586332151}[：表示]{style="font-family:宋体"}[直连下一跳对应的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x804352415}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道、采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[或]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TE]{lang="EN-US"}]{#struct_0_24739_x6658_85460940}[：表示]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口对应的隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GRE]{lang="EN-US"}]{#struct_0_24739_x6658_739763414}[：表示]{style="font-family:宋体"}[GRE]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CRLSP]{lang="EN-US"}]{#struct_0_24739_x6658_229904489}[：表示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[隧道或采用]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_24739_x6658_608640657}[：表示隧道类型为无效值]{style="font-family:宋体"}

[[Flag]{lang="DA"}]{#struct_0_24739_x6658_x1514847578}

[[转发标记，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x345618039}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_24739_x6658_207271525}[：隧道转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_24739_x6658_739697878}[：出接口]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[下一跳转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_24739_x6658_x1697932496}[：备份转发信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_24739_x6658_x514699805}[：]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[用转发信息]{lang="EN-US" style="font-family:宋体"}

[[OutLabel]{lang="EN-US"}]{#struct_0_24739_x6658_1169883931}

[[出标签值]{style="font-family:宋体"}]{#struct_0_24739_x6658_x646598506}

[[Forwarding Info]{lang="EN-US"}]{#struct_0_24739_x6658_739632342}

[[转发信息]{style="font-family:宋体"}]{#struct_0_24739_x6658_629072115}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[转发标记为]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1514027647}[N]{lang="EN-US"}[时，转发信息为出接口和下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[转发标记为]{style="font-family:宋体"}]{#struct_0_24739_x6658_955507943}[T]{lang="EN-US"}[时，转发信息为]{style="font-family:宋体"}[NID]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1719836433 .myid}
[]{#_Toc404790489}[]{#struct_0_24739_x6658_x582126888}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls interface**

------------------------------------------------------------------------

[**[display mpls interface]{lang="EN-US"}**]{#struct_0_24739_x6658_740091094}[命令用来显示使能了]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力接口的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x22607031}

[**[display mpls interface]{lang="EN-US"}**[ \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_24739_x6658_x1746468749}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1293473544}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1249969580}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_582262197}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x822503362}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x2041946356}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1478329955}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_740025558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1510232369}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_24739_x6658_1055202354}[：显示指定接口的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定本参数，则显示所有使能了]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力接口的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1605420000}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_1442634380}[显示所有使能了]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力接口的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls interface]{lang="EN-US"}]{#struct_0_24739_x6658_x738758352}

[Interface               Status       MPLS MTU]{lang="EN-US"}

[GE1/0/1                  Up           1514 ]{lang="EN-US"}

[GE1/0/2                  Up           1514 ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display mpls interface]{lang="EN-US"}]{#struct_0_24739_x6658_x755857520}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x638634004}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_1661190865}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_739960022}

[[Interface]{lang="EN-US"}]{#struct_0_24739_x6658_1229864451}

[[接口名称]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1879744401}

[[Status]{lang="EN-US"}]{#struct_0_24739_x6658_x1470262434}

[[接口状态]{style="font-family:宋体"}]{#struct_0_24739_x6658_530853220}

[[MPLS MTU]{lang="EN-US"}]{#struct_0_24739_x6658_x1051317739}

[[接口的]{style="font-family:宋体"}[MPLS MTU]{lang="EN-US"}]{#struct_0_24739_x6658_x1686670946}[，单位为字节]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_739894486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x367848838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls mtu]{lang="EN-US"}**]{#struct_0_24739_x6658_1023638769}

::: {#1674881191 .myid}
[]{#_Toc404790490}[]{#struct_0_24739_x6658_x1382885264}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls label**

------------------------------------------------------------------------

[**[display mpls label]{lang="EN-US"}**]{#struct_0_24739_x6658_x463830620}[命令用来显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签的使用状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x250142262}

[**[display mpls label]{lang="EN-US"}**[ { *label-value1* \[ **to** *label-value2* \] \| **all** }]{lang="EN-US"}]{#struct_0_24739_x6658_x1502541622}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1794554576}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_35990130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_740353238}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_626729107}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x1532187997}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_1197087672}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_1959775565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1198400081}

[*[label-value1]{lang="EN-US"}*]{#struct_0_24739_x6658_1525554253}[：显示指定标签的使用状态。]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[为标签值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。当与]{style="font-family:宋体"}*[label-value2]{lang="EN-US"}*[一起使用时，]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[表示标签范围的起始值。]{style="font-family:宋体"}

[**[to ]{lang="EN-US"}***[label-value2]{lang="EN-US"}*]{#struct_0_24739_x6658_x1944362805}[：标签范围的结束值。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果同时指定了]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[和本参数，则显示]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[到]{style="font-family:宋体"}*[label-value2]{lang="EN-US"}*[之间标签的使用状态。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_24739_x6658_x2118522501}[：显示所有标签的使用状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_740287702}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x963090117}[显示]{style="font-family:宋体"}[900]{lang="EN-US"}[～]{style="font-family:宋体"}[902]{lang="EN-US"}[之间标签的使用状态。]{style="font-family:宋体"}

[[\<Sysname\> display mpls label 900 to 902]{lang="EN-US"}]{#struct_0_24739_x6658_1920999519}

[Label          Owner          State]{lang="EN-US"}

[900            -              Idle]{lang="EN-US"}

[901            -              Idle]{lang="EN-US"}

[902            LDP            Alloc]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display mpls label]{lang="EN-US"}]{#struct_0_24739_x6658_x159232979}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x645472206}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_194775210}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_1548769855}

[[Label]{lang="EN-US"}]{#struct_0_24739_x6658_128343266}

[[标签值]{style="font-family:宋体"}]{#struct_0_24739_x6658_739828951}

[[Owner]{lang="EN-US"}]{#struct_0_24739_x6658_x1464916623}

[[标签使用者，即使用该标签的协议，取值包括：]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_24739_x6658_x375127670}[、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[、]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[和]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_24739_x6658_x1514190594}

[[标签的使用状态，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_1104372294}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_24739_x6658_x1775748400}[：标签空闲]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Alloc]{lang="EN-US"}]{#struct_0_24739_x6658_739763415}[：标签已被申请]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pending]{lang="EN-US"}]{#struct_0_24739_x6658_229904488}[：标签已释放，但仍被]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[表项使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inuse]{lang="EN-US"}]{#struct_0_24739_x6658_608640656}[：标签已被申请，同时被]{style="font-family:宋体"}[LSP]{lang="EN-US"}[表项使用]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1284769827 .myid}
[]{#_Toc404790491}[]{#struct_0_24739_x6658_x1514847579}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls lsp**

------------------------------------------------------------------------

[**[display mpls lsp]{lang="EN-US"}**]{#struct_0_24739_x6658_x1911701980}[命令用来显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[Label Switched Path]{lang="EN-US"}[，标签交换路径）信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1703991988}

[**[display mpls lsp]{lang="EN-US"}**[ \[ **egress** \| **in-label** *label-value* \| **ingress** \| **outgoing-interface** *interface-type interface-number* \| **protocol** { **bgp** \| **ldp** *\|* **local** \| **rsvp-te** \| **static** \| **static-cr** } \| **transit**  \] \[ **vpn-instance** *vpn-instance-name* \] \[ *ipv4-dest mask-length* \| **ipv6** \[ *ipv6-dest prefix-length* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_24739_x6658_1839224509}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_2019246833}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_739697879}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1697932495}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x917984332}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x2041666195}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1133811968}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x781686157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_996159078}

[**[egress]{lang="EN-US"}**]{#struct_0_24739_x6658_1269526857}[：显示本设备作为出节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}***[ label-value]{lang="EN-US"}*]{#struct_0_24739_x6658_1377439432}[：]{style="font-family:宋体"}[显示以指定值为入标签的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[label-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[标签值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ingress]{lang="EN-US"}**]{#struct_0_24739_x6658_1580997393}[：显示本设备作为入节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[outgoing-interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_24739_x6658_739632343}[：显示以指定接口为出接口的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[protocol]{lang="EN-US"}**]{#struct_0_24739_x6658_629072116}[：根据建立]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的协议类型显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[bgp]{lang="EN-US"}**]{#struct_0_24739_x6658_x1514027644}[：显示]{style="font-family:宋体"}[BGP LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[ldp]{lang="EN-US"}**]{#struct_0_24739_x6658_1358792470}[：显示]{style="font-family:宋体"}[LDP LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_24739_x6658_x706266239}[：显示直连下一跳、]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口、隧道捆绑接口对应的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[rsvp-te]{lang="EN-US"}**]{#struct_0_24739_x6658_1145297396}[：显示]{style="font-family:宋体"}[RSVP-TE]{lang="EN-US"}[建立的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_24739_x6658_1555561736}[：显示手工配置的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[static-cr]{lang="EN-US"}**]{#struct_0_24739_x6658_1405464531}[：显示手工配置的静态]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[transit]{lang="EN-US"}**]{#struct_0_24739_x6658_1244526035}[：显示本设备作为中间节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_24739_x6658_740091095}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，区分大小写。如果不指定本参数，则显示公网的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[i]{lang="EN-US"}*]{#struct_0_24739_x6658_x22607030}*[pv4-dest mask-length]{lang="NO-BOK"}*[：显示到达指定]{style="font-family:宋体"}[IPv4 FEC]{lang="NO-BOK"}[的]{style="font-family:宋体"}[LSP]{lang="NO-BOK"}[信息。]{style="font-family:宋体"}*[i]{lang="EN-US"}[pv4-dest]{lang="NO-BOK"}*[为]{style="font-family:宋体"}[FEC]{lang="NO-BOK"}[的目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[mask-length]{lang="NO-BOK"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_24739_x6658_x1746468748}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。如果不指定本参数，则显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[i]{lang="EN-US"}*]{#struct_0_24739_x6658_x1435409811}*[pv6-dest ]{lang="NO-BOK"}[prefix]{lang="EN-US"}[-length]{lang="NO-BOK"}*[：显示到达指定]{style="font-family:宋体"}[IPv6 FEC]{lang="NO-BOK"}[的]{style="font-family:宋体"}[LSP]{lang="NO-BOK"}[信息。]{style="font-family:宋体"}*[i]{lang="EN-US"}[pv6-dest]{lang="NO-BOK"}*[为]{style="font-family:宋体"}[FEC]{lang="NO-BOK"}[的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[prefix]{lang="EN-US"}[-length]{lang="NO-BOK"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_24739_x6658_1277183821}[：显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1302047105}

[[如果没有指定任何参数，则显示所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_1313636795}[的简要信息；如果只指定了]{style="font-family:宋体"}**[verbose]{lang="EN-US"}**[参数，则显示所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_653258272}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x947593212}[显示所有]{style="font-family:宋体"}[IPv4 LSP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls lsp]{lang="EN-US"}]{#struct_0_24739_x6658_739960023}

[FEC                         Proto    In/Out Label    Interface/Out NHLFE]{lang="EN-US"}

[100.100.100.100/24          LDP      -/1049          Vlan20]{lang="EN-US"}

[Backup                               -/1050          Vlan21]{lang="EN-US"}

[100.100.100.10/24           LDP      -/1051          Vlan22]{lang="EN-US"}

[Backup                               -/1050          Vlan21]{lang="EN-US"}

[100.100.100.10/24           LDP      -/1049          Vlan30]{lang="EN-US"}

[101.100.100.10/24           LDP      1026/1049       Vlan20]{lang="EN-US"}

[102.100.100.10/24           LDP      1027/-          -]{lang="EN-US"}

[103.100.100.10/24           LDP      1028/1049       Tunnel10]{lang="EN-US"}

[110.100.100.20/24           BGP      -/1049          Vlan20]{lang="EN-US"}

[111.100.100.10/24           BGP      2028/1049       Vlan20]{lang="EN-US"}

[112.100.100.10/24           BGP      2029/-          Vlan20]{lang="EN-US"}

[113.100.100.10/24           BGP      2030/1049       NHLFE1500]{lang="EN-US"}

[114.100.100.10/24           BGP      2031/1050       Tunnel100]{lang="EN-US"}

[100.100.100.100             Local    -/-             Vlan20]{lang="EN-US"}

[101.101.101.101/32          Static   -/100           Vlan20]{lang="EN-US"}

[-                           Static   100/200         Vlan20]{lang="EN-US"}

[-                           Static   101/-           Vlan20]{lang="EN-US"}

[200.200.200.200/64000/64000 RSVP     -/1030          Vlan10]{lang="EN-US"}

[201.200.200.200/64000/64000 RSVP     1024/1031       Vlan10]{lang="EN-US"}

[202.200.200.200/64000/64000 RSVP     1025/-          -]{lang="EN-US"}

[150.140.150.100/64001/0     StaticCR -/1000          Vlan10]{lang="EN-US"}

[-                           StaticCR 50/1001         Vlan10]{lang="EN-US"}

[-                           StaticCR 51/-            - ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display mpls lsp]{lang="EN-US"}]{#struct_0_24739_x6658_1229864450}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x641820552}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1879678865}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_x321106459}

[[FEC]{lang="EN-US"}]{#struct_0_24739_x6658_1970739100}

[[转发等价类，包括以下形式：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x542893261}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_589208884}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码：表示根据目的地址划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_739894487}[地址：表示根据下一跳地址划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_x367848837}[地址]{style="font-family:宋体"}[/Out Label]{lang="EN-US"}[：表示根据下一跳地址和出标签划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress LSR ID/Tunnel ID/LSP ID]{lang="EN-US"}]{#struct_0_24739_x6658_1024097521}[：表示]{style="font-family:
  宋体"}[RSVP TE]{lang="EN-US"}[的]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_24739_x6658_62963527}[：表示静态]{style="font-family:宋体"}[Transit LSP]{lang="EN-US"}[、静态]{style="font-family:宋体"}[Egress LSP]{lang="EN-US"}[、静态]{style="font-family:宋体"}[Transit CR-LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[Egress CR-LSP]{lang="EN-US"}

[[如果显示为"]{style="font-family:宋体"}[Backup]{lang="EN-US"}]{#struct_0_24739_x6658_1736990418}["，则表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[是前一条]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的备份]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[Proto]{lang="EN-US"}]{#struct_0_24739_x6658_1416631282}

[[标签分发协议，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_740353239}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP]{lang="EN-US"}]{#struct_0_24739_x6658_626729108}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[LDP LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP]{lang="EN-US"}]{#struct_0_24739_x6658_x1532187992}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[BGP LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_24739_x6658_437572785}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_24739_x6658_101279603}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为手工配置的静态]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StaticCR]{lang="EN-US"}]{#struct_0_24739_x6658_x2124157443}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为手工配置的静态]{lang="EN-US" style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_24739_x6658_740287703}[：]{style="font-family:宋体"}[表示该]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[为直连下一跳、]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口、隧道捆绑接口对应的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_24739_x6658_x963090118}

[[入标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_24739_x6658_1920147551}[出标签值]{style="font-family:宋体"}

[[Interface/Out NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_x1703493845}

[[出接口名称或]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_1361711029}[索引]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}[NHLFE*number*]{lang="EN-US"}]{#struct_0_24739_x6658_x1989054401}[时，表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[迭代到]{style="font-family:宋体"}[NID]{lang="EN-US"}[为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项对应的]{style="font-family:宋体"}[Ingress LSP]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1229516947}[显示所有]{style="font-family:宋体"}[IPv6 LSP]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls lsp ipv6]{lang="EN-US"}]{#struct_0_24739_x6658_x272429905}

[FEC      : 100:100:100:100:100:100:100:100/128]{lang="EN-US"}

[Protocol : BGP      In-Label     : 2050]{lang="EN-US"}

[Out-Label: 10003    Out-Interface: Vlan10]{lang="EN-US"}

[BkLabel  : 10004    BkInterface  : Vlan20]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display mpls lsp ipv6]{lang="EN-US"}]{#struct_0_24739_x6658_2060249356}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x648315956}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1367468343}

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_x104547106}

[[FEC]{lang="EN-US"}]{#struct_0_24739_x6658_x1989119937}

[[转发等价类，包括以下形式：]{style="font-family:宋体"}]{#struct_0_24739_x6658_2145360312}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_x1960823119}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码：表示根据目的地址划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_x1682542557}[地址：表示根据下一跳地址划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_x1498629699}[地址]{style="font-family:宋体"}[/Out Label]{lang="EN-US"}[：表示根据下一跳地址和出标签划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress LSR ID/Tunnel ID/LSP ID]{lang="EN-US"}]{#struct_0_24739_x6658_x1467228984}[：表示]{style="font-family:
  宋体"}[RSVP TE]{lang="EN-US"}[的]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_24739_x6658_x1989185473}[：表示静态]{style="font-family:宋体"}[Transit LSP]{lang="EN-US"}[、静态]{style="font-family:宋体"}[Egress LSP]{lang="EN-US"}[、静态]{style="font-family:宋体"}[Transit CR-LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[Egress CR-LSP]{lang="EN-US"}

[[Protocol]{lang="EN-US"}]{#struct_0_24739_x6658_163148228}

[[标签分发协议，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1938293292}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP]{lang="EN-US"}]{#struct_0_24739_x6658_x1591959297}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[LDP LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP]{lang="EN-US"}]{#struct_0_24739_x6658_349725981}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[BGP LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_24739_x6658_x1228458379}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_24739_x6658_x1989251009}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为手工配置的静态]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StaticCR]{lang="EN-US"}]{#struct_0_24739_x6658_x1538411447}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为手工配置的静态]{lang="EN-US" style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_24739_x6658_x1823724826}[：]{style="font-family:宋体"}[表示该]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[为直连下一跳、]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口、隧道捆绑接口对应的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[In-Label]{lang="IT"}]{#struct_0_24739_x6658_205452834}

[[入标签值]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1260470897}

[[Out-Label]{lang="EN-US"}]{#struct_0_24739_x6658_x1988792257}

[[出标签值]{style="font-family:宋体"}]{#struct_0_24739_x6658_447764984}

[[Out-Interface]{lang="EN-US"}]{#struct_0_24739_x6658_x336853165}

[[出接口]{style="font-family:宋体"}]{#struct_0_24739_x6658_1702057904}

[[BkLabel]{lang="EN-US"}]{#struct_0_24739_x6658_x522812998}

[[备份]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1988857793}[的出标签值]{style="font-family:宋体"}

[[BkInterface]{lang="EN-US"}]{#struct_0_24739_x6658_50460867}

[[备份]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x712476685}[的出接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_1151187930}[显示所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls lsp verbose]{lang="EN-US"}]{#struct_0_24739_x6658_x1988988865}

[Destination  : 56.10.10.2]{lang="EN-US"}

[FEC          : 56.10.10.2/32]{lang="EN-US"}

[Protocol     : LDP]{lang="EN-US"}

[LSR Type     : Egress ]{lang="EN-US"}

[Service      : Statistics ]{lang="EN-US"}

[In-Label     : 1024        ]{lang="EN-US"}

[State        : Active]{lang="EN-US"}

[Inbound Statistics:]{lang="EN-US"}

[  Octets    : 13000]{lang="EN-US"}

[  Packets   : 100]{lang="EN-US"}

[  Errors    : 0]{lang="EN-US"}

[  Discards  : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination  : 56.10.10.4]{lang="EN-US"}

[FEC          : 56.10.10.2/32]{lang="EN-US"}

[Protocol     : LDP]{lang="EN-US"}

[LSR Type     : Transit]{lang="EN-US"}

[Service      : Statistics]{lang="EN-US"}

[In-Label     : 1026]{lang="EN-US"}

[Inbound Statistics:]{lang="EN-US"}

[  Octets    : 10600]{lang="EN-US"}

[  Packets   : 100]{lang="EN-US"}

[  Errors    : 0]{lang="EN-US"}

[  Discards  : 0]{lang="EN-US"}

[Path ID      : 0x40000000.1]{lang="EN-US"}

[State        : Active]{lang="EN-US"}

[Out-Label    : 1800]{lang="EN-US"}

[Nexthop      : 10.1.1.2]{lang="EN-US"}

[Out-Interface: Vlan10]{lang="EN-US"}

[BkLabel      : 1900]{lang="EN-US"}

[BkNexthop    : 20.1.1.2]{lang="EN-US"}

[BkInterface   : Vlan20]{lang="EN-US"}

[Outbound Statistics:]{lang="EN-US"}

[  Octets    : 12600]{lang="EN-US"}

[  Packets   : 100]{lang="EN-US"}

[  Errors    : 0]{lang="EN-US"}

[  Discards  : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination  : 56.10.10.4]{lang="EN-US"}

[FEC          : 56.10.10.2/32]{lang="EN-US"}

[Protocol     : LDP]{lang="EN-US"}

[LSR Type     : Ingress]{lang="EN-US"}

[Service      : -       ]{lang="EN-US"}

[NHLFE ID     : 2000]{lang="EN-US"}

[State        : Active]{lang="EN-US"}

[Out-Label    : 1800]{lang="EN-US"}

[Nexthop      : 10.1.1.2]{lang="EN-US"}

[Out-Interface: Vlan10]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display mpls lsp verbose]{lang="EN-US"}]{#struct_0_24739_x6658_1805289657}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x647626470}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_1224097186}

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_x844382403}

[[Destination]{lang="EN-US"}]{#struct_0_24739_x6658_x460118089}

[[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1988530113}[的目的地址]{style="font-family:宋体"}

[[FEC]{lang="IT"}]{#struct_0_24739_x6658_x671053353}

[[转发等价类，包括以下形式：]{style="font-family:宋体"}]{#struct_0_24739_x6658_1046443570}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_59035316}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码：表示根据目的地址划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_x1070954423}[地址：表示根据下一跳地址划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_24739_x6658_1955136284}[地址]{style="font-family:宋体"}[/Out Label]{lang="EN-US"}[：表示根据下一跳地址和出标签划分]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress LSR ID/Tunnel ID/LSP ID]{lang="EN-US"}]{#struct_0_24739_x6658_x1988595649}[：表示]{style="font-family:
  宋体"}[RSVP TE]{lang="EN-US"}[的]{style="font-family:宋体"}[FEC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_24739_x6658_2096424962}[：表示静态]{style="font-family:宋体"}[Transit LSP]{lang="EN-US"}[、静态]{style="font-family:宋体"}[Egress LSP]{lang="EN-US"}[、静态]{style="font-family:宋体"}[Transit CR-LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[Egress CR-LSP]{lang="EN-US"}

[[Protocol]{lang="EN-US"}]{#struct_0_24739_x6658_x1343152358}

[[标签分发协议，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x654550729}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP]{lang="EN-US"}]{#struct_0_24739_x6658_x1266617749}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[LDP LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP]{lang="EN-US"}]{#struct_0_24739_x6658_1043806063}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[BGP LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP]{lang="EN-US"}]{#struct_0_24739_x6658_x1989054400}[：表示该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为采用]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[协议建立的]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_24739_x6658_1499366408}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为手工配置的静态]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StaticCR]{lang="EN-US"}]{#struct_0_24739_x6658_1319649798}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[为手工配置的静态]{lang="EN-US" style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_24739_x6658_1800877351}[：]{style="font-family:宋体"}[表示该]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[为直连下一跳、]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口、隧道捆绑接口对应的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[LSR Type]{lang="EN-US"}]{#struct_0_24739_x6658_1498579126}

[[LSR]{lang="EN-US"}]{#struct_0_24739_x6658_x1989119936}[类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress]{lang="EN-US"}]{#struct_0_24739_x6658_579276371}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的入节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_24739_x6658_991029885}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的中间节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Egress]{lang="EN-US"}]{#struct_0_24739_x6658_x110639158}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的出节点]{lang="EN-US" style="font-family:宋体"}

[[Service]{lang="EN-US"}]{#struct_0_24739_x6658_512164639}

[[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1989185472}[上部署的业务，目前仅支持]{style="font-family:宋体"}[Statistics]{lang="EN-US"}[，表示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发统计功能]{style="font-family:宋体"}

[[In-Label]{lang="EN-US"}]{#struct_0_24739_x6658_1729232169}

[[入标签值]{style="font-family:宋体"}]{#struct_0_24739_x6658_x466412199}

[[Path ID]{lang="EN-US"}]{#struct_0_24739_x6658_x1670575487}

[[转发路径，取值为]{style="font-family:宋体"}[0xnn.m]{lang="EN-US"}]{#struct_0_24739_x6658_536051264}[，]{style="font-family:宋体"}[nn]{lang="EN-US"}[表示承载本层]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的外层]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[组]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[m]{lang="EN-US"}[表示等价路径编号]{style="font-family:宋体"}

[[NHLFE ID]{lang="EN-US"}]{#struct_0_24739_x6658_x1989251008}

[[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_1190471908}[表项索引]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_24739_x6658_1173218190}

[[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1947692952}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_24739_x6658_x1988792256}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[正在使用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_24739_x6658_x1118318957}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[空闲未用]{style="font-family:宋体"}

[[Inbound Statistics]{lang="EN-US"}]{#struct_0_24739_x6658_x28874579}

[[入方向的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_911838237}[转发统计信息，包括入方向接收的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、接收的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、接收的错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Out-Label]{lang="EN-US"}]{#struct_0_24739_x6658_x1988857792}

[[出标签值]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1515623074}

[[Nexthop]{lang="EN-US"}]{#struct_0_24739_x6658_819103473}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_24739_x6658_x804371295}

[[Out-Interface]{lang="EN-US"}]{#struct_0_24739_x6658_x1988923328}

[[出接口]{style="font-family:宋体"}]{#struct_0_24739_x6658_1403548045}

[[BkLabel]{lang="EN-US"}]{#struct_0_24739_x6658_585943067}

[[备份]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1801579370}[的出标签值]{style="font-family:宋体"}

[[BkNexthop]{lang="EN-US"}]{#struct_0_24739_x6658_x1988988864}

[[备份]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x923593698}[的下一跳地址]{style="font-family:宋体"}

[[BkInterface]{lang="EN-US"}]{#struct_0_24739_x6658_507535123}

[[备份]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1125077106}[的出接口]{style="font-family:宋体"}

[[Outbound Statistics]{lang="EN-US"}]{#struct_0_24739_x6658_x1988530112}

[[出方向的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_2057830002}[转发统计信息，包括出方向发送的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、发送的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1774720904}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls lsp statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_614347941}

::: {#-655553075 .myid}
[]{#_Toc404790492}[]{#struct_0_24739_x6658_x722911423}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls lsp statistics**

------------------------------------------------------------------------

[**[display mpls lsp statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_x1988595648}[命令用来显示]{style="font-family:
宋体"}[LSP]{lang="EN-US"}[的统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_530341021}

[**[display mpls lsp statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_x233827479}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1738046141}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x254532998}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_234948925}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x125152951}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_1856694792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1618455958}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x1989054403}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x66717533}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_2112186312}[显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls lsp statistics]{lang="EN-US"}]{#struct_0_24739_x6658_387899768}

[LSP Type      Ingress/Transit/Egress  Active]{lang="EN-US"}

[Static LSP    0/0/0                   0/0/0]{lang="EN-US"}

[Static CRLSP  0/0/0                   0/0/0]{lang="EN-US"}

[LDP LSP       2/2/1                   2/2/1]{lang="EN-US"}

[RSVP CRLSP    0/0/0                   0/0/0]{lang="EN-US"}

[BGP LSP       0/0/0                   0/0/0]{lang="EN-US"}

[Local LSP     2/0/0                   2/0/0]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Total         4/2/1                   4/2/1]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display mpls lsp statistics]{lang="EN-US"}]{#struct_0_24739_x6658_1443525229}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x623101114}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_x326703776}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1989119939}

[[LSP Type]{lang="EN-US"}]{#struct_0_24739_x6658_x1343037930}

[[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_1773855815}[的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1620536880}[：]{style="font-family:宋体"}[静态]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static CRLSP]{lang="EN-US"}]{#struct_0_24739_x6658_365103226}[：]{style="font-family:宋体"}[静态]{lang="EN-US" style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LDP LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x227462318}[：]{style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}[建立的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1989185475}[：]{style="font-family:宋体"}[直连下一跳、]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口、隧道捆绑接口对应的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSVP CRLSP]{lang="EN-US"}]{#struct_0_24739_x6658_x999651186}[：]{style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:宋体"}[RSVP]{lang="EN-US"}[建立的]{lang="EN-US" style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP LSP]{lang="EN-US"}]{#struct_0_24739_x6658_711635412}[：]{style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[建立的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}

[[Total]{lang="EN-US"}]{#struct_0_24739_x6658_1707392424}

[[各种类型]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1512359212}[的总数]{style="font-family:宋体"}

[[Ingress]{lang="EN-US"}]{#struct_0_24739_x6658_x24663035}

[[本设备作为入节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1989251011}[数量]{style="font-family:宋体"}

[[Transit]{lang="EN-US"}]{#struct_0_24739_x6658_x1894576271}

[[本设备作为中间节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x328339543}[数量]{style="font-family:宋体"}

[[Egress]{lang="EN-US"}]{#struct_0_24739_x6658_574626414}

[[本设备作为出节点的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x947822429}[数量]{style="font-family:宋体"}

[[Active]{lang="EN-US"}]{#struct_0_24739_x6658_x1159649122}

[[处于可用状态的各种类型]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1988792259}[的数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-127309361 .myid}
[]{#_Toc404790493}[]{#struct_0_24739_x6658_1966794758}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls nib**

------------------------------------------------------------------------

[**[display mpls nib]{lang="EN-US"}**]{#struct_0_24739_x6658_1231693276}[命令用来显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[NIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Nexthop Information Base]{lang="EN-US"}[，下一跳信息库）信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x85489299}

[**[display mpls nib ]{lang="EN-US"}**[\[ *nib-id* \]]{lang="EN-US"}]{#struct_0_24739_x6658_893979102}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_236698116}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x189482345}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_848321464}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1988857795}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_1213260281}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_1280836959}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x454991965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1494647219}

[*[nib-id]{lang="EN-US"}*]{#struct_0_24739_x6658_154520658}[：显示指定]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[下一跳的信息。]{style="font-family:宋体"}*[nib-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[下一跳的索引，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFFFFFFFFFE]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[下一跳的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1056339859}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_470508154}[显示所有]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[下一跳的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls nib]{lang="EN-US"}]{#struct_0_24739_x6658_x1988923331}

[NIB ID: 0x40000000]{lang="EN-US"}

[  Users: 1]{lang="EN-US"}

[  Status: Active]{lang="EN-US"}

[  ECMP number: 1]{lang="EN-US"}

[      Outgoing NHLFE ID: 1024]{lang="EN-US"}

[      Backup outgoing NHLFE ID: 1027]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display mpls nib]{lang="EN-US"}]{#struct_0_24739_x6658_193628928}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x620763209}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_x404666990}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_1681054433}

[[NIB ID]{lang="EN-US"}]{#struct_0_24739_x6658_x362919456}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_124055913}[下一跳索引]{style="font-family:宋体"}

[[Users]{lang="EN-US"}]{#struct_0_24739_x6658_x133669723}

[[引用该]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x1988988867}[下一跳的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项数目]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_24739_x6658_642490243}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_1346633781}[下一跳的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_24739_x6658_86757121}[，激活表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dummy]{lang="EN-US"}]{#struct_0_24739_x6658_x360116410}[，非激活表项]{style="font-family:宋体"}

[[ECMP number]{lang="EN-US"}]{#struct_0_24739_x6658_972414052}

[[等价路径数目]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1988530115}

[[Outgoing NHLFE ID]{lang="EN-US"}]{#struct_0_24739_x6658_x1477622407}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x89698048}[下一跳对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引]{style="font-family:宋体"}

[[Backup outgoing NHLFE ID]{lang="EN-US"}]{#struct_0_24739_x6658_1101670034}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_17834917}[下一跳对应的备份]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的索引]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-509646385 .myid}
[]{#_Toc404790494}[]{#struct_0_24739_x6658_x883172276}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls nid**

------------------------------------------------------------------------

[**[display mpls nid]{lang="EN-US"}**]{#struct_0_24739_x6658_2005949228}[命令用来显示]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引的使用状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1988595651}

[**[display mpls nid ]{lang="EN-US"}**[\[ *nid-value1* \[ **to** *nid-value2* \] \]]{lang="EN-US"}]{#struct_0_24739_x6658_1740129066}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1332829487}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_1544438872}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_2049894440}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x2034277403}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_1928805145}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x693381877}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x345722559}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1989054402}

[*[nid-value1]{lang="EN-US"}*]{#struct_0_24739_x6658_x1632801474}[：显示指定]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引的使用状态。]{style="font-family:宋体"}*[nid-value1]{lang="EN-US"}*[为]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。当与]{style="font-family:宋体"}*[nid-value2]{lang="EN-US"}*[一起使用时，]{style="font-family:宋体"}*[nid-value1]{lang="EN-US"}*[表示索引范围的起始值。]{style="font-family:宋体"}

[**[to ]{lang="EN-US"}***[nid-value2]{lang="EN-US"}*]{#struct_0_24739_x6658_230268027}[：]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，表示索引范围的结束值。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果同时指定了]{style="font-family:宋体"}*[nid-value1]{lang="EN-US"}*[和本参数，则显示]{style="font-family:宋体"}*[nid-value1]{lang="EN-US"}*[到]{style="font-family:宋体"}*[nid-value2]{lang="EN-US"}*[之间的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引的使用状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x268298322}

[[设备上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_1446869960}[表项索引（该索引为]{style="font-family:宋体"}[32]{lang="EN-US"}[位二进制数）分为两类：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[固定]{style="font-family:宋体"}]{#struct_0_24739_x6658_x988455865}[NHLFE]{lang="EN-US"}[表项索引：设备为隧道接口或隧道捆绑接口生成的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，该索引的高]{style="font-family:宋体"}[4]{lang="EN-US"}[位为非]{style="font-family:宋体"}[0]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[动态]{style="font-family:宋体"}]{#struct_0_24739_x6658_1684900855}[NHLFE]{lang="EN-US"}[表项索引：设备为]{style="font-family:宋体"}[LDP LSP]{lang="EN-US"}[、静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[等协议生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分配的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，该索引的高]{style="font-family:宋体"}[4]{lang="EN-US"}[位为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[本命令只能用来显示动态]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_586446413}[表项索引的使用状态。]{style="font-family:宋体"}

[[执行本命令时，如果不指定任何参数，则显示所有动态]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}]{#struct_0_24739_x6658_x1960519}[表项索引的使用状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1989119938}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_1385845425}[显示]{style="font-family:宋体"}[1028]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[之间的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引的使用状态。]{style="font-family:宋体"}

[[\<Sysname\> display mpls nid 1028 to 1500]{lang="EN-US"}]{#struct_0_24739_x6658_213499251}

[NID alloc state: \'.\' means not used, \'\$\' means used]{lang="EN-US"}

[1028   :\...\$\.... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....]{lang="EN-US"}

[1092   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....]{lang="EN-US"}

[1156   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....]{lang="EN-US"}

[1220   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....]{lang="EN-US"}

[1284   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....]{lang="EN-US"}

[1348   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....]{lang="EN-US"}

[1412   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....]{lang="EN-US"}

[1476   :\...\..... \...\..... \...\..... .]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display mpls nid]{lang="EN-US"}]{#struct_0_24739_x6658_750514310}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x628768377}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_x488204887}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1989185474}

[[NID alloc state]{lang="EN-US"}]{#struct_0_24739_x6658_566432755}

[[NID]{lang="EN-US"}]{#struct_0_24739_x6658_x553225438}[使用状态]{style="font-family:宋体"}

[[\'.\' means not used]{lang="EN-US"}]{#struct_0_24739_x6658_759343838}

[["]{style="font-family:宋体"}[.]{lang="EN-US"}]{#struct_0_24739_x6658_791058786}["表示没有使用]{style="font-family:宋体"}

[[\'\$\' means used]{lang="EN-US"}]{#struct_0_24739_x6658_x2030805091}

[["]{style="font-family:宋体"}[\$]{lang="EN-US"}]{#struct_0_24739_x6658_1182869780}["表示已经使用]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1579335190 .myid}
[]{#_Toc404790495}[]{#struct_0_24739_x6658_x1989251010}

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls summary**

------------------------------------------------------------------------

[**[display mpls summary]{lang="EN-US"}**]{#struct_0_24739_x6658_834307084}[命令用来显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[汇总信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1941152413}

[**[display mpls summary]{lang="EN-US"}**]{#struct_0_24739_x6658_1150416827}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x744724243}

[[任意视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_370097928}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1501049803}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_1307655516}

[[network-operator]{lang="EN-US"}]{#struct_0_24739_x6658_x1652004178}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1988792258}

[[mdc-operator]{lang="EN-US"}]{#struct_0_24739_x6658_400710817}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x943672485}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x171300766}[显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[汇总信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls summary]{lang="EN-US"}]{#struct_0_24739_x6658_2059862564}

[MPLS LSR ID      : 2.2.2.2]{lang="EN-US"}

[Egress Label Type: Implicit-null]{lang="EN-US"}

[Labels:]{lang="EN-US"}

[  Range           Idle]{lang="EN-US"}

[  16-1023         1008]{lang="EN-US"}

[  1024-1000000    998849]{lang="EN-US"}

[Protocols:]{lang="EN-US"}

[  Type            State]{lang="EN-US"}

[  LDP             Normal]{lang="EN-US"}

[  Static          Normal]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display mpls summary]{lang="EN-US"}]{#struct_0_24739_x6658_x1900073384}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x627046548}[[字段]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1988857794}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_24739_x6658_x352823660}

[[MPLS LSR ID]{lang="EN-US"}]{#struct_0_24739_x6658_1759712869}

[[MPLS LSR]{lang="EN-US"}]{#struct_0_24739_x6658_2101951347}[标识符]{style="font-family:宋体"}

[[Egress Label Type]{lang="EN-US"}]{#struct_0_24739_x6658_786139831}

[[Egress]{lang="EN-US"}]{#struct_0_24739_x6658_1892062478}[向倒数第二跳通告的标签类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Implicit-null]{lang="EN-US"}]{#struct_0_24739_x6658_2137091964}[：隐式空标签]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Explicit-null]{lang="EN-US"}]{#struct_0_24739_x6658_x1988988866}[：显式空标签]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Non-null]{lang="EN-US"}]{#struct_0_24739_x6658_x2086393112}[：非空标签]{lang="EN-US" style="font-family:宋体"}

[[Labels]{lang="EN-US"}]{#struct_0_24739_x6658_x758832079}

[[标签相关信息]{style="font-family:宋体"}]{#struct_0_24739_x6658_x215741995}

[[Range]{lang="EN-US"}]{#struct_0_24739_x6658_x375562706}

[[标签范围]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1988530114}

[[Idle]{lang="EN-US"}]{#struct_0_24739_x6658_1251260948}

[[标签范围内空闲的标签数目]{style="font-family:宋体"}]{#struct_0_24739_x6658_1258300759}

[[Protocols]{lang="EN-US"}]{#struct_0_24739_x6658_x1651366607}

[[生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1312258406}[的标签分发协议及其运行状态]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_24739_x6658_x1988595650}

[[协议类型，取值包括：]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_24739_x6658_174045125}[、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[、]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[、]{style="font-family:宋体"}[Static]{lang="EN-US"}[、]{style="font-family:宋体"}[StaticCR]{lang="EN-US"}[、]{style="font-family:宋体"}[TE]{lang="EN-US"}[、]{style="font-family:宋体"}[CCC]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_24739_x6658_584497129}

[[标签分发协议运行状态，取值包括：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x2035177889}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_24739_x6658_402894064}[：正常状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Recover]{lang="EN-US"}]{#struct_0_24739_x6658_x1989054405}[：协议]{lang="EN-US" style="font-family:宋体"}[处于]{style="font-family:宋体"}[GR]{lang="EN-US"}[期间]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1166016354 .myid}
[]{#_Toc404790496}[]{#struct_0_24739_x6658_1096081881}[]{#_Toc325469529}[]{#_Toc325469530}[]{#_Toc325469531}[]{#_Toc325469532}[]{#_Toc325469533}[]{#_Toc325469534}[]{#_Toc325469535}[]{#_Toc325469536}[]{#_Toc325469537}[]{#_Toc325469538}[]{#_Toc325469539}[]{#_Toc325469540}[]{#_Toc325469541}[]{#_Toc325469542}[]{#_Toc325469543}[]{#_Toc325469544}[]{#_Toc325469545}[]{#_Toc325469546}[]{#_Toc325469547}[]{#_Toc325469548}[]{#_Toc325469549}[]{#_Toc325469550}[]{#_Toc325469551}[]{#_Toc325469552}[]{#_Toc325469553}[]{#_Toc325469554}[]{#_Toc325469555}[]{#_Toc325469556}[]{#_Toc325469557}[]{#_Toc325469558}[]{#_Toc325469559}[]{#_Toc325469560}[]{#_Toc325469561}[]{#_Toc325469562}[]{#_Toc325469563}[]{#_Toc325469564}[]{#_Toc325469565}[]{#_Toc325469566}[]{#_Toc325469567}[]{#_Toc325469568}[]{#_Toc325469569}[]{#_Toc325469570}[]{#_Toc325469571}[]{#_Toc325469572}[]{#_Toc325469573}[]{#_Toc325469574}[]{#_Toc325469575}[]{#_Toc325469576}[]{#_Toc325469577}[]{#_Toc325469578}[]{#_Toc325469579}[]{#_Toc325469580}[]{#_Toc325469581}[]{#_Toc325469582}[]{#_Toc325469631}[]{#_Toc325469632}[]{#_Toc325469633}[]{#_Toc325469634}[]{#_Toc325469635}[]{#_Toc325469636}[]{#_Toc293393940}[]{#_Toc293393941}[]{#_Toc293393942}[]{#_Toc293393943}[]{#_Toc293393944}[]{#_Toc293393945}[]{#_Toc293393946}[]{#_Toc293393947}[]{#_Toc293393948}[]{#_Toc293393949}[]{#_Toc293393950}[]{#_Toc293393951}[]{#_Toc293393952}[]{#_Toc293393953}[]{#_Toc293393954}[]{#_Toc293393955}[]{#_Toc293393958}[]{#_Toc293393959}[]{#_Toc293393975}[]{#_Toc293393976}[]{#_Toc293393978}[]{#_Toc293393979}[]{#_Toc293393980}[]{#_Toc293393981}[]{#_Toc293393994}

**MPLS基础 \-- MPLS基础配置命令 \-- ftn enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS基础命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_24739_x6658_x159521782}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_24739_x6658_1019051479}
:::

[ ]{lang="EN-US"}

[**[ftn enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x1989119941}[命令用来开启]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项维护功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ ftn enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x986610962}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x385727186}

[**[ftn enable]{lang="EN-US"}**]{#struct_0_24739_x6658_229155558}

[**[undo ftn enable]{lang="EN-US"}**]{#struct_0_24739_x6658_437758488}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_685896331}

[[RIB]{lang="EN-US"}]{#struct_0_24739_x6658_x1989185477}[的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项维护功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_2132516696}

[[RIB IPv4]{lang="EN-US"}]{#struct_0_24739_x6658_x1016914050}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1352741488}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x952127803}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1989251013}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x731776857}

[[FTN]{lang="EN-US"}]{#struct_0_24739_x6658_x2087388798}[（]{style="font-family:宋体"}[FEC to NHLFE map]{lang="EN-US"}[，]{style="font-family:宋体"}[FEC]{lang="EN-US"}[到]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的映射）表项是一类特殊的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项，该类]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项中包含出标签值信息。如果报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址匹配]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项，则为报文添加该表项中的出标签值后，转发该报文。]{style="font-family:宋体"}

[[只有执行本命令开启]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_24739_x6658_428489141}[的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项维护功能后，设备才会将]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项学习到]{style="font-family:宋体"}[RIB]{lang="EN-US"}[中，才能进一步执行]{style="font-family:宋体"}**[mpls-forwarding statistics prefix-list]{lang="EN-US"}**[命令，使能指定目的网络的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发统计功能。否则，不会对]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发进行统计。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1581897123}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1988792261}[开启]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项维护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_1610498862}

[\[Sysname\] rib]{lang="EN-US"}

[\[system-rib\] address-family ipv4]{lang="EN-US"}

[\[system-rib-ipv4\] ftn enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x860182154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls-forwarding statistics prefix-list]{lang="EN-US"}**]{#struct_0_24739_x6658_x1672934924}
:::::

::::: {#-1635273488 .myid}
[]{#_Toc404790497}[]{#struct_0_24739_x6658_1623173866}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls-forwarding statistics prefix-list**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS基础命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_24739_x6658_x1988857797}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_24739_x6658_x1918907601}
:::

[ ]{lang="EN-US"}

[**[mpls-forwarding statistics prefix-list]{lang="EN-US"}**]{#struct_0_24739_x6658_1279171315}[命令用来使能指定目的网络的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发统计功能。]{style="font-family:宋体"}

[**[undo mpls-forwarding statistics prefix-list]{lang="EN-US"}**]{#struct_0_24739_x6658_1557971022}[命令用来关闭指定目的网络的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1436438704}

[**[mpls-forwarding statistics prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_24739_x6658_598781299}

[**[undo ]{lang="EN-US"}[mpls-forwarding statistics prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_24739_x6658_x1988923333}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1356428342}

[[所有目的网络的]{style="font-family:宋体"}[FTN]{lang="EN-US"}]{#struct_0_24739_x6658_x577517215}[转发统计功能均处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1374112101}

[[RIB IPv4]{lang="EN-US"}]{#struct_0_24739_x6658_x705356258}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1988988869}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_192151549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x118499979}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x872676641}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_24739_x6658_x518603161}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。只有目的网络地址通过]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表的过滤，才会使能该目的网络的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发统计功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1988530117}

[[FTN]{lang="EN-US"}]{#struct_0_24739_x6658_1654545475}[转发是指接收到不带标签的报文，为其添加标签后转发该报文。本命令用来使能]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发的统计功能。]{style="font-family:宋体"}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_315219299}[标签转发是指接收到带有标签的报文后，根据报文中的入标签转发该报文。]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发的统计功能通过]{style="font-family:宋体"}**[mpls statistics]{lang="EN-US"}**[命令使能。]{style="font-family:宋体"}

[[执行本命令前，必须先执行]{style="font-family:宋体"}**[ftn enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x124243149}[命令开启]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项维护功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1425301123}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_596355232}[使能目的网络]{style="font-family:宋体"}[2.2.2.0/24]{lang="EN-US"}[的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_x1988595653}

[\[Sysname\] ip prefix-list abc permit 2.2.2.0 24]{lang="EN-US"}

[\[Sysname\] rib]{lang="EN-US"}

[\[system-rib\] address-family ipv4]{lang="EN-US"}

[\[system-rib-ipv4\] ftn enable]{lang="EN-US"}

[\[system-rib-ipv4\] mpls-forwarding statistics prefix-list abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1392038816}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ftn enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x1090936937}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_x769964080}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls statistics interval]{lang="EN-US"}**]{#struct_0_24739_x6658_x1989054404}
:::::

::: {#-451716348 .myid}
[]{#_Toc404790498}[]{#struct_0_24739_x6658_x470002060}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls enable**

------------------------------------------------------------------------

[**[mpls enable]{lang="EN-US"}**]{#struct_0_24739_x6658_788851407}[命令用来使能接口的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ mpls enable]{lang="EN-US"}**]{#struct_0_24739_x6658_1941581756}[命令用来关闭接口的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x15091765}

[**[mpls enable]{lang="EN-US"}**]{#struct_0_24739_x6658_1204404910}

[**[undo mpls enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x1312688687}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_914808689}

[[未使能接口的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x1897945661}[能力。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1989119940}

[[接口视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_1742272393}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_60709594}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x45937927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_106832492}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x434444975}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_24739_x6658_x781184980}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1989185476}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> System-view]{lang="EN-US"}]{#struct_0_24739_x6658_x596366659}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mpls enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_24739_x6658_1648168724}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_1424222352}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> System-view]{lang="EN-US"}]{#struct_0_24739_x6658_x1757733541}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] mpls enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1842408289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls interface]{lang="EN-US"}**]{#struct_0_24739_x6658_392161330}
:::

::::: {#-594742003 .myid}
[]{#_Toc404790499}[]{#struct_0_24739_x6658_x838521401}[]{#_Toc387165487}[]{#_Toc382312534}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls forwarding split-horizon**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS基础命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_24739_x6658_x1124897319}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_24739_x6658_x1159861159}
:::

[ ]{lang="EN-US"}

[**[mpls forwarding split-horizon]{lang="EN-US"}**]{#struct_0_24739_x6658_x225504590}[命令用来开启]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[转发的水平分割功能。]{style="font-family:宋体"}

[**[undo mpls forwarding split-horizon]{lang="EN-US"}**]{#struct_0_24739_x6658_x837669433}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x589163761}

[**[mpls forwarding split-horizon]{lang="EN-US"}**]{#struct_0_24739_x6658_x1737895991}

[**[undo mpls forwarding split-horizon]{lang="EN-US"}**]{#struct_0_24739_x6658_x1158005298}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1315847897}

[[未开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_1591419206}[转发的水平分割功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_892223157}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x261111227}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1936747174}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x837603897}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1772660873}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_623694706}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_1528273518}[开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发的水平分割功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_1255182835}

[\[Sysname\] mpls forwarding split-horizon]{lang="EN-US"}
:::::

::: {#1375661521 .myid}
[]{#_Toc404790500}[]{#struct_0_24739_x6658_x1989251012}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls label advertise**

------------------------------------------------------------------------

[**[mpls label advertise]{lang="EN-US"}**]{#struct_0_24739_x6658_1997106498}[命令用来配置设备作为]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点时分配的标签类型，即向倒数第二跳通告的标签类型。]{style="font-family:宋体"}

[**[undo mpls label advertise]{lang="EN-US"}**]{#struct_0_24739_x6658_1289437629}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1027287871}

[**[mpls label advertise]{lang="EN-US"}**[ { **explicit-null** \| **implicit-null** \| **non-null** }]{lang="EN-US"}]{#struct_0_24739_x6658_440756731}

[**[undo mpls label advertise]{lang="EN-US"}**]{#struct_0_24739_x6658_1928293594}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_2049610218}

[[设备作为]{style="font-family:宋体"}[Egress]{lang="EN-US"}]{#struct_0_24739_x6658_1455110040}[节点时，向倒数第二跳通告隐式空标签（]{style="font-family:宋体"}**[implicit-null]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1225925878}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1988792260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_44414921}

[[network-admin]{lang="FR"}]{#struct_0_24739_x6658_55855684}

[[mdc-admin]{lang="FR"}]{#struct_0_24739_x6658_x975256994}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1132379510}

[**[explicit-null]{lang="FR"}**]{#struct_0_24739_x6658_x275167876}[：]{style="font-family:宋体"}[指定设备作为]{style="font-family:宋体"}[Egress]{lang="FR"}[节点时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[向倒数第二跳通告显式空标签]{style="font-family:宋体"}[，标签]{style="font-family:宋体"}[值为]{style="font-family:宋体"}[0]{lang="FR"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[implicit-null]{lang="EN-US"}**]{#struct_0_24739_x6658_313805054}[：指定设备作为]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点时，向倒数第二跳通告隐式空标签，]{style="font-family:宋体"}[标签]{style="font-family:宋体"}[值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[non-null]{lang="EN-US"}**]{#struct_0_24739_x6658_x1067119467}[：指定设备作为]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点时，向倒数第二跳通告非空标签。非空标签的支持情况和取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_510988747}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请根据实际情况选择]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1988857796}[Egress]{lang="EN-US"}[节点分配的标签类型：如果倒数第二跳节点支持]{style="font-family:宋体"}[PHP]{lang="EN-US"}[（]{style="font-family:宋体"}[Penultimate Hop Popping]{lang="EN-US"}[，倒数第二跳弹出）功能，则建议采用隐式空标签；如果在简化]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点转发处理的同时，希望]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点能够根据标签中的]{style="font-family:宋体"}[TC]{lang="EN-US"}[等信息决定]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略，则建议采用显式空标签；非空标签只使用在一些比较特殊的场景，比如]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点上部署了]{style="font-family:宋体"}[OAM]{lang="EN-US"}[，只有根据标签才能对应到]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能实体的情况，通常情况下不建议使用非空标签。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备作为倒数第二跳节点时，允许]{style="font-family:宋体"}]{#struct_0_24739_x6658_809975754}[Egress]{lang="FR"}[节点向其通告显式空标签、隐式空标签和非空标签。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_24739_x6658_819128010}[LDP LSP]{lang="FR"}[，执行]{lang="EN-US" style="font-family:宋体"}**[mpls label advertise]{lang="FR"}**[命令修改]{lang="EN-US" style="font-family:
宋体"}[Egress]{lang="EN-US"}[分配的标签类型后，已经建立的]{lang="EN-US" style="font-family:
宋体"}[LDP LSP]{lang="EN-US"}[会被拆除，并根据新的标签类型重新建立。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_24739_x6658_1527870072}[BGP LSP]{lang="FR"}[，]{lang="EN-US" style="font-family:宋体"}**[mpls label advertise]{lang="EN-US"}**[命令只对新建立的]{lang="EN-US" style="font-family:
宋体"}[BGP LSP]{lang="EN-US"}[生效，执行本命令前已经建立的]{lang="EN-US" style="font-family:宋体"}[BGP LSP]{lang="EN-US"}[不受影响。若要使本命令对已经建立的]{lang="EN-US" style="font-family:宋体"}[BGP LSP]{lang="EN-US"}[生效，则需要从]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中删除]{lang="EN-US" style="font-family:宋体"}[BGP LSP]{lang="EN-US"}[对应的路由，并重新引入该路由。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_270807774}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_988050741}[配置设备作为]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点时，向倒数第二跳通告显式空标签。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_1339421385}

[\[Sysname\] mpls label advertise explicit-null]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1914347524}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mpls ldp]{lang="EN-US"}**]{#struct_0_24739_x6658_x1184794139}[（]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/LDP]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#-857921193 .myid}
[]{#_Toc404790501}[]{#struct_0_24739_x6658_x1988923332}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls lsr-id**

------------------------------------------------------------------------

[**[mpls lsr-id]{lang="EN-US"}**]{#struct_0_24739_x6658_x1372455013}[命令用来配置本节点的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo mpls lsr-id]{lang="EN-US"}**]{#struct_0_24739_x6658_2063304327}[命令用来删除]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x735962858}

[**[mpls lsr-id]{lang="EN-US"}**[ *lsr-id*]{lang="EN-US"}]{#struct_0_24739_x6658_771410984}

[**[undo mpls lsr-id]{lang="EN-US"}**]{#struct_0_24739_x6658_1045896128}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1341421778}

[[未配置本节点的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}]{#struct_0_24739_x6658_x1314512774}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1988988868}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_1758235490}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x577577404}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_1005341030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x800614229}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1900200974}

[*[lsr-id]{lang="EN-US"}*]{#struct_0_24739_x6658_549790765}[：]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，点分十进制格式，用于标识一个]{style="font-family:宋体"}[LSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1898363706}

[[推荐使用]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_24739_x6658_x1796408577}[上某个]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的地址作为]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1988530116}

[[\# ]{lang="NL-BE"}]{#struct_0_24739_x6658_88461534}[配置本节点的]{style="font-family:宋体"}[LSR]{lang="NL-BE"}[ ]{lang="NL-BE"}[ID]{lang="NL-BE"}[为]{style="font-family:宋体"}[3.3.3.3]{lang="NL-BE"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL-BE"}]{#struct_0_24739_x6658_1636548678}

[\[Sysname\] mpls lsr-id 3.3.3.3]{lang="NL-BE"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1932281524}

[[·[              ]{style="font:7.0pt "}]{lang="NL-BE" style="font-size:10.0pt;font-family:Symbol"}**[lsr-id]{lang="EN-US"}**]{#struct_0_24739_x6658_1656099563}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/LDP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1498448553 .myid}
[]{#_Toc404790502}[]{#struct_0_24739_x6658_1282364755}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls mtu**

------------------------------------------------------------------------

[**[mpls mtu]{lang="EN-US"}**]{#struct_0_24739_x6658_2116110846}[命令用来配置接口的]{style="font-family:宋体"}[MPLS MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mpls mtu**]{lang="EN-US"}]{#struct_0_24739_x6658_x183240641}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1070447548}

[**[mpls mtu ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_24739_x6658_x1988595652}

[**[undo mpls mtu]{lang="EN-US"}**]{#struct_0_24739_x6658_1336844539}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1712931240}

[[未配置接口的]{style="font-family:宋体"}[MPLS MTU]{lang="EN-US"}]{#struct_0_24739_x6658_x1968926874}[值，此时根据接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值进行分片，分片的长度不包含]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签栈的长度，为分片添加]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签栈后]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的长度可能会大于接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[的值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1330792293}

[[接口视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_1845081550}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1877129332}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_479009652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_1128541409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x422970460}

[*[value]{lang="EN-US"}*]{#struct_0_24739_x6658_x1607859785}[：接口的]{style="font-family:宋体"}[MPLS MTU]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[46]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x162280155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在接口上使能]{style="font-family:宋体"}]{#struct_0_24739_x6658_987242653}[MPLS]{lang="EN-US"}[功能后，该命令才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的]{style="font-family:宋体"}]{#struct_0_24739_x6658_1441009102}[MPLS MTU]{lang="EN-US"}[值大于接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[时，有可能导致数据转发失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MPLS TE]{lang="EN-US"}]{#struct_0_24739_x6658_134765897}[隧道接口不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x324999067}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_24739_x6658_x1876616406}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_175093685}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_x423035996}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mpls enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mpls mtu 1000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_24739_x6658_762028698}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1629933335}[配置接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_89828345}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] mpls enable]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] mpls mtu 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1487616754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls interface]{lang="EN-US"}**]{#struct_0_24739_x6658_986013793}
:::

::::: {#878451459 .myid}
[]{#_Toc404790503}[]{#struct_0_24739_x6658_1835639281}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS基础命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_24739_x6658_x423101532}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_24739_x6658_1093301615}
:::

[ ]{lang="EN-US"}

[**[mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_2018174006}[命令用来使能指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计功能。]{style="font-family:宋体"}

[**[undo mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_175164079}[命令用来关闭指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1902060759}

[**[mpls statistics ]{lang="EN-US"}**[{ **all** \| \[ **vpn-instance** *vpn-instance-name* \] { **ipv4** *ipv4-destination mask-length* \| **ipv6** *ipv6-destination prefix-length* } \| **static** \| **te** *ingress-lsr-id tunnel-id* }]{lang="EN-US"}]{#struct_0_24739_x6658_1960584173}

[**[undo mpls statistics ]{lang="EN-US"}**[{ **all** \| \[ **vpn-instance** *vpn-instance-name* \] { **ipv4** *ipv4-destination mask-length* \| **ipv6** *ipv6-destination prefix-length* } \| **static** \| **te** *ingress-lsr-id tunnel-id* }]{lang="EN-US"}]{#struct_0_24739_x6658_x423167068}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1508412468}

[[所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_24739_x6658_x1572586963}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计功能均处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1860228273}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1639796937}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1381677717}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1977588134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x640776111}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x422708316}

[**[all]{lang="EN-US"}**]{#struct_0_24739_x6658_x2063620524}[：统计所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_24739_x6658_1107636336}[：统计指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，区分大小写。如果没有指定本参数，则统计公网的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[ipv4 ]{lang="EN-US"}***[ipv4]{lang="EN-US"}[-destination mask-length]{lang="EN-US"}*]{#struct_0_24739_x6658_x727970597}[：统计指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[IPv4 LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[ipv4]{lang="EN-US"}[-destination]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[目的地址，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-destination prefix-length*]{lang="EN-US"}]{#struct_0_24739_x6658_1295778243}[：统计指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[BGP-IPv6 LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[ipv6-destination]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的地址，]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_24739_x6658_214545272}[：统计静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[和静态]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[te]{lang="EN-US"}**[ *ingress-lsr-id tunnel-id*]{lang="EN-US"}]{#struct_0_24739_x6658_1926254245}[：统计指定]{style="font-family:宋体"}[RSVP-TE]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}*[ingress-lsr-id]{lang="EN-US"}*[为入节点的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1686871622}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x422773852}[标签转发是指接收到带有标签的报文后，根据报文中的入标签转发该报文。本命令用来使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发的统计功能。]{style="font-family:宋体"}

[[FTN]{lang="EN-US"}]{#struct_0_24739_x6658_1519017801}[转发是指接收到不带标签的报文，为其添加标签后转发该报文。]{style="font-family:宋体"}[FTN]{lang="EN-US"}[转发的统计功能需要通过]{style="font-family:宋体"}[RIB IPv4]{lang="EN-US"}[地址族视图下的]{style="font-family:宋体"}**[mpls-forwarding statistics prefix-list]{lang="EN-US"}**[命令来使能。]{style="font-family:宋体"}

[[只有通过本命令使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x1889437249}[标签转发统计功能，并通过]{style="font-family:宋体"}**[mpls statistics interval]{lang="EN-US"}**[命令使能统计信息收集功能，用户才能利用]{style="font-family:宋体"}**[display mpls lsp verbose]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1610530470}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x422839388}[使能目的地址为]{style="font-family:宋体"}[2.2.2.2/32]{lang="EN-US"}[的]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_659823447}

[\[Sysname\] mpls statistics ipv4 2.2.2.2 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1483869526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls lsp verbose]{lang="EN-US"}**]{#struct_0_24739_x6658_x716487121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_1713784633}**[ interval]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_x397224148}
:::::

::::: {#-75221162 .myid}
[]{#_Toc404790504}[]{#struct_0_24739_x6658_235730923}[]{#_Toc338752313}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls statistics interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS基础命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_24739_x6658_x422904924}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_24739_x6658_1932930895}
:::

[ ]{lang="EN-US"}

[**[mpls statistics interval]{lang="EN-US"}**]{#struct_0_24739_x6658_x493153283}[命令用来使能]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[标签转发统计信息的收集功能，并设置统计信息收集的时间间隔。]{style="font-family:宋体"}

[**[undo mpls statistics interval]{lang="EN-US"}**]{#struct_0_24739_x6658_x188168247}[命令用来关闭]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[标签转发统计信息的收集功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1836998773}

[**[mpls statistics interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_24739_x6658_x909817274}

[**[undo mpls statistics interval]{lang="EN-US"}**]{#struct_0_24739_x6658_x422446172}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_338892839}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_355322106}[标签转发统计信息收集功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1977309265}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x57060465}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_591713585}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x532065840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x422511708}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x457804332}

[*[interval]{lang="EN-US"}*]{#struct_0_24739_x6658_743973026}[：]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计信息收集的时间间隔，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1541801270}

[[只有通过]{style="font-family:宋体"}**[mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_x1410874347}[命令使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计功能，并通过本命令使能统计信息收集功能，用户才能利用]{style="font-family:宋体"}**[display mpls lsp verbose]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x422970459}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1608318534}[使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签转发统计信息收集功能，并将统计信息收集时间间隔设置为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_x1109383293}

[\[Sysname\] mpls statistics interval 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_268137166}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls lsp verbose]{lang="EN-US"}**]{#struct_0_24739_x6658_428138214}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_x871859946}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_x1469060724}
:::::

::::: {#14186016 .myid}
[]{#_Toc404790505}[]{#struct_0_24739_x6658_x423035995}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls ttl expiration enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS基础命令.files/image001.png){#图片 6 width="63" height="25"}]{lang="EN-US"}]{#struct_0_24739_x6658_762225306}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_24739_x6658_x1383827474}
:::

[ ]{lang="EN-US"}

[**[mpls ttl expiration enable]{lang="EN-US"}**]{#struct_0_24739_x6658_671193065}[命令用来使能]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息发送功能。]{style="font-family:宋体"}

[**[undo mpls ttl expiration enable]{lang="EN-US"}**]{#struct_0_24739_x6658_512550987}[命令用来关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息发送功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1834630327}

[**[mpls ttl expiration enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x829221673}

[**[undo mpls ttl expiration enable]{lang="EN-US"}**]{#struct_0_24739_x6658_x99584694}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x2087710757}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x423101531}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息发送功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1093367151}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_446745960}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1142755088}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x663296612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1210459068}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x474783732}

[[使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_1292793664}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息发送功能后，当]{style="font-family:宋体"}[LSR]{lang="EN-US"}[收到]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[报文时，]{style="font-family:宋体"}[LSR]{lang="EN-US"}[会生成]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息。对于一层标签的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文，]{style="font-family:宋体"}[LSR]{lang="EN-US"}[沿着本地]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由返回]{style="font-family:宋体"}[ICMP TTL]{lang="EN-US"}[超时消息；对于多层标签的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文，]{style="font-family:宋体"}[LSR]{lang="EN-US"}[沿着发送]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[转发]{style="font-family:宋体"}[ICMP TTL]{lang="EN-US"}[超时消息，由]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点将该消息返回给发送者。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x855311743}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息发送功能后，当]{style="font-family:宋体"}[LSR]{lang="EN-US"}[收到]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[报文时，]{style="font-family:宋体"}[LSR]{lang="EN-US"}[不会生成]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x423167067}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_1509264436}[关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时消息发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_x1576470890}

[\[Sysname\] undo mpls ttl expiration enable]{lang="EN-US"}
:::::

::: {#-1399545683 .myid}
[]{#_Toc404790506}[]{#struct_0_24739_x6658_1353197666}

**MPLS基础 \-- MPLS基础配置命令 \-- mpls ttl propagate**

------------------------------------------------------------------------

[**[mpls ttl propagate]{lang="EN-US"}**]{#struct_0_24739_x6658_x668797769}[命令用来使能]{style="font-family:宋体"}[TTL]{lang="EN-US"}[复制功能，即]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文进入]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[域时将]{style="font-family:宋体"}[IP TTL]{lang="EN-US"}[复制到标签的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域；报文离开]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[域时将标签的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[复制到]{style="font-family:宋体"}[IP]{lang="EN-US"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[undo mpls ttl propagate]{lang="EN-US"}**]{#struct_0_24739_x6658_x1617931867}[命令用来禁止]{style="font-family:宋体"}[TTL]{lang="EN-US"}[复制功能，即]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文进入]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[域，为]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文添加标签时，标签的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域取值为]{style="font-family:宋体"}[255]{lang="EN-US"}[；报文离开]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[域时，直接弹出标签，不修改]{style="font-family:宋体"}[IP TTL]{lang="EN-US"}[的值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x681459062}

[**[mpls ttl propagate]{lang="EN-US"}**[ { **public** \| **vpn** }]{lang="EN-US"}]{#struct_0_24739_x6658_448730290}

[**[undo mpls ttl propagate]{lang="EN-US"}**[ { **public** \| **vpn** }]{lang="EN-US"}]{#struct_0_24739_x6658_1335392538}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x422708315}

[[对于通过公网进行转发的报文使能了]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_24739_x6658_x2063554988}[复制功能，对于通过]{style="font-family:宋体"}[VPN]{lang="EN-US"}[进行转发的报文禁止]{style="font-family:宋体"}[TTL]{lang="EN-US"}[复制功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_102481061}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_89141975}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1856804149}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1161207334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x88913703}

[[【参数】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x7626185}

[**[public]{lang="EN-US"}**]{#struct_0_24739_x6658_x328753743}[：对通过公网转发的报文进行设置。]{style="font-family:宋体"}

[**[vpn]{lang="EN-US"}**]{#struct_0_24739_x6658_x422773851}[：对通过]{style="font-family:宋体"}[VPN]{lang="EN-US"}[转发的报文进行设置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1519214409}

[[在]{style="font-family:宋体"}[Ingress]{lang="EN-US"}]{#struct_0_24739_x6658_x291252270}[和]{style="font-family:宋体"}[Egress]{lang="EN-US"}[上都使能]{style="font-family:宋体"}[TTL]{lang="EN-US"}[复制功能后，]{style="font-family:宋体"}[Tracert]{lang="EN-US"}[的结果将反映报文实际经过的路径。]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[骨干网的节点对用户网络的报文可见。]{style="font-family:宋体"}

[[禁止]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_24739_x6658_x1132118970}[复制功能后，]{style="font-family:宋体"}[Tracert]{lang="EN-US"}[的结果不包括]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[骨干网络中的每一跳。]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[骨干网的节点对用户网络的报文不可见，从而隐藏]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[骨干网络的结构。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_24739_x6658_x189545144}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1898607658}[MPLS]{lang="EN-US"}[域内部，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文多层标签之间的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值总是互相复制。]{style="font-family:宋体"}**[mpls ttl propagate]{lang="EN-US"}**[命令只决定是否将]{style="font-family:宋体"}[IP TTL]{lang="EN-US"}[复制到标签的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域、是否将标签的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[复制到]{style="font-family:宋体"}[IP]{lang="EN-US"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议在]{style="font-family:宋体"}]{#struct_0_24739_x6658_1429895397}[LSP]{lang="EN-US"}[经过的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[上配置相同的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域处理方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置]{lang="EN-US" style="font-family:宋体"}**[mpls ttl propagate vpn]{lang="EN-US"}**]{#struct_0_24739_x6658_x499722994}[命令使能对]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[TTL]{lang="EN-US"}[复制功能，则建议在]{lang="EN-US" style="font-family:宋体"}[同一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[所有]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[上都使能此功能，以保证不同的]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[上执行]{lang="EN-US" style="font-family:宋体"}[Tracert]{lang="EN-US"}[得到的]{lang="EN-US" style="font-family:宋体"}[跳数]{style="font-family:宋体"}[结果一致。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1058980581}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x422839387}[使能]{style="font-family:宋体"}[VPN]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[复制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_658971479}

[\[Sysname\] mpls ttl propagate vpn]{lang="EN-US"}[]{#_Toc240361859}[]{#_Toc240363190}[]{#_Toc240863919}[]{#_Toc240883123}[]{#_Toc240962129}[]{#_Toc241398957}[]{#_Toc241399421}[]{#_Toc240361860}[]{#_Toc240363191}[]{#_Toc240863920}[]{#_Toc240883124}[]{#_Toc240962130}[]{#_Toc241398958}[]{#_Toc241399422}[]{#_Toc240361862}[]{#_Toc240363193}[]{#_Toc240863922}[]{#_Toc240883126}[]{#_Toc240962132}[]{#_Toc241398960}[]{#_Toc241399424}[]{#_Toc240361864}[]{#_Toc240363195}[]{#_Toc240863924}[]{#_Toc240883128}[]{#_Toc240962134}[]{#_Toc241398962}[]{#_Toc241399426}[]{#_Toc240361866}[]{#_Toc240363197}[]{#_Toc240863926}[]{#_Toc240883130}[]{#_Toc240962136}[]{#_Toc241398964}[]{#_Toc241399428}[]{#_Toc240361867}[]{#_Toc240363198}[]{#_Toc240863927}[]{#_Toc240883131}[]{#_Toc240962137}[]{#_Toc241398965}[]{#_Toc241399429}[]{#_Toc240361889}[]{#_Toc240363220}[]{#_Toc240863949}[]{#_Toc240883153}[]{#_Toc240962159}[]{#_Toc241398987}[]{#_Toc241399451}[]{#_Toc256529028}[]{#_Toc256530442}[]{#_Toc256529029}[]{#_Toc256530443}[]{#_Toc256529031}[]{#_Toc256530445}[]{#_Toc256529033}[]{#_Toc256530447}[]{#_Toc256529035}[]{#_Toc256530449}[]{#_Toc256529036}[]{#_Toc256530450}[]{#_Toc256529058}[]{#_Toc256530472}[]{#_Toc240361891}[]{#_Toc240363222}[]{#_Toc240863951}[]{#_Toc240883155}[]{#_Toc240962161}[]{#_Toc241398989}[]{#_Toc241399453}[]{#_Toc240361892}[]{#_Toc240363223}[]{#_Toc240863952}[]{#_Toc240883156}[]{#_Toc240962162}[]{#_Toc241398990}[]{#_Toc241399454}[]{#_Toc240361893}[]{#_Toc240363224}[]{#_Toc240863953}[]{#_Toc240883157}[]{#_Toc240962163}[]{#_Toc241398991}[]{#_Toc241399455}[]{#_Toc240361894}[]{#_Toc240363225}[]{#_Toc240863954}[]{#_Toc240883158}[]{#_Toc240962164}[]{#_Toc241398992}[]{#_Toc241399456}[]{#_Toc240361895}[]{#_Toc240363226}[]{#_Toc240863955}[]{#_Toc240883159}[]{#_Toc240962165}[]{#_Toc241398993}[]{#_Toc241399457}[]{#_Toc240361896}[]{#_Toc240363227}[]{#_Toc240863956}[]{#_Toc240883160}[]{#_Toc240962166}[]{#_Toc241398994}[]{#_Toc241399458}[]{#_Toc240361897}[]{#_Toc240363228}[]{#_Toc240863957}[]{#_Toc240883161}[]{#_Toc240962167}[]{#_Toc241398995}[]{#_Toc241399459}[]{#_Toc240361898}[]{#_Toc240363229}[]{#_Toc240863958}[]{#_Toc240883162}[]{#_Toc240962168}[]{#_Toc241398996}[]{#_Toc241399460}[]{#_Toc240361899}[]{#_Toc240363230}[]{#_Toc240863959}[]{#_Toc240883163}[]{#_Toc240962169}[]{#_Toc241398997}[]{#_Toc241399461}[]{#_Toc240361900}[]{#_Toc240363231}[]{#_Toc240863960}[]{#_Toc240883164}[]{#_Toc240962170}[]{#_Toc241398998}[]{#_Toc241399462}[]{#_Toc240361901}[]{#_Toc240363232}[]{#_Toc240863961}[]{#_Toc240883165}[]{#_Toc240962171}[]{#_Toc241398999}[]{#_Toc241399463}[]{#_Toc240361902}[]{#_Toc240363233}[]{#_Toc240863962}[]{#_Toc240883166}[]{#_Toc240962172}[]{#_Toc241399000}[]{#_Toc241399464}[]{#_Toc240361903}[]{#_Toc240363234}[]{#_Toc240863963}[]{#_Toc240883167}[]{#_Toc240962173}[]{#_Toc241399001}[]{#_Toc241399465}[]{#_Toc240361904}[]{#_Toc240363235}[]{#_Toc240863964}[]{#_Toc240883168}[]{#_Toc240962174}[]{#_Toc241399002}[]{#_Toc241399466}[]{#_Toc240361905}[]{#_Toc240363236}[]{#_Toc240863965}[]{#_Toc240883169}[]{#_Toc240962175}[]{#_Toc241399003}[]{#_Toc241399467}[]{#_Toc240361906}[]{#_Toc240363237}[]{#_Toc240863966}[]{#_Toc240883170}[]{#_Toc240962176}[]{#_Toc241399004}[]{#_Toc241399468}[]{#_Toc240361907}[]{#_Toc240363238}[]{#_Toc240863967}[]{#_Toc240883171}[]{#_Toc240962177}[]{#_Toc241399005}[]{#_Toc241399469}[]{#_Toc240361908}[]{#_Toc240363239}[]{#_Toc240863968}[]{#_Toc240883172}[]{#_Toc240962178}[]{#_Toc241399006}[]{#_Toc241399470}[]{#_Toc240361909}[]{#_Toc240363240}[]{#_Toc240863969}[]{#_Toc240883173}[]{#_Toc240962179}[]{#_Toc241399007}[]{#_Toc241399471}[]{#_Toc240361910}[]{#_Toc240363241}[]{#_Toc240863970}[]{#_Toc240883174}[]{#_Toc240962180}[]{#_Toc241399008}[]{#_Toc241399472}[]{#_Toc240361916}[]{#_Toc240363247}[]{#_Toc240863976}[]{#_Toc240883180}[]{#_Toc240962186}[]{#_Toc241399014}[]{#_Toc241399478}[]{#_Toc240361926}[]{#_Toc240363257}[]{#_Toc240863986}[]{#_Toc240883190}[]{#_Toc240962196}[]{#_Toc241399024}[]{#_Toc241399488}[]{#_Toc240361927}[]{#_Toc240363258}[]{#_Toc240863987}[]{#_Toc240883191}[]{#_Toc240962197}[]{#_Toc241399025}[]{#_Toc241399489}[]{#_Toc240361928}[]{#_Toc240363259}[]{#_Toc240863988}[]{#_Toc240883192}[]{#_Toc240962198}[]{#_Toc241399026}[]{#_Toc241399490}[]{#_Toc285094915}[]{#_Toc285094916}[]{#_Toc285094917}[]{#_Toc285094918}[]{#_Toc285094919}[]{#_Toc285094920}[]{#_Toc285094921}[]{#_Toc285094922}[]{#_Toc285094923}[]{#_Toc285094924}[]{#_Toc285094925}[]{#_Toc285094926}[]{#_Toc285094927}[]{#_Toc285094933}[]{#_Toc285094935}[]{#_Toc285094936}[]{#_Toc285094937}[]{#_Toc285094954}[]{#_Toc256529066}[]{#_Toc256530480}[]{#_Toc256529068}[]{#_Toc256530482}[]{#_Toc256529069}[]{#_Toc256530483}[]{#_Toc256529074}[]{#_Toc256530488}[]{#_Toc256529075}[]{#_Toc256530489}[]{#_Toc256529094}[]{#_Toc256530508}[]{#_Toc135304096}[]{#_Toc175386882}[]{#_Toc175453166}[]{#_Toc176010014}[]{#_Toc175386885}[]{#_Toc175453169}[]{#_Toc176010017}[]{#_Toc175386886}[]{#_Toc175453170}[]{#_Toc176010018}[]{#_Toc175386887}[]{#_Toc175453171}[]{#_Toc176010019}[]{#_Toc175386888}[]{#_Toc175453172}[]{#_Toc176010020}[]{#_Toc175386889}[]{#_Toc175453173}[]{#_Toc176010021}[]{#_Toc175386890}[]{#_Toc175453174}[]{#_Toc176010022}[]{#_Toc175386891}[]{#_Toc175453175}[]{#_Toc176010023}[]{#_Toc175386892}[]{#_Toc175453176}[]{#_Toc176010024}[]{#_Toc175386893}[]{#_Toc175453177}[]{#_Toc176010025}[]{#_Toc175386894}[]{#_Toc175453178}[]{#_Toc176010026}[]{#_Toc175386895}[]{#_Toc175453179}[]{#_Toc176010027}[]{#_Toc175386896}[]{#_Toc175453180}[]{#_Toc176010028}[]{#_Toc175386897}[]{#_Toc175453181}[]{#_Toc176010029}[]{#_Toc175386898}[]{#_Toc175453182}[]{#_Toc176010030}[]{#_Toc175386900}[]{#_Toc175453184}[]{#_Toc176010032}[]{#_Toc175386902}[]{#_Toc175453186}[]{#_Toc176010034}[]{#_Toc175386903}[]{#_Toc175453187}[]{#_Toc176010035}[]{#_Toc175386904}[]{#_Toc175453188}[]{#_Toc176010036}[]{#_Toc175386905}[]{#_Toc175453189}[]{#_Toc176010037}[]{#_Toc175386907}[]{#_Toc175453191}[]{#_Toc176010039}[]{#_Toc175386910}[]{#_Toc175453194}[]{#_Toc176010042}[]{#_Toc135304099}[]{#_Toc256529098}[]{#_Toc256530512}[]{#_Toc240363297}[]{#_Toc240864028}[]{#_Toc240883232}[]{#_Toc240962238}[]{#_Toc241399066}[]{#_Toc241399530}[]{#_Toc240363298}[]{#_Toc240864029}[]{#_Toc240883233}[]{#_Toc240962239}[]{#_Toc241399067}[]{#_Toc241399531}[]{#_Toc240363300}[]{#_Toc240864031}[]{#_Toc240883235}[]{#_Toc240962241}[]{#_Toc241399069}[]{#_Toc241399533}[]{#_Toc240363301}[]{#_Toc240864032}[]{#_Toc240883236}[]{#_Toc240962242}[]{#_Toc241399070}[]{#_Toc241399534}[]{#_Toc240363302}[]{#_Toc240864033}[]{#_Toc240883237}[]{#_Toc240962243}[]{#_Toc241399071}[]{#_Toc241399535}[]{#_Toc240363303}[]{#_Toc240864034}[]{#_Toc240883238}[]{#_Toc240962244}[]{#_Toc241399072}[]{#_Toc241399536}[]{#_Toc240363304}[]{#_Toc240864035}[]{#_Toc240883239}[]{#_Toc240962245}[]{#_Toc241399073}[]{#_Toc241399537}[]{#_Toc240363305}[]{#_Toc240864036}[]{#_Toc240883240}[]{#_Toc240962246}[]{#_Toc241399074}[]{#_Toc241399538}[]{#_Toc240363306}[]{#_Toc240864037}[]{#_Toc240883241}[]{#_Toc240962247}[]{#_Toc241399075}[]{#_Toc241399539}[]{#_Toc240363307}[]{#_Toc240864038}[]{#_Toc240883242}[]{#_Toc240962248}[]{#_Toc241399076}[]{#_Toc241399540}[]{#_Toc240363308}[]{#_Toc240864039}[]{#_Toc240883243}[]{#_Toc240962249}[]{#_Toc241399077}[]{#_Toc241399541}[]{#_Toc240363309}[]{#_Toc240864040}[]{#_Toc240883244}[]{#_Toc240962250}[]{#_Toc241399078}[]{#_Toc241399542}[]{#_Toc240363310}[]{#_Toc240864041}[]{#_Toc240883245}[]{#_Toc240962251}[]{#_Toc241399079}[]{#_Toc241399543}[]{#_Toc240363311}[]{#_Toc240864042}[]{#_Toc240883246}[]{#_Toc240962252}[]{#_Toc241399080}[]{#_Toc241399544}[]{#_Toc240363312}[]{#_Toc240864043}[]{#_Toc240883247}[]{#_Toc240962253}[]{#_Toc241399081}[]{#_Toc241399545}[]{#_Toc240363315}[]{#_Toc240864046}[]{#_Toc240883250}[]{#_Toc240962256}[]{#_Toc241399084}[]{#_Toc241399548}[]{#_Toc240363316}[]{#_Toc240864047}[]{#_Toc240883251}[]{#_Toc240962257}[]{#_Toc241399085}[]{#_Toc241399549}[]{#_Toc240363317}[]{#_Toc240864048}[]{#_Toc240883252}[]{#_Toc240962258}[]{#_Toc241399086}[]{#_Toc241399550}[]{#_Toc240363319}[]{#_Toc240864050}[]{#_Toc240883254}[]{#_Toc240962260}[]{#_Toc241399088}[]{#_Toc241399552}[]{#_Toc240363320}[]{#_Toc240864051}[]{#_Toc240883255}[]{#_Toc240962261}[]{#_Toc241399089}[]{#_Toc241399553}[]{#_Toc191266567}[]{#_Toc191888136}[]{#_Toc191891763}[]{#_Toc191266570}[]{#_Toc191888139}[]{#_Toc191891766}[]{#_Toc191266571}[]{#_Toc191888140}[]{#_Toc191891767}[]{#_Toc191266572}[]{#_Toc191888141}[]{#_Toc191891768}[]{#_Toc191266573}[]{#_Toc191888142}[]{#_Toc191891769}[]{#_Toc191266574}[]{#_Toc191888143}[]{#_Toc191891770}[]{#_Toc191266575}[]{#_Toc191888144}[]{#_Toc191891771}[]{#_Toc191266576}[]{#_Toc191888145}[]{#_Toc191891772}[]{#_Toc191266577}[]{#_Toc191888146}[]{#_Toc191891773}[]{#_Toc191266578}[]{#_Toc191888147}[]{#_Toc191891774}[]{#_Toc191266579}[]{#_Toc191888148}[]{#_Toc191891775}[]{#_Toc191266580}[]{#_Toc191888149}[]{#_Toc191891776}[]{#_Toc191266581}[]{#_Toc191888150}[]{#_Toc191891777}[]{#_Toc191266584}[]{#_Toc191888153}[]{#_Toc191891780}[]{#_Toc135304107}[]{#_Toc135304110}[]{#_Toc135304112}[]{#_Toc135304115}[]{#_Toc135304117}[]{#_Toc177806590}[]{#_Toc177806591}[]{#_Toc177806592}[]{#_Toc177806593}[]{#_Toc177806594}[]{#_Toc177806595}[]{#_Toc177806596}[]{#_Toc177806597}[]{#_Toc177806598}[]{#_Toc177806599}[]{#_Toc177806600}[]{#_Toc177806601}[]{#_Toc177806602}[]{#_Toc177806603}[]{#_Toc177806604}[]{#_Toc177806605}[]{#_Toc138750046}[]{#_Toc139164435}[]{#_Toc138750047}[]{#_Toc139164436}[]{#_Toc138750049}[]{#_Toc139164438}[]{#_Toc138750050}[]{#_Toc139164439}[]{#_Toc138750051}[]{#_Toc139164440}[]{#_Toc138750052}[]{#_Toc139164441}[]{#_Toc138750053}[]{#_Toc139164442}[]{#_Toc138750054}[]{#_Toc139164443}[]{#_Toc138750055}[]{#_Toc139164444}[]{#_Toc138750056}[]{#_Toc139164445}[]{#_Toc138750057}[]{#_Toc139164446}[]{#_Toc138750058}[]{#_Toc139164447}[]{#_Toc138750059}[]{#_Toc139164448}[]{#_Toc138750060}[]{#_Toc139164449}[]{#_Toc138750061}[]{#_Toc139164450}[]{#_Toc138750062}[]{#_Toc139164451}[]{#_Toc138750063}[]{#_Toc139164452}[]{#_Toc138750064}[]{#_Toc139164453}[]{#_Toc138750070}[]{#_Toc139164459}[]{#_Toc256529105}
:::

::::: {#1818675733 .myid}
[]{#_Toc404790507}[]{#struct_0_24739_x6658_x77405210}[]{#_Toc338752316}[]{#_Toc383607329}[]{#_Toc383607330}[]{#_Toc383607331}[]{#_Toc383607332}[]{#_Toc383607333}[]{#_Toc383607334}[]{#_Toc383607335}[]{#_Toc383607336}[]{#_Toc383607337}[]{#_Toc383607338}[]{#_Toc383607339}[]{#_Toc383607340}[]{#_Toc383607341}[]{#_Toc383607342}[]{#_Toc383607343}[]{#_Toc383607344}[]{#_Toc383607345}[]{#_Toc383607346}[]{#_Toc383607347}[]{#_Toc383607348}

**MPLS基础 \-- MPLS基础配置命令 \-- reset mpls statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS基础命令.files/image001.png){#图片 5 width="63" height="25"}]{lang="EN-US"}]{#struct_0_24739_x6658_x998380848}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_24739_x6658_x2043992632}
:::

[ ]{lang="EN-US"}

[**[reset mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_844637077}[命令用来清除指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1398186559}

[**[reset mpls statistics ]{lang="EN-US"}**[{ **all** \| \[ **vpn-instance** *vpn-instance-name* \] { **ipv4** *ipv4-destination mask-length* \| **ipv6** *ipv6-destination prefix-length* } \| **static** \| **te** *ingress-lsr-id tunnel-id* }]{lang="EN-US"}]{#struct_0_24739_x6658_x422511707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x456821292}

[[用户视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_x1639022983}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_501698484}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1957313150}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1449628710}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_24739_x6658_8236137}

[**[all]{lang="EN-US"}**]{#struct_0_24739_x6658_690071637}[：清除所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_24739_x6658_x422970462}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，区分大小写。如果没有指定本参数，则清除公网的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[**[ipv4 ]{lang="EN-US"}***[ipv4]{lang="EN-US"}[-destination mask-length]{lang="EN-US"}*]{#struct_0_24739_x6658_x1607990857}[：清除指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[IPv4 LSP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[ipv4]{lang="EN-US"}[-destination]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[目的地址，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-destination prefix-length*]{lang="EN-US"}]{#struct_0_24739_x6658_x1475721944}[：清除指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[BGP-IPv6 LSP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[ipv6-destination]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的地址，]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_24739_x6658_173077242}[：清除静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[和静态]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[te]{lang="EN-US"}**[ *ingress-lsr-id tunnel-id*]{lang="EN-US"}]{#struct_0_24739_x6658_218037741}[：清除指定]{style="font-family:宋体"}[RSVP-TE]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}*[ingress-lsr-id]{lang="EN-US"}*[为入节点的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_621398046}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x1883183031}[清除目的地址为]{style="font-family:宋体"}[2.2.2.2/32]{lang="EN-US"}[的]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset mpls statistics ipv4 2.2.2.2 32]{lang="EN-US"}]{#struct_0_24739_x6658_x185964441}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1909594039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls lsp verbose]{lang="EN-US"}**]{#struct_0_24739_x6658_x423035998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls statistics]{lang="EN-US"}**]{#struct_0_24739_x6658_762946202}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls statistics interval]{lang="EN-US"}**]{#struct_0_24739_x6658_2102067881}
:::::

::: {#675959828 .myid}
[]{#_Toc404790508}[]{#struct_0_24739_x6658_1991859717}

**MPLS基础 \-- MPLS基础配置命令 \-- snmp-agent trap enable mpls**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable mpls**]{lang="EN-US"}]{#struct_0_24739_x6658_x1428406735}[命令用来开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable mpls**]{lang="EN-US"}]{#struct_0_24739_x6658_1991663109}[命令用来关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x1851655526}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **mpls**]{lang="EN-US"}]{#struct_0_24739_x6658_1385031757}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **mpls**]{lang="EN-US"}]{#struct_0_24739_x6658_207219728}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1302884148}

[[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x277678766}[模块的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1803247083}

[[系统视图]{style="font-family:宋体"}]{#struct_0_24739_x6658_1991728645}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x646990984}

[[network-admin]{lang="EN-US"}]{#struct_0_24739_x6658_56824250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_24739_x6658_x1674203588}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_24739_x6658_1059625595}

[[开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_24739_x6658_x1487675953}[模块的告警功能后，该模块会生成告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_24739_x6658_1992580613}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_24739_x6658_x793880565}

[[\# ]{lang="EN-US"}]{#struct_0_24739_x6658_x2125322586}[开启]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_24739_x6658_x1132548632}

[\[Sysname\] snmp-agent trap enable mpls]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
