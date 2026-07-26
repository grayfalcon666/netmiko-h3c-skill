::: {#1224304223 .myid}
[]{#_Toc121110292}[]{#_Toc404789371}[]{#struct_0_x1820_12830_x184012105}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp-snooping**]{lang="EN-US"}]{#struct_0_x1820_12830_x790734128}[命令用来显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1261111119}

[**[display]{lang="EN-US"}**[ **igmp-snooping** \[ **global** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1844786858}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1251927254}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_x700255310}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1519466439}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1435636263}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_830683252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1836275011}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_1011011157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_767856781}

[**[global]{lang="EN-US"}**]{#struct_0_x1820_12830_x1111531005}[：显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的全局状态信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x1503521973}[：显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_x42068230}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[在指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1252123862}

[[如果未指定任何可选参数，将显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_x802961629}[在全局以及所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1742117280}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_595784049}[显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[在全局以及所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1252058326}

[IGMP snooping information: Global]{lang="EN-US"}

[ IGMP snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Disabled]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-member-query-interval: 1s]{lang="EN-US"}

[ Report-aggregation: Enabled]{lang="EN-US"}

[ Dot1p-priority: \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[IGMP snooping information: VLAN 1]{lang="EN-US"}

[ IGMP snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Disabled]{lang="EN-US"}

[ Version: 2]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-member-query-interval: 1s]{lang="EN-US"}

[ Querier: Disabled]{lang="EN-US"}

[ Query-interval: 125s]{lang="EN-US"}

[ General-query source IP: 1.1.1.1]{lang="EN-US"}

[ Special-query source IP: 2.2.2.2]{lang="EN-US"}

[ Report source IP: 3.0.0.3]{lang="EN-US"}

[ Leave source IP: 1.0.0.1]{lang="EN-US"}

[ Dot1p-priority: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[IGMP snooping information: VLAN 10]{lang="EN-US"}

[ IGMP snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Enabled]{lang="EN-US"}

[ Version: 3]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-member-query-interval: 1s]{lang="EN-US"}

[ Querier: Disabled]{lang="EN-US"}

[ Query-interval: 125s]{lang="EN-US"}

[ General-query source IP: 1.1.1.1]{lang="EN-US"}

[ Special-query source IP: 2.2.2.2]{lang="EN-US"}

[ Report source IP: 3.0.0.3]{lang="EN-US"}

[ Leave source IP: 1.0.0.1]{lang="EN-US"}

[ Dot1p-priority: \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[IGMP snooping information: VSI aaa]{lang="EN-US"}

[ IGMP snooping: Enabled]{lang="EN-US"}

[ Drop-unknown: Enabled]{lang="EN-US"}

[ Version: 2]{lang="EN-US"}

[ Host-aging-time: 260s]{lang="EN-US"}

[ Router-aging-time: 260s]{lang="EN-US"}

[ Max-response-time: 10s]{lang="EN-US"}

[ Last-member-query-interval: 1s]{lang="EN-US"}

[ Querier: Disabled]{lang="EN-US"}

[ Query-interval: 125s]{lang="EN-US"}

[ General-query source IP: 1.1.1.1]{lang="EN-US"}

[ Special-query source IP: 2.2.2.2]{lang="EN-US"}

[]{#struct_0_x1820_12830_x909915669}[[表1-1 ]{lang="EN-US"}[display igmp-snooping]{lang="EN-US"}]{#_Toc288831908}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1305711266}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1989658424}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2080876940}

[[IGMP snooping information]{lang="EN-US"}]{#struct_0_x1820_12830_1900993623}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1252254934}[的状态信息]{style="font-family:宋体"}

[[IGMP snooping]{lang="EN-US"}]{#struct_0_x1820_12830_x1208331548}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_826689441}[的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1820_12830_x1954791222}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1820_12830_x1224326486}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Drop-unknown]{lang="EN-US"}]{#struct_0_x1820_12830_x1684637467}

[[丢弃未知组播数据报文功能的使能状态（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1226718621}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1820_12830_1252189398}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1820_12830_650466600}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Version]{lang="EN-US"}]{#struct_0_x1820_12830_667479668}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_x423636460}[的版本]{style="font-family:宋体"}

[[Host-aging-time]{lang="EN-US"}]{#struct_0_x1820_12830_x465954714}

[[动态成员端口的老化时间]{style="font-family:宋体"}]{#struct_0_x1820_12830_781972502}

[[Router-aging-time]{lang="EN-US"}]{#struct_0_x1820_12830_1251730647}

[[动态路由器端口老化时间]{style="font-family:宋体"}]{#struct_0_x1820_12830_455025844}

[[Max-response-time]{lang="EN-US"}]{#struct_0_x1820_12830_x706497245}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x389918922}[普遍组查询的最大响应时间]{style="font-family:宋体"}

[[Last-member-query-interval]{lang="EN-US"}]{#struct_0_x1820_12830_x1625317259}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_1251665111}[特定组查询报文的发送间隔]{style="font-family:宋体"}

[[Report-aggregation]{lang="EN-US"}]{#struct_0_x1820_12830_1454903309}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x1490958823}[成员关系报告报文抑制功能的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1820_12830_1014912327}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1820_12830_1454968845}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Dot1p-priority]{lang="EN-US"}]{#struct_0_x1820_12830_x724645690}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_1455034381}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示没有配置]{style="font-family:宋体"}

[[Querier]{lang="EN-US"}]{#struct_0_x1820_12830_1234719389}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1455099917}[查询器的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1820_12830_x736602803}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1820_12830_1455165453}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Query-interval]{lang="EN-US"}]{#struct_0_x1820_12830_1237507568}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_1454182413}[普遍组查询报文的发送间隔]{style="font-family:宋体"}

[[General-query source IP]{lang="EN-US"}]{#struct_0_x1820_12830_22035389}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_882948263}[普遍组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Special-query source IP]{lang="EN-US"}]{#struct_0_x1820_12830_1454247949}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x660998886}[特定组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Report source IP]{lang="EN-US"}]{#struct_0_x1820_12830_1454706700}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x323458802}[成员关系报告报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Leave source IP]{lang="EN-US"}]{#struct_0_x1820_12830_1454772236}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x1098761347}[离开组报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#391798419 .myid}
[]{#_Toc109290001}[]{#_Toc109289999}[]{#_Toc52102254}[]{#_Toc404789372}[]{#struct_0_x1820_12830_2027544007}[]{#_Toc123030573}[]{#_Toc121110309}[]{#_Toc114641929}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping group**

------------------------------------------------------------------------

[**[display igmp-snooping group]{lang="EN-US"}**]{#struct_0_x1820_12830_x1575135978}[命令用来显示动态]{style="font-family:
宋体"}[IGMP Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1103799062}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x936821502}

[**[display igmp-snooping]{lang="EN-US"}**[ **group** \[ *group-address* \| *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1944088188}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1872172890}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_1418063613}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *group-address* \| *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_1135126355}[模式：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_1251861719}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *group-address* \| *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x323637395}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1294430970}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_414313473}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x256025593}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x1092572523}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_464140910}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x10991415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1251796183}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x716347130}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x1820_12830_1687766771}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_857956415}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_x41478406}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1820_12830_1598496947}[：]{style="font-family:宋体"}[显示详细信息。如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_638009690}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x689224925}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x1231539646}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_991303345}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x274606937}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_307412576}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1025719073}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1251992791}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内动态]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping group vlan 2 verbose]{lang="EN-US"}]{#struct_0_x1820_12830_1227045565}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 entries.]{lang="EN-US"}

[  (0.0.0.0, 224.1.1.1)]{lang="EN-US"}

[    Attribute: local port]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/2                             (00:03:23)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x41543942}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内动态]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping group vsi aaa verbose]{lang="EN-US"}]{#struct_0_x1820_12830_179307228}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 entries.]{lang="EN-US"}

[  (0.0.0.0, 224.1.1.1)]{lang="EN-US"}

[    Attribute: global port]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)         (00:03:35)]{lang="EN-US"}

[        VLAN pairs (1 in total):]{lang="EN-US"}

