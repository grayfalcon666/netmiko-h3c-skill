::::: {#853638386 .myid}
[]{#_Toc404798642}[]{#struct_0_x1539_x1935_x833635611}[]{#_Toc393878946}[]{#_Toc383786740}[]{#_Toc383097749}[]{#_Toc376856930}[]{#_Toc371411810}

**VXLAN \-- VXLAN基础配置命令 \-- arp suppression enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_1648335821}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_1798104613}
:::

[ ]{lang="EN-US"}

[**[arp suppression enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_959982328}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[**[undo arp suppression enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x833635610}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1648270285}

[]{#_Toc178914661}[**[arp suppression enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x508476401}

[**[undo arp suppression enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_765385367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x833635609}

[[ARP]{lang="EN-US"}]{#struct_0_x1539_x1935_1648860110}[泛洪抑制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2080226610}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635608}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1648794574}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x906006271}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635607}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1648466894}

[[为了避免广播发送的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1539_x1935_x2082699336}[请求报文占用核心网络带宽，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[从本地站点、]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道接收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求和]{style="font-family:宋体"}[ARP]{lang="EN-US"}[应答报文后，根据该报文在本地建立]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。后续当]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[收到本站点内虚拟机请求其它虚拟机]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求时，优先根据]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项进行代答。如果没有对应的表项，则将]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求泛洪到核心网。]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能可以大大减少]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪的次数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x135245601}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635606}[在]{style="font-family:宋体"}[VSI vsi1]{lang="EN-US"}[下开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1648401358}

[\[Sysname\] vsi vsi1]{lang="EN-US"}

[\[Sysname-vsi-vsi1\] arp suppression enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_253868009}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp suppression]{lang="EN-US"}**]{#struct_0_x1539_x1935_x833635605}**[ vsi]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset arp suppression]{lang="EN-US"}**]{#struct_0_x1539_x1935_1648597966}**[ vsi]{lang="EN-US"}**
:::::

::: {#-1461383778 .myid}
[]{#_Toc404798643}[]{#struct_0_x1539_x1935_1859280128}[]{#_Toc375835809}

**VXLAN \-- VXLAN基础配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1539_x1935_1314967229}[命令用来设置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1002997609}[命令用来删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x78128063}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x1539_x1935_1786594374}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1358018249}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_143333773}

[[未配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x315836560}[的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1303690325}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1705911206}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1053845667}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1557172368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1703230401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_622273579}

[*[text]{lang="EN-US"}*]{#struct_0_x1539_x1935_1660204922}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1314399863}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1314901693}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[vsi for vpn1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1404792980}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] description vsi for vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1422485703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_384641513}
:::

::::: {#-530734358 .myid}
[]{#_Toc404798644}[]{#struct_0_x1539_x1935_x1642939674}[]{#_Toc393878948}[]{#_Toc383786741}[]{#_Toc383097750}[]{#_Toc376856931}[]{#_Toc371411811}

**VXLAN \-- VXLAN基础配置命令 \-- display arp suppression vsi**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x1053084078}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x1642939673}
:::

[ ]{lang="EN-US"}

[**[display arp suppression vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1456368605}[命令用来显示]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x485252309}

[]{#_Toc178914662}[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x70100206}

[**[display arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939672}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1539_x1935_109715336}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x1722221889}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1539_x1935_x273239457}[模式：]{style="font-family:宋体"}

[**[display arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939671}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x293569191}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1206383460}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2105086617}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939670}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1272514750}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_21497549}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1826251085}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1642939669}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_x649734015}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1675870461}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939668}[：显示指定成员设备的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1539_x1935_x5909580}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1539_x1935_916349926}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1755733355}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1417298097}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x1539_x1935_313375459}[：显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项的个数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1699625545}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1567340087}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_313375460}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026608}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_x1539_x1935_313375461}

[Total entries: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026607}[显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_313375462}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026610}[显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_x1539_x1935_692582521}

[Total entries: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1570552211}[显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_313375463}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026609}[显示主设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_x1539_x1935_313375464}

[Total entries: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026604}[显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_313375465}

[IP address      MAC address    Vsi Name                        Link ID    Aging]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 vsi1                            0x70000    14]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 vsi1                            0x80000    18]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 vsi2                            0x90000    10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026603}[显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression vsi count]{lang="EN-US"}]{#struct_0_x1539_x1935_692385912}

[Total entries: 3]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display arp suppression vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_313375466}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1356520968}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x639026606}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_313375467}

[[IP address]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026605}

[[ARP]{lang="EN-US"}]{#struct_0_x1539_x1935_313375468}[泛洪抑制表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1539_x1935_x639026616}

[[ARP]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516259}[泛洪抑制表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Vsi Name]{lang="EN-US"}]{#struct_0_x1539_x1935_1946771458}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516260}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1946181631}

[[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516261}[表项的出链路标识符，用来在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内唯一标识一条]{style="font-family:宋体"}[AC]{lang="EN-US"}[或一条]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_x1539_x1935_1946247167}

[[ARP]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516262}[泛洪抑制表项的老化时间，单位为分钟]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_x1539_x1935_1946312703}

[[ARP]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516263}[泛洪抑制表项的数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1946378239}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp suppression enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_716695764}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset arp suppression]{lang="EN-US"}**]{#struct_0_x1539_x1935_x2038469784}**[ vsi]{lang="EN-US"}**

::: {#305400511 .myid}
[]{#_Toc404798645}[]{#struct_0_x1539_x1935_x1359028732}[]{#_Toc374372845}[]{#_Toc355963320}[]{#_Toc378672367}[]{#_Toc378672422}[]{#_Toc378683222}[]{#_Toc378683277}[]{#_Toc378683958}[]{#_Toc379547054}[]{#_Toc390073115}

**VXLAN \-- VXLAN基础配置命令 \-- display igmp host group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp** **host** **group**]{lang="EN-US"}]{#struct_0_x1539_x1935_1924157855}[命令用来显示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[执行主机行为的所有组播组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_25345835}

[**[display]{lang="EN-US"}**[ **igmp** **host** **group** \[ *group-address* \| **interface** *interface-type* *interface-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_2130999707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x937937010}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1536129752}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1239719453}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x620542724}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1107356272}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1597705538}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1315098301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_103852541}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1539_x1935_345951602}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，则显示所有组播组的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1395564204}[：显示指定接口上的信息。如果未指定本参数，则显示所有接口上的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1539_x1935_850252641}[：显示详细信息。如果未指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x373610908}

[[采用组播路由方式泛洪流量时，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1031930561}[组播报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所在的接口需要作为]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[主机加入]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[所在的组播组。通过本命令可以查看接口是否加入组播组，及该组播组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1849420810}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1243869774}[显示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[执行主机行为的所有组播组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp host group]{lang="EN-US"}]{#struct_0_x1539_x1935_x1737307507}

[IGMP host groups in total: 2]{lang="EN-US"}

[ Vlan-interface10(1.1.1.20):]{lang="EN-US"}

[  IGMP host groups in total: 2]{lang="EN-US"}

[   Group address      Member state      Expires]{lang="EN-US"}

[   225.1.1.1          Idle              Off]{lang="EN-US"}

[   225.1.1.2          Idle              Off]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x700883243}[显示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[执行主机行为的所有组播组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp host group verbose]{lang="EN-US"}]{#struct_0_x1539_x1935_1315229373}

[ Vlan-interface10(1.1.1.20):]{lang="EN-US"}

[  IGMP host groups in total: 2]{lang="EN-US"}

[   Group: 225.1.1.1]{lang="EN-US"}

[     Group mode: Exclude]{lang="EN-US"}

[     Member state: Idle]{lang="EN-US"}

[     Expires: Off]{lang="EN-US"}

[     Source list (sources in total: 0):]{lang="EN-US"}

[   Group: 225.1.1.2]{lang="EN-US"}

[     Group mode: Exclude]{lang="EN-US"}

[     Member state: Idle]{lang="EN-US"}

[     Expires: Off]{lang="EN-US"}

[     Source list (sources in total: 0):]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display igmp host group]{lang="EN-US"}]{#struct_0_x1539_x1935_1687172517}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1945862375}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1087336933}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1315163837}

[[IGMP host groups in total]{lang="EN-US"}]{#struct_0_x1539_x1935_604022580}

[[IGMP]{lang="EN-US"}]{#struct_0_x1539_x1935_2051328062}[执行主机行为的组播组总数]{style="font-family:宋体"}

[[Vlan-interface10(1.1.1.20)]{lang="EN-US"}]{#struct_0_x1539_x1935_1329904835}

[[IGMP]{lang="EN-US"}]{#struct_0_x1539_x1935_209215564}[执行主机行为的接口的名称和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IGMP host groups in total]{lang="EN-US"}]{#struct_0_x1539_x1935_1315360445}

[[当前接口下]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1800075964}[执行主机行为的组播组数目]{style="font-family:宋体"}

[[Group address/Group]{lang="EN-US"}]{#struct_0_x1539_x1935_312888459}

[[组播组地址]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1315294909}

[[Member state]{lang="EN-US"}]{#struct_0_x1539_x1935_161011667}

[[组播组成员的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_345108032}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delay]{lang="EN-US"}]{#struct_0_x1539_x1935_1315491517}[：表示加入了组播组，并对该组启动了延迟发送报告报文的定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x1539_x1935_1695649797}[：表示加入了组播组，但对该组尚未启动延迟发送报告报文的定时器]{style="font-family:宋体"}

[[延迟发送报告报文定时器的值不可配置]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x63684864}

[[Expires]{lang="EN-US"}]{#struct_0_x1539_x1935_1315425981}

[[组播组延迟发送报告报文的剩余时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}]{#struct_0_x1539_x1935_1744986746}[表示该定时器关闭]{style="font-family:宋体"}

[[Group mode]{lang="EN-US"}]{#struct_0_x1539_x1935_x1962768624}

[[对组播源的过滤模式，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1077155637}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Include]{lang="EN-US"}]{#struct_0_x1539_x1935_1314967230}[：表示]{lang="EN-US" style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exclude]{lang="EN-US"}]{#struct_0_x1539_x1935_x1002538856}[：表示]{lang="EN-US" style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Source list]{lang="EN-US"}]{#struct_0_x1539_x1935_1314901694}

[[IGMP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1404727444}[执行主机行为的组播组所包含的组播源列表]{style="font-family:宋体"}

[[sources in total]{lang="EN-US"}]{#struct_0_x1539_x1935_1075632545}

[[组播源的总数]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1315098302}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image002.png){#图片 16 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_103787005}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[对本命令的显示信息更加详细的介绍，请参见"]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_2049578006}[IP]{lang="EN-US"}[组播配置指导"中的"]{style="font-family:楷体_GB2312"}[IGMP]{lang="EN-US"}["。]{style="font-family:楷体_GB2312"}
:::

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1416158288}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp host enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_2021042646}

::: {#356357916 .myid}
[]{#_Toc404798646}[]{#struct_0_x1539_x1935_727650457}

**VXLAN \-- VXLAN基础配置命令 \-- display l2vpn mac-address**

------------------------------------------------------------------------

[**[display l2vpn mac-address]{lang="EN-US"}**]{#struct_0_x1539_x1935_1702948177}[命令用来显示]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1771030431}

[**[display l2vpn mac-address ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ **dynamic** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x717867767}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_931481529}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_150634877}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1315032766}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x639689739}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1410536208}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1247669688}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x2026152689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x115753663}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_x1539_x1935_x891325203}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_x1539_x1935_272008085}[：显示通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。如果不指定本参数，则显示所有类型的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，包括通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的本地和远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项、通过]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议学习的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项、静态配置的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[不支持静态配置本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x1539_x1935_1314006873}[：显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数目。如果不指定本参数，则显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_575204960}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1351828553}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn mac-address]{lang="EN-US"}]{#struct_0_x1539_x1935_1315229374}

[MAC Address      State    VSI Name                        Link ID/Name  Aging]{lang="EN-US"}

[0000-0000-000a   dynamic  vpn1                            1             Aging]{lang="EN-US"}

[0000-0000-000b   static   vpn1                            Tunnel10      NotAging]{lang="EN-US"}

[0000-0000-000c   dynamic  vpn1                            Tunnel60      Aging]{lang="EN-US"}

[0000-0000-000d   dynamic  vpn1                            Tunnel99      Aging]{lang="EN-US"}

[\-\-- 4 mac address(es) found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1686975909}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项总数。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn mac-address count]{lang="EN-US"}]{#struct_0_x1539_x1935_x331760303}

[4 mac address(es) found]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display l2vpn mac-address]{lang="EN-US"}]{#struct_0_x1539_x1935_x1044389194}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1916675629}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1887308798}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_250204854}

[[MAC Address]{lang="EN-US"}]{#struct_0_x1539_x1935_1315163838}

[[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_603301684}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_x1165160868}

[[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1770092848}[地址的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_x1539_x1935_1541065412}[：表示通过]{style="font-family:宋体"}[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的本地或远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static]{lang="EN-US"}]{#struct_0_x1539_x1935_x1169627643}[：表示静态配置的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项（]{style="font-family:宋体"}[Aging]{lang="EN-US"}[字段取值为]{style="font-family:宋体"}[NotAging]{lang="EN-US"}[）或]{style="font-family:宋体"}[通过]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议学习的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项（]{style="font-family:宋体"}[Aging]{lang="EN-US"}[字段取值为]{style="font-family:宋体"}[Aging]{lang="EN-US"}[）]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_x1539_x1935_944341197}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1483876974}[名称]{style="font-family:宋体"}

[[Link ID/Name]{lang="EN-US"}]{#struct_0_x1539_x1935_x815994860}

[[对于本端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x901536408}[地址，为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的出链路标识符，即]{style="font-family:宋体"}[AC]{lang="EN-US"}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符；对于远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应的隧道名称]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_x1539_x1935_929225337}

[[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_1315360446}[地址表项是否老化，取值包括]{style="font-family:宋体"}[Aging]{lang="EN-US"}[和]{style="font-family:宋体"}[NotAging]{lang="EN-US"}

[[XX mac address(es) found]{lang="EN-US"}]{#struct_0_x1539_x1935_x1800272572}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x979672231}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x367465484}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset l2vpn mac-address]{lang="EN-US"}**]{#struct_0_x1539_x1935_x158177197}

::: {#-1122099741 .myid}
[]{#_Toc404798647}[]{#struct_0_x1539_x1935_1790689730}[]{#_Toc375835820}

**VXLAN \-- VXLAN基础配置命令 \-- display l2vpn service-instance**

------------------------------------------------------------------------

[**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x1539_x1935_798572278}[命令用来显示以太网服务实例的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1267037161}

[**[display l2vpn service-instance ]{lang="EN-US"}**[\[ **interface**]{lang="EN-US"}*[ interface-type interface-number]{lang="EN-US"}*[ \[ **service-instance** *instance-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x361790449}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1747771037}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x652814911}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1315294910}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_161601490}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x27404400}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1676815353}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x1489509659}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1452188395}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_x1065498173}[：显示指定二层以太网接口或二层聚合接口上的以太网服务实例信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则显示所有二层以太网接口和二层聚合接口上的以太网服务实例信息。]{style="font-family:
宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1838162898}[：显示指定以太网服务实例的信息。]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。如果指定了]{style="font-family:宋体"}**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*[参数，没有指定本参数，则显示指定二层以太网接口或二层聚合接口上所有以太网服务实例的信息。]{style="font-family:
宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1539_x1935_758840875}[：显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x547768276}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x31279543}[显示所有以太网服务实例的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance]{lang="EN-US"}]{#struct_0_x1539_x1935_1315491518}

[Total number of service-instances: 4, 4 up, 0 down]{lang="EN-US"}

[Total number of ACs: 4, 4 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                SrvID Owner                           LinkID State Type]{lang="EN-US"}

[GE1/0/3                  1     vsi10                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  2     vsi11                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  3     vsi12                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  4     vsi13                           1      Up    VSI]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display l2vpn service-instance]{lang="EN-US"}]{#struct_0_x1539_x1935_1695584261}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1914191949}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1701565837}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_930945688}

[[Total number of service-instances]{lang="EN-US"}]{#struct_0_x1539_x1935_x312006084}

[[以太网服务实例的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1539_x1935_1836825319}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的以太网服务实例数目]{style="font-family:宋体"}

[[Total number of ACs]{lang="EN-US"}]{#struct_0_x1539_x1935_1315425982}

[[AC]{lang="EN-US"}]{#struct_0_x1539_x1935_1744790138}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[AC]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_1136542577}

[[二层以太网接口或二层聚合接口名称]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1031929257}

[[SrvID ]{lang="EN-US"}]{#struct_0_x1539_x1935_x734116810}

[[以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1970206936}

[[Owner]{lang="EN-US"}]{#struct_0_x1539_x1935_200077544}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x564568491}[名称，如果以太网服务实例上尚未关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，则本字段显示为空]{style="font-family:宋体"}

[[LinkID]{lang="EN-US"}]{#struct_0_x1539_x1935_x600727932}

[[以太网服务实例在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x563458222}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_x1572045715}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x1539_x1935_x2002071143}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x1539_x1935_1575500402}

[[以太网服务实例所属的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x1539_x1935_1500394595}[类型，取值包括]{style="font-family:宋体"}[VSI]{lang="EN-US"}[和]{style="font-family:宋体"}[VPWS]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1457981841}[显示二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[上所有以太网服务实例的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/3 verbose]{lang="EN-US"}]{#struct_0_x1539_x1935_x600662396}

[Interface: GE1/0/3]{lang="EN-US"}

[  Service Instance: 1]{lang="EN-US"}

[    Encapsulation : s-vid 1 to 16]{lang="EN-US"}

[    VSI Name      : vsi10]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 2]{lang="EN-US"}

[    Encapsulation : s-vid 1001 to 1016]{lang="EN-US"}

[                    only-tagged]{lang="EN-US"}

[    VSI Name      : vsi11]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 3]{lang="EN-US"}

[    Encapsulation : s-vid 2000]{lang="EN-US"}

[                    c-vid 1001 to 1002 1015 to 1016]{lang="EN-US"}

[    VSI Name      : vsi12]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display l2vpn service-instance verbose]{lang="EN-US"}]{#struct_0_x1539_x1935_x167049098}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1917218611}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600859004}

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2118323032}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_x1937073615}

[[二层以太网接口或二层聚合接口]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x634732501}

[[Service Instance]{lang="EN-US"}]{#struct_0_x1539_x1935_557042667}

[[以太网服务实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1758847023}

[[Encapsulation]{lang="EN-US"}]{#struct_0_x1539_x1935_x973474867}

[[以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则不显示本字段]{style="font-family:宋体"}]{#struct_0_x1539_x1935_2044581105}

[[VSI Name]{lang="EN-US"}]{#struct_0_x1539_x1935_180923411}

[[与以太网服务实例关联的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_2123363991}[的名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x600793468}

[[以太网服务实例在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x190022421}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_1179859981}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x1539_x1935_x2022303084}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502333829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service-instance]{lang="EN-US"}**]{#struct_0_x1539_x1935_x737759377}

::: {#-1007637280 .myid}
[]{#_Toc404798648}[]{#struct_0_x1539_x1935_613487347}[]{#_Toc372102896}[]{#_Toc334795167}

**VXLAN \-- VXLAN基础配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

[**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_x9081544}[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600990076}

[**[display]{lang="EN-US"}**[ **l2vpn** **vsi** \[ **name** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x991301181}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x685067983}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1358388786}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1410719898}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_863450362}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x603348229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_60069366}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x2129789819}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2106738890}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_x190204345}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1204750357}[：显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600924540}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1364736978}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_x314395543}

[Total number of VSIs: 1, 1 up, 0 down, 0 admin down]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name                        VSI Index       MTU    State]{lang="EN-US"}

[vpna                            0               1500   Up]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x675139567}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi verbose]{lang="EN-US"}]{#struct_0_x1539_x1935_x601121148}

[VSI Name: vpna]{lang="EN-US"}

[  VSI Index               : 0]{lang="EN-US"}

[  VSI State               : Up]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : -]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  Flooding                : Enabled]{lang="EN-US"}

[  Statistics              : Enabled]{lang="EN-US"}

[  Input statistics:]{lang="EN-US"}

[    Octets   : 0]{lang="EN-US"}

[    Packets  : 0]{lang="EN-US"}

[    Errors   : 0]{lang="EN-US"}

[    Discards : 0]{lang="EN-US"}

[  Output statistics:]{lang="EN-US"}

[    Octets   : 0]{lang="EN-US"}

[    Packets  : 0]{lang="EN-US"}

[    Errors   : 0]{lang="EN-US"}

[    Discards : 0]{lang="EN-US"}

[  Gateway Interface       : VSI-interface 100]{lang="EN-US"}

[  VXLAN ID                : 10]{lang="EN-US"}

[  Tunnels:]{lang="EN-US"}

[    Tunnel Name          Link ID    State  Type]{lang="EN-US"}

[    Tunnel1              0x5000001  Up     Manual]{lang="EN-US"}

[    Tunnel2              0x5000002  Up     Manual]{lang="EN-US"}

[    MTunnel0             0x6002710  Up     Auto]{lang="EN-US"}

[  ACs:]{lang="EN-US"}

[    AC                               Link ID    State]{lang="EN-US"}

[    GE1/0/1 srv1000                  0          Up]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display l2vpn vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_205415797}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1925179177}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x393222165}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_506018887}

