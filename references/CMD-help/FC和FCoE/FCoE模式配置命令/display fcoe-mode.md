::: {#1453780028 .myid}
[]{#_Toc329882967}[]{#_Toc329608898}[]{#_Toc404798049}[]{#struct_0_x9962_12256_x302987258}

**FC和FCoE \-- FCoE模式配置命令 \-- display fcoe-mode**

------------------------------------------------------------------------

[**[display fcoe-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x667922539}[命令用来显示交换机的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2125925087}

[**[display fcoe-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_689555517}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1912498131}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1931440190}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x799337314}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1327340157}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1923009536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_60385752}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_332971373}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2124445359}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1086433117}[显示交换机的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> display fcoe-mode]{lang="EN-US"}]{#struct_0_x9962_12256_x1879244206}

[The FCoE mode is NONE.]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display fcoe-mode]{lang="EN-US"}]{#struct_0_x9962_12256_1273628667}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_799621653}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_851087335}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1086433118}

[[The FCoE mode is *mode*.]{lang="EN-US"}]{#struct_0_x9962_12256_x1879965102}

[[交换机的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x9962_12256_1661859848}[模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*[，]{style="font-family:宋体"}*[mode]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x187227510}[：]{lang="EN-US" style="font-family:宋体"}[FCF]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x115957224}[：]{lang="EN-US" style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_669271963}[：]{lang="EN-US" style="font-family:宋体"}[NPV]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TRANSIT]{lang="EN-US"}]{#struct_0_x9962_12256_x316137296}[：]{lang="EN-US" style="font-family:宋体"}[Transit]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_x9962_12256_14763694}[：]{lang="EN-US" style="font-family:宋体"}[非]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1931571262}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x801005609}

::: {#-326868841 .myid}
[]{#_Toc404798050}[]{#struct_0_x9962_12256_1111635845}

**FC和FCoE \-- FCoE模式配置命令 \-- fcoe-mode**

------------------------------------------------------------------------

[**[fcoe-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x601726288}[命令用来配置交换机的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[undo fcoe-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1360321218}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_597805195}

[**[fcoe-mode]{lang="EN-US"}**[ { **fcf** \| **fcf-npv** \| **npv** \| **transit** }]{lang="EN-US"}]{#struct_0_x9962_12256_x1564889245}

[**[undo fcoe-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1083216128}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1931505726}

[[交换机工作在非]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x9962_12256_x1934504593}[模式下。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x564940482}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x578936400}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x755581307}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_502431182}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_798156432}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1931702334}

[**[fcf]{lang="PT-BR"}**]{#struct_0_x9962_12256_752614899}[：]{style="font-family:宋体"}[FCF]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[fcf-npv]{lang="PT-BR"}**]{#struct_0_x9962_12256_1086433124}[：]{style="font-family:宋体"}[FCF-NPV]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[npv]{lang="SV"}**]{#struct_0_x9962_12256_651345689}[：]{style="font-family:宋体"}[NPV]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[transit]{lang="SV"}**]{#struct_0_x9962_12256_951832552}[：]{style="font-family:宋体"}[Transit]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1458405090}

[[一台具备]{style="font-family:宋体"}]{#struct_0_x9962_12256_1080635678}[FC]{lang="PT-BR"}[和]{style="font-family:宋体"}[FCoE]{lang="PT-BR"}[能力的交换机]{style="font-family:宋体"}[，]{style="font-family:宋体"}[既可工作在非]{style="font-family:宋体"}[FCoE]{lang="PT-BR"}[模式下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可工作在]{style="font-family:宋体"}[FCoE]{lang="PT-BR"}[模式下。其中，]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式又分为以下四种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1614396976}[模式：工作在本模式的交换机称为]{lang="EN-US" style="font-family:
宋体"}[FCF]{lang="EN-US"}[交换机，其]{lang="EN-US" style="font-family:宋体"}[接]{style="font-family:宋体"}[口支持]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[模式和]{lang="EN-US" style="font-family:宋体"}[F]{lang="EN-US"}[模式，分别称为]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机可通过]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="EN-US"}[连接其它交换机的]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[或者通过]{style="font-family:宋体"}[F_Port]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[节]{style="font-family:宋体"}[点设备的]{lang="EN-US" style="font-family:宋体"}[N_Port]{lang="EN-US"}[或其它]{style="font-family:宋体"}[交换机的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1474630018}[模式：工作在本模式的交换机称为]{lang="EN-US" style="font-family:
宋体"}[NPV]{lang="EN-US"}[交换机，其]{lang="EN-US" style="font-family:宋体"}[接]{style="font-family:宋体"}[口支持]{lang="EN-US" style="font-family:宋体"}[F]{lang="EN-US"}[模式和]{lang="EN-US" style="font-family:宋体"}[NP]{lang="EN-US"}[模式，分别称为]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机]{style="font-family:宋体"}[可通过]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="EN-US"}[连接节点设备的]{lang="EN-US" style="font-family:宋体"}[N_Port]{lang="EN-US"}[或]{style="font-family:宋体"}[其它交换机的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="EN-US"}[，或]{lang="EN-US" style="font-family:宋体"}[着通过]{style="font-family:宋体"}[NP_Port]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[其它]{style="font-family:宋体"}[交换机的]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1086433121}[模式：工作在本模式的交换机称为]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机。]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中的工作模式又可分为两种：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1879375275}[模式：在本模式下，]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机的工作机制和连接方式与]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机相同。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1421430235}[模式：在本模式下，]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机的工作机制和连接方式与]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_1931636798}[模式：工作在本模式的交换机称为]{lang="EN-US" style="font-family:宋体"}[Transit]{lang="EN-US"}[交换机，其以太]{lang="EN-US" style="font-family:宋体"}[网接]{style="font-family:宋体"}[口可工作]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[ENode]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}[或]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}[Transit]{lang="EN-US"}[交换机可通过将以太网接口配置为]{style="font-family:宋体"}[ENode]{lang="EN-US"}[模式或]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式，以限制该接口只能接收来自]{style="font-family:宋体"}[ENode]{lang="EN-US"}[或]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的流量。]{style="font-family:宋体"}

[[需要注意的是，交换机可以在非]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x9962_12256_212138802}[模式和]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式之间直接切换，但不能在四种]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式之间直接切换。当需要在四种]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式之间切换时，必须先将交换机切换至非]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式。当交换机从]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式切换至非]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式后，原]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式下的所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[和]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[相关配置将被清空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_82234262}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1727775822}[配置交换机工作在]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1931178043}

[\[Sysname\] fcoe-mode fcf]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1901705688}[当前交换机工作在]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式，修改其工作模式为]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_901933704}

[\[Sysname\] undo fcoe-mode]{lang="EN-US"}

[\[Sysname\] fcoe-mode npv]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1372559335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fcoe-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x534832400}
:::

::: {#-1188281503 .myid}
[]{#_Toc404798052}[]{#struct_0_x9962_12256_1991968815}

**FC和FCoE \-- FC接口配置命令 \-- bandwidth (FC interface view)**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_x1802128721}[命令用来配置当前接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_606708241}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_572596094}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x9962_12256_264643024}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_606773777}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1373739654}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x9962_12256_x1958859957}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1776244382}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_606577169}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x505894446}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x947534771}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_606642705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1325753861}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x9962_12256_x1791127210}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1032315585}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_606446097}[接口的期望带宽会影响]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[Cost]{lang="EN-US"}[值的计算，从而影响路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x63687222}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_606511633}[配置]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_606315025}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] bandwidth 50]{lang="EN-US"}
:::

::: {#-74294282 .myid}
[]{#_Toc404798053}[]{#struct_0_x9962_12256_x732613143}

**FC和FCoE \-- FC接口配置命令 \-- default (FC interface view)**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_871978867}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606380561}

[**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_798064215}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x830180469}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_606183953}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1344403691}

[[network-admin]{lang="FR"}]{#struct_0_x9962_12256_x1973343611}

[[mdc-admin]{lang="FR"}]{#struct_0_x9962_12256_1617670663}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606249489}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x346683336}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_x684090126}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606708240}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_572596093}[将]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_606577168}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] default]{lang="EN-US"}
:::

::: {#-1254685192 .myid}
[]{#_Toc404798054}[]{#struct_0_x9962_12256_x505894445}

**FC和FCoE \-- FC接口配置命令 \-- description (FC interface view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x9962_12256_606642704}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x9962_12256_1325753860}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1791061674}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x9962_12256_x1783066827}

[**[undo description]{lang="EN-US"}**]{#struct_0_x9962_12256_606446096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x63687223}

[[接口的描述信息为]{style="font-family:宋体"}]{#struct_0_x9962_12256_606511632}["]{style="font-family:宋体"}*[接口名]{style="font-family:宋体"}*[ Interface]{lang="FR"}["，]{style="font-family:宋体"}[例如]{style="font-family:宋体"}[：]{style="font-family:宋体"}[Fc1/0/1 Interface]{lang="FR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1458237830}

[[FC]{lang="FR"}]{#struct_0_x9962_12256_910488851}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606315024}

[[network-admin]{lang="FR"}]{#struct_0_x9962_12256_x732613142}

[[mdc-admin]{lang="FR"}]{#struct_0_x9962_12256_872044403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606380560}

[*[text]{lang="FR"}*]{#struct_0_x9962_12256_798064214}[：]{style="font-family:宋体"}[表示接口描述信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[255]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x830180468}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_606183952}[配置]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的描述信息为]{style="font-family:宋体"}[FCport1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_606708239}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] description FCport1]{lang="EN-US"}
:::

::: {#51893516 .myid}
[]{#_Toc404798055}[]{#struct_0_x9962_12256_x1383719034}

**FC和FCoE \-- FC接口配置命令 \-- display interface fc**

------------------------------------------------------------------------

[**[display interface fc]{lang="EN-US"}**]{#struct_0_x9962_12256_1720058332}[命令用来显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606773775}

[**[display interface]{lang="EN-US"}**[ \[ **fc** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_1173307925}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606577167}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x505894440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606642703}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1325753859}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1791651499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_389740551}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_606446095}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x63687224}

[**[fc]{lang="EN-US"}**]{#struct_0_x9962_12256_x1252219041}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的信息。如果未指定本参数，将显示设备支持的所有接口的信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_606511631}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}[如果未指定本参数，将显示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x9962_12256_1458237831}[：显示概要信息。如果未指定本参数，将显示详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x9962_12256_606315023}[：当用户配置的接口描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不会显示。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x9962_12256_x732613149}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果未指定本参数，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_606183951}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_606249487}[显示]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface fc 1/0/1]{lang="EN-US"}]{#struct_0_x9962_12256_606642702}

[Fc1/0/1]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Fc1/0/1 Interface]{lang="EN-US"}

[Bandwidth: 4000000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 2112]{lang="EN-US"}

[4000Mbps-speed mode]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol is FC]{lang="EN-US"}

[Fill word is idle-idle]{lang="EN-US"}

[Port WWN is 66:66:66:62:65:34:30:39]{lang="EN-US"}

[FC mode is Auto, state is E]{lang="EN-US"}

[Transmit B2B Credit is 64]{lang="EN-US"}

[Receive B2B Credit is 64]{lang="EN-US"}

[Support the VSAN protocol]{lang="EN-US"}

[VSAN tagging mode is Non tagging]{lang="EN-US"}

[EVFP common VSAN : 1]{lang="EN-US"}

[Last link flapping: 1 hours 12 minutes 25 seconds]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display interface fc]{lang="EN-US"}]{#struct_0_x9962_12256_1325753858}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1967922749}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_606446094}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x63687225}

[[Current state]{lang="EN-US"}]{#struct_0_x9962_12256_606511630}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_606315022}[接口的物理层状态和管理状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_606380558}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1158250930}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_606183950}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x9962_12256_606249486}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009992770}[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1010058306}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_x1234195971}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x9962_12256_1009861698}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009927234}[接口的描述信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x9962_12256_1614971027}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009730626}[接口的期望带宽]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x9962_12256_1009796162}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009599554}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}

[[4000Mbps-speed mode]{lang="EN-US"}]{#struct_0_x9962_12256_1009665090}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1908446538}[接口的速率]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x9962_12256_1009468482}

[[对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9962_12256_1009534018}[报文的处理能力，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示没有为该接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_x9962_12256_1009992769}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1010058305}[接口的链路层协议类型]{style="font-family:宋体"}

[[Fill word]{lang="EN-US"}]{#struct_0_x9962_12256_x879674464}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_686409477}[接口的]{style="font-family:宋体"}[Fill Word]{lang="EN-US"}[模式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[idle-idle]{lang="EN-US"}]{#struct_0_x9962_12256_412813490}[：]{lang="EN-US" style="font-family:宋体"}[idle-idle]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[idle-arbff]{lang="EN-US"}]{#struct_0_x9962_12256_1905282064}[：]{lang="EN-US" style="font-family:宋体"}[idle-arbff]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1234261507}

[[接口]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1009861697}

[[FC mode]{lang="EN-US"}]{#struct_0_x9962_12256_1009927233}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009730625}[接口的配置模式]{style="font-family:宋体"}

[[state]{lang="EN-US"}]{#struct_0_x9962_12256_1251615627}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009796161}[接口的协商运行状态]{style="font-family:宋体"}

[[Transmit B2B Credit]{lang="EN-US"}]{#struct_0_x9962_12256_1009599553}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009665089}[接口本端的]{style="font-family:宋体"}[BB_Credit]{lang="EN-US"}[值，此信息只有接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}[后才显示]{style="font-family:宋体"}

[[Receive B2B Credit]{lang="EN-US"}]{#struct_0_x9962_12256_1009468481}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1218496582}[接口对端的]{style="font-family:宋体"}[BB_Credit]{lang="EN-US"}[值，此信息只有接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}[后才显示]{style="font-family:宋体"}

[[Support the VSAN protocol]{lang="EN-US"}]{#struct_0_x9962_12256_1009534017}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1009992768}[接口支持]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[协议，经过协商后确定接口支持]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[协议且接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}[后才显示该信息]{style="font-family:宋体"}

[[VSAN tagging mode]{lang="EN-US"}]{#struct_0_x9962_12256_1010058304}

[[经过]{style="font-family:宋体"}[EVFP]{lang="EN-US"}]{#struct_0_x9962_12256_x1234327043}[协商后确定端口的连接方式是]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[（]{style="font-family:宋体"}[Tagging]{lang="EN-US"}[）或]{style="font-family:宋体"}[Access]{lang="EN-US"}[（]{style="font-family:宋体"}[Non tagging]{lang="EN-US"}[），此信息只有接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}[后才显示]{style="font-family:宋体"}

[[EVFP common VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1009861696}

[[经过协商后确定端口连接并]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x9962_12256_1009927232}[的公共]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，此信息只有接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}[后才显示]{style="font-family:宋体"}

[[Last link flapping]{lang="EN-US"}]{#struct_0_x9962_12256_x1252219042}

[[接口最近一次物理状态改变到现在的时长。]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x9962_12256_x1292224205}[表示接口从设备启动后一直处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态（没有改变过）]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x9962_12256_1849208891}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x9962_12256_x838670105}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1009730624}[显示]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface fc 1/0/1 brief]{lang="EN-US"}]{#struct_0_x9962_12256_1009665088}

[Brief information on FC interface(s):]{lang="EN-US"}

[Admin Mode: auto - auto; E - e port; F - f port; NP - n port proxy]{lang="EN-US"}

[Oper Mode: E - e port; F - f port; NP - n port proxy;]{lang="EN-US"}

[           TE - trunking e port; TF - trunking f port;]{lang="EN-US"}

[           TNP - trunking n port proxy]{lang="EN-US"}

[Interface  VSAN Admin Admin Oper Oper   Status SAN-Aggregation]{lang="EN-US"}

[                Mode  Trunk Mode Speed]{lang="EN-US"}

[                      Mode]{lang="EN-US"}

[Fc1/0/1    2    auto  off   E    4G     UP     SAGG23]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display interface fc brief]{lang="EN-US"}]{#struct_0_x9962_12256_1089694004}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2012080011}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2089727588}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1639189351}

[[Brief information on FC interface(s)]{lang="EN-US"}]{#struct_0_x9962_12256_1682118310}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x83897735}[接口的概要信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x2042473878}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1920124990}[接口的名称]{style="font-family:宋体"}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x476389937}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1870468946}[接口的]{style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}

[[Admin Mode]{lang="EN-US"}]{#struct_0_x9962_12256_x2033333983}

[[配置的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x523444104}[接口的模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x9962_12256_x631623957}[：表示]{lang="EN-US" style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_1042639837}[：表示]{lang="EN-US" style="font-family:宋体"}[E]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_707288324}[：表示]{lang="EN-US" style="font-family:宋体"}[F]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_x1024880344}[：表示]{lang="EN-US" style="font-family:宋体"}[NP]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Admin Trunk Mode]{lang="EN-US"}]{#struct_0_x9962_12256_x879740000}

[[配置的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1709112670}[接口的]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x9962_12256_686343941}[：表示]{lang="EN-US" style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[on]{lang="EN-US"}]{#struct_0_x9962_12256_x1001847417}[：表示]{lang="EN-US" style="font-family:宋体"}[On]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[off]{lang="EN-US"}]{#struct_0_x9962_12256_466093311}[：表示]{lang="EN-US" style="font-family:宋体"}[Off]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Oper Mode]{lang="EN-US"}]{#struct_0_x9962_12256_283059414}

[[链路层协商后，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1007302229}[接口的运行模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_x503825703}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_1849143355}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_1173671713}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_1089628468}[E]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_x1226517934}[F]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_x2707783}[NP]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[\--]{lang="EN-US"}]{#struct_0_x9962_12256_x1639254887}[：表示未发起协商或协商失败]{style="font-family:宋体"}

[[Oper Speed]{lang="EN-US"}]{#struct_0_x9962_12256_x102451546}

[[物理层协商后，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x2042539414}[接口的速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[。未发起协商或协商失败时，将显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x9962_12256_1771694662}

[[链路层协商后，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_2011629354}[接口的状态：]{style="font-family:宋体"}[UP]{lang="EN-US"}[或]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[SAN-Aggregation]{lang="EN-US"}]{#struct_0_x9962_12256_x476455473}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_797597781}[接口所属的]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组，当]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口没有加入任何]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组时，将显示为空]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_743596914}[显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的描述信息。]{style="font-family:宋体"}

[[\<sysname\> display interface fc brief description]{lang="EN-US"}]{#struct_0_x9962_12256_x523509640}

[Brief information on FC interface(s):]{lang="EN-US"}

[Interface    Description ]{lang="EN-US"}

[Fc1/0/2      Fc1/0/2 Interface]{lang="EN-US"}

[Fc1/0/3      Fc1/0/3 Interface]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display interface fc brief description]{lang="EN-US"}]{#struct_0_x9962_12256_x1098769745}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1989001887}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1028679683}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1798288103}

[[Brief information on FC interface(s)]{lang="EN-US"}]{#struct_0_x9962_12256_1042574301}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x461868857}[接口的概要信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1520139499}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x879805536}[接口的名称]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x9962_12256_x914071339}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_686278405}[接口的描述信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1907922249}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface fc brief down]{lang="EN-US"}]{#struct_0_x9962_12256_1009534016}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Fc1/0/1              ADM  Administratively]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display interface fc brief down]{lang="EN-US"}]{#struct_0_x9962_12256_x335612492}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1954972833}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1009992767}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1010058303}

[[Brief information on interface(s) under bridge mode]{lang="EN-US"}]{#struct_0_x9962_12256_x1234392579}

[[二层模式下（]{style="font-family:宋体"}[bridge]{lang="EN-US"}]{#struct_0_x9962_12256_1009861695}[）的接口概要信息，即二层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x9962_12256_1009927231}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x9962_12256_1009730623}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x9962_12256_1009796159}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1009861694}

[[接口名称]{style="font-family:宋体"}]{#struct_0_x9962_12256_1009927230}

[[Link]{lang="EN-US"}]{#struct_0_x9962_12256_1009730622}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1009796158}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_1009599550}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1009665086}[：表示接口物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x9962_12256_1009468478}[：表示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x9962_12256_1009534014}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x9962_12256_x556484387}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x9962_12256_x556418851}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1252219039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x9962_12256_x1244711286}**[ fc]{lang="EN-US"}**

::: {#-644779440 .myid}
[]{#_Toc404798056}[]{#struct_0_x9962_12256_x677603483}

**FC和FCoE \-- FC接口配置命令 \-- fc mode (FC interface view)**

------------------------------------------------------------------------

[**[fc mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x556615459}[命令用来配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的模式。]{style="font-family:宋体"}

[**[undo fc mode]{lang="EN-US"}**]{#struct_0_x9962_12256_501197768}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x556549923}

[**[fc mode]{lang="FR"}**]{#struct_0_x9962_12256_x1052826968}[ { **auto** \| **e** \| **f** ]{lang="FR"}[\| **np**]{lang="EN-US"}[ }]{lang="FR"}

[**[undo fc mode]{lang="FR"}**]{#struct_0_x9962_12256_x1532975259}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x556091172}

[[FCF]{lang="FR"}]{#struct_0_x9962_12256_90275080}[交换机缺省为]{style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[NPV]{lang="FR"}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="FR"}[交换机]{style="font-family:宋体"}[缺省]{style="font-family:宋体"}[为]{style="font-family:宋体"}[F]{lang="FR"}[模式。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_894151328}

[[FC]{lang="FR"}]{#struct_0_x9962_12256_x556222244}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x273938260}

[[network-admin]{lang="FR"}]{#struct_0_x9962_12256_84303366}

[[mdc-admin]{lang="FR"}]{#struct_0_x9962_12256_x556156708}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x556353316}

[**[auto]{lang="PT-BR"}**]{#struct_0_x9962_12256_x666069899}[：]{style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式，可以通过动态协商转化为]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式或]{style="font-family:宋体"}[E]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[e]{lang="PT-BR"}**]{#struct_0_x9962_12256_x556287780}[：]{style="font-family:宋体"}[E]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[f]{lang="SV"}**]{#struct_0_x9962_12256_2041692577}[：]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式。]{style="font-family:
宋体"}

[**[np]{lang="SV"}**]{#struct_0_x9962_12256_x556484388}[：]{style="font-family:宋体"}[NP]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_873209892}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1252219033}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_274318488}[交换机只支持]{lang="EN-US" style="font-family:
宋体"}[Auto]{lang="PT-BR"}[模式、]{lang="EN-US" style="font-family:
宋体"}[E]{lang="PT-BR"}[模式和]{lang="EN-US" style="font-family:
宋体"}[F]{lang="PT-BR"}[模式；]{lang="EN-US" style="font-family:
宋体"}[NPV]{lang="FR"}[交换机只支持]{lang="EN-US" style="font-family:宋体"}[F]{lang="PT-BR"}[模式和]{lang="EN-US" style="font-family:宋体"}[NP]{lang="EN-US"}[模式]{style="font-family:宋体"}[；]{lang="EN-US" style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机只支持]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[模式、]{lang="EN-US" style="font-family:宋体"}[F]{lang="PT-BR"}[模式和]{lang="EN-US" style="font-family:宋体"}[NP]{lang="EN-US"}[模式]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x9962_12256_x242129777}[FCF-NPV]{lang="EN-US"}[交换机上，如果用户配置的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口模式与该接口所属的某个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的工作模式不匹配，则]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口模式的配置在该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下将不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_90209544}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x556222245}[配置]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口工作在]{style="font-family:宋体"}[E]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x556353317}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] fc mode e]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x234214855}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1307316096}
:::

::: {#-1626749328 .myid}
[]{#_Toc404798057}[]{#struct_0_x9962_12256_x556287781}

**FC和FCoE \-- FC接口配置命令 \-- fcb2bcredit**

------------------------------------------------------------------------

[**[fcb2bcredit]{lang="FR"}**]{#struct_0_x9962_12256_2041758113}[命令用来配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[BB_Credit]{lang="EN-US"}[（]{style="font-family:宋体"}[Buffer-to-Buffer Credit]{lang="EN-US"}[，缓冲区到缓冲区信用数）值。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x9962_12256_x556484389}**[fcb2bcredit]{lang="FR"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_873275428}

[**[fcb2bcredit]{lang="FR"}**]{#struct_0_x9962_12256_x556418853}**[ ]{lang="FR"}***[credit-value]{lang="EN-US"}*

[**[undo ]{lang="EN-US"}**]{#struct_0_x9962_12256_x556615461}**[fcb2bcredit]{lang="FR"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_500673477}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x556549925}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1052433752}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x556091174}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_89881864}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x556025638}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_893233824}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x556222246}

[*[credit-value]{lang="EN-US"}*]{#struct_0_x9962_12256_x273807188}[：表示接口连续接收报文的个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x556156710}

[[BB_Credit]{lang="EN-US"}]{#struct_0_x9962_12256_501495394}[是一种流量控制机制，用来保证]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口不丢弃报文。通常情况下，用户不需要修改]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[BB_Credit]{lang="EN-US"}[值，采用缺省值即可。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2041561505}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x556418854}[配置]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[BB_Credit]{lang="EN-US"}[值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x556091175}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] fcb2bcredit 10]{lang="EN-US"}
:::

::: {#763064553 .myid}
[]{#_Toc404798058}[]{#struct_0_x9962_12256_282928342}[]{#_Toc369704879}[]{#_Toc362427984}

**FC和FCoE \-- FC接口配置命令 \-- fill-word**

------------------------------------------------------------------------

[**[fill-word]{lang="EN-US"}**]{#struct_0_x9962_12256_705594604}[命令用来配置]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}[速率的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[Fill Word]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[undo fill-word]{lang="EN-US"}**]{#struct_0_x9962_12256_x1986768690}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1421499728}

[**[fill-word]{lang="EN-US"}**[ { **idle-arbff** *\|* **idle-idle** }]{lang="EN-US"}]{#struct_0_x9962_12256_1849012283}

[**[undo fill-word]{lang="EN-US"}**]{#struct_0_x9962_12256_796875416}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_656280551}

[[8Gbps]{lang="EN-US"}]{#struct_0_x9962_12256_710442580}[速率的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[Fill Word]{lang="EN-US"}[模式为]{style="font-family:宋体"}[idle-arbff]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x988327801}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_531341914}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1036133606}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_854231447}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x138179754}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_475861578}

[**[idle-arbff]{lang="EN-US"}**]{#struct_0_x9962_12256_1089497396}[：]{style="font-family:宋体"}[idle-arbff]{lang="EN-US"}[模式，表示接口链路初始化阶段用]{style="font-family:宋体"}[idle]{lang="EN-US"}[原语信号，并且将]{style="font-family:宋体"}[ARBff]{lang="EN-US"}[原语信号作为]{style="font-family:宋体"}[Fill Word]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[idle-idle]{lang="EN-US"}**]{#struct_0_x9962_12256_1815139526}[：]{style="font-family:宋体"}[idle-idle]{lang="EN-US"}[模式，表示接口链路初始化阶段用]{style="font-family:宋体"}[idle]{lang="EN-US"}[原语信号，并且]{style="font-family:宋体"}[idle]{lang="EN-US"}[原语信号作为]{style="font-family:宋体"}[Fill Word]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1370933951}

[[本命令只用于]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}]{#struct_0_x9962_12256_x229126936}[速率的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口。]{style="font-family:宋体"}[2Gbps]{lang="EN-US"}[或]{style="font-family:宋体"}[4Gbps]{lang="EN-US"}[速率的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口仅支持]{style="font-family:宋体"}[idle-idle]{lang="EN-US"}[模式，即使配置了本命令也不生效。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}]{#struct_0_x9962_12256_x752740450}[速率的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口出现互通问题时，可以使用本命令调整]{style="font-family:宋体"}[Fill Word]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[配置本命令后，需要执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[/**undo shutdown**]{lang="EN-US"}]{#struct_0_x9962_12256_x949685586}[命令重启该]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口后才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1321618489}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_904725599}[配置]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}[速率的]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[Fill Word]{lang="EN-US"}[模式为]{style="font-family:宋体"}[idle-idle]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_61604822}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] speed 8000]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] fill-word idle-idle]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1639385959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[speed]{lang="EN-US"}**]{#struct_0_x9962_12256_435993480}
:::

::: {#-65933115 .myid}
[]{#_Toc404798059}[]{#struct_0_x9962_12256_89816328}

**FC和FCoE \-- FC接口配置命令 \-- interface fc**

------------------------------------------------------------------------

[**[interface fc]{lang="EN-US"}**]{#struct_0_x9962_12256_x556025639}[命令用来进入]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_893299360}

[**[interface fc ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x556222247}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x273741652}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x556156711}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_501429858}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x556353319}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x667052939}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x556287783}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_2041627041}[：表示]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x556484391}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x556615463}[进入]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x556025640}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\]]{lang="EN-US"}
:::

::::: {#1446084098 .myid}
[]{#_Toc404798060}[]{#struct_0_x9962_12256_203358180}

**FC和FCoE \-- FC接口配置命令 \-- port-type**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](FC和FCoE命令.files/image001.png){#图片 19 width="63" height="26"}]{lang="EN-US"}]{#struct_0_x9962_12256_1544262690}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x9962_12256_203161572}
:::

**[ ]{lang="EN-US"}**

[**[port-type]{lang="EN-US"}**]{#struct_0_x9962_12256_2073674195}[命令用来在二层以太网接口和]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口间进行类型切换。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_203227108}

[[在二层以太网接口视图下：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1998875707}

[**[port-type]{lang="EN-US"}**[ **fc**]{lang="EN-US"}]{#struct_0_x9962_12256_203030500}

[[在]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_203096036}[接口视图下：]{style="font-family:宋体"}

[**[port-type]{lang="EN-US"}**[ **ethernet**]{lang="EN-US"}]{#struct_0_x9962_12256_x1878587573}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_202899428}

[[接口为二层以太网接口类型。]{style="font-family:宋体"}]{#struct_0_x9962_12256_2142393250}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_202964964}

[[二层以太网接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}]{#struct_0_x9962_12256_203423715}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x546592124}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_203489251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_203292643}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1190978024}

[**[ethernet]{lang="EN-US"}**]{#struct_0_x9962_12256_203358179}[：将当前接口切换到二层以太网类型，切换后的接口速率与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[fc]{lang="EN-US"}**]{#struct_0_x9962_12256_1117295641}[：]{style="font-family:宋体"}[将当前接口切换到]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口类型]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_203161571}

[[某些二层以太网接口支持切换到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_203227107}[接口。]{style="font-family:宋体"}

[[如果要将二层以太网接口切换为]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1998875720}[接口，则需要进入对应的二层以太网接口视图执行]{style="font-family:宋体"}**[port-type]{lang="EN-US"}**[ **fc**]{lang="EN-US"}[命令；如果要将]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口切换回二层以太网接口，则需要进入对应的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口视图执行]{style="font-family:宋体"}**[port-type]{lang="EN-US"}**[ **ethernet**]{lang="EN-US"}[命令。]{style="font-family:宋体"}

[[接口类型切换后，原接口删除并创建新的接口，切换后的接口编号与切换前保持一致。]{style="font-family:宋体"}]{#struct_0_x9962_12256_203030499}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1043253870}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_202899427}[把二层以太网接口]{style="font-family:宋体"}[Ten-GigabitEthernet1/0/1]{lang="EN-US"}[切换为]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_203292642}

[\[Sysname\] interface ten-gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/0/1\] port-type fc]{lang="EN-US"}

[\[Sysname-Fc1/0/1\]]{lang="EN-US"}
:::::

::: {#-1230806099 .myid}
[]{#_Toc404798061}[]{#struct_0_x9962_12256_389295673}

**FC和FCoE \-- FC接口配置命令 \-- reset counters interface fc**

------------------------------------------------------------------------

[**[reset counters interface fc]{lang="EN-US"}**]{#struct_0_x9962_12256_x1398196163}[命令用来清除]{style="font-family:
宋体"}[FC]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_604813107}

[**[reset counters interface]{lang="EN-US"}**[ \[ **fc** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_389361209}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x592484562}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1628833642}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1469701966}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1642390978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2124504517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_275928341}

[**[fc]{lang="EN-US"}**]{#struct_0_x9962_12256_x2061523106}[：清除指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_1394063995}[：表示]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_418052819}

[[在某些情况下，需要统计一定时间内某]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x512377423}[接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9962_12256_x1793308940}**[fc]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9962_12256_388771384}**[fc]{lang="EN-US"}**[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[FC]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1397622148}**[fc]{lang="EN-US"}**[和]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1462575398}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_2072156729}[清除]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface fc 1/0/1]{lang="EN-US"}]{#struct_0_x9962_12256_1317921733}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_69373794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}**]{#struct_0_x9962_12256_x1467599693}**[fc]{lang="EN-US"}**
:::

::: {#1889156119 .myid}
[]{#_Toc404798062}[]{#struct_0_x9962_12256_203358178}

**FC和FCoE \-- FC接口配置命令 \-- shutdown (FC interface view)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x9962_12256_1117295642}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x9962_12256_203161570}[命令用来打开当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2073674197}

[**[shutdown]{lang="FR"}**]{#struct_0_x9962_12256_203227106}

[**[undo shutdown]{lang="FR"}**]{#struct_0_x9962_12256_203030498}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1043253869}

[[接口处于开启状态。]{style="font-family:宋体"}]{#struct_0_x9962_12256_203096034}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1878587571}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_202899426}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2142393252}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_202964962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_203423713}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x546592122}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_203292641}[关闭]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_203227105}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] shutdown]{lang="EN-US"}
:::

::: {#-738165832 .myid}
[]{#_Toc404798063}[]{#struct_0_x9962_12256_203030497}

**FC和FCoE \-- FC接口配置命令 \-- speed**

------------------------------------------------------------------------

[**[speed]{lang="EN-US"}**]{#struct_0_x9962_12256_x1043253880}[命令用来配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的速率。]{style="font-family:宋体"}

[**[undo speed]{lang="EN-US"}**]{#struct_0_x9962_12256_203096033}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_202899425}

[**[speed ]{lang="EN-US"}**[{**1000** \| **2000** \| **4000** \| **8000** \| **16000** \| **auto**}]{lang="EN-US"}]{#struct_0_x9962_12256_202964961}

[**[undo speed]{lang="EN-US"}**]{#struct_0_x9962_12256_x246333163}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_203423712}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x546592123}[接口的速率和]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的物理特性有关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_203489248}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_203292640}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1190978021}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_203358176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_203161568}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_117359053}

[**[1000]{lang="EN-US"}**]{#struct_0_x9962_12256_203227104}[：配置接口的]{style="font-family:宋体"}[速率为]{style="font-family:宋体"}[1000]{lang="FR"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2000]{lang="EN-US"}**]{#struct_0_x9962_12256_x1998875719}[：配置接口的]{style="font-family:宋体"}[速率为]{style="font-family:宋体"}[2000]{lang="FR"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[4000]{lang="EN-US"}**]{#struct_0_x9962_12256_203030496}[：配置接口的]{style="font-family:宋体"}[速率为]{style="font-family:宋体"}[4000]{lang="FR"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[8000]{lang="EN-US"}**]{#struct_0_x9962_12256_x1043253879}[：配置接口的]{style="font-family:宋体"}[速率为]{style="font-family:宋体"}[8000]{lang="FR"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[16000]{lang="EN-US"}**]{#struct_0_x9962_12256_x1363053442}[：配置接口的]{style="font-family:宋体"}[速率为]{style="font-family:宋体"}[16000]{lang="FR"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auto]{lang="EN-US"}**]{#struct_0_x9962_12256_x1362987906}[：配置接口]{style="font-family:宋体"}[自协商速率]{style="font-family:宋体"}[，通过两端的协商来选择可以接受的接口速率]{style="font-family:宋体"}[。]{style="font-family:宋体"}[具体协商机制与设备的型号有关，请以设备实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x474357906}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1363118978}[配置]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口的速率为]{style="font-family:宋体"}[1000Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1362725763}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] speed 1000]{lang="EN-US"}
:::

::: {#1167972859 .myid}
[]{#_Toc309984776}[]{#_Toc297888062}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404798065}[]{#struct_0_x9962_12256_352978749}

**FC和FCoE \-- VFC接口配置命令 \-- bandwidth (VFC interface view)**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_1931112507}[命令用来配置当前接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_x392298958}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x635993946}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x9962_12256_210786190}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_x1550742788}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2080588486}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x9962_12256_x390073267}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1315518610}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1931309115}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1129858428}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_724948914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1658602203}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x377996392}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x9962_12256_1892073103}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1776616740}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_586770163}[接口的期望带宽会影响]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[Cost]{lang="EN-US"}[值的计算，从而影响路由。]{style="font-family:宋体"}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x2019575795}[接口的缺省波特率为]{style="font-family:宋体"}[10Gbit/s]{lang="EN-US"}[，各产品可以修改其缺省波特率，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1931243579}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1164413433}[配置]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x711544550}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] bandwidth 50]{lang="EN-US"}
:::

::: {#1397158897 .myid}
[]{#_Toc404798066}[]{#struct_0_x9962_12256_118138092}

**FC和FCoE \-- VFC接口配置命令 \-- bind interface**

------------------------------------------------------------------------

[**[bind interface]{lang="EN-US"}**]{#struct_0_x9962_12256_x1305446505}[命令用来将]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口绑定到以太网接口（这里泛指二层以太网接口、二层聚合接口、]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口和]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口）。]{style="font-family:宋体"}

[**[undo bind interface]{lang="EN-US"}**]{#struct_0_x9962_12256_735918093}[命令用来删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口和以太网接口的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1197017967}

[**[bind interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}***[ ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*[ \[ **mac** *mac-address* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1931440187}

[**[undo bind interface]{lang="EN-US"}**]{#struct_0_x9962_12256_x799664993}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2062153947}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x728849225}[接口没有与以太网接口绑定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1664869552}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x201768929}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_875140703}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1585574407}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_41232381}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1931374651}

[*[interface-type interface-numbe]{lang="EN-US"}*[r]{lang="EN-US"}]{#struct_0_x9962_12256_x1162329393}[：指定接口类型和接口编号。接口类型包括二层以太网接口、二层聚合接口、]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口和]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口，不同型号的设备支持的接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x9962_12256_x1474723895}[：绑定的对端]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址，形式为]{style="font-family:宋体"}[XXXX-XXXX-XXXX]{lang="EN-US"}[，是]{style="font-family:宋体"}[6]{lang="EN-US"}[字节地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1124505677}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x426155987}[接口是一种虚拟接口，只有在绑定了以太网接口之后才可以使用、链路才能]{style="font-family:宋体"}[up]{lang="EN-US"}[，]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口通过与其绑定的以太网接口收发报文。]{style="font-family:宋体"}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_2014863275}[接口绑定对端]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址，可以使多个虚拟接口使用同一个物理链路。多个]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口可以绑定同一个以太网接口，但必须绑定不同的对端]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址，通过该]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址来区分]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口是和哪个对端设备进行通信。如果是点到多点的网络，必须要绑定]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址；如果是点到点的网络，则可以不绑定]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[交换机的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}]{#struct_0_x9962_12256_1301715410}[地址可以通过]{style="font-family:宋体"}**[display fcoe]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}[ENode]{lang="EN-US"}[的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址可以通过其它软件、网管等途径获取。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1931571259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x9962_12256_x801464358}[VFC]{lang="EN-US"}[接口只能绑定一个以太网接口，也只能绑定一个]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个以太网接口可以被多个]{style="font-family:宋体"}]{#struct_0_x9962_12256_1091879889}[VFC]{lang="EN-US"}[接口绑定，但是一个]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址仅能被一个]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口绑定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换机只有工作在专家模式下，才支持]{style="font-family:宋体"}]{#struct_0_x9962_12256_598862490}[FCoE over S-Channel]{lang="EN-US"}[能力，因此在绑定]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口或]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口前，应先将系统的工作模式切换为专家模式，否则会绑定失败。有关系统工作模式的介绍，请参见"基础配置指导"中的"设备管理"；有关]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口和]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口的介绍，请参见"]{style="font-family:宋体"}[EVB]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[EVB]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[绑定二层以太网接口时，该接口需具备]{style="font-family:宋体"}]{#struct_0_x9962_12256_x532136390}[FCoE]{lang="EN-US"}[能力，否则会绑定失败。绑定二层聚合接口时，其所有成员端口都需具备]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[能力，否则会绑定失败；向已绑定的二层聚合接口中添加新的成员端口时，需确保新加入的成员端口具备]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[能力，否则可能导致]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[流量转发不通。绑定]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口时，其对应的二层以太网接口需具备]{style="font-family:宋体"}[FCoE over S-Channel]{lang="EN-US"}[能力，否则会绑定失败。绑定]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口时，其对应二层聚合接口内的所有成员端口都需具备]{style="font-family:宋体"}[FCoE over S-Channel]{lang="EN-US"}[能力，否则会绑定失败；向已绑定的]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口对应的二层聚合接口中添加新的成员端口时，需确保新加入的成员端口具备]{style="font-family:宋体"}[FCoE over S-Channel]{lang="EN-US"}[能力，否则可能导致]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[流量转发不通。具体哪些单板具备]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[能力和]{style="font-family:宋体"}[FCoE over S-Channel]{lang="EN-US"}[能力，请参考产品手册的介绍。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果将二层聚合接口和该二层聚合接口的成员端口分别与不同的]{style="font-family:宋体"}]{#struct_0_x9962_12256_1804859600}[VFC]{lang="EN-US"}[接口绑定，则二层聚合接口的绑定配置将不会生效；如果将]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口和该]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口所对应二层聚合接口的成员端口分别与不同的]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口绑定，则]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口的绑定配置将不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在二层以太网接口或二层聚合接口上开启]{style="font-family:宋体"}]{#struct_0_x9962_12256_598862496}[EVB]{lang="EN-US"}[功能后，这些接口上的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[流量将断流，只有在这些接口上创建]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口或]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口并与]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口绑定后，才能恢复]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[流量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCoE over S-Channel]{lang="EN-US"}]{#struct_0_x9962_12256_1306999202}[只能应用于支持]{style="font-family:宋体"}[EVB]{lang="EN-US"}[功能的设备与服务器接口之间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x344245163}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1823716053}[将]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[4]{lang="EN-US"}[绑定到二层以太网接口]{style="font-family:宋体"}[Ten-GigabitEthernet1/0/1]{lang="EN-US"}[，并绑定]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[000c-2999-eacd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1931505723}

[\[sysname\] interface vfc 4]{lang="EN-US"}

[\[sysname-Vfc4\] bind interface ten-gigabitethernet 1/0/1 mac 000c-2999-eacd]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_598862495}[将]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[5]{lang="EN-US"}[绑定到二层聚合接口]{style="font-family:宋体"}[Bridge-aggregation1]{lang="EN-US"}[，并绑定]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[000c-2888-eacd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1306999203}

[\[sysname\] interface vfc 5]{lang="EN-US"}

[\[sysname-Vfc5\] bind interface bridge-aggregation 1 mac 000c-2888-eacd]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x943899594}[将]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[6]{lang="EN-US"}[绑定到]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channe1/0/1:10]{lang="EN-US"}[，并绑定]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[000c-2777-eacd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1758079820}

[\[sysname\] interface vfc 6]{lang="EN-US"}

[\[sysname-Vfc6\] bind interface s-channel 1/0/1:10 mac 000c-2777-eacd]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_598862494}[将]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[7]{lang="EN-US"}[绑定到]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="EN-US"}[，并绑定]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[000c-2666-eacd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1306999204}

[\[sysname\] interface vfc 7]{lang="EN-US"}

[\[sysname-Vfc7\] bind interface schannel-aggregation 1:10 mac 000c-2666-eacd]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1934701201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fcoe]{lang="EN-US"}**]{#struct_0_x9962_12256_1271175795}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_1717473970}
:::

::: {#-603010467 .myid}
[]{#_Toc309984777}[]{#_Toc297888063}[]{#_Toc404798067}[]{#struct_0_x9962_12256_1284613838}

**FC和FCoE \-- VFC接口配置命令 \-- default (VFC interface view)**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_x1859190126}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_252344317}

[**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_1287292340}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x449737086}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1931702331}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_752418291}

[[network-admin]{lang="FR"}]{#struct_0_x9962_12256_1164182383}

[[mdc-admin]{lang="FR"}]{#struct_0_x9962_12256_2035104987}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x102812203}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1274214224}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_x551673075}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_892703996}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1931636795}[将]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1963600810}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] default]{lang="EN-US"}
:::

::: {#393824126 .myid}
[]{#_Toc404798068}[]{#struct_0_x9962_12256_x1584311415}

**FC和FCoE \-- VFC接口配置命令 \-- description (VFC interface view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x9962_12256_x299482828}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo descripition]{lang="EN-US"}**]{#struct_0_x9962_12256_1410219249}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2010527144}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x9962_12256_1527016806}

[**[undo description]{lang="EN-US"}**]{#struct_0_x9962_12256_624380585}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1931178044}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ interface]{lang="EN-US"}]{#struct_0_x9962_12256_1901640152}["，例如：]{style="font-family:宋体"}[Vfc1 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1821105245}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x2128357969}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x508769033}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x835974412}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_725618829}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1572581453}

[*[text]{lang="EN-US"}*]{#struct_0_x9962_12256_1931112508}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x392102350}

[[接口的描述信息可以帮助用户标记接口的作用。]{style="font-family:宋体"}]{#struct_0_x9962_12256_491207785}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1786813254}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1955513537}[配置]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[VFCport1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_630769308}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] description VFCport1]{lang="EN-US"}
:::

::: {#330837287 .myid}
[]{#_Toc404798069}[]{#struct_0_x9962_12256_x800874537}[]{#_Toc309984778}[]{#_Toc297888064}[]{#_Toc396139634}[]{#_Toc396202852}[]{#_Toc396223384}[]{#_Toc396224461}[]{#_Toc396321045}[]{#_Toc396894904}[]{#_Toc397089081}[]{#_Toc396139635}[]{#_Toc396202853}[]{#_Toc396223385}[]{#_Toc396224462}[]{#_Toc396321046}[]{#_Toc396894905}[]{#_Toc397089082}[]{#_Toc367887644}[]{#_Toc369075976}[]{#_Toc367887645}[]{#_Toc369075977}[]{#_Toc367887646}[]{#_Toc369075978}[]{#_Toc367887647}[]{#_Toc369075979}[]{#_Toc367887648}[]{#_Toc369075980}[]{#_Toc367887649}[]{#_Toc369075981}[]{#_Toc367887650}[]{#_Toc369075982}[]{#_Toc367887651}[]{#_Toc369075983}[]{#_Toc367887652}[]{#_Toc369075984}[]{#_Toc367887653}[]{#_Toc369075985}[]{#_Toc367887654}[]{#_Toc369075986}[]{#_Toc367887655}[]{#_Toc369075987}[]{#_Toc367887656}[]{#_Toc369075988}[]{#_Toc367887657}[]{#_Toc369075989}[]{#_Toc367887658}[]{#_Toc369075990}[]{#_Toc367887659}[]{#_Toc369075991}[]{#_Toc367887660}[]{#_Toc369075992}[]{#_Toc367887661}[]{#_Toc369075993}[]{#_Toc367887662}[]{#_Toc369075994}[]{#_Toc367887678}[]{#_Toc369076010}[]{#_Toc367887679}[]{#_Toc369076011}[]{#_Toc367887680}[]{#_Toc369076012}[]{#_Toc367887681}[]{#_Toc369076013}[]{#_Toc367887682}[]{#_Toc369076014}

**FC和FCoE \-- VFC接口配置命令 \-- display interface vfc**

------------------------------------------------------------------------

[**[display interface vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_x450247597}[命令用来显示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x431242847}

[**[display interface]{lang="EN-US"}**[ \[ **vfc** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_1391824995}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2097665512}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1989294733}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1931505724}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1934373521}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1688638073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1666723246}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1019581412}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x567046168}

[**[vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_x105207968}[：显示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的信息。如果未指定本参数，将显示设备支持的所有接口的信息。]{style="font-family:宋体"}

[*[interface-numbe]{lang="EN-US"}*[r]{lang="EN-US"}]{#struct_0_x9962_12256_857529343}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准]{style="font-family:宋体"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x9962_12256_x88161431}[：显示概要信息。如果未指定本参数，将显示详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x9962_12256_752221683}[：当用户配置的接口描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不会显示。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x9962_12256_x959703378}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果未指定本参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_542257380}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_1520206098}**[vfc]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9962_12256_1809664740}**[vfc]{lang="EN-US"}**[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有]{lang="EN-US" style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1729164816}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x96247469}[显示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface vfc 1]{lang="EN-US"}]{#struct_0_x9962_12256_1931636796}

[Vfc1]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Vfc1 Interface]{lang="EN-US"}

[Bandwidth: 10000000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 2112]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol is FC]{lang="EN-US"}

[Port WWN is 66:66:66:63:66:64:61:30]{lang="EN-US"}

[FC mode is E, state is E]{lang="EN-US"}

[Support the VSAN protocol]{lang="EN-US"}

[VSAN tagging mode is Tagging]{lang="EN-US"}

[EVFP common VSAN: 1]{lang="EN-US"}

[Bound interface is Ten-GigabitEthernet1/0/1, Bound MAC is 000c-2933-eacd]{lang="EN-US"}

[VSAN of physical-UP state: 1]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display interface vfc]{lang="EN-US"}]{#struct_0_x9962_12256_1963535274}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1262787069}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_328833579}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_926987679}

[[Current state]{lang="EN-US"}]{#struct_0_x9962_12256_x797705308}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1138328600}[接口的物理状态和管理状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN ( Administratively )]{lang="EN-US"}]{#struct_0_x9962_12256_881375766}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1118671680}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_x1936420784}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x9962_12256_662651831}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x797770844}[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1478960715}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_x2071317535}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x9962_12256_1851718236}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x2076849781}[接口的描述信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x9962_12256_x797574236}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1893005426}[接口的期望带宽]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x9962_12256_926529152}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_921036335}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x9962_12256_x1327053444}

[[对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9962_12256_x797639772}[报文的处理能力，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示没有为该接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_x9962_12256_1975717110}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x60326994}[接口的链路层协议类型]{style="font-family:宋体"}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x694941138}

[[端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1257000465}

[[FC mode]{lang="EN-US"}]{#struct_0_x9962_12256_x797443164}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x1976645543}[接口的配置模式]{style="font-family:宋体"}

[[state]{lang="EN-US"}]{#struct_0_x9962_12256_720685425}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x1481515557}[接口的协商运行状态]{style="font-family:宋体"}

[[Support the VSAN protocol]{lang="EN-US"}]{#struct_0_x9962_12256_x797508700}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_420184365}[接口支持]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[VSAN tagging mode]{lang="EN-US"}]{#struct_0_x9962_12256_1267767521}

[[端口的连接方式是]{style="font-family:宋体"}[Trunk]{lang="EN-US"}]{#struct_0_x9962_12256_x1133214806}[（]{style="font-family:宋体"}[Tagging]{lang="EN-US"}[）或]{style="font-family:宋体"}[Access]{lang="EN-US"}[（]{style="font-family:宋体"}[Non tagging]{lang="EN-US"}[），]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口只支持]{style="font-family:宋体"}[Tagging]{lang="EN-US"}

[[EVFP common VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x797312092}

[[经过协商后确定端口连接并]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x9962_12256_x1202176860}[的公共]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，此信息只有接口链路]{style="font-family:宋体"}[up]{lang="EN-US"}[后才显示]{style="font-family:宋体"}

[[Bound interface]{lang="EN-US"}]{#struct_0_x9962_12256_x1614361756}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_294350942}[接口绑定的物理接口]{style="font-family:宋体"}

[[Bound MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x797377628}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1531222652}[接口绑定的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VSAN of physical-UP state]{lang="EN-US"}]{#struct_0_x9962_12256_1549860503}

[[处于物理]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x9962_12256_1784890061}[状态的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x9962_12256_x797181020}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x9962_12256_1550496008}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_483092714}[显示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface vfc 1 brief]{lang="EN-US"}]{#struct_0_x9962_12256_x582573830}

[Brief information on VFC interface(s):]{lang="EN-US"}

[Admin Mode: auto - auto; E - e port; F - f port; NP - n port proxy]{lang="EN-US"}

[Oper Mode: E - e port; F - f port; NP - n port proxy;]{lang="EN-US"}

[           TE - trunking e port; TF - trunking f port;]{lang="EN-US"}

[           TNP - trunking n port proxy]{lang="EN-US"}

[Interface  Admin Admin Oper Status Bind]{lang="EN-US"}

[           Mode  Trunk Mode        Interface]{lang="EN-US"}

[                 Mode]{lang="EN-US"}

[Vfc1       F     on    TF   UP     XGE1/0/1 01:02:03:04:05:06]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display interface vfc brief]{lang="EN-US"}]{#struct_0_x9962_12256_x1639517031}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1949725769}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2042801558}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_384910020}

[[Brief information on VFC interface(s)]{lang="EN-US"}]{#struct_0_x9962_12256_x476717617}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x523771784}[接口的概要信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_508196381}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1042312157}[接口的名称]{style="font-family:宋体"}

[[Admin Mode]{lang="EN-US"}]{#struct_0_x9962_12256_331438784}

[[配置的]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x745784416}[接口的模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x9962_12256_820299525}[：表示]{lang="EN-US" style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:宋体"}[VFC]{lang="PT-BR"}[接口不支持本模式）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_703169956}[：表示]{lang="EN-US" style="font-family:宋体"}[E]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_417014998}[：表示]{lang="EN-US" style="font-family:宋体"}[F]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_1709114936}[：表示]{lang="EN-US" style="font-family:宋体"}[NP]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Admin Trunk Mode]{lang="EN-US"}]{#struct_0_x9962_12256_1983098939}

[[配置的]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1223584052}[接口的]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x9962_12256_2033475790}[：表示]{lang="EN-US" style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[on]{lang="EN-US"}]{#struct_0_x9962_12256_x1505299303}[：表示]{style="font-family:宋体"}[On]{lang="PT-BR"}[模式（]{style="font-family:宋体"}[VFC]{lang="PT-BR"}[接口仅支持本模式）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[off]{lang="EN-US"}]{#struct_0_x9962_12256_x1908583830}[：表示]{lang="EN-US" style="font-family:宋体"}[Off]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Oper Mode]{lang="EN-US"}]{#struct_0_x9962_12256_x681908598}

[[链路层协商后，]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x342499889}[接口的运行模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_x389554056}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_1874728764}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_1176529885}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_x745849952}[E]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_x1219941567}[F]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_820233989}[NP]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[\--]{lang="EN-US"}]{#struct_0_x9962_12256_1138710350}[：表示未发起协商或协商失败]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x9962_12256_416949462}

[[链路层协商后，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1983033403}[接口的状态：]{style="font-family:宋体"}[UP]{lang="EN-US"}[或]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[Bind Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1388184279}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1223518516}[接口的绑定信息，包括：绑定的以太网接口和]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址。如果没有配置绑定信息，则显示为空]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1138370538}[显示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的描述信息。]{style="font-family:宋体"}

[[\<sysname\> display interface vfc brief description]{lang="EN-US"}]{#struct_0_x9962_12256_x1182958784}

[Brief information on VFC interface(s):]{lang="EN-US"}

[Interface    Description]{lang="EN-US"}

[Vfc1         Vfc1 Interface]{lang="EN-US"}

[Vfc2         Vfc2 Interface]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display interface vfc brief description]{lang="EN-US"}]{#struct_0_x9962_12256_x1505364839}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1960643151}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1583043052}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1908649366}

[[Brief information on VFC interface(s)]{lang="EN-US"}]{#struct_0_x9962_12256_x1823630307}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x342565425}[接口的概要信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x1551584420}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x389619592}[接口的名称]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x9962_12256_1176464349}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1251935979}[接口的描述信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x797246556}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface vfc brief down]{lang="EN-US"}]{#struct_0_x9962_12256_x1981673803}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Vfc1                 ADM  Administratively]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display interface vfc brief down]{lang="EN-US"}]{#struct_0_x9962_12256_x1091065675}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1260496377}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1648466183}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x481941035}

[[Brief information on interface(s) under bridge mode]{lang="EN-US"}]{#struct_0_x9962_12256_950057449}

[[二层模式下（]{style="font-family:宋体"}[bridge]{lang="EN-US"}]{#struct_0_x9962_12256_x797705307}[）的接口概要信息，即二层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x9962_12256_1137738776}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1277576807}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x9962_12256_26022039}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x797574235}

[[接口名称]{style="font-family:宋体"}]{#struct_0_x9962_12256_1892808818}

[[Link]{lang="EN-US"}]{#struct_0_x9962_12256_x2104053044}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x9962_12256_358266955}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_x797639771}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1975520502}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x9962_12256_x52743068}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x9962_12256_x883687073}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x9962_12256_1550037253}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x9962_12256_1686697176}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x105207966}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x9962_12256_588140171}**[ vfc]{lang="EN-US"}**

::: {#1691908750 .myid}
[]{#_Toc309984780}[]{#_Toc404798070}[]{#struct_0_x9962_12256_6673659}

**FC和FCoE \-- VFC接口配置命令 \-- fc mode (VFC interface view)**

------------------------------------------------------------------------

[**[fc mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x797246555}[命令用来配置]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的模式。]{style="font-family:宋体"}

[**[undo fc mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x1981739339}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1065300690}

[**[fc mode]{lang="FR"}**]{#struct_0_x9962_12256_x1209265391}[ { **e** \| **f** \| **np** }]{lang="FR"}

[**[undo fc mode]{lang="FR"}**]{#struct_0_x9962_12256_1146169628}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x584229592}

[[VFC]{lang="FR"}]{#struct_0_x9962_12256_x1060432893}[接]{style="font-family:宋体"}[口的模式为]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x57563742}

[[VFC]{lang="FR"}]{#struct_0_x9962_12256_x2035922491}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x797705310}

[[network-admin]{lang="FR"}]{#struct_0_x9962_12256_1137804311}

[[mdc-admin]{lang="FR"}]{#struct_0_x9962_12256_1102201254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1670932278}

[**[e]{lang="PT-BR"}**]{#struct_0_x9962_12256_x970008505}[：]{style="font-family:宋体"}[E]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[f]{lang="SV"}**]{#struct_0_x9962_12256_1415273667}[：]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式。]{style="font-family:
宋体"}

[**[np]{lang="SV"}**]{#struct_0_x9962_12256_x949573736}[：]{style="font-family:宋体"}[NP]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_205495443}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x105207961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x105207960}[交换机只支持]{style="font-family:宋体"}[E]{lang="PT-BR"}[模式和]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式；]{style="font-family:宋体"}[NPV]{lang="FR"}[交换机只支持]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式和]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式；]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持]{style="font-family:宋体"}[E]{lang="PT-BR"}[模式、]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式和]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x9962_12256_588009099}[FCF-NPV]{lang="EN-US"}[交换机上，如果用户配置的]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口模式与该接口所属的某个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的工作模式不匹配，则]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口模式的配置在该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下将不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1892612210}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x993104076}[配置]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[工作在]{style="font-family:宋体"}[E]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1614022647}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] fc mode e]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x958830987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1460400917}
:::

::: {#1262882529 .myid}
[]{#_Toc404798071}[]{#struct_0_x9962_12256_x959310165}

**FC和FCoE \-- VFC接口配置命令 \-- interface vfc**

------------------------------------------------------------------------

[**[interface vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_x959506773}[命令用来创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口并进入]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口视图。如果该]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口已经存在，则直接进入]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[**[undo interface vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_x959441237}[命令用来删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959637845}

[**[interface vfc ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x2016427374}

[**[undo interface vfc ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x959572309}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959768917}

[[不存在]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x959703381}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1111987427}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x959899989}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959834453}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x959375702}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x959310166}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_328725038}

[*[interface-numbe]{lang="EN-US"}*[r]{lang="EN-US"}]{#struct_0_x9962_12256_x959506774}[：表示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959441238}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x959637846}[接口是手工创建的虚拟逻辑口，它虚拟实现物理]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959572310}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x454358731}[创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x959768918}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959703382}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_x959899990}
:::

::: {#757013670 .myid}
[]{#_Toc404798072}[]{#struct_0_x9962_12256_x959834454}

**FC和FCoE \-- VFC接口配置命令 \-- reset counters interface vfc**

------------------------------------------------------------------------

[**[reset counters interface vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_x959375703}[命令用来清除]{style="font-family:
宋体"}[VFC]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959310167}

[**[reset counters interface]{lang="EN-US"}**[ \[ **vfc** \[ *number* \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_x959506775}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_750859979}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x959441239}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959637847}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x959572311}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x959768919}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2086824059}

[**[vfc]{lang="EN-US"}**]{#struct_0_x9962_12256_1470932832}[：清除指定]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*]{#struct_0_x9962_12256_x959703383}[：表示]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x959899991}

[[在某些情况下，需要统计一定时间内某]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x959834455}[接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9962_12256_1769507657}**[vfc]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9962_12256_1769573193}**[vfc]{lang="EN-US"}**[而不指定]{lang="EN-US" style="font-family:宋体"}*[number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_1690874112}**[vfc]{lang="EN-US"}**[和]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，则清除指定]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769376585}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1769442121}[清除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface vfc 1]{lang="EN-US"}]{#struct_0_x9962_12256_1769245513}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2097715989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}**]{#struct_0_x9962_12256_1769311049}**[vfc]{lang="EN-US"}**
:::

::: {#-22591828 .myid}
[]{#_Toc404798073}[]{#struct_0_x9962_12256_1769114441}

**FC和FCoE \-- VFC接口配置命令 \-- shutdown (VFC interface view)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x9962_12256_1769179977}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x9962_12256_1768983369}[命令用来打开当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769048905}

[**[shutdown]{lang="FR"}**]{#struct_0_x9962_12256_1769507656}

[**[undo shutdown]{lang="FR"}**]{#struct_0_x9962_12256_1694860128}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769573192}

[[接口处于开启状态。]{style="font-family:宋体"}]{#struct_0_x9962_12256_1769376584}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769442120}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x1029489537}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769245512}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1769311048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1769114440}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769179976}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1700995956}[关闭]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1769048904}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] shutdown]{lang="EN-US"}
:::

::: {#-526825173 .myid}
[]{#_Toc347837021}[]{#_Toc404798075}[]{#struct_0_x9962_12256_1769573191}

**FC和FCoE \-- FC链路聚合配置命令 \-- bandwidth (FC aggregate interface view)**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_1769376583}[命令用来配置当前接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_522915720}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769442119}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x9962_12256_1769245511}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x9962_12256_1769311047}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769114439}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_x9962_12256_1768983367}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769048903}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1769507654}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1694729056}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1769573190}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1769376582}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769442118}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x9962_12256_1769245510}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2097519381}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1769311046}[聚合接口的波特率＝]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的速率。]{style="font-family:宋体"}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1769114438}[聚合接口的期望带宽会影响]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[Cost]{lang="EN-US"}[值的计算，从而影响路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769179974}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1768983366}[配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[1000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1769048902}

[\[Sysname\] interface san-aggregation 3]{lang="EN-US"}

[\[Sysname-SAN-Aggregation3\] bandwidth 1000]{lang="EN-US"}
:::

::: {#-766323398 .myid}
[]{#_Toc404798076}[]{#struct_0_x9962_12256_x1019040013}

**FC和FCoE \-- FC链路聚合配置命令 \-- default (FC aggregate interface view)**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_1769507653}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769573189}

[**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_1769376581}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769442117}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1769245509}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2098109204}

[[network-admin]{lang="FR"}]{#struct_0_x9962_12256_1769311045}

[[mdc-admin]{lang="FR"}]{#struct_0_x9962_12256_1769114437}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769179973}

[[接口下的某些配置恢复到缺省情况后]{style="font-family:宋体"}]{#struct_0_x9962_12256_1701192564}[，]{style="font-family:
宋体"}[会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x9962_12256_1768983365}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769048901}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1769507652}[将]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1769376580}

[\[Sysname\] interface san-aggregation 3]{lang="EN-US"}

[\[Sysname-SAN-Aggregation3\] default]{lang="EN-US"}
:::

::: {#-1299500109 .myid}
[]{#_Toc404798077}[]{#struct_0_x9962_12256_522850184}

**FC和FCoE \-- FC链路聚合配置命令 \-- description (FC aggregate interface view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x9962_12256_1769048900}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo descripition]{lang="EN-US"}**]{#struct_0_x9962_12256_1816561824}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816627360}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x9962_12256_x1087080072}

[**[undo description]{lang="EN-US"}**]{#struct_0_x9962_12256_1816430752}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816496288}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ interface]{lang="EN-US"}]{#struct_0_x9962_12256_1816299680}["，例如：]{style="font-family:宋体"}[SAN-Aggregation3 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816365216}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_2025349914}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816168608}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1816234144}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1816037536}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816103072}

[*[text]{lang="EN-US"}*]{#struct_0_x9962_12256_x1834506440}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816430751}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1250100380}[配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[SAGG-interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1816496287}

[\[Sysname\] interface san-aggregation 3]{lang="EN-US"}

[\[Sysname-SAN-Aggregation3\] description SAGG-interface]{lang="EN-US"}
:::

::: {#-13916469 .myid}
[]{#_Toc404798078}[]{#struct_0_x9962_12256_2025153306}[]{#_Toc396139645}[]{#_Toc396202863}[]{#_Toc396223395}[]{#_Toc396224472}[]{#_Toc396321056}[]{#_Toc396894915}[]{#_Toc397089092}[]{#_Toc396139646}[]{#_Toc396202864}[]{#_Toc396223396}[]{#_Toc396224473}[]{#_Toc396321057}[]{#_Toc396894916}[]{#_Toc397089093}

**FC和FCoE \-- FC链路聚合配置命令 \-- display interface san-aggregation**

------------------------------------------------------------------------

[**[display interface san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_1816168607}[命令用来显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816234143}

[**[display interface]{lang="EN-US"}**[ \[ **san-aggregation** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_1816103071}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816561822}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1816627358}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816430750}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1250034844}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1816496286}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1816299678}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1816365214}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816168606}

[**[san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_1470932833}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的信息。如果未指定本参数，将显示设备支持的所有接口的信息。]{style="font-family:宋体"}

[*[interface-numbe]{lang="EN-US"}*[r]{lang="EN-US"}]{#struct_0_x9962_12256_x745428514}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，将显示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x9962_12256_1816234142}[：显示概要信息。如果未指定本参数，将显示详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x9962_12256_1816037534}[：当用户配置的接口描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不会显示。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x9962_12256_1816103070}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816561821}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}**[san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_1816627357}[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_1816430749}[参数，不指定]{lang="EN-US" style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有]{lang="EN-US" style="font-family:宋体"}[FC]{lang="EN-US"}[聚合]{style="font-family:宋体"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1250624669}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1816496285}[显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface san-aggregation 3]{lang="EN-US"}]{#struct_0_x9962_12256_1816168605}

[SAN-Aggregation3]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: SAN-Aggregation3 Interface]{lang="EN-US"}

[Bandwidth: 1000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 2112]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol is FC]{lang="EN-US"}

[Port WWN is 00:00:00:00:00:00:00:00]{lang="EN-US"}

[FC mode is Auto, state is Init]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display interface san-aggregation]{lang="EN-US"}]{#struct_0_x9962_12256_x745625122}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2049730513}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816037533}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816103069}

[[Current state]{lang="EN-US"}]{#struct_0_x9962_12256_1816627356}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1816430748}[聚合接口的物理状态和管理状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN ( Administratively )]{lang="EN-US"}]{#struct_0_x9962_12256_1816299676}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1816365212}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_1816234140}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x9962_12256_1816037532}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1816561819}[聚合接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1816430747}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_1816496283}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x9962_12256_1816365211}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1816168603}[聚合接口的描述信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x9962_12256_1816037531}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1816103067}[聚合接口的期望带宽，只有取值不为]{style="font-family:宋体"}[0]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x9962_12256_250543419}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_250346811}[聚合接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x9962_12256_250215739}

[[对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9962_12256_250281275}[报文的处理能力，]{style="font-family:宋体"}[disabled]{lang="EN-US"}[表示没有为该接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_x9962_12256_250150203}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_249953595}[聚合接口的链路层协议类型]{style="font-family:宋体"}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_250019131}

[[端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_250543418}

[[FC mode]{lang="EN-US"}]{#struct_0_x9962_12256_250346810}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_250215738}[聚合接口的配置模式]{style="font-family:宋体"}

[[state]{lang="EN-US"}]{#struct_0_x9962_12256_250281274}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_250150202}[聚合接口的协商运行状态]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x9962_12256_249953594}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x9962_12256_250477881}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_250543417}[显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface san-aggregation 3 brief]{lang="EN-US"}]{#struct_0_x9962_12256_250346809}

[Brief information on SAN-Aggregation interface(s):]{lang="EN-US"}

[Admin Mode: auto - auto; E - e port; F - f port; NP - n port proxy]{lang="EN-US"}

[Oper Mode: E - e port; F - f port; NP - n port proxy;]{lang="EN-US"}

[           TE - trunking e port; TF - trunking f port;]{lang="EN-US"}

[           TNP - trunking n port proxy]{lang="EN-US"}

[Interface  VSAN Admin Admin Oper Oper   Status]{lang="EN-US"}

[                Mode  Trunk Mode Speed]{lang="EN-US"}

[                      Mode]{lang="EN-US"}

[SAGG3      37   NP    auto  NP   4G     UP]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display interface san-aggregation brief]{lang="EN-US"}]{#struct_0_x9962_12256_x342762033}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1914170465}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x389816200}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1176267741}

[[Brief information on SAN-Aggregation interface(s)]{lang="EN-US"}]{#struct_0_x9962_12256_x746112096}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_819971845}[聚合接口的概要信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x132788906}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_416687318}[聚合接口的名称]{style="font-family:宋体"}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1982771259}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1223256372}[聚合接口的]{style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}

[[Admin Mode]{lang="EN-US"}]{#struct_0_x9962_12256_x1505626983}

[[配置的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1075965345}[聚合接口的模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x9962_12256_x1908911510}[：表示]{lang="EN-US" style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_x342827569}[：表示]{lang="EN-US" style="font-family:宋体"}[E]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_x389881736}[：表示]{lang="EN-US" style="font-family:宋体"}[F]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_1176202205}[：表示]{lang="EN-US" style="font-family:宋体"}[NP]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Admin Trunk Mode]{lang="EN-US"}]{#struct_0_x9962_12256_2050563711}

[[配置的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x611894368}[聚合接口的]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x9962_12256_954189573}[：表示]{lang="EN-US" style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[on]{lang="EN-US"}]{#struct_0_x9962_12256_550905046}[：表示]{lang="EN-US" style="font-family:宋体"}[On]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[off]{lang="EN-US"}]{#struct_0_x9962_12256_2116988987}[：表示]{lang="EN-US" style="font-family:宋体"}[Off]{lang="PT-BR"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Oper Mode]{lang="EN-US"}]{#struct_0_x9962_12256_1357474100}

[[链路层协商后，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1057378849}[聚合接口的运行模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_x1371409255}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_x1774693782}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_x208609841}[：表示工作在]{lang="EN-US" style="font-family:宋体"}[Access VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_x255664008}[E]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[E_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_1310419933}[F]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[F_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="PT-BR"}]{#struct_0_x9962_12256_x1163905825}[NP]{lang="PT-BR"}[：]{lang="EN-US" style="font-family:宋体"}[表示工作在]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="PT-BR"}[方式下的]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="PT-BR"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[\--]{lang="EN-US"}]{#struct_0_x9962_12256_x611959904}[：表示未发起协商或协商失败]{style="font-family:宋体"}

[[Oper Speed]{lang="EN-US"}]{#struct_0_x9962_12256_954124037}

[[物理层协商后，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_550839510}[聚合接口的速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[。未发起协商或协商失败时，将显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x9962_12256_2116923451}

[[链路层协商后，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1357408564}[聚合接口的状态：]{style="font-family:宋体"}[UP]{lang="EN-US"}[或]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1318139549}[显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的描述信息。]{style="font-family:宋体"}

[[\<sysname\> display interface san-aggregation brief description]{lang="EN-US"}]{#struct_0_x9962_12256_x101790805}

[Brief information on SAN-Aggregation interface(s):]{lang="EN-US"}

[Interface    Description]{lang="EN-US"}

[SAGG1        SAGG1 Interface]{lang="EN-US"}

[SAGG2        SAGG2 Interface]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display interface san-aggregation brief description]{lang="EN-US"}]{#struct_0_x9962_12256_x1524043387}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1896037445}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1371474791}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1774759318}

[[Brief information on SAN-Aggregation interface(s)]{lang="EN-US"}]{#struct_0_x9962_12256_x208675377}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x871810900}[聚合接口的概要信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x255729544}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1310354397}[聚合接口的名称]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x9962_12256_x612025440}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_954058501}[聚合接口的描述信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_377142459}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface san-aggregation brief down]{lang="EN-US"}]{#struct_0_x9962_12256_250412345}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[SAGG3                ADM  Administratively]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display interface san-aggregation brief down]{lang="EN-US"}]{#struct_0_x9962_12256_250215737}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2040467233}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_250281273}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_250150201}

[[Brief information on interface(s) under bridge mode]{lang="EN-US"}]{#struct_0_x9962_12256_249953593}

[[二层模式下（]{style="font-family:宋体"}[bridge]{lang="EN-US"}]{#struct_0_x9962_12256_250477880}[）的接口概要信息，即二层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x9962_12256_250543416}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x9962_12256_250215736}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x9962_12256_250281272}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_249953591}

[[接口名称]{style="font-family:宋体"}]{#struct_0_x9962_12256_250477878}

[[Link]{lang="EN-US"}]{#struct_0_x9962_12256_250346806}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x9962_12256_250412342}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_250084662}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_x2128597640}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x9962_12256_x2128859784}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x9962_12256_x2128728712}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x9962_12256_x2128663179}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x9962_12256_x2128728715}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x867719328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x9962_12256_348909868}**[ ]{lang="EN-US"}[san-aggregation]{lang="EN-US"}**

::: {#2047370689 .myid}
[]{#_Toc404798079}[]{#struct_0_x9962_12256_x2129056395}

**FC和FCoE \-- FC链路聚合配置命令 \-- display san-aggregation**

------------------------------------------------------------------------

[**[display san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x2129121931}[命令用来显示已有]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1405809599}

[**[display san-aggregation]{lang="EN-US"}**[ \[ **verbose** \] \[ **interface** **san-aggregation** *interface-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x2128532108}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2128597644}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x2128401036}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_678030352}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2128466572}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x2128794252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2128859788}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1290452600}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2128663180}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9962_12256_x2128728716}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的详细信息。不指定本参数时，将显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的简要信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ **san-aggregation** *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_x2129056396}[：显示指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的编号，]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。不指定本参数时，将显示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2129121932}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2128532109}[显示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display san-aggregation]{lang="EN-US"}]{#struct_0_x9962_12256_x2128728717}

[\* indicates the member port is selected.]{lang="EN-US"}

[Interface        State   Mode   Speed     Member port]{lang="EN-US"}

[SAGG1            UP      E      8Gbps    \*Fc1/0/1]{lang="EN-US"}

[                                          Fc1/0/2]{lang="EN-US"}

[SAGG2            DOWN    -      -         -]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display san-aggregation]{lang="EN-US"}]{#struct_0_x9962_12256_x2129056397}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1736969517}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_600351251}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_600285715}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_600416787}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_600089107}[聚合接口的简写名称]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x9962_12256_600220179}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_599826963}[聚合接口的物理状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_599761427}[：该接口的物理状态为关闭，表示对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组内没有选中成员接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_600285714}[：该接口的物理状态为开启，表示对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组内有选中成员接口]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x9962_12256_600416786}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_600089106}[聚合接口的运行模式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_600220178}[：]{style="font-family:宋体"}[E]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_600154642}[：]{style="font-family:宋体"}[F]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_599761426}[：]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_600285713}[聚合接口物理状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[时显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_x9962_12256_600482321}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_600089105}[聚合接口的速率，为所有选中成员接口的速率之和（]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口物理状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[时显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Member port]{lang="EN-US"}]{#struct_0_x9962_12256_600220177}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_600154641}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的成员接口（带]{style="font-family:宋体"}[\*]{lang="EN-US"}[表示为选中成员接口，没有成员接口时显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_599826961}[显示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display san-aggregation verbose]{lang="EN-US"}]{#struct_0_x9962_12256_600351247}

[Interface SAN-Aggregation1]{lang="EN-US"}[：]{style="font-family:宋体"}

[State                : UP]{lang="EN-US"}

[Mode                 : E]{lang="EN-US"}

[Speed                : 2Gbps]{lang="EN-US"}

[Member port number   : 2]{lang="EN-US"}

[Selected port number : 1]{lang="EN-US"}

[  Member port        State   Mode   Speed   Selected]{lang="EN-US"}

[  Fc1/0/1            UP      E      2Gbps   Y]{lang="EN-US"}

[  Fc1/0/2            UP      E      1Gbps   N]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface SAN-Aggregation2:]{lang="EN-US"}

[State                : DOWN]{lang="EN-US"}

[Mode                 : N/A]{lang="EN-US"}

[Speed                : N/A]{lang="EN-US"}

[Member port number   : 2]{lang="EN-US"}

[Selected port number : 0]{lang="EN-US"}

[  Member port         State   Mode   Speed   Selected]{lang="EN-US"}

[  Fc1/0/3             DOWN    -      -       N]{lang="EN-US"}

[  Fc1/0/4             DOWN    -      -       N]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display san-aggregation verbose]{lang="EN-US"}]{#struct_0_x9962_12256_600285711}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1720646417}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_600482319}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_600089103}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_600220175}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_600154639}[聚合接口的名称]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x9962_12256_599761423}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_600285710}[聚合接口的物理层状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_600416782}[：该接口的物理状态为关闭，表示对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组内没有选中成员接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_599826958}[：该接口的物理状态为开启，表示对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组内有选中成员接口]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x9962_12256_1003635778}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1003766850}[聚合接口的运行模式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_1003701314}[：]{style="font-family:宋体"}[E]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_1003308098}[：]{style="font-family:宋体"}[F]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_1003439170}[：]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1003045954}[聚合接口物理状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[时显示为"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_x9962_12256_1003635777}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1003766849}[聚合接口的速率，为所有选中成员接口的速率之和（]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口物理状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[时显示为"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Member port number]{lang="EN-US"}]{#struct_0_x9962_12256_1003373633}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1003308097}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的成员接口的数量]{style="font-family:宋体"}

[[Selected port number]{lang="EN-US"}]{#struct_0_x9962_12256_1003439169}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1003045953}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的选中成员接口的数量]{style="font-family:宋体"}

[[Member port]{lang="EN-US"}]{#struct_0_x9962_12256_1003570240}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1003766848}[聚合接口所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的成员接口名称，没有成员接口时不显示]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x9962_12256_1003373632}

[[成员接口的链路协议状态，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1003504704}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1003439168}[：该接口的链路协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9962_12256_1003045952}[：该接口的链路协议状态为开启]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x9962_12256_1003570239}

[[成员接口的运行模式，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1003701311}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x9962_12256_1003373631}[：]{style="font-family:宋体"}[E]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_1003504703}[：]{style="font-family:宋体"}[F]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_1003111487}[：]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[（成员接口的链路协议状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1003635774}[时显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_x9962_12256_1003766846}

[[成员接口的速率（成员接口的链路协议状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x9962_12256_1003701310}[时显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Selected]{lang="EN-US"}]{#struct_0_x9962_12256_1003308094}

[[成员接口的选中状态，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1003439166}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x9962_12256_1003045950}[：该接口未被选中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_x9962_12256_1003635773}[：该接口被选中]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1232884687 .myid}
[]{#_Toc347837020}[]{#_Toc404798080}[]{#struct_0_x9962_12256_1003766845}

**FC和FCoE \-- FC链路聚合配置命令 \-- fc mode (FC aggregate interface view)**

------------------------------------------------------------------------

[**[fc mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1003701309}[命令用来配置]{style="font-family:宋体"}[FC]{lang="FR"}[聚合接口的模式。]{style="font-family:宋体"}

[**[undo fc mode]{lang="EN-US"}**]{#struct_0_x9962_12256_513644580}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1003373629}

[**[fc mode]{lang="FR"}**]{#struct_0_x9962_12256_1003308093}[ { **auto** \| **e** \| **f** ]{lang="FR"}[\| **np**]{lang="EN-US"}[ }]{lang="FR"}

[**[undo fc mode]{lang="FR"}**]{#struct_0_x9962_12256_1003504701}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1003439165}

[[FCF]{lang="FR"}]{#struct_0_x9962_12256_x867719327}[交换机缺省为]{style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[NPV]{lang="FR"}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="FR"}[交换机]{style="font-family:宋体"}[缺省]{style="font-family:宋体"}[为]{style="font-family:宋体"}[F]{lang="FR"}[模式。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562448163}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x562513699}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562317091}

[[network-admin]{lang="FR"}]{#struct_0_x9962_12256_x562382627}

[[mdc-admin]{lang="FR"}]{#struct_0_x9962_12256_x562710307}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562775843}

[**[auto]{lang="PT-BR"}**]{#struct_0_x9962_12256_x562579235}[：]{style="font-family:宋体"}[Auto]{lang="PT-BR"}[模式，可以通过动态协商转化为]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式或]{style="font-family:宋体"}[E]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[e]{lang="PT-BR"}**]{#struct_0_x9962_12256_x562644771}[：]{style="font-family:宋体"}[E]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[**[f]{lang="SV"}**]{#struct_0_x9962_12256_x562972451}[：]{style="font-family:宋体"}[F]{lang="PT-BR"}[模式。]{style="font-family:
宋体"}

[**[np]{lang="SV"}**]{#struct_0_x9962_12256_x563037987}[：]{style="font-family:宋体"}[NP]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562448164}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_348320044}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x867719326}[交换机只支持]{lang="EN-US" style="font-family:
宋体"}[Auto]{lang="PT-BR"}[模式、]{lang="EN-US" style="font-family:
宋体"}[E]{lang="PT-BR"}[模式和]{lang="EN-US" style="font-family:
宋体"}[F]{lang="PT-BR"}[模式；]{lang="EN-US" style="font-family:
宋体"}[NPV]{lang="FR"}[交换机只支持]{lang="EN-US" style="font-family:宋体"}[F]{lang="PT-BR"}[模式和]{lang="EN-US" style="font-family:宋体"}[NP]{lang="EN-US"}[模式；]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机只支持]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[模式、]{lang="EN-US" style="font-family:宋体"}[F]{lang="PT-BR"}[模式和]{lang="EN-US" style="font-family:宋体"}[NP]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x9962_12256_348254508}[FCF-NPV]{lang="EN-US"}[交换机上，如果用户配置的]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口模式与该接口所属的某个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的工作模式不匹配，则]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口模式的配置在该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下将不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562382628}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x562710308}[配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[工作在]{style="font-family:宋体"}[E]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x562579236}

[\[Sysname\] interface san-aggregation 3]{lang="EN-US"}

[\[Sysname-SAN-Aggregation3\] fc mode e]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1538869676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x532173820}
:::

::: {#-1994619845 .myid}
[]{#_Toc404798081}[]{#struct_0_x9962_12256_1141829864}

**FC和FCoE \-- FC链路聚合配置命令 \-- interface san-aggregation**

------------------------------------------------------------------------

[**[interface san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x562644772}[命令用来创建]{style="font-family:
宋体"}[FC]{lang="EN-US"}[聚合接口并进入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口视图。如果该]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口已经存在，则直接进入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口视图。]{style="font-family:宋体"}

[**[undo interface san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x562972452}[命令用来删除]{style="font-family:
宋体"}[FC]{lang="EN-US"}[聚合接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x563037988}

[**[interface san-aggregation ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x562448165}

[**[undo interface san-aggregation ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x562513701}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562317093}

[[不存在]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x562382629}[聚合接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562710309}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x562775845}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562579237}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x562644773}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x562972453}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x563037989}

[*[interface-numbe]{lang="EN-US"}*[r]{lang="EN-US"}]{#struct_0_x9962_12256_x562448166}[：表示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562513702}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x73105675}[创建]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x562382630}

[\[Sysname\] interface san-aggregation 3]{lang="EN-US"}

[\[Sysname-SAN-Aggregation3\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x863040971}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x562710310}
:::

::: {#1278743515 .myid}
[]{#_Toc404798082}[]{#struct_0_x9962_12256_x562579238}

**FC和FCoE \-- FC链路聚合配置命令 \-- reset counters interface san-aggregation**

------------------------------------------------------------------------

[**[reset counters interface san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x562644774}[命令用来清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562972454}

[**[reset counters interface]{lang="EN-US"}**[ \[ **san-aggregation** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_x563037990}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562448167}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_371358833}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562513703}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x562317095}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x562382631}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562710311}

[**[san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x867719320}[：清除指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x562775847}[：表示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562579239}

[[在某些情况下，需要统计一定时间内某]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x562972455}[接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x1214969127}[和]{lang="EN-US" style="font-family:
宋体"}*[number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x563037991}[而不指定]{lang="EN-US" style="font-family:
宋体"}*[number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{style="font-family:宋体"}**[san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x562448168}[和]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，则清除指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562513704}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x562317096}[清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface san-aggregation 3]{lang="EN-US"}]{#struct_0_x9962_12256_x562382632}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x562710312}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_x562775848}
:::

::: {#1242456314 .myid}
[]{#_Toc404798083}[]{#struct_0_x9962_12256_x562579240}

**FC和FCoE \-- FC链路聚合配置命令 \-- san-aggregation group**

------------------------------------------------------------------------

[**[san-aggregation group]{lang="EN-US"}**]{#struct_0_x9962_12256_x562644776}[命令用来将]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口加入指定的]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组。]{style="font-family:宋体"}

[**[undo san-aggregation group]{lang="EN-US"}**]{#struct_0_x9962_12256_x562972456}[命令用来将]{style="font-family:
宋体"}[FC]{lang="EN-US"}[接口从已加入的]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x563037992}

[**[san-aggregation group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_x9962_12256_197066724}

[**[undo san-aggregation group]{lang="EN-US"}**]{#struct_0_x9962_12256_197001188}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_197197796}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_197132260}[接口未加入任何]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1769152096}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_196739044}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x265792533}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_196935652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_196870116}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196542436}

[*[group-number]{lang="EN-US"}*]{#struct_0_x9962_12256_196476900}[：指定已经存在的]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组所对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的编号。]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组和]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口一一对应、编号相同。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_197066723}

[[需要注意到是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1088595807}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x9962_12256_197001187}[FC]{lang="EN-US"}[接口只能加入一个]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_197197795}[接口加入]{lang="EN-US" style="font-family:
宋体"}[FC]{lang="EN-US"}[聚合组]{lang="EN-US" style="font-family:
宋体"}[后]{style="font-family:宋体"}[，会删除]{lang="EN-US" style="font-family:宋体"}[FC]{lang="EN-US"}[接口下原有的接口模式、]{lang="EN-US" style="font-family:宋体"}[Trunk]{lang="EN-US"}[模式、]{lang="EN-US" style="font-family:宋体"}[Trunk VSAN]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ Access VSAN]{lang="EN-US"}[配置]{lang="EN-US" style="font-family:宋体"}[，也不允许对成员接口做以上配置]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}[FC]{lang="EN-US"}[接口离开]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组后，这些配置也不会恢复，均为缺省配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x9962_12256_197132259}[FC]{lang="EN-US"}[聚合组中可以加入的成员接口数]{style="font-family:宋体"}[量与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196804579}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_196542435}[将]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_197132258}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] san-aggregation group 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196804578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display san-aggregation]{lang="EN-US"}**]{#struct_0_x9962_12256_196739042}
:::

::: {#-1750891528 .myid}
[]{#_Toc404798084}[]{#struct_0_x9962_12256_196935650}[]{#_Toc347837022}

**FC和FCoE \-- FC链路聚合配置命令 \-- san-aggregation load-sharing mode local-first**

------------------------------------------------------------------------

[**[san-aggregation load-sharing mode local-first]{lang="EN-US"}**]{#struct_0_x9962_12256_196870114}[命令用来开启本地转发优先功能。]{style="font-family:宋体"}

[**[undo san-aggregation load-sharing mode local-first]{lang="EN-US"}**]{#struct_0_x9962_12256_196542434}[命令用来关闭本地转发优先功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196476898}

[**[san-aggregation load-sharing mode local-first]{lang="EN-US"}**]{#struct_0_x9962_12256_197066721}

[**[undo san-aggregation load-sharing mode local-first]{lang="EN-US"}**]{#struct_0_x9962_12256_197001185}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_197197793}

[[本地转发优先功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x9962_12256_197132257}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196804577}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_196739041}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196935649}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_196870113}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_196542433}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196476897}

[[采用聚合负载分担的本地转发优先机制可以降低数据流量对]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9962_12256_197066720}[物理端口之间链路的冲击。在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中，如果某成员设备转发报文的出接口为]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口，且对应]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的选中口分布在多个成员设备上，则系统根据该成员设备上的配置进行如下处理：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当该成员设备开启了本地转发优先功能时，如果该成员设备上存在选中口，则只在该成员设备上的各选中口间进行负载分担；如果该成员设备上不存在选中口，则在所有成员设备上的所有选中口间进行负载分担。]{style="font-family:宋体"}]{#struct_0_x9962_12256_197001184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当该成员设备关闭了本地转发优先功能时，将在所有成员设备上的所有选中口间进行负载分担。]{style="font-family:宋体"}]{#struct_0_x9962_12256_197197792}

[[有关]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9962_12256_197132256}[的详细介绍，请参见"虚拟化技术配置指导"中的"]{style="font-family:宋体"}[IRF]{lang="EN-US"}["。]{style="font-family:宋体"}

[[需要注意的是，本地转发优选功能配置后会立即生效，可能造成转发流量丢失。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x951837090}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196804576}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_196739040}[开启本地转发优先功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_196870112}

[\[Sysname\] san-aggregation load-sharing mode local-first]{lang="EN-US"}
:::

::: {#-1365985633 .myid}
[]{#_Toc404798085}[]{#struct_0_x9962_12256_196542432}

**FC和FCoE \-- FC链路聚合配置命令 \-- shutdown (FC aggregate interface view)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x9962_12256_196476896}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x9962_12256_197066719}[命令用来打开当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_197001183}

[**[shutdown]{lang="FR"}**]{#struct_0_x9962_12256_197197791}

[**[undo shutdown]{lang="FR"}**]{#struct_0_x9962_12256_197132255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196804575}

[[接口处于开启状态。]{style="font-family:宋体"}]{#struct_0_x9962_12256_196935647}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x500232304}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_196870111}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_196542431}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_196476895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1369017217}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1369082753}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1368886145}[关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1369279361}

[\[Sysname\] interface san-aggregation 3]{lang="EN-US"}

[\[Sysname-SAN-Aggregation3\] shutdown]{lang="EN-US"}
:::

::: {#-2075199862 .myid}
[]{#_Toc404798087}[]{#struct_0_x9962_12256_x1369148289}

**FC和FCoE \-- FCoE功能配置命令 \-- display fcoe**

------------------------------------------------------------------------

[**[display fcoe]{lang="EN-US"}**]{#struct_0_x9962_12256_x1369213825}[命令用来显示全局的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1369541505}

[**[display fcoe]{lang="EN-US"}**]{#struct_0_x9962_12256_x1369607041}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1369017218}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1369082754}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1368886146}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1368951682}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1369279362}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1369344898}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1369148290}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1088595806}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1384627670}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1369213826}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1369541506}[显示全局的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[配置信息。（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> display fcoe]{lang="EN-US"}]{#struct_0_x9962_12256_x1369017219}

[Global FCoE information:]{lang="EN-US"}

[  FCoE MAC    : 0000-1234-0202]{lang="EN-US"}

[  FC-MAP      : 0x0efc25]{lang="EN-US"}

[  FCF Priority: 128]{lang="EN-US"}

[  FKA period  : 8 seconds]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display fcoe]{lang="EN-US"}]{#struct_0_x9962_12256_x1369082755}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1680889233}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1368886147}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1369279363}

[[Global FCoE information]{lang="EN-US"}]{#struct_0_x9962_12256_1088595811}

[[全局的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x9962_12256_1384824279}[配置信息]{style="font-family:宋体"}

[[FCoE MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x1369148291}

[[交换机的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x1369541507}[地址]{style="font-family:宋体"}

[[FC-MAP]{lang="EN-US"}]{#struct_0_x9962_12256_x1369017220}

[[FC-MAP]{lang="EN-US"}]{#struct_0_x9962_12256_x1368886148}[值]{style="font-family:宋体"}

[[FCF Priority]{lang="EN-US"}]{#struct_0_x9962_12256_x1368951684}

[[系统的]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1369344900}[优先级]{style="font-family:宋体"}

[[FKA period]{lang="EN-US"}]{#struct_0_x9962_12256_x1369213828}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x1369607044}[接口周期性发送发现请求报文和非请求发现通告报文的时间间隔]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1369017221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe fcmap]{lang="EN-US"}**]{#struct_0_x9962_12256_x1369082757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe fka-adv-period]{lang="EN-US"}**]{#struct_0_x9962_12256_x1368886149}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe global fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_x1368951685}

::: {#-879063825 .myid}
[]{#_Toc404798088}[]{#struct_0_x9962_12256_1088595812}

**FC和FCoE \-- FCoE功能配置命令 \-- display fcoe vlan**

------------------------------------------------------------------------

[**[display fcoe vlan]{lang="EN-US"}**]{#struct_0_x9962_12256_1384889815}[命令用来显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1276819924}

[**[display fcoe vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x2046352556}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x538585419}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x165897365}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x340110845}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1296306375}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x732610043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_99410648}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x279813483}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x378636378}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_2100018788}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_785759289}

[[只有]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1088595809}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1385348566}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1054134971}[显示]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[配置信息。（]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> display fcoe]{lang="EN-US"}]{#struct_0_x9962_12256_x793161079}

[FCoE information of VLAN 10:]{lang="EN-US"}

[  FCoE MAC    : 0000-2345-0202]{lang="EN-US"}

[  FC-MAP      : 0x0efc01]{lang="EN-US"}

[  FCF Priority: 128]{lang="EN-US"}

[  FKA period  : 8 seconds]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display fcoe vlan]{lang="EN-US"}]{#struct_0_x9962_12256_977907971}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_547472205}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x70436580}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1088595810}

[[FCoE information of VLAN 10]{lang="EN-US"}]{#struct_0_x9962_12256_1088595815}

[[VLAN 10]{lang="EN-US"}]{#struct_0_x9962_12256_1088595816}[中的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[配置信息]{style="font-family:宋体"}

[[FCoE MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x1250056353}

[[交换机的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x1250056352}[地址]{style="font-family:宋体"}

[[FC-MAP]{lang="EN-US"}]{#struct_0_x9962_12256_x1250056355}

[[FC-MAP]{lang="EN-US"}]{#struct_0_x9962_12256_x1250056354}[值]{style="font-family:宋体"}

[[FCF Priority]{lang="EN-US"}]{#struct_0_x9962_12256_x1250056349}

[[系统的]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1250056348}[优先级]{style="font-family:宋体"}

[[FKA period]{lang="EN-US"}]{#struct_0_x9962_12256_x1250056351}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1958591285}[接口周期性发送发现请求报文和非请求发现通告报文的时间间隔]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1250056350}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe fcmap]{lang="EN-US"}**]{#struct_0_x9962_12256_392507344}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe fka-adv-period]{lang="EN-US"}**]{#struct_0_x9962_12256_1135511851}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe global fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_1616289754}

::: {#1024902430 .myid}
[]{#_Toc404798089}[]{#struct_0_x9962_12256_1689484512}

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe enable**

------------------------------------------------------------------------

[**[fcoe enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1330165414}[命令用来开启]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能并指定映射]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo fcoe enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1166135962}[命令用来关闭]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_767793846}

[**[fcoe enable]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x797639774}

[**[undo fcoe enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1975848182}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1184788689}

[[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1135561009}[内的]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2036431160}

[[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1143554663}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_503274015}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1224145733}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x797443166}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1976514471}

[**[vsan]{lang="EN-US"}***[ vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x2112823145}[：当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，则当前]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[将与同编号的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[相映射。在编号为]{style="font-family:宋体"}[3840]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内则必须指定本参数，否则系统将提示出错。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_404240580}

[[通过]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1369607045}[接口或]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口发送报文时，都需要配置本功能：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1369017222}[FC]{lang="EN-US"}[接口发送报文时，用到的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[都要与某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射，并在该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内开启]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能，目的是让设备可以正常运行]{style="font-family:宋体"}[FC]{lang="EN-US"}[和]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[相关特性。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1971531386}[VFC]{lang="EN-US"}[接口发送报文时，由于其绑定的以太网接口可能同时允许多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[通过，因此需要在其中某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内开启]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能，并将该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[映射，这样该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的报文就会被打上该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[，并在此]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内发送。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1828163066}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许在]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1647807981}[VLAN 1]{lang="EN-US"}[内开启]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x920103354}[与]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[是一一对应的，一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[只能映射一个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，反之亦然。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[链路两端的设备必须通过相同的]{style="font-family:宋体"}]{#struct_0_x9962_12256_x797508702}[VSAN]{lang="EN-US"}[通信：使用]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口时，两端的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[可以与不同的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射；使用]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口时，两端的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[必须与相同的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在某个]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1250056344}[VLAN]{lang="EN-US"}[内开启了]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能后：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[该]{style="font-family:宋体"}]{#struct_0_x9962_12256_420315437}[VLAN]{lang="EN-US"}[内仅转发]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[流量，不转发其它业务流量（如]{style="font-family:宋体"}[IP]{lang="EN-US"}[流量）。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[该]{style="font-family:宋体"}]{#struct_0_x9962_12256_x41426705}[VLAN]{lang="EN-US"}[内的成员端口之间被设置为二层隔离，不会形成广播环路，因此，]{style="font-family:宋体"}[FCoE VLAN]{lang="EN-US"}[内不需要运行生成树协议或其它环路检测协议，否则可能会导致]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[转发链路被阻塞。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[该]{style="font-family:宋体"}]{#struct_0_x9962_12256_x556317039}[VLAN]{lang="EN-US"}[内可以运行二层协议，但由于成员端口之间被设置为二层隔离，因此二层协议将按照端口隔离的拓扑运行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1426275833}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1970804979}[在]{style="font-family:宋体"}[VLAN 4]{lang="EN-US"}[内开启]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[功能，并将该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[VSAN 6]{lang="EN-US"}[相映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x962263440}

[\[Sysname\] vlan 4]{lang="EN-US"}

[\[Sysname-vlan4\] fcoe enable vsan 6]{lang="EN-US"}
:::

::: {#149933874 .myid}
[]{#_Toc404798090}[]{#struct_0_x9962_12256_x2011267473}[]{#_Toc309984781}[]{#_Toc303958368}

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe fcf-priority**

------------------------------------------------------------------------

[**[fcoe fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_x797312094}[命令用来配置]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo fcoe fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_x1201783644}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x144762324}

[**[fcoe fcf-priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x9962_12256_5122109}

[**[undo fcoe fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_1530150163}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1973021439}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x1027379029}[接口的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1304931626}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_x797377630}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1531746939}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_37301120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1217130067}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2089614072}

[*[priority]{lang="EN-US"}*]{#struct_0_x9962_12256_764994685}[：]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，数值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1306431591}

[[发送请求发现通告报文时，报文中的]{style="font-family:宋体"}[fcf priority]{lang="EN-US"}]{#struct_0_x9962_12256_x1188859831}[字段将填写]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级的值。]{style="font-family:宋体"}

[[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_x797181022}[在收到多个]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送的发现通告报文的情况下，将从这些发现通告报文中选择]{style="font-family:宋体"}[fcf priority]{lang="EN-US"}[优先级最高的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[，并向其发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[报文，进行注册。]{style="font-family:宋体"}

[[本配置仅在]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_1550627080}[接口为]{style="font-family:宋体"}[F]{lang="EN-US"}[模式时生效，在]{style="font-family:宋体"}[E]{lang="EN-US"}[模式下可以配置，但不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2075587737}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_781741997}[配置]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x335340815}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] fcoe fcf-priority 12]{lang="EN-US"}
:::

::: {#1723132086 .myid}
[]{#_Toc404798091}[]{#struct_0_x9962_12256_x77667789}[]{#_Toc309984782}[]{#_Toc303958370}[]{#_Toc306290962}[]{#_Toc306290963}[]{#_Toc306290965}

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe fcmap**

------------------------------------------------------------------------

[**[fcoe fcmap]{lang="EN-US"}**]{#struct_0_x9962_12256_x711243312}[命令用来配置]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo fcoe fcmap]{lang="EN-US"}**]{#struct_0_x9962_12256_x657034198}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x797246558}

[**[fcoe fcmap]{lang="EN-US"}**[ *fc-map*]{lang="EN-US"}]{#struct_0_x9962_12256_x1981542731}

[**[undo fcoe fcmap]{lang="EN-US"}**]{#struct_0_x9962_12256_x1935726987}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x10444497}

[[FC-MAP]{lang="EN-US"}]{#struct_0_x9962_12256_x1391541293}[值为]{style="font-family:宋体"}[0x0EFC00]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1641286844}

[[系统视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_1123441854}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1204856818}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x797705309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1138394136}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1657619157}

[*[fc-map]{lang="EN-US"}*]{#struct_0_x9962_12256_934302984}[：]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0x0EFC00]{lang="EN-US"}[～]{style="font-family:宋体"}[0x0EFCFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1137474261}

[[本命令可以在系统视图或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2059360416}[视图下配置，]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机只支持系统视图下的配置，]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机只支持]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下的配置。]{style="font-family:宋体"}

[[FC-MAP]{lang="EN-US"}]{#struct_0_x9962_12256_x864927191}[值用来标识一个]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[网络，所有的交换机必须具有相同的]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[需要注意的是，配置]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}]{#struct_0_x9962_12256_x399814161}[值后，]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口会重新进行]{style="font-family:宋体"}[FIP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_831191315}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x797770845}[配置]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x0EFCFF]{lang="EN-US"}[。（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1478895179}

[\[Sysname\] fcoe fcmap 0efcff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2059360419}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中，配置]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x0EFCFF]{lang="EN-US"}[。（]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_808710984}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] fcoe fcmap 0efcff]{lang="EN-US"}
:::

::: {#-580994586 .myid}
[]{#_Toc404798092}[]{#struct_0_x9962_12256_x1350856235}[]{#_Toc309984783}[]{#_Toc303958369}

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe fka-adv-period**

------------------------------------------------------------------------

[**[fcoe fka-adv-period]{lang="EN-US"}**]{#struct_0_x9962_12256_1141492389}[命令用来配置]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo fcoe fka-adv-period]{lang="EN-US"}**]{#struct_0_x9962_12256_616782372}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_392336674}

[**[fcoe fka-adv-period]{lang="EN-US"}**[ *fka-adv-period*]{lang="EN-US"}]{#struct_0_x9962_12256_1684357571}

[**[undo fcoe fka-adv-period]{lang="EN-US"}**]{#struct_0_x9962_12256_527881574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x797574237}

[[fka-adv-period]{lang="EN-US"}]{#struct_0_x9962_12256_1892939890}[值为]{style="font-family:宋体"}[8]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x536461796}

[[系统视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_1553886720}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x422942616}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x56235276}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1502546482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x366277500}

[*[fka-adv-period]{lang="EN-US"}*]{#struct_0_x9962_12256_x797639773}[：]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1975651574}

[[本命令可以在系统视图或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1094950687}[视图下配置，]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机只支持系统视图下的配置，]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机只支持]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下的配置。]{style="font-family:宋体"}

[[fka-adv-period]{lang="EN-US"}]{#struct_0_x9962_12256_1504100387}[值的作用如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[虚链路建立以后，在]{style="font-family:宋体"}]{#struct_0_x9962_12256_1450845122}[E]{lang="EN-US"}[模式]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口上，交换机以]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[为间隔周期性向外发送非请求发现通告报文来维护建立的虚链路，非请求发现通告报文中携带]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。对端交换机收到非请求发现通告报文后，维持虚链路的状态，并记录]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。如果交换机在]{style="font-family:宋体"}[2.5]{lang="EN-US"}[倍的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[间隔（收到的非请求发现通告报文中携带的值，非本机配置的值）内没有收到非请求发现通告报文，则删除该虚链路。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[虚链路建立以后，在]{style="font-family:宋体"}]{#struct_0_x9962_12256_1496046852}[F]{lang="EN-US"}[模式]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口上，交换机以]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[为间隔周期性向外发送非请求发现通告报文来维护建立的虚链路，非请求发现通告报文中携带]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。对端]{style="font-family:宋体"}[ENode]{lang="EN-US"}[收到非请求发现通告报文后，维持虚链路的状态，并记录]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。如果]{style="font-family:宋体"}[ENode]{lang="EN-US"}[在]{style="font-family:宋体"}[2.5]{lang="EN-US"}[倍的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[间隔内没有收到非请求发现通告报文，则删除该虚链路。同时]{style="font-family:宋体"}[ENode]{lang="EN-US"}[使用记录的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[间隔周期性发送保活报文，交换机收到保活报文后，维持虚链路的状态。如果交换机在]{style="font-family:宋体"}[2.5]{lang="EN-US"}[倍的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[间隔内没有收到保活报文，则删除该虚链路。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NP]{lang="EN-US"}]{#struct_0_x9962_12256_x822394394}[模式的]{lang="EN-US" style="font-family:
宋体"}[VFC]{lang="EN-US"}[接口与]{lang="EN-US" style="font-family:
宋体"}[ENode]{lang="EN-US"}[的行为相同，不受本交换机配置的]{lang="EN-US" style="font-family:
宋体"}[fka-adv-period]{lang="EN-US"}[值的影响，使用从对端交换机学习到的]{lang="EN-US" style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。]{lang="EN-US" style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}]{#struct_0_x9962_12256_354234004}[值时，需要注意：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FC-BB-5]{lang="EN-US"}]{#struct_0_x9962_12256_x1332069650}[标准中规定，]{lang="EN-US" style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[取值上限为]{lang="EN-US" style="font-family:宋体"}[90]{lang="EN-US"}[秒，]{lang="EN-US" style="font-family:宋体"}[H3C]{lang="EN-US"}[交换机的]{lang="EN-US" style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[配置上限为]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[秒，超出了协议规定的取值范围。因此，当]{lang="EN-US" style="font-family:宋体"}[H3C]{lang="EN-US"}[交换机与服务器、存储设备或其他厂商交换机互通时，配置的]{lang="EN-US" style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值不能超出]{lang="EN-US" style="font-family:宋体"}[90]{lang="EN-US"}[秒。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下，使用]{style="font-family:宋体"}]{#struct_0_x9962_12256_810198342}[fka-adv-period]{lang="EN-US"}[的缺省值（]{style="font-family:宋体"}[8]{lang="EN-US"}[秒）即可。在交换机进行主备倒换或者有备用主控板的]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级时，为了保证业务不中断，如果]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[配置较多，则需要适当调大]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值，建议配置为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[90]{lang="EN-US"}[秒之间。关于]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[的详细介绍，请参见"基础配置指导"中的"]{style="font-family:宋体"}[ISSU]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[超出]{style="font-family:宋体"}]{#struct_0_x9962_12256_x797443165}[90]{lang="EN-US"}[秒的配置，建议用户在无备用主控板的]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级时使用。当交换机进行无备用主控板]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级时，由于没有备用主控板的存在，会有较长一段时间无法发送非请求发现通告报文或保活报文，为了使对端设备不会在此期间因超时而删除虚链路，从而保证业务不中断，建议调整]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值到]{style="font-family:宋体"}[300]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[秒之间，使得]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级能够完成。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1976580007}[交换机进行主备倒换或者]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级时，为了保证业务不中断，除了要调整本交换机的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值，还要调整上游]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。这是因为，]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机上的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值，仅影响本机]{style="font-family:宋体"}[F]{lang="EN-US"}[模式]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口和其连接的下游]{style="font-family:宋体"}[Enode]{lang="EN-US"}[的行为。]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口使用的是从上游]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机学习到的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。因此，]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机进行主备倒换或者]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级时，需要同时调整本交换机和上游]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[由于上述配置限制，当无备用主控板的接入]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_833563294}[交换机或]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级时，]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[流量会中断。这是因为接入]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机或]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机连接服务器、存储设备或者其他厂商]{style="font-family:宋体"}[NPV]{lang="EN-US"}[设备，由于互通限制，]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值不能超过]{style="font-family:宋体"}[90]{lang="EN-US"}[秒。由于没有备用主控板存在，]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级需要的时间较长，超过了]{style="font-family:宋体"}[2.5]{lang="EN-US"}[×]{style="font-family:宋体"}[90]{lang="EN-US"}[秒的超时间隔，]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[软重启升级期间虚链路会超时删除，所以，]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[流量会中断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1271588964}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1741165122}[配置]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x397356134}

[\[Sysname\] fcoe fka-adv-period 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2059360418}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中，配置]{style="font-family:宋体"}[fka-adv-period]{lang="EN-US"}[值为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。（]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1920172371}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] fcoe fka-adv-period 20]{lang="EN-US"}
:::

::: {#-1694028016 .myid}
[]{#_Toc404798093}[]{#struct_0_x9962_12256_x920711427}[]{#_Toc309984784}[]{#_Toc303958367}[]{#_Toc306356126}[]{#_Toc306356127}[]{#_Toc306356129}[]{#_Toc306356130}

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe global fcf-priority**

------------------------------------------------------------------------

[**[fcoe global fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_1424455192}[命令用来配置系统的]{style="font-family:
宋体"}[FCF]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo fcoe global fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_x797508701}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_420249901}

[**[fcoe global fcf-priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_x9962_12256_x1648547617}

[**[undo fcoe global fcf-priority]{lang="EN-US"}**]{#struct_0_x9962_12256_x676480282}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_645530246}

[[系统的]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_826678713}[优先级为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x786260596}

[[系统视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_962806848}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x797312093}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1202242396}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_891319790}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_975147880}

[*[priority]{lang="EN-US"}*]{#struct_0_x9962_12256_x851515636}[：]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，数值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_337685346}

[[本命令可以在系统视图或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2059360413}[视图下配置，]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机只支持系统视图下的配置，]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机只支持]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[视图下的配置。]{style="font-family:宋体"}

[[发送非请求发现通告报文时，报文中的]{style="font-family:宋体"}[fcf priority]{lang="EN-US"}]{#struct_0_x9962_12256_x435707982}[字段将填写系统的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级的值。]{style="font-family:宋体"}

[[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_x1954577171}[在收到多个]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送的发现通告报文的情况下，将从这些发现通告报文中选择]{style="font-family:宋体"}[fcf priority]{lang="EN-US"}[优先级最高的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[，并向其发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[报文，进行注册。]{style="font-family:宋体"}

[[本配置对所有]{style="font-family:宋体"}[F]{lang="EN-US"}]{#struct_0_x9962_12256_x976921370}[模式的]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x797377629}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1531157116}[配置系统的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[12]{lang="EN-US"}[。（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1167739095}

[\[Sysname\] fcoe global fcf-priority 12]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2059360412}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中，配置系统的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[12]{lang="EN-US"}[。（]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x401142597}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] fcoe global fcf-priority 12]{lang="EN-US"}
:::

::: {#358501414 .myid}
[]{#_Toc404798095}[]{#struct_0_x9962_12256_x965732695}

**FC和FCoE \-- VSAN配置命令 \-- display vsan port-member**

------------------------------------------------------------------------

[**[display vsan port-member]{lang="EN-US"}**]{#struct_0_x9962_12256_x965798231}[命令用来显示]{style="font-family:
宋体"}[VSAN]{lang="EN-US"}[配置的接口成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x965601623}

[**[display vsan]{lang="EN-US"}**[ \[ *vsan-id* \] **port-member**]{lang="EN-US"}]{#struct_0_x9962_12256_x965667159}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x965994839}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x965863767}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1385988201}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x965929303}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x966322519}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1763150665}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x609528910}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1763281737}

[*[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_1763216201}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[配置的接口成员，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[配置的接口成员。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1762888521}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1762822985}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[配置的接口成员。]{style="font-family:宋体"}

[[\<Sysname\> display vsan port-member]{lang="EN-US"}]{#struct_0_x9962_12256_1763019589}

[VSAN 1:]{lang="EN-US"}

[  Access Ports:]{lang="EN-US"}

[    Fc1/0/1              Fc1/0/2           Fc1/0/3]{lang="EN-US"}

[    Fc1/0/4              Fc1/0/5           Fc1/0/6]{lang="EN-US"}

[  Trunk Ports:]{lang="EN-US"}

[    Fc1/0/4              Fc1/0/5           Fc1/0/6]{lang="EN-US"}

[    Vfc2]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSAN 2:]{lang="EN-US"}

[  Access Ports:]{lang="EN-US"}

[  Trunk Ports:]{lang="EN-US"}

[    Fc1/0/4]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSAN 10:]{lang="EN-US"}

[  Access Ports:]{lang="EN-US"}

[  Trunk Ports:]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSAN 100:]{lang="EN-US"}

[  Access Ports:]{lang="EN-US"}

[  Trunk Ports:]{lang="EN-US"}

[    Fc1/0/4              Fc1/0/5           Fc1/0/6]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display vsan port-member]{lang="FR"}]{#struct_0_x9962_12256_1763150660}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1664484341}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1763216196}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1762822980}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1762954052}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1762560836}[编号]{style="font-family:宋体"}

[[Access Ports]{lang="EN-US"}]{#struct_0_x9962_12256_1810335904}

[[Access]{lang="EN-US"}]{#struct_0_x9962_12256_1809942688}[接口]{style="font-family:宋体"}

[[Trunk Ports]{lang="EN-US"}]{#struct_0_x9962_12256_1810073760}

[[Trunk]{lang="EN-US"}]{#struct_0_x9962_12256_1809680544}[接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1318374911 .myid}
[]{#_Toc404798096}[]{#struct_0_x9962_12256_x2059360415}

**FC和FCoE \-- VSAN配置命令 \-- display vsan status**

------------------------------------------------------------------------

[**[display vsan]{lang="EN-US"}**[ **status**]{lang="EN-US"}]{#struct_0_x9962_12256_x804427124}[命令用来显示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1878110411}

[**[display vsan]{lang="EN-US"}**[ \[ *vsan-id* \] **status**]{lang="EN-US"}]{#struct_0_x9962_12256_129171190}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1651106737}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1364956848}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1232784952}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x932232621}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x2059360414}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_761656817}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x456618004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1066178467}

[*[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x195973417}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的状态信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1284360378}

[[只有]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_59144084}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2021366208}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x836682362}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display vsan status]{lang="EN-US"}]{#struct_0_x9962_12256_1380961293}

[VSAN 1:]{lang="EN-US"}

[  Name: VSAN0001]{lang="EN-US"}

[  Working mode: NPV]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSAN 10:]{lang="EN-US"}

[  Name: VSAN0010]{lang="EN-US"}

[  Working mode: NPV]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display vsan ]{lang="FR"}[status]{lang="EN-US"}]{#struct_0_x9962_12256_x287905041}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_538841701}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2059360409}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x103045281}

[[VSAN 1]{lang="EN-US"}]{#struct_0_x9962_12256_x103045280}

[[VSAN 1]{lang="EN-US"}]{#struct_0_x9962_12256_x103045283}[的状态信息]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x9962_12256_x103045282}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x103045277}[的名称]{style="font-family:宋体"}

[[Working mode]{lang="EN-US"}]{#struct_0_x9962_12256_x103045276}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x103045279}[的工作模式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x103045273}[：]{lang="EN-US" style="font-family:宋体"}[FCF]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x103045272}[：]{lang="EN-US" style="font-family:宋体"}[NPV]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_664942466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsan]{lang="EN-US"}**]{#struct_0_x9962_12256_x2059644166}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x1226105674}

::: {#1212291552 .myid}
[]{#_Toc404798097}[]{#struct_0_x9962_12256_1810204831}

**FC和FCoE \-- VSAN配置命令 \-- port**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**]{#struct_0_x9962_12256_1810139295}[命令用来将接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式批量加入当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo port]{lang="EN-US"}**]{#struct_0_x9962_12256_1810335903}[命令用来将多个从当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中批量删除接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1810270367}

[**[port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_1809942687}

[**[undo port]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_1810073759}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1810008223}

[[接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}]{#struct_0_x9962_12256_1809680543}[方式属于]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1809615007}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1810204830}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1810139294}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1810270366}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1809942686}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1809877150}

[*[interface-list]{lang="EN-US"}*]{#struct_0_x9962_12256_1810073758}[：接口列表，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type interface-number1* \[ **to** *interface-type interface-number2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。接口类型可以是]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口或]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1810008222}

[[用户既可使用本命令在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1481746271}[视图下将]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口或]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式批量加入当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，也可使用]{style="font-family:宋体"}**[port]{lang="EN-US"}**[ **access vsan**]{lang="EN-US"}[命令在]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口或]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口视图下将当前接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式加入指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1810204829}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1810073757}[将接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[～]{style="font-family:宋体"}[FC1/0/10]{lang="EN-US"}[以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式批量加入]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1810008220}

[\[Sysname\] vsan 10]{lang="EN-US"}

[\[Sysname-vsan10\] port fc 1/0/1 to fc 1/0/10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1809680540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port]{lang="EN-US"}**[ **access vsan**]{lang="EN-US"}]{#struct_0_x9962_12256_1810204827}
:::

::: {#-1888864469 .myid}
[]{#_Toc404798098}[]{#struct_0_x9962_12256_1810139291}

**FC和FCoE \-- VSAN配置命令 \-- port access vsan**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**[ **access vsan**]{lang="EN-US"}]{#struct_0_x9962_12256_1810335899}[命令用来将当前接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式加入指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo port access vsan]{lang="EN-US"}**]{#struct_0_x9962_12256_1810270363}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1809877147}

[**[port access vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1810073755}

[**[undo port access vsan]{lang="EN-US"}**]{#struct_0_x9962_12256_1810008219}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1809615003}

[[接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}]{#struct_0_x9962_12256_244120891}[方式属于]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_244055355}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_244186427}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_243858747}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_243989819}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_243924283}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_243596603}

[*[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_243531067}[：]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[必须是设备上已经创建的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，否则，该命令将执行失败。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_244120890}

[[用户既可使用本命令在]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1481746272}[接口或]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口视图下将当前接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式加入指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，也可使用]{style="font-family:宋体"}**[port]{lang="EN-US"}**[命令在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图下将]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口或]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式批量加入当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。二者的配置优先级相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_244186426}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_243924282}[创建]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[，并将接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[以]{style="font-family:宋体"}[Access]{lang="EN-US"}[方式加入该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_243858745}

[\[Sysname\] vsan 10]{lang="EN-US"}

[\[Sysname-vsan10\] quit]{lang="EN-US"}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] port access vsan 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_243793209}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port]{lang="EN-US"}**]{#struct_0_x9962_12256_243924281}
:::

::: {#-569839150 .myid}
[]{#_Toc404798099}[]{#struct_0_x9962_12256_243596601}

**FC和FCoE \-- VSAN配置命令 \-- port trunk mode**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**[ **trunk mode**]{lang="EN-US"}]{#struct_0_x9962_12256_243531065}[命令用来配置当前接口的]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[undo port trunk mode]{lang="EN-US"}**]{#struct_0_x9962_12256_244120888}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_244251960}

[**[port trunk mode]{lang="FR"}**]{#struct_0_x9962_12256_244186424}[ { **auto** \| **off** \| **on** }]{lang="FR"}

[**[undo port trunk mode]{lang="FR"}**]{#struct_0_x9962_12256_243858744}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_243793208}

[[接口的]{style="font-family:宋体"}[Trunk]{lang="EN-US"}]{#struct_0_x9962_12256_243924280}[模式为]{style="font-family:宋体"}[Auto]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_243596600}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_244120887}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_244055351}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_244251959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_243858743}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_243793207}

[**[auto]{lang="EN-US"}**]{#struct_0_x9962_12256_243989815}[：表示]{style="font-family:宋体"}[Auto]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[off]{lang="EN-US"}**]{#struct_0_x9962_12256_243924279}[：表示]{style="font-family:宋体"}[Off]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[on]{lang="EN-US"}**]{#struct_0_x9962_12256_243531063}[：表示]{style="font-family:宋体"}[On]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_244120886}

[[互连的两个接口通过]{style="font-family:宋体"}[EVFP]{lang="EN-US"}]{#struct_0_x9962_12256_244186422}[协议，根据本命令所配置的]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[模式来协商接口是否支持]{style="font-family:宋体"}[VSAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_243596598}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1648110968}[配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[模式为]{style="font-family:宋体"}[On]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1648242039}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] port trunk mode on]{lang="EN-US"}
:::

::: {#-649614649 .myid}
[]{#_Toc404798100}[]{#struct_0_x9962_12256_1648045431}

**FC和FCoE \-- VSAN配置命令 \-- port trunk vsan**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**[ **trunk vsan**]{lang="EN-US"}]{#struct_0_x9962_12256_1648110967}[命令用来将当前接口以]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[方式加入]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo port trunk vsan]{lang="EN-US"}**]{#struct_0_x9962_12256_1647455607}[命令用来取消将当前接口以]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[方式加入]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1647914358}

[**[port]{lang="EN-US"}**[ **trunk vsan** *vsan-id-list*]{lang="EN-US"}]{#struct_0_x9962_12256_1647979894}

[**[undo port]{lang="EN-US"}**[ **trunk vsan** *vsan-id-list*]{lang="EN-US"}]{#struct_0_x9962_12256_1647783286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1648176502}

[[接口不以]{style="font-family:宋体"}[Trunk]{lang="EN-US"}]{#struct_0_x9962_12256_1648242038}[方式属于任何]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1648045430}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1647455606}[接口视图]{style="font-family:宋体"}[/VFC]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1647914357}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1647979893}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1647783285}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1648176501}

[*[vsan-id-list]{lang="EN-US"}*]{#struct_0_x9962_12256_1648242037}[：]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[列表，为]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[接口加入的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的范围，表示方式为]{style="font-family:宋体"}*[vsan-id-list = ]{lang="EN-US"}*[{ *vsan-id1* \[ **to** *vsan-id2* \] }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1481746275}

[[在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x233676722}[交换机上配置本命令时，在指定的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[列表中不建议同时包含]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式和]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。否则，]{style="font-family:宋体"}[E_Port]{lang="EN-US"}[将只选择]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[生效，]{style="font-family:宋体"}[NP_Port]{lang="EN-US"}[将只选择]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1648045429}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1647914356}[配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[允许]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1647390068}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] port trunk vsan 1 to 2 10 20 to 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1647455604}[配置接口]{style="font-family:宋体"}[VFC1]{lang="EN-US"}[允许]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1647979891}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] port trunk vsan 1 to 2 10 20 to 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1740113507}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x434215481}
:::

::: {#1579937519 .myid}
[]{#_Toc404798101}[]{#struct_0_x9962_12256_1647783283}

**FC和FCoE \-- VSAN配置命令 \-- vsan**

------------------------------------------------------------------------

[**[vsan]{lang="EN-US"}**]{#struct_0_x9962_12256_1647848819}[命令用来创建]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[并进入]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[已创建，则该命令直接用来进入该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[**[undo vsan]{lang="EN-US"}**]{#struct_0_x9962_12256_1648176499}[命]{style="font-family:宋体"}[令用来删除]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1648045427}

[**[vsan]{lang="EN-US"}**[ *vsan-id* \[ **name** *vsan-name* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1648110963}

[**[undo vsan]{lang="EN-US"}**[ *vsan-id* \[ **name** \]]{lang="EN-US"}]{#struct_0_x9962_12256_1647455603}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_81830419}

[[只存在默认]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_81895955}[（]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_81764883}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_82092563}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_81961491}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_82027027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_81306131}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_81830418}

[*[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_81895954}[：]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *vsan-name*]{lang="EN-US"}]{#struct_0_x9962_12256_1481746276}[：]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$ - \^ \_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。如果创建]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[时没有指定名称，则]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的默认名称由字符串"]{style="font-family:宋体"}[VSAN]{lang="EN-US"}["和]{style="font-family:宋体"}[4]{lang="EN-US"}[位数字的]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[组合而成。例如，]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[的默认名称为"]{style="font-family:宋体"}[VSAN0010]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_81699346}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x233742258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[初始情况下，只存在默认]{style="font-family:宋体"}]{#struct_0_x9962_12256_81764882}[VSAN]{lang="EN-US"}[（]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[），用户不能创建或删除默认]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。用户可以创建的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[范围是]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每台设备上包括默认]{style="font-family:宋体"}]{#struct_0_x9962_12256_82158098}[VSAN]{lang="EN-US"}[在内，最多可以配置的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[数目与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x9962_12256_x2137404439}**[undo vsan]{lang="EN-US"}**[命令时，如果指定了]{style="font-family:宋体"}**[name]{lang="EN-US"}**[参数，则将]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的名称恢复为缺省名称，如果未指定]{style="font-family:宋体"}**[name]{lang="EN-US"}**[参数，则删除该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_81961490}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_82027026}[创建]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_81371666}

[\[Sysname\] vsan 10]{lang="EN-US"}

[\[Sysname-vsan10\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1637629760}[修改已创建]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[的名称为]{style="font-family:宋体"}[FCF-VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1481746273}

[\[Sysname\] vsan 10 name ]{lang="EN-US"}[FCF-VSAN]{lang="EN-US"}

[\[Sysname-vsan10\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x234069938}[创建]{style="font-family:宋体"}[VSAN 11]{lang="EN-US"}[，为其配置名称为]{style="font-family:宋体"}[FCF-VSAN]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSAN 11]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x698150419}

[\[Sysname\] vsan 11 name ]{lang="EN-US"}[FCF-VSAN]{lang="EN-US"}

[\[Sysname-vsan11\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x767548000}[将]{style="font-family:宋体"}[VSAN 11]{lang="EN-US"}[的名称恢复为缺省名称。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x807961524}

[\[Sysname\] undo vsan 11 name]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1151755872}[删除]{style="font-family:宋体"}[VSAN 11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1535648336}

[\[Sysname\] undo vsan 11]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1033955564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vsan status]{lang="EN-US"}**]{#struct_0_x9962_12256_x815936273}
:::

::: {#-1703494206 .myid}
[]{#_Toc404798102}[]{#struct_0_x9962_12256_x174343117}[]{#_Toc384217985}

**FC和FCoE \-- VSAN配置命令 \-- working-mode**

------------------------------------------------------------------------

[**[working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1000896186}[命令用来配置]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的工作模式。]{style="font-family:宋体"}

[**[undo working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x1358427104}[命]{style="font-family:宋体"}[令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x631567004}

[**[working-mode ]{lang="EN-US"}**[{ **fcf** \| **npv** }]{lang="EN-US"}]{#struct_0_x9962_12256_1248494754}

[**[undo working-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_x1004441375}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1491788719}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1481746274}[的工作模式为]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x233611186}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_610758210}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1605180522}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1251531828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_111328050}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x9962_12256_6096231}

[**[fcf]{lang="EN-US"}**]{#struct_0_x9962_12256_398513006}[：表示]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[npv]{lang="EN-US"}**]{#struct_0_x9962_12256_x675647785}[：表示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_379603407}

[[只有]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1499079313}[交换机支持本命令。]{style="font-family:宋体"}

[[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_173489977}[交换机在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中的工作模式又可分为以下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_734086230}[模式：工作在本模式下的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，相当于一台独立的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x667925982}[模式：工作在本模式下的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，相当于一台独立的]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机。]{style="font-family:宋体"}

[[需要注意的是，在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x278894409}[交换机上，如果用户配置的接口模式与该接口所属的某个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的工作模式不匹配，则]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口模式的配置在该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下将不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1582574225}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1481746279}[配置]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[的工作模式为]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x234463154}

[\[Sysname\] vsan 10]{lang="EN-US"}

[\[Sysname-vsan10\] working-mode fcf]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1636980529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vsan status]{lang="EN-US"}**]{#struct_0_x9962_12256_x364506123}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fc ]{lang="EN-US"}[mode]{lang="EN-US"}**]{#struct_0_x9962_12256_322886853}
:::

::: {#-1359881240 .myid}
[]{#_Toc297038079}[]{#_Toc290886987}[]{#_Toc239584268}[]{#_Toc404798104}[]{#struct_0_x9962_12256_1794435317}

**FC和FCoE \-- Fabric网络命令 \-- allowed-domain-id**

------------------------------------------------------------------------

[**[allowed-domain-id]{lang="EN-US"}**]{#struct_0_x9962_12256_458012154}[命令用来配置交换机允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **allowed-domain-id**]{lang="EN-US"}]{#struct_0_x9962_12256_1522587300}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1086734687}

[**[allowed-domain-id]{lang="EN-US"}**[ *domain-id-list*]{lang="EN-US"}]{#struct_0_x9962_12256_x591181567}

[**[undo allowed-domain-id ]{lang="EN-US"}***[domain-id-list]{lang="EN-US"}*]{#struct_0_x9962_12256_2040312068}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2019511674}

[[交换机允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_768378631}[范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[239]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1053705819}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1043800662}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1258260334}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x890690224}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x845732251}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x73455560}

[*[domain-id-list]{lang="EN-US"}*]{#struct_0_x9962_12256_x17392788}[：域]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表，表示允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围。表示方式为]{style="font-family:宋体"}*[domain-id-list]{lang="EN-US"}*[ = { *domain-id1* \[ **to** *domain-id2* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[domain-id1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[domain-id2]{lang="EN-US"}*[为域]{style="font-family:宋体"}[ID]{lang="EN-US"}[的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[239]{lang="EN-US"}[，]{style="font-family:宋体"}*[domain-id2]{lang="EN-US"}*[必须大于等于]{style="font-family:宋体"}*[domain-id1]{lang="EN-US"}*[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_768313095}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1481746280}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[在网络地址分配时，每个]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1232314929}[交换机都会分配到一个域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，域]{style="font-family:宋体"}[ID]{lang="EN-US"}[的默认有效范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[239]{lang="EN-US"}[，可以通过配置，指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[交换机允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围。]{style="font-family:宋体"}

[[配置允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_x509891812}[范围对交换机的影响如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主交换机：只能从允许的域]{style="font-family:宋体"}]{#struct_0_x9962_12256_1086547585}[ID]{lang="EN-US"}[范围内分配域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。如果配置的允许域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围不包含已分配的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[和本地配置的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，配置均会失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非主交换机：手工配置的域]{style="font-family:宋体"}]{#struct_0_x9962_12256_1208210600}[ID]{lang="EN-US"}[必须在允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围内，否则会配置失败。主交换机为本交换机分配的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[必须在允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围内，否则不接受所分配的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，并隔离连接主交换机的接口。如果交换机当前运行时域]{style="font-family:宋体"}[ID]{lang="EN-US"}[（动态分配或者手工指定域]{style="font-family:宋体"}[ID]{lang="EN-US"}[后，交换机实际使用的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[）不在新配置的允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围内时，将导致配置失败。]{style="font-family:宋体"}

[[建议为一个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x435805140}[内的所有交换机都配置相同的允许域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1587897332}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x499549901}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置交换机允许的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_768509703}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] allowed-domain-id 3 to 10]{lang="EN-US"}
:::

::: {#-987591484 .myid}
[]{#_Toc404798105}[]{#struct_0_x9962_12256_x839633726}[]{#_Toc367888083}[]{#_Toc369076427}[]{#_Toc367888084}[]{#_Toc369076428}[]{#_Toc367888085}[]{#_Toc369076429}[]{#_Toc367888086}[]{#_Toc369076430}[]{#_Toc367888087}[]{#_Toc369076431}[]{#_Toc367888088}[]{#_Toc369076432}[]{#_Toc367888089}[]{#_Toc369076433}[]{#_Toc367888090}[]{#_Toc369076434}[]{#_Toc367888091}[]{#_Toc369076435}[]{#_Toc367888092}[]{#_Toc369076436}[]{#_Toc367888093}[]{#_Toc369076437}[]{#_Toc367888094}[]{#_Toc369076438}[]{#_Toc367888095}[]{#_Toc369076439}[]{#_Toc367888096}[]{#_Toc369076440}[]{#_Toc367888097}[]{#_Toc369076441}[]{#_Toc367888098}[]{#_Toc369076442}[]{#_Toc367888099}[]{#_Toc369076443}[]{#_Toc367888100}[]{#_Toc369076444}[]{#_Toc367888101}[]{#_Toc369076445}[]{#_Toc367888102}[]{#_Toc369076446}[]{#_Toc367888103}[]{#_Toc369076447}[]{#_Toc367888104}[]{#_Toc369076448}[]{#_Toc367888105}[]{#_Toc369076449}[]{#_Toc367888106}[]{#_Toc369076450}[]{#_Toc367888107}[]{#_Toc369076451}[]{#_Toc367888108}[]{#_Toc369076452}[]{#_Toc367888109}[]{#_Toc369076453}[]{#_Toc367888110}[]{#_Toc369076454}[]{#_Toc367888111}[]{#_Toc369076455}[]{#_Toc367888112}[]{#_Toc369076456}[]{#_Toc367888113}[]{#_Toc369076457}[]{#_Toc367888114}[]{#_Toc369076458}[]{#_Toc367888115}[]{#_Toc369076459}[]{#_Toc367888116}[]{#_Toc369076460}[]{#_Toc367888117}[]{#_Toc369076461}[]{#_Toc367888118}[]{#_Toc369076462}[]{#_Toc367888119}[]{#_Toc369076463}[]{#_Toc367888120}[]{#_Toc369076464}[]{#_Toc367888121}[]{#_Toc369076465}[]{#_Toc367888122}[]{#_Toc369076466}[]{#_Toc367888123}[]{#_Toc369076467}[]{#_Toc367888124}[]{#_Toc369076468}[]{#_Toc367888125}[]{#_Toc369076469}[]{#_Toc367888126}[]{#_Toc369076470}[]{#_Toc367888127}[]{#_Toc369076471}[]{#_Toc367888128}[]{#_Toc369076472}[]{#_Toc367888129}[]{#_Toc369076473}[]{#_Toc367888130}[]{#_Toc369076474}[]{#_Toc367888131}[]{#_Toc369076475}[]{#_Toc367888132}[]{#_Toc369076476}[]{#_Toc367888133}[]{#_Toc369076477}[]{#_Toc367888134}[]{#_Toc369076478}[]{#_Toc367888135}[]{#_Toc369076479}[]{#_Toc367888136}[]{#_Toc369076480}[]{#_Toc367888137}[]{#_Toc369076481}[]{#_Toc367888138}[]{#_Toc369076482}[]{#_Toc367888139}[]{#_Toc369076483}[]{#_Toc367888140}[]{#_Toc369076484}[]{#_Toc367888141}[]{#_Toc369076485}

**FC和FCoE \-- Fabric网络命令 \-- display fc domain**

------------------------------------------------------------------------

[**[display fc domain]{lang="EN-US"}**]{#struct_0_x9962_12256_768837383}[命令用来显示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的域信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1794435312}

[**[display fc domain]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_457815546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x346915471}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_502248413}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x567389963}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1239347391}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_957134694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_768378632}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1053705822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1043341909}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_621913268}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的域信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的域信息。在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机上，只能显示]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的域信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1259404817}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x856905889}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1440633376}[下的域信息，主要包含以下内容：本交换机运行时信息、本交换机配置信息以及主交换机运行时信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2120077042}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_517714632}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的域信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc domain vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_768313096}

[Domain Information of VSAN 1:]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Running time information:]{lang="EN-US"}

[        State: Stable]{lang="EN-US"}

[        Switch WWN: 41:6e:64:69:61:6d:6f:21]{lang="EN-US"}

[        Fabric name: 41:6e:64:69:61:6d:6f:21]{lang="EN-US"}

[        Priority: 2]{lang="EN-US"}

[        Domain ID: 100]{lang="EN-US"}

[    Configuration information:]{lang="EN-US"}

[        Domain configure: Enabled]{lang="EN-US"}

[        Domain auto-reconfigure: Disabled]{lang="EN-US"}

[        Fabric name: 41:6e:64:69:61:6d:6f:21]{lang="EN-US"}

[        Priority: 128]{lang="EN-US"}

[        Domain ID: 100 (static)]{lang="EN-US"}

[    Principal switch running time information:]{lang="EN-US"}

[        Priority: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Path               Interface]{lang="EN-US"}

[    Downstream         Fc1/0/1]{lang="EN-US"}

[    Downstream         Fc1/0/2]{lang="EN-US"}

[    Downstream         Fc1/0/4]{lang="EN-US"}

[]{#struct_0_x9962_12256_x1232314930}[[表1-20 ]{lang="EN-US"}[display fc domain]{lang="EN-US"}]{#_Toc233714470}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1277371593}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_768509704}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1816413248}

[[Domain Information of VSAN 1]{lang="EN-US"}]{#struct_0_x9962_12256_x1103865378}

[[VSAN 1]{lang="EN-US"}]{#struct_0_x9962_12256_x553905682}[内的域信息]{style="font-family:宋体"}

[[Running time information]{lang="EN-US"}]{#struct_0_x9962_12256_373074926}

[[本交换机运行时信息]{style="font-family:宋体"}]{#struct_0_x9962_12256_1366375678}

[[State]{lang="EN-US"}]{#struct_0_x9962_12256_768444168}

[[本交换机运行状态，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_937873818}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stable]{lang="EN-US"}]{#struct_0_x9962_12256_x1361728034}[：]{style="font-family:宋体"}[表示配置结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unstable]{lang="EN-US"}]{#struct_0_x9962_12256_1251150942}[：]{style="font-family:宋体"}[表示配置还未结束]{lang="EN-US" style="font-family:宋体"}

[[Switch WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1251288310}

[[本交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x782251478}

[[Fabric name]{lang="EN-US"}]{#struct_0_x9962_12256_768640776}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_1168161490}[网络的名称]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x9962_12256_1759103041}

[[本交换机的运行优先级]{style="font-family:宋体"}]{#struct_0_x9962_12256_2144651044}

[[Domain ID]{lang="EN-US"}]{#struct_0_x9962_12256_1929292854}

[[本交换机的运行域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_768575240}

[[Configuration information]{lang="EN-US"}]{#struct_0_x9962_12256_x1785302032}

[[本交换机配置信息]{style="font-family:宋体"}]{#struct_0_x9962_12256_x2049655705}

[[Domain configure]{lang="EN-US"}]{#struct_0_x9962_12256_x1885522783}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_768771848}[配置功能开启情况，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x9962_12256_2046015558}[：]{style="font-family:宋体"}[表示开启]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x9962_12256_x1097672311}[：]{style="font-family:宋体"}[表示关闭]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能]{lang="EN-US" style="font-family:宋体"}

[[Domain auto-reconfigure]{lang="EN-US"}]{#struct_0_x9962_12256_x688041467}

[[自动重配置功能开启情况，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_768706312}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x9962_12256_x1889801906}[：]{style="font-family:宋体"}[表示交换机开启自动重配置功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x9962_12256_x27970445}[：]{style="font-family:宋体"}[表示交换机关闭自动重配置功能]{lang="EN-US" style="font-family:宋体"}

[[Fabric name]{lang="EN-US"}]{#struct_0_x9962_12256_x782969589}

[[本交换机上配置的]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_1270486297}[网络的名称]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x9962_12256_768902920}

[[本交换机上配置的优先级]{style="font-family:宋体"}]{#struct_0_x9962_12256_x2067780178}

[[Domain ID]{lang="EN-US"}]{#struct_0_x9962_12256_1663938130}

[[本交换机上配置的域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_833531341}[。括号中内容的含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static]{lang="EN-US"}]{#struct_0_x9962_12256_768837384}[：]{style="font-family:宋体"}[表示该域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[是静态模式的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[preferred]{lang="EN-US"}]{#struct_0_x9962_12256_1794435315}[：]{style="font-family:宋体"}[表示该域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[是可选模式的]{lang="EN-US" style="font-family:宋体"}

[[Principal switch running time information]{lang="EN-US"}]{#struct_0_x9962_12256_457881082}

[[主交换机运行时信息]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1953227107}

[[Priority]{lang="EN-US"}]{#struct_0_x9962_12256_768378629}

[[主交换机的运行优先级]{style="font-family:宋体"}]{#struct_0_x9962_12256_x902609325}

[[Path]{lang="EN-US"}]{#struct_0_x9962_12256_1519454997}

[[接口路径类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_768313093}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Upstream]{lang="EN-US"}]{#struct_0_x9962_12256_x1232314935}[：]{style="font-family:宋体"}[表示上游主链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Downstream]{lang="EN-US"}]{#struct_0_x9962_12256_x2123095456}[：]{style="font-family:宋体"}[表示下游主链路]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1114709048}

[[本地的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_768509701}[接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-429294412 .myid}
[]{#_Toc404798106}[]{#struct_0_x9962_12256_x1816413251}[]{#_Toc326572986}[]{#_Toc326572987}[]{#_Toc326572988}[]{#_Toc326572989}[]{#_Toc326572990}

**FC和FCoE \-- Fabric网络命令 \-- display fc domain-list**

------------------------------------------------------------------------

[**[display fc domain-list]{lang="EN-US"}**]{#struct_0_x9962_12256_1981313873}[命令用来显示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内动态分配的域列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1177681159}

[**[display fc domain-list]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x812694958}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_384804174}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_406826987}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_768444165}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_937873823}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_212250073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1183393663}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_480641784}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1173983936}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x967794777}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内动态分配的域列表，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内动态分配的域列表。在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机上，只能显示]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内动态分配的域列表。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x659819566}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x856905890}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[在开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_768640773}[配置功能、动态建立]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络时，使用本命令可以查看]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内动态分配的域列表信息，包括域的总数目、域]{style="font-family:宋体"}[ID]{lang="EN-US"}[和交换机]{style="font-family:宋体"}[WWN]{lang="EN-US"}[的对应关系。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1168161495}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1759430721}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内动态分配的域列表。]{style="font-family:宋体"}

[[\<Sysname\> display fc domain-list vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_x990436210}

[Domain list of VSAN 1:]{lang="EN-US"}

[  Number of domains: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Domain ID    WWN]{lang="EN-US"}

[  0xc8(200)    20:01:00:05:30:00:47:df \[Principal\]]{lang="EN-US"}

[  0x63(99)     20:01:00:0d:ec:08:60:c1 \[Local\]]{lang="EN-US"}

[  0x61(97)     50:00:53:0f:ff:f0:10:06 ]{lang="EN-US"}

[]{#struct_0_x9962_12256_90247002}[[表1-21 ]{lang="EN-US"}[display fc domain-list]{lang="EN-US"}]{#_Toc233714471}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1302031389}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1077009142}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_768575237}

[[Domain list of VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x211323923}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2060815251}[内的域列表]{style="font-family:宋体"}

[[Number of domains]{lang="EN-US"}]{#struct_0_x9962_12256_x1846358932}

[[域的总数目]{style="font-family:宋体"}]{#struct_0_x9962_12256_1997840917}

[[Domain ID]{lang="EN-US"}]{#struct_0_x9962_12256_768771845}

[[域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_2046015561}

[[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1097082486}

[[交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_458290516}[。]{style="font-family:宋体"}[Principal]{lang="EN-US"}[表示主交换机，]{style="font-family:宋体"}[Local]{lang="EN-US"}[表示本地交换机]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_581347370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain configure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_745051860}

::: {#1990701447 .myid}
[]{#_Toc291054594}[]{#_Toc404798107}[]{#struct_0_x9962_12256_x883380288}[]{#_Toc312748297}[]{#_Toc258485911}

**FC和FCoE \-- Fabric网络命令 \-- display fc ess**

------------------------------------------------------------------------

[**[display fc ess]{lang="EN-US"}**]{#struct_0_x9962_12256_768706309}[命令用来显示]{style="font-family:宋体"}[ESS]{lang="EN-US"}[（]{style="font-family:宋体"}[Exchange Switch Support]{lang="EN-US"}[，交换机能力协商）协商结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_448850265}

[**[display fc ess]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_811759967}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1406185821}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1022541402}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_315074319}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1580744998}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1304999783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_768902917}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x493802063}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1378927247}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1610461078}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[ESS]{lang="EN-US"}[协商结果，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[ESS]{lang="EN-US"}[协商结果。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1908838404}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_105826523}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看]{style="font-family:宋体"}[ESS]{lang="EN-US"}]{#struct_0_x9962_12256_739821498}[协商结果，包括本交换机的能力和完成]{style="font-family:宋体"}[ESS]{lang="EN-US"}[协商的远端交换机的能力。]{style="font-family:宋体"}

[[关于各种交换机能力的详细介绍请查看相关的协议文档。]{style="font-family:宋体"}]{#struct_0_x9962_12256_1959989593}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1501189168}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_768837381}[显示]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[ESS]{lang="EN-US"}[协商结果。]{style="font-family:宋体"}

[[\<Sysname\> display fc ess vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_1794435310}

[ESS info of VSAN 2:]{lang="EN-US"}

[  Domain: 210]{lang="EN-US"}

[    Directory Server Capability:]{lang="EN-US"}

[      Accept large name server objects: Yes]{lang="EN-US"}

[      Accept small name server objects: No]{lang="EN-US"}

[      Accept large + FC-4 Features name server objects: No]{lang="EN-US"}

[      Accept small + FC-4 Features name server objects: No]{lang="EN-US"}

[      Support receiving ACCept with 0 length: Yes]{lang="EN-US"}

[    Fabric Controller Capability:]{lang="EN-US"}

[     Support receiving the SW_RSCN Request: Yes]{lang="EN-US"}

[    Fabric Configuration Server Capability:]{lang="EN-US"}

[      Support basic configuration services: Yes]{lang="EN-US"}

[      Support platform configuration services: No]{lang="EN-US"}

[      Support topology discovery configuration services: Yes]{lang="EN-US"}

[      Support enhanced configuration services: Yes]{lang="EN-US"}

[    Enhanced Zone Server Capability:]{lang="EN-US"}

[      Support enhanced zoning management: Yes]{lang="EN-US"}

[]{#struct_0_x9962_12256_457684474}[[表1-22 ]{lang="EN-US"}[display fc ess]{lang="EN-US"}]{#_Toc250649774}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1304062641}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_768378630}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1053705820}

[[ESS info of VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1043210837}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_2066318830}[内的]{style="font-family:宋体"}[ESS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Domain]{lang="EN-US"}]{#struct_0_x9962_12256_1818272209}

[[交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_1105271857}

[[Directory Server Capability]{lang="EN-US"}]{#struct_0_x9962_12256_768313094}

[[目录服务器能力列表]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1232314928}

[[Accept large name server objects]{lang="EN-US"}]{#struct_0_x9962_12256_1056192129}

[[交换机是否支持接收大模式的名称服务对象：]{style="font-family:宋体"}[yes]{lang="EN-US"}]{#struct_0_x9962_12256_x2140652614}[表示支持，]{style="font-family:宋体"}[no]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[（大模式下，除了包含小模式的信息之外，还包括]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x9962_12256_981120869}[端口符号名称和]{style="font-family:宋体"}[N]{lang="EN-US"}[节点符号名称信息）]{style="font-family:宋体"}

[[Accept small name server objects]{lang="EN-US"}]{#struct_0_x9962_12256_768509702}

[[交换机是否支持接收小模式的名称服务对象：]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_x9962_12256_x1816413254}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[（小模式下，只有基本信息，不包括]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x9962_12256_1221798986}[端口符号名称、]{style="font-family:宋体"}[N]{lang="EN-US"}[节点符号名称以及所支持的]{style="font-family:宋体"}[FC-4]{lang="EN-US"}[特性信息）]{style="font-family:宋体"}

[[Accept large + FC-4 Features name server objects]{lang="EN-US"}]{#struct_0_x9962_12256_577493071}

[[交换机是否支持接收大模式]{style="font-family:宋体"}[+FC-4]{lang="EN-US"}]{#struct_0_x9962_12256_768444166}[特性的名称服务对象：]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Acceptsmall + FC-4 Features name server objects]{lang="EN-US"}]{#struct_0_x9962_12256_937873820}

[[交换机是否支持接收小模式]{style="font-family:宋体"}[+FC-4]{lang="EN-US"}]{#struct_0_x9962_12256_212250070}[特性的名称服务对象：]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Support receiving ACCept with 0 length]{lang="EN-US"}]{#struct_0_x9962_12256_1183393666}

[[交换机是否支持接收负载为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x9962_12256_480969464}[的名称服务]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文：]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Fabric Controller Capability]{lang="EN-US"}]{#struct_0_x9962_12256_768640774}

[[网络控制器能力列表]{style="font-family:宋体"}]{#struct_0_x9962_12256_1168161492}

[[Support receiving the SW_RSCN Request]{lang="EN-US"}]{#struct_0_x9962_12256_1759234113}

[[交换机是否支持接收]{style="font-family:宋体"}[SW_RSCN]{lang="EN-US"}]{#struct_0_x9962_12256_1361400551}[请求报文：]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Fabric Configuration Server Capability]{lang="EN-US"}]{#struct_0_x9962_12256_768575238}

[[网络配置服务能力列表]{style="font-family:宋体"}]{#struct_0_x9962_12256_x211323928}

[[Support basic configuration services]{lang="EN-US"}]{#struct_0_x9962_12256_x2061142931}

[[交换机是否支持基本配置服务：]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_x9962_12256_754755371}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Support platform configuration services]{lang="EN-US"}]{#struct_0_x9962_12256_768771846}

[[交换机是否支持平台配置服务：]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_x9962_12256_2046015564}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Support topology discovery configuration services]{lang="EN-US"}]{#struct_0_x9962_12256_x1097410166}

[[交换机是否支持拓扑发现配置服务：]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_x9962_12256_x2065034800}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Support enhanced configuration services]{lang="EN-US"}]{#struct_0_x9962_12256_768706310}

[[交换机是否支持增强配置服务：]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_x9962_12256_x1889801904}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[[Enhanced Zone Server Capability]{lang="EN-US"}]{#struct_0_x9962_12256_x1409656281}

[[增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1409721817}[能力列表]{style="font-family:宋体"}

[[Support enhanced zoning management]{lang="EN-US"}]{#struct_0_x9962_12256_675773497}

[[交换机是否支持增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x2001325033}[模式：]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示支持，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不支持]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1828507707 .myid}
[]{#_Toc404798108}[]{#struct_0_x9962_12256_x1190769859}

**FC和FCoE \-- Fabric网络命令 \-- display fc login**

------------------------------------------------------------------------

[**[display fc login]{lang="EN-US"}**]{#struct_0_x9962_12256_x53115397}[命令用来显示节点注册的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x370846041}

[**[display fc login]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1238843743}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_594030605}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_768902918}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x493802058}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1378206354}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1383136624}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x52731769}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_678071410}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1734749009}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_768837382}[：指定所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的信息。在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机上，只能显示]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x9962_12256_1794435313}[：显示登录节点的数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x856905886}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x796087313}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_457750010}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1338171354}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[的节点注册的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc login vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_397996748}

[Interface VSAN FCID     Node WWN                Port WWN]{lang="EN-US"}

[Fc1/0/1   1    0x010000 21:01:00:1b:32:a0:fa:18 21:01:00:1b:32:a0:fa:17]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1918668179}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[的登录节点的数目。]{style="font-family:宋体"}

[[\<Sysname\> display fc login vsan 1 count]{lang="EN-US"}]{#struct_0_x9962_12256_617397346}

[Total entries: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1276158534}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的登录节点的数目。]{style="font-family:宋体"}

[[\<Sysname\> display fc login count]{lang="EN-US"}]{#struct_0_x9962_12256_x1275699782}

[VSAN        Entries]{lang="EN-US"}

[1           1]{lang="EN-US"}

[2           1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries: 2]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[display fc login]{lang="EN-US"}]{#struct_0_x9962_12256_x1604274362}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1298572849}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1547349181}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_737172835}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x1976994335}

[[交换机上和节点相连的接口]{style="font-family:宋体"}]{#struct_0_x9962_12256_977456716}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1403807344}

[[VSAN ID]{lang="EN-US"}]{#struct_0_x9962_12256_x1604339898}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_443376790}

[[交换机为节点分配的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_2073928364}[地址]{style="font-family:宋体"}

[[Node WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x2117959073}

[[节点]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1915706013}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1604143290}

[[节点上和交换机相连的端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1295903395}

[[Entries]{lang="EN-US"}]{#struct_0_x9962_12256_x1455823311}

[[某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1275765318}[内登录节点的数目]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_x9962_12256_x1358235202}

[[登录节点的总数目]{style="font-family:宋体"}]{#struct_0_x9962_12256_x848203638}

[ ]{lang="EN-US"}

::: {#-1838194818 .myid}
[]{#_Toc404798109}[]{#struct_0_x9962_12256_1206361102}[]{#_Toc312748298}[]{#_Toc258485913}

**FC和FCoE \-- Fabric网络命令 \-- display fc name-service database**

------------------------------------------------------------------------

[**[display fc name-service database]{lang="EN-US"}**]{#struct_0_x9962_12256_883267752}[命令用来显示名称服务数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1604208826}

[**[display fc name-service database ]{lang="EN-US"}**[\[ **vsan** *vsan-id* \[ **fcid** *fcid* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x9962_12256_x322980877}

[**[display fc name-service database]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \] **count**]{lang="EN-US"}]{#struct_0_x9962_12256_1836253624}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1353878006}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1247725793}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1551230365}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1476057772}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_490165878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1604012218}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_58938522}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1863033042}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x489206800}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的名称服务数据库信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的名称服务数据库信息。]{style="font-family:宋体"}

[**[fcid]{lang="EN-US"}**[ *fcid*]{lang="EN-US"}]{#struct_0_x9962_12256_x1989071490}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[的名称服务数据库表项。]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0x010000]{lang="EN-US"}[～]{style="font-family:宋体"}[0xEFFFFF]{lang="EN-US"}[（十六进制）。不指定该参数时，将显示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的表项。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9962_12256_x1758263438}[：显示名称服务数据库的详细信息。不指定该参数时，将显示名称服务数据库的简要信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x9962_12256_204330821}[：显示名称服务数据库表项的数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1671976000}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x528289919}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x87565431}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1604077754}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的名称服务数据库的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc name-service database vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_870803555}

[VSAN 1:]{lang="EN-US"}

[  FCID     Type               PWWN(vendor)                      FC4-type:feature]{lang="EN-US"}

[  0x030001 0x01(N)            20:00:00:05:30:00:25:a3           SCSI-FCP]{lang="EN-US"}

[  0x030200 0x01(N)            20:00:00:49:c9:28:c7:01           NPV]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1753119620}[显示名称服务数据库的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc name-service database verbose]{lang="EN-US"}]{#struct_0_x9962_12256_x1603881146}

[VSAN:1     FCID:0x030001]{lang="PT-BR"}

[  Port-WWN(vendor): 20:00:00:05:30:00:25:a3]{lang="PT-BR"}

[  Node-WWN: 20:00:00:05:30:00:25:9e]{lang="PT-BR"}

[  ]{lang="PT-BR"}[Class: 2,3]{lang="EN-US"}

[  Node-IP-addr: 192.168.0.52]{lang="EN-US"}

[  FC4-types(FC4_features): SCSI-FCP]{lang="EN-US"}

[  Symbolic-port-name:]{lang="EN-US"}

[  Symbolic-node-name:]{lang="EN-US"}

[  Port-type: 0x01(N)]{lang="EN-US"}

[  Fabric-port-WWN: 30:30:30:30:65:33:64:6]{lang="EN-US"}

[  Hard-addr: 0x000000]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSAN:1     FCID:0x030200]{lang="EN-US"}

[  Port-WWN(vendor): 20:00:00:5a:c9:28:c7:01]{lang="EN-US"}

[  Node-WWN: 10:00:00:5a:c9:28:c7:01]{lang="EN-US"}

[  Class: 3]{lang="EN-US"}

[  Node-IP-addr: 192.168.6.171]{lang="EN-US"}

[  FC4-types(FC4_features): NPV]{lang="EN-US"}

[  Symbolic-port-name: NPV-Sysname:Vfc1]{lang="EN-US"}

[  Symbolic-node-name: NPV-Sysname]{lang="EN-US"}

[  Port-type: 0x01(N)]{lang="EN-US"}

[  Fabric-port-WWN: 22:0a:00:05:30:00:26:1e]{lang="EN-US"}

[  Hard-addr: 0x000000]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Total 2 entries \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x420187213}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的名称服务数据库表项的数目。]{style="font-family:宋体"}

[[\<Sysname\> display fc name-service database vsan 1 count]{lang="EN-US"}]{#struct_0_x9962_12256_x1603946682}

[Total entries: 2]{lang="EN-US"}

[]{#struct_0_x9962_12256_786366736}[[表1-24 ]{lang="EN-US"}[display fc name-service database]{lang="EN-US"}]{#_Toc250649772}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1292696561}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x653694629}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1143529380}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1398773466}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x296355199}[内的信息]{style="font-family:宋体"}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x1603750074}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_472209415}[端口的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x9962_12256_x1172943765}

[[节点向交换机注册的端口类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1612670755}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x00(Unidentified)]{lang="EN-US"}]{#struct_0_x9962_12256_x1266623408}[：表示未注册端口类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x01(N)]{lang="EN-US"}]{#struct_0_x9962_12256_x1603815610}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[端口。]{style="font-family:宋体"}[N]{lang="EN-US"}[端口通过直连方式连接到]{style="font-family:宋体"}[Fabric]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x02(NL)]{lang="EN-US"}]{#struct_0_x9962_12256_531757333}[：表示]{lang="EN-US" style="font-family:宋体"}[NL]{lang="EN-US"}[端口。]{style="font-family:宋体"}[NL]{lang="EN-US"}[端口通过仲裁环连接到]{style="font-family:宋体"}[Fabric]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x03(F/NL)]{lang="EN-US"}]{#struct_0_x9962_12256_x325347660}[：表示]{lang="EN-US" style="font-family:宋体"}[F]{lang="EN-US"}[端口或者]{style="font-family:宋体"}[NL]{lang="EN-US"}[端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x7f(Nx)]{lang="EN-US"}]{#struct_0_x9962_12256_x1433957278}[：表示]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[端口、]{lang="EN-US" style="font-family:宋体"}[NL]{lang="EN-US"}[端口、]{lang="EN-US" style="font-family:宋体"}[F/NL]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x81(F)]{lang="EN-US"}]{#struct_0_x9962_12256_1987014471}[：表示]{style="font-family:宋体"}[F]{lang="EN-US"}[端口。]{style="font-family:宋体"}[F]{lang="EN-US"}[端口与]{style="font-family:宋体"}[N]{lang="EN-US"}[端口相连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x82(FL)]{lang="EN-US"}]{#struct_0_x9962_12256_x1604274361}[：表示]{lang="EN-US" style="font-family:宋体"}[FL]{lang="EN-US"}[端口。]{style="font-family:宋体"}[FL]{lang="EN-US"}[端口与]{style="font-family:宋体"}[NL]{lang="EN-US"}[端口相连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x84(E)]{lang="EN-US"}]{#struct_0_x9962_12256_1144064654}[：表示]{style="font-family:宋体"}[E]{lang="EN-US"}[端口。]{style="font-family:宋体"}[E]{lang="EN-US"}[端口与]{style="font-family:宋体"}[E]{lang="EN-US"}[端口或]{style="font-family:宋体"}[B]{lang="EN-US"}[端口相连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x85(B)]{lang="EN-US"}]{#struct_0_x9962_12256_1563324781}[：表示]{style="font-family:宋体"}[B]{lang="EN-US"}[端口。如果两个]{style="font-family:宋体"}[E]{lang="EN-US"}[端口之间通过桥设备连接，那么桥设备上连接]{style="font-family:宋体"}[E]{lang="EN-US"}[端口的端口就是]{style="font-family:宋体"}[B]{lang="EN-US"}[端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xXX(Unknown)]{lang="EN-US"}]{#struct_0_x9962_12256_x462215598}[：表示以上取值以外的其它端口类型]{lang="EN-US" style="font-family:宋体"}

[[![说明](FC和FCoE命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x9962_12256_920807328}

[[正常情况下节点只会注册两种端口类型：]{style="font-family:KaiTi_GB2312"}[N]{lang="EN-US"}]{#struct_0_x9962_12256_x1604339897}[端口、]{style="font-family:KaiTi_GB2312"}[NL]{lang="EN-US"}[端口。]{style="font-family:KaiTi_GB2312"}

[[PWWN(vendor)]{lang="EN-US"}]{#struct_0_x9962_12256_40092263}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_443874498}[端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[（制造厂商名称）]{style="font-family:宋体"}

[[FC4-type:feature]{lang="EN-US"}]{#struct_0_x9962_12256_x1154929143}

[[FC4]{lang="EN-US"}]{#struct_0_x9962_12256_x1604143289}[类型：属性（显示简要信息时，最多显示两条]{style="font-family:宋体"}[FC4]{lang="EN-US"}[类型：属性）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FC4]{lang="EN-US"}]{#struct_0_x9962_12256_x1789144784}[类型包括：]{lang="EN-US" style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LLC/SNAP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[SW_ILS]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[GS3]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VI]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NPV]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[属性包括：支持]{lang="EN-US" style="font-family:宋体"}[Initiator]{lang="EN-US"}]{#struct_0_x9962_12256_x1208582104}[、支持]{lang="EN-US" style="font-family:宋体"}[Target]{lang="EN-US"}[、两者都支持]{lang="EN-US" style="font-family:宋体"}[Initiator/Target]{lang="EN-US"}

[[ ]{lang="EN-US"}]{#_Toc250649773}

[[表1-25 ]{lang="EN-US"}[display fc name-service database verbose]{lang="EN-US"}]{#struct_0_x9962_12256_x1604208825}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1324643017}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1889064818}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1183090886}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1298167658}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1854524718}[内的信息]{style="font-family:宋体"}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_1616466435}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_x1604012217}[端口的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Port-WWN(vendor)]{lang="EN-US"}]{#struct_0_x9962_12256_1981252823}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_381849212}[端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[（制造厂商名称）]{style="font-family:宋体"}

[[Node-WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x441117713}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_201050565}[节点的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Class]{lang="EN-US"}]{#struct_0_x9962_12256_x1604077753}

[[CLASS]{lang="EN-US"}]{#struct_0_x9962_12256_111288668}[服务级别]{style="font-family:宋体"}

[[Node-IP-addr]{lang="EN-US"}]{#struct_0_x9962_12256_1576529243}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_1816337132}[节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[FC4-types(FC4 features)]{lang="EN-US"}]{#struct_0_x9962_12256_x1463191066}

[[FC4]{lang="EN-US"}]{#struct_0_x9962_12256_x1603881145}[类型（属性）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FC4]{lang="EN-US"}]{#struct_0_x9962_12256_x1986271154}[类型包括：]{lang="EN-US" style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LLC/SNAP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[SW_ILS]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[GS3]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VI]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NPV]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[属性包括：支持]{lang="EN-US" style="font-family:宋体"}[Initiator]{lang="EN-US"}]{#struct_0_x9962_12256_215692518}[、支持]{lang="EN-US" style="font-family:宋体"}[Target]{lang="EN-US"}[、两者都支持]{lang="EN-US" style="font-family:宋体"}[Initiator/Target]{lang="EN-US"}

[[Symbolic-port-name]{lang="EN-US"}]{#struct_0_x9962_12256_x1603946681}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_x779717205}[端口的符号名称，用于描述此端口。]{style="font-family:宋体"}[H3C]{lang="EN-US"}[的]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机会携带本机系统名和端口名，注册形如]{style="font-family:宋体"}*[system-name]{lang="EN-US"}*[:*port-name*]{lang="EN-US"}[的字符串作为端口描述名]{style="font-family:宋体"}

[[Symbolic-node-name]{lang="EN-US"}]{#struct_0_x9962_12256_x1700312664}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_x1192770661}[节点的符号名称，用于描述此节点。]{style="font-family:宋体"}[H3C]{lang="EN-US"}[的]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机会携带本机系统名，注册形如]{style="font-family:宋体"}*[system-name]{lang="EN-US"}*[的字符串作为节点描述名]{style="font-family:宋体"}

[[Port-type]{lang="EN-US"}]{#struct_0_x9962_12256_x1603750073}

[[节点向交换机注册的端口类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_2038293356}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x00(Unidentified)]{lang="EN-US"}]{#struct_0_x9962_12256_x2046591760}[：表示未注册端口类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x01(N)]{lang="EN-US"}]{#struct_0_x9962_12256_1614089577}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[端口。]{style="font-family:宋体"}[N]{lang="EN-US"}[端口通过直连方式连接到]{style="font-family:宋体"}[Fabric]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x02(NL)]{lang="EN-US"}]{#struct_0_x9962_12256_1572746600}[：表示]{lang="EN-US" style="font-family:宋体"}[NL]{lang="EN-US"}[端口。]{style="font-family:宋体"}[NL]{lang="EN-US"}[端口通过仲裁环连接到]{style="font-family:宋体"}[Fabric]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x03(F/NL)]{lang="EN-US"}]{#struct_0_x9962_12256_x1603815609}[：表示]{lang="EN-US" style="font-family:宋体"}[F]{lang="EN-US"}[端口或者]{style="font-family:宋体"}[NL]{lang="EN-US"}[端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x7f(Nx)]{lang="EN-US"}]{#struct_0_x9962_12256_x1390622504}[：表示]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[端口、]{lang="EN-US" style="font-family:宋体"}[NL]{lang="EN-US"}[端口、]{lang="EN-US" style="font-family:宋体"}[F/NL]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x81(F)]{lang="EN-US"}]{#struct_0_x9962_12256_x150825123}[：表示]{style="font-family:宋体"}[F]{lang="EN-US"}[端口。]{style="font-family:宋体"}[F]{lang="EN-US"}[端口与]{style="font-family:宋体"}[N]{lang="EN-US"}[端口相连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x82(FL)]{lang="EN-US"}]{#struct_0_x9962_12256_1567730696}[：表示]{lang="EN-US" style="font-family:宋体"}[FL]{lang="EN-US"}[端口。]{style="font-family:宋体"}[FL]{lang="EN-US"}[端口与]{style="font-family:宋体"}[NL]{lang="EN-US"}[端口相连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x84(E)]{lang="EN-US"}]{#struct_0_x9962_12256_x1604274364}[：表示]{style="font-family:宋体"}[E]{lang="EN-US"}[端口。]{style="font-family:宋体"}[E]{lang="EN-US"}[端口与]{style="font-family:宋体"}[E]{lang="EN-US"}[端口或]{style="font-family:宋体"}[B]{lang="EN-US"}[端口相连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x85(B)]{lang="EN-US"}]{#struct_0_x9962_12256_740780127}[：表示]{style="font-family:宋体"}[B]{lang="EN-US"}[端口。如果两个]{style="font-family:宋体"}[E]{lang="EN-US"}[端口之间通过桥设备连接，那么桥设备上连接]{style="font-family:宋体"}[E]{lang="EN-US"}[端口的端口就是]{style="font-family:宋体"}[B]{lang="EN-US"}[端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xXX(Unknown)]{lang="EN-US"}]{#struct_0_x9962_12256_x1195147256}[：表示以上取值以外的其它端口类型]{lang="EN-US" style="font-family:宋体"}

[[![说明](FC和FCoE命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x9962_12256_x1604339900}

[[正常情况下节点只会注册两种端口类型：]{style="font-family:KaiTi_GB2312"}[N]{lang="EN-US"}]{#struct_0_x9962_12256_800196973}[端口、]{style="font-family:KaiTi_GB2312"}[NL]{lang="EN-US"}[端口。]{style="font-family:KaiTi_GB2312"}

[[Fabric-port-WWN]{lang="EN-US"}]{#struct_0_x9962_12256_586569742}

[[F]{lang="EN-US"}]{#struct_0_x9962_12256_x1162775607}[端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Hard-addr]{lang="EN-US"}]{#struct_0_x9962_12256_x1604143292}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_133103981}[端口的硬件地址]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_x9962_12256_1291011415}

[[此]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1604208828}[内的表项数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#556924254 .myid}
[]{#_Toc404798110}[]{#struct_0_x9962_12256_x1842010651}[]{#_Toc312748299}[]{#_Toc258485914}

**FC和FCoE \-- Fabric网络命令 \-- display fc scr-table**

------------------------------------------------------------------------

[**[display fc scr-table]{lang="EN-US"}**]{#struct_0_x9962_12256_x1779404183}[命令用来显示]{style="font-family:宋体"}[N]{lang="EN-US"}[端口注册的]{style="font-family:宋体"}[SCR]{lang="EN-US"}[（]{style="font-family:宋体"}[State Change Registration]{lang="EN-US"}[，状态变化注册）列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_52804844}

[**[display fc scr-table]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1132578399}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1441924481}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_588738635}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1604012220}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_414972274}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1277904390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_960759381}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x604123950}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1941601342}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_732018731}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[SCR]{lang="EN-US"}[列表，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[SCR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x9962_12256_x1973312095}[：显示]{style="font-family:宋体"}[SCR]{lang="EN-US"}[表项的数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1672041536}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1394753426}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1604077756}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x291995859}[显示]{style="font-family:宋体"}[SCR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[\<Sysname\> display fc scr-table]{lang="EN-US"}]{#struct_0_x9962_12256_2002617432}

[SCR table for VSAN 1:]{lang="EN-US"}

[FCID         REGISTERED FOR]{lang="EN-US"}

[0x1b0300     fabric detected rscns]{lang="EN-US"}

[0x010121     nx_port detected rscns]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Total 2 entries \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1447529093}[显示]{style="font-family:宋体"}[SCR]{lang="EN-US"}[表项数目。]{style="font-family:宋体"}

[[\<Sysname\> display fc scr-table vsan 1 count]{lang="EN-US"}]{#struct_0_x9962_12256_267341403}

[Total entries: 2]{lang="EN-US"}

[]{#struct_0_x9962_12256_x1435239566}[[表1-26 ]{lang="EN-US"}[display fc scr-table]{lang="EN-US"}]{#_Toc250649775}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1314893053}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1603881148}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1226756267}

[[SCR table for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x59816003}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x66247262}[内的]{style="font-family:宋体"}[SCR]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x760411525}

[[N]{lang="EN-US"}]{#struct_0_x9962_12256_x2028694048}[端口的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[REGISTERED FOR]{lang="EN-US"}]{#struct_0_x9962_12256_x1603946684}

[[注册接收]{style="font-family:宋体"}[RSCN]{lang="EN-US"}]{#struct_0_x9962_12256_x376432678}[（]{style="font-family:宋体"}[Registered State Change Notification]{lang="EN-US"}[，注册状态变化通知）报文的种类：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fabric detected rscns]{lang="EN-US"}]{#struct_0_x9962_12256_x1632965702}[：表示注册接收所有由]{lang="EN-US" style="font-family:
  宋体"}[Fabric]{lang="EN-US"}[中的交换机感知到状态变化而]{style="font-family:
  宋体"}[发送的]{lang="EN-US" style="font-family:宋体"}[RSCN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[nx_port detected rscns]{lang="EN-US"}]{#struct_0_x9962_12256_1953144132}[：表示注册接收所有由]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}[感知到状态变化而]{style="font-family:宋体"}[发送的]{lang="EN-US" style="font-family:宋体"}[RSCN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[full detected rscns]{lang="EN-US"}]{#struct_0_x9962_12256_1155355269}[：表示注册接收所有的]{lang="EN-US" style="font-family:
  宋体"}[RSCN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_x9962_12256_x1603750076}

[[此]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1635008829}[内的表项数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1650104765 .myid}
[]{#_Toc404798111}[]{#struct_0_x9962_12256_38898017}

**FC和FCoE \-- Fabric网络命令 \-- display fc switch-wwn**

------------------------------------------------------------------------

[**[display fc switch-wwn]{lang="EN-US"}**]{#struct_0_x9962_12256_x480125946}[命令用来显示本交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1007318166}

[**[display fc switch-wwn]{lang="EN-US"}**]{#struct_0_x9962_12256_x91483696}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_38832481}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x21839207}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_836102413}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x981450816}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1544439017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2012830917}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1829435293}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1654270574}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x764748548}[显示本交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display fc switch-wwn]{lang="EN-US"}]{#struct_0_x9962_12256_39029089}

[Switch WWN is 10:00:00:0d:ec:ff:a3:25]{lang="EN-US"}
:::

::: {#802882091 .myid}
[]{#_Toc297038082}[]{#_Toc290886988}[]{#_Toc239584267}[]{#_Toc404798112}[]{#struct_0_x9962_12256_194886132}[]{#_Toc330053504}

**FC和FCoE \-- Fabric网络命令 \-- display fc timer**

------------------------------------------------------------------------

[**[display fc timer]{lang="EN-US"}**]{#struct_0_x9962_12256_966047595}[命令用来显示]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[定时器信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x239814669}

[**[display fc timer]{lang="EN-US"}**[ \[ **distributed-services** \| **error-detect** \| **resource-allocation** \] \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x191557463}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1541249699}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1603815612}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1694556747}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1279246021}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x2024638728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_51798581}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1007058970}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1460605594}

[**[distributed-services]{lang="EN-US"}**]{#struct_0_x9962_12256_x1008860643}[：显示分布式服务超时时间。]{style="font-family:宋体"}

[**[error-detect]{lang="EN-US"}**]{#struct_0_x9962_12256_x1604274363}[：显示错误检测超时时间。]{style="font-family:宋体"}

[**[resource-allocation]{lang="EN-US"}**]{#struct_0_x9962_12256_x18734760}[：显示资源分配超时时间。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1824236122}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[定时器信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示全局]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[定时器信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1380993770}

[[如果配置命令时不指定]{style="font-family:宋体"}**[distributed-services]{lang="EN-US"}**]{#struct_0_x9962_12256_97452467}[、]{style="font-family:宋体"}**[error-detect]{lang="EN-US"}**[、]{style="font-family:宋体"}**[resource-allocation]{lang="EN-US"}**[参数，将显示所有]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[定时器的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x597657247}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1835951355}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的所有]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[定时器信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc timer vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_x1604339899}

[Timer of VSAN 1:]{lang="EN-US"}

[  Distributed-services timer: 5000 ms]{lang="EN-US"}

[  Error-detect timer:         2000 ms]{lang="EN-US"}

[  Resource-allocation timer:  10000 ms]{lang="EN-US"}

[[表1-27 ]{lang="EN-US"}[display fc timer]{lang="EN-US"}]{#struct_0_x9962_12256_x1122707151}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1316751693}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1496311002}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1052114490}

[[Timer of VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_815153475}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_15494116}[内的]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[定时器信息]{style="font-family:宋体"}

[[Distributed-services timer]{lang="EN-US"}]{#struct_0_x9962_12256_x1604143291}

[[分布式服务超时时间，单位为毫秒]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1432979960}

[[Error-detect timer]{lang="EN-US"}]{#struct_0_x9962_12256_x1042892243}

[[错误检测超时时间，单位为毫秒]{style="font-family:宋体"}]{#struct_0_x9962_12256_x786130969}

[[Resource-allocation timer]{lang="EN-US"}]{#struct_0_x9962_12256_x1321778076}

[[资源分配超时时间，单位为毫秒]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1604208827}

[ ]{lang="EN-US"}

::: {#-1810497354 .myid}
[]{#_Toc404798113}[]{#struct_0_x9962_12256_x1816356706}[]{#_Toc393700657}

**FC和FCoE \-- Fabric网络命令 \-- display fcid allocation**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fcid** **allocation**]{lang="EN-US"}]{#struct_0_x9962_12256_x1165855621}[命令用来显示]{style="font-family:宋体"}[FCID]{lang="EN-US"}[的分配情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_912526649}

[**[display]{lang="EN-US"}**[ **fcid** **allocation** \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x123574149}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x365285679}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1464428450}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x738218389}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x748714304}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x722059516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x847177241}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x173618752}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1460060810}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1813184564}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1719470747}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x432470884}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1068309861}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1837397931}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[分配情况。]{style="font-family:宋体"}

[[\<Sysname\> display fcid allocation vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_1268822545}

[VSAN 1:]{lang="EN-US"}

[Free FCIDs: 0xef0000 to 0xef06ff]{lang="EN-US"}

[            0xef0701 to 0xef08ff]{lang="EN-US"}

[            0xef0901 to 0xefffff]{lang="EN-US"}

[ ]{lang="EN-US"}

[Assigned FCIDs: 0xef0700]{lang="EN-US"}

[                0xef0900]{lang="EN-US"}

[ ]{lang="EN-US"}

[Number of free FCIDs: 65534]{lang="EN-US"}

[Number of assigned FCIDs: 2]{lang="EN-US"}

[[表1-28 ]{lang="EN-US"}[display fcid allocation]{lang="EN-US"}]{#struct_0_x9962_12256_x1687405570}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_474373476}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1128581845}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1672107072}

[[VSAN 1]{lang="EN-US"}]{#struct_0_x9962_12256_510753779}

[[VSAN ID]{lang="EN-US"}]{#struct_0_x9962_12256_106023131}

[[Free FCIDs]{lang="EN-US"}]{#struct_0_x9962_12256_x1007499096}

[[未分配的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x1360834137}

[[Assigned FCIDs]{lang="EN-US"}]{#struct_0_x9962_12256_865538018}

[[已分配的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x1273872638}

[[Number of free FCIDs]{lang="EN-US"}]{#struct_0_x9962_12256_x700545923}

[[未分配的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_376911947}[数量]{style="font-family:宋体"}

[[Number of assigned FCIDs]{lang="EN-US"}]{#struct_0_x9962_12256_x297261396}

[[已分配的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x697257761}[数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#740876787 .myid}
[]{#_Toc404798114}[]{#struct_0_x9962_12256_x573203945}[]{#_Toc393700658}

**FC和FCoE \-- Fabric网络命令 \-- display fcid persistent**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fcid** **persistent**]{lang="EN-US"}]{#struct_0_x9962_12256_x1863345337}[命令用来显示]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1606452267}

[**[display]{lang="EN-US"}**[ **fcid** **persistent** \[ **unused** \] \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_338802297}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1460438451}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1489874539}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1162131241}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_441687695}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1043146771}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_840255882}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1816291170}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_662617823}

[**[unused]{lang="EN-US"}**]{#struct_0_x9962_12256_297908944}[：显示当前尚未使用（即对应节点未登录）的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。如果未指定本参数，将显示所有的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1446703337}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x458423483}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_944149696}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_603694422}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x675535409}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcid persistent]{lang="EN-US"}]{#struct_0_x9962_12256_912592185}

[VSAN 1:]{lang="EN-US"}

[FCID persistence: Enabled]{lang="EN-US"}

[Total entries: 3]{lang="EN-US"}

[WWN                      FCID       Used   Assignment]{lang="EN-US"}

[10:00:00:00:c9:ef:39:5f  0x1e0002   Yes    Dynamic]{lang="EN-US"}

[10:00:00:00:c9:ef:39:60  0x1e1000   Yes    Static]{lang="EN-US"}

[10:00:00:00:c9:ef:39:68  0x1e000a   Yes    Dynamic]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSAN 2:]{lang="EN-US"}

[FCID persistence: Disabled]{lang="EN-US"}

[Total entries: 0]{lang="EN-US"}

[[表1-29 ]{lang="EN-US"}[display fcid allocation]{lang="EN-US"}]{#struct_0_x9962_12256_1482737521}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_502753356}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1139485468}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1459995274}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x749543780}

[[VSAN ID]{lang="EN-US"}]{#struct_0_x9962_12256_1268888081}

[[FCID persistence]{lang="EN-US"}]{#struct_0_x9962_12256_x507335180}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_1672172608}[持久化功能的开启状态，包括：]{style="font-family:宋体"}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[[Enabled]{lang="EN-US"}]{.TableTextChar}]{#struct_0_x9962_12256_541990429}[[：]{style="font-family:宋体"}]{.TableTextChar}[[表示]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[[已]{style="font-family:宋体"}]{.TableTextChar}[[开启]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x9962_12256_106088667}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[已]{style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}

[[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_928517739}

[[节点的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_865603554}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x1378814058}

[[交换机为节点分配的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x700480387}[地址]{style="font-family:宋体"}

[[Used]{lang="EN-US"}]{#struct_0_x9962_12256_790098281}

[[分配的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_1363485208}[的使用情况，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x9962_12256_x297195860}[：表示节点在线，正在使用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x9962_12256_1569096557}[：表示节点不在线，未使用]{style="font-family:宋体"}

[[Assignment]{lang="EN-US"}]{#struct_0_x9962_12256_x1863279801}

[[分配的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x732529997}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_x9962_12256_x1816225634}[：表示]{style="font-family:宋体"}[动态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_x9962_12256_1373102069}[：表示]{style="font-family:宋体"}[静态]{lang="EN-US" style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_x9962_12256_912657721}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_1704582347}[持久化表项的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#215270591 .myid}
[]{#_Toc404798115}[]{#struct_0_x9962_12256_794710915}[]{#_Toc367888149}[]{#_Toc369076493}[]{#_Toc367888150}[]{#_Toc369076494}[]{#_Toc367888151}[]{#_Toc369076495}[]{#_Toc367888152}[]{#_Toc369076496}[]{#_Toc367888153}[]{#_Toc369076497}[]{#_Toc367888154}[]{#_Toc369076498}[]{#_Toc367888155}[]{#_Toc369076499}[]{#_Toc367888156}[]{#_Toc369076500}[]{#_Toc367888157}[]{#_Toc369076501}[]{#_Toc367888158}[]{#_Toc369076502}[]{#_Toc367888159}[]{#_Toc369076503}[]{#_Toc367888160}[]{#_Toc369076504}[]{#_Toc367888161}[]{#_Toc369076505}[]{#_Toc367888162}[]{#_Toc369076506}[]{#_Toc367888163}[]{#_Toc369076507}[]{#_Toc367888164}[]{#_Toc369076508}[]{#_Toc367888165}[]{#_Toc369076509}[]{#_Toc367888166}[]{#_Toc369076510}[]{#_Toc367888167}[]{#_Toc369076511}[]{#_Toc367888168}[]{#_Toc369076512}[]{#_Toc367888169}[]{#_Toc369076513}[]{#_Toc367888170}[]{#_Toc369076514}[]{#_Toc367888171}[]{#_Toc369076515}[]{#_Toc367888172}[]{#_Toc369076516}[]{#_Toc367888173}[]{#_Toc369076517}[]{#_Toc367888174}[]{#_Toc369076518}[]{#_Toc367888175}[]{#_Toc369076519}[]{#_Toc367888176}[]{#_Toc369076520}[]{#_Toc367888177}[]{#_Toc369076521}[]{#_Toc367888178}[]{#_Toc369076522}[]{#_Toc367888179}[]{#_Toc369076523}[]{#_Toc367888180}[]{#_Toc369076524}[]{#_Toc367888181}[]{#_Toc369076525}[]{#_Toc367888182}[]{#_Toc369076526}[]{#_Toc367888183}[]{#_Toc369076527}[]{#_Toc367888184}[]{#_Toc369076528}[]{#_Toc367888185}[]{#_Toc369076529}[]{#_Toc367888186}[]{#_Toc369076530}[]{#_Toc367888187}[]{#_Toc369076531}[]{#_Toc367888188}[]{#_Toc369076532}[]{#_Toc367888245}[]{#_Toc369076589}[]{#_Toc367888246}[]{#_Toc369076590}[]{#_Toc367888247}[]{#_Toc369076591}[]{#_Toc367888248}[]{#_Toc369076592}[]{#_Toc367888249}[]{#_Toc369076593}[]{#_Toc367888250}[]{#_Toc369076594}[]{#_Toc367888251}[]{#_Toc369076595}[]{#_Toc367888252}[]{#_Toc369076596}[]{#_Toc367888253}[]{#_Toc369076597}[]{#_Toc367888254}[]{#_Toc369076598}[]{#_Toc367888255}[]{#_Toc369076599}[]{#_Toc367888256}[]{#_Toc369076600}[]{#_Toc367888257}[]{#_Toc369076601}[]{#_Toc367888258}[]{#_Toc369076602}[]{#_Toc367888259}[]{#_Toc369076603}[]{#_Toc367888260}[]{#_Toc369076604}[]{#_Toc367888317}[]{#_Toc369076661}

**FC和FCoE \-- Fabric网络命令 \-- domain auto-reconfigure enable**

------------------------------------------------------------------------

[**[domain auto-reconfigure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1512522657}[命令用来开启自动]{style="font-family:
宋体"}[Fabric]{lang="EN-US"}[重配置功能。]{style="font-family:宋体"}

[**[undo domain auto-reconfigure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1603946685}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1189651263}

[**[domain auto-reconfigure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1509233723}

[**[undo domain auto-reconfigure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_2061465080}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_138120910}

[[自动]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x1823848585}[重配置功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1192036156}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1719647770}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1603750077}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_68924888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1308205871}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1502581964}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1268953617}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x726429613}[重配置将触发整个网络重新开始主交换机选举、域]{style="font-family:宋体"}[ID]{lang="EN-US"}[分配和]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址分配。]{style="font-family:宋体"}

[[自动]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x729670965}[重配置功能一般在网络出现故障或者合并时发生：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[两个]{style="font-family:宋体"}]{#struct_0_x9962_12256_x107216485}[Fabric]{lang="EN-US"}[网络合并时，如果域]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表重叠，交换机会自动进行中断重配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[两个]{style="font-family:宋体"}]{#struct_0_x9962_12256_1224071662}[Fabric]{lang="EN-US"}[网络合并时，如果两个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的主交换机信息不同，而且域]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表非空且不重叠，系统会自动进行非中断重配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主交换机宕机时，系统会自动进行非中断重配置。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1603815613}

[[需要注意的是，只有开启了]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_128472806}[配置功能后，本命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2046546495}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1255504845}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内开启自动]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[重配置功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1810911742}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] domain auto-reconfigure enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276787353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain configure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x259569242}
:::

::: {#2091549068 .myid}
[]{#_Toc404798116}[]{#struct_0_x9962_12256_x38190421}

**FC和FCoE \-- Fabric网络命令 \-- domain configure enable**

------------------------------------------------------------------------

[**[domain configure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_850073532}[命令用来开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **domain** **configure** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_1674151028}[命令用来关闭]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1591066702}

[**[domain configure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_2056405474}

[**[undo domain configure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1002623500}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1436897523}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_83895004}[内的]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38255957}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1579029649}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1861870697}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1797600805}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1496275050}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x865356093}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1099409255}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x386081650}[配置功能后，]{style="font-family:宋体"}[FC]{lang="EN-US"}[交换机会通过消息交互选举主交换机，并由选举出来的主交换机为网络中的所有交换机动态分配域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。因此，在动态建立]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络时，必须在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的所有交换机上都开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能；而在静态建立]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络时，则必须在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的所有交换机上都关闭]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能，需要手工配置各交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2023209116}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x38059349}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1859923911}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] domain configure enable]{lang="EN-US"}
:::

::: {#1567487087 .myid}
[]{#_Toc404798117}[]{#struct_0_x9962_12256_x127666455}[]{#_Toc45685348}

**FC和FCoE \-- Fabric网络命令 \-- domain restart**

------------------------------------------------------------------------

[**[domain]{lang="EN-US"}[ restart]{lang="EN-US"}**]{#struct_0_x9962_12256_x1381689241}[命令用来手工发起]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[重配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1654119438}

[**[domain restart]{lang="EN-US"}**[ \[ **disruptive** \]]{lang="EN-US"}]{#struct_0_x9962_12256_19777847}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x54265931}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x38124885}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_560177003}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x177663095}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x280987805}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x83713248}

[**[disruptive]{lang="EN-US"}**]{#struct_0_x9962_12256_x1336882370}[：]{style="font-family:宋体"}[表示发起中断重配置。如果未指定本参数，表示发起非中断重配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1576292325}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1099409256}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x1008186440}[重配置一般在网络改造（比如两个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络合并等）或外部干预（比如管理员通过命令行发起重配置）时发生。]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[重配置将触发整个网络重新开始主交换机选举、域]{style="font-family:宋体"}[ID]{lang="EN-US"}[分配和]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址分配。]{style="font-family:宋体"}

[[根据重配置过程中对]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x1499447631}[网络的影响程度不同，可将]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[重配置分为以下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[中断重配置：在整个]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_165800716}[中洪泛]{lang="EN-US" style="font-family:宋体"}[RCF]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Reconfigure Fabric]{lang="EN-US"}[，重配置]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[）报文，通知所有交换机进行中断重配置。]{lang="EN-US" style="font-family:宋体"}[重配置过程中，会清除所有运行数据重新进行协商，因此整个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的数据传输都会中断。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非中断重配置：在整个]{style="font-family:宋体"}]{#struct_0_x9962_12256_1580266713}[Fabric]{lang="EN-US"}[中洪泛]{style="font-family:宋体"}[BF]{lang="EN-US"}[（]{style="font-family:宋体"}[Build Fabric]{lang="EN-US"}[，建立]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[）报文，通知所有交换机进行非中断重配置。重配置过程中，会尽量保留上一次的运行数据，以保证交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[尽量不发生变化，从而不影响]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的数据传输。]{style="font-family:宋体"}

[[对于配置之后不会立即生效的]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x413835030}[配置（比如修改了交换机的优先级），需要执行中断重配置使其生效。]{style="font-family:宋体"}

[[需要注意的是，只有开启了]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_1115173107}[配置功能后，本命令才生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x78207179}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_2010495129}[手工在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内发起中断重配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x37993813}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] domain restart disruptive]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x960078325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain configure enable]{lang="EN-US"}**]{#struct_0_x9962_12256_492796810}
:::

::: {#1411680218 .myid}
[]{#_Toc404798118}[]{#struct_0_x9962_12256_x938360212}

**FC和FCoE \-- Fabric网络命令 \-- domain-id**

------------------------------------------------------------------------

[**[domain-id]{lang="EN-US"}**]{#struct_0_x9962_12256_1776738867}[命令用来配置交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **domain-id**]{lang="EN-US"}]{#struct_0_x9962_12256_x1819045945}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_663029766}

[**[domain-id]{lang="EN-US"}**[ *domain-id* { **preferred** \| **static** }]{lang="EN-US"}]{#struct_0_x9962_12256_x714040952}

[**[undo domain-id]{lang="EN-US"}**]{#struct_0_x9962_12256_x37797205}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1986794473}

[[交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_x1253954524}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，采用]{style="font-family:
宋体"}[preferred]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1689166357}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1425407010}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1772404416}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1102120687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x865524797}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37862741}

[*[domain-id]{lang="EN-US"}*]{#struct_0_x9962_12256_947800519}[：域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[239]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[preferred]{lang="EN-US"}**]{#struct_0_x9962_12256_x1335250841}[：]{style="font-family:宋体"}[preferred]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x9962_12256_153370635}[：]{style="font-family:宋体"}[static]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1440754558}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1239242912}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[虽然上层协议只能识别]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x2141097714}[，但实际报文传输时，在]{style="font-family:宋体"}[FC]{lang="EN-US"}[交换机之间的路由和转发使用的都是域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。域]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[8]{lang="EN-US"}[位的地址，域]{style="font-family:
宋体"}[ID]{lang="EN-US"}[是按每个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[进行分配的，也存在默认值。因为域]{style="font-family:宋体"}[ID]{lang="EN-US"}[的默认值都为]{style="font-family:宋体"}[0]{lang="EN-US"}[，无法区分不同的设备，所以在使用前必须分配域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，可以通过静态配置，也可以动态分配。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x604884265}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过静态配置指定域]{style="font-family:宋体"}]{#struct_0_x9962_12256_1481229391}[ID]{lang="EN-US"}[，则需要为]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络中的每台交换机都指定域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，且每台交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[必须是唯一的。在静态配置域]{style="font-family:宋体"}[ID]{lang="EN-US"}[情况下，]{style="font-family:宋体"}[preferred]{lang="EN-US"}[模式和]{style="font-family:宋体"}[static]{lang="EN-US"}[模式没有区别。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果动态分配域]{style="font-family:宋体"}]{#struct_0_x9962_12256_x37666133}[ID]{lang="EN-US"}[，则由主交换机负责为网络中的每台交换机分配域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。在动态获取域]{style="font-family:宋体"}[ID]{lang="EN-US"}[情况下，当非主交换机向主交换机请求分配配置的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[失败时，]{style="font-family:宋体"}[preferred]{lang="EN-US"}[模式下，非主交换机可以使用主交换机分配的其它域]{style="font-family:宋体"}[ID]{lang="EN-US"}[；]{style="font-family:宋体"}[static]{lang="EN-US"}[模式下，非主交换机将隔离上游主链路。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议为一个]{style="font-family:宋体"}]{#struct_0_x9962_12256_355634723}[VSAN]{lang="EN-US"}[内的所有交换机都配置相同模式的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1032524815}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x703337532}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[55]{lang="EN-US"}[，采用]{style="font-family:宋体"}[static]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x2119479570}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] domain-id 55 static]{lang="EN-US"}
:::

::: {#875704047 .myid}
[]{#_Toc404798119}[]{#struct_0_x9962_12256_x520563125}

**FC和FCoE \-- Fabric网络命令 \-- fabric-name**

------------------------------------------------------------------------

[**[fabric-name]{lang="EN-US"}**]{#struct_0_x9962_12256_625106699}[命令用来配置]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fabric-name**]{lang="EN-US"}]{#struct_0_x9962_12256_x37731669}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x812532279}

[**[fabric-name]{lang="EN-US"}**[ *name*]{lang="EN-US"}]{#struct_0_x9962_12256_743893323}

[**[undo fabric-name]{lang="EN-US"}**]{#struct_0_x9962_12256_x361598692}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1721205674}

[[使用]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_141819995}[作为]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x943442616}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x560060393}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38190420}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_850073531}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1674151031}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1591656525}

[*[name]{lang="EN-US"}*]{#struct_0_x9962_12256_1663451550}[：表示]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_392677343}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1239242915}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_619284817}[交换机支持为每个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[分配一个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络名称，其格式与]{style="font-family:宋体"}[WWN]{lang="EN-US"}[格式相同，是一个]{style="font-family:宋体"}[64]{lang="EN-US"}[位的地址。当]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[创建后，如果用户未配置]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称，则使用本交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[作为]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称。]{style="font-family:宋体"}

[[需要注意的是，仅在静态建立]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_1046386519}[网络时才需要配置]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称，并且同一]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有交换机的]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络名称必须一样。动态建立]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络时并不需要配置]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称，系统将使用主交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[作为]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38255956}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1579029648}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称为]{style="font-family:宋体"}[10:11:12:13:14:15:16:17]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1861936233}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] fabric-name 10:11:12:13:14:15:16:17]{lang="EN-US"}
:::

::: {#-598013670 .myid}
[]{#_Toc404798120}[]{#struct_0_x9962_12256_651351857}

**FC和FCoE \-- Fabric网络命令 \-- fc domain rcf-reject**

------------------------------------------------------------------------

[**[fc]{lang="EN-US"}**[ **domain** **rcf-reject**]{lang="EN-US"}]{#struct_0_x9962_12256_91982765}[命令用来配置接口拒绝收到的指定]{style="font-family:
宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:
宋体"}[RCF]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fc** **domain** **rcf-reject**]{lang="EN-US"}]{#struct_0_x9962_12256_x1548012784}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_29013580}

[**[fc domain rcf-reject vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x38059348}

[**[undo fc domain rcf-reject vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1859923912}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1693750396}

[[接口不拒绝收到的]{style="font-family:宋体"}[RCF]{lang="EN-US"}]{#struct_0_x9962_12256_740639040}[请求报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_718801411}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x730582953}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}[/VFC]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1827785644}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x38124884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_560177004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x177663088}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x281839772}[：指定所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1990847186}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1239242914}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[在一个稳定的网络中，可以配置接口拒绝收到的特定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1027644083}[内的]{style="font-family:宋体"}[RCF]{lang="EN-US"}[请求报文，以防止设备进行不必要的中断重配置。配置该功能后，如果接口收到该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[RCF]{lang="EN-US"}[请求报文，设备会回应拒绝报文，并将该接口隔离。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1574870726}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_181026535}[配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[拒绝收到的]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[RCF]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x37928276}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] fc domain rcf-reject vsan 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_75538961}[配置接口]{style="font-family:宋体"}[VFC1]{lang="EN-US"}[拒绝收到的]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[RCF]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_75670033}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] fc domain rcf-reject vsan 1]{lang="EN-US"}
:::

::: {#-137127985 .myid}
[]{#_Toc404798121}[]{#struct_0_x9962_12256_38766944}

**FC和FCoE \-- Fabric网络命令 \-- fc login-limit**

------------------------------------------------------------------------

[**[fc login-limit]{lang="EN-US"}**]{#struct_0_x9962_12256_x876480650}[命令用来配置]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下的最大登录节点数。]{style="font-family:宋体"}

[**[undo fc login-limit]{lang="EN-US"}**]{#struct_0_x9962_12256_x1920335230}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_584705603}

[**[fc login-limit]{lang="EN-US"}**[ *max-number*]{lang="EN-US"}]{#struct_0_x9962_12256_1775925041}

[**[undo fc login-limit]{lang="EN-US"}**]{#struct_0_x9962_12256_185569716}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_38701408}

[[不限制]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2005326583}[下的最大登录节点数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1176776882}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1841631168}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x425375450}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1376559915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1910957326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_39422304}

[*[max-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x2000538667}[：]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下的最大登录节点数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1008224215}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1239242909}[交换机支持本命令。]{style="font-family:宋体"}

[[本命令用于配置]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1499859305}[下的最大登录节点数，以防止某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下的登录节点过多，占用大量的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源。这里的登录节点数＝交换机直连的]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的数＋登录到本交换机上的服务器和磁盘数。]{style="font-family:宋体"}

[[如果已登录节点数大于配置的最大登录节点数，不会将已登录节点强制下线，但后续任何新节点均无法登陆。用户可以通过手工关闭接口等方式将不需要的节点下线。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x7770783}

[[需要注意的是，登录节点数即受本命令、也受硬件]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x9962_12256_39356768}[资源的限制，当硬件]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源耗尽时，新节点也无法登录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1290200088}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1643032259}[配置]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[下最多登录]{style="font-family:宋体"}[256]{lang="EN-US"}[个节点。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1295591222}

[[\[Sysname\] vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_x566791791}

[[\[Sysname-vsan2\] fc login-limit 256]{lang="EN-US"}]{#struct_0_x9962_12256_813602312}
:::

::: {#-1082597479 .myid}
[]{#_Toc404798122}[]{#struct_0_x9962_12256_355634724}[]{#_Toc356214013}[]{#_Toc355594363}[]{#_Toc367888324}[]{#_Toc369076668}[]{#_Toc367888325}[]{#_Toc369076669}[]{#_Toc367888326}[]{#_Toc369076670}[]{#_Toc367888327}[]{#_Toc369076671}[]{#_Toc367888328}[]{#_Toc369076672}[]{#_Toc367888329}[]{#_Toc369076673}[]{#_Toc367888330}[]{#_Toc369076674}[]{#_Toc367888331}[]{#_Toc369076675}[]{#_Toc367888332}[]{#_Toc369076676}[]{#_Toc367888333}[]{#_Toc369076677}[]{#_Toc367888334}[]{#_Toc369076678}[]{#_Toc367888335}[]{#_Toc369076679}[]{#_Toc367888336}[]{#_Toc369076680}[]{#_Toc367888337}[]{#_Toc369076681}[]{#_Toc367888338}[]{#_Toc369076682}[]{#_Toc367888339}[]{#_Toc369076683}[]{#_Toc367888340}[]{#_Toc369076684}[]{#_Toc367888341}[]{#_Toc369076685}[]{#_Toc367888342}[]{#_Toc369076686}[]{#_Toc367888343}[]{#_Toc369076687}[]{#_Toc367888344}[]{#_Toc369076688}[]{#_Toc367888345}[]{#_Toc369076689}[]{#_Toc367888346}[]{#_Toc369076690}[]{#_Toc367888347}[]{#_Toc369076691}[]{#_Toc367888348}[]{#_Toc369076692}[]{#_Toc367888349}[]{#_Toc369076693}[]{#_Toc367888350}[]{#_Toc369076694}[]{#_Toc367888351}[]{#_Toc369076695}[]{#_Toc367888352}[]{#_Toc369076696}[]{#_Toc367888353}[]{#_Toc369076697}[]{#_Toc367888354}[]{#_Toc369076698}[]{#_Toc367888355}[]{#_Toc369076699}[]{#_Toc367888356}[]{#_Toc369076700}[]{#_Toc367888357}[]{#_Toc369076701}[]{#_Toc324770309}[]{#_Toc324770310}[]{#_Toc324770311}[]{#_Toc324770312}

**FC和FCoE \-- Fabric网络命令 \-- fc name-service auto-discovery**

------------------------------------------------------------------------

[**[fc name-service auto-discovery]{lang="EN-US"}**]{#struct_0_x9962_12256_x1032524820}[命令用来开启]{style="font-family:
宋体"}[Fabric]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息功能。]{style="font-family:宋体"}

[**[undo fc name-service auto-discovery]{lang="EN-US"}**]{#struct_0_x9962_12256_x37731668}[命令用来关闭]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x812532280}

[**[fc name-service auto-discovery]{lang="EN-US"}**]{#struct_0_x9962_12256_743303504}

[**[undo fc name-service auto-discovery]{lang="EN-US"}**]{#struct_0_x9962_12256_477672594}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38190423}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_850073530}[自动发现]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1674151030}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x38255959}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1579029655}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1861084264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x38059351}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_478728241}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_104212140}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[某些节点设备有时不会主动注册支持]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}]{#struct_0_x9962_12256_1044806009}[协议（比如节点设备离线又重新上线后，不再主动注册]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[或]{style="font-family:宋体"}[Feature]{lang="EN-US"}[），也因此没有]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[协议对应的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[值，对节点设备间的互通可能产生影响。]{style="font-family:宋体"}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_231442220}[自动发现]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息功能可以主动获取节点设备的]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[协议及其对应的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[值，开启该功能后，]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机在节点设备登录后，会主动向节点设备发送]{style="font-family:宋体"}[PRLI]{lang="EN-US"}[报文，询问节点设备是否支持]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[协议，同时获取节点设备支持]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[协议对应的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[信息，并将此信息保存在名称服务数据库中。]{style="font-family:宋体"}

[[需要注意的是，开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x38124887}[自动发现]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息功能后，某些较老型号的网卡可能不会再向交换机自动注册节点设备信息。请用户根据实际情况选择是否开启本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_560177001}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x177663093}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[自动发现]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x37928279}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] fc name-server auto-discovery]{lang="EN-US"}
:::

::: {#202722521 .myid}
[]{#_Toc404798123}[]{#struct_0_x9962_12256_165800714}

**FC和FCoE \-- Fabric网络命令 \-- fc timer distributed-services**

------------------------------------------------------------------------

[**[fc timer]{lang="EN-US"}**[ **distributed-services**]{lang="EN-US"}]{#struct_0_x9962_12256_1580266711}[命令用来全局配置分布式服务超时时间。]{style="font-family:宋体"}

[**[undo fc timer]{lang="EN-US"}**[ **distributed-services**]{lang="EN-US"}]{#struct_0_x9962_12256_x413966102}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_353418296}

[**[fc timer distributed-services]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_x1826818647}

[**[undo fc timer distributed-services]{lang="EN-US"}**]{#struct_0_x9962_12256_x165890125}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37993815}

[[分布式服务超时时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}]{#struct_0_x9962_12256_x960078327}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_492665738}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_245672704}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1218058184}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1012984367}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1760679532}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1899111243}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_x37797207}[：分布式服务超时时间，取值范围为]{style="font-family:宋体"}[5000]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1986794475}

[[本命令与]{style="font-family:宋体"}**[timer distributed-services]{lang="EN-US"}**]{#struct_0_x9962_12256_x1239242910}[命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1170797825}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2126701655}[全局配置分布式服务超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_277301665}

[\[Sysname\] fc timer distributed-services 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37862743}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer distributed-services]{lang="EN-US"}**]{#struct_0_x9962_12256_947800517}
:::

::: {#1246473362 .myid}
[]{#_Toc404798124}[]{#struct_0_x9962_12256_x1335250843}[]{#_Toc297188406}

**FC和FCoE \-- Fabric网络命令 \-- fc timer error-detect**

------------------------------------------------------------------------

[**[fc timer]{lang="EN-US"}**[ **error-detect**]{lang="EN-US"}]{#struct_0_x9962_12256_x1009428779}[命令用来全局配置错误检测超时时间。]{style="font-family:宋体"}

[**[undo fc timer]{lang="EN-US"}**[ **error-detect**]{lang="EN-US"}]{#struct_0_x9962_12256_x1409171654}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x744560437}

[**[fc timer error-detect]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_x467463889}

[**[undo fc timer error-detect]{lang="EN-US"}**]{#struct_0_x9962_12256_1039236893}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37666135}

[[错误检测超时时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}]{#struct_0_x9962_12256_355634729}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1032524809}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1622326832}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_618810057}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_476273037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_948715312}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1749212994}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_x37731671}[：错误检测超时时间，取值范围为]{style="font-family:宋体"}[1000]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1143782849}

[[本命令与]{style="font-family:宋体"}**[timer error-detect]{lang="EN-US"}**]{#struct_0_x9962_12256_x1239242905}[命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1657263314}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_2092497892}[全局配置错误检测超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x38190422}

[\[Sysname\] fc timer error-detect 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_850073529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="EN-US"}**[ **error-detect**]{lang="EN-US"}]{#struct_0_x9962_12256_x664501137}
:::

::: {#-141892981 .myid}
[]{#_Toc404798125}[]{#struct_0_x9962_12256_x512715328}

**FC和FCoE \-- Fabric网络命令 \-- fc timer resource-allocation**

------------------------------------------------------------------------

[**[fc timer]{lang="EN-US"}**[ **resource-allocation**]{lang="EN-US"}]{#struct_0_x9962_12256_x1452068722}[命令用来全局配置资源分配超时时间。]{style="font-family:宋体"}

[**[undo fc timer]{lang="EN-US"}**[ **resource-allocation**]{lang="EN-US"}]{#struct_0_x9962_12256_276162885}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1155506871}

[**[fc timer resource-allocation]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_580937927}

[**[undo fc timer resource-allocation]{lang="EN-US"}**]{#struct_0_x9962_12256_x38255958}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1579029654}

[[资源分配超时时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}]{#struct_0_x9962_12256_x1861149800}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_399384023}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x32616768}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1957655502}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x577302740}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1319244945}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38059350}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_478728240}[：资源分配超时时间，取值范围为]{style="font-family:宋体"}[5000]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1044806010}

[[本命令与]{style="font-family:宋体"}**[timer resource-allocation]{lang="EN-US"}**]{#struct_0_x9962_12256_x1239242904}[命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1820351444}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x260088698}[全局配置资源分配超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x38124886}

[\[Sysname\] fc timer resource-allocation 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_560177002}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer resource-allocation]{lang="EN-US"}**]{#struct_0_x9962_12256_x177663094}
:::

::: {#1105465740 .myid}
[]{#_Toc69790683}[]{#_Toc297038080}[]{#_Toc296518428}[]{#_Toc404798126}[]{#struct_0_x9962_12256_x281053341}[]{#_Toc356214014}[]{#_Toc355594364}

**FC和FCoE \-- Fabric网络命令 \-- fc wwn default-fc4-type**

------------------------------------------------------------------------

[**[fc wwn default-fc4-type]{lang="EN-US"}**]{#struct_0_x9962_12256_x37928278}[命令用来配置节点设备的默认]{style="font-family:宋体"}[FC4]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[undo fc wwn default-fc4-type]{lang="EN-US"}**]{#struct_0_x9962_12256_165800715}[命令用来删除配置的节点设备的默认]{style="font-family:
宋体"}[FC4]{lang="EN-US"}[信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1580266712}

[**[fc wwn ]{lang="EN-US"}***[wwn-value ]{lang="EN-US"}***[default-fc4-type]{lang="EN-US"}**[ { *type-value* **feature** *feature-map \|* **scsi-fcp** **feature** { *feature-map \|* **both** *\|* **initiator** *\|* **target** } }]{lang="EN-US"}]{#struct_0_x9962_12256_x37993814}

[**[undo fc wwn ]{lang="EN-US"}***[wwn-value ]{lang="EN-US"}***[default-fc4-type]{lang="EN-US"}**[ { *type-value \|* **scsi-fcp** }]{lang="EN-US"}]{#struct_0_x9962_12256_x960078328}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_492600202}

[[没有配置节点设备的默认]{style="font-family:宋体"}[FC4]{lang="EN-US"}]{#struct_0_x9962_12256_1427179537}[信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37797206}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1986794476}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x850669997}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x37862742}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_947800518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1335250840}

[*[wwn-value]{lang="EN-US"}*]{#struct_0_x9962_12256_x37666134}[：]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[*[type-value]{lang="EN-US"}*]{#struct_0_x9962_12256_355634730}[：表示支持的]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[。]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[由]{style="font-family:宋体"}[256]{lang="EN-US"}[比特构成，每个比特位表示一种类型，某位比特的值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，则表示支持该比特位对应的类型。]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[值表示置位所支持的]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[的对应比特位，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[scsi-fcp]{lang="EN-US"}**]{#struct_0_x9962_12256_1306127344}[：表示支持的]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[为]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[，对应的]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[值为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[feature ]{lang="EN-US"}***[feature-map]{lang="EN-US"}*]{#struct_0_x9962_12256_x37731670}[：表示支持]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[值。每种协议共有四种属性，]{style="font-family:宋体"}[Feature]{lang="EN-US"}[值由]{style="font-family:宋体"}[4]{lang="EN-US"}[个比特组成，每个比特位表示一种属性，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。某位比特的值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，则表示支持该比特位对应的属性。[例如，]{#_Toc138129451}]{style="font-family:宋体"}[Feature]{lang="EN-US"}[值配置为]{style="font-family:宋体"}[15]{lang="EN-US"}[，表示节点设备对于该]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[对应的四种属性全部都支持。]{style="font-family:宋体"}[Feature]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不支持任何属性。当]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[为]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[时，用户还可配置如下参数：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[target]{lang="EN-US"}**]{#struct_0_x9962_12256_1143782848}[：]{lang="EN-US" style="font-family:宋体"}[表示支持]{style="font-family:宋体"}[target]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}[，对应的]{style="font-family:宋体"}*[feature-map]{lang="EN-US"}*[值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[initiator]{lang="EN-US"}**]{#struct_0_x9962_12256_1317952067}[：]{lang="EN-US" style="font-family:宋体"}[表示支持]{style="font-family:宋体"}[initiator]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}[，对应的]{style="font-family:宋体"}*[feature-map]{lang="EN-US"}*[值为]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[both]{lang="EN-US"}**]{#struct_0_x9962_12256_x38190425}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[同时支持]{lang="EN-US" style="font-family:宋体"}[initiator]{lang="EN-US"}[和]{style="font-family:宋体"}[target]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}[，对应的]{style="font-family:宋体"}*[feature-map]{lang="EN-US"}*[值为]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_850073528}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x299006851}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[为了不影响节点设备之间的互通，用户可以手工配置节点设备的默认]{style="font-family:宋体"}[FC4]{lang="EN-US"}]{#struct_0_x9962_12256_x664501138}[信息（]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[和]{style="font-family:宋体"}[Feature]{lang="EN-US"}[）。当节点设备不注册]{style="font-family:宋体"}[FC4]{lang="EN-US"}[信息并且交换机主动探测]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息也不成功时，名称服务数据库中记录的将是该默认]{style="font-family:宋体"}[FC4]{lang="EN-US"}[信息。此后，如果节点设备又主动注册了]{style="font-family:宋体"}[FC4]{lang="EN-US"}[信息或交换机又探测到了]{style="font-family:宋体"}[SCSI-FCP]{lang="EN-US"}[信息，则名称服务数据库中将保存节点设备注册或交换机探测到的]{style="font-family:宋体"}[FC4]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[配置本命令时，每条配置命令只能表示某个]{style="font-family:宋体"}[N_Port]{lang="EN-US"}]{#struct_0_x9962_12256_x511994432}[支持的一种]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[及其]{style="font-family:宋体"}[Feature]{lang="EN-US"}[，如果该]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[还支持其它]{style="font-family:宋体"}[FC4-Type]{lang="EN-US"}[及其]{style="font-family:宋体"}[Feature]{lang="EN-US"}[，则需要再配置一条命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38255961}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x377285489}[配置节点设备（其]{style="font-family:宋体"}[WWN]{lang="EN-US"}[为]{style="font-family:宋体"}[00:00:00:11:22:33:44:55]{lang="EN-US"}[）的默认]{style="font-family:宋体"}[FC4]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x38059353}

[\[Sysname\] fc wwn 00:00:00:11:22:33:44:55 default-fc4-type scsi-fcp feature target]{lang="EN-US"}

[\[Sysname\] fc wwn 00:00:00:11:22:33:44:55 default-fc4-type 9 feature 7]{lang="EN-US"}
:::

::: {#1863434130 .myid}
[]{#_Toc404798127}[]{#struct_0_x9962_12256_104277676}[]{#_Toc393700659}

**FC和FCoE \-- Fabric网络命令 \-- fcid persistent enable**

------------------------------------------------------------------------

[**[fcid]{lang="EN-US"}**[ **persistent** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_1906608089}[命令用来开启]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fcid** **persistent** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_900384904}[命令用来关闭]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x715301903}

[**[fcid]{lang="EN-US"}**[ **persistent** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_x861643328}

[**[undo]{lang="EN-US"}**[ **fcid** **persistent** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_1815314261}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_992925618}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x1865783172}[持久化功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1011771562}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x9859025}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1461806265}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1573746460}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_434827329}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1121565299}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_527291765}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_412772864}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启本功能后，手工配置的]{style="font-family:宋体"}]{#struct_0_x9962_12256_x239811554}[FCID]{lang="EN-US"}[持久化表项才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭本功能时，会删除所有静态和动态的]{style="font-family:宋体"}]{#struct_0_x9962_12256_979857015}[FCID]{lang="EN-US"}[持久化表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭本功能后，曾登录过的节点的]{style="font-family:宋体"}]{#struct_0_x9962_12256_2101573164}[WWN]{lang="EN-US"}[与]{style="font-family:宋体"}[FCID]{lang="EN-US"}[的对应关系也会被记录下来，在重新开启]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化功能时，系统会尝试将其恢复为动态的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。在此恢复过程中，如果]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项的总数达到了系统上限（]{style="font-family:宋体"}[40000]{lang="EN-US"}[条），系统会删除当前所有离线节点的动态表项后，再继续恢复。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1414752098}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1619423142}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内关闭]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_584558283}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] undo fcid persistent enable]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1966781952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wwn]{lang="EN-US"}**[ **fcid**]{lang="EN-US"}]{#struct_0_x9962_12256_1360753068}
:::

::: {#567732879 .myid}
[]{#_Toc404798128}[]{#struct_0_x9962_12256_850073527}[]{#_Toc367888363}[]{#_Toc369076707}[]{#_Toc367888364}[]{#_Toc369076708}[]{#_Toc367888365}[]{#_Toc369076709}[]{#_Toc367888366}[]{#_Toc369076710}[]{#_Toc367888367}[]{#_Toc369076711}[]{#_Toc367888368}[]{#_Toc369076712}[]{#_Toc367888369}[]{#_Toc369076713}[]{#_Toc367888370}[]{#_Toc369076714}[]{#_Toc367888371}[]{#_Toc369076715}[]{#_Toc367888372}[]{#_Toc369076716}[]{#_Toc367888373}[]{#_Toc369076717}[]{#_Toc367888374}[]{#_Toc369076718}[]{#_Toc367888375}[]{#_Toc369076719}[]{#_Toc367888376}[]{#_Toc369076720}[]{#_Toc367888377}[]{#_Toc369076721}[]{#_Toc367888378}[]{#_Toc369076722}[]{#_Toc367888379}[]{#_Toc369076723}[]{#_Toc367888380}[]{#_Toc369076724}[]{#_Toc367888381}[]{#_Toc369076725}[]{#_Toc367888382}[]{#_Toc369076726}[]{#_Toc367888383}[]{#_Toc369076727}[]{#_Toc367888384}[]{#_Toc369076728}[]{#_Toc367888385}[]{#_Toc369076729}[]{#_Toc367888386}[]{#_Toc369076730}[]{#_Toc352657995}[]{#_Toc352658435}[]{#_Toc352657996}[]{#_Toc352658436}[]{#_Toc352657997}[]{#_Toc352658437}[]{#_Toc352657998}[]{#_Toc352658438}[]{#_Toc352657999}[]{#_Toc352658439}[]{#_Toc352658000}[]{#_Toc352658440}[]{#_Toc352658001}[]{#_Toc352658441}[]{#_Toc352658002}[]{#_Toc352658442}[]{#_Toc352658003}[]{#_Toc352658443}[]{#_Toc352658004}[]{#_Toc352658444}[]{#_Toc352658005}[]{#_Toc352658445}[]{#_Toc352658006}[]{#_Toc352658446}[]{#_Toc352658007}[]{#_Toc352658447}[]{#_Toc352658008}[]{#_Toc352658448}[]{#_Toc352658009}[]{#_Toc352658449}[]{#_Toc352658010}[]{#_Toc352658450}[]{#_Toc352658011}[]{#_Toc352658451}[]{#_Toc352658012}[]{#_Toc352658452}[]{#_Toc352658013}[]{#_Toc352658453}[]{#_Toc352658014}[]{#_Toc352658454}[]{#_Toc352658015}[]{#_Toc352658455}[]{#_Toc352658016}[]{#_Toc352658456}[]{#_Toc352658017}[]{#_Toc352658457}[]{#_Toc352658018}[]{#_Toc352658458}[]{#_Toc352658019}[]{#_Toc352658459}[]{#_Toc352658020}[]{#_Toc352658460}[]{#_Toc352658021}[]{#_Toc352658461}[]{#_Toc352658022}[]{#_Toc352658462}[]{#_Toc367888387}[]{#_Toc369076731}[]{#_Toc367888388}[]{#_Toc369076732}[]{#_Toc367888389}[]{#_Toc369076733}[]{#_Toc367888390}[]{#_Toc369076734}[]{#_Toc367888391}[]{#_Toc369076735}[]{#_Toc367888392}[]{#_Toc369076736}[]{#_Toc367888393}[]{#_Toc369076737}[]{#_Toc367888394}[]{#_Toc369076738}[]{#_Toc367888395}[]{#_Toc369076739}[]{#_Toc367888396}[]{#_Toc369076740}[]{#_Toc367888397}[]{#_Toc369076741}[]{#_Toc367888398}[]{#_Toc369076742}[]{#_Toc367888399}[]{#_Toc369076743}[]{#_Toc367888400}[]{#_Toc369076744}[]{#_Toc367888401}[]{#_Toc369076745}[]{#_Toc367888402}[]{#_Toc369076746}[]{#_Toc324770319}[]{#_Toc324770320}[]{#_Toc324770321}[]{#_Toc324770322}[]{#_Toc324770323}[]{#_Toc324770324}[]{#_Toc324770325}[]{#_Toc324770326}[]{#_Toc324770327}[]{#_Toc324770328}[]{#_Toc324770329}[]{#_Toc324770330}[]{#_Toc324770331}[]{#_Toc324770332}[]{#_Toc324770333}[]{#_Toc324770334}[]{#_Toc324770335}[]{#_Toc324770336}[]{#_Toc324770337}[]{#_Toc324770338}[]{#_Toc324770339}[]{#_Toc324770340}[]{#_Toc367888403}[]{#_Toc369076747}[]{#_Toc367888404}[]{#_Toc369076748}[]{#_Toc367888405}[]{#_Toc369076749}[]{#_Toc367888406}[]{#_Toc369076750}[]{#_Toc367888407}[]{#_Toc369076751}[]{#_Toc367888408}[]{#_Toc369076752}[]{#_Toc367888409}[]{#_Toc369076753}[]{#_Toc367888410}[]{#_Toc369076754}[]{#_Toc367888411}[]{#_Toc369076755}[]{#_Toc367888412}[]{#_Toc369076756}[]{#_Toc367888413}[]{#_Toc369076757}[]{#_Toc367888414}[]{#_Toc369076758}[]{#_Toc367888415}[]{#_Toc369076759}[]{#_Toc367888416}[]{#_Toc369076760}[]{#_Toc367888417}[]{#_Toc369076761}[]{#_Toc367888418}[]{#_Toc369076762}[]{#_Toc367888419}[]{#_Toc369076763}[]{#_Toc367888420}[]{#_Toc369076764}[]{#_Toc367888421}[]{#_Toc369076765}[]{#_Toc367888422}[]{#_Toc369076766}[]{#_Toc367888423}[]{#_Toc369076767}[]{#_Toc367888424}[]{#_Toc369076768}[]{#_Toc367888425}[]{#_Toc369076769}[]{#_Toc367888426}[]{#_Toc369076770}[]{#_Toc367888427}[]{#_Toc369076771}[]{#_Toc367888428}[]{#_Toc369076772}[]{#_Toc367888429}[]{#_Toc369076773}[]{#_Toc367888430}[]{#_Toc369076774}[]{#_Toc367888431}[]{#_Toc369076775}[]{#_Toc367888432}[]{#_Toc369076776}

**FC和FCoE \-- Fabric网络命令 \-- priority**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**]{#struct_0_x9962_12256_x664501135}[命令用来配置交换机的优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_x9962_12256_x512846400}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_937802838}

[**[priority]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_x1741902401}

[**[undo priority]{lang="EN-US"}**]{#struct_0_x9962_12256_986335076}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38255960}

[[交换机]{style="font-family:宋体"}]{#struct_0_x9962_12256_x377285490}[的优先级为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38903899}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1628463323}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x863295017}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_937912232}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_943471652}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1629140594}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_x916776809}[：交换机的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[。优先级值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x38059352}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x2048546979}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[在一个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1412367036}[中，优先级高的交换机将优先被选为主交换机。同一台]{style="font-family:宋体"}[FC]{lang="EN-US"}[交换机在不同]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中的优先级可以不同。]{style="font-family:宋体"}

[[需要注意的是，交换机]{style="font-family:宋体"}]{#struct_0_x9962_12256_x820545050}[优先级的配置不能立即生效，需通过命令]{style="font-family:宋体"}**[domain restart]{lang="EN-US"}**[ **disruptive**]{lang="EN-US"}[进行一次中断重配置后才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_64398189}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1797499225}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置交换机的优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x38124888}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] priority 64]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_560177000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain restart]{lang="EN-US"}**]{#struct_0_x9962_12256_x177663092}
:::

::: {#1993875329 .myid}
[]{#_Toc404798129}[]{#struct_0_x9962_12256_x1058456202}[]{#_Toc393700660}

**FC和FCoE \-- Fabric网络命令 \-- reset fcid persistent**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **fcid** **persistent**]{lang="EN-US"}]{#struct_0_x9962_12256_x1181779675}[命令用来清除]{style="font-family:
宋体"}[FCID]{lang="EN-US"}[持久化表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x564621735}

[**[reset]{lang="EN-US"}**[ **fcid** **persistent** \[ **static** \] \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1670427153}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1709343866}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_555247979}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x442284858}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x711901637}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2088197735}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x115947426}

[**[static]{lang="EN-US"}**]{#struct_0_x9962_12256_1057834907}[：表示清除静态表项。如果未指定本参数，表示清除动态表项。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1359851107}[：清除指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，将清除所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1053379293}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_2073711680}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[需要注意的是，本命令不会清除在线节点的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x1385253948}[持久化表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2025412991}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_2079592722}[清除]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[下的所有动态]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。]{style="font-family:宋体"}

[[\<Sysname\> reset fcid persistent vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_519573981}
:::

::: {#-934500164 .myid}
[]{#_Toc291054587}[]{#_Toc239584272}[]{#_Toc404798130}[]{#struct_0_x9962_12256_x281184413}

**FC和FCoE \-- Fabric网络命令 \-- rscn aggregation enable**

------------------------------------------------------------------------

[**[rscn aggregation enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x101247276}[命令用来开启]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合功能。]{style="font-family:宋体"}

[**[undo rscn aggregation enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1225078}[命令用来关闭]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x932073983}

[**[rscn aggregation enable]{lang="EN-US"}**]{#struct_0_x9962_12256_272455234}

[**[undo rscn aggregation enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x37928280}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_121170707}

[[RSCN]{lang="EN-US"}]{#struct_0_x9962_12256_x169445018}[聚合功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1334601802}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_696098878}[视图]{style="font-family:宋体"}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x250899954}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1531305147}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2083987945}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37993816}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_507627739}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[RSCN]{lang="EN-US"}]{#struct_0_x9962_12256_x960078330}[聚合功能后，如果在]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合等待时间内，有多个节点设备产生变化事件，则使用携带了多个变化]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的一个]{style="font-family:宋体"}[ELS_RSCN]{lang="EN-US"}[报文，来代替以前只携带一个变化]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的多个]{style="font-family:宋体"}[ELS_RSCN]{lang="EN-US"}[报文，以此减少向关心该变化的节点设备发送]{style="font-family:宋体"}[ELS_RSCN]{lang="EN-US"}[报文的数量，减少变化通知次数。]{style="font-family:宋体"}

[[建议一个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_493124489}[内的所有交换机同时开启]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合功能，并配置相同的]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合等待时间，以避免可能产生的设备互通问题。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1980378599}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x783560010}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内开启]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1891679031}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] rscn aggregation enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1522274524}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rscn aggregation timer]{lang="EN-US"}**]{#struct_0_x9962_12256_901940546}
:::

::: {#960027826 .myid}
[]{#_Toc404798131}[]{#struct_0_x9962_12256_x37797208}

**FC和FCoE \-- Fabric网络命令 \-- rscn aggregation timer**

------------------------------------------------------------------------

[**[rscn aggregation timer]{lang="EN-US"}**]{#struct_0_x9962_12256_x1986794462}[命令用来配置]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合等待时间。]{style="font-family:宋体"}

[**[undo rscn aggregation timer]{lang="EN-US"}**]{#struct_0_x9962_12256_1474994367}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_129697358}

[**[rscn aggregation timer]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x9962_12256_x1115293251}

[**[undo rscn aggregation timer]{lang="EN-US"}**]{#struct_0_x9962_12256_x1194422001}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1539574739}

[[RSCN]{lang="EN-US"}]{#struct_0_x9962_12256_x37862744}[聚合等待时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_947800524}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_238727268}[视图]{style="font-family:宋体"}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x9962_12256_932807041}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x544517785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_884984367}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1545934385}

[*[time]{lang="EN-US"}*]{#struct_0_x9962_12256_695241794}[：]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合等待时间，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[2000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37666136}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x298941315}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[只有开启]{style="font-family:宋体"}[RSCN]{lang="EN-US"}]{#struct_0_x9962_12256_355634728}[聚合功能后，]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合等待时间才会生效。]{style="font-family:宋体"}

[[建议一个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1032524808}[内的所有交换机同时开启]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合功能，并配置相同的]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合等待时间，以避免可能产生的设备互通问题。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_56242891}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_420625684}[配置]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[聚合等待时间为]{style="font-family:宋体"}[1500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x261031837}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] rscn aggregation timer 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_450598140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rscn aggregation enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x542997960}
:::

::: {#-1429830885 .myid}
[]{#_Toc404798132}[]{#struct_0_x9962_12256_x1632206336}[]{#_Toc356224692}[]{#_Toc367888436}[]{#_Toc369076780}[]{#_Toc367888437}[]{#_Toc369076781}[]{#_Toc367888438}[]{#_Toc369076782}[]{#_Toc367888439}[]{#_Toc369076783}[]{#_Toc367888440}[]{#_Toc369076784}[]{#_Toc367888441}[]{#_Toc369076785}[]{#_Toc367888442}[]{#_Toc369076786}[]{#_Toc367888443}[]{#_Toc369076787}[]{#_Toc367888444}[]{#_Toc369076788}[]{#_Toc367888445}[]{#_Toc369076789}[]{#_Toc367888446}[]{#_Toc369076790}[]{#_Toc367888447}[]{#_Toc369076791}[]{#_Toc367888448}[]{#_Toc369076792}[]{#_Toc367888449}[]{#_Toc369076793}[]{#_Toc367888450}[]{#_Toc369076794}[]{#_Toc367888451}[]{#_Toc369076795}[]{#_Toc367888452}[]{#_Toc369076796}[]{#_Toc367888453}[]{#_Toc369076797}

**FC和FCoE \-- Fabric网络命令 \-- snmp-agent trap enable fc-fabric**

------------------------------------------------------------------------

[**[snmp-agent trap enable fc-fabric]{lang="EN-US"}**]{#struct_0_x9962_12256_157017484}[命令用来开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable fc-fabric]{lang="EN-US"}**]{#struct_0_x9962_12256_x1363940701}[命令用来关闭]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_220202839}

[**[snmp-agent trap enable fc-fabric]{lang="EN-US"}**[ \[ **domain-id-change** \| **fabric-change** \] \*]{lang="EN-US"}]{#struct_0_x9962_12256_156951948}

[**[undo snmp-agent trap enable fc-fabric]{lang="EN-US"}**[ \[ **domain-id-change** \| **fabric-change** \] \*]{lang="EN-US"}]{#struct_0_x9962_12256_1900421875}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_943888382}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_1534961736}[的告警功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_521445209}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x21099674}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1343046604}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1733149489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_156493193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2109880512}

[**[domain-id-change]{lang="EN-US"}**]{#struct_0_x9962_12256_1752628786}[：]{style="font-family:宋体"}[表示域]{style="font-family:宋体"}[ID]{lang="EN-US"}[变化的告警功能。开启本告警功能后，当本地交换机在所在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[发生变化时会生成告警信息，其中携带发生变化的]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[、本地交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[以及变化后的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[fabric-change]{lang="EN-US"}**]{#struct_0_x9962_12256_2132003246}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[变化的告警功能。开启了本告警功能后，当]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[进行重配置，即交换机收到或发送]{style="font-family:宋体"}[BF]{lang="EN-US"}[或]{style="font-family:宋体"}[RCF]{lang="EN-US"}[报文时（包括配置了拒绝收到的]{style="font-family:宋体"}[RCF]{lang="EN-US"}[请求报文的接口收到了]{style="font-family:宋体"}[RCF]{lang="EN-US"}[请求报文）会生成告警信息，其中携带进行]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[重配置的]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x649429703}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1414686562}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[如果未指定任何参数，则表示开启或关闭]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_1015360192}[的全部告警功能。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_974711451}[的告警功能之后，]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_952307634}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_147613749}[开启]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[的全部告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1948285928}

[\[Sysname\] snmp-agent trap enable fc-fabric]{lang="EN-US"}
:::

::: {#28199576 .myid}
[]{#_Toc404798133}[]{#struct_0_x9962_12256_723562074}[]{#_Toc385230674}

**FC和FCoE \-- Fabric网络命令 \-- snmp-agent trap enable fc-name-service**

------------------------------------------------------------------------

[**[snmp-agent trap enable fc-name-service]{lang="EN-US"}**]{#struct_0_x9962_12256_156362121}[命令用来开启名称服务的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable fc-name-service]{lang="EN-US"}**]{#struct_0_x9962_12256_974711456}[命令用来关闭名称服务的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1511835685}

[**[snmp-agent trap enable fc-name-service]{lang="EN-US"}**[ \[ **login** \| **logout** \] \*]{lang="EN-US"}]{#struct_0_x9962_12256_259285493}

[**[undo snmp-agent trap enable fc-name-service]{lang="EN-US"}**[ \[ **login** \| **logout** \] \*]{lang="EN-US"}]{#struct_0_x9962_12256_1928535340}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1069689496}

[[名称服务的告警功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x596928571}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2077327790}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_156296585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1915066798}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1963856302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x847573330}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x186737517}

[**[login]{lang="EN-US"}**]{#struct_0_x9962_12256_1005429471}[：表示]{style="font-family:宋体"}[节点向交换机注册名称服务信息的告警功能。开启本告警功能后，当本地交换机发生节点注册名称服务信息事件时会生成告警信息，其中携带]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[、本地交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[以及节点上]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[logout]{lang="EN-US"}**]{#struct_0_x9962_12256_156755337}[：表示]{style="font-family:宋体"}[节点向交换机注销名称服务信息的告警功能。开启本告警功能后，当本地交换机发生节点注销名称服务信息事件时会生成告警信息，其中携带]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[、本地交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[以及节点上]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_873705718}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x2048546975}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[如果未指定任何参数，则表示开启或关闭名称服务的全部告警功能。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x523775782}

[[开启了名称服务的告警功能之后，名称服务会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x9962_12256_974711454}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_110881103}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_156689801}[开启名称服务的全部告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1463177748}

[\[Sysname\] snmp-agent trap enable fc-name-service]{lang="EN-US"}
:::

::: {#1193300048 .myid}
[]{#_Toc404798134}[]{#struct_0_x9962_12256_x662776331}[]{#_Toc389831230}[]{#_Toc389831231}[]{#_Toc389831232}[]{#_Toc389831233}[]{#_Toc389831234}[]{#_Toc389831235}[]{#_Toc389831236}[]{#_Toc389831237}[]{#_Toc389831238}[]{#_Toc389831239}[]{#_Toc389831240}[]{#_Toc389831241}[]{#_Toc389831242}[]{#_Toc389831243}[]{#_Toc389831244}[]{#_Toc389831245}[]{#_Toc389831246}[]{#_Toc389831247}[]{#_Toc389831248}[]{#_Toc367888455}[]{#_Toc369076799}[]{#_Toc367888456}[]{#_Toc369076800}[]{#_Toc367888457}[]{#_Toc369076801}[]{#_Toc367888458}[]{#_Toc369076802}[]{#_Toc367888459}[]{#_Toc369076803}[]{#_Toc367888460}[]{#_Toc369076804}[]{#_Toc367888461}[]{#_Toc369076805}[]{#_Toc367888462}[]{#_Toc369076806}[]{#_Toc367888463}[]{#_Toc369076807}[]{#_Toc367888464}[]{#_Toc369076808}[]{#_Toc367888465}[]{#_Toc369076809}[]{#_Toc367888466}[]{#_Toc369076810}[]{#_Toc367888467}[]{#_Toc369076811}[]{#_Toc367888468}[]{#_Toc369076812}[]{#_Toc367888469}[]{#_Toc369076813}[]{#_Toc367888470}[]{#_Toc369076814}[]{#_Toc367888471}[]{#_Toc369076815}[]{#_Toc367888472}[]{#_Toc369076816}[]{#_Toc367888473}[]{#_Toc369076817}[]{#_Toc367888474}[]{#_Toc369076818}[]{#_Toc367888475}[]{#_Toc369076819}[]{#_Toc367888476}[]{#_Toc369076820}[]{#_Toc367888477}[]{#_Toc369076821}[]{#_Toc367888478}[]{#_Toc369076822}[]{#_Toc367888479}[]{#_Toc369076823}

**FC和FCoE \-- Fabric网络命令 \-- timer distributed-services**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **distributed-services**]{lang="EN-US"}]{#struct_0_x9962_12256_372563205}[命令用来在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内配置分布式服务超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **distributed-services**]{lang="EN-US"}]{#struct_0_x9962_12256_1006965978}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1814260173}

[**[timer distributed-services]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_x177601176}

[**[undo timer distributed-services]{lang="EN-US"}**]{#struct_0_x9962_12256_516656679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1872756424}

[[分布式服务超时时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}]{#struct_0_x9962_12256_1528090128}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1900006431}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1602001289}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1889167236}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1821543950}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_123971901}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_145245432}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_579228195}[：分布式服务超时时间，取值范围为]{style="font-family:宋体"}[5000]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1528286736}

[[本命令与]{style="font-family:宋体"}**[fc timer]{lang="EN-US"}**[ **distributed-services**]{lang="EN-US"}]{#struct_0_x9962_12256_x2048546974}[命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有]{style="font-family:
宋体"}[VSAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_460506136}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1128301439}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置分布式服务超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1967347551}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] timer distributed-services 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1528221200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fc timer]{lang="EN-US"}**[ **distributed-services**]{lang="EN-US"}]{#struct_0_x9962_12256_x1865701188}
:::

::: {#-1824440245 .myid}
[]{#_Toc404798135}[]{#struct_0_x9962_12256_957803744}

**FC和FCoE \-- Fabric网络命令 \-- timer error-detect**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **error-detect**]{lang="EN-US"}]{#struct_0_x9962_12256_811571609}[命令用来在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内配置错误检测超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **error-detect**]{lang="EN-US"}]{#struct_0_x9962_12256_x1269168168}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x229722324}

[**[timer error-detect]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_425978547}

[**[undo timer error-detect]{lang="EN-US"}**]{#struct_0_x9962_12256_691915117}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1528417808}

[[错误检测超时时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}]{#struct_0_x9962_12256_x1126973760}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2064329172}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1244982381}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_58874241}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1099286111}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x567317962}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_806441273}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_1528352272}[：错误检测超时时间，取值范围为]{style="font-family:宋体"}[1000]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_861281593}

[[本命令与]{style="font-family:宋体"}**[fc timer]{lang="EN-US"}**[ **error-detect**]{lang="EN-US"}]{#struct_0_x9962_12256_x2048546969}[命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1642400822}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1495221075}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置错误检测超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1527893521}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] timer error-detect 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1031049386}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fc timer]{lang="EN-US"}**[ **error-detect**]{lang="EN-US"}]{#struct_0_x9962_12256_1217152336}
:::

::: {#1261974448 .myid}
[]{#_Toc404798136}[]{#struct_0_x9962_12256_x1691739185}

**FC和FCoE \-- Fabric网络命令 \-- timer resource-allocation**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **resource-allocation**]{lang="EN-US"}]{#struct_0_x9962_12256_x1574393069}[命令用来在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内配置资源分配超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer** **resource-allocation**]{lang="EN-US"}]{#struct_0_x9962_12256_1444945381}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1508173030}

[**[timer resource-allocation]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_1933422384}

[**[undo timer resource-allocation]{lang="EN-US"}**]{#struct_0_x9962_12256_1527827985}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1025752644}

[[资源分配超时时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}]{#struct_0_x9962_12256_x1503781703}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1481487971}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1755234094}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_696034331}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_440767348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1561172746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1528024593}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_x668704404}[：资源分配超时时间，取值范围为]{style="font-family:宋体"}[5000]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1141437394}

[[本命令与]{style="font-family:宋体"}**[fc timer]{lang="EN-US"}**[ **resource-allocation**]{lang="EN-US"}]{#struct_0_x9962_12256_x2048546968}[命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[都有效，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[视图下的配置只对当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1272750983}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_835138718}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置资源分配超时时间为]{style="font-family:宋体"}[6000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1527959057}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] timer resource-allocation 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x942912466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fc timer]{lang="EN-US"}**[ **resource-allocation**]{lang="EN-US"}]{#struct_0_x9962_12256_1813260407}
:::

::: {#1050603374 .myid}
[]{#_Toc404798137}[]{#struct_0_x9962_12256_x1235614361}[]{#_Toc291054609}

**FC和FCoE \-- Fabric网络命令 \-- wwn fcid**

------------------------------------------------------------------------

[**[wwn]{lang="EN-US"}**[ **fcid**]{lang="EN-US"}]{#struct_0_x9962_12256_x155430785}[命令用来配置]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **wwn** **fcid**]{lang="EN-US"}]{#struct_0_x9962_12256_110162577}[命令用来删除]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1931515224}

[**[wwn]{lang="EN-US"}**[ *wwn-value* **fcid** *fcid-value* \[ **dynamic** \]]{lang="EN-US"}]{#struct_0_x9962_12256_1528155665}

[**[undo]{lang="EN-US"}**[ **wwn** *wwn-value* **fcid**]{lang="EN-US"}]{#struct_0_x9962_12256_x662841867}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x344353184}

[[不存在手工配置的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_x1314743206}[持久化表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1666995004}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1727224841}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x678927943}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1221413350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1528090129}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1900071967}

[*[wwn-value]{lang="EN-US"}*]{#struct_0_x9962_12256_1612699111}[：]{style="font-family:宋体"}[N_Port/NP_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[*[fcid-value]{lang="EN-US"}*]{#struct_0_x9962_12256_546911520}[：]{style="font-family:宋体"}[FCID]{lang="EN-US"}[的值，格式为]{style="font-family:宋体"}[xxxxxx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字，前两位表示]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[，中间两位表示]{style="font-family:宋体"}[Area_ID]{lang="EN-US"}[，后两位表示]{style="font-family:宋体"}[Port_ID]{lang="EN-US"}[。其中，]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[必须是本]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内正在运行的]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_x9962_12256_1314262329}[：表示动态的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。如果未指定本参数，表示静态的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。尽管节点上线时会自动生成动态的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项，但用户也可根据实际需要自行配置动态的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1648396720}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x92231841}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x785086406}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有开启了]{style="font-family:宋体"}]{#struct_0_x9962_12256_1738939439}[FCID]{lang="EN-US"}[持久化功能后，手工配置的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_x9962_12256_1528286737}[N_Port]{lang="EN-US"}[/NP_Port]{lang="EN-US"}[只能绑定一个]{style="font-family:宋体"}[FCID]{lang="EN-US"}[，一个]{style="font-family:宋体"}[FCID]{lang="EN-US"}[也只能与一个]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[/NP_Port]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要绑定的]{style="font-family:宋体"}]{#struct_0_x9962_12256_83315434}[N_Port]{lang="EN-US"}[/NP_Port]{lang="EN-US"}[如果已]{style="font-family:宋体"}[Login]{lang="EN-US"}[并分配了其它]{style="font-family:宋体"}[FCID]{lang="EN-US"}[，或者要绑定的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[已被分配给其它]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[/NP_Port]{lang="EN-US"}[，则不允许将二者绑定。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1058325130}[FCID]{lang="EN-US"}[持久化表项总数达到系统上限（]{style="font-family:宋体"}[40000]{lang="EN-US"}[条）后仍继续添加表项，系统会先删除当前所有离线节点的动态表项，如果所有表项均为静态表项，或对应节点均在线，则系统对此后收到的所有]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[请求均回应拒绝报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1483441475}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1124947119}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置如下静态]{style="font-family:宋体"}[FCID]{lang="EN-US"}[持久化表项：为]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[（]{style="font-family:宋体"}[WWN]{lang="EN-US"}[为]{style="font-family:宋体"}[33:e8:00:05:30:00:16:df]{lang="EN-US"}[）绑定]{style="font-family:宋体"}[Area_ID]{lang="EN-US"}[为]{style="font-family:宋体"}[03]{lang="EN-US"}[、]{style="font-family:宋体"}[Port_ID]{lang="EN-US"}[为]{style="font-family:宋体"}[12]{lang="EN-US"}[的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[，当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内运行的]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[为]{style="font-family:宋体"}[01]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x900284897}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] wwn 33:e8:00:05:30:00:16:df fcid 010312]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1670558225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcid]{lang="EN-US"}**[ **persistent** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_x1248292979}
:::

::: {#1928141858 .myid}
[]{#_Toc404798139}[]{#struct_0_x9962_12256_x1656033273}[]{#_Toc295400761}

**FC和FCoE \-- FC路由与转发配置命令 \-- display fc exchange**

------------------------------------------------------------------------

[**[display fc exchange]{lang="EN-US"}**]{#struct_0_x9962_12256_x835444624}[命令用来显示]{style="font-family:宋体"}[FC Exchange]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1105793065}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9962_12256_2106961652}

[**[display fc exchange]{lang="EN-US"}**[ { **link** \| **protocol** }]{lang="EN-US"}]{#struct_0_x9962_12256_x375158090}

[**[display fc exchange link verbose]{lang="EN-US"}**[ \[ **exid** *exid* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1528286735}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9962_12256_83446506}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display fc exchange]{lang="EN-US"}**[ { **link** \| **protocol** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x605145888}

[**[display fc exchange link verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **exid** *exid* \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_x415811619}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9962_12256_208232069}[模式：]{style="font-family:宋体"}

[**[display fc exchange]{lang="EN-US"}**[ { **link** \| **protocol** } \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1528221199}

[**[display fc exchange link verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **exid** *exid* \] \]]{lang="EN-US"}]{#struct_0_x9962_12256_854829237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_566981739}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_329806229}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1528417807}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1127694656}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1177361590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x252460920}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1123873419}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_365400232}

[**[link]{lang="EN-US"}**]{#struct_0_x9962_12256_1091580758}[：显示连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**]{#struct_0_x9962_12256_1358977031}[：显示协议]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[verbose]{lang="SV"}**]{#struct_0_x9962_12256_1528352271}[：显示连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项的详细信息。]{style="font-family:宋体"}

[**[exid]{lang="SV"}**]{#struct_0_x9962_12256_861084985}[ ]{lang="SV"}[[exid]{lang="SV"}]{.commandparameterChar}[：显示指定]{style="font-family:宋体"}[Exchange ID]{lang="EN-US"}[的连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}[[exid]{lang="SV"}]{.commandparameterChar}[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。如果不指定本参数，则显示所有连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_x9962_12256_728780789}[ ]{lang="SV"}[[slot-number]{lang="SV"}]{.commandparameterChar}[：显示指定单板上的信息。]{style="font-family:宋体"}[[slot-number]{lang="SV"}]{.commandparameterChar}[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_281328828}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备上的信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_x809601122}*[slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_x1994875582}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ **slot** ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备指定单板上的信息。]{style="font-family:宋体"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_x1769445827}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ **slot** ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定单板上的信息。]{style="font-family:宋体"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2031608354}

[[Exchange]{lang="SV"}]{#struct_0_x9962_12256_x1223832669}[是]{style="font-family:宋体"}[FC]{lang="SV"}[协议的基本概念]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[所有数据帧和控制帧的传输都要基于]{style="font-family:
宋体"}[Exchange]{lang="SV"}[完成。]{style="font-family:
宋体"}

[[一个]{style="font-family:宋体"}[Exchange]{lang="EN-US"}]{#struct_0_x9962_12256_1527893516}[表示两个通讯实体间的一次数据交换，可以包含多次双向的报文交互。]{style="font-family:宋体"}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1030983849}[协议中的任意一次数据交互或协议报文交互都要创建一对]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[结构（发起端]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[和回应端]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[），基于这一对]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[来完成报文的发送和接收，对于提供可靠传输服务的服务级别（]{style="font-family:宋体"}[Class 1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[），基于这对]{style="font-family:
宋体"}[Exchange]{lang="EN-US"}[来完成报文的确认、错误检测、报文重传。]{style="font-family:宋体"}

[[Exchange]{lang="EN-US"}]{#struct_0_x9962_12256_1658882195}[分为两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1975960869}[Exchange]{lang="EN-US"}[：只存在于服务器端，基于协议号和]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[创建，用于监听连接建立。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[连接]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}]{#struct_0_x9962_12256_1833387821}[：同时存在于数据交互的两端，基于]{lang="EN-US" style="font-family:宋体"}[Exchange ID]{lang="EN-US"}[创建，用于报文交互。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_914601839}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1739585987}[显示协议]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display fc exchange protocol]{lang="EN-US"}]{#struct_0_x9962_12256_1527827980}

[ Local_ID:EXID     Remote_ID:EXID     State       Protocol]{lang="EN-US"}

[ 0x000000:65535    0x000000:65535     LISTEN      5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1025424964}[显示协议]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display fc exchange protocol slot 1]{lang="EN-US"}]{#struct_0_x9962_12256_x1410899730}

[ Local_ID:EXID     Remote_ID:EXID     State       Slot  Protocol]{lang="EN-US"}

[ 0x000000:65535    0x000000:65535     LISTEN      1     6]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x390031797}[显示协议]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display fc exchange protocol chassis 1 slot 2]{lang="EN-US"}]{#struct_0_x9962_12256_1412083869}

[ Local_ID:EXID     Remote_ID:EXID     State       Chassis Slot  Protocol]{lang="EN-US"}

[ 0x000000:65535    0x000000:65535     LISTEN      1       2     13]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x409426086}[显示连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display fc exchange link]{lang="EN-US"}]{#struct_0_x9962_12256_1528024588}

[ Local_ID:EXID     Remote_ID:EXID     State       Protocol]{lang="EN-US"}

[ 0x060501:1024     0x010001:1025      ESTABLISHED 7]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x669425301}[显示连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display fc exchange link slot 2]{lang="EN-US"}]{#struct_0_x9962_12256_x827758518}

[ Local_ID:EXID     Remote_ID:EXID     State       Slot  Protocol]{lang="EN-US"}

[ 0x060501:1024     0x010001:1025      ESTABLISHED 2     8]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1493850540}[显示连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display fc exchange link chassis 3 slot 5]{lang="EN-US"}]{#struct_0_x9962_12256_526436978}

[ Local_ID:EXID     Remote_ID:EXID     State       Chassis Slot  Protocol]{lang="EN-US"}

[ 0x060501:1024     0x010001:1025      ESTABLISHED 3       5     11]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x208399706}[显示连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[表项详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc exchange link verbose slot 1]{lang="EN-US"}]{#struct_0_x9962_12256_1527959052}

[ slot: 1]{lang="EN-US"}

[ protocol: 8]{lang="EN-US"}

[ connection info: Local = 0x090801:1155 ,  Remote = 0x050001:1089]{lang="EN-US"}

[ PCB flags: 0x2]{lang="EN-US"}

[ FC Class: FC_CLASS_F]{lang="EN-US"}

[ connection state: ESTABLISHED]{lang="EN-US"}

[ VSAN ID: 25]{lang="EN-US"}

[[表1-30 ]{lang="EN-US"}[display fc exchange]{lang="EN-US"}]{#struct_0_x9962_12256_x943109074}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1336649353}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x982242759}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x946250995}

[[Local_ID:EXID/Local]{lang="EN-US"}]{#struct_0_x9962_12256_783356067}

[[本端]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1528155660}[地址及]{style="font-family:宋体"}[Exchange ID]{lang="EN-US"}[（对于协议]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[来说，此值没有意义）]{style="font-family:宋体"}

[[Remote_ID:EXID/Remote]{lang="EN-US"}]{#struct_0_x9962_12256_x663038475}

[[对端]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x357794938}[地址及]{style="font-family:宋体"}[Exchange ID]{lang="EN-US"}[（对于协议]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[来说，此值没有意义）]{style="font-family:宋体"}

[[State/connection state]{lang="EN-US"}]{#struct_0_x9962_12256_x1728307133}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x9962_12256_1789866404}[的连接状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PREPARE]{lang="EN-US"}]{#struct_0_x9962_12256_1528090124}[：表示协议]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[绑定成功]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[等待回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_x9962_12256_x1899744287}[：表示协议]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[监听连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_x9962_12256_683798833}[：表示连接建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABTS]{lang="EN-US"}]{#struct_0_x9962_12256_214670610}[：表示连接超时或出错后发送了]{lang="EN-US" style="font-family:宋体"}[ABTS]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[ABTS ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BA_ACC]{lang="EN-US"}]{#struct_0_x9962_12256_x1669432428}[：表示收到了]{lang="EN-US" style="font-family:宋体"}[ABTS]{lang="EN-US"}[并回应了]{lang="EN-US" style="font-family:宋体"}[BA_ACC]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[ACC ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABTS_ACK]{lang="EN-US"}]{#struct_0_x9962_12256_x1593452150}[：表示收到了]{lang="EN-US" style="font-family:宋体"}[ABTS ACK]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[BA_ACC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_x9962_12256_1528286732}[：表示连接关闭]{lang="EN-US" style="font-family:宋体"}

[[Slot/slot]{lang="EN-US"}]{#struct_0_x9962_12256_83512042}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x9962_12256_x1378532429}[建立所在的单板]{style="font-family:宋体"}

[[Protocol/protocol]{lang="EN-US"}]{#struct_0_x9962_12256_x710661763}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1528221196}[协议号，标识协议类型]{style="font-family:宋体"}

[[PCB flags]{lang="EN-US"}]{#struct_0_x9962_12256_855681205}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x9962_12256_x666151314}[状态控制标志位（一共]{style="font-family:宋体"}[4]{lang="EN-US"}[位）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_x9962_12256_144479578}[：该位取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[标识发送端，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[标识回应端]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_x9962_12256_x2048989796}[：该位取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[标识无主动权，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[标识有主动权]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x4]{lang="EN-US"}]{#struct_0_x9962_12256_1528417804}[：该位取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[标识]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[连接的第一个报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x8]{lang="EN-US"}]{#struct_0_x9962_12256_x1127760192}[：该位取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[标识]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[正在等待老化]{style="font-family:宋体"}

[[FC Class]{lang="EN-US"}]{#struct_0_x9962_12256_817143934}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x261671755}[连接服务级别，包含如下几种（其中]{style="font-family:宋体"}[FC_CLASS_3]{lang="EN-US"}[不需要回应]{style="font-family:宋体"}[ACK]{lang="EN-US"}[）：]{style="font-family:宋体"}

[[FC_CLASS_1]{lang="EN-US"}]{#struct_0_x9962_12256_1528352268}[、]{style="font-family:宋体"}[FC_CLASS_2]{lang="EN-US"}[、]{style="font-family:宋体"}[FC_CLASS_3]{lang="EN-US"}[、]{style="font-family:宋体"}[FC_CLASS_F]{lang="EN-US"}[、]{style="font-family:宋体"}[FC_CLASS_6]{lang="EN-US"}

[[VSAN ID]{lang="EN-US"}]{#struct_0_x9962_12256_860626234}

[[虚拟存储局域网索引]{style="font-family:宋体"}]{#struct_0_x9962_12256_1397707906}

[ ]{lang="EN-US"}

::: {#35369373 .myid}
[]{#_Toc404798140}[]{#struct_0_x9962_12256_x2122396441}[]{#_Toc295400763}

**FC和FCoE \-- FC路由与转发配置命令 \-- display fc fib**

------------------------------------------------------------------------

[**[display fc fib]{lang="EN-US"}**]{#struct_0_x9962_12256_x583430006}[命令用来显示]{style="font-family:宋体"}[FC FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1527893517}

[**[display fc fib]{lang="EN-US"}**[ \[ *fcid* \[ *mask-length* \] \] **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1030918313}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1508067123}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x640486644}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1902619217}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_992385190}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x637090037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1617748401}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1527827981}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1025490500}

[[[fcid]{lang="SV"}]{.commandparameterChar}]{#struct_0_x9962_12256_x1101515940}[：显示指定目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[FC FIB]{lang="EN-US"}[表项信息，取值范围为]{style="font-family:宋体"}[0x000000]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFFFF]{lang="EN-US"}[（十六进制）。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x9962_12256_x1217477271}[：目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vsan]{lang="SV"}**]{#struct_0_x9962_12256_812269774}[ ]{lang="SV"}[[vsan-id]{lang="SV"}]{.commandparameterChar}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FC FIB]{lang="SV"}[表项信息，]{style="font-family:宋体"}[vsan-id]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1564944240}

[[FC FIB]{lang="EN-US"}]{#struct_0_x9962_12256_1721506123}[提供以]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[和目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为索引的表项查询，为转发报文和本机发送报文提供出接口信息。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_111954440}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}*[fcid]{lang="EN-US"}*]{#struct_0_x9962_12256_1528024589}[和]{lang="EN-US" style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[，则显示指定目的]{lang="EN-US" style="font-family:宋体"}[FC]{lang="EN-US"}[地址和掩码长度的]{lang="EN-US" style="font-family:宋体"}[FC FIB]{lang="EN-US"}[表项信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9962_12256_x669359765}*[fcid]{lang="SV"}*[，]{lang="EN-US" style="font-family:宋体"}[不指定]{lang="EN-US" style="font-family:宋体"}*[mask-length]{lang="SV"}*[，则]{lang="EN-US" style="font-family:宋体"}[按照最长匹配原则显示指定目的]{lang="EN-US" style="font-family:
宋体"}[FC]{lang="SV"}[地址的]{lang="EN-US" style="font-family:宋体"}[FC FIB]{lang="SV"}[表项信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9962_12256_23392447}*[fcid]{lang="SV"}*[和]{lang="EN-US" style="font-family:宋体"}*[mask-length]{lang="SV"}*[，]{lang="EN-US" style="font-family:宋体"}[则显示指定]{lang="EN-US" style="font-family:宋体"}[VSAN]{lang="SV"}[内所有的]{lang="EN-US" style="font-family:宋体"}[FC FIB]{lang="SV"}[表项信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1497117327}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_325963047}[显示]{style="font-family:宋体"}[VSAN 18]{lang="EN-US"}[内所有的]{style="font-family:宋体"}[FC FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc fib vsan 18]{lang="EN-US"}]{#struct_0_x9962_12256_1527959053}

[FC FIB information in VSAN 18:]{lang="EN-US"}

[  Destination count: 6]{lang="EN-US"}

[  FIB entry count: 7]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/Mask              Interface]{lang="EN-US"}

[  0x030100/16                   Fc1/0/1]{lang="EN-US"}

[  0x030100/16                   Fc1/0/2]{lang="EN-US"}

[  0x030100/24                   Fc1/0/3]{lang="EN-US"}

[  0xfffc01/24                   InLoop0]{lang="EN-US"}

[  0xfffffa/24                   InLoop0]{lang="EN-US"}

[  0xfffffc/24                   InLoop0]{lang="EN-US"}

[  0xfffffd/24                   InLoop0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x943174610}[按照最长匹配原则显示指定目的]{style="font-family:宋体"}[FC]{lang="SV"}[地址的]{style="font-family:宋体"}[FC FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc fib 030100 vsan 18]{lang="EN-US"}]{#struct_0_x9962_12256_x1716109728}

[FC FIB information in VSAN 18:]{lang="EN-US"}

[  Destination count: 1]{lang="EN-US"}

[  FIB entry count: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/Mask              Interface]{lang="EN-US"}

[  0x030100/24                   Fc1/0/3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1535299909}[显示指定目的]{style="font-family:宋体"}[FC]{lang="SV"}[地址和掩码长度的]{style="font-family:宋体"}[FC FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc fib 030100 16 vsan 18]{lang="EN-US"}]{#struct_0_x9962_12256_1528155661}

[FC FIB information in VSAN 18:]{lang="EN-US"}

[  Destination count: 1]{lang="EN-US"}

[  FIB entry count: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/Mask              Interface]{lang="EN-US"}

[  0x030100/16                   Fc1/0/1]{lang="EN-US"}

[  0x030100/16                   Fc1/0/2]{lang="EN-US"}

[[表1-31 ]{lang="EN-US"}[display fc fib]{lang="EN-US"}]{#struct_0_x9962_12256_x663104011}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1331702369}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1556673323}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x662321413}

[[Destination count]{lang="EN-US"}]{#struct_0_x9962_12256_415471004}

[[显示表项中目的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_514330743}[地址个数]{style="font-family:宋体"}

[[FIB entry count]{lang="EN-US"}]{#struct_0_x9962_12256_x266081295}

[[显示表项中实际表项个数，包含等价路由]{style="font-family:宋体"}]{#struct_0_x9962_12256_1528090125}

[[Destination/Mask]{lang="EN-US"}]{#struct_0_x9962_12256_x1899809823}

[[目的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1132293565}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码长度]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1557380637}

[[出接口]{style="font-family:宋体"}]{#struct_0_x9962_12256_115025200}

[ ]{lang="EN-US"}

::: {#-2121895596 .myid}
[]{#_Toc404798141}[]{#struct_0_x9962_12256_1528286733}[]{#_Toc297214173}

**FC和FCoE \-- FC路由与转发配置命令 \-- display fc routing-table**

------------------------------------------------------------------------

[**[display fc routing-table]{lang="EN-US"}**]{#struct_0_x9962_12256_83577578}[命令用来显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_975300061}

[**[display fc routing-table]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \] \[ **statistics** \| **verbose** \]]{lang="EN-US"}]{#struct_0_x9962_12256_986858137}

[**[display fc routing-table]{lang="EN-US"}**[ **vsan** *vsan-id* *fcid* \[ *mask* \| *mask-length* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x9962_12256_915138023}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1129988927}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_677697423}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1528221197}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_855746741}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1391194633}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_872265255}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1524840055}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x778489124}

[**[vsan]{lang="EN-US"}***[ vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x54466291}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的路由信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。不指定该参数时，显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[*[fcid]{lang="DE"}*]{#struct_0_x9962_12256_x1413470118}[：指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[静态路由的目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址，取值范围为]{style="font-family:宋体"}[0x010000]{lang="EN-US"}[～]{style="font-family:宋体"}[0xEFFFFF]{lang="EN-US"}[（十六进制）。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x9962_12256_1528417805}[：]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的十六进制掩码，与]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[配合使用。取值为]{style="font-family:宋体"}[0xFF0000]{lang="EN-US"}[、]{style="font-family:宋体"}[0xFFFF00]{lang="EN-US"}[、]{style="font-family:宋体"}[0xFFFFFF]{lang="EN-US"}[。不指定该参数时，将显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由表内所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[，且掩码是]{style="font-family:宋体"}[0xFF0000]{lang="EN-US"}[、]{style="font-family:宋体"}[0xFFFF00]{lang="EN-US"}[和]{style="font-family:宋体"}[0xFFFFFF]{lang="EN-US"}[的路由。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x9962_12256_x1127825728}[：]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的十进制掩码，与]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[配合使用。取值为]{style="font-family:宋体"}[8]{lang="EN-US"}[、]{style="font-family:宋体"}[16]{lang="EN-US"}[、]{style="font-family:宋体"}[24]{lang="EN-US"}[。不指定该参数时，将显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由表内所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[，且掩码是]{style="font-family:宋体"}[8]{lang="EN-US"}[、]{style="font-family:宋体"}[16]{lang="EN-US"}[和]{style="font-family:宋体"}[24]{lang="EN-US"}[的路由。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_x9962_12256_969686066}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由表的统计信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9962_12256_549746498}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由表的详细信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1837111953}

[[路由表中保存了各种路由协议发现的路由。通过本命令可以查看路由表的概要信息、详细信息以及统计信息。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x972644250}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1128606416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[statistics]{lang="EN-US"}**]{#struct_0_x9962_12256_1016982540}[和]{lang="EN-US" style="font-family:宋体"}**[verbose]{lang="EN-US"}**[，将显示]{lang="EN-US" style="font-family:宋体"}[FC]{lang="EN-US"}[路由表的概要信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在显示]{style="font-family:宋体"}]{#struct_0_x9962_12256_x809887028}[FC]{lang="EN-US"}[路由表的概要信息时，将只显示激活的路由；在显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由表的详细信息时，将显示所有激活和非激活的路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1528352269}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_860560698}[显示]{style="font-family:宋体"}[VSAN 5]{lang="EN-US"}[内所有路由的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc routing-table vsan 5]{lang="EN-US"}]{#struct_0_x9962_12256_1932535422}

[Routing Table: VSAN 5]{lang="EN-US"}

[  Destinations : 5          Routes : 8]{lang="EN-US"}

[  Destination/mask   Protocol   Preference   Cost     Interface]{lang="EN-US"}

[  0x040000/8         FSPF       20           100      Vfc10]{lang="EN-US"}

[  0x040000/8         FSPF       20           100      Vfc20]{lang="EN-US"}

[  0x040000/8         FSPF       20           100      Vfc30]{lang="EN-US"}

[  0x040000/8         FSPF       20           100      Vfc40]{lang="EN-US"}

[  0xfffc01/24        DIRECT     0            0        InLoop0]{lang="EN-US"}

[  0xfffffa/24        DIRECT     0            0        InLoop0]{lang="EN-US"}

[  0xfffffc/24        DIRECT     0            0        InLoop0]{lang="EN-US"}

[  0xfffffd/24        DIRECT     0            0        InLoop0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x488321681}[显示]{style="font-family:宋体"}[VSAN 5]{lang="EN-US"}[内所有路由的的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc routing-table vsan 5 verbose]{lang="EN-US"}]{#struct_0_x9962_12256_x1201055371}

[Routing Table: VSAN 5]{lang="EN-US"}

[  Destinations : 5          Routes : 5]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/mask: 0x120000/8]{lang="EN-US"}

[          Protocol: STATIC]{lang="EN-US"}

[        Preference: 10]{lang="EN-US"}

[              Cost: 0]{lang="EN-US"}

[         Interface: Fc1/0/1]{lang="EN-US"}

[             State: Active]{lang="EN-US"}

[               Age: 0h21m36s]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/mask: 0xfffc01/24]{lang="EN-US"}

[          Protocol: DIRECT]{lang="EN-US"}

[        Preference: 0]{lang="EN-US"}

[              Cost: 0]{lang="EN-US"}

[         Interface: InLoop0]{lang="EN-US"}

[             State: Active]{lang="EN-US"}

[               Age: 0h21m36s]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/mask: 0xfffffa/24]{lang="EN-US"}

[          Protocol: DIRECT]{lang="EN-US"}

[        Preference: 0]{lang="EN-US"}

[              Cost: 0]{lang="EN-US"}

[         Interface: InLoop0]{lang="EN-US"}

[             State: Active]{lang="EN-US"}

[               Age: 0h21m36s]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/mask: 0xfffffc/24]{lang="EN-US"}

[          Protocol: DIRECT]{lang="EN-US"}

[        Preference: 0]{lang="EN-US"}

[              Cost: 0]{lang="EN-US"}

[         Interface: InLoop0]{lang="EN-US"}

[             State: Active]{lang="EN-US"}

[               Age: 0h21m36s]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination/mask: 0xfffffd/24]{lang="EN-US"}

[          Protocol: DIRECT]{lang="EN-US"}

[        Preference: 0]{lang="EN-US"}

[              Cost: 0]{lang="EN-US"}

[         Interface: InLoop0]{lang="EN-US"}

[             State: Active]{lang="EN-US"}

[               Age: 0h21m36s]{lang="EN-US"}

[[表1-32 ]{lang="EN-US"}[display fc routing-table]{lang="EN-US"}]{#struct_0_x9962_12256_1001336879}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1327442197}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200858763}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1478747902}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_2065573891}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2020432586}[编号]{style="font-family:宋体"}

[[Destinations]{lang="EN-US"}]{#struct_0_x9962_12256_1485165369}

[[不同目的地址的个数]{style="font-family:宋体"}]{#struct_0_x9962_12256_1849802332}

[[Routes]{lang="EN-US"}]{#struct_0_x9962_12256_x1200924299}

[[路由条数]{style="font-family:宋体"}]{#struct_0_x9962_12256_332112618}

[[Destination/mask]{lang="EN-US"}]{#struct_0_x9962_12256_389759489}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_683156213}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x9962_12256_569958404}

[[协议类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1200727691}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DIRECT]{lang="EN-US"}]{#struct_0_x9962_12256_1889991126}[：表示直连路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_x9962_12256_808446692}[：表示静态路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_205355467}[：表示]{lang="EN-US" style="font-family:宋体"}[FSPF]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_x9962_12256_835209150}

[[路由的优先级]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1068381697}

[[Cost]{lang="EN-US"}]{#struct_0_x9962_12256_1062997121}

[[路由的度量值]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1200793227}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1092073431}

[[出接口]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1090782499}

[[State]{lang="EN-US"}]{#struct_0_x9962_12256_x1473723376}

[[路由状态，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1603460072}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x9962_12256_x838892229}[：表示激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x9962_12256_x1242176756}[：表示非激活]{lang="EN-US" style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_x9962_12256_x1200596619}

[[路由在路由表中存在的时间，格式为：]{style="font-family:宋体"}[XXhXXmXXs]{lang="EN-US"}]{#struct_0_x9962_12256_x1374904055}[（]{style="font-family:宋体"}[XX]{lang="EN-US"}[小时]{style="font-family:宋体"}[XX]{lang="EN-US"}[分钟]{style="font-family:宋体"}[XX]{lang="EN-US"}[秒）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1641117616}[显示]{style="font-family:宋体"}[VSAN 5]{lang="EN-US"}[内所有路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc routing-table vsan 5 statistics]{lang="EN-US"}]{#struct_0_x9962_12256_x929951823}

[Routing Table: VSAN 5]{lang="EN-US"}

[  Protocol  route       active      added       deleted]{lang="EN-US"}

[  DIRECT    4           4           4           0]{lang="EN-US"}

[  STATIC    1           1           1           0]{lang="EN-US"}

[  FSPF      0           0           0           0]{lang="EN-US"}

[  Total     5           5           5           0]{lang="EN-US"}

[[表1-33 ]{lang="EN-US"}[display fc routing-table statistics]{lang="EN-US"}]{#struct_0_x9962_12256_1602123350}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1087926709}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200662155}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1321183897}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x415703154}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x143035156}[编号]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x9962_12256_2089595540}

[[协议类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1200465547}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DIRECT]{lang="EN-US"}]{#struct_0_x9962_12256_x79377342}[：表示直连路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_x9962_12256_581224564}[：表示静态路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_730616368}[：表示]{lang="EN-US" style="font-family:宋体"}[FSPF]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}

[[route]{lang="EN-US"}]{#struct_0_x9962_12256_x29409639}

[[协议类型]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x9962_12256_x1783558546}[下的路由数]{style="font-family:宋体"}

[[active]{lang="EN-US"}]{#struct_0_x9962_12256_x1331472893}

[[协议类型]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x9962_12256_1289500867}[下的激活路由数]{style="font-family:宋体"}

[[added]{lang="EN-US"}]{#struct_0_x9962_12256_x1200531083}

[[协议类型]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x9962_12256_x1558677893}[下添加的路由数]{style="font-family:宋体"}

[[deleted]{lang="EN-US"}]{#struct_0_x9962_12256_36931189}

[[协议类型]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x9962_12256_x275078185}[下删除的路由数]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_x9962_12256_x1612555077}

[[总计]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1200989834}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_645929417}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fc route-static]{lang="EN-US"}**]{#struct_0_x9962_12256_1706243297}

::: {#1203850968 .myid}
[]{#_Toc404798142}[]{#struct_0_x9962_12256_1560129417}[]{#_Toc316392298}[]{#_Toc316371522}

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf graceful-restart**

------------------------------------------------------------------------

[**[display fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_x274914450}[命令用来显示]{style="font-family:
宋体"}[FSPF GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x902376115}

[**[display fspf graceful-restart]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x786048456}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1720672470}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1201055370}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1727546476}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_922642717}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x556213146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1057582063}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1197154674}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x208684948}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1699888108}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF GR]{lang="EN-US"}[状态信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200858762}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_373606619}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看]{style="font-family:宋体"}[FSPF GR]{lang="EN-US"}]{#struct_0_x9962_12256_87336039}[状态信息，包括是否开启]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[、]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[以及正在重启的]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[数量、正在协助本机重启的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[数量等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x32933184}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_958756246}[显示]{style="font-family:宋体"}[FSPF GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display fspf graceful-restart]{lang="EN-US"}]{#struct_0_x9962_12256_1183230910}

[Graceful-restart capability      : Disable]{lang="EN-US"}

[Helper capability                : Enable]{lang="EN-US"}

[Graceful-restart period          : 120 seconds]{lang="EN-US"}

[ ]{lang="EN-US"}

[FSPF graceful restart information of VSAN 1:]{lang="EN-US"}

[  Number of neighbors under helper : 0]{lang="EN-US"}

[  Number of restarting neighbors   : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[FSPF graceful restart information of VSAN 2:]{lang="EN-US"}

[  Number of neighbors under helper : 0]{lang="EN-US"}

[  Number of restarting neighbors   : 0]{lang="EN-US"}

[[表1-34 ]{lang="EN-US"}[display fspf graceful-restart]{lang="EN-US"}]{#struct_0_x9962_12256_x1200924298}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1088794241}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1233971323}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x386050283}

[[Graceful-restart capability]{lang="EN-US"}]{#struct_0_x9962_12256_x1450949634}

[[是否开启]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x9962_12256_910835036}[能力，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[nable]{lang="EN-US"}]{#struct_0_x9962_12256_x1706409453}[：表示开启]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x9962_12256_x1200727690}[：表示未开启]{style="font-family:宋体"}

[[Helper capability]{lang="EN-US"}]{#struct_0_x9962_12256_x730874791}

[[是否开启]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_x9962_12256_x1313075021}[能力，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[nable]{lang="EN-US"}]{#struct_0_x9962_12256_289492919}[：表示开启]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x9962_12256_x698863257}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[未开启]{lang="EN-US" style="font-family:宋体"}

[[Graceful-restart period]{lang="EN-US"}]{#struct_0_x9962_12256_x1200793226}

[[GR]{lang="EN-US"}]{#struct_0_x9962_12256_x1636809924}[最大间隔时间]{style="font-family:宋体"}

[[Number of neighbors under helper]{lang="EN-US"}]{#struct_0_x9962_12256_1301060970}

[[处于]{style="font-family:宋体"}[helper]{lang="EN-US"}]{#struct_0_x9962_12256_317334511}[状态邻居的数量]{style="font-family:宋体"}

[[Number of restarting neighbors]{lang="EN-US"}]{#struct_0_x9962_12256_x2000188938}

[[处于]{style="font-family:宋体"}[restarter]{lang="EN-US"}]{#struct_0_x9962_12256_x1200596618}[状态邻居的数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_191179886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_673360290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fspf graceful-restart helper]{lang="EN-US"}**]{#struct_0_x9962_12256_x1818370139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fspf graceful-restart interval]{lang="EN-US"}**]{#struct_0_x9962_12256_770807042}

::: {#987310257 .myid}
[]{#_Toc404798143}[]{#struct_0_x9962_12256_x564983199}[]{#_Toc316392299}

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf lsdb**

------------------------------------------------------------------------

[**[display fspf lsdb]{lang="EN-US"}**]{#struct_0_x9962_12256_559185792}[命令用来显示]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[链路状态数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200662154}

[**[display fspf lsdb]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1407699458}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1236910826}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1120049136}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_82201940}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_734351999}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1199029463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1200465546}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1595493580}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1940950973}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x19578190}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[链路状态数据库信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[链路状态数据库信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2100146605}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1595761849}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_x748289986}[链路状态数据库信息，包括]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的总数和各]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的具体信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1966331370}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1023058945}[显示]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[链路状态数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> display fspf lsdb]{lang="EN-US"}]{#struct_0_x9962_12256_x1200531082}

[FSPF LSDB information of VSAN 1(01):]{lang="EN-US"}

[  Total LSR count: 2]{lang="EN-US"}

[    FSPF Link State Database for Domain 01]{lang="EN-US"}

[      LSR Type                  : 1]{lang="EN-US"}

[      LSR Age                   : 0]{lang="EN-US"}

[      LSR Incarnation number    : 0x80000008]{lang="EN-US"}

[      LSR Checksum              : 0x7deb]{lang="EN-US"}

[      Number of links           : 1]{lang="EN-US"}

[      NbrDomainID    IfIndex    NbrIfIndex    LinkType    Cost]{lang="EN-US"}

[      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      2              0x68       0x68          1           265]{lang="EN-US"}

[    FSPF Link State Database for Domain 02]{lang="EN-US"}

[      LSR Type                  : 1]{lang="EN-US"}

[      LSR Age                   : 6]{lang="EN-US"}

[      LSR Incarnation number    : 0x80000008]{lang="EN-US"}

[      LSR Checksum              : 0x7dea]{lang="EN-US"}

[      Number of links           : 1]{lang="EN-US"}

[      NbrDomainID    IfIndex    NbrIfIndex    LinkType    Cost]{lang="EN-US"}

[      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      1              0x68       0x68          1           265]{lang="EN-US"}

[[表1-35 ]{lang="EN-US"}[display fspf lsdb]{lang="EN-US"}]{#struct_0_x9962_12256_7406048}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1082745341}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200989837}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1049213944}

[[FSPF LSDB information of VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1829818241}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1696868428}[的链路状态数据库信息，括号中为本机域]{style="font-family:宋体"}[ID]{lang="EN-US"}[的十进制显示]{style="font-family:宋体"}

[[Total LSR count]{lang="EN-US"}]{#struct_0_x9962_12256_x761177643}

[[LSR]{lang="EN-US"}]{#struct_0_x9962_12256_x1201055373}[数量]{style="font-family:宋体"}

[[FSPF Link State Database for Domain]{lang="EN-US"}]{#struct_0_x9962_12256_x2130831003}

[[指定域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_x385394872}[交换机的链路状态数据库信息]{style="font-family:宋体"}

[[LSR Type]{lang="EN-US"}]{#struct_0_x9962_12256_x544598276}

[[LSR]{lang="EN-US"}]{#struct_0_x9962_12256_x1117604341}[类型，只支持]{style="font-family:宋体"}[Switch Link Record]{lang="EN-US"}[（]{style="font-family:宋体"}[0x01]{lang="EN-US"}[）类型]{style="font-family:宋体"}

[[LSR Age]{lang="EN-US"}]{#struct_0_x9962_12256_x1200858765}

[[LSR]{lang="EN-US"}]{#struct_0_x9962_12256_x672178848}[生存时间]{style="font-family:宋体"}

[[LSR Incarnation number]{lang="EN-US"}]{#struct_0_x9962_12256_x2124063457}

[[LSR]{lang="EN-US"}]{#struct_0_x9962_12256_1252452197}[实例号]{style="font-family:宋体"}

[[LSR Checksum]{lang="EN-US"}]{#struct_0_x9962_12256_1483750238}

[[LSR]{lang="EN-US"}]{#struct_0_x9962_12256_x1200924301}[校验和]{style="font-family:宋体"}

[[Number of links]{lang="EN-US"}]{#struct_0_x9962_12256_687884225}

[[链路数量]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1711603267}

[[NbrDomainID]{lang="EN-US"}]{#struct_0_x9962_12256_x949592528}

[[邻居域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_x1200727693}

[[IfIndex]{lang="EN-US"}]{#struct_0_x9962_12256_1998008564}

[[本交换机出接口索引]{style="font-family:宋体"}]{#struct_0_x9962_12256_1922872283}

[[NbrIfIndex]{lang="EN-US"}]{#struct_0_x9962_12256_1270422550}

[[邻居接口索引]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1200793229}

[[Link Type]{lang="EN-US"}]{#struct_0_x9962_12256_x2040094451}

[[链路类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x342392615}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x01]{lang="EN-US"}]{#struct_0_x9962_12256_1533093816}[：表示]{style="font-family:宋体"}[点到点类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xF0-FF]{lang="EN-US"}]{#struct_0_x9962_12256_x1200596621}[：表示厂商自定义类型]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x9962_12256_x1730937807}

[[链路开销]{style="font-family:宋体"}]{#struct_0_x9962_12256_823370574}

[ ]{lang="EN-US"}

::: {#283538323 .myid}
[]{#_Toc404798144}[]{#struct_0_x9962_12256_x1333729386}[]{#_Toc316392300}[]{#_Toc310002147}

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf neighbor**

------------------------------------------------------------------------

[**[display fspf neighbor]{lang="EN-US"}**]{#struct_0_x9962_12256_1397862066}[命令用来显示]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x905744779}

[**[display fspf neighbor]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1200662157}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x158384483}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1722146876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_931817556}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1317830431}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x961843165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1223524247}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1672700109}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200465549}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1489620135}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[邻居信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1565423405}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1939756096}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_x202067688}[邻居信息，包括邻居的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[、邻居接口索引及本机出接口索引、邻居剩余]{style="font-family:宋体"}[Dead]{lang="EN-US"}[时间、邻居状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1209840057}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2126183843}[显示]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display fspf neighbor]{lang="EN-US"}]{#struct_0_x9962_12256_47280821}

[FSPF neighbor information of VSAN 1(01):]{lang="EN-US"}

[  Interface   NbrDomain   IfIndex   NbrIfIndex   Dead Time   State ]{lang="EN-US"}

[  Fc1/0/1     2           0x68      0x68         00:01:06    Full]{lang="EN-US"}

[[表1-36 ]{lang="EN-US"}[display fspf neighbor]{lang="EN-US"}]{#struct_0_x9962_12256_x1200531085}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1081309977}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1929720349}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x308071549}

[[FSPF neighbor information of VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_508716309}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_851112381}[的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[邻居信息，括号中为本机域]{style="font-family:宋体"}[ID]{lang="EN-US"}[的十进制显示]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x77610756}

[[本机接口名称]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1200989836}

[[NbrDomain]{lang="EN-US"}]{#struct_0_x9962_12256_x516869997}

[[邻居域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9962_12256_x483851418}[，十进制显示]{style="font-family:宋体"}

[[IfIndex]{lang="EN-US"}]{#struct_0_x9962_12256_1979759112}

[[本机出接口索引]{style="font-family:宋体"}]{#struct_0_x9962_12256_1249450804}

[[NbrIfIndex]{lang="EN-US"}]{#struct_0_x9962_12256_x1201055372}

[[邻居接口索引]{style="font-family:宋体"}]{#struct_0_x9962_12256_x564747062}

[[Dead Time]{lang="EN-US"}]{#struct_0_x9962_12256_578703781}

[[邻居所剩]{style="font-family:宋体"}[Dead]{lang="EN-US"}]{#struct_0_x9962_12256_x220412865}[间隔（如果这个间隔后还未收到邻居的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，邻居状态变迁至]{style="font-family:宋体"}[Init]{lang="EN-US"}[）]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x9962_12256_x1338774892}

[[邻居状态，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1200858764}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x9962_12256_893905093}[：表示邻居还未开始协商]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x9962_12256_2130325155}[：表示开始协商]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DB_Exchange]{lang="EN-US"}]{#struct_0_x9962_12256_1849671915}[：表示已经发现邻居]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DB_Wait]{lang="EN-US"}]{#struct_0_x9962_12256_x1200924300}[：表示本端已发送完]{lang="EN-US" style="font-family:宋体"}[LSR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DB_Ack_Wait]{lang="EN-US"}]{#struct_0_x9962_12256_x878199716}[：表示对端已发送完]{lang="EN-US" style="font-family:宋体"}[LSR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Full]{lang="EN-US"}]{#struct_0_x9962_12256_x61544310}[：表示同步完成]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#328966122 .myid}
[]{#_Toc404798145}[]{#struct_0_x9962_12256_x280005429}[]{#_Toc316392301}[]{#_Toc310002149}

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf statistics**

------------------------------------------------------------------------

[**[display fspf statistics]{lang="EN-US"}**]{#struct_0_x9962_12256_1860274959}[命令用来显示]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2062014851}

[**[display fspf statistics]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1200727692}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_431924623}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x152905315}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2081313816}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1955131103}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1307330189}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1405695152}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1849732574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1601919558}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1200793228}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x474010510}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x29612372}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_x1032060518}[所有统计信息，包括全局统计信息和接口统计信息。全局统计信息包括当前路由计算次数、错误报文计数、及报文收发总数；接口统计信息包括各接口下报文收发数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_42226362}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1747043760}[显示]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fspf statistics]{lang="EN-US"}]{#struct_0_x9962_12256_x1200596620}

[FSPF statistics of VSAN 1(01):]{lang="EN-US"}

[  SPF computing count: 6]{lang="EN-US"}

[  Statistics counters:]{lang="EN-US"}

[    Bad packet       : 0      Neighbor unknown   : 0]{lang="EN-US"}

[    Timer mismatch   : 0      Neighbor state low : 0]{lang="EN-US"}

[    Bad LSR          : 0]{lang="EN-US"}

[  Packet statistics:]{lang="EN-US"}

[    Type          Input        Output]{lang="EN-US"}

[    HELLO         50           50]{lang="EN-US"}

[    LSU           5            5]{lang="EN-US"}

[    LSA           4            4]{lang="EN-US"}

[  Interface Fc1/0/1 statistics:]{lang="EN-US"}

[    Type          Input        Output]{lang="EN-US"}

[    HELLO         50           50]{lang="EN-US"}

[    LSU           5            5]{lang="EN-US"}

[    LSA           4            4]{lang="EN-US"}

[[表1-37 ]{lang="EN-US"}[display fspf statistics]{lang="EN-US"}]{#struct_0_x9962_12256_x164853866}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1073788901}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1280540567}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x863799607}

[[FSPF statistics of VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1200662156}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1724468424}[的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息，括号中为本机域]{style="font-family:宋体"}[ID]{lang="EN-US"}[的十进制显示]{style="font-family:宋体"}

[[SPF computing count]{lang="EN-US"}]{#struct_0_x9962_12256_287281090}

[[路由计算次数]{style="font-family:宋体"}]{#struct_0_x9962_12256_1489381246}

[[Statistics counters]{lang="EN-US"}]{#struct_0_x9962_12256_x1593971668}

[[统计计数]{style="font-family:宋体"}]{#struct_0_x9962_12256_1656051706}

[[Packet statistics]{lang="EN-US"}]{#struct_0_x9962_12256_x1200465548}

[[报文统计]{style="font-family:宋体"}]{#struct_0_x9962_12256_x76463806}

[[Interface statistics]{lang="EN-US"}]{#struct_0_x9962_12256_x1860731729}

[[端口下报文统计]{style="font-family:宋体"}]{#struct_0_x9962_12256_x185448255}

[[Bad packet]{lang="EN-US"}]{#struct_0_x9962_12256_x1200531084}

[[错误报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_x799163006}

[[Timer mismatch]{lang="EN-US"}]{#struct_0_x9962_12256_948815824}

[[和邻居]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x9962_12256_x1901137785}[或]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔值不匹配的报文]{style="font-family:宋体"}

[[Bad LSR]{lang="EN-US"}]{#struct_0_x9962_12256_197739630}

[[错误]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x9962_12256_x1200989839}

[[Neighbor unknown]{lang="EN-US"}]{#struct_0_x9962_12256_x113585470}

[[未知邻居发来的报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_1944596562}

[[Neighbor state low]{lang="EN-US"}]{#struct_0_x9962_12256_x654473333}

[[Init]{lang="EN-US"}]{#struct_0_x9962_12256_x1623026502}[状态收到]{style="font-family:宋体"}[LSU]{lang="EN-US"}[、]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文的统计]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x9962_12256_x1201055375}

[[报文类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1324261949}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x9962_12256_x1837252760}[：]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSU]{lang="EN-US"}]{#struct_0_x9962_12256_x2075620572}[：]{lang="EN-US" style="font-family:宋体"}[LSU]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSA]{lang="EN-US"}]{#struct_0_x9962_12256_x1200858767}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Input]{lang="EN-US"}]{#struct_0_x9962_12256_490620566}

[[接收的报文数目]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1841736138}

[[Output]{lang="EN-US"}]{#struct_0_x9962_12256_x1200924303}

[[发送的报文数目]{style="font-family:宋体"}]{#struct_0_x9962_12256_1850683639}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x37697797}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset fspf counters]{lang="EN-US"}**]{#struct_0_x9962_12256_1930185190}

::: {#1194898093 .myid}
[]{#_Toc404798146}[]{#struct_0_x9962_12256_x1936667154}[]{#_Toc297214174}

**FC和FCoE \-- FC路由与转发配置命令 \-- fc route-static**

------------------------------------------------------------------------

[**[fc route-static]{lang="EN-US"}**]{#struct_0_x9962_12256_x1100450535}[命令用来配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[静态路由。]{style="font-family:宋体"}

[**[undo fc route-static]{lang="EN-US"}**]{#struct_0_x9962_12256_x1200727695}[命令用来删除]{style="font-family:宋体"}[FC]{lang="EN-US"}[静态路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1134159318}

[**[fc route-static]{lang="EN-US"}***[ fcid ]{lang="EN-US"}*[{ *mask* \| *mask-length* } *interface-type interface-number* \[ **cost** *cost-value* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x976928504}

[**[undo fc route-static]{lang="EN-US"}***[ fcid ]{lang="EN-US"}*[{ *mask* \| *mask-length* } *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_x543269364}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x176739816}

[[不存在]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_183691568}[静态路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2127180555}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x713782955}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200793231}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1898576949}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1645494588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_158888173}

[*[fcid]{lang="DE"}*]{#struct_0_x9962_12256_x1774916857}[：指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[静态路由的目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址，取值范围为]{style="font-family:宋体"}[0x010000]{lang="EN-US"}[～]{style="font-family:宋体"}[0xEFFFFF]{lang="EN-US"}[（十六进制）。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x9962_12256_2133455389}[：]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的十六进制掩码，与]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[配合使用。取值为]{style="font-family:宋体"}[0xFF0000]{lang="EN-US"}[、]{style="font-family:宋体"}[0xFFFF00]{lang="EN-US"}[、]{style="font-family:宋体"}[0xFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x9962_12256_2118107663}[：]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址的十进制掩码，与]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[配合使用。取值为]{style="font-family:宋体"}[8]{lang="EN-US"}[、]{style="font-family:宋体"}[16]{lang="EN-US"}[、]{style="font-family:宋体"}[24]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x9962_12256_x1200596623}[：指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[静态路由的出接口，出接口必须为]{style="font-family:宋体"}[FC]{lang="EN-US"}[交换机上存在的]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口或者]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}***[ cost-value]{lang="EN-US"}*]{#struct_0_x9962_12256_x568138393}[：指定路由的度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1111587807}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1939821632}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[静态路由是由管理员手工配置的。配置静态路由后，去往指定目的地的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1779795683}[报文将按照管理员指定的路径进行转发。]{style="font-family:宋体"}

[[在组网结构比较简单的网络中，只需配置静态路由就可以实现网络互通。但是静态路由不能自动适应网络拓扑结构的变化，当网络发生故障或者拓扑发生变化后，需要管理员手工修改静态路由的配置。]{style="font-family:宋体"}]{#struct_0_x9962_12256_1172800776}

[[静态路由支持等价路由，如果先后配置多条目的地址相同、出接口不同的静态路由且度量值相同，则生成等价路由。]{style="font-family:宋体"}]{#struct_0_x9962_12256_1925985284}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1580651760}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1141369796}[添加一条目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0x010000]{lang="EN-US"}[、掩码为]{style="font-family:宋体"}[8]{lang="EN-US"}[、出接口为]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[、路由度量值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[静态路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1200662159}

[\[Sysname\] vsan 5]{lang="EN-US"}

[\[Sysname-vsan5\] fc route-static 010000 8 fc 1/0/1 cost 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1360645291}[添加一条目的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0x010000]{lang="EN-US"}[、掩码为]{style="font-family:宋体"}[8]{lang="EN-US"}[、出接口为]{style="font-family:宋体"}[VFC4]{lang="EN-US"}[、路由度量值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[静态路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1359045992}

[\[Sysname\] vsan 5]{lang="EN-US"}

[\[Sysname-vsan5\] fc route-static 010000 8 vfc 4 cost 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x671419337}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fc routing-table]{lang="EN-US"}**]{#struct_0_x9962_12256_x481498866}
:::

::: {#-1677525221 .myid}
[]{#_Toc404798147}[]{#struct_0_x9962_12256_602775576}[]{#_Toc316392302}[]{#_Toc310002152}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf cost**

------------------------------------------------------------------------

[**[fspf cost]{lang="EN-US"}**]{#struct_0_x9962_12256_x1200465551}[命令用来配置指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[开销。]{style="font-family:宋体"}

[**[undo fspf cost]{lang="EN-US"}**]{#struct_0_x9962_12256_1133455311}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2117586319}

[**[fspf cost]{lang="EN-US"}**[ *value* **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_561177084}

[**[undo fspf cost vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x403049269}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1363277329}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x721661341}[接口的缺省]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[开销根据接口波特率计算得到，计算公式为（]{style="font-family:宋体"}[1.0\*1.062e12/]{lang="EN-US"}[波特率）。]{style="font-family:宋体"}

[[VFC]{lang="EN-US"}]{#struct_0_x9962_12256_71595576}[接口、]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的缺省]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[开销为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200531087}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_766920935}[接口视图]{style="font-family:宋体"}[/VFC]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_777980363}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x492596958}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_953356097}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1469526684}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_x685961517}[：接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[开销，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x226903576}[：所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200989838}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1133252578}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[网络中，每一条链路会有不同的开销，在路由优选算法中将使用开销值来确定最有效的路由，接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_x1679669411}[开销越小说明链路的开销越小。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1930600014}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_x280363721}[配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[FSPF]{lang="DE"}[开销为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x280756938}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\]]{lang="EN-US"}[ ]{lang="EN-US"}[fspf cost 1000 vsan ]{lang="EN-US"}[4]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_762123480}[配置接口]{style="font-family:宋体"}[VFC1]{lang="DE"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[FSPF]{lang="DE"}[开销为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x28620885}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] ]{lang="DE"}[fspf cost 1000 vsan ]{lang="EN-US"}[4]{lang="DE"}
:::

::: {#-1360873717 .myid}
[]{#_Toc404798148}[]{#struct_0_x9962_12256_780640107}[]{#_Toc316392303}[]{#_Toc310002154}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf dead-interval**

------------------------------------------------------------------------

[**[fspf dead-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_x809599468}[命令用来配置指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内接口的]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔值。]{style="font-family:宋体"}

[**[undo fspf dead-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_x1201055374}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_241821992}

[**[fspf dead-interval]{lang="EN-US"}**[ *value* **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x926144355}

[**[undo fspf ]{lang="SV"}[dead]{lang="EN-US"}**]{#struct_0_x9962_12256_649866854}**[-interval]{lang="SV"}**[ **vsan** *vsan-id*]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1352635686}

[[接口的]{style="font-family:宋体"}[Dead]{lang="EN-US"}]{#struct_0_x9962_12256_x1043538480}[间隔值为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x134693637}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x405121171}[接口视图]{style="font-family:宋体"}[/VFC]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200858766}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2056704507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1774994949}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1340602801}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_x1835718253}[：接口的]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔值，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x2026796614}[：所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x551863554}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1595630777}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[两台交换机之间建立起邻居关系后，需要以]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x9962_12256_2090243384}[间隔值为周期向对方发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文来维护邻居关系。若在]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔内仍未收到对方的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，则认为邻居不存在，需要删除该邻居。]{style="font-family:宋体"}

[[需要注意的是，配置的]{style="font-family:宋体"}[Dead]{lang="EN-US"}]{#struct_0_x9962_12256_1368452641}[间隔值必须大于]{style="font-family:宋体"}[Hello]{lang="EN-US"}[间隔值，且邻居双方配置的]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔值必须一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1200924302}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_1651977592}[配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="DE"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔值为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_1652174200}

[\[Sysname\] interface fc 1/0/1]{lang="DE"}

[\[Sysname-Fc1/0/1\] ]{lang="DE"}[fspf dead-interval 100 vsan ]{lang="EN-US"}[4]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_284599698}[配置接口]{style="font-family:宋体"}[VFC1]{lang="DE"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔值为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_1961065058}

[\[Sysname\] interface vfc 1]{lang="DE"}

[\[Sysname-Vfc1\] ]{lang="DE"}[fspf dead-interval 100 vsan ]{lang="EN-US"}[4]{lang="DE"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_432970454}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fspf hello-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_x131969830}
:::

::: {#-835550704 .myid}
[]{#_Toc404798149}[]{#struct_0_x9962_12256_1439044404}[]{#_Toc316392304}[]{#_Toc310002150}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf enable**

------------------------------------------------------------------------

[**[fspf enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x705215825}[命令用来开启指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo fspf enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1200727694}[命令用来关闭指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1594724037}

[**[fspf enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1388456628}

[**[undo fspf enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1219731418}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1187923843}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2103639628}[创建后，]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_34495098}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1200793230}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x830306406}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x955713284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1707961117}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_386603847}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1180306745}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[开启了指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_315795051}[的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能后，该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[才可以运行]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[相关的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1545856151}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x717861190}[开启]{style="font-family:宋体"}[VSAN 4]{lang="EN-US"}[的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1200596622}

[\[Sysname\] vsan 4]{lang="EN-US"}

[\[Sysname-vsan4\] fspf enable]{lang="EN-US"}
:::

::: {#2081027069 .myid}
[]{#_Toc310002153}[]{#_Toc404798150}[]{#struct_0_x9962_12256_997945548}[]{#_Toc316392305}[]{#_Toc316371529}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf graceful-restart**

------------------------------------------------------------------------

[**[fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_1207021556}[命令用来开启]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_529176712}[命令用来关闭]{style="font-family:
宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_41794797}

[**[fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_176819000}

[**[undo fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_x617000020}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1917637050}

[[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_x1200662158}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x205438650}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_2136905277}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_692764739}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x115171181}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1084972407}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2130873621}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1536602641}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[GR]{lang="EN-US"}]{#struct_0_x9962_12256_1837530159}[（]{style="font-family:宋体"}[Graceful Restart]{lang="EN-US"}[，平滑重启）是一种通过备份]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[配置信息，在协议重启或主备倒换时]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[进行平滑重启，从邻居那里获得邻居关系，并对]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[进行同步，从而保证转发业务不中断的机制。]{style="font-family:宋体"}

[[GR]{lang="EN-US"}]{#struct_0_x9962_12256_x1200465550}[有两个角色：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GR Restarter]{lang="EN-US"}]{#struct_0_x9962_12256_x432628630}[：发生协议重启或主备倒换事件且具有]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力的设备。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GR Helper]{lang="EN-US"}]{#struct_0_x9962_12256_428050346}[：和]{lang="EN-US" style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[具有邻居关系，协助完成]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[流程的设备。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1630671363}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x79290252}[开启]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x944423595}

[\[Sysname\] fspf graceful-restart]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_89693370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_x1200531086}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fspf graceful-restart helper]{lang="EN-US"}**]{#struct_0_x9962_12256_x1961962420}
:::

::: {#-882973613 .myid}
[]{#_Toc404798151}[]{#struct_0_x9962_12256_x459401600}[]{#_Toc316392306}[]{#_Toc316371530}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf graceful-restart helper**

------------------------------------------------------------------------

[**[fspf graceful-restart helper]{lang="EN-US"}**]{#struct_0_x9962_12256_x1017414162}[命令用来开启]{style="font-family:
宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo fspf graceful-restart helper]{lang="EN-US"}**]{#struct_0_x9962_12256_1793844284}[命令用来关闭]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1366436376}

[**[fspf graceful-restart helper]{lang="EN-US"}**]{#struct_0_x9962_12256_962006759}

[**[undo fspf graceful-restart helper]{lang="EN-US"}**]{#struct_0_x9962_12256_1893915861}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721324466}

[[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_68730319}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1725911094}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1368931230}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_698833344}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_207611059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x477747156}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721258930}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_373803227}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_1211439929}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力后，该交换机才可以协助]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[完成]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x544066336}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1705923786}[开启]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_506375727}

[\[Sysname\] fspf graceful-restart helper]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1189704619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_1632258430}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_x86066637}
:::

::: {#-1916802991 .myid}
[]{#_Toc404798152}[]{#struct_0_x9962_12256_242933033}[]{#_Toc316392307}[]{#_Toc316371531}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf graceful-restart interval**

------------------------------------------------------------------------

[**[fspf graceful-restart interval]{lang="EN-US"}**]{#struct_0_x9962_12256_721455538}[命令用来配置]{style="font-family:
宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[最大间隔时间。]{style="font-family:宋体"}

[**[undo fspf graceful-restart interval]{lang="EN-US"}**]{#struct_0_x9962_12256_x1600239403}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1922329629}

[**[fspf graceful-restart interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_x9962_12256_1906697467}

[**[undo fspf graceful-restart interval]{lang="EN-US"}**]{#struct_0_x9962_12256_924615027}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x76783166}

[[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_1129158240}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[最大间隔时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721390002}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1664412810}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1653654402}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2105598832}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x632308639}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_290096934}

[*[interval-value]{lang="EN-US"}*]{#struct_0_x9962_12256_485502863}[：指定]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[最大间隔时间，取值范围为]{style="font-family:宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x784026395}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x432765827}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}]{#struct_0_x9962_12256_721586610}[来说，如果在]{style="font-family:宋体"}[GR]{lang="EN-US"}[最大间隔时间内没有完成]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程，则立即退出]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_752014813}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1377353487}[配置]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[最大间隔时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1182029379}

[\[Sysname\] fspf graceful-restart interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_864989190}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fspf graceful-restart]{lang="EN-US"}**]{#struct_0_x9962_12256_x1746545919}
:::

::: {#917715275 .myid}
[]{#_Toc404798153}[]{#struct_0_x9962_12256_x170932456}[]{#_Toc316392308}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf hello-interval**

------------------------------------------------------------------------

[**[fspf hello-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_97971223}[命令用来配置指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内接口的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[间隔值。]{style="font-family:宋体"}

[**[undo fspf hello-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_721521074}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_742714209}

[**[fspf hello-interval]{lang="EN-US"}**[ *value* **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1642398586}

[**[undo fspf hello-interval]{lang="SV"}**[ ]{lang="SV"}]{#struct_0_x9962_12256_642050248}**[vsan]{lang="SV"}**[ *vsan-id*]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x718274876}

[[接口的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x9962_12256_1064543329}[间隔值为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_687976696}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_966709787}[接口视图]{style="font-family:宋体"}[/VFC]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721717682}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_594990264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x180991855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1319912985}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_1016303120}[：接口的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[间隔值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_8824697}[：所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_301051983}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1595565241}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[交换机通过周期性向外发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x9962_12256_1150496072}[报文，来发现和维护邻居关系。]{style="font-family:宋体"}[Hello]{lang="EN-US"}[间隔值决定了接口在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[需要注意的是，配置的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x9962_12256_721652146}[间隔值必须小于]{style="font-family:宋体"}[Dead]{lang="EN-US"}[间隔值，且邻居双方配置的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[间隔值必须一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x543918489}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_86024718}[配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="DE"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[Hello]{lang="DE"}[间隔值为]{style="font-family:宋体"}[10]{lang="DE"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_85631502}

[\[Sysname\] interface fc 1/0/1]{lang="DE"}

[\[Sysname-Fc1/0/1\] fspf hello-interval 10 vsan 4]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_561428114}[配置接口]{style="font-family:宋体"}[VFC1]{lang="DE"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[Hello]{lang="DE"}[间隔值为]{style="font-family:宋体"}[10]{lang="DE"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_455180227}

[\[Sysname\] interface vfc 1]{lang="DE"}

[\[Sysname-Vfc1\] fspf hello-interval 10 vsan 4]{lang="DE"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x300997268}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}**[fspf dead-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_x1705685102}
:::

::: {#1517817754 .myid}
[]{#_Toc404798154}[]{#struct_0_x9962_12256_209157264}[]{#_Toc316392309}[]{#_Toc310002157}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf min-ls-arrival**

------------------------------------------------------------------------

[**[fspf min-ls-arrival]{lang="EN-US"}**]{#struct_0_x9962_12256_721848754}[命令用来配置指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[LSR]{lang="DE"}[最小接收间隔。]{style="font-family:宋体"}

[**[undo fspf min-ls-arrival]{lang="EN-US"}**]{#struct_0_x9962_12256_2004639570}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1877225761}

[**[fspf min-ls-arrival]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_x1898999012}

[**[undo fspf min-ls-arrival]{lang="EN-US"}**]{#struct_0_x9962_12256_1697961452}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_991159021}

[[LSR]{lang="DE"}]{#struct_0_x9962_12256_x2066144597}[最小接收间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1649381680}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_721783218}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1294990487}

[[network-admin]{lang="DE"}]{#struct_0_x9962_12256_50575549}

[[mdc-admin]{lang="DE"}]{#struct_0_x9962_12256_x1756347799}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1510036087}

[*[value]{lang="DE"}*]{#struct_0_x9962_12256_1423568466}[：]{style="font-family:宋体"}[LSR]{lang="DE"}[最小接收间隔]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:
宋体"}[0]{lang="DE"}[～]{style="font-family:宋体"}[60]{lang="DE"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1064163343}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1192215178}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[LSR]{lang="DE"}]{#struct_0_x9962_12256_683258242}[最小接收间隔决定了指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内接收]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的间隔。为了避免过于频繁的从邻居接收到同一个]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的新实例、更新本地]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[而频繁触发路由计算。在]{style="font-family:宋体"}[LSR]{lang="EN-US"}[最小接收间隔时间内，如果又一次接收到了这个]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的新实例，则直接丢弃，不做处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721324467}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_68730318}[配置]{style="font-family:宋体"}[VSAN 2]{lang="DE"}[内]{style="font-family:宋体"}[LSR]{lang="DE"}[最小接收间隔为]{style="font-family:
宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_612741066}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] fspf min-ls-arrival 10]{lang="EN-US"}
:::

::: {#-911667125 .myid}
[]{#_Toc404798155}[]{#struct_0_x9962_12256_x602532387}[]{#_Toc316392310}[]{#_Toc310002158}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf min-ls-interval**

------------------------------------------------------------------------

[**[fspf min-ls-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_855050260}[命令用来配置指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[LSR]{lang="DE"}[最小刷新间隔。]{style="font-family:宋体"}

[**[undo fspf min-ls-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_1680626974}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x738238368}

[**[fspf min-ls-interval]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_721258931}

[**[undo fspf min-ls-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_1211439930}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x543607585}

[[LSR]{lang="DE"}]{#struct_0_x9962_12256_1407699600}[最小刷新间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1619772133}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x734715459}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_373005233}

[[network-admin]{lang="DE"}]{#struct_0_x9962_12256_x1351617075}

[[mdc-admin]{lang="DE"}]{#struct_0_x9962_12256_721455539}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1600239402}

[*[value]{lang="DE"}*]{#struct_0_x9962_12256_x356245688}[：]{style="font-family:宋体"}[最小]{style="font-family:宋体"}[LSR]{lang="DE"}[刷新间隔值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="DE"}[～]{style="font-family:宋体"}[60]{lang="DE"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1040296664}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1939952704}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[LSR]{lang="DE"}]{#struct_0_x9962_12256_x1470134152}[最小刷新间隔决定了指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[LSR]{lang="EN-US"}[刷新间隔。为了避免本机]{style="font-family:宋体"}[LSR]{lang="EN-US"}[被频繁的刷新，从而降低路由计算的频率和减少]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[中]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的泛洪，在]{style="font-family:宋体"}[LSR]{lang="EN-US"}[最小刷新间隔内，交换机不能再次刷新本机]{style="font-family:宋体"}[LSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2125412272}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_1820922136}[配置]{style="font-family:宋体"}[VSAN 2]{lang="DE"}[内最小]{style="font-family:宋体"}[LSR]{lang="EN-US"}[刷新间隔值为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_721390003}

[\[Sysname\] vsan 2]{lang="DE"}

[\[Sysname-vsan2\] fspf min-ls-interval 10]{lang="DE"}
:::

::: {#-1498523541 .myid}
[]{#_Toc404798156}[]{#struct_0_x9962_12256_1664412811}[]{#_Toc316392311}[]{#_Toc310002155}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf retransmit-interval**

------------------------------------------------------------------------

[**[fspf retransmit-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_x1653588866}[命令用来配置指定]{style="font-family:
宋体"}[VSAN]{lang="EN-US"}[内接口的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[重传间隔。]{style="font-family:宋体"}

[**[undo fspf retransmit-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_1786058217}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2108108134}

[**[fspf retransmit-interval]{lang="EN-US"}**[ *value* **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1489447611}

[**[undo fspf ]{lang="SV"}[retransmit]{lang="EN-US"}**]{#struct_0_x9962_12256_x40687657}**[-interval vsan]{lang="SV"}**[ *vsan-id*]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x53093607}

[[接口的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x9962_12256_721586611}[重传间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_752014812}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1377353488}[接口视图]{style="font-family:宋体"}[/VFC]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1182619203}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1082050070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_765521048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1848904528}

[*[value]{lang="EN-US"}*]{#struct_0_x9962_12256_35680321}[：接口的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[重传间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_721521075}[：所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_742714208}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1133383650}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[LSDB]{lang="EN-US"}]{#struct_0_x9962_12256_1642398585}[的同步需要交互]{style="font-family:宋体"}[LSR]{lang="EN-US"}[。在发送]{style="font-family:宋体"}[LSR]{lang="EN-US"}[后，等待邻居回应报文确认，如果过了]{style="font-family:宋体"}[LSR]{lang="EN-US"}[重传间隔还没有接收到邻居的确认，那么需要再次发送该]{style="font-family:宋体"}[LSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_642246856}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_488916033}[配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="DE"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[重传间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_489505856}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] fspf retransmit-interval 10 vsan 4]{lang="EN-US"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_1085913781}[配置接口]{style="font-family:宋体"}[VFC1]{lang="DE"}[在]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[重传间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x594148936}

[\[Sysname\] interface vfc 1]{lang="EN-US"}

[\[Sysname-Vfc1\] fspf retransmit-interval 10 vsan 4]{lang="EN-US"}
:::

::: {#1998020377 .myid}
[]{#_Toc404798157}[]{#struct_0_x9962_12256_x480083766}[]{#_Toc316392312}[]{#_Toc310002151}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf silent**

------------------------------------------------------------------------

[**[fspf silent]{lang="EN-US"}**]{#struct_0_x9962_12256_721717683}[命令用来关闭指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo fspf silent]{lang="EN-US"}**]{#struct_0_x9962_12256_594990265}[命令用来开启指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x180991854}

[**[fspf silent vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1319847449}

[**[undo fspf silent vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1184845876}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x314920872}

[[所有接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_x592260355}[功能均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1524049279}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1923501401}[接口视图]{style="font-family:宋体"}[/VFC]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/FC]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721652147}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x543918488}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_561493650}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_840358991}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x582461792}[：所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2110342771}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x29415764}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[开启接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x9962_12256_1768241870}[功能后，接口才可以参与]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[路由运算，如果某接口不参与]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[路由运算，则需关闭该接口的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x674379605}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_489178174}[关闭]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内接口]{style="font-family:宋体"}[FC1/0/1]{lang="DE"}[的]{style="font-family:宋体"}[FSPF]{lang="DE"}[功能。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_489309246}

[\[Sysname\] interface fc 1/0/1]{lang="DE"}

[\[Sysname-Fc1/0/1\] fspf silent vsan 4]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_721848755}[关闭]{style="font-family:宋体"}[VSAN 4]{lang="DE"}[内接口]{style="font-family:宋体"}[VFC1]{lang="DE"}[的]{style="font-family:宋体"}[FSPF]{lang="DE"}[功能。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_2004639569}

[\[Sysname\] interface vfc 1]{lang="DE"}

[\[Sysname-Vfc1\] fspf silent vsan 4]{lang="DE"}
:::

::: {#-1831965871 .myid}
[]{#_Toc404798158}[]{#struct_0_x9962_12256_1876767008}[]{#_Toc316392313}[]{#_Toc310002156}

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf spf-hold-time**

------------------------------------------------------------------------

[**[fspf spf-hold-time]{lang="EN-US"}**]{#struct_0_x9962_12256_1958443949}[命令用来配置指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内最短]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算间隔。]{style="font-family:宋体"}

[**[undo fspf spf-hold-time]{lang="EN-US"}**]{#struct_0_x9962_12256_1850263224}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_699123584}

[**[fspf spf-hold-time]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9962_12256_x1839884101}

[**[undo fspf spf-hold-time]{lang="EN-US"}**]{#struct_0_x9962_12256_721783219}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1294990488}

[[最短]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x9962_12256_x1515508392}[计算间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1757291708}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1164430290}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1451011249}

[[network-admin]{lang="DE"}]{#struct_0_x9962_12256_1248085341}

[[mdc-admin]{lang="DE"}]{#struct_0_x9962_12256_x1804147191}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721324464}

[*[value]{lang="DE"}*]{#struct_0_x9962_12256_68730317}[：最短]{style="font-family:宋体"}[SPF]{lang="DE"}[计算间隔]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="DE"}[～]{style="font-family:宋体"}[60]{lang="DE"}[，]{style="font-family:
宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_185774026}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1548445538}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x9962_12256_1888822454}[发生改变时，需要进行]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算。]{style="font-family:宋体"}[SPF]{lang="DE"}[计算需要耗费一定的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，如果网络频繁变化，且每次变化都立即进行]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算，将会占用大量的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。为了避免交换机过于频繁的进行路由计算而浪费]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，用户可以配置最短的]{style="font-family:宋体"}[SPF]{lang="DE"}[计算间隔。]{style="font-family:宋体"}

[[最短]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x9962_12256_1974111543}[计算间隔决定了指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内两次连续的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算之间的最小时间间隔。最短]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算间隔配置的小，意味着]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[对于]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[的变化可以快速反应，重新计算]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的路由。一个更小的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算间隔会耗费更多的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1109311569}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_1048811686}[配置]{style="font-family:宋体"}[VSAN 2]{lang="DE"}[内最短]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_721258928}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] fspf spf-hold-time 10]{lang="EN-US"}
:::

::: {#-1350726027 .myid}
[]{#_Toc404798159}[]{#struct_0_x9962_12256_x1127212223}[]{#_Toc316392314}[]{#_Toc310002159}

**FC和FCoE \-- FC路由与转发配置命令 \-- reset fspf counters**

------------------------------------------------------------------------

[**[reset fspf counters]{lang="EN-US"}**]{#struct_0_x9962_12256_1108490931}[命令用来清除]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_195502951}

[**[reset fspf counters]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x2140056243}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_853498264}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_2041190660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x727763218}

[[network-admin]{lang="DE"}]{#struct_0_x9962_12256_721455536}

[[mdc-admin]{lang="DE"}]{#struct_0_x9962_12256_x1600239405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1209838253}

[**[vsan]{lang="DE"}**]{#struct_0_x9962_12256_x2056665155}[ *vsan-id*]{lang="DE"}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VSAN]{lang="DE"}[内的]{style="font-family:宋体"}[FSPF]{lang="DE"}[统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[vsan-id]{lang="DE"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="DE"}[～]{style="font-family:宋体"}[3839]{lang="DE"}[。不指定该参数时，将清除所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1192149642}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_428989756}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1213109652}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_x969292872}[清除]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="DE"}[reset fspf counters vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_x504690223}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x908987999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fspf statistics]{lang="EN-US"}**]{#struct_0_x9962_12256_721390000}
:::

::: {#2125205297 .myid}
[]{#_Toc404798161}[]{#struct_0_x9962_12256_x1653130115}[]{#_Toc308689020}

**FC和FCoE \-- FC Zone配置命令 \-- delete zone database all**

------------------------------------------------------------------------

[**[delete zone database all]{lang="EN-US"}**]{#struct_0_x9962_12256_x1870973286}[命令用来清除]{style="font-family:
宋体"}[Zone]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_729197159}

[**[delete zone database all]{lang="EN-US"}**]{#struct_0_x9962_12256_x1883518098}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1148082493}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1863296361}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721586608}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1204300331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_456079535}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_805537337}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1536733713}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[通过本命令可以删除指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x53550805}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[数据库信息，包括所有]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[以及]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名，但是]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[不会被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1653573454}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1996080791}[清除]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_721521072}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] delete zone database all]{lang="EN-US"}
:::

::: {#-508329469 .myid}
[]{#_Toc404798162}[]{#struct_0_x9962_12256_742714207}[]{#_Toc308689021}

**FC和FCoE \-- FC Zone配置命令 \-- display zone**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **zone**]{lang="EN-US"}]{#struct_0_x9962_12256_1642398576}[命令]{style="font-family:宋体"}[用来显示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_642050257}

[**[display]{lang="EN-US"}**[ **zone** \[ \[ **name** *zone-name* \] **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1620377285}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x61489313}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x705465006}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721717680}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_594990262}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x180991853}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1320044057}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1886724217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1716537726}

[**[name ]{lang="EN-US"}***[zone-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x1461815010}[：显示指定名称的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}*[zone-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}***[ vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x638230830}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721652144}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_373934299}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[根据用户的配置可以显示不同]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x543918491}[的信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_560903825}**[name]{lang="EN-US"}**[和]{style="font-family:宋体"}**[vsan]{lang="EN-US"}**[参数，则显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内指定名称的单个]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_1953675194}**[vsan]{lang="EN-US"}**[参数，则显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1567302193}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1848695688}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_66184651}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display zone]{lang="EN-US"}]{#struct_0_x9962_12256_721848752}

[VSAN 1:]{lang="EN-US"}

[  zone name z1]{lang="EN-US"}

[    fcid 0x111111 initiator]{lang="EN-US"}

[    fcid 0x222222 target]{lang="EN-US"}

[    pwwn 11:11:11:11:22:22:22:22]{lang="EN-US"}

[    fwwn 02:0e:30:30:33:33:32:35]{lang="EN-US"}

[  zone name z2]{lang="EN-US"}

[    fcid 0x111111]{lang="EN-US"}

[    zone-alias name za1]{lang="EN-US"}

[    fcid 0x333333 initiator]{lang="EN-US"}

[VSAN 2:]{lang="EN-US"}

[VSAN 3:]{lang="EN-US"}

[[表1-38 ]{lang="EN-US"}[display zone]{lang="EN-US"}]{#struct_0_x9962_12256_2004639572}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1103773953}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1877094689}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1098840213}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_870724512}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_721783216}[编号]{style="font-family:宋体"}

[[zone name]{lang="EN-US"}]{#struct_0_x9962_12256_x1294990477}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_50378941}[的名称]{style="font-family:宋体"}

[[fcid]{lang="EN-US"}]{#struct_0_x9962_12256_1291334246}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1925829832}[成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[pwwn]{lang="EN-US"}]{#struct_0_x9962_12256_721324465}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_68730316}[成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[fwwn]{lang="EN-US"}]{#struct_0_x9962_12256_1319292610}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1024728112}[成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[initiator]{lang="EN-US"}]{#struct_0_x9962_12256_1319227074}[、]{style="font-family:宋体"}[target]{lang="EN-US"}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1020754435}[成员的角色，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[initiator]{lang="EN-US"}]{#struct_0_x9962_12256_366567702}[：表示成员角色为发起端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[target]{lang="EN-US"}]{#struct_0_x9962_12256_1433238474}[：表示成员角色为目的端]{lang="EN-US" style="font-family:宋体"}

[[如果没有标出]{style="font-family:宋体"}[initiator]{lang="EN-US"}]{#struct_0_x9962_12256_1319161538}[或]{style="font-family:宋体"}[target]{lang="EN-US"}[，则表示同时兼具这两种角色]{style="font-family:宋体"}

[[zone-alias name]{lang="EN-US"}]{#struct_0_x9962_12256_x1770541110}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_625418514}[别名的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2145370152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member (zone view)]{lang="EN-US"}**]{#struct_0_x9962_12256_1945188013}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone clone]{lang="EN-US"}**]{#struct_0_x9962_12256_868608144}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone name]{lang="EN-US"}**]{#struct_0_x9962_12256_721258929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone rename]{lang="EN-US"}**]{#struct_0_x9962_12256_x1127212222}

::: {#263937424 .myid}
[]{#_Toc404798163}[]{#struct_0_x9962_12256_x457593010}[]{#_Toc308689022}

**FC和FCoE \-- FC Zone配置命令 \-- display zone member**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **zone member**]{lang="EN-US"}]{#struct_0_x9962_12256_1879676058}[命令用来显示指定]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1780805730}

[**[display]{lang="EN-US"}**[ **zone member** { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* \| **zone-alias** *zone-alias-name* } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x973030029}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1255801245}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x975655054}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721455537}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1600239404}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1519045102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1579762722}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x209980695}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1097789904}

[**[fcid ]{lang="EN-US"}***[fcid]{lang="EN-US"}*]{#struct_0_x9962_12256_988626649}[：显示指定的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址成员所属的父亲信息。]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[表示]{style="font-family:宋体"}[成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[xxxxxx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[fwwn ]{lang="EN-US"}***[fwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_1319554754}[：显示指定的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}*[fwwn]{lang="EN-US"}*[表示成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[pwwn ]{lang="EN-US"}***[pwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_930250361}[：显示指定的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[表示]{style="font-family:宋体"}[成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[zone-alias ]{lang="EN-US"}***[zone-alias-name]{lang="EN-US"}*]{#struct_0_x9962_12256_721390001}[：显示指定的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名成员所属的父亲信息。]{style="font-family:宋体"}*[zone-alias-name]{lang="EN-US"}*[：表示成员的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[**[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_1664412809}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1653064579}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1548380002}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[根据用户的配置，本命令可以显示]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1848819095}[地址类型、]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[类型、]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[类型、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名类型的成员所属的父亲信息。父亲信息包括：成员所属的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[和]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名，]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名所属的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[，以及]{style="font-family:宋体"}[Zone]{lang="EN-US"}[和]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名所属的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。当]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名没有被加入任何]{style="font-family:宋体"}[Zone]{lang="EN-US"}[时，其父亲信息将只显示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名所属的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1110155561}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1704354521}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[中]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}

[[\<Sysname\> display zone member fcid 010000 vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_721586609}

[fcid 0x010000]{lang="EN-US"}

[  VSAN 1:]{lang="EN-US"}

[    zone z1]{lang="EN-US"}

[    zone z2 ]{lang="EN-US"}

[    zone z3]{lang="EN-US"}

[    zone-alias a1]{lang="EN-US"}

[      zone z2]{lang="EN-US"}

[      zone z3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1204300332}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[11:22:33:44:55:66:77:88]{lang="EN-US"}[的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}

[[\<Sysname\> display zone member pwwn 11:22:33:44:55:66:77:88]{lang="EN-US"}]{#struct_0_x9962_12256_2022163476}

[pwwn 11:22:33:44:55:66:77:88]{lang="EN-US"}

[  VSAN 1:]{lang="EN-US"}

[    zone z1]{lang="EN-US"}

[    zone z2]{lang="EN-US"}

[    zone z3]{lang="EN-US"}

[    zone-alias a1]{lang="EN-US"}

[      zone z2]{lang="EN-US"}

[      zone z3]{lang="EN-US"}

[  VSAN 3:]{lang="EN-US"}

[    zone z1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1319423682}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[12:22:33:44:55:66:77:88]{lang="EN-US"}[的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}

[[\<Sysname\> display zone member fwwn 12:22:33:44:55:66:77:88]{lang="EN-US"}]{#struct_0_x9962_12256_x1687050536}

[fwwn 12:22:33:44:55:66:77:88]{lang="EN-US"}

[  VSAN 1:]{lang="EN-US"}

[    zone z1]{lang="EN-US"}

[    zone z2]{lang="EN-US"}

[    zone z3]{lang="EN-US"}

[    zone-alias a1]{lang="EN-US"}

[      zone z2]{lang="EN-US"}

[      zone z3]{lang="EN-US"}

[  VSAN 3:]{lang="EN-US"}

[    zone z1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1741060920}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[中]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名为]{style="font-family:宋体"}[za1]{lang="EN-US"}[的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员所属的父亲信息。]{style="font-family:宋体"}

[[\<Sysname\> display zone member zone-alias za1 vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_721521073}

[zone-alias za1]{lang="EN-US"}

[  VSAN 1]{lang="EN-US"}[：]{style="font-family:宋体"}

[    zone z1]{lang="EN-US"}

[    zone z2]{lang="EN-US"}

[[表1-39 ]{lang="EN-US"}[display zone member]{lang="EN-US"}]{#struct_0_x9962_12256_742714206}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1106117757}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1642398575}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_642246865}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x870401356}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_721717681}[编号]{style="font-family:宋体"}

[[fcid]{lang="EN-US"}]{#struct_0_x9962_12256_594990263}

[[指定显示的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x180991852}[成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[pwwn]{lang="EN-US"}]{#struct_0_x9962_12256_x1319978521}

[[指定显示的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_667766906}[成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[fwwn]{lang="EN-US"}]{#struct_0_x9962_12256_1319816898}

[[指定显示的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_982773082}[成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[zone-alias]{lang="EN-US"}]{#struct_0_x9962_12256_721652145}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x543918490}[别名的名称]{style="font-family:宋体"}

[[zone]{lang="EN-US"}]{#struct_0_x9962_12256_560969361}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1917739247}[的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x331129883}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member (zone view)]{lang="EN-US"}**]{#struct_0_x9962_12256_1296241221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member (zone-alias view)]{lang="EN-US"}**]{#struct_0_x9962_12256_721848753}

::: {#-1584725374 .myid}
[]{#_Toc404798164}[]{#struct_0_x9962_12256_1319751362}[]{#_Toc385230678}[]{#_Toc367103736}

**FC和FCoE \-- FC Zone配置命令 \-- display zone statistics**

------------------------------------------------------------------------

[**[display zone statistics]{lang="EN-US"}**]{#struct_0_x9962_12256_x2091610065}[命令用来显示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1319292607}

[**[display zone statistics]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1024269361}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_441208215}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1896220393}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1261676314}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2075628103}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2061394155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1319227071}

[**[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_1021082115}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x295843621}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1736165594}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1236722411}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_782256362}[显示]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display zone statistics vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_1319161535}

[VSAN 2:]{lang="EN-US"}

[  Message type      Sent          Received]{lang="EN-US"}

[  Merge Request     19            23]{lang="EN-US"}

[  Merge Accept      17            18]{lang="EN-US"}

[  Merge Reject      6             1]{lang="EN-US"}

[  Change Request    144           18]{lang="EN-US"}

[  Change Accept     0             0]{lang="EN-US"}

[  Change Reject     0             0]{lang="EN-US"}

[[表1-40 ]{lang="EN-US"}[display ]{lang="EN-US"}]{#struct_0_x9962_12256_1058836586}[zone statistics]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1007083747}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x325359505}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1319095999}

[[Message type]{lang="EN-US"}]{#struct_0_x9962_12256_1319554751}

[[报文类型]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319489215}

[[Sent]{lang="EN-US"}]{#struct_0_x9962_12256_1319423679}

[[发送报文的统计信息]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319358143}

[[Received]{lang="EN-US"}]{#struct_0_x9962_12256_1319816895}

[[接收报文的统计信息]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319751359}

[[Merge Request]{lang="EN-US"}]{#struct_0_x9962_12256_x2092068818}

[[合并过程中的请求报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319292608}

[[Merge Accept]{lang="EN-US"}]{#struct_0_x9962_12256_1319227072}

[[合并过程中的应答报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319161536}

[[Merge Reject]{lang="EN-US"}]{#struct_0_x9962_12256_1319096000}

[[合并过程中的拒绝报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319554752}

[[Change Request]{lang="EN-US"}]{#struct_0_x9962_12256_1319489216}

[[扩散过程中的请求报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319423680}

[[Change Accept]{lang="EN-US"}]{#struct_0_x9962_12256_1319358144}

[[扩散过程中的应答报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_611559964}

[[Change Reject]{lang="EN-US"}]{#struct_0_x9962_12256_1319816896}

[[扩散过程中的拒绝报文]{style="font-family:宋体"}]{#struct_0_x9962_12256_1319751360}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2091478993}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset zone statistics]{lang="EN-US"}**]{#struct_0_x9962_12256_1319292605}

::: {#861795488 .myid}
[]{#_Toc404798165}[]{#struct_0_x9962_12256_2004639571}[]{#_Toc308689023}

**FC和FCoE \-- FC Zone配置命令 \-- display zone status**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **zone status**]{lang="EN-US"}]{#struct_0_x9962_12256_1877291297}[命令用来显示]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[的配置信息以及运行状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1093287771}

[**[display]{lang="EN-US"}**[ **zone status** \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x433559178}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_832246452}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1662944617}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1686128881}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_721783217}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1294990478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1515705000}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x992295813}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1952940883}

[**[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x788651022}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[配置信息以及运行状态。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[配置信息以及运行状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1193064900}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_2029755207}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[通过本命令可以查看当前]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}]{#struct_0_x9962_12256_721324462}[的配置信息以及运行状态，包括：]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的模式、默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[策略、扩散和合并类型、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[数据库信息（创建的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的个数）、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的状态（如，正在进行扩散、合并等）。]{style="font-family:宋体"}

[[需要注意的是，增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1319161533}[模式的合并和扩散不受合并和扩散类型影响，所以在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下，不显示合并和扩散类型信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_68730315}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1646202954}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[的配置信息以及运行状态。]{style="font-family:宋体"}

[[\<Sysname\> display zone status]{lang="EN-US"}]{#struct_0_x9962_12256_721258926}

[VSAN 1:]{lang="EN-US"}

[  Mode: basic]{lang="EN-US"}

[  Default zone: deny]{lang="EN-US"}

[  Distribute: active only]{lang="EN-US"}

[  Hard-zoning: enabled]{lang="EN-US"}

[  Full zoning database:]{lang="EN-US"}

[    Zonesets: 10, Zones: 20, Zone-aliases: 0]{lang="EN-US"}

[  Status: merging]{lang="EN-US"}

[VSAN 2:]{lang="EN-US"}

[  Mode: enhanced]{lang="EN-US"}

[  Default zone: permit]{lang="EN-US"}

[  Hard-zoning: enabled]{lang="EN-US"}

[  Full zoning database:]{lang="EN-US"}

[    Zonesets: 10, Zones: 20, Zone-aliases: 0]{lang="EN-US"}

[  Status: distributing]{lang="EN-US"}

[[表1-41 ]{lang="EN-US"}[display zone status]{lang="EN-US"}]{#struct_0_x9962_12256_x1127212225}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1102170073}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1915059985}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_721455534}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1600239407}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_47038839}[编号]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x9962_12256_2078121703}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x228543606}[的模式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[basic]{lang="EN-US"}]{#struct_0_x9962_12256_721389998}[：基本]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enhanced]{lang="EN-US"}]{#struct_0_x9962_12256_x296411940}[：增强]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}

[[Default zone]{lang="EN-US"}]{#struct_0_x9962_12256_x548351633}

[[默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1380287908}[策略，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x9962_12256_721586606}[：默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内成员禁止互访]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x9962_12256_x1204300321}[：默认]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[内成员允许互访]{lang="EN-US" style="font-family:宋体"}

[[Distribute]{lang="EN-US"}]{#struct_0_x9962_12256_456145071}

[[扩散和合并类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_473644875}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active only]{lang="EN-US"}]{#struct_0_x9962_12256_721521070}[：非完全扩散和合并]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[full]{lang="EN-US"}]{#struct_0_x9962_12256_742714205}[：完全扩散和合并]{lang="EN-US" style="font-family:宋体"}

[[因为增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1319489213}[不受扩散和合并类型影响，所以在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下不显示]{style="font-family:宋体"}[Distribute]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Hard-zoning]{lang="EN-US"}]{#struct_0_x9962_12256_1642398574}

[[硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_642181329}[的生效状态，包括（不同]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下状态可能不同）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_x9962_12256_x351177427}[：硬件]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[处于生效状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled (Administratively)]{lang="EN-US"}]{#struct_0_x9962_12256_1319423677}[：用户]{lang="EN-US" style="font-family:宋体"}[通过命令手工]{style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}[硬件]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled (No enough hardware resource)]{lang="EN-US"}]{#struct_0_x9962_12256_x1687247155}[：由于底层资源不足，硬件]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[处于未生效状态]{style="font-family:宋体"}

[[Full Zoning Database]{lang="EN-US"}]{#struct_0_x9962_12256_x37552883}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_721652142}[数据库信息，将显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[、]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的个数]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x9962_12256_x543918493}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_561034897}[的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[merging]{lang="EN-US"}]{#struct_0_x9962_12256_1501337876}[：正在进行合并]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[distributing]{lang="EN-US"}]{#struct_0_x9962_12256_721848750}[：正在进行扩散]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[free]{lang="EN-US"}]{#struct_0_x9962_12256_1877487905}[：空闲状态，表示未处于扩散或合并的过程中]{style="font-family:宋体"}

[[在合并或扩散的过程中，不允许在此]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1485223288}[中进行]{style="font-family:宋体"}[Zone]{lang="EN-US"}[相关的配置]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1962048394}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone default-zone permit]{lang="EN-US"}**]{#struct_0_x9962_12256_721783214}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset distribute full]{lang="EN-US"}**]{#struct_0_x9962_12256_x1294990475}

::: {#295015856 .myid}
[]{#_Toc404798166}[]{#struct_0_x9962_12256_x1112420473}[]{#_Toc308689024}

**FC和FCoE \-- FC Zone配置命令 \-- display zone-alias**

------------------------------------------------------------------------

[**[display zone-alias]{lang="EN-US"}**]{#struct_0_x9962_12256_x327420829}[命令用来显示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1932656986}

[**[display]{lang="EN-US"}**[ **zone-alias** \[ \[ **name** *zone-alias-name* \] **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_671493035}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1692211125}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x206333188}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_721324463}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_68730314}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1388204086}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2003333642}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1846697433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2075937353}

[**[name ]{lang="EN-US"}***[zone-alias-name]{lang="EN-US"}*]{#struct_0_x9962_12256_27881023}[：显示指定名称的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[的相关信息。]{style="font-family:宋体"}*[zone-alias-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}***[ vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_721258927}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[相关信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1127212224}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1270305856}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[根据用户的配置可以显示不同]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_348976044}[别名]{style="font-family:宋体"}[的信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1149735145}**[name]{lang="EN-US"}**[和]{style="font-family:宋体"}**[vsan]{lang="EN-US"}**[参数，则显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内指定名称的单个]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[的信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1911614412}**[vsan]{lang="EN-US"}**[参数，则显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[的信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_x9962_12256_1452662730}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_974011286}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_721455535}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display zone-alias]{lang="EN-US"}]{#struct_0_x9962_12256_x1600239406}

[VSAN 1]{lang="EN-US"}[：]{style="font-family:
宋体"}

[  zone-alias name za1]{lang="EN-US"}

[    fcid 0x111111 initiator]{lang="EN-US"}

[    fcid 0x222222 target]{lang="EN-US"}

[    pwwn 11:11:11:11:22:22:22:22]{lang="EN-US"}

[  zone-alias name za2]{lang="EN-US"}

[    fcid 0x111111]{lang="EN-US"}

[    fwwn 12:11:11:11:22:22:22:22]{lang="EN-US"}

[VSAN 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[  zone-alias name za1]{lang="EN-US"}

[[表1-42 ]{lang="EN-US"}[display zone-alias]{lang="EN-US"}]{#struct_0_x9962_12256_1613122780}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1096774821}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1732699193}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_721389999}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x296411941}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_2051781006}[编号]{style="font-family:宋体"}

[[zone-alias name]{lang="EN-US"}]{#struct_0_x9962_12256_x1768184874}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x748865997}[别名的名称]{style="font-family:宋体"}

[[fcid]{lang="EN-US"}]{#struct_0_x9962_12256_x389958647}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_721586607}[别名成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[pwwn]{lang="EN-US"}]{#struct_0_x9962_12256_x1204300322}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_2022229012}[别名成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[fwwn]{lang="EN-US"}]{#struct_0_x9962_12256_1319161534}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1319095998}[别名成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[initiator]{lang="EN-US"}]{#struct_0_x9962_12256_1356751597}[、]{style="font-family:宋体"}[target]{lang="EN-US"}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1021489166}[成员的角色，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[initiator]{lang="EN-US"}]{#struct_0_x9962_12256_1319554750}[：表示成员角色为发起端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[target]{lang="EN-US"}]{#struct_0_x9962_12256_x2096638229}[：表示成员角色为目的端]{lang="EN-US" style="font-family:宋体"}

[[如果没有标出]{style="font-family:宋体"}[initiator]{lang="EN-US"}]{#struct_0_x9962_12256_x503654645}[或]{style="font-family:宋体"}[target]{lang="EN-US"}[，则表示同时兼具这两种角色]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1774042991}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member (zone-alias view)]{lang="EN-US"}**]{#struct_0_x9962_12256_x1954960029}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone-alias clone]{lang="EN-US"}**]{#struct_0_x9962_12256_721521071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone-alias name]{lang="EN-US"}**]{#struct_0_x9962_12256_742714204}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone-alias rename]{lang="EN-US"}**]{#struct_0_x9962_12256_1642398573}

::: {#-1785927750 .myid}
[]{#_Toc404798167}[]{#struct_0_x9962_12256_642377937}[]{#_Toc308689025}

**FC和FCoE \-- FC Zone配置命令 \-- display zoneset**

------------------------------------------------------------------------

[**[display zoneset]{lang="EN-US"}**]{#struct_0_x9962_12256_305999556}[命令用来显示]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1501834137}

[**[display]{lang="EN-US"}**[ **zoneset** \[ \[ **name** *zoneset-name*\] **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_115712682}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x386438834}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_721717679}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x125053761}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1327997373}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1595651798}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_218293208}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_902987882}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1065683126}

[**[name ]{lang="EN-US"}***[zoneset-name]{lang="EN-US"}*]{#struct_0_x9962_12256_721652143}[：显示指定名称的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}*[zoneset-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}***[ vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x543918492}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_561100433}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x699062612}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[根据用户的配置可以显示不同]{style="font-family:宋体"}[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_1480443535}[的信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{style="font-family:宋体"}]{#struct_0_x9962_12256_577241684}**[name]{lang="EN-US"}**[和]{style="font-family:宋体"}**[vsan]{lang="EN-US"}**[参数，则显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内指定名称的单个]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果仅指定]{lang="EN-US" style="font-family:宋体"}**[vsan]{lang="EN-US"}**]{#struct_0_x9962_12256_1495064620}[参数，则显示]{lang="EN-US" style="font-family:宋体"}[指定]{lang="EN-US" style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有]{lang="EN-US" style="font-family:宋体"}[Zone set]{lang="EN-US"}[的信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则显示所有]{lang="EN-US" style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x766170341}[内所有]{lang="EN-US" style="font-family:宋体"}[Zone set]{lang="EN-US"}[的信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1476599996}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_721848751}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display zoneset]{lang="EN-US"}]{#struct_0_x9962_12256_2004639573}

[VSAN 1:]{lang="EN-US"}

[  zoneset name zs1]{lang="EN-US"}

[    zone name z1]{lang="EN-US"}

[      fcid 0x111111]{lang="EN-US"}

[      fcid 0x222222]{lang="EN-US"}

[      pwwn 11:11:11:11:22:22:22:22]{lang="EN-US"}

[    zone name z2]{lang="EN-US"}

[      fcid 0x111111]{lang="EN-US"}

[      zone-alias name za1]{lang="EN-US"}

[        fcid 0x111112]{lang="EN-US"}

[  zoneset name zs2]{lang="EN-US"}

[    zone name z1]{lang="EN-US"}

[VSAN 2:]{lang="EN-US"}

[VSAN 3:]{lang="EN-US"}

[  zoneset name zs1]{lang="EN-US"}

[    zone name z1]{lang="EN-US"}

[[表1-43 ]{lang="EN-US"}[display zoneset]{lang="EN-US"}]{#struct_0_x9962_12256_1877160225}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1096848829}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_721783215}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1294990476}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1616462882}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1545659534}[编号]{style="font-family:宋体"}

[[zoneset name]{lang="EN-US"}]{#struct_0_x9962_12256_903278829}

[[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x2007558889}[的名称]{style="font-family:宋体"}

[[zone name]{lang="EN-US"}]{#struct_0_x9962_12256_968736040}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1881893476}[的名称]{style="font-family:宋体"}

[[fcid]{lang="EN-US"}]{#struct_0_x9962_12256_347669109}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1977202723}[或者]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[pwwn]{lang="EN-US"}]{#struct_0_x9962_12256_x2007624425}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_96201869}[或者]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[zone-alias name]{lang="EN-US"}]{#struct_0_x9962_12256_x1597228074}

[[Zone ]{lang="EN-US"}]{#struct_0_x9962_12256_x1107720397}[别名的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1538269891}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member (zoneset view)]{lang="EN-US"}**]{#struct_0_x9962_12256_552093074}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset clone]{lang="EN-US"}**]{#struct_0_x9962_12256_x2007427817}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset name]{lang="EN-US"}**]{#struct_0_x9962_12256_x936967325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset rename]{lang="EN-US"}**]{#struct_0_x9962_12256_390497573}

::: {#-1637097212 .myid}
[]{#_Toc404798168}[]{#struct_0_x9962_12256_x542023349}[]{#_Toc308689026}

**FC和FCoE \-- FC Zone配置命令 \-- display zoneset active**

------------------------------------------------------------------------

[**[display zoneset active]{lang="EN-US"}**]{#struct_0_x9962_12256_x1341613110}[命令用来显示]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1707420633}

[**[display]{lang="EN-US"}**[ **zoneset active** \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1205244212}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007493353}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1338533711}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x311070587}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1915039311}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1482919318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1708571331}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x343926143}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1947314675}

[**[vsan]{lang="EN-US"}***[ vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007296745}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[相关信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1818316937}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_867086865}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[同一]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1098795014}[内只会存在一个]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[显示信息的格式遵循下列规则：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1363788994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[根据用户所配置的成员类型，按照]{style="font-family:宋体"}]{#struct_0_x9962_12256_x613638524}[FC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[和]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[的顺序依次分类显示，同种类型的成员按照各自配置值所对应]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码升序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于在本地名称服务数据库中能够查找到的成员，即实际存在的成员，在显示结果的对应条目前面加上"]{style="font-family:宋体"}]{#struct_0_x9962_12256_384628363}[\*]{lang="EN-US"}["。如果用户配置的是成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[，那么交换机会在名称服务数据库中查找对应的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址并显示出来，并将配置的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[用"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["标注在]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址后面。如果用户配置的是成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[，那么交换机会在名称服务数据库中查找从该]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[成员登录的所有]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址并显示出来，并将配置的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[用"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["标注在]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址后面。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于在本地名称服务数据库中不存在的成员，则显示为用户的配置内容。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1372731784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不支持在]{lang="EN-US" style="font-family:宋体"}[Active Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x886887683}[信息中以]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[别名显示成员。配置激活]{lang="EN-US" style="font-family:宋体"}[Zone set]{lang="EN-US"}[后，如果该]{lang="EN-US" style="font-family:宋体"}[Zone set]{lang="EN-US"}[中的]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[存在]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[别名类型成员，会直接将]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[别名中的非重复]{lang="EN-US" style="font-family:宋体"}[N_Port]{lang="EN-US"}[成员添加进入]{lang="EN-US" style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了允许默认]{style="font-family:宋体"}]{#struct_0_x9962_12256_x226581689}[Zone]{lang="EN-US"}[成员互相访问策略，则会显示默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内的有效成员。即在本地名称服务数据库中存在的，并且不属于]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[的成员，都进行显示。显示信息中将显示这些有效成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007362281}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1239366163}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display zoneset active]{lang="EN-US"}]{#struct_0_x9962_12256_x2007165673}

[  ]{lang="DE"}[VSAN 1:]{lang="EN-US"}

[    ]{lang="DE"}[zoneset name zs1]{lang="EN-US"}

[      ]{lang="DE"}[zone name z1]{lang="EN-US"}

[        ]{lang="DE"}[\*fcid 0x222222]{lang="EN-US"}

[        ]{lang="DE"}[\*fcid 0x111111 \[pwwn 11:11:11:11:11:11:11:11\]]{lang="EN-US"}

[      ]{lang="DE"}[zone name z2]{lang="EN-US"}

[        fcid 0x123456]{lang="DE"}

[        ]{lang="DE"}[\*fcid 0x111111 \[pwwn 11:11:11:11:11:11:11:11\]]{lang="EN-US"}

[        pwwn ]{lang="DE"}[11:11:11:11:11:11:11:12]{lang="EN-US"}

[        ]{lang="DE"}[\*fcid 0x333333 \[pwwn 33:33:33:33:33:33:33:33\]]{lang="EN-US"}

[      zone name #default-zone#]{lang="EN-US"}

[        \*fcid 0x20abcd]{lang="EN-US"}

[        \*fcid 0xabcdef]{lang="EN-US"}

[  VSAN 2:]{lang="DE"}

[  VSAN 3:]{lang="DE"}

[    zoneset name zs1]{lang="DE"}

[      ]{lang="DE"}[zone name z1]{lang="EN-US"}

[         fcid 0x123456]{lang="EN-US"}

[        ]{lang="DE"}[\*fcid 0x111111 \[pwwn 11:11:11:11:11:11:11:11\]]{lang="EN-US"}

[        pwwn 11:11:11:11:11:11:11:12]{lang="DE"}

[        \*fcid 0x333333 \[pwwn 33:33:33:33:33:33:33:33\]]{lang="DE"}

[        \*fcid 0x222221 \[fwwn 22:22:22:22:22:22:22:22\]]{lang="DE"}

[        ]{lang="DE"}[\*fcid 0x222222 \[fwwn 22:22:22:22:22:22:22:22\]]{lang="EN-US"}

[        \*fcid 0x222223 \[fwwn 22:22:22:22:22:22:22:22\]]{lang="EN-US"}

[        fwwn aa:bb:cc:dd:ee:ff:00:11]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_206852313}[显示]{style="font-family:宋体"}[VSAN 1]{lang="DE"}[内的]{style="font-family:宋体"}[Active Zone set]{lang="DE"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display zoneset active vsan 1]{lang="DE"}]{#struct_0_x9962_12256_1936893244}

[  VSAN 1:]{lang="DE"}

[    zoneset name zs1]{lang="DE"}

[      zone name z1]{lang="DE"}

[        ]{lang="DE"}[\*fcid 0x222222]{lang="EN-US"}

[        ]{lang="DE"}[\*fcid 0x111111 \[pwwn 11:11:11:11:11:11:11:11\]]{lang="EN-US"}

[      ]{lang="DE"}[zone name z2]{lang="EN-US"}

[        fcid 0x123456]{lang="DE"}

[        \*fcid 0x111111 \[pwwn 11:11:11:11:11:11:11:11\]]{lang="DE"}

[        pwwn 11:11:11:11:11:11:11:12]{lang="DE"}

[        \*fcid 0x333333 \[pwwn 33:33:33:33:33:33:33:33\]]{lang="DE"}

[      ]{lang="DE"}[zone name #default_zone#]{lang="FR"}

[        \*fcid 0x20abcd]{lang="FR"}

[        \*fcid 0xabcdef]{lang="FR"}

[[表1-44 ]{lang="EN-US"}[display zoneset active]{lang="EN-US"}]{#struct_0_x9962_12256_401049778}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1091112385}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007231209}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1337644784}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_203113077}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1466103758}[编号]{style="font-family:宋体"}

[[zoneset name]{lang="EN-US"}]{#struct_0_x9962_12256_870681605}

[[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x2007034601}[的名称]{style="font-family:宋体"}

[[zone name]{lang="EN-US"}]{#struct_0_x9962_12256_1646539284}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1559929683}[的名称]{style="font-family:宋体"}

[[\*fcid]{lang="EN-US"}]{#struct_0_x9962_12256_1469554233}

[[本地名称服务数据库中存在的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1072683628}[成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[fcid]{lang="EN-US"}]{#struct_0_x9962_12256_x2007100137}

[[本地名称服务数据库中不存在的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_87245030}[成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[pwwn]{lang="EN-US"}]{#struct_0_x9962_12256_x1117289800}

[[用户配置的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x117446863}[成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[fwwn]{lang="EN-US"}]{#struct_0_x9962_12256_x613245308}

[[用户配置的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x613179772}[成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[#default_zone#]{lang="FR"}]{#struct_0_x9962_12256_x2007558888}

[[默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1760147315}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x942768411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset activate name]{lang="EN-US"}**]{#struct_0_x9962_12256_x969361846}

::: {#-1962604479 .myid}
[]{#_Toc404798169}[]{#struct_0_x9962_12256_1037997442}[]{#_Toc308689027}

**FC和FCoE \-- FC Zone配置命令 \-- member (zone view)**

------------------------------------------------------------------------

[**[member]{lang="EN-US"}**]{#struct_0_x9962_12256_1682945575}[命令用来在]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内添加成员。]{style="font-family:宋体"}

[**[undo member]{lang="EN-US"}**]{#struct_0_x9962_12256_x104284842}[命令用来在]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内删除成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007624424}

[**[member]{lang="EN-US"}**[ { { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* } \[ **initiator** \| **target** \] \| **zone-alias** *zone-alias-name* }]{lang="EN-US"}]{#struct_0_x9962_12256_x613114236}

[**[undo member]{lang="EN-US"}**[ { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* \| **zone-alias** *zone-alias-name* }]{lang="EN-US"}]{#struct_0_x9962_12256_x972053370}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x49351754}

[[新建的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_937990821}[内不存在任何成员。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1767419681}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_776151826}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007427816}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1791916030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_320225468}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1513221530}

[**[fcid ]{lang="EN-US"}***[fcid]{lang="EN-US"}*]{#struct_0_x9962_12256_1311477962}[：所配置成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[xxxxxx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[fwwn ]{lang="EN-US"}***[fwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_x613704059}[：所配成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[，]{style="font-family:宋体"}*[fwwn]{lang="EN-US"}*[是交换机上某]{style="font-family:宋体"}[F_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[fwwn]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。配置本参数后，从该]{style="font-family:宋体"}[F_Port]{lang="EN-US"}[登录的所有]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[都添加到该]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内。]{style="font-family:宋体"}

[**[pwwn ]{lang="EN-US"}***[pwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_48986426}[：所配置成员的]{style="font-family:
宋体"}[PWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[initiator]{lang="EN-US"}**]{#struct_0_x9962_12256_x613638523}[：表示成员角色为发起端。]{style="font-family:宋体"}

[**[target]{lang="EN-US"}**]{#struct_0_x9962_12256_166819764}[：表示成员角色为目的端。不指定]{style="font-family:宋体"}**[initiator]{lang="EN-US"}**[和]{style="font-family:宋体"}**[target]{lang="EN-US"}**[参数]{style="font-family:宋体"}[时，表示同时兼具这两种角色。]{style="font-family:宋体"}

[**[zone-alias ]{lang="EN-US"}***[zone-alias-name]{lang="EN-US"}*]{#struct_0_x9962_12256_2016829213}[：指定]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。指定的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_337806317}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_2029886279}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_560348456}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令用于向当前]{style="font-family:宋体"}]{#struct_0_x9962_12256_1734189337}[Zone]{lang="EN-US"}[添加或删除成员，为成员指定或更改角色。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当同一个成员以相同的配置方式（]{style="font-family:宋体"}]{#struct_0_x9962_12256_x25344711}[FC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[、]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[或]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名）多次指定角色时，该成员的角色为最后一次指定的值。例如：两次均以]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址方式指定成员角色，第一次指定为]{style="font-family:宋体"}**[initiator]{lang="EN-US"}**[，第二次指定为]{style="font-family:宋体"}**[target]{lang="EN-US"}**[，则该成员的角色为]{style="font-family:宋体"}**[target]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当同一个成员以不同的配置方式多次指定角色时，该成员的角色为多次指定的并集。例如：第一次以]{style="font-family:宋体"}]{#struct_0_x9962_12256_1125106251}[FC]{lang="EN-US"}[地址方式指定成员角色为]{style="font-family:宋体"}**[initiator]{lang="EN-US"}**[，第二次以]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[方式指定成员角色为]{style="font-family:宋体"}**[target]{lang="EN-US"}**[，则该成员将同时兼具这两种角色。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成员角色在开启]{style="font-family:宋体"}]{#struct_0_x9962_12256_x613572987}[Pairwise]{lang="EN-US"}[特性时才生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x432724006}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2007493352}[创建]{style="font-family:宋体"}[Zone z1]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_227550230}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone name z1]{lang="EN-US"}

[\[Sysname-vsan1-zone-z1\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_291705311}[添加]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[为]{style="font-family:宋体"}[z1]{lang="EN-US"}[的成员，并指明成员角色为发起端。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zone-z1\] member fcid 010000 initiator]{lang="EN-US"}]{#struct_0_x9962_12256_688495316}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1648761349}[添加]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[01:02:03:04:05:06:07:08]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[为]{style="font-family:宋体"}[z1]{lang="EN-US"}[的成员，并指明成员角色为目的端。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zone-z1\] member pwwn 01:02:03:04:05:06:07:08 target]{lang="EN-US"}]{#struct_0_x9962_12256_x1157438087}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x613507451}[恢复]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[01:02:03:04:05:06:07:08]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[的角色为兼具两种角色。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zone-z1\] member pwwn 01:02:03:04:05:06:07:08]{lang="EN-US"}]{#struct_0_x9962_12256_580601627}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1991181287}[添加]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[08:07:06:05:04:03:02:01]{lang="EN-US"}[的]{style="font-family:宋体"}[F_Port]{lang="EN-US"}[为]{style="font-family:宋体"}[z1]{lang="EN-US"}[的成员，并指明成员同时兼具两种角色。]{style="font-family:宋体"}

[[\[Sysname-vsan2-zone-z1\] member fwwn 08:07:06:05:04:03:02:01]{lang="EN-US"}]{#struct_0_x9962_12256_x613441915}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2007296744}[添加]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[za1]{lang="EN-US"}[为]{style="font-family:宋体"}[z1]{lang="EN-US"}[的成员，其中]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[za1]{lang="EN-US"}[已经存在。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zone-z1\] member zone-alias za1]{lang="EN-US"}]{#struct_0_x9962_12256_x252232996}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x32438104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone]{lang="EN-US"}**]{#struct_0_x9962_12256_2063693206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone member]{lang="EN-US"}**]{#struct_0_x9962_12256_x1145723554}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pairwise-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x910991870}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone name]{lang="EN-US"}**]{#struct_0_x9962_12256_x1726692174}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone-alias name]{lang="EN-US"}**]{#struct_0_x9962_12256_x354188054}
:::

::: {#1026106211 .myid}
[]{#_Toc404798170}[]{#struct_0_x9962_12256_716084955}[]{#_Toc308689028}

**FC和FCoE \-- FC Zone配置命令 \-- member (zone alias view)**

------------------------------------------------------------------------

[**[member]{lang="EN-US"}**]{#struct_0_x9962_12256_x2007362280}[命令用来在]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名内添加成员。]{style="font-family:宋体"}

[**[undo member]{lang="EN-US"}**]{#struct_0_x9962_12256_x326717778}[命令用来在]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名内删除成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_373984479}

[**[member]{lang="EN-US"}**[ { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* } \[ **initiator** \| **target** \]]{lang="EN-US"}]{#struct_0_x9962_12256_x613376379}

[**[undo member]{lang="EN-US"}**[ { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* }]{lang="EN-US"}]{#struct_0_x9962_12256_x165626998}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1383850402}

[[新建的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_351128362}[别名内不存在任何成员。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007165672}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1359231628}[别名视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_494056641}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x783715501}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1601670163}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1777804193}

[**[fcid ]{lang="EN-US"}***[fcid]{lang="EN-US"}*]{#struct_0_x9962_12256_848037491}[：所配置成员的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[xxxxxx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[fwwn ]{lang="EN-US"}***[fwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_x613245307}[：所配成员的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[，]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[是交换机上某]{style="font-family:宋体"}[F_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。配置本参数后，从该]{style="font-family:宋体"}[F_Port]{lang="EN-US"}[登录的所有]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[都添加到该]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名内。]{style="font-family:宋体"}

[**[pwwn ]{lang="EN-US"}***[pwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_566584263}[：所配置成员的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[initiator]{lang="EN-US"}**]{#struct_0_x9962_12256_x1733218357}[：表示成员角色为发起端。]{style="font-family:宋体"}

[**[target]{lang="EN-US"}**]{#struct_0_x9962_12256_369124946}[：表示成员角色为目的端。不指定]{style="font-family:宋体"}**[initiator]{lang="EN-US"}**[和]{style="font-family:宋体"}**[target]{lang="EN-US"}**[参数]{style="font-family:宋体"}[时，表示同时兼具这两种角色。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x175753613}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_867152401}[交换机支持本命令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1700847433}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令用于向当前]{style="font-family:宋体"}]{#struct_0_x9962_12256_x613179771}[Zone]{lang="EN-US"}[别名添加或删除成员，为成员指定或更改角色。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当同一个成员以相同的配置方式（]{style="font-family:宋体"}]{#struct_0_x9962_12256_1359086163}[FC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[、]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[或]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名）多次指定角色时，该成员的角色为最后一次指定的值。例如：两次均以]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址方式指定成员角色，第一次指定为]{style="font-family:宋体"}**[initiator]{lang="EN-US"}**[，第二次指定为]{style="font-family:宋体"}**[target]{lang="EN-US"}**[，则该成员的角色为]{style="font-family:宋体"}**[target]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当同一个成员以不同的配置方式多次指定角色时，该成员的角色为多次指定的并集。例如：第一次以]{style="font-family:宋体"}]{#struct_0_x9962_12256_477587829}[FC]{lang="EN-US"}[地址方式指定成员角色为]{style="font-family:宋体"}**[initiator]{lang="EN-US"}**[，第二次以]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[方式指定成员角色为]{style="font-family:宋体"}**[target]{lang="EN-US"}**[，则该成员将同时兼具这两种角色。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[成员角色在开启]{style="font-family:宋体"}]{#struct_0_x9962_12256_600930746}[Pairwise]{lang="EN-US"}[特性时才生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007231208}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1391238571}[创建]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[za1]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1285910398}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone-alias name za1]{lang="EN-US"}

[\[Sysname-vsan1-zone-alias-za1\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1226733140}[添加]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[为]{style="font-family:宋体"}[za1]{lang="EN-US"}[的成员，并指明成员角色为发起端。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zone-alias-za1\] member fcid 010000 initiator]{lang="EN-US"}]{#struct_0_x9962_12256_1770492244}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_65215924}[添加]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[01:02:03:04:05:06:07:08]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[为]{style="font-family:宋体"}[za1]{lang="EN-US"}[的成员，并指明成员角色为目的端。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zone-alias-za1\] member pwwn 01:02:03:04:05:06:07:08 target]{lang="EN-US"}]{#struct_0_x9962_12256_x2007034600}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x613114235}[添加]{style="font-family:宋体"}[FWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[08:07:06:05:04:03:02:01]{lang="EN-US"}[的]{style="font-family:宋体"}[F_Port]{lang="EN-US"}[为]{style="font-family:宋体"}[za1]{lang="EN-US"}[的成员，并指明成员同时兼具两种角色。]{style="font-family:宋体"}

[[\[Sysname-vsan2-zone-alias-za1\] member fwwn 08:07:06:05:04:03:02:01]{lang="EN-US"}]{#struct_0_x9962_12256_x613704062}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1082344071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone-alias]{lang="EN-US"}**]{#struct_0_x9962_12256_156322114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone-alias name]{lang="EN-US"}**]{#struct_0_x9962_12256_x444479316}
:::

::: {#-903927227 .myid}
[]{#_Toc404798171}[]{#struct_0_x9962_12256_x111138112}[]{#_Toc308689029}

**FC和FCoE \-- FC Zone配置命令 \-- member (zone set view)**

------------------------------------------------------------------------

[**[member]{lang="EN-US"}**]{#struct_0_x9962_12256_x651856141}[命令用来在]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[内添加]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo member]{lang="EN-US"}**]{#struct_0_x9962_12256_x975751322}[命令用来在]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[内删除]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1122143753}

[**[member]{lang="EN-US"}**[ *zone-*]{lang="EN-US"}*[name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007100136}

[**[undo]{lang="EN-US"}**[ **member** *zone-name*]{lang="EN-US"}]{#struct_0_x9962_12256_x1478838911}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_910941007}

[[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_1424900363}[内不存在任何]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1378431675}

[[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_1368506341}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_806293191}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2007558891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1325031936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1010653060}

[*[zone-name]{lang="FR"}*]{#struct_0_x9962_12256_1727654998}[：]{style="font-family:宋体"}[Zone]{lang="FR"}[的]{style="font-family:
宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。指定的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_463867874}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1285708359}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1268212026}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1027161410}[创建]{style="font-family:宋体"}[Zone z1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1584158627}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone name z1]{lang="EN-US"}

[\[Sysname-vsan1-zone-z1\] quit]{lang="EN-US"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_x2007624427}[创建]{style="font-family:宋体"}[Zone set zs1]{lang="DE"}[并进入]{style="font-family:宋体"}[其]{style="font-family:宋体"}[视图。]{style="font-family:宋体"}

[[\[Sysname\] zoneset name zs1]{lang="EN-US"}]{#struct_0_x9962_12256_x1066597545}

[\[Sysname-vsan1-zoneset-zs1\]]{lang="EN-US"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_x1339278593}[添加]{style="font-family:宋体"}[z1]{lang="DE"}[为]{style="font-family:
宋体"}[zs1]{lang="DE"}[的]{style="font-family:宋体"}[成员。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zoneset-zs1\] member z1]{lang="EN-US"}]{#struct_0_x9962_12256_2104768944}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_941800486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zoneset]{lang="EN-US"}**]{#struct_0_x9962_12256_1431303455}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone name]{lang="EN-US"}**]{#struct_0_x9962_12256_x1356363306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset name]{lang="EN-US"}**]{#struct_0_x9962_12256_x2007427819}
:::

::: {#498844439 .myid}
[]{#_Toc404798172}[]{#struct_0_x9962_12256_x613507454}[]{#_Toc385230684}[]{#_Toc367103737}

**FC和FCoE \-- FC Zone配置命令 \-- pairwise-zoning enable**

------------------------------------------------------------------------

[**[pairwise-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_580405019}[命令用来开启当前]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的]{style="font-family:宋体"}[Pairwise]{lang="EN-US"}[特性。]{style="font-family:宋体"}

[**[undo pairwise-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1474096403}[命令用来关闭当前]{style="font-family:
宋体"}[Zone]{lang="EN-US"}[的]{style="font-family:宋体"}[Pairwise]{lang="EN-US"}[特性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1196708352}

[**[pairwise-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_854834743}

[**[undo pairwise-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x613441918}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x911712766}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x2053183096}[的]{style="font-family:宋体"}[Pairwise]{lang="EN-US"}[特性处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1743087869}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1826204818}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_911565237}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1264764594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x227524731}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x613376382}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_2029951815}[交换机支持本命令。]{style="font-family:宋体"}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x165037175}[成员的角色有两种：]{style="font-family:宋体"}[Initiator]{lang="EN-US"}[和]{style="font-family:宋体"}[Target]{lang="EN-US"}[，分别表示发起端和目的端。一个]{style="font-family:宋体"}[Zone]{lang="EN-US"}[成员可以同时兼具这两种角色。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x700821350}[中开启]{style="font-family:宋体"}[Pairwise]{lang="EN-US"}[特性后，该]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内节点间的访问会受到成员角色的影响，即同一]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内具有不同角色的成员可以互相访问，角色相同的成员间不允许互相访问，兼具两种角色的成员可以和任意角色的成员互相访问。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x797546883}[中关闭]{style="font-family:宋体"}[Pairwise]{lang="EN-US"}[特性后，该]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内节点间的访问不会受到成员角色的影响，即同一]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内的所有成员之间都可以互相访问。]{style="font-family:宋体"}

[[Pairwise]{lang="EN-US"}]{#struct_0_x9962_12256_x1644163261}[特性开启后不会立即生效，需要重新激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[才能生效。]{style="font-family:宋体"}

[[本配置会在激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x1240907746}[或配置扩散命令后，与]{style="font-family:宋体"}[Zone]{lang="EN-US"}[信息一起在]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[中扩散。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x232656704}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x613310846}[开启]{style="font-family:宋体"}[z1]{lang="EN-US"}[的]{style="font-family:宋体"}[Pairwise]{lang="EN-US"}[特性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x149695913}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] zone name z1]{lang="EN-US"}

[\[Sysname-vsan2-zone-z1\] pairwise-zoning enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_435925950}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member (zone view)]{lang="EN-US"}**]{#struct_0_x9962_12256_849100941}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member (zone-alias view)]{lang="EN-US"}**]{#struct_0_x9962_12256_x613245310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset activate]{lang="EN-US"}**]{#struct_0_x9962_12256_x1733546036}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset distribute]{lang="EN-US"}**]{#struct_0_x9962_12256_489777309}
:::

::: {#-874205088 .myid}
[]{#_Toc404798173}[]{#struct_0_x9962_12256_1496180277}[]{#_Toc385230685}[]{#_Toc367103738}[]{#_Toc363662132}

**FC和FCoE \-- FC Zone配置命令 \-- reset zone statistics**

------------------------------------------------------------------------

[**[reset zone statistics]{lang="NO-BOK"}**]{#struct_0_x9962_12256_x106080111}[命令用来清除]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1925451651}

[**[reset zone statisti]{lang="NO-BOK"}[cs]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x613179774}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1358758483}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_836422016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1121807765}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1408123325}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2110875015}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x613114238}

[**[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_x971135866}[：清除指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定本参数，将清除所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_510922041}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1861665418}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x944939065}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1492178144}[清除]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset zone statistics vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_1717954505}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_916903529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone statistics]{lang="EN-US"}**]{#struct_0_x9962_12256_1724102754}
:::

::: {#-461479085 .myid}
[]{#_Toc404798174}[]{#struct_0_x9962_12256_x613704061}[]{#_Toc385230686}[]{#_Toc381974738}[]{#_Toc369534884}[]{#_Toc381787141}

**FC和FCoE \-- FC Zone配置命令 \-- snmp-agent trap enable fc-zone**

------------------------------------------------------------------------

[**[snmp-agent trap enable fc-zone]{lang="EN-US"}**]{#struct_0_x9962_12256_x587356883}[命令用来开启]{style="font-family:
宋体"}[Zone]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable fc-zone]{lang="EN-US"}**]{#struct_0_x9962_12256_x1370428765}[命令用来关闭]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1500392918}

[**[snmp-agent trap enable fc-zone]{lang="EN-US"}**[ \[ **activation-completed** \| **defaultzone-change** \| **hardzone-change** \| **merge-failed** \| **merge-succeeded** \] \*]{lang="EN-US"}]{#struct_0_x9962_12256_x1416283435}

[**[undo snmp-agent trap enable fc-zone]{lang="EN-US"}**[ \[ **activation-completed** \| **defaultzone-change** \| **hardzone-change** \| **merge-failed** \| **merge-succeeded** \] \*]{lang="EN-US"}]{#struct_0_x9962_12256_880677902}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x464169247}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_852619392}[的告警功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x613638525}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_166950836}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1950896562}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2127053247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x251034316}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_850337592}

[**[activation-completed]{lang="EN-US"}**]{#struct_0_x9962_12256_x2046384287}[：表示已完成激活]{style="font-family:宋体"}[/]{lang="EN-US"}[取消激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}

[**[defaultzone-change]{lang="EN-US"}**]{#struct_0_x9962_12256_1205241048}[：表示默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[策略发生变化的告警信息。]{style="font-family:宋体"}

[**[hardzone-change]{lang="EN-US"}**]{#struct_0_x9962_12256_x942827317}[：表示硬]{style="font-family:宋体"}[Zone]{lang="EN-US"}[功能已关闭的告警信息。]{style="font-family:宋体"}

[**[merge-failed]{lang="EN-US"}**]{#struct_0_x9962_12256_x613572989}[：表示合并失败的告警信息。]{style="font-family:宋体"}

[**[merge-succeeded]{lang="EN-US"}**]{#struct_0_x9962_12256_656730447}[：表示合并成功的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_475049970}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1270502464}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[如果未指定任何参数，则表示开启或关闭]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1613152050}[的全部告警功能。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_968223386}[的告警功能之后，]{style="font-family:宋体"}[Zone]{lang="EN-US"}[会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1341508640}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x613507453}[开启]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的全部告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_580732699}

[\[Sysname\] snmp-agent trap enable fc-zone]{lang="EN-US"}
:::

::: {#1032616269 .myid}
[]{#_Toc404798175}[]{#struct_0_x9962_12256_x1743536379}[]{#_Toc308689030}

**FC和FCoE \-- FC Zone配置命令 \-- zone clone**

------------------------------------------------------------------------

[**[zone clone]{lang="EN-US"}**]{#struct_0_x9962_12256_1648879674}[命令用来复制]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1811897415}

[**[zone clone ]{lang="EN-US"}***[src-name dest-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x269322057}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1817446942}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1106842157}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1017043668}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2007493355}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1793634171}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x592237871}

[*[src-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x12281320}[：被复制的源]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[*[dest-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x796041299}[：复制后的目的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_463933410}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1867459980}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1123463326}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1180995887}[创建]{style="font-family:宋体"}[Zone z1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x2007296747}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone name z1]{lang="EN-US"}

[\[Sysname-vsan1-zone-z1\] quit]{lang="EN-US"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_1313850945}[复制]{style="font-family:宋体"}[z1]{lang="EN-US"}[到]{style="font-family:宋体"}[z2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zone clone z1 z2]{lang="EN-US"}]{#struct_0_x9962_12256_1887241249}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2136009811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone]{lang="EN-US"}**]{#struct_0_x9962_12256_1462778072}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone name]{lang="EN-US"}**]{#struct_0_x9962_12256_x1764184422}
:::

::: {#-289706831 .myid}
[]{#_Toc404798176}[]{#struct_0_x9962_12256_x1555631795}[]{#_Toc308689031}

**FC和FCoE \-- FC Zone配置命令 \-- zone default-zone permit**

------------------------------------------------------------------------

[**[zone default-zone permit]{lang="FR"}**]{#struct_0_x9962_12256_x2007362283}[命令用来配置允许默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内的成员互相访问。]{style="font-family:宋体"}

[**[undo zone default-zone permit]{lang="FR"}**]{#struct_0_x9962_12256_76566749}[命令用来配置禁止默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内的成员互相访问。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x934067684}

[**[zone default-zone permit]{lang="FR"}**]{#struct_0_x9962_12256_2078966742}

[**[undo zone default-zone permit]{lang="FR"}**]{#struct_0_x9962_12256_1685185243}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276513187}

[[默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1342863107}[内的成员禁止互相访问。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1580544461}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2007165675}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x955947101}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1826603697}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1214812534}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x613245309}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x698866004}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x1734135861}[模式下，需要通过激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[或扩散命令显式地触发扩散，使默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[策略随同其它数据一同向全网扩散。但是在基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下，必须手动配置全网默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[策略一致。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1736084856}[模式切换时，为保证切换后全网默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[策略的一致性，无论是基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[向增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[切换，还是增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[向基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[扩散，默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[策略也会随同其它数据一同向全网扩散。]{style="font-family:宋体"}

[[在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1098728115}[模式下，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内交换机发生合并时，要求发生合并的交换机必须具有相同的默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[策略，否则合并失败，链路将被隔离。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1204872472}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_971104988}[配置允许默认]{style="font-family:宋体"}[Zone]{lang="EN-US"}[内的成员互相访问。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1285706481}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone default-zone permit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007231211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **zone status**]{lang="EN-US"}]{#struct_0_x9962_12256_981348888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone mode enhanced]{lang="EN-US"}**]{#struct_0_x9962_12256_x613179773}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset acti]{lang="EN-US"}**]{#struct_0_x9962_12256_1359217235}**[vate]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset distribute]{lang="EN-US"}**]{#struct_0_x9962_12256_480113939}
:::

::: {#2109614673 .myid}
[]{#_Toc367103740}[]{#_Toc363662133}[]{#_Toc404798177}[]{#struct_0_x9962_12256_1863788544}[]{#_Toc385230688}[]{#_Toc369704437}[]{#_Toc363482401}

**FC和FCoE \-- FC Zone配置命令 \-- zone hard-zoning enable**

------------------------------------------------------------------------

[**[zone hard-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1757827433}[命令用来开启]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo zone hard-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_278788655}[命令用来关闭]{style="font-family:
宋体"}[VSAN]{lang="EN-US"}[下硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x613114237}

[**[zone hard-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x971987834}

[**[undo zone hard-zoning enable]{lang="EN-US"}**]{#struct_0_x9962_12256_228936170}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x243081495}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1019575044}[下的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_832614421}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1980267291}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x613704064}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x587553491}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x390475722}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x548305928}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_510987577}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[当底层资源足够下发]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x227101895}[规则时，硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[才能生效，而软件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[一直处于生效状态。当底层资源足够下发当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[规则时，该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的软件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[和硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[一起生效；当底层资源不够下发当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[规则时，为了保证规则的完整性，系统会清空该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[已下发的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[规则，自动切换为硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[未生效状态，此时该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[下只有软件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[继续生效。]{style="font-family:宋体"}

[[当用户希望增强某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_580285801}[的安全性时，可以开启该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。当用户认为软件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[能够满足某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的节点访问控制要求时，可以关闭该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[，节约硬件表项资源供其它重要]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[使用。]{style="font-family:宋体"}

[[开启某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x613638528}[的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[后，系统将触发一次下发该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的所有]{style="font-family:宋体"}[Zone]{lang="EN-US"}[规则的操作；关闭某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[后，系统会清空该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[当前已经下发的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[规则，并且后续不会下发任何新的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_166098868}[模式下，需要通过激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[或扩散命令显式地触发扩散，使硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[配置随同其它数据一同向全网扩散。但是在基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下，必须手动配置保证全网硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[配置的一致性。]{style="font-family:宋体"}

[[用户可以通过]{style="font-family:宋体"}**[display zone status]{lang="EN-US"}**]{#struct_0_x9962_12256_950644180}[命令查询当前硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的生效状态。]{style="font-family:宋体"}

[[需要注意的是，当交换机处于合并或扩散状态时，不能配置本命令。]{style="font-family:宋体"}]{#struct_0_x9962_12256_967685544}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_655733099}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_475662065}[关闭]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[下硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x613572992}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] undo zone hard-zoning enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_657320270}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone status]{lang="EN-US"}**]{#struct_0_x9962_12256_x328597387}
:::

::: {#-1062936565 .myid}
[]{#_Toc404798178}[]{#struct_0_x9962_12256_x573469530}[]{#_Toc385230689}

**FC和FCoE \-- FC Zone配置命令 \-- zone merge-control restrict**

------------------------------------------------------------------------

[**[zone merge-control restrict]{lang="EN-US"}**]{#struct_0_x9962_12256_116910350}[命令用来在增强]{style="font-family:
宋体"}[Zone]{lang="EN-US"}[模式下，配置当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的合并控制模式为]{style="font-family:宋体"}[Restrict]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo zone merge-control restrict]{lang="EN-US"}**]{#struct_0_x9962_12256_1368437118}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x387677308}

[**[zone merge-control restrict]{lang="EN-US"}**]{#struct_0_x9962_12256_116761341}

[**[undo zone merge-control restrict]{lang="EN-US"}**]{#struct_0_x9962_12256_x613507456}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_580536091}

[[合并控制模式为]{style="font-family:宋体"}[Allow]{lang="EN-US"}]{#struct_0_x9962_12256_1686704906}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1223707004}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1647623908}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_810667768}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_782211850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1870970643}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x613441920}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_867283473}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[合并控制模式分为两种：]{style="font-family:宋体"}[Restrict]{lang="EN-US"}]{#struct_0_x9962_12256_x911188477}[和]{style="font-family:宋体"}[Allow]{lang="EN-US"}[。在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下，当]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的两台交换机发生合并时，合并操作的结果受其所配置的合并控制模式的影响。并且，只有当发生合并的交换机具有相同的合并控制模式时才允许进行合并，否则合并失败，链路将被隔离。]{style="font-family:宋体"}

[[需要注意到是，本命令仅支持在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1437234925}[模式下配置，该配置需要通过激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[或扩散命令显式地触发扩散，保证全网一致性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1363393809}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1265831638}[配置]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[的合并控制模式为]{style="font-family:宋体"}[Restrict]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x613376384}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] zone merge-control restrict]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x165430391}[配置]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[的合并控制模式为]{style="font-family:宋体"}[Allow]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan2\] undo zone merge-control restrict]{lang="EN-US"}]{#struct_0_x9962_12256_2053906763}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_95706015}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone mode enhanced]{lang="EN-US"}**]{#struct_0_x9962_12256_x1660833387}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset activate]{lang="EN-US"}**]{#struct_0_x9962_12256_993545441}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset distribute]{lang="EN-US"}**]{#struct_0_x9962_12256_512843730}
:::

::: {#1866363004 .myid}
[]{#_Toc404798179}[]{#struct_0_x9962_12256_x613310848}[]{#_Toc385230690}[]{#_Toc367103741}[]{#_Toc363662134}

**FC和FCoE \-- FC Zone配置命令 \-- zone mode enhanced**

------------------------------------------------------------------------

[**[zone mode enhanced]{lang="EN-US"}**]{#struct_0_x9962_12256_x148778409}[命令用来配置当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[工作在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[undo zone mode enhanced]{lang="EN-US"}**]{#struct_0_x9962_12256_x337136055}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_537196759}

[**[zone mode enhanced]{lang="EN-US"}**]{#struct_0_x9962_12256_x1999607300}

[**[undo zone mode enhanced]{lang="EN-US"}**]{#struct_0_x9962_12256_1866868282}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x78270988}

[[当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x613245312}[工作在基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1733414964}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1654012887}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x687730622}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2023310602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_604448444}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2139050853}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1102084995}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x328726369}[有两种工作模式：基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式和增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式。当进行]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式切换时，将进行]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[内的扩散操作，以保证]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[内的所有交换机的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式的一致性。因此，只有当]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[中的所有交换机都支持增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式时，才允许配置为增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x613179776}[模式切换时未能成功在]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[内完成扩散，可能造成本交换机]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式切换成功但]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[内其它交换机]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式切换失败的情况。如果扩散失败，系统将打印日志信息，告知用户扩散失败。此时，需要用户主动激发一次完全扩散过程，以保证]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[内所有交换机的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式的一致性。]{style="font-family:宋体"}

[[当从增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1358889555}[模式切换为基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式时，若存在激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[，且激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[大小超过了基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下激活]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的最大规格，则切换失败，本交换机的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式不变。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_427119689}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1801397428}[配置]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[工作在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1445552879}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] zone mode enhanced]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1532975608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone status]{lang="EN-US"}**]{#struct_0_x9962_12256_x613114240}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset distribute]{lang="EN-US"}**]{#struct_0_x9962_12256_x971660159}
:::

::: {#675313307 .myid}
[]{#_Toc404798180}[]{#struct_0_x9962_12256_1153091353}[]{#_Toc308689032}

**FC和FCoE \-- FC Zone配置命令 \-- zone name**

------------------------------------------------------------------------

[**[zone name]{lang="EN-US"}**]{#struct_0_x9962_12256_x142626695}[命令用来创建]{style="font-family:宋体"}[Zone]{lang="EN-US"}[，并进入其视图。如果指定的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[已经创建，则该命令直接用来进入该]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[**[undo zone name]{lang="EN-US"}**]{#struct_0_x9962_12256_x623749643}[命令用来删除指定名称的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1023010063}

[**[zone name]{lang="EN-US"}**[ *zone-name*]{lang="EN-US"}]{#struct_0_x9962_12256_x154249134}

[**[undo zone name]{lang="EN-US"}**[ *zone-name*]{lang="EN-US"}]{#struct_0_x9962_12256_x2007034603}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x90069154}

[[不存在任何]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x233609661}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1485628598}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1025331399}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1257547927}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1101990865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_779009593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1202217738}

[*[zone-name]{lang="FR"}*]{#struct_0_x9962_12256_1918645891}[：]{style="font-family:宋体"}[Zone]{lang="FR"}[的]{style="font-family:
宋体"}[名称，]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2030082887}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_92402120}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007100139}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1606274804}[创建]{style="font-family:宋体"}[Zone z1]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_636614295}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone name z1]{lang="EN-US"}

[\[Sysname-vsan1-zone-z1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1036001055}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone]{lang="EN-US"}**]{#struct_0_x9962_12256_x1449156477}
:::

::: {#1175623243 .myid}
[]{#_Toc404798181}[]{#struct_0_x9962_12256_899056680}[]{#_Toc308689033}

**FC和FCoE \-- FC Zone配置命令 \-- zone rename**

------------------------------------------------------------------------

[**[zone rename]{lang="EN-US"}**]{#struct_0_x9962_12256_x1064281305}[命令用来修改]{style="font-family:宋体"}[Zone]{lang="EN-US"}[的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007558890}

[**[zone rename]{lang="EN-US"}**[ ]{lang="EN-US"}*[old-name new-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x1403851419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_77784036}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1821927141}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_194484264}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1074832996}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_975063236}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_339761466}

[*[old-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007624426}[：待重命名的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[*[new-name]{lang="EN-US"}*]{#struct_0_x9962_12256_1662285810}[：新的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_511053113}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_157515754}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1948687125}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2121204597}[创建]{style="font-family:宋体"}[Zone z1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x206282847}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone name z1]{lang="EN-US"}

[\[Sysname-vsan1-zone-z1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1700988806}[将]{style="font-family:宋体"}[z1]{lang="EN-US"}[重命名为]{style="font-family:宋体"}[z2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zone rename z1 z2]{lang="EN-US"}]{#struct_0_x9962_12256_x2007427818}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_985346976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone]{lang="EN-US"}**]{#struct_0_x9962_12256_1697280624}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone name]{lang="EN-US"}**]{#struct_0_x9962_12256_x993961748}
:::

::: {#515820651 .myid}
[]{#_Toc404798182}[]{#struct_0_x9962_12256_x38817301}[]{#_Toc308689034}

**FC和FCoE \-- FC Zone配置命令 \-- zone-alias clone**

------------------------------------------------------------------------

[**[zone-alias clone]{lang="EN-US"}**]{#struct_0_x9962_12256_327798733}[命令用来复制]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x625773976}

[**[zone-alias clone ]{lang="EN-US"}***[src-name dest-name]{lang="EN-US"}*]{#struct_0_x9962_12256_98066252}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007493354}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x935249184}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1658262054}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_17513505}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1747391831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x186599280}

[*[src-name]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x9962_12256_1038685334}[被复制的源]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[*[dest-name]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x9962_12256_x1237594673}[复制后的目的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_733065745}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x234382183}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007296746}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1415032410}[创建]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[za1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_991156905}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone-alias name za1 ]{lang="EN-US"}

[\[Sysname-vsan1-zone-alias-za1\] quit]{lang="EN-US"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_x545631516}[复制]{style="font-family:宋体"}[za1]{lang="EN-US"}[到]{style="font-family:宋体"}[za2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zone-alias clone za1 za2]{lang="EN-US"}]{#struct_0_x9962_12256_866682411}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x646823737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone-alias]{lang="EN-US"}**]{#struct_0_x9962_12256_x2007362282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone-alias name]{lang="EN-US"}**]{#struct_0_x9962_12256_x1489517192}
:::

::: {#514653341 .myid}
[]{#_Toc404798183}[]{#struct_0_x9962_12256_x631504406}[]{#_Toc308689035}

**FC和FCoE \-- FC Zone配置命令 \-- zone-alias name**

------------------------------------------------------------------------

[**[zone-alias name]{lang="EN-US"}**]{#struct_0_x9962_12256_2036535303}[命令用来创建]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名，并进入其视图。如果指定的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名已经创建，则该命令直接用来进入该]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的视图。]{style="font-family:宋体"}

[**[undo zone-alias name]{lang="EN-US"}**]{#struct_0_x9962_12256_x1060388426}[命令用来删除指定名称的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x460417412}

[**[zone-alias name ]{lang="PT-BR"}**]{#struct_0_x9962_12256_x522169984}*[zone-alias-name]{lang="PT-BR"}*

[**[undo zone-alias name]{lang="PT-BR"}**]{#struct_0_x9962_12256_x1443096001}[ ]{lang="PT-BR"}*[zone-alias-name]{lang="PT-BR"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x90069151}

[[不存在任何]{style="font-family:宋体"}]{#struct_0_x9962_12256_x233609666}[Zone]{lang="PT-BR"}[别名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007165674}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1772936254}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x893325436}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_922452888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1606879691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1524828881}

[*[zone-alias-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x1956194377}[：]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x429733669}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_280780618}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1485708010}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2007231210}[创建]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[za1]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1747534467}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone-alias name za1]{lang="EN-US"}

[\[Sysname-vsan1-zone-alias-za1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_574596185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone-alias]{lang="EN-US"}**]{#struct_0_x9962_12256_754886240}
:::

::: {#-2038691588 .myid}
[]{#_Toc404798184}[]{#struct_0_x9962_12256_x2121579999}[]{#_Toc308689036}

**FC和FCoE \-- FC Zone配置命令 \-- zone-alias rename**

------------------------------------------------------------------------

[**[zone-alias rename]{lang="EN-US"}**]{#struct_0_x9962_12256_1277101468}[命令用来修改]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2137931697}

[**[zone-alias rename]{lang="EN-US"}**[ ]{lang="EN-US"}*[old-name new-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007034602}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_80455343}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x180002191}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1320068409}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x636305799}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x717055167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1047449721}

[*[old-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007100138}[：待重命名的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[*[new-name]{lang="EN-US"}*]{#struct_0_x9962_12256_40190863}[：新的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1236302723}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x89632837}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1747443195}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x941633857}[创建]{style="font-family:宋体"}[Zone]{lang="EN-US"}[别名]{style="font-family:宋体"}[za1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_2727160}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone-alias name za1]{lang="EN-US"}

[\[Sysname-vsan1-zone-alias-za1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x898882623}[将]{style="font-family:宋体"}[za1]{lang="EN-US"}[重命名为]{style="font-family:宋体"}[za2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zone-alias rename za1 za2]{lang="EN-US"}]{#struct_0_x9962_12256_x1378075275}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007558893}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone-alias]{lang="EN-US"}**]{#struct_0_x9962_12256_162232522}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone-alias name]{lang="EN-US"}**]{#struct_0_x9962_12256_x201402833}
:::

::: {#528624224 .myid}
[]{#_Toc404798185}[]{#struct_0_x9962_12256_1698695213}[]{#_Toc308689037}

**FC和FCoE \-- FC Zone配置命令 \-- zoneset activate**

------------------------------------------------------------------------

[**[zoneset activate]{lang="EN-US"}**]{#struct_0_x9962_12256_x811944388}[命令用来激活指定]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[生成]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[，并发起向全网的扩散过程。]{style="font-family:宋体"}

[**[undo zoneset activate]{lang="EN-US"}**]{#struct_0_x9962_12256_x1894800010}[命令用来删除]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[，并发起向全网的扩散过程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1371217211}

[**[zoneset activate name ]{lang="EN-US"}***[zoneset-name]{lang="EN-US"}*]{#struct_0_x9962_12256_1478458447}

[**[undo zoneset activate]{lang="EN-US"}**]{#struct_0_x9962_12256_x2007624429}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1873166599}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x560191613}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x327314086}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1925304685}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x747059224}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1766118946}

[**[name ]{lang="EN-US"}**]{#struct_0_x9962_12256_x412713533}*[zoneset-name]{lang="DE"}*[：]{style="font-family:宋体"}[被激活的]{style="font-family:宋体"}[Zone set]{lang="DE"}[的]{style="font-family:宋体"}[名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。指定的]{style="font-family:宋体"}[Zone ]{lang="EN-US"}[set]{lang="DE"}[必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007427821}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1895865159}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[虽然每个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2099570131}[内可以配置多个]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[，但只有一个可以生效，称为]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[。最终]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[成员的访问控制都在]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[内进行匹配。]{style="font-family:宋体"}

[[Active Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x359706043}[需要通过命令显式地在本地交换机上激活，并向整个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[进行同步，使其在全网范围内保持一致。如果扩散失败，系统将打印日志信息，告知用户扩散失败。此时需要用户重新激活该]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[，以保证]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[内所有交换机的]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[数据的一致性。]{style="font-family:宋体"}

[[在将]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x1461438714}[进行全网扩散时，交换机会根据]{style="font-family:宋体"}**[zoneset distribute full]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[扩散类型来决定扩散时是否携带数据库信息。]{style="font-family:宋体"}

[[被激活的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x576052925}[中至少要包含一个]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[[同一]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2100761902}[内只能够存在一个]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_952576489}[模式下，若]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[超过了最大规格，则激活失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_507354989}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_632031982}[创建]{style="font-family:宋体"}[Zone z1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x2007493357}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zone name z1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_630834757}[添加]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[为]{style="font-family:宋体"}[z1]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zone-z1\] member fcid 010000]{lang="EN-US"}]{#struct_0_x9962_12256_1679647640}

[\[Sysname-vsan1-zone-z1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_2054585287}[创建]{style="font-family:宋体"}[Zone set zs1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zoneset name zs1]{lang="EN-US"}]{#struct_0_x9962_12256_x429665884}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1285577775}[添加]{style="font-family:宋体"}[z1]{lang="EN-US"}[为]{style="font-family:宋体"}[zs1]{lang="EN-US"}[的成员。]{style="font-family:宋体"}

[[\[Sysname-vsan1-zoneset-zs1\] member z1]{lang="EN-US"}]{#struct_0_x9962_12256_x2007296749}

[\[Sysname-vsan1-zoneset-zs1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_151051531}[激活]{style="font-family:宋体"}[zs1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zoneset activate name zs1]{lang="EN-US"}]{#struct_0_x9962_12256_1810981457}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2072743784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zoneset active]{lang="EN-US"}**]{#struct_0_x9962_12256_560635130}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset distribute full]{lang="EN-US"}**]{#struct_0_x9962_12256_992249763}
:::

::: {#-877437114 .myid}
[]{#_Toc404798186}[]{#struct_0_x9962_12256_927718506}[]{#_Toc308689038}

**FC和FCoE \-- FC Zone配置命令 \-- zoneset clone**

------------------------------------------------------------------------

[**[zoneset clone]{lang="EN-US"}**]{#struct_0_x9962_12256_x2007362285}[命令用来复制]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1086232665}

[**[zoneset clone ]{lang="EN-US"}***[src-name dest-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007408693}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x817097905}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_489375316}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1373706688}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1312979636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1927292203}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x797299709}

[*[src-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007165677}[：被复制的源]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[*[dest-name]{lang="DE"}*]{#struct_0_x9962_12256_x2118746515}[：]{style="font-family:宋体"}[复制后的目的]{style="font-family:宋体"}[Zone set]{lang="DE"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_733131281}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_535815275}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_325914272}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_x1659030724}[创建]{style="font-family:宋体"}[Zone set zs1]{lang="DE"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x9962_12256_864201717}

[\[Sysname\] vsan 1]{lang="DE"}

[\[Sysname-vsan1\] zoneset name zs1]{lang="DE"}

[\[Sysname-vsan1-zoneset-zs1\] quit]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x9962_12256_307631708}[复制]{style="font-family:宋体"}[zs1]{lang="EN-US"}[到]{style="font-family:宋体"}[zs2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zoneset clone zs1 zs2]{lang="EN-US"}]{#struct_0_x9962_12256_x2007231213}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2144148302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zoneset]{lang="EN-US"}**]{#struct_0_x9962_12256_1519442892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset name]{lang="EN-US"}**]{#struct_0_x9962_12256_x1471210637}
:::

::: {#1937016784 .myid}
[]{#_Toc404798187}[]{#struct_0_x9962_12256_x1410673817}[]{#_Toc308689039}

**FC和FCoE \-- FC Zone配置命令 \-- zoneset distribute**

------------------------------------------------------------------------

[**[zoneset distribute]{lang="EN-US"}**]{#struct_0_x9962_12256_x1043511983}[命令用来激发完全扩散过程，扩散的内容包括]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[以及数据库。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x55945125}

[**[zoneset distribute]{lang="EN-US"}**]{#struct_0_x9962_12256_x459178510}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x650996001}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2007034605}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x679059544}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x217847773}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1437747129}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x149244181}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1136415808}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[配置该命令会触发一次]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_x52553984}[数据扩散流程，且为完全扩散，即将]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[和数据库均携带在报文中进行扩散。]{style="font-family:宋体"}

[[使用激活命令]{style="font-family:宋体"}**[zoneset activate]{lang="EN-US"}**]{#struct_0_x9962_12256_487669304}[激活一个]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[成为]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[后，用户可以继续修改数据库的配置，本命令可以在不改变]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[的同时将]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[以及修改后的数据库向全网扩散。]{style="font-family:宋体"}

[[如果扩散失败，系统将打印日志信息，告知用户扩散失败。此时需要用户重新激发一次完全扩散，以保证]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_952904169}[内所有交换机的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[数据的一致性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x333146783}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2007100141}[激发完全扩散过程。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1250372124}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zoneset distribute]{lang="EN-US"}
:::

::: {#682007666 .myid}
[]{#_Toc404798188}[]{#struct_0_x9962_12256_1220885504}[]{#_Toc308689040}

**FC和FCoE \-- FC Zone配置命令 \-- zoneset distribute full**

------------------------------------------------------------------------

[**[zoneset distribute full]{lang="EN-US"}**]{#struct_0_x9962_12256_989713671}[命令用来配置扩散和合并类型为完全扩散和完全合并。]{style="font-family:宋体"}

[**[undo zoneset distribute full]{lang="EN-US"}**]{#struct_0_x9962_12256_x1221304371}[命令用来恢复扩散和合并类型为非完全扩散和非完全合并。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1238710314}

[**[zoneset distribute full]{lang="EN-US"}**]{#struct_0_x9962_12256_x605547333}

[**[undo zoneset distribute full]{lang="EN-US"}**]{#struct_0_x9962_12256_x2004988140}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007558892}

[[基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1728316463}[模式下，扩散和合并类型为非完全扩散和非完全合并。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1998370098}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1880333635}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x887713847}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1396649874}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x329071658}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x945851126}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_329846754}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[完全扩散和完全合并会将]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x2007624428}[以及数据库都进行扩散和合并；非完全扩散和非完全合并仅将]{style="font-family:宋体"}[Active Zone set]{lang="EN-US"}[进行扩散和合并。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_855716756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只允许在基本]{style="font-family:宋体"}]{#struct_0_x9962_12256_952445418}[Zone]{lang="EN-US"}[模式下配置。在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下，扩散和合并类型固定为完全扩散和完全合并，因此不支持本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基本]{style="font-family:宋体"}]{#struct_0_x9962_12256_565120641}[Zone]{lang="EN-US"}[模式下，]{style="font-family:宋体"}[扩散类型仅会对使用]{lang="EN-US" style="font-family:宋体"}**[zoneset activate]{lang="EN-US"}**[命令激发的扩散过程产生影响，对使用]{lang="EN-US" style="font-family:宋体"}**[zoneset distrbute]{lang="EN-US"}**[命令激发的扩散不会产生影响。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基本]{style="font-family:宋体"}]{#struct_0_x9962_12256_588404909}[Zone]{lang="EN-US"}[模式下，合并类型会对所有合并过程产生影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1111963192}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x606820810}[配置扩散和合并类型为完全扩散和完全合并。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1695354394}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zoneset distribute full]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007427820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zone status]{lang="EN-US"}**]{#struct_0_x9962_12256_629313224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset activate]{lang="EN-US"}**]{#struct_0_x9962_12256_x1614982763}
:::

::: {#1957829260 .myid}
[]{#_Toc404798189}[]{#struct_0_x9962_12256_x1217385199}[]{#_Toc308689041}

**FC和FCoE \-- FC Zone配置命令 \-- zoneset name**

------------------------------------------------------------------------

[**[zoneset name]{lang="EN-US"}**]{#struct_0_x9962_12256_x257961006}[命令用来创建]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[，并进入其视图。如果指定的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[已经创建，则该命令直接用来进入该]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[**[undo zoneset name]{lang="EN-US"}**]{#struct_0_x9962_12256_x1095139757}[命令用来删除指定名称的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1957541727}

[**[zoneset name ]{lang="EN-US"}***[zoneset-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2041865286}

[**[undo zoneset name ]{lang="EN-US"}***[zoneset-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007493356}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1477420893}

[[不存在任何]{style="font-family:宋体"}[Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_x1556466550}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2098048598}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1093147174}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_450874668}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_382007417}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x326936341}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1170479235}

[*[zoneset-name]{lang="EN-US"}*[:Zone set]{lang="EN-US"}]{#struct_0_x9962_12256_518265617}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1895930695}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1982158735}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1259294827}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2007296748}[创建]{style="font-family:宋体"}[Zone set zs1]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1717135472}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zoneset name zs1]{lang="EN-US"}

[\[Sysname-vsan1-zoneset-zs1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_529359579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zoneset]{lang="EN-US"}**]{#struct_0_x9962_12256_1843897816}
:::

::: {#-844114536 .myid}
[]{#_Toc404798190}[]{#struct_0_x9962_12256_x1828193338}[]{#_Toc308689042}

**FC和FCoE \-- FC Zone配置命令 \-- zoneset rename**

------------------------------------------------------------------------

[[ **zoneset rename**]{lang="EN-US"}]{#struct_0_x9962_12256_617112571}[命令用来修改]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1657631985}

[**[zoneset rename]{lang="EN-US"}**[ ]{lang="EN-US"}*[old-name new-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2007362284}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1642650690}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1646247012}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_102498733}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1085227491}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1143020007}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x263830570}

[*[old-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x2055069243}[：待重命名的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[*[new-name]{lang="EN-US"}*]{#struct_0_x9962_12256_x764313388}[：新的]{style="font-family:宋体"}[Zone set]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：]{style="font-family:宋体"}[\$-\^\_]{lang="EN-US"}[，并且名称的起始字符只能为大小写英文字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_376900921}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1388111091}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2007165676}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_610136840}[创建]{style="font-family:宋体"}[Zone set zs1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x387143014}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] zoneset name zs1]{lang="EN-US"}

[\[Sysname-vsan1-zoneset-zs1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_523096013}[将]{style="font-family:宋体"}[zs1]{lang="EN-US"}[重命名为]{style="font-family:宋体"}[zs2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-vsan1\] zoneset rename zs1 zs2]{lang="EN-US"}]{#struct_0_x9962_12256_x1630338289}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x639510457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display zoneset]{lang="EN-US"}**]{#struct_0_x9962_12256_1466360438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zoneset name]{lang="EN-US"}**]{#struct_0_x9962_12256_x2007231212}
:::

::: {#123239425 .myid}
[]{#_Toc404798192}[]{#struct_0_x9962_12256_x4580915}

**FC和FCoE \-- NPV配置命令 \-- display fc nport**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fc** **nport**]{lang="EN-US"}]{#struct_0_x9962_12256_28811053}[命令用来显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机向]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机进行注册的信息以及获取到的管理地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1208725082}

[**[display]{lang="EN-US"}**[ **fc** **nport** \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1476946568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1560678524}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_152771}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_683668292}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x527442012}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1435626126}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1995625567}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x311516885}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_816757692}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_x1640355660}[：显示从指定接口获取到的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机管理地址，]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type*]{lang="EN-US"}[只能是]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口或]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口，且只能指定]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式的接口。如果未指定本参数，将显示从所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口和]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口获取到的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机管理地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2019982058}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1561503026}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[本命令可以显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1507348229}[交换机通过]{style="font-family:宋体"}[up]{lang="EN-US"}[的]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式接口，向]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机发送的注册信息，以及从]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机获取到的管理地址。]{style="font-family:宋体"}

[[需要注意的是，只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1329742266}[交换机向]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机成功注册后，才能显示相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1656902363}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_69246304}[显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机向]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机进行注册的信息以及获取到的管理地址。]{style="font-family:宋体"}

[[\<Sysname\> display fc nport]{lang="EN-US"}]{#struct_0_x9962_12256_78914360}

[NP port: FC1/0/5]{lang="EN-US"}

[  Port-WWN: 20:00:00:41:22:a8:00:05]{lang="EN-US"}

[  FC4-types(FC4_features): NPV]{lang="EN-US"}

[  Symbolic-node-name: NPV-Sysname]{lang="EN-US"}

[  Symbolic-port-name: NPV-Sysname:FC1/0/5]{lang="EN-US"}

[  Node-IP-addr: 192.168.0.153]{lang="EN-US"}

[  Peer management address: snmp://192.168.0.151]{lang="EN-US"}

[                           snmp://192.168.0.152]{lang="EN-US"}

[ ]{lang="EN-US"}

[NP port: Vfc2]{lang="EN-US"}

[  Port-WWN: 20:00:00:49:c9:28:c7:01]{lang="EN-US"}

[  FC4-types(FC4_features): NPV]{lang="EN-US"}

[  Symbolic-node-name: NPV-Sysname]{lang="EN-US"}

[  Symbolic-port-name: NPV-Sysname:Vfc2]{lang="EN-US"}

[  Node-IP-addr: 192.168.0.153]{lang="EN-US"}

[  Peer management address: snmp://192.168.0.151]{lang="EN-US"}

[                           snmp://192.168.0.152]{lang="EN-US"}

[[表1-45 ]{lang="EN-US"}[display fc nport]{lang="EN-US"}]{#struct_0_x9962_12256_577253724}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1067895053}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_673540978}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1167380329}

[[NP port]{lang="EN-US"}]{#struct_0_x9962_12256_x1047182764}

[[NP]{lang="EN-US"}]{#struct_0_x9962_12256_1214516257}[模式接口的名称]{style="font-family:宋体"}

[[Port-WWN]{lang="EN-US"}]{#struct_0_x9962_12256_398703612}

[[NP]{lang="EN-US"}]{#struct_0_x9962_12256_x1583720412}[模式接口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[FC4-types(FC4 features)]{lang="EN-US"}]{#struct_0_x9962_12256_x1316840067}

[[NP]{lang="EN-US"}]{#struct_0_x9962_12256_x1973949383}[模式接口固定注册]{style="font-family:宋体"}[FC4]{lang="EN-US"}[类型为]{style="font-family:宋体"}[NPV]{lang="EN-US"}[，无]{style="font-family:宋体"}[FC4]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Symbolic-node-name]{lang="EN-US"}]{#struct_0_x9962_12256_x905066290}

[[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1694377557}[节点的符号名称，用于描述此节点。]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式接口会携带本机系统名，注册形如]{style="font-family:宋体"}*[system-name]{lang="EN-US"}*[的字符串作为节点描述名]{style="font-family:宋体"}

[[Symbolic-port-name]{lang="EN-US"}]{#struct_0_x9962_12256_x407865442}

[[NP]{lang="EN-US"}]{#struct_0_x9962_12256_755710185}[模式接口的符号名称，用于描述此端口。]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式接口会携带本机系统名和端口名，注册形如]{style="font-family:宋体"}*[system-name]{lang="EN-US"}*[:*port-name*]{lang="EN-US"}[的字符串作为端口描述名]{style="font-family:宋体"}

[[Node-IP-addr]{lang="EN-US"}]{#struct_0_x9962_12256_83269331}

[[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1158218499}[交换机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Peer management address]{lang="EN-US"}]{#struct_0_x9962_12256_970115618}

[[NP]{lang="EN-US"}]{#struct_0_x9962_12256_x1589236976}[模式接口获取到的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机管理地址列表。例如：]{style="font-family:宋体"}[snmp://192.168.6.151]{lang="EN-US"}[，表示管理协议为]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[，管理地址为]{style="font-family:宋体"}[192.168.6.151]{lang="EN-US"}[。显示为空表示]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机上未配置管理地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#94464183 .myid}
[]{#_Toc404798193}[]{#struct_0_x9962_12256_x1488614378}[]{#_Toc310344706}[]{#_Toc309822323}

**FC和FCoE \-- NPV配置命令 \-- display npv login**

------------------------------------------------------------------------

[**[display npv login]{lang="EN-US"}**]{#struct_0_x9962_12256_51856999}[命令用来显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的下行口上相连的节点设备的注册信息和映射的上行口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1423587066}

[**[display npv login]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \] \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1480638108}

[**[display npv login]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \] **count**]{lang="EN-US"}]{#struct_0_x9962_12256_x595078568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2082045850}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x2007034604}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_887024397}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x355286164}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x388221377}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x851724068}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x856088514}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_674797180}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x215770222}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的下行口上相连的节点设备的注册信息和映射的上行口，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息。在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机上，只能显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_x2007100140}[：显示指定下行口上相连的节点设备的注册信息和映射的上行口。不指定该参数时，将显示所有下行口的信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x9962_12256_x315711817}[：显示登录节点的数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1755471398}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_467447802}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x325354575}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_537144978}[显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的下行口上相连的节点设备的注册信息和映射的上行口。]{style="font-family:宋体"}

[[\<Sysname\> display npv login]{lang="EN-US"}]{#struct_0_x9962_12256_x1162605812}

[Server                                                                  External]{lang="EN-US"}

[Interface VSAN FCID     Node WWN                Port WWN                Interface]{lang="EN-US"}

[Fc1/0/2   1    0xae0002 20:00:00:23:89:c9:fc:05 20:00:00:23:89:c9:fc:05 Fc1/0/1]{lang="EN-US"}

[Vfc3      1    0xae0003 10:00:00:00:c9:66:6b:60 20:00:00:00:c9:66:6b:60 Fc1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_371451098}[显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机上]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[的登录节点的数目。]{style="font-family:宋体"}

[[\<Sysname\> display npv login vsan 1 count]{lang="EN-US"}]{#struct_0_x9962_12256_1460075775}

[Total entries: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1856337028}[显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机上所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的登录节点的数目。]{style="font-family:宋体"}

[[\<Sysname\> display npv login count]{lang="EN-US"}]{#struct_0_x9962_12256_x427100935}

[VSAN        Entries]{lang="EN-US"}

[1           2]{lang="EN-US"}

[2           1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries: 3]{lang="EN-US"}

[[表1-46 ]{lang="EN-US"}[display npv login]{lang="EN-US"}]{#struct_0_x9962_12256_275880664}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1121196105}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_613702529}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_713076888}

[[Server Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x914186336}

[[下行口的接口名]{style="font-family:宋体"}]{#struct_0_x9962_12256_371516634}

[[External interface]{lang="EN-US"}]{#struct_0_x9962_12256_630449589}

[[下行口映射的上行口的接口名]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1154855695}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1497538951}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x852184273}[编号]{style="font-family:宋体"}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_371320026}

[[节点的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_786824286}[地址]{style="font-family:宋体"}

[[Node WWN]{lang="EN-US"}]{#struct_0_x9962_12256_170357962}

[[节点的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x977453893}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1103879360}

[[节点端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x966142581}

[[Entries]{lang="EN-US"}]{#struct_0_x9962_12256_1856271492}

[[某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1856730244}[内登录节点的数目]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_x9962_12256_1137400073}

[[登录节点的总数目]{style="font-family:宋体"}]{#struct_0_x9962_12256_1853691028}

[ ]{lang="EN-US"}

::: {#-1564138801 .myid}
[]{#_Toc404798194}[]{#struct_0_x9962_12256_x964644814}[]{#_Toc310344707}[]{#_Toc309822326}

**FC和FCoE \-- NPV配置命令 \-- display npv status**

------------------------------------------------------------------------

[**[display npv status]{lang="EN-US"}**]{#struct_0_x9962_12256_218231793}[命令用来显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1827485664}

[**[display npv status]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1726876440}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371713242}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x229239989}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x802416095}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1386732191}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x670265900}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x97689683}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1317093722}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x359388307}

[**[vsan]{lang="EN-US"}**[ ]{lang="EN-US"}*[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_371778778}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的状态信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的状态信息。在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机上，只能显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的状态信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_965243224}

[[使用本命令可以查询到]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x743679750}[交换机上各个接口在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的状态信息，包括接口]{style="font-family:宋体"}[VSAN Tag]{lang="EN-US"}[模式、接口在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的状态、]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址等。]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_415247111}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x148005896}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_2014294672}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[的]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display npv status vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_371582170}

[External Interfaces:]{lang="EN-US"}

[  Interface: Fc1/0/2  VSAN tagging mode: Tagging]{lang="EN-US"}

[    VSAN  State  FCID]{lang="EN-US"}

[    1     Up     0x010002]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: Fc1/0/3  VSAN tagging mode: Non tagging]{lang="EN-US"}

[    VSAN  State  FCID]{lang="EN-US"}

[    1     Up     0x010001]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Number of External Interfaces: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Server Interfaces:]{lang="EN-US"}

[  Interface: Fc1/0/5  VSAN tagging mode: Tagging]{lang="EN-US"}

[    VSAN  State]{lang="EN-US"}

[    1     Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Number of Server Interfaces: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1807058591}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display npv status]{lang="EN-US"}]{#struct_0_x9962_12256_371647706}

[External Interfaces:]{lang="EN-US"}

[  Interface: Fc1/0/1  VSAN tagging mode: Non tagging]{lang="EN-US"}

[    VSAN  State  FCID]{lang="EN-US"}

[    2     Up     0x010003]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: Fc1/0/2  VSAN tagging mode: Tagging]{lang="EN-US"}

[    VSAN  State  FCID]{lang="EN-US"}

[    1     Up     0x010002]{lang="EN-US"}

[    2     Up     0x010003(Unavailable)]{lang="EN-US"}

[    5     Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: Fc1/0/3  VSAN tagging mode: Non tagging]{lang="EN-US"}

[    VSAN  State  FCID]{lang="EN-US"}

[    1     Up     0x010001]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Number of External Interfaces: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[Server Interfaces:]{lang="EN-US"}

[  Interface: Fc1/0/4  VSAN tagging mode: Non tagging]{lang="EN-US"}

[    VSAN  State]{lang="EN-US"}

[    2     Up]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface: Fc1/0/5  VSAN tagging mode: Tagging]{lang="EN-US"}

[    VSAN  State]{lang="EN-US"}

[    1     Down]{lang="EN-US"}

[    2     Up]{lang="EN-US"}

[    3     Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Number of Server Interfaces: 2]{lang="EN-US"}

[[表1-47 ]{lang="EN-US"}[display npv status]{lang="EN-US"}]{#struct_0_x9962_12256_x660508221}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1122063637}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1735687246}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1960556291}

[[External Interfaces]{lang="EN-US"}]{#struct_0_x9962_12256_371975386}

[[上行口列表]{style="font-family:宋体"}]{#struct_0_x9962_12256_x70344966}

[[Server Interfaces]{lang="EN-US"}]{#struct_0_x9962_12256_x970978598}

[[下行口列表]{style="font-family:宋体"}]{#struct_0_x9962_12256_1414225429}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1366123318}

[[接口名]{style="font-family:宋体"}]{#struct_0_x9962_12256_372040922}

[[VSAN tagging mode]{lang="EN-US"}]{#struct_0_x9962_12256_1233864018}

[[VSAN Tag]{lang="EN-US"}]{#struct_0_x9962_12256_x944160346}[模式]{style="font-family:宋体"}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1663504583}

[[VSAN ID]{lang="EN-US"}]{#struct_0_x9962_12256_x17160804}

[[State]{lang="EN-US"}]{#struct_0_x9962_12256_371451099}

[[当前接口的]{style="font-family:宋体"}[Up/Down]{lang="EN-US"}]{#struct_0_x9962_12256_1460075774}[状态]{style="font-family:宋体"}

[[FCID]{lang="EN-US"}]{#struct_0_x9962_12256_275815128}

[[上行口]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x9962_12256_2127078299}[后，会显示核心交换机为之分配的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址；下行口没有]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[（在一个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_513461296}[内，如果]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机同时接入两个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络，并且这两个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络为上行口分配了相同的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[，那么其中一个上行口虽然可以]{style="font-family:宋体"}[Up]{lang="EN-US"}[，但并不能作为上行口工作，此时会在括号中显示]{style="font-family:宋体"}[Unavailable]{lang="EN-US"}[）]{style="font-family:宋体"}

[[![说明](FC和FCoE命令.files/image002.png){#图片 11 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x9962_12256_371516635}

[[FC SAN]{lang="EN-US"}]{#struct_0_x9962_12256_630449588}[中可能存在多个]{style="font-family:KaiTi_GB2312"}[Fabric]{lang="EN-US"}[网络，比如]{style="font-family:KaiTi_GB2312"}[FC SAN]{lang="EN-US"}[中有两台]{style="font-family:KaiTi_GB2312"}[FC]{lang="EN-US"}[交换机，但这两台]{style="font-family:KaiTi_GB2312"}[FC]{lang="EN-US"}[交换机之间并没有连接，那么每台]{style="font-family:KaiTi_GB2312"}[FC]{lang="EN-US"}[交换机都自成一个]{style="font-family:KaiTi_GB2312"}[Fabric]{lang="EN-US"}[网络。]{style="font-family:KaiTi_GB2312"}

[[Number of External Interfaces]{lang="EN-US"}]{#struct_0_x9962_12256_x1154855696}

[[上行口的数量]{style="font-family:宋体"}]{#struct_0_x9962_12256_1900823478}

[[Number of Server Interfaces]{lang="EN-US"}]{#struct_0_x9962_12256_371320027}

[[下行口的数量]{style="font-family:宋体"}]{#struct_0_x9962_12256_786824287}

[ ]{lang="EN-US"}

::: {#-1359112933 .myid}
[]{#_Toc404798195}[]{#struct_0_x9962_12256_x1103879361}[]{#_Toc310344708}[]{#_Toc309822325}

**FC和FCoE \-- NPV配置命令 \-- display npv traffic-map**

------------------------------------------------------------------------

[**[display npv traffic-map]{lang="EN-US"}**]{#struct_0_x9962_12256_599941360}[命令用来显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机上的流量映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1510795868}

[**[display]{lang="EN-US"}**[ **npv** **traffic-map** \[ **vsan** *vsan-id* \] \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1691458930}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_477594994}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_371385563}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1137400074}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1854018708}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_14010857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2134549708}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_389816903}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2114664092}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x889271477}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的流量映射信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的流量映射信息。在]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机上，只能显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的流量映射信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_x1940932388}[：显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机上指定下行口的]{style="font-family:宋体"}[流量映射信息。不指定该参数时，将显示]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机上所有下行口的流量映射信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371713243}

[[使用本命令可以查询到]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x229239990}[交换机上的流量映射信息，即下行口到上行口的映射关系。]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x801957344}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1627631724}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1943090972}[显示流量映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display npv traffic-map]{lang="EN-US"}]{#struct_0_x9962_12256_673792987}

[NPV traffic map information of VSAN 1:]{lang="EN-US"}

[Server interface       External interface]{lang="EN-US"}

[Fc1/0/1                Fc1/0/3]{lang="EN-US"}

[Fc1/0/2                Fc1/0/3]{lang="EN-US"}

[Vfc1                   Fc1/0/4]{lang="EN-US"}

[[表1-48 ]{lang="EN-US"}[display npv traffic-map]{lang="EN-US"}]{#struct_0_x9962_12256_371778779}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1119386449}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_965243223}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x743679743}

[[NPV traffic map information of VSAN 1]{lang="EN-US"}]{#struct_0_x9962_12256_415312646}

[[VSAN 1]{lang="EN-US"}]{#struct_0_x9962_12256_x1686678519}[内上下行口映射信息]{style="font-family:宋体"}

[[Server interface]{lang="EN-US"}]{#struct_0_x9962_12256_x1112559702}

[[下行口]{style="font-family:宋体"}]{#struct_0_x9962_12256_371582171}

[[External interface]{lang="EN-US"}]{#struct_0_x9962_12256_1807058592}

[[上行口]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1211905863}

[ ]{lang="EN-US"}

::: {#1042892433 .myid}
[]{#_Toc404798196}[]{#struct_0_x9962_12256_x832821588}[]{#_Toc393700663}[]{#_Toc393294215}

**FC和FCoE \-- NPV配置命令 \-- npv auto-load-balance enable**

------------------------------------------------------------------------

[**[npv auto-load-balance enable]{lang="EN-US"}**]{#struct_0_x9962_12256_80703108}[命令用来开启自动负载均衡功能。]{style="font-family:宋体"}

[**[undo npv auto-load-balance enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x2020202988}[命令用来关闭自动负载均衡功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_25117310}

[**[npv auto-load-balance enable]{lang="EN-US"}**]{#struct_0_x9962_12256_x1603764115}

[**[undo npv auto-load-balance enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1896061767}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1062265880}

[[自动负载均衡功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1907451123}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_252770406}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x2064427815}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1399937681}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1563660189}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_185284912}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_917591112}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1943115934}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[自动负载均衡的过程如下：当系统在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1059907045}[内检测到]{style="font-family:宋体"}[up]{lang="EN-US"}[的上行口时，会自动创建一个延迟定时器（可通过]{style="font-family:宋体"}**[npv auto-load-balance-interval]{lang="EN-US"}**[命令配置），待定时器超时后，系统将自动进行一次负载均衡。如果在定时器超时前又有新的上行口]{style="font-family:宋体"}[up]{lang="EN-US"}[，则重置该定时器。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9962_12256_457175985}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启了自动负载均衡功能后，上行口的]{style="font-family:宋体"}]{#struct_0_x9962_12256_x115865862}[up]{lang="EN-US"}[可能引起负载均衡的发生，从而可能导致流量中断。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭了自动负载均衡功能后，不会影响现有的上下行口映射关系。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x68538128}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1695922491}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x484741546}[配置]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内开启自动负载均衡功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x490096220}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] npv auto-load-balance enable]{lang="EN-US"}
:::

::: {#234920581 .myid}
[]{#_Toc404798197}[]{#struct_0_x9962_12256_x506589575}[]{#_Toc393700664}[]{#_Toc393294216}

**FC和FCoE \-- NPV配置命令 \-- npv auto-load-balance-interval**

------------------------------------------------------------------------

[**[npv auto-load-balance-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_377031993}[命令用来配置自动负载均衡的延迟时间。]{style="font-family:
宋体"}

[**[undo auto-load-balance-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_1287393969}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x103546120}

[**[npv auto-load-balance-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x9962_12256_x887956873}

[**[undo auto-load-balance-interval]{lang="EN-US"}**]{#struct_0_x9962_12256_x1808322944}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_862707772}

[[自动负载均衡的延迟时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x9962_12256_x1576216369}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x600496132}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1784554854}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1437941661}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1995555466}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_913981230}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1653021921}

[*[interval]{lang="EN-US"}*]{#struct_0_x9962_12256_x1480216457}[：自动负载均衡的延迟时间，单位为秒，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_280577955}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1521930048}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[自动负载均衡的延迟时间主要用来缓冲上行口的]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x9962_12256_2099476414}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[而引起震荡，以减少对自动负载均衡的影响。如果上行口的链路状况良好，可适当将减小延迟时间；否则，需增大延迟时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1586050535}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_733327889}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内配置自动负载均衡的延迟时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1351730}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] npv auto-load-balance-interval 20]{lang="EN-US"}
:::

::: {#-795873861 .myid}
[]{#_Toc404798198}[]{#struct_0_x9962_12256_44125933}[]{#_Toc310344709}[]{#_Toc309822327}

**FC和FCoE \-- NPV配置命令 \-- npv load-balance disruptive**

------------------------------------------------------------------------

[**[npv load-balance disruptive]{lang="EN-US"}**]{#struct_0_x9962_12256_x555968777}[命令用来发起一次中断负载均衡过程。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_195663810}

[**[npv load-balance disruptive]{lang="EN-US"}**]{#struct_0_x9962_12256_371647707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x660508220}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1735752782}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1115880951}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2016934880}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x998720094}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_708912721}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_1136612416}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[当某]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x129188961}[内各个接口负载不均衡时，可以使用本命令在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内发起一次中断负载均衡过程，强制该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的所有下行节点重新登录。发起中断负载均衡过程后，系统会重新进行上下行口的负载均衡分配，以达到更好的负载均衡效果，但会破坏已经稳定的上下行口的映射关系，从而导致流量中断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x70344967}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x970978597}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内发起一次中断负载均衡过程。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1414290965}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] npv load-balance disruptive]{lang="EN-US"}
:::

::: {#-1383283909 .myid}
[]{#_Toc404798199}[]{#struct_0_x9962_12256_1798899049}[]{#_Toc310344710}[]{#_Toc309822324}

**FC和FCoE \-- NPV配置命令 \-- npv traffic-map**

------------------------------------------------------------------------

[**[npv traffic-map]{lang="EN-US"}**]{#struct_0_x9962_12256_1001406005}[命令用来配置上下行口的映射关系。]{style="font-family:宋体"}

[**[undo npv traffic-map]{lang="EN-US"}**]{#struct_0_x9962_12256_1401556124}[命令用来删除配置的上下行口的映射关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1216410501}

[**[npv]{lang="EN-US"}**[ **traffic-map** **server-interface** *interface-type* *interface-number* **external-interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_372040923}

[**[undo]{lang="EN-US"}**[ **npv** **traffic-map** **server-interface** *interface-type* *interface-number* **external-interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_1233864019}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x944225882}

[[上下行口之间不存在映射关系。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1410485549}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x298785461}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x908884969}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1237859248}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x235970283}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_371451096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1460075785}

[**[server-interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_275880651}[：指定下行口。可以是]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口或者]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[external-interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_x960275580}[：指定上行口。可以是]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口或者]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1226532769}

[[只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_330043362}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[在进行下行口到上行口的映射时，如果该下行口有配置到上行口的映射关系，则该下行口只能从配置的上行口中选择一个有效接口进行映射，如果没有配置映射关系则可以从属于同一]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_188161133}[的所有上行口中选择一个有效接口进行映射。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_787290286}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_371516632}[在]{style="font-family:宋体"}[VSAN10]{lang="EN-US"}[内配置接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[到]{style="font-family:宋体"}[FC1/0/2]{lang="EN-US"}[的映射关系，其中]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[作为下行口，]{style="font-family:宋体"}[FC1/0/2]{lang="EN-US"}[作为上行口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_630449591}

[\[Sysname\] vsan 10]{lang="EN-US"}

[\[Sysname-vsan10\] npv traffic-map server-interface fc 1/0/1 external-interface fc 1/0/2]{lang="EN-US"}
:::

::: {#39923312 .myid}
[]{#_Toc404798201}[]{#struct_0_x9962_12256_x1480190293}

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping enode**

------------------------------------------------------------------------

[**[display fip-snooping enode]{lang="EN-US"}**]{#struct_0_x9962_12256_x1480059221}[命令用来显示]{style="font-family:
宋体"}[Transit]{lang="EN-US"}[交换机获取到的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1480452437}

[**[display fip-snooping enode]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1479928150}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1479797078}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1480190294}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1480059222}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1480452438}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1479928151}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1479731543}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1480124759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1479993687}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1480386903}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1249020745}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1249151817}[显示]{style="font-family:宋体"}[Transit]{lang="EN-US"}[交换机获取到的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display fip-snooping enode]{lang="EN-US"}]{#struct_0_x9962_12256_1248889672}

[VLAN 2:]{lang="EN-US"}

[Interface   ENode WWN                ENode MAC]{lang="EN-US"}

[XGE1/0/1    21:01:00:1b:32:a0:fa:18  000c-2999-eacd]{lang="EN-US"}

[[表1-49 ]{lang="EN-US"}[display fip-snooping enode]{lang="EN-US"}]{#struct_0_x9962_12256_1248496456}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1603718737}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1249151815}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1248889671}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_1249020742}

[[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_1248758598}[的信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1248496454}

[[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_1249151813}[交换机上连接]{style="font-family:宋体"}[ENode]{lang="EN-US"}[的以太网接口]{style="font-family:宋体"}

[[ENode WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1248430917}

[[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_1249086276}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[ENode MAC]{lang="EN-US"}]{#struct_0_x9962_12256_1248824132}

[[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_1296009376}[的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-794181718 .myid}
[]{#_Toc404798202}[]{#struct_0_x9962_12256_1296140448}

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping fcf**

------------------------------------------------------------------------

[**[display fip-snooping fcf]{lang="EN-US"}**]{#struct_0_x9962_12256_1295747232}[命令用来显示]{style="font-family:
宋体"}[Transit]{lang="EN-US"}[交换机获取到的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1295943840}

[**[display fip-snooping fcf]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1295550624}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1296074911}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1296205983}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1295812767}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1295943839}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1295550623}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1296074910}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1296205982}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1295878302}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1295485086}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1296009373}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1296140445}[显示]{style="font-family:宋体"}[Transit]{lang="EN-US"}[交换机获取到的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机信息。]{style="font-family:宋体"}

[[\<Sysname\> display fip-snooping fcf]{lang="EN-US"}]{#struct_0_x9962_12256_x269943493}

[VLAN 3:]{lang="EN-US"}

[Interface   FCF MAC        FCF WWN                 Fabric Name             ENode]{lang="EN-US"}

[XGE1/0/1    000c-2999-eacd 66:66:66:63:66:64:61:30 41:6e:64:69:61:6d:6f:21 1]{lang="EN-US"}

[XGE1/0/2    000c-2999-eaad 66:66:66:63:66:64:61:31 41:6e:64:69:61:6d:6f:22 2]{lang="EN-US"}

[[表1-50 ]{lang="EN-US"}[display fip-snooping fcf]{lang="EN-US"}]{#struct_0_x9962_12256_x270336709}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1568094217}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x270533317}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x269877958}

[[VLAN 3]{lang="EN-US"}]{#struct_0_x9962_12256_x270140102}

[[显示]{style="font-family:宋体"}[VLAN 3]{lang="EN-US"}]{#struct_0_x9962_12256_x269943495}[的信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x270205639}

[[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_x270074568}[交换机上连接]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的以太网接口]{style="font-family:宋体"}

[[FCF MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x270336712}

[[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x270533320}[交换机的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[FCF WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x269877961}

[[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x270140105}[交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Fabric Name]{lang="EN-US"}]{#struct_0_x9962_12256_x270009034}

[[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_x270205642}[网络的名称]{style="font-family:宋体"}

[[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_1645882744}

[[该]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1646144888}[交换机下存在的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[的个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-633155257 .myid}
[]{#_Toc404798203}[]{#struct_0_x9962_12256_1646013816}

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping flushing-rules**

------------------------------------------------------------------------

[**[display fip-snooping flushing-rules]{lang="EN-US"}**]{#struct_0_x9962_12256_1645358456}[命令用来显示正在下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1645817207}

[**[display fip-snooping flushing-rules]{lang="EN-US"}**[ \[ **enode** \| **fcf** \] \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1645686135}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1646079351}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1645948279}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1645292919}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1645817206}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1645686134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1646079350}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1645358454}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1645882741}

[**[enode]{lang="EN-US"}**]{#struct_0_x9962_12256_1645751669}[：显示正在下刷的]{style="font-family:宋体"}[ENode FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[fcf]{lang="EN-US"}**]{#struct_0_x9962_12256_1646144885}[：显示正在下刷的]{style="font-family:宋体"}[FCF FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1646013813}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的正在下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的正在下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1645358453}

[[只有已经下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}]{#struct_0_x9962_12256_1645817204}[规则可以用来过滤]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文，正在下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则不能用来过滤]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[需要注意的是，如果不指定]{style="font-family:宋体"}**[enode]{lang="EN-US"}**]{#struct_0_x9962_12256_1645686132}[和]{style="font-family:宋体"}**[fcf]{lang="EN-US"}**[参数，则显示正在下刷的所有]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则，包括]{style="font-family:宋体"}[ENode FIP Snooping]{lang="EN-US"}[规则和]{style="font-family:宋体"}[FCF FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1646079348}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1645948276}[显示正在下刷的所有]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[\<Sysname\> display fip-snooping flushing-rules]{lang="EN-US"}]{#struct_0_x9962_12256_79864337}

[VLAN 2:]{lang="EN-US"}

[  FCF flushing-rules information:]{lang="EN-US"}

[    Interface   Source MAC/Mask      Destination MAC/Mask]{lang="EN-US"}

[    XGE1/0/1    0000-1234-0212/48    0efc-0034-0111/24]{lang="EN-US"}

[  ENode flushing-rules information:]{lang="EN-US"}

[    Interface   Source MAC/Mask      Destination MAC/Mask]{lang="EN-US"}

[    XGE1/0/2    0efc-0034-0202/48    0000-1234-0101/48]{lang="EN-US"}

[ ]{lang="EN-US"}

[VLAN 5:]{lang="EN-US"}

[  FCF flushing-rules information:]{lang="EN-US"}

[    Interface   Source MAC/Mask      Destination MAC/Mask]{lang="EN-US"}

[    XGE1/0/3    0000-1234-2212/48    0efc-0034-2111/24]{lang="EN-US"}

[[表1-51 ]{lang="EN-US"}[display fip-snooping flushing-rules]{lang="EN-US"}]{#struct_0_x9962_12256_79208977}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1527597833}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_79602192}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_79274512}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_79667727}

[[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_79864335}[的信息]{style="font-family:宋体"}

[[FCF flushing-rules information]{lang="EN-US"}]{#struct_0_x9962_12256_79733262}

[[正在下刷的]{style="font-family:宋体"}[FCF FIP Snooping]{lang="EN-US"}]{#struct_0_x9962_12256_79929870}[规则]{style="font-family:宋体"}

[[ENode flushing-rules information]{lang="EN-US"}]{#struct_0_x9962_12256_483083330}

[[正在下刷的]{style="font-family:宋体"}[ENode FIP Snooping]{lang="EN-US"}]{#struct_0_x9962_12256_483279937}[规则]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_482493505}

[[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_482886720}[交换机上的以太网接口]{style="font-family:宋体"}

[[Source MAC/Mask]{lang="EN-US"}]{#struct_0_x9962_12256_482559040}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9962_12256_482952255}[地址和掩码]{style="font-family:宋体"}

[[Destination MAC/Mask]{lang="EN-US"}]{#struct_0_x9962_12256_483148863}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9962_12256_483017790}[地址和掩码]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_482886718}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fip-snooping rules]{lang="EN-US"}**]{#struct_0_x9962_12256_483279934}

::: {#1580459880 .myid}
[]{#_Toc404798204}[]{#struct_0_x9962_12256_482559038}

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping rules**

------------------------------------------------------------------------

[**[display fip-snooping rules]{lang="EN-US"}**]{#struct_0_x9962_12256_483083325}[命令用来显示已经下刷的]{style="font-family:
宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_482952253}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9962_12256_483345469}

[**[display fip-snooping rules]{lang="EN-US"}**[ \[ **enode** \| **fcf** \] \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_483214397}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9962_12256_482559037}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display fip-snooping rules]{lang="EN-US"}**[ \[ **enode** \| **fcf** \] \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1083000611}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9962_12256_x1083197219}[模式：]{style="font-family:宋体"}

[**[display fip-snooping rules]{lang="EN-US"}**[ \[ **enode** \| **fcf** \] \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1082804003}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1082935075}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1083590435}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1083066148}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1083197220}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1082804004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1083524900}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1083000613}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1083131685}

[**[enode]{lang="EN-US"}**]{#struct_0_x9962_12256_x1082738469}[：显示已经下刷的]{style="font-family:宋体"}[ENode FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[fcf]{lang="EN-US"}**]{#struct_0_x9962_12256_x1082869541}[：显示已经下刷的]{style="font-family:宋体"}[FCF FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1083524901}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的已经下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的已经下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_x9962_12256_x1082935078}[ ]{lang="SV"}[[slot-number]{lang="SV"}]{.commandparameterChar}[：显示指定单板上的信息。]{style="font-family:宋体"}[[slot-number]{lang="SV"}]{.commandparameterChar}[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_x1082804007}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备上的信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_1205338202}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_x1082738472}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ **slot** ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备指定单板上的信息。]{style="font-family:宋体"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9962_12256_1372375269}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1082869544}

[[只有已经下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}]{#struct_0_x9962_12256_x1083524904}[规则可以用来过滤]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文，正在下刷的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则不能用来过滤]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[需要注意的是，如果不指定]{style="font-family:宋体"}**[enode]{lang="EN-US"}**]{#struct_0_x9962_12256_x323485724}[和]{style="font-family:宋体"}**[fcf]{lang="EN-US"}**[参数，则显示]{style="font-family:宋体"}[已经下刷的所有]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则，包括]{style="font-family:宋体"}[ENode FIP Snooping]{lang="EN-US"}[规则和]{style="font-family:宋体"}[FCF FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x323616796}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x323289116}[显示已经下刷的所有]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[\<Sysname\> display fip-snooping rules slot 1]{lang="EN-US"}]{#struct_0_x9962_12256_x1890159492}

[Slot 1:]{lang="EN-US"}

[  VLAN 2]{lang="EN-US"}[：]{style="font-family:宋体"}

[    FCF rules information:]{lang="EN-US"}

[      Interface   Source MAC/Mask     Destination MAC/Mask   DriverContext]{lang="EN-US"}

[      XGE1/0/1    0000-1234-0202/48   0efc-0034-0101/24      ffffffff]{lang="EN-US"}

[    ENode rules information:]{lang="EN-US"}

[      Interface   Source MAC/Mask     Destination MAC/Mask   DriverContext]{lang="EN-US"}

[      XGE1/0/2    0efc-0034-0102/48   0000-1234-0201/48      ffffffff]{lang="EN-US"}

[ ]{lang="EN-US"}

[  VLAN 4]{lang="EN-US"}[：]{style="font-family:宋体"}

[    FCF rules information:]{lang="EN-US"}

[      Interface  Source MAC/Mask      Destination MAC/Mask   DriverContext]{lang="EN-US"}

[      XGE1/0/3   0000-1234-1202/48    0efc-0034-1101/24      ffffffff]{lang="EN-US"}

[[表1-52 ]{lang="EN-US"}[display fip-snooping rules]{lang="EN-US"}]{#struct_0_x9962_12256_x1889635205}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1495636989}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1889438597}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1889569670}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_x1889373062}

[[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_x1890159494}[的信息]{style="font-family:宋体"}

[[FCF rules information]{lang="EN-US"}]{#struct_0_x9962_12256_x1486088531}

[[已经下刷的]{style="font-family:宋体"}[FCF FIP Snooping]{lang="EN-US"}]{#struct_0_x9962_12256_x1486285140}[规则]{style="font-family:宋体"}

[[ENode rules information]{lang="EN-US"}]{#struct_0_x9962_12256_x1486022996}

[[已经下刷的]{style="font-family:宋体"}[ENode FIP Snooping]{lang="EN-US"}]{#struct_0_x9962_12256_x1486874964}[规则]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x1486022997}

[[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_x1486809429}[交换机上的以太网接口]{style="font-family:宋体"}

[[Source MAC/Mask]{lang="EN-US"}]{#struct_0_x9962_12256_x1486481750}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x1486219606}[地址和掩码]{style="font-family:宋体"}

[[Destination MAC/Mask]{lang="EN-US"}]{#struct_0_x9962_12256_x1486416215}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9962_12256_x1486154071}[地址和掩码]{style="font-family:宋体"}

[[DriverContext]{lang="EN-US"}]{#struct_0_x9962_12256_1242532681}

[[驱动上下文]{style="font-family:宋体"}]{#struct_0_x9962_12256_1242794825}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242073929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fip-snooping flushing-rules]{lang="EN-US"}**]{#struct_0_x9962_12256_1242598216}

::: {#-2090764144 .myid}
[]{#_Toc404798205}[]{#struct_0_x9962_12256_1242467144}

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping sessions**

------------------------------------------------------------------------

[**[display fip-snooping sessions]{lang="EN-US"}**]{#struct_0_x9962_12256_1242794824}[命令用来显示]{style="font-family:
宋体"}[FIP Snooping]{lang="EN-US"}[的会话信息，即]{style="font-family:
宋体"}[ENode]{lang="EN-US"}[和]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242663752}

[**[display fip-snooping sessions]{lang="EN-US"}**[ \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1242008392}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242467143}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1242860359}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242729287}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1242073927}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1242532678}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1242401606}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1242794822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242073926}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1242598213}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242467141}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1242860357}[显示]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[的会话信息。]{style="font-family:宋体"}

[[\<Sysname\> display fip-snooping sessions]{lang="EN-US"}]{#struct_0_x9962_12256_1242663749}

[VLAN 2:]{lang="EN-US"}

[FCF MAC         ENode MAC       VN_Port MAC     VN_Port WWN]{lang="EN-US"}

[0000-1234-0202  0000-1234-0100  0efc-00ae-0002  41:6e:64:69:61:6d:6f:21]{lang="EN-US"}

[[表1-53 ]{lang="EN-US"}[display fip-snooping sessions]{lang="EN-US"}]{#struct_0_x9962_12256_1242008389}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1195190757}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242860356}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1242073924}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_1289455776}

[[VLAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_1289717920}[中的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[会话信息]{style="font-family:宋体"}

[[FCF MAC]{lang="EN-US"}]{#struct_0_x9962_12256_1289521311}

[[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1289783455}[的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ENode MAC]{lang="EN-US"}]{#struct_0_x9962_12256_1289586846}

[[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_1289848990}[的]{style="font-family:宋体"}[FCoE MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VN_Port MAC]{lang="EN-US"}]{#struct_0_x9962_12256_1289652381}

[[VN_Port]{lang="EN-US"}]{#struct_0_x9962_12256_1289848989}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VN_Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1289062557}

[[VN_Port]{lang="EN-US"}]{#struct_0_x9962_12256_1289914524}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#327215851 .myid}
[]{#_Toc404798206}[]{#struct_0_x9962_12256_1289783452}

**FC和FCoE \-- FIP Snooping配置命令 \-- fip-snooping enable**

------------------------------------------------------------------------

[**[fip-snooping enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1289128092}[命令用来开启]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo fip-snooping enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1289586843}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1289455771}

[**[fip-snooping enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1289848987}

[**[undo fip-snooping enable]{lang="EN-US"}**]{#struct_0_x9962_12256_1289717915}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276431557}

[[FIP Snooping]{lang="EN-US"}]{#struct_0_x9962_12256_x276562629}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276169413}

[[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x276366021}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x277021381}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x276497094}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x276628166}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276300486}

[[在]{style="font-family:宋体"}[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_x276955846}[交换机上，没有开启]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[功能的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不能处理]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文和]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[当需要某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x276431559}[具有处理]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文以及]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文的能力时，开启该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276628167}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x276234951}[开启]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x276366023}

[\[Sysname\] vlan 10]{lang="EN-US"}

[\[Sysname-vlan10\] fip-snooping enable]{lang="EN-US"}
:::

::: {#-1596987020 .myid}
[]{#_Toc404798207}[]{#struct_0_x9962_12256_x276431560}

**FC和FCoE \-- FIP Snooping配置命令 \-- fip-snooping fc-map**

------------------------------------------------------------------------

[**[fip-snooping fc-map]{lang="EN-US"}**]{#struct_0_x9962_12256_x276562632}[命令用来配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下的]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo fip-snooping fc-map]{lang="EN-US"}**]{#struct_0_x9962_12256_x276169416}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276300488}

[**[fip-snooping fc-map]{lang="EN-US"}**[ *fc-map*]{lang="EN-US"}]{#struct_0_x9962_12256_x277021384}

[**[undo fip-snooping fc-map]{lang="EN-US"}**]{#struct_0_x9962_12256_x276497097}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276628169}

[[每个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x276300489}[下的]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值均为]{style="font-family:宋体"}[0x0EFC00]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276955849}

[[VLAN]{lang="EN-US"}]{#struct_0_x9962_12256_x276431562}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x276562634}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x276234954}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x276366026}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x277021386}

[*[fc-map]{lang="EN-US"}*]{#struct_0_x9962_12256_1656434040}[：]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0x0EFC00]{lang="EN-US"}[～]{style="font-family:宋体"}[0x0EFCFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656302968}

[[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_1656171896}[交换机上某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的以太网接口从]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机接收到报文后，会检查接收报文的]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值和]{style="font-family:宋体"}[Transit]{lang="EN-US"}[交换机上该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下的]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值是否一致：如果一致，则转发报文；如果不一致，则丢弃报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656106360}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1656630647}[配置]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x0EFCFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1656499575}

[\[Sysname\] vlan 10]{lang="EN-US"}

[\[Sysname-vlan 10\] fip-snooping fc-map 0efcff]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656368503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcoe fcmap]{lang="EN-US"}**]{#struct_0_x9962_12256_1656040823}
:::

::: {#1628540224 .myid}
[]{#_Toc404798208}[]{#struct_0_x9962_12256_1656565110}

**FC和FCoE \-- FIP Snooping配置命令 \-- fip-snooping port-mode**

------------------------------------------------------------------------

[**[fip-snooping port-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1656434038}[命令用来配置]{style="font-family:宋体"}[Transit]{lang="EN-US"}[交换机上以太网接口的模式。]{style="font-family:宋体"}

[**[undo fip-snooping port-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1656368502}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656237430}

[**[fip-snooping port-mode]{lang="EN-US"}**[ { **enode** \| **fcf** }]{lang="EN-US"}]{#struct_0_x9962_12256_1656106358}

[**[undo fip-snooping port-mode]{lang="EN-US"}**]{#struct_0_x9962_12256_1656630645}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656302965}

[[以太网接口为]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_1656171893}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656040821}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9962_12256_1656630644}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656499572}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1656368500}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1656237428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656565107}

[**[enode]{lang="EN-US"}**]{#struct_0_x9962_12256_1656434035}[：]{style="font-family:宋体"}[ENode]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[fcf]{lang="EN-US"}**]{#struct_0_x9962_12256_1656302963}[：]{style="font-family:宋体"}[FCF]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1656237427}

[[Transit]{lang="EN-US"}]{#struct_0_x9962_12256_1656106355}[交换机上的以太网接口有两种模式：]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式和]{style="font-family:宋体"}[ENode]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[与]{lang="EN-US" style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x9962_12256_90546707}[相连的以太网接口需要配置为]{lang="EN-US" style="font-family:宋体"}[ENode]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[与]{style="font-family:宋体"}]{#struct_0_x9962_12256_90415635}[FCF]{lang="EN-US"}[交换机相连的以太网接口需要配置为]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_90087955}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_90022418}[将接口]{style="font-family:宋体"}[Ten-GigabitEthernet1/0/2]{lang="EN-US"}[配置为]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_90219023}

[\[Sysname\] interface ten-gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-Ten-GigabitEthernet1/0/2\] fip-snooping port-mode fcf]{lang="EN-US"}
:::

::: {#1866212269 .myid}
[]{#_Toc404798210}[]{#struct_0_x9962_12256_x357597221}[]{#_Toc393442800}[]{#_Toc374188674}

**FC和FCoE \-- FC端口安全配置命令 \-- any-wwn**

------------------------------------------------------------------------

[**[any-wwn]{lang="EN-US"}**]{#struct_0_x9962_12256_x897596885}[命令用来配置允许任意设备在指定接口登录。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **any-wwn**]{lang="EN-US"}]{#struct_0_x9962_12256_x478802108}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_234482745}

[**[any-wwn]{lang="EN-US"}**[ **interface** *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_x929370293}

[**[undo]{lang="EN-US"}**[ **any-wwn** **interface** *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_x357597224}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x897793493}

[[未配置接口允许任意设备登录。]{style="font-family:宋体"}]{#struct_0_x9962_12256_763021440}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1251682534}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_846936982}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_115752311}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x357597223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x897727957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1278829856}

[**[interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_x1904731236}[：表示允许登录的接口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type* *interface-number1* \[ **to** *interface-type* *interface-number2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:
宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。支持]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口（不能是]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合的成员接口）、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_956485725}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1594081930}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该接口上已登录设备的登录状态。该接口上已登录的设备是否会下线，取决于配置安全策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线。]{style="font-family:宋体"}]{#struct_0_x9962_12256_1981054944}

[[需要注意的是，开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1531267554}[端口安全功能后才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1922386032}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1451295706}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中配置允许任意设备在]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1884687237}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] any-wwn interface fc 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1981054945}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中配置允许任意设备在]{style="font-family:宋体"}[VFC1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1531202018}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] any-wwn interface vfc 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1928265363}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_x1080175021}
:::

::: {#1925331093 .myid}
[]{#_Toc404798211}[]{#struct_0_x9962_12256_x122990341}[]{#_Toc393442801}[]{#_Toc374188679}

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security database**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_1981054942}[命令用来显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1531660770}

[**[display]{lang="EN-US"}**[ **fc-port-security** **database** { **all** \| **auto-learn** \| **static** } \[ **interface** *interface-type* *interface-number* \] \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1943071533}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_136751332}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1981054943}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1531595234}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_365940081}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x817685229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2072391854}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1981054940}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1531529698}

[**[all]{lang="EN-US"}**]{#struct_0_x9962_12256_x1986247493}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的所有表项，包括]{style="font-family:宋体"}[static]{lang="EN-US"}[表项、]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项、]{style="font-family:宋体"}[learning]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[auto-learn]{lang="EN-US"}**]{#struct_0_x9962_12256_1616920077}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项和]{style="font-family:宋体"}[learning]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x9962_12256_1137509378}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的]{style="font-family:宋体"}[static]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type*  *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_1054557360}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中指定接口相关的表项。如果不指定接口，则显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中所有接口的表项。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1981054941}[：显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的表项，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果不指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，则显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x27997989}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_393144698}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1531464162}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_408764968}[显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的所有表项。]{style="font-family:宋体"}

[[\<Sysname\> display fc-port-security database all vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_1981054938}

[Total entries: 7]{lang="EN-US"}

[Database for VSAN 2:]{lang="EN-US"}

[  Logging-in entity                Interface              Type]{lang="EN-US"}

[  Any WWN                          Fc1/0/7                Static]{lang="EN-US"}

[  20:33:44:78:66:77:ab:97(pWWN)    Any interface          Static]{lang="EN-US"}

[  20:36:44:78:66:77:ab:97(pWWN)    Fc1/0/6                Static]{lang="EN-US"}

[  20:36:44:78:66:77:ab:9e(pWWN)    Fc1/0/9                Learned]{lang="EN-US"}

[  20:86:44:65:90:2a:ab:3a(pWWN)    Fc1/0/5                Learning]{lang="EN-US"}

[  10:83:45:78:66:77:ab:93(nWWN)    Fc1/0/7                Static]{lang="EN-US"}

[  10:36:44:78:66:77:ab:96(sWWN)    Fc1/0/8                Static]{lang="EN-US"}

[[表1-54 ]{lang="EN-US"}[display fc-port-security database]{lang="EN-US"}]{#struct_0_x9962_12256_1531005407}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1483694698}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1981054936}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1981054937}

[[Total entries]{lang="EN-US"}]{#struct_0_x9962_12256_24739809}

[[表项的数目]{style="font-family:宋体"}]{#struct_0_x9962_12256_24739807}

[[Database for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_24739804}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_24739802}[内的表项]{style="font-family:宋体"}

[[Logging-in entity]{lang="EN-US"}]{#struct_0_x9962_12256_24739803}

[[允许登录设备的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_24739801}[（]{style="font-family:宋体"}[Any WWN]{lang="EN-US"}[表示允许任意设备登录），括号中显示的是]{style="font-family:宋体"}[WWN]{lang="EN-US"}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1931575328}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1931575330}[：表示]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[nWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1931575332}[：表示节点设备或]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x1931575331}

[[设备允许登录的接口，]{style="font-family:宋体"}[Any interface]{lang="EN-US"}]{#struct_0_x9962_12256_x1931575333}[表示允许在任意接口登录]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x9962_12256_x1931575335}

[[表项的类型，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x742096928}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static]{lang="EN-US"}]{#struct_0_x9962_12256_x742096930}[：表示手工配置的表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[learned]{lang="EN-US"}]{#struct_0_x9962_12256_x742096929}[：表示关闭自动学习功能后，由]{style="font-family:宋体"}[learning]{lang="EN-US"}[表项转化为的]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项，不随设备的下线而删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[learning]{lang="EN-US"}]{#struct_0_x9962_12256_x742096931}[：表示通过自动学习功能动态学习的临时表项，将随设备的下线而删除]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_146429130}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_x770389847}

::: {#1794260804 .myid}
[]{#_Toc404798212}[]{#struct_0_x9962_12256_x1028724538}[]{#_Toc393442802}[]{#_Toc374188680}

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fc-port-security** **statistics**]{lang="EN-US"}]{#struct_0_x9962_12256_x742096934}[命令用来显示]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_146756810}

[**[display]{lang="EN-US"}**[ **fc-port-security** **statistics** \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1510714961}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x903227607}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x742096933}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_146298058}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_143413933}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_304629048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_439630618}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x742096936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_146625738}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x518552509}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的统计信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果不指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1997366457}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1950536392}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2077550919}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_678439080}[显示]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc-port-security statistics vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_x742096935}

[Statistics for VSAN 2:]{lang="EN-US"}

[  Number of permitted pWWN logins: 2]{lang="EN-US"}

[  Number of permitted nWWN logins: 2]{lang="EN-US"}

[  Number of permitted sWWN logins: 2]{lang="EN-US"}

[  Number of denied pWWN logins   : 0]{lang="EN-US"}

[  Number of denied nWWN logins   : 0]{lang="EN-US"}

[  Number of denied sWWN logins   : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Total logins permitted  : 6]{lang="EN-US"}

[  Total logins denied     : 0]{lang="EN-US"}

[[表1-55 ]{lang="EN-US"}[display fc-port-security statistics]{lang="EN-US"}]{#struct_0_x9962_12256_146691274}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1197206992}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1596555233}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1596555230}

[[Statistics for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1596555228}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1596555229}[内的统计信息]{style="font-family:宋体"}

[[Number of permitted pWWN logins]{lang="EN-US"}]{#struct_0_x9962_12256_1596555227}

[[允许]{style="font-family:宋体"}[PWWN]{lang="EN-US"}]{#struct_0_x9962_12256_1596555225}[登录的次数]{style="font-family:宋体"}

[[Number of permitted nWWN logins]{lang="EN-US"}]{#struct_0_x9962_12256_x359759904}

[[允许]{style="font-family:宋体"}[NWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x359759906}[登录的次数]{style="font-family:宋体"}

[[Number of permitted sWWN logins]{lang="EN-US"}]{#struct_0_x9962_12256_x359759905}

[[允许]{style="font-family:宋体"}[SWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x359759907}[登录的次数]{style="font-family:宋体"}

[[Number of denied pWWN logins]{lang="EN-US"}]{#struct_0_x9962_12256_x359759910}

[[拒绝]{style="font-family:宋体"}[PWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x359759912}[登录的次数]{style="font-family:宋体"}

[[Number of denied nWWN logins]{lang="EN-US"}]{#struct_0_x9962_12256_1978892256}

[[拒绝]{style="font-family:宋体"}[NWWN]{lang="EN-US"}]{#struct_0_x9962_12256_1978892257}[登录的次数]{style="font-family:宋体"}

[[Number of denied sWWN logins]{lang="EN-US"}]{#struct_0_x9962_12256_1978892255}

[[拒绝]{style="font-family:宋体"}[SWWN]{lang="EN-US"}]{#struct_0_x9962_12256_1978892252}[登录的次数]{style="font-family:宋体"}

[[Total logins permitted]{lang="EN-US"}]{#struct_0_x9962_12256_1978892250}

[[总共允许登录的次数]{style="font-family:宋体"}]{#struct_0_x9962_12256_1978892251}

[[Total logins denied]{lang="EN-US"}]{#struct_0_x9962_12256_1978892249}

[[总共拒绝登录的次数]{style="font-family:宋体"}]{#struct_0_x9962_12256_22577120}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_22577121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **fc-port-security** **statistics**]{lang="EN-US"}]{#struct_0_x9962_12256_x2126959682}

::: {#-194268458 .myid}
[]{#_Toc404798213}[]{#struct_0_x9962_12256_226545497}[]{#_Toc393442803}[]{#_Toc374188681}

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security status**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fc-port-security** **status**]{lang="EN-US"}]{#struct_0_x9962_12256_x1767630278}[命令用来显示是否开启]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能和自动学习功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x957361677}

[**[display]{lang="EN-US"}**[ **fc-port-security** **status** \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_22577118}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_174956633}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x728529007}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1278338389}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_22577119}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_2131271769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x114715721}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x899403629}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_22577116}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1793564761}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能和自动学习功能开启情况，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果不指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能和自动学习功能开启情况。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x218355085}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1538151488}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[本命令查看是否开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1603022869}[端口安全功能和自动学习功能，包括由命令]{style="font-family:宋体"}**[fc-port-security]{lang="EN-US"}**[ **enable**]{lang="EN-US"}[和]{style="font-family:宋体"}**[fc-port-security]{lang="EN-US"}**[ **auto-learn**]{lang="EN-US"}[引起的状态变化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1685732025}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1739951576}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能和自动学习功能开启情况。]{style="font-family:宋体"}

[[\<Sysname\> display fc-port-security status ]{lang="EN-US"}]{#struct_0_x9962_12256_22577117}

[Status for VSAN 1:]{lang="EN-US"}

[  FC port security: Disabled]{lang="EN-US"}

[  Auto learn: Disabled]{lang="EN-US"}

[Status for VSAN 2:]{lang="EN-US"}

[  FC port security: Enabled]{lang="EN-US"}

[  Auto learn: Enabled]{lang="EN-US"}

[[表1-56 ]{lang="EN-US"}[display fc-port-security status]{lang="EN-US"}]{#struct_0_x9962_12256_x545087399}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1160002956}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_22577115}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_22577113}

[[Status for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1933738016}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1933738018}[内]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能和自动学习功能开启情况]{style="font-family:宋体"}

[[FC port security]{lang="EN-US"}]{#struct_0_x9962_12256_x1933738017}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1933738019}[端口安全功能的开启状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x9962_12256_x1933738022}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x9962_12256_x1933738024}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}

[[Auto learn]{lang="EN-US"}]{#struct_0_x9962_12256_x1933738023}

[[自动学习功能的开启状态，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x744259615}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x9962_12256_x744259618}[：表示开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x9962_12256_x744259620}[：表示关闭]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x744259619}[端口安全功能时是否开启自动学习功能同样会影响该状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x744259622}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fc-port-security]{lang="EN-US"}**[ **auto-learn**]{lang="EN-US"}]{#struct_0_x9962_12256_x2053101028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fc-port-security]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_x796018779}

::: {#-291898637 .myid}
[]{#_Toc404798214}[]{#struct_0_x9962_12256_x1988329369}[]{#_Toc393442804}[]{#_Toc374188682}

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security violation**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fc-port-security** **violation**]{lang="EN-US"}]{#struct_0_x9962_12256_x744259621}[命令用来显示非法登录的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2053035492}

[**[display]{lang="EN-US"}**[ **fc-port-security** **violation** \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1827398964}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x587535266}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x819360809}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x744259624}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2053232100}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1443574163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x710840127}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1843997918}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x744259623}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x2053166564}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的非法登录信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果不指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的非法登录信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x431216980}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_236845235}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x45943500}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1328982914}[显示]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的非法登录信息。]{style="font-family:宋体"}

[[\<Sysname\> display fc-port-security violation vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_1594392544}

[Total entries: 3]{lang="EN-US"}

[Violations for VSAN 2:]{lang="EN-US"}

[  Interface   Logging-in entity               Last time             Repeat count]{lang="EN-US"}

[  Fc1/0/7     20:36:44:78:66:77:ab:97(pWWN)   2013/10/30 12:59:23   2]{lang="EN-US"}

[              20:00:00:e0:8b:06:d9:1d(nWWN)]{lang="EN-US"}

[  Fc1/0/8     20:45:78:66:77:ab:98:12(pWWN)   2013/10/29 17:59:23   3]{lang="EN-US"}

[              20:00:00:e0:8b:06:d9:1d(nWWN)]{lang="EN-US"}

[  Fc1/0/9     10:36:44:78:66:77:ab:96(sWWN)   2013/10/28 11:30:23   12]{lang="EN-US"}

[[表1-57 ]{lang="EN-US"}[display fc-port-security violation]{lang="EN-US"}]{#struct_0_x9962_12256_976777117}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1170455782}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1594392545}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1594392543}

[[Total entries]{lang="EN-US"}]{#struct_0_x9962_12256_1594392540}

[[非法登录信息总条数]{style="font-family:宋体"}]{#struct_0_x9962_12256_1594392538}

[[Violations for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1594392539}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1594392537}[的非法登录信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_x361922592}

[[交换机的接口]{style="font-family:宋体"}]{#struct_0_x9962_12256_x361922594}

[[Logging-in entity]{lang="EN-US"}]{#struct_0_x9962_12256_x361922593}

[[非法登录设备的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x361922595}[，括号中显示的是]{style="font-family:宋体"}[WWN]{lang="EN-US"}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x361922598}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[NP_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sWWN]{lang="EN-US"}]{#struct_0_x9962_12256_x361922600}[：表示]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[nWWN]{lang="EN-US"}]{#struct_0_x9962_12256_1976729568}[：表示节点设备或]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Last time]{lang="EN-US"}]{#struct_0_x9962_12256_1976729566}

[[该]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1976729567}[最后一次非法登录的时间]{style="font-family:宋体"}

[[Repeat count]{lang="EN-US"}]{#struct_0_x9962_12256_1976729565}

[[该]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1976729563}[在此接口重复非法登录的次数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-566252126 .myid}
[]{#_Toc404798215}[]{#struct_0_x9962_12256_1023286073}[]{#_Toc393442805}[]{#_Toc374188675}

**FC和FCoE \-- FC端口安全配置命令 \-- fc-port-security auto-learn**

------------------------------------------------------------------------

[**[fc-port-security]{lang="EN-US"}**[ **auto-learn**]{lang="EN-US"}]{#struct_0_x9962_12256_x956282131}[命令用来开启自动学习功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fc-port-security** **auto-learn**]{lang="EN-US"}]{#struct_0_x9962_12256_x1818883922}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1976729560}

[**[fc-port-security]{lang="EN-US"}**[ **auto-learn**]{lang="EN-US"}]{#struct_0_x9962_12256_1023089465}

[**[undo]{lang="EN-US"}**[ **fc-port-security** **auto-learn**]{lang="EN-US"}]{#struct_0_x9962_12256_x238269095}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x642444763}

[[自动学习功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1631109401}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1976729561}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1023155001}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_616682992}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1910700268}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_2099937308}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_20414432}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1593950858}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[开启自动学习功能后，后续登录的设备将以]{style="font-family:宋体"}[learning]{lang="EN-US"}]{#struct_0_x9962_12256_1219608353}[表项学习到策略数据库中。]{style="font-family:宋体"}[learning]{lang="EN-US"}[表项不对其它设备的登录产生影响，并将随设备下线而删除。关闭自动学习功能后，当前的]{style="font-family:宋体"}[learning]{lang="EN-US"}[表项将转化为]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项，对后续设备的登录产生影响，此后该表项不再随设备下线而删除。]{style="font-family:宋体"}

[[需要注意的是，开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1201187254}[端口安全功能后才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_57835937}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2045971813}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中开启自动学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_20414433}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] fc-port-security enable]{lang="EN-US"}

[\[Sysname-vsan2\] fc-port-security auto-learn]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1119043807}[学习完成后关闭自动学习功能，可以将]{style="font-family:宋体"}[learning]{lang="EN-US"}[表项转换为]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\[Sysname-vsan2\] undo fc-port-security auto-learn]{lang="EN-US"}]{#struct_0_x9962_12256_x1299307176}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x796790259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **status**]{lang="EN-US"}]{#struct_0_x9962_12256_20414430}
:::

::: {#693473894 .myid}
[]{#_Toc404798216}[]{#struct_0_x9962_12256_837271329}[]{#_Toc393442806}[]{#_Toc374188676}

**FC和FCoE \-- FC端口安全配置命令 \-- fc-port-security database copy**

------------------------------------------------------------------------

[**[fc-port-security]{lang="EN-US"}**[ **database** **copy**]{lang="EN-US"}]{#struct_0_x9962_12256_x1362246881}[命令用来将策略数据库中的]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项转化为]{style="font-family:宋体"}[static]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x521169586}

[**[fc-port-security]{lang="EN-US"}**[ **database** **copy**]{lang="EN-US"}]{#struct_0_x9962_12256_x544400833}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_20414431}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1501380831}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x176344414}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x708520821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1743057220}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1851065136}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1538217024}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[设备重启后，]{style="font-family:宋体"}[learned]{lang="EN-US"}]{#struct_0_x9962_12256_20414428}[表项将会丢失。如果用户需要保留动态学习的]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项，可以使用本命令将]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项转化为]{style="font-family:宋体"}[static]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[需要注意的是，开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_874007174}[端口安全功能后才能执行本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2140810755}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1819836923}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中将自动学习的]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项转化为]{style="font-family:宋体"}[static]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x475444033}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] fc-port-security database copy]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1015294740}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_20414429}
:::

::: {#-833641396 .myid}
[]{#_Toc404798217}[]{#struct_0_x9962_12256_x1464644986}[]{#_Toc393442807}[]{#_Toc374188670}

**FC和FCoE \-- FC端口安全配置命令 \-- fc-port-security enable**

------------------------------------------------------------------------

[**[fc-port-security]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_x1829415661}[命令用来开启]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fc-port-security** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_x1633914000}[命令用来关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x62654193}

[**[fc-port-security]{lang="EN-US"}**[ **enable** \[ **auto-learn** \]]{lang="EN-US"}]{#struct_0_x9962_12256_20414426}

[**[undo]{lang="EN-US"}**[ **fc-port-security** **enable**]{lang="EN-US"}]{#struct_0_x9962_12256_2021018246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_692636731}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_252158236}[端口安全功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_20414427}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x317633914}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1576367373}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x581665743}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_20414424}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1638681222}

[**[auto-learn]{lang="EN-US"}**]{#struct_0_x9962_12256_x1685282757}[：开启自动学习功能。如果不指定本参数，则不开启自动学习功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_571015004}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x834435971}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_106558461}[端口安全功能后，将根据授权登录条件对当前已登录和后续登录交换机的设备进行检查，不符合授权登录条件的设备将不允许登录交换机。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_20414425}[端口安全功能时可选择是否同时开启自动学习功能：如果开启自动学习功能，交换机将对当前已登录和后续登录的设备进行学习，并以]{style="font-family:宋体"}[learning]{lang="EN-US"}[表项添加到策略数据库中；如果不开启自动学习功能，将导致当前已登录的设备下线。]{style="font-family:宋体"}

[[需要注意的是，开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x699970938}[端口安全功能后才能进行]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全相关的其它配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x23910774}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_198018107}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中开启]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全功能，并同时开启自动学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_748809201}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] fc-port-security enable auto-learn]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1943631029}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **status**]{lang="EN-US"}]{#struct_0_x9962_12256_x1935900704}
:::

::: {#60645593 .myid}
[]{#_Toc404798218}[]{#struct_0_x9962_12256_364794702}[]{#_Toc393442808}[]{#_Toc374188673}

**FC和FCoE \-- FC端口安全配置命令 \-- nwwn**

------------------------------------------------------------------------

[**[nwwn]{lang="EN-US"}**]{#struct_0_x9962_12256_x704974013}[命令用来配置允许指定节点设备或]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机在指定接口登录。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **nwwn**]{lang="EN-US"}]{#struct_0_x9962_12256_1660535857}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1707252266}

[**[nwwn]{lang="EN-US"}**[ *nwwn* \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1935900703}

[**[undo]{lang="EN-US"}**[ **nwwn** *nwwn* \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x38489825}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1430626449}

[[未配置节点设备或]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1740624993}[交换机与登录接口的绑定关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1243255362}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1935900706}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x798004712}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x996411475}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1855213169}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x597141120}

[*[nwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_x1935900705}[：节点设备或]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[NWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_x1201289239}[：表示允许登录的接口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type* *interface-number1* \[ **to** *interface-type* *interface-number2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:
宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。支持]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口（不能是]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合的成员接口）、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。如果不指定接口，则表示允许在任意接口登录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x85470423}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1950181218}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该节点设备或]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_x1479925693}[交换机在已登录接口上的登录状态。如果命令中指定了允许登录的接口，则可能会影响该接口上已登录设备的登录状态。该节点设备或]{style="font-family:宋体"}[NPV]{lang="EN-US"}[交换机是否会在已登录接口下线，取决于配置安全策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线；该接口上已登录设备是否会下线，也是同理。]{style="font-family:宋体"}

[[需要注意的是，开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x2032501036}[端口安全功能后才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1004358469}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1935900708}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中配置允许]{style="font-family:宋体"}[NWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[20:36:44:78:66:77:ab:9e]{lang="EN-US"}[的节点设备在]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1960804126}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] nwwn 20:36:44:78:66:77:ab:9e interface fc 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1792728554}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中配置允许]{style="font-family:宋体"}[NWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[20:36:44:78:66:77:ab:9e]{lang="EN-US"}[的节点设备在]{style="font-family:宋体"}[VFC1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x138759314}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] nwwn 20:36:44:78:66:77:ab:9e interface vfc 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1236210420}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_x1935900707}
:::

::: {#60645607 .myid}
[]{#_Toc404798219}[]{#struct_0_x9962_12256_1930878643}[]{#_Toc393442809}[]{#_Toc374188671}

**FC和FCoE \-- FC端口安全配置命令 \-- pwwn**

------------------------------------------------------------------------

[**[pwwn]{lang="EN-US"}**]{#struct_0_x9962_12256_x29312785}[命令用来配置允许指定]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[或]{style="font-family:宋体"}[NP_Port]{lang="EN-US"}[在指定接口登录。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **pwwn**]{lang="EN-US"}]{#struct_0_x9962_12256_1127520826}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_2083337019}

[**[pwwn]{lang="EN-US"}**[ *pwwn* \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1644509154}

[**[undo]{lang="EN-US"}**[ **pwwn** *pwwn* \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1935900710}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1604639302}

[[未配置]{style="font-family:宋体"}[N_Port]{lang="EN-US"}]{#struct_0_x9962_12256_x364896207}[或]{style="font-family:宋体"}[NP_Port]{lang="EN-US"}[与登录接口的绑定关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1874648426}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1344049131}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1935900709}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_768079229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_17134567}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_594665114}

[*[pwwn]{lang="EN-US"}*]{#struct_0_x9962_12256_743811127}[：]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[或]{style="font-family:宋体"}[NP_Port]{lang="EN-US"}[的]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_x1520072998}[：表示允许登录的接口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type* *interface-number1* \[ **to** *interface-type* *interface-number2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:
宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。支持]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口（不能是]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合的成员接口）、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。如果不指定接口，则表示允许在任意接口登录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1935900712}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1593885322}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该]{style="font-family:宋体"}[N_Port]{lang="EN-US"}]{#struct_0_x9962_12256_1527528580}[或]{style="font-family:宋体"}[NP_Port]{lang="EN-US"}[在已登录接口上的登录状态。如果命令中指定了允许登录的接口，则可能会影响该接口上其它已登录设备的登录状态。该]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[或]{style="font-family:宋体"}[NP_Port]{lang="EN-US"}[是否会在已登录接口下线，取决于配置策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线；该接口上已登录设备是否会下线，也是同理。]{style="font-family:宋体"}

[[需要注意的是，开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_1816516636}[端口安全功能后才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_78376375}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1023826239}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中配置允许]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[20:36:44:78:66:77:ab:9e]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[在]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1935900711}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] pwwn 20:36:44:78:66:77:ab:9e interface fc 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1124244053}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中配置允许]{style="font-family:宋体"}[PWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[20:36:44:78:66:77:ab:9e]{lang="EN-US"}[的]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[在]{style="font-family:宋体"}[VFC1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1458659769}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] pwwn 20:36:44:78:66:77:ab:9e interface vfc 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_134960390}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_1476447993}
:::

::: {#1791274056 .myid}
[]{#_Toc404798220}[]{#struct_0_x9962_12256_x746422304}[]{#_Toc393442810}[]{#_Toc374188677}

**FC和FCoE \-- FC端口安全配置命令 \-- reset fc-port-security database**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_609363991}[命令用来清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1701060752}

[**[reset]{lang="EN-US"}**[ **fc-port-security** **database** { **all** \| **auto-learn** \| **static** } \[ **interface** *interface-type* *interface-number* \] **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1155146734}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_909666639}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x746422303}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_609036311}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1743576243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x289241204}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1436174109}

[**[all]{lang="EN-US"}**]{#struct_0_x9962_12256_x746422306}[：清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的]{style="font-family:宋体"}[static]{lang="EN-US"}[表项和]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[auto-learn]{lang="EN-US"}**]{#struct_0_x9962_12256_609232919}[：清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x9962_12256_x1468391143}[：清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中的]{style="font-family:宋体"}[static]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x9962_12256_2056826495}[：清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中指定接口相关的表项。如果不指定接口，则清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中所有接口的表项。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1730651153}[：清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的表项，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_828486475}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x27801381}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[清除]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x746422305}[端口安全策略数据库中的表项后，将对已登录的设备重新根据授权登录条件进行检查，因此可能会导致当前已登录的设备下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_609429527}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1250584390}[清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全策略数据库中]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的所有]{style="font-family:宋体"}[static]{lang="EN-US"}[表项和]{style="font-family:宋体"}[learned]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> reset fc-port-security database all vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_517544697}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_629923886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_x746422308}
:::

::: {#1526259333 .myid}
[]{#_Toc404798221}[]{#struct_0_x9962_12256_609626135}[]{#_Toc393442811}[]{#_Toc374188678}

**FC和FCoE \-- FC端口安全配置命令 \-- reset fc-port-security statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **fc-port-security** **statistics**]{lang="EN-US"}]{#struct_0_x9962_12256_x202914224}[命令用来清除]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2009217999}

[**[reset]{lang="EN-US"}**[ **fc-port-security** **statistics** **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1858070319}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x252893936}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x746422307}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_609298455}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1130295746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_350624686}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x746422310}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_609101848}[：清除指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全统计信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x834370435}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x2027822539}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1320118696}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x213116895}[清除]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[的]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset fc-port-security statistics vsan 2]{lang="EN-US"}]{#struct_0_x9962_12256_1299299145}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x746422309}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **statistics**]{lang="EN-US"}]{#struct_0_x9962_12256_609691671}
:::

::: {#-1726896282 .myid}
[]{#_Toc404798222}[]{#struct_0_x9962_12256_173614340}[]{#_Toc393442812}

**FC和FCoE \-- FC端口安全配置命令 \-- snmp-agent trap enable fc-port-security**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **fc-port-security**]{lang="EN-US"}]{#struct_0_x9962_12256_x171669098}[命令用来开启]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **fc-port-security**]{lang="EN-US"}]{#struct_0_x9962_12256_1690757461}[命令用来关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_560450784}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **fc-port-security** \[ **violation-happen** \]]{lang="EN-US"}]{#struct_0_x9962_12256_x746422312}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **fc-port-security** \[ **violation-happen** \]]{lang="EN-US"}]{#struct_0_x9962_12256_608970776}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1066776245}

[[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1028518127}[端口安全的告警功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1423735094}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x174674737}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x746422311}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_609167384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1338254291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x382386008}

[**[violation-happen]{lang="EN-US"}**]{#struct_0_x9962_12256_1592229856}[：]{style="font-family:宋体"}[表示非法登录的告警功能。开启本告警功能后，当发生非法登录时会生成告警信息，其中携带非法登录设备的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[、非法登录的接口以及非法登录的时间。如果未指定本参数，表示开启或关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的全部告警功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1524482176}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1950115682}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x1770149945}[端口安全的告警功能之后，]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x840007973}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1592229857}[开启]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的全部告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_x1524416640}

[\[Sysname\] snmp-agent trap enable fc-port-security]{lang="EN-US"}
:::

::: {#60645604 .myid}
[]{#_Toc404798223}[]{#struct_0_x9962_12256_1743184741}[]{#_Toc393442813}[]{#_Toc374188672}

**FC和FCoE \-- FC端口安全配置命令 \-- swwn**

------------------------------------------------------------------------

[**[swwn]{lang="EN-US"}**]{#struct_0_x9962_12256_x665882290}[命令用来配置允许指定]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机在指定接口登录。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **swwn**]{lang="EN-US"}]{#struct_0_x9962_12256_1020463878}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1592229854}

[**[swwn]{lang="EN-US"}**[ *swwn* \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1524613248}

[**[undo]{lang="EN-US"}**[ **swwn** *swwn* \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x9962_12256_722353801}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9962_12256_440843920}

[[未配置]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1027004194}[交换机与登录接口的绑定关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1924674485}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1592229855}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1524547712}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1986020483}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1245606903}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1300334578}

[*[swwn]{lang="EN-US"}*]{#struct_0_x9962_12256_1592229852}[：]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机的]{style="font-family:宋体"}[sWWN]{lang="EN-US"}[，格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x9962_12256_x1524744320}[：表示允许登录的接口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type* *interface-number1* \[ **to** *interface-type* *interface-number2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:
宋体"}*[interface-type]{lang="EN-US"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为接口编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。支持]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口（不能是]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合的成员接口）、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。如果不指定接口，则表示允许在任意接口登录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x417291089}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x1593819786}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x687252136}[交换机在已登录接口上的登录状态。如果命令中指定了允许登录的接口，则可能会影响该接口上其它已登录设备的登录状态。该]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机是否会在已登录接口下线，取决于配置策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线；该接口上已登录设备是否会下线，也是同理。]{style="font-family:宋体"}

[[需要注意的是，开启]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x9962_12256_x326804720}[端口安全功能后才能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1592229853}

[[\# VSAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_x1524678784}[中配置允许]{style="font-family:宋体"}[SWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[20:36:44:78:66:77:ab:9e]{lang="EN-US"}[的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机在]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1428194798}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] swwn 20:36:44:78:66:77:ab:9e interface fc 1/0/1]{lang="EN-US"}

[[\# VSAN 2]{lang="EN-US"}]{#struct_0_x9962_12256_x864591538}[中配置允许]{style="font-family:宋体"}[SWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[20:36:44:78:66:77:ab:9e]{lang="EN-US"}[的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机在]{style="font-family:宋体"}[VFC1]{lang="EN-US"}[接口登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1592229850}

[\[Sysname\] vsan 2]{lang="EN-US"}

[\[Sysname-vsan2\] swwn 20:36:44:78:66:77:ab:9e interface vfc 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1524875392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **fc-port-security** **database**]{lang="EN-US"}]{#struct_0_x9962_12256_1553451592}
:::

::: {#766541045 .myid}
[]{#_Toc404798225}[]{#struct_0_x9962_12256_459956300}[]{#_Toc351468940}[]{#_Toc335308275}

**FC和FCoE \-- FCS配置命令 \-- fcs discovery start**

------------------------------------------------------------------------

[**[fcs discovery start]{lang="EN-US"}**]{#struct_0_x9962_12256_1121052155}[命令用来发起拓扑发现。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1444733671}

[**[fcs discovery start ]{lang="EN-US"}**[\[ **age** *interval* \] **vsan** *vsan-list*]{lang="EN-US"}]{#struct_0_x9962_12256_206720869}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371320024}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_786824284}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1103879362}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x2128941995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_56168108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x382864164}

[**[age ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x9962_12256_x1997072424}[：拓扑发现数据的老化时间。]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[300]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[900]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-list*]{lang="EN-US"}]{#struct_0_x9962_12256_179975364}[：]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[列表，表示发起拓扑发现的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[范围。表示方式为]{style="font-family:宋体"}*[vsan-list]{lang="EN-US"}*[ = *vsan-id* \[ **to** *vsan-id* \]]{lang="EN-US"}[，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1538348096}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1747368460}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371385560}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1137400075}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[～]{style="font-family:宋体"}[VSAN 100]{lang="EN-US"}[内发起拓扑发现。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_1854084244}

[\[Sysname\] fcs discovery start vsan 1 to 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1465494871}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fcs discovery status]{lang="EN-US"}**]{#struct_0_x9962_12256_x1484220645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fcs database]{lang="EN-US"}**]{#struct_0_x9962_12256_989553928}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fcs ie]{lang="EN-US"}**]{#struct_0_x9962_12256_x1868997449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fcs port]{lang="DE"}**]{#struct_0_x9962_12256_371713240}
:::

::: {#909904695 .myid}
[]{#_Toc404798226}[]{#struct_0_x9962_12256_x229239987}[]{#_Toc351468941}

**FC和FCoE \-- FCS配置命令 \-- fcs discovery stop**

------------------------------------------------------------------------

[**[fcs discovery stop]{lang="EN-US"}**]{#struct_0_x9962_12256_x802022879}[命令用来取消拓扑发现。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1816725317}

[**[fcs discovery stop vsan ]{lang="EN-US"}***[vsan-list]{lang="EN-US"}*]{#struct_0_x9962_12256_76046998}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1129983188}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1610837870}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_351996026}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1454113899}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_371778776}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_965243238}

[**[vsan]{lang="EN-US"}**[ *vsan-list*]{lang="EN-US"}]{#struct_0_x9962_12256_1594972406}[：]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[列表，表示取消拓扑发现的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[范围。表示方式为]{style="font-family:宋体"}*[vsan-list]{lang="EN-US"}*[ = *vsan-id* \[ **to** *vsan-id* \]]{lang="EN-US"}[，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_731779042}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1206053592}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1333301681}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2112214492}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[～]{style="font-family:宋体"}[VSAN 100]{lang="EN-US"}[内取消拓扑发现。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9962_12256_267693699}

[\[Sysname\] fcs discovery stop vsan 1 to 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_292741847}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcs discovery start]{lang="EN-US"}**]{#struct_0_x9962_12256_637783226}
:::

::: {#1385285688 .myid}
[]{#_Toc404798227}[]{#struct_0_x9962_12256_371582168}[]{#_Toc351468942}[]{#_Toc335308276}

**FC和FCoE \-- FCS配置命令 \-- display fcs discovery status**

------------------------------------------------------------------------

[**[display fcs discovery status]{lang="EN-US"}**]{#struct_0_x9962_12256_x149256553}[命令用来显示当前的拓扑发现状态。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1446161147}

[**[display fcs discovery status]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_2094924025}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1874795853}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x966225284}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_842491809}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x222432417}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_371647704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x660508219}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1736211531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1009557696}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_844071201}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的拓扑发现状态，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的拓扑发现状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x431020372}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x985800276}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1735619621}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x74300141}[显示所有]{style="font-family:宋体"}[VSAN ]{lang="EN-US"}[内的拓扑发现状态。]{style="font-family:宋体"}

[[\<Sysname\> display fcs discovery status]{lang="EN-US"}]{#struct_0_x9962_12256_371975384}

[VSAN    Discovery Status]{lang="EN-US"}

[1       inProgress]{lang="EN-US"}

[2       completed]{lang="EN-US"}

[3       localOnly]{lang="EN-US"}

[[表1-58 ]{lang="EN-US"}[display fcs discovery status]{lang="EN-US"}]{#struct_0_x9962_12256_x70344968}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1112687965}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x970978596}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1414356501}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_986443390}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_45600449}[编号]{style="font-family:宋体"}

[[Discovery Status]{lang="EN-US"}]{#struct_0_x9962_12256_372040920}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1233864020}[内的拓扑发现状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localOnly]{lang="EN-US"}]{#struct_0_x9962_12256_x944684631}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[未进行拓扑发现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inProgress]{lang="EN-US"}]{#struct_0_x9962_12256_2080194337}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[正在进行拓扑发现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[completed]{lang="EN-US"}]{#struct_0_x9962_12256_1976319225}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[已完成拓扑发现]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371451097}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcs discovery start]{lang="EN-US"}**]{#struct_0_x9962_12256_1460075784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcs discovery stop]{lang="EN-US"}**]{#struct_0_x9962_12256_275815115}

::: {#23581264 .myid}
[]{#_Toc404798228}[]{#struct_0_x9962_12256_553100176}[]{#_Toc351468943}[]{#_Toc335308277}

**FC和FCoE \-- FCS配置命令 \-- display fcs database**

------------------------------------------------------------------------

[**[display fcs database]{lang="EN-US"}**]{#struct_0_x9962_12256_x393113735}[命令用来显示]{style="font-family:宋体"}[FCS]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1842690096}

[**[display fcs database]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x9962_12256_1717437018}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_131627324}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_371516633}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_630449590}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1183796456}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_460021836}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1337897978}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1282913863}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2126511694}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_535360459}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FCS]{lang="EN-US"}[数据库信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FCS]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371320025}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_778833209}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看本地]{style="font-family:宋体"}[FCS]{lang="EN-US"}]{#struct_0_x9962_12256_786824285}[数据库信息，包括]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息和端口信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1103879363}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x562858054}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FCS]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs database]{lang="EN-US"}]{#struct_0_x9962_12256_371385561}

[FCS Local Database in VSAN 1:]{lang="EN-US"}

[  IE WWN                   : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[  Domain ID                : 0x01]{lang="EN-US"}

[  Management address list  : snmp://192.168.6.100]{lang="EN-US"}

[                             snmp://192.168.0.100]{lang="EN-US"}

[  Fabric name              : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[  Logical name             : IE-Sysname1]{lang="EN-US"}

[  Information list         : xxx, Inc.#DS-A8263-M5#1.3(2a)]{lang="EN-US"}

[  IE ports:]{lang="EN-US"}

[    Interface   Port WWN                  Port type  Attached port WWNs]{lang="EN-US"}

[    Fc1/0/2     2f:15:01:11:22:00:01:01   F_Port       2f:15:01:11:22:00:01:02]{lang="EN-US"}

[                                                     2f:15:01:11:22:00:01:03]{lang="EN-US"}

[                                                     2f:15:01:11:22:00:01:04]{lang="EN-US"}

[    Fc1/0/1     38:00:00:11:22:00:01:01   E_Port     38:00:00:11:22:00:01:02]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IE WWN                   : 10:00:00:11:22:00:01:02]{lang="EN-US"}

[  Domain ID                : 0x02]{lang="EN-US"}

[  Management address list  : snmp://192.168.6.101]{lang="EN-US"}

[  Fabric name              : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[  Logical name             : IE-Sysname2]{lang="EN-US"}

[  Information list         : xxx, Inc.#DS-A8263-M5#1.3(2a)]{lang="EN-US"}

[  IE ports:]{lang="EN-US"}

[    Interface   Port WWN                  Port type  Attached port WWNs]{lang="EN-US"}

[    -           2f:15:01:11:22:00:01:01   F_Port       2f:15:01:11:22:00:01:02]{lang="EN-US"}

[    -           38:00:00:11:22:00:01:01   E_Port       38:00:00:11:22:00:01:02]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[FCS Local Database in VSAN 2:]{lang="EN-US"}

[  IE WWN                   : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[  Domain ID                : 0x01]{lang="EN-US"}

[  Management address list  : snmp://192.168.6.100]{lang="EN-US"}

[                             snmp://192.168.0.100]{lang="EN-US"}

[  Fabric name              : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[  Logical name             : IE-Sysname]{lang="EN-US"}

[  Information list         : xxx, Inc.#DS-A8263-M5#1.3(2a)]{lang="EN-US"}

[  IE ports:]{lang="EN-US"}

[    Interface    Port WWN                  Port type  Attached port WWNs]{lang="EN-US"}

[[表1-59 ]{lang="EN-US"}[display fcs database]{lang="EN-US"}]{#struct_0_x9962_12256_1137400076}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1112173797}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1853887636}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_371713241}

[[FCS Local Database in VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x229239988}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x802481631}[内的]{style="font-family:宋体"}[FCS]{lang="EN-US"}[数据库信息]{style="font-family:宋体"}

[[IE WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1713412610}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_336785850}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Domain ID]{lang="EN-US"}]{#struct_0_x9962_12256_371778777}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_965243237}[的域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Management addresss list]{lang="EN-US"}]{#struct_0_x9962_12256_1594972413}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x1333629362}[的管理地址列表，其中]{style="font-family:宋体"}[snmp://192.168.6.100]{lang="EN-US"}[，表示支持]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[管理协议，管理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.6.100]{lang="EN-US"}[。]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取管理地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置管理地址]{style="font-family:宋体"}

[[Fabric name]{lang="EN-US"}]{#struct_0_x9962_12256_x921510842}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_371582169}[内]{style="font-family:宋体"}[IE]{lang="EN-US"}[所在]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称，]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络名称]{style="font-family:宋体"}

[[Logical name]{lang="EN-US"}]{#struct_0_x9962_12256_x149256552}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x1446095611}[的设备名称，]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取设备名称]{style="font-family:宋体"}

[[Information list]{lang="EN-US"}]{#struct_0_x9962_12256_873008145}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_653769227}[的信息列表：厂商名称]{style="font-family:宋体"}[\#]{lang="EN-US"}[产品名称]{style="font-family:宋体"}[/]{lang="EN-US"}[编号]{style="font-family:宋体"}[\#]{lang="EN-US"}[发布编码。]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取信息列表]{style="font-family:宋体"}

[[IE ports]{lang="EN-US"}]{#struct_0_x9962_12256_371647705}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x660508218}[上的端口信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x9962_12256_1736277067}

[[接口名称（只有本地交换机对应]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_x9962_12256_1027389325}[下的接口显示实际接口名称，其它]{style="font-family:宋体"}[IE]{lang="EN-US"}[下的接口显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_371975385}

[[端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x70344969}

[[Port type]{lang="EN-US"}]{#struct_0_x9962_12256_x970978595}

[[端口的模式，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_1414422037}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E_Port]{lang="EN-US"}]{#struct_0_x9962_12256_x1777933556}[：表示]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F_Port]{lang="EN-US"}]{#struct_0_x9962_12256_689945380}[：表示]{lang="EN-US" style="font-family:宋体"}[F]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x9962_12256_x211849615}[：表示非以上模式]{lang="EN-US" style="font-family:宋体"}

[[Attached port WWNs]{lang="EN-US"}]{#struct_0_x9962_12256_372040921}

[[端口所连接的端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1233864021}[，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示端口未与其它端口连接]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x944750167}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}**[fcs discovery start]{lang="EN-US"}**]{#struct_0_x9962_12256_2045055343}

::: {#-928199534 .myid}
[]{#_Toc404798229}[]{#struct_0_x9962_12256_x1354049144}[]{#_Toc351468944}[]{#_Toc335308278}[]{#_Toc335726514}[]{#_Toc335727040}[]{#_Toc335897962}

**FC和FCoE \-- FCS配置命令 \-- display fcs ie**

------------------------------------------------------------------------

[**[display fcs ie]{lang="EN-US"}**]{#struct_0_x9962_12256_1742551078}[命令用来显示]{style="font-family:宋体"}[FCS]{lang="EN-US"}[的]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1235138506}

[**[display fcs ie]{lang="EN-US"}**[ \[ **vsan** *vsan-id* \[ **nwwn** *wwn* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x9962_12256_371451094}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1460075787}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_275749579}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1204998659}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_567199648}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1322197355}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_450022613}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1833043877}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371516630}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_630449593}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[nwwn ]{lang="EN-US"}***[wwn]{lang="EN-US"}*]{#struct_0_x9962_12256_1183796459}[：显示指定]{style="font-family:宋体"}[WWN]{lang="EN-US"}[的]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[wwn]{lang="EN-US"}*[格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。不指定该参数时，将显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有]{style="font-family:宋体"}[IE]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9962_12256_460087372}[：显示]{style="font-family:宋体"}[IE]{lang="EN-US"}[的详细信息。不指定该参数时，将显示]{style="font-family:宋体"}[IE]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x968522627}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_314706521}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1796053221}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x44238115}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs ie]{lang="EN-US"}]{#struct_0_x9962_12256_371320022}

[IE List for VSAN 1:]{lang="EN-US"}

[  IE WWN                   Domain ID   Mgmt addr list           Logical name]{lang="EN-US"}

[  10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100     Sysname]{lang="EN-US"}

[                                       snmp://192.168.0.100]{lang="EN-US"}

[  10:00:00:11:22:00:01:02  0x02        snmp://192.168.6.101     Sysname]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Total 2 IEs in Fabric.]{lang="EN-US"}

[ ]{lang="EN-US"}

[IE List for VSAN 2:]{lang="EN-US"}

[  IE WWN                   Domain ID   Mgmt addr list           Logical name]{lang="EN-US"}

[  10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100     Sysname]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Total 1 IEs in Fabric.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_786824290}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs ie vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_1234772794}

[IE List for VSAN 1:]{lang="EN-US"}

[  IE WWN                   Domain ID   Mgmt addr list           Logical name]{lang="EN-US"}

[  10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100     Sysname]{lang="EN-US"}

[                                       snmp://192.168.0.100]{lang="EN-US"}

[  10:00:00:11:22:00:01:02  0x02        snmp://192.168.6.101     Sysname]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Total 2 IEs in Fabric.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_451739113}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[NWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[10:00:00:11:22:00:01:01]{lang="EN-US"}[的]{style="font-family:宋体"}[IE]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs ie vsan 1 nwwn 10:00:00:11:22:00:01:01]{lang="EN-US"}]{#struct_0_x9962_12256_1055423334}

[IE WWN                   Domain ID   Mgmt addr list            Logical name]{lang="EN-US"}

[10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100      Sysname]{lang="EN-US"}

[                                     snmp://192.168.0.100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_371385558}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[NWWN]{lang="EN-US"}[为]{style="font-family:宋体"}[10:00:00:11:22:00:01:01]{lang="EN-US"}[的]{style="font-family:宋体"}[IE]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs ie vsan 1 nwwn 10:00:00:11:22:00:01:01 verbose ]{lang="EN-US"}]{#struct_0_x9962_12256_x818915069}

[IE Attributes:]{lang="EN-US"}

[  IE WWN                 : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[  IE type                : Switch]{lang="EN-US"}

[  Domain ID              : 0x01]{lang="EN-US"}

[  Fabric name            : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[  Logical name           : Sysname]{lang="EN-US"}

[  Management address list: snmp://192.168.6.100]{lang="EN-US"}

[                           snmp://192.168.0.100]{lang="EN-US"}

[  Information list       :]{lang="EN-US"}

[    Vendor name      : abc, Inc.]{lang="EN-US"}

[    Model name/number: DS-A8263-M5]{lang="EN-US"}

[    Release code     : 1.3(2a)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x2035928883}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IE]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs ie verbose]{lang="EN-US"}]{#struct_0_x9962_12256_371713238}

[IE List for VSAN 1:]{lang="EN-US"}

[  IE Attributes:]{lang="EN-US"}

[    IE WWN                 : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[    IE type                : Switch]{lang="EN-US"}

[    Domain ID              : 0x01]{lang="EN-US"}

[    Fabric name            : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[    Logical name           : Sysname]{lang="EN-US"}

[    Management address list: snmp://192.168.6.100]{lang="EN-US"}

[                             snmp://192.168.0.100]{lang="EN-US"}

[    Information list       : ]{lang="EN-US"}

[      Vendor name      : abc, Inc.]{lang="EN-US"}

[      Model name/number: DS-A8263-M5]{lang="EN-US"}

[      Release code     : 1.3(2a)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Total 1 IEs in Fabric.]{lang="EN-US"}

[ ]{lang="EN-US"}

[IE List for VSAN 2:]{lang="EN-US"}

[  IE Attributes:]{lang="EN-US"}

[    IE WWN                 : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[    IE type                : Switch]{lang="EN-US"}

[    Domain ID              : 0x01]{lang="EN-US"}

[    Fabric name            : 10:00:00:11:22:00:01:01]{lang="EN-US"}

[    Logical name           : Sysname]{lang="EN-US"}

[    Management address list: snmp://192.168.6.100]{lang="EN-US"}

[                             snmp://192.168.0.100]{lang="EN-US"}

[    Information list       :]{lang="EN-US"}

[      Vendor name      : abc, Inc.]{lang="EN-US"}

[      Model name/number: DS-A8263-M5]{lang="EN-US"}

[      Release code     : 1.3(2a)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Total 1 IEs in Fabric.]{lang="EN-US"}

[[表1-60 ]{lang="EN-US"}[display fcs ie]{lang="EN-US"}]{#struct_0_x9962_12256_2109412181}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1108160245}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_371778774}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_965243236}

[[IE List for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1594972412}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1333563826}[内的]{style="font-family:宋体"}[IE]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[IE Attributes]{lang="EN-US"}]{#struct_0_x9962_12256_798222835}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_371582166}[的属性]{style="font-family:宋体"}

[[IE WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x149256551}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x1446292219}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[IE type]{lang="EN-US"}]{#struct_0_x9962_12256_x2124173083}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x1573292008}[的类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Switch]{lang="EN-US"}]{#struct_0_x9962_12256_1756101078}[：表示交换机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x9962_12256_1925820507}[：表示非交换机]{lang="EN-US" style="font-family:宋体"}

[[Domain ID]{lang="EN-US"}]{#struct_0_x9962_12256_371647702}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x660508225}[的域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Fabric name]{lang="EN-US"}]{#struct_0_x9962_12256_1735425102}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x1944859249}[所在]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络的名称，]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络名称]{style="font-family:宋体"}

[[Logical name]{lang="EN-US"}]{#struct_0_x9962_12256_1002681318}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_371975382}[的设备名称，]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取设备名称]{style="font-family:宋体"}

[[Mgmt addr list]{lang="EN-US"}]{#struct_0_x9962_12256_x70344970}

[[Management address list]{lang="EN-US"}]{#struct_0_x9962_12256_985336532}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_x1749222345}[的管理服务地址列表，其中]{style="font-family:宋体"}[snmp://192.168.6.100]{lang="EN-US"}[，表示支持]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[管理协议，管理地址为]{style="font-family:宋体"}[192.168.6.100]{lang="EN-US"}[。]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取管理地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置管理地址]{style="font-family:宋体"}

[[Information list ]{lang="EN-US"}]{#struct_0_x9962_12256_x1593866791}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_372040918}[信息列表，]{style="font-family:宋体"}[Unknown]{lang="EN-US"}[表示未从对应]{style="font-family:宋体"}[IE]{lang="EN-US"}[获取信息列表]{style="font-family:宋体"}

[[Vendor name]{lang="EN-US"}]{#struct_0_x9962_12256_x213267390}

[[厂商名称]{style="font-family:宋体"}]{#struct_0_x9962_12256_1671120525}

[[Model name/number]{lang="EN-US"}]{#struct_0_x9962_12256_1462973673}

[[产品名称]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9962_12256_2101457017}[编号]{style="font-family:宋体"}

[[Release code]{lang="EN-US"}]{#struct_0_x9962_12256_1352816551}

[[发布编码]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1811715990}

[[Total 2 IEs in Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_371451095}

[[显示]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x9962_12256_1460075786}[中]{style="font-family:宋体"}[IE]{lang="EN-US"}[的个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_275684043}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}**[fcs discovery start]{lang="EN-US"}**]{#struct_0_x9962_12256_1112086308}

::: {#182673974 .myid}
[]{#_Toc404798230}[]{#struct_0_x9962_12256_388558427}[]{#_Toc351468945}[]{#_Toc335308279}

**FC和FCoE \-- FCS配置命令 \-- display fcs port**

------------------------------------------------------------------------

[**[display fcs port]{lang="DE"}**]{#struct_0_x9962_12256_x2037759552}[命令用来显示]{style="font-family:宋体"}[FCS]{lang="DE"}[的端口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_371516631}

[**[display fcs port]{lang="DE"}**]{#struct_0_x9962_12256_630449592}[ \[ **vsan** *vsan-id* \[ **pwwn** *wwn* \] \] \[ **verbose** \]]{lang="DE"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1183796458}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_460152908}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1398331276}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_112042183}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_163162104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1895718855}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_371320023}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_786824291}

[**[vsan ]{lang="EN-US"}***[vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_1234772793}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的端口信息。]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的端口信息。]{style="font-family:宋体"}

[**[pwwn ]{lang="EN-US"}***[wwn]{lang="EN-US"}*]{#struct_0_x9962_12256_451673577}[：显示指定]{style="font-family:宋体"}[WWN]{lang="EN-US"}[的端口信息。]{style="font-family:宋体"}*[wwn]{lang="EN-US"}*[格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。不指定该参数时，将显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内所有端口的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9962_12256_x146977190}[：显示端口的详细信息。不指定该参数时，将显示端口的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1404195904}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_1254386386}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1051904693}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1730260601}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs port]{lang="EN-US"}]{#struct_0_x9962_12256_371385559}

[Port List for VSAN 1:]{lang="EN-US"}

[  IE WWN: 10:00:00:11:22:00:01:01]{lang="EN-US"}

[    Port WWN                  Port type    Tx type             Module type]{lang="EN-US"}

[    2f:15:01:11:22:00:01:01   Unknown      Shortwave Laser     SFP with Serial ID]{lang="EN-US"}

[    38:00:00:11:22:00:01:01   E_Port       Shortwave Laser     SFP with Serial ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Total 2 switch-ports in IE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IE WWN: 10:00:00:11:22:00:01:02]{lang="EN-US"}

[    Port WWN                  Port type    Tx type             Module type]{lang="EN-US"}

[    38:00:00:11:22:00:01:02   E_Port       Shortwave Laser     SFP with Serial ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Total 1 switch-ports in IE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Port List for VSAN 2:]{lang="EN-US"}

[  IE WWN: 10:00:00:11:22:00:01:01]{lang="EN-US"}

[    Port WWN                  Port type    Tx type             Module type]{lang="EN-US"}

[    2f:15:01:11:22:00:01:01   Unknown      Shortwave Laser     SFP with Serial ID]{lang="EN-US"}

[    38:00:00:11:22:00:01:01   E_Port       Shortwave Laser     SFP with Serial ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Total 2 switch-ports in IE.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x818915068}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[为]{style="font-family:宋体"}[38:00:00:11:22:00:01:01]{lang="EN-US"}[的端口的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs port vsan 1 pwwn 38:00:00:11:22:00:01:01]{lang="EN-US"}]{#struct_0_x9962_12256_371713239}

[Port WWN                  Port type    Tx type             Module type]{lang="EN-US"}

[38:00:00:11:22:00:01:01   E_Port       Shortwave Laser     SFP with Serial ID]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_2109412180}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[为]{style="font-family:宋体"}[38:00:00:11:22:00:01:01]{lang="EN-US"}[的端口的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcs port vsan 1 pwwn 38:00:00:11:22:00:01:01 verbose]{lang="EN-US"}]{#struct_0_x9962_12256_x2077610321}

[Port Attributes:]{lang="EN-US"}

[  Port WWN                         : 38:00:00:11:22:00:01:01]{lang="EN-US"}

[  Port type                        : E_Port]{lang="EN-US"}

[  Tx type                          : Shortwave Laser]{lang="EN-US"}

[  Module type                      : SFP with Serial ID]{lang="EN-US"}

[  Port number                      : 465]{lang="EN-US"}

[  Attached port WWNs               : 2f:15:01:11:22:00:01:02]{lang="EN-US"}

[  Port state                       : Offline]{lang="EN-US"}

[  Port speed capability            : 10Gbps, 16Gbps]{lang="EN-US"}

[  Port speed operation             : 10Gbps ]{lang="EN-US"}

[  Port zoning enforcement status   : Soft, Hard]{lang="EN-US"}

[[表1-61 ]{lang="EN-US"}[display fcs port]{lang="EN-US"}]{#struct_0_x9962_12256_x1061827212}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1137697029}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_371778775}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_965243235}

[[Port List for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1594972411}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1333498290}[内的端口信息]{style="font-family:宋体"}

[[IE WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x2047667166}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_297530123}[的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Port Attributes]{lang="EN-US"}]{#struct_0_x9962_12256_371582167}

[[端口的属性]{style="font-family:宋体"}]{#struct_0_x9962_12256_x149256550}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x1446226683}

[[端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x919318916}

[[Port type]{lang="EN-US"}]{#struct_0_x9962_12256_x1516013803}

[[端口的模式，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_371647703}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E_Port]{lang="EN-US"}]{#struct_0_x9962_12256_x972716741}[：表示]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F_Port]{lang="EN-US"}]{#struct_0_x9962_12256_x1376001268}[：表示]{lang="EN-US" style="font-family:宋体"}[F]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x9962_12256_x1972140569}[：表示非以上模式]{lang="EN-US" style="font-family:宋体"}

[[Tx type]{lang="EN-US"}]{#struct_0_x9962_12256_x660508224}

[[端口的传输类型，包括：]{style="font-family:宋体"}[Long wave laser-LL(1550nm)]{lang="EN-US"}]{#struct_0_x9962_12256_1735490638}[、]{style="font-family:宋体"}[Short wave laser-SN(850nm)]{lang="EN-US"}[、]{style="font-family:宋体"}[Long wave laser cost reduced-LC(1310nm)]{lang="EN-US"}[、]{style="font-family:宋体"}[Electrical-EL]{lang="EN-US"}[、]{style="font-family:宋体"}[10GBASE-SR 850nm laser]{lang="EN-US"}[、]{style="font-family:宋体"}[10GBASE-LR 1310nm laser]{lang="EN-US"}[、]{style="font-family:宋体"}[10GBASE-ER 1550nm laser]{lang="EN-US"}[、]{style="font-family:宋体"}[10GBASE-LX4 WWDM 1300nm laser]{lang="EN-US"}[、]{style="font-family:宋体"}[10GBASE-SW 850nm laser]{lang="EN-US"}[、]{style="font-family:宋体"}[10GBASE-LW 1310nm laser]{lang="EN-US"}[、]{style="font-family:宋体"}[10GBASE-EW 1550nm laser]{lang="EN-US"}[和]{style="font-family:宋体"}[10GBASE-CX4]{lang="EN-US"}[。非以上类型则显示]{style="font-family:宋体"}[Unknown]{lang="EN-US"}

[[Module type]{lang="EN-US"}]{#struct_0_x9962_12256_x1979771751}

[[端口采用的光模块类型，包括：]{style="font-family:宋体"}[GLM]{lang="EN-US"}]{#struct_0_x9962_12256_371975383}[、]{style="font-family:宋体"}[GBIC with serial ID]{lang="EN-US"}[、]{style="font-family:宋体"}[GBIC without serial ID]{lang="EN-US"}[、]{style="font-family:宋体"}[SFP with serial ID]{lang="EN-US"}[、]{style="font-family:宋体"}[SFP without serial ID]{lang="EN-US"}[、]{style="font-family:宋体"}[XFP]{lang="EN-US"}[、]{style="font-family:宋体"}[X2 short]{lang="EN-US"}[、]{style="font-family:宋体"}[X2 Medium]{lang="EN-US"}[、]{style="font-family:宋体"}[X2 Tall]{lang="EN-US"}[、]{style="font-family:宋体"}[XPAX short]{lang="EN-US"}[、]{style="font-family:宋体"}[XPAX Medium]{lang="EN-US"}[、]{style="font-family:宋体"}[XPAX Tall]{lang="EN-US"}[、]{style="font-family:宋体"}[XENPAK]{lang="EN-US"}[、]{style="font-family:宋体"}[SFP-DWDM]{lang="EN-US"}[、]{style="font-family:宋体"}[QSFP]{lang="EN-US"}[和]{style="font-family:宋体"}[X2-DWDM]{lang="EN-US"}[。非以上类型则显示]{style="font-family:宋体"}[Other]{lang="EN-US"}[，获取不到光模块的类型则显示]{style="font-family:宋体"}[Unknown]{lang="EN-US"}

[[Port number]{lang="EN-US"}]{#struct_0_x9962_12256_x70344971}

[[端口的索引值]{style="font-family:宋体"}]{#struct_0_x9962_12256_985336533}

[[Attached port WWNs]{lang="EN-US"}]{#struct_0_x9962_12256_x1749222344}

[[所连接的端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_x27782850}[。当不存在连接的端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}[时，显示]{style="font-family:宋体"}[NA]{lang="EN-US"}

[[Port state]{lang="EN-US"}]{#struct_0_x9962_12256_372040919}

[[端口当前状态，包括：]{style="font-family:宋体"}]{#struct_0_x9962_12256_x340114099}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_x9962_12256_x213201854}[：表示端口链路已连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_x9962_12256_1704549723}[：表示端口链路未连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x9962_12256_1352882087}[：表示非以上类型]{lang="EN-US" style="font-family:宋体"}

[[Port speed capability]{lang="EN-US"}]{#struct_0_x9962_12256_500842072}

[[端口支持的所有速率，速率包括：]{style="font-family:宋体"}[1Gbps]{lang="EN-US"}]{#struct_0_x9962_12256_2040140652}[、]{style="font-family:宋体"}[2Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[4Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[10Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[16Gbps]{lang="EN-US"}[和]{style="font-family:宋体"}[20Gbps]{lang="EN-US"}[（可包含其中一项或多项）。非以上速率则显示]{style="font-family:宋体"}[Unknown]{lang="EN-US"}

[[Port speed operation]{lang="EN-US"}]{#struct_0_x9962_12256_1937535039}

[[端口当前的运行速率，运行速率包括：]{style="font-family:宋体"}[1Gbps]{lang="EN-US"}]{#struct_0_x9962_12256_1596509552}[、]{style="font-family:宋体"}[2Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[4Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[10Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[16Gbps]{lang="EN-US"}[和]{style="font-family:宋体"}[20Gbps]{lang="EN-US"}[（只可包含其中一项）。非以上速率则显示]{style="font-family:宋体"}[Unknown]{lang="EN-US"}

[[端口当前状态为]{style="font-family:宋体"}[Offline]{lang="EN-US"}]{#struct_0_x9962_12256_x656064879}[时，端口运行速率显示为]{style="font-family:宋体"}[Speed not established]{lang="EN-US"}

[[Port zoning enforcement status]{lang="EN-US"}]{#struct_0_x9962_12256_1021386551}

[[端口当前支持的]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x9962_12256_1937600575}[类型：]{style="font-family:宋体"}[Soft]{lang="EN-US"}[表示软件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[；]{style="font-family:宋体"}[Hard]{lang="EN-US"}[表示硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[。可以同时支持两种，以上两种均不支持则显示]{style="font-family:宋体"}[NA]{lang="EN-US"}

[[Total xx switch-ports in IE]{lang="EN-US"}]{#struct_0_x9962_12256_x753789742}

[[IE]{lang="EN-US"}]{#struct_0_x9962_12256_591078124}[的端口个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2046590935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fcs discovery start]{lang="EN-US"}**]{#struct_0_x9962_12256_x2143375458}

::: {#82651306 .myid}
[]{#_Toc404798232}[]{#struct_0_x9962_12256_x25982672}[]{#_Toc351468947}[]{#_Toc331425144}

**FC和FCoE \-- FDMI配置命令 \-- display fdmi database**

------------------------------------------------------------------------

[**[display fdmi database]{lang="EN-US"}**]{#struct_0_x9962_12256_323303277}[命令用来显示]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_595064264}

[**[display]{lang="EN-US"}**[ **fdmi** **database** \[ **vsan** *vsan-id* \[ **hba-id** *hba-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x9962_12256_x1835783263}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1708174883}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1496384446}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1693045960}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1937469503}

[[network-operator]{lang="EN-US"}]{#struct_0_x9962_12256_1164068052}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_x1427067145}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9962_12256_x1009915374}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_380435270}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_2040410577}[：显示指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库信息，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。不指定该参数时，将显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}

[**[hba-id]{lang="EN-US"}**[ *hba-id*]{lang="EN-US"}]{#struct_0_x9962_12256_461780952}[：显示指定]{style="font-family:宋体"}[HBA ID]{lang="EN-US"}[的]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库信息。]{style="font-family:宋体"}*[hba-id]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[xx:xx:xx:xx:xx:xx:xx:xx]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9962_12256_733486840}[：显示]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库的详细信息。不指定该参数时，将显示]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1937797183}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x2084202338}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[使用本命令可以查看]{style="font-family:宋体"}[FDMI]{lang="EN-US"}]{#struct_0_x9962_12256_433239777}[数据库信息，包括整个]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络中所有已经注册节点设备上的]{style="font-family:宋体"}[HBA]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1566531039}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_x1376970743}[显示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display fdmi database]{lang="EN-US"}]{#struct_0_x9962_12256_1937862719}

[Registered HBA List for VSAN 1:]{lang="EN-US"}

[  HBA ID                        Port WWNs]{lang="EN-US"}

[  21:00:00:11:22:00:01:02       21:00:00:11:22:00:01:02]{lang="EN-US"}

[                                21:00:00:c0:dd:13:cc:d6]{lang="EN-US"}

[                                21:00:00:c0:dd:13:cc:d7]{lang="EN-US"}

[  38:00:00:11:22:00:01:01       21:00:00:c0:dd:13:cc:d4]{lang="EN-US"}

[                                21:00:00:c0:dd:13:cc:d5]{lang="EN-US"}

[                                38:00:00:11:22:00:01:01]{lang="EN-US"}

[ ]{lang="EN-US"}

[Registered HBA List for VSAN 2:]{lang="EN-US"}

[  HBA ID                        Port WWNs]{lang="EN-US"}

[  38:00:00:11:22:00:01:01       21:00:00:c0:dd:13:cc:d4]{lang="EN-US"}

[                                21:00:00:c0:dd:13:cc:d5]{lang="EN-US"}

[                                38:00:00:11:22:00:01:01]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_22609224}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库内指定]{style="font-family:宋体"}[HBA]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display fdmi database vsan 1 hba-id 38:00:00:11:22:00:01:01]{lang="EN-US"}]{#struct_0_x9962_12256_x1400951589}

[  HBA ID                        Port WWNs]{lang="EN-US"}

[  38:00:00:11:22:00:01:01       21:00:00:c0:dd:13:cc:d4]{lang="EN-US"}

[                                21:00:00:c0:dd:13:cc:d5]{lang="EN-US"}

[                                38:00:00:11:22:00:01:01]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_71885656}[显示]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内的]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[数据库的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display fdmi database vsan 1 verbose]{lang="EN-US"}]{#struct_0_x9962_12256_1937666111}

[Registered HBA List for VSAN 1:]{lang="EN-US"}

[  HBA ID: 38:00:00:11:22:00:01:01]{lang="EN-US"}

[    Node WWN: 20:00:00:c0:dd:13:cc:d5]{lang="EN-US"}

[    Manufacturer: QLogic Corporation]{lang="EN-US"}

[    Serial num: RFC1001S63347]{lang="EN-US"}

[    Model: QLE8152]{lang="EN-US"}

[    Model description: QLogic QLE8152 Fibre Channel Adapter]{lang="EN-US"}

[    Hardware version: 2.1]{lang="EN-US"}

[    Driver version: 9.1.9.17]{lang="EN-US"}

[    ROM version: 3.00]{lang="EN-US"}

[    Firmware version: 5.04.01]{lang="EN-US"}

[    OS name/version: Microsoft Windows Server 2003 R2 for x86]{lang="EN-US"}

[    CT payload len: 2112]{lang="EN-US"}

[      Port WWN: 21:00:00:c0:dd:13:cc:d5]{lang="EN-US"}

[        Supported FC4 types: FCP]{lang="EN-US"}

[        Supported speed: 10Gbps]{lang="EN-US"}

[        Current speed: 10Gbps]{lang="EN-US"}

[        Maximum frame size: 2048]{lang="EN-US"}

[        OS device name: S05131F]{lang="EN-US"}

[        Host name: S05131F]{lang="EN-US"}

[[表1-62 ]{lang="EN-US"}[display fdmi database]{lang="EN-US"}]{#struct_0_x9962_12256_x1156502622}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1136401541}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1579561687}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1937731647}

[[Registered HBA List for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1520263133}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_x1460145756}[内的]{style="font-family:宋体"}[HBA]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[HBA ID]{lang="EN-US"}]{#struct_0_x9962_12256_x1964616667}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_1558652085}[的编号]{style="font-family:宋体"}

[[Port WWNs]{lang="EN-US"}]{#struct_0_x9962_12256_1938059327}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_1742226778}[上的端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-63 ]{lang="EN-US"}[display fdmi database verbose]{lang="EN-US"}]{#struct_0_x9962_12256_1278773368}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1129735793}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_1553574215}

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1950723584}

[[Registered HBA List for VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1938124863}

[[VSAN]{lang="EN-US"}]{#struct_0_x9962_12256_1371554450}[内的]{style="font-family:宋体"}[HBA]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[HBA ID]{lang="EN-US"}]{#struct_0_x9962_12256_1906247373}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_x1440316930}[的编号]{style="font-family:宋体"}

[[Node WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1097722317}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_1937535040}[所属]{style="font-family:宋体"}[N]{lang="EN-US"}[节点的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Manufacturer]{lang="EN-US"}]{#struct_0_x9962_12256_1596050797}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_x1480828763}[制造商信息]{style="font-family:宋体"}

[[Serial num]{lang="EN-US"}]{#struct_0_x9962_12256_1059999057}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_1937600576}[序列号]{style="font-family:宋体"}

[[Model]{lang="EN-US"}]{#struct_0_x9962_12256_x753986350}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_x1289472186}[型号]{style="font-family:宋体"}

[[Model description]{lang="EN-US"}]{#struct_0_x9962_12256_1951731922}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_x1032146921}[型号描述]{style="font-family:宋体"}

[[Hardware version]{lang="EN-US"}]{#struct_0_x9962_12256_1937403968}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_x25654992}[的硬件版本号]{style="font-family:宋体"}

[[Driver version]{lang="EN-US"}]{#struct_0_x9962_12256_x720690523}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_118948247}[的驱动程序版本号]{style="font-family:宋体"}

[[ROM version]{lang="EN-US"}]{#struct_0_x9962_12256_1937469504}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_1164133588}[的]{style="font-family:宋体"}[ROM]{lang="EN-US"}[版本号]{style="font-family:宋体"}

[[Firmware version]{lang="EN-US"}]{#struct_0_x9962_12256_1630843254}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_x1891530574}[的固件版本号]{style="font-family:宋体"}

[[OS name/version]{lang="EN-US"}]{#struct_0_x9962_12256_1937797184}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_433436385}[所在操作系统名称和版本号]{style="font-family:宋体"}

[[CT payload len]{lang="EN-US"}]{#struct_0_x9962_12256_1859941519}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_1937862720}[允许的]{style="font-family:宋体"}[CT]{lang="EN-US"}[负载的最大长度，包括]{style="font-family:宋体"}[CT]{lang="EN-US"}[类型报文的基本头和扩展头，但不包括]{style="font-family:宋体"}[FC]{lang="EN-US"}[头]{style="font-family:宋体"}

[[Port WWN]{lang="EN-US"}]{#struct_0_x9962_12256_22019403}

[[HBA]{lang="EN-US"}]{#struct_0_x9962_12256_x2124803133}[上的端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}

[[Supported FC4 types]{lang="EN-US"}]{#struct_0_x9962_12256_1161114258}

[[端口支持的]{style="font-family:宋体"}[FC4]{lang="EN-US"}]{#struct_0_x9962_12256_1937666112}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCP]{lang="EN-US"}]{#struct_0_x9962_12256_x1156437086}[：表示光纤通道协议]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_x9962_12256_163004836}[：表示互联网协议]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLC/SNAP]{lang="EN-US"}]{#struct_0_x9962_12256_1937731648}[：表示链路控制]{style="font-family:宋体"}[/]{lang="EN-US"}[子网访问协议]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SW_ILS]{lang="EN-US"}]{#struct_0_x9962_12256_x1519804381}[：表示]{style="font-family:宋体"}[交换机]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}[网内部链接服务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SNMP]{lang="EN-US"}]{#struct_0_x9962_12256_1596602777}[：表示简单网络管理协议]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GS3]{lang="EN-US"}]{#struct_0_x9962_12256_1938059328}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[通用服务]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VI]{lang="EN-US"}]{#struct_0_x9962_12256_1741899098}[：表示接口虚拟化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NPV]{lang="EN-US"}]{#struct_0_x9962_12256_2131450953}[：表示]{style="font-family:宋体"}[N]{lang="EN-US"}[端口虚拟化]{style="font-family:宋体"}

[[Supported speed]{lang="EN-US"}]{#struct_0_x9962_12256_1938124864}

[[端口支持的速率，包括：]{style="font-family:宋体"}[1Gbps]{lang="EN-US"}]{#struct_0_x9962_12256_1371095698}[、]{style="font-family:宋体"}[2Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[4Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[10Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[16Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[20Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[32Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[40Gbps]{lang="EN-US"}[（可包含其中一项或多项）。非以上速率则显示]{style="font-family:宋体"}[Unknown]{lang="EN-US"}

[[如果不能确定端口支持的速率，则显示为]{style="font-family:宋体"}[Speed not established]{lang="EN-US"}]{#struct_0_x9962_12256_x464678193}

[[Current speed]{lang="EN-US"}]{#struct_0_x9962_12256_842300597}

[[端口当前的速率，包括：]{style="font-family:宋体"}[1Gbps]{lang="EN-US"}]{#struct_0_x9962_12256_1937535037}[、]{style="font-family:宋体"}[2Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[4Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[8Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[10Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[16Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[20Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[32Gbps]{lang="EN-US"}[、]{style="font-family:宋体"}[40Gbps]{lang="EN-US"}[（只可包含其中一项）。非以上速率则显示]{style="font-family:宋体"}[Unknown]{lang="EN-US"}

[[如果不能确定端口当前的速率，则显示为]{style="font-family:宋体"}[Speed not established]{lang="EN-US"}]{#struct_0_x9962_12256_1596116336}

[[Maximum frame size]{lang="EN-US"}]{#struct_0_x9962_12256_1937600573}

[[端口支持的最大帧大小]{style="font-family:宋体"}]{#struct_0_x9962_12256_x754182958}

[[OS device name]{lang="EN-US"}]{#struct_0_x9962_12256_x245298998}

[[端口所在操作系统的名称]{style="font-family:宋体"}]{#struct_0_x9962_12256_1937403965}

[[Host name]{lang="EN-US"}]{#struct_0_x9962_12256_x25851600}

[[端口所在]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x9962_12256_x2036844856}[节点设备的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#40757388 .myid}
[]{#_Toc404798234}[]{#struct_0_x9962_12256_1937469501}[]{#_Toc297038090}

**FC和FCoE \-- FC Ping配置命令 \-- fcping**

------------------------------------------------------------------------

[**[fcping]{lang="EN-US"}**]{#struct_0_x9962_12256_1163936980}[命令用来检查指定目的地址是否可达，并输出相应的统计信息。]{style="font-family:宋体"}

[[在执行命令过程中，键入]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_x9962_12256_x932049329}[可终止]{style="font-family:宋体"}[FC Ping]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1370952174}

[**[fcping]{lang="EN-US"}**[ \[ **-c** *count* \| **-t** *timeout* \] \* **fcid** *fcid* **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_x1231938279}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_793295672}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_1815483210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x918509873}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_1937797181}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_433108705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1290510916}

[**[-c]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_x9962_12256_x317564917}[：指定发送]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[请求报文的个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。其中，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示连续发送直到用户手动停止。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}**[ *timeout*]{lang="EN-US"}]{#struct_0_x9962_12256_x780819221}[：指定]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[回应报文的超时时间。发送]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[后还没有收到]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[回应报文，源端则认为]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[回应报文超时。]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[fcid]{lang="EN-US"}***[ fcid]{lang="EN-US"}*]{#struct_0_x9962_12256_x940305102}[：目的地址。当目的端为]{style="font-family:宋体"}[N]{lang="EN-US"}[节点时，]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[的值就是该节点的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址。当目的端为交换机时，]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[为该交换机的域控制器地址]{style="font-family:宋体"}[FFFCxx]{lang="EN-US"}[，]{style="font-family:宋体"}[xx]{lang="EN-US"}[为目的交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。例如：目的交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[，则域控制器地址为]{style="font-family:
宋体"}[FFFC03]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[vsan]{lang="EN-US"}***[ vsan-id]{lang="EN-US"}*]{#struct_0_x9962_12256_1917367068}[：]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x2131190969}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x2084136802}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1061648865}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1937862717}[检查]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内目的地址为]{style="font-family:宋体"}[FFFC02]{lang="EN-US"}[的设备是否可达。]{style="font-family:宋体"}

[[\<Sysname\> fcping fcid fffc02 vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_22478152}

[FCPING fcid 0xfffc02: 128 data bytes, press CTRL_C to break.]{lang="EN-US"}

[Reply from 0xfffc02: bytes = 128 time = 1.281 ms]{lang="EN-US"}

[Reply from 0xfffc02: bytes = 128 time = 0.890 ms ]{lang="EN-US"}

[Reply from 0xfffc02: bytes = 128 time = 0.889 ms ]{lang="EN-US"}

[Reply from 0xfffc02: bytes = 128 time = 0.892 ms]{lang="EN-US"}

[Reply from 0xfffc02: bytes = 128 time = 0.894 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- 0xfffc02 fcping statistics \-\--]{lang="EN-US"}

[5 packet(s) transmitted]{lang="EN-US"}

[5 packet(s) received]{lang="EN-US"}

[0.00% packet loss]{lang="EN-US"}

[round-trip min/avg/max = 0.889/0.969/1.281 ms]{lang="EN-US"}

[[\# FC Ping]{lang="EN-US"}]{#struct_0_x9962_12256_91477471}[时报文发送失败。]{style="font-family:宋体"}

[[\<Sysname\> fcping fcid fffc01 vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_1937666109}

[FCPING fcid 0xfffc01: 128 data bytes, press CTRL_C to break.]{lang="EN-US"}

[fcping: sendto: No route to host]{lang="EN-US"}

[fcping: sendto: No route to host]{lang="EN-US"}

[fcping: sendto: \^C]{lang="EN-US"}

[\-\-- 0xfffc01 fcping statistics \-\--]{lang="EN-US"}

[3 packet(s) transmitted]{lang="EN-US"}

[0 packet(s) received]{lang="EN-US"}

[100.00% packet loss]{lang="EN-US"}

[[表1-64 ]{lang="EN-US"}[fcping]{lang="EN-US"}]{#struct_0_x9962_12256_x1155978333}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1126273189}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_2082973749}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1489564937}

[[FCPING fcid 0xfffc02]{lang="EN-US"}]{#struct_0_x9962_12256_1937731645}

[[检查目的地址为]{style="font-family:宋体"}[FFFC02]{lang="EN-US"}]{#struct_0_x9962_12256_x1520132061}[的设备是否可达]{style="font-family:宋体"}

[[128 data bytes]{lang="EN-US"}]{#struct_0_x9962_12256_x1235984918}

[[每个]{style="font-family:宋体"}[ECHO]{lang="EN-US"}]{#struct_0_x9962_12256_1491617843}[请求报文中的数据字节数]{style="font-family:宋体"}

[[press CTRL_C to break]{lang="EN-US"}]{#struct_0_x9962_12256_714001666}

[[在执行命令过程中，键入]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_x9962_12256_1938059325}[可终止]{style="font-family:宋体"}[FC Ping]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[Reply from 0xfffc02: bytes = 128 time = 0.892 ms]{lang="EN-US"}]{#struct_0_x9962_12256_1742095706}

[[收到目的地址为]{style="font-family:宋体"}[0xfffc02]{lang="EN-US"}]{#struct_0_x9962_12256_890365444}[的设备回复的]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[回应报文：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_x9962_12256_x420343903}[表示]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[回应报文中的数据字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[time]{lang="EN-US"}]{#struct_0_x9962_12256_x698786104}[表示响应时间]{style="font-family:宋体"}

[[Request time out]{lang="EN-US"}]{#struct_0_x9962_12256_1938124861}

[[ECHO]{lang="EN-US"}]{#struct_0_x9962_12256_1371423378}[请求报文发送成功，超时时间内未收到]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[回应报文]{style="font-family:宋体"}

[[fcping: sendto: No route to host]{lang="EN-US"}]{#struct_0_x9962_12256_1111795995}

[[ECHO]{lang="EN-US"}]{#struct_0_x9962_12256_1332961934}[请求报文发送失败]{style="font-family:宋体"}

[[\-\-- 0xfffc02 fcping statistics \-\--]{lang="EN-US"}]{#struct_0_x9962_12256_1937535038}

[[FC Ping]{lang="EN-US"}]{#struct_0_x9962_12256_1596575088}[操作中收发报文的统计结果]{style="font-family:宋体"}

[[5 packet(s) transmitted]{lang="EN-US"}]{#struct_0_x9962_12256_x1071335966}

[[发送的]{style="font-family:宋体"}[ECHO]{lang="EN-US"}]{#struct_0_x9962_12256_1391544371}[请求报文数]{style="font-family:宋体"}

[[5 packet(s) received]{lang="EN-US"}]{#struct_0_x9962_12256_1937600574}

[[收到的]{style="font-family:宋体"}[ECHO]{lang="EN-US"}]{#struct_0_x9962_12256_x753855278}[回应报文数]{style="font-family:宋体"}

[[0.00% packet loss]{lang="EN-US"}]{#struct_0_x9962_12256_x547640316}

[[未收到]{style="font-family:宋体"}[ECHO]{lang="EN-US"}]{#struct_0_x9962_12256_1564742032}[回应报文的]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[请求报文占发送的总]{style="font-family:宋体"}[ECHO]{lang="EN-US"}[请求报文的百分比]{style="font-family:宋体"}

[[round-trip min/avg/max = 0.889/0.969/1.281 ms]{lang="EN-US"}]{#struct_0_x9962_12256_1937403966}

[[响应时间的最小值、平均值和最大值，单位为毫秒]{style="font-family:宋体"}]{#struct_0_x9962_12256_x26048208}

[ ]{lang="EN-US"}

::: {#650229491 .myid}
[]{#_Toc404798236}[]{#struct_0_x9962_12256_x1071569232}[]{#_Toc324769866}[]{#_Toc320777318}

**FC和FCoE \-- FC Tracert配置命令 \-- fctracert**

------------------------------------------------------------------------

[**[fctracert]{lang="EN-US"}**]{#struct_0_x9962_12256_x1175909419}[命令用来探测本端到目的端的双向路由信息，目的端可以为]{style="font-family:宋体"}[N]{lang="EN-US"}[节点或交换机。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x61781013}

[**[fctracert]{lang="EN-US"}**[ \[ **-t** *timeout* \] **fcid** *fcid* **vsan** *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1937469502}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9962_12256_1164002516}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1095353087}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9962_12256_328026860}

[[network-admin]{lang="EN-US"}]{#struct_0_x9962_12256_355322326}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9962_12256_772521593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9962_12256_678739017}

[**[-t]{lang="EN-US"}***[ timeout]{lang="EN-US"}*]{#struct_0_x9962_12256_1937797182}[：整个探测过程的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[fcid]{lang="EN-US"}**[ *fcid*]{lang="EN-US"}]{#struct_0_x9962_12256_433305313}[：目的地址。当目的端为]{style="font-family:宋体"}[N]{lang="EN-US"}[节点时，]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[的值就是该节点的]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址。当目的端为交换机时，]{style="font-family:宋体"}*[fcid]{lang="EN-US"}*[为该交换机的域控制器地址]{style="font-family:宋体"}[FFFCxx]{lang="EN-US"}[，]{style="font-family:宋体"}[xx]{lang="EN-US"}[为目的交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。例如：目的交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[，则域控制器地址为]{style="font-family:
宋体"}[FFFC03]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x9962_12256_1569027250}[：指定所属]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x1688239091}

[[只有]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x9962_12256_x161756965}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机支持本命令。]{style="font-family:宋体"}

[[通过本命令可以获取本端到目的端的双向路由信息，包括从本端到目的端往返所经过的所有交换机的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_395017861}[和域控制器地址。设备支持往返两端双向的最大跳数为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在执行命令过程中，键入]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_x9962_12256_x314588855}[可终止此次]{style="font-family:宋体"}[fctracert]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9962_12256_x248547493}

[[\# ]{lang="EN-US"}]{#struct_0_x9962_12256_1937862718}[探测在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内本端到]{style="font-family:宋体"}[FC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0xd70000]{lang="EN-US"}[的节点的双向路由信息。]{style="font-family:宋体"}

[[\<Sysname\> fctracert fcid d70000 vsan 1]{lang="EN-US"}]{#struct_0_x9962_12256_22543688}

[Route present for: 0xd70000, press CTRL_C to break.]{lang="EN-US"}

[20:00:00:0b:46:00:02:82(0xfffcd5)]{lang="EN-US"}

[20:00:00:05:30:00:18:db(0xfffcd7)]{lang="EN-US"}

[20:00:00:05:30:00:18:db(0xfffcd7)]{lang="EN-US"}

[20:00:00:0b:46:00:02:82(0xfffcd5)]{lang="EN-US"}

[Fctracert completed.]{lang="EN-US"}

[[表1-65 ]{lang="EN-US"}[fctracert]{lang="EN-US"}]{#struct_0_x9962_12256_x850609720}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1155674193}[[字段]{style="font-family:黑体"}]{#struct_0_x9962_12256_x491707642}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9962_12256_1862703839}

[[Route present for]{lang="EN-US"}]{#struct_0_x9962_12256_1937666110}

[[查看从当前设备到目的地址设备所经过的路径]{style="font-family:宋体"}]{#struct_0_x9962_12256_x1156568158}

[[press CTRL_C to break]{lang="EN-US"}]{#struct_0_x9962_12256_x852719832}

[[在执行命令过程中，键入]{style="font-family:宋体"}[\<Ctrl+C\>]{lang="EN-US"}]{#struct_0_x9962_12256_1356538604}[可终止操作]{style="font-family:宋体"}

[[20:00:00:0b:46:00:02:82]{lang="EN-US"}]{#struct_0_x9962_12256_2136983878}

[[设备的]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x9962_12256_1937731646}[值]{style="font-family:宋体"}

[[0xfffcd5]{lang="EN-US"}]{#struct_0_x9962_12256_x1520197597}

[[设备的域控制器地址]{style="font-family:宋体"}[FFFCxx]{lang="EN-US"}]{#struct_0_x9962_12256_x183446027}[，]{style="font-family:宋体"}[xx]{lang="EN-US"}[为交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Fctracert completed.]{lang="EN-US"}]{#struct_0_x9962_12256_x290378206}

[[FC Tracert]{lang="EN-US"}]{#struct_0_x9962_12256_1938059326}[命令执行完成]{style="font-family:宋体"}

[[Fctracert uncompleted.]{lang="EN-US"}]{#struct_0_x9962_12256_1742292314}

[[FC Tracert]{lang="EN-US"}]{#struct_0_x9962_12256_89086690}[命令执行未完成，原因如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[resource is not enough]{lang="EN-US"}]{#struct_0_x9962_12256_x747622809}[：资源不足]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[max hops reached]{lang="DE"}]{#struct_0_x9962_12256_202057817}[：]{lang="EN-US" style="font-family:宋体"}[已达到最大跳数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fabric is being built]{lang="DE"}]{#struct_0_x9962_12256_1938124862}[：]{lang="EN-US" style="font-family:
  宋体"}[Fabric]{lang="EN-US"}[网络正在建立]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no route to destination port]{lang="DE"}]{#struct_0_x9962_12256_1371488914}[：]{lang="EN-US" style="font-family:宋体"}[没有到目的端的路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[destination port is not in fabric]{lang="DE"}]{#struct_0_x9962_12256_396726186}[：]{lang="EN-US" style="font-family:宋体"}[目的端不在该]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[destination port and source port are not in the same zone]{lang="DE"}]{#struct_0_x9962_12256_442679201}[：]{lang="EN-US" style="font-family:宋体"}[目的端与源端不在同一个]{lang="EN-US" style="font-family:
  宋体"}[Zone]{lang="EN-US"}

[[Fctracert timeout.]{lang="EN-US"}]{#struct_0_x9962_12256_1937535035}

[[探测超时]{style="font-family:宋体"}]{#struct_0_x9962_12256_1596247408}

[[Service is unavailable.]{lang="DE"}]{#struct_0_x9962_12256_x1467429495}

[[FC Tracert]{lang="EN-US"}]{#struct_0_x9962_12256_1937600571}[服务未启动或者内部处理失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}
