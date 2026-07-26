::: {#-167645561 .myid}
[]{#_Toc323023217}[]{#_Toc404789359}[]{#struct_0_x1661_x1626_x2106681664}

**PIM Snooping \-- PIM Snooping命令 \-- display pim-snooping neighbor**

------------------------------------------------------------------------

[**[display pim-snooping neighbor]{lang="EN-US"}**]{#struct_0_x1661_x1626_468587742}[命令用来显示]{style="font-family:
宋体"}[PIM Snooping]{lang="EN-US"}[的邻居信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1021460775}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1184995590}

[**[display]{lang="EN-US"}**[ **pim-snooping** **neighbor** \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1661_x1626_942540238}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1661_x1626_x590333390}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display pim-snooping neighbor]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1661_x1626_880068617}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1661_x1626_1655080713}[模式：]{style="font-family:宋体"}

[**[display pim-snooping neighbor]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1661_x1626_x129948399}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x460282210}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x921040425}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x529530762}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_x1860763330}

[[network-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_x661713527}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_x250642635}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_2027293074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_336692457}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1661_x1626_1655277321}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1661_x1626_1517593182}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_1512568083}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_900442465}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_x1777512612}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1661_x1626_x1604381835}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1661_x1626_951370743}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1661_x1626_x1971459914}[：]{style="font-family:宋体"}[显示详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1676883420}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_x1771044930}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的邻居详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim-snooping neighbor vlan 2 verbose]{lang="EN-US"}]{#struct_0_x1661_x1626_1655211785}

[Total 2 neighbors.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 2 neighbors.]{lang="EN-US"}

[  10.1.1.2]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      GE1/0/1                             (02:02:23)    LAN Prune Delay(T)]{lang="EN-US"}

[  10.1.1.3]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      GE1/0/2                             (02:02:25)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_1517658718}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim-snooping neighbor vsi aaa]{lang="EN-US"}]{#struct_0_x1661_x1626_x1277056581}

[Total 2 neighbors.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 2 neighbors.]{lang="EN-US"}

[  10.0.0.1]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0 Link ID 2)          (00:01:32)]{lang="EN-US"}

[  10.0.0.4]{lang="EN-US"}

[    Slots (0 in total):]{lang="EN-US"}