[          Out VLAN 5     In VLAN 2        (00:03:35)]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display igmp-snooping group]{lang="EN-US"}]{#struct_0_x1820_12830_x2092181995}[命令显示信息描述表]{style="font-family:黑体"}

[]{#_Toc123030574}[]{#_Toc121110274}[]{#table_struct_0_1306886359}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_1328322233}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_997203260}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x1820_12830_1250769861}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_1251927255}

[[VLAN 2: Total 1 entries]{lang="EN-US"}]{#struct_0_x1820_12830_x700320846}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_1577971996}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 entries]{lang="EN-US"}]{#struct_0_x1820_12830_x42002695}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x42068231}[内的表项总数]{style="font-family:宋体"}

[[(0.0.0.0, 224.1.1.1)]{lang="EN-US"}]{#struct_0_x1820_12830_1767161675}

[[（]{style="font-family:宋体"}]{#struct_0_x1820_12830_1119340620}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[0.0.0.0]{lang="FR"}[表示所有组播源]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x1820_12830_x2049726532}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x974740023}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[global port]{lang="FR"}]{#struct_0_x1820_12830_x2049660996}[：表示表项中存在全局口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[local port]{lang="FR"}]{#struct_0_x1820_12830_700052309}[：表示表项中存在本单板的端口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[slot]{lang="FR"}]{#struct_0_x1820_12830_1013159215}[：表示表项中存在其它单板的端口]{style="font-family:宋体"}

[[FSM information]{lang="EN-US"}]{#struct_0_x1820_12830_x2050119748}

[[表项状态机，包括：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1310792230}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_x1820_12830_658772895}[：表示所有成员属性均已删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dummy]{lang="FR"}]{#struct_0_x1820_12830_x2050054212}[：表示新创建的临时表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[no info]{lang="FR"}]{#struct_0_x1820_12830_x838371395}[：表示没有表项存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[normal]{lang="FR"}]{#struct_0_x1820_12830_1595764128}[：表示主控板通知创建的正式表项]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x1951791798}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x1820_12830_1252123863}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1820_12830_x2130777446}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1820_12830_x803333793}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_x2130777447}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_762750148}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x803027165}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1744286131}

[[(00:03:23)]{lang="EN-US"}]{#struct_0_x1820_12830_1608255506}

[[成员端口的老化剩余时间。需要注意的是，本字段对于全局口（包括二层聚合接口、]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x1820_12830_x1526961358}[口、]{style="font-family:宋体"}[N-PW]{lang="EN-US"}[口、]{style="font-family:宋体"}[U-PW]{lang="EN-US"}[口等）将无条件显示，而对于非全局口：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1820_12830_x2050381892}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1820_12830_x460834353}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_1252058327}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_x909850133}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x42264839}

[[AC]{lang="FR"}]{#struct_0_x1820_12830_x42330375}[（]{style="font-family:宋体"}[Attachment Circuit]{lang="FR"}[，接入电路）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_1870749389}

[[N-PW]{lang="FR"}]{#struct_0_x1820_12830_x42395911}[（]{style="font-family:宋体"}[Network Pseudowire]{lang="FR"}[，网络侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_692656945}

[[U-PW]{lang="FR"}]{#struct_0_x1820_12830_x185127164}[（]{style="font-family:宋体"}[User facing Pseudowire]{lang="FR"}[，用户侧伪线）口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[VLAN pairs (1 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x42461447}

[[VLAN]{lang="FR"}]{#struct_0_x1820_12830_x2139607249}[对及总数]{style="font-family:宋体"}

[[Out VLAN 5, in VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_x41478407}

[[外层]{style="font-family:宋体"}]{#struct_0_x1820_12830_x981228245}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[5]{lang="FR"}[，内层]{style="font-family:
  宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[2]{lang="FR"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x417467929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset igmp-snooping group]{lang="EN-US"}**]{#struct_0_x1820_12830_x311277766}

::: {#-408441163 .myid}
[]{#_Toc404789373}[]{#struct_0_x1820_12830_1196246672}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping router-port**

------------------------------------------------------------------------

[**[display igmp-snooping router-port]{lang="EN-US"}**]{#struct_0_x1820_12830_1912357414}[命令用来显示动态路由器端口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1023575580}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1615602456}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_1252254935}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[router-port]{lang="EN-US"}**[ \[ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \[ **verbose** \] \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1208266012}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_1145079565}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[router-port]{lang="EN-US"}**[ \[ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \[ **verbose** \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_1499815247}[模式：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_895202682}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[router-port]{lang="EN-US"}**[ \[ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* \[ **verbose** \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_32015094}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_x2142753437}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x720622528}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1267198669}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_1252189399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_650401064}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x128121240}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1580239508}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1820_12830_x445352753}[：]{style="font-family:宋体"}[显示详细信息。如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x322341032}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_1871325116}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1825142165}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x195486471}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_737828822}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_2037780320}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_201422441}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_81906383}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x674756483}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1477152705}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内动态路由器端口的信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping router-port vlan 2]{lang="EN-US"}]{#struct_0_x1820_12830_217446532}

[VLAN 2:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    GE1/0/1                             (00:01:30)]{lang="EN-US"}

[    GE1/0/2                             (00:00:23)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x445418289}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内动态路由器端口的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping router-port vsi aaa verbose]{lang="EN-US"}]{#struct_0_x1820_12830_x445483825}

[VSI aaa:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (1 in total):]{lang="EN-US"}

[    AC (VSI index 0, link ID 1)         (00:03:35)]{lang="EN-US"}

[      VLAN pairs (1 in total):]{lang="EN-US"}

[        Out VLAN 5     In VLAN 2        (00:03:35)]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display igmp-snooping router-port]{lang="EN-US"}]{#struct_0_x1820_12830_1782875869}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1301153860}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_850902390}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_1902692567}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_438844012}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x1477218241}[的编号]{style="font-family:宋体"}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x445549361}

[[VSI]{lang="EN-US"}]{#struct_0_x1820_12830_1061366436}[的名称]{style="font-family:宋体"}

[[Router slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_649915103}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1803499991}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1820_12830_x2130777436}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有动态路由器端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1820_12830_x803399329}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_1389103734}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有动态路由器端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1607925065}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有动态路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Router ports (2 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x214879519}

[[动态路由器端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_1875182429}

[[(00:01:30)]{lang="EN-US"}]{#struct_0_x1820_12830_x624222692}

[[动态路由器]{style="font-family:宋体"}]{#struct_0_x1820_12830_828893668}[端口的老化剩余时间。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式设备上，将无条件显示]{style="font-family:宋体"}]{#struct_0_x1820_12830_x483708123}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1477021633}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_1750040214}[IRF]{lang="EN-US"}[设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_x834853615}[IRF]{lang="EN-US"}[模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x445680433}

[[AC]{lang="FR"}]{#struct_0_x1820_12830_x445745969}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_762295198}

[[N-PW]{lang="FR"}]{#struct_0_x1820_12830_x1737322539}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x444762929}

[[U-PW]{lang="FR"}]{#struct_0_x1820_12830_x1209784259}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[VLAN pairs (1 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x444828465}

[[VLAN]{lang="FR"}]{#struct_0_x1820_12830_256226984}[及总数]{style="font-family:宋体"}

[[Out VLAN 5, in VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_x445287218}

[[外层]{style="font-family:宋体"}]{#struct_0_x1820_12830_x445352754}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[5]{lang="FR"}[，内层]{style="font-family:
  宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}[2]{lang="FR"}

[ ]{lang="EN-US"}

[]{#_Toc293908670}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_321476529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset igmp-snooping router-port]{lang="EN-US"}**]{#struct_0_x1820_12830_358242960}

::: {#1264156924 .myid}
[]{#_Toc404789374}[]{#struct_0_x1820_12830_x522174666}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping static-group**

------------------------------------------------------------------------

[**[display igmp-snooping static]{lang="EN-US"}**]{#struct_0_x1820_12830_538521190}[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[命令用来显示静态]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1831394123}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1477087169}

[**[display igmp-snooping]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_x1820_12830_315180073}[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *group-address* \| *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **verbose** \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1956046044}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_x1820_12830_927725995}[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *group-address* \| *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **verbose** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_1747073377}[模式：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_x1820_12830_x1333080255}[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[group]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *group-address* \| *source-address* \] \* \[ **vlan** *vlan-id* \] \[ **verbose** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1067125116}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_1531976230}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x8901954}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1476890561}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x854419593}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1962091213}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x2003318682}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1990138947}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1820_12830_694835923}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x1022869726}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_1309864510}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1820_12830_514061645}[：]{style="font-family:宋体"}[显示详细信息。如果未指定本参数，将显示简要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x1283295239}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x1476956097}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x21686065}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x426635410}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x1736322276}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_1900693772}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_851682248}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_669660791}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内静态]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping static-group vlan 2 verbose]{lang="EN-US"}]{#struct_0_x1820_12830_x1367036261}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 entries.]{lang="EN-US"}

[  (0.0.0.0, 224.1.1.1)]{lang="EN-US"}

[    Attribute: local port]{lang="EN-US"}

[    FSM information: normal]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/2]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display igmp-snooping static]{lang="EN-US"}]{#struct_0_x1820_12830_x1512976902}[[-]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[group]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1303047120}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476759489}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_1690464236}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x1820_12830_545925783}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_1708516367}

[[VLAN 2: Total 1 entries]{lang="EN-US"}]{#struct_0_x1820_12830_x964162438}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_1352468982}[内的表项总数]{style="font-family:宋体"}

[[(0.0.0.0, 224.1.1.1)]{lang="EN-US"}]{#struct_0_x1820_12830_1278855533}

[[（]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1476825025}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[0.0.0.0]{lang="FR"}[表示所有组播源]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x1820_12830_x484035804}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x483970268}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[global port]{lang="FR"}]{#struct_0_x1820_12830_x483904732}[：表示表项中存在全局口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[local port]{lang="FR"}]{#struct_0_x1820_12830_x1150740550}[：表示表项中存在本单板的端口]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[slot]{lang="FR"}]{#struct_0_x1820_12830_x483839196}[：表示表项中存在其它单板的端口]{style="font-family:宋体"}

[[FSM information]{lang="EN-US"}]{#struct_0_x1820_12830_x1492642504}

[[表项状态机，包括：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x484297948}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_x1820_12830_x484232412}[：表示所有成员属性均已删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dummy]{lang="FR"}]{#struct_0_x1820_12830_1854233361}[：表示新创建的临时表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[no info]{lang="FR"}]{#struct_0_x1820_12830_x483773661}[：表示没有表项存在]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[normal]{lang="FR"}]{#struct_0_x1820_12830_x483708125}[：表示主控板通知创建的正式表项]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x863934483}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1047923683}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1820_12830_207874720}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1820_12830_1678339950}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_1669929913}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_207874719}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_908996845}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1237782128}

[ ]{lang="EN-US"}

::: {#-1455212073 .myid}
[]{#_Toc404789375}[]{#struct_0_x1820_12830_x1987098515}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping static-router-port**

------------------------------------------------------------------------

[**[display igmp-snooping static-router-port]{lang="EN-US"}**]{#struct_0_x1820_12830_x2042859428}[命令用来显示静态路由器端口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476628417}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1428532953}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_716847392}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static-router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1040672975}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_x732552354}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static-router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_x318387284}[模式：]{style="font-family:宋体"}

[**[display igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_x158054689}[[ ]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}**[static-router-port]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2101665999}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_x2039708067}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476693953}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1602376123}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_242688180}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_869178098}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x219909590}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1620181832}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x79910820}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_588153033}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1332897490}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x1231474110}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x1477152704}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_1688325004}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x549405029}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1348637409}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1315517524}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内静态路由器端口的信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping static-router-port vlan 2]{lang="EN-US"}]{#struct_0_x1820_12830_127926819}

[VLAN 2:]{lang="EN-US"}

[  Router slots (0 in total):]{lang="EN-US"}

[  Router ports (2 in total):]{lang="EN-US"}

[    GE1/0/1]{lang="EN-US"}

[    GE1/0/2]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display igmp-snooping static-router-port]{lang="EN-US"}]{#struct_0_x1820_12830_x748122008}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1296829026}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1513281644}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1477218240}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_x916168838}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_670594801}[的编号]{style="font-family:宋体"}

[[Router slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_480553956}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1513281405}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1820_12830_207874724}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有静态路由器端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1820_12830_1678339954}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_1670192057}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有静态路由器端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_628563488}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有静态路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Router ports (2 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x1902836420}

