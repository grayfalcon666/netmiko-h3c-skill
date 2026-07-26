::: {#-1219388899 .myid}
[]{#_Toc121110292}[]{#_Toc404790090}[]{#struct_0_x6470_x2019_x704137401}[]{#_Toc349815537}

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast ip**

------------------------------------------------------------------------

[**[display ipv6 l2-multicast ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_x297251153}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x320950045}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1177812551}

[**[display ipv6 l2-multicast ip ]{lang="EN-US"}**[\[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_652586825}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_744930365}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast ip ]{lang="EN-US"}**[\[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_1970451801}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_229359592}[模式：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast ip ]{lang="EN-US"}**[\[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x67786210}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x95359944}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x704202937}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1001453688}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1532577753}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x1680230751}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1600290074}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x991157202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1100703171}

[**[group]{lang="EN-US"}**[ *ipv6-group-address*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1743250716}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ ipv6-source-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_1250645509}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x704661692}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x46459138}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1851038137}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_79365320}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1162049908}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_2048781771}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1109223886}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_1080409734}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x100488234}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x798386629}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast ip vlan 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x704727228}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 IP entries.]{lang="EN-US"}

[   (::, FF1E::101)]{lang="EN-US"}

[    Attribute: static, success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/1                             (S, SUC)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x46524674}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast ip vsi aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x45803778}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 IP entries.]{lang="EN-US"}

[  (::, FF1E::101)]{lang="EN-US"}

[    Attribute: ]{lang="EN-US"}[dynamic]{lang="FR"}[, success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)         (D, SUC)]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ipv6 l2-multicast ip]{lang="EN-US"}]{#struct_0_x6470_x2019_x1437315245}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2029850417}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1579430374}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x356895615}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x6470_x2019_1010281477}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1542688973}

[[VLAN 2: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x195696538}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x704792764}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x6470_x2019_573817184}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_21794648}[内的表项总数]{style="font-family:宋体"}

[[(::, FF1E::101)]{lang="EN-US"}]{#struct_0_x6470_x2019_921503824}

[[（]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1617705079}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[::]{lang="FR"}[表示所有]{style="font-family:宋体"}[IPv6]{lang="FR"}[组播源]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x6470_x2019_x590761627}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1045515862}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="FR"}]{#struct_0_x6470_x2019_973923329}[：表示由动态协议创建的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[static]{lang="FR"}]{#struct_0_x6470_x2019_830252936}[：表示由静态协议创建的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[pim]{lang="FR"}]{#struct_0_x6470_x2019_x704858300}[：表示由]{style="font-family:宋体"}[IPv6 PIM]{lang="FR"}[协议创建的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[kernel]{lang="FR"}]{#struct_0_x6470_x2019_1651742397}[：表示从内核中获取的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="FR"}]{#struct_0_x6470_x2019_1734491008}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[处理]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="FR"}]{#struct_0_x6470_x2019_1950261243}[：表示处理失败]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_1659154620}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x704923836}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1974566844}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1974566843}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1607274494}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_740452477}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x615350996}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_2083574354}

[[(S, SUC)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1645068925}

[[端口属性，包括：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_2027754098}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="FR"}]{#struct_0_x6470_x2019_x704989372}[：表示动态端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="FR"}]{#struct_0_x6470_x2019_116001590}[：表示静态端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="FR"}]{#struct_0_x6470_x2019_x38692141}[：表示]{style="font-family:宋体"}[IPv6]{lang="FR"}[ PIM]{lang="FR"}[端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[K]{lang="FR"}]{#struct_0_x6470_x2019_1650702827}[：表示从内核中获取的端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="FR"}]{#struct_0_x6470_x2019_1368275831}[：表示从（]{style="font-family:宋体"}[\*]{lang="FR"}[，]{style="font-family:宋体"}[\*]{lang="FR"}[）表项扩展的端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="FR"}]{#struct_0_x6470_x2019_x705054908}[：表示从（]{style="font-family:宋体"}[\*]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项扩展的端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[SUC]{lang="FR"}]{#struct_0_x6470_x2019_x1419722007}[：表示处理成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="FR"}]{#struct_0_x6470_x2019_644381745}[：表示处理失败]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x46393603}

[[AC]{lang="FR"}]{#struct_0_x6470_x2019_x1437999798}[（]{style="font-family:宋体"}[Attachment Circuit]{lang="FR"}[，接入电路）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_207174700}

[[N-PW]{lang="FR"}]{#struct_0_x6470_x2019_x46196995}[（]{style="font-family:宋体"}[Network Pseudowire]{lang="FR"}[，网络侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_1906897257}

[[U-PW]{lang="FR"}]{#struct_0_x6470_x2019_542277814}[（]{style="font-family:宋体"}[User facing Pseudowire]{lang="FR"}[，用户侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1711022543 .myid}
[]{#_Toc404790091}[]{#struct_0_x6470_x2019_x339615665}

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast ip forwarding**

------------------------------------------------------------------------

[**[display ipv6 l2-multicast ip forwarding]{lang="EN-US"}**]{#struct_0_x6470_x2019_1160551376}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1227110465}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1693703382}

[**[display ipv6 l2-multicast ip forwarding]{lang="EN-US"}**[ \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x705120444}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_896725210}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast ip forwarding]{lang="EN-US"}**[ \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x702916915}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_1050270459}[模式：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast ip forwarding]{lang="EN-US"}**[ \[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x585226922}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_132328827}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x175056645}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1346420025}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x704137404}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x296923473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_850446516}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x1692105709}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1583697767}

[**[group]{lang="EN-US"}**[ *ipv6-group-address*]{lang="EN-US"}]{#struct_0_x6470_x2019_x889399676}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ ipv6-source-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1886448557}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1024003821}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x46590211}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1030105600}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x704202940}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1565334435}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1001388155}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_915902192}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_1163548920}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1200515358}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1631008329}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast ip forwarding vlan 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x767641100}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 IP entries.]{lang="EN-US"}

[   (::, FF1E::101)]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (3 in total):]{lang="EN-US"}

[      GE1/0/1]{lang="EN-US"}

[      GE1/0/2]{lang="EN-US"}

[      GE1/0/3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x46655747}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast ip forwarding vsi aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x46459139}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 IP entries.]{lang="EN-US"}

[  (::, FF1E::101)]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 l2-multicast ip forwarding]{lang="EN-US"}]{#struct_0_x6470_x2019_x61499872}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2027504311}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x704661691}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1850841529}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x1769261332}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1170323173}

[[VLAN 2: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x1907196023}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_16460801}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x770402871}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x46524675}[内的表项总数]{style="font-family:宋体"}

[[(::, FF1E::101)]{lang="EN-US"}]{#struct_0_x6470_x2019_1615934489}

[[（]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x704727227}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[::]{lang="EN-US"}[表示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1437642925}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1416604360}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_18251710}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1461872449}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1762042071}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1702669498}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (3 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1200505794}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1248713206}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x45803779}

[[AC]{lang="FR"}]{#struct_0_x6470_x2019_573817183}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_21794653}

[[N-PW]{lang="FR"}]{#struct_0_x6470_x2019_x45869315}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x261516035}

[[U-PW]{lang="FR"}]{#struct_0_x6470_x2019_x46328064}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1219374003 .myid}
[]{#_Toc109290001}[]{#_Toc404790092}[]{#struct_0_x6470_x2019_1330433754}[]{#_Toc349815539}

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast mac**

------------------------------------------------------------------------

[**[display ipv6 l2-multicast mac]{lang="EN-US"}**]{#struct_0_x6470_x2019_x704792763}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_921045072}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1797792331}

[**[display ipv6 l2-multicast mac ]{lang="EN-US"}**[\[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_389181202}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_x860265077}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast mac ]{lang="EN-US"}**[\[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x148543582}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_x1082155876}[模式：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast mac ]{lang="EN-US"}**[\[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x1971202618}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1557525776}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x704858299}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x687499578}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1875503949}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_24600963}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x654246064}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_1116681790}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2091552847}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_1394369309}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1924120739}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x46196992}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x704923835}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x615154388}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1613887614}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_2025235581}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_174487736}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_1080082053}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x685192876}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_190339885}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast mac vlan 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x362821406}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 3333-0000-0101]{lang="EN-US"}

[    Attribute: success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x46262528}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast mac vsi aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x275748715}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 0100-5e01-0101]{lang="EN-US"}

[    Attribute: success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ipv6 l2-multicast mac]{lang="EN-US"}]{#struct_0_x6470_x2019_x704989371}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1732185261}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_115936054}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x941284048}

[[Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x6470_x2019_1945714236}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1445695220}

[[VLAN 2: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x1860135151}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x360125029}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x46590208}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_801311463}[内的表项总数]{style="font-family:宋体"}

[[MAC group address]{lang="EN-US"}]{#struct_0_x6470_x2019_x705054907}

[[MAC]{lang="FR"}]{#struct_0_x6470_x2019_x1419656471}[组播组的地址]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x6470_x2019_239026122}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x149825715}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="FR"}]{#struct_0_x6470_x2019_x1448037376}[：]{style="font-family:宋体"}[表示处理成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="FR"}]{#struct_0_x6470_x2019_442013419}[：]{style="font-family:宋体"}[表示处理失败]{lang="EN-US" style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x705120443}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_896397530}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_18251705}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1469766620}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1667563799}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_18251704}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x2019773053}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1671641978}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x46655744}

[[AC]{lang="FR"}]{#struct_0_x6470_x2019_x46459136}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x770402878}

[[N-PW]{lang="FR"}]{#struct_0_x6470_x2019_x46524672}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_1943919682}

[[U-PW]{lang="FR"}]{#struct_0_x6470_x2019_x45803776}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1725959139 .myid}
[]{#_Toc404790093}[]{#struct_0_x6470_x2019_x2026455004}

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast mac forwarding**

------------------------------------------------------------------------

[**[display ipv6 l2-multicast mac forwarding]{lang="EN-US"}**]{#struct_0_x6470_x2019_500547560}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1628284303}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x704137403}

[**[display ipv6 l2-multicast mac forwarding]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x297120081}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_466625946}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast mac forwarding]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_2127695559}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_2121517525}[模式：]{style="font-family:宋体"}

[**[display ipv6 l2-multicast mac forwarding]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x1796951323}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x435571601}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x69243431}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x387712879}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x704202939}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x1000798328}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1902471019}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x1558865920}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1999309278}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1213382820}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_1890381000}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x46328065}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1096606773}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_174408090}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_270340593}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x704661694}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_1051680496}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x936275041}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1851169209}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x404740262}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast mac forwarding vlan 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x669191805}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 3333-0000-0101]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (3 in total):]{lang="EN-US"}

[      GE1/0/1]{lang="EN-US"}

[      GE1/0/2]{lang="EN-US"}

[      GE1/0/3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x46393601}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 l2-multicast mac forwarding vsi aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x46196993}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 0100-5e01-0101]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ipv6 l2-multicast mac forwarding]{lang="EN-US"}]{#struct_0_x6470_x2019_310613339}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1728394971}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x704727230}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1437839534}

[[Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x6470_x2019_723955024}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1403389194}

[[VLAN 2: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x6470_x2019_276137987}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x421390743}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x46262529}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x275748716}[内的表项总数]{style="font-family:宋体"}

