::: {#1986630234 .myid}
[]{#_Toc323023217}[]{#_Toc404790075}[]{#struct_0_x1118_x3453_x1746089630}[]{#_Toc334101960}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping neighbor**

------------------------------------------------------------------------

[**[display ipv6 pim-snooping neighbor]{lang="EN-US"}**]{#struct_0_x1118_x3453_x1866936817}[命令用来显示]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1674377836}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x749997109}

[**[display ipv6 pim-snooping neighbor]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1118_x3453_1644481195}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1118_x3453_x254101515}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 pim-snooping neighbor]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1118_x3453_961314156}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1118_x3453_1379708536}[模式：]{style="font-family:宋体"}

[**[display ipv6 pim-snooping neighbor]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1118_x3453_x1714712623}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_737842250}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x605223981}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1951761380}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x1867002353}

[[network-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_x1538253471}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x171552936}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_2060381077}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1319222080}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1118_x3453_1424301097}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1118_x3453_1513988709}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1118_x3453_x2144229225}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x1118_x3453_1887779177}[：显示指定成员设备上的信息，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x1118_x3453_2132693214}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1118_x3453_x174242085}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1118_x3453_x672957064}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[verbose]{lang="EN-US" style="color:black"}**]{#struct_0_x1118_x3453_1391258379}[：]{style="font-family:
宋体;color:black"}[显示详细信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}[如果未指定本参数，将显示简要信息。]{style="font-family:宋体;
color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1433383960}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_x1867461108}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的邻居详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim-snooping neighbor vlan 2 verbose]{lang="EN-US"}]{#struct_0_x1118_x3453_x35474584}

[Total 2 neighbors.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 2 neighbors.]{lang="EN-US"}

[  FE80::6401:101]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      GE1/0/1                             (02:02:23)    LAN Prune Delay(T)]{lang="EN-US"}

[  FE80::C801:101]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      GE1/0/2                             (02:02:25)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_1513398884}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim-snooping neighbor vsi aaa]{lang="EN-US"}]{#struct_0_x1118_x3453_120105495}

[Total 2 neighbors.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 2 neighbors.]{lang="EN-US"}

[  FE80::1]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0 Link ID 2)          (00:02:04)]{lang="EN-US"}

