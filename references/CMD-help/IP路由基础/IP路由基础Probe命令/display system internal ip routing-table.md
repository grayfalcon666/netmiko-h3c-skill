::: {#1019689130 .myid}
[]{#_Toc404799426}[]{#struct_0_20219_18486_1192802721}[]{#_Toc361832005}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table**

------------------------------------------------------------------------

[**[display system internal ip routing-table]{lang="EN-US"}**]{#struct_0_20219_18486_x130650511}[命令用来显示路由表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1825301204}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x196237154}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] \[ **verbose** \] **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_382114329}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_1192868257}[模式：]{style="font-family:宋体"}

[**[display system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] \[ **verbose** \] **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x901991728}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_550921824}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1877981179}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1238482760}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x222954037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1255616336}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_219048234}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_20219_18486_x418946186}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_1192933793}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_1433139646}[：显示全部路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x754563779}[：显示备份的指定单板的路由表信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1099000675}[：显示备份的指定成员设备的路由表信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x2035591189}[：显示备份的指定成员设备上指定单板的路由表信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x183903029}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1779718697 .myid}
[]{#_Toc404799427}[]{#struct_0_20219_18486_121426098}[]{#_Toc361832006}[]{#_Toc292701673}[]{#_Toc251058581}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table acl**

------------------------------------------------------------------------

[**[display system internal ip routing-table acl]{lang="EN-US"}**]{#struct_0_20219_18486_1953170783}[命令用来显示通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x425384726}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1192475041}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip routing-table ]{lang="EN-US"}**[\[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **acl** *acl-number* \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1338264074}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_1042928646}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ip routing-table ]{lang="EN-US"}**[\[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **acl** *acl-number* \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x872355957}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1078943732}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_929736826}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x283651586}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x233326129}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x2112489218}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x419675766}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_20219_18486_1192540577}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_640768005}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_20219_18486_735970620}[：基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_x1082437852}[：显示通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的所有路由的详细信息。如果未指定本参数，将只显示通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的激活路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x859265564}[：显示备份的指定单板的通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x999249190}[：显示备份的指定成员设备的通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_353504263}[：显示备份的指定成员设备上通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的路由信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x679152179}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1073426397 .myid}
[]{#_Toc404799428}[]{#struct_0_20219_18486_499051310}[]{#_Toc361832007}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table ip-address**

------------------------------------------------------------------------

[**[display system internal ip routing-table ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_20219_18486_1192606113}[命令用来显示指定目的地址的路由信息。]{style="font-family:宋体"}

[**[display system internal ip routing-table ]{lang="EN-US"}***[ip-address1 ]{lang="EN-US"}***[to]{lang="EN-US"}***[ ip-address2]{lang="EN-US"}*]{#struct_0_20219_18486_x1717812832}[命令用来显示指定目的地址范围内的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x834795254}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_388733868}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] *ip-address* \[ *mask* \| *mask-length* \] \[ **longer-match** \] \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1705653825}

[**[display system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] *ip-address1* **to** *ip-address2* \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x683750685}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1273346796}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] *ip-address* \[ *mask* \| *mask-length* \] \[ **longer-match** \] \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1628432280}

[**[display system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] *ip-address1* **to** *ip-address2* \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x164099604}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1192671649}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_249291724}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_2110308218}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_522099928}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1713978176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x827479846}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_20219_18486_1569594063}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x1693112942}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_20219_18486_140960334}[：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制格式。]{style="font-family:宋体"}

