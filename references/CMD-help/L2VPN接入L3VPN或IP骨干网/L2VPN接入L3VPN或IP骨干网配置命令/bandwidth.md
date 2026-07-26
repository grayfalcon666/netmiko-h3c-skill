::::: {#1742433432 .myid}
[]{#_Toc290542294}[]{#_Toc263067821}[]{#_Toc207010297}[]{#_Toc207010030}[]{#_Toc139515319}[]{#_Toc137103152}[]{#_Toc404791629}[]{#struct_0_16632_16529_1090796635}[]{#_Toc290542288}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- bandwidth**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](L2VPN接入L3VPN或IP骨干网命令.files/image001.png){#图片 1 width="63" height="25"}]{lang="EN-US"}]{#struct_0_16632_16529_x985972347}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_16632_16529_494230549}
:::

[ ]{lang="EN-US"}

[**[bandwidth]{lang="DA"}**]{#struct_0_16632_16529_x1369047066}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="DA"}**]{#struct_0_16632_16529_907354562}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_930590811}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_16632_16529_x1563957324}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_16632_16529_1985111364}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16632_16529_93907952}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_16632_16529_2113382312}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_1994264266}

[[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_1778330461}[接口视图]{style="font-family:宋体"}[/L2VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_x100453077}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_795638988}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_1696283503}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1418986723}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_16632_16529_x1369112602}[：]{style="font-family:宋体"}[接口的期望带宽]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16632_16529_2027303641}

[[接口的期望带宽会对下列内容有影响：]{style="font-family:宋体"}]{#struct_0_16632_16529_x790788983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[CBQ]{lang="EN-US"}]{#struct_0_16632_16529_x1149664905}[队列带宽。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[链路开销值。具体介绍请参见"三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_16632_16529_131006105}[路由配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_1973260429}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_2009937223}[配置接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[的]{style="font-family:宋体"}[期望带宽]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_1612608495}

[\[Sysname\] interface ve-l2vpn 100]{lang="EN-US"}

[\[Sysname-VE-L2VPN100\] bandwidth 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_189311427}[配置接口]{style="font-family:宋体"}[VE-L3VPN100]{lang="EN-US"}[的]{style="font-family:宋体"}[期望带宽]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x1781388547}

[\[Sysname\] interface ve-l3vpn 100]{lang="EN-US"}

[\[Sysname-VE-L3VPN100\] bandwidth 10000]{lang="EN-US"}
:::::

::: {#1948332219 .myid}
[]{#_Toc404791630}[]{#struct_0_16632_16529_x1855513001}[]{#_Toc290542290}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_16632_16529_x1369571353}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1457142505}

[**[default]{lang="EN-US"}**]{#struct_0_16632_16529_x2110803203}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_1284452785}

[[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_x346059328}[接口视图]{style="font-family:宋体"}[/L2VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_853617119}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_401717808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_x1606839135}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16632_16529_1188146134}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_16632_16529_x1896980344}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_16632_16529_168758070}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_x338200882}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x1369636889}[将接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x1874187926}

[\[Sysname\] interface ve-l2vpn 100]{lang="EN-US"}

[\[Sysname-VE-L2VPN100\] default]{lang="EN-US"}

[This command will restore the default settings. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_132421219}[将接口]{style="font-family:宋体"}[VE-L3VPN100]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x1443553969}

[\[Sysname\] interface ve-l3vpn 100]{lang="EN-US"}

[\[Sysname-VE-L3VPN100\] default]{lang="EN-US"}

[This command will restore the default settings. Continue? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404791631}[]{#struct_0_16632_16529_841278441}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_16632_16529_x2013662954}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_16632_16529_1203100613}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_746005452}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_16632_16529_x2065625936}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_16632_16529_1600920044}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1369702425}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_16632_16529_1760725169}["，例如：]{style="font-family:宋体"}[VE-L2VPN100 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_1064016491}

[[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_x900722843}[接口视图]{style="font-family:宋体"}[/L2VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_1347553355}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_x1027682667}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_x1131904837}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1269342308}

