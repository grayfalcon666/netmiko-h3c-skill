::: {#1615690736 .myid}
[]{#_Toc291226679}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404794845}[]{#struct_0_x2117_18423_x29612415}[]{#_Toc373753289}[]{#_Toc366004707}[]{#_Toc365981338}

**射频管理 \-- 射频管理命令 \-- a-mpdu enable**

------------------------------------------------------------------------

[**[a-mpdu enable]{lang="EN-US"}**]{#struct_0_x2117_18423_48822283}[命令用来开启]{style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[a-mpdu disable]{lang="EN-US"}**]{#struct_0_x2117_18423_x41041348}[命令用来关闭]{style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo a-mpdu]{lang="EN-US"}**]{#struct_0_x2117_18423_110654676}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_389811319}

[**[a-mpdu]{lang="EN-US"}**[ { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_x2117_18423_x633081292}

[**[undo a-mpdu]{lang="EN-US"}**]{#struct_0_x2117_18423_x2034930420}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1288127140}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1724465726}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1544968563}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能处于开启状态。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_231666316}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x342516969}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_415126927}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1229700972}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x2034908031}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1641862664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1595696356}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1540180825}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令仅对]{style="font-family:宋体"}]{#struct_0_x2117_18423_1136477112}[802.11n]{lang="EN-US"}[或]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[模式的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[有效。当进行]{style="font-family:宋体"}[Radio]{lang="EN-US"}[模式切换时，]{style="font-family:宋体"}[Radio]{lang="EN-US"}[会恢复该功能的缺省情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x494094651}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1956509608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_57758891}[设备]{lang="EN-US" style="font-family:
宋体"}[举例]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x318960821}[关闭]{style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x953822464}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] a-mpdu disable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_1137248725}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x1284523469}[关闭]{style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x2117_18423_x1059216432}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] a-mpdu disable]{lang="EN-US"}
:::

::: {#932477936 .myid}
[]{#_Toc404794846}[]{#struct_0_x2117_18423_x603956972}

**射频管理 \-- 射频管理命令 \-- a-msdu enable**

------------------------------------------------------------------------

[**[a-msdu enable]{lang="EN-US"}**]{#struct_0_x2117_18423_1674369785}[命令用来开启]{style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[a-msdu disable]{lang="EN-US"}**]{#struct_0_x2117_18423_x332063826}[命令用来关闭]{style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo a-msdu]{lang="EN-US"}**]{#struct_0_x2117_18423_x1548642189}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1642152284}

[**[a-msdu]{lang="EN-US"}**[ { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_x2117_18423_1237866436}

[**[undo a-msdu]{lang="EN-US"}**]{#struct_0_x2117_18423_x11392290}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_865855948}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1962578295}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1060688209}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能处于开启状态。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_1103503847}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_333491880}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x519196598}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_486062918}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x481816758}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_946548383}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1983565506}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1767129642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令仅对]{style="font-family:宋体"}]{#struct_0_x2117_18423_1180241166}[802.11n]{lang="EN-US"}[和]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[模式的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[有效。在进行]{style="font-family:宋体"}[Radio]{lang="EN-US"}[模式切换的时候，设备会恢复该]{style="font-family:宋体"}[功能在该模式下的缺省情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目前，设备只支持接收]{style="font-family:宋体"}]{#struct_0_x2117_18423_x1732449199}[A-MSDU]{lang="EN-US"}[报文，不支持发送]{style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1566164524}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_62334490}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1251724110}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1388523864}[关闭]{style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1853555246}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] a-msdu disable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_597351779}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_53177192}[关闭]{style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x2117_18423_x822336216}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] a-msdu disable]{lang="EN-US"}
:::

::: {#-1700297684 .myid}
[]{#_Toc404794847}[]{#struct_0_x2117_18423_1457164057}[]{#_Toc393205674}[]{#_Toc384717985}[]{#_Toc346719918}

**射频管理 \-- 射频管理命令 \-- ap-model**

------------------------------------------------------------------------

[**[ap-model]{lang="EN-US" style="color:black"}**]{#struct_0_x2117_18423_x825208181}[命令用来创建并进入]{style="font-family:宋体"}[AP]{lang="EN-US"}[组下的]{style="font-family:宋体"}[AP]{lang="EN-US"}[型号视图。]{style="font-family:宋体"}

[**[undo ap-model]{lang="EN-US" style="color:black"}**]{#struct_0_x2117_18423_x995252858}[命令用来删除组下]{style="font-family:宋体"}[AP]{lang="EN-US"}[型号视图及]{style="font-family:宋体"}[AP]{lang="EN-US"}[型号下的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1271719298}

[**[ap-model ]{lang="EN-US" style="color:black"}***[ap-model]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_18423_x426005694}

[**[undo ap-model ]{lang="EN-US" style="color:black"}***[ap-model]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_18423_1240113818}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1218654435}

[[没有]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1092264249}[型号配置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_903339554}

[[AP]{lang="EN-US"}]{#struct_0_x2117_18423_x823792581}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_331999929}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_578497474}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1655294002}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_938153802}

[*[ap-model]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_18423_1100999233}[：]{style="font-family:宋体;color:black"}[AP]{lang="EN-US" style="color:black"}[型号名。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1923955765}

[[在]{style="font-family:宋体;color:black"}[ap-model]{lang="EN-US" style="color:black"}]{#struct_0_x2117_18423_x1048193814}[视图下可以进入]{style="font-family:
宋体;color:black"}[radio]{lang="EN-US" style="color:black"}[视图，在此视图下可以配置]{style="font-family:宋体;color:black"}[radio]{lang="EN-US" style="color:black"}[的物理参数。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x506119354}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1267141196}[在]{style="font-family:宋体"}[AP]{lang="EN-US"}[组视图下设置]{style="font-family:宋体"}[AP]{lang="EN-US"}[的型号为]{style="font-family:宋体"}[WA4620i-ACN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<System\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_433637441}

[\[System\] wlan ap-group group1]{lang="EN-US"}

[\[System-wlan-ap-group-group1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[System-wlan-ap-group-group1-apmodel-WA4620i-ACN\]]{lang="EN-US"}
:::

::: {#-85123487 .myid}
[]{#_Toc404794848}[]{#struct_0_x2117_18423_x842852414}[]{#_Toc401582031}[]{#_Toc396742884}

**射频管理 \-- 射频管理命令 \-- beacon-interval**

------------------------------------------------------------------------

[**[beacon-interval]{lang="EN-US"}**]{#struct_0_x2117_18423_2018584731}[命令用来配置发送]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧的时间间隔。]{style="font-family:宋体"}

[**[undo beacon-interval]{lang="EN-US"}**]{#struct_0_x2117_18423_1364839216}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_770122374}

[**[beacon-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x2117_18423_x1192346293}

[**[undo beacon-interval]{lang="EN-US"}**]{#struct_0_x2117_18423_71389659}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_282181018}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1881659809}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1818778646}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，发送]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧的时间间隔为]{style="font-family:宋体"}[100TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x2058471632}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，发送]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧的时间间隔为]{style="font-family:宋体"}[100TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1864483945}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1714883532}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x237011791}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x2117_18423_x758517}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_487383952}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1095632167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1124691759}

[*[interval]{lang="EN-US"}*]{#struct_0_x2117_18423_629712948}[：发送]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧的时间间隔，取值范围为]{style="font-family:宋体"}[32]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[TU]{lang="EN-US"}[（]{style="font-family:宋体"}[Time Unit]{lang="EN-US"}[，]{style="font-family:宋体"}[1TU=1024]{lang="EN-US"}[微秒）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_908730716}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1536537062}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1185396388}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1993056061}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x1394733397}[配置发送]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧的时间间隔为]{style="font-family:宋体"}[1000TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1402088359}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] beacon-interval 1000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1805072187}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x224941269}[配置发送]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧的时间间隔为]{style="font-family:宋体"}[1000TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1903392338}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] beacon-interval 1000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_1221999322}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_922831914}[配置发送]{style="font-family:宋体"}[Beacon]{lang="EN-US"}[帧的时间间隔为]{style="font-family:宋体"}[1000TU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1558735738}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] type dot11g]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] beacon-interval 1000]{lang="EN-US"}
:::

::: {#470911652 .myid}
[]{#_Toc404794849}[]{#struct_0_x2117_18423_1530650021}[]{#_Toc401582032}[]{#_Toc396742886}

**射频管理 \-- 射频管理命令 \-- channel**

------------------------------------------------------------------------

[**[channel]{lang="EN-US"}**]{#struct_0_x2117_18423_x16837418}[命令用来配置射频工作信道。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **channel**]{lang="EN-US"}]{#struct_0_x2117_18423_1939821589}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1414963072}

[]{#struct_0_x2117_18423_1416341040}[]{#_Hlt20797640}**[channel]{lang="IT"}**[ { *channel-number* \| **auto** ]{lang="IT"}[{ **lock** \| **unlock** } ]{lang="EN-US"}[}]{lang="IT"}

[**[undo channel]{lang="IT"}**]{#struct_0_x2117_18423_x1443852119}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_973071329}

[[AC]{lang="IT"}]{#struct_0_x2117_18423_x2115524749}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}[Radio]{lang="IT"}[视图下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[继承]{style="font-family:宋体"}[AP]{lang="IT"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="IT"}]{#struct_0_x2117_18423_x533352305}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}[AP]{lang="IT"}[组]{style="font-family:宋体"}[Radio]{lang="IT"}[视图下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[工作信道为]{style="font-family:宋体"}**[auto]{lang="IT"}**[模式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[信道为]{style="font-family:宋体"}[unlock]{lang="IT"}[模式。]{style="font-family:宋体"}

[[FAT AP]{lang="IT"}]{#struct_0_x2117_18423_x522990713}[设备]{style="font-family:宋体"}[：]{style="font-family:
宋体"}[Radio]{lang="IT"}[接口视图]{style="font-family:宋体"}[下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[工作信道为]{style="font-family:宋体"}**[auto]{lang="IT"}**[模式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[信道为]{style="font-family:宋体"}[unlock]{lang="IT"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_879559099}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_138310121}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_756476911}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x925955774}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x15686681}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_57161578}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1955698304}

[*[channel-number]{lang="EN-US"}*]{#struct_0_x2117_18423_373737648}[：手动配置的射频工作信道。取值范围由国家码和射频类型决定。]{style="font-family:宋体"}

[**[auto lock]{lang="EN-US"}**]{#struct_0_x2117_18423_x520215799}[：自动选择信道并加锁模式，由设备根据实际环境自动选择最优信道，并将该信道锁定。]{style="font-family:宋体"}

[**[auto unlock]{lang="EN-US"}**]{#struct_0_x2117_18423_265986781}[：]{style="font-family:宋体"}[自动选择信道并解锁模]{style="font-family:宋体"}[式。]{style="font-family:宋体"}[由设备根据实际环境自动选择最优信道，并将该信道设置为无锁模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1567942377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[channel]{lang="EN-US"}**[ *channel-number*]{lang="EN-US"}]{#struct_0_x2117_18423_x1849672737}[、]{style="font-family:宋体"}**[chanel auto lock]{lang="EN-US"}**[和]{style="font-family:宋体"}**[channel auto unlock]{lang="EN-US"}**[此三条命令互斥，任何一条命令都可以将前一条配置覆盖。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在手工指定工作信道模式时，如果在当前工作信道上发现雷达信号，则设备会立即将工作信道调整至其他信道。雷达信号消失后，设备会恢复到指定的工作信道上。]{style="font-family:宋体"}]{#struct_0_x2117_18423_265071529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在自动选择信道模式上，无论是信道的加锁与否，如果在当前工作信道上发现雷达信号，则设备会立即将工作信道调整至其他信道。]{style="font-family:宋体"}]{#struct_0_x2117_18423_x1377185438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1880045202}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_860918299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x780774300}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_1340479352}[配置射频]{style="font-family:宋体"}[工作]{style="font-family:宋体"}[信道号为]{style="font-family:宋体"}[149]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_x718054208}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] channel 149]{lang="IT"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x843209692}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x390518250}[配置射频]{style="font-family:宋体"}[工作]{style="font-family:宋体"}[信道号为]{style="font-family:宋体"}[149]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1133252535}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] ]{lang="EN-US"}[channel 149]{lang="IT"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="IT"}]{#struct_0_x2117_18423_891682448}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_650310170}[配置射频工作信道号为]{style="font-family:宋体"}[6]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_780499614}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="IT"}

[\[Sysname-WLAN-Radio1/0/2\] channel 6]{lang="IT"}
:::

::: {#1319754360 .myid}
[]{#_Toc404794850}[]{#struct_0_x2117_18423_341484346}[]{#_Toc403564719}[]{#_Toc393198059}

**射频管理 \-- 射频管理命令 \-- channel band-width**

------------------------------------------------------------------------

[**[channel band-width]{lang="EN-US"}**]{#struct_0_x2117_18423_x2112905884}[命令用来设置带宽模式。]{style="font-family:宋体"}

[**[undo channel band-width]{lang="EN-US"}**]{#struct_0_x2117_18423_x1805396968}[命令用来恢复缺省情况**。**]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1579705184}

[**[channel band-width ]{lang="EN-US"}**[{ **20** \| **40** \| **80** \| **auto-switch** }]{lang="EN-US"}]{#struct_0_x2117_18423_x1140485506}

[**[undo channel band-width]{lang="EN-US"}**]{#struct_0_x2117_18423_1907568287}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1297598503}

[[AC]{lang="IT"}]{#struct_0_x2117_18423_1278391090}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}[Radio]{lang="IT"}[视图下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="IT"}]{#struct_0_x2117_18423_x1577992056}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}[AP]{lang="IT"}[组]{style="font-family:宋体"}[Radio]{lang="IT"}[视图下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[射频模式的带宽模式为]{style="font-family:宋体"}[80MHz]{lang="EN-US"}[，]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[射频模式的带宽模式为]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[，]{style="font-family:宋体"}[802.11gn]{lang="EN-US"}[射频模式的带宽模式为]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[FAT AP]{lang="IT"}]{#struct_0_x2117_18423_x632820277}[设备]{style="font-family:宋体"}[：]{style="font-family:
宋体"}[Radio]{lang="IT"}[接口视图]{style="font-family:宋体"}[下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[射频模式的带宽模式为]{style="font-family:宋体"}[80MHz]{lang="EN-US"}[，]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[射频模式的带宽模式为]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[，]{style="font-family:宋体"}[802.11gn]{lang="EN-US"}[射频模式的带宽模式为]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_701948693}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1017981970}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1297293673}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1913448046}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1849710219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x821315068}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_861840172}

[**[20]{lang="EN-US"}**]{#struct_0_x2117_18423_191343024}[：将带宽模式设置成]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[40]{lang="EN-US"}**]{#struct_0_x2117_18423_1718944925}[：将带宽模式设置成]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[80]{lang="EN-US"}**]{#struct_0_x2117_18423_x882715029}[：将带宽模式设置成]{style="font-family:宋体"}[80MHz]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auto-switch]{lang="EN-US"}**]{#struct_0_x2117_18423_x756511722}[：允许在]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[和]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[之间自动切换。仅当]{style="font-family:宋体"}[Radio]{lang="EN-US"}[模式为]{style="font-family:宋体"}[dot11gn]{lang="EN-US"}[模式时，支持配置本参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1109491152}

[[该命令仅对]{style="font-family:宋体"}[802.11n]{lang="EN-US"}]{#struct_0_x2117_18423_1796904956}[或]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[有效。在进行]{style="font-family:宋体"}[Radio]{lang="EN-US"}[模式切换的时候，带宽恢复切换模式下的缺省值。]{style="font-family:宋体"}

[[在指定带宽为]{style="font-family:宋体"}[40MHz]{lang="EN-US"}]{#struct_0_x2117_18423_x1977079308}[情况下，如果找到两条可以绑定到一起的相邻信道，那么使用]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[带宽；如果找不到可以绑定的相邻信道，那么实际只能使用]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[带宽。]{style="font-family:宋体"}

[[在指定带宽为]{style="font-family:宋体"}[80MHz]{lang="EN-US"}]{#struct_0_x2117_18423_939625802}[情况下，如果找到一组可以绑定为]{style="font-family:宋体"}[80MHz]{lang="EN-US"}[的相邻信道，那么使用]{style="font-family:宋体"}[80MHz]{lang="EN-US"}[带宽；如果找不到可以绑定为]{style="font-family:宋体"}[80MHz]{lang="EN-US"}[的一组信道，但可以找到两条可以绑定为]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[带宽的信道，那么使用]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[带宽；如果找不到可以绑定的信道，那么实际只能使用]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[带宽。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x884289123}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1457229593}[配置]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[带宽。]{style="font-family:宋体"}

[[\<AC\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_310465927}

[\[AC\] wlan ap ap1 model WA2620i-AGN]{lang="EN-US"}

[\[AC-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[AC-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[AC-wlan-ap-ap1-radio-1\] channel band-width 40]{lang="EN-US"}

[ ]{lang="EN-US"}
:::

::: {#1949292037 .myid}
[]{#_Toc404794851}[]{#struct_0_x2117_18423_x285346689}

**射频管理 \-- 射频管理命令 \-- client dot11n-only enable**

------------------------------------------------------------------------

[**[client dot11n-only enable]{lang="EN-US"}**]{#struct_0_x2117_18423_1192242631}[命令用来]{style="font-family:
宋体"}[开启仅允许]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入的]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[client dot11n-only disable]{lang="EN-US"}**]{#struct_0_x2117_18423_1817014198}[命令用来]{style="font-family:
宋体"}[关闭仅允许]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入的]{style="font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[undo client dot11n-only]{lang="EN-US"}**]{#struct_0_x2117_18423_x1459824760}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1219961092}

[**[client dot11n-only]{lang="EN-US"}**[ { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_x2117_18423_67866476}

[**[undo client dot11n-only]{lang="EN-US"}**]{#struct_0_x2117_18423_x1161182053}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x2125529779}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_12628111}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x758794078}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[允许]{style="font-family:宋体"}[802.11a]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入；]{style="font-family:宋体"}[802.11gn]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[允许]{style="font-family:宋体"}[802.11b/g]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11gn]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入；]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[允许]{style="font-family:宋体"}[802.11a]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x432831406}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[允许]{style="font-family:宋体"}[802.11a]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入；]{style="font-family:宋体"}[802.11gn]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[允许]{style="font-family:宋体"}[802.11b/g]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11gn]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入；]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[允许]{style="font-family:宋体"}[802.11a]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1253142140}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1887779776}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1321318693}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x612075953}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1015230342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_115279211}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1405107067}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行]{lang="EN-US" style="font-family:宋体"}**[client dot11n-only enable]{lang="EN-US"}**]{#struct_0_x2117_18423_84902302}[命令后，只有]{lang="EN-US" style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[802.11ac]{lang="EN-US"}[的客户端才能接入]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[。如果用户需要兼容]{lang="EN-US" style="font-family:宋体"}[802.11a/b/g]{lang="EN-US"}[的客户端，同时还要接入]{lang="EN-US" style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[802.11ac]{lang="EN-US"}[的客户端，则必须关闭]{lang="EN-US" style="font-family:宋体"}**[client dot11n-only]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[client dot11n-only enable]{lang="EN-US"}**]{#struct_0_x2117_18423_x1775744581}[命令前，需要先配置]{lang="EN-US" style="font-family:宋体"}[802.11n]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[MCS]{lang="EN-US"}[的最大索引。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1696879294}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1648203618}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_2009278047}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1980873723}[开启仅允许]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x29546879}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] client dot11n-only enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1360756396}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x273072321}[开启仅允许]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[用户接入的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x2117_18423_x743904557}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] client dot11n-only enable]{lang="EN-US"}
:::

::: {#1687654930 .myid}
[]{#_Toc404794852}[]{#struct_0_x2117_18423_719919356}[]{#_Toc393383825}[]{#_Toc403999219}

**射频管理 \-- 射频管理命令 \-- display wlan ap-model**

------------------------------------------------------------------------

[**[display wlan ap-model]{lang="EN-US"}**]{#struct_0_x2117_18423_x1729240779}[命令用来显示]{style="font-family:宋体"}[AP]{lang="EN-US"}[型号的信息。]{style="font-family:宋体"}[]{#_Toc403999220}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_271042351}[]{#_Toc403999221}

[**[display wlan ap-model]{lang="EN-US"}**[ { **all** \| **name** *model-name* }]{lang="EN-US"}]{#struct_0_x2117_18423_2090310485}[]{#_Toc403999222}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1749136495}[]{#_Toc403999223}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2117_18423_x312231067}[]{#_Toc403999224}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x2065998502}[]{#_Toc403999225}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x846164585}[]{#_Toc403999226}

[[network-operator]{lang="EN-US"}]{#struct_0_x2117_18423_955203159}[]{#_Toc403999227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1189491194}[]{#_Toc403999228}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2117_18423_x1903479867}[]{#_Toc403999229}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1620322693}[]{#_Toc403999230}

[**[all]{lang="EN-US"}**]{#struct_0_x2117_18423_x138391968}[：显示所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[型号的信息。]{style="font-family:宋体"}[]{#_Toc403999231}

[**[name ]{lang="EN-US"}***[model-name]{lang="EN-US"}*]{#struct_0_x2117_18423_x1511166563}[：显示指定]{style="font-family:宋体;color:black"}[AP]{lang="EN-US" style="color:black"}[型号的信息。]{style="font-family:宋体;color:black"}[]{#_Toc403999232}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x945556989}[]{#_Toc403999233}

[[\<Sysname\> display wlan ap-model name WA2620i-AGN]{lang="EN-US"}]{#struct_0_x2117_18423_1882718770}[]{#_Toc403999234}

[AP model        : WA2620i-AGN[]{#_Toc403999235}]{lang="EN-US"}

[Alias           : WA2620i-AGN[]{#_Toc403999236}]{lang="EN-US"}

[Vendor name     : H3C[]{#_Toc403999237}]{lang="EN-US"}

[Vendor ID       : 25506[]{#_Toc403999238}]{lang="EN-US"}

[Radio count     : 2[]{#_Toc403999239}]{lang="EN-US"}

[ Radio 1:[]{#_Toc403999240}]{lang="EN-US"}

[  Mode          : 802.11a, 802.11an[]{#_Toc403999241}]{lang="EN-US"}

[  Default mode  : 802.11an[]{#_Toc403999242}]{lang="EN-US"}

[  BSS count     : 16[]{#_Toc403999243}]{lang="EN-US"}

[ Radio 2:[]{#_Toc403999244}]{lang="EN-US"}

[  Mode          : 802.11b, 802.11g, 802.11gn[]{#_Toc403999245}]{lang="EN-US"}

[  Default mode  : 802.11gn[]{#_Toc403999246}]{lang="EN-US"}

[  BSS count     : 16]{lang="EN-US"}[]{#_Toc403999247}

[[表1-1 ]{lang="EN-US"}[display wlan ap-model]{lang="EN-US"}]{#struct_0_x2117_18423_83481152}[命令显示信息描述表]{style="font-family:黑体"}[]{#_Toc403999248}

[]{#table_struct_0_x600797593}[[字段]{style="font-family:黑体"}]{#struct_0_x2117_18423_x100935920}[]{#_Toc403999249}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2117_18423_811546828}[]{#_Toc403999250}

[]{#_Toc403999251}

[[AP model]{lang="EN-US"}]{#struct_0_x2117_18423_x1695562982}[]{#_Toc403999252}

[[AP ]{lang="EN-US"}]{#struct_0_x2117_18423_316634829}[型号名]{style="font-family:宋体"}[]{#_Toc403999253}

[]{#_Toc403999254}

[[Alias]{lang="EN-US"}]{#struct_0_x2117_18423_x784554470}[]{#_Toc403999255}

[[AP]{lang="EN-US"}]{#struct_0_x2117_18423_688723771}[型号别名]{style="font-family:宋体"}[]{#_Toc403999256}

[]{#_Toc403999257}

[[Vendor name]{lang="EN-US"}]{#struct_0_x2117_18423_203601789}[]{#_Toc403999258}

[[产商名]{style="font-family:宋体"}]{#struct_0_x2117_18423_x1249449112}[]{#_Toc403999259}

[]{#_Toc403999260}

[[Vendor ID]{lang="EN-US"}]{#struct_0_x2117_18423_x283663219}[]{#_Toc403999261}

[[产商]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2117_18423_x197275504}[]{#_Toc403999262}

[]{#_Toc403999263}

[[Radio count]{lang="EN-US"}]{#struct_0_x2117_18423_1172734804}[]{#_Toc403999264}

[[射频个数]{style="font-family:宋体"}]{#struct_0_x2117_18423_1479434243}[]{#_Toc403999265}

[]{#_Toc403999266}

[[Mode]{lang="EN-US"}]{#struct_0_x2117_18423_218040043}[]{#_Toc403999267}

[[支持的射频类型]{style="font-family:宋体"}]{#struct_0_x2117_18423_1031170936}[]{#_Toc403999268}

[]{#_Toc403999269}

[[Default mode ]{lang="EN-US"}]{#struct_0_x2117_18423_1671763195}[]{#_Toc403999270}

[[默认的射频类型]{style="font-family:宋体"}]{#struct_0_x2117_18423_x86649698}[]{#_Toc403999271}

[]{#_Toc403999272}

[[BSS count]{lang="EN-US"}]{#struct_0_x2117_18423_x68297490}[]{#_Toc403999273}

[[一个]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_x2117_18423_700258234}[可以创建的最大基本服务集个数]{style="font-family:宋体"}[]{#_Toc403999274}

[]{#_Toc403999275}

[ ]{lang="EN-US"}

::: {#-410979931 .myid}
[]{#_Toc404794853}[]{#struct_0_x2117_18423_x300990655}[]{#_Toc401582033}[]{#_Toc396742888}

**射频管理 \-- 射频管理命令 \-- distance**

------------------------------------------------------------------------

[**[distance]{lang="IT"}**]{#struct_0_x2117_18423_x2066878012}[命令用来配置]{style="font-family:宋体"}[射频]{style="font-family:宋体"}[可覆盖的最远距离]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo distance]{lang="IT"}**]{#struct_0_x2117_18423_x791659689}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x22213381}

[**[distance ]{lang="IT"}**]{#struct_0_x2117_18423_1662934695}*[distance]{lang="IT"}*

[**[undo distance]{lang="IT"}**]{#struct_0_x2117_18423_393028887}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x390811348}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x2113162742}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_480485376}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[射频]{style="font-family:宋体"}[可覆盖的最远距离为]{style="font-family:宋体"}[1]{lang="EN-US"}[公里。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_474323166}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[射频]{style="font-family:宋体"}[可覆盖的最远距离为]{style="font-family:宋体"}[1]{lang="EN-US"}[公里。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1595630820}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_620352338}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x790130435}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1899570594}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1409460205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1399526831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_777403106}

[*[distance]{lang="EN-US"}*]{#struct_0_x2117_18423_1365550823}[：射频可覆盖的最远距离，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[，单位为公里。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1952623833}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x27001236}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1408046385}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1226615407}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x127595385}[配置射频可覆盖的最远距离为]{style="font-family:宋体"}[5]{lang="EN-US"}[公里]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_x1791384720}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="IT"}[distance 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1712876816}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x1548576653}[配置射频可覆盖的最远距离为]{style="font-family:宋体"}[5]{lang="EN-US"}[公里]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x1596697042}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] distance 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x651593393}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x1020685153}[配置射频可覆盖的最远距离为]{style="font-family:宋体"}[5]{lang="EN-US"}[公里]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1863078433}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] type dot11g]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] distance 5]{lang="EN-US"}
:::

::: {#-699116966 .myid}
[]{#_Toc404794854}[]{#struct_0_x2117_18423_558673653}

**射频管理 \-- 射频管理命令 \-- dot11n mandatory maximum-mcs**

------------------------------------------------------------------------

[**[dot11n mandatory maximum-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_x2007936953}[命令用来配置射频]{style="font-family:
宋体"}[802.11n]{lang="EN-US"}[的基本]{style="font-family:
宋体"}[MCS]{lang="EN-US"}[最大索引。]{style="font-family:宋体"}

[**[undo dot11n mandatory maximum-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_x1236853931}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1333014780}

[**[dot11n mandatory maximum-mcs ]{lang="EN-US"}***[index]{lang="EN-US"}*]{#struct_0_x2117_18423_1182155431}

[**[undo dot11n mandatory maximum-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_2046541401}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1116885997}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1180306702}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x141664053}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，未配置任何]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[的基本]{style="font-family:宋体"}[MCS]{lang="EN-US"}[速率集。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_1429356327}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，未配置任何]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[的基本]{style="font-family:宋体"}[MCS]{lang="EN-US"}[速率集。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x2040378673}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1018873297}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x375452153}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x295179336}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x557839314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_484975434}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1580489936}

[*[index]{lang="EN-US"}*]{#struct_0_x2117_18423_376522419}[：指定射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[基本]{style="font-family:宋体"}[MCS]{lang="EN-US"}[速率集的最大]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[76]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x731374212}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户需要在指定]{lang="EN-US" style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_x2117_18423_x1338175516}[下配置]{lang="EN-US" style="font-family:宋体"}[**[client dot11n-only]{lang="EN-US"}**]{#_Toc189301523}**[ enable]{lang="EN-US"}**[命令，则必须配置]{lang="EN-US" style="font-family:宋体"}[802.11n]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[MCS]{lang="EN-US"}[最大索引。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户需要在指定]{lang="EN-US" style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_x2117_18423_1024973820}[下配置]{lang="EN-US" style="font-family:宋体"}**[dot11n multicast-mcs]{lang="EN-US"}**[命令，则必须配置]{lang="EN-US" style="font-family:
宋体"}[802.11n]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[MCS]{lang="EN-US"}[最大索引。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_2055114888}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1192280757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1215078230}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x1627411970}[设置射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[基本]{style="font-family:宋体"}[MCS]{lang="EN-US"}[速率集的最大]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_251263388}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] dot11n mandatory maximum-mcs 14]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x596010228}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x297654974}[设置射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[基本]{style="font-family:宋体"}[MCS]{lang="EN-US"}[速率集的最大]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x2117_18423_1967716564}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] dot11n mandatory maximum-mcs 14]{lang="EN-US"}
:::

::: {#1745058968 .myid}
[]{#_Toc404794855}[]{#struct_0_x2117_18423_867962643}

**射频管理 \-- 射频管理命令 \-- dot11n multicast-mcs**

------------------------------------------------------------------------

[**[dot11n multicast-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_98699788}[命令用来配置射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[的组播]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引。]{style="font-family:宋体"}

[**[undo dot11n multicast-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_1578541096}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1902395441}

[**[dot11n multicast-mcs ]{lang="EN-US"}***[index]{lang="EN-US"}*]{#struct_0_x2117_18423_x1543552510}

[**[undo dot11n multicast-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_x1746484457}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_164306723}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1536602598}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_755957271}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，未配置任何]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[组播]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1992089136}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，未配置任何]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[组播]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1826870855}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1425161635}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1284249135}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1150348077}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_331336203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_296162059}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_876365702}

[*[Index]{lang="EN-US"}*]{#struct_0_x2117_18423_929733997}[：指定射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[组播]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[76]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_866278756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接入的客户端都是]{style="font-family:宋体"}]{#struct_0_x2117_18423_1922997640}[802.11n]{lang="EN-US"}[客户端时，组播]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当存在非]{style="font-family:宋体"}]{#struct_0_x2117_18423_928759330}[802.11n]{lang="EN-US"}[客户端时，只能选用基础模式的组播速率，即]{style="font-family:宋体"}[802.11a/b/g]{lang="EN-US"}[的组播速率。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[组播]{style="font-family:宋体"}]{#struct_0_x2117_18423_x2014764964}[MCS]{lang="EN-US"}[索引起作用时，无论带宽模式设置的是]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[模式还是]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[模式，统一采用]{style="font-family:宋体"}[20MHz]{lang="EN-US"}[模式对应的速率。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_2005130276}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1939887125}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1029551684}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x601184288}[设置射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[组播]{style="font-family:宋体"}[MCS]{lang="EN-US"}[索引为]{style="font-family:宋体"}[14]{lang="EN-US"}[：]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x1800813758}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] dot11n mandatory maximum-mcs 15]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] dot11n multicast-mcs 14]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x946579273}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x849007963}[设置射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[组播]{style="font-family:宋体"}[MCS]{lang="EN-US"}[的最大索引为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x2117_18423_1755489}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] dot11n mandatory maximum-mcs 15]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] dot11n multicast-mcs 14]{lang="EN-US"}
:::

::: {#-1757448575 .myid}
[]{#_Toc404794856}[]{#struct_0_x2117_18423_1778206093}[]{#_Toc394936813}[]{#_Toc396119090}[]{#_Toc396290119}[]{#_Toc396742885}

**射频管理 \-- 射频管理命令 \-- dot11n support maximum-mcs**

------------------------------------------------------------------------

[**[dot11n support maximum-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_x131403549}[命令用来配置射频]{style="font-family:
宋体"}[802.11n]{lang="EN-US"}[支持]{style="font-family:
宋体"}[MCS]{lang="EN-US"}[的最大索引。]{style="font-family:宋体"}

[**[undo dot11n support maximum-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_675501874}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_34712679}

[**[dot11n support maximum-mcs ]{lang="EN-US"}***[index]{lang="EN-US"}*]{#struct_0_x2117_18423_1471048717}

[**[undo dot11n support maximum-mcs]{lang="EN-US"}**]{#struct_0_x2117_18423_373803184}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_30447609}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x168086566}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_549444608}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[支持]{style="font-family:宋体"}[MCS]{lang="EN-US"}[最大索引值为]{style="font-family:宋体"}[76]{lang="EN-US"}[。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_436154715}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[支持]{style="font-family:宋体"}[MCS]{lang="EN-US"}[最大索引值为]{style="font-family:宋体"}[76]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1371771092}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_484265877}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_1962333296}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x853429831}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_2129666759}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1554267760}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1045820695}

[*[index]{lang="EN-US"}*]{#struct_0_x2117_18423_1352352469}[：]{style="font-family:黑体"}[指定射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[支持]{style="font-family:宋体"}[MCS]{lang="EN-US"}[的最大索引值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[76]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1816642564}

[[用该命令指定的]{style="font-family:宋体"}[802.11n]{lang="EN-US"}]{#struct_0_x2117_18423_x1844478856}[支持]{style="font-family:宋体"}[MCS]{lang="EN-US"}[最大]{style="font-family:宋体"}[索引不能小于]{style="font-family:宋体"}**[dot11n mandatory maximum-mcs]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[基本]{style="font-family:宋体"}[MCS]{lang="EN-US"}[最大索引。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1665190218}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1133318071}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1668004373}[设置射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[支持]{style="font-family:宋体"}[MCS]{lang="EN-US"}[的最大索引为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x432200130}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[AC-wlan-ap-ap1-radio-1\] dot11n support maximum-mcs 14]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1497832978}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x379963880}[设置射频]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[支持]{style="font-family:宋体"}[MCS]{lang="EN-US"}[的最大索引为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x2117_18423_1712027527}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] dot11n support maximum-mcs 14]{lang="EN-US"}
:::

::: {#1039504537 .myid}
[]{#_Toc404794857}[]{#struct_0_x2117_18423_392067521}[]{#_Toc401582034}[]{#_Toc396742889}

**射频管理 \-- 射频管理命令 \-- max-power**

------------------------------------------------------------------------

[**[max-power]{lang="IT"}**]{#struct_0_x2117_18423_x524497458}[命令用来配置射频最大传输功率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2117_18423_1521192129}**[max-power]{lang="IT"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1737024264}

[**[max-power]{lang="EN-US"}***[ radio-power]{lang="EN-US"}*]{#struct_0_x2117_18423_x979431169}

[**[undo max-power]{lang="EN-US"}**]{#struct_0_x2117_18423_1616874986}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x15608176}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x432765870}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1826055250}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[射频]{style="font-family:宋体"}[使用支持的最大功率。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x2048029886}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[射频]{style="font-family:宋体"}[使用支持的最大功率。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1733461921}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x144232043}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1949358222}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_391933248}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1307448084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1054001222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1913041016}

[*[radio-power]{lang="EN-US"}*]{#struct_0_x2117_18423_x639856503}[：射频的最大传输功率，其取值范围由国家码和射频类型决定。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x2026178080}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最大功率和国家码、信道、]{style="font-family:宋体"}]{#struct_0_x2117_18423_x867181178}[AP]{lang="EN-US"}[型号、射频类型和天线类型相关，如果采用]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[，那么射频的最大功率和带宽类型也相关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[改变射频类型、射频的工作信道、国家码、天线类型、带宽、天线增益等属性时，]{style="font-family:宋体"}]{#struct_0_x2117_18423_1097373015}[max-power]{lang="EN-US"}[的值会自动改变。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_993196800}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1900927204}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1041334124}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x29481343}[配置射频最大传输功率为]{style="font-family:宋体"}[15dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_577554649}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="IT"}[max-power 15]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_539418624}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x39178052}[配置射频最大传输功率为]{style="font-family:宋体"}[15dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_620439114}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] max-power 15]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_601651809}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1917094826}[配置射频最大传输功率为]{style="font-family:宋体"}[15dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x2083727469}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] type dot11g]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] max-power 15]{lang="EN-US"}
:::

::: {#2054612893 .myid}
[]{#_Toc404794858}[]{#struct_0_x2117_18423_1556463229}[]{#_Toc401582035}[]{#_Toc396742890}

**射频管理 \-- 射频管理命令 \-- power-lock enable**

------------------------------------------------------------------------

[**[power]{lang="EN-US"}**]{#struct_0_x2117_18423_1300088509}**[-lock enable]{lang="IT"}**[命令用来开启功率锁定功能。]{style="font-family:宋体"}

[**[power]{lang="EN-US"}**]{#struct_0_x2117_18423_363754532}**[-lock disable]{lang="IT"}**[命令用来关闭功率锁定功能。]{style="font-family:宋体"}

[**[undo power]{lang="EN-US"}**]{#struct_0_x2117_18423_x1848537112}**[-lock]{lang="IT"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1595565284}

[**[power-lock]{lang="EN-US"}**[ { **enable** \| **disable** }]{lang="EN-US"}]{#struct_0_x2117_18423_822526507}

[**[undo ]{lang="IT"}[power]{lang="EN-US"}**]{#struct_0_x2117_18423_744878041}**[-lock]{lang="IT"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x779277940}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1391937759}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x553071578}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[功率锁定功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_748584200}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1885566398}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1276092402}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x245963117}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x710632167}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1286007210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果先开启功率调整，再配置锁定功率，]{style="font-family:宋体"}]{#struct_0_x2117_18423_x1646537406}[AC]{lang="EN-US"}[会自动将当前传输功率设置并锁定为自动功率调整后的功率值，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[重启后，]{style="font-family:宋体"}[AP]{lang="EN-US"}[能继续使用锁定的功率调整值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果先配置锁定功率]{style="font-family:宋体"}]{#struct_0_x2117_18423_748506634}[命令，后开启功率调整功能，由于功率已经被锁定，功率调整功能不会运行，所以在开启功率]{style="font-family:宋体"}[调整功能前，请确保]{style="font-family:宋体"}[功率]{style="font-family:宋体"}[没有被锁定]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[锁定功率后，如果信道发生调整，并且锁定的功率值]{style="font-family:宋体"}]{#struct_0_x2117_18423_x2044442842}[ \> ]{lang="EN-US"}[调整后使用信道支持的最大功率，在这种情况下，设备会将功率值调整为信道支持的最大功率。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1036691389}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[关于功率调整功能的详细介绍，请参见"]{style="font-family:宋体"}]{#struct_0_x2117_18423_1252892742}[WLAN]{lang="IT"}[配置指导"中的"]{style="font-family:宋体"}[WLAN RRM]{lang="IT"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1548511117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Radio]{lang="EN-US"}]{#struct_0_x2117_18423_x1953289495}[视图]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x1321528523}[配置]{style="font-family:宋体"}[锁定功率。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1560105145}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] power lock]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_x2117_18423_1210292919}[组]{lang="EN-US" style="font-family:
宋体"}[Radio]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_243538992}[配置锁定功率。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x455854026}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] power lock]{lang="EN-US"}
:::

::: {#-1957623772 .myid}
[]{#_Toc404794859}[]{#struct_0_x2117_18423_x1091166045}[]{#_Toc401582036}[]{#_Toc396742891}[]{#_Toc401932206}[]{#_Toc401932207}[]{#_Toc401932208}[]{#_Toc401932209}[]{#_Toc401932210}[]{#_Toc401932211}[]{#_Toc401932212}

**射频管理 \-- 射频管理命令 \-- preamble**

------------------------------------------------------------------------

[**[preamble]{lang="EN-US"}**]{#struct_0_x2117_18423_x2056427777}[命令用来配置前导码类型。]{style="font-family:宋体"}

[**[undo preamble]{lang="EN-US"}**]{#struct_0_x2117_18423_x113864992}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_53912980}

[**[preamble]{lang="EN-US"}**[ { **long** \| **short** }]{lang="EN-US"}]{#struct_0_x2117_18423_x968186986}

[**[undo preamble]{lang="EN-US"}**]{#struct_0_x2117_18423_x921445285}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1180372238}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_243699298}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1347096449}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[Radio]{lang="EN-US"}[使用]{style="font-family:宋体"}[短前导码。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x2024015059}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[Radio]{lang="EN-US"}[使用]{style="font-family:宋体"}[短前导码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1833559745}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1987462321}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x6255174}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1887785471}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_76966119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1781126025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x981376886}

[**[long]{lang="EN-US"}**]{#struct_0_x2117_18423_x1583665721}[：长和短前导码。在网络中如果有客户端使用早期的客户端网卡，可以选择长前导码兼容这些客户端。]{style="font-family:宋体"}

[**[short]{lang="EN-US"}**]{#struct_0_x2117_18423_1222117625}[：短前导码。选择短前导码能使网络同步性能更好，一般选择短前导码。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_479313700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[前导码是位于数据包起始处的一组]{style="font-family:宋体"}]{#struct_0_x2117_18423_x2144159773}[bit]{lang="EN-US"}[位，接收者可以据此同步并准备接收数据。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_2056411775}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1192215221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x259174220}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_286924696}[配置前导码类型为长前导码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_x332922203}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 2]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-2\] ]{lang="IT"}[preamble long]{lang="EN-US"}

[]{#OLE_LINK4}[]{#struct_0_x2117_18423_1932184622}[]{#OLE_LINK6}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#OLE_LINK5}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x1661123954}[配置前导码类型为长前导码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x2107802544}

[]{#OLE_LINK7}[]{#OLE_LINK9}[[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}]{#OLE_LINK8}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] preamble lon]{lang="EN-US"}[g]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_1987237090}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x810101380}[配置前导码类型为长前导码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_481385847}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] type dot11g]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] ]{lang="EN-US"}[preamble long]{lang="EN-US"}
:::

::: {#285664713 .myid}
[]{#_Toc404794860}[]{#struct_0_x2117_18423_x871656563}[]{#_Toc401582038}[]{#_Toc396742895}

**射频管理 \-- 射频管理命令 \-- radio enable**

------------------------------------------------------------------------

[**[radio enable]{lang="IT"}**]{#struct_0_x2117_18423_1573961317}[命令用来开启射频功能。]{style="font-family:宋体"}

[**[radio]{lang="IT"}[ disable]{lang="EN-US"}**]{#struct_0_x2117_18423_1536668134}[命令用来关闭射频功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2117_18423_x803096145}**[radio]{lang="IT"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x150611536}

[**[radio]{lang="EN-US"}**[ { **enable** \| **disable** }]{lang="EN-US"}]{#struct_0_x2117_18423_x1176797651}

[**[undo radio]{lang="EN-US"}**]{#struct_0_x2117_18423_198700869}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1913269615}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1566054120}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_440809551}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[射频处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1409264145}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x851252652}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x73987924}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_15012687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1751693575}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1945945848}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x637999902}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1564011724}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1939952661}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x571802324}[开启射频功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_x593499078}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="IT"}[radio enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_762055864}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x2039103830}[开启射频功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_434872064}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] radio enable]{lang="EN-US"}
:::

::: {#-1209792781 .myid}
[]{#_Toc404794861}[]{#struct_0_x2117_18423_x1215680708}[]{#_Toc401582037}[]{#_Toc396742892}

**射频管理 \-- 射频管理命令 \-- radio**

------------------------------------------------------------------------

[**[radio]{lang="IT"}**]{#struct_0_x2117_18423_1799768109}[命令用来进入]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_2145563507}

[**[radio ]{lang="EN-US"}***[radio-id]{lang="EN-US"}*]{#struct_0_x2117_18423_x12074275}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1305078446}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1540868294}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[ap-model]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1618745426}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_373868720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1274720009}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_308098214}

[*[radio-id]{lang="EN-US"}*]{#struct_0_x2117_18423_x1130789737}[：]{style="font-family:宋体"}[取值范围与]{style="font-family:宋体"}[AP]{lang="EN-US"}[设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x645357800}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1793968645}[进入]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x561794383}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x755895334}[进入]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x1829196792}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap-apgroup1\]ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-apgroup1-ap-model-WA4620i-ACN\]radio 1]{lang="EN-US"}
:::

::: {#1272578836 .myid}
[]{#_Toc404794862}[]{#struct_0_x2117_18423_x233122360}[]{#_Toc401582039}[]{#_Toc396742896}[]{#_Toc394936821}[]{#_Toc396119098}[]{#_Toc396290127}[]{#_Toc396742893}[]{#_Toc394936822}[]{#_Toc396119099}[]{#_Toc396290128}[]{#_Toc396742894}

**射频管理 \-- 射频管理命令 \-- rate**

------------------------------------------------------------------------

[**[rate]{lang="IT"}**]{#struct_0_x2117_18423_x168637632}[命令用来配置射频速率。]{style="font-family:宋体"}

[**[undo rate]{lang="IT"}**]{#struct_0_x2117_18423_572346816}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1882441789}

[**[rate]{lang="EN-US"}**[ { **disabled** \| **mandatory** \| **multicast** \| **supported** } *rate-value*]{lang="EN-US"}]{#struct_0_x2117_18423_x1139872879}

[**[undo rate]{lang="EN-US"}**]{#struct_0_x2117_18423_1133383607}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_117344729}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1118927761}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1580103835}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[802.11a]{lang="EN-US"}]{#struct_0_x2117_18423_1550058168}[/802.11an]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;
font-family:Wingdings"}[[禁用速率：]{lang="EN-US" style="font-family:宋体"}]{.ItemListCharChar}]{#struct_0_x2117_18423_x1899705874}[无。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;
font-family:Wingdings"}[[强制速率：]{lang="EN-US" style="font-family:宋体"}]{.ItemListCharChar}[6]{lang="EN-US"}]{#struct_0_x2117_18423_x278836420}[，]{lang="EN-US" style="font-family:宋体"}[12]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[24]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;
font-family:Wingdings"}[[组播速率：]{style="font-family:宋体"}]{.ItemListCharChar}]{#struct_0_x2117_18423_x398737753}[从强制速率中选取最大值[[。]{style="font-family:宋体"}]{.ItemListCharChar}]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;
font-family:Wingdings"}[[支持速率：]{lang="EN-US" style="font-family:宋体"}]{.ItemListCharChar}[9]{lang="EN-US"}]{#struct_0_x2117_18423_x318399776}[，]{lang="EN-US" style="font-family:宋体"}[18]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[48]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[54]{lang="EN-US"}[[。]{lang="EN-US" style="font-family:宋体"}]{.ItemListCharChar}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11b]{lang="EN-US"}]{#struct_0_x2117_18423_604439168}[：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[禁用速率：无。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2117_18423_x1776575919}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[强制速率：]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2117_18423_1255087342}[，]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[组播速率：从强制速率中选取最大值。]{style="font-family:宋体"}]{#struct_0_x2117_18423_1769862360}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[支持速率：]{lang="EN-US" style="font-family:宋体"}[5.5]{lang="EN-US"}]{#struct_0_x2117_18423_x657769473}[，]{lang="EN-US" style="font-family:宋体"}[11]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[802.11g]{lang="EN-US"}]{#struct_0_x2117_18423_x1771560215}[/802.11gn]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[禁用速率：无。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2117_18423_x194080967}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[强制速率：]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2117_18423_x432700334}[，]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[5.5]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[11]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[组播速率：从强制速率中选取最大值。]{style="font-family:宋体"}]{#struct_0_x2117_18423_x1115757895}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[支持速率：]{lang="EN-US" style="font-family:宋体"}[6]{lang="EN-US"}]{#struct_0_x2117_18423_x2077932647}[，]{lang="EN-US" style="font-family:宋体"}[9]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[12]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[18]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[24]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[48]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[54]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1689136061}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[802.11a]{lang="EN-US"}]{#struct_0_x2117_18423_x1901429146}[/802.11an]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[[禁用速率：]{lang="EN-US" style="font-family:
宋体"}]{.ItemListCharChar}]{#struct_0_x2117_18423_x1882313688}[无。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[[强制速率：]{lang="EN-US" style="font-family:
宋体"}]{.ItemListCharChar}[6]{lang="EN-US"}]{#struct_0_x2117_18423_x1929881354}[，]{lang="EN-US" style="font-family:宋体"}[12]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[24]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[[组播速率：]{style="font-family:宋体"}]{.ItemListCharChar}]{#struct_0_x2117_18423_1264456694}[从强制速率中选取最大值[[。]{style="font-family:宋体"}]{.ItemListCharChar}]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[[支持速率：]{lang="EN-US" style="font-family:
宋体"}]{.ItemListCharChar}[9]{lang="EN-US"}]{#struct_0_x2117_18423_x1434775823}[，]{lang="EN-US" style="font-family:宋体"}[18]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[48]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[54]{lang="EN-US"}[[。]{lang="EN-US" style="font-family:宋体"}]{.ItemListCharChar}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11b]{lang="EN-US"}]{#struct_0_x2117_18423_1254561969}[：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[禁用速率：无。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2117_18423_x1336758323}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[强制速率：]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2117_18423_46815019}[，]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[组播速率：从强制速率中选取最大值。]{style="font-family:宋体"}]{#struct_0_x2117_18423_1238227888}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[支持速率：]{lang="EN-US" style="font-family:宋体"}[5.5]{lang="EN-US"}]{#struct_0_x2117_18423_x623659132}[，]{lang="EN-US" style="font-family:宋体"}[11]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[802.11g]{lang="EN-US"}]{#struct_0_x2117_18423_548739851}[/802.11gn]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[禁用速率：无。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2117_18423_x167198278}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[强制速率：]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2117_18423_x29415807}[，]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[5.5]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[11]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[组播速率：从强制速率中选取最大值。]{style="font-family:宋体"}]{#struct_0_x2117_18423_x955285307}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[支持速率：]{lang="EN-US" style="font-family:宋体"}[6]{lang="EN-US"}]{#struct_0_x2117_18423_x899241248}[，]{lang="EN-US" style="font-family:宋体"}[9]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[12]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[18]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[24]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[36]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[48]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[54]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x654987036}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1644838223}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1316580147}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x166731686}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1219848694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x1355653080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1420175673}

[**[disabled]{lang="EN-US"}**]{#struct_0_x2117_18423_x1854745101}[：禁用速率。]{style="font-family:宋体"}[AP]{lang="EN-US"}[禁用的速率。]{style="font-family:宋体"}

[**[mandatory]{lang="EN-US"}**]{#struct_0_x2117_18423_1640665852}[：强制速率。客户端关联]{style="font-family:宋体"}[AP]{lang="EN-US"}[时，]{style="font-family:宋体"}[AP]{lang="EN-US"}[要求客户端必须支持的速率。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_x2117_18423_1643439551}[：组播速率，即]{style="font-family:宋体"}[AP]{lang="EN-US"}[向客户端发送组播报文的速率。组播速率必须在强制速率中选取。]{style="font-family:宋体"}

[**[supported]{lang="EN-US"}**]{#struct_0_x2117_18423_1026972865}[：支持速率。]{style="font-family:宋体"}[AP]{lang="EN-US"}[所支持的速率。客户端关联]{style="font-family:宋体"}[AP]{lang="EN-US"}[后，可以在]{style="font-family:宋体"}[AP]{lang="EN-US"}[支持的"支持速率集"中选用更高]{style="font-family:宋体"}[/]{lang="EN-US"}[更低的速率发送报文。]{style="font-family:宋体"}

[*[rate-value]{lang="EN-US"}*]{#struct_0_x2117_18423_x406184975}[：]{style="font-family:宋体"}[速率值，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}[可配置多个速率，用空格分隔]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802]{lang="EN-US"}[.11a]{lang="EN-US"}]{#struct_0_x2117_18423_x1211579578}[/802.11an]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[可以取值]{style="font-family:宋体"}[6]{lang="EN-US"}[、]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[12]{lang="EN-US"}[、]{style="font-family:宋体"}[18]{lang="EN-US"}[、]{style="font-family:宋体"}[24]{lang="EN-US"}[、]{style="font-family:宋体"}[36]{lang="EN-US"}[、]{style="font-family:宋体"}[48]{lang="EN-US"}[、]{style="font-family:宋体"}[54]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11b]{lang="EN-US"}]{#struct_0_x2117_18423_x1595499748}[：可以取值]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[5.5]{lang="EN-US"}[、]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.11g]{lang="EN-US"}]{#struct_0_x2117_18423_1493054611}[/802.1gn]{lang="EN-US"}[：可以取值]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[5.5]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[、]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:宋体"}[11]{lang="EN-US"}[、]{style="font-family:宋体"}[12]{lang="EN-US"}[、]{style="font-family:宋体"}[18]{lang="EN-US"}[、]{style="font-family:宋体"}[24]{lang="EN-US"}[、]{style="font-family:宋体"}[36]{lang="EN-US"}[、]{style="font-family:宋体"}[48]{lang="EN-US"}[、]{style="font-family:宋体"}[54]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1796265192}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[强制速率和组播速率不能为空。当强制速率只有一个值时，用户不能将这个值配置成支持速率或者禁止速率。]{style="font-family:宋体"}]{#struct_0_x2117_18423_x437267363}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x535264230}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x629796989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1060366260}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_2000757314}[配置强制速率为]{style="font-family:宋体"}[6Mbps]{lang="EN-US"}[、]{style="font-family:宋体"}[12Mbps]{lang="EN-US"}[、]{style="font-family:宋体"}[24Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_997160218}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="IT"}[rate **mandatory** 6 12 24]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x191480933}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1582630}[配置强制速率为]{style="font-family:宋体"}[6Mbps]{lang="EN-US"}[、]{style="font-family:宋体"}[12Mbps]{lang="EN-US"}[、]{style="font-family:宋体"}[24Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1272997811}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] rate mandatory 6 12 24]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1548445581}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1356077512}[配置强制速率为]{style="font-family:宋体"}[6Mbps]{lang="EN-US"}[、]{style="font-family:宋体"}[12Mbps]{lang="EN-US"}[、]{style="font-family:宋体"}[24Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_1823798483}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] type dot11g]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] rate mandatory 6 12 24]{lang="EN-US"}
:::

::: {#-1193283019 .myid}
[]{#_Toc404794863}[]{#struct_0_x2117_18423_1864226895}[]{#_Toc401932217}[]{#_Toc401932218}[]{#_Toc401932219}[]{#_Toc401932220}[]{#_Toc401932221}

**射频管理 \-- 射频管理命令 \-- short-gi enable**

------------------------------------------------------------------------

[**[short-gi enable]{lang="EN-US"}**]{#struct_0_x2117_18423_1593511847}[命令用来开启]{style="font-family:宋体"}[Short-GI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[short-gi disable]{lang="EN-US"}**]{#struct_0_x2117_18423_x395517078}[命令用来关闭]{style="font-family:宋体"}[Short-GI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo short-gi]{lang="EN-US"}**]{#struct_0_x2117_18423_x1587111260}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_99935108}

[**[short-gi]{lang="EN-US"}**[ { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_x2117_18423_x1853470251}

[**[undo short-gi]{lang="EN-US"}**]{#struct_0_x2117_18423_x1827308883}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_2033029633}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x466601766}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1044616739}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[功能处于开启状态。]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1344436241}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x829984762}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1180437774}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1709386564}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1419821422}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x839282812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1571408678}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x537751639}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令仅在支持]{style="font-family:宋体"}]{#struct_0_x2117_18423_1989045783}[802.11n]{lang="EN-US"}[和]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[上支持。在进行]{style="font-family:宋体"}[Radio]{lang="EN-US"}[模式切换的时候，设备会恢复该模式下该功能的缺省情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1783185807}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x387309948}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_511448144}[设备举例]{lang="EN-US" style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_x900366322}[关闭]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x1439835591}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] short-gi disable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x478785599}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_x2117_18423_x2120982404}[关闭]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x2117_18423_x1192149685}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/1\] short-gi disable]{lang="EN-US"}
:::

::: {#-1051447130 .myid}
[]{#_Toc404794864}[]{#struct_0_x2117_18423_x1944449671}[]{#_Toc401582040}[]{#_Toc396742897}

**射频管理 \-- 射频管理命令 \-- type**

------------------------------------------------------------------------

[**[type]{lang="EN-US"}**]{#struct_0_x2117_18423_231024387}[命令用来配置射频类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **type**]{lang="EN-US"}]{#struct_0_x2117_18423_x714564980}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x523262735}

[**[type ]{lang="EN-US"}**[{ **dot11a** \| **dot11an** \| **dot11b** \| **dot11g** \| **dot11gn** }]{lang="EN-US"}]{#struct_0_x2117_18423_x1051989526}

[**[undo type]{lang="EN-US"}**]{#struct_0_x2117_18423_x492267810}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_18423_203921949}

[[缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2117_18423_x476694370}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1161680174}

[[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1121080195}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_1685795799}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x1844658658}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_18423_x779866144}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_18423_1536733670}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_18423_363170125}

[**[dot11a]{lang="EN-US"}**]{#struct_0_x2117_18423_x1517709277}[：指定射频类型为]{style="font-family:宋体"}[802.11a]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot11an]{lang="EN-US"}**]{#struct_0_x2117_18423_x860478832}[：指定射频类型为]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[（]{style="font-family:宋体"}[5GHz]{lang="EN-US"}[）模式。]{style="font-family:宋体"}

[**[dot11b]{lang="EN-US"}**]{#struct_0_x2117_18423_1507753069}[：指定射频类型类型为]{style="font-family:宋体"}[802.11b]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot11g]{lang="EN-US"}**]{#struct_0_x2117_18423_2114432743}[：指定射频类型类型为]{style="font-family:宋体"}[802.11g]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot11gn]{lang="EN-US"}**]{#struct_0_x2117_18423_x1654714386}[：指定射频类型为]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[（]{style="font-family:宋体"}[2.4GHz]{lang="EN-US"}[）模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_18423_1763738838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1420603023}[设备：修改射频类型时，如果射频处于开启状态，会导致客户端下线。修改射频类型后，当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下与射频类型有关的命令，例如信道、最大功率、速率都会恢复为缺省值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_x1516727955}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x218563596}[设备：修改射频类型时，如果射频处于开启状态，会导致客户端下线。修改射频类型后，当前]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口下与射频类型有关的命令，例如信道、最大功率、速率都会恢复为缺省值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_18423_x305236810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_44358133}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_x2137687730}[配置射频类型为]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[（]{style="font-family:宋体"}[5GHz]{lang="EN-US"}[）模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x2117_18423_1940018197}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="IT"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] type dot11an]{lang="IT"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x2117_18423_1872816293}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="IT"}]{#struct_0_x2117_18423_257093544}[配置射频类型为]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[（]{style="font-family:宋体"}[5GHz]{lang="EN-US"}[）模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x1752660727}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] ]{lang="EN-US"}[type dot11an]{lang="IT"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x2117_18423_x1592810017}[设备举例]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_18423_1084500420}[配置]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口类型为]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[（]{style="font-family:宋体"}[5GHz]{lang="EN-US"}[）模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_18423_x985958707}

[\[Sysname\] interface wlan-radio 1/0/2]{lang="EN-US"}

[\[Sysname-WLAN-Radio1/0/2\] type dot11an]{lang="EN-US"}
:::
