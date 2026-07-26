::: {#-1753972376 .myid}
[]{#_Toc404800247}[]{#struct_0_x1185_x1056_682709117}[]{#_Toc385322228}[]{#_Toc385316277}[]{#_Toc384382994}[]{#_Toc380570749}[]{#_Toc377734252}[]{#_Toc370721324}

**SMA \-- SMA Probe命令 \-- display system internal sma-anti-spoof ipv6 address-prefix**

------------------------------------------------------------------------

[**[display system internal sma-anti-spoof ipv6 address-prefix]{lang="EN-US"}**]{#struct_0_x1185_x1056_1667861237}[命令用来显示地址前缀信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_2126301025}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1185_x1056_x1799972007}

[**[display system internal sma-anti-spoof ipv6 address-prefix ]{lang="EN-US"}**[\[ *ipv6-address ipv6-prefix-length* \]]{lang="EN-US"}]{#struct_0_x1185_x1056_2106578435}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1185_x1056_1158003809}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal sma-anti-spoof ipv6 address-prefix ]{lang="EN-US"}**[\[ *ipv6-address ipv6-prefix-length* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1185_x1056_x977287360}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1185_x1056_x159627042}[模式：]{style="font-family:宋体"}

[**[display system internal sma-anti-spoof ipv6 address-prefix ]{lang="EN-US"}**[\[ *ipv6-address ipv6-prefix-length* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1185_x1056_x174314040}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_x1738419058}

[[Probe]{lang="EN-US"}]{#struct_0_x1185_x1056_1699892673}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_x787452299}

[[network-admin]{lang="EN-US"}]{#struct_0_x1185_x1056_1399479228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1185_x1056_x1854652744}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_x1613114866}

[*[ipv6-address ipv6-prefix-length]{lang="EN-US"}*]{#struct_0_x1185_x1056_x383447071}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀信息。]{style="font-family:宋体"}*[ipv6-prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1185_x1056_x1981504832}[：显示指定单板上的地址前缀信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的地址前缀信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1185_x1056_724909077}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的地址前缀信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的地址前缀信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_x1094530621}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的地址前缀信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的地址前缀信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x1185_x1056_x1806685615}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的地址前缀信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的地址前缀信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_1184014040}[：显示指定单板的地址前缀信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的地址前缀信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x1185_x1056_x1244031328}*[cpu-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的地址前缀信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1513541556 .myid}
[]{#_Toc404800248}[]{#struct_0_x1185_x1056_1321944867}[]{#_Toc385322229}[]{#_Toc385316278}[]{#_Toc384382995}[]{#_Toc380570750}[]{#_Toc377734253}[]{#_Toc386985660}[]{#_Toc386985661}[]{#_Toc386985662}[]{#_Toc386985663}[]{#_Toc386985664}[]{#_Toc386985665}[]{#_Toc386985666}[]{#_Toc386985667}[]{#_Toc386985668}[]{#_Toc386985687}

**SMA \-- SMA Probe命令 \-- display system internal sma-anti-spoof ipv6 packet-tag**

------------------------------------------------------------------------

[**[display system internal sma-anti-spoof ipv6 packet-tag]{lang="EN-US"}**]{#struct_0_x1185_x1056_52322383}[命令用来显示标签信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_x173593144}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1185_x1056_1120368383}

[**[display system internal sma-anti-spoof ipv6 packet-tag ]{lang="EN-US"}**[\[ *source-as-number destination-as-number* \]]{lang="EN-US"}]{#struct_0_x1185_x1056_1270864083}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1185_x1056_2089879155}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal sma-anti-spoof ipv6 packet-tag ]{lang="EN-US"}**[\[ *source-as-number destination-as-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1185_x1056_x81970767}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1185_x1056_1494107994}[模式：]{style="font-family:宋体"}

[**[display system internal sma-anti-spoof ipv6 packet-tag ]{lang="EN-US"}**[\[*source-as-number destination-as-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1185_x1056_x1489187550}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_976467545}

[[Probe]{lang="EN-US"}]{#struct_0_x1185_x1056_11057205}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_x1208544212}

[[network-admin]{lang="EN-US"}]{#struct_0_x1185_x1056_x1185438547}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1185_x1056_x670422402}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1185_x1056_x114365516}

[*[source-as-number destination-as-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_x173658680}[：显示指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[对的标签信息。]{style="font-family:宋体"}*[source-as-number]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，]{style="font-family:宋体"}*[destination-as-number]{lang="EN-US"}*[表示目的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[对的标签信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1185_x1056_764632561}[：显示指定单板上的标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的标签信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_816499740}[：显示指定成员设备的标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的标签信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_827849216}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的标签信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_1597742777}[：显示指定成员设备上指定单板的标签信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的标签信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_358430556}[：显示指定单板的标签信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的标签信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1185_x1056_x234787058}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的标签信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::