[*[text]{lang="EN-US"}*]{#struct_0_16632_16529_x1282365644}[：接口的描述字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16632_16529_546097727}

[[当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。]{style="font-family:宋体"}]{#struct_0_16632_16529_x134581767}

[[本命令仅用于标识某接口，并无特别的功能。使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_16632_16529_776957403}[等命令可以看到设置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1832645589}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x1369767961}[配置接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[L2VPN-Terminate]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x952261028}

[\[Sysname\] interface ve-l2vpn 100]{lang="EN-US"}

[\[Sysname-VE-L2VPN100\] description L2VPN-Terminate]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x1985381046}[配置接口]{style="font-family:宋体"}[VE-L3VPN100]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[L3VPN-Access]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x1127667139}

[\[Sysname\] interface ve-l3vpn 100]{lang="EN-US"}

[\[Sysname-VE-L3VPN100\] description L3VPN-Access]{lang="EN-US"}
:::

::: {#186680629 .myid}
[]{#_Toc404791632}[]{#struct_0_16632_16529_x2127984885}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- display interface**

------------------------------------------------------------------------

[**[display interface]{lang="EN-US"}**]{#struct_0_16632_16529_x195327648}[命令用来显示接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_x287729053}

[**[display interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_16632_16529_2070227911}**[ve-l2vpn]{lang="DE"}**[ \[ *interface-number* *\| interface-number.subnumber* \] \| ]{lang="EN-US"}**[ve-l3vpn]{lang="DE"}**[ \[ *interface-number \| interface-number.subnumber* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_1475964748}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16632_16529_x1369309209}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_292688239}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_x129495146}

[[network-operator]{lang="EN-US"}]{#struct_0_16632_16529_x810769525}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_444072703}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16632_16529_2132404270}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1409075535}

[**[ve-l2vpn]{lang="DE"}**]{#struct_0_16632_16529_x1768989335}[：显示]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口或子接口的相关信息。]{style="font-family:宋体"}

[**[ve-l3vpn]{lang="DE"}**]{#struct_0_16632_16529_x2022522479}[：显示]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口或子接口的相关信息。]{style="font-family:宋体"}

[*[interface-number]{lang="DE"}*]{#struct_0_16632_16529_1858715188}[：]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口]{style="font-family:
宋体"}[或]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口]{style="font-family:宋体"}[的接口编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值已创建的]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口]{style="font-family:宋体"}[或]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口]{style="font-family:
宋体"}[的接口编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="DE"}*]{#struct_0_16632_16529_x618209887}[：]{style="font-family:宋体"}[L2VE]{lang="DE"}[子接口或]{style="font-family:
宋体"}[L3VE]{lang="DE"}[子接口的]{style="font-family:宋体"}[接口编号。其中]{style="font-family:宋体"}*[interface-number]{lang="DE"}*[为主接口编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值为已创建的]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口或]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口]{style="font-family:宋体"}[的接口编号]{style="font-family:宋体"}[；]{style="font-family:宋体"}*[subnumber]{lang="DE"}*[为子接口编号。该参数的支持情况[及子接口编号的取值范围]{style="color:black"}与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_16632_16529_888209967}[：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_16632_16529_x1369374745}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_16632_16529_x96801085}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16632_16529_1286921181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型（]{style="font-family:宋体"}]{#struct_0_16632_16529_x848762130}**[ve-l2vpn]{lang="DE"}**[和]{style="font-family:宋体"}**[ve-l3vpn]{lang="DE"}**[），将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型，不指定接口编号（]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*]{#struct_0_16632_16529_1951737918}[和]{lang="EN-US" style="font-family:
宋体"}*[interface-number.subnumber]{lang="EN-US"}*[）]{lang="EN-US" style="font-family:宋体"}[，则显示所有指定类型接口的信息。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则显示指定接口的信息。]{style="font-family:宋体"}]{#struct_0_16632_16529_x224922508}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_x460002573}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_1058670995}[显示接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_16632_16529_x1369440281}[display interface ve-l2vpn 100]{lang="NL-BE"}

[VE-L2VPN100]{lang="NL-BE"}

[Current state: UP]{lang="NL-BE"}

[Line protocol state: UP]{lang="NL-BE"}

[Description: VE-L2VPN100 Interface]{lang="NL-BE"}

[Bandwidth: 100000kbps]{lang="NL-BE"}

[Maximum Transmit Unit: 1500]{lang="NL-BE"}

[Internet protocol processing: disabled]{lang="NL-BE"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0202]{lang="NL-BE"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0202]{lang="NL-BE"}

[Link service is PWE3 ethernet mode]{lang="NL-BE"}

[Physical: L2VE]{lang="NL-BE"}

[Last clearing of counters: Never]{lang="NL-BE"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="NL-BE"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="NL-BE"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}

[[表1-1 ]{lang="EN-US"}[display interface]{lang="EN-US"}]{#struct_0_16632_16529_270243419}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1645885852}[[字段]{style="font-family:黑体"}]{#struct_0_16632_16529_x556012977}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16632_16529_141887597}

[[VE-L2VPN100]{lang="NL-BE"}]{#struct_0_16632_16529_1047552499}

[[接口]{style="font-family:宋体"}]{#struct_0_16632_16529_x1461364218}[VE-L2VPN100]{lang="NL-BE"}[的相关信息]{style="font-family:宋体"}

[[C]{lang="NL-BE"}[urrent state]{lang="EN-US"}]{#struct_0_16632_16529_x1994676981}

[[接口的物理状态和管理状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16632_16529_307532413}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administr]{lang="EN-US"}]{#struct_0_16632_16529_x1369505817}[a]{lang="EN-US"}[t]{lang="EN-US"}[ive]{lang="EN-US"}[ly DOWN]{lang="EN-US"}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_16632_16529_x1777372685}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_16632_16529_x1459664294}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_16632_16529_x528601425}

[[接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：]{style="font-family:宋体"}]{#struct_0_16632_16529_2042394162}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_16632_16529_x848468924}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_16632_16529_704886312}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_16632_16529_x115034437}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_16632_16529_x1369047065}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_16632_16529_1310639089}

[[Bandwidth]{lang="NL-BE"}]{#struct_0_16632_16529_x1976879832}

[[接口的期望带宽，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_16632_16529_1728827852}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_16632_16529_x1268335039}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_16632_16529_1031096230}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_16632_16529_x1369112601}

[[Tunnel]{lang="NO-BOK"}]{#struct_0_16632_16529_x701579714}[接口的]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址。如果没有为]{style="font-family:宋体"}[Tunnel]{lang="NO-BOK"}[接口配置]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址，则该字段显示为]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}[，表示不能处理]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[报文]{style="font-family:宋体"}

[[Primary]{lang="EN-US"}]{#struct_0_16632_16529_x52819276}[表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_16632_16529_x1884755448}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IP]{lang="EN-US"}]{#struct_0_16632_16529_1347366878}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_16632_16529_x1830516650}[，]{style="font-family:宋体"}[Hardware Address]{lang="EN-US"}

[[IPv6]{lang="EN-US"}]{#struct_0_16632_16529_196512591}[报文发送帧格式，硬件地址]{style="font-family:宋体"}

[[Link service]{lang="EN-US"}]{#struct_0_16632_16529_1406769845}

[[链路业务模式，取值包括：]{style="font-family:宋体"}]{#struct_0_16632_16529_1532706048}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS mode]{lang="EN-US"}]{#struct_0_16632_16529_x913560705}[：]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}[接口上绑定]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例时，接口的链路业务为该模式。]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[VPLS]{lang="EN-US"}["]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PWE3 ethernet mode]{lang="EN-US"}]{#struct_0_16632_16529_135647870}[：]{lang="EN-US" style="font-family:
  宋体"}[PWE3]{lang="EN-US"}[的]{lang="EN-US" style="font-family:
  宋体"}[Ethernet]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}[接口与]{style="font-family:宋体"}[PW]{lang="EN-US"}[关联，并且]{style="font-family:宋体"}[PW]{lang="EN-US"}[的封装方式为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[模式时，接口的链路业务为该模式。]{style="font-family:宋体"}[PW]{lang="EN-US"}[的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}["]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PWE3 vlan mode]{lang="EN-US"}]{#struct_0_16632_16529_190630245}[：]{lang="EN-US" style="font-family:宋体"}[PWE3]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}[接口与]{style="font-family:宋体"}[PW]{lang="EN-US"}[关联，并且]{style="font-family:宋体"}[PW]{lang="EN-US"}[的封装方式为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[模式时，接口的链路业务为该模式。]{style="font-family:宋体"}[PW]{lang="EN-US"}[的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}["]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_16632_16529_196447055}

[[接口的物理类型，取值包括：]{style="font-family:宋体"}]{#struct_0_16632_16529_x1766173885}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_2059094659}[：表示该接口为用来终结]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口或子接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L3VE]{lang="EN-US"}]{#struct_0_16632_16529_x347388375}[：表示该接口为用来接入]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[或]{style="font-family:宋体"}[IP]{lang="EN-US"}[骨干网的]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口或子接口]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_16632_16529_2037953996}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_16632_16529_196381519}[命令清除接口下的统计信息的时间（如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_16632_16529_x1633117742}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_16632_16529_1519379020}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的包数]{style="font-family:宋体"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_16632_16529_82654594}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_16632_16529_x1637477225}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的包数]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_16632_16529_196315983}

[[总计输入的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_16632_16529_780673903}[总计输入的字节，总计丢弃的输入报文数]{style="font-family:宋体"}

[[Output: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_16632_16529_x455531759}

[[总计输出的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_16632_16529_1596620244}[总计输出的字节，总计丢弃的输出报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x287221658}[显示所有]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[类型接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ve-l2vpn brief]{lang="EN-US"}]{#struct_0_16632_16529_196774735}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[L2VE20                DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x323583059}[显示接口]{style="font-family:宋体"}[L2VE2]{lang="EN-US"}[的概要信息，包括用户配置的全部描述信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ve-l2vpn 2 brief description]{lang="EN-US"}]{#struct_0_16632_16529_x548511985}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[L2VE2                 UP    UP       1.1.1.1          L2VPN-Terminate]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_2091288017}[显示当前状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface brief down]{lang="EN-US"}]{#struct_0_16632_16529_x571693293}

[Brief information of interface(s) under route mode:]{lang="NL-BE"}

[Link: ADM - administratively down; Stby - standby]{lang="NL-BE"}

[Interface            Link Cause]{lang="NL-BE"}

[L2VE20]{lang="EN-US"}[               DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[L3VE20]{lang="EN-US"}[               DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[]{#struct_0_16632_16529_x1004963996}[[表1-2 ]{lang="EN-US"}[display interface brief]{lang="EN-US"}]{#_Ref129008332}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_1673799228}[[字段]{style="font-family:黑体"}]{#struct_0_16632_16529_253948654}

[[描述]{style="font-family:黑体"}]{#struct_0_16632_16529_196709199}

[[Brief information of interface(s) under route mode:]{lang="EN-US"}]{#struct_0_16632_16529_x1876506530}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_16632_16529_x1946054117}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_16632_16529_x1615803665}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_16632_16529_1281697897}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_16632_16529_698275080}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_16632_16529_1025202406}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_16632_16529_x1875567272}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的网络层协议状态显示是]{style="font-family:宋体"}[UP]{lang="EN-US"}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_16632_16529_196643663}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_16632_16529_42340075}

[[Link]{lang="EN-US"}]{#struct_0_16632_16529_x183392534}

[[接口物理连接状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16632_16529_90594134}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_16632_16529_1615509607}[：表示本链路物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_16632_16529_424031422}[：表示本链路物理上]{lang="EN-US" style="font-family:宋体"}[是]{style="font-family:宋体"}[不通的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_16632_16529_333208646}[：表示本链路被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_16632_16529_196578127}[：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_16632_16529_x950482931}

[[接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：]{style="font-family:宋体"}]{#struct_0_16632_16529_143395156}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_16632_16529_1242275675}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (s)]{lang="EN-US"}]{#struct_0_16632_16529_x970135992}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_16632_16529_609443782}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_16632_16529_197036879}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16632_16529_1031442507}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_16632_16529_x689439283}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_16632_16529_x2066475852}

[[Cause]{lang="EN-US"}]{#struct_0_16632_16529_1771125599}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_16632_16529_842175151}[的原因，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_16632_16529_196971343}[：表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_16632_16529_x88297153}[：表示未成功建立隧道]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="NL-BE"}

[]{#_Toc290542368}[]{#_Toc290542364}[]{#_Toc263067887}[]{#_Toc207010368}[]{#_Toc207010101}[]{#_Toc205805549}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1522746903}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_16632_16529_881143656}

::::: {#-609497025 .myid}
[]{#_Toc404791633}[]{#struct_0_16632_16529_98436986}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- interface ve-l2vpn**

------------------------------------------------------------------------

[**[interface ve-l2vpn]{lang="DE"}**]{#struct_0_16632_16529_293591511}[命令用来创建一个]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口或子接口，并进入]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口或子接口视图。]{style="font-family:宋体"}

[**[undo interface ]{lang="EN-US"}**]{#struct_0_16632_16529_x1015758775}**[ve-l2vpn]{lang="DE"}**[命令用来删除指定的]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口或子接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_x609995739}

[**[interface ve-l2vpn]{lang="DE"}**]{#struct_0_16632_16529_x767412018}[ ]{lang="DE"}[{ *interface-number \| interface-number.subnumber* }]{lang="EN-US"}

[**[undo interface ]{lang="IT"}**]{#struct_0_16632_16529_196512592}**[ve-l2vpn ]{lang="DE"}**[{ *interface-number \| interface-number.subnumber* }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16632_16529_1406769842}

[[设备上不存在任何]{style="font-family:宋体"}[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_1532640512}[接口和]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_1831212249}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16632_16529_x987234665}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_771954350}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_x405893814}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_506297674}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16632_16529_11140447}

[*[interface-number]{lang="EN-US"}*]{#struct_0_16632_16529_1636616148}[：]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8192]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_16632_16529_x1364946857}[：]{style="font-family:
宋体"}[L2VE]{lang="EN-US"}[子接口的接口编号。其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8192]{lang="EN-US"}[；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号。该参数的支持情况及子接口编号的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16632_16529_2025663390}

[[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_x1880783509}[接口（又称为]{style="font-family:宋体"}[VE-L2VPN]{lang="EN-US"}[接口）或子接口用于终结]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[报文。]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口将还原的原始二层报文直接转交给与其相同接口编号的]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口或子接口处理，但是]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口只能将还原的二层报文直接转交给与其相同接口编号的]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口处理。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16632_16529_x1711231798}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16632_16529_112352427}[L2VE]{lang="EN-US"}[子接口收到的]{style="font-family:宋体"}[报文带有]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[时，]{lang="EN-US" style="font-family:宋体"}[需要在]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口上配置]{style="font-family:宋体"}[终结报文中的]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结的详细介绍，请参见"二层技术]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结"。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_16632_16529_1602445516}[L2VE]{lang="EN-US"}[接口，该接口上的子接口也将被删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_16632_16529_1636657773}[L2VE]{lang="EN-US"}[子接口之前，该子接口对应的主接口必须已经存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_16632_16529_451852034}[VPLS]{lang="EN-US"}[方式]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[接入]{style="font-family:宋体"}[L3VPN]{lang="EN-US"}[或]{style="font-family:宋体"}[IP]{lang="EN-US"}[骨干网的组网中，不支持创建]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](L2VPN接入L3VPN或IP骨干网命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_16632_16529_x672796600}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[子接口的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_16632_16529_x1455047101}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_196447056}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x1766173882}[创建接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_136780358}

[\[Sysname\] interface ve-l2vpn 100]{lang="EN-US"}

[\[Sysname-VE-L2VPN100\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_201137084}[创建子接口]{style="font-family:宋体"}[VE-L2VPN100.10]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x788483}

[\[Sysname\] interface ve-l2vpn 100.10]{lang="EN-US"}

[\[Sysname-VE-L2VPN100.10\]]{lang="EN-US"}
:::::

::::: {#956586916 .myid}
[]{#_Toc404791634}[]{#struct_0_16632_16529_627617949}[]{#_Toc292195407}[]{#_Toc292714313}[]{#_Toc292195408}[]{#_Toc292714314}[]{#_Toc292195409}[]{#_Toc292714315}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- interface ve-l3vpn**

------------------------------------------------------------------------

[**[interface ve-l3vpn]{lang="DE"}**]{#struct_0_16632_16529_x1753612875}[命令用来创建一个]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口或子接口，并进入]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口或子接口视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_16632_16529_x327677818}**[interface ve-l3vpn]{lang="DE"}**[命令用来删除指定的]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口或子接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_x795046658}

[**[interface ve-l3vpn]{lang="DE"}**]{#struct_0_16632_16529_2001014387}[ ]{lang="DE"}[{ *interface-number \| interface-number.subnumber* }]{lang="EN-US"}

[**[undo ]{lang="EN-US"}**]{#struct_0_16632_16529_605743565}**[interface ve-l3vpn ]{lang="DE"}**[{ *interface-number \| interface-number.subnumber* }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16632_16529_x130629626}

[[设备上不存在任何]{style="font-family:宋体"}[L3VE]{lang="EN-US"}]{#struct_0_16632_16529_1045893904}[接口和]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_196381520}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16632_16529_323197387}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1983283180}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_x1660885602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_x1781667896}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16632_16529_1777247741}

[*[interface-number]{lang="EN-US"}*]{#struct_0_16632_16529_x1873839021}[：]{style="font-family:宋体"}[L3VE]{lang="IT"}[接口的接口]{style="font-family:宋体"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8192]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_16632_16529_x536744417}[：]{style="font-family:
宋体"}[L3VE]{lang="EN-US"}[子接口的接口编号。其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8192]{lang="EN-US"}[；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号。该参数的支持情况及子接口编号的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16632_16529_x767815608}

[[L3VE]{lang="EN-US"}]{#struct_0_16632_16529_x836409138}[接口（又称为]{style="font-family:宋体"}[VE-L3VPN]{lang="EN-US"}[接口）用来将报文接入]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[或]{style="font-family:宋体"}[IP]{lang="EN-US"}[骨干网。]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口从骨干网侧接收到报文后，将报文转交给接口编号相同的]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[接口进行]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[处理。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16632_16529_1741492945}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接入]{style="font-family:宋体"}]{#struct_0_16632_16529_x1688774121}[MPLS L3VPN]{lang="EN-US"}[或]{style="font-family:宋体"}[IP]{lang="EN-US"}[骨干网的报文带有]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[时，需要创建]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[子接口，以便终结报文中的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结的详细介绍，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_16632_16529_196315984}[L3VE]{lang="IT"}[接口，该接口上的子接口也将被删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_16632_16529_780673908}[L3VE]{lang="EN-US"}[子接口之前，该子接口对应的主接口必须已经存在。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](L2VPN接入L3VPN或IP骨干网命令.files/image001.png){#图片 2 width="63" height="25"}]{lang="EN-US"}]{#struct_0_16632_16529_x455531766}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[子接口的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_16632_16529_1595637201}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1343763195}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_276187069}[创建接口]{style="font-family:宋体"}[VE-L3VPN100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x1647032871}

[\[Sysname\] interface ve-l3vpn 100]{lang="EN-US"}

[\[Sysname-VE-L3VPN100\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x939491796}[创建]{style="font-family:宋体"}[子]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[VE-L3VPN100.10]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[子]{style="font-family:宋体"}[接口视图。]{style="font-family:宋体"}

[[\[Sysname\] interface ve-l3vpn 100.10]{lang="IT"}]{#struct_0_16632_16529_1812098559}

[\[Sysname-]{lang="EN-US"}[VE-L3VPN100.10]{lang="IT"}[\]]{lang="EN-US"}
:::::

::: {#988247972 .myid}
[]{#_Toc404791635}[]{#struct_0_16632_16529_x819811840}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_16632_16529_196774736}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_16632_16529_x323583058}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_x548577521}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_16632_16529_617073193}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_16632_16529_2076156385}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1676024881}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_16632_16529_x302988245}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_91395739}

[[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_x122783010}[接口视图]{style="font-family:宋体"}[/L2VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1190371507}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_x276978493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_974413333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1994724060}

[*[size]{lang="EN-US"}*]{#struct_0_16632_16529_196709200}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[46]{lang="EN-US"}[～]{style="font-family:宋体"}[1560]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_1661680898}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_1704874898}[配置接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_130610518}

[\[Sysname\] interface ve-l2vpn 100]{lang="EN-US"}

[\[Sysname-VE-L2VPN100\] mtu 1430]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x1294570806}[配置接口]{style="font-family:宋体"}[VE-L3VPN100]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_1779503220}

[\[Sysname\] interface ve-l3vpn 100]{lang="EN-US"}

[\[Sysname-VE-L3VPN100\] mtu 1430]{lang="EN-US"}
:::

::: {#2052875588 .myid}
[]{#_Toc290542370}[]{#_Toc404791636}[]{#struct_0_16632_16529_275228928}[]{#_Toc290542313}[]{#_Toc263067840}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="DE"}**]{#struct_0_16632_16529_2142455954}[命令用来清除接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_145218053}

[**[reset counters interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_16632_16529_1729701105}**[ve-l2vpn]{lang="DE"}**[ \[ *interface-number* \| *interface-number.subnumber* \] \| ]{lang="EN-US"}**[ve-l3vpn]{lang="DE"}**[ ]{lang="DE"}[\[ *interface-number* \| *interface-number.subnumber* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_196643664}

[[用户视图]{style="font-family:宋体"}]{#struct_0_16632_16529_42340070}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_1008248554}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_x1517696761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_615652190}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1130982868}

[**[ve-l2vpn]{lang="DE"}**]{#struct_0_16632_16529_x1191689918}[：清除]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口或子接口的统计信息。]{style="font-family:宋体"}

[**[ve-l3vpn]{lang="DE"}**]{#struct_0_16632_16529_672743844}[：清除]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口或子接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="DE"}*]{#struct_0_16632_16529_x296502710}[：]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口]{style="font-family:
宋体"}[或]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口]{style="font-family:宋体"}[的接口编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值为已创建的]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口]{style="font-family:宋体"}[或]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口]{style="font-family:
宋体"}[的接口编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="DE"}*]{#struct_0_16632_16529_2001222865}[：]{style="font-family:宋体"}[L2VE]{lang="DE"}[子接口或]{style="font-family:
宋体"}[L3VE]{lang="DE"}[子接口的]{style="font-family:宋体"}[接口编号。其中]{style="font-family:宋体"}*[interface-number]{lang="DE"}*[为主接口编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值为已创建的]{style="font-family:宋体"}[L2VE]{lang="DE"}[接口或]{style="font-family:宋体"}[L3VE]{lang="DE"}[接口]{style="font-family:宋体"}[的接口编号]{style="font-family:宋体"}[；]{style="font-family:宋体"}*[subnumber]{lang="DE"}*[为子接口编号。该参数的支持情况[及子接口编号的取值范围]{style="color:black"}与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16632_16529_1837247979}

[[在某些情况下]{style="font-family:宋体"}]{#struct_0_16632_16529_2145826701}[，]{style="font-family:宋体"}[需要统计一定时间内某接口的流量]{style="font-family:宋体"}[，]{style="font-family:宋体"}[这就需要在统计开始前清除该接口原有的统计信息]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型（]{style="font-family:宋体"}]{#struct_0_16632_16529_196578128}**[ve-l2vpn]{lang="DE"}**[和]{style="font-family:宋体"}**[ve-l3vpn]{lang="DE"}**[），则清除所有接口的统计信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型]{lang="EN-US" style="font-family:宋体"}]{#struct_0_16632_16529_x950482946}[，]{lang="EN-US" style="font-family:宋体"}[不指定接口编号（]{lang="EN-US" style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[和]{lang="EN-US" style="font-family:宋体"}*[interface-number.subnumber]{lang="EN-US"}*[）]{lang="EN-US" style="font-family:宋体"}[，则清除所有指定类型接口的统计信息；]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则清除指定接口的统计信息。]{style="font-family:宋体"}]{#struct_0_16632_16529_143460695}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_369634206}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x1764399471}[清除接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface ve-l2vpn 100]{lang="EN-US"}]{#struct_0_16632_16529_183540599}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_1961807255}[清除接口]{style="font-family:宋体"}[VE-L3VPN100]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface ve-l3vpn 100]{lang="EN-US"}]{#struct_0_16632_16529_1982235396}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_1754250930}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface]{lang="EN-US"}**]{#struct_0_16632_16529_887825745}
:::

::: {#1170655049 .myid}
[]{#_Toc404791637}[]{#struct_0_16632_16529_1799919062}

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_16632_16529_1768570392}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_16632_16529_197036880}[命令用来开启当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1689546670}

[**[shutdown]{lang="EN-US"}**]{#struct_0_16632_16529_959376128}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_16632_16529_767885776}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1451400303}

[[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_x1247167621}[接口、]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口、]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口和]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[子接口均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16632_16529_826353881}

[[L2VE]{lang="EN-US"}]{#struct_0_16632_16529_1929365559}[接口视图]{style="font-family:宋体"}[/L2VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16632_16529_x1060448721}

[[network-admin]{lang="EN-US"}]{#struct_0_16632_16529_2019927758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16632_16529_x1347982351}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16632_16529_1290609821}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_196971344}[关闭接口]{style="font-family:宋体"}[VE-L2VPN100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_x88297152}

[\[Sysname\] interface ve-l2vpn 100]{lang="EN-US"}

[\[Sysname-VE-L2VPN100\] shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16632_16529_x1522746904}[关闭接口]{style="font-family:宋体"}[VE-L3VPN100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16632_16529_1284428183}

[\[Sysname\] interface ve-l3vpn 100]{lang="EN-US"}

[\[Sysname-VE-L3VPN100\] shutdown]{lang="EN-US"}
:::
