::::: {#-614357393 .myid}
[]{#_Toc136937987}[]{#_Toc99445936}[]{#_Toc34203769}[]{#_Toc33197993}[]{#_Toc328555079}[]{#_Toc322610583}[]{#_Toc404788711}[]{#struct_0_x6230_x1908_x1731236004}[]{#_Toc332358561}[]{#_Toc328555080}[]{#_Toc322610584}[]{#_Toc41204195}

**策略路由 \-- 策略路由配置命令 \-- apply access-vpn vpn-instance**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_x1472696257}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_1124892612}
:::

[ ]{lang="EN-US"}

[**[apply access-vpn vpn-instance]{lang="EN-US"}**]{#struct_0_x6230_x1908_1019616269}[命令用来设置报文在指定]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[中进行转发]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo apply access-vpn vpn-instance]{lang="EN-US"}**]{#struct_0_x6230_x1908_191622675}[命令用来取消报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[中进行转发的设置或者删除一个或多个指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例对应的配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x2086474080}

[**[apply access-vpn vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_1642126726}

[**[undo apply access-vpn vpn-instance]{lang="EN-US"}**[ \[ *vpn-instance-name*&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_x6230_x1908_1496287254}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1671967347}

[[未设置]{style="font-family:宋体"}]{#struct_0_x6230_x1908_653756063}[报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[中进行转发。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_431093455}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1472761793}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1990435360}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x296425918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_88179701}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x380373448}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1839869966}[：表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_50098685}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1509967751}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1826616909}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。当满足匹配规则后，将根据第一个可用的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例转发表进行转发。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1472303041}[命令时，如果指定了]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名，将删除该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例对应的配置；如果未指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名，将取消报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内转发的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_570991763}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_211054512}[在策略节点中设置]{style="font-family:宋体"}[报文在名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[、]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[中进行转发]{style="font-family:宋体"}[（]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[、]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[已存在）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1822665066}

[\[Sysname\] policy-based-route policy1 permit node 10]{lang="EN-US"}

[\[Sysname-pbr-policy1-10\] apply access-vpn vpn-instance vpn1 vpn2]{lang="EN-US"}
:::::

::::: {#317473173 .myid}
[]{#_Toc404788712}[]{#struct_0_x6230_x1908_x842436371}[]{#_Toc332358562}[]{#_Toc328555089}

**策略路由 \-- 策略路由配置命令 \-- apply continue**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_x1112189519}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_x2050509278}
:::

[ ]{lang="EN-US"}

[**[apply continue]{lang="EN-US"}**]{#struct_0_x6230_x1908_266254116}[命令用来设置匹配成功的当前节点指定转发路径失败后，继续进行后续节点的处理。]{style="font-family:宋体"}

[**[undo apply continue]{lang="EN-US"}**]{#struct_0_x6230_x1908_x774783990}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472368577}

[**[apply continue]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1217819786}

[**[undo apply continue]{lang="EN-US"}**]{#struct_0_x6230_x1908_2085001160}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x576397422}

[[匹配成功的当前节点指定转发路径失败后，不再进行下一节点的匹配。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1722370370}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1505768451}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1412810843}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x790363103}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472827328}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1711899865}

[[【使用指导】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_x1767960701}

[[本命令仅在策略节点的匹配模式为]{style="font-family:宋体"}**[permit]{lang="EN-US"}**]{#struct_0_x6230_x1908_1664269684}[时生效。]{style="font-family:宋体"}

[[在配置了该命令后，如果当前节点中没有配置影响报文转发路径的五个]{style="font-family:宋体"}**[apply]{lang="EN-US"}**]{#struct_0_x6230_x1908_1483154376}[子句（]{style="font-family:宋体"}**[apply access-vpn vpn-instance]{lang="EN-US"}**[、]{style="font-family:
宋体"}**[apply next-hop]{lang="EN-US"}**[、]{style="font-family:宋体"}**[apply output-interface]{lang="EN-US"}**[、]{style="font-family:宋体"}**[apply default-next-hop]{lang="EN-US"}**[和]{style="font-family:宋体"}**[apply default-output-interface]{lang="EN-US"}**[），或者配置了这五个子句中的一个或多个，但配置的子句都失效（下一跳不可达、出接口]{style="font-family:宋体"}[down]{lang="EN-US"}[或者报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内转发失败）时，会进行下一节点的处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1908782654}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_1425282068}[设置]{style="font-family:宋体"}[匹配成功的]{style="font-family:宋体"}[当前]{style="font-family:宋体"}[节点转发失败后继续进行后续节点的处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_1345002842}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply continue]{lang="EN-US"}
:::::

::::: {#136921610 .myid}
[]{#_Toc404788713}[]{#struct_0_x6230_x1908_1459903140}[]{#_Toc332358563}[]{#_Toc328555085}[]{#_Toc322610588}

**策略路由 \-- 策略路由配置命令 \-- apply default-next-hop**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_x1472892864}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_172875151}
:::

[ ]{lang="EN-US"}

[**[apply default-next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_x70408168}[命令用来设置指导报文转发的缺省下一跳。]{style="font-family:宋体"}

[**[undo apply default-next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1817484016}[命令用来取消指导报文转发的缺省下一跳的设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1415318448}

[**[apply default-next-hop ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name \|* **inbound-vpn** \] { *ip-address* \[ **direct** \] \[ **track** *track-entry-number* \] }&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_1689667015}

[**[undo apply default-next-hop ]{lang="EN-US"}**[\[ \[ **vpn-instance** *vpn-instance-name \|* **inbound-vpn** \] *ip-address*&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_x6230_x1908_x919087871}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_x1084733871}

[[未设置指导报文转发的缺省下一跳。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1472958400}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x379240765}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x968097321}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x102412129}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_681445422}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x565528182}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_1036418132}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_x322455184}[：缺省下一跳所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[**[inbound-vpn]{lang="EN-US"}**]{#struct_0_x6230_x1908_1831969679}[：报文入接口所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1473023936}[：]{style="font-family:宋体"}[缺省]{style="font-family:宋体"}[下一跳的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。不指定]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[或]{style="font-family:宋体"}**[inbound-vpn]{lang="EN-US"}**[参数，表示指定的是公网下一跳。]{style="font-family:宋体"}

[**[direct]{lang="EN-US"}**]{#struct_0_x6230_x1908_1614535662}[：指定当前缺省下一跳生效的条件为直连下一跳。]{style="font-family:宋体"}

[**[track]{lang="EN-US"}**[ *track-entry-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_847340112}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_x97855089}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_x1174666647}

[[用户可以同时配置多个缺省下一跳（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_253326028}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_x6230_x1908_660211807}[个缺省下一跳。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x6230_x1908_x350639394}[命令时，如果指定了缺省下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，将取消已配置的该缺省下一跳；如果没有指定缺省下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，将取消已配置的所有缺省下一跳。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_x585948401}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x1044733834}[设置指导报文转发的缺省直连下一跳为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472565184}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply default-next-hop 1.1.1.1 direct]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_913517993}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_x6230_x1908_x369335488}
:::::

::::: {#-1403479646 .myid}
[]{#_Toc404788714}[]{#struct_0_x6230_x1908_425158642}[]{#_Toc332358565}[]{#_Toc328555087}[]{#_Toc322610590}[]{#_Toc345338970}[]{#_Toc345338971}[]{#_Toc345338972}[]{#_Toc345338973}[]{#_Toc345338974}[]{#_Toc345338975}[]{#_Toc345338976}[]{#_Toc345338977}[]{#_Toc345338978}[]{#_Toc345338979}[]{#_Toc345338980}[]{#_Toc345338981}[]{#_Toc345338982}[]{#_Toc345338983}[]{#_Toc345338984}[]{#_Toc345338985}[]{#_Toc345338986}[]{#_Toc345338987}[]{#_Toc345338988}[]{#_Toc345338989}[]{#_Toc345338990}[]{#_Toc345338991}[]{#_Toc345338992}[]{#_Toc345338993}[]{#_Toc345338994}[]{#_Toc345338995}[]{#_Toc345338996}[]{#_Toc345338997}

**策略路由 \-- 策略路由配置命令 \-- apply default-output-interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_856577169}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_x979508763}
:::

[ ]{lang="EN-US"}

[**[apply default-output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_x694657654}[命令用来设置指导报文转发的缺省出接口。]{style="font-family:宋体"}

[**[undo apply default-output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_x2051761402}[命令用来取消指导报文转发的缺省出接口的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x275969069}

[**[apply default-output-interface ]{lang="EN-US"}**[{ ]{lang="EN-US"}*[interface-type interface-number ]{lang="EN-US"}*[\[ **track** *track-entry-number* \] }&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472630720}

[**[undo apply default-output-interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}[{ *interface-type interface-number* }&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_x6230_x1908_429018806}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1501651345}

[[未设置指导报文转发的缺省出接口。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_904690664}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1643685673}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_275572157}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_860070876}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_571073089}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1418464066}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472696256}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x441191329}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[**[track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_142247268}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_x61662054}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x56831262}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[用户可以同时配置多个缺省出接口（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x475788746}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_x6230_x1908_x626238010}[个缺省出接口。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[指定缺省出接口类型需配置为]{style="font-family:宋体"}[P2P]{lang="EN-US"}]{#struct_0_x6230_x1908_x94132850}[（]{style="font-family:宋体"}[Point-to-Point]{lang="EN-US"}[，点到点）接口，对于非]{style="font-family:宋体"}[P2P]{lang="EN-US"}[接口（广播类型的接口和]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型的接口），比如以太网接口、]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口，由于有多个可能的下一跳，可能会造成报文转发不成功的现象。]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[（]{style="font-family:宋体"}[Non Broadcast MultiAccess]{lang="EN-US"}[，非广播多路访问）指全连通、非广播、多点可达的网络，这种网络采用单播方式发送报文。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x6230_x1908_1514911173}[命令时，如果指定了接口，将取消已配置的该缺省出接口；如果没有指定接口，将取消已配置的所有缺省出接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_x1472761792}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x424351419}[设置报文的缺省出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1372949101}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply default-output-interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x580086443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_x6230_x1908_1887972663}
:::::

::::: {#989277777 .myid}
[]{#_Toc404788715}[]{#struct_0_x6230_x1908_1777175831}[]{#_Toc332358567}[]{#_Toc345338999}[]{#_Toc345339000}[]{#_Toc345339001}[]{#_Toc345339002}[]{#_Toc345339003}[]{#_Toc345339004}[]{#_Toc345339005}[]{#_Toc345339006}[]{#_Toc345339007}[]{#_Toc345339008}[]{#_Toc345339009}[]{#_Toc345339010}[]{#_Toc345339011}[]{#_Toc345339012}[]{#_Toc345339013}[]{#_Toc345339014}[]{#_Toc345339015}[]{#_Toc345339016}[]{#_Toc345339017}[]{#_Toc345339018}[]{#_Toc345339019}[]{#_Toc345339020}[]{#_Toc345339021}[]{#_Toc345339022}[]{#_Toc345339023}[]{#_Toc345339024}[]{#_Toc345339025}[]{#_Toc345339026}

**策略路由 \-- 策略路由配置命令 \-- apply ip-df**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_1969656505}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_1458900780}
:::

[ ]{lang="EN-US"}

[**[apply ip-df]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1472303040}[命令用来设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中的]{style="font-family:宋体"}[DF]{lang="EN-US"}[（]{style="font-family:宋体"}[Don't Fragment]{lang="EN-US"}[，不分片）]{style="font-family:宋体"}[标志。]{style="font-family:宋体"}

[**[undo apply ip-df]{lang="EN-US"}**]{#struct_0_x6230_x1908_2137075704}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1892598163}

[**[apply ip-df ]{lang="EN-US"}***[df-value]{lang="EN-US"}*]{#struct_0_x6230_x1908_1787278124}

[**[undo apply ip-df]{lang="EN-US"}**]{#struct_0_x6230_x1908_245748441}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1614985559}

[[不对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6230_x1908_1238678301}[报文头中的]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志进行设置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x253838927}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1888327655}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1943743133}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472368576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_348264155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_2004476880}

[*[df-value]{lang="EN-US"}*]{#struct_0_x6230_x1908_x391446245}[：设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中的]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志，取值]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}[0]{lang="EN-US"}[表示将]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文头中的]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志位置为]{style="font-family:宋体"}[0]{lang="EN-US"}[；]{style="font-family:宋体"}[1]{lang="EN-US"}[表示将]{style="font-family:
宋体"}[IP]{lang="EN-US"}[报文头中的]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志位置为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1002835807}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[报文中]{style="font-family:宋体"}[DF]{lang="EN-US"}]{#struct_0_x6230_x1908_x1053660695}[标志位置为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示可以对报文进行分片处理。]{style="font-family:宋体"}

[[报文中]{style="font-family:宋体"}[DF]{lang="EN-US"}]{#struct_0_x6230_x1908_x878614064}[标志位置为]{style="font-family:宋体"}[1]{lang="EN-US"}[，表示不可对报文进行分片处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x154872529}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x1845032487}[将报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[首部的]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志]{style="font-family:宋体"}[位]{style="font-family:宋体"}[置为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472827331}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply ip-df 0]{lang="EN-US"}
:::::

::: {#362027212 .myid}
[]{#_Toc404788716}[]{#struct_0_x6230_x1908_1373279386}[]{#_Toc343613569}

**策略路由 \-- 策略路由配置命令 \-- apply loadshare**

------------------------------------------------------------------------

[**[apply loadshare]{lang="EN-US"}**]{#struct_0_x6230_x1908_x901964850}[命令用来设置多个下一跳]{style="font-family:宋体"}[(]{lang="EN-US"}[出接口、缺省下一跳和缺省出接口]{style="font-family:宋体"}[)]{lang="EN-US"}[工作在负载分担模式。]{style="font-family:宋体"}

[**[undo apply loadshare]{lang="EN-US"}**]{#struct_0_x6230_x1908_1316144176}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1587140469}

[**[apply loadshare]{lang="EN-US"}**[ { **default-next-hop** \| **default-output-interface** \| **next-hop \| output-interface** }]{lang="EN-US"}]{#struct_0_x6230_x1908_x1950582952}

[**[undo apply loadshare]{lang="EN-US"}**[ { **default-next-hop** \| **default-output-interface** \| **next-hop \| output-interface** }]{lang="EN-US"}]{#struct_0_x6230_x1908_1078161526}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_144949323}

[[多个下一跳]{style="font-family:宋体"}[(]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472892867}[出接口、缺省下一跳和缺省出接口]{style="font-family:宋体"}[)]{lang="EN-US"}[工作在主备模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_576159678}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x467009850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x483528674}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1498374154}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x966072081}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_859113870}

[**[default-]{lang="EN-US"}[next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_523292028}[：设置指导报文转发的多个缺省下一跳工作在负载分担模式。]{style="font-family:宋体"}

[**[default-output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_984744712}[：设置指导报文转发的多个缺省出接口工作在负载分担模式。]{style="font-family:宋体"}

[**[next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1472958403}[：设置指导报文转发的多个下一跳工作在负载分担模式。]{style="font-family:宋体"}

[**[output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_24043762}[：设置指导报文转发的多个出接口工作在负载分担模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_359660799}

[[多个出接口]{style="font-family:宋体"}[(]{lang="EN-US"}]{#struct_0_x6230_x1908_x1434073856}[下一跳、缺省下一跳和缺省出接口]{style="font-family:宋体"}[)]{lang="EN-US"}[的工作模式有两种：主备模式、负载分担模式。以多个出接口为例：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主备模式：按照配置顺序，以第一个配置的出接口作为主用出接口，指导报文转发。当主用出接口失效时，按配置顺序选择后续的第一个有效的出接口指导报文转发。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1309528490}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[负载分担模式：按照配置顺序，逐包轮流选择有效的出接口指导报文转发。下一跳的负载分担模式则有些不同，会按照下一跳的权重指导报文转发。缺省情况下，多个下一跳会按照缺省的权重值平均分配带宽，多个下一跳的转发流量的比例是相同的。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_874694696}

[[缺省下一跳和缺省出接口的情况请参考多个出接口。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_659333865}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x400583247}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_328760492}[设置多个下一跳工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1473023939}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply next-hop 1.1.1.1 2.2.2.2]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply loadshare next-hop]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_498790415}[设置多个出接口工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x423087219}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply output-interface Vlan-interface 1 Vlan-interface 2]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply loadshare output-interface]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_1098091480}[设置多个缺省下一跳工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_1201267722}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply default-next-hop 1.1.1.1 2.2.2.2]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply loadshare default-next-hop]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_1262060027}[设置多个缺省出接口工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472565187}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply default-output-interface Vlan-interface 1 Vlan-interface 2]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply loadshare default-output-interface]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_510233466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply default-next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_1454826875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply default-output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_x283482004}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_1737972660}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_1424096559}
:::

