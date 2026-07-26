::: {#588496648 .myid}
[]{#_Toc404799508}[]{#struct_0_95746_15116_x849445682}[]{#_Toc343265990}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib prefix**

------------------------------------------------------------------------

[**[display system internal fib prefix]{lang="EN-US"}**]{#struct_0_95746_15116_1585034117}[命令用来显示]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_x1196467852}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_78094500}

[**[display system internal fib prefix ]{lang="EN-US"}**[\[ **topology** *topo-name* \| **vpn-instance** [vpn-instance-name ]{.commandparameterChar}\]]{lang="EN-US"}]{#struct_0_95746_15116_1252528995}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_1488963919}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib prefix ]{lang="EN-US"}]{#struct_0_95746_15116_x27393615}[\[ ]{lang="EN-US" style="font-weight:normal"}[topology ]{lang="EN-US"}*[topo-name]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ vpn-instance ]{lang="EN-US"}[[vpn-instance-name]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-weight:normal"}[ slot ]{lang="EN-US"}[[slot-number ]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\[]{lang="EN-US" style="font-weight:normal"}[ cpu ]{lang="EN-US"}*[cpu-number]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_1973665411}[模式：]{style="font-family:宋体"}

[**[display system internal fib prefix ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[topology]{lang="EN-US"}**[ *topo-name* \| **vpn-instance** *vpn-instance-name* \] **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_1606128277}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_572115111}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_x305490090}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_400028009}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_x565899486}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_x1196533388}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_x2008982764}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_95746_15116_x485907262}[：显示指定拓扑的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；取值为]{style="font-family:宋体"}**[base]{lang="EN-US"}**[时表示公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_95746_15116_774704256}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则显示公网的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x143703781}[：显示指定单板上的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x658268962}[：显示指定成员设备上的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_2626033}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_1109169848}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1429110381}[：显示指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_88976671}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1541922676 .myid}
[]{#_Toc404799509}[]{#struct_0_95746_15116_1831605352}[]{#_Toc343265991}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib prefix ip**

------------------------------------------------------------------------

[**[display system internal fib]{lang="EN-US"}**[ **prefix** *ip*]{lang="EN-US"}]{#struct_0_95746_15116_x960311859}[命令用来显示]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_95262083}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_x1659647515}

[[display system internal fib prefix]{lang="EN-US"}]{#struct_0_95746_15116_x1196861071}[ \[ ]{lang="EN-US" style="font-weight:normal"}[vpn-instance]{lang="EN-US"}[ ]{lang="EN-US" style="font-weight:normal"}[[vpn-instance-name]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\] ]{lang="EN-US" style="font-weight:normal"}[[ip ]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\[*mask* \| *mask-length*]{lang="EN-US" style="font-weight:normal"}[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_1368140801}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib prefix]{lang="EN-US"}]{#struct_0_95746_15116_1194546093}[ \[ ]{lang="EN-US" style="font-weight:normal"}[vpn-instance]{lang="EN-US"}[ ]{lang="EN-US" style="font-weight:normal"}[[vpn-instance-name]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \]]{lang="EN-US" style="font-weight:normal"}[ ]{lang="EN-US"}[[ip ]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\[]{lang="EN-US" style="font-weight:normal"}[ ]{lang="EN-US"}*[mask]{lang="EN-US" style="font-weight:normal"}*[ \| *mask-length*]{lang="EN-US" style="font-weight:normal"}[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-weight:normal"}[ ]{lang="EN-US"}[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \[]{lang="EN-US" style="font-weight:normal"}[ cpu ]{lang="EN-US"}*[cpu-number]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_497631561}[模式：]{style="font-family:宋体"}

[**[display system internal fib prefix ]{lang="EN-US"}**[\[ **vpn-instance**]{lang="EN-US"}**[ ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}**[ ]{lang="EN-US"}**[[ip]{lang="EN-US"}]{.commandparameterChar}**[ ]{lang="EN-US"}**[\[ *mask* \| *mask-length* \]]{lang="EN-US"}[  **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number]{.commandparameterChar} \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_1745255861}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_x1567562168}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_x1658868145}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_x1196402319}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_1613545696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_1370186329}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_692056200}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_95746_15116_619511500}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则显示公网的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}