[[VSI Name]{lang="EN-US"}]{#struct_0_x1539_x1935_996515276}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_176315117}[名称]{style="font-family:宋体"}

[[VSI Index]{lang="EN-US"}]{#struct_0_x1539_x1935_x602355636}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x321963996}[索引]{style="font-family:宋体"}

[[VSI Description]{lang="EN-US"}]{#struct_0_x1539_x1935_x601055612}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_194000773}[的描述信息，如果不配置，则此行不显示]{style="font-family:宋体"}

[[VSI State]{lang="EN-US"}]{#struct_0_x1539_x1935_x389153584}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1987981372}[的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1539_x1935_1176370414}[：]{style="font-family:宋体"}[up]{lang="EN-US"}[状态。只有]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联了处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的隧道和]{style="font-family:宋体"}[AC]{lang="EN-US"}[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[才会处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1539_x1935_1258829099}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_x1539_x1935_x916368307}[：通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令手工关闭]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}

[[MTU]{lang="EN-US"}]{#struct_0_x1539_x1935_x600203644}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x554861536}[上配置的最大传输单元]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x1539_x1935_621444724}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x808887365}[的带宽限制值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}

[[Broadcast Restrain]{lang="EN-US"}]{#struct_0_x1539_x1935_x1373024331}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_69322108}[的广播抑制百分比]{style="font-family:宋体"}

[[Multicast Restrain]{lang="EN-US"}]{#struct_0_x1539_x1935_x1179057033}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x600138108}[的组播抑制百分比]{style="font-family:宋体"}

[[Unknown Unicast Restrain]{lang="EN-US"}]{#struct_0_x1539_x1935_1722979766}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x468890575}[的未知单播抑制百分比]{style="font-family:宋体"}

[[MAC Learning]{lang="EN-US"}]{#struct_0_x1539_x1935_1278484933}

[[是否使能了]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1243347216}[地址学习功能]{style="font-family:宋体"}

[[MAC Table Limit]{lang="EN-US"}]{#struct_0_x1539_x1935_709522996}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1966679416}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[Drop Unknown]{lang="EN-US"}]{#struct_0_x1539_x1935_x600727931}

[[当]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x563392686}[内学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，是否禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文]{style="font-family:宋体"}

[[Hub-Spoke]{lang="EN-US"}]{#struct_0_x1539_x1935_687540784}

[[是否使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}]{#struct_0_x1539_x1935_959864329}[能力]{style="font-family:宋体"}

[[Flooding]{lang="EN-US"}]{#struct_0_x1539_x1935_x49604550}

[[是否使能]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x2053799150}[的泛洪功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x600662395}[：表示使能]{style="font-family:宋体"}[了]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能，即]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[会将目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知的单播数据帧发送给所有本地和远端站点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x166983562}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[禁止]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能]{lang="EN-US" style="font-family:宋体"}[，即]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[只将目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知的单播数据帧发送给所有本地站点]{style="font-family:宋体"}

[[Statistics]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329706}

[[是否使能]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329707}[的统计功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329708}[：使能了]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[的统计功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322461}[：禁止]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[的统计功能]{lang="EN-US" style="font-family:宋体"}

[[Input statistics]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322460}

[[入方向的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322459}[报文统计信息，包括入方向接收的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、接收的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、接收的错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Output statistics]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322458}

[[出方向的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322457}[报文统计信息，包括出方向发送的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、发送的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Gateway Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322456}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322454}[网关虚接口编号]{style="font-family:宋体"}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1883733876}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x700054915}[编号]{style="font-family:宋体"}

[[Tunnels]{lang="EN-US"}]{#struct_0_x1539_x1935_1938211562}

[[与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x600859003}[关联的隧道信息]{style="font-family:宋体"}

[[Tunnel Name]{lang="EN-US"}]{#struct_0_x1539_x1935_2117995352}

[[隧道名称]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1011722969}

[[Link ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1647230544}

[[隧道在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x600793467}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_x189825813}

[[隧道状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x1539_x1935_1982827636}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x1539_x1935_1780798524}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1695231434}[和]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道的关联方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1539_x1935_1077491423}[：表示自动关联，分为以下两种：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[通过]{style="font-family:
  宋体"}]{#struct_0_x1539_x1935_x600990075}[VXLAN ISIS]{lang="EN-US"}[协商]{style="font-family:
  宋体"}[VXLAN ID]{lang="EN-US"}[后，自动将]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道关联；]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[在组播路由方式下，自动创建用于转发泛洪流量的组播]{style="font-family:
  宋体"}]{#struct_0_x1539_x1935_x991104573}[VXLAN]{lang="EN-US"}[隧道（]{style="font-family:宋体"}[MTunnel]{lang="EN-US"}[），并将其与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1539_x1935_x690358263}[：表示手动关联]{lang="EN-US" style="font-family:宋体"}[VXLAN]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道]{lang="EN-US" style="font-family:宋体"}

[[ACs]{lang="EN-US"}]{#struct_0_x1539_x1935_x2142469883}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x600924539}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1364278221}

[[接入电路]{style="font-family:宋体"}]{#struct_0_x1539_x1935_930459115}

[[Link ID]{lang="EN-US"}]{#struct_0_x1539_x1935_387560967}

[[AC]{lang="EN-US"}]{#struct_0_x1539_x1935_x601121147}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_204432757}

[[AC]{lang="EN-US"}]{#struct_0_x1539_x1935_1761800104}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-997314772 .myid}
[]{#_Toc404798649}[]{#struct_0_x1539_x1935_709644995}[]{#_Toc372102898}

**VXLAN \-- VXLAN基础配置命令 \-- display vxlan tunnel**

------------------------------------------------------------------------

[**[display vxlan tunnel]{lang="EN-US"}**]{#struct_0_x1539_x1935_x601055611}[命令用来显示与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_194197381}

[**[display]{lang="EN-US"}**[ **vxlan tunnel** \[ **vxlan-id** *vxlan-id* \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x7025131}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1089757685}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x2110835552}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1662530594}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_994159342}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_779283646}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x963958426}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_348814543}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1169902117}

[*[vxlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_955575282}[：显示与指定]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联的隧道的信息。]{style="font-family:宋体"}*[vxlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。不指定此参数，则显示所有与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联的隧道的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600203643}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x554533856}[显示所有与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联的隧道的信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_x894331749}

[Total number of VXLANs: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VXLAN ID: 10, VSI name: vpna, Total tunnels: 4 (4 up, 0 down)]{lang="EN-US"}

[Tunnel name          Link ID    State  Type]{lang="EN-US"}

[Tunnel0              0x5000000  Up     Auto]{lang="EN-US"}

[Tunnel1              0x5000001  Up     Manual]{lang="EN-US"}

[Tunnel2              0x5000002  Up     Manual/Auto]{lang="EN-US"}

[MTunnel0             0x6002710  Up     Auto]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_43495725}[显示与编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联的隧道的信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan tunnel vxlan-id 10]{lang="EN-US"}]{#struct_0_x1539_x1935_691096131}

[VXLAN ID: 10, VSI name: vpna, Total tunnels: 4 (4 up, 0 down)]{lang="EN-US"}

[Tunnel name          Link ID    State  Type]{lang="EN-US"}

[Tunnel0              0x5000000  Up     Auto]{lang="EN-US"}

[Tunnel1              0x5000001  Up     Manual]{lang="EN-US"}

[Tunnel2              0x5000002  Up     Manual/Auto]{lang="EN-US"}

[MTunnel0             0x6002710  Up     Auto]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display vxlan tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_270431147}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1899627907}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1454601377}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1217105516}

[[Total number of VXLANs]{lang="EN-US"}]{#struct_0_x1539_x1935_x1303092520}

[[已创建的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x600138107}[的总数]{style="font-family:宋体"}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1723962806}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x800187410}

[[VSI name]{lang="EN-US"}]{#struct_0_x1539_x1935_x1200664911}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1271932875}[所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Total tunnels]{lang="EN-US"}]{#struct_0_x1539_x1935_188357913}

[[与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x712620399}[关联的隧道的]{style="font-family:宋体"}[总数，包括处于]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态的隧道总数]{style="font-family:宋体"}

[[Tunnel name]{lang="EN-US"}]{#struct_0_x1539_x1935_x1189424409}

[[隧道名称]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x600727934}

[[Link ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x563589294}

[[隧道在]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1130557678}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_x491800926}

[[隧道的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x1539_x1935_x57137493}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x1539_x1935_x1334455130}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x600662398}[和]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道的关联方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1539_x1935_x167704458}[：表示自动关联，分为以下两种：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[通过]{style="font-family:
  宋体"}]{#struct_0_x1539_x1935_1545532368}[VXLAN ISIS]{lang="EN-US"}[协商]{style="font-family:
  宋体"}[VXLAN ID]{lang="EN-US"}[后，自动将]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道关联；]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[在组播路由方式下，自动创建用于转发泛洪流量的组播]{style="font-family:
  宋体"}]{#struct_0_x1539_x1935_888560122}[VXLAN]{lang="EN-US"}[隧道（]{style="font-family:宋体"}[MTunnel]{lang="EN-US"}[），并将其与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651767978}[：表示手动关联]{lang="EN-US" style="font-family:宋体"}[VXLAN]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x427962976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel]{lang="EN-US"}**]{#struct_0_x1539_x1935_832301806}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_222425667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[negotiate-vni enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x820659478}

::: {#-900899430 .myid}
[]{#_Toc404798650}[]{#struct_0_x1539_x1935_x600859006}[]{#_Toc375835822}[]{#_Toc288911611}[]{#_Toc203551099}

**VXLAN \-- VXLAN基础配置命令 \-- encapsulation**

------------------------------------------------------------------------

[**[encapsulation]{lang="EN-US"}**]{#struct_0_x1539_x1935_2118191960}[命令用来配置以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1229356126}[命令用来删除以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1515180872}

[**[encapsulation]{lang="EN-US"}**[ **c-vid** { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x1539_x1935_29754634}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** { *vlan-id* \| *vlan-id-list* } \[ **only-tagged** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_35953032}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_x1539_x1935_705489628}

[**[encapsulation]{lang="EN-US"}**[ { **default** \| **tagged** \| **untagged** }]{lang="EN-US"}]{#struct_0_x1539_x1935_1135366377}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1537004537}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1951801995}

[[未配置任何报文匹配规则。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1038045323}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1730687903}

[[以太网服务实例视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1068283655}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600793470}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x189498134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1266130963}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_79975343}

[**[c-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x1539_x1935_x183821677}[：匹配内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Customer VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1671281158}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1539_x1935_x529350478}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ to *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x1539_x1935_99483919}[：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Service VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x2094880353}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1539_x1935_373248775}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[only-tagged]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1815236784}[：表示只匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。当匹配的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，如果未指定本关键字，则会同时匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文和未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文；如果指定了本参数，则只匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_x1539_x1935_1918442488}[：匹配指定外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签和内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_511056755}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1539_x1935_x600990078}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[al]{lang="EN-US"}**]{#struct_0_x1539_x1935_x991432253}**[l]{lang="EN-US"}**[表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_x1539_x1935_x686867214}[：表示缺省的报文匹配规则。]{style="font-family:宋体"}

[**[tagged]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1918786753}[：表示匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[untagged]{lang="EN-US"}**]{#struct_0_x1539_x1935_1124430308}[：表示匹配未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1451766620}

[[当同一个接口下配置的不同以太网服务实例的报文匹配规则出现重叠时，如何匹配报文与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1120954640}

[[同一个以太网接口下可以创建多个服务实例，但是最多只能有一个服务实例采用缺省的报文匹配规则（]{style="font-family:宋体"}**[encapsulation default]{lang="EN-US"}**]{#struct_0_x1539_x1935_x230203311}[）。如果接口下同时存在一个采用缺省报文匹配规则的服务实例和多个采用其他报文匹配规则的服务实例，则没有与任何其他报文匹配规则匹配的报文将匹配缺省报文匹配规则；如果接口下只存在一个采用缺省报文匹配规则的服务实例，则该接口上的所有报文都匹配缺省报文匹配规则。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_723605131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个以太网服务实例视图下，不能重复执行本命令。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1119258361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1119005249}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的关联。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[内层]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x600924542}[VLAN]{lang="EN-US"}[标签和外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的介绍请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[QinQ]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1364868050}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x515892599}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[上配置如下报文匹配规则：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[111]{lang="EN-US"}[，内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[20]{lang="EN-US"}[、]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1176114701}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\] encapsulation s-vid 111 c-vid 20 30 to 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_930983788}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1891065789}
:::

::: {#-2005881093 .myid}
[]{#_Toc404798651}[]{#struct_0_x1539_x1935_x1627800857}[]{#_Toc393878955}[]{#_Toc371411812}

**VXLAN \-- VXLAN基础配置命令 \-- flooding disable**

------------------------------------------------------------------------

[**[flooding disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1627800856}[命令用来关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能。]{style="font-family:宋体"}

[**[undo flooding disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1168722922}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_40957332}

[**[flooding disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1627800855}

[**[undo flooding disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1560160433}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1655788461}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800854}[的泛洪功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x5923508}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800852}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_800645546}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_328514275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_328514277}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_819365282}

[[缺省情况下，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_1448642752}[从本地站点内接收到目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知的单播数据帧后，会在该]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[内除接收接口外的所有本地接口和]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道上泛洪该数据帧，将该数据帧发送给]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[内的所有站点。如果用户希望把该类数据帧限制在本地站点内，不通过]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道将其转发到远端站点，则可以通过本命令手工禁止]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[对应]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514278}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_819365267}[关闭名称为]{style="font-family:宋体"}[vsi1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_328514279}

[\[Sysname\] vsi vsi1]{lang="EN-US"}

[\[Sysname-vsi-vsi1\] flooding disable]{lang="EN-US"}
:::

::: {#-1172193874 .myid}
[]{#_Toc404798652}[]{#struct_0_x1539_x1935_x1310059722}[]{#_Toc376875436}[]{#_Toc376875806}[]{#_Toc390073122}[]{#_Toc390073123}[]{#_Toc390073124}[]{#_Toc390073125}[]{#_Toc390073126}[]{#_Toc390073127}[]{#_Toc390073128}[]{#_Toc390073129}[]{#_Toc390073130}[]{#_Toc390073131}[]{#_Toc390073132}[]{#_Toc390073133}[]{#_Toc390073134}[]{#_Toc390073135}[]{#_Toc390073136}[]{#_Toc390073137}[]{#_Toc390073138}[]{#_Toc390073139}[]{#_Toc390073140}[]{#_Toc390073141}[]{#_Toc376957594}[]{#_Toc378672375}[]{#_Toc378672430}[]{#_Toc378683230}[]{#_Toc378683285}[]{#_Toc378683966}[]{#_Toc379547062}[]{#_Toc390073142}[]{#_Toc376957595}[]{#_Toc378672376}[]{#_Toc378672431}[]{#_Toc378683231}[]{#_Toc378683286}[]{#_Toc378683967}[]{#_Toc379547063}[]{#_Toc390073143}

**VXLAN \-- VXLAN基础配置命令 \-- group**

------------------------------------------------------------------------

[**[group]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1621505376}[命令用来配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[泛洪的组播地址和组播报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo group]{lang="EN-US"}**]{#struct_0_x1539_x1935_x765283481}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x332104086}

[**[group]{lang="EN-US"}**[ *group-address* **source** *source-address*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1933766756}

[**[undo group]{lang="EN-US"}**[ *group-address* **source** *source-address*]{lang="EN-US"}]{#struct_0_x1539_x1935_x601121150}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_204891508}

[[未指定]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_693622835}[泛洪的组播地址和组播报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[采用单播路由方式泛洪。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_354917425}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1355519805}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1351184332}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1769671977}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_2057160735}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1717757908}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1539_x1935_83258709}[：]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[泛洪的组播地址，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *source-address*]{lang="EN-US"}]{#struct_0_x1539_x1935_x601055614}[：指定]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[组播报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_194393989}

[[泛洪流量包括组播、广播和未知单播流量。]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1788435499}[流量泛洪可以采用如下两种方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单播路由方式（头端复制）：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1538146819}[VTEP]{lang="EN-US"}[接收到某个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的泛洪流量后，不仅通过本地接口在本地站点内泛洪，还会通过与该]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联的所有隧道、采用单播方式将其发送给]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[内的所有远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[组播路由方式（核心复制）：同一个]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1971306157}[VXLAN]{lang="EN-US"}[内的所有]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[都加入同一个组播组，利用组播路由协议在]{style="font-family:宋体"}[IP]{lang="EN-US"}[核心网上为该组播组建立组播转发表项。]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[接收到泛洪流量后，不仅在本地站点内泛洪，还会将本命令指定的组播地址作为目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}**[source]{lang="EN-US"}**[ *source-address*]{lang="EN-US"}[参数指定的地址作为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，对泛洪流量进行封装，封装后的报文根据已建立的组播转发表项转发到远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_2131161289}[采用单播路由方式泛洪流量。如果执行了本命令，则通过组播路由方式泛洪流量。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1300917338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于某些产品，为确保组播报文转发正常，]{style="font-family:宋体"}]{#struct_0_x1539_x1935_43196566}[VXLAN]{lang="EN-US"}[组播报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（]{style="font-family:宋体"}*[source-address]{lang="EN-US"}*[）应指定为一个已创建且处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道的源端地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以为不同的]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1328580450}[VXLAN]{lang="EN-US"}[指定相同的组播地址。例如，多个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[共用相同的]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[设备时，为这些]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[指定相同的组播地址，通过]{style="font-family:宋体"}[VXLAN ID]{lang="EN-US"}[来区分报文所属的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，可以减少]{style="font-family:宋体"}[IP]{lang="EN-US"}[核心网络中建立的组播转发表项数目。为不同]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[指定相同的组播地址时，要求为其指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址也必须相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1944735652}[VXLAN]{lang="EN-US"}[视图下重复执行本命令，则新的配置覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1411187211}

[]{#_Toc94588299}[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x920305449}[为]{style="font-family:宋体"}[VXLAN 100]{lang="EN-US"}[配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[泛洪的组播地址为]{style="font-family:宋体"}[233.1.1.1]{lang="EN-US"}[、]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[组播报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x600203646}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] vxlan 100]{lang="EN-US"}

[\[Sysname-vsi-aaa-vxlan-100\] group 233.1.1.1 source 2.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x554730464}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp]{lang="EN-US"}**[ **host** **enable**]{lang="EN-US"}]{#struct_0_x1539_x1935_996537005}
:::

::: {#2047546049 .myid}
[]{#_Toc404798653}[]{#struct_0_x1539_x1935_209482228}[]{#_Toc374372844}[]{#_Toc355963325}

**VXLAN \-- VXLAN基础配置命令 \-- igmp host enable**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **host** **enable**]{lang="EN-US"}]{#struct_0_x1539_x1935_x1999281674}[命令用来在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[协议的主机功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **host** **enable**]{lang="EN-US"}]{#struct_0_x1539_x1935_411374577}[命令用来关闭接口上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[协议的主机功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x770879911}

[**[igmp]{lang="EN-US"}**[ **host** **enable**]{lang="EN-US"}]{#struct_0_x1539_x1935_1275390352}

[**[undo]{lang="EN-US"}**[ **igmp** **host** **enable**]{lang="EN-US"}]{#struct_0_x1539_x1935_x887409369}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x551283533}

[[接口上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x1539_x1935_2053870612}[协议的主机功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600138110}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1723504053}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1555587275}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x545590227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_74780976}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_513895307}

[[采用组播路由方式泛洪流量时，必须在]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_87783334}[组播报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所在的接口上执行本命令，使得当前接口作为]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[主机，即从该接口收到]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询报文后，通过该接口发送组播组的报告报文，以便接收该组播组的报文。]{style="font-family:宋体"}

[[需要注意的是，只有通过]{style="font-family:宋体"}**[multicast routing]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1439786321}[命令使能]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由后，本命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1347337792}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1360867849}

[[\# ]{lang="FR"}]{#struct_0_x1539_x1935_x601994790}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="FR"}[组播路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上使能]{style="font-family:宋体"}[IGMP]{lang="FR"}[协议的主机功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x600727933}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp host enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x563523758}

[[\# ]{lang="FR"}]{#struct_0_x1539_x1935_1103265528}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="FR"}[组播路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="FR"}[上使能]{style="font-family:宋体"}[IGMP]{lang="FR"}[协议的主机功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x522753231}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[Vlan-interface10]{lang="FR"}[\] igmp host enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1073979576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **igmp** **host** **group**]{lang="EN-US"}]{#struct_0_x1539_x1935_x444986075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[group]{lang="EN-US"}**]{#struct_0_x1539_x1935_x77375988}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast]{lang="EN-US"}**[ **routing**]{lang="EN-US"}]{#struct_0_x1539_x1935_x8132298}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#2070950537 .myid}
[]{#_Toc404798654}[]{#struct_0_x1539_x1935_1815880731}[]{#_Toc375835823}

**VXLAN \-- VXLAN基础配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x600662397}[命令用来使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x167114634}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1157624620}

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1896852895}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1177866835}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2007887778}

[[L2VPN]{lang="EN-US"}]{#struct_0_x1539_x1935_1431139385}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_934167857}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_868288013}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x128413181}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x600859005}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_2118388568}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x431383337}

[[只有使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x1539_x1935_1723225808}[功能后，才能进行]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1543842224}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1524486627}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1591850457}

[\[Sysname\] l2vpn enable]{lang="EN-US"}
:::

::: {#-1775240408 .myid}
[]{#_Toc404798655}[]{#struct_0_x1539_x1935_x455623864}[]{#_Toc393878959}

**VXLAN \-- VXLAN基础配置命令 \-- mac-address static**

------------------------------------------------------------------------

[**[mac-address static]{lang="EN-US"}**]{#struct_0_x1539_x1935_97293564}[命令用来添加静态远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[undo mac-address static]{lang="EN-US"}**]{#struct_0_x1539_x1935_x455623865}[命令用来删除指定的静态远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_97228028}

[**[mac-address static]{lang="EN-US"}**[ *mac-address* **interface tunnel** *tunnel-number* **vsi** *vsi-name*]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623862}

[**[undo mac-address static]{lang="EN-US"}**[ \[ *mac-address* \] \[ **interface tunnel** *tunnel-number* \] **vsi** *vsi-name*]{lang="EN-US"}]{#struct_0_x1539_x1935_97686780}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x769482723}

[[设备上不存在任何静态的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623863}[地址表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_97621244}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_14358372}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x455623860}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_97555708}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x438168007}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x455623861}

[*[mac]{lang="EN-US"}*[-]{lang="EN-US"}]{#struct_0_x1539_x1935_97490172}*[address]{lang="EN-US"}*[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，不支持组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和全]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[interface tunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1500691268}[：指定远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道接口。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_1283758140}[：指定远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1500691267}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_1284085820}[地址是指]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[连接的远端站点内虚拟机的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址既可以通过本命令静态配置，也可以通过报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习、通过]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议学习。静态配置的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项优先级高于源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习和通过]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议学习的表项。源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习和通过]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议学习的表项优先级相同，后生成的表项可以覆盖已经存在的表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1614462587}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691270}[添加一条静态远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e201-0101]{lang="EN-US"}[，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道接口为]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[为]{style="font-family:宋体"}[vsi1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1284282429}

[\[Sysname\] mac-address static 000f-e201-0101 interface tunnel 1 vsi vsi1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1986629244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan tunnel mac-learning disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1500691269}
:::

::::: {#-1851718045 .myid}
[]{#_Toc371411813}[]{#_Toc375835837}[]{#_Toc404798656}[]{#struct_0_x1539_x1935_x837960892}[]{#_Toc393878960}[]{#_Toc383786769}[]{#_Toc383097751}[]{#_Toc376856932}[]{#_Toc371411817}[]{#_Toc397089258}[]{#_Toc397343495}[]{#_Toc397344539}[]{#_Toc397089259}[]{#_Toc397343496}[]{#_Toc397344540}[]{#_Toc397089260}[]{#_Toc397343497}[]{#_Toc397344541}[]{#_Toc397089261}[]{#_Toc397343498}[]{#_Toc397344542}[]{#_Toc397089262}[]{#_Toc397343499}[]{#_Toc397344543}[]{#_Toc397089263}[]{#_Toc397343500}[]{#_Toc397344544}[]{#_Toc397089264}[]{#_Toc397343501}[]{#_Toc397344545}[]{#_Toc397089265}[]{#_Toc397343502}[]{#_Toc397344546}[]{#_Toc397089266}[]{#_Toc397343503}[]{#_Toc397344547}[]{#_Toc397089267}[]{#_Toc397343504}[]{#_Toc397344548}[]{#_Toc397089268}[]{#_Toc397343505}[]{#_Toc397344549}[]{#_Toc397089269}[]{#_Toc397343506}[]{#_Toc397344550}[]{#_Toc397089270}[]{#_Toc397343507}[]{#_Toc397344551}[]{#_Toc397089271}[]{#_Toc397343508}[]{#_Toc397344552}[]{#_Toc397089272}[]{#_Toc397343509}[]{#_Toc397344553}[]{#_Toc397089273}[]{#_Toc397343510}[]{#_Toc397344554}[]{#_Toc397089274}[]{#_Toc397343511}[]{#_Toc397344555}[]{#_Toc397089275}[]{#_Toc397343512}[]{#_Toc397344556}[]{#_Toc397089276}[]{#_Toc397343513}[]{#_Toc397344557}[]{#_Toc397089277}[]{#_Toc397343514}[]{#_Toc397344558}[]{#_Toc397089278}[]{#_Toc397343515}[]{#_Toc397344559}[]{#_Toc397089279}[]{#_Toc397343516}[]{#_Toc397344560}[]{#_Toc397089280}[]{#_Toc397343517}[]{#_Toc397344561}[]{#_Toc397089281}[]{#_Toc397343518}[]{#_Toc397344562}[]{#_Toc376856865}[]{#_Toc376856929}[]{#_Toc376875440}[]{#_Toc376875810}[]{#_Toc376875441}[]{#_Toc376875811}[]{#_Toc376875442}[]{#_Toc376875812}[]{#_Toc376875443}[]{#_Toc376875813}[]{#_Toc376875444}[]{#_Toc376875814}[]{#_Toc376875445}[]{#_Toc376875815}[]{#_Toc376875446}[]{#_Toc376875816}[]{#_Toc376875447}[]{#_Toc376875817}[]{#_Toc376875448}[]{#_Toc376875818}[]{#_Toc376875449}[]{#_Toc376875819}[]{#_Toc376875450}[]{#_Toc376875820}[]{#_Toc376875451}[]{#_Toc376875821}[]{#_Toc376875452}[]{#_Toc376875822}[]{#_Toc376875453}[]{#_Toc376875823}[]{#_Toc376875454}[]{#_Toc376875824}[]{#_Toc376875455}[]{#_Toc376875825}[]{#_Toc376875456}[]{#_Toc376875826}[]{#_Toc376875457}[]{#_Toc376875827}[]{#_Toc376875458}[]{#_Toc376875828}[]{#_Toc376875459}[]{#_Toc376875829}[]{#_Toc376875460}[]{#_Toc376875830}[]{#_Toc376875461}[]{#_Toc376875831}[]{#_Toc376875462}[]{#_Toc376875832}[]{#_Toc376875463}[]{#_Toc376875833}[]{#_Toc376875464}[]{#_Toc376875834}[]{#_Toc376875465}[]{#_Toc376875835}[]{#_Toc376875466}[]{#_Toc376875836}[]{#_Toc376875467}[]{#_Toc376875837}[]{#_Toc376875468}[]{#_Toc376875838}[]{#_Toc376875469}[]{#_Toc376875839}[]{#_Toc376875470}[]{#_Toc376875840}[]{#_Toc376875471}[]{#_Toc376875841}[]{#_Toc376875472}[]{#_Toc376875842}[]{#_Toc376875473}[]{#_Toc376875843}[]{#_Toc376875474}[]{#_Toc376875844}[]{#_Toc376875475}[]{#_Toc376875845}[]{#_Toc376875476}[]{#_Toc376875846}[]{#_Toc376875477}[]{#_Toc376875847}[]{#_Toc376875478}[]{#_Toc376875848}[]{#_Toc376875479}[]{#_Toc376875849}[]{#_Toc390073147}[]{#_Toc390073148}[]{#_Toc390073149}[]{#_Toc390073150}[]{#_Toc390073151}[]{#_Toc390073152}[]{#_Toc390073153}[]{#_Toc390073154}[]{#_Toc390073155}[]{#_Toc390073156}[]{#_Toc390073157}[]{#_Toc390073158}[]{#_Toc390073159}[]{#_Toc390073160}[]{#_Toc390073161}[]{#_Toc390073162}[]{#_Toc390073163}[]{#_Toc390073164}[]{#_Toc390073165}[]{#_Toc390073166}[]{#_Toc390073167}[]{#_Toc390073168}[]{#_Toc390073169}[]{#_Toc390073170}[]{#_Toc390073171}[]{#_Toc390073172}[]{#_Toc390073173}[]{#_Toc390073174}[]{#_Toc390073175}

**VXLAN \-- VXLAN基础配置命令 \-- reset arp suppression vsi**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x217390335}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x536882625}
:::

[ ]{lang="EN-US"}

[**[reset arp suppression vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_x837960893}[命令用来清除]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x217455871}

[**[reset arp suppression vsi]{lang="EN-US"}**[ \[ **name** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960890}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x217521407}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1286054429}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960891}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x217586943}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1755595848}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960888}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_x218045696}[：清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_458108801}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960889}[清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> reset arp suppression vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_x218111232}

