::: {#-122466931 .myid}
[]{#_Toc404800235}[]{#struct_0_x1028_x7036_1851749906}

**sFlow \-- sFlow Probe命令 \-- display system internal sflow statistics**

------------------------------------------------------------------------

[**[display system internal sflow statistics]{lang="EN-US"}**]{#struct_0_x1028_x7036_x479308563}[命令用来显示]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_x1648272052}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1028_x7036_1773120832}

[**[display system internal sflow statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1028_x7036_x1208470296}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1028_x7036_x1613229838}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal sflow statistics ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1028_x7036_x1887947398}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1028_x7036_298929861}[模式：]{style="font-family:宋体"}

[**[display system internal sflow statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1028_x7036_x535378472}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_x1867086046}

[[probe]{lang="EN-US"}]{#struct_0_x1028_x7036_x42944700}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_x1651209027}

[[network-admin]{lang="EN-US"}]{#struct_0_x1028_x7036_x755840462}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1028_x7036_1631580938}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_1234834552}

[**[slot]{lang="SV"}**[ ]{lang="SV"}]{#struct_0_x1028_x7036_1649164714}*[slot-number]{lang="SV"}*[：查看指定单板上的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**[ ]{lang="SV"}]{#struct_0_x1028_x7036_x91262647}*[slot-number]{lang="SV"}*[：查看指定成员设备的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1028_x7036_1165425447}[：]{style="font-family:宋体"}[查看指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数时，将显示所有设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**[ ]{lang="SV"}]{#struct_0_x1028_x7036_1717550102}*[chassis-number]{lang="SV"}*[ ]{lang="SV"}**[slot]{lang="SV"}**[ ]{lang="SV"}*[slot-number]{lang="SV"}*[：查看指定成员设备上指定单板的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1028_x7036_1245813323}[：查看指定单板的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="SV"}**]{#struct_0_x1028_x7036_488615174}*[cpu-number]{lang="SV"}*[：显示指定]{style="font-family:
宋体"}[CPU]{lang="SV"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="SV"}*[表示]{style="font-family:宋体"}[CPU]{lang="SV"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-214182187 .myid}
[]{#_Toc404800236}[]{#struct_0_x1028_x7036_1634951155}[]{#_Toc294194630}[]{#_Toc362270422}[]{#_Toc362270423}[]{#_Toc362270424}[]{#_Toc362270425}[]{#_Toc362270426}[]{#_Toc362270427}[]{#_Toc362270428}[]{#_Toc362270429}[]{#_Toc362270430}[]{#_Toc362270431}[]{#_Toc362270432}[]{#_Toc362270433}[]{#_Toc362270434}[]{#_Toc362270435}[]{#_Toc362270436}[]{#_Toc362270437}[]{#_Toc362270438}[]{#_Toc362270439}[]{#_Toc362270479}

**sFlow \-- sFlow Probe命令 \-- reset system internal sflow statistics**

------------------------------------------------------------------------

[**[reset system internal sflow statistics]{lang="EN-US"}**]{#struct_0_x1028_x7036_200253275}[命令用来清除]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_510537305}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1028_x7036_2120785523}

[**[reset  system internal sflow statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1028_x7036_x42682555}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1028_x7036_x1105746938}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal sflow statistics ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1028_x7036_x428334548}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1028_x7036_x469291377}[模式：]{style="font-family:宋体"}

[**[reset system internal sflow statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1028_x7036_1261212982}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_836451644}

[[probe]{lang="EN-US"}]{#struct_0_x1028_x7036_x1256576850}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_94519539}

[[network-admin]{lang="EN-US"}]{#struct_0_x1028_x7036_1397340276}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1028_x7036_x121218865}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1028_x7036_x42748091}

[**[slot]{lang="SV"}**[ ]{lang="SV"}]{#struct_0_x1028_x7036_x355663529}*[slot-number]{lang="SV"}*[：清除指定单板上的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**[ ]{lang="SV"}]{#struct_0_x1028_x7036_x5925640}*[slot-number]{lang="SV"}*[：清除指定成员设备的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1028_x7036_x400658494}[：]{style="font-family:宋体"}[清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数时，将显示所有设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**[ ]{lang="SV"}]{#struct_0_x1028_x7036_1194072533}*[chassis-number]{lang="SV"}*[ ]{lang="SV"}**[slot]{lang="SV"}**[ ]{lang="SV"}*[slot-number]{lang="SV"}*[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1028_x7036_x1966742435}[：清除指定单板的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有设备上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="SV"}**]{#struct_0_x1028_x7036_x1467699970}*[cpu-number]{lang="SV"}*[：清除指定]{style="font-family:
宋体"}[CPU]{lang="SV"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="SV"}*[表示]{style="font-family:宋体"}[CPU]{lang="SV"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
