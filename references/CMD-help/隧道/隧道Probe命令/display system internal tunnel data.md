::: {#1354037335 .myid}
[]{#_Toc404800761}[]{#struct_0_x6099_14248_1452570777}[]{#_Toc338505886}[]{#_Toc273281609}[]{#_Toc218395051}[]{#_Toc215479534}[]{#_Toc207017822}[]{#_Toc207011361}[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc139515317}

**隧道 \-- 隧道Probe命令 \-- display system internal tunnel data**

------------------------------------------------------------------------

[**[display system internal tunnel data]{lang="EN-US"}**]{#struct_0_x6099_14248_360339826}[命令用来显示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6099_14248_33734620}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6099_14248_1713114690}

[**[display system internal tunnel data interface tunnel]{lang="EN-US"}**[ *number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x6099_14248_x421079192}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6099_14248_419371486}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal tunnel data interface tunnel]{lang="EN-US"}**[ *number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6099_14248_650712701}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6099_14248_144532437}[模式：]{style="font-family:宋体"}

[**[display system internal tunnel data interface tunnel]{lang="EN-US"}**[ *number* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6099_14248_x70422132}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6099_14248_x265132712}

[[Probe]{lang="EN-US"}]{#struct_0_x6099_14248_x242021896}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6099_14248_218924284}

[[network-admin]{lang="EN-US"}]{#struct_0_x6099_14248_360274290}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6099_14248_x1053871532}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6099_14248_x1940309319}

[**[interface tunnel ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x6099_14248_1871246518}[：显示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的内核数据信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口编号，取值为已创建的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x6099_14248_1568993514}[：显示指定单板的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示主用主控板的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x6099_14248_662614132}[：显示指定成员设备的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示命令所在主成员设备的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6099_14248_707758738}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口内核数据信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示全局主用主控板的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6099_14248_495103227}[：显示指定]{style="font-family:宋体"}[CPU]{lang="FR"}[上的]{style="font-family:宋体"}[Tunnel]{lang="FR"}[接口内核数据信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="FR"}[的编号。本参数的支持情况与设备的具体型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}
:::