[[MAC group address]{lang="EN-US"}]{#struct_0_x6470_x2019_1225588987}

[[MAC]{lang="FR"}]{#struct_0_x6470_x2019_x704792766}[组播组的地址]{style="font-family:宋体"}

[[Host slots (1 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_921372752}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1471309975}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1938063426}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_601775758}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1961777964}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1938063427}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (3 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_1557493527}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1435842883}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x46590209}

[[AC]{lang="FR"}]{#struct_0_x6470_x2019_x46655745}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_1820086631}

[[N-PW]{lang="FR"}]{#struct_0_x6470_x2019_x46459137}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x46524673}

[[U-PW]{lang="FR"}]{#struct_0_x6470_x2019_1943919681}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#166534308 .myid}
[]{#_Toc404790094}[]{#struct_0_x6470_x2019_2059210903}

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mld-snooping**]{lang="EN-US"}]{#struct_0_x6470_x2019_1568151630}[命令用来显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1097910344}

[**[display]{lang="EN-US"}**[ **mld-snooping** \[ **global** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x704858302}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1651611325}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_157200433}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_432539509}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_519946484}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_545921693}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_2090096810}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x1368115869}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1459086957}

[**[global]{lang="EN-US"}**]{#struct_0_x6470_x2019_x865433391}[：显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的全局状态信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x704923838}[：显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x45869313}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x614957780}

[[如果未指定任何可选参数，将显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_2027374500}[在全局以及所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x389393328}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x865611792}[显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[在全局以及所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x704989374}

[MLD snooping information: Global]{lang="EN-US"}

[ MLD snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Disabled]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-listener-query-interval: 1s]{lang="EN-US"}

[ Report-aggregation: Enabled]{lang="EN-US"}

[ Dot1p-priority: \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[MLD snooping information: VLAN 1]{lang="EN-US"}

[ MLD snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Disabled]{lang="EN-US"}

[ Version: 1]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-listener-query-interval: 1s]{lang="EN-US"}

[ Querier: Disabled]{lang="EN-US"}

[ Query-interval: 125s]{lang="EN-US"}

[ General-query source IP: FE80::2FF:FFFF:FE00:1]{lang="EN-US"}

[ Special-query source IP: FE80::2FF:FFFF:FE00:1]{lang="EN-US"}

[ Report source IP: FE80::2FF:FFFF:FE00:2]{lang="EN-US"}

[ Done source IP: FE80::2FF:FFFF:FE00:3]{lang="EN-US"}

[ Dot1p-priority: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[MLD snooping information: VLAN 10]{lang="EN-US"}

[ MLD snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Enabled]{lang="EN-US"}

[ Version: 2]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-listener-query-interval: 1s]{lang="EN-US"}

[ Querier: Disabled]{lang="EN-US"}

[ Query-interval: 125s]{lang="EN-US"}

[ General-query source IP: FE80::2FF:FFFF:FE00:1]{lang="EN-US"}

[ Special-query source IP: FE80::2FF:FFFF:FE00:1]{lang="EN-US"}

[ Report source IP: FE80::2FF:FFFF:FE00:2]{lang="EN-US"}

[ Done source IP: FE80::2FF:FFFF:FE00:3]{lang="EN-US"}

[ Dot1p-priority: \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[MLD snooping information: VSI aaa]{lang="EN-US"}

[ MLD snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Enabled]{lang="EN-US"}

[ Version: 1]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-listener-query-interval: 1s]{lang="EN-US"}

[ Querier: Disabled]{lang="EN-US"}

[ Query-interval: 125s]{lang="EN-US"}

[ General-query source IP: FE80::2FF:FFFF:FE00:1]{lang="EN-US"}

[ Special-query source IP: FE80::2FF:FFFF:FE00:1]{lang="EN-US"}

[]{#struct_0_x6470_x2019_115608374}[[表1-5 ]{lang="EN-US"}[display mld-snooping]{lang="EN-US"}]{#_Toc288831908}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1735061713}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_360957764}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_438139297}

[[MLD snooping information]{lang="EN-US"}]{#struct_0_x6470_x2019_x705054910}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x1419197718}[的状态信息]{style="font-family:宋体"}

[[MLD snooping ]{lang="EN-US"}]{#struct_0_x6470_x2019_x826196886}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_2097354647}[的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6470_x2019_1773477361}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6470_x2019_x1653441657}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Drop-unknown ]{lang="EN-US"}]{#struct_0_x6470_x2019_x2068887234}

[[丢弃未知组播数据报文功能的使能状态（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x705120446}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6470_x2019_896594138}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6470_x2019_979886863}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Version]{lang="EN-US"}]{#struct_0_x6470_x2019_x1738157465}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x604058758}[的版本]{style="font-family:宋体"}

[[Host-aging-time]{lang="EN-US"}]{#struct_0_x6470_x2019_x704137406}

[[动态成员端口的老化时间]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x296792401}

[[Router-aging-time]{lang="EN-US"}]{#struct_0_x6470_x2019_x739033838}

[[动态路由器端口老化时间]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1976718924}

[[Max-response-time]{lang="EN-US"}]{#struct_0_x6470_x2019_1455919056}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1146334164}[普遍组查询的最大响应时间]{style="font-family:宋体"}

[[Last-listener-query-interval]{lang="EN-US"}]{#struct_0_x6470_x2019_x704202942}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1001257083}[特定组查询报文的发送间隔]{style="font-family:宋体"}

[[Report-aggregation]{lang="EN-US"}]{#struct_0_x6470_x2019_x463347760}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x651472602}[成员关系报告报文抑制功能的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6470_x2019_x463413296}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6470_x2019_x1413382372}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Dot1p-priority]{lang="EN-US"}]{#struct_0_x6470_x2019_x463478832}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_1785429101}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示没有配置]{style="font-family:宋体"}

[[Querier]{lang="EN-US"}]{#struct_0_x6470_x2019_x463020080}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x630448040}[查询器的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6470_x2019_x463085616}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6470_x2019_491743078}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Query-interval]{lang="EN-US"}]{#struct_0_x6470_x2019_x463151152}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x229141159}[普遍组查询报文的发送间隔]{style="font-family:宋体"}

[[General-query source IP]{lang="EN-US"}]{#struct_0_x6470_x2019_x463216688}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1052910532}[普遍组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Special-query source IP]{lang="EN-US"}]{#struct_0_x6470_x2019_x462757936}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_1327976871}[特定组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Report source IP]{lang="EN-US"}]{#struct_0_x6470_x2019_x462823472}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x463282225}[成员关系报告报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Done source IP]{lang="EN-US"}]{#struct_0_x6470_x2019_130419158}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x463347761}[离开组报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1691338347 .myid}
[]{#_Toc109289999}[]{#_Toc52102254}[]{#_Toc404790095}[]{#struct_0_x6470_x2019_x292587492}[]{#_Toc123030573}[]{#_Toc121110309}[]{#_Toc114641929}

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping group**

------------------------------------------------------------------------

[**[display mld-snooping group]{lang="EN-US"}**]{#struct_0_x6470_x2019_1089837738}[命令用来显示动态]{style="font-family:
宋体"}[MLD Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1063048252}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1087983881}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x831165957}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *ipv6-group-address* \| *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_x704661693}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1850972601}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *ipv6-group-address* \| *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_x2109900250}[模式：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x251877487}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *ipv6-group-address* \| *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1857764648}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x583814299}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_207689698}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_699327272}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_1527730606}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x885116034}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x704727229}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1437249709}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x2083992462}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x646503533}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x360473452}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x45803782}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x6470_x2019_1380155160}[：]{style="font-family:宋体"}[显示详细信息。如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_461749852}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x847735425}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1029855480}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_613659554}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_985584911}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x936406115}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x704792765}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_921438288}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内动态]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping group vlan 2 verbose]{lang="EN-US"}]{#struct_0_x6470_x2019_x1561249246}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 entries.]{lang="EN-US"}

[  (::,FF1E::101)]{lang="EN-US"}

[    Attribute: local port]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/2                             (00:03:23)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x45869318}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内动态]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping group vsi aaa verbose]{lang="EN-US"}]{#struct_0_x6470_x2019_x46328071}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 entries.]{lang="EN-US"}

[  (::,FF1E::101)]{lang="EN-US"}

[    Attribute: global port]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)         (00:03:35)]{lang="EN-US"}

[        VLAN pairs (1 in total):]{lang="EN-US"}

[          Out VLAN 5     In VLAN 2        (00:03:35)]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display mld-snooping group]{lang="EN-US"}]{#struct_0_x6470_x2019_x266642142}[命令显示信息描述表]{style="font-family:黑体"}

[]{#_Toc123030574}[]{#_Toc121110274}[]{#table_struct_0_x1732719703}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1533867328}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x352372430}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x704858301}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1651676861}

[[VLAN 2: Total 1 entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x162109146}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x917966720}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x46393607}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x46196999}[内的表项总数]{style="font-family:宋体"}

[[(::]{lang="EN-US"}]{#struct_0_x6470_x2019_304331830}[，]{style="font-family:宋体"}[FF1E::101)]{lang="EN-US"}

[[（]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1870913483}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[::]{lang="EN-US"}[表示所有]{style="font-family:宋体"}[IPv6]{lang="FR"}[组播源]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x6470_x2019_x936143972}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x936209508}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[global port]{lang="FR"}]{#struct_0_x6470_x2019_x1998581202}[：表示表项中存在全局口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[local port]{lang="FR"}]{#struct_0_x6470_x2019_x936012900}[：表示表项中存在本单板的端口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[slot]{lang="FR"}]{#struct_0_x6470_x2019_x936078436}[：表示表项中存在其它单板的端口]{style="font-family:宋体"}

[[FSM information]{lang="EN-US"}]{#struct_0_x6470_x2019_x1609464184}

[[表项状态机，包括：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x936406116}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_x6470_x2019_x936471652}[：表示所有成员属性均已删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dummy]{lang="FR"}]{#struct_0_x6470_x2019_x936275044}[：表示新创建的临时表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[no info]{lang="FR"}]{#struct_0_x6470_x2019_805214950}[：表示没有表项存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[normal]{lang="FR"}]{#struct_0_x6470_x2019_x936340580}[：表示主控板通知创建的正式表项]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1917212541}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x704923837}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x748585028}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_73380703}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x748585029}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_73446239}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x615285460}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1987653573}

[[(00:03:23)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1954872690}

[[成员端口的老化剩余时间。需要注意的是，本字段对于全局口（包括二层聚合接口、]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x6470_x2019_989325394}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等）将无条件显示，而对于非全局口：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x936471653}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x704989373}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_116067126}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_734709791}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x46524679}

[[AC]{lang="FR"}]{#struct_0_x6470_x2019_x45803783}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x45869319}

[[N-PW]{lang="FR"}]{#struct_0_x6470_x2019_x449612593}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_816851041}

[[U-PW]{lang="FR"}]{#struct_0_x6470_x2019_x449678129}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[VLAN pairs (1 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x449481521}

[[VLAN]{lang="FR"}]{#struct_0_x6470_x2019_x449547057}[对及总数]{style="font-family:宋体"}

[[Out VLAN 5, in VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x449874737}

[[外层]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x449940273}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[5]{lang="FR"}[，内层]{style="font-family:
  宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[2]{lang="FR"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1466703032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mld-snooping group]{lang="EN-US"}**]{#struct_0_x6470_x2019_59393958}

::: {#-1054324774 .myid}
[]{#_Toc404790096}[]{#struct_0_x6470_x2019_x1256669738}

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping router-port**

------------------------------------------------------------------------

[**[display mld-snooping router-port]{lang="EN-US"}**]{#struct_0_x6470_x2019_x238373111}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x705054909}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1419787543}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_237972212}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[router-port]{lang="EN-US"}**[ \[ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \[ **verbose** \] \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_561123743}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1213110020}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[router-port]{lang="EN-US"}**[ \[ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \[ **verbose** \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_1697110947}[模式：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x634759023}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[router-port]{lang="EN-US"}**[ \[ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \[ **verbose** \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1782574352}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1075874008}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1484172520}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x705120445}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_896790746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1641389759}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x414360210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_630575677}

[**[verbose]{lang="EN-US"}**]{#struct_0_x6470_x2019_x449153841}[：]{style="font-family:宋体"}[显示详细信息。如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_396095121}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x449612594}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1232125631}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x536359436}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1480194174}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x821030261}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_2073512386}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x936275046}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x704137405}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x296989009}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping router-port vlan 2]{lang="EN-US"}]{#struct_0_x6470_x2019_871370007}

[VLAN 2:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    GE1/0/1                             (00:01:30)]{lang="EN-US"}

[    GE1/0/2                             (00:00:23)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x449481522}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping router-port vsi aaa verbose]{lang="EN-US"}]{#struct_0_x6470_x2019_x449547058}

[VSI aaa:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (1 in total):]{lang="EN-US"}

[    AC (VSI index 0, link ID 1)         (00:03:35)]{lang="EN-US"}

[      VLAN pairs (1 in total):]{lang="EN-US"}

[        Out VLAN 5     In VLAN 2        (00:03:35)]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display mld-snooping router-port]{lang="EN-US"}]{#struct_0_x6470_x2019_1169170085}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1739076361}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_572216229}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_331025401}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x1560031540}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x704202941}[的编号]{style="font-family:宋体"}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x6470_x2019_x449874738}

[[VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x449940274}[的名称]{style="font-family:宋体"}

[[Router slots (0 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1001322619}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_2089336401}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1590067136}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有动态路由器端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x692073142}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1610336107}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有动态路由器端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1590067135}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有动态路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Router ports (2 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_291066756}

[[动态路由器端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1050897795}

[[(00:01:30)]{lang="EN-US"}]{#struct_0_x6470_x2019_x556338221}

[[动态路由器]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1238406941}[端口的老化剩余时间。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x6470_x2019_629350148}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号（才会显示]{style="font-family:宋体"}]{#struct_0_x6470_x2019_861422251}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1487391304}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x488150588}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x449088306}

[[AC]{lang="FR"}]{#struct_0_x6470_x2019_x449153842}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x449612591}

[[N-PW]{lang="FR"}]{#struct_0_x6470_x2019_x449678127}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x6470_x2019_x449481519}

[[U-PW]{lang="FR"}]{#struct_0_x6470_x2019_x449547055}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[VLAN pairs (1 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x449874735}

[[VLAN]{lang="FR"}]{#struct_0_x6470_x2019_x449940271}[及总数]{style="font-family:宋体"}

[[Out VLAN 5, in VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x449743663}

[[外层]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x449809199}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[5]{lang="FR"}[，内层]{style="font-family:
  宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[2]{lang="FR"}

[ ]{lang="EN-US"}

[]{#_Toc293908670}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_409814111}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mld-snooping router-port]{lang="EN-US"}**]{#struct_0_x6470_x2019_17157805}

::: {#-306939318 .myid}
[]{#_Toc404790097}[]{#struct_0_x6470_x2019_82834791}

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping static-group**

------------------------------------------------------------------------

[**[display mld-snooping static]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1607256003}[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[命令用来显示静态]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1437867024}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_861356715}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_1782158080}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static]{lang="EN-US"}**[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *ipv6-group-address* \| *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **verbose** \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_1269420658}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_271733571}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static]{lang="EN-US"}**[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *ipv6-group-address* \| *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_2104251858}[模式：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_965381055}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static]{lang="EN-US"}**[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *ipv6-group-address* \| *ipv6-source-address* \] \* \[ **vlan** *vlan-id* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x757513307}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1180789608}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861291179}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x175461582}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_1009225196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_56912682}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x587160682}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1966949470}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1467604373}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1633567707}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_1826290532}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x6470_x2019_861225643}[：]{style="font-family:宋体"}[显示详细信息。如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1003882530}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_2047228333}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1836490070}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1891771414}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_1798640788}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_630005506}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x861057807}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_278155421}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内静态]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping static-group vlan 2 verbose]{lang="EN-US"}]{#struct_0_x6470_x2019_553794944}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 entries.]{lang="EN-US"}

[  (::,FF1E::101)]{lang="EN-US"}

[    Attribute: local port]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/2]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display mld-snooping static-group]{lang="EN-US"}]{#struct_0_x6470_x2019_861160107}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1739765883}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1617712663}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x432384158}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x6470_x2019_447418315}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_913740857}

[[VLAN 2: Total 1 entries]{lang="EN-US"}]{#struct_0_x6470_x2019_x896477420}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_x489383230}[内的表项总数]{style="font-family:宋体"}

[[(::]{lang="EN-US"}]{#struct_0_x6470_x2019_861094571}[，]{style="font-family:宋体"}[FF1E::101)]{lang="EN-US"}

[[（]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1124171174}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[::]{lang="EN-US"}[表示所有]{style="font-family:宋体"}[IPv6]{lang="FR"}[组播源]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x6470_x2019_630071041}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_630005505}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[global port]{lang="FR"}]{#struct_0_x6470_x2019_629677825}[：表示表项中存在全局口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[local port]{lang="FR"}]{#struct_0_x6470_x2019_629612289}[：表示表项中存在本单板的端口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[slot]{lang="FR"}]{#struct_0_x6470_x2019_629808897}[：表示表项中存在其它单板的端口]{style="font-family:宋体"}

[[FSM information]{lang="EN-US"}]{#struct_0_x6470_x2019_629743361}

[[表项状态机，包括：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_629415681}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_x6470_x2019_629350145}[：表示所有成员属性均已删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dummy]{lang="FR"}]{#struct_0_x6470_x2019_629939968}[：表示新创建的临时表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[no info]{lang="FR"}]{#struct_0_x6470_x2019_629874432}[：表示没有表项存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[normal]{lang="FR"}]{#struct_0_x6470_x2019_630071040}[：表示主控板通知创建的正式表项]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_259631199}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1695930102}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1590067129}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x692400823}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1623008806}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1377445705}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_1867863941}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x533155687}

[ ]{lang="EN-US"}

::: {#-1549892221 .myid}
[]{#_Toc404790098}[]{#struct_0_x6470_x2019_861029035}

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping static-router-port**

------------------------------------------------------------------------

[**[display mld-snooping static-router-port]{lang="EN-US"}**]{#struct_0_x6470_x2019_x2026627342}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由器端口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x818305626}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1105211407}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x243099449}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static-router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_x664983079}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1712554122}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static-router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6470_x2019_x593614808}[模式：]{style="font-family:宋体"}

[**[display mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_364706002}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static-router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_58866513}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_860963499}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1563553869}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x650161880}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x184648350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x368992169}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_x1159197991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1650725009}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1853415899}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x877176507}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_861946539}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_270406129}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_165968913}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_1682541578}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6470_x2019_1864362854}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black;border:none windowtext 1.0pt;padding:0cm"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1514296586}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_748285588}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由器端口的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping static-router-port vlan 2]{lang="EN-US"}]{#struct_0_x6470_x2019_1228908019}

