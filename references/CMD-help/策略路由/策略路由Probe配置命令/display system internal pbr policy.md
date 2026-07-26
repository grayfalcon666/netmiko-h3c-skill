::: {#288990856 .myid}
[]{#_Toc404800657}[]{#struct_0_19016_79711_x1841736138}

**策略路由 \-- 策略路由Probe配置命令 \-- display system internal pbr policy**

------------------------------------------------------------------------

[**[display system internal pbr policy]{lang="EN-US"}**]{#struct_0_19016_79711_x566212314}[用于显示用户态下的策略路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_x1502148136}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_19016_79711_682551401}

[**[display system internal pbr policy]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_19016_79711_x1333050583}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name]{lang="EN-US"}*[ \[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_19016_79711_x1014016368}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal pbr slot]{lang="EN-US"}**]{#struct_0_19016_79711_x1240698329}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] ** policy** ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name ]{lang="EN-US"}*[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup]{lang="EN-US"}**[ ]{lang="EN-US"}[\] \]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_19016_79711_x1200924303}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal pbr chassis]{lang="EN-US"}**]{#struct_0_19016_79711_1850683639}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **policy** ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup]{lang="EN-US"}**[ ]{lang="EN-US"}[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_x1936667154}

[[Probe]{lang="EN-US"}]{#struct_0_19016_79711_x1100450535}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_1714438855}

[[network-admin]{lang="EN-US"}]{#struct_0_19016_79711_x527521419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19016_79711_x2062584366}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_x1200727695}

[**[policy]{lang="EN-US"}**]{#struct_0_19016_79711_x1134159318}[ ]{lang="EN-US" style="font-size:10.0pt;
color:black"}*[policy-name]{lang="EN-US"}*[：显示用户态下指定策略路由的信息。]{style="font-family:宋体"}[policy-name]{lang="EN-US"}[为策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[setup]{lang="EN-US"}**]{#struct_0_19016_79711_x976928504}[：显示用户态下指定]{style="font-family:宋体"}[策略的接口应用信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_x543269364}[：显示]{style="font-family:宋体"}[用户态下指定单板上的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_x176739816}[：显示]{style="font-family:宋体"}[用户态下]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_x1829558085}[：显示用户态下]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19016_79711_183691568}[：显示]{style="font-family:宋体"}[用户态下]{style="font-family:宋体"}[指定成员设备上指定单板]{style="font-family:宋体"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19016_79711_x633875858}[：显示用户态下指定单板]{style="font-family:宋体"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_19016_79711_x269570818}[：显示用户态下指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上策略路由]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1265479622 .myid}
[]{#_Toc404800658}[]{#struct_0_19016_79711_762123480}[]{#_Toc361908240}[]{#_Toc361908241}[]{#_Toc361908242}[]{#_Toc361908243}[]{#_Toc361908244}[]{#_Toc361908245}[]{#_Toc361908246}[]{#_Toc361908247}[]{#_Toc361908260}[]{#_Toc361908261}[]{#_Toc361908262}[]{#_Toc361908263}[]{#_Toc361908264}[]{#_Toc361908265}[]{#_Toc361908266}[]{#_Toc361908267}[]{#_Toc361908268}[]{#_Toc361908269}[]{#_Toc361908285}[]{#_Toc361908286}[]{#_Toc361908287}[]{#_Toc361908288}[]{#_Toc361908289}[]{#_Toc361908290}[]{#_Toc361908291}[]{#_Toc361908292}[]{#_Toc361908305}

**策略路由 \-- 策略路由Probe配置命令 \-- display system internal pbr kernel policy**

------------------------------------------------------------------------

[**[display system internal pbr kernel policy]{lang="EN-US"}**]{#struct_0_19016_79711_x28620885}[用于显示内核态下的策略路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_780640107}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_19016_79711_x809599468}

[**[display system internal pbr kernel policy]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_19016_79711_x1201055374}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name]{lang="EN-US"}*[ \[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_19016_79711_241821992}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal pbr slot]{lang="EN-US"}**]{#struct_0_19016_79711_x926144355}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **kernel policy** ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name ]{lang="EN-US"}*[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_19016_79711_649866854}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal pbr chassis]{lang="EN-US"}**]{#struct_0_19016_79711_1352635686}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **kernel policy** ]{lang="EN-US"}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[policy-name ]{lang="EN-US"}*[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[setup ]{lang="EN-US"}**[\]]{lang="EN-US" style="font-size:10.0pt;
color:black"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US" style="font-size:10.0pt;color:black"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_1774994949}

[[Probe]{lang="EN-US"}]{#struct_0_19016_79711_x1340602801}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_x1835718253}

[[network-admin]{lang="EN-US"}]{#struct_0_19016_79711_x2026796614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19016_79711_x551863554}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_2090243384}

[**[policy]{lang="EN-US"}**]{#struct_0_19016_79711_1368452641}[ ]{lang="EN-US" style="font-size:10.0pt;
color:black"}*[policy-name]{lang="EN-US"}*[：显示内核态下指定策略路由的信息。]{style="font-family:宋体"}[policy-name]{lang="EN-US"}[为策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[setup]{lang="EN-US"}**]{#struct_0_19016_79711_x1200924302}[：显示内核态指定]{style="font-family:宋体"}[策略的接口应用信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_284599698}[：显示]{style="font-family:宋体"}[内核态下指定单板上的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_1961065058}[：显示]{style="font-family:宋体"}[内核态下]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_x666758671}[：显示]{style="font-family:宋体"}[内核]{style="font-family:宋体"}[态下]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19016_79711_432970454}[：显示]{style="font-family:宋体"}[内核态下]{style="font-family:宋体"}[指定成员设备上指定单板]{style="font-family:宋体"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19016_79711_x219841393}[：显示]{style="font-family:宋体"}[内核]{style="font-family:宋体"}[态下指定单板]{style="font-family:宋体"}[的策略路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_19016_79711_x269570816}[：显示内核态下指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上策略路由]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1572260241 .myid}
[]{#_Toc404800659}[]{#struct_0_19016_79711_x1725911094}[]{#_Toc361908307}[]{#_Toc361908308}[]{#_Toc361908309}[]{#_Toc361908310}[]{#_Toc361908311}[]{#_Toc361908312}[]{#_Toc361908313}[]{#_Toc361908314}[]{#_Toc361908315}[]{#_Toc361908316}[]{#_Toc361908317}[]{#_Toc361908318}[]{#_Toc361908319}[]{#_Toc361908320}[]{#_Toc361908321}[]{#_Toc361908340}[]{#_Toc361908341}[]{#_Toc361908342}[]{#_Toc361908343}[]{#_Toc361908344}[]{#_Toc361908345}[]{#_Toc361908346}[]{#_Toc361908347}[]{#_Toc361908348}[]{#_Toc361908361}[]{#_Toc361908362}[]{#_Toc361908363}[]{#_Toc361908364}[]{#_Toc361908365}[]{#_Toc361908366}[]{#_Toc361908367}[]{#_Toc361908368}[]{#_Toc361908381}

**策略路由 \-- 策略路由Probe配置命令 \-- display system internal pbr fib**

------------------------------------------------------------------------

[**[display system internal pbr fib]{lang="EN-US"}**]{#struct_0_19016_79711_x1368931230}[命令用来显示用户态下下一跳的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_698833344}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_19016_79711_207611059}

[**[display system internal pbr fib ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19016_79711_x477747156}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_19016_79711_x356955738}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal pbr slot]{lang="EN-US"}**]{#struct_0_19016_79711_721258930}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **fib** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_19016_79711_1211439929}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal pbr chassis]{lang="EN-US"}**]{#struct_0_19016_79711_x544066336}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[slot-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cpu** *cpu-number* \] **fib** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_x1922329629}

[[Probe]{lang="EN-US"}]{#struct_0_19016_79711_1906697467}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_924615027}

[[network-admin]{lang="EN-US"}]{#struct_0_19016_79711_x76783166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19016_79711_1129158240}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_19016_79711_1871435933}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_19016_79711_1216647765}[：显示用户态下指定私网内下一跳的配置信息，不指定该参数为公网内下一跳。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_721390002}[：]{style="font-family:宋体"}[显示用户态下指定单板指定私网内下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_1664412810}[：]{style="font-family:宋体"}[显示用户态下]{style="font-family:宋体"}[指定成员设备的]{style="font-family:宋体"}[指定私网内下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_19016_79711_2062124684}[：]{style="font-family:宋体"}[显示用户态下]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[指定私网内下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19016_79711_x1653654402}[：显示]{style="font-family:宋体"}[用户态下]{style="font-family:宋体"}[指定成员设备上指定单板]{style="font-family:宋体"}[的指定私网内下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_19016_79711_496040743}[：显示]{style="font-family:宋体"}[用户态下]{style="font-family:宋体"}[指定单板]{style="font-family:宋体"}[的指定私网内下一跳的配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_19016_79711_x269570822}[：显示用户态下指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上指定私网内下一跳的配置信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
