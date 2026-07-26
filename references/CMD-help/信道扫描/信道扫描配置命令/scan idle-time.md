::: {#-1662408598 .myid}
[]{#_Toc404795246}[]{#struct_0_37898_12462_1190335018}[]{#_Toc399228147}[]{#_Toc396496554}[]{#_Toc396495992}[]{#_Toc396495867}[]{#_Toc396495808}[]{#_Toc396495864}[]{#_Toc396495989}[]{#_Toc396496551}[]{#_Toc396496699}[]{#_Toc396495809}[]{#_Toc396495865}[]{#_Toc396495990}[]{#_Toc396496552}[]{#_Toc396496700}[]{#_Toc396495810}[]{#_Toc396495866}[]{#_Toc396495991}[]{#_Toc396496553}[]{#_Toc396496701}

**信道扫描 \-- 信道扫描配置命令 \-- scan idle-time**

------------------------------------------------------------------------

[**[scan idle-time]{lang="EN-US"}**]{#struct_0_37898_12462_x1597851998}[命令用来配置服务周期空闲时长。]{style="font-family:宋体"}

[**[undo scan idle-time]{lang="EN-US"}**]{#struct_0_37898_12462_1380280439}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37898_12462_874870705}

[**[scan idle-time]{lang="EN-US"}**[ *idle-time*]{lang="EN-US"}]{#struct_0_37898_12462_x1109322159}

[**[undo scan idle-time]{lang="EN-US"}**]{#struct_0_37898_12462_x961498863}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37898_12462_2106031218}

[]{#struct_0_37898_12462_x1138193403}[]{#OLE_LINK37}[[Radio]{lang="EN-US"}]{#OLE_LINK36}[视图]{style="font-family:宋体"}[：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_37898_12462_740260582}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图：服务周期空闲时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[Radio]{lang="EN-US"}]{#struct_0_37898_12462_x841518044}[接口视图：服务周期空闲时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37898_12462_531674635}

[[AC]{lang="EN-US"}]{#struct_0_37898_12462_803659259}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_37898_12462_1232410508}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37898_12462_x2122312553}

[[network-admin]{lang="EN-US"}]{#struct_0_37898_12462_1173174759}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37898_12462_1112606553}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37898_12462_x741741036}

[*[idle-time]{lang="EN-US"}*]{#struct_0_37898_12462_1756530184}[：服务周期的空闲时长，取值范围]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37898_12462_x1607523211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[服务周期空闲时长指在服务周期内，工作信道上持续无流量的时长。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_37898_12462_x1158781387}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个服务周期内，若流量停止的时间达到空闲时间，且当前周期已停留超过一个扫描周期时间，则切换到下一个扫描周期。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_37898_12462_97135593}[但如果没有达到扫描时间，即使空闲时间超时，也不应切换到扫描周期。即，]{lang="EN-US" style="font-family:宋体"}[服务周期空闲时长和扫描时长都不能大于服务周期最大持续时间。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[scan idle-time]{lang="EN-US"}**]{#struct_0_37898_12462_589506186}[实际生效时间为]{lang="EN-US" style="font-family:宋体"}**[beacon interval]{lang="EN-US"}**[的整数倍，当配置的]{lang="EN-US" style="font-family:宋体"}*[idle-time]{lang="EN-US"}*[小于]{lang="EN-US" style="font-family:宋体"}*[beacon interval]{lang="EN-US"}*[时，实际按照]{lang="EN-US" style="font-family:宋体"}*[beacon in]{lang="EN-US"}[terval]{lang="EN-US"}*[生效。]{lang="EN-US" style="font-family:宋体"}

[**[【举例】]{style="font-family:黑体"}**]{#struct_0_37898_12462_859689740}

[[\# ]{lang="EN-US"}]{#struct_0_37898_12462_x1498159144}[将]{style="font-family:宋体"}[ap1]{lang="EN-US"}[下的]{style="font-family:宋体"}[radio1]{lang="EN-US"}[的服务周期空闲时长配置为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[*[\<Sysna]{lang="EN-US"}*[me*\> system-view* ]{lang="EN-US"}]{#struct_0_37898_12462_1887365311}

[\[Sysna*me\] wlan ap ap1* model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] scan idle-time 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_37898_12462_2119155357}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[beacon interval]{lang="EN-US"}**]{#struct_0_37898_12462_359355919}
:::

::: {#-297593381 .myid}
[]{#_Toc404795247}[]{#struct_0_37898_12462_x1551157485}[]{#_Toc399228148}[]{#_Toc396496557}[]{#_Toc396495995}[]{#_Toc396495870}[]{#_Toc396495812}[]{#_Toc396495868}[]{#_Toc396495993}[]{#_Toc396496555}[]{#_Toc396496703}[]{#_Toc396495813}[]{#_Toc396495869}[]{#_Toc396495994}[]{#_Toc396496556}[]{#_Toc396496704}

**信道扫描 \-- 信道扫描配置命令 \-- scan max-service-time**

------------------------------------------------------------------------

[**[scan max-service-time]{lang="EN-US"}**]{#struct_0_37898_12462_559077814}[命令用来配置服务周期最大持续时间。]{style="font-family:宋体"}

[**[undo scan max-service-time]{lang="EN-US"}**]{#struct_0_37898_12462_512598907}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37898_12462_x948290749}

[**[scan max-service-time]{lang="EN-US"}**[ { *max-service-time* \| **no-limit** }]{lang="EN-US"}]{#struct_0_37898_12462_1787367592}

[**[undo scan max-service-time]{lang="EN-US"}**]{#struct_0_37898_12462_x567880356}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37898_12462_1249649092}

[[Radio]{lang="EN-US"}]{#struct_0_37898_12462_x285778674}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_37898_12462_x324689868}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图：服务周期的最大持续时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[Radio]{lang="EN-US"}]{#struct_0_37898_12462_894245647}[接口视图：服务周期的最大持续时间为]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37898_12462_x522411692}

[[AC]{lang="EN-US"}]{#struct_0_37898_12462_1285060091}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_37898_12462_2023881271}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37898_12462_x1741776135}

[[network-admin]{lang="EN-US"}]{#struct_0_37898_12462_x1949504538}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37898_12462_1951695200}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37898_12462_905698760}

[*[max-service-time]{lang="EN-US"}*]{#struct_0_37898_12462_201462725}[：服务周期的最大持续时间，取值范围]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[no-limit]{lang="EN-US"}**]{#struct_0_37898_12462_x661820026}[：不限制最大服务时间，直到信道闲置（流量停止时间达到空闲时间）才切换。当最大服务时间被配置为]{style="font-family:宋体"}[no-limit]{lang="EN-US"}[时，]{style="font-family:宋体"}[AP]{lang="EN-US"}[将始终优先保证服务类业务，只要存在业务流量，就不会进行扫描。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37898_12462_x1032707639}

[[当前服务周期达到最大持续时间后，如果有信道需要扫描，不论流量是否停止，都将切换到下一个扫描周期。服务周期最大持续时间不能少于扫描周期持续时间。]{style="font-family:宋体"}]{#struct_0_37898_12462_1745800744}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37898_12462_x1620426031}

[[\# ]{lang="EN-US"}]{#struct_0_37898_12462_x771726036}[配置]{style="font-family:宋体"}[服务周期最大持续时间]{style="font-family:宋体"}[为]{style="font-family:宋体"}[3000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_37898_12462_x753222080}

[\[Sysname\] wlan ap ap1model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] scan max-service-time 3000]{lang="EN-US"}
:::

::::: {#-949532182 .myid}
[]{#_Toc404795248}[]{#struct_0_37898_12462_x559478616}[]{#_Toc399228149}[]{#_Toc396496561}[]{#_Toc396495999}[]{#_Toc396495874}[]{#_Toc378521104}[]{#_Toc396495815}[]{#_Toc396495871}[]{#_Toc396495996}[]{#_Toc396496558}[]{#_Toc396496706}[]{#_Toc396495816}[]{#_Toc396495872}[]{#_Toc396495997}[]{#_Toc396496559}[]{#_Toc396496707}[]{#_Toc396495817}[]{#_Toc396495873}[]{#_Toc396495998}[]{#_Toc396496560}[]{#_Toc396496708}

**信道扫描 \-- 信道扫描配置命令 \-- scan scan-time**

------------------------------------------------------------------------

[**[scan scan-time]{lang="EN-US"}**]{#struct_0_37898_12462_1864669025}[命令用来配置扫描时长。]{style="font-family:宋体"}

[**[undo scan scan-time]{lang="EN-US"}**]{#struct_0_37898_12462_2000036683}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_37898_12462_x705002084}

[**[scan scan-time]{lang="EN-US"}***[ scan-time]{lang="EN-US"}*]{#struct_0_37898_12462_x1026947265}

[**[undo scan scan-time]{lang="EN-US"}**]{#struct_0_37898_12462_x991486832}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_37898_12462_x261943460}

[[Radio]{lang="EN-US"}]{#struct_0_37898_12462_x1927774348}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_37898_12462_x211000737}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图：扫描时长为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[Radio]{lang="EN-US"}]{#struct_0_37898_12462_x1320889926}[接口视图：扫描时长为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_37898_12462_x1816171887}

[[AC]{lang="EN-US"}]{#struct_0_37898_12462_x262755437}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_37898_12462_x1283561359}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_37898_12462_x50082510}

[[network-admin]{lang="EN-US"}]{#struct_0_37898_12462_2058631404}

[[mdc-admin]{lang="EN-US"}]{#struct_0_37898_12462_x1904368585}

[[【参数】]{style="font-family:黑体"}]{#struct_0_37898_12462_x1809323658}

[*[scan-time]{lang="EN-US"}*]{#struct_0_37898_12462_x1953077044}[：扫描时间，取值范围]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[5000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_37898_12462_x1364739497}

[[扫描时长指射频信道扫描周期持续的固定时间，同时也用来约定服务周期内提供扫描的时间长度，扫描时间不能大于最大服务时间。当前扫描周期达到扫描时间后，将切换到下一个扫描周期或服务周期。]{style="font-family:宋体"}]{#struct_0_37898_12462_x1108286611}

[[【举例】]{style="font-family:黑体"}]{#struct_0_37898_12462_2107399203}

[[\# ]{lang="EN-US"}]{#struct_0_37898_12462_x783667143}[配置]{style="font-family:宋体"}[扫描时间]{style="font-family:宋体"}[为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_37898_12462_x338713856}

[\[Sysname\] wlan ap ap1 model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1-radio-1\] scan scan-time 500]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](信道扫描命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_37898_12462_1481594702}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[此命令的支持情况与设备的类型有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_37898_12462_2092714299}
:::

[ ]{lang="EN-US"}
:::::