[VLAN 2:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    GE1/0/1]{lang="EN-US"}

[    GE1/0/2]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display mld-snooping static-router-port]{lang="EN-US"}]{#struct_0_x6470_x2019_786552722}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1738178583}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1568904734}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861881003}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x6470_x2019_1730748342}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_2142222733}[的编号]{style="font-family:宋体"}

[[Router slots (0 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x254063140}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x970681392}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x366248000}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有静态路由器端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x366248001}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1289126966}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有静态路由器端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1897953615}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有静态路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Router ports (2 in total)]{lang="EN-US"}]{#struct_0_x6470_x2019_x558199251}

[[静态路由器端口及总数]{style="font-family:宋体"}]{#struct_0_x6470_x2019_861422252}

[ ]{lang="EN-US"}

::: {#1125106362 .myid}
[]{#_Toc404790099}[]{#struct_0_x6470_x2019_x1487391305}

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **mld**-**snooping** **statistics**]{lang="EN-US"}]{#struct_0_x6470_x2019_x2054234529}[命令用来显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1196989901}

[**[display mld-snooping statistics]{lang="EN-US"}**]{#struct_0_x6470_x2019_x556508182}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1098279095}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_976233679}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x622514785}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1359728940}

[[network-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_861356716}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1782158081}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6470_x2019_1269355122}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x939681032}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_235564599}[显示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display mld-snooping statistics]{lang="EN-US"}]{#struct_0_x6470_x2019_861291180}

[Received MLD general queries:  0]{lang="EN-US"}

[Received MLDv1 specific queries:  0]{lang="EN-US"}

[Received MLDv1 reports:  0]{lang="EN-US"}

[Received MLD dones:  0]{lang="EN-US"}

[Sent     MLDv1 specific queries:  0]{lang="EN-US"}

[Received MLDv2 reports:  0]{lang="EN-US"}

[Received MLDv2 reports with right and wrong records:  0]{lang="EN-US"}

[Received MLDv2 specific queries:  0]{lang="EN-US"}

[Received MLDv2 specific sg queries:  0]{lang="EN-US"}

[Sent     MLDv2 specific queries:  0]{lang="EN-US"}

[Sent     MLDv2 specific sg queries:  0]{lang="EN-US"}

[Received error MLD messages:  0]{lang="EN-US"}

[]{#struct_0_x6470_x2019_633842489}[[表1-10 ]{lang="EN-US"}[display mld-snooping statistics]{lang="EN-US"}]{#_Toc288831907}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1743229671}[[字段]{style="font-family:黑体"}]{#struct_0_x6470_x2019_721364143}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x308447777}

[[general queries]{lang="EN-US"}]{#struct_0_x6470_x2019_1300385592}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_1418357517}[普遍组查询报文的数量]{style="font-family:宋体"}

[[specific queries]{lang="EN-US"}]{#struct_0_x6470_x2019_1888909796}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1119861225}[特定组查询报文的数量]{style="font-family:宋体"}

[[reports]{lang="EN-US"}]{#struct_0_x6470_x2019_861225644}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_1003882537}[成员关系报告报文的数量]{style="font-family:宋体"}

[[dones]{lang="EN-US"}]{#struct_0_x6470_x2019_2047293869}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x741031310}[离开组报文的数量]{style="font-family:宋体"}

[[reports with right and wrong records]{lang="EN-US"}]{#struct_0_x6470_x2019_x202210043}

[[包含错误和正确纪录的]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x422514500}[成员关系报告报文数量]{style="font-family:宋体"}

[[specific sg queries]{lang="EN-US"}]{#struct_0_x6470_x2019_861160108}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1617712664}[特定源组查询报文的数量]{style="font-family:宋体"}

[[error MLD messages]{lang="EN-US"}]{#struct_0_x6470_x2019_1940268837}

[[错误]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x2001409811}[报文的数量]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc293908672}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x2114311827}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mld-snooping statistics]{lang="EN-US"}**]{#struct_0_x6470_x2019_x894801878}

::: {#-203356666 .myid}
[]{#_Toc404790100}[]{#struct_0_x6470_x2019_1103063864}[]{#_Toc355703725}[]{#_Toc354920930}[]{#_Toc293908671}[]{#_Toc208651408}[]{#_Toc207106535}[]{#_Toc207099655}

**MLD Snooping \-- MLD Snooping配置命令 \-- dot1p-priority (MLD-Snooping view)**

------------------------------------------------------------------------

[**[dot1p-priority]{lang="EN-US"}**]{#struct_0_x6470_x2019_1102998328}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo dot1p-priority]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1728329831}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1148082285}

[**[dot1p-priority ]{lang="EN-US"}***[priority-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1102932792}

[**[undo dot1p-priority]{lang="EN-US"}**]{#struct_0_x6470_x2019_303905174}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1497077754}

[[没有配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_1102867256}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x512327498}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x1795930387}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1103326008}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1463160131}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1334465452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1103260472}

[*[priority-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1057039405}[：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。该数值越大，优先级越高。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1362143922}

[[对于基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1102801719}[的配置，本命令与]{style="font-family:宋体"}**[mld-snooping dot1p-priority]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[有效，后者的配置优先级较高；对于基于]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的配置，]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x97675396}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_236091195}[全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1102736183}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] dot1p-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1283191625}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1331638488}
:::

::::: {#1065654112 .myid}
[]{#_Toc404790101}[]{#struct_0_x6470_x2019_861094572}

**MLD Snooping \-- MLD Snooping配置命令 \-- drop-unknown (MLD-Snooping view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD%20Snooping命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6470_x2019_1124171175}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6470_x2019_259565663}
:::

[ ]{lang="EN-US"}

[**[drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_x2139736668}[命令用来全局使能丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文功能。]{style="font-family:宋体"}

[**[undo drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_x822781132}[命令用来全局关闭丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_725186073}

[**[drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1893331824}

[**[undo drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_780868539}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861029036}

[[丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x2026627343}[组播数据报文功能处于关闭状态，即对未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文进行广播。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_747778315}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_1583189844}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x910211303}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_273702240}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1816195535}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_485843670}

[[本命令与]{style="font-family:宋体"}**[mld-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_x205040400}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_860963500}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1974633559}[全局使能丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x2018137765}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] drop-unknown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x712417272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_x801945794}
:::::

