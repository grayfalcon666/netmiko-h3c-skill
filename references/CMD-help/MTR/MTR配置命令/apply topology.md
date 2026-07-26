::: {#-1557595323 .myid}
[]{#_Toc252801287}[]{#_Toc140491850}[]{#_Toc140491148}[]{#_Toc304794689}[]{#_Toc355342002}[]{#_Toc354060903}[]{#_Toc404789179}[]{#struct_0_29682_x5097_244984833}[]{#_Toc357171231}[]{#_Toc354060901}

**MTR \-- MTR配置命令 \-- apply topology**

------------------------------------------------------------------------

[**[apply topology]{lang="EN-US"}**]{#struct_0_29682_x5097_x804725976}[命令用来配置多拓扑转发策略节点应用的拓扑。]{style="font-family:宋体"}

[**[undo apply topology]{lang="EN-US"}**]{#struct_0_29682_x5097_2050439307}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x228636335}

[**[apply topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_29682_x5097_1226512481}

[**[undo apply topology]{lang="EN-US"}**]{#struct_0_29682_x5097_1758338171}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x653538804}

[[没有配置]{style="font-family:宋体"}]{#struct_0_29682_x5097_x353134783}[多拓扑转发策略节点应用的拓扑]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_895557522}

[[多拓扑策略节点视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_1418590032}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1855259777}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1734599630}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1605614411}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x887460368}

[*[topo-name]{lang="EN-US"}*]{#struct_0_29682_x5097_1359168752}[：拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x333788721}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_x441874544}[配置多拓扑转发策略]{style="font-family:宋体"}[mtr]{lang="EN-US"}[的节点]{style="font-family:宋体"}[0]{lang="EN-US"}[应用拓扑]{style="font-family:宋体"}[topo1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_x1742979230}

[\[Sysname\] mtr-policy mtr node 0]{lang="EN-US"}

[\[Sysname-mtr-policy-mtr-0\] apply topology topo1]{lang="EN-US"}
:::

::: {#659946018 .myid}
[]{#_Toc404789180}[]{#struct_0_29682_x5097_x353923597}

**MTR \-- MTR配置命令 \-- display mtr-policy**

------------------------------------------------------------------------

[**[display mtr-policy]{lang="EN-US"}**]{#struct_0_29682_x5097_x282225370}[命令显示多拓扑转发策略信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1323666248}

[**[display mtr-policy]{lang="EN-US"}**[ \[ **name** *mtr-policy-name* \]]{lang="EN-US"}]{#struct_0_29682_x5097_x1669838236}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_899662530}

[[任意视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_1734665166}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1933233611}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_636193271}

[[network-operator]{lang="EN-US"}]{#struct_0_29682_x5097_1766203427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x865750564}

[[mdc-operator]{lang="EN-US"}]{#struct_0_29682_x5097_x1153425051}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_167941847}

[**[name ]{lang="EN-US"}***[mtr-policy-name]{lang="EN-US"}*]{#struct_0_29682_x5097_546869161}[：多拓扑转发策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1287108648}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_1949618815}[显示所有的多拓扑转发策略。]{style="font-family:宋体"}

[]{#_Toc350333359}[]{#_Toc357171225}[[\<Sysname\> display mtr-policy]{lang="EN-US"}]{#struct_0_29682_x5097_1734992846}

[MTR-policy: mtr]{lang="EN-US"}

[  Node: 0]{lang="EN-US"}

[        if-match ip precedence critical]{lang="EN-US"}

[        if-match ip acl 3333]{lang="EN-US"}

[        apply topology 1]{lang="EN-US"}

[MTR-policy: p]{lang="EN-US"}

[  Node: 1]{lang="EN-US"}

[        if-match ip precedence routine]{lang="EN-US"}

[        if-match ip dscp cs1]{lang="EN-US"}

[        if-match ip acl 3501]{lang="EN-US"}

[MTR-policy: q]{lang="EN-US"}

[  Node: 0]{lang="EN-US"}

[        if-match ip precedence network]{lang="EN-US"}

[        if-match ip dscp ef]{lang="EN-US"}

[        if-match ip acl 3001]{lang="EN-US"}

[        apply topology 1]{lang="EN-US"}

[  Node: 1]{lang="EN-US"}

[MTR-policy: w]{lang="EN-US"}

[  Node: 0]{lang="EN-US"}

[        if-match ip precedence routine]{lang="EN-US"}

[        if-match ip dscp 3]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mtr-policy]{lang="EN-US"}]{#struct_0_29682_x5097_18283821}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x487201145}[[字段]{style="font-family:黑体"}]{#struct_0_29682_x5097_x606597796}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1400549606}

[[MTR-policy]{lang="EN-US"}]{#struct_0_29682_x5097_1735058382}

[[多拓扑策略名称]{style="font-family:宋体"}]{#struct_0_29682_x5097_x455362070}

[[Node]{lang="EN-US"}]{#struct_0_29682_x5097_69470457}

[[多拓扑策略节点]{style="font-family:宋体"}]{#struct_0_29682_x5097_1295963491}

[ ]{lang="EN-US"}

::: {#660792264 .myid}
[]{#_Toc404789181}[]{#struct_0_29682_x5097_1358166462}

**MTR \-- MTR配置命令 \-- display topology**

------------------------------------------------------------------------

[**[display topology]{lang="EN-US"}**]{#struct_0_29682_x5097_1288857938}[命令用来显示多拓扑实例的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1867918276}

[**[display topology ]{lang="EN-US"}**[\[ **name** *topo-name* \]]{lang="EN-US"}]{#struct_0_29682_x5097_321435540}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1503091219}

[[任意视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_x1959487355}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1086264310}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1734468557}

[[network-operator]{lang="EN-US"}]{#struct_0_29682_x5097_x481248917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1708220561}

[[mdc-operator]{lang="EN-US"}]{#struct_0_29682_x5097_x29534112}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x589778645}

[**[name]{lang="EN-US"}***[ topo-name]{lang="EN-US"}*]{#struct_0_29682_x5097_1953738759}[：显示指定拓扑详细信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有拓扑的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x61945459}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_1745659153}[显示所有拓扑的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display topology]{lang="EN-US"}]{#struct_0_29682_x5097_1734534093}

[  Total topologies : 4]{lang="EN-US"}

[  Topology                        Address-family         VRF]{lang="EN-US"}

[  base                            IPv4                   default]{lang="EN-US"}

[  mt1                             IPv4                   default]{lang="EN-US"}

[  mt2                             IPv4                   default]{lang="EN-US"}

[  mt3                             IPv4                   default]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_762778977}[显示拓扑]{style="font-family:宋体"}[mt1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display topology name mt1]{lang="EN-US"}]{#struct_0_29682_x5097_x89640188}

[Topology Name and Index: mt1, 1]{lang="EN-US"}

[Address-family: IPv4]{lang="EN-US"}

[Interfaces: LoopBack0, Vlan-interface1000,]{lang="EN-US"}

[            Vlan-interface1001, Vlan-interface1002,]{lang="EN-US"}

[            Vlan-interface1003]{lang="EN-US"}

[Maximum routes limit : 100]{lang="EN-US"}

[Threshold value(%): 90]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display topology]{lang="EN-US"}]{#struct_0_29682_x5097_356430226}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x494561529}[[字段]{style="font-family:黑体"}]{#struct_0_29682_x5097_x574802916}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_29682_x5097_1734403021}

[[Total topologies]{lang="EN-US"}]{#struct_0_29682_x5097_x1696272928}

[[已配置的拓扑数量]{style="font-family:宋体"}]{#struct_0_29682_x5097_1368013587}

[[Topology]{lang="EN-US"}]{#struct_0_29682_x5097_820359573}

[[拓扑名]{style="font-family:宋体"}]{#struct_0_29682_x5097_x851475402}

[[Address-family]{lang="EN-US"}]{#struct_0_29682_x5097_x130188987}

[[拓扑所在地址族]{style="font-family:宋体"}]{#struct_0_29682_x5097_1414825696}

[[VRF]{lang="EN-US"}]{#struct_0_29682_x5097_983196149}

[[所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_29682_x5097_x1747730582}

[[Topology Name and Index ]{lang="EN-US"}]{#struct_0_29682_x5097_x1192261325}

[[拓扑名和索引号]{style="font-family:宋体"}]{#struct_0_29682_x5097_x579666554}

[[Interfaces]{lang="EN-US"}]{#struct_0_29682_x5097_x2022174137}

[[拓扑关联的接口]{style="font-family:宋体"}]{#struct_0_29682_x5097_520031454}

[[Maximum routes limit]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_29682_x5097_x1084562055}

[[拓扑的]{style="font-family:宋体"}]{#struct_0_29682_x5097_1734730701}[路由最大路由前缀数]{style="font-size:10.0pt;
  font-family:宋体"}

[[Threshold value(%)]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_29682_x5097_x1210968903}

[[拓扑的路由告警门限值]{style="font-family:宋体"}]{#struct_0_29682_x5097_x1241640703}

[ ]{lang="EN-US"}

::: {#-1289886525 .myid}
[]{#_Toc357171232}[]{#_Toc357171222}[]{#_Toc357171227}[]{#_Toc354060897}[]{#_Toc404789182}[]{#struct_0_29682_x5097_349449988}[]{#_Toc357171221}

**MTR \-- MTR配置命令 \-- global-address-family ipv4**

------------------------------------------------------------------------

[**[global-address-family ipv4]{lang="EN-US"}**]{#struct_0_29682_x5097_x1069926604}[命令用]{style="font-family:
宋体"}[来]{style="font-family:宋体"}[进入全局地址族视图。]{style="font-family:
宋体"}

[**[undo global-address-family ipv4]{lang="EN-US"}**]{#struct_0_29682_x5097_218050859}[命令用来删除全局地址族视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1281374669}

[**[global-address-family ipv4]{lang="EN-US"}**[ \[ **unicast** \]]{lang="EN-US"}]{#struct_0_29682_x5097_209315064}

[**[undo global-address-family ipv4 ]{lang="EN-US"}**[\[ **unicast** \]]{lang="EN-US"}]{#struct_0_29682_x5097_x1292988401}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_442256327}

[[没有配置全局地址族视图。]{style="font-family:宋体"}]{#struct_0_29682_x5097_x865239850}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1734796237}

[[系统视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_x1160369280}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x473224483}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x531114943}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1139994721}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1376939632}

[**[unicast]{lang="EN-US"}**]{#struct_0_29682_x5097_x1164873656}[：表示进入]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播视图。如果未指定本参数，也进入]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播视图。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_29682_x5097_357893676}

[[如果要配置一个多拓扑，首先要通过该命令进入全局地址族视图。]{style="font-family:宋体"}]{#struct_0_29682_x5097_1201792793}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_487602764}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_x1179293945}[进入全局地址族视图。]{style="font-family:宋体"}

[]{#struct_0_29682_x5097_1734599629}[]{#_Hlt535131393}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] global-address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-global-ipv4\]]{lang="EN-US"}
:::

::: {#927839575 .myid}
[]{#_Toc404789183}[]{#struct_0_29682_x5097_x1606204234}[]{#_Toc357171230}[]{#_Toc354060900}

**MTR \-- MTR配置命令 \-- if-match ip acl**

------------------------------------------------------------------------

[**[if-match ip acl]{lang="EN-US"}**]{#struct_0_29682_x5097_304323937}[命令用来配置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的匹配条件。]{style="font-family:宋体"}

[**[undo if-match ip acl]{lang="EN-US"}**]{#struct_0_29682_x5097_300504194}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x376795137}

[**[if-match ip acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_29682_x5097_x2019270538}

[**[undo if-match ip acl]{lang="EN-US"}**]{#struct_0_29682_x5097_1862744270}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_982700135}

[[没有]{style="font-family:宋体"}]{#struct_0_29682_x5097_1266075142}[配置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的匹配条件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_2072192478}

[[多拓扑策略节点视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_558633300}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x413011467}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x440967908}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1341994324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1556069999}

[*[acl-number]{lang="EN-US"}*]{#struct_0_29682_x5097_1734665165}[：配置的作为匹配条件的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1933430219}

[[匹配原则：多个匹配条件（]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_29682_x5097_1438127254}[、]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级可以同时配置]{style="font-family:宋体"}[）之间是"或"的关系，即该节点的匹配条件任何一个满足，则该多拓扑转发策略节点匹配通过，该多拓扑转发策略也匹配通过。反之，该策略节点匹配失败，继续匹配其它节点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1608496944}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_1146096791}[创建一个名为]{style="font-family:宋体"}[mtr]{lang="EN-US"}[的多拓扑策略，其节点序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许]{style="font-family:宋体"}[ACL 3333]{lang="EN-US"}[的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_x542996437}

[\[Sysname\] mtr-policy mtr node 0]{lang="EN-US"}

[\[Sysname-mtr-policy-mtr-0\] if-match ip acl 3333]{lang="EN-US"}
:::

::: {#608583865 .myid}
[]{#_Toc404789184}[]{#struct_0_29682_x5097_x1317448175}[]{#_Toc357171229}[]{#_Toc354060899}

**MTR \-- MTR配置命令 \-- if-match ip dscp**

------------------------------------------------------------------------

[**[if-match ]{lang="EN-US"}[ip dscp]{lang="EN-US"}**]{#struct_0_29682_x5097_1105803339}[命令用来配置]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的匹配条件。]{style="font-family:宋体"}

[**[undo if-match ]{lang="EN-US"}[ip dscp]{lang="EN-US"}**]{#struct_0_29682_x5097_173649480}[命令用来]{style="font-family:宋体"}[取消该配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1093550634}

[**[if-match ip dscp]{lang="EN-US"}**[ *dscp-value*]{lang="EN-US"}]{#struct_0_29682_x5097_441473033}

[**[undo if-match ip dscp]{lang="EN-US"}**]{#struct_0_29682_x5097_1734992845}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_18349357}

[[没有]{style="font-family:宋体"}]{#struct_0_29682_x5097_x1709064624}[配置]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的匹配条件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x486436835}

[[多拓扑策略节点视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_x2141442527}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x447929243}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1404687582}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1156669648}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x707557589}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_29682_x5097_1178750747}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?608583865#_Ref378259523)[所示。]{style="font-family:宋体"}

[]{#struct_0_29682_x5097_982896742}[[表1-3 ]{lang="EN-US"}[DSCP]{lang="EN-US"}]{#_Ref378259523}[关键字与值的对应表]{style="font-family:黑体"}

[]{#table_struct_0_1313321858}[[关键字]{style="font-family:黑体"}]{#struct_0_29682_x5097_982831206}
:::

[[DSCP]{lang="EN-US"}]{#struct_0_29682_x5097_x2057749697}[值（二进制）]{style="font-family:黑体"}

[[DSCP]{lang="EN-US"}]{#struct_0_29682_x5097_x1053716212}[值（十进制）]{style="font-family:黑体"}

[[default]{lang="EN-US"}]{#struct_0_29682_x5097_983027814}

[[000000]{lang="EN-US"}]{#struct_0_29682_x5097_x636102719}

[[0]{lang="EN-US"}]{#struct_0_29682_x5097_1205259076}

[[af11]{lang="EN-US"}]{#struct_0_29682_x5097_982962278}

[[001010]{lang="EN-US"}]{#struct_0_29682_x5097_293747316}

[[10]{lang="EN-US"}]{#struct_0_29682_x5097_982634598}

[[af12]{lang="EN-US"}]{#struct_0_29682_x5097_1678111810}

[[001100]{lang="EN-US"}]{#struct_0_29682_x5097_x316817333}

[[12]{lang="EN-US"}]{#struct_0_29682_x5097_982569062}

[[af13]{lang="EN-US"}]{#struct_0_29682_x5097_x2138091196}

[[001110]{lang="EN-US"}]{#struct_0_29682_x5097_982765670}

[[14]{lang="EN-US"}]{#struct_0_29682_x5097_898197520}

[[af21]{lang="EN-US"}]{#struct_0_29682_x5097_x77997783}

[[010010]{lang="EN-US"}]{#struct_0_29682_x5097_982700134}

[[18]{lang="EN-US"}]{#struct_0_29682_x5097_1266075143}

[[af22]{lang="EN-US"}]{#struct_0_29682_x5097_983421030}

[[010100]{lang="EN-US"}]{#struct_0_29682_x5097_x826133787}

[[20]{lang="EN-US"}]{#struct_0_29682_x5097_x739352930}

[[af23]{lang="EN-US"}]{#struct_0_29682_x5097_983355494}

[[010110]{lang="EN-US"}]{#struct_0_29682_x5097_121462832}

[[22]{lang="EN-US"}]{#struct_0_29682_x5097_982896741}

[[af31]{lang="EN-US"}]{#struct_0_29682_x5097_1860689463}

[[011010]{lang="EN-US"}]{#struct_0_29682_x5097_982831205}

[[26]{lang="EN-US"}]{#struct_0_29682_x5097_x2057749698}

[[af32]{lang="EN-US"}]{#struct_0_29682_x5097_x1006662045}

[[011100]{lang="EN-US"}]{#struct_0_29682_x5097_983027813}

[[28]{lang="EN-US"}]{#struct_0_29682_x5097_x636102726}

[[af33]{lang="EN-US"}]{#struct_0_29682_x5097_982962277}

[[011110]{lang="EN-US"}]{#struct_0_29682_x5097_293747317}

[[30]{lang="EN-US"}]{#struct_0_29682_x5097_982634597}

[[af41]{lang="EN-US"}]{#struct_0_29682_x5097_1678111801}

[[100010]{lang="EN-US"}]{#struct_0_29682_x5097_x316751796}

[[34]{lang="EN-US"}]{#struct_0_29682_x5097_982569061}

[[af42]{lang="EN-US"}]{#struct_0_29682_x5097_x2138091195}

[[100100]{lang="EN-US"}]{#struct_0_29682_x5097_982765669}

[[36]{lang="EN-US"}]{#struct_0_29682_x5097_x1058117625}

[[af43]{lang="EN-US"}]{#struct_0_29682_x5097_982700133}

[[100110]{lang="EN-US"}]{#struct_0_29682_x5097_1266075140}

[[38]{lang="EN-US"}]{#struct_0_29682_x5097_983421029}

[[cs1]{lang="EN-US"}]{#struct_0_29682_x5097_1130181356}

[[001000]{lang="EN-US"}]{#struct_0_29682_x5097_983355493}

[[8]{lang="EN-US"}]{#struct_0_29682_x5097_121462835}

[[cs2]{lang="EN-US"}]{#struct_0_29682_x5097_982896748}

[[010000]{lang="EN-US"}]{#struct_0_29682_x5097_1860689454}

[[16]{lang="EN-US"}]{#struct_0_29682_x5097_728572744}

[[cs3]{lang="EN-US"}]{#struct_0_29682_x5097_982831212}

[[011000]{lang="EN-US"}]{#struct_0_29682_x5097_280902467}

[[24]{lang="EN-US"}]{#struct_0_29682_x5097_983027820}

[[cs4]{lang="EN-US"}]{#struct_0_29682_x5097_937875389}

[[100000]{lang="EN-US"}]{#struct_0_29682_x5097_982962284}

[[32]{lang="EN-US"}]{#struct_0_29682_x5097_249117304}

[[cs5]{lang="EN-US"}]{#struct_0_29682_x5097_982634604}

[[101000]{lang="EN-US"}]{#struct_0_29682_x5097_x697276207}

[[40]{lang="EN-US"}]{#struct_0_29682_x5097_982569068}

[[cs6]{lang="EN-US"}]{#struct_0_29682_x5097_x2138091202}

[[110000]{lang="EN-US"}]{#struct_0_29682_x5097_982765676}

[[48]{lang="EN-US"}]{#struct_0_29682_x5097_898197514}

[[cs7]{lang="EN-US"}]{#struct_0_29682_x5097_982700140}

[[111000]{lang="EN-US"}]{#struct_0_29682_x5097_x1072577021}

[[56]{lang="EN-US"}]{#struct_0_29682_x5097_983421036}

[[ef]{lang="EN-US"}]{#struct_0_29682_x5097_x826133785}

[[101110]{lang="EN-US"}]{#struct_0_29682_x5097_983355500}

[[46]{lang="EN-US"}]{#struct_0_29682_x5097_1260579737}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x2015349590}

[[匹配原则：多个匹配条件（]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_29682_x5097_1735058381}[、]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级可以同时配置]{style="font-family:宋体"}[）之间是"或"的关系，即该节点的匹配条件任何一个满足，则该多拓扑转发策略节点匹配通过，该多拓扑转发策略也匹配通过。反之，该策略节点匹配失败，继续匹配其它节点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x455296534}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_441464386}[创建一个名为]{style="font-family:宋体"}[mtr]{lang="EN-US"}[的多拓扑策略，其节点序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值为]{style="font-family:宋体"}[5]{lang="EN-US"}[的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_x111963371}

[\[Sysname\] mtr-policy mtr node 0]{lang="EN-US"}

[\[Sysname-mtr-policy-mtr-0\] if-match ip dscp 5]{lang="EN-US"}

::: {#-669817772 .myid}
[]{#_Toc404789185}[]{#struct_0_29682_x5097_x224561876}[]{#_Toc357171228}[]{#_Toc354060898}

**MTR \-- MTR配置命令 \-- if-match ip precedence**

------------------------------------------------------------------------

[**[if-match ip precedence]{lang="EN-US"}**]{#struct_0_29682_x5097_759854551}[命令用来配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级]{style="font-family:宋体"}[的匹配条件。]{style="font-family:宋体"}

[**[undo if-match ip precedence]{lang="EN-US"}**]{#struct_0_29682_x5097_1100127347}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_802062752}

[**[if-match ip precedence]{lang="EN-US"}**[ *prec-value*]{lang="EN-US"}]{#struct_0_29682_x5097_x1990141810}

[**[undo if-match]{lang="EN-US"}**[ **ip precedence**]{lang="EN-US"}]{#struct_0_29682_x5097_x392580746}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_872424970}

[[没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_29682_x5097_1734468556}[优先级的]{style="font-family:宋体"}[匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x481314453}

[[多拓扑策略节点视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_x228583686}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1136304366}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_318434251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x31685286}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1479480855}

[*[prec-value]{lang="EN-US"}*]{#struct_0_29682_x5097_1338339846}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](#_0_29682_x5097_983027819)[所示。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[IP]{lang="EN-US"}]{#struct_0_29682_x5097_983027819}[优先级关键字与值的对应表]{style="font-family:
黑体"}

[]{#table_struct_0_1099773510}[[关键字]{style="font-family:黑体"}]{#struct_0_29682_x5097_982962283}
:::

[[IP]{lang="EN-US"}]{#struct_0_29682_x5097_249117305}[优先级值]{style="font-family:黑体"}

[[routine]{lang="EN-US"}]{#struct_0_29682_x5097_x77074955}

[[0]{lang="EN-US"}]{#struct_0_29682_x5097_982634603}

[[priority]{lang="EN-US"}]{#struct_0_29682_x5097_x697276200}

[[1]{lang="EN-US"}]{#struct_0_29682_x5097_982569067}

[[immediate]{lang="EN-US"}]{#struct_0_29682_x5097_x2138091201}

[[2]{lang="EN-US"}]{#struct_0_29682_x5097_x616918602}

[[flash]{lang="EN-US"}]{#struct_0_29682_x5097_982765675}

[[3]{lang="EN-US"}]{#struct_0_29682_x5097_898197515}

[[flash-override]{lang="EN-US"}]{#struct_0_29682_x5097_982700139}

[[4]{lang="EN-US"}]{#struct_0_29682_x5097_1266075146}

[[critical]{lang="EN-US"}]{#struct_0_29682_x5097_983421035}

[[5]{lang="EN-US"}]{#struct_0_29682_x5097_x826133784}

[[internetwork]{lang="EN-US"}]{#struct_0_29682_x5097_x739287394}

[[6]{lang="EN-US"}]{#struct_0_29682_x5097_983355499}

[[network]{lang="EN-US"}]{#struct_0_29682_x5097_121462829}

[[7]{lang="EN-US"}]{#struct_0_29682_x5097_579612217}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_29682_x5097_670975351}

[[匹配原则：多个匹配条件（]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_29682_x5097_x549220157}[、]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级可以同时配置]{style="font-family:宋体"}[）之间是"或"的关系，即该节点的匹配条件任何一个满足，则该多拓扑转发策略节点匹配通过，该多拓扑转发策略也匹配通过。反之，该策略节点匹配失败，继续匹配其它节点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1753804632}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_1454518470}[创建一个名为]{style="font-family:宋体"}[mtr]{lang="EN-US"}[的多拓扑策略，其节点序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级]{style="font-family:宋体"}[值为]{style="font-family:宋体"}[5]{lang="EN-US"}[的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_1734534092}

[\[Sysname\] mtr-policy mtr node 0]{lang="EN-US"}

[\[Sysname-mtr-policy-mtr-0\] if-match ip precedence 5]{lang="EN-US"}

::: {#179985632 .myid}
[]{#_Toc404789186}[]{#struct_0_29682_x5097_x1962393070}

**MTR \-- MTR配置命令 \-- mtr-policy**

------------------------------------------------------------------------

[**[mtr-policy]{lang="EN-US"}**]{#struct_0_29682_x5097_x443864260}[命令用来创建多拓扑策略节点，并进入多拓扑策略节点视图。如果指定的节点已创建，则该命令直接用来进入该节点的视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[mtr-policy]{lang="EN-US"}**]{#struct_0_29682_x5097_1247559524}[命令用来删除已创建的多拓扑策略节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_305355940}

[**[mtr-policy]{lang="EN-US"}**[ *policy-name* **node** *node-value*]{lang="EN-US"}]{#struct_0_29682_x5097_x371962575}

[**[undo mtr-policy]{lang="EN-US"}**[ *policy-name* \[ **node** *node-value* \]]{lang="EN-US"}]{#struct_0_29682_x5097_x1592857579}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1081216247}

[[没有创建多拓扑策略节点。]{style="font-family:宋体"}]{#struct_0_29682_x5097_1377863106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1541056666}

[[系统视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_x394426311}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1734337484}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1531295588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1174982221}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1000545556}

[*[policy-name]{lang="EN-US"}*]{#struct_0_29682_x5097_1779001931}[：多拓扑转发策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[node]{lang="EN-US"}**[ *node-value*]{lang="EN-US"}]{#struct_0_29682_x5097_x2079145874}[：配置的该多拓扑转发策略的节点，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，每个多拓扑转发策略可以有多个节点，各个节点之间是或的关系，匹配上该多拓扑转发策略的其中任何一个节点，即匹配上该多拓扑转发策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1391396339}

[**[undo ]{lang="EN-US"}[mtr-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}***[ node ]{lang="EN-US"}***[node-value]{lang="EN-US"}*]{#struct_0_29682_x5097_x1366408695}[命令用来删除多拓扑转发策略]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[上的值为]{style="font-family:宋体"}*[node-value]{lang="EN-US"}*[的节点，如果该节点为多拓扑转发策略上的最后一个节点，则删除该多拓扑转发策略]{style="font-family:宋体"}[。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[mtr-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}[命令用来删除该多拓扑转发策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1192589164}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_x1307503625}[创建多拓扑策略]{style="font-family:宋体"}[mtr]{lang="EN-US"}[，节点为]{style="font-family:宋体"}[0]{lang="EN-US"}[，并进入多拓扑策略节点视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_x148177652}

[\[Sysname\] mtr-policy mtr node 0]{lang="EN-US"}

[\[Sysname-mtr-policy-mtr-0\]]{lang="EN-US"}
:::

::: {#573750374 .myid}
[]{#_Toc404789187}[]{#struct_0_29682_x5097_x1835808319}[]{#_Toc357171223}

**MTR \-- MTR配置命令 \-- routing-table limit**

------------------------------------------------------------------------

[**[routing-table limit]{lang="EN-US"}**]{#struct_0_29682_x5097_1734403020}[命令用来配置]{style="font-family:宋体"}[拓扑]{style="font-family:宋体"}[支持的最大激活路由前缀数。]{style="font-family:宋体"}

[**[undo routing-table limit]{lang="EN-US"}**]{#struct_0_29682_x5097_x1192326861}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_2081884969}

[**[routing-table]{lang="EN-US"}[ limit]{lang="EN-US"}**[ *number* { *warn-threshold* \| **simply-alert** }]{lang="EN-US"}]{#struct_0_29682_x5097_1233534043}

[**[undo routing-table limit]{lang="EN-US"}**]{#struct_0_29682_x5097_x937868792}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x784431114}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_29682_x5097_x1626490491}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x50712967}

[[多拓扑实例视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_x1809053106}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1400146786}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1636257290}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1734730700}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1210903367}

[*[number]{lang="EN-US"}*]{#struct_0_29682_x5097_1210154025}[：最大激活路由前缀数。不同设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[warn-threshold]{lang="EN-US"}*]{#struct_0_29682_x5097_x1364469904}[：告警门限值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为百分比。当（多拓扑实例中的激活路由前缀数]{style="font-family:宋体"}[/]{lang="EN-US"}[最大支持激活路由前缀数×]{style="font-family:宋体"}[100]{lang="EN-US"}[）达到告警门限值时，产生一条告警信息，但仍然允许激活路由前缀。当多拓扑实例中的激活路由前缀数达到最大支持激活路由前缀数目时，不再激活新的路由前缀。]{style="font-family:宋体"}

[**[simply-alert]{lang="EN-US"}**]{#struct_0_29682_x5097_1327908900}[：指定当多拓扑实例的激活路由前缀数超过支持的最大激活路由前缀数目时，可以继续激活新的路由前缀，但会产生一条系统日志信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x46016623}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_1429331042}[配置多拓扑]{style="font-family:宋体"}[mt1]{lang="EN-US"}[最大可支持]{style="font-family:宋体"}[1000]{lang="EN-US"}[条激活路由前缀，并且当激活路由前缀数超过最大支持激活路由前缀数时，可以继续激活新的路由前缀，但是会产生一条系统日志信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_x500389734}

[\[Sysname\] global-address-family ipv4 unicast]{lang="EN-US"}

[]{#_Toc94753854}[]{#_Toc94671180}[]{#_Toc73952257}[\[Sysname-global-ipv4\] topology mt1]{lang="EN-US"}

[\[Sysname-af-topology-mt1\] routing-table limit 1000 simply-alert]{lang="EN-US"}
:::

::: {#-1660379657 .myid}
[]{#_Toc404789188}[]{#struct_0_29682_x5097_x1082783088}

**MTR \-- MTR配置命令 \-- topology**

------------------------------------------------------------------------

[**[topology]{lang="EN-US"}**]{#struct_0_29682_x5097_1554462961}[命令用来创建一个拓扑，并进入多拓扑视图。]{style="font-family:宋体"}

[**[undo topology]{lang="EN-US"}**]{#struct_0_29682_x5097_x106284204}[命令用来删除一个拓扑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1734796236}

[**[topology]{lang="EN-US"}**[ ]{lang="EN-US"}*[topo-name]{lang="EN-US"}*]{#struct_0_29682_x5097_x1160303744}

[**[undo topology]{lang="EN-US"}**[ ]{lang="EN-US"}*[topo-name]{lang="EN-US"}*]{#struct_0_29682_x5097_440354934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_590489729}

[[没有]{style="font-family:宋体"}]{#struct_0_29682_x5097_x491557050}[创建拓扑。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x2043176282}

[[全局地址族视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_x796473829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1960785835}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1228608166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1168779152}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x622840771}

[*[topo-name]{lang="EN-US"}*]{#struct_0_29682_x5097_976683482}[：拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1734599628}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_x1606138698}[配置]{style="font-family:宋体"}[一个拓扑]{style="font-family:宋体"}[mt]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_572941522}

[\[Sysname\] global-address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-global-ipv4\] topology mt]{lang="EN-US"}

[\[Sysname-af-topology-mt\]]{lang="EN-US"}
:::

::: {#-1353377071 .myid}
[]{#_Toc404789189}[]{#struct_0_29682_x5097_1499973008}[]{#_Toc357171224}

**MTR \-- MTR配置命令 \-- topology ipv4**

------------------------------------------------------------------------

[**[topology ipv4]{lang="EN-US"}**]{#struct_0_29682_x5097_1322777013}[命令用来创建并进入]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播拓扑]{style="font-family:宋体"}[视图，将接口与指定]{style="font-family:宋体"}[拓扑进行]{style="font-family:宋体"}[关联。]{style="font-family:宋体"}

[**[undo topology ipv4]{lang="EN-US"}**]{#struct_0_29682_x5097_651607781}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x2021172167}

[**[topology ipv4]{lang="EN-US"}**[ \[ **unicast** \] *topo-name*]{lang="EN-US"}]{#struct_0_29682_x5097_x283112193}

[**[undo topology ipv4]{lang="EN-US"}**[ \[ **unicast** \] *topo-name*]{lang="EN-US"}]{#struct_0_29682_x5097_x585737430}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1102535974}

[[接口与没有关联到任何]{style="font-family:宋体"}]{#struct_0_29682_x5097_1390512062}[拓扑]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1734665164}

[[接口视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_1933364683}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x133741878}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1346792986}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1034724809}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1626652386}

[**[unicast]{lang="EN-US"}**]{#struct_0_29682_x5097_x857072421}[：单播方式。如果未指定本参数，也表示单播方式。]{style="font-family:宋体"}

[*[topo-name]{lang="EN-US"}*]{#struct_0_29682_x5097_344721521}[：拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_29682_x5097_211737920}

[[接口关联的拓扑必须已经创建成功。]{style="font-family:宋体"}]{#struct_0_29682_x5097_x628545474}

[[当拓扑名为"]{style="font-family:宋体"}[unicast]{lang="EN-US"}]{#struct_0_29682_x5097_x207051924}["时，参数]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[必须配置，否则命令无法正常下发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1487182565}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_1734992844}[将接口]{style="font-family:宋体"}[LoopBack 0]{lang="EN-US"}[与拓扑]{style="font-family:宋体"}[mt1]{lang="EN-US"}[进行]{style="font-family:宋体"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_18414893}

[\[Sysname\] interface loopback 0]{lang="EN-US"}

[\[Sysname-LoopBack0\] topology ipv4 unicast mt1]{lang="EN-US"}

[\[Sysname-LoopBack0-topology-1\]]{lang="EN-US"}
:::

::: {#-393518000 .myid}
[]{#_Toc404789190}[]{#struct_0_29682_x5097_415976840}

**MTR \-- MTR配置命令 \-- topology-routing mtr-policy**

------------------------------------------------------------------------

[**[topology-routing mtr-policy]{lang="EN-US"}**]{#struct_0_29682_x5097_1753593163}[命令使能多拓扑转发策略。]{style="font-family:
宋体"}

[**[undo topology-routing mtr-policy]{lang="EN-US"}**]{#struct_0_29682_x5097_x1316960614}[命令用来关闭多拓扑转发策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_29682_x5097_1303696326}

[**[topology-routing mtr-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_29682_x5097_x1426322212}

[**[undo topology-routing mtr-policy]{lang="EN-US"}**]{#struct_0_29682_x5097_1556857619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x271649844}

[[多拓扑转发策略处于关闭状态。]{style="font-family:宋体"}]{#struct_0_29682_x5097_224389458}

[[【视图】]{style="font-family:黑体"}]{#struct_0_29682_x5097_176055273}

[[全局地址族视图]{style="font-family:宋体"}]{#struct_0_29682_x5097_1735058380}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x455230998}

[[network-admin]{lang="EN-US"}]{#struct_0_29682_x5097_1649078750}

[[mdc-admin]{lang="EN-US"}]{#struct_0_29682_x5097_x1706694478}

[[【参数】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x1767024805}

[*[policy-name]{lang="EN-US"}*]{#struct_0_29682_x5097_x588377851}[：]{style="font-family:宋体"}[多拓扑转发策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_29682_x5097_x247422348}

[[\# ]{lang="EN-US"}]{#struct_0_29682_x5097_749479964}[使能多拓扑转发策略]{style="font-family:宋体"}[mtr]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_29682_x5097_841753835}

[\[Sysname\] global-address-family ipv4]{lang="EN-US"}

[\[Sysname-global-ipv4\] topology-routing mtr-policy mtr]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
