::: {#-1347531927 .myid}
[]{#_Toc404800213}[]{#struct_0_18996_x1404_440038042}[]{#_Toc375561649}[]{#_Toc369852588}

**RIPng \-- RIPng probe命令 \-- display system internal ripng database standby**

------------------------------------------------------------------------

[**[display system internal ripng]{lang="EN-US"}**[ **database standby**]{lang="EN-US"}]{#struct_0_18996_x1404_x1616048442}[命令用来显示备份的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[数据库的激活路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_439579291}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18996_x1404_x773629224}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ripng]{lang="EN-US"}**[ *process-id* **database standby**[ ]{style="color:blue"}\[ *ipv6-address* *prefix-length* \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_1148774731}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_x1063161588}[模式：]{style="font-family:宋体"}

[**[display system internal ripng]{lang="EN-US"}**[ *process-id* **database standby**[ ]{style="color:blue"}\[ *ipv6-address* *prefix-length* \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_x1985970704}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_321795209}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_1030689359}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_43009297}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x976933644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_588085115}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1021519460}

[*[process-id]{lang="EN-US"}*]{#struct_0_18996_x1404_x798372665}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_18996_x1404_439513755}**[ ]{lang="EN-US"}***[prefix-length]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的激活路由信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_1130084319}[：显示备份的指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[数据库的激活路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x119586130}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[数据库的激活路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_1540996019}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[数据库的激活路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_x820934901}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1837131945 .myid}
[]{#_Toc404800214}[]{#struct_0_18996_x1404_x1846530223}[]{#_Toc375561650}[]{#_Toc369852589}

**RIPng \-- RIPng probe命令 \-- display system internal ripng graceful-restart event-log**

------------------------------------------------------------------------

[**[display system internal ripng]{lang="EN-US"}**[ **graceful-restart event-log**]{lang="EN-US"}]{#struct_0_18996_x1404_x349483887}[命令用来显示]{style="font-family:宋体"}[RIPng GR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x493577029}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18996_x1404_x1780180321}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ripng]{lang="EN-US"}**[ **graceful-restart event-log** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_373950256}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_79951413}[模式：]{style="font-family:宋体"}

[**[display system internal ripng graceful-restart event-log ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_x446770288}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_439710363}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_x494279303}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1858728944}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_330608639}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x526252891}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x884020764}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_1461732356}[：显示指定单板的]{style="font-family:宋体"}[RIPng GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x1694155610}[：显示指定成员设备的]{style="font-family:宋体"}[RIPng GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_x2074507774}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_1858420935}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#740921878 .myid}
[]{#_Toc60036177}[]{#_Toc53707121}[]{#_Toc52484717}[]{#_Toc404800215}[]{#struct_0_18996_x1404_1836253624}[]{#_Toc341285945}[]{#_Toc286221458}[]{#_Toc286221461}[]{#_Toc286221462}[]{#_Toc286221463}[]{#_Toc286221464}[]{#_Toc286221465}[]{#_Toc286221466}[]{#_Toc286221467}[]{#_Toc286221468}[]{#_Toc286221469}[]{#_Toc286221470}[]{#_Toc286221471}[]{#_Toc286221472}[]{#_Toc286221473}[]{#_Toc286221474}[]{#_Toc286221475}[]{#_Toc135620205}[]{#_Toc135620208}[]{#_Toc135620209}[]{#_Toc135620210}[]{#_Toc135620211}[]{#_Toc135620212}[]{#_Toc135620213}[]{#_Toc135620214}[]{#_Toc135620215}[]{#_Toc135620216}[]{#_Toc135620217}[]{#_Toc135620218}[]{#_Toc135620219}[]{#_Toc135620220}[]{#_Toc135620221}[]{#_Toc135620222}[]{#_Toc135620223}[]{#_Toc135620224}[]{#_Toc135620225}[]{#_Toc135620226}[]{#_Toc135620227}[]{#_Toc135620234}[]{#_Toc135620248}[]{#_Toc135620249}[]{#_Toc135620256}[]{#_Toc135620257}[]{#_Toc135620261}[]{#_Toc135620263}[]{#_Toc135620264}[]{#_Toc135620277}[]{#_Toc286221476}[]{#_Toc286221477}[]{#_Toc286221478}[]{#_Toc286221479}[]{#_Toc286221480}[]{#_Toc286221481}[]{#_Toc286221482}[]{#_Toc286221483}[]{#_Toc286221484}[]{#_Toc286221485}[]{#_Toc286221486}[]{#_Toc286221487}[]{#_Toc286221488}[]{#_Toc286221489}[]{#_Toc286221490}[]{#_Toc286221491}[]{#_Toc286221492}[]{#_Toc286221493}[]{#_Toc286221494}[]{#_Toc338677863}[]{#_Toc338677897}[]{#_Toc341341704}[]{#_Toc341782646}

**RIPng \-- RIPng probe命令 \-- display system internal ripng interface**

------------------------------------------------------------------------

[**[display system internal ripng interface]{lang="EN-US"}**]{#struct_0_18996_x1404_1353878006}[命令用来显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1604012218}

[**[display system internal ripng interface ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] \[ *interface-type* *interface-number* \| *ipv6-address* *prefix-length* \]]{lang="EN-US"}]{#struct_0_18996_x1404_58938522}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1863033042}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_x489206800}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1989071490}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x1758263438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_204330821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x87565431}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_18996_x1404_2092487980}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_18996_x1404_x1604077754}[：接口类型和接口编号。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_18996_x1404_870803555}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_18996_x1404_x1753119620}[：前缀长度，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}
:::

::: {#579522441 .myid}
[]{#_Toc404800216}[]{#struct_0_18996_x1404_439644827}[]{#_Toc375561652}[]{#_Toc369852591}

**RIPng \-- RIPng probe命令 \-- display system internal ripng interface standby**

------------------------------------------------------------------------

[**[display system internal ripng interface standby]{lang="EN-US"}**]{#struct_0_18996_x1404_x499802279}[命令用来显示备份的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_137706864}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18996_x1404_439317147}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ripng ]{lang="EN-US"}***[process-id ]{lang="EN-US"}***[interface standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_2046807723}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_x1875775672}[模式：]{style="font-family:宋体"}

[**[display system internal ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ interface standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_x1316628288}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x496557758}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_1461295782}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_1420401421}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_850896889}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x2038832278}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x661626186}