[This command will delete all entries. Continue? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp suppression]{lang="EN-US"}**]{#struct_0_x1539_x1935_x217652480}**[ vsi]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp suppression enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_264956337}
:::::

::::: {#816869194 .myid}
[]{#_Toc404798657}[]{#struct_0_x1539_x1935_2117257363}

**VXLAN \-- VXLAN基础配置命令 \-- reset l2vpn mac-address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image003.png){width="61" height="26"}]{lang="EN-US"}]{#struct_0_x1539_x1935_2129030391}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x810539176}
:::

**[ ]{lang="EN-US"}**

[**[reset l2vpn mac-address]{lang="EN-US"}**]{#struct_0_x1539_x1935_1222116030}[命令用来清除通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1867560310}

[**[reset ]{lang="EN-US"}[l2vpn mac-address ]{lang="EN-US"}**[\[ **vsi**]{lang="EN-US"}*[ vsi-name ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_x1539_x1935_x264237422}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1689800925}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1338608021}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1176622333}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x2043248467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x600924541}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1364802514}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_188218606}[：清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x339713909}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x72198319}[通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习到错误的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，或学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项数目达到最大值时，可以执行本命令，以便重新学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_885415828}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1195434905}[清除名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[\<Sysname\> reset l2vpn mac-address vsi vpn1]{lang="EN-US"}]{#struct_0_x1539_x1935_x1416680811}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1319812698}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn mac-address vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_2138470880}
:::::

::::: {#1068872014 .myid}
[]{#_Toc383786770}[]{#_Toc404798658}[]{#struct_0_x1539_x1935_x1647264954}[]{#_Toc393878962}[]{#_Toc387305729}[]{#_Toc381105349}

**VXLAN \-- VXLAN基础配置命令 \-- reset l2vpn statistics vsi**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x1140750513}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x1647264955}
:::

[ ]{lang="EN-US"}

[**[reset l2vpn statistics vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_425333428}[命令用来清除]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1601684085}

[**[reset l2vpn statistics vsi ]{lang="EN-US"}**[\[ **name** *vsi-name* \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x1647264952}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1991417369}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1647264953}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x737465986}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1647264950}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_828617955}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x449879840}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_x1647264951}[：清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1900265400}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1647264948}[清除本设备上所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset l2vpn statistics vsi]{lang="EN-US"}]{#struct_0_x1539_x1935_1184782779}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x418935326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[statistics enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x874237743}
:::::

::: {#-26059450 .myid}
[]{#_Toc404798659}[]{#struct_0_x1539_x1935_x1647264949}[]{#_Toc393878963}[]{#_Toc371411814}

**VXLAN \-- VXLAN基础配置命令 \-- selective-flooding mac-address**

------------------------------------------------------------------------

[**[selective-flooding mac-addres]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1544100576}[命令用来配置]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo selective-flooding mac-addres]{lang="EN-US"}**]{#struct_0_x1539_x1935_x103109165}[命令用来删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的选择性泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1043335756}

[]{#_Toc178914659}[**[selective-flooding mac-addres]{lang="EN-US"}**[ *mac-addres*]{lang="EN-US"}]{#struct_0_x1539_x1935_309050180}

[**[undo selective-flooding mac-addres]{lang="EN-US"}**[ *mac-addres*]{lang="EN-US"}]{#struct_0_x1539_x1935_x948642827}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_309050179}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1772346350}[选择性泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_309050182}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x948642825}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_309050181}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x948642826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_936585304}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_309050184}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x1539_x1935_x948642831}[：选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[F]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_937044055}

[[通过]{style="font-family:宋体"}**[flooding disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_309050183}[命令关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的泛洪功能后，为了将某些]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数据帧泛洪到远端站点以保证某些业务的流量在站点间互通，可以配置选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。当数据帧的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址匹配选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时，该数据帧可以泛洪到远端站点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x948642824}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_936716376}[在]{style="font-family:宋体"}[VSI vsi1]{lang="EN-US"}[下配置选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e201-0101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_309050186}

[\[Sysname\] vsi vsi1]{lang="EN-US"}

[\[Sysname-vsi-vsi1\] selective-flooding mac-address 000f-e201-0101]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x948642829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[flooding disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_309050185}
:::

::: {#-1902885513 .myid}
[]{#_Toc404798660}[]{#struct_0_x1539_x1935_x1108473578}[]{#_Toc375835842}

**VXLAN \-- VXLAN基础配置命令 \-- service-instance**

------------------------------------------------------------------------

[**[service-instance]{lang="EN-US"}**]{#struct_0_x1539_x1935_x601121149}[命令用来创建以太网服务实例，并进入以太网服务实例视图。]{style="font-family:宋体"}

[**[undo service-instance]{lang="EN-US"}**]{#struct_0_x1539_x1935_205350261}[命令用来删除指定的以太网服务实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_462040956}

[**[service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x895010599}

[**[undo service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x734255816}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1928422678}

[[接口上不存在任何以太网服务实例。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x2034011766}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x610135631}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1539_x1935_x1217646613}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_226111405}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1573460305}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x601055613}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_194066309}

[*[instance-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_740478720}[：以太网服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1101437072}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1823880124}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上创建以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1316817559}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1554286405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x1539_x1935_x780365566}
:::

::: {#1170655049 .myid}
[]{#_Toc404798661}[]{#struct_0_x1539_x1935_x610366551}[]{#_Toc375835843}

**VXLAN \-- VXLAN基础配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1539_x1935_x600203645}[命令用来关闭当前的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1539_x1935_x554927072}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1683701075}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1539_x1935_187574309}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1539_x1935_154970426}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1366331134}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1249170457}[处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1611171176}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_352555119}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_390111316}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x247355724}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1536144158}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_805454482}

[[关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x600138109}[后，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[将不能提供二层交换服务。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1723045302}[功能通常用于暂时禁用二层交换服务，但还需要再次启用该服务的场景。关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[所有已存在的配置保持不变。在关闭状态下还可以对]{style="font-family:宋体"}[VSI]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[再次被开启后，基于最新的配置提供二层交换服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1554765326}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1443814822}[关闭名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_94335076}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1902487666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_x760184523}
:::

::::: {#-655052582 .myid}
[]{#_Toc383786771}[]{#_Toc404798662}[]{#struct_0_x1539_x1935_1885190988}[]{#_Toc393878966}[]{#_Toc387305730}[]{#_Toc381105350}[]{#_Toc376783185}

**VXLAN \-- VXLAN基础配置命令 \-- statistics enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x21072053}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_1885190987}
:::

[ ]{lang="EN-US"}

[**[statistics enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x20613301}[命令用来开启指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[报文统计功能。]{style="font-family:宋体"}

[**[undo statistics enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x453461180}[命令用来关闭指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[报文统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_191921654}

[**[statistics enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1290071713}

[**[undo statistics enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x453461181}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_191856118}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_2054197231}[的报文统计功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x453461178}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_191397363}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1416714708}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x453461179}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_191331827}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2070850079}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x453461176}[开启名为]{style="font-family:宋体"}[vpls1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的报文统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_192314867}

[\[Sysname\] vsi vpls1]{lang="EN-US"}

[\[Sysname-vsi-vpls1\] statistics enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x453461177}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset l2vpn statistics vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_192249331}
:::::

::: {#816204697 .myid}
[]{#_Toc404798663}[]{#struct_0_x1539_x1935_1886647086}[]{#_Toc372102899}[]{#_Toc371058550}[]{#_Toc376957599}[]{#_Toc378672384}[]{#_Toc378672439}[]{#_Toc378683239}[]{#_Toc378683294}[]{#_Toc378683975}[]{#_Toc379547071}[]{#_Toc390073180}[]{#_Toc376957600}[]{#_Toc378672385}[]{#_Toc378672440}[]{#_Toc378683240}[]{#_Toc378683295}[]{#_Toc378683976}[]{#_Toc379547072}[]{#_Toc390073181}[]{#_Toc376957601}[]{#_Toc378672386}[]{#_Toc378672441}[]{#_Toc378683241}[]{#_Toc378683296}[]{#_Toc378683977}[]{#_Toc379547073}[]{#_Toc390073182}[]{#_Toc376957602}[]{#_Toc378672387}[]{#_Toc378672442}[]{#_Toc378683242}[]{#_Toc378683297}[]{#_Toc378683978}[]{#_Toc379547074}[]{#_Toc390073183}[]{#_Toc376957603}[]{#_Toc378672388}[]{#_Toc378672443}[]{#_Toc378683243}[]{#_Toc378683298}[]{#_Toc378683979}[]{#_Toc379547075}[]{#_Toc390073184}[]{#_Toc376957604}[]{#_Toc378672389}[]{#_Toc378672444}[]{#_Toc378683244}[]{#_Toc378683299}[]{#_Toc378683980}[]{#_Toc379547076}[]{#_Toc390073185}[]{#_Toc376957605}[]{#_Toc378672390}[]{#_Toc378672445}[]{#_Toc378683245}[]{#_Toc378683300}[]{#_Toc378683981}[]{#_Toc379547077}[]{#_Toc390073186}[]{#_Toc376957606}[]{#_Toc378672391}[]{#_Toc378672446}[]{#_Toc378683246}[]{#_Toc378683301}[]{#_Toc378683982}[]{#_Toc379547078}[]{#_Toc390073187}[]{#_Toc376957607}[]{#_Toc378672392}[]{#_Toc378672447}[]{#_Toc378683247}[]{#_Toc378683302}[]{#_Toc378683983}[]{#_Toc379547079}[]{#_Toc390073188}[]{#_Toc376957608}[]{#_Toc378672393}[]{#_Toc378672448}[]{#_Toc378683248}[]{#_Toc378683303}[]{#_Toc378683984}[]{#_Toc379547080}[]{#_Toc390073189}[]{#_Toc376957609}[]{#_Toc378672394}[]{#_Toc378672449}[]{#_Toc378683249}[]{#_Toc378683304}[]{#_Toc378683985}[]{#_Toc379547081}[]{#_Toc390073190}[]{#_Toc376957610}[]{#_Toc378672395}[]{#_Toc378672450}[]{#_Toc378683250}[]{#_Toc378683305}[]{#_Toc378683986}[]{#_Toc379547082}[]{#_Toc390073191}[]{#_Toc376957611}[]{#_Toc378672396}[]{#_Toc378672451}[]{#_Toc378683251}[]{#_Toc378683306}[]{#_Toc378683987}[]{#_Toc379547083}[]{#_Toc390073192}[]{#_Toc376957612}[]{#_Toc378672397}[]{#_Toc378672452}[]{#_Toc378683252}[]{#_Toc378683307}[]{#_Toc378683988}[]{#_Toc379547084}[]{#_Toc390073193}[]{#_Toc376957613}[]{#_Toc378672398}[]{#_Toc378672453}[]{#_Toc378683253}[]{#_Toc378683308}[]{#_Toc378683989}[]{#_Toc379547085}[]{#_Toc390073194}[]{#_Toc376957614}[]{#_Toc378672399}[]{#_Toc378672454}[]{#_Toc378683254}[]{#_Toc378683309}[]{#_Toc378683990}[]{#_Toc379547086}[]{#_Toc390073195}[]{#_Toc376957615}[]{#_Toc378672400}[]{#_Toc378672455}[]{#_Toc378683255}[]{#_Toc378683310}[]{#_Toc378683991}[]{#_Toc379547087}[]{#_Toc390073196}[]{#_Toc376957616}[]{#_Toc378672401}[]{#_Toc378672456}[]{#_Toc378683256}[]{#_Toc378683311}[]{#_Toc378683992}[]{#_Toc379547088}[]{#_Toc390073197}[]{#_Toc376957617}[]{#_Toc378672402}[]{#_Toc378672457}[]{#_Toc378683257}[]{#_Toc378683312}[]{#_Toc378683993}[]{#_Toc379547089}[]{#_Toc390073198}[]{#_Toc376957618}[]{#_Toc378672403}[]{#_Toc378672458}[]{#_Toc378683258}[]{#_Toc378683313}[]{#_Toc378683994}[]{#_Toc379547090}[]{#_Toc390073199}[]{#_Toc376957619}[]{#_Toc378672404}[]{#_Toc378672459}[]{#_Toc378683259}[]{#_Toc378683314}[]{#_Toc378683995}[]{#_Toc379547091}[]{#_Toc390073200}[]{#_Toc376957620}[]{#_Toc378672405}[]{#_Toc378672460}[]{#_Toc378683260}[]{#_Toc378683315}[]{#_Toc378683996}[]{#_Toc379547092}[]{#_Toc390073201}[]{#_Toc376957621}[]{#_Toc378672406}[]{#_Toc378672461}[]{#_Toc378683261}[]{#_Toc378683316}[]{#_Toc378683997}[]{#_Toc379547093}[]{#_Toc390073202}[]{#_Toc376957622}[]{#_Toc378672407}[]{#_Toc378672462}[]{#_Toc378683262}[]{#_Toc378683317}[]{#_Toc378683998}[]{#_Toc379547094}[]{#_Toc390073203}[]{#_Toc376957623}[]{#_Toc378672408}[]{#_Toc378672463}[]{#_Toc378683263}[]{#_Toc378683318}[]{#_Toc378683999}[]{#_Toc379547095}[]{#_Toc390073204}

**VXLAN \-- VXLAN基础配置命令 \-- tunnel**

------------------------------------------------------------------------

[**[tunnel]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1397631735}[命令用来配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[与指定的隧道关联。]{style="font-family:宋体"}

[**[undo tunnel]{lang="EN-US"}**]{#struct_0_x1539_x1935_513163922}[命令用来取消]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[与指定隧道的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x940886760}

[**[tunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1191073326}

[**[undo tunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_x600727936}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x563720366}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_742793576}[没有与任何]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1681374576}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1597655553}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_900576824}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1496573549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1250887115}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1140482558}

[*[tunnel-numb]{lang="FR"}*[er]{lang="EN-US"}]{#struct_0_x1539_x1935_x925476329}[：隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1952520228}

[[在]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1134503020}[组网中，用户可以手工将]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道关联。]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[接收到某个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的泛洪流量后，如果采用单播路由泛洪方式，则]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[将在与该]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[关联的所有]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道上发送该流量，以便将流量转发给所有的远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[执行本命令时，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x764114671}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令指定的隧道必须是]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x600662400}[VXLAN]{lang="EN-US"}[模式的隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1406797933}[VXLAN]{lang="EN-US"}[可以关联多条]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道；一条]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道可以关联多个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_359301469}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x2018041185}[配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道]{style="font-family:宋体"}[Tunne0]{lang="EN-US"}[和]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[与]{style="font-family:宋体"}[VXLAN 10000]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_x1046078253}

[\[Sysname\] vsi vpna]{lang="EN-US"}

[\[Sysname-vsi-vpna\] vxlan 10000]{lang="EN-US"}

[\[Sysname-vsi-vpna-vxlan-10000\] tunnel 0]{lang="EN-US"}

[\[Sysname-vsi-vpna-vxlan-10000\] tunnel 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1087816875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan]{lang="EN-US"}[ tunnel]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1775472728}
:::

::: {#-126256708 .myid}
[]{#_Toc404798664}[]{#struct_0_x1539_x1935_1502853958}[]{#_Toc393878968}[]{#_Toc383786773}[]{#_Toc382551470}

**VXLAN \-- VXLAN基础配置命令 \-- tunnel bfd enable**

------------------------------------------------------------------------

[**[tunnel bfd enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1502853957}[命令用来开启隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[**[undo tunnel bfd enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1605086795}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_293145880}

[**[tunnel bfd enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_365080054}

[**[undo tunnel bfd enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1502853960}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1604759116}

[[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1539_x1935_697449722}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502853959}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1604169291}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2017379020}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x872686233}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853962}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1604890188}

[[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853961}[检测功能用来避免]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[设备无法及时感知隧道的故障，导致报文转发失败。]{style="font-family:宋体"}

[[开启隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1539_x1935_1604693580}[检测功能后，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[将自动建立多跳控制报文方式的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，检测隧道源和目的端之间链路的可达性。]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到链路不可达后，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[将]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的状态置为]{style="font-family:宋体"}[down]{lang="EN-US"}[，不再通过该隧道转发报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502853964}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1605021260}[开启]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道]{style="font-family:宋体"}[Tunnel9]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853963}

[\[Sysname\] interface tunnel 9 mode vxlan]{lang="EN-US"}

[\[Sysname-Tunnel9\] tunnel bfd enable]{lang="EN-US"}
:::

