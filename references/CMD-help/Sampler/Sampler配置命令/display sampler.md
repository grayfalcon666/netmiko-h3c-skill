::: {#2110356285 .myid}
[]{#_Toc404797152}[]{#struct_0_27289_x6771_207812095}[]{#_Toc55050581}[]{#_Toc28576987}

**Sampler \-- Sampler配置命令 \-- display sampler**

------------------------------------------------------------------------

[**[display sampler]{lang="EN-US"}**]{#struct_0_27289_x6771_878520352}[命令用来查看采样器的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_27289_x6771_x1615651681}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_27289_x6771_1118108282}

[**[display sampler ]{lang="EN-US"}**[\[ *sampler-name* \]]{lang="EN-US"}]{#struct_0_27289_x6771_1923918294}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_27289_x6771_1378173609}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display sampler ]{lang="EN-US"}**[\[ *sampler-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_27289_x6771_x1755272829}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_27289_x6771_90578062}[模式：]{style="font-family:宋体"}

[**[display sampler ]{lang="EN-US"}**[\[ *sampler-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_27289_x6771_1802984098}

[[【视图】]{style="font-family:黑体"}]{#struct_0_27289_x6771_x1734806216}

[[任意视图]{style="font-family:宋体"}]{#struct_0_27289_x6771_716106268}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_27289_x6771_x45210748}

[[network-admin]{lang="EN-US"}]{#struct_0_27289_x6771_1780990401}

[[network-operator]{lang="EN-US"}]{#struct_0_27289_x6771_616986186}

[[mdc-admin]{lang="EN-US"}]{#struct_0_27289_x6771_539012072}

[[mdc-operator]{lang="EN-US"}]{#struct_0_27289_x6771_1378108073}

[[【参数】]{style="font-family:黑体"}]{#struct_0_27289_x6771_604409875}

[*[sampler-name]{lang="EN-US"}*]{#struct_0_27289_x6771_x1810576602}[：采样器名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。未指定该参数时，将显示所有采样器的信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_27289_x6771_x896507044}[：查看指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。未指定该参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_27289_x6771_x1249273179}[：查看指定成员设备上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。未指定该参数时，将显示主用设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_27289_x6771_x1565334466}[：查看指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数时，将显示主用设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_27289_x6771_1305142759}[：查看指定成员设备上指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。未指定该参数时，将显示主用设备主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_27289_x6771_x649854069}[：查看指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位号。如果未指定该参数时，将显示主用设备主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_27289_x6771_x1672331421}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_27289_x6771_x1924646246}

[[\# ]{lang="EN-US"}]{#struct_0_27289_x6771_2048564122}[查看采样器]{style="font-family:宋体"}[256]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display sampler 256]{lang="EN-US"}]{#struct_0_27289_x6771_291529994}

[ Sampler name: 256]{lang="EN-US"}

[  Mode: Fixed;  Packet-interval: 8]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_27289_x6771_1377649322}[查看采样器]{style="font-family:宋体"}[256]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的配置信息。（分布式设备－独立运行模式）]{style="font-family:
宋体"}

[[\<Sysname\> display sampler 256 slot 1]{lang="EN-US"}]{#struct_0_27289_x6771_x355984560}

[ Sampler name: 256]{lang="EN-US"}

[  Mode: Fixed;  Packet-interval: 8]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_27289_x6771_1538990204}[查看采样器]{style="font-family:宋体"}[256]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号框]{style="font-family:
宋体"}[1]{lang="EN-US"}[号单板上的配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display sampler 256 chassis 1 slot 1]{lang="EN-US"}]{#struct_0_27289_x6771_978195443}

[ Sampler name: 256]{lang="EN-US"}

[  Mode: Fixed;  Packet-interval: 8]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display sampler]{lang="EN-US"}]{#struct_0_27289_x6771_x593205041}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x683665165}[[字段]{style="font-family:黑体"}]{#struct_0_27289_x6771_x828931249}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_27289_x6771_x876710316}

[[Sampler name]{lang="EN-US"}]{#struct_0_27289_x6771_1377583786}

[[采样器名称]{style="font-family:宋体"}]{#struct_0_27289_x6771_372680967}

[[Mode]{lang="EN-US"}]{#struct_0_27289_x6771_x728415389}

[[采样器模式，包括固定采样（]{style="font-family:宋体"}[Fixed]{lang="EN-US"}]{#struct_0_27289_x6771_x2005621874}[）和随机采样（]{style="font-family:宋体"}[Random]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Packet-interval]{lang="EN-US"}]{#struct_0_27289_x6771_x2139660046}

[[采样率]{style="font-family:宋体"}]{#struct_0_27289_x6771_x977112277}

[]{#_Toc150663363}[ ]{lang="EN-US"}

::: {#-1071821280 .myid}
[]{#_Toc404797153}[]{#struct_0_27289_x6771_x1727599827}

**Sampler \-- Sampler配置命令 \-- sampler**

------------------------------------------------------------------------

[**[sampler]{lang="EN-US"}**]{#struct_0_27289_x6771_1243096835}[命令用来创建采样器。]{style="font-family:宋体"}

[**[undo sampler]{lang="EN-US"}**]{#struct_0_27289_x6771_1377518250}[命令用来删除指定采样器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_27289_x6771_401444745}

[**[sampler ]{lang="EN-US"}***[sampler-name]{lang="EN-US"}***[ mode ]{lang="EN-US"}**[{ **fixed** \| **random** } **packet-interval** *rate*]{lang="EN-US"}]{#struct_0_27289_x6771_480863558}

[**[undo sampler ]{lang="EN-US"}***[sampler-name]{lang="EN-US"}*]{#struct_0_27289_x6771_x609069396}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_27289_x6771_x1941304855}

[[未创建任何采样器。]{style="font-family:宋体"}]{#struct_0_27289_x6771_x1570650246}

[[【视图】]{style="font-family:黑体"}]{#struct_0_27289_x6771_1881439114}

[[系统视图]{style="font-family:宋体"}]{#struct_0_27289_x6771_x970438992}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_27289_x6771_656498094}

[[network-admin]{lang="EN-US"}]{#struct_0_27289_x6771_x563267855}

[[mdc-admin]{lang="EN-US"}]{#struct_0_27289_x6771_1377452714}

[[【参数】]{style="font-family:黑体"}]{#struct_0_27289_x6771_x1173938760}

[*[sampler-name]{lang="EN-US"}*]{#struct_0_27289_x6771_1155803710}[：采样器名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[fixed]{lang="EN-US"}**]{#struct_0_27289_x6771_515294775}[：采样方式为固定采样，表示每组报文中的第一个报文被抽取。]{style="font-family:宋体"}

[**[random]{lang="EN-US"}**]{#struct_0_27289_x6771_274064070}[：采样方式为随机采样，表示每组报文中，任意一个报文都有可能被抽取。]{style="font-family:宋体"}

[*[rate]{lang="EN-US"}*]{#struct_0_27289_x6771_x568248426}[：采样率，即在指定的多个报文中抽取一个报文进行采样。对于硬件采样，按照]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}*[rate]{lang="EN-US"}*[次方进行计算。例如，该参数设为]{style="font-family:宋体"}[8]{lang="EN-US"}[，表示在]{style="font-family:宋体"}[256]{lang="EN-US"}[（]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:
宋体"}[8]{lang="EN-US"}[次方）个报文中采样]{style="font-family:宋体"}[1]{lang="EN-US"}[个报文；该参数设为]{style="font-family:宋体"}[10]{lang="EN-US"}[，表示在]{style="font-family:宋体"}[1024]{lang="EN-US"}[（]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:
宋体"}[10]{lang="EN-US"}[次方）个报文中采样]{style="font-family:宋体"}[1]{lang="EN-US"}[个报文；对于软件采样，按照用户输入的实际参数进行采样。例如，该参数设为]{style="font-family:宋体"}[100]{lang="EN-US"}[，表示在]{style="font-family:宋体"}[100]{lang="EN-US"}[个报文中采样]{style="font-family:宋体"}[1]{lang="EN-US"}[个报文。不同型号的设备支持的取值范围和实际采样率不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_27289_x6771_x1598391353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同型号的设备支持的采样器数目不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_27289_x6771_648938743}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令对所有单板生效。（分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_27289_x6771_x1574652132}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_27289_x6771_1377387178}

[[\# ]{lang="EN-US"}]{#struct_0_27289_x6771_x449545168}[创建一个名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的采样器，采用固定采样方式，设置采样率为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_27289_x6771_x1137396896}

[\[Sysname\] sampler abc mode fixed packet-interval 8]{lang="EN-US"}
:::