::::: {#-1850744860 .myid}
[]{#_Toc404788717}[]{#struct_0_x6230_x1908_1344096941}[]{#_Toc345339029}[]{#_Toc342567227}

**策略路由 \-- 策略路由配置命令 \-- apply next-hop**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image002.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_667191352}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_x108098367}
:::

**[ ]{lang="EN-US"}**

[**[apply next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1472630723}[命令用来设置报文转发的下一跳。]{style="font-family:宋体"}

[**[undo apply next-hop]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1137065135}[命令用来取消报文转发下一跳的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_124780111}

[**[apply next-hop]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \| **inbound-vpn** \] { *ip-address* \[ **direct** \] \[ **track** *track-entry-number* \] \[ **weight** *weight-value* \] }&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_721598312}

[**[undo apply next-hop]{lang="EN-US"}**[ \[ \[ **vpn-instance** *vpn-instance-name* \| **inbound-vpn** \] *ip-address*&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_x6230_x1908_x20476231}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_633407568}

[[未设置报文转发的下一跳。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_281063575}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_2043303612}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1889976854}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472696259}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_318323558}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_2035332541}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1378283817}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_906865123}[：下一跳所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[**[inbound-vpn]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1949047350}[：报文入接口所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x6230_x1908_467514054}[：]{style="font-family:宋体"}[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[不指定]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[或]{style="font-family:宋体"}**[inbound-vpn]{lang="EN-US"}**[参数，表示指定的是公网下一跳。]{style="font-family:宋体"}

[**[direct]{lang="EN-US"}**]{#struct_0_x6230_x1908_x765583458}[：指定当前下一跳生效的条件为直连下一跳。]{style="font-family:宋体"}

[**[track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x332693768}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472761795}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight ]{lang="EN-US"}***[weight-value]{lang="EN-US"}*]{#struct_0_x6230_x1908_273317061}[：指定]{style="font-family:宋体"}[下一跳负载分担的权重。设备根据权重确定该下一跳转发流量的比例。例如，三个下一跳配置的负载分担权重分别为]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[2]{lang="EN-US"}[，则它们的负载分担的比例分别为]{style="font-family:
宋体"}[1/4]{lang="EN-US"}[、]{style="font-family:
宋体"}[1/4]{lang="EN-US"}[和]{style="font-family:宋体"}[1/2]{lang="EN-US"}[。]{style="font-family:宋体"}*[weight-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1183866306}

[[用户可以同时配置多个下一跳（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1600490904}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1057626561}[个下一跳。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x6230_x1908_852916211}[命令时，如果指定了下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，将取消已配置的该下一跳；如果没有指定下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，将取消已配置的所有下一跳。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x303614274}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_2090451985}[设置报文的直连下一跳为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_1382799373}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply next-hop 1.1.1.1 direct]{lang="EN-US"}