[  FE80::2]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0 Link ID 1)          (00:02:13)]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ipv6 pim-snooping neighbor]{lang="EN-US"}]{#struct_0_x1118_x3453_x1906463839}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x348992893}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x427115479}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x3453_110207743}

[[Total 2 neighbors]{lang="EN-US"}]{#struct_0_x1118_x3453_x1867526644}

[[IPv6 PIM Snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_x1403801707}[邻居的总数]{style="font-family:宋体"}

[[VLAN 2: Total 2 neighbors]{lang="EN-US"}]{#struct_0_x1118_x3453_x1226243412}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1118_x3453_x1856396179}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 2 neighbors]{lang="EN-US"}]{#struct_0_x1118_x3453_1513464420}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1118_x3453_123328270}[内的表项总数]{style="font-family:宋体"}

[[FE80::6401:101]{lang="EN-US"}]{#struct_0_x1118_x3453_569009079}

[[IPv6 PIM Snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_x237090895}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Slots (0 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_x1867592180}

[[本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x685886627}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1942388799}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x448594232}[IPv6 PIM Snooping]{lang="EN-US"}[邻居的单板总数，以及各单板的槽位号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1573666498}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[邻居的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1118_x3453_438628463}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[邻居的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Ports (1 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_891170469}

[[IPv6 PIM Snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_x520359666}[邻居所在的端口及总数]{style="font-family:宋体"}

[[(02:02:23)]{lang="EN-US"}]{#struct_0_x1118_x3453_617749123}

[[IPv6 PIM Snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_x1844731290}[邻居所在端口的老化剩余时间。需要注意的是，本字段对于全局口（包括二层聚合接口、]{style="font-family:宋体"}[AC]{lang="EN-US"}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等）将无条件显示，而对于非全局口：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1486488977}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_441620860}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1518496452}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1118_x3453_207452557}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[LAN Prune Delay]{lang="EN-US"}]{#struct_0_x1118_x3453_1486357905}

[[表示该邻居发出的]{style="font-family:宋体"}[PIM Hello]{lang="EN-US"}]{#struct_0_x1118_x3453_x1355885210}[报文中携带有]{style="font-family:宋体"}[LAN_Prune_Delay]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[(T)]{lang="EN-US"}]{#struct_0_x1118_x3453_729818198}

[[表示该邻居已禁止加入报文抑制能力]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1395116661}

[[AC (VSI index 0 Link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1513136740}

[[AC]{lang="FR"}]{#struct_0_x1118_x3453_519499327}[（]{style="font-family:宋体"}[Attachment Circuit]{lang="FR"}[，接入电路）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1513202276}

[[N-PW]{lang="FR"}]{#struct_0_x1118_x3453_x230482893}[（]{style="font-family:宋体"}[Network Pseudowire]{lang="FR"}[，网络侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1513267812}

[[U-PW]{lang="FR"}]{#struct_0_x1118_x3453_x1767278078}[（]{style="font-family:宋体"}[User facing Pseudowire]{lang="FR"}[，用户侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1699257280 .myid}
[]{#_Toc404790076}[]{#struct_0_x1118_x3453_x75436414}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping router-port**

------------------------------------------------------------------------

[**[display ipv6 pim-snooping router-port]{lang="EN-US"}**]{#struct_0_x1118_x3453_x1867657716}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的路由器端口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_993782005}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1938279506}

[**[display ipv6 pim-snooping router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x1118_x3453_1738951662}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1118_x3453_1645649758}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 pim-snooping router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1118_x3453_1682857219}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1118_x3453_1833555003}[模式：]{style="font-family:宋体"}

[**[display ipv6 pim-snooping router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1118_x3453_1261817201}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1551532801}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1867723252}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1804440773}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x1280893337}

[[network-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_87799766}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_485810620}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_x1776856053}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1818996401}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1118_x3453_x797494343}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1118_x3453_1513923172}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1118_x3453_x417531756}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x1118_x3453_x1867788788}[：显示指定成员设备上的信息，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果不指定该参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x1118_x3453_x1759055091}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:
black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1118_x3453_x290392328}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果不指定该参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1118_x3453_x192971150}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x350274416}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_1044389754}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的路由器端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim-snooping router-port vlan 2]{lang="EN-US"}]{#struct_0_x1118_x3453_441751932}

[VLAN 2:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    GE1/0/1                             (00:01:30)]{lang="EN-US"}

[    GE1/0/2                             (00:01:32)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_1513988708}[显示]{style="font-family:宋体"}[VSI aaa ]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[的路由器端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim-snooping router-port vsi aaa]{lang="EN-US"}]{#struct_0_x1118_x3453_x309155627}

[VSI aaa:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    AC (VSI index 0 Link ID 0)          (00:02:43)]{lang="EN-US"}

[    AC (VSI index 0 Link ID 1)          (00:02:52)]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 pim-snooping router-port]{lang="EN-US"}]{#struct_0_x1118_x3453_599864840}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x321795127}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x421551209}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1506839084}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1118_x3453_114688319}

[[VLAN]{lang="EN-US"}]{#struct_0_x1118_x3453_x927216070}[的编号]{style="font-family:宋体"}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1118_x3453_1513398879}

[[VSI]{lang="EN-US"}]{#struct_0_x1118_x3453_1513464415}[的名称]{style="font-family:宋体"}

[[Router slots (1 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_x115533959}

[[本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1867919860}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1942388804}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有路由器端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1563749656}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x281715380}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有路由器端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1942388805}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Router ports (2 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_x618958020}

[[路由器端口的及总数]{style="font-family:宋体"}]{#struct_0_x1118_x3453_2094561243}

[[(00:01:30)]{lang="EN-US"}]{#struct_0_x1118_x3453_724162488}

[[路由器端口的老化剩余时间。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x27633994}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1486620049}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1700337489}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1866936820}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x2077465755}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1513529951}