::: {#-981054953 .myid}
[]{#_Toc404798665}[]{#struct_0_x1539_x1935_x1869174802}[]{#_Toc375835849}

**VXLAN \-- VXLAN基础配置命令 \-- vsi**

------------------------------------------------------------------------

[**[vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_1675680074}[命令用来创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Switching Instance]{lang="EN-US"}[，虚拟交换实例），并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **vsi**]{lang="EN-US"}]{#struct_0_x1539_x1935_779039935}[命令用来删除指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1557931349}

[**[vsi]{lang="IT"}**]{#struct_0_x1539_x1935_129478482}[ *vsi-name*]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_x1539_x1935_x600859008}[ ]{lang="IT"}**[vsi]{lang="IT"}**[ *vsi-name*]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2117536600}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x2145132035}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x898493521}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1379350442}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1328213265}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1054117416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x430377802}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x933198751}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_232818405}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600793472}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x189629206}[是]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[上为一个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[提供二层交换服务的虚拟交换实例。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[可以看做是]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[上的一台基于]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[进行二层转发的虚拟交换机，它具有传统以太网交换机的所有功能，包括源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址老化、泛洪等。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[一一对应。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1846340369}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1586767293}[创建名为]{style="font-family:宋体"}[vxlan10]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1648299319}

[\[Sysname\] vsi vxlan10]{lang="EN-US"}

[\[Sysname-vsi-vxlan10\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502008208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_x33830719}
:::

::: {#1253663136 .myid}
[]{#_Toc404798666}[]{#struct_0_x1539_x1935_x31095702}[]{#_Toc378672411}[]{#_Toc378672466}[]{#_Toc378683266}[]{#_Toc378683321}[]{#_Toc378684002}[]{#_Toc379547098}[]{#_Toc390073207}

**VXLAN \-- VXLAN基础配置命令 \-- vxlan**

------------------------------------------------------------------------

[**[vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1156757605}[命令用来创建]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_1235788229}[命令用来删除指定的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1920222828}

[**[vxlan ]{lang="EN-US"}***[vxlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x600990080}

[**[undo vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_x990907954}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1453090014}

[[设备上不存在任何]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x324477480}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1683983557}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1694301774}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x999121626}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1618169595}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1763644167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x999873041}

[*[vxlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1891879124}[：]{style="font-family:宋体"}[VXLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600924544}

[[在一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1364999122}[下只能创建一个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[。不同]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下创建的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，其]{style="font-family:宋体"}[VXLAN ID]{lang="EN-US"}[不能相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_660922097}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_403637799}[在名称为]{style="font-family:宋体"}[vpna]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下创建编号为]{style="font-family:宋体"}[10000]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_x1816813009}

[\[Sysname\] vsi vpna]{lang="EN-US"}

[\[Sysname-vsi-vpna\] vxlan 10000]{lang="EN-US"}

[\[Sysname-vsi-vpna-vxlan-10000\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1616629371}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_1486239002}
:::

::: {#1343021387 .myid}
[]{#_Toc404798667}[]{#struct_0_x1539_x1935_597837687}[]{#_Toc372033211}

**VXLAN \-- VXLAN基础配置命令 \-- vxlan invalid-udp-checksum discard**

------------------------------------------------------------------------

[**[vxlan invalid-udp-checksum discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1976901681}[命令用来配置丢弃]{style="font-family:宋体"}[UDP]{lang="EN-US"}[校验和检查失败的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo vxlan invalid-udp-checksum discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_x976542182}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x601121152}

[**[vxlan invalid-udp-checksum discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_204760436}

[**[undo vxlan invalid-udp-checksum discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_x277519059}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1731467022}

[[不会检查]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x8727655}[报文的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[校验和。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_962363798}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1792203938}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x139330788}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x271719878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_230746414}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x601055616}

[[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_194262917}[对二层数据帧进行封装时，将]{style="font-family:宋体"}[UDP]{lang="EN-US"}[校验和设置为]{style="font-family:宋体"}[0]{lang="EN-US"}[。缺省情况下，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[接收到]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文后，不会检查报文的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[校验和。如果在]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[上执行了本命令，则该]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[会对接收的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[校验和进行检查，校验和检查失败的报文将被丢弃。]{style="font-family:宋体"}

[[为了兼容其他厂商的设备，]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x1539_x1935_579624192}[检验和为]{style="font-family:宋体"}[0]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[检验和正确的报文均能通过]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[的检查，被]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[接收。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1546703693}

[[\# ]{lang="PT-BR"}]{#struct_0_x1539_x1935_1911017184}[配置丢弃]{style="font-family:宋体"}[UDP]{lang="EN-US"}[校验和检查失败的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x2074248776}

[\[Sysname\] vxlan invalid-udp-checksum discard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1505747883}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan invalid-vlan-tag discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_1036529660}
:::

::: {#-382258864 .myid}
[]{#_Toc404798668}[]{#struct_0_x1539_x1935_49562799}[]{#_Toc373172910}[]{#_Toc376856875}[]{#_Toc376856939}

**VXLAN \-- VXLAN基础配置命令 \-- vxlan invalid-vlan-tag discard**

------------------------------------------------------------------------

[**[vxlan invalid-vlan-tag discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_x959953680}[命令用来配置丢弃内层数据帧含有]{style="font-family:
宋体"}[VLAN tag]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo vxlan invalid-vlan-tag discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1613589211}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600203648}

[**[vxlan invalid-vlan-tag discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_x554075104}

[**[undo vxlan invalid-vlan-tag discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_1820175005}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_66246128}

[[不会检查]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1074131858}[报文内层封装的以太网数据帧是否携带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1924213037}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x90924726}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1899187851}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1679150382}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x281070369}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600138112}

[[如果在]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_1723635125}[上执行了本命令，则]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[接收到]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文并对其解封装后，若内层以太网数据帧带有]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[，则丢弃该]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_1935136202}[上通过]{style="font-family:宋体"}**[xconnect vsi]{lang="EN-US"}**[命令的]{style="font-family:宋体"}**[access-mode]{lang="EN-US"}**[参数配置接入模式为]{style="font-family:宋体"}**[ethernet]{lang="EN-US"}**[时，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文可能携带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。这种情况下建议不要在本端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[上执行]{style="font-family:宋体"}**[vxlan ]{lang="EN-US"}[invalid-vlan-tag discard]{lang="EN-US"}**[命令，以免错误地丢弃报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1307192262}

[[\# ]{lang="PT-BR"}]{#struct_0_x1539_x1935_x877446505}[配置丢弃内层数据帧含有]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1922449887}

[\[Sysname\] vxlan invalid-vlan-tag discard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1147867017}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan invalid-udp-checksum discard]{lang="EN-US"}**]{#struct_0_x1539_x1935_x495911994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[xconnect vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_2043130360}
:::

::: {#115618911 .myid}
[]{#_Toc404798669}[]{#struct_0_x1539_x1935_311212870}[]{#_Toc393878973}[]{#_Toc376856936}[]{#_Toc371411815}

**VXLAN \-- VXLAN基础配置命令 \-- vxlan local-mac report**

------------------------------------------------------------------------

[**[vxlan local-mac report]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1164730020}[命令用来开启]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除的日志功能。]{style="font-family:宋体"}

[**[undo vxlan local-mac report]{lang="EN-US"}**]{#struct_0_x1539_x1935_2136943256}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_311212869}

[**[vxlan local-mac report]{lang="EN-US"}**]{#struct_0_x1539_x1935_791585109}

[**[undo vxlan local-mac report]{lang="EN-US"}**]{#struct_0_x1539_x1935_x372803581}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_311212872}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1164730018}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时不会记录日志。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1801728144}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_311212871}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1164730019}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_311212874}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1164730016}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_311212873}

[[执行本配置后，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1164730017}[添加、删除本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时，将产生日志信息。生成的日志信息将被发送到设备的信息中心，通过设置信息中心的参数，决定日志信息的输出规则（即是否允许输出以及输出方向）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_311212876}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1878702917}[开启]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除的日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1878702920}

[\[Sysname\] vxlan local-mac report]{lang="EN-US"}
:::

::: {#484471969 .myid}
[]{#_Toc404798670}[]{#struct_0_x1539_x1935_x1750721058}[]{#_Toc393878974}

**VXLAN \-- VXLAN基础配置命令 \-- vxlan tunnel mac-learning disable**

------------------------------------------------------------------------

[**[vxlan tunnel mac-learning disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_328970789}[命令用来关闭远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址自动学习功能。]{style="font-family:宋体"}

[**[undo vxlan tunnel mac-learning disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1878702919}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1750262307}

[**[vxlan tunnel mac-learning disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1878702922}

[**[undo vxlan tunnel mac-learning disable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1750852130}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1878702921}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1750786594}[地址自动学习功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1878702924}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1750458914}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1878702923}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1750917666}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x459949244}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_112403239}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x459949245}[地址是指]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[连接的远端站点内虚拟机的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址可以通过报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动态学习。]{style="font-family:宋体"}

[[缺省情况下，设备可以自动学习远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x459949242}[地址。如果网络中存在攻击，为了避免学习到错误的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，可以通过本命令手工关闭远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址自动学习功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_112010023}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x459949243}[关闭远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址自动学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_111944487}

[\[Sysname\] vxlan tunnel mac-learning disable]{lang="EN-US"}
:::

::: {#1885768484 .myid}
[]{#_Toc404798671}[]{#struct_0_x1539_x1935_1509308142}[]{#_Toc372033212}[]{#_Toc376875486}[]{#_Toc376875856}[]{#_Toc376875487}[]{#_Toc376875857}[]{#_Toc376875488}[]{#_Toc376875858}[]{#_Toc376875489}[]{#_Toc376875859}[]{#_Toc376875490}[]{#_Toc376875860}[]{#_Toc376875491}[]{#_Toc376875861}[]{#_Toc376875492}[]{#_Toc376875862}[]{#_Toc376875493}[]{#_Toc376875863}[]{#_Toc376875494}[]{#_Toc376875864}[]{#_Toc376875495}[]{#_Toc376875865}[]{#_Toc376875496}[]{#_Toc376875866}[]{#_Toc376875497}[]{#_Toc376875867}[]{#_Toc376875498}[]{#_Toc376875868}[]{#_Toc376875499}[]{#_Toc376875869}[]{#_Toc376875500}[]{#_Toc376875870}[]{#_Toc376875501}[]{#_Toc376875871}[]{#_Toc376875502}[]{#_Toc376875872}[]{#_Toc376875503}[]{#_Toc376875873}[]{#_Toc376875504}[]{#_Toc376875874}[]{#_Toc390073211}[]{#_Toc390073212}[]{#_Toc390073213}[]{#_Toc390073214}[]{#_Toc390073215}[]{#_Toc390073216}[]{#_Toc390073217}[]{#_Toc390073218}[]{#_Toc390073219}[]{#_Toc390073220}[]{#_Toc390073221}[]{#_Toc390073222}[]{#_Toc390073223}[]{#_Toc390073224}[]{#_Toc390073225}[]{#_Toc390073226}[]{#_Toc390073227}[]{#_Toc390073228}[]{#_Toc390073229}[]{#_Toc390073230}

**VXLAN \-- VXLAN基础配置命令 \-- vxlan udp-port**

------------------------------------------------------------------------

[**[vxlan udp-port]{lang="EN-US"}**]{#struct_0_x1539_x1935_x600727935}[命令用来配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo vxlan udp-port]{lang="EN-US"}**]{#struct_0_x1539_x1935_x563654830}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x37358608}

[**[vxlan udp-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_x216220150}

[**[undo vxlan udp-port]{lang="EN-US"}**]{#struct_0_x1539_x1935_x532885002}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x534537201}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_535332002}[报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[4789]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_885658674}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1510376111}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x523702660}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1273883314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x600662399}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x167769994}

[*[port-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1544417587}[：]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1267465298}

[[属于同一个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_425564758}[的]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[设备上需要配置相同的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[建议不要将]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x2137399153}[报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号配置为知名端口，即]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[之间的端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1619098250}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1057904127}[配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[6666]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1625345099}

[\[Sysname\] vxlan udp-port 6666]{lang="EN-US"}
:::

::: {#-216238939 .myid}
[]{#_Toc404798672}[]{#struct_0_x1539_x1935_x600859007}[]{#_Toc375835850}

**VXLAN \-- VXLAN基础配置命令 \-- xconnect vsi**

------------------------------------------------------------------------

[**[xconnect vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_2118257496}[命令用来将]{style="font-family:宋体"}[AC]{lang="NL-BE"}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **xconnect vsi**]{lang="EN-US"}]{#struct_0_x1539_x1935_x395743994}[命令用来取消]{style="font-family:宋体"}[AC]{lang="EN-US"}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_823445632}

[**[xconnect vsi ]{lang="EN-US"}***[vsi-name ]{lang="EN-US"}*[\[ **access-mode** { **ethernet** \| **vlan** } \]]{lang="EN-US"}]{#struct_0_x1539_x1935_1652901128}

[**[undo xconnect vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_x356274352}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1038163830}

[[AC]{lang="EN-US"}]{#struct_0_x1539_x1935_1827899798}[没有]{style="font-family:宋体"}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_877612114}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1539_x1935_x320808425}[以太网服务实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1588418890}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x839392277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_430820207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x600793471}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_x1539_x1935_x189432598}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[access-mode]{lang="EN-US"}**]{#struct_0_x1539_x1935_x284271685}[：指定]{style="font-family:宋体"}[接入]{style="font-family:宋体"}[模式。当关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[为三层以太网子接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、以太网服务实例时，接入模式缺省为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[；其他情况下，接入模式缺省为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ethernet]{lang="EN-US"}**]{#struct_0_x1539_x1935_1211807963}[：指定]{style="font-family:宋体"}[接入模式]{style="font-family:宋体"}[为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_260733118}[：指定]{style="font-family:宋体"}[接入模式]{style="font-family:宋体"}[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1007258472}

[[在接口视图下执行本命令后，从接口接收到的报文将通过查找关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_622905605}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表进行转发；在某个接口的以太网服务实例视图下执行本命令后，从该接口接收到的、符合以太网服务实例报文匹配规则的报文，将通过查找关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表进行转发。]{style="font-family:宋体"}

[[接入模式分为以下两种：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_42478882}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_43833414}[接入模式：从本地站点接收到的、发送给本地站点的以太网帧必须带有]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[从本地站点接收到以太网帧后，删除该帧的所有]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[，再转发该数据帧；]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[发送以太网帧到本地站点时，为其添加]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。采用该模式时，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[不会传递]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[信息，不同站点可以独立地规划自己的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，不同站点的不同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[之间可以互通。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_x1539_x1935_1846270894}[接入模式：]{lang="EN-US" style="font-family:宋体"}[从本地站点接收到的、发送给本地站点的以太网帧可以携带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[，也可以不携带]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[从本地站点接收到以太网帧后，保持该帧的]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[信息不变，转发该数据帧；]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[发送以太网帧到本地站点时，不会为其添加]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[。采用该模式时，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[会在不同站点间传递]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[信息，不同站点的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[需要统一规划，否则无法互通。]{style="font-family:宋体"}

[[需要注意的是，在以太网服务实例下配置该命令前，必须先配置]{style="font-family:宋体"}**[encapsulation]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1345436657}[命令]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1636488311}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_x1539_x1935_270406129}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1682541578}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下关联名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1295677812}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] xconnect vsi vpn1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_x1539_x1935_222552769}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1545803393}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下采用以太网服务实例]{style="font-family:宋体"}[200]{lang="EN-US"}[来匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的报文，将该以太网服务实例与名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x600990079}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] encapsulation s-vid 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] xconnect vsi vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x991366717}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1474621701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x1539_x1935_582980932}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[encapsulation]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1309918487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_x1539_x1935_1089971405}
:::

::::: {#-793080710 .myid}
[]{#_Toc404798674}[]{#struct_0_x1539_x1935_1496365899}[]{#_Toc393878978}[]{#_Toc383786751}[]{#_Toc383097743}[]{#_Toc378325573}

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery client member**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 5 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_1901704858}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x842286268}
:::

[ ]{lang="EN-US"}

[**[display vxlan neighbor-discovery client member]{lang="EN-US"}**]{#struct_0_x1539_x1935_858805508}[命令用来在]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[学到的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x842286269}

[**[display vxlan neighbor-discovery client member]{lang="EN-US"}**[ \[ **interface** **tunnel** *interface-number* \| **local** *local-ip* ]{lang="EN-US"}]{#struct_0_x1539_x1935_858739972}[｜]{style="font-family:宋体"} **[remote]{lang="EN-US"}**[ *client-ip* \| **server** *server-ip* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x842286266}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_859460868}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x918958797}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286267}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_859395332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286264}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_859591940}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1811306985}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_x842286265}[：显示通过指定]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口学到的邻居信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[local ]{lang="EN-US"}***[local-ip]{lang="EN-US"}*]{#struct_0_x1539_x1935_x842286262}[：显示通过源端地址为指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口学到的邻居信息。]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*[表示]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口的源端地址，即本地]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[remote ]{lang="EN-US"}***[client-ip]{lang="EN-US"}*]{#struct_0_x1539_x1935_x842286263}[：显示设备学到的指定邻居]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[client-ip]{lang="EN-US"}*[表示邻居]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[server ]{lang="EN-US"}***[server-ip]{lang="EN-US"}*]{#struct_0_x1539_x1935_859133188}[：显示通过指定]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的邻居信息。]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x842286260}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_859329796}[学到的邻居信息，包括邻居的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址、桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、创建时间、老化时间、邻居之间的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道状态等信息。]{style="font-family:宋体"}

[[如果不指定任何参数，将显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286261}[学到的所有邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1651590332}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1649427642}[显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[学到的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan neighbor-discovery client member]{lang="EN-US"}]{#struct_0_x1539_x1935_x1649427641}

[Interface: Tunnel0    Network ID: 1]{lang="EN-US"}

[Local Address: 20.0.0.2]{lang="EN-US"}

[Server Address: 20.0.1.1]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    13        Up]{lang="EN-US"}

[20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    12        Up]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel0    Network ID: 1]{lang="EN-US"}

[Local Address: 20.0.0.2]{lang="EN-US"}

[Server Address: 20.0.1.2]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up]{lang="EN-US"}

[20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Up]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel1    Network ID: 2]{lang="EN-US"}

[Local Address: 21.0.0.1]{lang="EN-US"}

[Server Address: 21.0.1.2]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[21.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up]{lang="EN-US"}

[21.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel2    Network ID: 3]{lang="EN-US"}

[Local Address: 21.0.0.2]{lang="EN-US"}

[Server Address: NA]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[21.0.2.1        NA                2011/01/01 12:12:12    25        Up]{lang="EN-US"}

[21.0.3.1        NA                2011/01/01 12:12:12    19        Up]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display vxlan neighbor-discovery client member]{lang="EN-US"}]{#struct_0_x1539_x1935_x1649427638}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1469309501}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1649427639}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1649427636}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_306887492}

[[启动]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_306887491}[功能的接口名称]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_306887493}

[[隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_306887496}

[[Local Address]{lang="EN-US"}]{#struct_0_x1539_x1935_306887498}

[[NVE]{lang="EN-US"}]{#struct_0_x1539_x1935_306887500}[隧道接口的源端地址]{style="font-family:宋体"}

[[Server Address]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679044}

[[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679043}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[未知]{style="font-family:宋体"}

[[Neighbor]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679045}

[[通过]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679048}[学到的邻居]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[System ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679050}

[[邻居的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679052}[地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知]{style="font-family:宋体"}

[[Created Time]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679051}

[[邻居创建的时间]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x446973117}

[[Expire]{lang="EN-US"}]{#struct_0_x1539_x1935_x446973115}

[[邻居的老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x446973112}

[[Status]{lang="EN-US"}]{#struct_0_x1539_x1935_x446973110}

[[与邻居之间]{style="font-family:宋体"}[VXLAN ]{lang="EN-US"}]{#struct_0_x1539_x1935_x446973108}[隧道的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1539_x1935_x446973109}[：表示可以通过]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道进行传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342019}[：表示不可以通过]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道进行传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342021}[：表示尚未创建]{lang="EN-US" style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1436536759 .myid}
[]{#_Toc404798675}[]{#struct_0_x1539_x1935_1509342024}[]{#_Toc393878979}[]{#_Toc383786752}[]{#_Toc383097744}

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery client statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 6 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x9159980}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_1509342023}
:::

[ ]{lang="EN-US"}

[**[display vxlan neighbor-discovery client statistics]{lang="EN-US"}**]{#struct_0_x1539_x1935_x9487660}[命令用来在]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1509342026}

[**[display vxlan neighbor-discovery client statistics interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_x9291052}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1509342025}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x9094444}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1509342028}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x9946412}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x9225516}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310140}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x479198981}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_626679068}[：显示指定]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口对应的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x829310141}

[[通过本命令可以查看开启]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x479133445}[功能后，接口收到和发送]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x829310138}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x478674694}[显示]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan neighbor-discovery client statistics interface tunnel 0]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310137}

[Server Address: 10.0.0.1]{lang="EN-US"}

[Received packets:]{lang="EN-US"}

[  Reply:        170              Error:      1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Register:     170              Purge:      0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Server Address: 10.0.0.2]{lang="EN-US"}

[Received packets:]{lang="EN-US"}

[  Reply:        99               Error:      1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Register:     100              Purge:      0]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display vxlan neighbor-discovery client statistics]{lang="EN-US"}]{#struct_0_x1539_x1935_x479264518}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1774119997}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x829310135}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x829310132}

[[Server Address]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614204}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614202}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Received packets]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614200}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614201}[收到的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reply]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614199}[：表示注册应答报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x1539_x1935_1893841736}[：表示错误指示报文]{lang="EN-US" style="font-family:宋体"}

[[Sent packets]{lang="EN-US"}]{#struct_0_x1539_x1935_1893841738}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_1893841740}[发送的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Register]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810428}[：表示注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Purge]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810429}[：表示注销报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#661069788 .myid}
[]{#_Toc404798676}[]{#struct_0_x1539_x1935_x97840684}[]{#_Toc393878980}[]{#_Toc383786753}[]{#_Toc383097745}[]{#_Toc378325575}[]{#_Toc367864373}

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery client summary**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 7 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810426}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x96988716}
:::

[ ]{lang="EN-US"}

[**[display vxlan neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_x444810427}[命令用来在]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x96923180}

[**[display vxlan neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_1047237949}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x444810424}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x97119788}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_229656827}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810425}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x97054252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1366496364}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810422}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x97250860}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810423}[的运行信息，包括]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的配置信息、]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[与]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的连接状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x97185324}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x210208870}[显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan neighbor-discovery client summary]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810420}

[                         Status: I-Init  E-Establish  P-Probe]{lang="EN-US"}

[Interface    Local Address   Server Address  Network ID  Reg  Auth      Status]{lang="EN-US"}

[Tunnel0      20.0.0.2        20.0.0.1        1           15   enabled   E]{lang="EN-US"}

[Tunnel0      20.0.0.2        20.0.0.3        1           15   enabled   P]{lang="EN-US"}

[Tunnel1      21.0.0.2        21.0.0.1        2           15   disabled  P]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display vxlan neighbor-discovery client summary]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810421}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1788445446}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1511504708}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1511504710}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504709}

[[启动]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504712}[功能的接口名称]{style="font-family:宋体"}

[[Local Address]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504714}

[[本地]{style="font-family:宋体"}[NVE]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504716}[隧道接口的源端地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置]{style="font-family:宋体"}

[[Server Address]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504715}

[[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147453}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147451}

[[隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147448}[，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置]{style="font-family:宋体"}

[[Reg]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147449}

[[注册时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x827147446}

[[Auth]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147444}

[[是否开启认证功能：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1636451516}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451517}[：表示已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451514}[：表示未开启]{lang="EN-US" style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451513}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451510}[与]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的连接状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451511}[：表示初始状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451509}[：表示已建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x1539_x1935_319863619}[：表示未建立连接正在探测]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_319863622}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_x1539_x1935_988887461}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan neighbor-discovery client enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_319863621}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_988887458}

::::: {#212974923 .myid}
[]{#_Toc404798677}[]{#struct_0_x1539_x1935_319863624}[]{#_Toc393878981}[]{#_Toc383786754}[]{#_Toc383097746}[]{#_Toc378325576}[]{#_Toc367864374}

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery server member**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 8 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_988887463}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_319863623}
:::

