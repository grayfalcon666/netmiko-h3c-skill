::: {#132078315 .myid}
[]{#_Toc343245651}[]{#_Toc404799268}[]{#struct_0_81432_13537_x304992760}[]{#_Toc347301917}[]{#_Toc343008241}

**IP组播 \-- IP组播Probe命令 \-- debugging system internal igmp-snooping fsm tracing**

------------------------------------------------------------------------

[**[debugging]{lang="EN-US"}**[ **system** **internal** **igmp-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_x1218392561}[命令用来打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[状态机的]{style="font-family:宋体"}[Trace]{lang="EN-US"}[日志调试信息]{style="font-family:宋体"}[开关。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_1608318358}[命令用来关闭]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[状态机的]{style="font-family:宋体"}[Trace]{lang="EN-US"}[日志调试信息]{style="font-family:宋体"}[开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1556166425}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_849330834}

[**[debugging]{lang="EN-US"}**[ **system** **internal** **igmp-snooping** **fsm** **tracing** \[ **vlan** *vlan-id* \[ *group-address* *source-address* \] \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_998690243}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_x1592152788}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_988440482}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging]{lang="EN-US"}**[ **system** **internal** **igmp-snooping** **fsm** **tracing** \[ **vlan** *vlan-id* \[ *group-address* *source-address* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x455776508}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_x1218458097}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_602163201}[模式：]{style="font-family:宋体"}

[**[debugging]{lang="EN-US"}**[ **system** **internal** **igmp-snooping** **fsm** **tracing** \[ **vlan** *vlan-id* \[ *group-address* *source-address* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1113718380}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **igmp-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_x770594412}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_81432_13537_845272266}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_81432_13537_x1376430757}[状态机的]{style="font-family:宋体"}[Trace]{lang="EN-US"}[日志调试信息]{style="font-family:宋体"}[开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_546617166}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1218261489}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1336987152}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x643189208}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x2102842819}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1825543731}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x614297331}[：]{style="font-family:宋体"}[输出指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将输出所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_81432_13537_1238910612}[：输出指定组播组的信息。如果未指定本参数，将输出所有组播组的信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_81432_13537_585700341}[：输出指定组播源的信息。如果未指定本参数，将输出所有组播源的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1218327025}[：]{style="font-family:宋体"}[输出指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将输出主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1291445356}[：]{style="font-family:
宋体;color:black"}[输出指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将输出主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1294063429}[：]{style="font-family:宋体;
color:black"}[输出指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将输出主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_384988687}[：输出指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1434819926}[：输出指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1077102376}[：输出指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1796400126 .myid}
[]{#_Toc404799269}[]{#struct_0_81432_13537_x260895434}[]{#_Toc347301879}[]{#_Toc343008264}[]{#_Toc361302510}[]{#_Toc362010073}[]{#_Toc361302511}[]{#_Toc362010074}[]{#_Toc361302512}[]{#_Toc362010075}[]{#_Toc361302513}[]{#_Toc362010076}[]{#_Toc361302514}[]{#_Toc362010077}[]{#_Toc361302515}[]{#_Toc362010078}[]{#_Toc361302516}[]{#_Toc362010079}[]{#_Toc361302517}[]{#_Toc362010080}[]{#_Toc361302518}[]{#_Toc362010081}

**IP组播 \-- IP组播Probe命令 \-- debugging system internal mld-snooping fsm tracing**

------------------------------------------------------------------------

[**[debugging]{lang="EN-US"}**[ **system** **internal** **mld-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_x1559402288}[命令用来打开]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[状态机的]{style="font-family:宋体"}[Trace]{lang="EN-US"}[日志调试信息]{style="font-family:宋体"}[开关。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_939300032}[命令用来关闭]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[状态机的]{style="font-family:宋体"}[Trace]{lang="EN-US"}[日志调试信息]{style="font-family:宋体"}[开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1287878199}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_751686041}

[**[debugging]{lang="EN-US"}**[ **system** **internal** **mld-snooping** **fsm** **tracing** \[ **vlan** *vlan-id* \[ *ipv6-group-address* *ipv6-source-address* \] \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_1841097895}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_x1217999345}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_1090244521}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging]{lang="EN-US"}**[ **system** **internal** **mld-snooping** **fsm** **tracing** \[ **vlan** *vlan-id* \[ *ipv6-group-address* *ipv6-source-address* \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1386337447}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_2111450092}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_1317861665}[模式：]{style="font-family:宋体"}

[**[debugging]{lang="EN-US"}**[ **system** **internal** **mld-snooping** **fsm** **tracing** \[ **vlan** *vlan-id* \[ *ipv6-group-address* *ipv6-source-address* \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1218064881}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **mld-snooping** **fsm** **tracing**]{lang="EN-US"}]{#struct_0_81432_13537_1378101572}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_81432_13537_x194330544}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_81432_13537_x1849875000}[状态机的]{style="font-family:宋体"}[Trace]{lang="EN-US"}[日志调试信息]{style="font-family:宋体"}[开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_1687321457}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_841018418}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_821883201}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_857749121}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1217868273}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1235086829}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x945892457}[：]{style="font-family:宋体"}[输出指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将输出所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ *ipv6-group-address*]{lang="EN-US"}]{#struct_0_81432_13537_116664471}[：输出指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。如果未指定本参数，将输出所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ipv6-source-address*]{lang="EN-US"}]{#struct_0_81432_13537_705635829}[：输出指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将输出所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1217933809}[：]{style="font-family:宋体"}[输出指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将输出主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x658850840}[：]{style="font-family:
宋体;color:black"}[输出指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将输出主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_1031535399}[：]{style="font-family:宋体;
color:black"}[输出指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将输出主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1218392564}[：输出指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1462448774}[：输出指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将输出全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x316997660}[：输出指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::::: {#2011515376 .myid}
[]{#_Toc404799270}[]{#struct_0_81432_13537_1950857627}[]{#_Toc375731059}[]{#_Toc363827562}[]{#_Toc363576381}

**IP组播 \-- IP组播Probe命令 \-- display system internal igmp user-authorization record**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x740628119}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_943044200}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_1700459470}[命令用来显示按用户记录的认证模块通知给]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1124089047}

[**[display]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_x1728950953}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_572699835}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1868183897}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1419250563}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x438041239}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1511035627}
:::::

::::: {#484271875 .myid}
[]{#_Toc404799271}[]{#struct_0_81432_13537_369271459}[]{#_Toc375731060}[]{#_Toc363827564}[]{#_Toc363576383}

**IP组播 \-- IP组播Probe命令 \-- display system internal igmp user-authorization statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x740562583}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_x1356257280}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_1950661019}[命令用来显示按认证类型记录的认证模块通知给]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_2041884723}

[**[display]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_x1095212061}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x397262390}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_668089412}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1931554142}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1172193800}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1145416067}
:::::

::: {#1657827586 .myid}
[]{#_Toc347301889}[]{#_Toc342987808}[]{#_Toc404799272}[]{#struct_0_81432_13537_577537801}[]{#_Toc347301873}[]{#_Toc361302520}[]{#_Toc362010083}[]{#_Toc361302521}[]{#_Toc362010084}[]{#_Toc361302522}[]{#_Toc362010085}[]{#_Toc361302523}[]{#_Toc362010086}[]{#_Toc361302524}[]{#_Toc362010087}[]{#_Toc361302525}[]{#_Toc362010088}[]{#_Toc361302526}[]{#_Toc362010089}[]{#_Toc361302527}[]{#_Toc362010090}[]{#_Toc361302528}[]{#_Toc362010091}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast ip forwarding verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_218595148}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发表详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1991778757}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x230959540}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x475917519}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_128666092}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x823757010}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x2011722527}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **forwarding** **verbose** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1769274702}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1218327028}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1244391189}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1805999634}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x989926379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x603705728}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1118160759}

[**[group]{lang="EN-US"}**[ *ipv6-group-address*]{lang="EN-US"}]{#struct_0_81432_13537_1886685032}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ ipv6-source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x1218130420}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_1414786170}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_81432_13537_191491585}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x351903276}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1650293789}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1411355928}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1078589566}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x317325340}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-523973592 .myid}
[]{#_Toc404799273}[]{#struct_0_81432_13537_866919684}[]{#_Toc347301874}[]{#_Toc361302530}[]{#_Toc362010093}[]{#_Toc361302531}[]{#_Toc362010094}[]{#_Toc361302532}[]{#_Toc362010095}[]{#_Toc361302533}[]{#_Toc362010096}[]{#_Toc361302534}[]{#_Toc362010097}[]{#_Toc361302535}[]{#_Toc362010098}[]{#_Toc361302536}[]{#_Toc362010099}[]{#_Toc361302537}[]{#_Toc362010100}[]{#_Toc361302538}[]{#_Toc362010101}[]{#_Toc361302539}[]{#_Toc362010102}[]{#_Toc361302540}[]{#_Toc362010103}[]{#_Toc361302541}[]{#_Toc362010104}[]{#_Toc361302542}[]{#_Toc362010105}[]{#_Toc361302543}[]{#_Toc362010106}[]{#_Toc361302544}[]{#_Toc362010107}[]{#_Toc361302567}[]{#_Toc362010130}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast ip verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_1069295897}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1232495860}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1217868276}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **verbose** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address*\] \* \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x831802302}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_961989709}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **verbose** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address*\] \* \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_931371080}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x76864820}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ip** **verbose** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address*\] \* \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1379369811}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x840849829}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_933964615}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1186838202}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1217933812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_100598511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x825464373}

[**[group]{lang="EN-US"}**[ *ipv6-group-address*]{lang="EN-US"}]{#struct_0_81432_13537_989474545}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ ipv6-source-address]{lang="EN-US"}*]{#struct_0_81432_13537_404673578}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x718089889}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_81432_13537_695468525}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1218392563}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1293997893}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1523849524}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1434885462}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x317653020}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#622928641 .myid}
[]{#_Toc404799274}[]{#struct_0_81432_13537_347691381}[]{#_Toc347301875}[]{#_Toc361302569}[]{#_Toc362010132}[]{#_Toc361302570}[]{#_Toc362010133}[]{#_Toc361302571}[]{#_Toc362010134}[]{#_Toc361302572}[]{#_Toc362010135}[]{#_Toc361302573}[]{#_Toc362010136}[]{#_Toc361302574}[]{#_Toc362010137}[]{#_Toc361302575}[]{#_Toc362010138}[]{#_Toc361302576}[]{#_Toc362010139}[]{#_Toc361302577}[]{#_Toc362010140}[]{#_Toc361302578}[]{#_Toc362010141}[]{#_Toc361302579}[]{#_Toc362010142}[]{#_Toc361302580}[]{#_Toc362010143}[]{#_Toc361302581}[]{#_Toc362010144}[]{#_Toc361302582}[]{#_Toc362010145}[]{#_Toc361302583}[]{#_Toc362010146}[]{#_Toc361302584}[]{#_Toc362010147}[]{#_Toc361302585}[]{#_Toc362010148}[]{#_Toc361302586}[]{#_Toc362010149}[]{#_Toc361302587}[]{#_Toc362010150}[]{#_Toc361302588}[]{#_Toc362010151}[]{#_Toc361302589}[]{#_Toc362010152}[]{#_Toc361302590}[]{#_Toc362010153}[]{#_Toc361302651}[]{#_Toc362010214}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast ipc statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_1627955194}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播板间消息的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1597123346}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_981954668}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics** \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x80606248}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_345376576}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1754475091}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x412059699}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **ipc** **statistics** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x2008022547}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_347625845}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_845514598}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_900921274}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_2050185346}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1373491492}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1375092753}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1448324239}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_325901516}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果[未指定本参数，将显示主设备上的信息。（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x131198479}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x862595710}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1697282420}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x317063197}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#460122561 .myid}
[]{#_Toc404799275}[]{#struct_0_81432_13537_x1963088240}[]{#_Toc347301876}[]{#_Toc361302653}[]{#_Toc362010216}[]{#_Toc361302654}[]{#_Toc362010217}[]{#_Toc361302655}[]{#_Toc362010218}[]{#_Toc361302656}[]{#_Toc362010219}[]{#_Toc361302657}[]{#_Toc362010220}[]{#_Toc361302658}[]{#_Toc362010221}[]{#_Toc361302659}[]{#_Toc362010222}[]{#_Toc361302660}[]{#_Toc362010223}[]{#_Toc361302684}[]{#_Toc362010247}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast mac forwarding verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x555132358}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[转发表详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2102458166}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1845714722}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1922820828}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x1774686114}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_348084597}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x997346168}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **forwarding** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x292155648}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1652980881}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_303657833}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_47821273}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x122632990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1200286423}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x307294880}

[*[mac-address]{lang="EN-US"}*]{#struct_0_81432_13537_348019061}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_558001874}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1951350383}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1739947229}[：]{style="font-family:
宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x534483006}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_211797810}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1073588435}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x317325341}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#2117826497 .myid}
[]{#_Toc404799276}[]{#struct_0_81432_13537_x559945520}[]{#_Toc347301877}[]{#_Toc361302686}[]{#_Toc362010249}[]{#_Toc361302687}[]{#_Toc362010250}[]{#_Toc361302688}[]{#_Toc362010251}[]{#_Toc361302689}[]{#_Toc362010252}[]{#_Toc361302690}[]{#_Toc362010253}[]{#_Toc361302691}[]{#_Toc362010254}[]{#_Toc361302692}[]{#_Toc362010255}[]{#_Toc361302693}[]{#_Toc362010256}[]{#_Toc361302694}[]{#_Toc362010257}[]{#_Toc361302695}[]{#_Toc362010258}[]{#_Toc361302696}[]{#_Toc362010259}[]{#_Toc361302697}[]{#_Toc362010260}[]{#_Toc361302698}[]{#_Toc362010261}[]{#_Toc361302699}[]{#_Toc362010262}[]{#_Toc361302700}[]{#_Toc362010263}[]{#_Toc361302723}[]{#_Toc362010286}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast mac verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_347625846}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_845514601}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_2040038166}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_1578556467}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x750915581}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_363899886}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x978276253}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **mac** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_409320826}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x672162022}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_347822454}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_624623275}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1876704478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_6162201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_609269699}

[*[mac-address]{lang="EN-US"}*]{#struct_0_81432_13537_1239360305}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_557913406}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_347756918}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_85791599}[：]{style="font-family:宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_628316408}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_2080246943}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_940977152}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x317653021}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-667569517 .myid}
[]{#_Toc404799277}[]{#struct_0_81432_13537_x701991728}[]{#_Toc369010539}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 l2-multicast trill-offload-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **trill-offload-table**]{lang="EN-US"}]{#struct_0_81432_13537_x381131165}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播维护的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1475495684}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_583589404}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **trill-offload-table** \[ **local** \| **remote** \] \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_81432_13537_x701926192}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x1579754749}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **trill-offload-table** \[ **local** \| **remote** \] \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_393695713}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_4500900}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **l2-multicast** **trill-offload-table** \[ **local** \| **remote** \] \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1549069439}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x701336368}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1203119536}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1725273930}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x139750927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1627316920}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1642771766}

[**[local]{lang="EN-US"}**]{#struct_0_81432_13537_x701270832}[：显示入表项信息。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_81432_13537_x1945898818}[：显示出表项信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x1605805052}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_955507040}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1790526104}[：]{style="font-family:
宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1293932357}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x701860655}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x271234707}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}
:::

::: {#-1961988540 .myid}
[]{#_Toc404799278}[]{#struct_0_81432_13537_x1199736922}[]{#_Toc347301853}[]{#_Toc361302725}[]{#_Toc362010288}[]{#_Toc361302726}[]{#_Toc362010289}[]{#_Toc361302727}[]{#_Toc362010290}[]{#_Toc361302728}[]{#_Toc362010291}[]{#_Toc361302729}[]{#_Toc362010292}[]{#_Toc361302730}[]{#_Toc362010293}[]{#_Toc361302731}[]{#_Toc362010294}[]{#_Toc361302732}[]{#_Toc362010295}[]{#_Toc361302733}[]{#_Toc362010296}[]{#_Toc361302734}[]{#_Toc362010297}[]{#_Toc361302735}[]{#_Toc362010298}[]{#_Toc361302736}[]{#_Toc362010299}[]{#_Toc361302737}[]{#_Toc362010300}[]{#_Toc361302738}[]{#_Toc362010301}[]{#_Toc361302739}[]{#_Toc362010302}[]{#_Toc361302740}[]{#_Toc362010303}[]{#_Toc361302741}[]{#_Toc362010304}[]{#_Toc361302772}[]{#_Toc362010335}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 mrib interface statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **mrib** **interface** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_1172294965}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[MRIB]{lang="EN-US"}[所维护接口的]{style="font-family:宋体"}[统计]{style="font-family:宋体"}[信息，这些接口包括配置了]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[、]{style="font-family:宋体"}[MLD]{lang="EN-US"}[等]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播协议的接口以及注册接口、]{style="font-family:宋体"}[InLoopBack0]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Null0]{lang="EN-US"}[接口等内部接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_348215670}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **mrib** \[ **vpn-instance** *vpn-instance-name* \] **interface** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_822892551}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1885605698}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1326676038}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1542305179}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_441357242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1130039057}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2108209829}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_81432_13537_x501300947}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}
:::

::: {#1797378340 .myid}
[]{#_Toc404799279}[]{#struct_0_81432_13537_841171361}[]{#_Toc347301854}[]{#_Toc361302774}[]{#_Toc362010337}[]{#_Toc361302775}[]{#_Toc362010338}[]{#_Toc361302776}[]{#_Toc362010339}[]{#_Toc361302777}[]{#_Toc362010340}[]{#_Toc361302778}[]{#_Toc362010341}[]{#_Toc361302779}[]{#_Toc362010342}[]{#_Toc361302780}[]{#_Toc362010343}[]{#_Toc361302781}[]{#_Toc362010344}[]{#_Toc361302782}[]{#_Toc362010345}[]{#_Toc361302783}[]{#_Toc362010346}[]{#_Toc361302784}[]{#_Toc362010347}[]{#_Toc361302785}[]{#_Toc362010348}[]{#_Toc361302786}[]{#_Toc362010349}[]{#_Toc361302787}[]{#_Toc362010350}[]{#_Toc361302830}[]{#_Toc362010393}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 mrib mbr**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **mrib** **mbr** **interface**]{lang="EN-US"}]{#struct_0_81432_13537_1277018329}[命令用来显示]{style="font-family:
宋体"}[IPv6 MRIB]{lang="EN-US"}[进程中]{style="font-family:
宋体"}[MBR]{lang="EN-US"}[（]{style="font-family:宋体"}[Multicast Border Router]{lang="EN-US"}[，组播边界路由器）模块维护的组加入信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_347887987}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **mrib** \[ **vpn-instance** *vpn-instance-name* \] **mbr** **interface** *interface-type* *interface-number* \[ **source** *ipv6-source-address* **group** *ipv6-group-address* \]]{lang="EN-US"}]{#struct_0_81432_13537_x524938845}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1962957168}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_531602551}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x393063951}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_551667563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1817989814}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_2015573052}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_81432_13537_x1828742407}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_81432_13537_348084595}[：显示指定接口上的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ipv6-source-address*]{lang="EN-US"}]{#struct_0_81432_13537_x997346166}[：显示指定组播源的信息。如果未指定本参数，将不显示]{style="font-family:宋体"}[IPv6 MBR]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ *ipv6-group-address*]{lang="EN-US"}]{#struct_0_81432_13537_x292024576}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将不显示]{style="font-family:宋体"}[IPv6 MBR]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}
:::

::: {#1865977475 .myid}
[]{#_Toc404799280}[]{#struct_0_81432_13537_1417155420}[]{#_Toc361302832}[]{#_Toc362010395}[]{#_Toc361302833}[]{#_Toc362010396}[]{#_Toc361302834}[]{#_Toc362010397}[]{#_Toc361302835}[]{#_Toc362010398}[]{#_Toc361302836}[]{#_Toc362010399}[]{#_Toc361302837}[]{#_Toc362010400}[]{#_Toc361302838}[]{#_Toc362010401}[]{#_Toc361302839}[]{#_Toc362010402}[]{#_Toc361302840}[]{#_Toc362010403}[]{#_Toc361302841}[]{#_Toc362010404}[]{#_Toc361302842}[]{#_Toc362010405}[]{#_Toc361302843}[]{#_Toc362010406}[]{#_Toc361302844}[]{#_Toc362010407}[]{#_Toc361302845}[]{#_Toc362010408}[]{#_Toc361302846}[]{#_Toc362010409}[]{#_Toc361302847}[]{#_Toc362010410}[]{#_Toc361302848}[]{#_Toc362010411}[]{#_Toc361302849}[]{#_Toc362010412}[]{#_display_mld_group}[]{#_Toc361302874}[]{#_Toc362010437}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast forwarding vlan reference**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference**]{lang="EN-US"}]{#struct_0_81432_13537_899048149}[命令用来显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[出接口与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播表项之间的映射关系]{style="font-family:宋体"}[。]{style="font-size:11.0pt;
font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_125304112}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_347625844}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_845514599}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_900921273}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_2050185339}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_1373819173}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** **forwarding** **vlan** **reference** \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x524543343}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_774135565}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x957101024}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x661750423}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_347822452}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_624623281}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1156660442}

