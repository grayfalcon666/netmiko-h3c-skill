::: {#-426089907 .myid}
[]{#_Toc337801703}[]{#_Toc341285955}[]{#_Toc337801706}[]{#_Toc338678038}[]{#_Toc404799579}[]{#struct_0_x4099_31656_x624003101}[]{#_Toc341285956}[]{#_Toc132011605}[]{#_Toc131910394}[]{#_Toc132011600}[]{#_Toc132011606}[]{#_Toc131910395}[]{#_Toc132011601}[]{#_Toc132011607}[]{#_Hlt7610771}[]{#_Hlt7610887}[]{#_Hlt24184665}[]{#_Toc138043182}[]{#_Toc94590060}[]{#_Toc209857781}[]{#_Toc209857782}[]{#_Toc209857783}[]{#_Toc209857784}[]{#_Toc209857785}[]{#_Toc209857786}[]{#_Toc209857787}[]{#_Toc209857788}[]{#_Toc209857789}[]{#_Toc209857790}[]{#_Toc209857791}[]{#_Toc209857792}[]{#_Toc209857793}[]{#_Toc209857795}[]{#_Toc209857798}[]{#_Toc209857805}[]{#_Toc209857811}[]{#_Toc209857814}[]{#_Toc209857821}[]{#_Toc209857826}[]{#_Toc209857827}[]{#_Toc209857885}[]{#_Toc338695701}[]{#_Toc341341442}[]{#_Toc341782286}[]{#_Toc341966873}[]{#_Toc338695706}[]{#_Toc341341447}[]{#_Toc341782290}[]{#_Toc341966877}[]{#_Toc163546333}[]{#_Toc166583084}[]{#_Toc163546358}[]{#_Toc166583109}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis import-route**

------------------------------------------------------------------------

[**[display system internal isis import-route]{lang="EN-US"}**]{#struct_0_x4099_31656_1214864964}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入路由表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x808226756}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4099_31656_x1107006180}

[**[display system internal isis import-route]{lang="EN-US"}**[ \[ **ipv4** \[ **topology** *topo-name* \] \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x4099_31656_x593045007}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x4099_31656_502900562}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal isis import-route]{lang="EN-US"}**[ \[ **ipv4** \[ **topology** *topo-name* \] \] \[ *process-id* \] \[ **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4099_31656_1375454477}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4099_31656_x323746068}[模式：]{style="font-family:宋体"}

[**[display system internal isis import-route]{lang="EN-US"}**[ \[ **ipv4** \[ **topology** *topo-name* \] \] \[ *process-id* \] \[ **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4099_31656_x1283188669}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x820149487}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_1981094464}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_364005860}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_1973542955}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x1462952553}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_725147889}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4099_31656_x343298186}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入路由表。如果不指定该参数，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入路由表。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x4099_31656_x1106547428}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4099_31656_1879750012}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程引入路由表。]{style="font-family:宋体"} [如果未指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程引入路由表。]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_x566222200}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[引入路由表]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[引入路由表]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_465111511}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[引入路由表]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的引入路由表。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_1745471654}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[引入路由表]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的引入路由表。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4099_31656_1248430917}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#661203541 .myid}
[]{#_Toc404799580}[]{#struct_0_x4099_31656_x443290571}[]{#_Toc360800098}[]{#_Toc360800099}[]{#_Toc360800100}[]{#_Toc360800101}[]{#_Toc360800102}[]{#_Toc360800103}[]{#_Toc360800104}[]{#_Toc360800105}[]{#_Toc360800106}[]{#_Toc360800107}[]{#_Toc360800108}[]{#_Toc360800109}[]{#_Toc360800110}[]{#_Toc360800111}[]{#_Toc360800133}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis interface**

------------------------------------------------------------------------

[**[display system internal isis interface]{lang="EN-US"}**]{#struct_0_x4099_31656_x1937043291}[命令用来显示接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x440391902}

[**[display system internal isis interface ]{lang="EN-US"}**[\[ **ipv4** \] \[ **vpn-instance** *vpn-instance-name* \] \[ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } \]]{lang="EN-US"}]{#struct_0_x4099_31656_x808554437}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x1384463442}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_1515044028}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x378415214}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_168190031}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_405108297}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_221587155}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4099_31656_1922138886}[：显示接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[信息。如果未指定该参数，显示接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x4099_31656_x1440950127}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x4099_31656_1149338338}[：接口类型和接口编号。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4099_31656_x737089324}[：接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制，显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和掩码]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码长度接口的信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x4099_31656_x808226757}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x4099_31656_x593110543}[：掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}
:::

::: {#-1271009205 .myid}
[]{#_Toc404799581}[]{#struct_0_x4099_31656_1999896059}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis interface standby**

------------------------------------------------------------------------

[**[display system internal isis interface standby]{lang="EN-US"}**]{#struct_0_x4099_31656_x1624555298}[命令用来显示接口的备份信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x852088106}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x4099_31656_x625568131}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal isis interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \] \[ **verbose** \] \[ *process-id* \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_x1905940975}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4099_31656_1111423315}[模式：]{style="font-family:宋体"}

[**[display system internal isis interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \] \[ **verbose** \] \[ *process-id* \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_x216160561}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_223072788}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_x791434590}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_1999306236}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x1260830199}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_1686062653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x1914073536}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4099_31656_148851570}[：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4099_31656_779926998}[：显示接口的详细信息。如果未指定该参数，将显示接口的概要信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4099_31656_949626233}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示与指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程相关联接口的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的接口信息。]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_1095011646}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_x1246698474}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_x1361814738}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4099_31656_229483492}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-794511174 .myid}
[]{#_Toc404799582}[]{#struct_0_x4099_31656_1999371772}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis lsdb standby**

------------------------------------------------------------------------

[**[display system internal isis lsdb standby]{lang="EN-US"}**]{#struct_0_x4099_31656_333636660}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的备份链路状态数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_912401154}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x4099_31656_1029948935}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal isis lsdb]{lang="EN-US"}**[ \[ \[ **level-1** \| **level-2** \] \| **local** \| \[ **lsp-id** *lspid* \| **lsp-name** *lspname* \] \| **verbose** \] \* \[ *process-id* \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_895604624}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4099_31656_x1828683012}[模式：]{style="font-family:宋体"}

[**[display system internal isis lsdb]{lang="EN-US"}**[ \[ \[ **level-1** \| **level-2** \] \| **local** \| \[ **lsp-id** *lspid* \| **lsp-name** *lspname* \] \| **verbose** \] \* \[ *process-id* \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_121751325}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x2071877970}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_x1985523371}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_202017371}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_1999437308}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x2026648380}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_435535550}

