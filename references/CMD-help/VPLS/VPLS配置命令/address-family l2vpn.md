::: {#-1604945737 .myid}
[]{#_Toc339310125}[]{#_Toc336272255}[]{#_Toc404791631}[]{#struct_0_10012_x1780_458549647}[]{#_Toc339885933}[]{#_Toc337567360}

**VPLS \-- VPLS配置命令 \-- address-family l2vpn**

------------------------------------------------------------------------

[**[address-family l2vpn]{lang="EN-US"}**]{#struct_0_10012_x1780_442977325}[命令用来创建]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族，并进入]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[**[undo address-family l2vpn]{lang="EN-US"}**]{#struct_0_10012_x1780_1054571798}[命令用来删除]{style="font-family:
宋体"}[BGP L2VPN]{lang="EN-US"}[地址族及]{style="font-family:
宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_728652146}

[**[address-family l2vpn]{lang="EN-US"}**]{#struct_0_10012_x1780_1869140458}

[**[undo address-family l2vpn]{lang="EN-US"}**]{#struct_0_10012_x1780_516707250}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1965020162}

[[没有创建]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x1310559341}[地址族。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1092239167}

[[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1467072642}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1790712010}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_728717682}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1845249797}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1703584382}

[[在]{style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_332889168}[组网中，要想建立]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，需要在]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下通过]{style="font-family:宋体"}**[peer enable]{lang="EN-US"}**[命令使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体，以便]{style="font-family:宋体"}[PE]{lang="EN-US"}[与该对等体交换]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1780391561}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1389554737}[创建]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族，并进入]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_729307506}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\]]{lang="EN-US"}
:::

::: {#1067234336 .myid}
[]{#_Toc404791632}[]{#struct_0_10012_x1780_x481780486}

**VPLS \-- VPLS配置命令 \-- auto-discovery**

------------------------------------------------------------------------

[**[auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_1718633749}[命令用来指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_x1188321523}[命令用来取消]{style="font-family:宋体"}[VSI]{lang="EN-US"}[采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1554647672}

[**[auto-discovery bgp]{lang="EN-US"}**]{#struct_0_10012_x1780_299970585}

[**[undo auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_x1676891679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1702469964}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x93679853}[不会采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_729373042}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_694828640}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_639330925}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_541401365}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1793234507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_172829530}

[**[bgp]{lang="EN-US"}**]{#struct_0_10012_x1780_x1987717552}[：指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_479649905}

[[执行本命令进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_404957885}[自动发现视图后，在该视图下可以配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[自动发现的相关参数，如本端站点、]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[、]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性等，以便]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1643869774}[协议自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备后，可以采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[或]{style="font-family:宋体"}[BGP]{lang="EN-US"}[信令协议在]{style="font-family:宋体"}[PE]{lang="EN-US"}[之间建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}**[signaling-protocol]{lang="EN-US"}**[命令用来指定采用的信令协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_310806217}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1814573611}[指定名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1724275022}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_54556621}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_1895967648}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_10012_x1780_402312229}**[vsi]{lang="EN-US"}**
:::

::: {#2036451628 .myid}
[]{#_Toc404791633}[]{#struct_0_10012_x1780_x1643804238}

**VPLS \-- VPLS配置命令 \-- backup-peer**

------------------------------------------------------------------------

[**[backup-peer]{lang="EN-US"}**]{#struct_0_10012_x1780_1318069630}[命令]{style="font-family:宋体"}[用来配置]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI LDP]{lang="EN-US"}[备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图或]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。如果指定的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[已存在，则直接进入]{style="font-family:宋体"}[VSI LDP]{lang="EN-US"}[备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图或]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **backup-peer**]{lang="EN-US"}]{#struct_0_10012_x1780_x1707920029}[命令用来删除]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x413486292}

[[VSI LDP PW]{lang="EN-US"}]{#struct_0_10012_x1780_x2013414438}[视图：]{style="font-family:宋体"}

[**[backup-peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \[ **pw-id** *pw-id* \] \[ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* \] \*]{lang="EN-US"}]{#struct_0_10012_x1780_x914591287}

[**[undo]{lang="EN-US"}**[ **backup-peer** *ip-address* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_10012_x1780_x1511825941}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_2012555445}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图：]{style="font-family:宋体"}

[**[backup-peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \[ **pw-id** *pw-id* \] **in-label** *label-value* **out-label** *label-value* \[ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* \] \*]{lang="EN-US"}]{#struct_0_10012_x1780_x152021348}

[**[undo]{lang="EN-US"}**[ **backup-peer** *ip-address* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_10012_x1780_x1643738702}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_256253910}

[[未配置]{style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_x1204545744}[的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2126094386}

[[VSI LDP PW]{lang="EN-US"}]{#struct_0_10012_x1780_1247878356}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2036209751}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1484051909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x902699960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x373224679}

[*[ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_x1643673166}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}]{#struct_0_10012_x1780_x338198840}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果不指定本参数，则备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}**[default-pw-id]{lang="EN-US"}**[命令配置的缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_10012_x1780_x905869596}*[label-value]{lang="EN-US"}*[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签。]{style="font-family:宋体"}*[label-value]{lang="EN-US"}*[为入标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_10012_x1780_x1727984800}*[label-value]{lang="EN-US"}*[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的出标签。]{style="font-family:宋体"}*[label-value]{lang="EN-US"}*[为出标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pw-class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_10012_x1780_x592276573}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板中可以配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的数据封装类型、是否使用控制字等。如果不指定本参数，则]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，不支持控制字功能。]{style="font-family:宋体"}

[**[tunnel-policy]{lang="EN-US"}***[ tunnel-policy-name]{lang="EN-US"}*]{#struct_0_10012_x1780_1533480627}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的隧道选择策略。]{style="font-family:宋体"}*[tunnel-policy-name]{lang="EN-US"}*[表示隧道策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1391137944}

[[备份]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1644131918}[作为主]{style="font-family:宋体"}[PW]{lang="EN-US"}[的备份，可以为主]{style="font-family:宋体"}[PW]{lang="EN-US"}[提供冗余保护。当主]{style="font-family:宋体"}[PW]{lang="EN-US"}[出现故障时，设备将通过主]{style="font-family:宋体"}[PW]{lang="EN-US"}[对应的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发流量。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x137927531}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x841906906}[时指定的远端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[PW ID]{lang="EN-US"}[，不能与已经存在的]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}[ ]{lang="EN-US"}[PW]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[PW ID]{lang="EN-US"}[同时相同。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无需指定]{style="font-family:宋体"}]{#struct_0_10012_x1780_1403016721}[备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[hub]{lang="EN-US"}[属性和]{lang="EN-US" style="font-family:宋体"}[no-split-horizon]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}[，备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的这些属性]{style="font-family:宋体"}[与主]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[相同。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x574616286}[视图下通过]{lang="EN-US" style="font-family:宋体"}**[default-pw-id]{lang="EN-US"}**[命令配置了缺省]{lang="EN-US" style="font-family:宋体"}[PW ID]{lang="EN-US"}[，则执行]{lang="EN-US" style="font-family:宋体"}**[backup-peer]{lang="EN-US"}**[命令时可以不指定]{lang="EN-US" style="font-family:宋体"}**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}[参数，采用缺省的]{lang="EN-US" style="font-family:宋体"}[PW ID]{lang="EN-US"}[；否则，执行]{lang="EN-US" style="font-family:宋体"}**[backup-peer]{lang="EN-US"}**[命令时必须指定]{lang="EN-US" style="font-family:宋体"}**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}[参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果为静态]{style="font-family:宋体"}]{#struct_0_10012_x1780_653767229}[PW]{lang="EN-US"}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1243562390}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x78603019}[为名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[配置主备]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[：主]{style="font-family:宋体"}[PW]{lang="EN-US"}[的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[4.4.4.4]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[；备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5.5.5.5]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1644066382}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp\] peer 4.4.4.4 pw-id 100]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp-4.4.4.4-100\] backup-peer 5.5.5.5]{lang="EN-US"}[ pw-id 200]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp-4.4.4.4-100-backup\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2040422930}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-pw-id]{lang="EN-US"}**]{#struct_0_10012_x1780_721194416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ldp]{lang="EN-US"}**]{#struct_0_10012_x1780_1374928626}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_115969798}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer]{lang="EN-US"}**]{#struct_0_10012_x1780_x584715110}
:::

::: {#1807695599 .myid}
[]{#_Toc404791634}[]{#struct_0_10012_x1780_1787958473}[]{#_Toc375901834}[]{#_Toc375819693}[]{#_Toc375553164}[]{#_Toc373826859}

**VPLS \-- VPLS配置命令 \-- bandwidth（VSI LDP PW view/VSI static PW view）**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_1824117111}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_x180568281}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1056153595}

[**[bandwidth ]{lang="EN-US"}***[bandwidth-value]{lang="EN-US"}*]{#struct_0_10012_x1780_198493978}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_x660978154}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_172457163}

[[接口的期望带宽为]{style="font-family:宋体"}[10000000kbps]{lang="EN-US"}]{#struct_0_10012_x1780_x2132236328}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x812623312}

[[VSI LDP PW]{lang="EN-US"}]{#struct_0_10012_x1780_1788024009}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_799099357}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1298981438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1061085930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_560765652}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_10012_x1780_x1319174945}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[的期望带宽，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_2119007770}

[[接口的期望带宽会对]{style="font-family:宋体"}[CBQ]{lang="EN-US"}]{#struct_0_10012_x1780_x1552913082}[队列带宽有影响。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1052348894}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1116450530}[在静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[上配置期望带宽为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1222201637}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling static]{lang="EN-US"}

[\[Sysname-vsi-vpn1-static\] peer 5.5.5.5 pw-id 200 in-label 100 out-label 200]{lang="EN-US"}

[\[Sysname-vsi-vpn1-static-5.5.5.5-200\] bandwidth 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1478427868}[在]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[上配置期望带宽为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1384149655}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp\] peer 4.4.4.4 pw-id 100]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp-4.4.4.4-100\] bandwidth 10000]{lang="EN-US"}
:::

::::: {#-1268862555 .myid}
[]{#_Toc404791635}[]{#struct_0_10012_x1780_845909010}[]{#_Toc300843382}[]{#_Toc300843383}

**VPLS \-- VPLS配置命令 \-- bandwidth（VSI view）**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](VPLS命令.files/image001.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_x263111014}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_x2051238563}
:::

**[ ]{lang="EN-US"}**

[**[bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_x1644000846}[命令用来配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的最大带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_x904678413}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1396283003}

[**[bandwidth ]{lang="EN-US"}***[bandwidth]{lang="EN-US"}*]{#struct_0_10012_x1780_x145229026}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_x1205982691}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x426411927}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1643935310}[的最大带宽值为]{style="font-family:宋体"}[102400kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x334558968}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1826522958}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1855644560}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1215357368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1270980400}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1290803956}

[*[bandwidth]{lang="EN-US"}*]{#struct_0_10012_x1780_x1643345486}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的最大带宽，取值为]{style="font-family:宋体"}[64]{lang="EN-US"}[～]{style="font-family:宋体"}[4194303]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1797140130}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1914787982}[的最大带宽用来限制指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内创建的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[上转发的流量。限制的是]{style="font-family:宋体"}[PW]{lang="EN-US"}[入方向、出方向流量，还是同时限制入方向和出方向流量，以及超出最大带宽后如何处理，与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_840137047}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1643279950}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的最大带宽值为]{style="font-family:宋体"}[10240kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x689597030}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] bandwidth 10240]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x949509476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_x613406043}
:::::

::::: {#724706928 .myid}
[]{#_Toc404791636}[]{#struct_0_10012_x1780_x1750025258}

**VPLS \-- VPLS配置命令 \-- control-word enable**

------------------------------------------------------------------------

[**[control-word enable]{lang="EN-US"}**]{#struct_0_10012_x1780_x195251673}[命令用来使能控制字功能。]{style="font-family:宋体"}

[**[undo control-word enable]{lang="EN-US"}**]{#struct_0_10012_x1780_x1643869773}[命令用来恢复缺省情况]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_714090744}

[**[control-word enable]{lang="EN-US"}**]{#struct_0_10012_x1780_1447748654}

[**[undo control-word enable]{lang="EN-US"}**]{#struct_0_10012_x1780_x590092206}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1250638858}

[[未使能控制字功能。]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1120220766}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x929387237}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x685732769}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1643804237}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_108216049}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1495758668}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_848737146}

[[控制字字段位于]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_10012_x1780_983238137}[标签栈和二层数据之间，用来携带额外的二层数据帧的控制信息，如序列号等。控制字具有如下功能：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[避免报文乱序：在多路径转发的情况下，报文有可能产生乱序，此时可以通过控制字的序列号字段对报文进行排序重组。]{style="font-family:宋体"}]{#struct_0_10012_x1780_1251983018}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指示净载荷长度：如果]{style="font-family:宋体"}]{#struct_0_10012_x1780_1221641754}PW[上传送报文的净载荷长度小于]{style="font-family:宋体"}64[字节，则需要对报文进行填充，以避免报文发送失败。此时，通过控制字的载荷长度字段可以确定原始载荷的长度，以便从填充后的报文中正确获取原始的报文载荷。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VPLS命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10012_x1780_x187520972}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[上述功能的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_x1713486642}
:::

[ ]{lang="EN-US"}

[[本命令用来配置本端是否支持携带控制字字段。报文实际是否携带控制字字段，由两端的配置共同决定：如果两端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x1643738701}[上都使能了控制字功能，则报文中携带控制字字段；否则，报文中不携带控制字字段。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_180765898}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1080936584}[使能]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板]{style="font-family:宋体"}[pw100]{lang="EN-US"}[的控制字功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_444489609}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] control-word enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x71732798}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_x1643673165}
:::::

::: {#-833925659 .myid}
[]{#_Toc404791637}[]{#struct_0_10012_x1780_x741483367}

**VPLS \-- VPLS配置命令 \-- default-pw-id**

------------------------------------------------------------------------

[**[default-pw-id]{lang="EN-US"}**]{#struct_0_10012_x1780_x1337090888}[命令用来配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo default-pw-id]{lang="EN-US"}**]{#struct_0_10012_x1780_827486164}[命令用来删除为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[配置的缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2049647871}

[**[default-pw-id ]{lang="EN-US"}***[default-pw-id]{lang="EN-US"}*]{#struct_0_10012_x1780_774654545}

[**[undo ]{lang="EN-US"}[default-pw-id]{lang="EN-US"}**]{#struct_0_10012_x1780_211405814}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x529752704}

[[未配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x693245264}[的缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1644131917}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x541212058}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1989990542}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_927113435}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_925443425}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2117898300}

[*[default-pw-id]{lang="EN-US"}*]{#struct_0_10012_x1780_x1509882383}[：缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1085912485}

[[通过本命令指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1644066381}[的缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[后，执行]{style="font-family:宋体"}**[backup-peer]{lang="EN-US"}**[、]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令时，可以不指定]{style="font-family:宋体"}**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}[参数，创建的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[、]{style="font-family:宋体"}[PW]{lang="EN-US"}[采用缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，从而简化配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1637138403}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1449880342}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1344692335}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] default-pw-id 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_832753019}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup-peer]{lang="EN-US"}**]{#struct_0_10012_x1780_x1941222117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer]{lang="EN-US"}**]{#struct_0_10012_x1780_684040387}
:::

::: {#-1461383778 .myid}
[]{#_Toc404791638}[]{#struct_0_10012_x1780_x574770887}

**VPLS \-- VPLS配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_10012_x1780_x1644000845}[命令用来设置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_10012_x1780_1824204942}[命令用来删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1313185350}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_10012_x1780_x1410486402}

[**[undo description]{lang="EN-US"}**]{#struct_0_10012_x1780_x1459708347}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_2147258063}

[[未配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_608754661}[的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x694861219}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_321237518}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1643935309}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_2038159563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1068447856}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x843349120}

[*[text]{lang="EN-US"}*]{#struct_0_10012_x1780_1177037410}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1281915917}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x460276397}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[vsi for vpn1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1643345485}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] description vsi for vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_231056189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_443909155}
:::

::: {#-499473616 .myid}
[]{#_Toc339310130}[]{#_Toc404791639}[]{#struct_0_10012_x1780_1876890158}[]{#_Toc339885939}[]{#_Toc361662039}[]{#_Toc361662040}[]{#_Toc361662041}[]{#_Toc361662042}[]{#_Toc361662043}[]{#_Toc361662044}[]{#_Toc361662045}[]{#_Toc361662046}[]{#_Toc361662047}[]{#_Toc361662048}[]{#_Toc361662049}[]{#_Toc361662050}[]{#_Toc361662051}[]{#_Toc361662052}[]{#_Toc361662053}[]{#_Toc361662054}[]{#_Toc361662055}[]{#_Toc361662056}[]{#_Toc361662057}[]{#_Toc361662058}[]{#_Toc361662059}[]{#_Toc361662060}[]{#_Toc361662061}[]{#_Toc361662062}[]{#_Toc361662063}[]{#_Toc361662064}[]{#_Toc361662065}[]{#_Toc361662066}[]{#_Toc361662067}[]{#_Toc361662068}[]{#_Toc361662069}[]{#_Toc361662070}[]{#_Toc361662071}[]{#_Toc361662072}[]{#_Toc361662073}[]{#_Toc361662074}[]{#_Toc361662075}[]{#_Toc361662076}[]{#_Toc361662077}[]{#_Toc361662078}[]{#_Toc361662079}[]{#_Toc307388003}[]{#_Toc307232835}[]{#_Toc361662142}

**VPLS \-- VPLS配置命令 \-- display bgp l2vpn auto-discovery**

------------------------------------------------------------------------

[**[display bgp l2vpn auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_x722848766}[命令用来显示通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1106290353}

[**[display bgp l2vpn auto-discovery ]{lang="EN-US"}**[\[ **peer** *ip-address* { **advertised** \| **received** } \[ **statistics** \] \| **route-distinguisher** *route-distinguisher* \[ **pe-address** *ip-address* \[ **advertise-info** \] \] \| **statistics** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x1549458385}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1695712048}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1382919047}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1643804239}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1410813725}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_1584738522}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_499044918}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x1448531277}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x871691385}