[**[group]{lang="EN-US"}**[ *ipv6-group-address*]{lang="EN-US"}]{#struct_0_81432_13537_1547904203}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ipv6-source-address*]{lang="EN-US"}]{#struct_0_81432_13537_1568960578}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_347756916}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_85791605}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1423432174}[：]{style="font-family:
宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_1031666471}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x842879792}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x534417470}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x317194270}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1698818960 .myid}
[]{#_Toc404799281}[]{#struct_0_81432_13537_858197267}[]{#_Toc347301856}[]{#_Toc342997008}[]{#_Toc361302876}[]{#_Toc362010439}[]{#_Toc361302877}[]{#_Toc362010440}[]{#_Toc361302878}[]{#_Toc362010441}[]{#_Toc361302879}[]{#_Toc362010442}[]{#_Toc361302880}[]{#_Toc362010443}[]{#_Toc361302881}[]{#_Toc362010444}[]{#_Toc361302882}[]{#_Toc362010445}[]{#_Toc361302883}[]{#_Toc362010446}[]{#_Toc361302884}[]{#_Toc362010447}[]{#_Toc361302885}[]{#_Toc362010448}[]{#_Toc361302886}[]{#_Toc362010449}[]{#_Toc361302887}[]{#_Toc362010450}[]{#_Toc361302888}[]{#_Toc362010451}[]{#_Toc361302910}[]{#_Toc362010473}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast forwarding-table dummy**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** **forwarding-table** **dummy**]{lang="EN-US"}]{#struct_0_81432_13537_760064242}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播临时转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1399332873}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_1206611865}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **cpu** *cpu-number* \| **statistics** \] \*]{lang="EN-US"}]{#struct_0_81432_13537_1312987197}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_348019060}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **statistics** \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_81432_13537_558001873}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1951350376}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **statistics** \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x2142641932}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1605116615}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1347525506}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1714939234}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x2109328325}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1526282699}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_348215668}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_81432_13537_x1515759617}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x792828539}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_81432_13537_x138444333}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均表示]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_81432_13537_1289818152}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址的前缀长度。对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[；对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，其取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x317063199}[：显示指定单板上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1354420629}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_628381944}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1746948676}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1759193780}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x316997663}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US" style="color:black"}**]{#struct_0_81432_13537_1964665154}[：]{style="font-family:
宋体;color:black"}[显示统计信息。]{style="font-family:宋体;color:black"}
:::

::: {#-73650097 .myid}
[]{#_Toc404799282}[]{#struct_0_81432_13537_x997346164}[]{#_Toc347301857}[]{#_Toc361302912}[]{#_Toc362010475}[]{#_Toc361302913}[]{#_Toc362010476}[]{#_Toc361302914}[]{#_Toc362010477}[]{#_Toc361302915}[]{#_Toc362010478}[]{#_Toc361302916}[]{#_Toc362010479}[]{#_Toc361302917}[]{#_Toc362010480}[]{#_Toc361302918}[]{#_Toc362010481}[]{#_Toc361302919}[]{#_Toc362010482}[]{#_Toc361302920}[]{#_Toc362010483}[]{#_Toc361302921}[]{#_Toc362010484}[]{#_Toc361302922}[]{#_Toc362010485}[]{#_Toc361302923}[]{#_Toc362010486}[]{#_Toc361302924}[]{#_Toc362010487}[]{#_Toc361302952}[]{#_Toc362010515}[]{#_Toc361302953}[]{#_Toc362010516}[]{#_Toc361302954}[]{#_Toc362010517}[]{#_Toc361302955}[]{#_Toc362010518}[]{#_Toc361302956}[]{#_Toc362010519}[]{#_Toc361302957}[]{#_Toc362010520}[]{#_Toc361302958}[]{#_Toc362010521}[]{#_Toc361302959}[]{#_Toc362010522}[]{#_Toc361302960}[]{#_Toc362010523}[]{#_Toc361302961}[]{#_Toc362010524}[]{#_Toc361302962}[]{#_Toc362010525}[]{#_Toc361302963}[]{#_Toc362010526}[]{#_Toc361302964}[]{#_Toc362010527}[]{#_Toc361302965}[]{#_Toc362010528}[]{#_Toc361302990}[]{#_Toc362010553}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast forwarding-table verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** **forwarding-table** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x291893504}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播转发表的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1234880728}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x721742827}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **verbose** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **cpu** *cpu-number* \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x1056511314}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x849121348}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **verbose** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x1955429022}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x258837614}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **verbose** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_348019057}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1015976232}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x740178343}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_547272094}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_695674022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1659700871}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x814603096}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_81432_13537_x2102037227}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_81432_13537_2143955444}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_81432_13537_348215665}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均表示]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_81432_13537_x1515759604}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址的前缀长度。对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[；对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，其取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[incoming-interface]{lang="EN-US"}**]{#struct_0_81432_13537_88157079}[：显示指定入接口的信息。如果未指定本参数，将显示所有入接口的信息。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_81432_13537_551709385}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}**]{#struct_0_81432_13537_x534342068}[：]{style="font-family:宋体"}[显示指定出接口的信息。如果未指定本参数，将显示所有出接口的信息。]{style="font-family:宋体"}

[**[exclude]{lang="EN-US"}**]{#struct_0_81432_13537_1687407489}[：显示不包含指定接口的信息。]{style="font-family:宋体"}

[**[include]{lang="EN-US"}**]{#struct_0_81432_13537_2000409798}[：]{style="font-family:宋体"}[显示包含指定接口的信息。]{style="font-family:宋体"}

[**[match]{lang="EN-US"}**]{#struct_0_81432_13537_x564186791}[：]{style="font-family:宋体"}[显示包含且仅包含指定接口的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_348150129}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1320412137}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_1078720638}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x317587489}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1294391109}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883212673}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#590891342 .myid}
[]{#_Toc347301866}[]{#_Toc404799283}[]{#struct_0_81432_13537_x2024961614}[]{#_Toc345423891}[]{#_Toc361302992}[]{#_Toc362010555}[]{#_Toc361302993}[]{#_Toc362010556}[]{#_Toc361302994}[]{#_Toc362010557}[]{#_Toc361302995}[]{#_Toc362010558}[]{#_Toc361302996}[]{#_Toc362010559}[]{#_Toc361302997}[]{#_Toc362010560}[]{#_Toc361302998}[]{#_Toc362010561}[]{#_Toc361302999}[]{#_Toc362010562}[]{#_Toc361303000}[]{#_Toc362010563}[]{#_Toc361303001}[]{#_Toc362010564}[]{#_Toc361303002}[]{#_Toc362010565}[]{#_Toc361303003}[]{#_Toc362010566}[]{#_Toc361303004}[]{#_Toc362010567}[]{#_Toc361303005}[]{#_Toc362010568}[]{#_Toc361303006}[]{#_Toc362010569}[]{#_Toc361303007}[]{#_Toc362010570}[]{#_Toc361303008}[]{#_Toc362010571}[]{#_Toc361303009}[]{#_Toc362010572}[]{#_Toc361303010}[]{#_Toc362010573}[]{#_Toc361303011}[]{#_Toc362010574}[]{#_Toc361303012}[]{#_Toc362010575}[]{#_Toc361303013}[]{#_Toc362010576}[]{#_Toc361303014}[]{#_Toc362010577}[]{#_Toc361303060}[]{#_Toc362010623}[]{#_Toc361303061}[]{#_Toc362010624}[]{#_Toc239838367}[]{#_Toc239838369}[]{#_Toc239838370}[]{#_Toc239838371}[]{#_Toc239838372}[]{#_Toc239838373}[]{#_Toc239838374}[]{#_Toc239838375}[]{#_Toc239838376}[]{#_Toc239838377}[]{#_Toc239838378}[]{#_Toc239838379}[]{#_Toc239838380}[]{#_Toc239838381}[]{#_Toc239838382}[]{#_Toc239838383}[]{#_Toc239838384}[]{#_Toc239838385}[]{#_Toc239838386}[]{#_Toc239838387}[]{#_Toc239838389}[]{#_Toc239838392}[]{#_Toc239838393}[]{#_Toc239838406}[]{#_Toc239838408}[]{#_Toc239838410}[]{#_Toc239838411}[]{#_Toc239838412}[]{#_Toc239838413}[]{#_Toc239838414}[]{#_Toc239838415}[]{#_Toc239838416}[]{#_Toc239838417}[]{#_Toc239838418}[]{#_Toc239838419}[]{#_Toc239838420}[]{#_Toc239838421}[]{#_Toc239838422}[]{#_Toc239838423}[]{#_Toc239838424}[]{#_Toc239838425}[]{#_Toc239838426}[]{#_Toc239838427}[]{#_Toc239838428}[]{#_Toc239838429}[]{#_Toc239838430}[]{#_Toc239838431}[]{#_Toc239838432}[]{#_Toc239838433}[]{#_Toc239838434}[]{#_Toc239838435}[]{#_Toc239838437}[]{#_Toc239838439}[]{#_Toc239838442}[]{#_Toc239838444}[]{#_Toc239838445}[]{#_Toc239838446}[]{#_Toc239838471}[]{#_Toc131673363}[]{#_Toc131913571}[]{#_Toc131921487}[]{#_Toc131921539}[]{#_Toc131929831}[]{#_Toc132017317}[]{#_Toc132021674}[]{#_Toc132021781}[]{#_Toc132595862}[]{#_Toc239838473}[]{#_Toc239838474}[]{#_Toc239838475}[]{#_Toc239838476}[]{#_Toc239838477}[]{#_Toc239838478}[]{#_Toc239838479}[]{#_Toc239838480}[]{#_Toc239838481}[]{#_Toc239838482}[]{#_Toc239838483}[]{#_Toc239838484}[]{#_Toc239838485}[]{#_Toc239838486}[]{#_Toc239838487}[]{#_Toc239838488}[]{#_Toc239838489}[]{#_Toc239838490}[]{#_Toc239838491}[]{#_Toc239838492}[]{#_Toc239838493}[]{#_Toc239838495}[]{#_Toc239838497}[]{#_Toc239838500}[]{#_Toc239838501}[]{#_Toc239838502}[]{#_Toc239838503}[]{#_Toc239838504}[]{#_Toc239838506}[]{#_Toc239838507}[]{#_Toc239838509}[]{#_Toc239838510}[]{#_Toc239838538}[]{#_Toc131673365}[]{#_Toc131913573}[]{#_Toc131921489}[]{#_Toc131921541}[]{#_Toc131929833}[]{#_Toc132017319}[]{#_Toc132021676}[]{#_Toc132021783}[]{#_Toc132595864}[]{#_Toc239838540}[]{#_Toc239838541}[]{#_Toc239838542}[]{#_Toc239838543}[]{#_Toc239838544}[]{#_Toc239838545}[]{#_Toc239838546}[]{#_Toc239838547}[]{#_Toc239838548}[]{#_Toc239838549}[]{#_Toc239838550}[]{#_Toc239838551}[]{#_Toc239838552}[]{#_Toc239838553}[]{#_Toc239838554}[]{#_Toc239838555}[]{#_Toc239838556}[]{#_Toc239838559}[]{#_Toc239838560}[]{#_Toc239838562}[]{#_Toc239838564}[]{#_Toc239838565}[]{#_Toc239838596}[]{#_Toc87442270}[]{#_Toc87786910}[]{#_Toc87851772}[]{#_Toc87852553}[]{#_Toc87853332}[]{#_Toc87867371}[]{#_Toc87442272}[]{#_Toc87786912}[]{#_Toc87851774}[]{#_Toc87852555}[]{#_Toc87853334}[]{#_Toc87867373}[]{#_Toc87442273}[]{#_Toc87786913}[]{#_Toc87851775}[]{#_Toc87852556}[]{#_Toc87853335}[]{#_Toc87867374}[]{#_Toc87442274}[]{#_Toc87786914}[]{#_Toc87851776}[]{#_Toc87852557}[]{#_Toc87853336}[]{#_Toc87867375}[]{#_Toc87442275}[]{#_Toc87786915}[]{#_Toc87851777}[]{#_Toc87852558}[]{#_Toc87853337}[]{#_Toc87867376}[]{#_Toc87442276}[]{#_Toc87786916}[]{#_Toc87851778}[]{#_Toc87852559}[]{#_Toc87853338}[]{#_Toc87867377}[]{#_Toc87442277}[]{#_Toc87786917}[]{#_Toc87851779}[]{#_Toc87852560}[]{#_Toc87853339}[]{#_Toc87867378}[]{#_Toc87442278}[]{#_Toc87786918}[]{#_Toc87851780}[]{#_Toc87852561}[]{#_Toc87853340}[]{#_Toc87867379}[]{#_Toc87442279}[]{#_Toc87786919}[]{#_Toc87851781}[]{#_Toc87852562}[]{#_Toc87853341}[]{#_Toc87867380}[]{#_Toc87442280}[]{#_Toc87786920}[]{#_Toc87851782}[]{#_Toc87852563}[]{#_Toc87853342}[]{#_Toc87867381}[]{#_Toc87442281}[]{#_Toc87786921}[]{#_Toc87851783}[]{#_Toc87852564}[]{#_Toc87853343}[]{#_Toc87867382}[]{#_Toc87442282}[]{#_Toc87786922}[]{#_Toc87851784}[]{#_Toc87852565}[]{#_Toc87853344}[]{#_Toc87867383}[]{#_Toc87442283}[]{#_Toc87786923}[]{#_Toc87851785}[]{#_Toc87852566}[]{#_Toc87853345}[]{#_Toc87867384}[]{#_Toc87442284}[]{#_Toc87786924}[]{#_Toc87851786}[]{#_Toc87852567}[]{#_Toc87853346}[]{#_Toc87867385}[]{#_Toc87442285}[]{#_Toc87786925}[]{#_Toc87851787}[]{#_Toc87852568}[]{#_Toc87853347}[]{#_Toc87867386}[]{#_Toc87442286}[]{#_Toc87786926}[]{#_Toc87851788}[]{#_Toc87852569}[]{#_Toc87853348}[]{#_Toc87867387}[]{#_Toc87442287}[]{#_Toc87786927}[]{#_Toc87851789}[]{#_Toc87852570}[]{#_Toc87853349}[]{#_Toc87867388}[]{#_Toc87442319}[]{#_Toc87786959}[]{#_Toc87851821}[]{#_Toc87852602}[]{#_Toc87853381}[]{#_Toc87867420}[]{#_Toc87442331}[]{#_Toc87786971}[]{#_Toc87851833}[]{#_Toc87852614}[]{#_Toc87853393}[]{#_Toc87867432}[]{#_Toc239838597}[]{#_Toc239838598}[]{#_Toc239838599}[]{#_Toc239838600}[]{#_Toc239838601}[]{#_Toc239838602}[]{#_Toc239838603}[]{#_Toc239838604}[]{#_Toc239838605}[]{#_Toc239838606}[]{#_Toc239838607}[]{#_Toc239838608}[]{#_Toc239838609}[]{#_Toc239838610}[]{#_Toc239838611}[]{#_Toc239838612}[]{#_Toc239838613}[]{#_Toc239838614}[]{#_Toc239838615}[]{#_Toc239838616}[]{#_Toc239838617}[]{#_Toc239838618}[]{#_Toc239838619}[]{#_Toc239838620}[]{#_Toc239838621}[]{#_Toc239838622}[]{#_Toc239838623}[]{#_Toc239838624}[]{#_Toc239838625}[]{#_Toc239838626}[]{#_Toc239838627}[]{#_Toc239838628}[]{#_Toc239838629}[]{#_Toc239838630}[]{#_Toc239838631}[]{#_Toc239838632}[]{#_Toc239838633}[]{#_Toc239838635}[]{#_Toc239838637}[]{#_Toc239838638}[]{#_Toc239838639}[]{#_Toc239838640}[]{#_Toc239838641}[]{#_Toc239838642}[]{#_Toc239838643}[]{#_Toc239838644}[]{#_Toc239838645}[]{#_Toc239838646}[]{#_Toc239838647}[]{#_Toc239838648}[]{#_Toc239838649}[]{#_Toc239838650}[]{#_Toc239838651}[]{#_Toc239838652}[]{#_Toc239838653}[]{#_Toc239838654}[]{#_Toc239838655}[]{#_Toc239838656}[]{#_Toc239838657}[]{#_Toc239838658}[]{#_Toc239838659}[]{#_Toc239838660}[]{#_Toc239838661}[]{#_Toc239838662}[]{#_Toc239838663}[]{#_Toc239838664}[]{#_Toc239838667}[]{#_Toc239838671}[]{#_Toc239838672}[]{#_Toc239838673}[]{#_Toc239838674}[]{#_Toc239838675}[]{#_Toc239838676}[]{#_Toc239838677}[]{#_Toc239838678}[]{#_Toc239838679}[]{#_Toc239838680}[]{#_Toc239838681}[]{#_Toc239838682}[]{#_Toc239838683}[]{#_Toc239838684}[]{#_Toc239838685}[]{#_Toc239838686}[]{#_Toc239838689}[]{#_Toc239838690}[]{#_Toc239838691}[]{#_Toc239838692}[]{#_Toc239838700}[]{#_Toc239838702}[]{#_Toc239838709}[]{#_Toc239838710}[]{#_Toc239838747}[]{#_Toc239838749}[]{#_Toc239838750}[]{#_Toc239838751}[]{#_Toc239838752}[]{#_Toc239838753}[]{#_Toc239838754}[]{#_Toc239838755}[]{#_Toc239838756}[]{#_Toc239838757}[]{#_Toc239838758}[]{#_Toc239838759}[]{#_Toc239838760}[]{#_Toc239838761}[]{#_Toc239838762}[]{#_Toc239838763}[]{#_Toc239838764}[]{#_Toc239838765}[]{#_Toc239838766}[]{#_Toc239838767}[]{#_Toc239838768}[]{#_Toc239838769}[]{#_Toc239838770}[]{#_Toc239838771}[]{#_Toc239838773}[]{#_Toc239838774}[]{#_Toc239838775}[]{#_Toc239838776}[]{#_Toc239838778}[]{#_Toc239838779}[]{#_Toc239838780}[]{#_Toc239838781}[]{#_Toc239838784}[]{#_Toc239838785}[]{#_Toc239838786}[]{#_Toc239838787}[]{#_Toc239838788}[]{#_Toc239838789}[]{#_Toc239838790}[]{#_Toc239838791}[]{#_Toc239838792}[]{#_Toc239838793}[]{#_Toc239838794}[]{#_Toc239838795}[]{#_Toc239838796}[]{#_Toc239838797}[]{#_Toc239838798}[]{#_Toc239838799}[]{#_Toc239838800}[]{#_Toc239838801}[]{#_Toc239838802}[]{#_Toc239838806}[]{#_Toc239838807}[]{#_Toc239838808}[]{#_Toc239838809}[]{#_Toc239838810}[]{#_Toc239838811}[]{#_Toc239838812}[]{#_Toc239838813}[]{#_Toc239838814}[]{#_Toc239838815}[]{#_Toc239838816}[]{#_Toc239838817}[]{#_Toc239838818}[]{#_Toc239838819}[]{#_Toc239838820}[]{#_Toc239838821}[]{#_Toc239838823}[]{#_Toc239838824}[]{#_Toc239838827}[]{#_Toc239838828}[]{#_Toc239838829}[]{#_Toc239838830}[]{#_Toc239838831}[]{#_Toc239838832}[]{#_Toc239838833}[]{#_Toc239838834}[]{#_Toc239838835}[]{#_Toc239838836}[]{#_Toc239838837}[]{#_Toc239838838}[]{#_Toc239838839}[]{#_Toc239838840}[]{#_Toc239838841}[]{#_Toc239838842}[]{#_Toc239838843}[]{#_Toc239838845}[]{#_Toc239838846}[]{#_Toc239838849}[]{#_Toc239838851}[]{#_Toc239838852}[]{#_Toc239838853}[]{#_Toc239838854}[]{#_Toc239838855}[]{#_Toc239838856}[]{#_Toc239838857}[]{#_Toc239838858}[]{#_Toc239838859}[]{#_Toc239838860}[]{#_Toc239838861}[]{#_Toc239838862}[]{#_Toc239838863}[]{#_Toc239838864}[]{#_Toc239838865}[]{#_Toc239838868}[]{#_Toc239838872}[]{#_Toc239838873}[]{#_Toc239838876}[]{#_Toc239838877}[]{#_Toc239838878}[]{#_Toc239838879}[]{#_Toc239838880}[]{#_Toc239838881}[]{#_Toc239838882}[]{#_Toc239838883}[]{#_Toc239838884}[]{#_Toc239838885}[]{#_Toc239838886}[]{#_Toc239838887}[]{#_Toc239838889}[]{#_Toc239838890}[]{#_Toc239838893}[]{#_Toc239838894}[]{#_Toc239838895}[]{#_Toc239838896}[]{#_Toc239838897}[]{#_Toc239838898}[]{#_Toc239838899}[]{#_Toc239838900}[]{#_Toc239838901}[]{#_Toc239838902}[]{#_Toc239838903}[]{#_Toc239838904}[]{#_Toc239838905}[]{#_Toc239838906}[]{#_Toc239838907}[]{#_Toc239838908}[]{#_Toc239838909}[]{#_Toc239838910}[]{#_Toc239838911}[]{#_Toc239838913}[]{#_Toc87442345}[]{#_Toc87786985}[]{#_Toc87851847}[]{#_Toc87852630}[]{#_Toc87853411}[]{#_Toc87867450}[]{#_Toc87442346}[]{#_Toc87786986}[]{#_Toc87851848}[]{#_Toc87852631}[]{#_Toc87853412}[]{#_Toc87867451}[]{#_Toc87442347}[]{#_Toc87786987}[]{#_Toc87851849}[]{#_Toc87852632}[]{#_Toc87853413}[]{#_Toc87867452}[]{#_Toc87442348}[]{#_Toc87786988}[]{#_Toc87851850}[]{#_Toc87852633}[]{#_Toc87853414}[]{#_Toc87867453}[]{#_Toc87442349}[]{#_Toc87786989}[]{#_Toc87851851}[]{#_Toc87852634}[]{#_Toc87853415}[]{#_Toc87867454}[]{#_Toc87442350}[]{#_Toc87786990}[]{#_Toc87851852}[]{#_Toc87852635}[]{#_Toc87853416}[]{#_Toc87867455}[]{#_Toc87442351}[]{#_Toc87786991}[]{#_Toc87851853}[]{#_Toc87852636}[]{#_Toc87853417}[]{#_Toc87867456}[]{#_Toc87442352}[]{#_Toc87786992}[]{#_Toc87851854}[]{#_Toc87852637}[]{#_Toc87853418}[]{#_Toc87867457}[]{#_Toc87442353}[]{#_Toc87786993}[]{#_Toc87851855}[]{#_Toc87852638}[]{#_Toc87853419}[]{#_Toc87867458}[]{#_Toc87442354}[]{#_Toc87786994}[]{#_Toc87851856}[]{#_Toc87852639}[]{#_Toc87853420}[]{#_Toc87867459}[]{#_Toc87442355}[]{#_Toc87786995}[]{#_Toc87851857}[]{#_Toc87852640}[]{#_Toc87853421}[]{#_Toc87867460}[]{#_Toc87442356}[]{#_Toc87786996}[]{#_Toc87851858}[]{#_Toc87852641}[]{#_Toc87853422}[]{#_Toc87867461}[]{#_Toc87442357}[]{#_Toc87786997}[]{#_Toc87851859}[]{#_Toc87852642}[]{#_Toc87853423}[]{#_Toc87867462}[]{#_Toc87442358}[]{#_Toc87786998}[]{#_Toc87851860}[]{#_Toc87852643}[]{#_Toc87853424}[]{#_Toc87867463}[]{#_Toc87442359}[]{#_Toc87786999}[]{#_Toc87851861}[]{#_Toc87852644}[]{#_Toc87853425}[]{#_Toc87867464}[]{#_Toc87442360}[]{#_Toc87787000}[]{#_Toc87851862}[]{#_Toc87852645}[]{#_Toc87853426}[]{#_Toc87867465}[]{#_Toc87442361}[]{#_Toc87787001}[]{#_Toc87851863}[]{#_Toc87852646}[]{#_Toc87853427}[]{#_Toc87867466}[]{#_Toc87442362}[]{#_Toc87787002}[]{#_Toc87851864}[]{#_Toc87852647}[]{#_Toc87853428}[]{#_Toc87867467}[]{#_Toc87442363}[]{#_Toc87787003}[]{#_Toc87851865}[]{#_Toc87852648}[]{#_Toc87853429}[]{#_Toc87867468}[]{#_Toc87442364}[]{#_Toc87787004}[]{#_Toc87851866}[]{#_Toc87852649}[]{#_Toc87853430}[]{#_Toc87867469}[]{#_Toc87442365}[]{#_Toc87787005}[]{#_Toc87851867}[]{#_Toc87852650}[]{#_Toc87853431}[]{#_Toc87867470}[]{#_Toc87442366}[]{#_Toc87787006}[]{#_Toc87851868}[]{#_Toc87852651}[]{#_Toc87853432}[]{#_Toc87867471}[]{#_Toc87442367}[]{#_Toc87787007}[]{#_Toc87851869}[]{#_Toc87852652}[]{#_Toc87853433}[]{#_Toc87867472}[]{#_Toc87442368}[]{#_Toc87787008}[]{#_Toc87851870}[]{#_Toc87852653}[]{#_Toc87853434}[]{#_Toc87867473}[]{#_Toc87442369}[]{#_Toc87787009}[]{#_Toc87851871}[]{#_Toc87852654}[]{#_Toc87853435}[]{#_Toc87867474}[]{#_Toc87442370}[]{#_Toc87787010}[]{#_Toc87851872}[]{#_Toc87852655}[]{#_Toc87853436}[]{#_Toc87867475}[]{#_Toc87442371}[]{#_Toc87787011}[]{#_Toc87851873}[]{#_Toc87852656}[]{#_Toc87853437}[]{#_Toc87867476}[]{#_Toc87442372}[]{#_Toc87787012}[]{#_Toc87851874}[]{#_Toc87852657}[]{#_Toc87853438}[]{#_Toc87867477}[]{#_Toc87442373}[]{#_Toc87787013}[]{#_Toc87851875}[]{#_Toc87852658}[]{#_Toc87853439}[]{#_Toc87867478}[]{#_Toc87442374}[]{#_Toc87787014}[]{#_Toc87851876}[]{#_Toc87852659}[]{#_Toc87853440}[]{#_Toc87867479}[]{#_Toc208113006}[]{#_Toc208115110}[]{#_Toc208113007}[]{#_Toc208115111}[]{#_Toc208113009}[]{#_Toc208115113}[]{#_Toc208113010}[]{#_Toc208115114}[]{#_Toc208113011}[]{#_Toc208115115}[]{#_Toc208113012}[]{#_Toc208115116}[]{#_Toc208113013}[]{#_Toc208115117}[]{#_Toc208113014}[]{#_Toc208115118}[]{#_Toc208113015}[]{#_Toc208115119}[]{#_Toc208113016}[]{#_Toc208115120}[]{#_Toc208113017}[]{#_Toc208115121}[]{#_Toc208113018}[]{#_Toc208115122}[]{#_Toc208113019}[]{#_Toc208115123}[]{#_Toc208113020}[]{#_Toc208115124}[]{#_Toc208113021}[]{#_Toc208115125}[]{#_Toc208113022}[]{#_Toc208115126}[]{#_Toc208113023}[]{#_Toc208115127}[]{#_Toc208113024}[]{#_Toc208115128}[]{#_Toc208113025}[]{#_Toc208115129}[]{#_Toc208113026}[]{#_Toc208115130}[]{#_Toc208113027}[]{#_Toc208115131}[]{#_Toc208113029}[]{#_Toc208115133}[]{#_Toc208113030}[]{#_Toc208115134}[]{#_Toc208113031}[]{#_Toc208115135}[]{#_Toc208113033}[]{#_Toc208115137}[]{#_Toc239838916}[]{#_Toc239838918}[]{#_Toc239838919}[]{#_Toc239838920}[]{#_Toc239838921}[]{#_Toc239838922}[]{#_Toc239838923}[]{#_Toc239838924}[]{#_Toc239838925}[]{#_Toc239838926}[]{#_Toc239838927}[]{#_Toc239838928}[]{#_Toc239838929}[]{#_Toc239838930}[]{#_Toc239838931}[]{#_Toc239838932}[]{#_Toc239838934}[]{#_Toc239838935}[]{#_Toc239838939}[]{#_Toc239838941}[]{#_Toc239838944}[]{#_Toc239838945}[]{#_Toc239838946}[]{#_Toc239838947}[]{#_Toc239838948}[]{#_Toc239838949}[]{#_Toc239838950}[]{#_Toc239838951}[]{#_Toc239838952}[]{#_Toc239838953}[]{#_Toc239838954}[]{#_Toc239838955}[]{#_Toc239838956}[]{#_Toc239838957}[]{#_Toc239838958}[]{#_Toc239838959}[]{#_Toc239838962}[]{#_Toc239838963}[]{#_Toc239838965}[]{#_Toc239838966}[]{#_Toc239838967}[]{#_Toc239838968}[]{#_Toc239838969}[]{#_Toc239838970}[]{#_Toc239838971}[]{#_Toc239838972}[]{#_Toc239838973}[]{#_Toc239838974}[]{#_Toc239838975}[]{#_Toc239838976}[]{#_Toc239838977}[]{#_Toc239838978}[]{#_Toc239838979}[]{#_Toc239838980}[]{#_Toc239838981}[]{#_Toc239838983}[]{#_Toc361303098}[]{#_Toc362010661}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 multicast-vlan forwarding-table verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_1466752035}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_294665380}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_7979772}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **cpu** *cpu-number* \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x842854987}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x1865007250}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_521179573}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1742777700}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **multicast-vlan** **forwarding-table** **verbose** \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x2025027150}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_349277823}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x970478731}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1032347048}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1139128169}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_473283030}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1477640529}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_81432_13537_1087777345}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_81432_13537_456643814}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_81432_13537_897096312}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址的前缀长度。对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，其取值范[围为]{style="color:black"}]{style="font-family:宋体"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[128]{lang="EN-US" style="color:black"}[，缺省值为]{style="font-family:宋体;
color:black"}[128]{lang="EN-US" style="color:black"}[；对于]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:
black"}[组播组地址，其取值范围为]{style="font-family:宋体;color:black"}[8]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[128]{lang="EN-US" style="color:black"}[，缺省值为]{style="font-family:宋体;
color:black"}[128]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x225335663}[：显示指定单板上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1901830956}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x131591695}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1883474817}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x2084278814}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883409281}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[subvlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_957686501}[：显示指定子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。如果未指定本参数，将显示所有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x173821592}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}
:::

::: {#-474056831 .myid}
[]{#_Toc404799284}[]{#struct_0_81432_13537_x1886258087}[]{#_Toc361303100}[]{#_Toc362010663}[]{#_Toc361303101}[]{#_Toc362010664}[]{#_Toc361303102}[]{#_Toc362010665}[]{#_Toc361303103}[]{#_Toc362010666}[]{#_Toc361303104}[]{#_Toc362010667}[]{#_Toc361303105}[]{#_Toc362010668}[]{#_Toc361303106}[]{#_Toc362010669}[]{#_Toc361303107}[]{#_Toc362010670}[]{#_Toc361303108}[]{#_Toc362010671}[]{#_Toc361303109}[]{#_Toc362010672}[]{#_Toc361303110}[]{#_Toc362010673}[]{#_Toc361303111}[]{#_Toc362010674}[]{#_Toc361303112}[]{#_Toc362010675}[]{#_Toc361303113}[]{#_Toc362010676}[]{#_Toc361303114}[]{#_Toc362010677}[]{#_Toc361303115}[]{#_Toc362010678}[]{#_Toc361303116}[]{#_Toc362010679}[]{#_Toc361303117}[]{#_Toc362010680}[]{#_Toc361303118}[]{#_Toc362010681}[]{#_Toc361303119}[]{#_Toc362010682}[]{#_Toc361303156}[]{#_Toc362010719}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 pim interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_x2024437326}**[system]{lang="EN-US"}**[ **internal** ]{lang="EN-US"}**[ipv6]{lang="EN-US"}**[ ]{lang="EN-US"}**[pim]{lang="EN-US"}**[ **interface**]{lang="EN-US"}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[进程中]{style="font-family:宋体"}[路由管理]{style="font-family:宋体"}[LIB]{lang="EN-US"}[所维护的接口信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1886442531}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_946507193}**[system]{lang="EN-US"}**[ **internal** ]{lang="EN-US"}**[ipv6]{lang="EN-US"}**[ ]{lang="EN-US"}**[pim]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[interface]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ *interface-type* *interface-number* \[ **address** \| **gateway** \| **prefix**\] \] \| *ipv6-address* *prefix-length* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1494096400}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1987352374}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x6779298}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x472184236}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1717185433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x988679832}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_81432_13537_x2024502862}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网实例的信息。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_81432_13537_816809937}[：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。]{style="font-family:宋体"}

[**[address]{lang="EN-US"}**]{#struct_0_81432_13537_x189383397}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[gateway]{lang="EN-US"}**]{#struct_0_81432_13537_x717893641}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**]{#struct_0_81432_13537_975009099}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_81432_13537_377176737}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的信息。]{style="font-family:宋体"}[::]{lang="EN-US"}[为保留地址，用户不感知。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_81432_13537_x1155370061}[：表示前缀长度，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}
:::

::: {#715717225 .myid}
[]{#_Toc404799285}[]{#struct_0_81432_13537_215114106}[]{#_Toc347301867}[]{#_Toc361303158}[]{#_Toc362010721}[]{#_Toc361303159}[]{#_Toc362010722}[]{#_Toc361303160}[]{#_Toc362010723}[]{#_Toc361303161}[]{#_Toc362010724}[]{#_Toc361303162}[]{#_Toc362010725}[]{#_Toc361303163}[]{#_Toc362010726}[]{#_Toc361303164}[]{#_Toc362010727}[]{#_Toc361303165}[]{#_Toc362010728}[]{#_Toc361303166}[]{#_Toc362010729}[]{#_Toc361303167}[]{#_Toc362010730}[]{#_Toc361303168}[]{#_Toc362010731}[]{#_Toc361303169}[]{#_Toc362010732}[]{#_Toc361303170}[]{#_Toc362010733}[]{#_Toc361303171}[]{#_Toc362010734}[]{#_Toc361303172}[]{#_Toc362010735}[]{#_Toc361303173}[]{#_Toc362010736}[]{#_Toc361303174}[]{#_Toc362010737}[]{#_Toc361303175}[]{#_Toc362010738}[]{#_Toc361303176}[]{#_Toc362010739}[]{#_Toc361303177}[]{#_Toc362010740}[]{#_Toc361303178}[]{#_Toc362010741}[]{#_Toc361303179}[]{#_Toc362010742}[]{#_Toc361303180}[]{#_Toc362010743}[]{#_Toc361303181}[]{#_Toc362010744}[]{#_Toc361303182}[]{#_Toc362010745}[]{#_Toc361303183}[]{#_Toc362010746}[]{#_Toc361303184}[]{#_Toc362010747}[]{#_Toc361303185}[]{#_Toc362010748}[]{#_Toc361303186}[]{#_Toc362010749}[]{#_Toc361303187}[]{#_Toc362010750}[]{#_Toc361303188}[]{#_Toc362010751}[]{#_Toc361303189}[]{#_Toc362010752}[]{#_Toc361303190}[]{#_Toc362010753}[]{#_Toc361303191}[]{#_Toc362010754}[]{#_Toc361303192}[]{#_Toc362010755}[]{#_Toc361303253}[]{#_Toc362010816}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 pim rp**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **pim** **rp**]{lang="EN-US"}]{#struct_0_81432_13537_x1972591730}[命令用来显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_181152565}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **pim** \[ **vpn-instance** *vpn-instance-name* \] **rp**]{lang="EN-US"}]{#struct_0_81432_13537_1251172944}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_93207488}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x2024961616}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_303952621}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1873683401}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_674605408}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1010652140}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_81432_13537_1923685289}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网实例的信息。]{style="font-family:宋体"}
:::

::: {#-310570098 .myid}
[]{#_Toc404799286}[]{#struct_0_81432_13537_726509783}[]{#_Toc347301868}[]{#_Toc361303255}[]{#_Toc362010818}[]{#_Toc361303256}[]{#_Toc362010819}[]{#_Toc361303257}[]{#_Toc362010820}[]{#_Toc361303258}[]{#_Toc362010821}[]{#_Toc361303259}[]{#_Toc362010822}[]{#_Toc361303260}[]{#_Toc362010823}[]{#_Toc361303261}[]{#_Toc362010824}[]{#_Toc361303262}[]{#_Toc362010825}[]{#_Toc361303263}[]{#_Toc362010826}[]{#_Toc361303264}[]{#_Toc362010827}[]{#_Toc361303265}[]{#_Toc362010828}[]{#_Toc361303266}[]{#_Toc362010829}[]{#_Toc361303267}[]{#_Toc362010830}[]{#_Toc361303268}[]{#_Toc362010831}[]{#_Toc361303302}[]{#_Toc362010865}

**IP组播 \-- IP组播Probe命令 \-- display system internal ipv6 pim thread**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **pim** **thread**]{lang="EN-US"}]{#struct_0_81432_13537_159083136}[命令用来显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[线程的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_2043929359}

[**[display]{lang="EN-US"}**[ **system** **internal** **ipv6** **pim** **thread** { **event** \| **main** \| **route** }]{lang="EN-US"}]{#struct_0_81432_13537_300896122}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1108570402}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x2024568400}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_710979213}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x2093866904}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_728292293}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1781495202}

[**[event]{lang="EN-US"}**]{#struct_0_81432_13537_x987513356}[：显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[事件线程的统计信息。]{style="font-family:宋体"}

[**[main]{lang="EN-US"}**]{#struct_0_81432_13537_x1565667275}[：显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[主线程的统计信息。]{style="font-family:宋体"}

[**[route]{lang="EN-US"}**]{#struct_0_81432_13537_862175787}[：显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由线程的统计信息。]{style="font-family:宋体"}
:::

::: {#1360451034 .myid}
[]{#_Toc404799287}[]{#struct_0_81432_13537_396902646}[]{#_Toc347301911}[]{#_Toc361303304}[]{#_Toc362010867}[]{#_Toc361303305}[]{#_Toc362010868}[]{#_Toc361303306}[]{#_Toc362010869}[]{#_Toc361303307}[]{#_Toc362010870}[]{#_Toc361303308}[]{#_Toc362010871}[]{#_Toc361303309}[]{#_Toc362010872}[]{#_Toc361303310}[]{#_Toc362010873}[]{#_Toc361303311}[]{#_Toc362010874}[]{#_Toc361303312}[]{#_Toc362010875}[]{#_Toc361303313}[]{#_Toc362010876}[]{#_Toc361303314}[]{#_Toc362010877}[]{#_Toc361303315}[]{#_Toc362010878}[]{#_Toc361303316}[]{#_Toc362010879}[]{#_Toc361303317}[]{#_Toc362010880}[]{#_Toc361303318}[]{#_Toc362010881}[]{#_Toc361303319}[]{#_Toc362010882}[]{#_Toc361303320}[]{#_Toc362010883}[]{#_Toc361303321}[]{#_Toc362010884}[]{#_Toc361303382}[]{#_Toc362010945}[]{#_Toc361303383}[]{#_Toc362010946}[]{#_Toc361303384}[]{#_Toc362010947}[]{#_Toc361303385}[]{#_Toc362010948}[]{#_Toc361303386}[]{#_Toc362010949}[]{#_Toc361303387}[]{#_Toc362010950}[]{#_Toc361303388}[]{#_Toc362010951}[]{#_Toc361303389}[]{#_Toc362010952}[]{#_Toc361303390}[]{#_Toc362010953}[]{#_Toc361303391}[]{#_Toc362010954}[]{#_Toc361303392}[]{#_Toc362010955}[]{#_Toc361303393}[]{#_Toc362010956}[]{#_Toc361303394}[]{#_Toc362010957}[]{#_Toc361303395}[]{#_Toc362010958}[]{#_Toc361303396}[]{#_Toc362010959}[]{#_Toc361303397}[]{#_Toc362010960}[]{#_Toc361303428}[]{#_Toc362010991}[]{#_Toc361303429}[]{#_Toc362010992}[]{#_Toc361303430}[]{#_Toc362010993}[]{#_Toc361303431}[]{#_Toc362010994}[]{#_Toc361303432}[]{#_Toc362010995}[]{#_Toc361303433}[]{#_Toc362010996}[]{#_Toc361303434}[]{#_Toc362010997}[]{#_Toc361303435}[]{#_Toc362010998}[]{#_Toc361303436}[]{#_Toc362010999}[]{#_Toc361303437}[]{#_Toc362011000}[]{#_Toc361303438}[]{#_Toc362011001}[]{#_Toc361303439}[]{#_Toc362011002}[]{#_Toc361303440}[]{#_Toc362011003}[]{#_Toc361303441}[]{#_Toc362011004}[]{#_Toc361303442}[]{#_Toc362011005}[]{#_Toc361303443}[]{#_Toc362011006}[]{#_Toc361303495}[]{#_Toc362011058}

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast ip forwarding verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **forwarding** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x485095706}[命令用来显示二层组播的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[转发表详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2024437330}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1245790887}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **forwarding** **verbose** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_1452456098}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_988834034}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **forwarding** **verbose** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1561499033}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_1247486733}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **forwarding** **verbose** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1933150129}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x530115334}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1171102473}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2024502866}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1508788891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_886780857}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1528940936}

[**[group]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_81432_13537_x339791175}[：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ source-address]{lang="EN-US"}*]{#struct_0_81432_13537_1514630682}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x2024961617}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_81432_13537_1870036562}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_81432_13537_1176301743}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果[未指定本参数，将显示主设备上的信息。（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_627923192}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1261813899}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1650621469}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883278210}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1944855332 .myid}
[]{#_Toc404799288}[]{#struct_0_81432_13537_2043835684}[]{#_Toc347301912}[]{#_Toc361303497}[]{#_Toc362011060}[]{#_Toc361303498}[]{#_Toc362011061}[]{#_Toc361303499}[]{#_Toc362011062}[]{#_Toc361303500}[]{#_Toc362011063}[]{#_Toc361303501}[]{#_Toc362011064}[]{#_Toc361303502}[]{#_Toc362011065}[]{#_Toc361303503}[]{#_Toc362011066}[]{#_Toc361303504}[]{#_Toc362011067}[]{#_Toc361303505}[]{#_Toc362011068}[]{#_Toc361303506}[]{#_Toc362011069}[]{#_Toc361303507}[]{#_Toc362011070}[]{#_Toc361303508}[]{#_Toc362011071}[]{#_Toc361303509}[]{#_Toc362011072}[]{#_Toc361303510}[]{#_Toc362011073}[]{#_Toc361303511}[]{#_Toc362011074}[]{#_Toc361303534}[]{#_Toc362011097}

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast ip verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x2024699473}[命令用来显示二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x284190577}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_1190806626}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **verbose** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1176092451}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x459411641}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **verbose** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1019380238}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1766311434}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **ip** **verbose** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1518310538}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1062140604}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x2024765009}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1968168646}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1212502311}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_277886985}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x896922203}

