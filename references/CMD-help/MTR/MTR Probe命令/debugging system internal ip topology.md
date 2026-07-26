::: {#-704140718 .myid}
[]{#_Toc404799943}[]{#struct_0_69394_x5788_x599802567}

**MTR \-- MTR Probe命令 \-- debugging system internal ip topology**

------------------------------------------------------------------------

[**[debugging system internal ip topology]{lang="EN-US"}**]{#struct_0_69394_x5788_736443760}[命令用来打开拓扑调试信息的开关。]{style="font-family:宋体"}

[**[undo debugging system internal ip topology]{lang="EN-US"}**]{#struct_0_69394_x5788_1085630879}[命令用来关闭拓扑调试信息的开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69394_x5788_171712198}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69394_x5788_x1837789086}

[**[debugging system internal ip topology]{lang="EN-US"}**]{#struct_0_69394_x5788_x500632496}

[**[undo debugging system internal ip topology]{lang="EN-US"}**]{#struct_0_69394_x5788_1324353654}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69394_x5788_x663121455}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging system internal ip topology]{lang="EN-US"}**[ \[ **s**]{lang="EN-US"}]{#struct_0_69394_x5788_x1566272170}**[lot]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ *slot-number* ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ **cpu** *cpu-number* \] ]{lang="EN-US"}[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[**[undo debugging system internal ip topology]{lang="EN-US"}**[ \[ **s**]{lang="EN-US"}]{#struct_0_69394_x5788_995305561}**[lot]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[ *slot-number* ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ **cpu** *cpu-number* \] ]{lang="EN-US"}[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69394_x5788_1146485649}[模式：]{style="font-family:宋体"}

[**[debugging system internal ip topology]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_69394_x5788_1017046397}**[chassis]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ *chassis-number* **slot** *slot-number* ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ **cpu** *cpu-number* \] ]{lang="EN-US"}[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[**[undo debugging system internal ip topology]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_69394_x5788_778563154}**[chassis]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[ *chassis-number* **slot** *slot-number* ]{lang="EN-US" style="font-size:10.0pt;
color:black"}[\[ **cpu** *cpu-number* \] ]{lang="EN-US"}[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_69394_x5788_x459353764}

[[拓扑的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_69394_x5788_x217541539}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69394_x5788_657677794}

[[Probe]{lang="EN-US"}]{#struct_0_69394_x5788_171646662}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69394_x5788_x1077416488}

[[network-admin]{lang="EN-US"}]{#struct_0_69394_x5788_x1539053856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69394_x5788_1390598826}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69394_x5788_1052685104}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_69394_x5788_2023742920}[：指定单板，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将打开]{style="font-family:宋体"}[主用主控板的]{style="font-family:
宋体"}[拓扑调试信息开关。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_69394_x5788_1805127800}[：指定成员设备，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将打开]{style="font-family:宋体"}[主用设备的]{style="font-family:宋体"}[拓扑调试信息开关。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69394_x5788_x667385444}[：]{style="font-family:宋体"}[指定成员设备上指定单板]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将打开]{style="font-family:宋体"}[全局主用主控板的]{style="font-family:宋体"}[拓扑调试信息开关。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69394_x5788_x262313979}[：指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-88147351 .myid}
[]{#_Toc404799944}[]{#struct_0_69394_x5788_x578992896}

**MTR \-- MTR Probe命令 \-- display system internal ip topology**

------------------------------------------------------------------------

[**[display system internal ip topology]{lang="EN-US"}**]{#struct_0_69394_x5788_x806818784}[命令用来显示拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69394_x5788_306353862}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69394_x5788_x319838503}

[**[display system internal ip topology ]{lang="EN-US"}**[\[ *topology-name* \| **statistics** \]]{lang="EN-US"}]{#struct_0_69394_x5788_x579058432}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69394_x5788_483220677}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip topology]{lang="EN-US"}**[ \[ *topology-name* \| **statistics** \] \[ **s**]{lang="EN-US"}]{#struct_0_69394_x5788_2036078379}**[lot]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ *slot-number* ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ **cpu** *cpu-number* \] ]{lang="EN-US"}[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69394_x5788_47361401}[模式：]{style="font-family:宋体"}

[**[display system internal ip topology]{lang="EN-US"}**[ \[ *topology-name* \| **statistics** \] \[ ]{lang="EN-US"}]{#struct_0_69394_x5788_x1098840902}**[chassis]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[ *chassis-number* **slot** *slot-number* ]{lang="EN-US" style="font-size:10.0pt;
color:black"}[\[ **cpu** *cpu-number* \] ]{lang="EN-US"}[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69394_x5788_x695424960}

[[Probe]{lang="EN-US"}]{#struct_0_69394_x5788_x1628964714}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69394_x5788_x344291420}

[[network-admin]{lang="EN-US"}]{#struct_0_69394_x5788_x1750039227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69394_x5788_x296276291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69394_x5788_x579123968}

[*[topology-name]{lang="EN-US"}*]{#struct_0_69394_x5788_x769886572}[：配置的拓扑名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有拓扑的信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_69394_x5788_557505896}[：显示统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_69394_x5788_809926440}[：指定单板，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[主用主控板的]{style="font-family:
宋体"}[拓扑信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_69394_x5788_x1546959644}[：指定成员设备，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[主用设备的]{style="font-family:宋体"}[拓扑信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69394_x5788_884011339}[：]{style="font-family:宋体"}[指定成员设备上指定单板]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[全局主用主控板的]{style="font-family:宋体"}[拓扑信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69394_x5788_x1381898006}[：指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#868613532 .myid}
[]{#_Toc404799945}[]{#struct_0_69394_x5788_x863863109}

**MTR \-- MTR Probe命令 \-- display system internal ip topology inactive**

------------------------------------------------------------------------

[**[display system internal ip topology inactive]{lang="EN-US"}**]{#struct_0_69394_x5788_1696366489}[命令用来显示处于非活动状态的多拓扑实例信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69394_x5788_1332756989}

[**[display system internal ip topology inactive]{lang="EN-US"}**]{#struct_0_69394_x5788_172236487}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69394_x5788_x774086249}

[[Probe]{lang="EN-US"}]{#struct_0_69394_x5788_x1362969288}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69394_x5788_x299712835}

[[network-admin]{lang="EN-US"}]{#struct_0_69394_x5788_1425292565}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69394_x5788_x223863462}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_69394_x5788_438198187}

[[该命令可以显示处于删除状态，但是还没有完全删除完毕的多拓扑实例信息。]{style="font-family:宋体"}]{#struct_0_69394_x5788_x675621442}

[ ]{lang="EN-US"}
:::
