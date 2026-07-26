::::: {#-134608462 .myid}
[]{#_Toc404800030}[]{#struct_0_x2081_x5871_x1255277600}[]{#_Toc348020472}[]{#_Toc340222303}[]{#_Toc338927736}

**OSPF \-- OSPF probe命令 \-- display system internal ospf event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_248070284}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_x971996768}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf event-log]{lang="EN-US"}**]{#struct_0_x2081_x5871_1767423616}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1997557479}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2081_x5871_x919948285}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** **event-log** { **gr** \| **ha** \| **interface** \| **nib** \| **notify** \| **upgrade** }]{lang="EN-US"}]{#struct_0_x2081_x5871_x333547550}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x2081_x5871_13403304}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** **event-log** { **gr** \| **interface** \| **nib** \| **notify** \| { **ha** \| **upgrade** } \[ **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \] \] }]{lang="EN-US"}]{#struct_0_x2081_x5871_x1648066385}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_x2081_x5871_688460557}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** **event-log** { **gr** \| **interface** \| **nib** \| **notify** \| { **ha** \| **upgrade** } \[ **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] }]{lang="EN-US"}]{#struct_0_x2081_x5871_x1647673169}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1584115593}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_1610661456}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1144819780}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_720460873}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x1373524457}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1216851635}

[**[gr]{lang="EN-US"}**]{#struct_0_x2081_x5871_x173633661}[：显示]{style="font-family:宋体"}[GR]{lang="EN-US"}[日志。]{style="font-family:宋体"}

[**[ha]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1647607633}[：显示]{style="font-family:宋体"}[HA]{lang="EN-US"}[事件处理日志信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_x2081_x5871_x2070254331}[：显示接口事件日志。]{style="font-family:宋体"}

[**[nib]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1082332073}[：显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[日志。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_x2081_x5871_1474828935}[：]{style="font-family:宋体"}[显示接口通知日志。]{style="font-family:宋体"}

[**[upgrade]{lang="EN-US"}**]{#struct_0_x2081_x5871_610045736}[：显示升级平滑日志信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1648197456}*[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_199610594}*[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**]{#struct_0_x2081_x5871_515946083}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的日志信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_106278143}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::::: {#562467186 .myid}
[]{#_Toc404800031}[]{#struct_0_x2081_x5871_421384863}[]{#_Toc371424074}[]{#_Toc366565714}

**OSPF \-- OSPF probe命令 \-- display system internal ospf flood-list**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_x1900637295}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_421450399}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf flood-list]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1934192021}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[flooding]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1332657496}

