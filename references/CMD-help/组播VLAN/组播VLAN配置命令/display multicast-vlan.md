::: {#294354185 .myid}
[]{#_Toc130111253}[]{#_Toc404789385}[]{#struct_0_11215_x1506_x241123744}[]{#_Toc300300915}[]{#_Toc135123814}[]{#_Toc130111252}[]{#_Toc138836430}[]{#_Toc138836431}[]{#_Toc138836432}[]{#_Toc138836433}[]{#_Toc138836434}[]{#_Toc138836435}[]{#_Toc138836436}[]{#_Toc138836437}[]{#_Toc138836438}[]{#_Toc138836439}[]{#_Toc138836440}[]{#_Toc138836441}[]{#_Toc138836442}[]{#_Toc138836443}[]{#_Toc138836446}[]{#_Toc138836451}[]{#_Toc138836452}[]{#_Toc138836463}

**组播VLAN \-- 组播VLAN配置命令 \-- display multicast-vlan**

------------------------------------------------------------------------

[**[display multicast-vlan]{lang="EN-US"}**]{#struct_0_11215_x1506_x1619157972}[命令用来显示组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x181375072}

[**[display multicast-vlan]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_11215_x1506_x963277929}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1654949637}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11215_x1506_x1680124889}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x2102869940}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_404993657}