[[静态路由器端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_724362879}

[ ]{lang="EN-US"}

::: {#-1090782547 .myid}
[]{#_Toc404789376}[]{#struct_0_x1820_12830_x1477021632}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp**-**snooping** **statistics**]{lang="EN-US"}]{#struct_0_x1820_12830_x978843141}[命令用来显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1930266726}

[**[display igmp-snooping statistics]{lang="EN-US"}**]{#struct_0_x1820_12830_x63087321}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1888462926}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_2069262874}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x823054278}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1990251003}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x361629858}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1477087168}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_1881264014}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1307724319}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_290256374}[显示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp-snooping statistics]{lang="EN-US"}]{#struct_0_x1820_12830_x765746443}

[Received IGMP general queries:  0]{lang="EN-US"}

[Received IGMPv1 reports:  0]{lang="EN-US"}

[Received IGMPv2 reports:  19]{lang="EN-US"}

[Received IGMP leaves:  0]{lang="EN-US"}

[Received IGMPv2 specific queries:  0]{lang="EN-US"}

[Sent     IGMPv2 specific queries:  0]{lang="EN-US"}

[Received IGMPv3 reports:  1]{lang="EN-US"}

[Received IGMPv3 reports with right and wrong records:  0]{lang="EN-US"}

[Received IGMPv3 specific queries:  0]{lang="EN-US"}

[Received IGMPv3 specific sg queries:  0]{lang="EN-US"}

[Sent     IGMPv3 specific queries:  0]{lang="EN-US"}

[Sent     IGMPv3 specific sg queries:  0]{lang="EN-US"}

[Received error IGMP messages:  19]{lang="EN-US"}

[]{#struct_0_x1820_12830_x1476890560}[[表1-6 ]{lang="EN-US"}[display igmp-snooping statistics]{lang="EN-US"}]{#_Toc288831907}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1298408104}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_1874463762}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_2086709532}

[[general queries]{lang="EN-US"}]{#struct_0_x1820_12830_x301974890}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_680248380}[普遍组查询报文的数量]{style="font-family:宋体"}

[[specific queries]{lang="EN-US"}]{#struct_0_x1820_12830_274960710}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_1630990479}[特定组查询报文的数量]{style="font-family:宋体"}

[[reports]{lang="EN-US"}]{#struct_0_x1820_12830_x1476956096}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x1992719351}[成员关系报告报文的数量]{style="font-family:宋体"}

[[leaves]{lang="EN-US"}]{#struct_0_x1820_12830_x621313573}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_314269408}[离开组报文的数量]{style="font-family:宋体"}

[[reports with right and wrong records]{lang="EN-US"}]{#struct_0_x1820_12830_894658850}

[[包含错误和正确纪录的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x836042254}[成员关系报告报文数量]{style="font-family:宋体"}

[[specific sg queries]{lang="EN-US"}]{#struct_0_x1820_12830_x981677344}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x1476759488}[特定源组查询报文的数量]{style="font-family:宋体"}

[[error IGMP messages]{lang="EN-US"}]{#struct_0_x1820_12830_124380295}

[[错误]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x940025445}[报文的数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1181699435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset igmp-snooping statistics]{lang="EN-US"}**]{#struct_0_x1820_12830_x1404584387}

::: {#-2111393152 .myid}
[]{#_Toc404789377}[]{#struct_0_x1820_12830_x1703478017}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast ip**

------------------------------------------------------------------------

[**[display l2-multicast ip]{lang="EN-US"}**]{#struct_0_x1820_12830_60871997}[命令用来显示二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476825024}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_702149458}

[**[display l2-multicast ip]{lang="EN-US"}**[ \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1196013822}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1470386317}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display l2-multicast ip]{lang="EN-US"}**[ \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_985630592}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_1545600055}[模式：]{style="font-family:宋体"}

[**[display l2-multicast ip]{lang="EN-US"}**[ \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_x285981808}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_73382378}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_x898062651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476628416}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_137550988}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_555948793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x868031402}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x1824418565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1004904616}

[**[group]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_x1820_12830_x1596787408}[：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ source-address]{lang="EN-US"}*]{#struct_0_x1820_12830_1243898800}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x1476693952}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_x445352751}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1126507232}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1714077345}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_737894358}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_1028749763}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_973836541}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x828189583}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_546589944}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1534258913}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast ip vlan 2]{lang="EN-US"}]{#struct_0_x1820_12830_1660827669}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 IP entries.]{lang="EN-US"}

[  (0.0.0.0, 224.1.1.1)]{lang="EN-US"}

[    Attribute: static, success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/1                             (S, SUC)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x445483823}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast ip vsi aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x63071051}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 IP entries.]{lang="EN-US"}

[  (0.0.0.0, 224.1.1.1)]{lang="EN-US"}

[    Attribute: ]{lang="EN-US"}[dynamic]{lang="FR"}[, success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)         (D, SUC)]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display l2-multicast ip]{lang="EN-US"}]{#struct_0_x1820_12830_x1477152707}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1292843006}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_x945352882}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_2093557695}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x1820_12830_x1124548383}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_2004963968}

[[VLAN 2: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x1820_12830_x1941921409}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_1060889884}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x1820_12830_x445549359}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1820_12830_1060842151}[内的表项总数]{style="font-family:宋体"}

[[(0.0.0.0, 224.1.1.1)]{lang="EN-US"}]{#struct_0_x1820_12830_x1477218243}

[[（]{style="font-family:宋体"}]{#struct_0_x1820_12830_x512884311}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[0.0.0.0]{lang="FR"}[表示所有组播源]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x1820_12830_1259120013}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x2054281997}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="FR"}]{#struct_0_x1820_12830_1259801606}[：表示由动态协议创建的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[static]{lang="FR"}]{#struct_0_x1820_12830_x874270866}[：表示由静态协议创建的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[pim]{lang="FR"}]{#struct_0_x1820_12830_x1477021635}[：表示由]{style="font-family:宋体"}[PIM]{lang="FR"}[协议创建的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[kernel]{lang="FR"}]{#struct_0_x1820_12830_x1382127668}[：表示从内核中获取的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="FR"}]{#struct_0_x1820_12830_x1999495078}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[处理]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="FR"}]{#struct_0_x1820_12830_906845312}[：表示处理失败]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_1934741187}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x1820_12830_900309015}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1748440418}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1820_12830_2071089844}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_359010071}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_x288993270}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x1477087171}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_x40984751}

[[(S, SUC)]{lang="EN-US"}]{#struct_0_x1820_12830_x2146611274}

[[端口属性，包括：]{style="font-family:宋体"}]{#struct_0_x1820_12830_787477447}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="FR"}]{#struct_0_x1820_12830_x269816541}[：表示动态端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="FR"}]{#struct_0_x1820_12830_x1476890563}[：表示静态端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="FR"}]{#struct_0_x1820_12830_x2017219007}[：表示]{style="font-family:宋体"}[PIM]{lang="FR"}[端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[K]{lang="FR"}]{#struct_0_x1820_12830_x1347975574}[：表示从内核中获取的端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="FR"}]{#struct_0_x1820_12830_x278138265}[：表示从（]{style="font-family:宋体"}[\*]{lang="FR"}[，]{style="font-family:宋体"}[\*]{lang="FR"}[）表项扩展的端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="FR"}]{#struct_0_x1820_12830_433741086}[：表示从（]{style="font-family:宋体"}[\*]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项扩展的端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[SUC]{lang="FR"}]{#struct_0_x1820_12830_x1476956099}[：表示处理成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="FR"}]{#struct_0_x1820_12830_x876974104}[：表示处理失败]{style="font-family:宋体"}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x445745967}

[[AC]{lang="FR"}]{#struct_0_x1820_12830_762950558}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x444762927}

[[N-PW]{lang="FR"}]{#struct_0_x1820_12830_x1208866755}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x444828463}

[[U-PW]{lang="FR"}]{#struct_0_x1820_12830_x445287216}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#944819619 .myid}
[]{#_Toc404789378}[]{#struct_0_x1820_12830_1574819152}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast ip forwarding**

------------------------------------------------------------------------

[**[display l2-multicast ip forwarding]{lang="EN-US"}**]{#struct_0_x1820_12830_x800843120}[命令用来显示二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x446792371}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_946677818}

[**[display l2-multicast ip forwarding]{lang="EN-US"}**[ \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1111215267}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_1305764666}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display l2-multicast ip forwarding]{lang="EN-US"}**[ \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1476759491}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_1334168340}[模式：]{style="font-family:宋体"}

[**[display l2-multicast ip forwarding]{lang="EN-US"}**[ \[ **group** *group-address* \| **source** *source-address* \] \* \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1318864424}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1845548034}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_1054337034}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1198983942}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_650378843}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_1111534136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1317787373}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x1476825027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_298864931}

[**[group]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_x1820_12830_x570606857}[：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ source-address]{lang="EN-US"}*]{#struct_0_x1820_12830_1374994023}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x1896544694}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_x445418288}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x2049475465}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x1607654228}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1900759308}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x954651911}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_481639676}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_334675367}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x909083089}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1476628419}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast ip forwarding vlan 2]{lang="EN-US"}]{#struct_0_x1820_12830_x978194259}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 IP entries.]{lang="EN-US"}

[  (0.0.0.0, 224.1.1.1)]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (3 in total):]{lang="EN-US"}

[      GE1/0/1]{lang="EN-US"}

[      GE1/0/2]{lang="EN-US"}

[      GE1/0/3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x445483824}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast ip forwarding vsi aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x63136587}

[Total 1 entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 IP entries.]{lang="EN-US"}

[  (0.0.0.0, 224.1.1.1)]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display l2-multicast ip forwarding]{lang="EN-US"}]{#struct_0_x1820_12830_x734342043}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1322900748}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_1528089475}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1919922855}

[[Total 1 entries]{lang="EN-US"}]{#struct_0_x1820_12830_x1476693955}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_1886022119}

[[VLAN 2: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x1820_12830_184585787}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_x1587282996}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 IP entries]{lang="EN-US"}]{#struct_0_x1820_12830_x445549360}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x445614896}[内的表项总数]{style="font-family:宋体"}

[[(0.0.0.0, 224.1.1.1)]{lang="EN-US"}]{#struct_0_x1820_12830_1828694004}

[[（]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1233100494}[S]{lang="FR"}[，]{style="font-family:宋体"}[G]{lang="FR"}[）表项，]{style="font-family:
  宋体"}[0.0.0.0]{lang="FR"}[表示所有组播源]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_1203886720}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1477152706}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1820_12830_590211738}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1968279392}[成员端口]{style="font-family:宋体"}[的单板总数，以及各单板的槽位号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_x772877817}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有]{style="font-family:宋体"}[成员端口]{style="font-family:宋体"}[的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1245951478}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有]{style="font-family:宋体"}[成员端口]{style="font-family:宋体"}[的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (3 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_1783530473}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1118341429}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x445680432}

[[AC]{lang="FR"}]{#struct_0_x1820_12830_x445745968}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_762360734}

[[N-PW]{lang="FR"}]{#struct_0_x1820_12830_x444762928}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x444828464}

[[U-PW]{lang="FR"}]{#struct_0_x1820_12830_256292520}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-229122709 .myid}
[]{#_Toc404789379}[]{#struct_0_x1820_12830_1742247773}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast mac**

------------------------------------------------------------------------

[**[display l2-multicast mac]{lang="EN-US"}**]{#struct_0_x1820_12830_x291963629}[命令用来显示二层组播的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x323893065}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_x553689173}

[**[display l2-multicast mac]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1477218242}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x2078968252}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display l2-multicast mac]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1246819104}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_1045081777}[模式：]{style="font-family:宋体"}

[**[display l2-multicast mac]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_1729476726}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1113475623}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_1568694900}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1390814709}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x2118374895}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x1477021634}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_183956273}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_1589050797}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_980580202}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x1820_12830_109926726}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_3329420}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_x445418293}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1530536933}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x374789310}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1497474781}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x1051530960}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x424839520}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_1309416273}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1477087170}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1525099190}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast mac vlan 2]{lang="EN-US"}]{#struct_0_x1820_12830_721440075}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 0100-5e01-0101]{lang="EN-US"}

[    Attribute: success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      GE1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x445483829}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast mac vsi aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x63464267}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 0100-5e01-0101]{lang="EN-US"}

[    Attribute: success]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display l2-multicast mac]{lang="EN-US"}]{#struct_0_x1820_12830_x425792842}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1325104094}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_x179443027}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_312112924}

[[Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x1820_12830_x1476890562}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_711664348}

[[VLAN 2: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x1820_12830_x1786737504}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_1858809828}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x1820_12830_x445614901}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x1976615132}[内的表项总数]{style="font-family:宋体"}

