::: {#-1275460878 .myid}
[]{#_Toc404800472}[]{#struct_0_x1213_20198_x1626193508}

**以太网接口 \-- 以太网接口 Probe命令 \-- display system internal ethernet controlblock**

------------------------------------------------------------------------

[**[display system internal ethernet controlblock]{lang="EN-US"}**]{#struct_0_x1213_20198_1471635125}[命令用来显示接口的控制块信息，它记录了链路层参数的值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1213_20198_1956549268}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1213_20198_x714517339}

[**[display system internal ethernet controlblock interface]{lang="EN-US"}**[ { *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_x1213_20198_1040402201}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1213_20198_1639668252}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ethernet controlblock interface]{lang="EN-US"}**[ { *interface-type interface-number* } **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1213_20198_x1310148179}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1213_20198_x504385914}[模式：]{style="font-family:宋体"}

[**[display system internal ethernet controlblock interface]{lang="EN-US"}**[ { *interface-type interface-number* } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1213_20198_x2011985487}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1213_20198_x286883821}

[[Probe]{lang="EN-US"}]{#struct_0_x1213_20198_x1606233899}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1213_20198_x1919559309}

[[network-admin]{lang="EN-US"}]{#struct_0_x1213_20198_881308744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1213_20198_1524798285}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1213_20198_x835463074}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1213_20198_713971507}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_1687008196}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_472896146}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_409270398}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_x2012051023}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1213_20198_x1963841349}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1213_20198_495103239}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1361629797 .myid}
[]{#_Toc404800473}[]{#struct_0_x1213_20198_1411284341}[]{#_Toc360006369}[]{#_Toc360006370}[]{#_Toc360006371}[]{#_Toc360006372}[]{#_Toc360006373}[]{#_Toc360006374}[]{#_Toc360006375}[]{#_Toc360006376}[]{#_Toc360006377}[]{#_Toc360006378}[]{#_Toc360006379}[]{#_Toc360006380}[]{#_Toc360006381}[]{#_Toc360006382}[]{#_Toc360006383}[]{#_Toc360006384}[]{#_Toc360006385}[]{#_Toc360006386}[]{#_Toc360006387}[]{#_Toc360006388}[]{#_Toc360006389}[]{#_Toc360006390}[]{#_Toc360006391}[]{#_Toc360006392}[]{#_Toc360006393}[]{#_Toc360006394}[]{#_Toc360006395}[]{#_Toc360006396}[]{#_Toc360006397}[]{#_Toc360006431}

**以太网接口 \-- 以太网接口 Probe命令 \-- display system internal ethernet character**

------------------------------------------------------------------------

[**[display system internal ethernet character]{lang="EN-US"}**]{#struct_0_x1213_20198_x2012378703}[命令用来显示以太网模块侦听的特征统计信息和详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1213_20198_x1409992084}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1213_20198_890137091}

[**[display system internal ethernet character]{lang="EN-US"}**[ { **global** \| **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_x1213_20198_947862995}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1213_20198_1802909941}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ethernet character]{lang="EN-US"}**[ { **global** \| **interface** *interface-type interface-number* } **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1213_20198_x182830022}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1213_20198_2064598384}[模式：]{style="font-family:宋体"}

[**[display system internal ethernet character]{lang="EN-US"}**[ { **global** \| **interface** *interface-type interface-number* } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1213_20198_723624590}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1213_20198_1174778956}

[[Probe]{lang="EN-US"}]{#struct_0_x1213_20198_679317459}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1213_20198_x2012444239}

[[network-admin]{lang="EN-US"}]{#struct_0_x1213_20198_960668776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1213_20198_x1403347174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1213_20198_1366935879}

[**[global]{lang="EN-US"}**]{#struct_0_x1213_20198_x1721656913}[：显示全局的以太特征。全局特征表示对设备上所有报文进行匹配。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1213_20198_1505117719}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_x1461211905}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_x1461211906}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_x801041935}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1213_20198_1081690113}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1213_20198_x411998950}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1213_20198_434992943}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1213_20198_x1321959014}

[[以太网模块主要实现链路层报文接收去封装和发送加封装等处理。上层应用模块（如]{style="font-family:宋体"}[STP]{lang="EN-US"}]{#struct_0_x1213_20198_1719895718}[，]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[等）需要侦听处理协议报文，指定侦听的范围（如指定接口上的报文或者设备上所有报文），侦听的协议报文具有指定的特征（如特殊的以太协议类型、特定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[等），并将这些特征下发给以太网模块，以太网模块在指定阶段（如收包]{style="font-family:宋体"}[MAC]{lang="EN-US"}[阶段]{style="font-family:宋体"}[/]{lang="EN-US"}[收包]{style="font-family:宋体"}[LLC]{lang="EN-US"}[阶段]{style="font-family:宋体"}[/]{lang="EN-US"}[发包三层口阶段等）会根据注册的特征库对报文进行匹配。匹配上了这些特征就交给这个阶段处理，不匹配就交给下一个阶段处理。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