[    Ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0 Link ID 1)          (00:01:41)]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[ display pim-snooping neighbor]{lang="EN-US"}]{#struct_0_x1661_x1626_1457434799}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1864962157}[[字段]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x26324440}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1699876082}

[[Total 2 neighbors]{lang="EN-US"}]{#struct_0_x1661_x1626_363310369}

[[PIM Snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_x87129829}[邻居的总数]{style="font-family:宋体"}

[[VLAN 2: Total 2 neighbors]{lang="EN-US"}]{#struct_0_x1661_x1626_1655408393}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1661_x1626_x514799251}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 2 neighbors]{lang="EN-US"}]{#struct_0_x1661_x1626_1517462110}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1661_x1626_x1637868693}[内的表项总数]{style="font-family:宋体"}

[[10.1.1.2]{lang="EN-US"}]{#struct_0_x1661_x1626_x1977810177}

[[PIM Snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_x1843714861}[邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Slots (0 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_1968599736}

[[本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x416275733}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1661_x1626_203549339}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1744929358}[PIM Snooping]{lang="EN-US"}[邻居的单板总数，以及各单板的槽位号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1711456657}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[邻居的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1614880453}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[邻居的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Ports (1 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_66006985}

[[PIM Snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_1655342857}[邻居所在的端口及总数]{style="font-family:宋体"}

[[(02:02:23)]{lang="EN-US"}]{#struct_0_x1661_x1626_x1597948928}

[[PIM Snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_1472416178}[邻居所在端口的老化剩余时间。需要注意的是，本字段对于全局口（包括二层聚合接口、]{style="font-family:宋体"}[AC]{lang="EN-US"}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等）将无条件显示，而对于非全局口：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_269646379}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_804273744}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1661_x1626_1923159633}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x322286285}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[LAN Prune Delay]{lang="EN-US"}]{#struct_0_x1661_x1626_269515307}

[[表示该邻居发出的]{style="font-family:宋体"}[PIM Hello]{lang="EN-US"}]{#struct_0_x1661_x1626_320073204}[报文中携带有]{style="font-family:宋体"}[LAN_Prune_Delay]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[(T)]{lang="EN-US"}]{#struct_0_x1661_x1626_x1847643559}

[[表示该邻居已禁止加入报文抑制能力]{style="font-family:宋体"}]{#struct_0_x1661_x1626_269449771}

[[AC (VSI index 0 Link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_1517396574}

[[AC]{lang="FR"}]{#struct_0_x1661_x1626_x111743362}[（]{style="font-family:宋体"}[Attachment Circuit]{lang="FR"}[，接入电路）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_x229083923}

[[N-PW]{lang="FR"}]{#struct_0_x1661_x1626_1518248542}[（]{style="font-family:宋体"}[Network Pseudowire]{lang="FR"}[，网络侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_x691557822}

[[U-PW]{lang="FR"}]{#struct_0_x1661_x1626_579574434}[（]{style="font-family:宋体"}[User facing Pseudowire]{lang="FR"}[，用户侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1071570939 .myid}
[]{#_Toc404789360}[]{#struct_0_x1661_x1626_1423372322}

**PIM Snooping \-- PIM Snooping命令 \-- display pim-snooping router-port**

------------------------------------------------------------------------

[**[display pim-snooping router-port]{lang="EN-US"}**]{#struct_0_x1661_x1626_x1617486533}[命令用来显示]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的路由器端口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x667275988}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x272668768}

[**[display pim-snooping router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x1661_x1626_1632853483}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1661_x1626_1655539465}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display pim-snooping router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1661_x1626_x520137560}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1661_x1626_1814989879}[模式：]{style="font-family:宋体"}

[**[display pim-snooping router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1661_x1626_x2095762370}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1765233047}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1754386560}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1168705558}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_2132187767}

[[network-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_x1418286494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_x284391197}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_1655473929}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1925957309}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1661_x1626_382123550}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1661_x1626_x1211159096}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_2047593803}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_x741424419}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_x1017997725}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1661_x1626_236863202}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1661_x1626_2082254711}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_809644225}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_x971143015}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的路由器端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim-snooping router-port vlan 2]{lang="EN-US"}]{#struct_0_x1661_x1626_803880528}

[VLAN 2:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    GE1/0/1                             (00:01:30)]{lang="EN-US"}

[    GE1/0/2                             (00:01:32)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_x1211093560}[显示]{style="font-family:宋体"}[VSI aaa ]{lang="EN-US"}[内]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[的路由器端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim-snooping router-port vsi aaa]{lang="EN-US"}]{#struct_0_x1661_x1626_x1211290168}

[VSI aaa:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    AC (VSI index 0 Link ID 0)          (00:02:50)]{lang="EN-US"}

[    AC (VSI index 0 Link ID 1)          (00:02:59)]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display pim-snooping router-port]{lang="EN-US"}]{#struct_0_x1661_x1626_x1122275358}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1862791587}[[字段]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x877364708}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1661_x1626_822858890}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1661_x1626_1654949642}

[[VLAN]{lang="EN-US"}]{#struct_0_x1661_x1626_x1680321494}[的编号]{style="font-family:宋体"}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1661_x1626_x490459950}

[[VSI]{lang="EN-US"}]{#struct_0_x1661_x1626_x1211224632}[的名称]{style="font-family:宋体"}

[[Router slots (1 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_x2008545449}

[[本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_721986956}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1661_x1626_203549342}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有路由器端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1661_x1626_976059835}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x418329485}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有路由器端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1267531135}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Router ports (2 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_1612717286}

[[路由器端口及总数]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x588088986}

[[(00:01:30)]{lang="EN-US"}]{#struct_0_x1661_x1626_2107744037}

[[路由器端口的老化剩余时间。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_1655146250}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_269253162}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x2012190382}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1661_x1626_202515275}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1661_x1626_453316655}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_x1211421240}