[[AC]{lang="FR"}]{#struct_0_x1118_x3453_1513595487}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1654678106}

[[N-PW]{lang="FR"}]{#struct_0_x1118_x3453_1513136735}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_519171644}

[[U-PW]{lang="FR"}]{#struct_0_x1118_x3453_1513202271}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-910928305 .myid}
[]{#_Toc323023218}[]{#_Toc404790077}[]{#struct_0_x1118_x3453_100493901}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping routing-table**

------------------------------------------------------------------------

[**[display ipv6 pim-snooping routing-table]{lang="EN-US"}**]{#struct_0_x1118_x3453_x1225049033}[命令用来显示]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[路由表]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1044131693}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1764706229}

[**[display ipv6 pim-snooping routing-table ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1118_x3453_1384722042}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1118_x3453_1024560607}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 pim-snooping routing-table ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[slot *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1118_x3453_76952381}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1118_x3453_x1867002356}[模式：]{style="font-family:宋体"}

[**[display ipv6 pim-snooping routing-table ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1118_x3453_1997198938}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x255937611}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1118_x3453_597738162}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x2070892659}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_2002741096}

[[network-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_x1852797988}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x871377050}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_1945979178}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1867461107}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1118_x3453_1530609357}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1118_x3453_1513333343}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1118_x3453_x435731182}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参[数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x1118_x3453_731213347}[：显示指定成员设备上的信息，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x1118_x3453_566543737}[：]{style="font-family:宋体;
color:black"}[显示指定成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[的信息，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号]{style="font-family:宋体;color:black"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:
black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1118_x3453_302747054}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1118_x3453_2132627678}[：显示指定单板上的信息，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[对应的虚拟框号]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体;
color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;
color:black"}[（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[verbose]{lang="EN-US" style="color:black"}**]{#struct_0_x1118_x3453_1937255398}[：]{style="font-family:
宋体;color:black"}[显示详细信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}[如果未指定本参数，将显示简要信息。]{style="font-family:宋体;
color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1136341427}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_x786881231}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[路由表]{style="font-family:宋体"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim-snooping routing-table vlan 2 verbose]{lang="EN-US"}]{#struct_0_x1118_x3453_441555324}

[Total 1 entries.]{lang="EN-US"}

[FSM Flag: NI-no info, J-join, PP-prune pending]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 entries.]{lang="EN-US"}

[  (2000::1, FF1E::1)]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Upstream neighbor: FE80::101]{lang="EN-US"}

[      Upstream Slots (0 in total):]{lang="EN-US"}

[      Upstream Ports (1 in total):]{lang="EN-US"}

[        GE1/0/1]{lang="EN-US"}

[      Downstream Slots (0 in total):]{lang="EN-US"}

[      Downstream Ports (2 in total):]{lang="EN-US"}

[        GE1/0/2]{lang="EN-US"}

[          Expires: 00:03:01, FSM: J]{lang="EN-US"}

[          Downstream Neighbors (2 in total):]{lang="EN-US"}

[            1001::1]{lang="EN-US"}

[              Expires: 00:59:19, FSM: J]{lang="EN-US"}

[            1001::2]{lang="EN-US"}

[              Expires: 00:59:20, FSM: J]{lang="EN-US"}

[        GE1/0/3]{lang="EN-US"}

[          Expires: 00:02:21, FSM: PP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_1513988703}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim-snooping routing-table vsi aaa]{lang="EN-US"}]{#struct_0_x1118_x3453_x308696875}

[Total 1 entries.]{lang="EN-US"}

[FSM Flag: NI-no info, J-join, PP-prune pending]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 entries.]{lang="EN-US"}

