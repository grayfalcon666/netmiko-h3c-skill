::: {#-2023671670 .myid}
[]{#_Toc130111253}[]{#_Toc404790101}[]{#struct_0_x1077_x2294_x2072841852}[]{#_Toc300300915}[]{#_Toc135123814}[]{#_Toc130111252}[]{#_Toc138836430}[]{#_Toc138836431}[]{#_Toc138836432}[]{#_Toc138836433}[]{#_Toc138836434}[]{#_Toc138836435}[]{#_Toc138836436}[]{#_Toc138836437}[]{#_Toc138836438}[]{#_Toc138836439}[]{#_Toc138836440}[]{#_Toc138836441}[]{#_Toc138836442}[]{#_Toc138836443}[]{#_Toc138836446}[]{#_Toc138836451}[]{#_Toc138836452}[]{#_Toc138836463}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- display ipv6 multicast-vlan**

------------------------------------------------------------------------

[**[display ipv6 multicast-vlan]{lang="EN-US"}**]{#struct_0_x1077_x2294_1647135034}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_454878694}

[**[display ipv6 multicast-vlan]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1077_x2294_155218841}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x462501432}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1077_x2294_553948607}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_983112555}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x2108363774}

[[network-operator]{lang="EN-US"}]{#struct_0_x1077_x2294_1946520081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x301835914}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1077_x2294_1061566700}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_146017995}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x1077_x2294_1507402613}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1763231184}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_1242014682}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 multicast-vlan]{lang="EN-US"}]{#struct_0_x1077_x2294_x300852874}

[Total 2 IPv6 multicast VLANs.]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 multicast VLAN 100:]{lang="EN-US"}

[  Sub-VLAN list(3 in total):]{lang="EN-US"}

[    2-3, 6]{lang="EN-US"}

[  Port list(3 in total):]{lang="EN-US"}

[    GE1/0/1]{lang="EN-US"}

[    GE1/0/2]{lang="EN-US"}

[    GE1/0/3]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 multicast VLAN 200:]{lang="EN-US"}

[  Sub-VLAN list(0 in total):]{lang="EN-US"}