[[MAC group address]{lang="EN-US"}]{#struct_0_x1820_12830_1247958088}

[[MAC]{lang="FR"}]{#struct_0_x1820_12830_680585103}[组播组的地址]{style="font-family:宋体"}

[[Attribute]{lang="EN-US"}]{#struct_0_x1820_12830_x1476956098}

[[表项属性，包括：]{style="font-family:宋体"}]{#struct_0_x1820_12830_1851909251}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="FR"}]{#struct_0_x1820_12830_x517057492}[：]{style="font-family:宋体"}[表示处理成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="FR"}]{#struct_0_x1820_12830_x477739444}[：]{style="font-family:宋体"}[表示处理失败]{lang="EN-US" style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_1651960107}

[[除当前单板外其它所有有成员端口的单板的]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1775950871}[槽位及总数]{style="font-family:
  宋体"}[。本字段的]{style="font-family:宋体"}[支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Host ports (1 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x1476759490}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_x231915601}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x445745973}

[[AC]{lang="FR"}]{#struct_0_x1820_12830_x444762933}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x1209128898}

[[N-PW]{lang="FR"}]{#struct_0_x1820_12830_x444828469}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x445287222}

[[U-PW]{lang="FR"}]{#struct_0_x1820_12830_x445352758}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1179795292 .myid}
[]{#_Toc404789380}[]{#struct_0_x1820_12830_x26371087}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast mac forwarding**

------------------------------------------------------------------------

[**[display l2-multicast mac forwarding]{lang="EN-US"}**]{#struct_0_x1820_12830_x2013716122}[命令用来显示二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1595925432}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1820_12830_207926615}

[**[display l2-multicast mac forwarding]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1064377373}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1285568901}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display l2-multicast mac forwarding]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1343215454}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1820_12830_x1476825026}[模式：]{style="font-family:宋体"}

[**[display l2-multicast mac forwarding]{lang="EN-US"}**[ \[ *mac-address* \] \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1820_12830_1864948872}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2041294288}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_2006803631}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1324047927}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1484595556}

[[network-operator]{lang="EN-US"}]{#struct_0_x1820_12830_1807793619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1979625199}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1820_12830_x1476628418}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_587889682}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x1741169089}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_1161614914}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_x445483830}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1928275445}[：]{style="font-family:宋体"}[显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_497407573}[：]{style="font-family:宋体"}[显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1820_12830_737959894}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，将显示主设备上维护的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x1247838764}[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x828124047}[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1820_12830_x1260507547}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_896777864}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1025980298}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast mac forwarding vlan 2]{lang="EN-US"}]{#struct_0_x1820_12830_x1476693954}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 2: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 0100-5e01-0101]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (3 in total):]{lang="EN-US"}

[      GE1/0/1]{lang="EN-US"}

[      GE1/0/2]{lang="EN-US"}

[      GE1/0/3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x445549366}[显示]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内二层组播的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2-multicast mac forwarding vsi aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x445614902}

[Total 1 MAC entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI aaa: Total 1 MAC entries.]{lang="EN-US"}

[  MAC group address: 0100-5e01-0101]{lang="EN-US"}

[    Host slots (0 in total):]{lang="EN-US"}

[    Host ports (1 in total):]{lang="EN-US"}

[      AC (VSI index 0, link ID 1)]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display l2-multicast mac forwarding]{lang="EN-US"}]{#struct_0_x1820_12830_319938178}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1317266255}[[字段]{style="font-family:黑体"}]{#struct_0_x1820_12830_x181937353}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1820_12830_221160221}

[[Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x1820_12830_616173489}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_x22935645}

[[VLAN 2: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x1820_12830_x1477152709}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x1820_12830_x1395691576}[内的表项总数]{style="font-family:宋体"}

[[VSI aaa: Total 1 MAC entries]{lang="EN-US"}]{#struct_0_x1820_12830_x445680438}

[[VSI aaa]{lang="EN-US"}]{#struct_0_x1820_12830_x445745974}[内的表项总数]{style="font-family:宋体"}

[[MAC group address]{lang="EN-US"}]{#struct_0_x1820_12830_876304581}

[[MAC]{lang="FR"}]{#struct_0_x1820_12830_x1760250790}[组播组的地址]{style="font-family:宋体"}

[[Host slots (0 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_1994322517}

[[本字段的]{style="font-family:宋体"}]{#struct_0_x1820_12830_1783787419}[支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备：不支持本字段]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1366103397}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1501466171}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1366103398}[IRF]{lang="EN-US"}[设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1820_12830_1677755878}[IRF]{lang="EN-US"}[模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号]{style="font-family:宋体"}

[[Host ports (3 in total)]{lang="EN-US"}]{#struct_0_x1820_12830_x1477218245}

[[成员端口及总数]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1319453365}

[[AC (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_x444762934}

[[AC]{lang="FR"}]{#struct_0_x1820_12830_x444828470}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[NPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_1120796724}

[[N-PW]{lang="FR"}]{#struct_0_x1820_12830_1120731188}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[UPW (VSI index 0, link ID 1)]{lang="EN-US"}]{#struct_0_x1820_12830_1120665652}

[[U-PW]{lang="FR"}]{#struct_0_x1820_12830_1120600116}[口的]{style="font-family:宋体"}[VSI]{lang="FR"}[索引和链路标识符]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc293908672}

::: {#-2119988164 .myid}
[]{#_Toc404789381}[]{#struct_0_x1820_12830_x474161199}[]{#_Toc354920930}[]{#_Toc293908671}[]{#_Toc208651408}[]{#_Toc207106535}[]{#_Toc207099655}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- dot1p-priority (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[dot1p-priority]{lang="EN-US"}**]{#struct_0_x1820_12830_x224883366}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo dot1p-priority]{lang="EN-US"}**]{#struct_0_x1820_12830_1101160363}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1931664435}

[**[dot1p-priority ]{lang="EN-US"}***[priority-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x474226735}

[**[undo dot1p-priority]{lang="EN-US"}**]{#struct_0_x1820_12830_2071379324}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x66187662}

[[没有配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x474292271}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_922807052}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1999589738}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x474357807}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x601667291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x197701763}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1524321877}

[*[priority-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x474423343}[：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。该数值越大，优先级越高。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_547583774}

[[对于基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_508193182}[的配置，本命令与]{style="font-family:宋体"}**[igmp-snooping dot1p-priority]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[有效，后者的配置优先级较高；对于基于]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的配置，]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x473440303}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x2034695553}[全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1520527218}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] dot1p-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x473505839}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x1820_12830_x1254334416}
:::

::::: {#-1379387681 .myid}
[]{#_Toc404789382}[]{#struct_0_x1820_12830_2085163762}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- drop-unknown (IGMP-Snooping view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP%20Snooping命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1820_12830_x605030929}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1820_12830_774697087}
:::

[ ]{lang="EN-US"}

[**[drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_1802578745}[命令用来全局使能丢弃未知组播数据报文功能。]{style="font-family:宋体"}

[**[undo drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_x1769355237}[命令用来全局关闭丢弃未知组播数据报文功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1053875236}

[**[drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_x1477021637}

[**[undo drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_x219328254}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x750618855}

[[丢弃未知组播数据报文功能处于关闭状态，即对未知组播数据报文进行广播。]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1623418969}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x466106149}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_657972319}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1993116430}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x2010234429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_2109396451}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1477087173}

[[本命令与]{style="font-family:宋体"}**[igmp-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_x1203784165}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1822860730}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1880896217}[全局使能丢弃未知组播数据报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x986685537}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] drop-unknown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1611822032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_x1863597218}
:::::

::: {#661448865 .myid}
[]{#_Toc404789383}[]{#struct_0_x1820_12830_x999696462}[]{#_Toc345425126}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- enable (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x1476890565}[命令用来使能指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo enable]{lang="EN-US"}**]{#struct_0_x1820_12830_1471179235}[命令用来关闭指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2004884340}

[**[enable]{lang="EN-US"}**[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x1820_12830_x40245039}

[**[undo enable]{lang="EN-US"}**[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x1820_12830_x2129464983}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x144239261}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1916348953}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1288525283}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_728248928}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476956101}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1233663217}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_324484899}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_436461243}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_712779976}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1120600115}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使能]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1301427101}[内的]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[之前，必须先全局使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1120534579}[的配置，本命令与]{lang="EN-US" style="font-family:宋体"}**[igmp-snooping]{lang="EN-US"}[ enable]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下可以对指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_126628610}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_779816880}[全局使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_938187311}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] enable vlan 2 to 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476759493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_171368926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_x1568525031}**[ enable]{lang="EN-US"}**
:::

::: {#418727915 .myid}
[]{#_Toc404789384}[]{#struct_0_x1820_12830_x1415138008}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- entry-limit (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[entry-limit]{lang="EN-US"}**]{#struct_0_x1820_12830_1967404493}[命令用来配置]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表项（包括动态表项和静态表项）的全局最大数量。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[entry-limit]{lang="EN-US"}**]{#struct_0_x1820_12830_2041456059}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_469335092}

[**[entry-limit ]{lang="EN-US"}***[limit]{lang="EN-US"}*]{#struct_0_x1820_12830_75973512}

[**[undo entry-limit]{lang="EN-US"}**]{#struct_0_x1820_12830_1371591566}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476825029}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_749203625}[转发表项的全局最大数量为]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_539895904}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1279864107}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1936393835}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1510700580}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1661221967}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x263583819}

[*[limit]{lang="EN-US"}*]{#struct_0_x1820_12830_1862106871}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表项的全局最大数量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476628421}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x621898363}[配置]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表项的全局最大数量为]{style="font-family:宋体"}[512]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x2089376079}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] entry-limit 512]{lang="EN-US"}
:::

::: {#817256077 .myid}
[]{#_Toc404789385}[]{#struct_0_x1820_12830_x2052756}[]{#_Toc293908674}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- fast-leave (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[fast-leave]{lang="EN-US"}**]{#struct_0_x1820_12830_x2021172822}[命令用来全局使能端口快速离开功能。]{style="font-family:宋体"}

[**[undo fast-leave]{lang="EN-US"}**]{#struct_0_x1820_12830_x1042889233}[命令用来全局关闭端口快速离开功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1662889374}

[**[fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_631778407}

[**[undo fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_3520770}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476693957}

[[端口快速离开功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1820_12830_723222705}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1005690245}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1136927652}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1670466008}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1294126406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1342521796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x809322537}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_x2134702130}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1477152708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口快速离开是指当端口收到主机发来的离开指定组播组的]{style="font-family:宋体"}]{#struct_0_x1820_12830_1333191779}[IGMP]{lang="EN-US"}[离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[igmp-snooping fast-leave]{lang="EN-US"}**]{#struct_0_x1820_12830_763076708}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:
宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_461085942}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1495604984}[全局使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的端口快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1490801953}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] fast-leave vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_115945389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping fast-leave]{lang="EN-US"}**]{#struct_0_x1820_12830_x206780733}
:::

::: {#-379503904 .myid}
[]{#_Toc404789386}[]{#struct_0_x1820_12830_x1477218244}[]{#_Toc293908675}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- group-policy (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[group-policy]{lang="DA"}**]{#struct_0_x1820_12830_1409429990}[命令用来全局配置组播组过滤器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[以限定主机所能加入的组播组。]{style="font-family:宋体"}

[**[undo group-policy]{lang="DA"}**]{#struct_0_x1820_12830_x668975904}[命令用来删除全局组播组过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x75994961}

[**[group-policy]{lang="EN-US"}**[ *acl-number* \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1025498327}

[**[undo group-policy]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1748026879}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1985513530}

[[没有配置组播组过滤器]{style="font-family:宋体"}]{#struct_0_x1820_12830_x686816717}[，]{style="font-family:宋体"}[即主机可以加入任意合法的组播组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1559941468}

[[IGMP-Snooping]{lang="DA"}]{#struct_0_x1820_12830_x1477021636}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1346755687}

[[network-admin]{lang="DA"}]{#struct_0_x1820_12830_893379996}

[[mdc-admin]{lang="DA"}]{#struct_0_x1820_12830_x113746216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1923040265}

[*[acl-number]{lang="DA"}*]{#struct_0_x1820_12830_1381693706}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv4]{lang="DA"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="DA"}[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="DA"}[～]{style="font-family:宋体"}[3999]{lang="DA"}[。主机只能加入该]{style="font-family:
宋体"}[ACL]{lang="DA"}[规则所允许的组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有组播组。]{style="font-family:宋体"}

[**[vlan ]{lang="DA"}**]{#struct_0_x1820_12830_1263403669}*[vlan-list]{lang="DA"}*[：]{style="font-family:
宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="DA"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="DA"}*[为]{style="font-family:宋体"}[VLAN]{lang="DA"}[列表]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[表示一或多个]{style="font-family:
宋体"}[VLAN]{lang="DA"}[，]{style="font-family:宋体"}[表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="DA"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="DA"}[，]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[vlan-id]{lang="DA"}*[为]{style="font-family:宋体"}[VLAN]{lang="DA"}[的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:
宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[4094]{lang="DA"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x504909545}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1820_12830_1388120885}[IPv4]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的]{style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1820_12830_x719353499}[IPv4]{lang="DA"}[高级]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:
宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[IGMPv1/v2]{lang="DA"}[报文和未携带组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[IGMPv3]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[视其组播源地址为]{lang="EN-US" style="font-family:宋体"}[0.0.0.0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以为端口在不同的]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1477087172}[VLAN]{lang="EN-US"}[内配置不同的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则，但在相同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内所配置的新规则会取代旧规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对动态组播组有效，对静态组播组无效。]{style="font-family:宋体"}]{#struct_0_x1820_12830_362299776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[igmp-snooping ]{lang="EN-US"}**]{#struct_0_x1820_12830_x1779059275}**[group-policy]{lang="DA"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:
宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1915370150}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_24905029}[全局配置组播组过滤器，以限定]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的主机只能加入组播组]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1746837668}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 225.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] group-policy 2000 vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x53060233}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping ]{lang="EN-US"}**]{#struct_0_x1820_12830_x1476890564}**[group-policy]{lang="DA"}**
:::

::: {#-392075321 .myid}
[]{#_Toc404789387}[]{#struct_0_x1820_12830_x94904706}[]{#_Toc293908676}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- host-aging-time (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_595970401}[命令用来全局配置动态成员端口的老化时间。]{style="font-family:宋体"}

[**[undo host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_342508105}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1380212748}

[**[host-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1820_12830_1594652826}

[**[undo host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_663580466}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_185804339}

[[动态成员端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}]{#struct_0_x1820_12830_149866295}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476956100}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1495220138}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2004375788}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x838836779}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1890453026}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1722970964}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_x406179138}[：表示动态成员端口的老化时间，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1102973521}

[[本命令与]{style="font-family:宋体"}**[igmp-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x1653101018}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476759492}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1394715015}[全局配置动态成员端口的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_968199586}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] host-aging-time 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1576459631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x1716249838}
:::

::: {#1377695043 .myid}
[]{#_Toc404789388}[]{#struct_0_x1820_12830_x1396944258}[]{#_Toc123030578}[]{#_Toc121110275}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping**

------------------------------------------------------------------------

[**[igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_x489014512}[命令用来全局使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_x1165879695}[命令用来全局关闭]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1476825028}

[**[igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_x1979679730}

[**[undo igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_579266732}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x213664505}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_x1880447669}[处于全局关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1879169310}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_1835080566}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_734663969}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x731757932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1476628420}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_944185578}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1373373581}[全局使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1763617213}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_554795975}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x415216840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_1424014125}
:::