[**[peer]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_10012_x1780_824217134}[：]{style="font-family:宋体"}[显示向指定对等体发布或者从指定对等体收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[对等体的地址。]{style="font-family:宋体"}

[**[advertised]{lang="EN-US"}**]{#struct_0_10012_x1780_164549149}[：显示向指定对等体发布的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[received]{lang="EN-US"}**]{#struct_0_10012_x1780_x1038436363}[：显示从指定对等体接收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_10012_x1780_x1643738703}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[route-distinguisher]{lang="EN-US"}***[ route-distinguisher]{lang="EN-US"}*]{#struct_0_10012_x1780_x1309830031}[：显示通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的指定路由标识符的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[route-distinguisher]{lang="EN-US"}*[为路由标识符，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。路由标识符有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_10012_x1780_x1064275863}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x1011628414}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x898735998}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。]{style="font-family:宋体"}[例如：]{lang="EN-US" style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[pe-address ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_86934562}[：显示通过]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[协议自动发现的指定]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为自动发现的]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_10012_x1780_434909931}[：显示通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的通告信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1828997191}

[[执行本命令时，如果没有指定任何参数，则显示所有通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_702594599}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1643673167}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1904282781}[显示所有通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn auto-discovery]{lang="EN-US"}]{#struct_0_10012_x1780_x2095359330}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.140]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total number of automatically discovered PEs: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 2:2]{lang="EN-US"}

[ Total number of automatically discovered PEs: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[     PE address      Nexthop         VPLS ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  1.1.1.9         0.0.0.0         100:100]{lang="EN-US"}

[\* \>i 2.2.2.9         2.2.2.9         100:100]{lang="EN-US"}

[\* \>i 3.3.3.9         3.3.3.9         100:100]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display bgp l2vpn auto-discovery]{lang="EN-US"}]{#struct_0_10012_x1780_60698}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1768091681}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1644131919}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1704011472}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_10012_x1780_x785774365}

[[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1252911238}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Status codes]{lang="EN-US"}]{#struct_0_10012_x1780_384936739}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1154878475}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\* - valid]{lang="EN-US"}]{#struct_0_10012_x1780_x1644066383}[：合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> - best]{lang="EN-US"}]{#struct_0_10012_x1780_x474338989}[：普通优选路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d - damped]{lang="EN-US"}]{#struct_0_10012_x1780_608918862}[：震荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h - history]{lang="EN-US"}]{#struct_0_10012_x1780_x859786062}[：历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s - suppressed]{lang="EN-US"}]{#struct_0_10012_x1780_x596494584}[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S - Stale]{lang="EN-US"}]{#struct_0_10012_x1780_437975192}[：过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i - internal]{lang="EN-US"}]{#struct_0_10012_x1780_x1644000847}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e - external]{lang="EN-US"}]{#struct_0_10012_x1780_661405528}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_10012_x1780_87901560}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x241552658}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的来源，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="EN-US"}]{#struct_0_10012_x1780_x2024134658}[：表示产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[内]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1643935311}[：表示是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="EN-US"}[，外部网关协议）学到的]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="EN-US"}]{#struct_0_10012_x1780_x1900642909}[：表示来源无法确定]{lang="EN-US" style="font-family:宋体"}

[[Total number of automatically discovered PEs]{lang="EN-US"}]{#struct_0_10012_x1780_x571159832}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x116791159}[协议自动发现的所有]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的总数]{style="font-family:宋体"}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_10012_x1780_x1643345487}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_x931743225}

[[Total number of automatically discovered PEs]{lang="EN-US"}]{#struct_0_10012_x1780_355358547}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_735106541}[协议自动发现的、路由标识符为指定值的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息数目]{style="font-family:宋体"}

[[PE address]{lang="EN-US"}]{#struct_0_10012_x1780_x897661821}

[[自动发现的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x1643279951}[在]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内的标识]{style="font-family:宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_10012_x1780_2039286325}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x474603744}[的地址]{style="font-family:宋体"}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_1316255584}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1643869778}[，用来标识]{style="font-family:宋体"}[PE]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1658562251}[显示通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的路由标识符为]{style="font-family:宋体"}[2:2]{lang="EN-US"}[、地址为]{style="font-family:宋体"}[2.2.2.9]{lang="EN-US"}[的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn auto-discovery route-distinguisher 2:2 pe-address 2.2.2.9]{lang="EN-US"}]{#struct_0_10012_x1780_x1952801165}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.140]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 2:2]{lang="EN-US"}

[ Total number of automatically discovered PEs: 1]{lang="EN-US"}

[ Paths:   1 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ From            : 2.2.2.9 (192.168.1.135)]{lang="EN-US"}

[ Original nexthop: 2.2.2.9]{lang="EN-US"}

[ Ext-Community   : \<RT: 2:2\>, \<VPLS ID: 100:100\>]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : localpref 100, pref-val 0]{lang="EN-US"}

[ PE address      : 2.2.2.9]{lang="EN-US"}

[ State           : valid, internal, best]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display bgp l2vpn auto-discovery]{lang="EN-US"}]{#struct_0_10012_x1780_751981255}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1772865217}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1643804242}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_511828256}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1954084057}

[[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_66529884}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Local AS number]{lang="EN-US"}]{#struct_0_10012_x1780_x362759858}

[[本地自治系统号]{style="font-family:宋体"}]{#struct_0_10012_x1780_x632098521}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_10012_x1780_x1643738706}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_x2069344918}

[[Total number of automatically discovered PEs]{lang="EN-US"}]{#struct_0_10012_x1780_1701285552}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_1569155895}[协议自动发现的、路由标识符为指定值的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息总数]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_10012_x1780_x1705862486}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1933662611}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的数目：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_10012_x1780_x1643673170}[：有效可达信息数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_10012_x1780_x1500932718}[：最佳可达信息数目]{lang="EN-US" style="font-family:宋体"}

[[From]{lang="EN-US"}]{#struct_0_10012_x1780_2120120154}

[[发布该信息的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_1305159417}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Original nexthop]{lang="EN-US"}]{#struct_0_10012_x1780_x21217985}

[[原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1644131922}[更新消息中获得的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_10012_x1780_x944299977}

[[扩展团体属性值，包括：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x669767144}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_10012_x1780_x38317657}[：]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1999098472}[：用来标识该]{style="font-family:宋体"}[PE]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[AS-path]{lang="EN-US"}]{#struct_0_10012_x1780_x1644066386}

[[AS]{lang="EN-US"}]{#struct_0_10012_x1780_285175898}[路径属性，记录了此]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免环路的出现]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_10012_x1780_x2041791167}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_859686301}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的起源代码，取值包括]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="EN-US"}]{#struct_0_10012_x1780_x1644000850}[：表示可达信息来源于]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="EN-US"}]{#struct_0_10012_x1780_x2067412291}[：表示可达信息通过]{style="font-family:宋体"}[EGP]{lang="EN-US"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[incomplete]{lang="EN-US"}]{#struct_0_10012_x1780_x1435775629}[：表示可达信息的来源无法确定]{lang="EN-US" style="font-family:宋体"}

[[Attribute value]{lang="EN-US"}]{#struct_0_10012_x1780_447992878}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1643935314}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的属性值，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_10012_x1780_1634809500}[：与目的网络关联的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_10012_x1780_1314210895}[：本地优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_10012_x1780_x594475682}[：首选值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_10012_x1780_x1643345490}[：协议优先级]{lang="EN-US" style="font-family:宋体"}

[[PE address]{lang="EN-US"}]{#struct_0_10012_x1780_990505540}

[[自动发现的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x1718646663}[在]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内的标识]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_1192823727}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1643279954}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的当前状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_10012_x1780_1636001798}[：有效信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_10012_x1780_1608622200}[：内部信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_10012_x1780_x1113048463}[：外部信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_10012_x1780_x1643869777}[：本地产生信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_10012_x1780_x1255277724}[：最佳信息]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x2077397471}[显示通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn auto-discovery route-distinguisher 2:2 pe-address 1.1.1.9 advertise-info]{lang="EN-US"}]{#struct_0_10012_x1780_x1643804241}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.140]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 2:2]{lang="EN-US"}

[ Total number of automatically discovered PEs: 1]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ VPLS ID         : 100:100]{lang="EN-US"}

[ PE address      : 1.1.1.9]{lang="EN-US"}

[ Advertised to peers (2 in total):]{lang="EN-US"}

[    2.2.2.9]{lang="EN-US"}

[    3.3.3.9]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display bgp l2vpn auto-discovery advertise-info]{lang="EN-US"}]{#struct_0_10012_x1780_x1054255685}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1776745377}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x8142932}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_928355853}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_10012_x1780_977989662}

[[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_282070842}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Local AS number]{lang="EN-US"}]{#struct_0_10012_x1780_x737620966}

[[本地自治系统号]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1643738705}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_10012_x1780_1822337851}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_x25706651}

[[Total number of automatically discovered PEs]{lang="EN-US"}]{#struct_0_10012_x1780_x665766398}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_1043455247}[协议自动发现的、路由标识符为指定值的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息数目]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_10012_x1780_x47585923}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1643673169}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的数目：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_10012_x1780_1584115461}[：有效可达信息数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_10012_x1780_x728121761}[：最佳可达信息数目]{lang="EN-US" style="font-family:宋体"}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x443058835}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1510492861}[，用来标识]{style="font-family:宋体"}[PE]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[PE address]{lang="EN-US"}]{#struct_0_10012_x1780_x1644131921}

[[自动发现的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x1347584504}[在]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内的标识]{style="font-family:宋体"}

[[Advertised to peers (2 in total)]{lang="EN-US"}]{#struct_0_10012_x1780_92439144}

[[该信息已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_10012_x1780_x2025954658}

[ ]{lang="EN-US"}

::: {#1061336316 .myid}
[]{#_Toc336272262}[]{#_Toc336272265}[]{#_Toc404791640}[]{#struct_0_10012_x1780_x2057746363}[]{#_Toc339885970}[]{#_Toc337567367}[]{#_Toc353354474}[]{#_Toc353354475}[]{#_Toc353354476}[]{#_Toc353354477}[]{#_Toc353354478}[]{#_Toc353354479}[]{#_Toc353354480}[]{#_Toc353354481}[]{#_Toc353354482}[]{#_Toc353354483}[]{#_Toc353354484}[]{#_Toc353354485}[]{#_Toc353354486}[]{#_Toc353354487}[]{#_Toc353354488}[]{#_Toc353354489}[]{#_Toc353354490}[]{#_Toc353354491}[]{#_Toc353354492}[]{#_Toc353354493}[]{#_Toc353354494}[]{#_Toc353354495}[]{#_Toc353354496}[]{#_Toc353354497}[]{#_Toc353354498}[]{#_Toc353354499}[]{#_Toc353354500}[]{#_Toc353354501}[]{#_Toc353354502}[]{#_Toc353354503}[]{#_Toc353354504}[]{#_Toc353354505}[]{#_Toc353354506}[]{#_Toc353354507}[]{#_Toc353354508}[]{#_Toc353354509}[]{#_Toc353354510}[]{#_Toc353354511}[]{#_Toc353354512}[]{#_Toc353354513}[]{#_Toc353354514}[]{#_Toc353354515}[]{#_Toc353354516}[]{#_Toc353354517}[]{#_Toc353354518}[]{#_Toc353354519}[]{#_Toc353354520}[]{#_Toc353354521}[]{#_Toc353354522}[]{#_Toc353354523}[]{#_Toc353354565}[]{#_Toc339885941}[]{#_Toc339885942}[]{#_Toc339885943}[]{#_Toc339885944}[]{#_Toc339885945}[]{#_Toc339885946}[]{#_Toc339885947}[]{#_Toc339885948}[]{#_Toc339885949}[]{#_Toc339885950}[]{#_Toc339885951}[]{#_Toc339885952}[]{#_Toc339885953}[]{#_Toc339885954}[]{#_Toc339885955}[]{#_Toc339885956}[]{#_Toc339885969}

**VPLS \-- VPLS配置命令 \-- display bgp l2vpn signaling**

------------------------------------------------------------------------

[**[display bgp l2vpn signaling]{lang="EN-US"}**]{#struct_0_10012_x1780_x1091846491}[命令用来显示]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1644066385}

[**[display bgp l2vpn signaling]{lang="EN-US"}**[ \[ **peer** *ip-address* { **advertised** \| **received** } \[ **statistics** \] \| **route-distinguisher** *route-distinguisher* \[ **site-id** *site-id* \[ **label-offset** *label-offset* \[ **advertise-info** \] \] \] \| **statistics** \]]{lang="EN-US"}]{#struct_0_10012_x1780_688460425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_691219248}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x597230063}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_107619708}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1456110567}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x481483532}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_946327632}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_144649526}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1644000849}

[**[peer]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_10012_x1780_x857624246}[：]{style="font-family:宋体"}[显示向指定对等体发布或者从指定对等体收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[advertised]{lang="EN-US"}**]{#struct_0_10012_x1780_x435216285}[：显示向指定对等体发布的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[**[received]{lang="EN-US"}**]{#struct_0_10012_x1780_728103091}[：显示从指定对等体接收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_10012_x1780_x1214620181}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块的统计信息。]{style="font-family:宋体"}

[**[route-distinguisher]{lang="EN-US"}***[ route-distinguisher]{lang="EN-US"}*]{#struct_0_10012_x1780_273565859}[：显示指定路由标识符的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[route-distinguisher]{lang="EN-US"}*[为路由标识符，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。路由标识符有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_10012_x1780_x73945686}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x1918764702}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x1643935313}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。]{style="font-family:宋体"}[例如：]{lang="EN-US" style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[site-id]{lang="EN-US"}***[ site-id]{lang="EN-US"}*]{#struct_0_10012_x1780_1231524973}[：显示为指定站点分配的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[site-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[站点编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[label-offset ]{lang="EN-US"}***[label-offset]{lang="EN-US"}*]{#struct_0_10012_x1780_x777043449}[：显示标签块偏移量为指定值的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[label-offset]{lang="EN-US"}*[为标签块偏移量]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_10012_x1780_x1477937615}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块的通告信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_943435089}

[[执行本命令时，如果没有指定任何参数，则显示所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x795397297}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1473406347}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_2128317965}[显示所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn signaling]{lang="EN-US"}]{#struct_0_10012_x1780_x1643345489}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.135]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total number of label blocks: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 2:2]{lang="EN-US"}

[ Total number of label blocks: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Site ID  LB offset  LB range  LB base    Nexthop]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  1        0          10        1034       0.0.0.0]{lang="EN-US"}

[\* \>i 2        0          10        1162       192.3.3.3]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display bgp l2vpn signaling]{lang="EN-US"}]{#struct_0_10012_x1780_x2094542639}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1775708961}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x842554094}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_1620459212}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_10012_x1780_1453280463}

[[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1643279953}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Status codes]{lang="EN-US"}]{#struct_0_10012_x1780_876486911}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1094631906}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\* - valid]{lang="EN-US"}]{#struct_0_10012_x1780_681497641}[：合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> - best]{lang="EN-US"}]{#struct_0_10012_x1780_x585641604}[：普通优选路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d - damped]{lang="EN-US"}]{#struct_0_10012_x1780_x1872053818}[：震荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h - history]{lang="EN-US"}]{#struct_0_10012_x1780_x77785833}[：历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s - suppressed]{lang="EN-US"}]{#struct_0_10012_x1780_2064670253}[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S - Stale]{lang="EN-US"}]{#struct_0_10012_x1780_x1254275182}[：过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i - internal]{lang="EN-US"}]{#struct_0_10012_x1780_x647473294}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e - external]{lang="EN-US"}]{#struct_0_10012_x1780_1243454651}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_10012_x1780_x77720297}

[[标签块信息的来源，取值包括：]{style="font-family:宋体"}]{#struct_0_10012_x1780_1211230989}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="EN-US"}]{#struct_0_10012_x1780_1828586847}[：表示产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[内]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="EN-US"}]{#struct_0_10012_x1780_1453017603}[：表示是通过]{style="font-family:宋体"}[EGP]{lang="EN-US"}[学到的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="EN-US"}]{#struct_0_10012_x1780_x581634860}[：表示来源无法确定]{lang="EN-US" style="font-family:宋体"}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_10012_x1780_x77654761}

[[所有标签块信息的总数]{style="font-family:宋体"}]{#struct_0_10012_x1780_1971603813}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_10012_x1780_x2114279073}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_x104040424}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_10012_x1780_x77589225}

[[路由标识符为指定值的标签块信息的数目]{style="font-family:宋体"}]{#struct_0_10012_x1780_x2144736203}

[[Site ID]{lang="EN-US"}]{#struct_0_10012_x1780_x631744466}

[[站点编号]{style="font-family:宋体"}]{#struct_0_10012_x1780_2045710411}

[[LB offset]{lang="EN-US"}]{#struct_0_10012_x1780_972175157}

[[标签块偏移量]{style="font-family:宋体"}]{#struct_0_10012_x1780_x78047977}

[[LB range]{lang="EN-US"}]{#struct_0_10012_x1780_621810867}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_10012_x1780_1223265304}

[[LB base]{lang="EN-US"}]{#struct_0_10012_x1780_2053953105}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_10012_x1780_x77982441}

[[Nexthop]{lang="EN-US"}]{#struct_0_10012_x1780_x1282550417}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x1576122665}[的地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1959102292}[显示路由标识符为]{style="font-family:宋体"}[1:1]{lang="EN-US"}[、为站点]{style="font-family:宋体"}[2]{lang="EN-US"}[分配的、标签块偏移量为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn signaling route-distinguisher 1:1 site-id 2 label-offset 0]{lang="EN-US"}]{#struct_0_10012_x1780_x77916905}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.140]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 1:1]{lang="EN-US"}

[ Total number of label blocks: 1]{lang="EN-US"}

[ Paths:   1 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ From            : 2.2.2.9 (192.168.1.135)]{lang="EN-US"}

[ Original nexthop: 2.2.2.9]{lang="EN-US"}

[ Ext-Community   : \<RT: 1:1\>, \<L2VPN info: MTU 1500, Encap type BGP VPLS\>]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : localpref 100, pref-val 0]{lang="EN-US"}

[ Site ID         : 2]{lang="EN-US"}

[ LB offset       : 0]{lang="EN-US"}

[ LB base         : 1418]{lang="EN-US"}

[ LB range        : 10]{lang="EN-US"}

[ State           : valid, internal, best]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display bgp l2vpn signaling]{lang="EN-US"}]{#struct_0_10012_x1780_x1642272637}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1746479329}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1761938661}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1115493704}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_10012_x1780_x77851369}

[[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x2043447551}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Local AS number]{lang="EN-US"}]{#struct_0_10012_x1780_770460040}

[[本地自治系统号]{style="font-family:宋体"}]{#struct_0_10012_x1780_113641789}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_10012_x1780_x61622579}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_x77779004}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_10012_x1780_x77261545}

[[路由标识符为指定值的标签块信息的总数]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1631952746}

[[Paths]{lang="EN-US"}]{#struct_0_10012_x1780_x2055192298}

[[标签块信息的数目：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x331096888}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_10012_x1780_x1806567311}[：有效可达信息条数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_10012_x1780_x77196009}[：最佳可达信息条数]{style="font-family:宋体"}

[[From]{lang="EN-US"}]{#struct_0_10012_x1780_41419498}

[[发布该信息的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_820595936}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Original nexthop]{lang="EN-US"}]{#struct_0_10012_x1780_1750554643}

[[原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_365122045}[更新消息中获得的标签块信息，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_10012_x1780_x77785832}

[[扩展团体属性值，包括：]{style="font-family:宋体"}]{#struct_0_10012_x1780_2064670252}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_10012_x1780_x1254340718}[：]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2VPN ]{lang="EN-US"}]{#struct_0_10012_x1780_x1159026987}[i]{lang="EN-US"}[nfo]{lang="EN-US"}[：]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[相关信息，包括]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值、封装类型（]{style="font-family:宋体"}[Encap ]{lang="EN-US"}[t]{lang="EN-US"}[ype]{lang="EN-US"}[）]{style="font-family:宋体"}

[[AS-path]{lang="EN-US"}]{#struct_0_10012_x1780_x77720296}

[[AS]{lang="EN-US"}]{#struct_0_10012_x1780_1211230988}[路径属性，记录了此标签块信息经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免环路的出现]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_10012_x1780_1828521311}

[[标签块信息的起源代码，取值包括：]{style="font-family:宋体"}]{#struct_0_10012_x1780_1454942169}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="EN-US"}]{#struct_0_10012_x1780_1627863734}[：表示可达信息来源于]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="EN-US"}]{#struct_0_10012_x1780_x77654760}[：表示可达信息通过]{style="font-family:宋体"}[EGP]{lang="EN-US"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[incomplete]{lang="EN-US"}]{#struct_0_10012_x1780_1971603814}[：表示可达信息的来源无法确定]{lang="EN-US" style="font-family:宋体"}

[[Attribute value]{lang="EN-US"}]{#struct_0_10012_x1780_x2113951393}

[[标签块信息的属性值，包括：]{style="font-family:宋体"}]{#struct_0_10012_x1780_844978716}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_10012_x1780_x77589224}[：与目的网络关联的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_10012_x1780_x2144736204}[：本地优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_10012_x1780_1290569835}[：首选值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_10012_x1780_x1449116010}[：协议优先级]{style="font-family:宋体"}

[[Site ID]{lang="EN-US"}]{#struct_0_10012_x1780_x78047976}

[[站点编号]{style="font-family:宋体"}]{#struct_0_10012_x1780_621810866}

[[LB offset]{lang="EN-US"}]{#struct_0_10012_x1780_1223265305}

[[标签块偏移量]{style="font-family:宋体"}]{#struct_0_10012_x1780_2053887569}

[[LB base]{lang="EN-US"}]{#struct_0_10012_x1780_x77982440}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1282550418}

[[LB range]{lang="EN-US"}]{#struct_0_10012_x1780_1508991050}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1226926240}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_x77916904}

[[标签块信息的当前状态，取值包括：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1642272636}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_10012_x1780_x195854720}[：有效信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_10012_x1780_x77851368}[：内部信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_10012_x1780_x2043447550}[：外部信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_10012_x1780_x795623901}[：本地产生信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_10012_x1780_525322389}[：最佳信息]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x77261544}[显示指定]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn signaling route-distinguisher 1:1 site-id 1 label-offset 0 advertise-info]{lang="EN-US"}]{#struct_0_10012_x1780_x1631952747}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.140]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 1:1]{lang="EN-US"}

[ Total number of label blocks: 1]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Site ID         : 1]{lang="EN-US"}

[ LB offset       : 0]{lang="EN-US"}

[ LB base         : 1418]{lang="EN-US"}

[ LB range        : 10]{lang="EN-US"}

[ Advertised to peers (2 in total):]{lang="EN-US"}

[    2.2.2.9]{lang="EN-US"}

[    3.3.3.9]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display bgp l2vpn signaling advertise-info]{lang="EN-US"}]{#struct_0_10012_x1780_673691057}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1755989825}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x555419585}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x77196008}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_10012_x1780_41419499}

[[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_x1518056224}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Local AS number]{lang="EN-US"}]{#struct_0_10012_x1780_x153357939}

[[本地自治系统号]{style="font-family:宋体"}]{#struct_0_10012_x1780_x474037778}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_10012_x1780_x77785835}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_2064670247}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_10012_x1780_x1254537327}

[[路由标识符为指定值的标签块信息总数]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1901865679}

[[Paths]{lang="EN-US"}]{#struct_0_10012_x1780_x167724202}

[[标签块信息的数目：]{style="font-family:宋体"}]{#struct_0_10012_x1780_1932850131}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_10012_x1780_x77720299}[：有效可达信息数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_10012_x1780_1211230987}[：最佳可达信息数目]{lang="EN-US" style="font-family:宋体"}

[[Site ID]{lang="EN-US"}]{#struct_0_10012_x1780_1828980063}

[[站点编号]{style="font-family:宋体"}]{#struct_0_10012_x1780_1086206651}

[[LB offset]{lang="EN-US"}]{#struct_0_10012_x1780_826892525}

[[标签块偏移量]{style="font-family:宋体"}]{#struct_0_10012_x1780_x77654763}

[[LB base]{lang="EN-US"}]{#struct_0_10012_x1780_1971603815}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_10012_x1780_x2113885857}

[[LB range]{lang="EN-US"}]{#struct_0_10012_x1780_x1366909018}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1295088151}

[[Advertised to peers (2 in total)]{lang="EN-US"}]{#struct_0_10012_x1780_x77589227}

[[该信息已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_10012_x1780_x2144736201}

[[ ]{lang="EN-US"}]{#_Toc336272266}

::: {#1833502486 .myid}
[]{#_Toc404791641}[]{#struct_0_10012_x1780_x1110701673}[]{#_Toc339310131}[]{#_Toc353354567}[]{#_Toc353354568}[]{#_Toc353354569}[]{#_Toc353354570}[]{#_Toc353354571}[]{#_Toc353354572}[]{#_Toc353354573}[]{#_Toc353354574}[]{#_Toc353354575}[]{#_Toc353354576}[]{#_Toc353354577}[]{#_Toc353354578}[]{#_Toc353354579}[]{#_Toc353354580}[]{#_Toc353354581}[]{#_Toc353354582}[]{#_Toc353354583}[]{#_Toc353354584}[]{#_Toc353354585}[]{#_Toc353354586}[]{#_Toc353354587}[]{#_Toc353354588}[]{#_Toc353354589}[]{#_Toc353354590}[]{#_Toc353354591}[]{#_Toc353354592}[]{#_Toc353354593}[]{#_Toc353354594}[]{#_Toc353354595}[]{#_Toc353354596}[]{#_Toc353354597}[]{#_Toc353354598}[]{#_Toc353354599}[]{#_Toc353354600}[]{#_Toc353354601}[]{#_Toc353354602}[]{#_Toc353354603}[]{#_Toc353354604}[]{#_Toc353354605}[]{#_Toc353354606}[]{#_Toc353354607}[]{#_Toc353354608}[]{#_Toc353354609}[]{#_Toc353354610}[]{#_Toc353354611}[]{#_Toc353354612}[]{#_Toc353354613}[]{#_Toc353354614}[]{#_Toc353354615}[]{#_Toc353354616}[]{#_Toc353354664}[]{#_Toc361662145}[]{#_Toc361662146}[]{#_Toc361662147}[]{#_Toc361662148}[]{#_Toc361662149}[]{#_Toc361662150}[]{#_Toc361662151}[]{#_Toc361662152}[]{#_Toc361662153}[]{#_Toc361662154}[]{#_Toc361662155}[]{#_Toc361662156}[]{#_Toc361662157}[]{#_Toc361662158}[]{#_Toc361662159}[]{#_Toc361662160}[]{#_Toc361662161}[]{#_Toc361662162}[]{#_Toc361662163}[]{#_Toc361662164}[]{#_Toc361662165}[]{#_Toc361662166}[]{#_Toc361662167}[]{#_Toc361662168}[]{#_Toc361662169}[]{#_Toc361662170}[]{#_Toc361662171}[]{#_Toc361662211}[]{#_Toc361662212}[]{#_Toc361662213}[]{#_Toc361662214}[]{#_Toc361662215}[]{#_Toc361662216}[]{#_Toc361662217}[]{#_Toc361662218}[]{#_Toc361662219}[]{#_Toc361662220}[]{#_Toc361662221}[]{#_Toc361662222}[]{#_Toc361662223}[]{#_Toc361662224}[]{#_Toc361662225}[]{#_Toc361662226}[]{#_Toc361662227}[]{#_Toc361662228}[]{#_Toc361662229}[]{#_Toc361662230}[]{#_Toc361662231}[]{#_Toc361662232}[]{#_Toc361662233}[]{#_Toc361662234}[]{#_Toc361662235}[]{#_Toc361662236}[]{#_Toc361662237}[]{#_Toc361662238}[]{#_Toc361662239}[]{#_Toc361662240}[]{#_Toc361662241}[]{#_Toc361662242}[]{#_Toc361662243}[]{#_Toc361662244}[]{#_Toc361662245}[]{#_Toc361662341}[]{#_Toc361662342}[]{#_Toc361662343}[]{#_Toc361662344}[]{#_Toc361662345}[]{#_Toc361662346}[]{#_Toc361662347}[]{#_Toc361662348}[]{#_Toc361662349}[]{#_Toc361662350}[]{#_Toc361662351}[]{#_Toc361662352}[]{#_Toc361662353}[]{#_Toc361662354}[]{#_Toc361662376}[]{#_Toc361662377}[]{#_Toc361662378}[]{#_Toc361662379}[]{#_Toc361662380}[]{#_Toc361662381}[]{#_Toc361662382}[]{#_Toc361662383}[]{#_Toc361662384}[]{#_Toc361662385}[]{#_Toc361662386}[]{#_Toc361662387}[]{#_Toc361662388}[]{#_Toc361662389}[]{#_Toc361662390}[]{#_Toc361662391}[]{#_Toc361662392}[]{#_Toc361662393}[]{#_Toc361662394}[]{#_Toc361662395}[]{#_Toc361662396}[]{#_Toc361662397}[]{#_Toc361662398}[]{#_Toc361662399}[]{#_Toc361662400}[]{#_Toc361662401}[]{#_Toc361662402}[]{#_Toc361662403}[]{#_Toc361662404}[]{#_Toc361662405}[]{#_Toc361662406}[]{#_Toc361662407}[]{#_Toc361662408}[]{#_Toc361662409}[]{#_Toc361662410}[]{#_Toc361662411}[]{#_Toc361662412}[]{#_Toc361662413}[]{#_Toc361662414}[]{#_Toc361662415}[]{#_Toc361662416}[]{#_Toc361662417}[]{#_Toc361662418}[]{#_Toc361662459}

**VPLS \-- VPLS配置命令 \-- display l2vpn auto-discovery**

------------------------------------------------------------------------

[**[display l2vpn auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_1491349933}[命令用来显示]{style="font-family:
宋体"}[VPLS]{lang="EN-US"}[的自动发现信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2010848038}

[**[display l2vpn auto-discovery ]{lang="EN-US"}**[\[ **peer** *ip-address* \] \[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_10012_x1780_x78505789}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_743743951}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_591735533}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x500411880}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_152462852}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x1621698445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1301193920}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x2010651430}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_2061888594}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_209953140}[：显示指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[自动发现相关信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定本参数，则显示自动发现的所有]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_10012_x1780_1999296436}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1906721314}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1702533157}[显示自动发现的所有]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn auto-discovery]{lang="EN-US"}]{#struct_0_10012_x1780_x1316245850}

[Total number of automatically discovered peers: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: bbb]{lang="EN-US"}

[RD                    PE_address      VPLS ID               Nexthop]{lang="EN-US"}

[2:2                   1.1.1.9         100:100               1.1.1.9]{lang="EN-US"}

[2:2                   3.3.3.9         100:100               3.3.3.9]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display l2vpn auto-discovery]{lang="EN-US"}]{#struct_0_10012_x1780_x2010716966}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1472833217}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x729411393}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_1485665787}

[[Total number of automatically discovered peers]{lang="EN-US"}]{#struct_0_10012_x1780_x1679573441}

[[自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}]{#struct_0_10012_x1780_x895314349}[数目]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_1209006132}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x2010520358}[名称]{style="font-family:宋体"}

[[RD]{lang="EN-US"}]{#struct_0_10012_x1780_416166546}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_x830830956}

[[PE address]{lang="EN-US"}]{#struct_0_10012_x1780_1783096082}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x698785633}[在]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内的标识]{style="font-family:宋体"}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1582857195}

[[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_x2010585894}[实例标识符]{style="font-family:宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_10012_x1780_1287916307}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_1893359489}[的地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1757135019}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-distinguisher]{lang="EN-US"}**]{#struct_0_10012_x1780_1222919820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpls-id]{lang="EN-US"}**]{#struct_0_10012_x1780_851004458}

::: {#1558825221 .myid}
[]{#_Toc404791642}[]{#struct_0_10012_x1780_x2010389286}[]{#_Toc339310132}

**VPLS \-- VPLS配置命令 \-- display l2vpn bgp**

------------------------------------------------------------------------

[**[display l2vpn bgp]{lang="EN-US"}**]{#struct_0_10012_x1780_x1296829357}[命令用来显示]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的标签块信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1814889605}

[**[display l2vpn bgp]{lang="EN-US"}**[ \[ **local** \| **peer** *ip-address* \] \[ **vsi** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x183290790}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_870794303}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_1958201857}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_681619643}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x2010454822}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_1296761624}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1908087885}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_271354041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1925183687}

[**[local]{lang="EN-US"}**]{#struct_0_10012_x1780_1538691466}[：只显示本地分配的标签块信息。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_x2010258214}[：显示]{style="font-family:宋体"}[从指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的标签块信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_10012_x1780_1038532292}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[块信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[标签块信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10012_x1780_x1643381321}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_491591140}

[[执行本命令时指定了]{style="font-family:宋体"}**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_400521790}[参数，如果存在与从远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的标签块匹配的本地标签块，即接收到的标签块信息中携带的远端]{style="font-family:宋体"}[Site ID]{lang="EN-US"}[满足条件：本地标签块]{style="font-family:宋体"}[LO\<=]{lang="EN-US"}[远端]{style="font-family:宋体"}[Site ID\<=]{lang="EN-US"}[本地标签块]{style="font-family:宋体"}[LO+LR-1]{lang="EN-US"}[，则同时显示远端标签块和匹配的本地标签块信息；否则，只显示从远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的标签块信息。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_x2010323750}[和]{style="font-family:宋体"}**[local]{lang="EN-US"}**[参数，则]{style="font-family:宋体"}[显示从所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的]{style="font-family:宋体"}[标签块信息。如果存在与远端标签块匹配的本地标签块，则同时显示本地标签块信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x60977738}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1135849635}[显示从所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的]{style="font-family:宋体"}[标签块的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp]{lang="EN-US"}]{#struct_0_10012_x1780_x2010782501}

[Total number of BGP PWs: 2, 2 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: aaa]{lang="EN-US"}

[Rmt Site   Offset  RD                    Nexthop          In/Out Label     State]{lang="EN-US"}

[1          0       1:1                   1.1.1.9          1419/1420        Up]{lang="EN-US"}

[3          0       1:1                   3.3.3.9          1421/1282        Up]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display l2vpn bgp]{lang="EN-US"}]{#struct_0_10012_x1780_x48863001}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1445158081}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1175567061}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_1182709509}

[[Total number of BGP PWs]{lang="EN-US"}]{#struct_0_10012_x1780_1717978836}

[[BGP PW]{lang="EN-US"}]{#struct_0_10012_x1780_x718886698}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x2010848037}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1037239458}[名称]{style="font-family:宋体"}

[[Rmt Site]{lang="EN-US"}]{#struct_0_10012_x1780_x1080670819}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x878924773}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_10012_x1780_1026413899}

[[远端标签块的偏移量]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1959554764}

[[RD]{lang="EN-US"}]{#struct_0_10012_x1780_x2010651429}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_139639829}

[[Nexthop]{lang="EN-US"}]{#struct_0_10012_x1780_x527911951}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x2117503406}[地址]{style="font-family:宋体"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_10012_x1780_531557291}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x2010716965}[的入标签和出标签值]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_x1132695920}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1505166624}[状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1693577982}[显示从所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的]{style="font-family:宋体"}[标签块的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x2010585893}

[VSI Name: aaa]{lang="EN-US"}

[ Remote Site ID     : 1]{lang="EN-US"}

[ Offset             : 0]{lang="EN-US"}

[ RD                 : 1:1]{lang="EN-US"}

[ PW State           : Up]{lang="EN-US"}

[ Encapsulation      : BGP-VPLS]{lang="EN-US"}

[ MTU                : 1500]{lang="EN-US"}

[ Nexthop            : 1.1.1.9]{lang="EN-US"}

[ Local VC Label     : 1419]{lang="EN-US"}

[ Remote VC Label    : 1420]{lang="EN-US"}

[ Link ID            : 9]{lang="EN-US"}

[ Local Label Block  : 1418/10/0]{lang="EN-US"}

[ Remote Label Block : 1418/10/0]{lang="EN-US"}

[ Export Route Target: 1:1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Remote Site ID     : 3]{lang="EN-US"}

[ Offset             : 0]{lang="EN-US"}

[ RD                 : 1:1]{lang="EN-US"}

[ PW State           : Up]{lang="EN-US"}

[ Encapsulation      : BGP-VPLS]{lang="EN-US"}

[ MTU                : 1500]{lang="EN-US"}

[ Nexthop            : 3.3.3.9]{lang="EN-US"}

[ Local VC Label     : 1421]{lang="EN-US"}

[ Remote VC Label    : 1282]{lang="EN-US"}

[ Link ID            : 10]{lang="EN-US"}

[ Local Label Block  : 1418/10/0]{lang="EN-US"}

[ Remote Label Block : 1280/10/0]{lang="EN-US"}

[ Export Route Target: 1:1]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display l2vpn bgp verbose]{lang="EN-US"}]{#struct_0_10012_x1780_2047431194}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1443983009}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_861383789}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1709992889}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x487988505}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x172842889}[名称]{style="font-family:宋体"}

[[Remote Site ID]{lang="EN-US"}]{#struct_0_10012_x1780_x405083071}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x2010389285}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_10012_x1780_x893544830}

[[远端标签块的偏移量]{style="font-family:宋体"}]{#struct_0_10012_x1780_1354692721}

[[RD]{lang="EN-US"}]{#struct_0_10012_x1780_1913469847}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1809894182}

[[PW State]{lang="EN-US"}]{#struct_0_10012_x1780_x2010454821}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_893477097}[状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Encapsulation]{lang="EN-US"}]{#struct_0_10012_x1780_2103389850}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1835020340}[数据封装类型]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_10012_x1780_330568991}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x381733604}[协商后的最大传输单元，单位为字节]{style="font-family:宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_10012_x1780_x2010258213}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_279017405}[地址]{style="font-family:宋体"}

[[Local VC Label]{lang="EN-US"}]{#struct_0_10012_x1780_687087155}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x755588116}[的入标签]{style="font-family:宋体"}

[[Remote VC Label]{lang="EN-US"}]{#struct_0_10012_x1780_x2010323749}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1861271027}[的出标签]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1683896153}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_661985033}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[Local Label Block]{lang="EN-US"}]{#struct_0_10012_x1780_x2010782504}

[[本端的标签块信息，包括标签块的初始标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10012_x1780_354421526}[标签块大小]{style="font-family:宋体"}[/]{lang="EN-US"}[标签块的偏移量]{style="font-family:宋体"}

[[Remote Label Block]{lang="EN-US"}]{#struct_0_10012_x1780_x1054155458}

[[从远端收到的标签块信息，包括标签块的初始标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10012_x1780_28949761}[标签块大小]{style="font-family:宋体"}[/]{lang="EN-US"}[标签块的偏移量]{style="font-family:宋体"}

[[Export ]{lang="EN-US"}[Route Target]{lang="EN-US"}]{#struct_0_10012_x1780_x1627770436}

[[从远端收到的标签块对应的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}]{#struct_0_10012_x1780_x2010848040}[属性]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_277921179}[显示所有本地分配的标签块的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp local]{lang="EN-US"}]{#struct_0_10012_x1780_298759087}

[VSI Name: aaa]{lang="EN-US"}

[Site   Offset  Range  Label Base    RD]{lang="EN-US"}

[2      0       10     1418          1:1]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display l2vpn bgp local]{lang="EN-US"}]{#struct_0_10012_x1780_1134455573}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1454113665}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2010651432}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_899089180}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x641532253}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1532286981}[名称]{style="font-family:宋体"}

[[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x88853886}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_784769013}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_10012_x1780_x2010716968}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x1179750087}[分配的标签块的偏移量]{style="font-family:宋体"}

[[Range]{lang="EN-US"}]{#struct_0_10012_x1780_989771952}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x787587869}[分配的标签块大小]{style="font-family:宋体"}

[[Label Base]{lang="EN-US"}]{#struct_0_10012_x1780_x193944927}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x2010520360}[分配的标签块的初始标签值]{style="font-family:宋体"}

[[RD]{lang="EN-US"}]{#struct_0_10012_x1780_59739578}

[[标签块对应的路由标识符，如果没有配置，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_10012_x1780_x200447034}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1100394700}[显示所有本地分配的标签块的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp local verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x2010585896}

[VSI Name: aaa]{lang="EN-US"}

[ Site ID            : 2]{lang="EN-US"}

[ Offset             : 0]{lang="EN-US"}

[ RD                 : 1:1]{lang="EN-US"}

[ Range              : 10]{lang="EN-US"}

[ Label Base         : 1418]{lang="EN-US"}

[ Link ID            : 8,9,10,11,12,13,14,15,16]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display l2vpn bgp local verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x1844251575}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1451637121}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1573334516}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_523502410}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_1284911531}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x2010389288}[名称]{style="font-family:宋体"}

[[Site ID]{lang="EN-US"}]{#struct_0_10012_x1780_x490260303}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_692987267}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_10012_x1780_x1874526056}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_1468045482}[分配的标签块的偏移量]{style="font-family:宋体"}

[[RD]{lang="EN-US"}]{#struct_0_10012_x1780_x2010454824}

[[标签块对应的路由标识符，如果没有配置，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_10012_x1780_490192570}["]{style="font-family:宋体"}

[[Range]{lang="EN-US"}]{#struct_0_10012_x1780_x1429777243}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_1687558412}[分配的标签块大小]{style="font-family:宋体"}

[[Label Base]{lang="EN-US"}]{#struct_0_10012_x1780_2053493237}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x2010258216}[分配的标签块的初始标签值]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x124267122}

[[标签块对应的]{style="font-family:宋体"}[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x896431079}[序列值，即基于该标签块建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[Link ID]{lang="EN-US"}[值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1885254031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_1852197405}

::: {#-821721945 .myid}
[]{#_Toc404791643}[]{#struct_0_10012_x1780_x1706429259}

**VPLS \-- VPLS配置命令 \-- display l2vpn ldp**

------------------------------------------------------------------------

[**[display l2vpn ldp]{lang="EN-US"}**]{#struct_0_10012_x1780_538424137}[命令用来显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2010323752}

[**[display l2vpn ldp ]{lang="EN-US"}**[\[ **peer** *ip-address* \[ **pw-id** *pw-id* \| **vpls-id** *vpls-id* \] \| **vsi** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x1223777152}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1090118264}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1723092040}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1619309020}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_143078786}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x955795729}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x133321817}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_1359179160}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2010782503}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_1113936413}[：显示指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。如果没有指定本参数，则显示所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*]{#struct_0_10012_x1780_x769200843}[：显示指定]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。本参数和]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[参数配合使用，如果只指定了]{style="font-family:宋体"}**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[参数，则显示指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[vpls-id ]{lang="EN-US"}***[vpls-id]{lang="EN-US"}*]{#struct_0_10012_x1780_1684545693}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[vpls-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[，即]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例标识符，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:
宋体"}[21]{lang="EN-US"}[个字符的字符串，]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_10012_x1780_x1028276772}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x567949573}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x1022430872}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。例如：]{style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x284318236}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10012_x1780_1661116340}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2010848039}

[[LDP]{lang="EN-US"}]{#struct_0_10012_x1780_1487578152}[可以通过如下两种方式通告]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签与]{style="font-family:宋体"}[PW]{lang="EN-US"}[的绑定关系：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_10012_x1780_617927156}**[peer]{lang="EN-US"}**[命令手工指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[和]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的绑定关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用]{style="font-family:宋体"}]{#struct_0_10012_x1780_340304551}[BGP]{lang="EN-US"}[协议自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[和]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的绑定关系。]{style="font-family:宋体"}

[[本命令可以用来显示通过上述两种方式通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x588094866}[标签。]{style="font-family:宋体"}

[[执行本命令时，如果指定了]{style="font-family:宋体"}**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*]{#struct_0_10012_x1780_x1841752465}[参数，则显示指定]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息；如果指定了]{style="font-family:宋体"}**[vpls-id ]{lang="EN-US"}***[vpls-id]{lang="EN-US"}*[参数，则]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息；如果没有指定]{style="font-family:宋体"}**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*[和]{style="font-family:宋体"}**[vpls-id ]{lang="EN-US"}***[vpls-id]{lang="EN-US"}*[参数，则同时显示]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式和]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1186999934}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x2010651431}[显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn ldp]{lang="EN-US"}]{#struct_0_10012_x1780_495804653}

[Total number of LDP PWs: 6, 4 up, 2 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer            PW ID/VPLS ID         In/Out Label    State Owner]{lang="EN-US"}

[192.3.3.3       1001                  775125/775126   Up    vpls1]{lang="EN-US"}

[192.3.3.3       1003                  775117/775122   Up    vpls3]{lang="EN-US"}

[192.3.3.3       1004                  775120/775120   Up    vpls4]{lang="EN-US"}

[192.3.3.3       10009                 unknown/775134  Down  vpls5]{lang="EN-US"}

[192.4.4.4       100                   775116/unknown  Down  vpls6]{lang="EN-US"}

[2.2.2.2         99:99                 775135/775125   Up    vplsauto]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display l2vpn ldp]{lang="EN-US"}]{#struct_0_10012_x1780_x38972309}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1458989313}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_1105318011}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_914147558}

[[Total number of LDP PWs]{lang="EN-US"}]{#struct_0_10012_x1780_x2010716967}

[[LDP PW]{lang="EN-US"}]{#struct_0_10012_x1780_1999471962}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_10012_x1780_x2049645684}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1267372362}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID/VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1512227549}

[[对于]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}]{#struct_0_10012_x1780_1409647552}[方式，为]{style="font-family:宋体"}[PW]{lang="EN-US"}[标识符]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[；对于]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式，为用来标识]{style="font-family:宋体"}[PE]{lang="EN-US"}[所属]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}

[[只有]{style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_x2010520359}[支持]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_10012_x1780_1982250487}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1792833452}[的入标签和出标签]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_x1724384808}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x214419368}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_x2010585895}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_10012_x1780_x1440967048}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[处于]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[Owner]{lang="EN-US"}]{#struct_0_10012_x1780_x562810863}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1139417541}[所属]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x254626110}[显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn ldp verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x2010454823}

[Peer: 2.2.2.9          PW ID: 500]{lang="EN-US"}

[  VSI Name: ccc]{lang="EN-US"}

[  PW State: Up]{lang="EN-US"}

[  PW Status Communication: Notification method]{lang="EN-US"}

[  PW ID FEC (Local/Remote):]{lang="EN-US"}

[    PW Type     : VLAN/VLAN]{lang="EN-US"}

[    Group ID    : 0/0]{lang="EN-US"}

[    Label       : 1552/1552]{lang="EN-US"}

[    Control Word: Disabled/Disabled]{lang="EN-US"}

[    VCCV CV Type: -/-]{lang="EN-US"}

[    VCCV CC Type: -/-]{lang="EN-US"}

[    MTU         : 1500/1500]{lang="EN-US"}

[    PW Status   : PW forwarding/PW forwarding]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer: 2.2.2.9          VPLS ID: 100:100]{lang="EN-US"}

[  VSI Name: bbb]{lang="EN-US"}

[  PW State: Up]{lang="EN-US"}

[  PW Status Communication: Notification method]{lang="EN-US"}

[  PW ID FEC (Local/Remote):]{lang="EN-US"}

[    Local AII   : (1.1.1.9, 2.2.2.9)]{lang="EN-US"}

[    Remote AII  : (2.2.2.9, 1.1.1.9)]{lang="EN-US"}

[    PW Type     : VLAN/VLAN]{lang="EN-US"}

[    Group ID    : 0/0]{lang="EN-US"}

[    Label       : 1553/1553]{lang="EN-US"}

[    Control Word: Disabled/Disabled]{lang="EN-US"}

[    VCCV CV Type: -/-]{lang="EN-US"}

[    VCCV CC Type: -/-]{lang="EN-US"}

[    MTU         : 1500/1500]{lang="EN-US"}

[    PW Status   : PW forwarding/PW forwarding]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer: 3.3.3.9          VPLS ID: 100:100]{lang="EN-US"}

[  VSI Name: bbb]{lang="EN-US"}

[  PW State: Up]{lang="EN-US"}

[  PW Status Communication: Notification method]{lang="EN-US"}

[  PW ID FEC (Local/Remote):]{lang="EN-US"}

[    Local AII   : (1.1.1.9, 3.3.3.9)]{lang="EN-US"}

[    Remote AII  : (3.3.3.9, 1.1.1.9)]{lang="EN-US"}

[    PW Type     : VLAN/VLAN]{lang="EN-US"}

[    Group ID    : 0/0]{lang="EN-US"}

[    Label       : 1554/1416]{lang="EN-US"}

[    Control Word: Disabled/Disabled]{lang="EN-US"}

[    VCCV CV Type: -/-]{lang="EN-US"}

[    VCCV CC Type: -/-]{lang="EN-US"}

[    MTU         : 1500/1500]{lang="EN-US"}

[    PW Status   : PW forwarding/PW forwarding]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display l2vpn ldp verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x269322317}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1456475905}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x138868198}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_62883830}

[[Peer]{lang="EN-US"}]{#struct_0_10012_x1780_x2010258215}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x527551649}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID]{lang="EN-US"}]{#struct_0_10012_x1780_1847883223}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x2121413067}[标识符]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x1297193057}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x66340644}[所属]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称]{style="font-family:宋体"}

[[PW State]{lang="EN-US"}]{#struct_0_10012_x1780_x2010323751}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1505106203}[状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[PW Status Communication]{lang="EN-US"}]{#struct_0_10012_x1780_1823935744}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x831269652}[状态通知方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Notification method]{lang="EN-US"}]{#struct_0_10012_x1780_x1010101719}[：通过]{lang="EN-US" style="font-family:
  宋体"}[Notification]{lang="EN-US"}[消息通知]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Label withdraw method]{lang="EN-US"}]{#struct_0_10012_x1780_x2010782506}[：标签回收方式，即只有]{style="font-family:宋体"}[PW]{lang="EN-US"}[连接的]{style="font-family:宋体"}[AC]{lang="EN-US"}[状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时才会为该]{style="font-family:宋体"}[PW]{lang="EN-US"}[分配]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签，]{style="font-family:宋体"}[AC]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[时回收该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ]{lang="EN-US"}[标签]{style="font-family:宋体"}

[[PW ID FEC (Local/Remote)]{lang="EN-US"}]{#struct_0_10012_x1780_1517220940}

[[本地向远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_1045628266}[通告的]{style="font-family:宋体"}[PW ID FEC]{lang="EN-US"}[相关信息]{style="font-family:宋体"}[/]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通告给本地的]{style="font-family:宋体"}[PW ID FEC]{lang="EN-US"}[相关信息]{style="font-family:宋体"}

[[PW Type]{lang="EN-US"}]{#struct_0_10012_x1780_944105574}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1373373329}[数据封装类型]{style="font-family:宋体"}

[[Group ID]{lang="EN-US"}]{#struct_0_10012_x1780_x2010848042}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1440720593}[的]{style="font-family:宋体"}[Group]{lang="EN-US"}[标识符]{style="font-family:宋体"}

[[Label]{lang="EN-US"}]{#struct_0_10012_x1780_174146414}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1349488415}[标签]{style="font-family:宋体"}

[[Control Word]{lang="EN-US"}]{#struct_0_10012_x1780_x2010651434}

[[是否使能控制字功能，取值包括]{style="font-family:宋体"}]{#struct_0_10012_x1780_92520126}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_10012_x1780_x1490211578}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[使能了控制字功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_10012_x1780_x239254279}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[未使能控制字功能]{lang="EN-US" style="font-family:宋体"}

[[VCCV CV Type]{lang="EN-US"}]{#struct_0_10012_x1780_565514110}

[[支持的]{style="font-family:宋体"}[VCCV CV]{lang="EN-US"}]{#struct_0_10012_x1780_x2010716970}[（]{style="font-family:宋体"}[Connectivity Verification]{lang="EN-US"}[，连通性验证）类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP Ping]{lang="EN-US"}]{#struct_0_10012_x1780_x1535914911}[：采用]{lang="EN-US" style="font-family:宋体"}[MPLS ping]{lang="EN-US"}[检测]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD]{lang="EN-US"}]{#struct_0_10012_x1780_x1701417298}[：]{style="font-family:宋体"}[采用]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性，]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:
  宋体"}[IP/UDP]{lang="EN-US"}[ Encapsulation]{lang="EN-US"}[ ]{lang="EN-US"}[(with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Raw-BFD]{lang="EN-US"}]{#struct_0_10012_x1780_815877304}[：]{style="font-family:宋体"}[采用]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性，]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内的]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[VCCV CC Type]{lang="EN-US"}]{#struct_0_10012_x1780_x2010520362}

[[支持的]{style="font-family:宋体"}[VCCV CC]{lang="EN-US"}]{#struct_0_10012_x1780_x1103059836}[（]{style="font-family:宋体"}[Control Channel]{lang="EN-US"}[，控制通道）类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_10012_x1780_x2037931736}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_10012_x1780_1977996356}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_10012_x1780_x2010585898}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV]{lang="EN-US"}]{#struct_0_10012_x1780_x1037682521}[（]{style="font-family:宋体"}[Virtual Circuit Connectivity Verification]{lang="EN-US"}[，虚电路连通性验证）的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS OAM]{lang="EN-US"}["]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_10012_x1780_668625392}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_471983377}[的最大传输单元]{style="font-family:宋体"}

[[PW Status]{lang="EN-US"}]{#struct_0_10012_x1780_x2010389290}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x133964407}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW forwarding]{lang="EN-US"}]{#struct_0_10012_x1780_x246607732}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[可以转发报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW not forwarding]{lang="EN-US"}]{#struct_0_10012_x1780_x2010454826}[：]{lang="EN-US" style="font-family:
  宋体"}[PW]{lang="EN-US"}[不可以转发报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC receive fault]{lang="EN-US"}]{#struct_0_10012_x1780_x672606844}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[接收方向失效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC transmit fault]{lang="EN-US"}]{#struct_0_10012_x1780_1709882982}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[发送方向失效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW receive fault]{lang="EN-US"}]{#struct_0_10012_x1780_x952682061}[：]{lang="EN-US" style="font-family:
  宋体"}[PW]{lang="EN-US"}[接收方向失效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW transmit fault]{lang="EN-US"}]{#struct_0_10012_x1780_x2010258218}[：]{lang="EN-US" style="font-family:
  宋体"}[PW]{lang="EN-US"}[发送方向失效]{lang="EN-US" style="font-family:
  宋体"}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1643296896}

[[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_343527433}[实例标识符]{style="font-family:宋体"}

[[Local AII]{lang="EN-US"}]{#struct_0_10012_x1780_x2010323754}

[[本端向远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x2030346206}[发送的]{style="font-family:宋体"}[SAII]{lang="EN-US"}[（]{style="font-family:宋体"}[Source Attachment Individual Identifier]{lang="EN-US"}[，源转发实例本地标识符）和]{style="font-family:宋体"}[TAII]{lang="EN-US"}[（]{style="font-family:宋体"}[Target Attachment Individual Identifier]{lang="EN-US"}[，目的转发实例本地标识符）]{style="font-family:宋体"}

[[Remote AII]{lang="EN-US"}]{#struct_0_10012_x1780_x1601406657}

[[从远端接收到的]{style="font-family:宋体"}[SAII]{lang="EN-US"}]{#struct_0_10012_x1780_x2010782505}[和]{style="font-family:宋体"}[TAII]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-697284031 .myid}
[]{#_Toc404791644}[]{#struct_0_10012_x1780_1920505467}[]{#_Toc242067216}[]{#_Toc185927308}[]{#_Toc123026768}

**VPLS \-- VPLS配置命令 \-- display l2vpn forwarding**

------------------------------------------------------------------------

[**[display l2vpn forwarding]{lang="EN-US"}**]{#struct_0_10012_x1780_x903293594}[命令用来显示]{style="font-family:
宋体"}[L2VPN]{lang="EN-US"}[转发信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_803699740}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1865756166}

[**[display l2vpn forwarding]{lang="EN-US"}**[ { **ac** \| **pw** } \[ **vsi** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10012_x1780_1120856245}

[[分布式设备―独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10012_x1780_1696942502}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display l2vpn forwarding]{lang="EN-US"}**[ { **ac** \| **pw** } \[ **vsi** *vsi-name* \] \[ ]{lang="EN-US"}]{#struct_0_10012_x1780_1342205519}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_10012_x1780_x2010848041}[模式：]{style="font-family:宋体"}

[**[display l2vpn forwarding]{lang="EN-US"}**[ { **ac** \| **pw** } \[ **vsi** *vsi-name* \] \[ **chassis** *chassis-number* ]{lang="EN-US"}]{#struct_0_10012_x1780_1844005120}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1632115193}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x315337058}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_149309148}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_2096555018}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x593384929}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1992165299}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x2010651433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x666994761}

[**[ac]{lang="EN-US"}**]{#struct_0_10012_x1780_481817618}[：显示]{style="font-family:宋体"}[AC]{lang="EN-US"}[的转发信息。]{style="font-family:宋体"}

[**[pw]{lang="EN-US"}**]{#struct_0_10012_x1780_1854200063}[：显示]{style="font-family:宋体"}[PW]{lang="EN-US"}[的转发信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10012_x1780_1224680789}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的转发信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的转发信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x2025770074}[：显示指定单板上的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。（分布式设备―独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x2010716969}[：显示指定成员设备上的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x2149853}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_10012_x1780_1549133268}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主用主控板的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x1855172170}[：显示指定单板的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主用主控板的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x1287154788}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[转发信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10012_x1780_x1767977183}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1981116741}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1021739512}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[AC]{lang="EN-US"}[转发的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding ac]{lang="EN-US"}]{#struct_0_10012_x1780_x2010520361}

[Total number of VSIs: 1]{lang="EN-US"}

[Total number of ACs: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[AC                               VSI Name                        Link ID]{lang="EN-US"}

[GE1/0/5 srv1                     test                            3]{lang="EN-US"}

[GE1/0/5 srv2                     test                            4]{lang="EN-US"}

[GE1/0/6                          test                            5]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display l2vpn forwarding ac]{lang="EN-US"}]{#struct_0_10012_x1780_1625823519}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1434080385}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1908895575}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_410480827}

[[Total number of VSIs]{lang="EN-US"}]{#struct_0_10012_x1780_x248925614}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x2010585897}[的总数，包括没有关联]{style="font-family:宋体"}[AC]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}

[[Total number of ACs]{lang="EN-US"}]{#struct_0_10012_x1780_x278167634}

[[所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_778127618}[或指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下]{style="font-family:宋体"}[AC]{lang="EN-US"}[的总数]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_960644839}

[[接入电路，取值有如下两种：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1382554146}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层接口名称：如]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1080648368}[GE1/0/6]{lang="EN-US"}[。在三层接口下关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层接口名称和以太网服务实例：如]{style="font-family:宋体"}]{#struct_0_10012_x1780_x2010389289}[GE1/0/5 srv1]{lang="EN-US"}[。在以太网服务实例下关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_1075823638}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_807184539}[所属]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1675842206}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_x130558755}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x2010454825}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[AC]{lang="EN-US"}[转发的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding ac verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x2010323753}

[VSI Name: vpls1]{lang="EN-US"}

[  Interface: Vlan10]{lang="EN-US"}

[    Link ID      : 0]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[  Interface: GE1/0/3  Service Instance: 1]{lang="EN-US"}

[    Link ID      : 1]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[    Encapsulation: s-vid 1 to 2 15 to 16]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: vpls2]{lang="EN-US"}

[  Interface: Vlan13]{lang="EN-US"}

[    Link ID      : 0]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[    AC Attributes: Hub link]{lang="EN-US"}

[  Interface: GE1/0/3  Service Instance: 4]{lang="EN-US"}

[    Link ID      : 1]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[    AC Attributes: Hub link]{lang="EN-US"}

[    Encapsulation: untagged]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: vpls5]{lang="EN-US"}

[  Interface: Vlan14]{lang="EN-US"}

[    Link ID      : 0]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display l2vpn forwarding ac verbose]{lang="EN-US"}]{#struct_0_10012_x1780_342306789}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1431909825}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x23546166}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_63663614}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x1803503678}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_2046195720}[名称]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_10012_x1780_x444698561}

[[接入接口]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1714702742}

[[Service Instance]{lang="EN-US"}]{#struct_0_10012_x1780_x1493779317}

[[以太网服务实例，]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_10012_x1780_1443907039}[为二层接口的以太网服务实例时才显示该字段]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x444764097}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_1113997070}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[Access Mode]{lang="EN-US"}]{#struct_0_10012_x1780_10778780}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_739868778}[接入模式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_10012_x1780_x328224108}[：]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_10012_x1780_230370890}[：]{lang="EN-US" style="font-family:宋体"}[Ethernet]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[AC Attributes]{lang="EN-US"}]{#struct_0_10012_x1780_x444567489}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_x851129808}[的属性，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub link]{lang="EN-US"}]{#struct_0_10012_x1780_1862476355}[：]{lang="EN-US" style="font-family:宋体"}[VPLS Hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[hub]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke link]{lang="EN-US"}]{#struct_0_10012_x1780_1280511717}[：]{lang="EN-US" style="font-family:宋体"}[VPLS Hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[在与此]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_10012_x1780_x444633025}[关联的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[具有]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[属性时，才显示这个字段]{style="font-family:宋体"}

[[Encapsulation]{lang="EN-US"}]{#struct_0_10012_x1780_699505907}

[[以太网服务实例的报文匹配规则，]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_10012_x1780_1825186228}[为二层接口的以太网服务实例时才显示该字段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_223562377}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding pw]{lang="EN-US"}]{#struct_0_10012_x1780_x1103528582}

[Total number of VSIs: 1]{lang="EN-US"}

[Total number of PWs: 2, 2 up, 0 blocked, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name                        In/Out Label    NID        Link ID    State]{lang="EN-US"}

[aaa                             1272/1275       1034       8          Up]{lang="EN-US"}

[aaa                             1271/1273       1035       9          Up]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display l2vpn forwarding pw]{lang="EN-US"}]{#struct_0_10012_x1780_x2093121518}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1435377793}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x444436417}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_704533931}

[[Total number of VSIs]{lang="EN-US"}]{#struct_0_10012_x1780_1332953955}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x362837868}[的总数，包括没有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}

[[Total number of PWs]{lang="EN-US"}]{#struct_0_10012_x1780_x1094364669}

[[所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x444501953}[或指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下]{style="font-family:宋体"}[PW]{lang="EN-US"}[总数，以及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[blocked]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x1617001009}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1115180699}[所属]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称]{style="font-family:宋体"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_10012_x1780_1038923436}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x457078642}[的入标签和出标签]{style="font-family:宋体"}

[[NID]{lang="EN-US"}]{#struct_0_10012_x1780_707106425}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444305345}[的隧道对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[存在等价隧道时，一个]{style="font-family:宋体"}]{#struct_0_10012_x1780_1499247392}[PW]{lang="EN-US"}[会对应多个]{style="font-family:宋体"}[NID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不存在隧道，显示为]{lang="EN-US" style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_10012_x1780_1698811265}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_1172497167}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1250591864}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_x444370881}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1907953909}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[和]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}

[[其中，]{style="font-family:宋体"}[Blocked]{lang="EN-US"}]{#struct_0_10012_x1780_2079239720}[为存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，当前没有转发流量、起到备份作用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的状态；]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}[为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷的状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_579473103}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding pw verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x444174273}

[VSI Name: aaa]{lang="EN-US"}

[  Link ID: 8]{lang="EN-US"}

[    PW Type         : VLAN                  PW State : Up]{lang="EN-US"}

[    In Label        : 1272                  Out Label: 1275]{lang="EN-US"}

[    MTU             : 1500]{lang="EN-US"}

[    PW Attributes   : Main]{lang="EN-US"}

[    VCCV CC         : Router-Alert]{lang="EN-US"}

[    VCCV BFD        : Fault Detection with BFD]{lang="EN-US"}

[    Tunnel Group ID : 0x960000000]{lang="EN-US"}

[    Tunnel NHLFE IDs: 1034]{lang="EN-US"}

[  Link ID: 9]{lang="EN-US"}

[    PW Type         : VLAN                  PW State : Up]{lang="EN-US"}

[    In Label        : 1271                  Out Label: 1273]{lang="EN-US"}

[    MTU             : 1500]{lang="EN-US"}

[    PW Attributes   : Main]{lang="EN-US"}

[    VCCV CC         : Router-Alert]{lang="EN-US"}

[    VCCV BFD        : Fault Detection with BFD]{lang="EN-US"}

[    Tunnel Group ID : 0xa60000001]{lang="EN-US"}

[    Tunnel NHLFE IDs: 1035]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display l2vpn forwarding pw verbose]{lang="EN-US"}]{#struct_0_10012_x1780_729235034}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1441424417}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_1854160586}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x444239809}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_689973791}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x675762501}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_404614103}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1884642546}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[PW Type]{lang="EN-US"}]{#struct_0_10012_x1780_x1246403220}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444698560}[数据封装类型]{style="font-family:宋体"}

[[PW State]{lang="EN-US"}]{#struct_0_10012_x1780_x1714768278}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1828822484}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[和]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}

[[其中，]{style="font-family:宋体"}[Blocked]{lang="EN-US"}]{#struct_0_10012_x1780_558948401}[为存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，当前没有转发流量、起到备份作用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的状态；]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}[为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷的状态]{style="font-family:宋体"}

[[In Label]{lang="EN-US"}]{#struct_0_10012_x1780_1709128030}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444764096}[的入标签]{style="font-family:宋体"}

[[Out Label]{lang="EN-US"}]{#struct_0_10012_x1780_1114062606}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_299899887}[的出标签]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_10012_x1780_1896261124}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444567488}[协商后的最大传输单元]{style="font-family:宋体"}

[[PW Attributes]{lang="EN-US"}]{#struct_0_10012_x1780_x851064272}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x480698570}[的属性，取值包括]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Main]{lang="EN-US"}]{#struct_0_10012_x1780_x1373265835}[：主]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_10012_x1780_x1553149143}[：备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No-split-horizon]{lang="EN-US"}]{#struct_0_10012_x1780_x444633024}[：禁止水平分割]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub link]{lang="EN-US"}]{#struct_0_10012_x1780_699440371}[：]{lang="EN-US" style="font-family:宋体"}[VPLS hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[hub]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke link]{lang="EN-US"}]{#struct_0_10012_x1780_x1328554796}[：]{lang="EN-US" style="font-family:宋体"}[ VPLS hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[spoke]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[VCCV CC]{lang="EN-US"}]{#struct_0_10012_x1780_164601460}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444436416}[的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_10012_x1780_704468395}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_10012_x1780_1780397194}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_10012_x1780_x977611428}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV BFD]{lang="EN-US"}]{#struct_0_10012_x1780_x444501952}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1616935473}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with BFD]{lang="EN-US"}]{#struct_0_10012_x1780_x2115332847}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[IP/UDP]{lang="EN-US"}[ Encapsulation]{lang="EN-US"}[ ]{lang="EN-US"}[(with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with Raw-BFD]{lang="EN-US"}]{#struct_0_10012_x1780_1311058561}[：]{style="font-family:
  宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:
  宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[Tunnel Group ID]{lang="EN-US"}]{#struct_0_10012_x1780_x444305344}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1499312928}[的隧道组]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Tunnel NHLFE IDs]{lang="EN-US"}]{#struct_0_10012_x1780_x1056936036}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x349746945}[的隧道对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引列表]{style="font-family:宋体"}

[[存在等价隧道时，一个]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444370880}[会对应多个索引值]{style="font-family:宋体"}

[[如果不存在隧道，显示为]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_10012_x1780_1907888373}

[ ]{lang="EN-US"}

::: {#356357916 .myid}
[]{#_Toc404791645}[]{#struct_0_10012_x1780_x1019951169}

**VPLS \-- VPLS配置命令 \-- display l2vpn mac-address**

------------------------------------------------------------------------

[**[display l2vpn mac-address]{lang="EN-US"}**]{#struct_0_10012_x1780_53788003}[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1438833474}

[**[display l2vpn mac-address ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ **dynamic** \] \[ **count** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x79123024}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x444174272}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_729169498}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1901653915}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1687871726}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x1873024250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1916239487}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x316384250}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x395008851}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_10012_x1780_x444239808}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_10012_x1780_689908255}[：显示动态生成的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。如果不指定本参数，则显示所有类型的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。目前，只支持动态生成的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_10012_x1780_1747931631}[：显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数目。如果不指定本参数，则显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1410381642}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_868389033}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn mac-address]{lang="EN-US"}]{#struct_0_10012_x1780_x106917373}

[MAC Address      State    VSI Name                         Link ID/Name  Aging]{lang="EN-US"}

[0000-0000-000a   dynamic  vpn1                             1             Aging]{lang="EN-US"}

[0000-0000-0009   dynamic  vpn1                             2             Aging ]{lang="EN-US"}

[\-\-- 2 mac address(es) found  \-\--     ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1935454317}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项总数。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn mac-address count]{lang="EN-US"}]{#struct_0_10012_x1780_x444698563}

[2 mac address(es) found]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display l2vpn mac-address]{lang="EN-US"}]{#struct_0_10012_x1780_x1714571670}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1412023361}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1540059491}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_503664112}

[[MAC Address]{lang="EN-US"}]{#struct_0_10012_x1780_877498432}

[[MAC]{lang="EN-US"}]{#struct_0_10012_x1780_x189783516}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_x444764099}

[[MAC]{lang="EN-US"}]{#struct_0_10012_x1780_1113079566}[地址的状态，目前取值只包括]{style="font-family:宋体"}[dynamic]{lang="EN-US"}[，表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是动态学习的]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_1937782120}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1190657522}[名称]{style="font-family:宋体"}

[[Link ID/Name]{lang="EN-US"}]{#struct_0_10012_x1780_x1198994172}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x444567491}[表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项的出链路标识符，即]{style="font-family:宋体"}[AC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_10012_x1780_808355768}[用于]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[类型的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[类型的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[不支持]{style="font-family:宋体"}[Name]{lang="EN-US"}

[[Name]{lang="EN-US"}]{#struct_0_10012_x1780_x1264980353}[的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_10012_x1780_x850605519}

[[MAC]{lang="EN-US"}]{#struct_0_10012_x1780_1504226243}[地址表项是否老化，取值包括]{style="font-family:宋体"}[Aging]{lang="EN-US"}[和]{style="font-family:宋体"}[NotAging]{lang="EN-US"}

[[XX mac address(es) found]{lang="EN-US"}]{#struct_0_10012_x1780_279842149}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_575133707}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1592073237}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset l2vpn mac-address]{lang="EN-US"}**]{#struct_0_10012_x1780_x444633027}

::: {#1506055251 .myid}
[]{#_Toc404791646}[]{#struct_0_10012_x1780_699374835}[]{#_Toc300843391}[]{#_Toc300843392}

**VPLS \-- VPLS配置命令 \-- display l2vpn interface**

------------------------------------------------------------------------

[**[display l2vpn interface]{lang="EN-US"}**]{#struct_0_10012_x1780_1567462724}[命令用来显示与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1684487295}

[**[display l2vpn interface ]{lang="EN-US"}**[\[ **vsi** *vsi-name*]{lang="EN-US"}[ \| *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_10012_x1780_1306580167}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2067782847}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_992676906}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x949785856}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x444436419}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_705451435}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_359151745}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_1265419565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_581378825}

[**[vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x1994876515}[：显示与指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x2030452723}[：显示指定接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x290293832}

[[执行本命令时，如果没有指定任何参数，则显示所有与]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x444501955}[关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[本命令只能显示与]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1617132081}[关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。若要显示以太网服务实例的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息，则需要执行]{style="font-family:宋体"}**[display l2vpn service-instance]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1873314268}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1253061158}[显示所有与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn interface ]{lang="EN-US"}]{#struct_0_10012_x1780_x1305037210}

[Total number of interfaces: 4, 3 up, 1 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                Owner                           Link ID   State    Type]{lang="EN-US"}

[Vlan10                   vpls1                           0         Up       VSI]{lang="EN-US"}

[Vlan11                   vpls2                           0         Up       VSI]{lang="EN-US"}

[GE1/0/1                  vpls1                           1         Up       VSI]{lang="EN-US"}

[GE1/0/2                  vpls1                           2         Down     VSI]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display l2vpn interface]{lang="EN-US"}]{#struct_0_10012_x1780_x1943477122}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1409375393}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x444305347}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_1499116320}

[[Total number of interfaces]{lang="EN-US"}]{#struct_0_10012_x1780_122175938}

[[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_932662506}[关联的三层接口的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的接口数目]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_10012_x1780_18871151}

[[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1629793981}[关联的三层接口的名称]{style="font-family:宋体"}

[[Owner]{lang="EN-US"}]{#struct_0_10012_x1780_x444370883}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1907822837}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_1698380205}

[[接口对应]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_10012_x1780_x415278897}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_621967050}

[[接口的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_x444174275}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_10012_x1780_729628250}

[[接口对应的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_1598444975}[类型，取值包括]{style="font-family:宋体"}[VSI]{lang="EN-US"}[和]{style="font-family:宋体"}[VPWS]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1831545491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_224841082}

::: {#947157421 .myid}
[]{#_Toc404791647}[]{#struct_0_10012_x1780_1676949467}

**VPLS \-- VPLS配置命令 \-- display l2vpn pw**

------------------------------------------------------------------------

[**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_x444239811}[命令用来显示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_689449502}

[**[display]{lang="EN-US"}**[ **l2vpn** **pw** \[ **vsi** *vsi-name* \] \[ **protocol** { **bgp** \| **ldp** \| **static** } \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x331900809}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x622140680}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1361903412}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1114959058}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1240776441}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_532037569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x444698562}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x1714637206}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x434628393}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_10012_x1780_x1260419148}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**]{#struct_0_10012_x1780_1347332834}[：显示采用指定信令协议建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息。如果没有指定本参数，则显示所有协议产生的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[bgp]{lang="EN-US"}**]{#struct_0_10012_x1780_480336582}[：显示采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[作为]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息，即]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[ldp]{lang="EN-US"}**]{#struct_0_10012_x1780_222123469}[：显示采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[作为]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息，包括]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[和]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[两种方式建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[，即]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_10012_x1780_1403868346}[：显示采用静态方式建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息，即静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10012_x1780_x444764098}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_808486841}

[[开启]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1358303956}[统计功能后，可使用]{style="font-family:宋体"}**[display l2vpn pw verbose]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[PW]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1113145102}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1150197033}[显示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw]{lang="EN-US"}]{#struct_0_10012_x1780_1482097895}

[Flags: M - main, B - backup, H - hub link, S - spoke link, N - no split horizon]{lang="EN-US"}

[Total number of PWs: 5]{lang="EN-US"}

[5 up, 0 blocked, 0 down, 0 defect, 0 idle, 0 duplicate]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: aaa]{lang="EN-US"}

[Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State]{lang="EN-US"}

[2.2.2.9         2                 1420/1419       BGP     M     9        Up]{lang="EN-US"}

[3.3.3.9         3                 1421/1281       BGP     M     10       Up]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: bbb]{lang="EN-US"}

[Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State]{lang="EN-US"}

[2.2.2.9         -                 1553/1553       LDP     M     8        Up]{lang="EN-US"}

[3.3.3.9         -                 1554/1416       LDP     M     9        Up]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: ccc]{lang="EN-US"}

[Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State]{lang="EN-US"}

[2.2.2.9         500               1552/1552       LDP     M     8        Up]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display l2vpn pw]{lang="EN-US"}]{#struct_0_10012_x1780_x444567490}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1415732097}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x850539983}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x872078673}

[[Flags]{lang="EN-US"}]{#struct_0_10012_x1780_x68395840}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1246519178}[属性标记的取值]{style="font-family:宋体"}

[[Total number of PWs]{lang="EN-US"}]{#struct_0_10012_x1780_x1634650259}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444633026}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[blocked]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[、]{style="font-family:宋体"}[defect]{lang="EN-US"}[、]{style="font-family:宋体"}[idle]{lang="EN-US"}[和]{style="font-family:宋体"}[duplicate]{lang="EN-US"}[状态的]{style="font-family:宋体"}[PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_699309299}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x362327557}[名称]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_10012_x1780_2014466341}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_105177690}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID/Rmt Site]{lang="EN-US"}]{#struct_0_10012_x1780_x444436418}

[[如果是静态]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_705385899}[或]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式的]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[，则为]{style="font-family:宋体"}[PW]{lang="EN-US"}[标识符]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[；如果是]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["；如果是]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，则为远端]{style="font-family:宋体"}[Site]{lang="EN-US"}[标识符]{style="font-family:宋体"}[Rmt Site]{lang="EN-US"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_10012_x1780_2019209570}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1762928794}[的入标签和出标签]{style="font-family:宋体"}

[[Proto]{lang="EN-US"}]{#struct_0_10012_x1780_x166613549}

[[建立]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444501954}[使用的信令协议，取值包括]{style="font-family:宋体"}[LDP]{lang="EN-US"}[、]{style="font-family:宋体"}[Static]{lang="EN-US"}[和]{style="font-family:宋体"}[BGP]{lang="EN-US"}

[[Flag]{lang="EN-US"}]{#struct_0_10012_x1780_x1617066545}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_833622696}[属性标记，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}]{#struct_0_10012_x1780_566052270}[：]{lang="EN-US" style="font-family:宋体"}[Main]{lang="EN-US"}[，主]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_10012_x1780_x444305346}[：]{lang="EN-US" style="font-family:宋体"}[Backup ]{lang="EN-US"}[，备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_10012_x1780_1499181856}[：]{lang="EN-US" style="font-family:宋体"}[Hub link]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[VPLS Hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[hub]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_10012_x1780_x305798152}[：]{lang="EN-US" style="font-family:宋体"}[Spoke link]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[VPLS Hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[spoke]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_10012_x1780_x1582524838}[：]{lang="EN-US" style="font-family:宋体"}[No-split-horizon]{lang="EN-US"}[，取消水平分割]{lang="EN-US" style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_1990463266}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444370882}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_1907757301}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1801289382}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_x1314880342}[：表示该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_10012_x1780_x1315339095}[：表示该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Blocked]{lang="EN-US"}]{#struct_0_10012_x1780_x1315404631}[：表示存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，该]{style="font-family:宋体"}[PW]{lang="EN-US"}[当前没有转发流量、起到备份作用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Defect]{lang="EN-US"}]{#struct_0_10012_x1780_x1315470167}[：表示]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_10012_x1780_x1551669564}[：表示该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dup]{lang="EN-US"}]{#struct_0_10012_x1780_x1315535703}[：表示该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签与静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x444174274}[显示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x444698565}

[VSI Name: aaa]{lang="EN-US"}

[  Peer: 2.2.2.9          Remote Site: 2]{lang="EN-US"}

[    Signaling Protocol  : BGP]{lang="EN-US"}

[    Link ID             : 9          PW State : Up]{lang="EN-US"}

[    In Label            : 1420       Out Label: 1419]{lang="EN-US"}

[    MTU                 : 1500]{lang="EN-US"}

[    PW Attributes       : Main]{lang="EN-US"}

[    VCCV CC             : -]{lang="EN-US"}

[    VCCV BFD            : -]{lang="EN-US"}

[    Tunnel Group ID     : 0x800000960000000]{lang="EN-US"}

[    Tunnel NHLFE IDs    : 1038]{lang="EN-US"}

[  Peer: 3.3.3.9          Remote Site: 3]{lang="EN-US"}

[    Signaling Protocol  : BGP]{lang="EN-US"}

[    Link ID             : 10         PW State : Up]{lang="EN-US"}

[    In Label            : 1421       Out Label: 1281]{lang="EN-US"}

[    MTU                 : 1500]{lang="EN-US"}

[    PW Attributes       : Main]{lang="EN-US"}

[    VCCV CC             : -]{lang="EN-US"}

[    VCCV BFD            : -]{lang="EN-US"}

[    Tunnel Group ID     : 0x800000160000001]{lang="EN-US"}

[    Tunnel NHLFE IDs    : 1030]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: bbb]{lang="EN-US"}

[  Peer: 2.2.2.9          VPLS ID: 100:100]{lang="EN-US"}

[    Signaling Protocol  : LDP]{lang="EN-US"}

[    Link ID             : 8          PW State : Up]{lang="EN-US"}

[    In Label            : 1553       Out Label: 1553]{lang="EN-US"}

[    MTU                 : 1500]{lang="EN-US"}

[    PW Attributes       : Main]{lang="EN-US"}

[    VCCV CC             : -]{lang="EN-US"}

[    VCCV BFD            : -]{lang="EN-US"}

[    Tunnel Group ID     : 0x800000960000000]{lang="EN-US"}

[    Tunnel NHLFE IDs    : 1038]{lang="EN-US"}

[  Peer: 3.3.3.9          VPLS ID: 100:100]{lang="EN-US"}

[    Signaling Protocol  : LDP]{lang="EN-US"}

[    Link ID             : 9          PW State : Up]{lang="EN-US"}

[    In Label            : 1554       Out Label: 1416]{lang="EN-US"}

[    MTU                 : 1500]{lang="EN-US"}

[    PW Attributes       : Main]{lang="EN-US"}

[    VCCV CC             : -]{lang="EN-US"}

[    VCCV BFD            : -]{lang="EN-US"}

[    Tunnel Group ID     : 0x800000160000001]{lang="EN-US"}

[    Tunnel NHLFE IDs    : 1030]{lang="EN-US"}

[    Input statistics    : ]{lang="EN-US"}

[      Octets   : 10600]{lang="EN-US"}

[      Packets  : 100]{lang="EN-US"}

[      Errors   : 0]{lang="EN-US"}

[      Discards : 0 ]{lang="EN-US"}

[    Output statistics   : ]{lang="EN-US"}

[      Octets   : 12600]{lang="EN-US"}

[      Packets  : 100]{lang="EN-US"}

[      Errors   : 0]{lang="EN-US"}

[      Discards : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: ccc]{lang="EN-US"}

[  Peer: 2.2.2.9          PW ID: 500]{lang="EN-US"}

[    Signaling Protocol  : LDP]{lang="EN-US"}

[    Link ID             : 8          PW State : Up]{lang="EN-US"}

[    In Label            : 1552       Out Label: 1552]{lang="EN-US"}

[    MTU                 : 1500]{lang="EN-US"}

[    PW Attributes       : Main]{lang="EN-US"}

[    VCCV CC             : -]{lang="EN-US"}

[    VCCV BFD            : -]{lang="EN-US"}

[    Tunnel Group ID     : 0x800000960000000]{lang="EN-US"}

[    Tunnel NHLFE IDs    : 1038]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[display l2vpn pw verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x1714440598}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1420362881}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_1680429623}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1484634446}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x116353430}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x444764101}[名称]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_10012_x1780_x842711291}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1524201963}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID]{lang="EN-US"}]{#struct_0_10012_x1780_x70299642}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x505554178}[标识符]{style="font-family:宋体"}

[[Signaling Protocol]{lang="EN-US"}]{#struct_0_10012_x1780_267568051}

[[建立]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444567493}[使用的信令协议，取值包括]{style="font-family:宋体"}[LDP]{lang="EN-US"}[、]{style="font-family:宋体"}[Static]{lang="EN-US"}[和]{style="font-family:宋体"}[BGP]{lang="EN-US"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x850474447}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1889148961}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[PW State]{lang="EN-US"}]{#struct_0_10012_x1780_x777465219}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_55533648}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_x1315339096}[：表示该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_10012_x1780_x1315404632}[：表示该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Blocked]{lang="EN-US"}]{#struct_0_10012_x1780_x1315470168}[：表示存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，该]{style="font-family:宋体"}[PW]{lang="EN-US"}[当前没有转发流量、起到备份作用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Defect]{lang="EN-US"}]{#struct_0_10012_x1780_x1315535704}[：表示]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_10012_x1780_x1315601240}[：表示该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Duplicate]{lang="EN-US"}]{#struct_0_10012_x1780_x1315666776}[：表示该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签与静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同]{style="font-family:宋体"}

[[In Label]{lang="EN-US"}]{#struct_0_10012_x1780_700292339}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x293038421}[入标签]{style="font-family:宋体"}

[[Out Label]{lang="EN-US"}]{#struct_0_10012_x1780_337608811}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444436421}[出标签]{style="font-family:宋体"}

[[Wait to Restore Time]{lang="EN-US"}]{#struct_0_10012_x1780_704927150}

[[回切等待时间，单位为秒。如果配置不回切，显示为]{style="font-family:宋体"}[Infinite]{lang="EN-US"}]{#struct_0_10012_x1780_686923433}

[[只会在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1658718320}[同时存在的情况下显示，并且只在主]{style="font-family:宋体"}[PW]{lang="EN-US"}[上显示]{style="font-family:宋体"}

[[Remaining Time]{lang="EN-US"}]{#struct_0_10012_x1780_x817378939}

[[回切等待的剩余时间，单位为秒。回切等待定时器启动时，才会显示该字段]{style="font-family:宋体"}]{#struct_0_10012_x1780_x444501957}

[[MTU]{lang="EN-US"}]{#struct_0_10012_x1780_x1617263153}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x726980234}[协商后的最大传输单元]{style="font-family:宋体"}

[[PW ]{lang="EN-US"}[Attributes]{lang="EN-US"}]{#struct_0_10012_x1780_x263061059}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444305349}[的属性，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Main]{lang="EN-US"}]{#struct_0_10012_x1780_1500033824}[：主]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_10012_x1780_x1006260400}[：备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub link]{lang="EN-US"}]{#struct_0_10012_x1780_x658985265}[：]{lang="EN-US" style="font-family:宋体"}[VPLS Hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[hub]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke link]{lang="EN-US"}]{#struct_0_10012_x1780_x444370885}[：]{lang="EN-US" style="font-family:宋体"}[VPLS Hub-spoke]{lang="EN-US"}[组网中，]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[spoke]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No-split-horizon]{lang="EN-US"}]{#struct_0_10012_x1780_1908216053}[：取消水平分割]{lang="EN-US" style="font-family:
  宋体"}

[[VCCV CC]{lang="EN-US"}]{#struct_0_10012_x1780_x1988424347}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444174277}[的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_10012_x1780_729497178}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_10012_x1780_x602616979}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_10012_x1780_1264769756}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV BFD]{lang="EN-US"}]{#struct_0_10012_x1780_x444239813}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_689318430}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with BFD]{lang="EN-US"}]{#struct_0_10012_x1780_190057779}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[IP/UDP]{lang="EN-US"}[ Encapsulation]{lang="EN-US"}[ ]{lang="EN-US"}[(with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with Raw-BFD]{lang="EN-US"}]{#struct_0_10012_x1780_x444698564}[：]{style="font-family:
  宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:
  宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[Tunnel Group ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1714506134}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x155647773}[的隧道组]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Tunnel NHLFE IDs]{lang="EN-US"}]{#struct_0_10012_x1780_x1819032945}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444764100}[的隧道对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引列表]{style="font-family:宋体"}

[[存在等价隧道时，一个]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x842645755}[会对应多个索引值]{style="font-family:宋体"}

[[如果不存在隧道，显示为]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_10012_x1780_2005840834}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x444567492}

[[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_x850408911}[实例标识符]{style="font-family:宋体"}

[[Remote Site]{lang="EN-US"}]{#struct_0_10012_x1780_1854773088}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_x444633028}[标识符]{style="font-family:宋体"}

[[Input statistics]{lang="EN-US"}]{#struct_0_10012_x1780_808748982}

[[入方向的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_808683446}[转发统计信息，包括入方向接收的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、接收的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、接收的错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ Output statistics]{lang="EN-US"}]{#struct_0_10012_x1780_1602118769}

[[出方向的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1605224616}[转发统计信息，包括出方向发送的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、发送的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、发送的错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_808224695}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[statistics enable]{lang="EN-US"}**]{#struct_0_10012_x1780_x58099088}

::: {#365063371 .myid}
[]{#_Toc404791648}[]{#struct_0_10012_x1780_700226803}

**VPLS \-- VPLS配置命令 \-- display l2vpn pw-class**

------------------------------------------------------------------------

[**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_62435067}[命令用来显示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1614841971}

[**[display l2vpn pw-class]{lang="EN-US"}**[ \[ *class-name* \]]{lang="EN-US"}]{#struct_0_10012_x1780_x1340705267}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_708699455}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x367185602}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x562272312}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x444436420}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_704861614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x859411068}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_152731124}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1689409375}

[*[class-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x881383190}[：显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1762013193}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1120353314}[显示所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw-class ]{lang="EN-US"}]{#struct_0_10012_x1780_x444501956}

[Total number of PW classes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[PW Class Name       PW Type              Control Word   VCCV CC        VCCV BFD]{lang="EN-US"}

[pw1                 Ethernet             Enabled        Control-Word   Raw-BFD]{lang="EN-US"}

[pw2                 VLAN                 Disabled       Router-Alert   BFD]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[display l2vpn pw-class]{lang="EN-US"}]{#struct_0_10012_x1780_x1617197617}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1425067105}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x954579682}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x975560017}

[[Total number of PW classes]{lang="EN-US"}]{#struct_0_10012_x1780_1512899169}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x444305348}[模板的总数]{style="font-family:宋体"}

[[PW Class Name]{lang="EN-US"}]{#struct_0_10012_x1780_1500099360}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x315802270}[模板的名称]{style="font-family:宋体"}

[[PW Type]{lang="EN-US"}]{#struct_0_10012_x1780_945089000}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x109886559}[数据封装类型，取值包括]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Control Word]{lang="EN-US"}]{#struct_0_10012_x1780_x527049961}

[[是否使能控制字功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_10012_x1780_x444370884}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[VCCV CC]{lang="EN-US"}]{#struct_0_10012_x1780_1908150517}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1584061492}[的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_10012_x1780_x875790862}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_10012_x1780_220988064}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_10012_x1780_x444174276}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV BFD]{lang="EN-US"}]{#struct_0_10012_x1780_729431642}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1337075706}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with BFD]{lang="EN-US"}]{#struct_0_10012_x1780_1759170068}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[IP/UDP]{lang="EN-US"}[ Encapsulation]{lang="EN-US"}[ ]{lang="EN-US"}[(with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with Raw-BFD]{lang="EN-US"}]{#struct_0_10012_x1780_x444239812}[：]{style="font-family:
  宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:
  宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_689252894}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_232887687}

::: {#-1122099741 .myid}
[]{#_Toc404791649}[]{#struct_0_10012_x1780_586693928}[]{#_Toc300843396}

**VPLS \-- VPLS配置命令 \-- display l2vpn service-instance**

------------------------------------------------------------------------

[**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_x1632628356}[命令用来显示以太网服务实例的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1704849616}

[**[display l2vpn service-instance ]{lang="EN-US"}**[\[ **interface**]{lang="EN-US"}*[ interface-type interface-number]{lang="EN-US"}*[ \[ **service-instance** *instance-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x1483654059}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x237247520}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_1121385380}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1823877590}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x2050524496}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_1584863514}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1858731569}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x62305753}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x204436517}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x179250537}[：显示指定二层以太网接口或二层聚合接口上的以太网服务实例信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则显示所有二层以太网接口和二层聚合接口上的以太网服务实例信息。]{style="font-family:
宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_10012_x1780_1121319844}[：显示指定以太网服务实例的信息。]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。如果指定了]{style="font-family:宋体"}**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*[参数，没有指定本参数，则显示指定二层以太网接口或二层聚合接口上所有以太网服务实例的信息。]{style="font-family:
宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10012_x1780_1296125298}[：显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x338774440}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1567223738}[显示所有以太网服务实例的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance]{lang="EN-US"}]{#struct_0_10012_x1780_1244759177}

[Total number of service-instances: 8, 8 up, 0 down]{lang="EN-US"}

[Total number of ACs: 4, 4 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                SrvID Owner                           LinkID State Type]{lang="EN-US"}

[GE1/0/3                  1     vpls1                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  2     vpls2                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  3     vpls3                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  4     vpls4                           1      Up    VSI]{lang="EN-US"}

[GE1/0/3                  5                                            Up]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[display l2vpn service-instance]{lang="EN-US"}]{#struct_0_10012_x1780_1121516452}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1395319393}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_2107722244}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x708956648}

[[Total number of service-instances]{lang="EN-US"}]{#struct_0_10012_x1780_220322552}

[[以太网服务实例的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_10012_x1780_x449683924}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的以太网服务实例数目]{style="font-family:宋体"}

[[Total number of ACs]{lang="EN-US"}]{#struct_0_10012_x1780_1522769139}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_1121450916}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[AC]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_10012_x1780_158282587}

[[二层以太网接口或二层聚合接口名称]{style="font-family:宋体"}]{#struct_0_10012_x1780_1012645239}

[[SrvID ]{lang="EN-US"}]{#struct_0_10012_x1780_997155505}

[[以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_10012_x1780_570273882}

[[Owner]{lang="EN-US"}]{#struct_0_10012_x1780_1121647524}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1799700735}[名称，如果以太网服务实例上尚未关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，则本字段显示为空]{style="font-family:宋体"}

[[LinkID]{lang="EN-US"}]{#struct_0_10012_x1780_1311798751}

[[以太网服务实例对应]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_10012_x1780_x1196381791}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_535649252}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_1121581988}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_10012_x1780_x1409439776}

[[以太网服务实例所属的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_1278121670}[类型，取值包括]{style="font-family:宋体"}[VSI]{lang="EN-US"}[和]{style="font-family:宋体"}[VPWS]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1593622608}[显示二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[上所有以太网服务实例的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/3 verbose]{lang="EN-US"}]{#struct_0_10012_x1780_1121778596}

[Interface: GE1/0/3]{lang="EN-US"}

[  Service Instance: 1]{lang="EN-US"}

[    Encapsulation : s-vid 1 to 16]{lang="EN-US"}

[    VSI Name      : vpls1]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 2]{lang="EN-US"}

[    Encapsulation : s-vid 1001 to 1016]{lang="EN-US"}

[                    only-tagged]{lang="EN-US"}

[    VSI Name      : vpls2]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 3]{lang="EN-US"}

[    Encapsulation : s-vid 2000]{lang="EN-US"}

[                    c-vid 1001 to 1002 1015 to 1016]{lang="EN-US"}

[    VSI Name      : vpls3]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[[表1-24 ]{lang="EN-US"}[display l2vpn service-instance verbose]{lang="EN-US"}]{#struct_0_10012_x1780_1283250256}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1394458497}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1770555465}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_x788252325}

[[Interface]{lang="EN-US"}]{#struct_0_10012_x1780_1121713060}

[[二层以太网接口或二层聚合接口]{style="font-family:宋体"}]{#struct_0_10012_x1780_x663187114}

[[Service Instance]{lang="EN-US"}]{#struct_0_10012_x1780_x1209052932}

[[以太网服务实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_10012_x1780_x698899012}

[[Encapsulation]{lang="EN-US"}]{#struct_0_10012_x1780_1183452470}

[[以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则不显示本字段]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1857319499}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_1121909668}

[[与以太网服务实例关联的]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1846260690}[的名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1796067979}

[[以太网服务实例对应]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_10012_x1780_x755771634}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_x723943923}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_1121844132}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x631611283}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_x1516671423}

::: {#-1007637280 .myid}
[]{#_Toc404791650}[]{#struct_0_10012_x1780_x1575070222}[]{#_Toc300843398}

**VPLS \-- VPLS配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

[**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_x1771040467}[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1266247799}

[**[display]{lang="EN-US"}**[ **l2vpn** **vsi** \[ **name** *vsi-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_10012_x1780_372999234}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x61860984}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_1121385381}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1823812054}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1224158121}

[[network-operator]{lang="EN-US"}]{#struct_0_10012_x1780_x2045650793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x409044861}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10012_x1780_923058920}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1852990173}

[**[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x975363091}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_10012_x1780_1121319845}[：显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1296059762}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_68108096}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi]{lang="EN-US"}]{#struct_0_10012_x1780_1146561736}

[Total number of VSIs: 2, 1 up, 1 down, 0 admin down]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name                        VSI Index       MTU    State]{lang="EN-US"}

[vpls1                           0               1500   Up]{lang="EN-US"}

[vpls2                           1               1500   Down]{lang="EN-US"}

[[表1-25 ]{lang="EN-US"}[display l2vpn vsi]{lang="EN-US"}]{#struct_0_10012_x1780_1399109581}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1400329601}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1042727149}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121516453}

[[Total number of VSIs]{lang="EN-US"}]{#struct_0_10012_x1780_2107656708}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1505230623}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[和]{style="font-family:宋体"}[admin down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_1927574907}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x2090311471}[名称]{style="font-family:宋体"}

[[VSI Index]{lang="EN-US"}]{#struct_0_10012_x1780_1121450917}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_158217051}[索引]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_10012_x1780_x932022447}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1432013537}[上配置的最大传输单元]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_464816567}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x870788961}[的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_1121647525}[：]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_10012_x1780_x1799635199}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Admin down]{lang="EN-US"}]{#struct_0_10012_x1780_1207625982}[：通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令手工关闭]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_853568183}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi verbose]{lang="EN-US"}]{#struct_0_10012_x1780_1121581989}

[VSI Name: vpls1]{lang="EN-US"}

[  VSI Index               : 0]{lang="EN-US"}

[  VSI Description         : vsi for vpls1]{lang="EN-US"}

[  VSI State               : Up]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : Unlimited]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  LDP PWs:]{lang="EN-US"}

[    Peer            PW ID            Link ID    State]{lang="EN-US"}

[    192.3.3.3       1                8          Up]{lang="EN-US"}

[    192.3.3.3       1001             8          Blocked]{lang="EN-US"}

[  BGP PWs:]{lang="EN-US"}

[    Peer            Remote Site      Link ID    State]{lang="EN-US"}

[    192.4.4.4       1                9          Up]{lang="EN-US"}

[  ACs:]{lang="EN-US"}

[    AC                               Link ID    State]{lang="EN-US"}

[    Vlan10                           0          Up]{lang="EN-US"}

[    GE1/0/3 srv1                     1          Up]{lang="EN-US"}

[[表1-26 ]{lang="EN-US"}[display l2vpn vsi verbose]{lang="EN-US"}]{#struct_0_10012_x1780_x1409374240}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1398297697}[[字段]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121778597}

[[描述]{style="font-family:黑体"}]{#struct_0_10012_x1780_1283184720}

[[VSI Name]{lang="EN-US"}]{#struct_0_10012_x1780_x1025160771}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1143552466}[名称]{style="font-family:宋体"}

[[VSI Index]{lang="EN-US"}]{#struct_0_10012_x1780_x681354761}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1975850766}[索引]{style="font-family:宋体"}

[[VSI Description]{lang="EN-US"}]{#struct_0_10012_x1780_1121713061}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x663252650}[的描述信息，如果不配置，则此行不显示]{style="font-family:宋体"}

[[VSI State]{lang="EN-US"}]{#struct_0_10012_x1780_782895572}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1634288268}[的状态，取值包括]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_10012_x1780_348729271}[：]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_10012_x1780_1121909669}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_10012_x1780_x1846195154}[：通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令手工关闭]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}

[[MTU]{lang="EN-US"}]{#struct_0_10012_x1780_x2085557133}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1237813119}[上配置的最大传输单元]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_10012_x1780_1121844133}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1121385378}[的最大带宽值，单位为]{style="font-family:宋体"}[kbps ]{lang="EN-US"}

[[Broadcast Restrain]{lang="EN-US"}]{#struct_0_10012_x1780_x1823353295}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x2094804566}[的广播抑制百分比]{style="font-family:宋体"}

[[Multicast Restrain]{lang="EN-US"}]{#struct_0_10012_x1780_1121319842}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1295994226}[的组播抑制百分比]{style="font-family:宋体"}

[[Unknown Unicast Restrain]{lang="EN-US"}]{#struct_0_10012_x1780_x1411634704}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x179262296}[的未知单播抑制百分比]{style="font-family:宋体"}

[[MAC Learning]{lang="EN-US"}]{#struct_0_10012_x1780_1121516450}

[[是否使能了]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_10012_x1780_2107591172}[地址学习功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_10012_x1780_1198820392}[：使能了]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_10012_x1780_x2124785748}[：未使能]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能]{lang="EN-US" style="font-family:宋体"}

[[MAC Tabel Limit]{lang="EN-US"}]{#struct_0_10012_x1780_1121450914}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_158151515}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}]{#struct_0_10012_x1780_713080272}[，表示不限制]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[Drop Unknown]{lang="EN-US"}]{#struct_0_10012_x1780_x1677269551}

[[当]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1121647522}[内学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，是否禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_10012_x1780_x1799569663}[：表示禁止转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_10012_x1780_665930006}[：表示允许转发]{lang="EN-US" style="font-family:宋体"}

[[Hub-Spoke]{lang="EN-US"}]{#struct_0_10012_x1780_1947928302}

[[是否使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}]{#struct_0_10012_x1780_1121581986}[能力。取值为]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[，表示使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[能力；如果未使能]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[能力，则不显示此字段]{style="font-family:宋体"}

[[LDP PWs]{lang="EN-US"}]{#struct_0_10012_x1780_x1409832992}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1724660632}[的]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[Static PWs]{lang="EN-US"}]{#struct_0_10012_x1780_1121778594}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1283381328}[的静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[BGP PWs]{lang="EN-US"}]{#struct_0_10012_x1780_x1386025934}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1121713058}[的]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_10012_x1780_x663711403}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1572366847}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID]{lang="EN-US"}]{#struct_0_10012_x1780_x424891688}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1121909666}[标识符]{style="font-family:宋体"}

[[Remote Site]{lang="EN-US"}]{#struct_0_10012_x1780_x1845605330}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_10012_x1780_2103778587}[标识符]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_1121844130}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x631480211}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_1190650515}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1121385379}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[和]{style="font-family:宋体"}[Defect]{lang="EN-US"}

[[ACs]{lang="EN-US"}]{#struct_0_10012_x1780_x1823287759}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1425214790}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_1121319843}

[[接入电路，取值有如下两种：]{style="font-family:宋体"}]{#struct_0_10012_x1780_1295928690}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层接口名称：如]{style="font-family:宋体"}]{#struct_0_10012_x1780_989704887}[GE1/0/4]{lang="EN-US"}[。在三层接口下关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层接口名称和以太网服务实例：如]{style="font-family:宋体"}]{#struct_0_10012_x1780_1121516451}[GE1/0/3 srv1]{lang="EN-US"}[。在以太网服务实例下关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_10012_x1780_2107525636}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_448814736}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_10012_x1780_1121450915}

[[AC]{lang="EN-US"}]{#struct_0_10012_x1780_158085979}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_786187829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_x94529939}

::: {#-900899430 .myid}
[]{#_Toc404791651}[]{#struct_0_10012_x1780_1121647523}[]{#_Toc288911611}[]{#_Toc203551099}

**VPLS \-- VPLS配置命令 \-- encapsulation**

------------------------------------------------------------------------

[**[encapsulation]{lang="EN-US"}**]{#struct_0_10012_x1780_x1799504127}[命令用来配置以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_10012_x1780_x1288806629}[命令用来删除以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_602725896}

[**[encapsulation]{lang="EN-US"}**[ **c-vid** { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_10012_x1780_296860403}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** { *vlan-id* \| *vlan-id-list* } \[ **only-tagged** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x1671554568}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_10012_x1780_x1688822039}

[**[encapsulation]{lang="EN-US"}**[ { **default** \| **tagged** \| **untagged** }]{lang="EN-US"}]{#struct_0_10012_x1780_1913831868}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_10012_x1780_2139590536}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121581987}

[[未配置任何报文匹配规则。]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1409767456}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_833648052}

[[以太网服务实例视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x285069762}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_67179463}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_365616576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x989997726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1375314718}

[**[c-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_10012_x1780_1121778595}[：匹配内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Customer VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_10012_x1780_1283315792}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_10012_x1780_1718861461}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ to *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_10012_x1780_x1990815865}[：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Service VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_10012_x1780_x1346392280}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_10012_x1780_1593840833}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[only-tagged]{lang="EN-US"}**]{#struct_0_10012_x1780_x1946462297}[：表示只匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。当匹配的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，如果未指定本关键字，则会同时匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文和未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文；如果指定了本参数，则只匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_10012_x1780_x961752343}[：匹配指定外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签和内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_10012_x1780_1121713059}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_10012_x1780_x663776939}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[al]{lang="EN-US"}**]{#struct_0_10012_x1780_x1137976059}**[l]{lang="EN-US"}**[表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_10012_x1780_94111305}[：表示缺省的报文匹配规则。]{style="font-family:宋体"}

[**[tagged]{lang="EN-US"}**]{#struct_0_10012_x1780_x1971980719}[：表示匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[untagged]{lang="EN-US"}**]{#struct_0_10012_x1780_374508110}[：表示匹配未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x24137746}

[[当同一个接口下配置的不同以太网服务实例的报文匹配规则出现重叠时，如何匹配报文与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1998337556}

[[同一个以太网接口下可以创建多个服务实例，但是最多只能有一个服务实例采用缺省的报文匹配规则（]{style="font-family:宋体"}**[encapsulation default]{lang="EN-US"}**]{#struct_0_10012_x1780_1121909667}[）。如果接口下同时存在一个采用缺省报文匹配规则的服务实例和多个采用其他报文匹配规则的服务实例，则没有与任何其他报文匹配规则匹配的报文将匹配缺省报文匹配规则；如果接口下只存在一个采用缺省报文匹配规则的服务实例，则该接口上的所有报文都匹配缺省报文匹配规则。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1845539794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个以太网服务实例视图下，不能重复执行本命令。]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1334240264}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例]{style="font-family:宋体"}]{#struct_0_10012_x1780_1860748174}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的关联。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[内层]{style="font-family:宋体"}]{#struct_0_10012_x1780_1078636186}[VLAN]{lang="EN-US"}[标签和外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的介绍请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[QinQ]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1456148369}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1910319712}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[上配置如下报文匹配规则：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[111]{lang="EN-US"}[，内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[20]{lang="EN-US"}[、]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1121844131}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\] encapsulation s-vid 111 c-vid 20 30 to 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x631414675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_x1878192083}
:::

::: {#2070950537 .myid}
[]{#_Toc404791652}[]{#struct_0_10012_x1780_362993132}

**VPLS \-- VPLS配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_10012_x1780_1705352943}[命令用来使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_10012_x1780_x612812070}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x566760983}

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_10012_x1780_x261873298}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_10012_x1780_1121385376}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1823746511}

[[L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x1930873648}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x248553133}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x252404589}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x433315803}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1048208597}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1590903105}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121319840}

[[只有使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_1295863154}[功能后，才能进行]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1745356329}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1379596398}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1040519153}

[\[Sysname\] l2vpn enable]{lang="EN-US"}
:::

::::: {#-1924536592 .myid}
[]{#_Toc404791653}[]{#struct_0_10012_x1780_x1151500423}[]{#_Toc302467222}[]{#_Toc360712346}[]{#_Toc361311813}[]{#_Toc361311893}[]{#_Toc361662472}[]{#_Toc360712347}[]{#_Toc361311814}[]{#_Toc361311894}[]{#_Toc361662473}[]{#_Toc360712348}[]{#_Toc361311815}[]{#_Toc361311895}[]{#_Toc361662474}[]{#_Toc360712349}[]{#_Toc361311816}[]{#_Toc361311896}[]{#_Toc361662475}[]{#_Toc360712350}[]{#_Toc361311817}[]{#_Toc361311897}[]{#_Toc361662476}[]{#_Toc360712351}[]{#_Toc361311818}[]{#_Toc361311898}[]{#_Toc361662477}[]{#_Toc360712352}[]{#_Toc361311819}[]{#_Toc361311899}[]{#_Toc361662478}[]{#_Toc360712353}[]{#_Toc361311820}[]{#_Toc361311900}[]{#_Toc361662479}[]{#_Toc360712354}[]{#_Toc361311821}[]{#_Toc361311901}[]{#_Toc361662480}[]{#_Toc360712355}[]{#_Toc361311822}[]{#_Toc361311902}[]{#_Toc361662481}[]{#_Toc360712356}[]{#_Toc361311823}[]{#_Toc361311903}[]{#_Toc361662482}[]{#_Toc360712357}[]{#_Toc361311824}[]{#_Toc361311904}[]{#_Toc361662483}[]{#_Toc360712358}[]{#_Toc361311825}[]{#_Toc361311905}[]{#_Toc361662484}[]{#_Toc360712359}[]{#_Toc361311826}[]{#_Toc361311906}[]{#_Toc361662485}[]{#_Toc360712360}[]{#_Toc361311827}[]{#_Toc361311907}[]{#_Toc361662486}[]{#_Toc360712361}[]{#_Toc361311828}[]{#_Toc361311908}[]{#_Toc361662487}[]{#_Toc360712362}[]{#_Toc361311829}[]{#_Toc361311909}[]{#_Toc361662488}[]{#_Hlt24806852}[]{#_Toc360712363}[]{#_Toc361311830}[]{#_Toc361311910}[]{#_Toc361662489}[]{#_Toc360712364}[]{#_Toc361311831}[]{#_Toc361311911}[]{#_Toc361662490}[]{#_Toc360712365}[]{#_Toc361311832}[]{#_Toc361311912}[]{#_Toc361662491}[]{#_Toc360712366}[]{#_Toc361311833}[]{#_Toc361311913}[]{#_Toc361662492}[]{#_Toc360712367}[]{#_Toc361311834}[]{#_Toc361311914}[]{#_Toc361662493}[]{#_Toc360712368}[]{#_Toc361311835}[]{#_Toc361311915}[]{#_Toc361662494}[]{#_Toc360712369}[]{#_Toc361311836}[]{#_Toc361311916}[]{#_Toc361662495}[]{#_Toc360712370}[]{#_Toc361311837}[]{#_Toc361311917}[]{#_Toc361662496}

**VPLS \-- VPLS配置命令 \-- l2vpn switchover**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](VPLS命令.files/image001.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_x881541775}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_x1005733527}
:::

**[ ]{lang="EN-US"}**

[**[l2vpn switchover]{lang="EN-US"}**]{#struct_0_10012_x1780_1121581984}[命令用来将指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的流量手工倒换到它的冗余备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1409701920}

[**[l2vpn switchover peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_10012_x1780_x1979270035}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2010304584}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1999779010}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1825507190}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_214679211}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_636702207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121778592}

[**[peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_1283512400}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}]{#struct_0_10012_x1780_x1777300071}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1639394445}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1491819560}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识了一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[。如果该]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在对应的可用主]{style="font-family:宋体"}[PW]{lang="EN-US"}[或备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则执行本命令后，通过该]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发的流量将倒换到另一条可用的主]{style="font-family:宋体"}[PW]{lang="EN-US"}[或备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[上转发；如果不存在对应的可用主]{style="font-family:宋体"}[PW]{lang="EN-US"}[和备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则不进行流量倒换。]{style="font-family:宋体"}

[[本命令是]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1915764280}[保护倒换的手工倒换命令，用来方便管理员对网络流量进行管理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_772396840}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_690798618}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[、]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，将该]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的流量手工倒换到它的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[上转发。]{style="font-family:宋体"}

[[\<Sysname\> l2vpn switchover peer 3.3.3.3 pw-id 100]{lang="EN-US"}]{#struct_0_10012_x1780_1121713056}
:::::

::::: {#1058776332 .myid}
[]{#_Toc404791654}[]{#struct_0_10012_x1780_x662793899}

**VPLS \-- VPLS配置命令 \-- mac-learning enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](VPLS命令.files/image001.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_791772990}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_x542958825}
:::

**[ ]{lang="EN-US"}**

[**[mac-learning enable]{lang="EN-US"}**]{#struct_0_10012_x1780_1786754700}[命令用来开启]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[**[undo mac-learning]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_10012_x1780_x617461380}[命令用来关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_775708169}

[**[mac-learning enable]{lang="EN-US"}**]{#struct_0_10012_x1780_1576441592}

[**[undo mac-learning enable]{lang="EN-US"}**]{#struct_0_10012_x1780_1121909664}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1845474258}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x2109071421}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x386834001}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_479467482}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x306702631}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x110360494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x220016059}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121844128}

[[如果关闭了]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x630955922}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能，则设备接收到该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的报文后不会学习该报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_104242162}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1496758255}[关闭名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x431836295}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] undo mac-learning enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_187693544}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1572704693}
:::::

::::: {#-265759702 .myid}
[]{#_Toc404791655}[]{#struct_0_10012_x1780_x556370204}

**VPLS \-- VPLS配置命令 \-- mac-learing rate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VPLS命令.files/image003.png){#图片 8 width="61" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_1009713737}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_482979569}
:::

[ ]{lang="EN-US"}

[**[mac-learning rate]{lang="EN-US"}**]{#struct_0_10012_x1780_1896661352}[命令用来配置当前]{style="font-family:宋体"}[VSI]{lang="EN-US"}[学习单个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的时间间隔。]{style="font-family:宋体"}

[**[undo mac-learning rate]{lang="EN-US"}**]{#struct_0_10012_x1780_297919435}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1524761972}

[**[mac-learning]{lang="EN-US"}**[ **rate** *interva[l]{style="color:black"}*]{lang="EN-US"}]{#struct_0_10012_x1780_358055413}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[mac-learning]{lang="EN-US"}**[ **rate**]{lang="EN-US"}]{#struct_0_10012_x1780_1886142909}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1348039139}

[[学习单个]{style="font-family:宋体;color:black"}[MAC]{lang="EN-US" style="color:black"}]{#struct_0_10012_x1780_x1719169618}[地址的时间间隔为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[，即不限制]{style="font-family:宋体;color:black"}[MAC]{lang="EN-US" style="color:black"}[地址的学习速率]{style="font-family:宋体;
color:black"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1690213751}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1851157796}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1123087534}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x10698938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1538788162}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x241452661}

[*[interval]{lang="EN-US"}*]{#struct_0_10012_x1780_x2024593378}[：指定当前]{style="font-family:宋体"}[VSI]{lang="EN-US"}[学习单个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体;color:black"}[1000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[]{#struct_0_10012_x1780_x153085677}[]{#_GoBack}[【使用指导】]{style="font-family:黑体"}

[[通过配置学习单个]{style="font-family:宋体;color:black"}[MAC]{lang="EN-US"}]{#struct_0_10012_x1780_641575579}[地址的时间间隔，可对特定]{style="font-family:宋体;color:black"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习速率进行限制，以防止在短时间内学习过多的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，占用过多的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项资源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_205341793}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x250681126}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[学习单个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x356024786}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] mac-learning rate 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1800019761}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1412998264}
:::::

::::: {#2005444103 .myid}
[]{#_Toc404791656}[]{#struct_0_10012_x1780_1627260696}

**VPLS \-- VPLS配置命令 \-- mac-table limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](VPLS命令.files/image001.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_1121385377}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_x1823680975}
:::

[ ]{lang="EN-US"}

[**[mac-table limit]{lang="EN-US"}**]{#struct_0_10012_x1780_x1398499836}[命令用来配置允许]{style="font-family:宋体"}[VSI]{lang="EN-US"}[学习到的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数。]{style="font-family:宋体"}

[**[undo mac-table limit]{lang="EN-US"}**]{#struct_0_10012_x1780_x199665301}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1370454984}

[**[mac-table]{lang="EN-US"}**[ **limit** *mac-limit*]{lang="EN-US"}]{#struct_0_10012_x1780_7558655}

[**[undo mac-table]{lang="EN-US"}**[ **limit**]{lang="EN-US"}]{#struct_0_10012_x1780_1654771073}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1878437901}

[[不对]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1121319841}[学习到的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数进行限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1295797618}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x243282712}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_957622133}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_212917812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x844182572}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1878599568}

[*[mac-limit]{lang="EN-US"}*]{#struct_0_10012_x1780_320412395}[：允许]{style="font-family:宋体"}[VSI]{lang="EN-US"}[学习到的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121516449}

[[通常情况下，设备上能够保存的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_10012_x1780_2107001347}[地址表项数目具有一定的限制。本命令可以控制单个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数，以避免某个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项过多，占用过多的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项资源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_840207368}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_623954144}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[允许学习到的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数为]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x986480078}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] mac-table limit 1024]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1180416785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1729068549}
:::::

::::: {#213543152 .myid}
[]{#_Toc404791657}[]{#struct_0_10012_x1780_1121450913}

**VPLS \-- VPLS配置命令 \-- mac-table limit drop-unknown**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](VPLS命令.files/image004.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_158479195}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_1269689254}
:::

**[ ]{lang="EN-US"}**

[**[mac-table limit drop-unknown]{lang="EN-US"}**]{#struct_0_10012_x1780_x906747064}[命令用来配置当]{style="font-family:
宋体"}[VSI]{lang="EN-US"}[学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文，即丢弃该报文。对于源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文，进行正常转发。]{style="font-family:宋体"}

[**[undo mac-table limit ]{lang="EN-US"}[drop-unknown]{lang="EN-US"}**]{#struct_0_10012_x1780_133451604}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x508875970}

[**[mac-table limit drop-unknown]{lang="EN-US"}**]{#struct_0_10012_x1780_699873515}

[**[undo ]{lang="EN-US"}[mac-table limit drop-unknown]{lang="EN-US"}**]{#struct_0_10012_x1780_x1649436691}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121647521}

[[当]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1799373055}[学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，允许转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文，但是不会学习报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1099492557}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1212641006}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1854107576}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1444795959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_333833641}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x412015869}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1121581985}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[允许学习到的最大]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数为]{style="font-family:宋体"}[1024]{lang="EN-US"}[，并配置学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，丢弃源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1409636384}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] mac-table limit 1024]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] mac-table limit drop-unknown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x14439020}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_x1189277459}
:::::

::: {#988247972 .myid}
[]{#_Toc404791658}[]{#struct_0_10012_x1780_x288029049}

**VPLS \-- VPLS配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_10012_x1780_1348867013}[命令用来配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[mtu]{lang="EN-US"}**]{#struct_0_10012_x1780_x816448570}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1121778593}

[**[mtu]{lang="EN-US"}**[ *mtu*]{lang="EN-US"}]{#struct_0_10012_x1780_1283446864}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_10012_x1780_x1752604638}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x51273109}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_2096127531}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1353957475}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x262016080}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2075993094}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1400459466}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1121713057}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x662859435}

[*[mtu]{lang="EN-US"}*]{#struct_0_10012_x1780_62058893}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1495608515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果采用]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1878674542}[LDP]{lang="EN-US"}[信令协议建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则要求]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内所有]{style="font-family:宋体"}[PE]{lang="EN-US"}[上配置的]{style="font-family:宋体"}[VSI MTU]{lang="EN-US"}[值必须保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1443440292}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[是]{style="font-family:宋体"}[PW]{lang="EN-US"}[上发送报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，该]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为包括控制字、]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和网络层报文在内的报文的最大长度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_378438890}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1921398346}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1400]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1121909665}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] mtu 1400]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1845408722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_707528277}
:::

::: {#1903411553 .myid}
[]{#_Toc404791659}[]{#struct_0_10012_x1780_1181811834}

**VPLS \-- VPLS配置命令 \-- peer**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**]{#struct_0_10012_x1780_x518526202}[命令用来配置]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI LDP PW]{lang="EN-US"}[视图或]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[PW]{lang="EN-US"}[已存在，则直接进入]{style="font-family:宋体"}[VSI LDP PW]{lang="EN-US"}[视图或]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer**]{lang="EN-US"}]{#struct_0_10012_x1780_x1845380173}[命令用来删除指定的]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1956359712}

[[VSI LDP]{lang="EN-US"}]{#struct_0_10012_x1780_1121844129}[信令视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ *ip-address* \[ **pw-id** *pw-id* \] \[ **hub** \| **no-split-horizon** \| **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* \] \*]{lang="EN-US"}]{#struct_0_10012_x1780_x630890386}

[**[undo]{lang="EN-US"}**[ **peer** *ip-address* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_10012_x1780_1986650910}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x392399057}[静态配置视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ *ip-address* \[ **pw-id** *pw-id* \] \[ **in-label** *label-value* **out-label** *label-value* \[ **hub** \| **no-split-horizon** \| **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* \] \* \]]{lang="EN-US"}]{#struct_0_10012_x1780_120851542}

[**[undo]{lang="EN-US"}**[ **peer** *ip-address* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_10012_x1780_707095116}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x488331315}

[[未配置]{style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_x786581211}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607497975}

[[VSI LDP]{lang="EN-US"}]{#struct_0_10012_x1780_x1954587661}[信令视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态配置视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x889395708}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1543664752}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_210337172}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1059490659}

[*[ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_1978213512}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*]{#struct_0_10012_x1780_1608690147}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果不指定本参数，则]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}**[default-pw-id]{lang="EN-US"}**[命令配置的缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}**[ *l*]{lang="EN-US"}]{#struct_0_10012_x1780_x1607563511}*[abel-value]{lang="EN-US"}*[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[入标签。]{style="font-family:宋体"}*[l]{lang="EN-US"}[abel-value]{lang="EN-US"}*[为入标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}**[ *l*]{lang="EN-US"}]{#struct_0_10012_x1780_x1743634372}*[abel-value]{lang="EN-US"}*[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[出标签。]{style="font-family:宋体"}*[l]{lang="EN-US"}[abel-value]{lang="EN-US"}*[为出标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[hub]{lang="EN-US"}**]{#struct_0_10012_x1780_1345383139}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内为]{style="font-family:宋体"}[hub]{lang="EN-US"}[链路。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[使能了]{style="font-family:宋体"}[hub-spoke]{lang="EN-US"}[能力后，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的]{style="font-family:宋体"}[PW]{lang="EN-US"}[缺省为]{style="font-family:宋体"}[spoke]{lang="EN-US"}[链路。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[no-split-horizon]{lang="EN-US"}**]{#struct_0_10012_x1780_x932327583}[：指定通过该]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发报文时，不采用水平分割方式。缺省情况下，通过]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发报文时，必须采用水平分割方式。]{style="font-family:宋体"}

[**[pw-class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x1283554199}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板中可以配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的数据封装类型、是否使用控制字等。如果不指定本参数，则]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，不支持控制字功能。]{style="font-family:宋体"}

[**[tunnel-policy ]{lang="EN-US"}***[tunnel-policy-name]{lang="EN-US"}*]{#struct_0_10012_x1780_478991659}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的隧道选择策略。]{style="font-family:宋体"}*[tunnel-policy-name]{lang="EN-US"}*[表示隧道策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607366903}

[[创建静态]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_101656958}[时，必须指定]{style="font-family:宋体"}**[in-label]{lang="EN-US"}**[和]{style="font-family:宋体"}**[out-label]{lang="EN-US"}**[参数；静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[已经存在，进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图时，无需指定]{style="font-family:宋体"}**[in-label]{lang="EN-US"}**[和]{style="font-family:宋体"}**[out-label]{lang="EN-US"}**[参数。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x2018560825}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1264162802}[是一对]{style="font-family:宋体"}[PE]{lang="EN-US"}[之间]{style="font-family:宋体"}[PW]{lang="EN-US"}[的标识，本端和远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[上为同一]{style="font-family:宋体"}[PW]{lang="EN-US"}[指定的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[必须相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在本端]{style="font-family:宋体"}]{#struct_0_10012_x1780_1206921408}[PE]{lang="EN-US"}[上，远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[。配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[时指定的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，不能与已经存在的]{style="font-family:宋体"}[VPLS PW]{lang="EN-US"}[、交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[同时相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{style="font-family:宋体"}]{#struct_0_10012_x1780_x682453154}[VSI]{lang="EN-US"}[视图下通过]{style="font-family:宋体"}**[default-pw-id]{lang="EN-US"}**[命令配置了缺省]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，则执行]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令时可以不指定]{style="font-family:宋体"}**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}[参数，采用缺省的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[；否则，执行]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令时必须指定]{style="font-family:宋体"}**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果为静态]{style="font-family:宋体"}]{#struct_0_10012_x1780_250679308}[PW]{lang="EN-US"}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1464979539}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_40510055}[在]{style="font-family:宋体"}[VSI LDP]{lang="EN-US"}[信令视图下，配置一条]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[：远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[4.4.4.4]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并指定通过本]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发报文时不采用水平分割方式。配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[后，将进入]{style="font-family:宋体"}[VSI LDP PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1607432439}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp\] peer 4.4.4.4 pw-id 200 no-split-horizon]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp-4.4.4.4-200\] ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1798252216}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态配置视图下，配置一条]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[：远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[5.5.5.5]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[100]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并指定通过本]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发报文时不采用水平分割方式。配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[后，将进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x406038811}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling static]{lang="EN-US"}

[\[Sysname-vsi-vpn1-static\] peer 5.5.5.5 pw-id 200 in-label 100 out-label 200 no-split-horizon]{lang="EN-US"}

[\[Sysname-vsi-vpn1-static-5.5.5.5-200\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1207003819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-pw-id]{lang="EN-US"}**]{#struct_0_10012_x1780_948493745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ldp]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607235831}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_x1294893524}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_325671659}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel-policy]{lang="EN-US"}**]{#struct_0_10012_x1780_468410633}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道策略）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-238882288 .myid}
[]{#_Toc404791660}[]{#struct_0_10012_x1780_937118534}[]{#_Toc339885991}[]{#_Toc300843409}[]{#_Toc300843411}

**VPLS \-- VPLS配置命令 \-- peer auto-discovery**

------------------------------------------------------------------------

[**[peer auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_x2037010235}[命令]{style="font-family:宋体"}[用来使能本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的能力。]{style="font-family:宋体"}

[**[undo peer auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_x1147637854}[命令用来禁止本地路由器与指定对等体]{style="font-family:
宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:
宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1091995796}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **auto-discovery** \[ **non-standard** \]]{lang="EN-US"}]{#struct_0_10012_x1780_x1607301367}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **auto-discovery**]{lang="EN-US"}]{#struct_0_10012_x1780_31735670}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1313893396}

[[本地路由器具有与]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x881875373}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的能力，并且采用]{style="font-family:宋体"}[RFC 6074]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_2086833266}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_459339092}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x21347448}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_457549073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1607104759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x822103708}

[*[group-name]{lang="EN-US"}*]{#struct_0_10012_x1780_1489002150}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_407277119}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_10012_x1780_195916443}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[non-standard]{lang="EN-US"}**]{#struct_0_10012_x1780_x224875579}[：指定采用非标准]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。如果不指定本参数，则采用]{style="font-family:宋体"}[RFC 6074]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。请根据对等体支持的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式类型，选择是否指定本参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1230134264}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x843072124}[对等体之间可以通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息，以此来自动发现同一个]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例中的]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备，无需手工指定每一台]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备，从而简化网络配置和管理。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_1225860918}[地址族视图下执行]{style="font-family:宋体"}**[peer enable]{lang="EN-US"}**[命令后，本地路由器即具有与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的能力，并使用]{style="font-family:宋体"}[RFC 6074]{lang="EN-US"}[定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。如需禁止该能力或该对等体不支持交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息，则执行]{style="font-family:宋体"}**[undo peer auto-discovery]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607170295}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1372005090}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的能力，并采用]{style="font-family:宋体"}[RFC 6074]{lang="EN-US"}[定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1080940067}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] peer 3.3.3.9 auto-discovery]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_10012_x1780_x1207106398}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="SV"}[地址族视图下，使能本地路由器与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息的能力，并采用非标准的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_44847687}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] peer test auto-discovery non-standard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_203145791}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp l2vpn auto-discovery]{lang="EN-US"}**]{#struct_0_10012_x1780_2080811854}
:::

::: {#-1992627212 .myid}
[]{#_Toc404791661}[]{#struct_0_10012_x1780_x1606973687}[]{#_Toc339885992}[]{#_Toc336272256}

**VPLS \-- VPLS配置命令 \-- peer signaling**

------------------------------------------------------------------------

[**[peer signaling]{lang="EN-US"}**]{#struct_0_10012_x1780_1877865479}[命令]{style="font-family:宋体"}[用来使能本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息的能力。]{style="font-family:宋体"}

[**[undo peer signaling]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607039223}[命]{style="font-family:宋体"}[令用来禁止本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1926785808}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **signaling**]{lang="EN-US"}]{#struct_0_10012_x1780_193170208}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **signaling**]{lang="EN-US"}]{#struct_0_10012_x1780_x1583153688}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607497974}

[[本地路由器具有与]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x388503720}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换标签块信息的能力。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1520422958}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_652876942}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1886310712}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1425085827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x943794671}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1696645372}

[*[group-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x1607563510}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_10012_x1780_985248983}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_10012_x1780_1761476091}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1370518131}

[[建立]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}]{#struct_0_10012_x1780_1535020939}[时，]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备通过]{style="font-family:宋体"}[MP-BGP]{lang="EN-US"}[协议来交换标签块信息。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_1731335453}[地址族视图下执行]{style="font-family:宋体"}**[peer enable]{lang="EN-US"}**[命令后，本地路由器即具有与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换标签块信息的能力。如需禁止该能力或该对等体不支持交换标签块信息，则执行]{style="font-family:宋体"}**[undo peer signaling]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x912601543}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1607366902}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[交换]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1464426983}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] peer 3.3.3.9 signaling]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_702316156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp l2vpn ]{lang="EN-US"}**]{#struct_0_10012_x1780_1362792148}**[signaling]{lang="EN-US"}**
:::

::: {#-985333979 .myid}
[]{#_Toc404791662}[]{#struct_0_10012_x1780_x1607432438}

**VPLS \-- VPLS配置命令 \-- policy vpn-target**

------------------------------------------------------------------------

[**[policy vpn-target]{lang="EN-US"}**]{#struct_0_10012_x1780_x232168275}[命令用来对接收到的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息使能]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能，即只将]{style="font-family:宋体"}[Export Route Target]{lang="EN-US"}[属性与本地]{style="font-family:宋体"}[Import Route Target]{lang="EN-US"}[属性匹配的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息加入到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息表。]{style="font-family:宋体"}

[**[undo policy vpn-target]{lang="EN-US"}**]{#struct_0_10012_x1780_1335133923}[命令用来取消对]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息的]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能，即接收所有的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_293505429}

[**[policy vpn-target]{lang="EN-US"}**]{#struct_0_10012_x1780_130496039}

[**[undo policy vpn-target]{lang="EN-US"}**]{#struct_0_10012_x1780_1595089612}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2119745734}

[[对接收到的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x2001167898}[信息使能]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607235830}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_271190417}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_888326593}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_437704775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1574279416}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x734380314}

[[在跨域]{style="font-family:宋体"}[VPN-OptionB]{lang="EN-US"}]{#struct_0_10012_x1780_x1607301366}[组网中，]{style="font-family:宋体"}[ASBR-PE]{lang="EN-US"}[需要保存所有]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息（即通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息和标签块信息），以通告给远端]{style="font-family:宋体"}[ASBR-PE]{lang="EN-US"}[。这种情况下，]{style="font-family:宋体"}[ASBR-PE]{lang="EN-US"}[上需执行]{style="font-family:宋体"}**[undo policy vpn-target]{lang="EN-US"}**[命令接收所有的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息，不对它们进行]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤。]{style="font-family:宋体"}

[[跨域]{style="font-family:宋体"}[VPN-OptionB]{lang="EN-US"}]{#struct_0_10012_x1780_x1534348271}[的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1336534709}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1607104758}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，取消对]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息的]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1906779647}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] undo policy vpn-target]{lang="EN-US"}
:::

::: {#-1410971825 .myid}
[]{#_Toc404791663}[]{#struct_0_10012_x1780_480066816}

**VPLS \-- VPLS配置命令 \-- pw-class (system view)**

------------------------------------------------------------------------

[**[pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_x1659915133}[命令用来创建]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板]{style="font-family:宋体"}[，并]{style="font-family:宋体"}[进入]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_1480909580}[命令用来删除已经创建的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1374963222}

[**[pw-class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x1849644935}

[**[undo pw-class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x1607170294}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_194078851}

[[设备上不存在任何]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1126230094}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x235981799}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_2010607206}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1189778047}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1593334255}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_398756867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1606973686}

[*[class-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x851017876}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1972125339}

[[通过本命令创建]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x498044829}[模板，并进入]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图后，可以在]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图下指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的属性，如]{style="font-family:宋体"}[PW]{lang="EN-US"}[的数据封装类型、是否使用控制字。具有相同属性的]{style="font-family:宋体"}[PW]{lang="EN-US"}[可以通过引用相同的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板，实现对]{style="font-family:宋体"}[PW]{lang="EN-US"}[属性的配置，从而简化配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x298256465}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_663686835}[创建]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板]{style="font-family:宋体"}[pw100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x356606600}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607039222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[control-word enable]{lang="EN-US"}**]{#struct_0_10012_x1780_x360701867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_x544958976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-type]{lang="EN-US"}**]{#struct_0_10012_x1780_98416263}
:::

::: {#1984398029 .myid}
[]{#_Toc339310154}[]{#_Toc404791664}[]{#struct_0_10012_x1780_x1863222947}

**VPLS \-- VPLS配置命令 \-- pw-class (VSI auto-discovery view)**

------------------------------------------------------------------------

[**[pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_x1252193043}[命令用来指定引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **pw-class**]{lang="EN-US"}]{#struct_0_10012_x1780_665547024}[命令用来取消引用]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1479542435}

[**[pw-class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x1607497977}

[**[undo pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_x791788247}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x792886925}

[[不引用任何]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_636751840}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1283813206}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x86796473}[自动发现视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x479529964}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x2087524113}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1607563513}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x580834958}

[*[class-name]{lang="EN-US"}*]{#struct_0_10012_x1780_351934422}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_867159727}

[[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1390908752}[自动发现视图下执行本命令指定引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板后，该]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板将应用于该视图下建立的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x499207501}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_543201822}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现视图下，指定引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板为]{style="font-family:宋体"}[pw100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1607366905}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] pw-class pw100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1264456372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[control-word enable]{lang="EN-US"}**]{#struct_0_10012_x1780_139333351}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_x1463289088}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-type]{lang="EN-US"}**]{#struct_0_10012_x1780_1782501129}
:::

::: {#1550157549 .myid}
[]{#_Toc404791665}[]{#struct_0_10012_x1780_x1883247765}

**VPLS \-- VPLS配置命令 \-- pw-type**

------------------------------------------------------------------------

[**[pw-type]{lang="EN-US"}**]{#struct_0_10012_x1780_x433191106}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型。]{style="font-family:宋体"}

[**[undo pw-type]{lang="EN-US"}**]{#struct_0_10012_x1780_450981237}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607432441}

[**[pw-type]{lang="EN-US"}**[ { **ethernet** \| **vlan** }]{lang="EN-US"}]{#struct_0_10012_x1780_x1442218464}

[**[undo pw-type]{lang="EN-US"}**]{#struct_0_10012_x1780_473676928}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1364905807}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1785958002}[数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_985737388}

[[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x93330061}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2095848909}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1607235833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1837274358}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1802322676}

[**[ethernet]{lang="EN-US"}**]{#struct_0_10012_x1780_x1331283242}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_10012_x1780_x258434931}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1297670114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_10012_x1780_x1341916730}[数据封装类型下，]{style="font-family:
宋体"}[PW]{lang="EN-US"}[上传输的帧不能带服务提供商网络为了区分用户而要求用户压入的]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，该]{style="font-family:宋体"}[Tag]{lang="EN-US"}[又称为服务定界符。对于]{style="font-family:宋体"}[CE]{lang="EN-US"}[侧的报文，如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到带有]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文，则将其去除后再压入]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道封装转发；如果从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到不带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文，则直接压入]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道封装后转发。对于]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[CE]{lang="EN-US"}[的报文，如果]{style="font-family:宋体"}**[xconnect vsi]{lang="EN-US"}**[命令配置的接入模式为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则添加]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[后转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[；如果配置的接入模式为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[，则不添加]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，直接转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[；不允许重写或去除已经存在的任何]{style="font-family:宋体"}[Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_10012_x1780_x2128423903}[数据封装类型下，]{style="font-family:宋体"}[PW]{lang="EN-US"}[上传输的帧必须带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[。对于]{style="font-family:宋体"}[CE]{lang="EN-US"}[侧的报文，]{style="font-family:宋体"}[PE]{lang="EN-US"}[从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到带有]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文后，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[不要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则保留]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则将]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[改写为远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[期望的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（]{style="font-family:宋体"}[Tag]{lang="EN-US"}[可能是值为]{style="font-family:宋体"}[0]{lang="EN-US"}[的空]{style="font-family:宋体"}[Tag]{lang="EN-US"}[），再压入]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道封装后转发；从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到不带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文后，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[不要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则添加值为]{style="font-family:宋体"}[0]{lang="EN-US"}[的空]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则添加一个远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[期望的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（]{style="font-family:宋体"}[Tag]{lang="EN-US"}[可能是值为]{style="font-family:宋体"}[0]{lang="EN-US"}[的空]{style="font-family:宋体"}[Tag]{lang="EN-US"}[）后，再压入]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道封装后转发。对于]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[CE]{lang="EN-US"}[的报文，如果]{style="font-family:宋体"}**[xconnect vsi]{lang="EN-US"}**[命令配置的接入模式为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[时重写或保留]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[；如果配置的接入模式为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[，则去除]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[后转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607301369}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1487294104}[配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_187656642}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] pw-type ethernet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1158606852}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_10012_x1780_x573675224}
:::

::: {#1513393433 .myid}
[]{#_Toc404791666}[]{#struct_0_10012_x1780_x310681457}

**VPLS \-- VPLS配置命令 \-- pwsignaling**

------------------------------------------------------------------------

[**[pwsignaling]{lang="EN-US"}**]{#struct_0_10012_x1780_1190551111}[命令用来指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[使用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议，并进入对应的信令视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pwsignaling]{lang="EN-US"}**]{#struct_0_10012_x1780_x1597316240}[命令用来取消]{style="font-family:宋体"}[VSI]{lang="EN-US"}[使用指定的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607104761}

[**[pwsignaling]{lang="EN-US"}**[ { **ldp** \| **static** }]{lang="EN-US"}]{#struct_0_10012_x1780_x465676740}

[**[undo pwsignaling ]{lang="EN-US"}**[{ **ldp** \| **static** }]{lang="EN-US"}]{#struct_0_10012_x1780_1940708652}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1615337390}

[[未指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_366479686}[使用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_655689492}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1036962267}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1991868788}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1607170297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1760162792}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_304626905}

[**[ldp]{lang="EN-US"}**]{#struct_0_10012_x1780_x1532734336}[：指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[使用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令的]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI LDP]{lang="EN-US"}[信令视图。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_10012_x1780_2129205026}[：指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[采用静态配置方式建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[静态配置视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1551288650}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_432917039}[指定名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[使用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令的]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI LDP]{lang="EN-US"}[信令视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1606973689}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1071296425}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_x895225623}
:::

::::: {#816869194 .myid}
[]{#_Toc404791667}[]{#struct_0_10012_x1780_x1607235832}

**VPLS \-- VPLS配置命令 \-- reset l2vpn mac-address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](VPLS命令.files/image004.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_x891608997}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_368017814}
:::

**[ ]{lang="EN-US"}**

[**[reset l2vpn mac-address]{lang="EN-US"}**]{#struct_0_10012_x1780_x719992332}[命令用来清除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x802362932}

[**[reset ]{lang="EN-US"}[l2vpn mac-address ]{lang="EN-US"}**[\[ **vsi**]{lang="EN-US"}*[ vsi-name ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_10012_x1780_x146470962}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_281940308}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x449143985}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607301368}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1241589251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1313710941}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x673095754}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_10012_x1780_x1841995928}[：清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_578904812}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_849527191}[学习到错误的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，或学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项数目达到最大值时，可以执行本命令，以便重新学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_2048261598}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1607104760}[清除名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[\<Sysname\> reset l2vpn mac-address vsi vpn1]{lang="EN-US"}]{#struct_0_10012_x1780_x2031760681}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1312176485}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn mac-address vsi ]{lang="EN-US"}**]{#struct_0_10012_x1780_1070067252}
:::::

::::: {#1457959242 .myid}
[]{#_Toc404791668}[]{#struct_0_10012_x1780_x1920658660}[]{#_Toc389645819}[]{#_Toc378236174}

**VPLS \-- VPLS配置命令 \-- reset l2vpn statistics pw**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VPLS命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10012_x1780_x1019444543}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_x1882639492}
:::

[ ]{lang="EN-US"}

[**[reset l2vpn statistics pw]{lang="EN-US"}**]{#struct_0_10012_x1780_x1469655280}[命令用来清除指定]{style="font-family:
宋体"}[PW]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x61194292}

[**[reset l2vpn statistics pw ]{lang="EN-US"}**[\[ **vsi** ]{lang="EN-US"}]{#struct_0_10012_x1780_383969741}*[vsi-name]{lang="FR"}***[ ]{lang="FR"}**[\[ **link** ]{lang="EN-US"}*[link-id ]{lang="FR"}*[\] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1476677879}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1920724196}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2038486075}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x2130143256}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1114484590}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2094016748}

[**[vsi ]{lang="EN-US"}**]{#struct_0_10012_x1780_2123723307}*[vsi-name]{lang="FR"}*[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VSI]{lang="FR"}[实例内的]{style="font-family:宋体"}[PW]{lang="FR"}[报文统计信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定该参数，则清除所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[link ]{lang="FR"}**]{#struct_0_10012_x1780_x1920789732}*[link-id]{lang="FR"}*[：]{style="font-family:
宋体"}[清除指定]{style="font-family:宋体"}[PW]{lang="FR"}[的统计信息。]{style="font-family:宋体"}*[link-id]{lang="FR"}*[为]{style="font-family:宋体"}[VSI]{lang="FR"}[实例内标识]{style="font-family:
宋体"}[PW]{lang="FR"}[的链路]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:
宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[65534]{lang="FR"}[。如果不指定该参数，则清除指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[实例内的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x790496287}

[[当]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x828764318}[存在备]{style="font-family:宋体"}[PW]{lang="EN-US"}[时，会同时清除主]{style="font-family:宋体"}[PW]{lang="EN-US"}[和备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_688402192}

[[\# ]{lang="FR"}]{#struct_0_10012_x1780_x2013147510}[清除本设备上所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset l2vpn statistics pw]{lang="FR"}]{#struct_0_10012_x1780_x376455645}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1108566100}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[statistics enable]{lang="NO-BOK"}**]{#struct_0_10012_x1780_x1920855268}
:::::

::::: {#-1195135256 .myid}
[]{#_Toc288911613}[]{#_Toc265738467}[]{#_Toc404791669}[]{#struct_0_10012_x1780_275872785}

**VPLS \-- VPLS配置命令 \-- restrain**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](VPLS命令.files/image001.png){width="62" height="26"}]{lang="EN-US"}]{#struct_0_10012_x1780_556853304}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_x890527487}
:::

**[ ]{lang="EN-US"}**

[**[restrain]{lang="EN-US"}**]{#struct_0_10012_x1780_1473419945}[命令用来配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的广播、组播或未知单播抑制百分比。]{style="font-family:宋体"}

[**[undo restrain]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607170296}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x968720563}

[**[restrain]{lang="EN-US"}**[ { **broadcast** \| **multicast** \| **unknown-unicast** } *ratio*]{lang="EN-US"}]{#struct_0_10012_x1780_1873158501}

[**[undo restrain ]{lang="EN-US"}**[{ **broadcast** \| **multicast** \| **unknown-unicast** }]{lang="EN-US"}]{#struct_0_10012_x1780_x473657328}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1277539898}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x712655896}[的广播抑制百分比为]{style="font-family:宋体"}[5%]{lang="EN-US"}[，组播抑制百分比为]{style="font-family:宋体"}[100%]{lang="EN-US"}[，未知单播抑制百分比为]{style="font-family:宋体"}[100%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1557647176}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x2025628213}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1606973688}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1657586930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1074593700}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1582672127}

[**[broadcast]{lang="EN-US"}**]{#struct_0_10012_x1780_x1331130889}[：配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的广播抑制百分比。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_10012_x1780_x1060779359}[：配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的组播抑制百分比。]{style="font-family:宋体"}

[**[unknown-unicast]{lang="EN-US"}**]{#struct_0_10012_x1780_x939182199}[：配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的未知单播抑制百分比。未知单播报文是指在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表中不存在目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应表项的单播报文。]{style="font-family:宋体"}

[*[ratio]{lang="EN-US"}*]{#struct_0_10012_x1780_1788267327}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的广播、组播或未知单播的抑制百分比值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为百分比。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607039224}

[[本命令与]{style="font-family:宋体"}**[bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_x1523501281}[命令配合使用可以抑制]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的广播、组播和未知单播流量。当广播、组播或未知单播流量超过最大带宽值×对应的抑制百分比时，将丢弃超过该值的广播、组播或未知单播流量。]{style="font-family:宋体"}

[[抑制的是所有]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_1073821910}[入方向、出方向流量，还是同时抑制入方向和出方向流量，与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607497979}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_727241527}[配置名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的广播抑制百分比为]{style="font-family:宋体"}[10%]{lang="EN-US"}[，组播抑制百分比为]{style="font-family:宋体"}[50%]{lang="EN-US"}[，未知单播抑制百分比为]{style="font-family:宋体"}[50%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_14645351}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] restrain broadcast 10]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] restrain multicast 50]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] restrain unknown-unicast 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1830128403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bandwidth]{lang="EN-US"}**]{#struct_0_10012_x1780_558938580}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1672392087}
:::::

::: {#1047826473 .myid}
[]{#_Toc404791670}[]{#struct_0_10012_x1780_896343639}[]{#_Toc288911631}[]{#_Toc264644583}

**VPLS \-- VPLS配置命令 \-- revertive**

------------------------------------------------------------------------

[**[revertive]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607563515}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[冗余保护倒换的回切模式，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后流量是否从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[，以及回切模式下的回切等待时间，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后，流量从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[的等待时间。]{style="font-family:宋体"}

[**[undo revertive wtr]{lang="EN-US"}**]{#struct_0_10012_x1780_581964456}[命令用来恢复回切等待时间的缺省情况，即回切等待时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo revertive never]{lang="EN-US"}**]{#struct_0_10012_x1780_x1638807723}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1960153755}

[**[revertive ]{lang="EN-US"}**[{ **wtr** *wtr-time* \| **never** }]{lang="EN-US"}]{#struct_0_10012_x1780_1487552098}

[**[undo revertive ]{lang="EN-US"}**[{ **wtr** \| **never** }]{lang="EN-US"}]{#struct_0_10012_x1780_x2141024862}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1170702307}

[[开启回切功能，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1473896996}[恢复后，流量会从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[；回切等待时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后，流量会立即从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607366907}

[[VSI LDP]{lang="EN-US"}]{#struct_0_10012_x1780_x1867711510}[信令视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态配置视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1677561039}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x947698968}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_328644202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1494779452}

[**[wtr ]{lang="EN-US"}***[wtr-time]{lang="EN-US"}*]{#struct_0_10012_x1780_1244544734}[：开启回切功能，并指定回切等待时间（]{style="font-family:宋体"}[wait-to-restore time]{lang="EN-US"}[），即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后，等待]{style="font-family:宋体"}*[wtr-time]{lang="EN-US"}*[时间后，才将流量从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}*[wtr-time]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[never]{lang="EN-US"}**]{#struct_0_10012_x1780_x330796858}[：]{style="font-family:宋体"}[指定不回切。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607432443}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1689949418}[为名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[、采用静态配置方式建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[开启回切功能，并指定回切等待时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1087129100}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling static]{lang="EN-US"}

[\[Sysname-vsi-vpn1-static\] revertive wtr 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x669169898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_x15732614}
:::

::: {#263693428 .myid}
[]{#_Toc404791671}[]{#struct_0_10012_x1780_40515210}[]{#_Toc339310160}

**VPLS \-- VPLS配置命令 \-- route-distinguisher**

------------------------------------------------------------------------

[**[route-distinguisher]{lang="EN-US"}**]{#struct_0_10012_x1780_2141364249}[命令用来为当前]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[RD]{lang="EN-US"}[（]{style="font-family:宋体"}[Route Distinguisher]{lang="EN-US"}[，路由标识符）。]{style="font-family:宋体"}

[**[undo route-distinguisher]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607235835}[命令用来删除已配置的]{style="font-family:
宋体"}[RD]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_674474944}

[**[route-distinguisher]{lang="EN-US"}**[ *route-distinguisher*]{lang="EN-US"}]{#struct_0_10012_x1780_x1669513544}

[**[undo route-distinguisher]{lang="EN-US"}**]{#struct_0_10012_x1780_874093569}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1793523885}

[[没有为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1698497984}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式指定]{style="font-family:宋体"}[RD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1550719049}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x460773671}[自动发现视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607301371}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1131129280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1529779891}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1188449528}

[*[route-distinguisher]{lang="EN-US"}*]{#struct_0_10012_x1780_x1451014477}[：路由标识符，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。路由标识符有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_10012_x1780_2097599337}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x925420839}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x746978983}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。例如：]{style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607104763}

[[在]{style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_10012_x1780_x1628476154}[中，]{style="font-family:宋体"}[RD]{lang="EN-US"}[用来区分不同]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内编号相同的站点。]{style="font-family:宋体"}[PE]{lang="EN-US"}[在通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布其连接的站点信息时，在]{style="font-family:宋体"}[Site ID]{lang="EN-US"}[前增加]{style="font-family:宋体"}[RD]{lang="EN-US"}[，通过]{style="font-family:宋体"}[RD]{lang="EN-US"}[和]{style="font-family:宋体"}[Site ID]{lang="EN-US"}[来唯一标识网络中的一个站点。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10012_x1780_706767073}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置的]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1607170299}[RD]{lang="EN-US"}[对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居自动发现和]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块分发均有效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能为不同]{style="font-family:宋体"}]{#struct_0_10012_x1780_953593738}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置相同的]{style="font-family:宋体"}[RD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能通过重复执行]{lang="EN-US" style="font-family:宋体"}**[route-distinguisher]{lang="EN-US"}**]{#struct_0_10012_x1780_x253503950}[命令修改]{lang="EN-US" style="font-family:
宋体"}[RD]{lang="EN-US"}[值。必须先]{lang="EN-US" style="font-family:
宋体"}[执行]{style="font-family:宋体"}**[undo route-distinguisher]{lang="EN-US"}**[命令删除]{lang="EN-US" style="font-family:宋体"}[RD]{lang="EN-US"}[值，再通过]{lang="EN-US" style="font-family:宋体"}**[route-distinguisher]{lang="EN-US"}**[命令配置新的]{lang="EN-US" style="font-family:
宋体"}[RD]{lang="EN-US"}[值。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1933153438}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1007192470}[为名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[22:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x904906088}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] route-distinguisher 22:1]{lang="EN-US"}
:::

::: {#-190074586 .myid}
[]{#_Toc404791672}[]{#struct_0_10012_x1780_1439095557}

**VPLS \-- VPLS配置命令 \-- rr-filter**

------------------------------------------------------------------------

[**[rr-filter]{lang="EN-US"}**]{#struct_0_10012_x1780_x1606973691}[命令用来创建路由反射器的反射策略：通过配置路由反射器支持的扩展团体属性号，对接收的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息进行过滤，只有接收的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息包含指定的扩展团体属性号时，路由反射器才会反射该]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rr-filter**]{lang="EN-US"}]{#struct_0_10012_x1780_715000529}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1160919925}

[**[rr-filter ]{lang="EN-US"}***[extended-community-number]{lang="EN-US"}*]{#struct_0_10012_x1780_x1112548400}

[**[undo rr-filter]{lang="EN-US"}**]{#struct_0_10012_x1780_293979764}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1308448082}

[[路由反射器不会对反射的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_1763737522}[信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x640842843}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x1607039227}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_42582660}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1994938641}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x128601422}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1967032781}

[*[extended-community-number]{lang="EN-US"}*]{#struct_0_10012_x1780_1573376125}[：路由反射器支持的扩展团体属性号，取值范围]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1624633545}

[[当一个集群中存在多个路由反射器时，通过在不同的路由反射器上配置不同的反射策略，可以实现路由反射器之间的负载分担。]{style="font-family:宋体"}]{#struct_0_10012_x1780_1982239082}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1607497978}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x2001641828}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，配置路由反射器支持的扩展团体属性号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，即该路由反射器只反射包含扩展团体属性]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1373169380}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] rr-filter 10]{lang="EN-US"}
:::

::: {#-1902885513 .myid}
[]{#_Toc404791673}[]{#struct_0_10012_x1780_1883249195}

**VPLS \-- VPLS配置命令 \-- service-instance**

------------------------------------------------------------------------

[**[service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_x711833746}[命令用来创建以太网服务实例，并进入以太网服务实例视图。]{style="font-family:宋体"}

[**[undo service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_x1423477429}[命令用来删除指定的以太网服务实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_883151854}

[**[service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_10012_x1780_x1607563514}

[**[undo service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_10012_x1780_x984119485}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1674581026}

[[接口上不存在任何以太网服务实例。]{style="font-family:宋体"}]{#struct_0_10012_x1780_1561247690}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_444957763}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10012_x1780_x348657680}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1965438319}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1746982045}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1607366906}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_861171845}

[*[instance-id]{lang="EN-US"}*]{#struct_0_10012_x1780_704889727}[：以太网服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x868817838}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x331984378}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上创建以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_903942279}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1095965548}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607432442}
:::

::: {#1170655049 .myid}
[]{#_Toc404791674}[]{#struct_0_10012_x1780_x1038933937}

**VPLS \-- VPLS配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_10012_x1780_608454984}[命令用来关闭当前的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_10012_x1780_x919131929}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x301769347}

[**[shutdown]{lang="EN-US"}**]{#struct_0_10012_x1780_1019349748}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_10012_x1780_2137142657}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1860563306}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1607235834}[处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2054408411}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1787656243}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_150910037}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x814734385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1778820404}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x93768706}

[[关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1522039546}[后，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[将不能提供]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1607301370}[功能通常用于暂时禁用]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[服务，但还需要再次启用该]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[服务的场景。关闭]{style="font-family:宋体"}[VSI]{lang="EN-US"}[后，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[所有已存在的配置保持不变。在关闭状态下还可以对]{style="font-family:宋体"}[VSI]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[再次被开启后，基于最新的配置提供]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1597754075}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1857017168}[关闭名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1592118877}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1193128890}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_x2021477457}
:::

::: {#-230231420 .myid}
[]{#_Toc404791675}[]{#struct_0_10012_x1780_111480058}[]{#_Toc339310163}

**VPLS \-- VPLS配置命令 \-- signaling-protocol**

------------------------------------------------------------------------

[**[signaling-protocol]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607104762}[命令用来配置通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后，与该]{style="font-family:宋体"}[PE]{lang="EN-US"}[建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[时采用的信令协议，并进入对应的信令视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[signal]{lang="EN-US"}**[ing**-protocol**]{lang="EN-US"}]{#struct_0_10012_x1780_1100407201}[命令用来取消已配置的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1540783817}

[**[signaling-protocol]{lang="EN-US"}**[ { **bgp** \| **ldp** }]{lang="EN-US"}]{#struct_0_10012_x1780_1605442423}

[**[undo ]{lang="EN-US"}[signaling-protocol]{lang="EN-US"}**]{#struct_0_10012_x1780_x43501007}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1509286316}

[[未指定通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_10012_x1780_327224674}[自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后，与该]{style="font-family:宋体"}[PE]{lang="EN-US"}[建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[时采用的信令协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1174530017}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1607170298}[自动发现视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1775289617}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1691200037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x626632467}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1477569233}

[**[bgp]{lang="EN-US"}**]{#struct_0_10012_x1780_2045319920}[：指定采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[BGP]{lang="EN-US"}[信令视图。]{style="font-family:宋体"}

[**[ldp]{lang="EN-US"}**]{#struct_0_10012_x1780_x575451097}[：指定采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令视图。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1990423060}

[[在同一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1608914172}[自动发现视图下只能指定一种]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议。不允许重复执行本命令指定不同的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1606973690}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x2013882826}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现视图下，配置通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后，采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1506407644}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] signaling-protocol ldp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto-ldp\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_506102066}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_x998227258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_10012_x1780_x1238722023}**[vsi]{lang="EN-US"}**
:::

::: {#1273103123 .myid}
[]{#_Toc404791676}[]{#struct_0_10012_x1780_1944990302}[]{#_Toc339310164}

**VPLS \-- VPLS配置命令 \-- site**

------------------------------------------------------------------------

[**[site]{lang="EN-US"}**]{#struct_0_10012_x1780_x1607039226}[命令用来创建本地站点。]{style="font-family:宋体"}

[**[undo site]{lang="EN-US"}**]{#struct_0_10012_x1780_1608666601}[命令用来删除指定的本地站点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_456461533}

[**[site ]{lang="EN-US"}***[site-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **range** *range-value* \] \[ **default-offset** *default-offset* \]]{lang="EN-US"}]{#struct_0_10012_x1780_314816326}

[**[undo site]{lang="EN-US"}**[ *site-id*]{lang="EN-US"}]{#struct_0_10012_x1780_1257817760}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_523432914}

[[设备上不存在任何本地站点。]{style="font-family:宋体"}]{#struct_0_10012_x1780_836187259}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1392531340}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_314750790}[自动发现]{style="font-family:宋体"}[BGP]{lang="EN-US"}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1304496974}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x696237540}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_932420121}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1698678340}

[*[site-id]{lang="EN-US"}*]{#struct_0_10012_x1780_1602007950}[：本地站点的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[range ]{lang="EN-US"}***[range-value]{lang="EN-US"}*]{#struct_0_10012_x1780_x299859521}[：指定]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内最多包含的站点数目。]{style="font-family:宋体"}*[range-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}*[site-id]{lang="EN-US"}*[的最大值＋]{style="font-family:宋体"}[1]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[default-offset ]{lang="EN-US"}***[default-offset]{lang="EN-US"}*]{#struct_0_10012_x1780_315078470}[：指定]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例中站点的起始编号。]{style="font-family:宋体"}*[default-offset]{lang="EN-US"}*[为起始编号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内的站点从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始编号；取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，表示]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内的站点从]{style="font-family:宋体"}[1]{lang="EN-US"}[开始编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1170322874}

[[在同一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1494366331}[下，可以创建]{style="font-family:宋体"}[ID]{lang="EN-US"}[不同的多个本地站点。]{style="font-family:宋体"}

[[允许在]{style="font-family:宋体"}*[site-id]{lang="EN-US"}*]{#struct_0_10012_x1780_315012934}[和]{style="font-family:宋体"}*[default-offset]{lang="EN-US"}*[不改变的情况下，通过重复执行]{style="font-family:宋体"}**[site]{lang="EN-US"}**[命令来增大此站点的]{style="font-family:宋体"}[range]{lang="EN-US"}[值，但不允许将]{style="font-family:宋体"}[range]{lang="EN-US"}[改小。要想将]{style="font-family:宋体"}[range]{lang="EN-US"}[改小，则需要删除这个站点，并重新创建。]{style="font-family:宋体"}

[[不能通过重复执行]{style="font-family:宋体"}**[site]{lang="EN-US"}**]{#struct_0_10012_x1780_315144006}[命令来修改]{style="font-family:宋体"}*[default-offset]{lang="EN-US"}*[。必须先通过]{style="font-family:宋体"}**[undo site]{lang="EN-US"}**[命令删除本地站点，再通过]{style="font-family:宋体"}**[site]{lang="EN-US"}**[命令创建本地站点，并指定新的]{style="font-family:宋体"}*[default-offset]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_315340614}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x499359371}[在名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[下创建本地站点]{style="font-family:宋体"}[1]{lang="EN-US"}[，指定]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例内最多包含的站点数目为]{style="font-family:宋体"}[30]{lang="EN-US"}[，站点的起始编号为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_177933400}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] signaling-protocol bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto-bgp\] site 1 range 30 default-offset 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x520026219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_1430656830}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1800154016}
:::

::: {#1066584173 .myid}
[]{#_Toc404791677}[]{#struct_0_10012_x1780_1971220721}[]{#_Toc389645828}[]{#_Toc378236183}[]{#_Toc377993835}

**VPLS \-- VPLS配置命令 \-- snmp-agent trap enable l2vpn**

------------------------------------------------------------------------

[**[snmp-agent trap enable l2vpn]{lang="FR"}**]{#struct_0_10012_x1780_1971155185}[命令用来开启]{style="font-family:宋体"}[L2VPN]{lang="FR"}[模块的]{style="font-family:宋体"}[PW]{lang="FR"}[状态变化告警功能。]{style="font-family:
宋体"}

[**[undo snmp-agent trap enable l2vpn]{lang="FR"}**]{#struct_0_10012_x1780_x1765567823}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="FR"}[模块的]{style="font-family:宋体"}[PW]{lang="FR"}[状态变化告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x426978299}

[**[snmp-agent trap enable l2vpn ]{lang="FR"}**]{#struct_0_10012_x1780_430483102}[\[ **pw-up-down** \| **pw-delete** \] \*]{lang="FR"}

[**[undo snmp-agent trap enable l2vpn ]{lang="FR"}**]{#struct_0_10012_x1780_1971089649}[\[ **pw-up-down** \| **pw-delete** \] \*]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1825577880}

[[L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_1019461290}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_584421389}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x37044608}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1242055127}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x739293478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x296724858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_478410929}

[**[pw-up-down]{lang="FR"}**]{#struct_0_10012_x1780_1971548401}[：开启]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[up-down]{lang="EN-US"}[状态变化告警。]{style="font-family:宋体"}

[**[pw-delete]{lang="FR"}**]{#struct_0_10012_x1780_x146174068}[：开启]{style="font-family:宋体"}[PW]{lang="EN-US"}[删除告警。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1442659929}

[[开启]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_10012_x1780_x1522180859}[模块的告警功能后，当]{style="font-family:宋体"}[PW]{lang="EN-US"}[状态发生变化时会产生告警信息。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_10012_x1780_422762331}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1788706165}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_1978490944}[开启]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[up-down]{lang="EN-US"}[状态变化告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_10012_x1780_1191261311}

[\[Sysname\] snmp-agent trap enable l2vpn pw-up-down]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x802495405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display snmp-agent trap-list]{lang="NO-BOK"}**]{#struct_0_10012_x1780_236075113}[（网络管理和监控命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[SNMP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-655052582 .myid}
[]{#_Toc404791678}[]{#struct_0_10012_x1780_1971482865}[]{#_Toc389645829}[]{#_Toc378236184}[]{#_Toc377562530}

**VPLS \-- VPLS配置命令 \-- statistics enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VPLS命令.files/image002.png){#图片 16 width="62" height="25"}]{lang="EN-US"}]{#struct_0_10012_x1780_632298935}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10012_x1780_578171000}
:::

[ ]{lang="EN-US"}

[**[statistics enable]{lang="FR"}**]{#struct_0_10012_x1780_x2145491180}[命令用来开启指定]{style="font-family:宋体"}[PW]{lang="FR"}[的统计功能。]{style="font-family:宋体"}

[**[undo statistics enable]{lang="FR"}**]{#struct_0_10012_x1780_1980433837}[命令用来关闭指定]{style="font-family:宋体"}[PW]{lang="FR"}[的统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1957363116}

[**[statistics enable]{lang="FR"}**]{#struct_0_10012_x1780_x1255025971}

[**[undo statistics enable]{lang="FR"}**]{#struct_0_10012_x1780_1971024110}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_972490610}

[[通过命令行创建的]{style="font-family:宋体"}]{#struct_0_10012_x1780_242510234}[PW]{lang="FR"}[未开启]{style="font-family:宋体"}[PW]{lang="FR"}[报文统计]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[通过]{style="font-family:
宋体"}[MIB]{lang="FR"}[创建的]{style="font-family:宋体"}[PW]{lang="FR"}[开启]{style="font-family:宋体"}[PW]{lang="FR"}[报文统计。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x590344144}

[[VSI LDP PW]{lang="EN-US"}]{#struct_0_10012_x1780_x1099302837}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1142996689}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1320621136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x37442005}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_87097986}

[[备]{style="font-family:宋体"}]{#struct_0_10012_x1780_1970958574}[PW]{lang="FR"}[是否开启统计功能与其主]{style="font-family:宋体"}[PW]{lang="FR"}[保持一致，不需要单独]{style="font-family:宋体"}[开启或关闭备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的统计功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1410174731}

[[\# ]{lang="FR"}]{#struct_0_10012_x1780_x302327951}[开启指定]{style="font-family:宋体"}[PW]{lang="FR"}[的报文统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x228438313}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp\] peer 4.4.4.4 pw-id 100]{lang="EN-US"}

[\[Sysname-vsi-vpn1-ldp-4.4.4.4-100\] statistics enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1549031889}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[reset l2vpn statistics pw]{lang="NO-BOK"}**]{#struct_0_10012_x1780_x493616109}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="NO-BOK"}**]{#struct_0_10012_x1780_x1394274403}
:::::

::: {#95151371 .myid}
[]{#_Toc339310165}[]{#_Toc404791679}[]{#struct_0_10012_x1780_x2021263816}

**VPLS \-- VPLS配置命令 \-- tunnel-policy**

------------------------------------------------------------------------

[**[tunnel-policy]{lang="EN-US"}**]{#struct_0_10012_x1780_315275078}[命令用来指定引用的隧道策略。]{style="font-family:宋体"}

[**[undo tunnel-policy]{lang="EN-US"}**]{#struct_0_10012_x1780_x2100749142}[命令用来取消引用隧道策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1029186305}

[**[tunnel-policy]{lang="EN-US"}**[ *tunnel-policy-name*]{lang="EN-US"}]{#struct_0_10012_x1780_x1761568824}

[**[undo tunnel-policy]{lang="EN-US"}**]{#struct_0_10012_x1780_x791280690}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1201265285}

[[不引用任何隧道策略。]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1179494969}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x557233513}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_314816327}[自动发现视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1257817761}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_523498450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1626288292}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_262461682}

[*[tunnel-policy-name]{lang="EN-US"}*]{#struct_0_10012_x1780_881409644}[：隧道策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x555350040}

[[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1020457539}[自动发现视图下执行本命令指定引用的隧道策略后，该视图下建立的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[都将引用该隧道策略，即根据指定的隧道策略选择承载]{style="font-family:宋体"}[PW]{lang="EN-US"}[流量的公网隧道。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_10012_x1780_314750791}[没有引用隧道策略或者引用的隧道策略尚未配置，则该]{style="font-family:宋体"}[PW]{lang="EN-US"}[根据缺省选择策略来选择隧道。缺省选择策略为按照]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道－]{style="font-family:宋体"}[\>GRE]{lang="EN-US"}[隧道－]{style="font-family:宋体"}[\>CR-LSP]{lang="EN-US"}[隧道的优先级顺序选择隧道，负载分担的隧道数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1304496973}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_2032645815}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[自动发现视图下，指定引用的隧道策略为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1553874474}

[\[Sysname\] tunnel-policy policy1]{lang="EN-US"}

[\[Sysname-tunnel-policy-policy1\] quit]{lang="EN-US"}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] tunnel-policy policy1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1763814065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel-policy]{lang="EN-US"}**]{#struct_0_10012_x1780_x464385922}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道策略）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1898761475 .myid}
[]{#_Toc404791680}[]{#struct_0_10012_x1780_402745324}

**VPLS \-- VPLS配置命令 \-- vpls-id**

------------------------------------------------------------------------

[**[vpls-id]{lang="EN-US"}**]{#struct_0_10012_x1780_314947399}[命令用来配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vpls-id]{lang="EN-US"}**]{#struct_0_10012_x1780_1612695348}[命令用来删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1396940113}

[**[vpls-id]{lang="EN-US"}**[ *vpls-id*]{lang="EN-US"}]{#struct_0_10012_x1780_x1784351734}

[**[undo vpls-id]{lang="EN-US"}**]{#struct_0_10012_x1780_781598618}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1418122678}

[[没有指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x439149613}[的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x370404786}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1218325261}[自动发现]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_314881863}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x714547519}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x2109716713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1989098222}

[*[vpls-id]{lang="EN-US"}*]{#struct_0_10012_x1780_230478492}[：]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_10012_x1780_x1542919752}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x487273492}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_x180760668}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。例如：]{style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_315078471}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x1170322873}[用来唯一标识一个]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例。只有]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[相同时，才会在]{style="font-family:宋体"}[PE]{lang="EN-US"}[之间建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[VPLS ID]{lang="EN-US"}]{#struct_0_10012_x1780_x2041086078}[应用于通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[、并采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令协议]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况。一端]{style="font-family:宋体"}[PE]{lang="EN-US"}[在通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息发布本端信息时，将]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[作为扩展团体属性一同发布给]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体（即远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[）。远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到该消息后，如果消息中的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[与本端配置的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[相同，则采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[的]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式在二者之间建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[；否则，不会在两个]{style="font-family:宋体"}[PE]{lang="EN-US"}[之间建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，不能通过重复执行]{style="font-family:宋体"}]{#struct_0_10012_x1780_x1573308144}**[vpls-id]{lang="EN-US"}**[命令来修改]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[值。必须先执行]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[vpls-id]{lang="EN-US"}**[命令删除]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[值，再通过]{style="font-family:宋体"}**[vpls-id]{lang="EN-US"}**[命令配置新的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1224012991}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_13389990}[为名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[配置]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x908773996}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] signaling-protocol ldp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto-ldp\] vpls-id 100:1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_315012935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_10012_x1780_x431076174}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_10012_x1780_1770780790}**[vsi]{lang="EN-US"}**
:::

::: {#-595395675 .myid}
[]{#_Toc404791681}[]{#struct_0_10012_x1780_482489516}[]{#_Toc339310166}

**VPLS \-- VPLS配置命令 \-- vpn-target**

------------------------------------------------------------------------

[**[vpn-target]{lang="EN-US"}**]{#struct_0_10012_x1780_x1327186018}[命令用来为当前]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo vpn-target]{lang="EN-US"}**]{#struct_0_10012_x1780_x1311812393}[命令用来删除指定的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2109442476}

[**[vpn-target]{lang="EN-US"}**[ *vpn-target*&\<1-8\> \[ **both** \| **export-extcommunity** \| **import-extcommunity** \]]{lang="EN-US"}]{#struct_0_10012_x1780_624210097}

[**[undo vpn-target]{lang="EN-US"}**[ { *vpn-target&\<1-8\>* \| **all** } \[ **both** \| **export-extcommunity** \| **import-extcommunity** \]]{lang="EN-US"}]{#struct_0_10012_x1780_315209543}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1294936699}

[[没有为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x1254442045}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式指定]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1386568665}

[[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1869891681}[自动发现视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x636237977}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_2066646042}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x1404435661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_315144007}

[*[vpn-target]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_10012_x1780_756292884}[：]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性值，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_10012_x1780_790664794}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_944072459}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_10012_x1780_2140311322}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。例如：]{style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_10012_x1780_x935875761}[：指定配置的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值同时作为]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[和]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[。没有指定]{style="font-family:宋体"}**[both]{lang="EN-US"}**[、]{style="font-family:宋体"}**[export-extcommunity]{lang="EN-US"}**[和]{style="font-family:宋体"}**[import-extcommunity]{lang="EN-US"}**[中的任何一个参数时，缺省值为]{style="font-family:宋体"}**[both]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[export-extcommunity]{lang="EN-US"}**]{#struct_0_10012_x1780_129997838}[：指定配置的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值为]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[import-extcommunity]{lang="EN-US"}**]{#struct_0_10012_x1780_x1257393482}[：指定配置的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值为]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_10012_x1780_x896997780}[：所有]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_315340615}

[[Route Target]{lang="EN-US"}]{#struct_0_10012_x1780_x499359372}[用来控制]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息（即通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息和标签块信息）的发布。本地]{style="font-family:宋体"}[PE]{lang="EN-US"}[在通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息将]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息发送给远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[时，将]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息中携带的]{style="font-family:宋体"}[VPN target]{lang="EN-US"}[属性设置为]{style="font-family:宋体"}[Export target]{lang="EN-US"}[。远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息后，将该信息中携带的]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[属性与本地配置的]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[进行比较，如果二者中存在相同的值，则接受该信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_177998936}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_726669938}[为名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[为]{style="font-family:宋体"}[10:1 100:1 1000:1]{lang="EN-US"}[，]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[为]{style="font-family:宋体"}[20:1 200:1 2000:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_48564443}

[\[Sysname\] vsi aaa]{lang="EN-US"}

[\[Sysname-vsi-aaa\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] vpn-target 10:1 100:1 1000:1 import-extcommunity]{lang="EN-US"}

[\[Sysname-vsi-aaa-auto\] vpn-target 20:1 200:1 2000:1 export-extcommunity]{lang="EN-US"}
:::

::: {#-981054953 .myid}
[]{#_Toc404791682}[]{#struct_0_10012_x1780_1005077065}

**VPLS \-- VPLS配置命令 \-- vsi**

------------------------------------------------------------------------

[**[vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_355631553}[命令用来创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[已经存在，则直接进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **vsi**]{lang="EN-US"}]{#struct_0_10012_x1780_315275079}[命令用来删除指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x2100749141}

[**[vsi]{lang="IT"}**]{#struct_0_10012_x1780_x1432470832}[ *vsi-name* \[ **hub-spoke** \]]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_10012_x1780_x1070554268}[ ]{lang="IT"}**[vsi]{lang="IT"}**[ *vsi-name*]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1204010011}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x154590231}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_113570409}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10012_x1780_x742768057}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_314816324}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_1257817758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_522908623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_414005671}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_10012_x1780_664367922}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[hub-spoke]{lang="IT"}**]{#struct_0_10012_x1780_x2066727265}**[：]{style="font-family:宋体"}**[指定]{style="font-family:宋体"}[VSI]{lang="IT"}[具有]{style="font-family:宋体"}[hub-spoke]{lang="EN-US"}[能力。如果不指定本参数，则表示]{style="font-family:宋体"}[VSI]{lang="IT"}[不]{style="font-family:宋体"}[具有]{style="font-family:宋体"}[hub-spoke]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1397185113}

[[在同一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_1483214289}[下，可以同时使用不同的方式（]{style="font-family:宋体"}[LDP]{lang="EN-US"}[、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[、静态方式等）建立多条]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[Hub-Spoke]{lang="EN-US"}]{#struct_0_10012_x1780_314750788}[是]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的一种组网应用方式。在这种组网方式下，存在一个中心站点（]{style="font-family:宋体"}[Hub]{lang="EN-US"}[站点）和多个分支站点（]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[站点），]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[站点之间的数据必须通过]{style="font-family:宋体"}[Hub]{lang="EN-US"}[站点进行交换，而不允许各个]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[站点之间直接进行数据交换。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[Hub-Spoke]{lang="EN-US"}]{#struct_0_10012_x1780_1034155178}[组网中，需要指定]{style="font-family:宋体"}[VSI]{lang="IT"}[具有]{style="font-family:宋体"}[hub-spoke]{lang="EN-US"}[能力。]{style="font-family:宋体"}[使能]{style="font-family:宋体"}[hub-spoke]{lang="EN-US"}[能力的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路（]{style="font-family:宋体"}[AC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[）中只能有一个]{style="font-family:宋体"}[Hub]{lang="EN-US"}[链路（朝向中心站点方向的链路），其它都是]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[链路（朝向分支站点方向的链路）。缺省情况下，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的所有链路均为]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[链路，需要在执行]{style="font-family:宋体"}**[xconnect]{lang="EN-US"}**[命令或]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令时通过]{style="font-family:宋体"}**[hub]{lang="EN-US"}**[关键字手工将]{style="font-family:宋体"}[AC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[指定为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1715286536}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x2139051480}[创建名为]{style="font-family:宋体"}[vpls1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_x1618876864}

[\[Sysname\] vsi vpls1]{lang="EN-US"}

[\[Sysname-vsi-vpls1\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_554068202}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1506363999}
:::

::: {#-216238939 .myid}
[]{#_Toc404791683}[]{#struct_0_10012_x1780_314947396}

**VPLS \-- VPLS配置命令 \-- xconnect vsi**

------------------------------------------------------------------------

[**[xconnect vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1612695359}[命令用来将接口或以太网服务实例与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联，并配置和]{style="font-family:宋体"}[track]{lang="EN-US"}[项的联动功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **xconnect vsi**]{lang="EN-US"}]{#struct_0_10012_x1780_x1396874576}[命令用来取消接口或以太网服务实例]{style="font-family:宋体"}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的关联及和]{style="font-family:宋体"}[track]{lang="EN-US"}[的联动。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_706993090}

[**[xconnect vsi ]{lang="EN-US"}***[vsi-name ]{lang="EN-US"}*[\[ **access-mode** { **ethernet** \| **vlan** } \| **hub** \] \* \[ **track** *track-entry-number*&\<1-3\> \]]{lang="EN-US"}]{#struct_0_10012_x1780_x21611729}

[**[undo xconnect vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_234374830}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1524882446}

[[接口或以太网服务实例没有]{style="font-family:宋体"}]{#struct_0_10012_x1780_1116019729}[与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联，且未启动和]{style="font-family:宋体"}[track]{lang="EN-US"}[项的联动功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1836829340}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10012_x1780_314881860}[以太网服务实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x714547516}

[[network-admin]{lang="EN-US"}]{#struct_0_10012_x1780_x2109913321}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10012_x1780_143675836}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x216024680}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_10012_x1780_601072669}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[access-mode]{lang="EN-US"}**]{#struct_0_10012_x1780_766824390}[：指定]{style="font-family:宋体"}[接入]{style="font-family:宋体"}[模式。当关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[为以太网服务实例时，可以指定本参数，接入模式缺省为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[；当]{style="font-family:宋体"}[AC]{lang="EN-US"}[为三层以太网接口时，接入模式始终为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[，不可以指定本参数；当]{style="font-family:宋体"}[AC]{lang="EN-US"}[为三层以太网子接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口时，接入模式始终为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，不可以指定本参数。]{style="font-family:宋体"}

[**[ethernet]{lang="EN-US"}**]{#struct_0_10012_x1780_x1243965484}[：指定]{style="font-family:宋体"}[接入模式]{style="font-family:宋体"}[为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_10012_x1780_315078468}[：指定]{style="font-family:宋体"}[接入模式]{style="font-family:宋体"}[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hub]{lang="EN-US"}**]{#struct_0_10012_x1780_785992254}[：指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内为]{style="font-family:宋体"}[hub]{lang="EN-US"}[链路。与使能了]{style="font-family:宋体"}[hub-spoke]{lang="EN-US"}[能力的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联的]{style="font-family:宋体"}[AC]{lang="EN-US"}[缺省为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的]{style="font-family:宋体"}[spoke]{lang="EN-US"}[链路。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[track]{lang="EN-US"}**]{#struct_0_10012_x1780_1762000378}[：]{style="font-family:宋体"}[配置接口或以太网服务实例与指定]{style="font-family:宋体"}[track]{lang="EN-US"}[项联动。]{style="font-family:宋体"}

[*[track-entry-number]{lang="EN-US"}*[&\<1-3\>]{lang="EN-US"}]{#struct_0_10012_x1780_958878674}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-3\>]{lang="EN-US"}[表示可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[3]{lang="EN-US"}[个序号，每个序号之间使用空格分隔。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1392565446}

[[在接口视图下执行本命令后，从接口接收到的报文将通过查找关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x178919002}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表进行转发；在某个接口的以太网服务实例视图下执行本命令后，从该接口接收到的、符合以太网服务实例报文匹配规则的报文，将通过查找关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表进行转发。]{style="font-family:宋体"}

[[接入模式是]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_10012_x1780_x1988171407}[对从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到的以太网帧携带的外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的理解方式，以及]{style="font-family:宋体"}[PE]{lang="EN-US"}[向]{style="font-family:宋体"}[CE]{lang="EN-US"}[发送以太网帧的方式。接入模式分为两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_10012_x1780_608491348}[接入模式：]{style="font-family:宋体"}[CE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[PE]{lang="EN-US"}[的以太网帧头需要带有一个]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，该]{style="font-family:宋体"}[Tag]{lang="EN-US"}[被理解为]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，即服务提供商网络为了区分用户而压入的"服务定界符"。]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送以太网帧给]{style="font-family:宋体"}[CE]{lang="EN-US"}[时，也需要携带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_10012_x1780_579134961}[接入模式：]{lang="EN-US" style="font-family:宋体"}[CE]{lang="EN-US"}[发送给]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[的以太网帧头中如果带有]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，则该]{lang="EN-US" style="font-family:宋体"}[Tag]{lang="EN-US"}[被理解为]{lang="EN-US" style="font-family:宋体"}[U-Tag]{lang="EN-US"}[，即用户网络的内部]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，对于]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[设备没有意义。]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[发送以太网帧给]{style="font-family:宋体"}[CE]{lang="EN-US"}[时，不需要携带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[配置接口或以太网服务实例与]{style="font-family:宋体"}[track]{lang="EN-US"}]{#struct_0_10012_x1780_953974378}[联动后，仅当关联的]{style="font-family:宋体"}[track]{lang="EN-US"}[项中至少有一个状态为]{style="font-family:宋体"}[positive]{lang="EN-US"}[时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[的状态才会]{style="font-family:宋体"}[up]{lang="EN-US"}[，否则，]{style="font-family:宋体"}[AC]{lang="EN-US"}[的状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10012_x1780_x20500905}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在以太网服务实例下配置该命令前，必须先配置]{lang="EN-US" style="font-family:宋体"}**[encapsulation]{lang="EN-US"}**]{#struct_0_10012_x1780_315012932}[命令]{lang="EN-US" style="font-family:
宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有使能了]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_10012_x1780_x431076177}[的]{lang="EN-US" style="font-family:宋体"}[Hub-Spoke]{lang="EN-US"}[能力后，才可以进一步指定链路类型为]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[链路或者]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[链路，缺省的链路类型为]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10012_x1780_1770715254}

[[\# ]{lang="EN-US"}]{#struct_0_10012_x1780_x1518169487}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下采用以太网服务实例]{style="font-family:宋体"}[200]{lang="EN-US"}[来匹配外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的报文，将该以太网服务实例与名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[关联，并指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内为]{style="font-family:宋体"}[hub]{lang="EN-US"}[链路，以及和]{style="font-family:宋体"}[track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:
宋体"}[2]{lang="EN-US"}[和]{style="font-family:宋体"}[3]{lang="EN-US"}[联动。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10012_x1780_1960124573}

[\[Sysname\] vsi vpn1 hub-spoke]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] encapsulation s-vid 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] xconnect vsi vpn1 hub track 1 2 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10012_x1780_x1497618916}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn interface]{lang="EN-US"}**]{#struct_0_10012_x1780_66245660}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_10012_x1780_315209540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[encapsulation]{lang="EN-US"}**]{#struct_0_10012_x1780_x1294936696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_10012_x1780_1830671670}
:::
