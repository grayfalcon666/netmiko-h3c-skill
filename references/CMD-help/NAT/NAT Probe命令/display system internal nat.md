::: {#-1178655554 .myid}
[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc139515317}[]{#_Toc137103150}[]{#_Toc404799970}[]{#struct_0_x1279_x1958_376227771}[]{#_Toc357086029}[]{#_Toc351728019}

**NAT \-- NAT Probe命令 \-- display system internal nat**

------------------------------------------------------------------------

[**[display system internal nat]{lang="EN-US"}**]{#struct_0_x1279_x1958_2097707845}[命令用来显示内核的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_568574124}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1279_x1958_1721883571}

[**[display system internal nat]{lang="EN-US"}**]{#struct_0_x1279_x1958_565122272}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x1279_x1958_962013974}[－]{style="font-size:10.0pt;
font-family:宋体;color:black"}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal nat slot ]{lang="EN-US"}***[sl]{lang="EN-US"}[ot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1279_x1958_x1270846657}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x1279_x1958_1086098551}[－]{style="font-size:10.0pt;
font-family:宋体;color:black"}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display system internal nat chassis ]{lang="EN-US"}***[chassis]{lang="EN-US"}[-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1279_x1958_1244975773}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_x1894128415}

[[Probe]{lang="EN-US"}]{#struct_0_x1279_x1958_189950746}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_x628962145}

[[network-admin]{lang="EN-US"}]{#struct_0_x1279_x1958_x634918162}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1279_x1958_x1018722355}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_x678302477}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1279_x1958_1282665324}[：显示指定单板的内核的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息，]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备]{lang="EN-US" style="font-family:宋体"}[－]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:black"}[独立运行模式）]{lang="EN-US" style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1279_x1958_1314766389}[：显示指定成员设备的内核的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息，]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{lang="EN-US" style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{lang="EN-US" style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1279_x1958_896096504}[：显示指定成员设备]{lang="EN-US" style="font-family:宋体"}[/PEX]{lang="EN-US"}[的内核的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息，]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{lang="EN-US" style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1279_x1958_x230429198}[：]{lang="EN-US" style="font-family:宋体"}[显示指定成员设备上指定单板的]{lang="EN-US" style="font-family:
宋体"}[内核的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息，]{lang="EN-US" style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{lang="EN-US" style="font-family:宋体"}[所]{style="font-family:宋体"}[在的槽位号。]{lang="EN-US" style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;font-family:
宋体;color:black"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:
宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1279_x1958_x1382448157}[：]{lang="EN-US" style="font-family:宋体"}[显示指定单板的]{lang="EN-US" style="font-family:
宋体"}[内核的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[配置信息，]{lang="EN-US" style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{lang="EN-US" style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{lang="EN-US" style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{lang="EN-US" style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-size:10.0pt;font-family:
宋体;color:black"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:
宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_x1279_x1958_303239895}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的内核的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置]{lang="EN-US" style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的具体型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::::: {#1350624179 .myid}
[]{#_Toc377715682}[]{#_Toc377053893}[]{#_Toc404799971}[]{#struct_0_x1279_x1958_460742145}[]{#_Toc377715683}[]{#_Toc377053894}

**NAT \-- NAT Probe命令 \-- display system internal nat controller**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NAT%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1279_x1958_x1715895288}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1279_x1958_x1543612684}
:::

[ ]{lang="EN-US"}

[**[display system internal nat controller]{lang="EN-US"}**]{#struct_0_x1279_x1958_24687984}[命令用来显示处理]{style="font-family:宋体"}[NAT]{lang="EN-US"}[业务的引擎信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_x1523474729}

[**[display system internal nat controller]{lang="EN-US"}**]{#struct_0_x1279_x1958_485417824}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_1191097473}

[[Probe]{lang="EN-US"}]{#struct_0_x1279_x1958_1532611917}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_460807681}

[[network-admin]{lang="EN-US"}]{#struct_0_x1279_x1958_x1163069413}

[[network-operator]{lang="EN-US"}]{#struct_0_x1279_x1958_x2036686851}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1279_x1958_199649818}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1279_x1958_2107487065}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_411858364}

[[如果没有配置引流备份组，以引擎为单位显示所有引擎，如果配置了引擎备份组，则以备份组为单位显示所有备份组及其成员中的引擎。]{style="font-family:宋体"}]{#struct_0_x1279_x1958_1185976952}

[[每个双机热备备份组中包含两个引擎成员，主引擎负责处理所有的安全业务，当主引擎发生故障时，备引擎升级成主引擎。]{style="font-family:宋体"}]{#struct_0_x1279_x1958_402546566}
:::::

::::: {#-821314864 .myid}
[]{#_Toc404799972}[]{#struct_0_x1279_x1958_460873217}

**NAT \-- NAT Probe命令 \-- display system internal nat flow**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NAT%20Probe命令.files/image001.png){#图片 17 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1279_x1958_1606952472}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1279_x1958_x561956463}
:::

[ ]{lang="EN-US"}

[**[display system internal nat flow]{lang="EN-US"}**]{#struct_0_x1279_x1958_1622400328}[命令用来显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置相关的引流规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_1733309277}

[**[display system internal nat flow ]{lang="EN-US"}**[{ **all** \| **dynamic** \| **portblock**]{lang="EN-US"}]{#struct_0_x1279_x1958_x1865071237}[ ]{lang="EN-US"}[\| **server** \| **static** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_1680357005}

[[Probe]{lang="EN-US"}]{#struct_0_x1279_x1958_1184224613}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_461463041}

[[network-admin]{lang="EN-US"}]{#struct_0_x1279_x1958_1633874150}

[[network-operator]{lang="EN-US"}]{#struct_0_x1279_x1958_741425579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1279_x1958_x961001163}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1279_x1958_67409145}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_2011390159}

[**[all]{lang="EN-US"}**]{#struct_0_x1279_x1958_x814876676}[：显示所有]{style="font-family:宋体"}[NAT]{lang="EN-US"}[配置的引流规则。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_x1279_x1958_x965231532}[：显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[动态地址转换配置相关的引流规则。]{style="font-family:宋体"}

[**[server]{lang="EN-US"}**]{#struct_0_x1279_x1958_1373934906}[：显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[内部服务器配置相关的引流规则。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x1279_x1958_461528577}[：显示]{style="font-family:宋体"}[NAT]{lang="EN-US"}[静态地址转换配置相关的引流规则。]{style="font-family:宋体"}

[**[portblock]{lang="EN-US"}**]{#struct_0_x1279_x1958_34491949}[：显示]{style="font-family:宋体"}[NAT 444]{lang="EN-US"}[端口块映射配置相关的引流规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1279_x1958_1823826284}

[[多引擎环境下，为保证同一条流的正向报文和反向报文由同一个引擎处理，]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x1279_x1958_x829732438}[模块会在接口板下发相应的引流规则。]{style="font-family:宋体"}

[[引擎是多形态防火墙中用来处理安全业务的最小单元，存在于安全插卡（]{style="font-family:宋体"}]{#struct_0_x1279_x1958_x2041189708}[SecBlade]{lang="EN-US"}[）上。一个]{style="font-family:宋体"}[SecBlade]{lang="EN-US"}[上会有一个或者多个业务引擎，简称]{style="font-family:宋体"}[SPE]{lang="EN-US"}[，每个]{style="font-family:宋体"}[SPE]{lang="EN-US"}[之间相互独立，每个]{style="font-family:宋体"}[SPE]{lang="EN-US"}[由一个多核]{style="font-family:宋体"}[CPU]{lang="EN-US"}[组成。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::::
