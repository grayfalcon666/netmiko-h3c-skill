::: {#1252842756 .myid}
[]{#_Toc404799920}[]{#struct_0_66891_x1431_488108267}[]{#_Toc349205712}

**MPLS基础 \-- MPLS基础Probe命令 \-- debugging system internal mpls lfib**

------------------------------------------------------------------------

[**[debugging system internal mpls lfib]{lang="EN-US"}**]{#struct_0_66891_x1431_1763539252}[命令用来打开]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[模块的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging system internal mpls lfib]{lang="EN-US"}**]{#struct_0_66891_x1431_1001136870}[命令用来关闭]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[模块的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x134345468}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_798989105}

[**[debugging system internal mpls lfib]{lang="EN-US"}**[ { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** }]{lang="EN-US"}]{#struct_0_66891_x1431_1516847783}

[**[undo]{lang="EN-US"}**[ **debugging system internal mpls lfib** { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** }]{lang="EN-US"}]{#struct_0_66891_x1431_x1300203329}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_1484293316}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging system internal mpls lfib]{lang="EN-US"}**[ { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } ]{lang="EN-US"}]{#struct_0_66891_x1431_1467351832}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **debugging system internal mpls lfib** { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } **slot** ]{lang="EN-US"}]{#struct_0_66891_x1431_x120534899}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_x600166698}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[debugging system internal mpls lfib]{lang="EN-US"}**[ { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } ]{lang="EN-US"}]{#struct_0_66891_x1431_x945432053}**[chassis]{lang="PT-BR"}**[ ]{lang="PT-BR"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **debugging system internal mpls lfib** { **all** \| **config** \| **ilm** \| **message** \| **nhlfe** \| **sync** } ]{lang="EN-US"}]{#struct_0_66891_x1431_1516913319}**[chassis]{lang="PT-BR"}**[ ]{lang="PT-BR"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x109992405}

[[MPLS LFIB]{lang="EN-US"}]{#struct_0_66891_x1431_x520746863}[模块的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_288364614}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x1920314259}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1646517446}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x732234713}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x273936507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x1557741946}

[**[all]{lang="EN-US"}**]{#struct_0_66891_x1431_x1229365805}[：表示]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[config]{lang="EN-US"}**]{#struct_0_66891_x1431_1516716711}[：表示]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[配置消息调试信息开关。]{style="font-family:宋体"}

[**[ilm]{lang="EN-US"}**]{#struct_0_66891_x1431_1413672440}[：表示]{style="font-family:宋体"}[MPLS LFIB ILM]{lang="EN-US"}[相关调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_66891_x1431_1128995753}[：表示]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[消息相关调试信息开关。]{style="font-family:宋体"}

[**[nhlfe]{lang="EN-US"}**]{#struct_0_66891_x1431_1935201517}[：表示]{style="font-family:宋体"}[MPLS LFIB NHLFE]{lang="EN-US"}[相关调试信息开关。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_66891_x1431_2073731265}[：表示]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[同步相关调试信息开关。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_2141041618}*[ slot-number]{lang="PT-BR"}*[：表示指定单板的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_1802546161}*[ slot-number]{lang="PT-BR"}*[：表示指定成员设备的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_92428536}*[ slot-number]{lang="PT-BR"}*[：表示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_x582349705}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：表示指定成员设备上指定单板的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_2108851171}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：表示指定单板的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1295550622}[：指定单板]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-358729516 .myid}
[]{#_Toc349205705}[]{#_Toc404799921}[]{#struct_0_66891_x1431_262216585}[]{#_Toc352328277}[]{#_Toc360181328}[]{#_Toc361312398}[]{#_Toc360181329}[]{#_Toc361312399}[]{#_Toc360181330}[]{#_Toc361312400}[]{#_Toc360181331}[]{#_Toc361312401}[]{#_Toc360181332}[]{#_Toc361312402}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls forwarding temporary-ilm**

------------------------------------------------------------------------

[**[display system internal mpls forwarding temporary-ilm]{lang="EN-US"}**]{#struct_0_66891_x1431_x2104440535}[命令用来显示临时保存的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1517109927}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_x1331677884}

[**[display system internal mpls forwarding temporary-ilm ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ ]{lang="EN-US"}**]{#struct_0_66891_x1431_131527100}*[label ]{lang="EN-US"}*[\]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_66891_x1431_x1004302132}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mpls forwarding temporary-ilm ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ ]{lang="EN-US"}**]{#struct_0_66891_x1431_1517175463}*[label ]{lang="EN-US"}*[\]]{lang="EN-US"}[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_66891_x1431_689070812}[模式：]{style="font-family:宋体"}

[**[display system internal mpls forwarding temporary-ilm]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_66891_x1431_1498781003}*[label]{lang="EN-US"}*[ \] **chassis** ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1676010417}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_1048982791}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1516978855}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x99702568}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x652049654}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1582309854}

[*[label]{lang="EN-US"}*]{#struct_0_66891_x1431_1517044391}[：显示指定入标签的临时]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项，不同型号的设备支持的取值范围不同，请以设备的实际情况为准]{style="font-family:宋体"}[。如果不指定本参数，]{style="font-family:宋体"}[则显示所有的临时]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_1463932809}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定单板上的临时]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_1073819684}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定成员设备上的临时]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_542767230}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的临时]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_x998425637}*[chassis-number]{lang="PT-BR"}*[ **slot**]{lang="PT-BR"}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的临时]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_x1080750888}*[chassis-number]{lang="PT-BR"}*[ **slot**]{lang="PT-BR"}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定单板的临时]{style="font-family:宋体"}[ILM]{lang="PT-BR"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1296074909}[：显示指定]{style="font-family:宋体"}[CP]{lang="EN-US"}[U]{lang="EN-US"}[的临时]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#303184048 .myid}
[]{#_Toc404799922}[]{#struct_0_66891_x1431_1795279143}[]{#_Toc360181334}[]{#_Toc361312404}[]{#_Toc360181335}[]{#_Toc361312405}[]{#_Toc360181336}[]{#_Toc361312406}[]{#_Toc360181337}[]{#_Toc361312407}[]{#_Toc360181338}[]{#_Toc361312408}[]{#_Toc360181339}[]{#_Toc361312409}[]{#_Toc360181340}[]{#_Toc361312410}[]{#_Toc360181341}[]{#_Toc361312411}[]{#_Toc360181342}[]{#_Toc361312412}[]{#_Toc360181343}[]{#_Toc361312413}[]{#_Toc360181344}[]{#_Toc361312414}[]{#_Toc360181345}[]{#_Toc361312415}[]{#_Toc360181346}[]{#_Toc361312416}[]{#_Toc360181347}[]{#_Toc361312417}[]{#_Toc360181348}[]{#_Toc361312418}[]{#_Toc360181349}[]{#_Toc361312419}[]{#_Toc360181350}[]{#_Toc361312420}[]{#_Toc360181351}[]{#_Toc361312421}[]{#_Toc360181352}[]{#_Toc361312422}[]{#_Toc360181353}[]{#_Toc361312423}[]{#_Toc360181354}[]{#_Toc361312424}[]{#_Toc360181355}[]{#_Toc361312425}[]{#_Toc360181356}[]{#_Toc361312426}[]{#_Toc360181357}[]{#_Toc361312427}[]{#_Toc360181358}[]{#_Toc361312428}[]{#_Toc360181359}[]{#_Toc361312429}[]{#_Toc360181360}[]{#_Toc361312430}[]{#_Toc360181361}[]{#_Toc361312431}[]{#_Toc360181362}[]{#_Toc361312432}[]{#_Toc360181363}[]{#_Toc361312433}[]{#_Toc360181364}[]{#_Toc361312434}[]{#_Toc352328278}[]{#_Toc360181398}[]{#_Toc361312468}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib ilm**

------------------------------------------------------------------------

[**[display system internal mpls lfib ilm]{lang="EN-US"}**]{#struct_0_66891_x1431_1517437608}[命令用来显示]{style="font-family:宋体"}[MPLS ILM]{lang="EN-US"}[表项的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x863995589}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_x636458824}

[**[display system internal mpls lfib ilm]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x314931348}*[label]{lang="EN-US"}*

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_158817891}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mpls lfib ilm]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_2139411065}*[label]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_x283208575}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display system internal mpls lfib ilm ]{lang="EN-US"}**]{#struct_0_66891_x1431_987799401}*[label]{lang="EN-US"}*[ **chassis** ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_47588965}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x1212035568}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1734362747}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x57016713}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1770698493}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x562396223}

[*[label]{lang="EN-US"}*]{#struct_0_66891_x1431_x2065638238}[：显示指定入标签的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项详细信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_x1020733782}*[ slot-number]{lang="PT-BR"}*[：显示指定单板上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_x1211970032}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_765304150}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_799269461}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_815044335}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定单板的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1295747229}[：显示指定]{style="font-family:宋体"}[CP]{lang="EN-US"}[U]{lang="EN-US"}[的]{style="font-family:宋体"}[ILM]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-61314716 .myid}
[]{#_Toc324951715}[]{#_Toc404799923}[]{#struct_0_66891_x1431_1590334974}[]{#_Toc349205706}[]{#_Toc360181400}[]{#_Toc361312470}[]{#_Toc360181401}[]{#_Toc361312471}[]{#_Toc360181402}[]{#_Toc361312472}[]{#_Toc360181403}[]{#_Toc361312473}[]{#_Toc360181404}[]{#_Toc361312474}[]{#_Toc360181405}[]{#_Toc361312475}[]{#_Toc360181406}[]{#_Toc361312476}[]{#_Toc360181407}[]{#_Toc361312477}[]{#_Toc360181408}[]{#_Toc361312478}[]{#_Toc360181409}[]{#_Toc361312479}[]{#_Toc360181410}[]{#_Toc361312480}[]{#_Toc360181411}[]{#_Toc361312481}[]{#_Toc360181412}[]{#_Toc361312482}[]{#_Toc360181413}[]{#_Toc361312483}[]{#_Toc360181414}[]{#_Toc361312484}[]{#_Toc360181415}[]{#_Toc361312485}[]{#_Toc360181416}[]{#_Toc361312486}[]{#_Toc360181417}[]{#_Toc361312487}[]{#_Toc360181418}[]{#_Toc361312488}[]{#_Toc360181419}[]{#_Toc361312489}[]{#_Toc360181420}[]{#_Toc361312490}[]{#_Toc360181421}[]{#_Toc361312491}[]{#_Toc360181422}[]{#_Toc361312492}[]{#_Toc360181423}[]{#_Toc361312493}[]{#_Toc360181424}[]{#_Toc361312494}[]{#_Toc360181425}[]{#_Toc361312495}[]{#_Toc360181426}[]{#_Toc361312496}[]{#_Toc360181427}[]{#_Toc361312497}[]{#_Toc360181428}[]{#_Toc361312498}[]{#_Toc360181567}[]{#_Toc361312637}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib nhlfe**

------------------------------------------------------------------------

[**[display system internal mpls lfib nhlfe]{lang="EN-US"}**]{#struct_0_66891_x1431_x1211445746}[命令用来显示]{style="font-family:宋体"}[MPLS NHLFE]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1382643211}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_x413793644}

[**[display system internal mpls lfib nhlfe]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x2003602197}*[nid]{lang="EN-US"}*

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_353255522}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mpls lfib nhlfe]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x125123084}*[nid]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_x117219682}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display system internal mpls lfib nhlfe]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x1389821392}*[nid]{lang="EN-US"}*[ **chassis** ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_674815240}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x1212035569}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_168278806}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_1471664690}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1937307848}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x2072805079}

