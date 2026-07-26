::: {#339378254 .myid}
[]{#_Toc404799981}[]{#struct_0_14692_16114_2006069017}[]{#_Toc386982095}[]{#_Toc374372821}[]{#_Toc371058553}

**NVGRE \-- NVGRE Probe命令 \-- display system internal nvgre forwarding tunnel**

------------------------------------------------------------------------

[**[display system internal nvgre forwarding tunnel]{lang="EN-US"}**]{#struct_0_14692_16114_x965136163}[命令用来显示]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14692_16114_1368710237}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14692_16114_x732671122}

[**[display system internal ]{lang="EN-US"}[nvgre forwarding tunnel]{lang="EN-US"}**[ \[ **vsid** *vsid* \]]{lang="EN-US"}]{#struct_0_14692_16114_x301371849}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14692_16114_1082942880}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ]{lang="EN-US"}[nvgre forwarding tunnel]{lang="EN-US"}**[ \[ **vsid** *vsid* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_14692_16114_x424243939}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14692_16114_x163619196}[模式：]{style="font-family:宋体"}

[**[display system internal ]{lang="EN-US"}[nvgre forwarding tunnel]{lang="EN-US"}**[ \[ **vsid** *vsid* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_14692_16114_x522391216}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14692_16114_2034267568}

[[Probe]{lang="EN-US"}]{#struct_0_14692_16114_210938497}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14692_16114_x1368921809}

[[network-admin]{lang="EN-US"}]{#struct_0_14692_16114_x1082383986}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14692_16114_755496074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14692_16114_x1543090351}

[*[vsid]{lang="EN-US"}*]{#struct_0_14692_16114_743316190}[：显示指定]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[vsid]{lang="EN-US"}*[为]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[虚拟子网编号，取值范围为]{style="font-family:宋体"}[4096]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。不指定此参数，则显示所有]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[网络的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14692_16114_x1058240805}*[slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14692_16114_x1151829331}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14692_16114_1766102708}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14692_16114_x873055006}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14692_16114_1053581164}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14692_16114_456044493}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道转发信息。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