[*[ip]{lang="EN-US"}*]{#struct_0_95746_15116_x281044840}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_95746_15116_x857336210}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_95746_15116_x1592052089}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1734085874}[：显示指定单板上的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1196467855}[：显示指定成员设备上的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_1165425447}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x325190027}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_1245813323}[：显示指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_88976673}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1308398772 .myid}
[]{#_Toc404799510}[]{#struct_0_95746_15116_1634654323}[]{#_Toc343265992}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib prefix entry-status**

------------------------------------------------------------------------

[**[display system internal fib prefix entry-status]{lang="EN-US"}**]{#struct_0_95746_15116_220807786}[命令用来显示下驱动失败或者待老化的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_1833989440}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_432751669}

[[display system internal fib]{lang="EN-US"}]{#struct_0_95746_15116_x1908066879}[ ]{lang="EN-US" style="font-weight:normal"}[prefix]{lang="EN-US"}[ \[ ]{lang="EN-US" style="font-weight:normal"}[vpn-instance]{lang="EN-US"}[ ]{lang="EN-US" style="font-weight:normal"}[[vpn-instance-name]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\]]{lang="EN-US" style="font-weight:normal"}[ entry-status]{lang="EN-US"}[[ status]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_x1196598926}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib prefix]{lang="EN-US"}]{#struct_0_95746_15116_x1582293794}[ \[ ]{lang="EN-US" style="font-weight:normal"}[vpn-instance]{lang="EN-US"}[ ]{lang="EN-US" style="font-weight:normal"}[[vpn-instance-name]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \]]{lang="EN-US" style="font-weight:normal"}[ entry-status]{lang="EN-US"}[[ status]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \[]{lang="EN-US" style="font-weight:normal"}[ cpu ]{lang="EN-US"}*[cpu-number]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_148922778}[模式：]{style="font-family:宋体"}

[**[display system internal fib]{lang="EN-US"}**[ **prefix** \[ **vpn-instance** [vpn-instance-name]{.commandparameterChar}\] **entry-status[ ]{.commandparameterChar}**[status]{.commandparameterChar} **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_776983933}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_561711887}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_x492726058}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_159059835}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_x1196140174}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_559716807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_x236543314}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_95746_15116_x2012195056}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则显示公网的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[entry-status]{lang="EN-US"}***[ status]{lang="EN-US"}*]{#struct_0_95746_15116_x1452781342}[：用于匹配]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项；取值范围为]{style="font-family:宋体"}[\<A,F\>]{lang="EN-US"}[，"]{style="font-family:宋体"}[A]{lang="EN-US"}["表示需要被老化的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息，"]{style="font-family:宋体"}[F]{lang="EN-US"}["表示下刷驱动失败的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1196205710}[：显示指定单板上的]{style="font-family:宋体;color:black"}[下驱动失败或者待老化的]{style="font-family:
宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:
宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x521361551}[：显示指定成员设备上的]{style="font-family:宋体;color:black"}[下驱动失败或者待老化的]{style="font-family:
宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:
宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1966742435}[：显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;color:black"}[下驱动失败或者待老化的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x900434516}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定成员设备上指定单板的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1132362476}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定单板的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_88976668}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#243731028 .myid}
[]{#_Toc404799511}[]{#struct_0_95746_15116_1945251714}[]{#_Toc343265993}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib running-status**

------------------------------------------------------------------------

[**[display system internal fib running-status]{lang="EN-US"}**]{#struct_0_95746_15116_2027600050}[命令用来显示]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[全局信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_725846450}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_693450811}

[[display system internal fib]{lang="EN-US"}]{#struct_0_95746_15116_x299525208}[ ]{lang="EN-US" style="font-weight:normal"}[running-status]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_1043301335}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib]{lang="EN-US"}]{#struct_0_95746_15116_x50218857}[ ]{lang="EN-US" style="font-weight:normal"}[running-status]{lang="EN-US"}[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \[]{lang="EN-US" style="font-weight:normal"}[ cpu ]{lang="EN-US"}*[cpu-number]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_1136825779}[模式：]{style="font-family:宋体"}

[**[display system internal fib ]{lang="EN-US"}**[ ]{lang="EN-US"}**[running-status]{lang="EN-US"}**[ **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_x495203055}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_454805421}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_1386437733}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_725780914}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_1218985172}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_x359570990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_1215427187}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1965000380}[：显示指定单板上的]{style="font-family:宋体;color:black"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[全局信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_725715378}[：显示指定成员设备上的]{style="font-family:宋体;color:black"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[全局信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1516403741}[：显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;color:black"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[全局信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1453544029}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[全局信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_935016824}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[全局信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_88976678}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[全局信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1623952302 .myid}
[]{#_Toc404799512}[]{#struct_0_95746_15116_726174131}[]{#_Toc343265994}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib statistics**

------------------------------------------------------------------------

[**[display system internal fib statistics]{lang="EN-US"}**]{#struct_0_95746_15116_9612829}[命令用来显示]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项操作的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_1947149973}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_x1262854867}

[[display system internal fib]{lang="EN-US"}]{#struct_0_95746_15116_1190449720}[ ]{lang="EN-US" style="font-weight:normal"}[statistics]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_1200832184}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib statistics]{lang="EN-US"}]{#struct_0_95746_15116_489699764}[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_x79907080}[模式：]{style="font-family:宋体"}

[**[display system internal fib statistics]{lang="EN-US"}**[ **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_2076255552}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_726108595}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_414875984}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_387074223}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_1181947357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_214422561}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_95746_15116_2480451}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x554247181}[：显示指定单板上的]{style="font-family:宋体;color:black"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项操作的统计信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_725649840}[：显示指定成员设备上的]{style="font-family:宋体;color:black"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项操作的统计信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1160107845}[：显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;color:black"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项操作的统计信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_1957080959}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项操作的统计信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_1466553302}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定单板的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项操作的统计信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1867338466}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[、]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项操作的统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1756083080 .myid}
[]{#_Toc404799513}[]{#struct_0_95746_15116_x893443166}[]{#_Toc343265995}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib vn**

------------------------------------------------------------------------

[**[display system internal fib vn]{lang="EN-US"}**]{#struct_0_95746_15116_x1377318822}[命令用来显示]{style="font-family:
宋体"}[VN]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_x2003233516}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_1652413382}

[[display system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_x1139423549}[\[ ]{lang="EN-US" style="font-weight:normal"}[next-hop]{lang="EN-US"}[ [next-hop]{.commandparameterChar} \]]{lang="EN-US" style="font-weight:normal"}

[[display system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_x485445363}[{ ]{lang="EN-US" style="font-weight:normal"}[id]{lang="EN-US"}[ [id \|]{.commandparameterChar}]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US"}*[index]{lang="EN-US"}[[ index]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ }]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_1854508023}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib]{lang="EN-US"}]{#struct_0_95746_15116_1580910916}[ ]{lang="EN-US" style="font-weight:normal"}[vn ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-weight:normal"}[next-hop]{lang="EN-US"}[ [next-hop]{.commandparameterChar} \]]{lang="EN-US" style="font-weight:normal"}[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number ]{lang="EN-US" style="font-weight:
normal"}]{.commandparameterChar}[\[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[display system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_x1978632631}[{ ]{lang="EN-US" style="font-weight:normal"}[id]{lang="EN-US"}[ [id \| ]{.commandparameterChar}]{lang="EN-US" style="font-weight:normal"}[index]{lang="EN-US"}[[ index]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ } ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number ]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_x2003299052}[模式：]{style="font-family:宋体"}

[**[display system internal fib vn]{lang="EN-US"}**[ \[ **next-hop** *next-hop* \] **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_1044390799}

[**[display system internal fib vn]{lang="EN-US"}**[ { **id** *id \|* **index** *index* } **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_2127709170}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_1296253112}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_x1885471971}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_x826216559}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_x1876486277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_x2003364588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_297292549}

[**[id ]{lang="EN-US"}***[id]{lang="EN-US"}*]{#struct_0_95746_15116_x695499515}[：]{style="font-family:宋体"}[按指定]{style="font-family:宋体"}[VN ID]{lang="EN-US"}[显示]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}

[**[index]{lang="EN-US"}***[ index]{lang="EN-US"}*]{#struct_0_95746_15116_x472445774}[：]{style="font-family:宋体"}[按指定]{style="font-family:宋体"}[VN]{lang="EN-US"}[索引显示]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}

[**[next-hop]{lang="EN-US"}**[ *next-hop*]{lang="EN-US"}]{#struct_0_95746_15116_1455775829}[：显示指定]{style="font-family:宋体;color:black"}[下一跳的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项基本信息，可以输入]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1059070549}[：显示指定单板上的]{style="font-family:宋体;color:black"}[VN]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x2003430124}[：显示指定成员设备上的]{style="font-family:宋体;color:black"}[VN]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_2691569}[：显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;color:black"}[VN]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_342944396}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x639684833}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定单板的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1867338470}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1091341499 .myid}
[]{#_Toc404799514}[]{#struct_0_95746_15116_x1033954127}[]{#_Toc343265996}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib vn reference**

------------------------------------------------------------------------

[**[display system internal fib vn reference]{lang="EN-US"}**]{#struct_0_95746_15116_375579864}[命令用来显示前缀关联]{style="font-family:宋体"}[VN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_x1904295539}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_x1181030525}

[[display system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_375645400}[{ ]{lang="EN-US" style="font-weight:normal"}[id]{lang="EN-US"}[ [id \| ]{.commandparameterChar}]{lang="EN-US" style="font-weight:normal"}[index]{lang="EN-US"}[[ index]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ } ]{lang="EN-US" style="font-weight:normal"}[reference]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_x1980347738}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib]{lang="EN-US"}]{#struct_0_95746_15116_400971347}[ ]{lang="EN-US" style="font-weight:normal"}[vn ]{lang="EN-US"}[{ ]{lang="EN-US" style="font-weight:normal"}[id]{lang="EN-US"}[ [id \|]{.commandparameterChar}]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US"}*[index]{lang="EN-US"}[[ index]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ } ]{lang="EN-US" style="font-weight:normal"}[reference slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:
normal"}]{.commandparameterChar}[ \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_x1854563662}[模式：]{style="font-family:宋体"}

[**[display system internal fib vn]{lang="EN-US"}**[ { **id** *id \|* **index** *index* } **reference** **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_620230568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_x46379823}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_x1382974318}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_2116970726}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_375710936}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_341396646}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_x841489224}

[**[id ]{lang="EN-US"}***[id]{lang="EN-US"}*]{#struct_0_95746_15116_x640603453}[：]{style="font-family:宋体"}[按指定]{style="font-family:宋体"}[VN ID]{lang="EN-US"}[显示]{style="font-family:宋体"}[VN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[index]{lang="EN-US"}***[ index]{lang="EN-US"}*]{#struct_0_95746_15116_x736846599}[：]{style="font-family:宋体"}[按指定]{style="font-family:宋体"}[VN]{lang="EN-US"}[指针显示]{style="font-family:宋体"}[VN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[reference]{lang="EN-US"}**]{#struct_0_95746_15116_x1720976919}[：显示]{style="font-family:宋体;color:black"}[关联该]{style="font-family:宋体"}[VN]{lang="EN-US"}[的前缀信息。]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_376300760}[：显示指定单板上的]{style="font-family:宋体;color:black"}[前缀关联]{style="font-family:
宋体"}[VN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_1322875782}[：显示指定成员设备上的]{style="font-family:宋体;color:black"}[前缀关联]{style="font-family:
宋体"}[VN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_1165490983}[：显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;color:black"}[前缀关联]{style="font-family:宋体"}[VN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_376366296}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定成员设备上指定单板的前缀关联]{style="font-family:宋体"}[VN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_120738640}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定单板的前缀关联]{style="font-family:宋体"}[VN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1867338467}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的前缀关联]{style="font-family:宋体"}[VN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1115705278 .myid}
[]{#_Toc404799515}[]{#struct_0_95746_15116_x1180670400}[]{#_Toc343265997}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib vn entry-status**

------------------------------------------------------------------------

[**[display system internal fib vn entry-status]{lang="EN-US"}**]{#struct_0_95746_15116_375514329}[命令用来显示指定状态的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项基本信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_1649262245}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_x120169755}

[[display system internal fib vn]{lang="EN-US"}]{#struct_0_95746_15116_x1059775931}[ ]{lang="EN-US" style="font-weight:normal"}[entry-status ]{lang="EN-US"}[[status]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_x2066096718}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display system internal fib]{lang="EN-US"}]{#struct_0_95746_15116_x719856340}[ ]{lang="EN-US" style="font-weight:normal"}[vn entry-status ]{lang="EN-US"}[[status ]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_375579865}[模式：]{style="font-family:宋体"}

[**[display system internal fib vn]{lang="EN-US"}**[ **entry-status** [status]{.commandparameterChar} **chassis** [chassis-number]{.commandparameterChar} **slot** [slot-number ]{.commandparameterChar}\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_x1904295540}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_1191163718}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_1564408510}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_1394978416}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_x392383825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_2084947957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_x1353726092}

[**[entry-status]{lang="EN-US"}**[ [status]{.commandparameterChar}]{lang="EN-US"}]{#struct_0_95746_15116_39538910}[：]{style="font-family:宋体;color:black"}[按指定状态显示]{style="font-family:宋体"}[VN]{lang="EN-US"}[信息。取值范围为]{style="font-family:宋体"}[\<A,F,R\>]{lang="EN-US"}[，"]{style="font-family:宋体"}[A]{lang="EN-US"}["表示待老化表项，"]{style="font-family:宋体"}[F]{lang="EN-US"}["表示下驱动失败表项，"]{style="font-family:宋体"}[R]{lang="EN-US"}["表示由于被关联而未删除的表项。]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_375645401}[：显示指定单板上的]{style="font-family:宋体;color:black"}[指定状态的]{style="font-family:
宋体"}[VN]{lang="EN-US"}[表项基本信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_375710937}[：显示指定成员设备的]{style="font-family:宋体;color:black"}[指定状态的]{style="font-family:
宋体"}[VN]{lang="EN-US"}[表项基本信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x1966676899}[：显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[指定状态的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项基本信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_341396645}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定成员设备上指定单板的指定状态的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项基本信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ [chassis-number]{.commandparameterChar} ]{lang="EN-US" style="color:black"}]{#struct_0_95746_15116_x599784951}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ [slot-number]{.commandparameterChar}]{lang="EN-US"}[：显示指定单板的指定状态的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项基本信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_471313694}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的指定状态的]{style="font-family:宋体"}[VN]{lang="EN-US"}[表项基本信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-696260860 .myid}
[]{#_Toc404799516}[]{#struct_0_95746_15116_x1513280703}

**IP转发基础 \-- IP转发基础Probe配置命令 \-- reset system internal fib statistics**

------------------------------------------------------------------------

[**[reset system internal fib statistics]{lang="EN-US"}**]{#struct_0_95746_15116_375514326}[命令用来清除]{style="font-family:宋体"}[FIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_1649262232}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_x120497440}

[**[reset system internal fib statistics]{lang="EN-US"}**]{#struct_0_95746_15116_x259814207}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_291446945}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal fib statistics]{lang="EN-US"}***[ ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_x29415070}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95746_15116_2121934242}[模式：]{style="font-family:宋体"}

[**[reset system internal fib statistics]{lang="EN-US"}***[ ]{lang="EN-US"}***[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_95746_15116_2095993766}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_x470487796}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_1553222029}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_375579862}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_x1904295541}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_x1537719637}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_x754570617}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_456323688}[：清除指定单板的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_1122171572}[：清除指定成员设备的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1516338205}[：清除指定成员]{style="font-family:宋体"}[设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x772691873}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_1931840674}[：清除指定单板的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_471313690}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[FIB]{lang="EN-US"}[统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1451826625 .myid}
[]{#_Toc404799518}[]{#struct_0_95746_15116_x1531911394}[]{#_Toc343265999}

**IP转发基础 \-- IP转发基础Probe调试命令 \-- debugging system internal fib prefix**

------------------------------------------------------------------------

[**[debugging system internal fib ]{lang="EN-US"}**]{#struct_0_95746_15116_x467607599}[命令用来]{style="font-family:
宋体"}[打开]{style="font-family:宋体"}[FIB]{lang="EN-US"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo debugging system internal fib]{lang="EN-US"}**]{#struct_0_95746_15116_x1271115318}[命令用来]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[FIB]{lang="EN-US"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_x271927993}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_375710934}

[[debugging system internal fib prefix]{lang="EN-US"}]{#struct_0_95746_15116_341396648}[ {]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[}]{lang="EN-US" style="font-weight:normal"}

[[undo debugging system internal fib prefix ]{lang="EN-US"}]{#struct_0_95746_15116_x841489222}[{]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[}]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_x640996669}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[debugging system internal fib prefix ]{lang="EN-US"}]{#struct_0_95746_15116_x1896458738}[{]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[} ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[undo debugging system internal fib prefix]{lang="EN-US"}]{#struct_0_95746_15116_x20762595}[ {]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[} ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number ]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[ IRF]{lang="EN-US"}]{#struct_0_95746_15116_850540718}[模式：]{style="font-family:宋体"}

[[debugging system internal fib prefix]{lang="EN-US"}]{#struct_0_95746_15116_1828756183}[ {]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[} ]{lang="EN-US" style="font-weight:normal"}[chassis ]{lang="EN-US"}[[chassis-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ slot ]{lang="EN-US"}*[slot-number ]{lang="EN-US" style="font-weight:normal"}*[\[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[undo debugging system internal fib prefix]{lang="EN-US"}]{#struct_0_95746_15116_x2052109759}[ {]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[} ]{lang="EN-US" style="font-weight:normal"}[chassis ]{lang="EN-US"}*[chassis-number]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}*[slot-number]{lang="EN-US" style="font-weight:normal"}*[  \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95746_15116_x467476527}

[[FIB ]{lang="EN-US"}]{#struct_0_95746_15116_297000168}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_376300758}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_x633439346}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_303764179}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_132159543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_x780282517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_1799183122}

[**[all]{lang="EN-US"}**]{#struct_0_95746_15116_x1352729922}[：]{style="font-family:宋体"}[打开所有调试开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_95746_15116_2047299732}[：]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[message]{lang="EN-US"}[调试开关，打印路由下发和板间同步的]{style="font-family:宋体"}[IPv4 FIB]{lang="EN-US"}[前缀消息。]{style="font-family:宋体"}

[**[hardware]{lang="EN-US"}**]{#struct_0_95746_15116_376366294}[：]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[hardware]{lang="EN-US"}[调试开关，打印下发驱动信息以及驱动返回的消息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_95746_15116_595014853}[：打开指定单板的调试开关。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_95746_15116_x1890731835}[：]{style="font-family:宋体"}[打开指定成员设备的调试开关。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_95746_15116_x1160042309}[：]{style="font-family:宋体"}[打开指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试开关。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_x793931837}[：打开指定成员设备上指定单板的调试开关。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_1568841046}[：打开指定单板的调试开关。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_471313702}[：]{style="font-family:宋体"}[打开指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[调试开关。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-634261492 .myid}
[]{#_Toc404799519}[]{#struct_0_95746_15116_1943517010}[]{#_Toc343266000}

**IP转发基础 \-- IP转发基础Probe调试命令 \-- debugging system internal fib vn**

------------------------------------------------------------------------

[**[debugging system internal fib vn ]{lang="EN-US"}**]{#struct_0_95746_15116_x1630144868}[命令用来]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[VN]{lang="EN-US"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo debugging system internal fib vn]{lang="EN-US"}**]{#struct_0_95746_15116_x1630079332}[命令用来关闭]{style="font-family:宋体"}[VN]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_95746_15116_x530121683}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95746_15116_404516204}

[[debugging system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_x969456328}[{]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ bind ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ notify]{lang="EN-US"}[}]{lang="EN-US" style="font-weight:normal"}

[[undo d debugging system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_x1689264920}[{]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ bind ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ notify]{lang="EN-US"}[ }]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_408728869}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[debugging system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_1942057022}[{]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ bind ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ notify]{lang="EN-US"}[ } ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[  \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[undo debugging system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_x1320551215}[{]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ bind ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ notify]{lang="EN-US"}[ } ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number ]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[\[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95746_15116_x2071457364}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[debugging system internal fib vn ]{lang="EN-US"}]{#struct_0_95746_15116_65942461}[{]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ bind ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ notify]{lang="EN-US"}[ } ]{lang="EN-US" style="font-weight:normal"}[chassis ]{lang="EN-US"}[[chassis-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ slot ]{lang="EN-US"}*[slot-number ]{lang="EN-US" style="font-weight:normal"}*[\[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[undo debugging system internal fib vn]{lang="EN-US"}]{#struct_0_95746_15116_x1657392833}[ {]{lang="EN-US" style="font-weight:normal"}[ all ]{lang="EN-US"}[\| ]{lang="EN-US" style="font-weight:normal"}[message ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ hardware ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ bind ]{lang="EN-US"}[\|]{lang="EN-US" style="font-weight:normal"}[ notify]{lang="EN-US"}[ } ]{lang="EN-US" style="font-weight:normal"}[chassis ]{lang="EN-US"}*[chassis-number]{lang="EN-US" style="font-weight:normal"}*[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}*[slot-number]{lang="EN-US" style="font-weight:normal"}*[ \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \]]{lang="EN-US" style="font-weight:normal"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_95746_15116_x1630013796}

[[VN ]{lang="EN-US"}]{#struct_0_95746_15116_x265023661}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95746_15116_x1529502983}

[[Probe]{lang="EN-US"}]{#struct_0_95746_15116_x222867347}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95746_15116_x715420355}

[[network-admin]{lang="EN-US"}]{#struct_0_95746_15116_1941598270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95746_15116_717481990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95746_15116_x2043804906}

[**[all]{lang="EN-US"}**]{#struct_0_95746_15116_x1535986427}[：]{style="font-family:宋体"}[打开所有调试开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_95746_15116_1941663806}[：]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[message]{lang="EN-US"}[调试开关]{style="font-family:宋体"}[,]{lang="EN-US"}[显示路由下发和板间同步的]{style="font-family:宋体"}[vn]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[**[hardware]{lang="EN-US"}**]{#struct_0_95746_15116_1941729342}[：]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[hardware]{lang="EN-US"}[调试开关，显示下发驱动的信息以及驱动返回的信息。]{style="font-family:宋体"}

[**[bind]{lang="EN-US"}**]{#struct_0_95746_15116_1942384702}[：]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[bind]{lang="EN-US"}[调试开关，显示前缀绑定]{style="font-family:宋体"}[vn]{lang="EN-US"}[，]{style="font-family:宋体"}[vn]{lang="EN-US"}[绑定]{style="font-family:宋体"}[adj/nhlfe]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_95746_15116_1941925947}[：]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[notify]{lang="EN-US"}[调试开关，显示]{style="font-family:宋体"}[adj/nhlfe]{lang="EN-US"}[通知]{style="font-family:宋体"}[vn]{lang="EN-US"}[，以及]{style="font-family:宋体"}[vn]{lang="EN-US"}[通知前缀的信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_95746_15116_1941991483}[：打开指定单板的调试开关。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_95746_15116_1943189330}[：]{style="font-family:宋体"}[打开指定成员设备的调试开关。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_95746_15116_x1563326836}[：]{style="font-family:宋体"}[打开指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试开关。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_608787753}[：打开指定成员设备上指定单板的调试开关。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_95746_15116_386000008}[：打开指定单板的调试开关。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_95746_15116_x1485001440}[：]{style="font-family:宋体"}[打开指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的调试开关。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
