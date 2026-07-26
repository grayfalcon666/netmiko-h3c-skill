::: {#2029023714 .myid}
[]{#_Toc404795138}[]{#struct_0_x6946_x1740_x97139762}

**WLAN QoS \-- WLAN QoS命令 \-- cac policy**

------------------------------------------------------------------------

[**[cac policy]{lang="EN-US"}**]{#struct_0_x6946_x1740_1376667943}[命令用来配置开启]{style="font-family:宋体"}[CAC]{lang="EN-US"}[（]{style="font-family:宋体"}[Connect Admission Control]{lang="EN-US"}[，连接准入控制）功能后使用的接入控制策略。]{style="font-family:宋体"}

[**[undo cac policy]{lang="EN-US"}**]{#struct_0_x6946_x1740_126291600}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x2074931641}

[**[cac policy]{lang="EN-US"}**[ { **channelutilization** \[ *channelutilization-value* \] \| **client** \[ *users-number* \] }]{lang="EN-US"}]{#struct_0_x6946_x1740_x660226722}

[**[undo cac policy]{lang="EN-US"}**]{#struct_0_x6946_x1740_x1431380927}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1877476236}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x964633261}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1350533287}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，使用基于客户端数量的]{style="font-family:宋体"}[CAC]{lang="EN-US"}[策略，客户端数量为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_601450680}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，使用基于客户端数量的]{style="font-family:宋体"}[CAC]{lang="EN-US"}[策略，客户端数量为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_1150477887}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_816247896}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x890976237}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_288821183}

[[network-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_x420749495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_1216027383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1716815432}

[**[channelutilization]{lang="EN-US"}**]{#struct_0_x6946_x1740_102435109}[：]{style="font-family:宋体"}[CAC]{lang="EN-US"}[使用基于信道利用率的准入策略。]{style="font-family:宋体"}

[*[channelutilization-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_1692375541}[：允许接入的信道最大利用率，即单位时间内，允许接入]{style="font-family:
宋体"}[AC-VO]{lang="EN-US"}[和]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[优先级的业务流占用信道的有效时间与客户端回复的响应帧中]{style="font-family:宋体"}[Medium Time]{lang="EN-US"}[字段中携带值的百分比，有效时间为可用于实际收发数据的时间。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，为百分比形式，缺省值为]{style="font-family:宋体"}[65%]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[client]{lang="EN-US"}**]{#struct_0_x6946_x1740_39040676}[：]{style="font-family:宋体"}[CAC]{lang="EN-US"}[使用基于客户端数量的准入策略。]{style="font-family:宋体"}

[*[users-number]{lang="EN-US"}*]{#struct_0_x6946_x1740_x424578628}[：允许接入的客户端的最大个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[124]{lang="EN-US"}[。如果一个客户端同时接入]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[和]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[优先级业务流，接入客户端的个数按]{style="font-family:宋体"}[1]{lang="EN-US"}[计算。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_162637327}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x2127432675}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x886997934}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1687612433}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x557997281}[配置开启]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能后使用的基于信道利用率的接入控制策略，允许信道最大利用率为]{style="font-family:宋体"}[70]{lang="EN-US"}[％。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x1040334152}

[\[Sysname\] wlan ap ap1 model ]{lang="IT"}[WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="IT"}[cac policy channelutilization 70]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x990029984}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x561348734}[配置开启]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能后使用的基于信道利用率的接入控制策略，允许信道最大利用率为]{style="font-family:宋体"}[70]{lang="EN-US"}[％。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_122977319}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\]]{lang="EN-US"}[ ]{lang="EN-US"}[cac policy channelutilization 70]{lang="IT"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1532325559}[设备举例]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_847217600}[配置开启]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能后使用的基于信道利用率的接入控制策略，允许信道最大利用率为]{style="font-family:宋体"}[70]{lang="EN-US"}[％。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x909374895}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="IT"}

[\[Sysname-WLAN-Radio1/0/1\] cac policy channelutilization 70]{lang="IT"}
:::

::: {#1825905523 .myid}
[]{#_Toc404795139}[]{#struct_0_x6946_x1740_x565926487}[]{#_Toc401046926}[]{#_Toc401046927}

**WLAN QoS \-- WLAN QoS命令 \-- edca radio**

------------------------------------------------------------------------

[**[edca radio]{lang="EN-US"}**]{#struct_0_x6946_x1740_x605233838}[命令用来配置]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的工作参数。]{style="font-family:宋体"}

[**[undo edca radio]{lang="EN-US"}**]{#struct_0_x6946_x1740_384400419}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x62887697}

[**[edca radio]{lang="EN-US"}**[ { **ac-be** \| **ac-bk** \| **ac-vi** \| **ac-vo** } { **aifsn** *aifsn-value* \| **ecw** **ecwmin** *ecwmin-value* **ecwmax** *ecwmax-value* \| **noack** \| **txoplimit** *txoplimit-value* } \*]{lang="EN-US"}]{#struct_0_x6946_x1740_x1432348508}

[**[undo edca radio]{lang="EN-US"}**[ { **ac-be** \| **ac-bk** \| **ac-vi** \| **ac-vo** } { **aifsn** \| **all** \| **ecw** \| **noack** \| **txoplimit** }]{lang="EN-US"}]{#struct_0_x6946_x1740_1289091014}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1828656116}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_648504847}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x838159084}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1825905523#_Ref397345644)[所示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1633723}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[如]{lang="EN-US" style="font-family:宋体"}[[[表]{style="font-family:宋体"}1-1]{lang="EN-US"}](?1825905523#_Ref397345644)[所示]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[]{#struct_0_x6946_x1740_x1577512234}[[表1-1 ]{lang="EN-US"}[Radio]{lang="EN-US"}]{#_Ref397345644}[的工作参数的缺省值]{style="font-family:黑体"}

[]{#table_struct_0_x1711973615}[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1202247029}
:::

[[AIFSN]{lang="EN-US"}]{#struct_0_x6946_x1740_2053094648}

[[ECWmin]{lang="EN-US"}]{#struct_0_x6946_x1740_x716421592}

[[ECWmax]{lang="EN-US"}]{#struct_0_x6946_x1740_1293835786}

[[TXOP Limit]{lang="EN-US"}]{#struct_0_x6946_x1740_1864349054}

[[AC-BK]{lang="EN-US"}]{#struct_0_x6946_x1740_2004427695}

[[7]{lang="EN-US"}]{#struct_0_x6946_x1740_x34966089}

[[4]{lang="EN-US"}]{#struct_0_x6946_x1740_x2041638505}

[[10]{lang="EN-US"}]{#struct_0_x6946_x1740_345792257}

[[0]{lang="EN-US"}]{#struct_0_x6946_x1740_x1439792341}

[[AC-BE]{lang="EN-US"}]{#struct_0_x6946_x1740_1654852657}

[[3]{lang="EN-US"}]{#struct_0_x6946_x1740_x472433961}

[[4]{lang="EN-US"}]{#struct_0_x6946_x1740_x869239008}

[[6]{lang="EN-US"}]{#struct_0_x6946_x1740_x631312283}

[[0]{lang="EN-US"}]{#struct_0_x6946_x1740_x1919956097}

[[AC-VI]{lang="EN-US"}]{#struct_0_x6946_x1740_x1226913005}

[[1]{lang="EN-US"}]{#struct_0_x6946_x1740_x2113068211}

[[3]{lang="EN-US"}]{#struct_0_x6946_x1740_x907793568}

[[4]{lang="EN-US"}]{#struct_0_x6946_x1740_x190874392}

[[94]{lang="EN-US"}]{#struct_0_x6946_x1740_x1215891172}

[[AC-VO]{lang="EN-US"}]{#struct_0_x6946_x1740_x1843076868}

[[1]{lang="EN-US"}]{#struct_0_x6946_x1740_x1832312949}

[[2]{lang="EN-US"}]{#struct_0_x6946_x1740_x2014327410}

[[3]{lang="EN-US"}]{#struct_0_x6946_x1740_474844833}

[[47]{lang="EN-US"}]{#struct_0_x6946_x1740_1954075695}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_637394433}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_220916370}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_334865005}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x57853031}

[[network-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_x1521941922}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_2032712430}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_1140060594}

[**[ac-be]{lang="EN-US"}**]{#struct_0_x6946_x1740_x276992927}[：]{style="font-family:宋体"}[AC-BE]{lang="EN-US"}[（尽力而为流）优先级队列。]{style="font-family:宋体"}

[**[ac-bk]{lang="EN-US"}**]{#struct_0_x6946_x1740_x1769870312}[：]{style="font-family:宋体"}[AC-BK]{lang="EN-US"}[（背景流）优先级队列。]{style="font-family:宋体"}

[**[ac-vi]{lang="EN-US"}**]{#struct_0_x6946_x1740_528095840}[：]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[（视频流）优先级队列。]{style="font-family:宋体"}

[**[ac-vo]{lang="EN-US"}**]{#struct_0_x6946_x1740_735494287}[：]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[（语音流）优先级队列。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6946_x1740_1985225533}[：所有]{style="font-family:宋体"}[EDCA]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[**[aifsn]{lang="EN-US"}***[ aifsn-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x1490895176}[：仲裁帧间隙数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ecwmin]{lang="EN-US"}***[ ecwmin-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x760250493}[：最小竞争窗口指数形式，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ecwmax]{lang="EN-US"}***[ ecwmax-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_1486758042}[：最大竞争窗口指数形式，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}**[ecwmax]{lang="EN-US"}**[值必须大于等于]{style="font-family:宋体"}**[ecwmin]{lang="EN-US"}**[值。]{style="font-family:宋体"}

[**[noack]{lang="EN-US"}**]{#struct_0_x6946_x1740_x2117807555}[：指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[使用的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[策略是]{style="font-family:宋体"}[No ACK]{lang="EN-US"}[。缺省]{style="font-family:宋体"}[ACK]{lang="EN-US"}[策略为]{style="font-family:宋体"}[No ACK]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[txoplimit]{lang="EN-US"}***[ txoplimit-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_657410429}[：]{style="font-family:宋体"}[EDCA]{lang="EN-US"}[的]{style="font-family:宋体"}[TXOP Limit]{lang="EN-US"}[参数，以]{style="font-family:宋体"}[32]{lang="EN-US"}[微秒为单位，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示只允许传输一个]{style="font-family:宋体"}[MPDU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_1891953045}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_243933617}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[802.11b]{lang="EN-US"}]{#struct_0_x6946_x1740_x1857994074}[类型的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[，建议将]{style="font-family:宋体"}[AC-BK]{lang="EN-US"}[、]{style="font-family:宋体"}[AC-BE]{lang="EN-US"}[、]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[、]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[的]{style="font-family:宋体"}[TXOP Limit]{lang="EN-US"}[参数的值分别配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:
宋体"}[188]{lang="EN-US"}[和]{style="font-family:宋体"}[102]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_862478576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1130619202}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1911558258}[配置]{style="font-family:宋体"}[Radio]{lang="EN-US"}[使用的]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[队列的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x680277454}

[\[Sysname\] wlan ap ap1 model ]{lang="IT"}[WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="IT"}[edca radio ac-vo aifsn 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1810017558}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_1268742595}[配置]{style="font-family:宋体"}[Radio]{lang="EN-US"}[使用的]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[队列的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x562635437}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\]]{lang="EN-US"}[ ]{lang="EN-US"}[edca radio ac-vo aifsn 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1627559797}[设备举例]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_1249556059}[配置]{style="font-family:宋体"}[Radio]{lang="EN-US"}[使用的]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[队列的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_1729070990}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="IT"}

[\[Sysname-WLAN-Radio1/0/1\] ]{lang="IT"}[edca radio ac-vo aifsn 2]{lang="EN-US"}

::: {#1965224752 .myid}
[]{#_Toc404795140}[]{#struct_0_x6946_x1740_423272981}[]{#_Toc373753295}[]{#_Toc366004713}

**WLAN QoS \-- WLAN QoS命令 \-- reset wlan wmm**

------------------------------------------------------------------------

[**[reset wlan wmm]{lang="EN-US"}**]{#struct_0_x6946_x1740_995373241}[命令用来清空]{style="font-family:宋体"}[WMM]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_1138514307}

[**[reset wlan wmm ]{lang="EN-US"}**[{ **client** { **all** \| **ap** *ap-name* \| **mac-address** *mac-address* } \| **radio** { **all** \| **ap** *ap-name* } }]{lang="EN-US"}]{#struct_0_x6946_x1740_1292517900}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1615999835}

[[用户]{style="font-family:宋体"}]{#struct_0_x6946_x1740_x1331209296}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x275156735}

[[network-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_x920732259}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_245164718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_731900045}

[**[client]{lang="EN-US"}**]{#struct_0_x6946_x1740_1823599522}[：清除客户端的]{style="font-family:宋体"}[WMM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6946_x1740_x2040574802}[：清除所有]{style="font-family:宋体"}[Radio]{lang="EN-US"}[或客户端的]{style="font-family:宋体"}[WMM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_x6946_x1740_x1072380530}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x6946_x1740_2059227743}[：清除指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的客户端]{style="font-family:宋体"}[WMM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**]{#struct_0_x6946_x1740_2026694669}[：清除]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的]{style="font-family:宋体"}[WMM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_885806487}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_1284664369}[清空]{style="font-family:宋体"}[WMM]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset wlan wmm radio all]{lang="IT"}]{#struct_0_x6946_x1740_x1910290026}
:::

::: {#228602023 .myid}
[]{#_Toc404795141}[]{#struct_0_x6946_x1740_x270480087}

**WLAN QoS \-- WLAN QoS命令 \-- svp**

------------------------------------------------------------------------

[**[svp map-ac]{lang="EN-US"}**]{#struct_0_x6946_x1740_x248184185}[命令用来配置]{style="font-family:宋体"}[SVP]{lang="EN-US"}[映射功能，即将]{style="font-family:宋体"}[SVP]{lang="EN-US"}[报文放入指定的]{style="font-family:宋体"}[AC]{lang="EN-US"}[队列中。]{style="font-family:宋体"}

[**[undo svp map-ac]{lang="EN-US"}**]{#struct_0_x6946_x1740_144522839}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1683560217}

[**[svp map-ac]{lang="EN-US"}**[ { **ac-vi** \| **ac-vo** }]{lang="EN-US"}]{#struct_0_x6946_x1740_613153631}

[**[undo svp map-ac]{lang="EN-US"}**]{#struct_0_x6946_x1740_x2069688934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_767066376}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1725434851}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1726968487}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[SVP]{lang="EN-US"}[映射功能处于关闭状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_1839012713}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[SVP]{lang="EN-US"}[映射功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1357334304}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1795019828}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1678160602}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1025949538}

[[network-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_x141420147}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_x229938760}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1147558257}

[**[ac-vi]{lang="EN-US"}**]{#struct_0_x6946_x1740_140389643}[：]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[（视频流）优先级队列。]{style="font-family:宋体"}

[**[ac-vo]{lang="EN-US"}**]{#struct_0_x6946_x1740_2130054169}[：]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[（语音流）优先级队列。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_264910388}

[[SVP]{lang="EN-US"}]{#struct_0_x6946_x1740_x555564448}[映射只针对非]{style="font-family:宋体"}[WMM]{lang="EN-US"}[客户端接入，对]{style="font-family:宋体"}[WMM]{lang="EN-US"}[客户端不起作用。]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x159350910}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x52489587}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1345188393}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1936153591}[配置]{style="font-family:宋体"}[SVP]{lang="EN-US"}[映射功能，即将]{style="font-family:宋体"}[SVP]{lang="EN-US"}[报文放入]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[队列中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x23392431}

[\[Sysname\] wlan ap ap1 model ]{lang="IT"}[WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] ]{lang="IT"}[svp map-ac ac-vo]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1050502671}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x2116011213}[配置]{style="font-family:宋体"}[SVP]{lang="EN-US"}[映射功能，即将]{style="font-family:宋体"}[SVP]{lang="EN-US"}[报文放入]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[队列中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6946_x1740_1428306638}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN-radio-1\] svp map-ac ac-vo]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x2021111088}[设备举例]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1433636445}[配置]{style="font-family:宋体"}[SVP]{lang="EN-US"}[映射功能，即将]{style="font-family:宋体"}[SVP]{lang="EN-US"}[报文放入]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[队列中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_1993351534}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="IT"}

[\[Sysname-WLAN-Radio1/0/1\] ]{lang="IT"}[svp map-ac ac-vo]{lang="EN-US"}
:::

::: {#1343888514 .myid}
[]{#_Toc404795142}[]{#struct_0_x6946_x1740_634785933}

**WLAN QoS \-- WLAN QoS命令 \-- wmm**

------------------------------------------------------------------------

[**[wmm]{lang="EN-US"}**]{#struct_0_x6946_x1740_492191951}[命令用来开启]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **wmm**]{lang="EN-US"}]{#struct_0_x6946_x1740_224671494}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1966775090}

[**[wmm]{lang="EN-US"}**[ { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_x6946_x1740_738519182}

[**[undo wmm]{lang="EN-US"}**]{#struct_0_x6946_x1740_1336145181}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1780101651}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1678380684}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x188469874}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能处于开启状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1491594062}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能处于开启状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1197205811}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x2087445516}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_2005039681}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_704983252}

[[network-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_1098859040}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_1618361910}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1411149653}

[**[disable]{lang="EN-US"}**]{#struct_0_x6946_x1740_x1534717915}[：]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[enable]{lang="EN-US"}**]{#struct_0_x6946_x1740_1038827831}[：]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x489114045}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1406667495}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[协议要求]{style="font-family:宋体"}[802.11n]{lang="EN-US"}]{#struct_0_x6946_x1740_394037619}[的客户端必须支持]{style="font-family:宋体"}[WLAN QoS]{lang="EN-US"}[，所以当]{style="font-family:宋体"}[Radio]{lang="EN-US"}[工作在]{style="font-family:宋体"}[802.11an]{lang="EN-US"}[或]{style="font-family:宋体"}[802.11gn]{lang="EN-US"}[的情况下，]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能必须开启，否则可能会导致关联后的]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[的客户端无法通信]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1977516198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_338329984}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_126357136}[关闭]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6946_x1740_x766230931}

[\[Sysname\] ]{lang="EN-US"}[wlan ap ap1 model ]{lang="IT"}[WA4620i-ACN]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[wlan-ap-ap1]{lang="IT"}[\] ]{lang="EN-US"}[radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] wmm disable]{lang="IT"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x428531552}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1322215860}[关闭]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x1677995009}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1\] wmm disable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1173463405}[设备举例]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1315731149}[关闭]{style="font-family:宋体"}[WMM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x1177761010}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="IT"}

[\[Sysname-WLAN-Radio1/0/1\] wmm disable]{lang="IT"}
:::

::: {#-154405993 .myid}
[]{#_Toc404795143}[]{#struct_0_x6946_x1740_x1107699465}

**WLAN QoS \-- WLAN QoS命令 \-- wmm edca client（ac-be和ac-bk）**

------------------------------------------------------------------------

[**[wmm edca client]{lang="EN-US"}**]{#struct_0_x6946_x1740_1735573219}[命令用来配置]{style="font-family:宋体"}[Radio]{lang="EN-US"}[和客户端的协商参数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo wmm edca client]{lang="EN-US"}**]{#struct_0_x6946_x1740_x43808495}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1180889282}

[**[wmm edca client]{lang="EN-US"}**[ { **ac-be** \| **ac-bk** } { **aifsn** *aifsn-value* \| **ecw** **ecwmin** *ecwmin-value* **ecwmax** *ecwmax-value* \| **txoplimit** *txoplimit-value* } \*]{lang="EN-US"}]{#struct_0_x6946_x1740_x516555538}

[**[undo wmm edca client]{lang="EN-US"}**[ { **ac-be** \| **ac-bk** } { **aifsn** \| **all** \| **ecw** \| **txoplimit** }]{lang="EN-US"}]{#struct_0_x6946_x1740_x526569393}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_1004608178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_243868081}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x1193932579}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](?-154405993#_Ref171155503)[所示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x585636386}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[如]{lang="EN-US" style="font-family:宋体"}[[[表]{style="font-family:宋体"}1-2]{lang="EN-US"}](?-154405993#_Ref171155503)[所示]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[]{#struct_0_x6946_x1740_829674015}[[表1-2 ]{lang="EN-US"}[Radio]{lang="EN-US"}]{#_Ref171155503}[和客户端的协商参数的缺省值]{style="font-family:黑体"}

[]{#table_struct_0_x1718963857}[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_2005234222}
:::

[[AIFSN]{lang="EN-US"}]{#struct_0_x6946_x1740_1692441077}

[[ECWmin]{lang="EN-US"}]{#struct_0_x6946_x1740_432399244}

[[ECWmax]{lang="EN-US"}]{#struct_0_x6946_x1740_1776355014}

[[TXOP Limit ]{lang="EN-US"}]{#struct_0_x6946_x1740_x339569927}

[[AC-BK]{lang="EN-US"}]{#struct_0_x6946_x1740_x868347217}

[[7]{lang="EN-US"}]{#struct_0_x6946_x1740_2037403937}

[[4]{lang="EN-US"}]{#struct_0_x6946_x1740_x311788100}

[[10]{lang="EN-US"}]{#struct_0_x6946_x1740_x809732200}

[[0]{lang="EN-US"}]{#struct_0_x6946_x1740_1356990543}

[[AC-BE]{lang="EN-US"}]{#struct_0_x6946_x1740_x568712210}

[[3]{lang="EN-US"}]{#struct_0_x6946_x1740_287836827}

[[4]{lang="EN-US"}]{#struct_0_x6946_x1740_1060012808}

[[10]{lang="EN-US"}]{#struct_0_x6946_x1740_1289156550}

[[0]{lang="EN-US"}]{#struct_0_x6946_x1740_2100256910}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_1201864798}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x303368875}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1014655520}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1764233923}

[[network-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_571605522}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_888951283}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_766551937}

[**[ac-be]{lang="EN-US"}**]{#struct_0_x6946_x1740_x85718658}[：]{style="font-family:宋体"}[AC-BE]{lang="EN-US"}[（尽力而为流）优先级队列。]{style="font-family:宋体"}

[**[ac-bk]{lang="EN-US"}**]{#struct_0_x6946_x1740_341596}[：]{style="font-family:宋体"}[AC-BK]{lang="EN-US"}[（背景流）优先级队列。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6946_x1740_x1656324511}[：所有]{style="font-family:宋体"}[EDCA]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[**[aifsn]{lang="EN-US"}***[ aifsn-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x1622490074}[：仲裁帧间隙数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ecwmin]{lang="EN-US"}***[ ecwmin-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x811145590}[：最小竞争窗口指数形式，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ecwmax]{lang="EN-US"}***[ ecwmax-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x1475203100}[：最大竞争窗口指数形式，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}**[ecwmax]{lang="EN-US"}**[值必须大于等于]{style="font-family:宋体"}**[ecwmin]{lang="EN-US"}**[值。]{style="font-family:宋体"}

[**[txoplimit]{lang="EN-US"}***[ txoplimit-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x1439726805}[：传输机会限制，以]{style="font-family:宋体"}[32]{lang="EN-US"}[微秒为单位，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示只允许传输一个]{style="font-family:宋体"}[MPDU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_2053989743}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1194149760}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果所有客户端都是]{style="font-family:宋体"}]{#struct_0_x6946_x1740_x1029226723}[802.11b]{lang="EN-US"}[客户端，建议将]{style="font-family:宋体"}[AC-BK]{lang="EN-US"}[、]{style="font-family:宋体"}[AC-BE]{lang="EN-US"}[的]{style="font-family:宋体"}[TXOP Limit]{lang="EN-US"}[参数的值分别配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果网络中同时存在]{style="font-family:宋体"}]{#struct_0_x6946_x1740_823669036}[802.11b]{lang="EN-US"}[客户端和]{style="font-family:宋体"}[802.11g]{lang="EN-US"}[客户端，则建议按]{style="font-family:宋体"}[TXOP Limit]{lang="EN-US"}[参数值使用]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-2]{lang="EN-US"}](?-154405993#_Ref171155503)[中缺省值。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x455463320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1003382968}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x320760646}[配置]{style="font-family:宋体"}[AC-BE]{lang="EN-US"}[的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_1972109687}

[\[Sysname\] wlan ap ap1 model ]{lang="IT"}[WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] wmm ]{lang="IT"}[edca client ac-be aifsn 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x246269227}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1281807843}[配置]{style="font-family:宋体"}[AC-BE]{lang="EN-US"}[的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x1725500387}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1\] wmm edca client ac-be aifsn 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x681877867}[设备举例]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_442803004}[配置]{style="font-family:宋体"}[AC-BE]{lang="EN-US"}[的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_282861273}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="IT"}

[\[Sysname-WLAN-Radio1/0/1\] wmm ]{lang="IT"}[edca client ac-be aifsn 5]{lang="EN-US"}

::: {#-1211716778 .myid}
[]{#_Toc404795144}[]{#struct_0_x6946_x1740_1292704621}[]{#_Toc402880633}

**WLAN QoS \-- WLAN QoS命令 \-- wmm edca client（ac-vo和ac-vi）**

------------------------------------------------------------------------

[**[wmm edca client]{lang="EN-US"}**]{#struct_0_x6946_x1740_1086007994}[命令用来配置]{style="font-family:宋体"}[Radio]{lang="EN-US"}[和客户端的协商参数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo wmm edca client]{lang="EN-US"}**]{#struct_0_x6946_x1740_x1076570822}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1824900257}

[**[wmm edca client]{lang="EN-US"}**[ { **ac-vi** \| **ac-vo** } { **aifsn** *aifsn-value* \| **cac** \| **ecw** **ecwmin** *ecwmin-value* **ecwmax** *ecwmax-value* \| **txoplimit** *txoplimit-value* } \*]{lang="EN-US"}]{#struct_0_x6946_x1740_x1384595604}

[**[undo wmm edca client]{lang="EN-US"}**[ { **ac-vo** \| **ac-vi** } { **aifsn** \| **all** \| **cac** \| **ecw** \| **txoplimit** }]{lang="EN-US"}]{#struct_0_x6946_x1740_x2101657061}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1843011332}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x159416446}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x2089535765}[设备：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?-1211716778#_Ref168914192)[所示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_x1821745177}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[下，]{style="font-family:宋体"}[如]{lang="EN-US" style="font-family:宋体"}[[[表]{style="font-family:宋体"}1-3]{lang="EN-US"}](?-1211716778#_Ref168914192)[所示]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[]{#struct_0_x6946_x1740_x764957468}[[表1-3 ]{lang="EN-US"}[Radio]{lang="EN-US"}]{#_Ref168914192}[和客户端的协商参数的缺省值]{style="font-family:黑体"}

[]{#table_struct_0_x1716711405}[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1178685923}
:::

[[AIFSN]{lang="EN-US"}]{#struct_0_x6946_x1740_255562388}

[[ECWmin]{lang="EN-US"}]{#struct_0_x6946_x1740_x106710280}

[[ECWmax]{lang="EN-US"}]{#struct_0_x6946_x1740_424079757}

[[TXOP Limit ]{lang="EN-US"}]{#struct_0_x6946_x1740_x456660942}

[[AC-VI]{lang="EN-US"}]{#struct_0_x6946_x1740_1525478095}

[[2]{lang="EN-US"}]{#struct_0_x6946_x1740_359585852}

[[3]{lang="EN-US"}]{#struct_0_x6946_x1740_x2084787736}

[[4]{lang="EN-US"}]{#struct_0_x6946_x1740_1354495290}

[[94]{lang="EN-US"}]{#struct_0_x6946_x1740_x786506355}

[[AC-VO]{lang="EN-US"}]{#struct_0_x6946_x1740_x276927391}

[[2]{lang="EN-US"}]{#struct_0_x6946_x1740_x238073356}

[[2]{lang="EN-US"}]{#struct_0_x6946_x1740_2119128645}

[[3]{lang="EN-US"}]{#struct_0_x6946_x1740_x1582785257}

[[47]{lang="EN-US"}]{#struct_0_x6946_x1740_381623231}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x678489302}

[[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x267523829}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_1181974260}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_985286841}

[[network-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_538830968}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6946_x1740_x14797236}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_669001847}

[**[ac-vi]{lang="EN-US"}**]{#struct_0_x6946_x1740_1762629200}[：]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[（视频流）优先级队列。]{style="font-family:宋体"}

[**[ac-vo]{lang="EN-US"}**]{#struct_0_x6946_x1740_988029772}[：]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[（语音流）优先级队列。]{style="font-family:宋体"}

[**[aifsn]{lang="EN-US"}***[ aifsn-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x680211918}[：仲裁帧间隙数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6946_x1740_822261987}[：所有]{style="font-family:宋体"}[EDCA]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[**[cac]{lang="EN-US"}**]{#struct_0_x6946_x1740_852059809}[：支持客户端使用连接准入控制。]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[和]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[支持]{style="font-family:宋体"}[CAC]{lang="EN-US"}[，缺省为关闭。]{style="font-family:宋体"}

[**[ecwmin]{lang="EN-US"}***[ ecwmin-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_x989400588}[：最小竞争窗口指数形式，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ecwmax]{lang="EN-US"}***[ ecwmax-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_1377060082}[：最大竞争窗口指数形式，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}**[ecwmax]{lang="EN-US"}**[值必须大于等于]{style="font-family:宋体"}**[ecwmin]{lang="EN-US"}**[值。]{style="font-family:宋体"}

[**[txoplimit]{lang="EN-US"}***[ txoplimit-value]{lang="EN-US"}*]{#struct_0_x6946_x1740_1150563583}[：传输机会限制，以]{style="font-family:宋体"}[32]{lang="EN-US"}[微秒为单位，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示只允许传输一个]{style="font-family:宋体"}[MPDU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_1957217957}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_x662375143}[设备：]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图下配置的优先级高于]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果所有上线客户端都是]{style="font-family:宋体"}]{#struct_0_x6946_x1740_1556441093}[802.11b]{lang="EN-US"}[客户端，建议将]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[、]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[的]{style="font-family:宋体"}[TXOP Limit]{lang="EN-US"}[参数的值分别配置为]{style="font-family:宋体"}[188]{lang="EN-US"}[、]{style="font-family:宋体"}[102]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果网络中同时存在]{style="font-family:宋体"}]{#struct_0_x6946_x1740_2076618746}[802.11b]{lang="EN-US"}[客户端和]{style="font-family:宋体"}[802.11g]{lang="EN-US"}[客户端，则建议按]{style="font-family:宋体"}[TXOP Limit]{lang="EN-US"}[参数值使用]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-3]{lang="EN-US"}](?-1211716778#_Ref168914192)[中缺省值。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某优先级队列的]{style="font-family:宋体"}]{#struct_0_x6946_x1740_x452819980}[CAC]{lang="EN-US"}[功能被启动，则高于此优先级队列的]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能会同时被启用。例如，使用]{style="font-family:宋体"}**[wmm edca client]{lang="EN-US"}**[命令启动]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[优先级]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能，则]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[优先级也同时启动]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能，但是，启动]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[优先级的]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能，]{style="font-family:宋体"}[AC-VI]{lang="EN-US"}[优先级的]{style="font-family:宋体"}[CAC]{lang="EN-US"}[功能不会被启用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6946_x1740_x1389223086}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_1406864103}[设备举例（]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1006260363}[配置]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x255831817}

[\[Sysname\] wlan ap ap1 model ]{lang="IT"}[WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] radio 1]{lang="IT"}

[\[Sysname-wlan-ap-ap1-radio-1\] wmm ]{lang="IT"}[edca client ac-vo aifsn 3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_x6946_x1740_346092878}[设备举例（]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[Radio]{lang="EN-US"}[视图）]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x1322019252}[配置]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_1985866447}

[\[Sysname\] wlan ap-group apgroup1]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1\] ap-model WA4620i-ACN]{lang="EN-US"}

[\[Sysname-wlan-ap]{lang="EN-US"}[-group]{lang="EN-US"}[-apgroup1-ap-model-WA4620i-ACN\] radio 1]{lang="EN-US"}

[\[Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1\] wmm edca client ac-vo aifsn 3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAT AP]{lang="EN-US"}]{#struct_0_x6946_x1740_1242652580}[设备举例]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6946_x1740_x584557978}[配置]{style="font-family:宋体"}[AC-VO]{lang="EN-US"}[的]{style="font-family:宋体"}[AIFSN]{lang="EN-US"}[值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x6946_x1740_x1838112096}

[\[Sysname\] interface wlan-radio 1/0/1]{lang="IT"}

[\[Sysname-WLAN-Radio1/0/1\] wmm ]{lang="IT"}[edca client ac-vo aifsn 3]{lang="EN-US"}

[ ]{lang="EN-US"}