::: {#1227056706 .myid}
[]{#_Toc404790102}[]{#struct_0_x6470_x2019_x1234290473}[]{#_Toc345425324}[]{#_Toc345425126}

**MLD Snooping \-- MLD Snooping配置命令 \-- enable (MLD-Snooping view)**

------------------------------------------------------------------------

[**[enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1003100591}[命令用来使能指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_1178151324}[命令用来关闭指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861946540}

[**[enable]{lang="EN-US"}**[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x6470_x2019_1357610010}

[**[undo enable]{lang="EN-US"}**[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x6470_x2019_1422337230}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1096597355}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_956484770}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x998268264}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x37781339}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1148942245}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1472439939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_861881004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1730748345}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_2142419341}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x449809205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使能]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x449088309}[内的]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[ Snooping]{lang="EN-US"}[之前，必须先全局使能]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[ Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x449153845}[的配置，本命令与]{lang="EN-US" style="font-family:宋体"}**[mld]{lang="EN-US"}[-snooping]{lang="EN-US"}[ enable]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下可以对指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_452612424}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1833192459}[全局使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x320864713}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] enable vlan 2 to 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1984966511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld]{lang="EN-US"}[-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1498062974}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld]{lang="EN-US"}[-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_861422249}**[ enable]{lang="EN-US"}**
:::

::: {#-510456293 .myid}
[]{#_Toc404790103}[]{#struct_0_x6470_x2019_468923840}

**MLD Snooping \-- MLD Snooping配置命令 \-- entry-limit (MLD-Snooping view)**

------------------------------------------------------------------------

[**[entry-limit]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1646543400}[命令用来配置]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表项（包括动态表项和静态表项）的全局最大数量。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[entry-limit]{lang="EN-US"}**]{#struct_0_x6470_x2019_1781459687}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x163232072}

[**[entry-limit ]{lang="EN-US"}***[limit]{lang="EN-US"}*]{#struct_0_x6470_x2019_610208209}

[**[undo entry-limit]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1670701768}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_776968593}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_119373865}[转发表项的全局最大数量为]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861356713}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_1782158086}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1269027442}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1812104205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x65087630}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1754450070}

[*[limit]{lang="EN-US"}*]{#struct_0_x6470_x2019_1837101884}[：表示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表项的全局最大数量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1359716441}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_2062248210}[配置]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表项的全局最大数量为]{style="font-family:宋体"}[512]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_861291177}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] entry-limit 512]{lang="EN-US"}
:::

::: {#-535068174 .myid}
[]{#_Toc404790104}[]{#struct_0_x6470_x2019_x175461568}[]{#_Toc293908674}

**MLD Snooping \-- MLD Snooping配置命令 \-- fast-leave (MLD-Snooping view)**

------------------------------------------------------------------------

[**[fast-leave]{lang="EN-US"}**]{#struct_0_x6470_x2019_1008569834}[命令用来全局使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[端口快速离开功能。]{style="font-family:宋体"}

[**[undo fast-leave]{lang="EN-US"}**]{#struct_0_x6470_x2019_1162230969}[命令用来全局关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[端口快速离开功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x527739888}

[**[fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_582294261}

[**[undo fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_710413068}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_161679949}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_861225641}[端口快速离开功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1003882532}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_2047097261}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x683872172}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x858039242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x662363682}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1969323723}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_x2041073214}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_770486059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_861160105}[端口快速离开是指当端口收到主机发来的离开指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6470_x2019_x1617712661}**[mld]{lang="EN-US"}[-snooping fast-leave]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1595183572}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x806038206}[全局使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[端口快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1494062422}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] fast-leave vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1125814407}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping fast-leave]{lang="EN-US"}**]{#struct_0_x6470_x2019_x435525625}
:::

::: {#-1987457272 .myid}
[]{#_Toc404790105}[]{#struct_0_x6470_x2019_1893112683}[]{#_Toc293908675}

**MLD Snooping \-- MLD Snooping配置命令 \-- group-policy (MLD-Snooping view)**

------------------------------------------------------------------------

[**[group-policy]{lang="DA"}**]{#struct_0_x6470_x2019_x208900272}[命令用来全局配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[以限定主机所能加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[**[undo group-policy]{lang="DA"}**]{#struct_0_x6470_x2019_861094569}[命令用来删除全局]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1214480994}

[**[group-policy]{lang="EN-US"}**[ *acl6-number* \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x173335876}

[**[undo group-policy]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x1180999690}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x664140571}

[[没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_1826824381}[组播组过滤器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即主机可以加入任意合法的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_862019700}

[[MLD-Snooping]{lang="DA"}]{#struct_0_x6470_x2019_291821804}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1492148938}

[[network-admin]{lang="DA"}]{#struct_0_x6470_x2019_861029033}

[[mdc-admin]{lang="DA"}]{#struct_0_x6470_x2019_x2026627348}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_700724148}

[*[acl6-number]{lang="DA"}*]{#struct_0_x6470_x2019_x1300660539}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="DA"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="DA"}[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="DA"}[～]{style="font-family:宋体"}[3999]{lang="DA"}[。主机只能加入该]{style="font-family:
宋体"}[ACL]{lang="DA"}[规则所允许的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[**[vlan ]{lang="DA"}**]{#struct_0_x6470_x2019_x1958363528}*[vlan-list]{lang="DA"}*[：]{style="font-family:
宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="DA"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="DA"}*[为]{style="font-family:宋体"}[VLAN]{lang="DA"}[列表]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[表示一或多个]{style="font-family:
宋体"}[VLAN]{lang="DA"}[，]{style="font-family:宋体"}[表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="DA"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="DA"}[，]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[vlan-id]{lang="DA"}*[为]{style="font-family:宋体"}[VLAN]{lang="DA"}[的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:
宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[4094]{lang="DA"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x92292002}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x266862149}[IPv6]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1844599761}[IPv6]{lang="DA"}[高级]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[MLDv1]{lang="DA"}[报文和未携带]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[MLDv2]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[视其]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址为]{lang="EN-US" style="font-family:宋体"}[0::0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以为端口在不同的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1529214214}[VLAN]{lang="EN-US"}[内配置不同的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则，但在相同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内所配置的新规则会取代旧规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对]{style="font-family:宋体"}]{#struct_0_x6470_x2019_54900270}[IPv6]{lang="EN-US"}[动态组播组有效，对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态组播组无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6470_x2019_860963497}**[mld]{lang="EN-US"}[-snooping ]{lang="EN-US"}[group-policy]{lang="DA"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1563553867}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x199823186}[全局配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器，以限定]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的主机只能加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x937768736}

[\[Sysname\] acl ipv6 basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule permit source ff03::101 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] group-policy 2000 vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x784169071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping ]{lang="EN-US"}**]{#struct_0_x6470_x2019_x35187674}**[group-policy]{lang="DA"}**
:::

::: {#1634865047 .myid}
[]{#_Toc404790106}[]{#struct_0_x6470_x2019_x1290061977}[]{#_Toc293908676}

**MLD Snooping \-- MLD Snooping配置命令 \-- host-aging-time (MLD-Snooping view)**

------------------------------------------------------------------------

[**[host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1183367531}[命令用来全局配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态成员端口的老化时间。]{style="font-family:宋体"}

[**[undo host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_861946537}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_165968919}

[**[host-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x6470_x2019_1514296596}

[**[undo host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_748285589}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1228908018}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_786618258}[动态成员端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x102030491}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x1254231947}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1079585481}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_861881001}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1730748340}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2142091661}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_1270721526}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态成员端口的老化时间，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1381646323}

[[本命令与]{style="font-family:宋体"}**[mld-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1063914683}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1346626493}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_907577337}[全局配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态成员端口的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_861422250}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] host-aging-time 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1487391303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1247665475}
:::