::: {#-261994064 .myid}
[]{#_Toc404789389}[]{#struct_0_x1820_12830_x474226737}[]{#_Toc354920938}[]{#_Toc293908680}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping dot1p-priority**

------------------------------------------------------------------------

[**[igmp-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x1820_12830_x474292273}[命令用来在]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[内配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo igmp-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x1820_12830_922938124}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_10733218}

[**[igmp-snooping dot1p-priority ]{lang="EN-US"}***[priority-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x474357809}

[**[undo igmp-snooping dot1p-priority]{lang="EN-US"}**]{#struct_0_x1820_12830_x602060507}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_881127549}

[[没有配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x474423345}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_547190558}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1195278533}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x473440305}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x2034302337}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_708853955}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1238422255}

[*[priority-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x473505841}[：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。该数值越大，优先级越高。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1254858699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x122724106}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x473964594}[的配置，本命令与]{lang="EN-US" style="font-family:宋体"}**[dot1p-priority]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1434047833}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x391334069}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x474030130}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping dot1p-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1801059940}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1p-priority]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x1759344008}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1120403509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x474095666}
:::

::::: {#182485218 .myid}
[]{#_Toc404789390}[]{#struct_0_x1820_12830_x566337162}[]{#_Toc293908681}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping drop-unknown**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP%20Snooping命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1820_12830_x1476693956}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1820_12830_x842861236}
:::

[ ]{lang="EN-US"}

[**[igmp-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_x1541634450}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内使能丢弃未知组播数据报文功能。]{style="font-family:宋体"}

[**[undo igmp-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_1473893090}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内关闭丢弃未知组播数据报文功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x907564895}

[**[igmp-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_883540920}

[**[undo igmp-snooping drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_304045693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_496140339}

[[丢弃未知组播数据报文功能处于关闭状态，即对未知组播数据报文进行广播。]{style="font-family:宋体"}]{#struct_0_x1820_12830_1615764759}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_88931236}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_467790823}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_328956389}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1450509645}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x855345477}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2007018280}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_1013759033}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[drop-unknown]{lang="EN-US"}**]{#struct_0_x1820_12830_x572836604}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1507148124}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_88865700}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并使能丢弃未知组播数据报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1870436231}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping drop-unknown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1120469040}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并使能丢弃未知组播数据报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1120403504}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping drop-unknown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1212542366}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[drop-unknown]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x1862001850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1120337968}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_1324519724}
:::::

::: {#-1605170767 .myid}
[]{#_Toc404789391}[]{#struct_0_x1820_12830_859786414}[]{#_Toc123030580}[]{#_Toc121110295}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping enable**

------------------------------------------------------------------------

[**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_106644909}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_89062308}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内关闭]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1665002248}

[**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_284203607}

[**[undo igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_460684218}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1011033152}

[[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_x399333545}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1860384777}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1290340880}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1632000200}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_698094874}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_88996772}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x368132526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_x1912534539}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[之前，必须先全局使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{style="font-family:宋体"}]{#struct_0_x1820_12830_1120600111}[VLAN]{lang="EN-US"}[的配置，本命令与]{style="font-family:宋体"}**[enable]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下可以对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1771359499}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_489233325}[全局使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_567600565}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1120534575}[全局使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1791008564}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1027244496}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**]{#struct_0_x1820_12830_89193380}[ ]{lang="EN-US"}[(IGMP-Snooping view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_x1388340470}
:::

::: {#1685853223 .myid}
[]{#_Toc404789392}[]{#struct_0_x1820_12830_x1461741960}[]{#_Toc293908683}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping fast-leave**

------------------------------------------------------------------------

[**[igmp-snooping fast-leave]{lang="EN-US"}**]{#struct_0_x1820_12830_2054426660}[命令用来在端口上使能端口快速离开功能。]{style="font-family:
宋体"}

[**[undo ]{lang="EN-US"}[igmp-snooping fast-leave]{lang="EN-US"}**]{#struct_0_x1820_12830_1914002800}[命令用来在端口上关闭端口快速离开功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1112400913}

[**[igmp-snooping fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1360015848}

[**[undo igmp-snooping fast-leave]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1774361303}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x982794098}

[[端口快速离开功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1820_12830_89127844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2100836198}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x111781392}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_925064750}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x308997574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1652314003}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2000704199}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_x176756307}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1890664892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口快速离开是指当端口收到主机发来的离开指定组播组的]{style="font-family:宋体"}]{#struct_0_x1820_12830_89324452}[IGMP]{lang="EN-US"}[离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[fast-leave]{lang="EN-US"}**]{#struct_0_x1820_12830_x27082980}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x549525104}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1350716579}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能端口快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1742530530}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping fast-leave vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_707068260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fast-leave]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x93125743}
:::

::: {#1394306567 .myid}
[]{#_Toc404789393}[]{#struct_0_x1820_12830_x473505842}[]{#_Toc354920942}[]{#_Toc293908684}[]{#_Toc123030581}[]{#_Toc121110287}[]{#_Toc109290008}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping general-query source-ip**

------------------------------------------------------------------------

[**[igmp-snooping general-query source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_x1254924235}[命令用来配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo igmp-snooping general-query source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_1092119352}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1080475872}

[**[igmp-snooping general-query source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1820_12830_x1691826802}

[**[undo igmp-snooping general-query source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_1092053816}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1850803493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1565778861}[VLAN]{lang="EN-US"}[内，]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则采用]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1820_12830_717315589}[VSI]{lang="EN-US"}[内，]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1091988280}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x189418826}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_856596500}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_201241986}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1091922744}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_208891476}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x1663484914}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1091857208}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_x1393177536}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_583916321}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1091791672}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_966321080}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping general-query source-ip 10.1.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_717053445}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_718036485}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping general-query source-ip 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1091726136}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_717970949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x1378008699}
:::