[ ]{lang="EN-US"}

[**[display vxlan neighbor-discovery server member]{lang="EN-US"}**]{#struct_0_x1539_x1935_319863626}[命令用来在]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的成员信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_988887465}

[**[display vxlan neighbor-discovery server member]{lang="EN-US"}**[ \[ **interface** **tunnel** *interface-number* \| **local** *local-ip* \| **remote** *client-ip* \]]{lang="EN-US"}]{#struct_0_x1539_x1935_319863625}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_319863628}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_988887451}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_319863627}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353668}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_213910264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1065815701}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353667}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_213844728}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1887353670}[：显示通过指定]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口学到的成员信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[local ]{lang="EN-US"}***[local-ip]{lang="EN-US"}*]{#struct_0_x1539_x1935_213385977}[：显示指定]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的成员信息。]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*[表示本地]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[remote ]{lang="EN-US"}***[client-ip]{lang="EN-US"}*]{#struct_0_x1539_x1935_1887353669}[：显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的成员信息。]{style="font-family:宋体"}*[client-ip]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_213975800}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x451298490}[学到的成员信息，包括成员的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址、桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、创建时间、老化时间等信息。]{style="font-family:宋体"}

[[如果不指定任何参数，将显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_264607414}[学到的所有成员信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x451298491}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x451298488}[显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[成员信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan neighbor-discovery server member]{lang="EN-US"}]{#struct_0_x1539_x1935_x451298487}

[Interface: Tunnel0    Network ID: 1]{lang="EN-US"}

[IP Address: 11.0.0.1]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time]{lang="EN-US"}

[11.0.0.3        000F-0001-0001    25        2011/01/01 00:00:43]{lang="EN-US"}

[11.0.0.4        000F-0001-0002    15        2011/01/01 01:00:46]{lang="EN-US"}

[11.0.0.5        000F-0001-0003    20        2011/01/01 01:02:13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel1    Network ID: 2]{lang="EN-US"}

[IP Address: 11.0.1.2]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time]{lang="EN-US"}

[11.0.1.3        000F-0001-0011    19        2011/01/01 00:19:31]{lang="EN-US"}

[11.0.1.4        000F-0001-0012    30        2011/01/01 02:00:43]{lang="EN-US"}

[11.0.1.5        000F-0001-0013    20        2011/01/01 01:02:13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel2    Network ID: 3]{lang="EN-US"}

[IP Address: 12.0.0.1]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time]{lang="EN-US"}

[12.0.0.2        000F-0002-0001    30        2011/01/01 03:20:43]{lang="EN-US"}

[12.0.0.3        000F-0002-0002    37        2011/01/01 03:27:46]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display vxlan neighbor-discovery server member]{lang="EN-US"}]{#struct_0_x1539_x1935_265066167}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1802172497}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x451298485}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1505016644}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016646}

[[启动]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016645}[功能的接口名称]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016647}

[[隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016650}

[[IP Address]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016652}

[[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635516}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Client Address]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635514}

[[学到的成员的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635512}[地址]{style="font-family:宋体"}

[[System ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635510}

[[学到的成员的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635508}[地址]{style="font-family:宋体"}

[[Expire ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939580}

[[成员的剩余老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1642939578}

[[Created Time]{lang="EN-US"}]{#struct_0_x1539_x1935_1507179335}

[[成员的创建时间]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1507179337}

[ ]{lang="EN-US"}

::::: {#-624506768 .myid}
[]{#_Toc404798678}[]{#struct_0_x1539_x1935_917454142}[]{#_Toc393878982}[]{#_Toc383786755}[]{#_Toc383097747}[]{#_Toc378325577}[]{#_Toc367864375}

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery server statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 9 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_1507179340}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_917388609}
:::

[ ]{lang="EN-US"}

[**[display vxlan neighbor-discovery server statistics]{lang="EN-US"}**]{#struct_0_x1539_x1935_1507179339}[命令用来在]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472828}

[**[display vxlan neighbor-discovery server statistics interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1384041419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472829}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1384106955}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472826}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1384172491}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1384238027}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472824}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1384303563}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_x831472825}[：显示指定]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472822}

[[通过本命令可以查看开启]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_1384434635}[功能后，接口收到和发送报文的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472823}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1384500171}[显示]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan neighbor-discovery server statistics interface tunnel 0]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472821}

[Received packets:]{lang="EN-US"}

[  Register:     170              Purge:      13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Reply:        170              Error:      1]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display vxlan neighbor-discovery server statistics]{lang="EN-US"}]{#struct_0_x1539_x1935_1384631243}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1729621808}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640776893}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640776890}

[[Received packets]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776888}

[[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776889}[收到的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Register]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776887}[：表示注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Purge]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776884}[：表示注销报文]{lang="EN-US" style="font-family:宋体"}

[[Sent packets]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329801}

[[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329804}[发送的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reply]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322364}[：表示注册应答报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322362}[：表示错误指示报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1731354522 .myid}
[]{#_Toc404798679}[]{#struct_0_x1539_x1935_x438322363}[]{#_Toc393878983}[]{#_Toc383786756}[]{#_Toc383097748}[]{#_Toc378325578}[]{#_Toc367864376}

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery server summary**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 10 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_412011374}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x438322360}
:::

[ ]{lang="EN-US"}

[**[display vxlan neighbor-discovery server summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_x438322361}[命令用来在]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_411880302}

[**[display vxlan neighbor-discovery server summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_x438322358}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_412470125}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x438322359}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_412404589}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322356}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_411814765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322357}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1517992772}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1517992771}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_1475484364}[的运行信息，包括]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的配置信息、通过该]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学习到的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[个数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1517992774}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1475287756}[显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan neighbor-discovery server summary]{lang="EN-US"}]{#struct_0_x1539_x1935_1517992776}

[Interface      Local Address   Network ID    Auth        Members]{lang="EN-US"}

[Tunnel0        20.0.0.1        1             enabled     10]{lang="EN-US"}

[Tunnel2        21.0.0.1        2             disabled    20]{lang="EN-US"}

[Tunnel3        22.0.0.1        NA            disabled    0]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display vxlan neighbor-discovery server summary]{lang="EN-US"}]{#struct_0_x1539_x1935_1475418828}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1711774244}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1517992778}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1517992780}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_1517992779}

[[启动]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659389}[功能的接口名称]{style="font-family:宋体"}

[[Local Address]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659386}

[[接口的源端地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659384}[表示未配置]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659385}

[[隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659383}[，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置]{style="font-family:宋体"}

[[Auth]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659380}

[[是否开启认证功能：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1629963452}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963453}[：表示已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963451}[：表示未开启]{lang="EN-US" style="font-family:宋体"}

[[Members]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963446}

[[通过该]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963444}[学习到的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1629963445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_x1539_x1935_284889833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vxlan neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_326351684}

::: {#-767597346 .myid}
[]{#_Toc404798680}[]{#struct_0_x1539_x1935_1474692941}[]{#_Toc393878984}[]{#_Toc383786762}[]{#_Toc367864395}

**VXLAN \-- ENDP配置命令 \-- network-id**

------------------------------------------------------------------------

[**[network-id]{lang="EN-US"}**]{#struct_0_x1539_x1935_326351683}[命令用来配置隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo network-id]{lang="EN-US"}**]{#struct_0_x1539_x1935_1474692948}[命令用来删除隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_326351686}

[**[network-id]{lang="EN-US"}**[ *network-id*]{lang="EN-US"}]{#struct_0_x1539_x1935_326351685}

[**[undo network-id]{lang="EN-US"}**]{#struct_0_x1539_x1935_326351688}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1474692937}

[[没有配置隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_326351687}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_326351690}

[[NVE]{lang="EN-US"}]{#struct_0_x1539_x1935_326351689}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1474692938}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_326351692}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_326351691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1902492484}

[*[number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1902492483}[：]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1902492486}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1899742664}[通过]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[来自动发现远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[。]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[可以划分为多个实例，通过]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[来标识]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[实例。只有属于同一个]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[实例的]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[之间可以互相发现。]{style="font-family:宋体"}

[[需要注意的是，同一台设备的不同]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_1902492485}[接口下必须配置不同的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1899939272}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1902492488}[配置]{style="font-family:宋体"}[NVE]{lang="EN-US"}[隧道]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[为]{style="font-family:宋体"}[123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1902492487}

[\[Sysname\] interface tunnel 0 mode nve]{lang="EN-US"}

[\[Sysname-Tunnel0\] network-id 123]{lang="EN-US"}
:::

::::: {#-1472070890 .myid}
[]{#_Toc404798681}[]{#struct_0_x1539_x1935_x1899808200}[]{#_Toc393878985}[]{#_Toc383786775}[]{#_Toc383097740}

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery authentication**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_1902492490}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_1902492489}
:::

[ ]{lang="EN-US"}

[**[vxlan neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_x1539_x1935_1902492492}[命令用来开启]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[认证功能。]{style="font-family:宋体"}

[**[undo vxlan neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_x1539_x1935_1902492491}[命令用来关闭]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1900201417}

[**[vxlan neighbor-discovery authentication]{lang="EN-US"}**[ { **cipher** \| **simple** } ]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159676}*[password]{lang="EN-US"}*

[**[undo vxlan neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_x1539_x1935_x225111480}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x436159677}

[[ENDP]{lang="EN-US"}]{#struct_0_x1539_x1935_x225045944}[认证功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x436159674}

[[NVE]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159675}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x225177016}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159673}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x436159670}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1539_x1935_x224980408}[：表示以密文方式设置认证密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1539_x1935_x436159671}[：表示以明文方式设置认证密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_x1539_x1935_x224914872}[：设置的明文认证密码或密文认证密码，区分大小写。明文认证密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串；密文认证密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x436159668}

[[为了安全起见，可以配置]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159669}[认证功能来防止恶意的节点注册到]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[网络。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155460}[认证功能后，发送]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[报文的设备会使用配置的密码和]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法对报文进行摘要运算，然后把运算结果放到报文的认证字段。对端设备收到]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[报文后，如果该设备未配置认证功能，则认为报文合法；如果设备配置了认证功能，则利用本端配置的密码和]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法对报文进行摘要运算，然后比较运算结果与报文认证字段携带的信息是否一致，如果一致则认为报文合法，如果不一致则认为报文非法。]{style="font-family:宋体"}

[[只有本端与对端设备上都没有配置]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1656711887}[认证功能，或者都配置了认证功能且认证密码相同，才能在二者之间成功建立]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[在一个安全的网络中，可以不配置]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155459}[认证功能。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1520155462}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1681992203}[VXLAN]{lang="EN-US"}[网络中所有的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[与]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[必须配置相同的认证密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的认证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1520155461}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1682188811}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155464}[开启]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[认证功能，并以明文方式设置认证密码为]{style="font-family:宋体"}[web-vxlan]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155466}

[\[Sysname\] interface tunnel 0 mode nve]{lang="EN-US"}

[\[Sysname-Tunnel0\] vxlan neighbor-discovery authentication simple web-vxlan]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1681730059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_1520155465}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan neighbor-discovery server summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1681926667}
:::::

::::: {#2063828583 .myid}
[]{#_Toc404798682}[]{#struct_0_x1539_x1935_1520155468}[]{#_Toc393878986}[]{#_Toc383786776}[]{#_Toc383097739}

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery client enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155467}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x1681795595}
:::

[ ]{lang="EN-US"}

[**[vxlan neighbor-discovery client enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x818496700}[命令用来开启接口的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，并指定]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo vxlan neighbor-discovery client enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_738507731}[命令用来关闭接口的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x818496701}

[**[vxlan neighbor-discovery client enable ]{lang="EN-US"}***[server-ip]{lang="EN-US"}*]{#struct_0_x1539_x1935_738573267}

[**[undo vxlan neighbor-discovery client enable]{lang="EN-US"}**[ *server-ip*]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496698}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1600668710}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496699}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x818496696}

[[NVE]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496697}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1600209958}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496695}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x818496692}

[*[server-ip]{lang="EN-US"}*]{#struct_0_x1539_x1935_x1600013350}[：]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[要连接的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x818496693}

[[为了防止]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x1599947814}[异常导致]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[不能加入]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[网络，用户可以通过重复执行本命令为每个]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[指定两个]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[。]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[同时向两个]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[注册和获取]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[需要注意的是，建议为地址相同、]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800764}[不同的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[指定不同的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1627800765}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1559963816}[开启]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，并指定]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[地址为]{style="font-family:宋体"}[11.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800763}

[\[Sysname\] interface tunnel 0 mode nve]{lang="EN-US"}

[\[Sysname-Tunnel0\] vxlan neighbor-discovery client enable 11.0.0.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1928434426}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1627800760}
:::::

::::: {#-865181708 .myid}
[]{#_Toc404798683}[]{#struct_0_x1539_x1935_x1627800761}[]{#_Toc393878987}[]{#_Toc383786777}[]{#_Toc383097741}

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery client register-interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 3 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800758}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_1607214591}
:::

[ ]{lang="EN-US"}

[**[vxlan neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1627800759}[命令用来配置]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[注册的时间间隔。]{style="font-family:宋体"}

[**[undo vxlan neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1627800756}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1168722931}

[**[vxlan neighbor-discovery client register-interval]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800757}*[time-value]{lang="EN-US"}*

[**[undo vxlan neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_328514371}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514374}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x746718662}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[注册的时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514373}

[[NVE]{lang="EN-US"}]{#struct_0_x1539_x1935_x746718663}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514376}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_328514375}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x746718661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514378}

[*[time-value]{lang="EN-US"}*]{#struct_0_x1539_x1935_328514377}[：注册时间间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514380}

[[ENDP]{lang="EN-US"}]{#struct_0_x1539_x1935_1883028263}[协议中定义了]{style="font-family:宋体"}[3]{lang="EN-US"}[个定时器：探测定时器、注册定时器、老化定时器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[探测定时器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1539_x1935_1883028264}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623894}[请求加入]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[网络时会启用探测定时器，该定时器以]{style="font-family:宋体"}[5]{lang="EN-US"}[秒的时间间隔定时向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[发送注册报文，收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[应答报文后会停止探测定时器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[注册定时器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1539_x1935_x455623897}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_97359105}[加入]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[网络后，为了通告自己工作正常，会定时向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[发送注册报文，该定时器的默认时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒，用户可以通过配置]{style="font-family:宋体"}**[vxlan neighbor-discovery client register-interval]{lang="EN-US"}**[命令来调整该时间间隔。]{style="font-family:
宋体"}

[[如果]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623896}[连续发送]{style="font-family:宋体"}[5]{lang="EN-US"}[个注册报文，都未能收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的应答报文，则认为网络故障，此时需要清除之前学到的邻居信息，同时重新启用探测定时器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[老化定时器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1539_x1935_x455623891}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623890}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[发送的注册报文中携带注册时间间隔，]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[会记录该时间间隔。]{style="font-family:宋体"}

[[ENDC]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691237}[加入]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[网络后，如果]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[在]{style="font-family:宋体"}[5]{lang="EN-US"}[倍的注册时间内未收到]{style="font-family:
宋体"}[ENDC]{lang="EN-US"}[的注册报文则认为]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[出现故障，此时需要把]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[从]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[网络中删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1500691238}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691235}[配置]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[注册的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_1283954753}

[\[Sysname\] interface tunnel 0 mode nve]{lang="EN-US"}

[\[Sysname-Tunnel0\] vxlan neighbor-discovery client register-interval 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1500691236}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_1284151361}
:::::

::::: {#1011724921 .myid}
[]{#_Toc404798684}[]{#struct_0_x1539_x1935_1500691241}[]{#_Toc393878988}[]{#_Toc383786778}[]{#_Toc383097742}

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery server enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 4 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691242}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_1500691239}
:::

[ ]{lang="EN-US"}

[**[vxlan neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1283692609}[命令用来开启接口的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo vxlan neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1500691240}[命令用来关闭接口的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1500691245}

[**[vxlan neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1283954750}

[**[undo vxlan neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1500691246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960923}

[[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960922}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1738924790}

[[NVE]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960925}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1738466038}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960924}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960919}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960918}

[[开启接口的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960921}[功能时，会同时开启该接口的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能（该]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[地址为该接口的源地址）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960920}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1738793718}[开启]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960914}

[\[Sysname\] interface tunnel 0 mode nve]{lang="EN-US"}

[\[Sysname-Tunnel0\] vxlan neighbor-discovery server enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1738531577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan neighbor-discovery server summary]{lang="EN-US"}**]{#struct_0_x1539_x1935_74358745}
:::::

::: {#-303972291 .myid}
[]{#_Toc404798686}[]{#struct_0_x1539_x1935_x1647264986}[]{#_Toc393878990}[]{#_Toc383786743}[]{#_Toc371583408}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis brief**

------------------------------------------------------------------------

[**[display vxlan isis brief]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1647264989}[命令用来显示]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程的摘要信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1647264988}

[**[display vxlan isis brief]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1647264983}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x737793666}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x453461202}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502853925}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853926}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1605152328}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853923}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1604824648}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502853924}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853929}[显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis brief]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853930}

[Network-entity: 00.0011.2200.0001.00]{lang="EN-US"}

[LSP-length receive: 16384]{lang="EN-US"}

[LSP-length originate: 1400]{lang="EN-US"}

[Timers:]{lang="EN-US"}

[  LSP-max-age: 1200s]{lang="EN-US"}

[  LSP-refresh: 900s]{lang="EN-US"}

[State: Enabled]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display vxlan isis brief]{lang="EN-US"}]{#struct_0_x1539_x1935_1502853927}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1700109965}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502853928}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502853934}

[[Network-entity]{lang="EN-US"}]{#struct_0_x1539_x1935_x835798235}

[[网络实体名称]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x835798237}

[[LSP-length receive]{lang="EN-US"}]{#struct_0_x1539_x1935_x835798231}

[[可以接收]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_1878702889}[的最大长度]{style="font-family:宋体"}

[[LSP-length originate]{lang="EN-US"}]{#struct_0_x1539_x1935_1878702887}

[[生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_1878702893}[的最大长度]{style="font-family:宋体"}

[[Timers]{lang="EN-US"}]{#struct_0_x1539_x1935_x459949275}

[[LSP-max-age]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590363}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590362}[的最大生存时间，单位为秒]{style="font-family:宋体"}

[[LSP-refresh]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590364}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590359}[的刷新周期，单位为秒]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590358}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590360}[进程的运行状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590355}[：表示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程处于开启状态，即已经开启]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址同步功能]{lang="EN-US" style="font-family:宋体"}[或]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[自动协商功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590354}[：表示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程处于关闭状态，即尚未开启]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址同步功能]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[自动协商功能]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#493063886 .myid}
[]{#_Toc404798687}[]{#struct_0_x1539_x1935_304724773}[]{#_Toc393878991}[]{#_Toc383786744}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis graceful-restart status**

------------------------------------------------------------------------

[**[display vxlan isis graceful-restart status]{lang="EN-US"}**]{#struct_0_x1539_x1935_515240972}[命令用来显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x167623472}

[**[display vxlan isis graceful-restart status]{lang="EN-US"}**]{#struct_0_x1539_x1935_304724774}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_515240967}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_304724771}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_515240970}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_304724772}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_515240973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_304724777}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1880865577}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1880865578}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_531348854}[显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis graceful-restart status]{lang="EN-US"}]{#struct_0_x1539_x1935_x457786586}

[Restart status: RESTARTING]{lang="EN-US"}

[Restart phase: LSDB synchronization]{lang="EN-US"}

[Restart interval: 300s]{lang="EN-US"}

[T3 remaining time: 65531s]{lang="EN-US"}

[Total number of interfaces: 1]{lang="EN-US"}

[Number of waiting LSPs: 0]{lang="EN-US"}

[T2 remaining time: 56s]{lang="EN-US"}

[  Interface: Tunnel0]{lang="EN-US"}

[    T1 remaining time: 2]{lang="EN-US"}

[    RA received: N]{lang="EN-US"}

[    CSNP received: N]{lang="EN-US"}

[    T1 expired number: 3]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display vxlan isis graceful-restart status]{lang="EN-US"}]{#struct_0_x1539_x1935_x825018606}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1672791887}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x457786589}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x457786582}

[[Restart status]{lang="EN-US"}]{#struct_0_x1539_x1935_x457786584}

[[重启状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x457786578}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_x1539_x1935_306887461}[[：重启完成]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[STARTING]{lang="EN-US"}]{#struct_0_x1539_x1935_306887460}[[：重启开始]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[RESTARTING]{lang="EN-US"}]{#struct_0_x1539_x1935_1509341992}[[：重启中]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNKNOWN]{lang="EN-US"}]{#struct_0_x1539_x1935_1509341998}[[：未知状态]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[Restart phase]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310170}

[[重启阶段，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x829310167}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initialization]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310169}[：初始阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSDB synchronization]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310163}[：]{lang="EN-US" style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[同步阶段]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC receiving]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614235}[：接收本地]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址上报的阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stable]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614237}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614230}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新和泛洪的阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504686}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[完成的阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147482}[：未知阶段]{lang="EN-US" style="font-family:宋体"}

[[Restart interval]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353636}

[[重启间隔时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1887353642}

[[重启间隔时间即]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353640}[定时器的值，用来控制]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步时间。如果在]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间内没有完成]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步，则]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败，退出]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程]{style="font-family:宋体"}

[[该值可以通过]{style="font-family:宋体"}**[graceful-restart interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_1887353645}[命令设置]{style="font-family:宋体"}

[[T3 remaining time]{lang="EN-US"}]{#struct_0_x1539_x1935_x451298522}

[[定时器]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_x1539_x1935_x451298519}[的剩余时间，单位为秒]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_x1539_x1935_x451298521}[定时器内邻居不会断掉与重启设备的邻接关系。如果]{style="font-family:宋体"}[T3]{lang="EN-US"}[定时器超时后]{style="font-family:宋体"}[GR]{lang="EN-US"}[还没有完成，则]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[T3]{lang="EN-US"}]{#struct_0_x1539_x1935_x451298515}[定时器的值不可配置]{style="font-family:宋体"}

[[Total number of interfaces]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016613}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016614}[进程下的接口数]{style="font-family:宋体"}

[[Number of waiting LSPs]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016611}

[[GR Restarter]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016617}[与]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步时，未完成同步的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[T2 remaining time]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016615}

[[定时器]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016621}[的剩余时间，单位为秒]{style="font-family:宋体"}

[[T2]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635549}[定时器用来控制]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[的同步时间]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635543}

[[指定接口下]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635544}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[T1 remaining time]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939611}

[[定时器]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939612}[的剩余时间，单位为秒]{style="font-family:宋体"}

