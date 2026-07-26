::: {#-1800639945 .myid}
[]{#_Toc404799138}[]{#struct_0_x5829_12672_x87745654}

**IP地址管理 \-- IP地址管理 Probe命令 \-- display system internal ip address**

------------------------------------------------------------------------

[**[display system internal ip address]{lang="EN-US"}**]{#struct_0_x5829_12672_x1918910939}[命令用来显示地址详细信息]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5829_12672_944823859}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x5829_12672_1930757759}

[**[display system internal ip address]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ **interface** *interface-type interface-number* \] \[ *ip-address* \] ]{lang="EN-US"}]{#struct_0_x5829_12672_x1943292178}

[[分布式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5829_12672_1907317691}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip address]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ **interface** *interface-type interface-number* \] \[ *ip-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x5829_12672_x220757545}

[[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5829_12672_x2136306468}[设备：]{style="font-family:宋体"}

[**[display system internal ip address]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ **interface** *interface-type interface-number* \] \[ *ip-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x5829_12672_206982220}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5829_12672_x1964298375}

[[Probe]{lang="EN-US"}]{#struct_0_x5829_12672_1510687399}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5829_12672_629438854}

[[network-admin]{lang="EN-US"}]{#struct_0_x5829_12672_2137232817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5829_12672_248967567}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5829_12672_x5721539}

[**[ip-address]{lang="SV" style="color:black"}**]{#struct_0_x5829_12672_x994731942}*[ ip-address]{lang="SV" style="color:
black"}*[：显示指定]{style="font-family:宋体;color:black"}[IP]{lang="SV" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[**[vpn-instance]{lang="EN-US" style="color:black"}***[ vpn-instance-name]{lang="EN-US" style="color:black"}*]{#struct_0_x5829_12672_x2074365527}[：]{style="font-family:
宋体;color:black"}[ ]{style="color:black"}[显示指定]{style="font-family:宋体;color:black"}[VPN]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[**[interface ]{lang="EN-US" style="color:black"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_x5829_12672_1274696548}[：显示指定接口的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[interface-type interface-number]{lang="EN-US" style="color:black"}*[表示接口类型和接口编号。]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x5829_12672_x1712656285}[：显示指定单板上的]{style="font-family:
宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体;
color:black"}[IP]{lang="EN-US" style="color:black"}[地址。（分布式设备－独立运行模式）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x5829_12672_1510884007}[：显示指定成员设备上的]{style="font-family:
宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体;color:black"}[Master]{lang="EN-US" style="color:black"}[设备上的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）（不支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x5829_12672_x1028159860}[：显示指定成员设备]{style="font-family:
宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号或者]{style="font-family:宋体;color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体;color:black"}[Master]{lang="EN-US" style="color:black"}[设备上的]{style="font-family:宋体;
color:black"}[IP]{lang="EN-US" style="color:black"}[地址。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x5829_12672_x1730029944}[：显示指定成员设备上指定单板的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体;
color:black"}[IP]{lang="EN-US" style="color:black"}[地址。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x5829_12672_x1353847354}[：显示指定单板的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号或者]{style="font-family:宋体;color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板或]{style="font-family:
宋体;color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x5829_12672_x1077102374}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;
color:black"}[IP]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::
