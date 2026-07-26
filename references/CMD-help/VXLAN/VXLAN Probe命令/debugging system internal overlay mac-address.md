::: {#-44792535 .myid}
[]{#_Toc404800392}[]{#struct_0_69076_18124_2136262279}[]{#_Toc388346982}[]{#_Toc385922933}[]{#_Toc147393197}

**VXLAN \-- VXLAN Probe命令 \-- debugging system internal overlay mac-address**

------------------------------------------------------------------------

[**[debugging system internal overlay mac-address]{lang="EN-US"}**]{#struct_0_69076_18124_x1684868727}[命令用来打开]{style="font-family:宋体"}[Overlay MAC]{lang="EN-US"}[地址的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging system internal overlay mac-address]{lang="EN-US"}**]{#struct_0_69076_18124_x460325949}[命令用来关闭]{style="font-family:宋体"}[Overlay MAC]{lang="EN-US"}[地址的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_x112957458}

[**[debugging system internal overlay mac-address ]{lang="EN-US"}**[{ **all** \| **event** \| **hardware** \| **isis** }]{lang="EN-US"}]{#struct_0_69076_18124_x1528739942}

[**[undo debugging system internal overlay mac-address ]{lang="EN-US"}**[{ **all** \| **event** \| **hardware** \| **isis** }]{lang="EN-US"}]{#struct_0_69076_18124_1530129086}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_69076_18124_1907967280}

[[Overlay MAC]{lang="EN-US"}]{#struct_0_69076_18124_537624732}[地址的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_x446600374}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_2128482705}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_x1593634535}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_396463110}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_2136262278}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_x1684934263}

[**[all]{lang="EN-US"}**]{#struct_0_69076_18124_945657037}[：表示]{style="font-family:宋体"}[Overlay MAC]{lang="EN-US"}[地址的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_69076_18124_x858897775}[：表示]{style="font-family:宋体"}[Overlay MAC]{lang="EN-US"}[地址的事件调试信息开关。]{style="font-family:宋体"}

[**[hardware]{lang="EN-US"}**]{#struct_0_69076_18124_1383514829}[：表示]{style="font-family:宋体"}[Overlay MAC]{lang="EN-US"}[地址的下驱动调试信息开关。]{style="font-family:宋体"}

[**[isis]{lang="EN-US"}**]{#struct_0_69076_18124_x796571335}[：表示]{style="font-family:宋体"}[Overlay MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[相关调试信息开关。]{style="font-family:宋体"}
:::

::: {#-2033527992 .myid}
[]{#_Toc404800393}[]{#struct_0_69076_18124_x1813135216}[]{#_Toc376875432}

**VXLAN \-- VXLAN Probe命令 \-- display system internal multicast tunnel nexthop**

------------------------------------------------------------------------

[**[display system internel multicast tunnel nexthop]{lang="EN-US"}**]{#struct_0_69076_18124_x822278933}[命令用来显示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[组播隧道的下一跳表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_1096394123}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69076_18124_171256638}

[**[display ]{lang="EN-US"}[system internal multicast]{lang="EN-US"}**[ **tunnel nexthop** \[ *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| **mtunnel** *tunnel-number* \| **outgoing-interface** *interface-type interface-number* \] \*]{lang="EN-US"}]{#struct_0_69076_18124_x38998593}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69076_18124_x523531179}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[system internal multicast]{lang="EN-US"}**[ **tunnel nexthop** \[ *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| **mtunnel** *tunnel-number* \| **outgoing-interface** *interface-type interface-number* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_69076_18124_117405144}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69076_18124_398517641}[模式：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[system internal multicast]{lang="EN-US"}**[ **tunnel nexthop** \[ *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| **mtunnel** *tunnel-number* \| **outgoing-interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \*]{lang="EN-US"}]{#struct_0_69076_18124_1243174920}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_x2106035895}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_x1256713192}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_1649555990}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_247719272}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_x1714541893}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_x2007660455}

[*[source-address]{lang="EN-US"}*]{#struct_0_69076_18124_398845321}[：源地址，这里指到达下一跳的出接口地址。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_69076_18124_576977624}[：组播组地址，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_69076_18124_x287506668}[：指定组播组地址或下一跳出接口地址的掩码长度。对于组播组地址，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；对于下一跳出接口地址，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_69076_18124_x826331645}[：指定组播组地址或下一跳出接口地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mtunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_69076_18124_54293910}[：显示指定组播隧道的下一跳表项。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为组播隧道的编号。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_69076_18124_x619997123}[：显示指定出接口的下一跳表项。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为出接口的接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1406318690}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_1942612734}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_495909671}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_239163995}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_768824429}[：显示指定成员设备上指定单板的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69076_18124_1076441856}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1821451171 .myid}
[]{#struct_0_69076_18124_2136262284}[]{#_Toc404800394}

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay arp suppression**

------------------------------------------------------------------------

[**[display system internal overlay arp suppression]{lang="EN-US"}**]{#struct_0_69076_18124_x1684147818}[命令用来显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_478037457}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69076_18124_957101238}

[**[display system internal overlay arp suppression vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}*]{#struct_0_69076_18124_x598524980}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69076_18124_1826879609}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal overlay arp suppression vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_403197003}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69076_18124_1246232272}[模式：]{style="font-family:宋体"}

[**[display system internal overlay arp suppression vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_x1227531549}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_x506086435}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_1666308534}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_x202389883}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_1118112380}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_x1557652536}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_1366785164}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_69076_18124_2139527800}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_93825772}*[slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_1842529899}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1070174270}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_1205034159}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_1658709085}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69076_18124_620164697}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#326058744 .myid}
[]{#_Toc404800395}[]{#struct_0_69076_18124_1673784944}[]{#_Toc388346987}

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay flooding**

------------------------------------------------------------------------

[**[display system internal overlay flooding]{lang="EN-US"}**]{#struct_0_69076_18124_x1031141619}[命令用来显示泛洪模式状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_x202389884}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69076_18124_1118308988}

[**[display system internal overlay flooding vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}*]{#struct_0_69076_18124_1878895128}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69076_18124_x528051758}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal overlay flooding vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_x294292213}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69076_18124_2141011020}[模式：]{style="font-family:宋体"}

[**[display system internal overlay flooding vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}]{#struct_0_69076_18124_x2108314638}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_x642553011}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_302226578}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_1783483731}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_2049704533}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_x58825525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_x202389885}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_69076_18124_1118243452}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的泛洪模式状态。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_1579984793}*[slot-number]{lang="EN-US"}*[：显示指定单板上的泛洪模式状态。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的泛洪模式状态。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_1182664274}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的泛洪模式状态。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的泛洪模式状态。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_2109047779}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的泛洪模式状态。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的泛洪模式状态。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_475679125}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的泛洪模式状态。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪模式状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1702136511}[：显示指定成员设备上指定单板的泛洪模式状态。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪模式状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1975346212}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1141066895 .myid}
[]{#_Toc404800396}[]{#struct_0_69076_18124_x709542490}[]{#_Toc388346988}[]{#_Toc376875433}[]{#_Toc371411818}

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay mac-address**

------------------------------------------------------------------------

[**[display system internal overlay mac-address]{lang="EN-US"}**]{#struct_0_69076_18124_x934148077}[命令用来显示远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_1646757603}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69076_18124_x340919187}

[**[display system internal overlay mac-address ]{lang="EN-US"}**[\[ **isis-learned** \| **static** \| **openflow** \] \[ **interface tunnel** *tunnel-number* \] \[ **vsi** *vsi-name* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_69076_18124_x340645074}

[**[display system internal overlay mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_69076_18124_x1050954816}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69076_18124_x202389886}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal overlay mac-address ]{lang="EN-US"}**[\[ **isis-learned** \| **static** \| **openflow** \] \[ **interface tunnel** *tunnel-number* \] \[ **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_69076_18124_1118440060}

[**[display system internal overlay mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_1941505183}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69076_18124_x1975851670}[模式：]{style="font-family:宋体"}

[**[display system internal overlay mac-address ]{lang="EN-US"}**[\[ **isis-learned** \| **static** \| **openflow** \] \[ **interface tunnel** *tunnel-number* \] \[ **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_69076_18124_1355085861}

[**[display system internal overlay mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_x1145184752}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_1654848948}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_1474873572}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_1701030047}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_x409787411}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_162877271}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_x1783096141}

[**[isis-learned]{lang="EN-US"}**]{#struct_0_69076_18124_x202389879}[：显示通过]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议学习的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_69076_18124_1118505595}[：显示远端静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[openflow]{lang="EN-US"}**]{#struct_0_69076_18124_x1173790116}[：显示通过]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[下发的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[interface tunnel]{lang="EN-US"}***[ tunnel-number]{lang="EN-US"}*]{#struct_0_69076_18124_1634385508}[：显示与指定]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道接口对应的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_69076_18124_x1391735242}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_69076_18124_x1686975152}[：显示远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量。如果指定本参数，则仅显示符合条件的（由]{style="font-family:宋体"}**[count]{lang="EN-US"}**[前面的参数决定）远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量，而不显示远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体内容。如果不指定本参数，则显示符合条件的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体内容。]{style="font-family:宋体"}

[*[mac]{lang="EN-US"}*[-]{lang="EN-US"}]{#struct_0_69076_18124_388082941}*[address]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[-]{lang="EN-US"}*[address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_x183943862}*[slot-number]{lang="EN-US"}*[：显示指定单板上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_x1416245074}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1829623621}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_1475594729}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x321873655}[：显示指定成员设备上指定单板的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69076_18124_2060846798}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1677425641 .myid}
[]{#_Toc404800397}[]{#struct_0_69076_18124_x1015479826}

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlay selective-flooding mac-address**

------------------------------------------------------------------------

[**[display system internal overlay selective-flooding mac-address]{lang="EN-US"}**]{#struct_0_69076_18124_x202389880}[命令用来显示泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_1118046844}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69076_18124_338423391}

[**[display system internal overlay selective-flooding mac-address ]{lang="EN-US"}**[\[ *mac-address* \] \[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_69076_18124_262601234}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69076_18124_x864808816}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal overlay selective-flooding mac-address ]{lang="EN-US"}**[\[ *mac-address* \] \[ **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_2048097519}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69076_18124_1087041615}[模式：]{style="font-family:宋体"}

[**[display system internal overlay selective-flooding mac-address ]{lang="EN-US"}**[\[ *mac-address* \] \[ **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_874048524}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_x1712980187}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_294395450}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_615080864}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_x809849496}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_x202389881}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_1117981308}

[*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}]{#struct_0_69076_18124_964398947}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_69076_18124_x952140738}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1598426619}[：显示指定单板的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主控板的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_265389289}[：显示指定成员设备的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x666824207}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1892995608}[：显示指定成员设备上指定单板的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_2062059148}[：显示指定成员设备上指定单板的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69076_18124_528769742}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-798054653 .myid}
[]{#_Toc404800398}[]{#struct_0_69076_18124_x2027830013}[]{#_Toc376875630}[]{#_Toc376875737}[]{#_Toc376875631}[]{#_Toc376875738}[]{#_Toc390071966}[]{#_Toc390071967}[]{#_Toc390071968}[]{#_Toc390071969}[]{#_Toc390071970}[]{#_Toc390071971}[]{#_Toc390071972}[]{#_Toc390071973}[]{#_Toc390071974}[]{#_Toc390071975}[]{#_Toc390071976}[]{#_Toc390071977}[]{#_Toc390071978}[]{#_Toc390071979}[]{#_Toc390071980}[]{#_Toc390071981}[]{#_Toc390071982}[]{#_Toc390071983}[]{#_Toc390071984}[]{#_Toc390071985}[]{#_Toc390071986}[]{#_Toc390071987}[]{#_Toc390071988}[]{#_Toc390071989}[]{#_Toc390071990}[]{#_Toc390071991}[]{#_Toc390071992}[]{#_Toc390071993}[]{#_Toc390071994}[]{#_Toc390071995}[]{#_Toc390071996}[]{#_Toc390071997}[]{#_Toc390071998}[]{#_Toc390071999}[]{#_Toc390072000}[]{#_Toc390072001}[]{#_Toc390072002}[]{#_Toc390072003}[]{#_Toc390072004}[]{#_Toc390072005}[]{#_Toc390072006}[]{#_Toc390072007}[]{#_Toc390072008}[]{#_Toc390072009}[]{#_Toc390072010}[]{#_Toc390072011}

**VXLAN \-- VXLAN Probe命令 \-- display system internal overlaymac statistics**

------------------------------------------------------------------------

[**[display system internal overlaymac statistics]{lang="EN-US"}**]{#struct_0_69076_18124_x1791747252}[命令用来显示]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_1887999501}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69076_18124_x910342642}

[**[display system internal overlaymac statistics]{lang="EN-US"}**]{#struct_0_69076_18124_x1272321782}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69076_18124_x202389882}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal overlaymac statistics]{lang="EN-US"}**[ * *\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_1118177916}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69076_18124_x53970526}[模式：]{style="font-family:宋体"}

[**[display system internal overlaymac statistics]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_1786026928}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_x152543063}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_646419611}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_371454343}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_1812242227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_734272559}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_774949811}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1533096380}[：显示指定单板的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主控板的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1235775623}[：显示指定成员设备的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_495975207}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x908896426}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_x1070108734}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69076_18124_x202389875}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#288718479 .myid}
[]{#_Toc404800399}[]{#struct_0_69076_18124_398910857}[]{#_Toc376875434}[]{#_Toc372102897}

**VXLAN \-- VXLAN Probe命令 \-- display system internal vxlan forwarding tunnel**

------------------------------------------------------------------------

[**[display system internal vxlan forwarding tunnel]{lang="EN-US"}**]{#struct_0_69076_18124_1023461888}[命令用来显示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道的转发信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_1411098623}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_69076_18124_1211804159}

[**[display system internal ]{lang="EN-US"}[vxlan forwarding tunnel]{lang="EN-US"}**[ \[ **vxlan-id** *vxlan-id* \]]{lang="EN-US"}]{#struct_0_69076_18124_1386141324}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_69076_18124_x672076820}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ]{lang="EN-US"}[vxlan forwarding tunnel]{lang="EN-US"}**[ \[ **vxlan-id** *vxlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_1721089342}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_69076_18124_464473430}[模式：]{style="font-family:宋体"}

[**[display system internal ]{lang="EN-US"}[vxlan forwarding tunnel]{lang="EN-US"}**[ \[ **vxlan-id** *vxlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_69076_18124_x1368695605}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_x1329840827}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_398714249}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_1948812692}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_x1730651745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_1778419473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_69076_18124_x9644307}

[**[vxlan-id]{lang="EN-US"}***[ vxlan-id]{lang="EN-US"}*]{#struct_0_69076_18124_1470579335}[：显示指定]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的隧道转发信息。]{style="font-family:宋体"}*[vxlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。不指定此参数，则显示所有]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的隧道转发信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_x1500112144}*[slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_x470174490}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_1658774621}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_69076_18124_398779785}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_69076_18124_2000441921}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_69076_18124_731172073}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道转发信息。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#485242948 .myid}
[]{#_Toc404800400}[]{#struct_0_69076_18124_x202389876}[]{#_Toc388346990}[]{#_Toc384042043}[]{#_Toc383786742}

**VXLAN \-- VXLAN Probe命令 \-- display system internal vxlan isis status**

------------------------------------------------------------------------

[**[display system internal vxlan isis status]{lang="EN-US"}**]{#struct_0_69076_18124_1118440059}[命令用来显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程的状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_1942095004}

[**[display system internal vxlan isis status]{lang="EN-US"}**]{#struct_0_69076_18124_x133765627}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_937139121}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_x2026119528}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_x362122645}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_1753925253}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_x538583835}
:::

::: {#-1552535676 .myid}
[]{#_Toc404800401}[]{#struct_0_69076_18124_1321817871}

**VXLAN \-- VXLAN Probe命令 \-- reset system internal overlaymac statistics**

------------------------------------------------------------------------

[**[reset system internal overlaymac statistics]{lang="EN-US"}**]{#struct_0_69076_18124_x365969854}[命令用来清除]{style="font-family:宋体"}[OverlayMAC]{lang="EN-US"}[模块的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_69076_18124_422506857}

[**[reset system internal overlaymac statistics]{lang="EN-US"}**]{#struct_0_69076_18124_x876166224}

[[【视图】]{style="font-family:黑体"}]{#struct_0_69076_18124_774946204}

[[Probe]{lang="EN-US"}]{#struct_0_69076_18124_x741588943}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_69076_18124_x163400182}

[[network-admin]{lang="EN-US"}]{#struct_0_69076_18124_1405755724}

[[mdc-admin]{lang="EN-US"}]{#struct_0_69076_18124_62876306}

[ ]{lang="EN-US"}
:::