[[T1]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939609}[定时器用来控制带]{style="font-family:宋体"}[RR]{lang="EN-US"}[（]{style="font-family:宋体"}[Restart Request]{lang="EN-US"}[，]{style="font-family:宋体"}[Restart]{lang="EN-US"}[请求）标志位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的重传时间。如果在]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器内没有接收到对端回复的带有]{style="font-family:宋体"}[RA]{lang="EN-US"}[（]{style="font-family:宋体"}[Restart Acknowledgement]{lang="EN-US"}[，]{style="font-family:宋体"}[Restart]{lang="EN-US"}[应答）标志的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，则重传带]{style="font-family:宋体"}[RR]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[T1]{lang="EN-US"}]{#struct_0_x1539_x1935_313375525}[定时器的值不可配置]{style="font-family:宋体"}

[[RA received]{lang="EN-US"}]{#struct_0_x1539_x1935_313375524}

[[接口上是否收到邻居发送的带]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_x1539_x1935_313375528}[标志位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[CSNP received]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516325}

[[接口上是否收到完整的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516323}[报文，即是否完成与]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[T1 expired number]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516330}

[[定时器]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_x1539_x1935_1889516328}[的超时次数，超时达到]{style="font-family:宋体"}[10]{lang="EN-US"}[次后，不会再进行带]{style="font-family:宋体"}[RR]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的重传]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1069090605 .myid}
[]{#_Toc404798688}[]{#struct_0_x1539_x1935_1889516333}[]{#_Toc393878992}[]{#_Toc383786745}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis local-mac**

------------------------------------------------------------------------

[**[display vxlan isis local-mac]{lang="EN-US"}**]{#struct_0_x1539_x1935_1889516334}[命令用来显示]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x449135835}

[**[display vxlan isis local-mac dynamic]{lang="EN-US"}**[ \[ \[ **vxlan-id** *vxlan-id* \] \[ **count** \] \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x1579044103}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x449135834}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1579109639}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x449135837}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1579175175}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x449135836}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1579240711}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x449135831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1578781959}

[**[dynamic]{lang="EN-US"}**]{#struct_0_x1539_x1935_x449135830}[：显示本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[vxlan-id ]{lang="EN-US"}***[vxlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x1578847495}[：显示指定]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[vxlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x1539_x1935_x449135833}[：显示本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1578913031}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x673723111}[显示所有]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis local-mac dynamic]{lang="EN-US"}]{#struct_0_x1539_x1935_x449135826}

[  VXLAN ID: 100]{lang="EN-US"}

[    MAC address: 00aa-00bb-00cc]{lang="EN-US"}

[    MAC address: 00aa-00cc-00bb]{lang="EN-US"}

[    MAC address: 00cc-00aa-00bb]{lang="EN-US"}

[  VXLAN ID: 50]{lang="EN-US"}

[    MAC address: 00bb-00aa-00cc]{lang="EN-US"}

[    MAC address: 00bb-00cc-00aa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1579240712}[显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis local-mac dynamic count]{lang="EN-US"}]{#struct_0_x1539_x1935_1507179301}

[5 MAC addresses found.]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display vxlan isis local-mac]{lang="EN-US"}]{#struct_0_x1539_x1935_917323069}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1620914820}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1507179299}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1507179300}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1507179303}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1507179309}[编号]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472859}

[[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472861}[地址]{style="font-family:宋体"}

[[5 MAC addresses found]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472857}

[[本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472851}[地址的数目，本例中本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目为]{style="font-family:宋体"}[5]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#897093631 .myid}
[]{#_Toc404798689}[]{#struct_0_x1539_x1935_1384631244}[]{#_Toc393878993}[]{#_Toc383786746}[]{#_Toc371583411}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis lsdb**

------------------------------------------------------------------------

[**[display vxlan isis lsdb]{lang="EN-US"}**]{#struct_0_x1539_x1935_x831472850}[命令用来显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的链路状态数据库。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640776923}

[**[display vxlan isis lsdb]{lang="EN-US"}**[ \[ **local** \| **lsp-id** *lsp-id* \| **verbose** \] \* \[ **tunnel** *tunnel-number* \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x343465878}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640776922}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1222618063}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640776925}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776924}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_416049009}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1624817850}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776919}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1175629432}

[**[local]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1640776918}[：显示当前设备产生的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[lsp-id]{lang="EN-US"}**[ *lsp-id*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776921}[：显示指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[LSP]{lang="EN-US"}[标识，形式为]{style="font-family:宋体"}[SYSID*.*Pseudonode ID-fragment num]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[SYSID]{lang="EN-US"}[是产生该]{style="font-family:宋体"}[LSP]{lang="EN-GB"}[的节点或伪节点的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[，]{style="font-family:宋体"}[Pseudonode ID]{lang="EN-US"}[是伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[fragment num]{lang="EN-US"}[是该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片号。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1640776920}[：显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的详细信息。如果不指定本参数，将显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的摘要信息。]{style="font-family:宋体"}

[**[tunnel]{lang="EN-US"}**[ *tunnel-number*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1909549819}[：显示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640776915}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1149969396}[显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[链路状态数据库的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis lsdb]{lang="EN-US"}]{#struct_0_x1539_x1935_315538213}

[ ]{lang="EN-US"}

[          Link state database information for VXLAN ISIS (Tunnel 0)]{lang="EN-US"}

[LSP ID                   Seq num     Checksum  Holdtime  Length    Overload]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0011.2200.0201.0000-00   0x00000063  0x1bc2    1104      74        0]{lang="EN-US"}

[0011.2200.0401.0000-00\*  0x00000060  0x7f76    1089      55        0]{lang="EN-US"}

[0011.2200.0401.0001-00\*  0x0000005f  0xf77     1175      57        0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flags: \*-Self LSP, +-Self LSP(Extended)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_2076717815}[显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[链路状态数据库的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis lsdb verbose]{lang="EN-US"}]{#struct_0_x1539_x1935_315538218}

[ ]{lang="EN-US"}

[          Link state database information for VXLAN ISIS (Tunnel 0)]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID: 0011.2200.0201.0000-00]{lang="EN-US"}

[Sequence number: 0x00000063]{lang="EN-US"}

[Checksum: 0x1bc2]{lang="EN-US"}

[Holdtime: 745s]{lang="EN-US"}

[Length: 74]{lang="EN-US"}

[Overload: 0]{lang="EN-US"}

[Source: 0011.2200.0201.0000]{lang="EN-US"}

[Neighbour]{lang="EN-US"}

[    ID: 0011.2200.0401.0001, Cost: 10]{lang="EN-US"}

[VXLANs:]{lang="EN-US"}

[    VXLAN ID: 100]{lang="EN-US"}

[    VXLAN ID: 10]{lang="EN-US"}

[MAC addresses:]{lang="EN-US"}

[  VXLAN ID: 10   Confidence: 1]{lang="EN-US"}

[    0001-0001-0001]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID: 0011.2200.0401.0000-00\*]{lang="EN-US"}

[Sequence number: 0x00000060]{lang="EN-US"}

[Checksum: 0x7f76]{lang="EN-US"}

[Holdtime: 730s]{lang="EN-US"}

[Length: 55]{lang="EN-US"}

[Overload: 0]{lang="EN-US"}

[Source: 0011.2200.0401.0000]{lang="EN-US"}

[Neighbour]{lang="EN-US"}

[    ID: 0011.2200.0401.0001, Cost: 10]{lang="EN-US"}

[VXLANs:]{lang="EN-US"}

[    VXLAN ID: 10]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID: 0011.2200.0401.0001-00\*]{lang="EN-US"}

[Sequence number: 0x0000005f]{lang="EN-US"}

[Checksum: 0xf77]{lang="EN-US"}

[Holdtime: 816s]{lang="EN-US"}

[Length: 57]{lang="EN-US"}

[Overload: 0]{lang="EN-US"}

[Source: 0011.2200.0401.0001]{lang="EN-US"}

[Neighbour]{lang="EN-US"}

[    ID: 0011.2200.0201.0000, Cost: 0]{lang="EN-US"}

[    ID: 0011.2200.0401.0000, Cost: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flags: \*-Self LSP, +-Self LSP(Extended)]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display vxlan isis lsdb]{lang="EN-US"}]{#struct_0_x1539_x1935_315538215}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1875926478}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_315538222}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x820659418}

[[Link state database information for VXLAN IS-IS (Tunnel 1)]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659420}

[[Tunnel1]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659415}[上]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的链路状态数据库信息]{style="font-family:宋体"}

[[LSP ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659411}

[[链路状态报文]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963483}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[带]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1629963485}[\*]{lang="EN-US"}[号表示是本地生成的、原始系统]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[带]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1629963479}[+]{lang="EN-US"}[号表示是本地生成的、虚拟系统]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩展分片）]{style="font-family:宋体"}

[[Sequence number]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963481}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963475}[序列号]{style="font-family:宋体"}

[[Checksum]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496731}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496732}[校验和]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496729}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496723}[生存时间，随着时间推移递减，单位为秒]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800794}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800796}[长度]{style="font-family:宋体"}

[[Overload]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800793}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800787}[中]{style="font-family:宋体"}[Overload bit]{lang="EN-US"}[的置位情况。]{style="font-family:宋体"}[1]{lang="EN-US"}[表示置位，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有置位]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_x1539_x1935_328514342}

[[LSP]{lang="SV"}]{#struct_0_x1539_x1935_328514345}[生成路由器的]{style="font-family:宋体"}[System ID]{lang="SV"}

[[Neighbour]{lang="EN-US"}]{#struct_0_x1539_x1935_328514344}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_328514349}[生成路由器的邻居信息]{style="font-family:宋体"}

[[ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1883028358}

[[邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1883028356}

[[Cost]{lang="EN-US"}]{#struct_0_x1539_x1935_1883028361}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_1883028359}[生成路由器和邻居之间链路的开销值]{style="font-family:宋体"}

[[VXLANs]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623802}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623805}[中包含的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623800}

[[通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x455623795}[发布的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[MAC addresses]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691332}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691337}[中包含的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691336}

[[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691335}[地址所属的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[Confidence]{lang="EN-US"}]{#struct_0_x1539_x1935_1500691341}

[[可信度，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960826}[表示可信，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示不可信。当]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址出现冲突时，优选可信度为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1068181059 .myid}
[]{#_Toc404798690}[]{#struct_0_x1539_x1935_x837960827}[]{#_Toc393878994}[]{#_Toc383786747}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis peer**

------------------------------------------------------------------------

[**[display vxlan isis peer]{lang="EN-US"}**]{#struct_0_x1539_x1935_x217718026}[命令用来显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1737525350}

[**[display vxlan isis peer]{lang="EN-US"}**]{#struct_0_x1539_x1935_1464591212}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960828}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x218045706}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1498206326}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1030780966}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1268323520}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960829}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x218111242}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1096196741}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960822}[显示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis peer]{lang="EN-US"}]{#struct_0_x1539_x1935_x837960824}

[System ID: 0011.2200.0201]{lang="EN-US"}

[Link interface: Tunnel1]{lang="EN-US"}

[Circuit ID: 0011.2200.0401.0001]{lang="EN-US"}

[State: Up]{lang="EN-US"}

[Hold time: 26s]{lang="EN-US"}

[Neighbour DED priority: 64]{lang="EN-US"}

[Uptime: 00:01:24]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display vxlan isis peer]{lang="EN-US"}]{#struct_0_x1539_x1935_x217783562}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1806755187}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x837960818}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1647264891}

[[System ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x1647264886}

[[邻居的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x1647264889}

[[Link interface]{lang="EN-US"}]{#struct_0_x1539_x1935_x1647264883}

[[与对端相连的本地]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_309050245}[接口]{style="font-family:宋体"}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x1539_x1935_309050243}

[[链路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1539_x1935_309050249}

[[State]{lang="EN-US"}]{#struct_0_x1539_x1935_309050248}

[[邻居状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_309050254}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x1539_x1935_1885191046}[：邻居初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1539_x1935_1885191044}[：邻接关系建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1539_x1935_1885191050}[：邻接关系断开]{style="font-family:宋体"}

[[Hold time]{lang="EN-US"}]{#struct_0_x1539_x1935_1885191049}

[[存活时间，随着时间推移递减，单位为秒]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1885191048}

[[如果在存活时间内还没有收到邻居发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1539_x1935_1885191054}[报文，则认为邻居已经失效，如果收到了]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，则存活时间将重置为初始值]{style="font-family:宋体"}

[[Neighbour DED Priority]{lang="EN-US"}]{#struct_0_x1539_x1935_x453461114}

[[邻居接口]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_x453461115}[优先级，]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级数值高的设备被选为]{style="font-family:宋体"}[DED ]{lang="EN-US"}

[[Uptime]{lang="EN-US"}]{#struct_0_x1539_x1935_x453461117}

[[邻居关系保持的时间]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x453461111}

[ ]{lang="EN-US"}

::: {#872062984 .myid}
[]{#_Toc404798691}[]{#struct_0_x1539_x1935_x453461112}[]{#_Toc393878995}[]{#_Toc383786748}[]{#_Toc371583413}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis remote-mac**

------------------------------------------------------------------------

[**[display vxlan isis remote-mac]{lang="EN-US"}**]{#struct_0_x1539_x1935_x453461113}[命令用来显示通过]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[学习到的远端]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_191987181}

[**[display vxlan isis remote-mac]{lang="EN-US"}**[ \[ \[ **vxlan-id** *vxlan-id* \] \[ **count** \] \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x453461106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_192314862}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x453461107}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_192249326}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1502854022}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1502854021}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1502854020}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1502854019}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502854026}

[**[vxlan-id ]{lang="EN-US"}***[vxlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1502854024}[：显示指定]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[vxlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x1539_x1935_1502854023}[：显示远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1502854030}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1502854029}[显示通过]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[学习到的所有远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis remote-mac]{lang="EN-US"}]{#struct_0_x1539_x1935_x835798140}

[MAC Flags: A-MAC received on an active tunnel interface.]{lang="EN-US"}

[           C-MAC conflict with local dynamic MAC.]{lang="EN-US"}

[           F-MAC has been flushed to the remote MAC address table.]{lang="EN-US"}

[ ]{lang="EN-US"}

[  VXLAN ID: 10]{lang="EN-US"}

[    MAC address: 0001-0001-0001]{lang="EN-US"}

[      Interface: Tunnel1]{lang="EN-US"}

[          Flags: AF]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_332433290}[显示通过]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[学习到的所有远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis remote-mac count]{lang="EN-US"}]{#struct_0_x1539_x1935_x835798134}

[1 MAC addresses found.]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display vxlan isis remote-mac]{lang="EN-US"}]{#struct_0_x1539_x1935_x1645102195}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1776523730}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_311212932}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1496365961}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_1496365966}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286202}[的编号]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286205}

[[通过]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286198}[学习到的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286200}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x842286194}[地址对应的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590266}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590267}[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址标记，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590268}[：该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址从有效的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口接收到]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590262}[：该]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与]{lang="EN-US" style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[本地动态]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址冲突]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590264}[：该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址已经下发到远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表]{style="font-family:宋体"}

[[1 MAC address(es) found]{lang="EN-US"}]{#struct_0_x1539_x1935_x1651590258}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_304724870}[地址的数目，本例中远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目为]{style="font-family:宋体"}[1]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-2061308443 .myid}
[]{#_Toc404798692}[]{#struct_0_x1539_x1935_1498528648}[]{#_Toc393878996}[]{#_Toc383786749}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis remote-vxlan**

------------------------------------------------------------------------

[**[display vxlan isis remote-vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1373326546}[命令用来显示通过]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[学习到的远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1498528654}

[**[display]{lang="EN-US"}[ vxlan isis remote-vxlan]{lang="EN-US"}**[ \[ *vxlan-id* \| **count** \]]{lang="EN-US"}]{#struct_0_x1539_x1935_1498528653}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x840123514}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x840123515}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x840123516}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x840123517}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x1649427570}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1649427571}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_306887558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_306887557}

[*[vxlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_306887556}[：显示指定远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vxlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x1539_x1935_306887555}[：显示远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1891679114}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679112}[显示通过]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[学习到的所有远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis remote-vxlan]{lang="EN-US"}]{#struct_0_x1539_x1935_1891679117}

[VXLAN Flags: S-VXLAN supported at the local end.]{lang="EN-US"}

[             F-The association between VXLAN and Tunnels has been flushed to L2VPN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[      VXLAN ID: 10]{lang="EN-US"}

[      Tunnels: 1, 3-5]{lang="EN-US"}

[      Flags: SF]{lang="EN-US"}

[\<Sysname\> display vxlan isis remote-vxlan count]{lang="EN-US"}

[1 remote VXLANs found.]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display vxlan isis remote-mac]{lang="EN-US"}]{#struct_0_x1539_x1935_x446973050}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1471182125}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x446973053}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x446973048}

[[VXLAN ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x446973042}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342086}[学习到的远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}

[[Tunnels]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342090}

[[远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342089}[关联的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342087}

[[远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1509342093}[标记，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310074}[：本地支持该远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310076}[：该]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[与隧道的关联关系已经通知给]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x1539_x1935_x90890090}[：本地不支持该远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}

[[1 remote VXLANs found]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310070}

[[远端]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x829310072}[的数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1560051687 .myid}
[]{#_Toc371583415}[]{#_Toc404798693}[]{#struct_0_x1539_x1935_x829310066}[]{#_Toc393878997}[]{#_Toc383786750}

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis tunnel**

------------------------------------------------------------------------

[**[display vxlan isis tunnel]{lang="EN-US"}**]{#struct_0_x1539_x1935_1859322109}[命令用来显示]{style="font-family:
宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x829310067}

[**[display vxlan isis tunnel]{lang="EN-US"}**[ \[ *tunnel-number* \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x1638614139}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1638614140}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1638614141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_317700995}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_317701002}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_317701001}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_317701000}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_1283796101}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_317700999}

[*[tunnel-number]{lang="EN-US"}*]{#struct_0_x1539_x1935_1686508313}[：显示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[信息。如果不指定本参数，将显示所有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_317701006}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_317701005}[显示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[101]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display vxlan isis tunnel 101]{lang="EN-US"}]{#struct_0_x1539_x1935_1893841797}

[Tunnel101]{lang="EN-US"}

[MTU: 1400]{lang="EN-US"}

[DED: Yes]{lang="EN-US"}

[DED priority: 80]{lang="EN-US"}

[Hello timer: 10s]{lang="EN-US"}

[Hello multiplier: 3]{lang="EN-US"}

[CSNP timer: 10s]{lang="EN-US"}

[LSP timer: 100ms]{lang="EN-US"}

[Max LSP transmit number: 5]{lang="EN-US"}

[VXLANs:]{lang="EN-US"}

[  1,50,100]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[display vxlan isis tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_167764753}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1428789843}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1893841795}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1893841801}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_1893841800}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1893841799}[隧道接口编号]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_x1539_x1935_1893841805}

[[链路]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810362}[值]{style="font-family:宋体"}

[[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810364}

[[是否被选举为]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810365}[：]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示是；]{style="font-family:宋体"}[No]{lang="EN-US"}[表示否]{style="font-family:宋体"}

[[DED priority]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810358}

[[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810360}[优先级]{style="font-family:宋体"}

[[Hello timer]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810361}

[[Hello]{lang="EN-US"}]{#struct_0_x1539_x1935_x444810355}[报文发送时间间隔，单位为秒]{style="font-family:宋体"}

[[Hello multiplier]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504774}

[[Hello]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504772}[报文失效数目]{style="font-family:宋体"}

[[CSNP timer]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504777}

[[CSNP]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504775}[报文发送时间间隔，单位为秒]{style="font-family:宋体"}

[[LSP timer]{lang="EN-US"}]{#struct_0_x1539_x1935_1511504782}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147386}[的最小发送时间间隔，单位为毫秒]{style="font-family:宋体"}

[[Max LSP transmit number]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147388}

[[一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147389}[数目]{style="font-family:宋体"}

[[VXLANs]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147383}

[[与]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_x827147384}[接口关联的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#63544256 .myid}
[]{#_Toc404798694}[]{#struct_0_x1539_x1935_x827147385}[]{#_Toc393878998}[]{#_Toc383786757}

**VXLAN \-- VXLAN IS-IS配置命令 \-- graceful-restart**

------------------------------------------------------------------------

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1539_x1935_x827147378}[命令用来使能]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_x1539_x1935_93031477}[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x827147379}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1636451450}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1367964094}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1636451451}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1360919261}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1636451452}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x205164680}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1636451453}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1771248621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451446}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1636451447}

[[GR]{lang="EN-US"}]{#struct_0_x1539_x1935_554284671}[（]{style="font-family:宋体"}[Graceful Restart]{lang="EN-US"}[，平滑重启）是一种在协议重启或主备倒换时保证转发业务不中断的机制。需要协议重启或主备倒换的设备将重启状态通知给邻居，允许邻居重新建立邻接关系而不终止连接。]{style="font-family:宋体"}

[[GR]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451448}[有两个角色：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GR Restarter]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451449}[：发生协议重启或主备倒换事件且具有]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力的设备。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GR Helper]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451442}[：和]{lang="EN-US" style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[具有邻居关系，协助完成]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[流程的设备。]{lang="EN-US" style="font-family:宋体"}

[[GR Restarter]{lang="EN-US"}]{#struct_0_x1539_x1935_x1636451443}[和]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[上都需要使能]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1771314157}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_319863685}[使能]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_319863684}

[\[Sysname\] vxlan-isis]{lang="EN-US"}

[\[Sysname-vxlan-isis\] graceful-restart]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_319863683}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan isis graceful-restart status]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1394394716}
:::

::: {#16863910 .myid}
[]{#_Toc404798695}[]{#struct_0_x1539_x1935_319863690}[]{#_Toc393878999}[]{#_Toc383786758}

**VXLAN \-- VXLAN IS-IS配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

[**[graceful-restart interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_319863689}[命令用来配置]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[协议的]{style="font-family:
宋体"}[GR]{lang="EN-US"}[重启间隔时间。]{style="font-family:宋体"}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_319863688}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_319863687}

[**[graceful-restart interval]{lang="EN-US"}**[ *interval-value*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1394394712}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_x1539_x1935_319863694}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_319863693}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353734}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2125004035}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353733}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2125069571}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353732}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x2125135107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1887353738}

[*[interval-value]{lang="EN-US"}*]{#struct_0_x1539_x1935_x2124741891}[：]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1887353737}

[[本命令配置的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353736}[重启间隔时间作为]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器的值，用来控制]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步时间。如果在]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间内没有完成]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步，则]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败，退出]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2124872963}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353735}[配置]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1887353742}

[\[Sysname\] vxlan-isis]{lang="EN-US"}

