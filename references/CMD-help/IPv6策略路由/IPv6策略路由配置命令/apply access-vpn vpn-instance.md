::::: {#-614357393 .myid}
[]{#_Toc263858606}[]{#_Toc257723482}[]{#_Toc72327933}[]{#_Toc404789094}[]{#struct_0_80557_12584_2004499650}[]{#_Toc345339101}[]{#_Toc332358586}[]{#_Toc328557127}[]{#_Toc322610599}[]{#_Toc319479806}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply access-vpn vpn-instance**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_x1107946219}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_x2007263486}
:::

[ ]{lang="EN-US"}

[**[apply access-vpn vpn-instance]{lang="EN-US"}**]{#struct_0_80557_12584_347992838}[命令用来设置报文在指定]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[实例中进行转发。]{style="font-family:宋体"}

[**[undo apply access-vpn vpn-instance]{lang="EN-US"}**]{#struct_0_80557_12584_x508524914}[命令用来取消报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中进行转发的设置或者删除一个或多个指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例对应的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x2031041619}

[**[apply access-vpn vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_814326915}

[**[undo apply access-vpn vpn-instance]{lang="EN-US"}**[ \[ *vpn-instance-name*&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_80557_12584_470906641}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_1383987227}

[[未设置报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_80557_12584_1905579034}[实例中进行转发。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x150520647}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x1108011755}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_1798012781}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x196382866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_1196965012}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x796150440}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_80557_12584_x65133155}[：表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_x984253017}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_96391084}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_80557_12584_1837738783}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。当满足匹配规则后，将根据第一个可用的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例转发表进行转发。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_80557_12584_x1108077291}[命令时，如果指定了]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名，将删除该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例对应的配置；如果未指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名，将取消报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内转发的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_348873172}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x1549999188}[在策略节点中设置报文在名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[、]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中进行转发（]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[、]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[已存在）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_447231253}

[\[Sysname\]ipv6 policy-based-route policy1 permit node 10]{lang="EN-US"}

[\[Sysname-pbr6-policy1-10\] apply access-vpn vpn-instance vpn1 vpn2]{lang="EN-US"}
:::::