[  (3000::1, FF1E::101)]{lang="EN-US"}

[    Upstream neighbor: FE80::1]{lang="EN-US"}

[      Upstream Slots (0 in total):]{lang="EN-US"}

[      Upstream Ports (1 in total):]{lang="EN-US"}

[        AC (VSI index 0 Link ID 0)]{lang="EN-US"}

[      Downstream Slots (0 in total):]{lang="EN-US"}

[      Downstream Ports (1 in total):]{lang="EN-US"}

[        AC (VSI index 0 Link ID 1)]{lang="EN-US"}

[           Expires: 00:02:41, FSM: J]{lang="EN-US"}

[]{#struct_0_x1118_x3453_x12981755}[[表1-3 ]{lang="EN-US"}[display ipv6 pim-snooping routing-table]{lang="EN-US"}]{#_Toc252534573}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x322313155}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x394687172}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1867723251}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x1118_x3453_x238356832}

[[IPv6 PIM Snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_2090596607}[路由表中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）与（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的总数]{style="font-family:宋体"}

[[FSM Flag: NI-no info, J-join, PP-prune pending]{lang="EN-US"}]{#struct_0_x1118_x3453_x985844347}

[[下游端口的状态机标识：]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_x1118_x3453_x318564394}[表示初始状态，]{style="font-family:宋体"}[J]{lang="EN-US"}[表示加入状态，]{style="font-family:宋体"}[PP]{lang="EN-US"}[表示剪枝未决状态]{style="font-family:宋体"}

[[(2000::1, FF1E::1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1798939891}

[[IPv6 PIM Snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_x1785315815}[路由表中的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[FSM information]{lang="EN-US"}]{#struct_0_x1118_x3453_1486685584}

[[表项状态机，包括：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1486751120}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_x1118_x3453_x989140050}[：表示所有成员属性均已删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dummy]{lang="FR"}]{#struct_0_x1118_x3453_178340964}[：表示新创建的临时表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[no info]{lang="FR"}]{#struct_0_x1118_x3453_1486554512}[：表示没有表项存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[normal]{lang="FR"}]{#struct_0_x1118_x3453_x627619524}[：表示主控板通知创建的正式表项]{style="font-family:宋体"}

[[Upstream neighbor]{lang="EN-US"}]{#struct_0_x1118_x3453_x1867788787}

[[上游邻居]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1406137575}

[[Upstream Slots (1 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_x1715592688}

[[本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1816418040}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x752910400}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有上游邻居的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x752910401}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x947457299}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有上游邻居的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x384054706}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有上游邻居的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Upstream Ports (1 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_x1875072651}

[[上游邻居所在的端口及总数。需要注意的是，本字段：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1303545105}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1485899152}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若上游端口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1867854323}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1118_x3453_622764530}[IRF]{lang="EN-US"}[设备上，若上游端口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1712670876}[IRF]{lang="EN-US"}[模式上，若上游端口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[Downstream Slots (2 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_1825786255}

[[除当前单板外其它所有有]{style="font-family:宋体"}]{#struct_0_x1118_x3453_224283214}[下游端口的单板的槽位及总数。本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Downstream Ports (2 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_x1867919859}

[[下游端口及总数]{style="font-family:宋体"}]{#struct_0_x1118_x3453_590698953}

[[Downstream Neighbors (2 in total)]{lang="EN-US"}]{#struct_0_x1118_x3453_1486292367}

[[下游端口包含的下游邻居及总数]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x229011840}

[[Expires: 00:03:01, FSM: J]{lang="EN-US"}]{#struct_0_x1118_x3453_x1837487279}

[[下游端口或下游邻居的老化剩余时间和状态机。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1246760389}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1486751119}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x2027338899}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1866936819}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x867808782}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1513595486}

[[AC]{lang="FR"}]{#struct_0_x1118_x3453_1513136734}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1513202270}

[[N-PW]{lang="FR"}]{#struct_0_x1118_x3453_x230089677}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1118_x3453_1513267806}

[[U-PW]{lang="FR"}]{#struct_0_x1118_x3453_1513333342}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1491373641 .myid}
[]{#_Toc404790078}[]{#struct_0_x1118_x3453_211483062}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping statistics**

------------------------------------------------------------------------

[**[display ipv6 pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1118_x3453_1465644958}[命令用来显示]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1892604431}

[**[display ipv6 pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1118_x3453_x808998918}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x301377163}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1437093592}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1384417709}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_208655551}

[[network-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_x1924615654}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x2024987467}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1118_x3453_x678461282}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_2081328619}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_2049295733}[显示]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim-snooping statistics]{lang="EN-US"}]{#struct_0_x1118_x3453_x301442699}

[Received IPv6 PIM hello:  100]{lang="EN-US"}

[Received IPv6 PIM join/prune:  100]{lang="EN-US"}

[Received IPv6 PIM error:  0]{lang="EN-US"}

[Received IPv6 PIM messages in total:  200]{lang="EN-US"}

[]{#_Toc252534575}[[表1-4 ]{lang="EN-US"}[display ipv6 pim-snooping statistics]{lang="EN-US"}]{#struct_0_x1118_x3453_x1650915277}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x320142567}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x844427432}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x78132664}

[[Received IPv6 PIM hello]{lang="EN-US"}]{#struct_0_x1118_x3453_x1367200294}

[[收到的]{style="font-family:宋体"}[IPv6 PIM Hello]{lang="EN-US"}]{#struct_0_x1118_x3453_477101328}[报文数]{style="font-family:宋体"}

[[Received IPv6 PIM join/prune]{lang="EN-US"}]{#struct_0_x1118_x3453_x1131506522}

[[收到的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1118_x3453_x1396130446}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文数]{style="font-family:宋体"}

[[Received IPv6 PIM error]{lang="EN-US"}]{#struct_0_x1118_x3453_x301508235}

[[收到的错误]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1118_x3453_624924186}[报文数]{style="font-family:宋体"}

[[Received IPv6 PIM messages in total]{lang="EN-US"}]{#struct_0_x1118_x3453_884054700}

[[收到的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1118_x3453_x1379658221}[报文总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x835674538}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1118_x3453_x1613426586}

::: {#-1187818479 .myid}
[]{#_Toc404790079}[]{#struct_0_x1118_x3453_650572057}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- ipv6 pim-snooping enable**

------------------------------------------------------------------------

[**[ipv6 pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1118_x3453_x301573771}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1118_x3453_x1270973269}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内关闭]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x834244604}

[**[ipv6 pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1118_x3453_x442888315}

[**[undo ipv6 pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1118_x3453_1925494441}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x764190484}

[[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1118_x3453_x718987080}[内的]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x26851420}

[[VLAN]{lang="EN-US"}]{#struct_0_x1118_x3453_1808528273}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x301639307}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_1003948823}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x675625063}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_403726483}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[/VSI]{lang="EN-US"}]{#struct_0_x1118_x3453_1251159537}[内使能]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[之前，必须先在]{lang="EN-US" style="font-family:宋体"}[全局以及]{style="font-family:宋体"}[该]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[/VSI]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1118_x3453_x356887250}[的子]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[无效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x912604469}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_x1421499059}[全局使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1118_x3453_x1714769886}

[[\[Sysname\] mld-snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_x887380336}

[[\[Sysname-mld-snooping\] quit]{lang="EN-US"}]{#struct_0_x1118_x3453_x301704843}

[[\[Sysname\] vlan 2]{lang="NL"}]{#struct_0_x1118_x3453_682476525}

[[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}]{#struct_0_x1118_x3453_214349694}

[[\[Sysname-vlan2\] ipv6 pim-snooping enable]{lang="NL"}]{#struct_0_x1118_x3453_942832691}

[[\# ]{lang="NL"}]{#struct_0_x1118_x3453_x1215287864}[全局使能]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[，并在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[和]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="NL"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x1118_x3453_240589470}

[\[Sysname\] mld-snooping]{lang="NL"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="NL"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] ipv6 pim-snooping enable]{lang="NL"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1309054762}

[[·[              ]{style="font:7.0pt "}]{lang="NL" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping]{lang="NL"}**]{#struct_0_x1118_x3453_1901841383}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="NL"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/MLD Snooping]{lang="NL"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="NL" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="NL"}**]{#struct_0_x1118_x3453_1290180485}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="NL"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/MLD Snooping]{lang="NL"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#53351189 .myid}
[]{#_Toc404790080}[]{#struct_0_x1118_x3453_x1906747258}[]{#_Toc334101958}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- ipv6 pim-snooping graceful-restart join-aging-time**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6%20PIM%20Snooping命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1118_x3453_1389909882}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1118_x3453_x301770379}
:::

[ ]{lang="EN-US"}

[**[ipv6 pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**]{#struct_0_x1118_x3453_x2072907388}[命令用来配置主备倒换期间新主用主控板上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[全局下游端口和全局路由器端口的老化时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ipv6 pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**]{#struct_0_x1118_x3453_237483873}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1845263703}

[**[ipv6 pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1118_x3453_x1258434748}

[**[undo ipv6 pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**]{#struct_0_x1118_x3453_x552158146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1631021351}

[[主备倒换期间新]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x794139252}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[全局下游端口和全局路由器端口的老化时间]{style="font-family:宋体"}[为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x267711447}

[[VLAN]{lang="EN-US"}]{#struct_0_x1118_x3453_x301835915}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1061501164}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x217921602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x1668587929}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x124708490}

[*[interval]{lang="EN-US"}*]{#struct_0_x1118_x3453_618899036}[：表示老化时间，取值范围为]{style="font-family:宋体"}[210]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_839146134}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局端口包括二层聚合接口、]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x939786957}[AC]{lang="EN-US"}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等，由全局端口担任的下游端口和路由器端口分别称为全局下游端口和全局路由器端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1118_x3453_992672125}[/VSI]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x300852875}

[[\#]{lang="EN-US"}]{#struct_0_x1118_x3453_707332269}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内配置主备倒换期间新]{style="font-family:宋体"}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[全局]{style="font-family:宋体"}[下游端口和全局路由器端口的老化时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1118_x3453_x1793981345}

[[\[Sysname\] mld-snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_x1732496055}

[[\[Sysname-mld-snooping\] quit]{lang="EN-US"}]{#struct_0_x1118_x3453_1309347692}

[[\[Sysname\] vlan 2]{lang="NL"}]{#struct_0_x1118_x3453_510624215}

[[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}]{#struct_0_x1118_x3453_1212164589}

[[\[Sysname-vlan2\] ipv6 pim-snooping enable]{lang="NL"}]{#struct_0_x1118_x3453_484300650}

[[\[Sysname-vlan2\] ipv6 pim-snooping ]{lang="NL"}[graceful-restart join-aging-time 300]{lang="EN-US"}]{#struct_0_x1118_x3453_x327126223}

[[\# ]{lang="NL"}]{#struct_0_x1118_x3453_x1214960184}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内配置主备倒换期间新主用主控板上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="NL"}[全局下游端口和全局路由器端口的老化时间为]{style="font-family:宋体"}[600]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x1118_x3453_1223215846}

[\[Sysname\] mld-snooping]{lang="NL"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="NL"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] ipv6 pim-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] ipv6 pim-snooping graceful-restart join-aging-time 600]{lang="NL"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x300918411}

[[·[              ]{style="font:7.0pt "}]{lang="NL" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 pim-snooping enable]{lang="NL"}**]{#struct_0_x1118_x3453_x1312844128}
:::::

::::: {#-646866882 .myid}
[]{#_Toc404790081}[]{#struct_0_x1118_x3453_514734637}[]{#_Toc334101957}[]{#_Toc323023219}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- ipv6 pim-snooping graceful-restart neighbor-aging-time**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6%20PIM%20Snooping命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1118_x3453_x1658751142}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1118_x3453_x1526537136}
:::

[ ]{lang="EN-US"}

[**[ipv6 pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**]{#struct_0_x1118_x3453_x1602807800}[命令用来配置主备倒换期间新主用主控板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[全局邻居端口的老化时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ipv6 pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**]{#struct_0_x1118_x3453_x1909208565}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x451557273}

[**[ipv6 pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1118_x3453_x840777168}

[**[undo ipv6 pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**]{#struct_0_x1118_x3453_x301377162}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1437159128}

[[主备倒换期间新]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1367819575}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[全局]{style="font-family:宋体"}[邻居端口老化时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x894950772}

[[VLAN]{lang="EN-US"}]{#struct_0_x1118_x3453_x1527372155}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_1658392946}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x440321023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_1329038730}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1370302279}

[*[interval]{lang="EN-US"}*]{#struct_0_x1118_x3453_x301442698}[：表示老化时间，取值范围为]{style="font-family:宋体"}[105]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1650980813}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局端口包括二层聚合接口、]{style="font-family:宋体"}]{#struct_0_x1118_x3453_1465867357}[AC]{lang="EN-US"}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等，由全局端口担任的邻居端口称为全局邻居端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1118_x3453_x387677436}[/VSI]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_2073993978}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_x194602031}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内配置主备倒换期间新]{style="font-family:宋体"}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[全局]{style="font-family:宋体"}[邻居端口的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1118_x3453_x1819198162}

[[\[Sysname\] mld-snooping]{lang="EN-US"}]{#struct_0_x1118_x3453_426825166}

[[\[Sysname-mld-snooping\] quit]{lang="EN-US"}]{#struct_0_x1118_x3453_1438495660}

[[\[Sysname\] vlan 2]{lang="NL"}]{#struct_0_x1118_x3453_x333722226}

[[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}]{#struct_0_x1118_x3453_x301508234}

[[\[Sysname-vlan2\] ipv6 pim-snooping enable]{lang="NL"}]{#struct_0_x1118_x3453_624858650}

[[\[Sysname-vlan2\] ipv6 pim-snooping ]{lang="NL"}[graceful-restart neighbor-aging-time 300]{lang="EN-US"}]{#struct_0_x1118_x3453_x1786287638}

[[\# ]{lang="NL"}]{#struct_0_x1118_x3453_x1215353401}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内配置主备倒换期间新主用主控板上]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="NL"}[全局邻居端口的老化时间为]{style="font-family:宋体"}[300]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x1118_x3453_x1215287865}

[\[Sysname\] mld-snooping]{lang="NL"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="NL"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] ipv6 pim-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] ipv6 pim-snooping graceful-restart neighbor-aging-time 300]{lang="NL"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1318504300}

[[·[              ]{style="font:7.0pt "}]{lang="NL" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 pim-snooping enable]{lang="NL"}**]{#struct_0_x1118_x3453_x403720599}
:::::

::: {#825154983 .myid}
[]{#_Toc404790082}[]{#struct_0_x1118_x3453_x1356992114}

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- reset ipv6 pim-snooping statistics**

------------------------------------------------------------------------

[**[reset ipv6 pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1118_x3453_474138729}[命令用来清除]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1327110219}

[**[reset ipv6 pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1118_x3453_x167967477}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x301573770}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1118_x3453_x1270907733}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_x1320649010}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_717722900}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x3453_x1794833972}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_344910664}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x3453_1210941335}[清除]{style="font-family:宋体"}[IPv6 PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 pim-snooping statistics]{lang="EN-US"}]{#struct_0_x1118_x3453_x165769374}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1118_x3453_129626409}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ ipv6 pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1118_x3453_1996499794}
:::