[\[Sysname-vxlan-isis\] graceful-restart interval 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2125135114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan isis graceful-restart status]{lang="EN-US"}**]{#struct_0_x1539_x1935_x451298426}
:::

::: {#-1553303123 .myid}
[]{#_Toc404798696}[]{#struct_0_x1539_x1935_x451298427}[]{#_Toc393879000}[]{#_Toc383786759}

**VXLAN \-- VXLAN IS-IS配置命令 \-- log-peer-change enable**

------------------------------------------------------------------------

[**[log-peer-change enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x451298428}[命令用来打开邻接状态变化的输出开关。]{style="font-family:宋体"}

[**[undo log-peer-change enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_265131709}[命令用来关闭邻接状态变化的输出开关。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x451298429}

[**[log-peer-change enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x451298422}

[**[undo log-peer-change enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x451298423}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x451298424}

[[邻接状态变化的输出开关处于打开状态。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x451298425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x451298419}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016710}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1505016709}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016708}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_244190495}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1505016707}

[[打开邻接状态变化的输出开关后，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_243469599}[邻接状态变化时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_757776846}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016714}[打开邻接状态变化的输出开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016713}

[\[Sysname\] vxlan-isis]{lang="EN-US"}

[\[Sysname-vxlan-isis\] log-peer-change enable]{lang="EN-US"}
:::

::: {#81514559 .myid}
[]{#_Toc404798697}[]{#struct_0_x1539_x1935_243731744}[]{#_Toc393879001}[]{#_Toc383786760}[]{#_Toc371583431}

**VXLAN \-- VXLAN IS-IS配置命令 \-- mac-synchronization enable**

------------------------------------------------------------------------

[**[mac-synchronization enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1415686690}[命令用来开启]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址同步功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[mac-synchronization enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1505016712}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_243797280}

[**[mac-synchronization enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_178581639}

[**[undo mac-synchronization enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_1505016711}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_243600672}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1505016718}[不会在]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[之间同步]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_244190496}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_1781621658}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1505016717}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635450}

[[mdc-admim]{lang="EN-US"}]{#struct_0_x1539_x1935_2030607313}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x833635451}

[[开启本功能后，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_2030672849}[可以通过]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[协议发布本地的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息，并能够接收其他]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[发布的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_95220246}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635452}[开启]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址同步功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635453}

[\[Sysname\] vxlan-isis]{lang="EN-US"}

[\[Sysname-vxlan-isis\] mac-synchronization enable]{lang="EN-US"}
:::

::: {#-624957747 .myid}
[]{#_Toc404798698}[]{#struct_0_x1539_x1935_2030541777}[]{#_Toc393879002}[]{#_Toc383786761}[]{#_Toc371583430}

**VXLAN \-- VXLAN IS-IS配置命令 \-- negotiate-vni enable**

------------------------------------------------------------------------

[**[negotiate-vni enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1070164957}[命令用来开启]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[自动协商功能。]{style="font-family:宋体"}

[**[undo negotiate-vni enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x833635446}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2030738386}

[**[negotiate-vni enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1512460981}

[**[undo negotiate-vni enable]{lang="EN-US"}**]{#struct_0_x1539_x1935_x833635447}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2030803922}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x833635448}[不会在]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[之间交互]{style="font-family:宋体"}[VXLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2031131602}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x1857514594}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x833635449}

[[network-admin]{lang="PT-BR"}]{#struct_0_x1539_x1935_x833635442}

[[mdc-admim]{lang="PT-BR"}]{#struct_0_x1539_x1935_x833635443}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2030541778}

[[本功能用来实现]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939514}[隧道与]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的自动关联。]{style="font-family:宋体"}

[[开启本功能后]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1642939515}[，]{style="font-family:宋体"}[VTEP]{lang="PT-BR"}[在所有]{style="font-family:宋体"}[VXLAN]{lang="PT-BR"}[隧道上通过]{style="font-family:宋体"}[VXLAN IS-IS]{lang="PT-BR"}[将本地存在的]{style="font-family:宋体"}[VXLAN]{lang="PT-BR"}[的]{style="font-family:宋体"}[ID]{lang="PT-BR"}[通告给远端]{style="font-family:宋体"}[VTEP]{lang="PT-BR"}[。远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[将其与本地的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[进行比较，如果存在相同的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，则将该]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[与接收该信息的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道关联。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1675406062}

[[\# ]{lang="PT-BR"}]{#struct_0_x1539_x1935_x1642939516}[开启]{style="font-family:宋体"}[VXLAN IS-IS]{lang="PT-BR"}[的]{style="font-family:宋体"}[VXLAN]{lang="PT-BR"}[隧道自动协商功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1539_x1935_x1642939510}

[\[Sysname\] vxlan-isis]{lang="PT-BR"}

[\[Sysname-vxlan-isis\] negotiate-vni enable]{lang="PT-BR"}
:::

::: {#-1617549404 .myid}
[]{#_Toc404798699}[]{#struct_0_x1539_x1935_1272121535}[]{#_Toc393879003}[]{#_Toc383786763}

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis ded-priority**

------------------------------------------------------------------------

[**[overlay isis]{lang="EN-US"}[ ded-priority]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1642939511}[命令用来配置]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[DED]{lang="EN-US"}[（]{style="font-family:宋体"}[Designated Edge Device]{lang="EN-US"}[，指定边缘设备）优先级。]{style="font-family:宋体"}

[**[undo overlay isis]{lang="EN-US"}[ ded-priority]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1642939512}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_109322121}

[**[overlay isis]{lang="EN-US"}[ ded-priority]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1642939506}

[**[undo overlay isis ded-priority]{lang="EN-US"}**]{#struct_0_x1539_x1935_2078756125}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1642939507}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1539_x1935_512672184}[接口的]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_313375622}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x240901244}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/NVE]{lang="EN-US"}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_313375621}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_313375620}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_313375619}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_2097750911}

[*[value]{lang="EN-US"}*]{#struct_0_x1539_x1935_1507179398}[：]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1507179397}

[[每个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_917454132}[隧道两端的]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[设备通过交互]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文选举出一个]{style="font-family:宋体"}[DED]{lang="EN-US"}[。选举出的]{style="font-family:宋体"}[DED]{lang="EN-US"}[周期性发布]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文来进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步。]{style="font-family:宋体"}

[[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_1507179396}[优先级数值高的设备被选为]{style="font-family:宋体"}[DED]{lang="EN-US"}[；如果两台设备的]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级相同，则]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址较大的设备会被选中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1507179395}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_917585204}[配置]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[101]{lang="EN-US"}[的]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1507179402}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] overlay isis ded-priority 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1507179401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1539_x1935_1507179400}**[vxlan]{lang="EN-US"}[ isis tunnel]{lang="EN-US"}**
:::

::: {#2071266219 .myid}
[]{#_Toc404798700}[]{#struct_0_x1539_x1935_1507179399}[]{#_Toc393879004}[]{#_Toc383786764}[]{#_Toc371583404}

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer csnp**

------------------------------------------------------------------------

[**[overlay isis timer csnp]{lang="EN-US"}**]{#struct_0_x1539_x1935_1507179406}[命令用来配置]{style="font-family:宋体"}[DED]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo overlay isis timer csnp]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1421132483}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1507179405}

[**[overlay isis timer csnp]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1421066947}

[**[undo overlay isis timer csnp]{lang="EN-US"}**]{#struct_0_x1539_x1935_x831472762}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472763}

[[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_192859087}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472765}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_192728015}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/NVE]{lang="EN-US"}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472758}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_192400332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x831472760}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1539_x1935_x831472761}[：]{style="font-family:宋体"}[DED]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_192990159}

[[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472754}[使用]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文来进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步。因此，只有在被选举为]{style="font-family:宋体"}[DED]{lang="EN-US"}[的设备上进行该项配置才有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_192662476}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x831472755}[配置]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[101]{lang="EN-US"}[上]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的发送时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776826}

[\[Sysname\] interface  tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] overlay isis timer csnp 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x746750404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1640776827}**[vxlan]{lang="EN-US"}[ isis tunnel]{lang="EN-US"}**
:::

::: {#-485374831 .myid}
[]{#_Toc404798701}[]{#struct_0_x1539_x1935_x1640776828}[]{#_Toc393879005}[]{#_Toc383786765}[]{#_Toc371583405}

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer hello**

------------------------------------------------------------------------

[**[overlay isis timer hello]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1640776829}[命令用来配置]{style="font-family:
宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[**[undo overlay isis timer hello]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1640776822}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1222618064}

[**[overlay isis]{lang="EN-US"}[ timer hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776823}

[**[undo overlay isis timer hello]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1640776824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640776825}

[[VXLAN IS-IS Hello]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776818}[报文的发送时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1553253922}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1640776819}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/NVE]{lang="EN-US"}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_315538310}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_315538309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1686486630}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_315538307}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1539_x1935_1686486616}[：]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_315538314}

[[发送时间间隔越短，网络收敛越快，但也需要占用更多的系统资源。因此，需要根据实际情况合理配置]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}]{#struct_0_x1539_x1935_315538313}[报文的发送时间间隔。]{style="font-family:宋体"}

[[DED]{lang="EN-US"}]{#struct_0_x1539_x1935_315538312}[发送]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文的时间间隔是本命令设置的时间间隔的]{style="font-family:宋体"}[1/3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_315538311}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x652165538}[配置]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[101]{lang="EN-US"}[上]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_315538317}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] overlay isis timer hello 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x652165544}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1539_x1935_861121274}**[vxlan]{lang="EN-US"}[ isis tunnel]{lang="EN-US"}**
:::

::: {#1604871063 .myid}
[]{#_Toc404798702}[]{#struct_0_x1539_x1935_1900329862}[]{#_Toc393879006}[]{#_Toc383786766}

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer holding-multiplier**

------------------------------------------------------------------------

[**[overlay isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_x1539_x1935_1900329861}[命令用来配置]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文失效数目。]{style="font-family:宋体"}

[**[undo overlay isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_x1539_x1935_1900329860}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1900329859}

[**[overlay isis timer holding-multiplier]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1539_x1935_1300905341}

[**[undo overlay isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_x1539_x1935_1900329866}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1300184446}

[[VXLAN IS-IS Hello]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329865}[报文失效数目为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1300118910}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329864}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/NVE]{lang="EN-US"}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1900329863}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1900329870}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1300315519}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1900329869}

[*[value]{lang="EN-US"}*]{#struct_0_x1539_x1935_x438322298}[：]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文失效数目，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x438322299}

[[当前]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322300}[可以将邻接关系保持时间（即]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文失效数目与]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文发送时间间隔的乘积）通过]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文通知远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[。如果远端]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[在邻接关系保持时间内没有收到来自当前]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[的]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文，将宣告邻接关系失效。通过设置]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文失效数目和]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔，可以调整邻接关系保持时间。]{style="font-family:宋体"}

[[需要注意的是，邻接关系保持时间最大不能超过]{style="font-family:宋体"}[65535]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322301}[秒，超过]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒时，算作]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_411880296}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322295}[配置]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[101]{lang="EN-US"}[上]{style="font-family:宋体"}[VXLAN IS-IS Hello]{lang="EN-US"}[报文失效数目为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x438322296}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] overlay isis timer holding-multiplier 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1926837391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[overlay ]{lang="EN-US"}[isis timer hello]{lang="EN-US"}**]{#struct_0_x1539_x1935_x438322290}
:::

::: {#400420546 .myid}
[]{#_Toc404798703}[]{#struct_0_x1539_x1935_x438322291}[]{#_Toc393879007}[]{#_Toc383786767}[]{#_Toc371583407}

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer lsp**

------------------------------------------------------------------------

[**[overlay isis timer lsp]{lang="EN-US"}**]{#struct_0_x1539_x1935_1517992838}[命令用来配置]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[在接口上发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔以及一次可以最多发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的数目。]{style="font-family:宋体"}

[**[undo overlay isis timer lsp]{lang="EN-US"}**]{#struct_0_x1539_x1935_x2099897656}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1517992837}

[**[overlay isis timer lsp]{lang="EN-US"}**[ ]{lang="EN-US"}*[time ]{lang="EN-US"}*[\[ **count** *count* \]]{lang="EN-US"}]{#struct_0_x1539_x1935_x2099569976}

[**[undo overlay ]{lang="EN-US"}[isis timer lsp]{lang="EN-US"}**]{#struct_0_x1539_x1935_1517992836}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2099504440}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_1517992835}[的最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2099701048}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1517992842}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/NVE]{lang="EN-US"}[模式]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1517992841}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x2099438901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1517992840}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2099373365}

[*[time]{lang="EN-US"}*]{#struct_0_x1539_x1935_1517992839}[：发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，为]{style="font-family:宋体"}[100]{lang="EN-US"}[的整数倍，单位为毫秒。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**[ ]{lang="EN-US"}*[count]{lang="EN-US"}*]{#struct_0_x1539_x1935_1517992846}[：一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2099504437}

[[当]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1539_x1935_1517992845}[的内容发生变化时，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[将把发生变化的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩散出去。用户可以通过本命令对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送时间间隔进行调节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2099701045}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659322}[配置发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659323}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] overlay isis timer lsp 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_412031755}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1539_x1935_2097195550}**[vxlan]{lang="EN-US"}[ isis ]{lang="EN-US"}[brief]{lang="EN-US"}**
:::

::::: {#668066240 .myid}
[]{#_Toc404798704}[]{#struct_0_x1539_x1935_x820659324}[]{#_Toc393879008}

**VXLAN \-- VXLAN IS-IS配置命令 \-- reserved vxlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x820659318}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x820659319}
:::

[ ]{lang="EN-US"}

[**[reserved vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_x820659320}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议使用的保留]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo reserved vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_411835147}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x820659321}

[**[reserved vxlan]{lang="EN-US"}**[ *vxlan-id*]{lang="EN-US"}]{#struct_0_x1539_x1935_411900683}

[**[undo reserved vxlan]{lang="EN-US"}**]{#struct_0_x1539_x1935_x820659315}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_412162828}

[[没有指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963386}[协议使用的保留]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x118132547}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1629963387}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1447951394}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1044666867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1629963389}

[*[vxlan-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x1684216488}[：保留]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1629963382}

[[保留]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_1851235921}[用来接收和发送]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[报文。属于同一个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[上只有配置了相同的保留]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[之间才能够正常收发]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[只能在系统视图下配置一个全局保留]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963383}[，该]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[不能与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下创建的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x877647434}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1629963384}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议使用的保留]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VXLAN 10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_x1280931961}

[\[Sysname\] reserved vxlan 10000]{lang="EN-US"}
:::::

::: {#1205560370 .myid}
[]{#_Toc404798705}[]{#struct_0_x1539_x1935_x1629963385}[]{#_Toc393879009}

**VXLAN \-- VXLAN IS-IS配置命令 \-- reset vxlan isis**

------------------------------------------------------------------------

[**[reset vxlan isis]{lang="EN-US"}**]{#struct_0_x1539_x1935_285151980}[命令用来清除]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程下所有的动态数据，包括]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的邻居、本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VXLAN ID]{lang="EN-US"}[、链路状态数据库等信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1629963378}

[**[reset vxlan isis]{lang="EN-US"}**]{#struct_0_x1539_x1935_1044470259}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x971291827}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1629963379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_326351750}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x136021012}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_326351749}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2092336155}

[[\# ]{lang="PT-BR"}]{#struct_0_x1539_x1935_326351748}[清除]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程下所有的动态数据。]{style="font-family:宋体"}

[[\<Sysname\> reset vxlan isis]{lang="EN-US"}]{#struct_0_x1539_x1935_326351747}
:::

::: {#490996559 .myid}
[]{#_Toc404798706}[]{#struct_0_x1539_x1935_x2092336149}[]{#_Toc393879010}

**VXLAN \-- VXLAN IS-IS配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

[**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1539_x1935_326351754}[命令用来配置当前]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间。]{style="font-family:宋体"}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1539_x1935_x136021016}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1654952685}

[**[timer lsp-max-age ]{lang="EN-US"}***[second]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_x1539_x1935_326351753}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1539_x1935_x136021009}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_326351752}

[[当前]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_x136021010}[生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_326351751}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x136021011}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1654756077}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_326351758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x136021020}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_326351757}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1539_x1935_x136021013}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间，取值范围是]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1902492550}

[[每个]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_438516267}[都有一个最大生存时间，随着时间的推移]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的生存时间将逐渐减小，当]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的生存时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[将清除该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。用户可根据网络的实际情况调整]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1902492549}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1902492548}[配置生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[分钟，即]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1902492547}

[\[Sysname\] vxlan-isis]{lang="EN-US"}

[\[Sysname-vxlan-isis\] timer lsp-max-age 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_438843948}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan isis brief]{lang="EN-US"}**]{#struct_0_x1539_x1935_1902492554}
:::

::: {#-1091829735 .myid}
[]{#_Toc404798707}[]{#struct_0_x1539_x1935_1902492553}[]{#_Toc393879011}[]{#_Toc383786772}

**VXLAN \-- VXLAN IS-IS配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

[**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1539_x1935_438581803}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期。]{style="font-family:宋体"}

[**[undo timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1539_x1935_1902492552}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1902492551}

[**[timer lsp-refresh ]{lang="EN-US"}***[second]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_x1539_x1935_438450731}

[**[undo timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1539_x1935_1902492558}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1902492557}

[[LSP]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159610}[刷新周期为]{style="font-family:宋体"}[900]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x224980402}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159611}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x224914866}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x224849330}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x436159613}

[*[second]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_x1539_x1935_x224783794}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x436159606}

[**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1539_x1935_x225111475}[命令配置的时间必须小于]{style="font-family:宋体"}**[timer lsp-max-age]{lang="EN-US"}**[命令配置的时间，以保证在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失效前进行刷新。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x454068885}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159608}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期为]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x436159602}

[\[Sysname\] vxlan-isis]{lang="EN-US"}

[\[Sysname-vxlan-isis\] timer lsp-refresh 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x224849331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan isis brief]{lang="EN-US"}**]{#struct_0_x1539_x1935_x436159603}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1539_x1935_x224783795}
:::

::: {#1347731002 .myid}
[]{#_Toc404798708}[]{#struct_0_x1539_x1935_1520155526}[]{#_Toc393879012}[]{#_Toc383786774}

**VXLAN \-- VXLAN IS-IS配置命令 \-- virtual-system**

------------------------------------------------------------------------

[**[virtual-system]{lang="EN-US"}**]{#struct_0_x1539_x1935_1520155525}[命令用来创建一个]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[虚拟系统。]{style="font-family:宋体"}

[**[undo virtual-system]{lang="EN-US"}**]{#struct_0_x1539_x1935_656725489}[命令用来删除一个已经存在的]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[虚拟系统。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1520155524}

[**[virtual-system]{lang="EN-US"}**[ *system-id*]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155523}

[**[undo virtual-system ]{lang="EN-US"}***[system-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1520155530}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1520155529}

[[不存在任何]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_655939057}[虚拟系统。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1520155528}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_656004593}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x313361078}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155527}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1520155534}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_656791024}

[*[system-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1520155533}[：虚拟系统的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用来标识虚拟系统，格式为]{style="font-family:宋体"}[XXXX.XXXX.XXXX]{lang="EN-US"}[，]{style="font-family:宋体"}[X]{lang="EN-US"}[表示十六进制数字。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x818496634}

[[当本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1539_x1935_x1600406572}[地址数超过系统的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分片集所能携带的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数时，可以配置]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[虚拟系统来扩展]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片数量，以增加系统所能发布的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数量。]{style="font-family:宋体"}

[[创建虚拟系统前，系统最多可以发送约]{style="font-family:宋体"}[55]{lang="EN-US"}]{#struct_0_x1539_x1935_1365172374}[×]{style="font-family:宋体"}[2^10^]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息，每创建一个虚拟系统，最多可以多发送]{style="font-family:宋体"}[55]{lang="EN-US"}[×]{style="font-family:宋体"}[2^10^]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。用户可以根据本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的规模，来决定创建的虚拟系统的个数。]{style="font-family:宋体"}

[[创建虚拟系统时，用户需要保证所配置的虚拟系统的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496635}[在网络中是唯一的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1600341036}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496636}[创建一个系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0001.0001.0001]{lang="EN-US"}[的虚拟系统。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496637}

[\[Sysname\] vxlan-isis]{lang="EN-US"}

[\[Sysname-vxlan-isis\] virtual-system 0001.0001.0001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1600209964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vxlan isis brief]{lang="EN-US"}**]{#struct_0_x1539_x1935_x818496630}
:::

::: {#1415077958 .myid}
[]{#_Toc404798709}[]{#struct_0_x1539_x1935_x1600144428}[]{#_Toc393879013}[]{#_Toc383786779}[]{#_Toc371583429}

**VXLAN \-- VXLAN IS-IS配置命令 \-- vxlan-isis**

------------------------------------------------------------------------

[**[vxlan-isis]{lang="EN-US"}**]{#struct_0_x1539_x1935_x818496631}[命令用来]{style="font-family:宋体"}[创建]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程，并进入]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo vxlan-isis]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1600078892}[命令用来删除]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程，并清除]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程下的配置数据。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x818496632}

[**[vxlan-isis]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1600013356}

[**[undo vxlan-isis]{lang="EN-US"}**]{#struct_0_x1539_x1935_x818496633}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1599947820}

[[未创建]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_x1539_x1935_x818496626}[进程。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1600275499}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x818496627}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1600209963}

[[network-admin]{lang="PT-BR"}]{#struct_0_x1539_x1935_x1627800698}

[[mdc-admim]{lang="PT-BR"}]{#struct_0_x1539_x1935_1607476734}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1627800699}

[[\# ]{lang="PT-BR"}]{#struct_0_x1539_x1935_x1121406621}[创建]{style="font-family:宋体"}[VXLAN IS-IS]{lang="PT-BR"}[进程]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并进入]{style="font-family:宋体"}[VXLAN IS-IS]{lang="PT-BR"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1539_x1935_x1627800700}

[\[Sysname\] vxlan-isis]{lang="PT-BR"}

[\[Sysname-vxlan-isis\]]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1963117271}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1539_x1935_1486980077}**[vxlan]{lang="EN-US"}[ isis ]{lang="EN-US"}[brief]{lang="EN-US"}**[]{#_Toc382494925}[]{#_Toc382494940}
:::

::::: {#1742433432 .myid}
[]{#_Toc404798711}[]{#struct_0_x1539_x1935_1560422567}[]{#_Toc375835896}[]{#_Toc290542288}

**VXLAN \-- VXLAN IP网关配置命令 \-- bandwidth**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x1627800696}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x1168460788}
:::

[ ]{lang="EN-US"}

[**[bandwidth]{lang="DA"}**]{#struct_0_x1539_x1935_x1627800697}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="DA"}**]{#struct_0_x1539_x1935_397623153}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1627800690}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x1539_x1935_1963707094}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1627800691}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x765176261}

[[接口的期望带宽＝接口的最大速率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x1539_x1935_x1152394144}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514438}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x751877835}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1165607634}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_328514437}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x751877820}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514436}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x1539_x1935_x751877821}[：]{style="font-family:宋体"}[接口的期望带宽]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514435}

[[接口的期望带宽会对下列内容有影响：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x751877822}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBQ]{lang="EN-US"}]{#struct_0_x1539_x1935_1166066385}[队列带宽。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[链路开销值。具体介绍请参见"三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x1539_x1935_328514442}[路由配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1969111359}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_328514441}[配置接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的]{style="font-family:宋体"}[期望带宽]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_328514440}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] bandwidth 10000]{lang="EN-US"}
:::::

::: {#1948332219 .myid}
[]{#_Toc404798712}[]{#struct_0_x1539_x1935_1969111357}[]{#_Toc375835897}[]{#_Toc290542290}

**VXLAN \-- VXLAN IP网关配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x1539_x1935_328514439}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x751877834}

[**[default]{lang="EN-US"}**]{#struct_0_x1539_x1935_1165673170}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_328514446}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1969111363}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1853343818}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_328514445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1969111362}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1499946610}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1706836157}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x1539_x1935_1499946611}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1706770621}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1499946608}[将接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1499946609}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] default]{lang="EN-US"}

[This command will restore the default settings. Continue? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#437833442 .myid}
[]{#_Toc290542294}[]{#_Toc263067821}[]{#_Toc207010297}[]{#_Toc207010030}[]{#_Toc139515319}[]{#_Toc137103152}[]{#_Toc404798713}[]{#struct_0_x1539_x1935_1706246332}[]{#_Toc375835898}

**VXLAN \-- VXLAN IP网关配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1539_x1935_1499946606}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1539_x1935_1706967228}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x420839275}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x1539_x1935_1499946607}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x1539_x1935_1706901692}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x799041692}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_1499946604}["，例如：]{style="font-family:宋体"}[Vsi-interface100 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1707098300}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1499946605}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1499946602}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1706705084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1499946603}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1706639548}

[*[text]{lang="EN-US"}*]{#struct_0_x1539_x1935_x838705550}[：接口的描述字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1107453012}

[[当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x838705549}

[[本命令仅用于标识某接口，并无特别的功能。使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1106994261}[等命令可以看到设置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x654798480}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x838705552}[配置接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[gateway for VXLAN 10]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1107584084}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] description gateway for VXLAN 10]{lang="EN-US"}
:::

::: {#429599933 .myid}
[]{#_Toc404798714}[]{#struct_0_x1539_x1935_x838705551}[]{#_Toc375835899}

**VXLAN \-- VXLAN IP网关配置命令 \-- display interface vsi-interface**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1107518548}**[vsi-interface]{lang="DE"}**[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x191796501}

[**[display interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_x1539_x1935_x838705554}**[vsi-interface]{lang="DE"}**[ \[ *vsi-interface-id* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1107190868}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x838705553}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1107649620}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x838705556}

[[network-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x1107321940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x153249948}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1539_x1935_x838705555}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1107256404}

