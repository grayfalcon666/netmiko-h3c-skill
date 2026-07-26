::: {#-326271838 .myid}
[]{#_Toc404798687}[]{#struct_0_x2083_18752_1220882886}[]{#_Toc380745932}[]{#_Toc380654408}[]{#_Toc324497564}[]{#_Toc313525668}[]{#_Toc298766608}[]{#_Toc272768853}[]{#_Toc33096882}

**ASPF \-- ASPF Probe命令 \-- display system internal aspf statistics**

------------------------------------------------------------------------

[**[display system internal aspf statistics]{lang="EN-US"}**]{#struct_0_x2083_18752_x1353966570}[命令用来查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[、报文过滤以及对象策略模块的丢包统计信息]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2083_18752_1753881133}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2083_18752_x147411088}

[**[display system internal aspf statistics]{lang="EN-US"}**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** }]{lang="EN-US"}]{#struct_0_x2083_18752_x1305508367}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2083_18752_1951589889}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal aspf statistics]{lang="EN-US"}**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2083_18752_1673352371}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2083_18752_x1016390048}[模式：]{style="font-family:宋体"}

[**[display system internal aspf statistics]{lang="EN-US"}**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } \[ ]{lang="EN-US"}]{#struct_0_x2083_18752_942827664}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2083_18752_x2018285448}

[[Probe]{lang="EN-US"}]{#struct_0_x2083_18752_x1023002093}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2083_18752_x1968500019}

[[network-admin]{lang="EN-US"}]{#struct_0_x2083_18752_x1561034366}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2083_18752_x647822558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2083_18752_82716824}

[**[interface]{lang="EN-US"}**]{#struct_0_x2083_18752_686362439}[：查看接口上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢包统计信息。]{style="font-family:宋体"}

[**[zone-pair]{lang="EN-US"}**]{#struct_0_x2083_18752_30003302}[：查看域间实例上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢包统计信息。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x2083_18752_x1330310166}[：]{style="font-family:宋体"} [查看]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文的丢包统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x2083_18752_x1176758238}[：]{style="font-family:宋体"} [查看]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的丢包统计信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2083_18752_x35015198}[：显示指定单板上的]{style="font-family:宋体"}[丢包统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则表示显示所有单板上的]{style="font-family:宋体"}[丢包统计信息。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2083_18752_x2074903197}[：显示指定成员设备上的丢包统计信息，]{style="font-family:宋体"}*[s]{lang="EN-US"}[lot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若不指定该参数，则表示显示所有成员设备上的丢包统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2083_18752_1030052088}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的丢包统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的丢包统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2083_18752_x1413755866}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[丢包统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[若不指定该参数，则表示显示所有成员设备的所有单板上的丢包统计表项信息。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2083_18752_1627782729}[：]{style="font-family:宋体"}[显示指定单板上的丢包统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示显示所有单板上的丢包统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2083_18752_x1288827181}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的丢包统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1301483311 .myid}
[]{#_Toc404798688}[]{#struct_0_x2083_18752_x169064153}[]{#_Toc380745933}[]{#_Toc380654409}

**ASPF \-- ASPF Probe命令 \-- reset system internal aspf statistics**

------------------------------------------------------------------------

[**[reset system internal aspf statistics]{lang="EN-US"}**]{#struct_0_x2083_18752_566031047}[命令用来清除]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[、报文过滤以及对象策略模块的丢包统计信息]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2083_18752_1708671715}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2083_18752_x174024637}

[**[reset system internal aspf statistics]{lang="EN-US"}**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** }]{lang="EN-US"}]{#struct_0_x2083_18752_x1345465336}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2083_18752_x122361300}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal aspf statistics]{lang="EN-US"}**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2083_18752_380794258}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2083_18752_1560686867}[模式：]{style="font-family:宋体"}

[**[reset system internal aspf statistics]{lang="EN-US"}**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } \[ ]{lang="EN-US"}]{#struct_0_x2083_18752_47451941}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2083_18752_x581148407}

[[Probe]{lang="EN-US"}]{#struct_0_x2083_18752_1185456014}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2083_18752_30068838}

[[network-admin]{lang="EN-US"}]{#struct_0_x2083_18752_x108355768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2083_18752_x1712113650}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2083_18752_473100653}

[**[interface]{lang="EN-US"}**]{#struct_0_x2083_18752_647894754}[：]{style="font-family:宋体"}[清除接口上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢包统计信息。]{style="font-family:宋体"}

[**[zone-pair]{lang="EN-US"}**]{#struct_0_x2083_18752_x928489676}[：]{style="font-family:宋体"}[清除域间实例上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[丢包统计信息。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x2083_18752_x1480123696}[：清除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文的丢包统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x2083_18752_x1616449663}[：清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的丢包统计信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2083_18752_x1424323308}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定单板上的]{style="font-family:宋体"}[丢包统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若不指定该参数，则表示]{style="font-family:宋体"}[清除]{style="font-family:
宋体"}[所有单板上的]{style="font-family:宋体"}[丢包统计信息。]{style="font-family:
宋体"}[（分布式设备]{style="font-family:宋体"}[－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2083_18752_x1352904478}[：清除指定成员设备上的丢包统计信息，]{style="font-family:宋体"}*[s]{lang="EN-US"}[lot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若不指定该参数，则表示清除所有成员设备上的丢包统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2083_18752_x1248492573}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的丢包统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若不指定该参数，则表示清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的丢包统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2083_18752_1383105793}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定成员设备的指定单板上的]{style="font-family:宋体"}[丢包统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[若不指定该参数，则表示清除所有成员设备的所有单板上的丢包统计表项信息。]{style="font-family:宋体"}[（分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2083_18752_1480390782}[：]{style="font-family:宋体"}[清除指定单板上的丢包统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若不指定该参数，则表示清除所有单板上的丢包统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_x2083_18752_1511439955}[ *cpu-number*]{lang="EN-US"}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的丢包统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::