[*[process-id]{lang="EN-US"}*]{#struct_0_18996_x1404_439251611}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x1865798398}[：接口类型和编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[指定进程的所有接口信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_1013503985}[：显示备份的指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x1654217031}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_78444912}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_1385342954}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#2136263842 .myid}
[]{#_Toc404800217}[]{#struct_0_18996_x1404_x2046587300}[]{#_Toc375561653}[]{#_Toc369852593}

**RIPng \-- RIPng probe命令 \-- display system internal ripng neighbor standby**

------------------------------------------------------------------------

[**[display system internal ripng neighbor standby]{lang="EN-US"}**]{#struct_0_18996_x1404_x1361977686}[命令用来显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_1267170595}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18996_x1404_1237799846}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ neighbor standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_1058292987}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_439448219}[模式：]{style="font-family:宋体"}

[**[display system internal ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ neighbor standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **chassis** *chassis-number* ** slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_356211441}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x64283243}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_1100294302}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x791808360}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_1146192334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_1018256000}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x982913379}

[*[process-id]{lang="EN-US"}*]{#struct_0_18996_x1404_x1738157905}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x604451963}[：接口类型和编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[的所有接口信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x1188338174}[：显示备份的指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_439382683}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_x656987273}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_x994524499}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#595071455 .myid}
[]{#_Toc404800218}[]{#struct_0_18996_x1404_381849212}[]{#_Toc341285946}[]{#_Toc360798592}[]{#_Toc360798593}[]{#_Toc360798594}[]{#_Toc360798595}[]{#_Toc360798596}[]{#_Toc360798597}[]{#_Toc360798598}[]{#_Toc360798599}[]{#_Toc360798600}[]{#_Toc360798601}[]{#_Toc360798602}[]{#_Toc360798603}[]{#_Toc360798604}[]{#_Toc360798605}[]{#_Toc360798606}[]{#_Toc360798607}[]{#_Toc360798608}[]{#_Toc360798609}[]{#_Toc360798610}[]{#_Toc360798611}[]{#_Toc360798612}[]{#_Toc360798613}[]{#_Toc360798614}[]{#_Toc360798615}[]{#_Toc360798616}[]{#_Toc360798617}[]{#_Toc360798618}[]{#_Toc360798619}[]{#_Toc360798620}[]{#_Toc360798621}[]{#_Toc360798622}[]{#_Toc360798623}[]{#_Toc360798624}[]{#_Toc360798685}

**RIPng \-- RIPng probe命令 \-- display system internal ripng nib**

------------------------------------------------------------------------

[**[display  system internal ripng nib]{lang="EN-US"}**]{#struct_0_18996_x1404_x441117713}[命令用来]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_201050565}

[**[display system internal ripng nib]{lang="EN-US"}**[ \[ *nib-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18996_x1404_x794929509}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1070199530}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_x1604077753}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_111288668}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_1576529243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_1816337132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1463191066}

[*[nib-id]{lang="EN-US"}*]{#struct_0_18996_x1404_x1482820446}[：下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。如果不指定，显示所有下一跳信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_18996_x1404_x1760432191}[：显示下一跳详细信息。]{style="font-family:宋体"}
:::

::: {#882241091 .myid}
[]{#_Toc404800219}[]{#struct_0_18996_x1404_1380993770}[]{#_Toc341285947}[]{#_Toc360798687}[]{#_Toc360798688}[]{#_Toc360798689}[]{#_Toc360798690}[]{#_Toc360798691}[]{#_Toc360798692}[]{#_Toc360798693}[]{#_Toc360798694}[]{#_Toc360798695}[]{#_Toc360798696}[]{#_Toc360798697}[]{#_Toc360798698}[]{#_Toc360798699}[]{#_Toc360798700}[]{#_Toc360798701}[]{#_Toc360798702}[]{#_Toc360798703}[]{#_Toc360798757}[]{#_Toc360798758}[]{#_Toc360798759}[]{#_Toc360798760}[]{#_Toc360798761}[]{#_Toc360798762}[]{#_Toc360798763}[]{#_Toc360798764}[]{#_Toc360798765}[]{#_Toc360798766}[]{#_Toc360798767}[]{#_Toc360798768}[]{#_Toc360798769}[]{#_Toc360798770}[]{#_Toc360798771}[]{#_Toc360798772}[]{#_Toc360798773}[]{#_Toc360798774}[]{#_Toc360798775}[]{#_Toc360798776}[]{#_Toc360798777}[]{#_Toc360798778}[]{#_Toc360798779}[]{#_Toc360798780}[]{#_Toc360798781}[]{#_Toc360798782}[]{#_Toc360798783}[]{#_Toc360798784}[]{#_Toc360798785}[]{#_Toc360798786}[]{#_Toc360798787}[]{#_Toc360798788}[]{#_Toc360798789}[]{#_Toc360798838}

**RIPng \-- RIPng probe命令 \-- display system internal ripng nib log**

------------------------------------------------------------------------

[**[display  system internal ripng nib log]{lang="EN-US"}**]{#struct_0_18996_x1404_97452467}[命令用来]{style="font-family:
宋体"}[RIPng]{lang="EN-US"}[路由下一跳日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x597657247}

[**[display system internal ripng nib]{lang="EN-US"}**[ **log**]{lang="EN-US"}]{#struct_0_18996_x1404_x1835951355}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1604339899}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_x1122707151}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1496311002}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x1052114490}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_815153475}
:::

::: {#-973172504 .myid}
[]{#_Toc404800220}[]{#struct_0_18996_x1404_440103579}[]{#_Toc375561656}[]{#_Toc369852594}

**RIPng \-- RIPng probe命令 \-- display system internal ripng non-stop-routing event-log**

------------------------------------------------------------------------

[**[display system internal ripng]{lang="EN-US"}**[ **non-stop-routing event-log**]{lang="EN-US"}]{#struct_0_18996_x1404_x2013702665}[命令用来显示]{style="font-family:宋体"}[RIPng NSR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1244768463}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18996_x1404_x837873166}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ripng]{lang="EN-US"}**[ **non-stop-routing event-log** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_x1350674512}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_440038043}[模式：]{style="font-family:宋体"}

[**[display system internal ripng non-stop-routing event-log ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_x1616048443}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1548907242}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_1447222250}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x1357686043}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x1224763083}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_1738412526}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x324796978}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x1020323772}[：显示指定单板的]{style="font-family:宋体"}[RIPng NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x1418288000}[：显示指定成员设备的]{style="font-family:宋体"}[RIPng NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_x1806190981}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_2005663227}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1827191961 .myid}
[]{#_Toc404800221}[]{#struct_0_18996_x1404_x1585601778}[]{#_Toc375561657}[]{#_Toc369852596}

**RIPng \-- RIPng probe命令 \-- display system internal ripng route standby**

------------------------------------------------------------------------

[**[display system internal ripng route standby]{lang="EN-US"}**]{#struct_0_18996_x1404_1049763750}[命令用来显示备份的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_18996_x1404_x92549409}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18996_x1404_x1529860365}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ route standby ]{lang="EN-US"}**[\[ *ipv6-address prefix-length* \[ **verbose** \] \| **peer** *ipv6-address* \| **statistics** \]  **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_x273598645}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_827678092}[模式：]{style="font-family:宋体"}

[**[display system internal ripng ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ route standby ]{lang="EN-US"}**[\[ *ipv6-address prefix-length* \[ **verbose** \] \| **peer** *ipv6-address* \| **statistics** \]  **chassis** *chassis-number*   **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_1361006219}

[[【视图】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_18996_x1404_x1385623699}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_195007872}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_18996_x1404_2024065515}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_2005597691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_1498576212}

[[【参数】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_18996_x1404_916341057}

[*[process-id]{lang="EN-US"}*]{#struct_0_18996_x1404_x2129694483}[：]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_841317063}[：显示备份的指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_1910513358}[：显示备份的指定成员设备的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_x888625490}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_x398816198}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-2016103591 .myid}
[]{#_Toc404800222}[]{#struct_0_18996_x1404_x1603815611}[]{#_Toc341777617}[]{#_Toc360798840}[]{#_Toc360798841}[]{#_Toc360798842}[]{#_Toc360798843}[]{#_Toc360798844}[]{#_Toc360798845}[]{#_Toc360798846}[]{#_Toc360798847}[]{#_Toc360798848}[]{#_Toc360798849}[]{#_Toc360798850}[]{#_Toc360798851}[]{#_Toc360798852}[]{#_Toc360798853}[]{#_Toc360798854}[]{#_Toc360798855}[]{#_Toc360798856}[]{#_Toc360798857}[]{#_Toc360798858}[]{#_Toc360798859}[]{#_Toc360798860}[]{#_Toc360798861}[]{#_Toc360798862}[]{#_Toc360798863}[]{#_Toc360798864}[]{#_Toc360798865}[]{#_Toc360798866}[]{#_Toc360798867}[]{#_Toc360798919}

**RIPng \-- RIPng probe命令 \-- display system internal ripng status**

------------------------------------------------------------------------

[**[display ]{lang="EN-US"}[system internal ripng status]{lang="EN-US"}**]{#struct_0_18996_x1404_x1034326608}[命令用来显示]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[协议全局状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_336999291}

[**[display ]{lang="EN-US"}[system internal ripng status]{lang="EN-US"}**]{#struct_0_18996_x1404_771371866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_1905561519}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_x2084005917}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x506773303}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x238846743}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_1755118045}
:::

::: {#-1265569029 .myid}
[]{#_Toc404800223}[]{#struct_0_18996_x1404_2005794299}[]{#_Toc375561659}[]{#_Toc369852600}[]{#_Toc338677867}[]{#_Toc338677902}[]{#_Toc341341709}[]{#_Toc341782652}[]{#_Toc286221500}[]{#_Toc286221501}[]{#_Toc286221502}[]{#_Toc286221503}[]{#_Toc286221504}[]{#_Toc286221505}[]{#_Toc286221506}[]{#_Toc286221507}[]{#_Toc286221508}[]{#_Toc286221509}[]{#_Toc286221510}[]{#_Toc286221511}[]{#_Toc286221512}[]{#_Toc286221513}[]{#_Toc286221514}[]{#_Toc286221515}[]{#_Toc286221519}[]{#_Toc286221520}[]{#_Toc286221523}[]{#_Toc286221524}[]{#_Toc286221525}[]{#_Toc286221526}[]{#_Toc286221527}[]{#_Toc286221528}[]{#_Toc286221529}[]{#_Toc286221530}[]{#_Toc286221531}[]{#_Toc286221532}[]{#_Toc286221533}[]{#_Toc286221534}[]{#_Toc286221535}[]{#_Toc286221536}[]{#_Toc286221537}[]{#_Toc286221538}[]{#_Toc286221539}[]{#_Toc286221540}[]{#_Toc286221541}[]{#_Toc286221542}[]{#_Toc286221543}[]{#_Toc286221544}[]{#_Toc286221546}[]{#_Toc286221547}[]{#_Toc286221549}[]{#_Toc286221550}[]{#_Toc286221551}[]{#_Toc286221552}[]{#_Toc286221553}[]{#_Toc286221554}[]{#_Toc286221555}[]{#_Toc286221556}[]{#_Toc286221557}[]{#_Toc286221558}[]{#_Toc286221559}[]{#_Toc286221560}[]{#_Toc286221561}[]{#_Toc286221562}[]{#_Toc286221563}[]{#_Toc286221564}[]{#_Toc286221565}[]{#_Toc286221566}[]{#_Toc286221567}[]{#_Toc286221568}[]{#_Toc286221569}[]{#_Toc286221570}[]{#_Toc286221571}[]{#_Toc286221572}[]{#_Toc286221574}[]{#_Toc286221575}[]{#_Toc286221577}[]{#_Toc286221578}[]{#_Toc286221580}[]{#_Toc286221581}[]{#_Toc286221583}[]{#_Toc286221584}[]{#_Toc286221585}[]{#_Toc286221586}[]{#_Toc286221587}[]{#_Toc286221588}[]{#_Toc286221589}[]{#_Toc286221590}[]{#_Toc286221591}[]{#_Toc286221592}[]{#_Toc286221593}[]{#_Toc286221594}[]{#_Toc286221595}[]{#_Toc286221596}[]{#_Toc286221597}[]{#_Toc286221598}[]{#_Toc286221599}[]{#_Toc286221600}[]{#_Toc286221601}[]{#_Toc286221602}[]{#_Toc286221603}[]{#_Toc286221604}[]{#_Toc264986238}[]{#_Toc264986239}[]{#_Toc264986240}[]{#_Toc264986241}[]{#_Toc264986242}[]{#_Toc264986243}[]{#_Toc264986244}[]{#_Toc264986245}[]{#_Toc264986246}[]{#_Toc264986247}[]{#_Toc264986248}[]{#_Toc264986249}[]{#_Toc264986250}[]{#_Toc264986251}[]{#_Toc264986252}[]{#_Toc264986253}[]{#_Toc264986255}[]{#_Toc286221605}[]{#_Toc286221606}[]{#_Toc286221607}[]{#_Toc286221608}[]{#_Toc286221609}[]{#_Toc286221610}[]{#_Toc286221611}[]{#_Toc286221612}[]{#_Toc286221613}[]{#_Toc286221614}[]{#_Toc286221615}[]{#_Toc286221616}[]{#_Toc286221617}[]{#_Toc286221618}[]{#_Toc286221619}[]{#_Toc286221620}[]{#_Toc286221621}[]{#_Toc286221622}[]{#_Toc286221623}[]{#_Toc286221624}[]{#_Toc286221627}[]{#_Toc286221628}[]{#_Toc286221629}[]{#_Toc286221630}[]{#_Toc286221631}[]{#_Toc286221632}[]{#_Toc286221633}[]{#_Toc286221634}[]{#_Toc286221635}[]{#_Toc286221636}[]{#_Toc286221637}[]{#_Toc286221638}[]{#_Toc286221639}[]{#_Toc286221640}[]{#_Toc286221641}[]{#_Toc286221642}[]{#_Toc286221643}[]{#_Toc286221644}[]{#_Toc286221645}[]{#_Toc286221646}[]{#_Toc286221648}[]{#_Toc286221649}[]{#_Toc286221650}[]{#_Toc286221651}[]{#_Toc286221652}[]{#_Toc286221653}[]{#_Toc286221654}[]{#_Toc286221655}[]{#_Toc286221656}[]{#_Toc286221657}[]{#_Toc286221658}[]{#_Toc286221659}[]{#_Toc286221660}[]{#_Toc286221661}[]{#_Toc286221662}[]{#_Toc286221663}[]{#_Toc286221664}[]{#_Toc286221665}[]{#_Toc286221667}[]{#_Toc286221668}[]{#_Toc286221669}[]{#_Toc286221670}[]{#_Toc286221671}[]{#_Toc286221672}[]{#_Toc286221673}[]{#_Toc286221674}[]{#_Toc286221675}[]{#_Toc286221676}[]{#_Toc286221677}[]{#_Toc286221678}[]{#_Toc286221679}[]{#_Toc286221681}[]{#_Toc286221682}[]{#_Toc286221683}[]{#_Toc286221685}[]{#_Toc286221688}[]{#_Toc286221689}[]{#_Toc286221690}[]{#_Toc286221691}[]{#_Toc286221692}[]{#_Toc286221693}[]{#_Toc286221694}[]{#_Toc286221695}[]{#_Toc286221696}[]{#_Toc286221697}[]{#_Toc286221698}[]{#_Toc286221699}[]{#_Toc286221700}[]{#_Toc286221701}[]{#_Toc286221702}[]{#_Toc286221703}[]{#_Toc286221704}[]{#_Toc286221705}[]{#_Toc286221706}[]{#_Toc286221707}[]{#_Toc286221708}[]{#_Toc286221709}[]{#_Toc286221710}[]{#_Toc286221711}[]{#_Toc286221712}[]{#_Toc286221714}[]{#_Toc286221715}[]{#_Toc286221716}[]{#_Toc286221718}[]{#_Toc326738822}[]{#_Toc326738823}[]{#_Toc326738824}[]{#_Toc326738825}[]{#_Toc326738826}[]{#_Toc326738827}[]{#_Toc326738828}[]{#_Toc326738829}[]{#_Toc326738830}[]{#_Toc326738831}[]{#_Toc326738832}[]{#_Toc326738833}[]{#_Toc326738834}[]{#_Toc326738835}[]{#_Toc326738836}[]{#_Toc326738837}[]{#_Toc326738838}[]{#_Toc326738839}[]{#_Toc326738840}[]{#_Toc292815538}[]{#_Toc326738841}[]{#_Toc326738842}[]{#_Toc326738843}[]{#_Toc326738844}[]{#_Toc326738845}[]{#_Toc326738846}[]{#_Toc326738847}[]{#_Toc326738848}[]{#_Toc326738849}[]{#_Toc326738850}[]{#_Toc286221720}[]{#_Toc286221721}[]{#_Toc286221722}[]{#_Toc286221723}[]{#_Toc286221724}[]{#_Toc286221725}[]{#_Toc286221726}[]{#_Toc286221727}[]{#_Toc286221728}[]{#_Toc286221729}[]{#_Toc286221730}[]{#_Toc286221731}[]{#_Toc286221732}[]{#_Toc286221733}[]{#_Toc286221734}[]{#_Toc286221735}[]{#_Toc286221736}[]{#_Toc286221740}[]{#_Toc286221741}[]{#_Toc286221742}[]{#_Toc286221746}[]{#_Toc286221747}[]{#_Toc286221748}[]{#_Toc286221749}[]{#_Toc286221750}[]{#_Toc286221751}[]{#_Toc286221752}[]{#_Toc286221753}[]{#_Toc286221754}[]{#_Toc286221755}[]{#_Toc286221756}[]{#_Toc286221757}[]{#_Toc286221758}[]{#_Toc286221759}[]{#_Toc286221760}[]{#_Toc286221761}[]{#_Toc286221762}[]{#_Toc286221763}[]{#_Toc286221765}[]{#_Toc286221766}[]{#_Toc286221767}[]{#_Toc286221769}[]{#_Toc286221771}[]{#_Toc286221772}[]{#_Toc286221773}[]{#_Toc286221774}[]{#_Toc286221775}[]{#_Toc286221776}[]{#_Toc286221777}[]{#_Toc286221778}[]{#_Toc286221779}[]{#_Toc286221780}[]{#_Toc286221781}[]{#_Toc286221782}[]{#_Toc286221783}[]{#_Toc286221784}[]{#_Toc286221785}[]{#_Toc286221786}[]{#_Toc286221787}[]{#_Toc286221788}[]{#_Toc286221790}[]{#_Toc286221791}[]{#_Toc286221792}[]{#_Toc286221794}[]{#_Toc157826816}[]{#_Toc138824575}[]{#_Toc138824576}[]{#_Toc138824577}[]{#_Toc138824578}[]{#_Toc138824579}[]{#_Toc138824581}[]{#_Toc138824582}[]{#_Toc138824583}[]{#_Toc138824584}[]{#_Toc138824585}

**RIPng \-- RIPng probe命令 \-- reset system internal ripng graceful-restart event-log**

------------------------------------------------------------------------

[**[reset system internal ripng graceful-restart event-log]{lang="ES"}**]{#struct_0_18996_x1404_x831657555}[命令用来清除]{style="font-family:宋体"}[RIPng GR]{lang="ES"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x946371321}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_18996_x1404_1133544842}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="ES"}[集中式]{style="font-family:宋体"}[IRF]{lang="ES"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset system internal ripng graceful-restart event-log]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_1749434888}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_x369069843}[模式：]{style="font-family:宋体"}

[**[reset system internal ripng graceful-restart event-log]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_51769375}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x125998138}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_x1723554156}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_2005728763}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x65553368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_x1656122208}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x149116242}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_2048218405}[：清除指定单板的]{style="font-family:宋体"}[RIPng]{lang="ES"}[ GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x119350293}[：清除指定成员设备的]{style="font-family:宋体"}[RIPng]{lang="ES"}[ GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_x1193422267}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng]{lang="ES"}[ GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_376382014}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1850788511 .myid}
[]{#_Toc404800224}[]{#struct_0_18996_x1404_970213853}[]{#_Toc375561660}[]{#_Toc369852601}

**RIPng \-- RIPng probe命令 \-- reset system internal ripng non-stop-routing event-log**

------------------------------------------------------------------------

[**[reset system internal ripng non-stop-routing event-log]{lang="ES"}**]{#struct_0_18996_x1404_1004922539}[命令用来清除]{style="font-family:宋体"}[RIPng NSR]{lang="ES"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18996_x1404_1925724556}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_18996_x1404_1177051416}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="ES"}[集中式]{style="font-family:宋体"}[IRF]{lang="ES"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset system internal ripng non-stop-routing event-log ]{lang="EN-US"}[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_2005401083}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18996_x1404_x792163200}[模式：]{style="font-family:宋体"}

[**[reset system internal ripng non-stop-routing event-log ]{lang="EN-US"}[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_18996_x1404_x586102832}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x375432399}

[[Probe]{lang="EN-US"}]{#struct_0_18996_x1404_74836924}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18996_x1404_x2044101197}

[[network-admin]{lang="EN-US"}]{#struct_0_18996_x1404_446578881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18996_x1404_2030606933}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18996_x1404_122494885}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_x1619863658}[：清除指定单板的]{style="font-family:宋体"}[RIPng]{lang="ES"}[备进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_18996_x1404_1174231534}[：清除指定成员设备的]{style="font-family:宋体"}[RIPng]{lang="ES"}[备进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_18996_x1404_609992875}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[RIPng]{lang="ES"}[备进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_18996_x1404_2005335547}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