::: {#1018834762 .myid}
[]{#_Toc404789394}[]{#struct_0_x1820_12830_1176798237}[]{#_Toc293908685}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping group-limit**

------------------------------------------------------------------------

[**[igmp-snooping group-limit]{lang="DA"}**]{#struct_0_x1820_12830_507875281}[命令用来[]{#_Toc127795919}[配置端口加入的组播组最大数量]{#_Ref127672022}。]{style="font-family:宋体"}

[**[undo ]{lang="DA"}**]{#struct_0_x1820_12830_89258916}**[igmp-snooping group-limit]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x320431729}

[**[igmp-snooping group-limit]{lang="EN-US"}**[ *limit* \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1564969483}

[**[undo igmp-snooping group-limit]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1910799858}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1455961350}

[[端口加入的组播组最大数量为]{style="font-family:宋体"}[4294967295]{lang="EN-US"}]{#struct_0_x1820_12830_842051412}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1101169990}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_348042906}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x206487751}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_89455524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x582595673}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2136968150}

[*[limit]{lang="EN-US"}*]{#struct_0_x1820_12830_x534664156}[：表示端口加入的组播组最大数量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_542380141}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x866019826}

[[本命令只对动态组播组有效，对静态组播组无效。]{style="font-family:宋体"}]{#struct_0_x1820_12830_755888165}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1498650620}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1006675863}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内加入的组播组最大数量为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_89389988}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping group-limit 10 vlan 2]{lang="EN-US"}
:::

::: {#-1701725406 .myid}
[]{#_Toc404789395}[]{#struct_0_x1820_12830_x924931322}[]{#_Toc293908686}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping group-policy**

------------------------------------------------------------------------

[**[igmp-snooping group-policy]{lang="DA"}**]{#struct_0_x1820_12830_389903958}[命令用来[]{#_Toc127848451}[]{#_Toc125123262}[]{#_Toc122232024}[在端口上配置组播组过滤器]{#_Ref114841739}]{style="font-family:宋体"}[，]{style="font-family:宋体"}[以限定主机所能加入的组播组。]{style="font-family:宋体"}

[**[undo ]{lang="DA"}**]{#struct_0_x1820_12830_x193841472}**[igmp-snooping group-policy]{lang="DA"}**[命令用来删除端口上的组播组过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2113228277}

[**[igmp-snooping group-policy]{lang="EN-US"}**[ *acl-number* \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1501486530}

[**[undo igmp-snooping group-policy]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x2108375540}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1415457176}

[[没有配置组播组过滤器，即主机可以加入任意合法的组播组。]{style="font-family:宋体"}]{#struct_0_x1820_12830_88931237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1870861337}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_1892105670}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1004620190}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x103444836}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1083753423}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1085866616}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1330077599}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。主机只能加入该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有组播组。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_2098313025}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_88865701}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1820_12830_468215929}[IPv4]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的]{style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1820_12830_847713478}[IPv4]{lang="DA"}[高级]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:
宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[IGMPv1/v2]{lang="DA"}[报文和未携带组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[IGMPv3]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[视其组播源地址为]{lang="EN-US" style="font-family:宋体"}[0.0.0.0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以为端口在不同的]{style="font-family:宋体"}]{#struct_0_x1820_12830_316027353}[VLAN]{lang="EN-US"}[内配置不同的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则，但在相同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内所配置的新规则会取代旧规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对动态组播组有效，对静态组播组无效。]{style="font-family:宋体"}]{#struct_0_x1820_12830_x441145126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1820_12830_1756803832}**[group-policy]{lang="DA"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x766720454}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x466476695}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置组播组过滤器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[以限定]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的主机只能加入组播组]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_89062309}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 225.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping group-policy 2000 vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_673649912}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[group-policy]{lang="DA"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_619521772}
:::

::: {#-2023558763 .myid}
[]{#_Toc404789396}[]{#struct_0_x1820_12830_1659481983}[]{#_Toc293908687}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping host-aging-time**

------------------------------------------------------------------------

[**[igmp-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x1610633223}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内配置动态成员端口的老化时间。]{style="font-family:宋体"}

[**[undo igmp-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_1395430377}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1982375898}

[**[igmp-snooping host-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1820_12830_x1581096561}

[**[undo igmp-snooping host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_55122614}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_88996773}

[[动态成员端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}]{#struct_0_x1820_12830_1588182610}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_581537307}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x1325820294}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1246664741}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_706179364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1412327602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2081997355}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_413648756}[：表示动态成员端口的老化时间，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89193381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_567974666}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[host-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_485351501}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_986892585}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1502823991}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置动态成员端口的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1374890132}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping host-aging-time 300]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_717315590}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置动态成员端口的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_717250054}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping host-aging-time 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1883425792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_717184518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[host-aging-time]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_799155125}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_89127845}
:::

::: {#1378260319 .myid}
[]{#_Toc404789397}[]{#struct_0_x1820_12830_1091922743}[]{#_Toc354920946}[]{#_Toc293908688}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping host-join**

------------------------------------------------------------------------

[**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[host-join]{lang="EN-US"}**]{#struct_0_x1820_12830_1091857207}[命令用来[]{#_Toc127848457}[]{#_Toc125123268}[配置模拟主机加入]{#_Ref125123127}组播组或组播源组。模拟主机加入就是将二层设备的端口配置为组播组的成员。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1820_12830_x1392194496}**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[host-join]{lang="EN-US"}**[命令用来删除模拟主机加入的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1274894393}

[**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[host-join ]{lang="EN-US"}***[group-address]{lang="EN-US"}*[ \[ **source-ip** *source-address* \] **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_1091791671}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1820_12830_966255544}**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[host-join]{lang="EN-US"}**[ { *group-address* \[ **source-ip** *source-address* \] **vlan** *vlan-id* \| **all** }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1550337965}

[[没有配置模拟主机加入组播组或组播源组。]{style="font-family:宋体"}]{#struct_0_x1820_12830_1091726135}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1378205307}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x316640757}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1091660599}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_980899954}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1738169426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1092643639}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x701695337}[：表示模拟主机要加入的组播组的地址，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-ip ]{lang="EN-US"}***[source-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x1585235799}[：表示模拟主机要加入的组播源的地址。如果指定了本参数，表示加入组播源组；如果未指定本参数，则表示加入组播组。配置有本参数的模拟主机，只在]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[版本]{style="font-family:宋体"}[3]{lang="EN-US"}[下生效。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_1092578103}[：表示]{style="font-family:宋体"}[对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1820_12830_717184513}[：表示对所有组播组和组播源组进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1252897586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[与静态成员端口不同，配置了模拟主机加入的端口将作为动态成员端口参与动态成员端口的老化过程。]{style="font-family:宋体"}]{#struct_0_x1820_12830_717118977}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[模拟主机]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1820_12830_x48630828}[所]{style="font-family:宋体"}[采用的]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="EN-US"}[版本与]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的版本一致。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1080606944}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1389939514}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置模拟主机加入]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的组播源组（]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[232.1.1.1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1092053814}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping version 3]{lang="EN-US"}

[\[Sysname-vlan2\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping host-join 232.1.1.1 source-ip 1.1.1.1 vlan 2]{lang="EN-US"}
:::

::: {#782860140 .myid}
[]{#_Toc404789398}[]{#struct_0_x1820_12830_237815962}[]{#_Toc293908696}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping last-member-query-interval**

------------------------------------------------------------------------

[**[igmp-snooping last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_1026625200}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo igmp-snooping last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_756864461}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_697830284}

[**[igmp-snooping last-member-query-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_x1048551}

[**[undo igmp-snooping last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_x1615832656}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_489246119}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x619065460}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89324453}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x1983398116}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1846660525}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1014152302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_428540933}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x696175947}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_x190217362}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x808019432}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_x616625678}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_89258917}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1635883407}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_542345389}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1986428632}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="NL"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="NL"}

[\[Sysname-vlan2\] igmp-snooping last-member-query-interval 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x2011567766}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x2011633302}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="NL"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="NL"}

[\[Sysname-vsi-aaa\] igmp-snooping last-member-query-interval 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1732378458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x2011698838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x320226792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[last-member-query-interval]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x1155917961}
:::

::: {#483249982 .myid}
[]{#_Toc404789399}[]{#struct_0_x1820_12830_1091857206}[]{#_Toc354920948}[]{#_Toc293908691}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping leave source-ip**

------------------------------------------------------------------------

[**[igmp-snooping leave source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_x1392260032}[命令用来配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[离开组报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo igmp-snooping leave source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_1091791670}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_966190008}

[**[igmp-snooping leave source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1820_12830_x1039764812}

[**[undo igmp-snooping leave source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_1091726134}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1378139771}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_1091660598}[离开组报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则采用]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_980965490}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x646573124}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1092643638}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x701629801}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1152060182}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1092578102}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1820_12830_1252832050}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[离开组报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x841598250}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1092119349}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1081065697}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1112833475}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[离开组报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1092053813}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping leave source-ip 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1851000101}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x2011371159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_1091988277}
:::

::: {#-1116450163 .myid}
[]{#_Toc404789400}[]{#struct_0_x1820_12830_89455525}[]{#_Toc293908692}[]{#_Toc301367126}[]{#_Toc301427692}[]{#_Toc301367127}[]{#_Toc301427693}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping max-response-time**

------------------------------------------------------------------------

[**[igmp-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_1373719463}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间。]{style="font-family:宋体"}

[**[undo igmp-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x1716184263}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1122242167}

[**[igmp-snooping max-response-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1820_12830_x1284627384}

[**[undo igmp-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_602378156}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1358465517}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_2061753733}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_551789822}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_89389989}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1413720838}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x8321849}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1159057049}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1435096414}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_727017859}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_981235347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_1157023102}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免误删组播组成员，请确保]{style="font-family:宋体"}]{#struct_0_x1820_12830_1091857205}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间小于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x2011502228}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}[下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_88931234}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_850127847}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x657464691}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping max-response-time 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x2011567764}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x2011633300}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping max-response-time 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2106712027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x2011698836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x871995292}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_1091791669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-response-time]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1193828542}
:::

::: {#744886306 .myid}
[]{#_Toc404789401}[]{#struct_0_x1820_12830_x2065976623}[]{#_Toc293908693}[]{#_Toc301367129}[]{#_Toc301427695}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping overflow-replace**

------------------------------------------------------------------------

[**[igmp-snooping]{lang="DA"}[ overflow-replace]{lang="EN-US"}**]{#struct_0_x1820_12830_88865698}[命令用来在端口上使能组播组替换功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1820_12830_x1027196868}**[igmp-snooping]{lang="DA"}[ overflow-replace]{lang="EN-US"}**[命令用来在端口上关闭组播组替换功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1350789241}

[**[igmp-snooping overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_1364088049}

[**[undo igmp-snooping overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1582321928}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1333792545}

[[组播组替换功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1820_12830_742391284}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x428997515}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x885748445}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89062306}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1011356920}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1173361024}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1151860170}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_x1574886386}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1676862364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对动态组播组有效，对静态组播组无效。]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1575552003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[overflow-replace]{lang="EN-US"}**]{#struct_0_x1820_12830_x1397177516}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:
宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_583785373}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_88996770}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能组播组替换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x750469550}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping overflow-replace vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1262083382}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[overflow-replace]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1972634733}
:::

::: {#728833438 .myid}
[]{#_Toc404789402}[]{#struct_0_x1820_12830_1091660597}[]{#_Toc354920951}[]{#_Toc293908695}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping querier**

------------------------------------------------------------------------

[**[igmp-snooping querier]{lang="EN-US"}**]{#struct_0_x1820_12830_1092643637}[命令用来使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[igmp-snooping querier]{lang="EN-US"}**]{#struct_0_x1820_12830_x702612841}[命令用来关闭]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1092578101}

[**[igmp-snooping querier]{lang="EN-US"}**]{#struct_0_x1820_12830_1253028658}

[**[undo igmp-snooping querier]{lang="EN-US"}**]{#struct_0_x1820_12830_1845283308}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1092119348}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_x1081131233}[查询器处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1068833444}

[[VLAN]{lang="SV"}]{#struct_0_x1820_12830_1092053812}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1851065637}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1091988276}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x189287759}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_843424276}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_1091922740}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在组播]{style="font-family:宋体"}]{#struct_0_x1820_12830_208629332}[VLAN]{lang="EN-US"}[的子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内配置了本命令，只有当该子]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[被从组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中删除后，]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[查询器才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1091857204}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1392391104}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1091791668}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping querier]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x2010846869}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[查询器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x2010912405}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping querier]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_966714295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x2011371162}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_125721325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[subvlan]{lang="EN-US"}**[ (multicast-VLAN view)]{lang="EN-US"}]{#struct_0_x1820_12830_1091726132}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#1311972975 .myid}
[]{#_Toc404789403}[]{#struct_0_x1820_12830_x1378270843}[]{#_Toc354920952}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping query-interval**

------------------------------------------------------------------------

[**[igmp-snooping query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_x1201420993}[命令用来在]{style="font-family:
宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo igmp-snooping query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_1091660596}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_980310130}

[**[igmp-snooping query-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1820_12830_1092643636}

[**[undo igmp-snooping query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_x702547305}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1393708819}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_1092578100}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1252963122}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1092119347}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1080672481}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x255504137}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1092053811}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1851131173}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_1461770036}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1091988275}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_x189222223}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免误删组播组成员，请确保]{style="font-family:宋体"}]{#struct_0_x1820_12830_1091922739}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔大于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间，否则配置虽能生效但系统会给出提示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_208039503}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1544965802}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1091857203}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping query-interval 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x2010846874}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x2010912410}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping query-interval 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1392456640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x2011371163}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_1091791667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_966124471}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping querier]{lang="EN-US"}**]{#struct_0_x1820_12830_x1426504702}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_1091726131}
:::

::: {#-460834078 .myid}
[]{#_Toc404789404}[]{#struct_0_x1820_12830_x1378467451}[]{#_Toc354920953}[]{#_Toc293908697}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping report source-ip**

------------------------------------------------------------------------

[**[igmp-snooping report source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_1091660595}[命令用来配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo igmp-snooping report source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_980113522}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1876855000}

[**[igmp-snooping report source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1820_12830_1092643635}

[**[undo igmp-snooping report source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_x702481769}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1092578099}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x1085099205}[成员关系报告报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则采用]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x601051340}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x1636764003}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x896652908}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1636829539}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x96943747}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2053353082}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x1636895075}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1610374153}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_710727606}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636960611}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1536933792}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1637026147}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping report source-ip 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1936293118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x2011698843}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x1637091683}
:::

