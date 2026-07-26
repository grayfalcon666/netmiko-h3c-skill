::: {#1996851253 .myid}
[]{#_Toc404784727}[]{#struct_0_x8148_17965_1814743838}

**L2PT \-- L2PT配置命令 \-- display l2protocol statistics**

------------------------------------------------------------------------

[**[display l2protocol statistics]{lang="FR"}**]{#struct_0_x8148_17965_656385782}[命令用来显示]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x439588983}

[**[display l2protocol statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x8148_17965_1899267924}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x687878776}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x8148_17965_x663183212}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x2041516751}

[[network-admin]{lang="PT-BR"}]{#struct_0_x8148_17965_1043612001}

[[network-operator]{lang="PT-BR"}]{#struct_0_x8148_17965_x1223075234}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x8148_17965_206043459}

[[mdc-operator]{lang="FR"}]{#struct_0_x8148_17965_x1793123788}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8148_17965_140066324}

[**[interface]{lang="FR"}**]{#struct_0_x8148_17965_354004745}[ *interface-type* *interface-number*]{lang="FR"}[：]{style="font-family:宋体"}[显示指定二层以太网接口或二层聚合接口上的]{style="font-family:宋体"}[L2PT]{lang="FR"}[报文统计信息。]{style="font-family:宋体"}*[interface-type]{lang="FR"}*[ *interface-number*]{lang="FR"}[表示接口类型和接口编号。如未指定本参数，将显示所有二层以太网接和二层聚合接口的]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1170928713}

[[\# ]{lang="FR"}]{#struct_0_x8148_17965_541691657}[显示所有]{style="font-family:宋体"}[二层以太网接口和二层聚合接口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2protocol statistics]{lang="EN-US"}]{#struct_0_x8148_17965_x475432810}

[L2PT statistics information on interface Bridge-Aggregation1:]{lang="EN-US"}

[Protocol  Encapsulated      Decapsulated      Forwarded         Dropped]{lang="EN-US"}

[CDP       0                 0                 0                 0]{lang="EN-US"}

[DLDP      0                 3                 0                 0]{lang="EN-US"}

[EOAM      0                 2                 0                 0]{lang="EN-US"}

[GVRP      8                 4                 9                 2]{lang="EN-US"}

[LACP      0                 0                 0                 0]{lang="EN-US"}

[LLDP      0                 3                 0                 0]{lang="EN-US"}

[MVRP      0                 0                 0                 0]{lang="EN-US"}

[PAGP      0                 1                 0                 0]{lang="EN-US"}

[PVST      0                 0                 0                 0]{lang="EN-US"}

[STP       5                 5                 5                 0]{lang="EN-US"}

[Tunnel    N/A               N/A               100               10]{lang="EN-US"}

[VTP       0                 6                 0                 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[L2PT statistics information on interface GigabitEthernet1/0/1:]{lang="EN-US"}

[Protocol  Encapsulated      Decapsulated      Forwarded         Dropped]{lang="EN-US"}

[CDP       0                 0                 0                 0]{lang="EN-US"}

[DLDP      2                 3                 3                 0]{lang="EN-US"}

[EOAM      5                 2                 9                 0]{lang="EN-US"}

[GVRP      8                 4                 9                 2]{lang="EN-US"}

[LACP      0                 0                 0                 0]{lang="EN-US"}

[LLDP      3                 3                 3                 3]{lang="EN-US"}

[MVRP      0                 0                 0                 0]{lang="EN-US"}

[PAGP      5                 1                 7                 3]{lang="EN-US"}

[PVST      0                 0                 0                 0]{lang="EN-US"}

[STP       5                 5                 5                 0]{lang="EN-US"}

[Tunnel    N/A               N/A               100               10]{lang="EN-US"}

[VTP       0                 6                 0                 0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display l2protocol statistics]{lang="EN-US"}]{#struct_0_x8148_17965_572713908}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1798005737}[[字段]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1097909193}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x8148_17965_492180306}

[[Protocol]{lang="EN-US"}]{#struct_0_x8148_17965_x158237888}

[[协议类型]{style="font-family:宋体"}]{#struct_0_x8148_17965_989970850}

[[Encapsulated]{lang="EN-US"}]{#struct_0_x8148_17965_x1757752964}

[[封装统计计数]{style="font-family:宋体"}]{#struct_0_x8148_17965_x402143788}

[[用户侧收到协议报文后封装成]{style="font-family:宋体"}[BPDU Tunnel]{lang="EN-US"}]{#struct_0_x8148_17965_x1327596484}[报文，对应的协议封装统计计数加]{style="font-family:宋体"}[1]{lang="EN-US"}

[[对于]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x8148_17965_x990494156}[（表示]{style="font-family:宋体"}[BPDU Tunnel]{lang="EN-US"}[报文），对应值显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，为无效统计计数]{style="font-family:宋体"}

[[Decapsulated]{lang="EN-US"}]{#struct_0_x8148_17965_x307562348}

[[解封装统计计数]{style="font-family:宋体"}]{#struct_0_x8148_17965_1104349201}

[[网络侧收到]{style="font-family:宋体"}[BPDU Tunnel]{lang="EN-US"}]{#struct_0_x8148_17965_1090651131}[报文后解封装成协议报文，对应的协议解封装统计计数加]{style="font-family:宋体"}[1]{lang="EN-US"}

[[对于]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x8148_17965_x1383078963}[，对应值显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，为无效统计计数]{style="font-family:宋体"}

[[Forwarded]{lang="EN-US"}]{#struct_0_x8148_17965_x1388168970}

[[转发统计计数]{style="font-family:宋体"}]{#struct_0_x8148_17965_1475716729}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户侧或网络侧收到协议报文后转发，对应的协议转发统计计数加]{style="font-family:宋体"}]{#struct_0_x8148_17965_x1055068086}[1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[网络侧收到]{style="font-family:宋体"}]{#struct_0_x8148_17965_x1369317721}[BPDU Tunnel]{lang="EN-US"}[报文后转发，对应的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[转发统计计数加]{style="font-family:宋体"}[1]{lang="EN-US"}[（如果网络侧收到]{style="font-family:宋体"}[BPDU Tunnel]{lang="EN-US"}[报文时，设备没有任何用户侧端口，则]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[转发统计计数不会增加）]{style="font-family:宋体"}

[[Dropped]{lang="EN-US"}]{#struct_0_x8148_17965_x1366835649}

[[丢弃统计计数]{style="font-family:宋体"}]{#struct_0_x8148_17965_x1752487615}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口收到协议报文后丢弃，对应的协议丢弃统计计数加]{style="font-family:宋体"}]{#struct_0_x8148_17965_536395876}[1]{lang="EN-US"}[（如果协议报文被硬件丢弃，则协议丢弃统计计数不会增加）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口收到]{style="font-family:宋体"}]{#struct_0_x8148_17965_1292606691}[BPDU Tunnel]{lang="EN-US"}[报文后丢弃，对应的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[丢弃统计计数加]{style="font-family:宋体"}[1]{lang="EN-US"}

[ ]{lang="FR"}

::: {#-1480937880 .myid}
[]{#_Toc404784728}[]{#struct_0_x8148_17965_x1638232224}

**L2PT \-- L2PT配置命令 \-- l2protocol drop**

------------------------------------------------------------------------

[**[l2protocol drop]{lang="FR"}**]{#struct_0_x8148_17965_x1839122560}[命令用来使能指定协议的]{style="font-family:宋体"}[L2PT Drop]{lang="FR"}[功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即强制丢弃指定的协议报文。]{style="font-family:宋体"}

[**[undo l2protocol drop]{lang="FR"}**]{#struct_0_x8148_17965_x1117844057}[命令用来关闭指定协议的]{style="font-family:宋体"}[L2PT Drop]{lang="FR"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x646830834}

[[在二层]{style="font-family:宋体"}]{#struct_0_x8148_17965_2033193428}[以太网]{style="font-family:宋体"}[接口视图下：]{style="font-family:宋体"}

[**[l2protocol ]{lang="FR"}**]{#struct_0_x8148_17965_707755218}[{ **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **drop**]{lang="FR"}

[**[undo l2protocol ]{lang="FR"}**]{#struct_0_x8148_17965_313394204}[{ **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **drop**]{lang="FR"}

[[在二层聚合接口视图下：]{style="font-family:宋体"}]{#struct_0_x8148_17965_x1825770324}

[**[l2protocol]{lang="FR"}**]{#struct_0_x8148_17965_147082584}[ ]{lang="FR"}[{ **gvrp** \| **lldp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **drop**]{lang="FR"}

[**[undo l2protocol]{lang="FR"}**]{#struct_0_x8148_17965_1980928468}[ ]{lang="FR"}[{ **gvrp** \| **lldp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **drop**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1178390901}

[[各协议的]{style="font-family:宋体"}[L2PT Drop]{lang="EN-US"}]{#struct_0_x8148_17965_652490026}[功能均处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1172957437}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x8148_17965_1913567141}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1813022439}

[[network-admin]{lang="EN-US"}]{#struct_0_x8148_17965_x684461195}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8148_17965_x428378643}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x500390445}

[**[cdp]{lang="FR"}**]{#struct_0_x8148_17965_x1827278564}[：表示]{style="font-family:宋体"}[CDP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[dldp]{lang="FR"}**]{#struct_0_x8148_17965_1233210776}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[eoam]{lang="FR"}**]{#struct_0_x8148_17965_x572975778}[：表示]{style="font-family:宋体"}[EOAM]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[gvrp]{lang="FR"}**]{#struct_0_x8148_17965_1243177137}[：表示]{style="font-family:宋体"}[GVRP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[mvrp]{lang="FR"}**]{#struct_0_x8148_17965_989854895}[：表示]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[lacp]{lang="FR"}**]{#struct_0_x8148_17965_125948247}[：表示]{style="font-family:宋体"}[LACP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[lldp]{lang="FR"}**]{#struct_0_x8148_17965_288635732}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[pagp]{lang="FR"}**]{#struct_0_x8148_17965_1326958625}[：表示]{style="font-family:宋体"}[PAGP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[pvst]{lang="FR"}**]{#struct_0_x8148_17965_1128781711}[：表示]{style="font-family:宋体"}[PVST]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[stp]{lang="FR"}**]{#struct_0_x8148_17965_x27809765}[：表示]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[vtp]{lang="FR"}**]{#struct_0_x8148_17965_764430493}[：表示]{style="font-family:宋体"}[VTP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1772771203}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[允许在二层聚合组的成员端口上使能]{style="font-family:宋体"}]{#struct_0_x8148_17965_1472577546}[GVRP]{lang="FR"}[、]{style="font-family:宋体"}[MVRP]{lang="FR"}[、]{style="font-family:宋体"}[PVST]{lang="FR"}[、]{style="font-family:
宋体"}[STP]{lang="FR"}[和]{style="font-family:宋体"}[VTP]{lang="FR"}[协议的]{style="font-family:宋体"}[L2PT ]{lang="FR"}[Drop]{lang="FR"}[功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[但配置不生效。在二层聚合组的成员端口上使能]{style="font-family:宋体"}[CDP]{lang="FR"}[、]{style="font-family:宋体"}[DLDP]{lang="FR"}[、]{style="font-family:宋体"}[EOAM]{lang="FR"}[、]{style="font-family:
宋体"}[LACP]{lang="FR"}[、]{style="font-family:宋体"}[LLDP]{lang="FR"}[和]{style="font-family:宋体"}[PAGP]{lang="FR"}[协议的]{style="font-family:宋体"}[L2PT Drop]{lang="FR"}[功能会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[L2PT Drop]{lang="EN-US"}]{#struct_0_x8148_17965_x2065204377}[功能的优先级高于协议报文的处理优先级，因此，在接口上使能指定协议的]{style="font-family:
宋体"}[L2PT Drop]{lang="EN-US"}[功能时，不需要在当前接口关闭该协议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x8148_17965_1864682503}[LLDP]{lang="FR"}[协议]{style="font-family:宋体"}[，]{style="font-family:宋体"}[L2PT Drop]{lang="FR"}[功能支持所有的]{style="font-family:宋体"}[LLDP]{lang="FR"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[包括]{style="font-family:宋体"}[Nearest Bridge]{lang="FR"}[（]{style="font-family:宋体"}[最近桥代理]{style="font-family:宋体"}[）]{style="font-family:宋体"}[、]{style="font-family:宋体"}[Nearest Custome]{lang="FR"}[r Bridge]{lang="FR"}[（]{lang="EN-US" style="font-family:宋体"}[最近客户桥代理]{lang="EN-US" style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}[、]{lang="EN-US" style="font-family:宋体"}[Nearest non-TPMR Bridge]{lang="FR"}[（]{lang="EN-US" style="font-family:宋体"}[最近非]{lang="EN-US" style="font-family:宋体"}[TPMR]{lang="FR"}[桥代理]{lang="EN-US" style="font-family:宋体"}[）]{lang="EN-US" style="font-family:
宋体"}[类型的]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="FR"}[报文。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[l2protocol drop]{lang="EN-US"}**]{#struct_0_x8148_17965_1137705298}[与]{lang="EN-US" style="font-family:宋体"}**[l2protocol tunnel dot1q]{lang="EN-US"}**[命令会相互覆盖。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8148_17965_711380396}

[[\# ]{lang="EN-US"}]{#struct_0_x8148_17965_x1867346216}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[L2PT Drop]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8148_17965_x174127171}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] l2protocol stp drop]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x8148_17965_x955102978}[在二层聚合接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[L2PT Drop]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8148_17965_1063782603}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] l2protocol stp drop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1187003553}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[l2protocol tunnel dot1q]{lang="EN-US"}**]{#struct_0_x8148_17965_1849033434}
:::

::: {#486864975 .myid}
[]{#_Toc404784729}[]{#struct_0_x8148_17965_x1920479428}[]{#_Toc135901606}[]{#_Toc125895780}

**L2PT \-- L2PT配置命令 \-- l2protocol tunnel dot1q**

------------------------------------------------------------------------

[**[l2protocol]{lang="FR"}**]{#struct_0_x8148_17965_192831825}**[ tunnel ]{lang="FR"}[dot1q]{lang="EN-US"}**[命令用来使能]{style="font-family:
宋体"}[指定协议的]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x8148_17965_834197720}**[l2protocol]{lang="FR"}[ tunnel ]{lang="FR"}[dot1q]{lang="EN-US"}**[命令用来关闭指定协议的]{style="font-family:
宋体"}[L2PT]{lang="EN-US"}[功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1056761985}

[[在二层]{style="font-family:宋体"}]{#struct_0_x8148_17965_x750097804}[以太网]{style="font-family:宋体"}[接口视图下：]{style="font-family:宋体"}

[**[l2protocol ]{lang="FR"}**]{#struct_0_x8148_17965_410370407}[{ **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]{lang="FR"}

[**[undo l2protocol ]{lang="FR"}**]{#struct_0_x8148_17965_x1675959879}[{ **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]{lang="FR"}

[[在二层聚合接口视图下：]{style="font-family:宋体"}]{#struct_0_x8148_17965_x72213819}

[**[l2protocol ]{lang="FR"}**]{#struct_0_x8148_17965_1487250851}[{ **gvrp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]{lang="FR"}

[**[undo l2protocol]{lang="FR"}**]{#struct_0_x8148_17965_551712695}**[ ]{lang="FR"}**[{ **gvrp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x2089689806}

[[各协议的]{style="font-family:宋体"}[L2PT]{lang="EN-US"}]{#struct_0_x8148_17965_x518130270}[功能均处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1280299542}

[[二层]{style="font-family:宋体"}]{#struct_0_x8148_17965_1498236795}[以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1813364196}

[[network-admin]{lang="EN-US"}]{#struct_0_x8148_17965_x851611345}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8148_17965_1089240628}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x491227214}

[**[cdp]{lang="FR"}**]{#struct_0_x8148_17965_x1672046051}[：表示]{style="font-family:宋体"}[CDP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[dldp]{lang="FR"}**]{#struct_0_x8148_17965_x336884395}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[eoam]{lang="FR"}**]{#struct_0_x8148_17965_1305415858}[：表示]{style="font-family:宋体"}[EOAM]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[gvrp]{lang="FR"}**]{#struct_0_x8148_17965_x354063768}[：表示]{style="font-family:宋体"}[GVRP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[lacp]{lang="FR"}**]{#struct_0_x8148_17965_x789998638}[：表示]{style="font-family:宋体"}[LACP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[lldp]{lang="FR"}**]{#struct_0_x8148_17965_x1466916745}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[mvrp]{lang="FR"}**]{#struct_0_x8148_17965_1493870122}[：表示]{style="font-family:宋体"}[MVRP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[pagp]{lang="FR"}**]{#struct_0_x8148_17965_1742559143}[：表示]{style="font-family:宋体"}[PAGP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[pvst]{lang="FR"}**]{#struct_0_x8148_17965_x364618591}[：表示]{style="font-family:宋体"}[PVST]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[stp]{lang="FR"}**]{#struct_0_x8148_17965_1531280565}[：表示]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[vtp]{lang="FR"}**]{#struct_0_x8148_17965_1932793182}[：表示]{style="font-family:宋体"}[VTP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1821673805}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不支持在二层聚合接口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x8148_17965_x1485663889}[上使能]{style="font-family:宋体"}[CDP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[DLDP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[EOAM]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LACP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[PAGP]{lang="EN-US"}[协议的]{lang="EN-US" style="font-family:宋体"}[L2PT]{lang="EN-US"}[功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口上使能某协议的]{style="font-family:宋体"}]{#struct_0_x8148_17965_66042947}[L2PT]{lang="EN-US"}[功能时，对应的]{style="font-family:宋体"}[CE]{lang="EN-US"}[上应启用该协议，同时当前接口必须关闭该协议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[允许在二层聚合组的成员端口上使能]{style="font-family:宋体"}]{#struct_0_x8148_17965_325838258}[L2PT]{lang="EN-US"}[功能，但配置不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能在业务环回组的成员端口上]{style="font-family:宋体"}]{#struct_0_x8148_17965_1843278592}[使能]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x8148_17965_x785258265}[协议，]{lang="EN-US" style="font-family:宋体"}[L2PT]{lang="EN-US"}[功能只支持]{lang="EN-US" style="font-family:宋体"}[Nearest Bridge]{lang="EN-US"}[（最近桥代理）类型的]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[l2protocol tunnel dot1q]{lang="EN-US"}**]{#struct_0_x8148_17965_x1591763095}[与]{lang="EN-US" style="font-family:宋体"}**[l2protocol drop]{lang="EN-US"}**[命令会相互覆盖。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1542637980}

[]{#_Toc153192140}[[\# ]{lang="EN-US"}]{#struct_0_x8148_17965_1606931134}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上关闭]{style="font-family:宋体"}[STP]{lang="FR"}[协议，并使能]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8148_17965_604804958}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo stp enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="EN-US"}[l2protocol stp tunnel dot1q]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_x8148_17965_643645388}[在二层聚合接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="EN-US"}[上关闭]{style="font-family:宋体"}[STP]{lang="FR"}[协议]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并使能]{style="font-family:宋体"}[STP]{lang="FR"}[协议的]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8148_17965_x1235013233}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] undo stp enable]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] ]{lang="EN-US"}[l2protocol stp tunnel dot1q]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1948465588}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[l2protocol drop]{lang="EN-US"}**]{#struct_0_x8148_17965_x1744509559}
:::

::: {#1595572264 .myid}
[]{#_Toc404784730}[]{#struct_0_x8148_17965_1307878166}

**L2PT \-- L2PT配置命令 \-- l2protocol tunnel-dmac**

------------------------------------------------------------------------

[**[l2protocol tunnel-dmac]{lang="EN-US"}**]{#struct_0_x8148_17965_x1294678080}[命令用来配置]{style="font-family:宋体"}[BPDU Tunnel]{lang="EN-US"}[报文的组播目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo l2protocol tunnel-dmac]{lang="EN-US"}**]{#struct_0_x8148_17965_x88028146}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8148_17965_193902813}

[**[l2protocol tunnel-dmac ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_x8148_17965_972339700}

[**[undo l2protocol tunnel-dmac]{lang="EN-US"}**]{#struct_0_x8148_17965_1164107119}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1101102101}

[[BPDU Tunnel]{lang="EN-US"}]{#struct_0_x8148_17965_x1604576441}[报文的组播目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[010F-E200-0003]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1392380561}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x8148_17965_489773262}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1208263977}

[[network-admin]{lang="PT-BR"}]{#struct_0_x8148_17965_x284016627}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x8148_17965_331070708}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x1163234983}

[*[mac]{lang="FR"}*]{#struct_0_x8148_17965_1212712977}[-*address*]{lang="FR"}[：]{style="font-family:宋体"}[BPDU Tunnel]{lang="FR"}[报文的组播目的]{style="font-family:宋体"}[MAC]{lang="FR"}[地址]{style="font-family:宋体"}[。]{style="font-family:
宋体"}[取值可以为下列]{style="font-family:宋体"}[MAC]{lang="FR"}[地址之一]{style="font-family:宋体"}[：]{style="font-family:宋体"}[0100-0CCD-CDD0]{lang="FR"}[、]{style="font-family:宋体"}[0100-0CCD-CDD1]{lang="FR"}[、]{style="font-family:宋体"}[0100-0CCD-CDD2]{lang="FR"}[或]{style="font-family:宋体"}[010F-E200-0003]{lang="FR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8148_17965_528227221}

[[\# ]{lang="FR"}]{#struct_0_x8148_17965_1348042105}[配置]{style="font-family:宋体"}[BPDU Tunnel]{lang="FR"}[报文的组播目的]{style="font-family:宋体"}[MAC]{lang="FR"}[地址为]{style="font-family:宋体"}[0100-0CCD-CDD0]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x8148_17965_1123113632}

[\[Sysname\] l2protocol tunnel-dmac 0100-0ccd-cdd0]{lang="FR"}
:::

::: {#-893942984 .myid}
[]{#_Toc404784731}[]{#struct_0_x8148_17965_x12938863}

**L2PT \-- L2PT配置命令 \-- reset l2protocol statistics**

------------------------------------------------------------------------

[**[reset l2protocol statistics]{lang="FR"}**]{#struct_0_x8148_17965_1101309394}[命令用来清除]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1157840249}

[**[reset l2protocol statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x8148_17965_1181033485}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x912391473}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x8148_17965_2132762024}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1692922291}

[[network-admin]{lang="PT-BR"}]{#struct_0_x8148_17965_x1918865834}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x8148_17965_x557288092}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8148_17965_1618450103}

[**[interface]{lang="FR"}**]{#struct_0_x8148_17965_x2041582287}[ *interface-type* *interface-number*]{lang="FR"}[：]{style="font-family:宋体"}[清除指定二层以太网接口或二层聚合接口上的]{style="font-family:宋体"}[L2PT]{lang="FR"}[报文统计信息。]{style="font-family:宋体"}*[interface-type]{lang="FR"}*[ *interface-number*]{lang="FR"}[表示接口类型和接口编号。如未指定本参数，将清除所有二层以太网接口和二层聚合接口的]{style="font-family:宋体"}[L2PT]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8148_17965_x288718827}

[[\# ]{lang="FR"}]{#struct_0_x8148_17965_143761463}[清除所有]{style="font-family:宋体"}[二层以太网接口和二层聚合接口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[L2PT]{lang="FR"}[报文统计信息。]{style="font-family:
宋体"}

[[\<Sysname\> reset l2protocol statistics]{lang="FR"}]{#struct_0_x8148_17965_x1695530390}

[ ]{lang="FR"}
:::
