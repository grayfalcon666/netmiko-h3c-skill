::: {#-1434177193 .myid}
[]{#_Toc404799106}[]{#struct_0_16240_64087_2072295309}[]{#_Toc322610594}[]{#_Toc33197998}

**IPv6策略路由 \-- IPv6策略路由Probe配置命令 \-- display system internal ipv6 pbr policy**

------------------------------------------------------------------------

[**[display system internal ipv6 pbr policy]{lang="EN-US"}**]{#struct_0_16240_64087_x1816689131}[用于显示用户态下的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_1987471625}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_16240_64087_1168173963}

[**[display system internal ipv6 pbr policy]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_16240_64087_x1041911424}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name ]{lang="EN-US"}*[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_16240_64087_338295387}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal ipv6 pbr slot]{lang="EN-US"}**]{#struct_0_16240_64087_1510425260}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **policy**]{lang="EN-US"}[ \[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-nam]{lang="EN-US"}*[ \[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\] \] ]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_16240_64087_x518036881}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal ipv6 pbr chassis]{lang="EN-US"}**]{#struct_0_16240_64087_59751142}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **policy** ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name ]{lang="EN-US"}*[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\] \] ]{lang="EN-US" style="font-size:10.0pt;
color:black"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_1633705709}

[[Probe]{lang="EN-US"}]{#struct_0_16240_64087_x1615606350}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_2099825301}

[[network-admin]{lang="EN-US"}]{#struct_0_16240_64087_x1160795915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16240_64087_1510621868}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_303796289}

[]{#OLE_LINK2}[]{#struct_0_16240_64087_444593329}[]{#OLE_LINK3}**[policy]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;
color:black"}*[policy-name]{lang="EN-US"}*[：显示用户态下指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由信息。]{style="font-family:宋体"}[policy-name]{lang="EN-US"}[为策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[setup]{lang="EN-US"}**]{#struct_0_16240_64087_1867102438}[：显示用户态下指定]{style="font-family:宋体"}[策略的接口应用信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_1089027298}[：显示]{style="font-family:宋体"}[用户态下指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_x126560966}[：显示用户态下指定成员设备]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_537858545}[：显示用户态下]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16240_64087_571146555}[：显示用户态下指定成员设备上指定单板]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16240_64087_x1028225396}[：显示用户态下指定单板]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_16240_64087_x1077167909}[：显示用户态下指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-770338894 .myid}
[]{#_Toc404799107}[]{#struct_0_16240_64087_x586217358}[]{#_Toc361909210}[]{#_Toc361909211}[]{#_Toc361909212}[]{#_Toc361909213}[]{#_Toc361909214}[]{#_Toc361909215}[]{#_Toc361909216}[]{#_Toc361909217}[]{#_Toc361909230}[]{#_Toc361909231}[]{#_Toc361909232}[]{#_Toc361909233}[]{#_Toc361909234}[]{#_Toc361909235}[]{#_Toc361909236}[]{#_Toc361909237}[]{#_Toc361909238}[]{#_Toc361909239}[]{#_Toc361909255}[]{#_Toc361909256}[]{#_Toc361909257}[]{#_Toc361909258}[]{#_Toc361909259}[]{#_Toc361909260}[]{#_Toc361909261}[]{#_Toc361909262}[]{#_Toc361909275}

**IPv6策略路由 \-- IPv6策略路由Probe配置命令 \-- display system internal ipv6 pbr kernel policy**

------------------------------------------------------------------------

[**[display system internal ipv6 pbr kernel policy]{lang="EN-US"}**]{#struct_0_16240_64087_333750805}[用于显示内核态下指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_1511015084}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_16240_64087_637362925}

[**[display system internal ipv6 pbr kernel policy]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_16240_64087_1430846694}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name ]{lang="EN-US"}*[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_16240_64087_x2110182684}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal ipv6 pbr]{lang="EN-US"}**]{#struct_0_16240_64087_439292852}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **kernel policy** ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name]{lang="EN-US"}*[ \[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_16240_64087_143302027}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal ipv6 pbr]{lang="EN-US"}**]{#struct_0_16240_64087_1510949548}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **kernel policy** ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name]{lang="EN-US"}*[ \[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_818341273}

[[Probe]{lang="EN-US"}]{#struct_0_16240_64087_x273635488}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_1183735962}

[[network-admin]{lang="EN-US"}]{#struct_0_16240_64087_x259867106}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16240_64087_x2029141296}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_x1574733180}

[**[policy]{lang="EN-US"}**]{#struct_0_16240_64087_1188120579}[ ]{lang="EN-US" style="font-size:10.0pt;
color:black"}*[policy-name]{lang="EN-US"}*[：显示内核态下指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由信息。]{style="font-family:宋体"}[policy-name]{lang="EN-US"}[为策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[setup]{lang="EN-US"}**]{#struct_0_16240_64087_1510490793}[：显示内核态指定]{style="font-family:宋体"}[策略的接口应用信息]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_1433404585}[：显示]{style="font-family:宋体"}[内核态下指定单板上的内核态下]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_1637564979}[：显示]{style="font-family:宋体"}[内核态下]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_134574018}[：显示]{style="font-family:宋体"}[内核]{style="font-family:宋体"}[态下]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16240_64087_x1487191544}[：显示]{style="font-family:宋体"}[内核态下]{style="font-family:宋体"}[指定成员设备上指定单板]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16240_64087_1818772333}[：显示]{style="font-family:宋体"}[内核]{style="font-family:宋体"}[态下指定单板]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_16240_64087_x1076643622}[：显示内核态下指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1389252671 .myid}
[]{#_Toc404799108}[]{#struct_0_16240_64087_369651028}[]{#_Toc361909277}[]{#_Toc361909278}[]{#_Toc361909279}[]{#_Toc361909280}[]{#_Toc361909281}[]{#_Toc361909282}[]{#_Toc361909283}[]{#_Toc361909284}[]{#_Toc361909285}[]{#_Toc361909286}[]{#_Toc361909287}[]{#_Toc361909288}[]{#_Toc361909289}[]{#_Toc361909290}[]{#_Toc361909309}[]{#_Toc361909310}[]{#_Toc361909311}[]{#_Toc361909312}[]{#_Toc361909313}[]{#_Toc361909314}[]{#_Toc361909315}[]{#_Toc361909316}[]{#_Toc361909317}[]{#_Toc361909330}[]{#_Toc361909331}[]{#_Toc361909332}[]{#_Toc361909333}[]{#_Toc361909334}[]{#_Toc361909335}[]{#_Toc361909336}[]{#_Toc361909337}[]{#_Toc361909350}

**IPv6策略路由 \-- IPv6策略路由Probe配置命令 \-- display system internal ipv6 pbr fib**

------------------------------------------------------------------------

[**[display system internal ipv6 pbr fib]{lang="EN-US"}**]{#struct_0_16240_64087_x225750905}[命令用来显示用户态下]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_765133179}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_16240_64087_x601909611}

[**[display system internal ipv6 pbr fib ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_16240_64087_x1781920968}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_16240_64087_1510818473}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal ipv6 pbr]{lang="EN-US"}**]{#struct_0_16240_64087_x151475973}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **fib** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_16240_64087_424651655}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal ipv6 pbr]{lang="EN-US"}**]{#struct_0_16240_64087_x835554473}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **fib** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_x1503628149}

[[Probe]{lang="EN-US"}]{#struct_0_16240_64087_1968538631}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_x1202278832}

[[network-admin]{lang="EN-US"}]{#struct_0_16240_64087_1796071982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16240_64087_1541399561}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16240_64087_x861184659}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_16240_64087_1846997802}[：显示用户态下指定私网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息，不指定该参数为公网内下一跳。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_x2076378200}[：]{style="font-family:宋体"}[显示用户态下指定单板指定私网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_1510949545}[：]{style="font-family:宋体"}[显示用户态下]{style="font-family:宋体"}[指定成员设备的]{style="font-family:宋体"}[指定私网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_16240_64087_1297373432}[：]{style="font-family:宋体"}[显示用户态下]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[指定私网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16240_64087_x526437314}[：显示]{style="font-family:宋体"}[用户态下]{style="font-family:宋体"}[指定成员设备上指定单板]{style="font-family:宋体"}[的指定私网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_16240_64087_94763778}[：显示]{style="font-family:宋体"}[用户态下]{style="font-family:宋体"}[指定单板]{style="font-family:宋体"}[的指定私网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_16240_64087_x1076512550}[：显示用户态下指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上指定私网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[下一跳的配置信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US" style="font-size:10.0pt;font-family:\"Courier New\""}
:::