[*[vsi-nterface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_964737130}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x1539_x1935_x838705558}[：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1106928724}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x1539_x1935_x838705557}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1117609586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型（]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1539_x1935_955200808}**[vsi-interface]{lang="DE"}**[），将显示设备支持的所有接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型，不指定接口编号（]{lang="EN-US" style="font-family:宋体"}*[vsi-interface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1117609587}[）]{lang="EN-US" style="font-family:
宋体"}[，则显示所有]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[虚]{style="font-family:宋体"}[接口的信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则显示指定]{style="font-family:宋体"}]{#struct_0_x1539_x1935_955266344}[VSI]{lang="EN-US"}[虚接口的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1117609584}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_955331880}[显示接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_x1539_x1935_1117609582}[display interface vsi-interface 100]{lang="NL-BE"}

[Vsi-interface100]{lang="IT"}

[Current state: UP]{lang="IT"}

[Line protocol state: UP]{lang="IT"}

[Description: Vsi-interface100 Interface]{lang="IT"}

[Bandwidth: 1000000kbps]{lang="IT"}

[Maximum Transmit Unit: 1500]{lang="IT"}

[Internet Address is 10.1.1.1/24 Primary]{lang="IT"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102]{lang="IT"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102]{lang="IT"}

[Physical: Unknown, baudrate: 1000000 kbps]{lang="IT"}

[Last clearing of counters: Never]{lang="IT"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="IT"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="IT"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="IT"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="IT"}

[[表1-22 ]{lang="EN-US"}[display interface vsi-interface]{lang="EN-US"}]{#struct_0_x1539_x1935_954938664}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1398677436}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1117609580}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1117609581}

[[Vsi-interface100]{lang="NL-BE"}]{#struct_0_x1539_x1935_1117609579}

[[接口]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1221042574}[VSI-interface100]{lang="NL-BE"}[的相关信息]{style="font-family:宋体"}

[[C]{lang="NL-BE"}[urrent state]{lang="EN-US"}]{#struct_0_x1539_x1935_x1221042576}

[[接口的物理状态和管理状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1221042575}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administr]{lang="EN-US"}]{#struct_0_x1539_x1935_x1221042577}[a]{lang="EN-US"}[t]{lang="EN-US"}[ive]{lang="EN-US"}[ly DOWN]{lang="EN-US"}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1221042580}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1221042582}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x1539_x1935_x1221042581}

[[接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x2030346638}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1539_x1935_x2030346640}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_x1539_x1935_x2030346642}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1539_x1935_x2030346641}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1539_x1935_x2030346643}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x2030346646}

[[Bandwidth]{lang="NL-BE"}]{#struct_0_x1539_x1935_x74031502}

[[接口的期望带宽，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x1539_x1935_x74031501}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x1539_x1935_x74031503}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x74031506}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x1539_x1935_1119772267}

[[Tunnel]{lang="NO-BOK"}]{#struct_0_x1539_x1935_x1218879885}[接口的]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址。如果没有为]{style="font-family:宋体"}[Tunnel]{lang="NO-BOK"}[接口配置]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址，则该字段显示为]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}[，表示不能处理]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[报文]{style="font-family:宋体"}

[[Primary]{lang="EN-US"}]{#struct_0_x1539_x1935_x1218879888}[表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_x1539_x1935_x1218879890}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1218879892}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_x1539_x1935_x1218879891}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IPv6]{lang="EN-US"}]{#struct_0_x1539_x1935_x1218879894}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x1539_x1935_x2028183950}

[[接口的物理类型，取值为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_x1539_x1935_x2028183949}

[[baudrate]{lang="IT"}]{#struct_0_x1539_x1935_x2028183951}

[[接口的波特率，单位为]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x2028183954}[kbps]{lang="IT"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x1539_x1935_x2028183956}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x2028183955}[命令清除接口下的统计信息的时间（如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_x1539_x1935_x2028183957}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1539_x1935_x71868814}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的包数]{style="font-family:宋体"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_x1539_x1935_x71868813}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1539_x1935_x71868815}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的包数]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_x1539_x1935_x71868818}

[[总计输入的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_x1539_x1935_x71868820}[总计输入的字节，总计丢弃的输入报文数]{style="font-family:宋体"}

[[Output: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_x1539_x1935_x71868822}

[[总计输出的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_x1539_x1935_x71868821}[总计输出的字节，总计丢弃的输出报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1495621234}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface vsi-interface brief]{lang="EN-US"}]{#struct_0_x1539_x1935_1995695053}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Vsi100               DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_239121975}[显示接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的概要信息，包括用户配置的全部描述信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface vsi-interface 100 brief description]{lang="EN-US"}]{#struct_0_x1539_x1935_1495621232}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Vsi100               UP    UP      1.1.1.1         VSI-interface100]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1996088269}[显示当前状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface brief down]{lang="EN-US"}]{#struct_0_x1539_x1935_1495621230}

[Brief information of interface(s) under route mode:]{lang="NL-BE"}

[Link: ADM - administratively down; Stby - standby]{lang="NL-BE"}

[Interface            Link Cause]{lang="NL-BE"}

[Vsi100]{lang="EN-US"}[               DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[Vsi200]{lang="EN-US"}[               DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[]{#struct_0_x1539_x1935_1995957197}[[表1-23 ]{lang="EN-US"}[display interface vsi-interface brief]{lang="EN-US"}]{#_Ref129008332}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_1673799228}[[字段]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1495621228}

[[描述]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1495621229}

[[Brief information of interface(s) under route mode:]{lang="EN-US"}]{#struct_0_x1539_x1935_x843030926}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_x1539_x1935_x843030925}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x1539_x1935_x843030930}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1539_x1935_x843030929}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1539_x1935_x843030934}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x1539_x1935_1113284210}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x1539_x1935_1113284208}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的网络层协议状态显示是]{style="font-family:宋体"}[UP]{lang="EN-US"}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1539_x1935_1113284206}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1113284204}

[[Link]{lang="EN-US"}]{#struct_0_x1539_x1935_1113284202}

[[接口物理连接状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1113284203}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1225367949}[：表示本链路物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1539_x1935_x1225367952}[：表示本链路物理上]{lang="EN-US" style="font-family:宋体"}[是]{style="font-family:宋体"}[不通的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x1539_x1935_x1225367954}[：表示本链路被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x1539_x1935_x1225367956}[：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1539_x1935_x1225367955}

[[接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1225367957}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1539_x1935_x2034672013}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (s)]{lang="EN-US"}]{#struct_0_x1539_x1935_x2034672016}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1539_x1935_x2034672018}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x1539_x1935_x2034672020}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1539_x1935_x2034672019}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1539_x1935_x2034672021}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x78356877}

[[Cause]{lang="EN-US"}]{#struct_0_x1539_x1935_x78356880}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1539_x1935_x78356882}[的原因，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_x1539_x1935_x78356884}[：表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_x1539_x1935_x78356883}[：表示没有]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[关联该]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[或者]{lang="EN-US" style="font-family:宋体"}[关联该接口]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[没有]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PW.]{lang="EN-US"}

[ ]{lang="NL-BE"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x78356886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_520855544}

::::: {#-1992782108 .myid}
[]{#_Toc404798715}[]{#struct_0_x1539_x1935_x1658653950}[]{#_Toc402961799}

**VXLAN \-- VXLAN IP网关配置命令 \-- distributed-gateway local**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x92570009}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_780599684}
:::

**[ ]{lang="EN-US"}**

[**[distributed-gateway local]{lang="EN-US"}**]{#struct_0_x1539_x1935_925627519}[命令用来配置]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[虚接口为分布式网关接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **distributed-gateway local**]{lang="EN-US"}]{#struct_0_x1539_x1935_x1866662949}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1730861016}

[**[distributed-gateway local]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1718770268}

[**[undo distributed-gateway local]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1313590283}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1326233169}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1548194293}[虚接口不是分布式本地网关接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1117283572}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x581392489}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_347888490}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1389298295}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1989489187}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_523738973}

[[在分布式]{style="font-family:宋体"}[VXLAN IP]{lang="EN-US"}]{#struct_0_x1539_x1935_336999546}[网关组网中，多个网关上的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口需要配置相同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。为了避免]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址冲突，需要在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口上执行本命令，以防止]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口上报地址冲突，导致]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口不可用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_412717360}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1611599783}[配置接口]{style="font-family:宋体"}[Vsi-interface100]{lang="EN-US"}[为分布式网关接口。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_x2128668959}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] distributed-gateway local]{lang="EN-US"}
:::::

::::: {#693979390 .myid}
[]{#_Toc404798716}[]{#struct_0_x1539_x1935_x1124235406}[]{#_Toc402961800}

**VXLAN \-- VXLAN IP网关配置命令 \-- gateway subnet**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 2 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_494051127}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_1523098518}
:::

**[ ]{lang="EN-US"}**

[**[gateway subnet]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1511073608}[命令用来配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[所属的子网网段。]{style="font-family:宋体"}

[**[undo gateway subnet]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1885710388}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2071373442}

[**[gateway subnet ]{lang="EN-US"}**[{ *ip-address wildcard-mask* \| *ipv6-address prefix-length* } ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1339278706}

[**[undo gateway subnet]{lang="EN-US"}**[ { *ip-address wildcard-mask* \| *ipv6-address prefix-length* }]{lang="EN-US"}]{#struct_0_x1539_x1935_1473579468}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1640817941}

[[没有指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1343853282}[所属的子网网段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1976879912}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x1275585909}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_759051577}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x694444947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x2025981804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1255303887}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1539_x1935_x291941878}[：子网网段地址，为点分十进制格式。]{style="font-family:宋体"}

[*[wildcard-mask]{lang="EN-US"}*]{#struct_0_x1539_x1935_x312364566}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码的反码，即将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码取反（]{style="font-family:宋体"}[0]{lang="EN-US"}[变]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[变]{style="font-family:
宋体"}[0]{lang="EN-US"}[）。例如：子网掩码]{style="font-family:宋体"}[255.0.0.0]{lang="EN-US"}[的反码为]{style="font-family:宋体"}[0.255.255.255]{lang="EN-US"}[。其中，反码中的"]{style="font-family:宋体"}[1]{lang="EN-US"}["表示忽略]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址中对应的位，"]{style="font-family:宋体"}[0]{lang="EN-US"}["表示必须保留此位。]{style="font-family:宋体"}

[*[ipv6-address prefix-length]{lang="EN-US"}*]{#struct_0_x1539_x1935_282829998}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及前缀长度。]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x545111912}

[[为了节省分布式]{style="font-family:宋体"}[VXLAN IP]{lang="EN-US"}]{#struct_0_x1539_x1935_x1431141020}[网关设备上的三层接口资源，在网关设备上多个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[可以共用一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口，为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口配置一个主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和多个从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网络）、或多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网络），分别作为不同]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[内虚拟机的网关地址。]{style="font-family:宋体"}

[[多个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x793011312}[共用一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口时，网关设备无法判断从]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口接收到的报文属于哪个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[。为了解决该问题，需要在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图下通过本命令指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[所属的子网网段，通过子网网段判断报文所属的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并在该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内转发报文，从而限制广播报文范围，有效地节省带宽资源。但是每个]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[都有各自的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址子网网段以及网关]{style="font-family:宋体"}[IP]{lang="EN-US"}[，因此需要]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口支持按]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[设置]{style="font-family:宋体"}[Subnet IP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1729843034}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x1539_x1935_310780054}[VSI]{lang="EN-US"}[视图下最多可以配置]{style="font-family:宋体"}[8]{lang="EN-US"}[个子网网段，包括]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1539_x1935_2020612604}[VSI]{lang="EN-US"}[视图下配置子网网段前，必须先为该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[指定网关接口。取消为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[指定网关接口时，会自动删除为该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[指定的子网网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能为指定了相同网关接口的不同]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x814280489}[VSI]{lang="EN-US"}[配置相同的子网网段。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1724067341}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x237620754}[配置名称为]{style="font-family:宋体"}[vxlan]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[所属的子网网段为]{style="font-family:宋体"}[100.0.10.0/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1560288552}

[\[Sysname\] vsi vxlan]{lang="EN-US"}

[\[Sysname-vsi-vxlan\] gateway subnet 100.0.10.0 0.0.0.255]{lang="EN-US"}
:::::

::: {#17596291 .myid}
[]{#struct_0_x1539_x1935_x78356885}[]{#_Toc404798717}[]{#_Toc387305727}[]{#_Toc381105347}

**VXLAN \-- VXLAN IP网关配置命令 \-- gateway vsi-interface**

------------------------------------------------------------------------

[**[gateway vsi-interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_1497783922}[命令用来为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[指定网关接口。]{style="font-family:宋体"}

[**[undo gateway vsi-interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x110101891}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1497783923}

[**[gateway vsi-interface ]{lang="EN-US"}***[vsi-interface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x110167427}

[**[undo gateway vsi-interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_1497783920}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1497783921}

[[没有为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1497783918}[指定网关接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x110495108}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1497783919}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x110560644}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x602353022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1497783916}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x110364036}

[*[vsi-interface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_1497783917}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[网关虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x110429572}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1497783914}[VSI]{lang="EN-US"}[只能指定一个网关接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x110232964}[VSI]{lang="EN-US"}[可以指定相同的网关接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_193456319}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1497783915}[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[指定网关接口为]{style="font-family:宋体"}[Vsi-interface100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_x840868238}

[\[Sysname\] vsi vpna]{lang="EN-US"}

[\[Sysname-vsi-vpna\] gateway vsi-interface 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x652167509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface vsi-interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x302530104}
:::

::: {#-256627221 .myid}
[]{#_Toc404798718}[]{#struct_0_x1539_x1935_x840868237}[]{#_Toc387305728}[]{#_Toc381105348}

**VXLAN \-- VXLAN IP网关配置命令 \-- interface vsi-interface**

------------------------------------------------------------------------

[**[interface vsi-interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x840868240}[命令用来创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口视图。]{style="font-family:宋体"}

[**[undo interface vsi-interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x651643226}[命令用来删除]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[虚接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1344312567}

[**[interface vsi-interface ]{lang="EN-US"}***[vsi-interface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x840868239}

[**[undo interface vsi-interface ]{lang="EN-US"}***[vsi-interface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x652233045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x840868242}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x651512154}[虚接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1340868918}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x840868241}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x840868244}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x651905370}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x840868246}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x651774298}

[*[vsi-nterface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x840868245}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x651970906}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1115446898}[创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口]{style="font-family:宋体"}[100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_x1539_x1935_1115446899}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1493691870}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gateway vsi-interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x198515767}
:::

::: {#988247972 .myid}
[]{#_Toc404798719}[]{#struct_0_x1539_x1935_1115446896}[]{#_Toc375835902}

**VXLAN \-- VXLAN IP网关配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x1539_x1935_1115446897}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1539_x1935_1492774366}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x245880130}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x1539_x1935_1115446894}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1539_x1935_1492839902}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1012743730}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1115446895}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1492905438}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_1115446892}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1492970974}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1115446893}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1493036510}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1115446890}

[*[size]{lang="EN-US"}*]{#struct_0_x1539_x1935_1115446891}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[46]{lang="EN-US"}[～]{style="font-family:宋体"}[1560]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1493167582}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1223205262}[配置接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x1617902668}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] mtu 1430]{lang="EN-US"}
:::

::: {#877252436 .myid}
[]{#_Toc290542370}[]{#_Toc404798720}[]{#struct_0_x1539_x1935_x1223205261}[]{#_Toc375835903}[]{#_Toc290542313}[]{#_Toc263067840}

**VXLAN \-- VXLAN IP网关配置命令 \-- reset counters interface vsi-interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="DE"}**]{#struct_0_x1539_x1935_1110980687}[命令用来清除接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x615382010}

[**[reset counters interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_x1539_x1935_x1223205264}**[vsi-interface]{lang="DE"}**[ \[ *vsi-interface-id* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1223205263}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x1223205266}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1223205265}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x1214618141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_1204310174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1223205268}

[*[vsi-nterface-id]{lang="EN-US"}*]{#struct_0_x1539_x1935_x98872894}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1223205267}

[[在某些情况下]{style="font-family:宋体"}]{#struct_0_x1539_x1935_1917549741}[，]{style="font-family:宋体"}[需要统计一定时间内某接口的流量]{style="font-family:宋体"}[，]{style="font-family:宋体"}[这就需要在统计开始前清除该接口原有的统计信息]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型（]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1539_x1935_1061696699}**[vsi-interface]{lang="DE"}**[），则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1539_x1935_x1223205270}[，]{lang="EN-US" style="font-family:宋体"}[不指定接口编号（]{lang="EN-US" style="font-family:
宋体"}*[vsi-interface-id]{lang="EN-US"}*[）]{lang="EN-US" style="font-family:宋体"}[，则清除所有]{lang="EN-US" style="font-family:
宋体"}[VSI]{lang="EN-US"}[虚]{style="font-family:宋体"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则清除指定]{style="font-family:宋体"}]{#struct_0_x1539_x1935_x455037718}[VSI]{lang="EN-US"}[虚接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1223205269}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1467211047}[清除接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface vsi-interface 100]{lang="EN-US"}]{#struct_0_x1539_x1935_x2032509326}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_66696376}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface]{lang="EN-US"}**]{#struct_0_x1539_x1935_x2032509325}
:::

::: {#-716074350 .myid}
[]{#_Toc404798721}[]{#struct_0_x1539_x1935_469980903}[]{#_Toc375835904}

**VXLAN \-- VXLAN IP网关配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1539_x1935_x2032509328}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x1539_x1935_1585726150}[命令用来开启当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x2032509327}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1539_x1935_1632780317}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1539_x1935_x2032509330}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1229561326}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x2032509329}[虚接口均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1143157205}

[[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x2032509332}[虚接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1902606556}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x324245107}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_x2032509331}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1499322029}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_x795157333}[关闭接口]{style="font-family:宋体"}[VSI-interface100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_x2032509333}

[\[Sysname\] interface vsi-interface 100]{lang="EN-US"}

[\[Sysname-Vsi-interface100\] shutdown]{lang="EN-US"}
:::

::::: {#-1082119549 .myid}
[]{#_Toc404798722}[]{#struct_0_x1539_x1935_1339886028}[]{#_Toc402961801}[]{#_Toc390866207}[]{#_GoBack}

**VXLAN \-- VXLAN IP网关配置命令 \-- vxlan ip-forwarding**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VXLAN命令.files/image001.png){#图片 1 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1539_x1935_x1388997327}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1539_x1935_x1439111991}
:::

[ ]{lang="EN-US"}

[**[vxlan ip-forwarding]{lang="EN-US"}**]{#struct_0_x1539_x1935_x215785533}[命令用来配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[采用三层转发模式。]{style="font-family:宋体"}

[**[undo vxlan ip-forwarding]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_x1539_x1935_x59166572}[命令用来配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[采用二层转发模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_487031861}

[**[vxlan ip-forwarding]{lang="EN-US"}**]{#struct_0_x1539_x1935_x1090946292}

[**[undo vxlan ip-forwarding]{lang="EN-US"}**]{#struct_0_x1539_x1935_x433543469}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_449140497}

[[VXLAN]{lang="EN-US"}]{#struct_0_x1539_x1935_x2029250915}[采用三层转发模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x1454295889}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1539_x1935_177086614}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_789508004}

[[network-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_853229355}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1539_x1935_234005379}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_1298449075}

[[三层转发模式是指]{style="font-family:宋体"}[VTEP]{lang="EN-US"}]{#struct_0_x1539_x1935_1477328563}[设备通过查找]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网络）或]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项（]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网络）对流量进行转发。二层转发模式是指]{style="font-family:宋体"}[VTEP]{lang="EN-US"}[通过查找]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项对流量进行转发。]{style="font-family:宋体"}

[[采用分布式]{style="font-family:宋体"}[VXLAN IP]{lang="EN-US"}]{#struct_0_x1539_x1935_2044563536}[网关组网方案时，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[需要采用三层转发模式；其他情况下，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[采用二层转发模式。]{style="font-family:宋体"}

[[需要注意的是，修改本配置前，必须先删除设备上的所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x1539_x1935_x213204262}[、]{style="font-family:宋体"}[VSI]{lang="EN-US"}[虚接口和]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道，否则配置将失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1539_x1935_x684022687}

[[\# ]{lang="EN-US"}]{#struct_0_x1539_x1935_1339513543}[配置]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[采用三层转发模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1539_x1935_1928104207}

[\[Sysname\] vxlan ip-forwarding]{lang="EN-US"}
:::::
