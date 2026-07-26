::: {#-293878903 .myid}
[]{#_Toc404798859}[]{#struct_0_x1452_x6104_x596062759}[]{#_Toc373742289}

**FCoE \-- FCoE Probe命令 \-- display system internal fc fib**

------------------------------------------------------------------------

[**[display system internal fc fib]{lang="EN-US"}**]{#struct_0_x1452_x6104_1661221895}[命令用来显示]{style="font-family:
宋体"}[FC FIB]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_166906017}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1452_x6104_x1964026926}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal fc fib ]{lang="EN-US"}**[\[ *fcid* \[ *mask-length* \] \] **vsan** *vsan-id* \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_x144793268}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1452_x6104_376282324}[模式：]{style="font-family:宋体"}

[**[display system internal fc fib ]{lang="EN-US"}**[\[ *fcid* \[ *mask-length* \] \] **vsan** *vsan-id* \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_x1791055954}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_1689927435}

[[Probe]{lang="EN-US"}]{#struct_0_x1452_x6104_x1692937188}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x1007983637}

[[network-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_x996704069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_x1862010702}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_1326251542}

[*[fcid]{lang="EN-US"}*]{#struct_0_x1452_x6104_1162455233}[：显示指定目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[FC FIB]{lang="EN-US"}[表项信息，取值范围为]{style="font-family:宋体"}[0x000000]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFFFF]{lang="EN-US"}[（十六进制）。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1452_x6104_x207513008}[：目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1452_x6104_x1832289112}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FC FIB]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_1839515126}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_65129839}[：显示指定成员设备上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x1293997893}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_1820890809}[：显示指定成员设备指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_1434885462}[：显示指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}
:::

::: {#1601234182 .myid}
[]{#_Toc404798860}[]{#struct_0_x1452_x6104_x1643771410}[]{#_Toc354747759}

**FCoE \-- FCoE Probe命令 \-- display system internal fcoe vfcinfo**

------------------------------------------------------------------------

[**[display system internal fcoe vfcinfo]{lang="EN-US"}**]{#struct_0_x1452_x6104_x1775594091}[命令用来显示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口相关的内部信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x128279724}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1452_x6104_334699047}

[**[display system internal fcoe vfcinfo interface vfc]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_82786868}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1452_x6104_1628430771}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal fcoe vfcinfo interface vfc]{lang="EN-US"}***[ interface-number ]{lang="EN-US"}*[\[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_1339437914}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1452_x6104_1892136645}[模式：]{style="font-family:宋体"}

[**[display system internal fcoe vfcinfo interface vfc]{lang="EN-US"}***[ interface-number ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_563823048}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x2042407826}

[[Probe]{lang="EN-US"}]{#struct_0_x1452_x6104_x1393314637}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x319970287}

[[network-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_x1322921206}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_x56971668}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x896475888}

[**[interface]{lang="EN-US"}**[ **vfc** *interface-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_x1621130242}[：显示指定]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的内部信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x1057087573}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x1583489397}[：显示指定成员设备上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。]{style="font-family:宋体"}[(]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[)]{lang="EN-US"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x1697282420}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_x1222108155}[：显示指定成员设备指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。]{style="font-family:宋体"}[(]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[)]{lang="EN-US"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_1704299260}[：显示指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}
:::

::: {#-830676692 .myid}
[]{#_Toc404798861}[]{#struct_0_x1452_x6104_x555522657}[]{#_Toc354747760}

**FCoE \-- FCoE Probe命令 \-- display system internal fcoe vsaninfo**

------------------------------------------------------------------------

[**[display system internal fcoe vsaninfo]{lang="EN-US"}**]{#struct_0_x1452_x6104_1007159606}[命令用来显示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[相关的内部信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x1325253314}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1452_x6104_409110281}

[**[display system internal fcoe vsaninfo interface vfc]{lang="EN-US"}***[ interface-number ]{lang="EN-US"}***[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x1452_x6104_1401444882}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1452_x6104_757855706}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal fcoe vsaninfo interface vfc]{lang="EN-US"}***[ interface-number ]{lang="EN-US"}***[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x1452_x6104_x2041818002}

[*[ ]{lang="EN-US"}*[\[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_x1515592811}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1452_x6104_68950821}[模式：]{style="font-family:宋体"}

[**[display system internal fcoe vsaninfo interface vfc]{lang="EN-US"}***[ interface-number ]{lang="EN-US"}***[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x1452_x6104_744120021}

[*[ ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_x232379891}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_987894392}

[[Probe]{lang="EN-US"}]{#struct_0_x1452_x6104_x190134127}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x824707060}

[[network-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_1769311454}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_2113128588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_386571555}

[**[interface vfc]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x386559367}[：显示指定]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口下]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[相关的内部信息。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1452_x6104_x1034349424}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的内部信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x1362915089}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x1476257691}[：显示指定成员设备上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x2100566947}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_x1072248046}[：显示指定成员设备指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_628316408}[：显示指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}
:::

::: {#-1479237888 .myid}
[]{#_Toc404798862}[]{#struct_0_x1452_x6104_x2041752466}[]{#_Toc354747763}

**FCoE \-- FCoE Probe命令 \-- display system internal zone acl**

------------------------------------------------------------------------

[**[display system internal zone acl]{lang="EN-US"}**]{#struct_0_x1452_x6104_x546646551}[命令用来显示已经下发的]{style="font-family:宋体"}[FC Zone ACL]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x1178380814}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1452_x6104_x185169471}

[**[display system internal zone acl vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x1452_x6104_1956647973}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1452_x6104_163247243}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal zone acl vsan ]{lang="EN-US"}***[vsan-id ]{lang="EN-US"}*[\[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_725876175}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1452_x6104_x92170712}[模式：]{style="font-family:宋体"}

[**[display system internal zone acl vsan ]{lang="EN-US"}***[vsan-id ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1452_x6104_x527528734}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_1434428945}

[[Probe]{lang="EN-US"}]{#struct_0_x1452_x6104_1887156587}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x2145755007}

[[network-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_x1524159289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1452_x6104_606663602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1452_x6104_x1400966975}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1452_x6104_x610866943}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内已经下发的]{style="font-family:宋体"}[FC Zone ACL]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_x2042342291}[：显示指定单板上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_1450723648}[：显示指定成员设备上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1452_x6104_1078655102}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_x839137565}[：显示指定成员设备指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1452_x6104_x1057189226}[：显示指定单板上的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