[**[group]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_81432_13537_x468173484}[：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x2024568401}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x2017904142}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_81432_13537_1467779053}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x2010635469}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1294325573}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x2060593693}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1110979037}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883081603}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-636847321 .myid}
[]{#_Toc404799289}[]{#struct_0_81432_13537_x1481366864}[]{#_Toc347301913}[]{#_Toc361303536}[]{#_Toc362011099}[]{#_Toc361303537}[]{#_Toc362011100}[]{#_Toc361303538}[]{#_Toc362011101}[]{#_Toc361303539}[]{#_Toc362011102}[]{#_Toc361303540}[]{#_Toc362011103}[]{#_Toc361303541}[]{#_Toc362011104}[]{#_Toc361303542}[]{#_Toc362011105}[]{#_Toc361303543}[]{#_Toc362011106}[]{#_Toc361303544}[]{#_Toc362011107}[]{#_Toc361303545}[]{#_Toc362011108}[]{#_Toc361303546}[]{#_Toc362011109}[]{#_Toc361303547}[]{#_Toc362011110}[]{#_Toc361303548}[]{#_Toc362011111}[]{#_Toc361303549}[]{#_Toc362011112}[]{#_Toc361303550}[]{#_Toc362011113}[]{#_Toc361303551}[]{#_Toc362011114}[]{#_Toc361303552}[]{#_Toc362011115}[]{#_Toc361303553}[]{#_Toc362011116}[]{#_Toc361303554}[]{#_Toc362011117}[]{#_Toc361303555}[]{#_Toc362011118}[]{#_Toc361303556}[]{#_Toc362011119}[]{#_Toc361303557}[]{#_Toc362011120}[]{#_Toc361303618}[]{#_Toc362011181}

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast ipc statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_1141726718}**[system]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ **internal**]{lang="EN-US" style="font-size:10.0pt;color:black"}[ **l2-multicast** **ipc** **statistics**]{lang="EN-US"}[命令用来显示二层组播板间消息的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1848477652}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1124402106}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_477031307}**[system]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ **internal**]{lang="EN-US" style="font-size:10.0pt;color:black"}[ **l2-multicast** **ipc** **statistics** \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_1997116538}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_x1047182909}**[system]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ **internal**]{lang="EN-US" style="font-size:10.0pt;color:black"}[ **l2-multicast** **ipc** **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_454608164}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_x458353385}**[system]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ **internal**]{lang="EN-US" style="font-size:10.0pt;color:black"}[ **l2-multicast** **ipc** **statistics** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x619146145}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1348713291}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1116131027}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1378774935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1843602424}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_715344498}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x874563533}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1825999110}[：]{style="font-family:
宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x131526159}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x458418921}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1697610100}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883736963}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。（分布式设备－独立运行模式]{style="font-family:宋体;color:black"}[/]{lang="EN-US" style="color:black"}[集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备]{style="font-family:宋体;
color:black"}[/]{lang="EN-US" style="color:black"}[分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}
:::

::: {#1251069798 .myid}
[]{#_Toc404799290}[]{#struct_0_81432_13537_x1121819133}[]{#_Toc347301914}[]{#_Toc361303620}[]{#_Toc362011183}[]{#_Toc361303621}[]{#_Toc362011184}[]{#_Toc361303622}[]{#_Toc362011185}[]{#_Toc361303623}[]{#_Toc362011186}[]{#_Toc361303624}[]{#_Toc362011187}[]{#_Toc361303625}[]{#_Toc362011188}[]{#_Toc361303626}[]{#_Toc362011189}[]{#_Toc361303627}[]{#_Toc362011190}[]{#_Toc361303651}[]{#_Toc362011214}

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast mac forwarding verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **forwarding** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x2003289588}[命令用来显示二层组播的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[转发表详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x458812136}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1810953768}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **forwarding** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_1899638515}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x1758547054}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **forwarding** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1900606695}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x243659547}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **forwarding** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1299065607}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_270055038}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_758912899}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x458615528}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_2121706434}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_2114207243}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x864195335}