[**[display system internal ospf]{lang="EN-US"}**[ \[ *process-id* \] **flood-list** \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_x392651443}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x263474736}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_x120065103}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1700242083}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1940273901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1550700413}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1066130258}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_421515935}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[flooding]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_1891704825}[：显示指定接口的]{style="font-family:宋体"}[flooding]{lang="EN-US"}[信息。如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[flooding]{lang="EN-US"}[信息。]{style="font-family:宋体"}
:::::

::::: {#904648582 .myid}
[]{#_Toc348020473}[]{#_Toc340222304}[]{#_Toc348020471}[]{#_Toc404800032}[]{#struct_0_x2081_x5871_x351440212}[]{#_Toc360799423}[]{#_Toc362010253}[]{#_Toc360799424}[]{#_Toc362010254}[]{#_Toc360799425}[]{#_Toc362010255}[]{#_Toc360799426}[]{#_Toc362010256}[]{#_Toc360799427}[]{#_Toc362010257}[]{#_Toc360799428}[]{#_Toc362010258}[]{#_Toc360799429}[]{#_Toc362010259}[]{#_Toc360799430}[]{#_Toc362010260}[]{#_Toc360799431}[]{#_Toc362010261}[]{#_Toc360799432}[]{#_Toc362010262}[]{#_Toc360799454}[]{#_Toc362010284}[]{#_Toc360799455}[]{#_Toc362010285}[]{#_Toc360799456}[]{#_Toc362010286}[]{#_Toc360799457}[]{#_Toc362010287}[]{#_Toc360799458}[]{#_Toc362010288}[]{#_Toc360799459}[]{#_Toc362010289}[]{#_Toc360799460}[]{#_Toc362010290}[]{#_Toc360799461}[]{#_Toc362010291}[]{#_Toc360799462}[]{#_Toc362010292}[]{#_Toc360799463}[]{#_Toc362010293}[]{#_Toc360799464}[]{#_Toc362010294}[]{#_Toc360799465}[]{#_Toc362010295}[]{#_Toc360799466}[]{#_Toc362010296}[]{#_Toc360799467}[]{#_Toc362010297}[]{#_Toc360799468}[]{#_Toc362010298}[]{#_Toc360799469}[]{#_Toc362010299}[]{#_Toc360799470}[]{#_Toc362010300}[]{#_Toc360799471}[]{#_Toc362010301}[]{#_Toc360799520}[]{#_Toc362010350}[]{#_Toc360799521}[]{#_Toc362010351}[]{#_Toc360799522}[]{#_Toc362010352}[]{#_Toc360799523}[]{#_Toc362010353}[]{#_Toc360799524}[]{#_Toc362010354}[]{#_Toc360799525}[]{#_Toc362010355}[]{#_Toc360799526}[]{#_Toc362010356}[]{#_Toc360799527}[]{#_Toc362010357}[]{#_Toc360799528}[]{#_Toc362010358}[]{#_Toc360799658}[]{#_Toc362010488}

**OSPF \-- OSPF probe命令 \-- display system internal ospf interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_1016459912}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_x12045091}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf]{lang="EN-US"}***[ ]{lang="EN-US"}***[interface]{lang="EN-US"}**]{#struct_0_x2081_x5871_x242220713}[命令用来显示接口相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1998005287}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** **interface** \[ **vpn-instance** *vpn-instance-name* \] \[ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } \]]{lang="EN-US"}]{#struct_0_x2081_x5871_1378934613}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_2128414285}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_1944737135}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1296825457}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_44152185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_449288607}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_142420851}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1416242951}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例下接口相关信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1998070823}[：接口类型和编号。如果未指定本参数，将显示所有接口的信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1118328372}[：接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制，显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和掩码]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码长度接口的信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1978171149}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x2081_x5871_438567490}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}
:::::

::: {#1566218906 .myid}
[]{#_Toc404800033}[]{#struct_0_x2081_x5871_1079717923}[]{#_Toc363647454}[]{#_Toc357512832}

**OSPF \-- OSPF probe命令 \-- display system internal ospf interface standby**

------------------------------------------------------------------------

[**[display system internal ospf interface standby]{lang="EN-US"}**]{#struct_0_x2081_x5871_2045344687}[命令用来显示备份的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x978230194}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x2081_x5871_1079521315}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ospf]{lang="EN-US"}**[ \[ *process-id* \] **interface** \[ *interface-type interface-number* \| **verbose** \] **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_1702608842}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2081_x5871_x2088646533}[模式：]{style="font-family:宋体"}

[**[display system internal ospf]{lang="EN-US"}**[ \[ *process-id* \] **interface** \[ *interface-type interface-number* \| **verbose** \] **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_1651389337}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_491869549}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_1295929010}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1408777748}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1360626014}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1738870571}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1498672103}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_150411564}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的接口信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2081_x5871_1079586851}[：接口类型和编号。显示指定接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1492586493}[：显示所有接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_x897242644}[：]{style="font-family:宋体"}[显示备份的指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_x1216070583}[：]{style="font-family:宋体"}[显示备份的指定成员设备的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_x743745608}[：]{style="font-family:宋体"}[显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_106278144}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::::: {#-1998828863 .myid}
[]{#_Toc404800034}[]{#struct_0_x2081_x5871_x20931359}[]{#_Toc360799660}[]{#_Toc362010490}[]{#_Toc360799661}[]{#_Toc362010491}[]{#_Toc360799662}[]{#_Toc362010492}[]{#_Toc360799663}[]{#_Toc362010493}[]{#_Toc360799664}[]{#_Toc362010494}[]{#_Toc360799665}[]{#_Toc362010495}[]{#_Toc360799666}[]{#_Toc362010496}[]{#_Toc360799667}[]{#_Toc362010497}[]{#_Toc360799668}[]{#_Toc362010498}[]{#_Toc360799669}[]{#_Toc362010499}[]{#_Toc360799670}[]{#_Toc362010500}[]{#_Toc360799671}[]{#_Toc362010501}[]{#_Toc360799672}[]{#_Toc362010502}[]{#_Toc360799673}[]{#_Toc362010503}[]{#_Toc360799674}[]{#_Toc362010504}[]{#_Toc360799675}[]{#_Toc362010505}[]{#_Toc360799676}[]{#_Toc362010506}[]{#_Toc360799677}[]{#_Toc362010507}[]{#_Toc360799678}[]{#_Toc362010508}[]{#_Toc360799679}[]{#_Toc362010509}[]{#_Toc360799680}[]{#_Toc362010510}[]{#_Toc360799681}[]{#_Toc362010511}[]{#_Toc360799682}[]{#_Toc362010512}[]{#_Toc360799683}[]{#_Toc362010513}[]{#_Toc360799684}[]{#_Toc362010514}[]{#_Toc360799685}[]{#_Toc362010515}[]{#_Toc360799686}[]{#_Toc362010516}[]{#_Toc360799687}[]{#_Toc362010517}[]{#_Toc360799688}[]{#_Toc362010518}[]{#_Toc360799689}[]{#_Toc362010519}[]{#_Toc360799690}[]{#_Toc362010520}[]{#_Toc360799691}[]{#_Toc362010521}[]{#_Toc360799692}[]{#_Toc362010522}[]{#_Toc360799693}[]{#_Toc362010523}[]{#_Toc360799694}[]{#_Toc362010524}[]{#_Toc360799695}[]{#_Toc362010525}[]{#_Toc360799696}[]{#_Toc362010526}[]{#_Toc360799697}[]{#_Toc362010527}[]{#_Toc360799698}[]{#_Toc362010528}[]{#_Toc360799699}[]{#_Toc362010529}[]{#_Toc360799700}[]{#_Toc362010530}[]{#_Toc360799701}[]{#_Toc362010531}[]{#_Toc360799762}[]{#_Toc362010592}

**OSPF \-- OSPF probe命令 \-- display system internal ospf lsdb**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_x40993681}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_x253633794}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}**