::: {#-365991733 .myid}
[]{#_Toc404790107}[]{#struct_0_x6470_x2019_x1764665749}[]{#_Toc293908705}

**MLD Snooping \-- MLD Snooping配置命令 \-- last-listener-query-interval (MLD-Snooping view)**

------------------------------------------------------------------------

[**[last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_1370645039}[命令用来全局配置]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[特定组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_x836070765}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_960946605}

[**[last-listener-query-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1910560192}

[**[undo last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_861356714}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1782158079}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_1268830847}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1397838536}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_1077195470}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_311595708}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_288256031}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1188195091}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x358760877}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_861291178}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x175461583}

[[本命令与]{style="font-family:宋体"}**[mld-snooping last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_1009290732}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1100209111}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x924378396}[全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1989564968}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] last-listener-query-interval 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_536496050}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping]{lang="EN-US"}**[ **last-listener-query-interval**]{lang="EN-US"}]{#struct_0_x6470_x2019_1895121345}
:::

::: {#172064074 .myid}
[]{#_Toc404790108}[]{#struct_0_x6470_x2019_861225642}[]{#_Toc293908706}

**MLD Snooping \-- MLD Snooping配置命令 \-- max-response-time (MLD-Snooping view)**

------------------------------------------------------------------------

[**[max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_1003882531}[命令用来全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间。]{style="font-family:宋体"}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_2047162797}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_110579141}

[**[max-response-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x6470_x2019_x259680219}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1692929334}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1564542874}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1709753253}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_472233107}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_861160106}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1617712662}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1133699783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1260602654}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1519108933}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_979849325}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x185853956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免误删]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1102801717}[IPv6]{lang="EN-US"}[组播组成员，请确保]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间小于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6470_x2019_1116471350}**[mld]{lang="EN-US"}[-snooping max-response-time]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}[下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x630805710}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_861094570}[全局配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1124171173}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] max-response-time 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_259696735}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_490585978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_1102736181}
:::

::: {#-1316396052 .myid}
[]{#_Toc404790109}[]{#struct_0_x6470_x2019_x1349376278}[]{#_Toc123030578}[]{#_Toc121110275}[]{#_Toc301424948}[]{#_Toc301427648}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping**

------------------------------------------------------------------------

[**[mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1468241426}[命令用来全局使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1418439284}[命令用来全局关闭]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_486387126}

[**[mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_861029034}

[**[undo mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_x2026627341}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1910577729}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_668956955}[处于全局关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1249826585}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1584325774}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_256411413}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x988145324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_2109901676}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_860963498}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1563553868}[全局使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_915922061}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1788363482}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x740752655}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_223815741}
:::

::: {#1552962299 .myid}
[]{#_Toc354920938}[]{#_Toc293908680}[]{#_Toc404790110}[]{#struct_0_x6470_x2019_1102605109}[]{#_Toc355703735}[]{#_Toc354920948}[]{#_Toc293908691}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping done source-ip**

------------------------------------------------------------------------

[**[mld-snooping done source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_1103063861}[命令用来配置]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[离开组报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo mld-snooping done source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_329035605}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_28195069}

[**[mld-snooping done source-ip]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x6470_x2019_1102998325}

[**[undo mld-snooping done source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1728657511}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1102932789}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_303446421}[离开组报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址，则采用]{style="font-family:宋体"}[FE80::02FF:FFFF:FE00:0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1712309584}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1102867253}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x512524106}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_905028841}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1103326005}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1463487811}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x256801916}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[离开组报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1103260469}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1056449582}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1719096530}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1102801716}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[离开组报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80:0:0:1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x97085572}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping done source-ip fe80:0:0:1::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1102736180}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_1116143670}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1282995017}
:::

::: {#-131535815 .myid}
[]{#_Toc404790111}[]{#struct_0_x6470_x2019_1102670644}[]{#_Toc355703736}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping dot1p-priority**

------------------------------------------------------------------------

[**[mld-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x6470_x2019_x880729180}[命令用来在]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo mld-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1378741032}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1102605108}

[**[mld-snooping dot1p-priority ]{lang="EN-US"}***[priority-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1684772177}

[**[undo mld-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x6470_x2019_1026028482}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1103063860}

[[没有配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_328970069}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x628986100}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1102998324}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1728591975}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1334448281}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1102932788}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_303511957}

[*[priority-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1102867252}[：]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。该数值越大，优先级越高。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x512589642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_2047279806}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1103326004}[的配置，本命令与]{lang="EN-US" style="font-family:宋体"}**[dot1p-priority]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1463422275}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_149699707}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1103260468}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping dot1p-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1056384046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1p-priority]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_1102801715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_1116471349}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x96888964}
:::

::::: {#1696016439 .myid}
[]{#_Toc404790112}[]{#struct_0_x6470_x2019_1363847783}[]{#_Toc293908681}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping drop-unknown**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD%20Snooping命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6470_x2019_x718306551}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6470_x2019_861946538}
:::

[ ]{lang="EN-US"}

[**[mld-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_165968914}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内使能丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文功能。]{style="font-family:宋体"}

[**[undo mld-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_1514296583}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内关闭丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_748482196}

[**[mld-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_1494602641}

[**[undo mld-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1512673487}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_482092914}

[[丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_795293443}[组播数据报文功能处于关闭状态，即对未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文进行广播。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861881002}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1730748343}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2142288269}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x330245147}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1711381222}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1424584534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_108955750}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[drop-unknown]{lang="EN-US"}**]{#struct_0_x6470_x2019_677958816}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1221758498}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_861422247}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并使能丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_468923834}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vlan 2]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping drop-unknown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1116930101}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并使能丢弃未知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1116471344}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping drop-unknown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1456782804}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[drop-unknown]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_x2004272262}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_1116405808}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x747518340}
:::::

::: {#1220870234 .myid}
[]{#_Toc404790113}[]{#struct_0_x6470_x2019_1763096074}[]{#_Toc123030580}[]{#_Toc121110295}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping enable**

------------------------------------------------------------------------

[**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1773990028}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_861356711}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内关闭]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1782158084}

[**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_861291175}

[**[undo mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x175461570}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1009094121}

[[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_1607661144}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1017157694}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x377652838}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x454693900}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1637192954}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_861225639}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_194578476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_1293316367}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[之前，必须先全局使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1116274736}[VLAN]{lang="EN-US"}[的配置，本命令与]{style="font-family:宋体"}**[enable]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下可以对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1633205756}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1446857839}[全局使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_303490187}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1116995632}[全局使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1116930096}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1045337822}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x2085880588}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_861160103}
:::

::: {#-2137664132 .myid}
[]{#_Toc404790114}[]{#struct_0_x6470_x2019_x1617712659}[]{#_Toc293908683}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping fast-leave**

------------------------------------------------------------------------

[**[mld-snooping fast-leave]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1951348396}[命令用来在端口上使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[端口快速离开功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mld-snooping fast-leave**]{lang="EN-US"}]{#struct_0_x6470_x2019_1636503471}[命令用来在端口上关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[端口快速离开功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_49842447}

[**[mld-snooping fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x1392887424}

[**[undo mld-snooping fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x361659998}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1840443728}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_2136002233}[端口快速离开功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861094567}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_x1214480980}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x2142769880}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_908768890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1884819456}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x2120400168}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_361384737}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1395486672}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x2017509028}[端口快速离开是指当端口收到主机发来的离开指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[fast-leave]{lang="EN-US"}**]{#struct_0_x6470_x2019_861029031}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:
宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x2026627346}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1507293202}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[端口快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_861946535}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping fast-leave vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_165968917}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fast-leave]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_1514296582}
:::

::: {#-909028905 .myid}
[]{#_Toc404790115}[]{#struct_0_x6470_x2019_1102867251}[]{#_Toc355703740}[]{#_Toc354920942}[]{#_Toc293908684}[]{#_Toc123030581}[]{#_Toc121110287}[]{#_Toc109290008}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping general-query source-ip**

------------------------------------------------------------------------

[**[mld-snooping general-query source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_1103326003}[命令用来配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo mld-snooping general-query source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_1463881027}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2078721889}

[**[mld-snooping general-query source-ip]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x6470_x2019_1103260467}

[**[undo mld-snooping general-query source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_1057367086}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x154209041}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1626081635}[VLAN]{lang="EN-US"}[内，]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址，则采用]{style="font-family:宋体"}[FE80::02FF:FFFF:FE00:0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1116930095}[VSI]{lang="EN-US"}[内，]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80::02FF:FFFF:FE00:0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1722488590}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x41119023}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626147171}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1185253817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1626212707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1696761112}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x984489041}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626278243}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_763502999}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x576967718}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1625819491}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80:0:0:1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x251433488}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping general-query source-ip fe80:0:0:1::1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_712924677}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80:0:0:1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_712859141}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping general-query source-ip fe80:0:0:1::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625885027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_713055749}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_1927872345}
:::

::: {#-2140500275 .myid}
[]{#_Toc404790116}[]{#struct_0_x6470_x2019_748547732}[]{#_Toc293908685}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping group-limit**

------------------------------------------------------------------------

[**[mld-snooping group-limit]{lang="DA"}**]{#struct_0_x6470_x2019_686602967}[命令用来[]{#_Toc127795919}[配置端口加入的]{#_Ref127672022}]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组最大数量]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ]{lang="DA"}**]{#struct_0_x6470_x2019_x870119927}**[mld-snooping group-limit]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1862539129}

[**[mld-snooping group-limit]{lang="EN-US"}**[ *limit* \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_881608965}

[**[undo mld-snooping group-limit]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_861880999}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1071034391}

[[端口加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x306987820}[组播组最大数量为]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x2044571754}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_491892661}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1826105330}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1369039494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x176280569}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x703266345}

[*[limit]{lang="EN-US"}*]{#struct_0_x6470_x2019_861422248}[：表示端口加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组最大数量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_468923841}[：表示]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1646543401}

[[本命令只对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x947423668}[动态组播组有效，对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态组播组无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1186831545}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x157226231}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组最大数量为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_2000041538}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping group-limit 10 vlan 2]{lang="EN-US"}
:::

::: {#-351180443 .myid}
[]{#_Toc404790117}[]{#struct_0_x6470_x2019_x545682425}[]{#_Toc293908686}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping group-policy**

------------------------------------------------------------------------

[**[mld-snooping group-policy]{lang="DA"}**]{#struct_0_x6470_x2019_861356712}[命令用来[]{#_Toc127848451}[]{#_Toc125123262}[]{#_Toc122232024}[在端口上配置]{#_Ref114841739}]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[以限定主机所能加入的]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播组。]{style="font-family:宋体"}

[**[undo ]{lang="DA"}**]{#struct_0_x6470_x2019_1782158085}**[mld-snooping group-policy]{lang="DA"}**[命令用来删除端口上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1269092978}

[**[mld-snooping group-policy]{lang="EN-US"}**[ *acl6-number* \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_984956167}

[**[undo mld-snooping group-policy]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x387459599}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1780345676}

[[没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x174757864}[组播组过滤器，即主机可以加入任意合法的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x547796569}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_1958041040}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861291176}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x175461569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1008635370}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x729519448}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1260709201}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。主机只能加入该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则所允许的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_1721996701}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x259700350}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x6470_x2019_280228521}[IPv6]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x884218065}[IPv6]{lang="DA"}[高级]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[MLD]{lang="DA"}[报文中的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[MLDv1]{lang="DA"}[报文和未携带]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[MLDv2]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[视其]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[组播源地址为]{lang="EN-US" style="font-family:宋体"}[0::0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以为端口在不同的]{style="font-family:宋体"}]{#struct_0_x6470_x2019_861225640}[VLAN]{lang="EN-US"}[内配置不同的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则，但在相同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内所配置的新规则会取代旧规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1003882533}[IPv6]{lang="EN-US"}[动态组播组有效，对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态组播组无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6470_x2019_2047031725}**[group-policy]{lang="DA"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:
宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x285561870}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_85834089}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组过滤器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[以限定端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的主机只能加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1581136990}