[*[nid]{lang="EN-US"}*]{#struct_0_66891_x1431_x1594545153}[：显示指定]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的详细信息。]{style="font-family:宋体"}*[nid]{lang="EN-US"}*[为]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_x1211970033}*[ slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_x766814480}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_x800779791}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_66891_x1431_x1212166641}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_66891_x1431_1928103564}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1295943837}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-809242543 .myid}
[]{#_Toc404799924}[]{#struct_0_66891_x1431_255568256}[]{#_Toc349205707}[]{#_Toc360181569}[]{#_Toc361312639}[]{#_Toc360181570}[]{#_Toc361312640}[]{#_Toc360181571}[]{#_Toc361312641}[]{#_Toc360181572}[]{#_Toc361312642}[]{#_Toc360181573}[]{#_Toc361312643}[]{#_Toc360181574}[]{#_Toc361312644}[]{#_Toc360181575}[]{#_Toc361312645}[]{#_Toc360181576}[]{#_Toc361312646}[]{#_Toc360181577}[]{#_Toc361312647}[]{#_Toc360181578}[]{#_Toc361312648}[]{#_Toc360181579}[]{#_Toc361312649}[]{#_Toc360181580}[]{#_Toc361312650}[]{#_Toc360181581}[]{#_Toc361312651}[]{#_Toc360181582}[]{#_Toc361312652}[]{#_Toc360181583}[]{#_Toc361312653}[]{#_Toc360181584}[]{#_Toc361312654}[]{#_Toc360181585}[]{#_Toc361312655}[]{#_Toc360181586}[]{#_Toc361312656}[]{#_Toc360181587}[]{#_Toc361312657}[]{#_Toc360181588}[]{#_Toc361312658}[]{#_Toc360181589}[]{#_Toc361312659}[]{#_Toc360181590}[]{#_Toc361312660}[]{#_Toc360181591}[]{#_Toc361312661}[]{#_Toc360181592}[]{#_Toc361312662}[]{#_Toc360181593}[]{#_Toc361312663}[]{#_Toc360181594}[]{#_Toc361312664}[]{#_Toc360181595}[]{#_Toc361312665}[]{#_Toc360181596}[]{#_Toc361312666}[]{#_Toc360181597}[]{#_Toc361312667}[]{#_Toc360181598}[]{#_Toc361312668}[]{#_Toc360181599}[]{#_Toc361312669}[]{#_Toc360181600}[]{#_Toc361312670}[]{#_Toc360181601}[]{#_Toc361312671}[]{#_Toc360181602}[]{#_Toc361312672}[]{#_Toc360181603}[]{#_Toc361312673}[]{#_Toc360181604}[]{#_Toc361312674}[]{#_Toc360181605}[]{#_Toc361312675}[]{#_Toc360181606}[]{#_Toc361312676}[]{#_Toc360181607}[]{#_Toc361312677}[]{#_Toc360181741}[]{#_Toc361312811}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib nhlfe reflist**

------------------------------------------------------------------------

[**[display system internal mpls lfib nhlfe reflist]{lang="EN-US"}**]{#struct_0_66891_x1431_x1739051103}[命令用来显示]{style="font-family:宋体"}[MPLS NHLFE]{lang="EN-US"}[反向关联信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_832484502}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_x1211445747}

[**[display system internal mpls lfib nhlfe]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x1346240144}*[nid ]{lang="EN-US"}***[reflist]{lang="EN-US"}**

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_2004992973}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mpls lfib nhlfe]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x382522141}*[nid]{lang="EN-US"}*[ **reflist** **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_x1199350887}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display system internal mpls lfib nhlfe]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_1988111699}*[nid]{lang="EN-US"}*[ **reflist** **chassis** ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_985263079}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x1380564370}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x1221745397}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1470955148}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_354048373}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1131923259}

