::: {#1653360252 .myid}
[]{#_Toc404798838}[]{#struct_0_x1633_18491_973833989}[]{#_Toc340162905}

**EVI \-- EVI Probe命令 \-- display system internal evi flooding**

------------------------------------------------------------------------

[**[display system internal evi flooding]{lang="EN-US"}**]{#struct_0_x1633_18491_386687881}[命令用来显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1986878199}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1633_18491_x1501893153}

[**[display system internal evi flooding]{lang="EN-US"}**[ **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1633_18491_1529086960}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1633_18491_x1133294929}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal evi flooding interface]{lang="EN-US"}**[ *interface-type interface-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1633_18491_x1705186304}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1633_18491_1415364844}[模式：]{style="font-family:宋体"}

[**[display system internal evi flooding interface]{lang="EN-US"}**[ *interface-type interface-number* **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1633_18491_x1701521488}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1633_18491_1027751399}

[[Probe]{lang="EN-US"}]{#struct_0_x1633_18491_973899525}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1633_18491_109767943}

[[network-admin]{lang="EN-US"}]{#struct_0_x1633_18491_1036336885}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1633_18491_x1418646528}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x547667606}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x1911698808}[：显示指定接口的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1633_18491_x1984078960}[：显示指定单板的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1633_18491_1600063256}[：显示指定成员设备的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1633_18491_1834613543}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_223194963}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x1243969168}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1633_18491_489309246}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#519267423 .myid}
[]{#_Toc404798839}[]{#struct_0_x1633_18491_x1373972638}[]{#_Toc349048577}[]{#_Toc342471545}[]{#_Toc360181485}[]{#_Toc360181486}[]{#_Toc360181487}[]{#_Toc360181488}[]{#_Toc360181489}[]{#_Toc360181490}[]{#_Toc360181491}[]{#_Toc360181492}[]{#_Toc360181493}[]{#_Toc360181494}[]{#_Toc360181509}

**EVI \-- EVI Probe命令 \-- display system internal evi selective-flooding**

------------------------------------------------------------------------

[**[display system internal evi selective-flooding]{lang="EN-US"}**]{#struct_0_x1633_18491_2123816395}[命令用来显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下指定泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的下发驱动信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1633_18491_419249450}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1633_18491_x1342237030}

[**[display system internal evi selective-flooding interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}***[ ]{lang="EN-US"}[mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1633_18491_1778443261}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1633_18491_x1282037477}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal evi selective-flooding interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}***[ ]{lang="EN-US"}[mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}***[ slot]{lang="EN-US"}**]{#struct_0_x1633_18491_587221285}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1633_18491_973113093}[模式：]{style="font-family:宋体"}

[**[display system internal evi selective-flooding interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}***[ ]{lang="EN-US"}[mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**]{#struct_0_x1633_18491_1039545092}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1633_18491_1893322106}

[[Probe]{lang="EN-US"}]{#struct_0_x1633_18491_1354592154}[视图]{style="font-family:宋体"}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1633_18491_1530936117}

[[network-admin]{lang="EN-US"}]{#struct_0_x1633_18491_1154296508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1633_18491_111438257}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1290593263}

[**[interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1633_18491_1894049131}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口。]{style="font-family:宋体"}

[**[mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_x1633_18491_973178629}[：指定泛洪]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1633_18491_x144094814}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x367706627}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下指定泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的下发驱动信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x2110726901}[：显示指定成员设备的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下指定泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的下发驱动信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x1297554339}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下指定泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的下发驱动信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的]{style="font-family:宋体"}[成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设]{style="font-family:宋体"}[备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1633_18491_488981566}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下指定泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的下发驱动信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-419395048 .myid}
[]{#_Toc404798840}[]{#struct_0_x1633_18491_2090078127}[]{#_Toc349048578}[]{#_Toc342471543}[]{#_Toc360181511}[]{#_Toc360181512}[]{#_Toc360181513}[]{#_Toc360181514}[]{#_Toc360181515}[]{#_Toc360181516}[]{#_Toc360181517}[]{#_Toc360181518}[]{#_Toc360181519}[]{#_Toc360181535}

**EVI \-- EVI Probe命令 \-- display system internal evi statistics**

------------------------------------------------------------------------

[**[display system internal evi statistics]{lang="EN-US"}**]{#struct_0_x1633_18491_973768454}[命令用来显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1633_18491_305750032}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1633_18491_x942924554}

[**[display system internal evi statistics]{lang="EN-US"}**]{#struct_0_x1633_18491_x1304215740}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1633_18491_x1924934482}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal evi statistics slot]{lang="EN-US"}**]{#struct_0_x1633_18491_x465109517}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1633_18491_439873669}[模式：]{style="font-family:宋体"}

[**[display system internal evi statistics chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**]{#struct_0_x1633_18491_72822076}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1633_18491_1084146878}

[[Probe]{lang="EN-US"}]{#struct_0_x1633_18491_973833990}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1569627262}

[[network-admin]{lang="EN-US"}]{#struct_0_x1633_18491_x2075192616}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1633_18491_1614595586}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x746692006}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x2096486311}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x513381873}[：显示指定成员设备的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x847215645}[：显示指定成]{style="font-family:宋体"}[员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}
:::

::: {#-1777368592 .myid}
[]{#_Toc33197998}[]{#_Toc404798841}[]{#struct_0_x1633_18491_x1399015612}[]{#_Toc340162904}[]{#_Toc360181537}[]{#_Toc360181538}[]{#_Toc360181539}[]{#_Toc360181540}[]{#_Toc360181541}[]{#_Toc360181542}[]{#_Toc360181543}[]{#_Toc360181544}[]{#_Toc360181545}[]{#_Toc360181546}[]{#_Toc360181547}[]{#_Toc360181548}[]{#_Toc360181549}[]{#_Toc360181550}[]{#_Toc360181551}[]{#_Toc360181552}[]{#_Toc360181553}[]{#_Toc360181554}[]{#_Toc360181555}[]{#_Toc360181556}[]{#_Toc360181557}[]{#_Toc360181558}[]{#_Toc360181559}[]{#_Toc360181560}[]{#_Toc360181561}[]{#_Toc360181562}[]{#_Toc360181563}[]{#_Toc360181564}[]{#_Toc360181565}[]{#_Toc360181566}[]{#_Toc360181567}[]{#_Toc360181703}

**EVI \-- EVI Probe命令 \-- display system internal evi vlan-mapping**

------------------------------------------------------------------------

[**[display system internal evi vlan-mapping]{lang="EN-US"}**]{#struct_0_x1633_18491_575728594}[命令用来显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x411447997}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1633_18491_126633791}

[**[display system internal evi vlan-mapping vlan]{lang="EN-US"}**[ *vlan-id* **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1633_18491_2003141677}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1633_18491_x686519396}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal evi vlan-mapping vlan]{lang="EN-US"}**[ *vlan-id* **interface** *interface-type interface-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1633_18491_x1114827628}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1633_18491_825310230}[模式：]{style="font-family:宋体"}

[**[display system internal evi vlan-mapping vlan]{lang="EN-US"}**[ *vlan-id* **interface** *interface-type interface-number* **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1633_18491_1510954371}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1398950076}

[[Probe]{lang="EN-US"}]{#struct_0_x1633_18491_x1521836425}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1633_18491_1257475035}

[[network-admin]{lang="EN-US"}]{#struct_0_x1633_18491_872930695}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1633_18491_x1255578472}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1633_18491_806311768}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1633_18491_1963040185}[：显示指定本地]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}[v*lan-id*]{lang="EN-US"}[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1633_18491_1894601668}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_1997726666}[：显示指定单板的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x1398884540}[：显示指定成员设备的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x624678725}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_1741992027}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_x1927436689}[：显示指定单板的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成]{style="font-family:宋体"}[员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1633_18491_489178173}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1214142678 .myid}
[]{#_Toc404798842}[]{#struct_0_x1633_18491_1801131188}[]{#_Toc349048579}[]{#_Toc342471544}[]{#_Toc360181705}[]{#_Toc360181706}[]{#_Toc360181707}[]{#_Toc360181708}[]{#_Toc360181709}[]{#_Toc360181710}[]{#_Toc360181711}[]{#_Toc360181712}[]{#_Toc360181713}[]{#_Toc360181714}[]{#_Toc360181715}[]{#_Toc360181731}

**EVI \-- EVI Probe命令 \-- display system internal evi vlan-status**

------------------------------------------------------------------------

[**[display system internal evi vlan-status]{lang="EN-US"}**]{#struct_0_x1633_18491_1126799454}[命令用来显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下发驱动信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x702788361}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1633_18491_x2116053410}

[**[display system internal evi vlan-status interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1633_18491_x2133006811}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1633_18491_x1398687932}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal evi vlan-status interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}***[ slot]{lang="EN-US"}**]{#struct_0_x1633_18491_x1511155299}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1633_18491_194442027}[模式：]{style="font-family:宋体"}

[**[display system internal evi vlan-status interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}***[ vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**]{#struct_0_x1633_18491_x663731377}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x758213118}

[[Probe]{lang="EN-US"}]{#struct_0_x1633_18491_x601582570}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x184416239}

[[network-admin]{lang="EN-US"}]{#struct_0_x1633_18491_x1186910687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1633_18491_2073520230}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1398622396}

[**[interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1633_18491_x1314082923}[：指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1633_18491_1549995444}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_196863201}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下发驱动信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_1462779071}[：显示指定成员设备的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下发驱动]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_538120689}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下发驱动信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编]{style="font-family:宋体"}[号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1633_18491_489374781}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[EVI]{lang="EN-US"}[保存的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下发驱动信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#665348980 .myid}
[]{#_Toc404798843}[]{#struct_0_x1633_18491_x447745365}[]{#_Toc345077579}[]{#_Toc360181733}[]{#_Toc360181734}[]{#_Toc360181735}[]{#_Toc360181736}[]{#_Toc360181737}[]{#_Toc360181738}[]{#_Toc360181739}[]{#_Toc360181740}[]{#_Toc360181741}[]{#_Toc360181758}

**EVI \-- EVI Probe命令 \-- display system internal eviisis status**

------------------------------------------------------------------------

[**[display system internal eviisis status]{lang="EN-US"}**]{#struct_0_x1633_18491_x2117094498}[命令用来显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1633_18491_1910006034}

[**[display system internal eviisis status]{lang="EN-US"}**]{#struct_0_x1633_18491_x2087719332}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x976952258}

[[Probe]{lang="EN-US"}]{#struct_0_x1633_18491_x1754338281}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1239159997}

[[network-admin]{lang="EN-US"}]{#struct_0_x1633_18491_983975915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1633_18491_x1399015611}
:::

::: {#-1628633610 .myid}
[]{#_Toc404798844}[]{#struct_0_x1633_18491_603271147}[]{#_Toc342056480}[]{#_Toc338505887}[]{#_Toc360181760}[]{#_Toc360181761}[]{#_Toc360181762}[]{#_Toc360181763}[]{#_Toc360181764}[]{#_Toc360181765}[]{#_Toc360181766}[]{#_Toc360181767}[]{#_Toc360181768}[]{#_Toc360181769}[]{#_Toc360181770}[]{#_Toc360181771}[]{#_Toc360181772}[]{#_Toc360181773}[]{#_Toc360181774}[]{#_Toc360181799}

**EVI \-- EVI Probe命令 \-- display system internal evi-link data**

------------------------------------------------------------------------

[**[display system internal evi-link data]{lang="EN-US"}**]{#struct_0_x1633_18491_1544389105}[命令用来显示]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1398753467}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1633_18491_x77387304}

[**[display system internal evi-link data interface evi-link]{lang="EN-US"}**[ *number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1633_18491_x1259047015}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1633_18491_x1779260276}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal evi-link data interface evi-link]{lang="EN-US"}**[ *number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1633_18491_1391336326}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1633_18491_x1355070968}[模式：]{style="font-family:宋体"}

[**[display system internal evi-link data interface evi-link]{lang="EN-US"}**[ *number* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1633_18491_1632951824}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1633_18491_359374682}

[[Probe]{lang="EN-US"}]{#struct_0_x1633_18491_x786744955}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x1398687931}

[[network-admin]{lang="EN-US"}]{#struct_0_x1633_18491_54928642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1633_18491_1582504656}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1633_18491_x570799819}

[**[interface evi-link ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1633_18491_x925374163}[：显示指定]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口的内核数据信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口编号，取值为已创建的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口编号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_407776913}[：显示指定单板的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示主用主控板的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_353961715}[：显示指定成员设备的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示主成员设备的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_134836162}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则显示主成员设备的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_225685262}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示全局主用主控板的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1633_18491_1521858710}[：显示指定单板的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则显示全局主用主控板的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1633_18491_x1076512547}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