[]{#_Toc136937990}[]{#_Toc99445939}[]{#_Toc34203772}[]{#_Toc33197996}[]{#struct_0_x6230_x1908_x1594013989}[]{#_Toc302486745}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1472303043}
:::::

::::: {#1859300671 .myid}
[]{#_Toc404788718}[]{#struct_0_x6230_x1908_x591807651}[]{#_Toc332358570}[]{#_Toc328555083}[]{#_Toc322610586}[]{#_Toc319174130}[]{#_Toc345339031}[]{#_Toc345339032}[]{#_Toc345339033}[]{#_Toc345339034}[]{#_Toc345339035}[]{#_Toc345339036}[]{#_Toc345339037}[]{#_Toc345339038}[]{#_Toc345339039}[]{#_Toc345339040}[]{#_Toc345339041}[]{#_Toc345339042}[]{#_Toc345339043}[]{#_Toc345339044}[]{#_Toc345339045}[]{#_Toc345339046}[]{#_Toc345339047}[]{#_Toc345339048}[]{#_Toc345339049}[]{#_Toc345339050}[]{#_Toc345339051}[]{#_Toc345339052}[]{#_Toc345339053}[]{#_Toc345339054}[]{#_Toc345339055}[]{#_Toc345339056}[]{#_Toc345339057}[]{#_Toc345339058}

**策略路由 \-- 策略路由配置命令 \-- apply output-interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_1653119808}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_1208898862}
:::

[ ]{lang="EN-US"}

[**[apply output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1715615808}[命令用来设置指导报文转发的出接口。]{style="font-family:宋体"}

[**[undo apply output-interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_922045734}[命令用来取消指导报文转发的出接口的设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1752703899}

[**[apply output-interface ]{lang="EN-US"}**[{ *interface-type interface-number* \[ **track** *track-entry-number* \] }&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_1910386126}

[**[undo apply output-interface ]{lang="EN-US"}**[\[ { *interface-type* *interface-number* }&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_x6230_x1908_268103296}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472368579}

[[未设置指导报文转发的出接口。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_301209988}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1400974568}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1224542927}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x2145058305}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x940031088}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_1911325949}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1856791317}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_1508356118}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[**[track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1472827330}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_x6230_x1908_x1355603969}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x924708618}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[用户可以同时配置多个出接口（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_732538452}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_x6230_x1908_514213771}[个出接口。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[指定出接口类型需配置为]{style="font-family:宋体"}[P2P]{lang="EN-US"}]{#struct_0_x6230_x1908_143715245}[接口，对于非]{style="font-family:宋体"}[P2P]{lang="EN-US"}[接口（广播类型的接口和]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型的接口），比如以太网接口、]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口，由于有多个可能的下一跳，可能会造成报文转发不成功的现象。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x6230_x1908_x2111111625}[命令时，如果指定了接口，将取消已配置的该出接口；如果未指定接口，将取消已配置的所有出接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x2062188957}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472892866}[对已经匹配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文指定出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x989924263}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply output-interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1397614667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_x6230_x1908_x321674099}
:::::

::::: {#908845892 .myid}
[]{#_Toc404788719}[]{#struct_0_x6230_x1908_1570451253}[]{#_Toc332358572}[]{#_Toc345339060}[]{#_Toc345339061}[]{#_Toc345339062}[]{#_Toc345339063}[]{#_Toc345339064}[]{#_Toc345339065}[]{#_Toc345339066}[]{#_Toc345339067}[]{#_Toc345339068}[]{#_Toc345339069}[]{#_Toc345339070}[]{#_Toc345339071}[]{#_Toc345339072}[]{#_Toc345339073}[]{#_Toc345339074}[]{#_Toc345339075}[]{#_Toc345339076}[]{#_Toc345339077}[]{#_Toc345339078}[]{#_Toc345339079}[]{#_Toc345339080}[]{#_Toc345339081}[]{#_Toc345339082}[]{#_Toc345339083}[]{#_Toc345339084}[]{#_Toc345339085}[]{#_Toc345339086}[]{#_Toc345339087}

**策略路由 \-- 策略路由配置命令 \-- apply precedence**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_602390500}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_624146737}
:::

[ ]{lang="EN-US"}

[**[apply precedence]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_x6230_x1908_1102831309}[命令用来设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的优先级。]{style="font-family:宋体"}

[**[undo apply precedence]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1472958402}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1542040179}