[**[display system internal ospf lsdb]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_x2081_x5871_x448097023}[命令用来显示]{style="font-size:10.5pt;
font-family:宋体"}[LSA]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[产生的来源及详细信息。]{style="font-size:10.5pt;
font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x772814491}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** \[ *process-id* \] **lsdb** { **asbr** \| **ase** \| **nssa** \| **summary** }]{lang="EN-US"}]{#struct_0_x2081_x5871_x431986887}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1741489718}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_427505608}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_272161710}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x1459637499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_722024013}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1356339737}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_1746818420}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[LSA map]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[asbr]{lang="EN-US"}**]{#struct_0_x2081_x5871_169797543}[：显示数据库中]{style="font-family:宋体"}[Type-4 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[ASBR Summary LSA]{lang="EN-US"}[）的]{style="font-family:宋体"}[map]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[ase]{lang="EN-US"}**]{#struct_0_x2081_x5871_x432052423}[：显示数据库中]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[AS External LSA]{lang="EN-US"}[）的]{style="font-family:宋体"}[map]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[nssa]{lang="EN-US"}**]{#struct_0_x2081_x5871_863423207}[：显示数据库中]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[NSSA External LSA]{lang="EN-US"}[）的]{style="font-family:宋体"}[map]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_x2081_x5871_1749686300}[：显示数据库中]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Summary LSA]{lang="EN-US"}[）的]{style="font-family:宋体"}[map]{lang="EN-US"}[信息。]{style="font-family:宋体"}
:::::

::: {#2119289245 .myid}
[]{#_Toc404800035}[]{#struct_0_x2081_x5871_1079390243}[]{#_Toc363647456}[]{#_Toc357512834}

**OSPF \-- OSPF probe命令 \-- display system internal ospf lsdb standby**

------------------------------------------------------------------------

[**[display system internal ospf lsdb standby]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1834797786}[命令用来显示备份的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[链路状态数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1433797377}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x2081_x5871_x1094076688}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **lsdb** \[ **area** *area-id* \| **brief** \| \[ { **asbr** \| **ase** \| **network** \| **nssa** \| **opaque-area** \| **opaque-as** \| **opaque-link** \| **router** \| **summary** } \[ *link-state-id* \] \] \[ **originate-router** *advertising-router-id* \| **self-originate** \] \] **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_1079455779}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2081_x5871_x1038445999}[模式：]{style="font-family:宋体"}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **lsdb** \[ **area** *area-id* \| **brief** \| \[ { **asbr** \| **ase** \| **network** \| **nssa** \| **opaque-area** \| **opaque-as** \| **opaque-link** \| **router** \| **summary** } \[ *link-state-id* \] \] \[ **originate-router** *advertising-router-id* \| **self-originate** \] \] **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_203728279}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x279776873}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_x1624129981}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x100440553}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_810021221}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1989301376}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_957606959}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_247675172}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的链路状态数据库信息。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}***[ area-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_1079259171}[：显示数据库中指定区域的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[表示区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式*。*如果未指定本参数，将显示所有区域的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x2081_x5871_957553623}[：显示数据库的概要信息。]{style="font-family:宋体"}

[**[asbr]{lang="EN-US"}**]{#struct_0_x2081_x5871_310644270}[：显示数据库中]{style="font-family:宋体"}[Type-4 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[ASBR Summary LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[ase]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1935789386}[：显示数据库中]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[AS External LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**]{#struct_0_x2081_x5871_1549806140}[：显示数据库中]{style="font-family:宋体"}[Type-2 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Network LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[nssa]{lang="EN-US"}**]{#struct_0_x2081_x5871_x952006865}[：显示数据库中]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[NSSA External LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[opaque-area]{lang="EN-US"}**]{#struct_0_x2081_x5871_24851969}[：显示数据库中]{style="font-family:宋体"}[Type-10 LSA ]{lang="EN-US"}[（]{style="font-family:宋体"}[Opaque-area LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[opaque-as]{lang="EN-US"}**]{#struct_0_x2081_x5871_211570825}[：显示数据库中]{style="font-family:宋体"}[Type-11 LSA ]{lang="EN-US"}[（]{style="font-family:宋体"}[Opaque-AS LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[opaque-link]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1691247264}[：显示数据库中]{style="font-family:宋体"}[Type-9 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Opaque-link LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[router]{lang="EN-US"}**]{#struct_0_x2081_x5871_1079324707}[：显示数据库中]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_x2081_x5871_1697580950}[：显示数据库中]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Summary LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[*[link-state-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x655992828}[：链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[**[originate-router ]{lang="EN-US"}***[advertising-router-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1624700487}[：发布]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文的路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[self-originate]{lang="EN-US"}**]{#struct_0_x2081_x5871_404176724}[：显示本地路由器自己产生的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数据库信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_x719394763}*[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[链路状态数据库]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_1921295553}*[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[链路状态数据库信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**]{#struct_0_x2081_x5871_1856230996}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[链路状态数据库信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_106278140}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::::: {#-1561897303 .myid}
[]{#_Toc348020474}[]{#_Toc340222305}[]{#_Toc338927735}[]{#_Toc404800036}[]{#struct_0_x2081_x5871_x138394639}[]{#_Toc360799764}[]{#_Toc362010594}[]{#_Toc360799765}[]{#_Toc362010595}[]{#_Toc360799766}[]{#_Toc362010596}[]{#_Toc360799767}[]{#_Toc362010597}[]{#_Toc360799768}[]{#_Toc362010598}[]{#_Toc360799769}[]{#_Toc362010599}[]{#_Toc360799770}[]{#_Toc362010600}[]{#_Toc360799771}[]{#_Toc362010601}[]{#_Toc360799772}[]{#_Toc362010602}[]{#_Toc360799773}[]{#_Toc362010603}[]{#_Toc360799774}[]{#_Toc362010604}[]{#_Toc360799775}[]{#_Toc362010605}[]{#_Toc360799776}[]{#_Toc362010606}[]{#_Toc360799777}[]{#_Toc362010607}[]{#_Toc360799778}[]{#_Toc362010608}[]{#_Toc360799779}[]{#_Toc362010609}[]{#_Toc360799780}[]{#_Toc362010610}[]{#_Toc360799781}[]{#_Toc362010611}[]{#_Toc360799839}[]{#_Toc362010669}

**OSPF \-- OSPF probe命令 \-- display system internal ospf nib**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_x431986886}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_x1741424182}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf nib]{lang="EN-US"}**]{#struct_0_x2081_x5871_319486350}[命令用来显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[分配的下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1452281614}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** **nib** \[ *nib-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x2081_x5871_x1490224042}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1224262127}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_x1233248938}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1237987805}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x458639837}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x432052422}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_863357671}

[*[nib-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x2007349975}[：]{style="font-family:宋体"}[路由下一跳信息的]{style="font-family:宋体"}[ID]{lang="EN-US"}[值，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2081_x5871_x342418308}[：显示]{style="font-family:宋体"}[NIB]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}
:::::

::: {#1536106002 .myid}
[]{#_Toc404800037}[]{#struct_0_x2081_x5871_1080176675}[]{#_Toc363647460}[]{#_Toc357512833}

**OSPF \-- OSPF probe命令 \-- display system internal ospf peer standby**

------------------------------------------------------------------------

[**[display system internal ospf peer standby]{lang="EN-US"}**]{#struct_0_x2081_x5871_2009358476}[命令用来显示备份的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1221245851}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x2081_x5871_1080242211}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] **peer** \[ **verbose** \] \[ *interface-type interface-number* \] \[ *neighbor-id* \] **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_454921853}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2081_x5871_2122634217}[模式：]{style="font-family:宋体"}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] **peer** \[ **verbose** \] \[ *interface-type interface-number* \] \[ *neighbor-id* \] **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_1579963702}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1622714490}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_214458649}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_766475213}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x2070928713}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_2046451746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1079652388}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_1292246531}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的各区域邻居的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2081_x5871_1870873122}[：显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程各区域邻居的概要信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2081_x5871_1174907036}[：接口类型和编号。如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}

[*[neighbor-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_996965094}[：邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。如果未指定本参数，将显示所有邻居路由器的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_261714222}*[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_378015498}*[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**]{#struct_0_x2081_x5871_196755780}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_x1850036994}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1620007141 .myid}
[]{#_Toc404800038}[]{#struct_0_x2081_x5871_x370375834}[]{#_Toc363647461}[]{#_Toc361922329}[]{#_Toc138212553}[]{#_Toc119307763}[]{#_Toc118170392}

**OSPF \-- OSPF probe命令 \-- display system internal ospf peer statistics standby**

------------------------------------------------------------------------

[**[display ]{lang="EN-US"}**]{#struct_0_x2081_x5871_1919574002}**[system internal]{lang="SV"}[ ospf peer statistics standby]{lang="EN-US"}**[命令用来显示备份的本地路由器所有]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[邻居的统计信息，即处于各种状态的邻居数目。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1079717924}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x2081_x5871_2044885935}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **peer** **statistics** **standby** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_620943487}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_x2081_x5871_1060558932}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **peer** **statistics** **standby** **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_x949899696}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x211473588}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2081_x5871_x1307151148}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1549772359}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_462218270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1079521316}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1702805450}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x920819219}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的邻居统计信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_x2131813554}*[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[邻居统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_1166340865}*[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[邻居统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**]{#struct_0_x2081_x5871_1957909485}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[邻居统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_x1850036992}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::::: {#-553072989 .myid}
[]{#_Toc340222337}[]{#_Toc339616735}[]{#_Toc337653104}[]{#_Toc340222295}[]{#_Toc138212554}[]{#_Toc404800039}[]{#struct_0_x2081_x5871_x1618727408}[]{#_Toc348020475}[]{#_Toc340222294}[]{#_Toc338927730}[]{#_Toc360799841}[]{#_Toc362010671}[]{#_Toc360799842}[]{#_Toc362010672}[]{#_Toc360799843}[]{#_Toc362010673}[]{#_Toc360799844}[]{#_Toc362010674}[]{#_Toc360799845}[]{#_Toc362010675}[]{#_Toc360799846}[]{#_Toc362010676}[]{#_Toc360799847}[]{#_Toc362010677}[]{#_Toc360799848}[]{#_Toc362010678}[]{#_Toc360799849}[]{#_Toc362010679}[]{#_Toc360799850}[]{#_Toc362010680}[]{#_Toc360799851}[]{#_Toc362010681}[]{#_Toc360799852}[]{#_Toc362010682}[]{#_Toc360799853}[]{#_Toc362010683}[]{#_Toc360799854}[]{#_Toc362010684}[]{#_Toc360799855}[]{#_Toc362010685}[]{#_Toc360799856}[]{#_Toc362010686}[]{#_Toc360799857}[]{#_Toc362010687}[]{#_Toc360799858}[]{#_Toc362010688}[]{#_Toc360799859}[]{#_Toc362010689}[]{#_Toc360799860}[]{#_Toc362010690}[]{#_Toc360799861}[]{#_Toc362010691}[]{#_Toc360799862}[]{#_Toc362010692}[]{#_Toc360799863}[]{#_Toc362010693}[]{#_Toc360799864}[]{#_Toc362010694}[]{#_Toc360799865}[]{#_Toc362010695}[]{#_Toc360799866}[]{#_Toc362010696}[]{#_Toc360799903}[]{#_Toc362010733}[]{#_Toc360799904}[]{#_Toc362010734}[]{#_Toc360799905}[]{#_Toc362010735}[]{#_Toc360799906}[]{#_Toc362010736}[]{#_Toc360799907}[]{#_Toc362010737}[]{#_Toc360799908}[]{#_Toc362010738}[]{#_Toc360799909}[]{#_Toc362010739}[]{#_Toc360799910}[]{#_Toc362010740}[]{#_Toc360799911}[]{#_Toc362010741}[]{#_Toc360799912}[]{#_Toc362010742}[]{#_Toc360799913}[]{#_Toc362010743}[]{#_Toc360799914}[]{#_Toc362010744}[]{#_Toc360799915}[]{#_Toc362010745}[]{#_Toc360799916}[]{#_Toc362010746}[]{#_Toc360799917}[]{#_Toc362010747}[]{#_Toc360799918}[]{#_Toc362010748}[]{#_Toc360799919}[]{#_Toc362010749}[]{#_Toc360799920}[]{#_Toc362010750}[]{#_Toc360799921}[]{#_Toc362010751}[]{#_Toc360799922}[]{#_Toc362010752}[]{#_Toc360799923}[]{#_Toc362010753}[]{#_Toc360799924}[]{#_Toc362010754}[]{#_Toc360799925}[]{#_Toc362010755}[]{#_Toc360799926}[]{#_Toc362010756}[]{#_Toc360799927}[]{#_Toc362010757}[]{#_Toc360799928}[]{#_Toc362010758}[]{#_Toc360799929}[]{#_Toc362010759}[]{#_Toc360799930}[]{#_Toc362010760}[]{#_Toc360799931}[]{#_Toc362010761}[]{#_Toc360799932}[]{#_Toc362010762}[]{#_Toc360799933}[]{#_Toc362010763}[]{#_Toc360799934}[]{#_Toc362010764}[]{#_Toc360799935}[]{#_Toc362010765}[]{#_Toc360799936}[]{#_Toc362010766}[]{#_Toc360799937}[]{#_Toc362010767}[]{#_Toc360799938}[]{#_Toc362010768}[]{#_Toc360799984}[]{#_Toc362010814}

**OSPF \-- OSPF probe命令 \-- display system internal ospf prefix**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_1588475475}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_x432183493}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf prefix]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1896065372}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[中前缀对应的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_612975674}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** \[ *process-id* \] **prefix** \[ *ip-address* { *mask* \| *mask-length* } \]]{lang="EN-US"}]{#struct_0_x2081_x5871_1545088026}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_46459055}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_x1376660068}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1115308125}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1274759487}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x2027087061}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x431200453}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_209838572}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的前缀信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x2081_x5871_1187096924}[：路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果未指定本参数，将显示所有前缀的信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x2081_x5871_x578527062}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x2081_x5871_1581664620}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}
:::::

::::: {#-43594690 .myid}
[]{#_Toc404800040}[]{#struct_0_x2081_x5871_422171298}[]{#_Toc371424083}[]{#_Toc366565715}

**OSPF \-- OSPF probe命令 \-- display system internal ospf router**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_1402275952}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_1007840054}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf router]{lang="EN-US"}**]{#struct_0_x2081_x5871_1032987365}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[中到路由器节点的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x2081_x5871_x443828699}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** \[ *process-id* \] **router**]{lang="EN-US"}]{#struct_0_x2081_x5871_390903473}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x2081_x5871_1535569361}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_422236834}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x2081_x5871_x1927953518}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_2139170975}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1631520818}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x2081_x5871_x692513674}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1124022215}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的信息。]{style="font-family:宋体"}
:::::

::::: {#-329775856 .myid}
[]{#_Toc404800041}[]{#struct_0_x2081_x5871_364788073}[]{#_Toc371424084}

**OSPF \-- OSPF probe命令 \-- display system internal ospf statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_837892586}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_2079042958}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf statistics]{lang="EN-US"}**]{#struct_0_x2081_x5871_421647009}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1413804191}

[**[display system internal ospf ]{lang="EN-US"}**[\[ *process-id* \] **statistics** { **request-queue \| retrans-queue** } \[ *interface-type interface-number* \] \[ *neighbor-id* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_1511708304}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x553080421}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_1491530150}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1466259463}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x2025380909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_15713506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x104061619}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1408211688}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[**[request-queue]{lang="EN-US"}**]{#struct_0_x2081_x5871_387794532}[：邻居请求链计数。]{style="font-family:宋体"}

[**[retrans-queue]{lang="EN-US"}**]{#struct_0_x2081_x5871_421712545}[：邻居重传链计数。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2081_x5871_1036340621}[：接口类型和编号]{style="font-family:宋体"}[，显示指定接口的统计信息。]{style="font-family:宋体"}

[*[neighbor-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1877142208}[：显示指定邻居的统计信息。]{style="font-family:宋体"}
:::::

::::: {#-979535690 .myid}
[]{#_Toc404800042}[]{#struct_0_x2081_x5871_x1728425276}[]{#_Toc348020476}[]{#_Toc360799986}[]{#_Toc362010816}[]{#_Toc360799987}[]{#_Toc362010817}[]{#_Toc360799988}[]{#_Toc362010818}[]{#_Toc360799989}[]{#_Toc362010819}[]{#_Toc360799990}[]{#_Toc362010820}[]{#_Toc360799991}[]{#_Toc362010821}[]{#_Toc360799992}[]{#_Toc362010822}[]{#_Toc360799993}[]{#_Toc362010823}[]{#_Toc360799994}[]{#_Toc362010824}[]{#_Toc360799995}[]{#_Toc362010825}[]{#_Toc360799996}[]{#_Toc362010826}[]{#_Toc360799997}[]{#_Toc362010827}[]{#_Toc360799998}[]{#_Toc362010828}[]{#_Toc360799999}[]{#_Toc362010829}[]{#_Toc360800000}[]{#_Toc362010830}[]{#_Toc360800001}[]{#_Toc362010831}[]{#_Toc360800002}[]{#_Toc362010832}[]{#_Toc360800032}[]{#_Toc362010862}

**OSPF \-- OSPF probe命令 \-- display system internal ospf status**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_x1316542422}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_x431921348}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display system internal ospf status]{lang="EN-US"}**]{#struct_0_x2081_x5871_580677209}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议状态信息，包括内存门限状态，及各模块相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x417125808}

[**[display]{lang="EN-US"}**[ **system** **internal** **ospf** **status**]{lang="EN-US"}]{#struct_0_x2081_x5871_x1112330261}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_345063614}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_x1246666445}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1363192174}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_636209096}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x690473403}
:::::

::: {#2009505940 .myid}
[]{#_Toc404800043}[]{#struct_0_x2081_x5871_1079390244}[]{#_Toc363647462}[]{#_Toc357512835}

**OSPF \-- OSPF probe命令 \-- display system internal ospf vlink standby**

------------------------------------------------------------------------

[**[display system internal ospf vlink standby]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1835256538}[命令用来显示备份的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[虚连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_2040344512}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_x2081_x5871_x1870502843}[－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ospf]{lang="EN-US"}**[ \[ *process-id* \] **vlink** **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_x915858353}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2081_x5871_759199732}[模式：]{style="font-family:宋体"}

[**[display system internal ospf]{lang="EN-US"}**[ \[ *process-id* \] **vlink** **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2081_x5871_56472744}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1079455780}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_x1037987236}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_1813640538}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_724698336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x477841764}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x697266586}