::: {#265301931 .myid}
[]{#_Toc404789405}[]{#struct_0_x1820_12830_458098478}[]{#_Toc293908698}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping router-aging-time**

------------------------------------------------------------------------

[**[igmp-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_715338633}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内配置动态路由器端口的老化时间。]{style="font-family:宋体"}

[**[undo igmp-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x899002489}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x228377597}

[**[igmp-snooping router-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1820_12830_x729904027}

[**[undo igmp-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_89193378}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1781306675}

[[动态路由器端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}]{#struct_0_x1820_12830_2021618934}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_737135736}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x850435543}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1505733510}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_268938988}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x942392808}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1064970167}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_89127842}[：表示动态路由器端口的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x953825126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_x1562661880}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x1870919511}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:
宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}[下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x825361011}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x589793901}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置动态路由器端口的老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_139120753}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping router-aging-time 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1880835899}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置动态路由器端口的老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1880770363}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping router-aging-time 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89324450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1880311610}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x409420004}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[router-aging-time]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1349906786}
:::

::: {#792071963 .myid}
[]{#_Toc404789406}[]{#struct_0_x1820_12830_x1637222755}[]{#_Toc354920955}[]{#_Toc293908699}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping router-port-deny**

------------------------------------------------------------------------

[**[igmp-snooping router-port-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_x1636239715}[命令用来禁止端口成为动态路由器端口。]{style="font-family:
宋体"}

[**[undo igmp-snooping router-port-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_1826925528}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636305251}

[**[igmp-snooping router-port-deny]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x1049536934}

[**[undo igmp-snooping router-port-deny]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_495315802}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636764004}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1299937435}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636829540}

[[允许端口成为动态路由器端口。]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1306469648}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_540166922}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1636895076}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_44290212}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x237332453}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_x1636960612}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果指定了本参数，只有当该端口属于指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，本配置才生效；如果未指定本参数，则本配置将对该端口所属的所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1176778231}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1637091684}[禁止端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内成为动态路由器端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x566368435}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping router-port-deny vlan 2]{lang="EN-US"}
:::

::::: {#1696259932 .myid}
[]{#_Toc293908702}[]{#_Toc404789407}[]{#struct_0_x1820_12830_x1191213291}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping source-deny**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP%20Snooping命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1820_12830_x1063104301}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1820_12830_980322155}
:::

[ ]{lang="EN-US"}

[**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_x2139441582}[命令用来使能当前端口的组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1820_12830_x1485316538}**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[source-deny]{lang="EN-US"}**[命令用来关闭当前端口的组播数据报文源端口过滤功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_321275336}

[**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_89258914}

[**[undo igmp-snooping source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_x702768753}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1377539679}

[[组播数据报文源端口过滤功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1820_12830_1198988012}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x164253009}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1484489101}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_665600347}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1733798331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1463895666}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89455522}

[[本命令与]{style="font-family:宋体"}**[source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_x964932697}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_980355816}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x983964095}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1372854212}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping source-deny]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1758067094}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source-deny]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1633158365}
:::::

::: {#-1387648976 .myid}
[]{#_Toc404789408}[]{#struct_0_x1820_12830_x1636239716}[]{#_Toc354920957}[]{#_Toc293908701}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping special-query source-ip**

------------------------------------------------------------------------

[**[igmp-snooping special-query source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_x2064757241}[命令用来配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo igmp-snooping special-query source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_1627188540}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636305252}

[**[igmp-snooping special-query source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1820_12830_516547007}

[**[undo igmp-snooping special-query source-ip]{lang="EN-US"}**]{#struct_0_x1820_12830_x1636764005}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_266146506}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1820_12830_x267284777}[VLAN]{lang="EN-US"}[内，如果收到过]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文，则以其源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；否则，采用当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；若当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口没有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则采用]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1820_12830_1880311612}[VSI]{lang="EN-US"}[内，如果收到过]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文，则以其源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；否则，采用]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636829541}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_259614293}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636895077}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1521793729}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_439926668}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1636960613}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x374134378}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1637026149}

[[在配置本命令之前，必须先在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_x1552105124}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1637091685}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x2132452376}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1637157221}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping special-query source-ip 10.1.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1879983932}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1879918396}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping special-query source-ip 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1095760572}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_1879852860}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x1249486765}
:::

::: {#82628605 .myid}
[]{#_Toc404789409}[]{#struct_0_x1820_12830_x1258047015}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping static-group**

------------------------------------------------------------------------

[**[igmp-snooping]{lang="DA"}[ static-group]{lang="EN-US"}**]{#struct_0_x1820_12830_89389986}[命令用来配置]{style="font-family:宋体"}[静态成员端口，即配置端口静态加入组播组或组播源组。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1820_12830_693676806}**[igmp-snooping]{lang="DA"}[ static-group]{lang="EN-US"}**[命令用来删除静态成员端口的配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1920244581}

[**[igmp-snooping]{lang="DA"}[ static-group]{lang="EN-US"}**[ *group-address* \[ **source-ip** *source-address* \] **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x1300209234}

[**[undo igmp-snooping static-group]{lang="EN-US"}**[ { *group-address* \[ **source-ip** *source-address* \] **vlan** *vlan-id* \| **all** }]{lang="EN-US"}]{#struct_0_x1820_12830_x2054322322}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x104207249}

[[端口不是静态成员端口。]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1005760883}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x270184287}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_1695077472}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_88931235}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1488524313}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1626190147}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1211546306}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1820_12830_974878223}[：表示静态加入的组播组地址，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-ip ]{lang="EN-US"}***[source-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x1877641117}[：表示静态加入的组播源地址。如果指定了本参数，表示加入组播源组；如果未指定本参数，则表示加入组播组。配置有本参数的静态成员端口，只在]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[版本]{style="font-family:宋体"}[3]{lang="EN-US"}[下生效。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x1304301173}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1820_12830_1879852855}[：]{style="font-family:宋体"}[表示对所有组播组和组播源组进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1311455292}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1171219065}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置为]{style="font-family:宋体"}[组播源组（]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.1]{lang="EN-US"}[）在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的静态成员端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_1689459672}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping version 3]{lang="EN-US"}

[\[Sysname-vlan2\] quit]{lang="EN-US"}

[\[Sysname\] interface Gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping static-group 225.0.0.1 source-ip 1.1.1.1 vlan 2]{lang="EN-US"}
:::