[**[apply precedence ]{lang="EN-US"}**[{ *type* \| *value* }]{lang="EN-US"}]{#struct_0_x6230_x1908_x1904886402}

[**[undo apply precedence]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1177617204}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_575170631}

[[不对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6230_x1908_x813016816}[报文的优先级进行设置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1945418478}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1618602023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_568990634}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1325642088}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1473023938}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_2064874356}

[*[type]{lang="EN-US"}*]{#struct_0_x6230_x1908_x885319500}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的优先级类型。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_x6230_x1908_333845580}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的优先级值，]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文共有]{style="font-family:宋体"}[8]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:
宋体"}[7]{lang="EN-US"}[）个优先级，每个数值对应一个优先级类型。在输入参数的时候可以输入数值，也可以输入优先级类型。对应关系如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-1]{lang="EN-US"}](?908845892#_Ref329186298)[所示。]{style="font-family:
宋体"}

[]{#struct_0_x6230_x1908_x1996700138}[]{#_Ref329186298}[]{#_Toc138413934}[]{#_Toc138241327}[]{#_Toc95361162}[]{#_Toc85613765}[]{#_Toc81391285}[]{#_Toc74710506}[]{#_Toc72591630}[]{#_Toc65926761}[[表1-1 ]{lang="EN-US"}[IP]{lang="EN-US"}]{#_Toc60123195}[优先级值与优先级类型对应表]{style="font-family:黑体"}

[]{#table_struct_0_x1879550050}[[优先级值]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1102414143}
:::::

[[优先级类型]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x124455474}

[[0]{lang="EN-US"}]{#struct_0_x6230_x1908_650683276}

[[routine]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472565186}

[[1]{lang="EN-US"}]{#struct_0_x6230_x1908_2076317407}

[[priority]{lang="EN-US"}]{#struct_0_x6230_x1908_x2057998614}

[[2]{lang="EN-US"}]{#struct_0_x6230_x1908_x978342026}

[[immediate]{lang="EN-US"}]{#struct_0_x6230_x1908_x1540494506}

[[3]{lang="EN-US"}]{#struct_0_x6230_x1908_2121091728}

[[flash]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472630722}

[[4]{lang="EN-US"}]{#struct_0_x6230_x1908_1591818220}

[[flash-override]{lang="EN-US"}]{#struct_0_x6230_x1908_x673729842}

[[5]{lang="EN-US"}]{#struct_0_x6230_x1908_219801906}

[[critical]{lang="EN-US"}]{#struct_0_x6230_x1908_1413952191}

[[6]{lang="EN-US"}]{#struct_0_x6230_x1908_x1969939759}

[[internet]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472696258}

[[7]{lang="EN-US"}]{#struct_0_x6230_x1908_x1247760383}

[[network]{lang="EN-US"}]{#struct_0_x6230_x1908_x1908076012}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x985588129}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_935960561}[设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的优先级为]{style="font-family:宋体"}[5]{lang="EN-US"}[（]{style="font-family:宋体"}[critical]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_881785711}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] apply precedence critical]{lang="EN-US"}

::: {#-372696146 .myid}
[]{#_Toc404788720}[]{#struct_0_x6230_x1908_x1066757038}

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route**

------------------------------------------------------------------------

[**[display ip policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1472761794}[命令用来显示已经配置的策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_382217635}

[**[display ip policy-based-route ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ policy ]{lang="EN-US"}***[policy]{lang="EN-US"}[-name ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_x6230_x1908_1485980174}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_680359502}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1783909541}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1073658351}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_1530784988}

[[network-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_x1559477675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_839305894}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472303042}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_974276290}

[**[policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1849919386}[：显示指定的策略。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[表示策略名，唯一标识一个策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1507017528}

[[如果不指定策略名，将显示所有已经配置的策略；如果指定策略名，将显示指定的策略。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1329168828}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1400448873}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x1773858878}[显示所有已经配置的策略。]{style="font-family:宋体"}

[[\<Sysname\> display ip policy-based-route]{lang="EN-US"}]{#struct_0_x6230_x1908_1360893883}

[Policy name: aaa]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 1.1.1.1]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ip policy-based-route]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472368578}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1886592184}[[字段]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1867293929}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x499011107}

[[Policy name]{lang="EN-US"}]{#struct_0_x6230_x1908_143569062}

[[策略名]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1655958313}

[[node 1 permit]{lang="EN-US"}]{#struct_0_x6230_x1908_963997458}

[[节点]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x6230_x1908_1111450007}[的匹配模式为允许]{style="font-family:宋体"}

[[if-match acl]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472827333}

[[满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x6230_x1908_x1758888496}[的报文被匹配]{style="font-family:宋体"}

[[apply next-hop]{lang="EN-US"}]{#struct_0_x6230_x1908_1865555805}

[[为匹配的报文指定下一跳]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x349201872}

[ ]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_686196032}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x2079115540}

::: {#-899376548 .myid}
[]{#_Toc404788721}[]{#struct_0_x6230_x1908_x1955773877}[]{#_Toc136937992}[]{#_Toc99445941}[]{#_Toc34203774}[]{#_Toc33197998}

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route interface**

------------------------------------------------------------------------

[**[display ip policy-based-route interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1243867022}[命令用来显示接口下转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472892869}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x230409376}

[**[display ip policy-based-route interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x82505003}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6230_x1908_983892085}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip policy-based-route interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6230_x1908_x393726959}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6230_x1908_1303056251}[模式：]{style="font-family:宋体"}

[**[display ip policy-based-route interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6230_x1908_936512803}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x789066532}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1596271934}[]{#_Hlt24184728}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472958405}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1138755652}

[[network-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_x1069166697}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x376941632}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_x1210741176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_844854702}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x748153323}[：用来指定接口的类型和编号。]{style="font-family:宋体"}

[]{#OLE_LINK3}[]{#OLE_LINK2}[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1132356559}[：显示指定单板上转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x879047739}[：显示指定成员设备上转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x802305628}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的转发策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_x1473023941}[：显示指定成员设备上指定单板上转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_1476239033}[：]{style="font-family:宋体"}[显示指定单板上的转发策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_627842816}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上转发策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_855348455}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_1125346244}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip policy-based-route interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472565189}

[Policy based routing information for interface GigabitEthernet1/0/1(failed):]{lang="EN-US"}

[Policy name: aaa]{lang="EN-US"}

[  node 0 deny:]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 3999]{lang="EN-US"}

[  Matched: 0 ]{lang="EN-US"}

[  node 2 permit:]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 2.2.2.2]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 5 permit:]{lang="EN-US"}

[    if-match acl 3101]{lang="EN-US"}

[    apply next-hop 1.1.1.1]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/2 track 1 (down)]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/3 track 2 (inactive)]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[Total matched: 0]{lang="EN-US"}

[\<Sysname\> display ip policy-based-route interface gigabitethernet 1/0/1]{lang="EN-US"}

[Policy based routing information for interface GigabitEthernet1/0/1:]{lang="EN-US"}

[Policy name: aaa]{lang="EN-US"}

[  node 0 deny(not support):]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 3999]{lang="EN-US"}

[  Matched: 0 ]{lang="EN-US"}

[  node 2 permit(no resource):]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 2.2.2.2]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/2 track 1 (down)]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/3 track 2 (inactive)]{lang="EN-US"}

[  Matched: 0 ]{lang="EN-US"}

[  node 5 permit:]{lang="EN-US"}

[    if-match acl 3101]{lang="EN-US"}

[    apply next-hop 1.1.1.1]{lang="EN-US"}

[  Matched: 0 (no statistics resource)]{lang="EN-US"}

[Total matched: 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ip policy-based-route interface]{lang="EN-US"}]{#struct_0_x6230_x1908_2029263240}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1884731652}[[字段]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1323730154}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472630725}

[[Policy based routing information for interface GigabitEthernet1/0/1(failed)]{lang="EN-US"}]{#struct_0_x6230_x1908_25734279}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x6230_x1908_1732471796}[下转发策略路由的配置信息和统计信息（]{style="font-family:宋体"}[failed]{lang="EN-US"}[表示策略下发驱动失败，此时所有节点都下发失败，不再显示节点一级的失败提示）]{style="font-family:宋体"}

[[![说明](策略路由命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6230_x1908_x683958268}

[[显示全局接口（]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_1899864180}[全局接口只有一维编号]{style="font-family:
  KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[例如]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="PT-BR"}[接口]{style="font-family:KaiTi_GB2312"}[10]{lang="PT-BR"}[）的信息时，]{style="font-family:KaiTi_GB2312"}[必须在命令中指定]{style="font-family:KaiTi_GB2312"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[或]{style="font-family:KaiTi_GB2312"}**[chassis]{lang="PT-BR"}**[ *chassis-number* **slot** *slot-number*]{lang="PT-BR"}[参数]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[才会显示括号中的信息。]{style="font-family:KaiTi_GB2312"}

[[Policy name]{lang="EN-US"}]{#struct_0_x6230_x1908_1674717721}

[[策略名]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x797541462}

[[node 0 deny(not support)]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472696261}

[[node 2 permit(no resource)]{lang="EN-US"}]{#struct_0_x6230_x1908_x37841266}

[[节点的匹配模式为允许]{style="font-family:宋体"}]{#struct_0_x6230_x1908_970910651}[（]{style="font-family:宋体"}[permit]{lang="PT-BR"}[）]{style="font-family:宋体"}[/]{lang="EN-US"}[拒绝]{style="font-family:宋体"}[（]{style="font-family:宋体"}[deny]{lang="PT-BR"}[）。（]{style="font-family:宋体"}[not support]{lang="PT-BR"}[表示设备]{style="font-family:宋体"}[不支持该节点设置的规则]{style="font-family:宋体"}[；]{style="font-family:宋体"}[no resource]{lang="PT-BR"}[表示设备的]{style="font-family:宋体"}[ACL]{lang="PT-BR"}[等资源不足，为该节点分配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[等资源失败]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[![说明](策略路由命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6230_x1908_x941675769}

[[显示全局接口（]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_1936044993}[全局接口只有一维编号]{style="font-family:
  KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[例如]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="PT-BR"}[接口]{style="font-family:KaiTi_GB2312"}[10]{lang="PT-BR"}[）的信息时，]{style="font-family:KaiTi_GB2312"}[必须在命令中指定]{style="font-family:KaiTi_GB2312"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[或]{style="font-family:KaiTi_GB2312"}**[chassis]{lang="PT-BR"}**[ *chassis-number* **slot** *slot-number*]{lang="PT-BR"}[参数]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[才会显示括号中的信息。]{style="font-family:KaiTi_GB2312"}

[[if-match acl]{lang="EN-US"}]{#struct_0_x6230_x1908_42287782}

[[满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472761797}[的报文被匹配]{style="font-family:宋体"}

[[apply next-hop]{lang="EN-US"}]{#struct_0_x6230_x1908_x21066892}

[[为匹配的报文指定下一跳]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1773828021}

[[apply output-interface GigabitEthernet1/0/2 track 1 (down)]{lang="EN-US"}]{#struct_0_x6230_x1908_x35156184}

[[为匹配的报文指定出接口。括号中显示接口的状态：]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x6230_x1908_663256531}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[、]{style="font-family:宋体"}[inactive]{lang="EN-US"}[。接口不在位时，显示]{style="font-family:宋体"}[inactive]{lang="EN-US"}[；接口网络层]{style="font-family:宋体"}[down]{lang="EN-US"}[时，显示]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Matched: 0 (no statistics resource)]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472303045}

[[节点匹配成功的次数（]{style="font-family:宋体"}[no statistics resource]{lang="EN-US"}]{#struct_0_x6230_x1908_x1398376705}[表示统计资源不足）]{style="font-family:宋体"}

[[![说明](策略路由命令.files/image001.png){#图片 2 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6230_x1908_857570861}

[[显示全局接口（]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_1523493301}[全局接口只有一维编号]{style="font-family:
  KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[例如]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="PT-BR"}[接口]{style="font-family:KaiTi_GB2312"}[10]{lang="PT-BR"}[）的信息时，]{style="font-family:KaiTi_GB2312"}[必须在命令中指定]{style="font-family:KaiTi_GB2312"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[或]{style="font-family:KaiTi_GB2312"}**[chassis]{lang="PT-BR"}**[ *chassis-number* **slot** *slot-number*]{lang="PT-BR"}[参数]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[才会显示括号中的信息。]{style="font-family:KaiTi_GB2312"}

[[Total matched]{lang="EN-US"}]{#struct_0_x6230_x1908_877826348}

[[策略所有节点匹配成功的次数]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1472368581}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x55610196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip policy-based-route statistics]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1420788376}

::: {#-856535727 .myid}
[]{#_Toc136937991}[]{#_Toc99445940}[]{#_Toc34203773}[]{#_Toc33197997}[]{#_Toc404788722}[]{#struct_0_x6230_x1908_1811116214}[]{#_Toc332358575}[]{#_Toc328555095}[]{#_Toc322610594}

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route local**

------------------------------------------------------------------------

[**[display ip policy-based-route local]{lang="EN-US"}**]{#struct_0_x6230_x1908_x705761731}[命令用来显示本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1654154780}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x6230_x1908_703222397}

[**[display ip policy-based-route local]{lang="EN-US"}**]{#struct_0_x6230_x1908_x20287501}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472827332}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip policy-based-route local]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6230_x1908_x192804555}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6230_x1908_x1319306992}[模式：]{style="font-family:宋体"}

[**[display ip policy-based-route local ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x6230_x1908_503685000}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1269891759}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_639420258}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1138184632}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1822211441}

[[network-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_2138600043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472892868}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_x1796493317}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x963827945}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1996533247}[：显示指定单板上本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_1622891520}[：显示指定成员设备上本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x42856277}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[本地策略路由的配置信息和统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_x997546124}[：显示指定成员设备上指定单板上本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_x1651185038}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[本地策略路由的配置信息和统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_627777279}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[本地策略路由的配置信息和统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x291893446}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x721565484}[显示本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip policy-based-route local]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472958404}

[Policy based routing information for local:]{lang="EN-US"}

[Policy name: aaa]{lang="EN-US"}

[  node 0 deny:]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 3999]{lang="EN-US"}

[  Matched: 0 ]{lang="EN-US"}

[  node 2 permit:]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 2.2.2.2]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 5 permit:]{lang="EN-US"}

[    if-match acl 3101]{lang="EN-US"}

[    apply next-hop 1.1.1.1]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[Total matched: 0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ip policy-based-route local]{lang="EN-US"}]{#struct_0_x6230_x1908_1590127703}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1887889560}[[字段]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1847407320}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1928061599}

[[Policy based routing information for local]{lang="EN-US"}]{#struct_0_x6230_x1908_x1473023940}

[[本地策略路由的配置信息和统计信息]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1873534900}

[[Policy name]{lang="EN-US"}]{#struct_0_x6230_x1908_x627612989}

[[策略名]{style="font-family:宋体"}]{#struct_0_x6230_x1908_683403991}

[[node 0 deny/node 2 permit]{lang="EN-US"}]{#struct_0_x6230_x1908_x55171116}

[[节点的匹配模式为允许]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x295272942}[（]{style="font-family:宋体"}[permit]{lang="PT-BR"}[）]{style="font-family:宋体"}[/]{lang="EN-US"}[拒绝]{style="font-family:宋体"}[（]{style="font-family:宋体"}[deny]{lang="PT-BR"}[）]{style="font-family:宋体"}

[[if-match acl]{lang="EN-US"}]{#struct_0_x6230_x1908_x547472311}

[[满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472565188}[的报文被匹配]{style="font-family:宋体"}

[[apply next-hop]{lang="EN-US"}]{#struct_0_x6230_x1908_x699620115}

[[为匹配的报文指定下一跳]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1559681433}

[[Matched: 0]{lang="EN-US"}]{#struct_0_x6230_x1908_954979773}

[[节点匹配成功的次数]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1371937426}

[[Total matched]{lang="EN-US"}]{#struct_0_x6230_x1908_327056101}

[[策略所有节点匹配成功的次数]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1472630724}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x6230_x1908_x1540349662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip policy-based-route statistics]{lang="EN-US"}**]{#struct_0_x6230_x1908_x922699118}

::: {#1762051539 .myid}
[]{#_Toc404788723}[]{#struct_0_x6230_x1908_873274124}

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route setup**

------------------------------------------------------------------------

[**[display ip policy-based-route setup]{lang="EN-US"}**]{#struct_0_x6230_x1908_2042608129}[命令用来显示已经应用的策略路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1851972717}

[**[display ip policy-based-route setup]{lang="EN-US"}**]{#struct_0_x6230_x1908_1879653045}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1024371036}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1472696260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1603925207}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x2062386053}

[[network-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_x1504059959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_367063991}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6230_x1908_1505825620}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x2105251350}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_2064115135}[显示已经应用的策略路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip policy-based-route setup]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472761796}

[Policy Name              Interface Name]{lang="EN-US"}

[pr01                     GigabitEthernet 1/0/1]{lang="PT-BR"}

[[表1-5 ]{lang="EN-US"}[display ip policy-based-route setup]{lang="EN-US"}]{#struct_0_x6230_x1908_1545017049}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1895719177}[[字段]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1051198254}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1032278320}

[[policy Name]{lang="EN-US"}]{#struct_0_x6230_x1908_x824779617}

[[策略名]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x629138705}

[[Interface Name]{lang="EN-US"}]{#struct_0_x6230_x1908_x1432705620}

[[应用策略的接口]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1897809065}

[]{#_Hlt22459870}[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1472303044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_167707236}

::: {#1453609489 .myid}
[]{#_Toc404788724}[]{#struct_0_x6230_x1908_x475521470}[]{#_Toc136937993}[]{#_Toc99445942}[]{#_Toc34203775}[]{#_Toc33197999}

**策略路由 \-- 策略路由配置命令 \-- if-match acl**

------------------------------------------------------------------------

[**[if-match acl]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1022915128}[命令用来设置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配规则。]{style="font-family:宋体"}

[**[undo if-match acl]{lang="EN-US"}**]{#struct_0_x6230_x1908_x986091133}[命令用来删除]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x405227358}

[**[if-match acl]{lang="EN-US"}**[ { *acl-number \|* **name** *acl-name* }]{lang="EN-US"}]{#struct_0_x6230_x1908_x1874768244}

[**[undo if-match acl]{lang="EN-US"}**]{#struct_0_x6230_x1908_1096802522}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1761504881}

[[未设置]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x6230_x1908_x1472368580}[匹配规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1510473745}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1865000651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1569543119}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_1858973944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_2062272029}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_23736381}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_x2144894957}[：访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x6230_x1908_1973069825}[，]{lang="EN-US" style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[取值范围为]{lang="EN-US" style="font-family:宋体"}[2000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x6230_x1908_93256612}[，]{lang="EN-US" style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[取值范围为]{lang="EN-US" style="font-family:宋体"}[3000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1104963164}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1853983119}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x177551846}[设置满足]{style="font-family:宋体"}[ACL 2011]{lang="EN-US"}[的报文被匹配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_74419657}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] if-match acl 2011]{lang="EN-US"}

[]{#_Toc136937996}[]{#_Toc99445945}[]{#_Toc34203778}[]{#_Toc33198002}[]{#struct_0_x6230_x1908_1240192395}[]{#_Toc302486750}[]{#_Toc302486751}[\# ]{lang="EN-US"}[设置满足]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[名称]{style="font-family:宋体"}[为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的报文被匹配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x478324102}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] if-match acl name aaa]{lang="EN-US"}
:::

::::: {#-27633683 .myid}
[]{#_Toc404788725}[]{#struct_0_x6230_x1908_93191076}[]{#_Toc332358578}[]{#_Toc328555077}[]{#_Toc322610597}[]{#_Toc319479804}

**策略路由 \-- 策略路由配置命令 \-- if-match packet-length**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_582380268}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_x2027222366}
:::

[ ]{lang="EN-US"}

[**[if-match packet-length]{lang="EN-US"}**]{#struct_0_x6230_x1908_1114667001}[命令用来设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文长度匹配规则。]{style="font-family:宋体"}

[**[undo if-match packet-length]{lang="EN-US"}**]{#struct_0_x6230_x1908_x486049410}[命令用来删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文长度匹配规则的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1377637320}

[**[if-match packet-length]{lang="EN-US"}**[ *min-len max-len*]{lang="EN-US"}]{#struct_0_x6230_x1908_x825787446}

[**[undo if-match packet-length]{lang="EN-US"}**]{#struct_0_x6230_x1908_x959542052}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1495468345}

[[未设置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6230_x1908_93125540}[报文长度匹配规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1356019527}

[[策略节点视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x173508154}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1941086835}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x171800670}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_103416576}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1337864713}

[*[min-len]{lang="EN-US"}*]{#struct_0_x6230_x1908_618148213}[：最短]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[*[max-len]{lang="EN-US"}*]{#struct_0_x6230_x1908_x938905546}[：最长]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}*[max-len]{lang="EN-US"}*[应该不小于]{style="font-family:宋体"}*[min-len]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x6230_x1908_93060004}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[长度匹配含边界值，如指定]{style="font-family:宋体"}*[min-len]{lang="EN-US"}*]{#struct_0_x6230_x1908_609424661}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}*[max-len]{lang="EN-US"}*[为]{style="font-family:宋体"}[200]{lang="EN-US"}[，则报文长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[与]{style="font-family:宋体"}[200]{lang="EN-US"}[的报文都是匹配报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1086661661}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x1914967099}[设置报文长度在]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[字节之间的报文被匹配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x71386145}

[\[Sysname\] policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr-aa-11\] if-match packet-length 100 200]{lang="EN-US"}
:::::

::: {#2130398225 .myid}
[]{#_Toc404788726}[]{#struct_0_x6230_x1908_x808034686}[]{#_Toc332358579}[]{#_Toc328555091}[]{#_Toc322610593}

**策略路由 \-- 策略路由配置命令 \-- ip local policy-based-route**

------------------------------------------------------------------------

[**[ip local policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1762802974}[命令用来对本地报文应用策略。]{style="font-family:宋体"}

[**[undo ip local policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1621461804}[命令用来删除对本地报文应用策略的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x998668648}

[**[ip local policy-based-route]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_x6230_x1908_93518756}

[**[undo ip local policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x577056963}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x609895110}

[[对本地报文没有应用策略。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x384616211}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1329123743}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_96096671}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1516997916}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1642902590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1823159794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_93453220}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1366602802}[：策略名，唯一标识一个策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[，区分大小写。该策略必须已经存在]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x961670145}

[[对本地报文只能应用一个策略。应用新的策略前必须删除本地原来已经应用的策略。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_1633034634}

[[对本地报文应用的策略将对本地产生的所有报文进行匹配。若无特殊需求，建议用户不要配置本地策略路由。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x840940879}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_2143818158}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_2037570346}[对本地报文应用策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x672855871}

[\[Sysname\] ip local policy-based-route aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_2120114386}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip policy-based-route setup]{lang="EN-US"}**]{#struct_0_x6230_x1908_93387684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_1056156445}
:::

::: {#1884113505 .myid}
[]{#_Toc404788727}[]{#struct_0_x6230_x1908_x1736873644}

**策略路由 \-- 策略路由配置命令 \-- ip policy-based-route**

------------------------------------------------------------------------

[**[ip policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_1298293063}[命令用来对接口转发的报文应用策略。]{style="font-family:宋体"}

[**[undo ip policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_660339488}[命令用来删除对接口转发的报文应用的策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_856086581}

[**[ip policy-based-route]{lang="EN-US"}***[ policy-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_1647293794}

[**[undo ip policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1888039051}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_101540767}

[[对接口转发的报文没有应用策略。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_93322148}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_770782172}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x360349692}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x510529361}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x148700480}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x683142791}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x478192857}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_x594220241}[：策略名，唯一标识一个策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。该策略必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1319885442}

[[对接口转发的报文应用策略时，一个接口只能应用一个策略。应用新的策略前必须删除接口上原来已经应用的策略。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_93780900}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_899229234}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6230_x1908_1147701566}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x106842090}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[转发的报文应用策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1123350345}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip policy-based-route aaa]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6230_x1908_1968194386}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_301344273}[对接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[转发的报文应用策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_x1320610834}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-Vlan2\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ip policy-based-route aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_93715364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip policy-based-route setup]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1289035311}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x843489031}
:::

::: {#1260168437 .myid}
[]{#_Toc404788728}[]{#struct_0_x6230_x1908_x755488062}[]{#_Toc136937997}

**策略路由 \-- 策略路由配置命令 \-- policy-based-route**

------------------------------------------------------------------------

[**[policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_1249089382}[命令用来创建策略节点，并进入策略节点视图。如果指定的策略节点已创建，则该命令直接用来进入该策略节点的视图。]{style="font-family:宋体"}

[**[undo policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_2044222785}[命令用来删除已创建的策略或策略节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_979520997}

[**[policy-based-route]{lang="EN-US"}**[ *policy-name* \[ **deny** \| **permit** \] **node** *node-number*]{lang="EN-US"}]{#struct_0_x6230_x1908_1333026054}

[**[undo policy-based-route]{lang="EN-US"}**[ *policy-name* \[ **deny** \| **node** *node-number* \| **permit** \]]{lang="EN-US"}]{#struct_0_x6230_x1908_8072168}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_93256613}

[[没有创建策略节点。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_851351972}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1275743911}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x59463358}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1731278691}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_1229134195}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_847733070}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_2017414897}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_1903741837}[：策略名，唯一标识一个策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x6230_x1908_93191077}[：指定策略节点的匹配模式为拒绝模式。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x6230_x1908_x1756271892}[：指定策略节点的匹配模式为允许模式。缺省匹配模式为]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[node]{lang="EN-US"}***[ node-number]{lang="EN-US"}*]{#struct_0_x6230_x1908_538712646}[：]{style="font-family:宋体"}[策略节点编号。节点编号越小优先级越高，先对优先级高的节点进行匹配操作。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x660713601}

[[删除策略之前，必须先取消该策略在所有接口或者本地上的应用，否则删除失败。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_922058551}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x6230_x1908_986313621}[命令时，如果指定了策略节点，将删除指定的节点；如果指定了节点模式，将按模式删除策略内所有与该模式匹配的所有节点；如果两者都没有指定，将删除整个策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1033097896}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x2075111125}[配置一个策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[，并进入策略节点视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_93125541}

[\[Sysname\] policy-based-route policy1 permit node 10]{lang="EN-US"}

[\[Sysname-pbr-policy1-10\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_982632633}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_2028038360}
:::

::: {#-2056810072 .myid}
[]{#_Toc404788729}[]{#struct_0_x6230_x1908_x1415132099}

**策略路由 \-- 策略路由配置命令 \-- reset ip policy-based-route statistics**

------------------------------------------------------------------------

[**[reset ip policy-based-route statistics]{lang="EN-US"}**]{#struct_0_x6230_x1908_x938169752}[命令用来清除策略路由的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_978063946}

[**[reset ip policy-based-route ]{lang="EN-US"}[statistics]{lang="EN-US"}**[ \[ **policy** *policy-name* \]]{lang="EN-US"}]{#struct_0_x6230_x1908_x1325833068}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1153712040}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x133284994}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x597487748}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_93060005}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_x1346890475}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_551996864}

[**[policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_x6230_x1908_x1862559763}[：清除指定策略的统计信息。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[表示策略名，唯一标识一个策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_2097848611}

[[系统按照策略名清除策略路由的统计信息。如果不指定策略名，将清除所有配置策略的匹配统计信息（该统计信息可以通过]{style="font-family:宋体"}**[display ip policy-based-route interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_x906844595}[命令查看）；如果指定策略名，将清除指定策略的匹配统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1670759513}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x2021254351}[清除所有配置策略的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ip policy-based-route statistics]{lang="EN-US"}]{#struct_0_x6230_x1908_1050894673}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_93518757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip policy-based-route interface]{lang="EN-US"}**]{#struct_0_x6230_x1908_1379258173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip policy-based-route local]{lang="EN-US"}**]{#struct_0_x6230_x1908_x948334478}
:::

::::: {#-2067229804 .myid}
[]{#_Toc404788730}[]{#struct_0_x6230_x1908_1788558984}[]{#_Toc328555092}[]{#_Toc332358583}

**策略路由 \-- 策略路由配置命令 \-- snmp-agent trap enable policy-based-route**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](策略路由命令.files/image002.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_x6230_x1908_1975833086}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6230_x1908_x42817374}
:::

[ ]{lang="EN-US"}

[**[snmp-agent trap enable policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_1079860898}[命令用来开启下一跳失效告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_x681102330}[命令用来关闭下一跳]{style="font-family:宋体"}[失效告警功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x754558159}

[**[snmp-agent trap enable policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_93453221}

[**[undo snmp-agent trap enable policy-based-route]{lang="EN-US"}**]{#struct_0_x6230_x1908_589712334}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_x1218319947}

[[下一跳失效告警功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x6230_x1908_533925068}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1930101857}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6230_x1908_798793830}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_809875965}

[[network-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_472406203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6230_x1908_216467475}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_93387685}

[[开启策略路由模块的告警功能后，]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x900158691}[当下一跳的状态由有效变为无效时，]{style="font-family:宋体"}[该模块会生成包含下一跳地址的告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}]{#struct_0_x6230_x1908_x1055156816}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6230_x1908_1146047220}

[[\# ]{lang="EN-US"}]{#struct_0_x6230_x1908_x902365999}[启用告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6230_x1908_1573074961}

[\[Sysname\] snmp-agent trap enable policy-based-route]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
