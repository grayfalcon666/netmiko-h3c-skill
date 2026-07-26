::::: {#1075343667 .myid}
[]{#_Toc257708816}[]{#_Toc137951582}[]{#_Toc89225269}[]{#_Toc15375049}[]{#_Toc300730342}[]{#_Toc300730105}[]{#_Toc263066864}[]{#_Toc404783060}[]{#struct_0_55199_x9544_x84145130}[]{#_Toc311530788}[]{#_Toc263066920}[]{#_Toc206560297}

**设备管理 \-- 设备管理配置命令 \-- bootrom-access enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_938575337}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x1706024827}
:::

[ ]{lang="EN-US"}

[**[bootrom-access enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1308269705}[命令用来设置在系统启动过程中允许访问]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单。]{style="font-family:宋体"}

[**[undo bootrom-access enable]{lang="EN-US"}**]{#struct_0_55199_x9544_489897375}[命令用来设置在系统启动过程中禁止访问]{style="font-family:
宋体"}[Boot ROM]{lang="EN-US"}[菜单。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1793071989}

[**[bootrom-access enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x600785284}

[**[undo bootrom-access enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x620349293}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1455495808}

[[在系统启动过程中允许访问]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}]{#struct_0_55199_x9544_x84210666}[菜单。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_80500003}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1747719709}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x567190297}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x704438089}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x301885887}

[[缺省情况下，在系统启动过程中，用户在指定时间内按组合键]{style="font-family:宋体"}[\<Ctrl+B\>]{lang="EN-US"}]{#struct_0_55199_x9544_x900646667}[可以进入]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单，以便完成系统软件的加载和对存储介质的管理等操作。为防止非法用户访问]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单，用户可以配置禁止访问]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单。配置禁止访问]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单后，在系统启动过程中即使按组合键]{style="font-family:宋体"}[\<Ctrl+B\>]{lang="EN-US"}[都不会进入]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单，而直接进入命令行配置界面。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x250881316}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x84276202}[设置在系统启动过程中禁止访问]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单。]{style="font-family:宋体"}

[[\<Sysname\> undo bootrom-access enable]{lang="EN-US"}]{#struct_0_55199_x9544_x1519507395}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x504427515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bootrom-access]{lang="EN-US"}**]{#struct_0_55199_x9544_x2095427789}
:::::

::::: {#417572701 .myid}
[]{#_Toc404783061}[]{#struct_0_55199_x9544_1388953278}[]{#_Toc322680636}

**设备管理 \-- 设备管理配置命令 \-- brand**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x51773005}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1849610946}
:::

[ ]{lang="EN-US"}

[**[brand]{lang="EN-US"}**]{#struct_0_55199_x9544_767706000}[命令用来设置主控板的品牌标识。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x84341738}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1256901199}

[**[brand]{lang="EN-US"}**[ { **hp** \| **h3c** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_463646552}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1090012778}[模式：]{style="font-family:宋体"}

[**[brand ]{lang="EN-US"}**[{ **hp \| h3c** } \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1521054015}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1432838516}

[[主控板品牌标识的缺省情况与主控板的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1913014038}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x62172702}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x83882986}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1528566610}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_2076527109}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x486838352}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_589930641}

[**[hp]{lang="EN-US"}**]{#struct_0_55199_x9544_2099917059}[：表示配置主控板的品牌标识为]{style="font-family:宋体"}[hp]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[h3c]{lang="EN-US"}**]{#struct_0_55199_x9544_x365379719}[：表示配置主控板的品牌标识为]{style="font-family:宋体"}[h3c]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_753004711}[：表示主控板所在的槽位号。不指定该参数时，表示对所有主控板进行操作。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x83948522}[：表示指定成员设备上的指定主控板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1494639730}

[[修改主控板的品牌标识后，需要重启该主控板，新品牌标识才能生效。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x680207671}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_30188051}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x602123537}[修改设备主控板的品牌标识为]{style="font-family:宋体"}[HP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> brand hp]{lang="EN-US"}]{#struct_0_55199_x9544_x1856930748}

[ Configuration will take effect after next reboot, do you want to continue? \[Y/N\]: Y]{lang="EN-US"}

[ Configuration is successful.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1774600570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display brand]{lang="EN-US"}**]{#struct_0_55199_x9544_1087588334}
:::::

::::: {#343052021 .myid}
[]{#_Toc404783062}[]{#struct_0_55199_x9544_x84014058}[]{#_Toc350611279}

**设备管理 \-- 设备管理配置命令 \-- card-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_953815235}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_209853500}
:::

[ ]{lang="EN-US"}

[**[card-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_10594848}[命令用来设置接口卡的工作模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1180058340}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x910896482}

[**[card-mode slot ]{lang="EN-US"}***[slot-number mode-name]{lang="EN-US"}*]{#struct_0_55199_x9544_1461763167}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_663793986}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[card-mode slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}***[ ]{lang="EN-US"}***[mode-name]{lang="EN-US"}*]{#struct_0_55199_x9544_x84079594}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_620540828}[模式：]{style="font-family:宋体"}

[**[card-mode chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number* **subslot** *subslot-number* *mode-name*]{lang="EN-US"}]{#struct_0_55199_x9544_1366796993}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x960622842}

[[与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1468855616}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_732988489}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_188434669}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_284451012}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x83620842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_2103992928}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1395947833}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1382550606}[：子卡所在槽位号。（集中式设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1615946421}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1213237781}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_260399163}[：指定成员设备上指定单板。]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[subslot]{lang="EN-US"}**[ *subslot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1123906887}[：子卡所在的子槽位号。]{style="font-family:宋体"}

[*[mode-name]{lang="EN-US"}*]{#struct_0_55199_x9544_x567975986}[：指定接口卡的工作模式。工作模式如下所示，但支持情况与接口卡的型号有关，请以接口卡的实际情况为准。]{style="font-family:宋体"}

[**[e]{lang="EN-US"}**]{#struct_0_55199_x9544_x83686378}[：配置接口卡的工作模式为]{style="font-family:宋体"}[E]{lang="EN-US"}[模式（包括]{style="font-family:宋体"}[E1]{lang="EN-US"}[模式和]{style="font-family:宋体"}[E3]{lang="EN-US"}[模式）。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[CPOS E3E1]{lang="EN-US"}[融合接口使用。关于]{style="font-family:宋体"}[CPOS E3E1]{lang="EN-US"}[融合接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[t]{lang="EN-US"}**]{#struct_0_55199_x9544_x610248774}[：配置接口卡的工作模式为]{style="font-family:宋体"}[T]{lang="EN-US"}[模式（包括]{style="font-family:宋体"}[T1]{lang="EN-US"}[模式和]{style="font-family:宋体"}[T3]{lang="EN-US"}[模式）。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[CPOS T3T1]{lang="EN-US"}[融合接口使用。关于]{style="font-family:宋体"}[CPOS T3 T1]{lang="EN-US"}[融合接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[e1]{lang="EN-US"}**]{#struct_0_55199_x9544_1887073997}[：配置接口卡的工作模式为]{style="font-family:宋体"}[E1]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[CPOS E1]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[CPOS E1]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[t1]{lang="EN-US"}**]{#struct_0_55199_x9544_548537038}[：配置接口卡的工作模式为]{style="font-family:宋体"}[T1]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[CPOS T1]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[CPOS T1]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[e3]{lang="EN-US"}**]{#struct_0_55199_x9544_x2000102444}[：配置接口卡的工作模式为]{style="font-family:宋体"}[E3]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[CPOS E3]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[CPOS E3]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[t3]{lang="EN-US"}**]{#struct_0_55199_x9544_1921436479}[：配置接口卡的工作模式为]{style="font-family:宋体"}[T3]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[CPOS T3]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[CPOS T3]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[pos]{lang="EN-US"}**]{#struct_0_55199_x9544_x1678751197}[：配置接口卡的工作模式为]{style="font-family:宋体"}[POS]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[POS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[e-cpos]{lang="EN-US"}**]{#struct_0_55199_x9544_x2000036908}[：配置接口卡的工作模式为]{style="font-family:宋体"}[E-CPOS]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[oc-3]{lang="EN-US"}**]{#struct_0_55199_x9544_x458333885}[：配置接口卡的工作模式为]{style="font-family:宋体"}[OC-3c/STM-1c]{lang="EN-US"}[（]{style="font-family:宋体"}[155Mbps)]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[oc-12]{lang="EN-US"}**]{#struct_0_55199_x9544_x1059089313}[：配置接口卡的工作模式为]{style="font-family:宋体"}[OC-12c/STM-4c]{lang="EN-US"}[（]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[）模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[CPOS T3]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[ipsec]{lang="EN-US"}**]{#struct_0_55199_x9544_290840271}[：配置加密接口卡的加密模式为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[ssl]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999971372}[：配置加密接口卡的加密模式为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[atm]{lang="EN-US"}**]{#struct_0_55199_x9544_1721245247}[：配置接口卡的工作模式]{style="font-family:宋体"}[ATM]{lang="EN-US"}[模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999905836}[：表示接口卡自动选择工作在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[模式或者]{style="font-family:宋体"}[EFM]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[efm]{lang="EN-US"}**]{#struct_0_55199_x9544_x1373017439}[：配置接口卡的工作模式]{style="font-family:宋体"}[EFM]{lang="EN-US"}[（]{style="font-family:宋体"}[Ethernet First Mile]{lang="EN-US"}[）模式。配置后，该接口卡上的所有接口可作为]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口使用。关于]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口的详细介绍请参见"接口管理配置指导"中"]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_255924394}

[[模式切换后是必须重启设备或热插拔接口卡（如果接口卡支持热插拔），新配置的模式才会生效，还是配置后新模式立即生效，与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1483520632}

[[缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_55199_x9544_941193514}[支持该命令，非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[不支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1141737778}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x884516275}[将位于]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位的接口卡的工作模式设置为]{style="font-family:宋体"}[E3]{lang="EN-US"}[模式。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x2000364588}

[\[Sysname\] card-mode slot 2 e3]{lang="EN-US"}

[Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_297292408}[将位于]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位的接口卡]{style="font-family:宋体"}[1]{lang="EN-US"}[的工作模式设置为]{style="font-family:宋体"}[E3]{lang="EN-US"}[模式。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1496909407}

[\[Sysname\] card-mode slot 2 subslot 1 e3]{lang="EN-US"}

[Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1363739468}[将位于成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位的接口卡]{style="font-family:
宋体"}[1]{lang="EN-US"}[的工作模式设置为]{style="font-family:宋体"}[E3]{lang="EN-US"}[模式。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1860951244}

[\[Sysname\] card-mode chassis 1 slot 2 subslot 1 e3]{lang="EN-US"}

[Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1354182361}[将位于]{style="font-family:宋体"}[0]{lang="EN-US"}[号槽位的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口卡的工作模式设置为]{style="font-family:宋体"}[EFM]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x2000299052}

[\[Sysname\] card-mode slot 0 efm]{lang="EN-US"}

[Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.]{lang="EN-US"}
:::::

::: {#517905655 .myid}
[]{#_Toc404783063}[]{#struct_0_55199_x9544_1044390668}

**设备管理 \-- 设备管理配置命令 \-- clock datetime**

------------------------------------------------------------------------

[**[clock datetime]{lang="EN-US"}**]{#struct_0_55199_x9544_x211008521}[命令用来设置设备的]{style="font-family:宋体"}[UTC]{lang="EN-US"}[（]{style="font-family:宋体"}[Coordinated Universal Time]{lang="EN-US"}[，国际协调时间）时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1347389805}

[**[clock datetime]{lang="EN-US"}**[ *time date*]{lang="EN-US"}]{#struct_0_55199_x9544_12121870}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x947099132}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x675651475}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1154380248}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2000233516}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1652413241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x147715059}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_817088183}

[*[time]{lang="EN-US"}*]{#struct_0_55199_x9544_x281945348}[：设置的时间，格式为]{style="font-family:宋体"}[HH:MM:SS]{lang="EN-US"}[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟]{style="font-family:宋体"}[:]{lang="EN-US"}[秒），]{style="font-family:宋体"}[HH]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}[MM]{lang="EN-US"}[和]{style="font-family:宋体"}[SS]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。比如将]{style="font-family:宋体"}*[time]{lang="EN-US"}*[参数设置为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示零点。]{style="font-family:宋体"}

[*[date]{lang="EN-US"}*]{#struct_0_55199_x9544_1445104722}[：设置的日期，格式为]{style="font-family:宋体"}[MM/DD/YYYY]{lang="EN-US"}[（月]{style="font-family:宋体"}[/]{lang="EN-US"}[日]{style="font-family:宋体"}[/]{lang="EN-US"}[年）或者]{style="font-family:宋体"}[YYYY/MM/DD]{lang="EN-US"}[（年]{style="font-family:宋体"}[/]{lang="EN-US"}[月]{style="font-family:宋体"}[/]{lang="EN-US"}[日），]{style="font-family:
宋体"}[MM]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[，]{style="font-family:宋体"}[DD]{lang="EN-US"}[的取值范围与月份有关，]{style="font-family:宋体"}[YYYY]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2035]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_701591881}

[[命令行配置的系统时间由配置的]{style="font-family:宋体"}[UTC]{lang="EN-US"}]{#struct_0_55199_x9544_x2000167980}[时间、本地时区和夏令时运算之后联合决定，通过]{style="font-family:宋体"}**[display clock]{lang="EN-US"}**[命令可以查看。]{style="font-family:宋体"}

[[为了保证与其它设备协调工作，为了更好的监控和维护设备，请将系统时间配置准确。用户可使用该命令来配置系统时间，或者通过]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_55199_x9544_1454151102}[、]{style="font-family:宋体"}[PTP]{lang="EN-US"}[协议获取系统时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_70626716}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_819115998}[设置设备的]{style="font-family:宋体"}[UTC]{lang="EN-US"}[时间为]{style="font-family:宋体"}[2012]{lang="EN-US"}[年]{style="font-family:宋体"}[1]{lang="EN-US"}[月]{style="font-family:
宋体"}[1]{lang="EN-US"}[日]{style="font-family:宋体"}[8]{lang="EN-US"}[时]{style="font-family:宋体"}[8]{lang="EN-US"}[分]{style="font-family:宋体"}[8]{lang="EN-US"}[秒。]{style="font-family:
宋体"}

[[\<Sysname\> clock datetime 8:8:8 1/1/2012]{lang="EN-US"}]{#struct_0_55199_x9544_1214863594}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_358393427}[设置设备的]{style="font-family:宋体"}[UTC]{lang="EN-US"}[时间为]{style="font-family:宋体"}[2012]{lang="EN-US"}[年]{style="font-family:宋体"}[1]{lang="EN-US"}[月]{style="font-family:
宋体"}[1]{lang="EN-US"}[日]{style="font-family:宋体"}[8]{lang="EN-US"}[时]{style="font-family:宋体"}[10]{lang="EN-US"}[分。]{style="font-family:宋体"}

[[\<Sysname\> clock datetime 8:10 2012/1/1]{lang="EN-US"}]{#struct_0_55199_x9544_212615245}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1679298607}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock protocol]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999578156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock summer-time]{lang="EN-US"}**]{#struct_0_55199_x9544_x1801368619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock timezone]{lang="EN-US"}**]{#struct_0_55199_x9544_x14675147}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display clock]{lang="EN-US"}**]{#struct_0_55199_x9544_x1331919349}
:::

::: {#591691415 .myid}
[]{#_Toc404783064}[]{#struct_0_55199_x9544_x1999512620}[]{#_Toc353181690}[]{#_Toc340828665}

**设备管理 \-- 设备管理配置命令 \-- clock protocol**

------------------------------------------------------------------------

[**[clock protocol]{lang="EN-US"}**]{#struct_0_55199_x9544_x1521813638}[命令用来配置获取系统时间的方式。]{style="font-family:宋体"}

[**[undo clock protocol]{lang="EN-US"}**]{#struct_0_55199_x9544_x2000102443}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1614015930}

[**[clock protocol ]{lang="EN-US"}**[{ **none** \| { **ntp** \| **ptp** } **mdc** *mdc-id* }]{lang="EN-US"}]{#struct_0_55199_x9544_919140727}

[**[undo clock protocol]{lang="EN-US"}**]{#struct_0_55199_x9544_x1594889623}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1108101629}

[[由缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_55199_x9544_x2000036907}[通过的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[协议获取系统时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_751519696}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1144990537}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1999971371}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_155161306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x147452915}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_474884047}

[**[none]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999905835}[：表示通过本地时钟源获取系统时间。配置该参数后，用户可通过]{style="font-family:宋体"}**[clock datetime]{lang="EN-US"}**[、]{style="font-family:宋体"}**[clock timezone]{lang="EN-US"}**[、]{style="font-family:宋体"}**[clock summer-time]{lang="EN-US"}**[命令修改系统时间。]{style="font-family:宋体"}

[**[ptp]{lang="EN-US"}**]{#struct_0_55199_x9544_x2000364587}[：表示通过]{style="font-family:宋体"}[PTP]{lang="EN-US"}[（]{style="font-family:宋体"}[Precision Time Protocol]{lang="EN-US"}[，精确时间协议）协议获取系统时间。配置该参数后，用户不能通过命令行修改系统时间，需要配置]{style="font-family:宋体"}[PTP]{lang="EN-US"}[的相关参数才能获取到时钟。关于]{style="font-family:宋体"}[PTP]{lang="EN-US"}[的详细介绍和配置，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[PTP]{lang="EN-US"}["。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ntp]{lang="EN-US"}**]{#struct_0_55199_x9544_x2000299051}[：表示通过]{style="font-family:宋体"}[NTP]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Time Protocol]{lang="EN-US"}[，网络时间协议）协议获取系统时间。配置该参数后，用户不能通过命令行修改系统时间，需要配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的相关参数才能获取到时钟。关于]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的详细介绍和配置，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[NTP]{lang="EN-US"}["。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mdc ]{lang="EN-US"}**]{#struct_0_55199_x9544_x2000167979}*[mdc-id]{lang="EN-US"}*[：表示时钟的来源]{style="font-family:宋体"}[MDC]{lang="EN-US"}[编号。本参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1993661913}

[[所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_55199_x9544_x1999578155}[共用一个时钟源，系统时间相同。这个共用时钟源可以是：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地时钟源，设备上的晶体振荡器产生的时钟信号。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2000102442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[网络时钟源，通过协议从其它网络设备上获取的时钟信号。设备根据用户的配置，从指定的]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2000364586}[MDC]{lang="EN-US"}[，使用指定的协议获取时间后，同步给其它]{style="font-family:宋体"}[MDC]{lang="EN-US"}[作为系统时间。]{style="font-family:宋体"}

[[多次使用该命令配置不同的系统时间获取方式时，新配置将覆盖旧配置。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2000299050}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2087777214}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x2000233514}[配置通过本地时钟源获取系统时间。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x2000167978}

[\[Sysname\] clock protocol none]{lang="EN-US"}
:::

::: {#781602660 .myid}
[]{#_Toc404783065}[]{#_Toc311117314}[]{#struct_0_55199_x9544_427577972}

**设备管理 \-- 设备管理配置命令 \-- clock summer-time**

------------------------------------------------------------------------

[**[clock summer-time]{lang="EN-US"}**]{#struct_0_55199_x9544_1101268724}[命令用来设置夏令时。]{style="font-family:宋体"}

[**[undo clock summer-time]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999578154}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x638569205}

[**[clock summer-time]{lang="EN-US"}**[ *name* *start-time* *start-date end-time* *end-date* *add*-*time*]{lang="EN-US"}]{#struct_0_55199_x9544_x1292430672}

[**[undo clock summer-time]{lang="EN-US"}**]{#struct_0_55199_x9544_x748486116}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1479256660}

[[没有配置夏令时。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1523072968}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1324621083}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_2079762497}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1999512618}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1878240606}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x148108276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1899650101}

[*[name]{lang="EN-US"}*]{#struct_0_55199_x9544_x867565565}[：夏令时的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[start-time]{lang="EN-US"}*]{#struct_0_55199_x9544_x1664653266}[：开始时间，格式为]{style="font-family:宋体"}[HH:MM:SS]{lang="EN-US"}[，]{style="font-family:宋体"}[HH]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}[MM]{lang="EN-US"}[和]{style="font-family:宋体"}[SS]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。]{style="font-family:宋体"}

[*[start-date]{lang="EN-US"}*]{#struct_0_55199_x9544_414889531}[：开始日期，有两种输入方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[直接一次性输入月和日，参数格式为]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1876439141}[MM/DD]{lang="EN-US"}[，]{style="font-family:宋体"}[MM]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[，]{style="font-family:宋体"}[DD]{lang="EN-US"}[的取值范围与月份有关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分次输入月、日，各参数之间以]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2000102441}[\<]{lang="EN-US"}[空格]{style="font-family:宋体"}[\>]{lang="EN-US"}[键隔开。首先输入开始的月份，取值如下：]{style="font-family:宋体"}**[January]{lang="EN-US"}**[、]{style="font-family:宋体"}**[February]{lang="EN-US"}**[、]{style="font-family:宋体"}**[March]{lang="EN-US"}**[、]{style="font-family:宋体"}**[April]{lang="EN-US"}**[、]{style="font-family:宋体"}**[May]{lang="EN-US"}**[、]{style="font-family:宋体"}**[June]{lang="EN-US"}**[、]{style="font-family:宋体"}**[July]{lang="EN-US"}**[、]{style="font-family:宋体"}**[August]{lang="EN-US"}**[、]{style="font-family:宋体"}**[September]{lang="EN-US"}**[、]{style="font-family:宋体"}**[October]{lang="EN-US"}**[、]{style="font-family:宋体"}**[November]{lang="EN-US"}**[或]{style="font-family:宋体"}**[December]{lang="EN-US"}**[；然后输入开始的星期，用当月的第几个星期表示，取值如下：]{style="font-family:宋体"}**[first]{lang="EN-US"}**[、]{style="font-family:宋体"}**[second]{lang="EN-US"}**[、]{style="font-family:宋体"}**[third]{lang="EN-US"}**[、]{style="font-family:宋体"}**[fourth]{lang="EN-US"}**[、]{style="font-family:宋体"}**[fifth]{lang="EN-US"}**[或]{style="font-family:宋体"}**[last]{lang="EN-US"}**[；最后输入起始日，取值为]{style="font-family:宋体"}**[Sunday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Monday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Tuesday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Wednesday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Thursday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Friday]{lang="EN-US"}**[或]{style="font-family:宋体"}**[Saturday]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[end-time]{lang="EN-US"}*]{#struct_0_55199_x9544_1518151952}[：结束时间，格式为]{style="font-family:宋体"}[HH:MM:SS]{lang="EN-US"}[，]{style="font-family:宋体"}[HH]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}[MM]{lang="EN-US"}[和]{style="font-family:宋体"}[SS]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。]{style="font-family:宋体"}

[*[end-date]{lang="EN-US"}*]{#struct_0_55199_x9544_x1488744339}[：结束日期，有两种输入方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[直接一次性输入月日，参数格式为]{style="font-family:宋体"}]{#struct_0_55199_x9544_179358933}[MM/DD]{lang="EN-US"}[，]{style="font-family:宋体"}[MM]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="EN-US"}[，]{style="font-family:宋体"}[DD]{lang="EN-US"}[的取值范围与月份有关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分次输入月、日，各参数之间以]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2065416553}[\<]{lang="EN-US"}[空格]{style="font-family:宋体"}[\>]{lang="EN-US"}[键隔开。首先输入开始的月份，取值如下：]{style="font-family:宋体"}**[January]{lang="EN-US"}**[、]{style="font-family:宋体"}**[February]{lang="EN-US"}**[、]{style="font-family:宋体"}**[March]{lang="EN-US"}**[、]{style="font-family:宋体"}**[April]{lang="EN-US"}**[、]{style="font-family:宋体"}**[May]{lang="EN-US"}**[、]{style="font-family:宋体"}**[June]{lang="EN-US"}**[、]{style="font-family:宋体"}**[July]{lang="EN-US"}**[、]{style="font-family:宋体"}**[August]{lang="EN-US"}**[、]{style="font-family:宋体"}**[September]{lang="EN-US"}**[、]{style="font-family:宋体"}**[October]{lang="EN-US"}**[、]{style="font-family:宋体"}**[November]{lang="EN-US"}**[或]{style="font-family:宋体"}**[December]{lang="EN-US"}**[；然后输入开始的星期，用当月的第几个星期表示，取值如下：]{style="font-family:宋体"}**[first]{lang="EN-US"}**[、]{style="font-family:宋体"}**[second]{lang="EN-US"}**[、]{style="font-family:宋体"}**[third]{lang="EN-US"}**[、]{style="font-family:宋体"}**[fourth]{lang="EN-US"}**[、]{style="font-family:宋体"}**[fifth]{lang="EN-US"}**[或]{style="font-family:宋体"}**[last]{lang="EN-US"}**[；最后输入起始日，取值为]{style="font-family:宋体"}**[Sunday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Monday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Tuesday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Wednesday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Thursday]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Friday]{lang="EN-US"}**[或]{style="font-family:宋体"}**[Saturday]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[add-time]{lang="EN-US"}*]{#struct_0_55199_x9544_1160045566}[：偏移时间，格式为]{style="font-family:宋体"}[HH:MM:SS]{lang="EN-US"}[，]{style="font-family:宋体"}[HH]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}[MM]{lang="EN-US"}[和]{style="font-family:宋体"}[SS]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_722246361}

[[命令行配置的系统时间由配置的]{style="font-family:宋体"}[UTC]{lang="EN-US"}]{#struct_0_55199_x9544_x2000036905}[时间、本地时区和夏令时运算之后联合决定，通过]{style="font-family:宋体"}**[display clock]{lang="EN-US"}**[命令可以查看。为了保证与其它设备协调工作，为了更好的监控和维护设备，请将所有网络设备的夏令时配置保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x411279718}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_460128823}[设置夏令时]{style="font-family:宋体"}[PDT]{lang="EN-US"}[，从每年的]{style="font-family:宋体"}[8]{lang="EN-US"}[月]{style="font-family:宋体"}[1]{lang="EN-US"}[日的]{style="font-family:
宋体"}[06:00:00]{lang="EN-US"}[开始，到]{style="font-family:宋体"}[9]{lang="EN-US"}[月]{style="font-family:宋体"}[1]{lang="EN-US"}[日的]{style="font-family:宋体"}[06:00:00]{lang="EN-US"}[结束，比当前设备标准时间增加]{style="font-family:宋体"}[1]{lang="EN-US"}[小时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_528462845}

[\[Sysname\] clock summer-time PDT 6 08/01 6 09/01 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1483750817}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock datetime]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999971369}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock timezone]{lang="EN-US"}**]{#struct_0_55199_x9544_x613502552}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display clock]{lang="EN-US"}**]{#struct_0_55199_x9544_x1354569398}
:::

::: {#592182289 .myid}
[]{#_Toc309658907}[]{#_Toc296584671}[]{#_Toc295572798}[]{#_Toc295459110}[]{#_Toc404783066}[]{#struct_0_55199_x9544_x167723166}[]{#_Toc300730343}[]{#_Toc300730106}[]{#_Toc263066867}

**设备管理 \-- 设备管理配置命令 \-- clock timezone**

------------------------------------------------------------------------

[**[clock timezone]{lang="EN-US"}**]{#struct_0_55199_x9544_1542356790}[命令用来对本地时区进行设置。]{style="font-family:宋体"}

[**[undo clock timezone]{lang="EN-US"}**]{#struct_0_55199_x9544_x2000364585}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x818452839}

[**[clock timezone]{lang="EN-US"}**[ *zone-name* { **add** \| **minus** } *zone-offset*]{lang="EN-US"}]{#struct_0_55199_x9544_x1274746520}

[**[undo clock timezone]{lang="EN-US"}**]{#struct_0_55199_x9544_x473824773}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1042863468}

[[本地时区采用]{style="font-family:宋体"}[UTC]{lang="EN-US"}]{#struct_0_55199_x9544_x53359047}[时区。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1774772856}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x574808618}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2000299049}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_284941317}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x147846132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_803521341}

[*[zone-name]{lang="EN-US"}*]{#struct_0_55199_x9544_993371010}[：时区名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[add]{lang="EN-US"}**]{#struct_0_55199_x9544_x524012862}[：在]{style="font-family:宋体"}[UTC]{lang="EN-US"}[时间的基础上增加指定时间。]{style="font-family:宋体"}

[**[minus]{lang="EN-US"}**]{#struct_0_55199_x9544_x1160255065}[：在]{style="font-family:宋体"}[UTC]{lang="EN-US"}[时间的基础上减少指定时间。]{style="font-family:宋体"}

[*[zone-offset]{lang="EN-US"}*]{#struct_0_55199_x9544_1395040413}[：与]{style="font-family:宋体"}[UTC]{lang="EN-US"}[的时间差，格式为]{style="font-family:宋体"}[HH:MM:SS]{lang="EN-US"}[，]{style="font-family:宋体"}[HH]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}[MM]{lang="EN-US"}[和]{style="font-family:宋体"}[SS]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[，如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_758339756}

[[命令行配置的系统时间由配置的]{style="font-family:宋体"}[UTC]{lang="EN-US"}]{#struct_0_55199_x9544_x2000233513}[时间、本地时区和夏令时运算之后联合决定，通过]{style="font-family:宋体"}**[display clock]{lang="EN-US"}**[命令可以查看。为了保证与其它设备协调工作，为了更好的监控和维护设备，请将所有网络设备的时区和当地地理时区保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1883039168}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1311197512}[设置本地时区名称为]{style="font-family:宋体"}[Z5]{lang="EN-US"}[，比]{style="font-family:宋体"}[UTC]{lang="EN-US"}[标准时间增加]{style="font-family:宋体"}[5]{lang="EN-US"}[小时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_793868706}

[\[Sysname\] clock timezone Z5 add 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2000167977}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock datetime]{lang="EN-US"}**]{#struct_0_55199_x9544_x1850966689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock summer-time]{lang="EN-US"}**]{#struct_0_55199_x9544_x1475992689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display clock]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999578153}
:::

::: {#213757135 .myid}
[]{#_Toc404783067}[]{#struct_0_55199_x9544_2090314150}

**设备管理 \-- 设备管理配置命令 \-- command**

------------------------------------------------------------------------

[**[command]{lang="EN-US"}**]{#struct_0_55199_x9544_x614982160}[命令用来为]{style="font-family:宋体"}[Job]{lang="EN-US"}[分配命令。]{style="font-family:宋体"}

[**[undo command]{lang="EN-US"}**]{#struct_0_55199_x9544_2018109897}[命令用来取消为]{style="font-family:宋体"}[Job]{lang="EN-US"}[分配的命令。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1316694151}

[**[command ]{lang="EN-US"}***[id command]{lang="EN-US"}*]{#struct_0_55199_x9544_1556993866}

[**[undo command ]{lang="EN-US"}***[id]{lang="EN-US"}*]{#struct_0_55199_x9544_x645806562}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x986032595}

[[没有为]{style="font-family:宋体"}[Job]{lang="EN-US"}]{#struct_0_55199_x9544_749886151}[分配命令。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1999512617}

[[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x1118725719}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x466308820}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1534819341}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_93733971}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1029542596}

[*[id]{lang="EN-US"}*]{#struct_0_55199_x9544_x1787725181}[：命令编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。该编号表示命令在]{style="font-family:宋体"}[Job]{lang="EN-US"}[中的执行顺序，编号小的命令优先执行。]{style="font-family:宋体"}

[*[command]{lang="EN-US"}*]{#struct_0_55199_x9544_x639936507}[：为]{style="font-family:宋体"}[Job]{lang="EN-US"}[分配的命令。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2000102440}

[[多次输入]{style="font-family:宋体"}**[command]{lang="EN-US"}**]{#struct_0_55199_x9544_x47931989}[命令可以为当前]{style="font-family:宋体"}[Job]{lang="EN-US"}[分配多条命令，不同命令用编号来唯一区别。如果新分配命令的编号和已分配的某命令的编号相同，则新分配的命令会覆盖已分配的命令。]{style="font-family:宋体"}

[[通过]{style="font-family:宋体"}**[command]{lang="EN-US"}**]{#struct_0_55199_x9544_254732468}[分配的命令行必须是设备上可成功执行的命令行，不包括]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ftp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ssh2]{lang="EN-US"}**[和]{style="font-family:宋体"}**[monitor process]{lang="EN-US"}**[。由用户保证配置的正确性，否则，命令行不能自动被执行。]{style="font-family:宋体"}

[[如果需要分配的命令（假设为]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_55199_x9544_1220694100}[）是用户视图下的命令，则直接使用]{style="font-family:宋体"}**[command]{lang="EN-US"}**[命令分配即可，比如：]{style="font-family:宋体"}[command 1 display interface]{lang="EN-US"}[；如果需要分配的命令（假设为]{style="font-family:宋体"}[A]{lang="EN-US"}[）是非用户视图下的命令，则必须先分配进入]{style="font-family:宋体"}[A]{lang="EN-US"}[所在视图的命令（指定较小的]{style="font-family:宋体"}*[id]{lang="EN-US"}*[值），再分配]{style="font-family:宋体"}[A]{lang="EN-US"}[。比如：要使用]{style="font-family:宋体"}[Job]{lang="EN-US"}[定时执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令，则需执行三次]{style="font-family:宋体"}**[command]{lang="EN-US"}**[命令，分别分配]{style="font-family:宋体"}**[system-view]{lang="EN-US"}**[、]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[、]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令，且各]{style="font-family:宋体"}**[command]{lang="EN-US"}**[命令的]{style="font-family:宋体"}*[id]{lang="EN-US"}*[值逐渐增大。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_805528653}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_725582653}[为]{style="font-family:宋体"}[Job]{lang="EN-US"}[（假设名称为]{style="font-family:宋体"}[backupconfig]{lang="EN-US"}[）分配命令，以便将配置文件]{style="font-family:宋体"}[startup.cfg]{lang="EN-US"}[备份到]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.100.11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_604459246}

[\[Sysname\] scheduler job backupconfig]{lang="EN-US"}

[\[Sysname-job-backupconfig\] command 2 tftp 192.168.100.11 put flash:/startup.cfg backup.cfg]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x345389841}[为]{style="font-family:宋体"}[Job]{lang="EN-US"}[（假设名称为]{style="font-family:宋体"}[shutdownGE]{lang="EN-US"}[）分配命令，以便将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[关闭。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1395468900}

[\[Sysname\] scheduler job shutdownGE]{lang="EN-US"}

[\[Sysname-job-shutdownGE\] command 1 system-view]{lang="EN-US"}

[\[Sysname-job-shutdownGE\] command 2 interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-job-shutdownGE\] command 3 shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x990954416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler job]{lang="EN-US"}**]{#struct_0_55199_x9544_859699447}
:::

::: {#988508100 .myid}
[]{#_Toc404783068}[]{#struct_0_55199_x9544_x2000036904}[]{#_Toc300730344}[]{#_Toc300730107}[]{#_Toc263066869}

**设备管理 \-- 设备管理配置命令 \-- copyright-info enable**

------------------------------------------------------------------------

[**[copyright-info enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1154804223}[命令用来使能显示版权信息。]{style="font-family:宋体"}

[**[undo copyright-info enable]{lang="EN-US"}**]{#struct_0_55199_x9544_2106610079}[命令用来禁止显示版权信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_41162670}

[**[copyright-info enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x413177502}

[**[undo copyright-info enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x1613085003}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x256889685}

[[显示版权信息处于使能状态。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x388291758}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1999971368}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1767087459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1191233425}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1545409351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_843078849}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x238169232}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1024585140}[使能显示版权信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x877076886}

[\[Sysname\] copyright-info enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1999905832}[Telnet]{lang="EN-US"}[方式登录设备，会显示如下信息：]{style="font-family:宋体"}

[[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}]{#struct_0_55199_x9544_952581389}

[\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.\*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                               \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                  \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果当前已经使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1941393351}[Console]{lang="EN-US"}[口登录设备了，再退出用户视图重新登录，会显示如下信息：]{style="font-family:宋体"}

[[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}]{#struct_0_55199_x9544_x1317780956}

[\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.\*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                               \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                  \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[User interface con0 is available.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Press ENTER to get started.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1403612074}[禁止显示版权信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x2000364584}

[\[Sysname\] undo copyright-info enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_1910430516}[Telnet]{lang="EN-US"}[方式登录设备，会显示如下信息：]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}]{#struct_0_55199_x9544_x1670314848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果当前已经使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_x398342073}[Console]{lang="EN-US"}[口登录设备了，再退出用户视图重新登录，会显示如下信息：]{style="font-family:宋体"}

[[User interface con0 is available.]{lang="EN-US"}]{#struct_0_55199_x9544_x1087292267}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Press ENTER to get started.]{lang="EN-US"}
:::

::::: {#1945436061 .myid}
[]{#_Toc300730345}[]{#_Toc300730108}[]{#_Toc263066872}[]{#_Toc404783069}[]{#struct_0_55199_x9544_x286865852}[]{#_Toc306695852}[]{#_Toc300838328}[]{#_Toc299977220}[]{#_Toc263066870}[]{#_Toc299957985}[]{#_Toc299958436}[]{#_Toc299958668}[]{#_Toc299977224}[]{#_Toc300730109}[]{#_Toc300730346}[]{#_Toc300730542}[]{#_Toc300731444}[]{#_Toc300732180}[]{#_Toc300733064}[]{#_Toc300733338}[]{#_Toc300751160}[]{#_Toc300751354}[]{#_Toc300753466}[]{#_Toc300761939}[]{#_Toc300764380}[]{#_Toc300765500}[]{#_Toc299957986}[]{#_Toc299958437}[]{#_Toc299958669}[]{#_Toc299977225}[]{#_Toc300730110}[]{#_Toc300730347}[]{#_Toc300730543}[]{#_Toc300731445}[]{#_Toc300732181}[]{#_Toc300733065}[]{#_Toc300733339}[]{#_Toc300751161}[]{#_Toc300751355}[]{#_Toc300753467}[]{#_Toc300761940}[]{#_Toc300764381}[]{#_Toc300765501}[]{#_Toc299957987}[]{#_Toc299958438}[]{#_Toc299958670}[]{#_Toc299977226}[]{#_Toc300730111}[]{#_Toc300730348}[]{#_Toc300730544}[]{#_Toc300731446}[]{#_Toc300732182}[]{#_Toc300733066}[]{#_Toc300733340}[]{#_Toc300751162}[]{#_Toc300751356}[]{#_Toc300753468}[]{#_Toc300761941}[]{#_Toc300764382}[]{#_Toc300765502}[]{#_Toc299957988}[]{#_Toc299958439}[]{#_Toc299958671}[]{#_Toc299977227}[]{#_Toc300730112}[]{#_Toc300730349}[]{#_Toc300730545}[]{#_Toc300731447}[]{#_Toc300732183}[]{#_Toc300733067}[]{#_Toc300733341}[]{#_Toc300751163}[]{#_Toc300751357}[]{#_Toc300753469}[]{#_Toc300761942}[]{#_Toc300764383}[]{#_Toc300765503}[]{#_Toc299957989}[]{#_Toc299958440}[]{#_Toc299958672}[]{#_Toc299977228}[]{#_Toc300730113}[]{#_Toc300730350}[]{#_Toc300730546}[]{#_Toc300731448}[]{#_Toc300732184}[]{#_Toc300733068}[]{#_Toc300733342}[]{#_Toc300751164}[]{#_Toc300751358}[]{#_Toc300753470}[]{#_Toc300761943}[]{#_Toc300764384}[]{#_Toc300765504}[]{#_Toc299957990}[]{#_Toc299958441}[]{#_Toc299958673}[]{#_Toc299977229}[]{#_Toc300730114}[]{#_Toc300730351}[]{#_Toc300730547}[]{#_Toc300731449}[]{#_Toc300732185}[]{#_Toc300733069}[]{#_Toc300733343}[]{#_Toc300751165}[]{#_Toc300751359}[]{#_Toc300753471}[]{#_Toc300761944}[]{#_Toc300764385}[]{#_Toc300765505}[]{#_Toc299957991}[]{#_Toc299958442}[]{#_Toc299958674}[]{#_Toc299977230}[]{#_Toc300730115}[]{#_Toc300730352}[]{#_Toc300730548}[]{#_Toc300731450}[]{#_Toc300732186}[]{#_Toc300733070}[]{#_Toc300733344}[]{#_Toc300751166}[]{#_Toc300751360}[]{#_Toc300753472}[]{#_Toc300761945}[]{#_Toc300764386}[]{#_Toc300765506}[]{#_Toc299957992}[]{#_Toc299958443}[]{#_Toc299958675}[]{#_Toc299977231}[]{#_Toc300730116}[]{#_Toc300730353}[]{#_Toc300730549}[]{#_Toc300731451}[]{#_Toc300732187}[]{#_Toc300733071}[]{#_Toc300733345}[]{#_Toc300751167}[]{#_Toc300751361}[]{#_Toc300753473}[]{#_Toc300761946}[]{#_Toc300764387}[]{#_Toc300765507}[]{#_Toc299957993}[]{#_Toc299958444}[]{#_Toc299958676}[]{#_Toc299977232}[]{#_Toc300730117}[]{#_Toc300730354}[]{#_Toc300730550}[]{#_Toc300731452}[]{#_Toc300732188}[]{#_Toc300733072}[]{#_Toc300733346}[]{#_Toc300751168}[]{#_Toc300751362}[]{#_Toc300753474}[]{#_Toc300761947}[]{#_Toc300764388}[]{#_Toc300765508}[]{#_Toc299957994}[]{#_Toc299958445}[]{#_Toc299958677}[]{#_Toc299977233}[]{#_Toc300730118}[]{#_Toc300730355}[]{#_Toc300730551}[]{#_Toc300731453}[]{#_Toc300732189}[]{#_Toc300733073}[]{#_Toc300733347}[]{#_Toc300751169}[]{#_Toc300751363}[]{#_Toc300753475}[]{#_Toc300761948}[]{#_Toc300764389}[]{#_Toc300765509}[]{#_Toc299957995}[]{#_Toc299958446}[]{#_Toc299958678}[]{#_Toc299977234}[]{#_Toc300730119}[]{#_Toc300730356}[]{#_Toc300730552}[]{#_Toc300731454}[]{#_Toc300732190}[]{#_Toc300733074}[]{#_Toc300733348}[]{#_Toc300751170}[]{#_Toc300751364}[]{#_Toc300753476}[]{#_Toc300761949}[]{#_Toc300764390}[]{#_Toc300765510}[]{#_Toc299957996}[]{#_Toc299958447}[]{#_Toc299958679}[]{#_Toc299977235}[]{#_Toc300730120}[]{#_Toc300730357}[]{#_Toc300730553}[]{#_Toc300731455}[]{#_Toc300732191}[]{#_Toc300733075}[]{#_Toc300733349}[]{#_Toc300751171}[]{#_Toc300751365}[]{#_Toc300753477}[]{#_Toc300761950}[]{#_Toc300764391}[]{#_Toc300765511}[]{#_Toc299957997}[]{#_Toc299958448}[]{#_Toc299958680}[]{#_Toc299977236}[]{#_Toc300730121}[]{#_Toc300730358}[]{#_Toc300730554}[]{#_Toc300731456}[]{#_Toc300732192}[]{#_Toc300733076}[]{#_Toc300733350}[]{#_Toc300751172}[]{#_Toc300751366}[]{#_Toc300753478}[]{#_Toc300761951}[]{#_Toc300764392}[]{#_Toc300765512}[]{#_Toc299957998}[]{#_Toc299958449}[]{#_Toc299958681}[]{#_Toc299977237}[]{#_Toc300730122}[]{#_Toc300730359}[]{#_Toc300730555}[]{#_Toc300731457}[]{#_Toc300732193}[]{#_Toc300733077}[]{#_Toc300733351}[]{#_Toc300751173}[]{#_Toc300751367}[]{#_Toc300753479}[]{#_Toc300761952}[]{#_Toc300764393}[]{#_Toc300765513}[]{#_Toc299957999}[]{#_Toc299958450}[]{#_Toc299958682}[]{#_Toc299977238}[]{#_Toc300730123}[]{#_Toc300730360}[]{#_Toc300730556}[]{#_Toc300731458}[]{#_Toc300732194}[]{#_Toc300733078}[]{#_Toc300733352}[]{#_Toc300751174}[]{#_Toc300751368}[]{#_Toc300753480}[]{#_Toc300761953}[]{#_Toc300764394}[]{#_Toc300765514}[]{#_Toc299958000}[]{#_Toc299958451}[]{#_Toc299958683}[]{#_Toc299977239}[]{#_Toc300730124}[]{#_Toc300730361}[]{#_Toc300730557}[]{#_Toc300731459}[]{#_Toc300732195}[]{#_Toc300733079}[]{#_Toc300733353}[]{#_Toc300751175}[]{#_Toc300751369}[]{#_Toc300753481}[]{#_Toc300761954}[]{#_Toc300764395}[]{#_Toc300765515}[]{#_Toc299958001}[]{#_Toc299958452}[]{#_Toc299958684}[]{#_Toc299977240}[]{#_Toc300730125}[]{#_Toc300730362}[]{#_Toc300730558}[]{#_Toc300731460}[]{#_Toc300732196}[]{#_Toc300733080}[]{#_Toc300733354}[]{#_Toc300751176}[]{#_Toc300751370}[]{#_Toc300753482}[]{#_Toc300761955}[]{#_Toc300764396}[]{#_Toc300765516}[]{#_Toc299958002}[]{#_Toc299958453}[]{#_Toc299958685}[]{#_Toc299977241}[]{#_Toc300730126}[]{#_Toc300730363}[]{#_Toc300730559}[]{#_Toc300731461}[]{#_Toc300732197}[]{#_Toc300733081}[]{#_Toc300733355}[]{#_Toc300751177}[]{#_Toc300751371}[]{#_Toc300753483}[]{#_Toc300761956}[]{#_Toc300764397}[]{#_Toc300765517}[]{#_Toc299958003}[]{#_Toc299958454}[]{#_Toc299958686}[]{#_Toc299977242}[]{#_Toc300730127}[]{#_Toc300730364}[]{#_Toc300730560}[]{#_Toc300731462}[]{#_Toc300732198}[]{#_Toc300733082}[]{#_Toc300733356}[]{#_Toc300751178}[]{#_Toc300751372}[]{#_Toc300753484}[]{#_Toc300761957}[]{#_Toc300764398}[]{#_Toc300765518}[]{#_Toc299958004}[]{#_Toc299958455}[]{#_Toc299958687}[]{#_Toc299977243}[]{#_Toc300730128}[]{#_Toc300730365}[]{#_Toc300730561}[]{#_Toc300731463}[]{#_Toc300732199}[]{#_Toc300733083}[]{#_Toc300733357}[]{#_Toc300751179}[]{#_Toc300751373}[]{#_Toc300753485}[]{#_Toc300761958}[]{#_Toc300764399}[]{#_Toc300765519}[]{#_Toc299958005}[]{#_Toc299958456}[]{#_Toc299958688}[]{#_Toc299977244}[]{#_Toc300730129}[]{#_Toc300730366}[]{#_Toc300730562}[]{#_Toc300731464}[]{#_Toc300732200}[]{#_Toc300733084}[]{#_Toc300733358}[]{#_Toc300751180}[]{#_Toc300751374}[]{#_Toc300753486}[]{#_Toc300761959}[]{#_Toc300764400}[]{#_Toc300765520}[]{#_Toc299958006}[]{#_Toc299958457}[]{#_Toc299958689}[]{#_Toc299977245}[]{#_Toc300730130}[]{#_Toc300730367}[]{#_Toc300730563}[]{#_Toc300731465}[]{#_Toc300732201}[]{#_Toc300733085}[]{#_Toc300733359}[]{#_Toc300751181}[]{#_Toc300751375}[]{#_Toc300753487}[]{#_Toc300761960}[]{#_Toc300764401}[]{#_Toc300765521}[]{#_Toc299958007}[]{#_Toc299958458}[]{#_Toc299958690}[]{#_Toc299977246}[]{#_Toc300730131}[]{#_Toc300730368}[]{#_Toc300730564}[]{#_Toc300731466}[]{#_Toc300732202}[]{#_Toc300733086}[]{#_Toc300733360}[]{#_Toc300751182}[]{#_Toc300751376}[]{#_Toc300753488}[]{#_Toc300761961}[]{#_Toc300764402}[]{#_Toc300765522}[]{#_Toc299958008}[]{#_Toc299958459}[]{#_Toc299958691}[]{#_Toc299977247}[]{#_Toc300730132}[]{#_Toc300730369}[]{#_Toc300730565}[]{#_Toc300731467}[]{#_Toc300732203}[]{#_Toc300733087}[]{#_Toc300733361}[]{#_Toc300751183}[]{#_Toc300751377}[]{#_Toc300753489}[]{#_Toc300761962}[]{#_Toc300764403}[]{#_Toc300765523}[]{#_Toc299958009}[]{#_Toc299958460}[]{#_Toc299958692}[]{#_Toc299977248}[]{#_Toc300730133}[]{#_Toc300730370}[]{#_Toc300730566}[]{#_Toc300731468}[]{#_Toc300732204}[]{#_Toc300733088}[]{#_Toc300733362}[]{#_Toc300751184}[]{#_Toc300751378}[]{#_Toc300753490}[]{#_Toc300761963}[]{#_Toc300764404}[]{#_Toc300765524}[]{#_Toc299958010}[]{#_Toc299958461}[]{#_Toc299958693}[]{#_Toc299977249}[]{#_Toc300730134}[]{#_Toc300730371}[]{#_Toc300730567}[]{#_Toc300731469}[]{#_Toc300732205}[]{#_Toc300733089}[]{#_Toc300733363}[]{#_Toc300751185}[]{#_Toc300751379}[]{#_Toc300753491}[]{#_Toc300761964}[]{#_Toc300764405}[]{#_Toc300765525}[]{#_Toc299958011}[]{#_Toc299958462}[]{#_Toc299958694}[]{#_Toc299977250}[]{#_Toc300730135}[]{#_Toc300730372}[]{#_Toc300730568}[]{#_Toc300731470}[]{#_Toc300732206}[]{#_Toc300733090}[]{#_Toc300733364}[]{#_Toc300751186}[]{#_Toc300751380}[]{#_Toc300753492}[]{#_Toc300761965}[]{#_Toc300764406}[]{#_Toc300765526}[]{#_Toc299958012}[]{#_Toc299958463}[]{#_Toc299958695}[]{#_Toc299977251}[]{#_Toc300730136}[]{#_Toc300730373}[]{#_Toc300730569}[]{#_Toc300731471}[]{#_Toc300732207}[]{#_Toc300733091}[]{#_Toc300733365}[]{#_Toc300751187}[]{#_Toc300751381}[]{#_Toc300753493}[]{#_Toc300761966}[]{#_Toc300764407}[]{#_Toc300765527}[]{#_Toc299958013}[]{#_Toc299958464}[]{#_Toc299958696}[]{#_Toc299977252}[]{#_Toc300730137}[]{#_Toc300730374}[]{#_Toc300730570}[]{#_Toc300731472}[]{#_Toc300732208}[]{#_Toc300733092}[]{#_Toc300733366}[]{#_Toc300751188}[]{#_Toc300751382}[]{#_Toc300753494}[]{#_Toc300761967}[]{#_Toc300764408}[]{#_Toc300765528}[]{#_Toc299958014}[]{#_Toc299958465}[]{#_Toc299958697}[]{#_Toc299977253}[]{#_Toc300730138}[]{#_Toc300730375}[]{#_Toc300730571}[]{#_Toc300731473}[]{#_Toc300732209}[]{#_Toc300733093}[]{#_Toc300733367}[]{#_Toc300751189}[]{#_Toc300751383}[]{#_Toc300753495}[]{#_Toc300761968}[]{#_Toc300764409}[]{#_Toc300765529}[]{#_Toc299958015}[]{#_Toc299958466}[]{#_Toc299958698}[]{#_Toc299977254}[]{#_Toc300730139}[]{#_Toc300730376}[]{#_Toc300730572}[]{#_Toc300731474}[]{#_Toc300732210}[]{#_Toc300733094}[]{#_Toc300733368}[]{#_Toc300751190}[]{#_Toc300751384}[]{#_Toc300753496}[]{#_Toc300761969}[]{#_Toc300764410}[]{#_Toc300765530}[]{#_Toc299958016}[]{#_Toc299958467}[]{#_Toc299958699}[]{#_Toc299977255}[]{#_Toc300730140}[]{#_Toc300730377}[]{#_Toc300730573}[]{#_Toc300731475}[]{#_Toc300732211}[]{#_Toc300733095}[]{#_Toc300733369}[]{#_Toc300751191}[]{#_Toc300751385}[]{#_Toc300753497}[]{#_Toc300761970}[]{#_Toc300764411}[]{#_Toc300765531}[]{#_Toc299958017}[]{#_Toc299958468}[]{#_Toc299958700}[]{#_Toc299977256}[]{#_Toc300730141}[]{#_Toc300730378}[]{#_Toc300730574}[]{#_Toc300731476}[]{#_Toc300732212}[]{#_Toc300733096}[]{#_Toc300733370}[]{#_Toc300751192}[]{#_Toc300751386}[]{#_Toc300753498}[]{#_Toc300761971}[]{#_Toc300764412}[]{#_Toc300765532}[]{#_Toc299958018}[]{#_Toc299958469}[]{#_Toc299958701}[]{#_Toc299977257}[]{#_Toc300730142}[]{#_Toc300730379}[]{#_Toc300730575}[]{#_Toc300731477}[]{#_Toc300732213}[]{#_Toc300733097}[]{#_Toc300733371}[]{#_Toc300751193}[]{#_Toc300751387}[]{#_Toc300753499}[]{#_Toc300761972}[]{#_Toc300764413}[]{#_Toc300765533}[]{#_Toc299958022}[]{#_Toc299958473}[]{#_Toc299958705}[]{#_Toc299977261}[]{#_Toc300730146}[]{#_Toc300730383}[]{#_Toc300730579}[]{#_Toc300731481}[]{#_Toc300732217}[]{#_Toc300733101}[]{#_Toc300733375}[]{#_Toc300751197}[]{#_Toc300751391}[]{#_Toc300753503}[]{#_Toc300761976}[]{#_Toc300764417}[]{#_Toc300765537}[]{#_Toc299958023}[]{#_Toc299958474}[]{#_Toc299958706}[]{#_Toc299977262}[]{#_Toc300730147}[]{#_Toc300730384}[]{#_Toc300730580}[]{#_Toc300731482}[]{#_Toc300732218}[]{#_Toc300733102}[]{#_Toc300733376}[]{#_Toc300751198}[]{#_Toc300751392}[]{#_Toc300753504}[]{#_Toc300761977}[]{#_Toc300764418}[]{#_Toc300765538}[]{#_Toc299958024}[]{#_Toc299958475}[]{#_Toc299958707}[]{#_Toc299977263}[]{#_Toc300730148}[]{#_Toc300730385}[]{#_Toc300730581}[]{#_Toc300731483}[]{#_Toc300732219}[]{#_Toc300733103}[]{#_Toc300733377}[]{#_Toc300751199}[]{#_Toc300751393}[]{#_Toc300753505}[]{#_Toc300761978}[]{#_Toc300764419}[]{#_Toc300765539}[]{#_Toc299958029}[]{#_Toc299958480}[]{#_Toc299958712}[]{#_Toc299977268}[]{#_Toc300730153}[]{#_Toc300730390}[]{#_Toc300730586}[]{#_Toc300731488}[]{#_Toc300732224}[]{#_Toc300733108}[]{#_Toc300733382}[]{#_Toc300751204}[]{#_Toc300751398}[]{#_Toc300753510}[]{#_Toc300761983}[]{#_Toc300764424}[]{#_Toc300765544}[]{#_Toc299958033}[]{#_Toc299958484}[]{#_Toc299958716}[]{#_Toc299977272}[]{#_Toc300730157}[]{#_Toc300730394}[]{#_Toc300730590}[]{#_Toc300731492}[]{#_Toc300732228}[]{#_Toc300733112}[]{#_Toc300733386}[]{#_Toc300751208}[]{#_Toc300751402}[]{#_Toc300753514}[]{#_Toc300761987}[]{#_Toc300764428}[]{#_Toc300765548}[]{#_Toc299958034}[]{#_Toc299958485}[]{#_Toc299958717}[]{#_Toc299977273}[]{#_Toc300730158}[]{#_Toc300730395}[]{#_Toc300730591}[]{#_Toc300731493}[]{#_Toc300732229}[]{#_Toc300733113}[]{#_Toc300733387}[]{#_Toc300751209}[]{#_Toc300751403}[]{#_Toc300753515}[]{#_Toc300761988}[]{#_Toc300764429}[]{#_Toc300765549}[]{#_Toc299958040}[]{#_Toc299958491}[]{#_Toc299958723}[]{#_Toc299977279}[]{#_Toc300730164}[]{#_Toc300730401}[]{#_Toc300730597}[]{#_Toc300731499}[]{#_Toc300732235}[]{#_Toc300733119}[]{#_Toc300733393}[]{#_Toc300751215}[]{#_Toc300751409}[]{#_Toc300753521}[]{#_Toc300761994}[]{#_Toc300764435}[]{#_Toc300765555}[]{#_Toc299958045}[]{#_Toc299958496}[]{#_Toc299958728}[]{#_Toc299977284}[]{#_Toc300730169}[]{#_Toc300730406}[]{#_Toc300730602}[]{#_Toc300731504}[]{#_Toc300732240}[]{#_Toc300733124}[]{#_Toc300733398}[]{#_Toc300751220}[]{#_Toc300751414}[]{#_Toc300753526}[]{#_Toc300761999}[]{#_Toc300764440}[]{#_Toc300765560}[]{#_Toc299958049}[]{#_Toc299958500}[]{#_Toc299958732}[]{#_Toc299977288}[]{#_Toc300730173}[]{#_Toc300730410}[]{#_Toc300730606}[]{#_Toc300731508}[]{#_Toc300732244}[]{#_Toc300733128}[]{#_Toc300733402}[]{#_Toc300751224}[]{#_Toc300751418}[]{#_Toc300753530}[]{#_Toc300762003}[]{#_Toc300764444}[]{#_Toc300765564}[]{#_Toc299958050}[]{#_Toc299958501}[]{#_Toc299958733}[]{#_Toc299977289}[]{#_Toc300730174}[]{#_Toc300730411}[]{#_Toc300730607}[]{#_Toc300731509}[]{#_Toc300732245}[]{#_Toc300733129}[]{#_Toc300733403}[]{#_Toc300751225}[]{#_Toc300751419}[]{#_Toc300753531}[]{#_Toc300762004}[]{#_Toc300764445}[]{#_Toc300765565}[]{#_Toc299958051}[]{#_Toc299958502}[]{#_Toc299958734}[]{#_Toc299977290}[]{#_Toc300730175}[]{#_Toc300730412}[]{#_Toc300730608}[]{#_Toc300731510}[]{#_Toc300732246}[]{#_Toc300733130}[]{#_Toc300733404}[]{#_Toc300751226}[]{#_Toc300751420}[]{#_Toc300753532}[]{#_Toc300762005}[]{#_Toc300764446}[]{#_Toc300765566}[]{#_Toc299958059}[]{#_Toc299958510}[]{#_Toc299958742}[]{#_Toc299977298}[]{#_Toc300730183}[]{#_Toc300730420}[]{#_Toc300730616}[]{#_Toc300731518}[]{#_Toc300732254}[]{#_Toc300733138}[]{#_Toc300733412}[]{#_Toc300751234}[]{#_Toc300751428}[]{#_Toc300753540}[]{#_Toc300762013}[]{#_Toc300764454}[]{#_Toc300765574}[]{#_Toc299958060}[]{#_Toc299958511}[]{#_Toc299958743}[]{#_Toc299977299}[]{#_Toc300730184}[]{#_Toc300730421}[]{#_Toc300730617}[]{#_Toc300731519}[]{#_Toc300732255}[]{#_Toc300733139}[]{#_Toc300733413}[]{#_Toc300751235}[]{#_Toc300751429}[]{#_Toc300753541}[]{#_Toc300762014}[]{#_Toc300764455}[]{#_Toc300765575}[]{#_Toc299958085}[]{#_Toc299958536}[]{#_Toc299958768}[]{#_Toc299977324}[]{#_Toc300730209}[]{#_Toc300730446}[]{#_Toc300730642}[]{#_Toc300731544}[]{#_Toc300732280}[]{#_Toc300733164}[]{#_Toc300733438}[]{#_Toc300751260}[]{#_Toc300751454}[]{#_Toc300753566}[]{#_Toc300762039}[]{#_Toc300764480}[]{#_Toc300765600}[]{#_Toc299958086}[]{#_Toc299958537}[]{#_Toc299958769}[]{#_Toc299977325}[]{#_Toc300730210}[]{#_Toc300730447}[]{#_Toc300730643}[]{#_Toc300731545}[]{#_Toc300732281}[]{#_Toc300733165}[]{#_Toc300733439}[]{#_Toc300751261}[]{#_Toc300751455}[]{#_Toc300753567}[]{#_Toc300762040}[]{#_Toc300764481}[]{#_Toc300765601}[]{#_Toc299958087}[]{#_Toc299958538}[]{#_Toc299958770}[]{#_Toc299977326}[]{#_Toc300730211}[]{#_Toc300730448}[]{#_Toc300730644}[]{#_Toc300731546}[]{#_Toc300732282}[]{#_Toc300733166}[]{#_Toc300733440}[]{#_Toc300751262}[]{#_Toc300751456}[]{#_Toc300753568}[]{#_Toc300762041}[]{#_Toc300764482}[]{#_Toc300765602}[]{#_Toc299958094}[]{#_Toc299958545}[]{#_Toc299958777}[]{#_Toc299977333}[]{#_Toc300730218}[]{#_Toc300730455}[]{#_Toc300730651}[]{#_Toc300731553}[]{#_Toc300732289}[]{#_Toc300733173}[]{#_Toc300733447}[]{#_Toc300751269}[]{#_Toc300751463}[]{#_Toc300753575}[]{#_Toc300762048}[]{#_Toc300764489}[]{#_Toc300765609}[]{#_Toc299958097}[]{#_Toc299958548}[]{#_Toc299958780}[]{#_Toc299977336}[]{#_Toc300730221}[]{#_Toc300730458}[]{#_Toc300730654}[]{#_Toc300731556}[]{#_Toc300732292}[]{#_Toc300733176}[]{#_Toc300733450}[]{#_Toc300751272}[]{#_Toc300751466}[]{#_Toc300753578}[]{#_Toc300762051}[]{#_Toc300764492}[]{#_Toc300765612}[]{#_Toc299958100}[]{#_Toc299958551}[]{#_Toc299958783}[]{#_Toc299977339}[]{#_Toc300730224}[]{#_Toc300730461}[]{#_Toc300730657}[]{#_Toc300731559}[]{#_Toc300732295}[]{#_Toc300733179}[]{#_Toc300733453}[]{#_Toc300751275}[]{#_Toc300751469}[]{#_Toc300753581}[]{#_Toc300762054}[]{#_Toc300764495}[]{#_Toc300765615}[]{#_Toc299958101}[]{#_Toc299958552}[]{#_Toc299958784}[]{#_Toc299977340}[]{#_Toc300730225}[]{#_Toc300730462}[]{#_Toc300730658}[]{#_Toc300731560}[]{#_Toc300732296}[]{#_Toc300733180}[]{#_Toc300733454}[]{#_Toc300751276}[]{#_Toc300751470}[]{#_Toc300753582}[]{#_Toc300762055}[]{#_Toc300764496}[]{#_Toc300765616}

**设备管理 \-- 设备管理配置命令 \-- display alarm**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1895074928}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x2000299048}
:::

[ ]{lang="EN-US"}

[**[display alarm]{lang="EN-US"}**]{#struct_0_55199_x9544_1851025258}[命令用来显示设备的告警信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1092345357}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1594144414}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display alarm ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x2137707784}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1944966372}[模式：]{style="font-family:宋体"}

[**[display alarm ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1825143024}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1836286956}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2000233512}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x316955227}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1190736081}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x31309446}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_230466595}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1207590583}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2071405391}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1664121132}[：取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，暂无意义。（集中式设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x2000167976}[：显示指定单板的告警信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_877916666}[：显示指定成员设备的告警信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1980208987}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_253954646}[：显示指定单板的告警信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1547250988}[：显示指定单板]{style="font-family:
宋体"}[/PEX]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_255950378}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_244391816}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1967774430}[显示设备的告警信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display alarm]{lang="EN-US"}]{#struct_0_55199_x9544_2041325018}

[Slot CPU Level   Info]{lang="EN-US"}

[0    0   ERROR   faulty]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display alarm]{lang="EN-US"}]{#struct_0_55199_x9544_72341728}[命令显示信息描述表（集中式设备）]{style="font-family:黑体"}

[]{#table_struct_0_x663263122}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1999578152}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_524230209}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_2143963576}

[[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_55199_x9544_x279920278}[，暂无意义（如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则表示产生告警的元件位于机框上）]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_256409127}

[[告警]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_971815902}[的编号]{style="font-family:宋体"}

[[Level]{lang="EN-US"}]{#struct_0_55199_x9544_x1954610465}

[[告警的级别，级别由高到低依次为]{style="font-family:宋体"}[ERROR]{lang="EN-US"}]{#struct_0_55199_x9544_x914551319}[、]{style="font-family:宋体"}[WARNING]{lang="EN-US"}[、]{style="font-family:宋体"}[NOTICE]{lang="EN-US"}[、]{style="font-family:宋体"}[INFO]{lang="EN-US"}

[[Info]{lang="EN-US"}]{#struct_0_55199_x9544_802053604}

[[告警的详细信息。取值为：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1999512616}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[faulty]{lang="EN-US"}]{#struct_0_55199_x9544_x1361778176}[：表示]{style="font-family:宋体"}[单板处于]{style="font-family:宋体"}[faulty]{lang="EN-US"}[状态（该单板可能正在启动，或者当前处于故障状态）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fan ]{lang="EN-US"}]{#struct_0_55199_x9544_x1007452886}*[n]{lang="EN-US"}*[ is absent]{lang="EN-US"}[：风扇]{lang="EN-US" style="font-family:宋体"}*[n]{lang="EN-US"}*[当前不在位]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x2059324743}[显示设备的告警信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display alarm]{lang="EN-US"}]{#struct_0_55199_x9544_x2000102439}

[Slot CPU Level   Info]{lang="EN-US"}

[2    0   ERROR   faulty]{lang="EN-US"}

[5    0   ERROR   faulty]{lang="EN-US"}

[8    1   ERROR   faulty]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display alarm]{lang="EN-US"}]{#struct_0_55199_x9544_1874054632}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x670615314}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x646641804}

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_473466410}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_370683505}

[[产生告警的单板所在的槽位号（如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_55199_x9544_369778947}["，则表示产生告警的元件位于机框上）（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[产生告警的成员设备的编号（如果显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_55199_x9544_x2000036903}["，则表示产生告警的元件位于机框上）（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_x864660660}

[[告警单板的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_256474663}[编号]{style="font-family:宋体"}

[[Level]{lang="EN-US"}]{#struct_0_55199_x9544_x1217848772}

[[告警的级别，级别由高到低依次为]{style="font-family:宋体"}[ERROR]{lang="EN-US"}]{#struct_0_55199_x9544_x549477303}[、]{style="font-family:宋体"}[WARNING]{lang="EN-US"}[、]{style="font-family:宋体"}[NOTICE]{lang="EN-US"}[、]{style="font-family:宋体"}[INFO]{lang="EN-US"}

[[Info]{lang="EN-US"}]{#struct_0_55199_x9544_x2129343930}

[[告警的详细信息。取值为：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x949893240}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[faulty]{lang="EN-US"}]{#struct_0_55199_x9544_x1361778174}[：表示]{style="font-family:宋体"}[单板处于]{style="font-family:宋体"}[faulty]{lang="EN-US"}[状态（该单板可能正在启动，或者当前处于故障状态）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fan *n* is absent]{lang="EN-US"}]{#struct_0_55199_x9544_976873977}[：]{lang="EN-US" style="font-family:宋体"}[风扇]{lang="EN-US" style="font-family:宋体"}*[n]{lang="EN-US"}*[当前不在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Power *n* is absent]{lang="EN-US"}]{#struct_0_55199_x9544_x1369292466}[：]{lang="EN-US" style="font-family:宋体"}[电源]{lang="EN-US" style="font-family:宋体"}*[n]{lang="EN-US"}*[当前不在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The temperature of sensor *n* exceeds the lower limit]{lang="EN-US"}]{#struct_0_55199_x9544_1809232319}[：]{lang="EN-US" style="font-family:宋体"}[传感器]{lang="EN-US" style="font-family:
  宋体"}*[n]{lang="EN-US"}*[的温度低于低温门限]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The temperature of sensor *n* exceeds the upper limit]{lang="EN-US"}]{#struct_0_55199_x9544_x981058827}[：]{lang="EN-US" style="font-family:宋体"}[传感器]{lang="EN-US" style="font-family:
  宋体"}*[n]{lang="EN-US"}*[的温度高于高温门限]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x20163026}[显示设备当前告警信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display alarm]{lang="EN-US"}]{#struct_0_55199_x9544_x2000364583}

[Chassis  Slot  CPU  Level    Info]{lang="EN-US"}

[1        6     0    ERROR    Fan 2 is absent.]{lang="EN-US"}

[1        6     0    ERROR    Power 2 is absent.]{lang="EN-US"}

[1        6     1    ERROR    The board in slot 10 is faulty.]{lang="EN-US"}

[2        3     1    WARNING  The temperature of sensor 3 exceeds the lower limit.]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display alarm]{lang="EN-US"}]{#struct_0_55199_x9544_344346575}[命令显示信息描述表（分布式设备－]{style="font-family:黑体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:黑体"}

[]{#table_struct_0_x640933938}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1895637494}

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_1046027257}

[[Chassis]{lang="EN-US"}]{#struct_0_55199_x9544_x687932206}

[[告警设备的成员编号]{style="font-family:宋体"}]{#struct_0_55199_x9544_1625447448}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_x2000299047}

[[告警单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_55199_x9544_1447740731}

[[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_256540199}

[[告警单板的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_x1710375840}[编号]{style="font-family:宋体"}

[[Level]{lang="EN-US"}]{#struct_0_55199_x9544_1009664888}

[[告警的级别，级别由高到低依次为]{style="font-family:宋体"}[ERROR]{lang="EN-US"}]{#struct_0_55199_x9544_1187509788}[、]{style="font-family:宋体"}[WARNING]{lang="EN-US"}[、]{style="font-family:宋体"}[NOTICE]{lang="EN-US"}[、]{style="font-family:宋体"}[INFO]{lang="EN-US"}

[[Info]{lang="EN-US"}]{#struct_0_55199_x9544_x2022160742}

[[告警的详细信息。取值为：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1514027862}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fan *n* is absent]{lang="EN-US"}]{#struct_0_55199_x9544_976873980}[：]{lang="EN-US" style="font-family:宋体"}[风扇]{lang="EN-US" style="font-family:宋体"}*[n]{lang="EN-US"}*[当前不在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Power *n* is absent]{lang="EN-US"}]{#struct_0_55199_x9544_976873981}[：]{lang="EN-US" style="font-family:宋体"}[电源]{lang="EN-US" style="font-family:宋体"}*[n]{lang="EN-US"}*[当前不在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The board in slot *n* is faulty]{lang="EN-US"}]{#struct_0_55199_x9544_x1031585452}[：]{style="font-family:宋体"}*[n]{lang="EN-US"}*[号槽位上的单板处于]{lang="EN-US" style="font-family:宋体"}[faulty]{lang="EN-US"}[状态（该单板可能正在启动，或者当前处于故障状态）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The temperature of sensor *n* exceeds the lower limit]{lang="EN-US"}]{#struct_0_55199_x9544_x415250662}[：]{lang="EN-US" style="font-family:宋体"}[传感器]{lang="EN-US" style="font-family:
  宋体"}*[n]{lang="EN-US"}*[的温度低于低温门限]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The temperature of sensor *n* exceeds the upper limit]{lang="EN-US"}]{#struct_0_55199_x9544_x1348611595}[：]{lang="EN-US" style="font-family:宋体"}[传感器]{lang="EN-US" style="font-family:
  宋体"}*[n]{lang="EN-US"}*[的温度高于高温门限]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-999110757 .myid}
[]{#_Toc404783070}[]{#struct_0_55199_x9544_1407617892}[]{#_Toc311570024}

**设备管理 \-- 设备管理配置命令 \-- display bootrom-access**

------------------------------------------------------------------------

[**[display bootrom-access]{lang="EN-US"}**]{#struct_0_55199_x9544_x1999578151}[命令用来显示设备启动过程中用户是否可以进入]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1041853732}

[**[display bootrom-access]{lang="EN-US"}**]{#struct_0_55199_x9544_1210385276}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x186752232}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1806982106}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1946630541}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1206434928}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1489127275}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1999512615}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_2013442163}[显示设备启动过程中用户是否可以进入]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单。]{style="font-family:宋体"}

[[\<Sysname\> display bootrom-access]{lang="EN-US"}]{#struct_0_55199_x9544_x1699999760}

[Bootrom access: Enabled.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x579159560}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bootrom-access enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x289478522}
:::

::::: {#-1649738007 .myid}
[]{#_Toc404783071}[]{#struct_0_55199_x9544_585670676}[]{#_Toc322680645}[]{#_Toc317147093}

**设备管理 \-- 设备管理配置命令 \-- display brand**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 43 width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1493063952}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x434018503}
:::

[ ]{lang="EN-US"}

[**[display brand]{lang="EN-US"}**]{#struct_0_55199_x9544_x110983545}[命令用来显示主控板的品牌标识。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1785957075}

[**[display brand]{lang="EN-US"}**]{#struct_0_55199_x9544_x1165047077}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_101625905}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x820431449}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1634498039}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_922073457}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x433952967}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1456157656}

[**[\# ]{lang="EN-US"}**]{#struct_0_55199_x9544_599688203}[显示设备的品牌标识。]{style="font-family:宋体"}

[[\<Sysname\> display brand]{lang="EN-US"}]{#struct_0_55199_x9544_x1035576052}

[Current BRANDs:]{lang="EN-US"}

[ Slot 0: H3C.]{lang="EN-US"}

[ Slot 1: HP.]{lang="EN-US"}

[ ]{lang="EN-US"}

[New BRANDs:]{lang="EN-US"}

[ Slot 0: HP.]{lang="EN-US"}

[ Slot 1: HP.]{lang="EN-US"}

[[以上显示信息中，]{style="font-family:宋体"}[Current BRANDs]{lang="EN-US"}]{#struct_0_55199_x9544_x1020672421}[表示设备上当前生效的品牌标识；]{style="font-family:宋体"}[New BRANDs]{lang="EN-US"}[表示通过]{style="font-family:宋体"}**[brand]{lang="EN-US"}**[命令修改后的品牌标识，该标识在主控板重启后生效。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_454119671}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[brand]{lang="EN-US"}**]{#struct_0_55199_x9544_x433887431}
:::::

::: {#-796811701 .myid}
[]{#_Toc404783072}[]{#struct_0_55199_x9544_x1908177593}

**设备管理 \-- 设备管理配置命令 \-- display clock**

------------------------------------------------------------------------

[**[display clock]{lang="EN-US"}**]{#struct_0_55199_x9544_439593407}[命令用来显示系统当前的时间、日期、本地时区以及夏令时配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1994189622}

[**[display clock]{lang="EN-US"}**]{#struct_0_55199_x9544_492567758}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_766225152}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1537298784}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1861918107}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x433821895}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1274572419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2069946981}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_202483747}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2033234371}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_770061799}[没有配置本地时区时，显示系统当前日期和时间。]{style="font-family:宋体"}

[[\<Sysname\> display clock]{lang="EN-US"}]{#struct_0_55199_x9544_x782735609}

[10:09:00 UTC Fri 03/16/2012]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_2005502995}[配置了本地时区]{style="font-family:宋体"}[Z5]{lang="EN-US"}[后，显示系统当前日期和时间。]{style="font-family:宋体"}

[[\<Sysname\> display clock]{lang="EN-US"}]{#struct_0_55199_x9544_x434280647}

[15:10:00 Z5 Fri 03/16/2012]{lang="EN-US"}

[Time Zone : Z5 add 05:00:00]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1084547565}[配置了本地时区]{style="font-family:宋体"}[Z5]{lang="EN-US"}[和夏令时]{style="font-family:宋体"}[PDT]{lang="EN-US"}[后，显示系统当前日期和时间。]{style="font-family:宋体"}

[[\<Sysname\> display clock]{lang="EN-US"}]{#struct_0_55199_x9544_940430490}

[15:11:00 Z5 Fri 03/16/2012]{lang="EN-US"}

[Time Zone : Z5 add 05:00:00]{lang="EN-US"}

[Summer Time : PDT 06:00:00 08/01 06:00:00 09/01 01:00:00]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1458563967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock datetime]{lang="EN-US"}**]{#struct_0_55199_x9544_x540570456}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock timezone]{lang="EN-US"}**]{#struct_0_55199_x9544_1931678001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[clock summer-time]{lang="EN-US"}**]{#struct_0_55199_x9544_x434215111}
:::

::: {#1843823702 .myid}
[]{#_Toc404783073}[]{#struct_0_55199_x9544_x1991533847}[]{#_Toc306970100}[]{#_Toc304800170}[]{#_Toc304800158}

**设备管理 \-- 设备管理配置命令 \-- display copyright**

------------------------------------------------------------------------

[[display copyright]{lang="EN-US"}]{#struct_0_55199_x9544_1622891317}[命令用来显示系统软件和硬件的详细版权信息。]{style="font-family:宋体"}[]{#_Toc304800159}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_149137267}[]{#_Toc304800160}

[**[display copyright]{lang="EN-US"}**]{#struct_0_55199_x9544_x2025492583}[]{#_Toc304800161}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1492543375}[]{#_Toc304800162}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1221153895}[]{#_Toc304800163}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2130013813}[]{#_Toc304800164}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1942895010}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x434149575}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1465782856}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x748864346}

[]{#struct_0_55199_x9544_x735625375}[]{#_Toc304800165}[]{#_Toc304800166}[【使用指导】]{style="font-family:
黑体"}

[[通过查看版权信息，可以获知系统当前使用软件和硬件版本的版权信息、版权的参照标准、版权证书等相关信息。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1562076208}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_811715660}[]{#_Toc304800167}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_2137917443}[显示详细的软件版权信息。（本显示信息与设备的型号有关，请以设备的实际情况为准，此处略）]{style="font-family:宋体"}[]{#_Toc304800168}

[[\<Sysname\> display copyright]{lang="EN-US"}]{#struct_0_55199_x9544_x434084039}[]{#_Toc304800169}
:::

::: {#-488040415 .myid}
[]{#_Toc404783074}[]{#struct_0_55199_x9544_x1623519420}

**设备管理 \-- 设备管理配置命令 \-- display cpu-usage**

------------------------------------------------------------------------

[**[display cpu-usage]{lang="EN-US"}**]{#struct_0_55199_x9544_1316485395}[命令用来显示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x784899463}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_759436590}

[**[display cpu-usage]{lang="EN-US"}**]{#struct_0_55199_x9544_x526082922}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1428679083}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display cpu-usage ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x919450343}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1268830881}[模式：]{style="font-family:宋体"}

[**[display cpu-usage ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x433494215}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1484451802}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x864296544}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1958730816}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x878173007}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_237467287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x272952831}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x340595687}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x433428679}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1977190256}[：显示指定单板的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示的是所有单板的相应信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1421948141}[：显示指定成员设备的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示的是所有成员设备的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_817278501}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，显示的是所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1991890837}[：显示指定成员设备指定单板的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x454185891}[：显示指定单板的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1422239834}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的利用率统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_375630982}

[[该命令用于显示最近]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_55199_x9544_749030508}[秒钟、最近]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟、最近]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的平均值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1674142561}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x434018502}[显示当前]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display cpu-usage]{lang="EN-US"}]{#struct_0_55199_x9544_x111049081}

[Unit CPU usage:]{lang="EN-US"}

[       1% in last 5 seconds]{lang="EN-US"}

[       1% in last 1 minute]{lang="EN-US"}

[       1% in last 5 minutes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1048509970}[显示当前]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display cpu-usage]{lang="EN-US"}]{#struct_0_55199_x9544_1034657566}

[Slot 0 CPU 0 CPU usage:]{lang="EN-US"}

[       1% in last 5 seconds]{lang="EN-US"}

[       0% in last 1 minute]{lang="EN-US"}

[       0% in last 5 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 1 CPU 0 CPU usage:]{lang="EN-US"}

[       1% in last 5 seconds]{lang="EN-US"}

[       1% in last 1 minute]{lang="EN-US"}

[       1% in last 5 minutes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x433952966}[显示所有成员设备当前]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display cpu-usage]{lang="EN-US"}]{#struct_0_55199_x9544_x1456223192}

[Slot 1 CPU 0 CPU usage:]{lang="EN-US"}

[       6% in last 5 seconds]{lang="EN-US"}

[      10% in last 1 minute]{lang="EN-US"}

[       5% in last 5 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 2 CPU 0 CPU usage:]{lang="EN-US"}

[       5% in last 5 seconds]{lang="EN-US"}

[       8% in last 1 minute]{lang="EN-US"}

[       5% in last 5 minutes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1489499621}[显示所有单板]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display cpu-usage]{lang="EN-US"}]{#struct_0_55199_x9544_x433887430}

[Chassis 1 Slot 0 CPU 0 CPU usage:]{lang="EN-US"}

[       9% in last 5 seconds]{lang="EN-US"}

[       8% in last 1 minute]{lang="EN-US"}

[       8% in last 5 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 1 Slot 1 CPU 0 CPU usage:]{lang="EN-US"}

[       5% in last 5 seconds]{lang="EN-US"}

[       4% in last 1 minute]{lang="EN-US"}

[       4% in last 5 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 2 Slot 0 CPU 0 CPU usage:]{lang="EN-US"}

[       6% in last 5 seconds]{lang="EN-US"}

[       6% in last 1 minute]{lang="EN-US"}

[       6% in last 5 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 2 Slot 1 CPU 0 CPU usage:]{lang="EN-US"}

[       6% in last 5 seconds]{lang="EN-US"}

[       6% in last 1 minute]{lang="EN-US"}

[       6% in last 5 minutes]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display cpu-usage]{lang="EN-US"}]{#struct_0_55199_x9544_x1908112057}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x644951730}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_321034702}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x962105125}

[[Unit CPU usage]{lang="EN-US"}]{#struct_0_55199_x9544_x433821894}

[[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_1274637955}[利用率信息（集中式设备）]{style="font-family:宋体"}

[[1% in last 5 seconds]{lang="EN-US"}]{#struct_0_55199_x9544_1875278791}

[[设备启动后，会以]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_55199_x9544_174231656}[秒为周期计算并记录一次该]{style="font-family:宋体"}[5]{lang="EN-US"}[秒内的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的平均利用率。该字段显示的是最近一个]{style="font-family:宋体"}[5]{lang="EN-US"}[秒统计周期内]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的平均利用率]{style="font-family:宋体"}

[[1% in last 1 minute]{lang="EN-US"}]{#struct_0_55199_x9544_894928984}

[[设备启动后，会以]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_55199_x9544_1700951824}[分钟为周期计算并记录一次该]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟内的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的平均利用率。该字段显示的是最近一个]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟统计周期内]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的平均利用率]{style="font-family:宋体"}

[[1% in last 5 minutes]{lang="EN-US"}]{#struct_0_55199_x9544_x434280646}

[[设备启动后，会以]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_55199_x9544_1084613101}[分钟为周期计算并记录一次该]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟内的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的平均利用率。该字段显示的是最近一个]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟统计周期内]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的平均利用率]{style="font-family:宋体"}

[[Slot *x* CPU *y* CPU usage]{lang="EN-US"}]{#struct_0_55199_x9544_x2142829931}

[*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x103019736}[号单板上]{style="font-family:宋体"}*[y]{lang="EN-US"}*[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率信息（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[Slot *x* CPU *y* CPU usage]{lang="EN-US"}]{#struct_0_55199_x9544_1419381234}

[*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_288067760}[号成员设备上]{style="font-family:宋体"}*[y]{lang="EN-US"}*[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis *x* Slot *y* CPU *z* CPU usage]{lang="EN-US"}]{#struct_0_55199_x9544_x434215110}

[*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x1991599383}[号成员设备]{style="font-family:宋体"}*[y]{lang="EN-US"}*[号单板上]{style="font-family:宋体"}*[z]{lang="EN-US"}*[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#436327185 .myid}
[]{#_Toc404783075}[]{#struct_0_55199_x9544_x1006202632}[]{#_Toc358900717}[]{#_Toc340215444}

**设备管理 \-- 设备管理配置命令 \-- display cpu-usage configuration**

------------------------------------------------------------------------

[**[display cpu-usage configuration]{lang="EN-US"}**]{#struct_0_55199_x9544_1054115853}[命令用来显示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率历史信息记录功能相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1561272848}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1351339109}

[**[display cpu-usage configuration]{lang="EN-US"}**]{#struct_0_55199_x9544_x1006202631}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1457400380}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display cpu-usage configuration]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1225251691}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_716255382}[模式：]{style="font-family:宋体"}

[**[display cpu-usage configuration]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1006202630}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x108683561}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x525959925}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x783869135}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1006202629}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1813565204}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1508991571}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_346986338}[：表示单板所在的槽位号。不指定该参数时，显示的是主用主控板上的相应信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1850890325}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示的是主设备上的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x748805440}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，显示的是主设备上的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1006202628}[：表示指定成员设备上的指定单板。不指定该参数时，显示的是全局主用主控板上的相应信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1980077915}[：表示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，显示的是全局主用主控板上的相应信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_247481263}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1705775287}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1260546711}[显示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率历史信息记录功能相关配置。]{style="font-family:宋体"}

[[\<Sysname\> display cpu-usage configuration]{lang="EN-US"}]{#struct_0_55199_x9544_x1006202627}

[CPU usage monitor is enabled.]{lang="EN-US"}

[Current monitor interval is 60 seconds.]{lang="EN-US"}

[Current monitor threshold is 90%.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_294535430}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor cpu-usage enable]{lang="EN-US"}**]{#struct_0_55199_x9544_500524102}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor cpu-usage interval]{lang="EN-US"}**]{#struct_0_55199_x9544_x803764287}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor cpu-usage]{lang="EN-US"}**]{#struct_0_55199_x9544_940996906}**[ threshold]{lang="EN-US"}**
:::

::: {#1317015418 .myid}
[]{#_Toc404783076}[]{#struct_0_55199_x9544_1667312474}[]{#_Toc300730506}[]{#_Toc300730269}[]{#_Toc267485909}[]{#_Toc267468508}[]{#_Toc267468912}[]{#_Toc267485911}[]{#_Toc267468509}[]{#_Toc267468913}[]{#_Toc267485912}[]{#_Toc267468510}[]{#_Toc267468914}[]{#_Toc267485913}[]{#_Toc267468511}[]{#_Toc267468915}[]{#_Toc267485914}[]{#_Toc267468512}[]{#_Toc267468916}[]{#_Toc267485915}[]{#_Toc267468513}[]{#_Toc267468917}[]{#_Toc267485916}[]{#_Toc267468514}[]{#_Toc267468918}[]{#_Toc267485917}[]{#_Toc267468515}[]{#_Toc267468919}[]{#_Toc267485918}[]{#_Toc267468516}[]{#_Toc267468920}[]{#_Toc267485919}[]{#_Toc267468517}[]{#_Toc267468921}[]{#_Toc267485920}[]{#_Toc267468518}[]{#_Toc267468922}[]{#_Toc267485921}[]{#_Toc267468519}[]{#_Toc267468923}[]{#_Toc267485922}[]{#_Toc267468520}[]{#_Toc267468924}[]{#_Toc267485923}[]{#_Toc267468521}[]{#_Toc267468925}[]{#_Toc267485924}[]{#_Toc267468522}[]{#_Toc267468926}[]{#_Toc267485925}[]{#_Toc267468523}[]{#_Toc267468927}[]{#_Toc267485926}[]{#_Toc267468524}[]{#_Toc267468928}[]{#_Toc267485927}[]{#_Toc267468525}[]{#_Toc267468929}[]{#_Toc267485928}[]{#_Toc267468526}[]{#_Toc267468930}[]{#_Toc267485929}[]{#_Toc267468527}[]{#_Toc267468931}[]{#_Toc267485930}[]{#_Toc267468528}[]{#_Toc267468932}[]{#_Toc267485931}[]{#_Toc267468529}[]{#_Toc267468933}[]{#_Toc267485932}[]{#_Toc267468530}[]{#_Toc267468934}[]{#_Toc267485933}[]{#_Toc267468531}[]{#_Toc267468935}[]{#_Toc267485934}[]{#_Toc267468532}[]{#_Toc267468936}[]{#_Toc267485935}[]{#_Toc267468533}[]{#_Toc267468937}[]{#_Toc267485936}[]{#_Toc267468534}[]{#_Toc267468938}[]{#_Toc267485937}[]{#_Toc267468535}[]{#_Toc267468939}[]{#_Toc267485938}[]{#_Toc267468536}[]{#_Toc267468940}[]{#_Toc267485939}[]{#_Toc267468537}[]{#_Toc267468941}[]{#_Toc267485940}[]{#_Toc267468538}[]{#_Toc267468942}[]{#_Toc267485941}[]{#_Toc267468552}[]{#_Toc267468956}[]{#_Toc267485955}[]{#_Toc267468553}[]{#_Toc267468957}[]{#_Toc267485956}[]{#_Toc267468561}[]{#_Toc267468965}[]{#_Toc267485964}[]{#_Toc267468562}[]{#_Toc267468966}[]{#_Toc267485965}[]{#_Toc267468569}[]{#_Toc267468973}[]{#_Toc267485972}[]{#_Toc267468571}[]{#_Toc267468975}[]{#_Toc267485974}[]{#_Toc267468572}[]{#_Toc267468976}[]{#_Toc267485975}[]{#_Toc267468573}[]{#_Toc267468977}[]{#_Toc267485976}[]{#_Toc267468574}[]{#_Toc267468978}[]{#_Toc267485977}[]{#_Toc267468575}[]{#_Toc267468979}[]{#_Toc267485978}[]{#_Toc267468576}[]{#_Toc267468980}[]{#_Toc267485979}[]{#_Toc267468577}[]{#_Toc267468981}[]{#_Toc267485980}[]{#_Toc267468578}[]{#_Toc267468982}[]{#_Toc267485981}[]{#_Toc267468579}[]{#_Toc267468983}[]{#_Toc267485982}[]{#_Toc267468580}[]{#_Toc267468984}[]{#_Toc267485983}[]{#_Toc267468581}[]{#_Toc267468985}[]{#_Toc267485984}[]{#_Toc267468582}[]{#_Toc267468986}[]{#_Toc267485985}[]{#_Toc267468583}[]{#_Toc267468987}[]{#_Toc267485986}[]{#_Toc267468584}[]{#_Toc267468988}[]{#_Toc267485987}[]{#_Toc267468585}[]{#_Toc267468989}[]{#_Toc267485988}[]{#_Toc267468586}[]{#_Toc267468990}[]{#_Toc267485989}[]{#_Toc267468587}[]{#_Toc267468991}[]{#_Toc267485990}[]{#_Toc267468588}[]{#_Toc267468992}[]{#_Toc267485991}[]{#_Toc267468589}[]{#_Toc267468993}[]{#_Toc267485992}[]{#_Toc267468590}[]{#_Toc267468994}[]{#_Toc267485993}[]{#_Toc267468591}[]{#_Toc267468995}[]{#_Toc267485994}[]{#_Toc267468592}[]{#_Toc267468996}[]{#_Toc267485995}[]{#_Toc262215909}[]{#_Toc262473441}[]{#_Toc262215910}[]{#_Toc262473442}[]{#_Toc262215911}[]{#_Toc262473443}[]{#_Toc262215912}[]{#_Toc262473444}[]{#_Toc262215913}[]{#_Toc262473445}[]{#_Toc262215914}[]{#_Toc262473446}[]{#_Toc262215915}[]{#_Toc262473447}[]{#_Toc262215916}[]{#_Toc262473448}[]{#_Toc262215917}[]{#_Toc262473449}[]{#_Toc262215918}[]{#_Toc262473450}[]{#_Toc262215919}[]{#_Toc262473451}[]{#_Toc262215920}[]{#_Toc262473452}[]{#_Toc262215921}[]{#_Toc262473453}[]{#_Toc262215922}[]{#_Toc262473454}[]{#_Toc262215923}[]{#_Toc262473455}[]{#_Toc262215924}[]{#_Toc262473456}[]{#_Toc262215925}[]{#_Toc262473457}[]{#_Toc262215926}[]{#_Toc262473458}[]{#_Toc262215927}[]{#_Toc262473459}[]{#_Toc262215928}[]{#_Toc262473460}[]{#_Toc262215929}[]{#_Toc262473461}[]{#_Toc262215930}[]{#_Toc262473462}[]{#_Toc262215931}[]{#_Toc262473463}[]{#_Toc262215932}[]{#_Toc262473464}[]{#_Toc262215933}[]{#_Toc262473465}[]{#_Toc262215934}[]{#_Toc262473466}[]{#_Toc262215935}[]{#_Toc262473467}[]{#_Toc262215936}[]{#_Toc262473468}[]{#_Toc262215937}[]{#_Toc262473469}[]{#_Toc262215938}[]{#_Toc262473470}[]{#_Toc262215939}[]{#_Toc262473471}[]{#_Toc262215940}[]{#_Toc262473472}[]{#_Toc262215941}[]{#_Toc262473473}[]{#_Toc262215942}[]{#_Toc262473474}[]{#_Toc262215943}[]{#_Toc262473475}[]{#_Toc262215944}[]{#_Toc262473476}[]{#_Toc262215945}[]{#_Toc262473477}[]{#_Toc262215946}[]{#_Toc262473478}[]{#_Toc262215947}[]{#_Toc262473479}[]{#_Toc262215948}[]{#_Toc262473480}[]{#_Toc262215949}[]{#_Toc262473481}[]{#_Toc262215950}[]{#_Toc262473482}[]{#_Toc262215951}[]{#_Toc262473483}[]{#_Toc262215952}[]{#_Toc262473484}[]{#_Toc262215953}[]{#_Toc262473485}[]{#_Toc262215954}[]{#_Toc262473486}[]{#_Toc262215955}[]{#_Toc262473487}[]{#_Toc262215956}[]{#_Toc262473488}[]{#_Toc262215957}[]{#_Toc262473489}[]{#_Toc262215958}[]{#_Toc262473490}[]{#_Toc262215959}[]{#_Toc262473491}[]{#_Toc262215960}[]{#_Toc262473492}[]{#_Toc262215961}[]{#_Toc262473493}[]{#_Toc262215962}[]{#_Toc262473494}[]{#_Toc262215963}[]{#_Toc262473495}[]{#_Toc262215964}[]{#_Toc262473496}[]{#_Toc262215965}[]{#_Toc262473497}[]{#_Toc262215966}[]{#_Toc262473498}[]{#_Toc262215969}[]{#_Toc262473501}[]{#_Toc262215970}[]{#_Toc262473502}[]{#_Toc262215971}[]{#_Toc262473503}[]{#_Toc262215974}[]{#_Toc262473506}[]{#_Toc262215975}[]{#_Toc262473507}[]{#_Toc262215976}[]{#_Toc262473508}[]{#_Toc262215978}[]{#_Toc262473510}[]{#_Toc262215979}[]{#_Toc262473511}[]{#_Toc262215980}[]{#_Toc262473512}[]{#_Toc262215982}[]{#_Toc262473514}[]{#_Toc262215983}[]{#_Toc262473515}[]{#_Toc262215986}[]{#_Toc262473518}[]{#_Toc262215987}[]{#_Toc262473519}[]{#_Toc262215988}[]{#_Toc262473520}[]{#_Toc262215991}[]{#_Toc262473523}[]{#_Toc262215992}[]{#_Toc262473524}[]{#_Toc262215995}[]{#_Toc262473527}[]{#_Toc262215996}[]{#_Toc262473528}[]{#_Toc262215999}[]{#_Toc262473531}[]{#_Toc218401284}[]{#_Toc209953938}[]{#_Toc211937215}[]{#_Toc211937695}[]{#_Toc213494843}[]{#_Toc262216001}[]{#_Toc262473533}[]{#_Toc262216002}[]{#_Toc262473534}[]{#_Toc262216003}[]{#_Toc262473535}[]{#_Toc262216004}[]{#_Toc262473536}[]{#_Toc262216006}[]{#_Toc262473538}[]{#_Toc262216007}[]{#_Toc262473539}[]{#_Toc262216008}[]{#_Toc262473540}[]{#_Toc262216009}[]{#_Toc262473541}[]{#_Toc262216010}[]{#_Toc262473542}[]{#_Toc262216011}[]{#_Toc262473543}[]{#_Toc262216012}[]{#_Toc262473544}[]{#_Toc262216013}[]{#_Toc262473545}[]{#_Toc262216014}[]{#_Toc262473546}[]{#_Toc262216015}[]{#_Toc262473547}[]{#_Toc262216016}[]{#_Toc262473548}[]{#_Toc262216017}[]{#_Toc262473549}[]{#_Toc262216018}[]{#_Toc262473550}[]{#_Toc262216019}[]{#_Toc262473551}[]{#_Toc262216020}[]{#_Toc262473552}[]{#_Toc262216021}[]{#_Toc262473553}[]{#_Toc262216022}[]{#_Toc262473554}[]{#_Toc262216023}[]{#_Toc262473555}[]{#_Toc262216024}[]{#_Toc262473556}[]{#_Toc262216025}[]{#_Toc262473557}[]{#_Toc262216026}[]{#_Toc262473558}[]{#_Toc262216027}[]{#_Toc262473559}[]{#_Toc262216028}[]{#_Toc262473560}[]{#_Toc262216029}[]{#_Toc262473561}[]{#_Toc262216030}[]{#_Toc262473562}[]{#_Toc262216031}[]{#_Toc262473563}[]{#_Toc262216032}[]{#_Toc262473564}[]{#_Toc262216033}[]{#_Toc262473565}[]{#_Toc262216034}[]{#_Toc262473566}[]{#_Toc262216035}[]{#_Toc262473567}[]{#_Toc262216036}[]{#_Toc262473568}[]{#_Toc262216039}[]{#_Toc262473571}[]{#_Toc262216040}[]{#_Toc262473572}[]{#_Toc262216041}[]{#_Toc262473573}[]{#_Toc262216042}[]{#_Toc262473574}[]{#_Toc262216046}[]{#_Toc262473578}[]{#_Toc262216049}[]{#_Toc262473581}[]{#_Toc262216051}[]{#_Toc262473583}[]{#_Toc262216052}[]{#_Toc262473584}[]{#_Toc262216054}[]{#_Toc262473586}[]{#_Toc262216055}[]{#_Toc262473587}[]{#_Toc262216056}[]{#_Toc262473588}[]{#_Toc262216057}[]{#_Toc262473589}[]{#_Toc262216058}[]{#_Toc262473590}[]{#_Toc262216059}[]{#_Toc262473591}[]{#_Toc262216060}[]{#_Toc262473592}[]{#_Toc262216061}[]{#_Toc262473593}[]{#_Toc262216062}[]{#_Toc262473594}[]{#_Toc262216063}[]{#_Toc262473595}[]{#_Toc262216064}[]{#_Toc262473596}[]{#_Toc262216065}[]{#_Toc262473597}[]{#_Toc262216066}[]{#_Toc262473598}[]{#_Toc262216067}[]{#_Toc262473599}[]{#_Toc262216070}[]{#_Toc262473602}[]{#_Toc262216071}[]{#_Toc262473603}[]{#_Toc262216073}[]{#_Toc262473605}[]{#_Toc262216075}[]{#_Toc262473607}[]{#_Toc262216077}[]{#_Toc262473609}[]{#_Toc262216078}[]{#_Toc262473610}[]{#_Toc262216079}[]{#_Toc262473611}[]{#_Toc262216080}[]{#_Toc262473612}[]{#_Toc262216081}[]{#_Toc262473613}[]{#_Toc262216082}[]{#_Toc262473614}[]{#_Toc262216083}[]{#_Toc262473615}[]{#_Toc262216084}[]{#_Toc262473616}[]{#_Toc262216085}[]{#_Toc262473617}[]{#_Toc262216086}[]{#_Toc262473618}[]{#_Toc262216087}[]{#_Toc262473619}[]{#_Toc262216088}[]{#_Toc262473620}[]{#_Toc262216089}[]{#_Toc262473621}[]{#_Toc262216090}[]{#_Toc262473622}[]{#_Toc262216091}[]{#_Toc262473623}[]{#_Toc262216092}[]{#_Toc262473624}[]{#_Toc262216093}[]{#_Toc262473625}[]{#_Toc262216094}[]{#_Toc262473626}[]{#_Toc262216095}[]{#_Toc262473627}[]{#_Toc262216096}[]{#_Toc262473628}[]{#_Toc262216097}[]{#_Toc262473629}[]{#_Toc262216098}[]{#_Toc262473630}[]{#_Toc262216099}[]{#_Toc262473631}[]{#_Toc262216100}[]{#_Toc262473632}[]{#_Toc262216101}[]{#_Toc262473633}[]{#_Toc262216102}[]{#_Toc262473634}[]{#_Toc262216103}[]{#_Toc262473635}[]{#_Toc262216104}[]{#_Toc262473636}[]{#_Toc262216105}[]{#_Toc262473637}[]{#_Toc262216106}[]{#_Toc262473638}[]{#_Toc262216107}[]{#_Toc262473639}[]{#_Toc262216108}[]{#_Toc262473640}[]{#_Toc262216109}[]{#_Toc262473641}[]{#_Toc262216110}[]{#_Toc262473642}[]{#_Toc262216111}[]{#_Toc262473643}[]{#_Toc262216112}[]{#_Toc262473644}[]{#_Toc262216113}[]{#_Toc262473645}[]{#_Toc262216114}[]{#_Toc262473646}[]{#_Toc262216115}[]{#_Toc262473647}[]{#_Toc262216116}[]{#_Toc262473648}[]{#_Toc262216117}[]{#_Toc262473649}[]{#_Toc262216126}[]{#_Toc262473658}[]{#_Toc262216137}[]{#_Toc262473669}[]{#_Toc262216147}[]{#_Toc262473679}[]{#_Toc262216148}[]{#_Toc262473680}[]{#_Toc262216152}[]{#_Toc262473684}[]{#_Toc262216160}[]{#_Toc262473692}[]{#_Toc262216161}[]{#_Toc262473693}[]{#_Toc262216165}[]{#_Toc262473697}[]{#_Toc262216172}[]{#_Toc262473704}[]{#_Toc262216173}[]{#_Toc262473705}[]{#_Toc262216174}[]{#_Toc262473706}[]{#_Toc262216178}[]{#_Toc262473710}[]{#_Toc262216179}[]{#_Toc262473711}[]{#_Toc262216180}[]{#_Toc262473712}[]{#_Toc262216184}[]{#_Toc262473716}[]{#_Toc262216185}[]{#_Toc262473717}[]{#_Toc262216186}[]{#_Toc262473718}[]{#_Toc262216190}[]{#_Toc262473722}[]{#_Toc262216191}[]{#_Toc262473723}[]{#_Toc262216192}[]{#_Toc262473724}[]{#_Toc262216196}[]{#_Toc262473728}[]{#_Toc262216197}[]{#_Toc262473729}[]{#_Toc262216200}[]{#_Toc262473732}[]{#_Toc262216201}[]{#_Toc262473733}[]{#_Toc262216203}[]{#_Toc262473735}[]{#_Toc262216204}[]{#_Toc262473736}[]{#_Toc262216208}[]{#_Toc262473740}[]{#_Toc262216209}[]{#_Toc262473741}[]{#_Toc262216213}[]{#_Toc262473745}[]{#_Toc262216214}[]{#_Toc262473746}[]{#_Toc262216215}[]{#_Toc262473747}[]{#_Toc262216219}[]{#_Toc262473751}[]{#_Toc262216220}[]{#_Toc262473752}[]{#_Toc182048949}[]{#_Toc182120798}[]{#_Toc130782577}[]{#_Toc130786976}[]{#_Toc130782581}[]{#_Toc130786980}[]{#_Toc262216221}[]{#_Toc262473753}[]{#_Toc262216222}[]{#_Toc262473754}[]{#_Toc262216225}[]{#_Toc262473757}[]{#_Toc262216226}[]{#_Toc262473758}[]{#_Toc262216227}[]{#_Toc262473759}[]{#_Toc262216228}[]{#_Toc262473760}[]{#_Toc262216229}[]{#_Toc262473761}[]{#_Toc262216230}[]{#_Toc262473762}[]{#_Toc262216231}[]{#_Toc262473763}[]{#_Toc262216232}[]{#_Toc262473764}[]{#_Toc262216233}[]{#_Toc262473765}[]{#_Toc262216234}[]{#_Toc262473766}[]{#_Toc262216235}[]{#_Toc262473767}[]{#_Toc262216236}[]{#_Toc262473768}[]{#_Toc262216237}[]{#_Toc262473769}[]{#_Toc262216238}[]{#_Toc262473770}[]{#_Toc262216239}[]{#_Toc262473771}[]{#_Toc262216240}[]{#_Toc262473772}

**设备管理 \-- 设备管理配置命令 \-- display cpu-usage history**

------------------------------------------------------------------------

[**[display cpu-usage history]{lang="EN-US"}**]{#struct_0_55199_x9544_162544933}[命令用来以图表方式显示]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[利用率的历史信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1197886673}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_393756896}

[**[display cpu-usage history]{lang="EN-US"}**[ \[ **job** *job-id* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1894953428}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x434149574}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display cpu-usage history ]{lang="EN-US"}**[\[ **job** *job-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1465848392}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1632611827}[模式：]{style="font-family:宋体"}

[**[display cpu-usage history ]{lang="EN-US"}**[\[ **job** *job-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_350134331}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x641423766}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1905288008}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_630819511}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x715961078}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x434084038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1623453884}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_320362511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1214356816}

[**[job]{lang="EN-US"}**[ *job-id*]{lang="EN-US"}]{#struct_0_55199_x9544_1370870506}[：显示指定进程的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的历史信息，]{style="font-family:宋体"}*[job-id]{lang="EN-US"}*[表示进程的编号。不指定该参数时，显示的是整个系统的相应信息（整个系统的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率等于所有进程]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率之和）。可以使用]{style="font-family:宋体"}**[display process]{lang="EN-US"}**[命令可以查看当前运行的进程的编号和名称，]{style="font-family:宋体"}**[display process]{lang="EN-US"}**[命令的详细介绍请参见"网络管理与监控"中的"系统维护与调试"。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1131361279}[：显示指定单板的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的历史信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。当不指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[和该参数时，显示的是所有单板上所有进程的相应信息；当指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[参数，但不指定该参数时，显示的是主用主控板上指定进程的相应信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1300914014}[：显示指定成员设备的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的历史信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。当不指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[和该参数时，显示的是所有成员设备上所有进程的相应信息；当指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[参数，但不指定该参数时，显示的是主设备上指定进程的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_461048141}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，显示的是所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_150536537}[：显示指定成员设备上指定单板的]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[利用率的历史信息。]{style="font-family:
宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。当不指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[和该参数时，显示的是所有单板上所有进程的相应信息；当指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[参数，但不指定该参数时，显示的是全局主用主控板上指定进程的相应信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1111260169}[：显示指定单板的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的统计信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x433494214}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的利用率的历史信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。当不指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[和该参数时，表示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。当指定]{style="font-family:宋体"}**[job]{lang="EN-US"}**[参数，但不指定该参数时，表示默认]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1484517338}

[[开启]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_174671331}[利用率历史记录功能后，系统每隔一定时间（可通过]{style="font-family:宋体"}**[monitor cpu-usage interval]{lang="EN-US"}**[命令配置）会对]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的利用率进行采样，并把采样结果保存到历史记录区。通过]{style="font-family:宋体"}**[display cpu-usage history]{lang="EN-US"}**[命令可以查看到最近]{style="font-family:宋体"}[60]{lang="EN-US"}[个采样点的值。结果以坐标的形式进行显示，显示信息中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[纵坐标表示利用率，采用就近显示的原则。比如，利用率的间隔为]{style="font-family:宋体"}]{#struct_0_55199_x9544_x957952296}[5]{lang="EN-US"}[％，则实际统计值]{style="font-family:宋体"}[53]{lang="EN-US"}[％将被显示成]{style="font-family:宋体"}[55]{lang="EN-US"}[％，实际统计值]{style="font-family:宋体"}[52]{lang="EN-US"}[％将被显示成]{style="font-family:宋体"}[50]{lang="EN-US"}[％。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[横坐标表示时间，时间越靠左表示距离当前时间越近。]{style="font-family:宋体"}]{#struct_0_55199_x9544_517081537}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用连续的]{style="font-family:宋体"}]{#struct_0_55199_x9544_1249476713}[\#]{lang="EN-US"}[号表示该时刻的利用率，某个时间点上最高处的]{style="font-family:宋体"}[\#]{lang="EN-US"}[号对应的纵坐标值即为该时刻]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的利用率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x987986001}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_766979717}[以图表方式显示整个系统的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的历史记录。]{style="font-family:宋体"}

[[\<Sysname\> display cpu-usage history]{lang="EN-US"}]{#struct_0_55199_x9544_x434018501}

[100%\|]{lang="EN-US"}

[ 95%\|]{lang="EN-US"}

[ 90%\|]{lang="EN-US"}

[ 85%\|]{lang="EN-US"}

[ 80%\|]{lang="EN-US"}

[ 75%\|]{lang="EN-US"}

[ 70%\|]{lang="EN-US"}

[ 65%\|]{lang="EN-US"}

[ 60%\|]{lang="EN-US"}

[ 55%\|]{lang="EN-US"}

[ 50%\|]{lang="EN-US"}

[ 45%\|]{lang="EN-US"}

[ 40%\|]{lang="EN-US"}

[ 35%\|]{lang="EN-US"}

[ 30%\|]{lang="EN-US"}

[ 25%\|]{lang="EN-US"}

[ 20%\|]{lang="EN-US"}

[ 15%\|             \#]{lang="EN-US"}

[ 10%\|            ###  \#]{lang="EN-US"}

[  5%\|           \########]{lang="EN-US"}

[     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[              10        20        30        40        50        60  (minutes)]{lang="EN-US"}

[                      cpu-usage (Chassis 1 slot 0 CPU 0) last 60 minutes (SYSTEM)]{lang="EN-US"}

[[以上显示信息表明系统（用"]{style="font-family:宋体"}[SYSTEM]{lang="EN-US"}]{#struct_0_55199_x9544_x111114617}["表示，运行在]{style="font-family:宋体"}[Chassis 1 slot 0 CPU 0]{lang="EN-US"}[上）在最近]{style="font-family:宋体"}[60]{lang="EN-US"}[分钟内]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的利用率情况：]{style="font-family:宋体"}[12]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[5]{lang="EN-US"}[％，]{style="font-family:宋体"}[13]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[10]{lang="EN-US"}[％，]{style="font-family:宋体"}[14]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[15]{lang="EN-US"}[％，]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[10]{lang="EN-US"}[％，]{style="font-family:宋体"}[16]{lang="EN-US"}[、]{style="font-family:宋体"}[17]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[5]{lang="EN-US"}[％，]{style="font-family:宋体"}[18]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[10]{lang="EN-US"}[％，]{style="font-family:宋体"}[19]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[5]{lang="EN-US"}[％，其它时间均小于或等于]{style="font-family:宋体"}[2]{lang="EN-US"}[％。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1025006457}[以图表方式显示编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的进程的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率的历史记录。]{style="font-family:宋体"}

[[\<Sysname\> display cpu-usage history job 1]{lang="EN-US"}]{#struct_0_55199_x9544_x433952965}

[100%\|]{lang="EN-US"}

[ 95%\|]{lang="EN-US"}

[ 90%\|]{lang="EN-US"}

[ 85%\|]{lang="EN-US"}

[ 80%\|]{lang="EN-US"}

[ 75%\|]{lang="EN-US"}

[ 70%\|]{lang="EN-US"}

[ 65%\|]{lang="EN-US"}

[ 60%\|]{lang="EN-US"}

[ 55%\|]{lang="EN-US"}

[ 50%\|]{lang="EN-US"}

[ 45%\|]{lang="EN-US"}

[ 40%\|]{lang="EN-US"}

[ 35%\|]{lang="EN-US"}

[ 30%\|]{lang="EN-US"}

[ 25%\|]{lang="EN-US"}

[ 20%\|]{lang="EN-US"}

[ 15%\|]{lang="EN-US"}

[ 10%\|]{lang="EN-US"}

[  5%\|                   \#]{lang="EN-US"}

[     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[              10        20        30        40        50        60  (minutes)]{lang="EN-US"}

[                      cpu-usage (Chassis 1 slot 0 CPU 0) last 60 minutes (scmd)]{lang="EN-US"}

[[以上显示信息表明]{style="font-family:宋体"}[Chassis 1 slot 0 CPU 0]{lang="EN-US"}]{#struct_0_55199_x9544_x1456288728}[上编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的进程（进程名为]{style="font-family:宋体"}[scmd]{lang="EN-US"}[，如果进程名带有"]{style="font-family:宋体"}[\[\]]{lang="EN-US"}["标识则表示它是内核线程）在最近]{style="font-family:宋体"}[60]{lang="EN-US"}[分钟内]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的利用率情况：]{style="font-family:宋体"}[20]{lang="EN-US"}[分钟前大约为]{style="font-family:宋体"}[5]{lang="EN-US"}[％，其它时间均小于或等于]{style="font-family:宋体"}[2]{lang="EN-US"}[％。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x243691273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor cpu-usage enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x243691272}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}]{.TerminalDisplayChar}**[monitor cpu-usage interval]{lang="EN-US"}**]{#struct_0_55199_x9544_2126022188}
:::

::: {#-1507686845 .myid}
[]{#_Toc404783077}[]{#struct_0_55199_x9544_1772670893}[]{#_Toc300730507}[]{#_Toc300730270}[]{#_Toc263066878}[]{#_Toc206560265}

**设备管理 \-- 设备管理配置命令 \-- display device**

------------------------------------------------------------------------

[**[display device]{lang="EN-US"}**]{#struct_0_55199_x9544_x2005191475}[命令用来显示设备信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1532997434}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x134498781}

[**[display device ]{lang="EN-US"}**[\[ **cf-card** \| **flash** \| **harddisk** \| **usb** \] \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number* \| **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x433887429}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x1908701880}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display device ]{lang="EN-US"}**[\[ **cf-card** \| **flash** \| **harddisk** \| **usb**\] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **subslot** m*subslot-number* \] \| **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x2074204574}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1472151749}[模式：]{style="font-family:宋体"}

[**[display device ]{lang="EN-US"}**[\[ **cf-card** \| **flash** \| **harddisk** \| **usb** \] \[ **chassis** *chassis-number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number* \] \] \| **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x872562607}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1444146070}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x44791784}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_960613032}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x433821893}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1274965635}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_278761904}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1030503161}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1248692493}

[**[cf-card]{lang="EN-US"}**]{#struct_0_55199_x9544_x1798284699}[：显示]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[flash]{lang="EN-US"}**]{#struct_0_55199_x9544_x502164028}[：显示]{style="font-family:宋体"}[Flash]{lang="EN-US"}[的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[harddisk]{lang="EN-US"}**]{#struct_0_55199_x9544_x606277396}[：显示硬盘的信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[usb]{lang="EN-US"}**]{#struct_0_55199_x9544_x502164027}[：显示]{style="font-family:宋体"}[USB]{lang="EN-US"}[接口的信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x434280645}[：显示指定成员设备的详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。该参数仅在分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式上有效，其它设备上暂无实际意义。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1084678637}[：显示指定单板的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1739861419}[：显示指定成员设备的单板的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1152155503}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的单板的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1980504776}[：显示指定单板的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1600951987}[：显示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot]{lang="EN-US"}**[ *subslot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_203544358}[：显示指定子卡的信息。]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示子卡所在的子槽位号。不指定该参数时，不会显示子卡的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_55199_x9544_x1356104271}[：显示设备的详细信息。不指定该参数时，显示设备的简要信息，且此时不会显示防火墙插卡的信息。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_256409128}[：显示单板指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x972245468}

[[不带]{style="font-family:宋体"}**[cf-card]{lang="EN-US"}**]{#struct_0_55199_x9544_x710058072}[、]{style="font-family:宋体"}**[flash]{lang="EN-US"}**[、]{style="font-family:宋体"}**[harddisk]{lang="EN-US"}**[和]{style="font-family:宋体"}**[usb]{lang="EN-US"}**[参数时，显示的是设备上所有单板的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_463697551}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x434215109}[显示设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display device]{lang="EN-US"}]{#struct_0_55199_x9544_x1992058134}

[Slot brief information:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Slot No.   Brd Type        Brd Status   Software Version]{lang="EN-US"}

[ 0         Simware         Master       Simware-V700R001]{lang="EN-US"}

[ ]{lang="EN-US"}

[SubCard information on slot 0:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[SSlot No.   Type        Status   Software Version]{lang="EN-US"}

[ 1          Simware     Normal   Simware-V700R001]{lang="EN-US"}

[ 2          Simware     Normal   Simware-V700R001]{lang="EN-US"}

[ 3          NONE        Fault    NONE]{lang="EN-US"}

[ 4          NONE        Absent   NONE]{lang="EN-US"}

[ 5          NONE        Absent   NONE]{lang="EN-US"}

[ 6          NONE        Fault    NONE]{lang="EN-US"}

[ 7          Simware     Normal   Simware-V700R001]{lang="EN-US"}

[ 8          NONE        Absent   NONE]{lang="EN-US"}

[]{#struct_0_55199_x9544_x1974315664}[]{#_Toc138056656}[[表1-5 ]{lang="EN-US"}[display device]{lang="EN-US"}]{#_Ref122422495}[命令显示信息描述表]{style="font-family:黑体"}[（集中式设备）]{style="font-family:黑体"}

[]{#table_struct_0_x649273586}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x434149573}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_1465389640}

[[Slot brief information]{lang="EN-US"}]{#struct_0_55199_x9544_210037244}

[[单板的概要信息]{style="font-family:宋体"}]{#struct_0_55199_x9544_1602629004}

[[Slot No.]{lang="EN-US"}]{#struct_0_55199_x9544_x1157225554}

[[单板的槽位号]{style="font-family:宋体"}]{#struct_0_55199_x9544_584202631}

[[Brd Type]{lang="EN-US"}]{#struct_0_55199_x9544_x1115457745}

[[单板的硬件类型]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2076621932}

[[Brd Status]{lang="EN-US"}]{#struct_0_55199_x9544_x434084037}

[[单板的状态：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1623388348}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_55199_x9544_240332631}[表示该槽位单板出错，不能正常启动]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_55199_x9544_x1344798725}[表示该槽位单板处于正常工作状态]{style="font-family:宋体"}

[[Software Version]{lang="EN-US"}]{#struct_0_55199_x9544_210037245}

[[当前单板上运行的软件版本]{style="font-family:宋体"}]{#struct_0_55199_x9544_1602629003}

[[SubCard information on slot]{lang="EN-US"}]{#struct_0_55199_x9544_x1911603942}

[[单板上子卡的信息]{style="font-family:宋体"}]{#struct_0_55199_x9544_210037246}

[[SSlot No.]{lang="EN-US"}]{#struct_0_55199_x9544_1602629006}

[[子卡所在的子槽位号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1911800550}

[[Type]{lang="EN-US"}]{#struct_0_55199_x9544_x1484582874}

[[当前子卡的类型]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1403615125}

[[Status]{lang="EN-US"}]{#struct_0_55199_x9544_210037247}

[[子卡的状态：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1602629005}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_55199_x9544_x1911735014}[表示子卡出错，不能正常启动]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_55199_x9544_x1269778162}[表示子卡处于正常工作状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absent]{lang="EN-US"}]{#struct_0_55199_x9544_210037248}[表示子卡不存在]{style="font-family:宋体"}

[[Max Ports]{lang="EN-US"}]{#struct_0_55199_x9544_1602629016}

[[单板支持的最大物理端口数]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1911800549}

[[Hardware]{lang="EN-US"}]{#struct_0_55199_x9544_2031104353}

[[当前单板的硬件版本]{style="font-family:宋体"}]{#struct_0_55199_x9544_1273050568}

[[Driver]{lang="EN-US"}]{#struct_0_55199_x9544_x433428677}

[[当前单板的驱动版本]{style="font-family:宋体"}]{#struct_0_55199_x9544_1976534896}

[[CPLD]{lang="EN-US"}]{#struct_0_55199_x9544_1803290329}

[[当前单板的]{style="font-family:宋体"}[CPLD]{lang="EN-US"}]{#struct_0_55199_x9544_x1695996886}[版本]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x536817589}[缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[下，显示设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display device]{lang="EN-US"}]{#struct_0_55199_x9544_x434018500}

[Slot No.   Brd Type     Brd Status     Subslot Num    Sft Ver          Patch Ver]{lang="EN-US"}

[ 0         LSQ1MPUA     Standby        0              AAAAAA-0000      None]{lang="EN-US"}

[ 1         LSQ1MPUA     Master         0              AAAAAA-0000      None]{lang="EN-US"}

[ 2         LSQ1GP12EA   Normal         0              AAAAAA-0000      None]{lang="EN-US"}

[ 3         NONE         Absent         0              NONE             None]{lang="EN-US"}

[[以上显示信息表明，该分布式设备－独立运行模式上有两块主控板，一块接口板。其中插在]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_55199_x9544_x111180153}[号槽位的是备用主控板，插在]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位的是主用主控板，插在]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位的是接口板。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_256474664}[非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[下，显示设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display device]{lang="EN-US"}]{#struct_0_55199_x9544_x1770847535}

[Slot No. CPU No.  Brd Type      Brd Status   Subslot  Sft Ver      Patch Ver    ]{lang="EN-US"}

[  6        1      NSQ1FWCEA0    Master        0       M9000-9101   None         ]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[[  9        1      NSQ1FWCEA0    Normal        0       M9000-9101   None]{lang="EN-US"}]{#struct_0_55199_x9544_256540200}

[[以上显示信息表明，该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_55199_x9544_591540484}[中有两个安全引擎，其中插在]{style="font-family:宋体"}[6]{lang="EN-US"}[号槽位的是主安全引擎，插在]{style="font-family:宋体"}[9]{lang="EN-US"}[号槽位的是备安全引擎。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[display device]{lang="EN-US"}]{#struct_0_55199_x9544_x1023290857}[命令显示信息描述表（分布式设备－独立运行模式）]{style="font-family:黑体"}

[]{#table_struct_0_x650400402}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_689817030}

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1431684409}

[[Slot No.]{lang="EN-US"}]{#struct_0_55199_x9544_x1252399699}

[[单板的槽位号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x433952964}

[[CPU No.]{lang="EN-US"}]{#struct_0_55199_x9544_x1131821291}

[[安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_x1117254834}[编号（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[Brd Type]{lang="EN-US"}]{#struct_0_55199_x9544_x1456354264}

[[单板的硬件类型]{style="font-family:宋体"}]{#struct_0_55199_x9544_1900637501}

[[Brd Status]{lang="EN-US"}]{#struct_0_55199_x9544_917209465}

[[单板状态：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1890198782}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby]{lang="EN-US"}]{#struct_0_55199_x9544_372421550}[表示该板是备用主控板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_55199_x9544_x433887428}[表示该板是主用主控板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absent]{lang="EN-US"}]{#struct_0_55199_x9544_x1908636344}[表示该槽位没有插入单板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_55199_x9544_x1231635946}[表示该槽位单板出错，不能正常启动]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_55199_x9544_x1870080858}[表示该槽位单板是接口板并处于正常工作状态]{style="font-family:宋体"}

[[Subslot Num]{lang="EN-US"}]{#struct_0_55199_x9544_x1248594454}

[[单板支持子卡的最大个数]{style="font-family:宋体"}]{#struct_0_55199_x9544_x433821892}

[[Sft Ver]{lang="EN-US"}]{#struct_0_55199_x9544_1275031171}

[[当前单板上运行的软件版本]{style="font-family:宋体"}]{#struct_0_55199_x9544_318161009}

[[Patch Ver]{lang="EN-US"}]{#struct_0_55199_x9544_x1717276887}

[[当前单板上运行的热补丁版本]{style="font-family:宋体"}]{#struct_0_55199_x9544_x627649079}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x434280644}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中各成员设备的设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display device]{lang="EN-US"}]{#struct_0_55199_x9544_1084744173}

[Slot 1]{lang="EN-US"}

[SubSNo PortNum PCBVer FPGAVer CPLDVer BootRomVer AddrLM Type       State]{lang="EN-US"}

[0      28      REV.C  NULL    002     505        IVL    MAIN       Normal]{lang="EN-US"}

[1      0       REV.A  NULL    NULL    NULL       IVL    2\*10GE     Normal]{lang="EN-US"}

[Slot 2]{lang="EN-US"}

[SubSNo PortNum PCBVer FPGAVer CPLDVer BootRomVer AddrLM Type       State]{lang="EN-US"}

[0      28      REV.C  NULL    002     503        IVL    MAIN       Normal]{lang="EN-US"}

[1      0       REV.B  NULL    NULL    NULL       IVL    2\*10GE     Normal]{lang="EN-US"}

[[以上显示信息表明，该]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1390196348}[中包含两台成员设备，每台成员设备都拥有]{style="font-family:宋体"}[28]{lang="EN-US"}[个以太网接口，配置了]{style="font-family:宋体"}[2]{lang="EN-US"}[个]{style="font-family:宋体"}[10GE]{lang="EN-US"}[的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理口。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[display device]{lang="EN-US"}]{#struct_0_55199_x9544_x154833210}[命令显示信息描述表（集中式]{style="font-family:黑体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:黑体"}

[]{#table_struct_0_x621653490}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_538547515}

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x434215108}

[[Slot 1]{lang="EN-US"}]{#struct_0_55199_x9544_x1992123670}

[[成员编号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_55199_x9544_1611928888}[的成员设备的信息]{style="font-family:宋体"}

[[SubSNo]{lang="EN-US"}]{#struct_0_55199_x9544_x53958435}

[[子卡所在的槽位号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2136010742}

[[PortNum]{lang="EN-US"}]{#struct_0_55199_x9544_x24531092}

[[子卡支持的最大端口数]{style="font-family:宋体"}]{#struct_0_55199_x9544_x434149572}

[[PCBVer]{lang="EN-US"}]{#struct_0_55199_x9544_1465455176}

[[子卡的]{style="font-family:宋体"}[PCB]{lang="EN-US"}]{#struct_0_55199_x9544_x1930978740}[版本]{style="font-family:宋体"}

[[FPGAVer]{lang="EN-US"}]{#struct_0_55199_x9544_770770474}

[[子卡的]{style="font-family:宋体"}[FPGA]{lang="EN-US"}]{#struct_0_55199_x9544_x759309306}[版本]{style="font-family:宋体"}

[[CPLDVer]{lang="EN-US"}]{#struct_0_55199_x9544_x434084036}

[[子卡的]{style="font-family:宋体"}[CPLD]{lang="EN-US"}]{#struct_0_55199_x9544_x1623322812}[版本]{style="font-family:宋体"}

[[BootRomVer]{lang="EN-US"}]{#struct_0_55199_x9544_x1703951480}

[[子卡的]{style="font-family:宋体"}[BootRom]{lang="EN-US"}]{#struct_0_55199_x9544_x210955868}[版本]{style="font-family:宋体"}

[[AddrLM]{lang="EN-US"}]{#struct_0_55199_x9544_x1327025971}

[[地址学习模式]{style="font-family:宋体"}]{#struct_0_55199_x9544_x433494212}

[[Type]{lang="EN-US"}]{#struct_0_55199_x9544_x1484648410}

[[子卡的类型]{style="font-family:宋体"}]{#struct_0_55199_x9544_951950359}

[[State]{lang="EN-US"}]{#struct_0_55199_x9544_x254491441}

[[子卡的状态]{style="font-family:宋体"}]{#struct_0_55199_x9544_x433428676}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1976600432}[缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[下，显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中各成员设备的设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display device]{lang="EN-US"}]{#struct_0_55199_x9544_1765094594}

[Chassis   Slot Type         State        Subslot      Soft Ver     Patch Ver]{lang="EN-US"}

[1         0    LSQ1SRP1CB   Master       0            S7500E-0000  None]{lang="EN-US"}

[1         1    NONE         Absent       0            NONE         None]{lang="EN-US"}

[1         2    LSQ1P24XGSC  Normal       0            S7500E-0000  None]{lang="EN-US"}

[1         3    NONE         Absent       0            NONE         None]{lang="EN-US"}

[1         4    LSQ1FV48SA   Normal       0            S7500E-0000  None]{lang="EN-US"}

[2         0    LSQ1SRP2XB   Standby      0            S7500E-0000  None]{lang="EN-US"}

[2         1    LSQ1SRP2XB   Standby      0            S7500E-0000  None]{lang="EN-US"}

[2         2    LSQ1FV48SA   Normal       0            S7500E-0000  None]{lang="EN-US"}

[2         3    LSQ1FV48SA   Normal       0            S7500E-0000  None]{lang="EN-US"}

[2         4    LSQ1P24XGSC  Normal       0            S7500E-0000  None]{lang="EN-US"}

[2         5    SRP2XBSLAVE  Normal       0            S7500E-0000  None]{lang="EN-US"}

[2         6    SRP2XBSLAVE  Normal       0            S7500E-0000  None]{lang="EN-US"}

[[以上显示信息表明，该]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_51979824}[中包含两台成员设备，成员编号分别为]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[2]{lang="EN-US"}[。同时还显示了每个框上的单板信息。从单板状态可以看出，成员设备]{style="font-family:
宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板为整个]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[的主用主控板，成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的两个主控板（]{style="font-family:宋体"}[0]{lang="EN-US"}[号和]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位）均为整个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的备用主控板。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_256146984}[非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[下，显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中各成员设备的设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display device                                                                   ]{lang="EN-US"}]{#struct_0_55199_x9544_x250538091}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Blade controller device info \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--       ]{lang="EN-US"}

[Chassis  Slot CPU   Type         State    Subslot  Soft Ver     Patch Ver]{lang="EN-US"}

[1        6    1     NSQ1FWCEA0   Master   0        M9000-9101   None         ]{lang="EN-US"}

[[2        1    1     NSQ1FWCEA0   Normal   0        M9000-9101   None]{lang="EN-US"}]{#struct_0_55199_x9544_256212520}

[[以上显示信息表明，该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_55199_x9544_x476869136}[中包含两个安全引擎，其中成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[6]{lang="EN-US"}[号单板的]{style="font-family:
宋体"}[CPU 1]{lang="EN-US"}[是主安全引擎，成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[CPU 1]{lang="EN-US"}[是备安全引擎。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[display device]{lang="EN-US"}]{#struct_0_55199_x9544_x434018499}[命令显示信息描述表（分布式设备－]{style="font-family:黑体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:黑体"}

[]{#table_struct_0_x626974610}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_1844676222}

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_340494320}

[[Chassis]{lang="EN-US"}]{#struct_0_55199_x9544_893887910}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_2125946857}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_1875852507}

[[成员设备上单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x433952963}

[[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_x312350319}

[[安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_256278056}[编号（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_55199_x9544_x1455895512}

[[单板型号]{style="font-family:宋体"}]{#struct_0_55199_x9544_63119997}

[[State]{lang="EN-US"}]{#struct_0_55199_x9544_330114247}

[[单板的当前状态：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2035928550}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absent]{lang="EN-US"}]{#struct_0_55199_x9544_x433887427}[：单板不在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_55199_x9544_x1908570808}[：单板为全局主用主控板（即整个]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[的主用主控板）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby]{lang="EN-US"}]{#struct_0_55199_x9544_x997432635}[：单板为全局备用主控板（即整个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的备用主控板）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_55199_x9544_x1412481808}[：单板为接口板，并且状态正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_55199_x9544_1894799909}[：单板状态异常]{style="font-family:宋体"}

[[Subslot]{lang="EN-US"}]{#struct_0_55199_x9544_x433821891}

[[单板支持子卡的最大个数]{style="font-family:宋体"}]{#struct_0_55199_x9544_1274834563}

[[Soft Ver]{lang="EN-US"}]{#struct_0_55199_x9544_1440810609}

[[当前单板上运行的软件版本]{style="font-family:宋体"}]{#struct_0_55199_x9544_1749893838}

[[Patch Ver]{lang="EN-US"}]{#struct_0_55199_x9544_x751776203}

[[当前单板上运行的热补丁版本，]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_55199_x9544_x434280643}[表示没有补丁]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1431085200 .myid}
[]{#_Toc263066880}[]{#_Toc404783078}[]{#struct_0_55199_x9544_1084809709}[]{#_Toc300730508}[]{#_Toc300730271}[]{#_Toc263066879}[]{#_Toc206560266}[]{#_Ref170036793}[]{#_Ref170036790}[]{#_Toc145212270}[]{#_Toc140379438}[]{#_Toc262216245}[]{#_Toc262473777}[]{#_Toc262216246}[]{#_Toc262473778}[]{#_Toc262216247}[]{#_Toc262473779}[]{#_Toc262216248}[]{#_Toc262473780}[]{#_Toc262216249}[]{#_Toc262473781}[]{#_Toc262216250}[]{#_Toc262473782}[]{#_Toc262216251}[]{#_Toc262473783}[]{#_Toc262216252}[]{#_Toc262473784}[]{#_Toc262216253}[]{#_Toc262473785}[]{#_Toc262216254}[]{#_Toc262473786}[]{#_Toc262216255}[]{#_Toc262473787}[]{#_Toc262216256}[]{#_Toc262473788}[]{#_Toc262216257}[]{#_Toc262473789}[]{#_Toc262216258}[]{#_Toc262473790}[]{#_Toc262216259}[]{#_Toc262473791}[]{#_Toc262216260}[]{#_Toc262473792}[]{#_Toc262216261}[]{#_Toc262473793}[]{#_Toc262216262}[]{#_Toc262473794}[]{#_Toc262216263}[]{#_Toc262473795}[]{#_Toc262216264}[]{#_Toc262473796}[]{#_Toc262216265}[]{#_Toc262473797}[]{#_Toc262216266}[]{#_Toc262473798}[]{#_Toc262216267}[]{#_Toc262473799}[]{#_Toc262216268}[]{#_Toc262473800}[]{#_Toc262216269}[]{#_Toc262473801}[]{#_Toc262216270}[]{#_Toc262473802}[]{#_Toc262216271}[]{#_Toc262473803}[]{#_Toc262216275}[]{#_Toc262473807}[]{#_Toc262216276}[]{#_Toc262473808}[]{#_Toc262216292}[]{#_Toc262473824}[]{#_Toc262216293}[]{#_Toc262473825}[]{#_Toc262216294}[]{#_Toc262473826}[]{#_Toc262216300}[]{#_Toc262473832}[]{#_Toc262216301}[]{#_Toc262473833}[]{#_Toc262216314}[]{#_Toc262473846}[]{#_Toc262216315}[]{#_Toc262473847}[]{#_Toc262216316}[]{#_Toc262473848}[]{#_Toc262216317}[]{#_Toc262473849}[]{#_Toc262216320}[]{#_Toc262473852}[]{#_Toc262216321}[]{#_Toc262473853}[]{#_Toc262216337}[]{#_Toc262473869}[]{#_Toc262216338}[]{#_Toc262473870}[]{#_Toc262216339}[]{#_Toc262473871}[]{#_Toc262216345}[]{#_Toc262473877}[]{#_Toc262216346}[]{#_Toc262473878}[]{#_Toc262216359}

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo**

------------------------------------------------------------------------

[**[display device manuinfo]{lang="EN-US"}**]{#struct_0_55199_x9544_x952547795}[命令用来显示设备的电子标签信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_774554166}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x859398559}

[**[display device manuinfo]{lang="EN-US"}**[ \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_150836997}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x1266270848}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display device manuinfo]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1417864651}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x434215107}[模式：]{style="font-family:宋体"}

[**[display device manuinfo ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **subslot** *subslot-number* \] \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1991140630}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x526339623}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x584770937}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1429912311}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x736665671}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1009818576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1109276737}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x434149571}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1465520712}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1554164950}[：显示指定成员设备的电子标签信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不输入该参数时，显示所有成员设备的相应信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1645090452}[：显示指定成员设备]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟框的电子标签信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。不输入该参数时，显示所有成员设备]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟框的相应信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1876691290}[：显示指定单板的电子标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不输入该参数时，显示所有单板的相应信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1644238484}[：显示指定单板的电子标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不输入该参数时，显示所有单板的相应信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x892061954}[：显示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的电子标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不输入该参数时，显示所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的相应信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1112555471}[：显示指定成员设备的电子标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不输入该参数时，显示所有成员设备的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_2145235105}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的电子标签信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不输入该参数时，显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的相应信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot]{lang="EN-US"}**[ *subslot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_154235038}[：显示指定子卡的电子标签信息。]{style="font-family:宋体"}*[subslot-number]{lang="EN-US"}*[表示子卡所在的子槽位号。不指定该参数时，不会显示子卡的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_256343592}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的电子标签信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1386759152}

[[电子标签信息也可以称为永久配置数据或档案信息等，在单板或者设备的调测（调试、测试）过程中被写入到设备的存储器件中，包括单板的名称、生产序列号、]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_55199_x9544_x434084035}[地址、制造商等信息。本命令显示的是设备的部分电子标签信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1623257276}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_2031108415}[显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo]{lang="EN-US"}]{#struct_0_55199_x9544_851946768}

[Slot 0:]{lang="EN-US"}

[DEVICE_NAME          : aaaa]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : xxxx]{lang="EN-US"}

[MAC_ADDRESS          : 000F-E26A-58EA]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-11-10]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[The card does not support manufacture information.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_510104284}[显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo]{lang="EN-US"}]{#struct_0_55199_x9544_x433494211}

[Slot 0 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : LSQ1MPUA0]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210231A73SA07B000108]{lang="EN-US"}

[MAC_ADDRESS          : 000F-E26A-58ED]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-11-9]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[Slot 1 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : LSQ1MPUA0]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210231A73SA07B000075]{lang="EN-US"}

[MAC_ADDRESS          : 000F-E26A-581B]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-11-10]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[Slot 2 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : LSQ1T24XGSC0]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210231A76VX081000020]{lang="EN-US"}

[MAC_ADDRESS          : No]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-12-2]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1484713946}[显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo]{lang="EN-US"}]{#struct_0_55199_x9544_x433428675}

[Slot 1 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : 3CRS48G-24-91]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 9S4F9PLBC3111]{lang="EN-US"}

[MAC_ADDRESS          : 001C-C5BC-3111]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-05-08]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[Slot 2 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : S5500-28C-EI]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A252A079000140]{lang="EN-US"}

[MAC_ADDRESS          : 000F-E269-46D1]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-09-26]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display device manuinfo]{lang="EN-US"}]{#struct_0_55199_x9544_1976403824}[命令信息显示描述表]{style="font-family:黑体"}

[]{#table_struct_0_x629199314}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2094618336}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_1230377389}

[[Slot 1 CPU 0]{lang="EN-US"}]{#struct_0_55199_x9544_x434018498}

[[单板所在的槽位号和]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_1844610686}[编号（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[设备的成员编号和]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_309478300}[编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[DEVICE_NAME]{lang="EN-US"}]{#struct_0_55199_x9544_x63835523}

[[设备名称]{style="font-family:宋体"}]{#struct_0_55199_x9544_315202375}

[[DEVICE_SERIAL_NUMBER]{lang="EN-US"}]{#struct_0_55199_x9544_x1682325831}

[[设备序列号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x433952962}

[[MAC_ADDRESS]{lang="EN-US"}]{#struct_0_55199_x9544_x1455961048}

[[设备出厂]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_55199_x9544_x1490901647}[地址]{style="font-family:宋体"}

[[MANUFACTURING_DATE]{lang="EN-US"}]{#struct_0_55199_x9544_x1859845600}

[[设备调测日期]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1094836543}

[[VENDOR_NAME]{lang="EN-US"}]{#struct_0_55199_x9544_x433887426}

[[制造商名称]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1908505272}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1588477222}[显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo]{lang="EN-US"}]{#struct_0_55199_x9544_x433821890}

[Chassis 1 slot 0 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : LSQ1MPUA0]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210231A73SA07B000108]{lang="EN-US"}

[MAC_ADDRESS          : 000F-E26A-58ED]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-11-9]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[Chassis 1 slot 1 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : LSQ1MPUA0]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210231A73SA07B000075]{lang="EN-US"}

[MAC_ADDRESS          : 000F-E26A-581B]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-11-10]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[Chassis 1 slot 2 CPU 0:]{lang="EN-US"}

[DEVICE_NAME          : LSQ1T24XGSC0]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210231A76VX081000020]{lang="EN-US"}

[MAC_ADDRESS          : No]{lang="EN-US"}

[MANUFACTURING_DATE   : 2012-12-2]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display device manuinfo]{lang="EN-US"}]{#struct_0_55199_x9544_1274900099}[命令信息显示描述表]{style="font-family:黑体"}

[]{#table_struct_0_x634005554}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_303772649}

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_128590719}

[[Chassis 1 slot 0 CPU 0]{lang="EN-US"}]{#struct_0_55199_x9544_440521765}

[[成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_55199_x9544_x434280642}[上]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[0]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的相关信息]{style="font-family:宋体"}

[[DEVICE_NAME]{lang="EN-US"}]{#struct_0_55199_x9544_1084875245}

[[设备名称]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1388659339}

[[DEVICE_SERIAL_NUMBER]{lang="EN-US"}]{#struct_0_55199_x9544_x2050562689}

[[设备序列号]{style="font-family:宋体"}]{#struct_0_55199_x9544_528413185}

[[MAC_ADDRESS]{lang="EN-US"}]{#struct_0_55199_x9544_x690496793}

[[设备出厂]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_55199_x9544_x434215106}[地址]{style="font-family:宋体"}

[[MANUFACTURING_DATE]{lang="EN-US"}]{#struct_0_55199_x9544_x1991206166}

[[设备调测日期]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1746900558}

[[VENDOR_NAME]{lang="EN-US"}]{#struct_0_55199_x9544_1928605373}

[[制造商名称]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1076111930}

[ ]{lang="EN-US"}

::::: {#2058259436 .myid}
[]{#_Toc404783079}[]{#struct_0_55199_x9544_x434149570}[]{#_Toc300730509}[]{#_Toc300730272}[]{#_Toc298404812}[]{#_Toc297292392}[]{#_Toc279132141}

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo chassis-only**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1465586248}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x806678841}
:::

**[ ]{lang="EN-US"}**

[**[display device manuinfo chassis-only]{lang="EN-US"}**]{#struct_0_55199_x9544_x424241536}[命令用来显示指定机框背板的电子标签信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_968324430}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2052495449}

[**[display device manuinfo chassis-only]{lang="EN-US"}**]{#struct_0_55199_x9544_1094674344}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x474993965}[模式：]{style="font-family:宋体"}

[**[display device manuinfo chassis]{lang="EN-US"}**[ *chassis-number* **chassis-only**]{lang="EN-US"}]{#struct_0_55199_x9544_x434084034}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1623191740}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1383446846}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1944952800}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1595702353}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1361489953}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_655399048}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x433494210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1484779482}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_55199_x9544_670999570}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_55199_x9544_413797366}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x433428674}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1976469360}[显示机框背板的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo chassis-only]{lang="EN-US"}]{#struct_0_55199_x9544_632101646}

[Chassis self:]{lang="EN-US"}

[DEVICE_NAME          : backplane]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A36L1234567890]{lang="EN-US"}

[MAC_ADDRESS          : NONE]{lang="EN-US"}

[MANUFACTURING_DATE   : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1965894947}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上机框背板的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo chassis 1 chassis-only]{lang="EN-US"}]{#struct_0_55199_x9544_1132065438}

[Chassis 1:]{lang="EN-US"}

[Chassis self:]{lang="EN-US"}

[DEVICE_NAME            : backplane]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER   : 210235A36L1234567891]{lang="EN-US"}

[MAC_ADDRESS            : NONE]{lang="EN-US"}

[MANUFACTURING_DATE     : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME            : H3C]{lang="EN-US"}
:::::

::::: {#1074325144 .myid}
[]{#_Toc404783080}[]{#struct_0_55199_x9544_x994849259}[]{#_Toc300730510}[]{#_Toc300730273}[]{#_Toc298404813}[]{#_Toc297292393}

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo fan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_659492145}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1390004024}
:::

**[ ]{lang="EN-US"}**

[**[display device manuinfo fan]{lang="EN-US"}**]{#struct_0_55199_x9544_991111963}[命令用来显示指定风扇的电子标签信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x925805750}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x10902522}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display device manuinfo fan]{lang="EN-US"}***[ fan-id]{lang="EN-US"}*]{#struct_0_55199_x9544_x1721747577}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1132130974}[设备：]{style="font-family:宋体"}

[**[display device manuinfo slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ fan]{lang="EN-US"}***[ fan-id]{lang="EN-US"}*]{#struct_0_55199_x9544_1341723903}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1310052058}[模式：（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display device manuinfo chassis]{lang="EN-US"}**[ *chassis-number* **fan** *fan-id*]{lang="EN-US"}]{#struct_0_55199_x9544_x755033102}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x749002048}[模式：（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display device manuinfo chassis]{lang="EN-US"}**[ { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } **fan** *fan-id*]{lang="EN-US"}]{#struct_0_55199_x9544_x724949201}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1070492717}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1187950435}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_701842383}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x209875737}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1132196510}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_921709511}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x557088643}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_471504504}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1025002990}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1645090459}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_55199_x9544_2081561869}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_560714480}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[virtual-chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[在虚拟框中的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[fan-id]{lang="EN-US"}*]{#struct_0_55199_x9544_x315170895}[：表示设备上风扇的]{style="font-family:宋体"}[ID]{lang="EN-US"}[编号。该参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_194368019}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1132262046}[显示风扇]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo fan 2]{lang="EN-US"}]{#struct_0_55199_x9544_1693056663}

[Fan 2:]{lang="EN-US"}

[DEVICE_NAME          : fan]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A36L1234567890]{lang="EN-US"}

[MAC_ADDRESS          : NONE]{lang="EN-US"}

[MANUFACTURING_DATE   : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1193034216}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上风扇]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo fan 2]{lang="EN-US"}]{#struct_0_55199_x9544_1131803294}

[Slot 1:]{lang="EN-US"}

[Fan 2:]{lang="EN-US"}

[DEVICE_NAME          : fan]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A36L1234567890]{lang="EN-US"}

[MAC_ADDRESS          : NONE]{lang="EN-US"}

[MANUFACTURING_DATE   : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x133068619}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上风扇]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo chassis 1 fan 2]{lang="EN-US"}]{#struct_0_55199_x9544_2051966598}

[Chassis 1:]{lang="EN-US"}

[Fan 2:]{lang="EN-US"}

[DEVICE_NAME            : fan2]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER   : 210235A36L1234567891]{lang="EN-US"}

[MAC_ADDRESS            : NONE]{lang="EN-US"}

[MANUFACTURING_DATE     : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME            : H3C]{lang="EN-US"}
:::::

::::: {#-673283811 .myid}
[]{#_Toc404783081}[]{#struct_0_55199_x9544_x1331340388}[]{#_Toc300730511}[]{#_Toc300730274}[]{#_Toc298404814}[]{#_Toc297292394}

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo power**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_240859724}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x233409183}
:::

[ ]{lang="EN-US"}

[**[display device manuinfo power]{lang="EN-US"}**]{#struct_0_55199_x9544_1131868830}[命令用来显示指定电源的电子标签信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x127026964}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x1418258628}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display device manuinfo power]{lang="EN-US"}**[ *power-id*]{lang="EN-US"}]{#struct_0_55199_x9544_x1321963480}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x922376857}[设备：]{style="font-family:宋体"}

[**[display device manuinfo slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}***[power]{lang="EN-US"}**[ *power-id*]{lang="EN-US"}]{#struct_0_55199_x9544_1327830982}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x412798240}[模式：（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display device manuinfo chassis]{lang="EN-US"}**[ *chassis-number* **power** *power-id*]{lang="EN-US"}]{#struct_0_55199_x9544_1460041620}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_460851533}[模式：（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display device manuinfo chassis]{lang="EN-US"}**[ { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } **power** *power-id*]{lang="EN-US"}]{#struct_0_55199_x9544_x1152362989}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1131934366}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1061568906}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x550785455}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1849381977}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x120881152}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x282429838}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1314057042}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1870515079}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1131999902}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1644762778}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x918797263}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_1972918676}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[virtual-chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[在虚拟框中的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[power-id]{lang="EN-US"}*]{#struct_0_55199_x9544_516573017}[：表示设备上电源的]{style="font-family:宋体"}[ID]{lang="EN-US"}[编号，该参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1672692590}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1824317949}[显示电源]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo power 2]{lang="EN-US"}]{#struct_0_55199_x9544_2044317248}

[Power 2:]{lang="EN-US"}

[DEVICE_NAME          : power]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A36L1234567890]{lang="EN-US"}

[MAC_ADDRESS          : NONE]{lang="EN-US"}

[MANUFACTURING_DATE   : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1132589726}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上电源]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo slot 1 power 2]{lang="EN-US"}]{#struct_0_55199_x9544_100680883}

[Slot 1:]{lang="EN-US"}

[Power 2:]{lang="EN-US"}

[DEVICE_NAME          : power]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A36L1234567890]{lang="EN-US"}

[MAC_ADDRESS          : NONE]{lang="EN-US"}

[MANUFACTURING_DATE   : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x918370373}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上电源监控模块]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo chassis 1 power 2]{lang="EN-US"}]{#struct_0_55199_x9544_1132655262}

[Chassis 1:]{lang="EN-US"}

[Power 2:]{lang="EN-US"}

[DEVICE_NAME            : power2]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER   : 210235A36L1234567891]{lang="EN-US"}

[MAC_ADDRESS            : NONE]{lang="EN-US"}

[MANUFACTURING_DATE     : 2010-01-20]{lang="EN-US"}

[VENDOR_NAME            : H3C]{lang="EN-US"}
:::::

::::: {#-447189521 .myid}
[]{#_Toc404783082}[]{#struct_0_55199_x9544_x1644697242}

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo power-monitor**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1767660848}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x1644893850}
:::

[ ]{lang="EN-US"}

[**[display device manuinfo power-monitor]{lang="EN-US"}**]{#struct_0_55199_x9544_1887156640}[命令用来显示指定电源监控模块的电子标签信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x189898611}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x1072848747}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display device manuinfo power-monitor]{lang="EN-US"}**[ *pm-id*]{lang="EN-US"}]{#struct_0_55199_x9544_1134661698}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1549426619}[设备：]{style="font-family:宋体"}

[**[display device manuinfo slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}***[power-monitor]{lang="EN-US"}**[ *pm-id*]{lang="EN-US"}]{#struct_0_55199_x9544_1118733510}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1622364244}[模式：（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display device manuinfo chassis]{lang="EN-US"}**[ *chassis-number* **power-monitor** *pm-id*]{lang="EN-US"}]{#struct_0_55199_x9544_1376739738}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x369580300}[模式：（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display device manuinfo chassis]{lang="EN-US"}**[ { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } **power-monitor** *pm-id*]{lang="EN-US"}]{#struct_0_55199_x9544_x1533140699}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2056405562}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1644828314}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_673187904}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1768740642}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1556024239}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1437445465}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x2090904277}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x289521696}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_2107488623}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_23968967}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x239128131}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_x1645024922}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[virtual-chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[在虚拟框中的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[pm-id]{lang="EN-US"}*]{#struct_0_55199_x9544_x1722956853}[：表示设备上电源监控模块的]{style="font-family:宋体"}[ID]{lang="EN-US"}[编号，该参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_840479622}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_466822820}[显示电源监控模块]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo power-monitor 2]{lang="EN-US"}]{#struct_0_55199_x9544_x1156605390}

[PowerMonitor 2:]{lang="EN-US"}

[DEVICE_NAME          : PowerMonitor]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A36L1234567890]{lang="EN-US"}

[MAC_ADDRESS          : NONE]{lang="EN-US"}

[MANUFACTURING_DATE   : 2013-01-20]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1676403704}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上电源监控模块]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo slot 1 power-monitor 2]{lang="EN-US"}]{#struct_0_55199_x9544_x922194649}

[Slot 1:]{lang="EN-US"}

[PowerMonitor 2:]{lang="EN-US"}

[DEVICE_NAME          : PowerMonitor]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER : 210235A36L1234567890]{lang="EN-US"}

[MAC_ADDRESS          : NONE]{lang="EN-US"}

[MANUFACTURING_DATE   : 2013-01-20]{lang="EN-US"}

[VENDOR_NAME          : H3C]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1644959386}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上电源监控模块]{style="font-family:宋体"}[2]{lang="EN-US"}[的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display device manuinfo chassis 1 power-monitor 2]{lang="EN-US"}]{#struct_0_55199_x9544_x1241103969}

[Chassis 1:]{lang="EN-US"}

[PowerMonitor 2:]{lang="EN-US"}

[DEVICE_NAME            : PowerMonitor]{lang="EN-US"}

[DEVICE_SERIAL_NUMBER   : 210235A36L1234567891]{lang="EN-US"}

[MAC_ADDRESS            : NONE]{lang="EN-US"}

[MANUFACTURING_DATE     : 2013-01-20]{lang="EN-US"}

[VENDOR_NAME            : H3C]{lang="EN-US"}
:::::

::: {#957419880 .myid}
[]{#_Toc121581308}[]{#_Toc404783083}[]{#struct_0_55199_x9544_142134732}[]{#_Toc300730512}[]{#_Toc300730275}[]{#_Toc263066881}

**设备管理 \-- 设备管理配置命令 \-- display diagnostic-information**

------------------------------------------------------------------------

[**[display diagnostic-information]{lang="EN-US"}**]{#struct_0_55199_x9544_x713965718}[命令用来显示系统当前多个功能模块运行的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1207095087}

[**[display diagnostic-information ]{lang="EN-US"}**[\[ **hardware** \| **infrastructure** \| **l2** \| **l3** \| **service** \] \[ *filename* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1370142940}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1539776034}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1010445184}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1609997702}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1132065439}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x994783723}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1314469767}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x205496596}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_200989343}

[**[hardware]{lang="EN-US"}**]{#struct_0_55199_x9544_x1871863351}[：收集硬件相关诊断信息。]{style="font-family:宋体"}

[**[infrastructure]{lang="EN-US"}**]{#struct_0_55199_x9544_x1328119165}[：收集基础模块的诊断信息。]{style="font-family:宋体"}

[**[l2]{lang="EN-US"}**]{#struct_0_55199_x9544_x1912107483}[：收集二层特性相关诊断信息。]{style="font-family:宋体"}

[**[l3]{lang="EN-US"}**]{#struct_0_55199_x9544_1132130975}[：收集三层特性相关诊断信息。]{style="font-family:宋体"}

[**[service]{lang="EN-US"}**]{#struct_0_55199_x9544_1341658367}[：收集上层业务模块相关诊断信息。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_55199_x9544_1124650685}[：表示将收集到的诊断信息保存到指定文件。]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[表示文件的名称，后缀必须为"]{style="font-family:宋体"}[.tar.gz]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2018633830}

[[在日常维护或系统出现故障时，为了便于问题定位，用户需要查看各个功能模块的运行信息。因为各个功能模块都有其对应的运行信息，所以一般情况下，用户需要逐条运行相应的]{style="font-family:宋体"}**[display]{lang="EN-US"}**]{#struct_0_55199_x9544_x208757996}[命令。为便于一次性收集更多信息，用户可以在任意视图下执行]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **diagnostic-information**]{lang="EN-US"}[命令，显示系统当前多个功能模块运行的统计信息。]{style="font-family:宋体"}

[[使用该命令，用户可以直接显示指定的诊断信息或者将诊断信息直接保存到指定文件，因为诊断信息较多，系统会自动将该文件压缩后保存，文件名后缀为"]{style="font-family:宋体"}[.tar.gz]{lang="EN-US"}]{#struct_0_55199_x9544_x128102561}["。如果要在设备上查看该文件的内容，请使用]{style="font-family:宋体"}**[tar extract]{lang="EN-US"}**[命令解包后再使用]{style="font-family:宋体"}**[more]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[该命令不支持"]{style="font-family:宋体"}**[\|]{lang="EN-US"}**]{#struct_0_55199_x9544_1124716221}["、"]{style="font-family:宋体"}**[\>]{lang="EN-US"}**["和"]{style="font-family:宋体"}**[\>\>]{lang="EN-US"}**["参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1194268155}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1785004502}[显示系统当前各个功能模块运行的统计信息（因为显示信息多，而且跟设备型号有关，请以设备的实际情况为准，此处略）。]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic-information]{lang="EN-US"}]{#struct_0_55199_x9544_1132196511}

[Save or display diagnostic information (Y=save, N=display)? \[Y/N\]:n]{lang="EN-US"}

[===============================================]{lang="EN-US"}

[  ===============display clock===============]{lang="EN-US"}

[14:03:55 UTC Thu 01/05/2012]{lang="EN-US"}

[=================================================]{lang="EN-US"}

[  ===============display version===============  ]{lang="EN-US"}

[[......略......]{style="font-family:宋体"}]{#struct_0_55199_x9544_921643975}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x2053551541}[将收集到的诊断信息保存到文件]{style="font-family:宋体"}[test.tar.gz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法一：在交互信息时选择将诊断信息保存到指定文件，并输入文件名]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1745883938}[test.tar.gz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic-information]{lang="EN-US"}]{#struct_0_55199_x9544_x384616390}

[Save or display diagnostic information (Y=save, N=display)? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.tar.gz)\[flash:/diag.tar.gz\]: test.tar.gz]{lang="EN-US"}

[Diagnostic information is outputting to flash:/test.tar.gz.]{lang="EN-US"}

[Please wait\...]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方法二：在命令行中直接通过参数指定将诊断信息保存到文件]{style="font-family:宋体"}]{#struct_0_55199_x9544_1124126398}[test.tar.gz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic-information test.tar.gz]{lang="EN-US"}]{#struct_0_55199_x9544_295324292}

[Diagnostic information is outputting to flash:/test.tar.gz.]{lang="EN-US"}

[Please wait\...]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_789982998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[more]{lang="EN-US"}**]{#struct_0_55199_x9544_2098013876}[（基础配置命令参考]{style="font-family:
宋体"}[/]{lang="EN-US"}[文件系统管理）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tar extract]{lang="EN-US"}**]{#struct_0_55199_x9544_x1945309598}[（基础配置命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[文件系统管理）]{style="font-family:宋体"}
:::

::::: {#-1766790759 .myid}
[]{#_Toc404783084}[]{#struct_0_55199_x9544_x1759489407}[]{#_Toc300730513}[]{#_Toc300730276}[]{#_Toc263066882}[]{#_Toc174184066}[]{#_Toc174184067}[]{#_Toc174184098}

**设备管理 \-- 设备管理配置命令 \-- display environment**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x721376605}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_2050496480}
:::

**[ ]{lang="EN-US"}**

[**[display environment]{lang="EN-US"}**]{#struct_0_55199_x9544_216423786}[命令用来显示设备上温度传感器的温度信息，包括当前温度和设定的温度告警门限。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x674662592}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1132262047}

[**[display environment]{lang="EN-US"}**]{#struct_0_55199_x9544_1693122199}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_439643982}

[**[display environment]{lang="EN-US"}**[ \[ **slot** *slot-number* \| **vent** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x860542279}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x123663778}[设备：]{style="font-family:宋体"}

[**[display environment]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1944739692}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1110156063}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **environment** \[ **chassis** *chassis-number* \[ **slot** *slot-number* \| **vent** \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_924604822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1131803295}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x133003083}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x247966142}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1202039283}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x473598277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x79602293}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1177863155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1324054092}

[**[chassis]{lang="EN-US"}***[ ]{lang="EN-US"}[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1131868831}[：显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上温度传感器的温度信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ ]{lang="EN-US"}[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_862849357}[：显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上温度传感器的温度信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x126961428}[：显示设备中指定单板上的温度传感器的温度信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1297853138}[：显示设备中指定单板上的温度传感器的温度信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1483146795}[：显示设备中指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的温度传感器的温度信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1040484778}[：显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备上的温度传感器的温度信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示的是]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有温度传感器的温度信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_2064209074}[：显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上的温度传感器的温度信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，显示的是]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有温度传感器的温度信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[vent]{lang="EN-US"}**]{#struct_0_55199_x9544_x1917437780}[：显示设备中机框、风扇框上温度传感器的温度信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_434431815}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_1762513799}**[slot]{lang="EN-US"}**[和]{style="font-family:宋体"}**[vent]{lang="EN-US"}**[参数时，显示的是设备上所有温度传感器的温度信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_x215502592}**[chassis]{lang="EN-US"}**[参数时，显示的是]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有温度传感器的温度信息；指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[但不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[和]{style="font-family:宋体"}**[vent]{lang="EN-US"}**[参数时，显示的是指定成员设备上所有温度传感器的温度信息。]{style="font-family:宋体"}[（分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x801314479}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1131934367}[显示设备上所有温度传感器的温度信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display environment]{lang="EN-US"}]{#struct_0_55199_x9544_1061503370}

[System temperature information (degree centigrade):]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Slot  Sensor       Temperature  LowerLimit  WarningLimit  AlarmLimit ShutdownLimit]{lang="EN-US"}

[Vent  outflow 1    38           10          40            50          70]{lang="EN-US"}

[0     inflow 1     27           -10         50            70          100]{lang="EN-US"}

[0     hotspot 1    53           10          50            80          100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1326952693}[显示设备上所有温度传感器的温度信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display environment]{lang="EN-US"}]{#struct_0_55199_x9544_1131999903}

[System temperature information (degree centigrade):]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Slot  Sensor       Temperature  LowerLimit  WarningLimit  AlarmrLimit ShutdownLimit]{lang="EN-US"}

[Vent  outflow 1    38           10          40            50          100]{lang="EN-US"}

[0     hotspot 1    53           10          50            80          100]{lang="EN-US"}

[0     hotspot 2    52           10          50            80          100]{lang="EN-US"}

[0     outflow 1    39           10          50            80          100]{lang="EN-US"}

[1     hotspot 1    42           10          50            80          100]{lang="EN-US"}

[4     hotspot 1    42           10          50            80          100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x918862799}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有温度传感器的温度信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display environment]{lang="EN-US"}]{#struct_0_55199_x9544_x1824265742}

[System temperature information (degree centigrade):]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Slot   Sensor        Temperature LowerLimit WarningLimit AlarmrLimit ShutdownLimit]{lang="EN-US"}

[1/Vent outflow 1     38          10         40           50          70]{lang="EN-US"}

[1/0    inflow  1     27          -10        50           70          100]{lang="EN-US"}

[1/0    hotspot 1     53          10         50           80          100]{lang="EN-US"}

[1/0    hotspot 2     52          10         50           80          100]{lang="EN-US"}

[1/0    outflow 1     39          10         50           80          100]{lang="EN-US"}

[1/1    hotspot 1     42          10         50           80          100]{lang="EN-US"}

[1/4    hotspot 1     42          10         50           80          100]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display environment]{lang="EN-US"}]{#struct_0_55199_x9544_1491158016}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x607322770}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_1132589727}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_100746419}

[[System Temperature information (degree centigrade)]{lang="EN-US"}]{#struct_0_55199_x9544_1012725209}

[[系统温度信息（单位为摄氏度）]{style="font-family:宋体"}]{#struct_0_55199_x9544_1000432277}

[[sensor]{lang="EN-US"}]{#struct_0_55199_x9544_x2096743891}

[[温度传感器]{style="font-family:宋体"}]{#struct_0_55199_x9544_x348501458}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hotspot]{lang="EN-US"}]{#struct_0_55199_x9544_1132655263}[：表示热点温度传感器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inflow]{lang="EN-US"}]{#struct_0_55199_x9544_142069196}[：表示入风口温度传感器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[outflow]{lang="EN-US"}]{#struct_0_55199_x9544_x1888311245}[：表示出风口温度传感器]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_x1437359829}

[[当显示数字时表示设备上温度传感器的温度信息；当显示]{style="font-family:宋体"}[Vent]{lang="EN-US"}]{#struct_0_55199_x9544_1780999276}[时表示位于机框、风扇框上的温度传感器的温度信息（集中式设备）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_1132065440}

[[当显示数字时表示指定槽位单板上温度传感器的温度信息；当显示]{style="font-family:宋体"}[Vent]{lang="EN-US"}]{#struct_0_55199_x9544_x994324968}[时表示位于机框、风扇框上的温度传感器的温度信息（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_x1316227018}

[[当显示数字时表示指定成员设备上温度传感器的温度信息；当显示]{style="font-family:宋体"}[Vent]{lang="EN-US"}]{#struct_0_55199_x9544_x1156767420}[时表示位于机框、风扇框上的温度传感器的温度信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_2062429189}

[[当显示]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[/*slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1132130976}[时表示指定成员设备指定单板上温度传感器的温度信息；当显示]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[/Vent]{lang="EN-US"}[时表示指定成员设备上位于机框、风扇框上的温度传感器的温度信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Temperature]{lang="EN-US"}]{#struct_0_55199_x9544_1341592831}

[[当前温度]{style="font-family:宋体"}]{#struct_0_55199_x9544_902584828}

[[LowerLimit]{lang="EN-US"}]{#struct_0_55199_x9544_1218574144}

[[低温告警门限]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1914579222}

[[WarningLimit]{lang="EN-US"}]{#struct_0_55199_x9544_1132196512}

[[一般级（]{style="font-family:宋体"}[Warning]{lang="EN-US"}]{#struct_0_55199_x9544_921840583}[）高温告警门限]{style="font-family:宋体"}

[[AlarmLimit]{lang="EN-US"}]{#struct_0_55199_x9544_x1154842597}

[[严重级（]{style="font-family:宋体"}[Alarm]{lang="EN-US"}]{#struct_0_55199_x9544_609792083}[）高温告警门限]{style="font-family:宋体"}

[[ShutdownLimit]{lang="EN-US"}]{#struct_0_55199_x9544_1132262048}

[[关断级（]{style="font-family:宋体"}[Shutdown]{lang="EN-US"}]{#struct_0_55199_x9544_1692139159}[）高温告警门限，当温度传感器的温度大于该门限时，设备会自动关闭]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1683226009 .myid}
[]{#_Toc300730514}[]{#_Toc300730277}[]{#_Toc263066884}[]{#_Toc404783085}[]{#struct_0_55199_x9544_x1887289571}[]{#_Toc343516513}[]{#_Toc339630668}[]{#_Toc257634897}[]{#_Toc141506493}

**设备管理 \-- 设备管理配置命令 \-- display fabric utilization**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1514313496}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_396861189}
:::

[ ]{lang="EN-US"}

[**[display fabric utilization]{lang="EN-US"}**]{#struct_0_55199_x9544_258916382}[命令用来显示设备接口板上交换芯片的通道利用率信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1131803296}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[:]{lang="EN-US"}]{#struct_0_55199_x9544_x133199691}

[**[display fabric utilization]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x695856570}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x495448099}[模式]{style="font-family:宋体"}[:]{lang="EN-US"}

[**[display fabric utilization]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x296320684}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_829957580}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2113744958}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1131868832}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x126895892}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1383816174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x572784163}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_29676815}[：显示指定单板上交换芯片的通道利用率信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}*]{#struct_0_55199_x9544_x572606389}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的通道利用率信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[单板所在的槽位号。不指定该参数时，表示所有]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}*]{#struct_0_55199_x9544_815729654}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：显示指定单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的通道利用率信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示所有]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1599061610}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1904665618}[显示]{style="font-family:宋体"}[5]{lang="EN-US"}[号接口板上交换芯片的通道信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<System\> display fabric utilization slot 5]{lang="EN-US"}]{#struct_0_55199_x9544_1131934368}

[                    Input                         Output]{lang="EN-US"}

[Chs Slot Chan Speed Usage Peak                    Usage Peak]{lang="EN-US"}

[0    5    0    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30 ]{lang="EN-US"}

[0    5    1    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30 ]{lang="EN-US"}

[0    5    2    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30 ]{lang="EN-US"}

[0    5    3    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1060913546}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[6]{lang="EN-US"}[号接口板上交换芯片的通道信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<System\> display fabric utilization chassis 2 slot 6]{lang="EN-US"}]{#struct_0_55199_x9544_x223891334}

[                    Input                         Output]{lang="EN-US"}

[Chs Slot Chan Speed Usage Peak                    Usage Peak]{lang="EN-US"}

[2    6    0    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24]{lang="EN-US"}

[2    6    1    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24]{lang="EN-US"}

[2    6    2    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24]{lang="EN-US"}

[2    6    3    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display fabric utilization]{lang="EN-US"}]{#struct_0_55199_x9544_70088312}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x610098194}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_1131999904}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x918666191}

[[Chs]{lang="EN-US"}]{#struct_0_55199_x9544_1647819804}

[[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_55199_x9544_366238784}[，无实际意义（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_55199_x9544_x1180337375}[的缩写，为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_x2055073045}

[[接口板所在的槽位号]{style="font-family:宋体"}]{#struct_0_55199_x9544_1132589728}

[[Chan]{lang="EN-US"}]{#struct_0_55199_x9544_101074099}

[[Channel]{lang="EN-US"}]{#struct_0_55199_x9544_1556022461}[的缩写，通道号]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_55199_x9544_108215264}

[[通道的速率]{style="font-family:宋体"}]{#struct_0_55199_x9544_721784353}

[[Input]{lang="EN-US"}]{#struct_0_55199_x9544_1132655264}

[[入方向的统计数据]{style="font-family:宋体"}]{#struct_0_55199_x9544_141741516}

[[Output]{lang="EN-US"}]{#struct_0_55199_x9544_x682532240}

[[出方向的统计数据]{style="font-family:宋体"}]{#struct_0_55199_x9544_1070160792}

[[Usage]{lang="EN-US"}]{#struct_0_55199_x9544_1090335969}

[[通道利用率]{style="font-family:宋体"}]{#struct_0_55199_x9544_1132065441}

[[Peak]{lang="EN-US"}]{#struct_0_55199_x9544_x994259432}

[[通道利用率峰值以及峰值发生的时间]{style="font-family:宋体"}]{#struct_0_55199_x9544_1809124365}

[ ]{lang="EN-US"}

::: {#389579247 .myid}
[]{#_Toc404783086}[]{#struct_0_55199_x9544_x1794378183}

**设备管理 \-- 设备管理配置命令 \-- display fan**

------------------------------------------------------------------------

[**[display fan]{lang="EN-US"}**]{#struct_0_55199_x9544_x1001258191}[命令用来显示设备风扇的工作状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1132130977}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1341527295}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display fan]{lang="EN-US"}**[ \[ *fan-id \|* **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1060307915}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1742687120}[设备：]{style="font-family:宋体"}

[**[display fan]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ *fan-id* \] *\|* **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1263234347}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1604660014}[模式：（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display fan]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \[ *fan-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1107196125}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1866099534}[模式：（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display fan]{lang="EN-US"}**[ \[ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } \[ *fan-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1792057070}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1599389416}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1132196513}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_921775047}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1428824787}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x850304908}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x826466372}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_2018449447}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x986502815}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_405953430}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有风扇。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x2048374982}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示所有风扇。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1132262049}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[参数时，表示所有风扇。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_x2047523014}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上风扇的状态信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[virtual-chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[在虚拟框中的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[参数时，表示所有风扇。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[fan-id]{lang="EN-US"}*]{#struct_0_55199_x9544_1692204695}[：表示设备内置风扇的编号，是否支持本参数以及本参数的取值范围与设备的型号有关，请以设备的实际情况为准。不指定该参数时，表示指定位置的所有风扇。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_55199_x9544_800271187}[：显示设备内置风扇的详细信息。不指定该参数时，显示设备内置风扇的简要信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_920891908}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x497591226}[显示设备上所有风扇的工作状态。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准，此处略）]{style="font-family:宋体"}

[[\<Sysname\> display fan]{lang="EN-US"}]{#struct_0_55199_x9544_1484435817}
:::

::::: {#2073671768 .myid}
[]{#_Toc404783087}[]{#struct_0_55199_x9544_974711295}[]{#_Toc387411219}

**设备管理 \-- 设备管理配置命令 \-- display lpu-type**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image004.png){width="60" height="23"}]{lang="EN-US"}]{#struct_0_55199_x9544_x2138146677}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x1121180307}
:::

**[ ]{lang="EN-US"}**

[**[display lpu-type]{lang="EN-US"}**]{#struct_0_55199_x9544_x1948278917}[命令用来显示设备支持的接口板类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x979380385}

[**[display lpu-type]{lang="EN-US"}**]{#struct_0_55199_x9544_443941414}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2005872180}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_974711296}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2138146674}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1607703048}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x2114670871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x155426474}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1416022292}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1414120211}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_621872391}[显示设备支持的接口板类型。]{style="font-family:宋体"}

[[\<Sysname\> display lpu-type]{lang="EN-US"}]{#struct_0_55199_x9544_1994688711}

[Current LPU type is E series.]{lang="EN-US"}

[LPU type for the next startup is F series.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2073840750}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lpu-type]{lang="EN-US"}**]{#struct_0_55199_x9544_974711297}
:::::

::: {#-1938388534 .myid}
[]{#_Toc300730516}[]{#_Toc300730279}[]{#_Toc263066887}[]{#_Toc206560271}[]{#_Toc327350476}[]{#_Toc327178126}[]{#_Toc404783088}[]{#struct_0_55199_x9544_1482341876}[]{#_Toc320803325}[]{#_Toc316392148}[]{#_Toc295398667}[]{#_Toc209953951}[]{#_Toc211937228}[]{#_Toc211937708}[]{#_Toc213494856}[]{#_Toc209953952}[]{#_Toc211937229}[]{#_Toc211937709}[]{#_Toc213494857}[]{#_Toc209953957}[]{#_Toc211937234}[]{#_Toc211937714}[]{#_Toc213494862}[]{#_Toc209953959}[]{#_Toc211937236}[]{#_Toc211937716}[]{#_Toc213494864}[]{#_Toc209953960}[]{#_Toc211937237}[]{#_Toc211937717}[]{#_Toc213494865}

**设备管理 \-- 设备管理配置命令 \-- display memory**

------------------------------------------------------------------------

[**[display memory]{lang="EN-US"}**]{#struct_0_55199_x9544_x1095570385}[命令用来显示内存使用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1131803297}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x133134155}

[**[display memory]{lang="EN-US"}**]{#struct_0_55199_x9544_947064737}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x1947559571}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display memory]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_648285996}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_885729974}[模式：]{style="font-family:宋体"}

[**[display memory ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_735932181}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_819762832}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1131868833}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x126830356}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1810103849}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x838925604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_462461937}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_25049366}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1117846777}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x195760808}[：表示单板所在的槽位号，不指定时显示当前所有单板的内存使用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1131934369}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定时显示当前所有成员设备的内存使用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1060848010}[：表示指定成员设备上的指定单板，不指定时显示当前所有单板的内存使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1822493073}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1757303317}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1111943744}[显示设备的内存使用情况。]{style="font-family:宋体"}

[[\<Sysname\> display memory]{lang="EN-US"}]{#struct_0_55199_x9544_x993876431}

[The statistics about memory is measured in KB:]{lang="EN-US"}

[Slot 0:]{lang="EN-US"}

[             Total      Used      Free    Shared   Buffers    Cached   FreeRatio]{lang="EN-US"}

[Mem:        507980    154896    353084         0       488     54488       69.5%]{lang="EN-US"}

[-/+ Buffers/Cache:     99920    408060]{lang="EN-US"}

[Swap:           0         0         0]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display memory]{lang="EN-US"}]{#struct_0_55199_x9544_1131999905}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x613972274}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x918731727}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_914775591}

[[The statistics about memory is measured in KB:]{lang="EN-US"}]{#struct_0_55199_x9544_x152501331}

[[系统内存使用情况，以下统计信息均以]{style="font-family:宋体"}[KB]{lang="EN-US"}]{#struct_0_55199_x9544_244022734}[为单位]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_x206245880}

[[为固定值]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_55199_x9544_1132589729}[，暂无实际意义（集中式设备）]{style="font-family:宋体"}

[[单板所在的槽位号（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_55199_x9544_101139635}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_730721915}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis x Slot x]{lang="EN-US"}]{#struct_0_55199_x9544_1430528920}

[[单板所在的槽位号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1351924046}[模式）]{style="font-family:宋体"}

[[Mem]{lang="EN-US"}]{#struct_0_55199_x9544_x1704963710}

[[内存使用信息]{style="font-family:宋体"}]{#struct_0_55199_x9544_1132655265}

[[Total]{lang="EN-US"}]{#struct_0_55199_x9544_141675980}

[[系统可分配的物理内存的大小]{style="font-family:宋体"}]{#struct_0_55199_x9544_1677014273}

[[设备总物理内存分为不可分配物理内存和可分配物理内存。其中，不可分配物理内存用于内核代码段存储、内核管理开销以及]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_55199_x9544_x1283127431}[功能运行等；可分配物理内存用于支撑业务模块的运行、文件存储等操作。不可分配内存的大小由设备根据系统运行需要自动计算划分，可分配物理内存的大小等于设备总物理内存减去不可分配内存的大小]{style="font-family:宋体"}

[[Used]{lang="EN-US"}]{#struct_0_55199_x9544_x158578617}

[[整个系统已用的物理内存大小]{style="font-family:宋体"}]{#struct_0_55199_x9544_1132065442}

[[Free]{lang="EN-US"}]{#struct_0_55199_x9544_x994193896}

[[整个系统可用的物理内存大小]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1267349558}

[[Shared]{lang="EN-US"}]{#struct_0_55199_x9544_x77158672}

[[多个进程共享的物理内存总额]{style="font-family:宋体"}]{#struct_0_55199_x9544_839106051}

[[Buffers]{lang="EN-US"}]{#struct_0_55199_x9544_1132130978}

[[已使用的文件缓冲区的大小]{style="font-family:宋体"}]{#struct_0_55199_x9544_1340937471}

[[Cached]{lang="EN-US"}]{#struct_0_55199_x9544_1297415083}

[[高速缓冲寄存器已使用的内存大小]{style="font-family:宋体"}]{#struct_0_55199_x9544_56997378}

[[FreeRatio]{lang="EN-US"}]{#struct_0_55199_x9544_1132196514}

[[整个系统物理内存的空闲率]{style="font-family:宋体"}]{#struct_0_55199_x9544_921971655}

[[-/+ buffers/cache]{lang="EN-US"}]{#struct_0_55199_x9544_859704327}

[[-/+ Buffers/Cache:used = Mem:Used -- Mem:Buffers -- Mem:Cached]{lang="EN-US"}]{#struct_0_55199_x9544_1132655266}[，表示应用程序已用的物理内存大小]{style="font-family:宋体"}

[[-/+ Buffers/Cache:free = Mem:Free + Mem:Buffers + Mem:Cached]{lang="EN-US"}]{#struct_0_55199_x9544_1131934371}[，表示应用程序可用的物理内存大小]{style="font-family:宋体"}

[[Swap]{lang="EN-US"}]{#struct_0_55199_x9544_1061372299}

[[交换分区的使用信息]{style="font-family:宋体"}]{#struct_0_55199_x9544_1131999907}

[ ]{lang="EN-US"}

::: {#-799356652 .myid}
[]{#_Toc404783089}[]{#struct_0_55199_x9544_x918600655}

**设备管理 \-- 设备管理配置命令 \-- display memory-threshold**

------------------------------------------------------------------------

[**[display memory-threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_1298911970}[命令用来显示内存告警门限相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1413538542}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_300591446}

[**[display memory-threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_x431559501}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x199617871}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display memory-threshold ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1132589731}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_100615348}[模式：]{style="font-family:宋体"}

[**[display memory-threshold ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1715949784}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_544767916}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_941575437}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2125400769}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1204699003}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x423696819}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1132655267}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_141807052}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x843184857}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_894516828}[：表示指定成员设备上的指定单板。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1822624145}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1232536158}

[[当设备已经使用的物理内存大小超过内存某个告警门限阈值时，系统会认为发生了一次该类型内存异常，并记录第一次、最近一次发生异常的时间，以及这段时间内发生的该类异常的次数。如果想了解该类异常的详细情况，请查看日志信息，可按日志摘要关键字"]{style="font-family:宋体"}[MEM_EXCEED_THRESHOLD]{lang="EN-US"}]{#struct_0_55199_x9544_1778854719}["或"]{style="font-family:宋体"}[MEM_BELOW_THRESHOLD]{lang="EN-US"}["进行搜索。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x116259221}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1596817917}[显示内存告警门限相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display memory-threshold]{lang="EN-US"}]{#struct_0_55199_x9544_x1596752381}

[Memory usage threshold: 100%]{lang="EN-US"}

[Free memory threshold:]{lang="EN-US"}

[     Minor: 64M]{lang="EN-US"}

[     Severe: 48M]{lang="EN-US"}

[     Critical: 32M]{lang="EN-US"}

[     Normal: 96M]{lang="EN-US"}

[Current memory state: Normal]{lang="EN-US"}

[Event statistics:]{lang="EN-US"}

[ \[Back to normal state\]]{lang="EN-US"}

[    First notification: 2012-5-15 09:21:35.546]{lang="EN-US"}

[    Latest notification: 2012-5-15 09:21:35.546]{lang="EN-US"}

[    Total number of notifications sent: 1]{lang="EN-US"}

[ \[Enter minor low-memory state\]]{lang="EN-US"}

[    First notification at: 2012-5-15 09:07:05.941]{lang="EN-US"}

[    Latest  notification at: 2012-5-15 09:07:05.941]{lang="EN-US"}

[    Total number of notifications sent: 1]{lang="EN-US"}

[ \[Back to minor low-memory state\]]{lang="EN-US"}

[    First notification at: 0.0]{lang="EN-US"}

[    Latest  notification at: 0.0]{lang="EN-US"}

[    Total number of notifications sent: 0]{lang="EN-US"}

[ \[Enter severe low-memory state\]]{lang="EN-US"}

[    First notification at: 0.0]{lang="EN-US"}

[    Latest  notification at: 0.0]{lang="EN-US"}

[    Total number of notifications sent: 0]{lang="EN-US"}

[ \[Back to severe low-memory state\]]{lang="EN-US"}

[    First notification at: 0.0]{lang="EN-US"}

[    Latest  notification at: 0.0]{lang="EN-US"}

[    Total number of notifications sent: 0]{lang="EN-US"}

[ \[Enter critical low-memory state\]]{lang="EN-US"}

[    First notification at: 0.0]{lang="EN-US"}

[    Latest  notification at: 0.0]{lang="EN-US"}

[    Total number of notifications sent: 0]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display memory-threshold]{lang="EN-US"}]{#struct_0_55199_x9544_x2099949801}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x574224914}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1164359087}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_1832171595}

[[Memory usage threshold]{lang="EN-US"}]{#struct_0_55199_x9544_x87846924}

[[内存利用率阈值]{style="font-family:宋体"}]{#struct_0_55199_x9544_1478237017}

[[Free memory threshold]{lang="EN-US"}]{#struct_0_55199_x9544_x1596686845}

[[         Minor:]{lang="EN-US"}]{#struct_0_55199_x9544_1519912419}

[[         Severe:]{lang="EN-US"}]{#struct_0_55199_x9544_515316422}

[[         Critical:]{lang="EN-US"}]{#struct_0_55199_x9544_x1679539840}

[[         Normal:]{lang="EN-US"}]{#struct_0_55199_x9544_x1810727314}

[[剩余内存门限阈值：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1090051790}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Minor]{lang="EN-US"}]{#struct_0_55199_x9544_x1596621309}[：一级告警门限，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Severe]{lang="EN-US"}]{#struct_0_55199_x9544_135759014}[：二级告警门限，单位为]{lang="EN-US" style="font-family:宋体"}[MB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_55199_x9544_x932567958}[：三级告警门限，单位为]{lang="EN-US" style="font-family:宋体"}[MB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_55199_x9544_x2056551256}[：恢复到正常状态的阈值，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[Current memory state]{lang="EN-US"}]{#struct_0_55199_x9544_2145864523}

[[系统当前内存使用状态：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1597080061}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_55199_x9544_x1069272240}[：正常状态]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Minor]{lang="EN-US"}]{#struct_0_55199_x9544_955994690}[：一级告警门限状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Severe]{lang="EN-US"}]{#struct_0_55199_x9544_1886816351}[：二级告警门限状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_55199_x9544_x1392156765}[：三级告警门限状态]{lang="EN-US" style="font-family:宋体"}

[[Event statistics:]{lang="EN-US"}]{#struct_0_55199_x9544_1492193765}

[[门限事件统计信息，事件分为：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1597014525}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Back to normal state]{lang="EN-US"}]{#struct_0_55199_x9544_474366288}[：内存恢复]{lang="EN-US" style="font-family:
  宋体"}[到]{style="font-family:宋体"}[正常]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enter minor low-memory state]{lang="EN-US"}]{#struct_0_55199_x9544_890390106}[：进入一级告警门限状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Back to minor low-memory state]{lang="EN-US"}]{#struct_0_55199_x9544_x770919621}[：恢复到一级告警门限状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enter severe low-memory state]{lang="EN-US"}]{#struct_0_55199_x9544_x1596948989}[：进入二级告警门限状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Back to severe low-memory state]{lang="EN-US"}]{#struct_0_55199_x9544_x93274518}[：恢复到二级告警门限状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enter critical low-memory state]{lang="EN-US"}]{#struct_0_55199_x9544_x1691706441}[：进入三级告警门限状态]{lang="EN-US" style="font-family:宋体"}

[[First notification at]{lang="EN-US"}]{#struct_0_55199_x9544_x1633725037}

[[事件第一次发生的时间，格式]{style="font-family:宋体"}[yyyy-mm-dd hh:mm:ss.msec]{lang="EN-US"}]{#struct_0_55199_x9544_1791261817}

[[Latest  notification at]{lang="EN-US"}]{#struct_0_55199_x9544_x1596883453}

[[事件最近一次发生的时间，格式]{style="font-family:宋体"}[yyyy-mm-dd hh:mm:ss.msec]{lang="EN-US"}]{#struct_0_55199_x9544_1911900733}

[[Total number of notification send]{lang="EN-US"}]{#struct_0_55199_x9544_x892861443}

[[事件发生的总次数]{style="font-family:宋体"}]{#struct_0_55199_x9544_571585034}

[ ]{lang="EN-US"}

::::: {#1992752219 .myid}
[]{#_Toc404783090}[]{#struct_0_55199_x9544_x530189644}

**设备管理 \-- 设备管理配置命令 \-- display power**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1596293629}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x419119016}
:::

**[ ]{lang="EN-US"}**

[**[display power]{lang="EN-US"}**]{#struct_0_55199_x9544_284164696}[命令用来显示设备电源的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1397390327}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1804556498}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display power]{lang="EN-US"}**[ \[ *power*-*id* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1883698042}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1481299207}[设备：]{style="font-family:宋体"}

[**[display power]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ *power-id* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_948455287}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1596228093}[模式：（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display power]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \[ *power-id* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_457970359}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1218883109}[模式：（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display power]{lang="EN-US"}**[ \[ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } \[ *power-id* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_447325772}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1224119548}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1455967544}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2031219633}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1496631148}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_34747949}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1124534409}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1596817916}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x79913142}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1356968200}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有电源。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x2047457477}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示所有电源。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1387579586}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有电源。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_1509903146}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上电源的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[virtual-chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[在虚拟框中的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[参数时，表示所有电源。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[power]{lang="EN-US"}*[-*id*]{lang="EN-US"}]{#struct_0_55199_x9544_x1783675238}[：表示电源的编号，不同型号的设备的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示指定位置的所有电源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2005126384}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1200201495}[显示设备电源的状况。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准，此处略）]{style="font-family:宋体"}

[[\<Sysname\> display power]{lang="EN-US"}]{#struct_0_55199_x9544_x1596752380}
:::::

::::: {#871285355 .myid}
[]{#_Toc136403373}[]{#_Toc98563147}[]{#_Toc66782730}[]{#_Toc54490530}[]{#_Toc43175718}[]{#_Toc300730517}[]{#_Toc300730280}[]{#_Toc263066890}[]{#_Toc206560274}[]{#_Toc404783091}[]{#struct_0_55199_x9544_628933554}[]{#_Toc334689046}[]{#_Toc299977400}[]{#_Toc263066888}[]{#_Toc206560272}[]{#_Toc195417978}[]{#_Toc193873824}[]{#_Toc262048120}[]{#_Toc262216370}[]{#_Toc262473902}[]{#_Toc262048121}[]{#_Toc262216371}[]{#_Toc262473903}[]{#_Toc262048122}[]{#_Toc262216372}[]{#_Toc262473904}[]{#_Toc262048123}[]{#_Toc262216373}[]{#_Toc262473905}[]{#_Toc262048124}[]{#_Toc262216374}[]{#_Toc262473906}[]{#_Toc262048125}[]{#_Toc262216375}[]{#_Toc262473907}[]{#_Toc262048126}[]{#_Toc262216376}[]{#_Toc262473908}[]{#_Toc262048127}[]{#_Toc262216377}[]{#_Toc262473909}[]{#_Toc262048128}[]{#_Toc262216378}[]{#_Toc262473910}[]{#_Toc262048129}[]{#_Toc262216379}[]{#_Toc262473911}[]{#_Toc262048130}[]{#_Toc262216380}[]{#_Toc262473912}[]{#_Toc262048131}[]{#_Toc262216381}[]{#_Toc262473913}[]{#_Toc262048132}[]{#_Toc262216382}[]{#_Toc262473914}[]{#_Toc262048133}[]{#_Toc262216383}[]{#_Toc262473915}[]{#_Toc262048134}[]{#_Toc262216384}[]{#_Toc262473916}[]{#_Toc262048135}[]{#_Toc262216385}[]{#_Toc262473917}[]{#_Toc262048136}[]{#_Toc262216386}[]{#_Toc262473918}[]{#_Toc262048137}[]{#_Toc262216387}[]{#_Toc262473919}[]{#_Toc262048138}[]{#_Toc262216388}[]{#_Toc262473920}[]{#_Toc262048139}[]{#_Toc262216389}[]{#_Toc262473921}[]{#_Toc262048140}[]{#_Toc262216390}[]{#_Toc262473922}[]{#_Toc262048141}[]{#_Toc262216391}[]{#_Toc262473923}[]{#_Toc262048142}[]{#_Toc262216392}[]{#_Toc262473924}[]{#_Toc262048144}[]{#_Toc262216394}[]{#_Toc262473926}[]{#_Toc262048145}[]{#_Toc262216395}[]{#_Toc262473927}[]{#_Toc262048146}[]{#_Toc262216396}[]{#_Toc262473928}[]{#_Toc262048162}[]{#_Toc262216412}[]{#_Toc262473944}[]{#_Toc262048163}[]{#_Toc262216413}[]{#_Toc262473945}[]{#_Toc262048164}[]{#_Toc262216414}[]{#_Toc262473946}[]{#_Toc262048165}[]{#_Toc262216415}[]{#_Toc262473947}[]{#_Toc262048166}[]{#_Toc262216416}[]{#_Toc262473948}[]{#_Toc262048167}[]{#_Toc262216417}[]{#_Toc262473949}[]{#_Toc262048168}[]{#_Toc262216418}[]{#_Toc262473950}[]{#_Toc262048169}[]{#_Toc262216419}[]{#_Toc262473951}[]{#_Toc262048170}[]{#_Toc262216420}[]{#_Toc262473952}[]{#_Toc262048171}[]{#_Toc262216421}[]{#_Toc262473953}[]{#_Toc262048172}[]{#_Toc262216422}[]{#_Toc262473954}[]{#_Toc262048173}[]{#_Toc262216423}[]{#_Toc262473955}[]{#_Toc262048174}[]{#_Toc262216424}[]{#_Toc262473956}[]{#_Toc262048175}[]{#_Toc262216425}[]{#_Toc262473957}[]{#_Toc262048176}[]{#_Toc262216426}[]{#_Toc262473958}[]{#_Toc262048177}[]{#_Toc262216427}[]{#_Toc262473959}[]{#_Toc262048178}[]{#_Toc262216428}[]{#_Toc262473960}[]{#_Toc262048179}[]{#_Toc262216429}[]{#_Toc262473961}[]{#_Toc262048180}[]{#_Toc262216430}[]{#_Toc262473962}[]{#_Toc262048181}[]{#_Toc262216431}[]{#_Toc262473963}[]{#_Toc262048182}[]{#_Toc262216432}[]{#_Toc262473964}[]{#_Toc262048183}[]{#_Toc262216433}[]{#_Toc262473965}[]{#_Toc262048188}[]{#_Toc262216438}[]{#_Toc262473970}[]{#_Toc262048195}[]{#_Toc262216445}[]{#_Toc262473977}[]{#_Toc262048196}[]{#_Toc262216446}[]{#_Toc262473978}[]{#_Toc262048200}[]{#_Toc262216450}[]{#_Toc262473982}[]{#_Toc262048203}[]{#_Toc262216453}[]{#_Toc262473985}[]{#_Toc262048204}[]{#_Toc262216454}[]{#_Toc262473986}[]{#_Toc262048205}[]{#_Toc262216455}[]{#_Toc262473987}[]{#_Toc262048206}[]{#_Toc262216456}[]{#_Toc262473988}[]{#_Toc262048207}[]{#_Toc262216457}[]{#_Toc262473989}[]{#_Toc262048208}[]{#_Toc262216458}[]{#_Toc262473990}[]{#_Toc262048252}[]{#_Toc262216502}[]{#_Toc262474034}[]{#_Toc267468612}[]{#_Toc267469016}[]{#_Toc267486015}[]{#_Toc267468614}[]{#_Toc267469018}[]{#_Toc267486017}[]{#_Toc267468615}[]{#_Toc267469019}[]{#_Toc267486018}[]{#_Toc267468616}[]{#_Toc267469020}[]{#_Toc267486019}[]{#_Toc267468617}[]{#_Toc267469021}[]{#_Toc267486020}[]{#_Toc267468618}[]{#_Toc267469022}[]{#_Toc267486021}[]{#_Toc267468619}[]{#_Toc267469023}[]{#_Toc267486022}[]{#_Toc267468620}[]{#_Toc267469024}[]{#_Toc267486023}[]{#_Toc267468621}[]{#_Toc267469025}[]{#_Toc267486024}[]{#_Toc267468622}[]{#_Toc267469026}[]{#_Toc267486025}[]{#_Toc267468623}[]{#_Toc267469027}[]{#_Toc267486026}[]{#_Toc267468624}[]{#_Toc267469028}[]{#_Toc267486027}[]{#_Toc267468625}[]{#_Toc267469029}[]{#_Toc267486028}[]{#_Toc267468626}[]{#_Toc267469030}[]{#_Toc267486029}[]{#_Toc267468627}[]{#_Toc267469031}[]{#_Toc267486030}[]{#_Toc267468628}[]{#_Toc267469032}[]{#_Toc267486031}[]{#_Toc267468629}[]{#_Toc267469033}[]{#_Toc267486032}[]{#_Toc267468630}[]{#_Toc267469034}[]{#_Toc267486033}[]{#_Toc267468631}[]{#_Toc267469035}[]{#_Toc267486034}[]{#_Toc267468632}[]{#_Toc267469036}[]{#_Toc267486035}[]{#_Toc267468633}[]{#_Toc267469037}[]{#_Toc267486036}[]{#_Toc267468634}[]{#_Toc267469038}[]{#_Toc267486037}[]{#_Toc267468636}[]{#_Toc267469040}[]{#_Toc267486039}[]{#_Toc267468639}[]{#_Toc267469043}[]{#_Toc267486042}[]{#_Toc267468646}[]{#_Toc267469050}[]{#_Toc267486049}[]{#_Toc267468647}[]{#_Toc267469051}[]{#_Toc267486050}[]{#_Toc267468649}[]{#_Toc267469053}[]{#_Toc267486052}[]{#_Toc267468657}[]{#_Toc267469061}[]{#_Toc267486060}

**设备管理 \-- 设备管理配置命令 \-- display power-supply**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image003.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1710989397}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x278580159}
:::

**[ ]{lang="EN-US"}**

[**[display power-supply]{lang="EN-US"}**]{#struct_0_55199_x9544_x802946459}[命令用来显示设备电源的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_608754426}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1232612238}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display power-supply ]{lang="EN-US"}**[\[ **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_2143813132}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1876510519}[设备：]{style="font-family:宋体"}

[**[display power-supply ]{lang="EN-US"}**[\[ **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_1875724086}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1596686844}[模式：]{style="font-family:宋体"}

[**[display power-supply]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1208970936}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1628761865}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_564990740}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x880219453}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x176221178}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_118656315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2090335695}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1875855158}[：显示指定成员设备上电源的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x750485359}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上电源的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1596621308}[：显示指定成员设备上电源的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_769502086}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上电源的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。不指定该参数时，表示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_55199_x9544_1701842955}[：显示电源的详细信息。不指定该参数时，显示电源的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_496811701}

[]{#_Toc174438921}[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x2077004124}[显示电源详细信息（该显示信息与设备的型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> display power-supply verbose]{lang="EN-US"}]{#struct_0_55199_x9544_1467891942}
:::::

::::: {#791749674 .myid}
[]{#_Toc404783092}[]{#struct_0_55199_x9544_1809827683}

**设备管理 \-- 设备管理配置命令 \-- display rps**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1345552571}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1417370104}
:::

**[ ]{lang="EN-US"}**

[**[display rps]{lang="EN-US"}**]{#struct_0_55199_x9544_x275708600}[命令用来显示设备]{style="font-family:宋体"}[RPS]{lang="EN-US"}[（]{style="font-family:宋体"}[Redundant Power System]{lang="EN-US"}[，冗余电源系统）的状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1597014524}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x1091717653}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display rps]{lang="EN-US"}**[ \[ *rps*-*id* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x905816022}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x2070226146}[设备：]{style="font-family:宋体"}

[**[display rps]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ *rps-id* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1109714659}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x347200832}[模式：（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display rps]{lang="EN-US"}**[ \[ **chassis** *chassis-number* \[ *rps-id* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1654198441}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_842987151}[模式：（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[display rps]{lang="EN-US"}**[ \[ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } \[ *rps-id* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_701088525}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x47560069}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1596948988}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1472809423}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_338827918}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x821936519}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_483137672}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x2135812415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1696694575}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1316314124}[：表示单板所在的槽位号。不指定该参数时，表示所有]{style="font-family:宋体"}[RPS]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1596883452}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x2048309444}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示所有]{style="font-family:宋体"}[RPS]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x816982622}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有]{style="font-family:宋体"}[RPS]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_x1206661977}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上风扇的状态信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[virtual-chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[在虚拟框中的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[参数时，表示所有风扇。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[rps]{lang="EN-US"}*[-*id*]{lang="EN-US"}]{#struct_0_55199_x9544_2058676682}[：表示设备]{style="font-family:宋体"}[RPS]{lang="EN-US"}[的编号，不同型号的设备的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示指定位置的所有]{style="font-family:宋体"}[RPS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1239702824}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_916323826}[显示设备]{style="font-family:宋体"}[RPS]{lang="EN-US"}[的状态信息。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准，此处略）]{style="font-family:宋体"}

[[\<Sysname\> display rps]{lang="EN-US"}]{#struct_0_55199_x9544_x1289958208}
:::::

::::: {#-650108376 .myid}
[]{#_Toc309658908}[]{#_Toc296584680}[]{#_Toc295572807}[]{#_Toc294103500}[]{#_Toc404783093}[]{#struct_0_55199_x9544_429285715}[]{#_Toc311530754}[]{#_Toc263066891}[]{#_Toc230516697}[]{#_Toc230518610}[]{#_Toc230516699}[]{#_Toc230518612}[]{#_Toc230516700}[]{#_Toc230518613}[]{#_Toc230516701}[]{#_Toc230518614}[]{#_Toc230516702}[]{#_Toc230518615}[]{#_Toc230516703}[]{#_Toc230518616}[]{#_Toc230516704}[]{#_Toc230518617}[]{#_Toc230516705}[]{#_Toc230518618}[]{#_Toc230516706}[]{#_Toc230518619}[]{#_Toc230516707}[]{#_Toc230518620}[]{#_Toc230516708}[]{#_Toc230518621}[]{#_Toc230516712}[]{#_Toc230518625}[]{#_Toc230516713}[]{#_Toc230518626}[]{#_Toc230516714}[]{#_Toc230518627}[]{#_Toc230516727}[]{#_Toc230518640}

**设备管理 \-- 设备管理配置命令 \-- display save-power**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 20 width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x94259494}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x1596293628}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **save-power**]{lang="EN-US"}]{#struct_0_55199_x9544_x1985202957}[命令用来显示节能功能相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_879484601}

[**[display save-power]{lang="EN-US"}**]{#struct_0_55199_x9544_66346098}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_989279408}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_2129217736}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x12995967}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1596228092}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_2024054300}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x672181005}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1293258080}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x440093681}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x995779641}[显示节能功能是否使能以及所处的节能状态。]{style="font-family:宋体"}

[[\<Sysname\> display save-power]{lang="EN-US"}]{#struct_0_55199_x9544_x1315369775}

[Save-power state: enable(wake)]{lang="EN-US"}

[Save-power delay-time: 30(s)]{lang="EN-US"}

[Save-power delay-time remained: 5(s)]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display save-power]{lang="EN-US"}]{#struct_0_55199_x9544_x1596817915}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x576762642}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_323371385}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1711177380}

[[Save-power state]{lang="EN-US"}]{#struct_0_55199_x9544_x1263956461}

[[节能功能的状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_55199_x9544_2079374267}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_55199_x9544_494598733}[：表示没有使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled(wake)]{lang="EN-US"}]{#struct_0_55199_x9544_x1596752379}[：表示已经使能，且处于节能唤醒状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled(sleep)]{lang="EN-US"}]{#struct_0_55199_x9544_x1744702481}[：表示已经使能，且处于节能休眠状态]{lang="EN-US" style="font-family:宋体"}

[[Save-power delay-time]{lang="EN-US"}]{#struct_0_55199_x9544_999835631}

[[配置的设备从节能唤醒状态切换到节能休眠状态的时间间隔（只有节能功能使能时，才会显示该信息）]{style="font-family:宋体"}]{#struct_0_55199_x9544_x478650353}

[[Save-power delay-time remained]{lang="EN-US"}]{#struct_0_55199_x9544_x1304362300}

[[设备从节能唤醒状态切换到节能休眠状态的剩余时间间隔（只有节能功能的状态为"]{style="font-family:宋体"}[enabled(wake)]{lang="EN-US"}]{#struct_0_55199_x9544_x478632465}["时才显示该信息）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-936343098 .myid}
[]{#_Toc404783094}[]{#struct_0_55199_x9544_x1596686843}

**设备管理 \-- 设备管理配置命令 \-- display scheduler job**

------------------------------------------------------------------------

[**[display scheduler job]{lang="EN-US"}**]{#struct_0_55199_x9544_x1968485823}[命令用来查看]{style="font-family:宋体"}[Job]{lang="EN-US"}[的配置信息，包括]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称和分配的命令。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1901462188}

[**[display scheduler job ]{lang="EN-US"}**[\[ *job-name* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1273448130}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1882943572}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_569807446}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1563892242}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x76858371}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1596621307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x314579680}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1050803517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2033306430}

[*[job-name]{lang="EN-US"}*]{#struct_0_55199_x9544_1129848514}[：]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，则显示所有]{style="font-family:宋体"}[Job]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1608132689}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1796417109}[查看所有]{style="font-family:宋体"}[Job]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display scheduler job]{lang="EN-US"}]{#struct_0_55199_x9544_x1597080059}

[Job name: saveconfig]{lang="EN-US"}

[ copy startup.cfg backup.cfg]{lang="EN-US"}

[ ]{lang="EN-US"}

[Job name: backupconfig]{lang="EN-US"}

[ ]{lang="EN-US"}

[Job name: creat-VLAN100]{lang="EN-US"}

[ system-view]{lang="EN-US"}

[ vlan 100]{lang="EN-US"}

[[以上显示信息表明，设备当前配置了]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_55199_x9544_x712845272}[个]{style="font-family:宋体"}[Job]{lang="EN-US"}[，分别显示了]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称，以及为]{style="font-family:宋体"}[Job]{lang="EN-US"}[分配的命令（如果没有为]{style="font-family:宋体"}[Job]{lang="EN-US"}[分配命令，则只显示]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称），不同]{style="font-family:宋体"}[Job]{lang="EN-US"}[间用空行分隔。]{style="font-family:宋体"}
:::

::: {#673588799 .myid}
[]{#_Toc404783095}[]{#struct_0_55199_x9544_358822128}[]{#_Toc309658909}[]{#_Toc296584684}[]{#_Toc295572811}

**设备管理 \-- 设备管理配置命令 \-- display scheduler logfile**

------------------------------------------------------------------------

[**[display scheduler logfile]{lang="EN-US"}**]{#struct_0_55199_x9544_967697232}[命令用来显示已执行的]{style="font-family:
宋体"}[Job]{lang="EN-US"}[的日志信息，包括]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称、对应的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的名称、执行时间以及执行结果]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x112509649}

[**[display scheduler logfile]{lang="EN-US"}**]{#struct_0_55199_x9544_x1938947393}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2133474892}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1597014523}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x688433126}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1700540336}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_408315931}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1592380976}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1657513757}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1731737961}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1998752998}[显示]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[日志文件的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display scheduler logfile]{lang="EN-US"}]{#struct_0_55199_x9544_x1596948987}

[Logfile Size: 1902 Bytes.]{lang="EN-US"}

[ ]{lang="EN-US"}

[[Job name        : shutdown]{lang="EN-US"}]{.TerminalDisplayChar}

[[Schedule name   : shutdown]{lang="EN-US"}]{.TerminalDisplayChar}

[[Execution time  : Tue Dec 27 10:44:42 2011]{lang="EN-US"}]{.TerminalDisplayChar}

[[Completion time : Tue Dec 27 10:44:47 2011]{lang="EN-US"}]{.TerminalDisplayChar}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Job output \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{.TerminalDisplayChar}

[[\<]{lang="EN-US"}]{.TerminalDisplayChar}[Sysname[\>system-view]{.TerminalDisplayChar}]{lang="EN-US"}

[[System View: return to User View with Ctrl+Z.]{lang="EN-US"}]{.TerminalDisplayChar}

[[\[]{lang="EN-US"}]{.TerminalDisplayChar}[Sysname[\]interface rang gigabitethernet 1/0/1 to gigabitethernet 1/0/3]{.TerminalDisplayChar}]{lang="EN-US"}

[[\[]{lang="EN-US"}]{.TerminalDisplayChar}[Sysname[-if-range\]shutdown]{.TerminalDisplayChar}]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display scheduler logfile]{lang="EN-US"}]{#struct_0_55199_x9544_357064176}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x576655570}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2115454927}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x712495920}

[[Logfile Size]{lang="EN-US"}]{#struct_0_55199_x9544_x1596883451}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x1220267149}[日志文件的大小，单位为字节]{style="font-family:宋体"}

[[Job name]{lang="EN-US"}]{#struct_0_55199_x9544_1481624747}

[[Job]{lang="EN-US"}]{#struct_0_55199_x9544_2107394456}[的名称]{style="font-family:宋体"}

[[Schedule name]{lang="EN-US"}]{#struct_0_55199_x9544_x1925191379}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x1596293627}[的名称]{style="font-family:宋体"}

[[Execution time]{lang="EN-US"}]{#struct_0_55199_x9544_x1581918430}

[[开始执行]{style="font-family:宋体"}[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x854924584}[的时间]{style="font-family:宋体"}

[[Completion time]{lang="EN-US"}]{#struct_0_55199_x9544_1998528650}

[[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x794053841}[执行结束的时间（没有调度的或者没有分配命令的]{style="font-family:宋体"}[Job]{lang="EN-US"}[，均不会显示该信息）]{style="font-family:宋体"}

[[Job output]{lang="EN-US"}]{#struct_0_55199_x9544_2071250795}

[[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x1596228091}[中的命令执行时的输出信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x704829055}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset scheduler logfile]{lang="EN-US"}**]{#struct_0_55199_x9544_x1861743787}

::: {#-591676548 .myid}
[]{#_Toc136403374}[]{#_Toc120764584}[]{#_Toc117076253}[]{#_Toc404783096}[]{#struct_0_55199_x9544_x1346602069}[]{#_Toc309658910}[]{#_Toc296584679}[]{#_Toc295572806}[]{#_Toc294103499}

**设备管理 \-- 设备管理配置命令 \-- display scheduler reboot**

------------------------------------------------------------------------

[**[display scheduler reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_2103412201}[命令用来查看定时重启功能的相关配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1255002441}

[**[display scheduler reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_383555172}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1596817914}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1242712556}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1544722175}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_110713399}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_1587916585}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1153654664}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x922660259}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1596752378}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_984180874}[查看]{style="font-family:宋体"}[定时重启功能的相关配置。]{style="font-family:宋体"}

[[\<Sysname\> display scheduler reboot]{lang="EN-US"}]{#struct_0_55199_x9544_2102724418}

[System will reboot at 16:32:00 05/23/2011 (in 1 hours and 39 minutes).]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1077275061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler reboot at]{lang="EN-US"}**]{#struct_0_55199_x9544_1080660764}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler reboot delay]{lang="EN-US"}**]{#struct_0_55199_x9544_x1107790038}
:::

::: {#-1197920269 .myid}
[]{#_Toc404783097}[]{#struct_0_55199_x9544_1194680598}[]{#_Toc309658911}[]{#_Toc296584681}[]{#_Toc295572808}[]{#_Toc294103501}

**设备管理 \-- 设备管理配置命令 \-- display scheduler schedule**

------------------------------------------------------------------------

[**[display scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x1864869774}[命令用来查看]{style="font-family:
宋体"}[Schedule]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1596686842}

[**[display scheduler schedule ]{lang="EN-US"}**[\[ *schedule-name* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x402401882}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_636249605}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1988620650}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1741785301}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1191380879}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1954064177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x88318451}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1596621306}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1251504261}

[*[schedule-name]{lang="EN-US"}*]{#struct_0_55199_x9544_x1108192772}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定该参数，则显示所有]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1308627070}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x643447202}[查看所有]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display scheduler schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x1597080058}

[Schedule name        : shutdown]{lang="EN-US"}

[Schedule type        : Run once after 0 hours 2 minutes]{lang="EN-US"}

[Start time           : Tue Dec 27 10:44:42 2011]{lang="EN-US"}

[Last execution time  : Tue Dec 27 10:44:42 2011]{lang="EN-US"}

[Last completion time : Tue Dec 27 10:44:47 2011]{lang="EN-US"}

[Execution counts     : 1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Job name                                          Last execution status]{lang="EN-US"}

[shutdown                                          Successful]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display scheduler schedule]{lang="EN-US"}]{#struct_0_55199_x9544_853238669}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x579505298}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1316862505}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x523745182}

[[Schedule name]{lang="EN-US"}]{#struct_0_55199_x9544_2096866225}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_1352938588}[的名称]{style="font-family:宋体"}

[[Schedule type]{lang="EN-US"}]{#struct_0_55199_x9544_x1597014522}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_2040450229}[的执行时间配置。如果没有为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[配置执行时间，则不会显示该信息]{style="font-family:宋体"}

[[Start time]{lang="EN-US"}]{#struct_0_55199_x9544_x1503578149}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_767681370}[第一次开始执行的时间。如果没有为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[配置执行时间，则不会显示该信息]{style="font-family:宋体"}

[[Last execution time]{lang="EN-US"}]{#struct_0_55199_x9544_x2089709277}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x1596948986}[上一开始执行的时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有为]{style="font-family:宋体"}]{#struct_0_55199_x9544_1923148117}[Schedule]{lang="EN-US"}[配置执行时间，则不会显示该信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果还没有执行，则显示]{lang="EN-US" style="font-family:宋体"}[Yet to be executed]{lang="EN-US"}]{#struct_0_55199_x9544_x1479616358}

[[Last completion time]{lang="EN-US"}]{#struct_0_55199_x9544_594000609}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x14715081}[上一次执行完成的时间。如果没有为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[配置执行时间，则不会显示该信息]{style="font-family:宋体"}

[[Execution counts]{lang="EN-US"}]{#struct_0_55199_x9544_x1596883450}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_345816792}[已经执行的次数。如果]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[还没有执行，则不会显示该信息]{style="font-family:宋体"}

[[Job name]{lang="EN-US"}]{#struct_0_55199_x9544_x1038291915}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_2089201632}[下关联的]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称]{style="font-family:宋体"}

[[Last execution status]{lang="EN-US"}]{#struct_0_55199_x9544_x2049319095}

[[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x1596293626}[上一次被执行的状态（]{style="font-family:宋体"}[Job]{lang="EN-US"}[下分配的命令是否执行以及执行结果，请通过]{style="font-family:宋体"}**[display scheduler logfile]{lang="EN-US"}**[命令查看）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successful]{lang="EN-US"}]{#struct_0_55199_x9544_1146964925}[：表示]{lang="EN-US" style="font-family:宋体"}[执行]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed]{lang="EN-US"}]{#struct_0_55199_x9544_x2036830143}[：表示]{lang="EN-US" style="font-family:宋体"}[执行]{style="font-family:宋体"}[失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting]{lang="EN-US"}]{#struct_0_55199_x9544_x1688986774}[：表示正在等待被执行]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In process]{lang="EN-US"}]{#struct_0_55199_x9544_x1596228090}[：]{lang="EN-US" style="font-family:宋体"}[表示正在执行]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-NA-]{lang="EN-US"}]{#struct_0_55199_x9544_861254886}[：表示还没有到执行时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#322554104 .myid}
[]{#_Toc300730519}[]{#_Toc300730282}[]{#_Toc263066896}[]{#_Toc206560278}[]{#_Toc404783098}[]{#struct_0_55199_x9544_x569523394}

**设备管理 \-- 设备管理配置命令 \-- display system-working-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x2057273604}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x956554132}
:::

[ ]{lang="EN-US"}

[**[display system-working-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_1291526141}[命令用来显示设备当前的工作模式。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1596817913}

[**[display system-working-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x839428029}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x785545363}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1485081559}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x121377776}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1419539357}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_75893605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_673801966}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1596752377}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1031235041}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_494390874}[显示设备当前的工作模式。]{style="font-family:宋体"}

[[\<Sysname\> display system-working-mode]{lang="EN-US"}]{#struct_0_55199_x9544_x1369583010}

[The current system working mode is standard.]{lang="EN-US"}

[The system working mode for next startup is standard.]{lang="EN-US"}
:::::

::::: {#975698249 .myid}
[]{#_Toc404783099}[]{#struct_0_55199_x9544_876356828}

**设备管理 \-- 设备管理配置命令 \-- display transceiver alarm**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 8 width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1733310417}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x1596686841}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[是否支持可插拔接口模块以及模块类型的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x805686409}
:::

**[ ]{lang="EN-US"}**

[**[display transceiver alarm]{lang="EN-US"}**]{#struct_0_55199_x9544_x1081222438}[命令用来显示可插拔接口模块的当前故障告警信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x467848466}

[**[display transceiver alarm interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1202684690}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1706300295}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2079623745}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_45524423}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1596621305}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1477379094}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_2027380010}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_742270651}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x437440416}

[**[interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1022157458}[：显示接口上插入的可插拔接口模块的当前故障告警信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号，如果不指定该参数，表示所有接口。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_230211371}

[[目前，使用的可插拔接口模块可能出现的故障告警信息见]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1408064916}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-18]{lang="EN-US"}](?975698249#_Ref170038014)[。如果没有故障，则显示为]{style="font-family:
宋体"}[None]{lang="EN-US"}[。]{style="font-family:
宋体"}

[]{#struct_0_55199_x9544_x1597080057}[[表1-18 ]{lang="EN-US"}[display transceiver alarm]{lang="EN-US"}]{#_Ref170038014}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x583379378}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_93723782}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x207650467}

[[SFP/SFP+/GBIC/SFF]{lang="EN-US"}]{#struct_0_55199_x9544_123466150}

[[RX loss of signal]{lang="EN-US"}]{#struct_0_55199_x9544_1235984446}

[[接收信号丢失]{style="font-family:宋体"}]{#struct_0_55199_x9544_75186572}

[[RX power high]{lang="EN-US"}]{#struct_0_55199_x9544_x1597014521}

[[接收光功率高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1851232540}

[[RX power low]{lang="EN-US"}]{#struct_0_55199_x9544_x1658690923}

[[接收光功率低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1263688871}

[[TX fault]{lang="EN-US"}]{#struct_0_55199_x9544_713199646}

[[发送错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1596948985}

[[TX bias high]{lang="EN-US"}]{#struct_0_55199_x9544_1519863590}

[[偏置电流高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x238377388}

[[TX bias low]{lang="EN-US"}]{#struct_0_55199_x9544_x207387543}

[[偏置电流低]{style="font-family:宋体"}]{#struct_0_55199_x9544_1670270678}

[[TX power high]{lang="EN-US"}]{#struct_0_55199_x9544_x1596883449}

[[发送光功率高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x864102325}

[[TX power low]{lang="EN-US"}]{#struct_0_55199_x9544_x1537078795}

[[发送光功率低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1193864848}

[[Temp high]{lang="EN-US"}]{#struct_0_55199_x9544_x1596293625}

[[温度高]{style="font-family:宋体"}]{#struct_0_55199_x9544_1550249452}

[[Temp low]{lang="EN-US"}]{#struct_0_55199_x9544_864769428}

[[温度低]{style="font-family:宋体"}]{#struct_0_55199_x9544_1617791688}

[[Voltage high]{lang="EN-US"}]{#struct_0_55199_x9544_x1596228089}

[[电压高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1061124951}

[[Voltage low]{lang="EN-US"}]{#struct_0_55199_x9544_1262843721}

[[电压低]{style="font-family:宋体"}]{#struct_0_55199_x9544_276934807}

[[Transceiver info I/O error]{lang="EN-US"}]{#struct_0_55199_x9544_x213016114}

[[模块信息读写错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1596817912}

[[Transceiver info checksum error]{lang="EN-US"}]{#struct_0_55199_x9544_1889455326}

[[模块信息校验和错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x804012553}

[[Transceiver type and port configuration mismatch]{lang="EN-US"}]{#struct_0_55199_x9544_x1596752376}

[[模块类型和端口配置不匹配]{style="font-family:宋体"}]{#struct_0_55199_x9544_x534848900}

[[Transceiver type not supported by port hardware]{lang="EN-US"}]{#struct_0_55199_x9544_1690666990}

[[端口不支持该模块类型]{style="font-family:宋体"}]{#struct_0_55199_x9544_574636457}

[[QSFP+]{lang="EN-US"}]{#struct_0_55199_x9544_x1266838078}

[[Temp high]{lang="EN-US"}]{#struct_0_55199_x9544_x1266838077}

[[温度高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x19147406}

[[Temp low]{lang="EN-US"}]{#struct_0_55199_x9544_x1266838076}

[[温度低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1585231347}

[[Voltage high]{lang="EN-US"}]{#struct_0_55199_x9544_x1266838075}

[[电压高]{style="font-family:宋体"}]{#struct_0_55199_x9544_1143652008}

[[Voltage low]{lang="EN-US"}]{#struct_0_55199_x9544_x1266838090}

[[电压低]{style="font-family:宋体"}]{#struct_0_55199_x9544_1547329751}

[[RX signal loss in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x1266838089}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_1456313790}[接收到的信号丢失]{style="font-family:宋体"}

[[TX fault in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_303679324}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_1456313791}[发送报文时出错]{style="font-family:宋体"}

[[TX signal loss in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_1456313792}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_303810396}[发送的信号丢失]{style="font-family:宋体"}

[[RX power high in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_1456313793}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_303875932}[接收到的光的功率太高]{style="font-family:宋体"}

[[RX power low in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_1456313794}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_1456313795}[接收到的光的功率太低]{style="font-family:宋体"}

[[TX bias high in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_304007004}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_1456313796}[的偏置电流高]{style="font-family:宋体"}

[[TX bias low in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_304072540}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_1456313797}[的偏置电流低]{style="font-family:宋体"}

[[Transceiver info I/O error]{lang="EN-US"}]{#struct_0_55199_x9544_304138076}

[[模块读写错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_1456313782}

[[Transceiver info checksum error]{lang="EN-US"}]{#struct_0_55199_x9544_1456313783}

[[模块信息校验和错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_303875931}

[[Transceiver type and port configuration mismatched]{lang="EN-US"}]{#struct_0_55199_x9544_x500001346}

[[模块类型和端口配置不匹配]{style="font-family:宋体"}]{#struct_0_55199_x9544_x650877676}

[[Transceiver type not supported]{lang="EN-US"}]{#struct_0_55199_x9544_x500001345}

[[端口不支持该类型的模块]{style="font-family:宋体"}]{#struct_0_55199_x9544_x650681068}

[[CFP]{lang="EN-US"}]{#struct_0_55199_x9544_x500001344}

[[TX jitter PLL unlocked]{lang="EN-US"}]{#struct_0_55199_x9544_x650746604}

[[发送]{style="font-family:宋体"}[Jitter PLL]{lang="EN-US"}]{#struct_0_55199_x9544_x500001343}[失锁]{style="font-family:宋体"}

[[TX CMU unlocked]{lang="EN-US"}]{#struct_0_55199_x9544_x500001342}

[[发送]{style="font-family:宋体"}[CMU]{lang="EN-US"}]{#struct_0_55199_x9544_x650615532}[失锁]{style="font-family:宋体"}

[[Overloaded]{lang="EN-US"}]{#struct_0_55199_x9544_x500001341}

[[负载过大]{style="font-family:宋体"}]{#struct_0_55199_x9544_x650418924}

[[Loss of REFCLK input]{lang="EN-US"}]{#struct_0_55199_x9544_x500001340}

[[缺乏参考时钟]{style="font-family:宋体"}]{#struct_0_55199_x9544_x500001339}

[[Channel signals out of alignment]{lang="EN-US"}]{#struct_0_55199_x9544_x500001354}

[[主机通道信号不对齐]{style="font-family:宋体"}]{#struct_0_55199_x9544_x650746603}

[[PLD or flash initialization error]{lang="EN-US"}]{#struct_0_55199_x9544_x500001353}

[[初始化错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_1073976766}

[[Power supply fault]{lang="EN-US"}]{#struct_0_55199_x9544_x1814958204}

[[电源错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_1073976767}

[[CFP checksum error]{lang="EN-US"}]{#struct_0_55199_x9544_1073976768}

[[校验和错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1814040700}

[[TX bias high]{lang="EN-US"}]{#struct_0_55199_x9544_1073976769}

[[偏置电流高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1813975164}

[[TX bias low]{lang="EN-US"}]{#struct_0_55199_x9544_1073976770}

[[偏置电流低]{style="font-family:宋体"}]{#struct_0_55199_x9544_1073976771}

[[Temp high]{lang="EN-US"}]{#struct_0_55199_x9544_x1814499451}

[[温度高]{style="font-family:宋体"}]{#struct_0_55199_x9544_1073976772}

[[Temp low]{lang="EN-US"}]{#struct_0_55199_x9544_1073976773}

[[温度低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1814630523}

[[Voltage high]{lang="EN-US"}]{#struct_0_55199_x9544_1073976758}

[[电压高]{style="font-family:宋体"}]{#struct_0_55199_x9544_1073976759}

[[Voltage low]{lang="EN-US"}]{#struct_0_55199_x9544_x1813975161}

[[电压低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x882338370}

[[RX signal loss in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x882338369}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_844406711}[接收到的信号丢失]{style="font-family:宋体"}

[[RX IC unlocked in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x882338368}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x882338367}[接收到的]{style="font-family:宋体"}[IC]{lang="EN-US"}[时钟失锁]{style="font-family:宋体"}

[[RX FIFO error in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_844013495}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x882338366}[接收到]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[TX signal loss in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_843947959}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x882338365}[发送的信号丢失]{style="font-family:宋体"}

[[TX IC unlocked in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x882338364}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_844079031}[发送的]{style="font-family:宋体"}[IC]{lang="EN-US"}[时钟失锁]{style="font-family:宋体"}

[[TX FIFO error in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x882338363}

[[主机通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x882338378}[的发送]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[出错]{style="font-family:宋体"}

[[TX IC unlocked in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_844341176}

[[主机通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x882338377}[发送的]{style="font-family:宋体"}[IC]{lang="EN-US"}[时钟失锁]{style="font-family:宋体"}

[[APD supply fault in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_691639742}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_1064393626}[出现]{style="font-family:宋体"}[APD]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[TEC fault in channel x]{lang="EN-US"}]{#struct_0_55199_x9544_691639743}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_691639744}[出现]{style="font-family:宋体"}[TEC]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Wavelength unlocked in channel *x*]{lang="EN-US"}]{#struct_0_55199_x9544_1064393628}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_691639745}[的光信号波长失锁]{style="font-family:宋体"}

[[RX power high in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_691639746}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_1064393630}[接收到的光的功率太高]{style="font-family:宋体"}

[[RX power low in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_691639747}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_691639748}[接收到的光的功率太低]{style="font-family:宋体"}

[[TX power high in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_1064393632}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_691639749}[发送的光的功率太高]{style="font-family:宋体"}

[[TX power low in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_691639734}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x1274258532}[发送的光的功率太低]{style="font-family:宋体"}

[[TX bias high in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_691639735}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x1264675394}[的偏置电流高]{style="font-family:宋体"}

[[TX bias low in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x1942262210}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x1264675393}[的偏置电流低]{style="font-family:宋体"}

[[Temp high in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x1264675392}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x779462796}[的温度高]{style="font-family:宋体"}

[[Temp low in lane *x*]{lang="EN-US"}]{#struct_0_55199_x9544_x1264675391}

[[通道]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_55199_x9544_x1264675390}[的温度低]{style="font-family:宋体"}

[[Transceiver info I/O error]{lang="EN-US"}]{#struct_0_55199_x9544_383336618}

[[模块读写错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1264675389}

[[Transceiver info checksum error]{lang="EN-US"}]{#struct_0_55199_x9544_x1264675388}

[[模块信息校验和错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_739501442}

[[Transceiver type and port configuration mismatched]{lang="EN-US"}]{#struct_0_55199_x9544_x1264675387}

[[模块类型和端口配置不匹配]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1264675402}

[[Transceiver type not supported ]{lang="EN-US"}]{#struct_0_55199_x9544_x779004041}

[[端口不支持该类型的模块]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1264675401}

[[XFP]{lang="EN-US"}]{#struct_0_55199_x9544_x1596686840}

[[RX loss of signal]{lang="EN-US"}]{#struct_0_55199_x9544_760397532}

[[接收信号丢失]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1871359407}

[[RX not ready]{lang="EN-US"}]{#struct_0_55199_x9544_x1596621304}

[[接收状态未就绪]{style="font-family:宋体"}]{#struct_0_55199_x9544_88704847}

[[RX CDR loss of lock]{lang="EN-US"}]{#struct_0_55199_x9544_x1252919173}

[[RX CDR]{lang="EN-US"}]{#struct_0_55199_x9544_246465687}[时钟失锁]{style="font-family:宋体"}

[[RX power high]{lang="EN-US"}]{#struct_0_55199_x9544_x1597080056}

[[接收光功率高]{style="font-family:宋体"}]{#struct_0_55199_x9544_1659807723}

[[RX power low]{lang="EN-US"}]{#struct_0_55199_x9544_1602810829}

[[接收光功率低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1597014520}

[[TX not ready]{lang="EN-US"}]{#struct_0_55199_x9544_877650815}

[[发送状态未就绪]{style="font-family:宋体"}]{#struct_0_55199_x9544_2056169839}

[[TX fault]{lang="EN-US"}]{#struct_0_55199_x9544_x1596948984}

[[发送错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1209019765}

[[TX CDR loss of lock]{lang="EN-US"}]{#struct_0_55199_x9544_x997186709}

[[TX CDR]{lang="EN-US"}]{#struct_0_55199_x9544_x1596883448}[时钟失锁]{style="font-family:宋体"}

[[TX bias high]{lang="EN-US"}]{#struct_0_55199_x9544_701981616}

[[偏置电流高]{style="font-family:宋体"}]{#struct_0_55199_x9544_1767101919}

[[TX bias low]{lang="EN-US"}]{#struct_0_55199_x9544_x1596293624}

[[偏置电流低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x15834489}

[[TX power high]{lang="EN-US"}]{#struct_0_55199_x9544_577445829}

[[发送光功率高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1596228088}

[[TX power low]{lang="EN-US"}]{#struct_0_55199_x9544_504958990}

[[发送光功率低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x964277078}

[[Module not ready]{lang="EN-US"}]{#struct_0_55199_x9544_325496384}

[[模块状态未就绪]{style="font-family:宋体"}]{#struct_0_55199_x9544_x546849381}

[[APD supply fault]{lang="EN-US"}]{#struct_0_55199_x9544_717826892}

[[APD]{lang="EN-US"}]{#struct_0_55199_x9544_325561920}[（]{style="font-family:宋体"}[Avalanche Photo Diode]{lang="EN-US"}[，雪崩光电二极管）错误]{style="font-family:宋体"}

[[TEC fault]{lang="EN-US"}]{#struct_0_55199_x9544_x620606194}

[[TEC]{lang="EN-US"}]{#struct_0_55199_x9544_325627456}[（]{style="font-family:宋体"}[Thermoelectric Cooler]{lang="EN-US"}[，热点冷却器）错误]{style="font-family:宋体"}

[[Wavelength unlocked]{lang="EN-US"}]{#struct_0_55199_x9544_1626884575}

[[光信号波长失锁]{style="font-family:宋体"}]{#struct_0_55199_x9544_301162610}

[[Temp high]{lang="EN-US"}]{#struct_0_55199_x9544_325692992}

[[温度高]{style="font-family:宋体"}]{#struct_0_55199_x9544_x707703897}

[[Temp low]{lang="EN-US"}]{#struct_0_55199_x9544_325234240}

[[温度低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1620364552}

[[Voltage high]{lang="EN-US"}]{#struct_0_55199_x9544_x1485202172}

[[电压高]{style="font-family:宋体"}]{#struct_0_55199_x9544_325299776}

[[Voltage low]{lang="EN-US"}]{#struct_0_55199_x9544_334621489}

[[电压低]{style="font-family:宋体"}]{#struct_0_55199_x9544_x224565075}

[[Transceiver info I/O error]{lang="EN-US"}]{#struct_0_55199_x9544_325365312}

[[模块信息读写错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x842088702}

[[Transceiver info checksum error]{lang="EN-US"}]{#struct_0_55199_x9544_325430848}

[[模块信息校验错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_1704444174}

[[Transceiver type and port configuration mismatch]{lang="EN-US"}]{#struct_0_55199_x9544_326020672}

[[模块类型和端口配置不匹配]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1153235284}

[[Transceiver type not supported by port hardware]{lang="EN-US"}]{#struct_0_55199_x9544_x720087091}

[[端口不支持该模块类型]{style="font-family:宋体"}]{#struct_0_55199_x9544_326086208}

[[XENPAK]{lang="EN-US"}]{#struct_0_55199_x9544_x379833584}

[[WIS local fault]{lang="EN-US"}]{#struct_0_55199_x9544_325496385}

[[WIS]{lang="EN-US"}]{#struct_0_55199_x9544_x546849380}[（]{style="font-family:宋体"}[WAN Interface Sublayer]{lang="EN-US"}[）本地错误]{style="font-family:宋体"}

[[Receive optical power fault]{lang="EN-US"}]{#struct_0_55199_x9544_325561921}

[[接收光功率错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x620606195}

[[PMA/PMD receiver local fault]{lang="EN-US"}]{#struct_0_55199_x9544_x80471956}

[[PMA/PMD]{lang="EN-US"}]{#struct_0_55199_x9544_325627457}[（]{style="font-family:宋体"}[Physical Medium Attachment/Physical Medium Dependent]{lang="EN-US"}[）接收器本地错误]{style="font-family:宋体"}

[[PCS receive local fault]{lang="EN-US"}]{#struct_0_55199_x9544_1626884574}

[[PCS]{lang="EN-US"}]{#struct_0_55199_x9544_325692993}[（]{style="font-family:宋体"}[Physical Coding Sublayer]{lang="EN-US"}[）接收本地错误]{style="font-family:宋体"}

[[PHY XS receive local fault]{lang="EN-US"}]{#struct_0_55199_x9544_x707703896}

[[PHY XS]{lang="EN-US"}]{#struct_0_55199_x9544_325234241}[（]{style="font-family:宋体"}[PHY Extended Sublayer]{lang="EN-US"}[）接收本地错误]{style="font-family:宋体"}

[[RX power high]{lang="EN-US"}]{#struct_0_55199_x9544_x1620364551}

[[接收光功率高]{style="font-family:宋体"}]{#struct_0_55199_x9544_325299777}

[[RX power low]{lang="EN-US"}]{#struct_0_55199_x9544_334621490}

[[接收光功率低]{style="font-family:宋体"}]{#struct_0_55199_x9544_325365313}

[[Laser bias current fault]{lang="EN-US"}]{#struct_0_55199_x9544_x842088703}

[[激光器偏置电流错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_325430849}

[[Laser temperature fault]{lang="EN-US"}]{#struct_0_55199_x9544_1704444175}

[[激光器温度错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x286919216}

[[Laser output power fault]{lang="EN-US"}]{#struct_0_55199_x9544_326020673}

[[激光器输出光功率错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1153235285}

[[TX fault]{lang="EN-US"}]{#struct_0_55199_x9544_326086209}

[[发送器错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_x379833585}

[[PMA/PMD receiver local fault]{lang="EN-US"}]{#struct_0_55199_x9544_325496386}

[[PMA/PMD]{lang="EN-US"}]{#struct_0_55199_x9544_x546849379}[接收器本地错误]{style="font-family:宋体"}

[[PCS receive local fault]{lang="EN-US"}]{#struct_0_55199_x9544_325561922}

[[PCS]{lang="EN-US"}]{#struct_0_55199_x9544_x620606192}[接收本地错误]{style="font-family:宋体"}

[[PHY XS receive local fault]{lang="EN-US"}]{#struct_0_55199_x9544_325627458}

[[PHY XS]{lang="EN-US"}]{#struct_0_55199_x9544_325692994}[接收本地错误]{style="font-family:宋体"}

[[TX bias high]{lang="EN-US"}]{#struct_0_55199_x9544_x707703895}

[[偏置电流高]{style="font-family:宋体"}]{#struct_0_55199_x9544_325234242}

[[TX bias low]{lang="EN-US"}]{#struct_0_55199_x9544_x1620364554}

[[偏置电流低]{style="font-family:宋体"}]{#struct_0_55199_x9544_325299778}

[[TX power high]{lang="EN-US"}]{#struct_0_55199_x9544_334621491}

[[发送光功率高]{style="font-family:宋体"}]{#struct_0_55199_x9544_325365314}

[[TX power low]{lang="EN-US"}]{#struct_0_55199_x9544_x842088700}

[[发送光功率低]{style="font-family:宋体"}]{#struct_0_55199_x9544_325430850}

[[Temp high]{lang="EN-US"}]{#struct_0_55199_x9544_x251870970}

[[温度高]{style="font-family:宋体"}]{#struct_0_55199_x9544_326020674}

[[Temp low]{lang="EN-US"}]{#struct_0_55199_x9544_x1153235290}

[[温度低]{style="font-family:宋体"}]{#struct_0_55199_x9544_326086210}

[[Transceiver info I/O error]{lang="EN-US"}]{#struct_0_55199_x9544_1958818584}

[[模块信息]{style="font-family:宋体"}[I/O]{lang="EN-US"}]{#struct_0_55199_x9544_325496387}[错误]{style="font-family:宋体"}

[[Transceiver info checksum error]{lang="EN-US"}]{#struct_0_55199_x9544_x546849378}

[[模块信息校验错误]{style="font-family:宋体"}]{#struct_0_55199_x9544_325561923}

[[Transceiver type and port configuration mismatch]{lang="EN-US"}]{#struct_0_55199_x9544_x620606193}

[[模块类型和端口配置不匹配]{style="font-family:宋体"}]{#struct_0_55199_x9544_325627459}

[[Transceiver type not supported by port hardware]{lang="EN-US"}]{#struct_0_55199_x9544_1626884584}

[[端口不支持该模块类型]{style="font-family:宋体"}]{#struct_0_55199_x9544_325692995}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x707703894}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x795902736}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上插入的可插拔接口模块的当前故障告警信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> display transceiver alarm interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_55199_x9544_325234243}

[GigabitEthernet1/0/1 transceiver current alarm information:]{lang="EN-US"}

[  RX loss of signal]{lang="EN-US"}

[  RX power low]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display transceiver alarm]{lang="EN-US"}]{#struct_0_55199_x9544_x1620364553}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x545305970}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_80881769}

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x551726669}

[[transceiver current alarm information]{lang="EN-US"}]{#struct_0_55199_x9544_910702347}

[[接口光模块当前故障告警信息]{style="font-family:宋体"}]{#struct_0_55199_x9544_1634716892}

[[RX loss of signal]{lang="EN-US"}]{#struct_0_55199_x9544_x2110772342}

[[接收信号丢失]{style="font-family:宋体"}]{#struct_0_55199_x9544_325299779}

[[RX power low]{lang="EN-US"}]{#struct_0_55199_x9544_334621492}

[[接收光功率低告警]{style="font-family:宋体"}]{#struct_0_55199_x9544_2114087080}

[ ]{lang="EN-US"}

::::: {#1180540650 .myid}
[]{#_Toc404783100}[]{#struct_0_55199_x9544_x499094217}[]{#_Toc300730520}[]{#_Toc300730283}[]{#_Toc263066897}[]{#_Toc206560279}

**设备管理 \-- 设备管理配置命令 \-- display transceiver diagnosis**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 9 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x688195668}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x1718252693}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[数字诊断参数的显示与可插拔接口模块的类型有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_325365315}
:::

[ ]{lang="EN-US"}

[**[display transceiver diagnosis]{lang="EN-US"}**]{#struct_0_55199_x9544_x842088701}[命令用来显示可插拔光模块的数字诊断参数的当前测量值。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1982903618}

[**[display transceiver diagnosis interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x548470351}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1758925138}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1762337565}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1133111250}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1126906476}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_997911506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_325430851}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x251870969}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1255273227}

[**[interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x2144548992}[：显示接口上插入的可插拔光模块的数字诊断参数的当前测量值。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号，如果不指定该参数，表示所有接口。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x405676565}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_326086211}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上插入的可插拔光模块的数字诊断参数的当前测量值（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> display transceiver diagnosis interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_55199_x9544_325496388}

[GigabitEthernet1/0/1 transceiver diagnostic information:]{lang="EN-US"}

[  Current diagnostic parameters:]{lang="EN-US"}

[    Temp(°C)  Voltage(V)  Bias(mA)  RX power(dBm)  TX power(dBm)]{lang="EN-US"}

[    36        3.31        6.13      -35.64          -5.19]{lang="EN-US"}

[  Alarm thresholds:]{lang="EN-US"}

[           Temp(]{lang="EN-US"}[℃]{style="font-family:宋体"}[)   Voltage(V)  Bias(mA)  RX power(dBM)  TX power(dBM)]{lang="EN-US"}

[    High   50         3.55        1.44      -10.00         5.00]{lang="EN-US"}

[    Low    30         3.01        1.01      -30.00         0.00]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display transceiver diagnosis]{lang="EN-US"}]{#struct_0_55199_x9544_x546849377}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x553447634}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_717957955}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x15924880}

[[transceiver diagnostic information]{lang="EN-US"}]{#struct_0_55199_x9544_x251685185}

[[接口插入的光模块的数字诊断信息]{style="font-family:宋体"}]{#struct_0_55199_x9544_325561924}

[[Current diagnostic parameters]{lang="EN-US"}]{#struct_0_55199_x9544_x620606190}

[[当前的诊断参数]{style="font-family:宋体"}]{#struct_0_55199_x9544_x80144276}

[[Temp.(°C)]{lang="EN-US"}]{#struct_0_55199_x9544_1139673138}

[[数字诊断参数------温度，单位为]{style="font-family:宋体"}[°C]{lang="EN-US"}]{#struct_0_55199_x9544_x1463056015}[，精确到]{style="font-family:宋体"}[1°C]{lang="EN-US"}

[[Voltage(V)]{lang="EN-US"}]{#struct_0_55199_x9544_x949684223}

[[数字诊断参数------电压，单位为]{style="font-family:宋体"}[V]{lang="EN-US"}]{#struct_0_55199_x9544_325627460}[，精确到]{style="font-family:宋体"}[0.01V]{lang="EN-US"}

[[Bias(mA)]{lang="EN-US"}]{#struct_0_55199_x9544_x329430559}

[[数字诊断参数------偏置电流，单位为]{style="font-family:宋体"}[mA]{lang="EN-US"}]{#struct_0_55199_x9544_x2108423845}[，精确到]{style="font-family:宋体"}[0.01mA]{lang="EN-US"}

[[RX power(dBm)]{lang="EN-US"}]{#struct_0_55199_x9544_577714675}

[[数字诊断参数------接收光功率，单位为]{style="font-family:宋体"}[dBm]{lang="EN-US"}]{#struct_0_55199_x9544_851828608}[，精确到]{style="font-family:宋体"}[0.01dBm]{lang="EN-US"}

[[TX power(dBm)]{lang="EN-US"}]{#struct_0_55199_x9544_325692996}

[[数字诊断参数------发送光功率，单位为]{style="font-family:宋体"}[dBm]{lang="EN-US"}]{#struct_0_55199_x9544_x707703893}[，精确到]{style="font-family:宋体"}[0.01dBm]{lang="EN-US"}

[[Alarm thresholds]{lang="EN-US"}]{#struct_0_55199_x9544_930648413}

[[告警门限]{style="font-family:宋体"}]{#struct_0_55199_x9544_930648412}

[[High]{lang="EN-US"}]{#struct_0_55199_x9544_930648407}

[[高告警门限]{style="font-family:宋体"}]{#struct_0_55199_x9544_930648406}

[[Low]{lang="EN-US"}]{#struct_0_55199_x9544_930648409}

[[低告警门限]{style="font-family:宋体"}]{#struct_0_55199_x9544_930648408}

[ ]{lang="EN-US"}

::::: {#-340964738 .myid}
[]{#_Toc404783101}[]{#struct_0_55199_x9544_x795443984}[]{#_Toc300730518}[]{#_Toc300730281}[]{#_Toc263066895}[]{#_Toc206560280}

**设备管理 \-- 设备管理配置命令 \-- display transceiver interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_521193563}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_617500906}
:::

**[ ]{lang="EN-US"}**

[**[display transceiver interface]{lang="EN-US"}**]{#struct_0_55199_x9544_x2066940403}[命令用来显示可插拔接口模块的主要特征参数。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x157499707}

[**[display transceiver interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_325234244}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1620364556}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_840396656}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x189126698}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_473705878}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1717852937}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_2136007152}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x483415346}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_811961333}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_55199_x9544_325299780}[：显示接口上插入的可插拔接口模块的主要特征参数。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号，如果不指定该参数，表示所有接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1143925547}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1434524446}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上插入的可插拔接口模块的主要特征参数（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> display transceiver interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_55199_x9544_x947261333}

[GigabitEthernet1/0/1 transceiver information:]{lang="EN-US"}

[  Transceiver Type              : 1000_BASE_SX_SFP]{lang="EN-US"}

[  Connector Type                : LC]{lang="EN-US"}

[  Wavelength(nm)                : 850]{lang="EN-US"}

[  Transfer Distance(m)          : 550(50um),270(62.5um)]{lang="EN-US"}

[  Digital Diagnostic Monitoring : YES]{lang="EN-US"}

[  Vendor Name                   : H3C]{lang="EN-US"}

[  Ordering Name                 : SFP-GE-SX-MM850]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[display transceiver interface]{lang="EN-US"}]{#struct_0_55199_x9544_766674244}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x790866386}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_325365316}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x842088698}

[[transceiver information]{lang="EN-US"}]{#struct_0_55199_x9544_x356207303}

[[可插拔接口模块信息]{style="font-family:宋体"}]{#struct_0_55199_x9544_1443545514}

[[Transceiver Type]{lang="EN-US"}]{#struct_0_55199_x9544_x1505565341}

[[可插拔接口模块的物理型号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2086205133}

[[Connector Type]{lang="EN-US"}]{#struct_0_55199_x9544_325430852}

[[可插拔接口模块的连接器类型，其中：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x251870972}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[光纤连接器包括]{lang="EN-US" style="font-family:宋体"}[SC]{lang="EN-US"}]{#struct_0_55199_x9544_1255863050}[（]{lang="EN-US" style="font-family:宋体"}[SC Connector]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[NTT]{lang="EN-US"}[公司推出的拔插锁紧式光纤连接器）、]{lang="EN-US" style="font-family:宋体"}[LC]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[LC Connector]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Lucent]{lang="EN-US"}[公司推出的]{lang="EN-US" style="font-family:宋体"}[1.25mm/RJ45]{lang="EN-US"}[锁紧式光纤连接器）两种类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[其他连接器包括]{style="font-family:宋体"}]{#struct_0_55199_x9544_1769653819}[RJ-45]{lang="EN-US"}[、]{style="font-family:宋体"}[CX4]{lang="EN-US"}[等类型]{style="font-family:宋体"}

[[Wavelength(nm)]{lang="EN-US"}]{#struct_0_55199_x9544_1267577179}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[光模块：显示发送激光中心波长，单位]{style="font-family:宋体"}]{#struct_0_55199_x9544_326020676}[nm]{lang="EN-US"}[；对于支持多条不同波长光路的模块（例如]{style="font-family:宋体"}[10GBASE-LX4]{lang="EN-US"}[模块），各个波长值之间用逗号分隔]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[电模块：显示为"]{lang="EN-US" style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_55199_x9544_x1153235288}["]{lang="EN-US" style="font-family:宋体"}

[[Transfer Distance(xx)]{lang="EN-US"}]{#struct_0_55199_x9544_1961742097}

[[传输距离，]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_55199_x9544_833174682}[为传输距离的单位，对于单模模块]{style="font-family:宋体"}[xx]{lang="EN-US"}[为]{style="font-family:宋体"}[km]{lang="EN-US"}[，对于其他模块]{style="font-family:宋体"}[xx]{lang="EN-US"}[为]{style="font-family:宋体"}[m]{lang="EN-US"}[。当模块支持多种传输介质时，各个传输距离值之间用逗号分隔。距离值后面括号里包含对应的"传输介质"。下面是各个介质的名称：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9um]{lang="EN-US"}]{#struct_0_55199_x9544_x1778956951}[：表示]{style="font-family:宋体"}[9/125um]{lang="EN-US"}[单模光纤]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[50um]{lang="EN-US"}]{#struct_0_55199_x9544_326086212}[：表示]{lang="EN-US" style="font-family:宋体"}[50/125um]{lang="EN-US"}[多模光纤]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[62.5um]{lang="EN-US"}]{#struct_0_55199_x9544_1958818582}[：表示]{lang="EN-US" style="font-family:宋体"}[62.5/125um]{lang="EN-US"}[多模光纤]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TP]{lang="EN-US"}]{#struct_0_55199_x9544_x481638167}[：表示双绞线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CX4]{lang="EN-US"}]{#struct_0_55199_x9544_x194273194}[：表示]{lang="EN-US" style="font-family:宋体"}[CX4]{lang="EN-US"}[电缆]{lang="EN-US" style="font-family:宋体"}

[[Digital Diagnostic Monitoring]{lang="EN-US"}]{#struct_0_55199_x9544_2074527657}

[[对数字诊断功能的支持情况，其中：]{style="font-family:宋体"}]{#struct_0_55199_x9544_325496389}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[YES]{lang="EN-US"}]{#struct_0_55199_x9544_x546849376}[：表示支持数字诊断]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO]{lang="EN-US"}]{#struct_0_55199_x9544_717892419}[：表示不支持数字诊断]{style="font-family:宋体"}

[[Vendor Name]{lang="EN-US"}]{#struct_0_55199_x9544_1473638095}

[[模块生产或定制厂商名称]{style="font-family:宋体"}]{#struct_0_55199_x9544_325561925}

[[Ordering Name]{lang="EN-US"}]{#struct_0_55199_x9544_x620606191}

[[可插拔接口模块的对外型号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x80209812}

[ ]{lang="EN-US"}

::::: {#-1185178718 .myid}
[]{#_Toc136403375}[]{#_Toc98563155}[]{#_Toc31353742}[]{#_Toc404783102}[]{#struct_0_55199_x9544_x1359702696}[]{#_Toc300730521}[]{#_Toc300730284}[]{#_Toc263066898}[]{#_Toc206560281}

**设备管理 \-- 设备管理配置命令 \-- display transceiver manuinfo**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 10 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1213654656}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_69457738}
:::

[ ]{lang="EN-US"}

[**[display transceiver manuinfo]{lang="EN-US"}**]{#struct_0_55199_x9544_325627461}[命令用于显示可插拔接口模块的部分电子标签信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x329430560}

[**[display transceiver manuinfo interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x2108882594}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_858133785}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_363917105}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x483485735}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1554353138}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x1317091489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_325692997}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x707703892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x795509520}

[**[interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x664793964}[：显示接口上插入的可插拔接口模块的部分电子标签信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号，如果不指定该参数，表示所有接口。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x896565447}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_666862555}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上插入的可插拔接口模块的部分电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> display transceiver manuinfo interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_55199_x9544_1915452450}

[GigabitEthernet1/0/1 transceiver manufacture information:]{lang="EN-US"}

[  Manu. Serial Number  : 213410A0000054000251]{lang="EN-US"}

[  Manufacturing Date   : 2012-09-01]{lang="EN-US"}

[  Vendor Name          : H3C]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[display transceiver manuinfo]{lang="EN-US"}]{#struct_0_55199_x9544_1961106278}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x795019698}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_325234245}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1620364555}

[[Manu. Serial Number]{lang="EN-US"}]{#struct_0_55199_x9544_1243681183}

[[在生产过程中生成的序列号]{style="font-family:宋体"}]{#struct_0_55199_x9544_171948087}

[[Manufacturing Date]{lang="EN-US"}]{#struct_0_55199_x9544_x445512545}

[[写入电子标签的日期]{style="font-family:宋体"}]{#struct_0_55199_x9544_1480468477}

[[Vendor Name]{lang="EN-US"}]{#struct_0_55199_x9544_325299781}

[[厂商名称]{style="font-family:宋体"}]{#struct_0_55199_x9544_1143925548}

[ ]{lang="EN-US"}

::: {#-333764678 .myid}
[]{#_Toc404783103}[]{#struct_0_55199_x9544_x1434983198}[]{#_Toc300730522}[]{#_Toc300730285}[]{#_Toc263066899}[]{#_Toc209953983}[]{#_Toc211937260}[]{#_Toc211937740}[]{#_Toc213494888}[]{#_Toc167610158}[]{#_Toc168827749}[]{#_Toc167610159}[]{#_Toc168827750}[]{#_Toc142798563}[]{#_Toc141505970}[]{#_Toc141506499}[]{#_Toc135050094}[]{#_Toc230516747}[]{#_Toc230518660}[]{#_Toc230516748}[]{#_Toc230518661}[]{#_Toc230516750}[]{#_Toc230518663}[]{#_Toc230516751}[]{#_Toc230518664}[]{#_Toc230516752}[]{#_Toc230518665}[]{#_Toc230516753}[]{#_Toc230518666}[]{#_Toc230516754}[]{#_Toc230518667}[]{#_Toc230516755}[]{#_Toc230518668}[]{#_Toc230516756}[]{#_Toc230518669}[]{#_Toc230516757}[]{#_Toc230518670}[]{#_Toc230516758}[]{#_Toc230518671}[]{#_Toc230516759}[]{#_Toc230518672}[]{#_Toc230516760}[]{#_Toc230518673}[]{#_Toc230516761}[]{#_Toc230518674}[]{#_Toc230516762}[]{#_Toc230518675}[]{#_Toc230516763}[]{#_Toc230518676}[]{#_Toc230516764}[]{#_Toc230518677}[]{#_Toc230516765}[]{#_Toc230518678}[]{#_Toc230516766}[]{#_Toc230518679}[]{#_Toc230516767}[]{#_Toc230518680}[]{#_Toc230516768}[]{#_Toc230518681}[]{#_Toc230516769}[]{#_Toc230518682}[]{#_Toc230516770}[]{#_Toc230518683}[]{#_Toc230516771}[]{#_Toc230518684}[]{#_Toc230516772}[]{#_Toc230518685}[]{#_Toc230516773}[]{#_Toc230518686}[]{#_Toc230516774}[]{#_Toc230518687}[]{#_Toc230516775}[]{#_Toc230518688}[]{#_Toc230516776}[]{#_Toc230518689}[]{#_Toc230516777}[]{#_Toc230518690}[]{#_Toc230516778}[]{#_Toc230518691}[]{#_Toc230516779}[]{#_Toc230518692}[]{#_Toc171256235}[]{#_Toc171257145}[]{#_Toc230516780}[]{#_Toc230518693}[]{#_Toc230516781}[]{#_Toc230518694}[]{#_Toc230516782}[]{#_Toc230518695}[]{#_Toc230516783}[]{#_Toc230518696}[]{#_Toc230516785}[]{#_Toc230518698}[]{#_Toc209953989}[]{#_Toc211937266}[]{#_Toc211937746}[]{#_Toc213494894}[]{#_Toc209953990}[]{#_Toc211937267}[]{#_Toc211937747}[]{#_Toc213494895}[]{#_Toc209953994}[]{#_Toc211937271}[]{#_Toc211937751}[]{#_Toc213494899}

**设备管理 \-- 设备管理配置命令 \-- display version**

------------------------------------------------------------------------

[**[display version]{lang="EN-US"}**]{#struct_0_55199_x9544_x1900127538}[命令用来显示系统版本信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1340903393}

[**[display]{lang="EN-US"}**[ **version**]{lang="EN-US"}]{#struct_0_55199_x9544_x825683246}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_983719791}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_325365317}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x842088699}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x356272839}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x2050094930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x240090924}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x462614420}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_148763632}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1747148900}[查看系统版本信息（不同设备的版本信息不同，请以设备的实际情况为准，此处略）。]{style="font-family:宋体"}

[[\<Sysname\> display version]{lang="EN-US"}]{#struct_0_55199_x9544_325430853}
:::

::::: {#175996344 .myid}
[]{#_Toc300730524}[]{#_Toc300730287}[]{#_Toc263066901}[]{#_Toc206560283}[]{#_Toc404783104}[]{#struct_0_55199_x9544_x251870971}[]{#_Toc311530763}[]{#_Toc263066900}[]{#_Toc206560282}[]{#_Toc127779656}[]{#_Toc209953997}[]{#_Toc211937274}[]{#_Toc211937754}[]{#_Toc213494902}[]{#_Toc209954001}[]{#_Toc211937278}[]{#_Toc211937758}[]{#_Toc213494906}[]{#_Toc209954002}[]{#_Toc211937279}[]{#_Toc211937759}[]{#_Toc213494907}

**设备管理 \-- 设备管理配置命令 \-- display version-update-record**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 25 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1255797514}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x2144668556}
:::

[ ]{lang="EN-US"}

[**[display version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_238318281}[命令用来显示设备启动软件包版本更新操作的记录。（集中式设备）]{style="font-family:
宋体"}

[**[display version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_x4554407}[命令用来显示主用主控板启动软件包版本更新操作的记录。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[display version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_x89058356}[命令用来显示主设备启动软件包版本更新操作的记录。（集中式]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[display version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_1510918199}[命令用来显示全局主用主控板启动软件包版本更新操作的记录。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_326020677}

[**[display version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_x1153235289}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_395658156}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1677764695}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2032531688}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x788700792}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_x331004653}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1800073410}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_2014411300}

[[【描述】]{style="font-family:黑体"}]{#struct_0_55199_x9544_326086213}

[[设备启动时会记录当前使用的启动软件包版本信息，如果在运行过程中进行启动软件包版本更新操作，系统会记录该次更新的简要信息，包括升级时间和版本，以便管理员了解相关信息。设备重启这些记录也不会被删除。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1958818581}

[[目前最多可以保存的更新记录的数目与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x481834775}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2105350103}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1789258042}[显示设备启动软件包版本更新操作的记录。]{style="font-family:宋体"}

[[\<Sysname\> display version-update-record]{lang="EN-US"}]{#struct_0_55199_x9544_1891580325}

[Record 1  (updated on Apr 18 2014 at 06:23:54):]{lang="EN-US"}

[ \*Name        : simware-cmw710-boot-a5301.bin]{lang="EN-US"}

[  Version     : 7.1.053 Alpha 7153]{lang="EN-US"}

[  Compile time: Mar 25 2014 15:52:43]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \*Name        : simware-cmw710-system-a5301.bin]{lang="EN-US"}

[  Version     : 7.1.053 Alpha 7153]{lang="EN-US"}

[  Compile time: Mar 25 2014 15:52:43]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[display version-update-record]{lang="EN-US"}]{#struct_0_55199_x9544_x1641588728}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x794776850}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_474033965}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_180373539}

[[Record *n* (updated on Apr 18 2014 at 06:23:54)]{lang="EN-US"}]{#struct_0_55199_x9544_x481439073}

[[最近的第]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_55199_x9544_578557106}[次更新的时间，]{style="font-family:宋体"}[Record 1]{lang="EN-US"}[为最新的一次更新]{style="font-family:宋体"}

[[\*Name]{lang="EN-US"}]{#struct_0_55199_x9544_x958698871}

[[软件包的名称。带]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_55199_x9544_x509175900}[符号，表示软件包的版本和升级前的版本有变化；不带]{style="font-family:宋体"}[\*]{lang="EN-US"}[符号，表示版本没有变化]{style="font-family:宋体"}

[[Version]{lang="EN-US"}]{#struct_0_55199_x9544_1891645861}

[[软件包的版本号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1642023370}

[[Compile time]{lang="EN-US"}]{#struct_0_55199_x9544_2078988806}

[[版本编译时间]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1826061723}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_482429506}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_629129556}

::::: {#1813993242 .myid}
[]{#_Toc404783105}[]{#struct_0_55199_x9544_429103289}

**设备管理 \-- 设备管理配置命令 \-- display xbar**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 11 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1265195645}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1891776933}
:::

**[ ]{lang="EN-US"}**

[**[display xbar]{lang="EN-US"}**]{#struct_0_55199_x9544_1882407301}[命令用来显示设备上主用主控板和备用主控板的负载模式，包括配置的负载模式和当前运行的负载模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_794678463}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1179232482}

[**[display xbar]{lang="EN-US"}**]{#struct_0_55199_x9544_x610397137}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1085294323}[模式：]{style="font-family:宋体"}

[**[display xbar ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x616478178}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x456034437}

[[任意视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1891318181}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1903735792}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x398562679}

[[network-operator]{lang="EN-US"}]{#struct_0_55199_x9544_2055683283}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2013414663}

[[mdc-operator]{lang="EN-US"}]{#struct_0_55199_x9544_295065688}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x250913496}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x312175322}[：用来显示指定成员设备上主用主控板和备用主控板的负载模式。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891383717}

[[配置的负载模式和当前运行的负载模式不一定相同。只有主用主控板和备用主控板同时在位时，配置的负载分担模式才会生效；否则，即便配置了负载分担模式，主用主控板也会自动切换到独立负载模式。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2003109120}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_621125171}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_235238084}[显示设备主用主控板和备用主控板的负载模式。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display xbar]{lang="EN-US"}]{#struct_0_55199_x9544_x1440671767}

[The configured system HA xbar load mode is BALANCE]{lang="EN-US"}

[The activated system HA xbar load mode is SINGLE]{lang="EN-US"}

[[以上显示信息表明：当前系统配置的负载模式为负载分担模式，但实际生效的是独立负载模式。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x651999914}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1413536983}[显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[系统中所有成员设备上主用主控板和备用主控板的负载模式。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display xbar]{lang="EN-US"}]{#struct_0_55199_x9544_1891449253}

[Chassis 1:]{lang="EN-US"}

[The configured system HA xbar load mode is BALANCE]{lang="EN-US"}

[The activated system HA xbar load mode is SINGLE]{lang="EN-US"}

[Chassis 2:]{lang="EN-US"}

[The configured system HA xbar load mode is SINGLE]{lang="EN-US"}

[The activated system HA xbar load mode is SINGLE]{lang="EN-US"}

[[以上显示信息表明：]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1882668721}[系统中有两个成员设备，成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上配置的主用主控板和备用主控板的负载模式为负载分担模式，但实际生效的是独立负载模式；成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置的主用主控板和备用主控板的负载模式为独立负载模式，实际生效的也是独立负载模式。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_66179670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[xbar]{lang="EN-US"}**]{#struct_0_55199_x9544_364734757}
:::::

::::: {#1606769103 .myid}
[]{#_Toc300730525}[]{#_Toc300730288}[]{#_Toc297292420}[]{#_Toc278550997}[]{#_Toc404783106}[]{#struct_0_55199_x9544_486667240}[]{#_Toc353891374}[]{#_Toc209954010}[]{#_Toc211937287}[]{#_Toc211937767}[]{#_Toc213494915}

**设备管理 \-- 设备管理配置命令 \-- fabric load-sharing mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 7 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1826171077}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1891514789}
:::

[ ]{lang="EN-US"}

[**[fabric load-sharing mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x91215234}[命令用来配置业务板的负载分担类型。]{style="font-family:
宋体"}

[**[undo fabric load-sharing mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x1432491808}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x849396896}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x364751532}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[fabric load-sharing mode]{lang="EN-US"}**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-ip** \| **source-mac** \| **source-port** \| **vlan-id** } \* \| **flexible** \| **per-packet** } **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_330012165}

[**[undo fabric load-sharing mode slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_676433897}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1051422510}[模式：]{style="font-family:宋体"}

[**[fabric load-sharing mode]{lang="EN-US"}**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-ip** \| **source-mac** \| **source-port** \| **vlan-id** } \* \| **flexible** \| **per-packet** } **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1892104613}

[**[undo fabric load-sharing mode chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1724066555}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_990857902}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x71542048}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2097687900}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1941184873}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_717254872}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1557820936}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1892170149}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2114672786}

[**[destination-ip]{lang="EN-US"}**]{#struct_0_55199_x9544_x1663561816}[：表示按报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-mac]{lang="EN-US"}**]{#struct_0_55199_x9544_1054609967}[：表示按报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**]{#struct_0_55199_x9544_x833858298}[：表示按报文的目的服务端口进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ingress-port]{lang="EN-US"}**]{#struct_0_55199_x9544_1995540470}[：表示按报文的入端口进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ip-protocol]{lang="EN-US"}**]{#struct_0_55199_x9544_1381128197}[：表示按报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议类型进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label1]{lang="EN-US"}**]{#struct_0_55199_x9544_x259272076}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第一层标签进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label2]{lang="EN-US"}**]{#struct_0_55199_x9544_1891580326}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第二层标签进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mpls-label3]{lang="EN-US"}**]{#struct_0_55199_x9544_x1641654264}[：表示按]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文第三层标签进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**]{#struct_0_55199_x9544_437475299}[：表示按报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**]{#struct_0_55199_x9544_2070022550}[：表示按报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}**]{#struct_0_55199_x9544_x1650978367}[：表示按报文的源服务端口进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan-id]{lang="EN-US"}**]{#struct_0_55199_x9544_682131013}[：表示按报文所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[flexible]{lang="EN-US"}**]{#struct_0_55199_x9544_x1881664071}[：表示按报文类型（如二层、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[等）自动选择负载分担的类型。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[per-packet]{lang="EN-US"}**]{#struct_0_55199_x9544_x1193494509}[：表示对每个报文逐包进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_55199_x9544_x1891701764}*[slot-number]{lang="EN-US"}*[：单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_55199_x9544_1891645862}*[slot-number]{lang="EN-US"}*[：设备所在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_55199_x9544_1084993061}*[slot-number]{lang="EN-US"}*[：设备所在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_55199_x9544_x1642088906}*[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_55199_x9544_x203816526}*[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1295479656}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行本命令，新的配置将覆盖旧的配置。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1749467471}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于业务板不支持的负载分担类型，系统将提示用户不支持。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x535612850}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_927583247}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1275773742}[配置单板]{style="font-family:宋体"}[2]{lang="EN-US"}[按照报文目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行负载分担。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1891711398}

[\[Sysname\] fabric load-sharing mode destination-mac slot 2]{lang="EN-US"}
:::::

::::: {#-1483397931 .myid}
[]{#_Toc404783107}[]{#struct_0_55199_x9544_x86121558}

**设备管理 \-- 设备管理配置命令 \-- fan auto-control-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1843488673}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1192814631}
:::

**[ ]{lang="EN-US"}**

[**[fan auto-control-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_1012607506}[命令用来配置风扇的工作模式。]{style="font-family:宋体"}

[**[undo fan auto-control-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_1891776934}[命令用来回复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891318182}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1903801328}

[**[fan auto-control-mode]{lang="EN-US"}**[ { **low-temperature** \| **silence** }]{lang="EN-US"}]{#struct_0_55199_x9544_800429951}

[**[undo fan auto-control-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_1865307945}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1522891736}[模式：]{style="font-family:宋体"}

[**[fan auto-control-mode chassis]{lang="EN-US"}**[ *chassis-number* { **low-temperature** \| **silence** }]{lang="EN-US"}]{#struct_0_55199_x9544_x2027730224}

[**[undo fan auto-control-mode chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_592046865}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1334065093}

[[风扇工作在低温模式。]{style="font-family:宋体"}]{#struct_0_55199_x9544_768815443}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891383718}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2003698944}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_55199_x9544_6371938}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1310294124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x848150224}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_402395337}

[**[chassis]{lang="EN-US"}**[ *chassis-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1385069410}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[low-temperature]{lang="EN-US"}**]{#struct_0_55199_x9544_1822508852}[：配置风扇工作在低温模式。该模式下风扇转速较高，以便优先保证单板在较低的温度下工作。]{style="font-family:宋体"}

[**[silence]{lang="EN-US"}**]{#struct_0_55199_x9544_1891449254}[：配置设备工作在静音模式。该模式下风扇转速较低、噪音较小，但是单板温度比低温模式略高。在对噪音比较敏感的场合推荐使用此模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1882603185}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1912995171}[配置风扇工作在静音模式。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1194900987}

[\[Sysname\] fan auto-control-mode silence]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1977851858}[配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的风扇工作在静音模式。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1711447365}

[\[Sysname\] fan auto-control-mode chassis 2 silence]{lang="EN-US"}
:::::

::::: {#98750571 .myid}
[]{#_Toc404783108}[]{#struct_0_55199_x9544_1668774201}

**设备管理 \-- 设备管理配置命令 \-- fan prefer-direction**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image003.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1891514790}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x91805057}
:::

**[ ]{lang="EN-US"}**

[**[fan prefer-direction]{lang="EN-US"}**]{#struct_0_55199_x9544_x283061834}[命令用来配置用户期望的风扇模块的风道方向。]{style="font-family:宋体"}

[**[undo fan prefer-direction]{lang="EN-US"}**]{#struct_0_55199_x9544_x182208350}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_136552299}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1156922472}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[fan prefer-direction ]{lang="EN-US"}**[{ **power-to-port** \| **port-to-power** }]{lang="EN-US"}]{#struct_0_55199_x9544_393755319}

[**[undo fan prefer-direction]{lang="EN-US"}**]{#struct_0_55199_x9544_x1563197038}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1892104614}[设备：]{style="font-family:宋体"}

[**[fan prefer-direction slot]{lang="EN-US"}***[ slot-number ]{lang="EN-US"}*[{ **power-to-port** \| **port-to-power** }]{lang="EN-US"}]{#struct_0_55199_x9544_1724525307}

[**[undo fan prefer-direction slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1425266027}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x951825686}[模式：]{style="font-family:宋体"}

[**[fan prefer-direction chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}*[{ **power-to-port** \| **port-to-power** }]{lang="EN-US"}]{#struct_0_55199_x9544_125873166}

[**[undo fan prefer-direction chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1874964507}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2065434188}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x92792269}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1068493564}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1892170150}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2115131539}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1857782693}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x16041101}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1121359326}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_860114296}[：表示设备的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x481090880}[：表示设备的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x919972767}[：表示设备的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x2047174821}[：表示设备的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[power-to-port]{lang="EN-US"}**]{#struct_0_55199_x9544_x654841402}[：表示用户期望的风道方向是]{style="font-family:宋体"}[电源侧进风、端口侧出风]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[port-to-power]{lang="EN-US"}**]{#struct_0_55199_x9544_1891580327}**[：]{style="font-family:宋体"}**[表示用户期望的风道方向是]{style="font-family:宋体"}[端口侧进风、电源侧出风]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1641719800}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1567488229}[配置用户期望的风扇模块的风道方向为]{style="font-family:宋体"}[port-to-power]{lang="EN-US"}[。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1062949263}

[\[Sysname\] fan prefer-direction port-to-power]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_708754907}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的用户期望的风扇模块的风道方向为]{style="font-family:宋体"}[port-to-power]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1662004499}

[\[Sysname\] fan prefer-direction slot 1 port-to-power]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_8529456}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的用户期望的风扇模块的风道方向为]{style="font-family:宋体"}[port-to-power]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1891645863}

[\[Sysname\] fan prefer-direction chassis 1 port-to-power]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1642154442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fan]{lang="EN-US"}**]{#struct_0_55199_x9544_x727486836}
:::::

::::: {#419308024 .myid}
[]{#_Toc300730526}[]{#_Toc300730289}[]{#_Toc404783109}[]{#struct_0_55199_x9544_505288740}

**设备管理 \-- 设备管理配置命令 \-- forward-path-detection enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_2049172072}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x102609481}
:::

**[ ]{lang="EN-US"}**

[**[forward-path-detection enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1833044767}[命令用来开启转发通道自动检测功能。]{style="font-family:
宋体"}

[**[undo forward-path-detection enable]{lang="EN-US"}**]{#struct_0_55199_x9544_2029470389}[命令用来关闭转发通道自动检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891711399}

[**[forward-path-detection enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x86056022}

[**[undo forward-path-detection enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x1289150173}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_758520399}

[[转发通道自动检测功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_55199_x9544_528017687}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1494175616}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x750668192}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2063624277}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1891776935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1882276229}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_17195240}

[[转发通道自动检测功能可以检测设备中的数据转发通道是否正常。如果不正常，会打印日志信息提醒用户。]{style="font-family:宋体"}]{#struct_0_55199_x9544_552650705}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1043246760}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1216706440}[开启转发通道自动检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x748507761}

[\[Sysname\] forward-path-detection enable]{lang="EN-US"}
:::::

::::: {#-524773407 .myid}
[]{#_Toc404783110}[]{#struct_0_55199_x9544_85510701}

**设备管理 \-- 设备管理配置命令 \-- hardware-failure-detection**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1891318183}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1903866864}
:::

[ ]{lang="EN-US"}

[**[hardware-failure-detection]{lang="EN-US"}**]{#struct_0_55199_x9544_421399582}[命令用来配置当系统检测到硬件故障时自动采取的修复操作。]{style="font-family:
宋体"}

[**[undo hardware-failure-detection]{lang="EN-US"}**]{#struct_0_55199_x9544_1891383719}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2003764480}

[**[hardware-failure-detection]{lang="EN-US"}**[ { **board** \| **chip** \| **forwarding** } { **off** \| **isolate** \| **reset** \| **warning** }]{lang="EN-US"}]{#struct_0_55199_x9544_x67588564}

[**[undo hardware-failure-detection ]{lang="EN-US"}**[{ **board** \| **chip** \| **forwarding** }]{lang="EN-US"}]{#struct_0_55199_x9544_1891449255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1882537649}

[[当系统检测到器件（]{style="font-family:宋体"}[chip]{lang="EN-US"}]{#struct_0_55199_x9544_1989006492}[）、单板（]{style="font-family:宋体"}[board]{lang="EN-US"}[）和转发（]{style="font-family:宋体"}[forwarding]{lang="EN-US"}[）的硬件故障时，修复操作均为]{style="font-family:宋体"}[warning]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_582901919}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1690092458}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_470113672}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1967261763}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1863873596}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891514791}

[**[board]{lang="EN-US"}**]{#struct_0_55199_x9544_x91739521}[：对单板故障进行在线检测，包括控制通道检测和单板状态快速检测。]{style="font-family:宋体"}

[**[chip]{lang="EN-US"}**]{#struct_0_55199_x9544_1864183822}[：对器件故障进行在线检测，包括单板上各种器件（比如芯片、电容、电阻等）的检测。]{style="font-family:宋体"}

[**[forwarding]{lang="EN-US"}**]{#struct_0_55199_x9544_2018095484}[：对转发层面的故障进行在线检测，包括业务自动检测和其他转发相关的检测。]{style="font-family:宋体"}

[**[off]{lang="EN-US"}**]{#struct_0_55199_x9544_972379757}[：检测到故障时，设备不进行任何操作。]{style="font-family:宋体"}

[**[isolate]{lang="EN-US"}**]{#struct_0_55199_x9544_x409871100}[：检测到故障时，设备会自动关闭端口、隔离单板、禁止单板加载或给单板下电，从而尽量减小故障的影响。]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**]{#struct_0_55199_x9544_1747019393}[：检测到故障时，设备会自动重启器件]{style="font-family:宋体"}[/]{lang="EN-US"}[单板以尝试修复故障。]{style="font-family:宋体"}

[**[warning]{lang="EN-US"}**]{#struct_0_55199_x9544_196828481}[：检测到故障时，设备发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息，不会修复故障。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1892104615}

[[设备启动后，系统会持续自动检测器件、单板和转发的硬件故障。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1724459771}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_567954637}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1088626674}[配置系统检测到器件故障时自动告警。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_2028691851}

[\[Sysname\] hardware-failure-detection chip warning]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_517643329}[配置系统检测到单板故障时自动重启。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x679634663}

[\[Sysname\] hardware-failure-detection board reset]{lang="EN-US"}
:::::

::::: {#-892203964 .myid}
[]{#_Toc404783111}[]{#struct_0_55199_x9544_x680471250}

**设备管理 \-- 设备管理配置命令 \-- hardware-failure-protection aggregation**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1892170151}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_2115197075}
:::

[ ]{lang="EN-US"}

[**[hardware-failure-protection aggregation]{lang="EN-US"}**]{#struct_0_55199_x9544_278752471}[命令用来开启针对聚合组的硬件故障保护功能。]{style="font-family:宋体"}

[**[undo hardware-failure-protection aggregation]{lang="EN-US"}**]{#struct_0_55199_x9544_1790590336}[命令用来关闭针对聚合组的硬件故障保护功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_347166730}

[**[hardware-failure-protection aggregation]{lang="EN-US"}**]{#struct_0_55199_x9544_x785550386}

[**[undo hardware-failure-protection aggregation]{lang="EN-US"}**]{#struct_0_55199_x9544_720717010}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891580328}

[[针对聚合组的硬件故障保护功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1642309624}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1192926329}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1331543878}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_629881413}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_644746911}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_939409217}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_354061572}

[[只有配置]{style="font-family:宋体"}**[hardware-failure-detection forwarding isolate]{lang="EN-US"}**]{#struct_0_55199_x9544_1891711400}[命令后，该命令才生效。]{style="font-family:宋体"}

[[配置该命令后，当系统检测到硬件故障时，会按顺序遵循如下原则处理：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1891318184}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果聚合组成员端口配置]{lang="EN-US" style="font-family:宋体"}**[undo hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_1891383720}[命令，而且该端口不是聚合组中最后一个]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[状态的端口，则该端口会被自动关闭；]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果聚合组成员端口配置]{lang="EN-US" style="font-family:宋体"}**[undo hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_x2003174655}[命令，而该端口是聚合组中最后一个]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[状态的端口，则该端口不会被关闭；]{lang="EN-US" style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果聚合组成员端口配置了]{lang="EN-US" style="font-family:宋体"}**[hardware-failure-protection]{lang="EN-US"}**[ **auto-down**]{lang="EN-US"}]{#struct_0_55199_x9544_1891449256}[命令，则不管该端口是不是聚合组中最后一个]{lang="EN-US" style="font-family:
宋体"}[UP]{lang="EN-US"}[状态的端口，该端口都会被关闭。]{lang="EN-US" style="font-family:宋体"}

[[出现以下任意一种情况时，]{style="font-family:宋体"}**[hardware-failure-protection aggregation]{lang="EN-US"}**]{#struct_0_55199_x9544_1882472113}[命令会对聚合组中的该成员端口失效：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_55199_x9544_x351695433}[下]{style="font-family:宋体"}[配置了以太网接口环回测试功能]{lang="EN-US" style="font-family:宋体"}[，即]{style="font-family:宋体"}**[loopback]{lang="EN-US"}**[ { **external** \| **internal** }]{lang="EN-US"}[命令；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口下配置了以太网接口的强制开启功能，即]{lang="EN-US" style="font-family:宋体"}**[port up-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x920605759}[命令]{style="font-family:宋体"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该端口配置为]{style="font-family:宋体"}]{#struct_0_55199_x9544_1891514792}[IRF]{lang="EN-US"}[物理端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x91673985}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x2049178886}[开启针对聚合组的硬件故障保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1426941613}

[\[Sysname\] hardware-failure-protection aggregation]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1548161266}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hardware-failure-detection]{lang="EN-US"}**]{#struct_0_55199_x9544_x2139506601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_x1728177112}
:::::

::::: {#32860441 .myid}
[]{#_Toc404783112}[]{#struct_0_55199_x9544_x224102320}

**设备管理 \-- 设备管理配置命令 \-- hardware-failure-protection auto-down**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 12 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1892104616}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1724394235}
:::

[ ]{lang="EN-US"}

[**[hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_667967891}[命令用来开启针对端口的硬件故障保护功能。]{style="font-family:宋体"}

[**[undo hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_515207554}[命令用来关闭针对端口的硬件故障保护功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1056689410}

[**[hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_x628075253}

[**[undo hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_177513119}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x189087677}

[[端口的硬件故障保护功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1892170152}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2115000467}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1661798230}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1511206318}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_254275229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2114695688}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2040684793}

[[配置了]{style="font-family:宋体"}**[hardware-failure-detection]{lang="EN-US"}**[ **forwarding** **isolate**]{lang="EN-US"}]{#struct_0_55199_x9544_2033411364}[后，本命令才会生效。]{style="font-family:
宋体"}

[[在端口上配置该命令前，请确保该端口存在备份的链路，以免造成业务中断。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1891645865}

[[在端口上配置]{style="font-family:宋体"}**[hardware-failure-protection auto-down]{lang="EN-US"}**]{#struct_0_55199_x9544_x1642285514}[命令后，当系统检测到硬件故障时，会自动关闭该端口。此时使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**[命令可看到该端口状态为]{style="font-family:宋体"}[Protect DOWN]{lang="EN-US"}[。端口硬件故障解除后，请在接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令来恢复端口状态。]{style="font-family:宋体"}

[[出现以下任意一种情况时，]{style="font-family:宋体"}**[hardware-failure-protection aggregation]{lang="EN-US"}**]{#struct_0_55199_x9544_722099362}[命令会对该端口失效：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_55199_x9544_1755871510}[下]{style="font-family:宋体"}[配置了以太网接口环回测试功能]{lang="EN-US" style="font-family:宋体"}[，即]{style="font-family:宋体"}**[loopback]{lang="EN-US"}**[ { **external** \| **internal** }]{lang="EN-US"}[命令]{style="font-family:
宋体"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_55199_x9544_850308974}[下]{style="font-family:宋体"}[配置了以太网接口的强制开启功能]{lang="EN-US" style="font-family:宋体"}[，即]{style="font-family:宋体"}**[port up-mode]{lang="EN-US"}**[命令]{style="font-family:宋体"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该端口配置为]{style="font-family:宋体"}]{#struct_0_55199_x9544_1891711401}[IRF]{lang="EN-US"}[物理端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1105060785}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x631299102}[对端口配置硬件故障保护。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_398266925}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] hardware-failure-protection auto-down]{lang="EN-US"}
:::::

::: {#-765155106 .myid}
[]{#_Toc404783113}[]{#struct_0_55199_x9544_1021067000}

**设备管理 \-- 设备管理配置命令 \-- header**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**]{#struct_0_55199_x9544_1509343045}[命令用来设置欢迎信息。]{style="font-family:宋体"}

[**[undo header]{lang="EN-US"}**]{#struct_0_55199_x9544_x1575178379}[命令用来关闭欢迎信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891776937}

[**[header]{lang="EN-US"}**[ { **incoming** \| **legal** \| **login** \| **motd** \| **shell** } *text*]{lang="EN-US"}]{#struct_0_55199_x9544_1882145157}

[**[undo header ]{lang="EN-US"}**[{ **incoming \| legal** \| **login** \| **motd** \| **shell** }]{lang="EN-US"}]{#struct_0_55199_x9544_1568194143}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x138467812}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1517954635}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1263282582}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2110850230}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_151386015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1891318185}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1903473648}

[**[incoming]{lang="EN-US"}**]{#struct_0_55199_x9544_x1555255609}[：设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[登录用户登录进入用户视图时的欢迎信息。如果要求认证，则欢迎信息在通过认证后输出。]{style="font-family:宋体"}

[**[legal]{lang="EN-US"}**]{#struct_0_55199_x9544_x775073436}[：设置登录终端界面前的授权信息，在输入认证用户名和密码前输出。]{style="font-family:宋体"}

[**[login]{lang="EN-US"}**]{#struct_0_55199_x9544_x225675720}[：设置登录验证时的欢迎信息。]{style="font-family:宋体"}

[**[motd]{lang="EN-US"}**]{#struct_0_55199_x9544_x445668409}[：设置登录终端界面前的欢迎信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[shell]{lang="EN-US"}**]{#struct_0_55199_x9544_1048622696}[：设置非]{style="font-family:宋体"}[Modem]{lang="EN-US"}[登录用户登录进入用户视图时的欢迎信息。]{style="font-family:宋体"}

[*[text]{lang="EN-US"}*]{#struct_0_55199_x9544_x2022417819}[：输入欢迎信息的内容。内容的输入支持单行和多行两种方式，具体输入规则请参见"基础配置指导"中的"设备管理"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1891383721}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x2003240191}[先后配置]{style="font-family:宋体"}**[incoming]{lang="EN-US"}**[、]{style="font-family:宋体"}**[legal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[login]{lang="EN-US"}**[、]{style="font-family:宋体"}**[motd]{lang="EN-US"}**[和]{style="font-family:宋体"}**[shell]{lang="EN-US"}**[欢迎信息，并验证配置效果。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_691227012}

[\[Sysname\] header incoming]{lang="EN-US"}

[Please input banner content, and quit with the character \'%\'.]{lang="EN-US"}

[Welcome to incoming(header incoming)%]{lang="EN-US"}

[\[Sysname\] header legal]{lang="EN-US"}

[Please input banner content, and quit with the character \'%\'.]{lang="EN-US"}

[Welcome to legal (header legal)%]{lang="EN-US"}

[\[Sysname\] header login]{lang="EN-US"}

[Please input banner content, and quit with the character \'%\'.]{lang="EN-US"}

[Welcome to login(header login)%]{lang="EN-US"}

[\[Sysname\] header motd]{lang="EN-US"}

[Please input banner content, and quit with the character \'%\'.]{lang="EN-US"}

[Welcome to motd(header motd)%]{lang="EN-US"}

[\[Sysname\] header shell]{lang="EN-US"}

[Please input banner content, and quit with the character \'%\'.]{lang="EN-US"}

[Welcome to shell(header shell)%]{lang="EN-US"}

[[本例中，"]{style="font-family:宋体"}[%]{lang="EN-US"}]{#struct_0_55199_x9544_x647698596}["为]{style="font-family:宋体"}*[text]{lang="EN-US"}*[的起始]{style="font-family:宋体"}[/]{lang="EN-US"}[结束字符，在显示文本后输入"]{style="font-family:宋体"}[%]{lang="EN-US"}["表示文本结束，退出]{style="font-family:宋体"}[header]{lang="EN-US"}[命令。作为起始与结束字符，"]{style="font-family:宋体"}[%]{lang="EN-US"}["不会成为所设置欢迎信息的一部分。]{style="font-family:宋体"}

[[采用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_55199_x9544_1891449257}[方式远程登录设备，测试以上设置（只有设置了登录认证之后，才会显示]{style="font-family:宋体"}[login]{lang="EN-US"}[欢迎信息）。]{style="font-family:宋体"}

[[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}]{#struct_0_55199_x9544_1882406577}

[\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Welcome to legal (header legal)]{lang="EN-US"}

[ Press Y or ENTER to continue, N to exit.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Welcome to motd(header motd)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Welcome to login(header login)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Login authentication]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Password:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Welcome to shell(header shell)]{lang="EN-US"}[]{#_Toc262048268}[]{#_Toc262216518}[]{#_Toc262474050}[]{#_Toc262048269}[]{#_Toc262216519}[]{#_Toc262474051}[]{#_Toc262048271}[]{#_Toc262216521}[]{#_Toc262474053}[]{#_Toc262048272}[]{#_Toc262216522}[]{#_Toc262474054}[]{#_Toc262048273}[]{#_Toc262216523}[]{#_Toc262474055}[]{#_Toc262048274}[]{#_Toc262216524}[]{#_Toc262474056}[]{#_Toc262048275}[]{#_Toc262216525}[]{#_Toc262474057}[]{#_Toc262048276}[]{#_Toc262216526}[]{#_Toc262474058}[]{#_Toc262048277}[]{#_Toc262216527}[]{#_Toc262474059}[]{#_Toc262048278}[]{#_Toc262216528}[]{#_Toc262474060}[]{#_Toc262048279}[]{#_Toc262216529}[]{#_Toc262474061}[]{#_Toc262048280}[]{#_Toc262216530}[]{#_Toc262474062}[]{#_Toc262048281}[]{#_Toc262216531}[]{#_Toc262474063}[]{#_Toc262048282}[]{#_Toc262216532}[]{#_Toc262474064}[]{#_Toc262048283}[]{#_Toc262216533}[]{#_Toc262474065}[]{#_Toc262048284}[]{#_Toc262216534}[]{#_Toc262474066}[]{#_Toc262048285}[]{#_Toc262216535}[]{#_Toc262474067}[]{#_Toc262048286}[]{#_Toc262216536}[]{#_Toc262474068}[]{#_Toc262048288}[]{#_Toc262216538}[]{#_Toc262474070}[]{#_Toc262048290}[]{#_Toc262216540}[]{#_Toc262474072}[]{#_Toc262048291}[]{#_Toc262216541}[]{#_Toc262474073}[]{#_Toc262048292}[]{#_Toc262216542}[]{#_Toc262474074}[]{#_Toc262048293}[]{#_Toc262216543}[]{#_Toc262474075}[]{#_Toc262048294}[]{#_Toc262216544}[]{#_Toc262474076}[]{#_Toc262048295}[]{#_Toc262216545}[]{#_Toc262474077}[]{#_Toc262048296}[]{#_Toc262216546}[]{#_Toc262474078}[]{#_Toc262048297}[]{#_Toc262216547}[]{#_Toc262474079}[]{#_Toc262048298}[]{#_Toc262216548}[]{#_Toc262474080}[]{#_Toc262048299}[]{#_Toc262216549}[]{#_Toc262474081}[]{#_Toc262048300}[]{#_Toc262216550}[]{#_Toc262474082}[]{#_Toc262048301}[]{#_Toc262216551}[]{#_Toc262474083}[]{#_Toc262048302}[]{#_Toc262216552}[]{#_Toc262474084}[]{#_Toc262048303}[]{#_Toc262216553}[]{#_Toc262474085}[]{#_Toc262048304}[]{#_Toc262216554}[]{#_Toc262474086}
:::

::: {#2103272326 .myid}
[]{#_Toc404783114}[]{#struct_0_55199_x9544_1213882401}[]{#_Toc309658912}[]{#_Toc296584673}[]{#_Toc295572800}

**设备管理 \-- 设备管理配置命令 \-- job**

------------------------------------------------------------------------

[**[job]{lang="EN-US"}**]{#struct_0_55199_x9544_1252072167}[命令用来为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[分配]{style="font-family:宋体"}[Job]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo job]{lang="EN-US"}**]{#struct_0_55199_x9544_1891514793}[命令用来将]{style="font-family:宋体"}[Job]{lang="EN-US"}[从]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x91608449}

[**[job ]{lang="EN-US"}***[job-name]{lang="EN-US"}*]{#struct_0_55199_x9544_663266332}

[**[undo job]{lang="EN-US"}***[ job-name]{lang="EN-US"}*]{#struct_0_55199_x9544_1480485644}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1311948273}

[[没有为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_1937418457}[分配]{style="font-family:宋体"}[Job]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1943124330}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x519933622}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1892104617}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1724328699}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x195372847}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1719221394}

[*[job-name]{lang="EN-US"}*]{#struct_0_55199_x9544_1911656644}[：]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1691095531}

[[多次执行该命令，可以为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x515363411}[分配多个]{style="font-family:宋体"}[Job]{lang="EN-US"}[。多个]{style="font-family:宋体"}[Job]{lang="EN-US"}[在]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[指定的时间同时执行，没有先后顺序。]{style="font-family:宋体"}

[[分配的]{style="font-family:宋体"}[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x1531153271}[必须是设备上已经创建的]{style="font-family:宋体"}[Job]{lang="EN-US"}[，否则不能分配。]{style="font-family:宋体"}[Job]{lang="EN-US"}[可以通过]{style="font-family:宋体"}**[scheduler job]{lang="EN-US"}**[命令来创建。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1892170153}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_2115066003}[为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[分配一个名称为]{style="font-family:宋体"}[save-job]{lang="EN-US"}[的]{style="font-family:宋体"}[Job]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1267998246}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] job save-job]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1537820450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler job]{lang="EN-US"}**]{#struct_0_55199_x9544_x1138903869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x782122707}
:::

::::: {#483001519 .myid}
[]{#_Toc404783115}[]{#struct_0_55199_x9544_x1703217728}[]{#_Toc374113454}

**设备管理 \-- 设备管理配置命令 \-- locator blink**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image002.png){border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1299933201}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x1300340488}
:::

[ ]{lang="EN-US"}

[**[locator blink ]{lang="EN-US"}***[blink-time]{lang="EN-US"}*]{#struct_0_55199_x9544_x108381720}[命令用来定位设备的位置。]{style="font-family:宋体"}

[**[locator blink stop]{lang="EN-US"}**]{#struct_0_55199_x9544_1428950154}[命令用来停止定位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1661783362}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1832234681}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[locator blink ]{lang="EN-US"}***[blink-time]{lang="EN-US"}*]{#struct_0_55199_x9544_x1466416407}

[**[locator blink stop]{lang="EN-US"}**]{#struct_0_55199_x9544_266150740}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_117864362}[设备：]{style="font-family:宋体"}

[**[locator ]{lang="EN-US"}**[\[ **slot** *slot-number* \] **blink** *blink-time*]{lang="EN-US"}]{#struct_0_55199_x9544_x1621710498}

[**[locator]{lang="EN-US"}**[ \[ **slot** *slot-number* \] **blink** **stop**]{lang="EN-US"}]{#struct_0_55199_x9544_1381895987}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x690242183}[模式：（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[locator ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \] **blink** *blink-time*]{lang="EN-US"}]{#struct_0_55199_x9544_x184187954}

[**[locator ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \] **blink stop**]{lang="EN-US"}]{#struct_0_55199_x9544_x1571446219}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_804997377}[模式：（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[locator ]{lang="EN-US"}**[\[ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } \] **blink** *blink-time*]{lang="EN-US"}]{#struct_0_55199_x9544_1025600091}

[**[locator ]{lang="EN-US"}**[\[ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } \] **blink stop**]{lang="EN-US"}]{#struct_0_55199_x9544_491729829}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1671260875}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x540483850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1592222537}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x707402694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x137199323}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1031475787}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1299998737}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示对所有设备进行操作。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_681577462}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示对所有设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[进行操作。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_1743501575}[：显示指定成员设备上风扇的状态信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示对所有设备进行操作。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_55199_x9544_458405834}[：显示指定成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上风扇的状态信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号；]{style="font-family:宋体"}*[virtual-chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[在虚拟框中的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[参数时，表示对所有设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[进行操作。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[time ]{lang="EN-US"}***[blink-time]{lang="EN-US"}*]{#struct_0_55199_x9544_x1021003495}[：闪烁的持续时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[stop]{lang="EN-US"}**]{#struct_0_55199_x9544_x1295821051}[：停止闪烁。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1428884618}

[[配置]{style="font-family:宋体"}**[locator blink ]{lang="EN-US"}***[blink-time]{lang="EN-US"}*]{#struct_0_55199_x9544_1086414955}[命令后，指定设备上用于定位的]{style="font-family:宋体"}[LED]{lang="EN-US"}[灯会以间隔快闪的方式闪烁，并持续指定的时间。用户可根据]{style="font-family:宋体"}[LED]{lang="EN-US"}[灯的指示来定位设备所在的位置。]{style="font-family:宋体"}

[[不同型号的设备用于定位的]{style="font-family:宋体"}[LED]{lang="EN-US"}]{#struct_0_55199_x9544_1649822037}[灯不同，请以设备的实际情况为准。如果设备支持]{style="font-family:宋体"}[Locator]{lang="EN-US"}[灯，则]{style="font-family:宋体"}[Locator]{lang="EN-US"}[灯闪烁；如果只有]{style="font-family:宋体"}[SYS]{lang="EN-US"}[灯，则]{style="font-family:宋体"}[SYS]{lang="EN-US"}[灯闪烁；如果只有]{style="font-family:宋体"}[RUN]{lang="EN-US"}[灯，则]{style="font-family:宋体"}[RUN]{lang="EN-US"}[灯闪烁。]{style="font-family:宋体"}

[*[blink-time]{lang="EN-US"}*]{#struct_0_55199_x9544_1832169145}[时间到或者]{style="font-family:宋体"}[执行]{style="font-family:宋体"}**[locator blink stop]{lang="EN-US"}**[命令，则定位闪烁的]{style="font-family:宋体"}[LED]{lang="EN-US"}[灯会恢复正常点亮状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_266085204}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x650170604}[开始定位。]{style="font-family:宋体"}

[[\<Sysname\> locator blink 30]{lang="EN-US"}]{#struct_0_55199_x9544_x1370689019}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1381830451}[结束定位。]{style="font-family:宋体"}

[[\<Sysname\> locator blink stop]{lang="EN-US"}]{#struct_0_55199_x9544_1664841325}
:::::

::::: {#222885549 .myid}
[]{#_Toc404783116}[]{#struct_0_55199_x9544_x1750603265}[]{#_Toc387411220}

**设备管理 \-- 设备管理配置命令 \-- lpu-type**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image004.png){#图片 1 border="0" width="60" height="23"}]{lang="EN-US"}]{#struct_0_55199_x9544_x52690942}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x968025295}
:::

**[ ]{lang="EN-US"}**

[**[lpu-type]{lang="EN-US"}**]{#struct_0_55199_x9544_675964766}[命令用来配置设备支持的接口板类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x575154650}

[**[lpu-type]{lang="EN-US"}**[ { **e-series** \| **f-series** }]{lang="EN-US"}]{#struct_0_55199_x9544_x84224926}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1750603264}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1618774883}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_69345763}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1411455806}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x669097358}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_313020569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1643264681}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1900593215}

[**[e-series]{lang="EN-US"}**]{#struct_0_55199_x9544_144731994}[：配置设备只支持]{style="font-family:宋体"}[E]{lang="EN-US"}[系列的接口板]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[f-series]{lang="EN-US"}**]{#struct_0_55199_x9544_x1828364952}[：配置设备只支持]{style="font-family:宋体"}[F]{lang="EN-US"}[系列的接口板]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1619149958}

[[设备支持]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_55199_x9544_x1750603263}[系列的接口板和]{style="font-family:宋体"}[F]{lang="EN-US"}[系列的接口板。这]{style="font-family:宋体"}[两种类型的接口板不能互通，支持的特性有明显差异。请不要在同一台设备上同时插入这两种类型的接口板，即使插入，设备也只能识别指定类型的接口板。]{style="font-family:宋体"}

[[修改设备支持的接口板类型后，须重启设备才能生效。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x859259996}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x309124581}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_505463619}[将设备支持的接口板类型配置为]{style="font-family:宋体"}[E]{lang="EN-US"}[系列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x425633496}

[\[Sysname\] lpu-type e-series]{lang="EN-US"}

[Changing the LPU type to support. Continue? \[Y/N\]:y]{lang="EN-US"}

[LPU type changed. The change will take effect after a reboot.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_560947058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display lpu-type]{lang="EN-US"}**]{#struct_0_55199_x9544_x1879567519}
:::::

::: {#-628179475 .myid}
[]{#_Toc300730527}[]{#_Toc300730290}[]{#_Toc263066911}[]{#_Toc206560290}[]{#_Toc306695879}[]{#_Toc299977417}[]{#_Toc263066905}[]{#_Toc206560286}[]{#_Toc404783117}[]{#struct_0_55199_x9544_x1867031760}[]{#_Toc327350475}[]{#_Toc327178125}

**设备管理 \-- 设备管理配置命令 \-- memory-threshold**

------------------------------------------------------------------------

[**[memory-threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_x1384357059}[命令用来配置空闲内存告警的门限值。]{style="font-family:宋体"}

[**[undo memory-threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_1891580330}[命令用来恢复空闲内存告警的门限值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1641785335}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2022053846}

[**[memory-threshold minor ]{lang="EN-US"}***[minor-value]{lang="EN-US"}***[ severe ]{lang="EN-US"}***[severe-value]{lang="EN-US"}***[ critical ]{lang="EN-US"}***[critical-value ]{lang="EN-US"}***[normal ]{lang="EN-US"}***[normal-value]{lang="EN-US"}*]{#struct_0_55199_x9544_x1456679482}

[**[undo memory-threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_x1180952337}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_2132421635}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[memory-threshold]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **minor** *minor-value* **severe** *severe-value* **critical** *critical-value* **normal** *normal-value*]{lang="EN-US"}]{#struct_0_55199_x9544_1722061958}

[**[undo memory-threshold ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1974556545}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1891645866}[模式：]{style="font-family:宋体"}

[**[memory-threshold]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **minor** *minor-value* **severe** *severe-value* **critical** *critical-value* **normal** *normal-value*]{lang="EN-US"}]{#struct_0_55199_x9544_x1642351050}

[**[undo memory-threshold ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1484356262}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_79683994}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1223824139}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x284270483}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1134869440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_954971944}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1891711402}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1105126321}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x224785153}

[**[minor ]{lang="EN-US"}***[minor-value]{lang="EN-US"}*]{#struct_0_55199_x9544_1891776938}[：一级告警门限，单位为兆字节（]{style="font-family:宋体"}[MB]{lang="EN-US"}[），不同型号的设备取值范围不同，请以设备的实际情况为准；]{style="font-family:宋体"}*[minor-value]{lang="EN-US"}*[应小于等于]{style="font-family:宋体"}*[normal-value]{lang="EN-US"}*[；为]{style="font-family:宋体"}[0]{lang="EN-US"}[则表示关闭该级门限告警功能。]{style="font-family:宋体"}

[**[severe ]{lang="EN-US"}***[severe-value]{lang="EN-US"}*]{#struct_0_55199_x9544_1881948549}[：二级告警门限，单位为兆字节（]{style="font-family:宋体"}[MB]{lang="EN-US"}[），不同型号的设备取值范围不同，请以设备的实际情况为准；]{style="font-family:宋体"}*[severe-value]{lang="EN-US"}*[必须小于等于]{style="font-family:宋体"}*[minor-value]{lang="EN-US"}*[；为]{style="font-family:宋体"}[0]{lang="EN-US"}[则表示关闭该级门限告警功能。]{style="font-family:宋体"}

[**[critical ]{lang="EN-US"}***[critical-value]{lang="EN-US"}*]{#struct_0_55199_x9544_x178466441}[：三级告警门限，单位为兆字节（]{style="font-family:宋体"}[MB]{lang="EN-US"}[），不同型号的设备取值范围不同，请以设备的实际情况为准；]{style="font-family:宋体"}*[critical-value]{lang="EN-US"}*[必须小于等于]{style="font-family:宋体"}*[severe-value]{lang="EN-US"}*[；为]{style="font-family:宋体"}[0]{lang="EN-US"}[则表示关闭该级门限告警功能。]{style="font-family:宋体"}

[**[normal ]{lang="EN-US"}***[normal-value]{lang="EN-US"}*]{#struct_0_55199_x9544_x472334811}[：系统内存恢复正常状态时的内存大小，单位为兆字节（]{style="font-family:宋体"}[MB]{lang="EN-US"}[），不同型号的设备取值范围不同，请以设备的实际情况为准；]{style="font-family:宋体"}*[normal-value]{lang="EN-US"}*[必须小于等于实际内存大小。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_683791499}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x570612280}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_728631629}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_190376958}[：表示指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1981823370}[：表示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1822689677}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1992999692}

[[系统实时监控系统剩余空闲内存大小，当条件达到时，就产生相应的告警]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1891318186}[告警解除通知，以便通知关联的业务模块]{style="font-family:宋体"}[/]{lang="EN-US"}[进程采取相应的措施，以便最大限度的利用内存，又能保证设备的正常运行。]{style="font-family:宋体"}

[[设备支持一级、二级、三级告警门限，关于这些告警门限的详细介绍请参见"基础配置指导"中的"设备管理"。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1891449258}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1882341041}

[]{#struct_0_55199_x9544_1199303724}[]{#_Toc43895294}[]{#_Toc138238293}[]{#_Toc94930962}[]{#_Toc94586694}[]{#_Toc60036306}[]{#_Toc53707250}[]{#_Toc53518723}[]{#_Toc50837030}[\#]{lang="EN-US"}[ ]{lang="EN-US"}[一级、二级、三级告警门限分别为]{style="font-family:宋体"}[64MB]{lang="EN-US"}[、]{style="font-family:宋体"}[48MB]{lang="EN-US"}[、]{style="font-family:宋体"}[32MB]{lang="EN-US"}[，当系统剩余空闲内存大于]{style="font-family:宋体"}[96MB]{lang="EN-US"}[时，恢复到正常状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1324025087}

[\[Sysname\] memory-threshold minor 64 severe 48 critical 32 normal 96]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x137264859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_55199_x9544_x1703348800}**[memory-threshold]{lang="EN-US"}**
:::

::: {#-71215558 .myid}
[]{#_Toc404783118}[]{#struct_0_55199_x9544_x1996051197}[]{#_Toc372722672}[]{#_Toc367199925}

**设备管理 \-- 设备管理配置命令 \-- memory-threshold usage**

------------------------------------------------------------------------

[**[memory-threshold usage]{lang="EN-US"}**]{#struct_0_55199_x9544_x1300064273}[命令用来配置内存利用率阈值。]{style="font-family:宋体"}

[**[undo memory-threshold usage]{lang="EN-US"}**]{#struct_0_55199_x9544_1357459569}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_249386184}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1428819082}

[**[memory-threshold usage ]{lang="EN-US"}**]{#struct_0_55199_x9544_x923579309}*[memory-threshold]{lang="EN-US"}*

[**[undo memory-threshold usage]{lang="EN-US"}**]{#struct_0_55199_x9544_1832103609}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x708540009}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[memory-threshold ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_55199_x9544_209908034}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}**[ usage ]{lang="EN-US"}***[memory-threshold]{lang="EN-US"}*

[**[undo memory-threshold ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_55199_x9544_266019668}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}**[ usage]{lang="EN-US"}**

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_502465171}[模式：]{style="font-family:宋体"}

[**[memory-threshold]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_55199_x9544_1381764915}**[chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}**[ usage ]{lang="EN-US"}***[memory-threshold]{lang="EN-US"}*

[**[undo memory-threshold ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_55199_x9544_902515070}**[chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}**[usage]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x709471799}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x184319026}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_406262862}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1025469019}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x730575666}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2085708942}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x540614922}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1167081249}

[*[memory-threshold]{lang="EN-US"}*]{#struct_0_55199_x9544_x137330395}[：内存利用率阈值百分比，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_55199_x9544_x869080517}*[slot-number]{lang="EN-US"}*[：表示单板所在的槽位号，不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_55199_x9544_x1703414336}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x747059985}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_2101815764}[：表示指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1938793106}[：表示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1300129809}[：设置单板的指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的内存门限。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号]{style="font-family:宋体"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1994495153}

[[系统每隔]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_55199_x9544_1793766901}[分钟会对内存利用率进行采样，并将采样值和用户配置的内存利用率阈值比较。当采样值大时，则认为内存利用率过高，设备会发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1428753546}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1465356628}[配置内存利用率阈值为]{style="font-family:宋体"}[80%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1832038073}

[[\[Sysname\] memory-threshold chassis 1 slot 2 cpu 1 usage 80]{lang="EN-US"}]{#struct_0_55199_x9544_1597618680}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_265954132}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display memory-threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_1566352405}
:::

::: {#1394784268 .myid}
[]{#_Toc404783119}[]{#struct_0_55199_x9544_1690997085}[]{#_Toc358901098}

**设备管理 \-- 设备管理配置命令 \-- monitor cpu-usage enable**

------------------------------------------------------------------------

[**[monitor]{lang="EN-US"}[ cpu-usage enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1690997084}[命令用来开启]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率历史记录功能。]{style="font-family:宋体"}

[**[undo monitor]{lang="EN-US"}[ cpu-usage enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1300941864}[命令用来关闭]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率历史记录功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1690997079}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1690997078}

[**[monitor]{lang="EN-US"}[ cpu-usage enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1300679717}

[**[undo monitor]{lang="EN-US"}[ cpu-usage enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1690997081}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_1301269544}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}[ cpu-usage enable ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1690997080}

[**[undo monitor]{lang="EN-US"}[ cpu-usage enable ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1301204008}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1690997091}[模式：]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}[ cpu-usage enable ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1301269543}

[**[undo monitor]{lang="EN-US"}[ cpu-usage enable ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1690997090}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x265318053}

[[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_x573932528}[利用率历史记录功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x265318054}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x573604848}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x265318051}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x573801456}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x265318052}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x573998064}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x265318057}[：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x265318058}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，不指定表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1150344512}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_759910806}[：表示指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_348559921}[：表示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1822361997}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x265318055}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x573539312}[打开]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率历史记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x265318056}

[\[Sysname\] monitor cpu-usage enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x573735920}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cpu-usage configuration]{lang="EN-US"}**]{#struct_0_55199_x9544_1308660059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cpu-usage history]{lang="EN-US"}**]{#struct_0_55199_x9544_1308660061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor cpu-usage interval]{lang="EN-US"}**]{#struct_0_55199_x9544_1308660060}
:::

::: {#-1293577614 .myid}
[]{#_Toc404783120}[]{#struct_0_55199_x9544_1308660055}[]{#_Toc358901099}[]{#_Toc340215445}[]{#_Toc375581975}[]{#_Toc350522939}[]{#_Toc350523890}[]{#_Toc350522940}[]{#_Toc350523891}[]{#_Toc350522941}[]{#_Toc350523892}[]{#_Toc350522942}[]{#_Toc350523893}[]{#_Toc350522943}[]{#_Toc350523894}[]{#_Toc350522944}[]{#_Toc350523895}[]{#_Toc350522945}[]{#_Toc350523896}[]{#_Toc350522946}[]{#_Toc350523897}[]{#_Toc350522947}[]{#_Toc350523898}[]{#_Toc350522948}[]{#_Toc350523899}[]{#_Toc350522949}[]{#_Toc350523900}[]{#_Toc350522950}[]{#_Toc350523901}[]{#_Toc350522951}[]{#_Toc350523902}[]{#_Toc350522952}[]{#_Toc350523903}[]{#_Toc350522953}[]{#_Toc350523904}[]{#_Toc350522954}[]{#_Toc350523905}[]{#_Toc350522955}[]{#_Toc350523906}[]{#_Toc350522956}[]{#_Toc350523907}[]{#_Toc350522957}[]{#_Toc350523908}[]{#_Toc350522958}[]{#_Toc350523909}

**设备管理 \-- 设备管理配置命令 \-- monitor cpu-usage interval**

------------------------------------------------------------------------

[**[monitor cpu-usage interval]{lang="EN-US"}**]{#struct_0_55199_x9544_1308660054}[命令用来配置]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[利用率历史记录的采样周期。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_508044195}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1308660057}

[**[monitor cpu-usage interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_55199_x9544_1308660056}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_507913123}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor cpu-usage interval ]{lang="EN-US"}***[interval-value ]{lang="EN-US"}*[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1308660067}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_507978658}[模式：]{style="font-family:宋体"}

[**[monitor cpu-usage interval ]{lang="EN-US"}***[interval-value ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1308660066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_507913122}

[[CPU]{lang="EN-US"}]{#struct_0_55199_x9544_x647655077}[利用率历史记录采样周期为]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x647655078}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_458404801}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x647655075}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_459256769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x647655076}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_459060161}

[*[interval-value]{lang="EN-US"}*]{#struct_0_55199_x9544_x647655081}[：]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率历史记录采用周期，取值为]{style="font-family:宋体"}[5Sec]{lang="EN-US"}[、]{style="font-family:宋体"}[1Min]{lang="EN-US"}[或者]{style="font-family:宋体"}[5Min]{lang="EN-US"}[。输入该参数时，请完整输入，否则，系统会提示参数错误。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x647655082}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_458798022}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_59509069}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1416124711}[：表示指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1506683021}[：表示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1822427533}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x647655080}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_458929094}[配置]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率历史记录的采样周期为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x647655069}

[\[Sysname\] monitor cpu-usage interval 5Sec]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x647655070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cpu-usage configuration]{lang="EN-US"}**]{#struct_0_55199_x9544_926323035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cpu-usage history]{lang="EN-US"}**]{#struct_0_55199_x9544_926323034}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[monitor cpu-usage enable]{lang="EN-US"}**]{#struct_0_55199_x9544_926323037}
:::

::: {#-1200706753 .myid}
[]{#_Toc404783121}[]{#struct_0_55199_x9544_x1703479872}

**设备管理 \-- 设备管理配置命令 \-- monitor cpu-usage threshold**

------------------------------------------------------------------------

[**[monitor cpu-usage threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_x1300195345}[命令用来配置]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[利用率阈值。]{style="font-family:宋体"}

[**[undo monitor cpu-usage threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_471059607}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1295309185}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1428688010}

[**[monitor cpu-usage threshold ]{lang="EN-US"}***[cpu-threshold]{lang="EN-US"}*]{#struct_0_55199_x9544_620812405}

[**[undo monitor cpu-usage threshold]{lang="EN-US"}**]{#struct_0_55199_x9544_1831972537}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x189727447}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[monitor cpu-usage threshold ]{lang="EN-US"}***[cpu-threshold ]{lang="EN-US"}*[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_265888596}

[**[undo monitor cpu-usage threshold ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x39858150}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x1108692629}[模式：]{style="font-family:宋体"}

[**[monitor cpu-usage threshold ]{lang="EN-US"}***[cpu-threshold ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_1381633843}

[**[undo monitor cpu-usage threshold ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1828584815}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x184450098}

[[与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1974909711}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1025337947}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1816281244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1327827767}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x540745994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x383863898}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x137461467}

[*[cpu-threshold]{lang="EN-US"}*]{#struct_0_55199_x9544_x1643680258}[：]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率阈值百分比，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1703545408}[：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1972720087}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_818958420}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1918016734}[：表示指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1995646256}[：表示指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1300260881}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1988303261}

[[系统每隔]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_55199_x9544_1428622474}[分钟会对]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的利用率进行采样，并将采样值和用户配置的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率阈值比较。当采样值大时，则认为]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率过高，设备会发送]{style="font-family:宋体"}[Trap]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_681712845}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1831907001}[配置]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用率阈值为]{style="font-family:宋体"}[80%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>[ system-view]{.TerminalDisplayChar}]{lang="EN-US"}]{#struct_0_55199_x9544_x2136099293}

[[\[Sysname\] [monitor cpu-usage threshold 80]{.TerminalDisplayChar}]{lang="EN-US"}]{#struct_0_55199_x9544_1616411302}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_265823060}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cpu-usage configuration]{lang="EN-US"}**]{#struct_0_55199_x9544_23402573}
:::

::: {#366717010 .myid}
[]{#_Toc404783122}[]{#struct_0_55199_x9544_x1064361045}[]{#_Toc346287483}[]{#_Toc375581978}[]{#_Toc359569826}[]{#_Toc361930708}[]{#_Toc361991914}

**设备管理 \-- 设备管理配置命令 \-- password-recovery enable**

------------------------------------------------------------------------

[**[password-recovery enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1891514794}[命令用来使能密码恢复功能。]{style="font-family:
宋体"}

[**[undo password-recovery enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x92067201}[命令用来关闭密码恢复功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_617343695}

[**[password-recovery enable]{lang="EN-US"}**]{#struct_0_55199_x9544_372953765}

[**[undo password-recovery enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1893775146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2113123873}

[[密码恢复功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_55199_x9544_478976619}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1930736638}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x347192985}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1892104618}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1724787451}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1417920222}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1673855996}

[[配置密码恢复功能后，当用户忘记]{style="font-family:宋体"}[Console]{lang="EN-US"}]{#struct_0_55199_x9544_565547480}[口认证密码或者登录认证失败，导致无法使用命令行操作设备时，可通过]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单清除该认证密码，再继续使用设备；关闭密码恢复功能后，设备将处于一个安全性更高的状态，即当出现上述情况时，若想继续使用]{style="font-family:宋体"}[Console]{lang="EN-US"}[口对设备进行命令行操作，只能通过]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单选择将设备恢复为出厂配置之后方可继续操作，这样可以有效地防止非法用户获取启动配置文件。]{style="font-family:宋体"}

[[Boot ROM]{lang="EN-US"}]{#struct_0_55199_x9544_1537229348}[菜单中支持配置的选项与密码恢复功能的配置有关，详见产品的相关手册。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_773408157}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_762349308}[关闭密码恢复功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1892170154}

[\[Sysname\] undo password-recovery enable]{lang="EN-US"}
:::

::::: {#-645857532 .myid}
[]{#_Toc404783123}[]{#struct_0_55199_x9544_2114869395}

**设备管理 \-- 设备管理配置命令 \-- power-supply off**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image002.png){#图片 3 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_663955426}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_297804894}
:::

[ ]{lang="EN-US"}

[**[power-supply off]{lang="EN-US"}**]{#struct_0_55199_x9544_809927602}[命令用来强制给指定单板或子卡断电。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1942922320}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x909961925}

[**[power-supply off slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **subslot** *subslot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x837303030}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_992892624}[模式：]{style="font-family:宋体"}

[**[power-supply off chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **subslot** *subslot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x678336097}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_80920022}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1897373565}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1608892979}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1179698766}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_570081060}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x837237494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2095086569}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x860502818}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1263007140}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1424564612}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1778475218}[：表示]{style="font-family:宋体"}[子卡所在的子槽位号。不指定该参数时，表示所有子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x128413100}

[[如果设备电量不足，且某些接口板处于空闲状态或者连接的为非关键网络节点时，可以手工停止给这些接口板供电，以便节约电能保证给重要接口板供电。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2002100439}

[[在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x837171958}[中，当成员设备上处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理端口都位于同一接口板上时，则不允许强制给该接口板断电，以免导致]{style="font-family:宋体"}[IRF]{lang="EN-US"}[分裂。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x984257166}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_465740307}[强制给]{style="font-family:宋体"}[9]{lang="EN-US"}[号槽位的单板断电。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> power-supply off slot 9]{lang="EN-US"}]{#struct_0_55199_x9544_1753133765}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x955857114}[强制给成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板的单板断电。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:
宋体"}

[[\<Sysname\> power-supply off chassis 1 slot 3]{lang="EN-US"}]{#struct_0_55199_x9544_1828307663}
:::::

::::: {#-976790996 .myid}
[]{#_Toc404783124}[]{#struct_0_55199_x9544_1487978342}[]{#_Toc306695880}[]{#_Toc299977418}[]{#_Toc263066906}[]{#_Toc206560287}[]{#_Toc195417976}[]{#_Toc193873822}

**设备管理 \-- 设备管理配置命令 \-- power-supply on**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image002.png){#图片 4 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_235590007}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x837106422}
:::

[ ]{lang="EN-US"}

[**[power-supply on]{lang="EN-US"}**]{#struct_0_55199_x9544_631371992}[命令用来手工给指定单板或子卡供电。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x493218088}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x574717789}

[**[power-supply on slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ \[ **subslot ** *subslot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x868529744}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x230297364}[模式中：]{style="font-family:宋体"}

[**[power-supply on chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **subslot** *subslot-number* \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1620999142}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x694902295}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x837565174}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x550331536}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1458733655}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x361779790}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1311313613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1960937905}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1444807422}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x597252807}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_479018060}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[subslot ]{lang="EN-US"}***[subslot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x837499638}[：表示]{style="font-family:宋体"}[子卡所在的子槽位号。不指定该参数时，表示所有子卡。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x937553199}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1560652008}[手工给]{style="font-family:宋体"}[9]{lang="EN-US"}[号槽位的单板供电。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> power-supply on slot 9]{lang="EN-US"}]{#struct_0_55199_x9544_1060625410}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1401906544}[手工给成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板的单板供电。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:
宋体"}

[[\<Sysname\> power-supply on chassis 1 slot 3]{lang="EN-US"}]{#struct_0_55199_x9544_1270975973}
:::::

::::: {#1866157003 .myid}
[]{#_Toc404783125}[]{#struct_0_55199_x9544_168661428}[]{#_Toc306695881}[]{#_Toc299977419}[]{#_Toc263066907}[]{#_Toc206560288}[]{#_Toc195417979}[]{#_Toc193873825}

**设备管理 \-- 设备管理配置命令 \-- power-supply policy enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image002.png){#图片 5 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x837434102}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x2103373785}
:::

[ ]{lang="EN-US"}

[**[power-supply policy enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1851952776}[命令用来启用电源管理功能。]{style="font-family:
宋体"}

[**[undo power-supply policy enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1882602167}[命令用来关闭电源管理功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x347042316}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_544417587}

[**[power-supply policy enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x1982737187}

[**[undo power-supply policy enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x1966056675}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x837368566}[模式：]{style="font-family:宋体"}

[**[power-supply policy chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x199129328}

[**[undo power-supply policy chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ enable]{lang="EN-US"}**]{#struct_0_55199_x9544_250743853}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2093530305}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1637502031}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1496908370}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_470662206}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1550375304}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x836778742}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1317242762}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1648630835}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1395082130}[：]{style="font-family:宋体"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_761032568}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1218819818}[启用电源管理功能。（集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1760086088}

[\[Sysname\] power-supply policy enable]{lang="EN-US"}[]{#_Toc174438916}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1670687751}[启用成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的电源管理功能。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x836713206}

[\[Sysname\] power-supply policy chassis 1 enable]{lang="EN-US"}
:::::

::: {#356210413 .myid}
[]{#_Toc404783126}[]{#struct_0_55199_x9544_597448529}[]{#_Toc306695882}[]{#_Toc299977420}[]{#_Toc263066908}[]{#_Toc211673231}[]{#_Toc205094152}[]{#_Toc205000250}

**设备管理 \-- 设备管理配置命令 \-- power-supply policy priority**

------------------------------------------------------------------------

[**[power-supply policy priority]{lang="EN-US"}**]{#struct_0_55199_x9544_x32406961}[命令用来设置指定槽位单板的电源管理优先级。]{style="font-family:
宋体"}

[**[undo power-supply policy priority]{lang="EN-US"}**]{#struct_0_55199_x9544_x1471079962}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1223563295}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x708996841}

[**[power-supply policy slot ]{lang="EN-US"}***[slot-n]{lang="EN-US"}[umber]{lang="EN-US"}***[ priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_55199_x9544_x1373971720}

[**[undo power-supply policy slot]{lang="EN-US"}**[ *slot-number* **priority**]{lang="EN-US"}]{#struct_0_55199_x9544_1633761524}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x837303029}[模式：]{style="font-family:宋体"}

[**[power-supply policy chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-n]{lang="EN-US"}[umber]{lang="EN-US"}***[ priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_55199_x9544_993351375}

[**[undo power-supply policy chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number* **priority**]{lang="EN-US"}]{#struct_0_55199_x9544_x1707759816}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1679120010}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1673082086}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1674190388}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1957442783}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1706769247}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x837237493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2095414249}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_816244384}

[*[priority]{lang="EN-US"}*]{#struct_0_55199_x9544_1016122046}[：单板的电源管理优先级，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。本参数值越小表示单板的电源管理优先级越高。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_395123668}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1693081779}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x773069800}

[[请根据实际组网应用，将正在处理或将要处理重要业务的单板的优先级设置得高一些，以便在系统供电不足或者电力恢复时，优先保证对该单板的供电。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x13440985}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837171957}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x984060558}[设置]{style="font-family:宋体"}[1]{lang="EN-US"}[号槽位的单板的电源管理优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1634550785}

[\[Sysname\] power-supply policy slot 1 priority 10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x983493505}[设置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的电源管理优先级为]{style="font-family:
宋体"}[10]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x937111473}

[\[Sysname\] power-supply policy chassis 1 slot 1 priority 10]{lang="EN-US"}
:::

::::: {#-1569975245 .myid}
[]{#_Toc404783127}[]{#struct_0_55199_x9544_x1142264464}[]{#_Toc306695883}[]{#_Toc299977421}[]{#_Toc263066909}

**设备管理 \-- 设备管理配置命令 \-- power-supply policy redundant**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image002.png){#图片 6 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1705609450}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x837106421}
:::

[ ]{lang="EN-US"}

[**[power-supply policy redundant]{lang="EN-US"}**]{#struct_0_55199_x9544_631437528}[命令用来配置冗余电源模块数。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **power-supply policy redundant**]{lang="EN-US"}]{#struct_0_55199_x9544_154944726}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_208403528}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1378766352}

[**[power-supply policy redundant ]{lang="EN-US"}***[module-count]{lang="EN-US"}*]{#struct_0_55199_x9544_x1838075432}

[**[undo power-supply policy redundant]{lang="EN-US"}**]{#struct_0_55199_x9544_x1304206142}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_943496985}[模式：]{style="font-family:宋体"}

[**[power-supply policy chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[redundant ]{lang="EN-US"}***[module-count]{lang="EN-US"}*]{#struct_0_55199_x9544_x837565173}

[**[undo power-supply policy chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ redundant]{lang="EN-US"}**]{#struct_0_55199_x9544_x550003856}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1427860528}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x401985259}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1070741707}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1634811893}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_210458441}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1444812297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1215514765}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837499637}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1150475584}[：]{style="font-family:宋体"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[*[module-count]{lang="EN-US"}*]{#struct_0_55199_x9544_x937094447}[：表示冗余电源模块数目，不同型号的设备支持的取值范围不同，用户可以通过帮助信息来获取设备支持的取值范围，但是该范围的上限是系统支持的最大冗余模块数，根据设备安插的接口板的数量和耗电量不同，用户实际能够设置的值会小于等于系统支持的最大冗余模块数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_487921705}

[[只有在使能电源管理功能后，冗余电源配置才会生效。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x937728174}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_370837389}

[]{#_Toc184564416}[]{#_Toc174438918}[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x999840142}[配置电源冗余模块数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x837434101}

[\[Sysname\] power-supply policy redundant ]{lang="EN-US"}[3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x2103177177}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的电源冗余模块数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1221109068}

[\[Sysname\] power-supply policy chassis 1 redundant 3]{lang="EN-US"}
:::::

::: {#772218301 .myid}
[]{#_Toc404783128}[]{#struct_0_55199_x9544_x1396880074}

**设备管理 \-- 设备管理配置命令 \-- reboot**

------------------------------------------------------------------------

[**[reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_x763002230}[命令用来重启设备或者指定子卡。（集中式设备）]{style="font-family:宋体"}

[**[reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_x198178408}[命令用来重启指定单板、指定子卡或整个设备。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_x921665334}[命令用来重启指定成员设备、指定子卡或所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_x1315200058}[命令用来重启指定成员设备、指定子卡或所有成员设备。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837368565}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x199325936}

[**[reboot ]{lang="EN-US"}**[\[ **subslot** *subslot-number* \] \[ **force** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x214989928}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_55199_x9544_x428801219}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reboot ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **subslot** *subslot-number* \] \] \[ **force** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1659799946}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_337855851}[模式：]{style="font-family:宋体"}

[**[reboot ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \[ **slot** *slot-number* \[ **subslot** *subslot-number* \] \] \] \[ **force** \]]{lang="EN-US"}]{#struct_0_55199_x9544_x2113435629}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x836778741}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_1317439370}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1183986907}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_128475009}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1903003894}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_172643089}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_2093560676}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1625461938}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_438783056}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_x1063081991}[：表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_258590537}[：表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x836713205}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_59377997}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot]{lang="EN-US"}**[ *subslot-number*]{lang="EN-US"}]{#struct_0_55199_x9544_597382993}[：子卡所在的子槽位号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[force]{lang="EN-US"}**]{#struct_0_55199_x9544_x1401681623}[：强制重启：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定该参数时，重启设备，系统会做一些保护性检查（如启动文件是否存在，是否正在写磁盘等），若检查不通过则退出处理，不会重启设备；]{style="font-family:宋体"}]{#struct_0_55199_x9544_x906586891}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定该参数时，系统将不进行任何检查，直接执行重启操作。]{style="font-family:宋体"}]{#struct_0_55199_x9544_194370178}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x393270775}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_2053842300}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_1648176722}**[slot]{lang="EN-US"}**[参数，会导致整个设备重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_1872398358}**[slot]{lang="EN-US"}**[参数，不指定]{style="font-family:宋体"}**[sub]{lang="EN-US"}[slot]{lang="EN-US"}**[参数，会重启指定单板。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1232302001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新启动可能会导致业务中断，请谨慎使用该命令。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x837303028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用启动文件损坏或者不存在，则不能通过]{style="font-family:宋体"}]{#struct_0_55199_x9544_993416911}**[reboot]{lang="EN-US"}**[命令重启设备。此时，可以通过指定新的主用启动文件再重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x837237492}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_1832139172}**[force]{lang="EN-US"}**[参数时，系统在重启时不会做任何保护性措施。重启后，可能导致文件系统损坏，请谨慎使用该参数。建议在系统故障或无法正常重启时，才使用该参数。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_x2095479785}[设备：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_1031283759}**[slot]{lang="EN-US"}**[参数，会导致所有成员设备重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_1251248635}**[slot]{lang="EN-US"}**[参数，不指定]{style="font-family:宋体"}**[sub]{lang="EN-US"}[slot]{lang="EN-US"}**[参数，会重启指定成员设备。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_55199_x9544_800049704}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新启动可能会导致业务中断，请谨慎使用该命令。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x837171956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用启动文件损坏或者不存在，则不能通过]{style="font-family:宋体"}]{#struct_0_55199_x9544_x984126094}**[reboot]{lang="EN-US"}**[命令重启设备。此时，可以通过指定新的主用启动文件再重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x298111594}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_1831942564}**[force]{lang="EN-US"}**[参数时，系统在重启时不会做任何保护性措施。重启后，可能导致文件系统损坏，请谨慎使用该参数。建议在系统故障或无法正常重启时，才使用该参数。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_55199_x9544_x880234240}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_154539696}**[chassis]{lang="EN-US"}**[和]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数，则会重启所有成员设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_x837106420}**[chassis]{lang="EN-US"}**[不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数，则会重启]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定的成员设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同时指定]{style="font-family:宋体"}]{#struct_0_55199_x9544_631503064}**[chassis]{lang="EN-US"}**[和]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数，则会重启]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中指定的单板。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1432033380}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新启动可能会导致业务中断，请谨慎使用该命令。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x837565172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用启动文件损坏或者不存在，则不能通过]{style="font-family:宋体"}]{#struct_0_55199_x9544_x549938320}**[reboot]{lang="EN-US"}**[命令重启设备。此时，可以通过指定新的主用启动文件再重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1022052724}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_1831811492}**[force]{lang="EN-US"}**[参数时，系统在重启时不会做任何保护性措施。重启后，可能导致文件系统损坏，请谨慎使用该参数。建议在系统故障或无法正常重启时，才使用该参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x227426563}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_649795624}[当配置没有变化时，重启设备（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> reboot]{lang="EN-US"}]{#struct_0_55199_x9544_x837499636}

[Start to check configuration with next startup configuration file, please wait\...\...\...DONE!]{lang="EN-US"}

[This command will reboot the device. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x937159983}[当配置有变化时，重启设备，并选择保存配置文件（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> reboot]{lang="EN-US"}]{#struct_0_55199_x9544_x837217723}

[Start to check configuration with next startup configuration file, please wait\...\...\...DONE!]{lang="EN-US"}

[Current configuration will be lost after the reboot, save current configuration? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/startup.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):]{lang="EN-US"}

[flash:/startup.cfg exists, overwrite? \[Y/N\]:y]{lang="EN-US"}

[Validating file. Please wait\...]{lang="EN-US"}

[Configuration is saved to flash successfully.]{lang="EN-US"}

[This command will reboot the device. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x516848610}[当配置有变化时，重启设备，但不保存配置文件（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[\<Sysname\> reboot]{lang="EN-US"}]{#struct_0_55199_x9544_x1716488199}

[Start to check configuration with next startup configuration file, please wait\...\...\...DONE!]{lang="EN-US"}

[Current configuration will be lost after the reboot, save current configuration? \[Y/N\]:n]{lang="EN-US"}

[This command will reboot the device. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x837434100}[强制重启设备。]{style="font-family:宋体"}

[[\<Sysname\> reboot force]{lang="EN-US"}]{#struct_0_55199_x9544_x2103242713}

[A forced reboot might cause the storage medium to be corrupted. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1040601637}[重启接口板（接口板所在的槽位号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reboot slot 2]{lang="EN-US"}]{#struct_0_55199_x9544_471840812}

[Start to check configuration with next startup configuration file, please wait..]{lang="EN-US"}

[\...\....DONE!]{lang="EN-US"}

[This command will reboot the specified slot, Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x81291905}[强制重启接口板（接口板所在的槽位号为]{style="font-family:宋体"}[2]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> reboot slot 2 force]{lang="EN-US"}]{#struct_0_55199_x9544_x845610180}

[A forced reboot might cause the storage medium to be corrupted. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x837368564}[重启成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> reboot chassis 2]{lang="EN-US"}]{#struct_0_55199_x9544_x199260400}

[Start to check configuration with next startup configuration file, please wait..]{lang="EN-US"}

[\...\....DONE!]{lang="EN-US"}

[This command will reboot the specified chassis, Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_224404867}[强制重启成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reboot chassis 2 force]{lang="EN-US"}]{#struct_0_55199_x9544_9493556}

[A forced reboot might cause the storage medium to be corrupted. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x414698741}[重启成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> reboot chassis 2 slot 2]{lang="EN-US"}]{#struct_0_55199_x9544_x228427845}

[Start to check configuration with next startup configuration file, please wait..]{lang="EN-US"}

[\...\....DONE!]{lang="EN-US"}

[This command will reboot the specified slot, Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x764113727}[强制重启成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[2]{lang="EN-US"}[号接口板。]{style="font-family:宋体"}

[[\<Sysname\> reboot chassis 2 slot 2 force]{lang="EN-US"}]{#struct_0_55199_x9544_x836778740}

[A forced reboot might cause the storage medium to be corrupted. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now rebooting, please wait\...]{lang="EN-US"}
:::

::: {#-275225003 .myid}
[]{#_Toc404783129}[]{#struct_0_55199_x9544_x250179241}[]{#_Toc355966190}

**设备管理 \-- 设备管理配置命令 \-- restore factory-default**

------------------------------------------------------------------------

[**[restore factory-default]{lang="EN-US"}**]{#struct_0_55199_x9544_x250179242}[命令用来将设备恢复到出厂状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1584865855}

[**[restore factory-default]{lang="EN-US"}**]{#struct_0_55199_x9544_x250179239}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1584276034}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x250179240}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x250179229}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1584276033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x250179230}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1323798875}

[[当设备使用场景更改，或者设备出现故障时，可以使用本命令来将设备恢复到出厂状态。执行该命令后，设备将只保留"]{style="font-family:宋体"}[.bin]{lang="EN-US"}]{#struct_0_55199_x9544_x1323509666}["软件包、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、电子标签等维持设备正常工作必需的信息，其它文件和参数均恢复到出厂状态，例如，设备存储介质根目录下的所有配置文件（即后缀为"]{style="font-family:宋体"}[.cfg]{lang="EN-US"}["的文件）将被清除，设备在使用过程中生成的日志信息（即]{style="font-family:宋体"}[/logfile]{lang="EN-US"}[下的"]{style="font-family:宋体"}[.log]{lang="EN-US"}["文件以及]{style="font-family:宋体"}[logbuffer]{lang="EN-US"}[中的信息）、]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息、]{style="font-family:宋体"}[Debug]{lang="EN-US"}[信息将被清除，]{style="font-family:宋体"}[Boot ROM]{lang="EN-US"}[菜单中各选项的值将恢复到缺省值等。因此，请谨慎使用该命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1323798874}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1323798877}[将设备恢复到出厂状态。]{style="font-family:宋体"}

[[\<Sysname\> restore factory-default]{lang="EN-US"}]{#struct_0_55199_x9544_1323798876}

[This command will restore the system to the factory default configuration and clear the operation data. Continue \[Y/N\]:y]{lang="EN-US"}

[Restoring the factory default configuration. This process might take a few minutes. Please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}

[Please reboot the system to place the factory default configuration into effect.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1323575202}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_1323798871}
:::

::: {#-1852343178 .myid}
[]{#_Toc404783130}[]{#struct_0_55199_x9544_1317373834}

**设备管理 \-- 设备管理配置命令 \-- reset scheduler logfile**

------------------------------------------------------------------------

[**[reset scheduler logfile]{lang="EN-US"}**]{#struct_0_55199_x9544_x370759814}[命令用来清除]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[日志文件的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x757929680}

[**[reset scheduler logfile]{lang="EN-US"}**]{#struct_0_55199_x9544_1914184498}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_391829355}

[[无]{style="font-family:宋体"}]{#struct_0_55199_x9544_146185867}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x836713204}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_597317457}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1997272651}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1419284548}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1985782991}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1187863171}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1685454380}[清除]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[日志文件的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> reset scheduler logfile]{lang="EN-US"}]{#struct_0_55199_x9544_1982432732}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837303027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display scheduler logfile]{lang="EN-US"}**]{#struct_0_55199_x9544_992958159}
:::

::::: {#-51898789 .myid}
[]{#_Toc404783131}[]{#struct_0_55199_x9544_1289340409}[]{#_Toc311530780}[]{#_Toc263066913}[]{#_Toc206560292}

**设备管理 \-- 设备管理配置命令 \-- reset version-update-record**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image003.png){#图片 36 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1016367211}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1404779054}
:::

[ ]{lang="EN-US"}

[**[reset version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_x1502659327}[命令用来清除设备启动软件包版本更新操作的记录。（集中式设备）]{style="font-family:
宋体"}

[**[reset version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_x1156487939}[命令用来清除主用主控板启动软件包版本更新操作的记录。（分布式设备－独立运行模式）]{style="font-family:
宋体"}

[**[reset version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_x837237491}[命令用来清除主设备启动软件包版本更新操作的记录。（集中式]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[reset version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_x2095283177}[命令用来清除全局主用主控板启动软件包版本更新操作的记录。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2064744324}

[**[reset version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_79562119}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1316053007}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_931408282}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1771030151}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2060588353}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_357424520}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837171955}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x983929486}[清除设备启动软件包版本更新操作的记录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x2102192870}

[\[Sysname\] reset version-update-record]{lang="EN-US"}

[This command will delete all records of version update. Continue? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1894778145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display version-update-record]{lang="EN-US"}**]{#struct_0_55199_x9544_2026484600}
:::::

::::: {#874997097 .myid}
[]{#_Toc309658914}[]{#_Toc296584670}[]{#_Toc404783132}[]{#struct_0_55199_x9544_x1220323977}[]{#_Toc311530781}[]{#_Toc263066914}[]{#_Toc248294242}[]{#_Toc308441425}[]{#_Toc308441426}[]{#_Toc308441427}

**设备管理 \-- 设备管理配置命令 \-- save-power delay-timer**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x787414183}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x837106419}
:::

[ ]{lang="EN-US"}

[**[save-power delay-timer]{lang="EN-US"}**]{#struct_0_55199_x9544_631961819}[命令用来设置设备从节能唤醒状态切换到节能休眠状态的时间间隔。]{style="font-family:宋体"}

[**[undo save-power delay-timer]{lang="EN-US"}**]{#struct_0_55199_x9544_603687755}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_477207242}

[**[save-power delay-timer ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_55199_x9544_x78837445}

[**[undo save-power delay-timer]{lang="EN-US"}**]{#struct_0_55199_x9544_19863311}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1103831981}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_93864202}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837565171}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x550134928}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1819205733}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1494061622}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1220731924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1725257700}

[*[time]{lang="EN-US"}*]{#struct_0_55199_x9544_331092453}[：设备从节能唤醒状态切换到节能休眠状态的时间间隔，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_55199_x9544_3132907}

[[使能节能功能后，设备可能处于节能休眠状态（]{style="font-family:宋体"}**[sleep]{lang="EN-US"}**]{#struct_0_55199_x9544_x837499635}[）或节能唤醒状态（]{style="font-family:宋体"}**[wake]{lang="EN-US"}**[）。当设备处于节能休眠状态时，只要用户按设备上的]{style="font-family:宋体"}[\<Mode\>]{lang="EN-US"}[按钮或者通过]{style="font-family:宋体"}[Console]{lang="EN-US"}[连接和设备之间有报文交互，设备会立即切换到节能唤醒状态；反之，当设备处于节能唤醒状态，且在]{style="font-family:宋体"}*[time]{lang="EN-US"}*[时间内用户没有按]{style="font-family:宋体"}[\<Mode\>]{lang="EN-US"}[按钮并且没有通过]{style="font-family:宋体"}[Console]{lang="EN-US"}[连接和设备之间有报文交互，设备会切换到节能休眠状态以便达到更节能的效果。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x937225519}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1508730135}[设置设备从节能唤醒状态切换到节能休眠状态的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_749440229}

[\[Sysname\] save-power delay-timer 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2014532868}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[save-power enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x1404956781}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[save-power mode]{lang="EN-US"}**]{#struct_0_55199_x9544_652885870}
:::::

::::: {#1604796234 .myid}
[]{#_Toc404783133}[]{#struct_0_55199_x9544_1629600826}[]{#_Toc311530782}[]{#_Toc263066915}[]{#_Toc248294243}

**设备管理 \-- 设备管理配置命令 \-- save-power enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x837434099}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_235999278}
:::

[ ]{lang="EN-US"}

[**[save-power enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x1879626231}[命令用来使能设备的节能功能。]{style="font-family:宋体"}

[**[undo save-power enable]{lang="EN-US"}**]{#struct_0_55199_x9544_1075967710}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_786004712}

[**[save-power enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x936482175}

[**[undo save-power enable]{lang="EN-US"}**]{#struct_0_55199_x9544_789302222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x981314065}

[[节能功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x837368563}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x198932720}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_236207442}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_82778553}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x2032368660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_826256865}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2013411277}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1862698472}[使能设备的节能功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x836778739}

[\[Sysname\] save-power enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1316915089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[save-power delay-timer]{lang="EN-US"}**]{#struct_0_55199_x9544_x836713203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[save-power mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x837303026}
:::::

::::: {#173088690 .myid}
[]{#_Toc404783134}[]{#struct_0_55199_x9544_993023695}[]{#_Toc311530783}[]{#_Toc263066916}

**设备管理 \-- 设备管理配置命令 \-- save-power mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 39 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_413682098}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x837237490}
:::

[ ]{lang="EN-US"}

[**[save-power mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x2095348713}[命令用于手工强制切换设备的节能状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x113757442}

[**[save-power mode]{lang="EN-US"}**[ { **sleep** \| **wake** }]{lang="EN-US"}]{#struct_0_55199_x9544_784222039}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1922029035}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x60573843}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1470142041}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_797449762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x837171954}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x983995022}

[**[sleep]{lang="EN-US"}**]{#struct_0_55199_x9544_x169767852}[：将设备切换到节能休眠状态。处于该状态的设备会强制关闭除]{style="font-family:宋体"}[SYS]{lang="EN-US"}[指示灯以外的面板上的所有指示灯，并自动使能所有以太网接口的节能功能。]{style="font-family:宋体"}

[**[wake]{lang="EN-US"}**]{#struct_0_55199_x9544_x264285791}[：将设备切换到节能唤醒状态。处于该状态的设备上的所有指示灯仍然正常亮、灭、闪烁，只是自动使能所有以太网接口的节能功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1831442528}

[[使能节能功能后，设备可能处于节能休眠状态（]{style="font-family:宋体"}**[sleep]{lang="EN-US"}**]{#struct_0_55199_x9544_1258638873}[）或节能唤醒状态（]{style="font-family:宋体"}**[wake]{lang="EN-US"}**[），节能休眠状态比节能唤醒状态更节能。两种状态的切换由按键、报文或者定时器触发，使用]{style="font-family:宋体"}**[save-power mode]{lang="EN-US"}**[命令可以不需要按键也不需要等到定时器超时来实现节能状态之间的快速切换。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x954349152}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_974398058}[将设备切换到节能休眠状态。]{style="font-family:宋体"}

[[\<Sysname\> save-power mode sleep]{lang="EN-US"}]{#struct_0_55199_x9544_x837106418}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_632027355}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[save-power enable]{lang="EN-US"}**]{#struct_0_55199_x9544_x10587153}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[save-power delay-time]{lang="EN-US"}**]{#struct_0_55199_x9544_1709598338}
:::::

::: {#-19259303 .myid}
[]{#_Toc404783135}[]{#struct_0_55199_x9544_x587675617}

**设备管理 \-- 设备管理配置命令 \-- scheduler job**

------------------------------------------------------------------------

[**[scheduler job]{lang="EN-US"}**]{#struct_0_55199_x9544_x1574925261}[命令用来创建]{style="font-family:宋体"}[Job]{lang="EN-US"}[并进入]{style="font-family:宋体"}[Job]{lang="EN-US"}[视图。如果]{style="font-family:宋体"}[Job]{lang="EN-US"}[已创建，则直接进入]{style="font-family:宋体"}[Job]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo scheduler job]{lang="EN-US"}**]{#struct_0_55199_x9544_17872038}[命令用来删除已创建的]{style="font-family:宋体"}[Job]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1974792988}

[**[scheduler job ]{lang="EN-US"}***[job-name]{lang="EN-US"}*]{#struct_0_55199_x9544_x837565170}

[**[undo scheduler job ]{lang="EN-US"}***[job-name]{lang="EN-US"}*]{#struct_0_55199_x9544_x550069392}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x704634406}

[[没有创建]{style="font-family:宋体"}[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x1862876145}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x168866603}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_2136464746}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2069088594}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_770998524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x837499634}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x937291055}

[*[job-name]{lang="EN-US"}*]{#struct_0_55199_x9544_x360157871}[：]{style="font-family:宋体"}[Job]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1349758727}

[[一个]{style="font-family:宋体"}[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x1778177608}[可以被多个]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[引用。]{style="font-family:宋体"}[Job]{lang="EN-US"}[视图下用户可以通过]{style="font-family:宋体"}**[command]{lang="EN-US"}**[命令为]{style="font-family:宋体"}[Job]{lang="EN-US"}[分配命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1197299572}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_896331553}[创建名称为]{style="font-family:宋体"}[backupconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Job]{lang="EN-US"}[并进入]{style="font-family:宋体"}[Job]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x868436806}

[\[Sysname\] scheduler job backupconfig]{lang="EN-US"}

[\[Sysname-job-backupconfig\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837434098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[command]{lang="EN-US"}**]{#struct_0_55199_x9544_235933742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x669849678}
:::

::: {#-1931331758 .myid}
[]{#_Toc404783136}[]{#struct_0_55199_x9544_x1931742839}[]{#_Toc309658915}[]{#_Toc296584682}[]{#_Toc295572809}

**设备管理 \-- 设备管理配置命令 \-- scheduler logfile size**

------------------------------------------------------------------------

[**[scheduler logfile size]{lang="EN-US"}**]{#struct_0_55199_x9544_x228471990}[命令用来设置]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[日志文件的大小。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1568508422}

[**[scheduler logfile size ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_55199_x9544_1609257087}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_815301108}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x837368562}[日志文件的大小为]{style="font-family:宋体"}[16KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x198867184}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_977902412}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1438459132}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1564886229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1729891943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1644976266}

[*[value]{lang="EN-US"}*]{#struct_0_55199_x9544_x759202006}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[日志文件的大小，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[，单位是]{style="font-family:宋体"}[KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_578357424}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x836778738}[日志文件用来记录]{style="font-family:宋体"}[Job]{lang="EN-US"}[下命令行的执行结果。如果该文件的大小超过了用户设置值，则系统会把老的记录删除，用来记录新的记录。如果要记录的日志信息超长，超过了日志文件的大小，则该日志超出的部分不会记录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1316849553}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1948857437}[设置]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[日志文件的大小为]{style="font-family:宋体"}[32KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x951911480}

[\[Sysname\] scheduler logfile size 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2066972251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display scheduler logfile]{lang="EN-US"}**]{#struct_0_55199_x9544_941109043}
:::

::: {#-1466299017 .myid}
[]{#_Toc404783137}[]{#struct_0_55199_x9544_474096302}[]{#_Toc309658916}[]{#_Toc296584677}[]{#_Toc295572804}[]{#_Toc294103496}[]{#_Toc308441430}[]{#_Toc308441431}[]{#_Toc308441432}

**设备管理 \-- 设备管理配置命令 \-- scheduler reboot at**

------------------------------------------------------------------------

[**[scheduler reboot at]{lang="EN-US"}**]{#struct_0_55199_x9544_x836713202}[命令用来指定设备重启的具体时间和日期。]{style="font-family:宋体"}

[**[undo scheduler reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_597710673}[命令用来取消重启时间的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1790435205}

[**[scheduler reboot at]{lang="EN-US"}**[ *time* \[ *date* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1878636025}

[**[undo scheduler]{lang="EN-US"}**[ **reboot**]{lang="EN-US"}]{#struct_0_55199_x9544_1004204133}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_359200405}

[[没有指定设备重启的具体时间和日期。]{style="font-family:宋体"}]{#struct_0_55199_x9544_1112744595}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_412276521}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_8372592}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837303025}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_993089231}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x395698976}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_33587600}

[*[time]{lang="EN-US"}*]{#struct_0_55199_x9544_1182274837}[：设备重启的时间，格式为]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[。]{style="font-family:宋体"}*[HH]{lang="EN-US"}*[代表小时，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[代表分钟，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[date]{lang="EN-US"}*]{#struct_0_55199_x9544_x1443083747}[：设备重启的日期，格式为]{style="font-family:宋体"}*[MM/DD/YYYY]{lang="EN-US"}*[（月]{style="font-family:宋体"}[/]{lang="EN-US"}[日]{style="font-family:宋体"}[/]{lang="EN-US"}[年）或者]{style="font-family:
宋体"}*[YYYY/MM/DD]{lang="EN-US"}*[（年]{style="font-family:
宋体"}[/]{lang="EN-US"}[月]{style="font-family:宋体"}[/]{lang="EN-US"}[日）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[YYYY]{lang="EN-US"}*]{#struct_0_55199_x9544_x1596785500}[的取值范围为]{style="font-family:
宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2035]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[MM]{lang="EN-US"}*]{#struct_0_55199_x9544_1155448535}[的取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[12]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[DD]{lang="EN-US"}*]{#struct_0_55199_x9544_x837237489}[的取值范围与具体月份有关。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2094758888}

[[如果没有指定]{style="font-family:宋体"}*[date]{lang="EN-US"}*]{#struct_0_55199_x9544_x499431318}[参数，并且：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设置的时间点在当前时间之后，则设备将在当天的该时间点重启；]{style="font-family:宋体"}]{#struct_0_55199_x9544_521646473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设置的时间点在当前时间之前，则设备将在第二天的该时间点重启。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1367029998}

[[多次配置]{style="font-family:宋体"}**[scheduler reboot at]{lang="EN-US"}**]{#struct_0_55199_x9544_x1554147895}[、]{style="font-family:宋体"}**[scheduler reboot delay]{lang="EN-US"}**[命令，最新配置生效。]{style="font-family:宋体"}

[[如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。]{style="font-family:宋体"}]{#struct_0_55199_x9544_700174922}

[[需要注意的是，该命令会使设备在将来的某个时间点重新启动，从而导致业务中断，请谨慎使用。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x600759536}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837171953}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x983798414}[假设系统的当前时间为]{style="font-family:宋体"}[2011]{lang="EN-US"}[年]{style="font-family:宋体"}[6]{lang="EN-US"}[月]{style="font-family:
宋体"}[6]{lang="EN-US"}[日]{style="font-family:宋体"}[11:43]{lang="EN-US"}[，设置设备在当天中午]{style="font-family:宋体"}[12:00]{lang="EN-US"}[重启。]{style="font-family:宋体"}

[[\<Sysname\> scheduler reboot at 12:00]{lang="EN-US"}]{#struct_0_55199_x9544_x520708042}

[Reboot system at 12:00:00 06/06/2011 (in 0 hours and 16 minutes). Confirm? \[Y/N\]:]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x966941098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler reboot delay]{lang="EN-US"}**]{#struct_0_55199_x9544_x1876584883}
:::

::: {#234410898 .myid}
[]{#_Toc404783138}[]{#struct_0_55199_x9544_482008493}[]{#_Toc309658917}[]{#_Toc296584678}[]{#_Toc295572805}[]{#_Toc294103497}

**设备管理 \-- 设备管理配置命令 \-- scheduler reboot delay**

------------------------------------------------------------------------

[**[scheduler reboot delay]{lang="EN-US"}**]{#struct_0_55199_x9544_x1828172688}[命令用来配置重启设备的延迟时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **scheduler reboot**]{lang="EN-US"}]{#struct_0_55199_x9544_x2086133658}[命令用来取消延时重启配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837106417}

[**[scheduler]{lang="EN-US"}**[ **reboot** **delay** *time*]{lang="EN-US"}]{#struct_0_55199_x9544_631568603}

[**[undo scheduler]{lang="EN-US"}**[ **reboot**]{lang="EN-US"}]{#struct_0_55199_x9544_x1427058769}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1546970211}

[[没有配置重启设备的延迟时间。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x413121875}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1556897146}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_896594895}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_278055335}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_584251005}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x837565169}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x550659217}

[*[time]{lang="EN-US"}*]{#struct_0_55199_x9544_1241195272}[：设备重启的等待时延，格式为]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟）或]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[（分钟）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_297330153}*[HH:MM]{lang="EN-US"}*[格式时，]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[，]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[的最大长度为]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_1244246857}*[MM]{lang="EN-US"}*[格式时，最大长度为]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1448900487}

[[如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x604568698}

[[需要注意的是，该命令会使设备在将来的某个时间点重新启动，从而导致业务中断，请谨慎使用。]{style="font-family:宋体"}]{#struct_0_55199_x9544_312907297}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837499633}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x936832303}[假设系统的当前时间为]{style="font-family:宋体"}[2011]{lang="EN-US"}[年]{style="font-family:宋体"}[6]{lang="EN-US"}[月]{style="font-family:
宋体"}[6]{lang="EN-US"}[日]{style="font-family:宋体"}[11:48]{lang="EN-US"}[，配置设备在]{style="font-family:宋体"}[88]{lang="EN-US"}[分钟后重启。]{style="font-family:宋体"}

[[\<Sysname\> scheduler reboot delay 88]{lang="EN-US"}]{#struct_0_55199_x9544_1160170573}

[Reboot system at 13:16 06/06/2011(in 1 hours and 28 minutes). Confirm? \[Y/N\]:]{lang="EN-US"}
:::

::: {#-1659834024 .myid}
[]{#_Toc404783139}[]{#struct_0_55199_x9544_x39103568}[]{#_Toc309658918}[]{#_Toc295572799}[]{#_Toc296584672}

**设备管理 \-- 设备管理配置命令 \-- scheduler schedule**

------------------------------------------------------------------------

[**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x1346010358}[命令用来创建]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[并进入相应的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[视图。如果]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[已创建，则直接进入]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x1480492608}[命令用来删除指定]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x837434097}

[**[scheduler schedule ]{lang="EN-US"}***[schedule-name]{lang="EN-US"}*]{#struct_0_55199_x9544_235606062}

[**[undo scheduler schedule ]{lang="EN-US"}***[schedule-name]{lang="EN-US"}*]{#struct_0_55199_x9544_1792874642}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_573712916}

[[没有创建]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_1001731122}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_622303270}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x708903023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1784249645}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x837368561}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x199063792}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1328494745}

[*[schedule-name]{lang="EN-US"}*]{#struct_0_55199_x9544_848940539}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1586178153}

[[使用]{style="font-family:宋体"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_412767725}[命令可以配置定时执行任务，让设备在指定时间执行指定命令。]{style="font-family:宋体"}

[[配置步骤如下：]{style="font-family:宋体"}]{#struct_0_55199_x9544_1723902725}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[使用]{lang="EN-US" style="font-family:宋体"}**[scheduler job]{lang="EN-US"}**]{#struct_0_55199_x9544_x1207690256}[命令创建]{lang="EN-US" style="font-family:宋体"}[Job]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[Job]{lang="EN-US"}]{#struct_0_55199_x9544_x836778737}[视图下，使用]{lang="EN-US" style="font-family:宋体"}**[command]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[配置]{style="font-family:宋体"}[需要执行的命令。]{lang="EN-US" style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[使用]{lang="EN-US" style="font-family:宋体"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_1317046161}[命令创建]{lang="EN-US" style="font-family:宋体"}[Schedule]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:宋体"}*

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_826207841}[视图下，使用]{lang="EN-US" style="font-family:宋体"}**[job]{lang="EN-US"}**[命令为]{lang="EN-US" style="font-family:宋体"}[Schedule]{lang="EN-US"}[分配]{lang="EN-US" style="font-family:宋体"}[Job]{lang="EN-US"}[。一个]{lang="EN-US" style="font-family:宋体"}[Schedule]{lang="EN-US"}[下可以分配多个]{lang="EN-US" style="font-family:宋体"}[Job]{lang="EN-US"}[，但必须是已创建的]{lang="EN-US" style="font-family:宋体"}[Job]{lang="EN-US"}[，否则分配失败。]{lang="EN-US" style="font-family:宋体"}

[[(5)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x906390285}[视图下，]{lang="EN-US" style="font-family:宋体"}[使用]{style="font-family:宋体"}**[user-role]{lang="EN-US"}**[命令为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[配置用户角色。]{style="font-family:宋体"}[一个]{lang="EN-US" style="font-family:宋体"}[Schedule]{lang="EN-US"}[下最多可以分配]{style="font-family:宋体"}[64]{lang="EN-US"}[个角色。]{style="font-family:宋体"}

[[(6)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_1901381758}[视图下，使用]{lang="EN-US" style="font-family:宋体"}**[time at]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[time once]{lang="EN-US"}**[或者]{lang="EN-US" style="font-family:宋体"}**[time repeating]{lang="EN-US"}**[命令来配置任务执行的时间。]{lang="EN-US" style="font-family:宋体"}[一个]{lang="EN-US" style="font-family:宋体"}[Schedule]{lang="EN-US"}[下只能设置一个执行时间。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_548903077}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1182426731}[创建名为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_895311909}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x840339715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[job]{lang="EN-US"}**]{#struct_0_55199_x9544_x836713201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time at]{lang="EN-US"}**]{#struct_0_55199_x9544_597645137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time ]{lang="EN-US"}**]{#struct_0_55199_x9544_984985585}**[once]{lang="EN-US"}**
:::

::::: {#259430797 .myid}
[]{#_Toc404783140}[]{#struct_0_55199_x9544_2067003666}[]{#_Toc300730528}[]{#_Toc300730291}[]{#_Toc263066919}[]{#_Toc206560296}[]{#_Toc136403379}[]{#_Toc124236662}[]{#_Toc380046869}

**设备管理 \-- 设备管理配置命令 \-- shutdown-interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1355242206}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_1436623164}
:::

**[ ]{lang="EN-US"}**

[**[shutdown-interval]{lang="EN-US"}**]{#struct_0_55199_x9544_1762036078}[命令用来设定定时检测的时间间隔。]{style="font-family:宋体"}

[**[undo shutdown-interval]{lang="EN-US"}**]{#struct_0_55199_x9544_728780911}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x810733898}

[**[shutdown-interval]{lang="EN-US"}***[ time]{lang="EN-US"}*]{#struct_0_55199_x9544_130446584}

[**[undo shutdown-interval]{lang="EN-US"}**]{#struct_0_55199_x9544_x1131058583}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1980193268}

[[定时检测的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_55199_x9544_x797965638}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1602976677}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1747848421}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_728846447}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_525938541}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_691916074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_507438915}

[*[time]{lang="EN-US"}*]{#struct_0_55199_x9544_x319812936}[：定时检测的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_612559340}

[[某些协议模块在特定情况下会自动关闭某个端口，比如当使能了]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_55199_x9544_620786535}[保护功能的端口收到配置消息时，]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[协议模块将自动关闭该端口。同时，系统会启动一个检测定时器，如果直到定时器超时（即经过]{style="font-family:宋体"}*[time]{lang="EN-US"}*[秒之后），该端口仍处于关闭状态，协议模块则自动激活该端口，令其恢复到真实的物理状态。]{style="font-family:宋体"}

[[需要注意的是，如果用户在端口定时检测过程中将检测时间间隔修改为]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_55199_x9544_x1069789583}[，修改时刻距协议关闭端口时间间隔为]{style="font-family:宋体"}[T]{lang="EN-US"}[。若]{style="font-family:宋体"}[T\<T1]{lang="EN-US"}[，则被关闭的端口会再经过]{style="font-family:宋体"}[T1-T]{lang="EN-US"}[时间后被恢复；若]{style="font-family:宋体"}[T\>=T1]{lang="EN-US"}[，则被关闭的端口会立即恢复。例如当前]{style="font-family:宋体"}*[time]{lang="EN-US"}*[设置为]{style="font-family:宋体"}[30]{lang="EN-US"}[，当端口被协议模块关闭]{style="font-family:宋体"}[2]{lang="EN-US"}[秒（]{style="font-family:宋体"}[T=2]{lang="EN-US"}[）后，修改]{style="font-family:宋体"}*[time]{lang="EN-US"}*[为]{style="font-family:宋体"}[10]{lang="EN-US"}[（]{style="font-family:宋体"}[T1=10]{lang="EN-US"}[），则该接口会再经过]{style="font-family:宋体"}[8]{lang="EN-US"}[秒后被恢复；如果当前]{style="font-family:宋体"}*[time]{lang="EN-US"}*[为]{style="font-family:宋体"}[30]{lang="EN-US"}[，端口被协议模块关闭]{style="font-family:宋体"}[10]{lang="EN-US"}[秒后，修改]{style="font-family:宋体"}*[time]{lang="EN-US"}*[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，则该端口会立即恢复。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_728911983}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x637457005}[设定定时检测时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_2045543617}

[\[Sysname\] shutdown-interval 100]{lang="EN-US"}
:::::

::: {#487995318 .myid}
[]{#_Toc136403380}[]{#_Toc98563159}[]{#_Toc73958732}[]{#_Toc65405836}[]{#_Toc404783141}[]{#struct_0_55199_x9544_x1381514532}[]{#_Toc300730529}[]{#_Toc300730292}[]{#_Toc263066921}

**设备管理 \-- 设备管理配置命令 \-- sysname**

------------------------------------------------------------------------

[**[sysname]{lang="EN-US"}**]{#struct_0_55199_x9544_324397805}[命令用来设置设备的名称。]{style="font-family:宋体"}

[**[undo sysname]{lang="EN-US"}**]{#struct_0_55199_x9544_149872394}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_102562431}

[**[sysname]{lang="EN-US"}**[ *sysname*]{lang="EN-US"}]{#struct_0_55199_x9544_497377585}

[**[undo sysname]{lang="EN-US"}**]{#struct_0_55199_x9544_728977519}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1827953625}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2115710422}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x277827826}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x645510644}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_925962546}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_713554794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1890542299}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_728518767}

[*[sysname]{lang="EN-US"}*]{#struct_0_55199_x9544_728584303}[：设备名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_444918358}

[[设备的名称对应于命令行接口的提示符，如设备的名称为]{style="font-family:宋体"}[Sysname]{lang="EN-US"}]{#struct_0_55199_x9544_728649839}[，则用户视图的提示符为]{style="font-family:宋体"}[\<Sysname\>]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_720877607}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1870721744}[设置设备的名称为]{style="font-family:宋体"}[R2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1134313457}

[\[Sysname\] sysname R2000]{lang="EN-US"}

[\[R2000\]]{lang="EN-US"}[]{#_Toc255981043}[]{#_Toc255995942}[]{#_Toc255995976}
:::

::::: {#2134897255 .myid}
[]{#_Toc300730530}[]{#_Toc300730293}[]{#_Toc263066923}[]{#_Toc404783142}[]{#struct_0_55199_x9544_x451516378}

**设备管理 \-- 设备管理配置命令 \-- system-working-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 14 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x459917621}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_x212811089}
:::

[ ]{lang="EN-US"}

[**[system-working-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x1847828850}[命令用来配置设备的工作模式。]{style="font-family:宋体"}

[**[undo system-working-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_x1752765953}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_728715375}

[**[system-working-mode]{lang="EN-US"}**[ { **advance** \| **bridgee** \| **expert** \| **routee** \| **standard** }]{lang="EN-US"}]{#struct_0_55199_x9544_1524164911}

[**[undo system-working-mode]{lang="EN-US"}**]{#struct_0_55199_x9544_2004246867}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x385548201}

[[设备工作在标准模式。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1284333581}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1113890664}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x678546684}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1059930615}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_729305199}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1910229651}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1823880615}

[**[advance]{lang="EN-US"}**]{#struct_0_55199_x9544_1119302359}[：将设备的工作模式设置为高级模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[bridgee]{lang="EN-US"}**]{#struct_0_55199_x9544_x385410033}[：将设备的工作模式设置为二层增强模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[expert]{lang="EN-US"}**]{#struct_0_55199_x9544_x1752765952}[：将设备的工作模式设置为专家模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[routee]{lang="EN-US"}**]{#struct_0_55199_x9544_x1325710101}[：将设备的工作模式设置为三层增强模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[standard]{lang="EN-US"}**]{#struct_0_55199_x9544_x528457744}[：将设备的工作模式设置为标准模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1456304960}

[[不同模式下设备支持的特性不同，或者相同的特性支持的规格不同，请根据实际需要配置。]{style="font-family:宋体"}]{#struct_0_55199_x9544_729370735}

[[要使修改的工作模式生效，必须重启设备。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x68439302}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x631058421}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_430212744}[将设备工作模式配置为高级模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x1805620141}

[\[Sysname\] system-working-mode advance]{lang="EN-US"}

[The system working mode is changed, it will take effect after system restart.]{lang="EN-US"}
:::::

::::: {#-320898865 .myid}
[]{#_Toc404783143}[]{#struct_0_55199_x9544_x166881140}

**设备管理 \-- 设备管理配置命令 \-- temperature-limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 15 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x43608481}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_728780912}
:::

**[ ]{lang="EN-US"}**

[**[temperature-limit]{lang="EN-US"}**]{#struct_0_55199_x9544_x810733899}[命令用于设置设备的温度告警门限。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **temperature-limit**]{lang="EN-US"}]{#struct_0_55199_x9544_130512120}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x769615770}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1812830065}

[**[temperature-limit]{lang="EN-US"}**[ { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* \[ *alarmlimit* \]]{lang="EN-US"}]{#struct_0_55199_x9544_63606797}

[**[undo temperature-limit]{lang="EN-US"}**[ { **hotspot** \| **inflow** \| **outflow** } *sensor-number*]{lang="EN-US"}]{#struct_0_55199_x9544_1758794471}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2122100164}

[**[temperature-limit]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **slot** *slot-number* \| **vent** } { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* \[ *alarmlimit* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1981404191}

[**[undo temperature-limit ]{lang="EN-US"}**[{ **slot** *slot-number* \| **vent** } { **hotspot** ]{lang="EN-US"}[\| **inflow** \| **outflow** } *sensor-number*]{lang="EN-US"}]{#struct_0_55199_x9544_728846448}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_525938540}[设备：]{style="font-family:宋体"}

[**[temperature-limit]{lang="EN-US"}**[ **slot** *slot-number*]{lang="EN-US"}[ { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* \[ *alarmlimit* \]]{lang="EN-US"}]{#struct_0_55199_x9544_691916073}

[**[undo temperature-limit slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ { **hotspot** ]{lang="EN-US"}[\| **inflow** \| **outflow** } *sensor-number*]{lang="EN-US"}]{#struct_0_55199_x9544_507438908}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_1636502187}[模式：]{style="font-family:宋体"}

[**[temperature-limit]{lang="EN-US"}**[ **chassis**]{lang="EN-US"}[ *chassis-number* { **slot** *slot-number* \| **vent** } { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* \[ *alarmlimit* \]]{lang="EN-US"}]{#struct_0_55199_x9544_57605557}

[**[undo temperature-limit chassis]{lang="EN-US"}**[ *chassis-number* { **slot** *slot-number* \| **vent** } { **hotspot** \| **inflow** \| **outflow** } *sensor-number*]{lang="EN-US"}]{#struct_0_55199_x9544_136612503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x189556045}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_55199_x9544_728911984}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x637457012}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_2045084866}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_632317167}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1313240426}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1517966235}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x156616948}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_x1898563795}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_728977520}[：配置指定单板上温度传感器的温度门限。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_55199_x9544_893035566}[：配置指定成员设备上温度传感器的温度门限。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[vent]{lang="EN-US"}**]{#struct_0_55199_x9544_x1152325632}[：配置位于机框、风扇框上面的温度传感器的温度门限。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[hotspot]{lang="EN-US"}**]{#struct_0_55199_x9544_x228723615}[：配置热点传感器]{style="font-family:宋体"}[的温度门限。热点传感器一般置于发热量较大的芯片附近，监测芯片温度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[inflow]{lang="EN-US"}**]{#struct_0_55199_x9544_x1114874035}[：配置入风传感器]{style="font-family:宋体"}[的温度门限。入风传感器一般置于入风口附近，监测环境温度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outflow]{lang="EN-US"}**]{#struct_0_55199_x9544_x2025091358}[：配置出风传感器]{style="font-family:宋体"}[的温度门限。出风传感器一般置于出风口附近，监测设备温度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[sensor-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1022322734}[：温度传感器的编号，取值为从]{style="font-family:宋体"}[1]{lang="EN-US"}[开始的正整数，每一个数字对应设备（单板）上的一个温度传感器。]{style="font-family:宋体"}

[*[lowlimit]{lang="EN-US"}*]{#struct_0_55199_x9544_x1739907780}[：低温告警门限，单位为摄氏度，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[warninglimit]{lang="EN-US"}*]{#struct_0_55199_x9544_2006897584}[：一般级（]{style="font-family:宋体"}[Warning]{lang="EN-US"}[）高温告警门限，单位为摄氏度，不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但必须大于低温告警门限。]{style="font-family:宋体"}

[*[alarmlimit]{lang="EN-US"}*]{#struct_0_55199_x9544_728518768}[：严重级（]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[）高温告警门限，单位为摄氏度，不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但必须大于一般级高温告警门限。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x386090074}

[[如果温度低于低温告警门限，系统会生成日志信息和告警信息提示用户；如果温度高于]{style="font-family:宋体"}[Warning]{lang="EN-US"}]{#struct_0_55199_x9544_x1857207293}[高温门限，系统会生成日志信息和告警信息提示用户；如果温度高于]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[高温门限，系统一方面通过反复打印日志信息和告警信息提示用户，另一方面还会通过设备面板上的指示指示灯来告警。]{style="font-family:宋体"}

[[配置时，需要注意的是：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x2080760480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[高温告警门限必须大于低温告警门限；]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1600868959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Alarm]{lang="EN-US"}]{#struct_0_55199_x9544_x452074489}[高温告警门限必须大于]{lang="EN-US" style="font-family:宋体"}[Warning]{lang="EN-US"}[高温告警门限。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1382686513}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_348741733}[配置入风方向]{style="font-family:宋体"}[1]{lang="EN-US"}[号温度传感器，低温门限为]{style="font-family:宋体"}[-10]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Warning]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[70]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[100]{lang="EN-US"}[摄氏度。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_728584304}

[\[sysname\] temperature-limit inflow 1 -10 70 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_444918365}[配置]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板上入风方向]{style="font-family:宋体"}[1]{lang="EN-US"}[号温度传感器，低温门限为]{style="font-family:宋体"}[-10]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Warning]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[70]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[100]{lang="EN-US"}[摄氏度。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1953151442}

[\[sysname\] temperature-limit slot 0 inflow 1 -10 70 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x437276581}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上入风方向]{style="font-family:宋体"}[1]{lang="EN-US"}[号温度传感器，低温门限为]{style="font-family:宋体"}[-10]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Warning]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[70]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[100]{lang="EN-US"}[摄氏度。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1809250483}

[\[sysname\] temperature-limit slot 1 inflow 1 -10 70 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1368663076}[配置]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板上入风方向]{style="font-family:宋体"}[1]{lang="EN-US"}[号温度传感器，低温门限为]{style="font-family:宋体"}[-10]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Warning]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[70]{lang="EN-US"}[摄氏度，]{style="font-family:宋体"}[Alarm]{lang="EN-US"}[级高温门限为]{style="font-family:宋体"}[100]{lang="EN-US"}[摄氏度。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x742346412}

[\[sysname\] temperature-limit chassis 1 slot 0 inflow 1 -10 70 100]{lang="EN-US"}
:::::

::: {#590439629 .myid}
[]{#_Toc404783144}[]{#struct_0_55199_x9544_728649840}[]{#_Toc309658919}

**设备管理 \-- 设备管理配置命令 \-- time at**

------------------------------------------------------------------------

[**[time at]{lang="EN-US"}**]{#struct_0_55199_x9544_x1235437520}[命令用来配置在指定时刻执行]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo time]{lang="EN-US"}**]{#struct_0_55199_x9544_1525148640}[命令用来为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[取消执行时间配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1508432028}

[**[time at ]{lang="EN-US"}***[time date]{lang="EN-US"}*]{#struct_0_55199_x9544_x803587535}

[**[undo time]{lang="EN-US"}**]{#struct_0_55199_x9544_x957985005}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1324985319}

[[没有为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_1698157801}[配置执行时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_728715376}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_1524164912}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2004312403}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x409850480}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_596439534}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x2132047370}

[*[time]{lang="EN-US"}*]{#struct_0_55199_x9544_x581843339}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的执行时间，格式为]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}*[HH]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[date]{lang="EN-US"}*]{#struct_0_55199_x9544_1915474133}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[执行的日期，格式为]{style="font-family:宋体"}*[MM/DD/YYYY]{lang="EN-US"}*[（月]{style="font-family:宋体"}[/]{lang="EN-US"}[日]{style="font-family:宋体"}[/]{lang="EN-US"}[年）或者]{style="font-family:宋体"}*[YYYY/MM/DD]{lang="EN-US"}*[（年]{style="font-family:宋体"}[/]{lang="EN-US"}[月]{style="font-family:宋体"}[/]{lang="EN-US"}[日）。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[YYYY]{lang="EN-US"}*]{#struct_0_55199_x9544_x1944660210}[的取值范围为]{style="font-family:
宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2035]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[MM]{lang="EN-US"}*]{#struct_0_55199_x9544_729305200}[的取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[12]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[DD]{lang="EN-US"}*]{#struct_0_55199_x9544_x1245620751}[的取值范围与具体月份有关。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_665602184}

[[配置的时间点必须晚于系统当前时间点，否则配置失败。]{style="font-family:宋体"}]{#struct_0_55199_x9544_606900980}

[[一个]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_396887562}[只能配置一个执行时间。因此，同一]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[视图下，多次执行]{style="font-family:宋体"}**[time at]{lang="EN-US"}**[、]{style="font-family:宋体"}**[time once]{lang="EN-US"}**[或]{style="font-family:宋体"}**[time repeating]{lang="EN-US"}**[命令时，最新配置生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x96169753}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1485483584}[配置]{style="font-family:宋体"}[2011]{lang="EN-US"}[年]{style="font-family:宋体"}[5]{lang="EN-US"}[月]{style="font-family:
宋体"}[11]{lang="EN-US"}[日]{style="font-family:宋体"}[1]{lang="EN-US"}[点]{style="font-family:宋体"}[1]{lang="EN-US"}[分执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_729370736}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time at 1:1 2011/05/11]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x68439305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x631058424}
:::

::: {#-1112071751 .myid}
[]{#_Toc404783145}[]{#struct_0_55199_x9544_430409352}[]{#_Toc309658920}[]{#_Toc308441440}[]{#_Toc308441444}[]{#_Toc308441445}[]{#_Toc308441446}

**设备管理 \-- 设备管理配置命令 \-- time once**

------------------------------------------------------------------------

[**[time once]{lang="EN-US"}**]{#struct_0_55199_x9544_x10577334}[命令用来为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[配置执行时间。]{style="font-family:宋体"}

[**[undo time]{lang="EN-US"}**]{#struct_0_55199_x9544_164461798}[命令用来为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[取消执行时间配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x953942892}

[**[time]{lang="EN-US"}**[ **once** **at** *time* \[ **month-date** *month-day* \| **week-day** *week-day*&\<1-7\> \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1167521343}

[**[time once delay]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_55199_x9544_728780913}

[**[undo time]{lang="EN-US"}**]{#struct_0_55199_x9544_x810733900}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1826392849}

[[没有为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x810559397}[配置执行时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_835781316}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x511974957}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x488463000}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_400150607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1398208581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_728846449}

[**[at ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_55199_x9544_525938539}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的执行时间，格式为]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}*[HH]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[month-date ]{lang="EN-US"}***[month-day]{lang="EN-US"}*]{#struct_0_55199_x9544_x499725022}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[在一个月中的哪天被执行。]{style="font-family:宋体"}*[month-day]{lang="EN-US"}*[表示日期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。如果指定了一个本月不存在的日期，则实际生效的时间为下一个月的该日期，比如，二月没有]{style="font-family:宋体"}[30]{lang="EN-US"}[号，则实际生效的时间为三月的]{style="font-family:宋体"}[30]{lang="EN-US"}[号。]{style="font-family:宋体"}

[**[week-day]{lang="EN-US"}**[ *week-day*&\<1-7\>]{lang="EN-US"}]{#struct_0_55199_x9544_510231579}[：]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[在一周中的哪（些）天被执行。]{style="font-family:宋体"}*[week-day]{lang="EN-US"}*[&\<1-7\>]{lang="EN-US"}[表示一周中任一天或几天的组合，]{style="font-family:宋体"}*[week-day]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}**[Mon]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Tue]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Wed]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Thu]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Fri]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Sat]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Sun]{lang="EN-US"}**[，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。设置多天时，字符串之间用空格分开。]{style="font-family:宋体"}

[**[delay ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_55199_x9544_x2071897591}[：指定]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[延迟执行的时间。格式为]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟）或]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[（分钟）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1266283360}*[HH:MM]{lang="EN-US"}*[格式时，]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[，]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[最大长度为]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_814554139}*[MM]{lang="EN-US"}*[格式时，最大长度为]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_760467884}

[[配置该命令后，]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_728911985}[在该设定时间点到达时执行，若当天]{style="font-family:宋体"}[/]{lang="EN-US"}[本月]{style="font-family:宋体"}[/]{lang="EN-US"}[本周该时间点已过去，则顺延到第二天]{style="font-family:宋体"}[/]{lang="EN-US"}[下月]{style="font-family:宋体"}[/]{lang="EN-US"}[下周。执行后下次再到达该时间点时]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[不再执行。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x637457011}[只能配置一个执行时间。因此，同一]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[视图下，多次执行]{style="font-family:宋体"}**[time at]{lang="EN-US"}**[、]{style="font-family:宋体"}**[time once]{lang="EN-US"}**[或]{style="font-family:宋体"}**[time repeating]{lang="EN-US"}**[命令时，最新配置生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2045281474}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x608982103}[当天的]{style="font-family:宋体"}[15]{lang="EN-US"}[点执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1580075152}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time once at 15:00]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_323206781}[最近到达的]{style="font-family:宋体"}[15]{lang="EN-US"}[号的]{style="font-family:宋体"}[15]{lang="EN-US"}[点执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_x532304185}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time once at 15:00 month-date 15]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_728977521}[最近一个周一和周五的]{style="font-family:宋体"}[12]{lang="EN-US"}[点整执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_893035567}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time once at 12:00 week-day mon fri]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1152325633}[延迟]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1337360326}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time once delay 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1005513408}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x1492159989}
:::

::: {#1475047916 .myid}
[]{#_Toc404783146}[]{#struct_0_55199_x9544_x1610488938}[]{#_Toc309658921}

**设备管理 \-- 设备管理配置命令 \-- time repeating**

------------------------------------------------------------------------

[**[time repeating]{lang="EN-US"}**]{#struct_0_55199_x9544_728518769}[命令用来配置重复执行]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的时间。]{style="font-family:宋体"}

[**[undo time]{lang="EN-US"}**]{#struct_0_55199_x9544_x386090073}[命令用来为]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[取消执行时间配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1857141757}

[**[time repeating ]{lang="EN-US"}**[\[ **at** *time* \[ *date* \] \] **interval** *interval-time*]{lang="EN-US"}]{#struct_0_55199_x9544_x951419819}

[**[time]{lang="EN-US"}**[ **repeating at** *time* \[ **month-date** \[ *month-day* *\|* **last** \] \| **week-day** *week-day*&\<1-7\> \]]{lang="EN-US"}]{#struct_0_55199_x9544_1658987205}

[**[undo time]{lang="EN-US"}**]{#struct_0_55199_x9544_x1161497684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1760143217}

[[没有配置重复执行]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_1470738812}[的时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2028965839}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_728584305}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_444918364}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_1953151443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x437342117}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_610913129}

[**[at]{lang="EN-US"}***[ time]{lang="EN-US"}*]{#struct_0_55199_x9544_245463718}[：表示重复执行的时间，格式为]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}*[HH]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。不指定该参数时，表示从现在开始。]{style="font-family:宋体"}

[*[date]{lang="EN-US"}*]{#struct_0_55199_x9544_854976653}[：指定]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[重复执行的开始日期，格式为]{style="font-family:宋体"}*[MM/DD/YYYY]{lang="EN-US"}*[（月]{style="font-family:宋体"}[/]{lang="EN-US"}[日]{style="font-family:宋体"}[/]{lang="EN-US"}[年）或者]{style="font-family:宋体"}*[YYYY/MM/DD]{lang="EN-US"}*[（年]{style="font-family:宋体"}[/]{lang="EN-US"}[月]{style="font-family:宋体"}[/]{lang="EN-US"}[日）。不指定该参数时，表示将来第一次到达]{style="font-family:
宋体"}[time]{lang="EN-US"}[的时间点的日期。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[YYYY]{lang="EN-US"}*]{#struct_0_55199_x9544_x1706843720}[的取值范围为]{style="font-family:
宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2035]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[MM]{lang="EN-US"}*]{#struct_0_55199_x9544_728649841}[的取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[12]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[DD]{lang="EN-US"}*]{#struct_0_55199_x9544_x1235437521}[的取值范围与具体月份有关。]{style="font-family:
宋体"}

[**[interval ]{lang="EN-US"}***[interval-time]{lang="EN-US"}*]{#struct_0_55199_x9544_x40935301}[：指定重复执行的时间间隔。格式为]{style="font-family:宋体"}*[HH:MM]{lang="EN-US"}*[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟）或]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[（分钟）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1366721433}*[HH:MM]{lang="EN-US"}*[格式时，]{style="font-family:宋体"}*[MM]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[，最大长度为]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1876173590}*[MM]{lang="EN-US"}*[格式时，取值的最小值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[最大长度为]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[**[month-date ]{lang="EN-US"}**[\[ *month-day* *\|* **last** \]]{lang="EN-US"}]{#struct_0_55199_x9544_1551953900}[：表示每月中的某一天。其中，]{style="font-family:宋体"}*[month-day]{lang="EN-US"}*[表示日期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。如果指定了一个本月不存在的日期，则实际生效的时间为下一个月的该日期，比如，二月没有]{style="font-family:宋体"}[30]{lang="EN-US"}[号，则实际生效的时间为三月的]{style="font-family:宋体"}[30]{lang="EN-US"}[号。]{style="font-family:宋体"}**[last]{lang="EN-US"}**[表示每月的最后一天。]{style="font-family:宋体"}

[**[week-day]{lang="EN-US"}**[ *week-day*&\<1-7\>]{lang="EN-US"}]{#struct_0_55199_x9544_1315161624}[：表示每周中的某（些）天。]{style="font-family:宋体"}*[week-day]{lang="EN-US"}*[&\<1-7\>]{lang="EN-US"}[表示一周中任一天或几天的组合，]{style="font-family:宋体"}*[week-day]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}**[Mon]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Tue]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Wed]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Thu]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Fri]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Sat]{lang="EN-US"}**[、]{style="font-family:宋体"}**[Sun]{lang="EN-US"}**[，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。设置多天时，字符串之间用空格分开。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_148279401}

[**[time repeating ]{lang="EN-US"}**[\[ **at** *time* \[ *date* \] \] **interval** *interval-time*]{lang="EN-US"}]{#struct_0_55199_x9544_728715377}[表示从指定时间开始，周期性执行]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time]{lang="EN-US"}**[ **repeating at** *time* \[ **month-date** \[ *month-day* *\|* **last** \] \| **week-day** *week-day*&\<1-7\> \]]{lang="EN-US"}]{#struct_0_55199_x9544_1524164913}[表示每月]{style="font-family:宋体"}[/]{lang="EN-US"}[每周的某（些）天重复执行]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_2004377939}[只能配置一个执行时间。因此，同一]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[视图下，多次执行]{style="font-family:宋体"}**[time at]{lang="EN-US"}**[、]{style="font-family:宋体"}**[time once]{lang="EN-US"}**[或]{style="font-family:宋体"}**[time repeating]{lang="EN-US"}**[命令时，最新配置生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_381711512}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_104684119}[配置从早上八点开始，每隔]{style="font-family:宋体"}[1]{lang="EN-US"}[小时执行一次名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_454014832}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time repeating at 8:00 interval 60]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_712692555}[配置从现在开始每天的]{style="font-family:宋体"}[12:00]{lang="EN-US"}[执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_729305201}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time repeating at 12:00 ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x1245620752}[配置从现在开始每个月]{style="font-family:宋体"}[5]{lang="EN-US"}[号的上午]{style="font-family:宋体"}[8]{lang="EN-US"}[点执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_262317657}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time repeating at 8:00 month-date 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1365982658}[配置从现在开始每个月的最后一天]{style="font-family:宋体"}[8]{lang="EN-US"}[点执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_1867660256}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time repeating at 8:00 month-date last]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_297030533}[配置从现在开始每个周五和周六的上午]{style="font-family:宋体"}[8]{lang="EN-US"}[点执行名称为]{style="font-family:宋体"}[saveconfig]{lang="EN-US"}[的]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_729370737}

[\[Sysname\] scheduler schedule saveconfig]{lang="EN-US"}

[\[Sysname-schedule-saveconfig\] time repeating at 8:00 week-day fri sat]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x68439304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_x631058423}
:::

::::: {#1126610829 .myid}
[]{#_Toc300730535}[]{#_Toc404783147}[]{#struct_0_55199_x9544_96743661}[]{#_Toc380046877}[]{#_Toc380046878}[]{#_Toc380046879}[]{#_Toc380046880}[]{#_Toc380046881}[]{#_Toc380046882}[]{#_Toc380046883}[]{#_Toc380046884}[]{#_Toc380046885}[]{#_Toc380046886}[]{#_Toc380046887}[]{#_Toc380046888}[]{#_Toc380046889}[]{#_Toc380046890}[]{#_Toc380046891}[]{#_Toc380046892}[]{#_Toc380046893}[]{#_Toc380046894}[]{#_Toc380046895}[]{#_Toc380046896}[]{#_Toc380046897}[]{#_Toc380046898}

**设备管理 \-- 设备管理配置命令 \-- usb disable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_1564139991}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_728911986}
:::

**[ ]{lang="EN-US"}**

[**[usb disable]{lang="EN-US"}**]{#struct_0_55199_x9544_x637457010}[命令用来关闭设备上所有的]{style="font-family:宋体"}[USB]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo usb disable]{lang="EN-US"}**]{#struct_0_55199_x9544_2045215938}[命令用来打开设备上所有的]{style="font-family:宋体"}[USB]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1037162817}

[**[usb disable]{lang="EN-US"}**]{#struct_0_55199_x9544_447544883}

[**[undo usb disable]{lang="EN-US"}**]{#struct_0_55199_x9544_x934446161}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1828193949}

[[设备上所有的]{style="font-family:宋体"}[USB]{lang="EN-US"}]{#struct_0_55199_x9544_x948774756}[接口处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_728977522}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_893035564}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1152325630}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1391523029}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_399713108}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_19567898}

[[在执行]{style="font-family:宋体"}**[usb disable]{lang="EN-US"}**]{#struct_0_55199_x9544_997082512}[命令前，请先使用]{style="font-family:宋体"}**[umount]{lang="EN-US"}**[命令卸载所有]{style="font-family:宋体"}[USB]{lang="EN-US"}[分区，否则命令执行失败。有关]{style="font-family:宋体"}**[umount]{lang="EN-US"}**[命令的详细介绍，请参见"基础配置命令参考"中的"文件系统管理"。]{style="font-family:宋体"}

[[用户可通过]{style="font-family:宋体"}[USB]{lang="EN-US"}]{#struct_0_55199_x9544_2140057962}[口进行文件的上传和下载或者接]{style="font-family:宋体"}[USB 3G Modem]{lang="EN-US"}[模块。缺省状态下]{style="font-family:宋体"}[USB]{lang="EN-US"}[口处于开启状态，用户可根据需要关闭]{style="font-family:宋体"}[USB]{lang="EN-US"}[口。]{style="font-family:宋体"}

[[缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_55199_x9544_1515458355}[支持该命令，非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[不支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1284968364}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_728518770}[关闭]{style="font-family:宋体"}[USB]{lang="EN-US"}[接口，请先]{style="font-family:宋体"}[umount]{lang="EN-US"}[所有]{style="font-family:宋体"}[USB]{lang="EN-US"}[分区。]{style="font-family:宋体"}

[[\<Sysname\> umount usba0:]{lang="EN-US" style="layout-grid-mode:line"}]{#struct_0_55199_x9544_1570225054}

[\<Sysname\> umount slot1]{lang="EN-US" style="layout-grid-mode:line"}[\#[usba0:]{style="layout-grid-mode:line"}]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US" style="layout-grid-mode:line"}

[\[Sysname\] usb disable]{lang="EN-US" style="layout-grid-mode:line"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x982412514}[打开]{style="font-family:宋体"}[USB]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="layout-grid-mode:line"}]{#struct_0_55199_x9544_x1319281741}

[\[Sysname\] undo usb disable]{lang="EN-US" style="layout-grid-mode:line"}
:::::

::: {#1580969545 .myid}
[]{#_Toc404783148}[]{#struct_0_55199_x9544_x906390284}

**设备管理 \-- 设备管理配置命令 \-- user-role**

------------------------------------------------------------------------

[**[user-role]{lang="EN-US"}**]{#struct_0_55199_x9544_945484041}[命令用来配置执行]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的定时任务时使用的用户角色。]{style="font-family:宋体"}

[**[undo user-role]{lang="EN-US"}**]{#struct_0_55199_x9544_1214137248}[命令用来将已经配置的用户角色从]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x906324748}

[**[user-role]{lang="EN-US"}**[ *role-name*]{lang="EN-US"}]{#struct_0_55199_x9544_2064696177}

[**[undo user-role ]{lang="EN-US"}***[role-name]{lang="EN-US"}*]{#struct_0_55199_x9544_655819570}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x906259212}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x288355790}[执行定时任务时使用的用户角色，为创建该]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[的用户的用户角色。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_912952217}

[[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_x906193676}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1018594241}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_255033927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x906652428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_140380268}

[*[role-name]{lang="EN-US"}*]{#struct_0_55199_x9544_x562742860}[：执行定时任务时使用的用户角色，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，区分大小写。可以是系统预定义的角色名称，包括]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[、]{style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[、]{style="font-family:宋体"}[level-0]{lang="EN-US"}[～]{style="font-family:宋体"}[level-15]{lang="EN-US"}[，也可以是自定义的用户角色名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1977808226}

[[用户角色中定义了允许用户操作哪些系统功能、资源对象以及可执行哪些命令。设备支持的每条命令执行时都需要相应的用户角色，如果本命令中配置的用户角色不能执行]{style="font-family:宋体"}**[command]{lang="EN-US"}**]{#struct_0_55199_x9544_x906586892}[命令中指定的命令行，则会导致]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[中的部分命令不能执行。管理员使用本命令可以限制低级别用户使用]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[执行高级别命令行。]{style="font-family:宋体"}

[[多次执行本命令可给]{style="font-family:宋体"}[Schedule]{lang="EN-US"}]{#struct_0_55199_x9544_194173570}[配置多个用户角色，系统会使用这些用户角色权限的并集去执行]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[。同一个]{style="font-family:宋体"}[Schedule]{lang="EN-US"}[最多可以配置]{style="font-family:宋体"}[64]{lang="EN-US"}[个用户角色。关于用户角色的详细描述请参见"基础配置指导"中的"]{style="font-family:宋体"}[RBAC]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x906521356}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1702651363}[配置执行定时任务]{style="font-family:宋体"}[test]{lang="EN-US"}[时使用的用户角色为]{style="font-family:宋体"}[rolename]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_226138172}

[\[Sysname\] scheduler schedule test]{lang="EN-US"}

[\[Sysname-schedule-test\] user-role rolename]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x906455820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[command]{lang="EN-US"}**]{#struct_0_55199_x9544_x230803349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scheduler schedule]{lang="EN-US"}**]{#struct_0_55199_x9544_723081134}
:::

::: {#-443134910 .myid}
[]{#_Toc404783149}[]{#struct_0_55199_x9544_81167475}

**设备管理 \-- 设备管理配置命令 \-- warm-reboot**

------------------------------------------------------------------------

[**[warm-reboot]{lang="EN-US"}**]{#struct_0_55199_x9544_x1604949303}[命令用来热重启设备，并可同时升级启动软件包。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1809150767}

[**[warm-reboot ]{lang="EN-US"}**[\[ **file ipe** *ipe-filename* \]]{lang="EN-US"}]{#struct_0_55199_x9544_1188882739}

[**[warm-reboot ]{lang="EN-US"}**[\[ **file** { **boot** *boot-package* \| **system** *system-package* \| **feature** *feature-package*&\<1-30\> } \]]{lang="EN-US"}]{#struct_0_55199_x9544_x1082421963}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x836030431}

[[用户视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1484916466}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1819268084}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x510481865}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_276192775}

[**[file]{lang="EN-US"}**]{#struct_0_55199_x9544_x2052557253}[：用于在热重启设备时，升级启动软件包（该启动软件包会被设置为主用下次启动软件包）。]{style="font-family:宋体"}

[**[ipe]{lang="EN-US"}***[ ipe-filename]{lang="EN-US"}*]{#struct_0_55199_x9544_583009120}[：表示]{style="font-family:宋体"}[IPE]{lang="EN-US"}[（]{style="font-family:宋体"}[Image Package Envelope]{lang="EN-US"}[，复合软件包套件）文件的名称，以]{style="font-family:宋体"}[.ipe]{lang="EN-US"}[作为后缀名，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[boot ]{lang="EN-US"}***[boot-package]{lang="EN-US"}*]{#struct_0_55199_x9544_x2116972676}[：]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包的名称，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**[ *system-package*]{lang="EN-US"}]{#struct_0_55199_x9544_303704395}[：]{style="font-family:宋体"}[System]{lang="EN-US"}[包的名称，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**[ *feature-package*]{lang="EN-US"}]{#struct_0_55199_x9544_x323649233}[：]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包的名称，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，从]{style="font-family:宋体"}[flash]{lang="EN-US"}[、]{style="font-family:宋体"}[cf]{lang="EN-US"}[、]{style="font-family:宋体"}[usb]{lang="EN-US"}[开始最多可输入]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，不区分大小写。]{style="font-family:宋体"}*[feature-package]{lang="EN-US"}*[&\<1-30\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1711858934}

[[当配置该命令时，命令中指定的软件包必须放在存储介质根目录下，文件名中必须且只能包含存储介质的名称。]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1223344373}

[[在热重启并同时升级时，要求如下（否则，热重启命令执行失败）：]{style="font-family:宋体"}]{#struct_0_55199_x9544_640560942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备必须支持]{style="font-family:宋体"}]{#struct_0_55199_x9544_40312496}[ISSU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备工作在非]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1262379546}[IRF]{lang="EN-US"}[模式，且没有配置]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[新启动软件包]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1495366560}[/IPE]{lang="EN-US"}[文件的升级方式必须为增量升级或者软重启方式，为其它方式时，不能使用该方式升级。]{style="font-family:宋体"}[用户可以使用]{lang="EN-US" style="font-family:宋体"}**[display version comp-matrix]{lang="EN-US"}**[命令来显示软件版本兼容信息。关于]{lang="EN-US" style="font-family:宋体"}[ISSU]{lang="EN-US"}[和升级方式的详细介绍请参见"基础配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[ISSU]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1616999421}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_994455161}[热重启设备，并同时升级]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}[flash:/devkit.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> warm-reboot file feature flash:/devkit.bin]{lang="EN-US"}]{#struct_0_55199_x9544_x1480272393}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:y]{lang="EN-US"}

[Verifying the file flash:/devkit.bin on slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/devkit.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Demo 2601006]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  1                           Warm Reboot]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[This operation maybe take several minutes, please wait\...\.....]{lang="EN-US"}

[[表1-24 ]{lang="EN-US"}[warm-reboot]{lang="EN-US"}]{#struct_0_55199_x9544_591730630}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1312064591}[[字段]{style="font-family:黑体"}]{#struct_0_55199_x9544_x859095019}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1665664073}

[[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]]{lang="EN-US"}]{#struct_0_55199_x9544_1063219282}

[[当前操作会删除上一次的日志信息和回滚点，并且未保存的配置可能会丢失，询问用户是否继续执行升级操作]{style="font-family:宋体"}]{#struct_0_55199_x9544_1466503809}

[[Verifying the file flash:/devkit.bin on slot 1\...Done.]{lang="EN-US"}]{#struct_0_55199_x9544_x99580132}

[[检验软件包的合法性]{style="font-family:宋体"}]{#struct_0_55199_x9544_x52525965}

[[Decompressing file *A* to *B*\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}]{#struct_0_55199_x9544_x1618609906}

[[将文件从位置]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_55199_x9544_303769931}[解压缩到位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*[。只有使用]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件升级时，才显示该信息]{style="font-family:宋体"}

[[Upgrade summary according to following table]{lang="NO-BOK"}]{#struct_0_55199_x9544_x1262314010}

[[升级信息摘要]{style="font-family:宋体"}]{#struct_0_55199_x9544_x859029483}

[[Running Version]{lang="EN-US"}]{#struct_0_55199_x9544_1869853872}

[[设备当前运行的相同类型软件包的产品版本号]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1665598537}

[[New Version]{lang="EN-US"}]{#struct_0_55199_x9544_1063284818}

[[将要升级的软件包的产品版本号]{style="font-family:宋体"}]{#struct_0_55199_x9544_1466569345}

[[Slot]{lang="EN-US"}]{#struct_0_55199_x9544_x99514596}

[[设备成员编号只能为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_55199_x9544_x52460429}

[[Upgrade Way]{lang="EN-US"}]{#struct_0_55199_x9544_x1618544370}

[[升级策略，取值]{style="font-family:宋体"}]{#struct_0_55199_x9544_303835467}[为]{style="font-family:宋体"}[Warm Reboot]{lang="NO-BOK"}[，]{style="font-family:宋体"}[表示通过热重启方式升级]{style="font-family:宋体"}

[[Upgrading software images to compatible versions. Continue? \[Y/N\]]{lang="EN-US"}]{#struct_0_55199_x9544_x1262248474}

[[询问用户是否执行兼容升级操作]{style="font-family:宋体"}]{#struct_0_55199_x9544_x858963947}

[[This operation maybe take several minutes, please wait\...\.....]{lang="EN-US"}]{#struct_0_55199_x9544_1869919408}

[[热重启过程需要一定时间，请稍候]{style="font-family:宋体"}]{#struct_0_55199_x9544_x1665533001}

[ ]{lang="EN-US"}

::::: {#-421990659 .myid}
[]{#_Toc404783150}[]{#struct_0_55199_x9544_793060567}

**设备管理 \-- 设备管理配置命令 \-- xbar**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理命令.files/image001.png){#图片 16 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_55199_x9544_x1141525659}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_55199_x9544_728584306}
:::

**[ ]{lang="EN-US"}**

[**[xbar]{lang="EN-US"}**]{#struct_0_55199_x9544_444918363}[命令用来配置主用主控板和备用主控板的负载模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1953151448}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_55199_x9544_x437931941}

[**[xbar ]{lang="EN-US"}**[{ **load-balance** \| **load-single** }]{lang="EN-US"}]{#struct_0_55199_x9544_x1766429095}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_55199_x9544_876351772}[模式：]{style="font-family:宋体"}

[**[xbar chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ { **load-balance** \| **load-single** }]{lang="EN-US"}]{#struct_0_55199_x9544_x1017930418}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1250008497}

[[主控板的负载模式为]{style="font-family:宋体"}**[load-single]{lang="EN-US"}**]{#struct_0_55199_x9544_728649842}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1235437522}

[[系统视图]{style="font-family:宋体"}]{#struct_0_55199_x9544_362349226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_55199_x9544_557978905}

[[network-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x1503851719}

[[mdc-admin]{lang="EN-US"}]{#struct_0_55199_x9544_x721620138}

[[【参数】]{style="font-family:黑体"}]{#struct_0_55199_x9544_1270743448}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_55199_x9544_1724885317}[：用来设置指定成员设备上主用主控板和备用主控板的负载模式。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[load-balance]{lang="EN-US"}**]{#struct_0_55199_x9544_728715378}[：设备的主用主控板和备用主控板共同参与报文的处理和转发。]{style="font-family:宋体"}

[**[load-single]{lang="EN-US"}**]{#struct_0_55199_x9544_1524164922}[：只有主用主控板能处理和转发报文，备用主控板仅备份主用主控板的数据、监控主用主控板的状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_55199_x9544_2004312406}

[[只有主用主控板和备用主控板同时在位时，配置的]{style="font-family:宋体"}**[load-balance]{lang="EN-US"}**]{#struct_0_55199_x9544_x410178160}[模式才会生效；否则，即便配置了]{style="font-family:宋体"}**[load-balance]{lang="EN-US"}**[模式，主用主控板也会自动切换到]{style="font-family:宋体"}**[load-single]{lang="EN-US"}**[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1124763924}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_1577683351}[配置主用主控板和备用主控板的负载模式为]{style="font-family:宋体"}**[load-balance]{lang="EN-US"}**[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_987998556}

[\[Sysname\] xbar load-balance]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_55199_x9544_x893734453}[配置成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上主用主控板和备用主控板的负载模式为]{style="font-family:宋体"}**[load-balance]{lang="EN-US"}**[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_55199_x9544_729305202}

[\[Sysname\] xbar chassis 2 load-balance]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_55199_x9544_x1245620753}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display xbar]{lang="EN-US"}**]{#struct_0_55199_x9544_1828401598}
:::::
