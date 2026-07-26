::: {#434161679 .myid}
[]{#_Toc404795539}[]{#struct_0_x1819_23372_x1868360011}[]{#_Toc351105887}

**CFD \-- CFD配置命令 \-- cfd ais enable**

------------------------------------------------------------------------

[**[cfd ais enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x1817345141}[命令用来开启告警抑制功能。]{style="font-family:宋体"}

[**[undo cfd ais enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x1664600752}[命令用来关闭告警抑制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2066753675}

[**[cfd ais enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x1868032331}

[**[undo cfd ais enable]{lang="EN-US"}**]{#struct_0_x1819_23372_47640325}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1307693918}

[[告警抑制功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1819_23372_608399317}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2025265670}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_56602220}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1867966795}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x316189291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x798227888}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x259352043}

[[\# ]{lang="PT-BR"}]{#struct_0_x1819_23372_1062996214}[开启告警抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1819_23372_x1568469432}

[\[Sysname\] cfd ais enable]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868163403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_x1060475715}**[ais]{lang="EN-US"}[ ]{lang="EN-US"}[level]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais period]{lang="EN-US"}**]{#struct_0_x1819_23372_138391241}
:::

::: {#-8961781 .myid}
[]{#_Toc404795540}[]{#struct_0_x1819_23372_x1990357738}[]{#_Toc351105888}

**CFD \-- CFD配置命令 \-- cfd ais level**

------------------------------------------------------------------------

[**[cfd ais level]{lang="EN-US"}**]{#struct_0_x1819_23372_1821910936}[命令用来配置]{style="font-family:宋体"}[AIS]{lang="EN-US"}[报文的发送级别。]{style="font-family:宋体"}

[**[undo cfd ais level]{lang="EN-US"}**]{#struct_0_x1819_23372_884880056}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1931059607}

[**[cfd ais level ]{lang="EN-US"}***[level-value]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1868097867}

[**[undo cfd ais level ]{lang="EN-US"}***[level-value]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1031930760}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1467149322}

[[没有配置]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_1967597470}[报文的发送级别。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1657570145}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x974904215}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1867770187}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1804154578}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1617753658}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1180018413}

[**[level ]{lang="EN-US"}***[level-value]{lang="EN-US"}*]{#struct_0_x1819_23372_671797913}[：表示]{style="font-family:宋体"}[AIS]{lang="EN-US"}[报文的发送级别，]{style="font-family:宋体"}*[level-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1273239682}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1867704651}

[[如果服务实例中没有配置]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_x654571886}[报文的发送级别，则该服务实例中的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[将无法发送]{style="font-family:宋体"}[AIS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_348749270}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1356102082}[配置服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内]{style="font-family:宋体"}[AIS]{lang="EN-US"}[报文的发送级别为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1819_23372_x1108601865}

[\[Sysname\] cfd ais level 3 service-instance 1]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868294478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_x578692975}**[ais]{lang="EN-US"}[ ]{lang="EN-US"}[enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais period]{lang="EN-US"}**]{#struct_0_x1819_23372_1531636729}
:::

::: {#1198092584 .myid}
[]{#_Toc404795541}[]{#struct_0_x1819_23372_1174547360}[]{#_Toc351105889}

**CFD \-- CFD配置命令 \-- cfd ais period**

------------------------------------------------------------------------

[**[cfd ais period]{lang="EN-US"}**]{#struct_0_x1819_23372_x1350468763}[命令用来配置]{style="font-family:宋体"}[AIS]{lang="EN-US"}[报文的发送周期。]{style="font-family:宋体"}

[**[undo cfd ais period]{lang="EN-US"}**]{#struct_0_x1819_23372_x249054255}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868228942}

[**[cfd ais period ]{lang="EN-US"}***[period-value]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x316576863}

[**[undo cfd ais period ]{lang="EN-US"}***[period-value]{lang="EN-US"}*[ **service-instance** *instance-id*]{lang="EN-US"}]{#struct_0_x1819_23372_840809398}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1691338976}

[[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_x553012232}[报文的发送周期为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x800978831}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1868425550}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1062109791}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1090706583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1710232133}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1285757999}

[**[period ]{lang="EN-US"}***[period-value]{lang="EN-US"}*]{#struct_0_x1819_23372_x1095772965}[：表示发送周期，]{style="font-family:宋体"}*[period-value]{lang="EN-US"}*[的取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1630741557}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868360014}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_2074337628}[配置服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内]{style="font-family:宋体"}[AIS]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1819_23372_1582067436}

[\[Sysname\] cfd ais period 60 service-instance 1]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_626185541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_x765952425}**[ais]{lang="EN-US"}[ ]{lang="EN-US"}[enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais level]{lang="EN-US"}**]{#struct_0_x1819_23372_x1868032334}
:::

::::: {#1390632749 .myid}
[]{#_Toc404795542}[]{#struct_0_x1819_23372_450924852}[]{#_Toc351105890}

**CFD \-- CFD配置命令 \-- cfd ais-track link-status global**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CFD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_23372_x1596869634}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_23372_x787037552}
:::

[ ]{lang="EN-US"}

[**[cfd ais-track link-status global]{lang="EN-US"}**]{#struct_0_x1819_23372_x559046189}[命令用来开启端口状态与]{style="font-family:宋体"}[AIS]{lang="EN-US"}[的联动功能。]{style="font-family:宋体"}

[**[undo cfd ais-track link-status global]{lang="EN-US"}**]{#struct_0_x1819_23372_360134138}[命令用来关闭端口状态与]{style="font-family:宋体"}[AIS]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1867966798}

[**[cfd ais-track link-status global]{lang="EN-US"}**]{#struct_0_x1819_23372_x719473818}

[**[undo cfd ais-track link-status global]{lang="EN-US"}**]{#struct_0_x1819_23372_x74156852}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_567653896}

[[端口状态与]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_743079829}[联动功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868163406}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1463760242}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x661395057}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x294688764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1758298513}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1396717013}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1868097870}[开启端口状态与]{style="font-family:宋体"}[AIS]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_x1340656699}

[\[Sysname\] cfd ais-track link-status global]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_377349140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status level]{lang="EN-US"}**]{#struct_0_x1819_23372_x1626883987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_1125187521}**[period]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_256884516}**[vlan]{lang="EN-US"}**
:::::

::::: {#-150704138 .myid}
[]{#_Toc404795543}[]{#struct_0_x1819_23372_x1867770190}[]{#_Toc351105891}

**CFD \-- CFD配置命令 \-- cfd ais-track link-status level**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CFD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_23372_1044574155}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_23372_x576687932}
:::

[ ]{lang="EN-US"}

[**[cfd ais-track link-status level]{lang="EN-US"}**]{#struct_0_x1819_23372_1764706758}[命令用来配置]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的发送级别。]{style="font-family:宋体"}

[**[undo cfd ais-track link-status]{lang="EN-US"}**]{#struct_0_x1819_23372_420089607}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1867704654}

[**[cfd ais-track link-status level ]{lang="EN-US"}***[level-value]{lang="EN-US"}*]{#struct_0_x1819_23372_x1414086773}

[**[undo cfd ais-track link-status level]{lang="EN-US"}**]{#struct_0_x1819_23372_115223191}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1668697929}

[[没有配置]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_1431854843}[报文的发送级别。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1421558187}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1819_23372_x1868294477}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1437729660}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1745926915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_2137752927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2102922829}

[**[level]{lang="EN-US"}***[ level-value]{lang="EN-US"}*]{#struct_0_x1819_23372_x912084991}[：表示]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的发送级别，]{style="font-family:宋体"}*[level-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868228941}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果端口上没有配置]{style="font-family:宋体"}]{#struct_0_x1819_23372_1249507078}[EAIS]{lang="EN-US"}[报文的发送级别，那么该端口将无法触发]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1819_23372_172555303}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x563441394}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x819096089}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的发送级别为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1819_23372_x1868425549}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-GigabitEthernet1/0/1\] cfd ais-track link-status level 3]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x860270046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_x901898082}**[global]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_899913414}**[period]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_1481131205}**[vlan]{lang="EN-US"}**
:::::

::::: {#424415369 .myid}
[]{#_Toc404795544}[]{#struct_0_x1819_23372_x1868360013}[]{#_Toc351105892}

**CFD \-- CFD配置命令 \-- cfd ais-track link-status period**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CFD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_23372_x654545727}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_23372_x2023314588}
:::

[ ]{lang="EN-US"}

[**[cfd ais-track link-status period]{lang="EN-US"}**]{#struct_0_x1819_23372_x759860790}[命令用来配置]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的发送周期。]{style="font-family:宋体"}

[**[undo cfd ais-track link-status period]{lang="EN-US"}**]{#struct_0_x1819_23372_x998968555}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1918599599}

[**[cfd ais-track link-status period ]{lang="EN-US"}***[period-value]{lang="EN-US"}*]{#struct_0_x1819_23372_x1868032333}

[**[undo cfd ais-track link-status period]{lang="EN-US"}**]{#struct_0_x1819_23372_1210439739}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x563399457}

[[没有配置]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_x2015301440}[报文的发送周期。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x75587976}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1819_23372_x1867966797}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_846610123}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x2061442544}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_344655104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2144317520}

[**[period ]{lang="EN-US"}***[period-value]{lang="EN-US"}*]{#struct_0_x1819_23372_1553133485}[：表示发送周期，]{style="font-family:宋体"}*[period-value]{lang="EN-US"}*[的取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868163405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果端口上没有配置]{style="font-family:宋体"}]{#struct_0_x1819_23372_102323699}[EAIS]{lang="EN-US"}[报文的发送周期，那么该端口将无法触发]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1819_23372_x517125405}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_687288298}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1627651656}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1819_23372_x1868097869}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-GigabitEthernet1/0/1\] cfd ais-track link-status period 60]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_581592066}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_x575605996}**[global]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_759128218}**[level]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_79582646}**[vlan]{lang="EN-US"}**
:::::

::::: {#-602572743 .myid}
[]{#_Toc404795545}[]{#struct_0_x1819_23372_x1867770189}[]{#_Toc351105893}

**CFD \-- CFD配置命令 \-- cfd ais-track link-status vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CFD命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_23372_x1328013304}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_23372_x516160830}
:::

[ ]{lang="EN-US"}

[**[cfd ais-track link-status vlan]{lang="EN-US"}**]{#struct_0_x1819_23372_x449785318}[命令用来配置]{style="font-family:
宋体"}[EAIS]{lang="EN-US"}[报文的发送]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cfd ais-track link-status vlan]{lang="EN-US"}**]{#struct_0_x1819_23372_x787303519}[命令用来删除指定的发送]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1421463564}

[**[cfd ais-track link-status vlan ]{lang="NL"}**]{#struct_0_x1819_23372_x1867704653}*[vlan-list]{lang="NL"}*

[**[undo cfd ais-track link-status vlan ]{lang="NL"}**]{#struct_0_x1819_23372_x1817371300}*[vlan-list]{lang="NL"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2114747186}

[[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_1847815448}[报文只在本端口的缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内发送。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_618194177}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1819_23372_x1868294480}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x935382087}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1033254032}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_418448291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1960606142}

[**[vlan ]{lang="NL"}**]{#struct_0_x1819_23372_425201448}*[vlan-list]{lang="NL"}*[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[EAIS]{lang="NL"}[报文发送的]{style="font-family:宋体"}[VLAN]{lang="NL"}[范围。]{style="font-family:宋体"}*[vlan-list]{lang="NL"}*[为]{style="font-family:宋体"}[VLAN]{lang="NL"}[列表]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[表示多个]{style="font-family:
宋体"}[VLAN]{lang="NL"}[。其表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868228944}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_489992191}[报文将在本命令所指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与本设备上实际存在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的交集内发送。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行本命令，将取各次所配置]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1840722491}[VLAN]{lang="EN-US"}[的合集。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1819_23372_588355522}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x365122088}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_733612527}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的发送]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1819_23372_x1868425552}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-GigabitEthernet1/0/1\] cfd ais-track link-status vlan 100 to 200]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2070058091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_1601236054}**[global]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_975703398}**[level]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ais-track link-status ]{lang="EN-US"}**]{#struct_0_x1819_23372_x1868360016}**[period]{lang="EN-US"}**
:::::

::: {#252718924 .myid}
[]{#_Toc123026768}[]{#_Toc404795546}[]{#struct_0_x1819_23372_1096622659}[]{#_cfd_cc_enable}[]{#_Toc286930982}[]{#_Toc286934368}[]{#_Toc286930983}[]{#_Toc286934369}[]{#_Toc286930984}[]{#_Toc286934370}[]{#_Toc286930985}[]{#_Toc286934371}[]{#_Toc286930986}[]{#_Toc286934372}[]{#_Toc286930987}[]{#_Toc286934373}[]{#_Toc286930988}[]{#_Toc286934374}[]{#_Toc286930989}[]{#_Toc286934375}[]{#_Toc286930990}[]{#_Toc286934376}[]{#_Toc286930991}[]{#_Toc286934377}[]{#_Toc286930992}[]{#_Toc286934378}[]{#_Toc286930993}[]{#_Toc286934379}[]{#_Toc286930994}[]{#_Toc286934380}[]{#_Toc286930995}[]{#_Toc286934381}[]{#_Toc286930996}[]{#_Toc286934382}[]{#_Toc286930997}[]{#_Toc286934383}[]{#_Toc286930999}[]{#_Toc286934385}[]{#_Toc286931000}[]{#_Toc286934386}[]{#_Toc286931001}[]{#_Toc286934387}[]{#_Toc286931002}[]{#_Toc286934388}[]{#_Toc286931003}[]{#_Toc286934389}[]{#_Toc286931004}[]{#_Toc286934390}[]{#_Toc286931005}[]{#_Toc286934391}[]{#_Toc286931006}[]{#_Toc286934392}[]{#_Toc286931007}[]{#_Toc286934393}[]{#_Toc286931008}[]{#_Toc286934394}[]{#_Toc286931009}[]{#_Toc286934395}[]{#_Toc286931010}[]{#_Toc286934396}[]{#_Toc286931011}[]{#_Toc286934397}[]{#_Toc286931012}[]{#_Toc286934398}[]{#_Toc286931013}[]{#_Toc286934399}[]{#_Toc286931014}[]{#_Toc286934400}[]{#_Toc286931015}[]{#_Toc286934401}[]{#_Toc286931016}[]{#_Toc286934402}[]{#_Toc286931017}[]{#_Toc286934403}[]{#_Toc286931018}[]{#_Toc286934404}[]{#_Toc286931020}[]{#_Toc286934406}[]{#_Toc286931021}[]{#_Toc286934407}[]{#_Toc286931022}[]{#_Toc286934408}[]{#_Toc286931023}[]{#_Toc286934409}[]{#_Toc286931024}[]{#_Toc286934410}[]{#_Toc286931025}[]{#_Toc286934411}[]{#_Toc286931026}[]{#_Toc286934412}[]{#_Toc286931027}[]{#_Toc286934413}[]{#_Toc286931028}[]{#_Toc286934414}[]{#_Toc286931029}[]{#_Toc286934415}[]{#_Toc286931030}[]{#_Toc286934416}[]{#_Toc286931031}[]{#_Toc286934417}[]{#_Toc286931032}[]{#_Toc286934418}[]{#_Toc286931033}[]{#_Toc286934419}[]{#_Toc286931034}[]{#_Toc286934420}[]{#_Toc286931035}[]{#_Toc286934421}[]{#_Toc286931036}[]{#_Toc286934422}[]{#_Toc286931037}[]{#_Toc286934423}[]{#_Toc286931039}[]{#_Toc286934425}[]{#_Toc286931040}[]{#_Toc286934426}[]{#_Toc286931041}[]{#_Toc286934427}[]{#_Toc286931042}[]{#_Toc286934428}[]{#_Toc286931043}[]{#_Toc286934429}[]{#_Toc286931044}[]{#_Toc286934430}[]{#_Toc286931045}[]{#_Toc286934431}[]{#_Toc286931046}[]{#_Toc286934432}[]{#_Toc286931047}[]{#_Toc286934433}[]{#_Toc286931048}[]{#_Toc286934434}[]{#_Toc286931049}[]{#_Toc286934435}[]{#_Toc286931050}[]{#_Toc286934436}[]{#_Toc286931051}[]{#_Toc286934437}[]{#_Toc286931052}[]{#_Toc286934438}[]{#_Toc286931053}[]{#_Toc286934439}[]{#_Toc286931054}[]{#_Toc286934440}[]{#_Toc286931055}[]{#_Toc286934441}[]{#_Toc286931056}[]{#_Toc286934442}[]{#_Toc286931059}[]{#_Toc286934445}[]{#_Toc286931060}[]{#_Toc286934446}[]{#_Toc286931061}[]{#_Toc286934447}[]{#_Toc286931062}[]{#_Toc286934448}[]{#_Toc286931063}[]{#_Toc286934449}[]{#_Toc286931064}[]{#_Toc286934450}[]{#_Toc286931065}[]{#_Toc286934451}[]{#_Toc286931066}[]{#_Toc286934452}[]{#_Toc286931067}[]{#_Toc286934453}[]{#_Toc286931068}[]{#_Toc286934454}[]{#_Toc286931069}[]{#_Toc286934455}[]{#_Toc286931070}[]{#_Toc286934456}[]{#_Toc286931071}[]{#_Toc286934457}[]{#_Toc286931072}[]{#_Toc286934458}[]{#_Toc286931073}[]{#_Toc286934459}[]{#_Toc286931074}[]{#_Toc286934460}[]{#_Toc286931075}[]{#_Toc286934461}[]{#_Toc286931076}[]{#_Toc286934462}[]{#_Toc286931077}[]{#_Toc286934463}[]{#_Toc286931078}[]{#_Toc286934464}[]{#_Toc286931081}[]{#_Toc286934467}[]{#_Toc286931082}[]{#_Toc286934468}[]{#_Toc286931083}[]{#_Toc286934469}[]{#_Toc286931084}[]{#_Toc286934470}[]{#_Toc286931085}[]{#_Toc286934471}[]{#_Toc286931086}[]{#_Toc286934472}[]{#_Toc286931087}[]{#_Toc286934473}[]{#_Toc286931088}[]{#_Toc286934474}[]{#_Toc286931089}[]{#_Toc286934475}[]{#_Toc286931090}[]{#_Toc286934476}[]{#_Toc286931091}[]{#_Toc286934477}[]{#_Toc286931092}[]{#_Toc286934478}[]{#_Toc286931093}[]{#_Toc286934479}[]{#_Toc286931094}[]{#_Toc286934480}[]{#_Toc286931095}[]{#_Toc286934481}[]{#_Toc286931096}[]{#_Toc286934482}[]{#_Toc286931097}[]{#_Toc286934483}[]{#_Toc286931098}[]{#_Toc286934484}[]{#_Toc286931100}[]{#_Toc286934486}[]{#_Toc286931101}[]{#_Toc286934487}[]{#_Toc286931103}[]{#_Toc286934489}[]{#_Toc286931104}[]{#_Toc286934490}[]{#_Toc286931105}[]{#_Toc286934491}[]{#_Toc286931106}[]{#_Toc286934492}[]{#_Toc286931107}[]{#_Toc286934493}[]{#_Toc286931108}[]{#_Toc286934494}[]{#_Toc286931109}[]{#_Toc286934495}[]{#_Toc286931110}[]{#_Toc286934496}[]{#_Toc286931111}[]{#_Toc286934497}[]{#_Toc286931112}[]{#_Toc286934498}[]{#_Toc286931113}[]{#_Toc286934499}[]{#_Toc286931114}[]{#_Toc286934500}[]{#_Toc286931115}[]{#_Toc286934501}[]{#_Toc286931116}[]{#_Toc286934502}[]{#_Toc286931117}[]{#_Toc286934503}[]{#_Toc286931118}[]{#_Toc286934504}[]{#_Toc286931119}[]{#_Toc286934505}[]{#_Toc286931120}[]{#_Toc286934506}[]{#_Toc286931122}[]{#_Toc286934508}[]{#_Toc286931123}[]{#_Toc286934509}

**CFD \-- CFD配置命令 \-- cfd cc enable**

------------------------------------------------------------------------

[**[cfd cc enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x199594192}[命令用来在接口下开启指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文发送功能。]{style="font-family:宋体"}

[**[undo cfd cc enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x829108722}[命令用来在接口下关闭指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文发送功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x511793749}

[**[cfd cc service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x1292602126}

[**[undo cfd cc service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x1468468988}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x394025445}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x442334450}[的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文发送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_70532742}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1819_23372_x1865072096}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x20010198}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x828649969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x574874865}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_754898284}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_142164486}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_116285740}[：表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x190741759}

[[以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1819_23372_1557639594}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_102651156}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_1511827410}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启服务实例]{style="font-family:宋体"}[5]{lang="EN-US"}[内]{style="font-family:宋体"}[MEP 3]{lang="EN-US"}[的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_x828584433}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] cfd cc service-instance 5 mep 3 enable]{lang="EN-US"}

