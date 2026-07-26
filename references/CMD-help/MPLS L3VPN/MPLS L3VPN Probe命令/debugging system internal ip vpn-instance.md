::: {#133692062 .myid}
[]{#_Toc404799862}[]{#struct_0_x1798_11770_1931636798}[]{#_Toc349222972}[]{#_Toc343266700}

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- debugging system internal ip vpn-instance**

------------------------------------------------------------------------

[**[debugging system internal ip vpn-instance]{lang="EN-US"}**]{#struct_0_x1798_11770_1963928490}[命令用来打开]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}

[**[undo debugging system internal ip vpn-instance]{lang="EN-US"}**]{#struct_0_x1798_11770_357805526}[命令用来关闭]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1798_11770_35424847}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1798_11770_x1629593233}

[**[debugging system internal ip vpn-instance]{lang="EN-US"}**]{#struct_0_x1798_11770_703535052}

[**[undo debugging system internal ip vpn-instance]{lang="EN-US"}**]{#struct_0_x1798_11770_212138802}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1798_11770_82234262}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging system internal ip vpn-instance slot]{lang="EN-US"}**]{#struct_0_x1798_11770_x1727775822}*[ slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[**[undo debugging system internal ip vpn-instance slot]{lang="EN-US"}**]{#struct_0_x1798_11770_39286776}*[ slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1798_11770_1931178043}[模式：]{style="font-family:宋体"}

[**[debugging system internal ip vpn-instance chassis]{lang="EN-US"}**]{#struct_0_x1798_11770_1901705688}*[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **debugging system internal ip vpn-instance chassis**]{lang="EN-US"}]{#struct_0_x1798_11770_901933704}*[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1372559335}

[[VPN]{lang="EN-US"}]{#struct_0_x1798_11770_x534832400}[实例的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x1853043636}

[[Probe]{lang="EN-US"}]{#struct_0_x1798_11770_352978749}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1643362012}

[[network-admin]{lang="EN-US"}]{#struct_0_x1798_11770_x1636476223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1798_11770_1931112507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x392298958}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x635993946}*[ slot-number]{lang="PT-BR"}*[：表示指定单板上的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_210786190}*[ slot-number]{lang="PT-BR"}*[：表示指定成员设备上的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x1026283333}*[ slot-number]{lang="PT-BR"}*[：表示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_x1550742788}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：表示指定成员设备上指定单板的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_1068258117}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：表示指定单板的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1798_11770_x1465537274}[：]{style="font-family:宋体"}[表示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例调试信息开关。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1565696666 .myid}
[]{#_Toc53860601}[]{#_Toc137867281}[]{#_Toc83790606}[]{#_Toc81376567}[]{#_Toc67196362}[]{#_Toc67145409}[]{#_Toc404799863}[]{#struct_0_x1798_11770_1129858428}[]{#_Toc349222973}[]{#_Toc343266696}[]{#_Toc361312273}[]{#_Toc361312274}[]{#_Toc361312275}[]{#_Toc361312276}[]{#_Toc361312277}[]{#_Toc361312278}[]{#_Toc361312279}[]{#_Toc361312280}[]{#_Toc361312281}[]{#_Toc361312282}

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-binding**

------------------------------------------------------------------------

[**[display system internal ip vpn-binding]{lang="EN-US"}**]{#struct_0_x1798_11770_724948914}[命令用来显示内核的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1658602203}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1798_11770_x377996392}

[**[display system internal ip vpn-binding]{lang="EN-US"}**]{#struct_0_x1798_11770_1892073103}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1798_11770_x1776616740}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip vpn-binding slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1798_11770_586770163}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1798_11770_x2019575795}[模式：]{style="font-family:宋体"}

[**[display system internal ip vpn-binding chassis]{lang="EN-US"}**]{#struct_0_x1798_11770_1931243579}*[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1164413433}

[[Probe]{lang="EN-US"}]{#struct_0_x1798_11770_x711544550}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1798_11770_118138092}

[[network-admin]{lang="EN-US"}]{#struct_0_x1798_11770_x1305446505}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1798_11770_735918093}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1197017967}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x1986081458}*[ slot-number]{lang="PT-BR"}*[：显示指定单板上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例绑定信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x1575908580}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例绑定信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_1702600022}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例绑定信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_1931440187}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上指定单板的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例绑定信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_136516081}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定单板的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例绑定信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1798_11770_x276058882}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例绑定信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-106734466 .myid}
[]{#_Toc404799864}[]{#struct_0_x1798_11770_2014863275}[]{#_Toc349222974}[]{#_Toc343266697}[]{#_Toc340564366}[]{#_Toc361312284}[]{#_Toc361312285}[]{#_Toc361312286}[]{#_Toc361312287}[]{#_Toc361312288}[]{#_Toc361312289}[]{#_Toc361312290}[]{#_Toc361312291}[]{#_Toc361312292}[]{#_Toc361312305}

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-instance**

------------------------------------------------------------------------

[**[display system internal ip vpn-instance]{lang="EN-US"}**]{#struct_0_x1798_11770_1931571259}[命令用来显示内核的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x801464358}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1798_11770_1091879889}

[**[display system internal ip vpn-instance]{lang="EN-US"}**[ \[ **instance-name** ]{lang="EN-US"}]{#struct_0_x1798_11770_x532136390}*[vpn-instance-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1798_11770_1804859600}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip vpn-instance]{lang="EN-US"}**[ \[ **instance-name** ]{lang="EN-US"}]{#struct_0_x1798_11770_x344245163}*[vpn-instance-name]{lang="EN-US"}*[ \] **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1798_11770_1823716053}[模式：]{style="font-family:宋体"}

[**[display system internal ip vpn-instance]{lang="EN-US"}**[ \[ **instance-name** ]{lang="EN-US"}]{#struct_0_x1798_11770_x436778418}*[vpn-instance-name ]{lang="EN-US"}*[\] **chassis** ]{lang="EN-US"}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1798_11770_2116716431}

[[Probe]{lang="EN-US"}]{#struct_0_x1798_11770_1931505723}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x1934701201}

[[network-admin]{lang="EN-US"}]{#struct_0_x1798_11770_1271175795}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1798_11770_1717473970}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1284613838}

[**[instance-name ]{lang="EN-US"}**]{#struct_0_x1798_11770_x1859190126}*[vpn-instance-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的内核信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_252344317}*[ slot-number]{lang="PT-BR"}*[：显示指定单板上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_1287292340}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x1429567860}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_x449737086}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上指定单板的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_x622031734}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定单板的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1798_11770_x276058880}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1804664969 .myid}
[]{#_Toc404799865}[]{#struct_0_x1798_11770_x2128357969}[]{#_Toc361312307}[]{#_Toc361312308}[]{#_Toc361312309}[]{#_Toc361312310}[]{#_Toc361312311}[]{#_Toc361312312}[]{#_Toc361312313}[]{#_Toc361312314}[]{#_Toc361312315}[]{#_Toc361312316}[]{#_Toc361312317}[]{#_Toc361312336}

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-instance inactive**

------------------------------------------------------------------------

[**[display system internal ip vpn-instance inactive]{lang="EN-US"}**]{#struct_0_x1798_11770_x508769033}[命令用来显示正在删除中的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x835974412}

[**[display system internal ip vpn-instance inactive]{lang="EN-US"}**]{#struct_0_x1798_11770_725618829}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1931112508}

[[Probe]{lang="EN-US"}]{#struct_0_x1798_11770_x392102350}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1798_11770_491207785}

[[network-admin]{lang="EN-US"}]{#struct_0_x1798_11770_x1786813254}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1798_11770_1955513537}
:::

::: {#903649303 .myid}
[]{#_Toc404799866}[]{#struct_0_x1798_11770_1931243580}[]{#_Toc349222975}[]{#_Toc343266698}[]{#_Toc361312338}[]{#_Toc361312339}[]{#_Toc361312340}[]{#_Toc361312341}[]{#_Toc361312342}[]{#_Toc361312343}[]{#_Toc361312344}[]{#_Toc361312345}[]{#_Toc361312346}[]{#_Toc361312347}[]{#_Toc361312348}[]{#_Toc361312349}[]{#_Toc361312359}

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ip vpn-instance statistics**

------------------------------------------------------------------------

[**[display system internal ip vpn-instance statistics]{lang="EN-US"}**]{#struct_0_x1798_11770_1164872176}[命令用来显示内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x1871234049}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1798_11770_601311525}

[**[display system internal ip vpn-instance statistics]{lang="EN-US"}**]{#struct_0_x1798_11770_1023690003}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1798_11770_204878750}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip vpn-instance statistics slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1798_11770_1085337647}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1798_11770_x229059230}[模式：]{style="font-family:宋体"}

[**[display system internal ip vpn-instance statistics chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1798_11770_376707560}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1931440188}

[[Probe]{lang="EN-US"}]{#struct_0_x1798_11770_x799861601}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1729737229}

[[network-admin]{lang="EN-US"}]{#struct_0_x1798_11770_x1637105951}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1798_11770_x1053862330}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x1918491962}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x2119458556}*[ slot-number]{lang="PT-BR"}*[：显示指定单板上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x1743478301}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x1798_11770_x266768446}*[ slot-number]{lang="PT-BR"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_1931374652}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定成员设备上指定单板的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x1798_11770_x328106869}*[chassis-number]{lang="PT-BR"}*[ ]{lang="PT-BR"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[：显示指定单板的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1798_11770_x276058886}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的内核]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1405455163 .myid}
[]{#_Toc404799867}[]{#struct_0_x1798_11770_1999830522}[]{#_Toc378146369}[]{#_Toc335321155}

**MPLS L3VPN \-- MPLS L3VPN Probe命令 \-- display system internal ospf sham-link standby**

------------------------------------------------------------------------

[**[display system internal ospf sham-link standby]{lang="EN-US"}**]{#struct_0_x1798_11770_x1608231001}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[备进程上]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[伪连接的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x1830650235}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1798_11770_x1592209113}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[system internal ospf ]{lang="EN-US"}**[\[ *process-id* \] **sham-link** \[ **area** *area-id* \] **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1798_11770_x2015539364}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1798_11770_1647831756}[模式：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[system internal ospf ]{lang="EN-US"}**[\[ *process-id* \] **sham-link** \[ **area** *area-id* \] **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1798_11770_x705054867}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1798_11770_918995687}

[[Probe]{lang="EN-US"}]{#struct_0_x1798_11770_x1927315556}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1999896058}

[[network-admin]{lang="EN-US"}]{#struct_0_x1798_11770_x1624489762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1798_11770_x1419861588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1798_11770_x411815593}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1798_11770_2043556089}[：显示指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程内的伪连接信息。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的伪连接信息。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}**[ *area-id*]{lang="EN-US"}]{#struct_0_x1798_11770_737115086}[：显示指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域内的伪连接信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域号，可以是整数形式，也可以是]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址形式。当是整数形式时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域的伪连接信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1798_11770_x1182983328}[：指定备进程所在的单板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1798_11770_1622163849}[：指定备进程所在的成员设备。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1798_11770_1386516885}[：指定备进程所在的成员设备和单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1798_11770_2086363149}[：]{style="font-family:宋体"}[指定备进程所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1798_11770_1999306239}

[[执行本命令时，如果不指定进程号和区域号，则显示所有的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x1798_11770_x1260371447}[伪连接信息。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[OSPF NSR]{lang="EN-US"}]{#struct_0_x1798_11770_x1000403068}[功能后，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[主进程将]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居和路由等信息备份到备进程，通过本命令可以显示备份到备进程的信息。如果没有开启]{style="font-family:宋体"}[OSPF NSR]{lang="EN-US"}[功能，则不会显示任何信息。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