[[AC]{lang="FR"}]{#struct_0_x1661_x1626_x1211355704}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_609806628}

[[N-PW]{lang="FR"}]{#struct_0_x1661_x1626_x1211552312}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_x1147034422}

[[U-PW]{lang="FR"}]{#struct_0_x1661_x1626_1768541414}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#835686562 .myid}
[]{#_Toc323023218}[]{#_Toc404789361}[]{#struct_0_x1661_x1626_x1694230915}

**PIM Snooping \-- PIM Snooping命令 \-- display pim-snooping routing-table**

------------------------------------------------------------------------

[**[display pim-snooping routing-table]{lang="EN-US"}**]{#struct_0_x1661_x1626_x622613604}[命令用来显示]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[路由表]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1776132246}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_1655080714}

[**[display pim-snooping routing-table ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1661_x1626_x130276079}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1661_x1626_x906626892}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display pim-snooping routing-table ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1661_x1626_181459681}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1661_x1626_1445588409}[模式：]{style="font-family:宋体"}

[**[display pim-snooping routing-table ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1661_x1626_1020717067}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_736214762}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1661_x1626_68315750}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_113098093}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_1655277322}

[[network-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_1512633619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_550414098}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_309662414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_182919901}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1661_x1626_665865525}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1661_x1626_x1210569272}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_32882521}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_x115900869}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1661_x1626_2114104621}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1661_x1626_338481916}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1661_x1626_x502674771}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1661_x1626_x1692123835}[：]{style="font-family:宋体"}[显示详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1655211786}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_1457238191}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[路由表]{style="font-family:宋体"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim-snooping routing-table vlan 2 verbose]{lang="EN-US"}]{#struct_0_x1661_x1626_804208209}

[Total 1 entries.]{lang="EN-US"}

[FSM Flag: NI-no info, J-join, PP-prune pending]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 entries.]{lang="EN-US"}

[  (172.10.10.1, 225.1.1.1)]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Upstream neighbor: 20.1.1.1]{lang="EN-US"}

[      Upstream Slots (0 in total):]{lang="EN-US"}

[      Upstream Ports (1 in total):]{lang="EN-US"}

[        GE1/0/1]{lang="EN-US"}

[      Downstream Slots (0 in total):]{lang="EN-US"}

[      Downstream Ports (2 in total):]{lang="EN-US"}

[        GE1/0/2]{lang="EN-US"}

[          Expires: 00:03:01, FSM: J]{lang="EN-US"}

[          Downstream Neighbors (2 in total):]{lang="EN-US"}

[            7.1.1.1]{lang="EN-US"}

[              Expires: 00:59:19, FSM: J]{lang="EN-US"}

[            7.1.1.11]{lang="EN-US"}

[              Expires: 00:59:20, FSM: J]{lang="EN-US"}

[        GE1/0/3]{lang="EN-US"}

[          Expires: 00:02:21, FSM: PP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_x1211159097}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim-snooping routing-table vsi aaa]{lang="EN-US"}]{#struct_0_x1661_x1626_737167098}

[Total 1 entries.]{lang="EN-US"}

[FSM Flag: NI-no info, J-join, PP-prune pending]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 entries.]{lang="EN-US"}

[  (172.10.10.1, 225.1.1.1)]{lang="EN-US"}

[    Upstream neighbor: 20.1.1.1]{lang="EN-US"}

[      Upstream Slots (0 in total):]{lang="EN-US"}

[      Upstream Ports (1 in total):]{lang="EN-US"}

[        AC (VSI index 0 Link ID 0)]{lang="EN-US"}

[      Downstream Slots (0 in total):]{lang="EN-US"}

[      Downstream Ports (1 in total):]{lang="EN-US"}

[        AC (VSI index 0 Link ID 1)]{lang="EN-US"}

[           Expires: 00:03:23, FSM: J]{lang="EN-US"}