[*[process-id]{lang="EN-US"}*]{#struct_0_x2081_x5871_x1750528336}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的虚连接信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_x1869898916}*[ slot-number]{lang="EN-US"}*[：显示备份的指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[虚连接信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[虚连接]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}**]{#struct_0_x2081_x5871_1079259172}*[ slot-number]{lang="EN-US"}*[：显示备份的指定成员设备的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[虚连接]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[虚连接]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**]{#struct_0_x2081_x5871_957619159}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示备份的指定成员设备上指定单板的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[虚连接]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[虚连接]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2081_x5871_x1850036996}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::::: {#-639876777 .myid}
[]{#_Toc404800044}[]{#_Toc348020478}[]{#struct_0_x2081_x5871_x431790275}[]{#_Toc340222353}[]{#_Toc339616742}[]{#_Toc337654564}[]{#_Toc360800034}[]{#_Toc362010864}[]{#_Toc360800035}[]{#_Toc362010865}[]{#_Toc360800036}[]{#_Toc362010866}[]{#_Toc360800037}[]{#_Toc362010867}[]{#_Toc360800038}[]{#_Toc362010868}[]{#_Toc360800039}[]{#_Toc362010869}[]{#_Toc360800040}[]{#_Toc362010870}[]{#_Toc360800041}[]{#_Toc362010871}[]{#_Toc360800042}[]{#_Toc362010872}[]{#_Toc360800043}[]{#_Toc362010873}[]{#_Toc360800044}[]{#_Toc362010874}[]{#_Toc360800045}[]{#_Toc362010875}[]{#_Toc360800046}[]{#_Toc362010876}[]{#_Toc360800047}[]{#_Toc362010877}[]{#_Toc360800048}[]{#_Toc362010878}[]{#_Toc360800049}[]{#_Toc362010879}[]{#_Toc360800050}[]{#_Toc362010880}[]{#_Toc360800051}[]{#_Toc362010881}[]{#_Toc360800093}[]{#_Toc362010923}[]{#_Toc355942334}[]{#_Toc355942335}[]{#_Toc355942336}[]{#_Toc355942337}[]{#_Toc355942338}[]{#_Toc355942339}[]{#_Toc355942340}[]{#_Toc355942341}[]{#_Toc355942342}[]{#_Toc355942343}[]{#_Toc355942344}[]{#_Toc355942345}[]{#_Toc355942346}[]{#_Toc355942347}[]{#_Toc355942348}[]{#_Toc355942349}[]{#_Toc355942350}[]{#_Toc355942351}[]{#_Toc355942352}[]{#_Toc355942353}[]{#_Toc355942354}[]{#_Toc355942355}[]{#_Toc355942356}[]{#_Toc355942357}[]{#_Toc355942358}[]{#_Toc355942359}

**OSPF \-- OSPF probe命令 \-- reset system internal ospf event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF%20Probe命令.files/image002.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2081_x5871_1338041013}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2081_x5871_x1194942337}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[reset system internal ospf event-log]{lang="EN-US"}**]{#struct_0_x2081_x5871_x431855811}[命令用来清除]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x431921347}

[**[reset]{lang="EN-US"}**[ **system internal ospf** **event-log** { **interface** \| **nib** \| **notify** }]{lang="EN-US"}]{#struct_0_x2081_x5871_x431986883}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x1741227574}

[[Probe]{lang="EN-US"}]{#struct_0_x2081_x5871_x697036716}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_x2143285641}

[[network-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_1195465542}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2081_x5871_x1853901322}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2081_x5871_261269570}

[**[interface]{lang="EN-US"}**]{#struct_0_x2081_x5871_2132825782}[：接口事件相关日志。]{style="font-family:宋体"}

[**[nib]{lang="EN-US"}**]{#struct_0_x2081_x5871_x432052419}[：]{style="font-family:宋体"}[NIB]{lang="EN-US"}[的相关日志。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_x2081_x5871_862767844}[：接口通知相关日志。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::::