[*[nid]{lang="EN-US"}*]{#struct_0_66891_x1431_x129464172}[：显示指定]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的反向关联信息。]{style="font-family:宋体"}*[nid]{lang="EN-US"}*[为]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_774385393}*[ slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的反向关联信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_1282782907}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的反向关联信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_362019623}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的反向关联信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_66891_x1431_1763347931}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的反向关联信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_66891_x1431_1475559941}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的反向关联信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1295550621}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项的反向关联信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#228487914 .myid}
[]{#_Toc404799925}[]{#struct_0_66891_x1431_x173391384}[]{#_Toc349205709}[]{#_Toc360181743}[]{#_Toc361312813}[]{#_Toc360181744}[]{#_Toc361312814}[]{#_Toc360181745}[]{#_Toc361312815}[]{#_Toc360181746}[]{#_Toc361312816}[]{#_Toc360181747}[]{#_Toc361312817}[]{#_Toc360181748}[]{#_Toc361312818}[]{#_Toc360181749}[]{#_Toc361312819}[]{#_Toc360181750}[]{#_Toc361312820}[]{#_Toc360181751}[]{#_Toc361312821}[]{#_Toc360181752}[]{#_Toc361312822}[]{#_Toc360181753}[]{#_Toc361312823}[]{#_Toc360181769}[]{#_Toc361312839}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib record**

------------------------------------------------------------------------

[**[display system internal mpls lfib record]{lang="EN-US"}**]{#struct_0_66891_x1431_x424768117}[命令用来显示]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[模块记录的信息，包括]{style="font-family:宋体"}[LFIB]{lang="EN-US"}[模块收到的信息、]{style="font-family:宋体"}[LFIB]{lang="EN-US"}[通知驱动的信息、驱动返回的信息等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_2121836116}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_353982837}

[**[display system internal mpls lfib record]{lang="EN-US"}**[ \[ **start** ]{lang="EN-US"}]{#struct_0_66891_x1431_567455747}*[start-number]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_1550740339}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mpls lfib record]{lang="EN-US"}**[ \[ **start** ]{lang="EN-US"}]{#struct_0_66891_x1431_1663116460}*[start-number]{lang="EN-US"}*[ \] **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_x812773548}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display system internal mpls lfib record]{lang="EN-US"}**[ \[ **start** ]{lang="EN-US"}]{#struct_0_66891_x1431_x801016597}*[start-number]{lang="EN-US"}*[ \] ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x1200236117}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_1723025638}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_367842833}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1808955345}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1559047538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_354310517}

[**[start]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_1802886492}*[start-number]{lang="EN-US"}*[：从指定位置开始显示记录信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_633080863}*[ slot-number]{lang="PT-BR"}*[：显示指定单板上的记录信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_x670261895}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上的记录信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_1524819037}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的记录信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_x466776774}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上指定单板的记录信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_x2003874739}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定单板的记录信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1296205980}[：显示指定单板]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的记录信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_223696203}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="ES"}[system internal]{lang="EN-US"}**]{#struct_0_66891_x1431_x2002849660}**[ ]{lang="EN-US"}[mpls lfib record]{lang="ES"}**
:::

::: {#1502509140 .myid}
[]{#_Toc404799926}[]{#struct_0_66891_x1431_41729495}[]{#_Toc349205708}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lfib statistics**

------------------------------------------------------------------------

[**[display system internal mpls ]{lang="EN-US"}**]{#struct_0_66891_x1431_x1740895445}**[lfib ]{lang="EN-US"}[statistics]{lang="EN-US"}**[命令用来显示]{style="font-family:
宋体"}[MPLS LFIB]{lang="EN-US"}[的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1043861286}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_x2019838095}

[**[display system internal ]{lang="EN-US"}**]{#struct_0_66891_x1431_354572661}**[mpls lfib statistics]{lang="EN-US"}**

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_1668972499}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mpls lfib statistics slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x10601503}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_802305926}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display system internal mpls lfib statistics]{lang="EN-US"}**[ **chassis** ]{lang="EN-US"}]{#struct_0_66891_x1431_x1377802530}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x1499518305}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x347786715}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1723618768}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x2019895185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1871138885}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_354638197}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_x1579241590}*[ slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_x1774315093}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备上的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_66891_x1431_x41264904}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_66891_x1431_51037313}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_66891_x1431_1975157731}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1295878300}[：显示指定单板]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[模块统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-102485204 .myid}
[]{#_Toc404799927}[]{#struct_0_66891_x1431_x590053837}[]{#_Toc344711486}[]{#_Toc342483946}[]{#_Toc339555212}[]{#_Toc360181772}[]{#_Toc361312842}[]{#_Toc360181773}[]{#_Toc361312843}[]{#_Toc360181774}[]{#_Toc361312844}[]{#_Toc360181775}[]{#_Toc361312845}[]{#_Toc360181776}[]{#_Toc361312846}[]{#_Toc360181777}[]{#_Toc361312847}[]{#_Toc360181778}[]{#_Toc361312848}[]{#_Toc360181779}[]{#_Toc361312849}[]{#_Toc360181780}[]{#_Toc361312850}[]{#_Toc360181781}[]{#_Toc361312851}[]{#_Toc360181782}[]{#_Toc361312852}[]{#_Toc360181783}[]{#_Toc361312853}[]{#_Toc360181784}[]{#_Toc361312854}[]{#_Toc360181785}[]{#_Toc361312855}[]{#_Toc360181786}[]{#_Toc361312856}[]{#_Toc360181787}[]{#_Toc361312857}[]{#_Toc360181788}[]{#_Toc361312858}[]{#_Toc360181789}[]{#_Toc361312859}[]{#_Toc360181790}[]{#_Toc361312860}[]{#_Toc360181791}[]{#_Toc361312861}[]{#_Toc360181792}[]{#_Toc361312862}[]{#_Toc360181793}[]{#_Toc361312863}[]{#_Toc360181794}[]{#_Toc361312864}[]{#_Toc360181795}[]{#_Toc361312865}[]{#_Toc360181796}[]{#_Toc361312866}[]{#_Toc360181797}[]{#_Toc361312867}[]{#_Toc360181798}[]{#_Toc361312868}[]{#_Toc360181799}[]{#_Toc361312869}[]{#_Toc360181800}[]{#_Toc361312870}[]{#_Toc360181801}[]{#_Toc361312871}[]{#_Toc360181802}[]{#_Toc361312872}[]{#_Toc360181803}[]{#_Toc361312873}[]{#_Toc360181804}[]{#_Toc361312874}[]{#_Toc360181805}[]{#_Toc361312875}[]{#_Toc360181806}[]{#_Toc361312876}[]{#_Toc360181807}[]{#_Toc361312877}[]{#_Toc360181808}[]{#_Toc361312878}[]{#_Toc360181809}[]{#_Toc361312879}[]{#_Toc360181810}[]{#_Toc361312880}[]{#_Toc360181811}[]{#_Toc361312881}[]{#_Toc360181812}[]{#_Toc361312882}[]{#_Toc360181813}[]{#_Toc361312883}[]{#_Toc360181814}[]{#_Toc361312884}[]{#_Toc360181815}[]{#_Toc361312885}[]{#_Toc360181816}[]{#_Toc361312886}[]{#_Toc360181817}[]{#_Toc361312887}[]{#_Toc360181818}[]{#_Toc361312888}[]{#_Toc360181819}[]{#_Toc361312889}[]{#_Toc360181820}[]{#_Toc361312890}[]{#_Toc360181821}[]{#_Toc361312891}[]{#_Toc360181822}[]{#_Toc361312892}[]{#_Toc360181823}[]{#_Toc361312893}[]{#_Toc360181824}[]{#_Toc361312894}[]{#_Toc360181825}[]{#_Toc361312895}[]{#_Toc360181826}[]{#_Toc361312896}[]{#_Toc360181827}[]{#_Toc361312897}[]{#_Toc360181828}[]{#_Toc361312898}[]{#_Toc360181829}[]{#_Toc361312899}[]{#_Toc360181830}[]{#_Toc361312900}[]{#_Toc360181831}[]{#_Toc361312901}[]{#_Toc360181832}[]{#_Toc361312902}[]{#_Toc360181833}[]{#_Toc361312903}[]{#_Toc360181834}[]{#_Toc361312904}[]{#_Toc360181835}[]{#_Toc361312905}[]{#_Toc360181836}[]{#_Toc361312906}[]{#_Toc360181837}[]{#_Toc361312907}[]{#_Toc360181838}[]{#_Toc361312908}[]{#_Toc360181839}[]{#_Toc361312909}[]{#_Toc360181840}[]{#_Toc361312910}[]{#_Toc360181841}[]{#_Toc361312911}[]{#_Toc360181842}[]{#_Toc361312912}[]{#_Toc360181843}[]{#_Toc361312913}[]{#_Toc360181844}[]{#_Toc361312914}[]{#_Toc360181845}[]{#_Toc361312915}[]{#_Toc360181846}[]{#_Toc361312916}[]{#_Toc360181847}[]{#_Toc361312917}[]{#_Toc360181848}[]{#_Toc361312918}[]{#_Toc360181849}[]{#_Toc361312919}[]{#_Toc360181850}[]{#_Toc361312920}[]{#_Toc360181851}[]{#_Toc361312921}[]{#_Toc360181852}[]{#_Toc361312922}[]{#_Toc360181853}[]{#_Toc361312923}[]{#_Toc360181854}[]{#_Toc361312924}[]{#_Toc360181855}[]{#_Toc361312925}[]{#_Toc360181856}[]{#_Toc361312926}[]{#_Toc360181857}[]{#_Toc361312927}[]{#_Toc360181858}[]{#_Toc361312928}[]{#_Toc360181859}[]{#_Toc361312929}[]{#_Toc360181860}[]{#_Toc361312930}[]{#_Toc360181861}[]{#_Toc361312931}[]{#_Toc360181862}[]{#_Toc361312932}[]{#_Toc360181863}[]{#_Toc361312933}[]{#_Toc360181864}[]{#_Toc361312934}[]{#_Toc360181865}[]{#_Toc361312935}[]{#_Toc360181866}[]{#_Toc361312936}[]{#_Toc360181867}[]{#_Toc361312937}[]{#_Toc360181868}[]{#_Toc361312938}[]{#_Toc360181869}[]{#_Toc361312939}[]{#_Toc360181870}[]{#_Toc361312940}[]{#_Toc360181871}[]{#_Toc361312941}[]{#_Toc360182286}[]{#_Toc361313356}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls lsp-pending**

------------------------------------------------------------------------

[**[display system internal mpls lsp-pending]{lang="EN-US"}**]{#struct_0_66891_x1431_1694025586}[命令用来显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[、]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[协议]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程中，尚未下发到转发平面的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1829090933}

[**[display system internal mpls lsp-pending]{lang="EN-US"}**]{#struct_0_66891_x1431_1067660257}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x200584315}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x718355536}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x1615646679}

[[network-admin]{lang="FR"}]{#struct_0_66891_x1431_x1549807343}

[[mdc-admin]{lang="FR"}]{#struct_0_66891_x1431_x452586218}
:::

::: {#1766020638 .myid}
[]{#_Toc404799928}[]{#struct_0_66891_x1431_880396284}[]{#_Toc344711488}[]{#_Toc360182288}[]{#_Toc361313358}[]{#_Toc360182289}[]{#_Toc361313359}[]{#_Toc360182290}[]{#_Toc361313360}[]{#_Toc360182291}[]{#_Toc361313361}[]{#_Toc360182292}[]{#_Toc361313362}[]{#_Toc360182293}[]{#_Toc361313363}[]{#_Toc360182294}[]{#_Toc361313364}[]{#_Toc360182295}[]{#_Toc361313365}[]{#_Toc360182296}[]{#_Toc361313366}[]{#_Toc360182297}[]{#_Toc361313367}[]{#_Toc360182298}[]{#_Toc361313368}[]{#_Toc360182299}[]{#_Toc361313369}[]{#_Toc360182300}[]{#_Toc361313370}[]{#_Toc360182329}[]{#_Toc361313399}

**MPLS基础 \-- MPLS基础Probe命令 \-- display system internal mpls statistics**

------------------------------------------------------------------------

[**[display system internal mpls statistics]{lang="EN-US"}**]{#struct_0_66891_x1431_x451996394}[命令用来显示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[的内部状态统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x476432555}

[**[display system internal mpls statistics]{lang="EN-US"}**]{#struct_0_66891_x1431_393997240}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x952896344}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x510105}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x648392274}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1699534897}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1268792628}
:::

::: {#-1699610735 .myid}
[]{#_Toc404799929}[]{#struct_0_66891_x1431_1491391948}[]{#_Toc349205710}[]{#_Toc360182331}[]{#_Toc361313401}[]{#_Toc360182332}[]{#_Toc361313402}[]{#_Toc360182333}[]{#_Toc361313403}[]{#_Toc360182334}[]{#_Toc361313404}[]{#_Toc360182335}[]{#_Toc361313405}[]{#_Toc360182336}[]{#_Toc361313406}[]{#_Toc360182337}[]{#_Toc361313407}[]{#_Toc360182338}[]{#_Toc361313408}[]{#_Toc360182339}[]{#_Toc361313409}[]{#_Toc360182340}[]{#_Toc361313410}[]{#_Toc360182341}[]{#_Toc361313411}[]{#_Toc360182342}[]{#_Toc361313412}[]{#_Toc360182343}[]{#_Toc361313413}[]{#_Toc360182344}[]{#_Toc361313414}[]{#_Toc360182345}[]{#_Toc361313415}[]{#_Toc360182346}[]{#_Toc361313416}[]{#_Toc360182347}[]{#_Toc361313417}[]{#_Toc360182348}[]{#_Toc361313418}[]{#_Toc360182349}[]{#_Toc361313419}[]{#_Toc360182350}[]{#_Toc361313420}[]{#_Toc360182351}[]{#_Toc361313421}[]{#_Toc360182352}[]{#_Toc361313422}[]{#_Toc360182353}[]{#_Toc361313423}[]{#_Toc360182354}[]{#_Toc361313424}[]{#_Toc360182355}[]{#_Toc361313425}[]{#_Toc360182356}[]{#_Toc361313426}[]{#_Toc360182357}[]{#_Toc361313427}[]{#_Toc360182358}[]{#_Toc361313428}[]{#_Toc360182359}[]{#_Toc361313429}[]{#_Toc360182360}[]{#_Toc361313430}[]{#_Toc360182361}[]{#_Toc361313431}[]{#_Toc360182362}[]{#_Toc361313432}[]{#_Toc360182363}[]{#_Toc361313433}[]{#_Toc360182364}[]{#_Toc361313434}[]{#_Toc360182365}[]{#_Toc361313435}[]{#_Toc360182366}[]{#_Toc361313436}[]{#_Toc360182367}[]{#_Toc361313437}[]{#_Toc360182368}[]{#_Toc361313438}[]{#_Toc360182369}[]{#_Toc361313439}[]{#_Toc360182494}[]{#_Toc361313564}

**MPLS基础 \-- MPLS基础Probe命令 \-- mpls lfib record size**

------------------------------------------------------------------------

[**[mpls lfib record size]{lang="EN-US"}**]{#struct_0_66891_x1431_1490543665}[命令用来设置]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[模块记录信息的最大数目。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x2002585037}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_x649035784}

[**[mpls lfib record size]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x1668042096}*[size]{lang="EN-US"}*

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_x751708798}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[mpls lfib record size]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x2024368246}*[size]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_1926620378}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[mpls lfib record size ]{lang="EN-US"}**]{#struct_0_66891_x1431_x1307888745}*[size]{lang="EN-US"}*[ **chassis** ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x362612987}

[[MPLS LFIB]{lang="EN-US"}]{#struct_0_66891_x1431_488114884}[模块记录信息的最大数目为]{style="font-family:宋体"}[4096]{lang="EN-US"}[条。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1397144882}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_x178640142}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x861928763}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_1100512459}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_1605319182}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1090207095}

[*[size]{lang="EN-US"}*]{#struct_0_66891_x1431_1926554842}[：指定记录信息的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_696869069}*[ slot-number]{lang="PT-BR"}*[：指定单板上的记录信息的最大数目。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_x834063078}*[ slot-number]{lang="PT-BR"}*[：指定成员设备上的记录信息的最大数目。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_x1963513669}*[ slot-number]{lang="PT-BR"}*[：指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的记录信息的最大数目。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_x70298041}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：指定成员设备上指定单板的记录信息的最大数目。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_765369686}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：指定单板的记录信息的最大数目。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1296074907}[：指定单板]{style="font-family:宋体"}[CPU]{lang="EN-US"}[记录信息的最大数目。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#914716930 .myid}
[]{#_Toc404799930}[]{#struct_0_66891_x1431_1926489306}[]{#_Toc349205711}[]{#_Toc360182496}[]{#_Toc361313566}[]{#_Toc360182497}[]{#_Toc361313567}[]{#_Toc360182498}[]{#_Toc361313568}[]{#_Toc360182499}[]{#_Toc361313569}[]{#_Toc360182500}[]{#_Toc361313570}

**MPLS基础 \-- MPLS基础Probe命令 \-- reset system internal mpls lfib record**

------------------------------------------------------------------------

[**[reset system internal mpls lfib record]{lang="EN-US"}**]{#struct_0_66891_x1431_1789807823}[命令用来清除]{style="font-family:宋体"}[MPLS LFIB]{lang="EN-US"}[模块记录的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_387503164}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_66891_x1431_145668070}

[**[reset system internal mpls lfib record]{lang="EN-US"}**]{#struct_0_66891_x1431_1926423770}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_66891_x1431_x947023574}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal mpls lfib record slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_x770270260}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_66891_x1431_x1126039082}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[reset system internal mpls lfib record chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_66891_x1431_1926358234}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_66891_x1431_995023070}

[[Probe]{lang="EN-US"}]{#struct_0_66891_x1431_1676493531}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_66891_x1431_1806739744}

[[network-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x1263518464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_66891_x1431_x138141010}

[[【参数】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x1069716106}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_1494582957}*[ slot-number]{lang="PT-BR"}*[：清除指定单板上的记录信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_1926292698}*[ slot-number]{lang="PT-BR"}*[：清除指定成员设备上的记录信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_66891_x1431_x800714255}*[ slot-number]{lang="PT-BR"}*[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的记录信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_x1705108145}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：清除指定成员设备上指定单板的记录信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_66891_x1431_1928169100}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：清除指定单板的记录信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_66891_x1431_1295485083}[：清除指定单板]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[记录信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_66891_x1431_x2037852594}

[[·[              ]{style="font:7.0pt "}]{lang="ES" style="font-size:10.0pt;font-family:Symbol"}**[display system internal mpls lfib record]{lang="EN-US"}**]{#struct_0_66891_x1431_460898246}
:::
