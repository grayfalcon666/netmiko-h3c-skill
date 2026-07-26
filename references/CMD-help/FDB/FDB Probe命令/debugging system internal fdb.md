::: {#-774497720 .myid}
[]{#_Toc289415221}[]{#_Toc138239296}[]{#_Toc136679734}[]{#_Toc291055660}[]{#_Toc271702012}[]{#_Toc238271212}[]{#_Toc404798875}[]{#struct_0_x1212_x9592_x141408643}[]{#_Toc376165149}

**FDB \-- FDB Probe命令 \-- debugging system internal fdb**

------------------------------------------------------------------------

[**[debugging system internal fdb ]{lang="EN-US"}**]{#struct_0_x1212_x9592_x562055638}[命令用来打开流表调试开关。]{style="font-family:
宋体"}

[**[undo debugging system internal fdb]{lang="EN-US"}**]{#struct_0_x1212_x9592_x1240963223}[命令用来关闭流表调试开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_x1787555572}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1212_x9592_x1864070251}

[**[debugging system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** \[ **verbose** \] \[ **acl** *acl-number* \] }]{lang="EN-US"}]{#struct_0_x1212_x9592_x1673757938}

[**[undo debugging system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** \[ **verbose** \] \[ **acl** *acl-number* \] }]{lang="EN-US"}]{#struct_0_x1212_x9592_x1282892009}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1212_x9592_1384554829}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging system internal]{lang="EN-US"}**[ { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** \[ **verbose** \] \[ **acl** *acl-number* \] } **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1212_x9592_x1305196231}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** \[ **verbose** \] \[ **acl** *acl-number* \] } **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1212_x9592_x1096835131}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1212_x9592_800731700}[模式：]{style="font-family:宋体"}

[**[debugging]{lang="EN-US"}**[ **system** **internal** { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** \[ **verbose** \] \[ **acl** *acl-number* \] } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1212_x9592_637639589}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** { **ipv4** \| **ipv6** } **fdb** { **all** \| **drv** \| **entry** \[ **verbose** \] \[ **acl** *acl-number* \] } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1212_x9592_x1592888137}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_x995091520}

[[流表调试开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1212_x9592_634433704}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_x298576131}

[[Probe]{lang="EN-US"}]{#struct_0_x1212_x9592_x523366597}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_1299847127}

[[network-admin]{lang="EN-US"}]{#struct_0_x1212_x9592_1441844290}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1212_x9592_1748791401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_1628420111}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x1212_x9592_x1806617764}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的流表调试信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x1212_x9592_1927621709}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的流表调试信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1212_x9592_293382201}[：表示所有的调试信息开关。]{style="font-family:宋体"}

[**[drv]{lang="EN-US"}**]{#struct_0_x1212_x9592_x1311051575}[：表示下驱动的调试信息开关。]{style="font-family:宋体"}

[**[entry]{lang="EN-US"}**]{#struct_0_x1212_x9592_x298510595}[：表示流表的调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1212_x9592_1848714767}[：表示显示详细信息的流表调试信息开关。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_x1212_x9592_x340889329}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，]{style="font-family:宋体"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[，高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_x732878009}[：显示指定单板上的流表调试信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_444368878}[：显示指定成员设备上的流表调试信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_x624613189}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的流表调试信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_x1964321687}[：显示指定成员设备上指定单板的流表调试信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_1213489010}[：显示指定单板的流表调试信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_x1212_x9592_2088316080}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的流表调试信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#340570820 .myid}
[]{#_Toc404798876}[]{#struct_0_x1212_x9592_275993484}[]{#_Toc376165151}

**FDB \-- FDB Probe命令 \-- display system internal fdb**

------------------------------------------------------------------------

[**[display system internal fdb]{lang="EN-US"}**]{#struct_0_x1212_x9592_935412950}[命令用来显示流表的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_1100116791}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1212_x9592_x298445059}

[**[display system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb statistics**]{lang="EN-US"}]{#struct_0_x1212_x9592_x135035911}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1212_x9592_1251318439}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb statistics slot** *slot-number* \[ **[cpu]{style="color:black"}**[ *cpu-number* ]{style="color:black"}\]]{lang="EN-US"}]{#struct_0_x1212_x9592_424200719}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1212_x9592_590931925}[模式：]{style="font-family:宋体"}

[**[display system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb statistics chassis** *chassis-number* **slot** *slot-number* \[ **[cpu]{style="color:black"}**[ *cpu-number* ]{style="color:black"}\]]{lang="EN-US"}]{#struct_0_x1212_x9592_1099115649}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_415086179}

[[Probe]{lang="EN-US"}]{#struct_0_x1212_x9592_x1560634876}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_x651820358}

[[network-admin]{lang="EN-US"}]{#struct_0_x1212_x9592_x1401818359}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1212_x9592_x298379523}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_x1240855469}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x1212_x9592_762696867}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的流表统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x1212_x9592_1060421659}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的流表统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_184535006}[：]{style="font-family:宋体"}[显示指定单板上流表的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_701580279}[：]{style="font-family:宋体"}[显示指定成员设备上流表的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_538186225}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上流表的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_x279510168}[：]{style="font-family:宋体"}[显示指定成员设备指定单板上流表的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_1660976075}[：]{style="font-family:宋体"}[显示指定单板上流表的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US" style="font-size:11.0pt;color:black"}**]{#struct_0_x1212_x9592_x386989470}[ *cpu-number*]{lang="EN-US" style="font-size:11.0pt;color:black"}[：]{style="font-size:11.0pt;font-family:宋体;color:black"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上流表的统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US" style="font-size:
11.0pt;color:black"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#2106920767 .myid}
[]{#_Toc404798877}[]{#struct_0_x1212_x9592_1284642061}[]{#_Toc376165153}

**FDB \-- FDB Probe命令 \-- reset system internal fdb**

------------------------------------------------------------------------

[**[reset system internal fdb]{lang="EN-US"}**]{#struct_0_x1212_x9592_1230081524}[命令用来清除流表的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_x298838275}

[[集中式设备：]{style="font-family:宋体"} ]{#struct_0_x1212_x9592_x460029490}

[**[reset system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb statistics**]{lang="EN-US"}]{#struct_0_x1212_x9592_x74256358}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1212_x9592_1643617435}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb statistics** \[ **slot** *slot-number* \[ **[cpu]{style="color:black"}**[ *cpu-number* ]{style="color:black"}\][ ]{style="color:black"}\]]{lang="EN-US"}]{#struct_0_x1212_x9592_x483591029}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1212_x9592_1190246756}[模式：]{style="font-family:宋体"}

[**[reset system internal ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } **fdb statistics** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **[cpu]{style="color:black"}**[ *cpu-number* ]{style="color:black"}\] \] ]{lang="EN-US"}]{#struct_0_x1212_x9592_1153385000}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_259055149}

[[Probe]{lang="EN-US"}]{#struct_0_x1212_x9592_x672737364}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_x1060812374}

[[network-admin]{lang="EN-US"}]{#struct_0_x1212_x9592_x1108447590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1212_x9592_x298772739}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1212_x9592_298466581}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x1212_x9592_2058990139}[：表示清除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的流表统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x1212_x9592_x379775164}[：表示清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的流表统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_x999268239}[：]{style="font-family:宋体"}[清除指定单板上流表的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则清除所有单板上的流表的统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_1511227560}[：]{style="font-family:宋体"}[清除指定成员设备上流表的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除所有成员设备上的上流表的统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_1700985639}[：]{style="font-family:宋体"}[清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上流表的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上流表的统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_677149187}[：]{style="font-family:宋体"}[清除指定成员设备的指定单板上流表的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则清除所有单板上流表的统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1212_x9592_x1554093622}[：]{style="font-family:宋体"}[清除指定单板上流表的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则清除所有单板上流表的统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US" style="font-size:11.0pt;color:black"}**]{#struct_0_x1212_x9592_106275323}[ *cpu-number*]{lang="EN-US" style="font-size:11.0pt;color:black"}[：]{style="font-size:11.0pt;font-family:宋体;color:black"}[清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上流表的统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US" style="font-size:
11.0pt;color:black"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