[\[Sysname\] acl ipv6 basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule permit source ff03::101 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping group-policy 2000 vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1318507231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[group-policy]{lang="DA"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_861160104}
:::

::: {#-1614015347 .myid}
[]{#_Toc404790118}[]{#struct_0_x6470_x2019_x1617712660}[]{#_Toc293908687}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping host-aging-time**

------------------------------------------------------------------------

[**[mld-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x29099631}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态成员端口的老化时间。]{style="font-family:宋体"}

[**[undo mld-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_1975848897}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x375681234}

[**[mld-snooping host-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1485009373}

[**[undo mld-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1308217222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1475406841}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x1390350303}[动态成员端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_861094568}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x1214480995}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1392748065}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1414745222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_653952331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1354863764}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_103893026}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态成员端口的老化时间，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1489966070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_780885892}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[host-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_861029032}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x2026627347}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1221590153}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态成员端口的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1125128757}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vlan 2]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping host-aging-time 300]{lang="NL"}

[[\# ]{lang="NL"}]{#struct_0_x6470_x2019_712859143}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[，]{style="font-family:宋体"}[并配置]{style="font-family:宋体"}[IPv6]{lang="NL"}[动态成员端口的老化时间为]{style="font-family:宋体"}[300]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x6470_x2019_713055751}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping host-aging-time 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1434705279}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_712990215}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[host-aging-time]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_x688282994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_1368349450}
:::

::: {#-1977666748 .myid}
[]{#_Toc404790119}[]{#struct_0_x6470_x2019_x1626278244}[]{#_Toc355703744}[]{#_Toc354920946}[]{#_Toc293908688}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping host-join**

------------------------------------------------------------------------

[**[mld-snooping]{lang="DA"}[ ]{lang="DA"}[host-join]{lang="EN-US"}**]{#struct_0_x6470_x2019_1523017886}[命令用来[]{#_Toc127848457}[]{#_Toc125123268}[配置模拟主机加入]{#_Ref125123127}]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组。模拟主机加入就是将二层设备的端口配置为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的成员。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x6470_x2019_x240992452}**[mld-snooping]{lang="DA"}[ ]{lang="DA"}[host-join]{lang="EN-US"}**[命令用来删除模拟主机加入的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625819492}

[**[mld-snooping]{lang="DA"}[ ]{lang="DA"}[host-join ]{lang="EN-US"}***[ipv6-group-address]{lang="EN-US"}*[ \[ **source-ip** *ipv6-source-address* \] **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1817517429}

[**[undo ]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1625885028}**[mld-snooping]{lang="DA"}[ ]{lang="DA"}[host-join]{lang="EN-US"}**[ { *ipv6-group-address* \[ **source-ip** *ipv6-source-address* \] **vlan** *vlan-id* \| **all** }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x444780650}

[[没有配置模拟主机加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x1625950564}[组播组或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_706893902}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_x1918629132}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626016100}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_661911985}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1671436160}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625557348}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1120589132}[：表示模拟主机要加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的地址，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。]{style="font-family:
宋体"}

[**[source-ip ]{lang="EN-US"}***[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1625622884}[：表示模拟主机要加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的地址。如果指定了本参数，表示加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组；如果未指定本参数，则表示加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。配置有本参数的模拟主机，只在]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[版本]{style="font-family:宋体"}[2]{lang="EN-US"}[下生效。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x900134872}[：表示]{style="font-family:宋体"}[对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6470_x2019_712990214}[：表示对所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_542688070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[与静态成员端口不同，配置了模拟主机加入的端口将作为动态成员端口参与动态成员端口的老化过程。]{style="font-family:宋体"}]{#struct_0_x6470_x2019_713711110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[模拟主机]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6470_x2019_x1626081637}[所]{style="font-family:宋体"}[采用的]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[版本与]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[版本一致。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626147173}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1946914065}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置模拟主机加入]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组（]{style="font-family:宋体"}[2002::22]{lang="EN-US"}[，]{style="font-family:宋体"}[FF3E::101]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1626212709}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping version 2]{lang="EN-US"}

[\[Sysname-vlan2\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping host-join ]{lang="EN-US"}[ff3e::101 source-ip 2002::22 vlan 2]{lang="NL"}
:::

::: {#147556214 .myid}
[]{#_Toc404790120}[]{#struct_0_x6470_x2019_860963496}[]{#_Toc293908696}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping last-listener-query-interval**

------------------------------------------------------------------------

[**[mld-snooping last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1563553866}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo mld-snooping last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_1366260755}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1746250735}

[**[mld-snooping last-listener-query-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_x315307203}

[**[undo mld-snooping last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_542000855}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_813811631}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1838922356}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_27457280}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_861946536}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_165968920}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x59681525}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x700414858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x393034798}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_76150692}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[，单位为秒。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x327277345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x749695977}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[last-listener-query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_861881000}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1730748341}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_2142157197}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_511832052}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vlan 2]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping last-listener-query-interval 3]{lang="NL"}

[[\# ]{lang="NL"}]{#struct_0_x6470_x2019_712859136}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[，]{style="font-family:宋体"}[并配置]{style="font-family:宋体"}[MLD]{lang="NL"}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[3]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_713055744}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] mld-snooping last-]{lang="EN-US"}[listener]{lang="NL"}[-query-interval 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x769657786}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_712990208}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[last-listener-query-interval]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_x656977462}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x577584466}
:::

::: {#2116876278 .myid}
[]{#_Toc404790121}[]{#struct_0_x6470_x2019_x1754409775}[]{#_Toc293908692}[]{#_Toc301424957}[]{#_Toc301427657}[]{#_Toc301424958}[]{#_Toc301427658}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping max-response-time**

------------------------------------------------------------------------

[**[mld-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1867461104}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间。]{style="font-family:宋体"}

[**[undo mld-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_1933893884}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1262188362}

[**[mld-snooping max-response-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x6470_x2019_x854981523}

[**[undo mld-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_1616412241}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_351214438}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_1288163063}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_534053562}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_2078987620}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_908160578}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867526640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_921797121}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x913395844}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_182923281}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_251272535}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x1445046694}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_924830090}[上的配置只对当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[有效，但配置优先级高于全局配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免误删]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1626016101}[IPv6]{lang="EN-US"}[组播组成员，请确保]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间小于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x2015696535}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}[下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x281517567}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x858414434}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867592176}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vlan 2]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping max-response-time 5]{lang="NL"}

[[\# ]{lang="NL"}]{#struct_0_x6470_x2019_x2015762071}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[，]{style="font-family:宋体"}[并配置]{style="font-family:宋体"}[MLD]{lang="NL"}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[5]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015565463}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping max-response-time 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_119961531}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015630999}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-response-time]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1371490757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_600319345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1625557349}
:::

::: {#-631757700 .myid}
[]{#_Toc404790122}[]{#struct_0_x6470_x2019_x1476161172}[]{#_Toc293908693}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping overflow-replace**

------------------------------------------------------------------------

[**[mld-snooping]{lang="DA"}[ overflow-replace]{lang="EN-US"}**]{#struct_0_x6470_x2019_x420156881}[命令用来在端口上使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组替换功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x6470_x2019_496244631}**[mld-snooping]{lang="DA"}[ overflow-replace]{lang="EN-US"}**[命令用来在端口上关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组替换功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867657712}

[**[mld-snooping overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x1331816823}

[**[undo mld-snooping overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x1863354803}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_638165363}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x667622357}[组播组替换功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1787622720}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_798221160}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_614781509}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_665438593}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_330547172}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867723248}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_971562285}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1259521711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对]{style="font-family:宋体"}]{#struct_0_x6470_x2019_487565013}[IPv6]{lang="EN-US"}[动态组播组有效，对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态组播组无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[overflow-replace]{lang="EN-US"}**]{#struct_0_x6470_x2019_x615440179}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:
宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x680734045}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x386197636}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组替换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1113611721}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping overflow-replace vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_194334974}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[overflow-replace]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867788784}
:::

::: {#195404045 .myid}
[]{#_Toc404790123}[]{#struct_0_x6470_x2019_x1626147174}[]{#_Toc355703748}[]{#_Toc354920951}[]{#_Toc293908695}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping querier**

------------------------------------------------------------------------

[**[mld-snooping querier]{lang="EN-US"}**]{#struct_0_x6470_x2019_x781969290}[命令用来使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[mld-snooping querier]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1626212710}[命令用来关闭]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_130742707}

[**[mld-snooping querier]{lang="EN-US"}**]{#struct_0_x6470_x2019_278626612}

[**[undo mld-snooping querier]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1626278246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_360218472}

[[MLD Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x1625819494}[查询器处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1010948375}

[[VLAN]{lang="SV"}]{#struct_0_x6470_x2019_x1625885030}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x800945474}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x61982519}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1625950566}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1869693316}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x1626016102}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1824711399}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内配置了本命令，只有当该子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[被从]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中删除后，]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[查询器才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_600418323}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1625557350}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1625622886}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping querier]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015827604}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015893140}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping querier]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_262664542}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015172244}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_720816593}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[subvlan]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x1626081639}[IPv6 ]{lang="EN-US"}[multicast-VLAN view)]{lang="EN-US"}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#-497017061 .myid}
[]{#_Toc404790124}[]{#struct_0_x6470_x2019_603110238}[]{#_Toc355703749}[]{#_Toc354920952}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping query-interval**

------------------------------------------------------------------------

[**[mld-snooping query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1626147175}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo mld-snooping query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_784114651}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626212711}

[**[mld-snooping query-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1435341234}

[**[undo mld-snooping query-interval]{lang="EN-US"}**]{#struct_0_x6470_x2019_1180354950}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626278247}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x1205865469}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625819495}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1717934980}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625885031}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_765138467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_2116237506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625950567}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_303609375}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626016103}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_258627458}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免误删]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1625557351}[IPv6]{lang="EN-US"}[组播组成员，请确保]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔大于]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询的最大响应时间，否则配置虽能生效但系统会给出提示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1251998327}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x784086848}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1625622887}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping query-interval 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015827605}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015893141}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping query-interval 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1828748483}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015237781}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1626081640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1318876383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1626147176}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping querier]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1944768704}
:::

::: {#451338105 .myid}
[]{#_Toc404790125}[]{#struct_0_x6470_x2019_x1626212712}[]{#_Toc355703750}[]{#_Toc354920953}[]{#_Toc293908697}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping report source-ip**

------------------------------------------------------------------------

[**[mld-snooping report source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_1293542121}[命令用来配置]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[成员关系报告报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo mld-snooping report source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_711618258}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1626278248}

[**[mld-snooping report source-ip]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x6470_x2019_x446350582}

[**[undo mld-snooping report source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1625819496}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_151851039}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_x679279480}[成员关系报告报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址，则采用]{style="font-family:宋体"}[FE80::02FF:FFFF:FE00:0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625885032}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x1963744888}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625950568}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1262474566}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1626016104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1663686843}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_826563824}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625557352}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x314085614}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1625622888}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1069233596}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80:0:0:1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x59997694}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping report source-ip fe80:0:0:1::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1069092795}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015958682}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x60063230}
:::

