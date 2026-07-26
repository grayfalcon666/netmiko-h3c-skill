::::: {#1431668441 .myid}
[]{#_Toc404799818}[]{#struct_0_x6778_81963_x1934439057}[]{#_Toc375143314}[]{#_Toc375143315}[]{#_Toc375143316}[]{#_Toc375143317}[]{#_Toc375143318}[]{#_Toc375143319}[]{#_Toc375143320}[]{#_Toc375143321}[]{#_Toc375143322}[]{#_Toc375143323}[]{#_Toc375143324}[]{#_Toc375143325}[]{#_Toc375143326}[]{#_Toc375143327}[]{#_Toc375143328}[]{#_Toc375143329}[]{#_Toc375143330}[]{#_Toc375143331}[]{#_Toc375143332}[]{#_Toc375143333}[]{#_Toc375143334}[]{#_Toc375143335}[]{#_Toc360006500}[]{#_Toc360006501}[]{#_Toc360006502}[]{#_Toc360006503}[]{#_Toc360006504}[]{#_Toc360006505}[]{#_Toc360006506}[]{#_Toc360006507}[]{#_Toc360006508}[]{#_Toc360006509}[]{#_Toc360006510}[]{#_Toc360006511}[]{#_Toc360006512}[]{#_Toc360006513}[]{#_Toc360006532}

**MBUF \-- MBUF Probe命令 \-- display system internal mbuf relay statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MBUF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6778_81963_x82224192}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6778_81963_x826837681}
:::

[ ]{lang="EN-US"}

[**[display system internal mbuf relay ]{lang="EN-US"}[statistics]{lang="EN-US"}**]{#struct_0_x6778_81963_x1108767415}[命令用来显示]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6778_81963_835976875}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6778_81963_x336796822}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mbuf relay ]{lang="EN-US"}[statistics]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-numbe* \] \[ **vcpu** *vcpu-number* \[ **rcv** *receiver-id* \] \]]{lang="EN-US"}]{#struct_0_x6778_81963_x1786840702}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6778_81963_1931702335}[模式：]{style="font-family:宋体"}

[**[display system internal mbuf relay ]{lang="EN-US"}[statistics]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-numbe* \] \[ **vcpu** *vcpu-number* \[ **rcv** *receiver-id* \] \]]{lang="EN-US"}]{#struct_0_x6778_81963_752680435}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6778_81963_x127448838}

[[Probe]{lang="EN-US"}]{#struct_0_x6778_81963_x1867733455}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6778_81963_1872174131}

[[network-admin]{lang="EN-US"}]{#struct_0_x6778_81963_1039599443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6778_81963_x494844751}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6778_81963_28047632}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6778_81963_786210610}[：显示指定单板的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6778_81963_1931636799}[：显示指定成员设备的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6778_81963_1299249959}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6778_81963_1963862954}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6778_81963_x266833982}[：显示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6778_81963_1530739709}[：]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继使用的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vcpu]{lang="EN-US"}**]{#struct_0_x6778_81963_x1465537282}[ v*cpu-*]{lang="EN-US"}*[number]{lang="EN-US"}*[：]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继使用的]{style="font-family:宋体"}[VCPU]{lang="EN-US"}[的]{style="font-family:宋体"}[编号。不指定该参数时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示当前单板上的所有]{style="font-family:宋体"}[VCPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rcv ]{lang="EN-US"}***[received-id]{lang="EN-US"}*]{#struct_0_x6778_81963_x1201650442}[：]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继接收者的编号。不指定该参数时，表示当前]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有接收者。]{style="font-family:宋体"}
:::::

::::: {#1109228169 .myid}
[]{#_Toc404799819}[]{#struct_0_x6778_81963_x667922539}[]{#_Toc360006534}[]{#_Toc360006535}[]{#_Toc360006536}[]{#_Toc360006537}[]{#_Toc360006538}[]{#_Toc360006539}[]{#_Toc360006540}[]{#_Toc360006541}[]{#_Toc360006542}[]{#_Toc360006543}[]{#_Toc360006544}[]{#_Toc360006545}[]{#_Toc360006546}[]{#_Toc360006547}[]{#_Toc360006548}[]{#_Toc360006549}[]{#_Toc360006550}[]{#_Toc360006551}[]{#_Toc360006552}[]{#_Toc360006553}[]{#_Toc360006554}[]{#_Toc360006555}[]{#_Toc360006556}[]{#_Toc360006557}[]{#_Toc360006558}[]{#_Toc360006559}[]{#_Toc360006560}[]{#_Toc360006561}[]{#_Toc360006562}[]{#_Toc360006563}[]{#_Toc360006564}[]{#_Toc360006565}[]{#_Toc360006566}[]{#_Toc360006567}[]{#_Toc360006694}

**MBUF \-- MBUF Probe命令 \-- reset system internal mbuf relay statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MBUF%20Probe命令.files/image001.png){#图片 43 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6778_81963_1931440190}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6778_81963_x799337314}
:::

[ ]{lang="EN-US"}

[**[reset system internal mbuf relay ]{lang="EN-US"}[statistics]{lang="EN-US"}**]{#struct_0_x6778_81963_1327340157}[命令用来清除]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6778_81963_x1923009536}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6778_81963_60385752}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal mbuf relay ]{lang="EN-US"}[statistics]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-numbe* \] \[ **vcpu** *vcpu-number* \[ **rcv** *receiver-id* \] \]]{lang="EN-US"}]{#struct_0_x6778_81963_332971373}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6778_81963_x2124445359}[模式：]{style="font-family:宋体"}

[**[reset system internal mbuf relay ]{lang="EN-US"}[statistics]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-numbe* \] \[ **vcpu** *vcpu-number* \[ **rcv** *receiver-id* \] \]]{lang="EN-US"}]{#struct_0_x6778_81963_x2080336162}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6778_81963_1931374654}

[[Probe]{lang="EN-US"}]{#struct_0_x6778_81963_x1162526001}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6778_81963_x95512938}

[[network-admin]{lang="EN-US"}]{#struct_0_x6778_81963_1772560955}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6778_81963_331166814}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6778_81963_x791240255}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6778_81963_x462215809}[：清除指定单板的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6778_81963_2112513961}[：清除指定成员设备的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6778_81963_x1832917923}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6778_81963_2022677240}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6778_81963_1050642736}[：清除指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继模块的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6778_81963_1931571262}[：]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继使用的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vcpu]{lang="EN-US"}**]{#struct_0_x6778_81963_x1465537286}[ v*cpu-*]{lang="EN-US"}*[ number]{lang="EN-US"}*[：]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继使用的]{style="font-family:宋体"}[VCPU]{lang="EN-US"}[的]{style="font-family:宋体"}[编号。不指定该参数时，表示当前单板上的所有]{style="font-family:宋体"}[VCPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rcv ]{lang="EN-US"}***[received-id]{lang="EN-US"}*]{#struct_0_x6778_81963_x801005609}[：]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中继接收者的编号。不指定该参数时，表示当前]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有接收者。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::::