[]{#struct_0_x1661_x1626_1655539466}[[表1-3 ]{lang="EN-US"}[display pim-snooping routing-table]{lang="EN-US"}]{#_Toc252534573}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1869462520}[[字段]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x520072024}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x153359957}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x1661_x1626_x925031830}

[[PIM Snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_1983345936}[路由表中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）与（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的总数]{style="font-family:宋体"}

[[FSM Flag: NI-no info, J-join, PP-prune pending]{lang="EN-US"}]{#struct_0_x1661_x1626_230801055}

[[下游端口的状态机标识：]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_x1661_x1626_2072123246}[表示初始状态，]{style="font-family:宋体"}[J]{lang="EN-US"}[表示加入状态，]{style="font-family:宋体"}[PP]{lang="EN-US"}[表示剪枝未决状态]{style="font-family:宋体"}

[[(172.10.10.1, 225.1.1.1)]{lang="EN-US"}]{#struct_0_x1661_x1626_1655473930}

[[PIM Snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_1926416062}[路由表中的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[FSM information]{lang="EN-US"}]{#struct_0_x1661_x1626_268794410}

[[表项状态机，包括：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1134609389}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_x1661_x1626_269384233}[：表示所有成员属性均已删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dummy]{lang="FR"}]{#struct_0_x1661_x1626_58024330}[：表示新创建的临时表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[no info]{lang="FR"}]{#struct_0_x1661_x1626_269318697}[：表示没有表项存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[normal]{lang="FR"}]{#struct_0_x1661_x1626_1210660091}[：表示主控板通知创建的正式表项]{style="font-family:宋体"}

[[Upstream neighbor]{lang="EN-US"}]{#struct_0_x1661_x1626_x899397084}

[[上游邻居]{style="font-family:宋体"}]{#struct_0_x1661_x1626_155949671}

[[Upstream Slots (0 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_x52991765}

[[本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_2040827164}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1752765798}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有上游邻居的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x78195172}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x2146256405}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有上游邻居的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1661_x1626_2020361206}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有上游邻居的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Upstream Ports (1 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_1655015175}

[[上游邻居所在的端口及总数。需要注意的是，本字段：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x2015175152}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_269187625}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若上游端口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x249575844}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1435847838}[IRF]{lang="EN-US"}[设备上，若上游端口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x715702060}[IRF]{lang="EN-US"}[模式上，若上游端口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[Downstream Slots (1 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_1654949639}

[[除当前单板外其它所有有]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1681042393}[下游端口的单板的槽位及总数。本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Downstream Ports (2 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_841845836}

[[下游端口及总数]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x100285668}

[[Downstream Neighbors (2 in total)]{lang="EN-US"}]{#struct_0_x1661_x1626_269449769}

[[下游端口包含的下游邻居及总数]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x2076917439}

[[Expires: 00:03:01, FSM: J]{lang="EN-US"}]{#struct_0_x1661_x1626_x1159514175}

[[下游端口或下游邻居的老化剩余时间和状态机。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：]{style="font-family:宋体"}]{#struct_0_x1661_x1626_1573575971}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_269318696}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1661_x1626_1655146247}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x2011862701}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1661_x1626_787167590}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_x1211224633}

[[AC]{lang="FR"}]{#struct_0_x1661_x1626_x1211421241}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_403392543}

[[N-PW]{lang="FR"}]{#struct_0_x1661_x1626_x1211355705}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1661_x1626_x956277313}

[[U-PW]{lang="FR"}]{#struct_0_x1661_x1626_x1211552313}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1747882245 .myid}
[]{#_Toc404789362}[]{#struct_0_x1661_x1626_x1673156035}

**PIM Snooping \-- PIM Snooping命令 \-- display pim-snooping statistics**

------------------------------------------------------------------------

[**[display pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1661_x1626_2123257863}[命令用来显示]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1655277319}

[**[display pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1661_x1626_1512043798}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1396201652}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x621174946}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1935158884}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_903526860}

[[network-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_x1012082755}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_1860146875}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1661_x1626_1055199058}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x878029516}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_1655211783}[显示]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim-snooping statistics]{lang="EN-US"}]{#struct_0_x1661_x1626_1457565871}

[[Received PIMv2 hello:  100]{lang="EN-US"}]{#struct_0_x1661_x1626_x2025136798}

[[Received PIMv2 join/prune:  100]{lang="EN-US"}]{#struct_0_x1661_x1626_x749575660}

[[Received PIMv2 error:  0]{lang="EN-US"}]{#struct_0_x1661_x1626_441037667}

[[Received PIMv2 messages in total:  200]{lang="EN-US"}]{#struct_0_x1661_x1626_492165426}

[[Received PIMv1 messages in total:  0]{lang="EN-US"}]{#struct_0_x1661_x1626_x1709028043}[]{#_Toc252534575}

[[表1-4 ]{lang="EN-US"}[display pim-snooping statistics]{lang="EN-US"}]{#struct_0_x1661_x1626_x125145328}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1868426084}[[字段]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1279155454}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1655408391}

[[Received PIMv2 hello]{lang="EN-US"}]{#struct_0_x1661_x1626_x514930323}

[[收到的]{style="font-family:宋体"}[PIMv2 Hello]{lang="EN-US"}]{#struct_0_x1661_x1626_x1542073597}[报文数]{style="font-family:宋体"}

[[Received PIMv2 join/prune]{lang="EN-US"}]{#struct_0_x1661_x1626_1145448305}

[[收到的]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}]{#struct_0_x1661_x1626_x1609242582}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文数]{style="font-family:宋体"}

[[Received PIMv2 error]{lang="EN-US"}]{#struct_0_x1661_x1626_277742029}

[[收到的错误]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}]{#struct_0_x1661_x1626_471083264}[报文数]{style="font-family:宋体"}

[[Received PIMv2 messages in total]{lang="EN-US"}]{#struct_0_x1661_x1626_1655342855}

[[收到的]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}]{#struct_0_x1661_x1626_x1598080000}[报文总数]{style="font-family:宋体"}

[[Received PIMv1 messages in total]{lang="EN-US"}]{#struct_0_x1661_x1626_496680726}

[[收到的]{style="font-family:宋体"}[PIMv1]{lang="EN-US"}]{#struct_0_x1661_x1626_2004381080}[报文总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc323023219}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1593275543}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1661_x1626_x2028972720}

::: {#-1103764540 .myid}
[]{#_Toc404789363}[]{#struct_0_x1661_x1626_2071977413}

**PIM Snooping \-- PIM Snooping命令 \-- pim-snooping enable**

------------------------------------------------------------------------

[**[pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1661_x1626_675311171}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内使能]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1661_x1626_1655539463}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内关闭]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x520268632}

[**[pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1661_x1626_x2100714100}

[**[undo pim-snooping enable]{lang="EN-US"}**]{#struct_0_x1661_x1626_x1007631090}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1823621765}

[[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1661_x1626_x2023200068}[内的]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_293552906}

[[VLAN]{lang="EN-US"}]{#struct_0_x1661_x1626_x283756292}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x607506868}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_1655473927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_1926350525}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x935250939}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1661_x1626_x1791696402}[内使能]{lang="EN-US" style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[之前，必须先在]{lang="EN-US" style="font-family:宋体"}[全局以及]{style="font-family:宋体"}[该]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在组播]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1661_x1626_x154613632}[的子]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[无效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1299027191}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_1454951743}[全局使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[和]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1661_x1626_442871635}

[[\[Sysname\] igmp-snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_1080702479}

[[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}]{#struct_0_x1661_x1626_80711138}

[[\[Sysname\] vlan 2]{lang="NL"}]{#struct_0_x1661_x1626_1655015176}

[[\[Sysname-vlan2\] igmp-snooping enable]{lang="NL"}]{#struct_0_x1661_x1626_x2015371760}

[[\[Sysname-vlan2\] pim-snooping enable]{lang="NL"}]{#struct_0_x1661_x1626_x1944068824}

[[\# ]{lang="NL"}]{#struct_0_x1661_x1626_x1211355702}[全局使能]{style="font-family:宋体"}[IGMP Snooping]{lang="NL"}[，并在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="NL"}[和]{style="font-family:宋体"}[PIM Snooping]{lang="NL"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x1661_x1626_x1211552310}

[\[Sysname\] igmp-snooping]{lang="NL"}

[\[Sysname-igmp-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="NL"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] pim-snooping enable]{lang="NL"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_252802272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping]{lang="EN-US"}**]{#struct_0_x1661_x1626_x1860956014}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/IGMP Snooping]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1661_x1626_x2023960283}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/IGMP Snooping]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-379617962 .myid}
[]{#_Toc404789364}[]{#struct_0_x1661_x1626_35016793}[]{#_Toc334101958}

**PIM Snooping \-- PIM Snooping命令 \-- pim-snooping graceful-restart join-aging-time**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PIM%20Snooping命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1661_x1626_950218080}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1661_x1626_1972257234}
:::

[ ]{lang="EN-US"}

[**[pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**]{#struct_0_x1661_x1626_1654949640}[命令用来配置主备倒换期间新主用主控板上]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[全局下游端口和全局路由器端口的老化时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**]{#struct_0_x1661_x1626_x1680452566}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_907165877}

[**[pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1661_x1626_1903668622}

[**[undo pim-snooping graceful-restart join-aging-time]{lang="EN-US"}**]{#struct_0_x1661_x1626_1526384766}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_616391064}

[[主备倒换期间新]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x173394190}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[全局下游端口和全局路由器端口的老化时间]{style="font-family:宋体"}[为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_716821651}

[[VLAN]{lang="EN-US"}]{#struct_0_x1661_x1626_561313189}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1655146248}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_x2012714669}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_1816913433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1063147988}

[*[interval]{lang="EN-US"}*]{#struct_0_x1661_x1626_1223331306}[：表示老化时间，取值范围为]{style="font-family:宋体"}[210]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_91334814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局端口包括二层聚合接口、]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x845573721}[AC]{lang="EN-US"}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等，由全局端口担任的下游端口和路由器端口分别称为全局下游端口和全局路由器端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1661_x1626_1074896018}[/VSI]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x378277984}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_1291208924}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内配置主备倒换期间新]{style="font-family:宋体"}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[全局]{style="font-family:宋体"}[下游端口和全局路由器端口的老化时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1661_x1626_1655080712}

[[\[Sysname\] igmp-snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_x129882863}

[[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}]{#struct_0_x1661_x1626_x472323312}

[[\[Sysname\] vlan 2]{lang="NL"}]{#struct_0_x1661_x1626_1044543162}

[[\[Sysname-vlan2\] igmp-snooping enable]{lang="NL"}]{#struct_0_x1661_x1626_x973549934}

[[\[Sysname-vlan2\] pim-snooping enable]{lang="NL"}]{#struct_0_x1661_x1626_x1415976724}

[[\[Sysname-vlan2\] pim-snooping ]{lang="NL"}[graceful-restart join-aging-time 600]{lang="EN-US"}]{#struct_0_x1661_x1626_x257824688}

[[\# ]{lang="NL"}]{#struct_0_x1661_x1626_x1210569270}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内配置主备倒换期间新主用主控板上]{style="font-family:宋体"}[PIM Snooping]{lang="NL"}[全局下游端口和全局路由器端口的老化时间为]{style="font-family:宋体"}[600]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x1661_x1626_x1211159095}

[\[Sysname\] igmp-snooping]{lang="NL"}

[\[Sysname-igmp-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="NL"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] pim-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] pim-snooping graceful-restart join-aging-time 600]{lang="NL"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1830346583}

[[·[              ]{style="font:7.0pt "}]{lang="NL" style="font-size:10.0pt;font-family:Symbol"}**[pim-snooping enable]{lang="NL"}**]{#struct_0_x1661_x1626_x1193009799}
:::::

::::: {#1666925298 .myid}
[]{#_Toc404789365}[]{#struct_0_x1661_x1626_1655277320}[]{#_Toc334101957}

**PIM Snooping \-- PIM Snooping命令 \-- pim-snooping graceful-restart neighbor-aging-time**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PIM%20Snooping命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1661_x1626_1512502547}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1661_x1626_941890375}
:::

[ ]{lang="EN-US"}

[**[pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**]{#struct_0_x1661_x1626_x828717494}[命令用来配置主备倒换期间新主用主控板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[全局邻居端口的老化时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**]{#struct_0_x1661_x1626_1876593897}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1861506808}

[**[pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1661_x1626_283503731}

[**[undo pim-snooping graceful-restart neighbor-aging-time]{lang="EN-US"}**]{#struct_0_x1661_x1626_739158730}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_201372447}

[[主备倒换期间新]{style="font-family:宋体"}]{#struct_0_x1661_x1626_598133494}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[全局]{style="font-family:宋体"}[邻居端口老化时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1655211784}

[[VLAN]{lang="EN-US"}]{#struct_0_x1661_x1626_1457369263}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x1254861457}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_1856883435}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_x1616853447}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_31569535}

[*[interval]{lang="EN-US"}*]{#struct_0_x1661_x1626_x200296646}[：表示老化时间，取值范围为]{style="font-family:宋体"}[105]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x691611150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局端口包括二层聚合接口、]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1401048624}[AC]{lang="EN-US"}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等，由全局端口担任的邻居端口称为全局邻居端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1661_x1626_1770440990}[/VSI]{lang="EN-US"}[内使能]{lang="EN-US" style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1655408392}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_x514733715}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内配置主备倒换期间新]{style="font-family:宋体"}[主用]{style="font-family:宋体"}[主控板上]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[全局]{style="font-family:宋体"}[邻居端口的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1661_x1626_x374246163}

[[\[Sysname\] igmp-snooping]{lang="EN-US"}]{#struct_0_x1661_x1626_1635499385}

[[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}]{#struct_0_x1661_x1626_1316111579}

[[\[Sysname\] vlan 2]{lang="NL"}]{#struct_0_x1661_x1626_1577881710}

[[\[Sysname-vlan2\] igmp-snooping enable]{lang="NL"}]{#struct_0_x1661_x1626_x939540636}

[[\[Sysname-vlan2\] pim-snooping enable]{lang="NL"}]{#struct_0_x1661_x1626_x1736973709}

[[\[Sysname-vlan2\] pim-snooping ]{lang="NL"}[graceful-restart neighbor-aging-time 300]{lang="EN-US"}]{#struct_0_x1661_x1626_888389399}

[[\# ]{lang="NL"}]{#struct_0_x1661_x1626_x1211224631}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内配置主备倒换期间新主用主控板上]{style="font-family:宋体"}[PIM Snooping]{lang="NL"}[全局邻居端口的老化时间为]{style="font-family:宋体"}[300]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x1661_x1626_x1211421239}

[\[Sysname\] igmp-snooping]{lang="NL"}

[\[Sysname-igmp-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="NL"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] pim-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] pim-snooping graceful-restart neighbor-aging-time 300]{lang="NL"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1655342856}

[[·[              ]{style="font:7.0pt "}]{lang="NL" style="font-size:10.0pt;font-family:Symbol"}**[pim-snooping enable]{lang="NL"}**]{#struct_0_x1661_x1626_x1597883392}
:::::

::: {#-1376233027 .myid}
[]{#_Toc334101960}[]{#_Toc404789366}[]{#struct_0_x1661_x1626_x816720510}

**PIM Snooping \-- PIM Snooping命令 \-- reset pim-snooping statistics**

------------------------------------------------------------------------

[**[reset pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1661_x1626_861328065}[命令用来清除]{style="font-family:
宋体"}[PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1743986418}

[**[reset pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1661_x1626_891717387}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_265863425}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1661_x1626_x1537522072}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_293445117}

[[network-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_899519618}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1661_x1626_1655539464}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_x520203096}

[[\# ]{lang="EN-US"}]{#struct_0_x1661_x1626_x1726718337}[清除]{style="font-family:宋体"}[PIM Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset pim-snooping statistics]{lang="EN-US"}]{#struct_0_x1661_x1626_251684591}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1661_x1626_1478120715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ pim-snooping statistics]{lang="EN-US"}**]{#struct_0_x1661_x1626_x2080492311}
:::