[*[mac-address]{lang="EN-US"}*]{#struct_0_81432_13537_x1917098041}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x769637685}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_81432_13537_x458681064}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1442939342}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x534810686}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x568278187}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_892330782}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883474820}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1120730626 .myid}
[]{#_Toc404799291}[]{#struct_0_81432_13537_102623076}[]{#_Toc361303653}[]{#_Toc362011216}[]{#_Toc361303654}[]{#_Toc362011217}[]{#_Toc361303655}[]{#_Toc362011218}[]{#_Toc361303656}[]{#_Toc362011219}[]{#_Toc361303657}[]{#_Toc362011220}[]{#_Toc361303658}[]{#_Toc362011221}[]{#_Toc361303659}[]{#_Toc362011222}[]{#_Toc361303660}[]{#_Toc362011223}[]{#_Toc361303661}[]{#_Toc362011224}[]{#_Toc361303662}[]{#_Toc362011225}[]{#_Toc361303663}[]{#_Toc362011226}[]{#_Toc361303664}[]{#_Toc362011227}[]{#_Toc361303665}[]{#_Toc362011228}[]{#_Toc361303666}[]{#_Toc362011229}[]{#_Toc361303667}[]{#_Toc362011230}[]{#_Toc361303690}[]{#_Toc362011253}

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast mac verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x839044060}[命令用来显示二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x458418920}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_1237030755}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1562766050}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_1748437169}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1222245448}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1072245163}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **mac** **verbose** \[ *mac-address* \] \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_570867164}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_1781565514}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x208552492}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x458877675}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1756904755}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x473890521}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x915406075}