::: {#1681340035 .myid}
[]{#_Toc404790126}[]{#struct_0_x6470_x2019_1322745780}[]{#_Toc293908698}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping router-aging-time**

------------------------------------------------------------------------

[**[mld-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_1455740326}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的老化时间。]{style="font-family:宋体"}

[**[undo mld-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x719575886}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x880332714}

[**[mld-snooping router-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1759618220}

[**[undo mld-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_607610643}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_669831872}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867854320}[动态路由器端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_219480003}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x659600601}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1568666314}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_676204332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_543265813}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1133925966}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1256084054}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1436946806}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867919856}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_187414426}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1414658218}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1330679896}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1661674863}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vlan 2]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping router-aging-time 100]{lang="NL"}

[[\# ]{lang="NL"}]{#struct_0_x6470_x2019_x2015893147}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[，]{style="font-family:宋体"}[并配置]{style="font-family:宋体"}[IPv6]{lang="NL"}[动态路由器端口的老化时间为]{style="font-family:宋体"}[100]{lang="NL"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x6470_x2019_x2015172251}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping router-aging-time 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1208527921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x2015237787}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_x112754410}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[router-aging-time]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_x1866936816}
:::

::: {#368366568 .myid}
[]{#_Toc404790127}[]{#struct_0_x6470_x2019_x59735550}[]{#_Toc355703752}[]{#_Toc354920955}[]{#_Toc293908699}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping router-port-deny**

------------------------------------------------------------------------

[**[mld-snooping router-port-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_901546932}[命令用来禁止端口成为动态路由器端口。]{style="font-family:
宋体"}

[**[undo mld-snooping router-port-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_x59801086}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1447961918}

[**[mld-snooping router-port-deny]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_2115155787}

[**[undo mld-snooping router-port-deny]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x59866622}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_714215322}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_x59932158}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x828133056}

[[允许端口成为动态路由器端口。]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x59473406}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1382676661}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1592565664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x59538942}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1796148334}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_x59997695}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="DA"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果指定了本参数，只有当该端口属于指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，本配置才生效；如果未指定本参数，则本配置将对该端口所属的所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x176813970}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x258050149}[禁止端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内成为动态路由器端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x60128767}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping router-port-deny vlan 2]{lang="EN-US"}
:::

::::: {#1878314643 .myid}
[]{#_Toc293908702}[]{#_Toc404790128}[]{#struct_0_x6470_x2019_1054505519}[]{#_Toc330456977}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping source-deny**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD%20Snooping命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6470_x2019_x1222320792}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6470_x2019_16885196}
:::

[ ]{lang="DA"}

[**[mld-snooping source-deny]{lang="DA"}**]{#struct_0_x6470_x2019_x74500235}[命令用来使能当前端口的]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[**[undo ]{lang="DA"}**]{#struct_0_x6470_x2019_744171312}**[mld-snooping source-deny]{lang="DA"}**[命令用来关闭当前端口的]{style="font-family:宋体"}[IPv6]{lang="DA"}[组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1385122578}

[**[mld-snooping]{lang="DA"}[ ]{lang="DA"}[source-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_1893736680}

[**[undo mld-snooping source-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_2112176506}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867002352}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_27830470}[组播数据报文源端口过滤功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x2059746011}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_70625306}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1909505210}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1543559623}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1652045747}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1239211533}

[[本命令与]{style="font-family:宋体"}**[source-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_979542207}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867461103}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x794989471}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_907218195}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping source-deny]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1760698790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source-deny]{lang="EN-US"}**[ (MLD-Snooping view)]{lang="EN-US"}]{#struct_0_x6470_x2019_1880696305}
:::::

::: {#2008273917 .myid}
[]{#_Toc404790129}[]{#struct_0_x6470_x2019_x59801087}[]{#_Toc355703754}[]{#_Toc354920957}[]{#_Toc293908701}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping special-query source-ip**

------------------------------------------------------------------------

[**[mld-snooping special-query source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_1447961919}[命令用来配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo mld-snooping special-query source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_x59866623}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_714215323}

[**[mld-snooping special-query source-ip]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x6470_x2019_882357657}

[**[undo mld-snooping special-query source-ip]{lang="EN-US"}**]{#struct_0_x6470_x2019_x59932159}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x828133057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x59473407}[VLAN]{lang="EN-US"}[内，如果收到过]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文，则以其源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址；否则，采用当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址，则采用]{style="font-family:宋体"}[FE80::02FF:FFFF:FE00:0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x6470_x2019_1875986237}[VSI]{lang="EN-US"}[内，如果收到过]{style="font-family:宋体"}[MLD]{lang="EN-US"}[普遍组查询报文，则以其源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址；否则，采用]{style="font-family:宋体"}[FE80::02FF:FFFF:FE00:0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1382676660}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x59538943}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1796148333}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x59997696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1069092797}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x784581383}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x60063232}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x176813973}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x60128768}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x995733880}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x60194304}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80:0:0:1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1381924135}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping special-query source-ip fe80:0:0:1::1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1875789629}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[MLD]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80:0:0:1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1876510525}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping special-query source-ip fe80:0:0:1::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x59735552}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_1876444989}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_901546930}
:::

::: {#-1898263987 .myid}
[]{#_Toc404790130}[]{#struct_0_x6470_x2019_1351835750}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping static-group**

------------------------------------------------------------------------

[**[mld-snooping]{lang="DA"}[ static-group]{lang="EN-US"}**]{#struct_0_x6470_x2019_1429134597}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态成员端口，即配置端口静态加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1867526639}**[mld-snooping]{lang="DA"}[ static-group]{lang="EN-US"}**[命令用来删除静态成员端口的配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1000189500}

[**[mld-snooping]{lang="DA"}**]{#struct_0_x6470_x2019_x579412606}[ **static-group** *ipv6-group-address* \[ **source-ip** *ipv6-source-address* \] **vlan** *vlan-id*]{lang="DA"}

[**[undo mld-snooping static-group]{lang="EN-US"}**[ { *ipv6-group-address* \[ **source-ip** *ipv6-source-address* \] **vlan** *vlan-id* \| **all** }]{lang="EN-US"}]{#struct_0_x6470_x2019_x1919292492}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1786749146}

[[端口不是]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x1712765233}[静态成员端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1020377069}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_501853219}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x964490423}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867592175}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1446122410}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x797266865}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1655173454}[：表示静态加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。]{style="font-family:
宋体"}

[**[source-ip ]{lang="EN-US"}***[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x909058850}[：表示静态加入的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址。如果指定了本参数，表示加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组；如果未指定本参数，则表示加入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。配置有本参数的静态成员端口，只在]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[版本]{style="font-family:宋体"}[2]{lang="EN-US"}[下生效。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_406078535}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6470_x2019_1875920695}[：]{style="font-family:宋体"}[表示对所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867657711}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1397066532}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源组（]{style="font-family:宋体"}[2002::22]{lang="EN-US"}[，]{style="font-family:宋体"}[FF3E::101]{lang="EN-US"}[）在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的静态成员端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1683734044}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] mld-snooping version 2]{lang="NL"}

[\[Sysname-vlan2\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping static-group ff3e::101 source-ip 2002::22 vlan 2]{lang="EN-US"}
:::

::: {#-1459248088 .myid}
[]{#_Toc404790131}[]{#struct_0_x6470_x2019_1361262233}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping static-router-port**

------------------------------------------------------------------------

[**[mld-snooping]{lang="DA"}[ static-router-port]{lang="EN-US"}**]{#struct_0_x6470_x2019_588463425}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由器端口。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x6470_x2019_689060259}**[mld-snooping]{lang="DA"}[ static-router-port]{lang="EN-US"}**[命令用来删除静态路由器端口的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867723247}

[**[mld-snooping]{lang="DA"}[ static-router-port vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1401090710}

[**[undo]{lang="EN-US"}**[ **mld-snooping** **static-router-port** { **all** \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x6470_x2019_x1680042326}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1245457948}

[[端口不是]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x275973049}[静态路由器端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x484542597}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6470_x2019_x86877282}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1106048353}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1772966590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867788783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_919461253}

[**[all]{lang="EN-US"}**]{#struct_0_x6470_x2019_1278774490}[：表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6470_x2019_x1570175221}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_458398673}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1751337566}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置为]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由器端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x401083144}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mld-snooping static-router-port vlan 2]{lang="EN-US"}
:::

::: {#10214654 .myid}
[]{#_Toc404790132}[]{#struct_0_x6470_x2019_x843351073}[]{#_Toc293908704}

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping version**

------------------------------------------------------------------------

[**[mld-snooping version]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1867854319}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的版本。]{style="font-family:宋体"}

[**[undo mld-snooping version]{lang="EN-US"}**]{#struct_0_x6470_x2019_2141990912}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x132434421}[令]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[**[mld-snooping version ]{lang="EN-US"}***[version-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1736773673}

[**[undo mld-snooping version]{lang="EN-US"}**]{#struct_0_x6470_x2019_205293901}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1916319869}

[[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x2123440654}[内]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的版本为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1765906731}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1585974855}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867919855}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1378669515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1126355969}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_963827248}

[*[version-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1859525666}[：表示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1728961889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x6470_x2019_x120805541}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x852962657}[VLAN]{lang="EN-US"}[的配置，]{style="font-family:宋体"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[version]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下可以对指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_939762695}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_598630212}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[版本为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1866936815}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="NL"}

[\[Sysname\] vlan 2]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping enable]{lang="NL"}

[\[Sysname-vlan2\] mld-snooping version 2]{lang="NL"}