::: {#-1703652813 .myid}
[]{#_Toc404789410}[]{#struct_0_x1820_12830_1467827887}[]{#_Toc293908703}[]{#_Toc123030607}[]{#_Toc121110291}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping static-router-port**

------------------------------------------------------------------------

[**[igmp-snooping]{lang="DA"}[ static-router-port]{lang="EN-US"}**]{#struct_0_x1820_12830_x938376439}[命令用来配置静态路由器端口。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1820_12830_89062307}**[igmp-snooping]{lang="DA"}[ static-router-port]{lang="EN-US"}**[命令用来删除静态路由器端口的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x944958216}

[**[igmp-snooping]{lang="DA"}[ static-router-port vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1820_12830_x319637876}

[**[undo igmp-snooping static-router-port]{lang="EN-US"}**[ { **all** \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x1820_12830_x1751103621}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2024353081}

[[端口不是静态路由器端口。]{style="font-family:宋体"}]{#struct_0_x1820_12830_110911957}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1406680385}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1820_12830_x1625480272}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1937940870}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x422964233}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_88996771}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1205845586}

[**[all]{lang="EN-US"}**]{#struct_0_x1820_12830_x191862287}[：表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1820_12830_x1192346245}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x734327427}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1537574014}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置为]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的静态路由器端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x750435830}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp-snooping static-router-port vlan 2]{lang="EN-US"}
:::

::: {#381858590 .myid}
[]{#_Toc404789411}[]{#struct_0_x1820_12830_1551281028}[]{#_Toc293908704}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping version**

------------------------------------------------------------------------

[**[igmp-snooping version]{lang="EN-US"}**]{#struct_0_x1820_12830_89193379}[命令用来在]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[内配置]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的版本。]{style="font-family:宋体"}

[**[undo igmp-snooping version]{lang="EN-US"}**]{#struct_0_x1820_12830_175008461}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命]{style="font-family:黑体"}]{#struct_0_x1820_12830_392385189}[令]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[**[igmp-snooping version ]{lang="EN-US"}***[version-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1701551752}

[**[undo igmp-snooping version]{lang="EN-US"}**]{#struct_0_x1820_12830_x404580388}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1636823371}

[[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_2010482868}[内]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的版本为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1950412816}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x783700184}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89127843}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1384827034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1783944252}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_62343353}

[*[version-number]{lang="EN-US"}*]{#struct_0_x1820_12830_1801960815}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x806542652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}]{#struct_0_x1820_12830_730859538}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{style="font-family:宋体"}]{#struct_0_x1820_12830_x849030497}[VLAN]{lang="EN-US"}[的配置，]{style="font-family:宋体"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[version]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下可以对指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1098297136}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1515868679}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[版本为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_89324451}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vlan2\] igmp-snooping version 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x848571742}[在]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[内使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[版本为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x848637278}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping enable]{lang="EN-US"}

[\[Sysname-vsi-aaa\] igmp-snooping version 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1929232156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x848702814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_473963867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[version]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x848833886}
:::

::: {#-2124547157 .myid}
[]{#_Toc404789412}[]{#struct_0_x1820_12830_1987880374}[]{#_Toc293908705}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- last-member-query-interval (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_1178367599}[命令用来全局配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_x863077334}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x648654690}

[**[last-member-query-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_692076332}

[**[undo last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_89258915}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1253546383}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x820090668}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1456209806}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_x432465382}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1870554220}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1395588795}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1580027077}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_123069437}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_89455523}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[，单位为秒。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_991382439}

[[本命令与]{style="font-family:宋体"}**[igmp-snooping last-member-query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_1708062232}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1346553162}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_1978518472}[全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文的发送间隔为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_479891335}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] last-member-query-interval 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2135483532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping]{lang="EN-US"}**[ **last-member-query-interval**]{lang="EN-US"}]{#struct_0_x1820_12830_x1571521092}
:::

::: {#-204830081 .myid}
[]{#_Toc404789413}[]{#struct_0_x1820_12830_89389987}[]{#_Toc293908706}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- max-response-time (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x1262638330}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间。]{style="font-family:宋体"}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_1559912432}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x49661260}

[**[max-response-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1820_12830_x481149647}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_211358758}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1559990950}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_1984759008}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_902645460}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_88931232}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x296883225}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_446875866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1772053928}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1444309143}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_x1971572583}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1370637719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免误删组播组成员，请确保]{style="font-family:宋体"}]{#struct_0_x1820_12830_x1636239718}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间小于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[igmp-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x848964964}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图]{style="font-family:宋体"}[下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[/VSI]{lang="EN-US"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_911485424}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1281362395}[全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_88865696}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] max-response-time 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1649162300}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping max-response-time]{lang="EN-US"}**]{#struct_0_x1820_12830_1835948672}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping query-interval]{lang="EN-US"}**]{#struct_0_x1820_12830_x1636305254}
:::

::: {#1208320838 .myid}
[]{#_Toc404789414}[]{#struct_0_x1820_12830_x507201329}[]{#_Toc293908707}[]{#_Toc301367137}[]{#_Toc301427703}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- overflow-replace (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[overflow-replace]{lang="EN-US"}**]{#struct_0_x1820_12830_555115864}[命令用来全局使能组播组替换功能。]{style="font-family:宋体"}

[**[undo overflow-replace]{lang="EN-US"}**]{#struct_0_x1820_12830_459847873}[命令用来全局关闭组播组替换功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_767008598}

[**[overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_x131106471}

[**[undo overflow-replace]{lang="EN-US"}**[ \[ **vlan** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1820_12830_89062304}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_629019896}

[[组播组替换功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1820_12830_x690186767}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_920194773}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1254727851}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1434252408}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1635123565}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1436717962}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2090223889}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_88996768}[：]{style="font-family:
宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，则表示对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x787205395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对动态组播组有效，对静态组播组无效。]{style="font-family:宋体"}]{#struct_0_x1820_12830_996444999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[igmp-snooping overflow-replace]{lang="EN-US"}**]{#struct_0_x1820_12830_x1689698134}[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:
宋体"}[都有效，]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[视图下的配置只对当前]{lang="EN-US" style="font-family:宋体"}[端口]{style="font-family:宋体"}[有效，后者的配置优先级较高]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1173022610}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1991958980}[全局使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的组播组替换功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x28015843}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] overflow-replace vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_735485838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping overflow-replace]{lang="EN-US"}**]{#struct_0_x1820_12830_89193376}
:::

::: {#-1792376404 .myid}
[]{#_Toc293908709}[]{#_Toc404789415}[]{#struct_0_x1820_12830_601975501}[]{#_Toc293908708}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- report-aggregation (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[report-aggregation]{lang="EN-US"}**]{#struct_0_x1820_12830_x1763949463}[命令用来使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文抑制功能。]{style="font-family:宋体"}

[**[undo report-aggregation]{lang="EN-US"}**]{#struct_0_x1820_12830_x247949771}[命令用来关闭]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文抑制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x74765535}

[**[report-aggregation]{lang="EN-US"}**]{#struct_0_x1820_12830_1802548163}

[**[undo report-aggregation]{lang="EN-US"}**]{#struct_0_x1820_12830_x1389049831}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_64031488}

[[IGMP]{lang="EN-US"}]{#struct_0_x1820_12830_x1077626849}[成员关系报告报文抑制功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1232462634}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_89127840}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1336162150}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x133519825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1704989359}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_115424312}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1045182592}[关闭]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_406964103}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] undo report-aggregation]{lang="EN-US"}
:::

::: {#558726975 .myid}
[]{#_Toc404789416}[]{#struct_0_x1820_12830_x784878547}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- reset igmp-snooping group**

------------------------------------------------------------------------

[**[reset ]{lang="EN-US"}**]{#struct_0_x1820_12830_89324448}**[igmp-snooping]{lang="DA"}[ group]{lang="EN-US"}**[命令用来清除动态]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_790115255}

[**[reset igmp-snooping group]{lang="EN-US"}**[ { *group-address* \[ *source-address* \] \| **all** } \[ **vlan** *vlan-id* \| **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x1820_12830_545399052}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x632089852}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_685249000}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_979699464}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1627239923}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1675389705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1603707275}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1820_12830_89258912}[：清除指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x1820_12830_x1085105777}[：清除指定组播源的信息。如果未指定本参数，将清除所有组播源的信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1820_12830_x579780442}[：清除所有组播组的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_x1820_12830_813302437}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_1517789795}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_567761979}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_x1206121650}[清除所有动态]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[转发表的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ]{lang="EN-US"}]{#struct_0_x1820_12830_x1530151549}[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[group all]{lang="EN-US"}

[]{#_Toc293908710}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x93457721}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display igmp-snooping group]{lang="EN-US"}**]{#struct_0_x1820_12830_1315013796}
:::

::: {#433399686 .myid}
[]{#_Toc404789417}[]{#struct_0_x1820_12830_89455520}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- reset igmp-snooping router-port**

------------------------------------------------------------------------

[**[reset ]{lang="EN-US"}**]{#struct_0_x1820_12830_x1347269721}**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[router-port]{lang="EN-US"}**[命令用来清除动态路由器端口的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x875160917}

[**[reset igmp-snooping router-port]{lang="EN-US"}**[ { **all** \| **vlan** *vlan-id* \| **vsi** *vsi-name* }]{lang="EN-US"}]{#struct_0_x1820_12830_2142437885}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_952168650}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_x530618353}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x2007791695}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_1528016758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_101403310}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89389984}

[**[all]{lang="EN-US"}**]{#struct_0_x1820_12830_1076013830}[：清除所有动态路由器端口的信息。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_x1820_12830_1912383907}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1820_12830_1517593186}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1752914057}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_547746163}[清除所有动态路由器端口的信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ]{lang="EN-US"}]{#struct_0_x1820_12830_1633660909}[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[router-port all]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1539118296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display igmp-snooping router-port]{lang="EN-US"}**]{#struct_0_x1820_12830_x1396524598}
:::

::: {#-508772165 .myid}
[]{#_Toc404789418}[]{#struct_0_x1820_12830_x2039537337}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- reset igmp-snooping statistics**

------------------------------------------------------------------------

[**[reset igmp-snooping statistics]{lang="EN-US"}**]{#struct_0_x1820_12830_88931233}[命令用来清除]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1659431911}

[**[reset igmp-snooping statistics]{lang="EN-US"}**]{#struct_0_x1820_12830_x1584746510}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1393974095}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1820_12830_1104182603}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1017496939}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x362423019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1884193004}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1521216562}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_88865697}[清除]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[监听到的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset igmp-snooping statistics]{lang="EN-US"}]{#struct_0_x1820_12830_x307152836}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1058342824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display igmp-snooping statistics]{lang="EN-US"}**]{#struct_0_x1820_12830_1952922624}
:::

::: {#1158905413 .myid}
[]{#_Toc404789419}[]{#struct_0_x1820_12830_x793757006}[]{#_Toc293908711}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- router-aging-time (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_2147130082}[命令用来全局配置动态路由器端口的老化时间。]{style="font-family:宋体"}

[**[undo router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_265303804}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1177009507}

[**[router-aging-time]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1820_12830_89062305}

[**[undo router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x1327295240}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1487541414}

[[动态路由器端口的老化时间为]{style="font-family:宋体"}[260]{lang="EN-US"}]{#struct_0_x1820_12830_988801899}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1167200215}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_x1880697625}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_492855271}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1088878539}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x1963151994}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_88996769}

[*[interval]{lang="EN-US"}*]{#struct_0_x1820_12830_1169109741}[：表示动态路由器端口的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_234955636}

[[本命令与]{style="font-family:宋体"}**[igmp-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_x423593000}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下的全局配置对所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VLAN/VSI]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x484090102}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_283329542}[全局配置动态路由器端口的老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_2051195215}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] router-aging-time 100]{lang="EN-US"}[]{#_Toc138647989}[]{#_Toc138648274}[]{#_Toc138648543}[]{#_Toc138647990}[]{#_Toc138648275}[]{#_Toc138648544}[]{#_Toc138647993}[]{#_Toc138648278}[]{#_Toc138648547}[]{#_Toc134006615}[]{#_Toc138647998}[]{#_Toc138648283}[]{#_Toc138648552}[]{#_Toc135732953}[]{#_Toc136006430}[]{#_Toc136009014}[]{#_Toc136009484}[]{#_Toc136009706}[]{#_Toc136659547}[]{#_Toc134006634}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_581161255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping router-aging-time]{lang="EN-US"}**]{#struct_0_x1820_12830_2072120244}
:::

::::: {#1980124287 .myid}
[]{#_Toc404789420}[]{#struct_0_x1820_12830_89193377}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- source-deny (IGMP-Snooping view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP%20Snooping命令.files/image002.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1820_12830_x1736676659}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1820_12830_238599960}
:::

[ ]{lang="EN-US"}

[**[source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_x2117060245}[命令用来使能指定端口的组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[**[undo source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_347012688}[命令用来关闭指定端口的组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1577641984}

[**[source-deny port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x1820_12830_1769324593}

[**[undo source-deny port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x1820_12830_x627104175}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_89127841}

[[组播数据报文源端口过滤功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1820_12830_1002490010}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x297000091}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_462300472}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x194294670}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_2027812840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_x845279343}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1829120539}

[**[port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x1820_12830_x1254083648}[：表示对指定端口进行配置。]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[为端口列表，表示一或多个端口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type* *interface-number* \[ **to** *interface-type* *interface-number* \] }]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1290256570}

[[本命令与]{style="font-family:宋体"}**[igmp-snooping source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_89324449}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x1166199881}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_100396875}[使能端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[～]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[上的组播数据报文源端口过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_x1109866592}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] source-deny port gigabitethernet 1/0/1 to gigabitethernet 1/0/4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1367187644}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping]{lang="DA"}[ ]{lang="DA"}[source-deny]{lang="EN-US"}**]{#struct_0_x1820_12830_600671214}
:::::

::: {#-618713921 .myid}
[]{#_Toc404789421}[]{#struct_0_x1820_12830_1432755236}[]{#_Toc345425154}

**IGMP Snooping \-- IGMP Snooping配置命令 \-- version (IGMP-Snooping view)**

------------------------------------------------------------------------

[**[version]{lang="EN-US"}**]{#struct_0_x1820_12830_87805366}[命令用来配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的版本。]{style="font-family:宋体"}

[**[undo version]{lang="EN-US"}**]{#struct_0_x1820_12830_89258913}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命]{style="font-family:黑体"}]{#struct_0_x1820_12830_871209359}[令]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[**[version ]{lang="EN-US"}***[version-number]{lang="EN-US"}*[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x1820_12830_x1917402909}

[**[undo version]{lang="EN-US"}**[ **vlan** *vlan-list*]{lang="EN-US"}]{#struct_0_x1820_12830_268498373}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1820_12830_2087777547}

[[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_74172583}[内]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的版本为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x429680264}

[[IGMP-Snooping]{lang="EN-US"}]{#struct_0_x1820_12830_1430651292}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1381212229}

[[network-admin]{lang="EN-US"}]{#struct_0_x1820_12830_89455521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1820_12830_609045415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x622588651}

[*[version-number]{lang="EN-US"}*]{#struct_0_x1820_12830_x1037982189}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1820_12830_293455132}[：]{style="font-family:宋体"}[表示对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1820_12830_517182496}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先在]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_x1055460091}[内使能]{lang="EN-US" style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于基于]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1820_12830_1517593183}[的配置，本命令与]{lang="EN-US" style="font-family:宋体"}**[igmp-snooping]{lang="EN-US"}[ version]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{lang="EN-US" style="font-family:宋体"}[IGMP-Snooping]{lang="EN-US"}[视图下可以对指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下只能对当前]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行配置，二者的配置优先级相同]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1820_12830_1087477664}

[[\# ]{lang="EN-US"}]{#struct_0_x1820_12830_2030556349}[使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，并配置这些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[版本为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1820_12830_89389985}

[\[Sysname\] igmp-snooping]{lang="EN-US"}

[\[Sysname-igmp-snooping\] enable vlan 2 to 10]{lang="EN-US"}

[\[Sysname-igmp-snooping\] version 3 vlan 2 to 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1820_12830_x880301306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable]{lang="EN-US"}**[ (IGMP-Snooping view)]{lang="EN-US"}]{#struct_0_x1820_12830_x1400391388}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping enable]{lang="EN-US"}**]{#struct_0_x1820_12830_x1460323545}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp-snooping]{lang="EN-US"}**]{#struct_0_x1820_12830_1517658719}**[ version]{lang="EN-US"}**

[ ]{lang="EN-US"}
:::