[*[mac-address]{lang="EN-US"}*]{#struct_0_81432_13537_x768099368}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x584585184}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x458943211}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1339331870}[：]{style="font-family:
宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_627988728}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1098883234}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1219338359}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883671428}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#10021535 .myid}
[]{#_Toc404799292}[]{#struct_0_81432_13537_864354355}[]{#_Toc369010554}[]{#_Toc363134029}

**IP组播 \-- IP组播Probe命令 \-- display system internal l2-multicast trill-offload-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **trill-offload-table**]{lang="EN-US"}]{#struct_0_81432_13537_x488904581}[命令用来显示二层组播维护的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1565714493}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_1432150852}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **trill-offload-table** \[ **local** \| **remote** \] \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1064102655}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_864419891}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **trill-offload-table** \[ **local** \| **remote** \] \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_144507478}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_705065314}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **l2-multicast** **trill-offload-table** \[ **local** \| **remote** \] \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1368806256}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_815720103}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1160590780}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_863961139}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1842199005}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1533256406}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_725146080}

[**[local]{lang="EN-US"}**]{#struct_0_81432_13537_x701691225}[：显示入表项信息。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_81432_13537_864026675}[：显示出表项信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_469737985}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1366873580}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1002518931}[：]{style="font-family:
宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1428019013}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_885901342}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x670665053}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}
:::

::::: {#1457324934 .myid}
[]{#_Toc404799293}[]{#struct_0_81432_13537_34572641}[]{#_Toc375731080}[]{#_Toc363827565}

**IP组播 \-- IP组播Probe命令 \-- display system internal mld user-authorization record**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x740955803}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_1407693793}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_1000948388}[命令用来显示按用户记录的认证模块通知给]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1758971811}

[**[display]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_x259543219}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1280994150}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1438939241}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1121210341}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_2078684198}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1665465133}
:::::

::::: {#1152457001 .myid}
[]{#_Toc404799294}[]{#struct_0_81432_13537_x2067424687}[]{#_Toc375731081}[]{#_Toc363827567}

**IP组播 \-- IP组播Probe命令 \-- display system internal mld user-authorization statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x741414555}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_x2104213786}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_34507105}[命令用来显示按认证类型记录的认证模块通知给]{style="font-family:宋体"}[MLD]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1356797205}

[**[display]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_x917179277}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x124124590}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_280047202}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1220464967}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_351157909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1317720773}
:::::

::: {#92310361 .myid}
[]{#_Toc404799295}[]{#struct_0_81432_13537_x458484459}[]{#_Toc347301887}[]{#_Toc361303692}[]{#_Toc362011255}[]{#_Toc361303693}[]{#_Toc362011256}[]{#_Toc361303694}[]{#_Toc362011257}[]{#_Toc361303695}[]{#_Toc362011258}[]{#_Toc361303696}[]{#_Toc362011259}[]{#_Toc361303697}[]{#_Toc362011260}[]{#_Toc361303698}[]{#_Toc362011261}[]{#_Toc361303699}[]{#_Toc362011262}[]{#_Toc361303700}[]{#_Toc362011263}[]{#_Toc361303701}[]{#_Toc362011264}[]{#_Toc361303702}[]{#_Toc362011265}[]{#_Toc361303703}[]{#_Toc362011266}[]{#_Toc361303704}[]{#_Toc362011267}[]{#_Toc361303705}[]{#_Toc362011268}[]{#_Toc361303706}[]{#_Toc362011269}[]{#_Toc361303707}[]{#_Toc362011270}[]{#_Toc361303708}[]{#_Toc362011271}[]{#_Toc361303739}[]{#_Toc362011302}

**IP组播 \-- IP组播Probe命令 \-- display system internal mrib interface statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **mrib** **interface** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_x1804656608}[命令用来显示]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[所维护接口的]{style="font-family:宋体"}[统计]{style="font-family:宋体"}[信息，这些接口包括配置了]{style="font-family:宋体"}[PIM]{lang="EN-US"}[、]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[等组播协议的接口以及注册接口、]{style="font-family:宋体"}[InLoopBack0]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Null0]{lang="EN-US"}[接口等内部接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1541591072}

[**[display]{lang="EN-US"}**[ **system** **internal** **mrib** \[ **vpn-instance** *vpn-instance-name* \] **interface** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_190609546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_2086038263}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1463171553}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x810703950}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1828424468}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x458549995}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1480973648}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_81432_13537_1190092490}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}
:::

::: {#-1256461881 .myid}
[]{#_Toc404799296}[]{#struct_0_81432_13537_243647868}[]{#_Toc347301888}[]{#_Toc342902034}[]{#_Toc361303741}[]{#_Toc362011304}[]{#_Toc361303742}[]{#_Toc362011305}[]{#_Toc361303743}[]{#_Toc362011306}[]{#_Toc361303744}[]{#_Toc362011307}[]{#_Toc361303745}[]{#_Toc362011308}[]{#_Toc361303746}[]{#_Toc362011309}[]{#_Toc361303747}[]{#_Toc362011310}[]{#_Toc361303748}[]{#_Toc362011311}[]{#_Toc361303749}[]{#_Toc362011312}[]{#_Toc361303750}[]{#_Toc362011313}[]{#_Toc361303751}[]{#_Toc362011314}[]{#_Toc361303752}[]{#_Toc362011315}[]{#_Toc361303753}[]{#_Toc362011316}[]{#_Toc361303754}[]{#_Toc362011317}[]{#_Toc361303797}[]{#_Toc362011360}

**IP组播 \-- IP组播Probe命令 \-- display system internal mrib mbr**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **mrib** **mbr**]{lang="EN-US"}]{#struct_0_81432_13537_x1794331154}[命令用来显示]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[进程中]{style="font-family:宋体"}[MBR]{lang="EN-US"}[模块维护的组加入信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1434529694}

[**[display]{lang="EN-US"}**[ **system** **internal** **mrib** \[ **vpn-instance** *vpn-instance-name* \] **mbr** **interface** *interface-type* *interface-number* \[ **source** *source-address* **group** *group-address* \]]{lang="EN-US"}]{#struct_0_81432_13537_x458615530}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_2122230721}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1184442139}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x792621639}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x172445238}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x59547567}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_593462268}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_81432_13537_x1444942325}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1291561715}[：显示指定接口上的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *source-address*]{lang="EN-US"}]{#struct_0_81432_13537_x458681066}[：显示指定组播源的信息。如果未指定本参数，将不显示]{style="font-family:宋体"}[MBR]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_81432_13537_x1443070414}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将不显示]{style="font-family:宋体"}[MBR]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}
:::

::: {#-379610767 .myid}
[]{#_Toc404799297}[]{#struct_0_81432_13537_1012225464}[]{#_Toc361303799}[]{#_Toc362011362}[]{#_Toc361303800}[]{#_Toc362011363}[]{#_Toc361303801}[]{#_Toc362011364}[]{#_Toc361303802}[]{#_Toc362011365}[]{#_Toc361303803}[]{#_Toc362011366}[]{#_Toc361303804}[]{#_Toc362011367}[]{#_Toc361303805}[]{#_Toc362011368}[]{#_Toc361303806}[]{#_Toc362011369}[]{#_Toc361303807}[]{#_Toc362011370}[]{#_Toc361303808}[]{#_Toc362011371}[]{#_Toc361303809}[]{#_Toc362011372}[]{#_Toc361303810}[]{#_Toc362011373}[]{#_Toc361303811}[]{#_Toc362011374}[]{#_Toc361303812}[]{#_Toc362011375}[]{#_Toc361303813}[]{#_Toc362011376}[]{#_Toc361303814}[]{#_Toc362011377}[]{#_Toc361303815}[]{#_Toc362011378}[]{#_Toc361303816}[]{#_Toc362011379}[]{#_Toc361303842}[]{#_Toc362011405}

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast capability**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **capability**]{lang="EN-US"}]{#struct_0_81432_13537_x145726662}[命令用来显示组播能力的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1957713357}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x458877677}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **capability**]{lang="EN-US"}]{#struct_0_81432_13537_x1757035827}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x1902956598}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **capability** \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1197070376}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1974723987}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **capability** \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1576260431}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x59140866}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1435205294}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_442469962}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x458943213}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1339200798}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x412412588}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_1149430127}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1475067052}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，则显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x668504126}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_389540303}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x50072686}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}
:::

::: {#762318935 .myid}
[]{#_Toc404799298}[]{#struct_0_81432_13537_468315141}[]{#_Toc361303844}[]{#_Toc362011407}[]{#_Toc361303845}[]{#_Toc362011408}[]{#_Toc361303846}[]{#_Toc362011409}[]{#_Toc361303847}[]{#_Toc362011410}[]{#_Toc361303848}[]{#_Toc362011411}[]{#_Toc361303849}[]{#_Toc362011412}[]{#_Toc361303850}[]{#_Toc362011413}[]{#_Toc361303851}[]{#_Toc362011414}[]{#_Toc361303852}[]{#_Toc362011415}[]{#_Toc361303853}[]{#_Toc362011416}[]{#_Toc361303854}[]{#_Toc362011417}[]{#_Toc361303855}[]{#_Toc362011418}[]{#_Toc361303856}[]{#_Toc362011419}[]{#_Toc361303857}[]{#_Toc362011420}[]{#_Toc361303858}[]{#_Toc362011421}[]{#_Toc361303859}[]{#_Toc362011422}[]{#_Toc361303860}[]{#_Toc362011423}[]{#_Toc361303861}[]{#_Toc362011424}[]{#_Toc361303862}[]{#_Toc362011425}[]{#_Toc361303863}[]{#_Toc362011426}[]{#_Toc361303864}[]{#_Toc362011427}[]{#_Toc361303865}[]{#_Toc362011428}[]{#_Toc361303866}[]{#_Toc362011429}[]{#_Toc361303867}[]{#_Toc362011430}[]{#_Toc361303901}[]{#_Toc362011464}

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast forwarding vlan reference**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **forwarding** **vlan** **reference**]{lang="EN-US"}]{#struct_0_81432_13537_x458549997}[命令用来显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[出接口与二层组播表项之间的映射关系]{style="font-family:宋体"}[。]{style="font-size:11.0pt;
font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1481104720}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_1992014711}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **forwarding** **vlan** **reference** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x439866600}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_835320289}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **forwarding** **vlan** **reference** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1802152529}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_649831374}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **forwarding** **vlan** **reference** \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_1727651000}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x458353389}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x619408289}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1040222340}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_666799546}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x256737802}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1700184687}