[**[level-1]{lang="EN-US"}**]{#struct_0_x4099_31656_x1169241880}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[链路状态数据库。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x4099_31656_x1820312542}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[链路状态数据库。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x4099_31656_x1892805545}[：显示当前路由器产生的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[lsp-id]{lang="EN-US"}***[ lspid]{lang="EN-US"}*]{#struct_0_x4099_31656_1281349005}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[标识，形式为]{style="font-family:宋体"}[SYSID*.*Pseudonode ID-fragment num]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[SYSID]{lang="EN-US"}[是]{style="font-family:宋体"}[产生该]{style="font-family:宋体"}[LSP]{lang="EN-GB"}[的节点或伪节点的]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[，]{style="font-family:宋体"}[Pseudonode ID]{lang="EN-US"}[是伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[fragment num]{lang="EN-US"}[是该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片号。]{style="font-family:宋体"}

[**[lsp-name]{lang="EN-US"}***[ lspname]{lang="EN-US"}*]{#struct_0_x4099_31656_718751576}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[名称，形式为]{style="font-family:宋体"}[Symbolic name.\[Pseudo ID\]-fragment num]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4099_31656_654877782}[：显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的详细信息。如果未指定该参数，将显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4099_31656_573562436}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的链路状态数据库信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的链路状态数据库信息。]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_1163342450}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[链路状态数据库信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_1999502844}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[链路状态数据库信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_1855680208}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[链路状态数据库信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4099_31656_x1886968625}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1661134554 .myid}
[]{#_Toc338678039}[]{#_Toc404799583}[]{#struct_0_x4099_31656_1399131995}[]{#_Toc341285957}[]{#_Toc360800135}[]{#_Toc360800136}[]{#_Toc360800137}[]{#_Toc360800138}[]{#_Toc360800139}[]{#_Toc360800140}[]{#_Toc360800141}[]{#_Toc360800142}[]{#_Toc360800143}[]{#_Toc360800144}[]{#_Toc360800145}[]{#_Toc360800146}[]{#_Toc360800147}[]{#_Toc360800148}[]{#_Toc360800149}[]{#_Toc360800150}[]{#_Toc360800151}[]{#_Toc360800152}[]{#_Toc360800153}[]{#_Toc360800154}[]{#_Toc360800155}[]{#_Toc360800156}[]{#_Toc360800157}[]{#_Toc360800158}[]{#_Toc360800159}[]{#_Toc360800160}[]{#_Toc360800161}[]{#_Toc360800162}[]{#_Toc360800163}[]{#_Toc360800164}[]{#_Toc360800165}[]{#_Toc360800166}[]{#_Toc360800167}[]{#_Toc360800168}[]{#_Toc360800169}[]{#_Toc360800170}[]{#_Toc360800171}[]{#_Toc360800172}[]{#_Toc360800173}[]{#_Toc360800174}[]{#_Toc360800175}[]{#_Toc360800176}[]{#_Toc360800177}[]{#_Toc360800178}[]{#_Toc360800179}[]{#_Toc360800180}[]{#_Toc360800181}[]{#_Toc360800182}[]{#_Toc360800183}[]{#_Toc360800184}[]{#_Toc360800185}[]{#_Toc360800186}[]{#_Toc360800187}[]{#_Toc360800188}[]{#_Toc360800249}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis nib**

------------------------------------------------------------------------

[**[display system internal isis nib]{lang="EN-US"}**]{#struct_0_x4099_31656_1596449772}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x265077068}

[**[display system internal isis nib]{lang="EN-US"}**[ \[ **ipv4** \] \[ *nib-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4099_31656_1699827867}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_742116421}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_2023638992}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_757201828}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x295143760}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x602421301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_453273084}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4099_31656_x1281621888}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[下一跳信息。如果不指定该参数，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[下一跳信息。]{style="font-family:宋体"}

[*[nib-id]{lang="EN-US"}*]{#struct_0_x4099_31656_1412175836}[：下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。如果不指定，显示所有下一跳信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4099_31656_x1189387562}[：显示下一跳详细信息。]{style="font-family:宋体"}
:::

::: {#-312816430 .myid}
[]{#_Toc404799584}[]{#struct_0_x4099_31656_x1957513762}[]{#_Toc341285958}[]{#_Toc360800251}[]{#_Toc360800252}[]{#_Toc360800253}[]{#_Toc360800254}[]{#_Toc360800255}[]{#_Toc360800256}[]{#_Toc360800257}[]{#_Toc360800258}[]{#_Toc360800259}[]{#_Toc360800260}[]{#_Toc360800261}[]{#_Toc360800262}[]{#_Toc360800263}[]{#_Toc360800264}[]{#_Toc360800265}[]{#_Toc360800266}[]{#_Toc360800267}[]{#_Toc360800321}[]{#_Toc360800322}[]{#_Toc360800323}[]{#_Toc360800324}[]{#_Toc360800325}[]{#_Toc360800326}[]{#_Toc360800327}[]{#_Toc360800328}[]{#_Toc360800329}[]{#_Toc360800330}[]{#_Toc360800331}[]{#_Toc360800332}[]{#_Toc360800333}[]{#_Toc360800334}[]{#_Toc360800335}[]{#_Toc360800336}[]{#_Toc360800337}[]{#_Toc360800338}[]{#_Toc360800339}[]{#_Toc360800340}[]{#_Toc360800341}[]{#_Toc360800342}[]{#_Toc360800343}[]{#_Toc360800344}[]{#_Toc360800345}[]{#_Toc360800346}[]{#_Toc360800347}[]{#_Toc360800348}[]{#_Toc360800349}[]{#_Toc360800350}[]{#_Toc360800351}[]{#_Toc360800352}[]{#_Toc360800353}[]{#_Toc360800402}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis nib log**

------------------------------------------------------------------------

[**[display system internal isis nib log]{lang="EN-US"}**]{#struct_0_x4099_31656_1669235362}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由下一跳日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x829580522}

[**[display system internal isis nib log]{lang="EN-US"}**]{#struct_0_x4099_31656_757463973}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x413269782}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_1495269936}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_1693400953}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_68376613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_520982488}
:::

::: {#-910228773 .myid}
[]{#_Toc404799585}[]{#struct_0_x4099_31656_1999109628}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis peer standby**

------------------------------------------------------------------------

[**[display system internal isis peer standby]{lang="EN-US"}**]{#struct_0_x4099_31656_x1978056935}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的备份邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x1493876780}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x4099_31656_1999175164}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system internal isis** **peer** \[ **statistics** \| **verbose** \] \[ *process-id* \] **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_x1253525919}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4099_31656_x404225723}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system internal** **isis** **peer** \[ **statistics** \| **verbose** \] \[ *process-id* \] **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_x1114097723}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_499677803}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_x252797132}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_715768434}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_799356917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x774757096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_555305391}

[**[statistics]{lang="EN-US"}**]{#struct_0_x4099_31656_1999240700}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的统计信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4099_31656_x1238673169}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的详细信息。如果未指定该参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的概要信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4099_31656_1420355076}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的邻居信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的邻居信息。]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_x703474127}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_x162151473}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_614831447}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4099_31656_1280922439}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1865794386 .myid}
[]{#_Toc404799586}[]{#struct_0_x4099_31656_x481270100}[]{#_Toc360800404}[]{#_Toc360800405}[]{#_Toc360800406}[]{#_Toc360800407}[]{#_Toc360800408}[]{#_Toc360800409}[]{#_Toc360800410}[]{#_Toc360800411}[]{#_Toc360800412}[]{#_Toc360800413}[]{#_Toc360800414}[]{#_Toc360800415}[]{#_Toc360800416}[]{#_Toc360800417}[]{#_Toc360800418}[]{#_Toc360800419}[]{#_Toc360800420}[]{#_Toc360800421}[]{#_Toc360800422}[]{#_Toc360800423}[]{#_Toc360800424}[]{#_Toc360800425}[]{#_Toc360800426}[]{#_Toc360800427}[]{#_Toc360800428}[]{#_Toc360800429}[]{#_Toc360800430}[]{#_Toc360800431}[]{#_Toc360800432}[]{#_Toc360800433}[]{#_Toc360800434}[]{#_Toc360800435}[]{#_Toc360800436}[]{#_Toc360800437}[]{#_Toc360800438}[]{#_Toc360800439}[]{#_Toc360800440}[]{#_Toc360800441}[]{#_Toc360800493}[]{#_Toc341285951}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis prefix**

------------------------------------------------------------------------

[**[display system internal isis prefix]{lang="EN-US"}**]{#struct_0_x4099_31656_170935368}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_757595042}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4099_31656_x1106744036}

[**[display system internal isis prefix ]{lang="EN-US"}**[\[ **ipv4** \[ **topology** *topo-name* \] \] \[ \[ **level-1** \| **level-2** \] \| \[ *prefix mask-length* \] \] \* \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x4099_31656_1503861863}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x4099_31656_822915218}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal isis prefix ]{lang="EN-US"}**[\[ **ipv4** \[ **topology** *toponame* \] \] \[ \[ **level-1** \| **level-2** \] \| \[ *prefix mask-length* \] \] \* \[ *process-id* \] \[ **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4099_31656_29439686}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4099_31656_286513287}[模式：]{style="font-family:宋体"}

[**[display system internal isis prefix ]{lang="EN-US"}**[\[ **ipv4** \[ **topology** *toponame* \] \] \[ \[ **level-1** \| **level-2** \] \| \[ *prefix mask-length* \] \] \* \[ *process-id* \] \[ **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4099_31656_57028633}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_1223792514}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_x348971850}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x99973557}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x2012445672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_1047242509}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_497900258}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4099_31656_445253954}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀信息。如果不指定该参数，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x4099_31656_x1106285284}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x4099_31656_x627818382}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[前缀信息。如果未指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的前缀信息。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x4099_31656_757660578}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[前缀信息。如果未指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的前缀信息。]{style="font-family:宋体"}

[*[prefix mask-length]{lang="EN-US"}*]{#struct_0_x4099_31656_x996116445}[：显示指定前缀和掩码长度的前缀信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4099_31656_2036469460}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的前缀信息。如果未指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的前缀信息。]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_945624282}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_x1106350820}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4099_31656_2124277289}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[前缀信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4099_31656_1249151812}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-138070322 .myid}
[]{#_Toc404799587}[]{#struct_0_x4099_31656_1999896060}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis standby**

------------------------------------------------------------------------

[**[display system internal isis]{lang="EN-US"}**[ **standby**]{lang="EN-US"}]{#struct_0_x4099_31656_x1623965471}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的进程备份信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x1237303361}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x4099_31656_1207318740}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal isis ]{lang="EN-US"}**[\[ *process-id* \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_2062665953}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4099_31656_431263385}[模式：]{style="font-family:宋体"}

[**[display system internal isis ]{lang="EN-US"}**[\[ *process-id* \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x4099_31656_x461925612}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_1999306233}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_x1261026807}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_872582944}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x598841369}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x840453621}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x197813067}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4099_31656_792578262}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的进程信息。]{style="font-family:宋体"}[如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[进程]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_x1187249463}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[进程]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_x1497017698}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[进程]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby ]{lang="EN-US"}**]{#struct_0_x4099_31656_23807491}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[进程]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4099_31656_2012231448}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-769526525 .myid}
[]{#_Toc404799588}[]{#struct_0_x4099_31656_x374167973}[]{#_Toc341777626}[]{#_Toc360800495}[]{#_Toc360800496}[]{#_Toc360800497}[]{#_Toc360800498}[]{#_Toc360800499}[]{#_Toc360800500}[]{#_Toc360800501}[]{#_Toc360800502}[]{#_Toc360800503}[]{#_Toc360800504}[]{#_Toc360800505}[]{#_Toc360800506}[]{#_Toc360800507}[]{#_Toc360800508}[]{#_Toc360800509}[]{#_Toc360800510}[]{#_Toc360800511}[]{#_Toc360800512}[]{#_Toc360800513}[]{#_Toc360800514}[]{#_Toc360800515}[]{#_Toc360800516}[]{#_Toc360800517}[]{#_Toc360800518}[]{#_Toc360800519}[]{#_Toc360800520}[]{#_Toc360800521}[]{#_Toc360800522}[]{#_Toc360800523}[]{#_Toc360800524}[]{#_Toc360800525}[]{#_Toc360800526}[]{#_Toc360800527}[]{#_Toc360800528}[]{#_Toc360800529}[]{#_Toc360800530}[]{#_Toc360800531}[]{#_Toc360800532}[]{#_Toc360800533}[]{#_Toc360800534}[]{#_Toc360800535}[]{#_Toc360800536}[]{#_Toc360800537}[]{#_Toc360800538}[]{#_Toc360800539}[]{#_Toc360800540}[]{#_Toc360800541}[]{#_Toc360800542}[]{#_Toc360800543}[]{#_Toc360800544}[]{#_Toc360800545}[]{#_Toc360800546}[]{#_Toc360800547}[]{#_Toc360800548}[]{#_Toc360800549}[]{#_Toc360800550}[]{#_Toc360800551}[]{#_Toc360800552}[]{#_Toc360800553}[]{#_Toc360800554}[]{#_Toc360800555}[]{#_Toc360800556}[]{#_Toc360800557}[]{#_Toc360800558}[]{#_Toc360800559}[]{#_Toc360800560}[]{#_Toc360800561}[]{#_Toc360800562}[]{#_Toc360800563}[]{#_Toc360800564}[]{#_Toc360800565}[]{#_Toc360800566}[]{#_Toc360800567}[]{#_Toc360800568}[]{#_Toc360800569}[]{#_Toc360800570}[]{#_Toc360800571}[]{#_Toc360800572}[]{#_Toc360800573}[]{#_Toc360800574}[]{#_Toc360800575}[]{#_Toc360800576}[]{#_Toc360800577}[]{#_Toc360800578}[]{#_Toc360800579}[]{#_Toc360800580}[]{#_Toc360800581}[]{#_Toc360800582}[]{#_Toc360800583}[]{#_Toc360800584}[]{#_Toc360800585}[]{#_Toc360800586}[]{#_Toc360800587}[]{#_Toc360800588}[]{#_Toc360800589}[]{#_Toc360800590}[]{#_Toc360800591}[]{#_Toc360800592}[]{#_Toc360800593}[]{#_Toc360800594}[]{#_Toc360800595}[]{#_Toc360800596}[]{#_Toc360800597}[]{#_Toc360800598}[]{#_Toc360800599}[]{#_Toc360800600}[]{#_Toc360800601}[]{#_Toc360800602}[]{#_Toc360800603}[]{#_Toc360800604}[]{#_Toc360800605}[]{#_Toc360800606}[]{#_Toc360800607}[]{#_Toc360800608}[]{#_Toc360800609}[]{#_Toc360800610}[]{#_Toc360800611}[]{#_Toc360800612}[]{#_Toc360800613}[]{#_Toc360800614}[]{#_Toc360800615}[]{#_Toc360800616}[]{#_Toc360800617}[]{#_Toc360800618}[]{#_Toc360800619}[]{#_Toc360800620}[]{#_Toc360800621}[]{#_Toc360800622}[]{#_Toc360800623}[]{#_Toc360800624}[]{#_Toc360800625}[]{#_Toc360800626}[]{#_Toc360800627}[]{#_Toc360800628}[]{#_Toc360800629}[]{#_Toc360800630}[]{#_Toc360800631}[]{#_Toc360800695}

**IS-IS \-- IS-IS probe命令 \-- display system internal isis status**

------------------------------------------------------------------------

[**[display system internal isis status]{lang="EN-US"}**]{#struct_0_x4099_31656_1667647742}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的协议全局状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x1787853886}

[**[display system internal isis status]{lang="EN-US"}**]{#struct_0_x4099_31656_x127969654}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4099_31656_x1811145939}

[[Probe]{lang="EN-US"}]{#struct_0_x4099_31656_x1312892550}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4099_31656_652678106}

[[network-admin]{lang="EN-US"}]{#struct_0_x4099_31656_x2106226196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4099_31656_757922723}

[]{#_Toc338695712}[]{#_Toc341341453}[]{#_Toc341782298}[]{#_Toc341966885}[]{#_Hlt9932878}[]{#_Toc328662275}[]{#_Toc328662276}[]{#_Toc328662277}[]{#_Toc328662278}[]{#_Toc328662279}[]{#_Toc328662280}[]{#_Toc328662281}[]{#_Toc328662282}[]{#_Toc328662283}[]{#_Toc328662284}[]{#_Toc328662285}[]{#_Toc328662286}[]{#_Toc328662287}[]{#_Toc328662288}[]{#_Toc328662289}[]{#_Toc328662290}[]{#_Toc328662291}[]{#_Toc328662292}[]{#_Toc328662293}[]{#_Toc328662294}[]{#_Toc328662295}[]{#_Toc328662296}[]{#_Toc328662297}[]{#_Toc328662298}[]{#_Toc328662299}[]{#_Toc328662300}[]{#_Toc163546251}[]{#_Toc50204095}[]{#_Toc33866094}[]{#_Toc17101067}[]{#_Toc302996860}[]{#_Toc252200747}[]{#_Toc199911156}[]{#_Toc193268606}[]{#_Toc193268506}[]{#_Toc193260336}[]{#_Toc131910356}[]{#_Toc132011562}[]{#_Toc302996870}[]{#_Toc290911758}[]{#_Hlt9926332}[]{#_Toc131842023}[]{#_Toc131842774}[]{#_Toc131842024}[]{#_Toc131842775}[]{#_Toc131842025}[]{#_Toc131842776}[]{#_Toc290911762}[]{#_Toc167021737}[]{#_Toc167021738}[]{#_Hlt9930022}[]{#_Toc308430274}[]{#_Toc252200778}[]{#_Hlt9849512}[]{#_Hlt9848777}[]{#_Hlt9934657}[]{#_Toc269462885}[]{#_Hlt12072832}[ ]{lang="EN-US"}
:::