[[network-operator]{lang="EN-US"}]{#struct_0_11215_x1506_x1226739227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_2088520203}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11215_x1506_x1271370988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1513678071}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_11215_x1506_1677830581}[：显示指定组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x2030291962}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_1655146245}[显示所有组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-vlan]{lang="EN-US"}]{#struct_0_11215_x1506_x2011993773}

[Total 2 multicast VLANs.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Multicast VLAN 100:]{lang="EN-US"}

[  Sub-VLAN list(3 in total):]{lang="EN-US"}

[    2-3, 6]{lang="EN-US"}

[  Port list(3 in total):]{lang="EN-US"}

[    GE1/0/1]{lang="EN-US"}

[    GE1/0/2]{lang="EN-US"}

[    GE1/0/3]{lang="EN-US"}

[ ]{lang="EN-US"}

[Multicast VLAN 200:]{lang="EN-US"}

[  Sub-VLAN list(0 in total):]{lang="EN-US"}

[  Port list(0 in total):]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display multicast-vlan]{lang="EN-US"}]{#struct_0_11215_x1506_x1514039293}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1478862502}[[字段]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1064864358}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11215_x1506_1897233997}

[[Total 2 multicast VLANs]{lang="EN-US"}]{#struct_0_11215_x1506_1655080709}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x130603760}[的总数]{style="font-family:宋体"}

[[Multicast VLAN 100]{lang="EN-US"}]{#struct_0_11215_x1506_x108046478}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_1036179889}

[[Sub-VLAN list(3 in total)]{lang="EN-US"}]{#struct_0_11215_x1506_1658078513}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x1186543127}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表及总数]{style="font-family:宋体"}

[[Port list(3 in total)]{lang="EN-US"}]{#struct_0_11215_x1506_x2146556628}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_1655277317}[的端口列表及总数]{style="font-family:宋体"}

[ ]{lang="EN-US" style="layout-grid-mode:line"}

::: {#-1860152310 .myid}
[]{#_Toc300300916}[]{#_Toc404789386}[]{#struct_0_11215_x1506_1512437014}[]{#_Toc334792529}[]{#_Toc329178771}

**组播VLAN \-- 组播VLAN配置命令 \-- display multicast-vlan group**

------------------------------------------------------------------------

[**[display multicast-vlan group]{lang="EN-US"}**]{#struct_0_11215_x1506_x1037338308}[命令用来显示组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的组播组表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_89612886}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_11215_x1506_x1740070910}

[**[display multicast-vlan]{lang="EN-US"}**[ **group** \[ *source-address* \| *group-address* \| **cpu** *cpu-number* \| **verbose** \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_11215_x1506_x1267495510}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11215_x1506_1837956407}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display multicast-vlan]{lang="EN-US"}**[ **group** \[ *source-address* \| *group-address* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **verbose** \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_11215_x1506_629680830}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11215_x1506_2039977816}[模式：]{style="font-family:宋体"}

[**[display multicast-vlan]{lang="EN-US"}**[ **group** \[ *source-address* \| *group-address* \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **verbose** \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_11215_x1506_1655211781}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1457696943}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11215_x1506_1473866025}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x124194909}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x2041500055}

[[network-operator]{lang="EN-US"}]{#struct_0_11215_x1506_x590719223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x656274222}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11215_x1506_x1363206280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1643063840}

[*[source-address]{lang="EN-US"}*]{#struct_0_11215_x1506_x436809922}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_11215_x1506_1655408389}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_1961212885}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_x687063748}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_11215_x1506_x1643425956}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}[slot-number]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_1835730321}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_1085457399}[：显示指定单板上的信息，]{style="font-family:宋体"}[chassis-number]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_11215_x1506_1835664785}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_11215_x1506_1260769126}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_11215_x1506_x1123540176}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_529838064}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_x891009072}[显示组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的所有组播组表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-vlan group verbose]{lang="EN-US"}]{#struct_0_11215_x1506_1655342853}

[Total 6 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Multicast VLAN 10: Total 3 entries.]{lang="EN-US"}

[  (2.2.2.2, 225.1.1.2)]{lang="EN-US"}

[    Flags: 0x70000020]{lang="EN-US"}

[    Sub-VLANs (1 in total):]{lang="EN-US"}

[      VLAN 40]{lang="EN-US"}

[  (111.112.113.115, 225.1.1.4)]{lang="EN-US"}

[    Flags: 0x70000030]{lang="EN-US"}

[    Sub-VLANs (1 in total):]{lang="EN-US"}

[      VLAN 40]{lang="EN-US"}

[  (0.0.0.0, 226.1.1.6)]{lang="EN-US"}

[    Flags: 0x60000020]{lang="EN-US"}

[    Sub-VLANs (1 in total):]{lang="EN-US"}

[      VLAN 40]{lang="EN-US"}

[ ]{lang="EN-US"}

[Multicast VLAN 20: Total 3 entries.]{lang="EN-US"}

[  (2.2.2.2, 225.1.1.2)]{lang="EN-US"}

[    Flags: 0x70000010]{lang="EN-US"}

[    Sub-VLANs (0 in total):]{lang="EN-US"}

[  (111.112.113.115, 225.1.1.4)]{lang="EN-US"}

[    Flags: 0x70000010]{lang="EN-US"}

[    Sub-VLANs (0 in total):]{lang="EN-US"}

[  (0.0.0.0, 226.1.1.6)]{lang="EN-US"}

[    Flags: 0x50000010]{lang="EN-US"}

[    Sub-VLANs (0 in total):]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display multicast-vlan group]{lang="EN-US"}]{#struct_0_11215_x1506_x1598211072}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1476969306}[[字段]{style="font-family:黑体"}]{#struct_0_11215_x1506_1643171097}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11215_x1506_x2041726904}

[[Total 6 entries]{lang="EN-US"}]{#struct_0_11215_x1506_x1781505921}

[[表项的总数]{style="font-family:宋体"}]{#struct_0_11215_x1506_1655539461}

[[Multicast VLAN 10: Total 3 entries]{lang="EN-US"}]{#struct_0_11215_x1506_x520399704}

[[组播]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}]{#struct_0_11215_x1506_x1363076471}[的组播组表项总数]{style="font-family:宋体"}

[[(0.0.0.0, 226.1.1.6)]{lang="EN-US"}]{#struct_0_11215_x1506_x948261492}

[[（]{style="font-family:宋体"}]{#struct_0_11215_x1506_x1757969090}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[0.0.0.0]{lang="FR"}[表示所有组播源]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_11215_x1506_2009988603}

[[（]{style="font-family:宋体"}]{#struct_0_11215_x1506_2009923067}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项的状态，通过将不同的比特位置位来表示不同的状态：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x10]{lang="FR"}]{#struct_0_11215_x1506_x1092902529}[：表示表项由组播]{style="font-family:宋体"}[VLAN]{lang="FR"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x20]{lang="FR"}]{#struct_0_11215_x1506_354733609}[：表示表项由子]{style="font-family:宋体"}[VLAN]{lang="FR"}[创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x40]{lang="FR"}]{#struct_0_11215_x1506_787578711}[：表示表项即将被删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x10000000]{lang="FR"}]{#struct_0_11215_x1506_2009857531}[：表示表项新创建或在查询周期内收到过]{style="font-family:
  宋体"}[IGMP]{lang="FR"}[查询报文，且没有收到过]{style="font-family:
  宋体"}[IGMPv1]{lang="FR"}[报告报文]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x20000000]{lang="FR"}]{#struct_0_11215_x1506_x1877248971}[：表示表项在查询周期内没有收到过]{style="font-family:
  宋体"}[IGMPv2/v3]{lang="FR"}[报告报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[0x40000000]{lang="FR"}]{#struct_0_11215_x1506_1232966441}[：表示表项]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[查询周期内没有收到]{lang="EN-US" style="font-family:宋体"}[过]{style="font-family:
  宋体"}[IGMPv3 IS_EX(NULL)]{lang="FR"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Sub-VLANs (1 in total)]{lang="EN-US"}]{#struct_0_11215_x1506_1159279120}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_1742493070}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表及总数]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc334792530}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1655473925}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset multicast-vlan group]{lang="EN-US"}**]{#struct_0_11215_x1506_1926219453}

::: {#2066906735 .myid}
[]{#_Toc404789387}[]{#struct_0_11215_x1506_x181842536}

**组播VLAN \-- 组播VLAN配置命令 \-- display multicast-vlan forwarding-table**

------------------------------------------------------------------------

[**[display multicast-vlan forwarding-table]{lang="EN-US"}**]{#struct_0_11215_x1506_x1692181447}[命令用来显示组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_529333970}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_11215_x1506_x816304551}

[**[display multicast-vlan forwarding-table]{lang="EN-US"}**[ \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **cpu** *cpu-number* \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_11215_x1506_x1103780691}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11215_x1506_1289444166}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display multicast-vlan forwarding-table]{lang="EN-US"}**[ \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_11215_x1506_x265336488}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11215_x1506_1655015174}[模式：]{style="font-family:宋体"}

[**[display multicast-vlan forwarding-table]{lang="EN-US"}**[ \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **subvlan** *vlan-id* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_11215_x1506_x2015240688}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1128588918}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11215_x1506_x482590023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1971930313}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x968936479}

[[network-operator]{lang="EN-US"}]{#struct_0_11215_x1506_x1269768890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x590212517}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11215_x1506_x1072874419}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1244645434}

[*[group-address]{lang="EN-US"}*]{#struct_0_11215_x1506_1654949638}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_11215_x1506_x1680976857}[：指定组播组的掩码长度或掩码。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_11215_x1506_1549267671}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_11215_x1506_x548733677}[：指定组播源的掩码长度或掩码。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_1256472619}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_831863638}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_11215_x1506_x883911069}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_1834878353}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11215_x1506_1996863972}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_11215_x1506_x479807250}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[subvlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_11215_x1506_621938602}[：显示指定子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。如果未指定本参数，将显示所有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_11215_x1506_x351416267}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1655146246}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_x2011797165}[显示组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表的全部信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-vlan forwarding-table]{lang="EN-US"}]{#struct_0_11215_x1506_x2128105773}

[Multicast VLAN 100 Forwarding Table]{lang="EN-US"}

[Total 1 entries, 1 matched]{lang="EN-US"}

[ ]{lang="EN-US"}

[00001. (1.1.1.1, 225.0.0.1)]{lang="EN-US"}

[     Flags: 0x10000]{lang="EN-US"}

[     Multicast VLAN: 100]{lang="EN-US"}

[     List of sub-VLANs (3 in total):]{lang="EN-US"}

[       1: VLAN 10]{lang="EN-US"}

[       2: VLAN 20]{lang="EN-US"}

[       3: VLAN 30]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display multicast-vlan forwarding-table]{lang="EN-US"}]{#struct_0_11215_x1506_1979855636}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1483640179}[[字段]{style="font-family:黑体"}]{#struct_0_11215_x1506_1592365521}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11215_x1506_x25971042}

[[Multicast VLAN 100 Forwarding Table]{lang="EN-US"}]{#struct_0_11215_x1506_1655080710}

[[组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}]{#struct_0_11215_x1506_x130013935}[的转发表]{style="font-family:宋体"}

[[Total 1 entries, 1 matched]{lang="EN-US"}]{#struct_0_11215_x1506_x496544181}

[[表项的总数和匹配数]{style="font-family:宋体"}]{#struct_0_11215_x1506_x86509446}

[[00001]{lang="EN-US"}]{#struct_0_11215_x1506_x759500086}

[[表示（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_11215_x1506_1741156977}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）项的序号]{style="font-family:宋体"}

[[ (1.1.1.1, 255.0.0.1)]{lang="EN-US"}]{#struct_0_11215_x1506_256083993}

[[（]{style="font-family:宋体"}]{#struct_0_11215_x1506_1655277318}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[0.0.0.0]{lang="FR"}[表示所有组播源]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_11215_x1506_1511978262}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_11215_x1506_1792321755}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）项的当前状态，使用不同的比特位来表示（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）项所处的不同状态]{style="font-family:宋体"}[，主要取值如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_11215_x1506_2009595387}[：表示表项处于]{lang="EN-US" style="font-family:宋体"}[Inactive]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x4]{lang="EN-US"}]{#struct_0_11215_x1506_423779979}[：表示表项下刷失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x8]{lang="EN-US"}]{#struct_0_11215_x1506_2009529851}[：表示有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下刷失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x200]{lang="EN-US"}]{#struct_0_11215_x1506_1955082498}[：表示表项处于平滑状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x10000]{lang="EN-US"}]{#struct_0_11215_x1506_1417755602}[：表示组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Multicast VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x2129009609}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x258686720}

[[List of sub-VLANs (3 in total)]{lang="EN-US"}]{#struct_0_11215_x1506_x861522137}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_1655211782}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表及总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#589548107 .myid}
[]{#_Toc404789388}[]{#struct_0_11215_x1506_1457500335}

**组播VLAN \-- 组播VLAN配置命令 \-- multicast-vlan**

------------------------------------------------------------------------

[**[multicast-vlan]{lang="EN-US"}**]{#struct_0_11215_x1506_x1225579411}[命令用来配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，并进入组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo multicast-vlan]{lang="EN-US"}**]{#struct_0_11215_x1506_1486110862}[命令用来取消指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_995391317}

[**[multicast-vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_11215_x1506_x403053004}

[**[undo multicast-vlan]{lang="EN-US"}**[ { **all** \| *vlan-id* }]{lang="EN-US"}]{#struct_0_11215_x1506_1793293283}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x536741099}

[[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x1936429535}[不是组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1655408390}

[[系统视图]{style="font-family:宋体"}]{#struct_0_11215_x1506_x514864787}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1563338132}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_762031891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x91439409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x371350351}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_11215_x1506_x1611070941}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_11215_x1506_707004931}[：删除所有组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【配置指导】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1229061619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要配置为组播]{style="font-family:宋体"}]{#struct_0_11215_x1506_1209847279}[VLAN]{lang="EN-US"}[的指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在已使能了]{style="font-family:宋体"}]{#struct_0_11215_x1506_1655342854}[IP]{lang="EN-US"}[组播路由的设备上不建议再配置组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[组播]{style="font-family:宋体"}]{#struct_0_11215_x1506_x1598014464}[VLAN]{lang="EN-US"}[的总数不得超过系统限制，该限制值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于子]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x1091455413}[模式的组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，需在组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[及其所有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[；对于基于端口模式的组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，需在组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和所有用户]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1200261096}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_x2118274247}[在]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，将其配置为组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，并进入组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11215_x1506_1196074546}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 100]{lang="EN-US"}

[\[Sysname-vlan100\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan100\] quit]{lang="EN-US"}

[\[Sysname\] multicast-vlan 100]{lang="EN-US"}

[\[Sysname-mvlan-100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_734210845}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_11215_x1506_1655539462}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/IGMP Snooping]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast routing]{lang="EN-US"}**]{#struct_0_11215_x1506_x520334168}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-1625659032 .myid}
[]{#_Toc130111254}[]{#_Toc404789389}[]{#struct_0_11215_x1506_x1311494492}[]{#_Toc300300917}[]{#_Toc205091251}

**组播VLAN \-- 组播VLAN配置命令 \-- multicast-vlan entry-limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VLAN命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_11215_x1506_302131908}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11215_x1506_x1254603656}
:::

[ ]{lang="EN-US"}

[**[multicast-vlan entry-limit]{lang="EN-US"}**]{#struct_0_11215_x1506_1272700300}[命令用来配置组播]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[转发表项的最大数量。]{style="font-family:宋体"}

[**[undo multicast-vlan entry-limit]{lang="EN-US"}**]{#struct_0_11215_x1506_x1537395546}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_2117487513}

[**[multicast-vlan entry-limit ]{lang="EN-US"}***[limit]{lang="EN-US"}*]{#struct_0_11215_x1506_1744268740}

[**[undo multicast-vlan entry-limit]{lang="EN-US"}**]{#struct_0_11215_x1506_1655473926}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1926284989}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_11215_x1506_x1238212178}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1865955247}

[[系统视图]{style="font-family:宋体"}]{#struct_0_11215_x1506_1562614192}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1256839682}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_373979043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_1270942908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1732779286}

[*[limit]{lang="EN-US"}*]{#struct_0_11215_x1506_x1901705986}[：组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表项的最大数量，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x717637818}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_1660962682}[配置组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[转发表项的最大数量为]{style="font-family:宋体"}[512]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11215_x1506_x1792001054}

[\[Sysname\] multicast-vlan entry-limit 512]{lang="EN-US"}

[]{#_Toc300300918}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1271988158}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[entry-limit]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_11215_x1506_576110642}[IGMP]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}[ ]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/IGMP Snooping]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#1755630030 .myid}
[]{#_Toc404789390}[]{#struct_0_11215_x1506_1474166348}

**组播VLAN \-- 组播VLAN配置命令 \-- port (multicast-VLAN view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VLAN命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_11215_x1506_1315172494}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11215_x1506_1325669321}
:::

[ ]{lang="EN-US"}

[**[port]{lang="EN-US"}**]{#struct_0_11215_x1506_1272466703}[命令用来向组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内添加端口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **port**]{lang="EN-US"}]{#struct_0_11215_x1506_x717703354}[命令用来删除组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x610110223}

[**[port ]{lang="EN-US"}***[interface-list]{lang="EN-US"}*]{#struct_0_11215_x1506_x54144485}

[**[undo]{lang="DA"}**]{#struct_0_11215_x1506_x375832858}[ ]{lang="DA"}**[port]{lang="EN-US"}**[ { ]{lang="DA"}**[all]{lang="EN-US"}**[ \| ]{lang="DA"}*[interface-list]{lang="EN-US"}*[ }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11215_x1506_501869620}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x1372856803}[内没有端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x2106489217}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x1193172929}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1133181490}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x953030999}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x717506746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x615138377}

[*[interface-list]{lang="EN-US"}*]{#struct_0_11215_x1506_52524782}[：端口列表，表示一个或多个端口。表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { ]{lang="DA"}*[interface-type interface-number]{lang="EN-US"}*[ \[ ]{lang="DA"}**[to]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*[ \] }]{lang="DA"}[。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_11215_x1506_793360812}[：删除当前组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的所有端口。]{style="font-family:宋体"}

[[【配置指导】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x165634231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个端口只能属于一个组播]{style="font-family:宋体"}]{#struct_0_11215_x1506_x1871776785}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只允许将以太网接口或二层聚合接口类型的用户端口配置为组播]{style="font-family:宋体"}]{#struct_0_11215_x1506_1547128048}[VLAN]{lang="EN-US"}[的端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_342026386}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_1250265323}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[到]{style="font-family:宋体"}[GigabitEthernet1/0/5]{lang="EN-US"}[添加到组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[内。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11215_x1506_x717572282}

[\[Sysname\] multicast-vlan 100]{lang="EN-US"}

[\[Sysname-mvlan-100\] port gigabitethernet 1/0/1 to gigabitethernet 1/0/5]{lang="EN-US"}
:::::

::::: {#-1466988827 .myid}
[]{#_Toc404789391}[]{#struct_0_11215_x1506_145615183}[]{#_Toc300300919}

**组播VLAN \-- 组播VLAN配置命令 \-- port multicast-vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VLAN命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_11215_x1506_756133974}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11215_x1506_x1452996181}
:::

[ ]{lang="EN-US"}

[**[port multicast-vlan]{lang="EN-US"}**]{#struct_0_11215_x1506_x1910532465}[命令用来指定端口所属的组播]{style="font-family:宋体"}[VLAN]{lang="DA"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**]{#struct_0_11215_x1506_x645315570}[ ]{lang="EN-US"}**[port multicast-vlan]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1391480012}

[**[port multicast-vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_11215_x1506_x1917282161}

[**[undo]{lang="DA"}**]{#struct_0_11215_x1506_1766873789}[ ]{lang="DA"}**[port multicast-vlan]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x717375674}

[[端口不属于任何组播]{style="font-family:宋体"}]{#struct_0_11215_x1506_140062757}[VLAN]{lang="DA"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_332300658}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_11215_x1506_1426539056}[/]{lang="DA"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1526510419}

[[network-admin]{lang="DA"}]{#struct_0_11215_x1506_x1615869390}

[[mdc-admin]{lang="DA"}]{#struct_0_11215_x1506_x2137803625}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_904153470}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_11215_x1506_x1083011345}[：指定端口所属组播]{style="font-family:宋体"}[VLAN]{lang="DA"}[的编号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[4094]{lang="DA"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x717441210}

[[一个端口只能属于一个组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x1412014590}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_1511647763}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_1063745911}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[属于组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11215_x1506_837130867}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port multicast-vlan 100]{lang="EN-US"}
:::::

::: {#338682931 .myid}
[]{#_Toc300300920}[]{#_Toc404789392}[]{#struct_0_11215_x1506_x398677478}

**组播VLAN \-- 组播VLAN配置命令 \-- reset multicast-vlan group**

------------------------------------------------------------------------

[**[reset multicast-vlan group]{lang="EN-US"}**]{#struct_0_11215_x1506_2028313347}[命令用来清除组播]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的组播组表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_2124579977}

[**[reset]{lang="EN-US"}**[ **multicast-vlan** **group** \[ *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_11215_x1506_x913686282}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x717244602}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11215_x1506_x1417042842}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x272202380}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x374609141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x651826862}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x168937624}

[*[source-address]{lang="EN-US"}*]{#struct_0_11215_x1506_572740068}[：清除包含指定组播源的表项。如果未指定本参数，将清除包含所有组播源表项。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_11215_x1506_x1028578473}[：指定组播源的掩码长度或掩码。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_11215_x1506_x1350157419}[：清除指定组播组的表项，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将清除所有组播组的表项。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_11215_x1506_x326811165}[：指定组播组的掩码长度或掩码。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[的缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_11215_x1506_x717310138}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的表项，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x636628392}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_x362248267}[清除组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的所有组播组表项。]{style="font-family:宋体"}

[[\<Sysname\> reset multicast-vlan group]{lang="EN-US"}]{#struct_0_11215_x1506_x1442481212}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1470128503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display multicast-vlan group]{lang="EN-US"}**]{#struct_0_11215_x1506_538738060}
:::

::::: {#1938752496 .myid}
[]{#_Toc404789393}[]{#struct_0_11215_x1506_2076141201}

**组播VLAN \-- 组播VLAN配置命令 \-- subvlan (multicast-VLAN view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VLAN命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_11215_x1506_x1640385654}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11215_x1506_715873379}
:::

[ ]{lang="EN-US"}

[**[subvlan]{lang="EN-US"}**]{#struct_0_11215_x1506_x717113530}[命令用来向组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内添加子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **subvlan**]{lang="EN-US"}]{#struct_0_11215_x1506_x998542263}[命令用来删除组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x846906158}

[**[subvlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_11215_x1506_x960539122}

[**[undo]{lang="DA"}**]{#struct_0_11215_x1506_x684199706}[ ]{lang="DA"}**[subvlan]{lang="EN-US"}**[ ]{lang="EN-US"}[{ ]{lang="DA"}**[all]{lang="EN-US"}**[ \| ]{lang="DA"}*[vlan-list]{lang="EN-US"}*[ }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1397812183}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_1187739388}[内没有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1259518260}

[[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_1686851842}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x705041656}

[[network-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x717179066}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11215_x1506_x682163628}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11215_x1506_x1250439219}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_11215_x1506_x1540143552}[：]{style="font-family:宋体"}[指定子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ ]{lang="EN-US"}[= { ]{lang="DA"}*[vlan-id]{lang="EN-US"}*[ \[ **to** ]{lang="DA"}*[vlan-id]{lang="EN-US"}*[ \] }&\<1-10\>]{lang="DA"}[，]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_11215_x1506_x1730299249}[：删除当前组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的所有子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11215_x1506_825680280}

[[要添加到组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11215_x1506_x1840818580}[内的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须存在，且不能是组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[或其它组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11215_x1506_840695181}

[[\# ]{lang="EN-US"}]{#struct_0_11215_x1506_1179628340}[配置]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[到]{style="font-family:宋体"}[VLAN 15]{lang="EN-US"}[为组播]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11215_x1506_x717637817}

[\[Sysname\] multicast-vlan 100]{lang="EN-US"}

[\[Sysname-mvlan-100\] subvlan 10 to 15]{lang="EN-US"}
:::::