[[\# ]{lang="NL"}]{#struct_0_x6470_x2019_x853224801}[在]{style="font-family:宋体"}[VSI aaa]{lang="NL"}[内使能]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[，]{style="font-family:宋体"}[并配置该]{style="font-family:宋体"}[VSI]{lang="NL"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="NL"}[版本为]{style="font-family:宋体"}[2]{lang="NL"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NL"}]{#struct_0_x6470_x2019_x853028193}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] mld-snooping version 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1457790046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x853093729}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_1476797620}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[version]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x852438369}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}
:::

::: {#1834251130 .myid}
[]{#_Toc404790133}[]{#struct_0_x6470_x2019_x1978369105}[]{#_Toc293908707}

**MLD Snooping \-- MLD Snooping配置命令 \-- overflow-replace (MLD-Snooping view)**

------------------------------------------------------------------------

[**[overflow-replace]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1408207525}[命令用来全局使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组替换功能。]{style="font-family:宋体"}

[**[undo overflow-replace]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1563944369}[命令用来全局关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组替换功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x651015896}

[**[overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x1741641066}

[**[undo overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_779053179}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867002351}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x375454057}[组播组替换功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1088432914}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x454104201}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2030903194}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1249016803}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1028552652}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_563938438}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_x2068958763}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1835334523}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x1867461106}[IPv6]{lang="EN-US"}[动态组播组有效，对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态组播组无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6470_x2019_x1198273998}**[mld]{lang="EN-US"}[-snooping overflow-replace]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1739684684}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x667270540}[全局使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组替换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_969285789}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] overflow-replace vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_64547792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping overflow-replace]{lang="EN-US"}**]{#struct_0_x6470_x2019_1858487461}
:::

::: {#-404357375 .myid}
[]{#_Toc293908709}[]{#_Toc404790134}[]{#struct_0_x6470_x2019_x579013554}[]{#_Toc351733181}[]{#_Toc293908708}

**MLD Snooping \-- MLD Snooping配置命令 \-- report-aggregation (MLD-Snooping view)**

------------------------------------------------------------------------

[**[report-aggregation]{lang="EN-US"}**]{#struct_0_x6470_x2019_1220638258}[命令用来使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文抑制功能。]{style="font-family:宋体"}

[**[undo report-aggregation]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1867526642}[命令用来关闭]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文抑制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2084596535}

[**[report-aggregation]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1799007161}

[**[undo report-aggregation]{lang="EN-US"}**]{#struct_0_x6470_x2019_x244889519}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1159342916}

[[MLD]{lang="EN-US"}]{#struct_0_x6470_x2019_188365823}[成员关系报告报文抑制功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1480863147}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_860422099}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_372391355}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867592178}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x330377163}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1431337881}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x196849964}[关闭]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_1621560628}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] undo report-aggregation]{lang="EN-US"}
:::

::: {#-437265329 .myid}
[]{#_Toc404790135}[]{#struct_0_x6470_x2019_x841862338}

**MLD Snooping \-- MLD Snooping配置命令 \-- reset mld-snooping group**

------------------------------------------------------------------------

[**[reset ]{lang="EN-US"}**]{#struct_0_x6470_x2019_1333799069}**[mld-snooping]{lang="DA"}[ group]{lang="EN-US"}**[命令用来清除动态]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1219345155}

[**[reset mld-snooping group]{lang="EN-US"}**[ { *ipv6-group-address* \[ *ipv6-source-address* \] \| **all** } \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x6470_x2019_x176362604}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867657714}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_x2138385877}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2123079819}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1559773395}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_337823461}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_2129395374}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x428554008}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。]{style="font-family:
宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x6470_x2019_x2031341875}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。如果未指定本参数，将清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6470_x2019_x796517435}[：清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1624466783}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x853224799}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867723250}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1327727109}[清除所有动态]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ]{lang="EN-US"}]{#struct_0_x6470_x2019_x369246492}[mld-snooping]{lang="DA"}[ ]{lang="DA"}[group all]{lang="EN-US"}

[]{#_Toc293908710}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1121985477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mld-snooping group]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1563582600}
:::

::: {#644958037 .myid}
[]{#_Toc404790136}[]{#struct_0_x6470_x2019_283521746}[]{#_Toc302380312}

**MLD Snooping \-- MLD Snooping配置命令 \-- reset mld-snooping router-port**

------------------------------------------------------------------------

[**[reset ]{lang="EN-US"}**]{#struct_0_x6470_x2019_x830494079}**[mld-snooping]{lang="DA"}[ ]{lang="DA"}[router-port]{lang="EN-US"}**[命令用来清除]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1330769876}

[**[reset mld-snooping router-port]{lang="EN-US"}**[ { **all** \| **vlan** *vlan-id* \| **vsi** *vsi-name* }]{lang="EN-US"}]{#struct_0_x6470_x2019_1605298528}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867788786}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_159946366}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_738720341}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x253105906}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_770747135}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_393510423}

[**[all]{lang="EN-US"}**]{#struct_0_x6470_x2019_141310481}[：清除所有动态路由器端口的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1977034893}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x6470_x2019_x853224804}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x652953156}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1512860393}[清除所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867854322}[mld-snooping]{lang="DA"}[ ]{lang="DA"}[router-port all]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x943319411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mld-snooping router-port]{lang="EN-US"}**]{#struct_0_x6470_x2019_x215864735}
:::

::: {#-540883330 .myid}
[]{#_Toc404790137}[]{#struct_0_x6470_x2019_x1230330482}

**MLD Snooping \-- MLD Snooping配置命令 \-- reset mld-snooping statistics**

------------------------------------------------------------------------

[**[reset mld-snooping statistics]{lang="EN-US"}**]{#struct_0_x6470_x2019_502464988}[命令用来清除]{style="font-family:
宋体"}[MLD Snooping]{lang="EN-US"}[监听到的]{style="font-family:
宋体"}[MLD]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1251753229}

[**[reset mld-snooping statistics]{lang="EN-US"}**]{#struct_0_x6470_x2019_1610663649}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x401037555}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6470_x2019_734875210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1117995093}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867919858}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x975384988}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x8858478}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_1008190466}[清除]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset mld-snooping statistics]{lang="EN-US"}]{#struct_0_x6470_x2019_71836621}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x849838669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mld-snooping statistics]{lang="EN-US"}**]{#struct_0_x6470_x2019_1547286184}
:::

::: {#-1141991402 .myid}
[]{#_Toc404790138}[]{#struct_0_x6470_x2019_x1573943187}[]{#_Toc293908711}

**MLD Snooping \-- MLD Snooping配置命令 \-- router-aging-time (MLD-Snooping view)**

------------------------------------------------------------------------

[**[router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_839116972}[命令用来全局配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的老化时间。]{style="font-family:宋体"}

[**[undo router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1866936818}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1861074573}

[**[router-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x6470_x2019_x895277507}

[**[undo router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_1982831134}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x953554170}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_1157505025}[动态路由器端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_812244325}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x802510125}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1732382399}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1946440634}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867002354}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1134968944}

[*[interval]{lang="EN-US"}*]{#struct_0_x6470_x2019_x1154643561}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x406337763}

[[本命令与]{style="font-family:宋体"}**[mld-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1246605608}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x931704219}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x396816309}[全局配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[动态路由器端口的老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x948498465}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] router-aging-time 100]{lang="EN-US"}[]{#_Toc138647989}[]{#_Toc138648274}[]{#_Toc138648543}[]{#_Toc138647990}[]{#_Toc138648275}[]{#_Toc138648544}[]{#_Toc138647993}[]{#_Toc138648278}[]{#_Toc138648547}[]{#_Toc134006615}[]{#_Toc138647998}[]{#_Toc138648283}[]{#_Toc138648552}[]{#_Toc135732953}[]{#_Toc136006430}[]{#_Toc136009014}[]{#_Toc136009484}[]{#_Toc136009706}[]{#_Toc136659547}[]{#_Toc134006634}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_188069420}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1867461105}
:::

::::: {#-571094675 .myid}
[]{#_Toc404790139}[]{#struct_0_x6470_x2019_367809943}[]{#_Toc330456988}

**MLD Snooping \-- MLD Snooping配置命令 \-- source-deny (MLD-Snooping view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MLD%20Snooping命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6470_x2019_1311642384}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6470_x2019_x1920721995}
:::

[ ]{lang="EN-US"}

[**[source-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1141852382}[命令用来使能指定端口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[**[undo source-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_x261108079}[命令用来关闭指定端口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1107985436}

[**[source-deny port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x6470_x2019_x244569213}

[**[undo source-deny port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x6470_x2019_1980967587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867526641}

[[IPv6]{lang="EN-US"}]{#struct_0_x6470_x2019_x644286820}[组播数据报文源端口过滤功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1749134073}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x1385662709}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1606467397}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x2134539969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x2083985855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1477154571}

[**[port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x6470_x2019_442369879}[：表示对指定端口进行配置。]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[为端口列表，表示一或多个端口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type* *interface-number* \[ **to** *interface-type* *interface-number* \] }]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1679833996}

[[本命令与]{style="font-family:宋体"}**[mld-snooping source-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1867592177}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[MLD-Snooping]{lang="EN-US"}[视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1686045472}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_x378093953}[使能端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[～]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x1054378447}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] source-deny port gigabitethernet 1/0/1 to gigabitethernet 1/0/4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1390765846}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld-snooping]{lang="DA"}[ ]{lang="DA"}[source-deny]{lang="EN-US"}**]{#struct_0_x6470_x2019_x174593696}
:::::

::: {#410599914 .myid}
[]{#_Toc404790140}[]{#struct_0_x6470_x2019_x969705724}[]{#_Toc345425352}[]{#_Toc345425154}

**MLD Snooping \-- MLD Snooping配置命令 \-- version (MLD-Snooping view)**

------------------------------------------------------------------------

[**[version]{lang="EN-US"}**]{#struct_0_x6470_x2019_x882546576}[命令用来配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的版本。]{style="font-family:宋体"}

[**[undo version]{lang="EN-US"}**]{#struct_0_x6470_x2019_x1867657713}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命]{style="font-family:黑体"}]{#struct_0_x6470_x2019_234267118}[令]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[**[version ]{lang="EN-US"}***[version-number]{lang="EN-US"}*[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x6470_x2019_x423252950}

[**[undo version]{lang="EN-US"}**[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x6470_x2019_1534912999}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1812267728}

[[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_x2141222992}[内]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的版本为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_1977384932}

[[MLD-Snooping]{lang="EN-US"}]{#struct_0_x6470_x2019_x976943207}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x190089345}

[[network-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_1957170122}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6470_x2019_x1867723249}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x594521656}

[*[version-number]{lang="EN-US"}*]{#struct_0_x6470_x2019_1011200365}[：表示]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x6470_x2019_x413596311}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x52642891}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_647013936}[内使能]{lang="EN-US" style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6470_x2019_1513923170}[的配置，本命令与]{lang="EN-US" style="font-family:宋体"}**[mld]{lang="EN-US"}[-snooping]{lang="EN-US"}[ version]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[MLD]{lang="EN-US"}[-Snooping]{lang="EN-US"}[视图下可以对指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1508049488}

[[\# ]{lang="EN-US"}]{#struct_0_x6470_x2019_104090118}[使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[，并配置这些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[MLD Snooping]{lang="EN-US"}[版本为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6470_x2019_x340674734}

[\[Sysname\] mld-snooping]{lang="EN-US"}

[\[Sysname-mld-snooping\] enable vlan 2 to 10]{lang="EN-US"}

[\[Sysname-mld-snooping\] version 2 vlan 2 to 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6470_x2019_x1867788785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x6470_x2019_x243338161}[MLD]{lang="EN-US"}[-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld]{lang="EN-US"}[-snooping enable]{lang="EN-US"}**]{#struct_0_x6470_x2019_2113844683}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mld]{lang="EN-US"}[-snooping]{lang="EN-US"}**]{#struct_0_x6470_x2019_1513988706}**[ version]{lang="EN-US"}**

[ ]{lang="EN-US"}
:::
