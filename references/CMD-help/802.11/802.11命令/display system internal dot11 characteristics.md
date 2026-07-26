::::: {#306058854 .myid}
[]{#_Toc404798600}[]{#struct_0_19094_x3111_x473885871}[]{#_Toc375660933}

**802.11 \-- 802.11命令 \-- display system internal dot11 characteristics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](802.11%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_19094_x3111_x1278451503}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_19094_x3111_1484237}
:::

[ ]{lang="EN-US"}

[]{#_Toc375660934}[**[display system internal dot11 characteristics]{lang="EN-US"}**]{#struct_0_19094_x3111_1143719304}[命令用来显示]{style="font-family:宋体"}[802.11]{lang="EN-US"}[侦听特征的统计信息和详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19094_x3111_89939176}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_19094_x3111_x1507869093}

[**[display system internal dot11 characteristics ]{lang="EN-US"}**[{ **bss** *bssid* \| **interface wlan-radio** *interface-number* }]{lang="EN-US"}]{#struct_0_19094_x3111_x389287252}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19094_x3111_x491412972}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal dot11 characteristics ]{lang="EN-US"}**[{ **bss** *bssid* \| **interface wlan-radio ** *interface-number* } **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_19094_x3111_x1221444364}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_19094_x3111_x1739169979}[模式：]{style="font-family:宋体"}

[**[display system internal dot11 characteristics ]{lang="EN-US"}**[{ **bss** *bssid* \| **interface wlan-radio** *interface-number* } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_19094_x3111_1285871411}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19094_x3111_x1917064444}

[[Probe]{lang="EN-US"}]{#struct_0_19094_x3111_x673549065}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19094_x3111_1753802994}

[[network-admin]{lang="EN-US"}]{#struct_0_19094_x3111_x128435493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19094_x3111_238478}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19094_x3111_1889494231}

[**[bss ]{lang="EN-US"}***[bssid]{lang="EN-US"}*]{#struct_0_19094_x3111_x1168619173}[：显示]{style="font-family:宋体"}[BSS]{lang="EN-US"}[实体的特征统计信息和详细信息，包括]{style="font-family:宋体"}[BSS]{lang="EN-US"}[接收报文方向和发送报文方向。]{style="font-family:宋体"}

[**[wlan-radio ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_19094_x3111_69912182}[：显示指定射频接口的特征统计信息和详细信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_19094_x3111_x565796047}[：显示指定单板的特征统计信息和详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_19094_x3111_x1396450036}[：显示指定成员设备的特征统计信息和详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_19094_x3111_x624547653}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的特征统计信息和详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19094_x3111_x1507221963}[：显示指定成员设备上指定单板的特征统计信息和详细信息，]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19094_x3111_1236700320}[：显示指定单板的特征统计信息和详细信息，]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_19094_x3111_x2004151647}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::::: {#1427643256 .myid}
[]{#_Toc404798601}[]{#struct_0_19094_x3111_x337017103}

**802.11 \-- 802.11命令 \-- display system internal dot11 verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](802.11%20Probe命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_19094_x3111_x230915106}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_19094_x3111_1910676465}
:::

[ ]{lang="EN-US"}

[**[display system internal dot11 verbose]{lang="EN-US"}**]{#struct_0_19094_x3111_1441787411}[命令用来显示]{style="font-family:宋体"}[802.11]{lang="EN-US"}[协议]{style="font-family:宋体"}[socket]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19094_x3111_2135555183}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_19094_x3111_x1527135826}

[**[display system internal dot11 verbose]{lang="EN-US"}**]{#struct_0_19094_x3111_x1326311438}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19094_x3111_x1863747129}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal dot11]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \] **verbose**]{lang="EN-US"}]{#struct_0_19094_x3111_1605580661}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_19094_x3111_1469260612}[模式：]{style="font-family:宋体"}

[**[display system internal dot11 chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] **verbose**]{lang="EN-US"}]{#struct_0_19094_x3111_129651725}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19094_x3111_x1506358110}

[[Probe]{lang="EN-US"}]{#struct_0_19094_x3111_x1423785036}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19094_x3111_1141928248}

[[network-admin]{lang="EN-US"}]{#struct_0_19094_x3111_206497675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19094_x3111_1043595679}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19094_x3111_708568413}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_19094_x3111_x1000132813}[：显示指定单板的]{style="font-family:宋体"}[socket]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_19094_x3111_x1826874819}[：显示指定成员设备的]{style="font-family:宋体"}[socket]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_19094_x3111_538251761}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19094_x3111_1435735241}[：显示指定成员设备上的指定单板的]{style="font-family:
宋体"}[socket]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19094_x3111_1133102245}[：显示指定单板的]{style="font-family:
宋体"}[socket]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_19094_x3111_1126813111}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::