[**[group]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_81432_13537_x458418925}[：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *source-address*]{lang="EN-US"}]{#struct_0_81432_13537_1237358435}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_1501477401}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1418100426}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1750038561}[：]{style="font-family:
宋体;color:black"}[显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_494295288}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1475332590}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1038500940}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1883343750}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1496264796 .myid}
[]{#_Toc404799299}[]{#struct_0_81432_13537_x1811346989}[]{#_Toc347301891}[]{#_Toc342987806}[]{#_Toc361303903}[]{#_Toc362011466}[]{#_Toc361303904}[]{#_Toc362011467}[]{#_Toc361303905}[]{#_Toc362011468}[]{#_Toc361303906}[]{#_Toc362011469}[]{#_Toc361303907}[]{#_Toc362011470}[]{#_Toc361303908}[]{#_Toc362011471}[]{#_Toc361303909}[]{#_Toc362011472}[]{#_Toc361303910}[]{#_Toc362011473}[]{#_Toc361303911}[]{#_Toc362011474}[]{#_Toc361303912}[]{#_Toc362011475}[]{#_Toc361303913}[]{#_Toc362011476}[]{#_Toc361303914}[]{#_Toc362011477}[]{#_Toc361303915}[]{#_Toc362011478}[]{#_Toc361303937}[]{#_Toc362011500}

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast forwarding-table dummy**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **forwarding-table** **dummy**]{lang="EN-US"}]{#struct_0_81432_13537_x1710827142}[命令用来显示组播临时转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_856619307}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1510225077}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **cpu** *cpu-number* \| **statistics** \] \*]{lang="EN-US"}]{#struct_0_81432_13537_1227285501}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x2100570543}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **statistics** \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x1426819281}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_475291541}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **statistics** \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x458615532}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_2122361793}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x383673506}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1596469103}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1143993034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1274596883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2050953202}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_81432_13537_x455968835}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_81432_13537_59348933}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x458681068}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_81432_13537_x1443201486}[：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；对于组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_81432_13537_2017359684}[：指定组播组或组播源地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1963753407}[：显示指定单板上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1184225210}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1427953477}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x754644435}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_501056486}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1479797074}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US" style="color:black"}**]{#struct_0_81432_13537_x1477828515}[：]{style="font-family:
宋体;color:black"}[显示]{style="font-family:宋体;color:black"}[统计信息。]{style="font-family:宋体"}
:::

::: {#1666630704 .myid}
[]{#_Toc404799300}[]{#struct_0_81432_13537_757946784}[]{#_Toc347301892}[]{#_Toc361303939}[]{#_Toc362011502}[]{#_Toc361303940}[]{#_Toc362011503}[]{#_Toc361303941}[]{#_Toc362011504}[]{#_Toc361303942}[]{#_Toc362011505}[]{#_Toc361303943}[]{#_Toc362011506}[]{#_Toc361303944}[]{#_Toc362011507}[]{#_Toc361303945}[]{#_Toc362011508}[]{#_Toc361303946}[]{#_Toc362011509}[]{#_Toc361303947}[]{#_Toc362011510}[]{#_Toc361303948}[]{#_Toc362011511}[]{#_Toc361303949}[]{#_Toc362011512}[]{#_Toc361303950}[]{#_Toc362011513}[]{#_Toc361303951}[]{#_Toc362011514}[]{#_Toc361303979}[]{#_Toc362011542}[]{#_Toc361303980}[]{#_Toc362011543}[]{#_Toc361303981}[]{#_Toc362011544}[]{#_Toc361303982}[]{#_Toc362011545}[]{#_Toc361303983}[]{#_Toc362011546}[]{#_Toc361303984}[]{#_Toc362011547}[]{#_Toc361303985}[]{#_Toc362011548}[]{#_Toc361303986}[]{#_Toc362011549}[]{#_Toc361303987}[]{#_Toc362011550}[]{#_Toc361303988}[]{#_Toc362011551}[]{#_Toc361303989}[]{#_Toc362011552}[]{#_Toc361303990}[]{#_Toc362011553}[]{#_Toc361303991}[]{#_Toc362011554}[]{#_Toc361303992}[]{#_Toc362011555}[]{#_Toc361304017}[]{#_Toc362011580}

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast forwarding-table verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **forwarding-table** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x394567265}[命令用来显示组播转发表的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1551997603}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1843530836}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **verbose** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **cpu** *cpu-number* \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_1920394458}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_681402772}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **verbose** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x1351721923}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1752703974}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **verbose** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **incoming-interface** *interface-type* *interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_x1625983788}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1253822567}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1246596943}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1146980237}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1920459994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x947434282}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1938800918}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_81432_13537_x1954381431}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_81432_13537_x73144830}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x989690006}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_81432_13537_204621100}[：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；对于组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_81432_13537_x1873826898}[：指定组播组或组播源地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[incoming-interface]{lang="EN-US"}**]{#struct_0_81432_13537_1920263386}[：显示指定入接口的信息。如果未指定本参数，将显示所有入接口的信息。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_81432_13537_1006997995}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}**]{#struct_0_81432_13537_644382877}[：]{style="font-family:宋体"}[显示指定出接口的信息。如果未指定本参数，将显示所有出接口的信息。]{style="font-family:宋体"}

[**[exclude]{lang="EN-US"}**]{#struct_0_81432_13537_x1951347664}[：显示不包含指定接口的信息。]{style="font-family:宋体"}

[**[include]{lang="EN-US"}**]{#struct_0_81432_13537_1059453152}[：]{style="font-family:宋体"}[显示包含指定接口的信息。]{style="font-family:宋体"}

[**[match]{lang="EN-US" style="color:black"}**]{#struct_0_81432_13537_433374903}[：]{style="font-family:
宋体;color:black"}[显示包含且仅包含指定接口的信息。]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1191694153}[：显示指定单板上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x368018972}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1831238004}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1480190295}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1325851759}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_x1480124759}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-956304130 .myid}
[]{#_Toc404799301}[]{#struct_0_81432_13537_1920722139}[]{#_Toc361304019}[]{#_Toc362011582}[]{#_Toc361304020}[]{#_Toc362011583}[]{#_Toc361304021}[]{#_Toc362011584}[]{#_Toc361304022}[]{#_Toc362011585}[]{#_Toc361304023}[]{#_Toc362011586}[]{#_Toc361304024}[]{#_Toc362011587}[]{#_Toc361304025}[]{#_Toc362011588}[]{#_Toc361304026}[]{#_Toc362011589}[]{#_Toc361304027}[]{#_Toc362011590}[]{#_Toc361304028}[]{#_Toc362011591}[]{#_Toc361304029}[]{#_Toc362011592}[]{#_Toc361304030}[]{#_Toc362011593}[]{#_Toc361304031}[]{#_Toc362011594}[]{#_Toc361304032}[]{#_Toc362011595}[]{#_Toc361304033}[]{#_Toc362011596}[]{#_Toc361304034}[]{#_Toc362011597}[]{#_Toc361304035}[]{#_Toc362011598}[]{#_Toc361304036}[]{#_Toc362011599}[]{#_Toc361304037}[]{#_Toc362011600}[]{#_Toc361304038}[]{#_Toc362011601}[]{#_Toc361304039}[]{#_Toc362011602}[]{#_Toc361304040}[]{#_Toc362011603}[]{#_Toc361304041}[]{#_Toc362011604}[]{#_Toc361304087}[]{#_Toc362011650}[]{#_Toc361304088}[]{#_Toc362011651}[]{#_Toc361304125}[]{#_Toc362011688}

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast record**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **record**]{lang="EN-US"}]{#struct_0_81432_13537_x1330701128}[命令用来显示组播表项的操作记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x910618585}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x1318357057}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **record** { **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_1465133532}[ \| { ]{lang="EN-US" style="font-size:
10.0pt"}[{ **all** \| **fail** } \[ { **group** \[ *group-address* \| *ipv6-group-address* \] \| **source** \[ *source-address* \| *ipv6-source-address* \] } \* \| **item**]{lang="EN-US"}[ ]{lang="EN-US"}*[item-list]{lang="DE"}*[ ]{lang="DE"}[\| **filter** { **exclude** \| **include** } { { **add-l2-ip** \| **add-l2-ip-port** \| **add-l2-ip-slot** \| **add-l2-mac** \| **add-l2-mac-port** \| **add-l2-mac-slot** \| **add-l3-ipm** \| **add-l3-oif** \| **add-l3-port** \| **add-l3-slot** \| **del-l2-ip** \| **del-l2-ip-port** \| **del-l2-ip-slot** \| **del-l2-mac** \| **del-l2-mac-port** \| **del-l2-mac-slot** \| **del-l3-ipm** \| **del-l3-oif** \| **del-l3-port** \| **del-l3-slot** \| **set-l3-iif** } \* \| **ipmc-type-all** } \] \[ **verbose** \] } } \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_1952887165}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **record** { **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_1181283282}[ \| { ]{lang="EN-US" style="font-size:
10.0pt"}[{ **all** \| **fail** } \[ { **group** \[ *group-address* \| *ipv6-group-address* \] \| **source** \[ *source-address* \| *ipv6-source-address* \] } \* \| **item**]{lang="EN-US"}[ ]{lang="EN-US"}*[item-list]{lang="DE"}*[ ]{lang="DE"}[\| **filter** { **exclude** \| **include** } { { **add-l2-ip** \| **add-l2-ip-port** \| **add-l2-ip-slot** \| **add-l2-mac** \| **add-l2-mac-port** \| **add-l2-mac-slot** \| **add-l3-ipm** \| **add-l3-oif** \| **add-l3-port** \| **add-l3-slot** \| **del-l2-ip** \| **del-l2-ip-port** \| **del-l2-ip-slot** \| **del-l2-mac** \| **del-l2-mac-port** \| **del-l2-mac-slot** \| **del-l3-ipm** \| **del-l3-oif** \| **del-l3-port** \| **del-l3-slot** \| **set-l3-iif** } \* \| **ipmc-type-all** } \] \[ **verbose** \] } } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_219022097}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast** **record** { **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_x381531163}[ \| { ]{lang="EN-US" style="font-size:
10.0pt"}[{ **all** \| **fail** } \[ { **group** \[ *group-address* \| *ipv6-group-address* \] \| **source** \[ *source-address* \| *ipv6-source-address* \] } \* \| **item**]{lang="EN-US"}[ ]{lang="EN-US"}*[item-list]{lang="DE"}*[ ]{lang="DE"}[\| **filter** { **exclude** \| **include** } { { **add-l2-ip** \| **add-l2-ip-port** \| **add-l2-ip-slot** \| **add-l2-mac** \| **add-l2-mac-port** \| **add-l2-mac-slot** \| **add-l3-ipm** \| **add-l3-oif** \| **add-l3-port** \| **add-l3-slot** \| **del-l2-ip** \| **del-l2-ip-port** \| **del-l2-ip-slot** \| **del-l2-mac** \| **del-l2-mac-port** \| **del-l2-mac-slot** \| **del-l3-ipm** \| **del-l3-oif** \| **del-l3-port** \| **del-l3-slot** \| **set-l3-iif** } \* \| **ipmc-type-all** } \] \[ **verbose** \] } } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_1920132312}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1711727368}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1669152234}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1916812515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x504685850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1298581329}

[**[statistics]{lang="EN-US"}**]{#struct_0_81432_13537_x1803496397}[：显示组播表项操作记录的统计信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_81432_13537_457799481}[：显示组播表项的所有操作记录。]{style="font-family:宋体"}

[**[fail]{lang="EN-US"}**]{#struct_0_81432_13537_1920197848}[：显示组播表项的失败操作记录。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_81432_13537_x486555862}[：组播组地址，显示指定组播组的记录。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_81432_13537_1920001240}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的记录。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_81432_13537_1804445823}[：组播源地址，显示包含指定组播源的记录。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x291018129}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，显示包含指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的记录。]{style="font-family:宋体"}

[**[item]{lang="EN-US"}**]{#struct_0_81432_13537_1256620139}[ ]{lang="EN-US"}*[item-list]{lang="DE"}*[：]{style="font-family:
宋体"}[记录列表，表示一条或多条记录。表示方式为]{style="font-family:宋体"}*[item-list =]{lang="DE"}*[ ]{lang="DE"}*[start-item]{lang="EN-US"}*[ \[ **to** ]{lang="DE"}*[end-item]{lang="EN-US"}*[ \]]{lang="DE"}[。其中，]{style="font-family:宋体"}*[start-item]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-item]{lang="EN-US"}*[的取值范围均为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[500000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[filter]{lang="EN-US"}**]{#struct_0_81432_13537_x1098111796}[：显示指定模式下的组播表项操作记录。]{style="font-family:宋体"}

[**[exclude]{lang="EN-US"}**]{#struct_0_81432_13537_x1929047507}[：显示排除满足指定条件的组播表项操作记录。]{style="font-family:宋体"}

[**[include]{lang="EN-US"}**]{#struct_0_81432_13537_352653461}[：]{style="font-family:宋体"}[显示包含满足指定条件的组播表项操作记录。]{style="font-family:宋体"}

[**[add-l2-ip]{lang="EN-US"}**]{#struct_0_81432_13537_x1699260075}[：表示添加二层]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的操作记录。]{style="font-family:宋体"}

[**[add-l2-ip-port]{lang="EN-US"}**]{#struct_0_81432_13537_1920066776}[：表示添加二层]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项端口的操作记录。]{style="font-family:宋体"}

[**[add-l2-ip-slot]{lang="EN-US"}**]{#struct_0_81432_13537_x517190993}[：表示添加二层]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项板信息的操作记录。]{style="font-family:宋体"}

[**[add-l2-mac]{lang="EN-US"}**]{#struct_0_81432_13537_1019793936}[：表示添加二层]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项的操作记录。]{style="font-family:宋体"}

[**[add-l2-mac-port]{lang="EN-US"}**]{#struct_0_81432_13537_x1776507146}[：表示添加二层]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项端口的操作记录。]{style="font-family:宋体"}

[**[add-l2-mac-slot]{lang="EN-US"}**]{#struct_0_81432_13537_850616054}[：表示添加二层]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项板信息的操作记录。]{style="font-family:宋体"}

[**[add-l3-ipm]{lang="EN-US"}**]{#struct_0_81432_13537_x1419166315}[：表示添加三层组播表项的操作记录。]{style="font-family:宋体"}

[**[add-l3-oif]{lang="EN-US"}**]{#struct_0_81432_13537_x1027085742}[：表示添加三层表项出接口的操作记录。]{style="font-family:宋体"}

[**[add-l3-port]{lang="EN-US"}**]{#struct_0_81432_13537_301254595}[：表示添加三层表项出端口的操作记录。]{style="font-family:宋体"}

[**[add-l3-slot]{lang="EN-US"}**]{#struct_0_81432_13537_1420516054}[：表示添加三层表项分布式转发的出接口板信息的操作记录。]{style="font-family:宋体"}

[**[del-l2-ip]{lang="EN-US"}**]{#struct_0_81432_13537_1920394456}[：表示删除二层]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项的操作记录。]{style="font-family:宋体"}

[**[del-l2-ip-port]{lang="EN-US"}**]{#struct_0_81432_13537_682320276}[：表示删除二层]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项端口的操作记录。]{style="font-family:宋体"}

[**[del-l2-ip-slot]{lang="EN-US"}**]{#struct_0_81432_13537_x70910127}[：表示删除二层]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项板信息的操作记录。]{style="font-family:宋体"}

[**[del-l2-mac]{lang="EN-US"}**]{#struct_0_81432_13537_x184916618}[：表示删除二层]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项的操作记录。]{style="font-family:宋体"}

[**[del-l2-mac-port]{lang="EN-US"}**]{#struct_0_81432_13537_x422171002}[：表示删除二层]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项端口的操作记录。]{style="font-family:宋体"}

[**[del-l2-mac-slot]{lang="EN-US"}**]{#struct_0_81432_13537_1885566320}[：表示删除二层]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项板信息的操作记录。]{style="font-family:宋体"}

[**[del-l3-ipm]{lang="EN-US"}**]{#struct_0_81432_13537_x1275568125}[：表示删除三层组播表项的操作记录。]{style="font-family:宋体"}

[**[del-l3-oif]{lang="EN-US"}**]{#struct_0_81432_13537_2063578111}[：表示删除三层表项出接口的操作记录。]{style="font-family:宋体"}

[**[del-l3-port]{lang="EN-US"}**]{#struct_0_81432_13537_1244504725}[：表示删除三层表项出端口的操作记录。]{style="font-family:宋体"}

[**[del-l3-slot]{lang="EN-US"}**]{#struct_0_81432_13537_1920459992}[：表示删除三层表项分布式转发的出接口板信息的操作记录。]{style="font-family:宋体"}

[**[set-l3-iif]{lang="EN-US"}**]{#struct_0_81432_13537_x947041066}[：表示设置三层表项入接口的操作记录。]{style="font-family:宋体"}

[**[ipmc-type-all]{lang="EN-US"}**]{#struct_0_81432_13537_x810121981}[：表示全部类型。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_81432_13537_x670016137}[：]{style="font-family:宋体"}[显示详细信息。如果记录的出接口和出端口显示不全时，需要指定本参数。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_1013038399}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数[，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x561272332}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_494360824}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1890711082}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_204395629}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_1248758601}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1432915454 .myid}
[]{#_Toc404799302}[]{#struct_0_81432_13537_x2013435523}[]{#_Toc345417462}[]{#_Toc361304127}[]{#_Toc362011690}[]{#_Toc361304128}[]{#_Toc362011691}[]{#_Toc361304129}[]{#_Toc362011692}[]{#_Toc361304130}[]{#_Toc362011693}[]{#_Toc361304131}[]{#_Toc362011694}[]{#_Toc361304132}[]{#_Toc362011695}[]{#_Toc361304133}[]{#_Toc362011696}[]{#_Toc361304134}[]{#_Toc362011697}[]{#_Toc361304135}[]{#_Toc362011698}[]{#_Toc361304136}[]{#_Toc362011699}[]{#_Toc361304137}[]{#_Toc362011700}[]{#_Toc361304138}[]{#_Toc362011701}[]{#_Toc361304139}[]{#_Toc362011702}[]{#_Toc361304140}[]{#_Toc362011703}[]{#_Toc361304141}[]{#_Toc362011704}[]{#_Toc361304142}[]{#_Toc362011705}[]{#_Toc361304143}[]{#_Toc362011706}[]{#_Toc361304144}[]{#_Toc362011707}[]{#_Toc361304145}[]{#_Toc362011708}[]{#_Toc361304146}[]{#_Toc362011709}[]{#_Toc361304147}[]{#_Toc362011710}[]{#_Toc361304148}[]{#_Toc362011711}[]{#_Toc361304149}[]{#_Toc362011712}[]{#_Toc361304150}[]{#_Toc362011713}[]{#_Toc361304151}[]{#_Toc362011714}[]{#_Toc361304152}[]{#_Toc362011715}[]{#_Toc361304153}[]{#_Toc362011716}[]{#_Toc361304154}[]{#_Toc362011717}[]{#_Toc361304155}[]{#_Toc362011718}[]{#_Toc361304156}[]{#_Toc362011719}[]{#_Toc361304157}[]{#_Toc362011720}[]{#_Toc361304158}[]{#_Toc362011721}[]{#_Toc361304159}[]{#_Toc362011722}[]{#_Toc361304160}[]{#_Toc362011723}[]{#_Toc361304161}[]{#_Toc362011724}[]{#_Toc361304162}[]{#_Toc362011725}[]{#_Toc361304163}[]{#_Toc362011726}[]{#_Toc361304164}[]{#_Toc362011727}[]{#_Toc361304165}[]{#_Toc362011728}[]{#_Toc361304166}[]{#_Toc362011729}[]{#_Toc361304167}[]{#_Toc362011730}[]{#_Toc361304168}[]{#_Toc362011731}[]{#_Toc361304169}[]{#_Toc362011732}[]{#_Toc361304170}[]{#_Toc362011733}[]{#_Toc361304171}[]{#_Toc362011734}[]{#_Toc361304172}[]{#_Toc362011735}[]{#_Toc361304173}[]{#_Toc362011736}[]{#_Toc361304174}[]{#_Toc362011737}[]{#_Toc361304175}[]{#_Toc362011738}[]{#_Toc361304254}[]{#_Toc362011817}[]{#_Toc361304255}[]{#_Toc362011818}[]{#_Toc361304256}[]{#_Toc362011819}[]{#_Toc361304257}[]{#_Toc362011820}[]{#_Toc361304258}[]{#_Toc362011821}[]{#_Toc361304259}[]{#_Toc362011822}[]{#_Toc361304260}[]{#_Toc362011823}[]{#_Toc361304261}[]{#_Toc362011824}[]{#_Toc361304262}[]{#_Toc362011825}[]{#_Toc361304278}[]{#_Toc362011841}

**IP组播 \-- IP组播Probe命令 \-- display system internal multicast-vlan forwarding-table verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast-vlan** **forwarding-table** **verbose**]{lang="EN-US"}]{#struct_0_81432_13537_x1257825587}[命令用来显示组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1113100235}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_1218512133}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast-vlan** **forwarding-table** **verbose** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **cpu** *cpu-number* \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_1920066774}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x517322065}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast-vlan** **forwarding-table** **verbose** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_692447519}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1562920945}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **multicast-vlan** **forwarding-table** **verbose** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_81432_13537_1571456613}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x986255323}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x2016113843}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x367372035}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_1003358748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_1920394454}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_682189204}

[*[group-address]{lang="EN-US"}*]{#struct_0_81432_13537_1637089429}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_81432_13537_x1526184615}[：指定组播组的掩码长度或掩码。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x1367538211}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_81432_13537_346279418}[：指定组播源的掩码长度或掩码。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x1334975369}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x201722639}[：显示指定成员设备上的信息，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_944699518}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1249086280}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_2131428590}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_1249151816}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[subvlan]{lang="EN-US" style="color:black"}**[ *vlan-id*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1920459990}[：显示指定子]{style="font-family:宋体;
color:black"}[VLAN]{lang="EN-US" style="color:black"}[的信息。如果未指定本参数，将显示所有子]{style="font-family:宋体;color:black"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_81432_13537_x947172138}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}
:::

::: {#-1158447436 .myid}
[]{#_Toc347301895}[]{#_Toc342987816}[]{#_Toc404799303}[]{#struct_0_81432_13537_x1273739062}[]{#_Toc347301904}[]{#_Toc361304280}[]{#_Toc362011843}[]{#_Toc361304281}[]{#_Toc362011844}[]{#_Toc361304282}[]{#_Toc362011845}[]{#_Toc361304283}[]{#_Toc362011846}[]{#_Toc361304284}[]{#_Toc362011847}[]{#_Toc361304285}[]{#_Toc362011848}[]{#_Toc361304286}[]{#_Toc362011849}[]{#_Toc361304287}[]{#_Toc362011850}[]{#_Toc361304288}[]{#_Toc362011851}[]{#_Toc361304289}[]{#_Toc362011852}[]{#_Toc361304290}[]{#_Toc362011853}[]{#_Toc361304291}[]{#_Toc362011854}[]{#_Toc361304292}[]{#_Toc362011855}[]{#_Toc361304293}[]{#_Toc362011856}[]{#_Toc361304294}[]{#_Toc362011857}[]{#_Toc361304295}[]{#_Toc362011858}[]{#_Toc361304296}[]{#_Toc362011859}[]{#_Toc361304297}[]{#_Toc362011860}[]{#_Toc361304298}[]{#_Toc362011861}[]{#_Toc361304299}[]{#_Toc362011862}[]{#_Toc361304336}[]{#_Toc362011899}

**IP组播 \-- IP组播Probe命令 \-- display system internal pim interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_x1515751682}**[system]{lang="EN-US"}**[ **internal** **pim** **interface**]{lang="EN-US"}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[进程中]{style="font-family:宋体"}[路由管理]{style="font-family:宋体"}[LIB]{lang="EN-US"}[所维护的接口信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1103844212}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_81432_13537_1920197847}**[system]{lang="EN-US"}**[ **internal** **pim** ]{lang="EN-US"}[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[interface]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ *interface-type* *interface-number* \| *ip-address* { *mask-length* \| *mask* } \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x485703894}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1215639429}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_699513762}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_209235808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1080318279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x952965665}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_81432_13537_x398545951}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_81432_13537_x754875428}[：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_81432_13537_1920001239}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的信息。]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[为保留地址，用户不感知。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_81432_13537_1805035644}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_81432_13537_x1116574987}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[掩码。]{style="font-family:宋体"}
:::

::: {#-2134943903 .myid}
[]{#_Toc404799304}[]{#struct_0_81432_13537_x808882113}[]{#_Toc347301905}[]{#_Toc361304338}[]{#_Toc362011901}[]{#_Toc361304339}[]{#_Toc362011902}[]{#_Toc361304340}[]{#_Toc362011903}[]{#_Toc361304341}[]{#_Toc362011904}[]{#_Toc361304342}[]{#_Toc362011905}[]{#_Toc361304343}[]{#_Toc362011906}[]{#_Toc361304344}[]{#_Toc362011907}[]{#_Toc361304345}[]{#_Toc362011908}[]{#_Toc361304346}[]{#_Toc362011909}[]{#_Toc361304347}[]{#_Toc362011910}[]{#_Toc361304348}[]{#_Toc362011911}[]{#_Toc361304349}[]{#_Toc362011912}[]{#_Toc361304350}[]{#_Toc362011913}[]{#_Toc361304351}[]{#_Toc362011914}[]{#_Toc361304352}[]{#_Toc362011915}[]{#_Toc361304353}[]{#_Toc362011916}[]{#_Toc361304354}[]{#_Toc362011917}[]{#_Toc361304355}[]{#_Toc362011918}[]{#_Toc361304356}[]{#_Toc362011919}[]{#_Toc361304357}[]{#_Toc362011920}[]{#_Toc361304358}[]{#_Toc362011921}[]{#_Toc361304359}[]{#_Toc362011922}[]{#_Toc361304420}[]{#_Toc362011983}

**IP组播 \-- IP组播Probe命令 \-- display system internal pim rp**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **pim** **rp**]{lang="EN-US"}]{#struct_0_81432_13537_x1750595409}[命令用来显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x956547229}

[**[display]{lang="EN-US"}**[ **system** **internal** **pim** \[ **vpn-instance** *vpn-instance-name* \] **rp**]{lang="EN-US"}]{#struct_0_81432_13537_x264125909}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_572942280}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x890631019}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_1081913803}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1467285072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1342750337}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x808816577}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_81432_13537_x200484071}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网实例的信息。]{style="font-family:宋体"}
:::

::: {#1605149348 .myid}
[]{#_Toc404799305}[]{#struct_0_81432_13537_x593372687}[]{#_Toc347301906}[]{#_Toc342902033}[]{#_Toc361304422}[]{#_Toc362011985}[]{#_Toc361304423}[]{#_Toc362011986}[]{#_Toc361304424}[]{#_Toc362011987}[]{#_Toc361304425}[]{#_Toc362011988}[]{#_Toc361304426}[]{#_Toc362011989}[]{#_Toc361304427}[]{#_Toc362011990}[]{#_Toc361304428}[]{#_Toc362011991}[]{#_Toc361304429}[]{#_Toc362011992}[]{#_Toc361304430}[]{#_Toc362011993}[]{#_Toc361304431}[]{#_Toc362011994}[]{#_Toc361304432}[]{#_Toc362011995}[]{#_Toc361304433}[]{#_Toc362011996}[]{#_Toc361304434}[]{#_Toc362011997}[]{#_Toc361304435}[]{#_Toc362011998}[]{#_Toc361304469}[]{#_Toc362012032}

**IP组播 \-- IP组播Probe命令 \-- display system internal pim thread**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **pim** **thread**]{lang="EN-US"}]{#struct_0_81432_13537_x1199489883}[命令用来显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[线程的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1703775528}

[**[display]{lang="EN-US"}**[ **system** **internal** **pim** **thread**]{lang="EN-US"}]{#struct_0_81432_13537_x1014090989}[ ]{lang="EN-US"}[{]{lang="EN-US"}[ **event** \| **main** \| **route** ]{lang="EN-US"}[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x622011152}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x217811701}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x808161217}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x608082565}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_815007557}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_788920214}

[**[event]{lang="EN-US"}**]{#struct_0_81432_13537_1191343224}[：显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[事件线程的统计信息。]{style="font-family:宋体"}

[**[main]{lang="EN-US"}**]{#struct_0_81432_13537_368704257}[：显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[主线程的统计信息。]{style="font-family:宋体"}

[**[route]{lang="EN-US"}**]{#struct_0_81432_13537_x1092713036}[：显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由线程的统计信息。]{style="font-family:宋体"}
:::

::::: {#-1610987269 .myid}
[]{#_Toc404799306}[]{#struct_0_81432_13537_34703712}[]{#_Toc375731093}[]{#_Toc363827569}[]{#_Toc363576386}

**IP组播 \-- IP组播Probe命令 \-- igmp user-authorization record limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x1144633542}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_x1860907830}
:::

[ ]{lang="EN-US"}

[**[igmp]{lang="EN-US"}**[ **user-authorization** **record** **limit**]{lang="EN-US"}]{#struct_0_81432_13537_684372076}[命令用来配置按用户记录的认证模块通知给]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[进程消息数的用户上限。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1520360120}

[**[igmp]{lang="EN-US"}**[ **user-authorization** **record** **limit** *limit-value*]{lang="EN-US"}]{#struct_0_81432_13537_x661875757}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_81432_13537_1307732171}

[[按用户记录的]{style="font-family:宋体"}]{#struct_0_81432_13537_1472150106}[认证模块通知给]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[进程]{style="font-family:宋体"}[消息数的用户上限为]{style="font-family:宋体"}[512]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2055981848}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1640279575}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1163436659}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_125715376}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_34638176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1552970754}

[*[limit-value]{lang="EN-US"}*]{#struct_0_81432_13537_1929585644}[：表示用户上限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[524288]{lang="EN-US"}[。]{style="font-family:宋体"}
:::::

::::: {#-980575742 .myid}
[]{#_Toc404799307}[]{#struct_0_81432_13537_1681839464}[]{#_Toc375731094}[]{#_Toc363827570}

**IP组播 \-- IP组播Probe命令 \-- mld user-authorization record limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x1144502470}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_446277426}
:::

[ ]{lang="EN-US"}

[**[mld]{lang="EN-US"}**[ **user-authorization** **record** **limit**]{lang="EN-US"}]{#struct_0_81432_13537_x319863246}[命令用来配置按用户记录的认证模块通知给]{style="font-family:宋体"}[MLD]{lang="EN-US"}[进程消息数的用户上限。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x913476276}

[**[mld]{lang="EN-US"}**[ **user-authorization** **record** **limit** *limit-value*]{lang="EN-US"}]{#struct_0_81432_13537_x1419133992}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2014133144}

[[按用户记录的认证模块通知给]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_81432_13537_318237419}[进程消息数的用户上限为]{style="font-family:宋体"}[512]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1868545788}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x859192389}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x221181752}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x195791507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_35096928}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_1588472503}

[*[limit-value]{lang="EN-US"}*]{#struct_0_81432_13537_x962425417}[：表示用户上限，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[524288]{lang="EN-US"}[。]{style="font-family:宋体"}
:::::

::: {#2140172749 .myid}
[]{#_Toc404799308}[]{#struct_0_81432_13537_x1197434107}[]{#_Toc361304471}[]{#_Toc362012034}[]{#_Toc361304472}[]{#_Toc362012035}[]{#_Toc361304473}[]{#_Toc362012036}[]{#_Toc361304474}[]{#_Toc362012037}[]{#_Toc361304475}[]{#_Toc362012038}[]{#_Toc361304476}[]{#_Toc362012039}[]{#_Toc361304477}[]{#_Toc362012040}[]{#_Toc361304478}[]{#_Toc362012041}[]{#_Toc361304479}[]{#_Toc362012042}[]{#_Toc361304480}[]{#_Toc362012043}[]{#_Toc361304481}[]{#_Toc362012044}[]{#_Toc361304482}[]{#_Toc362012045}[]{#_Toc361304483}[]{#_Toc362012046}[]{#_Toc361304484}[]{#_Toc362012047}[]{#_Toc361304485}[]{#_Toc362012048}[]{#_Toc361304486}[]{#_Toc362012049}[]{#_Toc361304487}[]{#_Toc362012050}[]{#_Toc361304488}[]{#_Toc362012051}[]{#_Toc361304549}[]{#_Toc362012112}[]{#_Toc361304550}[]{#_Toc362012113}[]{#_Toc361304551}[]{#_Toc362012114}[]{#_Toc361304552}[]{#_Toc362012115}[]{#_Toc361304553}[]{#_Toc362012116}[]{#_Toc361304554}[]{#_Toc362012117}[]{#_Toc361304555}[]{#_Toc362012118}[]{#_Toc361304556}[]{#_Toc362012119}[]{#_Toc361304557}[]{#_Toc362012120}[]{#_Toc361304558}[]{#_Toc362012121}[]{#_Toc361304559}[]{#_Toc362012122}[]{#_Toc361304560}[]{#_Toc362012123}[]{#_Toc361304561}[]{#_Toc362012124}[]{#_Toc361304562}[]{#_Toc362012125}[]{#_Toc361304563}[]{#_Toc362012126}[]{#_Toc361304564}[]{#_Toc362012127}[]{#_Toc361304595}[]{#_Toc362012158}[]{#_Toc361304596}[]{#_Toc362012159}[]{#_Toc361304597}[]{#_Toc362012160}[]{#_Toc361304598}[]{#_Toc362012161}[]{#_Toc361304599}[]{#_Toc362012162}[]{#_Toc361304600}[]{#_Toc362012163}[]{#_Toc361304601}[]{#_Toc362012164}[]{#_Toc361304602}[]{#_Toc362012165}[]{#_Toc361304603}[]{#_Toc362012166}[]{#_Toc361304604}[]{#_Toc362012167}[]{#_Toc361304605}[]{#_Toc362012168}[]{#_Toc361304606}[]{#_Toc362012169}[]{#_Toc361304607}[]{#_Toc362012170}[]{#_Toc361304608}[]{#_Toc362012171}[]{#_Toc361304609}[]{#_Toc362012172}[]{#_Toc361304610}[]{#_Toc362012173}[]{#_Toc361304662}[]{#_Toc362012225}

**IP组播 \-- IP组播Probe命令 \-- multicast record limit**

------------------------------------------------------------------------

[**[multicast]{lang="EN-US"}**[ **record** **limit**]{lang="EN-US"}]{#struct_0_81432_13537_1038953148}[命令用来配置组播表项操作记录的最大数目。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **multicast** **record** **limit**]{lang="EN-US"}]{#struct_0_81432_13537_x1655994221}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1313585527}

[**[multicast]{lang="EN-US"}**[ **record** \[ **fail** \] **limit** *limit-value*]{lang="EN-US"}]{#struct_0_81432_13537_x536321455}

[**[undo]{lang="EN-US"}**[ **multicast** **record** \[ **fail** \] **limit**]{lang="EN-US"}]{#struct_0_81432_13537_x808882114}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1750136657}

[[组播表项操作记录的最大数目为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_81432_13537_1984310969}[，即不记录组播表项的操作信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x653166701}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x319408541}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x155617415}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_139838093}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x380741421}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_x665798230}

[**[fail]{lang="EN-US"}**]{#struct_0_81432_13537_x808816578}[：表示组播表项的失败操作记录。]{style="font-family:宋体"}

[*[limit-value]{lang="EN-US"}*]{#struct_0_81432_13537_x199894247}[：表示操作记录的最大数目，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[500000]{lang="EN-US"}[。]{style="font-family:宋体"}
:::

::::: {#615633661 .myid}
[]{#_Toc404799309}[]{#struct_0_81432_13537_1725460719}

**IP组播 \-- IP组播Probe命令 \-- reset system internal igmp user-authorization record**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x1357565092}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_1001533814}
:::

[ ]{lang="EN-US"}

[**[reset]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_269201069}[命令用来清除按用户记录的认证模块通知给]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1525986254}

[**[reset]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_1724870892}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_1818309344}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x2055654015}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x83181689}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x931202584}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x394409185}
:::::

::::: {#1845492813 .myid}
[]{#_Toc404799310}[]{#struct_0_81432_13537_35031392}[]{#_Toc375731096}[]{#_Toc363827574}[]{#_Toc363576384}

**IP组播 \-- IP组播Probe命令 \-- reset system internal igmp user-authorization statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x1144436931}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_461652329}
:::

[ ]{lang="EN-US"}

[**[reset]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_x1503253153}[命令用来清除按认证类型记录的认证模块通知给]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_374093742}

[**[reset]{lang="EN-US"}**[ **system** **internal** **igmp** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_1013052227}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_254942193}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1794134928}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x493789894}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x559280930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_34572639}
:::::

::: {#1326185643 .myid}
[]{#_Toc404799311}[]{#struct_0_81432_13537_1490599608}[]{#_Toc347301859}[]{#_Toc391026164}[]{#_Toc391026165}[]{#_Toc391026166}[]{#_Toc391026167}[]{#_Toc391026168}[]{#_Toc391026169}[]{#_Toc391026170}[]{#_Toc391026171}[]{#_Toc391026172}[]{#_Toc391026173}[]{#_Toc391026174}[]{#_Toc391026175}[]{#_Toc361304664}[]{#_Toc362012227}[]{#_Toc361304665}[]{#_Toc362012228}[]{#_Toc361304666}[]{#_Toc362012229}[]{#_Toc361304667}[]{#_Toc362012230}[]{#_Toc361304668}[]{#_Toc362012231}

**IP组播 \-- IP组播Probe命令 \-- reset system internal ipv6 multicast forwarding-table dummy**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal ipv6** **multicast** **forwarding-table** **dummy**]{lang="EN-US"}]{#struct_0_81432_13537_x1223672169}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播临时转发表中的表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_648471841}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x808488898}

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** { { *ipv6-group-address* \[ *prefix-length* \] \| *ipv6-source-address* \[ *prefix-length* \] } \* \| **all** } \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1041197503}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x1444898811}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** { { *ipv6-group-address* \[ *prefix-length* \] \| *ipv6-source-address* \[ *prefix-length* \] } \* \| **all** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1698690091}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_x1189531977}[模式：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal ipv6** **multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** { { *ipv6-group-address* \[ *prefix-length* \] \| *ipv6-source-address* \[ *prefix-length* \] } \* \| **all** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_260516614}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x820117447}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_475368502}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x137705014}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x808423362}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_574651597}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_262526314}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_81432_13537_1626440937}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的表项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的表项。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_81432_13537_365638494}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的表项，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均表示]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将清除所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的表项。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x967751235}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的表项。如果未指定本参数，将清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的表项。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_81432_13537_x1472686587}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址的前缀长度。对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，其取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[；对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_81432_13537_982878140}[：清除所有表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_81432_13537_x808619970}[：清除指定单板上的表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将清除主控板上的表项。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1249020742}[：清除指定成员设备上的表项，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将清除主设备上的表项。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x1784118301}[：]{style="font-family:宋体;
color:black"}[清除指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的表项，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将清除主设备上的表项。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x279049448}[：清除指定成员设备上指定单板的表项，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_944765054}[：清除指定单板上的表项，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_1249151814}[：清除指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::::: {#1890819358 .myid}
[]{#_Toc404799312}[]{#struct_0_81432_13537_1724674284}

**IP组播 \-- IP组播Probe命令 \-- reset system internal mld user-authorization record**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_639328569}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_x324364096}
:::

[ ]{lang="EN-US"}

[**[reset]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_1329082004}[命令用来清除按用户记录的认证模块通知给]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x2144068330}

[**[reset]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **record**]{lang="EN-US"}]{#struct_0_81432_13537_1724477676}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_1000849087}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x1764410275}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_79366369}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_532487004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x645717648}
:::::

::::: {#859524320 .myid}
[]{#_Toc404799313}[]{#struct_0_81432_13537_34441567}[]{#_Toc375731099}[]{#_Toc363827576}

**IP组播 \-- IP组播Probe命令 \-- reset system internal mld user-authorization statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP组播Probe命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_81432_13537_x1144699075}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_81432_13537_x1144633539}
:::

[ ]{lang="EN-US"}

[**[reset]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_x1752729546}[命令用来清除按认证类型记录的认证模块通知给]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[进程的消息数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1732011112}

[**[reset]{lang="EN-US"}**[ **system** **internal** **mld** **user-authorization** **statistics**]{lang="EN-US"}]{#struct_0_81432_13537_x168884164}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_151450674}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_384495027}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x464766412}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1179788022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x102206768}
:::::

::: {#-690154841 .myid}
[]{#_Toc404799314}[]{#struct_0_81432_13537_x1132947713}[]{#_Toc347301897}[]{#_Toc342987828}[]{#_Toc391026179}[]{#_Toc391026180}[]{#_Toc391026181}[]{#_Toc391026182}[]{#_Toc391026183}[]{#_Toc391026184}[]{#_Toc391026185}[]{#_Toc391026186}[]{#_Toc391026187}[]{#_Toc391026188}[]{#_Toc391026189}[]{#_Toc391026190}[]{#_Toc361304670}[]{#_Toc362012233}[]{#_Toc361304671}[]{#_Toc362012234}[]{#_Toc361304672}[]{#_Toc362012235}[]{#_Toc361304673}[]{#_Toc362012236}[]{#_Toc361304674}[]{#_Toc362012237}

**IP组播 \-- IP组播Probe命令 \-- reset system internal multicast forwarding-table dummy**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal multicast** **forwarding-table** **dummy**]{lang="EN-US"}]{#struct_0_81432_13537_893145558}[命令用来清除组播临时转发表中的表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_1970333489}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_81432_13537_x808554434}

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** { { *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] } \* \| **all** } \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_81432_13537_x1384660050}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_81432_13537_x1746098706}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** { { *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] } \* \| **all** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_72588214}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_81432_13537_1990041595}[模式：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}**[system]{lang="EN-US"}**[ **internal multicast** \[ **vpn-instance** *vpn-instance-name* \] **forwarding-table** **dummy** { { *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] } \* \| **all** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_81432_13537_x1858214903}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1805249077}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_1995174063}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_x1346753796}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x808226754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_x593176079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_81432_13537_743116500}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_81432_13537_216380527}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的表项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的表项。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_81432_13537_x176386735}[：清除指定组播源的表项。如果未指定本参数，将清除所有组播源的表项。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_81432_13537_x1127760445}[：清除指定组播组的表项，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将清除所有组播组的表项。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_81432_13537_413138506}[：指定组播源或组播组地址的掩码长度。对于组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；对于组播组地址，其取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_81432_13537_270448876}[：指定组播源或组播组地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US" style="color:black"}**]{#struct_0_81432_13537_x1851474746}[：清除所有表项。]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x608410245}[：清除指定单板上的表项，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将清除主控板上的表项。（分布式设备－独立运行模式）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_1249020741}[：清除指定成员设备上的表项，]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将清除主设备上的表项。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_81432_13537_x265022991}[：]{style="font-family:宋体;
color:black"}[清除指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的表项，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将清除主设备上的表项。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_43184485}[：清除指定成员设备上指定单板的表项，]{style="font-family:宋体;
color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_81432_13537_x1831106932}[：清除指定单板上的表项，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将清除全局主用主控板上的表项。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_81432_13537_1249151813}[：清除指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体;
color:black"}**[slot]{lang="EN-US" style="color:black"}**[支持多]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:
black"}[时，才能配置该参数。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1340619163 .myid}
[]{#_Toc404799315}[]{#struct_0_81432_13537_x756230939}[]{#_Toc347301898}[]{#_Toc361304676}[]{#_Toc362012239}[]{#_Toc361304677}[]{#_Toc362012240}[]{#_Toc361304678}[]{#_Toc362012241}[]{#_Toc361304679}[]{#_Toc362012242}[]{#_Toc361304680}[]{#_Toc362012243}

**IP组播 \-- IP组播Probe命令 \-- reset system internal multicast record**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **system** **internal multicast** **record**]{lang="EN-US"}]{#struct_0_81432_13537_1158279653}[命令用来清除组播表项的操作记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_81432_13537_x808751045}

[**[reset]{lang="EN-US"}**[ **system** **internal multicast** **record**]{lang="EN-US"}]{#struct_0_81432_13537_x216635876}

[[【视图】]{style="font-family:黑体"}]{#struct_0_81432_13537_x511364943}

[[Probe]{lang="EN-US"}]{#struct_0_81432_13537_x481975101}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_81432_13537_930516054}

[[network-admin]{lang="EN-US"}]{#struct_0_81432_13537_x1151188521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_81432_13537_231728768}

[ ]{lang="EN-US"}
:::