[  Port list(0 in total):]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ipv6 multicast-vlan]{lang="EN-US"}]{#struct_0_x1077_x2294_707397805}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x226519133}[[字段]{style="font-family:黑体"}]{#struct_0_x1077_x2294_593131407}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x778751531}

[[Total 2 IPv6 multicast VLANs]{lang="EN-US"}]{#struct_0_x1077_x2294_x492925437}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_2122548314}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的总数]{style="font-family:宋体"}

[[IPv6 multicast VLAN 100]{lang="EN-US"}]{#struct_0_x1077_x2294_x1996436391}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x300918410}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Sub-VLAN list(3 in total)]{lang="EN-US"}]{#struct_0_x1077_x2294_x1312778592}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_277785922}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表及总数]{style="font-family:宋体"}

[[Port list(3 in total)]{lang="EN-US"}]{#struct_0_x1077_x2294_1674448296}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x710635597}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的端口列表及总数]{style="font-family:宋体"}

[ ]{lang="EN-US" style="layout-grid-mode:line"}

::: {#-65342780 .myid}
[]{#_Toc300300916}[]{#_Toc404790102}[]{#struct_0_x1077_x2294_1280848056}[]{#_Toc334792529}[]{#_Toc329178771}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- display ipv6 multicast-vlan group**

------------------------------------------------------------------------

[**[display ipv6 multicast-vlan group]{lang="EN-US"}**]{#struct_0_x1077_x2294_1501024661}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的组播组表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1690957403}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x301377165}

[**[display ipv6 multicast-vlan]{lang="EN-US"}**[ **group** \[ *ipv6-source-address* \| *ipv6-group-address* \| **cpu** *cpu-number* \| **verbose** \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_x1077_x2294_1437224664}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1077_x2294_x1699134733}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 multicast-vlan]{lang="EN-US"}**[ **group** \[ *ipv6-source-address* \| *ipv6-group-address* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **verbose** \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_x1077_x2294_1065063723}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1077_x2294_x1680690785}[模式：]{style="font-family:宋体"}

[**[display ipv6 multicast-vlan]{lang="EN-US"}**[ **group** \[ *ipv6-source-address* \| *ipv6-group-address* \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **verbose** \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_x1077_x2294_677337824}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x431525366}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x1745577105}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x2087523254}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x301442701}

[[network-operator]{lang="EN-US"}]{#struct_0_x1077_x2294_305924140}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x1126062158}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1077_x2294_x959114611}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x41017445}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x1077_x2294_2037294211}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x1077_x2294_x663669267}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1077_x2294_x276252988}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[slot-number]{lang="EN-US"}*]{#struct_0_x1077_x2294_x1760892149}[：显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1077_x2294_1151034623}[：[显示指定成员设备]{style="color:black"}]{style="font-family:宋体"}[/PEX]{lang="EN-US" style="color:black"}[上[的信息，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号[。如果未指定本参数，将显示主设备上的信息]{style="color:black"}。[（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="color:black"}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1077_x2294_1486488972}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="color:black"}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1077_x2294_x1942072665}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[cpu-number]{lang="EN-US"}*]{#struct_0_x1077_x2294_x1338977773}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US" style="color:black"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1077_x2294_x301508237}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1077_x2294_625055258}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_452664713}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_x904418556}[显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的所有组播组表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 multicast-vlan group verbose]{lang="EN-US"}]{#struct_0_x1077_x2294_x301573773}

[Total 6 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 multicast VLAN 10: Total 3 entries.]{lang="EN-US"}

[  (2::2, FF0E::2)]{lang="EN-US"}

[    Flags: 0x70000020]{lang="EN-US"}

[    Sub-VLANs (1 in total):]{lang="EN-US"}

[      VLAN 40]{lang="EN-US"}

[  (22::22, FF0E::4)]{lang="EN-US"}

[    Flags: 0x70000030]{lang="EN-US"}

[    Sub-VLANs (1 in total):]{lang="EN-US"}

[      VLAN 40]{lang="EN-US"}

[  (::, FF0E::10)]{lang="EN-US"}

[    Flags: 0x10000030]{lang="EN-US"}

[    Sub-VLANs (1 in total):]{lang="EN-US"}

[      VLAN 40]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 multicast VLAN 20: Total 3 entries.]{lang="EN-US"}

[  (2::2, FF0E::2)]{lang="EN-US"}

[    Flags: 0x70000010]{lang="EN-US"}

[    Sub-VLANs (0 in total):]{lang="EN-US"}

[  (22::22, FF0E::4)]{lang="EN-US"}

[    Flags: 0x70000010]{lang="EN-US"}

[    Sub-VLANs (0 in total):]{lang="EN-US"}

[  (::, FF0E::10)]{lang="EN-US"}

[    Flags: 0x50000010]{lang="EN-US"}

[    Sub-VLANs (0 in total):]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 multicast-vlan group]{lang="EN-US"}]{#struct_0_x1077_x2294_x1270842197}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x233043125}[[字段]{style="font-family:黑体"}]{#struct_0_x1077_x2294_550800504}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1117084136}

[[Total 6 entries]{lang="EN-US"}]{#struct_0_x1077_x2294_2105857938}

[[表项的总数]{style="font-family:宋体"}]{#struct_0_x1077_x2294_573535285}

[[IPv6 multicast VLAN 10: Total 3 entries]{lang="EN-US"}]{#struct_0_x1077_x2294_777252202}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x301639309}[组播]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的组播组表项总数]{style="font-family:宋体"}

[[(::, FF0E::10)]{lang="EN-US"}]{#struct_0_x1077_x2294_1004604183}

[[（]{style="font-family:宋体"}]{#struct_0_x1077_x2294_359200284}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[::]{lang="FR"}[表示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x1077_x2294_x1287109369}

[[（]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x1394156116}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项的状态，通过将不同的比特位置位来表示不同的状态：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x10]{lang="FR"}]{#struct_0_x1077_x2294_278384743}[：表示表项由]{style="font-family:宋体"}[IPv6]{lang="FR"}[组播]{style="font-family:宋体"}[VLAN]{lang="FR"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x20]{lang="FR"}]{#struct_0_x1077_x2294_x1522809002}[：表示表项由子]{style="font-family:宋体"}[VLAN]{lang="FR"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x40]{lang="FR"}]{#struct_0_x1077_x2294_x1749558590}[：表示表项即将被删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x10000000]{lang="FR"}]{#struct_0_x1077_x2294_278450279}[：表示表项新创建或在查询周期内收到过]{style="font-family:
  宋体"}[MLD]{lang="FR"}[查询报文]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x20000000]{lang="FR"}]{#struct_0_x1077_x2294_x833584682}[：表示表项在查询周期内没有收到过]{style="font-family:
  宋体"}[MLDv1/v2]{lang="FR"}[报告报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x40000000]{lang="FR"}]{#struct_0_x1077_x2294_97325072}[：表示表项]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[查询周期内没有收到]{lang="EN-US" style="font-family:宋体"}[过]{style="font-family:
  宋体"}[MLD]{lang="FR"}[v]{lang="FR"}[2]{lang="FR"}[ IS_EX(NULL)]{lang="FR"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Sub-VLANs (1 in total)]{lang="EN-US"}]{#struct_0_x1077_x2294_389965552}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x1811304896}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表及总数]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc334792530}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1756312442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 multicast-vlan group]{lang="EN-US"}**]{#struct_0_x1077_x2294_x45401087}

::: {#1370364442 .myid}
[]{#_Toc404790103}[]{#struct_0_x1077_x2294_x301704845}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- display ipv6 multicast-vlan forwarding-table**

------------------------------------------------------------------------

[**[display ipv6 multicast-vlan forwarding-table]{lang="EN-US"}**]{#struct_0_x1077_x2294_682607597}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1675933833}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1077_x2294_2004920443}

[**[display ipv6 multicast-vlan forwarding-table]{lang="EN-US"}**[ \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **cpu** *cpu-number* \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_x1077_x2294_750523932}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1077_x2294_1406673814}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 multicast-vlan forwarding-table]{lang="EN-US"}**[ \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_x1077_x2294_11710220}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1077_x2294_1449660032}[模式：]{style="font-family:宋体"}

[**[display ipv6 multicast-vlan forwarding-table]{lang="EN-US"}**[ \[ *ipv6-source-address* \[ *prefix-length* \] \| *ipv6-group-address* \[ *prefix-length* \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_x1077_x2294_794313617}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x301770381}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x2072383091}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_965920511}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x1150223404}

[[network-operator]{lang="EN-US"}]{#struct_0_x1077_x2294_852179071}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_1012354406}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1077_x2294_x1718036556}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x563865260}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x1077_x2294_x445749044}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x1077_x2294_x301835917}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x1077_x2294_1061632236}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x1077_x2294_930495677}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的前缀长度，取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1077_x2294_x346655115}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[slot-number]{lang="EN-US"}*]{#struct_0_x1077_x2294_2085139390}[：显示指定成员设备上的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1077_x2294_x1624968435}[：[显示指定成员设备]{style="color:black"}]{style="font-family:宋体"}[/PEX]{lang="EN-US" style="color:black"}[上[的信息，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号[。如果未指定本参数，将显示主设备上的信息]{style="color:black"}。[（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="color:black"}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1077_x2294_1486751116}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="color:black"}**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1077_x2294_1757483660}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US" style="color:black"}*[cpu-number]{lang="EN-US"}*]{#struct_0_x1077_x2294_x989271123}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上的信息，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US" style="color:black"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[subvlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_x1077_x2294_x556647846}[：显示指定]{style="font-family:宋体;color:black"}[子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。如果未指定本参数，将显示所有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1077_x2294_1354023569}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x415185082}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_x300852877}[显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表的全部信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 multicast-vlan forwarding-table]{lang="EN-US"}]{#struct_0_x1077_x2294_707201197}

[IPv6 multicast VLAN 100 Forwarding Table]{lang="EN-US"}

[Total 1 entries, 1 matched]{lang="EN-US"}

[ ]{lang="EN-US"}

[00001. (1::1, FF0E::1)]{lang="EN-US"}

[     Flags: 0x10000]{lang="EN-US"}

[     IPv6 multicast VLAN: 100]{lang="EN-US"}

[     List of sub-VLANs (3 in total):]{lang="EN-US"}

[       1: VLAN 10]{lang="EN-US"}

[       2: VLAN 20]{lang="EN-US"}

[       3: VLAN 30]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ipv6 multicast-vlan forwarding-table]{lang="EN-US"}]{#struct_0_x1077_x2294_x1741248793}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x231149837}[[字段]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1899820379}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1431440330}

[[IPv6 multicast VLAN 100 Forwarding Table]{lang="EN-US"}]{#struct_0_x1077_x2294_x929391729}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x300918413}[组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[的转发表]{style="font-family:宋体"}

[[Total 1 entries, 1 matched]{lang="EN-US"}]{#struct_0_x1077_x2294_x1312975200}

[[表项的总数和匹配数]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x1300118513}

[[00001]{lang="EN-US"}]{#struct_0_x1077_x2294_x862685713}

[[表示（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1077_x2294_2103732364}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）项的序号]{style="font-family:宋体"}

[[ (1::1, FF0E::1)]{lang="EN-US"}]{#struct_0_x1077_x2294_705965594}

[[（]{style="font-family:宋体"}]{#struct_0_x1077_x2294_800834394}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[::]{lang="FR"}[表示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x1077_x2294_x301377164}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1077_x2294_1437290200}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）项的当前状态，使用不同的比特位来表示（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）项所处的不同状态]{style="font-family:宋体"}[，主要取值如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_x1077_x2294_278319207}[：表示表项处于]{lang="EN-US" style="font-family:宋体"}[Inactive]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x4]{lang="EN-US"}]{#struct_0_x1077_x2294_1271759188}[：表示表项下刷失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x8]{lang="EN-US"}]{#struct_0_x1077_x2294_278909031}[：表示有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下刷失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x200]{lang="EN-US"}]{#struct_0_x1077_x2294_1611885295}[：表示表项处于平滑状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x10000]{lang="EN-US"}]{#struct_0_x1077_x2294_278974567}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[IPv6 multicast VLAN]{lang="EN-US"}]{#struct_0_x1077_x2294_1376392541}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_311893596}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[List of sub-VLANs (3 in total)]{lang="EN-US"}]{#struct_0_x1077_x2294_1118918995}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x301442700}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表及总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1265139634 .myid}
[]{#_Toc404790104}[]{#struct_0_x1077_x2294_305858604}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- ipv6 multicast-vlan**

------------------------------------------------------------------------

[**[ipv6 multicast-vlan]{lang="EN-US"}**]{#struct_0_x1077_x2294_x1913560754}[命令用来配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo ipv6 multicast-vlan]{lang="EN-US"}**]{#struct_0_x1077_x2294_x1224706946}[命令用来取消指定]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_202437038}

[**[ipv6 multicast-vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1077_x2294_1650140868}

[**[undo ipv6 multicast-vlan]{lang="EN-US"}**[ { **all** \| *vlan-id* }]{lang="EN-US"}]{#struct_0_x1077_x2294_x1755568905}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_630296488}

[[VLAN]{lang="EN-US"}]{#struct_0_x1077_x2294_167238000}[不是]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x301508236}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1077_x2294_624989722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_537124948}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_793709274}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_44623055}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_797739636}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x1077_x2294_x1724721468}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1077_x2294_1277967986}[：删除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【配置指导】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1301641967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要配置为]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x301573772}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在已使能了]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x1270776661}[IPv6]{lang="EN-US"}[组播路由的设备上不建议再配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x776615128}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的总数不得超过系统限制，该限制值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于子]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1077_x2294_2006409359}[模式的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，需在]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[及其所有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[ Snooping]{lang="EN-US"}[；对于基于端口模式的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，需在]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和所有用户]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[ Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1768436061}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_x1446310169}[在]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，将其配置为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1077_x2294_x556483906}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 100]{lang="EN-US"}

[\[Sysname-vlan100\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan100\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 multicast-vlan 100]{lang="EN-US"}

[\[Sysname-ipv6-mvlan-100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1690539191}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x1077_x2294_x301639308}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[MLD]{lang="EN-US"}[ Snooping]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 multicast routing]{lang="EN-US"}**]{#struct_0_x1077_x2294_1004669719}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[IPv6]{lang="EN-US"}[组播路由与转发）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-1622581192 .myid}
[]{#_Toc130111254}[]{#_Toc300300917}[]{#_Toc205091251}[]{#_Toc300300919}[]{#_Toc404790105}[]{#struct_0_x1077_x2294_1488731418}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- ipv6 multicast-vlan entry-limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
![说明](IPv6组播VLAN命令.files/image001.png){width="62" height="25" align="left" hspace="12"}[\
]{lang="EN-US"}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1077_x2294_788130733}
:::

[ ]{lang="EN-US"}

[**[ipv6 multicast-vlan entry-limit]{lang="EN-US"}**]{#struct_0_x1077_x2294_931773275}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表项的最大数量。]{style="font-family:宋体"}

[**[undo ipv6 multicast-vlan entry-limit]{lang="EN-US"}**]{#struct_0_x1077_x2294_1630222747}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1888682346}

[**[ipv6 multicast-vlan entry-limit ]{lang="EN-US"}***[limit]{lang="EN-US"}*]{#struct_0_x1077_x2294_1516238002}

[**[undo ipv6 multicast-vlan entry-limit]{lang="EN-US"}**]{#struct_0_x1077_x2294_x301704844}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_682542061}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1077_x2294_2133071320}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_152605697}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x869840208}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1663705544}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x1583572371}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x1389543804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_628474873}

[*[limit]{lang="EN-US"}*]{#struct_0_x1077_x2294_459584527}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表项的最大数量，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x301770380}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_x2072317555}[配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表项的最大数量为]{style="font-family:宋体"}[512]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1077_x2294_1851324987}

[\[Sysname\] ipv6 multicast-vlan entry-limit 512]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x429305152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[entry-limit]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x1077_x2294_x863329493}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}[ ]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[MLD]{lang="EN-US"}[ Snooping]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#-1801787307 .myid}
[]{#_Toc404790106}[]{#struct_0_x1077_x2294_x1007095633}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- ipv6 port multicast-vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6组播VLAN命令.files/image002.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1077_x2294_x1128884052}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1077_x2294_x1826619820}
:::

[ ]{lang="DA"}

[**[ipv6 port multicast-vlan]{lang="EN-US"}**]{#struct_0_x1077_x2294_x301835916}[命令用来指定端口所属的]{style="font-family:
宋体"}[IPv6]{lang="DA"}[组播]{style="font-family:宋体"}[VLAN]{lang="DA"}[。]{style="font-family:宋体"}

[**[undo ipv6 port multicast-vlan]{lang="EN-US"}**]{#struct_0_x1077_x2294_1061697772}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1426291776}

[**[ipv6 port multicast-vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1077_x2294_x400129877}

[**[undo ipv6 port multicast-vlan]{lang="DA"}**]{#struct_0_x1077_x2294_720308813}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1639272647}

[[端口不属于任何]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x1906772958}[IPv6]{lang="DA"}[组播]{style="font-family:宋体"}[VLAN]{lang="DA"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x725654910}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1077_x2294_x2057752786}[/]{lang="DA"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1748192045}

[[network-admin]{lang="DA"}]{#struct_0_x1077_x2294_x300852876}

[[mdc-admin]{lang="DA"}]{#struct_0_x1077_x2294_707266733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x651271837}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x1077_x2294_597261642}[：指定端口所属]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播]{style="font-family:宋体"}[VLAN]{lang="DA"}[的编号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[4094]{lang="DA"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1105272727}

[[一个端口只能属于一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_758687120}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1140773774}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_1426902753}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[属于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1077_x2294_x300918412}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 port multicast-vlan 100]{lang="EN-US"}
:::::

::::: {#-1867498095 .myid}
[]{#_Toc404790107}[]{#struct_0_x1077_x2294_x1312909664}[]{#_Toc300300918}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- port (IPv6 multicast-VLAN view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6组播VLAN命令.files/image002.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1077_x2294_x1711896664}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1077_x2294_23692320}
:::

[ ]{lang="EN-US"}

[**[port]{lang="EN-US"}**]{#struct_0_x1077_x2294_1542466786}[命令用来向]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内添加端口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **port**]{lang="EN-US"}]{#struct_0_x1077_x2294_1438156727}[命令用来删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1627532228}

[**[port ]{lang="EN-US"}***[interface-list]{lang="EN-US"}*]{#struct_0_x1077_x2294_1113594996}

[**[undo]{lang="DA"}**]{#struct_0_x1077_x2294_34854647}[ ]{lang="DA"}**[port]{lang="EN-US"}**[ { ]{lang="DA"}**[all]{lang="EN-US"}**[ \| ]{lang="DA"}*[interface-list]{lang="EN-US"}*[ }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x301377167}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_1437355736}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内没有端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1834339898}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_1902724468}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1573778939}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_544837578}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_1604113692}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1508159270}

[*[interface-list]{lang="EN-US"}*]{#struct_0_x1077_x2294_x1229177534}[：端口列表，表示一个或多个端口。表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { ]{lang="DA"}*[interface-type interface-number]{lang="EN-US"}*[ \[ ]{lang="DA"}**[to]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*[ \] }]{lang="DA"}[。其中，]{style="font-family:
宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1077_x2294_x67962364}[：删除当前]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的所有端口。]{style="font-family:宋体"}

[[【配置指导】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x301442703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个端口只能属于一个]{style="font-family:宋体"}]{#struct_0_x1077_x2294_306055212}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只允许将以太网接口或二层聚合接口类型的用户端口配置为]{style="font-family:宋体"}]{#struct_0_x1077_x2294_2099393767}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1133908554}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_x1228614554}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[到]{style="font-family:宋体"}[GigabitEthernet1/0/5]{lang="EN-US"}[添加到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[内。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1077_x2294_409906927}

[\[Sysname\] ipv6 multicast-vlan 100]{lang="EN-US"}

[\[Sysname-ipv6-mvlan-100\] port gigabitethernet 1/0/1 to gigabitethernet 1/0/5]{lang="EN-US"}
:::::

::: {#55067400 .myid}
[]{#_Toc300300920}[]{#_Toc404790108}[]{#struct_0_x1077_x2294_x1515705806}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- reset ipv6 multicast-vlan group**

------------------------------------------------------------------------

[**[reset ipv6 multicast-vlan group]{lang="EN-US"}**]{#struct_0_x1077_x2294_170503609}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的组播组表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x301508239}

[**[reset ipv6 multicast-vlan]{lang="EN-US"}**[ **group** \[ *ipv6-group-address* \[ *prefix-length* \] \| *ipv6-source-address* \[ *prefix-length* \] \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_x1077_x2294_624137754}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x42017109}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1077_x2294_1618965865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1424006700}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x1319977980}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_x1567374047}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x2007387232}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x1077_x2294_391497670}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的表项，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将清除所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的表项。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x1077_x2294_x301573775}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的前缀长度，取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x1077_x2294_x1270711125}[：清除包含指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的表项。如果未指定本参数，将清除包含所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的表项。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x1077_x2294_597470603}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1077_x2294_x70655921}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的表项，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1221588300}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_x934155107}[清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的所有组播组表项。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 multicast-vlan group]{lang="EN-US"}]{#struct_0_x1077_x2294_x1423140087}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x626704927}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 multicast-vlan group]{lang="EN-US"}**]{#struct_0_x1077_x2294_x1969148148}
:::

::::: {#2036466912 .myid}
[]{#_Toc404790109}[]{#struct_0_x1077_x2294_970837051}

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- subvlan (IPv6 multicast-VLAN view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6组播VLAN命令.files/image003.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1077_x2294_x301639311}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1077_x2294_1004079894}
:::

[ ]{lang="EN-US"}

[**[subvlan]{lang="EN-US"}**]{#struct_0_x1077_x2294_1530608980}[命令用来向]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内添加子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **subvlan**]{lang="EN-US"}]{#struct_0_x1077_x2294_1146468792}[命令用来删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x973805519}

[**[subvlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1077_x2294_x727686957}

[**[undo]{lang="DA"}**]{#struct_0_x1077_x2294_x1833297816}[ ]{lang="DA"}**[subvlan]{lang="EN-US"}**[ ]{lang="EN-US"}[{ ]{lang="DA"}**[all]{lang="EN-US"}**[ \| ]{lang="DA"}*[vlan-list]{lang="EN-US"}*[ }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1448346275}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_438929494}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内没有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x301704847}

[[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_682738669}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x1034343287}

[[network-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_562234760}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1077_x2294_201043555}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1923897078}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_x1077_x2294_2094579266}[：]{style="font-family:宋体"}[指定子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="DA"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="DA"}[，]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[vlan-id]{lang="DA"}*[为指定子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1077_x2294_365441758}[：删除当前]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的所有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_1481239757}

[[要添加到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1077_x2294_x301770383}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须存在，且不能是]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[或其它]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1077_x2294_x2072252019}

[[\# ]{lang="EN-US"}]{#struct_0_x1077_x2294_x1706211392}[配置]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[到]{style="font-family:宋体"}[VLAN 15]{lang="EN-US"}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1077_x2294_x782104290}

[\[Sysname\] ipv6 multicast-vlan 100]{lang="EN-US"}

[\[Sysname-ipv6-mvlan-100\] subvlan 10 to 15]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