::::: {#317473173 .myid}
[]{#_Toc404789095}[]{#struct_0_80557_12584_x1665332968}[]{#_Toc345339102}[]{#_Toc332358587}[]{#_Toc328557136}[]{#_Toc322610607}[]{#_Toc319479815}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply continue**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_x1586570989}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_x1300372477}
:::

[ ]{lang="EN-US"}

[**[apply continue]{lang="EN-US"}**]{#struct_0_80557_12584_x1379244550}[命令用来设置匹配成功的当前节点指定转发路径失败后，继续进行后续节点的处理。]{style="font-family:宋体"}

[**[undo apply continue]{lang="EN-US"}**]{#struct_0_80557_12584_x1108142827}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1006295689}

[**[apply continue]{lang="EN-US"}**]{#struct_0_80557_12584_x318448339}

[**[undo apply continue]{lang="EN-US"}**]{#struct_0_80557_12584_x166824074}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_1530786865}

[[匹配成功的当前节点指定转发路径失败后，不再进行下一节点的匹配。]{style="font-family:宋体"}]{#struct_0_80557_12584_1559964541}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_763122049}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_68483931}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x485572970}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1108208363}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1953484008}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1958871280}

[[本命令仅在策略节点的匹配模式为]{style="font-family:宋体"}**[permit]{lang="EN-US"}**]{#struct_0_80557_12584_1390930130}[时生效。]{style="font-family:宋体"}

[[在配置了该命令后，如果当前节点中没有配置影响报文转发路径的五个]{style="font-family:宋体"}**[apply]{lang="EN-US"}**]{#struct_0_80557_12584_993220485}[子句（]{style="font-family:宋体"}**[apply access-vpn vpn-instance]{lang="EN-US"}**[、]{style="font-family:
宋体"}**[apply next-hop]{lang="EN-US"}**[、]{style="font-family:宋体"}**[apply output-interface]{lang="EN-US"}**[、]{style="font-family:宋体"}**[apply default-next-hop]{lang="EN-US"}**[和]{style="font-family:宋体"}**[apply default-output-interface]{lang="EN-US"}**[），或者配置了这五个子句中的一个或多个，但配置的子句都失效（下一跳不可达、出接口]{style="font-family:宋体"}[down]{lang="EN-US"}[或者报文在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内转发失败）时，会进行下一节点的处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_1472815228}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x129658414}[设置匹配成功的当前节点转发失败后继续进行后续节点的处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_724149873}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply continue]{lang="EN-US"}
:::::

::::: {#136921610 .myid}
[]{#_Toc404789096}[]{#struct_0_80557_12584_x1108273899}[]{#_Toc345339103}[]{#_Toc332358588}[]{#_Toc328557132}[]{#_Toc322610603}[]{#_Toc319479811}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply default-next-hop**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_173868722}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_1274722053}
:::

[ ]{lang="EN-US"}

[**[apply default-next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_1471290849}[命令用来设置指导报文转发的缺省下一跳。]{style="font-family:宋体"}

[**[undo apply default-next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_x1138018995}[命令用来取消指导报文转发的缺省下一跳的设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x943489161}

[**[apply default-next-hop ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name* *\|* **inbound-vpn** \] { *ipv6-address* \[ **direct** \] \[ **track** *track-entry-number* \] }&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_991177415}

[**[undo apply default-next-hop ]{lang="EN-US"}**[\[ \[ **vpn-instance** *vpn-instance-name \|* **inbound-vpn** \] *ipv6-address*&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_80557_12584_1811805501}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1468702226}

[[未设置指导报文转发的缺省下一跳。]{style="font-family:宋体"}]{#struct_0_80557_12584_x1108339435}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x789834674}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_1194072024}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1830195335}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_766599146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1320767541}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1940711008}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_80557_12584_x351055521}[：缺省下一跳所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[**[inbound-vpn]{lang="EN-US"}**]{#struct_0_80557_12584_1059695264}[：报文入接口所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_80557_12584_x1108404971}[：缺省下一跳的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。不指定]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[或]{style="font-family:宋体"}**[inbound-vpn]{lang="EN-US"}**[参数，表示指定的是公网下一跳。]{style="font-family:宋体"}

[**[direct]{lang="EN-US"}**]{#struct_0_80557_12584_x1339417516}[：指定当前缺省下一跳生效的条件为直连下一跳。]{style="font-family:宋体"}

[**[track]{lang="EN-US"}**[ *track-entry-number*]{lang="EN-US"}]{#struct_0_80557_12584_x1317332631}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_x1214484443}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1204711596}

[[用户可以同时配置多个缺省下一跳（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_80557_12584_650221481}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_80557_12584_18012301}[个缺省下一跳。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_80557_12584_1807553583}[命令时，如果指定了缺省下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，将取消已配置的该缺省下一跳；如果没有指定缺省下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，将取消已配置的所有缺省下一跳。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1986892}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x1107421931}[设置指导报文转发的缺省直连下一跳为]{style="font-family:宋体"}[1:1::1:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x1726280705}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply default-next-hop 1:1::1:1 direct]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x696568342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_80557_12584_1770488113}
:::::

::::: {#-1403479646 .myid}
[]{#_Toc404789097}[]{#struct_0_80557_12584_1273466795}[]{#_Toc345339132}[]{#_Toc332358590}[]{#_Toc328557134}[]{#_Toc322610605}[]{#_Toc319479813}[]{#_Toc345339104}[]{#_Toc345339105}[]{#_Toc345339106}[]{#_Toc345339107}[]{#_Toc345339108}[]{#_Toc345339109}[]{#_Toc345339110}[]{#_Toc345339111}[]{#_Toc345339112}[]{#_Toc345339113}[]{#_Toc345339114}[]{#_Toc345339115}[]{#_Toc345339116}[]{#_Toc345339117}[]{#_Toc345339118}[]{#_Toc345339119}[]{#_Toc345339120}[]{#_Toc345339121}[]{#_Toc345339122}[]{#_Toc345339123}[]{#_Toc345339124}[]{#_Toc345339125}[]{#_Toc345339126}[]{#_Toc345339127}[]{#_Toc345339128}[]{#_Toc345339129}[]{#_Toc345339130}[]{#_Toc345339131}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply default-output-interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_x1946947540}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_443789991}
:::

[ ]{lang="EN-US"}

[**[apply default-output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_x1422184722}[命令用来设置指导报文转发的缺省出接口。]{style="font-family:
宋体"}

[**[undo apply default-output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_x1107487467}[命令用来取消指导报文转发的缺省出接口的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1528324066}

[**[apply default-output-interface ]{lang="EN-US"}**[{ ]{lang="EN-US"}*[interface-type interface-number ]{lang="EN-US"}*[\[ **track** *track-entry-number* \] }&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_x1497272118}

[**[undo apply default-output-interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}[{ *interface-type interface-number* }&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_80557_12584_918642644}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_236027336}

[[未设置指导报文转发的缺省出接口。]{style="font-family:宋体"}]{#struct_0_80557_12584_x192895788}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_605652098}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_1799030463}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x210085710}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1107946218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_x441179545}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x627168710}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_80557_12584_1509860779}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[**[track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_80557_12584_x1563745560}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_1599936749}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x851820353}

[[用户可以同时配置多个缺省出接口（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_80557_12584_x487263480}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_80557_12584_x178597979}[个缺省出接口。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[指定缺省出接口类型需配置为]{style="font-family:宋体"}[P2P]{lang="EN-US"}]{#struct_0_80557_12584_x1108011754}[（]{style="font-family:宋体"}[Point-to-Point]{lang="EN-US"}[，点到点）]{style="font-family:宋体"}[接口，对于非]{style="font-family:宋体"}[P2P]{lang="EN-US"}[接口（广播类型的接口和]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型的接口），比如以太网接口、]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口，由于有多个可能的下一跳，可能会造成报文转发不成功的现象。]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[（]{style="font-family:宋体"}[Non Broadcast MultiAccess]{lang="EN-US"}[，非广播多路访问）指全连通、非广播、多点可达的网络，这种网络采用单播方式发送报文。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_80557_12584_231928840}[命令时，如果指定了接口，将取消已配置的该缺省出接口；如果没有指定接口，将取消已配置的所有缺省出接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x2132435654}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1009682369}[设置报文的缺省出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x1495975316}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply default-output-interface ]{lang="EN-US"}[gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_308728194}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_80557_12584_1200284485}
:::::

::::: {#362027212 .myid}
[]{#_Toc404789098}[]{#struct_0_80557_12584_855635600}[]{#_Toc345339160}[]{#_Toc342567228}[]{#_Toc345339133}[]{#_Toc345339134}[]{#_Toc345339135}[]{#_Toc345339136}[]{#_Toc345339137}[]{#_Toc345339138}[]{#_Toc345339139}[]{#_Toc345339140}[]{#_Toc345339141}[]{#_Toc345339142}[]{#_Toc345339143}[]{#_Toc345339144}[]{#_Toc345339145}[]{#_Toc345339146}[]{#_Toc345339147}[]{#_Toc345339148}[]{#_Toc345339149}[]{#_Toc345339150}[]{#_Toc345339151}[]{#_Toc345339152}[]{#_Toc345339153}[]{#_Toc345339154}[]{#_Toc345339155}[]{#_Toc345339156}[]{#_Toc345339157}[]{#_Toc345339158}[]{#_Toc345339159}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply loadshare**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_x1108077290}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_x1217210769}
:::

**[ ]{lang="EN-US"}**

[**[apply loadshare]{lang="EN-US"}**]{#struct_0_80557_12584_x214782999}[命令用来设置多个下一跳]{style="font-family:宋体"}[(]{lang="EN-US"}[出接口、缺省下一跳和缺省出接口]{style="font-family:宋体"}[)]{lang="EN-US"}[工作在负载分担模式。]{style="font-family:宋体"}

[**[undo apply loadshare]{lang="EN-US"}**]{#struct_0_80557_12584_780986771}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x998676164}

[**[apply loadshare]{lang="EN-US"}**[ { **default-next-hop** \| **default-output-interface** \| **next-hop \| output-interface** }]{lang="EN-US"}]{#struct_0_80557_12584_x89124961}

[**[undo apply loadshare]{lang="EN-US"}**[ { **default-next-hop** \| **default-output-interface** \| **next-hop \| output-interface** }]{lang="EN-US"}]{#struct_0_80557_12584_1119226895}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_1135472276}

[[多个下一跳]{style="font-family:宋体"}[(]{lang="EN-US"}]{#struct_0_80557_12584_x1174929974}[出接口、缺省下一跳和缺省出接口]{style="font-family:宋体"}[)]{lang="EN-US"}[工作在主备模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_267991406}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x1108142826}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_559788252}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_118250764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_1278006428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x401542997}

[**[default-]{lang="EN-US"}[next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_x774043626}[：设置指导报文转发的多个缺省下一跳工作在负载分担模式。]{style="font-family:宋体"}

[**[default-output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_x1382910409}[：设置指导报文转发的多个缺省出接口工作在负载分担模式。]{style="font-family:宋体"}

[**[next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_x1429732288}[：设置指导报文转发的多个下一跳工作在负载分担模式。]{style="font-family:宋体"}

[**[output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_769078863}[：设置指导报文转发的多个出接口工作在负载分担模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1108208362}

[[多个出接口]{style="font-family:宋体"}[(]{lang="EN-US"}]{#struct_0_80557_12584_x387400067}[下一跳、缺省下一跳和缺省出接口]{style="font-family:宋体"}[)]{lang="EN-US"}[的工作模式有两种：主备模式、负载分担模式。以多个出接口为例：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主备模式：按照配置顺序，以第一个配置的出接口作为主用出接口，指导报文转发。当主用出接口失效时，按配置顺序选择后续的第一个有效的出接口指导报文转发。]{style="font-family:宋体"}]{#struct_0_80557_12584_x1050917648}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[负载分担模式：按照配置顺序，逐包轮流选择有效的出接口指导报文转发。下一跳的负载分担模式则有些不同，会按照下一跳的权重指导报文转发。缺省情况下，多个下一跳会按照缺省的权重值平均分配带宽，多个下一跳的转发流量的比例是相同的。]{style="font-family:宋体"}]{#struct_0_80557_12584_1021044187}

[[缺省下一跳和缺省出接口的情况请参考多个出接口。]{style="font-family:宋体"}]{#struct_0_80557_12584_x422157972}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_1536658485}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1907669432}[设置多个下一跳工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x651150056}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply next-hop 1::1 2::2]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply loadshare next-hop]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x1108273898}[设置多个出接口工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x1392215219}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply output-interface Vlan-interface 1 Vlan-interface 2]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply loadshare output-interface]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x629799870}[设置多个缺省下一跳工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_1231690478}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply default-next-hop 1::1 2::2]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply loadshare default-next-hop]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_333976786}[设置多个缺省出接口工作在负载分担模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x52056339}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply default-output-interface Vlan-interface 1 Vlan-interface 2]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply loadshare default-output-interface]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_80557_12584_x1108339434}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply default-next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_1939048681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[a]{lang="EN-US"}[pply default-output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_x1380271637}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_1522820604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_x1432997161}
:::::

::::: {#-1850744860 .myid}
[]{#_Toc404789099}[]{#struct_0_80557_12584_1240861482}[]{#_Toc345339162}[]{#_Toc345339161}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply next-hop**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_706918257}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_x1167973540}
:::

**[ ]{lang="EN-US"}**

[**[apply next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_1158040228}[命令用来设置报文转发的下一跳。]{style="font-family:宋体"}

[**[undo apply next-hop]{lang="EN-US"}**]{#struct_0_80557_12584_x1108404970}[命令用来取消报文转发下一跳的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_226666425}

[**[apply next-hop]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \| **inbound-vpn** \] { *ipv6-address* \[ **direct** \] \[ **track** *track-entry-number* \] \[ **weight** *weight-value* \] } &\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_1968642558}

[**[undo apply next-hop]{lang="EN-US"}**[ \[ \[ **vpn-instance** *vpn-instance-name* \| **inbound-vpn** \] *ipv6-address*&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_80557_12584_x1270596421}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_678004628}

[[未设置报文转发的下一跳。]{style="font-family:宋体"}]{#struct_0_80557_12584_2139439914}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x731891364}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_243166841}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_567455157}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1107421930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_x160196764}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1240540067}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_80557_12584_x1630732012}[：下一跳所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[**[inbound-vpn]{lang="EN-US"}**]{#struct_0_80557_12584_x691527860}[：报文入接口所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_80557_12584_577411750}[：下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。不指定]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[或]{style="font-family:宋体"}**[inbound-vpn]{lang="EN-US"}**[参数，表示指定的是公网下一跳。]{style="font-family:宋体"}

[**[direct]{lang="EN-US"}**]{#struct_0_80557_12584_x628331798}[：指定当前下一跳生效的条件为直连下一跳。]{style="font-family:宋体"}

[**[track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_80557_12584_x227248728}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_1774232972}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight ]{lang="EN-US"}***[weight-value]{lang="EN-US"}*]{#struct_0_80557_12584_680206072}[：指定]{style="font-family:宋体"}[下一跳负载分担的权重。设备根据权重确定该下一跳转发流量的比例。例如，三个下一跳配置的负载分担权重分别为]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[2]{lang="EN-US"}[，则它们的负载分担的比例分别为]{style="font-family:
宋体"}[1/4]{lang="EN-US"}[、]{style="font-family:
宋体"}[1/4]{lang="EN-US"}[和]{style="font-family:宋体"}[1/2]{lang="EN-US"}[。]{style="font-family:宋体"}*[weight-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_1770659457}

[[用户可以同时配置多个下一跳（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_80557_12584_x1107487466}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_80557_12584_37759875}[个下一跳。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_80557_12584_x4625400}[命令时，如果指定了下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，将取消已配置的该下一跳；如果没有指定下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，将取消已配置的所有下一跳。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1535491448}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x486263660}[设置报文转发的下一跳为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_949079975}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply next-hop 1::1]{lang="EN-US"}

[]{#_Toc263858610}[]{#_Toc257723486}[]{#_Toc72327936}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_1115512038}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_80557_12584_698620747}
:::::

::::: {#1859300671 .myid}
[]{#_Toc404789100}[]{#struct_0_80557_12584_x1107946221}[]{#_Toc345339191}[]{#_Toc332358594}[]{#_Toc328557130}[]{#_Toc322610601}[]{#_Toc319479809}[]{#_Toc345339163}[]{#_Toc345339164}[]{#_Toc345339165}[]{#_Toc345339166}[]{#_Toc345339167}[]{#_Toc345339168}[]{#_Toc345339169}[]{#_Toc345339170}[]{#_Toc345339171}[]{#_Toc345339172}[]{#_Toc345339173}[]{#_Toc345339174}[]{#_Toc345339175}[]{#_Toc345339176}[]{#_Toc345339177}[]{#_Toc345339178}[]{#_Toc345339179}[]{#_Toc345339180}[]{#_Toc345339181}[]{#_Toc345339182}[]{#_Toc345339183}[]{#_Toc345339184}[]{#_Toc345339185}[]{#_Toc345339186}[]{#_Toc345339187}[]{#_Toc345339188}[]{#_Toc345339189}[]{#_Toc345339190}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply output-interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_x1650836518}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_2013124672}
:::

[ ]{lang="EN-US"}

[**[apply output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_219073192}[命令用来设置指导报文转发的出接口。]{style="font-family:宋体"}

[**[undo apply output-interface]{lang="EN-US"}**]{#struct_0_80557_12584_1182390132}[命令用来取消指导报文转发的出接口的设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_86931352}

[**[apply output-interface ]{lang="EN-US"}**[{ *interface-type interface-number* \[ **track** *track-entry-number* \] }&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_x1131305079}

[**[undo apply output-interface ]{lang="EN-US"}**[\[ { *interface-type* *interface-number* }&\<1-*n*\> \]]{lang="EN-US"}]{#struct_0_80557_12584_x1564164066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_858464285}

[[未设置指导报文转发的出接口。]{style="font-family:宋体"}]{#struct_0_80557_12584_x1108011757}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1334155101}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x258719711}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_269558506}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x514610655}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_1174459107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x524346608}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_80557_12584_x1559816224}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[**[track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_80557_12584_1772301001}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，]{style="font-family:宋体"}*[track-entry-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[&\<1-*n*\>]{lang="EN-US"}]{#struct_0_80557_12584_x1108077293}[：表示前面的参数最多可以输入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次。]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x813926242}

[[用户可以同时配置多个出接口（通过一次或多次配置本命令实现），起到主备或负载分担的作用。]{style="font-family:宋体"}]{#struct_0_80557_12584_x1212957644}

[[每个节点最多可以配置]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_80557_12584_320661764}[个出接口。]{style="font-family:宋体"}*[m]{lang="EN-US"}*[的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[指定出接口类型需配置为]{style="font-family:宋体"}[P2P]{lang="EN-US"}]{#struct_0_80557_12584_857897343}[接口，对于非]{style="font-family:宋体"}[P2P]{lang="EN-US"}[接口（广播类型的接口和]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型的接口），比如以太网接口、]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口，由于有多个可能的下一跳，可能会造成报文转发不成功的现象。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_80557_12584_x1505377196}[命令时，如果指定了接口，将取消已配置的该出接口；如果没有指定接口，将取消已配置的所有出接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x380855147}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_461802609}[对已经匹配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文指定出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x1108142829}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply output-interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_1769641833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[apply loadshare]{lang="EN-US"}**]{#struct_0_80557_12584_109824035}
:::::

::::: {#908845892 .myid}
[]{#_Toc404789101}[]{#struct_0_80557_12584_x1931257614}[]{#_Toc345339220}[]{#_Toc332358596}[]{#_Toc328557126}[]{#_Toc322610598}[]{#_Toc319479805}[]{#_Toc345339192}[]{#_Toc345339193}[]{#_Toc345339194}[]{#_Toc345339195}[]{#_Toc345339196}[]{#_Toc345339197}[]{#_Toc345339198}[]{#_Toc345339199}[]{#_Toc345339200}[]{#_Toc345339201}[]{#_Toc345339202}[]{#_Toc345339203}[]{#_Toc345339204}[]{#_Toc345339205}[]{#_Toc345339206}[]{#_Toc345339207}[]{#_Toc345339208}[]{#_Toc345339209}[]{#_Toc345339210}[]{#_Toc345339211}[]{#_Toc345339212}[]{#_Toc345339213}[]{#_Toc345339214}[]{#_Toc345339215}[]{#_Toc345339216}[]{#_Toc345339217}[]{#_Toc345339218}[]{#_Toc345339219}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- apply precedence**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image002.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_211899786}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_1890806768}
:::

[ ]{lang="EN-US"}

[**[apply precedence]{lang="EN-US"}**]{#struct_0_80557_12584_1868185825}[命令用来设置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的优先级。]{style="font-family:宋体"}

[**[undo apply precedence]{lang="EN-US"}**]{#struct_0_80557_12584_x1484154190}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_969657037}

[**[apply precedence ]{lang="EN-US"}**[{ *type* \| *value* }]{lang="EN-US"}]{#struct_0_80557_12584_x1108208365}

[**[undo apply precedence]{lang="EN-US"}**]{#struct_0_80557_12584_1178683874}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_1049405785}

[[不对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x1242176119}[报文的优先级进行设置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_892789982}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_1383032802}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_80557_12584_5344828}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1217734555}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1589890271}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1108273901}

[*[type]{lang="EN-US"}*]{#struct_0_80557_12584_x181902887}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的优先级类型。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_80557_12584_x108962783}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的优先级值，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文共有]{style="font-family:宋体"}[8]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:
宋体"}[7]{lang="EN-US"}[）个优先级，每个数值对应一个优先级类型。在输入参数的时候可以输入数值，也可以输入优先级类型。对应关系如]{style="font-family:宋体"}[[**[[错误！未找到引用源。]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}**]{lang="EN-US"}](#_Ref329186298)[所示。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_670894233}[优先级值与优先级类型对应表]{style="font-family:
黑体"}

[]{#table_struct_0_1289514122}[[优先级值]{style="font-family:黑体"}]{#struct_0_80557_12584_999693780}
:::::

[[优先级类型]{style="font-family:黑体"}]{#struct_0_80557_12584_1311632441}

[[0]{lang="EN-US"}]{#struct_0_80557_12584_x748217431}

[[routine]{lang="EN-US"}]{#struct_0_80557_12584_x1877292637}

[[1]{lang="EN-US"}]{#struct_0_80557_12584_x1108339437}

[[priority]{lang="EN-US"}]{#struct_0_80557_12584_x1952634088}

[[2]{lang="EN-US"}]{#struct_0_80557_12584_x1928219066}

[[immediate]{lang="EN-US"}]{#struct_0_80557_12584_x318435735}

[[3]{lang="EN-US"}]{#struct_0_80557_12584_x1710215057}

[[flash]{lang="EN-US"}]{#struct_0_80557_12584_x279353908}

[[4]{lang="EN-US"}]{#struct_0_80557_12584_x1108404973}

[[flash-override]{lang="EN-US"}]{#struct_0_80557_12584_1792750366}

[[5]{lang="EN-US"}]{#struct_0_80557_12584_1355241541}

[[critical]{lang="EN-US"}]{#struct_0_80557_12584_1161736380}

[[6]{lang="EN-US"}]{#struct_0_80557_12584_711855877}

[[internet]{lang="EN-US"}]{#struct_0_80557_12584_x810905637}

[[7]{lang="EN-US"}]{#struct_0_80557_12584_x1107421933}

[[network]{lang="EN-US"}]{#struct_0_80557_12584_x563481291}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_1487115751}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_582532703}[设置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的优先级为]{style="font-family:宋体"}[5]{lang="EN-US"}[（]{style="font-family:宋体"}[critical]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x1742819737}

[\[Sysname\]ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] apply precedence critical]{lang="EN-US"}

::: {#-1446055306 .myid}
[]{#_Toc404789102}[]{#struct_0_80557_12584_358114823}[]{#_Toc345339221}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- display ipv6 policy-based-route**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipv6 policy-based-route**]{lang="EN-US"}]{#struct_0_80557_12584_x1965831691}[命令用来显示已经配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1107487469}

[**[display ipv6 policy-based-route]{lang="EN-US"}**[ \[ **policy** *policy-name* \]]{lang="EN-US"}]{#struct_0_80557_12584_1603843816}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_123907655}

[[任意视图]{style="font-family:宋体"}]{#struct_0_80557_12584_x1752552472}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1569072180}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_990521470}

[[network-operator]{lang="EN-US"}]{#struct_0_80557_12584_x2100227040}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_723490388}

[[mdc-operator]{lang="EN-US"}]{#struct_0_80557_12584_2065395985}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1107946220}

[**[policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}*]{#struct_0_80557_12584_x84752577}[：显示指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[表示策略名，唯一标识一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x2110868639}

[[如果不指定策略名，将显示所有已经配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x1281194495}[策略；如果指定策略名，将显示指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x662909188}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x1136004749}[显示所有已经配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 policy-based-route]{lang="EN-US"}]{#struct_0_80557_12584_x1695825692}

[Policy name: aaa]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 1000::1]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 policy-based-route]{lang="EN-US"}]{#struct_0_80557_12584_x1923431484}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1284569162}[[字段]{style="font-family:黑体"}]{#struct_0_80557_12584_x1108011756}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_80557_12584_1394728254}

[[Policy name]{lang="EN-US"}]{#struct_0_80557_12584_x1542343815}

[[策略名]{style="font-family:宋体"}]{#struct_0_80557_12584_x160152013}

[[node 1 permit]{lang="EN-US"}]{#struct_0_80557_12584_x454358536}

[[节点]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_80557_12584_x384985341}[的匹配模式为允许]{style="font-family:宋体"}

[[if-match acl]{lang="EN-US"}]{#struct_0_80557_12584_595430482}

[[满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_80557_12584_x1108077292}[的报文被匹配]{style="font-family:宋体"}

[[apply next-hop ]{lang="EN-US"}]{#struct_0_80557_12584_1914957113}

[[为匹配的报文指定下一跳]{style="font-family:宋体"}]{#struct_0_80557_12584_x1947109222}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1668334395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 policy-based-route (System view)]{lang="EN-US"}**]{#struct_0_80557_12584_2036610943}

::: {#-1631172849 .myid}
[]{#_Toc404789103}[]{#struct_0_80557_12584_2086996192}[]{#_Toc345339222}[]{#_Toc263858612}[]{#_Toc257723488}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- display ipv6 policy-based-route interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipv6 policy-based-route interface**]{lang="EN-US"}]{#struct_0_80557_12584_1999393493}[命令用来显示接口下]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1108142828}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_80557_12584_x959241522}

[**[display ipv6 policy-based-route interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_80557_12584_1121025354}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_80557_12584_x1802512878}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 policy-based-route interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_80557_12584_x810919692}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_80557_12584_2035745608}[模式：]{style="font-family:宋体"}

[**[display ipv6 policy-based-route interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_80557_12584_x2119843468}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1202117981}

[[任意视图]{style="font-family:宋体"}]{#struct_0_80557_12584_697389044}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1108208364}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1550199481}

[[network-operator]{lang="EN-US"}]{#struct_0_80557_12584_1640265765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_69789256}

[[mdc-operator]{lang="EN-US"}]{#struct_0_80557_12584_x630816195}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_1221589481}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_80557_12584_2116570296}[：用来指定接口的类型和编号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_80557_12584_1723332798}[：显示指定单板上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_80557_12584_x1217651409}[：显示指定成员设备上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_80557_12584_1206154780}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_80557_12584_x1108273900}[：显示指定成员设备上指定单板上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_80557_12584_1620768303}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_80557_12584_x2060539972}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1747986828}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x792446853}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 policy-based-route interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_80557_12584_x1108339436}

[Policy based routing information for interface GigabitEthernet1/0/1(failed):]{lang="EN-US"}

[Policy name: aaa]{lang="EN-US"}

[  node 0 deny:]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 3999]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 2 permit:]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 1000::1]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/2 track 1 (down)]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/3 track 2 (inactive)]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 5 permit:]{lang="EN-US"}

[    if-match acl 3101]{lang="EN-US"}

[    apply next-hop 1000::1]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[Total matched: 0]{lang="EN-US"}

[\<Sysname\> display ipv6 policy-based-route interface gigabitethernet 1/0/1]{lang="EN-US"}

[Policy based routing information for interface GigabitEthernet1/0/1:]{lang="EN-US"}

[Policy name: aaa]{lang="EN-US"}

[  node 0 deny(not support):]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 3999]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 2 permit(no resource):]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 1000::1]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/2 track 1 (down)]{lang="EN-US"}

[    apply output-interface GigabitEthernet1/0/3 track 2 (inactive)]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 5 permit:]{lang="EN-US"}

[    if-match acl 3101]{lang="EN-US"}

[    apply next-hop 1000::1]{lang="EN-US"}

[  Matched: 0 (no statistics resource)]{lang="EN-US"}

[Total matched: 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ipv6 policy-based-route interface]{lang="EN-US"}]{#struct_0_80557_12584_776249267}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1284503914}[[字段]{style="font-family:黑体"}]{#struct_0_80557_12584_x970186094}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_80557_12584_x1108404972}

[[Policy based routing information for interface GigabitEthernet1/0/1(failed)]{lang="EN-US"}]{#struct_0_80557_12584_x936132989}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_80557_12584_x750859458}[下]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发策略路由的配置信息和统计信息（]{style="font-family:宋体"}[failed]{lang="EN-US"}[表示策略下发驱动失败，此时所有节点都下发失败，不再显示节点一级的失败提示）]{style="font-family:宋体"}

[[![说明](IPv6策略路由命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_80557_12584_700064582}

[[显示全局接口（]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_x1327083449}[全局接口只有一维编号]{style="font-family:
  KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[例如]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="PT-BR"}[接口]{style="font-family:KaiTi_GB2312"}[10]{lang="PT-BR"}[）的信息时，]{style="font-family:KaiTi_GB2312"}[必须在命令中指定]{style="font-family:KaiTi_GB2312"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[或]{style="font-family:KaiTi_GB2312"}**[chassis]{lang="PT-BR"}**[ *chassis-number* **slot** *slot-number*]{lang="PT-BR"}[参数]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[才会显示括号中的信息。]{style="font-family:KaiTi_GB2312"}

[[Policy name]{lang="EN-US"}]{#struct_0_80557_12584_754305390}

[[策略名]{style="font-family:宋体"}]{#struct_0_80557_12584_x1107421932}

[[node 0 deny(not support)]{lang="EN-US"}]{#struct_0_80557_12584_1002602650}

[[node 2 permit(no resource)]{lang="EN-US"}]{#struct_0_80557_12584_x1822803347}

[[节点的匹配模式为允许]{style="font-family:宋体"}]{#struct_0_80557_12584_x1779843387}[（]{style="font-family:宋体"}[permit]{lang="PT-BR"}[）]{style="font-family:宋体"}[/]{lang="EN-US"}[拒绝]{style="font-family:宋体"}[（]{style="font-family:宋体"}[deny]{lang="PT-BR"}[）。（]{style="font-family:宋体"}[not support]{lang="PT-BR"}[表示设备]{style="font-family:宋体"}[不支持该节点设置的规则]{style="font-family:宋体"}[；]{style="font-family:宋体"}[no resource]{lang="PT-BR"}[表示设备的]{style="font-family:宋体"}[ACL]{lang="PT-BR"}[等资源不足，为该节点分配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[等资源失败]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[![说明](IPv6策略路由命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_80557_12584_1651009890}

[[显示全局接口（]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_942626118}[全局接口只有一维编号]{style="font-family:
  KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[例如]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="PT-BR"}[接口]{style="font-family:KaiTi_GB2312"}[10]{lang="PT-BR"}[）的信息时，]{style="font-family:KaiTi_GB2312"}[必须在命令中指定]{style="font-family:KaiTi_GB2312"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[或]{style="font-family:KaiTi_GB2312"}**[chassis]{lang="PT-BR"}**[ *chassis-number* **slot** *slot-number*]{lang="PT-BR"}[参数]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[才会显示括号中的信息。]{style="font-family:KaiTi_GB2312"}

[[if-match acl]{lang="EN-US"}]{#struct_0_80557_12584_x1107487468}

[[满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_80557_12584_x1125039539}[的报文被匹配]{style="font-family:宋体"}

[[apply next-hop]{lang="EN-US"}]{#struct_0_80557_12584_1784735264}

[[为匹配的报文指定下一跳]{style="font-family:宋体"}]{#struct_0_80557_12584_x2021868015}

[[apply output-interface GigabitEthernet1/0/2 track 1 (down)]{lang="EN-US"}]{#struct_0_80557_12584_x55220481}

[[为匹配的报文指定出接口。括号中显示接口的状态：]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_80557_12584_1271063770}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[、]{style="font-family:宋体"}[inactive]{lang="EN-US"}[。接口不在位时，显示]{style="font-family:宋体"}[inactive]{lang="EN-US"}[；接口网络层]{style="font-family:宋体"}[down]{lang="EN-US"}[时，显示]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Matched: 0 (no statistics resource)]{lang="EN-US"}]{#struct_0_80557_12584_556378535}

[[节点匹配成功的次数（]{style="font-family:宋体"}[no statistics resource]{lang="EN-US"}]{#struct_0_80557_12584_1477151352}[表示统计资源不足）]{style="font-family:宋体"}

[[![说明](IPv6策略路由命令.files/image001.png){#图片 2 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_80557_12584_65257554}

[[显示全局接口（]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_1242482022}[全局接口只有一维编号]{style="font-family:
  KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[例如]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="PT-BR"}[接口]{style="font-family:KaiTi_GB2312"}[10]{lang="PT-BR"}[）的信息时，]{style="font-family:KaiTi_GB2312"}[必须在命令中指定]{style="font-family:KaiTi_GB2312"}**[slot]{lang="PT-BR"}***[ slot-number]{lang="PT-BR"}*[或]{style="font-family:KaiTi_GB2312"}**[chassis]{lang="PT-BR"}**[ *chassis-number* **slot** *slot-number*]{lang="PT-BR"}[参数]{style="font-family:KaiTi_GB2312"}[，]{style="font-family:KaiTi_GB2312"}[才会显示括号中的信息。]{style="font-family:KaiTi_GB2312"}

[[Total matched]{lang="EN-US"}]{#struct_0_80557_12584_1271129306}

[[策略所有节点匹配成功的次数]{style="font-family:宋体"}]{#struct_0_80557_12584_x189195403}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x339309714}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip]{lang="EN-US"}**]{#struct_0_80557_12584_1510675056}**[v6]{lang="EN-US"}[ policy-based-route statistics]{lang="EN-US"}**

::: {#-1120858041 .myid}
[]{#_Toc263858611}[]{#_Toc257723487}[]{#_Toc72327937}[]{#_Toc404789104}[]{#struct_0_80557_12584_x133274960}[]{#_Toc345339223}[]{#_Toc332358599}[]{#_Toc328557142}[]{#_Toc322610609}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- display ipv6 policy-based-route local**

------------------------------------------------------------------------

[**[display ipv6 policy-based-route local]{lang="EN-US"}**]{#struct_0_80557_12584_x591130753}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_878257564}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_80557_12584_1997461432}

[**[display ipv6 policy-based-route local]{lang="EN-US"}**]{#struct_0_80557_12584_1271194842}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_80557_12584_1329596248}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 policy-based-route local]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \]\]]{lang="EN-US"}]{#struct_0_80557_12584_202590723}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_80557_12584_x1857900168}[模式：]{style="font-family:宋体"}

[**[display ipv6 policy-based-route local ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_80557_12584_934210850}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_732235415}

[[任意视图]{style="font-family:宋体"}]{#struct_0_80557_12584_x896120942}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_1121658270}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_1271260378}

[[network-operator]{lang="EN-US"}]{#struct_0_80557_12584_x1407306422}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_129410388}

[[mdc-operator]{lang="EN-US"}]{#struct_0_80557_12584_x1718617419}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x2074552030}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_80557_12584_1363894741}[：显示指定单板上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_80557_12584_x345496268}[：显示指定成员设备上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_80557_12584_1609439307}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_80557_12584_1023759794}[：显示指定成员设备上指定单板上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_80557_12584_x1951646504}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_80557_12584_x2061064260}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_1342393579}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1923075933}[显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[本地策略路由的配置信息和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 policy-based-route local]{lang="EN-US"}]{#struct_0_80557_12584_1271325914}

[Policy based routing information for local:]{lang="EN-US"}

[Policy name: aaa]{lang="EN-US"}

[  node 0 deny:]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 1 permit:]{lang="EN-US"}

[    if-match acl 3999]{lang="EN-US"}

[  Matched: 0 ]{lang="EN-US"}

[  node 2 permit:]{lang="EN-US"}

[    if-match acl 2000]{lang="EN-US"}

[    apply next-hop 1::1]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[  node 5 permit:]{lang="EN-US"}

[    if-match acl 3101]{lang="EN-US"}

[    apply next-hop 2::2]{lang="EN-US"}

[  Matched: 0]{lang="EN-US"}

[Total matched: 0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ipv6 policy-based-route local]{lang="EN-US"}]{#struct_0_80557_12584_581079804}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1279554858}[[字段]{style="font-family:黑体"}]{#struct_0_80557_12584_1632803228}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_80557_12584_1271391450}

[[Policy based routing information for local]{lang="EN-US"}]{#struct_0_80557_12584_1334886540}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x1712510239}[本地策略路由的配置信息和统计信息]{style="font-family:宋体"}

[[Policy name]{lang="EN-US"}]{#struct_0_80557_12584_1808062462}

[[策略名]{style="font-family:宋体"}]{#struct_0_80557_12584_x586794310}

[[node 0 deny/node 2 permit]{lang="EN-US"}]{#struct_0_80557_12584_x1248061577}

[[节点的匹配模式为允许]{style="font-family:宋体"}]{#struct_0_80557_12584_x62242815}[（]{style="font-family:宋体"}[permit]{lang="PT-BR"}[）]{style="font-family:宋体"}[/]{lang="EN-US"}[拒绝]{style="font-family:宋体"}[（]{style="font-family:宋体"}[deny]{lang="PT-BR"}[）]{style="font-family:宋体"}

[[if-match acl]{lang="EN-US"}]{#struct_0_80557_12584_1271456986}

[[满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_80557_12584_162132013}[的报文被匹配]{style="font-family:宋体"}

[[apply next-hop]{lang="EN-US"}]{#struct_0_80557_12584_1485517823}

[[为匹配的报文指定下一跳]{style="font-family:宋体"}]{#struct_0_80557_12584_1108399262}

[[Matched: 0]{lang="EN-US"}]{#struct_0_80557_12584_x969523842}

[[节点匹配成功的次数]{style="font-family:宋体"}]{#struct_0_80557_12584_x2085781766}

[[Total matched]{lang="EN-US"}]{#struct_0_80557_12584_1271522522}

[[策略所有节点匹配成功的次数]{style="font-family:宋体"}]{#struct_0_80557_12584_x1383522920}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x2053847678}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip]{lang="EN-US"}**]{#struct_0_80557_12584_1403686375}**[v6]{lang="EN-US"}[ policy-based-route statistics]{lang="EN-US"}**

::: {#191385019 .myid}
[]{#_Toc404789105}[]{#struct_0_80557_12584_x1361244969}[]{#_Toc345339224}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- display ipv6 policy-based-route setup**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipv6 policy-based-route setup**]{lang="EN-US"}]{#struct_0_80557_12584_103234118}[命令用来显示已经应用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_341942427}

[**[display ipv6 policy-based-route setup]{lang="EN-US"}**]{#struct_0_80557_12584_1063964564}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_1270539482}

[[任意视图]{style="font-family:宋体"}]{#struct_0_80557_12584_216406777}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x725780593}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1702690431}

[[network-operator]{lang="EN-US"}]{#struct_0_80557_12584_x1092993796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_952586459}

[[mdc-operator]{lang="EN-US"}]{#struct_0_80557_12584_401768444}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x408632496}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x1363736459}[显示已经应用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 policy-based-route setup]{lang="EN-US"}]{#struct_0_80557_12584_1270605018}

[Policy Name              Interface Name]{lang="EN-US"}

[pr01                     GigabitEthernet 1/0/1]{lang="PT-BR"}

[[表1-5 ]{lang="EN-US"}[display ipv6 policy-based-route setup]{lang="EN-US"}]{#struct_0_80557_12584_x635006315}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1276364202}[[字段]{style="font-family:黑体"}]{#struct_0_80557_12584_x1751910279}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_80557_12584_1890006510}

[[policy Name]{lang="EN-US"}]{#struct_0_80557_12584_x2044968478}

[[策略名]{style="font-family:宋体"}]{#struct_0_80557_12584_1305564005}

[[Interface Name]{lang="EN-US"}]{#struct_0_80557_12584_x1543113293}

[[应用策略的接口]{style="font-family:宋体"}]{#struct_0_80557_12584_1271063771}

[]{#_Toc291836208}[]{#_Toc291836210}[]{#_Toc291836211}[]{#_Toc291836212}[]{#_Toc291836213}[]{#_Toc291836214}[]{#_Toc291836215}[]{#_Toc291836216}[]{#_Toc291836217}[]{#_Toc291836218}[]{#_Toc291836219}[]{#_Toc291836220}[]{#_Toc291836221}[]{#_Toc291836222}[]{#_Toc291836223}[]{#_Toc291836224}[]{#_Toc291836225}[]{#_Toc291836226}[]{#_Toc291836227}[]{#_Toc291836228}[]{#_Toc291836229}[]{#_Toc291836230}[]{#_Toc291836231}[]{#_Toc291836232}[]{#_Toc291836233}[]{#_Toc291836234}[]{#_Toc291836239}[]{#_Toc291836241}[]{#_Toc291836242}[]{#_Toc291836243}[]{#_Toc291836244}[]{#_Toc291836269}[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_556312999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 policy-based-route (interface view)]{lang="EN-US"}**]{#struct_0_80557_12584_1964905074}

::: {#1453609489 .myid}
[]{#_Toc404789106}[]{#struct_0_80557_12584_188586415}[]{#_Toc345339225}[]{#_Toc263858613}[]{#_Toc257723489}[]{#_Toc72327939}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- if-match acl**

------------------------------------------------------------------------

[**[if-match acl]{lang="EN-US"}**]{#struct_0_80557_12584_x494057255}[命令用来设置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配规则。]{style="font-family:宋体"}

[**[undo if-match acl]{lang="EN-US"}**]{#struct_0_80557_12584_1620810199}[命令用来删除]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_1081225952}

[**[if-match acl ]{lang="EN-US"}**[{ *acl6-number \|* **name** *acl6-name* }]{lang="EN-US"}]{#struct_0_80557_12584_x319897922}

[**[undo if-match acl]{lang="EN-US"}**]{#struct_0_80557_12584_194332606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_1271129307}

[[未设置]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_80557_12584_x189260939}[匹配规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1124645819}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x2142660891}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1591530731}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x2119279034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_1461781474}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_1046464525}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_80557_12584_457666792}[：访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基本]{lang="EN-US" style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}]{#struct_0_80557_12584_1271194843}[，]{lang="EN-US" style="font-family:宋体"}*[acl]{lang="EN-US"}[6]{lang="EN-US"}[-number]{lang="EN-US"}*[取值范围为]{lang="EN-US" style="font-family:宋体"}[2000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[高级]{lang="EN-US" style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}]{#struct_0_80557_12584_1329661784}[，]{lang="EN-US" style="font-family:宋体"}*[acl]{lang="EN-US"}[6]{lang="EN-US"}[-number]{lang="EN-US"}*[取值范围为]{lang="EN-US" style="font-family:宋体"}[3000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl6-name]{lang="EN-US"}*]{#struct_0_80557_12584_1017620545}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl6-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x761592609}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x455603622}[设置满足]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[的报文被匹配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x1516858120}

[\[Sysname\] ipv6 policy-based-route aa permit node 10]{lang="EN-US"}

[\[Sysname-pbr6-aa-10\] if-match acl 2000]{lang="EN-US"}

[]{#_Toc263858616}[]{#_Toc257723492}[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x1336687692}[设置满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的报文被匹配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_1271260379}

[\[Sysname\] ipv6 policy-based-route aa permit node 10]{lang="EN-US"}

[\[Sysname-pbr6-aa-10\] if-match acl name aaa]{lang="EN-US"}
:::

::::: {#-27633683 .myid}
[]{#struct_0_80557_12584_x1407371958}[]{#_Toc404789107}[]{#_Toc345339226}[]{#_Toc332358602}[]{#_Toc328557125}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- if-match packet-length**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_1941594076}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_1948676290}
:::

[ ]{lang="EN-US"}

[**[if-match packet-length]{lang="EN-US"}**]{#struct_0_80557_12584_1001031673}[命令用来设置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文长度匹配规则。]{style="font-family:宋体"}

[**[undo if-match packet-length]{lang="EN-US"}**]{#struct_0_80557_12584_x1716283254}[命令用来删除]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[报文长度匹配规则的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_591053132}

[**[if-match packet-length]{lang="EN-US"}**[ *min-len max-len*]{lang="EN-US"}]{#struct_0_80557_12584_276922345}

[**[undo if-match packet-length]{lang="EN-US"}**]{#struct_0_80557_12584_x1020418860}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_1271325915}

[[未设置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_581014268}[报文长度匹配规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1061352748}

[[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_311606389}[策略节点视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_218537689}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1552591989}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_917773626}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_99225174}

[*[min-len]{lang="EN-US"}*]{#struct_0_80557_12584_x152260499}[：最短]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[*[max-len]{lang="EN-US"}*]{#struct_0_80557_12584_1271391451}[：最长]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}*[max-len]{lang="EN-US"}*[应该不小于]{style="font-family:宋体"}*[min-len]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_1334952076}

[[长度匹配含边界值，如指定]{style="font-family:宋体"}[min-len]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_80557_12584_1824455981}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[max-len]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[与]{style="font-family:宋体"}[200]{lang="EN-US"}[的报文都是匹配报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_1413600659}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1907623134}[设置报文长度在]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[字节之间的报文被匹配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_559066890}

[\[Sysname\] ipv6 policy-based-route aa permit node 11]{lang="EN-US"}

[\[Sysname-pbr6-aa-11\] if-match packet-length 100 200]{lang="EN-US"}
:::::

::: {#-543920179 .myid}
[]{#_Toc404789108}[]{#struct_0_80557_12584_x1014586474}[]{#_Toc345339227}[]{#_Toc332358603}[]{#_Toc328557138}[]{#_Toc322610608}[]{#_Toc319479816}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- ipv6 local policy-based-route**

------------------------------------------------------------------------

[**[ipv6 local policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_814091267}[命令用来对本地报文应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo ipv6 local policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_1271456987}[命令用来删除对本地报文应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_162197549}

[**[ipv6 local policy-based-route]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_80557_12584_x821373714}

[**[undo ipv6 local policy-based-route]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_80557_12584_1617583817}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_x468474193}

[[对本地报文没有应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_95024055}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_1638358040}

[[系统视图]{style="font-family:宋体"}]{#struct_0_80557_12584_1812249113}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_1480996259}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_1271522523}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1383588456}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x771986655}

[*[policy-name]{lang="EN-US"}*]{#struct_0_80557_12584_x1114259840}[：策略名，唯一标识一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x857020953}

[[对本地报文只能应用一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_1463087520}[策略。应用新的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略前必须删除本地原来已经应用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[对本地报文应用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x301366261}[策略将对本地产生的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进行匹配。若无特殊需求，建议用户不要配置本地策略路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_1435556413}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1118972739}[对本地报文应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_1270539483}

[\[Sysname\] ipv6 local policy-based-route aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_216472313}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_80557_12584_869901566}**[v6]{lang="EN-US"}[ policy-based-route setup]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 poli]{lang="EN-US"}**]{#struct_0_80557_12584_x11612148}**[cy]{lang="EN-US"}[-based-route (System view)]{lang="EN-US"}**
:::

::: {#-762898868 .myid}
[]{#_Toc404789109}[]{#struct_0_80557_12584_x610968201}[]{#_Toc345339228}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- ipv6 policy-based-route (interface view)**

------------------------------------------------------------------------

[**[ipv6 policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_317093849}[命令用来对接口转发的报文应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo ipv6 policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_x1420130673}[命令用来取消对接口转发的报文应用]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_993933231}

[**[ipv6 policy-based-route]{lang="EN-US"}***[ policy-name]{lang="EN-US"}*]{#struct_0_80557_12584_x2135876483}

[**[undo ipv6 policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_1270605019}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_x635071851}

[[对接口转发的报文没有应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_1415277840}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1300530682}

[[接口视图]{style="font-family:宋体"}]{#struct_0_80557_12584_x1464677137}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_357355937}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1039723657}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_x924843113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_1922195372}

[*[policy-name]{lang="EN-US"}*]{#struct_0_80557_12584_1271063768}[：策略名，唯一标识一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_556902824}

[[对接口转发的报文应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_325033451}[策略时，一个接口只能应用一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。应用新的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略前必须删除接口上原来已经应用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x697153085}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_80557_12584_587122632}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_x1573068827}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[转发的报文应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_1997253417}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 policy-based-route aaa]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_80557_12584_524679965}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1271129304}[对接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[转发的报文应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x189064331}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-Vlan2\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 policy-based-route aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_54466163}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_80557_12584_x1485211655}**[v6]{lang="EN-US"}[ policy-based-route setup]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 poli]{lang="EN-US"}**]{#struct_0_80557_12584_506147236}**[cy]{lang="EN-US"}[-based-route (System view)]{lang="EN-US"}**
:::

::: {#-370592797 .myid}
[]{#_Toc404789110}[]{#struct_0_80557_12584_x1415893880}[]{#_Toc345339229}[]{#_Toc263858617}[]{#_Toc257723493}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- ipv6 policy-based-route (System view)**

------------------------------------------------------------------------

[**[ipv6 policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_x1728342245}[命令用来创建]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略节点，并进入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略节点视图。如果指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略节点已创建，则该命令直接用来进入该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略节点的视图。]{style="font-family:宋体"}

[**[undo ipv6 policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_1966601449}[命令用来删除已创建的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[策略或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_1271194840}

[**[ipv6 policy-based-route]{lang="EN-US"}**[ *policy-name* \[ **deny** \| **permit** \] **node** *node-number*]{lang="EN-US"}]{#struct_0_80557_12584_1329727320}

[**[undo ipv6 policy-based-route]{lang="EN-US"}**[ *policy-name* \[ **deny** \| **node** *node-number* \| **permit** \]]{lang="EN-US"}]{#struct_0_80557_12584_610582246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_167386677}

[[没有创建]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_2077028263}[策略节点。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_756057012}

[[系统视图]{style="font-family:宋体"}]{#struct_0_80557_12584_458635712}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_x39403490}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x1968900179}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_1271260376}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1408223926}

[*[policy-name]{lang="EN-US"}*]{#struct_0_80557_12584_x607325966}[：策略名，唯一标识一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_80557_12584_567818273}[：指定节点的匹配模式为拒绝模式。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_80557_12584_x1076228838}[：指定节点的匹配模式为允许模式。缺省匹配模式为]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[node]{lang="EN-US"}***[ node-number]{lang="EN-US"}*]{#struct_0_80557_12584_x1532254118}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略节点。节点编号越小优先级越高，先对优先级高的节点进行匹配操作。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_1976461224}

[[删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_x1350058006}[策略之前，必须先取消该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略在所有接口上的应用，否则删除失败。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_80557_12584_1467236158}[命令时，如果指定了策略节点，将删除指定的节点；如果指定了节点模式，将按模式删除策略内所有与该模式匹配的所有节点；如果两者都没有指定，将删除整个策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_1271325912}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_580686588}[配置一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[，并进入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略节点视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x26322819}

[\[Sysname\] ipv6 policy-based-route aaa permit node 10]{lang="EN-US"}

[\[Sysname-pbr6-aaa-10\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_1117879233}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_80557_12584_x629787557}**[v6]{lang="EN-US"}[ policy-based-route]{lang="EN-US"}**
:::

::: {#536924487 .myid}
[]{#_Toc404789111}[]{#struct_0_80557_12584_x631599902}[]{#_Toc345339230}[]{#_Toc263858618}[]{#_Toc257723494}[]{#_Toc165364212}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- reset ipv6 policy-based-route statistics**

------------------------------------------------------------------------

[**[reset ipv6 policy-based-route statistics]{lang="EN-US"}**]{#struct_0_80557_12584_x1131081040}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略路由的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_x945822077}

[**[reset ipv6 policy-based-route statistics]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **policy** *policy-name* \]]{lang="EN-US"}]{#struct_0_80557_12584_1271391448}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_1335410827}

[[用户视图]{style="font-family:宋体"}]{#struct_0_80557_12584_x92924775}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_482905110}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_x2054974600}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_587485669}

[[【参数】]{style="font-family:黑体"}]{#struct_0_80557_12584_514973236}

[**[policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_80557_12584_2040416833}[：清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[表示策略名，唯一标识一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x1834714054}

[[系统按照策略名清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_80557_12584_1271456984}[策略路由的统计信息。如果不指定策略名，将清除所有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略的匹配统计信息（该统计信息可以通过]{style="font-family:宋体"}**[display ipv6 policy-based-route interface]{lang="EN-US"}**[命令查看）；如果指定策略名，将清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略的匹配统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_162263085}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1780757402}[清除所有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 policy-based-route statistics]{lang="EN-US"}]{#struct_0_80557_12584_189781217}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_1899392628}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_80557_12584_176648092}**[v6]{lang="EN-US"}[ policy-based-route interface]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_80557_12584_x403614903}**[v6]{lang="EN-US"}[ policy-based-route]{lang="EN-US"}[ local]{lang="EN-US"}**
:::

::::: {#-1695661411 .myid}
[]{#_Toc404789112}[]{#struct_0_80557_12584_x1323383792}

**IPv6策略路由 \-- IPv6策略路由配置命令 \-- snmp-agent trap enable ipv6 policy-based-route**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6策略路由命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_80557_12584_x1170892616}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_80557_12584_1271522520}
:::

[ ]{lang="EN-US"}

[**[snmp-agent trap enable ipv6]{lang="EN-US"}**[ **policy-based-route**]{lang="EN-US"}]{#struct_0_80557_12584_x1383391848}[命令用来开启下一跳失效告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable ipv6 policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_x654610608}[命令用来关闭下一跳]{style="font-family:宋体"}[失效告警功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_80557_12584_682029770}

[**[snmp-agent trap enable]{lang="EN-US"}[ ipv6 policy-based-route]{lang="EN-US"}**]{#struct_0_80557_12584_x1846959746}

[**[undo snmp-agent trap enable]{lang="EN-US"}**[ **ipv6 policy-based-route**]{lang="EN-US"}]{#struct_0_80557_12584_x126585733}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_80557_12584_x657611929}

[[下一跳失效告警功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_80557_12584_2108325421}

[[【视图】]{style="font-family:黑体"}]{#struct_0_80557_12584_645422543}

[[系统视图]{style="font-family:宋体"}]{#struct_0_80557_12584_1270539480}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_80557_12584_216275705}

[[network-admin]{lang="EN-US"}]{#struct_0_80557_12584_573929324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_80557_12584_851867887}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_80557_12584_x737033380}

[[开启]{style="font-family:宋体"}]{#struct_0_80557_12584_1422743105}[IPv6]{lang="EN-US"}[策略路由模块的告警功能后，]{style="font-family:宋体"}[当下一跳的状态由有效变为无效时，]{style="font-family:宋体"}[该模块会生成包含下一跳地址的告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}]{#struct_0_80557_12584_1098748240}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_80557_12584_x328027272}

[[\# ]{lang="EN-US"}]{#struct_0_80557_12584_1270605016}[启用告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_80557_12584_x634088811}

[\[Sysname\] snmp-agent trap enable ipv6 policy-based-route]{lang="EN-US"}
:::::