[*[mask/mask-length]{lang="EN-US"}*]{#struct_0_20219_18486_961130249}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[longer-match]{lang="EN-US"}**]{#struct_0_20219_18486_1193261473}[：匹配掩码更长的路由。]{style="font-family:宋体"}

[*[ip-address1]{lang="EN-US"}*[ **to** *ip-address2*]{lang="EN-US"}]{#struct_0_20219_18486_x2108562347}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}*[ip-address1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[ip-address2]{lang="EN-US"}*[共同决定一个地址范围，只有地址在此范围内的路由才会被显示。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_1663952870}[：显示全部路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1128776737}[：显示备份的指定单板的指定目的地址的路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_990160429}[：显示备份的指定成员设备的指定目的地址的路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1059646541}[：显示备份的指定成员设备上指定目的地址的路由信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_5810199}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#431872114 .myid}
[]{#_Toc404799429}[]{#struct_0_20219_18486_1708008738}[]{#_Toc361832008}[]{#_Toc292701675}[]{#_Toc251058583}[]{#_Toc17100929}[]{#_Toc15880065}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table prefix-list**

------------------------------------------------------------------------

[**[display system internal ip routing-table prefix-list]{lang="EN-US"}**]{#struct_0_20219_18486_1766377668}[命令用来显示通过指定前缀列表过滤的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1193327009}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x1702441621}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip routing-table ]{lang="EN-US"}**[\[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **prefix-list** *prefix-list-name* \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x478928561}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x2054136314}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **prefix-list** *prefix-list-name* \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1423876216}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1055641923}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x797331406}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_758231368}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1335236361}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x961253404}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1192737186}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_20219_18486_x153563937}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_1862243480}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_20219_18486_x1803701801}[：前缀列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_x589715385}[：当使用该参数时，显示通过过滤规则的所有路由的详细信息。如果未指定本参数，将只显示通过过滤规则的激活路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1799517157}[：显示备份的指定单板的指定前缀列表过滤的路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1564317930}[：显示备份的指定成员设备的指定前缀列表过滤的路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x527607807}[：显示备份的指定成员设备上指定单板的指定前缀列表过滤的路由信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x935555842}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1753828847 .myid}
[]{#_Toc404799430}[]{#struct_0_20219_18486_1192802722}[]{#_Toc361832009}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table protocol**

------------------------------------------------------------------------

[**[display system internal ip routing-table]{lang="EN-US"}**[ **protocol**]{lang="EN-US"}]{#struct_0_20219_18486_x130847119}[命令用来显示指定协议生成或发现的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1294695099}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1901175279}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **protocol** *protocol* \[ **inactive** \| **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_1665297109}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x935099318}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **protocol** *protocol* \[ **inactive** \| **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_2066223595}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_2106828003}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_408861497}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1192868258}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x902974768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x5782483}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1799127320}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_20219_18486_1032512426}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_1139932588}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_20219_18486_508755250}[：显示指定路由协议的信息，包括]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[inactive]{lang="EN-US"}**]{#struct_0_20219_18486_x679641699}[：显示未激活路由的信息。如果未指定本参数，则显示激活路由和未激活路由的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_x1434415570}[：当使用该参数时，显示路由的详细信息。如果未指定本参数，将显示路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1192933794}[：显示备份的指定单板的指定路由协议的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1433598398}[：显示备份的指定成员设备的路由表中的指定路由协议的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1141065383}[：显示备份的指定成员设备上指定单板的路由表中的指定路由协议的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1161882511}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#2037879185 .myid}
[]{#_Toc404799431}[]{#struct_0_20219_18486_x973805952}[]{#_Toc361832010}[]{#_Toc251058585}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ip routing-table statistics**

------------------------------------------------------------------------

[**[display system internal ip routing-table statistics]{lang="EN-US"}**]{#struct_0_20219_18486_1272537295}[命令用来显示路由表中的综合路由统计信息。综合路由统计信息包括路由总数目、路由协议添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除路由数目、激活路由数目。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1180531572}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1804725093}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **statistics** **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_1240820361}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_707740372}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ip routing-table]{lang="EN-US"}**[ \[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* \] **statistics** **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_1192475042}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1338329610}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_243123804}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1325641004}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1418418119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_116767488}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x464509442}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_20219_18486_1994846444}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_1759658207}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1192540578}[：显示备份的指定单板的路由表中的综合路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_641619973}[：显示备份的指定成员设备的路由表中的综合路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1923868807}[：显示备份的指定成员设备上指定单板的路由表中的综合路由统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x414461360}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#729842666 .myid}
[]{#_Toc404799432}[]{#struct_0_20219_18486_240344584}[]{#_Toc361832012}[]{#_Toc343698412}[]{#_Toc340320593}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib attribute**

------------------------------------------------------------------------

[**[display system internal ipv6 rib attribute]{lang="EN-US"}**]{#struct_0_20219_18486_x543465744}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的路由属性信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x2093894784}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x1436665248}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib attribute]{lang="EN-US"}**[ \[ *attribute-id* \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x687853259}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_62836943}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib attribute]{lang="EN-US"}**[ \[ *attribute-id* \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_1192606114}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1717485152}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_574848210}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_843336223}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_2024151096}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1868588128}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x295110823}

[*[attribute-id]{lang="EN-US"}*]{#struct_0_20219_18486_x1336859232}[：路由属性]{style="font-family:宋体"}[ID]{lang="EN-US"}[值，取值范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1391932473}[：显示备份的指定单板的]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[路由属性信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1070507853}[：显示备份的指定成员设备的]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[路由属性信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1192671650}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[路由属性信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_248832971}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#96644528 .myid}
[]{#_Toc340320596}[]{#_Toc340320597}[]{#_Toc404799433}[]{#struct_0_20219_18486_236793723}[]{#_Toc340320607}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event attribute**

------------------------------------------------------------------------

[**[display system internal ipv6 rib event attribute ]{lang="EN-US"}**]{#struct_0_20219_18486_823913227}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的路由属性事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x227600386}

[**[display system internal ipv6 rib event attribute]{lang="EN-US"}**]{#struct_0_20219_18486_x2103770718}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1469220249}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1936027711}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1163573065}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x964710156}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1769873764}
:::

::: {#846237611 .myid}
[]{#_Toc340320605}[]{#_Toc404799434}[]{#struct_0_20219_18486_1935962175}[]{#_Toc340320609}[]{#_Toc361386877}[]{#_Toc362010928}[]{#_Toc361386878}[]{#_Toc362010929}[]{#_Toc361386879}[]{#_Toc362010930}[]{#_Toc361386880}[]{#_Toc362010931}[]{#_Toc361386881}[]{#_Toc362010932}[]{#_Toc361386882}[]{#_Toc362010933}[]{#_Toc361386883}[]{#_Toc362010934}[]{#_Toc361386884}[]{#_Toc362010935}[]{#_Toc361386885}[]{#_Toc362010936}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event policy**

------------------------------------------------------------------------

[**[display system internal ipv6 rib event policy]{lang="EN-US"}**]{#struct_0_20219_18486_x978592410}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的路由策略事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_2016078743}

[**[display system internal ipv6 rib event policy]{lang="EN-US"}**]{#struct_0_20219_18486_1093705088}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x334252523}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_632474405}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1935503424}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1280280849}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_319846328}
:::

::: {#412025840 .myid}
[]{#_Toc404799435}[]{#struct_0_20219_18486_192327380}[]{#_Toc361386887}[]{#_Toc362010938}[]{#_Toc361386888}[]{#_Toc362010939}[]{#_Toc361386889}[]{#_Toc362010940}[]{#_Toc361386890}[]{#_Toc362010941}[]{#_Toc361386891}[]{#_Toc362010942}[]{#_Toc361386892}[]{#_Toc362010943}[]{#_Toc361386893}[]{#_Toc362010944}[]{#_Toc361386894}[]{#_Toc362010945}[]{#_Toc361386895}[]{#_Toc362010946}[]{#_Toc361386896}[]{#_Toc362010947}[]{#_Toc361386897}[]{#_Toc362010948}[]{#_Toc361386898}[]{#_Toc362010949}[]{#_Toc361386899}[]{#_Toc362010950}[]{#_Toc361386900}[]{#_Toc362010951}[]{#_Toc361386901}[]{#_Toc362010952}[]{#_Toc361386902}[]{#_Toc362010953}[]{#_Toc361386903}[]{#_Toc362010954}[]{#_Toc361386904}[]{#_Toc362010955}[]{#_Toc361386905}[]{#_Toc362010956}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event prefix**

------------------------------------------------------------------------

[**[display system internal ipv6 rib event prefix]{lang="EN-US"}**]{#struct_0_20219_18486_x420011903}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的路由前缀事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1871874801}

[**[display system internal ipv6 rib event prefix]{lang="EN-US"}**]{#struct_0_20219_18486_x1053394303}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_94053266}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1935372352}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1287585393}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1474674143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_533137197}
:::

::: {#-1714324626 .myid}
[]{#_Toc404799436}[]{#struct_0_20219_18486_1887979289}[]{#_Toc340320603}[]{#_Toc361386907}[]{#_Toc362010958}[]{#_Toc361386908}[]{#_Toc362010959}[]{#_Toc361386909}[]{#_Toc362010960}[]{#_Toc361386910}[]{#_Toc362010961}[]{#_Toc361386911}[]{#_Toc362010962}[]{#_Toc361386912}[]{#_Toc362010963}[]{#_Toc361386913}[]{#_Toc362010964}[]{#_Toc361386914}[]{#_Toc362010965}[]{#_Toc361386915}[]{#_Toc362010966}[]{#_Toc361386916}[]{#_Toc362010967}[]{#_Toc361386917}[]{#_Toc362010968}[]{#_Toc361386918}[]{#_Toc362010969}[]{#_Toc361386919}[]{#_Toc362010970}[]{#_Toc361386920}[]{#_Toc362010971}[]{#_Toc361386921}[]{#_Toc362010972}[]{#_Toc361386922}[]{#_Toc362010973}[]{#_Toc361386923}[]{#_Toc362010974}[]{#_Toc361386924}[]{#_Toc362010975}[]{#_Toc361386925}[]{#_Toc362010976}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event protocol**

------------------------------------------------------------------------

[**[display system internal ipv6 rib event protocol]{lang="EN-US"}**]{#struct_0_20219_18486_x1857873178}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的协议事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1115657379}

[**[display system internal ipv6 rib event protocol ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_20219_18486_1935765568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x255865415}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1371188229}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_352423950}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1105020046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_568533998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1408120411}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x198564916}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1659687978 .myid}
[]{#_Toc404799437}[]{#struct_0_20219_18486_1306583530}[]{#_Toc340320611}[]{#_Toc361386927}[]{#_Toc362010978}[]{#_Toc361386928}[]{#_Toc362010979}[]{#_Toc361386929}[]{#_Toc362010980}[]{#_Toc361386930}[]{#_Toc362010981}[]{#_Toc361386931}[]{#_Toc362010982}[]{#_Toc361386932}[]{#_Toc362010983}[]{#_Toc361386933}[]{#_Toc362010984}[]{#_Toc361386934}[]{#_Toc362010985}[]{#_Toc361386935}[]{#_Toc362010986}[]{#_Toc361386936}[]{#_Toc362010987}[]{#_Toc361386937}[]{#_Toc362010988}[]{#_Toc361386938}[]{#_Toc362010989}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib event statistics**

------------------------------------------------------------------------

[**[display system internal ipv6 rib event statistics]{lang="EN-US"}**]{#struct_0_20219_18486_1935634496}[用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的统计事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_526991988}

[**[display system internal ipv6 rib event statistics]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_20219_18486_256315772}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x866552028}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1067387481}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1335198756}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_585873881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x317671027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1935568960}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x1434666678}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#170209272 .myid}
[]{#_Toc404799438}[]{#struct_0_20219_18486_1935962176}[]{#_Toc336358571}[]{#_Toc340320613}[]{#_Toc361386940}[]{#_Toc362010991}[]{#_Toc361386941}[]{#_Toc362010992}[]{#_Toc361386942}[]{#_Toc362010993}[]{#_Toc361386943}[]{#_Toc362010994}[]{#_Toc361386944}[]{#_Toc362010995}[]{#_Toc361386945}[]{#_Toc362010996}[]{#_Toc361386946}[]{#_Toc362010997}[]{#_Toc361386947}[]{#_Toc362010998}[]{#_Toc361386948}[]{#_Toc362010999}[]{#_Toc361386949}[]{#_Toc362011000}[]{#_Toc361386950}[]{#_Toc362011001}[]{#_Toc361386951}[]{#_Toc362011002}[]{#_Toc361386952}[]{#_Toc362011003}[]{#_Toc361386953}[]{#_Toc362011004}[]{#_Toc361386954}[]{#_Toc362011005}[]{#_Toc361386955}[]{#_Toc362011006}[]{#_Toc361386956}[]{#_Toc362011007}[]{#_Toc361386957}[]{#_Toc362011008}[]{#_Toc361386958}[]{#_Toc362011009}[]{#_Toc361386959}[]{#_Toc362011010}[]{#_Toc361386960}[]{#_Toc362011011}[]{#_Toc361386961}[]{#_Toc362011012}[]{#_Toc361386962}[]{#_Toc362011013}[]{#_Toc361386963}[]{#_Toc362011014}[]{#_Toc361386964}[]{#_Toc362011015}[]{#_Toc361386965}[]{#_Toc362011016}[]{#_Toc361386966}[]{#_Toc362011017}[]{#_Toc361386967}[]{#_Toc362011018}[]{#_Toc361386968}[]{#_Toc362011019}[]{#_Toc361386969}[]{#_Toc362011020}[]{#_Toc361386970}[]{#_Toc362011021}[]{#_Toc361386971}[]{#_Toc362011022}[]{#_Toc361386972}[]{#_Toc362011023}[]{#_Toc361386973}[]{#_Toc362011024}[]{#_Toc361386974}[]{#_Toc362011025}[]{#_Toc361386975}[]{#_Toc362011026}[]{#_Toc361386976}[]{#_Toc362011027}[]{#_Toc361386977}[]{#_Toc362011028}[]{#_Toc361386978}[]{#_Toc362011029}[]{#_Toc361386979}[]{#_Toc362011030}[]{#_Toc361386980}[]{#_Toc362011031}[]{#_Toc361386981}[]{#_Toc362011032}[]{#_Toc361386982}[]{#_Toc362011033}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib log**

------------------------------------------------------------------------

[**[display system internal ipv6 rib log]{lang="EN-US"}**]{#struct_0_20219_18486_133656935}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1276527794}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_526941044}

[**[display system internal ipv6 rib log]{lang="EN-US"}**[ \[ **reverse** \]]{lang="EN-US"}]{#struct_0_20219_18486_x115391664}

[**[display system internal ipv6 rib event log]{lang="EN-US"}**]{#struct_0_20219_18486_1935503421}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1280084241}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x503035422}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib event log]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1533097862}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x114772145}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1935437885}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib event log]{lang="EN-US"}**[ \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_961918670}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_937102403}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1633803012}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1304486174}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1172960103}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1399758775}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_2070918011}

[**[rib]{lang="EN-US"}**]{#struct_0_20219_18486_1935372349}[：显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_1287126640}[：显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[路由变化通知的日志信息。]{style="font-family:宋体"}

[**[reverse]{lang="EN-US"}**]{#struct_0_20219_18486_x821469043}[：按时间新旧显示日志信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x768992561}[：显示备份的指定单板]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_2118650588}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x785319714}[：显示备份的指定成员设备上]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_91139367}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-2052391364 .myid}
[]{#_Toc404799439}[]{#struct_0_20219_18486_x1696503533}[]{#_Toc361386984}[]{#_Toc362011035}[]{#_Toc361386985}[]{#_Toc362011036}[]{#_Toc361386986}[]{#_Toc362011037}[]{#_Toc361386987}[]{#_Toc362011038}[]{#_Toc361386988}[]{#_Toc362011039}[]{#_Toc361386989}[]{#_Toc362011040}[]{#_Toc361386990}[]{#_Toc362011041}[]{#_Toc361386991}[]{#_Toc362011042}[]{#_Toc361386992}[]{#_Toc362011043}[]{#_Toc361386993}[]{#_Toc362011044}[]{#_Toc361387012}[]{#_Toc362011063}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib memory**

------------------------------------------------------------------------

[**[display system internal]{lang="EN-US"}**[ **ipv6 rib memory**]{lang="EN-US"}]{#struct_0_20219_18486_1935634493}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的内存信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_526664308}

[**[display system internal ipv6 rib memory]{lang="EN-US"}**]{#struct_0_20219_18486_x1146904233}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1200632531}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x274646417}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_253607522}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_414761360}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_681229054}
:::

::: {#-214993834 .myid}
[]{#_Toc404799440}[]{#struct_0_20219_18486_x723154592}[]{#_Toc361832014}[]{#_Toc343698414}[]{#_Toc340320595}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib nib**

------------------------------------------------------------------------

[**[display system internal ipv6 rib nib]{lang="EN-US"}**]{#struct_0_20219_18486_x31642017}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x754462046}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x1091040938}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 rib nib ]{lang="EN-US"}**[\[ **self-originated** \] \[ *nib-id* \] \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_2097748253}

[**[display system internal ipv6 ]{lang="EN-US"}[rib nib protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*[ \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x142301384}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x723482272}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 ]{lang="EN-US"}[rib nib]{lang="EN-US"}**[ \[ **self-originated** \] \[ *nib-id* \] \[ **verbose** \]  **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_383904404}

[**[display system internal ipv6 ]{lang="EN-US"}[rib nib protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*[ \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_825965097}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1417625183}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x685808964}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1324375917}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x998676759}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1236463712}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1079674572}

[**[self-originated]{lang="EN-US"}**]{#struct_0_20219_18486_1304102698}[：路由管理自己生成的下一跳。]{style="font-family:宋体"}

[*[nib-id]{lang="EN-US"}*]{#struct_0_20219_18486_x1143391602}[：路由下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}[值，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_x1212682586}[：显示详细信息。如果未指定本参数，则显示概要信息。]{style="font-family:宋体"}

[**[protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*]{#struct_0_20219_18486_x723547808}[：显示指定路由协议的下一跳信息，包括]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static6]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x385381219}[：显示备份的指定单板的]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[下一跳信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1775352101}[：显示备份的指定成员设备的]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[下一跳信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x595714465}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[下一跳信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1369311051}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1186207909 .myid}
[]{#_Toc340320599}[]{#_Toc404799441}[]{#struct_0_20219_18486_x1506376692}[]{#_Toc336358573}[]{#_Toc340320615}[]{#_Toc361387014}[]{#_Toc362011065}[]{#_Toc361387015}[]{#_Toc362011066}[]{#_Toc361387016}[]{#_Toc362011067}[]{#_Toc361387017}[]{#_Toc362011068}[]{#_Toc361387018}[]{#_Toc362011069}[]{#_Toc361387019}[]{#_Toc362011070}[]{#_Toc361387020}[]{#_Toc362011071}[]{#_Toc361387021}[]{#_Toc362011072}[]{#_Toc361387022}[]{#_Toc362011073}[]{#_Toc361387023}[]{#_Toc362011074}[]{#_Toc361387024}[]{#_Toc362011075}[]{#_Toc361387025}[]{#_Toc362011076}[]{#_Toc361387026}[]{#_Toc362011077}[]{#_Toc361387027}[]{#_Toc362011078}[]{#_Toc361387028}[]{#_Toc362011079}[]{#_Toc361387029}[]{#_Toc362011080}[]{#_Toc361387030}[]{#_Toc362011081}[]{#_Toc361387031}[]{#_Toc362011082}[]{#_Toc361387032}[]{#_Toc362011083}[]{#_Toc361387033}[]{#_Toc362011084}[]{#_Toc361387034}[]{#_Toc362011085}[]{#_Toc361387035}[]{#_Toc362011086}[]{#_Toc361387036}[]{#_Toc362011087}[]{#_Toc361387037}[]{#_Toc362011088}[]{#_Toc361387038}[]{#_Toc362011089}[]{#_Toc361387039}[]{#_Toc362011090}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib nib log**

------------------------------------------------------------------------

[**[display system internal ipv6 rib nib log]{lang="EN-US"}**]{#struct_0_20219_18486_828692374}[命令用来显示系统内部]{style="font-family:宋体"}[IPv6 NIB]{lang="EN-US"}[子模块运行状态的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x867623541}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1474330459}

[**[display system internal ipv6 rib nib log]{lang="EN-US"}**[ \[ **reverse** \]]{lang="EN-US"}]{#struct_0_20219_18486_1935962173}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_901446957}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib nib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_2008633987}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_1988928264}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib nib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1333603979}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1935503422}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1279887633}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1980794105}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x446927017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1356281171}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1442009059}

[**[nib]{lang="EN-US"}**]{#struct_0_20219_18486_806461930}[：显示]{style="font-family:宋体"}[IPv6 NIB]{lang="EN-US"}[子模块的运行状态。]{style="font-family:宋体"}

[**[reverse]{lang="EN-US"}**]{#struct_0_20219_18486_x823837482}[：按时间新旧显示日志信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1935437886}[：显示备份的指定单板]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_961853134}[：显示备份的指定成员设备的]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_962506250}[：显示备份的指定成员设备上]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1865175776}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-2060181217 .myid}
[]{#_Toc404799442}[]{#struct_0_20219_18486_x445161395}[]{#_Toc361387041}[]{#_Toc362011092}[]{#_Toc361387042}[]{#_Toc362011093}[]{#_Toc361387043}[]{#_Toc362011094}[]{#_Toc361387044}[]{#_Toc362011095}[]{#_Toc361387045}[]{#_Toc362011096}[]{#_Toc361387046}[]{#_Toc362011097}[]{#_Toc361387047}[]{#_Toc362011098}[]{#_Toc361387048}[]{#_Toc362011099}[]{#_Toc361387049}[]{#_Toc362011100}[]{#_Toc361387050}[]{#_Toc362011101}[]{#_Toc361387051}[]{#_Toc362011102}[]{#_Toc361387052}[]{#_Toc362011103}[]{#_Toc361387053}[]{#_Toc362011104}[]{#_Toc361387054}[]{#_Toc362011105}[]{#_Toc361387055}[]{#_Toc362011106}[]{#_Toc361387056}[]{#_Toc362011107}[]{#_Toc361387057}[]{#_Toc362011108}[]{#_Toc361387058}[]{#_Toc362011109}[]{#_Toc361387059}[]{#_Toc362011110}[]{#_Toc361387060}[]{#_Toc362011111}[]{#_Toc361387061}[]{#_Toc362011112}[]{#_Toc361387062}[]{#_Toc362011113}[]{#_Toc361387063}[]{#_Toc362011114}[]{#_Toc361387064}[]{#_Toc362011115}[]{#_Toc361387065}[]{#_Toc362011116}[]{#_Toc361387066}[]{#_Toc362011117}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib prefix**

------------------------------------------------------------------------

[**[display system internal ipv6 rib prefix]{lang="EN-US"}**]{#struct_0_20219_18486_x1221084200}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表前缀信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1454707556}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1972705747}

[**[display system internal ipv6 rib prefix ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}***[ ]{lang="EN-US"}***[prefix-length]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_20219_18486_2018218619}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1366662459}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib prefix ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}***[ ]{lang="EN-US"}***[prefix-length]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \] \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1935765566}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x255996487}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib prefix ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}***[ ]{lang="EN-US"}***[prefix-length]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \] \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1372178604}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1879677382}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1042556607}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1935700030}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_2081428669}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_2049296027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1862499183}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_20219_18486_x188996845}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的]{style="font-family:宋体"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_20219_18486_1574121089}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_1521795140}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1935634494}[：显示备份的指定单板]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表前缀信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表前缀信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_527123060}[：显示备份的指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表前缀信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表前缀信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_173810757}[：显示备份的指定成员设备上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表前缀信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表前缀信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1865175782}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#924997877 .myid}
[]{#_Toc404799443}[]{#struct_0_20219_18486_x256491965}[]{#_Toc340320601}[]{#_Toc361387068}[]{#_Toc362011119}[]{#_Toc361387069}[]{#_Toc362011120}[]{#_Toc361387070}[]{#_Toc362011121}[]{#_Toc361387071}[]{#_Toc362011122}[]{#_Toc361387072}[]{#_Toc362011123}[]{#_Toc361387073}[]{#_Toc362011124}[]{#_Toc361387074}[]{#_Toc362011125}[]{#_Toc361387075}[]{#_Toc362011126}[]{#_Toc361387076}[]{#_Toc362011127}[]{#_Toc361387077}[]{#_Toc362011128}[]{#_Toc361387078}[]{#_Toc362011129}[]{#_Toc361387079}[]{#_Toc362011130}[]{#_Toc361387080}[]{#_Toc362011131}[]{#_Toc361387081}[]{#_Toc362011132}[]{#_Toc361387082}[]{#_Toc362011133}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 rib summary**

------------------------------------------------------------------------

[**[display system internal ipv6 rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_1936027710}[命令用来显示]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1163507529}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_x202538140}

[**[display system internal ipv6 rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_x2018208225}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1935962174}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib summary ]{lang="EN-US"}**[\[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_901512493}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_528217465}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 rib summary ]{lang="EN-US"}**[\[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1935503419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1280608532}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1211051435}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1489871424}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1753552691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x2332804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1885340628}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1935437883}[：显示备份的指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_961525454}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1885801122}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1865175780}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-93939762 .myid}
[]{#_Toc404799444}[]{#struct_0_20219_18486_x1215793904}[]{#_Toc348956742}[]{#_Toc337654560}[]{#_Toc361387084}[]{#_Toc362011135}[]{#_Toc361387085}[]{#_Toc362011136}[]{#_Toc361387086}[]{#_Toc362011137}[]{#_Toc361387087}[]{#_Toc362011138}[]{#_Toc361387088}[]{#_Toc362011139}[]{#_Toc361387089}[]{#_Toc362011140}[]{#_Toc361387090}[]{#_Toc362011141}[]{#_Toc361387091}[]{#_Toc362011142}[]{#_Toc361387092}[]{#_Toc362011143}[]{#_Toc361387093}[]{#_Toc362011144}[]{#_Toc361387094}[]{#_Toc362011145}[]{#_Toc361387095}[]{#_Toc362011146}[]{#_Toc361387096}[]{#_Toc362011147}[]{#_Toc361387097}[]{#_Toc362011148}[]{#_Toc361387098}[]{#_Toc362011149}[]{#_Toc361387099}[]{#_Toc362011150}[]{#_Toc361387100}[]{#_Toc362011151}[]{#_Toc361387101}[]{#_Toc362011152}[]{#_Toc361387102}[]{#_Toc362011153}[]{#_Toc361387103}[]{#_Toc362011154}[]{#_Toc361387104}[]{#_Toc362011155}[]{#_Toc361387105}[]{#_Toc362011156}[]{#_Toc361387106}[]{#_Toc362011157}[]{#_Toc361387107}[]{#_Toc362011158}[]{#_Toc361387108}[]{#_Toc362011159}[]{#_Toc361387109}[]{#_Toc362011160}[]{#_Toc361387110}[]{#_Toc362011161}[]{#_Toc361387111}[]{#_Toc362011162}[]{#_Toc361387112}[]{#_Toc362011163}[]{#_Toc361387113}[]{#_Toc362011164}[]{#_Toc361387114}[]{#_Toc362011165}[]{#_Toc361387115}[]{#_Toc362011166}[]{#_Toc361387116}[]{#_Toc362011167}[]{#_Toc361387117}[]{#_Toc362011168}[]{#_Toc361387118}[]{#_Toc362011169}[]{#_Toc361387119}[]{#_Toc362011170}[]{#_Toc361387120}[]{#_Toc362011171}[]{#_Toc361387121}[]{#_Toc362011172}[]{#_Toc361387122}[]{#_Toc362011173}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 route-direct interface**

------------------------------------------------------------------------

[**[display system internal ipv6 route-direct interface]{lang="EN-US"}**]{#struct_0_20219_18486_1238733870}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址接口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1700432220}

[**[display system internal ipv6 route-direct interface]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ *interface-type* *interface-number* \| *ipv6-address* *prefix-length* \]]{lang="EN-US"}]{#struct_0_20219_18486_1555708465}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_2138884481}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1439681234}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x179468090}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1526619566}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1935700027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_2081625276}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x364268995}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_20219_18486_x751666239}[：接口类型和接口编号。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_20219_18486_1509046055}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_20219_18486_x1978462940}[：前缀长度，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}
:::

::: {#1292087507 .myid}
[]{#_Toc340320606}[]{#_Toc340320640}[]{#_Toc337654557}[]{#_Toc404799445}[]{#struct_0_20219_18486_526729844}[]{#_Toc350345744}[]{#_Toc340320651}[]{#_Toc337654562}[]{#_Toc361387124}[]{#_Toc362011175}[]{#_Toc361387125}[]{#_Toc362011176}[]{#_Toc361387126}[]{#_Toc362011177}[]{#_Toc361387127}[]{#_Toc362011178}[]{#_Toc361387128}[]{#_Toc362011179}[]{#_Toc361387129}[]{#_Toc362011180}[]{#_Toc361387130}[]{#_Toc362011181}[]{#_Toc361387131}[]{#_Toc362011182}[]{#_Toc361387132}[]{#_Toc362011183}[]{#_Toc361387133}[]{#_Toc362011184}[]{#_Toc361387134}[]{#_Toc362011185}[]{#_Toc361387135}[]{#_Toc362011186}[]{#_Toc361387136}[]{#_Toc362011187}[]{#_Toc361387137}[]{#_Toc362011188}[]{#_Toc361387138}[]{#_Toc362011189}[]{#_Toc361387139}[]{#_Toc362011190}[]{#_Toc361387140}[]{#_Toc362011191}[]{#_Toc361387141}[]{#_Toc362011192}[]{#_Toc361387142}[]{#_Toc362011193}[]{#_Toc361387143}[]{#_Toc362011194}[]{#_Toc361387144}[]{#_Toc362011195}[]{#_Toc361387145}[]{#_Toc362011196}[]{#_Toc361387146}[]{#_Toc362011197}[]{#_Toc361387147}[]{#_Toc362011198}[]{#_Toc361387148}[]{#_Toc362011199}[]{#_Toc361387149}[]{#_Toc362011200}[]{#_Toc361387150}[]{#_Toc362011201}[]{#_Toc361387151}[]{#_Toc362011202}[]{#_Toc361387152}[]{#_Toc362011203}[]{#_Toc361387153}[]{#_Toc362011204}[]{#_Toc361387154}[]{#_Toc362011205}[]{#_Toc361387155}[]{#_Toc362011206}[]{#_Toc361387156}[]{#_Toc362011207}[]{#_Toc361387157}[]{#_Toc362011208}[]{#_Toc361387158}[]{#_Toc362011209}[]{#_Toc361387159}[]{#_Toc362011210}[]{#_Toc361387160}[]{#_Toc362011211}[]{#_Toc361387161}[]{#_Toc362011212}[]{#_Toc361387162}[]{#_Toc362011213}[]{#_Toc361387163}[]{#_Toc362011214}[]{#_Toc361387164}[]{#_Toc362011215}[]{#_Toc361387165}[]{#_Toc362011216}[]{#_Toc361387166}[]{#_Toc362011217}[]{#_Toc361387167}[]{#_Toc362011218}[]{#_Toc361387168}[]{#_Toc362011219}[]{#_Toc361387169}[]{#_Toc362011220}[]{#_Toc361387170}[]{#_Toc362011221}[]{#_Toc361387171}[]{#_Toc362011222}[]{#_Toc361387172}[]{#_Toc362011223}[]{#_Toc361387173}[]{#_Toc362011224}[]{#_Toc361387234}[]{#_Toc362011285}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 route-direct log**

------------------------------------------------------------------------

[**[display system internal ipv6 route-direct log]{lang="EN-US"}**]{#struct_0_20219_18486_x1434273459}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[直连路由日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1266275407}

[**[display system internal ipv6 route-direct ]{lang="EN-US"}**[{ **event** \| **notify** \| **nib** } **log** \[ **reverse** \]]{lang="EN-US"}]{#struct_0_20219_18486_1936027708}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1164031818}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_130336870}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1935962172}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_901381421}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x542378464}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x793379932}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_1051266157}[：接口事件相关日志。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_20219_18486_x567383628}[：接口事件通知相关日志。]{style="font-family:宋体"}

[**[nib]{lang="EN-US"}**]{#struct_0_20219_18486_x1874755887}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[直连路由]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块相关日志。]{style="font-family:宋体"}

[**[reverse]{lang="EN-US"}**]{#struct_0_20219_18486_x793445468}[：按时间新旧显示日志信息。]{style="font-family:宋体"}
:::

::: {#1845517874 .myid}
[]{#_Toc404799446}[]{#struct_0_20219_18486_x723089055}[]{#_Toc361832016}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table**

------------------------------------------------------------------------

[**[display system internal ipv6 routing-table]{lang="EN-US"}**]{#struct_0_20219_18486_x1606739485}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1195355099}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x290277734}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 routing-table ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] \[ **verbose** \] **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1505519077}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1375917497}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 routing-table ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] \[ **verbose** \] **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x217548442}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1786148698}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x723154591}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x31576481}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1771985619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_493828039}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x154927021}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_20219_18486_x1398291793}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_480753457}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_760603003}[：显示备份的指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x166983070}[：显示备份的指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x723482271}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_383838868}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-635316968 .myid}
[]{#_Toc404799447}[]{#struct_0_20219_18486_1602728216}[]{#_Toc361832017}[]{#_Toc292701679}[]{#_Toc251058587}[]{#_Toc138233421}[]{#_Toc135644122}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table acl**

------------------------------------------------------------------------

[**[display system internal ipv6 routing-table acl]{lang="EN-US"}**]{#struct_0_20219_18486_36620383}[命令用来显示通过指定]{style="font-family:
宋体"}[IPv6 ACL]{lang="EN-US"}[过滤的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_824876789}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_910956108}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **acl** *acl-number* \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x143346174}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1809099438}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **acl** *acl-number* \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_1715430359}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x723547807}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x385446755}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1339544029}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1873104944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x235618542}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_433096625}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_20219_18486_x1420290668}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1072874716}[：基本]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_1033899224}[：显示通过指定]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[过滤的所有路由的详细信息。如果未指定本参数，只显示通过]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[过滤的激活路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1246608302}[：显示备份的指定单板的通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x723351199}[：显示备份的指定成员设备的通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x37259864}[：显示备份的指定成员设备上通过指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x934388340}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-2080138517 .myid}
[]{#_Toc404799448}[]{#struct_0_20219_18486_x667711730}[]{#_Toc361832018}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table ipv6-address**

------------------------------------------------------------------------

[**[display system internal ipv6 routing-table ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_20219_18486_x992111106}[命令用来显示指定目的地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[display system internal ipv6 routing-table ]{lang="EN-US"}***[ipv6-address1 ]{lang="EN-US"}***[to]{lang="EN-US"}***[ ipv6-address2]{lang="EN-US"}*]{#struct_0_20219_18486_x816598777}[命令用来显示指定目的地址范围内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1627813721}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_735416490}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] *ip-address* \[ *mask* \| *mask-length* \] \[ **longer-match** \] \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x723416735}

[**[display system internal ipv6 routing-table ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] *ipv6-address1* **to** *ipv6-address2* \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_755701796}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1450976433}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] *ip-address* \[ *mask* \| *mask-length* \] \[ **longer-match** \] \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1641962714}

[**[display system internal ipv6 routing-table ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] *ipv6-address1* **to** *ipv6-address2* \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x365263205}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x441680269}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x253423214}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1128436919}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1228518875}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x631823465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x722695839}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_20219_18486_1981260743}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_20219_18486_353335224}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_20219_18486_1816524137}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[longer-match]{lang="EN-US"}**]{#struct_0_20219_18486_x1872374035}[：匹配并显示前缀最长的路由条目。]{style="font-family:宋体"}

[*[ipv6-address1]{lang="EN-US"}*[ **to** *ipv6-address2*]{lang="EN-US"}]{#struct_0_20219_18486_1287277782}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}*[ipv6-address1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[ipv6-address2]{lang="EN-US"}*[共同决定一个地址范围，只有地址在此范围内的路由才会被显示。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_x441789059}[：显示激活和未激活路由的详细信息。如果未指定本参数，将显示激活路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1845613855}[：显示备份的指定单板的指定目的地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_319529102}[：显示备份的指定成员设备的指定目的地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1671027536}[：显示备份的指定成员设备上指定目的地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x722761375}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#2098140676 .myid}
[]{#_Toc404799449}[]{#struct_0_20219_18486_x62556650}[]{#_Toc361832019}[]{#_Toc292701681}[]{#_Toc251058590}[]{#_Toc138233424}[]{#_Toc135644125}[]{#_Toc86723754}[]{#_Toc77992814}[]{#_Toc65740884}[]{#_Toc61239926}[]{#_Toc53707342}[]{#_Toc52486336}[]{#_Toc52008539}[]{#_Toc48417814}[]{#_Toc48409526}[]{#_Toc35941347}[]{#_Toc33866418}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table prefix-list**

------------------------------------------------------------------------

[**[display system internal ipv6 routing-table prefix-list]{lang="EN-US"}**]{#struct_0_20219_18486_1631590402}[命令用来显示通过指定前缀列表过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_49943671}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x67846935}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **prefix-list** *prefix-list-name* \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x234231536}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_1245605203}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **prefix-list** *prefix-list-name* \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_852420035}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1165708717}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x723220130}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1537999028}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x826457038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_2035322046}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1340346071}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_20219_18486_x1804269137}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_20219_18486_1020853491}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀列表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_x2006347600}[：显示所有路由的详细信息。如果未指定本参数，只显示激活路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x206848317}[：显示备份的指定单板的指定前缀列表过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1111451971}[：显示备份的指定成员设备的指定前缀列表过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x723285666}[：显示备份的指定成员设备上指定单板的指定前缀列表过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_388801246}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-145430185 .myid}
[]{#_Toc404799450}[]{#struct_0_20219_18486_1983481268}[]{#_Toc361832020}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table protocol**

------------------------------------------------------------------------

[**[display system internal ipv6 routing-table protocol]{lang="EN-US"}**]{#struct_0_20219_18486_1414589319}[命令用来显示指定协议生成或发现的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_568079552}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x399200743}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **protocol** *protocol* \[ **inactive** \| **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1870125697}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x223540129}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **protocol** *protocol* \[ **inactive** \| **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_2029388087}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1696648092}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x723089058}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1607067165}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1132729004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1834400521}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x104683357}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_20219_18486_x1009353460}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_20219_18486_1895034267}[：显示指定路由协议的信息，包括]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[inactive]{lang="EN-US"}**]{#struct_0_20219_18486_x752014561}[：如果配置了该参数，此命令只显示未激活路由信息。如果未指定本参数，将显示所有激活和未激活路由信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_x934404298}[：显示激活和未激活路由的详细信息。如果未指定本参数，将显示路由的概要信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1410002898}[：显示备份的指定单板的指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由协议的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x723154594}[：显示备份的指定成员设备的指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由协议的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x31773089}[：显示备份的指定成员设备上指定单板的指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由协议的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x781921591}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#840269214 .myid}
[]{#_Toc404799451}[]{#struct_0_20219_18486_1776073200}[]{#_Toc361832021}[]{#_Toc283297032}[]{#_Toc251058592}[]{#_Toc138233426}[]{#_Toc135644127}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal ipv6 routing-table statistics**

------------------------------------------------------------------------

[**[display system internal ipv6 routing-table statistics]{lang="EN-US"}**]{#struct_0_20219_18486_x1124095583}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中的综合路由统计信息。综合路由统计信息包括路由总数、增加的路由数、删除的路由数等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_643660393}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_234121994}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **statistics** **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1466806142}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x348436571}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal ipv6 routing-table]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **statistics** **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1986374223}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x723482274}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_383511188}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1961715753}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x283904365}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1772349515}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x836010207}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_20219_18486_x2131369553}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_637867119}[：显示备份的指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中的综合路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_569221562}[：显示备份的指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中的综合路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1929271879}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中的综合路由统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_700837387}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1717220490 .myid}
[]{#_Toc404799452}[]{#struct_0_20219_18486_x723547810}[]{#_Toc361832023}[]{#_Toc343698422}[]{#_Toc340320592}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib attribute**

------------------------------------------------------------------------

[**[display system internal rib attribute]{lang="EN-US"}**]{#struct_0_20219_18486_x385905508}[命令用来显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的路由属性信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x2134143914}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x2017945203}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rib attribute]{lang="EN-US"}**[ \[ *attribute-id* \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1692126401}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1911462550}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal rib attribute ]{lang="EN-US"}**[\[ *attribute-id* \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_483369446}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_485109360}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1516876349}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_661450070}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x723351202}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1919514033}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1262343917}

[*[attribute-id]{lang="EN-US"}*]{#struct_0_20219_18486_x870207039}[：路由属性]{style="font-family:宋体"}[ID]{lang="EN-US"}[值，取值范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1166952673}[：显示备份的指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由属性信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1496005598}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由属性信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x2058766731}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由属性信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_353081408}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1282651049 .myid}
[]{#_Toc404799453}[]{#struct_0_20219_18486_440136985}[]{#_Toc361387236}[]{#_Toc362011287}[]{#_Toc361387237}[]{#_Toc362011288}[]{#_Toc361387238}[]{#_Toc362011289}[]{#_Toc361387239}[]{#_Toc362011290}[]{#_Toc361387240}[]{#_Toc362011291}[]{#_Toc361387241}[]{#_Toc362011292}[]{#_Toc361387242}[]{#_Toc362011293}[]{#_Toc361387243}[]{#_Toc362011294}[]{#_Toc361387244}[]{#_Toc362011295}[]{#_Toc361387245}[]{#_Toc362011296}[]{#_Toc361387246}[]{#_Toc362011297}[]{#_Toc361387247}[]{#_Toc362011298}[]{#_Toc361387248}[]{#_Toc362011299}[]{#_Toc361387249}[]{#_Toc362011300}[]{#_Toc361387250}[]{#_Toc362011301}[]{#_Toc361387251}[]{#_Toc362011302}[]{#_Toc361387252}[]{#_Toc362011303}[]{#_Toc361387253}[]{#_Toc362011304}[]{#_Toc361387254}[]{#_Toc362011305}[]{#_Toc361387255}[]{#_Toc362011306}[]{#_Toc361387256}[]{#_Toc362011307}[]{#_Toc361387257}[]{#_Toc362011308}[]{#_Toc361387258}[]{#_Toc362011309}[]{#_Toc361387259}[]{#_Toc362011310}[]{#_Toc361387260}[]{#_Toc362011311}[]{#_Toc361387261}[]{#_Toc362011312}[]{#_Toc361387262}[]{#_Toc362011313}[]{#_Toc361387263}[]{#_Toc362011314}[]{#_Toc361387264}[]{#_Toc362011315}[]{#_Toc361387319}[]{#_Toc362011370}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event attribute**

------------------------------------------------------------------------

[**[display system internal rib event attribute]{lang="EN-US"}**]{#struct_0_20219_18486_x1439971207}[命令用来显示]{style="font-family:宋体"}[IPv4 RIB]{lang="EN-US"}[的路由属性事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x548321632}

[**[display system internal rib event attribute]{lang="EN-US"}**]{#struct_0_20219_18486_1382385060}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1628717414}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1808324732}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1936598160}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x15550134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x793117790}
:::

::: {#-1749794466 .myid}
[]{#_Toc404799454}[]{#struct_0_20219_18486_1886221441}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event policy**

------------------------------------------------------------------------

[**[display system internal rib event policy]{lang="EN-US"}**]{#struct_0_20219_18486_x356786842}[命令用来显示]{style="font-family:宋体"}[IPv4 RIB]{lang="EN-US"}[的路由策略事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x95275258}

[**[display system internal rib event policy]{lang="EN-US"}**]{#struct_0_20219_18486_1150814590}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x773893724}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1109096351}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1886286977}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1002070251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_89727981}
:::

::: {#-1186607259 .myid}
[]{#_Toc404799455}[]{#struct_0_20219_18486_268766425}[]{#_Toc340320604}[]{#_Toc361387321}[]{#_Toc362011372}[]{#_Toc361387322}[]{#_Toc362011373}[]{#_Toc361387323}[]{#_Toc362011374}[]{#_Toc361387324}[]{#_Toc362011375}[]{#_Toc361387325}[]{#_Toc362011376}[]{#_Toc361387326}[]{#_Toc362011377}[]{#_Toc361387327}[]{#_Toc362011378}[]{#_Toc361387328}[]{#_Toc362011379}[]{#_Toc361387329}[]{#_Toc362011380}[]{#_Toc361387330}[]{#_Toc362011381}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event prefix**

------------------------------------------------------------------------

[**[display system internal rib notificaion prefix]{lang="EN-US"}**]{#struct_0_20219_18486_1425983442}[命令用来显示]{style="font-family:宋体"}[IPv4 RIB]{lang="EN-US"}[的路由前缀事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_543985806}

[**[display system internal rib event prefix]{lang="EN-US"}**]{#struct_0_20219_18486_x1554929787}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x499814325}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1285290263}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x746424394}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x553435414}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_753249154}
:::

::: {#-1258323415 .myid}
[]{#_Toc404799456}[]{#struct_0_20219_18486_x2097234402}[]{#_Toc340320602}[]{#_Toc361387332}[]{#_Toc362011383}[]{#_Toc361387333}[]{#_Toc362011384}[]{#_Toc361387334}[]{#_Toc362011385}[]{#_Toc361387335}[]{#_Toc362011386}[]{#_Toc361387336}[]{#_Toc362011387}[]{#_Toc361387337}[]{#_Toc362011388}[]{#_Toc361387338}[]{#_Toc362011389}[]{#_Toc361387339}[]{#_Toc362011390}[]{#_Toc361387340}[]{#_Toc362011391}[]{#_Toc361387341}[]{#_Toc362011392}[]{#_Toc361387342}[]{#_Toc362011393}[]{#_Toc361387343}[]{#_Toc362011394}[]{#_Toc361387344}[]{#_Toc362011395}[]{#_Toc361387345}[]{#_Toc362011396}[]{#_Toc361387346}[]{#_Toc362011397}[]{#_Toc361387347}[]{#_Toc362011398}[]{#_Toc361387348}[]{#_Toc362011399}[]{#_Toc361387349}[]{#_Toc362011400}[]{#表NBR_4}[]{#表prefix}[]{#_Toc361387350}[]{#_Toc362011401}[]{#_Toc361387387}[]{#_Toc362011438}[]{#_Toc361387389}[]{#_Toc362011440}[]{#_Toc361387390}[]{#_Toc362011441}[]{#_Toc361387391}[]{#_Toc362011442}[]{#_Toc361387392}[]{#_Toc362011443}[]{#_Toc361387393}[]{#_Toc362011444}[]{#_Toc361387394}[]{#_Toc362011445}[]{#_Toc361387395}[]{#_Toc362011446}[]{#_Toc361387396}[]{#_Toc362011447}[]{#_Toc361387397}[]{#_Toc362011448}[]{#_Toc361387398}[]{#_Toc362011449}[]{#_Toc361387399}[]{#_Toc362011450}[]{#_Toc361387400}[]{#_Toc362011451}[]{#_Toc361387401}[]{#_Toc362011452}[]{#_Toc361387402}[]{#_Toc362011453}[]{#_Toc361387403}[]{#_Toc362011454}[]{#_Toc361387404}[]{#_Toc362011455}[]{#_Toc361387405}[]{#_Toc362011456}[]{#_Toc361387427}[]{#_Toc362011478}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event protocol**

------------------------------------------------------------------------

[**[display system internal rib event protocol]{lang="EN-US"}**]{#struct_0_20219_18486_x214836553}[命令用来显示]{style="font-family:宋体"}[IPv4 RIB]{lang="EN-US"}[的协议事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1124973650}

[**[display system internal rib event protocol ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_20219_18486_x533622641}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x793248861}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1832353956}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_480741846}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1134212165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_2293397}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1154923815}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x602290662}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-851396999 .myid}
[]{#_Toc404799457}[]{#struct_0_20219_18486_x1347923292}[]{#_Toc340320610}[]{#_Toc361387429}[]{#_Toc362011480}[]{#_Toc361387430}[]{#_Toc362011481}[]{#_Toc361387431}[]{#_Toc362011482}[]{#_Toc361387432}[]{#_Toc362011483}[]{#_Toc361387433}[]{#_Toc362011484}[]{#_Toc361387434}[]{#_Toc362011485}[]{#_Toc361387435}[]{#_Toc362011486}[]{#_Toc361387436}[]{#_Toc362011487}[]{#_Toc361387437}[]{#_Toc362011488}[]{#_Toc361387438}[]{#_Toc362011489}[]{#_Toc361387439}[]{#_Toc362011490}[]{#_Toc361387440}[]{#_Toc362011491}[]{#_Toc361387441}[]{#_Toc362011492}[]{#_Toc361387442}[]{#_Toc362011493}[]{#_Toc361387467}[]{#_Toc362011518}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib event statistics**

------------------------------------------------------------------------

[**[display system internal rib event statistics]{lang="EN-US"}**]{#struct_0_20219_18486_x924096953}[用来显示]{style="font-family:宋体"}[IPv4 RIB]{lang="EN-US"}[的统计事件信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x340650183}

[**[display system internal rib event statistics]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_20219_18486_x793445472}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x215579652}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_703464128}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x2111273524}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_122946295}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1560943757}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1090473864}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x962220348}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1964687443 .myid}
[]{#_Toc336358570}[]{#_Toc340320612}[]{#_Toc404799458}[]{#struct_0_20219_18486_975123204}[]{#_Toc361387469}[]{#_Toc362011520}[]{#_Toc361387470}[]{#_Toc362011521}[]{#_Toc361387471}[]{#_Toc362011522}[]{#_Toc361387472}[]{#_Toc362011523}[]{#_Toc361387473}[]{#_Toc362011524}[]{#_Toc361387474}[]{#_Toc362011525}[]{#_Toc361387475}[]{#_Toc362011526}[]{#_Toc361387476}[]{#_Toc362011527}[]{#_Toc361387477}[]{#_Toc362011528}[]{#_Toc361387478}[]{#_Toc362011529}[]{#_Toc361387479}[]{#_Toc362011530}[]{#_Toc361387480}[]{#_Toc362011531}[]{#_Toc361387481}[]{#_Toc362011532}[]{#_Toc361387482}[]{#_Toc362011533}[]{#_Toc361387483}[]{#_Toc362011534}[]{#_Toc361387484}[]{#_Toc362011535}[]{#_Toc361387485}[]{#_Toc362011536}[]{#_Toc361387486}[]{#_Toc362011537}[]{#_Toc361387487}[]{#_Toc362011538}[]{#_Toc361387488}[]{#_Toc362011539}[]{#_Toc361387489}[]{#_Toc362011540}[]{#_Toc361387490}[]{#_Toc362011541}[]{#_Toc361387491}[]{#_Toc362011542}[]{#_Toc361387492}[]{#_Toc362011543}[]{#_Toc361387493}[]{#_Toc362011544}[]{#_Toc361387494}[]{#_Toc362011545}[]{#_Toc361387495}[]{#_Toc362011546}[]{#_Toc361387496}[]{#_Toc362011547}[]{#_Toc361387497}[]{#_Toc362011548}[]{#_Toc361387498}[]{#_Toc362011549}[]{#_Toc361387499}[]{#_Toc362011550}[]{#_Toc361387500}[]{#_Toc362011551}[]{#_Toc361387501}[]{#_Toc362011552}[]{#_Toc361387502}[]{#_Toc362011553}[]{#_Toc361387503}[]{#_Toc362011554}[]{#_Toc361387504}[]{#_Toc362011555}[]{#_Toc361387505}[]{#_Toc362011556}[]{#_Toc361387506}[]{#_Toc362011557}[]{#_Toc361387507}[]{#_Toc362011558}[]{#_Toc361387508}[]{#_Toc362011559}[]{#_Toc361387509}[]{#_Toc362011560}[]{#_Toc361387510}[]{#_Toc362011561}[]{#_Toc361387511}[]{#_Toc362011562}[]{#_Toc361387623}[]{#_Toc362011674}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib ftn**

------------------------------------------------------------------------

[**[display system internal rib ftn]{lang="EN-US"}**]{#struct_0_20219_18486_2036546648}[命令用来显示]{style="font-family:宋体"}[FTN]{lang="EN-US"}[表项和统计计数信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_772966153}

[**[display system internal rib ftn]{lang="EN-US"}**[ \[ *index* \] \[ **statistics** \]]{lang="EN-US"}]{#struct_0_20219_18486_329092561}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1620880598}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_772900617}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1510027558}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_274954692}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1451039223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x227820705}

[*[index]{lang="EN-US"}*]{#struct_0_20219_18486_1430651356}[：显示指定]{style="font-family:宋体"}[FTN]{lang="EN-US"}[索引的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[index]{lang="EN-US"}*[为]{style="font-family:宋体"}[FTN]{lang="EN-US"}[索引值，为十六进制数，最高位统一设置为]{style="font-family:宋体"}[1]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[FTN]{lang="EN-US"}[索引的]{style="font-family:宋体"}[FTN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_20219_18486_773228297}[：显示]{style="font-family:宋体"}[FTN]{lang="EN-US"}[统计计数信息。]{style="font-family:宋体"}
:::

::: {#1532656974 .myid}
[]{#_Toc404799459}[]{#struct_0_20219_18486_975123202}[]{#_Toc349986725}[]{#_Toc343688316}[]{#_Toc361387625}[]{#_Toc362011676}[]{#_Toc361387626}[]{#_Toc362011677}[]{#_Toc361387627}[]{#_Toc362011678}[]{#_Toc361387628}[]{#_Toc362011679}[]{#_Toc361387629}[]{#_Toc362011680}[]{#_Toc361387630}[]{#_Toc362011681}[]{#_Toc361387631}[]{#_Toc362011682}[]{#_Toc361387632}[]{#_Toc362011683}[]{#_Toc361387633}[]{#_Toc362011684}[]{#_Toc361387634}[]{#_Toc362011685}[]{#_Toc361387635}[]{#_Toc362011686}[]{#_Toc361387636}[]{#_Toc362011687}[]{#_Toc361387637}[]{#_Toc362011688}[]{#_Toc361387638}[]{#_Toc362011689}[]{#_Toc361387639}[]{#_Toc362011690}[]{#_Toc361387640}[]{#_Toc362011691}[]{#_Toc361387641}[]{#_Toc362011692}[]{#_Toc361387642}[]{#_Toc362011693}[]{#_Toc361387643}[]{#_Toc362011694}[]{#_Toc361387644}[]{#_Toc362011695}[]{#_Toc361387645}[]{#_Toc362011696}[]{#_Toc361387646}[]{#_Toc362011697}[]{#_Toc361387647}[]{#_Toc362011698}[]{#_Toc361387648}[]{#_Toc362011699}[]{#_Toc361387649}[]{#_Toc362011700}[]{#_Toc361387650}[]{#_Toc362011701}[]{#_Toc361387651}[]{#_Toc362011702}[]{#_Toc361387652}[]{#_Toc362011703}[]{#_Toc361387653}[]{#_Toc362011704}[]{#_Toc361387681}[]{#_Toc362011732}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib ftn summary**

------------------------------------------------------------------------

[**[display system internal rib ftn summary]{lang="EN-US"}**]{#struct_0_20219_18486_x513386953}[命令用来显示]{style="font-family:宋体"}[FTN]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_772966151}

[**[display system internal rib ftn summary]{lang="EN-US"}**]{#struct_0_20219_18486_329092559}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_46902494}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_772900615}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1510027560}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_275478981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_772835079}
:::

::: {#41914380 .myid}
[]{#_Toc404799460}[]{#struct_0_20219_18486_x2137624053}[]{#_Toc361387683}[]{#_Toc362011734}[]{#_Toc361387684}[]{#_Toc362011735}[]{#_Toc361387685}[]{#_Toc362011736}[]{#_Toc361387686}[]{#_Toc362011737}[]{#_Toc361387687}[]{#_Toc362011738}[]{#_Toc361387688}[]{#_Toc362011739}[]{#_Toc361387689}[]{#_Toc362011740}[]{#_Toc361387690}[]{#_Toc362011741}[]{#_Toc361387691}[]{#_Toc362011742}[]{#_Toc361387692}[]{#_Toc362011743}[]{#_Toc361387693}[]{#_Toc362011744}[]{#_Toc361387694}[]{#_Toc362011745}[]{#_Toc361387695}[]{#_Toc362011746}[]{#_Toc361387696}[]{#_Toc362011747}[]{#_Toc361387697}[]{#_Toc362011748}[]{#_Toc361387698}[]{#_Toc362011749}[]{#_Toc361387699}[]{#_Toc362011750}[]{#_Toc361387700}[]{#_Toc362011751}[]{#_Toc361387701}[]{#_Toc362011752}[]{#_Toc361387702}[]{#_Toc362011753}[]{#_Toc361387703}[]{#_Toc362011754}[]{#_Toc361387704}[]{#_Toc362011755}[]{#_Toc361387756}[]{#_Toc362011807}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib log**

------------------------------------------------------------------------

[**[display system internal rib log]{lang="EN-US"}**]{#struct_0_20219_18486_x581126620}[命令用来显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_772638470}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_511788940}

[**[display system internal rib log]{lang="EN-US"}**[ \[ **reverse** \]]{lang="EN-US"}]{#struct_0_20219_18486_x1021697290}

[**[display system internal rib event log]{lang="EN-US"}**]{#struct_0_20219_18486_1574309025}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_772572934}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal rib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_975123203}

[**[dis]{lang="EN-US"}[play system internal rib event log]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_772507398}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x140806094}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal rib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_772966150}

[**[dis]{lang="EN-US"}[play system internal rib event log]{lang="EN-US"}**[ \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_772900614}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1510027559}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_275020228}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1992413409}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x171844350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_846386538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1708569948}

[**[rib]{lang="EN-US"}**]{#struct_0_20219_18486_x1438630731}[：显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_772835078}[：显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由变化通知的日志信息。]{style="font-family:宋体"}

[**[reverse]{lang="EN-US"}**]{#struct_0_20219_18486_1113332224}[：按时间新旧显示日志信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_53615636}[：显示备份的指定单板]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_772769542}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x227820700}[：显示备份的指定成员设备上]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的日志信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_473476390}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#101486676 .myid}
[]{#_Toc404799461}[]{#struct_0_20219_18486_x1479550818}[]{#_Toc361387758}[]{#_Toc362011809}[]{#_Toc361387759}[]{#_Toc362011810}[]{#_Toc361387760}[]{#_Toc362011811}[]{#_Toc361387761}[]{#_Toc362011812}[]{#_Toc361387762}[]{#_Toc362011813}[]{#_Toc361387763}[]{#_Toc362011814}[]{#_Toc361387764}[]{#_Toc362011815}[]{#_Toc361387765}[]{#_Toc362011816}[]{#_Toc361387766}[]{#_Toc362011817}[]{#_Toc361387767}[]{#_Toc362011818}[]{#_Toc361387768}[]{#_Toc362011819}[]{#_Toc361387769}[]{#_Toc362011820}[]{#_Toc361387791}[]{#_Toc362011842}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib memory**

------------------------------------------------------------------------

[**[display system internal rib memory]{lang="EN-US"}**]{#struct_0_20219_18486_x198894465}[命令用来显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的内存信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1746860307}

[**[display system internal rib memory]{lang="EN-US"}**]{#struct_0_20219_18486_x1600014522}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1845551549}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1858123722}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x613497057}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x201570500}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1281093955}
:::

::: {#-717469433 .myid}
[]{#_Toc404799462}[]{#struct_0_20219_18486_x723482273}[]{#_Toc361832025}[]{#_Toc343698424}[]{#_Toc340320594}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib nib**

------------------------------------------------------------------------

[**[display system internal rib nib]{lang="EN-US"}**]{#struct_0_20219_18486_383969940}[命令用来显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_42351896}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_162804983}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rib nib ]{lang="EN-US"}**[\[ **self-originated** \] \[ *nib-id* \] \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_470437205}

[**[display system internal ]{lang="EN-US"}[rib nib protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*[ \[ **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x723547809}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x385315683}[模式：]{style="font-family:宋体"}

[**[display system internal ]{lang="EN-US"}[rib nib ]{lang="EN-US"}**[\[ **self-originated** \] \[ *nib-id* \] \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_580815768}

[**[display system internal ]{lang="EN-US"}[rib nib protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*[ \[ **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x202215264}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_719665089}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1931985416}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x70440491}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1811102770}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_2112363699}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_832674359}

[**[self-originated]{lang="EN-US"}**]{#struct_0_20219_18486_x1966363858}[：路由管理自己生成的下一跳信息。]{style="font-family:宋体"}

[*[nib-id]{lang="EN-US"}*]{#struct_0_20219_18486_x723351201}[：路由下一跳信息的]{style="font-family:宋体"}[ID]{lang="EN-US"}[值，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20219_18486_1919579569}[：显示详细信息。如果未指定本参数，则显示概要信息。]{style="font-family:宋体"}

[**[protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*]{#struct_0_20219_18486_2047816889}[：显示指定路由协议生成的下一跳信息，包括]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1484293453}[：显示备份的指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[下一跳信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x973725029}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[下一跳信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_850616437}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[下一跳信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_524095492}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-658985157 .myid}
[]{#_Toc340320598}[]{#_Toc404799463}[]{#struct_0_20219_18486_918977496}[]{#_Toc340320614}[]{#_Toc336358572}[]{#_Toc361387793}[]{#_Toc362011844}[]{#_Toc361387794}[]{#_Toc362011845}[]{#_Toc361387795}[]{#_Toc362011846}[]{#_Toc361387796}[]{#_Toc362011847}[]{#_Toc361387797}[]{#_Toc362011848}[]{#_Toc361387798}[]{#_Toc362011849}[]{#_Toc361387799}[]{#_Toc362011850}[]{#_Toc361387800}[]{#_Toc362011851}[]{#_Toc361387801}[]{#_Toc362011852}[]{#_Toc361387802}[]{#_Toc362011853}[]{#_Toc361387803}[]{#_Toc362011854}[]{#_Toc361387804}[]{#_Toc362011855}[]{#_Toc361387805}[]{#_Toc362011856}[]{#_Toc361387806}[]{#_Toc362011857}[]{#_Toc361387807}[]{#_Toc362011858}[]{#_Toc361387808}[]{#_Toc362011859}[]{#_Toc361387809}[]{#_Toc362011860}[]{#_Toc361387810}[]{#_Toc362011861}[]{#_Toc361387811}[]{#_Toc362011862}[]{#_Toc361387812}[]{#_Toc362011863}[]{#_Toc361387813}[]{#_Toc362011864}[]{#_Toc361387814}[]{#_Toc362011865}[]{#_Toc361387815}[]{#_Toc362011866}[]{#_Toc361387816}[]{#_Toc362011867}[]{#_Toc361387817}[]{#_Toc362011868}[]{#_Toc361387818}[]{#_Toc362011869}[]{#_Toc361387843}[]{#_Toc362011894}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib nib log**

------------------------------------------------------------------------

[**[display system internal rib nib log]{lang="EN-US"}**]{#struct_0_20219_18486_x2021499710}[命令用来显示系统内部]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块运行状态的日志记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1854206818}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_x1599817914}

[**[display system internal rib nib log]{lang="EN-US"}**[ \[ **reverse** \]]{lang="EN-US"}]{#struct_0_20219_18486_x1242712519}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_429239072}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rib nib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1599883450}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1599424698}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal rib nib log]{lang="EN-US"}**[ \[ **reverse** \] \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_2099777579}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_814334125}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_2066666078}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1599490234}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_104882854}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x2080905302}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_233473766}

[**[nib]{lang="EN-US"}**]{#struct_0_20219_18486_1435216560}[：显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态。]{style="font-family:宋体"}

[**[reverse]{lang="EN-US"}**]{#struct_0_20219_18486_x1228526551}[：按时间新旧显示日志信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1599948985}[：显示备份的指定单板]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1519863627}[：显示备份的指定成员设备的]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1812421043}[：显示备份的指定成员设备上]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块的运行状态日志。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1482838752}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#588508660 .myid}
[]{#_Toc404799464}[]{#struct_0_20219_18486_223784378}[]{#_Toc361387845}[]{#_Toc362011896}[]{#_Toc361387846}[]{#_Toc362011897}[]{#_Toc361387847}[]{#_Toc362011898}[]{#_Toc361387848}[]{#_Toc362011899}[]{#_Toc361387849}[]{#_Toc362011900}[]{#_Toc361387850}[]{#_Toc362011901}[]{#_Toc361387851}[]{#_Toc362011902}[]{#_Toc361387852}[]{#_Toc362011903}[]{#_Toc361387853}[]{#_Toc362011904}[]{#_Toc361387854}[]{#_Toc362011905}[]{#_Toc361387855}[]{#_Toc362011906}[]{#_Toc361387856}[]{#_Toc362011907}[]{#_Toc361387857}[]{#_Toc362011908}[]{#_Toc361387858}[]{#_Toc362011909}[]{#_Toc361387859}[]{#_Toc362011910}[]{#_Toc361387860}[]{#_Toc362011911}[]{#_Toc361387861}[]{#_Toc362011912}[]{#_Toc361387862}[]{#_Toc362011913}[]{#_Toc361387863}[]{#_Toc362011914}[]{#_Toc361387864}[]{#_Toc362011915}[]{#_Toc361387865}[]{#_Toc362011916}[]{#_Toc361387866}[]{#_Toc362011917}[]{#_Toc361387867}[]{#_Toc362011918}[]{#_Toc361387868}[]{#_Toc362011919}[]{#_Toc361387869}[]{#_Toc362011920}[]{#_Toc361387870}[]{#_Toc362011921}[]{#_Toc361387934}[]{#_Toc362011985}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib prefix**

------------------------------------------------------------------------

[**[display system internal rib prefix]{lang="EN-US"}**]{#struct_0_20219_18486_x1600014524}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表前缀信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1642846693}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1781369896}

[**[display system internal rib prefix ]{lang="EN-US"}***[ip-address mask-length]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1316534450}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x1600080060}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rib prefix ]{lang="EN-US"}***[ip-address mask-length]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \] \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1600145596}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1924714986}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal rib prefix ]{lang="EN-US"}***[ip-address mask-length]{lang="EN-US"}*[ \[ **vpn-instance** *vpn-instance-name* \] \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1599686844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1208970901}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_293486900}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1076414513}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1760238499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1444592255}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1599752380}

[*[ip-address]{lang="EN-US"}*]{#struct_0_20219_18486_628933591}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[目的地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_20219_18486_x289955760}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_2079296592}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1832131601}[：显示备份的指定单板]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表前缀信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表前缀信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1599817916}[：显示备份的指定成员设备的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表前缀信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表前缀信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x79913105}[：显示备份的指定成员设备上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表前缀信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表前缀信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1482838758}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-262550734 .myid}
[]{#_Toc404799465}[]{#struct_0_20219_18486_x1600145595}[]{#_Toc340320600}[]{#_Toc361387936}[]{#_Toc362011987}[]{#_Toc361387937}[]{#_Toc362011988}[]{#_Toc361387938}[]{#_Toc362011989}[]{#_Toc361387939}[]{#_Toc362011990}[]{#_Toc361387940}[]{#_Toc362011991}[]{#_Toc361387941}[]{#_Toc362011992}[]{#_Toc361387942}[]{#_Toc362011993}[]{#_Toc361387943}[]{#_Toc362011994}[]{#_Toc361387944}[]{#_Toc362011995}[]{#_Toc361387945}[]{#_Toc362011996}[]{#_Toc361387946}[]{#_Toc362011997}[]{#_Toc361387947}[]{#_Toc362011998}[]{#_Toc361387948}[]{#_Toc362011999}[]{#_Toc361387949}[]{#_Toc362012000}[]{#_Toc361387950}[]{#_Toc362012001}[]{#_Toc361387988}[]{#_Toc362012039}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal rib summary**

------------------------------------------------------------------------

[**[display system internal rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_x1599686843}[命令用来显示]{style="font-family:宋体"}[IPv4 RIB]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1968485788}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_x1599752379}

[**[display system internal rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_x1744702444}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_239534312}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rib summary]{lang="EN-US"}**[ \[ **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1599817915}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1599883451}[模式：]{style="font-family:宋体"}

[**[dis]{lang="EN-US"}[play system internal rib summary]{lang="EN-US"}**[ \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1599424699}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_533693638}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1819403822}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x888666402}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1954206}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1075660648}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1599490235}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1670966795}[：显示备份的指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1599948990}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1600014526}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIB]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1482838756}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#197469962 .myid}
[]{#_Toc336358578}[]{#_Toc340320620}[]{#_Toc404799466}[]{#struct_0_20219_18486_1101368808}[]{#_Toc348956700}[]{#_Toc337653101}[]{#_Toc361387990}[]{#_Toc362012041}[]{#_Toc361387991}[]{#_Toc362012042}[]{#_Toc361387992}[]{#_Toc362012043}[]{#_Toc361387993}[]{#_Toc362012044}[]{#_Toc361387994}[]{#_Toc362012045}[]{#_Toc361387995}[]{#_Toc362012046}[]{#_Toc361387996}[]{#_Toc362012047}[]{#_Toc361387997}[]{#_Toc362012048}[]{#_Toc361387998}[]{#_Toc362012049}[]{#_Toc361387999}[]{#_Toc362012050}[]{#_Toc361388000}[]{#_Toc362012051}[]{#_Toc361388001}[]{#_Toc362012052}[]{#_Toc361388002}[]{#_Toc362012053}[]{#_Toc361388003}[]{#_Toc362012054}[]{#_Toc361388004}[]{#_Toc362012055}[]{#_Toc361388005}[]{#_Toc362012056}[]{#_Toc361388006}[]{#_Toc362012057}[]{#_Toc361388007}[]{#_Toc362012058}[]{#_Toc361388008}[]{#_Toc362012059}[]{#_Toc361388009}[]{#_Toc362012060}[]{#_Toc361388010}[]{#_Toc362012061}[]{#_Toc361388011}[]{#_Toc362012062}[]{#_Toc361388012}[]{#_Toc362012063}[]{#_Toc361388013}[]{#_Toc362012064}[]{#_Toc361388014}[]{#_Toc362012065}[]{#_Toc361388015}[]{#_Toc362012066}[]{#_Toc361388016}[]{#_Toc362012067}[]{#_Toc361388017}[]{#_Toc362012068}[]{#_Toc361388018}[]{#_Toc362012069}[]{#_Toc361388019}[]{#_Toc362012070}[]{#_Toc361388020}[]{#_Toc362012071}[]{#_Toc361388021}[]{#_Toc362012072}[]{#_Toc361388022}[]{#_Toc362012073}[]{#_Toc361388023}[]{#_Toc362012074}[]{#_Toc361388024}[]{#_Toc362012075}[]{#_Toc361388025}[]{#_Toc362012076}[]{#_Toc361388026}[]{#_Toc362012077}[]{#_Toc361388027}[]{#_Toc362012078}[]{#_Toc361388028}[]{#_Toc362012079}[]{#_Toc361388122}[]{#_Toc362012173}[]{#_display_system_internel}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal route-direct interface**

------------------------------------------------------------------------

[**[display system internal route-direct interface]{lang="EN-US"}**]{#struct_0_20219_18486_763749080}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址接口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1148585296}

[**[display system internal route-direct interface]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } \]]{lang="EN-US"}]{#struct_0_20219_18486_x813028374}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x63080818}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1555265546}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_858005507}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x2018584570}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x33930581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1219192020}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x1124890399}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1293226919}[：接口类型和接口编号。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_20219_18486_x803363980}[：接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制，显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和掩码]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码长度接口的信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_20219_18486_x1311015826}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_20219_18486_x752347012}[：掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}
:::

::: {#-998045671 .myid}
[]{#_Toc336358579}[]{#_Toc340320621}[]{#_Toc340320634}[]{#_Toc337653098}[]{#_Toc404799467}[]{#struct_0_20219_18486_x34061652}[]{#_Toc350345686}[]{#_Toc340320645}[]{#_Toc337653103}[]{#_Toc361388124}[]{#_Toc362012175}[]{#_Toc361388125}[]{#_Toc362012176}[]{#_Toc361388126}[]{#_Toc362012177}[]{#_Toc361388127}[]{#_Toc362012178}[]{#_Toc361388128}[]{#_Toc362012179}[]{#_Toc361388129}[]{#_Toc362012180}[]{#_Toc361388130}[]{#_Toc362012181}[]{#_Toc361388131}[]{#_Toc362012182}[]{#_Toc361388132}[]{#_Toc362012183}[]{#_Toc361388133}[]{#_Toc362012184}[]{#_Toc361388134}[]{#_Toc362012185}[]{#_Toc361388135}[]{#_Toc362012186}[]{#_Toc361388136}[]{#_Toc362012187}[]{#_Toc361388137}[]{#_Toc362012188}[]{#_Toc361388138}[]{#_Toc362012189}[]{#_Toc361388139}[]{#_Toc362012190}[]{#_Toc361388140}[]{#_Toc362012191}[]{#_Toc361388141}[]{#_Toc362012192}[]{#_Toc361388142}[]{#_Toc362012193}[]{#_Toc361388143}[]{#_Toc362012194}[]{#_Toc361388144}[]{#_Toc362012195}[]{#_Toc361388145}[]{#_Toc362012196}[]{#_Toc361388146}[]{#_Toc362012197}[]{#_Toc361388147}[]{#_Toc362012198}[]{#_Toc361388148}[]{#_Toc362012199}[]{#_Toc361388149}[]{#_Toc362012200}[]{#_Toc361388150}[]{#_Toc362012201}[]{#_Toc361388151}[]{#_Toc362012202}[]{#_Toc361388152}[]{#_Toc362012203}[]{#_Toc361388153}[]{#_Toc362012204}[]{#_Toc361388154}[]{#_Toc362012205}[]{#_Toc361388155}[]{#_Toc362012206}[]{#_Toc361388156}[]{#_Toc362012207}[]{#_Toc361388157}[]{#_Toc362012208}[]{#_Toc361388158}[]{#_Toc362012209}[]{#_Toc361388159}[]{#_Toc362012210}[]{#_Toc361388160}[]{#_Toc362012211}[]{#_Toc361388161}[]{#_Toc362012212}[]{#_Toc361388222}[]{#_Toc362012273}

**IP路由基础 \-- IP路由基础Probe命令 \-- display system internal route-direct log**

------------------------------------------------------------------------

[**[display system internal route-direct log]{lang="EN-US"}**]{#struct_0_20219_18486_x33602900}[命令用来显示直连路由日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1453125140}

[**[display system internal route-direct ]{lang="EN-US"}**[{ **event** \| **notify** \| **nib** } **log** \[ **reverse** \]]{lang="EN-US"}]{#struct_0_20219_18486_x33668436}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1301942379}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x33733972}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_138023537}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x33799508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x33340756}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_20219_18486_1606856}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_x33406292}[：接口事件相关日志。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_20219_18486_x1662465305}[：接口事件通知相关日志。]{style="font-family:宋体"}

[**[nib]{lang="EN-US"}**]{#struct_0_20219_18486_x33865047}[：直连路由]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块相关日志。]{style="font-family:宋体"}

[**[reverse]{lang="EN-US"}**]{#struct_0_20219_18486_763749078}[：按时间新旧显示日志信息。]{style="font-family:宋体"}
:::

::: {#-340994124 .myid}
[]{#_Toc404799468}[]{#struct_0_20219_18486_1183916477}[]{#_Toc365035785}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ip routing-table statistics protocol**

------------------------------------------------------------------------

[**[reset system internal ip routing-table statistics protocol]{lang="EN-US"}**]{#struct_0_20219_18486_477257604}[命令用来清除路由表中的路由统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1283531828}

[**[reset ip routing-table statistics protocol ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] { *protocol* \| **all** } **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x184138039}

[**[reset ip routing-table statistics protocol ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] { *protocol* \| **all** } **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_1975689102}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_405150546}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20219_18486_x382167464}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_760652338}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x177040067}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1280115097}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x1671250349}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的路由统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则清除公网的路由统计信息。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_20219_18486_x639096240}[：清除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表中指定路由协议的统计信息。目前可选择]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_20219_18486_1435695220}[：清除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由表中所有路由协议的统计信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1113771472}[：清除备份的指定单板的路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x374501328}[：清除备份的指定成员设备的路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x678523453}[：清除备份的指定成员设备的路由统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1441892611}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#893775604 .myid}
[]{#_Toc404799469}[]{#struct_0_20219_18486_1405913500}[]{#_Toc361388224}[]{#_Toc362012275}[]{#_Toc361388225}[]{#_Toc362012276}[]{#_Toc361388226}[]{#_Toc362012277}[]{#_Toc361388227}[]{#_Toc362012278}[]{#_Toc361388228}[]{#_Toc362012279}[]{#_Toc361388229}[]{#_Toc362012280}[]{#_Toc361388230}[]{#_Toc362012281}[]{#_Toc361388231}[]{#_Toc362012282}[]{#_Toc361388232}[]{#_Toc362012283}[]{#_Toc361388233}[]{#_Toc362012284}[]{#_Toc361388234}[]{#_Toc362012285}[]{#_Toc361388235}[]{#_Toc362012286}[]{#_Toc361388236}[]{#_Toc362012287}[]{#_Toc361388237}[]{#_Toc362012288}[]{#_Toc361388238}[]{#_Toc362012289}[]{#_Toc361388239}[]{#_Toc362012290}[]{#_Toc361388240}[]{#_Toc362012291}[]{#_Toc361388241}[]{#_Toc362012292}[]{#_Toc361388242}[]{#_Toc362012293}[]{#_Toc361388243}[]{#_Toc362012294}[]{#_Toc361388244}[]{#_Toc362012295}[]{#_Toc361388245}[]{#_Toc362012296}[]{#_Toc361388246}[]{#_Toc362012297}[]{#_Toc361388247}[]{#_Toc362012298}[]{#_Toc361388248}[]{#_Toc362012299}[]{#_Toc361388249}[]{#_Toc362012300}[]{#_Toc361388250}[]{#_Toc362012301}[]{#_Toc361388251}[]{#_Toc362012302}[]{#_Toc361388252}[]{#_Toc362012303}[]{#_Toc361388304}[]{#_Toc362012355}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 rib log**

------------------------------------------------------------------------

[**[reset system internal ipv6 rib log]{lang="EN-US"}**]{#struct_0_20219_18486_1128999002}[命令用来清除]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[相关的日志内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x869512148}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1532087824}

[**[reset system internal ipv6 rib]{lang="EN-US"}**[ \[ **event** \] **log**]{lang="EN-US"}]{#struct_0_20219_18486_x901204149}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1532022288}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal ipv6 rib]{lang="EN-US"}**[ \[ **event** \] **log** \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532481040}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_1791205367}[模式：]{style="font-family:宋体"}

[**[reset system internal ipv6 rib]{lang="EN-US"}**[ \[ **event** \] **log** \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532349968}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1306507908}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x728493739}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_734355243}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x805617542}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x701214855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_390644520}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_1679909619}[：]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[路由变化相关的日志。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1532284432}[：清除备份的指定单板]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1532743184}[：清除备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1030195548}[：清除备份的指定成员设备上]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x293360353}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-292961312 .myid}
[]{#_Toc404799470}[]{#struct_0_20219_18486_x727496191}[]{#_Toc336358581}[]{#_Toc340320623}[]{#_Toc361388306}[]{#_Toc362012357}[]{#_Toc361388307}[]{#_Toc362012358}[]{#_Toc361388308}[]{#_Toc362012359}[]{#_Toc361388309}[]{#_Toc362012360}[]{#_Toc361388310}[]{#_Toc362012361}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 rib nib log**

------------------------------------------------------------------------

[**[reset system internal ipv6 rib nib log]{lang="EN-US"}**]{#struct_0_20219_18486_x1490217151}[命令用来清除]{style="font-family:宋体"}[IPv6 NIB]{lang="EN-US"}[子模块日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1181458832}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1532218897}

[**[reset system internal ipv6 rib nib log]{lang="EN-US"}**]{#struct_0_20219_18486_x930956755}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1532153361}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal ipv6 rib nib log]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532087825}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x901138613}[模式：]{style="font-family:宋体"}

[**[reset system internal ipv6 rib nib log ]{lang="EN-US"}**[\[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532481041}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1791270903}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x426419986}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x712107309}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1543784116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x946835193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1532415505}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1056492943}[：清除备份的指定单板]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1532349969}[：清除备份的指定成员设备的]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将清除]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1532284433}[：清除备份的指定成员设备上]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x293360358}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-992562286 .myid}
[]{#_Toc404799471}[]{#struct_0_20219_18486_1607067103}[]{#_Toc340320625}[]{#_Toc361388312}[]{#_Toc362012363}[]{#_Toc361388313}[]{#_Toc362012364}[]{#_Toc361388314}[]{#_Toc362012365}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 rib summary**

------------------------------------------------------------------------

[**[reset system internal ipv6 rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_1030261084}[命令用来清除]{style="font-family:宋体"}[IPv6 RIB]{lang="EN-US"}[的统计摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_2029035706}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_x966276722}

[**[reset system internal ipv6 rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_1532677649}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_275691267}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal ipv6 rib summary]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532218894}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_1532153358}[模式：]{style="font-family:宋体"}

[**[reset system internal ipv6 rib summary]{lang="EN-US"}**[ \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532087822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x901073077}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_2089647072}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1532022286}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1798569544}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1749467502}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x132000642}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1532481038}[：清除备份的指定单板]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1532415502}[：清除备份的指定成员设备]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1532349966}[：清除备份的指定成员设备上]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_x293360356}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#290497634 .myid}
[]{#_Toc404799472}[]{#struct_0_20219_18486_1532284430}[]{#_Toc350345745}[]{#_Toc340320653}[]{#_Toc337654564}[]{#_Toc361388316}[]{#_Toc362012367}[]{#_Toc361388317}[]{#_Toc362012368}[]{#_Toc361388318}[]{#_Toc362012369}[]{#表NBR}[]{#_Toc324781394}[]{#_Toc324781395}[]{#_Toc324781396}[]{#_Toc324781397}[]{#_Toc324781398}[]{#_Toc324781399}[]{#_Toc324781400}[]{#表NBR_1}[]{#表NBR_2}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 route-direct log**

------------------------------------------------------------------------

[**[reset system internal ipv6 route-direct log]{lang="EN-US"}**]{#struct_0_20219_18486_1532743182}[命令用来清除直连路由日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1532677646}

[**[reset system internal ipv6 route-direct ]{lang="EN-US"}**[{ **event** \| **notify** \| **nib** } **log**]{lang="EN-US"}]{#struct_0_20219_18486_276412163}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1532218895}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_1532153359}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1405323673}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1532087823}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1532022287}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1798635080}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_1532481039}[：接口事件相关日志。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_20219_18486_1532415503}[：接口事件通知相关日志。]{style="font-family:宋体"}

[**[nib]{lang="EN-US"}**]{#struct_0_20219_18486_1056886159}[：]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[直连路由]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块相关日志。]{style="font-family:宋体"}
:::

::: {#-739935987 .myid}
[]{#_Toc404799473}[]{#struct_0_20219_18486_x1901197238}[]{#_Toc365035786}[]{#_Toc283297127}[]{#_Toc251058602}[]{#_Toc146504803}[]{#_Toc135644131}[]{#_Toc73957980}[]{#_Toc69886880}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal ipv6 routing-table statistics protocol**

------------------------------------------------------------------------

[**[reset system internal ipv6 routing-table statistics protocol]{lang="EN-US"}**]{#struct_0_20219_18486_1804819350}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中的综合路由统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1238383704}

[**[reset system internal ipv6 routing-table statistics protocol]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { *protocol* \| **all** } **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_1343392217}

[**[reset system internal ipv6 routing-table statistics protocol]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { *protocol* \| **all** } **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_20219_18486_x1977984316}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_21182599}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20219_18486_x1048828606}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1683392427}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_2110604448}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_2109131606}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_20219_18486_x520123485}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的路由统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则清除公网的路由统计信息。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_20219_18486_1808621213}[：清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中指定路由协议的统计信息。目前可选择]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_20219_18486_x601253822}[：清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由表中所有路由协议的统计信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x146441182}[：清除备份的指定单板的路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1544901342}[：清除备份的指定成员设备的路由统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1715002213}[：清除备份的指定成员设备的路由统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_659823599}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-2058376106 .myid}
[]{#_Toc404799474}[]{#struct_0_20219_18486_x930629075}[]{#_Toc361388320}[]{#_Toc362012371}[]{#_Toc361388321}[]{#_Toc362012372}[]{#_Toc361388322}[]{#_Toc362012373}[]{#_Toc361388323}[]{#_Toc362012374}[]{#_Toc361388324}[]{#_Toc362012375}[]{#_Toc361388325}[]{#_Toc362012376}[]{#_Toc361388326}[]{#_Toc362012377}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal rib log**

------------------------------------------------------------------------

[**[reset system internal rib log]{lang="EN-US"}**]{#struct_0_20219_18486_734756696}[命令用来清除]{style="font-family:
宋体"}[RIB]{lang="EN-US"}[相关的日志内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_123170321}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1532153356}

[**[reset system internal rib]{lang="EN-US"}**[ \[ **event** \] **log**]{lang="EN-US"}]{#struct_0_20219_18486_1406306713}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1532087820}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal rib]{lang="EN-US"}**[ \[ **event** \] **log** \[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532022284}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_1532481036}[模式：]{style="font-family:宋体"}

[**[reset system internal rib]{lang="EN-US"}**[ \[ **event** \] **log** \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532415500}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1056820623}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_2139956235}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1656036888}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_x152016538}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1532349964}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1305721476}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_x291262731}[：]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由变化相关的日志。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_65813578}[：清除备份的指定单板]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1532284428}[：清除备份的指定成员设备的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1532743180}[：清除备份的指定成员设备上]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[相关的日志内容。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_2045291806}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#596048093 .myid}
[]{#_Toc404799475}[]{#struct_0_20219_18486_1532677644}[]{#_Toc336358580}[]{#_Toc340320622}[]{#_Toc361388328}[]{#_Toc362012379}[]{#_Toc361388329}[]{#_Toc362012380}[]{#_Toc361388330}[]{#_Toc362012381}[]{#_Toc361388331}[]{#_Toc362012382}[]{#_Toc361388332}[]{#_Toc362012383}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal rib nib log**

------------------------------------------------------------------------

[**[reset system internal rib nib log]{lang="EN-US"}**]{#struct_0_20219_18486_1077688628}[命令用来清除]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x21131285}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1532218893}

[**[reset system internal rib nib log]{lang="EN-US"}**]{#struct_0_20219_18486_x930694611}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_1532153357}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal rib nib log ]{lang="EN-US"}**[\[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532087821}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x900876469}[模式：]{style="font-family:宋体"}

[**[reset system internal rib]{lang="EN-US"}**[ **nib log** \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_1532481037}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_1790877694}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x55849912}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_1043407559}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_1902574662}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_1950938541}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_1532415501}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_1532349965}[：清除备份的指定单板]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1305655940}[：清除备份的指定成员设备的]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将清除]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_1532284429}[：清除备份的指定成员设备上]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块日志。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_2045291809}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#440227724 .myid}
[]{#_Toc404799476}[]{#struct_0_20219_18486_1029998940}[]{#_Toc340320624}[]{#_Toc361388334}[]{#_Toc362012385}[]{#_Toc361388335}[]{#_Toc362012386}[]{#_Toc361388336}[]{#_Toc362012387}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal rib summary**

------------------------------------------------------------------------

[**[reset system internal rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_1801747598}[命令用来清除]{style="font-family:宋体"}[IPv4 RIB]{lang="EN-US"}[的统计摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_1515290963}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20219_18486_1532677645}

[**[reset system internal rib summary]{lang="EN-US"}**]{#struct_0_20219_18486_276477699}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20219_18486_x1196664459}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal rib summary ]{lang="EN-US"}**[\[ **standby slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1196729995}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20219_18486_x1196795531}[模式：]{style="font-family:宋体"}

[**[reset system internal rib summary]{lang="EN-US"}**[ \[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20219_18486_x1196861067}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_561506211}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1841755413}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1317333536}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_841719905}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1196402315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1068283492}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1196467851}[：清除备份的指定单板]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_20219_18486_x1196533387}[：清除备份的指定成员设备]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20219_18486_x1196598923}[：清除备份的指定成员设备上]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将清除]{style="font-family:宋体"}[RIB]{lang="EN-US"}[的统计摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_20219_18486_2045291803}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#703350159 .myid}
[]{#_Toc404799477}[]{#struct_0_20219_18486_x1196140171}[]{#_Toc350345687}[]{#_Toc340320647}[]{#_Toc337653105}[]{#_Toc361388338}[]{#_Toc362012389}[]{#_Toc361388339}[]{#_Toc362012390}[]{#_Toc361388340}[]{#_Toc362012391}

**IP路由基础 \-- IP路由基础Probe命令 \-- reset system internal route-direct log**

------------------------------------------------------------------------

[**[reset system internal route-direct log]{lang="EN-US"}**]{#struct_0_20219_18486_x1196205707}[命令用来清除直连路由日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1196664458}

[**[reset system internal route-direct]{lang="EN-US"}**[ { **event** \| **notify** \| **nib** } **log**]{lang="EN-US"}]{#struct_0_20219_18486_x1302195566}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1196729994}

[[Probe]{lang="EN-US"}]{#struct_0_20219_18486_x1196795530}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1196861066}

[[network-admin]{lang="EN-US"}]{#struct_0_20219_18486_2127590152}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20219_18486_x1196402314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20219_18486_x1196467850}

[**[event]{lang="EN-US"}**]{#struct_0_20219_18486_x1196533386}[：接口事件相关日志。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_20219_18486_x1202413710}[：接口事件通知相关日志。]{style="font-family:宋体"}

[**[nib]{lang="EN-US"}**]{#struct_0_20219_18486_x1196598922}[：直连路由]{style="font-family:宋体"}[NIB]{lang="EN-US"}[子模块相关日志。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