[]{#struct_0_x1819_23372_x2004078900}[]{#_创建/删除维护域}[]{#_cfd_cc_interval}[【相关命令】]{style="font-family:
黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd cc interval]{lang="EN-US"}**]{#struct_0_x1819_23372_x1111433909}
:::

::: {#-1572688889 .myid}
[]{#_Toc404795547}[]{#struct_0_x1819_23372_560653744}

**CFD \-- CFD配置命令 \-- cfd cc interval**

------------------------------------------------------------------------

[**[cfd cc interval]{lang="EN-US"}**]{#struct_0_x1819_23372_194408735}[命令用来配置]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文中时间间隔域的值。]{style="font-family:宋体"}

[**[undo cfd cc interval]{lang="EN-US"}**]{#struct_0_x1819_23372_928382162}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1735264927}

[**[cfd cc interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x760462610}

[**[undo cfd cc interval]{lang="EN-US"}**[ \[ *interval-value* \] **service-instance** *instance-id*]{lang="EN-US"}]{#struct_0_x1819_23372_x2033907078}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_238502666}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x828518897}[发送的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文中时间间隔域的值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1334008294}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1576171438}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1845087542}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1611399981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1015426473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x293671468}

[**[interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_x1819_23372_x2044284466}[：表示]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文中时间间隔域（]{style="font-family:宋体"}[Interval]{lang="EN-US"}[域）的值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1651438905}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x828453361}

[[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_x1675075793}[报文中时间间隔域的值、]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文的发送间隔和远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的超时时间这三者之间的关系如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-1572688889#_Ref138497021)[所示。]{style="font-family:宋体"}

[]{#struct_0_x1819_23372_x1775522656}[]{#_Ref138497021}[]{#_Ref135397128}[]{#_Ref135391095}[[表1-1 ]{lang="EN-US"}[参数关系表]{style="font-family:
黑体"}]{#_Toc132605770}

[]{#table_struct_0_223051137}[[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_1868143650}[报文中时间间隔域的值]{style="font-family:黑体"}
:::

[[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_x1052397181}[报文的发送间隔]{style="font-family:黑体"}

[[远端]{style="font-family:黑体"}]{#struct_0_x1819_23372_1122438275}[MEP]{lang="EN-US"}[的超时时间]{style="font-family:黑体"}

[[1]{lang="EN-US"}]{#struct_0_x1819_23372_x33040335}

[[10/3]{lang="EN-US"}]{#struct_0_x1819_23372_510744369}[毫秒]{style="font-family:宋体"}

[[35/3]{lang="EN-US"}]{#struct_0_x1819_23372_x828387825}[毫秒]{style="font-family:宋体"}

[[2]{lang="EN-US"}]{#struct_0_x1819_23372_x112948130}

[[10]{lang="EN-US"}]{#struct_0_x1819_23372_x792234023}[毫秒]{style="font-family:宋体"}

[[35]{lang="EN-US"}]{#struct_0_x1819_23372_962525164}[毫秒]{style="font-family:宋体"}

[[3]{lang="EN-US"}]{#struct_0_x1819_23372_x347814328}

[[100]{lang="EN-US"}]{#struct_0_x1819_23372_x632733848}[毫秒]{style="font-family:宋体"}

[[350]{lang="EN-US"}]{#struct_0_x1819_23372_x828322289}[毫秒]{style="font-family:宋体"}

[[4]{lang="EN-US"}]{#struct_0_x1819_23372_1845684789}

[[1]{lang="EN-US"}]{#struct_0_x1819_23372_1499361584}[秒]{style="font-family:宋体"}

[[3.5]{lang="EN-US"}]{#struct_0_x1819_23372_x614931411}[秒]{style="font-family:宋体"}

[[5]{lang="EN-US"}]{#struct_0_x1819_23372_x1095999899}

[[10]{lang="EN-US"}]{#struct_0_x1819_23372_1715330258}[秒]{style="font-family:宋体"}

[[35]{lang="EN-US"}]{#struct_0_x1819_23372_x828256753}[秒]{style="font-family:宋体"}

[[6]{lang="EN-US"}]{#struct_0_x1819_23372_1095833467}

[[60]{lang="EN-US"}]{#struct_0_x1819_23372_1499134426}[秒]{style="font-family:宋体"}

[[210]{lang="EN-US"}]{#struct_0_x1819_23372_x1823069448}[秒]{style="font-family:宋体"}

[[7]{lang="EN-US"}]{#struct_0_x1819_23372_x1465481220}

[[600]{lang="EN-US"}]{#struct_0_x1819_23372_x828191217}[秒]{style="font-family:宋体"}

[[2100]{lang="EN-US"}]{#struct_0_x1819_23372_x855739023}[秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CFD命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_23372_x361815317}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[]{#struct_0_x1819_23372_2130405582}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:KaiTi_GB2312"}1-1]{lang="EN-US"}](?-1572688889#_Ref138497021)[中时间间隔域的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1080738319}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x692923846}[配置服务实例]{style="font-family:宋体"}[2]{lang="EN-US"}[内]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文中时间间隔域的值为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_2030160052}

[\[Sysname\] cfd cc interval 7 service-instance 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x829174257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd cc enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x95015322}

::: {#-1228955664 .myid}
[]{#_Toc404795548}[]{#struct_0_x1819_23372_x1868360015}[]{#_Toc351105896}

**CFD \-- CFD配置命令 \-- cfd dm one-way**

------------------------------------------------------------------------

[**[cfd dm one-way]{lang="EN-US"}**]{#struct_0_x1819_23372_508253687}[命令用来开启单向时延测试功能，通过从源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送]{style="font-family:宋体"}[1DM]{lang="EN-US"}[报文到目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[来测试设备间的单向时延。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868032335}

[**[cfd dm one-way service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } \[ **number** *number* \]]{lang="EN-US"}]{#struct_0_x1819_23372_2017008793}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x783770251}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1867966799}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2009409537}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1621832035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_693443600}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1868163407}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1265123113}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1341567359}[：表示源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1819_23372_904395817}[：表示目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mep]{lang="EN-US"}***[ target-mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x2050357342}[：表示目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[target-mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x1819_23372_x1868097871}[：表示]{style="font-family:宋体"}[1DM]{lang="EN-US"}[报文的发送数量，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_225427242}

[[单向时延的测试结果需在目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_183250710}[上通过]{style="font-family:宋体"}**[display cfd dm one-way history]{lang="EN-US"}**[命令来显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x310462809}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1867770191}[在服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内测试源]{style="font-family:宋体"}[MEP 1101]{lang="EN-US"}[到目标]{style="font-family:宋体"}[MEP 1003]{lang="EN-US"}[的单向时延。]{style="font-family:宋体"}

[[\<Sysname\> cfd dm one-way service-instance 1 mep 1101 target-mep 1003]{lang="PT-BR"}]{#struct_0_x1819_23372_x1684309200}

[5 1DMs have been sent. Please check the result on the remote device.]{lang="PT-BR"}

[]{#struct_0_x1819_23372_x471151945}[[表1-2 ]{lang="EN-US"}[cfd dm one-way]{lang="EN-US"}]{#_Toc239048808}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1580666491}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1885434531}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1867704655}

[[5 1DMs have been sent]{lang="EN-US"}]{#struct_0_x1819_23372_1314796582}

[[已发送]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1819_23372_891022834}[个]{style="font-family:宋体"}[1DM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Please check the result on the remote device]{lang="EN-US"}]{#struct_0_x1819_23372_x302210535}

[[请在目标设备上查看结果]{style="font-family:宋体"}]{#struct_0_x1819_23372_937095357}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x429733738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cfd dm one-way history]{lang="EN-US"}**]{#struct_0_x1819_23372_x302144999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset cfd dm one-way history]{lang="EN-US"}**]{#struct_0_x1819_23372_x1782070460}

::: {#-1239899415 .myid}
[]{#_Toc404795549}[]{#struct_0_x1819_23372_1536200177}[]{#_Toc351105897}

**CFD \-- CFD配置命令 \-- cfd dm two-way**

------------------------------------------------------------------------

[**[cfd dm two-way]{lang="EN-US"}**]{#struct_0_x1819_23372_x1172368033}[命令用来开启双向时延测试功能，通过从源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送]{style="font-family:宋体"}[DMM]{lang="EN-US"}[报文到目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[，并检测回应的]{style="font-family:宋体"}[DMR]{lang="EN-US"}[报文来测试设备间的双向时延。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x302341607}

[**[cfd dm two-way service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } \[ **number** *number* \]]{lang="EN-US"}]{#struct_0_x1819_23372_1724933532}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1759285386}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x302276071}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_530504175}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1964345212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x301948391}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1705339224}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1162137730}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1204234735}[：表示源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1819_23372_x301882855}[：表示目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mep]{lang="EN-US"}***[ target-mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1471875243}[：表示目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[target-mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x1819_23372_391352788}[：表示]{style="font-family:宋体"}[DMM]{lang="EN-US"}[报文的发送数量，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x991989349}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x302079463}[在服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内测试源]{style="font-family:宋体"}[MEP 1101]{lang="EN-US"}[到目标]{style="font-family:宋体"}[MEP 2001]{lang="EN-US"}[的双向时延。]{style="font-family:宋体"}

[[\<Sysname\> cfd dm two-way service-instance 1 mep 1101 target-mep 2001]{lang="PT-BR"}]{#struct_0_x1819_23372_1688275439}

[Frame delay:]{lang="PT-BR"}

[Reply from 0010-fc00-6512: 10ms]{lang="PT-BR"}

[Reply from 0010-fc00-6512: 9ms]{lang="PT-BR"}

[Reply from 0010-fc00-6512: 11ms]{lang="PT-BR"}

[Reply from 0010-fc00-6512: 5ms]{lang="PT-BR"}

[Reply from 0010-fc00-6512: 5ms]{lang="PT-BR"}

[Average: 8ms]{lang="PT-BR"}

[Sent DMMs: 5        Received: 5        Lost: 0]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Frame delay variation: 5ms 4ms 6ms 0ms 0ms]{lang="PT-BR"}

[Average: 3ms]{lang="PT-BR"}

[[表1-3 ]{lang="EN-US"}[cfd dm two-way]{lang="EN-US"}]{#struct_0_x1819_23372_x302013927}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1583337628}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_1738374117}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_1235239632}

[[Frame delay]{lang="EN-US"}]{#struct_0_x1819_23372_x301686247}

[[帧时延]{style="font-family:宋体"}]{#struct_0_x1819_23372_1414322910}

[[Reply from 0010-fc00-6512]{lang="EN-US"}]{#struct_0_x1819_23372_650779667}

[[从]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_x301620711}[地址为]{style="font-family:宋体"}[0010-FC00-6512]{lang="EN-US"}[的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[返回的]{style="font-family:宋体"}[DMR]{lang="EN-US"}[报文的时延]{style="font-family:宋体"}

[[Average]{lang="EN-US"}]{#struct_0_x1819_23372_1455747491}

[[帧时延或帧时延变化的平均值]{style="font-family:宋体"}]{#struct_0_x1819_23372_78902380}

[[Sent DMMs]{lang="EN-US"}]{#struct_0_x1819_23372_x302210534}

[[发送的]{style="font-family:宋体"}[DMM]{lang="EN-US"}]{#struct_0_x1819_23372_937160893}[报文总数]{style="font-family:宋体"}

[[Received]{lang="EN-US"}]{#struct_0_x1819_23372_x302144998}

[[收到的]{style="font-family:宋体"}[DMR]{lang="EN-US"}]{#struct_0_x1819_23372_x1782135996}[报文总数]{style="font-family:宋体"}

[[Lost]{lang="EN-US"}]{#struct_0_x1819_23372_x1537402838}

[[丢失的]{style="font-family:宋体"}[DMR]{lang="EN-US"}]{#struct_0_x1819_23372_x302341606}[报文总数]{style="font-family:宋体"}

[[Frame delay variation]{lang="EN-US"}]{#struct_0_x1819_23372_1724867996}

[[帧时延变化]{style="font-family:宋体"}]{#struct_0_x1819_23372_1425522245}

[ ]{lang="EN-US"}

::: {#1785984888 .myid}
[]{#_Toc404795550}[]{#struct_0_x1819_23372_492803123}[]{#_创建/删除维护集}[]{#_Toc286931127}[]{#_Toc286934513}[]{#_Toc286931128}[]{#_Toc286934514}[]{#_Toc286931129}[]{#_Toc286934515}[]{#_Toc286931130}[]{#_Toc286934516}[]{#_Toc286931131}[]{#_Toc286934517}[]{#_Toc286931132}[]{#_Toc286934518}[]{#_Toc286931133}[]{#_Toc286934519}[]{#_Toc286931134}[]{#_Toc286934520}[]{#_Toc286931135}[]{#_Toc286934521}[]{#_Toc286931136}[]{#_Toc286934522}[]{#_Toc286931137}[]{#_Toc286934523}[]{#_Toc286931138}[]{#_Toc286934524}[]{#_Toc286931139}[]{#_Toc286934525}[]{#_Toc286931140}[]{#_Toc286934526}[]{#_Toc286931141}[]{#_Toc286934527}[]{#_Toc286931142}[]{#_Toc286934528}[]{#_Toc286931143}[]{#_Toc286934529}[]{#_Toc286931144}[]{#_Toc286934530}[]{#_Toc286931145}[]{#_Toc286934531}[]{#_Toc286931146}[]{#_Toc286934532}[]{#_Toc286931147}[]{#_Toc286934533}[]{#_Toc286931148}[]{#_Toc286934534}[]{#_Toc286931149}[]{#_Toc286934535}[]{#_Toc286931150}[]{#_Toc286934536}[]{#_Toc286931152}[]{#_Toc286934538}[]{#_Toc286931154}[]{#_Toc286934540}[]{#_Toc286931155}[]{#_Toc286934541}[]{#_Toc286931165}[]{#_Toc286934551}[]{#_Toc286931167}[]{#_Toc286934553}[]{#_Toc286931168}[]{#_Toc286934554}[]{#_Toc286931169}[]{#_Toc286934555}[]{#_Toc286931170}[]{#_Toc286934556}[]{#_Toc286931171}[]{#_Toc286934557}[]{#_Toc286931172}[]{#_Toc286934558}[]{#_Toc286931173}[]{#_Toc286934559}[]{#_Toc286931174}[]{#_Toc286934560}[]{#_Toc286931175}[]{#_Toc286934561}[]{#_Toc286931176}[]{#_Toc286934562}[]{#_Toc286931177}[]{#_Toc286934563}[]{#_Toc286931178}[]{#_Toc286934564}[]{#_Toc286931179}[]{#_Toc286934565}[]{#_Toc286931180}[]{#_Toc286934566}[]{#_Toc286931181}[]{#_Toc286934567}[]{#_Toc286931182}[]{#_Toc286934568}[]{#_Toc286931183}[]{#_Toc286934569}[]{#_Toc286931184}[]{#_Toc286934570}[]{#_Toc286931185}[]{#_Toc286934571}[]{#_Toc286931186}[]{#_Toc286934572}[]{#_Toc286931187}[]{#_Toc286934573}[]{#_Toc286931188}[]{#_Toc286934574}[]{#_Toc286931189}[]{#_Toc286934575}[]{#_Toc286931197}[]{#_Toc286934583}[]{#_Toc286931200}[]{#_Toc286934586}[]{#_Toc286931225}[]{#_Toc286934611}

**CFD \-- CFD配置命令 \-- cfd enable**

------------------------------------------------------------------------

[**[cfd enable]{lang="EN-US"}**]{#struct_0_x1819_23372_x1083796617}[命令用来使能]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo cfd enable]{lang="EN-US"}**]{#struct_0_x1819_23372_233752004}[命令用来关闭]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1703545025}

[**[cfd enable]{lang="EN-US"}**]{#struct_0_x1819_23372_619539023}

[**[undo cfd enable]{lang="EN-US"}**]{#struct_0_x1819_23372_487275142}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1472834508}

[[CFD]{lang="EN-US"}]{#struct_0_x1819_23372_x829108721}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x511728213}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_1790343062}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1225458944}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1148971414}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_2034808651}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1750248559}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_1478019631}[]{#_Hlt18738541}[使能]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_x828649972}

[\[Sysname\] cfd enable]{lang="EN-US"}
:::

::::: {#1024858350 .myid}
[]{#_Toc404795551}[]{#struct_0_x1819_23372_x301882854}[]{#_Toc351105899}

**CFD \-- CFD配置命令 \-- cfd hardware-cc**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CFD命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_23372_546533706}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_23372_x1019550235}
:::

[ ]{lang="EN-US"}

[**[cfd hardware-cc]{lang="EN-US"}**]{#struct_0_x1819_23372_1471809707}[命令用来开启硬件检测功能。]{style="font-family:宋体"}

[**[undo cfd hardware-cc]{lang="EN-US"}**]{#struct_0_x1819_23372_x302079462}[用来关闭硬件检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1688340975}

[**[cfd hardware-cc service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*[ **remote-mep** *mep-list*]{lang="EN-US"}]{#struct_0_x1819_23372_x1731102827}

[**[undo]{lang="EN-US"}**[ **cfd hardware-cc service-instance** *instance-id* **remote-mep** *mep-list*]{lang="EN-US"}]{#struct_0_x1819_23372_x303407574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x302013926}

[[硬件检测功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1819_23372_1738439653}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2004305104}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1206428211}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1238517988}

[[network-admin]{lang="PT-BR"}]{#struct_0_x1819_23372_x301686246}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x1819_23372_1414257374}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1405188611}

[**[service-instance]{lang="PT-BR"}**]{#struct_0_x1819_23372_1968228516}*[ instance-id]{lang="PT-BR"}*[：]{style="font-family:宋体"}[表示服务实例的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[instance-id]{lang="PT-BR"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[32767]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[remote-mep ]{lang="PT-BR"}**]{#struct_0_x1819_23372_x301620710}*[mep]{lang="PT-BR"}[-list]{lang="PT-BR"}*[：]{style="font-family:宋体"}[表示远端]{style="font-family:宋体"}[MEP]{lang="PT-BR"}[的编号列表]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示多个远端]{style="font-family:宋体"}[MEP]{lang="PT-BR"}[。表示方式为]{style="font-family:宋体"}*[mep-list]{lang="PT-BR"}*[ = { *mep-id* \[ **to** *mep-id* \] }&\<1-10\>]{lang="PT-BR"}[。其中，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1455681955}

[[\# ]{lang="PT-BR"}]{#struct_0_x1819_23372_x1097879505}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上开启硬件检测功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[在服务实例]{style="font-family:宋体"}[1]{lang="PT-BR"}[内对远端]{style="font-family:宋体"}[MEP 5]{lang="PT-BR"}[进行硬件检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1819_23372_x302210537}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-GigabitEthernet1/0/1\] cfd hardware-cc service-instance 1 remote-mep 5]{lang="PT-BR"}
:::::

::: {#-730035159 .myid}
[]{#_Toc404795552}[]{#struct_0_x1819_23372_x574416114}[]{#_创建/删除服务实例}[]{#_cfd_linktrace}

**CFD \-- CFD配置命令 \-- cfd linktrace**

------------------------------------------------------------------------

[**[cfd linktrace]{lang="EN-US"}**]{#struct_0_x1819_23372_1477295649}[命令用来查找源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[到目标]{style="font-family:宋体"}[MP]{lang="EN-US"}[的路径，通过从源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文到目标]{style="font-family:宋体"}[MP]{lang="EN-US"}[，并检测回应的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文来确定设备间的路径。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x355626210}

[**[cfd linktrace service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **target-mac** *mac-address* \| **target-mep** *target-mep-id* } \[ **ttl** *ttl-value* \] \[ **hw-only** \]]{lang="EN-US"}]{#struct_0_x1819_23372_x1949485272}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2146499883}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_1015632196}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1429595212}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_2085465695}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x828584436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2003751220}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1689971931}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1401613030}[：表示源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1819_23372_1517137674}[：表示目标]{style="font-family:宋体"}[MP]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mep]{lang="EN-US"}***[ target-mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x864781915}[：表示目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[target-mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ttl ]{lang="EN-US"}***[ttl-value]{lang="EN-US"}*]{#struct_0_x1819_23372_x1100704253}[：表示生存时间值，]{style="font-family:宋体"}*[ttl-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hw-only]{lang="EN-US"}**]{#struct_0_x1819_23372_1790718385}[：表示所发送的]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文的]{style="font-family:宋体"}[HW-only]{lang="EN-US"}[位置位。当设置了此参数时，表示接收]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MIP]{lang="EN-US"}[在硬件转发表中找不到目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时，不对报文进行广播；否则，将对报文进行广播。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x26299525}

[]{#struct_0_x1819_23372_x828518900}[]{#_Toc138653851}[\# ]{lang="EN-US"}[在服务实例]{style="font-family:
宋体"}[1]{lang="EN-US"}[内查找源]{style="font-family:宋体"}[MEP 1101]{lang="EN-US"}[到目标]{style="font-family:宋体"}[MEP 2001]{lang="EN-US"}[的路径。]{style="font-family:宋体"}

[[\<Sysname\> cfd linktrace service-instance 1 mep 1101 target-mep 2001]{lang="EN-US"}]{#struct_0_x1819_23372_1004709393}

[Linktrace to MEP 2001 with the sequence number 1101-43361:]{lang="EN-US"}

[MAC address               TTL     Last MAC         Relay action]{lang="EN-US"}

[0010-fc00-6512            63      0010-fc00-6500   Hit]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[cfd linktrace]{lang="EN-US"}]{#struct_0_x1819_23372_736378101}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_218551479}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_2015276573}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_1651827091}

[[Linktrace to MEP 2001 with the sequence number 1101-43361]{lang="EN-US"}]{#struct_0_x1819_23372_x1368394796}

[[以序列号]{style="font-family:宋体"}[1101-43361]{lang="EN-US"}]{#struct_0_x1819_23372_1534636511}[发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文到目标]{style="font-family:宋体"}[MEP 2001]{lang="EN-US"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1819_23372_x828453364}

[[LTR]{lang="EN-US"}]{#struct_0_x1819_23372_x1674879185}[报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_x1819_23372_89876573}

[[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_77907533}[报文经过此设备时的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Last MAC]{lang="EN-US"}]{#struct_0_x1819_23372_955247188}

[[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_10800529}[报文所经过上一跳设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Relay action]{lang="EN-US"}]{#struct_0_x1819_23372_x828387828}

[[表示转发设备在]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_x113669026}[地址表中是否找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hit]{lang="EN-US"}]{#struct_0_x1819_23372_x776076518}[：表示本设备就是目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FDB]{lang="EN-US"}]{#struct_0_x1819_23372_x1939096259}[：表示在转发表中找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MPDB]{lang="EN-US"}]{#struct_0_x1819_23372_x1505433629}[：表示没有找到目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，或者在]{style="font-family:宋体"}[MEP]{lang="EN-US"}[或]{style="font-family:宋体"}[MIP]{lang="EN-US"}[数据库中找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x727710839}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd linktrace auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_1645019511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cfd linktrace-reply]{lang="EN-US"}**]{#struct_0_x1819_23372_x828322292}

::: {#-2071654467 .myid}
[]{#_Toc404795553}[]{#struct_0_x1819_23372_1845357110}[]{#_创建/删除维护端点}[]{#_cfd_linktrace_auto-detection}

**CFD \-- CFD配置命令 \-- cfd linktrace auto-detection**

------------------------------------------------------------------------

[**[cfd linktrace auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_1899429107}[命令用来开启自动发送]{style="font-family:
宋体"}[LTM]{lang="EN-US"}[报文功能。]{style="font-family:宋体"}

[**[undo cfd linktrace auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_565853878}[命令用来关闭自动发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1576683199}

[**[cfd linktrace auto-detection]{lang="EN-US"}**[ \[ **size** *size-value* \]]{lang="EN-US"}]{#struct_0_x1819_23372_x1307024469}

[**[undo cfd linktrace auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_1599313340}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x851444990}

[[自动发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_x431874012}[报文功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x828256756}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_1096030075}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x184919886}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1123085030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x780802395}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2130879424}

[**[size]{lang="EN-US"}***[ size-value]{lang="EN-US"}*]{#struct_0_x1819_23372_1687290517}[：表示缓冲区只记录最近]{style="font-family:宋体"}*[size-value]{lang="EN-US"}*[次自动检测的结果，]{style="font-family:宋体"}*[size-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，以发送的次数为单位，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[次，即缓冲区只记录最近]{style="font-family:宋体"}*[5]{lang="EN-US"}*[次自动检测的结果。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_47019956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启本功能后，当源]{style="font-family:宋体"}]{#struct_0_x1819_23372_194402952}[MEP]{lang="EN-US"}[在]{style="font-family:宋体"}[3.5]{lang="EN-US"}[个]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文发送周期内未收到目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发来的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文，从而判定与目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的连接出错时，将发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文（该]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文的目地为目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[，]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文中]{style="font-family:宋体"}[TTL]{lang="EN-US"}[字段为最大值]{style="font-family:宋体"}[255]{lang="EN-US"}[），通过检测回应的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文来定位故障。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭自动发送]{style="font-family:宋体"}]{#struct_0_x1819_23372_1612078411}[LTM]{lang="EN-US"}[报文的功能后，缓冲区中的内容将被删除，记录被清空。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[支持硬件检测功能的单板上所配置的外向]{style="font-family:宋体"}]{#struct_0_x1819_23372_x302210536}[MEP]{lang="EN-US"}[，不会自动发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x828191220}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x855673490}[开启自动发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文功能，且缓冲区只记录最近]{style="font-family:宋体"}[100]{lang="EN-US"}[次自动检测的结果。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_x1122659071}

[\[Sysname\] cfd linktrace auto-detection size 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_577728674}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd linktrace]{lang="EN-US"}**]{#struct_0_x1819_23372_877780962}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cfd linktrace-reply auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_920598054}
:::

::: {#1253589574 .myid}
[]{#_Toc404795554}[]{#struct_0_x1819_23372_x963034401}

**CFD \-- CFD配置命令 \-- cfd loopback**

------------------------------------------------------------------------

[**[cfd loopback]{lang="EN-US"}**]{#struct_0_x1819_23372_x1253379380}[命令用来开启环回功能，从源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[向目标]{style="font-family:宋体"}[MP]{lang="EN-US"}[发送]{style="font-family:宋体"}[LBM]{lang="EN-US"}[报文并接收]{style="font-family:宋体"}[LBR]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x829174260}

[**[cfd loopback service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **target-mac** *mac-address* \| **target-mep** *target-mep-id* } \[ **number** *number* \]]{lang="EN-US"}]{#struct_0_x1819_23372_x94687645}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_273435017}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1596520459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x9141075}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1857263496}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1330132435}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x829108724}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x511400533}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x2056138081}[：表示源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1819_23372_46710170}[：表示目标]{style="font-family:宋体"}[MP]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mep]{lang="EN-US"}***[ target-mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1039690670}[：表示目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[target-mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x1819_23372_x2035018542}[：表示发送]{style="font-family:宋体"}[LBM]{lang="EN-US"}[报文数量，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1642404866}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1449544895}[开启环回功能，检查服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内]{style="font-family:宋体"}[MEP 1101]{lang="EN-US"}[到]{style="font-family:宋体"}[2001]{lang="EN-US"}[的链路状况（假设链路状态正常）。]{style="font-family:宋体"}

[[\<Sysname\> cfd loopback service-instance 1 mep 1101 target-mep 2001]{lang="EN-US"}]{#struct_0_x1819_23372_x828649971}

[Loopback to 0010-fc00-6512 with the sequence number start from 1101-43404:]{lang="EN-US"}

[Reply from 0010-fc00-6512: sequence number=1101-43404 Time=5ms]{lang="EN-US"}

[Reply from 0010-fc00-6512: sequence number=1101-43405 Time=5ms]{lang="EN-US"}

[Reply from 0010-fc00-6512: sequence number=1101-43406 Time=5ms]{lang="EN-US"}

[Reply from 0010-fc00-6512: sequence number=1101-43407 Time=5ms]{lang="EN-US"}

[Reply from 0010-fc00-6512: sequence number=1101-43408 Time=5ms]{lang="EN-US"}

[Sent: 5        Received: 5        Lost: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x574350578}[开启环回功能，检查服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内]{style="font-family:宋体"}[MEP 1101]{lang="EN-US"}[到]{style="font-family:宋体"}[2001]{lang="EN-US"}[的链路状况（假设链路状态不正常）。]{style="font-family:宋体"}

[[\<Sysname\> cfd loopback service-instance 1 mep 1101 target-mep 2001]{lang="EN-US"}]{#struct_0_x1819_23372_x1238040010}

[Loopback to 0010-fc00-6512 with the sequence number start from 1101-43404:]{lang="EN-US"}

[Sent: 5        Received: 0        Lost: 5]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[cfd loopback]{lang="EN-US"}]{#struct_0_x1819_23372_x193819167}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_220893841}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1275065036}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x72722899}

[[Loopback to 0010-fc00-6512 with the sequence number start from 1101-43404]{lang="EN-US"}]{#struct_0_x1819_23372_x338975354}

[[以]{style="font-family:宋体"}[1101-43404]{lang="EN-US"}]{#struct_0_x1819_23372_x828584435}[为起始序列号发送]{style="font-family:宋体"}[LBM]{lang="EN-US"}[报文到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0010-FC00-6512]{lang="EN-US"}[的]{style="font-family:宋体"}[MEP]{lang="EN-US"}

[[Reply from 0010-fc00-6512]{lang="EN-US"}]{#struct_0_x1819_23372_x2003685684}

[[表示从]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_923995044}[地址为]{style="font-family:宋体"}[0010-FC00-6512]{lang="EN-US"}[的目标]{style="font-family:宋体"}[MP]{lang="EN-US"}[返回]{style="font-family:宋体"}

[[sequence number]{lang="EN-US"}]{#struct_0_x1819_23372_1744581648}

[[LBR]{lang="EN-US"}]{#struct_0_x1819_23372_1915467721}[报文中的序列号]{style="font-family:宋体"}

[[Time=5ms]{lang="EN-US"}]{#struct_0_x1819_23372_x398231234}

[[表示从发出]{style="font-family:宋体"}[LBM]{lang="EN-US"}]{#struct_0_x1819_23372_1239462117}[报文到收到]{style="font-family:宋体"}[LBR]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[毫秒]{style="font-family:宋体"}

[[Sent]{lang="EN-US"}]{#struct_0_x1819_23372_x828518899}

[[发送]{style="font-family:宋体"}[LBM]{lang="EN-US"}]{#struct_0_x1819_23372_x1333352934}[报文的数量]{style="font-family:宋体"}

[[Received]{lang="EN-US"}]{#struct_0_x1819_23372_1174374097}

[[收到]{style="font-family:宋体"}[LBR]{lang="EN-US"}]{#struct_0_x1819_23372_x1743190129}[报文的数量]{style="font-family:宋体"}

[[Lost]{lang="EN-US"}]{#struct_0_x1819_23372_x245243366}

[[丢失]{style="font-family:宋体"}[LBR]{lang="EN-US"}]{#struct_0_x1819_23372_x332293109}[报文的数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#232785222 .myid}
[]{#_Toc404795555}[]{#struct_0_x1819_23372_x828453363}[]{#_cfd_ma}[]{#_Toc286931231}[]{#_Toc286934617}[]{#_Toc286931232}[]{#_Toc286934618}[]{#_Toc286931233}[]{#_Toc286934619}[]{#_Toc286931234}[]{#_Toc286934620}[]{#_Toc286931235}[]{#_Toc286934621}[]{#_Toc286931236}[]{#_Toc286934622}[]{#_Toc286931237}[]{#_Toc286934623}[]{#_Toc286931238}[]{#_Toc286934624}[]{#_Toc286931239}[]{#_Toc286934625}[]{#_Toc286931240}[]{#_Toc286934626}[]{#_Toc286931241}[]{#_Toc286934627}[]{#_Toc286931242}[]{#_Toc286934628}[]{#_Toc286931243}[]{#_Toc286934629}[]{#_Toc286931244}[]{#_Toc286934630}[]{#_Toc286931245}[]{#_Toc286934631}[]{#_Toc286931246}[]{#_Toc286934632}[]{#_Toc286931247}[]{#_Toc286934633}[]{#_Toc286931248}[]{#_Toc286934634}[]{#_Toc286931249}[]{#_Toc286934635}[]{#_Toc286931250}[]{#_Toc286934636}[]{#_Toc286931251}[]{#_Toc286934637}[]{#_Toc286931253}[]{#_Toc286934639}[]{#_Toc286931254}[]{#_Toc286934640}[]{#_cfd_md}

**CFD \-- CFD配置命令 \-- cfd md**

------------------------------------------------------------------------

[**[cfd md]{lang="EN-US"}**]{#struct_0_x1819_23372_x1674944721}[命令用来创建]{style="font-family:宋体"}[MD]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cfd md]{lang="EN-US"}**]{#struct_0_x1819_23372_x628519428}[命令用来删除]{style="font-family:宋体"}[MD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1830610259}

[**[cfd md ]{lang="EN-US"}***[md-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **index** *index-value* \] **level** *level-value* \[ **md-id** { **dns** *dns-name* \| **mac** *mac-address* *subnumber* \| **none** } \]]{lang="EN-US"}]{#struct_0_x1819_23372_2010631511}

[**[undo cfd md ]{lang="EN-US"}***[md-name]{lang="EN-US"}*]{#struct_0_x1819_23372_x402684852}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_209372179}

[[没有创建]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x328149143}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1358764612}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x828387827}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x113079202}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1165295114}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_2040440796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_72497106}

[**[md ]{lang="EN-US"}***[md-name]{lang="EN-US"}*]{#struct_0_x1819_23372_286274382}[：表示字符串格式的]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称，]{style="font-family:宋体"}*[md-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[43]{lang="EN-US"}[个字符的字符串，可以由字母、数字和特殊字符（包括]{style="font-family:宋体"}[\` \~ ! @ \# \$ % \^ & \* ( ) - \_ + = { } \[ \] \| : ; \' \< \> , . /]{lang="EN-US"}[）组成。]{style="font-family:宋体"}

[**[index]{lang="EN-US"}**[ *index-value*]{lang="EN-US"}]{#struct_0_x1819_23372_1727636735}[：表示]{style="font-family:宋体"}[MD]{lang="EN-US"}[的索引号，]{style="font-family:宋体"}*[index-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，系统将自动分配尚未使用的最小索引号。不建议用户手工指定]{style="font-family:宋体"}[MD]{lang="EN-US"}[的索引号，最好由系统来自动分配。]{style="font-family:宋体"}

[**[level]{lang="EN-US"}***[ level-value]{lang="EN-US"}*]{#struct_0_x1819_23372_x242398618}[：表示]{style="font-family:宋体"}[MD]{lang="EN-US"}[的级别，]{style="font-family:宋体"}*[level-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[md-id]{lang="EN-US"}**]{#struct_0_x1819_23372_x1029982778}[：表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[所发送的报文携带的]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称。如果未指定本参数，该名称就是]{style="font-family:宋体"}*[md-name]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[dns]{lang="EN-US"}**[ *dns-name*]{lang="EN-US"}]{#struct_0_x1819_23372_x828322291}[：表示采用]{style="font-family:宋体"}[DNS]{lang="EN-US"}[名称的]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称，]{style="font-family:宋体"}*[dns-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[的名称。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**[ *mac-address* *subnumber*]{lang="EN-US"}]{#struct_0_x1819_23372_1845160502}[：表示由]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和一个整数构成的]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x1819_23372_x879803465}[：表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[所发送的报文不携带]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_261846940}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x1395775132}[的名称应符合]{style="font-family:宋体"}[IEEE802.1ag-2007]{lang="EN-US"}[中表]{style="font-family:宋体"}[21-19]{lang="EN-US"}[的规定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当输入的]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1122259509}[MD]{lang="EN-US"}[名称错误或已存在，或者指定的索引号已被使用时，将不能创建]{style="font-family:宋体"}[MD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_x1819_23372_229690309}[MD]{lang="EN-US"}[时，基于该]{style="font-family:宋体"}[MD]{lang="EN-US"}[的配置均被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_78507273}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x159521716}[创建级别为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[MD test_md1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_x828256755}

[\[Sysname\] cfd md test_md1 level 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_1095964539}[创建级别为]{style="font-family:宋体"}[5]{lang="EN-US"}[的]{style="font-family:宋体"}[MD test_md2]{lang="EN-US"}[，且]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送的报文携带的]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称由]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[1-1-1]{lang="EN-US"}[和整数]{style="font-family:宋体"}[1]{lang="EN-US"}[构成。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_1076439537}

[\[Sysname\] cfd md test_md2 level 5 md-id mac 1-1-1 1]{lang="EN-US"}
:::

::: {#-1668677436 .myid}
[]{#_Toc404795556}[]{#struct_0_x1819_23372_726932241}[]{#_接口启动/停止CCM发送}[]{#_cfd_mep}

**CFD \-- CFD配置命令 \-- cfd mep**

------------------------------------------------------------------------

[**[cfd mep]{lang="EN-US"}**]{#struct_0_x1819_23372_1049568028}[命令用来创建]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cfd mep]{lang="EN-US"}**]{#struct_0_x1819_23372_1419110409}[命令用来删除]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1891304710}

[[在二层以太网接口视图或二层聚合接口视图下：]{style="font-family:宋体"}]{#struct_0_x1819_23372_x98161859}

[**[cfd mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*[ { **inbound \| outbound** }]{lang="EN-US"}]{#struct_0_x1819_23372_x380133285}

[**[undo cfd mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x828191219}

[[在三层以太网接口视图下：]{style="font-family:宋体"}]{#struct_0_x1819_23372_x856132239}

[**[cfd mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*[ **outbound**]{lang="EN-US"}]{#struct_0_x1819_23372_714803407}

[**[undo cfd mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_2049923045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1657683603}

[[接口上不存在]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1351376234}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1812490645}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1819_23372_1162871965}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x829174259}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x95146394}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_2092602556}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x303144131}

[**[mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_149472074}[：表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1981372496}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x1819_23372_1150389848}[：表示建立的是内向]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x1819_23372_360273261}[：表示建立的是外向]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2047291987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在创建]{style="font-family:宋体"}]{#struct_0_x1819_23372_x829108723}[MEP]{lang="EN-US"}[时，通过指定的服务实例确定该]{style="font-family:宋体"}[MEP]{lang="EN-US"}[所在的]{style="font-family:宋体"}[MA]{lang="EN-US"}[和]{style="font-family:宋体"}[MD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建的]{style="font-family:宋体"}]{#struct_0_x1819_23372_x511859285}[MEP]{lang="EN-US"}[必须已包含在对应服务实例的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表中，否则不能创建成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1819_23372_x940571803}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_374703562}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x914104960}[在服务实例]{style="font-family:宋体"}[5]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表，在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上创建服务实例]{style="font-family:宋体"}[5]{lang="EN-US"}[内的外向]{style="font-family:宋体"}[MEP 3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_419669120}

[\[Sysname\] cfd md test_md level 3]{lang="EN-US"}

[\[Sysname\] cfd service-instance 5 ma-id vlan-based md test_md vlan 100]{lang="EN-US"}

[\[Sysname\] cfd meplist 3 service-instance 5]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] cfd mep 3 service-instance 5 outbound]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1537134549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd meplist]{lang="EN-US"}**]{#struct_0_x1819_23372_432751251}
:::

::: {#-1576336398 .myid}
[]{#_Toc404795557}[]{#struct_0_x1819_23372_737433973}[]{#_Toc219716690}[]{#_配置CCM发送间隔}[]{#_Toc286931258}[]{#_Toc286934644}[]{#_Toc286931259}[]{#_Toc286934645}[]{#_Toc286931260}[]{#_Toc286934646}[]{#_Toc286931261}[]{#_Toc286934647}[]{#_Toc286931262}[]{#_Toc286934648}[]{#_Toc286931263}[]{#_Toc286934649}[]{#_Toc286931264}[]{#_Toc286934650}[]{#_Toc286931265}[]{#_Toc286934651}[]{#_Toc286931266}[]{#_Toc286934652}[]{#_Toc286931267}[]{#_Toc286934653}[]{#_Toc286931268}[]{#_Toc286934654}[]{#_Toc286931269}[]{#_Toc286934655}[]{#_Toc286931270}[]{#_Toc286934656}[]{#_Toc286931271}[]{#_Toc286934657}[]{#_Toc286931272}[]{#_Toc286934658}[]{#_Toc286931273}[]{#_Toc286934659}[]{#_Toc286931274}[]{#_Toc286934660}[]{#_Toc286931276}[]{#_Toc286934662}[]{#_Toc286931277}[]{#_Toc286934663}[]{#_发送链路跟踪报文}

**CFD \-- CFD配置命令 \-- cfd meplist**

------------------------------------------------------------------------

[**[cfd meplist]{lang="EN-US"}**]{#struct_0_x1819_23372_x279182932}[命令用来配置]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表，包括允许配置的本地]{style="font-family:宋体"}[MEP]{lang="EN-US"}[和需要监控的远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cfd meplist]{lang="EN-US"}**]{#struct_0_x1819_23372_x2004423887}[命令用来删除已配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1471937728}

[**[cfd meplist ]{lang="EN-US"}***[mep-list]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_x1819_23372_990685695}

[**[undo cfd meplist ]{lang="EN-US"}***[mep-list]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_x1819_23372_x1786958925}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1389153091}

[[不存在]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1115030193}[列表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x472578788}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_737499509}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x331318732}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1463580915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1229680961}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_388248472}

[**[meplist ]{lang="EN-US"}***[mep]{lang="EN-US"}[-list]{lang="EN-US"}*]{#struct_0_x1819_23372_x1515568674}[：表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号列表，表示多个]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[mep-list]{lang="EN-US"}*[ = { *mep-id* \[ **to** *mep-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x2073771473}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x48904675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1938936521}[MEP]{lang="EN-US"}[列表之前必须先创建]{style="font-family:宋体"}[MD]{lang="EN-US"}[和服务实例。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_x1819_23372_737565045}[MEP]{lang="EN-US"}[列表时，基于该列表的本地]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的配置均被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1646598742}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1205409786}[在服务实例]{style="font-family:宋体"}[5]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MEP]{lang="EN-US"}[为]{style="font-family:宋体"}[9]{lang="EN-US"}[到]{style="font-family:
宋体"}[15]{lang="EN-US"}[的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_627896715}

[\[Sysname\] cfd md test_md level 3]{lang="EN-US"}

[\[Sysname\] cfd service-instance 5 ma-id vlan-based md test_md vlan 100]{lang="EN-US"}

[\[Sysname\] cfd meplist 9 to 15 service-instance 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x34054349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd md]{lang="EN-US"}**]{#struct_0_x1819_23372_x655713123}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd service-instance]{lang="EN-US"}**]{#struct_0_x1819_23372_x852257576}
:::

::: {#-1883368077 .myid}
[]{#_Toc404795558}[]{#struct_0_x1819_23372_737630581}

**CFD \-- CFD配置命令 \-- cfd mip-rule**

------------------------------------------------------------------------

[**[cfd mip-rule]{lang="EN-US"}**]{#struct_0_x1819_23372_x1573422862}[命令用来配置]{style="font-family:宋体"}[MIP]{lang="EN-US"}[的创建规则，系统将按照此规则在接口上自动创建]{style="font-family:宋体"}[MIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cfd mip-rule]{lang="EN-US"}**]{#struct_0_x1819_23372_x772861412}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_323325544}

[**[cfd mip-rule ]{lang="EN-US"}**[{ **default** \| **explicit** } **service-instance** *instance-id*]{lang="EN-US"}]{#struct_0_x1819_23372_1380762956}

[**[undo cfd mip-rule]{lang="EN-US"}**[ \[ **default** \| **explicit** \] **service-instance** *instance-id*]{lang="EN-US"}]{#struct_0_x1819_23372_1307217376}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1853325822}

[[没有配置]{style="font-family:宋体"}[MIP]{lang="EN-US"}]{#struct_0_x1819_23372_x551952849}[的创建规则，系统不自动创建]{style="font-family:宋体"}[MIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2087127475}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_737696117}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x26695730}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x393129498}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1687751720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1877218391}

[**[default]{lang="EN-US"}**]{#struct_0_x1819_23372_x931660132}[：表示]{style="font-family:宋体"}[Default]{lang="EN-US"}[规则，即：当接口上没有更低级别的]{style="font-family:宋体"}[MIP]{lang="EN-US"}[时，在本级别创建]{style="font-family:宋体"}[MIP]{lang="EN-US"}[。在此规则下，接口上即使没有配置]{style="font-family:宋体"}[MEP]{lang="EN-US"}[也可创建]{style="font-family:宋体"}[MIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[explicit]{lang="EN-US"}**]{#struct_0_x1819_23372_x796990766}[：表示]{style="font-family:宋体"}[Explicit]{lang="EN-US"}[规则，即：当接口上没有更低级别的]{style="font-family:宋体"}[MIP]{lang="EN-US"}[且有更低级别的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[时，在本级别创建]{style="font-family:宋体"}[MIP]{lang="EN-US"}[。在此规则下，接口上只有配置了更低级别的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[时才可创建]{style="font-family:宋体"}[MIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1615124857}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1808565053}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_737761653}[在服务实例]{style="font-family:宋体"}[5]{lang="EN-US"}[内配置]{style="font-family:宋体"}[MIP]{lang="EN-US"}[的创建规则为]{style="font-family:宋体"}[Default]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_1526126078}

[\[Sysname\] cfd mip-rule default service-instance 5]{lang="EN-US"}
:::

::: {#-1052490484 .myid}
[]{#_Toc404795559}[]{#struct_0_x1819_23372_x1678685553}[]{#_Toc219718040}[]{#_Toc219718375}[]{#_Toc219718041}[]{#_Toc219718376}[]{#_Toc219718042}[]{#_Toc219718377}[]{#_Toc219718043}[]{#_Toc219718378}[]{#_Toc219718044}[]{#_Toc219718379}[]{#_Toc219718045}[]{#_Toc219718380}[]{#_Toc219718046}[]{#_Toc219718381}[]{#_Toc219718047}[]{#_Toc219718382}[]{#_Toc219718048}[]{#_Toc219718383}[]{#_Toc219718049}[]{#_Toc219718384}[]{#_Toc219718050}[]{#_Toc219718385}[]{#_Toc219718051}[]{#_Toc219718386}[]{#_Toc219718052}[]{#_Toc219718387}[]{#_Toc219718053}[]{#_Toc219718388}[]{#_Toc219718054}[]{#_Toc219718389}[]{#_Toc219718055}[]{#_Toc219718390}[]{#_Toc219718057}[]{#_Toc219718392}[]{#_Toc219718058}[]{#_Toc219718393}[]{#_自动发送链路跟踪报文}

**CFD \-- CFD配置命令 \-- cfd service-instance**

------------------------------------------------------------------------

[**[cfd service-instance]{lang="EN-US"}**]{#struct_0_x1819_23372_x1893114424}[命令用来创建服务实例。]{style="font-family:宋体"}

[**[undo cfd service-instance]{lang="EN-US"}**]{#struct_0_x1819_23372_896150445}[命令用来删除服务实例。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1241333623}

[**[cfd service-instance]{lang="EN-US"}***[ instance-id ]{lang="EN-US"}***[ma-id]{lang="EN-US"}**[ { **icc-based** *ma-name* \| **integer** *ma-num* \| **string** *ma-name* \| **vlan-based** \[ *vlan-id* \] } \[ **ma-index** *index-value* \] **md** *md-name* \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1819_23372_717410144}

[**[undo cfd service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1730042173}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_23372_737827189}

[[不存在服务实例。]{style="font-family:宋体"}]{#struct_0_x1819_23372_x240081237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1076724998}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x450033909}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1115198420}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1329419812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1976953824}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2099664775}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1720293406}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ma-id]{lang="EN-US"}**]{#struct_0_x1819_23372_737892725}[：表示创建]{style="font-family:宋体"}[MA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[icc-based]{lang="EN-US"}**[ *ma-name*]{lang="EN-US"}]{#struct_0_x1819_23372_1330144110}[：表示以]{style="font-family:宋体"}[ICC]{lang="EN-US"}[（]{style="font-family:宋体"}[ITU Carrier Codes]{lang="EN-US"}[，国际电信联盟运营商代码）格式的字符串为名称的]{style="font-family:宋体"}[MA]{lang="EN-US"}[，]{style="font-family:宋体"}*[ma-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[13]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[integer]{lang="EN-US"}**[ *ma-num*]{lang="EN-US"}]{#struct_0_x1819_23372_145375889}[：表示以整数为名称的]{style="font-family:宋体"}[MA]{lang="EN-US"}[，]{style="font-family:宋体"}*[ma-num]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[string]{lang="EN-US"}**[ *ma-name*]{lang="EN-US"}]{#struct_0_x1819_23372_x205272703}[：表示以普通字符串为名称的]{style="font-family:宋体"}[MA]{lang="EN-US"}[，]{style="font-family:宋体"}*[ma-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[45]{lang="EN-US"}[个字符的字符串，可以由字母、数字和特殊字符（包括]{style="font-family:宋体"}[\` \~ ! @ \# \$ % \^ & \* ( ) \_ - + = { } \[ \] \| : ; \' \< \> , . /]{lang="EN-US"}[）组成。]{style="font-family:宋体"}

[**[vlan-based]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1819_23372_x1729230966}[：表示以]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号为名称的]{style="font-family:宋体"}[MA]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，则使用]{style="font-family:宋体"}**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}[参数所指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号作为]{style="font-family:宋体"}[MA]{lang="EN-US"}[的名称；而如果不指定]{style="font-family:宋体"}**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}[参数，则必须在本参数中指定]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[ma-index]{lang="EN-US"}**[ *index-value*]{lang="EN-US"}]{#struct_0_x1819_23372_x683402941}[：表示]{style="font-family:宋体"}[MA]{lang="EN-US"}[的索引号，]{style="font-family:宋体"}*[index-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，系统将自动分配尚未使用的最小索引号。不建议用户手工指定]{style="font-family:宋体"}[MA]{lang="EN-US"}[的索引号，最好由系统来自动分配。]{style="font-family:宋体"}

[**[md]{lang="EN-US"}***[ md-name]{lang="EN-US"}*]{#struct_0_x1819_23372_1896438711}[：表示]{style="font-family:宋体"}[MD]{lang="EN-US"}[的名称，]{style="font-family:宋体"}*[md-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[43]{lang="EN-US"}[个字符的字符串，可以由字母、数字和特殊字符（包括]{style="font-family:宋体"}[\` \~ ! @ \# \$ % \^ & \* ( ) - \_ + = { } \[ \] \| : ; \' \< \> , . /]{lang="EN-US"}[）组成。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1819_23372_x846875824}[：表示]{style="font-family:宋体"}[MA]{lang="EN-US"}[所服务的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x942164989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[服务实例根据]{style="font-family:宋体"}]{#struct_0_x1819_23372_736909685}[MD]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[划分，每个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[是一个]{style="font-family:宋体"}[MA]{lang="EN-US"}[，有一个]{style="font-family:宋体"}[MA]{lang="EN-US"}[名称，并指定一个服务实例编号。]{style="font-family:宋体"}[MA]{lang="EN-US"}[的索引号代表了一个]{style="font-family:宋体"}[MD]{lang="EN-US"}[中的特定]{style="font-family:宋体"}[MA]{lang="EN-US"}[，它只在特定]{style="font-family:宋体"}[MD]{lang="EN-US"}[中唯一，不同]{style="font-family:宋体"}[MD]{lang="EN-US"}[中可以使用相同的]{style="font-family:宋体"}[MA]{lang="EN-US"}[索引号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MA]{lang="EN-US"}]{#struct_0_x1819_23372_1140651499}[的名称应符合]{lang="EN-US" style="font-family:
宋体"}[IEEE802.1ag-2007]{lang="EN-US"}[中表]{lang="EN-US" style="font-family:宋体"}[21-20]{lang="EN-US"}[的规定。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{lang="EN-US" style="font-family:宋体"}[MA]{lang="EN-US"}]{#struct_0_x1819_23372_x1477372727}[时，]{lang="EN-US" style="font-family:宋体"}[如果]{style="font-family:宋体"}[指定了]{lang="EN-US" style="font-family:宋体"}**[vlan-based]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}[参数，该]{lang="EN-US" style="font-family:宋体"}[MA]{lang="EN-US"}[就称为带]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[属性的]{lang="EN-US" style="font-family:宋体"}[MA]{lang="EN-US"}[；否则称为不带]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[属性的]{lang="EN-US" style="font-family:宋体"}[MA]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在创建服务实例之前，必须先为该服务实例创建]{style="font-family:宋体"}]{#struct_0_x1819_23372_629782582}[MD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在删除服务实例时，基于该服务实例的配置均被删除。]{style="font-family:宋体"}]{#struct_0_x1819_23372_1589615107}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除服务实例将不仅解除该服务实例与]{style="font-family:宋体"}]{#struct_0_x1819_23372_2113257014}[MA]{lang="EN-US"}[之间的关联，]{style="font-family:宋体"}[MA]{lang="EN-US"}[本身也将被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_19164414}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x796229431}[创建级别为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[MD test_md]{lang="EN-US"}[，并创建服务实例]{style="font-family:宋体"}[5]{lang="EN-US"}[，该服务实例的]{style="font-family:宋体"}[MA]{lang="EN-US"}[以]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号为名称，且服务于]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_23372_1153371150}

[\[Sysname\] cfd md test_md level 3]{lang="EN-US"}

[\[Sysname\] cfd service-instance 5 ma-id vlan-based md test_md vlan 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_736975221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd md]{lang="EN-US"}**]{#struct_0_x1819_23372_1988960952}
:::

::: {#-1622213107 .myid}
[]{#_Toc404795560}[]{#struct_0_x1819_23372_1620234836}[]{#_Toc351105909}

**CFD \-- CFD配置命令 \-- cfd slm**

------------------------------------------------------------------------

[**[cfd slm]{lang="EN-US"}**]{#struct_0_x1819_23372_x813276748}[命令用来开启单向丢包测试功能，通过从源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送]{style="font-family:宋体"}[LMM]{lang="EN-US"}[报文到目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[，并检测回应的]{style="font-family:宋体"}[LMR]{lang="EN-US"}[报文来测试设备间的单向丢包情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1620300372}

[**[cfd slm service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } \[ **number** *number* \]]{lang="EN-US"}]{#struct_0_x1819_23372_700462083}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1620628052}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x895559566}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_466750613}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1620693588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1620103765}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x467955305}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x2045613904}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1620169301}[：表示源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1819_23372_x496612045}[：表示目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mep]{lang="EN-US"}***[ target-mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1619972693}[：表示目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[target-mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x1819_23372_981736142}[：表示]{style="font-family:宋体"}[LMM]{lang="EN-US"}[报文的发送数量，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1620038229}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1280255815}[在服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内测试源]{style="font-family:宋体"}[MEP 1101]{lang="EN-US"}[到目标]{style="font-family:宋体"}[MEP 2001]{lang="EN-US"}[的单向丢包情况。]{style="font-family:宋体"}

[[\<Sysname\> cfd slm service-instance 1 mep 1101 target-mep 2001]{lang="PT-BR"}]{#struct_0_x1819_23372_1620365909}

[Reply from 0010-fc00-6512]{lang="PT-BR"}

[Far-end frame loss: 10    Near-end frame loss: 20]{lang="PT-BR"}

[Reply from 0010-fc00-6512]{lang="PT-BR"}

[Far-end frame loss: 40    Near-end frame loss: 40]{lang="PT-BR"}

[Reply from 0010-fc00-6512]{lang="PT-BR"}

[Far-end frame loss: 0     Near-end frame loss: 10]{lang="PT-BR"}

[Reply from 0010-fc00-6512]{lang="PT-BR"}

[Far-end frame loss: 30    Near-end frame loss: 30]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Average]{lang="PT-BR"}

[Far-end frame loss: 20    Near-end frame loss: 25]{lang="PT-BR"}

[Far-end frame loss rate: 25.00%      Near-end frame loss rate: 32.00%]{lang="PT-BR"}

[Sent LMMs: 5    Received: 5    Lost: 0]{lang="PT-BR"}

[[表1-6 ]{lang="EN-US"}[cfd slm]{lang="EN-US"}]{#struct_0_x1819_23372_1620431445}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1548801637}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_710846450}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_1620234837}

[[Reply from 0010-fc00-6512]{lang="EN-US"}]{#struct_0_x1819_23372_1620300373}

[[从]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_700396547}[地址为]{style="font-family:宋体"}[0010-FC00-6512]{lang="EN-US"}[的目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[返回的]{style="font-family:宋体"}[LMR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Far-end frame loss]{lang="EN-US"}]{#struct_0_x1819_23372_1620628053}

[[目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1620693589}[的帧丢失数]{style="font-family:宋体"}

[[Near-end frame loss]{lang="EN-US"}]{#struct_0_x1819_23372_x102985354}

[[源]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1620103762}[的帧丢失数]{style="font-family:宋体"}

[[Far-end frame loss rate]{lang="EN-US"}]{#struct_0_x1819_23372_1620169298}

[[目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1459244330}[的帧丢失率]{style="font-family:宋体"}

[[Near-end frame loss rate]{lang="EN-US"}]{#struct_0_x1819_23372_1619972690}

[[源]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1620038226}[的帧丢失率]{style="font-family:宋体"}

[[Average]{lang="EN-US"}]{#struct_0_x1819_23372_x1279403847}

[[帧丢失数平均值]{style="font-family:宋体"}]{#struct_0_x1819_23372_1620365906}

[[Sent LMMs]{lang="EN-US"}]{#struct_0_x1819_23372_1620431442}

[[发送的]{style="font-family:宋体"}[LMM]{lang="EN-US"}]{#struct_0_x1819_23372_1620234834}[报文总数]{style="font-family:宋体"}

[[Received]{lang="EN-US"}]{#struct_0_x1819_23372_x813407820}

[[收到的]{style="font-family:宋体"}[LMR]{lang="EN-US"}]{#struct_0_x1819_23372_1620300370}[报文总数]{style="font-family:宋体"}

[[Lost]{lang="EN-US"}]{#struct_0_x1819_23372_1620628050}

[[丢失的]{style="font-family:宋体"}[LMR]{lang="EN-US"}]{#struct_0_x1819_23372_x895428494}[报文总数]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc351105910}

::: {#299511375 .myid}
[]{#_Toc404795561}[]{#struct_0_x1819_23372_1620693586}

**CFD \-- CFD配置命令 \-- cfd tst**

------------------------------------------------------------------------

[**[cfd tst]{lang="EN-US"}**]{#struct_0_x1819_23372_x102919818}[命令用来开启比特错误测试功能，通过从源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送]{style="font-family:宋体"}[TST]{lang="EN-US"}[报文到目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[来测试设备间的比特错误。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1620103763}

[**[cfd tst service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } \[ **number** *number* \] \[ **length-of-test** *length* \] \[ **pattern-of-test** { **all-zero** \| **prbs** } \[ **with-crc** \] \]]{lang="EN-US"}]{#struct_0_x1819_23372_x467562089}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1620169299}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_1459178794}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1619972691}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_981605070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1620038227}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1279338311}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1620365907}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x30353871}[：表示源]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x1819_23372_x1455909348}[：表示目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[target-mep]{lang="EN-US"}***[ target-mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1620431443}[：表示目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[target-mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_x1819_23372_710715378}[：表示]{style="font-family:宋体"}[TST]{lang="EN-US"}[报文的发送数量，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[length-of-test]{lang="EN-US"}***[ length]{lang="EN-US"}*]{#struct_0_x1819_23372_1620234835}[：表示]{style="font-family:宋体"}[TST]{lang="EN-US"}[报文中]{style="font-family:宋体"}[Test TLV]{lang="EN-US"}[（]{style="font-family:宋体"}[Type/Length/Value]{lang="EN-US"}[，类型]{style="font-family:宋体"}[/]{lang="EN-US"}[长度]{style="font-family:宋体"}[/]{lang="EN-US"}[值）中的长度值，]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[1400]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pattern-of-test ]{lang="EN-US"}**[{ **all-zero** \| **prbs** } \[ **with-crc** \]]{lang="EN-US"}]{#struct_0_x1819_23372_x813342284}[：表示]{style="font-family:宋体"}[TST]{lang="EN-US"}[报文中]{style="font-family:宋体"}[Test TLV]{lang="EN-US"}[的模式，一共有四种模式，分别是：]{style="font-family:宋体"}**[all-zero]{lang="EN-US"}**[（不带]{style="font-family:宋体"}[CRC-32]{lang="EN-US"}[校验码的全]{style="font-family:宋体"}[0]{lang="EN-US"}[值）、]{style="font-family:宋体"}**[prbs]{lang="EN-US"}**[（不带]{style="font-family:宋体"}[CRC-32]{lang="EN-US"}[校验码的伪随机序列）、]{style="font-family:宋体"}**[all-zero]{lang="EN-US"}***[ ]{lang="EN-US"}***[with-crc]{lang="EN-US"}**[（带]{style="font-family:宋体"}[CRC-32]{lang="EN-US"}[校验码的全]{style="font-family:宋体"}[0]{lang="EN-US"}[值）和]{style="font-family:宋体"}**[prbs]{lang="EN-US"}**[ **with-crc**]{lang="EN-US"}[（带]{style="font-family:宋体"}[CRC-32]{lang="EN-US"}[校验码的伪随机序列）。缺省模式为]{style="font-family:宋体"}**[all-zero]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_753789198}

[[比特错误的测试结果需在目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1620300371}[上通过]{style="font-family:宋体"}**[display cfd tst]{lang="EN-US"}**[命令来显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_700265475}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_1620628051}[在服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内测试源]{style="font-family:宋体"}[MEP 1101]{lang="EN-US"}[到目标]{style="font-family:宋体"}[MEP 1003]{lang="EN-US"}[的比特错误。]{style="font-family:宋体"}

[[\<Sysname\> cfd tst service-instance 1 mep 1101 target-mep 1003]{lang="PT-BR"}]{#struct_0_x1819_23372_x895494030}

[5 TSTs have been sent. Please check the result on the remote device.]{lang="PT-BR"}

[[表1-7 ]{lang="EN-US"}[cfd tst]{lang="EN-US"}]{#struct_0_x1819_23372_1620693587}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1526041486}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1108779589}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_963184293}

[[5 TSTs have been sent]{lang="EN-US"}]{#struct_0_x1819_23372_x1108714053}

[[已发送]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1819_23372_x1108910661}[个]{style="font-family:宋体"}[TST]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Please check the result on the remote device]{lang="EN-US"}]{#struct_0_x1819_23372_x1108845125}

[[请在目标设备上查看结果]{style="font-family:宋体"}]{#struct_0_x1819_23372_279187108}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1108517445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cfd tst]{lang="EN-US"}**]{#struct_0_x1819_23372_x1709211796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset cfd tst]{lang="EN-US"}**]{#struct_0_x1819_23372_x1108451909}

::: {#1402615208 .myid}
[]{#_Toc404795562}[]{#struct_0_x1819_23372_x1101214473}[]{#_Toc351105911}

**CFD \-- CFD配置命令 \-- display cfd ais**

------------------------------------------------------------------------

[**[display cfd ais]{lang="EN-US"}**]{#struct_0_x1819_23372_x1108648517}[命令用来显示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[上]{style="font-family:宋体"}[AIS]{lang="EN-US"}[的配置和动态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x200989334}

[**[display cfd ais]{lang="EN-US"}**[ \[ **service-instance** *instance-id* \[ **mep** *mep-id* \] \]]{lang="EN-US"}]{#struct_0_x1819_23372_x1108582981}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1552964652}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_1566527872}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1108255301}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x196447799}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x1108189765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x94664266}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x1108779588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x602899648}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1108714052}[：显示指定服务实例内的信息，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。如果未指定本参数，将显示所有服务实例内的信息。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_83472301}[：显示指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的信息，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1108910660}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1627142539}[显示所有服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[上]{style="font-family:宋体"}[AIS]{lang="EN-US"}[的配置和动态信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd ais]{lang="PT-BR"}]{#struct_0_x1819_23372_x1108517444}

[Service instance: 5]{lang="PT-BR"}

[AIS level: 4    AIS period: 1s]{lang="PT-BR"}

[MEP ID: 1]{lang="PT-BR"}

[AIS condition: yes   Time to enter the condition: 2013/01/22 10:43:57]{lang="PT-BR"}

[AIS state machine: Previous state: NO_RECEIVE]{lang="PT-BR"}

[                   Current state: RECEIVE]{lang="PT-BR"}

[MEP ID: 2]{lang="PT-BR"}

[AIS condition: yes   Time to enter the condition: 2013/01/22 10:43:57]{lang="PT-BR"}

[AIS state machine: Previous state: NO_RECEIVE]{lang="PT-BR"}

[                   Current state: RECEIVE]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Service instance: 20]{lang="PT-BR"}

[AIS level: 3    AIS period: 60s]{lang="PT-BR"}

[MEP ID: 10]{lang="PT-BR"}

[AIS condition: yes   Time to enter the condition: 2013/01/22 10:43:57]{lang="PT-BR"}

[AIS state machine: Previous state: NO_RECEIVE]{lang="PT-BR"}

[                   Current state: RECEIVE]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Service instance: 100]{lang="PT-BR"}

[AIS level: 6    AIS period: 1s]{lang="PT-BR"}

[MEP ID: 20]{lang="PT-BR"}

[AIS condition: no    Time to enter the condition: 2013/01/22 11:40:01]{lang="PT-BR"}

[AIS state machine: Previous state: IDLE]{lang="PT-BR"}

[                   Current state: NO_RECEIVE]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[MEP ID: 50]{lang="PT-BR"}

[AIS condition: no    Time to enter the condition: -]{lang="PT-BR"}

[AIS state machine: Previous state: IDLE]{lang="PT-BR"}

[                   Current state: NO_RECEIVE]{lang="PT-BR"}

[[表1-8 ]{lang="EN-US"}[display cfd ais]{lang="EN-US"}]{#struct_0_x1819_23372_1019671559}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1501383688}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1108451908}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1108648516}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_1365094607}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1108582980}[所在的服务实例]{style="font-family:宋体"}

[[AIS level]{lang="EN-US"}]{#struct_0_x1819_23372_x1108255300}

[[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_x1762531740}[报文的发送级别]{style="font-family:宋体"}

[[AIS period]{lang="EN-US"}]{#struct_0_x1819_23372_x1108189764}

[[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_x1108714057}[报文的发送周期]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_x1108910665}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1108845129}[的编号]{style="font-family:宋体"}

[[AIS condition]{lang="EN-US"}]{#struct_0_x1819_23372_x1108517449}

[[抑制告警的状态：]{style="font-family:宋体"}]{#struct_0_x1819_23372_972617392}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[yes]{lang="EN-US"}]{#struct_0_x1819_23372_x1108451913}[：表示正在抑制告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no]{lang="EN-US"}]{#struct_0_x1819_23372_x1108648521}[：表示没有抑制告警]{style="font-family:宋体"}

[[Time to enter the condition]{lang="EN-US"}]{#struct_0_x1819_23372_x1108582985}

[[上次进入抑制告警状态的时间（"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x1819_23372_x772634176}["表示开启了告警抑制功能，但]{style="font-family:宋体"}[MEP]{lang="EN-US"}[从未收到过]{style="font-family:宋体"}[AIS]{lang="EN-US"}[报文）]{style="font-family:宋体"}

[[AIS state machine]{lang="EN-US"}]{#struct_0_x1819_23372_x1108255305}

[[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_x1108189769}[报文接收状态机]{style="font-family:宋体"}

[[Previous state]{lang="EN-US"}]{#struct_0_x1819_23372_1874704202}

[[上一个状态：]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1108779592}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_x1819_23372_x1108714056}[：表示未激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO_RECEIVE]{lang="EN-US"}]{#struct_0_x1819_23372_x1108910664}[：表示激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECEIVE]{lang="EN-US"}]{#struct_0_x1819_23372_x1108845128}[：表示收到]{lang="EN-US" style="font-family:宋体"}[AIS]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_x1819_23372_x836558139}

[[当前状态：]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1108517448}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_x1819_23372_x1108451912}[：表示未激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO_RECEIVE]{lang="EN-US"}]{#struct_0_x1819_23372_x1148203104}[：表示激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECEIVE]{lang="EN-US"}]{#struct_0_x1819_23372_x1108648520}[：表示收到]{lang="EN-US" style="font-family:宋体"}[AIS]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1505489083 .myid}
[]{#_Toc404795563}[]{#struct_0_x1819_23372_202360729}[]{#_Toc351105912}

**CFD \-- CFD配置命令 \-- display cfd ais-track link-status**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CFD命令.files/image001.png){#图片 6 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_23372_x1108582984}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_23372_793449765}
:::

[ ]{lang="EN-US"}

[**[display cfd ais-track link-status]{lang="EN-US"}**]{#struct_0_x1819_23372_x1108255304}[命令用来显示与端口状态相关联的]{style="font-family:宋体"}[AIS]{lang="EN-US"}[的配置和动态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_563067088}

[**[display cfd ais-track link-status]{lang="EN-US"}**[ \[ **interface** ]{lang="EN-US"}*[interface-type interface-number ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_x1819_23372_x1469381420}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1108189768}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x854179153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_457304352}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1628476576}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_567429668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_457369888}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x1440121879}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_457173280}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1819_23372_x167245410}[：显示指定端口的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号。如果未指定本参数，将显示所有端口的信息。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_457632033}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_457435425}[显示与所有端口的端口状态相关联的]{style="font-family:宋体"}[AIS]{lang="EN-US"}[的配置和动态信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd ais-track link-status]{lang="PT-BR"}]{#struct_0_x1819_23372_457500961}

[AIS tracking link-status is enabled.]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Interface GigabitEthernet1/0/1:]{lang="PT-BR"}

[AIS level: 5          AIS period: 1s]{lang="PT-BR"}

[Configured VLANs: 1, 10-100, 103]{lang="PT-BR"}

[Send VLANs: 1, 10-100, 103]{lang="PT-BR"}

[AIS condition: yes     Time to enter the condition: 2013/02/26 10:43:57]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Interface GigabitEthernet1/0/2:]{lang="PT-BR"}

[AIS level: 5          AIS period: 1s]{lang="PT-BR"}

[Configured VLANs: 1-4094]{lang="PT-BR"}

[Send VLANs: 1-2000]{lang="PT-BR"}

[AIS condition: yes     Time to enter the condition: 2013/02/26 10:44:57]{lang="PT-BR"}

[[表1-9 ]{lang="EN-US"}[display cfd ais-track link-status]{lang="EN-US"}]{#struct_0_x1819_23372_457828641}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1484571780}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x773989402}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_457894177}

[[AIS tracking link-status is enabled]{lang="EN-US"}]{#struct_0_x1819_23372_457304350}

[[端口状态与]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_1628476574}[联动功能处于开启状态]{style="font-family:宋体"}

[[AIS tracking link-status is disabled]{lang="EN-US"}]{#struct_0_x1819_23372_457369886}

[[端口状态与]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_457173278}[联动功能处于关闭状态]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1819_23372_457238814}

[[与]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_1646033672}[联动的端口]{style="font-family:宋体"}

[[AIS level]{lang="EN-US"}]{#struct_0_x1819_23372_457566494}

[[端口上]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_457632030}[报文的发送级别]{style="font-family:宋体"}

[[AIS period]{lang="EN-US"}]{#struct_0_x1819_23372_457435422}

[[端口上]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_1898443342}[报文的发送周期]{style="font-family:宋体"}

[[Configured VLANs]{lang="EN-US"}]{#struct_0_x1819_23372_457828638}

[[端口上配置的]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_457894174}[报文发送的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围]{style="font-family:宋体"}

[[Send VLANs]{lang="EN-US"}]{#struct_0_x1819_23372_457304351}

[[端口上实际的]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_1628476573}[报文发送的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围]{style="font-family:宋体"}

[[AIS condition]{lang="EN-US"}]{#struct_0_x1819_23372_457369887}

[[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_457173279}[报文的发送状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[yes]{lang="EN-US"}]{#struct_0_x1819_23372_457238815}[：表示正在发送]{lang="EN-US" style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no]{lang="EN-US"}]{#struct_0_x1819_23372_457566495}[：表示没有发送]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Time to enter the condition]{lang="EN-US"}]{#struct_0_x1819_23372_x796724424}

[[最近一次链路故障激发]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_x1819_23372_457632031}[报文发送的时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1314321628 .myid}
[]{#_Toc404795564}[]{#struct_0_x1819_23372_457435423}[]{#_Toc351105913}

**CFD \-- CFD配置命令 \-- display cfd dm one-way history**

------------------------------------------------------------------------

[**[display cfd dm one-way history]{lang="EN-US"}**]{#struct_0_x1819_23372_1898443343}[命令用来显示单向时延的测试结果。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_457500959}

[**[display cfd dm one-way history]{lang="EN-US"}**[ \[ **service-instance** *instance-id* \[ **mep** *mep-id* \] \]]{lang="EN-US"}]{#struct_0_x1819_23372_368576151}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_457828639}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_1946999790}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_457894175}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x714036708}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_457304348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x327838554}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_1943971503}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_457369884}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1440121867}[：显示指定服务实例内的测试结果，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。如果未指定本参数，将显示所有服务实例内的测试结果。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_457173276}[：显示指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1358886496}

[[对于内向]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_457238812}[，其所属服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的单向时延测试结果都相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1646033674}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_457566492}[显示所有服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[上单向时延的测试结果。]{style="font-family:宋体"}

[[\<Sysname\> display cfd dm one-way history]{lang="PT-BR"}]{#struct_0_x1819_23372_457435420}

[Service instance: 1]{lang="PT-BR"}

[MEP ID: 1003]{lang="PT-BR"}

[Sent 1DM total number: 0]{lang="PT-BR"}

[Received 1DM total number: 5]{lang="PT-BR"}

[Frame delay: 10ms 9ms 11ms 5ms 5ms]{lang="PT-BR"}

[Delay average: 8ms]{lang="PT-BR"}

[Frame delay variation: 5ms 4ms 6ms 0ms 0ms]{lang="PT-BR"}

[Variation average: 3ms]{lang="PT-BR"}

[MEP ID: 1004]{lang="PT-BR"}

[Sent 1DM total number: 0]{lang="PT-BR"}

[Received 1DM total number: 5]{lang="PT-BR"}

[Frame delay: 10ms 9ms 11ms 5ms 5ms]{lang="PT-BR"}

[Delay average: 8ms]{lang="PT-BR"}

[Delay variation: 5ms 4ms 6ms 0ms 0ms]{lang="PT-BR"}

[Variation average: 3ms]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Service instance: 2]{lang="PT-BR"}

[No MEP exists in the service instance.]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Service instance: 3]{lang="PT-BR"}

[MEP ID: 1023]{lang="PT-BR"}

[Sent 1DM total number: 5]{lang="PT-BR"}

[Received 1DM total number: 10]{lang="PT-BR"}

[Frame delay: 20ms 9ms 8ms 7ms 1ms 5ms 13ms 17ms 9ms 10ms]{lang="PT-BR"}

[Delay average: 9ms]{lang="PT-BR"}

[Delay variation: 19ms 8ms 7ms 6ms 0ms 4ms 12ms 16ms 8ms 9ms]{lang="PT-BR"}

[Variation average: 8ms]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Service instance: 4]{lang="PT-BR"}

[MEP ID: 1023]{lang="PT-BR"}

[Sent 1DM total number: 77]{lang="PT-BR"}

[Received 1DM total number: 0]{lang="PT-BR"}

[[表1-10 ]{lang="EN-US"}[display cfd dm one-way history]{lang="EN-US"}]{#struct_0_x1819_23372_457500956}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1196068395}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_368576142}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_457828636}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_457894172}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x714036703}[所在的服务实例]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_457304349}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_457369885}[的编号]{style="font-family:宋体"}

[[Sent 1DM total number]{lang="EN-US"}]{#struct_0_x1819_23372_x1440121868}

[[发出的]{style="font-family:宋体"}[1DM]{lang="EN-US"}]{#struct_0_x1819_23372_457173277}[报文数量]{style="font-family:宋体"}

[[Received 1DM total number]{lang="EN-US"}]{#struct_0_x1819_23372_457238813}

[[收到的]{style="font-family:宋体"}[1DM]{lang="EN-US"}]{#struct_0_x1819_23372_457566493}[报文数量]{style="font-family:宋体"}

[[Frame delay]{lang="EN-US"}]{#struct_0_x1819_23372_x796724430}

[[帧时延]{style="font-family:宋体"}]{#struct_0_x1819_23372_457632029}

[[Delay average]{lang="EN-US"}]{#struct_0_x1819_23372_457435421}

[[帧时延的平均值]{style="font-family:宋体"}]{#struct_0_x1819_23372_1898443345}

[[Delay variation]{lang="EN-US"}]{#struct_0_x1819_23372_457500957}

[[帧时延变化]{style="font-family:宋体"}]{#struct_0_x1819_23372_457828637}

[[Variation average]{lang="EN-US"}]{#struct_0_x1819_23372_457894173}

[[帧时延变化的平均值]{style="font-family:宋体"}]{#struct_0_x1819_23372_2023388293}

[[No MEP exists in the service instance]{lang="EN-US"}]{#struct_0_x1819_23372_180407195}

[[本服务实例内没有]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_2023453829}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2023257221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_1397142144}**[dm one-way]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset cfd dm one-way history]{lang="EN-US"}**]{#struct_0_x1819_23372_2023322757}

::: {#613343691 .myid}
[]{#_Toc404795565}[]{#struct_0_x1819_23372_x1030261168}[]{#_Toc286931281}[]{#_Toc286934667}[]{#_Toc286931282}[]{#_Toc286934668}[]{#_Toc286931283}[]{#_Toc286934669}[]{#_Toc286931284}[]{#_Toc286934670}[]{#_Toc286931285}[]{#_Toc286934671}[]{#_Toc286931286}[]{#_Toc286934672}[]{#_Toc286931287}[]{#_Toc286934673}[]{#_Toc286931288}[]{#_Toc286934674}[]{#_Toc286931289}[]{#_Toc286934675}[]{#_Toc286931290}[]{#_Toc286934676}[]{#_Toc286931291}[]{#_Toc286934677}[]{#_Toc286931292}[]{#_Toc286934678}[]{#_Toc286931293}[]{#_Toc286934679}[]{#_Toc286931294}[]{#_Toc286934680}[]{#_Toc286931295}[]{#_Toc286934681}[]{#_Toc286931296}[]{#_Toc286934682}[]{#_Toc286931297}[]{#_Toc286934683}[]{#_Toc286931298}[]{#_Toc286934684}[]{#_Toc286931299}[]{#_Toc286934685}[]{#_Toc286931300}[]{#_Toc286934686}[]{#_Toc286931301}[]{#_Toc286934687}[]{#_Toc286931302}[]{#_Toc286934688}[]{#_Toc286931303}[]{#_Toc286934689}[]{#_Toc286931304}[]{#_Toc286934690}[]{#_Toc286931305}[]{#_Toc286934691}[]{#_Toc286931306}[]{#_Toc286934692}[]{#_Toc286931307}[]{#_Toc286934693}[]{#_Toc286931309}[]{#_Toc286934695}[]{#_Toc286931311}[]{#_Toc286934697}[]{#_Toc286931313}[]{#_Toc286934699}[]{#_Toc286931314}[]{#_Toc286934700}[]{#_Toc286931316}[]{#_Toc286934702}[]{#_Toc286931317}[]{#_Toc286934703}[]{#_Toc286931318}[]{#_Toc286934704}[]{#_Toc286931319}[]{#_Toc286934705}[]{#_Toc286931320}[]{#_Toc286934706}[]{#_Toc286931321}[]{#_Toc286934707}[]{#_Toc286931322}[]{#_Toc286934708}[]{#_Toc286931323}[]{#_Toc286934709}[]{#_Toc286931324}[]{#_Toc286934710}[]{#_Toc286931325}[]{#_Toc286934711}[]{#_Toc286931326}[]{#_Toc286934712}[]{#_Toc286931327}[]{#_Toc286934713}[]{#_Toc286931328}[]{#_Toc286934714}[]{#_Toc286931329}[]{#_Toc286934715}[]{#_Toc286931330}[]{#_Toc286934716}[]{#_Toc286931331}[]{#_Toc286934717}[]{#_Toc286931332}[]{#_Toc286934718}[]{#_Toc286931333}[]{#_Toc286934719}[]{#_Toc286931334}[]{#_Toc286934720}[]{#_Toc286931336}[]{#_Toc286934722}[]{#_Toc286931337}[]{#_Toc286934723}[]{#_Toc286931338}[]{#_Toc286934724}[]{#_Toc286931339}[]{#_Toc286934725}[]{#_Toc286931340}[]{#_Toc286934726}[]{#_Toc286931341}[]{#_Toc286934727}[]{#_Toc286931342}[]{#_Toc286934728}[]{#_Toc286931344}[]{#_Toc286934730}[]{#_Toc286931345}[]{#_Toc286934731}[]{#_Toc286931346}[]{#_Toc286934732}[]{#_Toc286931349}[]{#_Toc286934735}[]{#_Toc286931350}[]{#_Toc286934736}[]{#_Toc286931351}[]{#_Toc286934737}[]{#_Toc239580617}[]{#_Toc239581765}[]{#_Toc246298436}[]{#_Toc249341911}[]{#_Toc286931382}[]{#_Toc286934768}[]{#_Toc286931384}[]{#_Toc286934770}[]{#_Toc286931385}[]{#_Toc286934771}[]{#_Toc286931386}[]{#_Toc286934772}[]{#_Toc286931387}[]{#_Toc286934773}[]{#_Toc286931388}[]{#_Toc286934774}[]{#_Toc286931389}[]{#_Toc286934775}[]{#_Toc286931390}[]{#_Toc286934776}[]{#_Toc286931391}[]{#_Toc286934777}[]{#_Toc286931392}[]{#_Toc286934778}[]{#_Toc286931393}[]{#_Toc286934779}[]{#_Toc286931394}[]{#_Toc286934780}[]{#_Toc286931395}[]{#_Toc286934781}[]{#_Toc286931396}[]{#_Toc286934782}[]{#_Toc286931397}[]{#_Toc286934783}[]{#_Toc286931398}[]{#_Toc286934784}[]{#_Toc286931399}[]{#_Toc286934785}[]{#_Toc286931400}[]{#_Toc286934786}[]{#_Toc286931401}[]{#_Toc286934787}[]{#_Toc286931402}[]{#_Toc286934788}[]{#_Toc286931403}[]{#_Toc286934789}[]{#_Toc286931404}[]{#_Toc286934790}[]{#_Toc286931405}[]{#_Toc286934791}[]{#_Toc286931406}[]{#_Toc286934792}[]{#_Toc286931408}[]{#_Toc286934794}[]{#_Toc286931410}[]{#_Toc286934796}[]{#_Toc286931411}[]{#_Toc286934797}[]{#_Toc286931421}[]{#_Toc286934807}[]{#_Toc286931423}[]{#_Toc286934809}[]{#_Toc286931424}[]{#_Toc286934810}[]{#_Toc286931425}[]{#_Toc286934811}[]{#_Toc286931426}[]{#_Toc286934812}[]{#_Toc286931427}[]{#_Toc286934813}[]{#_Toc286931428}[]{#_Toc286934814}[]{#_Toc286931429}[]{#_Toc286934815}[]{#_Toc286931430}[]{#_Toc286934816}[]{#_Toc286931431}[]{#_Toc286934817}[]{#_Toc286931432}[]{#_Toc286934818}[]{#_Toc286931433}[]{#_Toc286934819}[]{#_Toc286931434}[]{#_Toc286934820}[]{#_Toc286931435}[]{#_Toc286934821}[]{#_Toc286931436}[]{#_Toc286934822}[]{#_Toc286931437}[]{#_Toc286934823}[]{#_Toc286931438}[]{#_Toc286934824}[]{#_Toc286931439}[]{#_Toc286934825}[]{#_Toc286931440}[]{#_Toc286934826}[]{#_Toc286931442}[]{#_Toc286934828}[]{#_Toc286931444}[]{#_Toc286934830}[]{#_Toc286931445}[]{#_Toc286934831}[]{#_Toc286931446}[]{#_Toc286934832}[]{#_Toc286931447}[]{#_Toc286934833}[]{#_Toc286931448}[]{#_Toc286934834}[]{#_Toc286931449}[]{#_Toc286934835}[]{#_Toc286931450}[]{#_Toc286934836}[]{#_Toc286931451}[]{#_Toc286934837}[]{#_Toc286931452}[]{#_Toc286934838}[]{#_Toc286931453}[]{#_Toc286934839}[]{#_Toc286931454}[]{#_Toc286934840}[]{#_Toc286931455}[]{#_Toc286934841}[]{#_Toc286931456}[]{#_Toc286934842}[]{#_Toc286931457}[]{#_Toc286934843}[]{#_Toc286931458}[]{#_Toc286934844}[]{#_Toc286931459}[]{#_Toc286934845}[]{#_Toc286931460}[]{#_Toc286934846}[]{#_Toc286931461}[]{#_Toc286934847}[]{#_Toc286931462}[]{#_Toc286934848}[]{#_Toc286931463}[]{#_Toc286934849}[]{#_Toc286931464}[]{#_Toc286934850}[]{#_Toc286931465}[]{#_Toc286934851}[]{#_Toc286931466}[]{#_Toc286934852}[]{#_Toc286931467}[]{#_Toc286934853}[]{#_Toc286931469}[]{#_Toc286934855}[]{#_Toc286931470}[]{#_Toc286934856}[]{#_Toc286931471}[]{#_Toc286934857}[]{#_Toc286931474}[]{#_Toc286934860}[]{#_Toc286931477}[]{#_Toc286934863}[]{#_Toc286931481}[]{#_Toc286934867}[]{#_Toc286931482}[]{#_Toc286934868}[]{#_Toc286931484}[]{#_Toc286934870}[]{#_Toc286931491}[]{#_Toc286934877}[]{#_Toc286931530}[]{#_Toc286934916}[]{#_Toc286931532}[]{#_Toc286934918}[]{#_Toc286931533}[]{#_Toc286934919}[]{#_Toc286931534}[]{#_Toc286934920}[]{#_Toc286931535}[]{#_Toc286934921}[]{#_Toc286931536}[]{#_Toc286934922}[]{#_Toc286931537}[]{#_Toc286934923}[]{#_Toc286931538}[]{#_Toc286934924}[]{#_Toc286931539}[]{#_Toc286934925}[]{#_Toc286931540}[]{#_Toc286934926}[]{#_Toc286931541}[]{#_Toc286934927}[]{#_Toc286931542}[]{#_Toc286934928}[]{#_Toc286931543}[]{#_Toc286934929}[]{#_Toc286931544}[]{#_Toc286934930}[]{#_Toc286931545}[]{#_Toc286934931}[]{#_Toc286931546}[]{#_Toc286934932}[]{#_Toc286931547}[]{#_Toc286934933}[]{#_Toc286931548}[]{#_Toc286934934}[]{#_Toc286931549}[]{#_Toc286934935}[]{#_Toc286931550}[]{#_Toc286934936}[]{#_Toc286931551}[]{#_Toc286934937}[]{#_Toc286931552}[]{#_Toc286934938}[]{#_Toc286931555}[]{#_Toc286934941}[]{#_Toc286931560}[]{#_Toc286934946}[]{#_Toc286931561}[]{#_Toc286934947}[]{#_Toc286931566}[]{#_Toc286934952}[]{#_Toc286931567}[]{#_Toc286934953}[]{#_Toc286931600}[]{#_Toc286934986}[]{#_Toc286931602}[]{#_Toc286934988}[]{#_Toc286931603}[]{#_Toc286934989}[]{#_Toc286931604}[]{#_Toc286934990}[]{#_Toc286931605}[]{#_Toc286934991}[]{#_Toc286931606}[]{#_Toc286934992}[]{#_Toc286931607}[]{#_Toc286934993}[]{#_Toc286931608}[]{#_Toc286934994}[]{#_Toc286931609}[]{#_Toc286934995}[]{#_Toc286931610}[]{#_Toc286934996}[]{#_Toc286931611}[]{#_Toc286934997}[]{#_Toc286931612}[]{#_Toc286934998}[]{#_Toc286931613}[]{#_Toc286934999}[]{#_Toc286931614}[]{#_Toc286935000}[]{#_Toc286931615}[]{#_Toc286935001}[]{#_Toc286931616}[]{#_Toc286935002}[]{#_Toc286931617}[]{#_Toc286935003}[]{#_Toc286931618}[]{#_Toc286935004}[]{#_Toc286931619}[]{#_Toc286935005}[]{#_Toc286931620}[]{#_Toc286935006}[]{#_Toc286931621}[]{#_Toc286935007}[]{#_Toc286931622}[]{#_Toc286935008}[]{#_Toc286931623}[]{#_Toc286935009}[]{#_Toc286931624}[]{#_Toc286935010}[]{#_Toc286931625}[]{#_Toc286935011}[]{#_Toc286931629}[]{#_Toc286935015}[]{#_Toc286931631}[]{#_Toc286935017}[]{#_Toc286931636}[]{#_Toc286935022}[]{#_Toc286931638}[]{#_Toc286935024}[]{#_Toc286931640}[]{#_Toc286935026}[]{#_Toc286931641}[]{#_Toc286935027}[]{#_Toc286931642}[]{#_Toc286935028}[]{#_Toc286931643}[]{#_Toc286935029}[]{#_Toc286931645}[]{#_Toc286935031}[]{#_Toc286931648}[]{#_Toc286935034}[]{#_Toc286931650}[]{#_Toc286935036}[]{#_Toc286931651}[]{#_Toc286935037}[]{#_Toc286931652}[]{#_Toc286935038}[]{#_Toc286931656}[]{#_Toc286935042}[]{#_Toc286931657}[]{#_Toc286935043}[]{#_Toc286931688}[]{#_Toc286935074}

**CFD \-- CFD配置命令 \-- display cfd linktrace-reply**

------------------------------------------------------------------------

[**[display cfd linktrace-reply]{lang="EN-US"}**]{#struct_0_x1819_23372_180245116}[命令用来显示]{style="font-family:
宋体"}[MEP]{lang="EN-US"}[上获得的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_987011071}

[**[display cfd linktrace-reply]{lang="EN-US"}**[ \[ **service-instance** *instance-id* \[ **mep** *mep-id* \] \]]{lang="EN-US"}]{#struct_0_x1819_23372_1603949297}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1505084356}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1204312152}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1265318599}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_737433974}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x279182927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x2004227280}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_641633951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2001737529}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_1020097821}[：显示指定服务实例内的信息，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。如果未指定本参数，将显示所有服务实例内的信息。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x810303673}[：显示指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的信息，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_510030962}

[[本命令只显示执行]{style="font-family:宋体"}**[cfd linktrace]{lang="EN-US"}**]{#struct_0_x1819_23372_1179724926}[命令所收到的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x887290092}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_737499510}[显示所有服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[保存的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd linktrace-reply]{lang="EN-US"}]{#struct_0_x1819_23372_2007333435}

[Service instance: 1       MEP ID: 1003]{lang="EN-US"}

[MAC address               TTL     Last MAC          Relay action]{lang="EN-US"}

[0000-fc00-6505            63      0000-fc00-6504    MPDB]{lang="EN-US"}

[000f-e269-a852            62      0000-fc00-6505    FDB]{lang="EN-US"}

[0000-fc00-6508            61      000f-e269-a852    Hit]{lang="EN-US"}

[Service instance: 2       MEP ID: 1023]{lang="EN-US"}

[MAC address               TTL     Last MAC          Relay action]{lang="EN-US"}

[0000-fc00-6508            61      000f-e269-a852    Hit]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display cfd linktrace-reply]{lang="EN-US"}]{#struct_0_x1819_23372_1837277740}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_250984877}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x527911024}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1308395943}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_1638184763}

[[发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_737565046}[报文的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[所在的服务实例]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_1646598745}

[[发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_x1205475322}[报文的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1819_23372_1113318072}

[[LTR]{lang="EN-US"}]{#struct_0_x1819_23372_1950525983}[报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_x1819_23372_533847407}

[[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_x801492428}[经过此设备时的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Last MAC]{lang="EN-US"}]{#struct_0_x1819_23372_737630582}

[[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_x1573422865}[报文所经过上一跳设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Relay action]{lang="EN-US"}]{#struct_0_x1819_23372_1956021943}

[[表示转发设备在]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_x632180614}[地址表中是否找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hit]{lang="EN-US"}]{#struct_0_x1819_23372_x90447346}[：表示本设备就是目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FDB]{lang="EN-US"}]{#struct_0_x1819_23372_x1691779891}[：表示在转发表中找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MPDB]{lang="EN-US"}]{#struct_0_x1819_23372_737696118}[：表示没有找到目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，或者在]{style="font-family:宋体"}[MEP]{lang="EN-US"}[或]{style="font-family:宋体"}[MIP]{lang="EN-US"}[数据库中找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x26695737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd linktrace]{lang="EN-US"}**]{#struct_0_x1819_23372_x393129503}

::: {#-1386265867 .myid}
[]{#_Toc404795566}[]{#struct_0_x1819_23372_x651490257}

**CFD \-- CFD配置命令 \-- display cfd linktrace-reply auto-detection**

------------------------------------------------------------------------

[**[display cfd linktrace-reply auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_914420365}[命令用来显示自动发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文后收到的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1160965384}

[**[display cfd linktrace-reply auto-detection ]{lang="EN-US"}**[\[ **size** *size-value* \]]{lang="EN-US"}]{#struct_0_x1819_23372_1109563828}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_225816234}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_737761654}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1526126073}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1677964657}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_252020548}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1687565997}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_1015348202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1487099360}

[**[size]{lang="EN-US"}***[ size-value]{lang="EN-US"}*]{#struct_0_x1819_23372_412260184}[：显示最近]{style="font-family:宋体"}*[size-value]{lang="EN-US"}*[次自动检测的结果，]{style="font-family:宋体"}*[size-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。如果未指定本参数，将显示缓冲区中的全部信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_426611770}

[[本命令只显示执行]{style="font-family:宋体"}**[cfd linktrace auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_737827190}[命令所收到的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2098570916}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x23180210}[显示自动发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文所收到的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文的内容。]{style="font-family:宋体"}

[[\<Sysname\> display cfd linktrace-reply auto-detection]{lang="EN-US"}]{#struct_0_x1819_23372_x61551539}

[Service instance: 1       MEP ID: 1003    Time: 2013/05/22 10:43:57]{lang="EN-US"}

[Target MEP ID: 2005       TTL: 64]{lang="EN-US"}

[MAC address               TTL     Last MAC          Relay action]{lang="EN-US"}

[0000-fc00-6505            63      0000-fc00-6504    MPDB]{lang="EN-US"}

[000f-e269-a852            62      0000-fc00-6505    FDB]{lang="EN-US"}

[0000-fc00-6508            61      000f-e269-a852    Hit]{lang="EN-US"}

[Service instance: 2       MEP ID: 1023    Time: 2013/05/22 10:44:06]{lang="EN-US"}

[Target MEP ID: 2025       TTL: 64]{lang="EN-US"}

[MAC address               TTL     Last MAC          Relay action]{lang="EN-US"}

[0000-fc00-6508            61      000f-e269-a852    Hit]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display cfd linktrace-reply auto-detection]{lang="EN-US"}]{#struct_0_x1819_23372_x710725547}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_244628507}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_1287073940}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_737892726}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_1330144111}

[[发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_145441425}[报文的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[所在的服务实例]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_2029998620}

[[发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_1312213740}[报文的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[Time]{lang="EN-US"}]{#struct_0_x1819_23372_x1267947622}

[[自动发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_x1166742705}[报文的时间]{style="font-family:宋体"}

[[Target MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_736909686}

[[目标]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1140651498}[的编号]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_x1819_23372_629848118}

[[自动发送的]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_x134232559}[报文中的初始]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1819_23372_770493218}

[[LTR]{lang="EN-US"}]{#struct_0_x1819_23372_518332942}[报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_x1819_23372_736975222}

[[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_1988960949}[报文经过此设备时的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Last MAC]{lang="EN-US"}]{#struct_0_x1819_23372_x1029802417}

[[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_x15908573}[报文所经过上一跳设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Relay action]{lang="EN-US"}]{#struct_0_x1819_23372_x1331451233}

[[表示转发设备在]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_x888318361}[地址表中是否找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hit]{lang="EN-US"}]{#struct_0_x1819_23372_737433971}[：表示本设备就是目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FDB]{lang="EN-US"}]{#struct_0_x1819_23372_x279182930}[：表示在转发表中找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MPDB]{lang="EN-US"}]{#struct_0_x1819_23372_x2004554959}[：表示没有找到目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，或者在]{style="font-family:宋体"}[MEP]{lang="EN-US"}[或]{style="font-family:宋体"}[MIP]{lang="EN-US"}[数据库中找到了目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_432454916}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd linktrace auto-detection]{lang="EN-US"}**]{#struct_0_x1819_23372_489568377}

::: {#198162364 .myid}
[]{#_Toc404795567}[]{#struct_0_x1819_23372_64874142}[]{#_Toc286931692}[]{#_Toc286935078}[]{#_Toc286931693}[]{#_Toc286935079}[]{#_Toc286931694}[]{#_Toc286935080}[]{#_Toc286931695}[]{#_Toc286935081}[]{#_Toc286931696}[]{#_Toc286935082}[]{#_Toc286931697}[]{#_Toc286935083}[]{#_Toc286931698}[]{#_Toc286935084}[]{#_Toc286931699}[]{#_Toc286935085}[]{#_Toc286931700}[]{#_Toc286935086}[]{#_Toc286931701}[]{#_Toc286935087}[]{#_Toc286931702}[]{#_Toc286935088}[]{#_Toc286931703}[]{#_Toc286935089}[]{#_Toc286931704}[]{#_Toc286935090}[]{#_Toc286931705}[]{#_Toc286935091}[]{#_Toc286931706}[]{#_Toc286935092}[]{#_Toc286931707}[]{#_Toc286935093}[]{#_Toc286931708}[]{#_Toc286935094}[]{#_Toc286931709}[]{#_Toc286935095}[]{#_Toc286931710}[]{#_Toc286935096}[]{#_Toc286931711}[]{#_Toc286935097}[]{#_Toc286931712}[]{#_Toc286935098}[]{#_Toc286931713}[]{#_Toc286935099}[]{#_Toc286931714}[]{#_Toc286935100}[]{#_Toc286931715}[]{#_Toc286935101}[]{#_Toc286931722}[]{#_Toc286935108}[]{#_Toc286931727}[]{#_Toc286935113}[]{#_Toc286931728}[]{#_Toc286935114}[]{#_Toc286931731}[]{#_Toc286935117}[]{#_Toc286931732}[]{#_Toc286935118}[]{#_Toc286931760}[]{#_Toc286935146}

**CFD \-- CFD配置命令 \-- display cfd md**

------------------------------------------------------------------------

[**[display cfd md]{lang="EN-US"}**]{#struct_0_x1819_23372_833370424}[命令用来显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1535615951}

[**[display cfd md]{lang="EN-US"}**]{#struct_0_x1819_23372_737499507}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x331318726}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1463843060}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1780551757}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_982969188}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_1838990809}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x369355788}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x1519228942}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_869244488}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_737565043}[显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd md]{lang="EN-US"}]{#struct_0_x1819_23372_1646598748}

[CFD is enabled.]{lang="EN-US"}

[Maintenance domains configured: 4 in total]{lang="EN-US"}

[Level  Index      Maintenance domain                          MD format  MD ID]{lang="EN-US"}

[0      1          md_0                                        CHARSTRING md_0]{lang="EN-US"}

[1      2          md_1                                        DNS        dns1]{lang="EN-US"}

[2      3          md_2                                        MAC        0001-00]{lang="EN-US"}

[01-0001-1]{lang="EN-US"}

[3      4          md_3                                        NONE       Without]{lang="EN-US"}

[ ID]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display cfd md]{lang="EN-US"}]{#struct_0_x1819_23372_x1205803002}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_245632675}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_2140980212}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1719650805}

[[CFD is enabled]{lang="EN-US"}]{#struct_0_x1819_23372_x715338905}

[[表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}]{#struct_0_x1819_23372_737630579}[功能处于开启状态]{style="font-family:宋体"}

[[CFD is disabled]{lang="EN-US"}]{#struct_0_x1819_23372_x853378822}

[[表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}]{#struct_0_x1819_23372_563320578}[功能处于关闭状态]{style="font-family:宋体"}

[[Maintenance domains configured]{lang="EN-US"}]{#struct_0_x1819_23372_x1619215015}

[[系统配置的]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_x1819_23372_1326881796}[个数]{style="font-family:宋体"}

[[Level]{lang="EN-US"}]{#struct_0_x1819_23372_1525720954}

[[MD]{lang="EN-US"}]{#struct_0_x1819_23372_737696115}[级别]{style="font-family:宋体"}

[[Index]{lang="EN-US"}]{#struct_0_x1819_23372_x26695732}

[[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x393129500}[索引号]{style="font-family:宋体"}

[[Maintenance domain]{lang="EN-US"}]{#struct_0_x1819_23372_x651424721}

[[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x197713890}[名称]{style="font-family:宋体"}

[[MD format]{lang="EN-US"}]{#struct_0_x1819_23372_x1973368704}

[[MD]{lang="EN-US"}]{#struct_0_x1819_23372_737761651}[名称的格式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CHARSTRING]{lang="EN-US"}]{#struct_0_x1819_23372_1526126076}[：表示]{style="font-family:宋体"}[字符串]{lang="EN-US" style="font-family:宋体"}[格式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNS]{lang="EN-US"}]{#struct_0_x1819_23372_x1677768049}[：表示采用]{style="font-family:宋体"}[DNS]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_2146255592}[：表示由]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和一个整数构成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_x1819_23372_x1319773877}[：表示不携带]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[MD ID]{lang="EN-US"}]{#struct_0_x1819_23372_737827187}

[[MD ID]{lang="EN-US"}]{#struct_0_x1819_23372_x240081239}[的值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1819_23372_1076856070}[CHARSTRING]{lang="EN-US"}[格式下，显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}[本身]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1819_23372_x102371418}[DNS]{lang="EN-US"}[格式下，显示为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_1466590621}[格式下，显示]{lang="EN-US" style="font-family:宋体"}[方式]{style="font-family:宋体"}[为]{lang="EN-US" style="font-family:宋体"}[MAC address]{lang="EN-US"}[-]{lang="EN-US"}[Subnumber]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[NONE]{lang="EN-US"}]{#struct_0_x1819_23372_737892723}[格式下，显示为]{lang="EN-US" style="font-family:宋体"}[Without ID]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1325481727 .myid}
[]{#_Toc404795568}[]{#struct_0_x1819_23372_1330144116}

**CFD \-- CFD配置命令 \-- display cfd mep**

------------------------------------------------------------------------

[**[display cfd mep]{lang="EN-US"}**]{#struct_0_x1819_23372_145244817}[命令用来显示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的属性和运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1418409630}

[**[display cfd mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}***[ service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x535839615}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_72487764}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x73631828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1374783265}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1870812857}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_736909683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1140651493}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_629389366}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_694148701}

[**[mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x779493689}[：表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x479103199}[：表示服务实例的编号，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_396657890}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_736975219}[显示服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[内]{style="font-family:宋体"}[MEP 50]{lang="EN-US"}[的属性和运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd mep 50 service-instance 1]{lang="EN-US"}]{#struct_0_x1819_23372_737433972}

[Interface: GigabitEthernet1/0/2]{lang="FR"}

[Maintenance domain: md_0]{lang="FR"}

[Maintenance domain index]{lang="FR"}[：]{style="font-family:宋体"}[1]{lang="FR"}

[Maintenance association: ma_0]{lang="EN-US"}

[Maintenance association index]{lang="EN-US"}[：]{style="font-family:宋体"}[1]{lang="EN-US"}

[Level: 0        VLAN: 1         Direction: Outbound]{lang="EN-US"}

[Current state: Active          CCM send: Enabled]{lang="EN-US"}

[FNG state: FNG_DEFECT_REPORTED]{lang="EN-US"}

[ ]{lang="EN-US"}

[CCM:]{lang="EN-US"}

[Current state: CCI_WAITING]{lang="EN-US"}

[Interval: 1s        SendCCM: 12018]{lang="EN-US"}

[ ]{lang="EN-US"}

[Loopback:]{lang="EN-US"}

[NextSeqNumber: 8877]{lang="EN-US"}

[SendLBR: 0          ReceiveInOrderLBR: 0          ReceiveOutOrderLBR: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Linktrace:]{lang="EN-US"}

[NextSeqNumber: 8877]{lang="EN-US"}

[SendLTR: 0          ReceiveLTM: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[No CCM received from some remote MEPs.]{lang="EN-US"}

[ ]{lang="EN-US"}

[One or more streams of error CCMs is received. The last received CCM:]{lang="EN-US"}

[Maintenance domain: (Without ID)]{lang="EN-US"}

[Maintenance association: matest1]{lang="EN-US"}

[MEP ID: 5      Sequence Number:0x50A]{lang="EN-US"}

[MAC Address: 0011-2233-4402]{lang="EN-US"}

[Received Time: 2013/03/06 13:01:34]{lang="EN-US"}

[ ]{lang="EN-US"}

[One or more streams of cross-connect CCMs is received. The last received CCM:]{lang="EN-US"}

[Maintenance domain: mdtest1]{lang="EN-US"}

[Maintenance association:matest1]{lang="EN-US"}

[MEP ID: 6      Sequence Number:0x63A]{lang="EN-US"}

[MAC Address: 0011-2233-4401]{lang="EN-US"}

[Received Time: 2013/03/06 13:01:34]{lang="EN-US"}

[ ]{lang="EN-US"}

[Some other MEPs are transmitting the RDI bit.]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display cfd mep]{lang="EN-US"}]{#struct_0_x1819_23372_x279182933}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_242471211}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2004489423}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2080615670}

[[Interface]{lang="EN-US"}]{#struct_0_x1819_23372_1793903720}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x2121467466}[所在的接口]{style="font-family:宋体"}

[[Maintenance domain]{lang="EN-US"}]{#struct_0_x1819_23372_737499508}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x331318733}[所在的]{style="font-family:宋体"}[MD]{lang="EN-US"}[（如果]{style="font-family:宋体"}[MD]{lang="EN-US"}[为无]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称的格式，则该]{style="font-family:宋体"}[MD]{lang="EN-US"}[的名称显示为]{style="font-family:宋体"}[Without ID]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Maintenance domain index]{lang="FR"}]{#struct_0_x1819_23372_x1463646451}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x174029588}[所在]{style="font-family:宋体"}[MD]{lang="EN-US"}[的索引号]{style="font-family:宋体"}

[[Maintenance association]{lang="EN-US"}]{#struct_0_x1819_23372_259319840}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x39868686}[所在的]{style="font-family:宋体"}[MA]{lang="EN-US"}

[[Maintenance association index]{lang="EN-US"}]{#struct_0_x1819_23372_x1556607073}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_737565044}[所在]{style="font-family:宋体"}[MA]{lang="EN-US"}[的索引号]{style="font-family:宋体"}

[[Level]{lang="EN-US"}]{#struct_0_x1819_23372_1646598743}

[[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x1205344250}[的级别]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x1819_23372_x9401028}

[[MA]{lang="EN-US"}]{#struct_0_x1819_23372_99109208}[所在的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Direction]{lang="EN-US"}]{#struct_0_x1819_23372_x1164315047}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_737630580}[的方向]{style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_x1819_23372_x1573422863}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_793222529}[的当前状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1819_23372_659928147}[：激活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x1819_23372_1488897615}[：未激活]{style="font-family:宋体"}

[[CCM send]{lang="EN-US"}]{#struct_0_x1819_23372_1555420218}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_737696116}[是否发送]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FNG state]{lang="EN-US"}]{#struct_0_x1819_23372_x26695731}

[[FNG]{lang="EN-US"}]{#struct_0_x1819_23372_x393129497}[（]{style="font-family:宋体"}[Fault Notification Generator]{lang="EN-US"}[，错误提示生成器）状态机的状态值（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FNG_RESET]{lang="EN-US"}]{#struct_0_x1819_23372_1686899752}[：故障已清除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FNG_DEFECT]{lang="EN-US"}]{#struct_0_x1819_23372_x365083087}[：检测到故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FNG_REPORT_DEFECT]{lang="EN-US"}]{#struct_0_x1819_23372_737761652}[：报告故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FNG_DEFECT_REPORTED]{lang="EN-US"}]{#struct_0_x1819_23372_1526126079}[：已报告故障]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FNG_DEFECT_CLEARING]{lang="EN-US"}]{#struct_0_x1819_23372_x1678620017}[：故障清除中]{style="font-family:宋体"}

[[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_x35714877}

[[与]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_737827188}[报文有关的信息]{style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_x1819_23372_x240081236}

[[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_1076790534}[报文发送状态的状态值（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CCI_IDLE]{lang="EN-US"}]{#struct_0_x1819_23372_x496356183}[：初始状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CCI_WAITING]{lang="EN-US"}]{#struct_0_x1819_23372_737892724}[：发送状态]{style="font-family:宋体"}

[[Interval]{lang="EN-US"}]{#struct_0_x1819_23372_1330144109}

[[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_144917136}[报文发送的时间间隔（"]{style="font-family:宋体"}[Not supported]{lang="EN-US"}["表示该]{style="font-family:宋体"}[MEP]{lang="EN-US"}[不支持该间隔的检测）]{style="font-family:宋体"}

[[SendCCM]{lang="EN-US"}]{#struct_0_x1819_23372_1565767764}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_736909684}[已发送的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文的数量（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[Loopback]{lang="EN-US"}]{#struct_0_x1819_23372_1140651500}

[[与环回相关的信息]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1326991313}

[[NextSeqNumber]{lang="EN-US"}]{#struct_0_x1819_23372_1327478511}

[[下一个要发送的]{style="font-family:宋体"}[LBM]{lang="EN-US"}]{#struct_0_x1819_23372_1952831539}[报文的序号]{style="font-family:宋体"}

[[SendLBR]{lang="EN-US"}]{#struct_0_x1819_23372_736975220}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1988960951}[已发送的]{style="font-family:宋体"}[LBR]{lang="EN-US"}[报文的数量。如果]{style="font-family:宋体"}[MEP]{lang="EN-US"}[为入方向，则不进行]{style="font-family:宋体"}[LBR]{lang="EN-US"}[报文的计数]{style="font-family:宋体"}

[[ReceiveInOrderLBR]{lang="EN-US"}]{#struct_0_x1819_23372_x1030326704}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_737433969}[收到的序列正确的]{style="font-family:宋体"}[LBR]{lang="EN-US"}[报文的数量]{style="font-family:宋体"}

[[ReceiveOutOrderLBR]{lang="EN-US"}]{#struct_0_x1819_23372_1677132214}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1853693468}[收到的乱序的]{style="font-family:宋体"}[LBR]{lang="EN-US"}[报文的数量]{style="font-family:宋体"}

[[Linktrace]{lang="EN-US"}]{#struct_0_x1819_23372_737499505}

[[与链路跟踪相关的信息]{style="font-family:宋体"}]{#struct_0_x1819_23372_x331318728}

[[NextSeqNumber]{lang="EN-US"}]{#struct_0_x1819_23372_x1462925556}

[[下一个要发送的]{style="font-family:宋体"}[LTM]{lang="EN-US"}]{#struct_0_x1819_23372_417586079}[报文的序号]{style="font-family:宋体"}

[[SendLTR]{lang="EN-US"}]{#struct_0_x1819_23372_737565041}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1646598746}[已发送的]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文的数量。如果]{style="font-family:宋体"}[MEP]{lang="EN-US"}[为入方向，则不进行]{style="font-family:宋体"}[LTR]{lang="EN-US"}[报文的计数]{style="font-family:宋体"}

[[ReceiveLTM]{lang="EN-US"}]{#struct_0_x1819_23372_x1205671930}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1745210360}[收到的]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文的数量]{style="font-family:宋体"}

[[No CCM received from some remote MEPs.]{lang="EN-US"}]{#struct_0_x1819_23372_737630577}

[[表明没有收到某些远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x853378828}[发送的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文（本信息在有]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文丢失的时候才会显示）]{style="font-family:宋体"}

[[One or more streams of error CCMs is received. The last received CCM:]{lang="EN-US"}]{#struct_0_x1819_23372_562927362}

[[表明收到了错误的]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_737696113}[报文，并显示最后一个错误的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文的内容（本信息在收到了错误的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文时才会显示）]{style="font-family:宋体"}

[[Maintenance domain]{lang="FR"}]{#struct_0_x1819_23372_x26695726}

[[最后一个错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_1563185632}[报文所属的]{style="font-family:宋体"}[MD]{lang="EN-US"}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[Maintenance association]{lang="FR"}]{#struct_0_x1819_23372_282237620}

[[最后一个错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_737761649}[报文所属的]{style="font-family:宋体"}[MA]{lang="EN-US"}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x430189068}

[[发送最后一个错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_2088899143}[报文的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[编号（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[Sequence Number]{lang="EN-US"}]{#struct_0_x1819_23372_737827185}

[[最后一个错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_x240081241}[报文的序列号（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_x1819_23372_1076331777}

[[发送错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_737892721}[报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Received Time]{lang="EN-US"}]{#struct_0_x1819_23372_1330144114}

[[收到最后一个错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_145113745}[报文的时间（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[One or more streams of cross-connect CCMs is received. The last received CCM:]{lang="EN-US"}]{#struct_0_x1819_23372_736909681}

[[网络的配置中可能存在有交叉连接的情况，本信息表明收到了交叉连接的报文，并显示最后一个交叉连接的报文的内容（本信息在收到]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_x1819_23372_1140651495}[报文后，认为属于交叉连接时才显示）]{style="font-family:宋体"}

[[Some other MEPs are transmitting the RDI bit.]{lang="EN-US"}]{#struct_0_x1819_23372_736975217}

[[收到了其他]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x732028238}[发送的]{style="font-family:宋体"}[RDI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Defect Indication]{lang="EN-US"}[，远程故障指示）标志位被置位的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文（本信息在收到该种类型的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文后才显示）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-264529161 .myid}
[]{#_Toc404795569}[]{#struct_0_x1819_23372_840730249}[]{#_Toc219716719}

**CFD \-- CFD配置命令 \-- display cfd meplist**

------------------------------------------------------------------------

[**[display cfd meplist]{lang="EN-US"}**]{#struct_0_x1819_23372_x1174186843}[命令用来显示服务实例内的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x951910952}

[**[display cfd meplist]{lang="EN-US"}**[ \[ **service-instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_x1819_23372_1692660459}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1894950809}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x530668419}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_737433970}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x279182931}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x2004620495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x438768526}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x767916144}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_700570950}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x2012863726}[：显示指定服务实例内的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。如果未指定本参数，将显示所有服务实例内的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_161673790}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_380205406}[显示服务实例]{style="font-family:宋体"}[5]{lang="EN-US"}[内的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[\<Sysname\> display cfd meplist service-instance 5]{lang="EN-US"}]{#struct_0_x1819_23372_737499506}

[Service instance: 5]{lang="EN-US"}

[MEP list: 1 to 20, 30, 50.]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display cfd meplist]{lang="EN-US"}]{#struct_0_x1819_23372_x331318727}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_267002357}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1463908596}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x449504908}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_1950432963}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_132201301}[所在的服务实例]{style="font-family:宋体"}

[[MEP list]{lang="EN-US"}]{#struct_0_x1819_23372_x1321102928}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1410133886}[列表，]{style="font-family:宋体"}[NULL]{lang="EN-US"}[表示该服务实例没有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#196851644 .myid}
[]{#_Toc404795570}[]{#struct_0_x1819_23372_737565042}

**CFD \-- CFD配置命令 \-- display cfd mp**

------------------------------------------------------------------------

[**[display cfd mp]{lang="EN-US"}**]{#struct_0_x1819_23372_1646598749}[命令用来显示]{style="font-family:宋体"}[MP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1205737466}

[**[display cfd mp ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1819_23372_x1155214059}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x20229150}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x430807717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1785169221}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_1131169559}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_737630578}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x853378823}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_563386114}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_337022479}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1819_23372_x1226178890}[：显示指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1100755880}

[[MP]{lang="EN-US"}]{#struct_0_x1819_23372_x1777015565}[信息的显示顺序：按照接口名称的顺序排列；在同一个接口上，按照先显示服务于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MP,]{lang="EN-US"}[再显示不服务于任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MP]{lang="EN-US"}[的顺序排列。服务于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MP]{lang="EN-US"}[按照]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[从小到大的顺序排列；在同一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内按照]{style="font-family:宋体"}[MIP]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[（级别从高到低）的顺序排列；不服务于任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[按级别从高到低的顺序排列。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_860358911}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_804148897}[显示所有接口上]{style="font-family:宋体"}[MP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd mp]{lang="EN-US"}]{#struct_0_x1819_23372_737696114}

[Interface GigabitEthernet1/0/1   VLAN 100]{lang="EN-US"}

[MIP              Level: 2    Service instance: 102]{lang="EN-US"}

[Maintenance domain: md_2]{lang="EN-US"}

[Maintenance domain index]{lang="EN-US"}[：]{style="font-family:宋体"}[3]{lang="EN-US"}

[Maintenance association: ma_2]{lang="EN-US"}

[Maintenance association index: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[MEP ID: 101      Level: 1    Service instance: 101    Direction: Inbound]{lang="EN-US"}

[Maintenance domain: md_1]{lang="EN-US"}

[Maintenance domain index]{lang="EN-US"}[：]{style="font-family:宋体"}[2]{lang="EN-US"}

[Maintenance association: ma_1]{lang="EN-US"}

[Maintenance association index: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[MEP ID: 100      Level: 0    Service instance: 100    Direction: Outbound]{lang="EN-US"}

[Maintenance domain: md_0]{lang="EN-US"}

[Maintenance domain index]{lang="EN-US"}[：]{style="font-family:宋体"}[1]{lang="EN-US"}

[Maintenance association: ma_0]{lang="EN-US"}

[Maintenance association index: 1]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display cfd mp]{lang="EN-US"}]{#struct_0_x1819_23372_x26695733}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_261812751}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x393129499}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_1687817256}

[[Interface GigabitEthernet1/0/1   VLAN 100]{lang="EN-US"}]{#struct_0_x1819_23372_737761650}

[[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_x1819_23372_1526126077}[在]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[中的]{style="font-family:宋体"}[MP]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[MIP]{lang="EN-US"}]{#struct_0_x1819_23372_x1677702513}

[[该]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x1819_23372_864132417}[是]{style="font-family:宋体"}[MIP]{lang="EN-US"}

[[Level]{lang="EN-US"}]{#struct_0_x1819_23372_x1122399402}

[[MP]{lang="EN-US"}]{#struct_0_x1819_23372_x388370853}[所处的]{style="font-family:宋体"}[MD]{lang="EN-US"}[级别]{style="font-family:宋体"}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_290079886}

[[MP]{lang="EN-US"}]{#struct_0_x1819_23372_737827186}[所在的服务实例]{style="font-family:宋体"}

[[Maintenance domain]{lang="EN-US"}]{#struct_0_x1819_23372_x240081238}

[[MP]{lang="EN-US"}]{#struct_0_x1819_23372_1076921606}[所属的]{style="font-family:宋体"}[MD]{lang="EN-US"}

[[Maintenance domain  index]{lang="EN-US"}]{#struct_0_x1819_23372_x870924475}

[[MP]{lang="EN-US"}]{#struct_0_x1819_23372_1963775307}[所属]{style="font-family:宋体"}[MD]{lang="EN-US"}[的索引号]{style="font-family:宋体"}

[[Maintenance association]{lang="EN-US"}]{#struct_0_x1819_23372_x2017093006}

[[MP]{lang="EN-US"}]{#struct_0_x1819_23372_737892722}[所属的]{style="font-family:宋体"}[MA]{lang="EN-US"}

[[Maintenance association index]{lang="EN-US"}]{#struct_0_x1819_23372_1330144115}

[[MP]{lang="EN-US"}]{#struct_0_x1819_23372_145179281}[所属]{style="font-family:宋体"}[MA]{lang="EN-US"}[的索引号]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_x2018034821}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1749103231}[的编号]{style="font-family:宋体"}

[[Direction]{lang="EN-US"}]{#struct_0_x1819_23372_x1909141732}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_736909682}[的方向：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inbound]{lang="EN-US"}]{#struct_0_x1819_23372_1140651494}[：表示入方向]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Outbound]{lang="EN-US"}]{#struct_0_x1819_23372_629061686}[：表示出方向]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#2035357525 .myid}
[]{#_Toc404795571}[]{#struct_0_x1819_23372_x1492507854}

**CFD \-- CFD配置命令 \-- display cfd remote-mep**

------------------------------------------------------------------------

[**[display cfd remote-mep]{lang="EN-US"}**]{#struct_0_x1819_23372_x17920575}[命令用来显示远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1240244311}

[**[display cfd remote-mep service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}***[ mep ]{lang="EN-US"}***[mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_985405407}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1104056270}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_736975218}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x732028241}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_840271490}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x1724182564}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_591446287}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x1113584780}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x805706068}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1862083911}[：显示指定服务实例内的远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_619693550}[：显示指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[所对应的远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1984587360}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1635219022}[显示服务实例]{style="font-family:宋体"}[4]{lang="EN-US"}[内]{style="font-family:宋体"}[MEP 10]{lang="EN-US"}[所对应的远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd remote-mep service-instance 4 mep 10]{lang="EN-US"}]{#struct_0_x1819_23372_x1426136441}

[MEP ID   MAC address      State        Time                  MAC status]{lang="EN-US"}

[20       00e0-fc00-6565   OK           2013/03/06 02:36:38   UP]{lang="EN-US"}

[30       00e0-fc27-6502   OK           2013/03/06 02:36:38   DOWN]{lang="EN-US"}

[40       00e0-fc00-6510   FAILED       2013/03/06 02:36:39   DOWN]{lang="EN-US"}

[50       00e0-fc52-baa0   OK           2013/03/06 02:36:44   DOWN]{lang="PL"}

[60       0010-fc00-6502   OK           2013/03/06 02:36:42   DOWN]{lang="PL"}

[[表1-17 ]{lang="EN-US"}[display cfd remote-mep]{lang="EN-US"}]{#struct_0_x1819_23372_98848677}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_262988365}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_179422838}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_507950094}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_1284514924}

[[远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1635153486}[的编号]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1819_23372_x1904787069}

[[远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1352335503}[所在设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1819_23372_1874322424}

[[远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1429004702}[的运行状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OK]{lang="EN-US"}]{#struct_0_x1819_23372_110601621}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAILED]{lang="EN-US"}]{#struct_0_x1819_23372_1587940639}

[[Time]{lang="EN-US"}]{#struct_0_x1819_23372_x1635087950}

[[远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1216378169}[最后进入]{style="font-family:宋体"}[FAILED]{lang="EN-US"}[或]{style="font-family:宋体"}[OK]{lang="EN-US"}[状态的时间（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）]{style="font-family:宋体"}

[[MAC status]{lang="EN-US"}]{#struct_0_x1819_23372_1845028290}

[[最后一次收到的远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1439164581}[发送的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文中表示该]{style="font-family:宋体"}[MEP]{lang="EN-US"}[所在接口的状态（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示不支持本字段）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1819_23372_1246446216}[：表示已准备好传输报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1819_23372_x1635022414}[：表示无法传输报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TESTING]{lang="EN-US"}]{#struct_0_x1819_23372_x257226716}[：表示处于测试模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNKNOWN]{lang="EN-US"}]{#struct_0_x1819_23372_x1036175804}[：表示状态无法确认]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DORMANT]{lang="EN-US"}]{#struct_0_x1819_23372_17215482}[：表示处于休眠中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOT-PRESENT]{lang="EN-US"}]{#struct_0_x1819_23372_272746744}[：表示某些组件不在位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLD]{lang="EN-US"}]{#struct_0_x1819_23372_906867531}[：表示因底层无连接而]{style="font-family:宋体"}[down]{lang="EN-US"}[掉]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1532266292 .myid}
[]{#_Toc404795572}[]{#struct_0_x1819_23372_x1584089032}

**CFD \-- CFD配置命令 \-- display cfd service-instance**

------------------------------------------------------------------------

[**[display cfd service-instance]{lang="EN-US"}**]{#struct_0_x1819_23372_x1634956878}[命令用来显示服务实例的配置信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1427887396}

[**[display cfd service-instance ]{lang="EN-US"}**[\[ *instance-id* \]]{lang="EN-US"}]{#struct_0_x1819_23372_868315583}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1870190627}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x716426010}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_2082323411}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1221397070}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x574584839}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_724030668}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x1596428715}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1634891342}

[*[instance-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1389452593}[：显示指定服务实例的信息，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。如果未指定本参数，将显示所有服务实例的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x2100734130}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x725109480}[显示所有服务实例的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display cfd service-instance]{lang="EN-US"}]{#struct_0_x1819_23372_x1634825806}

[Service instances configured (2 in total):]{lang="EN-US"}

[Service instance 5:]{lang="FR"}

[Maintenance domain: md_5]{lang="FR"}

[Maintenance domain index: 5]{lang="FR"}

[Maintenance association: ma_5]{lang="EN-US"}

[Maintenance association index: 5]{lang="EN-US"}

[Level: 5  VLAN: 5   MIP rule: NONE   CCM interval: 1s   Direction: Inbound]{lang="EN-US"}

[MEP ID: 730  Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Service instance 6:]{lang="EN-US"}

[Maintenance domain: (Without ID)]{lang="EN-US"}

[Maintenance domain index: 6]{lang="FR"}

[Maintenance association: ma_6]{lang="EN-US"}

[Maintenance association index: 6]{lang="EN-US"}

[Level: 6  VLAN: 6   MIP rule: NONE   CCM interval: 1s   Direction: Outbound]{lang="EN-US"}

[MEP ID: 731  Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display cfd service-instance]{lang="EN-US"}]{#struct_0_x1819_23372_218755453}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_256770673}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1700315779}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_2120275899}

[[Service instances configured]{lang="EN-US"}]{#struct_0_x1819_23372_2121124181}

[[系统中配置的服务实例的个数]{style="font-family:宋体"}]{#struct_0_x1819_23372_x618441574}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_585719304}

[[服务实例的编号]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1634760270}

[[Maintenance domain]{lang="FR"}]{#struct_0_x1819_23372_1204532409}

[[该服务实例所在的]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x548914671}[（如果]{style="font-family:宋体"}[MD]{lang="EN-US"}[为无]{style="font-family:宋体"}[MD]{lang="EN-US"}[名称的格式，则该]{style="font-family:宋体"}[MD]{lang="EN-US"}[的名称显示为]{style="font-family:宋体"}[Without ID]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Maintenance domain index]{lang="EN-US"}]{#struct_0_x1819_23372_611991363}

[[该服务实例所在]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x1545172365}[的索引号]{style="font-family:宋体"}

[[Maintenance association:]{lang="FR"}]{#struct_0_x1819_23372_x1858334418}

[[该服务实例所在的]{style="font-family:宋体"}[MA]{lang="EN-US"}]{#struct_0_x1819_23372_x1635743310}

[[Maintenance association index]{lang="EN-US"}]{#struct_0_x1819_23372_1909123713}

[[该服务实例所在]{style="font-family:宋体"}[MA]{lang="EN-US"}]{#struct_0_x1819_23372_775270193}[的索引号]{style="font-family:宋体"}

[[Level]{lang="FR"}]{#struct_0_x1819_23372_x2099079637}

[[MD]{lang="EN-US"}]{#struct_0_x1819_23372_x2092692000}[的级别]{style="font-family:宋体"}

[[VLAN]{lang="FR"}]{#struct_0_x1819_23372_98045060}

[[MA]{lang="EN-US"}]{#struct_0_x1819_23372_x1635677774}[所在的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[MIP rule]{lang="EN-US"}]{#struct_0_x1819_23372_412510274}

[[服务实例上配置的创建]{style="font-family:宋体"}[MIP]{lang="EN-US"}]{#struct_0_x1819_23372_250021806}[的规则]{style="font-family:宋体"}

[[CCM interval]{lang="EN-US"}]{#struct_0_x1819_23372_x689783812}

[[该服务实例内的]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1751986064}[发送]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文的间隔]{style="font-family:宋体"}

[[Direction]{lang="EN-US"}]{#struct_0_x1819_23372_x1178258140}

[[在服务实例上配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1635219021}[的方向]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_139947500}

[[在服务实例上配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_446412282}[的编号]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1819_23372_x1516361824}

[[在服务实例上配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1297007254}[所处的接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#239380082 .myid}
[]{#_Toc404795573}[]{#struct_0_x1819_23372_x1635153485}

**CFD \-- CFD配置命令 \-- display cfd status**

------------------------------------------------------------------------

[**[display cfd status]{lang="EN-US"}**]{#struct_0_x1819_23372_x338703128}[命令用来显示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[和]{style="font-family:宋体"}[AIS]{lang="EN-US"}[的开启状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1997842605}

[**[display cfd status]{lang="EN-US"}**]{#struct_0_x1819_23372_x45614710}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1133560265}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_931861618}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1008602041}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x306890130}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x2072514073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x1635087949}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_705870596}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_405652409}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1335870020}[显示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[的开启状态。]{style="font-family:宋体"}

[[\<Sysname\> display cfd status]{lang="EN-US"}]{#struct_0_x1819_23372_x1716534124}

[CFD is enabled.]{lang="EN-US"}

[AIS is disabled.]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display cfd status]{lang="EN-US"}]{#struct_0_x1819_23372_x1474088992}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_255478193}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1646706333}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1943114461}

[[CFD is enabled]{lang="EN-US"}]{#struct_0_x1819_23372_x1635022413}

[[表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}]{#struct_0_x1819_23372_502288171}[功能处于开启状态]{style="font-family:宋体"}

[[AIS is enabled]{lang="EN-US"}]{#struct_0_x1819_23372_x711917589}

[[表示]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_x711720981}[功能处于开启状态]{style="font-family:宋体"}

[[CFD is disabled]{lang="EN-US"}]{#struct_0_x1819_23372_x190212594}

[[表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}]{#struct_0_x1819_23372_x786940860}[功能处于关闭状态]{style="font-family:宋体"}

[[AIS is disabled]{lang="EN-US"}]{#struct_0_x1819_23372_x711589909}

[[表示]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_x1819_23372_x711655445}[功能处于关闭状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#998675332 .myid}
[]{#_Toc404795574}[]{#struct_0_x1819_23372_x711458837}[]{#_Toc351105924}

**CFD \-- CFD配置命令 \-- display cfd tst**

------------------------------------------------------------------------

[**[display cfd tst]{lang="EN-US"}**]{#struct_0_x1819_23372_x711524373}[命令用来显示比特错误的测试结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1269409006}

[**[display cfd tst]{lang="EN-US"}**[ \[ **service-instance** *instance-id* \[ **mep** *mep-id* \] \]]{lang="EN-US"}]{#struct_0_x1819_23372_x711327765}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x711393301}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x637635446}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x711852056}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x711917592}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_23372_523585443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_23372_x711720984}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_23372_x711786520}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1018709005}

[**[service-instance]{lang="PT-BR"}**]{#struct_0_x1819_23372_x711589912}*[ instance-id]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定服务实例内的测试结果]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[instance-id]{lang="PT-BR"}*[为服务实例的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[32767]{lang="PT-BR"}[。如果未指定本参数，将显示所有服务实例内的测试结果。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x711655448}[：显示指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x276877133}

[[对于内向]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x711458840}[，其所属服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的比特错误测试结果都相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x711524376}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_1269605614}[显示所有服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[上比特错误的测试结果。]{style="font-family:宋体"}

[[\<Sysname\> display cfd tst]{lang="PT-BR"}]{#struct_0_x1819_23372_x711852055}

[Service instance: 1]{lang="PT-BR"}

[MEP ID: 1003]{lang="PT-BR"}

[Sent TST total number: 0]{lang="PT-BR"}

[Received TST total number: 5]{lang="PT-BR"}

[Received from 0010-fc00-6510, Bit True,  sequence number 0]{lang="PT-BR"}

[Received from 0010-fc00-6510, Bit True,  sequence number 1]{lang="PT-BR"}

[Received from 0010-fc00-6510, Bit True,  sequence number 2]{lang="PT-BR"}

[Received from 0010-fc00-6510, Bit True,  sequence number 3]{lang="PT-BR"}

[Received from 0010-fc00-6510, Bit True,  sequence number 4]{lang="PT-BR"}

[MEP ID: 1004]{lang="PT-BR"}

[Sent TST total number: 5]{lang="PT-BR"}

[Received TST total number: 0]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Service instance: 2]{lang="PT-BR"}

[No MEP exists in the service instance.]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[Service instance: 3]{lang="PT-BR"}

[MEP ID: 1023]{lang="PT-BR"}

[Sent TST total number: 5]{lang="PT-BR"}

[Received TST total number: 0]{lang="PT-BR"}

[[表1-20 ]{lang="EN-US"}[display cfd tst]{lang="EN-US"}]{#struct_0_x1819_23372_x711917591}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1077727940}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_23372_x711720983}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_23372_x711786519}

[[Service instance]{lang="EN-US"}]{#struct_0_x1819_23372_x711655447}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x711458839}[所在的服务实例]{style="font-family:宋体"}

[[MEP ID]{lang="EN-US"}]{#struct_0_x1819_23372_x711524375}

[[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x711327767}[的编号]{style="font-family:宋体"}

[[Sent TST total number]{lang="EN-US"}]{#struct_0_x1819_23372_x711852058}

[[发送的]{style="font-family:宋体"}[TST]{lang="EN-US"}]{#struct_0_x1819_23372_x711917594}[报文总数]{style="font-family:宋体"}

[[Received TST total number]{lang="EN-US"}]{#struct_0_x1819_23372_x711786522}

[[收到的]{style="font-family:宋体"}[TST]{lang="EN-US"}]{#struct_0_x1819_23372_x711589914}[报文总数]{style="font-family:宋体"}

[[Received from 0010-fc00-6510, Bit True,  sequence number 0]{lang="PT-BR"}]{#struct_0_x1819_23372_x711655450}

[[从]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1819_23372_x711524378}[地址为]{style="font-family:宋体"}[0010-FC00-6510]{lang="EN-US"}[的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[收到的序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[TST]{lang="EN-US"}[报文：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bit True]{lang="EN-US"}]{#struct_0_x1819_23372_x711327770}[：表示没有发生比特错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bit False]{lang="EN-US"}]{#struct_0_x1819_23372_x711852057}[：表示发生了比特错误]{lang="EN-US" style="font-family:宋体"}

[[No MEP exists in the service instance]{lang="PT-BR"}]{#struct_0_x1819_23372_x711917593}

[[本服务实例内没有]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x711720985}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x711786521}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_x711589913}**[tst]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_x711655449}**[tst]{lang="EN-US"}**

::: {#1723820741 .myid}
[]{#_Toc404795575}[]{#struct_0_x1819_23372_x711458841}[]{#_Toc351105925}

**CFD \-- CFD配置命令 \-- reset cfd dm one-way history**

------------------------------------------------------------------------

[**[reset cfd dm one-way history]{lang="EN-US"}**]{#struct_0_x1819_23372_x711524377}[命令用来清除单向时延的测试结果。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_1269671150}

[**[reset cfd dm one-way history]{lang="EN-US"}**[ \[ **service-instance** *instance-id* \[ **mep** *mep-id* \] \]]{lang="EN-US"}]{#struct_0_x1819_23372_x711327769}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x711393305}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_854231887}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_854166351}

[[network-admin]{lang="PT-BR"}]{#struct_0_x1819_23372_854362959}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x1819_23372_x1874520398}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874585934}

[**[service-instance]{lang="PT-BR"}**]{#struct_0_x1819_23372_1018724249}*[ instance-id]{lang="PT-BR"}*[：]{style="font-family:宋体"}[清除指定服务实例内的测试结果]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[instance-id]{lang="PT-BR"}*[为服务实例的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[32767]{lang="PT-BR"}[。如果未指定本参数，将清除所有服务实例内的测试结果。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1874389326}[：清除指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874454862}

[[清除某内向]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_x1874258254}[的单向时延测试结果，将会清除其所属服务实例内的所有单向时延测试结果。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874323790}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1874127182}[清除所有服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[上单向时延的测试结果。]{style="font-family:宋体"}

[[\<Sysname\> reset cfd dm one-way history]{lang="PT-BR"}]{#struct_0_x1819_23372_x1874192718}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_316397590}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_x1874651469}**[dm one-way]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cfd dm one-way history]{lang="EN-US"}**]{#struct_0_x1819_23372_x1874717005}
:::

::: {#-2021413500 .myid}
[]{#_Toc404795576}[]{#struct_0_x1819_23372_x1874520397}[]{#_Toc351105926}

**CFD \-- CFD配置命令 \-- reset cfd tst**

------------------------------------------------------------------------

[**[reset cfd tst]{lang="EN-US"}**]{#struct_0_x1819_23372_x900592314}[命令用来清除比特错误的测试结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874389325}

[**[reset cfd tst]{lang="EN-US"}**[ \[ **service-instance** *instance-id* \[ **mep** *mep-id* \] \]]{lang="EN-US"}]{#struct_0_x1819_23372_x2141260754}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874454861}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1819_23372_x1874258253}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874323789}

[[network-admin]{lang="PT-BR"}]{#struct_0_x1819_23372_x1874127181}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x1819_23372_x1874192717}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1962147071}

[**[service-instance]{lang="PT-BR"}**]{#struct_0_x1819_23372_x1874651472}*[ instance-id]{lang="PT-BR"}*[：]{style="font-family:宋体"}[清除指定服务实例内的测试结果]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[instance-id]{lang="PT-BR"}*[为服务实例的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[32767]{lang="PT-BR"}[。如果未指定本参数，将清除所有服务实例内的测试结果。]{style="font-family:宋体"}

[**[mep]{lang="EN-US"}***[ mep-id]{lang="EN-US"}*]{#struct_0_x1819_23372_x1874717008}[：清除指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的测试结果。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874520400}

[[清除某内向]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_x1819_23372_1827832292}[的比特错误测试结果，将会清除其所属服务实例内的所有比特错误测试结果。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x1874585936}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_23372_x1874389328}[清除所有服务实例内所有]{style="font-family:宋体"}[MEP]{lang="EN-US"}[上比特错误的测试结果。]{style="font-family:宋体"}

[[\<Sysname\> reset cfd tst]{lang="PT-BR"}]{#struct_0_x1819_23372_x1874454864}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1819_23372_x567946735}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cfd ]{lang="EN-US"}**]{#struct_0_x1819_23372_x1874258256}**[tst]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cfd tst]{lang="EN-US"}**]{#struct_0_x1819_23372_x1874323792}

[ ]{lang="EN-US"}
:::
